# Completion

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Completion collects compatible answers at every finite order. Its usefulness depends on whether those answers preserve equations, submodules and dimensions. Artin–Rees will supply the required control for finite modules over Noetherian rings. We will also see exactly why both finiteness conditions matter.

For an ideal \(I\subseteq R\), write

\[
\widehat M=\varprojlim_{n\geq1}M/I^nM,\qquad
\widehat R=\varprojlim_{n\geq1}R/I^n.
\tag{1}
\]

All completions in a statement use its specified ideal. Local ring completions use the maximal ideal. A module is *complete* when its canonical map to (1) is an isomorphism; this includes separatedness. We use Artin–Rees and Krull intersection from *Noetherian and Artinian rings*, Theorems 5.1 and 6.1; the ideal flatness criterion from *Tor and flat modules*, Theorem 2.1; and faithful flatness criteria and ideal contraction from *Faithful flatness and the local criterion for flatness*, Theorems 1.1 and 2.2.

## 1. Compatible choices in an inverse system

For maps \(A_{n+1}\to A_n\), the inverse limit is the subgroup of \(\prod_n A_n\) consisting of sequences whose neighboring coordinates agree under these maps. A map into this subgroup is precisely a compatible family of maps into all \(A_n\); this proves its universal property.

An inverse system is *Mittag–Leffler* if, for each fixed stage \(n\), the descending images of all later stages in \(A_n\) eventually become constant. Surjective transition maps satisfy this condition. [Stacks, Tag 0595.]

**Lemma 1.1.** A countable Mittag–Leffler inverse system of nonempty sets has a nonempty limit.

**Proof.** First suppose the indices are positive integers. Let \(E_n'\) be the eventual image inside \(E_n\). Its elements come from every sufficiently late stage. The maps \(E_{n+1}'\to E_n'\) are surjective: given an element in \(E_n'\), lift it from a stage beyond stabilization for both \(n\) and \(n+1\), and take its image in \(E_{n+1}\). Starting with a point of \(E_1'\), choose successive preimages. They give a compatible sequence.

For a countable directed set, enumerate its indices and choose recursively an index above both the preceding chosen index and the next index in the enumeration. This is a cofinal increasing sequence. Restricting an inverse system to it preserves its limit: recover any omitted coordinate by mapping down from a chosen index above it, and compatibility makes this independent of the choice. It also preserves the Mittag–Leffler condition. Apply the integer-indexed case. \(\square\)

**Theorem 1.2.** For a short exact sequence of countable directed inverse systems of abelian groups, if \((A_n)\) is Mittag–Leffler, then

\[
0\longrightarrow\varprojlim A_n
\longrightarrow\varprojlim B_n
\longrightarrow\varprojlim C_n\longrightarrow0
\tag{2}
\]

is exact. [Stacks, Tags 0598, 02N1.]

**Proof.** Injectivity and the kernel assertion hold coordinate by coordinate. Fix a compatible element \(c=(c_n)\) in the last limit. At stage \(n\), its set of lifts in \(B_n\) is a nonempty coset of \(A_n\). The images of later lift sets inside this set are nested nonempty cosets of the corresponding images of \(A_j\) in \(A_n\). Once these subgroups stabilize, the nested cosets coincide. Thus the system of lift sets is Mittag–Leffler. Lemma 1.1 supplies compatible lifts, proving surjectivity. \(\square\)

Two descending filtrations \(F_n,G_n\) of the same module are *cofinal* if every term of either contains some term of the other. Their inverse-limit quotients are canonically isomorphic. To define each quotient coordinate, project from a sufficiently fine term of the other filtration. A common finer term proves independence of the choice and compatibility; using it again proves that the two resulting maps compose to the identity.

## 2. Topology and the powers of the ideal

The \(I\)-adic neighborhoods of \(m\in M\) are \(m+I^nM\). The kernel of \(M\to\widehat M\) is \(\bigcap_n I^nM\). The closure of a submodule \(N\) is
\(\bigcap_n(N+I^nM)\), directly from this neighborhood description. Ring operations and module actions on the limits are defined coordinatewise, so \(\widehat M\) is a \(\widehat R\)-module.

**Lemma 2.1.** For any ring and any submodule \(N\subseteq M\),

\[
0\longrightarrow\varprojlim N/(N\cap I^nM)
\longrightarrow\widehat M
\longrightarrow\widehat{M/N}\longrightarrow0
\tag{3}
\]

is exact. In particular completion preserves surjections.

**Proof.** The corresponding quotient sequence is exact at each stage: the quotient filtration on \(M/N\) is \(I^n(M/N)\). The transition maps on the left are surjective, since they are quotients of the same module \(N\). Apply Theorem 1.2. \(\square\)

The left term in (3) uses the *induced* filtration on \(N\), which need not be its own \(I\)-adic filtration.

**Proposition 2.2.** If \(I\) is finitely generated, then for every \(R\)-module \(M\), without a finiteness condition on \(M\),

\[
I^a\widehat M=\ker(\widehat M\to M/I^aM),\qquad
\widehat M/I^a\widehat M=M/I^aM.
\tag{4}
\]

Consequently \(\widehat M\) is \(I\)-adically complete. [Stacks, Tag 05GG; the theorem is attributed there to Matlis, and the finite-generator proof to Bjorn Poonen (5 November 2016).]

**Proof.** For \(n\geq a\), apply Theorem 1.2 to

\[
0\longrightarrow I^aM/I^nM
\longrightarrow M/I^nM\longrightarrow M/I^aM\longrightarrow0.
\tag{5}
\]

The left system has surjective transitions. Its limit is the completion of \(I^aM\), because the latter's own filtration is
\(I^b(I^aM)=I^{a+b}M\). Choose finite generators \(h_1,\ldots,h_r\) of \(I^a\). The surjection \(M^r\to I^aM\), given by these generators, remains surjective on completion by Lemma 2.1. Completion commutes with this finite direct sum, as is seen coordinatewise. Composing with the injection supplied by (5), its image in \(\widehat M\) is exactly \(I^a\widehat M\). This proves the kernel identity and the quotient identity. Taking their compatible inverse limits proves that the canonical map from \(\widehat M\) to its completion is an isomorphism. \(\square\)

The inverse-limit topology always uses the kernels of the projections in (1). Proposition 2.2 identifies them with ideal powers when \(I\) is finite. Without that hypothesis, the two topologies can differ; a completion can fail to be complete for its own maximal ideal, as Exercise 7.6 shows.

For any complete ring with respect to an ideal \(J\), one has \(J\subseteq\operatorname{Jac}(R)\). Indeed, for \(u\in J\), the partial sums of \(\sum_{i\geq0}u^i\) converge; multiplication by \(1-u\) gives one in the limit. Applying this to every \(u=av\), \(v\in J\), proves the Jacobson radical assertion by its unit characterization.

**Proposition 2.3.** Completion at a maximal ideal \(\mathfrak m\) is a local ring with residue field \(R/\mathfrak m\). Its maximal ideal is the kernel of projection to that field; when \(\mathfrak m\) is finite, it equals \(\mathfrak m\widehat R\).

**Proof.** Each \(R/\mathfrak m^n\) is local: the radical of \(\mathfrak m^n\) is \(\mathfrak m\), so there is exactly one maximal ideal. An element of the limit with nonzero residue has a unit in every coordinate. Their inverses are compatible and give its inverse in the limit. The projection to \(R/\mathfrak m\) is surjective, by successive lifting through the surjective transition maps. Hence its kernel is the unique maximal ideal. The last assertion is (4). \(\square\)

## 3. Noetherian exactness, tensoring and flatness

**Theorem 3.1.** If \(R\) is Noetherian, completion is exact on finite \(R\)-modules, and for every such module

\[
M\otimes_R\widehat R\ \cong\ \widehat M.
\tag{6}
\]

[Stacks, Tag 00MA.]

**Proof.** In a short exact sequence \(0\to N\to M\to L\to0\) of finite modules, Artin–Rees supplies \(c\) with

\[
I^nN\subseteq N\cap I^nM\subseteq I^{n-c}N
\quad(n\geq c).
\tag{7}
\]

These filtrations on \(N\) are cofinal. Lemma 2.1 and the cofinal-filtration comparison turn (3) into the required exact sequence
\(0\to\widehat N\to\widehat M\to\widehat L\to0\).

A finite \(M\) has a finite presentation \(R^r\to R^s\to M\to0\), because kernels of maps between finite modules over a Noetherian ring are finite. Completing this presentation is right exact by the exactness just proved. Tensoring it with \(\widehat R\) is right exact as well. Indeed, for any target module, balanced bilinear maps on the free generators and the tensor factor descend uniquely to the presented module precisely when they vanish on the relations. The tensor universal property therefore identifies maps from its tensor product to every target with maps from that same cokernel, proving right exactness. Both have the same map \(\widehat R^r\to\widehat R^s\), with the original matrix entries. Identifying their cokernels gives the natural isomorphism (6). \(\square\)

**Theorem 3.2.** For a Noetherian \(R\), the map \(R\to\widehat R\) is flat. If \(I\subseteq\operatorname{Jac}(R)\), it is faithfully flat.
[Stacks, Tags 00MB, 00MC.]

**Proof.** Every ideal \(J\) of \(R\) is finite. Theorem 3.1 identifies its tensor map
\(J\otimes_R\widehat R\to\widehat R\)
with the injection \(\widehat J\to\widehat R\). The ideal criterion for flatness applies.

If \(I\) is in every maximal ideal \(\mathfrak m\), the completion of \(R/\mathfrak m\) is itself. Formula (6) gives
\(\widehat R/\mathfrak m\widehat R=R/\mathfrak m\ne0\).
The maximal-residue criterion for a flat module makes \(\widehat R\) faithfully flat. \(\square\)

Faithful flatness gives an injection \(R\to\widehat R\), and for every ideal \(J\) of \(R\),

\[
J\widehat R\cap R=J.
\tag{8}
\]

These follow from the universal injection and ideal-contraction theorem of the faithful flatness lesson. For local completion, \(I=\mathfrak m\) always satisfies the hypothesis.

**Theorem 3.3.** If \(R\) is Noetherian, then \(\widehat R\) is Noetherian and complete with respect to \(J=I\widehat R\). Moreover

\[
\widehat R/J^n=R/I^n,\qquad
\operatorname{gr}_J\widehat R=\operatorname{gr}_I R.
\tag{9}
\]

[Stacks, Tags 05GH, 0316, 031C.]

**Proof.** The ideal \(I\) is finite, so Proposition 2.2 proves completeness and the quotient identities. The extended-ideal powers are \(J^n=I^n\widehat R\). The compatible identities for two consecutive quotients identify their kernels, giving the graded-ring identity.

If \(I\) has \(r\) generators, its associated graded ring is a quotient of
\((R/I)[T_1,\ldots,T_r]\), by mapping each variable to the corresponding degree-one class. Thus the Hilbert basis theorem makes this graded ring Noetherian.

Let \(Q\) be any ideal of \(\widehat R\). Its initial classes form the homogeneous ideal
\(\bigoplus_n(Q\cap J^n)/(Q\cap J^{n+1})\)
inside \(\operatorname{gr}_J\widehat R\). Choose finitely many homogeneous generators and lift them to \(q_1,\ldots,q_\ell\in Q\), of respective orders \(d_i\). We prove they generate \(Q\) itself.

Starting with \(q\in Q\), at step \(n\) express the degree-\(n\) class of the residual element by those generators. Lift its coefficients to \(a_{i,n}\in J^{n-d_i}\) for \(d_i\leq n\), and use zero for the other indices. Subtraction leaves a residual element in \(Q\cap J^{n+1}\). For each fixed \(i\), the series \(\sum_n a_{i,n}\) converges in the complete ring, since the orders of its terms tend to infinity. Write its sum as \(a_i\). Then
\(q-\sum_i a_iq_i\)
belongs to every \(J^n\) and is zero by separatedness. Thus \(Q=(q_1,\ldots,q_\ell)\). Every ideal is finite, proving Noetherianity without assuming in advance that \(Q\) is closed. \(\square\)

When the original Noetherian ring is \(I\)-adically complete, (6) shows that every finite module is complete. If \(I\) lies in its Jacobson radical, every submodule of a finite module is closed: its finite quotient has zero intersection of ideal powers by Krull intersection, and the closure formula in §2 applies. Completeness of quotients must retain this separation condition.

## 4. Local dimension and regularity

**Theorem 4.1.** For a Noetherian local ring \((R,\mathfrak m,\kappa)\), its completion is a Noetherian local ring with maximal ideal \(\widehat{\mathfrak m}=\mathfrak m\widehat R\), residue field \(\kappa\), and

\[
\dim\widehat R=\dim R,\qquad
R\text{ regular}\ \Longleftrightarrow\ \widehat R\text{ regular}.
\tag{10}
\]

**Proof.** Propositions 2.3 and Theorem 3.3 give the ring and residue assertions. Formula (9) gives

\[
\ell_{\widehat R}(\widehat R/\widehat{\mathfrak m}^{\,n})
=\ell_R(R/\mathfrak m^n).
\tag{11}
\]

The lengths agree because both actions factor through the same quotient ring, so their submodule lattices agree. Theorem 2.1 of *Dimension theory of Noetherian local rings* identifies the degree of this Hilbert–Samuel polynomial with the local dimension. Hence the dimensions are equal. The first graded piece in (9) identifies
\(\widehat{\mathfrak m}/\widehat{\mathfrak m}^2\)
with \(\mathfrak m/\mathfrak m^2\), so the embedding dimensions are equal too. Equality of embedding dimension and dimension is the definition of regularity in both rings. \(\square\)

Compatible truncated polynomials give, directly,

\[
\widehat{k[X_1,\ldots,X_d]_{(X_1,\ldots,X_d)}}
=k[[X_1,\ldots,X_d]].
\tag{12}
\]

At order \(n\), only monomials of total degree smaller than \(n\) remain. Every denominator outside the maximal ideal has nonzero constant term and a truncated geometric-series inverse, so localization does not change these quotients. Their compatible coefficients are exactly formal power series. The same reasoning gives the \((T)\)-adic completion of \(k[T]\) and of \(k[T]_{(T)}\) as \(k[[T]]\).

The next required lesson, [Coefficient rings and the Cohen structure theorem](coefficient-rings-and-cohen-structure.md), proves coefficient-ring existence for every complete local ring, without a Noetherian or perfect-residue-field hypothesis. Its Theorem 6.1 proves the **Cohen structure theorem**: a complete local ring with finitely generated maximal ideal is a quotient of a finite-variable power-series ring over a field or a Cohen ring. In positive residue characteristic the coefficient map may have a kernel when a power of the prime integer vanishes. The completion arguments above supply its inverse-limit prerequisites. [Stacks, Tags 0327, 032A.]

## 5. Hensel lifting in every complete local ring

In this section \((R,\mathfrak m,\kappa)\) is complete for its maximal ideal; it need not be Noetherian.

**Theorem 5.1 (simple-root Hensel lemma).** If a monic \(f\in R[T]\) has a root \(\bar a\in\kappa\) with \(f'(\bar a)\ne0\), then exactly one root \(a\in R\) reduces to \(\bar a\).
[Stacks, Tag 04GM.]

**Proof.** Start with any lift \(a_0\). Its derivative is a unit. Define

\[
a_{n+1}=a_n-f'(a_n)^{-1}f(a_n).
\tag{13}
\]

Every \(a_n\) has the same residue, so every derivative remains a unit. Polynomial expansion gives
\(f(a+h)=f(a)+f'(a)h+h^2H(a,h)\).
Induction in (13) therefore gives

\[
f(a_n)\in\mathfrak m^{2^n},\qquad
a_{n+1}-a_n\in\mathfrak m^{2^n}.
\tag{14}
\]

Completeness supplies their limit \(a\). Polynomial operations respect congruences modulo all powers of \(\mathfrak m\), so \(f(a)\) is in every such power and equals zero. If \(b\) is another root with the same residue, then
\(0=f(b)-f(a)=(b-a)(f'(a)+(b-a)H)\).
The second factor has nonzero residue and is a unit, proving \(b=a\). This argument also works for a nonmonic polynomial with the same simple-root hypothesis. \(\square\)

**Theorem 5.2 (coprime factor lifting).** If monic \(f\in R[T]\) reduces to a product of coprime monic polynomials \(\bar g\bar h\) over \(\kappa\), there are unique monic \(g,h\) of the same respective degrees and residues with \(f=gh\).

**Proof.** Let the degrees be \(r,s\). For monic lifts \(g,h\), consider the coefficient map between free \(R\)-modules of rank \(r+s\),

\[
L_{g,h}:R[T]_{<r}\oplus R[T]_{<s}\longrightarrow R[T]_{<r+s},
\qquad (U,V)\longmapsto hU+gV.
\tag{15}
\]

Its reduction is injective: if \(\bar hU=-\bar gV\), coprimality implies \(\bar g\mid U\), and the degree bound forces \(U=0\); then \(V=0\). Equal finite dimensions make it an isomorphism over \(\kappa\). Its matrix determinant is consequently a unit in \(R\), making (15) invertible over \(R\).

Choose initial monic lifts. Their error \(E=f-gh\) has degree smaller than \(r+s\) and coefficients in \(\mathfrak m\). Whenever \(E\) has coefficients in \(\mathfrak m^N\), choose \((U,V)=L_{g,h}^{-1}(E)\), whose coefficients also lie there. Replace \(g,h\) by \(g+U,h+V\). Their new error is \(-UV\), with coefficients in \(\mathfrak m^{2N}\). Iterate from \(N=1\). The finitely many coefficients converge; the limits remain monic, have the prescribed degrees and residues, and multiply to \(f\).

For uniqueness, the differences of two lifts initially have coefficients in \(\mathfrak m\). The equality of their products says
\(L_{g,h}(\delta g,\delta h)=-\delta g\,\delta h\).
Its inverse puts the differences in \(\mathfrak m^2\), then in \(\mathfrak m^4\), and so on. Separatedness makes them zero. Degree zero factors, where the corresponding coefficient module is zero, are included. \(\square\)

## 6. Two ways exactness can fail

**Infinite modules over a Noetherian ring.** Let \(R=k[t]\), \(I=(t)\), and \(E=\bigoplus_{j\geq1}R\). The map \(E\to E\) multiplying the \(j\)-th coordinate by \(t^{2j}\) is injective, with cokernel
\(\bigoplus_jR/(t^{2j})\).
The completion of \(E\) consists of families \(b_j\in k[[t]]\) tending to zero \(t\)-adically: modulo each \(t^n\) only finitely many coordinates are nonzero. This follows by identifying \(E/t^nE\) and then taking compatible coordinates.

The family \(b_j=t^{2j+1}\) is in the completed middle term and maps to zero in the completed cokernel. Its only possible preimage has every coordinate equal to \(t\), which does not tend to zero. Thus completion loses middle exactness. Tensoring with \(\widehat R\) remains exact by flatness; completion and tensoring need not agree on these infinite modules. [Stacks, Section 05JF.]

**Finite presentation over a non-Noetherian ring.** Let \(V\) be the \(k\)-vector space with basis \(u_j,v_{j,a}\) for \(j\geq1,a\geq0\). Put \(A=k[t][[s]]\) and \(M=V[[s]]\), where each coefficient is a finite linear combination of basis vectors. Define an \(A\)-module structure by

\[
t u_j=s^jv_{j,0},\qquad
t v_{j,a}=v_{j,a+1}.
\tag{16}
\]

These actions commute with \(s\). They define the action of \(A\), since at each \(s\)-degree a power series calculation uses only finitely many coefficient polynomials. Both \(A\) and \(M\) are \(s\)-adically separated and complete. The ring \(B=A\oplus M\), with multiplication
\((a,m)(b,n)=(ab,an+bm)\), is therefore complete too.

The element \(\eta=\sum_{j\geq1}s^jv_{j,0}\) lies in the closure of \(tB\): its truncation before degree \(N\) is \(t\sum_{j<N}u_j\), with remainder in \(s^NB\). But \(\eta\notin tB\). If \(t(a,m)=\eta\), then \(ta=0\) in the domain \(A\), forcing \(a=0\). In \(tm\), the coefficient of \(s^jv_{j,0}\) can only come from the coefficient of \(u_j\) in the degree-zero coefficient of \(m\). Equation (16) would require that coefficient to be one for every \(j\), impossible because that single coefficient has finite support.

Thus \(B/(t)\), although a finitely presented \(B\)-module, is not \(s\)-adically separated. Its map to its completion is not injective. Since \(\widehat B=B\), tensoring it with \(\widehat B\) does not equal completion. Finite presentation alone cannot replace the Noetherian hypothesis in Theorem 3.1.

## 7. Exercises

**Exercise 7.1 (easy).** Define \(\mathbb Z_p=\varprojlim_n\mathbb Z/p^n\mathbb Z\). Show that it is a DVR and that \(\mathbb Z\to\mathbb Z_p\) is flat. Is this map faithfully flat?

**Exercise 7.2 (medium).** Over a field of characteristic different from two, let
\(R=(k[x,y]/(y^2-x^2(1+x)))_{(x,y)}\).
Prove that \(R\) is a domain but its completion is isomorphic to \(k[[u,v]]/(uv)\).

**Exercise 7.3 (medium).** Compute the maximal-ideal completion of \(\mathbb Z[x]_{(p,x)}\).

**Exercise 7.4 (medium).** For a Noetherian local ring, deduce injectivity of \(R\to\widehat R\) and \(J\widehat R\cap R=J\) for every ideal \(J\), directly from faithful flatness.

**Exercise 7.5 (hard).** Prove that a Noetherian local ring is regular if and only if its completion is regular, by comparing the Hilbert–Samuel function and the cotangent space. Apply this to the completion of \(k[x,y,z]_{(x,y,z)}/(xy-z^2)\) in every characteristic.

**Exercise 7.6 (hard).** Complete \(R_0=k[X_1,X_2,\ldots]_{(X_1,X_2,\ldots)}\) at its maximal ideal. Describe its limit ring \(C\), show that its maximal ideal differs from the extended original ideal, and prove that \(C\) is not complete for its own maximal ideal.

## 8. Solutions

**Solution 7.1.** Localizing \(\mathbb Z\) at \((p)\) does not change \(\mathbb Z/p^n\): every integer prime to \(p\) has an inverse there. Hence \(\mathbb Z_p\) is also the completion of the DVR \(\mathbb Z_{(p)}\). Theorem 4.1 makes it regular local of dimension one, with maximal ideal generated by \(p\). Theorem 1.1 of *Regular local rings* also makes it a domain. The DVR characterization in Theorem 1.2 of *Discrete valuation rings, normal rings and Serre's criterion* now makes it a DVR. Theorem 3.2 applied to the Noetherian ring \(\mathbb Z\) gives flatness. It is not faithfully flat over \(\mathbb Z\): a prime integer \(q\ne p\) is a unit in every coordinate, so
\((\mathbb Z/q)\otimes_{\mathbb Z}\mathbb Z_p=0\)
although \(\mathbb Z/q\ne0\).

**Solution 7.2.** The rational function \(1+x\) is not a square in \(k(x)\), because its order at \(x=-1\) is one, whereas a rational square has even order. Thus \(y^2-x^2(1+x)\) is irreducible over \(k(x)\); a root would make \(1+x\) a square. Gauss factorization and monic division show that it is prime in \(k[x,y]\). Its quotient and the indicated localization are domains.

By (12) and finite-module exactness,

\[
\widehat R=k[[x,y]]/(y^2-x^2(1+x)).
\tag{17}
\]

Apply Theorem 5.1 in \(k[[x]]\) to \(G^2-(1+x)\), with residue root one and derivative two. There is \(g(x)\) with \(g(0)=1\) and \(g(x)^2=1+x\). Set

\[
u=y-xg(x),\qquad v=y+xg(x).
\tag{18}
\]

This is an invertible formal change of coordinates. To verify it, the series \(F(x)=xg(x)\) has leading coefficient one and constant term zero. Its compositional inverse is constructed coefficient by coefficient: after choosing coefficients through degree \(n-1\), the coefficient in degree \(n\) of \(F(H(T))\) contains the new coefficient of \(H\) with coefficient one, so a unique choice makes it equal to \(T\). This gives a right inverse; the same uniqueness gives a two-sided inverse. The inverse of (18) is
\(x=F^{-1}((v-u)/2)\), \(y=(u+v)/2\).
All substitutions have zero constant term and are well-defined on formal series. The equation becomes \(uv\). Neither \(u\) nor \(v\) vanishes in \(k[[u,v]]/(uv)\), as reduction modulo the other variable shows, but their product vanishes. The completed local ring is not a domain.

**Solution 7.3.** Write \(\mathfrak m=(p,x)\). The ring
\(\mathbb Z[x]/\mathfrak m^n\) is local Artinian, so denominators outside \(\mathfrak m\) are already units and localization does not change it. Its elements have representatives of degree smaller than \(n\), with the coefficient of \(x^i\) taken modulo \(p^{n-i}\). This follows from the generators \(p^{n-i}x^i\), \(0\leq i\leq n\), of \((p,x)^n\). Compatible coefficients therefore give

\[
\widehat{\mathbb Z[x]_{(p,x)}}=\mathbb Z_p[[x]].
\tag{19}
\]

Conversely every such series determines the described truncated polynomials, so this is a bijection respecting addition and multiplication. Its maximal ideal is \((p,x)\). The coefficient congruences also identify its limit topology with the \((p,x)\)-adic topology.

**Solution 7.4.** Theorem 3.2 makes \(R\to\widehat R\) faithfully flat. Theorem 2.2 of the faithful flatness lesson says that \(M\to M\otimes_R\widehat R\) is injective for every module. For \(M=R\) this gives the first assertion. For \(M=R/J\), its target is \(\widehat R/J\widehat R\); the kernel consists exactly of \((J\widehat R\cap R)/J\), giving the second assertion. No separate assumption that \(J\) is the completion ideal is involved.

**Solution 7.5.** The quotients in (9) have the same submodules and composition factors over either ring, so their lengths agree for every \(n\). Their eventual Hilbert–Samuel polynomials are identical. The dimension theorem gives equal dimensions. The degree-one graded pieces are the same vector space over the same residue field, so the embedding dimensions agree. The equality defining regularity holds for one ring exactly when it holds for the other.

For the cone, §6 of *Regular local rings* gives local dimension two at the origin in every characteristic. Its maximal ideal has three independent classes modulo its square, because \(xy-z^2\) has no linear term. Completion gives \(k[[x,y,z]]/(xy-z^2)\), by the quotient computation used in (17). Its dimension is therefore two and its embedding dimension three. Both local rings are nonregular, including in characteristic two.

**Solution 7.6.** Modulo degree \(n\), a polynomial with nonzero constant term has a finite geometric-series inverse. Thus localization does not change the quotients, and \(C\) consists of series with only finitely many nonzero monomials in each total degree. Let \(K_n\) be the series of degrees at least \(n\). It is complete and separated for this degree filtration. Proposition 2.3 makes it local with maximal ideal \(\mathfrak n=K_1\).

The series \(\sum_{j\geq1}X_j^j\) is in \(\mathfrak n\) but not in \((X_1,X_2,\ldots)C\). A member of the latter uses finitely many of these variable generators. Setting them to zero kills that member but leaves a nonzero tail of the displayed series. Hence the two ideals differ.

We next show \(K_2\ne\mathfrak n^2\). Partition variables into disjoint blocks \(B_j\) of size \(2j+1\). Choose strictly increasing integers \(e_j>1\) not divisible by the characteristic, and set

\[
z=\sum_{j\geq1}z_j,\qquad z_j=\sum_{X\in B_j}X^{e_j}.
\tag{20}
\]

This is an element of \(K_2\). Suppose \(z=\sum_{i=1}^t f_i g_i\) with \(f_i,g_i\in\mathfrak n\). Choose \(j\geq t\) and set all variables outside \(B_j\) to zero. In \(D=k[[B_j]]\) we obtain \(z_j=\sum_i F_iG_i\), with all factors in its maximal ideal. Formal differentiation gives

\[
\left(\frac{\partial z_j}{\partial X}:X\in B_j\right)
\subseteq(F_1,\ldots,F_t,G_1,\ldots,G_t).
\tag{21}
\]

The left ideal has radical the full maximal ideal, since \(e_j\) is a unit. Thus the right ideal would be primary to that maximal ideal. But \(D\) is regular local of dimension \(2j+1\), by (12) and Theorem 4.1 applied to the polynomial local ring. An ideal generated by \(2t\) elements cannot have height \(2j+1>2t\), by Theorem 3.1 of the local dimension lesson. This contradiction proves \(z\notin\mathfrak n^2\).

For the final completeness assertion, \(\mathfrak n^n\subseteq K_n\) gives short exact sequences

\[
0\longrightarrow K_n/\mathfrak n^n
\longrightarrow C/\mathfrak n^n
\longrightarrow C/K_n\longrightarrow0.
\tag{22}
\]

The left transition maps are surjective. Indeed, subtract the finite degree-\(n\) homogeneous part of an element of \(K_n\). That part is in \(\mathfrak n^n\), and the remainder is in \(K_{n+1}\). Since \(K_2/\mathfrak n^2\ne0\), compatible preimages give a nonzero element of its inverse limit. Theorem 1.2 applied to (22) therefore gives a surjection
\(\varprojlim C/\mathfrak n^n\to C\)
with nonzero kernel. Its composite with the canonical map \(C\to\varprojlim C/\mathfrak n^n\) is the identity, because \(\varprojlim C/K_n=C\). If that canonical map were an isomorphism, this kernel would be zero. It is not, so \(C\) is not \(\mathfrak n\)-adically complete. The inverse-limit topology and the maximal-ideal topology have different consequences here.

## References and proof scope

The Stacks project supplies the Mittag–Leffler, completion and Cohen locators cited above. Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, §§13.9 and 28.1, discusses Artin–Rees and completion. The inverse-system arguments, completion proofs, examples and complete solutions are supplied in this lesson; the full coefficient-ring construction is proved in the linked supplement. The sources retain their own licences.

Verified tag references: [Tag 0595](https://stacks.math.columbia.edu/algebra.html#definition-ML-system), [Tag 0598](https://stacks.math.columbia.edu/algebra.html#lemma-ML-exact-sequence), [Tag 02N1](https://stacks.math.columbia.edu/homology.html#lemma-Mittag-Leffler), [Tag 0315](https://stacks.math.columbia.edu/algebra.html#lemma-completion-generalities), [Tag 0317](https://stacks.math.columbia.edu/algebra.html#definition-complete), [Tag 00MA](https://stacks.math.columbia.edu/algebra.html#lemma-completion-tensor), [Tag 00MB](https://stacks.math.columbia.edu/algebra.html#lemma-completion-flat), [Tag 00MC](https://stacks.math.columbia.edu/algebra.html#lemma-completion-faithfully-flat), [Tag 05GH](https://stacks.math.columbia.edu/algebra.html#lemma-completion-Noetherian), [Tag 0316](https://stacks.math.columbia.edu/algebra.html#lemma-completion-Noetherian-Noetherian), [Tag 031C](https://stacks.math.columbia.edu/algebra.html#lemma-completion-complete), [Tag 04GM](https://stacks.math.columbia.edu/algebra.html#lemma-complete-henselian), [Tag 032A](https://stacks.math.columbia.edu/algebra.html#theorem-cohen-structure-theorem), [Tag 0327](https://stacks.math.columbia.edu/algebra.html#definition-cohen-ring), [Tag 05GG](https://stacks.math.columbia.edu/algebra.html#lemma-hathat-finitely-generated), [Tag 0594](https://stacks.math.columbia.edu/algebra.html#section-mittag-leffler), [Tag 05JF](https://stacks.math.columbia.edu/examples.html#section-completion-not-exact), [Tag 05JA](https://stacks.math.columbia.edu/examples.html#section-noncomplete-completion), [Tag 05JD](https://stacks.math.columbia.edu/examples.html#section-noncomplete-quotient).

**Proof dependencies.** The coefficient-ring construction and Cohen presentation discussed in §4 are proved in the following required lesson, Theorems 4.1, 5.1 and 6.1. All five assigned result groups, finite-ideal arbitrary-module completeness, both Hensel lifting forms, the two exactness counterexamples and all six exercises have proofs above. The prerequisite Artin–Rees, flatness, Hilbert–Samuel dimension, regularity, DVR and height results are used at the stated earlier-course locators.

