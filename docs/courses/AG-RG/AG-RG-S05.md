# Artin approximation for polynomial equations and its desingularization proof

*Written by GPT-6.1 Sol (OpenAI), Codex, Ultra. Self-checked by the writing AI. CC0 1.0.*

A formal solution satisfies polynomial equations in a completion. Approximation asks for an exact solution on an étale neighbourhood with the same prescribed finite-order values. To keep both requirements, we encode the equations and the congruences in a single finite presentation.

The proof proceeds from smooth factorization to a pointed étale neighbourhood. Sections 1–3 give that passage and the finite coefficient system for an embedded torus. Section 4 proves the desingularization theorem that supplies the smooth factorization; Section 5 contains the algebra used in its proof.

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
\(R/\mathfrak m^{r+1}\to R/\mathfrak m^r\) is \(\mathfrak m^r/\mathfrak m^{r+1}\).
Its square is zero because \(2r\geq r+1\). Formal etaleness gives a unique lift of the already chosen map at each step. Denote these compatible \(R\)-maps by \(\phi_r:R'\to R/\mathfrak m^r\). By definition \(\widehat R=\varprojlim_r R/\mathfrak m^r\): it is the subring of the product formed by compatible tuples, with addition and multiplication componentwise. Therefore \(x\mapsto(\phi_r(x))_r\) is an \(R\)-algebra map \(R'\to\widehat R\), inducing the specified residue map. Conversely any such map, composed with the coordinate projections \(\widehat R\to R/\mathfrak m^r\), gives these same \(\phi_r\) by induction and formal uniqueness. Its value on every \(x\) is consequently the same tuple. This proves existence and uniqueness using the inverse-limit definition alone, with no Noetherian or completion-quotient theorem needed for this lemma. Formal etaleness is part of the defining lifting property of an etale algebra in AG-CA-17; its nilpotent lifting criterion is Theorem 1.2 of that earlier lesson. ∎

**Lemma 1.3 (a smooth residue-field point has an étale lift).** If \(B\) is a smooth finitely presented \(R\)-algebra and \(B\to\kappa=R/\mathfrak m\) is an \(R\)-map, there are a finitely presented étale \(R\)-algebra \(R'\), a point \(R'\to\kappa\), and an \(R\)-map \(B\to R'\) inducing the original point.

**Proof.** Use the local standard form proved in AG-CA, Formally smooth, unramified and étale ring maps, Theorem 5.1. At the kernel of the given point, localize once to write

\[
B_g=R[X_1,\ldots,X_s]/(h_1,\ldots,h_c),
\qquad
\Delta=\det(\partial h_i/\partial X_j)_{i,j\leq c}
\quad\text{a unit}.
\]

This presentation includes any localization variable and its equation. Choose \(r_{c+1},\ldots,r_s\in R\) lifting the point's coordinates in the remaining variables. Substitute these elements in the equations, keeping the first \(c\) variables, and invert the substituted \(\Delta\) and the original denominators. Call the resulting finitely presented algebra \(R'\). Here is its entire lifting test. Given a map \(R'\to D/J\) with \(J^2=0\), lift its variable values to a vector \(x\in D^c\). The inverted polynomials stay units: if \(uv=1+j\) with \(j\in J\), then \(u\) has inverse \(v(1-j)\). The equation errors form a vector \(h(x)\in J^c\), and the Jacobian \(H(x)\) is invertible by its unit determinant and the cofactor identity. Taylor expansion of each monomial, dropping every product of two elements of \(J\), gives \(h(x+z)=h(x)+H(x)z\) for \(z\in J^c\). Thus \(z=-H(x)^{-1}h(x)\) gives a solution. If \(y\) is any second lifted solution, the same identity gives \(H(x)(y-x)=0\), so \(y=x\). The inverse variables are then forced by the unit equations. For \(J^N=0\), repeat this unique lifting through \(D/J^{r+1}\to D/J^r\), whose kernel is square-zero for \(r\geq1\). This proves formal etaleness, including \(c=0\); finite presentation proves etaleness by the earlier programme definition. This is the square-Jacobian specialization of AG-CA-17, Theorem 4.1, with uniqueness proved here as well. The original residue coordinates define \(R'\to\kappa\), because all inverted elements have nonzero residues. Its kernel is maximal with residue field \(\kappa\), since \(R\to\kappa\) is surjective. Substitution gives \(B_g\to R'\), hence \(B\to R'\), inducing exactly the original point. ∎

**Proof of Theorem 1.1.** The equality $R/\mathfrak m^N\simeq\widehat R/\mathfrak m^N\widehat R$ is proved in the earlier AG-CA lesson *Completion*, Proposition 2.2. Choose \(c_i\in R\) representing \(\widehat a_i\) modulo \(\mathfrak m^N\widehat R\), and choose finitely many generators \(d_1,\ldots,d_M\) of \(\mathfrak m^N\). Write

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

**Proof.** The section criterion proved in [AG-CA, Henselian local rings and henselization, Theorem 1.2](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/AG-CA/henselian-local-rings-and-henselization.html#1-roots-and-maps-with-a-prescribed-residue) gives \(R'\to R\) with the specified residue map. Its composition with \(R\to\widehat R\) is the map \(\rho\) by Lemma 1.2, so (1.1) is preserved. For \(R^h\), use the pointed étale colimit and its universal property proved in that lesson, Lemma 4.1 and Theorem 4.2. Compatibility with the map into the complete henselian ring follows from the same uniqueness. Here the principal monic chart consumed by that section-criterion proof is supplied by the full [earlier structural étale proof, Lemma D2.2](AG-RG-S04.md), whose integral closure input is [the affine conductor theorem, Theorem C4.3](AG-RG-S04.md). Its polynomial normality input is proved in [the preliminary coefficient argument, Corollary B1.2](AG-RG-S04.md). To spell out the actual section step, localize the selected étale algebra
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
Here a torus is etale locally a product of copies of \(\mathbf G_m\). Starting instead with the fpqc multiplicative-type definition gives this same condition by AG-GS-05, Theorem 7.7; its finite torsion-free character-group step is proved in [AG-RG-S04, Lemma P0.10](AG-RG-S04.md#finite-torsion-free-lattices). Every torus therefore has such a chart and residue point: choose an affine finite-presentation part of an etale splitting cover meeting the closed fibre, and a closed point of that fibre. Its residue field is finite over \(\kappa\) by the finite-type field-algebra argument in AG-RG-S04, Lemma P0.9. The quotient sequence for differentials gives \(\Omega_{K/\kappa}=0\), because the chart is formally unramified. The finite-field differential calculation in AG-CA-17, Lemma 7.1 then proves separability.

Furthermore, a torus \(T_0/\kappa\), with character lattice split by \(L\), has a torus lift over \(A\) split by this same \(E\). Its character lattice and descent action reduce compatibly modulo every \(\mathfrak m^n\).

**Proof.** A finite separable extension embeds in a finite normal separable extension: adjoin all the roots of the minimal polynomials of a finite generating list. The finite splitting-field construction and separable-tower calculations of AG-RG-S02, Lemma 4.A, prove finiteness and separability. Every embedding permutes the root sets, so the resulting extension \(L/\kappa\) is normal. The same embedding count gives \(|\Gamma|=[L:\kappa]\). We give the whole primitive-element step here. Write \(n=[L:\kappa]\), choose a finite generating list \(b_1,\ldots,b_s\), and list the \(n\) embeddings \(\sigma_i\) into a finite splitting field. If \(\kappa\) is infinite, every pair of distinct embeddings differs on some generator, so \(\sum_j(\sigma_i(b_j)-\sigma_{i'}(b_j))X_j\) is a nonzero polynomial. Their finite product is nonzero, because a polynomial ring over a field is a domain, as follows by multiplying leading coefficients successively in each variable. It cannot vanish on every tuple in \(\kappa^s\): induction on the variables first makes a nonzero coefficient polynomial nonzero and then avoids the finitely many roots in the last variable, using the root bound of Lemma 4.A. Choose such a tuple \((c_j)\). Then \(\alpha=\sum_j c_jb_j\) has \(n\) different embedding images. Its minimal polynomial has at least \(n\) roots, hence degree at least \(n\); the tower-degree formula bounds that degree by \(n\), so \(L=\kappa(\alpha)\). If \(\kappa\) is finite, a finite basis makes \(L\) a finite set. The complete cyclic-subgroup calculation of Lemma 4.A makes \(L^\times\) cyclic. A generator \(\alpha\) generates \(L\) as a field because every nonzero element is its power. Degree one is included by choosing \(\alpha=1\). Let \(\bar f\in\kappa[X]\) be the monic minimal polynomial of this \(\alpha\), and lift its coefficients to a monic \(f\in A[X]\). Put
\[
E=A[t]=A[X]/(f),\qquad d=\deg(f).
\]
Successively subtracting leading multiples of the monic polynomial \(f\) reduces every polynomial to degree less than \(d\). A nonzero multiple \(qf\) has degree \(\deg(q)+d\), since its leading coefficient is the nonzero leading coefficient of \(q\). Thus the remainder is unique, and \(1,t,\ldots,t^{d-1}\) is a basis making \(E\) free of positive finite rank over \(A\); it is faithfully flat because tensoring a module with this free module gives a direct sum of \(d\) copies. Its quotient by \(\mathfrak mE\) is \(L\). If \(e\in E\) has nonzero residue, multiplication by \(e\) on this basis is invertible modulo \(\mathfrak m\). Its determinant is a unit of \(A\), and the cofactor calculation proved in Lemma 3.B gives an inverse to multiplication by \(e\). Thus \(e\) is a unit, \(E\) is local with maximal ideal \(\mathfrak mE\), and coordinatewise completeness gives
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

For the final assertion use the specified finite Galois field \(L\) splitting \(T_0\), so that the algebra \(E\) just constructed is the same one as in the statement. Its character group \(M\) is finite free by AG-RG-S04, Lemma P0.10, and the split character calculation of AG-GS-05, Theorem 2.2. The descent of \(T_0\) along \(L/\kappa\) gives its \(\Gamma\)-action on \(M\): pull back a character along each descent isomorphism; the cocycle gives the group law. Theorem 2.2 identifies these maps with the corresponding lattice maps. On \(E[M]\) put
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

<a id="finite-free-perfect-trace"></a>

**Lemma 3.B (perfect trace, over an arbitrary base).** Let $A$ be a commutative ring and $C$ a commutative $A$-algebra free of finite rank $d$. If the determinant of the pairing $(c,z)\mapsto\operatorname{Tr}_{C/A}(cz)$ is a unit, then $C/A$ is finitely presented and formally etale, hence etale. If $d>0$, it is faithfully flat. These assertions require no Noetherian, reducedness or characteristic hypothesis.

**Proof.** First, the elementary matrix identities used here hold over every commutative ring. Define a determinant by the signed permutation sum and a cofactor by the corresponding smaller signed determinant. Expanding along a row or column gives the determinant. A matrix with two equal rows or columns has determinant zero: pair each permutation with the permutation interchanging those positions; their contributions have opposite signs, including in characteristic two. Consequently, if $M$ is square, multiplying it on either side by its transposed cofactor matrix gives $(\det M)I$: a diagonal entry is the row or column expansion, and an off-diagonal entry is the expansion of a determinant with two equal rows or columns. A unit determinant therefore gives the inverse $(\det M)^{-1}\operatorname{adj}(M)$. For size zero the determinant is one. To verify the converse implication as well, expand $\det(UV)$ by multilinearity in its columns. The expansion chooses, for each column of $UV$, one column of $U$ with its coefficient from $V$. A tuple repeating a column of $U$ contributes zero by the cancellation just proved. Every remaining tuple is a permutation of all the columns of $U$, whose determinant is its permutation sign times $\det(U)$. Summing its coefficients with these signs is precisely $\det(V)$. Thus $\det(UV)=\det(U)\det(V)$, including for size zero. If $UV=I$, this equation gives $\det(U)\det(V)=1$, so an invertible matrix has a unit determinant. For square matrices $U,V$, the finite double sum also gives $\operatorname{tr}(UV)=\operatorname{tr}(VU)$. Thus conjugating a multiplication matrix by an invertible change of basis preserves its trace. Multiplication matrices, their traces and their determinants commute with every scalar extension, entry by entry.

Suppose first that $d>0$, and choose a basis $u_1,\ldots,u_d$. Write $u_i u_j=\sum_k m_{ijk}u_k$ and $1=\sum_i a_i u_i$. There is an explicit finite algebra presentation
$$
C=A[X_1,\ldots,X_d]/\bigl(X_iX_j-\sum_k m_{ijk}X_k,\;1-\sum_i a_iX_i\bigr).
$$
Indeed, repeatedly replace a product of two variables by the displayed linear combination, reducing each monomial to degree at most one. Replace its constant term by that constant times $\sum_i a_iX_i$. Every quotient element is therefore represented by $\sum_i b_iX_i$. The map to $C$ is surjective, and if this representative maps to zero, linear independence of the $u_i$ makes every $b_i$ zero. This proves the presentation without an assumption on ideals of $A$.

The inverse pairing matrix supplies a trace-dual basis $v_1,\ldots,v_d$, characterized by $\operatorname{Tr}(u_jv_i)=\delta_{ij}$. In particular $x=\sum_i u_i\operatorname{Tr}(v_ix)$ and $x=\sum_i\operatorname{Tr}(u_ix)v_i$. To check the second equality, pair both sides with each $u_j$ and use invertibility of the pairing; the first is the ordinary basis-coordinate equality. Put
$$
e=\sum_i u_i\otimes v_i\in C\otimes_A C.
$$
The $A$-linear map
$$
\Phi:C\otimes_A C\longrightarrow\operatorname{End}_A(C),\qquad
\Phi(a\otimes b)(x)=a\operatorname{Tr}(bx)
$$
is an isomorphism, with inverse $F\mapsto\sum_i F(u_i)\otimes v_i$. The first coordinate equality proves $\Phi\Phi^{-1}(F)=F$; the second proves $\Phi^{-1}\Phi(a\otimes b)=a\otimes b$, and pure tensors generate. Since $\Phi(e)$ is the identity, both $(c\otimes1)e$ and $(1\otimes c)e$ have image multiplication by $c$. Thus
$$
(c\otimes1)e=(1\otimes c)e\qquad(c\in C).
\tag{3.6}
$$
Let $s=\sum_i u_iv_i$. The diagonal coefficient of multiplication by $c$ in position $i$ is $\operatorname{Tr}(v_i c u_i)$. Summing those coefficients gives $\operatorname{Tr}(c)=\operatorname{Tr}(cs)$ for every $c$. Invertibility of the pairing now gives
$$
\sum_i u_iv_i=1.
\tag{3.7}
$$
No division by $d$, or assertion that $d$ is a unit, occurs.

We prove the lifting property directly. Let $J\subset D$ be a square-zero ideal of a commutative $A$-algebra, and let $\bar f:C\to D/J$ be an $A$-algebra map. The free-module lifting calculation in [AG-RG-S01, Lemma 1.0](AG-RG-S01.md#1-the-algebra-of-localization) gives an $A$-linear lift $l:C\to D$. Its value $l(1)$ is $1+j$ with $j\in J$, and has inverse $1-j$. Multiplying the whole lift by that inverse makes $l(1)=1$ while preserving $A$-linearity and its reduction. Give $J$ its $C$-module action via $\bar f$: multiply by any lift of $\bar f(c)$, which is independent of that lift because $J^2=0$.

The defect $b(c,z)=l(cz)-l(c)l(z)$ lies in $J$, is $A$-bilinear and has $b(c,1)=b(1,c)=0$. Associativity in $C$ and $D$ gives, by expanding the four terms,
$$
c\,b(z,t)-b(cz,t)+b(c,zt)-b(c,z)\,t=0.
\tag{3.8}
$$
Define the $A$-linear correction $h(c)=\sum_i u_i b(v_i,c)$ in $J$. Apply the $A$-linear map $a\otimes z\mapsto a b(z,t)$ to (3.6); it gives $c h(t)=\sum_i u_i b(cv_i,t)$. Using (3.8) with $(v_i,c,t)$ and then (3.7), we obtain
$$
c h(t)-h(ct)+h(c)t
=\sum_i u_i\bigl(b(v_ic,t)-b(v_i,ct)+b(v_i,c)t\bigr)
=\sum_i u_iv_i b(c,t)=b(c,t).
$$
Consequently $f=l+h$ is multiplicative: the defect of this new map is $b(c,t)+h(ct)-c h(t)-h(c)t=0$, since $h(c)h(t)=0$. Also $h(1)=0$. Thus $f$ is a unital $A$-algebra lift of $\bar f$.

For uniqueness, the difference $\delta$ of two such lifts takes values in $J$ and satisfies $\delta(ct)=c\delta(t)+\delta(c)t$; expand their products and use $J^2=0$. Apply $a\otimes z\mapsto\delta(a)z$ to (3.6). The difference between its two sides is $\delta(c)\sum_i u_iv_i=\delta(c)$, by that identity and (3.7). It is zero, so every lift is unique. If $J^N=0$, lift successively through $D/J^{r+1}\to D/J^r$, for $1\le r<N$. Its kernel is square-zero because $2r\ge r+1$. Existence and uniqueness at each step prove formal etaleness for every nilpotent ideal. Together with the explicit finite presentation, this is etaleness by the programme definition.

For $d=0$, $C$ is the zero algebra with presentation $A/(1)$. If a unital map $C\to D/J$ exists and $J$ is nilpotent, then $D/J=0$, so $1\in J$ and nilpotence forces $D=0$. There is exactly one lift. Finally, for positive $d$, tensoring an $A$-module with $C$ gives $d$ copies of that module; this is exact and detects whether it is zero. This proves faithful flatness. $\square$

This is the finite-free case of the discriminant criterion in the freely accessible [Stacks Project, Lemma 49.3.1, Tag 0BJF](https://stacks.math.columbia.edu/tag/0BJF). The complete lifting proof above supplies the result used here.

Return to the splitting algebra $E/\widehat R$ from Lemma 3.A. Its trace determinant is a unit, as we now check rather than adding an unsupported inverse variable. By (3.2), after scalar extension from $\widehat R$ to $E$ the algebra becomes $\prod_{\sigma\in\Gamma}E$. Multiplication in this product is diagonal in the coordinate idempotent basis. Its trace pairing matrix is the identity, hence invertible. The preceding trace and basis-change calculations imply that the original pairing matrix becomes invertible over $E$, so its determinant $\Delta$ becomes a unit there. Then $(\widehat R/\Delta\widehat R)\otimes_{\widehat R}E=0$. Faithful flatness from Lemma 3.A detects zero modules, giving $\widehat R/\Delta\widehat R=0$, which means that $\Delta$ is already a unit of $\widehat R$.

Fix the finite free basis of $E$ supplied by Lemma 3.A. Its multiplication table, unit and multiplication matrices define finitely many coefficient variables; associativity, commutativity and the unit laws are finite polynomial equations. Add a variable $w$ and the equation $w\Delta=1$ for the trace determinant. The original completed coefficient tuple satisfies this equation by the preceding argument. After approximation it still satisfies the same equation exactly. Lemma 3.B makes the resulting finite free algebra etale and, since its unchanged rank is positive, faithfully flat.

Add coefficients for the finite presentations, Hopf maps, the isomorphism (3.1), its inverse, and the homomorphism to \(G\). Laurent expressions can be written polynomially by adding inverse variables and relations \(Z_iW_i=1\). The maps need to be specified on finite generating sets. Relations between their images need finitely many witnesses in the finitely generated relation ideals. The two composites of the splitting isomorphism and its inverse are tested on finite generators; equality of these composites with the identity is recorded by their witnesses. The same method records comultiplication, counit, inverse, and the homomorphism identities on a finite list of generators. Coassociativity and every needed descent identity are likewise checked on finite generators, using the finite multiplication tables on the finite overlap algebras. Each expression and witness has finite support.

Retain the closed immersion in this same system. The pullback \(\mathcal O(G_{\widehat R})\to\mathcal O(\widehat T)\) is surjective. Choose preimages of a finite list of algebra generators of \(\mathcal O(\widehat T)\), and include the equations asserting that their images are those generators. After approximation these equations still prove surjectivity; consequently the resulting homomorphism is a closed immersion.

We have obtained one finite polynomial system over the local model, solved by the original completed coefficient tuple. Apply Theorem 1.1 at order one. The defining equations hold exactly after approximation, while all the chosen coefficients retain their original residues. The preserved splitting maps identify the source Hopf algebra with a Laurent polynomial Hopf algebra on the finite étale faithfully flat cover. Thus it is a torus, with the specified special fibre and closed embedding. If a prescribed higher jet is needed, use that order instead. Lemma 2.1 spreads the data and the neighbourhood back to an open part of the finite-type model; base change returns them to the original base.

The local model is essentially of finite type over \(\mathbb Z\). The G-ring permanence argument in §5 is therefore a consumed part of this application, including its coefficient-ring inputs. It must be proved before the approximation step is declared complete. An excellence label or an external Stacks link does not replace this work.

**Scope of the supporting algebra.** The approximation theorem and the desingularization theorem concern Noetherian rings. Every base ring of the finite-type algebra diagrams in their proof is Noetherian. In the foundational complete-intersection arguments below we state and prove the exact Noetherian forms consumed there; arguments explicitly stated over arbitrary rings retain that wider scope. Polynomial presentations with arbitrarily many variables occur only in the two-term cotangent comparison, whose elementary presentation and filtered-colimit proofs are written without Noetherian assumptions. This distinction preserves arbitrary characteristic, imperfect residue fields, and the full Noetherian local G-ring statement.

## 4. Desingularization proof sequence

We prove approximation by passing through presentation changes, infinitesimal lifts and improvements of singular ideals. Local resolutions are constructed separately for separable and inseparable residue fields, then assembled into the smooth-colimit theorem. Smoothness throughout means the conormal condition [F.6](#algebra-definition-smooth). Each displayed list of arrows specifies the maps in the relevant commuting diagram.

### Singular ideals

<a id="smoothing-section-singular-ideal"></a>

The singular ideal records the complement of the smooth locus. Its radical formulation lets us compare smooth neighbourhoods across different finite presentations.

<a id="smoothing-definition-singular-ideal"></a>

#### Definition D.1: singular ideal

Reading source: [Stacks, Tag 07C5](https://stacks.math.columbia.edu/tag/07C5).

For any ring map $R\to A$, let $U_{A/R}$ be its smooth locus in $\operatorname{Spec}A$, with smoothness at a prime understood as in [F.7](#algebra-definition-smooth-at-prime). Its *singular ideal* $H_{A/R}$ is the radical ideal characterized by
$$V(H_{A/R})=\operatorname{Spec}A\setminus U_{A/R}.$$
No finite-presentation hypothesis on $A/R$, or quasi-compactness hypothesis on $U_{A/R}$, is part of this definition.

**Verification.** The definition of smoothness at a prime writes
$$U_{A/R}=\bigcup_{\substack{g\in A\\ R\to A_g\ \mathrm{smooth}}}D(g).$$
Indeed a witnessing $g$ gives smoothness at every prime avoiding it, and every smooth prime has such a witness. Thus $U_{A/R}$ is open. Write its closed complement as $V(J)$ and set $H_{A/R}=\sqrt J$. A prime contains $J$ exactly when it contains $\sqrt J$, since a power belonging to a prime forces its base element into that prime. This proves existence.

Here is the radical-ideal uniqueness argument used below. For any ideal $J$ and $x\notin\sqrt J$, the ideals containing $J$ and avoiding $\{1,x,x^2,\ldots\}$ have a maximal member $L$, by the chain-union argument and Zorn's lemma. If $uv\in L$ while $u,v\notin L$, maximality provides a power of $x$ in each of $L+(u)$ and $L+(v)$. Their product is again a power of $x$ and belongs to $L$, a contradiction. Hence $L$ is a prime containing $J$ and avoiding $x$. It follows that
$$\sqrt J=\bigcap_{\mathfrak q\in V(J)}\mathfrak q,$$
where the empty intersection is $A$. Two radical ideals with the same closed set are therefore equal. This also covers $A=0$ and an empty singular locus. The smooth open need not have a finite subcover, as the fully proved example [D.6](#smoothing-example-not-quasi-compact) shows. ∎

<a id="smoothing-lemma-find-strictly-standard"></a>

#### Lemma D.2: find strictly standard

Reading source: [AI Integrated Stacks, pinned smoothing, lines 141–181](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/smoothing.tex#L141-L181).

Fix a finite presentation
$$P=R[x_1,\ldots,x_n],\qquad I=(f_1,\ldots,f_m),\qquad A=P/I.$$
At a prime $\mathfrak q$ where $A/R$ is smooth, one can select equally many equations and variables, indexed by sets $V$ and $U$ of size $c\leq\min(n,m)$, and find $a,a'\in A$ such that
$$a\notin\mathfrak q,\qquad
a=a'\det(\partial f_j/\partial x_i)_{j\in V,\ i\in U},\qquad
\widetilde a f_\ell\in(f_j:j\in V)+I^2\quad(1\leq\ell\leq m).$$
Here $\widetilde a$ is any polynomial lift of $a$. The last condition is equivalently the relation $a[f_\ell]\in\langle[f_j]:j\in V\rangle$ in $I/I^2$.

**Proof.** The task is to choose a nonvanishing minor and then kill a finite conormal quotient. Let $M=I/I^2$ and $K=\kappa(\mathfrak q)$. Smoothness at the prime supplies $s\notin\mathfrak q$ with $A_s/R$ smooth, by [F.7](#algebra-definition-smooth-at-prime). The full comparison [F.11](#algebra-lemma-NL-homotopy), localization [F.65](#algebra-lemma-localize-NL), and definition [F.6](#algebra-definition-smooth) give
$$0\longrightarrow M_s\xrightarrow{\mathrm d}A_s^n
\longrightarrow\Omega_{A_s/R}\longrightarrow0.$$
This sequence splits because its quotient is projective. Consequently the differential on $M\otimes_A K$ is injective. The finite list $[f_j]$ spans that vector space; extract a basis from this list and call its index set $V$. If its length is $c$, injectivity implies $c\leq n$, while its construction implies $c\leq m$.

To justify a choice of $U$, use the following row calculation over $K$. When $c>0$, a nonzero entry in the first column supplies a pivot row. Subtract its multiples from the other rows. The lower block of the remaining $c-1$ columns is independent: a dependence there could be completed by a multiple of the first column to give a dependence of all $c$ columns. Induction selects $c-1$ lower rows with nonzero determinant. The determinant on these rows and the pivot row is the pivot times this nonzero determinant. Subtracting multiples of the pivot row did not change it, so it is a minor of the original columns. For $c=0$ use the determinant $1$. Thus the corresponding Jacobian minor $\delta$ belongs to $A\setminus\mathfrak q$.

Now form the finite $A$-module
$$Q=M/\langle[f_j]:j\in V\rangle.$$
Its residue at $\mathfrak q$ vanishes, and [F.10](#algebra-lemma-NAK) gives $Q_{\mathfrak q}=0$. For each generator of $Q$ choose a localization witness outside $\mathfrak q$ annihilating it. Their finite product $t$ annihilates $Q$ and still lies outside $\mathfrak q$; use $t=1$ when $Q=0$. Put $a=t\delta$ and $a'=t$. Then $aQ=0$ gives every stated conormal relation. Lifting its coefficients to $P$ gives the displayed polynomial-ideal relation. A different lift of $a$ changes its product with $f_\ell$ by an element of $I^2$, so the relation does not depend on that lift. No cancellation of $a$, $\delta$ or another possible zero divisor occurs. The empty equation and variable cases are included by the same construction. ∎

The next definition distinguishes witnesses using a single Jacobian minor from witnesses using a sum of minors. [D.15](#smoothing-lemma-compare-standard) compares these two conditions with smoothness after localization.

<a id="smoothing-definition-strictly-standard"></a>

#### Definition D.3: strictly standard

Reading source: [Stacks, Tag 07C7](https://stacks.math.columbia.edu/tag/07C7).

Let $R\to A$ be finitely presented. A witness for either standard-element condition consists of
$$P=R[x_1,\ldots,x_n],\qquad I=(f_1,\ldots,f_m),\qquad A=P/I,\qquad 0\leq c\leq\min(n,m).$$
All Jacobian entries below are reduced to $A$. For $a\in A$, choose any lift $\widetilde a\in P$ when writing a polynomial-ideal condition.

The element $a$ is *elementary standard* if some such witness and $a'\in A$ satisfy both

<a id="equation-elementary-standard-one"></a>

$$a=a'\det\left(\frac{\partial f_j}{\partial x_i}\right)_{i,j=1}^{c}\tag{D.3e1}$$

and

<a id="equation-elementary-standard-two"></a>

$$\widetilde a f_{c+j}\in(f_1,\ldots,f_c)+I^2\quad(1\leq j\leq m-c).\tag{D.3e2}$$

The element $a$ is *strictly standard* if some witness and coefficients $a_U\in A$, indexed by the $c$-element subsets of $\{1,\ldots,n\}$, satisfy both

<a id="equation-strictly-standard-one"></a>

$$a=\sum_{|U|=c}a_U\det\left(\frac{\partial f_j}{\partial x_i}\right)_{j=1,\ldots,c,\ i\in U}\tag{D.3s1}$$

and

<a id="equation-strictly-standard-two"></a>

$$\widetilde a f_{c+j}\in(f_1,\ldots,f_c)+I^2\quad(1\leq j\leq m-c).\tag{D.3s2}$$

Use increasing order on each selected variable set in the determinants. Changing the lift $\widetilde a$ adds an element of $I$; multiplying this difference by $f_{c+j}\in I$ puts it in $I^2$. Thus both relation conditions are independent of the lift. Equivalently they assert $a[f_{c+j}]\in\langle[f_1],\ldots,[f_c]\rangle$ in the $A$-module $I/I^2$. The minor condition and this relation condition are separate requirements.

For $c=0$ there is one minor, the empty determinant $1$, and the first equation imposes no restriction on $a$. The second equation then reads $\widetilde a I\subset I^2$. For $m=c$ the second equation has an empty list of tests. These conventions include empty polynomial presentations and the zero algebra. ∎

<a id="smoothing-lemma-parse-equation-strictly-standard-one"></a>

#### Lemma D.4: parse equation strictly standard one

Reading source: [Stacks, Tag 07ET](https://stacks.math.columbia.edu/tag/07ET).

In the presentation of [D.3](#smoothing-definition-strictly-standard), the strict minor condition for $a$ gives an $A$-linear map $\psi:A^n\to A^c$ for which the composite
$$A^c\xrightarrow{e_j\mapsto[f_j]}I/I^2\xrightarrow{\mathrm d}A^n\xrightarrow{\psi}A^c$$
is $a1_c$. Conversely the existence of this map gives the strict minor condition for $a^c$. These assertions concern the minor condition alone; the remaining-equation condition still has to be imposed independently.

**Proof.** Identify $A^n$ with the free differential module on $dx_1,\ldots,dx_n$. Its conormal map is well-defined: for $u,v\in I$, the product rule gives $d(uv)=u\,dv+v\,du$, which vanishes after reduction to $A$. The composite of its first two maps has the $n\times c$ matrix
$$M_{ij}=\frac{\partial f_j}{\partial x_i}\bmod I.$$
For a selected variable set $U$, let $E_U:A^n\to A^c$ be coordinate selection and put $M_U=E_UM$. The determinant in D.3s1 is $\det M_U$: transposition preserves the determinant by reversing the permutation indexing in its signed expansion.

The arbitrary-ring adjugate and determinant identities are proved in [F.70](#algebra-lemma-matrix-left-inverse). If $a=\sum_U a_U\det M_U$, they give the explicit map with matrix
$$B=\sum_U a_U\operatorname{adj}(M_U)E_U,\qquad BM=a1_c.$$
This is the required $\psi$. Conversely write $B$ for any proposed $\psi$. The same proved multilinear expansion gives
$$a^c=\det(BM)=\sum_{|U|=c}\det(B^U)\det(M_U),$$
where $B^U$ selects the columns indexed by $U$. This is the required minor expression for $a^c$, without cancellation or an invertibility assumption. If $c=0$, both modules are zero, the map is unique, and $a^0=1$ has its expression using the empty minor. Zero rings obey the same formulas. ∎

<a id="smoothing-lemma-elkik"></a>

#### Lemma D.5: elkik

Reading source: [Stacks, Tag 07CA](https://stacks.math.columbia.edu/tag/07CA).

For a finitely presented $R$-algebra $A$, let $J_e$ and $J_s$ be the ideals generated by all its elementary standard and strictly standard elements, respectively. Then
$$H_{A/R}=\sqrt{J_e}=\sqrt{J_s}.$$
In particular $A_a$ is smooth over $R$ whenever $a$ is strictly standard.

**Proof.** First fix a strictly standard witness from D.3 and put $B=A_a$ and $N=(I/I^2)\otimes_A B$. Its relation condition says that the first $c$ equation classes generate $N$: divide each relation by the unit $a$. Write $q:B^c\to N$ for this surjection and $d:N\to B^n$ for the conormal differential. D.4 gives $\psi:B^n\to B^c$ with
$$\psi d q=a1_c.$$
If $q(v)=0$ this identity gives $av=0$, hence $v=0$. Consequently $q$ is an isomorphism. The map $\chi=q\,a^{-1}\psi:B^n\to N$ satisfies $\chi d=1_N$. Thus
$$B^n=d(N)\oplus\ker\chi.$$
Its quotient by $d(N)$ is a finite projective module, being a direct summand of $B^n$, and $d$ has zero kernel.

The actual localization still has a finite presentation over $R$: if $h\in P$ lifts $a$, it is $P[z]/(f_1,\ldots,f_m,hz-1)$. The quotient isomorphism follows by adjoining the specified inverse of $h$. The full presentation comparison [F.11](#algebra-lemma-NL-homotopy) and localization calculation [F.65](#algebra-lemma-localize-NL) identify its first cotangent homology and differential module with the kernel and cokernel just calculated. Therefore the smoothness definition [F.6](#algebra-definition-smooth) proves that $R\to B$ is smooth. If $B=0$, these modules are zero and the same finite presentation and criterion apply.

Each singular prime contains every such $a$, since a prime avoiding $a$ has the smooth neighbourhood $A_a$. Hence $V(H_{A/R})\subset V(J_s)$. Setting every other minor coefficient to zero makes an elementary witness a strict witness, so $J_e\subset J_s$. If a prime is smooth, [D.2](#smoothing-lemma-find-strictly-standard) supplies an elementary witness outside it; relabel its selected variables and equations to place them first, absorbing any ordering sign in the coefficient. Such a prime cannot contain $J_e$. These statements give
$$V(J_e)\subset V(H_{A/R})\subset V(J_s)\subset V(J_e).$$
The radical/prime equality proved in D.1 now proves both asserted equalities of ideals. Neither this argument nor the conormal splitting assumes that the base is Noetherian or that the smooth locus is quasi-compact. ∎

<a id="smoothing-example-not-quasi-compact"></a>

#### Example D.6: not quasi compact

Reading source: [AI Integrated Stacks, pinned smoothing, lines 285–292](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/smoothing.tex#L285-L292).

A smooth locus can fail to be quasi-compact even for a finitely presented map. For any field $k$, take
$$R=k[x,y_1,y_2,\ldots]/(xy_i\mid i\geq1),\qquad A=R/(x).$$
In $\operatorname{Spec}A$, its smooth locus is precisely
$$U=\bigcup_{i\geq1}D(y_i)
=\operatorname{Spec}A\setminus\{\mathfrak m\},\qquad
\mathfrak m=(y_1,y_2,\ldots).$$
No finite family of these distinguished opens covers $U$. In particular $U$ is not quasi-compact.

**Proof.** The quotient identifies $A$ with $k[y_1,y_2,\ldots]$. The map $R\to A$ is of finite presentation: it is the quotient by the single generator $x$, with no algebra variables required. The base ring $R$ is not assumed Noetherian. Evaluation at all $y_i=0$ gives $A/\mathfrak m=k$, so $\mathfrak m$ is maximal and is the only prime containing every $y_i$.

Here is the ideal calculation. Setting all $y_i$ to zero gives a retraction $R\to k[x]$ of the natural inclusion $k[x]\to R$, so that inclusion is injective. For $I=(x)\subset R$, the relations $xy_i=0$ give $xr=xr(x,0,0,\ldots)$ for every $r\in R$. Therefore
$$
I=xk[x],\qquad I^2=x^2k[x],\qquad I/I^2=k\,\bar x\simeq A/\mathfrak m.
$$
In the last identification every $y_i$ annihilates $\bar x$. For the zero-variable polynomial presentation $R\twoheadrightarrow A$, the conormal complex is $[I/I^2\to0]$. The presentation comparison in Lemma [F.11](#algebra-lemma-NL-homotopy) identifies it with the naive cotangent complex used in Definition [F.6](#algebra-definition-smooth).

First suppose $y_i\notin\mathfrak q$. Inverting $y_i$ in $R$ makes $x=0$, hence $A_{y_i}=R_{y_i}$. As an $R$-algebra this is
$$
R[t]/(h),\qquad h=y_it-1.
$$
The element $h$ is a nonzerodivisor over this arbitrary base ring. Indeed, if $h\sum_{n=0}^Nb_nt^n=0$, its constant coefficient gives $b_0=0$, and its successive coefficients $y_ib_{n-1}-b_n=0$ give every $b_n=0$. Consequently $(h)/(h^2)$ is free on $\bar h$ over $R[t]/(h)$: multiplication by $h$ gives a surjection onto it, and cancellation of the nonzerodivisor $h$ shows that its kernel is exactly $(h)$. An $R$-derivation of $R[t]$ is determined by its value on $t$; the product rule gives $d(t^n)=nt^{n-1}dt$. Thus $\Omega_{R[t]/R}=R[t]dt$, and this presentation has conormal complex
$$
A_{y_i}\,\bar h\xrightarrow{\ y_i\ }A_{y_i}\,dt.
$$
Its differential is an isomorphism, since $y_i$ is a unit. Both first homology and the differential module are zero, and the zero module is finite projective. The displayed presentation is finite, so Definition [F.6](#algebra-definition-smooth) proves $R\to A_{y_i}$ smooth. Definition [F.7](#algebra-definition-smooth-at-prime) proves smoothness at every point of $D(y_i)$.

We must also exclude the exceptional point $\mathfrak m$ from every smooth neighbourhood. Let $g\in A\setminus\mathfrak m$. Its constant coefficient $c=g(0,0,\ldots)$ is nonzero. Regard its polynomial expression as a lift $\widetilde g\in R$. A presentation of $A_g$ over $R$ is
$$
P=R[t]\twoheadrightarrow A_g,\qquad
J=\ker(P\to A_g)=(x,\widetilde g t-1).
$$
The class of $x$ in $J/J^2$ has relative differential zero, because $x$ belongs to the base ring $R$. This class is nonzero. To see this, put $C=(R/(x^2))_{\widetilde g}$. The $R$-algebra map $P\to C$ sending $t$ to $\widetilde g^{-1}$ maps $J$ into the square-zero ideal $(x)C$, and maps $J^2$ to zero. It therefore maps the class of $x$ in $J/J^2$ to $x\in C$. The assignments $x\mapsto\epsilon$ and $y_i\mapsto0$ define
$$
R/(x^2)\longrightarrow k[\epsilon]/(\epsilon^2).
$$
They respect all the relations, and send $\widetilde g$ to the unit $c$. The map extends to $C$ and sends $x$ to the nonzero element $\epsilon$; its nonzeroness follows directly from the degree bound for a multiple of $\epsilon^2$. Hence $x\ne0$ in $C$, and the class of $x$ is a nonzero kernel element in the conormal complex $[J/J^2\to A_gdt]$. By the same presentation comparison, $H_1(\operatorname{NL}_{A_g/R})\ne0$. Definition [F.6](#algebra-definition-smooth) shows that $R\to A_g$ is not smooth. This holds for every $g\notin\mathfrak m$, so Definition [F.7](#algebra-definition-smooth-at-prime) shows that $R\to A$ is not smooth at $\mathfrak m$.

Every other prime omits some $y_i$, proving that the smooth locus is exactly the displayed open $U$. In the notation of Definition [D.1](#smoothing-definition-singular-ideal), this also gives $H_{A/R}=\mathfrak m$.

Finally the open cover $U=\bigcup_{i\geq1}D(y_i)$ has no finite subcover. Given a finite set $F$ of indices, choose $j\notin F$. Evaluation $y_j\mapsto1$ and $y_i\mapsto0$ for $i\ne j$ defines a surjection $A\to k$ with prime kernel $\mathfrak q_j$. This point lies in $D(y_j)\subset U$ but in none of the $D(y_i)$ with $i\in F$. Thus no finite subfamily covers $U$, and $U$ is not quasi-compact. $\square$

<a id="smoothing-lemma-strictly-standard-base-change"></a>

#### Lemma D.7: strictly standard base change

Reading source: [Stacks, Tag 07CC](https://stacks.math.columbia.edu/tag/07CC).

Let $R\to A$ be finitely presented and $R\to R'$ any ring map. An elementary standard element $a$ remains elementary standard as $a\otimes1$ in $A\otimes_R R'$. The same assertion holds for strictly standard elements. No flatness assumption on $R'$ is needed.

**Proof.** Take the finite presentation and witness from D.3 and set $P'=R'[x_1,\ldots,x_n]$. The polynomial base-change map $P\otimes_R R'\to P'$ sends $x^E\otimes r'$ to $r'x^E$. Its inverse sends the coefficient of every monomial to the same tensor; the polynomial monomials are the free $R$-basis of $P$, so these maps are inverse. Tensor right exactness identifies
$$A\otimes_R R'=P'/I',\qquad I'=(f'_1,\ldots,f'_m),$$
where $f'_j$ is obtained by changing coefficients along $R\to R'$.

For a monomial $r x^E$, differentiation multiplies its coefficient by the integer $E_i$ and reduces the $i$th exponent by one. Changing coefficients commutes with this operation, including when that integer becomes zero in $R'$. Consequently every selected Jacobian entry and its determinant is the image of the old one. The elementary single-minor identity, or the strict sum-of-minors identity, maps to exactly the required new identity with coefficients $a'\otimes1$ or $a_U\otimes1$.

For the relation condition, choose a polynomial lift $\widetilde a$ and write each old relation with its finitely many coefficients in $(f_1,\ldots,f_c)+I^2$. Its image expresses $\widetilde a' f'_{c+j}$ in $(f'_1,\ldots,f'_c)+(I')^2$, because products of two elements of $I$ map to products of two elements of $I'$. These are exactly D.3e2 or D.3s2 for the new witness. No injectivity of a tensor map was used. Empty minors, empty relation lists and a zero base-changed algebra satisfy the same identities. ∎

<a id="smoothing-lemma-final-solve"></a>

#### Lemma D.8: final solve

Reading source: [Stacks, Tag 07EU](https://stacks.math.columbia.edu/tag/07EU).

Suppose $R\to A\xrightarrow{\rho}\Lambda$, with $A$ finitely presented over $R$ and $H_{A/R}\Lambda=\Lambda$. Then $\rho$ factors through an $R$-smooth algebra:
$$A\longrightarrow B\longrightarrow\Lambda.$$

**Proof.** If $\Lambda=0$, choose $B=0$. Its presentation $R/(1)$ is finite and its cotangent homology and differential module are zero, so F.6 makes it smooth. Assume henceforth $\Lambda\ne0$.

Let $J_s$ be the ideal generated by strictly standard elements. D.5 gives $H_{A/R}=\sqrt{J_s}$. We first check that extending the smaller ideal also gives the unit ideal. Choose $h_1,\ldots,h_t\in H_{A/R}$ and $\lambda_i\in\Lambda$ with $\sum_i\rho(h_i)\lambda_i=1$. For each $i$ some $n_i\geq1$ has $h_i^{n_i}\in J_s$. Raise that identity to
$$N=1+\sum_i(n_i-1).$$
Every term in its distributive expansion uses some $h_i$ at least $n_i$ times: otherwise its total degree would be at most $N-1$. Each term therefore belongs to $J_s\Lambda$. Thus $1\in J_s\Lambda$.

Expanding the finite expressions in this ideal gives strictly standard elements $a_1,\ldots,a_r$ and $\mu_i\in\Lambda$ with $\sum_i\rho(a_i)\mu_i=1$. Here $r>0$, since the target is nonzero. Define
$$B=A[T_1,\ldots,T_r]/\left(\sum_i a_iT_i-1\right).$$
The map sending $T_i$ to $\mu_i$ gives $B\to\Lambda$ and extends the prescribed $\rho$. Appending these finite variables and this one relation to a finite presentation of $A$ proves that $B/R$ is finitely presented.

In $B$, the elements $a_i$ generate one. Their principal opens therefore cover its spectrum: a prime containing all of them would contain the displayed unit. For each $i$ there is the explicit isomorphism
$$B_{a_i}\cong A_{a_i}[T_j:j\ne i].$$
The map from right to left includes the remaining variables; its inverse substitutes $T_i=a_i^{-1}(1-\sum_{j\ne i}a_jT_j)$. Substitution kills the relation and both composites fix their generators. D.5 proves $A_{a_i}/R$ smooth. Adjoining the finitely many remaining polynomial variables is smooth directly: its empty-relation presentation has zero first cotangent homology and a finite free differential module on those variables, by F.11 and AG-CA-15, Theorem 5.1. F.6 therefore gives smoothness over $A_{a_i}$. The entire composition proof [F.29](#algebra-lemma-compose-smooth) makes $B_{a_i}/R$ smooth. The proved finite principal-cover criterion [F.67](#algebra-lemma-locally-smooth) now makes $B/R$ smooth. Zero localizations create empty charts and are already included in those criteria. This proves the required factorization over an arbitrary base ring. ∎

### Presentations of algebras

<a id="smoothing-section-presentations"></a>

The presentation change in [D.9](#smoothing-lemma-improve-presentation) uses a symmetric algebra over $A$. Over a Noetherian base its finite generators also give finite presentation. These constructions are among the results originating with Elkik.

<a id="smoothing-lemma-improve-presentation"></a>

#### Lemma D.9: improve presentation

Reading source: [Stacks, Tag 07CE](https://stacks.math.columbia.edu/tag/07CE).

For a finitely presented algebra $A$ over an arbitrary ring $R$, there is an $R$-algebra map $A\to C$ of finite type with a retraction $C\to A$ such that:

1. Whenever $R\to A_a$ is a local complete intersection, $A_a\to C_a$ is smooth and $C_a$ has a finite polynomial presentation over $R$ with free conormal module.
2. Whenever $A_a/R$ is smooth, $\Omega_{C_a/R}$ is free.

**Proof.** Fix $P=R[X_1,\ldots,X_n]\twoheadrightarrow A$ with $I=(f_1,\ldots,f_m)$ and let
$$M=I/I^2,\qquad K=\ker(A^m\longrightarrow M),\qquad C=\operatorname{Sym}_A(M).$$
The map $A^m\to M$ sends $e_j$ to $[f_j]$. The symmetric algebra and its degree-zero augmentation are constructed in [F.128](#more-algebra-lemma-symmetric-algebra-smooth); their composite on $A$ is identity. Its universal property identifies $C$ with the quotient of $P[Y_1,\ldots,Y_m]$ by an ideal $J$ generated by $I$ and the linear forms whose coefficient classes belong to $K$. In fact maps out of this quotient are exactly maps $A\to D$ together with linear maps $A^m\to D$ killing $K$, hence linear maps $M\to D$. The resulting maps are inverse because they fix $A$ and every $Y_j$. This proves the kernel description and finite type even when $K$ is not finite.

Fix $a\in A$ and write $B=A_a$. Suppose first $R\to B$ is a local complete intersection. The arbitrary-ring presentation comparison [F.94.A](#more-algebra-lemma-lci-presentation-independent) supplies local Koszul-regular equation lists for the inverse-variable polynomial presentation of $B$. Such a list gives a conormal basis: correct a relation modulo the square of its ideal by coefficients in the ideal; the resulting exact relation is a first Koszul cycle, hence a boundary, whose coefficients belong to the ideal. This proves independence as well as generation of its equation classes. [F.72](#algebra-lemma-principal-localization-NL) identifies this locally free conormal module with $M_a\oplus B$. Its summand $M_a$ is locally finite flat and finitely presented, since both summands are generated by projections of a finite basis. The local finite-flat proof [S01, Lemma 1.2](AG-RG-S01.md) therefore makes $M_a$ free at each local ring; its finite presentation permits extending that basis to a principal neighbourhood. Thus $M_a$ is locally finite free.

Here are the finiteness and global splitting steps. Choose finitely many principal charts $D(b_i)$ covering $\operatorname{Spec}B$ on which $M_a$ is free. A finite subcover exists because the covering elements generate the unit ideal, witnessed by a finite expression for $1$. On each chart the surjection $B_{b_i}^m\to(M_a)_{b_i}$ splits and its kernel $(K_a)_{b_i}$ is a finite direct summand. Lift its finite generating list to fractions of elements of $K_a$ and collect their numerators in a finite submodule $K_0\subset K_a$. Then $(K_a/K_0)_{b_i}=0$ for every $i$. Any module element vanishing on these charts is zero: a power of each $b_i$ kills it, and these powers generate $1$, since a prime containing them would contain all the $b_i$. Hence $K_0=K_a$, so $M_a$ is finitely presented.

For each local splitting $s_i:M_{ab_i}\to B_{b_i}^m$, finite presentation identifies
$$\operatorname{Hom}_B(M_a,B^m)_{b_i}=\operatorname{Hom}_{B_{b_i}}(M_{ab_i},B_{b_i}^m).$$
To verify this identity, present $M_a$ by finite free modules; both Hom modules are the kernels of the same finite matrix map after exact localization. Clear denominators of $s_i$, then multiply by a further power of $b_i$ to kill the error on a finite generating list. This gives $t_i:M_a\to B^m$ with $\pi t_i=b_i^{e_i}1_{M_a}$. Choose $r_i$ satisfying $\sum_i r_i b_i^{e_i}=1$. The map $\sum_i r_it_i$ splits $\pi$. Consequently
$$M_a\oplus K_a\cong B^m,$$
and both summands are finite projective. This argument also handles $B=0$ directly by its zero modules.

The identities in F.128 give $C_a=\operatorname{Sym}_B(M_a)$, which is smooth and finitely presented over $B$. The inverse-variable presentation makes $B/R$ finitely presented, and finite substitution [F.28](#algebra-lemma-compose-finite-type) therefore makes $C_a/R$ finitely presented as well. The conormal calculation [F.102](#more-algebra-lemma-cotangent-complex-symmetric-algebra) identifies the kernel conormal of $B[Y]\to C_a$ with $K_a\otimes_B C_a$. On principal charts where the split modules are free, this kernel is generated by a subset of polynomial coordinates. Those coordinates form a regular sequence: multiplication by each new variable is injective by polynomial coefficient comparison, even over an arbitrary ring. The regular-list cone calculation in [F.118](#more-algebra-lemma-noetherian-finite-all-equivalent) gives their Koszul exactness in positive degrees; that direction requires no Noetherian hypothesis. Thus [F.130](#more-algebra-lemma-transitive-lci-at-end) supplies the actual left injection in the conormal transitivity sequence.

If $h\in P$ lifts $a$, introduce an inverse variable $X_0$ and use the equation ideals $I'=(I,hX_0-1)$ and $J'=(J,hX_0-1)$. The explicit localization calculation [F.72](#algebra-lemma-principal-localization-NL) and the conormal sequence just justified give
$$0\longrightarrow C_a\oplus(M_a\otimes_B C_a)\longrightarrow J'/(J')^2\longrightarrow K_a\otimes_B C_a\longrightarrow0.$$
The last module is projective because a split finite free presentation stays split after tensoring. Hence
$$J'/(J')^2\cong C_a\oplus((M_a\oplus K_a)\otimes_B C_a)\cong C_a^{m+1}.$$
Together with the explicit polynomial quotient for $C_a$ this proves (1). This conormal calculation uses only finite projectivity of $M_a$ and $K_a$, so it also applies when those properties are supplied by the smooth branch below.

For (2), suppose $B/R$ is smooth, without first assuming (1). [F.6](#algebra-definition-smooth), the full presentation comparison [F.11](#algebra-lemma-NL-homotopy) and localization [F.65](#algebra-lemma-localize-NL) give the split exact conormal sequence for the original $n$ variables:
$$0\longrightarrow M_a\longrightarrow B^n\longrightarrow\Omega_{B/R}\longrightarrow0.$$
Thus $M_a$ is finite projective and $M_a\oplus\Omega_{B/R}\cong B^n$. F.128 gives smoothness of $C_a/B$; its derivation universal property also identifies $\Omega_{C_a/B}=M_a\otimes_B C_a$, since a derivation from the symmetric algebra is exactly a linear map on its degree-one generators. The full cotangent transitivity calculation [F.42](#algebra-lemma-exact-sequence-NL) now gives
$$0\longrightarrow\Omega_{B/R}\otimes_B C_a\longrightarrow\Omega_{C_a/R}\longrightarrow M_a\otimes_B C_a\longrightarrow0.$$
The right term is projective, so the sequence splits and its middle term is $C_a^n$. This proves (2). Zero algebras and empty variable or equation lists obey the same identities. ∎

<a id="smoothing-proposition-lift-smooth"></a>

#### Proposition D.10: lift smooth

Reading source: [Stacks, Tag 07M8](https://stacks.math.columbia.edu/tag/07M8).

Let $R\twoheadrightarrow R_0=R/I$ be a surjection of Noetherian rings. A syntomic $R_0$-algebra $A_0$ has a syntomic lift $A$ over $R$, with a specified isomorphism $A/IA\cong A_0$. If $A_0/R_0$ is smooth, the lift can be chosen smooth. This is the auxiliary Noetherian lifting assertion used in desingularization.

**Proof.** If $A_0=0$, take $A=0$: its presentation $R/(1)$ is finite, it is flat, its cotangent modules are zero, and its fibres are empty. Assume $A_0\ne0$ and syntomic. Choose a finite polynomial presentation $A_0=R_0[X]/J_0$ and put $P_0=J_0/J_0^2$. [F.88](#algebra-lemma-syntomic-presentation-ideal-mod-squares) makes $P_0$ finite projective. By [F.129](#more-algebra-lemma-syntomic-lci) the map is a local complete intersection, so [D.9](#smoothing-lemma-improve-presentation) constructs
$$C_0=\operatorname{Sym}_{A_0}(P_0)$$
with a free-conormal polynomial presentation and a smooth map $A_0\to C_0$. Its finite presentation follows from [F.128](#more-algebra-lemma-symmetric-algebra-smooth) and finite substitution [F.28](#algebra-lemma-compose-finite-type). The smooth/syntomic and composition proofs [F.83](#algebra-lemma-smooth-syntomic) and [F.32](#algebra-lemma-composition-syntomic) make $C_0/R_0$ syntomic.

The complete equation-basis argument [F.55](#algebra-lemma-huber) yields
$$C_0=R_0[Y_1,\ldots,Y_v]/(\bar f_1,\ldots,\bar f_c),$$
with these classes a conormal basis. Flatness identifies that conormal after residue-field base change with the fibre conormal, by right exact tensor and the injection of the equation ideal into the polynomial ring. The fibres are locally complete intersections by syntomicness. [F.57](#algebra-lemma-lci) therefore makes their point-dimensions $v-c$; applying this at their finitely many minimal primes gives dimension $v-c$ for every nonempty fibre.

Lift each $\bar f_j$ to the full polynomial ring $R[Y_1,\ldots,Y_v]$ and set $C^{\mathrm{pre}}=R[Y]/(f_1,\ldots,f_c)$. Its reduction is exactly $C_0$. [F.66(1)](#algebra-lemma-localize-relative-complete-intersection) gives $g\equiv1\pmod{IC^{\mathrm{pre}}}$ such that $C=(C^{\mathrm{pre}})_g$ is a relative global complete intersection. Thus $C/IC=C_0$, with no localization of the special fibre, and [F.76](#algebra-lemma-relative-global-complete-intersection) makes $C/R$ syntomic.

Choose a complementary finite projective module $Q_0$ with $P_0\oplus Q_0=A_0^N$. Apply the complete lifting proof [F.117](#more-algebra-lemma-lift-projective-module) to the finite projective $C_0$-module $Q_0\otimes_{A_0}C_0$. It gives a finitely presented étale $C\to C'$ inducing $C'/IC'\cong C_0$ and a finite projective $C'$-module $Q$ reducing to that specified module. Put $D=\operatorname{Sym}_{C'}(Q)$. It is smooth over $C'$ by F.128, and the proved composition statements make $D/R$ syntomic: étale maps are smooth by their zero cotangent complex and finite presentation, smooth maps are syntomic, and the base rings here are Noetherian finite-type algebras. The actual symmetric-algebra identities from F.128 give
$$\begin{aligned}
D/ID&\cong\operatorname{Sym}_{C_0}(Q_0\otimes_{A_0}C_0)\\
&\cong\operatorname{Sym}_{A_0}(Q_0)\otimes_{A_0}\operatorname{Sym}_{A_0}(P_0)\\
&\cong\operatorname{Sym}_{A_0}(Q_0\oplus P_0)\cong A_0[Z_1,\ldots,Z_N].
\end{aligned}$$
Choose $z_i\in D$ lifting these variables and set $E=D/(z_1,\ldots,z_N)$. Reduction of this quotient gives the specified $E/IE=A_0$.

We verify the claimed syntomic neighbourhood of every $\mathfrak q\in V(IE)$ rather than assuming it. Let $\mathfrak t$ be its preimage in $D$ and $\mathfrak p=\mathfrak q\cap R$. Then $I\subset\mathfrak p$. By [F.87](#algebra-lemma-syntomic) choose $u\notin\mathfrak t$ and a relative global complete-intersection presentation
$$D_u=R[W_1,\ldots,W_m]/(a_1,\ldots,a_s).$$
In the fibre over $k=\kappa(\mathfrak p)$ this is the localization of $(A_0\otimes_{R_0}k)[Z_1,\ldots,Z_N]$ at the image of $u$. Its ordered $Z_i$ are a regular sequence at the prime in question: multiplication by a polynomial variable is injective over any coefficient ring, successive quotients remove one variable, and exact localization preserves each injection. Their ideal stays proper at this prime because it comes from $\mathfrak q$ of the quotient.

Lift each $z_i$ to a polynomial $b_i$ in $R[W]$. By [F.77](#algebra-lemma-relative-global-complete-intersection-conormal), the fibre $\bar a_j$ form a regular sequence in the corresponding polynomial local ring. The just proved regularity of $Z_i$ in its quotient makes $(\bar a_1,\ldots,\bar a_s,\bar b_1,\ldots,\bar b_N)$ a regular sequence there. [F.57](#algebra-lemma-lci) gives fibre point-dimension $m-s-N$ for
$$E_{\bar u}=R[W]/(a_1,\ldots,a_s,b_1,\ldots,b_N).$$
Apply [F.66(3)](#algebra-lemma-localize-relative-complete-intersection) to this actual $s+N$-equation presentation. It supplies a relative global complete-intersection neighbourhood of $\mathfrak q$, hence a syntomic one by F.76. A further localization of $E_{\bar u}$ is a principal localization of $E$: write its inverted element as $e/\bar u^r$ and invert $\bar u e$. This proves the claim at every point of $V(IE)$.

Let $W$ be the union of these syntomic neighbourhoods and write its closed complement as $V(L)$ in $\operatorname{Spec}E$. Since $V(L)\cap V(IE)=\varnothing$, the ideal $L+IE$ is all of $E$; otherwise a containing maximal ideal would give a point of that intersection. Choose $h\in L$ with $h\equiv1\pmod{IE}$. Then $D(h)\subset W$, and $E_h/IE_h=A_0$ exactly. The finite principal-cover criterion [F.62](#algebra-lemma-local-syntomic) makes $A=E_h$ syntomic over $R$: its spectrum has a finite subcover by the already constructed syntomic charts, using the finite expression for $1$ in their covering ideal. This proves the first assertion, including $N=0$.

Now assume $A_0/R_0$ smooth. For every prime $\mathfrak q\in V(IA)$ the fibre of $A/R$ is the same as the fibre of $A_0/R_0$ over its contracted base prime. Those fibres are smooth by the following calculation, which does not assume that the residue-field map is flat. [F.83](#algebra-lemma-smooth-syntomic) covers $A_0$ by standard smooth principal charts; choose finitely many by their unit-ideal cover. Tensor right exactness changes each polynomial quotient to the quotient by the coefficient-changed equations. Monomial differentiation commutes with changing coefficients, so its chosen Jacobian determinant is the image of the old unit and is still a unit. [F.85](#algebra-lemma-standard-smooth) makes every fibre chart smooth. The finite expression for $1$ in the covering ideal remains such an expression after base change, so these charts cover the fibre; [F.67](#algebra-lemma-locally-smooth) makes the whole fibre smooth. Since $A/R$ is finitely presented and flat, [F.45](#algebra-lemma-flat-fibre-smooth) gives a smooth neighbourhood of each such $\mathfrak q$. Write the complement of their union as $V(L')$. Exactly as above choose $h'\in L'$ with $h'\equiv1\pmod{IA}$. Then $A_{h'}/IA_{h'}=A_0$, while F.67 makes $A_{h'}/R$ smooth. No hypothesis that $I$ is nilpotent or lies in the Jacobson radical is needed for either shrinking step. ∎

For Noetherian $R$, [F.87](#algebra-lemma-syntomic) gives relative global
complete-intersection neighbourhoods of a syntomic map. The next lemma
proves the required arbitrary-base extension and constructs a
symmetric-algebra bundle over $\operatorname{Spec}(A)$ with a retraction
whose total space is a relative global complete intersection over $R$.

<a id="smoothing-lemma-syntomic-complete-intersection"></a>

#### Lemma D.11: syntomic complete intersection

Reading source: [Stacks, Tag 07CG](https://stacks.math.columbia.edu/tag/07CG).

For a syntomic map $R\to A$ over any ring $R$, there is a smooth $A$-algebra $C$ and a retraction $C\to A$ such that
$$C=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c)$$
is flat over $R$ and every nonempty fibre has dimension $n-c$.

**Proof.** We first prove the arbitrary-base local complete-intersection assertion needed to apply [D.9](#smoothing-lemma-improve-presentation). Fix a finite presentation $A=R[X_1,\ldots,X_N]/(u_1,\ldots,u_s)$ and a prime $\mathfrak q$ of $A$ over $\mathfrak p$ of $R$. In the polynomial local ring of its $k=\kappa(\mathfrak p)$ fibre, syntomicness and [F.58](#algebra-lemma-lci-at-prime) give a complete-intersection equation ideal. Its conormal is free by [F.57](#algebra-lemma-lci). Select from the $u_i$ a list whose conormal residue classes are a basis. Nakayama and the unit determinant of its coordinate matrix make its local conormal classes a basis; the final assertion of F.57 makes that selected list generate the fibre ideal regularly.

Model the local map $R_{\mathfrak p}\to A_{\mathfrak q}$ using [F.59](#algebra-lemma-limit-essentially-finite-presentation). Explicitly, for finite-type $\mathbf Z$-subalgebras $R_0\subset R$ containing all equation coefficients, put $T_0=R_0[X]/(u_i)$ and contract the chosen primes to $\mathfrak p_0,\mathfrak q_0$. The stages are $R_{0,\mathfrak p_0}\to(T_0)_{\mathfrak q_0}$. Adding numerators and denominators of any finite set of fractions proves cofinality in the stated local-model system. The models are Noetherian, their transitions are exactly localized base changes, and their colimits are the given local rings. Since $A_{\mathfrak q}$ is flat over $R_{\mathfrak p}$ and is a finite module over itself, [F.21](#algebra-lemma-colimit-eventually-flat) gives a stage where $(T_0)_{\mathfrak q_0}$ is flat over $R_{0,\mathfrak p_0}$.

We verify its closed-fibre complete-intersection property. Let $k_0=\kappa(\mathfrak p_0)$. There is an embedding $k_0\subset k$ by contraction of primes and the fraction-field construction. The map from the polynomial fibre local ring $V_0$ at the contracted prime to the final polynomial fibre local ring $V$ is local and flat, being field extension followed by localization. The selected equations generate the final fibre ideal. The finite $V_0$-module consisting of the model ideal modulo their span becomes zero after tensoring with $V$, so it is zero: a finite module with zero tensor along a local flat map has zero residue-field tensor, and Nakayama kills it. Here the target residue field extends the source residue field, so that residue-field tensor is faithful on vector spaces.

The same argument applies to each positive homology module of the selected finite free Koszul complex. These modules are finite because $V_0$ is Noetherian. Flat tensor commutes with their kernels and images, so their tensors are zero, since the final list is regular. Nakayama again gives zero homology in the model. The list lies in the maximal ideal, and [F.118](#more-algebra-lemma-noetherian-finite-all-equivalent) makes it regular in $V_0$. Thus the model has precisely the closed fibre required by the Noetherian-base theorem [F.87](#algebra-lemma-syntomic).

Apply that theorem to obtain $g_0\notin\mathfrak q_0$ with $B_0=(T_0)_{g_0}$ a relative global complete intersection over $R_0$. Its scalar extension is exactly $A_g$, with $g\notin\mathfrak q$. Write $B_0=P_0/(b_1,\ldots,b_t)$ using its finite polynomial complete-intersection presentation. By [F.126](#more-algebra-lemma-relative-global-complete-intersection-koszul) its augmented Koszul complex is exact, and by [F.76](#algebra-lemma-relative-global-complete-intersection) its last quotient $B_0$ is $R_0$-flat. Every complex term is also $R_0$-flat, being finite free over the polynomial ring.

All successive kernels in this augmented complex are $R_0$-flat. For $0\to Z\to F\to Q\to0$ with $F,Q$ flat, quotient flatness makes tensor preserve the left injection. For any inclusion of modules, the resulting map after tensoring with $Z$ is injective by embedding its two tensor products into those for $F$. Thus $Z$ is flat. Induct upwards from the flat augmentation quotient. Tensoring each short exact sequence with $R$ now remains exact. The actual base-changed equation list for $A_g$ is therefore Koszul-regular. This is the needed arbitrary-base assertion; it does not apply F.87 directly to a non-Noetherian base. The comparison [F.94.A](#more-algebra-lemma-lci-presentation-independent) transports these presentations to the fixed finite polynomial presentation of $A$ at every prime, proving that $R\to A$ is a local complete intersection.

Let $I=(u_i)$ and $M=I/I^2$. D.9 with $a=1$ constructs $C=\operatorname{Sym}_A(M)$ with its degree-zero augmentation $C\to A$, proves $M$ finite projective and $A\to C$ smooth, and supplies a polynomial presentation over $R$ with free conormal. The finite-presentation proof [F.128](#more-algebra-lemma-symmetric-algebra-smooth) and finite substitution [F.28](#algebra-lemma-compose-finite-type) make $C/R$ finitely presented. The complete equation-basis construction [F.55](#algebra-lemma-huber) gives a presentation $C=R[x_1,\ldots,x_n]/J$ with $J=(f_1,\ldots,f_c)$ and those classes a basis of $J/J^2$.

On a finite principal cover of $\operatorname{Spec}A$ trivializing $M$, the symmetric-algebra identities in F.128 make $C$ a polynomial algebra over each chart. Those algebras are $A$-flat. Tensoring an injection with $C$ and detecting its kernel on the cover proves $A$-flatness of $C$ globally. The given flatness of $A/R$ consequently makes $C/R$ flat.

For a base residue field $k$, the same identities give $C_k=\operatorname{Sym}_{A_k}(M\otimes_A A_k)$. The original syntomic hypothesis makes $A_k$ locally a complete intersection. Trivializing the module and restricting to complete-intersection charts makes $C_k$ a polynomial algebra over such a chart. Its regular equations remain regular after polynomial extension and localization, because both are flat; the ambient polynomial local rings are regular. F.58 therefore proves that $C_k$ is locally a complete intersection.

Flatness of $C/R$ makes tensoring $0\to J\to R[x]\to C\to0$ injective on the left. Hence $J\otimes_R k$ is the fibre equation ideal $\bar J$. Right exactness applied to $J^2\to J\to J/J^2\to0$ identifies its conormal: the image of $J^2\otimes_R k$ consists exactly of products of the fibre ideal generators. Thus
$$\bar J/\bar J^2\cong(J/J^2)\otimes_R k\cong C_k^c.$$
At a minimal prime of a nonzero $C_k$, F.57 identifies this rank with the height of its polynomial preimage, since the quotient local ring has dimension zero. Each component therefore has dimension $n-c$ by AG-CA-09, Theorem 4.3. The field algebra has finitely many components, so its dimension is their maximum, also $n-c$. The augmentation fixes $A$, and is the required retraction.

If $A=0$, take $C=0$ with presentation $R/(1)$. It is flat, the identity $A\to C$ is smooth, and all fibres are empty. Empty variable or regular lists use the same constructions. No condition has been added to the arbitrary base ring. ∎

<a id="smoothing-lemma-smooth-standard-smooth"></a>

#### Lemma D.12: smooth standard smooth

Reading source: [Stacks, Tag 07CH](https://stacks.math.columbia.edu/tag/07CH).

Every smooth algebra $A$ over an arbitrary ring $R$ is a retract of an $R$-algebra $B$ that is standard smooth over $R$, with the map $A\to B$ itself smooth. Thus $B$ has a finite polynomial presentation with an invertible square Jacobian minor on its first equation variables.

**Proof.** If $A=0$, set $B=0$. The presentation $R[X]/(1)$ has Jacobian entry $0$, which is a unit in the zero ring, and the identity is its smooth retraction. Suppose $A\ne0$.

The smooth branch of [D.9](#smoothing-lemma-improve-presentation) constructs $C=\operatorname{Sym}_A(I/I^2)$, with $A\to C$ smooth and an augmentation $C\to A$. In this branch the conormal sequence is split by F.6, so the same finite-projective conormal calculation in D.9 applies, independently of any syntomic implication over the base. Appending the inverse variable for $1$ gives a finite polynomial presentation of $C$ with free conormal. [F.55](#algebra-lemma-huber) replaces it by
$$C=R[X_1,\ldots,X_n]/(f_1,\ldots,f_c)$$
whose equation classes are a conormal basis. [F.29](#algebra-lemma-compose-smooth) makes $C/R$ smooth. It is nonzero, because it retracts onto $A$.

By [F.6](#algebra-definition-smooth) and the full comparison [F.11](#algebra-lemma-NL-homotopy), the conormal differential in this presentation is a split injection. Write its matrix with equations as rows as $J=(\partial f_j/\partial X_i)$, of size $c\times n$. A left inverse of the transposed conormal map gives an $n\times c$ matrix $T$ over $C$ such that $JT=1_c$. Reduction at any maximal ideal of $C$ gives $c\le n$ by vector-space dimension. Lift its entries to polynomials $\widetilde T_{i\ell}$.

Set $E=C[Y_1,\ldots,Y_c]$ and introduce redundant coordinates $Z_i$ by the equations
$$h_i=X_i-\sum_{\ell=1}^c\widetilde T_{i\ell}(X)Y_\ell-Z_i.$$
Eliminating $Z_i$ gives inverse generator maps for
$$E=R[X,Y,Z]/(f_1,\ldots,f_c,h_1,\ldots,h_n).$$
Let $G$ be the determinant of its square Jacobian on the selected variables $(X_1,\ldots,X_n,Y_1,\ldots,Y_c)$, using the displayed equation order. Modulo $Y$ in $C$ its matrix is
$$\begin{pmatrix}J&0\\1_n&-T\end{pmatrix}.$$
Interchange the two row blocks, which contributes $(-1)^{nc}$, then subtract $J$ times the first block row from the second. The resulting matrix is block upper triangular with diagonal $1_n,JT=1_c$. Its determinant is $1$. Thus the image $g$ of $G$ in $E$ satisfies $g\bmod(Y)=(-1)^{nc}$.

Put $B=E_g$. Evaluation at $Y=0$ sends $g$ to that unit and therefore extends the augmentation to $B\to C$. Its composite with $C\to B$ is identity; composing with $C\to A$ gives the required retraction of $A\to B$.

We verify both remaining smooth maps directly. The polynomial extension $C\to E=C[Y_1,\ldots,Y_c]$ has an empty-relation conormal complex: its degree-one term is zero, and its differential module is finite free on $dY_1,\ldots,dY_c$, by AG-CA-15, Theorem 5.1. Presentation comparison F.11 and the definition F.6 therefore give smoothness. The localization is the finite presentation $B=E[U]/(gU-1)$, with inverse maps adjoining $g^{-1}$ or evaluating $U$ there. Its conormal is generated by the single equation class, whose differential is $g\,dU$. This coefficient is a unit in $B$. Hence the surjection $B\to (gU-1)/(gU-1)^2$, followed by the conormal differential to $B\,dU$, is an isomorphism. Both maps are consequently isomorphisms. Its kernel and differential cokernel are zero, so F.11 and F.6 prove smoothness of $E\to B$. Applying the entire composition proof F.29 to $A\to C\to E\to B$ proves that $A\to B$ is smooth. These calculations use no Noetherian or fibre-dimension hypothesis.

Finally adjoining the inverse of $G$ writes
$$B=R[X,Y,U,Z]/(f_1,\ldots,f_c,h_1,\ldots,h_n,UG-1).$$
Order the selected variables as $(X,Y,U)$, before all the $Z_i$. There are $n+c+1$ equations and selected variables. The Jacobian has the earlier square block in its upper left, zeros above the last column, and $G$ in its last diagonal position. Its determinant is therefore $G^2$, a unit since $UG=1$. Renaming the variables in this order gives the standard smooth presentation asserted. Empty blocks have determinant $1$; the argument includes $c=0$ and $n=0$ over any base ring. ∎

<a id="smoothing-lemma-colimit-standard-smooth"></a>

#### Lemma D.13: colimit standard smooth

Reading source: [Stacks, Tag 07CI](https://stacks.math.columbia.edu/tag/07CI).

If an $R$-algebra $\Lambda$ is a filtered colimit of smooth $R$-algebras, then it is a filtered colimit of standard smooth $R$-algebras, over an arbitrary base ring $R$.

**Proof.** First consider a map $A\to\Lambda$ with $A$ finitely presented over $R$. Choose representatives for its finite generator list at one common smooth stage. Each of its finitely many defining relations is zero at a later stage, by the equality rule for filtered colimits. A common successor therefore gives a factorization $A\to B\to\Lambda$ with $B/R$ smooth. By [D.12](#smoothing-lemma-smooth-standard-smooth), $B$ is a retract of a standard smooth $R$-algebra $C$. The composite $A\to B\to C$ followed by $C\to B\to\Lambda$ is the original map. Thus every such finite-presentation map factors through a standard smooth algebra.

Take as objects finite polynomial presentations of standard smooth $R$-algebras together with maps to $\Lambda$, and as arrows algebra maps respecting those maps. This is a small category: the finite coefficient lists form a set, and each map to $\Lambda$ is determined by a finite tuple of elements. The presentation of $R$ with empty variable and equation lists is an object. Two objects have a common successor by applying the factorization just proved to the map from their tensor product to $\Lambda$; that tensor product has the finite presentation with their disjoint variables and both relation lists. To equalize parallel arrows $u,v\colon B\rightrightarrows C$, choose generators $b_1,\ldots,b_s$ of $B$ and append $u(b_i)-v(b_i)$ to the relations of $C$. The resulting finitely presented quotient maps to $\Lambda$; its factorization through a standard smooth object supplies an arrow out of $C$ equalizing $u,v$, since equality on generators implies equality on all polynomials in them. These constructions prove that the category is filtered.

Let $L$ be its colimit. The canonical map $L\to\Lambda$ is surjective: factor $R[T]\to\Lambda$ with $T\mapsto\lambda$ to represent any chosen $\lambda$ at one of the objects. For injectivity, if $b\in B$ has zero image, the finitely presented algebra $B/(b)$ maps to $\Lambda$ and factors through an object. The resulting successor kills $b$, so its colimit class is zero. For two representatives with equal images, first move them to a common successor and use the same argument on their difference. Hence $L\to\Lambda$ is an isomorphism and every stage is standard smooth. Empty lists and zero rings obey the same constructions. ∎

<a id="smoothing-lemma-standard-smooth-include-generators"></a>

#### Lemma D.14: standard smooth include generators

Reading source: [Stacks, Tag 07EY](https://stacks.math.columbia.edu/tag/07EY).

Suppose $A/R$ is standard smooth and $E=\{a_1,\ldots,a_n\}\subset A$ is finite. There is a standard smooth presentation
$$A=R[x_1,\ldots,x_{n+m}]/(f_1,\ldots,f_c),\qquad c\ge n,$$
whose first $n$ coordinate classes are the specified $a_i$ in any chosen order, and whose Jacobian minor on its first $c$ variables is a unit.

**Proof.** Start with $A=R[y_1,\ldots,y_m]/(g_1,\ldots,g_d)$ and rename its variables so that the $d\times d$ minor on $y_1,\ldots,y_d$ is a unit. Choose polynomials $h_i(y)$ mapping to $a_i$. Adjoin variables $x_i$ with equations $x_i-h_i(y)$. Substitution defines an isomorphism
$$R[x_1,\ldots,x_n,y_1,\ldots,y_m]/(x_i-h_i,g_j)\longrightarrow A.$$
Its inverse sends the old $y_j$ classes to themselves. The two composites fix all $y_j$, and fix $x_i$ because its new relation identifies it with $h_i(y)$; they are therefore identity maps.

Order the equations by the $n$ new graph equations followed by the $d$ old equations. With equations as rows, the minor on $(x_1,\ldots,x_n,y_1,\ldots,y_d)$ is
$$\begin{pmatrix}1_n&-(\partial h_i/\partial y_j)\\0&(\partial g_i/\partial y_j)\end{pmatrix}.$$
In the signed permutation formula, each of its first $n$ columns has only its diagonal entry nonzero. The surviving terms therefore give exactly the old $d\times d$ determinant, which is a unit. Transposing yields the determinant convention with variables as rows and equations as columns. Now set $c=n+d$ and rename $y_j=x_{n+j}$, placing the unselected $y$ variables last. Since $d\le m$, this is the required minor on the first $c$ variables. The first $n$ classes are the prescribed elements. Empty blocks use determinant $1$, so the proof includes an empty $E$ or an empty old equation list. ∎

<a id="smoothing-lemma-compare-standard"></a>

#### Lemma D.15: compare standard

Reading source: [AI Integrated Stacks, pinned smoothing, lines 718–850](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/smoothing.tex#L718-L850).

For a finitely presented $R$-algebra $A$ and $a\in A$, put $B=A_a$. Number the following six properties:

1. $B/R$ is smooth.
2. $B/R$ is smooth and $\Omega_{B/R}$ is stably free.
3. $B/R$ is smooth and $\Omega_{B/R}$ is free.
4. $B/R$ admits a standard smooth presentation.
5. $a$ satisfies the strictly standard condition of [D.3](#smoothing-definition-strictly-standard).
6. $a$ satisfies the elementary standard condition of D.3.

Their comparisons are:

- **(a)** $(4)\Rightarrow(3)\Rightarrow(2)\Rightarrow(1)$.
- **(b)** $(6)\Rightarrow(5)$.
- **(c)** $(6)\Rightarrow(4)$.
- **(d)** $(5)\Rightarrow(2)$.
- **(e)** Property (2) gives an $e_0$ such that $a^e$ is strictly standard for every $e\geq e_0$.
- **(f)** Every sufficiently large positive power $a^e$ is elementary standard exactly when $B/R$ is smooth and $\Omega_{B/R}$ has a finite basis $\mathrm db_1,\ldots,\mathrm db_d$ represented by elements $b_i\in A$. Having even one elementary positive power implies both these conditions.

In (f) the representatives must come from $A$, rather than merely from $B$. Property (4) by itself does not give elementary powers over an arbitrary base. The proof ends with a complete example establishing that distinction.

**Proof of (a)--(e).**
By [F.85](#algebra-lemma-standard-smooth), a standard smooth algebra is smooth and its differentials are free. A free module is stably free by adding the zero free module; forgetting this condition gives (a). For (b), take the coefficients of the other minors to be zero in D.3s1; transposing the one square minor does not change its determinant. D.3e2 and D.3s2 are the same relation condition.

For (c), use an elementary presentation $A=P/I$, where $P=R[x_1,\ldots,x_n]$, $I=(f_1,\ldots,f_m)$ and the first $c$ equations have minor $\Delta$. Lift $a$ to $h\in P$. Write
$$B=A_a=P[x_0]/J,\qquad J=(x_0h-1,f_1,\ldots,f_m),$$
and $K=(x_0h-1,f_1,\ldots,f_c)$. The localization conormal calculation [F.72](#algebra-lemma-principal-localization-NL) and D.3e2 give $J=K+J^2$: after inverting $a$, the classes of the remaining $f_j$ are combinations of the first $c$ classes. The module $J/K$ is finite, since $J$ has the displayed finite generating list, and satisfies $J/K=J(J/K)$. Choose generators $v_i$ and write $v_i=\sum_j b_{ij}v_j$ with $b_{ij}\in J$. Multiplication by the adjugate of $(\delta_{ij}-b_{ij})$, whose identity is proved in [F.70](#algebra-lemma-matrix-left-inverse), shows that
$$g=\det(\delta_{ij}-b_{ij})\in1+J,\qquad gJ\subset K.$$
For the zero module choose $g=1$. Thus $J_g=K_g$. Since $g$ maps to $1$ in $B$, adjoining an inverse for it does not change $B$, and
$$B=P[x_0,z]/(x_0h-1,f_1,\ldots,f_c,gz-1).$$
For these ordered equations select $(x_0,x_1,\ldots,x_c,z)$. The first $c+1$ rows have zero last column. Their first $c+1$ columns form the block matrix with upper left entry $h$, lower left zero, and lower right Jacobian minor $\Delta$. The last diagonal entry of the whole matrix is $g$. Its determinant is therefore $gh\Delta$. In $B$, $g=1$, $h=a$ is a unit, and D.3e1 gives $a=a'\Delta$, so $\Delta^{-1}=a'/a$. This proves standard smoothness, including the empty minor case $c=0$.

For (d), D.3s2 makes the first $c$ equation classes generate $M=(I/I^2)_a$. D.4 and D.3s1 give a map back from $B^n$ whose composite with the map $B^c\to M\to B^n$ is multiplication by the unit $a$. Thus $B^c\to M$ is both surjective and injective, and the conormal differential is a split injection. D.5 proves that $B=A_a$ is smooth. The localized conormal sequence, by F.65 and F.72, now gives
$$M\oplus\Omega_{B/R}\cong B^n,\qquad M\cong B^c.$$
Consequently $\Omega_{B/R}\oplus B^c\cong B^n$, exactly the required stable freeness.

For (e), start with a finite presentation $A=R[X_1,\ldots,X_n]/I$ and $B=A_a$. If $B=0$, the equality $1/1=0$ means $a^L=0$ for some $L$. For every $e\ge L$, take $c=0$ in any finite presentation: the empty minor is $1$ and all multiplied relation classes are zero. Such powers are elementary, hence strictly standard. Assume $B\ne0$. Smoothness, the conormal description of the naive cotangent complex, and F.65/F.72 give the split exact sequence
$$0\to M=(I/I^2)_a\to B^n\to\Omega_{B/R}\to0.$$
If $\Omega_{B/R}\oplus B^s\cong B^t$, then $M\oplus B^t\cong B^{n+s}$. Add $t$ variables $Y_i$ mapping to zero in $A$. The kernel of this enlarged presentation is $J=(I,Y_1,\ldots,Y_t)$, and
$$J/J^2\cong I/I^2\oplus A^t.$$
Indeed, evaluation at $Y=0$ gives the first component, and the coefficients of the terms linear in $Y$ modulo $I$ give the second; their kernel consists precisely of products of two elements of $J$. The differential sends the new generators to the independent $\mathrm dY_i$. Thus $(J/J^2)_a$ is finite free and its differential is a split injection into $B^{n+t}$.

Choose representatives $f_1,\ldots,f_c\in J$ of a basis after localization: a basis element is a fraction of an element of $J/J^2$, and multiplying each basis element by its own denominator, a unit in $B$, still gives a basis. Extend them to a finite generating list $f_1,\ldots,f_m$ of $J$. Finiteness follows from [F.44](#algebra-lemma-finite-presentation-independent), or directly from the old finite list and the new variables. Each remaining class is zero in the localization of
$$Q=(J/J^2)/\langle f_1,\ldots,f_c\rangle.$$
For each of its finitely many generators some power of $a$ kills that class. Choose a common exponent $L$. For a polynomial lift $h$ of $a$ this says
$$h^L f_j\in(f_1,\ldots,f_c)+J^2\qquad(j>c).$$
Multiplying by further powers of $h$ gives D.3s2 for every $a^e$, $e\ge L$.

Let $F$ be the $(n+t)\times c$ matrix of the differentials of the first $c$ equations over $A$. The split injection after localization has a matrix left inverse $P$ over $B$. Choose $u$ and a matrix $P_0$ over $A$ with $(P_0)_a=a^uP$. Every entry of $P_0F-a^u1_c$ becomes zero in $B$, so a common further power $a^v$ kills all those finitely many entries. Hence
$$P_1F=a^{u+v}1_c,\qquad P_1=a^vP_0,$$
as an exact equality over $A$. Increase $u+v$ to a positive integer $k$ by multiplying $P_1$ by an additional power of $a$ if necessary. No power of $a$ has been cancelled. F.70 puts $a^{ck}$ in the ideal of the $c\times c$ minors of $F$. Reduction at a prime of the nonzero ring $B$ shows $c\le n+t$. For every $e\ge\max(L,ck,1)$, multiply the minor coefficients by $a^{e-ck}$ to obtain D.3s1, together with the already established D.3s2. When $c=0$, the minor ideal is $A$ and the same conclusion uses the empty determinant $1$. This proves (e) over arbitrary rings, including zero divisors. ∎

**Proof of (f).** Put $B=A_a$. If $B=0$, some power $a^L$ is zero. The zero differential module has the empty basis, and, as in (e), every $a^e$ with $e\ge\max(L,1)$ is elementary using $c=0$ and the empty minor $1$. Assume $B\ne0$.

First suppose $B$ is smooth and $\mathrm db_1,\ldots,\mathrm db_d$ is a basis with $b_i\in A$. Choose finite algebra generators $z_1,\ldots,z_n$ of $A$ over $R$ and the surjection
$$P=R[X_1,\ldots,X_n,Y_1,\ldots,Y_d]\longrightarrow A,
\qquad X_i\longmapsto z_i,\quad Y_j\longmapsto b_j.$$
Its kernel $J$ is finitely generated by [F.44](#algebra-lemma-finite-presentation-independent). The smoothness definition [F.6](#algebra-definition-smooth), the presentation description of the naive cotangent complex [F.11](#algebra-lemma-NL-homotopy), and localization [F.65](#algebra-lemma-localize-NL) give the exact sequence
$$0\longrightarrow M=(J/J^2)_a\xrightarrow{\mathrm d}
B^n\oplus B^d\longrightarrow\Omega_{B/R}\longrightarrow0.$$
Here the two summands have coordinates $\mathrm dX_i$ and $\mathrm dY_j$. The map from the second summand to $\Omega_{B/R}$ is an isomorphism, because its images are the chosen basis. Consequently projection onto the first summand restricts to an isomorphism $M\to B^n$: for each $v\in B^n$, there is a unique $w\in B^d$ whose differential image cancels that of $v$, so $(v,w)$ is in the image of $M$; a vector of $M$ with first component zero has second component zero as well. Injectivity of $\mathrm d$ proves uniqueness in $M$.

Let $\eta_1,\ldots,\eta_n$ be the resulting basis of $M$ whose projected differentials are the standard basis of $B^n$. Write each $\eta_i$ as a fraction of a class represented by $f_i\in J$, with denominator $a^{k_i}$. Thus the classes of $f_i$ are $a^{k_i}\eta_i$, still a basis over $B$. Their square Jacobian on $X_1,\ldots,X_n$ is diagonal after passage to $B$, with entries $a^{k_i}$. In particular the image of
$$\delta=\det(\partial f_i/\partial X_j)_{i,j=1}^n\in A$$
is a unit in $B$. Extend $f_1,\ldots,f_n$ to a finite generating list $f_1,\ldots,f_m$ of $J$. The finite module
$$Q=(J/J^2)/\langle f_1,\ldots,f_n\rangle$$
has zero localization at $a$. A common power $a^L$ kills its finite generating list. For a polynomial lift $h\in P$ of $a$, this means
$$h^L f_j\in(f_1,\ldots,f_n)+J^2\qquad(j>n).$$
All higher powers satisfy the same relation condition.

Since $\delta$ is a unit in $B$, choose $u\in A$ and $r\ge0$ with $\delta(u/a^r)=1$ in $B$. The equality in this localization supplies $v\ge0$ such that
$$a^v(\delta u-a^r)=0\quad\hbox{in }A,
\qquad a^{r+v}=\delta(a^v u).$$
Increase the exponent to a positive $K$ by multiplying this equality by an additional power of $a$ if necessary. This gives $a^K=\delta u_0$ in $A$, without cancelling a power of a possible zero divisor. Every $e\ge\max(K,L,1)$ then satisfies both D.3e1 and D.3e2 for the presentation $A=P/J$, with $c=n$ and the selected variables $X_i$. This proves the forward direction, including $n=0$, when $\delta$ is the empty determinant $1$.

Conversely, suppose $a^r$ is elementary for some $r\ge1$. Inverting $a^r$ is the same as inverting $a$, since $a^{-1}=a^{r-1}(a^r)^{-1}$. Part (c), applied to $a^r$, proves that $B$ is standard smooth, hence smooth. Take its elementary presentation $A=R[x_1,\ldots,x_N]/I$ with $I=(g_1,\ldots,g_m)$ and selected minor on $x_1,\ldots,x_c$. In $B$, D.3e2 makes every remaining conormal class a combination of the first $c$. Therefore
$$\Omega_{B/R}=B^N/\langle\mathrm dg_1,\ldots,\mathrm dg_c\rangle.$$
The selected $c\times c$ Jacobian block is invertible. Subtracting a unique combination of these $c$ differential rows eliminates the first $c$ coordinates of any vector in $B^N$; a combination with those coordinates zero has all its coefficients zero. Hence the images of $\mathrm dx_{c+1},\ldots,\mathrm dx_N$ form a basis of this quotient. Their representatives are elements of $A$. The forward direction now proves that every sufficiently large power is elementary. This proves (f). ∎

**Why standard smoothness alone is insufficient.** Take
$$R=\mathbf Z,\qquad A=\mathbf Z[t^2,t^3]\subset\mathbf Z[t],\qquad a=t^2.$$
This algebra has the finite presentation
$$A\cong\mathbf Z[X,Y]/(Y^2-X^3),\qquad X\longmapsto t^2,\quad Y\longmapsto t^3.$$
Indeed division by the monic polynomial $Y^2-X^3$ writes every class uniquely as $p(X)+Yq(X)$. After substitution, the first summand has even exponents and the second has odd exponents at least $3$; their disjoint monomials prove injectivity. The image is precisely the indicated subalgebra.

Inverting $a$ gives
$$B=A_a=\mathbf Z[t,t^{-1}],\qquad t=Y/X,\quad t^{-1}=Y/X^2.$$
These identities follow from $Y^2=X^3$ and give both inclusions with the Laurent ring. The presentation $B=\mathbf Z[T,U]/(TU-1)$ is standard smooth: select $U$ for its one equation, whose derivative is the unit $T$. Every derivation of $B$ is uniquely determined by its value on $t$, with $\mathrm d(t^{-1})=-t^{-2}\mathrm dt$. Thus $\Omega_{B/\mathbf Z}=B\,\mathrm dt$.

The units of $\mathbf Z[t,t^{-1}]$ are exactly $\pm t^k$. To check this, the lowest and highest nonzero exponents of a product add, since their coefficients are nonzero products in the domain $\mathbf Z$. For a product equal to $1$, each factor must therefore have width zero and be a monomial; its integer coefficient must be $1$ or $-1$.

Every $b\in A$ has the form $b_0+\sum_{k\ge2}b_k t^k$, with integer coefficients and a finite sum. Consequently
$$\mathrm db=\left(\sum_{k\ge2}k b_k t^{k-1}\right)\mathrm dt.$$
This coefficient cannot be a unit: if it were $\pm t^j$, necessarily $j\ge1$, and its sole coefficient would require $(j+1)b_{j+1}=\pm1$, impossible in $\mathbf Z$. A basis of the free rank-one module $B\,\mathrm dt$ must contain one generator; tensoring with $\mathbf Q(t)$ verifies that its length is one. Hence it has no basis consisting of differentials of elements of $A$. By the converse in (f), no positive power of $a$ is elementary standard, despite standard smoothness of $B$.

There is no conflict with (e). In the original cusp presentation the two one-by-one minors are $-3X^2$ and $2Y$, and in $A$
$$X^3=(-X)(-3X^2)+(-Y)(2Y).$$
The relation condition is empty because there is only one equation. Thus $a^3$, and every $a^e$ with $e\ge3$ after multiplication by $a^{e-3}$, is strictly standard. This exact example distinguishes the sum-of-minors condition from the single-minor condition over the same arbitrary base.

### The lifting problem

<a id="smoothing-section-lifting"></a>

[D.18](#smoothing-proposition-lift) lifts a smooth filtered presentation across a nilpotent ideal when the target remains flat. Its two preliminary steps use the explicit smooth presentations constructed in the [preceding section](#smoothing-section-presentations).

<a id="smoothing-lemma-lift-once"></a>

#### Lemma D.16: lift once

Reading source: [Stacks, Tag 07CK](https://stacks.math.columbia.edu/tag/07CK).

Let $R\to\Lambda$ be a ring map and $I\subset R$ an ideal with $I^2=0$. Suppose that $\Lambda/I\Lambda$ is a filtered colimit of smooth $R/I$-algebras. Every map $\varphi:A\to\Lambda$ from a finitely presented $R$-algebra factors as
$$A\longrightarrow B/J\longrightarrow\Lambda,$$
where $B/R$ is smooth and $J\subset IB$ is a finitely generated ideal. Neither $R$ nor $I$ is required to be Noetherian or finite.

**Proof.** Write $\bar R=R/I$ and $\bar A=A/IA$. By [D.13](#smoothing-lemma-colimit-standard-smooth), the induced map $\bar A\to\Lambda/I\Lambda$ factors through a standard smooth $\bar R$-algebra $C$. This factorization occurs at a finite stage: take representatives for the finite generators of $\bar A$ and then a common successor where all its finitely many equations vanish.

There is a finite presentation $C=\bar A[t_1,\ldots,t_r]/(\bar g_1,\ldots,\bar g_s)$ relative to this specified map. To see the finiteness directly, choose $C=\bar R[t]/(k_1,\ldots,k_v)$ and generators $a_1,\ldots,a_u$ of $\bar A$. Represent their images by polynomials $v_i(t)$. Over $\bar A[t]$, the finite equations $k_j(t)$ and $a_i-v_i(t)$ give exactly $C$: substituting for the $a_i$ recovers its displayed $\bar R$-presentation. Include these equations in the list $\bar g$.

Lift each $\bar g_i$ to $g_i\in A[t]$ and the images of the $t_j$ in $\Lambda/I\Lambda$ to $\lambda_j\in\Lambda$. Evaluation gives a finite expression
$$\varphi(g_i)(\lambda)=\sum_{j=1}^{q_i}\epsilon_{ij}\mu_{ij},\qquad \epsilon_{ij}\in I,\quad\mu_{ij}\in\Lambda.$$
Introduce one variable $z_{ij}$ for each of these terms and set
$$T=A[t,z]/\bigl(g_i-\sum_j\epsilon_{ij}z_{ij}\bigr).$$
This is finitely presented over $R$, by combining the finite presentation of $A$ with the displayed lists. The assignments $a\mapsto\varphi(a)$, $t_j\mapsto\lambda_j$, $z_{ij}\mapsto\mu_{ij}$ define $T\to\Lambda$, and reduction gives
$$T/IT\cong C[z].$$
Adjoining free variables to a standard smooth presentation preserves its invertible Jacobian minor: retain the equations and their pivot variables. Thus choose
$$T/IT=(R/I)[X_1,\ldots,X_n]/(\bar f_1,\ldots,\bar f_c)$$
with $\bar\Delta=\det(\partial\bar f_i/\partial X_j)_{1\leq i,j\leq c}$ invertible. Lift the $f_i$ to $R[X]$, put $\Delta=\det(\partial f_i/\partial X_j)_{1\leq i,j\leq c}$, and form
$$B=R[X_1,\ldots,X_n,W]/(f_1,\ldots,f_c,W\Delta-1).$$
On pivots $X_1,\ldots,X_c,W$, its Jacobian has upper right block zero and lower right entry $\Delta$; its determinant is $\Delta^2$, a unit in $B$. It is therefore standard smooth, hence smooth by [F.85](#algebra-lemma-standard-smooth). Its reduction is precisely $T/IT$, since $W$ becomes the inverse of $\bar\Delta$.

We construct a map $\psi:B\to T$ inducing that isomorphism. Choose lifts $y_i\in T$ of the displayed coordinate classes in $T/IT$, and let $L=IT$, so $L^2=0$. The element $\Delta(y)$ is a unit: a lift $d$ of its modular inverse satisfies $\Delta(y)d=1+\ell$ with $\ell\in L$, and $(1+\ell)^{-1}=1-\ell$. Let $H=(\partial f_i/\partial X_j(y))_{1\leq i,j\leq c}$. Its determinant is $\Delta(y)$, so the cofactor identity proved in [F.70](#algebra-lemma-matrix-left-inverse) gives an inverse matrix. Every $f_i(y)$ lies in $L$. Choose
$$ (u_1,\ldots,u_c)^{\mathsf t}=-H^{-1}(f_1(y),\ldots,f_c(y))^{\mathsf t}\in L^c$$
and set $u_j=0$ for $j>c$. Expanding each monomial, all terms with two correction factors vanish in $L^2$, and hence
$$ f_i(y+u)=f_i(y)+\sum_{j=1}^c\frac{\partial f_i}{\partial X_j}(y)u_j=0.$$
The new determinant is still a unit because its reduction is unchanged. Set $\psi(X_i)=y_i+u_i$ and $\psi(W)=\Delta(y+u)^{-1}$. These assignments satisfy every equation of $B$ and lift the required reduction map.

The map $\psi$ is onto without a finiteness assumption on $I$. For $t\in T$, lift its reduction to $b\in B$ and write $t-\psi(b)=\sum_\nu\eta_\nu t_\nu$ with $\eta_\nu\in I$. Lift each reduction of $t_\nu$ to $b_\nu\in B$. Since $I(IT)=0$, one obtains $t=\psi(b+\sum_\nu\eta_\nu b_\nu)$. Its kernel $J$ lies in $IB$, because $B/IB\to T/IT$ is injective. To prove that $J$ is finite, compose the finite polynomial presentation $R[X,W]\twoheadrightarrow B$ with $\psi$. The kernel of the resulting surjection to the finitely presented algebra $T$ is finite by [F.44](#algebra-lemma-finite-presentation-independent). Its images in $B$ generate $J$. Thus $T\cong B/J$, and the maps $A\to T\to\Lambda$ give the claimed factorization. Empty equation lists use $\Delta=1$ and require no correction coordinates. ∎

<a id="smoothing-lemma-lift-twice"></a>

#### Lemma D.17: lift twice

Reading source: [Stacks, Tag 07CL](https://stacks.math.columbia.edu/tag/07CL).

Let $R\to\Lambda$ be flat, let $I^2=0$, and suppose that $\Lambda/I\Lambda$ is a filtered colimit of smooth $R/I$-algebras. If $B/R$ is smooth, $\varphi:B\to\Lambda$ is an $R$-map, and $J\subset IB$ is a finitely generated ideal with $\varphi(J)=0$, there are maps
$$B\xrightarrow{\alpha}B'\xrightarrow{\beta}\Lambda$$
with $B'/R$ smooth, $\alpha(J)=0$, and the exact equality $\beta\alpha=\varphi$.

**Proof.** We first give the square-zero lifting calculation needed below. For any smooth $R$-algebra $B$, any $R$-algebra $E$, any ideal $L\subset E$ with $L^2=0$, and any $R$-map $\gamma:B\to E/L$, there is a lift $B\to E$. Choose a finite polynomial presentation $P=R[Z_1,\ldots,Z_n]\twoheadrightarrow B$, with kernel $K$, and lifts $e_i\in E$ of $\gamma(Z_i)$. Evaluation of a relation $f\in K$ lies in $L$ and vanishes on $K^2$. It gives a $B$-linear map
$$\delta:K/K^2\longrightarrow L,$$
where $L$ is a $B$-module through $\gamma$; its $E/L$-module structure is well defined because $L^2=0$. Indeed evaluation of $pf$ is evaluation of $p$ times evaluation of $f$, and that multiplication on $L$ depends only on $p$ modulo $K$ and $E$ modulo $L$.

By the definition [F.6](#algebra-definition-smooth) and presentation comparison [F.11](#algebra-lemma-NL-homotopy), the sequence
$$0\longrightarrow K/K^2\xrightarrow{d}B^n\longrightarrow\Omega_{B/R}\longrightarrow0$$
is exact and its last module is finite projective. This sequence splits: realize that projective module as a direct summand of a finite free module, lift the free basis through the surjection, and restrict the lift to the summand. The resulting section defines a retraction $r:B^n\to K/K^2$ of $d$. Put $\ell=\delta r:B^n\to L$ and $c_i=\ell(dZ_i)$. Evaluate polynomials instead at $e_i-c_i$. The monomial expansion, using $L^2=0$, gives for each $f\in K$
$$ f(e-c)=f(e)-\sum_i\frac{\partial f}{\partial Z_i}(e)c_i
 =\delta([f])-\ell(d[f])=0.$$
In the second equality the derivative coefficients act on $L$ through their images under $\gamma$, so no choice of their lifts changes the product. Evaluation therefore descends to $B\to E$ and lifts $\gamma$. This proves the needed lifting statement in full arbitrary-ring scope.

Now suppose first that $J=(h)$. Write $h=\sum_{i=1}^q\epsilon_i b_i$ with $\epsilon_i\in I$ and $b_i\in B$. Consider the row map $v:R^q\to R$, $v(a)=\sum_i\epsilon_i a_i$, and let $K_v=\ker v$, $H_v=\operatorname{im}v$. Flatness preserves the two exact sequences $0\to K_v\to R^q\to H_v\to0$ and $0\to H_v\to R$. Consequently
$$\ker(v\otimes_R\Lambda)=\operatorname{im}(K_v\otimes_R\Lambda\longrightarrow\Lambda^q).$$
The vector $(\varphi(b_i))_i$ belongs to this kernel, since $\varphi(h)=0$. An element of a tensor product is a finite sum of pure tensors. Thus there are finitely many $\lambda_j\in\Lambda$ and columns $(a_{ij})_i\in K_v$ with
$$\varphi(b_i)=\sum_{j=1}^m a_{ij}\lambda_j,\qquad
\sum_i\epsilon_i a_{ij}=0\quad\text{for each }j.$$
This derives the finite relation directly from flatness, including the case of a zero vector and an empty tensor sum.

Set $C=B[T_1,\ldots,T_m]/(b_i-\sum_j a_{ij}T_j)$. Its finite presentation follows by appending these variables and equations to a finite presentation of $B$. The displayed relations define a map $C\to\Lambda$ extending $\varphi$, with $T_j\mapsto\lambda_j$. By [D.16](#smoothing-lemma-lift-once) this map factors through $E/J'$, where $E/R$ is smooth and $J'\subset IE$ is finite. In particular $(J')^2=0$. Apply the lifting calculation above to $B\to C\to E/J'$ and obtain $\alpha:B\to E$. Let $\beta:E\to E/J'\to\Lambda$. Since the reduction of $\alpha$ is the original map through $C$, one has $\beta\alpha=\varphi$ exactly.

Choose lifts $\xi_j\in E$ of the images of $T_j$. The equations in $C$ give $\alpha(b_i)=\sum_j a_{ij}\xi_j+\theta_i$ for some $\theta_i\in J'$. Therefore
$$\alpha(h)=\sum_j\Bigl(\sum_i\epsilon_i a_{ij}\Bigr)\xi_j
              +\sum_i\epsilon_i\theta_i=0.$$
The first sum vanishes by the column relations, the second because $IJ'\subset I^2E=0$. This proves the one-generator case, with $B'=E$.

For $J=(h_1,\ldots,h_s)$, apply that construction successively to the image of $h_i$ in the smooth algebra obtained at the preceding step. Each such image lies in $I$ times that algebra, and its map to $\Lambda$ is zero because the composite to $\Lambda$ remains $\varphi$. Each new map preserves the previously killed generators. After finitely many steps their composite kills every generator, hence the whole ideal $J$, and still factors $\varphi$ exactly. If $J=0$, take $B'=B$, $\alpha=1$, and $\beta=\varphi$. ∎

<a id="smoothing-proposition-lift"></a>

#### Proposition D.18: lift

Reading source: [Stacks, Tag 07CM](https://stacks.math.columbia.edu/tag/07CM).

Suppose that $R\to\Lambda$ is flat, $I\subset R$ is nilpotent, and $\Lambda/I\Lambda$ is a filtered colimit of smooth $R/I$-algebras. Then $\Lambda$ is a filtered colimit of smooth $R$-algebras.

**Proof.** Begin with $I^2=0$. Given any $R$-map $A\to\Lambda$ from a finitely presented algebra, [D.16](#smoothing-lemma-lift-once) gives maps $A\to B/J\to\Lambda$ with $B/R$ smooth, $J\subset IB$ finite. Let $\varphi:B\to\Lambda$ be the induced map; it kills $J$. The flat map and the same square-zero ideal meet every hypothesis of [D.17](#smoothing-lemma-lift-twice). Obtain $B\to B'\to\Lambda$ with $B'/R$ smooth and $J$ killed in $B'$. The first arrow descends to $B/J\to B'$, and its composite to $\Lambda$ is the given quotient map because D.17 gives equality of the maps from $B$. Thus $A\to B'\to\Lambda$ is an exact factorization of the original map. Criterion [F.90](#algebra-lemma-when-colimit), whose filtered-category construction and colimit isomorphism are proved there, gives the assertion for square-zero ideals.

Induct on a positive integer $n$ with $I^n=0$. For $n=1$ the ideal is zero and the assertion is the hypothesis. For $n\geq2$, set $J=I^{n-1}$, so $J^2=0$ because $2n-2\geq n$. Over $\bar R=R/J$ put $\bar\Lambda=\Lambda/J\Lambda$ and $\bar I=I/J$. Then $\bar I^{n-1}=0$ and $\bar\Lambda/\bar I\bar\Lambda=\Lambda/I\Lambda$. The map $\bar R\to\bar\Lambda$ is flat: for every $\bar R$-module $M$ the maps on pure tensors give
$$M\otimes_{\bar R}(\Lambda/J\Lambda)\cong M\otimes_R\Lambda.$$
Here tensors involving $J\Lambda$ vanish because $JM=0$; this verifies the inverse maps as well. An exact sequence of $\bar R$-modules is exact over $R$, so the original flatness makes the displayed tensor functor exact. The induction hypothesis therefore expresses $\bar\Lambda$ as a filtered colimit of smooth $\bar R$-algebras. Apply the square-zero case already proved to $J\subset R$ and the original flat map $R\to\Lambda$. Its quotient is exactly this smooth colimit, hence it expresses $\Lambda$ as a filtered colimit of smooth $R$-algebras. This completes the induction without assuming that the nilpotent ideal is finitely generated. ∎

### The lifting lemma

<a id="smoothing-section-lifting-lemma"></a>

[D.19](#smoothing-lemma-lifting) constructs a finitely presented algebra whose smooth locus lifts the prescribed quotient data.

<a id="smoothing-lemma-lifting"></a>

#### Lemma D.19: lifting

Reading source: [Stacks, Tag 07CP](https://stacks.math.columbia.edu/tag/07CP).

Let \(R\) be Noetherian, let \(\pi\in R\), let \(\Lambda\) be an \(R\)-algebra, and assume
\[
\operatorname{Ann}_R(\pi)=\operatorname{Ann}_R(\pi^2),
\qquad
\operatorname{Ann}_\Lambda(\pi)=\operatorname{Ann}_\Lambda(\pi^2).
\]
Given a finitely presented \(R/\pi^2R\)-algebra \(\bar C\) and a map \(\bar C\to\Lambda/\pi^2\Lambda\), there is a finitely presented \(R\)-algebra \(D\), a map \(D\to\Lambda\), and commuting maps
\[
\begin{array}{ccccc}
R/\pi^2R&\longrightarrow&\bar C&\longrightarrow&\Lambda/\pi^2\Lambda\\
\downarrow&&\downarrow&&\downarrow\\
R/\pi R&\longrightarrow&D/\pi D&\longrightarrow&\Lambda/\pi\Lambda.
\end{array}
\]
The map \(R\to D\) is smooth at every prime avoiding \(\pi\). It is also smooth at each prime containing \(\pi\) whose inverse image in \(\bar C\) is smooth over \(R/\pi^2R\). At these latter primes, \(\bar C/\pi\bar C\to D/\pi D\) is smooth as well.

**Proof.** Put \(P=R[x_1,\ldots,x_n]\) and choose lifts \(f_1,\ldots,f_m\in P\) of a finite relation list for
\[
\bar C=(R/\pi^2R)[x_1,\ldots,x_n]/(\bar f_1,\ldots,\bar f_m).
\]
Write \(\bar P=(R/\pi^2R)[x]\) and \(\bar J=(\bar f_1,\ldots,\bar f_m)\). Thus the kernel of \(P\to\bar C\) is \((f_1,\ldots,f_m)+\pi^2P\); \(\pi^2\) need not be in the chosen list.

At a smooth prime, [D.2](#smoothing-lemma-find-strictly-standard) supplies a principal neighbourhood, selected equation indices \(E\), and equally many variable indices \(U\). On that neighbourhood the selected Jacobian minor \(\delta\) is a unit and the selected classes generate \(\bar J/\bar J^2\). They are a basis: their composite with the conormal differential projected onto the \(U\)-coordinates is invertible, so a relation among them is zero. Shrink the polynomial neighbourhood to make \(\bar J\) itself generated by these selected equations. Here are the details of that shrinking. The finite module
\[
M=(\bar J/(\bar f_j:j\in E))_a
\]
satisfies \(M=\bar J_aM\). The determinant form of [F.10](#algebra-lemma-NAK) gives \(b'\in\bar J_a\) with \((1+b')M=0\). Write \(b'=b/a^N\), with \(b\in\bar J\). Replacing the polynomial \(a\) by \(a(a^N+b)\) inverts \(1+b'\). Its image in \(\bar C\) is the old \(a^{N+1}\), so this replacement preserves the principal open in \(\operatorname{Spec}\bar C\).

These principal opens cover the smooth locus. They have a finite subcover for an algebraic reason: \(\bar C\) is Noetherian by [S01, Lemma 1.3](AG-RG-S01.md), so the ideal generated by all their defining elements is generated by finitely many of those elements. To obtain such a list, express a finite ideal generating list as finite sums of the original elements and collect those that occur. Their principal opens have the same union. Index the resulting charts by \(k=1,\ldots,r\). An empty smooth locus uses \(r=0\).

Clear the finitely many denominators in the equality of localized relation ideals on each chart and replace its \(a_k\) by a sufficiently large positive power. There are then exact identities in \(P\)
\[
a_kf_\ell=\sum_{j\in E_k}h_{k\ell}^jf_j+\pi^2g_{k\ell}.
\tag{D.19a}
\]
For \(\ell\in E_k\), take \(h_{k\ell}^j=a_k\delta_{\ell j}\) and \(g_{k\ell}=0\). The selected conormal classes remain a basis on \(\bar C_{a_k}\), and the selected Jacobian minor \(\delta_k\) remains invertible there.

In \(Q=P[z_1,\ldots,z_m]\), put
\[
F_\ell=f_\ell-\pi z_\ell,\qquad
p_{k\ell}=a_kz_\ell-\sum_{j\in E_k}h_{k\ell}^jz_j-\pi g_{k\ell},
\]
and define \(D=Q/(F_\ell,p_{k\ell})_{\ell,k}\). All lists are finite. Choose lifts \(\lambda_i\in\Lambda\) of the prescribed images of \(x_i\), and write \(f_\ell(\lambda)=\pi^2\mu_\ell\). Send \(x_i\) to \(\lambda_i\) and \(z_\ell\) to \(\pi\mu_\ell\). The \(F_\ell\) vanish. Evaluation of (D.19a) shows that
\[
\pi^2\left(a_k(\lambda)\mu_\ell-
\sum_{j\in E_k}h_{k\ell}^j(\lambda)\mu_j-g_{k\ell}(\lambda)\right)=0.
\]
The annihilator hypothesis in \(\Lambda\) makes its product with \(\pi\) zero; that product is exactly the image of \(p_{k\ell}\). This defines \(D\to\Lambda\). Reduction of \(F_\ell=0\) modulo \(\pi\) defines \(\bar C\to D/\pi D\), and the variable assignments verify every square in the displayed diagram.

The polynomial identity
\[
\pi p_{k\ell}=-a_kF_\ell+\sum_{j\in E_k}h_{k\ell}^jF_j
\tag{D.19b}
\]
follows by substituting (D.19a). After inverting \(\pi\), all \(p_{k\ell}\) follow from the \(F_\ell\), and \(F_\ell=0\) eliminates \(z_\ell=f_\ell/\pi\). Thus \(D_\pi=R_\pi[x]\), a polynomial localization smooth over \(R\) by the empty-equation and inverse-variable cases of [F.85](#algebra-lemma-standard-smooth).

Fix \(k\), and retain only its selected equations and its own compatibility equations:
\[
D_k=Q/(F_j:j\in E_k,\ p_{k\ell}:\ell\notin E_k).
\]
There is a surjection \(D_k\to D\). Let \(\mathfrak q\subset D\) contain \(\pi\) and lie over a smooth prime of \(\bar C\); choose \(k\) with \(a_k\notin\mathfrak q\), and let \(\mathfrak q_k\) be its inverse image in \(D_k\). In \(D_k/\pi D_k\), after inverting \(a_k\), each \(z_\ell\) for \(\ell\notin E_k\) is uniquely
\[
z_\ell=a_k^{-1}\sum_{j\in E_k}h_{k\ell}^jz_j.
\]
Substitution and its reverse on the remaining variables give the actual isomorphism
\[
(D_k/\pi D_k)_{a_k}
 \cong(\bar C/\pi\bar C)_{a_k}[z_j:j\in E_k].
\tag{D.19c}
\]
Here the equality of the relation ideals modulo \(\pi^2\) also gives their equality modulo \(\pi\).

There are \(m\) equations in this presentation of \(D_k\). Choose as pivot variables \(x_i\), \(i\in U_k\), followed by \(z_\ell\), \(\ell\notin E_k\). Their Jacobian modulo \(\pi\), with selected equations first, has blocks
\[
\begin{pmatrix}
(\partial f_j/\partial x_i)_{j\in E_k,i\in U_k}&0\\
*&a_k1_{m-|E_k|}
\end{pmatrix}.
\]
Its determinant is \(\delta_k a_k^{m-|E_k|}\), invertible at \(\mathfrak q_k\). If \(\Delta_k\) denotes the determinant before reduction, \((D_k)_{a_k\Delta_k}\) is standard smooth: adjoining an inverse of \(a_k\Delta_k\) adds one equation and one pivot, whose block determinant is \((a_k\Delta_k)\Delta_k\). [F.85](#algebra-lemma-standard-smooth) proves smoothness. [F.83](#algebra-lemma-smooth-syntomic), with the Noetherian base \(R\), proves flatness of this smooth chart. Localization is exact by [S01, Lemma 1.1](AG-RG-S01.md), so \(T=(D_k)_{\mathfrak q_k}\) is flat over \(R\).

We now show that every additional relation of \(D_k\to D\) vanishes in \(T\). First (D.19b), with the \(k\)-relations zero and \(a_k\) invertible, gives \(F_\ell=0\) for all \(\ell\). For another chart \(k'\), set
\[
b_{kk'\ell}^j=a_{k'}h_{k\ell}^j-
\sum_{j'\in E_{k'}}h_{k'\ell}^{j'}h_{kj'}^j
\quad(j\in E_k).
\]
Reduce (D.19a) modulo \(\pi^2\) and express \(a_ka_{k'}[\bar f_\ell]\) in the conormal basis indexed by \(E_k\) in the two possible orders. The difference is \(\sum_{j\in E_k}b_{kk'\ell}^j[\bar f_j]=0\). Basis independence therefore makes every coefficient zero in \(\bar C_{a_k}\). Equivalently,
\[
b_{kk'\ell}^j\in
((f_j:j\in E_k)+\pi^2P)_{a_k}.
\]
Its image in \((D_k)_{a_k}\) belongs to \(\pi(D_k)_{a_k}\), since every selected \(f_j\) equals \(\pi z_j\). Directly expanding the definitions, modulo \(\pi\), gives
\[
a_kp_{k'\ell}-a_{k'}p_{k\ell}
+\sum_{j'\in E_{k'}}h_{k'\ell}^{j'}p_{kj'}
=\sum_{j\in E_k}b_{kk'\ell}^jz_j.
\]
Consequently \(p_{k'\ell}\in\pi T\). Identity (D.19b) for \(k'\) also gives \(\pi p_{k'\ell}=0\) in \(T\).

Flat tensor applied to the multiplication-kernel sequences identifies
\[
\operatorname{Ann}_T(\pi^e)
=\operatorname{im}(\operatorname{Ann}_R(\pi^e)\otimes_RT\to T)
\qquad(e=1,2).
\]
Indeed, factor multiplication through its image and tensor its short exact kernel sequence and that image's injection into \(R\); flatness preserves both. The assumed equality over \(R\) thus gives equality of these annihilators in \(T\). For \(p=p_{k'\ell}=\pi u\), the equality \(\pi p=0\) means \(\pi^2u=0\); it follows that \(p=\pi u=0\). This kills all additional generators.

Finally this local calculation supplies genuine neighbourhoods. The kernel of \(D_k\to D\) is generated by the finite lists of additional \(F_\ell\) and \(p_{k'\ell}\). For each generator, vanishing at \(\mathfrak q_k\) gives an element outside \(\mathfrak q_k\) killing it. Their product \(s\) kills the entire kernel. The surjection therefore becomes an isomorphism after inverting \(a_k\Delta_ks\), which still avoids \(\mathfrak q_k\). This identifies a principal neighbourhood of \(\mathfrak q\) with a localization of the standard smooth chart, proving the required smoothness of \(R\to D\) by F.85 and [F.7](#algebra-definition-smooth-at-prime). Modulo \(\pi\), (D.19c) identifies the same neighbourhood with a localization of a polynomial algebra over \(\bar C/\pi\bar C\): denominators in the \(a_k\)-localized polynomial algebra can be cleared by a power of \(a_k\). F.85 proves its smoothness over that base. This gives the second claimed smoothness assertion as well. Empty equation or chart lists use determinant and denominator product \(1\); the same constructions cover zero algebras. ∎

### The desingularization lemma

<a id="smoothing-section-desingularization-lemma"></a>

[D.20](#smoothing-lemma-desingularize) combines a lifting witness with extra equations to enlarge the singular ideal in the target.

<a id="smoothing-lemma-desingularize"></a>

#### Lemma D.20: desingularize

Reading source: [Stacks, Tag 07CR](https://stacks.math.columbia.edu/tag/07CR).

Let \(R\) be Noetherian, let \(\pi\in R\), and let \(\Lambda\) be an \(R\)-algebra with \(\operatorname{Ann}_\Lambda(\pi)=\operatorname{Ann}_\Lambda(\pi^2)\). Suppose \(A\) is finitely presented over \(R\), a map \(A\to\Lambda\) is given, the image of \(\pi\) is strictly standard in \(A/R\), and a section
\[
\rho:A/\pi^4A\longrightarrow R/\pi^4R
\]
agrees with the prescribed map to \(\Lambda/\pi^4\Lambda\). Then there is a factorization \(A\to B\to\Lambda\), with \(B/R\) finitely presented, such that
\[
\mathfrak aB\subset H_{B/R},\qquad
\mathfrak a=\operatorname{Ann}_R
\bigl(\operatorname{Ann}_R(\pi^2)/\operatorname{Ann}_R(\pi)\bigr).
\]
No annihilator equality in \(R\) is assumed.

**Proof.** Choose the strict witness from [D.3](#smoothing-definition-strictly-standard):
\[
A=R[x_1,\ldots,x_n]/(f_1,\ldots,f_m),\quad
0\le c\le\min(n,m),\quad I=(f_1,\ldots,f_m).
\]
It gives a sum-of-minors identity for \(\pi\) and the relations \(\pi f_\ell\in(f_1,\ldots,f_c)+I^2\) for \(\ell>c\). Subtract lifts in \(R\) of the finitely many values \(\rho(x_i)\) from the variables. This translation is a polynomial automorphism, preserves both witness identities, and makes \(\rho(x_i)=0\). Hence \(f_j(0)\in\pi^4R\), and the actual image of \(x_i\) in \(\Lambda\) has the form \(\pi^4\lambda_i\).

Write the linear terms of \(f_j\) as \(\sum_i r_{ji}x_i\), and let \(M=(r_{ji})_{j\le c,i\le n}\). Evaluate the sum-of-minors identity at \(\rho\). There are coefficients \(d_U\in R\) and \(u\in1+\pi^3R\) such that
\[
u\pi=\sum_{|U|=c}d_U\det(M_U).
\]
Apply [F.70](#algebra-lemma-matrix-left-inverse) to \(M^{\mathsf t}\) and transpose its resulting identity. This supplies an \(n\times c\) matrix \(S=(s_{ij})\) with \(MS=u\pi1_c\).

Introduce \(v_1,\ldots,v_c,w_1,\ldots,w_n\), set \(L_i=\sum_j s_{ij}v_j+\pi w_i\), and substitute \(x_i=\pi^2L_i\). For \(j\le c\), constant terms are divisible by \(\pi^4\), linear terms become
\[
\pi^2\sum_i r_{ji}L_i
=\pi^3u v_j+\pi^3\sum_i r_{ji}w_i,
\]
and every monomial of degree \(d\ge2\) becomes divisible by \(\pi^{2d}\). Dividing these specified powers in the coefficient expressions, rather than cancelling a ring element, constructs a polynomial \(G_j\) and an exact identity
\[
f_j(\pi^2L)=\pi^3g_j,\qquad
g_j=u v_j+\sum_i r_{ji}w_i+\pi G_j.
\tag{D.20a}
\]
For example, a constant term \(\pi^4a_j\) contributes \(a_j\) to \(G_j\), and a degree-\(d\) term with coefficient \(b_\alpha\) contributes \(b_\alpha\pi^{2d-4}L^\alpha\). Thus this construction is valid even when \(\pi\) is a zero divisor.

Let \(h_i=x_i-\pi^2L_i\), and define
\[
B=R[x,v,w]/(h_i,\ g_j:j\le c,\ f_\ell:1\le\ell\le m).
\]
Eliminating \(x_i\) using the \(h_i\) is an actual inverse substitution isomorphism. The two required maps send the old \(x_i\) to their classes in \(B\), and send
\[
x_i\longmapsto\pi^4\lambda_i,\qquad
v_j\longmapsto0,\qquad w_i\longmapsto\pi\lambda_i
\]
in \(\Lambda\). The \(h_i\) and \(f_\ell\) vanish there. Each \(g_j\) has image \(t\in\pi\Lambda\) by (D.20a) modulo \(\pi\), and satisfies \(\pi^3t=0\). The annihilator equality implies \(\operatorname{Ann}_\Lambda(\pi^e)=\operatorname{Ann}_\Lambda(\pi)\) for every \(e\ge1\): if \(\pi^e b=0\) for \(e\ge2\), apply the equality to \(\pi^{e-2}b\) and reduce the exponent successively. Writing \(t=\pi b\) now gives \(\pi^4b=0\), hence \(t=0\). All relations therefore vanish, and the factorization is exact.

After inverting \(\pi\), the \(h_i\) uniquely eliminate \(w_i\), and (D.20a) makes the \(g_j\) consequences of the \(f_j\). Consequently
\[
B_\pi\cong A_\pi[v_1,\ldots,v_c].
\]
[D.5](#smoothing-lemma-elkik) makes \(A_\pi\) smooth over \(R\); a polynomial extension is smooth by [F.85](#algebra-lemma-standard-smooth), and [F.29](#algebra-lemma-compose-smooth) proves smoothness of \(B_\pi/R\).

For primes containing \(\pi\), first use the algebra
\[
B'=R[v,w]/(g_1,\ldots,g_c).
\]
The Jacobian on the pivot variables \(v_j\) is \(u1_c+\pi(\partial G_j/\partial v_k)\), so its determinant \(\Delta\) is \(1\) modulo \(\pi\). Thus \(B'_\Delta\) is standard smooth by the inverse-variable Jacobian calculation in F.85. It is flat over the Noetherian base \(R\) by [F.83](#algebra-lemma-smooth-syntomic). Notice also the explicit reduction \(B'/\pi B'\cong(R/\pi R)[w]\), obtained by eliminating \(v_j=-\sum_i r_{ji}w_i\).

The natural surjection \(B'\to B\) has kernel generated by
\[
F_\ell=f_\ell(\pi^2L)\quad(\ell>c);
\]
the first \(c\) equations have already vanished by (D.20a). Let \(\mathfrak q\subset B\) contain \(\pi\) and avoid some \(r\in\mathfrak a\), and let \(\mathfrak q'\) be its inverse image in \(B'\). Then \(\Delta\notin\mathfrak q'\), and \(T=B'_{\mathfrak q'}\) is flat over \(R\), since it is a localization of that flat chart. Every \(F_\ell\) belongs to \(\pi^2T\): its substituted variables have this divisibility and its constant term belongs to \(\pi^4R\).

Substitute in the strict relation condition and use the first \(c\) equations already killed in \(B'\). It gives
\[
\pi F_\ell=\sum_{a,b>c}b_{\ell ab}F_aF_b.
\]
For the finite \(T\)-module \(N=(\pi F_\ell:\ell>c)\), divisibility of \(F_a\) by \(\pi^2\) gives \(N\subset\pi N\); the reverse inclusion holds for every ideal. Since \(\pi\) lies in the maximal ideal of \(T\), [F.10](#algebra-lemma-NAK) gives \(N=0\). Thus \(\pi F_\ell=0\).

Flatness identifies each multiplication kernel and preserves their quotient sequence, giving the canonical isomorphism
\[
\bigl(\operatorname{Ann}_R(\pi^2)/\operatorname{Ann}_R(\pi)\bigr)
\otimes_RT
\cong
\operatorname{Ann}_T(\pi^2)/\operatorname{Ann}_T(\pi).
\]
For the kernel identification, tensor the short exact sequence through the image of multiplication by \(\pi^e\), and its injection into \(R\), for \(e=1,2\). Tensor their annihilator inclusion and quotient sequence next. The element \(r\) kills the left-hand module and is a unit in \(T\), so the quotient on the right is zero. Write \(F_\ell=\pi b_\ell\). From \(\pi F_\ell=0\) and the resulting annihilator equality in \(T\), we obtain \(F_\ell=0\).

To obtain a smooth neighbourhood rather than only an isomorphism of local rings, choose for each of the finitely many \(F_\ell\) an element of \(B'\setminus\mathfrak q'\) killing it; these exist by the localization equality criterion. Their product \(s\) kills the whole kernel. Hence \(B'_{\Delta s}\to B_{\Delta s}\) is an isomorphism, and \(\Delta s\) avoids \(\mathfrak q\). This is a localization of a standard smooth algebra, so F.85 and [F.7](#algebra-definition-smooth-at-prime) prove smoothness of \(R\to B\) at \(\mathfrak q\).

Every prime avoiding \(\pi\) is smooth by the earlier description of \(B_\pi\). Every other prime avoiding \(\mathfrak aB\) has some such \(r\) and is smooth by the chart just constructed. Thus every nonsmooth prime contains \(\mathfrak aB\). The radical/prime intersection formula proved in [D.1](#smoothing-definition-singular-ideal), applied to \(H_{B/R}\), gives \(\mathfrak aB\subset H_{B/R}\). Empty lists use determinant and product \(1\), so the argument includes \(c=0\), \(c=m\), and zero rings. ∎

<a id="smoothing-lemma-desingularize-strictly-standard"></a>

#### Lemma D.21: desingularize strictly standard

Reading source: [Stacks, Tag 07CT](https://stacks.math.columbia.edu/tag/07CT).

Let \(R\) be Noetherian, let \(\pi\in R\), and let \(A\to\Lambda\), \(D\to\Lambda\) be \(R\)-algebra maps, with \(A/R\) and \(D/R\) finitely presented. Assume
\[
\operatorname{Ann}_R(\pi)=\operatorname{Ann}_R(\pi^2),\qquad
\operatorname{Ann}_\Lambda(\pi)=\operatorname{Ann}_\Lambda(\pi^2),
\]
that \(\pi\) is strictly standard in \(A/R\), and that a map \(A/\pi^4A\to D/\pi^4D\) agrees with both prescribed maps to \(\Lambda/\pi^4\Lambda\). There are compatible maps \(A\to B\), \(D\to B\), \(B\to\Lambda\), with \(B/R\) finitely presented, such that
\[
H_{D/R}B\subset H_{B/D},
\qquad
H_{D/R}B\subset H_{B/R}.
\]

**Proof.** Let \(C=A\otimes_RD\), with map to \(\Lambda\) sending \(a\otimes d\) to the product of their prescribed images. A finite presentation \(A=R[x]/(f)\) gives \(C=D[x]/(f)\), so \(C/D\) is finitely presented. The strict witness changes coefficients to \(D\) by [D.7](#smoothing-lemma-strictly-standard-base-change). The given map \(\phi:A/\pi^4A\to D/\pi^4D\) gives the section
\[
C/\pi^4C\longrightarrow D/\pi^4D,\qquad
a\otimes d\longmapsto\phi(\bar a)\bar d.
\]
The tensor relations make this well-defined; on the \(D/\pi^4D\) factor it is the identity. Its composition to \(\Lambda/\pi^4\Lambda\) is the original product map by the assumed compatibility.

The ring \(D\) is Noetherian by [S01, Lemma 1.3](AG-RG-S01.md). Apply [D.20](#smoothing-lemma-desingularize) with base \(D\) and algebra \(C\). Its hypotheses require the annihilator equality in \(\Lambda\), already assumed, and require no such equality in \(D\). We obtain \(C\to B\to\Lambda\), with \(B/D\) finitely presented, and
\[
\mathfrak aB\subset H_{B/D},\qquad
M=\operatorname{Ann}_D(\pi^2)/\operatorname{Ann}_D(\pi),\quad
\mathfrak a=\operatorname{Ann}_D(M).
\]
The two tensor-factor maps give \(A\to B\) and \(D\to B\), with the desired exact composites to \(\Lambda\). If \(D=R[u]/(g)\) and \(B=D[v]/(h)\), choose polynomial lifts \(\widetilde h\) in \(R[u,v]\). Substitution in both directions gives \(B=R[u,v]/(g,\widetilde h)\), proving finite presentation over \(R\).

Fix a prime \(\mathfrak q\subset D\) where \(R\to D\) is smooth. A smooth principal neighbourhood is flat over the Noetherian ring \(R\) by [F.83](#algebra-lemma-smooth-syntomic); exact localization [S01, Lemma 1.1](AG-RG-S01.md) makes \(D_{\mathfrak q}\) flat as well. Tensor the multiplication-kernel sequences for \(\pi,\pi^2\) as in D.20. The equality of the original annihilators over \(R\) gives
\[
\operatorname{Ann}_{D_{\mathfrak q}}(\pi)
=\operatorname{Ann}_{D_{\mathfrak q}}(\pi^2),\qquad M_{\mathfrak q}=0.
\]
The module \(M\) is finite: its two annihilator ideals are finite over the Noetherian ring \(D\), and \(M\) is their quotient. Choose generators \(m_i\). For each, vanishing at \(\mathfrak q\) gives \(s_i\notin\mathfrak q\) with \(s_im_i=0\). Their product \(s\) kills every generator; hence \(s\in\mathfrak a\setminus\mathfrak q\). For \(M=0\), use \(s=1\).

At a prime \(\mathfrak r\subset B\) above \(\mathfrak q\), this element remains outside \(\mathfrak r\). Since \(s\in\mathfrak aB\subset H_{B/D}\), [D.1](#smoothing-definition-singular-ideal) shows that \(D\to B\) is smooth at \(\mathfrak r\). To verify smooth composition at the level of actual neighbourhoods, choose \(t\in D\setminus\mathfrak q\) with \(D_t/R\) smooth. Inside a smooth \(D\)-neighbourhood of \(\mathfrak r\), F.83 supplies a principal neighbourhood \(B_g\) that is standard smooth over \(D\). The denominator conversion in its proof makes \(g\) an element of \(B\setminus\mathfrak r\). Base change to \(D_t\) preserves the standard smooth presentation and its unit determinant by [F.85(5)](#algebra-lemma-standard-smooth), so \(B_{tg}/D_t\) is smooth. [F.29](#algebra-lemma-compose-smooth) now makes \(B_{tg}/R\) smooth. Thus \(R\to B\) is smooth at every such \(\mathfrak r\).

An element of \(H_{D/R}\) avoided by a prime of \(B\) is avoided by its contraction in \(D\), so that contraction is smooth. We have just proved that the prime of \(B\) is smooth for both \(B/D\) and \(B/R\). Consequently every nonsmooth prime for either map contains \(H_{D/R}B\). Intersecting these primes and using the radical/prime formula in D.1 proves both claimed ideal inclusions. Empty singular loci and zero algebras use the same convention that the intersection of no primes is the unit ideal. ∎

<a id="smoothing-lemma-desingularize-lifting-apply"></a>

#### Lemma D.22: desingularize lifting apply

Reading source: [Stacks, Tag 07F0](https://stacks.math.columbia.edu/tag/07F0).

Let \(R\) be Noetherian, let \(\pi\in R\), and let \(A\to\Lambda\) be an \(R\)-algebra map with \(A/R\) finitely presented. Assume
\[
\operatorname{Ann}_R(\pi)=\operatorname{Ann}_R(\pi^2),\qquad
\operatorname{Ann}_\Lambda(\pi)=\operatorname{Ann}_\Lambda(\pi^2),
\]
and that \(\pi\) is strictly standard in \(A/R\). Given a factorization
\[
A/\pi^8A\longrightarrow\bar C\longrightarrow\Lambda/\pi^8\Lambda
\]
with \(\bar C\) finitely presented over \(R/\pi^8R\), there is a factorization \(A\to B\to\Lambda\), with \(B/R\) finitely presented, such that \(B_\pi/R_\pi\) is smooth and
\[
H_{\bar C/(R/\pi^8R)}(\Lambda/\pi^8\Lambda)
\subset \bigl(\sqrt{H_{B/R}\Lambda}+\pi^8\Lambda\bigr)/\pi^8\Lambda.
\]

**Proof.** If multiplication by \(u\) on a module has \(\ker u=\ker u^2\), its kernels for all positive powers agree. Indeed \(u^{r+1}v=0\) puts \(u^{r-1}v\) in \(\ker u^2=\ker u\), hence \(u^rv=0\); repeating lowers the exponent to one. Thus the annihilators of \(\pi^4\) and \(\pi^8\) agree in both \(R\) and \(\Lambda\).

Use [D.19](#smoothing-lemma-lifting) with parameter \(\pi^4\) and algebra \(\bar C\). It constructs \(D/R\) finitely presented, a map \(D\to\Lambda\), and commuting maps
\[
\bar C/\pi^4\bar C\longrightarrow D/\pi^4D
\longrightarrow\Lambda/\pi^4\Lambda.
\]
It proves smoothness of \(D/R\) away from \(\pi\), and also at a prime over \(\pi\) if its contraction to \(\bar C\) is smooth over \(R/\pi^8R\). Compose the reduced map from \(A\) with this diagram. The resulting \(A/\pi^4A\to D/\pi^4D\) agrees with the prescribed maps to \(\Lambda/\pi^4\Lambda\). Therefore [D.21](#smoothing-lemma-desingularize-strictly-standard) constructs compatible maps \(A\to B\), \(D\to B\), \(B\to\Lambda\), with \(B/R\) finitely presented and
\[
H_{D/R}B\subset H_{B/R}.
\tag{D.22a}
\]
If a prime \(\mathfrak b\subset B\) avoids \(\pi\), its contraction to \(D\) is smooth and hence avoids \(H_{D/R}\). Inclusion (D.22a) makes \(\mathfrak b\) avoid \(H_{B/R}\) as well, so \(B/R\) is smooth at that prime by [D.1](#smoothing-definition-singular-ideal). Its smooth principal neighbourhood can be localized further at \(\pi\) by [F.67](#algebra-lemma-locally-smooth). Viewed over \(R_\pi\), it is smooth: a polynomial presentation over \(R\) in which \(\pi\) is invertible localizes to the same presentation over \(R_\pi\). Exact localization [S01, Lemma 1.1](AG-RG-S01.md) identifies its kernel ideal and conormal quotient with their localizations. Since \(\pi\) is already invertible on the presented algebra, its two conormal terms and their differential are unchanged. Definition [F.6](#algebra-definition-smooth) and comparison [F.11](#algebra-lemma-NL-homotopy) give the assertion. Every prime of \(B_\pi\) has such a neighbourhood, and F.67 gives global smoothness over \(R_\pi\).

Set \(J=H_{B/R}\Lambda\). For each prime \(\mathfrak l\subset\Lambda\) containing \(J\), let \(\mathfrak b,\mathfrak d\) be its contractions to \(B,D\). They contain \(H_{B/R},H_{D/R}\), respectively, so both contracted points are nonsmooth. The preceding conclusion forces \(\pi\in\mathfrak l\). The prime \(\mathfrak d/\pi^4D\) now contracts along the quotient diagram to a prime \(\mathfrak c\) of \(\bar C\). If this were smooth, D.19 would make \(\mathfrak d\) smooth, a contradiction. Consequently \(H_{\bar C/(R/\pi^8R)}\subset\mathfrak c\).

The contraction \(\mathfrak c\) is also the inverse image of \(\mathfrak l/\pi^8\Lambda\) under \(\bar C\to\Lambda/\pi^8\Lambda\). To check this equality, reduce that map modulo \(\pi^4\) and use the commuting diagram through \(D/\pi^4D\); both quotient primes are the contractions of the same \(\mathfrak l\), which contains \(\pi\). Thus the ideal generated by the images of \(H_{\bar C/(R/\pi^8R)}\) lies in every such \(\mathfrak l/\pi^8\Lambda\).

For an explicit radical argument, let \(K\subset\Lambda\) be the inverse image of that generated ideal. The preceding paragraph and \(\pi\in\mathfrak l\) give \(K\subset\mathfrak l\) for every prime containing \(J\). The prime-intersection proof in D.1 yields \(K\subset\sqrt J\), as well as \(\pi\in\sqrt J\). In particular \(\pi^8\Lambda\subset\sqrt J\); taking the image of \(K\subset\sqrt J\) in \(\Lambda/\pi^8\Lambda\) is precisely the claimed inclusion. If no prime contains \(J\), D.1 gives \(\sqrt J=\Lambda\), and the same argument holds. This proves the result for an arbitrary target \(\Lambda\), including zero quotients. ∎

### Warmup: reduction to a base field

<a id="smoothing-section-reduction"></a>

The preceding lifting constructions allow [D.26](#smoothing-lemma-reduce-to-field) to reduce the smooth-colimit theorem to a field base. We fix the global assumptions before proving that reduction.

<a id="smoothing-situation-global"></a>

#### Situation D.23: global

Reading source: [AI Integrated Stacks, pinned smoothing, lines 1915–1918](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/smoothing.tex#L1915-L1918).

Throughout the reduction to a field, $R$ and $\Lambda$ are Noetherian and the map $R\to\Lambda$ is regular. For this fixed map, the abbreviation *PT holds* means that there is a filtered system of smooth $R$-algebras with colimit $\Lambda$ as an $R$-algebra.

<a id="smoothing-lemma-product"></a>

#### Lemma D.24: product

Reading source: [Stacks, Tag 07F3](https://stacks.math.columbia.edu/tag/07F3).

For \(i=1,2\), let \(R_i\to\Lambda_i\) be a regular map of Noetherian rings as in [D.23](#smoothing-situation-global). If each \(\Lambda_i\) is a filtered colimit of smooth \(R_i\)-algebras, then \(\Lambda_1\times\Lambda_2\) is a filtered colimit of smooth \(R_1\times R_2\)-algebras.

**Proof.** Put \(R=R_1\times R_2\), with orthogonal idempotents \(e_1=(1,0)\), \(e_2=(0,1)\). For any \(R\)-module \(M\), the maps
\[
M\longrightarrow e_1M\times e_2M,\quad m\longmapsto(e_1m,e_2m),
\qquad (m_1,m_2)\longmapsto m_1+m_2
\]
are inverse, since \(e_1+e_2=1\) and \(e_1e_2=0\). Tensor products split by the same rule:
\[
M\otimes_R(\Lambda_1\times\Lambda_2)
\cong(e_1M\otimes_{R_1}\Lambda_1)\times
      (e_2M\otimes_{R_2}\Lambda_2).
\]
The maps send a pure tensor to its two component tensors; summing the inclusions gives the inverse, and cross tensors vanish because the idempotent can be moved to either factor. This verifies the formula by [S01, Lemma 1.0](AG-RG-S01.md). Exact sequences split into their two component sequences, so component flatness proves flatness of the product map.

Every ideal in a finite product splits in this fashion into two ideals. Finite generator lists for those component ideals give a finite generator list for the original ideal. Hence \(R\) and \(\Lambda_1\times\Lambda_2\) are Noetherian. A prime contains exactly one of \(e_1,e_2\): it contains at least one since their product is zero, and cannot contain both since their sum is one. It therefore comes from exactly one component, with that component's residue field. Tensoring with this residue field kills the other component and identifies the fibre with the corresponding fibre of \(R_i\to\Lambda_i\). Geometric regularity of these fibres proves regularity of the product map, so it is again in Situation D.23.

We prove smoothness of each product algebra used below. Let \(C_i/R_i\) be smooth and let \(C=C_1\times C_2\). Then \(C_{e_i}=C_i\), with inverse maps given by projection and inclusion of the selected component; the other component vanishes when \(e_i\) is made invertible. Also \(R_{e_i}=R_i\). Indeed inverting an idempotent forces it to equal one, so this localization is the quotient \(R/(1-e_i)\). The inverse-variable presentation \(R[T]/(e_iT-1)\), whose derivative \(e_i\) is a unit, proves \(R_i/R\) smooth by [F.85](#algebra-lemma-standard-smooth). Thus [F.29](#algebra-lemma-compose-smooth) makes \(C_i/R\) smooth. The two elements \(e_i\) generate one in \(C\), so [F.35](#algebra-lemma-cover-upstairs) gives finite presentation of \(C/R\) from that of the \(C_{e_i}/R\). At every prime one \(e_i\) is avoided; the corresponding localization is smooth over \(R\). The full gluing result [F.67](#algebra-lemma-locally-smooth) therefore proves \(C/R\) smooth.

Choose the assumed presentations
\[
\Lambda_i=\operatorname*{colim}_{a\in I_i}C_{i,a}.
\]
The category \(I_1\times I_2\) is filtered: it is nonempty, successors of two objects are chosen in each coordinate, and parallel arrows are equalized in each coordinate. The preceding argument makes every \(C_{1,a}\times C_{2,b}\) smooth over \(R\). Component maps induce
\[
\operatorname*{colim}_{(a,b)\in I_1\times I_2}
(C_{1,a}\times C_{2,b})\longrightarrow\Lambda_1\times\Lambda_2.
\]
Any pair on the right has representatives at a pair of stages, proving surjectivity. If a represented pair maps to zero, each component becomes zero at a later stage by the filtered equality criterion. The pair of these stages kills the represented pair, proving injectivity. The same criterion applied to differences proves equality detection, and the maps preserve sums, products and units componentwise. The displayed map is consequently an \(R\)-algebra isomorphism. Iterating gives the same conclusion for any finite nonempty product; zero components obey these identical idempotent calculations. ∎

<a id="smoothing-lemma-delocalize-base"></a>

#### Lemma D.25: delocalize base

Reading source: [Stacks, Tag 07F4](https://stacks.math.columbia.edu/tag/07F4).

Let \(R\to A\to\Lambda\) be ring maps with \(A/R\) finitely presented, and let \(S\subset R\) be multiplicative. Suppose \(S^{-1}A\to B'\to S^{-1}\Lambda\) is a factorization with \(B'/S^{-1}R\) smooth. Then the original map factors as \(A\to B\to\Lambda\), with \(B/R\) finitely presented and the image of some \(s\in S\) elementary standard in \(B/R\) in the sense of [D.3](#smoothing-definition-strictly-standard).

**Proof.** If \(0\in S\), take \(B=A\) and \(s=0\). In its finite presentation choose \(c=0\): the empty minor is one with coefficient zero, and multiplying every extra equation by zero gives zero. This verifies both elementary standard conditions. Hence assume \(0\notin S\).

The retraction [D.12](#smoothing-lemma-smooth-standard-smooth) replaces \(B'\) by a standard smooth algebra: compose the original map into its retract inclusion, and compose its retraction with the original target map. These composites preserve the original factorization. Write \(A=R[x_1,\ldots,x_n]/(g_1,\ldots,g_t)\), with coordinate images \(\lambda_i\in\Lambda\). The graph-equation construction [D.14](#smoothing-lemma-standard-smooth-include-generators), applied to this ordered list of images, gives
\[
B'=S^{-1}R[x_1,\ldots,x_{n+m}]/(f_1,\ldots,f_c),
\qquad n\le c\le n+m,
\]
with the first \(n\) variables representing the given images and with the minor on its first \(c\) variables invertible. Repeated images are permitted: each graph equation has its own variable and the same identity Jacobian block.

For \(i>n\), write the image of the old coordinate \(x_i\) in \(S^{-1}\Lambda\) as \(\lambda_i/d_i\), with \(d_i\in S\). Introduce the new coordinate \(y_i=d_ix_i\), leaving \(y_i=x_i\) for \(i\le n\). Express each old equation in the new coordinates by substituting \(x_i=d_i^{-1}y_i\). The reverse substitution is \(y_i=d_ix_i\), so these changes give inverse polynomial-algebra maps over \(S^{-1}R\). The new coordinates map to \(\lambda_i/1\). Differentiating the substituted equations multiplies the column for an added selected variable by \(d_i^{-1}\); the determinant remains a unit. Clear the finite coefficient denominators in each equation by multiplying it by \(u_j\in S\). This does not change the localized relation ideal and multiplies the determinant by the unit \(\prod_j u_j\). Rename the new coordinates \(x_i\) and the scaled equations \(f_j\). Now
\[
P=R[x_1,\ldots,x_{n+m}],\qquad f_j\in P,\qquad
\Delta=\det(\partial f_j/\partial x_i)_{1\le j,i\le c}
\]
has invertible image in \(B'\).

A polynomial representative of its inverse gives \(b_0,\ldots,b_c\in S^{-1}P\) with \(1=b_0\Delta+\sum_j b_jf_j\). Choose \(d\in S\) and \(c_j\in P\) representing all \(db_j\). The polynomial \(d-c_0\Delta-\sum_jc_jf_j\) is zero after localization; some \(e\in S\) therefore annihilates it in \(P\). With \(s_0=ed\) and \(a_j=ec_j\), we have the exact identity
\[
s_0=a_0\Delta+\sum_{j=1}^c a_jf_j\quad\text{in }P.
\tag{D.25a}
\]
The annihilating multiplier is required even when \(P\) has \(S\)-torsion; no element of \(S\) has been cancelled in \(P\).

Each original relation \(g_k\) is zero in \(S^{-1}(P/(f_1,\ldots,f_c))\), so choose \(s_k\in S\) and \(v_{kj}\in P\) with \(s_kg_k=\sum_jv_{kj}f_j\). Each \(f_j(\lambda)\) is zero in \(S^{-1}\Lambda\), so choose \(t_j\in S\) with \(t_jf_j(\lambda)=0\) in \(\Lambda\). Set
\[
h_j=t_jf_j,\quad
B=P/(h_1,\ldots,h_c,g_1,\ldots,g_t),\quad
s=s_0\prod_{k=1}^t s_k\prod_{j=1}^c t_j.
\]
These finite relations give finite presentation. The original coordinates define \(A\to B\); evaluation of all coordinates at \(\lambda_i\) defines \(B\to\Lambda\), since it kills both relation lists. Their composite is the given map.

Here is the full witness for elementary standardness. For each \(k\), multiply its relation identity by \(s_0\prod_{\ell\ne k}s_\ell\prod_jt_j\). Replacing \(t_jf_j\) by \(h_j\) gives
\[
sg_k=\sum_{j=1}^c
s_0\Bigl(\prod_{\ell\ne k}s_\ell\Bigr)
\Bigl(\prod_{q\ne j}t_q\Bigr)v_{kj}h_j
\quad\text{in }P.
\]
Thus \(sg_k\in(h_1,\ldots,h_c)\), which implies D.3's extra-relation condition even without its allowed \(I^2\) term. Multiplication of (D.25a) by \(\prod_jt_j\) gives
\[
s_0\prod_jt_j
=a_0\det(\partial h_j/\partial x_i)_{1\le j,i\le c}
+\sum_{j=1}^c a_j\Bigl(\prod_{q\ne j}t_q\Bigr)h_j.
\]
The determinant equality follows by factoring \(t_j\), a base scalar, from equation row \(j\). In \(B\), the second sum is zero. Multiplying by \(\prod_ks_k\) expresses the image of \(s\) as this selected minor times the image of \(a_0\prod_ks_k\), exactly D.3's other condition. Every product with an empty index set is one. This proves the assertion also for empty equation lists and zero target algebras. ∎

<a id="smoothing-lemma-reduce-to-field"></a>

#### Lemma D.26: reduce to field

Reading source: [Stacks, Tag 07F5](https://stacks.math.columbia.edu/tag/07F5).

If PT holds for every regular map \(K\to\Lambda\) of Noetherian rings with \(K\) a field, then PT holds for every regular map \(R\to\Lambda\) of Noetherian rings, as in [D.23](#smoothing-situation-global).

**Proof.** Suppose a map fails PT. Each quotient \(R/I\to\Lambda/I\Lambda\) is regular by [F.123](#more-algebra-lemma-regular-base-change); its rings are Noetherian because ideals in a quotient lift to ideals in the original ring. The set of failing quotient ideals is nonempty and has a maximal member by the ascending-chain condition. Replace the map by that quotient. Hence every further nonzero ideal gives PT. The new \(R\) is nonzero: a unital map from the zero ring has zero target, which is already a smooth algebra over itself and a constant filtered colimit.

The nilradical \(N\) is finitely generated because \(R\) is Noetherian. If its generators satisfy \(a_i^{n_i}=0\), every monomial of degree \(1+\sum_i(n_i-1)\) contains some \(a_i^{n_i}\), so that power of \(N\) is zero. If \(N\ne0\), maximality gives PT after quotienting by \(N\), and flatness of the original regular map allows [D.18](#smoothing-proposition-lift) to lift PT back to \(R\). This is a contradiction. Thus \(R\) is reduced.

We supply the finite-prime decomposition needed for its total fraction ring. Every radical ideal of a Noetherian ring is a finite intersection of prime ideals. Otherwise take a maximal counterexample \(I\) by the ascending-chain condition. It is proper and not prime, so there are \(a,b\notin I\) with \(ab\in I\). Both \(\sqrt{I+(a)}\) and \(\sqrt{I+(b)}\) are strictly larger and hence finite intersections of primes (the unit ideal is the empty intersection). Their intersection is \(I\): if \(x\) lies in both, then \(x^m\in I+(a)\) and \(x^n\in I+(b)\) for some positive \(m,n\), whence \(x^{m+n}\in I+(ab)=I\); radicalness gives \(x\in I\). Combining the two finite lists contradicts the choice of \(I\).

Apply this to the radical zero ideal of the nonzero reduced ring, and remove repeated primes and any prime containing another in the list. We obtain
\[
0=\bigcap_{i=1}^r\mathfrak p_i
\]
with a nonempty, pairwise incomparable list. These are exactly the minimal primes. Indeed the product of the listed ideals is contained in their intersection, so any prime over zero contains at least one listed prime: otherwise choose an element from each \(\mathfrak p_i\) outside it, whose product contradicts primality. If a prime lies strictly inside \(\mathfrak p_i\), the same observation puts a listed \(\mathfrak p_j\) inside it, contradicting incomparability. This proves finiteness, minimality and the zero intersection directly.

For each \(i\), choose
\[
y_i\in\bigcap_{j\ne i}\mathfrak p_j\setminus\mathfrak p_i
\]
by multiplying one element of \(\mathfrak p_j\setminus\mathfrak p_i\) for each \(j\ne i\); for \(r=1\) take \(y_1=1\). An element outside all \(\mathfrak p_i\) is a nonzerodivisor: test an annihilated product in the domains \(R/\mathfrak p_i\), then use their zero intersection. Conversely \(a\in\mathfrak p_i\) satisfies \(ay_i=0\), while \(y_i\ne0\), and is a zerodivisor. Hence the multiplicative set of nonzerodivisors is \(S=R\setminus\bigcup_i\mathfrak p_i\).

Let \(d=\sum_i y_i\in S\), \(Q=S^{-1}R\), and \(e_i=y_i/d\). Fractions define an injection
\[
Q\longrightarrow\prod_i\operatorname{Frac}(R/\mathfrak p_i):
\]
the denominators are nonzero in every component, and a fraction in its kernel has numerator in their zero intersection. In component \(i\), \(e_i\) equals one; in all other components it equals zero. Therefore \(e_i^2=e_i\), \(e_ie_j=0\) for \(i\ne j\), and \(\sum_i e_i=1\). Projection by these idempotents and summation give inverse maps \(Q\cong\prod_i e_iQ\).

Each \(K_i=e_iQ\) is a field. A nonzero \(e_i a/s\) has \(a\notin\mathfrak p_i\). The element
\[
u=e_i a+(1-e_i)
 =\frac{y_i a+\sum_{j\ne i}y_j}{d}
\]
is a unit of \(Q\): its numerator avoids \(\mathfrak p_i\) because \(y_i a\) does, and avoids every other \(\mathfrak p_j\) because only \(y_j\) survives there. Its numerator is thus in \(S\), giving the fraction inverse. The inverse of \(e_i a/s\) inside \(e_iQ\) is \(e_i s u^{-1}\). This proves the claimed field decomposition with actual inverse ring maps.

The localization \(Q\to\Lambda_Q=S^{-1}\Lambda\) is a regular map of Noetherian rings. To verify Noetherianness of either localization, extend the contraction of an ideal: each fraction in the ideal has its numerator in that contraction, and finite generators of the contraction generate the localized ideal. For a \(Q\)-module \(M\), the tensor maps of [S01, Lemma 1.0](AG-RG-S01.md) give
\[
M\otimes_Q\Lambda_Q\cong M\otimes_R\Lambda.
\]
Here elements of \(S\) are already invertible on \(M\), so the maps on pure tensors and their inverse respect the fraction relations. Exactness of the right side gives flatness. For a prime \(\mathfrak q\subset Q\), its contraction \(\mathfrak p\subset R\) avoids \(S\), and \(\mathfrak q=S^{-1}\mathfrak p\): a fraction belongs to \(\mathfrak q\) exactly when its numerator does, because its denominator is a unit. Conversely a prime disjoint from \(S\) extends to a prime, since \(S^{-1}(R/\mathfrak p)\) is a domain. The quotient \(Q/\mathfrak q\) is this localized domain and its fraction field is \(\operatorname{Frac}(R/\mathfrak p)\), so its residue field equals \(\kappa(\mathfrak p)\). Tensor associativity from S01, Lemma 1.0 identifies its fibre with \(\Lambda\otimes_R\kappa(\mathfrak p)\), geometrically regular by hypothesis. The idempotents split \(\Lambda_Q=\prod_i e_i\Lambda_Q\). Each component \(K_i\to e_i\Lambda_Q\) is flat by the same component tensor calculation in [D.24](#smoothing-lemma-product), and has the corresponding regular fibre. Its rings are Noetherian, since it is a quotient of the respective localization. The assumed field case and the finite-product conclusion of D.24 give PT for \(Q\to\Lambda_Q\).

Take any finitely presented \(R\)-algebra \(A\to\Lambda\). Localizing its finite generator and relation lists gives a finitely presented \(Q\)-algebra. Criterion [F.90](#algebra-lemma-when-colimit) factors it through a smooth \(Q\)-algebra. By [D.25](#smoothing-lemma-delocalize-base) there is \(A\to A_1\to\Lambda\), with \(A_1/R\) finitely presented and \(\pi\in S\) elementary standard in \(A_1/R\). It is strictly standard by [D.3](#smoothing-definition-strictly-standard): put its elementary coefficient at the selected variable set and put all other minor coefficients equal to zero.

Since \(R\ne0\) and multiplication by \(\pi\) is injective, \(\pi^8\ne0\). Maximality of the failing quotient therefore gives PT for \(R/\pi^8R\to\Lambda/\pi^8\Lambda\), including when this quotient is zero. Apply F.90 to obtain
\[
A_1/\pi^8A_1\longrightarrow\bar C\longrightarrow\Lambda/\pi^8\Lambda
\]
with \(\bar C/(R/\pi^8R)\) smooth. All powers of \(\pi\) act injectively on \(R\), and flatness makes them injective on \(\Lambda\) by tensoring \(0\to R\xrightarrow{\pi^n}R\), using S01, Lemma 1.0. Thus both annihilator equalities hold for parameters \(\pi\) and \(\pi^4\).

Apply [D.19](#smoothing-lemma-lifting) with parameter \(\pi^4\). It supplies \(D/R\) finitely presented, \(D\to\Lambda\), and the compatible map
\[
A_1/\pi^4A_1\longrightarrow\bar C/\pi^4\bar C
\longrightarrow D/\pi^4D\longrightarrow\Lambda/\pi^4\Lambda.
\]
Every prime of \(D\) avoiding \(\pi\) is smooth by that lemma. Every prime containing \(\pi\) contracts to a smooth point of \(\bar C\), since the whole map \(\bar C/(R/\pi^8R)\) is smooth, and is therefore smooth as well. The actual neighbourhood criterion [F.67](#algebra-lemma-locally-smooth) makes \(D/R\) globally smooth.

Finally [D.21](#smoothing-lemma-desingularize-strictly-standard), applied to \(A_1,D,\pi\) and the displayed quotient map, constructs \(A_1\to B\to\Lambda\), with \(B/R\) finitely presented and \(H_{D/R}B\subset H_{B/R}\). Definition [D.1](#smoothing-definition-singular-ideal) gives \(H_{D/R}=D\), so \(H_{B/R}=B\). Thus every prime of \(B\) is smooth, and F.67 makes \(B/R\) smooth. Composing with \(A\to A_1\) gives the required smooth factorization of every finitely presented input. F.90 now gives PT for the supposedly failing map, a contradiction. Consequently no failing quotient exists and PT holds for the original map. ∎

### Local tricks

<a id="smoothing-section-local"></a>

<a id="smoothing-situation-local"></a>

#### Situation D.27: local

Reading source: [Stacks, Tag 07F7](https://stacks.math.columbia.edu/tag/07F7).

Fix a Noetherian ring \(R\), an \(R\)-algebra \(A\) of finite presentation, an \(R\)-algebra map \(A\to\Lambda\), and a prime \(\mathfrak q\) of \(\Lambda\). The target need not be Noetherian. For any intermediate \(R\)-algebra \(T\) with a specified map to \(\Lambda\), write
\[
\mathfrak h_T=\sqrt{H_{T/R}\Lambda},
\]
where \(H_{T/R}\) is the singular ideal of [D.1](#smoothing-definition-singular-ideal) and its extension is generated by its images in \(\Lambda\).

A *resolution at \(\mathfrak q\)* is a factorization \(A\to B\to\Lambda\) through an \(R\)-algebra \(B\) of finite presentation for which
\[
\mathfrak h_A\subset\mathfrak h_B,
\qquad \mathfrak h_B\not\subset\mathfrak q.
\]
We say that the specified local problem is *resolvable* when such a factorization exists. Both ideals in this condition belong to the same target ring \(\Lambda\); finite presentation of \(B\) is over the fixed base \(R\). The second condition means that some element of \(\mathfrak h_B\) lies outside \(\mathfrak q\), while the first requires preservation of the entire original singular radical.

<a id="smoothing-lemma-lift-solution"></a>

#### Lemma D.28: lift solution

Reading source: [Stacks, Tag 07F8](https://stacks.math.columbia.edu/tag/07F8).

Work in [D.27](#smoothing-situation-local). Let \(r\ge1\), and choose \(\pi_1,\ldots,\pi_r\in R\) whose images lie in \(\mathfrak q\). For each \(i\), suppose that \(\pi_i\) is strictly standard in \(A/R\), and that multiplication by \(\pi_i\) and by \(\pi_i^2\) has the same kernel on each of
\[
R/(\pi_1^8,\ldots,\pi_{i-1}^8)R,
\qquad
\Lambda/(\pi_1^8,\ldots,\pi_{i-1}^8)\Lambda.
\]
If the problem obtained by quotienting \(R,A,\Lambda\) by all \(\pi_i^8\), at the image of \(\mathfrak q\), is resolvable, then the original problem is resolvable.

**Proof.** First establish a base-change inclusion used in the single-element step. If \(R\to R'\) is any map and \(A'=A\otimes_R R'\), then
\[
H_{A/R}A'\subset H_{A'/R'}.
\tag{D.28a}
\]
Indeed, a prime of \(A'\) whose contraction is smooth has a standard smooth principal neighbourhood after taking a smooth neighbourhood of that contraction and applying [F.83](#algebra-lemma-smooth-syntomic). The coefficient base-change construction [F.85(5)](#algebra-lemma-standard-smooth) makes its inverse image standard smooth over \(R'\). Thus every nonsmooth prime of \(A'\) contracts to a nonsmooth prime of \(A\), and contains the images of \(H_{A/R}\). The prime-intersection verification in D.1 gives (D.28a), including an empty nonsmooth locus. No flatness was required.

Consider \(r=1\), and abbreviate \(\pi=\pi_1\). Put \(\bar R=R/\pi^8R\), \(\bar A=A/\pi^8A\), \(\bar\Lambda=\Lambda/\pi^8\Lambda\), and \(\bar{\mathfrak q}=\mathfrak q/\pi^8\Lambda\). The assumed resolution provides \(\bar A\to\bar C\to\bar\Lambda\), with \(\bar C/\bar R\) finitely presented, such that
\[
\sqrt{H_{\bar A/\bar R}\bar\Lambda}
\subset\sqrt{H_{\bar C/\bar R}\bar\Lambda}
\not\subset\bar{\mathfrak q}.
\tag{D.28b}
\]
The two kernel equalities and strict standardness are exactly the hypotheses of [D.22](#smoothing-lemma-desingularize-lifting-apply). Let \(A\to B\to\Lambda\) be its factorization, and set \(\mathfrak h_B=\sqrt{H_{B/R}\Lambda}\). The proof of D.22 shows that every prime containing \(H_{B/R}\Lambda\) contains \(\pi\); D.1 consequently gives \(\pi\in\mathfrak h_B\). Its other conclusion is
\[
H_{\bar C/\bar R}\bar\Lambda
\subset \mathfrak h_B/\pi^8\Lambda.
\tag{D.28c}
\]
The ideal on the right is radical. To check this directly, lift a class whose power belongs to it to \(x\in\Lambda\). Then \(x^a\in\mathfrak h_B+\pi^8\Lambda=\mathfrak h_B\), so \(x\in\mathfrak h_B\). Taking radicals in (D.28c) is therefore legitimate.

Write \(\rho:\Lambda\to\bar\Lambda\) for the quotient. Inclusion (D.28a) gives
\[
\rho(\mathfrak h_A)
\subset\sqrt{H_{\bar A/\bar R}\bar\Lambda}
\subset\mathfrak h_B/\pi^8\Lambda:
\]
an element of \(\mathfrak h_A\) has a power in \(H_{A/R}\Lambda\), whose image belongs to \(H_{\bar A/\bar R}\bar\Lambda\). Since \(\ker\rho=\pi^8\Lambda\subset\mathfrak h_B\), this proves \(\mathfrak h_A\subset\mathfrak h_B\). If \(\mathfrak h_B\subset\mathfrak q\), then (D.28c), after taking radicals, would put \(\sqrt{H_{\bar C/\bar R}\bar\Lambda}\) inside \(\bar{\mathfrak q}\), contradicting (D.28b). Thus \(\mathfrak h_B\not\subset\mathfrak q\). D.22 supplies the required finite presentation of \(B/R\), so this is a resolution with both radical conditions verified.

For \(r>1\), quotient first by \(\pi_1^8\). The base \(R'=R/\pi_1^8R\) is Noetherian: any ascending chain of its ideals lifts to one in \(R\). The finite polynomial presentation of \(A\) changes coefficients to give the finite presentation of \(A'=A/\pi_1^8A\) over \(R'\). The image \(\mathfrak q'\) is prime because \(\pi_1^8\Lambda\subset\mathfrak q\). For the remaining elements \(\pi_2,\ldots,\pi_r\), each successive quotient is precisely the original quotient by \(\pi_1^8,\ldots,\pi_{i-1}^8\); hence its two kernel hypotheses are unchanged. Strict standardness survives by [D.7](#smoothing-lemma-strictly-standard-base-change). The induction hypothesis gives a resolution of this first quotient problem. Apply the single-element step just proved to \(\pi_1\) to lift it to the original problem. This completes the induction, with no Noetherian assumption on \(\Lambda\). ∎

<a id="smoothing-lemma-delocalize-weak"></a>

#### Lemma D.29: delocalize weak

Reading source: [AI Integrated Stacks, pinned smoothing, lines 2147–2227](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/smoothing.tex#L2147-L2227).

Use the local setting [D.27](#smoothing-situation-local), and set $\mathfrak p=R\cap\mathfrak q$. Suppose $\mathfrak q$ is minimal over $\mathfrak h_A$ and the problem over $R_{\mathfrak p}$ with input $A_{\mathfrak p}$ and target $\Lambda_{\mathfrak q}$ is resolvable. Then the original map from $A$ factors through a finitely presented $R$-algebra $C$ whose singular ideal satisfies
$$H_{C/R}\Lambda\not\subset\mathfrak q.$$

**Proof.** We construct the required algebra by turning a localized smooth presentation into a finite system over $R$. A resolution over the local target has singular radical outside its maximal ideal. Its extended singular ideal must therefore be the unit ideal: a proper ideal in that local ring lies in the maximal ideal, and so does its radical. Apply [D.8](#smoothing-lemma-final-solve) to replace that intermediate algebra by a smooth one, then [D.12](#smoothing-lemma-smooth-standard-smooth) to obtain a standard smooth factorization of the prescribed map from $A_{\mathfrak p}$.

Write $A=R[x_1,\ldots,x_n]/(g_1,\ldots,g_t)$ and denote the target images of $x_i$ by $\lambda_i$. By [D.14](#smoothing-lemma-standard-smooth-include-generators), the smooth factorization has a presentation
$$D=R_{\mathfrak p}[x_1,\ldots,x_n,u_1,\ldots,u_m]/(f_1,\ldots,f_c),\qquad c\geq n,$$
containing that specific generator list, with a chosen Jacobian determinant invertible. D.14 uses a separate identity equation for each prescribed generator, so repeated images are allowed.

Multiplying each $f_j$ by a coefficient denominator outside $\mathfrak p$ puts every equation in $P=R[x,u]$. These multipliers are units over $R_{\mathfrak p}$, so the chosen determinant $\delta$ remains invertible there. Lift its inverse and the identity proving it is an inverse to polynomial expressions over $R_{\mathfrak p}$. Clear their finite denominator lists and annihilate the remaining localization error by an element outside $\mathfrak p$. This yields $s_0\notin\mathfrak p$ for which $\delta$ is invertible in $P_{s_0}/(f_j)$. Likewise, since each $g_i$ vanishes in $D$, there is $s_i\notin\mathfrak p$ such that $s_i g_i\in(f_j)$ in $P$. For
$$s=s_0\prod_{i=1}^t s_i,\qquad D_0=P_s/(f_j),$$
we have a standard smooth $R_s$-algebra receiving $A$, and $D_0/R$ is smooth by principal localization and smooth composition.

The target images of the finitely many $u_\ell$ can be written $\nu_\ell/h$ with one $h\in\Lambda\setminus\mathfrak q$. If there are no such variables, choose $h=1$. For integers $d_j$ large enough to remove negative powers, form
$$F_j(x,U,v)=v^{d_j}f_j(x,U/v)\in R[x,U,v].$$
Each value $F_j(\lambda,\nu,h)$ becomes zero in $\Lambda_{\mathfrak q}$. Choose a localization annihilator for each value and multiply them to obtain $\lambda_0\notin\mathfrak q$ with
$$\lambda_0 F_j(\lambda,\nu,h)=0\quad\text{in }\Lambda\quad\text{for every }j.$$
Define the finite presentation
$$C=R[w,x_1,\ldots,x_n,U_1,\ldots,U_m,v]/
\bigl(g_i(x),\,wF_j(x,U,v)\bigr).$$
The assignments $w\mapsto\lambda_0$, $x_i\mapsto\lambda_i$, $U_\ell\mapsto\nu_\ell$, $v\mapsto h$ respect all equations and give $A\to C\to\Lambda$.

Let $b=wvs$ in $C$. All three factors of its image avoid $\mathfrak q$, so its image does too. In $C_b$ substitute $u_\ell=U_\ell/v$. Inverting $w,v,s$ changes each equation $wF_j=0$ into $f_j=0$; the $g_i$ are already consequences of these equations over $R_s$. The inverse substitution $U_\ell=vu_\ell$ proves, on generators and relations, the exact isomorphism
$$C_b\cong D_0[w,w^{-1},v,v^{-1}].$$
The right side is smooth over $R$ by polynomial extension, localization and [F.29](#algebra-lemma-compose-smooth). Thus $b\in H_{C/R}$ by [D.1](#smoothing-definition-singular-ideal) and [F.67](#algebra-lemma-locally-smooth). Its image outside $\mathfrak q$ proves the claimed noncontainment. Every annihilator used belongs to a finite list; the argument requires no Noetherian property of $\Lambda$. ∎

<a id="smoothing-lemma-delocalize-height-zero"></a>

#### Lemma D.30: delocalize height zero

Reading source: [AI Integrated Stacks, pinned smoothing, lines 2229–2274](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/smoothing.tex#L2229-L2274).

In the setting [D.27](#smoothing-situation-local), put $\mathfrak p=R\cap\mathfrak q$. Assume $\mathfrak q$ is minimal over $\mathfrak h_A$, that the localized problem $R_{\mathfrak p}\to A_{\mathfrak p}\to\Lambda_{\mathfrak q}$ is resolvable, and that $\dim\Lambda_{\mathfrak q}=0$. Then a resolution exists over the original base $R$ and target $\Lambda$.

**Proof.** We need an algebra that improves the singular ideal at $\mathfrak q$ while retaining the original singular radical. The Noetherian ring here is $R$. Its finite-type algebra $A$ is Noetherian by AG-CA-03, Theorem 2.1, so write $H_{A/R}=(a_1,\ldots,a_r)$.

A zero-dimensional local ring has just one prime, its maximal ideal: another prime would give a strict chain of length one. The radical/prime identity proved in [D.1](#smoothing-definition-singular-ideal) therefore identifies the nilradical of $\Lambda_{\mathfrak q}$ with $\mathfrak q\Lambda_{\mathfrak q}$. Since each $a_i$ maps into this prime, it has nilpotent image in the localization. Choose one positive exponent $N$ annihilating their finite list there. Clearing the localization zeros gives $\lambda\in\Lambda\setminus\mathfrak q$ such that
$$\lambda a_i^N=0\quad(1\leq i\leq r)$$
in $\Lambda$. If the list is empty, take $N=1,\lambda=1$. This step uses nilpotence of individual elements, without asserting that the whole maximal ideal is nilpotent or that the local target is Artinian.

By [D.29](#smoothing-lemma-delocalize-weak) there is a finite-presentation factorization $A\to C\to\Lambda$ with $\mathfrak h_C\not\subset\mathfrak q$. Choose $c\in H_{C/R}$ with image outside $\mathfrak q$; otherwise that ideal and its radical would be contained in the prime. We can present $C$ as
$$C=A[x_1,\ldots,x_n]/(f_1,\ldots,f_m).$$
Indeed a finite $R$-generating list also generates over $A$, and the resulting polynomial ring over Noetherian $A$ has a finitely generated kernel.

Introduce $r$ variables $y_i$, one variable $z$, and $rm$ variables $t_{ij}$. Set
$$B=A[x_1,\ldots,x_n,y_1,\ldots,y_r,z,t_{ij}]/
\left(f_j-\sum_{i=1}^r y_it_{ij},\,zy_i\right).$$
Send $x_i$ to its given image, $y_i$ to $a_i^N$, $z$ to $\lambda$, and every $t_{ij}$ to zero. The equations vanish by the chosen annihilators and the map on $C$, so this defines $A\to B\to\Lambda$. The finite lists make $B$ finitely presented over $R$.

There are two kinds of smooth principal neighbourhoods. On the first, invert $z$; the equations force every $y_i=0$, giving
$$B_z=C[z,z^{-1},t_{ij}].$$
Since $c$ lies in the singular ideal, $C_c/R$ is smooth by [F.67](#algebra-lemma-locally-smooth). Polynomial extension and localization then make $B_{zc}/R$ smooth. For the second kind, invert $y_\ell$. We must have $z=0$, and each equation eliminates exactly one variable:
$$t_{\ell j}=y_\ell^{-1}\left(f_j-\sum_{i\ne\ell}y_it_{ij}\right).$$
The assignments in this formula and their inverse inclusions identify
$$B_{y_\ell}=A[x_j,y_i,y_\ell^{-1},t_{ij}\ (i\ne\ell)].$$
After also inverting $a_\ell$, this is smooth over $R$ because $A_{a_\ell}/R$ is smooth. Consequently $zc$ and every $a_\ell y_\ell$ belong to $H_{B/R}$.

Their target images are $\lambda c$ and $a_\ell^{N+1}$ respectively. The first avoids $\mathfrak q$, proving $\mathfrak h_B\not\subset\mathfrak q$. The others put all $a_\ell$ in the radical $\mathfrak h_B$, hence give $\mathfrak h_A\subset\mathfrak h_B$. These are precisely both resolution requirements. ∎

<a id="smoothing-section-separable"></a>

For separable residue extensions, a suitable sequence in the base permits the local lifting construction to produce a resolution.

<a id="smoothing-lemma-ogoma"></a>

#### Lemma D.31: ogoma

Reading source: [Stacks, Tag 07FC](https://stacks.math.columbia.edu/tag/07FC).

Let \(A\) be Noetherian, \(M\) a finite \(A\)-module, \(S\subset A\) multiplicative, and \(\pi\in A\). Suppose that multiplication by \(\pi\) and \(\pi^2\) has equal kernels on \(S^{-1}M\). There is one \(s\in S\) such that, for every positive integer \(n\),
\[
\ker(s^n\pi:M\to M)=\ker((s^n\pi)^2:M\to M).
\]

**Proof.** Let
\[
N=\{m\in M:\pi^2m/1=0\text{ in }S^{-1}M\}.
\]
It is a submodule of the finite module \(M\), so [S01, Lemma 1.3](AG-RG-S01.md) gives a finite generating list \(u_1,\ldots,u_t\). By the assumed equality of localized kernels, \(\pi u_j/1=0\) for every \(j\). The fraction-zero calculation of [S01, Lemma 1.1](AG-RG-S01.md) gives \(s_j\in S\) with \(s_j\pi u_j=0\) in \(M\). Put \(s=\prod_j s_j\), using \(s=1\) for an empty list. Multiplication by \(s\pi\) kills every generator and hence all of \(N\).

Fix \(n>0\) and suppose \((s^n\pi)^2m=0\). Since \(s\) is a unit after localization, this implies \(\pi^2m/1=0\), so \(m\in N\). Therefore \(s\pi m=0\), and multiplication by \(s^{n-1}\) gives \(s^n\pi m=0\). The reverse inclusion follows by applying \(s^n\pi\) a second time to an element of its kernel. The same \(s\) works for all \(n\). The argument also covers \(0\in S\) and \(M=0\), without cancelling \(s\) inside \(M\). ∎

<a id="smoothing-lemma-find-sequence"></a>

#### Lemma D.32: find sequence

Reading source: [Stacks, Tag 07FD](https://stacks.math.columbia.edu/tag/07FD).

Let \(\Lambda\) be Noetherian, let \(I\subset\mathfrak q\) with \(\mathfrak q\) prime, and fix positive integers \(n,e\). Suppose that \(L=\Lambda_{\mathfrak q}\) is regular local of dimension \(d\) and that \(\mathfrak q^nL\subset IL\). There are \(\pi_1,\ldots,\pi_d\in\Lambda\) satisfying
\[
(\pi_1,\ldots,\pi_d)L=\mathfrak qL,
\qquad \pi_i^n\in I,
\]
and, for every \(1\le i\le d\),
\[
\operatorname{Ann}_{\Lambda/(\pi_1^e,\ldots,\pi_{i-1}^e)\Lambda}(\pi_i)
=\operatorname{Ann}_{\Lambda/(\pi_1^e,\ldots,\pi_{i-1}^e)\Lambda}(\pi_i^2).
\]
The prescribed exponents \(n,e\) are retained.

**Proof.** Set \(S=\Lambda\setminus\mathfrak q\). Regularity says that \(\mathfrak qL/(\mathfrak qL)^2\) has dimension \(d\). Lift a basis to \(\mathfrak qL\); finite-module Nakayama, [S01, Lemma 1.2](AG-RG-S01.md), makes these \(d\) lifts generate \(\mathfrak qL\). Each lift is a fraction with numerator in \(\mathfrak q\) and denominator in \(S\). Multiplying each by its denominator replaces it by \(a_i\in\mathfrak q\) and preserves the minimal generating property, since these denominators are units in \(L\).

The containment \(\mathfrak q^nL\subset IL\) gives \(a_i^n/1=0\) in \(S^{-1}(\Lambda/I)\). Exact localization and the fraction-zero criterion [S01, Lemma 1.1](AG-RG-S01.md) provide \(v_i\in S\) with \(v_i a_i^n\in I\). Replace \(a_i\) by \(v_i a_i\). Its \(n\)th power is \(v_i^{n-1}(v_i a_i^n)\in I\), and the list still minimally generates the localized maximal ideal. No change of \(n\) was made. Later multiplication of an entry by an element of \(S\) also preserves these two properties.

Now choose the entries in order. Suppose \(\pi_1,\ldots,\pi_{i-1}\) have been fixed, with their required annihilator equalities, and keep the remaining entries as their current \(a_j\). The whole list is a minimal generating list of \(\mathfrak qL\), so it is regular by the full parameter proof AG-CA-12, Theorem 6.1. The power theorem AG-CA-12, Proposition 1.3, applied with exponents \(e\) on the first \(i-1\) entries and exponent one on the rest, therefore makes \(a_i\) injective on
\[
L/(\pi_1^e,\ldots,\pi_{i-1}^e)L.
\]
Its square is injective too, so their kernels are both zero.

Take the finite \(\Lambda\)-module \(M_i=\Lambda/(\pi_1^e,\ldots,\pi_{i-1}^e)\Lambda\). S01, Lemma 1.1 identifies its localization with the displayed quotient of \(L\). Apply [D.31](#smoothing-lemma-ogoma) to \(M_i,S,a_i\). It supplies \(w_i\in S\) for which multiplication by \(w_i a_i\) and its square has the same kernel on \(M_i\); choose the positive power one in that lemma and set \(\pi_i=w_i a_i\). This is exactly the required \(i\)th annihilator equality.

The earlier equalities involve only their own entry and the entries preceding it, none of which has changed. The \(n\)th-power condition remains true because \(I\) is an ideal. In \(L\), the unit \(w_i\) preserves the generating list and its successive regularity: the preceding power ideals stay the same, and multiplication by a unit preserves injectivity on every quotient. Thus the next step has the same hypotheses. After \(d\) steps the list satisfies all assertions. If \(d=0\), Nakayama gives \(\mathfrak qL=0\); the empty list already satisfies them, with both given exponents unchanged. ∎

<a id="smoothing-lemma-resolve-special"></a>

#### Lemma D.33: resolve special

Reading source: [Stacks, Tag 07FE](https://stacks.math.columbia.edu/tag/07FE).

In [D.27](#smoothing-situation-local), let the base be a field \(k\), let \(\Lambda\) be Noetherian, and let \(\mathfrak q\) be minimal over \(\mathfrak h_A\). Assume that \(L=\Lambda_{\mathfrak q}\) is regular local and that its residue field \(K=\kappa(\mathfrak q)\) is separable over \(k\). Then the problem has a resolution.

**Proof.** Write \(\mathfrak m=\mathfrak qL\) and \(d=\dim L\). If \(d=0\), regularity says that \(\mathfrak m/\mathfrak m^2=0\). The finite-module Nakayama lemma [F.10](#algebra-lemma-NAK) makes \(\mathfrak m=0\), so \(L=K\). By [F.23](#algebra-lemma-colimit-syntomic), this field is a filtered colimit of smooth \(k\)-algebras. Finite presentation and [F.90](#algebra-lemma-when-colimit) factor \(A\to L\) through one such algebra. The resulting localized resolution returns to \(\Lambda\) by [D.30](#smoothing-lemma-delocalize-height-zero). Henceforth \(d>0\).

Set \(I=H_{A/k}\Lambda\). Minimality gives \(\sqrt{IL}=\mathfrak m\). Choose finite generators of \(\mathfrak m\), and, for each generator, a positive power belonging to \(IL\). A monomial whose degree exceeds the sum of these powers minus the number of generators contains one of those powers. Consequently there is \(n>0\) with \(\mathfrak m^n\subset IL\). The Hilbert theorem AG-CA-03, Theorem 2.1 makes \(A\) Noetherian; choose \(H_{A/k}=(a_1,\ldots,a_r)\).

Introduce the polynomial base \(P=k[x_1,\ldots,x_d]\) and the finitely presented algebra
\[
B=A[x_1,\ldots,x_d,z_{ij}]/(x_i^n-\sum_j a_jz_{ij}).
\]
On the chart where \(a_j\) is invertible, each equation eliminates \(z_{ij}\). This chart is a polynomial algebra over \(A_{a_j}[x_1,\ldots,x_d]\), and is smooth over \(P\). On inverting \(x_i\), the equation gives \(1=\sum_j a_jx_i^{-n}z_{ij}\); thus these \(a_j\)-charts cover \(B_{x_i}\). Smooth gluing [F.67](#algebra-lemma-locally-smooth) proves that \(B_{x_i}/P\) is smooth.

Apply [D.9](#smoothing-lemma-improve-presentation) over \(P\). It supplies \(B\to C\) and a retraction \(C\to B\), with each \(C_{x_i}/P\) smooth and its differential module finite free. Its symmetric-algebra construction is smooth also on every \(a_j\)-chart. The algebra \(C\) is finitely presented, since it is finite type over the Noetherian ring \(P\). By [D.15(e)](#smoothing-lemma-compare-standard), choose a common \(c>0\) such that every \(x_i^c\) is strictly standard in \(C/P\), and put \(e=8c\).

Use [D.32](#smoothing-lemma-find-sequence) with the fixed \(n,e,I\). Obtain elements \(\pi_i\in\Lambda\) generating \(\mathfrak m\) in \(L\), with
\[
\pi_i^n=\sum_j a_j\lambda_{ij}
\quad\hbox{in }\Lambda,
\]
and equal kernels for \(\pi_i\) and \(\pi_i^2\) on each quotient by the earlier \(\pi_j^e\). Sending \(x_i\) to \(\pi_i\) and \(z_{ij}\) to \(\lambda_{ij}\) defines \(B\to\Lambda\); the retraction defines \(C\to\Lambda\).

It is enough to resolve this new problem over \(P\). In fact the smooth \(a_j\)-charts put every \(a_j\) in \(H_{C/P}\). A \(P\)-resolution through \(T\) therefore preserves \(\mathfrak h_A\). A smooth \(P\)-neighbourhood is smooth over \(k\), so \(H_{T/P}\subset H_{T/k}\). Finite presentation over \(P\) is finite presentation over \(k\), by adjoining the finitely many \(x_i\) to a presentation. These observations give both conditions of an original \(k\)-resolution.

For the new problem apply [D.28](#smoothing-lemma-lift-solution) to \(x_1^c,\ldots,x_d^c\). On the source quotients multiplication by a remaining polynomial variable is injective, as equality of polynomial coefficients shows. On a target quotient, equality \(\ker u=\ker u^2\) implies \(\ker u^s=\ker u\) for all \(s\ge1\): if \(u^{s+1}v=0\), applying the equality to \(u^{s-1}v\) gives \(u^sv=0\), and induction finishes the argument. Thus D.32 supplies the equal kernels for \(\pi_i^c\) and \(\pi_i^{2c}\). Since \((x_i^c)^8=x_i^e\), D.28 reduces the task to the quotient by these \(e\)-th powers.

Localize that quotient at its target prime. The base and target are
\[
S=P_{(x_1,\ldots,x_d)}/(x_1^e,\ldots,x_d^e),
\qquad L_0=L/(\pi_1^e,\ldots,\pi_d^e).
\]
The contracted prime is \((x_1,\ldots,x_d)\), because reduction of a polynomial in the \(\pi_i\) is its constant in \(k\subset K\). The polynomial local base is regular by iterating AG-CA-14, Proposition 3.3 from the field. The regular local ring \(L\) has dimension \(d\), and its maximal ideal is generated by the \(d\) elements \(\pi_i\). The minimal-parameter theorem AG-CA-12, Theorem 6.1 makes this list regular. The criterion [F.46](#algebra-lemma-flat-over-regular) gives flatness of \(P_{(x)}\to L\); quotient base change gives flatness of \(S\to L_0\).

The maximal ideals of \(S\) and \(L_0\) are nilpotent: every monomial of degree \(d(e-1)+1\) contains an \(e\)-th power. The closed fibre of \(S\to L_0\) is \(K/k\). F.23 expresses it as a smooth colimit, and the nilpotent lifting theorem [D.18](#smoothing-proposition-lift) does the same for \(L_0/S\). By F.90, the finitely presented algebra \(C\otimes_P S\) factors through a smooth \(S\)-algebra.

To return to the unlocalized quotient, let its target prime be \(\overline{\mathfrak q}\). Its target localization has dimension zero by the preceding nilpotence calculation. If the quotient input's singular radical escapes \(\overline{\mathfrak q}\), its identity factorization already resolves the problem. Otherwise \(\overline{\mathfrak q}\) is minimal over that radical, and D.30 delocalizes the smooth factorization. D.28 lifts the quotient resolution to \(P\to C\to\Lambda\). The change-of-base argument above then gives the required resolution over \(k\). ∎

### Inseparable residue fields

<a id="smoothing-section-inseparable"></a>

For inseparable residue extensions, we first enlarge the coefficient field and control the necessary denominators. The resulting finite system then permits a local resolution.

<a id="smoothing-lemma-helper"></a>

#### Lemma D.34: helper

Reading source: [Stacks, Tag 07FG](https://stacks.math.columbia.edu/tag/07FG).

Let \(k\) be a field of characteristic \(p>0\), and let \((\Lambda,\mathfrak m,K)\) be an Artinian local \(k\)-algebra. If \(H_1(L_{K/k})\) is finite-dimensional over \(K\), then \(\Lambda\) is a directed union of Artinian local \(k\)-subalgebras \(A\), essentially of finite type over \(k\), such that \(A\to\Lambda\) is faithfully flat and \(\mathfrak m_A\Lambda=\mathfrak m\).

**Proof.** Keep the specified map \(i:k\to\Lambda\) throughout. Its reduction identifies \(k\) with a subfield of \(K\). By AG-CA-03, Theorem 4.2, choose generators \(u_1,\ldots,u_d\) of \(\mathfrak m\) and a least \(N\ge1\) with \(\mathfrak m^N=0\). We use the following internal prime-field lifting calculation. For a field \(E\) of characteristic \(p\), [F.119](#more-algebra-lemma-p-basis) proves the p-basis presentation
\[
E=E^p[T_b:b\in\mathcal B]/(T_b^p-b^p:b\in\mathcal B).
\]
In a square-zero test \(f:E\to C/J\), define a map on \(E^p\) by sending \(a^p\) to the pth power of any lift of \(f(a)\). The pth root in \(E\) is unique, and the value is independent of the lift because \(j^p=0\) for \(j\in J\). The Frobenius identities prove addition and multiplication for this map. Choose any lifts of the images of the basis elements \(b\). Their pth powers are exactly the prescribed values of \(b^p\), so the displayed presentation gives an \(\mathbb F_p\)-map \(E\to C\) lifting \(f\). This proves formal smoothness for every such field, including an infinite p-basis.

It lifts maps across a nilpotent ideal by its successive powers: the kernel from the quotient by \(J^{a+1}\) to the quotient by \(J^a\) is square zero for \(a\ge1\). In particular a residue section \(s:K\to\Lambda\) exists. Define \(\psi_s:K[X_1,\ldots,X_d]\to\Lambda\) by this section and \(X_j\mapsto u_j\).

We first prove that the section can be chosen so that, for a field \(k\subset F_0\subset K\) finitely generated over \(k\), the subring \(\psi_s(F_0[X])\) contains \(i(k)\). This is automatic for \(N=1\), with \(s\) the identity and \(F_0=k\). Suppose \(N>1\) and put \(I=\mathfrak m^{N-1}\). Then \(I^2=0\) and \(\mathfrak m I=0\), so scalar multiplication on \(I\) factors through \(K\). Applying the induction assertion to \(\Lambda/I\) gives a section \(s_0\) and a finitely generated field \(F\supset k\) containing the prescribed image in \(s_0(F)[\bar u]\). Lift \(s_0\) to \(s\). The ring
\[
T=F[X_1,\ldots,X_d]/(X_1,\ldots,X_d)^N
\]
maps onto \(s_0(F)[\bar u]\). The kernel is contained in the ideal of positive-degree terms, because a nonzero constant from \(F\) has nonzero residue. It is therefore nilpotent. Formal smoothness of \(k/\mathbb F_p\) lifts its specified map to a map \(v:k\to T\). The difference \(e=i-\psi_s v:k\to I\) is an \(\mathbb F_p\)-derivation: expand a product, use agreement modulo \(I\), and discard the product of the two errors in \(I^2\).

Choose the absolute differential basis \((dz_j)_{j\in J}\) supplied by [F.119](#more-algebra-lemma-p-basis). Formal smoothness and [F.17](#algebra-lemma-characterize-formally-smooth-field-extension) give \(H_1(L_{K/\mathbb F_p})=0\). Consequently [F.131](#more-algebra-lemma-transitivity-gamma) identifies the kernel in
\[
\Omega_{k/\mathbb F_p}\otimes_kK\longrightarrow\Omega_{K/\mathbb F_p}
\]
with \(H_1(L_{K/k})\). A finite basis of this kernel uses only finitely many coordinates \(dz_j\); let \(J_0\) contain their supports. The images of the other basis vectors are linearly independent, since a relation supported outside \(J_0\) would also have to be supported inside it. Define a \(K\)-linear map on their span by \(dz_j\mapsto e(z_j)\). Extend a basis of this span to a basis of \(\Omega_{K/\mathbb F_p}\), assign zero on the extra vectors, and use the universal differential map to obtain a derivation \(\delta:K\to I\).

The formula \(s_1=s+\delta\) gives another ring section: the derivation identity accounts for the two cross terms, and \(I^2=0\) discards the last term. In evaluating \(v(a)\), the constant coefficient is \(a\in k\subset F\). Changes to positive-degree coefficients are annihilated by their monomials, using \(\mathfrak m I=0\). Thus \(\psi_{s_1}v(a)-\psi_s v(a)=\delta(a)\). The remaining error has the form
\[
e(a)-\delta(a)=\sum_{j\in J_0}a_j w_j,
\qquad da=\sum_j a_j dz_j,\quad a_j\in k,
\quad w_j=e(z_j)-\delta(z_j)\in I.
\]
Each \(w_j\) is a linear combination of the finitely many degree-\((N-1)\) monomials \(u^E\), with coefficients in \(K\). Indeed these monomials generate \(I\), and a coefficient may be replaced by its residue because \(\mathfrak m I=0\). Adjoin all these coefficients to \(F\) to obtain \(F_0\). When multiplying a \(w_j\), the scalar \(i(a_j)\) can equally be represented by \(s_1(a_j)\), since their difference belongs to \(\mathfrak m\). The displayed error and \(\psi_{s_1}v(a)\) therefore both lie in \(\psi_{s_1}(F_0[X])\). This proves the assertion for the actual structure map. Fix this section henceforth and call it \(s\).

The map \(\psi_s\) is surjective. Subtract a residue representative, write the remainder using the \(u_j\), and do the same for its coefficients. After \(N\) steps the remainder lies in \(\mathfrak m^N=0\). This produces a polynomial expression for each element. By the Hilbert basis theorem AG-CA-03, Theorem 2.1, its kernel has finitely many generators \(g_1,\ldots,g_b\). Enlarge \(F_0\) by their finitely many coefficients to a field \(F_*\). For each finitely generated intermediate field \(F_*\subset F\subset K\), set
\[
A_F=F[X_1,\ldots,X_d]/(g_1,\ldots,g_b).
\]
The presentation gives \(K\otimes_F A_F=\Lambda\). Choose a basis of \(K/F\) containing \(1\). As an \(A_F\)-module this tensor product is a direct sum of copies of \(A_F\); its \(1\)-coordinate makes the natural map injective, exact, and faithful on every module. Thus \(A_F\subset\Lambda\) and this inclusion is faithfully flat. It contains \(i(k)\) by the preceding assertion.

The ideal generated by the \(X_j\) has \(N\)th power zero, as may be checked in the injective image. Its quotient is \(F\), since each \(g_j\) has zero constant coefficient. The monomials of degree below \(N\) span \(A_F\) over \(F\). Finite dimension makes it Artinian; the nilpotent ideal is its unique maximal ideal, since an element with nonzero constant term is invertible by the finite geometric series. That ideal extends to \(\mathfrak m\). The residue field \(F/k\) is finitely generated, hence is the fraction field of the finite-type domain generated by a field-generator list. [F.40](#algebra-lemma-essentially-of-finite-type-into-artinian-local) now makes \(A_F\) essentially of finite type for its actual, possibly different, \(k\)-structure map.

Two finite field-generator lists have a common successor, their joint generated field. Every polynomial expression in \(\Lambda\) uses finitely many coefficients of \(K\); adjoining them to \(F_*\) places that element in some \(A_F\). These actual subrings therefore form a directed union equal to \(\Lambda\), with all the required properties. ∎

<a id="smoothing-artinian-denominator-enlargement"></a>

#### Lemma D.34A: Artinian denominator enlargement

Reading sources: the unit enlargement in [Stacks, Tag 07FI](https://stacks.math.columbia.edu/tag/07FI) and the finite étale construction in [Tag 04GK](https://stacks.math.columbia.edu/tag/04GK). The auxiliary statement and the calculations below are written here.

Let \(k\) have characteristic \(p>0\), and let \(A\to B\) be a flat local map of Noetherian Artinian local \(k\)-algebras with \(\mathfrak m_AB=\mathfrak m_B\) and \(\mathfrak m_B^N=0\). Denote their residue fields by \(F\subset K\). Given finitely many units \(b_j\in B\), there is a local factorization \(A\to A'\to B\) such that \(A\to A'\) is essentially smooth, \(A'\to B\) is faithfully flat, \(\mathfrak m_{A'}B=\mathfrak m_B\), and a \(p\)-power of each \(b_j\) belongs to the subring \(A'\subset B\). The residue extension is a finite tower of simple transcendental and finite separable extensions. At a transcendental step the unit itself is adjoined.

**Proof.** The local faithful-flatness theorem AG-CA-08, Theorem 2.1 makes the given map faithfully flat, hence injective. For one unit \(b\), write \(\beta\in K^\times\) for its residue.

If \(\beta\) is transcendental over \(F\), take \(A'=A[T]_{\mathfrak m_AA[T]}\) and send \(T\) to \(b\). Every denominator has a nonzero polynomial residue at \(\beta\), hence maps to a unit of \(B\). This defines a local, essentially smooth map with maximal ideal \(\mathfrak m_AA'\) and residue \(F(\beta)\). The ring is Noetherian by the Hilbert basis theorem and localization. Its maximal ideal is nilpotent. Each successive ideal-power quotient is a finite-dimensional vector space over its residue field, since each power is a finite module. These quotients give finite length, so \(A'\) is Artinian.

In the remaining algebraic case, take \(A'=A\) if \(\beta\in F\). Otherwise let \(f\) be its monic irreducible polynomial. If \(f'=0\), every positive exponent occurring in \(f\) is divisible by \(p\), so \(f(T)=f_1(T^p)\). The polynomial \(f_1\) is irreducible, since a factorization would give one of \(f\) by substitution. Repeat this operation while the derivative vanishes. The degrees decrease, so it stops at an irreducible polynomial with nonzero derivative. Its roots include \(\beta^{q_0}\) for a \(p\)-power \(q_0\). Bézout with the derivative proves this root separable. Thus \(F_1=F(\beta^{q_0})\) is finite separable over \(F\).

Lift its monic minimal polynomial to \(h\in A[T]\), and put \(A'=A[T]/(h)\). Monic division makes \(A'\) finite free over \(A\). Its reduction is the field \(F_1\); the ideal \(\mathfrak m_AA'\) is nilpotent and is its unique maximal ideal. It is Artinian by the same finite-length argument. Bézout for \(\bar h,\bar h'\) makes \(h'\) invertible in the reduction, and a finite geometric series lifts its inverse across the nilpotent ideal. The one-equation Jacobian proof AG-CA-17, Proposition 6.1 makes \(A'/A\) étale.

Here is the actual map to \(B\). Choose \(r_0\in B\) reducing to \(\beta^{q_0}\). Its derivative value is a unit, and \(h(r_0)\in\mathfrak m_B\). Define
\[
r_{a+1}=r_a-h'(r_a)^{-1}h(r_a).
\]
Polynomial expansion shows that \(h(r_{a+1})\) belongs to the square of the ideal containing \(h(r_a)\): the constant and linear terms cancel, and all remaining terms contain at least two copies of the correction. Consequently \(h(r_a)\in\mathfrak m_B^{2^a}\). The residues stay fixed and the derivatives stay units. Once \(2^a\ge N\), this gives an exact root and the required homomorphism \(A'\to B\). Two roots with that residue are equal: their difference times the divided-difference polynomial is zero, and that polynomial has the nonzero derivative as residue and is a unit. This is the simple-root construction without an external lifting step.

In all three cases \(A'\) is \(A\)-flat and \(A'/\mathfrak m_AA'=F'\), its residue field. Tensor a free \(A\)-resolution of \(F\) with \(A'\); flatness makes it a free \(A'\)-resolution of \(F'\). Tensoring further with \(B\) gives
\[
\operatorname{Tor}^{A'}_1(F',B)=\operatorname{Tor}^{A}_1(F,B)=0.
\]
Apply the Noetherian local criterion AG-CA-08, Theorem 4.2 with local source \(A'\), local target \(B\), and the finite \(B\)-module \(B\). It proves \(A'\to B\) flat. Locality makes it faithfully flat and injective, so \(A'\) is the asserted subring. Its maximal ideal still generates \(\mathfrak m_B\).

In the two algebraic cases choose a unit \(x\in A'\) with residue \(\beta^{-q_0}\), taking \(q_0=1\) if \(\beta\in F\). Then \(xb^{q_0}-1\in\mathfrak m_B\). For a \(p\)-power \(q_1\ge N\), the characteristic-\(p\) binomial identity yields
\[
(xb^{q_0})^{q_1}=1,
\qquad b^{q_0q_1}=x^{-q_1}\in A'.
\]
In the transcendental case \(b\) itself already belongs to \(A'\). Repeat for the finite unit list. Each earlier power remains in every later subring, and the maps remain essentially smooth by composition.

For use in D.35, retain the natural differential information. A simple transcendental residue step has
\[
\Omega_{F(\beta)/k}
=(\Omega_{F/k}\otimes_F F(\beta))\oplus F(\beta)\,d\beta,
\]
by polynomial differentials and the inverse rule in localization. In a finite separable step, differentiating the monic equation solves its new differential uniquely, because its derivative is invertible; it leaves precisely the old differential space after scalar extension. Both residue extensions are formally smooth by [F.49](#algebra-lemma-formally-smooth-extensions-easy), so their relative first homology vanishes by [F.17](#algebra-lemma-characterize-formally-smooth-field-extension). The exact field sequence [F.131](#more-algebra-lemma-transitivity-gamma) therefore gives the natural isomorphism
\[
H_1(L_{F'/k})=H_1(L_{F/k})\otimes_F F'.
\]
Composition gives these formulas for the whole finite tower. In particular its first-homology image in \(H_1(L_{K/k})\) is unchanged. ∎

<a id="smoothing-lemma-solution-modulo"></a>

#### Lemma D.35: solution modulo

Reading source: [Stacks, Tag 07FH](https://stacks.math.columbia.edu/tag/07FH). The global representatives and their denominators are constructed explicitly below.

Let \(k\) have characteristic \(p>0\), let \(\Lambda\) be a Noetherian geometrically regular \(k\)-algebra, and choose a prime \(\mathfrak q\), an integer \(n\ge1\), and a finite subset \(E\subset\Lambda_{\mathfrak q}/\mathfrak q^n\Lambda_{\mathfrak q}\). There is a map \(\varphi:P=k[y_1,\ldots,y_m]\to\Lambda\), for some \(m\ge0\), such that, with \(\mathfrak p=\varphi^{-1}(\mathfrak q)\):

1. \(P_{\mathfrak p}\to\Lambda_{\mathfrak q}\) is flat and \(\mathfrak p\Lambda_{\mathfrak q}=\mathfrak q\Lambda_{\mathfrak q}\).
2. Its quotient map has a local Artinian factorization
   \[
   P_{\mathfrak p}/\mathfrak p^nP_{\mathfrak p}
   \longrightarrow D\longrightarrow
   \Lambda_{\mathfrak q}/\mathfrak q^n\Lambda_{\mathfrak q},
   \]
   with the first arrow essentially smooth and the second faithfully flat.
3. The image of \(D\) contains \(E\).

**Proof.** Write \(L=\Lambda_{\mathfrak q}\), \(\mathfrak m=\mathfrak qL\), \(K=L/\mathfrak m\), and \(B=L/\mathfrak m^n\). The injection in [F.133](#more-algebra-proposition-characterization-geometrically-regular) embeds \(H_1(L_{K/k})\) in the finite-dimensional space \(\mathfrak m/\mathfrak m^2\). By [D.34](#smoothing-lemma-helper), choose a local Artinian subring \(A\subset B\) containing \(E\), essentially of finite type over \(k\), faithfully flat to \(B\), with \(\mathfrak m_AB=\mathfrak m_B\). Let \(F\subset K\) be its residue field. This field is finitely generated over \(k\): present \(A\) as a localization of a finite-type algebra, take its residue quotient, and express the resulting field as fractions of the image of the finite algebra-generator list.

The differentials of such a field-generator list span \(\Omega_{F/k}\), since the product and inverse rules differentiate every rational expression. Select a basis \(d\theta_1,\ldots,d\theta_t\) from this spanning list and lift its elements to \(A\). Each lift has a representative \(a_j/b_j\in L\), with \(a_j\in\Lambda\) and \(b_j\notin\mathfrak q\).

By the left injection in [F.131](#more-algebra-lemma-transitivity-gamma), \(H_1(L_{F/k})\otimes_FK\) embeds in \(H_1(L_{K/k})\). Denote its image in \(\mathfrak m/\mathfrak m^2\) by \(V\). If \(n\ge2\), the elements of \(\mathfrak m_A\) span this cotangent space over \(K\): its identification with the cotangent space of \(B\) and the equality of extended maximal ideals prove that assertion. Choose elements whose images are a basis of a complement to \(V\). Lift them to fractions \(c_i/d_i\), with \(c_i\in\mathfrak q\) and \(d_i\notin\mathfrak q\). For \(n=1\), select instead representatives \(c_i\in\mathfrak q\) of a complement in \(\mathfrak m/\mathfrak m^2\) and put \(d_i=1\). Their images in \(B=K\) are zero, so are already in \(A\).

Apply [D.34A](#smoothing-artinian-denominator-enlargement) to the finitely many units represented by \(b_j,d_i\) in \(B\). Obtain \(A\subset A'\subset B\), with \(A\to A'\) essentially smooth, \(A'\to B\) faithfully flat, and unchanged extended maximal ideal. For appropriate \(p\)-powers \(q_j,r_i\), all four kinds of global elements
\[
a_jb_j^{q_j-1},\quad b_j^{q_j},\quad
c_id_i^{r_i-1},\quad d_i^{r_i}
\]
have images in \(A'\). The first and third are the fractional lifts multiplied by the indicated powers; the second and fourth are supplied by the enlargement. Record in addition every original denominator which was adjoined at a transcendental residue step. It itself has its image in \(A'\).

Let \(F'\) be the residue field of \(A'\). The residues of the first two kinds of elements, together with these recorded transcendental denominators, have differentials spanning \(\Omega_{F'/k}\). Indeed their quotient is \(\theta_j\), so the inverse rule expresses each old \(d\theta_j\) in their span. D.34A adds just one new differential at each transcendental step and none at a finite separable step. Select a differential basis from this finite list, and call its actual global representatives \(\lambda_1,\ldots,\lambda_s\in\Lambda\). This argument does not set \(d(b_j^{q_j})\) to zero in \(F'\): the root \(b_j\) need not belong to that field. Every selected representative has its class in \(A'\).

Define \(P'=k[y_1,\ldots,y_s]\to\Lambda\) by these elements, let \(\mathfrak p'\) be the inverse image of \(\mathfrak q\), and set \(K_0=\kappa(\mathfrak p')\subset F'\). Since all the basis differentials come from \(K_0\), \(\Omega_{F'/K_0}=0\). The extension is finitely generated, because \(F'/k\) is finitely generated. The equality proved in [F.98](#more-algebra-lemma-cartier-equality) gives
\[
-\dim_{F'}H_1(L_{F'/K_0})
=\operatorname{trdeg}_{K_0}F'.
\]
Its two nonnegative dimensions must both be zero. Finitely many algebraic field generators give a finite extension by multiplying their degrees; the zero first homology gives separability by [F.91](#algebra-proposition-characterize-separable-field-extensions). Thus \(F'/K_0\) is finite separable. The field sequence F.131, whose relative first homology and differential module here vanish, identifies
\[
H_1(L_{K_0/k})\otimes_{K_0}K
=H_1(L_{F'/k})\otimes_{F'}K
=H_1(L_{F/k})\otimes_FK.
\]
The last identity is the natural one retained in D.34A, so its image in \(\mathfrak m/\mathfrak m^2\) is still \(V\).

Apply [F.109](#more-algebra-lemma-geometrically-regular-over-field) using the selected differential basis. It gives a flat map \(P'_{\mathfrak p'}\to L\) and a regular quotient \(L/\mathfrak p'L\). Its written conormal square identifies the image of the source cotangent space with the preceding first-homology image \(V\). Append the global elements \(\lambda_{s+i}=c_id_i^{r_i-1}\) to form \(P=k[y_1,\ldots,y_m]\to\Lambda\). Their cotangent classes are the originally chosen complementary classes multiplied by the nonzero scalars \(\bar d_i^{r_i}\), and therefore still form a complementary basis. Their residues are zero. Hence \(P_{\mathfrak p}\) is the localization of \(P'_{\mathfrak p'}[y_{s+1},\ldots,y_m]\) at the prime generated by \(\mathfrak p'\) and these variables.

Polynomial local regularity is proved in AG-CA-14, Proposition 3.3. The old regular parameters and the appended variables are a regular parameter list for this source: its maximal ideal is generated by them and its cotangent space is the old cotangent space plus one independent class for each new variable. Their images are a regular sequence in \(L\). The old list remains regular by the flat map from \(P'_{\mathfrak p'}\), applying flat base change to each successive multiplication injection. The new list is a minimal parameter list on the regular local quotient \(L/\mathfrak p'L\), hence is regular by AG-CA-12, Theorem 6.1. Concatenating these lists proves the assertion. [F.46](#algebra-lemma-flat-over-regular) now makes \(P_{\mathfrak p}\to L\) flat. Their cotangent classes span \(\mathfrak m/\mathfrak m^2\); Nakayama [F.10](#algebra-lemma-NAK) gives \(\mathfrak pL=\mathfrak m\). This proves (1).

All polynomial generators have their classes in \(A'\), so the map to \(B\) factors through \(A'\). An element outside \(\mathfrak p\) has nonzero residue and maps to a unit of this local ring. Moreover \(\mathfrak p^n\) maps to zero in \(B\), hence in \(A'\subset B\). We obtain
\[
R=P_{\mathfrak p}/\mathfrak p^nP_{\mathfrak p}
\longrightarrow A'\longrightarrow B.
\]
The ring \(R\) is Artinian: it is Noetherian local with nilpotent maximal ideal, and its finite ideal-power quotients have finite dimension over its residue field. Its composite map to \(B\) is the flat base change of (1). Since \(A'\to B\) is faithfully flat, [F.48](#algebra-lemma-flatness-descends-more-general) makes \(R\to A'\) flat. The ideals \(\mathfrak pA'\) and \(\mathfrak m_{A'}\) become equal in \(B\); faithful flatness detects equality by tensoring their quotient, so they are equal. The residue extension is the finite separable extension \(F'/K_0\) just proved. [F.40](#algebra-lemma-essentially-of-finite-type-into-artinian-local) makes \(A'\) a finite \(R\)-module. Since \(R\) is Noetherian, it is a finitely presented algebra, by taking finite module generators and a finite kernel in their polynomial presentation. Its only fibre is the finite separable residue field. The proved étale criterion [F.16](#algebra-lemma-characterize-etale) therefore makes \(R\to A'\) étale, in particular essentially smooth. Take \(D=A'\). It retains \(E\subset A\), proving (2) and (3). ∎

<a id="smoothing-lemma-enlarge-solution-modulo"></a>

#### Lemma D.36: enlarge solution modulo

Reading source: [Stacks, Tag 07FI](https://stacks.math.columbia.edu/tag/07FI).

Use the notation and a local Artinian factorization of D.35:
\[
R=k[y_1,\ldots,y_m]_{\mathfrak p}/\mathfrak p^n
\longrightarrow D\longrightarrow
B=\Lambda_{\mathfrak q}/\mathfrak q^n\Lambda_{\mathfrak q},
\]
where \(R\to D\) is essentially smooth and \(D\to B\) is flat. For every \(\lambda\in\Lambda\setminus\mathfrak q\), there are a positive \(p\)-power \(q\) and a local Artinian factorization \(R\to D\to D'\to B\) with \(D\to D'\) essentially smooth, \(D'\to B\) faithfully flat, and \(\lambda^q\) in the image of \(D'\).

**Proof.** The polynomial-source maximal ideal extends to that of \(B\), by D.35(1). We verify that the maximal ideal of \(D\) does also, even for a factorization other than the particular étale one constructed there. The closed fibre \(D/\mathfrak m_RD\) is Artinian local and essentially smooth over the field \(R/\mathfrak m_R\). The regularity theorem AG-CA-18, Theorem 2.1, followed by localization, makes it regular. An Artinian local ring has dimension zero. For a regular local ring of dimension zero its cotangent dimension is zero; its finite maximal ideal equals its square, and Nakayama makes that ideal zero. Thus this fibre is a field and \(\mathfrak m_D=\mathfrak m_RD\). Extending to \(B\) gives \(\mathfrak m_DB=\mathfrak m_B\).

All rings required by D.34A are Noetherian. The source \(R\) is Noetherian, and the essentially smooth algebra \(D\) is a localization of a finitely presented \(R\)-algebra, so the Hilbert basis theorem and localization make it Noetherian. The ring \(B\) is the displayed Artinian quotient of the Noetherian local ring \(\Lambda_{\mathfrak q}\), and \(\mathfrak m_B^n=0\). The flat local map \(D\to B\) is faithfully flat by the local criterion. The image of \(\lambda\) is a unit because its residue is nonzero. Apply the one-unit case of [D.34A](#smoothing-artinian-denominator-enlargement). It supplies \(D\subset D'\subset B\), an essentially smooth first map, a faithfully flat last map, and the exact power containment \(\lambda^q\in D'\). Composition with \(R\to D\) gives the required factorization. ∎

<a id="smoothing-lemma-resolve-general"></a>

#### Lemma D.37: resolve general

Reading source: [Stacks, Tag 07FJ](https://stacks.math.columbia.edu/tag/07FJ).

Let \(k\) have characteristic \(p>0\). In [D.27](#smoothing-situation-local), suppose that \(\Lambda\) is Noetherian and geometrically regular over \(k\), and that \(\mathfrak q\) is minimal over \(\mathfrak h_A\). Then the problem has a resolution.

**Proof.** Put \(L=\Lambda_{\mathfrak q}\), \(\mathfrak m=\mathfrak qL\), \(d=\dim L\), and \(H=H_{A/k}=(a_1,\ldots,a_r)\). These generators exist by the Hilbert theorem AG-CA-03, Theorem 2.1. The ring \(L\) is regular by geometric regularity. As in D.33, minimality and a finite maximal-ideal generating list give \(N>0\) with \(\mathfrak m^N\subset HL\).

Over \(P_0=k[x_1,\ldots,x_d]\) form
\[
B=A[x_1,\ldots,x_d,z_{ij}]/(x_i^{2N}-\sum_j a_jz_{ij}).
\]
Eliminating \(z_{ij}\) on an \(a_j\)-chart proves smoothness there; the equation makes those charts cover \(B_{x_i}\). By [F.67](#algebra-lemma-locally-smooth), \(B_{x_i}/P_0\) is smooth. Apply [D.9](#smoothing-lemma-improve-presentation) to obtain \(B\to C\) with retraction \(C\to B\). The smooth charts of \(C\) have finite free differentials. Since \(C/P_0\) is finitely presented by the Hilbert theorem, [D.15(e)](#smoothing-lemma-compare-standard) gives one \(c>0\) for which all \(x_i^c\) are strictly standard. If \(d=0\), take \(c=1\). Fix, before making any Artinian approximation,
\[
e=8c,\qquad n=\max\{N+dc,\ d(e-1)+1\}.
\tag{D.37a}
\]

Apply [D.35](#smoothing-lemma-solution-modulo) to the images of a finite \(k\)-algebra generating list of \(A\) in \(\overline L=L/\mathfrak m^n\). It gives a polynomial algebra \(P=k[y_1,\ldots,y_m]\) mapping to \(\Lambda\), its contracted prime \(\mathfrak p\), and local maps
\[
S_0=P_{\mathfrak p}/\mathfrak p^nP_{\mathfrak p}
\longrightarrow D\longrightarrow\overline L.
\]
The first map is essentially smooth, the second is flat, and the generator images belong to \(D\). Also \(P_{\mathfrak p}\to L\) is flat and \(\mathfrak pL=\mathfrak m\). Its closed fibre is a field, so the dimension formula AG-CA-11, Theorem 5.1 gives \(\dim P_{\mathfrak p}=d\).

Choose \(\pi_1,\ldots,\pi_d\in\mathfrak p\) representing a regular parameter list of \(P_{\mathfrak p}\). Polynomial local rings are regular by iteration of AG-CA-14, Proposition 3.3, starting with the field. The minimal-parameter theorem AG-CA-12, Theorem 6.1 makes their minimal generating list regular. Their images generate \(\mathfrak m\) and form a regular parameter list of \(L\), by the same theorem and \(\dim L=d\). Let
\[
R=P[t_1,\ldots,t_d],\qquad \gamma_i=\pi_it_i.
\]
Throughout, localization of this polynomial ring at the coefficients means
\[
R_S=(P\setminus\mathfrak p)^{-1}R=P_{\mathfrak p}[t_1,\ldots,t_d].
\]
It is distinct from localization at a prime of \(R\).

First arrange the source kernel conditions. By [F.75](#algebra-lemma-regular-sequence-in-polynomial-ring), the \(\gamma_i\) form a regular sequence in \(R_S\). Powers of earlier entries preserve regularity by AG-CA-12, Proposition 1.3. Inductively, on the finite \(R\)-module \(R/(\gamma_1^e,\ldots,\gamma_{i-1}^e)\), the localized kernels for \(\gamma_i\) and \(\gamma_i^2\) are zero. [D.31](#smoothing-lemma-ogoma) supplies \(s_i\in P\setminus\mathfrak p\) such that replacing \(\pi_i\) by \(s_i\pi_i\) makes these kernels equal globally. Earlier equalities are unchanged, because their entries and quotient ideals have not changed. Such scaling is by local units, so both local parameter lists remain regular. Continue through all \(i\), using the modified \(\pi_i\) from now on.

Next construct units \(\delta_i\in\Lambda\setminus\mathfrak q\), coefficients \(\lambda_{ij}\in\Lambda\), and an essentially smooth Artinian enlargement \(D\to D'\) with flat local map \(D'\to\overline L\), such that
\[
(\delta_i\pi_i)^{2N}=\sum_j a_j\lambda_{ij}
\quad\hbox{in }\Lambda,
\tag{D.37b}
\]
and both \(\delta_i\) and \(\lambda_{ij}\) have images in \(D'\). We additionally require equal kernels for \(\delta_i\pi_i\) and its square modulo the earlier \((\delta_h\pi_h)^e\). A flat local map into the nonzero local ring \(\overline L\) is faithfully flat, and hence injective, by AG-CA-08, Theorem 2.2. Thus every ring in this construction may be regarded as a subring of \(\overline L\). In particular all relations among the chosen \(A\)-generator images already hold in \(D\), so there is a map \(A\to D\).

Suppose the construction has reached \(i-1\). The element \(\pi_i^N\) lies in \(H\overline L\); faithful flatness contracts this ideal to \(HD'\). Write \(\pi_i^N=\sum_j a_jd_j\) in \(D'\), and lift the \(d_j\) to \(u_j\in L\). The error lies in \(\mathfrak m^n\subset H\mathfrak m^{n-N}\), since \(n\ge N\). Thus choose \(v_j\in\mathfrak m^{n-N}\) with
\[
\pi_i^N=\sum_j a_j(u_j+v_j)\quad\hbox{in }L.
\]
Set \(w_j=\pi_i^N(u_j+v_j)\). Then \(\pi_i^{2N}=\sum_j a_jw_j\), and the residue of \(w_j\) in \(\overline L\) is \(\pi_i^Nd_j\), because \(\pi_i^Nv_j\in\mathfrak m^n\).

Here is the global denominator calculation. Choose \(s_0\notin\mathfrak q\) so that every \(s_0^{2N}w_j\) is represented by \(\widetilde\mu_j\in\Lambda\). The error
\[
r_i=(s_0\pi_i)^{2N}-\sum_j a_j\widetilde\mu_j
\]
vanishes in \(L\). Hence some \(v\notin\mathfrak q\) annihilates \(r_i\), by the fraction-zero criterion of [S01, Lemma 1.1](AG-RG-S01.md). Set \(s=s_0v\) and \(\mu_j=v^{2N}\widetilde\mu_j\). Now \((s\pi_i)^{2N}=\sum_j a_j\mu_j\) in \(\Lambda\), and \(\mu_j/s^{2N}=w_j\) in \(L\).

Use [D.36](#smoothing-lemma-enlarge-solution-modulo) to put \(s^h\) in a further \(D'\), for some \(h>0\). Replace \(s\) by \(s^h\) and \(\mu_j\) by \(s_{\rm old}^{2N(h-1)}\mu_j\). The exact equation survives, and the new coefficient residue is \(s^{2N}\pi_i^Nd_j\in D'\). In \(L/((\delta_1\pi_1)^e,\ldots,(\delta_{i-1}\pi_{i-1})^e)\), multiplication by \(s\pi_i\) is injective, because the preceding entries are powers of a regular parameter list scaled by units. Apply D.31 on the corresponding finite \(\Lambda\)-module to obtain \(s'\notin\mathfrak q\) for which every \((s')^q s\pi_i\), \(q>0\), has equal global kernels with its square. D.36 puts one such \((s')^q\) in an enlargement of \(D'\). Take
\[
\delta_i=(s')^qs,\qquad \lambda_{ij}=(s')^{2Nq}\mu_j.
\]
This proves (D.37b), the residue assertions, and the required target kernel equality. Later enlargements retain all earlier assertions. The finite induction constructs the full list; when \(d=0\) this construction is empty and \(D'=D\).

Map \(R\to\Lambda\) by the given \(P\)-map and \(t_i\mapsto\delta_i\). Give \(R\) its \(P_0\)-structure by \(x_i\mapsto\gamma_i\). Equation (D.37b) defines \(B\to\Lambda\) by \(x_i\mapsto\delta_i\pi_i\) and \(z_{ij}\mapsto\lambda_{ij}\). The retraction defines \(C\to\Lambda\), and these maps induce
\[
C_R=C\otimes_{P_0}R\longrightarrow\Lambda.
\]
Every \(a_j\)-chart of \(C_R/R\) is smooth, so the singular radical of this new input contains \(\mathfrak h_A\). A resolution over \(R\) returns to one over \(k\): finite presentation composes with the polynomial base, and smooth composition gives \(H_{T/R}\subset H_{T/k}\).

Let \(I=(\gamma_1^e,\ldots,\gamma_d^e)\subset R\). [D.7](#smoothing-lemma-strictly-standard-base-change) transports the strictly standard elements \(x_i^c\) to \(\gamma_i^c\). The arranged source and target kernel equalities hold also for their \(c\)-th powers, by the kernel induction in D.33. [D.28](#smoothing-lemma-lift-solution) therefore lifts a resolution modulo \(I\) to an \(R\)-resolution. For \(d=0\), \(I=0\) and this lifting step is unnecessary.

We construct the quotient resolution explicitly. Put \(J=(\pi_1^e,\ldots,\pi_d^e)\subset P\), and let \(\mathfrak r\) be the inverse image of \(\mathfrak q\) in \(R\). Each \(t_i\notin\mathfrak r\), since \(\delta_i\notin\mathfrak q\). Consequently
\[
IR_{\mathfrak r}=JR_{\mathfrak r},
\qquad IL=JL.
\tag{D.37c}
\]
The parameters generate \(\mathfrak pP_{\mathfrak p}\) and \(\mathfrak m\). The bound \(n\ge d(e-1)+1\) in (D.37a) gives, by expansion into monomials,
\[
\mathfrak p^nP_{\mathfrak p}\subset JP_{\mathfrak p},
\qquad\mathfrak m^n\subset JL.
\tag{D.37d}
\]
For \(d=0\), both maximal ideals are zero, so these containments hold as well.

Set \(S_1=S_0[t_1,\ldots,t_d]\). Bars below denote elements in \(D'\subset\overline L\). Each \(\overline\delta_i\) is a unit of \(D'\): its image is a unit and the map is local. Define
\[
B\longrightarrow D'[t_1,\ldots,t_d],
\qquad
x_i\longmapsto\overline\pi_it_i,\quad
z_{ij}\longmapsto
\overline\lambda_{ij}\overline\delta_i^{-2N}t_i^{2N}.
\tag{D.37e}
\]
Injectivity of \(D'\to\overline L\) transports (D.37b) to \(D'\). The image of the \(i\)-th defining equation in (D.37e) is therefore
\[
t_i^{2N}\left(\overline\pi_i^{2N}
-\overline\delta_i^{-2N}\sum_j\overline a_j\overline\lambda_{ij}\right)=0.
\]
Its restriction to \(P_0\) is exactly the prescribed \(x_i\mapsto\pi_it_i\) in \(S_1\), so the map extends to \(B\otimes_{P_0}S_1\). Evaluation \(t_i\mapsto\overline\delta_i\) recovers the prescribed images \(\delta_i\pi_i,\lambda_{ij}\) in \(\overline L\).

The map \(S_0\to D'\) is essentially smooth by construction and composition. Express it as a localization of a smooth finitely presented \(S_0\)-algebra. Localization is the filtered colimit of its principal localizations at finite products of the inverted elements. These stages are smooth, and adjoining the \(t_i\) gives smooth \(S_1\)-stages with colimit \(D'[t_i]\). Finite presentation and [F.90](#algebra-lemma-when-colimit) factor (D.37e) through one smooth \(S_1\)-stage \(T\), followed by the specified map to \(\overline L\). Composing with \(C\to B\) gives the same smooth factorization for \(C\otimes_{P_0}S_1\).

By (D.37d) there are quotient maps \(S_1\to P_{\mathfrak p}[t_i]/J\) and \(\overline L\to L/JL\). Base changing \(T\) gives a smooth factorization over \(P_{\mathfrak p}[t_i]/J\). Localize further at \(\mathfrak r\). Every denominator then has a unit image in the local target, so its map extends. By (D.37c) this is a smooth factorization of the localized problem modulo \(I\).

The target \(L/JL\) has nilpotent maximal ideal: degree \(d(e-1)+1\) monomials vanish. Thus its dimension is zero. If the singular radical of the unlocalized quotient input escapes the image of \(\mathfrak q\), the identity factorization resolves that quotient. Otherwise this prime is minimal over the radical, and [D.30](#smoothing-lemma-delocalize-height-zero) delocalizes the smooth factorization just obtained. D.28 then lifts it before quotienting by \(I\). Finally the polynomial change of base returns the resolution to \(k\). All constructions above include \(d=0\), empty parameter lists, and the specified target maps. ∎

### The main theorem

<a id="smoothing-section-main"></a>

The final argument selects a maximal unsuccessful singular radical and uses the local resolutions to enlarge it, giving a contradiction.

<a id="smoothing-theorem-popescu"></a>

#### Theorem D.38: popescu

Reading source: [Stacks, Tag 07GC](https://stacks.math.columbia.edu/tag/07GC).

If \(R\to\Lambda\) is a regular map between Noetherian rings, then \(\Lambda\), as an \(R\)-algebra, is a filtered colimit of smooth \(R\)-algebras.

**Proof.** The reduction [D.26](#smoothing-lemma-reduce-to-field) reduces the assertion to a field \(k\) and a Noetherian geometrically regular \(k\)-algebra \(\Lambda\). By [D.8](#smoothing-lemma-final-solve), it is enough that every finite type factorization \(k\to A\to\Lambda\) can be followed by \(A\to B\to\Lambda\) with \(B\) finite type and \(\mathfrak h_B=\Lambda\). All such algebras are finitely presented by the Hilbert theorem.

Assume some factorization has no such successor. Among the singular radicals of all these unsuccessful factorizations choose a maximal one, say \(\mathfrak h_A\). A nonempty collection of ideals in a Noetherian ring has a maximal member: otherwise successive strict enlargements would contradict the ascending chain condition. The ideal \(\mathfrak h_A\) is proper, since if it were \(\Lambda\), \(A\) itself would be a successor.

There is a prime \(\mathfrak q\) minimal over \(\mathfrak h_A\). Here are the existence details. Zorn's lemma first gives an ideal maximal among the proper ideals containing \(\mathfrak h_A\): a chain union is still proper, since it cannot contain \(1\). Such an ideal is prime, because if \(a\) is outside it, the ideal and \(a\) generate \(1\), and multiplication of that relation by \(b\) shows that \(ab\) in the ideal forces \(b\) into it. Now order all primes containing \(\mathfrak h_A\) by reverse inclusion. A chain intersection is a proper ideal containing \(\mathfrak h_A\), and is prime: if \(ab\) belongs to the intersection while \(a,b\) do not, two members excluding them have a smaller member excluding both, contradicting its primality. Zorn's lemma therefore supplies the desired minimal prime.

Geometric regularity makes \(\Lambda_{\mathfrak q}\) regular local. In positive characteristic [D.37](#smoothing-lemma-resolve-general) resolves this problem. In characteristic zero every field extension is separable in the sense of [F.5](#algebra-definition-separable-field-extension): each finitely generated subextension has a finite transcendence basis followed by a finite algebraic extension, whose irreducible polynomials have nonzero derivatives and hence distinct roots. Thus [D.33](#smoothing-lemma-resolve-special) resolves it in that case.

In either case obtain \(A\to C\to\Lambda\) with
\[
\mathfrak h_A\subset\mathfrak h_C,\qquad
\mathfrak h_C\not\subset\mathfrak q.
\]
Because \(\mathfrak h_A\subset\mathfrak q\), the first inclusion is strict. Maximality of the unsuccessful ideal \(\mathfrak h_A\) means that \(C\) has a successor with unit singular radical. Composing its factorization with \(A\to C\) supplies the forbidden successor of \(A\), a contradiction. Hence every finite type input has the required successor. D.8 supplies the smooth filtered presentation, and D.26 returns the assertion to the original regular map. ∎

## 5. Foundation statements and their free-source proofs

The flatness arguments use projective resolutions, the two ways of computing Tor, and the connecting maps of a short exact sequence. These constructions are proved for arbitrary modules in [Algebra and sheaf cohomology before reductive groups, Lemma 1.A (Reductive group schemes)](AG-RG-S01.md#tor-calculus).

We begin with the two-term conormal complex and the field and dimension conventions used below. The numbered arguments then establish the presentation, flatness, regularity and completion results needed in Section 4. Section 6 collects the earlier algebra lessons used along the way.

<a id="cotangent-context"></a>

**The two-term conormal complex.** A polynomial presentation $P=R[X_s]\twoheadrightarrow S$ with kernel $I$ gives the complex $[I/I^2\to\bigoplus_s S\,dX_s]$, in degrees $-1$ and $0$; the map sends the class of $f$ to $df$. We denote it by $\operatorname{NL}(P\to S)$. One presentation is always available: take a variable $X_s$ for each $s\in S$ and send it to $s$. For maps $R\to R'$ and $S\to S'$ forming a commuting square, a map of presentations is a compatible map of their polynomial algebras lifting $S\to S'$. The comparison and homotopy formulas below prove that the resulting two-term object does not depend on the presentation. The localization argument concerns this complex itself.

<a id="inseparable-exponent-context"></a>

**The inseparable exponent calculation.** Let $\alpha$ be algebraic over a field $F$ of characteristic $p$. Its irreducible polynomial is $f(T)=g(T^{p^s})$ for a maximal $s\geq0$. Such $s$ exists because $f$ has finite positive degree. Maximality gives $g'\ne0$. Any factorization of $g$ would give a factorization of $f$, so $g$ is irreducible, and its relatively prime derivative makes it separable. The element $\alpha^{p^s}$ is a root of $g$, hence is separable over $F$. This proves the field-theoretic exponent choice used in the enlargement argument.

<a id="dimension-context"></a>

**Dimension conventions.** The dimension of a ring is the supremum of the lengths of its finite chains of primes. For a prime $\mathfrak p$, its height is $\dim R_{\mathfrak p}$. In a Noetherian local ring of dimension $d$, a system of parameters consists of $d$ elements whose ideal has radical the maximal ideal. Existence is proved in AG-CA-11, Theorem 2.1. Minimal primes and irreducible components are treated in AG-CA-01, Theorem 4.1, Lemma 4.2 and Theorem 4.3. Polynomial-ring dimension and the finite-type domain height formula are AG-CA-11, Theorem 6.1 and AG-CA-09, Theorem 4.3, respectively.

<a id="algebra-definition-lci"></a>

#### Definition F.1: lci

Reading sources: [Stacks, Tag 00SL](https://stacks.math.columbia.edu/tag/00SL); [AI Integrated Stacks, pinned Algebra, lines 37874–37881](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L37874-L37881).

For an arbitrary ring map $R\to S$, the word *syntomic* means that the following three requirements hold together: $S$ is a finitely presented $R$-algebra, it is flat as an $R$-module, and, for every $\mathfrak p\in\operatorname{Spec}R$, the fibre algebra
$$S(\mathfrak p)=S\otimes_R\kappa(\mathfrak p)$$
is a local complete intersection over $\kappa(\mathfrak p)$ in the sense of [F.2](#algebra-definition-lci-field). The phrase *flat local complete intersection over $R$* has this same meaning.

<a id="algebra-definition-lci-field"></a>

#### Definition F.2: lci field

Reading sources: [Stacks, Tag 00S9](https://stacks.math.columbia.edu/tag/00S9); [AI Integrated Stacks, pinned Algebra, lines 37249–37264](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L37249-L37264).

Let $S$ be a finite-type algebra over a field $k$. To call $S$ a *global complete intersection over $k$* is to require a finite presentation
$$S=k[x_1,\ldots,x_n]/(f_1,\ldots,f_c)$$
for which its Krull dimension is exactly $n-c$. A *local complete intersection over $k$* means that one can cover $\operatorname{Spec}S$ by principal opens $D(g_i)$, with each algebra $S_{g_i}$ satisfying this global condition. The zero algebra is included among the global complete intersections by convention; it therefore causes no exception when an open or a fibre is empty.

<a id="algebra-definition-lci-local-ring"></a>

#### Definition F.3: lci local ring

Reading sources: [Stacks, Tag 00SD](https://stacks.math.columbia.edu/tag/00SD); [AI Integrated Stacks, pinned Algebra, lines 37446–37458](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L37446-L37458).

Suppose $S$ is a local $k$-algebra essentially of finite type, where $k$ is a field. The condition *complete intersection over $k$* asks for a regular local $k$-algebra $R$, itself essentially of finite type, together with a regular sequence
$$f_1,\ldots,f_c\in\mathfrak m_R$$
and a $k$-algebra isomorphism $R/(f_1,\ldots,f_c)\cong S$. Thus the presenting ring is local and regular, and the equations lie in its maximal ideal. All these requirements belong to the definition.

<a id="algebra-definition-relative-global-complete-intersection"></a>

#### Definition F.4: relative global complete intersection

Reading sources: [Stacks, Tag 00SP](https://stacks.math.columbia.edu/tag/00SP); [AI Integrated Stacks, pinned Algebra, lines 37943–37951](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L37943-L37951).

For a ring map $R\to S$, a *relative global complete-intersection presentation* consists of
$$S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c)$$
such that, for each $\mathfrak p\in\operatorname{Spec}R$ with nonempty fibre, the ring $S\otimes_R\kappa(\mathfrak p)$ has dimension $n-c$. The map is a *relative global complete intersection* if it has at least one such presentation. When a particular displayed presentation is called a relative global complete intersection, the fibre condition refers to its displayed values of $n$ and $c$. Empty fibres impose no dimension condition.

<a id="algebra-definition-separable-field-extension"></a>

#### Definition F.5: separable field extension

Reading sources: [Stacks, Tag 030O](https://stacks.math.columbia.edu/tag/030O); [AI Integrated Stacks, pinned Algebra, lines 10135–10146](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L10135-L10146).

Consider a field extension $K/k$. It is *separably generated* when there is a transcendence basis $(x_i)_{i\in I}$ such that
$$K/k(x_i\mid i\in I)$$
is algebraic and separable. The index set may be infinite. The condition *separable over $k$* used here is tested on every intermediate field $K'$ finitely generated over $k$: each extension $K'/k$ must be separably generated in the preceding sense. These are the two field-extension conditions used in the separable and inseparable arguments.

<a id="algebra-definition-smooth"></a>

#### Definition F.6: smooth

Reading sources: [Stacks, Tag 00T2](https://stacks.math.columbia.edu/tag/00T2); [AI Integrated Stacks, pinned Algebra, lines 38526–38533](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L38526-L38533).

Smoothness of $R\to S$ requires finite presentation together with the following condition on the naive cotangent complex:
$$H_1(\operatorname{NL}_{S/R})=0,\qquad
\Omega_{S/R}\text{ is a finite projective }S\text{-module}.$$
Equivalently, that two-term complex is quasi-isomorphic to a finite projective module concentrated in degree zero. To verify this equivalence directly, map the two-term complex to its degree-zero cokernel. This map induces an isomorphism on degree-zero homology; it is a quasi-isomorphism exactly when the degree-minus-one kernel, denoted $H_1$, vanishes. Its cokernel is $\Omega_{S/R}$. Presentation independence is proved in [F.11](#algebra-lemma-NL-homotopy).

<a id="algebra-definition-smooth-at-prime"></a>

#### Definition F.7: smooth at prime

Reading sources: [Stacks, Tag 00TB](https://stacks.math.columbia.edu/tag/00TB); [AI Integrated Stacks, pinned Algebra, lines 38953–38960](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L38953-L38960).

Given $R\to S$ and $\mathfrak q\in\operatorname{Spec}S$, *smoothness at $\mathfrak q$* means that some principal neighbourhood of this point has a smooth coordinate algebra over $R$. Explicitly, there must be
$$g\in S\setminus\mathfrak q\quad\text{with}\quad R\to S_g\text{ smooth}.$$
This definition applies to any ring map; finite presentation is required of the witnessing localization through [F.6](#algebra-definition-smooth).

<a id="algebra-definition-unramified"></a>

#### Definition F.8: unramified

Reading sources: [Stacks, Tag 00UT](https://stacks.math.columbia.edu/tag/00UT); [AI Integrated Stacks, pinned Algebra, lines 42897–42912](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L42897-L42912).

For $R\to S$, both unramified conditions require $\Omega_{S/R}=0$. Their finiteness requirements differ: *unramified* requires finite type, whereas *G-unramified* requires finite presentation.

At a prime $\mathfrak q$ of $S$, each condition means that it holds on some principal neighbourhood $D(g)$ of $\mathfrak q$. Thus *unramified at $\mathfrak q$* requires $g\notin\mathfrak q$ with $S_g/R$ of finite type and $\Omega_{S_g/R}=0$; *G-unramified at $\mathfrak q$* requires such a $g$ with $S_g/R$ finitely presented and the same differential-module vanishing.

<a id="algebra-lemma-CM-over-regular-flat"></a>

#### Lemma F.9: CM over regular flat

Reading source: [AI Integrated Stacks, pinned Algebra, lines 34036–34074](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L34036-L34074).

Let $R\to S$ be local, with both rings Noetherian and local. Suppose $R$ is regular, $S$ is Cohen–Macaulay, and
$$\dim S=\dim R+\dim(S/\mathfrak m_RS).$$
Then $S$ is flat as an $R$-module.

**Proof.** We reduce the dimension of the regular source by one while preserving the dimension equality. Write $d=\dim R$. If $d=0$, regularity says $\mathfrak m_R/\mathfrak m_R^2=0$. Nakayama, [F.10](#algebra-lemma-NAK), applies to the finite ideal $\mathfrak m_R$ and gives $\mathfrak m_R=0$. Thus $R$ is a field, and a basis makes every $R$-module free, hence flat.

For $d>0$, consider the finitely many associated primes of $S$. The Cohen–Macaulay component theorem AG-CA-12, Theorem 4.1, says that they are its minimal primes $\mathfrak q_i$ and that $\dim(S/\mathfrak q_i)=\dim S$. None contains $\mathfrak m_RS$. Indeed that containment would give a surjection $S/\mathfrak m_RS\to S/\mathfrak q_i$, forcing the dimension of the latter to be at most that of the former, whereas the hypothesis gives
$$\dim(S/\mathfrak m_RS)=\dim S-d<\dim S.$$
Consequently every contraction $\mathfrak p_i=R\cap\mathfrak q_i$ is strictly smaller than $\mathfrak m_R$.

The prime-avoidance calculation [F.80](#algebra-lemma-silly) now chooses
$$x\in\mathfrak m_R\setminus\bigl(\mathfrak m_R^2\cup\textstyle\bigcup_i\mathfrak p_i\bigr).$$
To check its hypotheses, $\mathfrak m_R$ is not contained in any $\mathfrak p_i$, and is not contained in $\mathfrak m_R^2$, since otherwise Nakayama would again give $d=0$. There is just one nonprime ideal in this avoidance list.

The element $x$ avoids all associated primes of $S$, so it is a nonzerodivisor on $S$. The complete regular-sequence and Cohen–Macaulay arguments of AG-CA-12, Sections 2 and 4, make $S/xS$ Cohen–Macaulay with dimension $\dim S-1$. AG-CA-14, Theorem 1.1 and Corollary 1.2, make $x$ a nonzerodivisor of $R$ and $R/xR$ regular of dimension $d-1$. The quotient map is still local, and its closed fibre is $S/\mathfrak m_RS$. Hence it satisfies
$$\dim(S/xS)=\dim(R/xR)+\dim(S/\mathfrak m_RS).$$
Induction gives flatness of $S/xS$ over $R/xR$.

The two-term free resolution of $R/xR$ has differential multiplication by $x$. Its tensor with $S$ therefore has zero first homology, because $x$ is a nonzerodivisor on $S$. Thus $\operatorname{Tor}_1^R(R/xR,S)=0$. Apply the entire proper-ideal local criterion AG-CA-08, Corollary 4.4, with ideal $(x)$ and module $S$, which is finite over the stipulated Noetherian local overring $S$. The quotient is flat and its required Tor vanishes. This proves flatness over $R$ and completes the induction. ∎

<a id="algebra-lemma-NAK"></a>

#### Lemma F.10: NAK

Reading sources: [Stacks, Tag 00DV](https://stacks.math.columbia.edu/tag/00DV); [AI Integrated Stacks, pinned Algebra, lines 3732–3813](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L3732-L3813).

For a ring $R$, an ideal $I$, and an $R$-module $M$, the following twelve forms of Nakayama's lemma hold. Write $\operatorname{rad}(R)$ for the Jacobson radical.

1. If $M$ is finite and $M=IM$, some $f\in1+I$ annihilates $M$.
2. Under the conditions of (1), $I\subset\operatorname{rad}(R)$ implies $M=0$.
3. If $N,N'\subset M$, $M=N+IN'$ and $N'$ is finite, some $f\in1+I$ satisfies $fM\subset N$ and $M_f=N_f$.
4. Under the conditions of (3), $I\subset\operatorname{rad}(R)$ implies $M=N$.
5. For a module map $N\to M$ with $M$ finite, surjectivity of $N/IN\to M/IM$ implies surjectivity of $N_f\to M_f$ for some $f\in1+I$.
6. Under the conditions of (5), $I\subset\operatorname{rad}(R)$ makes the original map $N\to M$ surjective.
7. If $M$ is finite and the images of $x_1,\ldots,x_n$ generate $M/IM$, these same elements generate $M_f$ over $R_f$ for some $f\in1+I$.
8. Under the conditions of (7), $I\subset\operatorname{rad}(R)$ implies that $x_1,\ldots,x_n$ generate $M$.
9. If $I$ is nilpotent, $M=IM$ implies $M=0$, with no finiteness requirement on $M$.
10. If $I$ is nilpotent and $M=N+IN'$ for submodules $N,N'$, then $M=N$, with no finiteness requirement on $N'$.
11. If $I$ is nilpotent and $N/IN\to M/IM$ is surjective, then $N\to M$ is surjective, without module finiteness assumptions.
12. If $I$ is nilpotent and a possibly infinite family $(x_\alpha)$ generates $M/IM$, it generates $M$.

**Proof.** The determinant assertion [F.10 / nakayama](#algebra-lemma-NAK), namely (1), supplies all finite-module cases. Choose a generating column $y=(y_1,\ldots,y_r)^{\mathsf t}$ of $M$. The equality $M=IM$ expresses each $y_i$ as an $I$-linear combination of the $y_j$, so for a matrix $Z$ with entries in $I$ we have $(1_r-Z)y=0$. By the proved adjugate identity [F.70](#algebra-lemma-matrix-left-inverse),
$$\operatorname{adj}(1_r-Z)(1_r-Z)=\det(1_r-Z)1_r.$$
Consequently $f=\det(1_r-Z)$ kills every generator. Reduction modulo $I$ gives $f\equiv1$, as required. An empty generating list uses $f=1$.

If $I\subset\operatorname{rad}(R)$, [F.34](#algebra-lemma-contained-in-radical) proves that every element of $1+I$ is a unit. Multiplying $fM=0$ by its inverse proves (2).

For (3) and (4), put $Q=M/N$. Since the image of $N'$ generates $Q$ and $N'$ is finite, $Q$ is finite. The hypothesis $M=N+IN'$ gives $Q=IQ$. Apply (1) to obtain $fQ=0$, equivalently $fM\subset N$, and apply (2) for the equality $Q=0$ when the radical condition holds. Once $fM\subset N$, any fraction $m/f^a$ in $M_f$ equals $(fm)/f^{a+1}$ and comes from $N_f$. The inclusion $N_f\subset M_f$ follows from exact localization. Thus the stated equality of localized modules is proved as well.

For a map $u:N\to M$, let $Q=\operatorname{coker}u$. Right exactness identifies its quotient $Q/IQ$ with the cokernel of $N/IN\to M/IM$. The assumed surjectivity therefore gives $Q=IQ$. If $M$ is finite, so is $Q$. Assertion (1) makes $Q_f=0$, and exact localization makes $u_f$ surjective, proving (5). Assertion (2) gives $Q=0$ in the radical case, proving (6). Apply these conclusions to $R^n\to M$, $(r_i)\mapsto\sum r_ix_i$, to get (7) and (8).

Finally suppose $I^a=0$. Repeated substitution into $M=IM$ yields $M=I^aM=0$, proving (9) for an arbitrary module. In (10), $Q=M/N$ satisfies $Q=IQ$, whether or not the image of $N'$ is finite, so (9) gives $Q=0$. For (11), take the same cokernel $Q$ of the given map and use its zero quotient modulo $I$. For (12), quotient by the submodule generated by all $x_\alpha$; its quotient modulo $I$ is zero, so (9) kills it. This proves all twelve assertions, including empty generating lists and arbitrary nilpotent ideals. ∎

<a id="algebra-lemma-NL-homotopy"></a>

#### Lemma F.11: NL homotopy

Reading sources: [Stacks, Tag 00S1](https://stacks.math.columbia.edu/tag/00S1); [AI Integrated Stacks, pinned Algebra, lines 36700–36815](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L36700-L36815).

Let $u:R\to R'$ and $\phi:S\to S'$ be compatible with the structure maps $R\to S$ and $R'\to S'$. Choose polynomial presentations $\alpha:P\twoheadrightarrow S$ and $\alpha':P'\twoheadrightarrow S'$, allowing arbitrary sets of variables. Then:

1. There is a map $\psi:P\to P'$ whose restriction to $R$ is $u$ and for which $\alpha'\psi=\phi\alpha$.
2. Any two such maps induce chain-homotopic maps $\operatorname{NL}(\alpha)\to\operatorname{NL}(\alpha')$.
3. Composing presentation maps composes their induced complex maps.
4. If $u$ and $\phi$ are isomorphisms, every induced map is a homotopy equivalence and a quasi-isomorphism.

In particular the comparison with the [canonical presentation](#cotangent-context) identifies $\operatorname{NL}(\alpha)$ with $\operatorname{NL}_{S/R}$ up to homotopy, and these identifications respect the stated functorialities up to homotopy.

**Proof.** Write $P=R[x_a\mid a\in E]$, $I=\ker\alpha$ and $I'=\ker\alpha'$. For each $a$, choose a polynomial in $P'$ lifting $\phi(\alpha(x_a))$. Sending the variables to these choices and the coefficients through $u$ gives $\psi$ by the polynomial universal property. Each polynomial uses only finitely many variables, so this construction also works when $E$ is infinite. It proves (1).

The two terms of the complex are
$$C_1=I/I^2,\qquad C_0=\bigoplus_{a\in E}S\,dx_a,\qquad
d:C_1\to C_0,\quad [f]\mapsto df.$$
The map is well-defined because $d(fg)=f\,dg+g\,df$ vanishes modulo $I$ when $f,g\in I$. Its target counterpart is $C'_1=I'/(I')^2\to C'_0=\Omega_{P'/R'}\otimes_{P'}S'$. Regard these target modules as $S$-modules through $\phi$. The induced maps are
$$\psi_1([f])=[\psi(f)],\qquad
\psi_0(dx_a)=d\psi(x_a).$$
The map on $I/I^2$ is well-defined since $\psi(I)\subset I'$. On a monomial the product rule gives $\psi_0(df)=d\psi(f)$, since differentiation over $R'$ kills the transformed coefficient from $R$. Addition gives this identity for every polynomial. Thus these are complex maps.

For another choice $\chi$, both evaluations of any $p\in P$ have the same residue in $S'$. Set
$$D(p)=\psi(p)-\chi(p)\pmod{(I')^2}\in I'/(I')^2.$$
Both choices give the same action of $P$ on this module: their difference lies in $I'$, which kills $I'/(I')^2$. That action factors through $S$, because the image of $I$ is in $I'$. The exact product identity
$$\psi(pq)-\chi(pq)
=\psi(p)\bigl(\psi(q)-\chi(q)\bigr)
 +\bigl(\psi(p)-\chi(p)\bigr)\chi(q)$$
therefore becomes the derivation rule for $D$. It is additive and vanishes on $R$. Define the $S$-linear map
$$h:C_0\longrightarrow C'_1,\qquad h(dx_a)=D(x_a).$$
Expanding a monomial by the derivation rule shows $h(dp)=D(p)$ for every polynomial $p$, including constant and empty-variable cases.

Both homotopy identities can now be checked without a diagram omission. For $f\in I$,
$$h(d[f])=D(f)=\psi_1([f])-\chi_1([f]).$$
For each free differential generator,
$$d'h(dx_a)=d\bigl(\psi(x_a)-\chi(x_a)\bigr)
=\psi_0(dx_a)-\chi_0(dx_a).$$
The first identity holds on all relation classes and the second on a free basis, so
$$\psi_1-\chi_1=hd,\qquad \psi_0-\chi_0=d'h.$$
These are exactly a chain homotopy, proving (2).

For a subsequent presentation map $\eta:P'\to P''$, the relation-class map sends $[f]$ successively to $[\psi(f)]$ and $[\eta\psi(f)]$. The differential map sends $dx_a$ to $d\psi(x_a)$ and then to $d(\eta\psi(x_a))$, by the same monomial product-rule calculation. Thus the composite equals the map of the composite presentation, proving (3).

If the two structural square maps are isomorphisms, apply (1) to their inverse square to get a presentation map in the reverse direction. Both composites lie over identity squares. By (2), their complex maps are homotopic to the respective identity maps. This is the required homotopy equivalence. A homotopy changes a degree-one map by $hd$ and a degree-zero map by $d'h$; the former is zero on the kernel and the latter has zero class in the cokernel. Thus homotopic maps act equally on both homology modules. The two reverse maps consequently induce inverse isomorphisms on kernel and cokernel, proving the quasi-isomorphism assertion. Taking identity structural maps and the canonical polynomial presentation proves the last assertion, with composition compatibility already established. ∎

<a id="algebra-lemma-Noetherian-field-extension"></a>

#### Lemma F.12: Noetherian field extension

Reading source: [AI Integrated Stacks, pinned Algebra, lines 6331–6347](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L6331-L6347).

If $A$ is a Noetherian algebra over a field $k$, then extending scalars from $k$ to a finitely generated field extension $K$ leaves it Noetherian.

**Proof.** Select a finite field-generating list $\xi_1,\ldots,\xi_r$ for $K/k$, and put $B=k[\xi_1,\ldots,\xi_r]\subset K$. The field of fractions of $B$ is $K$, since it contains both $k$ and all chosen field generators. Therefore
$$K=(B\setminus\{0\})^{-1}B.$$
A polynomial surjection $k[T_1,\ldots,T_r]\to B$ gives a surjection $A[T_1,\ldots,T_r]\to A\otimes_kB$. The Hilbert-basis and quotient arguments in AG-CA-03, Theorem 2.1, make the latter algebra Noetherian.

Localizing it at the images of the nonzero elements of $B$ gives $A\otimes_kK$: the maps in both directions send a pure tensor with a fraction to that fraction of the corresponding pure tensor. They are inverse by the tensor and localization universal properties. AG-CA-03, Theorem 2.1, also proves that a localization of a Noetherian ring is Noetherian, giving the result. For a finite extension the same conclusion follows from its finite $k$-basis, which makes the tensor algebra a finite free $A$-module; its ideals are then finite $A$-submodules. The argument requires finite field generation, rather than finite degree. ∎

<a id="algebra-lemma-another-variant-local-criterion-flatness"></a>

#### Lemma F.13: another variant local criterion flatness

Reading source: [AI Integrated Stacks, pinned Algebra, lines 24942–24990](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L24942-L24990).

Consider a commutative square of local homomorphisms between Noetherian local rings
$$
\begin{array}{ccc}
R&\longrightarrow&R'\\
\downarrow&&\downarrow\\
S&\longrightarrow&S'.
\end{array}
$$
Let $I\subsetneq R$ and let $M$ be a finite $S$-module. Put $I'=IR'$ and $M'=M\otimes_SS'$. Assume $S'$ is a localization of $B=S\otimes_RR'$, the module $M/IM$ is flat over $R/I$, and the natural map
$$\operatorname{Tor}_1^R(M,R/I)
\longrightarrow\operatorname{Tor}_1^{R'}(M',R'/I')$$
is zero. Then $M'$ is flat over $R'$.

**Proof.** We prove the needed Tor surjection and then apply the proper-ideal criterion. All free-resolution comparisons, naturality and balance used here are the complete arbitrary-module calculus of [AG-RG-S01, Lemma 1.A](AG-RG-S01.md#tor-calculus).

Choose an $R$-free presentation $0\to K\to F\to M\to0$, with no finiteness requirement on $F$. Set $T=\operatorname{Tor}_1^R(M,R/I)$, and let $U$ be the image of $K/IK$ in $F/IF$. The free-presentation kernel formula gives exact sequences
$$0\to T\to K/IK\to U\to0,\qquad
0\to U\to F/IF\to M/IM\to0.$$
Since the last quotient is flat, the proved flat-syzygy criterion AG-CA-07, Theorem 6.1, makes $U$ flat over $R/I$. Tensoring the first sequence with an $R/I$-module $N$ is consequently left exact. Tensoring the second is left exact because its last quotient is flat. Their kernel comparison gives the natural identity
$$\operatorname{Tor}_1^R(M,N)=T\otimes_{R/I}N.$$
This uses only the kernel formula for a free presentation; it does not assume that $K$ is flat.

Take $N=R'/I'$. In $F_0=F\otimes_RR'$ let $K_0$ be the image of $K\otimes_RR'$. Then $F_0$ is $R'$-free and $F_0/K_0=M_0=M\otimes_RR'$. The surjection $K\otimes_RR'\to K_0$ remains surjective after tensoring with $R'/I'$. A cycle in
$$\ker\bigl(K_0\otimes_{R'}R'/I'\to F_0\otimes_{R'}R'/I'\bigr)$$
therefore has a lift in $K\otimes_RR'/I'$. That lift maps to zero in the same free-module target, so is already a source cycle. Thus
$$\operatorname{Tor}_1^R(M,R'/I')
\twoheadrightarrow\operatorname{Tor}_1^{R'}(M_0,R'/I').$$
The preceding natural identity identifies its source with $T\otimes_RR'$.

Write $S'=V^{-1}B$, so $M'=V^{-1}M_0$. We justify localization of the last Tor group with its natural $B$-action. Choose an $R'$-free resolution of $R'/I'$. Balance identifies Tor with the homology after tensoring this resolution with $M_0$; multiplication by $B$ acts on each tensor term. Exact localization of $B$-modules commutes with kernels and images, and tensoring the same resolution with $V^{-1}M_0$ is the localization of each term. Hence
$$\operatorname{Tor}_1^{R'}(M',R'/I')
=V^{-1}\operatorname{Tor}_1^{R'}(M_0,R'/I').$$
The preceding surjection is $B$-linear: multiplication by $S$ acts by the functorial module maps on $M$, while $R'$ acts by scalar extension; the comparison calculus in Lemma 1.A makes these actions compatible. Localizing that surjection consequently gives
$$V^{-1}(T\otimes_RR')\twoheadrightarrow
\operatorname{Tor}_1^{R'}(M',R'/I').$$
The hypothesis says the original natural map from $T$ to this target is zero. Its $R'$-linear extension is zero, and its extension across $V$ is still zero, because the target is a module over $V^{-1}B$. The displayed surjection is therefore the zero map, forcing its target to vanish.

Finally $M'/I'M'$ is obtained from the flat $R/I$-module $M/IM$ by scalar extension to $R'/I'$ and localization at $V$. Scalar extension preserves flatness. For the localization, an injection of $R'/I'$-modules remains injective after tensoring with the unlocalized flat module, and remains injective after exact localization of the resulting $B$-modules. This proves flatness of the localized quotient. The ideal $I'$ is proper because $R\to R'$ is local and $I\subset\mathfrak m_R$. The module $M'$ is finite over the stipulated Noetherian local ring $S'$. AG-CA-08, Corollary 4.4, applies with this quotient flatness and the Tor vanishing just proved, and gives $R'$-flatness. No flatness assumption on $R\to R'$ was added. ∎

<a id="algebra-lemma-base-change-relative-global-complete-intersection"></a>

#### Lemma F.14: base change relative global complete intersection

Reading sources: [Stacks, Tag 00SS](https://stacks.math.columbia.edu/tag/00SS); [AI Integrated Stacks, pinned Algebra, lines 38076–38106](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L38076-L38106).

For a relative global complete-intersection presentation
$$S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c),$$
all three of the following presentations have the same property:

1. For any $R\to R'$, the coefficientwise base change $S\otimes_RR'=R'[x_1,\ldots,x_n]/(f_1,\ldots,f_c)$.
2. If $g\in S$ is represented by $h\in R[x_1,\ldots,x_n]$, the principal localization
$$S_g=R[x_1,\ldots,x_n,Z]/(f_1,\ldots,f_c,hZ-1).$$
3. If $f\in R$ already has a unit image in $S$, its presentation over $R_f$ obtained by viewing the same equations in $R_f[x_1,\ldots,x_n]$.

**Proof.** The fibre condition of [F.4](#algebra-definition-relative-global-complete-intersection) is a dimension condition. We first prove the field-extension calculation it requires. Let $A$ be a finite-type $k$-algebra and $K/k$ any field extension. Its nilradical is nilpotent and has finitely many minimal primes, by AG-CA-03, Proposition 2.2. Nilpotence persists after tensoring with $K$ and does not affect dimension, since every prime contains every nilpotent element.

For the reduced quotient, let its minimal primes be $\mathfrak q_1,\ldots,\mathfrak q_r$. Their product is zero, being contained in their zero intersection. After field extension the product of their extended ideals is still zero. Every prime contains one of these extended ideals: otherwise choose one element outside the prime from each ideal and multiply, contradicting primality. Thus the extended spectrum is the finite union of the closed spectra of
$$(A/\mathfrak q_i)\otimes_kK.$$
Every prime chain belongs to one of these closed sets, by choosing an ideal contained in its smallest prime. Dimension is therefore the maximum of their dimensions.

For each domain $A/\mathfrak q_i$, Noether normalization AG-CA-09, Corollary 3.2, supplies an injective finite polynomial subalgebra $k[t_1,\ldots,t_{d_i}]$. Exact field tensor preserves its injection and finite module generators. The corresponding $K$-algebra is thus integral and injective over $K[t_1,\ldots,t_{d_i}]$. The entire integral-dimension theorem AG-CA-05, Theorem 5.1, gives dimension $d_i$. Taking the maximum proves $\dim(A\otimes_kK)=\dim A$. The zero algebra has empty spectrum and causes no nonempty-fibre case.

For (1), a fibre at a prime of $R'$ is the scalar extension of the original fibre at its contraction, by associativity of tensor products and the induced residue-field inclusion. A nonempty new fibre therefore has the original dimension $n-c$ by the calculation above. The displayed coefficientwise presentation proves (1).

For (2), the field case of [F.77](#algebra-lemma-relative-global-complete-intersection-conormal) proves that each original nonempty fibre is equidimensional of dimension $n-c$. Indeed its minimal-prime height calculation applies to its polynomial presentation over the fibre field, without any Noetherian assumption on $R$. A principal open in a surviving irreducible component has the same dimension as that component: its coordinate domain has unchanged fraction field, and AG-CA-09, Theorem 4.2, computes dimension by its transcendence degree. The localized nonempty fibre therefore still has dimension $n-c$. Adjoining $Z$ and $hZ-1$ adds one variable and one equation, preserving the difference $n-c$. Evaluation at $Z=g^{-1}$ and adjoining that inverse give both directions of the claimed algebra isomorphism.

For (3), multiplication gives $S\otimes_RR_f\cong S$, because the image of $f$ already has an inverse. Its inverse sends $s$ to $s\otimes1$; the forced inverse of $f$ verifies the other composite on fractions. Apply (1) to this base localization. All three arguments apply over arbitrary base rings and to empty fibres. ∎

<a id="algebra-lemma-change-base-NL"></a>

#### Lemma F.15: change base NL

Reading sources: [Stacks, Tag 00S4](https://stacks.math.columbia.edu/tag/00S4); [AI Integrated Stacks, pinned Algebra, lines 36963–36981](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L36963-L36981).

Let $\alpha:P\twoheadrightarrow S$ be a polynomial presentation over $R$, with an arbitrary variable set, and let $R\to R'$ be flat. Put $P'=P\otimes_RR'$, $S'=S\otimes_RR'$, and let $\alpha':P'\twoheadrightarrow S'$ be the resulting presentation. There is an isomorphism of two-term complexes
$$\operatorname{NL}(\alpha)\otimes_RR'
=\operatorname{NL}(\alpha)\otimes_SS'
\cong\operatorname{NL}(\alpha').$$
Consequently the canonical comparison
$$\operatorname{NL}_{S/R}\otimes_SS'\longrightarrow
\operatorname{NL}_{S'/R'}$$
is a homotopy equivalence.

**Proof.** Write $I=\ker\alpha$. Tensoring $0\to I\to P\to S\to0$ with the flat $R'$ identifies $I'=\ker\alpha'$ with $I\otimes_RR'$. The square $(I')^2$ is the image of $I^2\otimes_RR'$: a product of two elementary tensors from $I'$ is the image of the product of their $I$-entries, and every product generator of $I^2$ is obtained this way. Tensoring the quotient therefore gives
$$I'/(I')^2\cong(I/I^2)\otimes_RR'.$$
For any $S$-module $E$, the pure-tensor maps
$$E\otimes_SS'\longrightarrow E\otimes_RR',
\quad e\otimes(s\otimes r')\longmapsto se\otimes r',
\qquad e\otimes r'\longmapsto e\otimes(1\otimes r')$$
are inverse. They give the other tensor description of the conormal term.

The polynomial differential term is free on the same $dx_a$ over $S$ and over $S'$. Differentiating a polynomial commutes with changing its coefficients, since every monomial derivative multiplies by the same integer exponent and lowers the same variable degree. Thus both differentials agree on every relation class, proving the complex isomorphism. Each polynomial has finite support, so no finite-variable assumption enters.

Apply [F.11](#algebra-lemma-NL-homotopy) to compare each presentation with the canonical one. Tensoring its explicit homotopy identities with $S'$ preserves those identities. The complex isomorphism just proved, between these comparison homotopy equivalences, therefore identifies the displayed canonical map up to homotopy and supplies its inverse up to homotopy. This proves the final assertion without assuming that $S$ is flat over $R$. ∎

<a id="algebra-lemma-characterize-etale"></a>

#### Lemma F.16: characterize etale

Reading source: [AI Integrated Stacks, pinned Algebra, lines 40942–40975](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L40942-L40975).

Let $\mathfrak q\in\operatorname{Spec}S$ lie over $\mathfrak p\in\operatorname{Spec}R$. The map $R\to S$ is étale at $\mathfrak q$ if the following four hypotheses hold: it is finitely presented; $R_{\mathfrak p}\to S_{\mathfrak q}$ is flat; the ideal $\mathfrak pS_{\mathfrak q}$ is the maximal ideal of $S_{\mathfrak q}$; and $\kappa(\mathfrak q)/\kappa(\mathfrak p)$ is finite separable.

**Proof.** Write $k=\kappa(\mathfrak p)$ and $L=\kappa(\mathfrak q)$. The stipulated maximal-ideal equality identifies the local fibre ring with the field $L$. Since $L/k$ is finite, the complete isolated-fibre argument [F.56](#algebra-lemma-isolated-point-fibre) supplies a principal neighbourhood of $\mathfrak q$ having no other point in this fibre. Its finite presentation is preserved by [F.35](#algebra-lemma-cover-upstairs). On this neighbourhood the fibre algebra $B=S\otimes_Rk$ has exactly one prime. It is local: every nonunit lies in a maximal ideal, and there is only one such ideal. Therefore its localization at that prime is $B$ itself. This localization is the given local fibre $L$, so $B=L$.

We prove directly the smoothness and differential vanishing of this finite separable field fibre. A finite $k$-basis generates $L$ as a field; adjoining its entries gives a finite tower $k=E_0\subset E_1\subset\cdots\subset E_t=L$, with $E_i=E_{i-1}(\alpha_i)$. Let $p_i(T)$ be the monic minimal polynomial of $\alpha_i$ over $E_{i-1}$. The complete monic-division and Bezout arguments [AG-RG-S02, Lemma 4.A](AG-RG-S02.md) give $E_i=E_{i-1}[T]/(p_i)$. Each $p_i$ divides the separable minimal polynomial of $\alpha_i$ over $k$, now regarded over $E_{i-1}$, so $p_i'(\alpha_i)\ne0$.

Choose polynomial representatives in the preceding variables for all coefficients of $p_i$, obtaining $P_i(T_1,\ldots,T_i)$. Successive monic division gives
$$L=k[T_1,\ldots,T_t]/(P_1,\ldots,P_t).$$
The Jacobian over $L$ is triangular with diagonal $p_i'(\alpha_i)$, so is invertible. The equation classes give a surjection $L^t\to I/I^2$, where $I=(P_1,\ldots,P_t)$, and its composite with the conormal differential to $L^t$ is this invertible Jacobian. The surjection must also be injective, and the conormal differential is an isomorphism. Hence its kernel and cokernel vanish. [Definition F.6](#algebra-definition-smooth) and presentation comparison give smoothness of $L/k$ and $\Omega_{L/k}=0$. For $L=k$, use the empty tower and the two zero modules.

The local flatness hypothesis and the finite presentation now meet every condition of [F.45](#algebra-lemma-flat-fibre-smooth), giving a smooth principal neighbourhood of $\mathfrak q$. The complete arbitrary-base chart result [F.83](#algebra-lemma-smooth-syntomic) gives a further neighbourhood with a standard smooth presentation
$$S=R[X_1,\ldots,X_n]/(f_1,\ldots,f_c).$$
Every inverted element has nonzero residue in $L$, so the fibre remains exactly $L$. By [F.85(2)](#algebra-lemma-standard-smooth), the differential module is free on $dX_{c+1},\ldots,dX_n$. The full differential scalar-extension calculation AG-CA-15, Theorem 2.1, identifies its fibre with $\Omega_{L/k}=0$. Thus $L^{n-c}=0$, forcing $n=c$.

We check the lifting definition of étaleness on this final chart. Given a map to $D/J$ with $J^2=0$, lift its variable tuple to $a\in D^n$. The error vector $f(a)$ lies in $J^n$. The square Jacobian $A(a)$ is invertible: its determinant is a unit modulo $J$, a lift of an inverse gives a product $1+j$ with inverse $1-j$, and the adjugate identity [F.70](#algebra-lemma-matrix-left-inverse) gives the matrix inverse. Take
$$b=a-A(a)^{-1}f(a).$$
Expanding each monomial and dropping terms with two entries from $J$ gives $f(b)=f(a)+A(a)(b-a)=0$. Thus $b$ defines a lift. A second lifting root has the form $b+\epsilon$ for $\epsilon\in J^n$. The same expansion gives $A(b)\epsilon=0$, and $A(b)$ is invertible by its unchanged reduction modulo $J$, so $\epsilon=0$. Every square-zero test therefore has exactly one lift. With finite presentation this is étaleness by the programme definition. The chart contains $\mathfrak q$, proving the claim for the original map. Empty variable lists use the unique empty tuple and determinant $1$; no Noetherian or perfect-field hypothesis was introduced. ∎

<a id="algebra-lemma-characterize-formally-smooth-field-extension"></a>

#### Lemma F.17: characterize formally smooth field extension

Reading source: [AI Integrated Stacks, pinned Algebra, lines 45959–45969](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L45959-L45969).

For any field extension $K/k$, the vanishing of $H_1(\operatorname{NL}_{K/k})$ is equivalent to formal smoothness of $K$ as a $k$-algebra.

**Proof.** Choose a polynomial surjection $P=k[X_a\mid a\in E]\to K$, allowing an infinite set $E$, with kernel $I$. By [F.11](#algebra-lemma-NL-homotopy), the homology in question is the kernel of
$$d:I/I^2\longrightarrow\Omega_{P/k}\otimes_PK.$$
Its cokernel is $\Omega_{K/k}$, by the conormal calculation. When this kernel is zero, the sequence with these three modules is short exact. A vector-space basis of $\Omega_{K/k}$ can be lifted to the middle module. Extending those lifts $K$-linearly splits the surjection, and hence the sequence.

The entire arbitrary-variable criterion AG-CA-17, Theorem 3.1, proves that this split conormal sequence is equivalent to formal smoothness. Its hypotheses apply to the chosen polynomial presentation over $k$ with target $K$ and impose no finite generation. Conversely, formal smoothness gives a split exact conormal sequence by that same complete theorem, so its left map has zero kernel. F.11 identifies that kernel with the presentation-independent first cotangent homology, also denoted $H_1(L_{K/k})$ in the reading source. This proves both directions for arbitrary field extensions. ∎

<a id="algebra-lemma-characterize-smooth-kbar"></a>

#### Lemma F.18: characterize smooth kbar

Reading sources: [Stacks, Tag 00TS](https://stacks.math.columbia.edu/tag/00TS); [AI Integrated Stacks, pinned Algebra, lines 39962–40064](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L39962-L40064).

Let $S$ be a finite-type algebra over an algebraically closed field $k$, and let $\mathfrak m$ be a maximal ideal. Write
$$d=\dim S_{\mathfrak m},\qquad
e=\dim_{\kappa(\mathfrak m)}
\bigl(\Omega_{S/k}\otimes_S\kappa(\mathfrak m)\bigr).$$
The following four conditions are equivalent: $S_{\mathfrak m}$ is regular local; $e\leq d$; $e=d$; and some $g\in S\setminus\mathfrak m$ has $S_g/k$ smooth.

**Proof.** The complete rational-point result AG-CA-18, Proposition 3.1, gives $\kappa(\mathfrak m)=k$ and
$$\Omega_{S/k}\otimes_Sk\cong\mathfrak m/\mathfrak m^2.$$
The embedding-dimension theorem of AG-CA-14, Section 1, says $d\leq\dim_k\mathfrak m/\mathfrak m^2$, with equality exactly for regularity. Thus the first three conditions are equivalent. The same complete AG-CA-18 proposition proves that smoothness at this closed rational point implies regularity, giving the implication from the fourth to the first.

For the converse we construct a smooth chart and identify its entire relation ideal. Suppose $S_{\mathfrak m}$ is regular. Choose a finite polynomial presentation $S=k[x_1,\ldots,x_n]/I$, shifting each generator by its residue so that the preimage of $\mathfrak m$ is $\mathfrak n=(x_1,\ldots,x_n)$. The exact conormal sequence at this point is
$$I/\mathfrak nI\longrightarrow\mathfrak n/\mathfrak n^2
\longrightarrow\mathfrak m/\mathfrak m^2\longrightarrow0.$$
Since the middle dimension is $n$ and the last is $d$, select $c=n-d$ elements $f_1,\ldots,f_c\in I$ whose linear classes form a basis of the kernel. Put $J=(f_1,\ldots,f_c)$ and $T=k[x]/J$, with maximal ideal $\mathfrak m'=\mathfrak n/J$. The corresponding conormal sequence shows that the cotangent space of $T_{\mathfrak m'}$ has dimension $d$. This local ring surjects onto $S_{\mathfrak m}$, so its dimension is at least $d$; its embedding dimension bounds it above by $d$. It is therefore regular of dimension $d$.

By AG-CA-14, Theorem 1.1, $T_{\mathfrak m'}$ is a domain. The surjection to $S_{\mathfrak m}$ has zero kernel. To prove this, a nonzero kernel would put every lifted quotient prime strictly above $(0)$. A prime chain of length $d$ in the quotient exists because its dimension is the finite integer $d$. Prepending $(0)$ to the lifted chain would give length $d+1$ in $T_{\mathfrak m'}$, a contradiction. Thus the local surjection is an isomorphism.

The independent linear coefficient rows of the $f_i$ have a nonzero $c$-variable Jacobian minor $\Delta$ at this point. Existence of such a minor follows from the explicit pivot induction in [D.2](#smoothing-lemma-find-strictly-standard); for $c=0$ take $\Delta=1$. Reorder the pivot variables first. The presentation
$$T_\Delta=k[x_1,\ldots,x_n,u]/(f_1,\ldots,f_c,u\Delta-1)$$
has a selected Jacobian determinant $\Delta^2$: the last column is zero in the first $c$ rows, its last entry is $\Delta$, and the first square block has determinant $\Delta$. This determinant is a unit in the quotient. The complete principal-localization standard-smooth calculation [F.85](#algebra-lemma-standard-smooth) therefore proves $T_\Delta/k$ smooth.

It remains to pass from $T$ to $S$. The kernel of $T\to S$ is finite since $T$ is Noetherian, and becomes zero at $\mathfrak m'$ by the local isomorphism. For each of its finite generators take a localization annihilator outside $\mathfrak m'$. Their product $a$ still avoids $\mathfrak m'$ and kills the entire kernel. Exact localization of the surjection then gives $T_a\cong S_{\bar a}$, hence
$$T_{a\Delta}\cong S_{\overline{a\Delta}}.$$
The left side is a principal localization of the smooth algebra $T_\Delta$, and F.85(4) supplies its smooth presentation. On the right $g=\overline{a\Delta}$ avoids $\mathfrak m$. This gives the fourth condition, with the exact kernel eliminated on the whole neighbourhood. Empty equation lists obey the same construction. The algebraically closed ground-field assumption is retained throughout. ∎

<a id="algebra-lemma-charpoly"></a>

#### Lemma F.19: charpoly

Reading source: [Stacks, Tag 00DX](https://stacks.math.columbia.edu/tag/00DX).

For a square matrix \(M\) of size \(n\) over any commutative ring \(R\), let \(P(T)=\det(T1_n-M)\). Then \(P(M)=0\) as an endomorphism of \(R^n\).

**Proof.** Define determinants by the signed permutation formula. Grouping its terms according to the entry in a fixed row gives the cofactor expansion. If that row is replaced by another row, the same expansion is zero: permutations pair with the transposition of the two equal rows, and the paired terms have opposite signs. The column calculation is identical. Thus, for every square matrix \(C\), the transpose of its signed cofactor matrix, denoted \(\operatorname{adj}(C)\), satisfies
\[
C\operatorname{adj}(C)=\operatorname{adj}(C)C=(\det C)1_n.
\]
This argument uses addition and multiplication only, so it applies over \(R[T]\) as well.

Assume \(n>0\), write
\[
\operatorname{adj}(T1_n-M)=\sum_{j=0}^{n-1}C_jT^j,
\qquad P(T)=\sum_{j=0}^n p_jT^j,\quad p_n=1.
\]
The degree bound follows because each cofactor is a determinant of size \(n-1\). Comparing coefficients in the first adjugate identity gives
\[
-MC_0=p_0 1_n,\qquad
C_{j-1}-MC_j=p_j1_n\ (1\leq j<n),\qquad C_{n-1}=1_n.
\]
Multiply the equation indexed by \(j\) on the left by \(M^j\), the constant equation by \(1_n\), and the last equation by \(M^n\). Adding them cancels every \(M^{j+1}C_j\) against its next occurrence. The result is \(\sum_{j=0}^n p_jM^j=0\). No substitution into a polynomial with noncommuting matrix coefficients, and no division, is involved. If \(n=0\), the empty determinant gives \(P=1\); its value is the identity of the zero module, which is the zero endomorphism. ∎

<a id="algebra-lemma-codimension"></a>

#### Lemma F.20: codimension

Reading source: [AI Integrated Stacks, pinned Algebra, lines 29578–29596](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L29578-L29596).

Let $S'\twoheadrightarrow S$ be a surjection of finite-type algebras over a field $k$. For a prime $\mathfrak p\subset S$, let $\mathfrak p'\subset S'$ be its inverse image, and let $x,x'$ denote the corresponding points. Then
$$\dim_{x'}\operatorname{Spec}S'-\dim_x\operatorname{Spec}S
=\operatorname{ht}_{S'}\mathfrak p'-\operatorname{ht}_S\mathfrak p.$$

**Proof.** The induced map $S'/\mathfrak p'\to S/\mathfrak p$ is an isomorphism: surjectivity descends, and the definition of $\mathfrak p'$ makes its kernel zero. Its fraction-field map therefore identifies $\kappa(\mathfrak p')$ with $\kappa(\mathfrak p)$ as extensions of $k$. Call their common transcendence degree $e$.

The complete point-dimension argument AG-CA-09, Theorem 6.1, applies separately to the two finite-type algebras and gives
$$\dim_{x'}\operatorname{Spec}S'=\dim S'_{\mathfrak p'}+e,\qquad
\dim_x\operatorname{Spec}S=\dim S_{\mathfrak p}+e.$$
Here point dimension is the minimum of the dimensions of open neighbourhoods. Localization identifies chains of primes in $S'_{\mathfrak p'}$ with chains in $S'$ ending below $\mathfrak p'$; taking their supremum gives $\dim S'_{\mathfrak p'}=\operatorname{ht}_{S'}\mathfrak p'$. The same chain correspondence gives $\dim S_{\mathfrak p}=\operatorname{ht}_S\mathfrak p$. All dimensions are finite by that earlier finite-type theorem. Subtract the two displayed equalities; the identical terms $e$ cancel and give the assertion. No equidimensionality assumption is needed. ∎

<a id="algebra-lemma-colimit-eventually-flat"></a>

#### Lemma F.21: colimit eventually flat

Reading source: [AI Integrated Stacks, pinned Algebra, lines 34105–34145](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L34105-L34145).

Consider a directed system of local maps $R_\lambda\to S_\lambda$ between Noetherian local rings, with local transition maps, and let $R=\operatorname*{colim}_\lambda R_\lambda$ and $S=\operatorname*{colim}_\lambda S_\lambda$. Suppose that for $\mu\geq\lambda$, $S_\mu$ is the specified localization of $S_\lambda\otimes_{R_\lambda}R_\mu$. Let $M_\lambda$ be finite $S_\lambda$-modules with $M_\mu=M_\lambda\otimes_{S_\lambda}S_\mu$, and put $M=\operatorname*{colim}_\lambda M_\lambda$. These are exactly the kinds of models supplied by [F.59](#algebra-lemma-limit-essentially-finite-presentation) and [F.60](#algebra-lemma-limit-module-essentially-finite-presentation). If $M$ is $R$-flat, then $M_\mu$ is $R_\mu$-flat at some stage.

**Proof.** Fix $\lambda$, write $\mathfrak m=\mathfrak m_\lambda$, and form
$$T=\operatorname{Tor}_1^{R_\lambda}(M_\lambda,R_\lambda/\mathfrak m)
=\ker\bigl(\mathfrak m\otimes_{R_\lambda}M_\lambda\longrightarrow M_\lambda\bigr).$$
The free-resolution and ideal-kernel calculation is AG-RG-S01, Lemma 1.A. The ideal $\mathfrak m$ is finite over $R_\lambda$, so its tensor with the finite $S_\lambda$-module $M_\lambda$ is finite over $S_\lambda$. Since $S_\lambda$ is Noetherian, its kernel $T$ is finite as well. Choose generators $\xi_1,\ldots,\xi_a$ over $S_\lambda$.

For $\nu\geq\lambda$, put $I_\nu=\mathfrak mR_\nu$. The transition of each $\xi_i$ lies in
$$\ker(I_\nu\otimes_{R_\nu}M_\nu\longrightarrow M_\nu)
=\operatorname{Tor}_1^{R_\nu}(M_\nu,R_\nu/I_\nu).$$
The colimit of the ideals $I_\nu$ is $\mathfrak mR$: a finite sum of images of generators has a representative at a common stage, and equality of two representatives holds at a later stage. The same finite sums and the finitely many tensor relations show
$$\operatorname*{colim}_{\nu\geq\lambda}
(I_\nu\otimes_{R_\nu}M_\nu)
\cong(\mathfrak mR)\otimes_R M.$$
Multiplication from the last module into $M$ is injective, because tensoring the inclusion $\mathfrak mR\subset R$ with the flat module $M$ preserves injectivity. Each $\xi_i$ consequently has zero image in this colimit. The definition of a directed colimit says that its representative is already zero at some later stage. Choose a common successor $\mu$ for these finitely many witnesses. The entire natural map
$$T\longrightarrow\operatorname{Tor}_1^{R_\mu}(M_\mu,R_\mu/\mathfrak mR_\mu)$$
is now zero, since it is compatible with the scalar map $S_\lambda\to S_\mu$ and kills every chosen generator.

Apply the full local-square criterion [F.13](#algebra-lemma-another-variant-local-criterion-flatness) to $(R_\lambda,S_\lambda,R_\mu,S_\mu)$ and $I=\mathfrak m$. This ideal is proper and its extension is proper because $R_\lambda\to R_\mu$ is local. The module $M_\lambda/\mathfrak mM_\lambda$ is flat over the field $R_\lambda/\mathfrak m$: any vector-space basis expresses it as a free module, without a finite-dimensional assumption. The localized tensor description and finite $S_\lambda$-module hypothesis are exactly those stipulated above. The zero Tor map just proved supplies the last hypothesis of F.13, giving $R_\mu$-flatness of $M_\mu$. ∎

<a id="algebra-lemma-colimit-formally-etale"></a>

#### Lemma F.22: colimit formally etale

Reading source: [AI Integrated Stacks, pinned Algebra, lines 42732–42747](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L42732-L42747).

Let $(S_i)$ be a filtered system of formally étale $R$-algebras. Then $\operatorname*{colim}_iS_i$ is formally étale over $R$.

**Proof.** Set $S=\operatorname*{colim}_iS_i$. Test the formal lifting property on an $R$-algebra $A$, an ideal $J\subset A$ with $J^2=0$, and an $R$-map $u:S\to A/J$. The restriction $u_i:S_i\to A/J$ has exactly one lifting $v_i:S_i\to A$, by the assumed formal étaleness.

If $\phi_{ij}:S_i\to S_j$ is a transition map, then $v_j\phi_{ij}$ and $v_i$ both lift $u_i$. Uniqueness on $S_i$ forces $v_j\phi_{ij}=v_i$. The colimit universal property therefore gives a map $v:S\to A$ whose restrictions are all $v_i$. Its reduction agrees with $u$ on every stage and hence on $S$. If $v'$ is another lifting, its restriction to each $S_i$ equals $v_i$, so the same universal property gives $v'=v$.

For a general nilpotent ideal $J$ with $J^N=0$, apply the square-zero test successively to $A/J^{n+1}\to A/J^n$ for $1\leq n<N$. Its kernel $J^n/J^{n+1}$ has square zero because $2n\geq n+1$. Each lifting step exists uniquely; induction reaches $A$ and also proves uniqueness there. Thus either formulation of the formal étale test holds. No finite-presentation condition on any stage or on the colimit enters the proof. ∎

<a id="algebra-lemma-colimit-syntomic"></a>

#### Lemma F.23: colimit syntomic

Reading source: [AI Integrated Stacks, pinned Algebra, lines 46090–46123](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L46090-L46123).

Every extension of fields $K/k$ is a filtered union of $k$-subalgebras that are global complete intersections. If $K/k$ is separable, it is a filtered union of smooth $k$-subalgebras.

**Proof.** We first place an arbitrary finite set $E\subset K$ in one of the asserted complete intersections. The subfield $L=k(E)$ has a finite transcendence basis $t_1,\ldots,t_d$ and is finite over $F=k(t_1,\ldots,t_d)$. Choose a finite tower
$$F=L_0\subset L_1\subset\cdots\subset L_r=L,\qquad L_i=L_{i-1}(y_i).$$
Write $e_i$ for the degree of the monic minimal polynomial of $y_i$ over $L_{i-1}$. Successive monic division, proved in AG-RG-S02, Lemma 4.A, makes the products $\prod_{j<i}y_j^{a_j}$ with $0\leq a_j<e_j$ an $F$-basis of $L_{i-1}$. Expand each coefficient of the minimal polynomial in this basis. Its basis coefficients belong to $F$; finitely many rational-function denominators occur.

Choose one nonzero $h\in k[t_1,\ldots,t_d]$ clearing these denominators, and put $B=k[t_1,\ldots,t_d,1/h]$. The expansions give monic polynomials
$$P_i\in B[Y_1,\ldots,Y_i],\qquad
C=B[Y_1,\ldots,Y_r]/(P_1,\ldots,P_r).$$
At each successive quotient monic division gives a free module on $1,Y_i,\ldots,Y_i^{e_i-1}$. Hence $C$ is finite free over $B$ on the corresponding product monomials. Multiplication by a monic polynomial in a polynomial ring is injective even over a ring with zero divisors: in a nonzero product, the leading coefficient of the other factor survives unchanged as the leading coefficient. Applying this fact at each stage proves that the displayed equation list is a regular sequence.

After tensoring with $F$, these same quotients are the chosen minimal-polynomial tower, so $C\otimes_BF=L$. Freeness over the domain $B$ makes the map $C\to C\otimes_BF$ injective: a nonzero element of $B$ cannot kill a nonzero coordinate in a free basis. We may thus regard $C$ as a subalgebra of $L$. Expand the finitely many elements of $E$ in its product basis over $F$, and enlarge $h$ to clear their coefficients as well. The construction with this enlarged $B$ then contains $E$.

The coefficient ring $B$ has dimension $d$ by the finite-type-domain dimension theorem AG-CA-09, Theorem 4.2; its fraction field is $F$. The finite injective integral map $B\to C$ preserves dimension by AG-CA-05, Theorem 5.1. Encoding $1/h$ by a variable $Z$ gives
$$C\cong k[t_1,\ldots,t_d,Y_1,\ldots,Y_r,Z]/
(P_1,\ldots,P_r,hZ-1),$$
where the coefficients of the $P_i$ are polynomial representatives modulo $hZ-1$. This presentation has $d+r+1$ variables, $r+1$ equations, and dimension $d$, so it satisfies the global complete-intersection definition [F.4](#algebra-definition-relative-global-complete-intersection) over $k$.

If the extension is separable, [F.5](#algebra-definition-separable-field-extension) makes the finitely generated subfield $L$ separably generated. The entire forward construction in [F.64](#algebra-lemma-localization-smooth-separable) supplies a smooth finite-type domain $D\subset L$ with fraction field $L$. For every element of $E$ choose a numerator and a nonzero denominator in $D$. Localizing at their finite product gives a smooth algebra containing $E$, by the principal-localization calculation [F.85](#algebra-lemma-standard-smooth).

Finally, in either case two constructed subalgebras have finite sets of algebra generators over $k$. Apply the corresponding construction to the union of those generator sets. The resulting subalgebra contains both, proving directedness under inclusion. Applying the construction to a singleton includes each element of $K$. The union, and thus its filtered colimit, is exactly $K$. Empty towers and transcendence bases use the same argument with their empty products equal to one. ∎

<a id="algebra-lemma-colimits-NL"></a>

#### Lemma F.24: colimits NL

Reading source: [AI Integrated Stacks, pinned Algebra, lines 36983–36999](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L36983-L36999).

For a filtered system of ring maps $R_\lambda\to S_\lambda$, put $R=\operatorname*{colim}R_\lambda$ and $S=\operatorname*{colim}S_\lambda$. The canonical two-term conormal complexes satisfy
$$\operatorname{NL}_{S/R}\cong
\operatorname*{colim}_\lambda\operatorname{NL}_{S_\lambda/R_\lambda}.$$

**Proof.** Use the canonical presentation $P_\lambda=R_\lambda[X_s\mid s\in S_\lambda]\twoheadrightarrow S_\lambda$, with kernel $I_\lambda$. A transition sends coefficients along the base map and sends $X_s$ to the variable named by the image of $s$. Thus distinct variables may become equal; injective transition maps are not assumed. Let $P=R[X_s\mid s\in S]$ and $I=\ker(P\to S)$.

Every element of $P$ uses finitely many coefficients, variables and monomials. They all have representatives at one common stage, giving surjectivity of $\operatorname*{colim}P_\lambda\to P$. If a representative polynomial is zero in $P$, the finitely many identifications among its variable labels and the finitely many coefficient equalities hold at a common later stage. The representative is zero there. This proves injectivity and identifies the two polynomial rings.

A representative polynomial belongs to $I$ precisely when its evaluation becomes zero in $S$. That one finite equality holds at a later stage, so the polynomial can then be represented in $I_\mu$. If an element of $I_\lambda$ becomes zero in $I\subset P$, it is zero at a later polynomial stage, and hence at a later ideal stage. Therefore $I=\operatorname*{colim}I_\lambda$. An element of $I^2$ is a finite sum of products of two elements of $I$. Choose a common stage for all those factors and their kernel equalities; their products lie in $I_\mu^2$. Vanishing is again detected in a later polynomial ring. This proves $I^2=\operatorname*{colim}I_\lambda^2$.

Filtered colimits of the relevant modules preserve short exact sequences. Indeed, if a left representative maps to zero in the middle colimit, it is zero in the middle at a later stage, where injectivity makes it zero on the left. If a middle representative maps to zero on the right, at a later stage exactness expresses it as an image from the left. A right representative has a middle preimage at its own stage. These arguments also work for modules over the varying rings: the actions of the colimit rings are defined using common representatives. Applying them to $I_\lambda^2\subset I_\lambda$ gives
$$I/I^2\cong\operatorname*{colim}_\lambda I_\lambda/I_\lambda^2.$$

The degree-zero term is $\bigoplus_{s\in S}S\,dX_s$. Its vectors have finite support; a common-stage argument for their coefficients and labels, with later-stage detection of zero, identifies it with the colimit of $\bigoplus_{s\in S_\lambda}S_\lambda\,dX_s$. Formal differentiation of a polynomial is a finite coefficient calculation and respects every transition, including variable identifications. Consequently the two module identifications intertwine the maps $[f]\mapsto df$. They give the asserted isomorphism of entire two-term complexes. ∎

<a id="algebra-lemma-complete-local-Noetherian-domain-finite-over-regular"></a>

#### Lemma F.25: complete local Noetherian domain finite over regular

Reading source: [AI Integrated Stacks, pinned Algebra, lines 46654–46712](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L46654-L46712).

Every complete Noetherian local domain $A$ contains a regular complete local subring $A_0$ such that $A$ is finite over $A_0$ and the residue fields agree. The subring can be chosen as a power-series ring over a field or over a Cohen ring.

**Proof.** Write $\mathfrak m$ for the maximal ideal and $D=\dim A$. The complete coefficient-ring construction is AG-CA-19S, Theorem 5.1. Its arbitrary-residue-field step uses [F.119](#more-algebra-lemma-p-basis), including the full degree-$p$ argument: $T^p-a^p=(T-a)^p$, and the coefficient $-da$ of a proper monic factor, with $1\leq d<p$, forces the claimed degree. Thus this construction applies without a perfect-residue-field assumption.

In equal characteristic it embeds a coefficient field $k\subset A$. Choose a system of $D$ parameters $x_1,\ldots,x_D$ by AG-CA-11, Theorem 2.1. In mixed characteristic the coefficient ring is a Cohen DVR $C$ with uniformizer $p$ and residue field $k$. It embeds in $A$: a nonzero kernel ideal in this DVR would contain a power of $p$, whereas the domain $A$ has characteristic zero. The element $p$ is consequently a nonzerodivisor in $A$, and AG-CA-11, Theorem 3.2, gives $\dim A/pA=D-1$. Choose parameters $x_1,\ldots,x_{D-1}$ in that quotient and lift them to $A$.

In the respective cases put
$$B=k[[X_1,\ldots,X_D]]
\quad\hbox{or}\quad
B=C[[X_1,\ldots,X_{D-1}]],$$
and let $\mathfrak n$ be its maximal ideal. The ideal $I$ generated by the proposed images of $\mathfrak n$ is $(x_1,\ldots,x_D)$ or $(p,x_1,\ldots,x_{D-1})$. The parameter property gives $\sqrt I=\mathfrak m$. AG-CA-03, Proposition 2.2, supplies an integer $b$ with $\mathfrak m^b\subset I$, while $I\subset\mathfrak m$. Hence
$$\mathfrak m^{bn}\subset I^n\subset\mathfrak m^n\qquad(n\geq1).$$
The two filtrations are cofinal. Completeness and separatedness of $A$ for its maximal-ideal filtration therefore imply the same properties for its $I$-adic filtration. Evaluation $X_i\mapsto x_i$ defines a ring map $B\to A$: the tail of a power series of degree at least $n$ evaluates into $I^n$, and finite truncation followed by a separated limit respects addition and multiplication. This is the evaluation calculation of AG-CA-19S, Theorem 6.1.

The local quotient $A/I$ has nilpotent maximal ideal and residue field $k$. Each maximal-ideal layer is finite-dimensional over $k$, since $\mathfrak m$ is finite and its powers are generated by finitely many products. The finite-layer proof in AG-CA-03, Theorem 4.2, therefore makes $A/I$ finite-dimensional. Choose elements $a_1,\ldots,a_s\in A$ lifting a $k$-basis of this quotient.

These elements generate $A$ over $B$. To verify this directly, approximate any $a\in A$ modulo $I$ by $\sum_jc_{j1}a_j$ with coefficients lifted from $k$ to $B$. If coefficients have been chosen through order $n$, the error lies in $I^n$. Express it as a finite sum of degree-$n$ products of the generators of $I$ times elements of $A$. Replace each latter element modulo $I$ by its residue-basis expansion. Lifting those coefficients to $B$ gives corrections in $\mathfrak n^n$ and leaves an error in $I^{n+1}$. Induction constructs compatible coefficients $c_{jn}$ modulo $\mathfrak n^n$. The complete ring $B$ supplies limits $c_j$; continuity of evaluation and $I$-adic separatedness give $a=\sum_jc_ja_j$. Thus $A$ is a finite $B$-module.

The ring $B$ is the maximal-ideal completion of the polynomial local ring over $k$ or $C$: their quotients by each maximal-ideal power have the same finite polynomial truncations, including the coefficient reductions modulo powers of $p$ in the second case. AG-CA-14, Proposition 3.3, proves regularity of that polynomial local ring, and AG-CA-11, Theorem 5.1, gives its dimension $D$. Completion preserves this dimension and regularity by AG-CA-19, Theorem 4.1. Hence $B$ is a regular local domain of dimension $D$.

Let $J$ be the evaluation kernel. If it contains a nonzero element $f$, the one-equation theorem AG-CA-11, Theorem 3.2, gives $\dim B/(f)=D-1$, and the further quotient $B/J$ has dimension at most $D-1$. But $B/J$ embeds in the finite integral extension $A$, so AG-CA-05, Theorem 5.1, gives $\dim B/J=\dim A=D$, a contradiction. Therefore $J=0$. Take $A_0$ to be the resulting embedded copy of $B$. Its residue map is the coefficient identification with $k$, and the finiteness has already been proved. If $D=0$, the Noetherian local domain is its own residue field, so $A_0=A$ gives the empty-variable case directly. ∎

<a id="algebra-lemma-completion-at-quasi-finite-prime"></a>

#### Lemma F.26: completion at quasi finite prime

Reading source: [AI Integrated Stacks, pinned Algebra, lines 32412–32464](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L32412-L32464).

Let $R$ be Noetherian, let $R\to S$ be finite type, and let $\mathfrak q\subset S$ be quasi-finite over $\mathfrak p=\mathfrak q\cap R$. There is an algebra $D$ with
$$\widehat{R_{\mathfrak p}}\otimes_RS
\cong\widehat{S_{\mathfrak q}}\times D,$$
whose first projection is the natural map to the completed local ring.

**Proof.** The full affine conductor theorem [Zariski Main, Theorem C4.3](AG-RG-S04.md) produces an integral subalgebra $C\subset S$ and $g\in C\setminus\mathfrak q$ such that $C_g=S_g$. Choose a finite set of $R$-algebra generators of $S_g$. Each is a fraction with numerator in $C$ and denominator a power of $g$. Let $S'\subset C$ be generated over $R$ by those numerators and by $g$. All these generators are integral. Repeated monic reduction, as in AG-CA-05, Section 1, shows that their bounded product powers generate $S'$ as an $R$-module. Thus $S'$ is finite over $R$, and the chosen generators give $S'_g=S_g$.

Put $\mathfrak q'=\mathfrak q\cap S'$. Localizing the last equality at the corresponding primes gives $S'_{\mathfrak q'}=S_{\mathfrak q}$, including their maximal ideals, so their maximal-adic completions are naturally identified. By [F.27](#algebra-lemma-completion-finite-extension),
$$T'=\widehat{R_{\mathfrak p}}\otimes_RS'
\cong A\times D',\qquad A=\widehat{S_{\mathfrak q}}.$$
Let $e\in T'$ be the idempotent $(1,0)$. Its image in $T=\widehat{R_{\mathfrak p}}\otimes_RS$ gives an explicit product map
$$T\longrightarrow eT\times(1-e)T,\qquad t\longmapsto(et,(1-e)t),$$
with inverse addition. The structural map $A=eT'\to eT$ is unital. The image of $g$ in $A$ is a unit because $g\notin\mathfrak q'$, and remains a unit in $eT$.

Localizing $T'\to T$ at $g$ gives an isomorphism, by $S'_g=S_g$ and the tensor/localization universal properties. Its $e$-factor is
$$A=A_g\xrightarrow{\ \sim\ }(eT)_g=eT.$$
This identifies the first factor with the required completion, and the second is $D=(1-e)T$.

It remains to determine the projection on all of $T$. On $\widehat{R_{\mathfrak p}}$ and $S'$ it agrees with the completed-local structural maps by the construction in F.27. Given $s\in S$, the equality $S'_g=S_g$ writes $s/1=b/g^n$ with $b\in S'$. Equality of these fractions means that some $g^a$ kills $g^ns-b$ in $S$. Therefore $g^{n+a}s=g^ab\in S'$. Both the factor projection and the natural map $S\to\widehat{S_{\mathfrak q}}$ have the same value on this element and on the unit $g$. Multiplying by the inverse of $g^{n+a}$ makes their values on $s$ equal. The values on all pure tensors are now equal, proving the assertion about the first projection. ∎

<a id="algebra-lemma-completion-finite-extension"></a>

#### Lemma F.27: completion finite extension

Reading source: [AI Integrated Stacks, pinned Algebra, lines 24144–24184](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L24144-L24184).

For a finite map of Noetherian rings $R\to S$ and a prime $\mathfrak p\subset R$, let $\mathfrak q_1,\ldots,\mathfrak q_r$ be all primes of $S$ above $\mathfrak p$. Then
$$\widehat{R_{\mathfrak p}}\otimes_RS
\cong\prod_{i=1}^r\widehat{S_{\mathfrak q_i}},$$
where each local ring is completed at its own maximal ideal.

**Proof.** Replace the base by $R_{\mathfrak p}$ and the finite algebra by $S_{\mathfrak p}$; tensor associativity gives the same left side, and localizing at each prime gives the same right side. Write $\mathfrak m$ for the resulting base maximal ideal. The integral lying-over and maximal-ideal results AG-CA-05, Theorems 3.3–3.4, show that the maximal ideals of this finite algebra are precisely the finitely many $\mathfrak q_i$, and all contract to $\mathfrak m$.

For $n\geq1$, the ring $R/\mathfrak m^n$ has a finite filtration whose successive quotients are finite-dimensional over the residue field: each $\mathfrak m^j/\mathfrak m^{j+1}$ is generated by finitely many products of generators of $\mathfrak m$. It is therefore Artinian. The finite module $S/\mathfrak m^nS$ has finite length over this ring, by the finite-module argument AG-CA-03, Theorem 3.3, and consequently is itself Artinian. Its primes are the images of the $\mathfrak q_i$: every prime over $\mathfrak m^n$ contracts to $\mathfrak m$ and is maximal by integrality.

The entire Artinian product theorem AG-CA-03, Theorem 4.2, now gives the canonical localization decomposition
$$S/\mathfrak m^nS
\cong\prod_{i=1}^r S_{\mathfrak q_i}/\mathfrak m^nS_{\mathfrak q_i}.$$
These maps commute with reduction from order $n+1$ to order $n$, because every projection is the corresponding localization map. Inverse limits of a finite product are computed componentwise: a compatible tuple sequence is exactly a tuple of compatible sequences. Hence the $\mathfrak mS$-adic completion of $S$ is
$$\varprojlim_n S/\mathfrak m^nS
\cong\prod_i\varprojlim_n
S_{\mathfrak q_i}/\mathfrak m^nS_{\mathfrak q_i}.$$

In the $i$th local ring the radical of $\mathfrak mS_{\mathfrak q_i}$ is its maximal ideal $\mathfrak q_iS_{\mathfrak q_i}$: a prime containing the former corresponds to a prime above $\mathfrak m$, and localization leaves only $\mathfrak q_i$. AG-CA-03, Proposition 2.2, supplies $b_i$ such that
$$(\mathfrak q_iS_{\mathfrak q_i})^{b_in}
\subset\mathfrak m^nS_{\mathfrak q_i}
\subset(\mathfrak q_iS_{\mathfrak q_i})^n.$$
These cofinal filtrations have canonically identical completions. The right-hand limits are thus $\widehat{S_{\mathfrak q_i}}$. Finally AG-CA-19, Theorem 3.1, identifies the left-hand limit with $\widehat R\otimes_RS$, because $S$ is a finite $R$-module. Every identification respects the maps from $R$ and $S$, giving the asserted natural product. If there are no primes above $\mathfrak p$, then $S_{\mathfrak p}=0$, and both sides are the zero ring, with the empty product interpreted as that ring. ∎

<a id="algebra-lemma-compose-finite-type"></a>

#### Lemma F.28: compose finite type

Reading source: [AI Integrated Stacks, pinned Algebra, lines 547–571](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L547-L571).

Finite-type maps compose, and finitely presented maps compose. Given $R\to S'\to S$, if $S/R$ is finite type then $S/S'$ is finite type. If $S/R$ is finitely presented and $S'/R$ is finite type, then $S/S'$ is finitely presented.

**Proof.** Choose generators $y_1,\ldots,y_a$ for $S'$ over $R$ and $x_1,\ldots,x_b$ for $S$ over $S'$. Each coefficient of a polynomial expression in the $x_j$ is itself a polynomial in the $y_i$ with coefficients in $R$. Substitution shows that the combined finite list generates $S$ over $R$, proving the first claim.

For the second claim take finite presentations
$$S'=R[Y_1,\ldots,Y_a]/(u_1,\ldots,u_c),\qquad
S=S'[X_1,\ldots,X_b]/(v_1,\ldots,v_d).$$
Lift the finitely many coefficients of the $v_j$ through $R[Y]\twoheadrightarrow S'$ to obtain $\widetilde v_j\in R[Y,X]$. Then
$$R[Y,X]/(u_1,\ldots,u_c,\widetilde v_1,\ldots,\widetilde v_d)
\cong S.$$
Indeed quotienting first by the $u_i$ gives $S'[X]$, where the remaining equations are exactly the $v_j$. This is a finite presentation of the composite.

If $S$ is generated by a finite list over $R$, every element is already an $R$-coefficient polynomial in that list, hence also an $S'$-coefficient polynomial. This proves the third claim without a finiteness assumption on $S'$.

For the fourth claim write
$$S=R[X_1,\ldots,X_b]/(f_1,\ldots,f_d),\qquad S'=R[Y_1,\ldots,Y_a]/J.$$
The ideal $J$ need not be finite. For each $i$ choose $h_i(X)$ representing the image of $\bar Y_i$ in $S$. Form the finitely presented $S'$-algebra
$$Q=S'[X_1,\ldots,X_b]/
(f_1,\ldots,f_d,\bar Y_1-h_1(X),\ldots,\bar Y_a-h_a(X)).$$
Evaluation at the specified elements of $S$ defines $Q\to S$. Conversely the images of the $X_j$ in $Q$ satisfy every $f_j$, giving an $R$-map $S\to Q$. Their composite on $S$ fixes its $R$-algebra generators. The other composite fixes each $X_j$, and it fixes every coefficient from $S'$ because it fixes $\bar Y_i=h_i(X)$ and $S'$ is generated by those elements over $R$. Both composites are identities, so $Q\cong S$ as $S'$-algebras. This proves finite presentation over $S'$ without making any extra assumption on $J$. ∎

<a id="algebra-lemma-compose-smooth"></a>

#### Lemma F.29: compose smooth

Reading source: [AI Integrated Stacks, pinned Algebra, lines 39039–39053](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L39039-L39053).

If $R\to S$ and $S\to T$ are smooth ring maps, then $R\to T$ is smooth.

**Proof.** First translate the cotangent condition into the earlier lifting criterion. For a polynomial presentation of $S/R$, F.11 identifies its conormal complex with the canonical one. F.6 gives zero kernel and a projective differential cokernel, so the conormal sequence is split exact. AG-CA-17, Theorem 3.1 then proves that $S$ is formally smooth over $R$. The same argument proves that $T$ is formally smooth over $S$.

In a lifting problem $T\to C/J$ over $R$, where $J$ is nilpotent, first lift its restriction $S\to C/J$ to an $R$-map $S\to C$. This supplies an $S$-algebra structure on $C$ whose reduction is exactly the given one. Formal smoothness of $T/S$ now lifts the original map to an $S$-map $T\to C$. In particular it is an $R$-map. Thus $T/R$ is formally smooth, by an explicit composition of the two lifts.

Finite presentation is equally explicit. Write $S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_r)$ and $T=S[y_1,\ldots,y_m]/(g_1,\ldots,g_s)$, and lift each coefficient in the $g_j$ to a polynomial in the $x_i$. The resulting polynomials $\widetilde g_j$ give $T=R[x_i,y_l]/(f_i,\widetilde g_j)$: the two maps fixing the generators are inverse by the quotient universal property. Applying the same entire conormal criterion AG-CA-17, Theorem 3.1 to this finite presentation gives zero first homology and finite projective differentials. F.11 transports them to the canonical complex, so F.6 proves that $R\to T$ is smooth. The lifting and presentation arguments include zero algebras and empty lists. ∎

<a id="algebra-lemma-compose-standard-smooth"></a>

#### Lemma F.30: compose standard smooth

Reading source: [AI Integrated Stacks, pinned Algebra, lines 38815–38878](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L38815-L38878).

A composite of standard smooth ring maps is standard smooth.

**Proof.** Take standard smooth presentations
$$S=R[X_1,\ldots,X_n]/(f_1,\ldots,f_c),\qquad
T=S[Y_1,\ldots,Y_m]/(g_1,\ldots,g_d).$$
Reorder the variables in each list so that the first $c$ and first $d$ variables respectively give the chosen square Jacobian minors. Denote their determinants by $\Delta_f$ and $\Delta_g$; they are units in $S$ and $T$. Choose polynomial representatives $\widetilde g_j\in R[X,Y]$ for the coefficients of every $g_j$. Quotienting first by $(f)$ and then by the remaining equations gives
$$T\cong R[X_1,\ldots,X_n,Y_1,\ldots,Y_m]/
(f_1,\ldots,f_c,\widetilde g_1,\ldots,\widetilde g_d).$$

Use the pivot variables $X_1,\ldots,X_c,Y_1,\ldots,Y_d$ and write Jacobian rows by equations. In $T$ its selected matrix has the form
$$\begin{pmatrix}A&0\\ B&C\end{pmatrix},\qquad
A=(\partial f_i/\partial X_j),\quad
C=(\partial g_i/\partial Y_j).$$
The upper-right entries are zero because the $f_i$ contain no $Y$ variables. Reduction of the derivatives of $\widetilde g_i$ with respect to $Y_j$ equals the derivatives of $g_i$: changing polynomial coefficients commutes with the monomial differentiation rule.

In the permutation expansion of this determinant, a nonzero term must assign the first $c$ rows to the first $c$ columns; otherwise one of those rows uses a zero upper-right entry. The remaining rows then use the remaining columns. Factoring the two independent permutation sums gives $\det A\det C=\Delta_f\Delta_g$. The image of the first unit and the second given unit are units in $T$, so their product is a unit. The displayed finite presentation is therefore standard smooth.

If a presentation includes a principal localization at $h$, replace it by one more variable $Z$ and equation $hZ-1$. With $Z$ added last to the pivot list, the old equation rows have zero $Z$ entry and the new last diagonal entry is $h$. The selected determinant is the old determinant times $h$, which is invertible in the localized quotient. This calculation encodes all the stated localized presentations before applying the preceding composition argument. Empty equation lists use determinant one and the same permutation calculation. ∎

<a id="algebra-lemma-composition-essentially-of-finite-type"></a>

#### Lemma F.31: composition essentially of finite type

Reading source: [AI Integrated Stacks, pinned Algebra, lines 13129–13138](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L13129-L13138).

Composites of essentially finite-type ring maps are essentially finite type. Composites of essentially finitely presented ring maps are essentially finitely presented.

**Proof.** Let $R\to S\to T$ be the maps. Write $S=U^{-1}A$, where $A$ is a finite-type $R$-algebra, and write $T=V^{-1}(S[Y_1,\ldots,Y_m]/J)$. Set $P=A[Y_1,\ldots,Y_m]$ and let $K$ be the kernel of $P\to S[Y]/J$. Its quotient $B=P/K$ is finite type over $R$, even if $J$ and $K$ have infinitely many generators.

The map $U^{-1}P\to S[Y]/J$ has kernel exactly $U^{-1}K$. Indeed every element of $U^{-1}P$ is $f/u$; its image is zero precisely when the image of $f$ is zero, because the image of $u$ is a unit. This identifies $U^{-1}B$ with $S[Y]/J$. For each $v\in V$, choose a fraction $b_v/u_v$ representing it in $U^{-1}B$. Let $W\subset B$ be generated multiplicatively by the images of $U$ and all the $b_v$. Since the $u_v$ are already inverted, inverting $b_v/u_v$ is equivalent to inverting $b_v$. The localization universal property in both directions gives $T\cong W^{-1}B$, proving the finite-type assertion. No single denominator for all relations has been assumed.

For finite presentation, choose $A$ finitely presented over $R$ and $J=(j_1,\ldots,j_d)$ in $U^{-1}P$. Each $j_i$ has the form $f_i/u_i$ with $f_i\in P$ and $u_i\in U$. The images of $f_1,\ldots,f_d$ generate the same ideal after localizing at $U$, since all their denominators are units there. Therefore
$$S[Y]/J\cong U^{-1}\bigl(A[Y]/(f_1,\ldots,f_d)\bigr).$$
The algebra in parentheses is finitely presented over $R$: combine the finite presentation of $A$ with these finitely many polynomial equations, as in [F.28](#algebra-lemma-compose-finite-type). As before, incorporate the numerator representatives of $V$ into the final multiplicative set. Thus $T$ is a localization of a finitely presented $R$-algebra. The two arguments also cover empty variable lists and the zero algebra. ∎

<a id="algebra-lemma-composition-syntomic"></a>

#### Lemma F.32: composition syntomic

Reading source: [AI Integrated Stacks, pinned Algebra, lines 38404–38453](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L38404-L38453).

For arbitrary ring maps $R\to S\to T$:

1. If both maps are syntomic, their composite is syntomic.
2. If both maps admit relative global complete-intersection presentations, their composite admits such a presentation.

**Proof.** Begin with (2). Choose presentations
$$S=R[X_1,\ldots,X_n]/(f_1,\ldots,f_c),\qquad
T=S[Y_1,\ldots,Y_m]/(h_1,\ldots,h_d).$$
Lifting each coefficient of $h_j$ to $R[X]$ gives polynomials $\widetilde h_j$ and the exact presentation
$$T\cong R[X,Y]/(f_1,\ldots,f_c,\widetilde h_1,\ldots,\widetilde h_d).$$
To check [F.4](#algebra-definition-relative-global-complete-intersection), fix $\mathfrak p\subset R$ and let $k=\kappa(\mathfrak p)$, $A=S\otimes_Rk$ and $B=T\otimes_Rk$. Empty $B$ imposes no dimension condition. If $B\ne0$, then $A\ne0$, and $\dim A=n-c$. Every nonempty fibre of $A\to B$ has dimension $m-d$: it is a field extension of a corresponding fibre of $S\to T$, so the coefficient-change calculation [F.14](#algebra-lemma-base-change-relative-global-complete-intersection) applies.

We prove both dimension inequalities for $B$. Given a minimal prime $\eta$ of $B$, let $\mathfrak a=\eta\cap A$, $F=\kappa(\mathfrak a)$ and $L=\kappa(\eta)$. The finite-type domain $A/\mathfrak a$ has dimension $\operatorname{trdeg}_kF\leq\dim A=n-c$, by AG-CA-09, Theorem 4.2. The prime induced by $\eta$ in $B\otimes_AF$ has residue field $L$. That fibre has dimension $m-d$, so applying the same domain dimension theorem to its prime quotient gives $\operatorname{trdeg}_FL\leq m-d$. Transcendence degrees add here. To check this, choose a finite transcendence basis $U$ of $F/k$ and one $V$ of $L/F$. The elements of $V$ are independent over $F$, hence over $k(U)$; together with the independence of $U$ this proves independence of $U\cup V$ over $k$. Algebraicity of $F/k(U)$ and $L/F(V)$, and transitivity of algebraicity, show that $L/k(U,V)$ is algebraic. Thus
$$\dim(B/\eta)=\operatorname{trdeg}_kL
=\operatorname{trdeg}_kF+\operatorname{trdeg}_FL
\leq n-c+m-d.$$
The Noetherian finite-type algebra $B$ has finitely many minimal primes, and its dimension is the maximum of their quotient dimensions. This proves the upper bound.

For the lower bound, the polynomial presentation of $B$ has $n+m$ variables and $c+d$ equations. A prime minimal over its equation ideal has height at most $c+d$, by the full height theorem AG-CA-11, Theorem 3.1. The polynomial domain dimension formula AG-CA-09, Theorem 4.3, makes its quotient dimension at least $n+m-c-d$. Such a prime exists because $B\ne0$. Consequently $\dim B\geq n+m-c-d$. Equality follows, proving (2) over arbitrary $R$.

For (1), first suppose that $R$ is Noetherian. Finite presentation of both syntomic maps makes $S$ and $T$ Noetherian by the Hilbert basis theorem. At $\mathfrak q\subset T$, with contraction $\mathfrak r\subset S$, the entire neighbourhood criterion [F.87](#algebra-lemma-syntomic) supplies $g\in S\setminus\mathfrak r$ and $h\in T\setminus\mathfrak q$ such that $R\to S_g$ and $S\to T_h$ have relative global complete-intersection presentations. By F.14, $S_g\to T_{gh}$ has one too. Assertion (2) gives such a presentation for $R\to T_{gh}$. These opens cover $\operatorname{Spec}T$. Its quasi-compactness AG-CA-01, Proposition 2.3 gives a finite subcover. Each chart is syntomic by F.87, and the complete gluing proof [F.62](#algebra-lemma-local-syntomic) gives syntomicity of $T/R$.

Now let $R$ be arbitrary. Finite presentation follows from F.28, and flatness follows by composing the two exact tensor functors, as in AG-CA-07, Proposition 3.2. For $\mathfrak p\subset R$ use the same $k,A,B$ as above. The map $k\to A$ is syntomic: finite presentation and flatness survive base change, and its only field fibre is the given local complete intersection. The map $A\to B$ is also syntomic. Its finite presentation and flatness are the base changes of those of $S\to T$. At a prime $\mathfrak a\subset A$ over $\mathfrak r\subset S$, its fibre is
$$B\otimes_A\kappa(\mathfrak a)
\cong\bigl(T\otimes_S\kappa(\mathfrak r)\bigr)
\otimes_{\kappa(\mathfrak r)}\kappa(\mathfrak a).$$
Choose the principal global complete-intersection cover of the original field fibre, as in [F.2](#algebra-definition-lci-field). Scalar extension carries that cover to a cover, and F.14 carries each of its presentations to a global complete-intersection presentation. Thus the displayed fibre is a local complete intersection. Since the base $k$ is Noetherian, the case already proved applies to $k\to A\to B$. It makes $B/k$ syntomic, in particular a local complete intersection. Every field fibre of $T/R$ has now been checked. Together with flatness and finite presentation, the syntomic definition [F.1](#algebra-definition-lci) proves (1) for arbitrary bases. ∎

<a id="algebra-lemma-conormal-module-localize"></a>

#### Lemma F.33: conormal module localize

Reading source: [AI Integrated Stacks, pinned Algebra, lines 37203–37225](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L37203-L37225).

Suppose that $R[X_1,\ldots,X_n]\twoheadrightarrow S$ and $R[Y_1,\ldots,Y_m]\twoheadrightarrow S_g$ have kernels $I$ and $J$. There is an isomorphism of $S_g$-modules
$$(I/I^2)_g\oplus S_g^{\oplus m}
\cong J/J^2\oplus S_g^{\oplus n}.$$

**Proof.** Put $C=S_g$, $P=R[X]$ and $Q=R[Y]$. Choose $f\in P$ mapping to $g$. Exact localization gives $P_f\twoheadrightarrow C$ with kernel $I_f$. Lift the image of each $Y_j$ to $u_j\in P_f$, and lift the image of each $X_i$ to $v_i\in Q$.

The simultaneous evaluation $W=P[Y]=Q[X]\to C$ has kernel $L=(J,X_i-v_i(Y))$: quotienting by the graph equations eliminates $X$ and leaves exactly $Q/J$. Translation by $v_i(Y)$ makes $W=Q[Z_1,\ldots,Z_n]$ and $L=(J,Z_1,\ldots,Z_n)$. In this polynomial ring
$$L^2=(J^2,\ JZ_1,\ldots,JZ_n,\ Z_iZ_j\mid1\leq i,j\leq n).$$
Therefore reading the constant term modulo $J^2$ and each linear coefficient modulo $J$ gives an isomorphism $L/L^2\to J/J^2\oplus C^n$. Its inverse sends a relation class to its constant representative and each coordinate to the class of the corresponding $Z_i$. Changes of representatives lie in the displayed square, so both maps are well defined and inverse.

The image of $f$ is a unit in $C$, and $L/L^2$ is a $C$-module. Multiplication by $f$ on it is consequently invertible. Localizing thus gives the same module, namely
$$L/L^2\cong L_f/L_f^2.$$
On $W_f=P_f[Y]$, the same evaluation has kernel $(I_f,Y_j-u_j)$: eliminating $Y$ leaves $P_f/I_f=C$. Translate $Y_j$ by $u_j$. The identical constant-and-linear calculation now gives
$$L_f/L_f^2\cong I_f/I_f^2\oplus C^m.$$
The ideal-product fraction formulas identify $I_f/I_f^2$ with $(I/I^2)_g$. Combining these isomorphisms gives the assertion. No free summand was cancelled, and no flatness of $C$ over $R$ was used. Empty variable lists and $C=0$ satisfy the same formulas. ∎

<a id="algebra-lemma-contained-in-radical"></a>

#### Lemma F.34: contained in radical

Reading source: [Stacks, Tag 0AME](https://stacks.math.columbia.edu/tag/0AME).

For an ideal \(I\) of a commutative ring \(R\), the inclusion \(I\subset\operatorname{Jac}(R)\) is equivalent to invertibility of every \(1+i\), \(i\in I\). Under either condition, every element invertible modulo \(I\) is already invertible in \(R\). Here the Jacobson radical is the intersection of all maximal ideals.

**Proof.** We first justify the maximal-ideal test for a unit. A nonunit \(a\) generates a proper ideal. The partially ordered set of proper ideals containing \((a)\) has an upper bound for every chain, its union: that union cannot contain \(1\), since then a member would contain \(1\). Zorn's lemma supplies a maximal proper ideal containing \(a\). Conversely no unit belongs to a proper ideal. Therefore an element is a unit exactly when it belongs to no maximal ideal.

Suppose \(I\) is contained in every maximal ideal. If a maximal ideal contained \(1+i\), it would contain its difference with \(i\), namely \(1\). This is impossible, so the unit test makes every \(1+i\) invertible. Conversely, if a maximal ideal \(\mathfrak m\) fails to contain \(I\), maximality gives \(I+\mathfrak m=R\). Write \(1=i+b\) with \(i\in I\) and \(b\in\mathfrak m\). The element \(b=1-i\) has the stipulated form, yet is not a unit. This contradiction proves the inclusion.

If \(a\bmod I\) is a unit, lift one inverse to \(b\in R\). Then \(ab=1+i\) for some \(i\in I\). The element \(b(ab)^{-1}\) is an actual inverse of \(a\), proving the last assertion. In the zero ring the empty intersection is the whole ring and its unique element is its identity and a unit; the conclusions hold there too. ∎

<a id="algebra-lemma-cover-upstairs"></a>

#### Lemma F.35: cover upstairs

Reading source: [AI Integrated Stacks, pinned Algebra, lines 4346–4405](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L4346-L4405).

Let $g_1,\ldots,g_r\in S$ generate the unit ideal. The $R$-algebra $S$ is finite type, respectively finitely presented, if and only if every $S_{g_i}$ has that property.

**Proof.** We will use a finite-cover calculation for arbitrary modules. In a ring $A$, suppose $\sum_i c_it_i=1$ and $N_{t_i}=0$ for all $i$. For $n\in N$, choose positive $e_i$ with $t_i^{e_i}n=0$. In the expansion of $(\sum_i c_it_i)^b$ with $b=1+\sum_i(e_i-1)$, every monomial has an exponent at least $e_i$ in one of the $t_i$. Multiplication by $n$ kills every monomial. Since the expanded element is one, $n=0$. Thus $N=0$ without a finiteness hypothesis.

Choose $h_i$ with $\sum_i h_ig_i=1$. If every $S_{g_i}$ is finite type, choose a finite $R$-algebra generator list for each, written as fractions $a_{ij}/g_i^{b_{ij}}$. Let $S_0\subset S$ be generated over $R$ by all $a_{ij},g_i,h_i$. The map $(S_0)_{g_i}\to S_{g_i}$ is surjective by the chosen generators. It is injective: a numerator from $S_0$ whose fraction vanishes in $S_{g_i}$ is killed by a power of $g_i$ in $S$, hence also in the subring $S_0$. Therefore $(S/S_0)_{g_i}=0$ as a module over $S_0$. The $g_i$ generate one in $S_0$, so the cover calculation gives $S=S_0$. This proves finite type.

If every chart is finitely presented, the finite-type case supplies $S=P/J$ for a finite polynomial ring $P=R[X_1,\ldots,X_n]$. Choose lifts $u_i,v_i\in P$ of $g_i,h_i$. The kernel of
$$P[Z]\longrightarrow S_{g_i},\qquad Z\longmapsto g_i^{-1},$$
is $JP[Z]+(u_iZ-1)$, since its quotient is exactly $(P/J)[Z]/(g_iZ-1)$. The entire presentation-independence proof [F.44](#algebra-lemma-finite-presentation-independent) makes this kernel finitely generated. Express each of its finite generators as a finite sum of multiples of elements of $J$ and of $u_iZ-1$. Collect the finitely many coefficients $a_{ij}\in J$ used in those sums. They, together with $u_iZ-1$, generate the same kernel: they belong to it and generate each chosen generator.

Set
$$J_0=\bigl(\sum_i v_iu_i-1,\ a_{ij}\text{ for all }i,j\bigr)\subset J,\qquad A=P/J_0.$$
The images of $u_i$ generate one in $A$. The preceding kernel equalities give isomorphisms $A_{u_i}\cong S_{g_i}$. Indeed adjoining $Z$ with $u_iZ-1$ identifies both quotients with the same localization, and every element of $J_0$ also belongs to the original kernel. The kernel $J/J_0$ of $A\twoheadrightarrow S$ therefore vanishes on this cover. The arbitrary-module calculation gives $J=J_0$, so the original finite polynomial presentation has a finite relation ideal.

Conversely, localization adds only $g_i^{-1}$ to a finite generating list. For a finite presentation $S=P/(f_1,\ldots,f_d)$ and a lift $u_i$ of $g_i$ it gives the exact finite presentation $S_{g_i}=P[Z]/(f_1,\ldots,f_d,u_iZ-1)$. If the cover is empty, its unit-ideal condition forces $S=0$; the presentation $R/(1)$ handles both assertions directly. Empty generator lists cause no exception. ∎

<a id="algebra-lemma-criterion-flatness-fibre"></a>

#### Lemma F.36: criterion flatness fibre

Reading source: [AI Integrated Stacks, pinned Algebra, lines 34374–34496](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L34374-L34496).

Let $R\to S\to S'$ be local maps of local rings and write $\mathfrak m=\mathfrak m_R$. Suppose that both $S/R$ and $S'/R$ are essentially finitely presented, that $M\ne0$ is a finitely presented $S'$-module, that $M$ is $R$-flat, and that $M/\mathfrak mM$ is flat over $S/\mathfrak mS$. Then $S$ is $R$-flat and $M$ is $S$-flat. The original rings need not be Noetherian.

**Proof.** We construct compatible Noetherian local models, then apply the Noetherian fibre criterion twice through the two flatness hypotheses. The full finite-expression construction [F.59](#algebra-lemma-limit-essentially-finite-presentation) writes $R=\operatorname*{colim}R_\lambda$, where the $R_\lambda$ are local rings essentially of finite type over $\mathbf Z$, with maximal ideals $\mathfrak p_\lambda$ and local transitions. Their maximal ideals have colimit $\mathfrak m$.

An essentially finitely presented algebra that is local is a localization at one prime of a finitely presented algebra: all elements outside the inverse image of its maximal ideal are units, so the two localization universal properties identify the rings. Choose such finite presentations for $S$ and $S'$. To model their intervening map, choose images in $S'$ of the finite generators of $S$, represented by polynomials with finitely many denominators. Put those denominators among the inverted elements, and impose the finite graph equations equating the chosen source generators with their images. Eliminating the graph variables recovers the presentation of $S'$ over $R$ after localization. The source relations vanish there; any vanishing of their finitely many representatives is witnessed by finitely many additional denominators. Include these witnesses too. All the coefficients and finite equality witnesses can be placed at one stage of F.59.

For later stages we consequently have presentations
$$S_\lambda=(R_\lambda[X]/(f_\lambda))_{\mathfrak q_\lambda},\qquad
S'_\lambda=(R_\lambda[X,Y]/(f_\lambda,g_\lambda))_{\mathfrak q'_\lambda},$$
where the primes are contracted from the actual local target rings. The two maps are local. The coefficient lists are fixed and finite, so the Hilbert basis theorem makes all these model rings Noetherian. For $\mu\geq\lambda$, tensoring the displayed polynomials and relations gives exactly
$$S_\lambda\otimes_{R_\lambda}R_\mu\longrightarrow S_\mu,\qquad
S'_\lambda\otimes_{S_\lambda}S_\mu\longrightarrow S'_\mu$$
as localizations. The same description holds with the final rings $R,S,S'$.

Write a finite module presentation $(S')^a\xrightarrow{A}(S')^b\to M\to0$. By [F.60](#algebra-lemma-limit-module-essentially-finite-presentation), its finitely many matrix entries occur at a common stage. Define $M_\lambda=\operatorname{coker}((S'_\lambda)^a\xrightarrow{A_\lambda}(S'_\lambda)^b)$. Right exactness of tensor gives
$$M_\mu\cong M_\lambda\otimes_{S'_\lambda}S'_\mu,\qquad
M\cong M_\lambda\otimes_{S'_\lambda}S'.$$
In particular every $M_\lambda$ is nonzero, because a zero one would make the final tensor zero. It is finite over the stipulated Noetherian local overring $S'_\lambda$.

The $R$-flatness of $M$ and the localized tensor descriptions allow [F.21](#algebra-lemma-colimit-eventually-flat) to be applied to $R_\lambda\to S'_\lambda$ and $M_\lambda$. It gives a stage where $M_\lambda$ is $R_\lambda$-flat. At every later stage this persists: scalar extension preserves the exact tensor functor, and localization of an algebra-module preserves its injection tests. The final module and the later ones have precisely these two forms.

Next put
$$A_\lambda=S_\lambda/\mathfrak p_\lambda S_\lambda,\qquad
B_\lambda=S'_\lambda/\mathfrak p_\lambda S'_\lambda,\qquad
N_\lambda=M_\lambda/\mathfrak p_\lambda M_\lambda.$$
These are local Noetherian algebra models with finite target modules. The local transitions and right exactness give their colimits $S/\mathfrak mS$, $S'/\mathfrak mS'$ and $M/\mathfrak mM$. Reduction of the same polynomial presentations along the residue-field maps $R_\lambda/\mathfrak p_\lambda\to R_\mu/\mathfrak p_\mu$ shows that
$$B_\lambda\otimes_{A_\lambda}A_\mu\longrightarrow B_\mu$$
is a localization, and that $N_\mu=N_\lambda\otimes_{B_\lambda}B_\mu$. Thus this quotient system has every model property required by F.21. The assumed flatness of its limit over $S/\mathfrak mS$ gives a later stage where $N_\lambda$ is $A_\lambda$-flat. Passing to a common successor retains the first flatness assertion as well.

At that stage the local maps $R_\lambda\to S_\lambda\to S'_\lambda$ and the nonzero finite module $M_\lambda$ satisfy the full criterion [F.37](#algebra-lemma-criterion-flatness-fibre-Noetherian). It gives $R_\lambda$-flatness of $S_\lambda$ and $S_\lambda$-flatness of $M_\lambda$. Finally $S$ is a localization of $S_\lambda\otimes_{R_\lambda}R$, so it is $R$-flat. The module $M$ is a localization of $M_\lambda\otimes_{S_\lambda}S$, so it is $S$-flat. These conclusions use the exact scalar-extension and localization functors and impose no new hypothesis on the original rings. ∎

<a id="algebra-lemma-criterion-flatness-fibre-Noetherian"></a>

#### Lemma F.37: criterion flatness fibre Noetherian

Reading source: [AI Integrated Stacks, pinned Algebra, lines 24999–25045](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L24999-L25045).

Let $R\to S\to T$ be local maps of Noetherian local rings, let $\mathfrak m=\mathfrak m_R$, and let $M\ne0$ be finite over $T$. If $M$ is $R$-flat and $M/\mathfrak mM$ is flat over $S/\mathfrak mS$, then $M$ is faithfully flat over $S$ and $S$ is flat over $R$.

**Proof.** Set $I=\mathfrak mS$. Locality gives $I\subset\mathfrak m_S$, so it is proper. The map
$$u:\mathfrak m\otimes_RM\longrightarrow I\otimes_SM,\qquad
x\otimes z\longmapsto x\otimes z$$
is surjective: write an element of $I$ as a finite sum of products $sx$ and move each $s$ to the module factor. Its composite with multiplication $I\otimes_SM\to M$ is injective by $R$-flatness. Therefore $u$ is injective as well as surjective, and multiplication from $I\otimes_SM$ is injective. The ideal-kernel Tor calculation of AG-RG-S01, Lemma 1.A, gives $\operatorname{Tor}_1^S(S/I,M)=0$.

Apply the full proper-ideal criterion AG-CA-08, Corollary 4.4, to the source $S$, local overring $T$, finite $T$-module $M$ and ideal $I$. Its flat quotient condition is exactly the assumed flatness of $M/IM$ over $S/I$, and the Tor condition has just been proved. Thus $M$ is $S$-flat. Since $M$ is finite and nonzero over the local ring $T$, Nakayama [F.10](#algebra-lemma-NAK) gives $M/\mathfrak m_TM\ne0$. The quotient $M/\mathfrak m_SM$ surjects onto it, by locality of $S\to T$, so this closed fibre is nonzero too. The complete flat-module criterion AG-CA-08, Theorem 1.1, gives faithful flatness over $S$.

Let $L=\operatorname{Tor}_1^R(R/\mathfrak m,S)$. The ideal sequence over $R$ and its Tor-kernel calculation give the exact sequence of $S$-modules
$$0\longrightarrow L\longrightarrow\mathfrak m\otimes_RS
\longrightarrow I\longrightarrow0.$$
Tensor with the flat $S$-module $M$. Tensor associativity identifies its middle term with $\mathfrak m\otimes_RM$, and its final term is $I\otimes_SM$. Their map is the isomorphism $u$ already proved, so $L\otimes_SM=0$. Faithfulness forces $L=0$. AG-CA-08, Theorem 4.2, applied to the local map $R\to S$ and the module $S$, finite over its own Noetherian local overring, gives $R$-flatness of $S$. Both conclusions are established with the stated target-module finiteness, without assuming $M$ finite over $R$ or $S$. ∎

<a id="algebra-lemma-descent-regular"></a>

#### Lemma F.38: descent regular

Reading source: [AI Integrated Stacks, pinned Algebra, lines 48353–48371](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L48353-L48371).

If $R\to S$ is faithfully flat and $S$ is a regular ring, then $R$ is regular. In particular the source is Noetherian even if this is not separately assumed.

**Proof.** First prove that $R$ is Noetherian. For an ideal $I\subset R$, its extension $IS$ is finite because $S$ is Noetherian. Express a finite generating list for $IS$ using finitely many elements $a_1,\ldots,a_r$ of $I$, and let $I_0=(a_1,\ldots,a_r)$ in $R$. Then $I_0S=IS$. Flatness identifies $I\otimes_RS$ with $IS$ and $I_0\otimes_RS$ with $I_0S$, by tensoring their inclusions into $R$. Right exactness consequently gives $(I/I_0)\otimes_RS=0$. Faithfulness implies $I=I_0$. Every ideal is finite, proving Noetherianity.

Fix $\mathfrak p\subset R$. Faithful flatness supplies a prime $\mathfrak q\subset S$ above it, by AG-CA-08, Theorem 2.1. Put $A=R_{\mathfrak p}$, $B=S_{\mathfrak q}$ and $k=\kappa(\mathfrak p)$. The induced map $A\to B$ is flat and local, hence faithfully flat by that same theorem. The ring $B$ is regular local by the hypothesis.

Take a free resolution $F_\bullet\to k$ over the Noetherian local ring $A$. Tensoring with the flat algebra $B$ gives a free resolution of $k\otimes_AB$ over $B$. The complex computing its self-Tor is
$$(F_\bullet\otimes_AB)\otimes_B(k\otimes_AB)
\cong(F_\bullet\otimes_Ak)\otimes_AB.$$
Exact tensor with $B$ commutes with kernels and images, so the entire arbitrary-module resolution calculus AG-RG-S01, Lemma 1.A, gives
$$\operatorname{Tor}_i^A(k,k)\otimes_AB
\cong\operatorname{Tor}_i^B(k\otimes_AB,k\otimes_AB).$$
The regular-local global-dimension theorem AG-CA-14, Theorem 2.2, makes the right-hand groups zero for sufficiently large $i$. Faithfulness makes the corresponding source groups zero.

The full minimal-resolution construction AG-CA-13, Theorem 2.2, gives a resolution of $k$ by finite free $A$-modules whose differentials have entries in $\mathfrak m_A$. Tensoring it with $k$ makes every differential zero. Thus its degree-$i$ free term modulo $\mathfrak m_A$ is exactly $\operatorname{Tor}_i^A(k,k)$. Eventual vanishing makes those finite free terms zero, and the resolution truncates. Therefore $k$ has finite projective dimension. The reverse implication in AG-CA-14, Theorem 2.2, proves that $A$ is regular local. This holds at every source prime, proving regularity of $R$. ∎

<a id="algebra-lemma-dimension-fibres-bounded-open-upstairs"></a>

#### Lemma F.39: dimension fibres bounded open upstairs

Reading source: [AI Integrated Stacks, pinned Algebra, lines 32674–32690](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L32674-L32690).

For a finite-type ring map $R\to S$ and $\mathfrak q\subset S$ over $\mathfrak p\subset R$, put
$$n=\dim_{\bar{\mathfrak q}}\operatorname{Spec}
(S\otimes_R\kappa(\mathfrak p)),$$
the dimension in a neighbourhood of its point in the fibre. Some principal open neighbourhood of $\mathfrak q$ has fibre point-dimension at most $n$ at every point. The base ring is arbitrary.

**Proof.** The fibre is a finite-type algebra over $k=\kappa(\mathfrak p)$ and hence Noetherian. By the definition of point dimension and the complete field point-dimension theorem AG-CA-09, Theorem 6.1, choose a principal neighbourhood of $\bar{\mathfrak q}$ in that fibre whose algebra has dimension exactly $n$. Its defining element is a fraction $b/a$ with $b\in S$ and $a\in R\setminus\mathfrak p$. Since $a$ is a fibre unit, the same fibre open is defined by $b$; also $b\notin\mathfrak q$. Replace $S$ temporarily by $S_b$.

Apply the full Noether-normalization proof AG-CA-09, Lemma 2.1 and Corollary 3.2, to this fibre. It supplies $n$ algebraically independent parameters and a finite map from their polynomial algebra to the fibre. These parameters lift to elements $t_1,\ldots,t_n\in S_b$. Indeed that proof repeatedly replaces a generator by it minus an integer power of the last generator, so its chosen parameters are polynomials with integer coefficients in the original fibre generators. Dividing a relation by its nonzero leading coefficient proves integrality and does not change those parameter expressions.

The finite-type map $R[T_1,\ldots,T_n]\to S_b$, $T_i\mapsto t_i$, is quasi-finite at the chosen point. Its fibre there is a further fibre of the displayed finite $k[T]$-algebra, and is therefore finite-dimensional over the contracted polynomial prime's residue field. The entire open-locus proof [Zariski Main, Theorem C5.1](AG-RG-S04.md), using its algebraic Theorem C4.3 over arbitrary bases, gives a principal open around that point on which this polynomial map is quasi-finite everywhere. A defining fraction in $S_b$ has numerator $c\in S$; the resulting neighbourhood in the original spectrum is $D(bc)$.

For any $\mathfrak p'\subset R$, let $U=S_{bc}\otimes_R\kappa(\mathfrak p')$. The map $\kappa(\mathfrak p')[T]\to U$ is quasi-finite. This can be checked directly on its fibres: the polynomial base ring is a quotient and localization of $R[T]$ along $\mathfrak p'$, so a point and its residue field are those of the corresponding prime of $R[T]$, and its fibre is the fibre of the quasi-finite polynomial map just constructed.

At a minimal prime $\eta$ of a nonzero $U$, its residue field is finite over the residue field of its contracted polynomial prime, by the full isolated-fibre criterion [F.56](#algebra-lemma-isolated-point-fibre). The latter field has transcendence degree at most $n$ over $\kappa(\mathfrak p')$, since it is generated as a field by the images of $n$ polynomial variables. Finite algebraic extension preserves this transcendence degree. AG-CA-09, Theorem 4.2, therefore gives $\dim(U/\eta)\leq n$. Taking the maximum over its finitely many minimal primes gives $\dim U\leq n$. Every neighbourhood dimension at a point of this fibre is at most its total dimension, proving the required bound on $D(bc)$. Empty fibres have no point to check. The earlier conductor proof includes the polynomial-normality argument [Zariski Main over an arbitrary base, Corollary B1.2](AG-RG-S04.md); no Noetherian assumption on $R$ or $S$ has entered the argument. ∎

<a id="algebra-lemma-essentially-of-finite-type-into-artinian-local"></a>

#### Lemma F.40: essentially of finite type into artinian local

Reading source: [Stacks, Tag 07DT](https://stacks.math.columbia.edu/tag/07DT).

Let \(R\to S\) be any ring map, with \(S\) Artinian local, maximal ideal \(\mathfrak m\), and residue field \(K=S/\mathfrak m\). Each of the following properties of \(S/R\) is equivalent to the same property of \(K/R\): finite, of finite type, and essentially of finite type.

**Proof.** The Artinian length theorem AG-CA-03, Theorem 4.2 gives a finite composition series of the \(S\)-module \(S\). Every simple factor is \(K\): a nonzero element of a simple module generates it, and its annihilator is the unique maximal ideal. If \(K\) is finite over \(R\), each factor is therefore a finite \(R\)-module. Finite generation passes through an extension directly: lift finitely many generators of the quotient and adjoin finitely many generators of the submodule. Induction on the composition series makes \(S\) finite over \(R\). The converse follows by taking the images of module generators in \(K\). This proves the finite assertion for an arbitrary source ring.

For finite type, a quotient keeps the images of any finite list of algebra generators. Conversely, lift finite \(R\)-algebra generators of \(K\) to \(s_1,\ldots,s_a\in S\). The polynomial map \(P=R[X_1,\ldots,X_a]\to S\), \(X_i\mapsto s_i\), is surjective on residues. Thus \(K\) is cyclic as a \(P\)-module. The finite assertion just proved makes \(S\) a finite \(P\)-module. Choose its module generators \(u_1,\ldots,u_b\). Every element is a sum of polynomials in the \(s_i\) times the \(u_j\), so \(s_i,u_j\) together generate \(S\) as an \(R\)-algebra.

Finally, a quotient of a localization of a finite-type algebra is the localization of its quotient, by the fraction formula. Hence essential finite type passes from \(S\) to \(K\). For the converse write \(K=T^{-1}C\), with \(C\) a finite-type \(R\)-algebra, and let \(C_0\) be the image of \(C\) in \(K\). The domain \(C_0\) has fraction field \(K\): every element of the displayed localization is a fraction of its elements, and the field \(K\) contains the inverse of every nonzero element of \(C_0\).

Lift a finite list of \(R\)-algebra generators of \(C_0\) to \(S\), and let \(A\subset S\) be the \(R\)-subalgebra they generate. Put \(\mathfrak p=A\cap\mathfrak m\). Then \(A/\mathfrak p=C_0\), so \(\kappa(\mathfrak p)=K\). Every element of \(A\setminus\mathfrak p\) maps to a unit in \(S\); thus the inclusion extends to \(A_{\mathfrak p}\to S\). Applying the finite assertion to this map makes \(S\) a finite \(A_{\mathfrak p}\)-module. Choose generators \(v_1,\ldots,v_c\) and set \(B=A[v_1,\ldots,v_c]\subset S\). This is a finite-type \(R\)-algebra. Localizing \(B\) at \(A\setminus\mathfrak p\) maps injectively into \(S\), because those denominators are units there, and surjectively because the \(v_j\) generate over \(A_{\mathfrak p}\). Therefore \(S\) is that localization of \(B\). This proves the last equivalence without a finiteness assumption on \(R\). ∎

<a id="algebra-lemma-etale-standard-smooth"></a>

#### Lemma F.41: etale standard smooth

Reading source: [AI Integrated Stacks, pinned Algebra, lines 40737–40760](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L40737-L40760).

Every étale ring map $R\to S$ has a standard smooth presentation with equally many variables and equations:
$$S\cong R[X_1,\ldots,X_n]/(f_1,\ldots,f_n),\qquad
\det(\partial f_i/\partial X_j)\in S^\times.$$

**Proof.** If $S=0$, take $S=R[X]/(1)$. Its Jacobian determinant is zero, which is the unit element in the zero ring, so it has the required property.

Suppose $S\ne0$ and choose a finite polynomial presentation $P=R[X_1,\ldots,X_n]\twoheadrightarrow S$ with kernel $I$. The complete formal/conormal comparison AG-CA-17, Theorem 3.1 and Section 4, says that the conormal differential of an étale presentation is an isomorphism:
$$I/I^2\xrightarrow{\ \sim\ }\bigoplus_{i=1}^nS\,dX_i,\qquad
[f]\longmapsto\sum_i(\partial f/\partial X_i)dX_i.$$
Specifically, formal smoothness gives a split injection and formal unramifiedness gives zero cokernel; étaleness supplies both. Thus $I/I^2$ is finite free.

The entire global construction [F.55](#algebra-lemma-huber) replaces this presentation by $S=R[Y_1,\ldots,Y_m]/J$ with $J=(g_1,\ldots,g_c)$ and the classes of the $g_j$ a basis of $J/J^2$. Apply the same étale conormal comparison to this new presentation. In its actual equation and differential bases it is the Jacobian map $S^c\xrightarrow{H}S^m$. It is an isomorphism. Choose any maximal ideal of the nonzero ring $S$ and reduce this inverse pair modulo it. The resulting vector-space isomorphism forces $c=m$.

The matrix $H$ is now square and has an inverse over $S$. The determinant product identity gives $\det(H)\det(H^{-1})=1$, so its determinant is a unit. Relabeling these $m$ variables and $m$ equations produces the asserted presentation of the whole algebra. It proves global standard smoothness, with no Noetherian-base assumption or restriction to a neighbourhood. ∎

<a id="algebra-lemma-exact-sequence-NL"></a>

#### Lemma F.42: exact sequence NL

Reading source: [AI Integrated Stacks, pinned Algebra, lines 36838–36913](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L36838-L36913).

Let $A\to B\to C$ be ring maps. Choose surjections $P=A[x_s\mid s\in\mathcal S]\to B$ and $Q=B[y_t\mid t\in\mathcal T]\to C$, with kernels $I,J$. Put $E=A[x_s,y_t]$ and $K=\ker(E\to C)$. Variable sets may be infinite. Define
$$N_A=(I/I^2)\otimes_BC,\quad N_B=K/K^2,\quad N_C=J/J^2,$$
$$E_A=\bigoplus_sC\,dx_s,\quad
E_B=E_A\oplus\bigoplus_tC\,dy_t,\quad
E_C=\bigoplus_tC\,dy_t.$$
Their conormal differentials give the commutative diagram with exact rows
$$\begin{array}{ccccccccc}
0&\longrightarrow&E_A&\xrightarrow{i}&E_B&\xrightarrow{p}&E_C&\longrightarrow&0\\
&&\uparrow d_A&&\uparrow d_B&&\uparrow d_C\\
&&N_A&\xrightarrow{a}&N_B&\xrightarrow{b}&N_C&\longrightarrow&0.
\end{array}$$
No injectivity of $a$ is asserted. With the first cotangent homology $H_1(L_{-/ -})$ computed by these presentation complexes, the resulting canonical exact sequence is
$$\begin{gathered}
H_1(\operatorname{NL}_{B/A}\otimes_BC)\longrightarrow
H_1(L_{C/A})\longrightarrow H_1(L_{C/B})\\
\xrightarrow{\delta} C\otimes_B\Omega_{B/A}
\longrightarrow\Omega_{C/A}\longrightarrow\Omega_{C/B}\longrightarrow0.
\end{gathered}$$
It extends the differential sequence AG-CA-15, Theorem 3.1. If both $\operatorname{Tor}_1^B(\Omega_{B/A},C)$ and $\operatorname{Tor}_2^B(\Omega_{B/A},C)$ vanish, there is moreover a natural identification
$$H_1(\operatorname{NL}_{B/A}\otimes_BC)
\cong H_1(L_{B/A})\otimes_BC.$$

**Proof.** The map $i$ includes the $dx_s$ coordinates, and $p$ kills those coordinates and retains the $dy_t$. Their row is split exact. Define
$$a([f]\otimes c)=[\widetilde c f]\in K/K^2,\qquad
b([h])=[h\bmod IE]\in J/J^2,$$
where $\widetilde c\in E$ lifts $c$. Changing this lift adds an element of $K$ times $f\in I\subset K$, hence an element of $K^2$. Changing $f$ by $I^2$, or using a different polynomial lift of a coefficient in $B$, also changes the result by $K^2$. Multiplication of coefficient representatives proves the tensor-balancing relation, so $a$ is well defined. The map $E\to Q$ has kernel $IE$, maps $K$ onto $J$, and maps $K^2$ onto $J^2$. Therefore the preimage of $J^2$ in $K$ is $K^2+IE$: subtract a finite sum of products of lifts from $K$ to leave an element of $IE$. The image of $a$ is exactly $(IE+K^2)/K^2$. This proves exactness at $N_B$ and $N_C$.

Differentiation gives $d_B(\widetilde c f)=c\,df$, since $f$ evaluates to zero in $C$. Hence $d_Ba=id_A$. Projecting a polynomial derivative to its $dy_t$ part gives precisely its derivative in $Q$ relative to $B$, so $pd_B=d_Cb$. These identities prove commutativity of the entire diagram.

We now give the connecting map and check every exactness assertion. For $z\in\ker d_C$, choose $y\in N_B$ with $b(y)=z$. Then $p(d_By)=d_Cz=0$, so the split exact upper row gives a unique $v\in E_A$ with $i(v)=d_By$. Set $\delta(z)=[v]\in E_A/\operatorname{im}d_A$. If the lift $y$ changes, its difference is $a(x)$ for some $x\in N_A$; the corresponding $v$ changes by $d_Ax$. Thus this class is well defined.

A cycle $y\in\ker d_B$ mapping to zero under $b$ is $a(x)$, and $0=d_Ba(x)=i(d_Ax)$ forces $d_Ax=0$, since $i$ is injective. This proves exactness at $H_1(L_{C/A})$. At $\ker d_C$, the class $\delta(z)$ is zero precisely when the above $v$ is $d_Ax$ for some $x$; then $y-a(x)$ is a cycle lifting $z$. Conversely a cycle lift has $v=0$. This proves exactness at $H_1(L_{C/B})$.

At $E_A/\operatorname{im}d_A$, a class $[v]$ maps to zero in $E_B/\operatorname{im}d_B$ precisely when $i(v)=d_By$ for some $y$. Its image $b(y)$ is then a cycle in $N_C$, and the construction gives $\delta(b(y))=[v]$. At the next term, if $p(w)=d_Cz$, choose $y$ with $b(y)=z$. Then $p(w-d_By)=0$, so $w-d_By=i(v)$ for a $v\in E_A$. Thus $[w]$ comes from $[v]$. Conversely every image of $i$ is killed by $p$. Finally $p$ is surjective, so its map on the cokernels is surjective as well. These calculations prove the complete displayed sequence.

The entire presentation comparison [F.11](#algebra-lemma-NL-homotopy) identifies the kernels and cokernels with the stated cotangent homology and differential modules. The sequence is canonical under those identifications. Indeed comparison maps are obtained by lifting each source polynomial variable to the new presentation. Make the lifts for $B$ first, then lift the target variables for $C$ and their coefficients; this gives comparison maps on $P,Q,E$ respecting $I,J,K$. Their relation-class and derivative maps commute with $a,b,i,p$. Transporting a chosen lift $y$ transports its derivative and the unique $v$, so the connecting classes commute too. F.11 proves that alternative choices are homotopic and that the reverse comparisons induce inverse homology maps. Hence the induced sequence and its maps are independent of the chosen presentations.

For the final assertion write $\operatorname{NL}_{B/A}=[F_1\xrightarrow{d}F_0]$, with $F_0$ free, put $N=\operatorname{im}d$, $H=\ker d$ and $\Omega=\operatorname{coker}d$. The short exact sequence $0\to N\to F_0\to\Omega\to0$ and the first Tor hypothesis give
$$0\longrightarrow N\otimes_BC\longrightarrow F_0\otimes_BC
\longrightarrow\Omega\otimes_BC\longrightarrow0.$$
The long Tor sequence and freeness of $F_0$ identify $\operatorname{Tor}_1^B(N,C)$ with $\operatorname{Tor}_2^B(\Omega,C)$, using the full resolution calculus of AG-RG-S01, Lemma 1.A. The second hypothesis therefore makes tensoring $0\to H\to F_1\to N\to0$ give
$$0\longrightarrow H\otimes_BC\longrightarrow F_1\otimes_BC
\longrightarrow N\otimes_BC\longrightarrow0.$$
Since $N\otimes_BC$ injects into $F_0\otimes_BC$, these two sequences identify $H\otimes_BC$ with the kernel of the tensor differential. This is the claimed natural first-homology identification. No flatness of $F_1$ and no finite-variable assumption has been added. ∎

<a id="algebra-lemma-extension"></a>

#### Lemma F.43: extension

Reading source: [Stacks, Tag 0519](https://stacks.math.columbia.edu/tag/0519).

Let \(R\) be any ring and let \(0\to M_1\to M_2\to M_3\to0\) be exact. If the two end modules are finite, so is the middle module; a quotient of a finite module is finite. If both end modules are finitely presented, so is the middle module. A quotient of a finitely presented module by a finite submodule is finitely presented. Finally, if \(M_2\) is finite and \(M_3\) is finitely presented, then \(M_1\) is finite.

**Proof.** Identify \(M_1\) with its image in \(M_2\). To generate the middle module, take generators of \(M_1\) and lifts of generators of \(M_3\). Subtracting a combination of the latter from an arbitrary element leaves an element of \(M_1\). Images of any generating list generate a quotient. These observations prove the two assertions about finite modules.

We first establish the presentation calculation needed in the other assertions. Suppose \(q : G\twoheadrightarrow N\) is a finite free presentation with finitely generated kernel \(L\), and \(p : F\twoheadrightarrow N\) is any surjection from a finite free module. Choose maps \(u : F\to G\) and \(v : G\to F\) by lifting their finite bases, so that \(qu=p\) and \(pv=q\). For every \(z\in\ker p\),
\[
z=v(uz)+(1-vu)z,
\qquad uz\in L.
\]
Both \(v(L)\) and \((1-vu)F\) lie in \(\ker p\), since \(pv=q\) and \(pvu=qu=p\). Thus that kernel is generated by the images under \(v\) of a finite generating list of \(L\), together with the finitely many columns of \(1-vu\). In particular the kernel of every finite free surjection onto a finitely presented module is finite. The choices of lifts here use only the defining property of a free basis.

If \(M_2\) is finite, choose a finite free surjection \(F\to M_2\). When \(M_3\) is finitely presented, the kernel of the composite \(F\to M_3\) is finite by this calculation. Its image in \(M_2\) is exactly \(M_1\): an element mapping to zero in \(M_3\) has any chosen lift in that kernel. Hence \(M_1\) is finite.

Next write a finitely presented \(M_2\) as \(F/K\), with \(F\) finite free and \(K\) finite. If \(M_1\) is generated by \(a_1,\ldots,a_h\), choose lifts \(\widetilde a_i\in F\). The kernel of \(F\to M_3\) is
\[
K+R\widetilde a_1+\cdots+R\widetilde a_h.
\]
Indeed an element in that kernel maps to a combination of the \(a_i\) in \(M_2\); subtracting the corresponding lifted combination puts it in \(K\). This is a finite kernel and gives the asserted finite presentation of the quotient.

Finally choose finite free presentations \(p_i : F_i\twoheadrightarrow M_i\), with finite kernels \(K_i\), for \(i=1,3\). Lift the basis of \(F_3\) to obtain \(\ell : F_3\to M_2\), and use
\[
F_1\oplus F_3\longrightarrow M_2,
\qquad (a,b)\longmapsto p_1(a)+\ell(b).
\]
It is onto by the first generator argument. For each generator \(b_j\) of \(K_3\), the element \(\ell(b_j)\) lies in \(M_1\); choose \(a_j\in F_1\) with \(p_1(a_j)=-\ell(b_j)\). Its kernel is generated by \((K_1,0)\) and the finitely many pairs \((a_j,b_j)\). To see this, the second coordinate of any kernel element lies in \(K_3\). Subtract a combination of these pairs to make that coordinate zero; the first coordinate then lies in \(K_1\). We have constructed a finite generating list of relations, so \(M_2\) is finitely presented. Empty generating lists and zero modules satisfy the same formulas. No Noetherian assumption is used. ∎

<a id="algebra-lemma-finite-presentation-independent"></a>

#### Lemma F.44: finite presentation independent

Reading source: [Stacks, Tag 00R2](https://stacks.math.columbia.edu/tag/00R2).

If an \(R\)-algebra \(S\) is finitely presented, the kernel of every surjection \(\alpha : R[X_1,\ldots,X_n]\twoheadrightarrow S\) is a finitely generated ideal.

**Proof.** Fix one presentation
\[
S=R[Y_1,\ldots,Y_m]/(f_1,\ldots,f_h).
\]
Choose \(g_i(Y)\) representing \(\alpha(X_i)\), and, using the surjectivity of \(\alpha\), choose \(h_j(X)\) representing the class of \(Y_j\). In the polynomial ring \(P=R[X_1,\ldots,X_n]\), form the finite ideal
\[
J=\bigl(f_1(h(X)),\ldots,f_h(h(X)),\;
X_i-g_i(h(X))\ (1\leq i\leq n)\bigr).
\]
Each generator maps to zero under \(\alpha\), by the choices of representatives, so \(J\subset\ker\alpha\).

For the reverse inclusion, take \(F(X)\in\ker\alpha\). The polynomial \(F(g(Y))\) represents zero in the fixed presentation; hence there are polynomials \(c_l(Y)\) with
\[
F(g(Y))=\sum_{l=1}^h c_l(Y)f_l(Y).
\]
Substitute \(Y=h(X)\). This puts \(F(g(h(X)))\) in \(J\). Also
\[
F(X)-F(g(h(X)))\in
\bigl(X_i-g_i(h(X)):1\leq i\leq n\bigr).
\]
Here is the polynomial identity behind this last inclusion, valid over an arbitrary ring. Replace the variables one at a time and telescope the differences. At a single variable, every monomial difference is divisible by its coordinate difference, because
\(U^a-V^a=(U-V)\sum_{b=0}^{a-1}U^{a-1-b}V^b\) for \(a>0\); the difference is zero for \(a=0\). Adding the monomials proves the inclusion without division by any coefficient. Thus \(F\in J\), proving \(\ker\alpha=J\). The argument includes either empty variable list, an empty relation list and the zero algebra. ∎

<a id="algebra-lemma-flat-fibre-smooth"></a>

#### Lemma F.45: flat fibre smooth

Reading source: [AI Integrated Stacks, pinned Algebra, lines 39115–39149](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L39115-L39149).

Let $R\to S$ be a ring map and let $\mathfrak q\subset S$ lie over $\mathfrak p\subset R$. Suppose that some $s\in S\setminus\mathfrak q$ makes $S_s$ finitely presented over $R$, that $R_{\mathfrak p}\to S_{\mathfrak q}$ is flat, and that $S\otimes_R\kappa(\mathfrak p)$ is smooth at the point of this fibre induced by $\mathfrak q$. Then $R\to S$ is smooth at $\mathfrak q$, over an arbitrary base ring.

**Proof.** Replace $S$ by $S_s$ and keep the same notation for the prime. Choose a finite presentation $S=P/I$, where $P=R[X_1,\ldots,X_n]$ and $I=(a_1,\ldots,a_m)$. Let $\mathfrak r$ be the inverse image of $\mathfrak q$ in $P$, and put
$$A=R_{\mathfrak p},\quad k=\kappa(\mathfrak p),\quad
Q=P_{\mathfrak r},\quad B=S_{\mathfrak q}.$$
Thus $0\to I_{\mathfrak r}\to Q\to B\to0$ is exact over $A$, and $B$ is $A$-flat.

The full arbitrary-module Tor construction [AG-RG-S01, Lemmas 1.0 and 1.A](AG-RG-S01.md#1-the-algebra-of-localization) gives exactness after tensoring this sequence with $k$. Indeed use a free resolution of $k$ to compute $\operatorname{Tor}_1^A(k,B)$; tensoring with flat $B$ preserves the kernels and images of that exact resolution, so its positive homology is zero. The natural long exact Tor sequence therefore gives
$$0\longrightarrow I_{\mathfrak r}/\mathfrak pI_{\mathfrak r}
\longrightarrow Q/\mathfrak pQ\longrightarrow B/\mathfrak pB\longrightarrow0.$$
Set $\bar Q=Q/\mathfrak pQ$, $\bar B=B/\mathfrak pB$ and $J=\ker(\bar Q\to\bar B)$. The injection identifies $J$ with $I_{\mathfrak r}/\mathfrak pI_{\mathfrak r}$. Quotient and localization commute by their fraction maps, giving $\bar Q=k[X]_{\bar{\mathfrak r}}$ and $\bar B=\bar Q/J$. These are local rings, $J$ lies in the maximal ideal of $\bar Q$, and $J$ is generated by the finitely many images of the $a_j$.

The smooth fibre has a smooth principal neighbourhood. Definition [F.6](#algebra-definition-smooth), presentation comparison [F.11](#algebra-lemma-NL-homotopy), and the full conormal criterion AG-CA-17, Theorem 3.1 make that neighbourhood formally smooth over $k$: its injective conormal map has projective cokernel, so the sequence splits. The localization lifting proof in AG-CA-17, Theorem 1.2, gives formal smoothness of its local ring $\bar B$. This argument does not assert that the local ring is finitely presented.

Apply formal smoothness to the square-zero surjection $\bar Q/J^2\to\bar B$, lifting the identity of $\bar B$ to a $k$-algebra section $\sigma$. Then
$$D(q)=q\bmod J^2-\sigma(q\bmod J)\in J/J^2$$
is a $k$-derivation. Expanding $q=\sigma(\bar q)+D(q)$ and $q'=\sigma(\bar q')+D(q')$, the product of the two correction terms is zero, giving the Leibniz rule. For $j\in J$, $D(j)=[j]$. The universal differential construction thus supplies a left inverse of
$$J/J^2\longrightarrow\Omega_{\bar Q/k}\otimes_{\bar Q}\bar B=\bar B^n.$$
The differential basis and its localization are the complete AG-CA-15, Theorems 5.1 and 2.2. In coordinates this conormal map sends $[j]$ to its partial derivatives. Consequently $J/J^2$ is a finite projective direct summand of $\bar B^n$.

Choose from $a_1,\ldots,a_m$ elements $f_1,\ldots,f_c$ whose reduced conormal classes form a basis over the residue field $\kappa(\mathfrak q)$. The finite Nakayama argument [F.10](#algebra-lemma-NAK) makes the map $\bar B^c\to J/J^2$ surjective. Projectivity splits it. Its kernel is a finite direct summand of $\bar B^c$, and its residue quotient is zero by the chosen residue basis; a second application of F.10 makes this kernel zero. Thus the chosen classes are a free basis.

Let $H$ be their $c$-by-$n$ equation-by-variable Jacobian over $\bar B$. The conormal map has matrix $H^{\mathsf T}$ and a left inverse, so its reduction modulo the maximal ideal is injective; hence $c\leq n$. The full maximal-minor calculation [F.70](#algebra-lemma-matrix-left-inverse), applied to this $n$-by-$c$ matrix and its left inverse with scalar $1$, makes its maximal minors generate one in $\bar B$. Some minor is therefore a unit in this local ring. Transposing the selected minor preserves its determinant. Let $\Delta\in P$ be the corresponding $c$-variable Jacobian determinant. Its residue in $\kappa(\mathfrak q)$ is nonzero, so $\Delta\notin\mathfrak r$. If $c=0$, use the empty basis and $\Delta=1$.

The chosen $f_i$ generate the whole ideal after localizing at $\mathfrak r$. First $J=(\bar f_1,\ldots,\bar f_c)+J^2$. Its finite quotient by the displayed generators is equal to $J$ times that quotient. Since $J$ lies in the local maximal ideal, F.10 gives $J=(\bar f_1,\ldots,\bar f_c)$. Now the finite $Q$-module
$$M=I_{\mathfrak r}/(f_1,\ldots,f_c)Q$$
has quotient $M/\mathfrak pM=0$, by the exact tensor identification of $J$. The ideal $\mathfrak pQ$ lies in the maximal ideal of $Q$, so F.10 gives $M=0$. This is where the flat local quotient is used; neither ring has needed a chain condition.

For each original generator $a_j$ of $I$, write its image in $Q$ as a finite combination of the $f_i$. Clear all coefficient denominators, and also the multipliers outside $\mathfrak r$ witnessing the resulting equalities in the localization. Their finite product $v\notin\mathfrak r$ gives
$$I_v=(f_1,\ldots,f_c)P_v,\qquad
S_{\bar v\bar\Delta}\cong R[X]_{v\Delta}/(f_1,\ldots,f_c).$$
This uses the fraction equality criterion, including its annihilator factor, so no possible zero divisor has been cancelled.

Adjoin $Z$ with equation $v\Delta Z-1$. The selected Jacobian block for the $c$ pivot variables and $Z$ has zero $Z$ entries in the first $c$ rows; its determinant is $\Delta(v\Delta)=v\Delta^2$, a unit in the quotient. The entire arbitrary-base standard-smooth proof [F.85](#algebra-lemma-standard-smooth) applies to this finite presentation and proves its smoothness. In terms of lifting, it inverts this square block, corrects the lifted pivot coordinates by the negative error vector, and the monomial expansion kills all terms containing two corrections in a square-zero ideal. Unit lifts then extend evaluation through the inverse-variable relation, exactly as proved in F.85.

Finally express the elements inverted in this neighbourhood of $S_s$ as fractions with powers of $s$ as denominators. Inverting $s$ and their finitely many numerators gives one principal neighbourhood in the original $\operatorname{Spec}S$ containing $\mathfrak q$. Its smoothness proves the conclusion, including empty pivot lists. ∎

<a id="algebra-lemma-flat-over-regular"></a>

#### Lemma F.46: flat over regular

Reading source: [Stacks, Tag 07DY](https://stacks.math.columbia.edu/tag/07DY).

Let \(R\to S\) be a homomorphism of Noetherian local rings. Suppose \(R\) is regular and one regular system of parameters \(x_1,\ldots,x_d\) maps to an \(S\)-regular sequence. Then \(S\) is flat over \(R\). A regular sequence here has proper generated ideal.

**Proof.** The \(x_i\) generate the maximal ideal of \(R\). Their images belong to the maximal ideal of \(S\), because the ideal they generate is proper in that local ring. Thus the given map is local, even though this was not a separate assumption.

For \(0\leq i\leq d\), put
\[
R_i=R/(x_1,\ldots,x_i),\qquad
S_i=S/(x_1,\ldots,x_i)S.
\]
These are nonzero Noetherian local rings and their induced maps are local. The written regular-parameter theorem AG-CA-12, Theorem 6.1 makes the chosen list regular in \(R\). Therefore, for every \(i<d\), multiplication by \(x_{i+1}\) is injective on \(R_i\); the assumed regularity in \(S\) gives the same injection on \(S_i\).

At \(i=d\), the source \(R_d\) is the residue field of \(R\), so \(S_d\) is flat over it. Indeed a vector-space basis identifies tensoring with that space with a direct sum of copies of a module, which preserves injections.

We descend from \(i+1\) to \(i\). Since \(x_{i+1}\) is a nonzerodivisor of \(R_i\),
\[
0\longrightarrow R_i\xrightarrow{x_{i+1}}R_i
\longrightarrow R_{i+1}\longrightarrow0
\]
is a free resolution. Tensoring it with \(S_i\) computes
\[
\operatorname{Tor}_1^{R_i}(R_{i+1},S_i)
=\ker(x_{i+1} : S_i\to S_i)=0.
\]
The quotient \(S_i/x_{i+1}S_i=S_{i+1}\) is flat over \(R_{i+1}\) by the descending induction. Apply the complete ideal local criterion AG-CA-08, Corollary 4.4 and equation (6) to \(R_i\to S_i\), the proper ideal \((x_{i+1})\subset R_i\), and the module \(S_i\). This module is finite over the target ring \(S_i\), being generated by \(1\); it need not be finite over the source. The Tor vanishing and quotient flatness prove that \(S_i\) is \(R_i\)-flat. The induction reaches \(S_0=S\) over \(R_0=R\). If \(d=0\), the initial field argument already proves the conclusion. ∎

<a id="algebra-lemma-flat-over-regular-with-regular-fibre"></a>

#### Lemma F.47: flat over regular with regular fibre

Reading source: [Stacks, Tag 031E](https://stacks.math.columbia.edu/tag/031E).

Let \((R,\mathfrak m)\to(S,\mathfrak n)\) be a flat local map of Noetherian local rings. If \(R\) and the closed fibre \(F=S/\mathfrak mS\) are regular, then \(S\) is regular.

**Proof.** Put \(d=\dim R\) and \(e=\dim F\). Regularity supplies generators \(x_1,\ldots,x_d\) of \(\mathfrak m\) and generators \(\overline y_1,\ldots,\overline y_e\) of the maximal ideal \(\mathfrak n/\mathfrak mS\) of \(F\). Choose lifts \(y_j\in\mathfrak n\). Every \(z\in\mathfrak n\) reduces to a combination of the \(\overline y_j\); lifting the coefficients and subtracting that combination leaves an element of \(\mathfrak mS=(x_1,\ldots,x_d)S\). Consequently
\[
\mathfrak n=(x_1,\ldots,x_d,y_1,\ldots,y_e)S.
\]
Its cotangent space \(\mathfrak n/\mathfrak n^2\) is therefore spanned by at most \(d+e\) vectors over the residue field of \(S\).

The flat local dimension formula, with precisely the stated Noetherian and flatness hypotheses, is proved in AG-CA-11, Theorem 5.1; it gives \(\dim S=d+e\). Its Proposition 4.2 proves that the dimension of a Noetherian local ring is at most the dimension of its cotangent space: lifts of a cotangent basis generate the maximal ideal by finite Nakayama, and the parameter/height theorem bounds dimension by that generator count. Combining these inequalities gives
\[
d+e=\dim S\leq
\dim_{\kappa(\mathfrak n)}\mathfrak n/\mathfrak n^2
\leq d+e.
\]
Equality of dimension and embedding dimension is the definition of regularity, so \(S\) is regular. The empty source or fibre parameter lists when \(d=0\) or \(e=0\) obey the same calculation. No finite-type assumption on the ring map is needed. ∎

<a id="algebra-lemma-flatness-descends-more-general"></a>

#### Lemma F.48: flatness descends more general

Reading source: [Stacks, Tag 0584](https://stacks.math.columbia.edu/tag/0584).

Let \(S\to S'\) be a flat map of \(R\)-algebras, let \(M\) be any \(S\)-module, and put \(M'=S'\otimes_S M\). If \(M\) is flat over \(R\), so is \(M'\). If \(S\to S'\) is faithfully flat, the converse holds as well.

**Proof.** Test an arbitrary injection \(f:N\hookrightarrow N_1\) of \(R\)-modules. Write
\[
Z=\ker\bigl(N\otimes_R M\xrightarrow{f\otimes1}N_1\otimes_R M\bigr).
\]
Both tensor products, their map and \(Z\) are \(S\)-modules, using the action on \(M\). Flatness of \(S'\) over \(S\) preserves this kernel. The balancing relations give inverse isomorphisms
\[
S'\otimes_S(N\otimes_R M)\ \longleftrightarrow\ N\otimes_R M',
\qquad s'\otimes(n\otimes m)\ \longleftrightarrow\ n\otimes(s'\otimes m),
\]
and the same formula for \(N_1\). These maps commute with \(f\), so
\[
S'\otimes_S Z\cong
\ker\bigl(N\otimes_R M'\longrightarrow N_1\otimes_R M'\bigr).
\]
If \(M\) is \(R\)-flat, \(Z=0\), and the displayed kernel vanishes for every \(f\). If \(M'\) is \(R\)-flat, the right side is zero; faithful flatness then detects \(Z=0\). In either direction the injection characterization of flatness, proved for arbitrary modules in AG-CA-07, Theorem 2.1, gives the claimed flatness. No module in this calculation is required to be finite. ∎

<a id="algebra-lemma-formally-smooth-extensions-easy"></a>

#### Lemma F.49: formally smooth extensions easy

Reading source: [AI Integrated Stacks, pinned Algebra, lines 45971–46012](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L45971-L46012).

For a field extension $K/k$, each of the following conditions implies formal smoothness of $K$ over $k$: it is purely transcendental; it is separable algebraic; or it is separable in the sense of [F.5](#algebra-definition-separable-field-extension). Infinite generator sets and infinite algebraic extensions are allowed.

**Proof.** In the first case write $K=k(x_j\mid j\in\mathcal J)$. Given a $k$-algebra $D$, a square-zero ideal $I$ and a $k$-map $K\to D/I$, choose lifts $a_j\in D$ of the variable images. Polynomial evaluation at these lifts is well defined because each polynomial involves finitely many variables. Every nonzero polynomial in the $x_j$ is a unit in $K$, so its evaluated image is a unit modulo $I$. Units lift: if $bc=1+r$ with $r\in I$, then $bc(1-r)=1$ since $r^2=0$. Thus all the nonzero polynomials have unit evaluations in $D$. The polynomial map extends uniquely, for these chosen variable lifts, through the fraction-field localization to a $k$-map $K\to D$. Its reduction is the given map, proving the lifting property.

For a separable algebraic extension, a finite subset of $K$ generates a finite separable subextension: successive degrees of its finitely many algebraic generators are finite and multiply along the tower. These subfields are directed under inclusion, since the union of two finite generator lists is finite, and their union is $K$. The full separable-generator tower proof AG-CA-17, Proposition 6.3 gives a unique square-zero lift on every such finite field. The derivatives of its separable minimal polynomials are units, so its successive one-equation lifting steps apply. Consequently every finite subextension is formally étale. The entire compatible-lifts proof [F.22](#algebra-lemma-colimit-formally-etale) makes their colimit formally étale, and hence formally smooth.

In the third case use the directed family of finitely generated subfields $K_i/k$. By F.5 each has a separating transcendence basis and is a finite separable extension of the resulting rational-function field. The first two cases give formal smoothness of both maps in that tower; the full composition lifting proof AG-CA-17, Theorem 1.2 gives formal smoothness of $K_i/k$. The arbitrary-field criterion [F.17](#algebra-lemma-characterize-formally-smooth-field-extension) therefore gives $H_1(L_{K_i/k})=0$.

Now [F.24](#algebra-lemma-colimits-NL) identifies the conormal complex of $K/k$ with the filtered colimit of these complexes. Its representative proof of exactness of filtered module colimits also identifies their homology: a cycle is represented at a stage after its finite differential equality holds, and a boundary equality is witnessed at a common later stage. Thus $H_1(L_{K/k})=\operatorname*{colim}_iH_1(L_{K_i/k})=0$. Applying F.17 again proves formal smoothness of $K/k$. This uses the field criterion, rather than assuming a general permanence theorem for filtered colimits of formally smooth algebras. ∎

<a id="algebra-lemma-geometrically-regular"></a>

#### Lemma F.50: geometrically regular

Reading source: [AI Integrated Stacks, pinned Algebra, lines 48753–48798](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L48753-L48798).

Let $A$ be a Noetherian $k$-algebra, where $k$ is a field. Regularity of $A\otimes_kK$ for every finitely generated field extension $K/k$ is equivalent to regularity of $A\otimes_kk'$ for every finite purely inseparable field extension $k'/k$.

**Proof.** The forward implication includes the finite purely inseparable extensions among the finitely generated ones. For the converse, fix a finitely generated $K/k$. The full separabilization construction [F.69](#algebra-lemma-make-separably-generated) gives finite purely inseparable extensions $k'/k$ and $K'/K$, inside a commuting field square, with $K'/k'$ separably generated. This last extension is finitely generated: a finite field-generating list for $K/k$ and finitely many generators for $K'/K$ still generate $K'$ after enlarging the coefficient field to $k'$.

The entire forward smooth-domain construction [F.64](#algebra-lemma-localization-smooth-separable) supplies a smooth finite-type domain $D\subset K'$ over $k'$ with fraction field $K'$. Its explicit separating-generator equations, denominator clearing and derivative localization have been proved there. They also give the smooth field model recognized by AG-CA-18, Theorem 3.2.

By assumption $A'=A\otimes_kk'$ is regular. It is Noetherian by [F.12](#algebra-lemma-Noetherian-field-extension). Form $C=A'\otimes_{k'}D$. The coefficient-change polynomial presentation makes it finitely presented over $A'$, and formal smoothness survives base change by AG-CA-17, Theorem 1.2. Hence $C/A'$ is smooth. It is also Noetherian, being finite type over the Noetherian ring $A'$.

The complete smooth-flatness and regular-fibre results AG-CA-18, Theorems 6.1 and 2.1, make this map flat with regular residue-field fibres. At a prime of $C$, the localized source is regular, and its closed fibre is the local ring of one of those regular fibres. The full ascent calculation [F.47](#algebra-lemma-flat-over-regular-with-regular-fibre) therefore makes the target local ring regular. This proves regularity of $C$.

Localizing at all nonzero elements of $D$ gives
$$C\otimes_DK'=A'\otimes_{k'}K'\cong A\otimes_kK'.$$
Every local ring of this localization is a local ring of the original regular ring, so it is regular. Finally choose a basis of the finite field extension $K'/K$. As a module over $B=A\otimes_kK$, the algebra $A\otimes_kK'$ is the direct sum of $[K':K]\geq1$ copies of $B$, by tensoring this basis. Tensoring an arbitrary $B$-module with that algebra therefore takes this positive finite number of copies; it preserves exactness and detects zero modules. Thus the map $A\otimes_kK\to A\otimes_kK'$ is faithfully flat. The full arbitrary-source regularity descent proof [F.38](#algebra-lemma-descent-regular) makes $A\otimes_kK$ regular. This holds for every chosen $K$, proving the equivalence without a perfect-field assumption. ∎

<a id="algebra-lemma-geometrically-regular-descent"></a>

#### Lemma F.51: geometrically regular descent

Reading source: [AI Integrated Stacks, pinned Algebra, lines 48815–48834](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L48815-L48834).

Let $A\to B$ be a faithfully flat map of $k$-algebras. If $B$ is geometrically regular over the field $k$, then $A$ is geometrically regular over $k$. No separate Noetherianity hypothesis on $A$ is needed.

**Proof.** The trivial extension $k/k$ is among the field tests for geometric regularity, so $B$ is regular. The full regularity descent proof [F.38](#algebra-lemma-descent-regular) makes $A$ regular as well, deriving its Noetherianity by its finite-ideal argument.

For every finite purely inseparable extension $k'/k$, set $A'=A\otimes_kk'$ and $B'=B\otimes_kk'$. Both are Noetherian by [F.12](#algebra-lemma-Noetherian-field-extension). Tensor associativity identifies $B'$ with $A'\otimes_AB$, and for an arbitrary $A'$-module $M$ it gives the inverse pure-tensor maps
$$M\otimes_{A'}(A'\otimes_AB)\cong M\otimes_AB,\qquad
m\otimes(a'\otimes b)\longmapsto a'm\otimes b,\quad
m\otimes b\longmapsto m\otimes(1\otimes b).$$
The balancing relations verify these maps and their inverse composites. Restriction from $A'$-modules to $A$-modules preserves exact sequences and detects the zero module. Since $B$ is faithfully flat over $A$, the displayed tensor identification proves that $B'$ is faithfully flat over $A'$.

Geometric regularity makes $B'$ regular. Applying F.38 gives regularity of $A'$ for every such $k'$. The complete finite purely inseparable criterion [F.50](#algebra-lemma-geometrically-regular) now applies to the Noetherian algebra $A$ and proves its geometric regularity over $k$. ∎

<a id="algebra-lemma-geometrically-regular-over-subfields"></a>

#### Lemma F.52: geometrically regular over subfields

Reading source: [AI Integrated Stacks, pinned Algebra, lines 48851–48866](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L48851-L48866).

Let $A$ be a Noetherian algebra geometrically regular over the field $k$.

1. For any field extension $E/k$ such that $C=A\otimes_kE$ is Noetherian, $C$ is regular.
2. Under this same Noetherian tensor hypothesis, $C$ is geometrically regular over $E$.
3. If $k$ is a directed union of subfields $k_i$ and $A$ is geometrically regular over every $k_i$, then $A$ is geometrically regular over $k$.

**Proof.** For (1), write $E$ as the union of its intermediate fields $E_i$ generated by finite subsets over $k$. They are directed, since the union of two finite generator sets is finite. Put $C_i=A\otimes_kE_i$. An $E_i$-basis of $E$ containing $1$ gives
$$C=C_i\otimes_{E_i}E\cong\bigoplus_{\beta\in\mathcal B_i}C_i.$$
Here the structural inclusion $C_i\to C$ is the coordinate belonging to $1$. To obtain such a basis, take a maximal independent set containing $1$; if it did not span, a vector outside its span could be adjoined, contradicting maximality. The tensor/direct-sum calculation is AG-RG-S01, Lemma 1.0. It proves both injectivity of this inclusion and flatness of $C$ over $C_i$, even when the basis is infinite. Every element of $C$ uses finitely many field coefficients and so lies in one $C_i$.

Suppose that $C$ is Noetherian and fix $\mathfrak q\subset C$. In the Noetherian local ring $T=C_{\mathfrak q}$ choose a finite generating list $x_1,\ldots,x_r$ for its maximal ideal $\mathfrak m$. Write $x_j=a_j/s_j$, with $a_j\in\mathfrak q$ and $s_j\notin\mathfrak q$. Put all their finitely many field coefficients into a common $E_i$, so that every $a_j,s_j$ lies in $C_i$. Let $\mathfrak q_i=\mathfrak q\cap C_i$ and $B_i=(C_i)_{\mathfrak q_i}$. The fractions $x_j$ now belong to $B_i$, and their numerators lie in its maximal ideal.

The map $B_i\to T$ is local and flat: it is obtained by localizing the free scalar-extension map above, and exact localization preserves its injection tests. Its extended maximal ideal is contained in $\mathfrak m$ and contains every $x_j$. Hence
$$\mathfrak q_iT=\mathfrak m,\qquad
T\otimes_{B_i}\kappa(\mathfrak q_i)=T/\mathfrak m.$$
The source $B_i$ is Noetherian by [F.12](#algebra-lemma-Noetherian-field-extension), and is regular because $E_i/k$ is finitely generated and $A$ is geometrically regular. The displayed closed fibre is a field, thus regular. The entire flat-local ascent proof [F.47](#algebra-lemma-flat-over-regular-with-regular-fibre) makes $T$ regular. An empty generating list gives the same argument when $\mathfrak m=0$. This proves regularity at every prime of $C$; if $C=0$, there are no primes to test.

For (2), let $F/E$ be a finite purely inseparable extension. F.12 makes $C\otimes_EF$ Noetherian. Tensor associativity identifies it with $A\otimes_kF$, so (1), applied to the field extension $F/k$, makes it regular. The complete finite purely inseparable criterion [F.50](#algebra-lemma-geometrically-regular) proves geometric regularity of $C$ over $E$.

For (3), we construct an actual finite purely inseparable field model. Let $k'/k$ be finite purely inseparable. If it is trivial, use $k_i'=k_i$ at any index. Otherwise the characteristic is $p>0$. Choose a $k$-basis $b_1=1,b_2,\ldots,b_d$ of $k'$. A common exponent $e$ satisfies $b_j^{p^e}\in k$ for every $j$, since the extension is purely inseparable and the list is finite. Write its finitely many multiplication constants
$$b_jb_\ell=\sum_h c_{j\ell h}b_h,\qquad c_{j\ell h}\in k.$$
Choose $k_i$ containing all $c_{j\ell h}$ and all $b_j^{p^e}$. This is possible because the union is directed and the list is finite.

The subspace $V=\bigoplus_j k_i b_j\subset k'$ contains $1$ and is closed under multiplication by those identities. It is a finite-dimensional domain over $k_i$. Multiplication by any nonzero $v\in V$ is an injective endomorphism of that finite-dimensional vector space, hence surjective; a preimage of $1$ gives its inverse. Therefore $V$ is a field, denoted $k_i'$. Moreover every $v=\sum_j a_jb_j$ in it has
$$v^{p^e}=\sum_j a_j^{p^e}b_j^{p^e}\in k_i.$$
Thus $k_i'/k_i$ is finite purely inseparable. This checks the exponent condition for every element of the field, beyond just its chosen generators.

The multiplication map $k\otimes_{k_i}k_i'\to k'$, $a\otimes v\mapsto av$, is an algebra isomorphism: its basis $1\otimes b_j$ maps to the given $k$-basis $b_j$, proving both bijectivity and compatibility with the prescribed products. Consequently
$$A\otimes_kk'\cong A\otimes_{k_i}k_i'.$$
The right side is regular by the hypothesis over $k_i$. F.50 proves geometric regularity over $k$. In characteristic zero all finite purely inseparable extensions are trivial, so the same conclusion follows from the trivial case. All three assertions are established. ∎

<a id="algebra-lemma-grothendieck-regular-sequence"></a>

#### Lemma F.53: grothendieck regular sequence

Reading source: [AI Integrated Stacks, pinned Algebra, lines 24513–24526](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L24513-L24526).

Let $R\to P$ be a flat local map of Noetherian local rings, and let $\mathfrak m=\mathfrak m_R$. If the reductions of $f_1,\ldots,f_c\in P$ form a regular sequence in $P/\mathfrak mP$, then the list is regular in $P$, and every $P/(f_1,\ldots,f_i)$ is flat over $R$.

**Proof.** Put $P_i=P/(f_1,\ldots,f_i)$, including $P_0=P$. The regular-sequence hypothesis includes a nonzero final fibre quotient. Consequently each $\bar f_i$ belongs to the maximal ideal of the local closed fibre: a unit there would make the final quotient zero. Its lift $f_i$ belongs to the maximal ideal of $P$ as well. Every $P_i$ is thus a nonzero Noetherian local quotient, and $R\to P_i$ remains local. Its closed fibre is
$$P_i/\mathfrak mP_i
\cong(P/\mathfrak mP)/(\bar f_1,\ldots,\bar f_i).$$

Induct on $i$, keeping $R$-flatness of $P_i$. The initial assertion is the assumed flatness of $P$. On $P_i$ consider multiplication by $f_{i+1}$. Both its source and target are finite over this actual Noetherian local ring, and its target is $R$-flat by induction. The displayed fibre description and the original regular-list hypothesis make its reduction injective. The full lifting-injectivity proof AG-CA-08, Lemma 5.1 gives injectivity on $P_i$ and $R$-flatness of its cokernel $P_{i+1}$. This proves the induction.

Every multiplication in the list has now been proved injective on its preceding quotient, and the final quotient is nonzero, so the list is regular. The same induction has proved flatness of each successive quotient. If $c=0$, the list is empty and the only quotient is the original flat ring $P$, giving both assertions directly. ∎

<a id="algebra-lemma-henselian-cat-finite-etale"></a>

#### Lemma F.54: henselian cat finite etale

Reading source: [Stacks, Tag 04GK](https://stacks.math.columbia.edu/tag/04GK).

For a henselian local ring \((R,\mathfrak m,k)\), reduction \(S\mapsto S/\mathfrak mS\) is an equivalence from finite étale \(R\)-algebras to finite products of finite separable extensions of \(k\). Ring maps are unital, and the zero algebra is the empty product.

**Proof.** The written idempotent and finite-algebra theorem [AG-CA-20, Theorem 2.2](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/AG-CA/henselian-local-rings-and-henselization.html) decomposes a finite \(R\)-algebra into finitely many local factors. A factor of an étale algebra is étale, since it is localization at its component idempotent. For each such factor \(S_i\), reduction is an étale \(k\)-algebra and is local: every maximal ideal of a finite algebra contracts to \(\mathfrak m\), and \(S_i\) has only one. The field classification AG-CA-17, Theorem 7.2 makes this reduction a finite separable field. In particular \(\mathfrak mS_i\) is its maximal ideal. Every \(S_i\) is henselian by [AG-CA-20, Proposition 3.1](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/AG-CA/henselian-local-rings-and-henselization.html).

Construct a lift of a finite separable field extension \(L/k\) as follows. Choose finitely many field generators and use their successive fields
\[
k=L_0\subset L_1\subset\cdots\subset L_a=L,
\qquad L_i=L_{i-1}(\alpha_i).
\]
Each minimal polynomial is monic separable. Starting with \(T_0=R\), lift its coefficients to a monic \(h_i\in T_{i-1}[X]\) and define \(T_i=T_{i-1}[X]/(h_i)\). Its bounded powers of \(X\) are a free \(T_{i-1}\)-basis, by monic division. Reduction modulo \(\mathfrak m\) is \(L_i\). Every maximal ideal contracts to \(\mathfrak m\) by integrality, so the field reduction makes \(T_i\) local with maximal ideal \(\mathfrak mT_i\). The derivative \(h_i'\) has nonzero residue in that field and is consequently a unit. The one-equation Jacobian proof AG-CA-17, Theorem 4.1 and Section 6 makes \(T_i/T_{i-1}\) étale. Composition makes \(T_a/R\) finite étale, with free rank \([L:k]\) and reduction \(L\). Finite products of these lifts provide every desired residue algebra.

We next show explicitly that every local finite étale \(R\)-algebra \(S\), with residue \(L\), is isomorphic to this constructed \(T_a\). Given the residue identification, lift a map \(T_{i-1}\to S\) through the next step by choosing the root of \(h_i\) reducing to \(\alpha_i\). The simple-root Hensel statement, [AG-CA-20, Theorem 1.2](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/AG-CA/henselian-local-rings-and-henselization.html), gives exactly one such root in the henselian local ring \(S\), and hence exactly one map \(T_i\to S\) at each step. This constructs \(\phi:T_a\to S\) inducing the chosen isomorphism on residues.

By the complete arbitrary-base proof in [S04, Lemma E4.2](AG-RG-S04.md), a finite étale algebra is finite locally free. Its proof first obtains a finite module presentation from monic algebra equations, then applies Lemma A1.3 to a finitely presented flat module. Since \(R\) is local, \(S\) is finite free, of rank \(\dim_k(S/\mathfrak mS)=[L:k]\). Both modules in \(\phi\) therefore have this same finite rank. In chosen bases its matrix reduces to an invertible matrix over \(k\), so its determinant lies outside \(\mathfrak m\) and is a unit of \(R\). The adjugate matrix divided by this unit is its inverse. Thus \(\phi\) is an isomorphism of modules, and its bijective algebra map is an algebra isomorphism.

Now let \(S_1,S_2\) be local finite étale algebras and let \(L_1\to L_2\) be a \(k\)-field map between their residues. Replace \(S_1\) by its isomorphic tower \(T_a\). Starting with \(R\to S_2\), lift each successive generator to the unique simple root whose residue is its prescribed image in \(L_2\). The same Hensel calculation supplies a unique \(R\)-algebra map \(S_1\to S_2\) inducing the field map. Conversely, any algebra map has those generator values, so it is this unique lift. The map on residue fields is defined because \(\mathfrak mS_i\) is the maximal ideal.

For products, a map to a local target sends each source component idempotent to \(0\) or \(1\); orthogonality and their sum \(1\) force exactly one component to be chosen. The residue map chooses precisely that component, and the local result lifts its field map uniquely. Doing this independently for each target factor proves a bijection on all Hom sets. The empty-product cases follow from unital maps directly: there is one map to the zero ring and none from it to a nonzero ring. We have proved full faithfulness and essential surjectivity, hence the asserted equivalence, over every henselian local source. ∎

<a id="algebra-lemma-huber"></a>

#### Lemma F.55: huber

Reading source: [Stacks, Tag 07CF](https://stacks.math.columbia.edu/tag/07CF).

Suppose a finitely presented $R$-algebra $S$ has a finite polynomial presentation $S=P/I$, where $P=R[X_1,\ldots,X_n]$, and $I/I^2$ is free over $S$. Then $S$ has another finite polynomial presentation whose defining equations themselves form a basis of its conormal module.

**Proof.** [F.44](#algebra-lemma-finite-presentation-independent) makes $I$ finitely generated. Thus $I/I^2$ has a finite basis: when $S\ne0$, the supports of a finite generating list in any free basis have finite union, which must contain the entire basis; when $S=0$, choose its empty conormal basis directly. Lift this basis to $f_1,\ldots,f_c\in I$ and put $K=(f_1,\ldots,f_c)$. The basis property gives $I=K+I^2$. The finite $P$-module $U=I/K$ consequently satisfies $U=IU$.

Choose generators $u_1,\ldots,u_t$ of $U$ and coefficients $b_{ij}\in I$ with $u_i=\sum_j b_{ij}u_j$. The adjugate identity proved in [F.70](#algebra-lemma-matrix-left-inverse) applied to $1_t-(b_{ij})$ shows that
$$g=\det(1_t-(b_{ij})),\qquad gU=0,\qquad g\in1+I.$$
For $U=0$ take $g=1$. Hence $gI\subset K$ and $I_g=K_g$. The image of $g$ in $S$ is exactly $1$, so $P_g/I_g=S$. It follows, with both inverse maps given by adjoining or evaluating $g^{-1}$, that
$$S=P[T]/(f_1,\ldots,f_c,gT-1).$$

Let $L$ be the displayed equation ideal. After localization at $g$, the classes of $f_i$ form the given basis of $I_g/I_g^2$. The explicit inverse-variable conormal calculation [F.72](#algebra-lemma-principal-localization-NL), applied to $P_g/I_g$ and this presentation, identifies
$$L/L^2\cong S^c\oplus S.$$
The first basis vectors are $[f_i]$ and the last is $[gT-1]$: the last equation has derivative $g$, a unit, in its new variable, and the remaining classes are read by evaluation at $T=g^{-1}$. These are exactly the claimed equation classes. No Noetherian hypothesis or cancellation of a free summand is used. Empty bases use the same determinant convention; if $S=0$, all the displayed modules and bases are interpreted over the zero ring. ∎

<a id="algebra-lemma-isolated-point-fibre"></a>

#### Lemma F.56: isolated point fibre

Reading source: [Stacks, Tag 00PK](https://stacks.math.columbia.edu/tag/00PK).

Let $R\to S$ be of finite type and let $\mathfrak q\in\operatorname{Spec}S$ lie over $\mathfrak p$. Put $k=\kappa(\mathfrak p)$, $T=S\otimes_R k$, and let $x\in\operatorname{Spec}T$ be the corresponding point. The following conditions are equivalent: $x$ is isolated; $T_x=S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}$ is finite-dimensional over $k$; some $g\in S\setminus\mathfrak q$ has $x$ as the only point of its fibre neighbourhood; the fibre point-dimension at $x$ is zero; $x$ is closed and $\dim T_x=0$; and $\kappa(x)/k$ is finite and $\dim T_x=0$.

**Proof.** All the geometry can be checked in the finite-type field algebra $T$. Such an algebra and its principal localizations are Noetherian by AG-CA-03, Theorem 2.1. We will use the following consequence of its Theorem 4.2. A zero-dimensional finite-type $k$-algebra $B$ is Artinian, with finitely many local factors and nilpotent radical $J$. Every residue field is finite over $k$ by AG-CA-06, Theorem 2.1. Each $J^i/J^{i+1}$ is finite over the product $B/J$ of those fields: $B$ is Noetherian, so the ideals involved are finite. Its coordinate summands are consequently finite-dimensional over the residue fields, hence over $k$. The finite filtration by powers of $J$ proves that $B$ is finite-dimensional over $k$. The factor idempotents give a principal singleton neighbourhood of each of its points.

If $x$ is isolated, choose $h\in T$ with $D(h)=\{x\}$. The algebra $T_h$ has just one prime, so has dimension zero and is finite-dimensional by the preceding calculation. Every element outside its unique maximal ideal is a unit. Its localization at that ideal is therefore itself, and $T_x=T_h$ is finite-dimensional.

Conversely, a finite-dimensional $T_x$ is Artinian: chains of its ideals are chains of subspaces of a finite-dimensional $k$-space. Each of its prime quotients is a finite-dimensional domain, hence a field, because multiplication by a nonzero element is an injective, and thus surjective, linear map. Thus $\dim T_x=0$, and its residue field is finite over $k$. For a prime of a finite-type $k$-algebra, finiteness of the residue extension implies closedness: $T/x$ embeds into the finite-dimensional field $\kappa(x)$, so is a finite-dimensional domain and the same multiplication argument makes it a field. The converse follows from the cited weak Nullstellensatz.

Suppose now that $x$ is closed and $\dim T_x=0$. The prime corresponding to $x$ is both maximal and minimal. There are finitely many other minimal primes, by AG-CA-03, Proposition 2.2. From each choose an element outside $x$ and take their product $h$; use $h=1$ if there are none. A prime in $D(h)$ contains none of those other minimal primes. Since every prime contains a minimal prime, it must contain $x$ and therefore equal $x$. Hence $D(h)=\{x\}$ and $x$ is isolated. This proves the equivalence of isolation, finite local fibre algebra, and the two residue-field/local-dimension conditions.

An isolated point has point-dimension zero, using its singleton open neighbourhood. Conversely, zero point-dimension supplies an open neighbourhood of dimension zero: the infimum defining that dimension is an attained nonnegative integer. Take a principal neighbourhood inside it. Its algebra has dimension zero, so the Artinian factor calculation above supplies a smaller principal singleton neighbourhood of $x$. Thus zero point-dimension implies isolation as well.

Finally, every $h\in T=S_{R\setminus\mathfrak p}/\mathfrak pS_{R\setminus\mathfrak p}$ is represented by $g/s$ with $g\in S$ and $s\in R\setminus\mathfrak p$. The image of $s$ is a fibre unit, so $D(h)=D(\bar g)$, and $h\notin x$ means $g\notin\mathfrak q$. Conversely the fibre of $D(g)$ is exactly $D(\bar g)$. This proves the neighbourhood condition over the original ring, with no Noetherian assumption on $R$. ∎

<a id="algebra-lemma-lci"></a>

#### Lemma F.57: lci

Reading source: [AI Integrated Stacks, pinned Algebra, lines 37341–37441](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L37341-L37441).

Let $k$ be a field, $S$ a finite-type $k$-algebra, and $\mathfrak q$ a prime of $S$. Fix any polynomial presentation $S=P/I$, with $P=k[X_1,\ldots,X_n]$, and let $\mathfrak Q\subset P$ lie over $\mathfrak q$. Put
$$c=\operatorname{ht}\mathfrak Q-\operatorname{ht}\mathfrak q
=n-\dim_{\mathfrak q}\operatorname{Spec}S.$$
The last equality is the point-codimension formula [F.20](#algebra-lemma-codimension). The following are equivalent.

1. Some $S_g$, with $g\notin\mathfrak q$, is a global complete intersection over $k$.
2. $I_{\mathfrak Q}$ has a generating list of length $c$.
3. $(I/I^2)_{\mathfrak q}$ has a generating list of length $c$.
4. $(I/I^2)_{\mathfrak q}$ is free of rank $c$ over $S_{\mathfrak q}$.
5. $I_{\mathfrak Q}$ is generated by a regular sequence in $P_{\mathfrak Q}$.

Whenever these hold, every list of $c$ elements spanning $I_{\mathfrak Q}/\mathfrak QI_{\mathfrak Q}$ is a regular sequence in $P_{\mathfrak Q}$.

**Proof.** Write $V=P_{\mathfrak Q}$ and $J=I_{\mathfrak Q}$. The whole polynomial-local regularity proof AG-CA-14, Proposition 3.3, starting with $k$, makes $V$ regular. The whole AG-CA-12, Theorem 6.1 makes it Cohen–Macaulay. Its dimension is $\operatorname{ht}\mathfrak Q$, whereas $V/J=S_{\mathfrak q}$ has dimension $\operatorname{ht}\mathfrak q$. In particular $J$ is proper and finite, and the dimension drop is $c$.

Generators of $J$ give generators of $J/J^2=(I/I^2)_{\mathfrak q}$. Conversely lift $c$ generators of this quotient to $f_1,\ldots,f_c\in J$. Their quotient module $N=J/(f_1,\ldots,f_c)V$ satisfies $N=JN$. It is finite, and $J$ lies in the maximal ideal of $V$, so the determinant proof [F.10](#algebra-lemma-NAK) gives $N=0$. Thus (2) and (3) are equivalent. The entire expected-dimension criterion AG-CA-12, Theorem 4.2, now says that any such generating list is regular: it lies in the maximal ideal and lowers the dimension of the Cohen–Macaulay ring by exactly its length. A list spanning $J/\mathfrak QJ$ generates $J$ by the same Nakayama argument, proving the final assertion too.

We spell out the conormal basis for a regular generating list. The regular-list cone proof [F.118](#more-algebra-lemma-noetherian-finite-all-equivalent) makes its first Koszul homology zero. If $\sum_i a_if_i\in J^2$, write this sum as $\sum_i b_if_i$ with every $b_i\in J$. The vector $(a_i-b_i)$ is a first Koszul cycle, hence a boundary. Each coefficient of a degree-two Koszul boundary belongs to $J$, because its differential has coefficients among the $f_i$. Thus every $a_i\in J$. This proves independence, as well as generation, of the classes of the $f_i$ in $J/J^2$. Consequently (3) implies (4); (4) plainly implies (3). The same criterion proves (2) implies (5). If (5) uses a regular list of length $e$, successive regular quotients of a Cohen–Macaulay local ring lower dimension by one, by the complete depth and dimension proofs in AG-CA-12, Sections 2 and 4. Hence
$$\operatorname{ht}\mathfrak q
=\dim(V/J)=\dim V-e=\operatorname{ht}\mathfrak Q-e,$$
so $e=c$, proving (5) implies (2).

Suppose (2) holds. Choose generators $f_i=a_i/s_i$ with $a_i\in I$ and $s_i\notin\mathfrak Q$. Multiplication by these units shows that the $a_i$ also generate $J$ and form a regular list there. Since $I$ is finite over the Noetherian polynomial ring, each generator of $I/(a_1,\ldots,a_c)$ is killed by some element outside $\mathfrak Q$. Their product $h'\notin\mathfrak Q$ gives $I_{h'}=(a_1,\ldots,a_c)_{h'}$.

Choose a principal neighbourhood $D(h'')$ of $\mathfrak q$ on which the dimension is its point dimension. Here is the finite-component construction from F.20: for every minimal prime $\mathfrak p$ of $S$ not contained in $\mathfrak q$, choose an element in $\mathfrak p\setminus\mathfrak q$ and multiply these finitely many elements. The product kills exactly the components not passing through the point; any surviving component has its original dimension, since a nonempty principal open in a finite-type domain over a field has the same transcendence degree and dimension. Thus the maximum surviving component dimension is the point dimension, by the whole AG-CA-09, Theorem 6.1, calculation. Lift this product to $h''\in P\setminus\mathfrak Q$ and put $h=h'h''$. Its image $g$ is outside $\mathfrak q$, and
$$S_g\cong k[X_1,\ldots,X_n,Z]/
(a_1,\ldots,a_c,hZ-1),\qquad \dim S_g=n-c.$$
This is the required global complete-intersection presentation: there are $n+1$ variables, $c+1$ equations and the prescribed dimension difference. This proves (1).

Conversely suppose (1), and choose a global complete-intersection presentation $S_g=k[Y_1,\ldots,Y_m]/H$, with $H=(b_1,\ldots,b_t)$ and $\dim S_g=m-t$. Every minimal prime $\mathfrak a$ over $H$ has height at most $t$ by the entire AG-CA-11, Theorem 3.1. Its component has dimension $m-\operatorname{ht}\mathfrak a$ by the polynomial height formula in AG-CA-09, Theorem 4.3. Hence each component has dimension at least $m-t$, while their maximum is the given dimension $m-t$. All components therefore have dimension exactly $m-t$. The point formula of AG-CA-09, Theorem 6.1, gives this same dimension at $\mathfrak qS_g$.

At the polynomial prime $\mathfrak Q''$ over that point, [F.20](#algebra-lemma-codimension) consequently gives
$$t=\operatorname{ht}\mathfrak Q''-\operatorname{ht}\mathfrak q.$$
The actual ambient polynomial local ring is regular and Cohen–Macaulay as above. The expected-dimension criterion makes its given $b_1,\ldots,b_t$ regular. The conormal calculation already proved makes $(H/H^2)_{\mathfrak q}$ free of rank $t$. The entire graph-presentation calculation [F.33](#algebra-lemma-conormal-module-localize), localized at this point, supplies
$$S_{\mathfrak q}^{\,t+n}
\cong (I/I^2)_{\mathfrak q}\oplus S_{\mathfrak q}^{\,m}.$$
Thus the conormal module is a finite direct summand of a finite free module. Tensor injections restricted to this summand prove flatness; the finite complementary summand gives finite presentation. The full local finite-flat proof [AG-RG-S01, Lemma 1.2](AG-RG-S01.md) makes it free. Reducing the displayed isomorphism to the residue field computes its rank as
$$t+n-m=n-\dim_{\mathfrak q}\operatorname{Spec}S=c.$$
This proves (4). Empty equation lists are included in the conormal and dimension calculations, so every implication and the last assertion also hold when $c=0$. ∎

<a id="algebra-lemma-lci-at-prime"></a>

#### Lemma F.58: lci at prime

Reading source: [Stacks, Tag 00SG](https://stacks.math.columbia.edu/tag/00SG).

For a finite-type $k$-algebra $S$ and $\mathfrak q\in\operatorname{Spec}S$, the following are equivalent: $S_{\mathfrak q}$ is a complete intersection in the sense of [F.3](#algebra-definition-lci-local-ring); it has a global complete-intersection principal neighbourhood; and the kernel of any finite polynomial presentation of $S$ is generated by a regular sequence in the polynomial local ring above $\mathfrak q$. Equivalently, there is a principal neighbourhood that is locally a complete intersection over $k$.

**Proof.** Write $C=S_{\mathfrak q}$ and $P=k[X_1,\ldots,X_n]_{\mathfrak q'}\twoheadrightarrow C$. The field $k$ is a regular ring: its only prime localization is itself, with dimension and maximal-ideal generating number both zero. Iterating the entire polynomial-regularity proof AG-CA-14, Proposition 3.3 makes $k[X_1,\ldots,X_n]$ a regular ring. Its localization at the displayed prime is therefore regular local, by the definition of a regular ring. A regular generating list for its kernel therefore gives the ambient ring required by F.3. Conversely suppose F.3 gives $C=Q/(a_1,\ldots,a_e)$, where $Q$ is regular local and essentially of finite type over the same field $k$, and this list is regular in its maximal ideal. We compare this local ambient with $P$ explicitly.

Present $Q$ as a quotient of a polynomial local ring $V=k[Y_1,\ldots,Y_m]_{\mathfrak n}$. Both $V$ and $Q$ are regular local. AG-CA-14, Proposition 1.4, makes the kernel of $V\to Q$ generated by part of a regular parameter system. Append lifts of the $a_i$. The resulting list generates $\ker(V\to C)$ and is regular: its first successive quotients are those by the parameter list, and its remaining multiplication injections are precisely those of the given regular list in $Q$.

Let $U=k[X,Y]_{\mathfrak r}$, where $\mathfrak r$ is the preimage of the maximal ideal of $C$ under the map using both sets of coordinates, and put $L=\ker(U\to C)$. Lift the images of $X_i$ to $V$ and denote them by $u_i(Y)$; these are fractions with denominators outside $\mathfrak n$. Those denominators are units in $U$. The quotient by $X_i-u_i(Y)$ is $V$, including its indicated localization: evaluating an element outside $\mathfrak r$ gives an element outside $\mathfrak n$, hence a unit, and every fraction defining $V$ already occurs in $U$. Translation of polynomial variables shows that the graph equations form a regular sequence. They remain regular after localization by exactness, and their quotient is nonzero. Appending the preceding regular list in $V$ consequently gives a regular generating list for $L$.

In the other direction lift the images of $Y_j$ to fractions $v_j(X)$ in $P$. The identical graph calculation gives
$$U/(Y_j-v_j(X))\cong P,\qquad L=(\ker(P\to C),Y_j-v_j(X))U.$$
The constant and linear coefficient calculation of [F.33](#algebra-lemma-conormal-module-localize) works in this localized polynomial ring as well: first invert the finitely many denominators of the $v_j$, translate $Y_j$ by $v_j$, and then localize at $\mathfrak r$. Modulo $L^2$ its constant terms are read modulo $\ker(P\to C)^2$, its graph-linear coefficients modulo $\ker(P\to C)$, and terms of graph-degree at least two vanish. The resulting mutually inverse maps give
$$L/L^2\cong \ker(P\to C)/\ker(P\to C)^2\oplus C^m.$$

The regular list for $L$ makes its conormal finite free by [F.74](#algebra-lemma-regular-quasi-regular). Its rank is $\dim U-\dim C$ by AG-CA-12, Corollary 6.2. Hence the first summand in the display is finite projective, and is finite free over the local ring $C$ by [S01, Lemma 1.2](AG-RG-S01.md). Reduction to its residue field computes its rank. The polynomial height formula AG-CA-09, Theorem 4.3 gives $\dim U=\dim P+m$, since the two polynomial primes have the same residue field $\kappa(\mathfrak q)$. The rank is thus $\dim P-\dim C$. F.57 now supplies a regular generating list for $\ker(P\to C)$ and a global complete-intersection principal neighbourhood of $\mathfrak q$. This proves the assertion for every chosen polynomial presentation, including the local ambients in F.3.

Conversely a global complete-intersection neighbourhood has the regular local equation lists proved in F.57, so gives F.3 at $\mathfrak q$. It is also locally a complete intersection: apply F.57 at each of its points. A locally complete-intersection principal neighbourhood contains a further global complete-intersection principal neighbourhood of the specified point by the defining local condition. If the further inverted element is $b/g^r$ in $S_g$, that neighbourhood is $S_{gb}$, with $gb\notin\mathfrak q$. This proves the last equivalence. All graph and rank calculations allow empty coordinate or equation lists. ∎

<a id="algebra-lemma-limit-essentially-finite-presentation"></a>

#### Lemma F.59: limit essentially finite presentation

Reading source: [AI Integrated Stacks, pinned Algebra, lines 33722–33770](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L33722-L33770).

Let $R\to S$ be a local map of local rings, with $S$ essentially finitely presented over $R$. There are a directed set and local maps $R_\lambda\to S_\lambda$ such that their colimit is $R\to S$, each $R_\lambda$ is essentially finite type over $\mathbf Z$, each $S_\lambda$ is essentially finite type over $R_\lambda$, and, for $\lambda\leq\mu$,
$$S_\lambda\otimes_{R_\lambda}R_\mu\longrightarrow S_\mu$$
is localization at a prime. All model rings are Noetherian, although $R$ and $S$ need not be.

**Proof.** Write $S=(R[X_1,\ldots,X_n]/(f_1,\ldots,f_c))_{\mathfrak q}$. Such a prime localization represents the given local essentially finitely presented algebra: in any localization presentation, every element outside the inverse image of the local maximal ideal is a unit, so the two localization universal properties give the prime localization. Locality of $R\to S$ makes $\mathfrak q\cap R=\mathfrak m_R$.

Let $\Lambda$ be the finite subsets of $R$ containing all coefficients of the $f_j$, ordered by inclusion. It is directed under finite union. Let $A_\lambda\subset R$ be the subring generated by such a subset over the image of $\mathbf Z$, put $\mathfrak p_\lambda=A_\lambda\cap\mathfrak m_R$, and set $R_\lambda=(A_\lambda)_{\mathfrak p_\lambda}$. Elements outside $\mathfrak p_\lambda$ are units in $R$, so this localization embeds in $R$: a fraction becoming zero has zero numerator, since its denominator is a unit there and $A_\lambda$ is a subring. The maps $R_\lambda\to R_\mu$ are therefore inclusions and are local, with maximal ideals contracted from $\mathfrak m_R$. Every element of $R$ occurs in some finite subset, proving $\operatorname*{colim}R_\lambda=R$.

Define
$$C_\lambda=R_\lambda[X_1,\ldots,X_n]/(f_1,\ldots,f_c),$$
where the fixed coefficient list lies in $R_\lambda$. Let $\mathfrak q_\lambda$ be the inverse image of the maximal ideal of $S$ under $C_\lambda\to S$, and set $S_\lambda=(C_\lambda)_{\mathfrak q_\lambda}$. These are local rings, and $R_\lambda\to S_\lambda$ is local because the maximal-ideal contractions agree. We verify the integer base and the permanence steps explicitly. A nonzero ideal of $\mathbf Z$ has a least positive member $d$. Repeated subtraction of $d$ writes any nonnegative member as $qd+r$ with $0\le r<d$; the remainder is in the ideal and minimality forces $r=0$. Negative members are handled by changing their sign. Thus every integer ideal is principal, including the zero ideal, so $\mathbf Z$ is Noetherian.

Each $A_\lambda$ is a quotient of a finite-variable polynomial ring over $\mathbf Z$, and the Hilbert basis theorem AG-CA-03, Theorem 2.1, makes that polynomial ring Noetherian. An ideal of a quotient is the image of its inverse-image ideal, so is finitely generated. An ideal of a localization equals the localization of its contraction: if $a/s$ is in the ideal, then $a/1$ is too, and the converse follows by multiplying by $1/s$. Its contracted ideal has finite generators, whose localized images generate the original ideal. These calculations prove quotient and localization permanence and make $R_\lambda,C_\lambda,S_\lambda$ Noetherian. Their finite polynomial lists and prime localizations give the two essential finite-type assertions; composition of such maps was fully proved in [F.31](#algebra-lemma-composition-essentially-of-finite-type).

Polynomial scalar extension gives $C_\lambda\otimes_{R_\lambda}R_\mu\cong C_\mu$. The tensor with $S_\lambda$ initially inverts the images of $C_\lambda\setminus\mathfrak q_\lambda$. Those images avoid $\mathfrak q_\mu$, by their definition as contractions from the same target. Thus $\mathfrak q_\mu$ defines a prime of that tensor localization. Localizing at it inverts the remaining elements outside $\mathfrak q_\mu$ and gives exactly $S_\mu$. The fraction universal property proves both inverse maps, establishing the stipulated transition formula. The identical argument with the final base $R$ gives $S$ as a prime localization of $S_\lambda\otimes_{R_\lambda}R$.

For the colimit of the target rings, every fraction in $S$ uses finitely many coefficients in its numerator and denominator, so it has a representative in some $S_\lambda$. If two representatives become equal in $S$, their cross difference is killed in $R[X]/(f)$ by a denominator outside $\mathfrak q$. Lift that denominator to a polynomial and express the killed difference as a finite sum $\sum_jh_jf_j$ in $R[X]$. These polynomials and their equality use finitely many coefficients. Put them into one common later $R_\mu$. The denominator still avoids $\mathfrak q_\mu$, and the same ideal-membership equality holds there, so the representatives are already equal in $S_\mu$. This proves injectivity as well as surjectivity of the colimit map. The structural maps from the base agree throughout, giving the entire claimed colimit of local ring maps. ∎

<a id="algebra-lemma-limit-module-essentially-finite-presentation"></a>

#### Lemma F.60: limit module essentially finite presentation

Reading source: [AI Integrated Stacks, pinned Algebra, lines 33804–33859](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L33804-L33859).

For a local essentially finitely presented map $R\to S$ and a finitely presented $S$-module $M$, the models in [F.59](#algebra-lemma-limit-essentially-finite-presentation) can be taken at sufficiently large stages with finitely presented $S_\lambda$-modules $M_\lambda$ such that
$$M_\lambda\otimes_{S_\lambda}S_\mu\cong M_\mu
\quad(\lambda\leq\mu),\qquad
\operatorname*{colim}_\lambda M_\lambda\cong M.$$
In particular each module is finite over its model algebra, and all base/prime-localization assertions of F.59 remain valid.

**Proof.** Choose a finite presentation
$$S^a\xrightarrow{H}S^b\longrightarrow M\longrightarrow0.$$
The finitely many entries of $H$ are elements of the colimit $S$. The representative proof in F.59 puts them in a common $S_{\lambda_0}$. Restrict to stages $\lambda\geq\lambda_0$ and let $H_\lambda$ be their images there. Define
$$M_\lambda=\operatorname{coker}
\bigl(S_\lambda^a\xrightarrow{H_\lambda}S_\lambda^b\bigr).$$
This is a finite presentation over $S_\lambda$. Right exactness of tensor and the fixed free bases identify the tensor of this presentation with the presentation given by $H_\mu$, proving the asserted transition isomorphism. The same calculation gives $M_\lambda\otimes_{S_\lambda}S\cong M$.

We verify the colimit explicitly. Any element of $M$ is represented by a vector in $S^b$, whose finitely many coordinates occur at a common model stage, giving surjectivity from the module colimit. If $x_\lambda\in S_\lambda^b$ represents a class that is zero in $M$, its image is $Hy$ for some finite vector $y\in S^a$. Choose a later stage representing every coordinate of $y$. The vector equality $x=Hy$ is a finite list of ring equalities, so F.59 detects all of them at one common successor. There $x_\mu=H_\mu y_\mu$, proving that the original class is zero in $M_\mu$. This proves injectivity of the colimit map. The representative and transition calculations respect addition and the ring actions, so the isomorphism is an isomorphism of modules over $\operatorname*{colim}S_\lambda=S$.

No ring models have been changed except for removing an initial segment of the directed set, which leaves all colimits unchanged: every earlier representative has an image at a common successor with $\lambda_0$. Hence their local maps, essential finite-type properties and prime tensor-localizations are exactly those proved in F.59. The arguments include $a=0$, $b=0$ and the zero module. ∎

<a id="algebra-lemma-local-dimension-zero-henselian"></a>

#### Lemma F.61: local dimension zero henselian

Reading source: [AI Integrated Stacks, pinned Algebra, lines 44097–44121](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L44097-L44121).

Every local ring $(R,\mathfrak m)$ of dimension zero is henselian. No Noetherian or nilpotent-maximal-ideal hypothesis is required.

**Proof.** The only prime of $R$ is $\mathfrak m$: any other prime is properly below the maximal ideal and would give a chain of length one. Every $u\in\mathfrak m$ is nilpotent. Indeed, if no power of $u$ were zero, $R_u$ would be nonzero. A maximal proper ideal of this ring exists by the chain-union and Zorn argument, and its inverse image would be a prime of $R$ avoiding $u$. It cannot be the unique prime $\mathfrak m$, a contradiction.

Use the simple-root definition of henselianity in [AG-CA-20, Section 1](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/AG-CA/henselian-local-rings-and-henselization.html). Let $f\in R[T]$ be monic, and let $\bar a$ be a root of its reduction with $\bar f'(\bar a)\ne0$. Choose any lift $a_0\in R$. The element $f'(a_0)$ is a unit because its residue is nonzero, and $\epsilon_0=f(a_0)\in\mathfrak m$ has some zero power $\epsilon_0^N=0$.

Inductively set
$$a_{j+1}=a_j-f'(a_j)^{-1}f(a_j).$$
Every $a_j$ has residue $\bar a$, so each inverse in this formula exists. Expanding the polynomial by the binomial formula gives, for all $a,h$,
$$f(a+h)=f(a)+f'(a)h+h^2Q(a,h)$$
for a polynomial $Q$ over $R$. Substitution of the correction therefore gives
$$f(a_{j+1})\in(f(a_j)^2)
\subset(\epsilon_0^{\,2^{j+1}}).$$
The correction remains in $\mathfrak m$, as needed for the residue induction. Choose $j$ with $2^j\geq N$; then $f(a_j)=0$. This supplies the required lifted root in finitely many steps, using only the nilpotence of the initial error.

For completeness it is unique with this residue. If $a,b$ are two such roots, polynomial subtraction factors as
$$0=f(b)-f(a)=(b-a)\bigl(f'(a)+(b-a)H(a,b)\bigr).$$
The second factor has the nonzero residue $\bar f'(\bar a)$ and is a unit, so $b=a$. All simple residue roots have thus been lifted, proving henselianity. ∎

<a id="algebra-lemma-local-syntomic"></a>

#### Lemma F.62: local syntomic

Reading source: [AI Integrated Stacks, pinned Algebra, lines 37927–37941](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L37927-L37941).

Let $R\to S$ be any ring map. If finitely many principal opens $D(g_i)$ cover $\operatorname{Spec}S$ and every $R\to S_{g_i}$ is syntomic, then $R\to S$ is syntomic.

**Proof.** The assumed cover means the $g_i$ generate the unit ideal. The whole finite-equation gluing proof [F.35](#algebra-lemma-cover-upstairs) gives finite presentation of $S/R$ from the chart finite presentations.

To prove flatness, take an arbitrary injection $M'\to M$ of $R$-modules and let $K$ be the kernel of $M'\otimes_RS\to M\otimes_RS$. Exactness of localization identifies $K_{g_i}$ with the kernel after tensoring with $S_{g_i}$; it is zero by chart flatness. If $x\in K$, some power $g_i^{e_i}$ kills $x$ for each $i$. These powers still generate the unit ideal: otherwise a maximal ideal containing all of them would contain all the $g_i$. A linear combination equal to one then kills $x$. Thus $K=0$, proving flatness without a finiteness condition on these modules.

For every $\mathfrak p\subset R$, put $C=S\otimes_R\kappa(\mathfrak p)$. The images of the $g_i$ still generate the unit ideal, and
$$C_{g_i}\cong S_{g_i}\otimes_R\kappa(\mathfrak p)$$
by the fraction universal property. Each is a local complete intersection over the field, by syntomicness of that chart. For a point of $C$, choose a chart containing it and then a global complete-intersection principal neighbourhood there. If that second denominator is $a/g_i^e$, its principal open in the chart is $D(g_i)\cap D(a)=D(g_i a)$ in $C$. Its coordinate algebra is exactly the same iterated localization. Thus these neighbourhoods give the required complete-intersection cover of the entire fibre, as in [F.2](#algebra-definition-lci-field). Finite presentation, flatness and all fibre conditions are now proved. If the cover is empty, its spectrum is empty and $S=0$; this algebra is finitely presented as $R/(1)$, flat, and has empty fibres, so the conclusion holds as well. ∎

<a id="algebra-lemma-localization-colimit"></a>

#### Lemma F.63: localization colimit

Reading source: [AI Integrated Stacks, pinned Algebra, lines 1260–1278](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L1260-L1278).

Let $U\subset R$ be multiplicative and $M$ an $R$-module. Then $U^{-1}M$ is a filtered colimit of copies of $M$ with transition maps given by multiplication by denominators. It is also the filtered colimit of the principal localizations $M_s$ for $s\in U$. In particular $U^{-1}R$ is the corresponding filtered colimit of the rings $R_s$.

**Proof.** We give a directed indexing set with specified transitions. Let $\Lambda$ be the finitely supported functions $\nu:U\to\mathbf N$, ordered coordinatewise, and put $s_\nu=\prod_{u\in U}u^{\nu(u)}$. For $\nu\leq\mu$, write
$$s_\mu=s_\nu v_{\nu\mu},\qquad
v_{\nu\mu}=\prod_{u\in U}u^{\mu(u)-\nu(u)}.$$
The maximum of two functions is a common successor. The displayed factor is specified even if the ring has zero divisors, and the factors multiply compatibly along three stages. Put one copy $M^{(\nu)}=M$ at each stage, with transition $m\mapsto v_{\nu\mu}m$.

The maps $M^{(\nu)}\to U^{-1}M$, $m\mapsto m/s_\nu$, commute with the transitions and are jointly surjective, since every denominator occurs as a one-element product. If $m/s_\nu=n/s_\mu$, the fraction criterion gives $u\in U$ with
$$u(s_\mu m-s_\nu n)=0.$$
At the successor $\rho=\nu+\mu+\delta_u$, both representatives have become equal, their difference being the left side of this identity. Here $\delta_u$ has value one at $u$ and zero elsewhere. Conversely equality at any successor gives equality of the fractions. This proves bijectivity. To check addition, move two representatives to a common successor; addition there becomes the usual common-denominator addition. Scalar multiplication is preserved by every map, so the bijection is an $R$-module isomorphism.

For the principal-localization assertion use the same directed set, now with modules $M_{s_\nu}$. If $\nu\leq\mu$, $s_\nu$ is a unit after inverting $s_\mu=s_\nu v_{\nu\mu}$: its inverse is $v_{\nu\mu}/s_\mu$. This gives the specified localization map. Each fraction in $U^{-1}M$ is represented at a principal stage. If $m/s_\nu^a$ and $n/s_\mu^b$ become equal in the full localization, some $u\in U$ kills their cross difference
$$u(s_\mu^b m-s_\nu^a n)=0.$$
At the principal successor $s_\rho=s_\nu s_\mu u$, all three factors are units. The identity therefore makes the two fractions equal there. This proves both directions of the colimit isomorphism, including all module operations.

Taking $M=R$, these transition maps are ring maps. The same fraction calculation preserves multiplication and one, proving the ring colimit. These diagrams represent the usual directed family of principal localizations: each product is itself in $U$, and any finite family of its elements is inverted at their product. The argument includes $0\in U$, in which case every representative vanishes at a successor containing that denominator. ∎

<a id="algebra-lemma-localization-smooth-separable"></a>

#### Lemma F.64: localization smooth separable

Reading source: [AI Integrated Stacks, pinned Algebra, lines 46075–46088](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L46075-L46088).

A finitely generated field extension $K/k$ is separably generated if and only if it is the fraction field of a smooth finite-type $k$-domain.

**Proof.** For the forward direction choose a finite separating transcendence basis $T_1,\ldots,T_d$, set $F=k(T_1,\ldots,T_d)$, and write the remaining finite separable extension as a finite tower
$$F=K_0\subset K_1\subset\cdots\subset K_r=K,\qquad K_i=K_{i-1}(y_i).$$
A finite field-generating list gives such a tower; each step is separable. Let its monic minimal polynomial have degree $e_i$. Successive monic division makes the products $y_1^{a_1}\cdots y_{i-1}^{a_{i-1}}$, with $0\leq a_j<e_j$, a basis of $K_{i-1}$ over $F$. Express every coefficient of the next minimal polynomial in this basis. There are only finitely many coefficients and basis vectors in the entire tower. One nonzero polynomial $h\in k[T_1,\ldots,T_d]$ clears every rational-function denominator.

Put $R_0=k[T_1,\ldots,T_d,1/h]$. The coefficient expressions give successive monic equations $F_i$ in $R_0[Y_1,\ldots,Y_i]$. Define
$$C_i=R_0[Y_1,\ldots,Y_i]/(F_1,\ldots,F_i).$$
Monic polynomial division, applied successively, makes the same standard monomials an $R_0$-basis of $C_i$. Tensoring with $F$ gives exactly $K_i$. Since $R_0$ is a domain and these modules are free, their maps to their tensors with $F$ are injective. Thus each $C_i$ is an actual subdomain of $K_i$.

The derivative $\delta_i=(\partial F_i/\partial Y_i)(y_1,\ldots,y_i)$ is nonzero in $K_i$, by separability of its minimal polynomial. Form the successive rings
$$D_0=R_0,\qquad
D_i=(D_{i-1}[Y_i]/(F_i))_{\delta_i}.$$
Here the coefficient expressions are mapped from the preceding $C_{i-1}$, and all previously inverted derivatives remain inverted. Inductively $D_i$ is the corresponding localization of $C_i$, so is a domain in $K_i$. Each map $D_{i-1}\to D_i$ is a standard étale one-equation map, with monic equation and inverted derivative. The entire AG-CA-17, Proposition 6.1 proves its unique square-zero lifts. The polynomial, localization and composition proofs in its Theorem 1.2 make $D_r$ formally smooth over $k$. All equations, variables and inverses are finite in number, so it is finitely presented, hence smooth. It contains every $T_j$ and $y_i$, and lies in $K$, so its fraction field is exactly $K$. Empty towers have no derivatives to invert and give the same construction.

Conversely let $C$ be a smooth finite-type $k$-domain with fraction field $K$. Choose a nonzero principal standard smooth chart $D$ by the entire AG-CA-17, Theorem 5.1. Its fraction field remains $K$. Reorder the variables of this finite polynomial presentation so the invertible square Jacobian minor uses the pivot variables, and call the remaining variables $U_1,\ldots,U_t$. With $B_0=k[U_1,\ldots,U_t]$, the identical chart is a finitely presented algebra over $B_0$ with only the pivot variables and an invertible full square Jacobian. The explicit square-zero equation correction of AG-CA-17, Theorem 4.1, gives a unique lift: the square invertible matrix solves the error vector uniquely. Thus $B_0\to D$ is étale. The whole arbitrary-base flatness proof AG-CA-18, Corollary 6.2 makes it flat.

This structural map from $B_0$ is injective. For $0\ne b\in B_0$, multiplication by $b$ is injective on the polynomial domain. Flat tensor with $D$ preserves this injection. If $b$ had zero structural image, that map on the nonzero ring $D$ would be zero, a contradiction. Consequently the $U_j$ are algebraically independent in $K$.

Localize this base at its nonzero elements, obtaining $F_0=k(U_1,\ldots,U_t)$. The domain $D\otimes_{B_0}F_0$ is nonzero and étale over $F_0$, by the full base-change proof of AG-CA-17, Theorem 1.2. Its entire Theorem 7.2 classifies it as a finite product of finite separable extensions of $F_0$. A nonzero domain has no nontrivial orthogonal idempotents, so this product has exactly one factor. It is therefore a finite separable field. It contains $D$ and lies in $K$; every nonzero element of $D$ is invertible in this field. Hence the field is precisely $K$. Thus the independent $U_j$ form a separating transcendence basis, proving the converse at every characteristic, without using F.91. ∎

<a id="algebra-lemma-localize-NL"></a>

#### Lemma F.65: localize NL

Reading source: [AI Integrated Stacks, pinned Algebra, lines 37118–37133](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L37118-L37133).

For any ring map $A\to B$ and multiplicative subset $U\subset B$, the canonical map
$$\operatorname{NL}_{B/A}\otimes_B U^{-1}B
\longrightarrow \operatorname{NL}_{U^{-1}B/A}$$
is a quasi-isomorphism.

**Proof.** Use the directed principal-localization diagram constructed in [F.63](#algebra-lemma-localization-colimit), with stages $B_{s_\nu}$ and colimit $U^{-1}B$. At every stage the whole calculation [F.72](#algebra-lemma-principal-localization-NL) gives a homotopy equivalence
$$\operatorname{NL}_{B/A}\otimes_B B_{s_\nu}
\longrightarrow\operatorname{NL}_{B_{s_\nu}/A}.$$
These are the canonical maps induced by $B\to B_{s_\nu}$; they are compatible with later localizations. Presentation comparisons and their explicit homotopies are proved in [F.11](#algebra-lemma-NL-homotopy). No compatible choice of the individual contracting homotopies is needed for the induced homology maps.

Tensor commutes with this colimit term by term: a tensor is a finite sum of pure tensors, and each coefficient has a common-stage representative; its balancing relations and equalities hold at a later stage. The right side has colimit $\operatorname{NL}_{U^{-1}B/A}$ by the complete canonical-presentation proof [F.24](#algebra-lemma-colimits-NL).

Finally filtered colimits commute with homology here. A cycle in either colimit has a stage representative; its differential is zero at some later stage, giving a cycle there. If its homology class vanishes, it is the differential of a representative vector in the colimit. Put the two representatives and their equality at one common successor to obtain a boundary there. This proves both directions of the homology-colimit isomorphism. The stage maps induce isomorphisms in degrees one and zero, so their colimit does too. All other homology groups vanish since these complexes have only two terms. This proves the claimed quasi-isomorphism, without a Noetherian or finite-generation hypothesis on $U$. The zero localization is included in the same diagrams. ∎

<a id="algebra-lemma-localize-relative-complete-intersection"></a>

#### Lemma F.66: localize relative complete intersection

Reading source: [Stacks, Tag 00ST](https://stacks.math.columbia.edu/tag/00ST).

Let $R$ be Noetherian and put $S=R[X_1,\ldots,X_n]/(f_1,\ldots,f_c)$. In each situation below there are $g\in S$ and a polynomial lift $h$ of $g$ for which
$$S_g=R[X_1,\ldots,X_n,T]/(f_1,\ldots,f_c,hT-1)$$
is a relative global complete intersection as defined in [F.4](#algebra-definition-relative-global-complete-intersection).

1. If every nonempty fibre over $V(I)$, for an ideal $I\subset R$, has dimension $n-c$, one may require $g\equiv1\pmod{IS}$.
2. If the fibre over $\mathfrak p\in\operatorname{Spec}R$ has dimension $n-c$, one may require the image of $g$ in that fibre to be a unit.
3. If a point $\mathfrak q$ of the fibre over $\mathfrak p$ has fibre point-dimension $n-c$, one may require $g\notin\mathfrak q$.

**Proof.** Set $d=n-c$. The neighbourhood bound proved in [F.39](#algebra-lemma-dimension-fibres-bounded-open-upstairs) gives, around every point whose fibre point-dimension is at most $d$, a principal neighbourhood on which every fibre point-dimension is at most $d$. The union of these neighbourhoods is an open $W$ with that same bound. Each of its nonempty fibres has dimension at most $d$: a finite-type field fibre is Noetherian, and its component dimensions are its point-dimensions at the corresponding generic points, as in [F.20](#algebra-lemma-codimension). Open subsets retain this bound.

In case (1) choose $W$ containing $V(IS)$; each point of those fibres has point-dimension at most their assumed dimension. Write the closed complement of $W$ as $V(J)$ in $\operatorname{Spec}S$. The equality $V(J+IS)=\varnothing$ implies $J+IS=S$: a proper ideal would be contained in a maximal, hence prime, ideal. Write $1=g+b$ with $g\in J$ and $b\in IS$. Then $g\equiv1\pmod{IS}$, and $D(g)\subset W$.

In case (2) take $W$ containing the entire indicated fibre, and again write its complement as $V(J)$. If $k=\kappa(\mathfrak p)$, the image ideal $J(S\otimes_R k)$ is the unit ideal. Choose a finite expression $1=\sum_j\beta_j\bar g_j$, where $g_j\in J$. Each $\beta_j$ is represented in $S_{R\setminus\mathfrak p}/\mathfrak pS_{R\setminus\mathfrak p}$. Clear their finitely many denominators to obtain $b_j\in S$ and $s\in R\setminus\mathfrak p$ with $\beta_j=\bar b_j/\bar s$. Thus $g=\sum_j b_jg_j\in J$ has fibre image $\bar s$, a unit. Again $D(g)\subset W$.

In case (3), one of the principal neighbourhoods supplied directly by F.39 is $D(g)$ with $g\notin\mathfrak q$ and the required upper bound. In all three cases select any polynomial lift $h$ of $g$. Adjoining the inverse of $h$ gives the presentation in the statement, by the explicit substitution $T\mapsto g^{-1}$ and its inverse. Every nonempty fibre of this presentation has dimension at least
$$ (n+1)-(c+1)=d.$$
Indeed, in its polynomial ring over the residue field a minimal prime over $c+1$ equations has height at most $c+1$, by AG-CA-11, Theorem 3.1; AG-CA-09, Theorem 4.3 gives that component dimension as $n+1$ minus its height. The upper bound on $D(g)$ makes the dimension exactly $d$. This proves the relative global complete-intersection assertion, without presupposing flatness; its flatness is subsequently proved in F.77. Empty fibres impose no dimension test, and a zero localization is included. ∎

<a id="algebra-lemma-locally-smooth"></a>

#### Lemma F.67: locally smooth

Reading source: [Stacks, Tag 00TC](https://stacks.math.columbia.edu/tag/00TC).

For any ring map $R\to S$, smoothness is equivalent to the existence, around every prime of $S$, of a principal localization that is smooth over $R$.

**Proof.** Use the finite-presentation and cotangent-complex definition [F.6](#algebra-definition-smooth). If $S/R$ is smooth, then $S_g$ is finitely presented by adjoining an inverse variable. The exact calculation [F.72](#algebra-lemma-principal-localization-NL), together with the presentation comparison [F.11](#algebra-lemma-NL-homotopy), identifies its conormal complex with the localized complex plus a contractible summand. Its first homology is zero and its differential module is the localization of a finite projective module. Localization keeps the splitting of a finite free module, so that module is still finite projective. Thus $S_g/R$ is smooth.

For the converse, the elements defining the given neighbourhoods generate the unit ideal: otherwise a maximal ideal containing them would be an uncovered prime. A finite expression for $1$ gives a cover by $D(g_1),\ldots,D(g_r)$. The complete gluing proof [F.35](#algebra-lemma-cover-upstairs) makes $S/R$ finitely presented. Fix $S=R[X_1,\ldots,X_n]/I$ with $I$ finite. For this presentation set
$$K=\ker(I/I^2\xrightarrow{d}S^n),\qquad M=\operatorname{coker}(I/I^2\xrightarrow{d}S^n)=\Omega_{S/R}.$$
The derivatives of a finite list generating $I$ generate the image of $d$, so $M$ is finitely presented. Exact localization and F.72/F.11 identify $K_{g_i}$ with the zero first homology of each smooth chart. The power-annihilator module calculation in F.35 therefore gives $K=0$.

It remains to produce a global projective splitting for $M$. Write $\pi:S^n\twoheadrightarrow M$. On each chart $M_{g_i}$ is finite projective. A section $s_i$ of $\pi_{g_i}$ exists: write that projective module as a summand of a finite free module, lift the free basis through $\pi_{g_i}$, and restrict the resulting lift to the summand.

For a finitely presented module, localization of $\operatorname{Hom}_S(M,S^n)$ is $\operatorname{Hom}_{S_{g_i}}(M_{g_i},S_{g_i}^n)$. Indeed a finite presentation of $M$ identifies both modules with the kernel of the same matrix between finite powers of $S^n$, and localization is exact. Clear the denominator of $s_i$ to obtain $t_i:M\to S^n$ whose localized composite is $g_i^{a_i}1_M$. The error $\pi t_i-g_i^{a_i}1_M$ vanishes on a finite generating list after localization. A further common power of $g_i$ kills those finitely many errors. After multiplying $t_i$ by that power, we have an actual equality
$$\pi t_i=g_i^{e_i}1_M.$$
Increase $e_i$ to a positive integer if needed. These powers generate $1$: expand a finite unit expression in the $g_i$ to exponent $1+\sum_i(e_i-1)$; every monomial contains one of the required powers. Choose $c_i$ with $\sum_i c_ig_i^{e_i}=1$. Then $t=\sum_i c_it_i$ satisfies $\pi t=1_M$. Thus $S^n=t(M)\oplus\ker\pi$, with both summands generated by projections of its finite basis. This proves finite projectivity of $M$ directly.

We have proved finite presentation, zero first cotangent homology and finite projective differentials, exactly F.6. If $S=0$, its finite presentation is $R/(1)$ and both cotangent modules are zero, so the conclusion also holds for the empty spectrum. No Noetherian hypothesis is needed. ∎

<a id="algebra-lemma-make-etale-map-prescribed-residue-field"></a>

#### Lemma F.68: make etale map prescribed residue field

Reading source: [AI Integrated Stacks, pinned Algebra, lines 41287–41319](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L41287-L41319).

Let $\mathfrak p$ be a prime of a ring $R$, and let $L/\kappa(\mathfrak p)$ be finite separable. There are a finitely presented étale $R$-algebra $R'$ and a prime $\mathfrak p'$ over $\mathfrak p$ with an isomorphism $\kappa(\mathfrak p')\cong L$ respecting the given residue-field extension.

**Proof.** Choose a finite field-generating list $\alpha_1,\ldots,\alpha_r$ for $L/\kappa(\mathfrak p)$, for example a vector-space basis. Put $E_0=\kappa(\mathfrak p)$ and $E_i=E_{i-1}(\alpha_i)$. Each step is finite separable: the minimal polynomial over $E_{i-1}$ divides a separable polynomial over $E_0$ and therefore has no repeated root.

Inductively construct a finitely presented étale $R$-algebra $A_i$ with a prime $\mathfrak q_i$ and a compatible identification $\kappa(\mathfrak q_i)=E_i$. Start with $A_0=R$ and $\mathfrak q_0=\mathfrak p$. Suppose the preceding stage is constructed, and write $A=A_{i-1}$, $\mathfrak q=\mathfrak q_{i-1}$. Let
$$\bar F_i(T)=T^{e_i}+\sum_{j<e_i}\bar a_jT^j\in E_{i-1}[T]$$
be the monic minimal polynomial of $\alpha_i$. The residue map $A_{\mathfrak q}\to E_{i-1}$ is surjective, so lift each $\bar a_j$ as a fraction $a_j/s_j$ with $s_j\notin\mathfrak q$. The product $h=\prod_j s_j$ is outside $\mathfrak q$, and all these lifts belong to the single principal localization $A_h$. They give a monic polynomial $F_i\in A_h[T]$. Set
$$A_i=(A_h[T]/(F_i))_{F_i'}.$$
Its defining equation has an invertible derivative. The full one-equation square-zero correction AG-CA-17, Proposition 6.1 makes this map étale. Principal localization is formally étale by its Theorem 1.2 and finitely presented by its inverse-variable equation. Finite composition, with the equation substitution proof [F.28](#algebra-lemma-compose-finite-type), therefore makes $A_i/R$ finitely presented and étale.

Evaluation at $T=\alpha_i$ defines a ring map $A_i\to E_i$: its derivative has nonzero value by separability, so its inverse can be evaluated. Let $\mathfrak q_i$ be the kernel. It is prime, and its contraction to $A$ is exactly $\mathfrak q$, since the restriction is the given residue map and $h$ has nonzero residue.

To compute its residue field, let $D_i$ be the image of $A_i$ in $E_i$. It is a domain, and $A_i/\mathfrak q_i=D_i$. The fraction field of the image of $A_h$ is $E_{i-1}$: this image is $(A/\mathfrak q)_h$, and localization does not change its fraction field $\kappa(\mathfrak q)$. Thus $\operatorname{Frac}D_i$ contains $E_{i-1}$ as well as $\alpha_i$, and so contains $E_i=E_{i-1}(\alpha_i)$. It lies inside $E_i$, giving equality. Localization at the kernel identifies
$$\kappa(\mathfrak q_i)=\operatorname{Frac}(A_i/\mathfrak q_i)
=\operatorname{Frac}D_i=E_i.$$
This uses the fraction field of the image; it does not require the evaluation map itself to be onto the field.

Continue through the finite tower. Taking $R'=A_r$ and $\mathfrak p'=\mathfrak q_r$ gives the required extension and prime, with all residue identifications commuting with the original map from $R$. For the trivial extension the empty tower gives $R'=R$ and $\mathfrak p'=\mathfrak p$. ∎

<a id="algebra-lemma-make-separably-generated"></a>

#### Lemma F.69: make separably generated

Reading source: [AI Integrated Stacks, pinned Algebra, lines 10182–10253](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L10182-L10253).

For any finitely generated field extension $K/k$, there is a commutative square of inclusions
$$
\begin{array}{ccc}
K&\longrightarrow&K'\\
\uparrow&&\uparrow\\
k&\longrightarrow&k'
\end{array}
$$
in which $k'/k$ and $K'/K$ are finite purely inseparable and $K'/k'$ is separably generated.

**Proof.** Choose a finite field-generating list and a maximal algebraically independent sublist $T_1,\ldots,T_d$. Every remaining generator is algebraic over $F=k(T_1,\ldots,T_d)$: a polynomial dependence using that generator has a nonzero coefficient after substituting the independent $T_j$. A finite algebraic generator tower is finite. At each step, division by the monic minimal polynomial gives a power basis; multiplication of these bases gives a basis of the whole tower, since grouping a relation by the powers of the last generator proves independence inductively. Thus $K/F$ is finite. In characteristic zero its irreducible polynomials have nonzero derivatives, so every tower step is separable. The entire separable-tower proof AG-CA-17, Lemma 7.1 gives the result with $k'=k$ and $K'=K$.

Assume now characteristic $p>0$. We first prove the finite-extension facts used in the construction. For a finite extension $E/F$, the elements separable over $F$ form a subfield $E_s$. Indeed if $x,y$ are separable, the minimal polynomial of $y$ over $F(x)$ divides its separable polynomial over $F$. The two separable steps and the same complete separable-tower proof make every element of $F(x,y)$ separable over $F$. This proves closure under sums, products and inverses. As a subspace of the finite-dimensional $F$-space $E$, this field is finite over $F$.

If $x\in E$ has irreducible minimal polynomial $f$, repeatedly remove zero derivatives to write
$$f(X)=g(X^{p^e}),\qquad g'\ne0.$$
This process terminates as degrees decrease; $g$ is irreducible because a factorization would substitute to one of $f$. Its derivative has smaller degree, so the Euclidean algorithm gives $\gcd(g,g')=1$. Hence $x^{p^e}$ is separable over $F$ and lies in $E_s$. A common exponent for a finite field-generating list makes every $p^e$th power from $E$ belong to $E_s$: apply Frobenius to its rational expressions. Thus $E/E_s$ is purely inseparable.

We will use the degree calculation without an external $p$-basis result. If $\beta^p\in H$ but $\beta\notin H$, its minimal polynomial over $H$ divides $X^p-\beta^p=(X-\beta)^p$ in a field containing $\beta$. A monic proper nonconstant factor of degree $r<p$ has coefficient $-r\beta$ at degree $r-1$. Since $r$ is nonzero in the field, a factor over $H$ would force $\beta\in H$, a contradiction. The minimal polynomial therefore has degree $p$. By adjoining the powers of each purely inseparable generator in reverse order, starting from a power in the base, each nontrivial step has this degree. Multiplication of the power bases shows that every finite purely inseparable degree is a power of $p$.

Apply these facts to $K/F$, and call its separable subfield $K_s$. Prove the desired assertion by strong induction on $m=[K:K_s]$, for all finitely generated extensions with their chosen transcendence bases. If $m=1$, the chosen $T_j$ already separate $K/k$. If $m>1$, choose $x\in K\setminus K_s$ and the least $e\geq1$ with $x^{p^e}\in K_s$. Put
$$\beta=x^{p^{e-1}},\qquad \alpha=\beta^p\in K_s.$$
Then $\beta\notin K_s$. The degree calculation gives $[K_s(\beta):K_s]=p$ and $[K:K_s(\beta)]=m/p$.

Let
$$P(X)=X^n+\sum_{i<n}a_iX^i\in F[X]$$
be the separable minimal polynomial of $\alpha$. Write all $a_i$ as rational functions in $T$, and list the finitely many coefficients of $k$ occurring in their numerators and denominators. Adjoin their $p$th roots compatibly over $K$, one at a time. Such a root exists in a field extension: take the quotient by an irreducible factor of $X^p-c$. The quotient is a field by the Euclidean algorithm. A root is unique in any common extension, since $(u-v)^p=u^p-v^p$. All old fields therefore remain embedded in these successive root fields. Let $k_1$ be the field generated by these roots over $k$. It is finite purely inseparable, and $k_1^p\subset k$, since taking the $p$th power of any rational expression puts all its coefficients and generators in $k$.

In the same compatible extension adjoin $U_j$ with $U_j^p=T_j$. They are algebraically independent over $k_1$: a nonzero polynomial relation would, after taking its $p$th power, be a nonzero relation among the $T_j$ over $k$. Its coefficients remain nonzero under Frobenius. Put
$$F_1=k_1(U_1,\ldots,U_d),\qquad L=KF_1.$$
This gives the actual commuting intermediate field square. The extension $L/K$ is finite and purely inseparable; it adjoins finitely many roots with $p$th powers in $K$. The $p$th power of any rational expression in them lies in $K$.

Take coefficientwise $p$th roots of the chosen numerator and denominator for each $a_i$, and substitute the $U_j$. This gives $b_i\in F_1$ with $b_i^p=a_i$. The denominator is nonzero because its $p$th power is the original nonzero denominator. Define
$$Q(X)=X^n+\sum_{i<n}b_iX^i,\qquad Q(X)^p=P(X^p).$$
Then $Q(\beta)^p=P(\alpha)=0$, so $Q(\beta)=0$. The derivative calculation, using $i^p=i$ in the prime field, gives
$$Q'(\beta)^p=P'(\alpha)\ne0.$$
Write $Q=hq$ with $h$ the minimal polynomial of $\beta$ over $F_1$. Evaluation of $Q'=h'q+hq'$ at $\beta$ implies $h'(\beta)q(\beta)\ne0$. Thus $h$ is separable, and $\beta$ is separable over $F_1$.

Every separable polynomial remains square-free after a field extension: its Euclidean identity with its derivative remains an identity equal to one after extending coefficients. The minimal polynomial of a generator after base change divides that polynomial and is therefore separable too. A finite generating tower for $K_s/F$ consequently gives a separable tower for $K_sF_1/F_1$. The minimal polynomial of the now separable $\beta$ over this larger field divides its separable polynomial over $F_1$, so this final step is separable as well. The separable-tower proof gives
$$H=K_s(\beta)F_1\subset L_s,$$
where $L_s$ denotes the separable subfield of the finite extension $L/F_1$.

To bound its remaining inseparable degree, take a basis of $K$ over $K_s(\beta)$ of size $m/p$ and span it over $H$ inside $L$. This span contains $K$ and $H$, contains one, and is closed under multiplication, since the basis-product coefficients belong to $K_s(\beta)\subset H$. It is a finite-dimensional domain over $H$, hence a field: nonzero multiplication is injective, therefore surjective, and supplies an inverse. It contains $F_1$ and $K$, so equals $L$. Consequently
$$[L:L_s]\leq[L:H]\leq m/p<m.$$
Also $L/F_1$ is finite, by the same spanning argument starting with a basis of $K/F$. The $U_j$ are a transcendence basis for the finitely generated extension $L/k_1$. Strong induction thus applies to this precise new data, giving finite purely inseparable $k_2/k_1$ and $L'/L$ with $L'/k_2$ separably generated.

Finally finite purely inseparable extensions compose: for each element of $L'$, a $p$-power lies in $L$ and a further $p$-power lies in $K$. The same argument applies to $k_2/k$. Finiteness follows by multiplying their finite tower degrees. Taking $K'=L'$ and $k'=k_2$ gives the asserted square. Empty transcendence bases, trivial adjunctions and the base case are all included. ∎

<a id="algebra-lemma-matrix-left-inverse"></a>

#### Lemma F.70: matrix left inverse

Reading source: [Stacks, Tag 07DQ](https://stacks.math.columbia.edu/tag/07DQ).

Let \(A\) be an \(n\times m\) matrix over a commutative ring \(R\), where \(0\leq m\leq n\), and let \(J\) be the ideal of its maximal minors. Every \(f\in J\) has an \(m\times n\) matrix \(B\) with \(BA=f1_m\). Conversely, existence of such a \(B\) implies \(f^m\in J\).

**Proof.** For an increasing \(m\)-element subset \(I\) of \(\{1,\ldots,n\}\), let \(E_I\) select those coordinates from \(R^n\), and put \(A_I=E_IA\). Its determinant is the corresponding minor. By the complete cofactor calculation in [F.19](#algebra-lemma-charpoly),
\[
\operatorname{adj}(A_I)E_IA=(\det A_I)1_m.
\]
Thus, from an expression \(f=\sum_I c_I\det A_I\), the finite sum
\[
B=\sum_I c_I\operatorname{adj}(A_I)E_I
\]
constructs the required matrix.

For the converse, here is the determinant product calculation. Expand each column of \(BA\) as the linear combination of columns of \(B\) whose coefficients are entries of that column of \(A\). Multilinearity follows directly from the determinant permutation formula. A term choosing the same column twice is zero by the equal-column cancellation. For any fixed set \(I\) of distinct chosen columns, order those indices increasingly. Reordering them in all possible ways contributes their permutation signs; the signed sum of their coefficient products is exactly \(\det A_I\). The remaining column determinant is \(\det B^I\), where \(B^I\) uses the columns indexed by \(I\). Consequently
\[
\det(BA)=\sum_{|I|=m}(\det B^I)(\det A_I)\in J.
\]
When \(BA=f1_m\), its determinant is \(f^m\). This proves the converse over arbitrary rings, including rings with nilpotents. If \(m=0\), the sole minor is the empty determinant \(1\), so \(J=R\). The unique map to and from the zero module supplies the first assertion, and \(f^0=1\in J\) supplies the second. ∎

<a id="algebra-lemma-presentation-sym-exterior"></a>

#### Lemma F.71: presentation sym exterior

Reading source: [Stacks, Tag 00DO](https://stacks.math.columbia.edu/tag/00DO). The quotient maps and both kernels are proved below.

For an exact sequence \(M_2\xrightarrow{u}M_1\xrightarrow{v}M\to0\) of modules over any commutative ring and every integer \(n\geq1\), there are exact sequences
\[
M_2\otimes_R\operatorname{Sym}^{n-1}M_1
\longrightarrow\operatorname{Sym}^nM_1
\longrightarrow\operatorname{Sym}^nM\longrightarrow0,
\]
\[
M_2\otimes_R\bigwedge^{n-1}M_1
\longrightarrow\bigwedge^nM_1
\longrightarrow\bigwedge^nM\longrightarrow0.
\]
The first maps multiply, respectively wedge, with \(u(x)\); the second maps apply \(v\) to every factor. In degree zero both second maps are the identity of \(R\), so both kernels are zero.

**Proof.** Put \(N=\operatorname{im}u\), so exactness identifies \(M=M_1/N\). Construct the tensor algebra \(T(M_1)=\bigoplus_{d\geq0}M_1^{\otimes d}\) with multiplication by concatenation. Balancing in each tensor factor makes that product well defined. Its symmetric quotient imposes \(xy=yx\) for degree-one generators; its exterior quotient imposes \(x^2=0\) for every degree-one generator. In the latter quotient, expanding \((x+y)^2=0\) gives \(xy=-yx\) over every ring, including characteristic two.

In either algebra let \(L\) be the two-sided homogeneous ideal generated by the degree-one image of \(N\). The factorwise map to the corresponding algebra of \(M_1/N\) is onto: every pure tensor in the target lifts, and pure tensors generate each degree. It kills \(L\). Its inverse on the quotient is explicit. Send a class \(\bar x\in M_1/N\) to the class of any lift \(x\) in the source algebra modulo \(L\). Another lift differs by an element of \(N\), hence gives the same class. This map is linear, so its products extend to the tensor algebra by the tensor balancing relations. Those products obey commutation, respectively square-zero, relations in the indicated quotient; it therefore descends to the symmetric, respectively exterior, algebra. The two composites fix every degree-one generator and the scalar ring, hence every product and sum of generators. They are inverse graded algebra maps.

It remains to identify the degree-\(n\) part of \(L\). It is spanned by products having one selected factor in \(N\), since those generate the ideal and all factors have nonnegative degree. In the symmetric case move that factor to the front by commutation. In the exterior case move it to the front using \(xy=-yx\), retaining the resulting sign. Every remaining product has degree \(n-1\). Thus that part is exactly the image of \(N\otimes_R\operatorname{Sym}^{n-1}M_1\), respectively \(N\otimes_R\bigwedge^{n-1}M_1\), under multiplication. Each selected element of \(N\) lifts through \(u\), so these are also the images of the stated maps from \(M_2\). The inverse quotient maps just constructed prove that these images are exactly the kernels. The ideal has no degree-zero part, proving the separate degree-zero assertion. No module is assumed finite or free. ∎

<a id="algebra-lemma-principal-localization-NL"></a>

#### Lemma F.72: principal localization NL

Reading source: [AI Integrated Stacks, pinned Algebra, lines 37031–37116](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L37031-L37116).

Let $A\to B$ be a ring map, $g\in B$, and $P\twoheadrightarrow B$ a polynomial presentation over $A$ with kernel $I$. Choose $f\in P$ mapping to $g$. The map $P[X]\to B_g$ extending the presentation and sending $X$ to $g^{-1}$ has kernel $J=(I,fX-1)$, and:

1. $J/J^2\cong(I/I^2)_g\oplus B_g[fX-1]$.
2. $\Omega_{P[X]/A}\otimes_{P[X]}B_g\cong(\Omega_{P/A}\otimes_PB_g)\oplus B_g\,dX$.
3. The two-term conormal complex is isomorphic to
$$\operatorname{NL}(P\to B)\otimes_BB_g
\oplus(B_g\xrightarrow{g}B_g).$$

Consequently the canonical map $\operatorname{NL}_{B/A}\otimes_BB_g\to\operatorname{NL}_{B_g/A}$ is a homotopy equivalence.

**Proof.** The inverse-variable universal property gives
$$P[X]/(I,fX-1)=B[X]/(gX-1)\cong B_g,$$
including a nilpotent $g$, when the last ring is zero. Put $q=gX-1\in B[X]$. Multiplication by $q$ is injective: if a polynomial has lowest nonzero coefficient at degree $j$, the product's coefficient at that degree is its negative. Thus the map
$$B[X]/(q)\longrightarrow(q)/(q^2),\quad [a]\longmapsto[aq]$$
is an isomorphism. It is surjective by the definition of the principal ideal, and $aq=bq^2$ implies $a=bq$ by the proved multiplication injection. Therefore $(q)/(q^2)$ is free of rank one over $B_g$, with the indicated generator, also when both modules are zero.

Reduction modulo $I$ gives an exact sequence
$$ (I/I^2)\otimes_BB_g\longrightarrow J/J^2
\longrightarrow(q)/(q^2)\longrightarrow0.$$
For exactness in the middle, if an element of $J$ becomes a multiple of $q^2$, lift its coefficient to $P[X]$ and subtract that coefficient times $(fX-1)^2$. The remainder lies in $IP[X]$. Its class modulo $J^2$ is a finite sum of classes of elements of $I$, with coefficients evaluated in $B_g$. This is exactly the image of the left map.

That map is injective and has a retraction. Define
$$\pi:P[X]\longrightarrow(P/I^2)_f,\qquad X\longmapsto f^{-1}.$$
It maps $J$ into the square-zero ideal $I_f/I_f^2$ and maps $J^2$ to zero. The target ideal is naturally $(I/I^2)\otimes_BB_g$: the action factors through $B_g$, and localization commutes with the quotient and square by its exact fraction identities. Hence $\pi$ induces a $B_g$-linear map from $J/J^2$ to this module. On the left map its composite is the identity, proving injectivity. It kills $[fX-1]$, whose image generates the right quotient. Lifting a right-quotient coefficient by $a[fX-1]$, for $a\in B_g$, gives the asserted direct sum and proves (1).

For (2), derivations out of $P[X]$ are uniquely a derivation out of $P$ together with the chosen value of $X$. This proves the differential direct sum by the universal property, and tensoring yields the displayed formula.

Write $E=\Omega_{P/A}\otimes_PB_g$. On the first summand the conormal differential is the original $[a]\mapsto da$. On the new generator it is
$$d(fX-1)=g^{-1}df+g\,dX
=g\bigl(dX+g^{-2}df\bigr).$$
Changing the new differential generator from $dX$ to $w=dX+g^{-2}df$ is invertible, with inverse $dX=w-g^{-2}df$. It leaves $E$ fixed. The two direct sums now identify the entire differential with the old conormal differential plus multiplication by $g$, proving (3).

The new summand is contractible: multiplication by $g^{-1}$ from degree zero to degree one has both composites with its differential equal to the identity. Inclusion of the old summand and projection onto it therefore have composite identity there, and their other composite differs from identity by this explicit homotopy. They are homotopy inverses. The inclusion is precisely the map induced by $P\to P[X]$ and $B\to B_g$. The full presentation comparison [F.11](#algebra-lemma-NL-homotopy) identifies it with the stated canonical map. The argument uses neither a nonnilpotence assumption on $g$ nor a proper regular-sequence condition. ∎

<a id="algebra-lemma-product-local"></a>

#### Lemma F.73: product local

Reading source: [AI Integrated Stacks, pinned Algebra, lines 13035–13062](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L13035-L13062).

If a ring $R$ has finitely many maximal ideals and locally nilpotent Jacobson radical, every prime is maximal and the natural map to the product of the corresponding localizations is an isomorphism.

**Proof.** Write the distinct maximal ideals as $\mathfrak m_1,\ldots,\mathfrak m_r$, and put $J=\bigcap_i\mathfrak m_i$. Each element of $J$ is nilpotent. Any prime contains $J$, hence contains $\mathfrak m_1\cdots\mathfrak m_r\subset J$. If it contained none of the factors, choosing one element outside the prime from each factor would give a product outside the prime, a contradiction. It therefore equals one of the maximal ideals.

The maximal ideals are pairwise comaximal. For two comaximal ideals $A,B$, choose $a\in A,b\in B$ with $a+b=1$; the element $ub+va$ lifts prescribed residues $u$ modulo $A$ and $v$ modulo $B$. Also $A\cap B=AB$, since $x=x(a+b)\in AB$ when $x\in A\cap B$. These identities inductively give the Chinese remainder isomorphism
$$R/J\cong\prod_{i=1}^r R/\mathfrak m_i.$$
For the induction, the intersection of preceding factors is comaximal with the next one: multiply elements in the preceding maximal ideals whose residues are one modulo the next ideal. Their product lies in the intersection and still has residue one.

We give the nil-ideal idempotent lift explicitly. If $e_0^2-e_0=\epsilon$ is nilpotent, then $u=2e_0-1$ is a unit, since $u^2=1+4\epsilon$ has inverse given by a finite geometric series. Set $e_1=e_0-u^{-1}\epsilon$. Direct expansion gives
$$e_1^2-e_1=u^{-2}\epsilon^2.$$
The correction lies in the nil ideal. Repeat; the error squares at each step, so a zero power of the initial error makes the process terminate at an idempotent with the prescribed residue. Uniqueness across a nil ideal follows as well: if $e,f$ are two lifts, the idempotents $e(1-f)$ and $f(1-e)$ lie in that ideal. A nilpotent idempotent is zero, so $e=ef=f$.

Lift the coordinate idempotents of $R/J$ to $e_i\in R$. Their products for distinct indices are idempotents in $J$, hence zero. Their sum is then idempotent, so $1-\sum_i e_i$ is an idempotent in $J$ and is zero. Thus
$$R\longrightarrow\prod_i e_iR,\quad r\longmapsto(e_ir)_i$$
has inverse $(r_i)_i\mapsto\sum_i r_i$. Each factor, whose identity is $e_i$, has exactly one prime, corresponding to $\mathfrak m_i$, so it is local.

The factor is precisely $R_{\mathfrak m_i}$. For $s\notin\mathfrak m_i$, $e_is$ avoids its unique maximal ideal and is a unit in $e_iR$; this gives a map $R_{\mathfrak m_i}\to e_iR$. Conversely $e_i$ is an idempotent outside $\mathfrak m_i$, hence becomes one in that localization, whereas the other $e_j$ become zero. The map $e_iR\to R_{\mathfrak m_i}$ is therefore unital, and the two fraction maps are inverse. This identifies the displayed product with the natural localization map. If there are no maximal ideals, the ring is zero by the maximal-proper-ideal Zorn argument, and the empty product is the zero ring. ∎

<a id="algebra-lemma-regular-quasi-regular"></a>

#### Lemma F.74: regular quasi regular

Reading source: [AI Integrated Stacks, pinned Algebra, lines 17680–17766](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L17680-L17766).

Let $A$ be any ring, $M$ any $A$-module, and $f_1,\ldots,f_c$ an $M$-regular sequence. Put $J=(f_1,\ldots,f_c)$. Then the natural graded map
$$
(M/JM)[T_1,\ldots,T_c]\longrightarrow
\bigoplus_{n\geq0}J^nM/J^{n+1}M,\qquad
\bar mT^a\longmapsto[mf^a]
$$
is an isomorphism. Thus a regular sequence is quasi-regular, both for rings and for arbitrary modules. In particular, for a regular sequence in $A$, $J/J^2$ is free over $A/J$ on the classes of the $f_i$.

**Proof.** Every degree is generated by products of the $f_i$, so the map is surjective. Degree zero is the identity. We prove injectivity in every positive degree by induction on $c$, without finiteness or Noetherian assumptions on $M$.

For $c=1$, a relation $mf_1^n\in f_1^{n+1}M$ reads $f_1^n(m-f_1v)=0$ for some $v$. Multiplication by $f_1$ is injective on $M$, hence so is its $n$th power; thus $m\in f_1M$. For $c=0$, only degree zero is present.

Suppose now $c>1$ and the assertion holds for the first $c-1$ entries; write $J'=(f_1,\ldots,f_{c-1})$ and $f'= (f_1,\ldots,f_{c-1})$. A degree-$n$ relation modulo $J^{n+1}M$ can be made an exact zero relation by subtracting, from each coefficient, an element of $JM$: every element of $J^{n+1}M$ is a sum of degree-$n$ products with coefficients in $JM$. It suffices therefore to handle
$$\sum_{e=0}^{\ell}\ \sum_{|a|=n-e}m_{a,e}(f')^a f_c^e=0
\quad(0\leq\ell\leq n).$$
Induct on its largest exponent $\ell$. If $\ell=0$, the induction on $c$ applied in degree $n$ gives all coefficients in $J'M\subset JM$. For $\ell\geq1$, every lower-exponent term belongs to $J'^{\,n-\ell+1}M$. Consequently
$$\sum_{|a|=n-\ell}(f_c^\ell m_{a,\ell})(f')^a
\in J'^{\,n-\ell+1}M.$$
The already proved degree-$n-\ell$ assertion for the shorter list gives $f_c^\ell m_{a,\ell}\in J'M$; in degree zero this is simply membership in $J'M$. Since $f_c$ is injective on $M/J'M$, its powers are injective there, and hence $m_{a,\ell}\in J'M$.

Write each such coefficient as $\sum_{j<c}f_jb_{a,j}$. Replace its top term by
$$m_{a,\ell}(f')^af_c^\ell
=\sum_{j<c}(f_cb_{a,j})(f')^{a+\delta_j}f_c^{\ell-1}.$$
The new relation has largest exponent at most $\ell-1$, and the only changed coefficients differ from the old ones by elements of $f_cM\subset JM$. The induction on $\ell$ puts all new coefficients in $JM$. It therefore puts all old lower coefficients in $JM$, and the old top coefficients were already in $J'M$. This proves the homogeneous injectivity for every $n$ and completes both inductions.

Taking $M=A$ proves the ring assertion. Its degree-one isomorphism is exactly $(A/J)^c\to J/J^2$, with the stated basis. No permutation of the regular list, separatedness, or finite-module hypothesis has been used. ∎

<a id="algebra-lemma-regular-sequence-in-polynomial-ring"></a>

#### Lemma F.75: regular sequence in polynomial ring

Reading source: [AI Integrated Stacks, pinned Algebra, lines 17576–17624](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L17576-L17624).

Let $f_1,\ldots,f_r\in R$ generate a proper ideal in an arbitrary ring. These conditions are equivalent:

1. Every permutation of the list is regular.
2. Every subsequence in its original order is regular.
3. $f_1X_1,\ldots,f_rX_r$ is regular in $R[X_1,\ldots,X_r]$.

**Proof.** A subsequence can be placed first in a permutation, so (1) implies (2). To prove the converse we first check the interchange of two elements. If $a,b$ is regular and $b$ is also a nonzerodivisor, then $b,a$ is regular. Indeed, if $ax=by$, injectivity of $b$ modulo $(a)$ gives $y=az$. Injectivity of $a$ then gives $x=bz$, proving injectivity of $a$ modulo $(b)$. The final ideal is the same proper ideal.

Induct on $r$ to deduce (1) from (2). Any proper sublist inherits (2), so by induction all its permutations are regular. Given a permutation whose last entry is $f_s$, the preceding entries are therefore regular, and it remains to check that $f_s$ is injective modulo all the others. If $s=r$, this is the last injection of the original list. If $s<r$, put
$$V=R/(f_1,\ldots,\widehat f_s,\ldots,f_{r-1}).$$
Permuting the first $r-1$ entries shows that $f_s$ is a nonzerodivisor on $V$. The original-order subsequence omitting $f_s$ shows that $f_r$ is one too. The pair $f_s,f_r$ is regular in $V$, since its second injection is the final injection of the original full list. The two-element interchange just proved makes $f_r,f_s$ regular in $V$, giving the required last injection. All quotient ideals are proper because they are contained in the original proper ideal.

For the polynomial condition, the coefficient of each monomial is independent of the coefficients of the others. After imposing the first $i$ equations, this gives the exact $R$-module decomposition
$$
R[X]/(f_1X_1,\ldots,f_iX_i)
\cong\bigoplus_{e\in\mathbf N^r}(R/J_e)\,X^e,\qquad
J_e=(f_j\mid j\leq i,\ e_j>0).
$$
To verify it, a multiple of $f_jX_j$ contributes to the coefficient of $X^e$ precisely when $e_j>0$, and then contributes a multiple of $f_j$. Conversely any such coefficient is obtained by multiplying $f_jX_j$ by that monomial with its $j$th exponent reduced by one. These two calculations identify the entire ideal coefficient by coefficient.

Multiplication by $f_{i+1}X_{i+1}$ shifts each exponent to $e+\delta_{i+1}$ and multiplies its coefficient by $f_{i+1}$. The coefficient ideal $J_e$ is unchanged by this shift, since only the first $i$ indices occur in it. The multiplication is injective precisely when $f_{i+1}$ is injective on every $R/J_e$.

Under (2), the ordered list with indices $\{j\leq i:e_j>0\}$ followed by $i+1$ is a regular subsequence, giving every such injection. This proves (3). Conversely, for any subset $U\subset\{1,\ldots,i\}$ choose $e_j=1$ for $j\in U$ and zero otherwise. The injection supplied by (3) says that $f_{i+1}$ is injective on $R/(f_j:j\in U)$. Apply it successively along any ordered subsequence to prove all of (2). The polynomial equation ideal is proper since evaluation at all $X_j=0$ factors its quotient onto the nonzero ring $R$. For the empty list all three conditions hold directly. ∎

<a id="algebra-lemma-relative-global-complete-intersection"></a>

#### Lemma F.76: relative global complete intersection

Reading source: [AI Integrated Stacks, pinned Algebra, lines 38280–38292](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L38280-L38292).

A relative global complete intersection over any commutative base ring is syntomic.

**Proof.** Write its presentation as $S=R[X_1,\ldots,X_n]/(f_1,\ldots,f_c)$, with every nonempty residue-field fibre of dimension $n-c$, as in the relative complete-intersection definition. The finite generator and equation lists give finite presentation. The entire arbitrary-base proof [F.77](#algebra-lemma-relative-global-complete-intersection-conormal) gives flatness of $S$ over $R$.

Each nonempty fibre has the displayed $n$ polynomial variables, $c$ equations and dimension $n-c$, so is a global complete intersection over its field. It is consequently locally a complete intersection: the whole five-condition proof [F.57](#algebra-lemma-lci) applies at every fibre prime, or its global presentation itself is the required neighbourhood. Empty fibres have no point to check. These are the finite-presentation, flatness and fibre conditions for syntomicness. If $S=0$, finite presentation is $R/(1)$, flatness is immediate, and all fibres are empty, giving the same conclusion. ∎

<a id="algebra-lemma-relative-global-complete-intersection-conormal"></a>

#### Lemma F.77: relative global complete intersection conormal

Reading source: [AI Integrated Stacks, pinned Algebra, lines 38204–38278](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L38204-L38278).

Let $R$ be any ring and
$$S=R[X_1,\ldots,X_n]/(f_1,\ldots,f_c)$$
a relative global complete intersection: every nonempty residue-field fibre has dimension $n-c$. For a prime $\mathfrak q\subset S$, let $\mathfrak Q\subset R[X]$ be its inverse image. Then:

1. $f_1,\ldots,f_c$ is regular in $R[X]_{\mathfrak Q}$.
2. Every $R[X]_{\mathfrak Q}/(f_1,\ldots,f_i)$, including $i=0$, is flat over $R$.
3. The global $S$-module $(f)/(f)^2$ is free on the classes of the $f_i$.

In particular $S$ is flat over $R$. These assertions include bases that are not Noetherian.

**Proof.** First take a Noetherian base. Fix $\mathfrak Q$ and put $\mathfrak p=\mathfrak Q\cap R$, $k=\kappa(\mathfrak p)$. Its closed polynomial fibre is a localization of $k[X]$ at the corresponding prime. In the nonempty quotient fibre, every minimal equation prime has height at most $c$, by the whole AG-CA-11, Theorem 3.1. The polynomial height formula AG-CA-09, Theorem 4.3, makes each component dimension at least $n-c$. Their maximum is the assumed dimension $n-c$, so all have this dimension. The point formula of AG-CA-09, Theorem 6.1, gives dimension $n-c$ at the chosen quotient point. Thus [F.20](#algebra-lemma-codimension) gives local dimension drop exactly $c$ for this polynomial presentation. The full criterion [F.57](#algebra-lemma-lci) makes its actual $c$-element equation list regular in the ambient fibre local ring.

The map $R_{\mathfrak p}\to R[X]_{\mathfrak Q}$ is flat and local: a polynomial ring is free, and localization preserves exact tensor injection tests. Both rings are Noetherian. Apply the complete successive-quotient lifting proof [F.53](#algebra-lemma-grothendieck-regular-sequence). It proves both regularity in the polynomial local ring and flatness of every local successive quotient over $R_{\mathfrak p}$, hence over $R$.

For the general base we construct a finite Noetherian coefficient model. We first justify the field-dimension fact needed in this descent. For a nonzero finite-type $k$-algebra $C$, the entire AG-CA-09, Corollary 3.2 gives an inclusion $k[T_1,\ldots,T_d]\subset C$ with $C$ finite over it, even when $C$ is not reduced or a domain. For any field extension $E/k$, a basis makes its tensor functor free and faithfully flat. Thus the inclusion remains an inclusion of $E[T]$ into $C\otimes_kE$, and finiteness remains true. The entire AG-CA-05, Theorem 5.1 and polynomial dimension AG-CA-09, Theorem 4.2, give
$$\dim C=d=\dim(C\otimes_kE).$$
The zero algebra stays zero. This proves precisely the field-extension dimension preservation used below.

Let $R_a\subset R$ be generated over the image of $\mathbf Z$ by all coefficients of the equations, and put $S_a=R_a[X]/(f)$. These are finite-type Noetherian models, and $S=R\otimes_{R_a}S_a$. At any actual $\mathfrak q\subset S$, let $\mathfrak p,\mathfrak q_a,\mathfrak p_a$ be its contractions. The residue fields give an inclusion $\kappa(\mathfrak p_a)\subset\kappa(\mathfrak p)$, and the two corresponding fibres are related by that scalar tensor. The latter is nonempty, since the prime $\mathfrak q$ lies over $\mathfrak p$. Its dimension is $n-c$. The proved field-dimension fact therefore gives that dimension for the model fibre as well.

The whole arbitrary-base neighbourhood proof [F.39](#algebra-lemma-dimension-fibres-bounded-open-upstairs) supplies $g_{\mathfrak q}\in S_a\setminus\mathfrak q_a$ whose localized model fibres all have dimension at most $n-c$. Indeed its bound is the dimension at the chosen fibre point, which is at most its total dimension $n-c$; a bound at every point bounds the total dimension by testing the finitely many component generic points. The resulting opens pull back to a cover of $\operatorname{Spec}S$. Choose finitely many, defined by $g_1,\ldots,g_m$, by affine quasi-compactness: their images generate the unit ideal, because otherwise a maximal ideal would give an uncovered point.

Choose polynomial representatives $G_j\in R_a[X]$. A unit-ideal relation in $S$ has a finite polynomial witness
$$1=\sum_j H_jG_j+\sum_i V_if_i\quad\text{in }R[X].$$
Adjoin to $R_a$ all coefficients of the finitely many $H_j,V_i$, obtaining a finite-type integer subalgebra $R_0\subset R$. Set $S_0=R_0[X]/(f)$. The same identity now holds in $R_0[X]$, so the images of the $G_j$ cover $\operatorname{Spec}S_0$.

For every base prime of $R_0$, its residue field extends that of its contraction in $R_a$. Each chart fibre is therefore the corresponding old chart fibre after a field extension. It retains dimension at most $n-c$ by the proved dimension fact. A finite open cover has total dimension the maximum of the chart dimensions here: in a finite-type field algebra each component's generic point belongs to some chart, and that nonempty principal component open retains its dimension. Thus every nonempty fibre of $S_0/R_0$ has dimension at most $n-c$. The height bound for an ideal generated by $c$ elements in a polynomial ring gives the reverse inequality at any minimal equation prime. Every nonempty model fibre consequently has dimension exactly $n-c$. This constructs the required Noetherian relative global complete-intersection model, with the identical equation list and
$$S=R\otimes_{R_0}S_0.$$
If $S=0$, a finite identity $1=\sum_iV_if_i$ already gives a model with $S_0=0$. The local claims are then vacuous and both conormal modules are zero; hence we may continue with a chosen actual prime.

Contract $\mathfrak Q$ to $\mathfrak Q_0\subset R_0[X]$ and $\mathfrak p_0\subset R_0$. Put
$$A_0=(R_0)_{\mathfrak p_0},\qquad
B_0=(R_0[X])_{\mathfrak Q_0},\qquad
B_i=B_0/(f_1,\ldots,f_i).$$
The Noetherian case gives regularity and $A_0$-flatness of each $B_i$, so for every $i<c$ there is an exact sequence
$$0\longrightarrow B_i\xrightarrow{f_{i+1}}B_i
\longrightarrow B_{i+1}\longrightarrow0.$$
Tensor it with $R_{\mathfrak p}$ over $A_0$. It remains left exact because its quotient $B_{i+1}$ is $A_0$-flat: the full Tor long exact sequence [AG-RG-S01, Lemma 1.A](AG-RG-S01.md) gives zero for the possible first kernel. This is the exact reason regularity survives this possibly nonflat scalar change. Base change also makes each $B_i\otimes_{A_0}R_{\mathfrak p}$ flat over $R_{\mathfrak p}$, by the tensor associativity formula for injection tests.

The further prime localization of $B_0\otimes_{A_0}R_{\mathfrak p}$ at the prime induced by $\mathfrak Q$ is exactly $R[X]_{\mathfrak Q}$. To check this, the tensor first inverts the images of $R_0[X]\setminus\mathfrak Q_0$, all of which avoid the actual prime. The further localization inverts the remaining polynomials outside $\mathfrak Q$. Every fraction in the full prime localization is then represented, and the two localization universal properties give inverse maps. Taking the same localizations of the quotient tensors gives exactly $R[X]_{\mathfrak Q}/(f_1,\ldots,f_i)$. Exact localization preserves each displayed multiplication injection and its quotient. Its last quotient is $S_{\mathfrak q}\ne0$, so the resulting list is regular. Localization preserves flatness of these target modules, and $R_{\mathfrak p}$ is flat over $R$. This proves (1) and (2) over the original arbitrary base.

Finally [F.74](#algebra-lemma-regular-quasi-regular) gives the conormal basis at every prime of $S$. The global map $S^c\to(f)/(f)^2$ is surjective by generation. Localization commutes with this ideal quotient; its kernel vanishes at every prime by the local bases. A nonzero module element would have a proper annihilator contained in a maximal ideal and would stay nonzero there, so the kernel is zero. This proves (3). For any injection of $R$-modules the tensor kernel with $S$ likewise vanishes after localization at every $\mathfrak q$, by (2) for its final quotient. The same module detection proves that kernel zero. Thus $S$ is flat over $R$, as asserted. Empty equation lists are included at every step. ∎

<a id="algebra-lemma-relative-global-complete-intersection-smooth"></a>

#### Lemma F.78: relative global complete intersection smooth

Reading source: [AI Integrated Stacks, pinned Algebra, lines 39071–39113](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L39071-L39113).

For a relative global complete-intersection presentation $S=R[X_1,\ldots,X_n]/(f_1,\ldots,f_c)$ over any ring $R$, smoothness at a prime $\mathfrak q\subset S$ is equivalent to some $c\times c$ Jacobian minor having image outside $\mathfrak q$.

**Proof.** The whole unrestricted conormal proof [F.77](#algebra-lemma-relative-global-complete-intersection-conormal) identifies the conormal module with $S^c$, on the actual equation classes. In the polynomial differential basis the conormal map is
$$J:S^c\longrightarrow S^n,\qquad
e_j\longmapsto\sum_i\frac{\partial f_j}{\partial X_i}\,dX_i.$$
Thus its maximal minors are precisely the stated polynomials.

If a selected minor $\Delta$ has image $g\notin\mathfrak q$, then $S_g$ has the inverse-variable presentation
$$S_g=R[X_1,\ldots,X_n,Z]/(f_1,\ldots,f_c,\Delta Z-1).$$
Use the selected $c$ variable columns together with $Z$. Its square Jacobian block has the original selected block at the top, a zero top-right column, and $\Delta$ at the bottom right. Its determinant is $\Delta^2$, a unit in this algebra. The entire arbitrary-base standard smooth lifting proof AG-CA-17, Theorem 4.1 therefore makes this finitely presented algebra smooth. This proves the sufficient direction with an actual principal neighbourhood.

Conversely suppose some $S_h$, with $h\notin\mathfrak q$, is smooth. Its polynomial inverse-variable presentation has a split conormal map by the complete split-sequence proof AG-CA-17, Theorem 3.1. The entire [F.72](#algebra-lemma-principal-localization-NL) calculation identifies its conormal complex with the original localized complex
$$S_h^c\xrightarrow{J_h}S_h^n$$
plus a contractible rank-one complex, whose differential is multiplication by the unit $h$. In these explicitly changed bases, restrict a left inverse of the full differential to the original degree-zero summand, and project its values to the original degree-one summand. The composite is a left inverse of $J_h$. Reduction to $\kappa(\mathfrak q)$ preserves this identity. Hence the resulting $n$-by-$c$ matrix has rank $c$, and the full minor calculation [F.70](#algebra-lemma-matrix-left-inverse) supplies a nonzero $c$-minor over that field. Its original image is outside $\mathfrak q$, proving necessity.

For $c=0$ the empty minor is one and the presentation is a polynomial algebra, smooth by arbitrary variable lifting. Thus this case obeys the same criterion. No Noetherian condition on the base or the target is used. ∎

<a id="algebra-lemma-section-smooth"></a>

#### Lemma F.79: section smooth

Reading source: [AI Integrated Stacks, pinned Algebra, lines 39859–39914](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L39859-L39914).

Let $R\to S$ be smooth and let $\sigma:S\to R$ be its section, with $I=\ker\sigma$. Then $I/I^2$ is finite projective over $R$. If it is free of rank $d$, the $I$-adic completion of $S$ is isomorphic as an $R$-algebra to $R[[T_1,\ldots,T_d]]$.

**Proof.** Define
$$D:S\longrightarrow I/I^2,\qquad
D(s)=[s-\sigma(s)].$$
Give the target its $S$-module action through $\sigma$. Expanding a product and discarding the product of two elements of $I$ proves the derivation identity. It is an $R$-derivation. The universal differential map therefore induces $\Omega_{S/R}\otimes_{S,\sigma}R\to I/I^2$. Its inverse sends $[i]$ to $di\otimes1$. This is well-defined since $d(ij)$ vanishes after tensoring for $i,j\in I$; on every $ds$ its composite is $d(s-\sigma(s))=ds$, and on every ideal class its other composite is the identity. Thus the two maps are inverse.

The entire AG-CA-17, Theorem 3.1 gives finite projectivity of the differential module of this finitely presented formally smooth algebra. Tensor of its finite free direct-summand description with $R$ retains that description, proving the first assertion. The section ideal is finite as well: if $x_1,\ldots,x_m$ are finite algebra generators, the polynomial difference identity makes the $x_j-\sigma(x_j)$ generate its kernel.

Choose $t_1,\ldots,t_d\in I$ representing a free conormal basis, and put $P=R[[T_1,\ldots,T_d]]$, $J=(T_1,\ldots,T_d)$. Continuous evaluation defines
$$b:P\longrightarrow\widehat S=\varprojlim_n S/I^n,\qquad T_i\longmapsto t_i.$$
This map is surjective. To see it, every element of $I$ is an $R$-linear combination of the $t_i$ modulo $I^2$. Multiplying these expressions shows that the degree-$n$ monomials in the $t_i$ generate $I^n/I^{n+1}$ over $R$ for every $n$. Start with the constant residue of a chosen element of $\widehat S$, which is in $S/I=R$. At step $n$, the error in its coordinate modulo $I^{n+1}$ lies in $I^n/I^{n+1}$, so subtract a homogeneous degree-$n$ polynomial in the $t_i$ with coefficients in $R$. The resulting sum of homogeneous corrections is a formal series in $P$, with image the chosen compatible sequence. This proves surjectivity without a Noetherian completion theorem.

The square-zero section decomposition $S/I^2=R\oplus I/I^2$ defines an $R$-map $u_2:S\to P/J^2$, sending the chosen $t_i$ to $T_i$. Formal smoothness lifts it successively along
$$P/J^{n+1}\longrightarrow P/J^n\quad(n\geq2),$$
whose kernel $J^n/J^{n+1}$ has square zero. Choose each lift to extend the preceding one. Their inverse limit is an $R$-map $u:S\to P$ taking $I$ into $J$. Therefore the maps modulo $J^n$ factor through $S/I^n$ and give a continuous extension $a:\widehat S\to P$.

The composite $v=ab$ is an $R$-endomorphism of $P$ with
$$v(T_i)=T_i+\text{terms of degree at least two}.$$
We prove that such a substitution is invertible. Having chosen inverse variable series through degree $n-1$, compute the degree-$n$ error after substitution. Adding its negative as the next homogeneous term removes it, since the identity linear part changes that degree by exactly the added term; all nonlinear changes have higher degree. This recursively constructs a right inverse. The substitution is injective: any nonzero series has a lowest nonzero homogeneous part, and the identity linear part leaves that part unchanged. If $w$ is the right inverse, then $v(wv)=v$; injectivity gives $wv=1$, proving that it is also a left inverse. The coefficient calculations hold over arbitrary $R$, including zero divisors.

Replace $a$ by $v^{-1}a$. Now $ab=1$; hence $b$ is injective, and it was already proved surjective. It is the desired $R$-algebra isomorphism. All maps are continuous for the displayed adic topologies. When $d=0$, the homogeneous correction argument gives $\widehat S=R$ directly, and the same assertion holds. ∎

<a id="algebra-lemma-silly"></a>

#### Lemma F.80: silly

Reading source: [Stacks, Tag 00DS](https://stacks.math.columbia.edu/tag/00DS).

Let \(J,I_1,\ldots,I_r\) be ideals of any commutative ring. Suppose \(J\not\subset I_i\) for every \(i\), and at most two of the \(I_i\) are not prime. There is an element of \(J\) outside all the \(I_i\).

**Proof.** Remove repetitions and every listed ideal contained in another listed ideal. Avoiding the retained larger ideals also avoids the removed smaller ones. The remaining ideals are pairwise incomparable, and still at most two are not prime. We prove the assertion for this remaining list by induction on its length.

For the empty list choose \(0\in J\); there are no avoidance conditions. For one ideal the hypothesis supplies an element outside it. For two ideals choose \(a\in J\setminus I_1\) and \(b\in J\setminus I_2\). If either avoids both, it suffices. Otherwise \(a\in I_2\), \(b\in I_1\). Their sum belongs to neither: membership in \(I_1\) would force \(a=(a+b)-b\in I_1\), and membership in \(I_2\) would similarly force \(b\in I_2\).

For a list of length at least three, place a prime ideal last, calling it \(\mathfrak p=I_r\). Induction gives \(a\in J\) outside all earlier ideals. If \(a\notin\mathfrak p\), it already suffices. Otherwise choose \(b_0\in J\setminus\mathfrak p\) and, for each \(i<r\), choose \(b_i\in I_i\setminus\mathfrak p\); incomparability supplies the latter choices. The product \(b=b_0b_1\cdots b_{r-1}\) belongs to \(J\) and every earlier \(I_i\). It lies outside \(\mathfrak p\), because iterating the defining implication for a prime ideal shows that a product of elements outside it stays outside. Then \(a+b\in J\) still avoids every earlier ideal by subtraction of \(b\), and avoids \(\mathfrak p\) by subtraction of \(a\). This completes the induction without a Noetherian hypothesis. ∎

<a id="algebra-lemma-size-extension-pth-roots"></a>

#### Lemma F.81: size extension pth roots

Reading source: [AI Integrated Stacks, pinned Algebra, lines 45787–45812](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L45787-L45812).

Let $k$ have characteristic $p>0$. If $da_1,\ldots,da_n$ are linearly independent in $\Omega_{k/\mathbf F_p}$, then
$$[k(a_1^{1/p},\ldots,a_n^{1/p}):k]=p^n.$$

**Proof.** Roots can be adjoined successively by quotienting by an irreducible factor of $X^p-a_i$. Such a factor exists by descent on degree, and its quotient is a field by the Euclidean algorithm. A $p$th root is unique in any field containing it: equal $p$th powers give $(x-y)^p=0$, hence $x=y$. Thus these compatible adjunctions give the asserted root field.

We also prove the degree at a nontrivial step. If $\beta^p=a\in H$ and $\beta\notin H$, its minimal polynomial divides $X^p-a=(X-\beta)^p$ in a field containing $\beta$. A monic proper nonconstant factor has degree $r$ with $1\leq r<p$ and coefficient $-r\beta$ at degree $r-1$. If it were over $H$, the nonzero scalar $r$ would put $\beta$ in $H$, a contradiction. Thus the minimal polynomial has degree $p$, and monic division gives the basis $1,\beta,\ldots,\beta^{p-1}$.

Induct on the number of roots already adjoined. The zero-root extension is $k$, of degree one. Suppose the first $i-1$ roots have degree $p^{i-1}$ and the standard monomials in them form a $k$-basis. If $a_i$ were a $p$th power in that field, a root could be written in that basis. Raising it to the $p$th power would give
$$a_i=\sum_{0\leq e_j<p}\lambda_e^p\prod_{j<i}a_j^{e_j},
\qquad \lambda_e\in k.$$
Every $p$th power in $k$ has zero differential, directly from the derivation product rule. Differentiating this finite equality therefore gives
$$
da_i=\sum_e\ \sum_{\substack{j<i\\e_j>0}}
e_j\lambda_e^p\,a_j^{e_j-1}
\left(\prod_{\substack{\ell<i\\\ell\ne j}}a_\ell^{e_\ell}\right)da_j.
$$
This is a linear dependence on the earlier differentials, contrary to the hypothesis. For $i=1$ the right side is empty, giving the same contradiction. Hence the next root is not in the preceding field; the degree-$p$ calculation applies. Its power basis multiplied by the old monomial basis gives the new monomial basis, proving both independence and generation. Degrees multiply along these finite vector-space towers, so the final degree is $p^n$. This also covers $n=0$, and uses no converse criterion for zero absolute differentials. ∎

<a id="algebra-lemma-smooth-over-field"></a>

#### Lemma F.82: smooth over field

Reading source: [AI Integrated Stacks, pinned Algebra, lines 38622–38676](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L38622-L38676).

Every smooth finite-type algebra over any field is locally a complete intersection.

**Proof.** Let $S/k$ be smooth and choose a prime $\mathfrak q$ of $S$. The full principal-chart proof AG-CA-17, Theorem 5.1 supplies a standard smooth neighbourhood $D=S_h$ containing it. Write its polynomial presentation as
$$D=k[Y_1,\ldots,Y_N]/(F_1,\ldots,F_r),$$
with an invertible $r$-column Jacobian minor. Let $\mathfrak Q$ be the polynomial prime over the chosen point and put $V=k[Y]_{\mathfrak Q}$, $\mathfrak m=\mathfrak QV$.

The classes of the $F_i$ in $\mathfrak m/\mathfrak m^2$ are independent. Indeed the differential of a product of two elements of $\mathfrak m$ is zero after tensoring with its residue field. A relation among these classes would consequently give the same residue-field relation among the vectors $dF_i$; derivatives of its lifted coefficients multiply $F_i$ and vanish in that residue field. The chosen nonzero Jacobian minor makes these vectors independent, proving the assertion. This does not assume that the entire cotangent-to-differential map is injective.

The entire polynomial-local regularity proof AG-CA-14, Proposition 3.3 makes $V$ regular. Extend the independent classes to a basis of its finite-dimensional cotangent space and lift the added classes to $\mathfrak m$. Nakayama makes this list a minimal generating list for $\mathfrak m$. The whole AG-CA-12, Theorem 6.1 proves that every such list is regular in this order. Its initial list $F_1,\ldots,F_r$ is therefore regular and generates the defining ideal in $V$.

Condition (5) of the entire criterion [F.57](#algebra-lemma-lci) now gives a principal global complete-intersection neighbourhood of this point in $D$. Its denominator is some $a/h^e$ with $a\in S$, so the same neighbourhood in $\operatorname{Spec}S$ is $D(ha)$, with the identical iterated localization as coordinate algebra. Every point thus has a global complete-intersection principal neighbourhood. This is precisely local complete-intersectionness over $k$. The argument treats arbitrary primes and fields, including imperfect fields. For $S=0$ its empty spectrum already has the required empty cover. ∎

<a id="algebra-lemma-smooth-syntomic"></a>

#### Lemma F.83: smooth syntomic

Reading source: [Stacks, Tag 00TA](https://stacks.math.columbia.edu/tag/00TA).

A smooth map $R\to S$ admits a cover of $\operatorname{Spec}S$ by principal opens $D(g)$ for which $S_g$ is standard smooth over $R$. When $R$ is Noetherian, the map is also syntomic.

**Proof.** The case $S=0$ has an empty cover. The zero algebra has the finite presentation $R/(1)$, is flat as a zero module, and has no nonempty fibres, so it also satisfies the asserted syntomic condition. Hence consider a nonzero $S$.

Fix a finite presentation $P=R[x_1,\ldots,x_n]\twoheadrightarrow S$ with kernel $I=(f_1,\ldots,f_m)$, and put $M=I/I^2$. The split conormal theorem AG-CA-17, Theorem 3.1 puts $M$ inside $S^n$ as a direct summand. Its complement is finite, because projections of the coordinate vectors generate it. The splitting therefore presents $M$ finitely; it also proves flatness by restricting tensor injections for the free module. [S01, Lemma 1.2](AG-RG-S01.md) makes $M$ free over each local ring.

For a subset $E$ of the equation indices, let $U_E$ be the points where the classes indexed by $E$ are a basis of $M$. These loci are open and cover the spectrum. Here are the denominator details. At a prime $\mathfrak q$, select a basis of the residue vector space from the spanning equation classes, with $r$ selected members. Their map $\varphi:S^r\to M$ is surjective over $S_{\mathfrak q}$ by Nakayama. In a local free basis its matrix is square and invertible modulo the maximal ideal, hence invertible by the determinant and adjugate identities. The finite cokernel vanishes at $\mathfrak q$; multiplying denominators which kill its generators gives $a\notin\mathfrak q$ with $\varphi_a$ surjective. Since $M_a$ is projective, its kernel is a finite summand of $S_a^r$. It vanishes at $\mathfrak q$ too. Multiplying numerators of denominators which kill its generators gives $b\notin\mathfrak q$ with $\varphi_{ab}$ an isomorphism. Thus $D(ab)$ lies in this basis locus. The same reasoning applies at every point of any fixed $U_E$, proving openness. Selecting a basis from a spanning vector-space list proves covering. For rank zero the selected list is empty and empty denominator products are $1$.

Choose principal opens inside these loci. On one such open $D(g)$, adjoining a variable representing $g^{-1}$ gives a finite polynomial presentation whose conormal module, by [F.72](#algebra-lemma-principal-localization-NL), is $M_g\oplus S_g$. It is free. [F.55](#algebra-lemma-huber) then supplies a polynomial presentation of $S_g$ whose kernel is generated by a list which is itself a conormal basis. Denote this algebra temporarily by $T$, and write its presentation as
$$
R[y_1,\ldots,y_N]\twoheadrightarrow T,
\qquad K=(a_1,\ldots,a_c),\qquad K/K^2=T^c.
$$

The conormal differential has a left inverse. In these bases let its matrix be $A:T^c\to T^N$, and let $B:T^N\to T^c$ satisfy $BA=1$. At a residue field this forces $c\le N$. The determinant expansion [F.70(2)](#algebra-lemma-matrix-left-inverse) shows that its $c$-row minors $\Delta_E$ generate $1$. Each selected square map is invertible precisely on $D(\Delta_E)$, by the adjugate formula, so these principal opens cover $\operatorname{Spec}T$. The empty minor for $c=0$ is $1$.

On a selected minor open, order its $c$ pivot variables first and let $h\in R[y]$ represent the inverted element $u=\Delta_E\in T$. Present $T_u$ by $a_1,\ldots,a_c,hz-1$. Its Jacobian on $y_1,\ldots,y_c,z$ has diagonal blocks the selected Jacobian and $u$, and upper right block zero. Its determinant is $u\Delta_E$, a unit. This is a standard smooth presentation. Finally a principal open in $S_g$ is principal in $S$: write its defining fraction as $s/g^k$, so its open corresponds to $D(gs)$. The charts just constructed are consequently the required principal cover of the original spectrum.

If $R$ is Noetherian, [F.85](#algebra-lemma-standard-smooth) makes each chart a relative global complete intersection. [F.76](#algebra-lemma-relative-global-complete-intersection) makes it syntomic, and [F.62](#algebra-lemma-local-syntomic) glues that condition on the target. This proves the last assertion.
∎

<a id="algebra-lemma-snake"></a>

#### Lemma F.84: snake

Reading source: [Stacks, Tag 07JW](https://stacks.math.columbia.edu/tag/07JW).

Suppose the following diagram of abelian groups commutes and both rows are exact:
$$
\begin{array}{ccccccccc}
&&X&\xrightarrow{a}&Y&\xrightarrow{b}&Z&\longrightarrow&0\\
&&\alpha\downarrow&&\beta\downarrow&&\gamma\downarrow\\
0&\longrightarrow&U&\xrightarrow{i}&V&\xrightarrow{j}&W.
\end{array}
$$
There is a canonical exact sequence
$$
\ker\alpha\xrightarrow{a}\ker\beta\xrightarrow{b}\ker\gamma
\xrightarrow{\partial}\operatorname{coker}\alpha
\xrightarrow{i}\operatorname{coker}\beta
\xrightarrow{j}\operatorname{coker}\gamma.
$$
Its first map is injective if $a$ is injective, and its last map is surjective if $j$ is surjective.

**Proof.** For $z\in\ker\gamma$, choose $y$ with $b(y)=z$. Commutativity gives $j\beta(y)=0$, so exactness supplies $u$ with $i(u)=\beta(y)$. The injection $i$ makes this $u$ unique for the chosen $y$. Define $\partial z=[u]$ modulo $\alpha(X)$. Replacing $y$ by another lift changes it by $a(x)$; commutativity and injectivity of $i$ then change $u$ by $\alpha(x)$. Thus the class is independent of the lift. Adding lifts proves additivity. The other arrows are the restrictions or quotient maps induced by $a,b,i,j$, which are well defined by the commutative squares.

For exactness at $\ker\beta$, take $y$ there with $b(y)=0$. Write $y=a(x)$. Since $i\alpha(x)=\beta a(x)=0$ and $i$ is injective, $x\in\ker\alpha$. Conversely the image of such an $x$ lies in that kernel and has zero $b$-image.

At $\ker\gamma$, the condition $\partial z=0$ says that the chosen $u$ is $\alpha(x)$ for some $x$. Subtract $a(x)$ from the chosen $y$. This still maps to $z$, and its $\beta$-image is zero. Conversely a lift already in $\ker\beta$ allows $u=0$, so has zero connecting class.

At $\operatorname{coker}\alpha$, a class $[u]$ dies in $\operatorname{coker}\beta$ exactly when $i(u)=\beta(y)$ for some $y$. Then $z=b(y)$ satisfies $\gamma(z)=j\beta(y)=ji(u)=0$, and the defining lift gives $\partial z=[u]$. Every connecting class has zero image for this same reason.

At $\operatorname{coker}\beta$, a class $[v]$ dies in $\operatorname{coker}\gamma$ exactly when $j(v)=\gamma(z)$ for some $z$. Lift $z$ to $y\in Y$. The element $v-\beta(y)$ has zero $j$-image, so is $i(u)$ by bottom-row exactness. Hence $[v]$ comes from $[u]$. Conversely $ji=0$ kills every such image. These checks prove exactness at every intermediate term. Restriction of an injective $a$ remains injective. If $j$ is onto, lift any representative in $W$ to $V$ to obtain surjectivity on the last cokernel.
∎

<a id="algebra-lemma-standard-smooth"></a>

#### Lemma F.85: standard smooth

Reading source: [Stacks, Tag 00T7](https://stacks.math.columbia.edu/tag/00T7).

Let $P=R[x_1,\ldots,x_n]$, $I=(f_1,\ldots,f_c)$, and $S=P/I$ be standard smooth, with the first $c$ variables chosen as pivots. Then:

1. $R\to S$ is smooth.
2. $\Omega_{S/R}$ has the free basis $dx_{c+1},\ldots,dx_n$.
3. $I/I^2$ has the free basis $[f_1],\ldots,[f_c]$.
4. Every principal localization $S_g$ is standard smooth over $R$.
5. For every base map $R\to R'$, the algebra $R'\otimes_R S$ is standard smooth over $R'$.
6. If $r\in R$ becomes a unit in $S$, then $S$ is standard smooth over $R_r$.
7. This presentation makes $S$ a relative global complete intersection over $R$.

**Proof.** Let $C=(\partial f_i/\partial x_j)_{1\le i,j\le c}$; its determinant is a unit in $S$. The map $S^c\to I/I^2$ taking the standard vectors to the equation classes is onto. Its composite with the conormal differential and projection onto the first $c$ differential coordinates is an invertible matrix (the transpose of $C$ under column-vector conventions). Thus this surjection is injective as well. The equation classes are a basis, and the conormal differential is split injective.

Write its image in $S^n$ as the columns of $\binom{C^{\mathsf t}}{D}$. An arbitrary vector $(v,w)$ differs from a unique conormal vector by
$$
(v,w)-\binom{C^{\mathsf t}}{D}(C^{\mathsf t})^{-1}v
=(0,w-D(C^{\mathsf t})^{-1}v).
$$
The conormal image meets the last coordinate summand only in zero. Its cokernel is therefore exactly that summand, with the asserted differential basis. Finite presentation and this split conormal sequence give smoothness by the complete criterion AG-CA-17, Theorem 3.1 and Section 4. This proves (1)–(3), including $c=0$.

To invert $g$, choose a polynomial $h$ representing it and use the equations $f_1,\ldots,f_c,hz-1$. On pivot variables $x_1,\ldots,x_c,z$, the Jacobian has blocks
$$
\begin{pmatrix}C&0\\z(\partial h/\partial x_1,\ldots,\partial h/\partial x_c)&h\end{pmatrix}.
$$
Its determinant $h\det C$ is a unit in $S_g$. This proves (4), even when the localization is zero. Under a base map, applying the map to every coefficient presents the tensor product; the same operation takes the determinant to its image, which remains invertible. This proves (5). For (6), the original equations over $R_r$ present $S_r=S$, since the image of $r$ is already invertible; their determinant is unchanged.

For (7), it remains to compute every nonempty fibre's dimension. By (5) such a fibre is a nonzero standard smooth algebra $B=k[x_1,\ldots,x_n]/(\bar f_1,\ldots,\bar f_c)$ over its residue field $k$. It is locally a complete intersection by [F.82](#algebra-lemma-smooth-over-field). At any prime $\mathfrak q$ of $B$, let $\mathfrak q'$ be its polynomial preimage. The conormal module is free of rank $c$ by (3); reducing to the residue field determines that rank uniquely. [F.57](#algebra-lemma-lci) identifies it with $\operatorname{height}(\mathfrak q')-\operatorname{height}(\mathfrak q)$. For a minimal prime $\mathfrak q$ this gives $\operatorname{height}(\mathfrak q')=c$. The polynomial height formula AG-CA-09, Theorem 4.3 therefore gives dimension $n-c$ for every component.

The algebra $B$ is Noetherian by [S01, Lemma 1.3](AG-RG-S01.md), so [F.136](#topology-lemma-Noetherian) and [F.137](#topology-lemma-irreducible) give a finite component cover. Dimension equals the largest component dimension: a finite chain of irreducible closed subsets lies in a component containing its largest member, and every chain inside a component is also a chain in the whole space. Thus $\dim B=n-c$. This argument works over imperfect fields and for an empty equation list. Empty fibres require no dimension assertion, completing (7).
∎

<a id="algebra-lemma-sum-two-terms"></a>

#### Lemma F.86: sum two terms

Reading source: [Stacks, Tag 00S3](https://stacks.math.columbia.edu/tag/00S3).

Let $A_1\xrightarrow{d_A}A_0$ and $B_1\xrightarrow{d_B}B_0$ be two-term complexes of modules over a ring. If they are homotopy equivalent, then
$$
A_1\oplus B_0\cong B_1\oplus A_0.
$$

**Proof.** Choose chain maps $\varphi:A_\bullet\to B_\bullet$ and $\psi:B_\bullet\to A_\bullet$ and homotopies $h:A_0\to A_1$, $h':B_0\to B_1$ with
$$
1-\psi_1\varphi_1=hd_A,\qquad 1-\psi_0\varphi_0=d_Ah,
$$
$$
1-\varphi_1\psi_1=h'd_B,\qquad 1-\varphi_0\psi_0=d_Bh'.
$$
Define $U:B_1\oplus A_0\to A_1\oplus B_0$ and $V$ in the reverse direction by
$$
U=\begin{pmatrix}\psi_1&h\\-d_B&\varphi_0\end{pmatrix},\qquad
V=\begin{pmatrix}\varphi_1&-h'\\d_A&\psi_0\end{pmatrix}.
$$
Multiplying the blocks and using the four homotopy identities and the two chain-map identities gives
$$
UV=\begin{pmatrix}1&h\psi_0-\psi_1h'\\0&1\end{pmatrix},\qquad
VU=\begin{pmatrix}1&\varphi_1h-h'\varphi_0\\0&1\end{pmatrix}.
$$
Each off-diagonal matrix squares to zero, so negating that off-diagonal block gives the inverse product. Consequently $L=(VU)^{-1}V$ is a left inverse of $U$, and $T=V(UV)^{-1}$ is a right inverse. The equality $L=L(UT)=(LU)T=T$ makes them the same inverse. Hence $U$ is an isomorphism, proving the claim without any finite-generation or freeness hypothesis.
∎

<a id="algebra-lemma-syntomic"></a>

#### Lemma F.87: syntomic

Reading source: [Stacks, Tag 00SY](https://stacks.math.columbia.edu/tag/00SY).

Let $R$ be Noetherian, and let $\mathfrak q\in\operatorname{Spec}S$ lie over $\mathfrak p\in\operatorname{Spec}R$. The following neighbourhood conditions are equivalent:

1. Some $g\notin\mathfrak q$ makes $R\to S_g$ syntomic.
2. Some $g\notin\mathfrak q$ makes $S_g$ a relative global complete intersection over $R$.
3. Some $g\notin\mathfrak q$ makes $S_g$ finitely presented over $R$, while $R_{\mathfrak p}\to S_{\mathfrak q}$ is flat and $S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}$ is a complete-intersection local ring over $k=\kappa(\mathfrak p)$ in the sense of [F.3](#algebra-definition-lci-local-ring).

**Proof.** A syntomic neighbourhood is finitely presented and flat and has locally complete-intersection fibres; [F.58](#algebra-lemma-lci-at-prime) gives (3) from (1). [F.76](#algebra-lemma-relative-global-complete-intersection) gives (1) from (2). We prove the remaining implication with all rings localized explicitly.

Under (3), first replace $S$ by the indicated finitely presented neighbourhood, retaining the prime. Write $P=R[x_1,\ldots,x_n]\twoheadrightarrow S$ with kernel $I$ and polynomial preimage $\mathfrak q'$. In the fibre $\bar P=k[x_1,\ldots,x_n]$, write $\bar I$ for the image ideal and $\bar{\mathfrak q}'$ for the induced prime. By [F.58](#algebra-lemma-lci-at-prime) and [F.57](#algebra-lemma-lci), the ideal $\bar I_{\bar{\mathfrak q}'}$ has a regular generating list of length $c$, its minimal number of generators. Choose $f_1,\ldots,f_c\in I$ whose images give a basis of $\bar I_{\bar{\mathfrak q}'}/\bar{\mathfrak q}'\bar I_{\bar{\mathfrak q}'}$. This is possible by selecting a basis from the images of a finite generating list of $I$. Nakayama gives generation in the fibre local ring, and the last assertion of F.57 makes this very list regular there.

Set $T=P/(f_1,\ldots,f_c)$ and $J=\ker(T\to S)$. The polynomial ring is Noetherian by [S01, Lemma 1.3](AG-RG-S01.md), so $J$ is finite. Localize the short exact sequence at $\mathfrak q'$ as $P$-modules:
$$
0\longrightarrow J_{\mathfrak q'}\longrightarrow T_{\mathfrak q'}\longrightarrow S_{\mathfrak q}\longrightarrow0.
$$
These are $R_{\mathfrak p}$-modules. Flatness of the last module makes tensoring with $k$ injective on the first arrow, by the tensor-kernel calculation [S01, Lemma 1.2 and Lemma 1.A](AG-RG-S01.md). The last arrow becomes an isomorphism after tensoring, because the chosen fibre equations generate the localized fibre ideal. Hence
$$
J_{\mathfrak q'}/\mathfrak pJ_{\mathfrak q'}=0.
$$
Over the local polynomial ring $P_{\mathfrak q'}$, the ideal $\mathfrak pP_{\mathfrak q'}$ is contained in its maximal ideal. Applying [F.10](#algebra-lemma-NAK) to the finite module $J_{\mathfrak q'}$ gives zero. Clear annihilating denominators for a finite generating list of $J$: some $u\in P\setminus\mathfrak q'$ gives $J_u=0$, and thus $T_u=S_u$.

The fibre of $T$ at the induced prime has the same local quotient by the chosen regular list. F.57 gives its point dimension $n-c$. Applying [F.66(3)](#algebra-lemma-localize-relative-complete-intersection) to this $c$-equation presentation produces a relative global complete-intersection principal neighbourhood of that point. Apply this to $T_u$, using its presentation with the additional equation $uz-1$; the fibre point dimension remains $n-c$, and the variable and equation counts both increase by one. The resulting neighbourhood is therefore a principal localization of $S_u$ with a relative global complete-intersection presentation. Writing its inverted element as a fraction in $S_u$ makes the composite neighbourhood $S_g$ for some $g\notin\mathfrak q$. This is (2). Empty regular lists use the same argument with $c=0$.
∎

<a id="algebra-lemma-syntomic-presentation-ideal-mod-squares"></a>

#### Lemma F.88: syntomic presentation ideal mod squares

Reading source: [Stacks, Tag 07BT](https://stacks.math.columbia.edu/tag/07BT).

Let $R$ be Noetherian, let $S=R[x_1,\ldots,x_n]/I$ with $I$ finitely generated, and suppose $S_g$ is syntomic over $R$. Then $(I/I^2)_g$ is finite projective over $S_g$.

**Proof.** Put $A=S_g$ and $M=(I/I^2)_g$. If $A=0$, then $M=0$ and the assertion follows. Otherwise $A$ is Noetherian by [S01, Lemma 1.3](AG-RG-S01.md) and localization, so the finite module $M$ is finitely presented.

At every prime of $A$, [F.87](#algebra-lemma-syntomic) supplies a principal relative global complete-intersection neighbourhood. [F.77](#algebra-lemma-relative-global-complete-intersection-conormal) makes the conormal of its displayed equations finite free. The presentation comparison [F.33](#algebra-lemma-conormal-module-localize) identifies $M$ there, up to finite free summands, with that conormal. Therefore $M$ is finite projective there: the comparison realizes it as a summand of a finite free module. Choose finitely many of these neighbourhoods $D(a_i)$ covering $\operatorname{Spec}A$. The finite choice follows from the principal-open cover criterion: the ideal of all covering elements is not contained in any prime, hence contains $1$, which is a finite sum.

Here is the global splitting argument. Choose a finite free surjection $\pi:A^N\to M$. Its localization on $D(a_i)$ has a right inverse $s_i$, because $M_{a_i}$ is projective. A finite presentation $A^r\to A^s\to M\to0$ realizes $\operatorname{Hom}_A(M,A^N)$ as the kernel of a map between finite matrix modules. Localization is exact and commutes with these finite modules, so
$$
\operatorname{Hom}_A(M,A^N)_{a_i}
=\operatorname{Hom}_{A_{a_i}}(M_{a_i},A_{a_i}^N).
$$
Consequently some global $t_i:M\to A^N$ represents $a_i^{k_i}s_i$. The map $\pi t_i-a_i^{k_i}1_M$ becomes zero after inverting $a_i$. Multiplying by another power of $a_i$ kills its values on all members of a finite generating list of $M$. Replacing $t_i$ by that multiple gives
$$
\pi t_i=a_i^{e_i}1_M.
$$
The powers $a_i^{e_i}$ still generate $1$: if a proper ideal contained them, a containing prime would contain all the corresponding $a_i$, contradicting the cover. Choose $b_i$ with $\sum_i b_i a_i^{e_i}=1$. Then $\sum_i b_i t_i$ is a global right inverse of $\pi$. Thus $M$ is a direct summand of $A^N$, which proves finite projectivity. All denominator and zero-module cases are included.
∎

<a id="algebra-lemma-total-ring-fractions-no-embedded-points"></a>

#### Lemma F.89: total ring fractions no embedded points

Reading source: [Stacks, Tag 02LX](https://stacks.math.columbia.edu/tag/02LX).

Suppose a ring $R$ has finitely many minimal primes $\mathfrak q_1,\ldots,\mathfrak q_t$, and its zerodivisors are exactly their union. Its total ring of fractions has the canonical decomposition
$$
Q(R)\cong\prod_{i=1}^t R_{\mathfrak q_i}.
$$

**Proof.** If $t=0$, the assumed zerodivisor set is empty. A nonzero ring would make $0$ a zerodivisor, since it annihilates $1\ne0$, so $R=0$. Both its localization and the empty ring product are zero. Now assume $t>0$. Let $D$ be the multiplicative set of nonzerodivisors and put $A=D^{-1}R$. Every element of $D$ avoids every $\mathfrak q_i$, so each map $R\to R_{\mathfrak q_i}$ extends to $A$. The prime correspondence for localization identifies the primes of $A$ with primes of $R$ disjoint from $D$. Such a prime is contained in $\bigcup_i\mathfrak q_i$. By [F.80](#algebra-lemma-silly) it is contained in one $\mathfrak q_i$, and minimality forces equality. Thus the primes of $A$ are precisely the extensions $\mathfrak m_i=D^{-1}\mathfrak q_i$. They are distinct and incomparable, hence all maximal.

We construct the product decomposition, including possible nilpotents. For each $i$ and $j\ne i$, choose an element in $\mathfrak m_j\setminus\mathfrak m_i$, and multiply these choices to obtain $a_i$. Then $a_i$ avoids $\mathfrak m_i$ and belongs to every other prime. For $t=1$ use the empty product $a_1=1$. Each product $a_i a_j$ for $i\ne j$ belongs to every prime, and hence is nilpotent by AG-CA-01, Theorem 1.2. Choose a common positive integer $N$ with $a_i^N a_j^N=0$ for every pair. The elements $a_i^N$ generate the unit ideal, since no prime contains all of them. Write $1=\sum_i b_i a_i^N$ and set $e_i=b_i a_i^N$. The $e_i$ are orthogonal and sum to $1$; multiplying this sum by $e_i$ gives $e_i^2=e_i$. Modulo $\mathfrak m_i$, only the $i$th summand survives, so $e_i$ is $1$ there and is zero at every other prime.

The maps $a\mapsto(e_i a)_i$ and $(u_i)_i\mapsto\sum_i u_i$ are inverse ring maps between $A$ and $\prod_i e_iA$. Each factor has only the prime induced by $\mathfrak m_i$, and is therefore local: a nonunit lies in a maximal ideal, which must be that prime. The projection $A\to e_iA$ consequently inverts every element outside $\mathfrak m_i$. Conversely, in $A_{\mathfrak m_i}$ the idempotent $e_i$ is a unit and hence equals $1$, so the complementary factor vanishes. These universal properties give $e_iA\cong A_{\mathfrak m_i}\cong R_{\mathfrak q_i}$. The isomorphism is the canonical map stated above.
∎

<a id="algebra-lemma-when-colimit"></a>

#### Lemma F.90: when colimit

Reading source: [Stacks, Tag 07C3](https://stacks.math.columbia.edu/tag/07C3).

For an arbitrary ring map $R\to\Lambda$, the following are equivalent: $\Lambda$ is a filtered colimit of smooth $R$-algebras; every $R$-algebra map from a finitely presented algebra $A$ to $\Lambda$ factors through a smooth $R$-algebra.

**Proof.** First suppose such a filtered presentation of $\Lambda$ is given. Write $A$ with finitely many polynomial generators and finitely many defining equations. The images of its generators have representatives at a common stage. Each defining equation becomes zero at a later stage, by the equality criterion in a filtered colimit. A common successor of those finitely many stages therefore satisfies every equation. The generator images define the required map to that smooth stage.

For the converse, form the category whose objects are smooth $R$-algebras $B$ with a map $B\to\Lambda$, and whose arrows commute with those maps. Smooth algebras are finitely presented. This category can be taken small: finite polynomial presentations form a set, and a map from each one to $\Lambda$ is specified by a finite tuple of elements of $\Lambda$; use these presentations as representatives. The object $R\to\Lambda$ makes it nonempty.

Given two objects $B_1,B_2$, the tensor product $B_1\otimes_R B_2$ is finitely presented: combine their finite generator lists and equations. Factor its induced map to $\Lambda$ through a smooth algebra. The two structure maps into that algebra give a common successor in the category. For parallel arrows $u,v\colon B\rightrightarrows C$, choose finite algebra generators $b_1,\ldots,b_r$ of $B$. The quotient
$$
C/(u(b_1)-v(b_1),\ldots,u(b_r)-v(b_r))
$$
is finitely presented by adding these finitely many equations to a presentation of $C$. Its map to $\Lambda$ factors through a smooth algebra by the hypothesis. The resulting arrow from $C$ equalizes $u$ and $v$, because equality on the generators gives equality on every polynomial in them. These two constructions prove filteredness.

Let $L$ be this category's colimit and $L\to\Lambda$ its induced map. It is surjective: for any $\lambda\in\Lambda$, apply the factoring hypothesis to $R[T]\to\Lambda$ with $T\mapsto\lambda$; the intermediate object supplies a representative of $\lambda$ in $L$. For injectivity, a representative $b\in B$ with zero image in $\Lambda$ gives a map $B/(b)\to\Lambda$. This quotient is finitely presented, so its factorization through a smooth object yields a successor at which $b=0$. Hence its colimit class is zero. Two representatives can be moved to a common stage and this argument applied to their difference, proving equality detection as well. Thus $L\to\Lambda$ is an isomorphism of $R$-algebras, establishing the filtered presentation without any Noetherian hypothesis.
∎

<a id="algebra-proposition-characterize-separable-field-extensions"></a>

#### Proposition F.91: characterize separable field extensions

Reading source: [AI Integrated Stacks, pinned Algebra, lines 46037–46069](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L46037-L46069).

For every field extension $K/k$, the following are equivalent: separability in [F.5](#algebra-definition-separable-field-extension); geometric reducedness over $k$; algebraic formal smoothness over $k$; $H_1(L_{K/k})=0$; and injectivity of
$$\iota:K\otimes_k\Omega_{k/P}\longrightarrow\Omega_{K/P},$$
where $P$ is the prime field. In characteristic $p>0$ they are also equivalent to the condition that an absolute $p$-basis of $k$ remains $p$-independent over $K^p$. In characteristic zero all the conditions hold. For finitely generated extensions they agree with the existence of a separating transcendence basis.

**Proof.** We give the comparisons in an order that does not assume the last finitely generated assertion.

First, every field is formally smooth over its prime field. In characteristic zero, choose a transcendence basis over $\mathbf Q$; the remaining algebraic extension is separable, because a nonconstant irreducible polynomial has nonzero derivative of smaller degree and hence is relatively prime to it. The two entire lifting constructions in [F.49](#algebra-lemma-formally-smooth-extensions-easy), together with the composition lifting proof AG-CA-17, Theorem 1.2, give formal smoothness, for arbitrary bases and algebraic extensions.

In characteristic $p$, take an absolute $p$-basis $B$ of a field $H$ by the whole [F.119](#more-algebra-lemma-p-basis). Given a prime-field map $\psi:H\to D/J$, $J^2=0$, define a lift on $H^p$ by
$$\theta(a^p)=\widetilde{\psi(a)}^{\,p}.$$
The root $a$ is unique in $H$, and changing its chosen lift by $j\in J$ does not change this power, since $j^p=0$. Frobenius of sums and products proves that $\theta$ is a unital ring map. Choose arbitrary lifts of the $\psi(b)$ for $b\in B$. Their $p$th powers are $\theta(b^p)$; the exact presentation
$$H=H^p[T_b:b\in B]/(T_b^p-b^p)$$
proved in F.119 therefore extends them to a lift on $H$. This establishes prime-field formal smoothness in both characteristics.

Suppose $\iota$ is injective. In a square-zero lifting problem for $K/k$, obtain a $P$-lift $u:K\to D$ by the preceding argument. Write $v:k\to D$ for the prescribed structural map. The difference $u|_k-v$ takes values in $J$ and is a $P$-derivation for the common action modulo $J$, by expanding a product and using $J^2=0$. The given map $K\to D/J$ makes $J$ a $K$-vector space. Its derivation corresponds to a linear map from $K\otimes_k\Omega_{k/P}$ to $J$; extend it along the injection $\iota$ to $\Omega_{K/P}$ by extending a vector-space basis. The resulting derivation $\delta:K\to J$ gives the corrected lift $u-\delta$. Indeed
$$
(u(x)-\delta(x))(u(y)-\delta(y))
=u(xy)-u(x)\delta(y)-u(y)\delta(x)
=u(xy)-\delta(xy).
$$
It preserves one and agrees with $v$ on $k$, proving formal smoothness.

Conversely, any $P$-derivation $d:k\to V$, for a $K$-vector space $V$, makes $K\oplus V$ a $k$-algebra by $a\mapsto(a,d(a))$; its multiplication is $(x,v)(y,w)=(xy,xw+yv)$. Formal smoothness lifts the identity through the square-zero quotient to $K$. The second component of that lift is a derivation extending $d$. Thus every linear functional on the domain of $\iota$ extends to its codomain. If a nonzero vector lay in its kernel, extend that vector to a basis and take a functional equal to one on it; such a functional could not extend. Hence $\iota$ is injective. The whole [F.17](#algebra-lemma-characterize-formally-smooth-field-extension) proves precisely the equivalence with the displayed first cotangent homology condition, in arbitrary field scope.

In characteristic $p$, F.119 identifies the differentials of an absolute $p$-basis $B$ of $k$ with a basis of $\Omega_{k/P}$. Applied over $P$ to $K$, its other equivalence says their images are independent exactly when the standard monomials in $B$ are independent over $K^p$. This proves the equivalence with $\iota$'s injectivity.

We next compare this condition with reducedness. A finite root algebra
$$K\otimes_k k(b^{1/p}:b\in B_0)
=K[T_b:b\in B_0]/(T_b^p-b),\qquad B_0\subset B\ {\rm finite},$$
is free on the standard monomials. The corresponding root-field monomials are independent over $K$ exactly when the monomials in $B_0$ are independent over $K^p$: raise a proposed relation to its $p$th power, and take roots of its coefficients for the converse. If independent, the algebra maps isomorphically to the root field. If dependent, that map has a nonzero kernel. Every element of the root algebra has $p$th power in $K$; a kernel element therefore has $p$th power zero in the algebra itself. It is a nonzero nilpotent. The full algebra $K\otimes_k k^{1/p}$ is the union of these algebras with injective transitions, since a full $p$-basis expansion expresses every root using finitely many basis roots. Reducedness of this union is equivalent to reducedness of every finite stage. Thus geometric reducedness implies the $p$-basis condition.

For the converse we must test all field extensions. The independence persists through all root heights. More explicitly, a relation
$$\sum_a c_a^{p^r}B^a=0,\qquad 0\leq a_b<p^r,$$
can be grouped by $a=pu+v$, $0\leq v_b<p$. The coefficient of $B^v$ is
$$\left(\sum_u c_{pu+v}^{p^{r-1}}B^u\right)^p.$$
Independence over $K^p$ makes each coefficient zero. Frobenius is injective in a field; induction on $r$ then kills every $c_a$. Iterating the unique finite $p$-basis expansions in $k$ shows that the monomials with exponents below $p^r$ are a basis of $k$ over $k^{p^r}$. Taking roots gives the standard presentation and basis of every finite subset root extension of height $r$. The preceding relation calculation makes all its base changes to $K$ fields; their directed union $K\otimes_k k^{1/p^r}$ is a field too.

Every finite purely inseparable extension $k'/k$ embeds over $k$ in some $k^{1/p^r}$: choose finitely many generators and a common root height. Tensoring its inclusion with the vector space $K$ is injective. Hence $K\otimes_k k'$ is a finite-dimensional domain over $K$, and is a field by the multiplication-inverse argument.

Now take a finitely generated field extension $E/k$. In characteristic $p$, the entire [F.69](#algebra-lemma-make-separably-generated) supplies finite purely inseparable $k'/k$, an extension $E'/E$ containing $k'$, and a separating transcendence basis for $E'/k'$. Put $H=K\otimes_k k'$, a field as just proved. In characteristic zero use $k'=k$, $H=K$ and $E'=E$: a maximal algebraically independent subset of finite field generators leaves a finite algebraic, necessarily separable, extension.

In either case, for a separating basis $T$, the ring
$$C=H\otimes_{k'}k'(T)=\bigl(k'[T]\setminus\{0\}\bigr)^{-1}H[T]$$
is a domain. The algebra $C\otimes_{k'(T)}E'$ is finite free over $C$, by a vector-space basis of the finite separable field extension $E'/k'(T)$. It therefore injects into its localization over $\operatorname{Frac}(C)$. That generic algebra is reduced: express the finite separable extension by a finite tower of simple generators. At each step a monic minimal polynomial is relatively prime to its derivative, and its Bézout identity remains valid after any field extension. Its irreducible factors are consequently distinct. The two-factor Bézout Chinese remainder formula and its finite induction, proved in [F.73](#algebra-lemma-product-local), identify its quotient with a product of fields. Repeat on every field factor at the next step of the tower. The final tensor algebra is a finite product of fields, hence reduced. Its subalgebra $C\otimes E'=H\otimes_{k'}E'=K\otimes_kE'$ is reduced as well.

The inclusion $E\subset E'$ remains injective after tensoring over $k$ with $K$, since field-vector-space inclusions split by extending bases. Thus $K\otimes_kE$ is reduced. An arbitrary field extension of $k$ is the directed union of its finitely generated subfields, with injective tensor transitions. A nilpotent and its finite power relation occur at one stage, so the union is reduced. This proves geometric reducedness from the $p$-basis condition; it also proves it for all extensions in characteristic zero.

It remains to connect formal smoothness with the definition of separability. For a finitely generated formally smooth field $L/k$, choose a finite-type domain $B=k[a_1,\ldots,a_n]\subset L$ with fraction field $L$, and a polynomial presentation $Q=k[X_1,\ldots,X_n]\to B$ with prime kernel $I$. Hilbert's basis theorem AG-CA-03, Theorem 2.1, makes $I$ finite. The entire localization comparison [F.65](#algebra-lemma-localize-NL), together with F.17 for $L/k$, makes
$$
(I/I^2)\otimes_B L\longrightarrow L^n
$$
injective: exact field-of-fractions localization identifies this map's kernel with the localized first cotangent homology. Choose $f_1,\ldots,f_c\in I$ whose conormal classes form a basis of this finite-dimensional space. Their differentials are independent, giving a $c$-column Jacobian determinant $\Delta\notin I$.

The local ring $Q_I$ has maximal ideal $IQ_I$ and residue field $L$. Its cotangent space is exactly the conormal space just used. The whole [F.10](#algebra-lemma-NAK) makes the $f_i$ generate $IQ_I$. The finite module $I/(f_1,\ldots,f_c)$ then vanishes there. Kill its finite generator list by a product $h_0\notin I$ of annihilating denominators. For $h=h_0\Delta$ and its image $g\in B$ this gives
$$B_g=k[X_1,\ldots,X_n,Z]/(f_1,\ldots,f_c,hZ-1).$$
The square Jacobian block using the selected columns and $Z$ has determinant $h\Delta$, a unit. The full AG-CA-17, Theorem 4.1, makes this a standard smooth domain. Its fraction field is $L$, and the entire domain calculation [F.64](#algebra-lemma-localization-smooth-separable) gives a separating transcendence basis. This includes $c=0$, with empty minor one. Conversely such a basis gives a purely transcendental extension followed by a finite separable one; F.49 and the full formal composition proof make $L/k$ formally smooth.

If $K/k$ is separable by F.5, the whole F.49(3) gives formal smoothness, hence the conditions already compared. Conversely, in characteristic $p$ the $p$-basis condition descends to every finitely generated intermediate $L$: coefficients in $L^p$ are also in $K^p$. The differential and lifting comparisons make $L/k$ formally smooth, and the preceding finite construction makes it separably generated. This is exactly F.5's definition for $K/k$. In characteristic zero the finite transcendence-basis argument above gives that definition for every intermediate field. Finally F.49 gives formal smoothness there, hence differential injectivity and the homology condition. All comparisons and the finite-generation assertion are now proved. ∎

<a id="more-algebra-definition-G-ring"></a>

#### Definition F.92: G ring

Reading source: [Stacks, Tag 07GH](https://stacks.math.columbia.edu/tag/07GH).

The term *G-ring* imposes two requirements on $R$: it is Noetherian, and at every prime $\mathfrak p$ its localization-to-completion map is regular. The map in this second requirement is
$$
R_{\mathfrak p}\longrightarrow\widehat{R_{\mathfrak p}},
\qquad
\widehat{R_{\mathfrak p}}
=\varprojlim_{n\ge1}R_{\mathfrak p}/(\mathfrak pR_{\mathfrak p})^n.
$$
Thus the completion used in the definition is taken at the maximal ideal of the local ring, separately for each prime.

<a id="more-algebra-definition-excellent"></a>

#### Definition F.93: excellent

Reading source: [Stacks, Tag 07QT](https://stacks.math.columbia.edu/tag/07QT).

For a Noetherian ring $R$, *quasi-excellence* means that $R$ satisfies the G-ring condition of [F.92](#more-algebra-definition-G-ring) and the J-2 condition. Here J-2 requires the regular locus
$$
\{\mathfrak q\in\operatorname{Spec}B:B_{\mathfrak q}\text{ is regular}\}
$$
to be open for each finite-type $R$-algebra $B$; this is the terminology of [Stacks, Tag 07P7](https://stacks.math.columbia.edu/tag/07P7).

An *excellent* ring has these properties and is universally catenary. To specify that last condition, a ring is catenary when, between each fixed pair of comparable primes, the lengths of finite strict chains have a common finite bound and the chains into which no further prime can be inserted all have equal length. A Noetherian ring is universally catenary when every finite-type algebra over it has this property. These two definitions are [Stacks, Tag 00NI](https://stacks.math.columbia.edu/tag/00NI) and [Tag 00NL](https://stacks.math.columbia.edu/tag/00NL).

<a id="more-algebra-definition-local-complete-intersection"></a>

#### Definition F.94: local complete intersection

Reading source: [Stacks, Tag 07D0](https://stacks.math.columbia.edu/tag/07D0).

For a map $A\to B$ of finite type, choose a surjection
$$
P=A[T_1,\ldots,T_n]\twoheadrightarrow B,
\qquad I=\ker(P\to B).
$$
The map is a *local complete intersection* when $I$ is a Koszul-regular ideal, with that ideal condition understood exactly as in [F.95](#more-algebra-definition-regular-ideal). Checking one such presentation suffices: the full arbitrary-ring proof [F.94.A](#more-algebra-lemma-lci-presentation-independent) below shows that every other finite polynomial presentation then has a Koszul-regular kernel. Neither this definition nor that comparison assumes $A$ Noetherian.

<a id="more-algebra-lemma-lci-presentation-independent"></a>

#### Lemma F.94.A: arbitrary-ring presentation independence

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 8869–8942](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L8869-L8942); [Stacks, Tag 07CZ](https://stacks.math.columbia.edu/tag/07CZ).

Let $A$ be an arbitrary ring and suppose an algebra $C$ has finite polynomial presentations
$$P=A[T_1,\ldots,T_n]\twoheadrightarrow C=P/I,\qquad
Q=A[X_1,\ldots,X_m]\twoheadrightarrow C=Q/J.$$
If $I$ is a Koszul-regular ideal as defined in [F.95](#more-algebra-definition-regular-ideal), then $J$ is also Koszul-regular. Moreover $C$ is finitely presented. This proves the presentation-independence assertion in F.94 without Noetherian hypotheses.

**Proof.** We first supply the elementary complex calculations used to compare the two presentations.

For a list $f=(f_1,\ldots,f_c)$ over a ring $V$, take a free module with basis $e_1,\ldots,e_c$ and form
$$K_j(f;V)=\bigwedge^jV^c,\qquad
d(e_{i_1}\wedge\cdots\wedge e_{i_j})
=\sum_{a=1}^j(-1)^{a-1}f_{i_a}
e_{i_1}\wedge\cdots\widehat{e_{i_a}}\cdots\wedge e_{i_j}.$$
Deleting a pair of indices in the two orders gives opposite signs, so $d^2=0$. Its degree-zero homology is $V/(f)$. Appending $u$ identifies the new degree-$j$ term with $K_j(f)\oplus K_{j-1}(f)$, with differential
$$d(a,b)=(d_fa+ub,-d_fb);$$
the sign identification multiplies the wedge ending in the added basis vector by $(-1)^{j-1}$.

If $K(f)$ has zero positive homology and $u$ acts injectively on $V/(f)$, this cone has zero positive homology too. Indeed a degree-$j$ cycle satisfies $d_fb=0$ and $d_fa=-ub$. For $j>1$, write $b=d_fc$ using the old acyclicity. For $j=1$, the last equation makes $u[b]=0$ in $H_0(K(f))$; injectivity likewise gives $b=d_fc$. Subtract the boundary of $(0,-c)$ to obtain $(a+uc,0)$, an old positive-degree cycle. Its old bounding chain makes this remaining vector a boundary in the cone. Degree zero is the additional quotient by $u$. This proves the appending assertion, including empty initial lists.

A second calculation will detect conormal ranks. If $H_1(K(f))=0$, the classes of the $f_i$ give a basis of $(f)/(f)^2$ over $V/(f)$. They generate by definition. Given $\sum_i b_if_i\in(f)^2$, write the right side as $\sum_{i,j}a_{ij}f_if_j$ and replace $b_i$ by $b_i-\sum_j a_{ij}f_j$. Their scalar product is now exactly zero, so the resulting vector is a degree-one cycle. A degree-two Koszul boundary has every coordinate in $(f)$. Vanishing of $H_1$ therefore puts all the corrected coefficients, and hence every $b_i$, in $(f)$. This proves independence.

We next prove that the kernels are finite. The principal charts in the Koszul-regularity condition cover $V(I)$. If their denominators are $a_\lambda\in P$, then $I+(a_\lambda)=P$: a proper ideal is contained in a maximal ideal, which would give an uncovered prime containing $I$. Thus finitely many denominators and an element $b\in I$ satisfy
$$1=b+\sum_{\ell=1}^s c_\ell a_\ell.$$
Choose numerators in $I$ of every finite local generator list for $I_{a_\ell}$, and let $I_0$ be generated by those numerators and $b$. At a prime where some $a_\ell$ is invertible, $I_0$ and $I$ have the same localization. At any other prime, the identity makes $b$ a unit, so both localize to the unit ideal. Therefore $(I/I_0)$ vanishes at every prime, and is zero. Here is local detection for this possibly infinite module: a nonzero element has a proper annihilator contained in a maximal ideal; if it became zero there, an element outside that ideal would annihilate it, a contradiction. Hence $I=I_0$ is finite. This makes $C$ finitely presented, and the entire [F.44](#algebra-lemma-finite-presentation-independent) then makes $J$ finite. If $C=0$, both kernels are unit ideals and their required prime tests are empty. We now assume $C\ne0$ and fix $\mathfrak q\in\operatorname{Spec}C$.

Choose $p_j(T)\in P$ representing each image of $X_j$ and $q_i(X)\in Q$ representing each image of $T_i$. In $W=A[T,X]$ the kernel $L$ of the common map to $C$ has two exact descriptions:
$$L=(I,u_1,\ldots,u_m)=(J,s_1,\ldots,s_n),\qquad
u_j=X_j-p_j(T),\quad s_i=T_i-q_i(X).$$
Quotienting by the added equations eliminates those variables and recovers the specified maps to $C$, which proves both descriptions. Let $\mathfrak r\subset W$ be the inverse image of $\mathfrak q$, and $\mathfrak p_P,\mathfrak p_Q$ its contractions. Translation is a polynomial-ring isomorphism $W=Q[s_1,\ldots,s_n]$. Constant and linear coefficients in these variables give an exact decomposition
$$L/L^2=(J/J^2)\oplus C^n.$$
The constant part is taken modulo $J^2$, the linear coefficients modulo $J$, and all terms with at least two $s$ factors disappear. Sending these data to their constant-plus-linear representatives and reading them back gives inverse maps, so the decomposition is valid over arbitrary rings.

Pick $a\in P\setminus\mathfrak p_P$ and a Koszul-regular list $f$ generating $I_a$. Polynomial extension is free and localization is flat, by the entire tensor/localization proofs AG-RG-S01, Lemmas 1.0–1.1; exact flat tensor preserves each cycle and boundary quotient of this complex. Hence $f$ remains Koszul-regular over $W_a$. In the quotient by $f$, the $u_j$ are successive polynomial variables after translation. Multiplication by each is injective by comparison of coefficients, and remains so after localization. Applying the cone calculation one entry at a time proves that $(f,u)$ is Koszul-regular over $W_a$. Its conormal classes consequently form a basis of $L/L^2$ at $\mathfrak r$.

The decomposition above now makes $(J/J^2)_{\mathfrak q}$ a finite direct summand of a finite free $C_{\mathfrak q}$-module. Such a summand is flat by restricting the free tensor injection test. It is finitely presented: the projection onto its complementary summand sends a finite free basis to finitely many generators of the kernel of the projection onto the original summand. The whole AG-RG-S01, Lemma 1.2, therefore makes it finite free over this local ring.

From a finite generating list of $J$ choose $g_1,\ldots,g_d$ whose conormal residue classes form a basis. Relative to a basis of the finite free conormal module, their square coefficient matrix is invertible modulo the maximal ideal, hence has unit determinant and is invertible by the cofactor formula. They thus form a basis over $C_{\mathfrak q}$. In $Q_{\mathfrak p_Q}$ this says $J=(g)+J^2$. The finite module $J/(g)$ equals $J$ times itself; $J$ lies in the maximal ideal. The entire Nakayama proof in AG-RG-S01, Lemma 1.2, gives $J_{\mathfrak p_Q}=(g)$. Since $J$ is finite, kill the finitely many quotient generators by denominators outside $\mathfrak p_Q$. Their product $v_0\notin\mathfrak p_Q$ gives $J_{v_0}=(g)$ on an actual principal chart.

In $W_{\mathfrak r}$ both $(f,u)$ and $(g,s)$ generate $L_{\mathfrak r}$ and their conormal classes are bases. Their lengths agree by reduction to the residue field. Expressing the second list in the first gives a square matrix $M$ whose reduction modulo $\mathfrak r$ is invertible: $L^2\subset\mathfrak rL$, so these are precisely the two bases of $L/\mathfrak rL$. The determinant is therefore a unit. The exterior powers of the map on free generator modules give an isomorphism of the Koszul complexes. Indeed that map preserves their degree-one scalar-product functional, so the alternating deletion formula checks commutation with $d$ on every wedge; the exterior powers of the inverse matrix give the inverse complex map. Permuting $(g,s)$ to $(s,g)$ is the same calculation with a permutation matrix.

All of this can be realized on a principal neighbourhood. Include $a$ and $v_0$ in a denominator product. Include representatives outside $\mathfrak r$ of every denominator in the finite matrix and both finite generator comparisons, and the numerator of its determinant. For each asserted equality in the stalk, also include a denominator outside $\mathfrak r$ that kills its cross-difference. Their product $h\notin\mathfrak r$ gives the actual generator equalities over $W_h$ and an invertible comparison matrix there. This clearing uses annihilating denominators and never cancels a zero divisor. The complex on $(s,g)$ over $W_h$ is consequently isomorphic to the acyclic-positive complex on $(f,u)$.

Evaluate $h$ by $T_i=q_i(X)$, and call the resulting element of $Q$ $v$. Its image in $C$ agrees with that of $h$, so $v\notin\mathfrak p_Q$. Elimination and localization give
$$W_h/(s)=Q_v,\qquad J_v=(g).$$
The second equality holds because $v_0$ was a factor of $h$, and hence of $v$.

Finally $K(s;W_h)$ is a free resolution of $Q_v$. Before localization this follows by appending the successive polynomial variables $s_i$ with the cone calculation above; exact localization preserves it. Form its double complex with the finite free complex $K(g;W_h)$. The total complex is $K(s,g;W_h)$, with differential $d_s+(-1)^i d_g$ at $s$-degree $i$. Augmentation maps it to $K(g;Q_v)$ and induces an isomorphism on homology. To verify this without a spectral sequence, augment each vertical column by its quotient in degree $-1$. Every such column is exact because the fixed $g$ term is free. For a total cycle, its component of greatest $g$ degree is a vertical cycle: no component of greater $g$ degree contributes to its differential. Lift it in that exact column and subtract the resulting total boundary. This removes that component and changes only smaller $g$ degrees. The procedure terminates, because there are only finitely many $g$ degrees. It proves the augmented total complex acyclic, equivalently both surjectivity and injectivity of the augmentation on homology by lifting cycles and boundaries.

The source total complex has zero positive homology. Thus $K(g;Q_v)$ does too, and its entries generate $J_v$. We have produced the required Koszul-regular principal neighbourhood of the specified prime of $C$. Repeating for every prime proves the claim for $J$. The equations, complexes and finite eliminations include all empty variable and generator lists. ∎

<a id="more-algebra-definition-regular-ideal"></a>

#### Definition F.95: regular ideal

Reading sources: [AI Integrated Stacks, pinned More Algebra, lines 8710–8731](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L8710-L8731); [Stacks, Tag 061P](https://stacks.math.columbia.edu/tag/061P).

Let $R$ be any ring. For a finite list $f=(f_1,\ldots,f_c)$ put $J=(f_1,\ldots,f_c)$.

1. The list is **regular** when $J\ne R$ and multiplication by $f_i$ is injective on $R/(f_1,\ldots,f_{i-1})$ for every $i$.
2. It is **Koszul-regular** when every positive-degree homology module of the exterior-power Koszul complex $K(f;R)$ is zero.
3. It is **$H_1$-regular** when $H_1(K(f;R))=0$.
4. It is **quasi-regular** when the graded $R/J$-algebra map
$$
(R/J)[Z_1,\ldots,Z_c]\longrightarrow
\operatorname{gr}_J(R)=\bigoplus_{d\ge0}J^d/J^{d+1},
\quad
Z_1^{e_1}\cdots Z_c^{e_c}\longmapsto
f_1^{e_1}\cdots f_c^{e_c}\bmod J^{1+\sum_i e_i}
$$
is an isomorphism.

For an ideal $I\subset R$, each of these four conditions defines the corresponding **regular**, **Koszul-regular**, **$H_1$-regular**, or **quasi-regular ideal** by the following local requirement: for every prime $\mathfrak p$ containing $I$, there are $g\in R\setminus\mathfrak p$ and a finite list in $R_g$ generating $I_g$ and satisfying that list condition. The denominator and list may depend on the prime. This specifies all four ideal definitions over arbitrary rings.

**Verification of the formulas.** The complex in (2) and (3) has term $\bigwedge^dR^c$ and differential
$$
d(e_{i_1}\wedge\cdots\wedge e_{i_d})
=\sum_{a=1}^d(-1)^{a-1}f_{i_a}
e_{i_1}\wedge\cdots\widehat{e_{i_a}}\cdots\wedge e_{i_d}.
$$
Each pair of deleted indices contributes twice to $d^2$, with opposite signs, so this is a complex in every characteristic. Its degree-zero homology is $R/J$, since the degree-one differential has image $J$. The whole complex calculations in [F.94.A](#more-algebra-lemma-lci-presentation-independent) also apply to the empty list.

The map in (4) is well defined on coefficients modulo $J$: changing a coefficient by an element of $J$ changes a degree-$d$ value by an element of $J^{d+1}$. Multiplication of representatives respects the displayed graded products, so it is a graded algebra map. It is surjective in every degree because $J^d$ is generated by the degree-$d$ products of the $f_i$. If it is an isomorphism, degree one gives precisely
$$
(R/J)^c\overset{\sim}{\longrightarrow}J/J^2,
\qquad (a_i)\longmapsto\sum_i a_if_i\bmod J^2.
$$
Thus quasi-regularity includes the conormal basis used later.

For the empty list $J=0$, the complex consists only of $R$ in degree zero and the graded map is the identity of $R$ in degree zero. It supplies all four local tests for the zero ideal at its primes. For $I=R$, no prime contains it and the ideal conditions are vacuous. These conventions handle both the zero ring and empty charts without a Noetherian hypothesis. ∎

<a id="more-algebra-lemma-G-ring-goes-up-quasi-finite"></a>

#### Lemma F.96: G ring goes up quasi finite

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 12823–12870](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L12823-L12870).

Let $R\to R'$ be finite type between Noetherian rings. Let $\mathfrak q'\subset\mathfrak p'$ be primes of $R'$ contracting to $\mathfrak q\subset\mathfrak p$ in $R$, and assume the map is quasi-finite at $\mathfrak p'$.

1. If $\widehat{R_{\mathfrak p}}\otimes_R\kappa(\mathfrak q)$ is geometrically regular over $\kappa(\mathfrak q)$, then $\widehat{R'_{\mathfrak p'}}\otimes_{R'}\kappa(\mathfrak q')$ is geometrically regular over $\kappa(\mathfrak q')$.
2. If all formal fibres of $R_{\mathfrak p}$ are geometrically regular, the same holds for $R'_{\mathfrak p'}$.
3. A quasi-finite algebra over a Noetherian G-ring is a G-ring.

**Proof.** Put $A=\widehat{R_{\mathfrak p}}$, $B=\widehat{R'_{\mathfrak p'}}$, $k=\kappa(\mathfrak q)$ and $E=\kappa(\mathfrak q')$. The injection $R/\mathfrak q\to R'/\mathfrak q'$ gives a field map $k\to E$: nonzero elements remain nonzero, so invert in the target fraction field. The specified completion-factor construction [F.26](#algebra-lemma-completion-at-quasi-finite-prime) supplies an isomorphism of $R'$-algebras
$$T=A\otimes_RR'\cong B\times D,$$
whose projection onto $B$ is the natural completed-local map. No finiteness assertion about the unneeded second factor is required.

The ring $A$ is Noetherian by AG-CA-19, Theorem 3.3, and $T$ is a finite-type $A$-algebra, hence Noetherian by the earlier Hilbert basis theorem. Tensor associativity identifies
$$T\otimes_{R'}E\cong(A\otimes_Rk)\otimes_kE.$$
The left ring is Noetherian: writing $U=R'\setminus\mathfrak q'$, it equals $U^{-1}(T/\mathfrak q'T)$. The hypothesis makes $A\otimes_Rk$ geometrically regular, so the field-extension assertion [F.52](#algebra-lemma-geometrically-regular-over-subfields), with this target Noetherianness checked, makes the displayed ring geometrically regular over $E$.

The product splitting gives
$$T\otimes_{R'}E\cong(B\otimes_{R'}E)\times(D\otimes_{R'}E).$$
For any finite purely inseparable extension $E'/E$, the tensor of this product with $E'$ is regular. Its first factor is localization at the idempotent $(1,0)$: inverting that idempotent kills exactly the second factor. Its prime local rings are therefore prime local rings of the regular product, so it is regular. That first factor is also Noetherian, as a quotient of the Noetherian product. The same quotient argument makes $B\otimes_{R'}E$ Noetherian. The finite purely inseparable criterion [F.50](#algebra-lemma-geometrically-regular) proves (1), including zero factors, which have no prime local rings.

For (2), every prime of $R'_{\mathfrak p'}$ comes from a $\mathfrak q'\subset\mathfrak p'$ and contracts to a $\mathfrak q\subset\mathfrak p$. Its fibre is exactly the ring in (1), by localization and tensor associativity. Thus (1) proves all the required geometric-regularity assertions. The completion map is flat by AG-CA-19, Theorem 3.2, so these fibres make it regular. For (3), quasi-finiteness applies at every $\mathfrak p'$, and the G-ring hypothesis gives the assumption of (2) at its contracted $\mathfrak p$. Definition [F.92](#more-algebra-definition-G-ring) then gives a regular completion map at every prime of $R'$, exactly the G-ring condition. ∎

<a id="more-algebra-lemma-another-helper-G-ring"></a>

#### Lemma F.97: another helper G ring

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 13103–13159](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L13103-L13159).

Let $R$ be a complete Noetherian local domain with fraction field $K$. For every prime $\mathfrak q\subset R[X]$, the ring $\widehat{R[X]_{\mathfrak q}}\otimes_RK$ is regular. Moreover, if $\mathfrak q$ lies over the maximal ideal of $R$ and $0\ne\mathfrak r\subset\mathfrak q$ contracts to zero in $R$, then
$$\widehat{R[X]_{\mathfrak q}}\otimes_{R[X]}\kappa(\mathfrak r)$$
is geometrically regular over $\kappa(\mathfrak r)$. The second assertion includes the maximal-ideal, positive-characteristic case of the reading source.

**Proof.** Choose the finite regular complete local subring $A_0\subset R$ from [F.25](#algebra-lemma-complete-local-Noetherian-domain-finite-over-regular), and put $F=\operatorname{Frac}(A_0)$. A finite-dimensional domain over $F$ is a field: multiplication by a nonzero element is an injective endomorphism of a finite-dimensional vector space, hence surjective and has an inverse element. Therefore $R\otimes_{A_0}F$ is a field containing $R$ and equals $K$. In particular $K/F$ is finite.

Contract $\mathfrak q$ to $\mathfrak q_0\subset A_0[X]$. Applying [F.27](#algebra-lemma-completion-finite-extension) to the finite map $A_0[X]\to R[X]$ gives
$$\widehat{A_0[X]_{\mathfrak q_0}}\otimes_{A_0[X]}R[X]
\cong\prod_i\widehat{R[X]_{\mathfrak q_i}},$$
where the finitely many $\mathfrak q_i$ are all primes above $\mathfrak q_0$, including $\mathfrak q$. Tensoring over $R$ with $K$ identifies the left side with
$$\bigl(\widehat{A_0[X]_{\mathfrak q_0}}\otimes_{A_0}F\bigr)\otimes_FK.$$
The ring in parentheses is geometrically regular by the first assertion of [F.110](#more-algebra-lemma-helper-G-ring). Its tensor with $K$ is Noetherian, since $K/F$ is finite, and is regular by [F.52](#algebra-lemma-geometrically-regular-over-subfields). On the right it is the product of the rings $\widehat{R[X]_{\mathfrak q_i}}\otimes_RK$. Each factor is localization of that product at its factor idempotent, so its local rings are regular and it is Noetherian. This proves the first assertion for every prime, without a formal-smoothness criterion for regularity.

For the second assertion set $E=\kappa(\mathfrak r)$. The prime $\mathfrak r$ remains nonzero in $K[X]$: choose a nonzero polynomial in it, and localization is injective because $R[X]$ is a domain. Its extension is a proper prime, by the localization correspondence, and hence is generated by an irreducible polynomial of positive degree in the Euclidean ring $K[X]$. Thus $E=K[X]/\mathfrak rK[X]$ is finite over $K$. The equality with the residue field follows because this quotient is already a field containing the image of $R[X]/\mathfrak r$ and all its fractions.

Fix a finite purely inseparable extension $L/E$. It is finite over $K$. Choose finitely many algebraic field generators of $L/K$ and multiply each by a nonzero element of $R$ so that its monic equation has coefficients in $R$: for a degree-$d$ equation, the coefficient of degree $j$ is multiplied by the $(d-j)$th power of that scalar. The resulting integral generators define a finite domain $B\subset L$, $R\subset B$, with fraction field $L$. The ring $B$ is complete local, as follows directly from [F.27](#algebra-lemma-completion-finite-extension) applied to the complete ring $R$ at its maximal ideal. Its left side is $B$, so
$$B\cong\prod_j\widehat{B_{\mathfrak n_j}}.$$
Integral maximal-ideal correspondence makes the $\mathfrak n_j$ exactly its maximal ideals. Each factor is nonzero, since its residue-field quotient is nonzero. A domain has only the idempotents zero and one: $e(1-e)=0$ proves this. Hence there is exactly one factor. The resulting unique maximal ideal makes $B=B_{\mathfrak n}$, and the natural isomorphism identifies it with its maximal-adic completion. Finiteness over Noetherian $R$ also makes $B$ Noetherian.

Let $a\in L$ be the image of $X$ through $R[X]\to E\to L$, and let $\mathfrak r'=\ker(B[X]\to L)$ for the map evaluating $X$ at $a$. The quotient image is a domain containing $B$, so its fraction field contains $\operatorname{Frac}(B)=L$ and equals $L$. Thus $\kappa(\mathfrak r')=L$, and $\mathfrak r'$ contracts to $\mathfrak r$ in $R[X]$. Its extension to $L[X]$ is exactly $(X-a)$.

Put $H=\widehat{R[X]_{\mathfrak q}}$. The finite map $R[X]\to B[X]$ and F.27 identify the tested extension with
$$\begin{aligned}
\bigl(H\otimes_{R[X]}E\bigr)\otimes_EL
&=H\otimes_{R[X]}L\\
&\cong\prod_i\bigl(\widehat{B[X]_{\mathfrak q_i}}\otimes_{B[X]}L\bigr),
\end{aligned}$$
where $\mathfrak q_i$ run over the primes above $\mathfrak q$. In each factor tensor first with $L=\operatorname{Frac}(B)$ over $B$ and then impose the evaluation relation in $L[X]$. Its ring is precisely
$$\bigl(\widehat{B[X]_{\mathfrak q_i}}\otimes_BL\bigr)/(X-a).$$
The parent ring is Noetherian regular by the already proved first assertion, applied to the complete local domain $B$ and the prime $\mathfrak q_i$; no maximality assumption on this prime is needed. Polynomial differentiation $\partial/\partial X$ kills $B$. The three successive extensions through prime localization, completion and localization by $B\setminus\{0\}$ are furnished by [F.104](#more-algebra-lemma-derivation-extends). Its fraction formula shows that it kills $L$ as well, and it sends $X-a$ to one. The full hypersurface argument [F.122](#more-algebra-lemma-quotient-regular) therefore makes this quotient regular. A zero quotient is included. A finite product of regular Noetherian rings is regular: each prime contains all but one factor idempotent and its local ring is the corresponding factor local ring. The tested fibre is consequently regular for every $L/E$. It is Noetherian as a localized quotient of $H$ before the finite field extension. Criterion [F.50](#algebra-lemma-geometrically-regular) proves the claimed geometric regularity. ∎

<a id="more-algebra-lemma-cartier-equality"></a>

#### Lemma F.98: cartier equality

Reading source: [Stacks, Tag 07E1](https://stacks.math.columbia.edu/tag/07E1).

For a finitely generated field extension $K/k$, the spaces of differentials and first conormal homology are finite-dimensional, and
$$
\dim_K\Omega_{K/k}-\dim_K H_1(L_{K/k})
=\operatorname{trdeg}_k K.
$$

**Proof.** Put $d=\operatorname{trdeg}_k K$. Apply the explicit monic-tower construction in [F.23](#algebra-lemma-colimit-syntomic) to a finite field-generating list for $K/k$. It gives a domain $C\subset K$ containing that list and having fraction field $K$. In that construction there are $d$ transcendence variables, $r$ algebraic tower variables and one inverse variable. Consequently its polynomial presentation has
$$
N=d+r+1\quad\text{variables},\qquad c=r+1\quad\text{equations}.
$$
The first equation is $hZ-1$ for the chosen nonzero denominator polynomial $h$. The remaining equations, after imposing this first equation, are the successive monic minimal polynomials in the tower. Multiplication by $hZ-1$ is injective: the lowest nonzero coefficient of a polynomial in its product with $hZ-1$ is the negative of that coefficient. Each subsequent monic equation is injective on its polynomial ring by its highest-coefficient calculation. Thus this ordered list is regular, exactly as in the construction of F.23.

Write $C=k[X_1,\ldots,X_N]/I$. [F.74](#algebra-lemma-regular-quasi-regular) identifies $I/I^2$ with $C^c$ on the equation classes. Polynomial differentials identify the other term with $C^N$ on $dX_i$. Presentation comparison [F.11](#algebra-lemma-NL-homotopy) and localization [F.65](#algebra-lemma-localize-NL), applied at all nonzero elements of the domain $C$, therefore identify the first conormal homology and the differential module of $K/k$ with the kernel and cokernel of a linear map
$$
D:K^c\longrightarrow K^N.
$$
Localization is exact by [S01, Lemma 1.1](AG-RG-S01.md), so it preserves the kernel and cokernel used in this comparison.

If $\rho$ is the rank of $D$, choosing bases for its image and extending them to bases gives
$$
\dim_K\ker D=c-\rho,\qquad
\dim_K\operatorname{coker}D=N-\rho.
$$
Their difference is $N-c=d$, and both numbers are finite. This proves the asserted equality without a separability hypothesis. Equivalently the parameter count is $\dim C=d=\operatorname{trdeg}_k K$, as proved for finite-type domains in AG-CA-09, Theorem 4.2. Empty transcendence or tower lists obey the same count, including $K=k$.
∎

<a id="more-algebra-lemma-check-G-ring-easy"></a>

#### Lemma F.99: check G ring easy

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 12803–12821](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L12803-L12821).

A Noetherian ring $R$ is a G-ring exactly when, for every pair of primes $\mathfrak q\subset\mathfrak p$, the algebra
$$
\widehat{(R/\mathfrak q)_{\mathfrak p}}\otimes_{R/\mathfrak q}\kappa(\mathfrak q)
$$
is geometrically regular over $\kappa(\mathfrak q)$. The completion is at the maximal ideal of the displayed local quotient.

**Proof.** Fix $\mathfrak p$ and put $A=R_{\mathfrak p}$, $\mathfrak m=\mathfrak pA$. Primes of $A$ correspond exactly to primes $\mathfrak q\subset\mathfrak p$ of $R$, by extension and contraction in localization. Their residue fields are the same $\kappa(\mathfrak q)=\operatorname{Frac}(R/\mathfrak q)$: tensoring with that field already inverts every denominator outside $\mathfrak p$.

Since $A$ is Noetherian, both $\mathfrak qA$ and $A/\mathfrak qA$ are finite $A$-modules. The whole completion exactness and tensor theorem AG-CA-19, Theorem 3.1 applied to
$$0\longrightarrow\mathfrak qA\longrightarrow A\longrightarrow A/\mathfrak qA\longrightarrow0$$
gives the natural ring identification
$$
\widehat A/\mathfrak q\widehat A
\ \cong\ \widehat{A/\mathfrak qA}
=\widehat{(R/\mathfrak q)_{\mathfrak p}}.
$$
The completion topology on the quotient is the correct maximal-ideal topology: its degree-$r$ quotient is $A/(\mathfrak m^r+\mathfrak qA)$. The kernel image is $\mathfrak q\widehat A$, since the tensor map from the finite ideal sends its generators and coefficients to their products in $\widehat A$.

Because $\mathfrak q$ annihilates $\kappa(\mathfrak q)$, the defining balanced tensor relations now give
$$
\widehat A\otimes_A\kappa(\mathfrak q)
\cong \widehat A\otimes_R\kappa(\mathfrak q)
\cong(\widehat A/\mathfrak q\widehat A)\otimes_{R/\mathfrak q}\kappa(\mathfrak q).
$$
Explicitly the last map sends $\widehat a\otimes\lambda$ to $(\widehat a\bmod\mathfrak q\widehat A)\otimes\lambda$. Its inverse chooses a representative; changing the representative adds products by elements of $\mathfrak q$, whose tensors vanish. The first identity holds because the inverted denominators act invertibly in both factors. These maps preserve the specified residue-field algebra structures.

The entire AG-CA-19, Theorem 3.2, makes $A\to\widehat A$ flat. Thus it is regular precisely when all its residue-field fibres are geometrically regular, by the regular-map definition. The identities above identify those fibres with exactly the algebras in the assertion. By [F.92](#more-algebra-definition-G-ring), being a G-ring means that this regularity holds at every $\mathfrak p$. Applying the equivalence at each prime proves both directions. If $R=0$, there are no primes and the two conditions are vacuous. ∎

<a id="completion-flat-local-map"></a>

#### Lemma F.99A: completion of a flat local map

Reading sources: AG-CA-19, Proposition 2.2 and Theorems 3.2–3.3; AG-CA-08, Theorems 4.2 and 2.1.

If $(A,\mathfrak m)\to(B,\mathfrak n)$ is a flat local map of Noetherian local rings, its induced map on maximal-ideal completions $\widehat A\to\widehat B$ is faithfully flat. The residue fields may differ.

**Proof.** Since $\mathfrak m^r$ maps into $\mathfrak n^r$, the finite-quotient maps $A/\mathfrak m^r\to B/\mathfrak n^r$ commute with their transitions. Their inverse limit defines the asserted map.

The entire completion proofs AG-CA-19, Proposition 2.2 and Theorem 3.3, make the completions Noetherian and complete, with
$$\widehat A/\mathfrak m\widehat A=A/\mathfrak m=\kappa,
\qquad \widehat B/\mathfrak n\widehat B=B/\mathfrak n.$$
These are local rings with the indicated extended maximal ideals. Explicitly, an element whose residue is nonzero has an inverse modulo the extended ideal. Its product with a chosen inverse is $1-j$; the series $\sum_{r\geq0}j^r$ converges in the complete ring and inverts this product. Thus every element outside the extended maximal ideal is a unit. The completion map sends $\mathfrak m\widehat A$ into $\mathfrak n\widehat B$, so it is local.

Choose a free $A$-resolution $F_\bullet\to\kappa$ by the whole construction [AG-RG-S01, Lemma 1.A](AG-RG-S01.md). The full AG-CA-19, Theorem 3.2, proves $A\to\widehat A$ flat, so $F_\bullet\otimes_A\widehat A$ is an exact free $\widehat A$-resolution of $\kappa\otimes_A\widehat A=\kappa$. The same theorem makes $\widehat B$ flat over $B$, and the given flatness of $B/A$ then makes it flat over $A$ by tensor associativity. Consequently tensoring the original resolution with $\widehat B$ is exact in positive degrees, and
$$
\operatorname{Tor}^{\widehat A}_1(\kappa,\widehat B)
=H_1\bigl((F_\bullet\otimes_A\widehat A)
\otimes_{\widehat A}\widehat B\bigr)
=H_1(F_\bullet\otimes_A\widehat B)=0.
$$

Apply the complete local criterion AG-CA-08, Theorem 4.2, to the actual local map of Noetherian rings $\widehat A\to\widehat B$ and the module $\widehat B$. This module is finite over the stipulated target $\widehat B$, which is the required finiteness condition; no finiteness over $\widehat A$ is being assumed. The vanishing just proved gives flatness.

Its closed fibre is nonzero: $\mathfrak m\widehat B\subset\mathfrak n\widehat B$, so $\widehat B/\mathfrak m\widehat B$ surjects onto the nonzero field $B/\mathfrak n$. The entire local faithful-flatness proof AG-CA-08, Theorem 2.1, therefore makes the map faithfully flat. This proves the full assertion without identifying the two residue fields. ∎

<a id="more-algebra-lemma-check-G-ring-maximal-ideals"></a>

#### Lemma F.100: check G ring maximal ideals

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 13001–13037](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L13001-L13037).

A Noetherian ring $R$ is a G-ring if and only if $R_{\mathfrak m}$ has geometrically regular formal fibres for every maximal ideal $\mathfrak m$.

**Proof.** If $R$ is a G-ring, definition [F.92](#more-algebra-definition-G-ring) gives the stated property at every maximal ideal. Conversely assume those properties, and fix any prime $\mathfrak p\subset R$. Choose a maximal ideal $\mathfrak m\supset\mathfrak p$. Put $C=\widehat{R_{\mathfrak m}}$. The local completion map $R_{\mathfrak m}\to C$ is faithfully flat by AG-CA-19, Theorem 3.2. Hence its fibre at $\mathfrak pR_{\mathfrak m}$ is nonzero. Choose a prime of that fibre and take its preimage $\mathfrak p'\subset C$; the residue-field map is injective, so its contraction is exactly $\mathfrak pR_{\mathfrak m}$. This is the prime lifting supplied by faithful flatness.

Set $B=C_{\mathfrak p'}$ and $\widehat B=\widehat{C_{\mathfrak p'}}$. The map $R_{\mathfrak p}\to B$ is local and flat: it is induced by the localized completion map, and its closed prime contraction is $\mathfrak pR_{\mathfrak p}$. A local map sends every power of the source maximal ideal into the corresponding power of the target maximal ideal. Taking inverse limits therefore constructs the map $\widehat{R_{\mathfrak p}}\to\widehat B$. Naturality of reduction makes both squares in the actual diagram commute:
$$\begin{array}{ccccc}
C&\longrightarrow&B&\longrightarrow&\widehat B\\
\uparrow&&\uparrow&&\uparrow\\
R_{\mathfrak m}&\longrightarrow&R_{\mathfrak p}&\longrightarrow&\widehat{R_{\mathfrak p}}.
\end{array}$$

All rings here are Noetherian. By assumption and completion flatness, the first vertical map $R_{\mathfrak m}\to C$ is regular. The map $C\to B$ is regular: localization is flat; at a prime of $C$ its fibre is its residue field if the multiplicative set avoids that prime, and the zero ring otherwise. Every extension of that residue field leaves a field, hence a regular ring. Also $C$ is complete Noetherian local, so [F.132](#more-algebra-proposition-Noetherian-complete-G-ring) makes it a G-ring and gives regularity of $B\to\widehat B$. Applying [F.124](#more-algebra-lemma-regular-composition) twice proves $R_{\mathfrak m}\to\widehat B$ regular.

This composite factors through $R_{\mathfrak p}$. It makes $\widehat B$ flat over $R_{\mathfrak p}$: tensoring any injection of $R_{\mathfrak p}$-modules with $\widehat B$ is the same as tensoring the underlying $R_{\mathfrak m}$-modules, by the localization universal property. Its fibres at primes of $R_{\mathfrak p}$ are the corresponding fibres over $R_{\mathfrak m}$, since their residue fields are identical. Thus $R_{\mathfrak p}\to\widehat B$ is regular as well.

The proved flat local map $R_{\mathfrak p}\to B$ satisfies precisely the hypotheses of [F.99A](#completion-flat-local-map), which makes the induced map $\widehat{R_{\mathfrak p}}\to\widehat B$ faithfully flat. The factorization in the right square and [F.125](#more-algebra-lemma-regular-permanence) therefore descend regularity of $R_{\mathfrak p}\to\widehat B$ to regularity of $R_{\mathfrak p}\to\widehat{R_{\mathfrak p}}$. As $\mathfrak p$ was arbitrary, F.92 says $R$ is a G-ring. For the zero ring both sets of tests are empty, so the equivalence still holds. ∎

<a id="more-algebra-lemma-conormal-sequence-H1-regular-ideal"></a>

#### Lemma F.101: conormal sequence H1 regular ideal

Reading source: [Stacks, Tag 07CX](https://stacks.math.columbia.edu/tag/07CX).

For ideals $I\subset J$ of an arbitrary ring $A$, suppose the ideal $J/I$ of $A/I$ is $H_1$-regular. Then
$$
I\cap J^2=IJ.
$$

**Proof.** The inclusion $IJ\subset I\cap J^2$ follows from $I\subset J$. We prove the other inclusion at each prime of $A$. Exact localization commutes with the intersection, the product and the quotient in this assertion; the fraction proof and the detection of a zero module are [S01, Lemma 1.1](AG-RG-S01.md). These facts will turn the local equalities into the global one.

At a prime outside $V(J)$, the ideal $J$ becomes the unit ideal, and both sides become $I$. At a prime containing $J$, localize $A$ there. The defining neighbourhood in [F.95](#more-algebra-definition-regular-ideal) supplies a finite list $g_1,\ldots,g_s\in J$ whose images generate $J/I$ and have zero first Koszul homology over $A/I$. Indeed we can lift the list from its quotient neighbourhood and localize further at the prime; exact localization preserves cycles, boundaries and their homology. In this local ring $J=I+(g_1,\ldots,g_s)$.

Take $x\in I\cap J^2$. Expanding a finite expression for $x$ as a sum of products of members of $J$ gives
$$
x=u+\sum_{i=1}^s g_i b_i,
\qquad u\in IJ,\quad b_i\in J.
$$
Terms having a factor in $I$ were absorbed in $u$; all other terms have two factors from the displayed list. Reducing modulo $I$ makes $(\bar b_i)$ a degree-one Koszul cycle because its scalar product with $(\bar g_i)$ is zero. The zero first homology says this cycle is a boundary. With the convention
$$
\partial(e_i\wedge e_j)=\bar g_i e_j-\bar g_j e_i,
$$
it is a finite sum of these displayed vectors with coefficients in $A/I$.

Lift those coefficients to $A$ and subtract the corresponding vectors $g_i e_j-g_j e_i$ from $(b_i)$. Their scalar products with $(g_i)$ are exactly zero in $A$, so this subtraction leaves $\sum_i g_i b_i$ unchanged. Its new coefficients reduce to zero modulo $I$, hence belong to $I$. The sum is therefore in $IJ$, as is $u$, proving $x\in IJ$. An empty list gives the same calculation with sum zero. No finite generation of $I$ and no Noetherian condition were used. Applying local detection to $(I\cap J^2)/IJ$ completes the proof.
∎

<a id="more-algebra-lemma-cotangent-complex-symmetric-algebra"></a>

#### Lemma F.102: cotangent complex symmetric algebra

Reading source: [Stacks, Tag 07EV](https://stacks.math.columbia.edu/tag/07EV).

Let $A$ be any ring and let
$$
0\longrightarrow K\longrightarrow A^m\xrightarrow{q}M\longrightarrow0
$$
be exact, where $M$ is finite projective. Set $C=\operatorname{Sym}_A(M)$ and let $\alpha:A[y_1,\ldots,y_m]\twoheadrightarrow C$ be the presentation induced by $q$, with kernel $J$. The natural map
$$
K\otimes_A C\longrightarrow J/J^2,
\qquad (k_1,\ldots,k_m)\otimes c
\longmapsto c\sum_i k_i y_i\bmod J^2
$$
is an isomorphism. With this identification the conormal complex and its cokernel are
$$
\operatorname{NL}(\alpha)=[K\otimes_A C\longrightarrow C^m],
\qquad \Omega_{C/A}=M\otimes_A C,
$$
where the differential is obtained from $K\hookrightarrow A^m$ by tensoring with $C$.

**Proof.** Choose a section $s:M\to A^m$ using projectivity. The map $(k,m)\mapsto k+s(m)$ identifies $K\oplus M$ with $A^m$: its inverse sends $a$ to $(a-sq(a),q(a))$. We compute the presentation using this decomposition, keeping track of its specified natural map.

For a module $V$, the symmetric algebra is the tensor algebra modulo the relations that interchange two adjacent factors. A linear map $V\to D$ into a commutative $A$-algebra extends on a pure tensor by multiplying its images; the interchange relations vanish, and these products determine the extension uniquely. This proves the symmetric-algebra universal property from the tensor construction [S01, Lemma 1.0](AG-RG-S01.md). It also gives its grading by tensor degree, with degree zero $A$ and degree one $V$.

That property and the algebra tensor universal property give inverse maps
$$
\operatorname{Sym}_A(K\oplus M)
\ \cong\ \operatorname{Sym}_A(K)\otimes_A C.
$$
In one direction send $k$ to $k\otimes1$ and $m$ to $1\otimes m$. In the other direction use the inclusions of $K$ and $M$ into $K\oplus M$ on the two tensor factors. Both composites fix the algebra generators, hence are identities. Likewise the symmetric algebra of $A^m$ is the polynomial ring on its coordinate basis. Under these identifications $\alpha$ is the augmentation on the $K$ factor and the identity on $C$.

Grade the tensor product by $K$ degree. The direct-sum tensor formula of S01, Lemma 1.0 gives
$$
J=\bigoplus_{d\ge1}\operatorname{Sym}_A^d(K)\otimes_A C,
\qquad
J^2=\bigoplus_{d\ge2}\operatorname{Sym}_A^d(K)\otimes_A C.
$$
For the second equality, a product of positive degrees has degree at least two. Conversely each degree-$d$ term is generated by products $k_1\cdots k_d\otimes c$; when $d\ge2$ separate its first factor from the rest to express it as a product of two elements of $J$. Quotienting thus leaves precisely $K\otimes_A C$. Its generator $k\otimes c$ corresponds in the original coordinates to $c\sum_i k_i y_i$, proving exactly the natural isomorphism in the statement, independently of the auxiliary section.

Relative differentiation sends this linear polynomial to $\sum_i k_i\,dy_i$. The polynomial differentials are free on these $m$ symbols, so the displayed complex has exactly the claimed differential. Tensoring the split sequence with $C$ remains split exact, and its cokernel is $M\otimes_A C$. This proves the assertion about $\Omega_{C/A}$ as well, including zero modules and the empty coordinate basis.

The projectivity hypothesis prevents additional conormal relations. For example let $A=k[\varepsilon]/(\varepsilon^2)$, let $M=k^2$ via $\varepsilon M=0$, and let $q:A^2\to M$ be reduction. Then $K=\varepsilon A^2$, $C=A[y_1,y_2]/(\varepsilon y_1,\varepsilon y_2)$, and $J=(\varepsilon y_1,\varepsilon y_2)$ has square zero. The source $K\otimes_A C$ is $k[y_1,y_2]^2$, whereas the vector $(y_2,-y_1)$ maps to $\varepsilon y_1y_2-\varepsilon y_2y_1=0$ in $J/J^2$ and is nonzero in that source. Thus the same conormal identity need not hold after dropping the hypothesis.
∎

<a id="more-algebra-lemma-degree-p-extension-regular"></a>

#### Lemma F.103: degree p extension regular

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 12453–12467](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L12453-L12467).

Let $R$ be a Noetherian regular ring and let $D:R\to R$ be a derivation such that $D(f)$ is a unit. For every integer-coefficient polynomial $P(Z)$, the ring $R[Z]/(P(Z)-f)$ is regular. In particular this holds for $P(Z)=Z^n$, $n\ge1$, including degree-$p$ adjunctions in characteristic $p$.

**Proof.** The whole polynomial-regularity argument AG-CA-14, Proposition 3.3 makes $V=R[Z]$ regular; Hilbert's basis theorem also makes it Noetherian. Extend the derivation by the explicit formula
$$D_V\!\left(\sum_i a_iZ^i\right)=\sum_i D(a_i)Z^i.$$
Coefficient convolution and the product rule in $R$ prove the product rule for $D_V$, and additivity is coefficientwise. The identity $D(1)=2D(1)$ gives $D(1)=0$; additivity and additive inverses then give $D(n)=0$ for every integer scalar $n$. Hence $D_V(P)=0$ and
$$D_V(P-f)=-D(f).$$
This is a unit already in $V$, and remains a unit in its quotient. The entire hypersurface result [F.122](#more-algebra-lemma-quotient-regular), with its localized-derivation and parameter-quotient proofs, applies to $V$ and $P-f$. It makes the quotient regular, for every specified $P$. Constant polynomials, units and the zero quotient obey the same calculation. ∎

<a id="more-algebra-lemma-derivation-extends"></a>

#### Lemma F.104: derivation extends

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 12363–12405](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L12363-L12405).

Let $D:R\to R$ be a derivation of an arbitrary ring.

1. It extends uniquely to every localization $U^{-1}R$.
2. For every ideal $I$, it has a canonical continuous extension to $\widehat R=\varprojlim_n R/I^n$, with its inverse-limit topology. This extension is unique among continuous extensions.
3. If $R\subset R'$ is finite type, $g\in R$ is a nonzerodivisor in $R'$, and the inclusions identify $R_g=R'_g$, then some $g^ND$ extends to a derivation $R'\to R'$.

**Proof.** For (1), the map $r\mapsto r+\epsilon D(r)$ into $(U^{-1}R)[\epsilon]/(\epsilon^2)$ is a ring map. Each $s\in U$ has image with inverse
$$s^{-1}-\epsilon s^{-2}D(s).$$
Localization's universal property therefore extends the map. Its constant component is the structural map on the localized ring, so its second component is a derivation, with formula
$$D_U(r/s)=D(r)/s-rD(s)/s^2.$$
This constructs a well-defined derivation even with zero divisors. Any extension must have that formula by differentiating $s\,s^{-1}=1$, proving uniqueness.

For (2), a product of $n+1$ ideal elements differentiates into $I^n$; finite sums and coefficient derivatives give
$$D(I^{n+1})\subset I^n\qquad(n\ge1).$$
For a compatible family $a=(a_n)\in\widehat R$, choose $r\in R$ representing $a_{n+1}$ and define its derivative's $n$th coordinate as $D(r)\bmod I^n$. Replacing $r$ changes its derivative by an element of $I^n$, so this is well defined. Comparing representatives of $a_{n+2}$ and $a_{n+1}$ gives compatibility of these derivative coordinates. They therefore define $\widehat D(a)\in\widehat R$.

Represent $a,b$ modulo $I^{n+1}$ by $r,s$. Their sum and product are represented by $r+s,rs$. The identities in $R$, reduced modulo $I^n$, give
$$
\widehat D(a+b)_n=\widehat D(a)_n+\widehat D(b)_n,\qquad
\widehat D(ab)_n=a_n\widehat D(b)_n+b_n\widehat D(a)_n.
$$
Thus the inverse-limit map is a derivation and extends $D$ through the canonical map $R\to\widehat R$.

Write $K_n=\ker(\widehat R\to R/I^n)$. The formula gives $\widehat D(K_{n+1})\subset K_n$, proving continuity. Canonical images of $R$ are dense: any coordinate modulo $I^m$ has a representative in $R$, matching all lower coordinates too. If another continuous extension were given, their difference would be a continuous additive map vanishing on this dense image. For a prescribed output coordinate choose a sufficiently deep input kernel mapped into its kernel by continuity, and choose an $R$-representative matching that input coordinate. The difference has zero prescribed output coordinate. This holds for every coordinate, and the inverse limit is separated, so the difference is zero. The construction uses the inverse-limit kernels, without assuming an infinitely generated ideal's extended powers agree with those kernels.

For (3), $R'$ embeds in $R'_g$: if $x/1=0$, some $g^j x=0$, and injectivity of multiplication by $g$ repeatedly gives $x=0$. Choose algebra generators $x_1,\ldots,x_s$ of $R'/R$. The localized equality writes each as a fraction from $R$ with denominator a power of $g$; the embedding just proved makes those cleared equalities hold in $R'$. Thus a common $n\ge0$ satisfies $g^nx_i\in R$ for every $i$.

Inside the common localization apply (1). The product rule, including $D(g^n)=ng^{n-1}D(g)$ when $n>0$, gives
$$g^{n+1}D_U(x_i)=gD(g^nx_i)-n(g^nx_i)D(g)\in R.$$
For $n=0$ the second term is zero and the same identity holds directly. Multiplying a derivation by the scalar $g^{n+1}$ still gives a derivation. It sends $R$ into $R$ and each generator into $R$, so repeated product and sum rules send every polynomial expression in the generators into $R'$. Since this is the restriction of an actual derivation on the localization, all relations in $R'$ are respected. Restriction therefore gives the required extension with $N=n+1$. Empty generator lists and the zero ring cause no exception. ∎

<a id="more-algebra-lemma-find-D"></a>

#### Lemma F.105: find D

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 12469–12520](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L12469-L12520).

Let $p$ be prime, let $B$ be a domain of characteristic $p$, and let $f\in B$ be outside $\operatorname{Frac}(B)^p$. If $B$ is finite type over a complete Noetherian local ring, there is a derivation $D:B\to B$ with $D(f)\ne0$.

**Proof.** Let $R_1\to B$ be such a finite-type map. Its kernel is prime. Exact completion on finite modules AG-CA-19, Theorem 3.1 identifies the quotient $R_1/\ker(R_1\to B)$ with its maximal-adic completion: tensor the finite quotient with $\widehat{R_1}=R_1$. Thus its image is again a complete Noetherian local domain, of characteristic $p$. By [F.25](#algebra-lemma-complete-local-Noetherian-domain-finite-over-regular) it is finite over an embedded power-series ring $R=k[[X_1,\ldots,X_n]]$. A finite module generating list for the image ring, together with the finite algebra generating list for $B$ over that image, makes $B$ finite type over $R$. In particular $R\subset B$ is injective.

Put $K_0=\operatorname{Frac}(R)$. Noether normalization AG-CA-09, Corollary 3.2 supplies algebraically independent parameters in $B\otimes_RK_0$ over which that algebra is finite. Multiply each parameter by a nonzero scalar of $R$ to put it in $B$; independence and the parameter algebra over $K_0$ are unchanged. Write the resulting parameters as $y_1,\ldots,y_d$, and put $A=R[y_1,\ldots,y_d]$. Choose finite $A$-algebra generators $b_i$ of $B$. Each satisfies a monic equation over $K_0[y]$. There is a common nonzero $g\in R$ for which every coefficient belongs to $A_g$.

Write such an equation as $b_i^{e_i}+\sum_{j<e_i}c_{ij}b_i^j=0$. Choose $N$ such that $g^{N(e_i-j)}c_{ij}\in A$ for every $i,j$. Multiplying by $g^{Ne_i}$ gives a monic equation over $A$ for $g^Nb_i$. Consequently
$$B'=A[g^Nb_1,\ldots,g^Nb_t]\subset B$$
is finite over $A$: reduce powers of each generator using its monic equation, obtaining a finite spanning list of bounded monomials. Moreover $B'_g=B_g$, since all $b_i$ belong to $B'_g$. A sufficiently large $r\geq0$ therefore puts $f'=g^{pr}f$ in $B'$. The fraction fields of $B'$ and $B$ agree; call this field $L$. Since $g^{pr}=(g^r)^p$, membership of $f'$ in $L^p$ would imply membership of $f$ in $L^p$. Thus $f'\notin L^p$. Finiteness over $A$ makes $L$ finite over $K=\operatorname{Frac}(A)$: the localization $B'\otimes_AK$ is a finite-dimensional domain, hence a field, and contains all fractions of $B'$.

The complete power-series calculation [F.120](#more-algebra-lemma-power-series-ring-subfields) supplies a nonempty downward-directed family of coefficient subrings
$$A_J=k_J[[X_1^p,\ldots,X_n^p]][y_1^p,\ldots,y_d^p]\subset A,$$
with $A$ finite free over $A_J$ and fraction fields $K_J$ containing $K^p$, whose intersection is $K^p$. Here $J$ runs over finite subsets of an absolute $p$-basis of $k$, and $k_J$ is generated over $k^p$ by the basis elements outside $J$; no perfection hypothesis is imposed. The finite-extension assertion of [F.112](#more-algebra-lemma-intersection-subfields) gives $\bigcap_JL^pK_J=L^p$. Since $f'\notin L^p$, choose $J$ with $f'\notin L^pK_J$.

The relative $p$-basis theorem [F.119](#more-algebra-lemma-p-basis) extends $\{f'\}$ to a $p$-basis of $L/K_J$. Indeed its first degree is $p$: a proper monic factor of $T^p-(f')^p=(T-f')^p$ has coefficient $-ef'$, $1\leq e<p$, and would put $f'$ in $L^pK_J$. The coordinate derivation from the full presentation in F.119 consequently gives $\delta:L\to L$ killing $K_J$ with $\delta(f')=1$.

The ring $B'$ is finite over $A_J$, by the two finite module spanning lists. Choose $A_J$-module generators $v_1,\ldots,v_s$. Write each $\delta(v_i)$ as a fraction of $B'$ and let $h\in B'\setminus\{0\}$ be the product of their nonzero denominators. Then $D'=h\delta$ sends every $v_i$ into $B'$ and kills $A_J$. Differentiating an arbitrary expression $\sum_i a_iv_i$, $a_i\in A_J$, proves $D'(B')\subset B'$. Its value on $f'$ is $h\ne0$.

Finally $B$ is finite type over $B'$, $g$ is a nonzerodivisor in both domains, and $B'_g=B_g$. The third assertion of [F.104](#more-algebra-lemma-derivation-extends) therefore gives $s\geq0$ for which $g^sD'$ restricts to a derivation $D:B\to B$. In the common fraction field, the fraction formula and $D'(g^{pr})=prg^{pr-1}D'(g)=0$ yield
$$D(f)=g^sD'(g^{-pr}f')=g^{s-pr}h\ne0.$$
Its membership in $B$ follows from the restriction just proved; the displayed expression proves its nonvanishing. Empty parameter lists or a coefficient field as base require no changes. ∎

<a id="more-algebra-lemma-formally-smooth"></a>

#### Lemma F.106: formally smooth

Reading source: [Stacks, Tag 07EC](https://stacks.math.columbia.edu/tag/07EC).

Let $\varphi:R\to S$ be continuous. If the underlying algebra map is formally smooth, it is formally smooth when $R$ has any linear topology and $S$ has a pre-adic topology. Moreover, if the topologies on $R$ and $S$ are given by the powers of ideals $\mathfrak m$ and $\mathfrak n$, formal smoothness is unchanged when the topology on $R$ is replaced by the discrete topology.

**Proof.** We specify the topological test. Give a ring $D$ and its quotient $D/J$ the discrete topology, where $J^2=0$. Fix continuous maps $a:R\to D$ and $b:S\to D/J$ such that $b\varphi$ is the reduction of $a$. A solution is a continuous $R$-algebra map $c:S\to D$ reducing to $b$. Topological formal smoothness requires a solution for every such test; algebraic formal smoothness uses the same tests without continuity conditions. The latter definition is AG-CA-17, Section 1.

For a pre-adic topology on $S$, choose $\mathfrak n$ whose powers form a neighbourhood basis at zero. A ring map from $S$ to a discrete ring is continuous precisely when its kernel contains some $\mathfrak n^r$: continuity at zero gives this condition, and translation gives continuity at every point. Algebraic formal smoothness supplies a lift $c$ in the test. Continuity of $b$ gives $b(\mathfrak n^r)=0$ for some $r\ge1$. Thus $c(\mathfrak n^r)\subset J$, and multiplication of two such ideal powers gives
$$
c(\mathfrak n^{2r})\subset J^2=0.
$$
The lift is therefore continuous. The linear topology on $R$ needs no further restriction beyond continuity of the stipulated maps.

Now assume both topologies are given by the stated ideal powers. If formal smoothness holds with discrete $R$, any test with continuous $a$ is among its tests, so the same property holds with the original topology on $R$. In the other direction, start with a test having discrete $R$; the map $a$ is initially allowed to be arbitrary. Continuity of $\varphi$ gives an integer $s\ge1$ with $\varphi(\mathfrak m^s)\subset\mathfrak n$. For the integer $r$ supplied by $b$ as above, compatibility implies
$$
a(\mathfrak m^{sr})\subset J,
\qquad a(\mathfrak m^{2sr})=0.
$$
Hence $a$ was continuous for the $\mathfrak m$-power topology as well. Formal smoothness for that topology now gives the desired continuous lift. This proves both directions, with no finite-generation or Noetherian assumption. Neither completeness nor separatedness of $S$ was required.
∎

<a id="more-algebra-lemma-formally-smooth-completion"></a>

#### Lemma F.107: formally smooth completion

Reading source: [Stacks, Tag 07ED](https://stacks.math.columbia.edu/tag/07ED).

Let $R\to S$ be a continuous map of Noetherian rings with topologies defined by finitely generated ideals $\mathfrak m\subset R$ and $\mathfrak n\subset S$. Write $\widehat R$ and $\widehat S$ for the corresponding completions. The following three properties are equivalent: $R\to S$ is formally smooth for the $\mathfrak n$-power topology; $R\to\widehat S$ is formally smooth for the $\mathfrak n\widehat S$-power topology; and $\widehat R\to\widehat S$ is formally smooth for that target topology.

**Proof.** The continuous map induces the last completion map by applying it to compatible finite-order coordinates. AG-CA-19, Proposition 2.2 proves the exact quotient identities
$$
\widehat R/\mathfrak m^q\widehat R=R/\mathfrak m^q,
\qquad
\widehat S/\mathfrak n^q\widehat S=S/\mathfrak n^q
\quad(q\ge1).
$$
These identities use the canonical maps and commute with all transition maps. That proposition also proves completeness for the extended-ideal topologies.

A continuous homomorphism $u:S\to D$ to a discrete ring kills some $\mathfrak n^q$. Its factorization through $S/\mathfrak n^q$ and the second displayed identity define a homomorphism $\widehat u:\widehat S\to D$ killing $\mathfrak n^q\widehat S$. It extends $u$. It is the only continuous extension: any other extension kills a possibly different ideal power; pass to an exponent at least as large as both, where its map is determined by the same surjective finite quotient. Restriction and extension are inverse, and they commute with maps between discrete target rings. The identical argument applies to $R$ and $\widehat R$.

Use the tests defined in [F.106](#more-algebra-lemma-formally-smooth), with $D\to D/J$ square-zero. First compare $R\to S$ with $R\to\widehat S$. Keep the structural map from $R$ fixed. The just-proved correspondence identifies every continuous map to $D/J$, every continuous lift to $D$, and their compatibility with $R$. Thus one test has a solution exactly when its counterpart does.

Next compare $R\to\widehat S$ with $\widehat R\to\widehat S$. With the original topology on the base, extension and restriction identify the structural maps to both discrete test rings. Compatibility after restriction implies compatibility after extension: the two continuous maps from $\widehat R$ agree by uniqueness of extension. The test diagrams and their dotted lifts therefore correspond in both directions. Finally F.106 identifies each of these topological-base tests with the tests using discrete base. In particular a structural map allowed in a discrete-base test is automatically continuous when it is compatible with the continuous target map modulo $J$; that is precisely the ideal-power calculation in F.106. This proves the three equivalences in the stipulated Noetherian scope.
∎

<a id="more-algebra-lemma-gamma-commutative-diagram"></a>

#### Lemma F.108: gamma commutative diagram

Reading source: [Stacks, Tag 07E3](https://stacks.math.columbia.edu/tag/07E3).

Consider a commutative square of fields with arrows $k\to k'$, $k\to K$, $k'\to K'$ and $K\to K'$. Assume $k'/k$ and $K'/K$ are finitely generated. For the natural maps
$$
\alpha:\Omega_{K/k}\otimes_KK'\longrightarrow\Omega_{K'/k'},
\qquad
\beta:H_1(L_{K/k})\otimes_KK'\longrightarrow H_1(L_{K'/k'}),
$$
all four kernels and cokernels are finite-dimensional, and
$$
\dim\ker\alpha-\dim\operatorname{coker}\alpha
-\dim\ker\beta+\dim\operatorname{coker}\beta
=\operatorname{trdeg}_k k'-\operatorname{trdeg}_K K'.
$$

**Proof.** All vector spaces below are over $K'$, and all omitted scalar extensions are to $K'$. Apply the full field-transitivity proof [F.131](#more-algebra-lemma-transitivity-gamma) to $k\subset k'\subset K'$ and $k\subset K\subset K'$. Let
$$
V=H_1(L_{K'/k}),\qquad U=\Omega_{K'/k}.
$$
For the first row put $P_1=H_1(L_{k'/k})\otimes_{k'}K'$, $W_1=H_1(L_{K'/k'})$, $Q_1=\Omega_{k'/k}\otimes_{k'}K'$ and $Z_1=\Omega_{K'/k'}$. For the second put $P_2=H_1(L_{K/k})\otimes_KK'$, $W_2=H_1(L_{K'/K})$, $Q_2=\Omega_{K/k}\otimes_KK'$ and $Z_2=\Omega_{K'/K}$. The two exact rows are
$$
0\longrightarrow P_i\longrightarrow V\longrightarrow W_i
\longrightarrow Q_i\longrightarrow U\longrightarrow Z_i\longrightarrow0
\qquad(i=1,2).
$$
Their first injections identify $P_1,P_2$ with subspaces of $V$. Naturality of the representative and derivative maps in [F.42](#algebra-lemma-exact-sequence-NL) identifies $\beta$ with $P_2\to V\to W_1$ and $\alpha$ with $Q_2\to U\to Z_1$.

We calculate only finite defects, so no subtraction of infinite dimensions is involved. Set
$$
T=P_1\cap P_2,\quad Y=V/(P_1+P_2),\quad
A_i=\ker(Q_i\to U),\quad B_i=\operatorname{im}(Q_i\to U).
$$
Write $i_0=\dim T$, $r=\dim(P_1/T)$, $y=\dim Y$, $a_i=\dim A_i$, $j=\dim(B_1\cap B_2)$, $s=\dim(B_1/(B_1\cap B_2))$ and $z=\dim(U/(B_1+B_2))$. These are finite. Indeed [F.98](#more-algebra-lemma-cartier-equality) makes $P_1,Q_1,W_2,Z_2$ finite. The space $Y$ is a quotient of $V/P_2$, which embeds in $W_2$; $A_2$ is a quotient of $W_2$; and the space measured by $z$ is a quotient of $Z_2$. All other spaces on the list are subspaces or quotients of $P_1$ or $Q_1$.

The kernel of $\beta$ is $T$. Exactness of the first row gives an injection $V/P_1\to W_1$ with quotient $A_1$. Dividing its image by the image of $P_2$ therefore yields
$$
0\longrightarrow Y\longrightarrow\operatorname{coker}\beta
\longrightarrow A_1\longrightarrow0.
$$
For $\alpha$, its kernel consists of the elements of $Q_2$ whose image in $U$ lies in $B_1$. Mapping them into $U$ gives a surjection onto $B_1\cap B_2$ with kernel $A_2$. Its cokernel is $U/(B_1+B_2)$. Hence
$$
\dim\ker\beta=i_0,\quad \dim\operatorname{coker}\beta=y+a_1,
\qquad \dim\ker\alpha=a_2+j,\quad \dim\operatorname{coker}\alpha=z.
$$
The second row identifies $V/P_2$ with the kernel of $W_2\to Q_2$. Inside $V/P_2$, the image of $P_1$ is $P_1/T$ and has quotient $Y$. Similarly $U/B_2$ contains the image $B_1/(B_1\cap B_2)$ with quotient $U/(B_1+B_2)$. The resulting finite exact sequences give
$$
\dim P_1=i_0+r,\quad \dim W_2=r+y+a_2,
\qquad \dim Q_1=a_1+j+s,\quad \dim Z_2=s+z.
$$
Subtracting these finite numbers shows that the expression in the statement equals
$$
(a_2+j)-z-i_0+(y+a_1)
=\dim Q_1-\dim P_1-\dim Z_2+\dim W_2.
$$
F.98 applied to $k'/k$ and $K'/K$ gives the required transcendence-degree difference. This also proves finiteness of every defect without requiring $K/k$ or $K'/k'$ to be finitely generated.
∎

<a id="more-algebra-lemma-geometrically-regular-over-field"></a>

#### Lemma F.109: geometrically regular over field

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 9460–9501](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L9460-L9501).

Let $k$ have characteristic $p>0$, and let $(A,\mathfrak m,K)$ be a geometrically regular Noetherian local $k$-algebra. Let $k\subset F\subset K$ be finitely generated over $k$. Suppose a map $\varphi:k[y_1,\ldots,y_m]\to A$ has residue images $\overline y_i\in F$, with $d\overline y_1,\ldots,d\overline y_m$ a basis of $\Omega_{F/k}$. Put $\mathfrak p=\varphi^{-1}(\mathfrak m)$. Then
$$k[y_1,\ldots,y_m]_{\mathfrak p}\longrightarrow A$$
is flat, and $A/\mathfrak pA$ is regular.

**Proof.** Write $R_0=k[y_1,\ldots,y_m]_{\mathfrak p}$, $\mathfrak m_0=\mathfrak pR_0$, and $K_0=R_0/\mathfrak m_0$. The residue map embeds $K_0$ into $F$, and
$$K_0=k(\overline y_1,\ldots,\overline y_m).$$
Indeed it is the fraction field of the domain image of $k[y]$ in $K$; localizing at the kernel inverts every nonzero image. The polynomial and fraction differential formulas in AG-CA-15, Sections 1–2 and Theorem 5.1 make $\Omega_{R_0/k}$ free on $dy_i$, and make their images span $\Omega_{K_0/k}$. They are independent in that last space: a $K_0$-linear relation maps to an $F$-linear relation between the assumed basis of $\Omega_{F/k}$, so every coefficient vanishes in $F$, and hence in $K_0$. Thus
$$\Omega_{R_0/k}\otimes_{R_0}K_0\xrightarrow{\ \sim\ }\Omega_{K_0/k}.$$

The ring $R_0$ is regular local by iterating AG-CA-14, Proposition 3.3 from the field and using the definition of a regular ring at its prime localizations. For a finite purely inseparable $k'/k$, its tensor is the localization of $k'[y]$ at the images of $k[y]\setminus\mathfrak p$, and is Noetherian regular. Criterion [F.50](#algebra-lemma-geometrically-regular) therefore makes $R_0$ geometrically regular over $k$. The geometric-regularity characterization [F.133](#more-algebra-proposition-characterization-geometrically-regular) gives injectivity of the connecting map
$$\gamma_0:H_1(L_{K_0/k})\longrightarrow\mathfrak m_0/\mathfrak m_0^2.$$
The full quotient sequence [F.42](#algebra-lemma-exact-sequence-NL) gives
$$H_1(L_{K_0/k})\longrightarrow\mathfrak m_0/\mathfrak m_0^2
\longrightarrow\Omega_{R_0/k}\otimes_{R_0}K_0
\longrightarrow\Omega_{K_0/k}\longrightarrow0.$$
The last nonzero arrow is the displayed isomorphism, so exactness also makes $\gamma_0$ surjective. Hence it is an isomorphism.

All arrows in the following square are the connecting and scalar-extension maps of the same quotient presentations:
$$\begin{array}{ccc}
H_1(L_{K_0/k})\otimes_{K_0}K&\xrightarrow{\gamma_0\otimes1}&
(\mathfrak m_0/\mathfrak m_0^2)\otimes_{K_0}K\\
\downarrow&&\downarrow\\
H_1(L_{K/k})&\xrightarrow{\gamma}&\mathfrak m/\mathfrak m^2.
\end{array}$$
It commutes: a lifted polynomial relation has the same differentiated representative whether mapped first to $A$ or first to its residue field, as in F.42. The left arrow is injective by the first injection of the field-tower sequence [F.131](#more-algebra-lemma-transitivity-gamma) for $k\subset K_0\subset K$. The bottom arrow is injective by F.133 applied to the assumed geometrically regular $A$. The top arrow is an isomorphism, since tensor over a field is exact. If a vector in its upper-right space maps to zero below, take its preimage in the upper-left space. Commutativity and the two injections force that preimage, and then the vector, to be zero. This proves injectivity of the right arrow.

Choose a regular system of parameters $x_1,\ldots,x_d$ of $R_0$. Their classes are a $K_0$-basis of $\mathfrak m_0/\mathfrak m_0^2$; after scalar extension they remain a $K$-basis. The right injection says their images have independent classes in $\mathfrak m/\mathfrak m^2$. The ring $A$ is regular, by F.133. Extend those classes to a basis of this finite-dimensional $K$-space and lift the additional basis vectors to $\mathfrak m$. Nakayama's lemma [F.10](#algebra-lemma-NAK) makes the resulting list a minimal generating list for $\mathfrak m$. The complete parameter theorem AG-CA-12, Theorem 6.1 makes it a regular sequence. In particular its prefix, the images of $x_1,\ldots,x_d$, is regular in $A$, with proper generated ideal.

The map $R_0\to A$ is local by the definition of $\mathfrak p$. Therefore [F.46](#algebra-lemma-flat-over-regular) applies to these images and proves flatness. The full successive parameter-quotient result AG-CA-14, Theorem 1.1 and Corollary 1.2 makes $A/(x_1,\ldots,x_d)A$ regular local. Since the parameters generate $\mathfrak m_0$, their image ideal is exactly $\mathfrak pA$. This is the asserted regular quotient. If $d=0$, $R_0$ is a field, its flatness assertion is the vector-space argument, and the quotient is $A$ itself; the proof also covers $m=0$. ∎

<a id="more-algebra-lemma-helper-G-ring"></a>

#### Lemma F.110: helper G ring

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 12915–12963](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L12915-L12963).

Let $A_0$ be a regular complete Noetherian local domain, put $P=A_0[Y_1,\ldots,Y_m]$, and let $\mathfrak q\subset P$ be any prime. Both
$$\widehat{P_{\mathfrak q}}\otimes_{A_0}\operatorname{Frac}(A_0)
\quad\hbox{and}\quad
\widehat{P_{\mathfrak q}}\otimes_P\operatorname{Frac}(P)$$
are geometrically regular over their displayed fields. The second assertion contains the power-series helper; the first is the additional form used in F.97.

**Proof.** Polynomial regularity and localization are AG-CA-14, Proposition 3.3 and Theorem 3.2. Thus $P_{\mathfrak q}$ is regular local. Its completion $H=\widehat{P_{\mathfrak q}}$ is Noetherian regular local by AG-CA-19, Theorem 4.1. Each displayed ring is a localization of $H$, so is Noetherian and regular. If the indicated field has characteristic zero, its only finite purely inseparable extension is itself, and [F.50](#algebra-lemma-geometrically-regular) proves geometric regularity.

Suppose the characteristic is $p>0$. In this case $A_0\cong k[[X_1,\ldots,X_n]]$, with no assumption that $k$ is perfect. To check this specialization, AG-CA-19S, Theorem 6.1 evaluates the variables at a minimal list of generators of the maximal ideal of $A_0$, giving a surjection from $k[[X_1,\ldots,X_n]]$. Regularity makes $n=\dim A_0$. The source is regular local of dimension $n$, by the polynomial completion calculation and AG-CA-19, Theorem 4.1. If the kernel contained a nonzero element, the one-equation dimension theorem AG-CA-11, Theorem 3.2 would make the quotient dimension at most $n-1$, a contradiction. The evaluation kernel is therefore zero.

Treat the two assertions together by taking $Q=A_0$, $F=\operatorname{Frac}(A_0)$ in the first case, and $Q=P$, $F=\operatorname{Frac}(P)$ in the second. We prove that $H\otimes_Q L$ is regular for every finite purely inseparable extension $L/F$, by induction on its degree. The base case is the localization already proved regular. Such an extension has a tower of degree-$p$ steps: take finite field generators, with successive $p$-powers in $F$, and adjoin their roots one at a time; at a nontrivial step the proper-factor argument in [F.119](#more-algebra-lemma-p-basis) gives degree $p$. Thus at the final step write $F\subset M\subset L=M(z)$, $z^p=f\in M\setminus M^p$, and assume $E=H\otimes_QM$ regular.

There is a finite domain $B$, $Q\subset B\subset M$, with fraction field $M$ and, after rescaling $z$, with $f\in B$. Here are the denominator details. Choose finitely many algebraic generators $u_i$ of $M/F$. For a monic equation $u_i^{d_i}+\sum_{j<d_i}c_{ij}u_i^j=0$, multiplication by a suitable nonzero $a_i\in Q$ makes every $a_i^{d_i-j}c_{ij}$ lie in $Q$. Hence $a_iu_i$ is integral over $Q$. The algebra generated by these elements is finite by bounded monic reductions, and its fraction field is $M$. Write $f=b/d$ in that algebra. A monic integral equation for $d\ne0$ can be shortened, by cancelling powers of $d$ in this domain, until its constant coefficient $a\in Q$ is nonzero. The equation expresses $a/d$ in $B$. Replace $z$ by $az$. Its new $p$th power is $a^pf=b a^{p-1}(a/d)\in B$, and remains outside $M^p$, since $a^p$ is a nonzero $p$th power. Relabel this generator and its power as $z,f$. The monic irreducible equation makes $C=B[Z]/(Z^p-f)$ a finite domain with fraction field $L$; injectivity in $L$ follows from the degree-$p$ minimal polynomial.

The base $Q$ is a normal domain. In the first case this is regular local normality; in the second it is polynomial regularity followed by AG-CA-15, Corollary 4.5. Every element of $B$ or $C$ has some $p$-power in $F$, since its fraction field is finite purely inseparable over $F$. That power is integral over $Q$, because the element is integral. Normality therefore puts the power in $Q$.

Set $T=B[Y_1,\ldots,Y_m]$ in the first case, and $T=B$ in the second. Then $P\subset T$ is finite, and every element of $T$ has a sufficiently high $p$-power in $P$. For a polynomial in the first case, take a common exponent for its finitely many coefficients and apply Frobenius to the sum. Lying over gives a prime $\mathfrak r$ above $\mathfrak q$, and it is unique: for $t^{p^e}\in P$, membership of $t$ in a prime above $\mathfrak q$ is equivalent to membership of $t^{p^e}$ in $\mathfrak q$. The full finite-completion product theorem [F.27](#algebra-lemma-completion-finite-extension) thus has one factor and gives
$$H\otimes_PT\cong\widehat{T_{\mathfrak r}}.$$
Tensoring with $M=\operatorname{Frac}(B)$ over $B$, and using $P\otimes_{A_0}B=T$ in the first case, gives the actual identity
$$E=H\otimes_QM\cong\widehat{T_{\mathfrak r}}\otimes_BM.$$
In particular $E$ is a localization of a Noetherian completed local ring. These are the maximal-ideal completions specified in F.27, not a replacement by an unrelated topology.

The domain $B$ is finite type over the complete local ring $A_0$, in either case. Since $f\notin M^p$, [F.105](#more-algebra-lemma-find-D) produces a derivation $D:B\to B$ with $D(f)\ne0$. Extend it coefficientwise to $T$ in the first case, assigning zero to the $Y_i$; coefficient convolution proves the product rule. In the second case it is already a derivation of $T$. By [F.104](#more-algebra-lemma-derivation-extends) it extends successively to $T_{\mathfrak r}$, its maximal-adic completion, and the localization by $B\setminus\{0\}$. The resulting derivation of $E$ sends $f$ to the original nonzero element $D(f)\in M$. This is a unit in every nonzero $M$-algebra $E$; if $E=0$, the next test ring is also zero and already regular.

Finally tensor associativity and $L=M[Z]/(Z^p-f)$ give
$$H\otimes_QL\cong E\otimes_ML\cong E[Z]/(Z^p-f).$$
The polynomial quotient identity follows by reducing each polynomial to its degree-less-than-$p$ remainder, or directly from its finite monic presentation. [F.103](#more-algebra-lemma-degree-p-extension-regular) applies: $E$ is Noetherian regular and its derivation has unit value on $f$. It proves this next ring regular. The induction covers every finite purely inseparable extension. Criterion F.50 now gives both assertions. Empty lists of $X_i$ or $Y_i$ are included throughout. ∎

<a id="more-algebra-lemma-helper-integral"></a>

#### Lemma F.111: helper integral

Reading source: [Stacks, Tag 09XG](https://stacks.math.columbia.edu/tag/09XG).

Let \(A\to B\) be an integral ring map, \(I\subset A\) an ideal, and \(y\in B\) have idempotent image in \(B/IB\). There are an integer \(d\geq1\) and a monic polynomial \(f(T)\in A[T]\) such that
\[
f(y)=0,\qquad f(T)\bmod I=T^d(T-1)^d.
\]

**Proof.** Write \(z=y^2-y=\sum_{i=1}^h a_ib_i\) with \(a_i\in I\) and \(b_i\in B\). This is a finite sum by the definition of the extended ideal. The subalgebra \(C=A[y,b_1,\ldots,b_h]\subset B\) is a finite \(A\)-module: each of its finitely many generators satisfies a monic equation over \(A\), and successive substitution reduces every monomial to one whose exponent in each generator is below that equation's degree. Those finitely many bounded monomials generate \(C\). This argument uses the image of \(A\); injectivity of \(A\to B\) is unnecessary.

Choose a finite module generating list \(c_1,\ldots,c_d\) for \(C\), including \(1\), so \(d\geq1\). Since \(zC\subset IC\), express each \(zc_i\) as \(\sum_j m_{ij}c_j\) with all \(m_{ij}\in I\). For the column \(c=(c_i)\) these equations say \((z1_d-M)c=0\), where \(M=(m_{ij})\). Multiplying by the adjugate, whose identity was proved completely in [F.19](#algebra-lemma-charpoly), gives
\[
g(z)c_i=0\quad\hbox{for all }i,
\qquad g(U)=\det(U1_d-M)\in A[U].
\]
The included generator \(1\) makes \(g(z)=0\) in \(C\), hence in \(B\). The determinant expansion makes \(g\) monic of degree \(d\); reducing the entries of \(M\) modulo \(I\) gives \(g(U)\bmod I=U^d\). Set \(f(T)=g(T^2-T)\). Its leading coefficient is \(1\), it annihilates \(y\), and its reduction is \((T^2-T)^d=T^d(T-1)^d\). The same construction permits an empty sum for \(z\), the zero target algebra, and \(I=A\). ∎

<a id="more-algebra-lemma-intersection-subfields"></a>

#### Lemma F.112: intersection subfields

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 12067–12128](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L12067-L12128).

Let $K$ have characteristic $p>0$. Let $(F_\lambda)$ be a nonempty downward-directed family of subfields of $K$ containing $K^p$, with intersection $K^p$. Then
$$
\bigcap_\lambda\ker\bigl(\Omega_{K/\mathbf F_p}\to\Omega_{K/F_\lambda}\bigr)=0.
$$
For every finite field extension $L/K$, the composita in $L$ also satisfy
$$\bigcap_\lambda L^pF_\lambda=L^p.$$

**Proof.** Take an absolute $p$-basis of $K$ by the entire [F.119](#more-algebra-lemma-p-basis). If a nonzero absolute differential $\omega$ vanished in every indicated relative module, write it in that differential basis using a finite nonempty subset $b_1,\ldots,b_c$ and coefficients not all zero. At every $\lambda$ those relative differentials would be dependent. F.119's full equivalence makes their $p$-monomials dependent over $F_\lambda K^p=F_\lambda$.

Index those finitely many monomials by $e$, $0\le e_i<p$, and form the actual $K$-subspace
$$V=\{(a_e)\in K^{p^c}:\ \sum_e a_e b^e=0\}.$$
Its intersection with $F_\lambda^{p^c}$ is nonzero at every index. The entire newly proved [F.113](#more-algebra-lemma-intersection-subfields-subspace) gives a nonzero intersection with $(K^p)^{p^c}$, contradicting independence of the absolute $p$-basis monomials. Hence no such $\omega$ exists, proving the first assertion.

We prove the second assertion through finite simple steps. Here is the reduction for an arbitrary finite extension. Choose finitely many field generators $\alpha_i$. For each monic irreducible polynomial over $K$, remove a common factor $p$ from its positive exponents repeatedly until writing it as $G_i(T^{p^{e_i}})$ with $G_i'\ne0$. This terminates because its degree decreases. The polynomial $G_i$ is irreducible, since a factorization would give one of the original polynomial, and its nonzero derivative is relatively prime to it. Thus $\beta_i=\alpha_i^{p^{e_i}}$ is separable over $K$.

The field $M=K(\beta_i)$ is finite separable: at each successive adjunction its minimal polynomial divides the original squarefree polynomial over the larger coefficient field, and remains separable. The full separable-tower transitivity proof AG-CA-17, Lemma 7.1 proves that this tower is separable over $K$. From $M$, adjoin each successive $p$th root needed to recover the $\alpha_i$. Each step has degree one or $p$: if the root is absent, the proper-factor coefficient calculation in F.119 proves its degree-$p$ polynomial irreducible. This gives a tower of separable simple steps followed by degree-$p$ purely inseparable steps.

If the desired intersection identity has been proved up to an intermediate field $M$, the fields $E_\lambda=M^pF_\lambda\subset M$ are downward directed, contain $M^p$, and have intersection $M^p$. For the next field $N$, one has $N^pE_\lambda=N^pF_\lambda$, since $M^p\subset N^p$. Thus the same statement for that next simple step proves it for the composite. It remains to prove the two types of simple steps.

For a separable simple extension $L=K(\alpha)$, put $\theta=\alpha^p$. The minimal polynomial over $K(\alpha^p)$ divides both the original squarefree polynomial and $T^p-\alpha^p=(T-\alpha)^p$. It must therefore have degree one, so $K(\theta)=L$ and $\theta\in L^p$. Write $d=[L:K]$. Frobenius transports the $K$-basis $1,\alpha,\ldots,\alpha^{d-1}$ to the $K^p$-basis $1,\theta,\ldots,\theta^{d-1}$ of $L^p$: raising expansions to the $p$th power proves spanning, and unique roots of coefficients prove independence. The same powers are a $K$-basis of $L$, because $K(\theta)=L$.

Consequently they are independent over every $F_\lambda\subset K$. Their monic relation over $K^p$ gives spanning over $F_\lambda$, so the algebra $F_\lambda[\theta]$ is a finite-dimensional domain and therefore a field, by multiplication and inversion. It is exactly $L^pF_\lambda$, with the displayed basis. An element in every compositum has a unique expansion in the $K$-basis of $L$; its coefficients must belong to every $F_\lambda$, hence to $K^p$. It therefore lies in $L^p$, proving the identity for this step.

For a nontrivial degree-$p$ purely inseparable step, write $L=K(\theta)$ with $\theta^p=t\in K\setminus K^p$. Frobenius of its power basis gives
$$L^p=K^p(t),\qquad 1,t,\ldots,t^{p-1}\ \text{a }K^p\text{-basis}.$$
Choose $\lambda_0$ with $t\notin F_{\lambda_0}$, possible from the intersection assumption. Restrict to members contained in $F_{\lambda_0}$. This family is cofinal under refinement: downward directedness refines any given member together with $\lambda_0$. Its intersection is still $K^p$, by the same refinement argument in F.113, and taking the intersection of the composita over it does not change the full intersection.

For every such member, $t^p\in K^p\subset F_\lambda$ while $t\notin F_\lambda$. The proper-factor calculation gives degree $p$, so $L^pF_\lambda=F_\lambda(t)$ has basis $1,t,\ldots,t^{p-1}$. Use the unique expansion over the fixed coarse field $F_{\lambda_0}$; every refined-field expansion must have those same coefficients. They belong to all refined fields and hence to $K^p$. The element is therefore in $K^p(t)=L^p$. The reverse inclusion is automatic. This cofinal argument includes indices where $t$ was initially already in the field, without presuming a degree-$p$ basis there.

Both step types are proved. Applying the tower reduction establishes the identity for every finite extension, including the trivial one. Both assertions and all directed-family hypotheses have now been checked. ∎

<a id="more-algebra-lemma-intersection-subfields-subspace"></a>

#### Lemma F.113: intersection subfields subspace

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 12027–12065](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L12027-L12065).

Let $(F_\lambda)$ be a nonempty downward-directed family of subfields of a field $K$, and put $F=\bigcap_\lambda F_\lambda$. For every $K$-linear subspace $V\subset K^n$,
$$
V\cap F^n\ne0
\quad\Longleftrightarrow\quad
V\cap F_\lambda^n\ne0\ \text{for every }\lambda.
$$

**Proof.** A nonzero vector in the intersection over $F$ belongs to every larger field's intersection. For the other implication induct on $n$. At $n=0$ both nonzero-intersection assertions are false, since the family is nonempty. At $n=1$, a $K$-subspace of $K$ is zero or all of $K$; the hypothesis excludes zero, and the vector one lies in $F$.

For $n>1$, let $V_0$ be the subspace of vectors of $V$ with first coordinate zero, viewed in $K^{n-1}$. If $V_0\cap F^{n-1}$ is nonzero, adjoining the zero first coordinate finishes the proof. Otherwise the induction hypothesis gives an index $\lambda_0$ with $V_0\cap F_{\lambda_0}^{n-1}=0$. Choose a nonzero vector of $V\cap F_{\lambda_0}^n$. Its first coordinate cannot vanish; divide by it to get a vector $v$ with first coordinate one.

For any other vector $w$ in this intersection, subtract $w_1v$. The difference is in $V_0\cap F_{\lambda_0}^{n-1}$ and hence zero. Thus its normalized vector is uniquely $v$. In particular, for every member $F_\mu\subset F_{\lambda_0}$, the hypothesized nonzero intersection contains a vector whose first coordinate is nonzero, and normalization gives this same $v$. All coordinates of $v$ consequently belong to the intersection of these refined fields.

That intersection is $F$. One inclusion follows because $F$ lies in every member. For the other, given any index $\lambda$, downward directedness supplies a member contained in both $F_{\lambda_0}$ and $F_\lambda$; membership in every refinement then implies membership in $F_\lambda$. Thus $v\in F^n$, and it is nonzero because its first coordinate is one. This proves the induction and the full equivalence. ∎

<a id="more-algebra-lemma-lci-local"></a>

#### Lemma F.114: lci local

Reading source: [Stacks, Tag 07D1](https://stacks.math.columbia.edu/tag/07D1).

Let $R$ be Noetherian and let $S$ be a finitely presented $R$-algebra. A kernel of a finite polynomial presentation of $S$ is a regular ideal if and only if this property holds for polynomial presentations on a finite principal cover of $\operatorname{Spec}S$. The condition does not depend on the chosen presentations.

**Proof.** The arbitrary-ring comparison [F.94.A](#more-algebra-lemma-lci-presentation-independent) proves presentation independence for Koszul-regular kernels. The finite polynomial rings and their localizations are Noetherian by AG-CA-03, Theorem 2.1; its Theorem 1.1 and Proposition 1.2 make their finite-module submodules finite. In these rings, [F.118](#more-algebra-lemma-noetherian-finite-all-equivalent) converts a Koszul-regular generating list in a local maximal ideal into a regular list. To obtain the neighbourhood condition in [F.95](#more-algebra-definition-regular-ideal), we will explicitly spread the successive injections, rather than infer global regularity merely from Koszul acyclicity.

Fix $P=R[X_1,\ldots,X_n]\twoheadrightarrow S$ with kernel $I$, and a prime $\mathfrak q\supset I$ of $P$. Suppose a chart $S_g$ containing its image has a regular presentation. Choose $u\in P$ lifting $g$, so $u\notin\mathfrak q$. A presentation of that chart is
$$
Q=P[Z]\twoheadrightarrow S_g,\qquad H=(I,t),\quad t=uZ-1.
$$
The prime $\mathfrak q'$ of $Q$ given by $\mathfrak q$ and $Z=1/u$ satisfies
$$
Q_{\mathfrak q'}/(t)=P_{\mathfrak q}.
$$
Indeed quotienting first gives $P_u$, and then localization at the prime over $\mathfrak q$ gives $P_{\mathfrak q}$. Presentation comparison and F.118 give a regular generating list for $H_{\mathfrak q'}$. Its conormal classes are a basis by [F.74](#algebra-lemma-regular-quasi-regular). Meanwhile [F.72](#algebra-lemma-principal-localization-NL) gives, at this point,
$$
(H/H^2)_{\mathfrak q'}
\cong (I/I^2)_{\mathfrak q}\oplus S_{\mathfrak q/I}\,t.
$$
The first summand is a finite direct summand of a finite free module. It is flat and finitely presented, hence free over the local quotient by [S01, Lemma 1.2](AG-RG-S01.md). Choose $f_1,\ldots,f_c\in I$ whose classes are a basis there; denominators may be cleared since their values outside $\mathfrak q$ are units. The list $t,f_1,\ldots,f_c$ is a conormal basis. Nakayama applied to $H_{\mathfrak q'}/(t,f_1,\ldots,f_c)$ makes it a generator list for $H_{\mathfrak q'}$.

Compare it with the regular generator list just obtained. Both have the same length, equal to the conormal rank. Express the new list in the old one. Modulo the maximal ideal the coefficient matrix takes one basis of the conormal fibre to the other, so its determinant is a unit in $Q_{\mathfrak q'}$. Its exterior powers identify the Koszul complexes: the differential on a wedge deletes one entry with its alternating sign, and this formula commutes with the change of basis. Thus $t,f_1,\ldots,f_c$ has zero first homology. F.118 makes this very order regular, with $t$ first. Quotienting by $t$ proves that $f_1,\ldots,f_c$ is a regular list generating $I_{\mathfrak q}$.

Here is the required principal neighbourhood. The module $I/(f_1,\ldots,f_c)$ is finite and vanishes at $\mathfrak q$. For each $i$, the kernel of multiplication by $f_i$ on $P/(f_1,\ldots,f_{i-1})$ is also finite, because $P$ is Noetherian; it vanishes at $\mathfrak q$ by the just-proved regularity. Exact localization and the finite-generator fraction-zero argument [S01, Lemma 1.1](AG-RG-S01.md) give one element $h\notin\mathfrak q$ annihilating all these finitely many modules. In $P_h$ the list therefore generates $I_h$ and every successive multiplication is injective. Its final quotient is nonzero because the prime $\mathfrak qP_h$ still contains $I_h$. The list is regular on this actual neighbourhood, as required by F.95.

The argument applies at every point lying in one of the stipulated charts, hence at every prime above $I$. Conversely, localization preserves the successive injections of a regular list. For a chart where a given neighbourhood also inverts $u$, present the localization by adjoining $Z$ and put $uZ-1$ first. Multiplication by this polynomial is injective by its lowest-coefficient calculation, and its quotient is $P_u$; the remaining localized list is regular wherever the quotient is nonzero. Charts with zero quotient have no primes to check. Thus the kernel condition restricts to every principal chart. The local neighbourhoods cover the target, and a finite subcover exists by the finite unit-ideal calculation AG-CA-01, Proposition 2.3. Applying the same comparison to a second initial presentation proves the claimed independence. If $S=0$, all these prime conditions are vacuous, including the empty-cover case.
∎

<a id="more-algebra-lemma-lift-factorization-monic"></a>

#### Lemma F.115: lift factorization monic

Reading source: [Stacks, Tag 0ALH](https://stacks.math.columbia.edu/tag/0ALH).

Let $I\subset A$ be any ideal. Suppose the reduction of a monic $f\in A[T]$ has a factorization $\bar f=\bar G\bar H$ into coprime monic polynomials over $A/I$. There is a finitely presented étale map $A\to A'$ such that its canonical map $A/I\to A'/IA'$ is an isomorphism and $f=G'H'$ in $A'[T]$, with monic factors reducing to the prescribed ones.

**Proof.** If $I=A$, take $A'=0$, the principal localization at zero; its closed fibre and the prescribed factors are zero, so all requirements hold. Assume $A/I\ne0$. Put $d=\deg\bar G$ and $e=\deg\bar H$. Introduce $d+e$ variables for the lower coefficients of monic polynomials $G$ and $H$ of those degrees. The $d+e$ lower coefficients of $GH-f$ are equations in these variables. Write $C_0$ for their quotient algebra and $\Delta$ for the determinant of their square Jacobian matrix.

Over $D=A/I$, the derivative of multiplication at the given factors is
$$
D[T]_{<d}\oplus D[T]_{<e}\longrightarrow D[T]_{<d+e},
\qquad (v,w)\longmapsto\bar H v+\bar G w.
$$
Here $D[T]_{<r}$ is the free module on $1,T,\ldots,T^{r-1}$. Monic division works over this arbitrary ring: for a monic polynomial $p$ of degree $r$, subtract the current leading coefficient times $T^k p$ until the remainder has degree below $r$. For a nonzero polynomial $q$, the product $qp$ has degree $\deg q+r$, with the same nonzero leading coefficient as $q$. Hence no nonzero multiple of $p$ has degree below $r$, and the quotient and remainder are unique. For $r=0$, the monic polynomial is $1$ and the remainder is zero. Choose a Bezout identity $a\bar G+b\bar H=1$. For a polynomial $q$ in the right module, let $v$ be the remainder of $bq$ on monic division by $\bar G$. Then $q-\bar H v$ is divisible by $\bar G$; its quotient $w$ has degree below $e$. This constructs a preimage of $q$. If the image of $(v,w)$ is zero, reduction modulo $\bar G$ and invertibility of $\bar H$ there give $v=0$, by its degree bound, and monic multiplication then gives $w=0$. Thus this is an isomorphism even when $D$ has zero divisors. Degree-zero factors are covered by empty polynomial modules.

Consequently $\Delta$ has a unit value at the prescribed coefficient tuple. Set $C=(C_0)_\Delta$. The square Jacobian calculation AG-CA-17, Theorem 4.1 gives formal smoothness, and there are no remaining differential coordinates. Theorem 2.2 of that lesson therefore gives formal unramifiedness. The finite equations and principal localization give finite presentation, so $C/A$ is étale. The coefficient tuple defines a $D$-algebra retraction $\sigma:E=C/IC\to D$ of its structural map.

We select exactly this section in the closed fibre. Let $L=\ker\sigma$. Finite algebra generators $x_i$ of $E/D$ give finite ideal generators $x_i-\sigma(x_i)$ for $L$: replace each variable by its constant value in a polynomial and telescope the difference one variable at a time. The map
$$
\delta:E\longrightarrow L/L^2,\qquad
x\longmapsto x-\sigma(x)\pmod {L^2}
$$
is a $D$-derivation, with $E$ acting on $L/L^2$ through $\sigma$. To check products, expand $x=\sigma(x)+\ell$ and $y=\sigma(y)+m$ and discard $\ell m\in L^2$. Since $E/D$ is étale by base change, its differentials vanish by the same Theorem 2.2. The universal differential property makes $\delta=0$. Its restriction to $L$ is the quotient map, so $L=L^2$.

Choose finite ideal generators $\ell_i$ and write $\ell_i=\sum_j m_{ij}\ell_j$ with $m_{ij}\in L$. The adjugate identity of [S01, Lemma 1.2](AG-RG-S01.md) shows that $a=\det(1-M)$ annihilates $L$, while $a\equiv1\pmod L$. Put $p=1-a\in L$. Then $p\ell=\ell$ for every $\ell\in L$, so $p^2=p$ and $L=pE$. Inverting $1-p$ kills precisely $L$ and induces $E_{1-p}\cong E/L=D$, compatibly with its structural map. Lift $1-p$ to $h\in C$ and put $A'=C_h$. Its closed fibre is this very copy of $D$, and principal localization preserves finite presentation and étaleness by AG-CA-17, Theorem 1.2 and Section 4. The universal polynomials in $A'[T]$ supply $G',H'$. If both degrees are zero, one can directly take $A'=A$ and both factors equal to one.
∎

<a id="more-algebra-lemma-lift-idempotent-upstairs"></a>

#### Lemma F.116: lift idempotent upstairs

Reading source: [Stacks, Tag 07M4](https://stacks.math.columbia.edu/tag/07M4).

Suppose $A\to B$ is integral and $I\subset A$ is an ideal. Every idempotent $\bar e\in B/IB$ lifts to an idempotent of $B\otimes_A A'$ after a finitely presented étale map $A\to A'$ for which $A/I\to A'/IA'$ is an isomorphism.

**Proof.** Choose $y\in B$ reducing to $\bar e$. The determinant proof [F.111](#more-algebra-lemma-helper-integral) gives an integer $d\ge1$ and a monic $f\in A[T]$ with
$$
f(y)=0,\qquad \bar f=T^d(T-1)^d.
$$
The two factors generate the unit ideal: in the expansion of $(T+(1-T))^{2d-1}=1$, every term contains either $T^d$ or $(1-T)^d$. Apply [F.115](#more-algebra-lemma-lift-factorization-monic). Over its étale algebra $A_1$ we have $f=GH$ with reductions $T^d$ and $(T-1)^d$. Put $B_1=B\otimes_AA_1$, write $y_1$ for the image of $y$, and set $b_1=G(y_1)$, $b_2=H(y_1)$. Then
$$
b_1b_2=0,\qquad
\bar b_1=\bar e,\quad \bar b_2=(-1)^d(1-\bar e).
$$
Thus $b_1,b_2$ generate the unit ideal modulo $IB_1$.

The map $A_1\to B_1$ remains integral. Indeed each tensor element uses finitely many elements of $B$; their monic equations generate a finite module algebra after base change, and its elements are integral by the determinant test AG-CA-05, Theorems 1.1–1.2. Let $K$ be the inverse image in $A_1$ of the ideal $(b_1,b_2)B_1$. The closed-image and lying-over proof in Theorem 3.4 of that lesson gives
$$
\operatorname{image}V_{B_1}(b_1,b_2)=V_{A_1}(K).
$$
No prime in this image can contain $IA_1$, since its prime upstairs would contain $IB_1$ as well as $b_1,b_2$. Hence $V(K+IA_1)$ is empty and $K+IA_1=A_1$, by the prime-separation proof AG-CA-01, Lemma 1.1. Choose $a\in K$ with $a\equiv1\pmod {IA_1}$ and set $A'=(A_1)_a$.

In $B'=B_1\otimes_{A_1}A'$, the image of $a$ is a unit belonging to $(b_1,b_2)$. Choose $u,v\in B'$ with $ub_1+vb_2=1$ and put $e'=ub_1$. The equations give
$$
e'(1-e')=uvb_1b_2=0,
$$
so $e'$ is idempotent. Reducing $ub_1+vb_2=1$ and multiplying by $\bar e$ gives $\bar u\bar e=\bar e$, proving that $e'$ reduces to the specified idempotent. Finally $a$ reduces to one, so the last localization leaves the quotient $A_1/IA_1=A/I$ unchanged. Its composition with $A\to A_1$ is finitely presented étale by the proved stability in AG-CA-17, Theorem 1.2 and Section 4. This supplies every stated property, including the zero closed fibre.
∎

<a id="more-algebra-lemma-lift-projective-module"></a>

#### Lemma F.117: lift projective module

Reading source: [Stacks, Tag 07M5](https://stacks.math.columbia.edu/tag/07M5).

For an ideal $I$ of any ring $A$ and a finite projective $A/I$-module $\bar P$, there is a finitely presented étale map $A\to A'$ inducing $A/I\cong A'/IA'$, and a finite projective $A'$-module $P'$ with $P'/IP'\cong\bar P$ under that identification.

**Proof.** Realize $\bar P$ as a direct summand of $(A/I)^n$ and let $\bar p$ be its projector. Such a realization follows from projectivity by splitting a finite free surjection, as in [S01, Lemma 1.0](AG-RG-S01.md). Lift the finitely many entries of $\bar p$ to a matrix $\varphi$ over $A$. Its characteristic polynomial $f(T)=\det(T1-\varphi)$ is monic. The full coefficient proof of Cayley–Hamilton [F.19](#algebra-lemma-charpoly) gives an algebra map
$$
B=A[T]/(f)\longrightarrow\operatorname{End}_A(A^n),
\qquad x\longmapsto\varphi,
$$
where $x$ is the class of $T$. For $n>0$, subtracting the leading coefficient times the appropriate power of $T$ times the monic polynomial $f$ reduces any polynomial to degree below $n$. Conversely, for nonzero $q$, the leading coefficient of $qf$ equals that of $q$ and its degree is $\deg q+n$; thus no nonzero multiple of $f$ has degree below $n$. These two calculations show that $1,x,\ldots,x^{n-1}$ are a free $A$-basis of $B$, even when $A$ has zero divisors. The proved finite-algebra determinant criterion AG-CA-05, Theorem 1.2 now makes $A\to B$ integral. The case $n=0$ is handled directly below.

In each residue field of $A/I$, an idempotent linear operator decomposes the vector space into its image and kernel: $v=\bar p v+(1-\bar p)v$, and applying $\bar p$ proves the intersection zero. Choose bases of the two summands. Its characteristic polynomial there is $T^{n-r}(T-1)^r$ for the dimension $r$ of its image. Consequently at every prime of $B/IB$ the image of $x$ is zero or one: pass to the field of that prime and use this factorization. The nilradical calculation AG-CA-01, Theorem 1.2 then gives an integer $N\ge1$ such that
$$
x^N(1-x)^N=0\quad\text{in }E=B/IB.
$$
This uses a single nilpotent element, with no Noetherian condition.

Set $a=x^N$, $b=(1-x)^N$ in $E$. They generate the unit ideal: expand $(x+(1-x))^{2N-1}$, whose every term is divisible by $a$ or $b$. Also $ab=0$. Choose $u,v$ with $ua+vb=1$. Then $(a+b)(u^2a+v^2b)=u^2a^2+v^2b^2=(ua+vb)^2=1$. Thus $a+b$ is a unit, and
$$
\epsilon=\frac{a}{a+b},\qquad
\epsilon(1-\epsilon)=\frac{ab}{(a+b)^2}=0
$$
is an idempotent. Under the reduction of the displayed endomorphism map, $a$ goes to $\bar p^N=\bar p$, $b$ to $(1-\bar p)^N=1-\bar p$, and their sum to the identity. Hence $\epsilon$ maps to exactly $\bar p$.

Apply [F.116](#more-algebra-lemma-lift-idempotent-upstairs) to the integral algebra $B/A$ and this idempotent of $B/IB$. It supplies the required étale $A'$ and an idempotent of $B\otimes_AA'$ lifting $\epsilon$. Its image in $\operatorname{End}_{A'}((A')^n)$ is a projector $p'$ reducing to $\bar p$. Put $P'=\operatorname{im}p'$. The decomposition
$$
(A')^n=\operatorname{im}p'\oplus\operatorname{im}(1-p')
$$
follows by writing each vector as the sum of its two projections; applying $p'$ makes their intersection zero. The projections of the finite coordinate basis generate each summand, so $P'$ is finite projective. Reduction preserves this split decomposition and identifies its first summand with $\operatorname{im}\bar p=\bar P$. If $n=0$, take $A'=A$ and $P'=0$ directly. This also handles $A/I=0$ by choosing its zero module with $n=0$.
∎

<a id="more-algebra-lemma-noetherian-finite-all-equivalent"></a>

#### Lemma F.118: noetherian finite all equivalent

Reading source: [Stacks, Tag 09CC](https://stacks.math.columbia.edu/tag/09CC), together with the regular-sequence and Koszul arguments cited there. The proof below is independently written for finite modules.

For a nonzero finite module over a Noetherian local ring and a list in its maximal ideal, regularity, vanishing of all positive Koszul homology, vanishing of first Koszul homology, and the polynomial associated-graded condition are equivalent.

**Proof.**
Write $(A,\mathfrak m)$ for the ring, $M$ for the module, and $J=(f_1,\ldots,f_r)$. The fourth assertion means that the natural graded map
$$\theta:(M/JM)[T_1,\ldots,T_r]\longrightarrow\bigoplus_{n\geq0}J^nM/J^{n+1}M,\qquad \bar mT^a\longmapsto[mf^a],$$
is an isomorphism. It is always surjective. If $r=0$, the Koszul complex has only $M$ in degree zero, $J=0$, and $\theta$ is the identity in degree zero. The empty list is regular because $M\ne0$. Thus all four assertions hold in that case; assume $r>0$.

Use the exterior complex on the symbols $e_1,\ldots,e_r$, with coefficients in $M$, differential $d(e_i)=f_i$, and the signed product rule. Separating wedges which contain $e_r$ identifies it with the cone of multiplication by $f_r$ on the complex for the first $r-1$ entries. Its homology sequence contains
$$H_1(K_{r-1})\xrightarrow{f_r}H_1(K_{r-1})\longrightarrow H_1(K_r)\longrightarrow H_0(K_{r-1})\xrightarrow{f_r}H_0(K_{r-1}).$$
For the two consequences needed here, exactness can also be checked directly. A degree-one cycle of $K_{r-1}$ becomes a boundary in $K_r$ when $H_1(K_r)=0$. Writing that boundary as the sum of a wedge without $e_r$ and a wedge containing $e_r$ shows that its class in $H_1(K_{r-1})$ is $f_r$ times a class represented by a cycle. This gives surjectivity of the first arrow. If $f_rm\in(f_1,\ldots,f_{r-1})M$, choose coefficients for this equality to obtain a degree-one cycle in $K_r$ with last coefficient $m$. A degree-two boundary has last coefficient in $(f_1,\ldots,f_{r-1})M$, so $[m]=0$ in $H_0(K_{r-1})$. This gives injectivity of the last arrow.

If $H_1(K_r)=0$, the preceding $H_1$ is a finite $A$-module, since its complex consists of finite modules over a Noetherian ring. Nakayama, with $f_r\in\mathfrak m$, makes it zero by the surjectivity just proved. Induction therefore gives all successive multiplication injections, including the final one displayed above. Their last quotient is nonzero by Nakayama applied to $M/JM$. This proves regularity. Conversely, assume the list regular and the preceding complex acyclic in positive degrees. A cycle in $K_r$ of degree $k$ has a component $v$ multiplying $e_r$, and $v$ is a cycle of degree $k-1$ in $K_{r-1}$. For $k\geq2$, preceding acyclicity makes $v$ a boundary. For $k=1$, the cycle identity says $f_r[v]=0$ in $H_0(K_{r-1})$; regularity again makes $v$ a boundary. Subtract the differential of a suitable wedge containing $e_r$ to remove $v$. What remains is a degree-$k$ cycle in $K_{r-1}$ and is a boundary by preceding acyclicity. This proves acyclicity in every positive degree by induction. In particular it implies vanishing of $H_1$.

We next prove that a regular list makes $\theta$ injective. In degree zero this is the defining quotient $M/JM$. In degree one, suppose $\sum_i f_im_i\in J^2M$. Express this element as $\sum_i f_iu_i$ with $u_i\in JM$, and subtract. The vector $(m_i-u_i)$ is a degree-one Koszul cycle. By the preceding acyclicity it is a boundary, whose coefficients all belong to $JM$, since the degree-two differential has coefficients $f_i$. Consequently every $m_i\in JM$. This proves directly the module version of the conormal calculation in [F.74](#algebra-lemma-regular-quasi-regular).

Here is a coefficient calculation for any degree $n\geq1$. In a relation
$$\sum_{|a|=n}m_af^a\in J^{n+1}M,$$
collect every term involving one of $f_1,\ldots,f_{r-1}$ into their generated submodule. The only remaining term on the left is $m_{(0,\ldots,0,n)}f_r^n$; the only remaining type on the right is $u f_r^{n+1}$. Thus
$$\bigl(m_{(0,\ldots,0,n)}-uf_r\bigr)f_r^n+\sum_{i<r}f_iv_i=0$$
for suitable $u,v_i\in M$. The list $f_1,\ldots,f_{r-1},f_r^n$ is regular by AG-CA-12, Proposition 1.3, whose power argument applies to modules. Its first Koszul homology is zero by the cone argument. Hence the last coefficient of this relation belongs to $(f_1,\ldots,f_{r-1})M$, so $m_{(0,\ldots,0,n)}\in JM$.

To recover the coefficients of all monomials, put $B=A[U_1,\ldots,U_r,U_r^{-1}]$, $N=M\otimes_AB$, and
$$g_i=f_i-(U_i/U_r)f_r\quad(i<r),\qquad g_r=f_r/U_r.$$
The ring $B$ is free and faithfully flat over $A$, with its Laurent monomials as a basis. Tensoring preserves Koszul acyclicity. The displayed change of generators is invertible, so its exterior powers identify the two Koszul complexes and give $H_1(K(g;N))=0$.

Fix a prime $\mathfrak p$ of $B$. If $N_{\mathfrak p}=0$, every term of every Koszul complex with these coefficients is zero. If $N_{\mathfrak p}\ne0$ and $JB\subset\mathfrak p$, the local criterion already proved makes $g_1,\ldots,g_r$ regular on the nonzero finite $B_{\mathfrak p}$-module $N_{\mathfrak p}$. Its power list $g_1,\ldots,g_{r-1},g_r^n$ is regular and has zero $H_1$. Finally, if $JB\not\subset\mathfrak p$, at least one $g_i$ is a unit in $B_{\mathfrak p}$. The power list still contains a unit, so choose $a_i$ with $\sum_{i<r}a_ig_i+a_rg_r^n=1$. Wedge multiplication by $\sum_i a_ie_i$ satisfies $dh+hd=1$ by the signed product rule, and contracts its Koszul complex. These three cases show that the power list has zero first homology at every prime. Localization commutes with the complex and its homology; a module whose localizations at all primes vanish is zero. The global $H_1$ therefore vanishes as well.

The preceding pure-last-coefficient calculation now applies to $g$ on $N$. Substituting $f_i=g_i+U_ig_r$ for $i<r$ and $f_r=U_rg_r$ makes the coefficient of $g_r^n$ equal to $\sum_{|a|=n}m_aU^a$. Thus this element belongs to $JN$. Since $N/JN=(M/JM)\otimes_AB$ is the direct sum of its Laurent monomial copies of $M/JM$, each coefficient $m_a$ belongs to $JM$. This proves injectivity of $\theta$ in every degree.

For the converse, suppose $\theta$ is an isomorphism. Krull intersection, AG-CA-03, Theorem 6.1, gives $\bigcap_{n\geq0}J^nM=0$. Every nonzero $m\in M$ therefore has a finite order $v$, characterized by $m\in J^vM\setminus J^{v+1}M$. Its initial class is nonzero; multiplication by $T_1$ is injective on $(M/JM)[T_1,\ldots,T_r]$, so $f_1m$ is nonzero and has order $v+1$. In particular $f_1$ acts injectively on $M$. The same calculation gives
$$f_1M\cap J^nM=f_1J^{n-1}M\qquad(n\geq1):$$
if $f_1m\in J^nM$ and $m\ne0$, its order forces $m\in J^{n-1}M$; the reverse inclusion follows from $f_1\in J$.

Set $M'=M/f_1M$ and let $J'$ be the ideal induced by $J$. In degree $n\geq1$, the last equality identifies the kernel of $J^nM/J^{n+1}M\to J'^nM'/J'^{n+1}M'$ with multiplication by $T_1$ from degree $n-1$. Indeed an element in that kernel is $y+f_1m$, with $y\in J^{n+1}M$; then $f_1m\in J^nM$, so $m\in J^{n-1}M$. Degree zero is unchanged. It follows that
$$\operatorname{gr}_{J'}M'\simeq(M/JM)[T_2,\ldots,T_r].$$
Repeat the order and quotient argument for the remaining entries. Nakayama ensures that each finite intermediate module and the final quotient are nonzero. This proves regularity and hence all four equivalences.
 ∎

<a id="more-algebra-lemma-p-basis"></a>

#### Lemma F.119: p basis

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 11972–12025](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L11972-L12025).

Let $L/F$ be a field extension of characteristic $p>0$ and put $E=FL^p$. A subset $C\subset L$ is *$p$-independent over $F$* when its monomials, with finite support and exponents between $0$ and $p-1$, are linearly independent over $E$. It is a *$p$-basis* when those monomials are a basis of $L$ over $E$. Independence holds exactly when the differentials $dc$ are linearly independent over $L$ in $\Omega_{L/F}$. Every such subset extends to a $p$-basis. Moreover $C$ is a $p$-basis exactly when its differentials form an $L$-basis of $\Omega_{L/F}$.

**Proof.** All derivations over $F$ annihilate $E$: they kill $F$, the product rule kills $p$th powers, and the inverse rule kills the field generated by these elements. We first construct the coordinate system for a maximal $p$-independent set.

Order the $p$-independent supersets of the prescribed set by inclusion. A chain has an independent union, since any proposed relation involves finitely many elements contained together in one member of the chain. Zorn's lemma gives a maximal set $B$. For each finite $B_0\subset B$, the algebra $E[B_0]$ is spanned by its standard monomials, because $b^p\in E$. It is a finite-dimensional domain and therefore a field: multiplication by any nonzero element is an injective linear endomorphism, hence surjective, and its inverse image of one supplies an inverse. The union $E[B]$ is consequently a field as well.

Suppose $x\in L\setminus E[B]$. Its minimal polynomial over that field divides $T^p-x^p$. In $L[T]$ this polynomial is $(T-x)^p$, and unique Euclidean factorization shows that any monic divisor is $(T-x)^r$. If $0<r<p$ and this divisor were defined over $E[B]$, its next coefficient $-rx$ would put $x$ there, a contradiction. Thus the minimal polynomial has degree $p$. The power basis of this degree-$p$ extension, together with independence of the old monomials, proves that $B\cup\{x\}$ remains $p$-independent. Maximality rules this out, so $E[B]=L$.

There is now an exact presentation
$$
L=E[T_b:b\in B]/(T_b^p-b^p:b\in B).
$$
Surjectivity follows from $E[B]=L$. For injectivity, reduce a polynomial, which involves only finitely many variables, by the displayed monic relations. Its reduced standard-monomial expression can vanish only when every coefficient is zero, by $p$-independence. This proves the presentation for infinite sets too.

Differentiate polynomials in a single variable $T_b$, killing $E$ and all other variables. Each defining relation has derivative zero, so this operation descends through the exact presentation to an $F$-derivation $\partial_b:L\to L$. It sends $b$ to one and every other member of $B$ to zero. These derivations prove that the $db$ are independent. The finite monomial expansion of each element, differentiated by the product rule, proves they span $\Omega_{L/F}$. This establishes the differential-basis assertion for $B$, and shows that every $p$-independent subset has independent differentials.

Conversely, let $dc_1,\ldots,dc_r$ be independent. Each coordinate functional on their span extends to all of $\Omega_{L/F}$. For completeness, order the extensions to larger subspaces by extension; chain unions give compatible upper bounds. A maximal extension must have the whole space as domain, since otherwise one can adjoin a vector outside its domain and assign it value zero. This is another application of Zorn's lemma. The universal differential property turns these extended functionals into $F$-derivations $D_i$ with $D_i(c_j)=\delta_{ij}$, all killing $E$.

If these elements had a nonzero standard-monomial relation over $E$, choose its polynomial $P$ with least total degree. This degree is positive. Some partial derivative of $P$ is nonzero: a nonconstant monomial has a positive exponent strictly below $p$, and distinct monomials containing that variable have distinct differentiated monomials. Applying the corresponding $D_i$ gives the smaller-degree relation $(\partial P/\partial T_i)(c)=0$, a contradiction. Thus the finite set is $p$-independent. Since every relation on any subset is finite, this proves the equivalence in general.

Finally, if the $dc$ form a basis, the equivalence makes $C$ $p$-independent. Extend it to $B$ by the construction above. An additional $b\in B\setminus C$ would have a differential independent of all the $dc$, contradicting their spanning property. Hence $B=C$ and $C$ is a $p$-basis. The converse has already been proved by the presentation. Empty bases and arbitrary infinite transcendence degree are included. ∎

<a id="more-algebra-lemma-power-series-ring-subfields"></a>

#### Lemma F.120: power series ring subfields

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 12130–12171](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L12130-L12171).

Let $k$ have characteristic $p>0$ and let $B$ be a $p$-basis of $k$ over $\mathbf F_p$. Set
$$A=k[[X_1,\ldots,X_n]][Y_1,\ldots,Y_m],\qquad K=\operatorname{Frac}(A).$$
For each finite $J\subset B$, define
$$
k_J=k^p(B\setminus J),\quad
A_J=k_J[[X_1^p,\ldots,X_n^p]][Y_1^p,\ldots,Y_m^p],
\quad K_J=\operatorname{Frac}(A_J).
$$
Then $A$ is finite free over $A_J$. The subfields $K_J$ contain $K^p$, are downward directed, and have intersection $K^p$.

**Proof.** The whole [F.119](#more-algebra-lemma-p-basis) gives the standard monomial basis of $k$ over $k^p$. In particular the subalgebra generated by any subset of $B$ is a field: each element lies in a finite-dimensional domain generated by finitely many of those elements, and multiplication by a nonzero element gives its inverse there. Thus $k_J=k^p[B\setminus J]$.

The $p^{|J|}$ monomials in $J$ form a basis of $k$ over $k_J$. They span by grouping each finite standard-monomial expansion according to its exponents in $J$. For independence, expand any finitely many coefficients from $k_J$ in the monomials of $B\setminus J$. A relation then becomes a relation between distinct monomials in the full $p$-basis, so all coefficients vanish. The same uniqueness shows
$$\bigcap_{J\subset B,\ J\ {\rm finite}}k_J=k^p:$$
if an element's unique finite expansion has a monomial involving $b\in B$, it cannot belong to $k_{\{b\}}$.

The algebra $A$ is a domain. For two nonzero power series, the product of their first nonzero total-degree homogeneous polynomials is nonzero: polynomial domains follow by taking a leading monomial. This product is the first nonzero homogeneous part of their product. Adjoining the polynomial variables preserves the domain property by the same leading-monomial test.

A basis of $A$ as an $A_J$-module is the finite list
$$
\left\{\prod_{b\in J}b^{e_b}\prod_iX_i^{r_i}\prod_jY_j^{s_j}:
0\leq e_b,r_i,s_j<p\right\}.
$$
Indeed expand each coefficient in the finite $k_J$-basis just proved, and group the $X$ and $Y$ exponents by their residues modulo $p$. The grouped coefficients are power series in $X^p$ and polynomials in $Y^p$ over $k_J$. There are finitely many $Y$ terms initially, so these expressions remain polynomials. Coefficient comparison and uniqueness of the field basis prove linear independence. The rank is $p^{|J|+n+m}$, including empty variable lists.

The characteristic-$p$ identity for a series is computed in each finite degree, where only finitely many terms contribute. It gives $a^p\in A_J$ for every $a\in A$, hence $K^p\subset K_J$. Also $k_{J\cup J'}\subset k_J\cap k_{J'}$, so $K_{J\cup J'}\subset K_J\cap K_{J'}$. This proves downward directedness.

It remains to identify the intersection; fractions cannot be compared by their coefficients directly. Write a candidate as $u=f/g^p$ with $f,g\in A$ and $g\ne0$, by multiplying an arbitrary numerator and denominator by the $(p-1)$st power of its denominator. Fix finite $J$ and suppose $u\in K_J$. Writing it as $a/h$ with $a,h\in A_J$, $h\ne0$, gives
$$u=(ah^{p-1})/h^p.$$
Rename this numerator $a$ and put $b=h$. Cross multiplication yields $b^pf=ag^p\in A_J$.

Any $A_J$-derivation $D:A\to A$ consequently gives $b^pD(f)=0$, because the derivatives of $p$th powers vanish. The domain property makes $D(f)=0$. The formal partial derivatives in every $X_i$ and $Y_j$ are such derivations. Their product rules hold coefficient by coefficient, since each convolution coefficient is a finite sum. Distinct monomials containing a given variable have distinct derivative monomials; their scalar exponents are nonzero precisely when not divisible by $p$. Therefore only exponents divisible by $p$ can occur in $f$.

For $b\in J$, the coordinate derivation of $k/k_J$ differentiates its unique $J$-monomial expansion. It kills $k_J$ and exists by the exact presentation in F.119, or by restricting its $b$-coordinate derivation. Its extension to $A$ applies it to each coefficient and kills $X,Y$; the finite convolution formula again proves the product rule. The common kernel of these derivations on $k$ is exactly $k_J$: differentiation of the finite $J$-basis expansion kills precisely the coefficient terms with a positive exponent in an excluded variable. Thus every coefficient of $f$ belongs to $k_J$.

If $u$ belongs to every $K_J$, all these conclusions hold for every finite $J$. Its coefficients then lie in $k^p$ by the field intersection above, and all its variable exponents are multiples of $p$. Choose the unique $p$th root of each coefficient and divide each exponent by $p$; this defines an element $v\in A$ with $v^p=f$. The polynomial variables still have bounded degree. It follows that $u=(v/g)^p\in K^p$. Together with the first inclusion this proves the claimed intersection, even with an infinite coefficient $p$-basis. ∎

<a id="more-algebra-lemma-quasi-regular-ideal-finite-projective"></a>

#### Lemma F.121: quasi regular ideal finite projective

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 8769–8778](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L8769-L8778).

For an arbitrary ring $R$ and quasi-regular ideal $I$, the module $I/I^2$ is finite projective over $R/I$.

**Proof.** Put $S=R/I$ and $M=I/I^2$. If $S=0$, then $I=R$ and $M=0$, so the assertion holds. Otherwise the explicit quasi-regularity definition [F.95](#more-algebra-definition-regular-ideal) gives principal neighbourhoods of all primes of $S$ on which the ideal is generated by a finite quasi-regular list. The degree-one graded isomorphism identifies its conormal module with the free module on that list. Exact localization gives the same identification for $M_g$ over $S_g$.

The chart denominators generate $S$: if their ideal were proper, a maximal ideal containing it would lie outside every chart. A finite list $g_1,\ldots,g_s$ therefore already generates the unit ideal and supplies finite free localizations of $M$. We record the detection argument needed without any finiteness assumption on a module $N$. If $N_{g_i}=0$ for every $i$, each $x\in N$ satisfies $g_i^{e_i}x=0$ for positive integers $e_i$. These powers generate the unit ideal too, since a maximal ideal containing all of them would contain all the $g_i$. Multiply an expression $1=\sum_i a_i g_i^{e_i}$ by $x$ to obtain $x=0$. Hence $N=0$.

For every local basis, represent its finitely many elements by fractions from $M$ and take their numerators. Multiplication by the corresponding powers of the unit $g_i$ still gives a basis locally. The finite submodule generated by all these numerators has quotient zero on every chart; the detection argument makes that quotient zero globally. Thus $M$ is finite. Choose a finite free surjection $S^t\to M$ with kernel $H$.

Localizing on a chart gives a surjection onto a finite free module, so it splits by lifting a basis. The complementary projection of the $t$ standard vectors then generates $H_{g_i}$. Exact localization identifies this kernel with the localization of $H$; clear the finitely many denominators of its displayed generators and collect their numerators from $H$. They generate a finite submodule $H_0$ with $(H/H_0)_{g_i}=0$ everywhere. Detection again gives $H=H_0$, so $M$ is finitely presented.

Every stalk of $M$ is free, because a chart contains that prime. The entire AG-CA-07, Theorem 3.3 gives flatness over $S$. The full proof of AG-CA-07, Theorem 5.3 then splits a finite presentation of this flat module, making it a direct summand of a finite free module. This is finite projectivity. The argument supplies the missing global finite presentation and applies without Noetherianity or finite generation of $I$ in $R$. ∎

<a id="more-algebra-lemma-quotient-regular"></a>

#### Lemma F.122: quotient regular

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 12407–12424](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L12407-L12424).

Let $R$ be a Noetherian regular ring. If a derivation $D:R\to R$ satisfies that $D(f)$ is a unit in $R/(f)$, then $R/(f)$ is regular.

**Proof.** Fix a prime $\mathfrak p$ containing $f$ and set $V=R_{\mathfrak p}$, $\mathfrak m=\mathfrak pV$. We first extend the derivation without a finiteness or continuity assumption. The map
$$r\longmapsto r+\epsilon D(r),\qquad \epsilon^2=0,$$
is a ring homomorphism to $V[\epsilon]/(\epsilon^2)$ by the product rule. For $s\notin\mathfrak p$ its image has the explicit inverse $s^{-1}-\epsilon s^{-2}D(s)$. The universal property of localization extends this map to $V$. Its constant component is the identity, so its $\epsilon$ component is a derivation $D_V:V\to V$ extending $D$, with
$$D_V(a/s)=D(a)/s-aD(s)/s^2.$$
This construction proves well-definedness and the product rule for the fraction formula.

The hypothesis gives $uD(f)+vf=1$ for some $u,v\in R$. At $\mathfrak p$, this makes $D_V(f)$ a unit modulo $\mathfrak m$, and in particular outside $\mathfrak m$. If $f$ belonged to $\mathfrak m^2$, express it as a finite sum $\sum_j a_jb_j$ with $a_j,b_j\in\mathfrak m$. The product rule would give
$$D_V(f)=\sum_j\bigl(a_jD_V(b_j)+b_jD_V(a_j)\bigr)\in\mathfrak m,$$
a contradiction. Thus $f\in\mathfrak m\setminus\mathfrak m^2$.

Regularity of $R$ makes $V$ regular local. The entire AG-CA-14, Corollary 1.2 proves $V/fV$ regular: extend the nonzero class of $f$ to a cotangent basis, lift it, and apply the proved successive parameter-quotient theorem. These quotients are exactly the local rings of $R/(f)$ at its corresponding primes. The quotient is Noetherian, so this proves regularity. If no prime contains $f$, the quotient is zero and has no local rings to test. ∎

<a id="more-algebra-lemma-regular-base-change"></a>

#### Lemma F.123: regular base change

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 11022–11047](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L11022-L11047).

For a regular map $R\to\Lambda$ of Noetherian rings and any finite-type $R$-algebra $R'$, the map
$$R'\longrightarrow T=\Lambda\otimes_RR'$$
is regular.

**Proof.** Both $R'$ and $T$ are Noetherian: a finite algebra-generating list for $R'$ makes it a quotient of a polynomial ring over $R$, and makes $T$ a quotient of the corresponding polynomial ring over $\Lambda$. The entire Hilbert basis theorem AG-CA-03, Theorem 2.1, applies to each. The full tensor proof AG-CA-07, Proposition 3.2 proves flatness of $T$ over $R'$ by base change.

Let $\mathfrak p'$ be any prime of $R'$, with contraction $\mathfrak p$ to $R$. Put $k=\kappa(\mathfrak p)$ and $E=\kappa(\mathfrak p')$. The field inclusion $k\hookrightarrow E$ is induced by the domain inclusion $R/\mathfrak p\hookrightarrow R'/\mathfrak p'$. If $u_1,\ldots,u_n$ are algebra generators, localizing this domain inclusion at $R\setminus\mathfrak p$ gives
$$
(R\setminus\mathfrak p)^{-1}(R'/\mathfrak p')
=k[\bar u_1,\ldots,\bar u_n].
$$
Its fraction field is still $E$, since this intermediate localization does not change the fraction field of the domain. Thus $E=k(\bar u_1,\ldots,\bar u_n)$ is a finitely generated field extension of $k$. This step requires neither algebraicity nor separability.

Set $F=\Lambda\otimes_Rk$. The original regular map gives a Noetherian geometrically regular $k$-algebra $F$. Tensor associativity, with the indicated residue-field maps, gives the actual new fibre
$$T\otimes_{R'}E\cong\Lambda\otimes_RE\cong F\otimes_kE.$$
The entire [F.12](#algebra-lemma-Noetherian-field-extension) makes it Noetherian from the finite field-generating list. Assertion (2) of the complete [F.52](#algebra-lemma-geometrically-regular-over-subfields) makes it geometrically regular over $E$; its required Noetherian tensor hypothesis has just been checked. Every new fibre satisfies the criterion, and the map is flat, so it is regular. Empty spectra require no fibre test. ∎

<a id="more-algebra-lemma-regular-composition"></a>

#### Lemma F.124: regular composition

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 11049–11065](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L11049-L11065).

If $A\to B$ and $B\to C$ are regular maps of Noetherian rings, then $A\to C$ is regular.

**Proof.** The complete flat-composition calculation AG-CA-07, Proposition 3.2, makes the composite flat. Fix $\mathfrak a\in\operatorname{Spec}A$ and write $k_0=\kappa(\mathfrak a)$. Its two relevant fibres are Noetherian:
$$
B\otimes_Ak_0=(A\setminus\mathfrak a)^{-1}(B/\mathfrak aB),
\qquad
C\otimes_Ak_0=(A\setminus\mathfrak a)^{-1}(C/\mathfrak aC).
$$
They are localizations of quotients of the stipulated Noetherian rings.

Test a finite purely inseparable field extension $K/k_0$, including the trivial one. Put
$$D=B\otimes_AK,\qquad E=C\otimes_AK.$$
The full [F.12](#algebra-lemma-Noetherian-field-extension) makes both Noetherian. Regularity of $A\to B$ makes $D$ regular. Moreover $E\cong C\otimes_BD$, and the full flat base-change proof makes $D\to E$ flat.

Choose $\mathfrak r\in\operatorname{Spec}E$ and contract it to $\mathfrak s\subset D$ and then $\mathfrak b\subset B$. The contraction of $\mathfrak b$ to $A$ is $\mathfrak a$: its elements vanish in $K$, while every element of $A\setminus\mathfrak a$ is inverted there. Consequently $k_0$ embeds in $\kappa(\mathfrak b)$. The residue-field change relevant at this point is finite, as we now check directly.

There is a natural finite-dimensional algebra
$$
Q=D\otimes_B\kappa(\mathfrak b)
\cong K\otimes_{k_0}\kappa(\mathfrak b).
$$
A finite $k_0$-basis of $K$ gives its finite basis over $\kappa(\mathfrak b)$. Since $\mathfrak s$ contracts to $\mathfrak b$, quotienting by $\mathfrak bD$ and inverting $B\setminus\mathfrak b$ carries it to a prime $\bar{\mathfrak s}$ of $Q$. Its quotient is a finite-dimensional domain over $\kappa(\mathfrak b)$, hence a field: multiplication by a nonzero element is an injective finite-dimensional linear map and supplies an inverse. This quotient is also the localization of $D/\mathfrak s$ at the nonzero images of $B\setminus\mathfrak b$. A field containing that domain and obtained by this localization is its full fraction field. Hence
$$Q/\bar{\mathfrak s}=\kappa(\mathfrak s),\qquad
[\kappa(\mathfrak s):\kappa(\mathfrak b)]<\infty.$$

Tensor associativity identifies the fibre of $D\to E$ at $\mathfrak s$ with
$$
E\otimes_D\kappa(\mathfrak s)
\cong(C\otimes_B\kappa(\mathfrak b))
   \otimes_{\kappa(\mathfrak b)}\kappa(\mathfrak s).
$$
The $B$-fibre in parentheses is Noetherian and geometrically regular. The finite residue-field extension just proved and F.12 make the displayed tensor Noetherian; the whole [F.52](#algebra-lemma-geometrically-regular-over-subfields) makes it regular. The closed fibre of the actual flat local map $D_{\mathfrak s}\to E_{\mathfrak r}$ is a localization of this ring and is regular. Its source is regular local, and both local rings are Noetherian. The entire [F.47](#algebra-lemma-flat-over-regular-with-regular-fibre) therefore makes $E_{\mathfrak r}$ regular.

This holds at every target prime; if there are none, the assertion is vacuous. Thus $E$ is regular for every finite purely inseparable $K/k_0$. The complete criterion [F.50](#algebra-lemma-geometrically-regular) now proves that the original composite fibre is geometrically regular. Applying this at every $\mathfrak a$ proves regularity of the composite, with all fibre Noetherianity conditions verified. ∎

<a id="more-algebra-lemma-regular-permanence"></a>

#### Lemma F.125: regular permanence

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 11116–11129](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L11116-L11129).

For maps $A\to B\to C$ of Noetherian rings, if $A\to C$ is regular and $B\to C$ is faithfully flat, then $A\to B$ is regular.

**Proof.** Take any inclusion of $A$-modules $U\hookrightarrow V$ and let
$$H=\ker(U\otimes_AB\longrightarrow V\otimes_AB).$$
Flatness of $C$ over $B$ identifies $H\otimes_BC$ with the kernel of this map after tensoring with $C$. Tensor associativity identifies that map with $U\otimes_AC\to V\otimes_AC$, which is injective because $A\to C$ is flat. Hence $H\otimes_BC=0$; faithfulness gives $H=0$. Tensoring every inclusion with $B$ is therefore injective, proving flatness of $A\to B$.

For a prime $\mathfrak a\subset A$, put $k=\kappa(\mathfrak a)$ and
$$F=B\otimes_Ak,\qquad G=C\otimes_Ak.$$
These are Noetherian localizations of $B/\mathfrak aB$ and $C/\mathfrak aC$ at $A\setminus\mathfrak a$. Their structural map is faithfully flat. Indeed $G\cong F\otimes_BC$, and for every $F$-module $N$ the natural balancing maps give
$$N\otimes_FG\cong N\otimes_BC.$$
Restriction to $B$ preserves exact sequences and detects a zero module. Since the right tensor functor is exact and detects zero, the left one has both properties too. This proves faithful flatness on the actual fibre rings, without a finiteness assumption on the residue-field maps.

Regularity of $A\to C$ makes $G$ geometrically regular over $k$. The entire geometric descent proof [F.51](#algebra-lemma-geometrically-regular-descent) therefore makes $F$ geometrically regular. This checks every fibre of the flat map $A\to B$, so that map is regular. If a target fibre is zero, faithfulness forces its source fibre to be zero as well; the same argument and empty local-ring tests apply. ∎

<a id="more-algebra-lemma-relative-global-complete-intersection-koszul"></a>

#### Lemma F.126: relative global complete intersection koszul

Reading source: [Stacks, Tag 07D2](https://stacks.math.columbia.edu/tag/07D2). The following proof gives the Noetherian form used in this lesson.

Let $R$ be Noetherian, $P=R[X_1,\ldots,X_n]$, and $S=P/(f_1,\ldots,f_c)$. Suppose each nonempty fibre of $R\to S$ has dimension $n-c$, as in Definition F.4. The Koszul complex $K_P(f_1,\ldots,f_c)$ has zero homology in every positive degree.

**Proof.** Let $I=(f_1,\ldots,f_c)$ and fix a prime $\mathfrak p$ of $P$. If $I\subset\mathfrak p$, the complete relative conormal argument [F.77](#algebra-lemma-relative-global-complete-intersection-conormal) makes this ordered list regular in $P_{\mathfrak p}$. The cone induction in [F.118](#more-algebra-lemma-noetherian-finite-all-equivalent) then makes its localized Koszul complex acyclic in positive degrees. That implication only needs the successive multiplication injections; it imposes no assertion of global ordered regularity outside $V(I)$.

If $I\not\subset\mathfrak p$, write $\sum_i a_i f_i=1$ in $P_{\mathfrak p}$. On the exterior complex with basis $e_i$ and differential $d(e_i)=f_i$, set $h(v)=(\sum_i a_i e_i)\wedge v$. The signed product rule gives
$$d h(v)+h d(v)=\Big(\sum_i a_i f_i\Big)v=v.$$
Thus every localized cycle is a boundary in this case too. Localization is exact and therefore commutes with kernels, images and homology, by [AG-RG-S01, Lemma 1.1](AG-RG-S01.md#1-the-algebra-of-localization). Each positive homology module now has zero localization at every prime. The local-detection proof in that same lemma makes it zero. When $c=0$, there are no positive complex terms. When $S=0$, every prime is in the contracting-homotopy case. Both cases satisfy the assertion. ∎

<a id="more-algebra-lemma-relative-regular-immersion-algebra"></a>

#### Lemma F.127: relative regular immersion algebra

Reading source: [Stacks, Tag 0CEP](https://stacks.math.columbia.edu/tag/0CEP). All tensor steps are specified below.

Take ring maps $A\to B$ and $A\to A'$, a finite list $f_1,\ldots,f_r\in B$, and $J=(f_1,\ldots,f_r)$. Assume $B/J$ is flat over $A$. Put $B'=B\otimes_A A'$, let $f_i'$ be the images, and put $J'=(f_1',\ldots,f_r')$. If the original list is quasi-regular, so is the new list. If its first Koszul homology vanishes, the new first Koszul homology vanishes. No flatness of $B$ is assumed.

**Proof.** We use the exact quotient-flatness statement AG-CA-07, Theorem 6.1: a short exact sequence with flat quotient remains short exact under any tensor functor, and an extension of two flat modules is flat.

In the quasi-regular case Definition [F.95](#more-algebra-definition-regular-ideal) identifies
$$J^n/J^{n+1}\simeq (B/J)^{\oplus\{a\in\mathbf N^r:|a|=n\}}.$$
These modules are $A$-flat. Starting with $B/J$, the sequences
$$0\to J^n/J^{n+1}\to B/J^{n+1}\to B/J^n\to0$$
therefore prove by induction that $B/J^n$ is flat for every $n\geq1$. Apply quotient-flatness to $0\to J^n\to B\to B/J^n\to0$. Its tensor identifies $J^n\otimes_A A'$ with its image in $B'$. That image is exactly $(J')^n$: the finite products of the $f_i$ generate $J^n$, and their images generate $(J')^n$. Right exactness applied to $J^{n+1}\to J^n\to J^n/J^{n+1}\to0$ now gives
$$ (J')^n/(J')^{n+1}\simeq (J^n/J^{n+1})\otimes_A A'. $$
In degree zero it gives $B'/J'=(B/J)\otimes_A A'$. The identifications commute with multiplication, since every one is induced by the images of the same products of generators. They carry each $T_i$ to $f_i'$ and prove the required polynomial graded-ring identity.

For the first-homology assertion, put $Z=\ker(B^r\xrightarrow{(f_i)}J)$. Quotient-flatness first gives an injection $J\otimes_A A'\hookrightarrow B'$, whose image is $J'$. Right exactness of
$$Z\longrightarrow B^r\longrightarrow J\longrightarrow0$$
then makes $Z\otimes_A A'$ surject onto $Z'=\ker((B')^r\xrightarrow{(f_i')}B')$. The original Koszul boundaries are the image of $\bigwedge^2 B^r\to Z$. If $H_1=0$, this map is surjective. Tensoring preserves its surjectivity, and the natural identification $(\bigwedge^2 B^r)\otimes_A A'=\bigwedge^2(B')^r$ carries its alternating boundary formula to the new formula. Consequently every element of $Z'$ is a new boundary, as required. For an empty list $J=0$ and all first complex terms vanish; both conclusions still hold. Unit ideals and zero rings cause no change to these exact-sequence arguments. ∎

<a id="more-algebra-lemma-symmetric-algebra-smooth"></a>

#### Lemma F.128: symmetric algebra smooth

Reading source: [Stacks, Tag 07M6](https://stacks.math.columbia.edu/tag/07M6). The universal-property and lifting argument is written here for arbitrary modules and rings.

For an $A$-module $M$, its symmetric algebra $C=\operatorname{Sym}_A(M)$ is smooth over $A$ precisely when $M$ is finite projective. The base-change, direct-sum and free-module identities used in D.10 hold without finiteness hypotheses.

**Proof.** Start with $\bigoplus_{d\geq0}M^{\otimes_A d}$, where degree zero is $A$. Concatenation of tensors defines its product: the balancing relations defining a tensor product are preserved by concatenation, and associativity holds on pure tensors, which generate. Quotient by the homogeneous relations $m\otimes n-n\otimes m$. Interchanging adjacent factors makes the quotient commutative. This constructs $C$, with $C_0=A$, $C_1=M$, and all its pieces generated by products from degree one. Projection $\epsilon:C\to A$ is an algebra map. If $J=\ker\epsilon$, the homogeneous degree calculation gives $J/J^2=M$.

For a commutative $A$-algebra $D$, an $A$-linear map $u:M\to D$ extends by the formula
$$m_1\otimes\cdots\otimes m_d\longmapsto u(m_1)\cdots u(m_d).$$
It respects balancing and the displayed commutation relations, hence defines an algebra map $C\to D$. Every algebra map has this restriction and is determined by it. These constructions are inverse, proving the universal property.

That property gives actual mutually inverse maps
$$\begin{aligned}
B\otimes_A\operatorname{Sym}_A(M)&\simeq\operatorname{Sym}_B(B\otimes_A M),\\
\operatorname{Sym}_A(M\oplus N)&\simeq\operatorname{Sym}_A(M)\otimes_A\operatorname{Sym}_A(N),\\
\operatorname{Sym}_A(A^n)&\simeq A[X_1,\ldots,X_n].
\end{aligned}$$
In the first pair of maps send $b\otimes m$ to $b\otimes m$, and send $m$ back to $1\otimes m$; the tensor-algebra coproduct calculation in [AG-RG-S01, Lemma 1.0](AG-RG-S01.md#1-the-algebra-of-localization) combines the latter map with the base map from $B$. For the second, send $(m,n)$ to $m\otimes1+1\otimes n$; the inverse comes from the two inclusions into $M\oplus N$ and the same coproduct formula. For the last, send basis vectors to variables and variables back to basis vectors. Each composite fixes the base ring and every degree-one generator, so is identity. The maps preserve degree. These verifications prove the identities, including reduction modulo a base ideal, used later in the lesson.

Suppose first $C$ is smooth. It is finitely presented, hence has algebra generators $z_1,\ldots,z_s$. The differences $y_i=z_i-\epsilon(z_i)$ generate $J$: for a polynomial $P$, successive subtraction in each variable expresses $P(z)-P(\epsilon(z))$ as a sum of multiples of those differences. For an element of $J$ the second term is zero. Thus $M=J/J^2$ is finite. Choose a finite free surjection $\pi:F\to M$.

For any module $V$, form the square-zero algebra $A\oplus V$, with multiplication $(a,v)(b,w)=(ab,aw+bv)$. The map $A\oplus F\to A\oplus M$ induced by $\pi$ is surjective with square-zero kernel. The linear map $m\mapsto(0,m)$ extends to an algebra map $C\to A\oplus M$. The formal-smoothness comparison proved in AG-CA-17, Theorem 3.1 and Section 4 gives a lift to $A\oplus F$. Its first coordinate on $m$ is zero, because reduction leaves that coordinate unchanged. Write its second coordinate as $s(m)$. Restriction of the algebra map makes $s$ linear and $\pi s=1_M$. Hence
$$F=s(M)\oplus\ker\pi,$$
as the decomposition $f=s(\pi f)+(f-s(\pi f))$ and application of $\pi$ verify. This is exactly finite projectivity of $M$.

Conversely write $F=A^n=M\oplus K$ with maps $i:M\to F$ and $\pi:F\to M$ satisfying $\pi i=1_M$. The projections of a basis of $F$ generate $K$. By the universal property, $C$ is the quotient of $A[X_1,\ldots,X_n]$ by the linear forms corresponding to $K$: maps from that quotient are precisely linear maps $F\to D$ killing $K$, and hence precisely linear maps $M\to D$. The generator maps give the inverse algebra identifications. Since $K$ has the finite generating list just exhibited, this is a finite presentation of $C$.

Now take a square-zero surjection $D\to D/H$ of $A$-algebras and a map $C\to D/H$. Its restriction is a linear $u:M\to D/H$. Lift the finitely many values of $u\pi$ on the free basis of $F$ to elements of $D$. The resulting linear map $v:F\to D$ reduces to $u\pi$, so $vi$ lifts $u$. Its algebra extension lifts the original map from $C$. Thus $C$ is formally smooth; its finite presentation and the same proved formal/conormal comparison make it smooth. The constructions include $M=0$, $n=0$, and the zero ring. ∎

<a id="more-algebra-lemma-syntomic-lci"></a>

#### Lemma F.129: syntomic lci

Reading source: [Stacks, Tag 07D3](https://stacks.math.columbia.edu/tag/07D3). We use the Noetherian-base version and specify the syntomic conditions directly.

Let $R$ be Noetherian. A map $R\to S$ is syntomic if and only if it is flat and a local complete intersection homomorphism in Definition [F.94](#more-algebra-definition-local-complete-intersection). Here syntomic means flat, finitely presented, with local complete intersection fibres as in Definition F.2.

**Proof.** If $R\to S$ is syntomic, the complete principal-neighbourhood construction [F.87](#algebra-lemma-syntomic) covers $\operatorname{Spec}S$ by charts that have relative global complete intersection presentations. On each chart [F.126](#more-algebra-lemma-relative-global-complete-intersection-koszul) makes the presenting equations Koszul-regular. Thus each chart is a local complete intersection homomorphism. A finite collection of the principal charts suffices, and [F.114](#more-algebra-lemma-lci-local) proves their local complete intersection property descends to $R\to S$. Flatness was one of the syntomic conditions.

Conversely suppose $R\to S$ is flat and a local complete intersection. The finite-kernel and arbitrary-presentation proof [F.94.A](#more-algebra-lemma-lci-presentation-independent) makes it finitely presented. Choose $S=P/I$ with $P=R[X_1,\ldots,X_n]$. For a field-valued base map $R\to k$, put $P'=k[X_1,\ldots,X_n]$ and $S'=S\otimes_R k=P'/I'$, with $I'$ the image of $I$.

Fix a prime $\mathfrak q'$ of $S'$ and its inverse image $\mathfrak p'$ in $P'$. Contract to a prime $\mathfrak p$ of $P$. Definition [F.95](#more-algebra-definition-regular-ideal) and the presentation comparison give $g\notin\mathfrak p$ such that $I_g$ has a finite Koszul-regular generating list $f_1,\ldots,f_r$. Its first Koszul homology is zero. The quotient $P_g/I_g=S_g$ is $R$-flat, since localization is flat and flat maps compose. Apply [F.127](#more-algebra-lemma-relative-regular-immersion-algebra) to $R\to P_g$ and $R\to k$. It proves first-homology vanishing for the image list in $P'_g$; this list generates $I'_g$ by tensor right exactness. The image of $g$ is outside $\mathfrak p'$ by contraction. Localize at $\mathfrak p'$. This is a Noetherian polynomial local ring, the list lies in its maximal ideal, and [F.118](#more-algebra-lemma-noetherian-finite-all-equivalent) makes it regular there. The full field complete-intersection neighbourhood argument [F.57](#algebra-lemma-lci) therefore gives a global complete intersection chart of $S'$ around $\mathfrak q'$. Since every prime of every fibre has such a chart, the fibres meet Definition F.2. Together with flatness and finite presentation this proves syntomicity. If a fibre or $S$ is zero there are no primes requiring charts; the same conditions and argument remain valid. ∎

<a id="more-algebra-lemma-transitive-lci-at-end"></a>

#### Lemma F.130: transitive lci at end

Reading source: [Stacks, Tag 07D4](https://stacks.math.columbia.edu/tag/07D4). The two rows and their maps are written explicitly.

Let $A\to B\to C$ be maps, with $B\to C$ a local complete intersection homomorphism. Choose $P=A[X_s:s\in\Sigma]\twoheadrightarrow B$ with kernel $I$, allowing an arbitrary set $\Sigma$. Choose $B[Y_1,\ldots,Y_m]\twoheadrightarrow C$ with kernel $J$. Put $Q=P[Y_1,\ldots,Y_m]$ and let $K$ be the kernel of $Q\to C$. There are natural short exact rows of $C$-modules
$$\begin{gathered}
0\to(I/I^2)\otimes_B C\to K/K^2\to J/J^2\to0,\\
0\to\Omega_{P/A}\otimes_P C\to\Omega_{Q/A}\otimes_Q C
\to\Omega_{B[Y]/B}\otimes_{B[Y]} C\to0.
\end{gathered}$$
The conormal differential maps from the first row to the second commute. In particular the cotangent transitivity sequence is exact with zero at the left:
$$\begin{gathered}
0\to H_1(\NL_{B/A}\otimes_B C)\to H_1(L_{C/A})\to H_1(L_{C/B})\\
\to\Omega_{B/A}\otimes_B C\to\Omega_{C/A}\to\Omega_{C/B}\to0.
\end{gathered}$$

**Proof.** The kernel of $Q\to B[Y]$ is $IQ$, by comparing polynomial coefficients, and $J=K/IQ$. The arbitrary-ring presentation comparison [F.94.A](#more-algebra-lemma-lci-presentation-independent) makes $J$ a Koszul-regular ideal in this chosen finite polynomial presentation. In particular it is $H_1$-regular. Apply the intersection identity [F.101](#more-algebra-lemma-conormal-sequence-H1-regular-ideal) to $Q\to Q/IQ$ and the ideal $K$. It gives
$$IQ\cap K^2=(IQ)K.$$
Thus the kernel of $K/K^2\to J/J^2$ is $IQ/(IQ)K$, embedded in $K/K^2$. On the other hand
$$IQ/(IQ)K\simeq (I/I^2)\otimes_B C.$$
To check this identity directly, polynomial coefficients identify $IQ/I^2Q=(I/I^2)\otimes_B B[Y]$. Quotienting by the products with $J=K/IQ$ gives the right-hand tensor with $C=B[Y]/J$, and gives $IQ/(IQ)K$ on the left; $I^2Q\subset(IQ)K$ already. The maps send a generator class of $I$ to its class in $K/K^2$. This proves exactness of the first row, including its left injection and right surjection.

The second row is the split sequence of free differential modules on the $X$ symbols, on both the $X$ and $Y$ symbols, and on the $Y$ symbols. Inclusion and projection give the maps, and inclusion of the $Y$ symbols is a splitting. These statements remain true for an infinite set $\Sigma$, since each polynomial and differential involves finitely many symbols. The vertical maps send a relation $f$ to $df$ after reduction in $C$. Including a relation from $I$, or reducing one from $K$ modulo $IQ$, commutes with this differentiation; hence the square on each pair of maps commutes.

Apply the complete snake argument [F.84](#algebra-lemma-snake) to these actual short exact rows. Their kernel and cokernel sequence begins with zero and ends with zero. The polynomial-presentation homotopy comparison [F.11](#algebra-lemma-NL-homotopy) identifies the middle and right kernels with the indicated first cotangent homologies and their cokernels with the corresponding differential modules. For the left vertical map, right exactness identifies its source and target with the terms of $\NL_{B/A}\otimes_B C$. Its kernel is therefore $H_1(\NL_{B/A}\otimes_B C)$, and its cokernel is $\Omega_{B/A}\otimes_B C$. No flatness of $B\to C$ is needed or inferred in this identification. The representative description of the snake connecting map agrees with the cotangent map in [F.42](#algebra-lemma-exact-sequence-NL): lift a relation, differentiate and take the class in the left cokernel. Thus the displayed sequence has the specified canonical maps. Empty variable lists and the zero target obey the same quotient and complex formulas. ∎

<a id="more-algebra-lemma-transitivity-gamma"></a>

#### Lemma F.131: transitivity gamma

Reading source: [Stacks, Tag 07E2](https://stacks.math.columbia.edu/tag/07E2).

For any tower of fields $K\subset L\subset M$, the natural sequence
$$
\begin{gathered}
0\longrightarrow H_1(L_{L/K})\otimes_LM
\longrightarrow H_1(L_{M/K})\longrightarrow H_1(L_{M/L})\\
\longrightarrow\Omega_{L/K}\otimes_LM
\longrightarrow\Omega_{M/K}\longrightarrow\Omega_{M/L}\longrightarrow0.
\end{gathered}
$$
is exact, including its first injection. No finite-generation assumption is imposed on the fields.

**Proof.** First replace $M$ by a global complete-intersection $L$-algebra $C=L[Y_1,\ldots,Y_r]/J$, with $J$ generated by a regular list. Choose a polynomial presentation $P=K[X_s]\twoheadrightarrow L$ with kernel $I$, allowing an arbitrary set of variables. Let $Q=P[Y_1,\ldots,Y_r]$ and let $H=\ker(Q\to C)$; the image of $H$ in $Q/IQ=L[Y]$ is $J$.

The regular-list Koszul argument in [F.118](#more-algebra-lemma-noetherian-finite-all-equivalent) proves vanishing of its first homology; that direction uses only the successive multiplication injections. Thus [F.101](#more-algebra-lemma-conormal-sequence-H1-regular-ideal), applied to $IQ\subset H$ in $Q$, gives $IQ\cap H^2=IH$. Polynomial coefficient expansion identifies
$$
IQ/IH=(I/I^2)\otimes_L C.
$$
Indeed first reduce $I$ modulo $I^2$, extend polynomial coefficients to $L[Y]$, and then impose the equations of $J$; these are precisely the relations obtained by dividing $IQ$ by $IH$. Lifting representatives of $J$ to $H$ gives the short exact conormal row
$$
0\longrightarrow (I/I^2)\otimes_L C
\longrightarrow H/H^2\longrightarrow J/J^2\longrightarrow0.
$$
The first injection is exactly the intersection equality just proved. Differentiation, with coefficients evaluated in $C$, maps this row to the split exact row
$$
0\longrightarrow\Omega_{P/K}\otimes_P C
\longrightarrow\Omega_{Q/K}\otimes_Q C
\longrightarrow\Omega_{L[Y]/L}\otimes_{L[Y]}C\longrightarrow0.
$$
Its maps include the free $dX_s$ coordinates and project to the free $dY_i$ coordinates. Differentiating any lifted polynomial relation verifies commutativity. The complete snake proof [F.84](#algebra-lemma-snake) now gives the asserted six-term kernel/cokernel sequence for $C$, with zero at both ends. Presentation comparison [F.11](#algebra-lemma-NL-homotopy) identifies its kernels and cokernels with the named first conormal homologies and differential modules. For the left terms, tensoring over the field $L$ is exact, so they are $H_1(L_{L/K})\otimes_L C$ and $\Omega_{L/K}\otimes_L C$.

Finally [F.23](#algebra-lemma-colimit-syntomic) writes $M$ as a directed union of global complete-intersection $L$-subalgebras of this kind. The relation and differential comparison [F.24](#algebra-lemma-colimits-NL) identifies their cotangent complexes over both $K$ and $L$ with those of the union. The sequence maps agree at each inclusion because they were defined by the same polynomial representatives and their derivatives. Filtered colimits are exact: a representative killed in a colimit is killed at some common later stage, and finite sums and equalities can all be placed at one such stage, as proved in F.24. The tensor generators and their balanced relations likewise give $\varinjlim(C\otimes_L V)=M\otimes_L V$ for each $L$-vector space $V$. Taking the colimit of the exact sequences therefore proves the full sequence for $M$, including its first zero. Empty equation lists and infinitely generated intermediate fields obey the same argument.
∎

<a id="more-algebra-proposition-Noetherian-complete-G-ring"></a>

#### Proposition F.132: Noetherian complete G ring

Reading source: [AI Integrated Stacks, pinned More Algebra, lines 12965–12999](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex#L12965-L12999).

Every complete Noetherian local ring is a G-ring.

**Proof.** We first prove the following generic-fibre assertion for every complete Noetherian local domain $B$, with fraction field $K$: for each prime $\mathfrak p\subset B$,
$$\widehat{B_{\mathfrak p}}\otimes_BK$$
is geometrically regular over $K$. Choose the embedded regular complete local subring $A_0\subset B$ of [F.25](#algebra-lemma-complete-local-Noetherian-domain-finite-over-regular). It can be chosen as a power-series ring over a field or a Cohen ring, and $B$ is finite over it. Write $F=\operatorname{Frac}(A_0)$ and $\mathfrak p_0=\mathfrak p\cap A_0$.

The localization $(A_0)_{\mathfrak p_0}$ is regular local by AG-CA-14, Theorem 3.2, and its completion is Noetherian regular local by AG-CA-19, Theorem 4.1. Its localization
$$G=\widehat{(A_0)_{\mathfrak p_0}}\otimes_{A_0}F$$
is therefore Noetherian regular. If $F$ has characteristic zero, there are no nontrivial finite purely inseparable extensions of $F$, and [F.50](#algebra-lemma-geometrically-regular) makes $G$ geometrically regular. If its characteristic is positive, the chosen subring is $k[[X_1,\ldots,X_n]]$; the Cohen-ring alternative has characteristic-zero fraction field. The case $m=0$ of [F.110](#more-algebra-lemma-helper-G-ring) makes $G$ geometrically regular in this positive-characteristic case as well.

The finite map $A_0\to B$ is quasi-finite at $\mathfrak p$. To see the fibre condition, its algebra over any residue field is finite-dimensional. Descending chains of ideals stabilize because their vector-space dimensions decrease, so it is Artinian. The full product theorem AG-CA-03, Theorem 4.2 makes its prime points a finite discrete set. Every prime quotient is a finite-dimensional domain, hence a field, giving finite residue extensions. Equivalently the finite morphism satisfies the quasi-finite fibre criterion used in [F.26](#algebra-lemma-completion-at-quasi-finite-prime). Apply assertion (1) of [F.96](#more-algebra-lemma-G-ring-goes-up-quasi-finite) to the pairs $(0)\subset\mathfrak p$ in $B$ and $(0)\subset\mathfrak p_0$ in $A_0$. Both rings are domains and the subring is injective, so these are the exact contractions. Its assumption is the geometric regularity of $G$ just proved. Its conclusion is the desired generic-fibre assertion for $B$. This uses the single specified fibre assertion of F.96, and does not presuppose that $A_0$ is a G-ring.

Now let $A$ be an arbitrary complete Noetherian local ring. For each prime $\mathfrak q\subset A$, the domain $B=A/\mathfrak q$ is complete Noetherian local. Indeed AG-CA-19, Theorem 3.1 identifies completion of this finite quotient with $\widehat A\otimes_A(A/\mathfrak q)=A/\mathfrak q$, with its induced maximal-adic topology. For every prime $\mathfrak p$ containing $\mathfrak q$, put $\overline{\mathfrak p}=\mathfrak p/\mathfrak q$. The generic assertion applied to this domain gives geometric regularity of
$$\widehat{B_{\overline{\mathfrak p}}}\otimes_B\operatorname{Frac}(B).$$
These are all pairs required by the exact quotient criterion [F.99](#more-algebra-lemma-check-G-ring-easy). That criterion identifies the displayed ring with the $\mathfrak q$-fibre of $A_{\mathfrak p}\to\widehat{A_{\mathfrak p}}$, and proves that geometric regularity for every such pair makes $A$ a G-ring. Thus no other prime fibres are omitted. If $A$ is the zero ring, there are no primes and the definition is vacuous. ∎

<a id="more-algebra-proposition-characterization-geometrically-regular"></a>

#### Proposition F.133: characterization geometrically regular

Reading source: [Stacks, Tag 07E5](https://stacks.math.columbia.edu/tag/07E5). The proof below includes both finite-defect dimension arguments.

Let $k$ have characteristic $p>0$, and let $(A,\mathfrak m,K)$ be a Noetherian local $k$-algebra. The following conditions are equivalent:

1. $A$ is geometrically regular over $k$.
2. $A\otimes_k k'$ is regular whenever $k\subset k'\subset k^{1/p}$ and $[k':k]<\infty$.
3. $A$ is regular and $H_1(L_{K/k})\to\mathfrak m/\mathfrak m^2$ is injective.
4. $A$ is regular and $\Omega_{k/\mathbf F_p}\otimes_k K\to\Omega_{A/\mathbf F_p}\otimes_A K$ is injective.

**Proof.** Write $E=\mathfrak m/\mathfrak m^2$, $H=H_1(L_{K/k})$, $U=\Omega_{k/\mathbf F_p}\otimes_k K$ and $V=\Omega_{A/\mathbf F_p}\otimes_A K$. The quotient presentation of $K$ over $A$ has no relative polynomial variables, so its naive complex is $E\to0$. Every field is formally smooth over its prime field by AG-CA-19S, Lemma 1.1, and [F.17](#algebra-lemma-characterize-formally-smooth-field-extension) consequently gives $H_1(L_{K/\mathbf F_p})=0$. The complete quotient transitivity proof [F.42](#algebra-lemma-exact-sequence-NL) and the field version [F.131](#more-algebra-lemma-transitivity-gamma) give
$$\begin{gathered}
0\to E\to V\to\Omega_{K/\mathbf F_p}\to0,\\
0\to H\to U\to\Omega_{K/\mathbf F_p}\to\Omega_{K/k}\to0.
\end{gathered}$$
Naturality maps the second row into the first, with identity on $\Omega_{K/\mathbf F_p}$. If $u\in U$ maps to zero in $V$, it maps to zero in $\Omega_{K/\mathbf F_p}$ and hence comes from a unique $h\in H$. The first row embeds $E$ in $V$, so this $h$ maps to zero in $E$. Conversely an $h$ killed in $E$ maps to a vector of $U$ killed in $V$. Thus the two kernels are canonically isomorphic, proving (3) equivalent to (4).

Assume (3), and take any finite purely inseparable $k'/k$. Set $A'=A\otimes_k k'$. A basis of $k'$ containing $1$ makes $A'$ finite free over $A$ and the structural map injective. It is integral by the determinant proof AG-CA-05, Theorem 1.2. For some $e$, $(k')^{p^e}\subset k$; applying Frobenius to a finite tensor sum shows $x^{p^e}\in A$ for every $x\in A'$. For a prime $\mathfrak q$ over $\mathfrak p$, the equivalence $x\in\mathfrak q\Longleftrightarrow x^{p^e}\in\mathfrak p$ determines $\mathfrak q$ uniquely. Lying over supplies it. Integral maximal-ideal correspondence, AG-CA-05, Theorem 3.3, makes $A'$ local with maximal ideal $\mathfrak m'$ over $\mathfrak m$. It is Noetherian, since it is finite over $A$. Write $K'=A'/\mathfrak m'$ and $E'=\mathfrak m'/\mathfrak m'^2$. The surjection $K\otimes_k k'\to K'$ proves $[K':K]<\infty$. The integral inclusion preserves dimension by AG-CA-05, Theorem 5.1.

Put $H'=H_1(L_{K'/k'})$. Relative quotient transitivity gives rows
$$\begin{gathered}
0\to H\otimes_K K'\to E\otimes_K K'\to V_0\to W\to0,\\
H'\to E'\to V_0\to W'\to0,
\end{gathered}$$
where $W=\Omega_{K/k}\otimes_K K'$, $W'=\Omega_{K'/k'}$, and differential base change AG-CA-15, Theorem 2.1 identifies the two middle differential terms $V_0$. Let $\alpha:W\to W'$ and $\beta:H\otimes_K K'\to H'$ be the natural maps. Surjectivity from the common $V_0$ makes $\alpha$ surjective. Both extensions $k'/k$ and $K'/K$ are finite, so [F.108](#more-algebra-lemma-gamma-commutative-diagram) applies with transcendence degrees zero and proves
$$\dim\ker\alpha-\dim\ker\beta+\dim\operatorname{coker}\beta=0.$$
All these defects are finite. Also $H$ embeds in the finite space $E$, and finite cokernel of $\beta$ therefore makes $H'$ finite.

Let $L$ and $L'$ be the images of the two conormal terms in $V_0$. Then $L\subset L'$ and $L'/L=\ker\alpha$. The first row gives $\dim E=\dim H+\dim L$; the second gives $\dim E'\leq\dim H'+\dim L'$. Consequently
$$\begin{aligned}
\dim E'-\dim E
&\leq\dim H'-\dim H+\dim\ker\alpha\\
&=\dim\operatorname{coker}\beta-\dim\ker\beta+\dim\ker\alpha=0.
\end{aligned}$$
Here only finite spaces are subtracted. Since $A$ is regular and $\dim A'=\dim A$, this says $\dim E'\leq\dim A'$. Conversely a basis of $E'$ lifts to generators of $\mathfrak m'$ by [F.10](#algebra-lemma-NAK), and AG-CA-11, Theorem 3.1 and Proposition 4.2 give $\dim A'\leq\dim E'$. Equality makes $A'$ regular. This holds for every finite purely inseparable extension, so [F.50](#algebra-lemma-geometrically-regular) proves (1).

It remains to prove (2) implies (4). Taking $k'=k$ first makes $A$ regular. Choose $a_1,\ldots,a_n\in k$ whose absolute differentials are independent. The full root-degree proof [F.81](#algebra-lemma-size-extension-pth-roots) identifies
$$k'=k(a_1^{1/p},\ldots,a_n^{1/p})=k[T_1,\ldots,T_n]/(T_i^p-a_i),\qquad [k':k]=p^n.$$
The preceding prime and dimension arguments apply to $A'=A\otimes_k k'$; by (2) it is regular. Its monic equations are a regular list, since successive monic quotient division makes each next monic polynomial injective by its leading coefficient. Their conormal classes are a free basis by [F.74](#algebra-lemma-regular-quasi-regular). All relative derivatives are zero. Thus $H_1(L_{A'/A})$ and $\Omega_{A'/A}$ are free of rank $n$. The representative connecting-map construction in F.42 sends the $i$th homology basis vector to $da_i\otimes1$, up to an immaterial common sign, and yields
$$A'^n\to\Omega_{A/\mathbf F_p}\otimes_A A'\to\Omega_{A'/\mathbf F_p}\to A'^n\to0.$$
This row stays exact after tensoring with $K'$. Indeed the last surjection splits because its target is free. Its kernel therefore embeds after tensoring, while tensor right exactness preserves the preceding cokernel presentation. Combining these two statements gives a map
$$\delta:V\otimes_K K'\longrightarrow V'=\Omega_{A'/\mathbf F_p}\otimes_{A'}K'$$
whose kernel is spanned by the $n$ vectors $da_i\otimes1$ and whose cokernel is $K'^n$.

Use the two absolute short exact rows
$$\begin{gathered}
0\to E\otimes_K K'\to V\otimes_K K'\to\Omega_{K/\mathbf F_p}\otimes_K K'\to0,\\
0\to E'\to V'\to\Omega_{K'/\mathbf F_p}\to0.
\end{gathered}$$
The left vertical map has finite equally dimensional domain and target: both dimensions equal $\dim A=\dim A'$. Its kernel and cokernel thus have equal dimensions. For the right vertical map, F.131 identifies the kernel with $H_1(L_{K'/K})$ and the cokernel with $\Omega_{K'/K}$. Their finite dimensions agree by [F.98](#more-algebra-lemma-cartier-equality), applied to the proved finite extension $K'/K$. The full snake sequence [F.84](#algebra-lemma-snake) now gives
$$\dim\ker\delta-\dim\operatorname{coker}\delta=0.$$
Every defect in this computation is finite, although the absolute differential spaces need not be finite. Since the cokernel has dimension $n$, the $n$ vectors spanning the kernel are independent. The $p$-basis proof in AG-CA-19S, Lemma 1.1, and its differential calculation F.81 give a basis of $\Omega_{k/\mathbf F_p}$ consisting of such $da_i$. Every prospective relation uses a finite subset. Applying the preceding calculation to that subset proves the full injection in (4). For $n=0$ the argument is empty. Finally (1) implies (2) directly from geometric regularity. These implications prove the equivalence. ∎

<a id="more-algebra-proposition-finite-type-over-G-ring"></a>

#### Proposition F.134: finite type over G ring

Reading source: [Stacks, Tag 07PV](https://stacks.math.columbia.edu/tag/07PV). The completed-local descent and each individual fibre reduction are explicit below.

If $R$ is a G-ring and $S$ is an essentially finite-type $R$-algebra, then $S$ is a G-ring.

**Proof.** G-rings are Noetherian by Definition [F.92](#more-algebra-definition-G-ring); finite-type algebras and their localizations are Noetherian by AG-CA-03, Theorem 2.1 and Proposition 1.2. A localization has the same prime local rings as the original ring at the surviving primes. Thus it suffices to handle finite-type algebras. Such an algebra is a quotient of a finite-variable polynomial ring. Quotient maps are quasi-finite, and [F.96](#more-algebra-lemma-G-ring-goes-up-quasi-finite) proves G-ring ascent for them. Induction on the number of variables reduces the problem to $R[X]$.

By [F.100](#more-algebra-lemma-check-G-ring-maximal-ideals), fix a maximal ideal $\mathfrak q$ of $R[X]$ and prove its local completion map regular. Let $\mathfrak p=\mathfrak q\cap R$. Replacing $R$ by $R_{\mathfrak p}$ leaves $R[X]_{\mathfrak q}$ unchanged, and this new base is a local G-ring. Write its maximal ideal as $\mathfrak m$, its completion as $\widehat R$, and put
$$A=R[X]_{\mathfrak q},\qquad B=\widehat R[X]_{\mathfrak q'}.$$
There is exactly one prime $\mathfrak q'$ above $\mathfrak q$: the quotient identity $\widehat R/\mathfrak m\widehat R=R/\mathfrak m$ gives $\widehat R[X]/\mathfrak q\widehat R[X]=R[X]/\mathfrak q$, a field. This uses AG-CA-19, Proposition 2.2 and the fact $\mathfrak m\subset\mathfrak q$. The map $A\to B$ is local and flat. It is also regular, since it is a localization of the base change of the regular G-ring map $R\to\widehat R$; these operations preserve regularity by [F.123](#more-algebra-lemma-regular-base-change).

If $B\to\widehat B$ is regular, [F.124](#more-algebra-lemma-regular-composition) makes $A\to\widehat B$ regular. The completed map $\widehat A\to\widehat B$ is faithfully flat by the full proof [F.99A](#completion-flat-local-map) for this actual flat local $A\to B$. Therefore [F.125](#more-algebra-lemma-regular-permanence) makes $A\to\widehat A$ regular. This reduces us to a complete Noetherian local base, with $\mathfrak q$ above its maximal ideal; it does not assume unrelated completions are equal.

For this complete base, fix $\mathfrak r\subset\mathfrak q$ in $R[X]$. Its completed fibre is
$$\widehat{R[X]_{\mathfrak q}}\otimes_{R[X]}\kappa(\mathfrak r).$$
Let $\mathfrak a=\mathfrak r\cap R$. Finite-module completion commutes with quotient by $\mathfrak a$, by AG-CA-19, Theorem 3.1. Since $\mathfrak a$ vanishes in the displayed residue field, replacing $R$ by $R/\mathfrak a$ gives exactly the same fibre. The quotient is still complete and Noetherian, by that theorem and Theorem 3.3. Thus assume $R$ is a complete local domain and $\mathfrak r\cap R=0$.

Choose the finite regular complete local subring $R_0\subset R$ from [F.25](#algebra-lemma-complete-local-Noetherian-domain-finite-over-regular). The map $R_0[X]\to R[X]$ is finite, hence quasi-finite at the contracted primes $\mathfrak r_0\subset\mathfrak q_0$. The prime $\mathfrak q_0$ is maximal by integral maximal-ideal correspondence; it lies above the maximal ideal of $R_0$, since $R$ is finite local over the local subring with the same residue field. Also $\mathfrak r_0\cap R_0=0$. Assertion (1) of F.96 transfers geometric regularity of this individual completed fibre from $R_0[X]$ to $R[X]$. Its tensor and completion-product proof requires only that fibre, without any prior G-ring assertion for $R_0[X]$. We may therefore assume the base domain is regular and complete.

Let $K=\operatorname{Frac}(R)$. If $\mathfrak r=0$, the fibre is $\widehat{R[X]_{\mathfrak q}}\otimes_{R[X]}\operatorname{Frac}(R[X])$, geometrically regular by the second full assertion of [F.110](#more-algebra-lemma-helper-G-ring). If $\mathfrak r\ne0$, its extension to the principal ideal domain $K[X]$ is a nonzero prime, hence generated by an irreducible polynomial. Its residue field is finite over $K$. The second complete assertion of [F.97](#more-algebra-lemma-another-helper-G-ring) proves geometric regularity of this fibre: for each finite purely inseparable test field it constructs a finite complete local domain $D$ inside that field and identifies the tested fibre with factors of
$$\big(\widehat{D[X]_{\mathfrak q_i}}\otimes_D\operatorname{Frac}(D)\big)/(X-a).$$
Its first assertion makes the parenthesized algebra regular. The extended $\partial/\partial X$ sends $X-a$ to $1$, and the proved hypersurface argument then makes the quotient regular. This quotient is used as a quotient; no localization assertion about it is required. The two prime cases exhaust the fibres. Completion is flat by AG-CA-19, Theorem 3.2, so the geometrically regular fibres make its map regular. This proves polynomial permanence and all the reductions to $S$. Zero target rings have no local rings to check. ∎

<a id="more-algebra-proposition-ubiquity-G-ring"></a>

#### Proposition F.135: ubiquity G ring

Reading source: [Stacks, Tag 07PX](https://stacks.math.columbia.edu/tag/07PX). We prove precisely the finite-type-over-$\mathbf Z$ assertion used in this programme.

Every ring essentially of finite type over $\mathbf Z$ is a G-ring.

**Proof.** The prime ideals of $\mathbf Z$ are $(0)$ and $(\ell)$ for prime integers $\ell$. At $(0)$ its local ring is $\mathbf Q$. Completion at the zero maximal ideal is identity, so this local completion map is regular.

At $(\ell)$ put $A=\mathbf Z_{(\ell)}$. Factoring an integer into its power of $\ell$ and its remaining factor shows every nonzero element of $A$ is $\ell^n u$ with $u$ a unit. Every nonzero ideal is generated by the element of smallest such order. Hence $A$ is Noetherian local with maximal ideal $(\ell)$ and only the primes $(0)$ and $(\ell)$. These are also the DVR computations in AG-CA-15, Section 1.

Write $\widehat A$ for its maximal-ideal completion. The exact quotient identities and local-ring proof AG-CA-19, Proposition 2.2, Proposition 2.3 and Theorems 3.2–3.3 make it Noetherian, complete and separated, with maximal ideal $\ell\widehat A$ and residue field $\mathbf F_\ell$. They also make $A\to\widehat A$ flat, so multiplication by $\ell$ remains injective. If $0\ne x\in\widehat A$, separatedness gives a finite largest $n$ with $x\in\ell^n\widehat A$. Thus $x=\ell^n u$, and $u$ cannot belong to $\ell\widehat A$, or maximality would fail. The local-ring unit criterion makes $u$ invertible. For two nonzero elements their product is a unit times a power of $\ell$, which is nonzero by its multiplication injection. This proves directly that $\widehat A$ is a domain. The same order argument makes its nonzero ideals powers of $\ell$ and makes $\widehat A[1/\ell]$ its fraction field.

There are just two fibres of the flat map $A\to\widehat A$. The closed fibre is $\widehat A/\ell\widehat A=\mathbf F_\ell$ over itself; the generic fibre is the field $\widehat A[1/\ell]$ over $\mathbf Q$. A field of characteristic zero is geometrically regular over any characteristic-zero subfield by [F.50](#algebra-lemma-geometrically-regular): the only finite purely inseparable test extension is the identity, and the tested ring is a field, hence regular. The closed fibre satisfies the same criterion over itself, since a finite purely inseparable extension tensored with its base field is again that extension field. Thus both fibres are geometrically regular. Definition [F.92](#more-algebra-definition-G-ring) now makes $\mathbf Z$ a G-ring. Apply the fully proved finite-type permanence [F.134](#more-algebra-proposition-finite-type-over-G-ring) and its localization step to obtain the assertion. The zero algebra is included by its empty spectrum. ∎

<a id="topology-lemma-Noetherian"></a>

#### Lemma F.136: Noetherian

Reading source: [Stacks, Tag 0052](https://stacks.math.columbia.edu/tag/0052).

Let $X$ be a Noetherian topological space. Every subspace is Noetherian, there are finitely many irreducible components, and each component contains a nonempty subset open in $X$.

**Proof.** Recall that Noetherianity means stabilization of descending sequences of closed subsets. For a subspace $T$, take a descending sequence $C_j$ closed in $T$ and choose closed $D_j\subset X$ with $C_j=T\cap D_j$. Put $E_j=D_1\cap\cdots\cap D_j$. Because the $C_j$ descend, $T\cap E_j=C_j$. The descending sequence $E_j$ stabilizes in $X$, so the sequence $C_j$ stabilizes in $T$. This proves the assertion for every subspace, including the empty one.

We first show that every closed subset of $X$ is a finite union of irreducible closed subsets. The empty subset is the union of an empty family. Otherwise, if there were closed subsets without such an expression, the descending-chain condition would supply a minimal one $C$: lacking a minimal member would allow a strictly descending sequence of counterexamples. This $C$ is nonempty and cannot itself be irreducible. Thus $C=C_1\cup C_2$, where both $C_i$ are proper subsets closed in $C$, and hence closed in $X$. Minimality supplies a finite irreducible closed cover of each $C_i$, and their combined covers supply one of $C$, a contradiction.

Apply the result to $X$. From the finite cover remove any member contained in the union of the others; this operation terminates and still leaves a cover. By [F.138](#topology-lemma-pick-irreducible-components), its members are exactly the irreducible components. There are consequently only finitely many of them.

Fix a component $C$ and list the others as $C_1,\ldots,C_s$. They are closed by [F.137](#topology-lemma-irreducible). The open set $U=X\setminus\bigcup_{i=1}^s C_i$ lies in $C$, since the components cover $X$. It is nonempty: otherwise $C$ would be the finite union of the closed subsets $C\cap C_i$. Binary irreducibility, applied repeatedly to a finite union, would force $C\subset C_i$ for some $i$, contradicting the distinctness and maximality of these components. If there are no other components, $U=X=C$, which is nonempty by the definition of an irreducible component.
 ∎

<a id="topology-lemma-irreducible"></a>

#### Lemma F.137: irreducible

Reading source: [Stacks, Tag 004W](https://stacks.math.columbia.edu/tag/004W).

In an arbitrary topological space, the closure of every irreducible subset is irreducible. Every irreducible subset is contained in an irreducible component; components are closed and together cover the space.

**Proof.** We use the nonempty convention for irreducibility. A nonempty space is irreducible exactly when any two nonempty open subsets intersect: taking complements converts this into the assertion that two proper closed subsets cannot cover it.

Let $Y\subset X$ be irreducible. An open subset of $X$ which meets $\overline Y$ meets $Y$, by the definition of closure. If two relatively open subsets of $\overline Y$ are nonempty, represent them by ambient opens. Their intersections with $Y$ are nonempty and relatively open in $Y$, so they intersect. The original two subsets therefore intersect as well. This proves irreducibility of $\overline Y$.

Consider the set of all irreducible subsets of $X$ containing $Y$, ordered by inclusion. It is nonempty because it contains $Y$. For a nonempty chain, its union $V$ is nonempty. Two nonempty relatively open subsets of $V$ meet some members of the chain. One of those members contains the other, so that member meets both opens. Its irreducibility supplies a point in their intersection. Thus $V$ is irreducible and is an upper bound in the set. The empty chain has $Y$ as an upper bound. Zorn's lemma now gives a maximal member $C$. Any irreducible subset containing $C$ also contains $Y$, so this is a maximal irreducible subset of $X$, namely a component.

The first part shows that $\overline C$ is irreducible; maximality forces $C=\overline C$, so every component is closed. Each singleton is irreducible, since its only nonempty open subset is itself. Applying the existence argument to every singleton proves that the components cover $X$. For $X=\varnothing$ both the component family and its union are empty.
 ∎

<a id="topology-lemma-pick-irreducible-components"></a>

#### Lemma F.138: pick irreducible components

Reading source: [Stacks, Tag 0G2Y](https://stacks.math.columbia.edu/tag/0G2Y).

Suppose $X=C_1\cup\cdots\cup C_n$, where every $C_i$ is irreducible and closed in $X$, and no $C_i$ lies in the union of the remaining members. Then this family is exactly the family of irreducible components of $X$.

**Proof.** Let $D$ be any irreducible component. The sets $D\cap C_i$ form a finite closed cover of $D$. Irreducibility implies that one member of a finite closed cover is the whole space: for two members this is its definition, and grouping the last member against the preceding union proves the assertion by induction. Consequently $D\subset C_i$ for some $i$. Because $C_i$ is itself irreducible, maximality of $D$ gives $D=C_i$.

Conversely fix $C_i$. The general existence argument [F.137](#topology-lemma-irreducible) puts it in a component $D$. The preceding paragraph identifies $D$ with some $C_j$. If $j\ne i$, the containment $C_i\subset C_j$ would put $C_i$ in the union of all the other members, contrary to the hypothesis. Thus $j=i$, and $C_i$ is a component. These two arguments prove equality of the families. When $n=0$, the covering assumption says $X$ is empty, and it has no nonempty irreducible components, giving the same conclusion.
 ∎

## 6. Earlier algebra and geometry

The following lessons supply the algebra used above. The henselian section argument uses [Affine descent, Zariski Main and recognition of spaces](AG-RG-S04.md), Lemma D2.2, Theorem C4.3 and Corollary B1.2. The completion and G-ring arguments are F.99A, F.110 and F.132–F.135. For the torus application, finite-type and finite-presentation descent on affine pairs is [Lemma A1.8 of the same supporting lesson](AG-RG-S04.md#affine-presentation-communication). The fixed-character splitting scheme becomes a disjoint union on its splitting cover, which is the case of AG-GS-05, Lemma 7.6 used here.

### Programme proof locators

The statement numbers specify the earlier results used in this lesson.

| Consumed source label | Earlier programme proof |
| --- | --- |
| definition regular | AG-CA-14, Section 1, definition |
| definition regular local | AG-CA-14, Section 1, definition |
| definition standard smooth | AG-CA-17, Section 4, equations (6) and (7) |
| lemma Artin Rees | AG-CA-03, Theorem 5.1 |
| lemma Noetherian irreducible components | AG-CA-03, Proposition 2.2 |
| lemma Noetherian topology | AG-CA-03, Proposition 2.2 |
| lemma Zariski topology | AG-CA-01, Theorem 1.2 and Proposition 2.1 |
| lemma artinian finite length | AG-CA-03, Theorem 4.2 |
| lemma characterize henselian | [AG-CA-20, Theorem 1.2 and Theorem 2.2](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/AG-CA/henselian-local-rings-and-henselization.html) |
| lemma characterize projective | AG-CA-06S, Section 1 |
| lemma cokernel flat | AG-CA-08, Lemma 5.1 |
| lemma compose formally smooth | AG-CA-17, Theorem 1.2 |
| lemma differentials base change | AG-CA-15, Theorem 2.1 |
| lemma differentials finitely presented | AG-CA-15, Theorem 5.1, finite polynomial presentation |
| lemma dimension base fibre equals total | AG-CA-11, Theorem 5.1 |
| lemma dimension base fibre total | AG-CA-11, Theorem 5.1 |
| lemma dimension prime polynomial ring | AG-CA-09, Theorem 4.3 |
| lemma disjoint implies product | AG-CA-01, Theorem 5.2 and Corollary 5.3 |
| lemma etale at prime | AG-CA-17, Theorem 7.2 and Corollary 7.3 |
| lemma exact sequence differentials | AG-CA-15, Theorem 3.1 |
| lemma faithfully flat universally injective | AG-CA-08, Theorem 2.2 |
| lemma finite finite fibres | AG-CA-05, Theorem 3.4 |
| lemma finite projective | AG-CA-07, Theorem 5.3 |
| lemma finite transitive | AG-CA-05, Theorem 1.2 |
| lemma flat | AG-CA-07, Theorem 2.1 |
| lemma flat base change | AG-CA-07, Proposition 3.2 |
| lemma flat eq | AG-CA-07, Theorem 5.1 |
| lemma flat going down | AG-CA-07, Theorem 6.3 |
| lemma flat tor zero | AG-CA-07, Theorem 2.1 |
| lemma formally etale etale | AG-CA-17, Theorem 2.2 and Proposition 6.1 |
| lemma integral no inclusion | AG-CA-05, Theorem 3.3 |
| lemma intersect powers ideal module zero | AG-CA-03, Theorem 6.1 |
| lemma lci CM | AG-CA-12, Corollary 6.2 |
| lemma maximal chain CM | AG-CA-12, Lemma 5.4 and Theorem 5.5 |
| lemma quasi compact | AG-CA-01, Proposition 2.3 |
| lemma rank omega | AG-CA-18, Proposition 3.1 |
| lemma reformulate CM | AG-CA-12, Theorem 4.2 and Corollary 4.3 |
| lemma regular domain | AG-CA-12, Theorem 6.1 |
| lemma regular goes up | AG-CA-14, Proposition 3.3 |
| lemma regular ring CM | AG-CA-12, Theorem 6.1 |
| lemma regular sequence powers | AG-CA-12, Proposition 1.3 |
| lemma spec localization | AG-CA-02, Theorem 3.1 |
| lemma variant local criterion flatness | AG-CA-08, Corollary 4.4 and equation (6) |
| proposition CM module | AG-CA-12, Theorem 4.2 and Corollary 4.3 |
| proposition characterize formally smooth | AG-CA-17, Theorem 3.1 |
| proposition smooth formally smooth | AG-CA-17, Theorem 3.1 and the split conormal definition of smoothness in this draft |
| lemma completion regular | AG-CA-19, Theorem 4.1 |
| complete-local simple-root lifting | AG-CA-19, Theorem 5.1 |
| finite residue fields in finite-type fibres | AG-CA-06, Theorem 2.1 |
| minimal resolutions and Tor detection | AG-CA-13, Theorem 2.2 |
| regular Noetherian rings are normal | AG-CA-15, Corollary 4.5 |
| arbitrary fields lift over their prime field | AG-CA-19S, Lemma 1.1 |
| complete local coefficient rings | AG-CA-19S, Theorem 5.1 |
| complete local power-series presentations | AG-CA-19S, Theorem 6.1 |

## Further reading

- The Stacks Project Authors, [*Smoothing Ring Maps*](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/smoothing.tex), [*Algebra*](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex), and [*More on Algebra*](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex). Individual arguments above give their exact tag or source locator.
- [AI Integrated Stacks, the consulted edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790), including its smoothing and algebra chapters.
