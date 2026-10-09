# Endoscopy and the classification of automorphic representations of classical groups: an outlook

*Draft lesson. Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Public domain (CC0).*

For \(\mathrm{SL}_2\), the characteristic polynomial does not determine
the rational conjugacy class. The determinant of a conjugating matrix
records the missing information. Over a local field this gives a finite
set for a regular semisimple stable class; over a number field the set
can be infinite. We first prove the precise count, including an explicit
global example. Restriction of representations supplies a second
comparison: a determinant twist disappears on
\(\mathrm{SL}_2\). We then prove the full global cuspidal restriction
theorem, including its irreducible constituents and complete smooth
function images.

## 1. Geometric conjugacy and rational conjugacy

Let \(F\) be any field and \(g\in\mathrm{SL}_2(F)\). Write
\[
 p_g(T)=T^2-tT+1,\qquad t=\operatorname{tr}(g).
 \tag{1.1}
\]
We call two matrices geometrically conjugate if they are conjugate
over an algebraic closure \(\overline F\). For regular semisimple
matrices this is the stable conjugacy relation used here.
Regular semisimple means that \(p_g\) is separable. In characteristic
different from two its condition is \(t^2-4\ne0\); in characteristic
two it is \(t\ne0\).

**Lemma 1.1 (the cyclic basis and the centralizer).** If \(g\)
is nonscalar, there is \(v\in F^2\) such that \(v,gv\) is a
basis. In that basis \(g\) is the companion matrix of \(p_g\),
and
\[
 E=F[g]\simeq F[T]/(p_g),\qquad
 Z_{\mathrm{GL}_2(F)}(g)=E^\times.
 \tag{1.2}
\]
The determinant of multiplication by \(z\in E\) is its algebra
norm \(N_{E/F}(z)\).

**Proof.** If every vector were an eigenvector, applying the hypothesis
to a basis \(e_1,e_2\) would give \(ge_i=a_i e_i\), and applying
it to \(e_1+e_2\) would give \(a_1=a_2\). The matrix would be
scalar. Thus the indicated \(v\) exists. The identity
\(g^2-tg+I=0\) follows by direct multiplication of a two-by-two
matrix. In the basis \(v,gv\) the two columns of \(g\) are
\((0,1)^t\) and \((-1,t)^t\). Hence its minimal polynomial has
degree two and is \(p_g\).

Identify \(F^2\) with \(E\) by sending \(1\) to \(v\).
An endomorphism commuting with \(g\) commutes with every polynomial
in \(g\); it is an \(E\)-linear endomorphism of the rank-one
module \(E\), therefore multiplication by its value at 1. It is
invertible precisely when that value is a unit. The algebra norm is
defined as the determinant of this multiplication, proving the last
assertion. \(\square\)

**Theorem 1.2 (the exact rational-class count).** Fix a nonscalar
\(g\in\mathrm{SL}_2(F)\), and use the algebra \(E\) in (1.2).
Its \(\mathrm{GL}_2(F)\)-conjugacy class is one geometric conjugacy
class intersected with \(\mathrm{SL}_2(F)\). Its ordinary
\(\mathrm{SL}_2(F)\)-conjugacy classes are in bijection with
\[
 F^\times/N_{E/F}(E^\times).
 \tag{1.3}
\]
For the class represented by \(xgx^{-1}\), the bijection assigns
\(\det x\) modulo norms. In particular, representatives can be
chosen as
\[
 g_a=d_a g d_a^{-1},\qquad d_a=\operatorname{diag}(a,1),
 \qquad a\in F^\times/N_{E/F}(E^\times).
 \tag{1.4}
\]
For regular semisimple \(g\), \(E\) is a quadratic étale algebra
and (1.3) counts ordinary classes in its stable class. No finiteness
assumption on \(F\) is part of this formula.

**Proof.** Two nonscalar matrices with the same characteristic
polynomial have the same companion matrix by Lemma 1.1, so are
conjugate over \(F\). Geometric conjugacy preserves that polynomial
and preserves the condition of being scalar. Conversely,
\(\mathrm{GL}_2(F)\)-conjugacy gives geometric
\(\mathrm{SL}_2\)-conjugacy: over \(\overline F\), multiplication
by a scalar has any prescribed determinant, since every nonzero
element has a square root. Multiply a conjugator by such a scalar
in the centralizer to make its determinant one.

Let \(g_x=xgx^{-1}\) and \(g_y=ygy^{-1}\). If
\(g_y=s g_x s^{-1}\), \(s\in\mathrm{SL}_2(F)\), then
\(y^{-1}sx\in E^\times\). Taking determinants gives
\(\det x/\det y\in N(E^\times)\). Conversely, if that ratio
is the norm of \(c\in E^\times\), set \(s=ycx^{-1}\).
It has determinant one and conjugates \(g_x\) to \(g_y\).
Thus the determinant coset is independent of the conjugator and
distinguishes exactly the ordinary classes. Every coset occurs
because \(\det d_a=a\). This proves (1.3)–(1.4).

If \(p_g\) is separable, its quotient algebra is either a quadratic
field or \(F\times F\). This is exactly the asserted étale case.
\(\square\)

The distinction between scalar and nonscalar matrices matters. A scalar
matrix has a single geometric and ordinary class. A nonscalar matrix
with repeated characteristic root is not regular semisimple. Its
centralizer algebra is \(F[\epsilon]/(\epsilon^2)\). Multiplication
by \(a+b\epsilon\), \(a\ne0\), has determinant \(a^2\), so its
geometric class splits according to
\[
 F^\times/(F^\times)^2.
 \tag{1.5}
\]
This is a geometric-conjugacy calculation for the nonsemisimple
case, rather than the regular semisimple stable-class count.

## 2. The local counts

**Corollary 2.1.** For a regular semisimple matrix, a split algebra
\(E=F\times F\) gives one ordinary class. Over \(\mathbb R\),
an elliptic class gives two; over \(\mathbb C\), every such class
gives one. Over a finite field, every regular semisimple stable class
gives one. Over every nonarchimedean local field, including positive
characteristic and residual characteristic two, a quadratic-field
centralizer gives exactly two ordinary classes.

**Proof.** The split norm is \((x,y)\mapsto xy\), which is
surjective. The complex norm over \(\mathbb R\) is
\(z\mapsto z\overline z\), whose image is
\(\mathbb R_{>0}\), giving the two signs. A quadratic étale
algebra over \(\mathbb C\) is split.

For clarity, the finite-field norm is also surjective. Every finite
subgroup \(A\) of the multiplicative group of a field is cyclic:
for each prime dividing an element order choose an element of maximal
prime-power order. Appropriate powers of the chosen elements have
those prime-power orders, and their product has order \(M\), the
product of those maximal powers. Every element of \(A\) satisfies
\(x^M=1\). A degree-\(M\) polynomial has at most \(M\) roots,
so \(|A|\le M\); the chosen product already supplies \(M\)
distinct elements. Hence it generates \(A\).

In a quadratic field extension \(\mathbb F_{q^2}/\mathbb F_q\),
the nontrivial automorphism is \(z\mapsto z^q\): its fixed field
has exactly \(q\) elements, because \(T^q-T\) has precisely
the ground-field elements as roots. The norm is \(z^{q+1}\).
A generator of the cyclic group of order \(q^2-1\) therefore
has norm of order \(q-1\), proving surjectivity.

Finally a separable quadratic field extension of a nonarchimedean
local field is cyclic of degree two. The fully proved norm-index
calculation in *Local reciprocity and norm groups*, Proposition
6.2 gives
\([F^\times:N(E^\times)]=2\). That proof uses a normal-basis
lattice, complete lifting through its unit filtration, the cyclic
Herbrand quotient and Hilbert 90; it applies to all ramification
and both characteristics. Theorem 1.2 now gives the count.
\(\square\)

For example, over \(\mathbb R\) let
\[
 g=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
 \tag{2.1}
\]
The centralizer is \(\mathbb C^\times\), all of whose determinants
are positive. The matrices \(g\) and
\(\operatorname{diag}(-1,1)g\operatorname{diag}(-1,1)^{-1}=-g\)
are geometrically conjugate but lie in the two different ordinary
classes. Choosing a negative determinant conjugator cannot be
repaired by multiplying it by an element of this real centralizer.

## 3. A global stable class with infinitely many rational classes

**Theorem 3.1.** The stable class of (2.1) in
\(\mathrm{SL}_2(\mathbb Q)\) contains countably infinitely many
ordinary classes. Its quotient (1.3) is
\[
 \mathbb Q^\times/N_{\mathbb Q(i)/\mathbb Q}\mathbb Q(i)^\times.
 \tag{3.1}
\]
For every finite set \(S\) of primes congruent to 3 modulo 4,
the matrix
\[
 a_S=\prod_{p\in S}p,\qquad
 g_S=\begin{pmatrix}0&-a_S\\a_S^{-1}&0\end{pmatrix}
 \tag{3.2}
\]
is a representative, and these matrices have pairwise distinct
ordinary classes.

**Proof.** The polynomial \(T^2+1\) is irreducible over
\(\mathbb Q\), since a rational square cannot be \(-1\), so
the centralizer is the field \(\mathbb Q(i)\). Its norms are
\(x^2+y^2\), with rational \(x,y\) not both zero.

If \(p\equiv3\pmod4\), then \(-1\) is not a square modulo
\(p\). Indeed the cyclic group \(\mathbb F_p^\times\), proved
above, has a square equal to \(-1\) exactly when its order
\(p-1\) is divisible by four. Put
\(r=\min(v_p(x),v_p(y))\), allowing the valuation of 0 to be
\(+\infty\). After division by \(p^r\), the two numbers are
integral at \(p\), with at least one a unit. Their squared sum
is a unit: otherwise reduction would make \(-1\) a square,
or make both coordinates zero. Consequently
\[
 v_p(x^2+y^2)=2r.
 \tag{3.3}
\]
Every norm has even valuation at each such prime.

There are infinitely many primes congruent to 3 modulo 4. If
\(p_1,\ldots,p_m\) were all of them, the positive integer
\(4p_1\cdots p_m-1\) is 3 modulo 4 and is divisible by none
of the listed primes. Its factorization must have a prime factor
3 modulo 4, since a product of primes 1 modulo 4 and an even
number of factors 3 modulo 4 is 1 modulo 4. This is a contradiction.
The same argument starts with the integer 3 if the list is empty.

For distinct finite subsets \(S,T\), a prime in their symmetric
difference has odd valuation in \(a_S/a_T\). Equation (3.3)
shows this quotient is not a norm. Theorem 1.2 distinguishes
the ordinary classes of \(g_S,g_T\). They all have the same
separable characteristic polynomial and hence the same stable
class. There are infinitely many, while the set of rational
matrices is countable, proving the precise cardinality.
\(\square\)

The local count of two therefore does not imply a finite global
count. The field-norm quotient in (3.1) should also be distinguished
from the idele-class norm quotient: replacing one by the other
changes the object being counted.

## 4. Restriction and determinant twists

**Proposition 4.1.** For any group representation \(\pi\) of
\(\mathrm{GL}_2(R)\), where \(R\) is a field or an adele ring,
and any character \(\chi:R^\times\to\mathbb C^\times\),
\[
 (\pi\otimes(\chi\circ\det))|_{\mathrm{SL}_2(R)}
       =\pi|_{\mathrm{SL}_2(R)}
 \tag{4.1}
\]
on the same vector space. Their irreducible subquotient sets and
multiplicities, whenever defined, are identical.

**Proof.** For \(h\in\mathrm{SL}_2(R)\), \(\chi(\det h)=\chi(1)=1\).
The two actions are equal on every vector. Their invariant subspaces,
quotient actions and all intertwiners are consequently equal.
\(\square\)

For an automorphic character \(\chi\) of
\(F^\times\backslash\mathbb A_F^\times\), the function model of
the twist is multiplication by \(\chi(\det g)\). Its restriction
to \(\mathrm{SL}_2(\mathbb A_F)\) is exactly the original function.
Left rational invariance follows from \(\chi|_{F^\times}=1\).
The twist also preserves the cuspidal constant terms: a unipotent
matrix has determinant one, so the multiplier is constant in the
unipotent integration variable. This establishes the equality of
the two automorphic restriction images. It does not by itself prove
that this image contains an irreducible cuspidal constituent.

### Global cuspidal restriction

Let \(F\) be any number field, \(\mathbb A=\mathbb A_F\),
\(G=GL_2\), and \(S=SL_2\). An actual cuspidal realization means the full finite-level complete smooth realization, with its continuous inclusion in smooth automorphic functions, supplied by Theorems 1.19 and 1.11–1.13 of [*L-functions for \(GL_n\): Godement–Jacquet and Rankin–Selberg*](LG-GLOB-04.html). Those theorems give a real determinant norm twist of an actual irreducible admissible unitary Hilbert constituent and its compatible local unitary restricted tensor factors. A determinant norm twist is one on \(S(\mathbb A)\), so we first remove it.

Write \(H=\widehat\bigotimes_v'(H_v,\xi_v)\) for that unitary Hilbert realization, \(V\) for its full adelic smooth space (smooth at infinity, fixed by some finite-place compact open subgroup), and \(V_0\) for its mixed finite core. At infinity this core is finite under the compact group, rather than invariant under every real group element.

We shall prove all the following assertions:

- \(V_0|_{S(\mathbb A)}\), interpreted as a mixed module at infinity, is an algebraic direct sum of irreducible admissible \(S\)-modules. Its Hilbert completion is a discrete orthogonal sum of actual irreducible admissible unitary representations of \(S(\mathbb A)\).
- Restriction \(R\phi=\phi|_{S(\mathbb A)}\) is nonzero on \(V\), takes its entire smooth space into square-integrable smooth cusp functions, and has a nonzero irreducible cuspidal image. On every fixed finite level it is continuous in the complete smooth topologies. Every nonzero irreducible image has its actual Hilbert and full smooth realization.
- For every smooth automorphic character \(\chi:F^\times\backslash\mathbb A^\times\to\mathbb C^\times\), \(\pi\) and \(\pi\otimes(\chi\circ\det)\) have identical abstract restriction packets and identical automorphic restriction images under the natural twisting of their actual realizations.

No automorphy of every abstract member of a restriction packet, or multiplicity formula, is asserted. The argument proves the required constituent existence as well as the image equality. A further unitary determinant norm twist makes the positive scalar action trivial when applying rapid decay: its character on the positive scalar one-parameter group is \(t^{ia}\), and \(|\det(tI)|_{\mathbb A}=t^{2[F:\mathbb Q]}\). This further twist is also one on \(S\). Thus this normalization loses none of the assertions.

### Local finite-index restriction in the unitary models

**Lemma 4.2 (the scalar extension has finite index).** If \(k\) is a completion of a number field, \(G_k=GL_2(k)\), \(S_k=SL_2(k)\), and \(Z_k=k^\times I\), then
\[
N_k=Z_kS_k=\{g:\det g\in(k^\times)^2\}
\quad\hbox{is open, normal, and of finite index in }G_k.
\tag{4.2}
\]

*Proof.* The displayed equality follows by writing \(g=z(z^{-1}g)\) if \(\det g=z^2\). Determinant identifies the quotient with \(k^\times/(k^\times)^2\). For \(k=\mathbb R\) it has order two, and for \(k=\mathbb C\) it is trivial.

For a finite extension of \(\mathbb Q_p\), write \(k^\times=\varpi^{\mathbb Z}\mathcal O^\times\). The valuation gives only two classes. Put \(e=v_k(2)\) and choose \(m>2e\). Every \(1+t\), \(t\in\mathfrak p^m\), is a square. Indeed solve \(s(2+s)=t\) in \(\mathfrak p^{m-e}\) by iteration
\[
s\longmapsto t/(2+s).
\tag{4.3}
\]
On that ball \(|2+s|=|2|\), the map preserves the ball, and its Lipschitz constant is at most \(|t|/|2|^2<1\). Iterates are Cauchy with geometrically decreasing differences, and completeness gives their fixed point. Thus \(1+\mathfrak p^m\subset(\mathcal O^\times)^2\). The quotient \(\mathcal O^\times/(1+\mathfrak p^m)\) is finite, since every residue ring \(\mathcal O/\mathfrak p^m\) is finite. This proves finite index and openness, including residue characteristic two.

The same estimate gives a continuous square root near one. Thus multiplication \(Z_k\times S_k\to N_k\) has local continuous sections: near \(I\), take the small square root \(z\) of \(\det g\) and put \(z^{-1}g\in S_k\). In particular the product of a sufficiently small scalar neighbourhood and an open neighbourhood in \(S_k\) contains a \(G_k\)-neighbourhood of \(I\). \(\square\)

**Lemma 4.3 (finite-index unitary Clifford decomposition).** Let \((\rho,\mathcal H)\) be an actual irreducible admissible unitary representation of \(G_k\), with scalar central character. Then
\[
\mathcal H|_{S_k}=\mathcal H_1\oplus\cdots\oplus\mathcal H_r
\tag{4.4}
\]
orthogonally, where each \(\mathcal H_j\) is an actual irreducible admissible unitary \(S_k\)-representation and \(r\le[G_k:N_k]\). Repeated isomorphism classes are allowed in this assertion. Its local finite core is the direct sum of the finite cores of these summands.

*Proof.* Put \(m=[G_k:N_k]\). A bounded \(G_k\)-intertwiner is scalar. It preserves a nonzero finite-dimensional compact corner, has an eigenvector there, and its closed eigenkernel is a nonzero invariant Hilbert subspace, hence all of \(\mathcal H\). At a finite place choose a nonzero compact-open fixed corner; at an infinite place use a nonzero finite packet of compact types. These exist by smooth/compact averaging, and are finite dimensional by admissibility.

If \(P\) is any orthogonal projection onto a closed \(N_k\)-invariant subspace, average its conjugates over coset representatives:
\[
\sum_{g\in G_k/N_k}\rho(g)P\rho(g)^{-1}=mc(P)I.
\tag{4.5}
\]
This sum commutes with \(G_k\), independently of the representatives, because \(P\) commutes with \(N_k\). If \(P\ne0\), positivity of the other terms gives \(P\le mc(P)I\), so \(c(P)\ge1/m\). For pairwise orthogonal nonzero such projections, summing and averaging their inequality \(\sum P\le I\) shows that their number is at most \(m\). Starting with \(I\), split a range whenever it has a nonzero proper closed invariant subspace. At most \(m-1\) splits are possible. The resulting minimal projections give at most \(m\) irreducible \(N_k\)-summands. Scalars act by the given central character on every summand, so its \(N_k\)-irreducibility is precisely \(S_k\)-irreducibility.

Here are the admissibility details. At a finite place let \(J\subset S_k\) be compact open. Choose a sufficiently small compact scalar group \(C\subset Z_k\) on which the smooth central character is one. The group \(CJ\) is compact open in \(G_k\), by the local sections in Lemma 4.2. A \(J\)-fixed vector is \(CJ\)-fixed, so its space in \(\mathcal H\), and in each summand, is finite dimensional.

At a real or complex place let \(K_G=O(2)\) or \(U(2)\), and \(K_S=SO(2)\) or \(SU(2)\). The group \(K_1=(Z_k\cap K_G)K_S\) has index two in \(K_G\) over \(\mathbb R\), and index one over \(\mathbb C\). The second assertion follows by choosing a unit-modulus square root of \(\det k\). Fix a \(K_S\)-type \(\sigma\). The scalar character fixes its extension to \(K_1\), if that extension is compatible with the intersection; incompatible types cannot occur. Inducing this finite-dimensional representation across the finite index gives a finite-dimensional \(K_G\)-representation. It contains every possible \(K_G\)-type contributing to this \(K_S\)-isotypic space. Compact complete reducibility makes its type list finite, and \(G_k\)-admissibility makes the corresponding finite \(K_G\)-packet finite dimensional. This proves \(S_k\)-admissibility without a classification of compact highest weights.

An \(S_k\)-smooth vector is \(G_k\)-smooth at a finite place by the \(CJ\) argument. At infinity \(K_S\)-finiteness implies \(K_G\)-finiteness by the same finite-index induction and scalar character. Conversely \(G_k\)-finite vectors are \(S_k\)-finite. Each summand's projection \(P_j\) preserves the \(G_k\)-core. At a finite place it commutes with the open subgroup \(N_k\); at infinity its conjugates under \(K_G\) form a finite set, since that action factors through \(G_k/N_k\). Consequently the compact orbit of \(P_jv\), for a compact-finite \(v\), lies in a finite-dimensional span of these finitely many projections applied to its finite-dimensional compact orbit. The projections commute with the full Lie algebra, which is the Lie algebra of \(Z_kS_k\). They therefore also preserve the full smooth spaces.

Finally, the finite core of each irreducible admissible unitary summand is irreducible. Here the proof of Lemma 1.9 of [*L-functions for \(GL_n\): Godement–Jacquet and Rankin–Selberg*](LG-GLOB-04.html) applies with the local \(S_k\)-compact projectors. To spell out why its hypotheses and conclusion remain valid, conjugation-average a small real smooth kernel under \(K_S\). It commutes with a finite compact packet and tends to the identity, so it is eventually invertible on that finite-dimensional packet; hence every finite vector is smooth. Compact coefficient kernels approximate all smooth vectors in every Lie-derivative seminorm. Its graph-core argument uses only invariant Haar measure and the estimate that the coefficients of left minus right differentiation vanish at the identity. Both hold for \(SL_2(k)\). Thus finite vectors are a common core for its real generators. If an algebraic finite submodule \(M\) is nonzero, project orthogonally onto its Hilbert closure. On each finite compact corner, density and finite dimensionality identify the closure's corner with \(M\)'s corner. The projection consequently preserves finite vectors and commutes with Lie generators there, by their skew-adjointness. The common-core identity extends to their closed domains, and differentiating the conjugated projection makes it commute with the one-parameter groups. At a finite place the same argument uses only compact-open averages and the full group action. The local real groups \(SL_2(\mathbb R)\) and \(SL_2(\mathbb C)\) are connected: Gram–Schmidt expresses them as upper unipotent, positive determinant-one diagonal, and \(SO(2)\) or \(SU(2)\); those compact groups are connected, with \(SU(2)\) the unit sphere in \(\mathbb R^4\). Their one-parameter groups therefore generate the full group. Irreducibility makes the closure all of the summand, and applying its finite compact corners again makes \(M\) the whole finite core. This proves the last assertion. \(\square\)

The finite-index argument just proved uses only the actual unitary local factors, which is enough for every cuspidal model under consideration. The corresponding free primary comparison is [Labesse–Langlands, *\(L\)-indistinguishability for \(SL(2)\)*, author IAS edition, §2, Lemma 2.4 and its proof, edition/PDF pages 9–10](https://publications.ias.edu/sites/default/files/l-indistinguishability-for-sl2_rpl.pdf). No local restriction or multiplicity-one statement from that source is being substituted for the argument.

### The distinguished line at almost every place

**Lemma 4.4.** If \(k\) is nonarchimedean of characteristic zero and \(\rho\) is an irreducible unramified \(GL_2(k)\)-representation, then
\[
\dim\rho^{SL_2(\mathcal O_k)}=1.
\tag{4.6}
\]
In the unitary decomposition (4.4), its \(GL_2(\mathcal O_k)\)-fixed reference vector belongs to precisely one summand. That summand has multiplicity one and a one-dimensional \(SL_2(\mathcal O_k)\)-fixed space; all other summands have zero fixed space.

*Proof.* The actual earlier proof in [*Unramified representations of \(GL_2\) and Satake parameters*, Theorem 3.2](../automorphic-forms-and-representations-of-gl2/unramified-representations-of-gl2-and-satake-parameters.html) realizes every spherical irreducible as the unique spherical irreducible constituent of a normalized principal series \(I(\mu_1,\mu_2)\) with both \(\mu_i\) unramified. Its proof uses the proved commutative spherical corner, the actual two-factor principal-series theorem, and exact compact invariants; it does not assume an unproved cuspidal-support classification. The complete irreducibility and exceptional-factor proof is *Whittaker models, Kirillov models and the local classification*, Theorem 4.2.

The \(SL_2(\mathcal O_k)\)-fixed space of this whole induced representation has dimension one. Indeed \(G_k=BK_G\), the actual Iwasawa proof in [*Lattices over a local field: the tree of \(GL_2\) and its decompositions*, Proposition 11.4](../NT-ADL/NT-ADL-11.html). Given \(s=bk\in S_k\), put \(d=\operatorname{diag}(\det k,1)\in B\cap K_G\). Then \(bd\in B\cap S_k\) and \(d^{-1}k\in K_S\). This proves \(S_k=(B\cap S_k)K_S\).

Every \(G_k\)-section is determined by its restriction to \(S_k\), since \(G_k=BS_k\). Its restricted inducing multiplier on \(\operatorname{diag}(a,a^{-1})\) is
\(|a|_k(\mu_1/\mu_2)(a)\). A right \(K_S\)-fixed section is determined by its value at one; on the compact intersection this multiplier is one, because the characters are unramified. Conversely the Iwasawa formula supplies a section of value one. Its well-definedness is precisely triviality of this compact-intersection multiplier. Hence the whole induced space has one fixed line.

Taking invariants under a compact group is exact in a smooth representation: average a lift in any surjection over normalized Haar measure; its orbit has finite image at a finite place, so this is an algebraic finite sum. Apply this to the finite composition series proved in the cited principal-series theorem. Every constituent has at most one \(K_S\)-fixed vector. Our spherical constituent has a nonzero \(K_G\)-fixed vector, hence a nonzero \(K_S\)-fixed vector, proving (4.6).

Orthogonal projections in (4.4) commute with \(K_S\). If two summands had a nonzero projection of the reference vector, they would give two independent fixed vectors, contradicting (4.6). Thus exactly one contains it. If its irreducible isomorphism class occurred twice, both copies would have that same nonzero fixed-space dimension, again contradicting (4.6). This proves the final assertions. The distinguished summand is \(K_G\)-stable: a \(K_G\)-translate is an \(S_k\)-summand containing the same fixed reference line, and that class has only one copy. Its orthogonal projection therefore commutes with \(K_G\). \(\square\)

### The global restricted tensor decomposition

Choose the local orthogonal decompositions (4.4). At almost every finite place label its distinguished summand by \(j=0\), and keep the original norm-one reference vector \(\xi_v\) there. Let \(\mathcal J\) be the choices \(\mathbf j=(j_v)\) with \(j_v=0\) at all but finitely many of these places. Include every choice at the finitely many remaining places. Put
\[
H_{\mathbf j}=\widehat{\bigotimes_v'}
(\mathcal H_{v,j_v},\xi_v),\qquad
W_{\mathbf j}=\bigotimes_v'\mathcal H_{v,j_v,\mathrm{fin}}.
\tag{4.7}
\]
Reference vectors at an exceptional chosen place can be any nonzero finite vectors; their scalar normalization affects no representation class.

**Proposition 4.5.** There are actual orthogonal and algebraic decompositions
\[
H|_{S(\mathbb A)}=\widehat{\bigoplus_{\mathbf j\in\mathcal J}}H_{\mathbf j},
\qquad
V_0|_{S}=\bigoplus_{\mathbf j\in\mathcal J}W_{\mathbf j}.
\tag{4.8}
\]
Every \(H_{\mathbf j}\) is irreducible unitary and admissible, and every \(W_{\mathbf j}\) is its simple admissible mixed finite core. The entire restriction \(H|_S\) is also admissible: every simultaneous finite-level and finite-compact-type corner is finite dimensional.

*Proof.* A pure tensor differs from the original reference tensor in finitely many factors. Decompose those finitely many factors by (4.4); Lemma 4.4 places every unchanged tail factor in its distinguished summand. This gives a finite algebraic sum of the spaces on the right of (4.8). Different choices are orthogonal, since they differ by orthogonal local summands. Their pure tensors have dense span, so completion gives the Hilbert identity. Lemma 4.3's core identity at each active place gives its algebraic identity. These subspaces are invariant under the full \(S(\mathbb A)\)-action on the Hilbert completion and under its mixed algebra on the finite core; compact tail factors fix the reference tensor.

Each restricted tensor core is simple. Here is the finite interpolation argument used to justify this assertion. For a simple admissible local core \(E\), its endomorphisms are scalars by the finite-corner eigenvector argument. If \(x_1,\ldots,x_r\) are linearly independent vectors in \(E\), the local algebra can send them to any prescribed \(r\) target vectors. Induct on \(r\), the case \(r=1\) being simplicity. The image \(M\) of \(a\mapsto(ax_1,\ldots,ax_r)\) is a submodule of \(E^r\), and projects onto \(E^{r-1}\) by induction. Its intersection with the last coordinate is a submodule of \(E\), hence zero or \(E\). If it is \(E\), surjectivity to the first coordinates gives \(M=E^r\). Otherwise the projection is an isomorphism and \(M\) is the graph of a module homomorphism \(E^{r-1}\to E\). Each of that map's coordinate restrictions is a scalar endomorphism of \(E\), so its last coordinate is a fixed scalar combination of its first coordinates. Applied to every \(a\), and then a local unit fixing all \(x_i\), this contradicts independence. This proves interpolation.

Given a nonzero finite tensor sum, apply this interpolation successively in its finitely many active factors to isolate a nonzero pure tensor. Simplicity in each factor then generates every tensor at that finite stage. Activating one further reference factor and using its simplicity generates the next stage. The union of the stages is the whole restricted tensor core, proving simplicity.

For admissibility choose a finite-place compact open group \(J\). It contains a product subgroup \(J'=\prod J'_v\), with \(J'_v=SL_2(\mathcal O_v)\) outside a finite set \(T\), because the group is a restricted product and \(J\) is open. In a given \(H_{\mathbf j}\), outside \(T\) the \(J'_v\)-fixed space is the distinguished reference line, or zero if the choice is nondistinguished. Averaging pure tensors over the compact product \(J'\) therefore leaves a finite tensor product of local fixed spaces in \(T\), with that fixed reference tail; averaging is contractive and the tensors are dense, so the same description holds in the Hilbert completion. Lemma 4.3 makes those local fixed spaces finite dimensional. A finite packet of archimedean compact types gives finite-dimensional spaces in the finitely many infinite factors. Thus a joint corner in \(H_{\mathbf j}\) is finite dimensional.

For the whole sum, a choice contributes to this corner only if it is distinguished outside \(T\). There are only finitely many remaining choices, including the finitely many infinite places. Hence the whole corner is finite dimensional too.

A nonzero closed invariant subspace of \(H_{\mathbf j}\) has a nonzero compact/level projection, by approximation to the identity. That vector lies in its finite core. Its simple mixed module therefore puts the whole dense core in the subspace, making it all of \(H_{\mathbf j}\). This proves Hilbert irreducibility. The common-core and smooth-density argument in Lemma 4.3, now with simultaneous finite-place averaging, is exactly the group-independent argument of Lemma 1.9 cited there. It identifies \(W_{\mathbf j}\) with the actual finite core and supplies its complete smooth topology. \(\square\)

This proves discrete constituent existence before using the restriction of functions. The global packet is the set of isomorphism classes represented by (4.7), with repeated copies removed. The distinguished-line condition is indispensable: it makes the algebraic sum and the finiteness of the joint corners valid even when infinitely many local restrictions split.

### A determinant-one reduction domain

**Lemma 4.6 (covering, volume and restricted rapid decay).** Put \(d=[F:\mathbb Q]\). There are compact sets \(\Omega'_N\subset N(\mathbb A)\), \(C_S\subset S(\mathbb A)\), and \(t_0>0\), such that, with \(b(t)=\operatorname{diag}(t,t^{-1})\) at every infinite place and the identity at finite places,
\[
S(\mathbb A)=S(F)\Omega'_N\{b(t):t\ge t_0\}C_S.
\tag{4.9}
\]
The quotient \(X_S=S(F)\backslash S(\mathbb A)\) has finite volume. For \(\phi\in V_0\), \(R\phi\) and every right \(S_\infty\)-derivative belong to \(L^2(X_S)\). They are smooth cusp functions and decay faster than any power of \(t\) in (4.9).

*Proof.* Use the actual general adelic reduction in Proposition 1.1a of [*L-functions for \(GL_n\): Godement–Jacquet and Rankin–Selberg*](LG-GLOB-04.html), with \(n=2\). For \(h\in S(\mathbb A)\) it gives
\[
h=\gamma n b(t)\omega,\qquad
\gamma\in GL_2(F),\quad n\in\Omega_N,\quad
\omega\in\Omega_TK,\quad t\ge t_0.
\tag{4.10}
\]
The diagonal \(b(t)\) has determinant one as an idèle, not merely norm one. The same is true of \(n\). Consequently
\(\det\gamma=(\det\omega)^{-1}\). The set \(\det(\Omega_TK)\) is compact in \(\mathbb A^\times\). Its inverse is also compact, and its inclusion in the additive adèles is continuous. It meets \(F^\times\) in a finite set: \(F\) is discrete and closed in \(\mathbb A\), as actually proved in *The adèle ring of a number field*, Theorem 2.2. A closed discrete subgroup meets a compact set finitely, since otherwise a compact accumulation point would contradict discreteness.

List the possible determinants as \(q_1,\ldots,q_a\), and put \(r_i=\operatorname{diag}(q_i,1)\in GL_2(F)\). When \(\det\gamma=q_i\), write \(\gamma'=\gamma r_i^{-1}\in S(F)\). Since \(r_i\) commutes with \(b(t)\),
\[
h=\gamma'(r_i n r_i^{-1})b(t)(r_i\omega).
\tag{4.11}
\]
The finite union of the first parenthesized compact sets is \(\Omega'_N\). The finite union of \((r_i\Omega_TK)\cap S(\mathbb A)\) is a compact set \(C_S\), since \(S(\mathbb A)\) is closed. This proves (4.9). It uses no finite-intersection assertion for an entire Siegel set.

Here are the measure details. The group \(S(\mathbb A)\) is unimodular. On its local Lie algebra the determinant of conjugation is one: on \(M_2(k)\) the determinant is \((\det g)^2(\det g^{-1})^2=1\), and its scalar line is fixed, so the determinant on trace-zero matrices is one. At a finite place the same linear change of coordinates on a small matrix chart proves preservation of Haar density. Thus quotient right translation is unitary.

The local determinant-one Iwasawa decomposition proved in Lemma 4.4, and its real/complex Gram–Schmidt counterpart, give \(S(\mathbb A)=N(\mathbb A)T_S(\mathbb A)K_S\). A compact subset has Iwasawa torus coordinates in a compact subset: at infinity this follows from the explicit positive row norms in Gram–Schmidt, bounded above and away from zero on a compact invertible set; at a finite place finitely many bounded valuations suffice, and the remaining unit entries range over compact unit groups. Only finitely many finite places differ from the integral compact group. The unipotent coordinates can also be chosen in a compact set, by the same row operations. Write a torus coordinate as \(\operatorname{diag}(a,a^{-1})\). If its idèle norm is \(r\), extract the positive common-infinite scalar \(r^{1/d}\); its remaining idèle has norm one. Applied to the compact set \(C_S\), this leaves a compact set \(D_T\) of norm-one torus coordinates, and only a bounded positive change of \(t\).

After this Iwasawa decomposition of the compact right factor in (4.9), an element has the form \(n'b(t)n_C t_Ck\). Move \(n_C\) to the left through \(b(t)\). Reduce the resulting upper entry modulo \(F\) by a rational upper unipotent, using a compact set \(D_N\) of representatives for \(\mathbb A/F\), again Theorem 2.2 just cited. This gives a cover of \(X_S\) by
\[
D_N\{b(t):t\ge t_1\}D_TK_S,\qquad t_1>0.
\tag{4.12}
\]
The conjugation modulus on its single upper root line is
\(\delta_S(\operatorname{diag}(a,a^{-1}))=|a|_{\mathbb A}^{2}\). Changing that additive coordinate in left Haar measure gives the Iwasawa density \(\delta_S^{-1}\,du\,d^\times a\,dk\). The decomposition of \(a\) into its norm and norm-one part disintegrates multiplicative Haar measure into a constant times \(dt/t\) and Haar measure on the norm-one part: it is the group isomorphism \(a\mapsto(t,a/t)\), with \(t=|a|_{\mathbb A}^{1/d}\). Enlarge \(D_T\) to a compact neighbourhood in that part if necessary. Thus the integral over (4.12) is bounded by a constant times
\[
\int_{t_1}^{\infty}t^{-2d}\frac{dt}{t}<\infty.
\tag{4.13}
\]
This also bounds quotient volume: partition countably many injective quotient charts into disjoint measurable pieces and integrate there; the covering integral overcounts each piece. Such charts exist by discreteness of \(S(F)\), inherited from the matrix-entry embedding in \(\mathbb A^4\). This establishes the bound without requiring bounded covering multiplicity.

Finally, \(b(t)^{-1}\Omega'_Nb(t)\) is compact as \(t\ge t_0\): its upper entry is multiplied by \(t^{-2}\) at all infinite places and unchanged at finite places. A representative in (4.9) therefore has the form \(b(t)\omega'\), with \(\omega'\) in a fixed compact subset of \(GL_2(\mathbb A)^1\). Lemma 1.1b of the same \(L\)-function lesson gives, for every \(M\) and every right differential operator \(D\),
\[
|R(D)\phi(b(t)\omega')|\le C_{D,M}t^{-2dM}.
\tag{4.14}
\]
Its proof allows precisely this compact enlargement: the compact smoothing kernel and its derivatives have fixed support; the Fourier-Schwartz estimates there are uniform for the right factor in any fixed compact set. All other estimates use only the lower root-ratio bound. Its quantity \(\beta(b)\) is \(t^{2d}\) in rank two. Rational \(S\)-automorphy lets us apply (4.14) to (4.9). The integral bound (4.13) then puts every derivative in \(L^2(X_S)\).

The restriction is \(S(F)\)-invariant and smooth. Its upper-unipotent cusp integral is exactly the original \(GL_2\) constant term, since their upper-unipotent groups coincide:
\[
\int_{F\backslash\mathbb A}\phi(n(x)s)\,dx=0.
\tag{4.15}
\]
This is the only proper standard parabolic of \(SL_2\); its rational conjugates give the other parabolics by left rational automorphy. Moderate growth and all its differentiated versions restrict from the given \(GL_2\) model. This proves the lemma. \(\square\)

### Turning algebraic images into actual cusp constituents

**Lemma 4.7 (nonzero images have complete unitary realizations).** For a summand \(W_{\mathbf j}\) of (4.8), either \(R|_{W_{\mathbf j}}=0\), or restriction is injective and there is a number \(c_{\mathbf j}>0\) such that
\[
\langle Rw,Rw'\rangle_{L^2(X_S)}
=c_{\mathbf j}\langle w,w'\rangle_H
\quad(w,w'\in W_{\mathbf j}).
\tag{4.16}
\]
In the second case it extends to a bounded scaled isometry from \(H_{\mathbf j}\) onto a closed irreducible admissible Hilbert cusp subrepresentation of \(L^2(X_S)\). On its entire finite-level smooth space this extension agrees with pointwise restriction and gives its complete smooth cusp realization.

*Proof.* Restriction intertwines finite-place group actions, compact operations and right Lie differentiation. Its algebraic kernel is a submodule of the simple \(W_{\mathbf j}\). If it is nonzero, it is the whole module. Otherwise the form on the left of (4.16) is positive definite, by Lemma 4.6 and injectivity.

The core images satisfy the usual infinitesimal finiteness required of automorphic forms. At each infinite place the complexified Lie algebra is the direct sum of the \(SL_2\) Lie algebra and its scalar centre. Thus \(Z(U(\mathfrak s))\) embeds in \(Z(U(\mathfrak g))\): it commutes with both summands. The original irreducible core's infinitesimal character restricts to this subalgebra. Together with the finite level, compact finiteness and moderate growth already verified, this makes the images actual cuspidal automorphic modules, rather than merely smooth functions in an invariant \(L^2\)-subspace.

We first justify the invariant adjoints in this form. All right derivatives of \(Rw\) are square integrable by (4.14). For a right Lie generator \(X\), the ordinary fundamental theorem of calculus gives
\[
Rw(s\exp(tX))-Rw(s)=
\int_0^t R(X)Rw(s\exp(rX))\,dr.
\tag{4.17}
\]
The equality holds also in \(L^2\), by Minkowski's inequality and unitarity of right translation. Strong continuity of translation makes its difference quotient converge to \(R(X)Rw\). Iterating over words in the Lie algebra proves that \(Rw\) is a Hilbert smooth vector with the stated derivatives. Hence its Lie adjoint is \(X^*=-X\). Compact and finite-place adjoints follow from Haar invariance and averaging. This avoids an integration-by-parts assumption at the cusp.

For completeness, any two invariant positive Hermitian forms \(h_1,h_2\) on a simple admissible mixed module with self-adjoint finite local units are proportional. If a local unit \(e\) fixes \(w\), invariance gives \(h_2(w,z)=h_2(w,ez)\). Riesz representation on the finite-dimensional \(eW\), for \(h_1\), gives a unique \(Tw\in eW\) with \(h_2(w,z)=h_1(Tw,z)\) for every \(z\). The definitions from larger local units agree because \(h_1\) separates vectors. Invariance makes \(T\) commute with the mixed algebra. Its restriction to a nonzero finite corner has an eigenvector, whose eigenkernel in \(W\) is a nonzero submodule. Simplicity makes this kernel all of \(W\), so \(T=cI\); positivity makes \(c>0\). This is also the finite-corner mechanism proved in Lemma 1.12 of [*L-functions for \(GL_n\): Godement–Jacquet and Rankin–Selberg*](LG-GLOB-04.html). Applying it here proves (4.16).

Complete (4.16) to obtain a bounded scaled isometry \(R_{\mathbf j}:H_{\mathbf j}\to L^2(X_S)\) with closed range. It intertwines the full \(S\)-action. At finite places this follows on the dense group-invariant finite core and then by continuity. At infinity it follows from the generator-core statement in Proposition 4.5: (4.17) identifies the target generator on core images, and closedness extends the intertwining identity from the common source generator core to its whole domain. Differentiating
\(\exp(-tB_X)R_{\mathbf j}\exp(tA_X)\) on that domain then makes it constant. The resulting intertwining of one-parameter groups gives the full connected real and complex \(SL_2\)-groups.

Its range is cuspidal. Define its weak constant term by pairing \(\int_{F\backslash\mathbb A}f(n(x)g)\,dx\) with each compact smooth test function of \(g\) on \(S(\mathbb A)\). This is a continuous \(L^2\)-distribution. Indeed choose compact additive quotient representatives; their product with the test support is compact in \(S(\mathbb A)\). A compact subset has bounded overlap with injective rational quotient charts, since only finitely many \(\gamma\in S(F)\) meet its compact product with its inverse. Cauchy–Schwarz in \(g\), followed by the finite measure of the additive quotient, bounds the pairing by a constant times \(\|f\|_2\). Equation (4.15) kills every such pairing on core images, hence on their closure. For smooth representatives the compact unipotent average is smooth, and zero as a distribution implies zero pointwise. Thus this defines a closed Hilbert cusp subspace with the required usual smooth cusp functions. The closed range is irreducible and admissible by Proposition 4.5 and its isometry with \(H_{\mathbf j}\).

We still must identify its full smooth functions with pointwise restriction. A bounded group intertwiner preserves the entire smooth space and all its derivative seminorms. A finite-level Hilbert smooth vector on \(X_S\) has a unique smooth representative, continuously in every compact smooth seminorm. Here is the local argument, also the argument of Lemma 1.10 in the cited \(L\)-function lesson. Around any given quotient point choose a small real coordinate box and a small finite open fibre on which the rational quotient map is injective. On any compact collection of such charts there is a common finite subdivision and a fixed positive lower Haar-density bound. Group Lie derivatives are weak coordinate derivatives, by differentiating translation against compact tests. Mollify in the real coordinates. Applying the fundamental theorem of calculus once in every coordinate to a cut-off function bounds its value by the \(L^2\)-norms of finitely many derivatives on the box, by Cauchy–Schwarz. Apply the same bound to every derivative on a smaller box. The mollifications are then Cauchy in every compact smooth seminorm; their limit is the unique smooth representative. These estimates give the claimed continuity. The finite fibre has positive Haar volume and supplies the same bound when there are no real coordinates.

Approximate a source finite-level smooth vector by its finite core in all derivative seminorms, as proved in Proposition 4.5. This approximation also converges in the original \(GL_2\) smooth realization whenever the source level is a \(GL_2\) level: its Lie algebra is the direct sum of the \(SL_2\) Lie algebra and the scalar Lie algebra, and the latter acts by a fixed smooth scalar character. Thus the derivative topologies agree. The source's continuous automorphic inclusion and the target compact Sobolev estimates show that both restrictions converge uniformly with every derivative on compact subsets of \(S(\mathbb A)\). They agree on the core, so their limits agree.

Every \(S\)-finite-level vector in this summand is indeed an original \(GL_2\)-finite-level vector. Outside a finite set its \(S(\mathcal O_v)\)-fixed factor is the distinguished reference line, fixed by \(GL_2(\mathcal O_v)\). At the finitely many active places use \(C_vJ_v\) from Lemma 4.3, taking \(C_v\) in the kernel of the scalar character. At infinity scalar derivatives again add no smoothness condition. This verifies the level assertion just used, without assuming that compact convolution preserves an arbitrary algebraic mixed submodule.

Consequently the image's full smooth space consists of the pointwise restricted functions. It is complete in the usual Hilbert derivative Fréchet topology at every finite level, is continuously included in smooth automorphic functions, and is cuspidal by (4.15) and compact convergence. Its growth and differentiated growth are inherited from the original model. These are the required actual smooth cusp models. \(\square\)

**Proposition 4.8 (the full restriction image).** Pointwise restriction takes all of \(V\) into smooth square-integrable cusp functions. It is continuous at each fixed finite level, in Hilbert derivative seminorms and in compact smooth seminorms. Its image contains a nonzero actual irreducible admissible cuspidal \(SL_2(\mathbb A)\)-representation. At any fixed \(SL_2\) finite level, that image is the full smooth space of a closed finite sum of these Hilbert constituents.

*Proof.* At a fixed compact-open finite-place \(SL_2\) level \(J\), the proof of Proposition 4.5 shows that only finitely many choices \(\mathbf j\) have \(H_{\mathbf j}^J\ne0\): choose a product subgroup inside \(J\), and all tail choices must be distinguished. Write these finitely many indices as \(I_J\). The orthogonal projections \(P_{\mathbf j}\) commute with \(S\), with \(J\), and with all its Lie derivatives. Hence a \(J\)-fixed smooth vector decomposes as the finite sum
\[
v=\sum_{\mathbf j\in I_J}P_{\mathbf j}v.
\tag{4.18}
\]
Each summand belongs to the original \(GL_2\) full smooth space by the level and Lie-algebra argument at the end of Lemma 4.7. Conversely the original \(GL_2\) smooth space is \(S\)-finite-level and \(S_\infty\)-smooth. Therefore these two full adelic smooth spaces are equal as vector spaces. The respective derivative topologies agree after passing to an appropriate finite \(GL_2\) level; the necessary level may depend on \(J\), and this claim does not assert an equality of the two groups' compact-open subgroups.

For every summand put \(c_{\mathbf j}=0\) if its restriction is zero, and use (4.16) otherwise. Pointwise restriction of (4.18) equals the finite sum of the maps in Lemma 4.7. In particular,
\[
\|Rv\|_2\le
\sum_{\mathbf j\in I_J}\sqrt{c_{\mathbf j}}\,
\|P_{\mathbf j}v\|_H
\le C_J\|v\|_H .
\tag{4.19}
\]
The same inequality after every \(S\)-Lie word proves finite-level smooth continuity. Compact smooth continuity follows from the target chart estimate in Lemma 4.7. It also proves square-integrability, smoothness and cuspidality for all \(v\in V\), without a uniform bound on \(c_{\mathbf j}\) over the whole unrestricted Hilbert sum.

To check that the finite sum of image constituents is closed, inequivalent image constituents are orthogonal. Indeed the projection of one closed invariant irreducible image to another is a bounded intertwiner; it is zero unless they are equivalent. A nonzero bounded intertwiner is a scalar multiple of a unitary equivalence: its adjoint product is scalar by the finite-corner Schur argument, and its closed invariant range is the entire irreducible target. For finitely many equivalent images identify their source Hilbert copies with one model. The Gram operator of their finite sum map is then a finite scalar positive matrix tensored with the identity of that model. Diagonalize this finite matrix; its positive eigenvalues have a positive minimum, so the map is bounded below on its kernel's orthogonal complement and has closed range. Doing this in each of the finitely many equivalence classes proves the closed finite-sum assertion. The resulting inverse on the kernel's orthogonal complement is bounded and intertwines \(S\), hence preserves full smooth vectors. Averaging by \(J\) shows that every \(J\)-fixed vector in the range has a \(J\)-fixed preimage. Thus the image at that level is exactly the full smooth space of the closed finite sum, rather than only a dense algebraic image.

Finally \(R\ne0\). A nonzero actual cusp function \(\phi\in V\) has \(\phi(g_0)\ne0\) at some \(g_0\). Its full right translate is in \(V\) and has nonzero value at the identity of \(S\). Compact-finite approximations at its finite level converge in the full smooth topology, and evaluation at one is continuous in the supplied automorphic realization. Thus some vector of \(V_0\) already has nonzero restriction. Its finite decomposition (4.8) contains a \(W_{\mathbf j}\) with nonzero restriction. Lemma 4.7 supplies its injective cusp image and closed irreducible admissible Hilbert completion. This proves the required cuspidal constituent existence. \(\square\)

### Twists and the intrinsic automorphic image

**Lemma 4.9 (twisting the full actual realization).** For a smooth automorphic idèle character \(\chi\), multiplication
\[
(T_\chi\phi)(g)=\chi(\det g)\phi(g)
\tag{4.20}
\]
is an invertible map of actual full smooth cusp models. It realizes the determinant twist and obeys
\[
T_\chi\pi(s)=\pi_\chi(s)T_\chi,\qquad
R_\chi T_\chi=R,\qquad s\in S(\mathbb A).
\tag{4.21}
\]
Its finite cores and all complete smooth constituent images are identified.

*Proof.* The multiplier is left \(G(F)\)-invariant and trivial on the upper unipotent group. Thus it preserves automorphy and zero constant terms. Right translation satisfies
\(R(g)T_\chi=\chi(\det g)T_\chi R(g)\), giving the twisted group action. The inverse multiplier is \(T_{\chi^{-1}}\).

The multiplier and its inverse have moderate growth. Indeed the norm-one idèle class group is compact by the actual proof in *Idèles and the idèle class group*, Theorem 3.3. Its image under \(|\chi|\) is a compact subgroup of the positive real numbers, hence one: any element other than one has unbounded positive or negative integer powers. Therefore \(|\chi(a)|\) factors through the idèle norm. After taking logarithms, it is a continuous additive function on \(\mathbb R\); rational approximation makes it \(r\log|a|_{\mathbb A}\) for some real \(r\). Thus \(|\chi(a)|=|a|_{\mathbb A}^{r}\). A fixed power of \(|\det g|_{\mathbb A}^{\pm1}\) is bounded by a power of the matrix-and-inverse height, by the determinant expansion at infinity and the ultrametric determinant bound at finite places. Differentiating a smooth character only multiplies it by constants, so the same assertion holds after every derivative.

At finite places the smooth character has a compact-open kernel, and intersects a given finite level in another finite level. At infinity its restriction to the compact group is a one-dimensional compact representation. Tensoring a finite packet of compact types with that character leaves a finite packet. Lie differentiation is changed by fixed scalar constants on the centre and is unchanged on the \(SL_2\) Lie algebra. These observations prove continuity and invertibility in all fixed-level full smooth topologies, after the indicated finite-level refinement, and preservation of the finite cores and infinitesimal finiteness. Theorem 1.19's norm normalization again supplies a unitary actual model if \(\chi\) is nonunitary.

Finally \(\det s=1\) gives both equalities (4.21) on the entire smooth space. They identify the kernels, algebraic irreducible images, and their Hilbert/full smooth models constructed in Lemma 4.7 and Proposition 4.8. This proves substantially more than a pointwise identity on one cusp function. \(\square\)

The natural actual twisted model is enough for equality in (4.21). The following additional lemma verifies that an arbitrary actual cuspidal realization of the same abstract representation has the same function image. Its proof uses the local uniqueness now actually proved for the cuspidal local models, and does not assume a global multiplicity theorem.

**Lemma 4.10 (weak multiplicity for actual \(GL_2\) cusp embeddings).** Two actual full smooth cuspidal embeddings of the same irreducible admissible \(GL_2(\mathbb A)\)-module have images differing only by a nonzero scalar. In particular their restriction images in the space of functions on \(X_S\) are identical.

*Proof.* Remove their common determinant norm normalization. The two positive invariant Hilbert forms on their identified mixed core are proportional by the finite-corner Riesz argument in Lemma 4.7. Complete that scalar-adjusted isometry. It intertwines full real group actions by the common generator cores of Lemma 1.9, finite group actions by density, and compact components on the core. It therefore identifies their full smooth spaces and derivative topologies. Denote the resulting two continuous function embeddings by \(I,J\) on one space \(V\).

Fix a nontrivial unitary additive character \(\psi:F\backslash\mathbb A\to\mathbb C^\times\), and define continuous global Whittaker functionals
\[
\lambda_I(v)=\int_{F\backslash\mathbb A}I(v)(n(x))\psi(-x)\,dx,
\qquad \lambda_J(v)=\int_{F\backslash\mathbb A}J(v)(n(x))\psi(-x)\,dx.
\tag{4.22}
\]
Continuity at fixed level follows from compactness of the additive quotient and the given compact-smooth continuity of each embedding. At every finite place local Whittaker uniqueness is the full actual proof of Theorem 2.0 in [*L-functions for \(GL_n\): Godement–Jacquet and Rankin–Selberg*](LG-GLOB-04.html). At every infinite place Theorem 2.0v of the same lesson proves uniqueness on the actual unitary full smooth cusp factors of Theorems 1.19 and 1.11–1.13, with their irreducible admissible compact-type cores. It applies also before restoring the determinant twist. Its hypothesis is the actual cusp model, so no uniqueness assertion for an arbitrary nonunitary globalization is used here.

Here are the tensor and continuity steps needed to apply these local bounds. Fix a finite set of active places containing all infinite places, and fix the reference factors at all other places. The map from a local smooth factor with all others fixed into \(V\) is continuous: under the actual Hilbert tensor isometry its derivative seminorms are the local derivative seminorms times the fixed other factors' finite norms. The full tensor identification is the actual proof of Theorem 1.13 in the cited lesson. Thus currying either functional in an infinite factor gives a continuous local Whittaker functional; currying in a finite factor gives a linear functional on its smooth module. The action of the local upper unipotent is through its local character, by translating the compact global integral. A local Hom space of dimension at most one therefore makes such a finite tensor-stage functional a scalar multiple of the product of fixed local Whittaker functionals. This last tensor assertion is elementary: in one factor evaluate at a vector on which the chosen functional is one; every slice is then that functional times the evaluation on that vector, and proceed through the finitely many factors. It uses no completion of an infinite algebraic tensor dual.

The global genericity proof in [*Automorphic representations and automorphic \(L\)-functions*, Theorem 1.3](LG-GLOB-03.html) shows that \(\lambda_I\) is nonzero on some full smooth right translate of a nonzero cusp vector. Finite-core approximation and its continuity make it nonzero on the mixed core, and expansion of a finite tensor sum makes it nonzero on a pure tensor \(x_0\). Every finite tensor stage containing \(x_0\) therefore has nonzero \(\lambda_I\). On such a stage both functionals are in the at-most-one-dimensional product functional space, so
\(\lambda_J=c_T\lambda_I\) there. Evaluation at \(x_0\) makes all \(c_T\) the same scalar \(c\). The stages exhaust the mixed core, and its density in the fixed-level smooth spaces gives \(\lambda_J=c\lambda_I\) on all of \(V\).

Apply this equality to every full smooth right translate of \(v\). The two global Whittaker transforms satisfy
\[
W_{J(v)}(g)=c\,W_{I(v)}(g)\quad(g\in G(\mathbb A)).
\tag{4.23}
\]
The same actual global genericity theorem says that a nonzero smooth cusp function has a nonzero Whittaker transform somewhere; equivalently that transform is injective on cusp functions. Apply it to \(J(v)-cI(v)\), which is again a smooth cusp function. It follows that \(J(v)=cI(v)\) for every \(v\). The scalar cannot be zero because \(J\) is an embedding. This proves the assertion. \(\square\)

**Theorem 4.11 (global cuspidal restriction and determinant twists).** For every number field \(F\) and every actual irreducible admissible cuspidal automorphic \(GL_2(\mathbb A_F)\)-representation:

1. Its \(SL_2(\mathbb A_F)\) mixed restriction is a discrete algebraic sum of irreducible admissible modules, with the actual orthogonal unitary completions in (4.8), after a determinant norm normalization.
2. Pointwise restriction on its entire actual smooth realization is a nonzero map into square-integrable smooth cusp functions. Its image contains at least one irreducible admissible cuspidal \(SL_2(\mathbb A_F)\)-representation. Every nonzero irreducible constituent image has the complete actual Hilbert and smooth realization in Lemma 4.7; the finite-level image statement is Proposition 4.8.
3. For every smooth automorphic idèle character \(\chi\), the representations \(\pi\) and \(\pi\otimes(\chi\circ\det)\) have the same abstract restriction packet, and the same automorphic restriction image as a subspace of cusp functions on \(SL_2(F)\backslash SL_2(\mathbb A_F)\). This holds in any actual cuspidal realizations of these representations.

*Proof.* Lemmas 4.2–4.4 and Proposition 4.5 prove statement 1, including the distinguished unramified lines, admissibility and core irreducibility. Lemmas 4.6–4.7 and Proposition 4.8 prove statement 2, including nonzero restriction, \(L^2\), closed irreducible constituent extraction and full smooth comparison. Lemma 4.9 identifies the full restricted \(S\)-module, its packet, and its function image under the natural twist. Lemma 4.10 makes the latter independent of the chosen actual embedding. Restoring either real or imaginary determinant norm twists changes none of these \(S\)-actions or restricted functions. This proves statement 3 and the theorem. \(\square\)

The packet here is the set of irreducible classes in the restriction. The theorem does not identify it with a conjecturally parametrized packet, assert that every abstract class is automorphic, or compute its automorphic multiplicity. None of those additional assertions is needed for the full restriction and twist invariance just proved.

The only external mathematical reference for comparison in this fragment is [Jean-Pierre Labesse and Robert P. Langlands, *\(L\)-indistinguishability for \(SL(2)\)*, the freely accessible author IAS edition](https://publications.ias.edu/sites/default/files/l-indistinguishability-for-sl2_rpl.pdf): §1, edition/PDF page 2, for the global finite-change packet convention; §2, Lemma 2.4 and its proof, edition/PDF pages 9–10, for local finite-index restriction. All proof dependencies beyond those locally written have the actual earlier programme proof locators given above.

## 5. Exercises

**Exercise 5.1 (easy).** Show that
\(\operatorname{diag}(a,a^{-1})\) and
\(\operatorname{diag}(a^{-1},a)\), \(a\in F^\times\), are
conjugate in \(\mathrm{SL}_2(F)\).

**Solution.** The matrix
\(w=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\)
has determinant one and interchanges the two diagonal entries by
conjugation. This works in characteristic two as well. For
\(a\ne a^{-1}\), the centralizer is split and Corollary 2.1
also predicts a single ordinary class. If \(a=a^{-1}\), the
matrix is scalar, so the assertion is immediate. \(\square\)

**Exercise 5.2 (medium).** Count the ordinary classes in a regular
elliptic stable class over a nonarchimedean local field and over
\(\mathbb R\). Explain what changes over \(\mathbb Q\) in example
(2.1).

**Solution.** An elliptic centralizer here is a quadratic field.
Corollary 2.1 gives two classes over either local field, with
representatives indexed by the two norm cosets. Over \(\mathbb R\)
these cosets are the two signs. Over \(\mathbb Q\), Theorem 3.1
gives infinitely many cosets, detected by the independent valuation
parities at primes 3 modulo 4. Thus the global answer is not two
and is not necessarily finite. \(\square\)

**Exercise 5.3 (medium).** Explain why restriction identifies a
representation and any determinant twist. Does the character need
to be quadratic?

**Solution.** Equation (4.1) is equality of actions because the
determinant of every acting matrix is 1. No order condition on
\(\chi\) is needed. In an automorphic function model the multiplier
equals one on the subgroup as well, so the restriction images
coincide. Neither equality alone establishes constituent existence;
that further assertion is proved in Theorem 4.11 using Lemmas 4.2–4.7
and Proposition 4.8.
\(\square\)

**Exercise 5.4 (hard).** Why does restriction of the complete smooth
cuspidal model in Theorem 4.11 have an \(L^2\) bound at each fixed
\(SL_2\) finite level even though no bound uniform over all its
Hilbert constituents was asserted? Explain the role of the unique
unramified fixed line.

**Solution.** Lemma 4.4 puts the original unramified reference vector
in exactly one local summand, whose \(SL_2(\mathcal O_v)\)-fixed
space is one dimensional. Every other summand has no such fixed
vector. A fixed global compact open level contains the full integral
groups outside a finite set. Proposition 4.5 therefore leaves only
finitely many global choices with nonzero fixed vectors. For these
choices Lemma 4.7 gives constants \(c_{\mathbf j}>0\) for their
nonzero restriction maps. Cauchy–Schwarz bounds the sum of these
maps by \((\sum c_{\mathbf j})^{1/2}\) times the source Hilbert
norm. Apply the same inequality to every Lie derivative to obtain
the complete smooth bound in Proposition 4.8. No bound on constants
for choices outside that fixed level is needed. \(\square\)

## 6. Remaining constructions

Theorem 4.11 proves global cuspidal constituent existence under
restriction to \(\mathrm{SL}_2(\mathbb A_F)\), the actual Hilbert
and full smooth comparisons, and determinant-twist invariance in
every actual cusp realization. Its restriction packet is the set of
irreducible classes in the restricted module. Identifying that set with
a parametrized packet, deciding automorphy of every abstract member,
and computing automorphic multiplicities remain separate constructions.

The endoscopic transfer identities, fundamental lemma, stable trace
formula, global packet multiplicity formulas and Arthur's discrete
classification for quasi-split symplectic and orthogonal groups
remain to be constructed. The Niemeier-lattice parameter example
and the full Saito–Kurokawa exercise also require those exact
parameter and representation comparisons. None of these assertions
is used as a premise of the conjugacy and twist proofs above.

## References

- J.-P. Labesse and R. P. Langlands, [*L-indistinguishability for
  SL(2)*, freely accessible IAS author edition](https://publications.ias.edu/sites/default/files/l-indistinguishability-for-sl2_rpl.pdf),
  §1 and the opening of §2, printed/PDF pages 1–3, for the distinction
  between rational and stable conjugacy and the local norm quotient.
- *Local reciprocity and norm groups*, Proposition 6.2,
  for the preceding fully proved local norm index in all characteristics.
