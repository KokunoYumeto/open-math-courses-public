# Hilbert and ring class fields, and quadratic prime forms

*Written by OpenAI GPT-6.1 Sol in Codex, Ultra effort, October 2026. Self-checked by the writing AI; no independent review is claimed. Public domain (CC0).*

**Lesson 19.** A prime ideal is principal exactly when it splits in the Hilbert class field. For an imaginary quadratic order, the ring class field gives the corresponding test for a prime represented by a norm form. We construct these fields from the ray class correspondence, prove principalization, and identify the fields needed for the forms \(x^2+5y^2\), \(x^2+14y^2\) and \(x^2+27y^2\).

The class field input is [Ray class fields, conductors and ideal reciprocity](ray-class-fields-conductors-and-ideal-reciprocity.md). The arithmetic of quadratic ideal classes and orders is supplied by [Quadratic fields: ideal classes and binary quadratic forms](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#NT-ANT-10), Theorems 10.1–10.2 and Proposition 10.3, and [Orders in number fields and their Picard groups](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#NT-ANT-11), Theorems 11.3–11.4 and Corollary 11.5. Section 4 below also proves the needed reduction, extension–contraction and class-number calculations in full, so the explicit examples have a direct proof path here. We do not need complex multiplication or a generation theorem using modular functions.


**Prerequisite proof availability.** The named results below identify specific programme lessons. The [prerequisite record](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#lesson-19) shows which results are proved in published lessons and which full proofs are still missing. A record or external reference is not a supplied proof; arguments using an unavailable prerequisite retain that dependency.

## 1. The ordinary and narrow Hilbert class fields

**Theorem 19.1.** A number field \(K\) has a unique maximal finite abelian extension \(H/K\) unramified at every place, including the real places, and
\[
H=K_{(1)},\qquad
\operatorname{Gal}(H/K)\simeq\operatorname{Cl}_K.
\tag{1}
\]
A finite prime splits completely in \(H\) exactly when its ideal is principal. The **narrow Hilbert class field** \(H^+\) is maximal among abelian extensions unramified at the finite places, and
\[
\operatorname{Gal}(H^+/K)\simeq\operatorname{Cl}_K^+.
\tag{2}
\]
It is the ray field whose finite modulus is \((1)\) and whose real modulus includes all real places. Its real places may become complex.

**Proof.** Theorem 18.4 constructs both fields. Proposition 18.3 says that absence of ramification at all places is equivalent to conductor \((1)\), so every such abelian extension lies in \(K_{(1)}\). Equation (4) of lesson 18 identifies this ray group with the ordinary ideal class group. In its ideal Artin map, the class of a prime is its Frobenius; triviality of that class is precisely complete splitting.

Selecting every real place permits the sign quotient, while imposing full unit groups at every finite place forbids finite ramification. The same conductor criterion gives maximality of this field, and the positivity condition on principal generators identifies its ray group with the narrow class group. \(\square\)

These fields are equal for imaginary number fields. In a real quadratic field, Proposition 10.3 of the quadratic-fields lesson gives \([H^+:H]=1\) when there is a unit of norm \(-1\), and \([H^+:H]=2\) otherwise. This statement about the two full class groups does not, by itself, give their quotients by squares; genus theory will require a separate argument.

## 2. Transfer and the principal ideal theorem

For a finite-index subgroup \(V\subset G\), choose representatives \(r\) of left cosets \(G/V\). If \(gr=r'h_r\), with \(h_r\in V\), the **transfer** is
\[
\operatorname{Ver}:G^{\mathrm{ab}}\longrightarrow V^{\mathrm{ab}},
\qquad g\longmapsto\prod_r h_r\pmod{[V,V]}.
\tag{3}
\]
The product is independent of the representatives and is multiplicative: in a product \(g_1g_2\), the cosets for \(g_2\) are merely permuted before applying \(g_1\), and changing representatives inserts cancelling factors. This is the transfer used in Proposition 5.2, equation (11), of [The reciprocity law and the class field correspondence](the-reciprocity-law-and-the-class-field-correspondence.md).

### The transfer to the commutator subgroup

We prove the group-theoretic theorem completely. For a group \(G\), let \(I_G\) be the augmentation ideal in \(\mathbf Z[G]\), and write \(\delta g=g-1\).

**Transfer lemma.** If \(G\) is finitely generated and \(A=G/[G,G]\) is finite, then
\[
\operatorname{Ver}:A\longrightarrow [G,G]/[[G,G],[G,G]]
\quad\text{is trivial}.
\tag{4}
\]

**Proof.** Put \(V=[G,G]\), \(R=\mathbf Z[A]\), and
\(M=I_G/(I_GI_V)\), viewed as a right \(R\)-module. The action factors through \(A\): multiplying an element of \(I_G\) by a difference of representatives modulo \(V\) gives an element of \(I_GI_V\). The ring \(R\) is commutative.

First identify transfer in this module. The abelian group \(T=\mathbf Z[G]I_V\) has basis \(r(h-1)\), for coset representatives \(r\) and \(h\in V\setminus\{1\}\). Send this basis element to the class of \(h\) in \(V^{\mathrm{ab}}\), using additive notation in the target. This map kills \(I_GI_V\). Indeed if \(gr=r'h'\), then
\[
gr(h-1)=r'\bigl(\delta(h'h)-\delta h'\bigr),
\]
whose image is \([h'h]-[h']=[h]\), the same as the image of \(r(h-1)\). Their difference generates the required relations. Conversely \(h\mapsto\delta h\) modulo \(I_GI_V\) is a homomorphism, since
\(\delta(hk)=\delta h+\delta k+\delta h\delta k\)
and \(I_V^2\subseteq I_GI_V\). The two maps are inverse, because \(r\delta h\equiv\delta h\). Thus
\[
T/(I_GI_V)\simeq V^{\mathrm{ab}}.
\tag{5}
\]
Summing \(\delta(gr)=\delta g\,r+\delta r=\delta r'+r'\delta h_r\) over the representatives cancels the \(\delta r\) terms by permutation. Modulo \(I_GI_V\), it gives
\[
\delta g\sum_r r\equiv\sum_r\delta h_r.
\tag{6}
\]
Under (5), the right side is exactly (3).

Let \(g_1,\ldots,g_n\) generate \(G\). The kernel of \(\mathbf Z^n\to A\), sending the standard basis to these generators, is a full lattice. Choose its basis matrix \((m_{ik})\) with positive determinant \(|A|\); integer lattice index gives this determinant. The words
\(w_k=\prod_i g_i^{m_{ik}}\)
belong to \(V\). The identities
\[
\delta(xy)=\delta x\,y+\delta y,
\qquad\delta(x^{-1})=-\delta x\,x^{-1}
\tag{7}
\]
expand every word as a right-linear combination of the \(\delta g_i\). The augmentation of the coefficient of \(\delta g_i\) is its total exponent in the word. Each \(w_k\) also has an expression as a product of commutators of generator words, with total exponent zero for each generator. Subtract these two expansions of the same \(\delta w_k\) and pass to \(M\). We obtain a matrix \((\mu_{ik})\) over \(R\) with
\[
\sum_i\delta g_i\,\mu_{ik}=0,
\qquad \operatorname{aug}(\mu_{ik})=m_{ik}.
\tag{8}
\]
This explains both the existence of the matrix and its augmentation, including negative exponents.

Let \(\Delta=\det(\mu_{ik})\in R\). Multiplication by its adjugate gives \(\delta g_i\Delta=0\) in \(M\) for every \(i\). These \(\delta g_i\) generate \(I_G\) as a right module, by (7), so \(\delta g\Delta=0\) for all \(g\). Projecting to \(R\) gives
\((a-1)\Delta=0\) for all \(a\in A\). Thus the coefficients of \(\Delta\) are all equal: translation by \(A\) permutes its basis regularly. Hence
\[
\Delta=c\sum_{a\in A}a,
\qquad
c|A|=\operatorname{aug}(\Delta)=\det(m_{ik})=|A|,
\]
so \(c=1\). Therefore \(\delta g\sum_r r=0\) in \(M\). Equations (5)–(6) make every transfer value trivial, proving (4). \(\square\)

**Theorem 19.2 (principal ideal theorem).** Every fractional ideal of \(K\) becomes principal in its ordinary Hilbert class field \(H\).

**Proof.** Let \(H_2\) be the Hilbert class field of \(H\). Uniqueness makes \(H_2/K\) Galois: every conjugation of \(H\) sends its maximal abelian everywhere-unramified extension to itself. Unramified extensions compose in towers, and real places still split, so \(H_2/K\) is everywhere unramified. Its maximal abelian subextension is \(H\), by Theorem 19.1. Consequently for \(G=\operatorname{Gal}(H_2/K)\),
\[
V=\operatorname{Gal}(H_2/H)=[G,G],
\]
and \(V\) is abelian.

Reciprocity identifies \(\operatorname{Cl}_K\) with \(G/V\) and \(\operatorname{Cl}_H\) with \(V\). Inclusion of idèle classes corresponds to transfer by Proposition 5.2; passing to their ordinary ideal quotients makes the same map extension of ideals \(\mathfrak a\mapsto\mathfrak a\mathcal O_H\). Lemma (4) makes this map zero. Thus the extended ideal has trivial class in \(\operatorname{Cl}_H\), which is exactly principality. \(\square\)

The ideal map used here is compatible with extension because a finite local component inserted into all completions above it has valuations multiplied by the ramification indices. The associated ideal is therefore the extended ideal. This verifies the arithmetic interpretation of the transfer, not just the formal Galois reduction.

## 3. Quadratic genus fields and the real-field distinction

Let \(K=\mathbf Q(\sqrt D)\), with nontrivial fundamental discriminant \(D\). Factor it into prime discriminants
\[
D=d_1\cdots d_t,
\qquad p^*=(-1)^{(p-1)/2}p\text{ for odd }p,
\tag{9}
\]
with the single dyadic factor, if present, equal to \(-4\), \(8\), or \(-8\). The integer \(t\) is the number of rational primes dividing \(|D|\). These signed discriminants include each prime exactly once.

**Proposition 19.3 (genus field).** The maximal subfield of \(H^+\) abelian over \(\mathbf Q\) is
\[
M^+=\mathbf Q(\sqrt{d_1},\ldots,\sqrt{d_t}),
\qquad
\operatorname{Gal}(M^+/K)\simeq
\operatorname{Cl}_K^+/(\operatorname{Cl}_K^+)^2
\simeq(\mathbf Z/2)^{t-1}.
\tag{10}
\]
For imaginary \(K\), this is also the ordinary genus field. For real \(K\), the ordinary genus field is the maximal totally real subfield of \(M^+\). Consequently
\[
|\operatorname{Cl}_K/\operatorname{Cl}_K^2|=
\begin{cases}
2^{t-1},&D<0,\\
2^{t-1},&D>0\text{ and every }d_i>0,\\
2^{t-2},&D>0\text{ and some }d_i<0.
\end{cases}
\tag{11}
\]
The last case has at least two negative factors, so its exponent is nonnegative.

**Proof.** The square classes of the \(d_i\) are independent: each odd prime valuation detects its own factor, and the remaining dyadic square class is nontrivial. Kummer theory gives \([M^+:\mathbf Q]=2^t\), and (9) places \(K\) in \(M^+\).

At a finite prime, only one of the quadratic fields \(\mathbf Q(\sqrt{d_i})\) ramifies, and its local ramified extension has degree \(2\); all the other factors are unramified. Thus the absolute inertia in their compositum has order \(2\) and maps nontrivially to the inertia in \(K/\mathbf Q\). Its kernel over \(K\) is trivial. This holds at \(2\) as well: odd fundamental discriminants give unramified or split \(2\)-adic extensions, and the unique dyadic factor supplies the ramified one. Therefore \(M^+/K\) is unramified at every finite place, and is abelian, so it lies in \(H^+\).

Put \(A=\operatorname{Cl}_K^+\). Conjugation of ideals induces inversion on \(A\), since \(\mathfrak a\bar{\mathfrak a}=(N\mathfrak a)\) has a positive rational generator. The narrow class field is stable under the nontrivial automorphism of \(K/\mathbf Q\), by uniqueness. Choose a finite prime ramified in \(K\). Since \(H^+/K\) is unramified there, its absolute inertia has order \(2\) and maps onto \(\operatorname{Gal}(K/\mathbf Q)\). This supplies an order-two lift of that automorphism. Thus
\[
\operatorname{Gal}(H^+/\mathbf Q)=A\rtimes\mathbf Z/2,
\]
where the lift acts by inversion. Its commutator subgroup is \(A^2\), as the commutators with the lift are precisely the squares. The maximal abelian subfield is therefore multiquadratic, with its relative Galois group \(A/A^2\).

We show that every quadratic subfield of this abelian subfield is already in \(M^+\). At a ramified finite prime its character on local units is either the character of \(K\) or trivial, because absolute inertia has order \(2\) and maps isomorphically to that of \(K\). At an unramified prime it is trivial on units. Select exactly those prime discriminants \(d_i\) where the first choice occurs. The quadratic character of their product has exactly the same restrictions on every finite unit group: all other prime discriminants are locally unramified there. The quotient of these characters defines an extension of \(\mathbf Q\) unramified at every finite prime. Such an abelian extension is trivial, since the narrow Hilbert class group of \(\mathbf Q\) is trivial—every rational ideal has a positive generator. Hence the two characters coincide. This proves maximality of \(M^+\), and its already computed degree gives (10).

For real \(K\), the ordinary Hilbert field requires all real places to remain real. Thus its maximal abelian-over-\(\mathbf Q\) subfield is exactly the real part of \(M^+\): that real part is unramified at every place over \(K\), and every ordinary genus field lies in it. If all \(d_i\) are positive, nothing is removed. Otherwise complex conjugation is a nontrivial order-two element on \(M^+\), so its real part has half its degree. Applying the same inversion-and-commutator calculation to the ordinary class group proves (11). The imaginary case has no real place condition and \(H=H^+\). \(\square\)

For a real quadratic field, the middle case of (11) is also equivalent to \(-1\in N_{K/\mathbf Q}K^\times\). The Hilbert symbol at each odd ramified prime tests \((-1/p)\); it is \(1\) exactly when \(p\equiv1\pmod4\). If all these tests pass, the \(2\)-adic formula of lesson 11 also gives \(1\), and infinity gives \(1\). Hasse’s cyclic norm theorem then supplies the global norm. These conditions are precisely positivity of all the factors in (9). The assertion concerns a norm of a field element, which need not be a unit.

For example \(D=12=(-4)(-3)\), so \(M^+=\mathbf Q(i,\sqrt{-3})\). The field \(K=\mathbf Q(\sqrt3)\) has narrow genus quotient of order \(2\), but ordinary genus quotient of order \(1\). This agrees with its ordinary class number \(1\) and narrow class number \(2\). It shows why a formula \(2^{t-1}\) for every ordinary quadratic class group would be false.

## 4. Ring class fields of imaginary quadratic orders

Let \(K\) be imaginary quadratic and \(\mathcal O=\mathbf Z+f\mathcal O_K\) an order of conductor integer \(f\geq1\). Its Picard group consists of invertible fractional \(\mathcal O\)-ideals modulo principal ideals. Theorem 11.3 of the orders lesson proves extension and contraction of ideals prime to \(f\), with equal norms, and that every invertible class has such a representative. This identifies
\[
\operatorname{Pic}(\mathcal O)\simeq I_K^{(f)}/P_{K,\mathbf Z}(f),
\tag{12}
\]
where \(P_{K,\mathbf Z}(f)\) is generated by principal ideals \((\alpha)\) with \(\alpha\equiv a\pmod{f\mathcal O_K}\) locally at \(f\), for an integer \(a\) coprime to \(f\).

Here is the kernel verification in (12). A prime-to-conductor ideal has trivial Picard class exactly when its contraction is principal. At every conductor prime, a generator of such a principal ideal must be a unit in the localized order. Its residue is therefore in
\((\mathcal O/f\mathcal O_K)^\times=(\mathbf Z/f)^\times\).
Conversely a generator with such a residue is an order unit at those primes, so contraction of its full-ring principal ideal agrees locally everywhere with its order principal ideal. The equality follows from local detection of ideal membership, proved in the orders lesson. Fractional generators may have denominators outside \(f\); their residue is still represented by an integer coprime to \(f\). Passing to ratios gives exactly the generated subgroup in (12). When \(f=1\), these conditions impose no restriction.

**Theorem 19.4.** There is a unique finite abelian **ring class field** \(L_{\mathcal O}/K\) whose ideal Artin kernel in \(I_K^{(f)}\) is \(P_{K,\mathbf Z}(f)\), and
\[
\operatorname{Gal}(L_{\mathcal O}/K)\simeq\operatorname{Pic}(\mathcal O).
\tag{13}
\]
It is Galois over \(\mathbf Q\), with
\[
\operatorname{Gal}(L_{\mathcal O}/\mathbf Q)
\simeq\operatorname{Pic}(\mathcal O)\rtimes\mathbf Z/2,
\tag{14}
\]
where the nontrivial element acts by inversion. Its conductor over \(K\) divides \(f\mathcal O_K\). The maximal-order case is the Hilbert class field.

**Proof.** The subgroup in (12) contains the ray principal subgroup modulo \(f\), and has finite index by the Picard finiteness theorem, Theorem 11.4 of the orders lesson. Takagi’s correspondence, Proposition 18.5, therefore constructs the field and gives (13), with the stated conductor bound.

Complex conjugation preserves both the modulus and the subgroup in (12). Uniqueness and conjugation compatibility of reciprocity imply \(\overline{L_{\mathcal O}}=L_{\mathcal O}\), so the field is Galois over \(\mathbf Q\). Complex conjugation is an order-two automorphism restricting nontrivially to \(K\), and therefore splits its Galois exact sequence. On ideal classes it acts by inversion: \(\mathfrak a\bar{\mathfrak a}=(N\mathfrak a)\), with rational generator prime to \(f\), is trivial in (12). This proves (14). For \(f=1\), (12) is the ordinary ideal class group and Theorem 19.1 identifies the field. \(\square\)

### Order arithmetic used in the examples

Here are the ideal and form arguments needed in sections 4–8. They also give a direct reading route through those examples. For a freely readable comparison of proper ideals and their inverses, see A. Sutherland, [*The CM torsor*, §§17.1–17.3, Theorem 17.10](https://math.mit.edu/classes/18.783/2023/LectureNotes17.pdf). Only the order arithmetic is used here.

**Ideals away from the conductor.** Put \(B=\mathcal O_K\) and \(O=\mathbf Z+fB\). Then \(fB\subset O\). At a rational prime \(\ell\nmid f\), localization therefore gives \(O\otimes\mathbf Z_\ell=B\otimes\mathbf Z_\ell\). An integral ideal prime to \(f\) has localization equal to the full ring at every \(\ell\mid f\). Thus extension and contraction preserve its localizations everywhere and are mutually inverse. Equality of these lattices can be detected locally: after clearing a common denominator, a nonzero quotient is a finitely generated abelian group and has a nonzero localization at some prime. The same local argument proves preservation of ideal norms, since the quotients at conductor primes are zero and the other quotients agree.

Every invertible fractional \(O\)-ideal has a representative prime to \(f\). Indeed an invertible ideal is locally principal: if \(II^{-1}=O\), write \(1=\sum a_jb_j\), and at a maximal ideal some \(a_jb_j\) is a unit; this \(a_j\) generates the localized ideal. Over \(O\otimes\mathbf Z_\ell\), choose one generator by the Chinese remainder theorem on its finitely many maximal ideals. For the finitely many \(\ell\mid f\), let these generators be \(\lambda_\ell\). Choose \(a\in K^\times\) sufficiently close to \(\lambda_\ell^{-1}\) at all those primes. Such approximation follows by clearing denominators and applying the Chinese remainder theorem to the rank-two integer lattice \(B\); the required congruences are open and nonempty. Then \(aI\) equals the local order at every conductor prime. Multiplying by an integer prime to \(f\) clears its remaining denominators. This gives the desired integral representative. The argument applies as well to fractional \(B\)-ideals. It proves the representative and extension–contraction assertions used in (12).

There is also an exact sequence
\[
B^\times\longrightarrow
\frac{(B/fB)^\times}{(\mathbf Z/f\mathbf Z)^\times}
\longrightarrow\operatorname{Pic}(O)
\longrightarrow\operatorname{Cl}(B)\longrightarrow1.
\]
For \(f=1\), the middle residue group is trivial. For \(f>1\), lift a residue unit to \(\alpha\in B\) prime to \(f\) and contract \(\alpha B\); its invertible order-ideal class defines the middle map. Two lifts have quotient congruent to 1 locally modulo \(fB\), hence their contracted ideals differ by an order principal ideal. Multiplication by an integer residue unit has the same property. Surjectivity on the right follows from the prime-to-conductor representatives. A class in its kernel extends to \(\alpha B\); after clearing denominators prime to \(f\), \(\alpha\) gives a residue unit, so the class comes from the middle map. Finally this class is order principal exactly when a generator can be changed by a \(B\)-unit to be an order unit at the conductor. Its residue is then an integer unit modulo \(f\). This is exactly the image of the first map, proving exactness. These arguments also verify the principal subgroup in (12), including fractional generators.

Norms of invertible ideals are multiplicative. Locally such an ideal is generated by one element; multiplication by that element has determinant its field norm on the rank-two lattice. The local index of a product therefore multiplies by the same determinant. Comparing indices at every rational prime proves the global identity, and clearing denominators extends it to fractional ideals.

**Forms and ideal classes.** Let \(D<0\) be the discriminant of \(O\), choose \(\sqrt D\) with positive imaginary part, and orient ideal bases by that embedding. A primitive positive form
\[
Q(x,y)=ax^2+bxy+cy^2,\qquad b^2-4ac=D,
\]
gives the ideal \(I=[a,(b+\sqrt D)/2]\). Its norm is \(a\), because its second generator differs from a fixed generator of \(O\) by an integer. If \(\tau=(b+\sqrt D)/(2a)\), its primitive integral polynomial is \(aX^2-bX+c\). An element preserving \([1,\tau]\) is \(m+n\tau\), and preserving its product with \(\tau\) requires \(a\mid nb\) and \(a\mid nc\). As \(\gcd(a,b,c)=1\), these two requirements imply \(a\mid n\). Thus the multiplier ring is \([1,a\tau]=O\). Further,
\[
I\bar I=a[a,(b+\sqrt D)/2,(b-\sqrt D)/2,c]=aO:
\]
the integer generators \(a,b,c\) span 1. Hence \(I\) is invertible and \(I^{-1}=\bar I/a\). Its normalized norm form is exactly \(Q\).

Conversely, for an invertible ideal with oriented basis \((\alpha,\beta)\),
\[
Q_I(x,y)=\frac{N_{K/\mathbf Q}(x\alpha+y\beta)}{N(I)}
\]
is integral, primitive and positive, with discriminant \(D\). Integrality follows because \((z)I^{-1}\) is an integral ideal for \(z\in I\), and its norm is \(N(z)/N(I)\). For primitivity, at each prime \(\ell\) choose an element of \(I\) congruent to a local generator modulo \(\ell I\). Its normalized norm is an \(\ell\)-adic unit. No prime can therefore divide every value, or all three coefficients, of \(Q_I\). The determinant of the ideal basis has absolute value \(N(I)\) times that of the order basis, so the discriminant of its norm form is \(D\). Write its first two coefficients as \(a,b\). The orientation gives
\(\beta/\alpha=(b+\sqrt D)/(2a)\), so scaling the ideal by \(a/\alpha\) recovers \([a,(b+\sqrt D)/2]\).

Changing an oriented basis is an \(\mathrm{SL}_2(\mathbf Z)\) change of variables. Multiplying the ideal by \(\lambda\in K^\times\) preserves orientation, scales its norm by \(N(\lambda)>0\), and leaves the normalized form unchanged. The two constructions just given are inverse. Thus proper form classes are precisely invertible ideal classes. Conjugation replaces \(b\) by \(-b\) and takes the inverse class, by \(I\bar I=aO\).

**Reduction and the three maximal-order class numbers.** A shear first puts \(|b|\leq a\). If \(c<a\), the determinant-one substitution \((x,y)\mapsto(-y,x)\) replaces \((a,b,c)\) by \((c,-b,a)\) and decreases the positive integer first coefficient. Repeating terminates at
\[
|b|\leq a\leq c,\qquad
b\geq0\text{ if }|b|=a\text{ or }a=c.
\]
The boundary convention follows by a shear when \(|b|=a\), and by the displayed substitution when \(a=c\). Such a reduced form has \(3a^2\leq|D|\), since \(4ac-b^2\geq3a^2\). There are consequently finitely many reduced forms, proving Picard finiteness for every imaginary quadratic order.

For completeness, this enumeration counts classes, rather than merely bounding them. The least nonzero value of a reduced form is \(a\):
\(Q(x,y)\geq a(x^2-|xy|+y^2)\geq a\).
If \(a<c\), its primitive vectors attaining that value are only \(\pm(1,0)\). Therefore an equivalence between reduced forms fixes the first coefficient, and its first basis vector is one of those vectors; the second coefficient can change only by \(2ak\). The reduced inequalities force \(k=0\), except for the two boundary signs \(b=\pm a\), already identified by the convention. When \(a=c\) and \(|b|<a\), the additional minimal vectors are \(\pm(0,1)\); swapping them changes only the sign of \(b\). When \(a=c=|b|\), there is one additional pair \(\pm(1,-\operatorname{sgn}(b))\), and using it again yields that same boundary form. This exhausts the possible minimal vectors and proves uniqueness under the stated convention.

Checking the integers \(a\leq\sqrt{|D|/3}\), \(|b|\leq a\) and \(c=(b^2-D)/(4a)\) gives these complete lists of reduced primitive forms:

- For \(D=-20\), the forms are \((1,0,5)\) and \((2,2,3)\), so \(h=2\).
- For \(D=-56\), the forms are \((1,0,14)\), \((2,0,7)\), \((3,2,5)\) and \((3,-2,5)\), so \(h=4\).
- For \(D=-23\), the forms are \((1,1,6)\), \((2,1,3)\) and \((2,-1,3)\), so \(h=3\).

For \(-56\), the last two forms are distinct inverse classes, so their order is greater than two. A group of order four with such an element is cyclic. This proves the class-group assertions used in sections 6 and 8.

**The order of conductor six in \(\mathbf Q(\sqrt{-3})\).** Write \(B=\mathbf Z[\zeta_3]\). It is norm Euclidean: approximate the two real lattice coordinates of a complex number by integers, leaving coordinates \(u,v\) of absolute value at most \(1/2\); then
\(N(u+v\zeta_3)=u^2-uv+v^2\leq3/4<1\).
Division with this remainder gives the Euclidean algorithm, so \(\operatorname{Cl}(B)=1\). Solving \(u^2-uv+v^2=1\) gives its six units. The order \(O=\mathbf Z+6B=\mathbf Z[\sqrt{-27}]\) has just the two units \(\pm1\).

The Chinese remainder theorem gives \(B/6B=(B/2B)\times(B/3B)\). The first factor is \(\mathbf F_4\), with three units, since \(X^2+X+1\) is irreducible modulo 2. The second is \(\mathbf F_3[\epsilon]/(\epsilon^2)\), with six units, since the same polynomial has a double root modulo 3. There are eighteen residue units in total. The integer residue-unit subgroup has order \(\varphi(6)=2\). The image of \(B^\times\) in the quotient by those integer units has order three: a unit lies in that kernel exactly when it belongs to the unit group of \(O\), which has order two. The exact sequence above therefore gives
\[
|\operatorname{Pic}(\mathbf Z[\sqrt{-27}])|=\frac{18}{2\cdot3}=3.
\]
This supplies the class number and the norm and ideal identifications required by the cubic example, without an external class-field table.


## 5. A splitting test for primes represented by a norm form

Fix \(n>0\), \(K=\mathbf Q(\sqrt{-n})\), and \(\mathcal O=\mathbf Z[\sqrt{-n}]\). This is an order even when \(n\) has square factors. Its discriminant is \(-4n=f^2D_K\), and let \(L\) be its ring class field.

**Theorem 19.5.** For an odd prime \(p\nmid n\),
\[
p=x^2+ny^2\text{ with }x,y\in\mathbf Z
\quad\Longleftrightarrow\quad p\text{ splits completely in }L.
\tag{15}
\]
There is a real algebraic integer \(\alpha\) with \(L=K(\alpha)\). Its minimal polynomial \(f_n\in\mathbf Z[X]\) has degree \(|\operatorname{Pic}(\mathcal O)|\), and for odd \(p\nmid n\operatorname{disc}(f_n)\),
\[
p=x^2+ny^2
\quad\Longleftrightarrow\quad
(-n/p)=1\text{ and }f_n\text{ has a root in }\mathbf F_p.
\tag{16}
\]

**Proof.** Since \(p\nmid-4n\), the prime is unramified in \(K\) and prime to the conductor of \(\mathcal O\). A representation gives \(\beta=x+y\sqrt{-n}\in\mathcal O\) of norm \(p\). Its principal ideal has norm \(p\), by the ideal norm and extension–contraction theorem, so it is a prime ideal above a split rational prime. Its invertible order ideal class is trivial. Conversely a split prime whose contracted order ideal is principal has a generator \(\beta\in\mathcal O\) with norm \(p\): the ideal is contained in \(\mathcal O\), hence its generator belongs to it, and the imaginary norm is positive. Writing \(\beta=x+y\sqrt{-n}\) gives the representation. By (13) triviality of this class means trivial Frobenius in \(L/K\). The conjugate prime has inverse class and is trivial as well. As \(L/\mathbf Q\) is Galois, this is complete rational splitting, proving (15).

Let \(c\) be complex conjugation in (14), and \(R=L^{\langle c\rangle}\). It is a real field of degree \(|\operatorname{Pic}(\mathcal O)|\) over \(\mathbf Q\). A primitive element can be chosen integral: for two separable generators, all but finitely many rational linear combinations distinguish their embeddings; repeat and clear a rational denominator. Choose such an \(\alpha\in R\). Since \(K\) is imaginary quadratic and \(R\) is real, \(K\cap R=\mathbf Q\), so \(KR=L\). Thus \(L=K(\alpha)\) and its monic minimal polynomial over \(\mathbf Q\) has the asserted degree and integer coefficients.

At a prime avoiding the polynomial discriminant, its roots have distinct reductions in the splitting field. Frobenius fixes a reduced root exactly when that root lies in \(\mathbf F_p\); distinctness makes this equivalent to fixing its algebraic conjugate. If \((-n/p)=1\), Frobenius lies in \(A=\operatorname{Gal}(L/K)\). Its action on the \(A\)-orbit of \(\alpha\) is regular, because \(\alpha\) generates \(L/K\). Therefore fixing any one of those conjugates forces Frobenius to be the identity. The full \(\mathbf Q\)-orbit is that same orbit, by its degree. Combining this with (15) proves (16). The discriminant exclusion is necessary for this distinct-root argument. \(\square\)

## 6. The forms with coefficients five and fourteen

The quadratic-fields lesson enumerates the two reduced forms of discriminant \(-20\), so \(K=\mathbf Q(\sqrt{-5})\) has class number \(2\). Its prime discriminants are \(-4\) and \(5\). Proposition 19.3 gives a genus field of relative degree \(2\), already the whole Hilbert class field:
\[
H=\mathbf Q(\sqrt{-5},i)=\mathbf Q(i,\sqrt5).
\tag{17}
\]
For an odd prime \(p\ne5\), complete splitting in this biquadratic field means
\((-1/p)=(5/p)=1\). The quadratic reciprocity law proved in lesson 16 gives \((5/p)=(p/5)\). Thus (15) gives
\[
p=x^2+5y^2\quad\Longleftrightarrow\quad p\equiv1,9\pmod{20}.
\tag{18}
\]
The conditions are \(p\equiv1\pmod4\) and \(p\equiv\pm1\pmod5\); the Chinese remainder theorem gives the two displayed residues. The excluded prime \(5\) is represented by \(0^2+5\cdot1^2\), whereas \(2\) is not represented. Thus for every rational prime the condition is \(p=5\) or \(p\equiv1,9\pmod{20}\). The restriction in (18) must not be omitted.

For \(K=\mathbf Q(\sqrt{-14})\), the reduced forms of discriminant \(-56\) give class group \(\mathbf Z/4\), as proved in the quadratic-fields lesson. We claim
\[
H=K(\alpha),\qquad
\alpha=\sqrt{2\sqrt2-1}>0,
\qquad f_{14}(X)=X^4+2X^2-7.
\tag{19}
\]
We verify degree, cyclicity and unramifiedness, including the dyadic place.

The norm of \(-1+2\sqrt2\) from \(\mathbf Q(\sqrt2)\) is \(-7\), so it is not a square there. Hence \([\mathbf Q(\alpha):\mathbf Q]=4\). This field is real and intersects the imaginary quadratic \(K\) in \(\mathbf Q\); therefore \([K(\alpha):K]=4\). The field \(L=K(\alpha)\) contains
\[
\sqrt2=(\alpha^2+1)/2,\qquad
\sqrt{-7}=\sqrt{-14}/\sqrt2,\qquad
\beta=\sqrt{-7}/\alpha,
\]
with \(\beta^2=-1-2\sqrt2\). Thus it contains all four roots \(\pm\alpha,\pm\beta\) of \(f_{14}\), so it is a splitting field. An automorphism over \(K\) taking \(\alpha\) to \(\beta\) takes \(\sqrt2\) and \(\sqrt{-7}\) to their negatives; it consequently takes \(\beta\) to \(-\alpha\). It has order \(4\), proving that \(L/K\) is cyclic.

The resultant with \(f_{14}'=4X(X^2+1)\) gives
\[
\operatorname{disc}(f_{14})=-2^{14}\cdot7.
\tag{20}
\]
Indeed the product of its roots is \(-7\), while the product of their \((X^2+1)\) values is \(f_{14}(i)f_{14}(-i)=64\), and the derivative contributes \(4^4\). Therefore no finite prime except \(2\) or \(7\) can ramify in the splitting field. This follows also directly from distinct residue roots: inertia fixes each integral root's residue, and when the discriminant is a unit the roots have distinct residues, forcing inertia to fix all roots.

At \(7\), choose the \(7\)-adic square root \(\sqrt2\equiv3\pmod7\), supplied by Hensel's lemma. Then \(\alpha^2\equiv5\pmod7\) is a nonsquare unit, so adjoining \(\alpha\) is unramified quadratic. The completion of \(K\) is \(\mathbf Q_7(\sqrt{-7})\), and that of \(L\) is obtained by adjoining this unramified radical. Base change remains unramified.

At \(2\), \(-7\equiv1\pmod8\) is a square in \(\mathbf Q_2\), so \(K_v=E=\mathbf Q_2(\sqrt2)\). Put \(u=-1+2\sqrt2\). The polynomial
\[
25r^2+5r+2
\]
has value \(32\) and odd derivative \(55\) at \(r=1\). Hensel's lemma gives a root \(r\equiv1\pmod8\), which is a square \(a^2\) in \(\mathbf Q_2\) by the odd-unit square criterion. Set \(b=1/(5a)\). Its defining equation gives
\[
a^2+2b^2=-1/5,\qquad ab=1/5,
\qquad (a+b\sqrt2)^2=u/5.
\tag{21}
\]
Consequently \(E(\alpha)=E(\sqrt5)\), the base change of the unramified quadratic extension of \(\mathbf Q_2\). It is unramified over \(E\). All infinite places of \(K\) are complex. We have proved that \(L/K\) is everywhere unramified and cyclic of degree \(4\). The Hilbert class field has degree \(4\), so \(L=H\), proving (19).

Equations (16), (19) and (20) now give the explicit test, for odd \(p\ne7\),
\[
p=x^2+14y^2\quad\Longleftrightarrow\quad
(-14/p)=1\text{ and }X^4+2X^2-7\text{ has a root modulo }p.
\tag{22}
\]

## 7. The cubic criterion for \(x^2+27y^2\)

The order \(\mathcal O=\mathbf Z[\sqrt{-27}]\) has conductor \(6\) in \(K=\mathbf Q(\sqrt{-3})\) and Picard group of order \(3\), computed in Corollary 11.5 and Exercise 3 of the orders lesson. Its ring class field \(L\) is therefore cyclic cubic over \(K\), and (14) makes \(L/\mathbf Q\) an \(S_3\)-extension. Its finite ramification is supported above \(2\) and \(3\).

We identify \(L\) without a table of class fields. Let \(\sigma\) generate \(\operatorname{Gal}(L/K)\), let \(\zeta\) be a primitive cube root of unity, and choose a real integral primitive element \(\alpha\), as in Theorem 19.5. Define
\[
u_j=\alpha+\zeta^j\sigma^{-1}\alpha+\zeta^{2j}\sigma^{-2}\alpha,
\qquad j=0,1,2.
\tag{23}
\]
Then \(\sigma u_j=\zeta^j u_j\). Complex conjugation fixes \(\alpha\), inverts \(\zeta\), and changes \(\sigma\) into \(\sigma^{-1}\); it interchanges the last two terms and fixes each \(u_j\). Thus \(u_j^3\) is a real element of \(K\), hence a rational integer. At least one of \(u_1,u_2\) is nonzero: otherwise the inverse three-term Fourier transform would give \(3\alpha=u_0\), making \(\alpha\) rational. A nonzero such \(u_j\) is not in \(K\), by its nontrivial eigenvalue, and generates \(L/K\). Removing integer cube factors and changing its sign gives
\[
L=K(\sqrt[3]m),\qquad m>0\text{ cube-free}.
\tag{24}
\]

Every rational prime dividing \(m\) ramifies in this radical extension. Its valuation in \(K\) is its exponent \(1\) or \(2\), multiplied by the base ramification index, which is \(2\) only at \(3\). This is never divisible by \(3\). A cube root therefore has fractional valuation and forces relative ramification. Since only \(2,3\) can ramify, the possible \(m\)'s are
\(2,3,4,6,9,12,18,36\).
Replacing a radical by its square pairs these into four fields:
\[
K(\sqrt[3]2),\quad K(\sqrt[3]3),\quad
K(\sqrt[3]6),\quad K(\sqrt[3]{12}).
\tag{25}
\]

But \(31=2^2+27\) splits completely in \(L\), by (15). It splits in \(K\), since \(11^2\equiv-3\pmod{31}\). Its nonzero cubic residues are precisely
\[
1,2,4,8,15,16,23,27,29,30.
\]
At a split prime away from \(6\), the extension in (24) splits locally exactly when \(m\) is a cube in \(\mathbf F_{31}\): the simple residue root lifts, and \(\mu_3\) is already present. This excludes \(m=3,6,12\) in (25). Therefore
\[
L=K(\sqrt[3]2),\qquad f_{27}(X)=X^3-2.
\tag{26}
\]
Its polynomial discriminant is \(-108\). For \(p>3\), the quadratic reciprocity law of lesson 16 gives \((-3/p)=1\) exactly when \(p\equiv1\pmod3\). The root test (16) consequently proves Gauss's criterion
\[
p=x^2+27y^2\quad\Longleftrightarrow\quad
p\equiv1\pmod3\text{ and }2\text{ is a cube modulo }p.
\tag{27}
\]
The exclusion of \(2,3\) agrees with the explicit discriminant calculation.

## 8. A cubic generator for the Hilbert field of discriminant \(-23\)

Reduction gives the three forms
\((1,1,6),(2,1,3),(2,-1,3)\)
of discriminant \(-23\), so \(K=\mathbf Q(\sqrt{-23})\) has class number \(3\). Let \(\alpha\) be the real root of
\[
f(X)=X^3-X-1.
\tag{28}
\]
This cubic has no root modulo \(2\), hence is irreducible over \(\mathbf Q\), and its discriminant is \(-23\). Its splitting field \(S\) has Galois group \(S_3\): a transitive cubic group is \(C_3\) or \(S_3\), and the square root of the discriminant changes by the sign of a root permutation. Its nonsquare discriminant excludes \(C_3\), and its quadratic fixed field is exactly \(K\). Hence \(S=K(\alpha)\) and \([S:K]=3\).

Outside \(23\), distinct root reductions show that \(S/\mathbf Q\) is unramified. At \(23\),
\[
f(X)\equiv(X-10)^2(X-3)\pmod{23}.
\]
The simple root \(3\) lifts to \(\mathbf Q_{23}\), so the local decomposition group fixes one cubic root and is contained in its order-two stabilizer. The quadratic field \(K\) is ramified there, since its discriminant is \(-23\). Thus absolute inertia has order \(2\) and maps nontrivially to \(K\); its relative kernel over \(K\) is trivial. Therefore \(S/K\) is unramified at \(23\) as well. There are no real places of \(K\). The degree-three abelian extension \(S/K\) is everywhere unramified and has the Hilbert field's degree, proving
\[
H(\mathbf Q(\sqrt{-23}))=K(\alpha).
\tag{29}
\]

## 9. Iterating the Hilbert field

Starting with \(K_0=K\), set \(K_{j+1}=H(K_j)\). The principal ideal theorem proved in section 2 makes the ideal classes of \(K_j\) principal in \(K_{j+1}\). This allows further class groups and further Hilbert fields.

[Brauer groups of local and global fields, Theorem 24.9](brauer-groups-of-local-and-global-fields.md#theorem-24-9-an-infinite-hilbert-class-field-tower) proves that the tower of
\[
K=\mathbf Q\bigl(\sqrt{-5\cdot13\cdot17\cdot29\cdot37\cdot41}\bigr)
\]
is infinite. Its proof combines the genus construction of section 3 with the complete filtered Golod–Shafarevich proof and the unit-cohomology relation bound developed in that lesson. Follow that theorem after the cohomology has been established.

## 10. Exercises and complete solutions

### Exercise 1 — A quadratic Hilbert field (easy)

Show that \(H(\mathbf Q(\sqrt{-5}))=\mathbf Q(\sqrt{-5},i)\).

**Solution.** The two reduced positive forms of discriminant \(-20\) are \((1,0,5)\) and \((2,2,3)\), so the class number is \(2\), by the quadratic-fields lesson. The prime discriminants are \(-4\) and \(5\). Proposition 19.3 proves that \(M=\mathbf Q(i,\sqrt5)\) is unramified over \(K=\mathbf Q(\sqrt{-5})\) and has relative degree \(2\). It lies in the Hilbert class field by Theorem 19.1. The latter also has degree \(2\), so they are equal. Since \(i\sqrt5=\sqrt{-5}\), the two descriptions of \(M\) agree.

### Exercise 2 — The congruence test and its exceptional prime (medium)

For an odd prime \(p\ne5\), prove
\(p=x^2+5y^2\Longleftrightarrow p\equiv1,9\pmod{20}\).
Then include the primes excluded by this statement.

**Solution.** The preceding exercise identifies the Hilbert field with the biquadratic field \(\mathbf Q(i,\sqrt5)\). For \(p\nmid10\), Theorem 19.5 says that representation is equivalent to complete splitting there. Its two independent quadratic characters give \((-1/p)=(5/p)=1\). The first condition is \(p\equiv1\pmod4\). Quadratic reciprocity gives \((5/p)=(p/5)\), so the second is \(p\equiv1\) or \(4\pmod5\). Solving these two simultaneous congruences gives \(p\equiv1\) or \(9\pmod{20}\). Finally \(5=0^2+5\cdot1^2\), while a representation of \(2\) would have \(y=0\) and then require an integer square equal to \(2\). Thus the condition for all primes is \(p=5\) or those two residue classes.

### Exercise 3 — A cubic Hilbert-field generator (medium)

For \(K=\mathbf Q(\sqrt{-23})\), show that adjoining the real root of \(X^3-X-1\) gives its Hilbert class field.

**Solution.** The reduced-form bound \(a\leq\sqrt{23/3}<3\) leaves \((1,1,6),(2,1,3),(2,-1,3)\), so \(h_K=3\). The cubic has no root modulo \(2\), hence is irreducible, and discriminant \(-23\). Its splitting field has group \(S_3\), with quadratic fixed field \(K\); adjoining one cubic root to \(K\) is the entire splitting field, cyclic cubic over \(K\). It is unramified away from \(23\), since the root differences have unit discriminant there. At \(23\) the factorization \((X-10)^2(X-3)\) has the simple root \(3\), which Hensel lifts. The local decomposition group therefore lies in a stabilizer of order \(2\). Its inertia maps nontrivially to the ramified quadratic field \(K\), so relative inertia over \(K\) is trivial. The field is everywhere unramified over \(K\), which has no real places. Its degree is the Hilbert degree \(3\), proving the assertion.

### Exercise 4 — The transfer theorem (hard)

Prove that transfer from a finitely generated group with finite abelianization to the abelianization of its commutator subgroup is trivial. Explain its use in Theorem 19.2.

**Solution.** Set \(V=[G,G]\), \(A=G/V\), \(R=\mathbf Z[A]\) and \(M=I_G/(I_GI_V)\). The map \(r(h-1)\mapsto[h]\) identifies \(\mathbf Z[G]I_V/(I_GI_V)\) with \(V^{\mathrm{ab}}\); left multiplication merely permutes cosets and does not change \([h]\). Under this identification, \(\delta g\sum_r r\) is transfer, as the coset-permutation terms cancel in (6).

Choose generators \(g_i\) and a basis \((m_{ik})\) of the relation lattice \(\ker(\mathbf Z^n\to A)\), with determinant \(|A|\). Expand \(\prod_i g_i^{m_{ik}}\) both as that word and as a product of commutators. Their difference, using (7), gives \(\sum_i\delta g_i\mu_{ik}=0\) in \(M\), with \(\operatorname{aug}(\mu_{ik})=m_{ik}\). The adjugate of this matrix annihilates each \(\delta g_i\) by \(\Delta=\det(\mu_{ik})\), and hence annihilates every \(\delta g\). Projection to \(R\) gives \((a-1)\Delta=0\) for each \(a\in A\), so \(\Delta=c\sum_A a\). Taking augmentation gives \(c|A|=|A|\), hence \(c=1\). Transfer is therefore zero. Each step applies to negative exponents by the inverse identity in (7).

For \(G=\operatorname{Gal}(H_2/K)\), the commutator subgroup is \(\operatorname{Gal}(H_2/H)\), which is abelian. The ideal-extension map \(\operatorname{Cl}_K\to\operatorname{Cl}_H\) is this transfer by reciprocity. Its vanishing means that each extended ideal is principal. The argument does not assert that \(\operatorname{Cl}_H\) itself vanishes.

## Editable edition

The reading edition provides the complete LaTeX source of this lesson, the cumulative course LaTeX and the editable source ZIP. The archive contains all twenty-four Markdown lessons, complete LaTeX bodies, original diagrams, metadata and reproduction instructions.

## References

Sections 1–3 prove Hilbert fields, the augmentation-ideal transfer theorem, principalization and the ordinary/narrow genus distinction. Section 4 proves order arithmetic and reduction. Sections 6–8 verify the explicit quadratic prime-form fields by degrees, ramification and residue calculations; lesson 24 supplies the tower arguments.

- [Kiran S. Kedlaya, Notes on class field theory, author-hosted HTML edition](https://kskedlaya.org/cft/sec_abstractcft1.html).
- [J. S. Milne, Class Field Theory, version 4.03](https://www.jmilne.org/math/CourseNotes/CFT.pdf).

The [proof guide](../FREE_PROOFS.md) gives the lesson sequence and the exact prerequisite record. External references accompany the written arguments.
