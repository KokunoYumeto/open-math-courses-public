# Algebraic functions of one variable: conductors and adjoints

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A singular plane curve can put several branches at one point or omit functions that are regular on its normalization. The conductor measures that omission. Trace duality relates it to the different; at an ordinary multiple point it gives precisely the vanishing conditions of an adjoint curve.

We assume Noether's axioms for Dedekind domains, Three differents, and elementary divisors on a smooth curve. Finite normalization and the completed branch description are proved below. Throughout the geometric discussion, \(k\) is algebraically closed and the curves are integral. Arithmetic analogues use orders in number fields, as in **Orders in number fields and their Picard groups**. Prime factorization in a monogenic order is governed by Decomposition of primes in extensions, Theorem 5.3 (Kummer–Dedekind). The projective cohomology and duality arguments use the exact earlier programme proofs linked at their applications; a source citation does not supply those proofs. Basic references are [Noether], [Fulton], [Stacks] and [Vakil].

## 1. A function field, a plane model and its normalization

Let \(L/k\) be finitely generated of transcendence degree one. A nonconstant \(z\in L\) makes \(L/k(z)\) finite. The integral closure \(B\) of \(k[z]\) in \(L\) is finite and Dedekind. Lemma 1.2 proves finiteness, including inseparable extensions, using the separable trace theorem of the first lesson and a finite Frobenius-root module. The earlier Normalization, Theorem 5.1, also gives a complete proof over arbitrary fields. Compare [Stacks, Tag 03GR] for the Nagata-base formulation. The prime ideals of \(B\) give the places where \(z\) is finite. The places at infinity are obtained from the normalization over \(k[1/z]\). Together they are the closed points of the smooth projective curve with function field \(L\).

For trace arguments choose \(z\) **separating**, so that \(L/k(z)\) is separable. Lemma 1.2 supplies the proof of existence over our perfect ground field; compare [Milne FT, Theorem 9.27]. Tags 030Q and 030W describe separating bases and characterize separability; their hypotheses alone do not assert existence over a perfect ground field. An arbitrary transcendental element need not be separating in positive characteristic.

Choose an integral primitive element \(s\) and its monic minimal polynomial \(f(z,T)\in k[z][T]\). The plane order

\[
 O=k[z,s]\subseteq B
\]

is free over \(k[z]\). Its normalization may have more than one point above a singular point. Each local ring upstairs is a DVR, although the normalization over that point is a semilocal ring rather than one DVR.

The **conductor** is

\[
 \mathfrak c=(O:B)=\{b\in B:bB\subseteq O\}
 =\operatorname{Ann}_O(B/O).
\]

It is an ideal of both rings, contained in \(O\), and is nonzero: clear denominators of finitely many \(O\)-module generators of \(B\). Define

\[
 \delta_P=\dim_k(\widetilde{O_P}/O_P),
\]

where \(\widetilde{O_P}\) denotes the semilocal normalization. It is finite: the finite module \(B/O\) is killed by a nonzero conductor element, so its localized support is zero-dimensional and its length is finite. Proposition 1.1 identifies its support; compare [Stacks, Section 0C3Q].

**Proposition 1.1.** The conductor is the unit ideal at a point exactly when that point is nonsingular.

**Proof.** A conductor equal to the unit ideal means \(1\cdot\widetilde{O_P}\subseteq O_P\), hence equality of the two rings. Conversely equality makes the conductor the unit ideal. A one-dimensional Noetherian normal local domain is a DVR; a nonsingular point on a curve over a perfect field has a regular one-dimensional local ring, also a DVR. The DVR characterization is proved in Discrete valuation rings and Dedekind domains. The regular–smooth equivalence at these rational points is Smooth algebras over a field and the Jacobian criterion, Theorem 3.2. These implications give the equivalence. Thus \(\operatorname{Supp}(B/O)\), the vanishing locus of its annihilator, is exactly the singular locus. \(\square\)

**Lemma 1.2 (the curve normalization inputs).** Over the perfect field \(k\), the normalization of an affine integral curve in any finite extension of its function field is finite. A function field of one variable has a separating parameter and a smooth projective model.

**Proof.** First let \(K=k(z)\) and \(L/K\) be finite. In characteristic zero the separable finiteness theorem of Lesson 1 applies to \(k[z]\). In characteristic \(p\), let \(M\) be the subfield of elements of \(L\) separable over \(K\). There is a power \(q=p^e\) with \(L^q\subseteq M\): for each of finitely many field generators, its irreducible polynomial is \(g(T^{p^r})\) with \(g'\ne0\), so its \(p^r\)-th power is separable; take a common exponent. Separable elements form a field, since a compositum of finite separable extensions is separable, as proved in the field preliminaries of Algebraic integers and rings of integers.

Let \(C\) be the integral closure of \(k[z]\) in \(M\). It is finite by Lesson 1. Choose algebra generators \(c_1,\ldots,c_s\) for it. Inside a fixed algebraic closure, the ring
\[
C^{1/q}=k[z^{1/q},c_1^{1/q},\ldots,c_s^{1/q}]
\]
contains the unique \(q\)-th root of every element of \(C\), because \(k\) is perfect and the Frobenius map respects sums and products. Each displayed generator is integral over \(k[z]\): raise an integral equation for \(c_i\) to its root form over \(k[z^{1/q}]\), and use transitivity of integrality. Thus this ring is finite over \(k[z]\). If \(b\) is integral over \(k[z]\) in \(L\), then \(b^q\in M\) is integral and belongs to \(C\). The desired closure is consequently a \(k[z]\)-submodule of \(C^{1/q}\); it is finite because \(k[z]\) is Noetherian. It is Dedekind by Lesson 1, Corollary 4.4.

For an affine curve ring \(R\), Krull dimension and Noether normalization, Corollary 3.2 and Theorem 4.2, supply a finite inclusion \(k[z]\subset R\) and a finite extension of fraction fields. An element of the enlarged field is integral over \(R\) exactly when it is integral over \(k[z]\): one direction is transitivity; the other uses the same monic equation with its coefficients now in \(R\). Its closure is therefore the finite module just constructed. A generating family over \(k[z]\) also generates over \(R\).

Here is the separating-parameter argument, including characteristic \(p\). Choose any transcendental \(z\in L\) and put \(n=[L:k(z)]\), which is finite since \(L\) has finitely many algebraic generators over this field. Frobenius gives
\[
[L^p:k(z^p)]=n,\qquad [L:k(z^p)]=np,
\]
so \([L:L^p]=p\). Choose \(u\notin L^p\); it is transcendental over the algebraically closed field \(k\), and \(L=L^p(u)\). Put \(F=k(u)\), and let \(M/F\) be the maximal separable subextension of \(L/F\). The first paragraph gives \(L^{p^r}\subseteq M\) for some \(r\). If \(L\ne M\), the equality \(L=L^pF\) gives \(L=ML^p\); raising to \(p\)-th powers and substituting repeatedly gives \(L=ML^{p^r}=M\), a contradiction. Hence \(L/F\) is separable. In characteristic zero any transcendental parameter works. Clear the coefficients of the minimal polynomial of a primitive element to make a scalar multiple integral over \(k[u]\); its plane order is a model with function field \(L\). The primitive-element proof is in the same earlier arithmetic lesson.

Normalize the projective closure of this plane model, applying the affine construction on each chart. These normalizations glue: integral closure commutes with localization, since a monic equation over a localization becomes an integral equation for a suitable scalar multiple after clearing its denominators. The resulting map is finite and birational. Its source is proper by Proper morphisms and valuative criteria, Theorem 2.1, and projective-space properness in Theorem 4.1. It is projective as follows. The pullback \(L\) of the hyperplane line has affine section opens covering the source, since the map is finite. On one such open, any principal-open function \(b\) extends after multiplication by a power of its defining section \(s\), by Coherent sheaves on projective schemes: Serre's theorems, Lemma 1.1, whose hypotheses are just quasi-compactness and quasi-separatedness. Multiplying the extension by one additional \(s\) makes its nonvanishing open exactly that principal open, including outside the chart. These affine section opens form a basis, so \(L\) is ample. Lemma 1.3 of that lesson now embeds the proper source closedly in projective space. Its local rings at closed points are DVRs. Their residue fields are \(k\) by the weak Nullstellensatz, and regularity implies smoothness by Smooth algebras over a field and the Jacobian criterion, Theorem 3.2. This gives the promised smooth projective model \(X\).

The same construction from the integral closures over \(k[z]\) and \(k[1/z]\), glued where \(z\) is invertible, gives a finite map to \(\mathbb P^1\). It describes precisely the finite and infinite places. Indeed a nontrivial valuation trivial on \(k\) is nonnegative on one of \(z,z^{-1}\); its valuation ring contains that chart's integral closure, since a root of a monic equation cannot have negative valuation (its leading term would have strictly least value). Its center is a closed point: if its restriction to \(k(z)\) were trivial, the same minimal-polynomial test would force its value on every nonzero algebraic element also to be zero. The localized closure at its center is a DVR, and a valuation ring dominating a DVR in the same fraction field equals it, by writing every element as a uniformizer power times a unit. Conversely each closed-point DVR gives such a place. The birational identification of two projective normal curve models extends over every DVR by Theorem 3.1 of Proper morphisms and valuative criteria. The finitely many coordinates on an affine neighbourhood of the image are elements of that local ring, hence regular on some neighbourhood of the source point; thus these local extensions give morphisms on neighbourhoods and glue by separatedness. The reverse identification does too, and their composites are the identity on the dense generic point and hence everywhere by separatedness. \(\square\)

**Lemma 1.3 (normalization and completed branches).** Let \(R\) be the local ring at a closed point of an integral curve, and \(B\) its finite semilocal normalization. Then
\[
B\otimes_R\widehat R=\prod_{Q}\widehat{B_Q}
=\prod_Q k[[t_Q]]
\]
is the normalization of \(\widehat R\) in its total quotient ring. Conductor kernels and finite lengths are preserved by completion.

**Proof.** Completion, Theorems 3.1 and 3.2, prove tensoring, exactness and faithful flatness for these finite modules. The radical of \(\mathfrak m_RB\) is the intersection of the finitely many maximal ideals \(\mathfrak n_Q\), and its powers and those of \(\mathfrak m_RB\) are cofinal: in the Artinian quotient by \(\mathfrak m_RB\), the radical is nilpotent. The Chinese remainder theorem for the pairwise comaximal powers of the \(\mathfrak n_Q\) therefore splits the completion into the displayed local factors. Each \(B_Q\) is a DVR with residue field \(k\). Successive extraction of residue coefficients in its uniformizer gives an isomorphism \(\widehat{B_Q}=k[[t_Q]]\), with the given embedding of constants; completeness gives surjectivity and the least nonzero coefficient gives injectivity.

Choose a nonzero conductor element \(c\in R\) and multiply it by a nonzero element of \(\mathfrak m_R\). It then has positive valuation on every factor. The equality \(R[1/c]=B[1/c]\) survives flat completion, and gives
\[
\widehat R[1/c]=\prod_Q k((t_Q)).
\]
The inclusion of \(\widehat R\) in the product of power-series rings is injective by exactness of completion. Thus \(\widehat R\) is reduced, \(c\) is a nonzerodivisor, and this product of fields is its total quotient ring: a nonzerodivisor cannot have zero image on a component, since a power of \(c\) times that component's idempotent lies in \(\widehat R\) and would be a nonzero annihilator. The completed \(B\) is finite and integral over \(\widehat R\), and is integrally closed in that product of fields. Every fraction integral over \(\widehat R\) is integral over the completed \(B\), and so belongs to it. This proves the normalization assertion without assuming an excellence theorem.

Choose finite module generators \(b_j\) of \(B\). The conductor is the kernel of \(R\to\bigoplus_j B/R\), \(a\mapsto(ab_j\bmod R)_j\); exact completion preserves it. A composition series of a finite-length \(R\)-module has factors \(k\), unchanged by completion, so its length is preserved as well. \(\square\)

## 2. Euler's lemma and the conductor identity

We first retain a general normal base. Let \(A\) be a normal Noetherian domain with fraction field \(K\), let \(L=K(\theta)\) be finite separable, and let \(f\in A[T]\) be the monic minimal polynomial of the integral element \(\theta\). Put \(O=A[\theta]\). Let \(B\) be its integral closure and assume \(B\) finite over \(A\). For a lattice \(N\), write

\[
 N^*=\{x\in L:\operatorname{Tr}_{L/K}(xN)\subseteq A\}.
\]

**Lemma 2.1 (Euler).** \(O^*=f'(\theta)^{-1}O\), and \(O^{**}=O\).

**Proof.** Let \(\lambda\) extract the coefficient of \(\theta^{n-1}\) from the unique representative of degree less than \(n=\deg f\). In the power basis the pairing \(\lambda(ab)\) has zeros when the exponents sum to less than \(n-1\) and ones when they sum to \(n-1\). Reversing its columns gives a triangular matrix with diagonal ones. It therefore identifies \(O\) with \(\operatorname{Hom}_A(O,A)\).

For distinct roots \(r_i\) of \(f\), Lagrange interpolation gives

\[
 [T^{n-1}]q(T)=\sum_i\frac{q(r_i)}{f'(r_i)}
 =\operatorname{Tr}_{L/K}\left(\frac{q(\theta)}{f'(\theta)}\right)
\]

for \(\deg q<n\). Applying this to products reduced modulo \(f\), the perfect \(\lambda\)-pairing says exactly that the trace-dual lattice is \(f'(\theta)^{-1}O\). Double duality follows from the perfect pairing and freeness of \(O\). \(\square\)

**Theorem 2.2 (general conductor formula).** In this setting,

\[
 \boxed{\mathfrak c=f'(\theta)B^*.}
\tag{2.1}
\]

If \(B\) is Dedekind, its trace-dual fractional ideal is invertible and this becomes Dedekind's familiar formula

\[
 \boxed{\mathfrak c\mathfrak D_{B/A}=f'(\theta)B.}
\tag{2.2}
\]

**Proof.** Double duality tests membership in \(O\) by traces against \(O^*\). For \(c\in L\),

\[
 cB\subseteq O
 \Longleftrightarrow cO^*\subseteq B^*
 \Longleftrightarrow \frac{c}{f'(\theta)}O\subseteq B^*
 \Longleftrightarrow \frac{c}{f'(\theta)}\in B^*.
\]

The last equivalence uses \(1\in O\) and the \(B\)-module structure of \(B^*\). The first condition already forces \(c\in O\subseteq B\), so it is exactly the conductor condition. This proves (2.1). When \(B^*\) is invertible, multiply by its inverse \(\mathfrak D\) to obtain (2.2). \(\square\)

The argument applies to plane orders over \(k[z]\) and number orders over \(\mathbb Z\). It also identifies the limitation over a higher-dimensional normal base: defining \(\mathfrak D=(B:B^*)\) does not make \(B^*\mathfrak D=B\).

Here is a counterexample to (2.2) in that greater generality. Over an algebraically closed field of characteristic different from three, put

\[
 A=k[u,v],\quad u=x^3,\quad v=y^3,\quad
 B=k[x^3,x^2y,xy^2,y^3],\quad
 \theta=x^2y,\quad\eta=xy^2.
\]

The ring \(B\) is normal: it is the invariants of \(k[x,y]\) under scalar multiplication by cube roots of unity. An invariant fraction integral over it lies in the normal polynomial ring and remains invariant. Grouping exponents modulo three gives \(B=A\oplus A\theta\oplus A\eta\). Its fraction field over \(\operatorname{Frac}(A)\) is generated by \(\theta\), with separable polynomial \(T^3-u^2v\). The products are \(\theta^2=u\eta\), \(\eta^2=v\theta\), \(\theta\eta=uv\). The trace matrix in \(1,\theta,\eta\) therefore has its only nonzero entries \(3\) at \((1,1)\) and \(3uv\) at the two off-diagonal positions. Hence

\[
 B^*=A+A\frac{\theta}{uv}+A\frac{\eta}{uv},\qquad
 \mathfrak c=f'(\theta)B^*=(u,\theta)B.
\]

Since \(\theta/(uv)=1/\eta\) and \(\eta/(uv)=1/\theta\), one has \(\mathfrak D=\theta B\cap\eta B\). Give \(x,y\) degree one. This intersection has no nonzero element of degree below six: in degree three the two spaces are respectively \(k\theta\) and \(k\eta\), with zero intersection. The conductor has minimum degree three. Thus \(\mathfrak c\mathfrak D\) has minimum degree at least nine, whereas \(f'(\theta)=3\theta^2\) has degree six. Formula (2.2) fails, while (2.1) remains valid with all its stated hypotheses.

## 3. Ordinary multiple points

An ordinary \(r\)-fold point has multiplicity \(r\) and \(r\) distinct tangent lines. Choose local coordinates \(x,y\) with the \(x\)-projection transverse to each tangent. None of those tangents is \(x=0\), so their equations are \(y=a_i x\) with distinct \(a_i\in k\).

In the completed local ring put \(A=k[[x]]\). Substitution \(y=xv\), followed by division by \(x^r\), gives an equation whose reduction at \(x=0\) has the simple roots \(a_i\). Solving its coefficients successively, the nonzero derivative at each \(a_i\) gives a unique root \(v_i(x)\in A\). Thus the branches are

\[
 y=\phi_i(x)=xv_i(x),\qquad
 \phi_i-\phi_j=x\cdot\text{unit}\quad(i\ne j).
\]

Formal division by each \(y-\phi_i\) factors the curve equation as a unit times \(g(y)=\prod_i(y-\phi_i)\). The final factor is a unit because the initial form already has precisely those \(r\) factors. Since \(g\) is monic and its lower coefficients are divisible by \(x\), formal division gives

\[
 \widehat O=A[y]/(g),\qquad
 \widehat B=\prod_{i=1}^r A,
\tag{3.1}
\]

with inclusion \(q(y)\mapsto(q(\phi_i))_i\). Formal reduction of a power series by \(g\) converges \(x\)-adically and gives a unique remainder of degree less than \(r\); thus the stated polynomial presentation also represents the power-series quotient. The inclusion has nonzero Vandermonde determinant, so after inverting \(x\) it identifies the generic algebra with the product of the branch fields. The ring \(A^r\) is finite over the order and is integrally closed in that product, so it is its normalization. Lemma 1.3 proves that this is also the completed normalization of the original local curve ring.

We will use the following DVR matrix calculation. In a full-rank matrix over a DVR, choose an entry of least valuation and move it to the upper left by row and column swaps. It divides every entry, so invertible row and column operations clear its row and column. Repeat on the remaining square matrix. The result is a diagonal matrix with nonzero entries \(t^{b_i}\) times units, with \(b_i\ge0\). The cokernel is a direct sum of modules \(A/(t^{b_i})\), of total length \(\sum b_i\), exactly the determinant valuation. This proves the Smith length calculation used here and in Sections 4 and 5; no divisibility ordering of the diagonal entries is needed.

**Theorem 3.1.** At an ordinary \(r\)-fold point,

\[
 \mathfrak c_P=\mathfrak m_P^{r-1},\qquad
 \delta_P=\frac{r(r-1)}2.
\]

**Proof.** The matrix of (3.1), in the basis \(1,y,\ldots,y^{r-1}\), is a Vandermonde matrix. Its determinant is

\[
 \prod_{i<j}(\phi_j-\phi_i),
\]

of \(x\)-valuation \(r(r-1)/2\). Smith reduction of a full-rank matrix over the DVR \(A\) says that this valuation is the length of its cokernel. Length over \(A\) equals dimension over \(k\), giving the formula for \(\delta_P\).

Let \(e_i\) be the \(i\)-th component idempotent of \(\widehat B\). A vector \(c=(c_i)\) is in the conductor precisely when every \(c_i e_i\) is in \(\widehat O\), because the conductor is a \(\widehat B\)-ideal and these idempotents split it. The unique interpolating polynomial for \(c_i e_i\) is

\[
 c_i\frac{\prod_{j\ne i}(y-\phi_j)}
 {\prod_{j\ne i}(\phi_i-\phi_j)}.
\]

Its leading coefficient is integral only if \(v_x(c_i)\ge r-1\). Conversely that inequality makes every coefficient integral: the denominator is \(x^{r-1}\) times a unit. Therefore \(\widehat{\mathfrak c}=x^{r-1}\widehat B\).

The generators \(x^{r-1-j}y^j\), \(0\le j\le r-1\), of \(\widehat{\mathfrak m}^{r-1}\) have component vectors

\[
 x^{r-1}(v_i(x)^j)_i.
\]

This second Vandermonde matrix is invertible over \(A\), since its reduction has the distinct \(a_i\). These vectors span \(x^{r-1}\widehat B\) over \(A\). Hence \(\widehat{\mathfrak m}^{r-1}=\widehat{\mathfrak c}\).

The conductor is a finite kernel: choose module generators \(b_j\) for the normalization and test that \(c b_j\) belongs to \(O\) for each \(j\). Flat completion preserves this kernel and the finite quotient defining \(\delta\). Faithful flatness descends the ideal equality, and completion preserves the finite length. \(\square\)

This argument imposes no restriction on the characteristic beyond distinctness of the tangents. It does not say that every singularity has conductor a power of its maximal ideal.

## 4. The symmetry of a plane singularity and the genus

**Proposition 4.1.** For a plane curve singularity,

\[
 \dim_k(\widetilde O/\mathfrak c)=2\dim_k(\widetilde O/O)=2\delta.
\tag{4.1}
\]

**Proof.** Work in the completion and choose a generic transverse separating projection \(x\). Here is why it gives a free monogenic order over \(A=k[[x]]\). If the local multiplicity is \(r\), the equation has the form \(y^r u(y)+x h(x,y)\), with \(u(0)\ne0\). Hence \(y^r\in xO\), so the maximal-ideal and \(x\)-adic topologies are equivalent. Lifting the basis \(1,y,\ldots,y^{r-1}\) of \(O/xO\) successively in powers of \(x\) shows that these elements generate \(O\) over \(A\). The transverse parameter \(x\) is a nonzerodivisor. Thus this finite module is free over the DVR, of rank \(r\), and the lifted powers are a basis. Expressing \(y^r\) in that basis gives a monic polynomial and \(O=A[y]/(f)\). Its normalization \(B\) is a product of DVRs finite free over \(A\); the separating choice makes its generic algebra separable. Euler's lemma and (2.2) apply equally to that product. Denote length over \(A\) by \(\ell\).

For any full-rank lattice \(N\) with integral nondegenerate trace form, the trace matrix represents \(N\to N^*\). Thus \(\ell(N^*/N)\) is the valuation of its discriminant. For \(B\), since \(B^*=\mathfrak D^{-1}\), this length is \(\ell(B/\mathfrak D)\): factor the ideal on each DVR component and compare the lengths of opposite intervals of powers of its uniformizer. Changing from a basis of \(B\) to one of \(O\) multiplies the discriminant by the square of the determinant of the inclusion. Consequently

\[
 v_x(\operatorname{disc}O)=2\ell(B/O)+\ell(B/\mathfrak D).
\]

For a monogenic order its discriminant, up to sign, is the norm of \(f'(s)\). The valuation of that norm is \(\ell(B/f'(s)B)\), by the determinant of multiplication on the free module \(B\). From \(f'(s)B=\mathfrak c\mathfrak D\), adding ideal exponents on each component gives

\[
 \ell(B/f'(s)B)=\ell(B/\mathfrak c)+\ell(B/\mathfrak D).
\]

Subtract to obtain (4.1). The residue fields are \(k\), so all these finite lengths equal the corresponding \(k\)-dimensions. \(\square\)

**Proposition 4.2 (the genus correction).** For an integral plane curve \(C\) of degree \(d\), with normalization \(\nu:X\to C\),
\[
g(X)=\frac{(d-1)(d-2)}2-\sum_P\delta_P.
\tag{4.2}
\]
Here \(g(X)=h^1(X,\mathcal O_X)\), and the sum includes singularities at infinity.

**Proof.** The equation \(F\) of \(C\) gives
\[
0\longrightarrow\mathcal O_{\mathbb P^2}(-d)
\xrightarrow{\ F\ }\mathcal O_{\mathbb P^2}
\longrightarrow\mathcal O_C\longrightarrow0.
\]
Cohomology of projective space, Theorem 2.2, proves \(H^1(\mathbb P^2,\mathcal O(q))=0\) for every integer \(q\), \(H^0(\mathcal O)=k\), and \(H^2(\mathcal O)=0\). It gives \(H^0(\mathcal O_C)=k\) and
\[
H^1(\mathcal O_C)=H^2(\mathbb P^2,\mathcal O(-d)),\qquad
h^1(\mathcal O_C)=\frac{(d-1)(d-2)}2.
\]
For \(d\ge3\), the last group has a basis of reciprocal monomials with three strictly negative exponents summing to \(-d\); their number is \(\binom{d-1}{2}\). For \(d=1,2\) it is zero, agreeing with the same polynomial. This proves the plane arithmetic-genus formula.

Lemma 1.2 makes \(X\) smooth and projective. Projective coherent cohomology is finite-dimensional by Serre's theorems, Theorem 2.1. The finite-dimensional \(k\)-algebra \(H^0(\mathcal O_X)\) embeds in the function field and is a domain. Multiplication by a nonzero element is an injective endomorphism of this finite-dimensional space and hence surjective, so it is a field finite over \(k\); algebraic closure makes it \(k\).

The quotient \(Q=\nu_*\mathcal O_X/\mathcal O_C\) is supported at finitely many points: on an affine chart a nonzero conductor kills it, and a one-dimensional Noetherian domain has only finitely many primes over a nonzero ideal, since those primes are maximal and minimal over that ideal. Each stalk is a finite-length module, of \(k\)-dimension \(\delta_P\). Thus \(Q\) is a direct sum of sheaves carried by finite local schemes at those points; this follows by the Chinese remainder decomposition of a sufficiently high power of its annihilator. Each such scheme is affine and its map to \(C\) is affine. Cohomology of affine schemes, Theorems 2.2 and 3.2, therefore give \(H^{i>0}(Q)=0\) and \(h^0(Q)=\sum_P\delta_P\). The same affine-morphism theorem identifies the cohomology of \(\nu_*\mathcal O_X\) with that on \(X\). Taking Euler characteristics of
\[
0\longrightarrow\mathcal O_C\longrightarrow\nu_*\mathcal O_X
\longrightarrow Q\longrightarrow0
\]
now gives (4.2). There is no higher cohomology here: the two standard affine charts of \(\mathbb P^1\), pulled back by the finite function-field map of Lemma 1.2, give an acyclic two-member cover of \(X\); Theorem 3.1 of the affine-cohomology lesson kills degrees at least two. \(\square\)

**Theorem 4.3 (Riemann–Roch).** Let \(D\) be any divisor on the smooth projective curve \(X\), and let \(K_X\) be a divisor of its canonical line bundle. Then
\[
\ell(D)-\ell(K_X-D)=\deg D+1-g(X),
\qquad \ell(D)=h^0(X,\mathcal O_X(D)).
\]

**Proof.** We use the complete earlier Dualizing sheaves and Serre duality for projective schemes, Theorems 4.1 and 4.2. A smooth integral curve is equidimensional and Cohen–Macaulay: its closed local rings are DVRs, with a nonzerodivisor uniformizer giving depth one, and its generic local ring is a field. Its dualizing sheaf \(\omega_X\) is the canonical line described explicitly in Theorem 5.1 below. With \(F=\mathcal O_X(D)\), dimension one and \(i=0\), the proved duality is
\[
H^1(X,\mathcal O_X(D))^\vee
\simeq\operatorname{Hom}_X(\mathcal O_X(D),\omega_X)
=H^0(X,\omega_X(-D)).
\]
All spaces are finite-dimensional. At a closed point \(Q\), a uniformizer gives the exact sequence
\[
0\longrightarrow\mathcal O_X(D-Q)\longrightarrow\mathcal O_X(D)
\longrightarrow k(Q)\longrightarrow0,
\]
whose quotient is one-dimensional over \(k\). Euler characteristics consequently increase by one when a point is added. Adding and subtracting the finitely many coefficients of \(D\) gives
\(\chi(\mathcal O_X(D))=\chi(\mathcal O_X)+\deg D=1-g(X)+\deg D\).
Substitute the duality formula for \(h^1\) to obtain the assertion. This proof covers every divisor and every characteristic. The identification of \(\omega_X\) with regular differentials, including the singular plane model's conductor correction, is supplied next. Compare [Stacks, Tag 0BS6] and [Fulton, Section 8.6]. \(\square\)

Its role in point counting is explained in Weil's proof for curves and what is missing over the integers.

## 5. Adjoints and the residual theorem

An adjoint condition is a conductor condition. Let \(\nu:X\to C\) normalize an integral plane curve of degree \(d\). Its conductor \(\mathfrak c\), viewed as an ideal on the smooth curve \(X\), is invertible: each nonzero ideal in a DVR is a uniformizer power. Write
\[
\mathfrak c\mathcal O_X=\mathcal O_X(-\Delta),
\qquad \Delta=\sum_Q a_QQ\quad(a_Q\ge0).
\]
The conductor itself is a \(\nu_*\mathcal O_X\)-ideal, so \(\nu_*\mathcal O_X(-\Delta)=\mathfrak c\) as subsheaves of \(\nu_*\mathcal O_X\).

For a curve with only ordinary singularities, Theorem 3.1 gives
\[
\Delta=E=\sum_{P\in\operatorname{Sing}C}\ \sum_{Q\mapsto P}(r_P-1)Q.
\]
A form \(H\) is an **adjoint** when its restriction to \(C\) belongs locally to the conductor. In the ordinary case this says that \(H\) has multiplicity at least \(r_P-1\) at each singular point. The equivalence is exact: \(\mathfrak c_P=\mathfrak m_P^{r_P-1}\), and the local plane equation has order \(r_P\), so passing from the ambient local ring to the curve changes none of these order-\(r_P-1\) conditions. For a form whose restriction is nonzero, its pulled-back zero divisor contains \(\Delta\). Removing these forced zeros gives a section of
\[
L_m=\nu^*\mathcal O_C(m)(-\Delta).
\tag{5.1}
\]

**Theorem 5.1 (adjunction with the conductor).** The canonical line of the normalization is
\[
\boxed{\omega_X\simeq\nu^*\mathcal O_C(d-3)(-\Delta).}
\tag{5.2}
\]
It is the line of regular algebraic differentials. In particular, for ordinary singularities, \(\Delta=E\), and degree-\(d-3\) adjoints represent canonical sections. The assertion includes all characteristics, all degrees \(d\ge1\), and singularities beyond the ordinary case.

**Proof.** First identify the dualizing line without a differential calculation. The complete hypersurface adjunction proof in Dualizing sheaves and Serre duality for projective schemes, Theorem 5.1, gives \(\omega_C^\circ=\mathcal O_C(d-3)\), even for a singular curve. Put \(B=\nu_*\mathcal O_X\) and
\[
W=\mathcal H om_C(B,\omega_C^\circ),
\]
regarded as a sheaf on \(X\) using its \(B\)-action. Finite-map adjunction gives, for a coherent sheaf \(M\) on \(X\),
\[
\operatorname{Hom}_X(M,W)=
\operatorname{Hom}_C(\nu_*M,\omega_C^\circ)
=H^1(C,\nu_*M)^\vee=H^1(X,M)^\vee.
\]
Here the middle isomorphism is that earlier lesson's Theorem 4.1, and the last is the affine-morphism cohomology theorem. The first adjunction is elementary: over a finite algebra \(R\subset B\), a map \(M\to\operatorname{Hom}_R(B,N)\) goes to evaluation at one; its inverse takes \(\phi:M\to N\) to \(m\mapsto[b\mapsto\phi(bm)]\). These formulas are inverse and \(B\)-linear where required, and localize because the modules are finite over Noetherian rings. Taking the trace corresponding to the identity makes \(W\) a dualizing sheaf; uniqueness, Proposition 1.1 of that lesson, identifies it with \(\omega_X\).

On a chart where \(\omega_C^\circ\) has a frame,
\[
\operatorname{Hom}_R(B,R)=\{c\in L:cB\subset R\}=\mathfrak c.
\]
Indeed an \(R\)-linear map becomes multiplication by a field element after tensoring with the common fraction field; its value at one is that element, and the image condition is exactly the displayed test. Thus \(W=\mathfrak c\otimes\omega_C^\circ\). Interpreting this \(B\)-module on \(X\) gives (5.2), and proves its invertibility.

We now identify this line with regular differentials, making the trace formula's geometric role explicit. On an affine plane chart choose linear coordinates \(x,y\) such that its equation \(f(x,y)\) is monic in \(y\) and \(f_y\ne0\). Such a direction exists: its highest homogeneous part must be nonzero on the direction, and its directional derivative must not be the zero polynomial. The first excludes a proper polynomial zero set and the second a proper linear subspace. At least one partial derivative is nonzero, since over perfect \(k\) an irreducible polynomial with both partials zero would be a \(p\)-th power. The infinite field permits both conditions simultaneously. This gives a finite separable projection to \(\operatorname{Spec}A\), \(A=k[x]\), with plane order \(R=A[y]/(f)\) and finite normalization \(B\). Theorem 2.2 says
\[
\mathfrak c\,\frac{dx}{f_y}=B^*dx.
\tag{5.3}
\]
The field differential space is one-dimensional on \(dx\), by the unique extension of derivations through a separable generator proved in Kähler differentials, Lemma 6.1 and Theorem 6.2.

To calculate the right side at a branch above \(x=a\), complete. The finite-algebra Chinese remainder and DVR coefficient arguments in Lemma 1.3 split \(B\otimes_A k[[s]]\), \(s=x-a\), into branch rings \(T=k[[t]]\), with the given constants \(k\). Each is a finite free extension of complete DVRs: \(B\) is finite torsion-free over the PID \(A\), and each completed branch is a direct summand over the local ring \(k[[s]]\). Put \(e=v_t(s)\). Reduction modulo \(s\) has basis \(1,t,\ldots,t^{e-1}\); its dimension is also the free rank. Nakayama therefore makes these a basis over \(k[[s]]\) and gives \(T=k[[s]][t]\). The equation
\[
g(t,s)=0,\qquad
g(T,s)=T^e+\sum_{i<e}a_i(s)T^i
\]
has every \(a_i\) divisible by \(s\). Its constant coefficient has \(s\)-valuation one: up to sign it is the determinant of multiplication by \(t\), whose cokernel \(T/tT=k\) has length one over \(k[[s]]\); the DVR matrix reduction in Section 3 equates determinant valuation and cokernel length. Consequently \(g_s(t,s)\) is a unit, since its residue is the nonzero coefficient of \(s\) in \(a_0\). The generic extension is separable, since separable finite field algebras remain products of separable fields after this scalar extension; hence \(g_t(t,s)\ne0\).

The completed trace pairing is the scalar extension of its finite free matrix, and splits over the branch factors. Euler's lemma on this factor gives \(T^*=g_t(t,s)^{-1}T\). Formal differentiation of \(g(t,s(t))=0\) gives
\[
g_t(t,s)+g_s(t,s)s'(t)=0.
\]
Since \(g_s\) is a unit, \(g_tT=s'(t)T\), so
\[
T^*dx=g_t^{-1}T\,s'(t)dt=T\,dt.
\]
This calculation divides by neither \(e\) nor the characteristic; wild ramification is included. The differentials here are the completion of the finite algebraic differential module on the smooth curve. That module is free on \(dt\) locally: smoothness gives rank one, and the cotangent-space identification at a rational point sends \(dt\) to the nonzero class of the uniformizer, so Nakayama makes it a generator. Its derivation is continuous, since differentiating \(t^n b\) lowers valuation by at most one, and its extension to the completion is precisely formal differentiation. We are not identifying the unrestricted algebraic differentials of the Laurent-series field with this completed module. Faithfully flat completion of these finite lattices now descends \(B^*dx=\Omega_{B/k}\). Thus (5.3) is the exact regularity condition.

Finally this affine expression has the required projective twist. On \(Z\ne0\) put \(x=X/Z,y=Y/Z\), \(f=F(x,y,1)\), and \(\eta_Z=dx/f_y=-dy/f_x\), using a nonzero denominator. On \(X\ne0\) put \(u=Y/X,v=Z/X\), \(g=F(1,u,v)\), and \(\eta_X=du/g_v=-dv/g_u\). The relation \(f=v^{-d}g\), with \(x=v^{-1}\), gives on overlaps
\[
\eta_Z=v^{d-3}\eta_X,\qquad
\eta_X=x^{d-3}\eta_Z.
\]
The cyclic third chart has the same rule. These are exactly the frame transitions of \(\mathcal O_C(d-3)\). A linear change in an affine chart changes the residue frame by its nonzero constant Jacobian determinant and the inverse scalar of the equation; therefore the separating coordinates used for (5.3) generate the same fractional line there. Multiplication by the conductor makes these frames regular on \(X\), as proved above. This identifies its differential line with the line already found by duality, and completes the proof. Compare [Fulton, Sections 8.3 and 8.5] for the classical ordinary-point treatment. \(\square\)

**Proposition 5.2 (every normalized adjoint section lifts).** For every integer \(m\), restriction of degree-\(m\) adjoint forms surjects onto \(H^0(X,L_m)\). Its kernel consists of multiples of the equation \(F\) of \(C\). Negative-degree forms are zero.

**Proof.** Let \(\mathcal J\) be the inverse image of \(\mathfrak c\subset\mathcal O_C\) under \(\mathcal O_{\mathbb P^2}\to\mathcal O_C\). Then
\[
0\longrightarrow\mathcal O_{\mathbb P^2}(m-d)
\xrightarrow{\ F\ }\mathcal J(m)
\longrightarrow\nu_*L_m\longrightarrow0
\]
is exact. The last identification is checked in each twist frame, where its module is the conductor itself. Global sections of \(\mathcal J(m)\) are precisely the homogeneous forms satisfying the conductor condition; this uses the proved \(H^0(\mathbb P^2,\mathcal O(m))\) calculation. Theorem 2.2 of the projective-space cohomology lesson gives \(H^1(\mathbb P^2,\mathcal O(m-d))=0\) for every integer \(m-d\). The exact cohomology sequence therefore gives the asserted surjection and kernel, with no bound on \(m\). \(\square\)

**Theorem 5.3 (Max Noether's AF+BG theorem).** Let \(F,G\) be homogeneous plane forms of degrees \(a,b\) having no common component, and \(H\) a form of degree \(n\). There exist forms \(U,V\), of degrees \(n-a,n-b\), with
\[
H=UF+VG
\]
if and only if, at every point of \(V(F)\cap V(G)\), the dehomogenization of \(H\) lies in the local ideal generated by those of \(F,G\). A form of negative degree is zero. Set-theoretic vanishing at the intersection is insufficient when the intersection has multiplicity. Compare [Fulton, Section 5.5].

**Proof.** A nonzero constant among \(F,G\) makes both assertions immediate. We may therefore assume both degrees are positive. The hypothesis means \(F,G\) are relatively prime in \(k[X,Y,Z]\).

We use the elementary Gauss argument over the PID \(k[x]\). The content valuation at an irreducible \(q\) is the least valuation of a coefficient. Content valuations add under multiplication: divide out their common powers of \(q\) and reduce the two polynomials modulo \(q\), where their nonzero product remains nonzero in the polynomial ring over a field. Clearing denominators and dividing contents consequently turns any factorization over \(k(x)[y]\) into a factorization over \(k[x,y]\), up to a scalar. Factoring contents in the PID and primitive polynomials over \(k(x)\) also proves unique factorization in \(k[x,y]\). Repeating this argument with one more variable proves it in \(S\).

We first justify choosing a line avoiding their common zeros. On any affine chart their dehomogenizations \(f,g\) have no common nonconstant factor: homogenizing such a factor would give a common component of \(F,G\). The Gauss argument makes them relatively prime also in \(k(x)[y]\). The Euclidean algorithm there, followed by clearing denominators, gives \(Af+Bg=h(x)\ne0\), with \(A,B\in k[x,y]\). Interchanging the variables gives another identity with a nonzero right side in \(k[y]\). Thus both coordinates of a common zero belong to finite sets, and there are finitely many common zeros on that chart. The three charts prove finiteness in the projective plane. Over the infinite field \(k\), choose a line avoiding that finite set: the forbidden lines form finitely many proper linear subspaces of the three-dimensional space of line equations, whose union cannot cover it (the product of their defining nonzero linear polynomials is not the zero polynomial). Make this line \(Z=0\).

Put \(\bar F=F(X,Y,0)\), \(\bar G=G(X,Y,0)\). These are nonzero and relatively prime binary forms. Nonzero follows because a form divisible by \(Z\) would meet the other positive-degree form on that line. Relatively prime follows by factoring binary forms into linear factors over \(k\): a common factor gives a common point on the line. Binary polynomial rings are factorial by Gauss's lemma over the PID \(k[X]\); equivalently apply that lemma to factorization in \(k(X)[Y]\) and clear contents. Therefore
\[
\bar F\bar U+\bar G\bar V=0
\quad\Longrightarrow\quad
\bar U=\bar G\bar W,\quad \bar V=-\bar F\bar W.
\tag{5.4}
\]

Multiplication by \(Z\) is injective on \(S/(F,G)\), where \(S=k[X,Y,Z]\). In fact, if \(ZA=FU+GV\), reduce modulo \(Z\) and apply (5.4). Lift \(\bar W\) to \(W\in S\). Then \(U-GW=ZU_1\) and \(V+FW=ZV_1\); substituting and cancelling \(Z\) in the polynomial domain gives \(A=FU_1+GV_1\). This proves the injectivity assertion, for arbitrary polynomials and hence in every degree.

All intersection points are now on \(Z\ne0\). Put \(h=H(x,y,1)\). Its class in \(k[x,y]/(f,g)\) vanishes at every localization at a maximal ideal: the assumed local membership handles common zeros, and elsewhere one of \(f,g\) is a unit. The weak Nullstellensatz, The Nullstellensatz and Jacobson rings, Theorem 2.1, says these are all maximal ideals. An element of a module zero at every maximal localization is zero: if it were nonzero, its proper annihilator would lie in a maximal ideal, at which no element outside that ideal could annihilate it. Consequently \(h\in(f,g)\).

The homogeneous degree-zero part of \(S[1/Z]/(F,G)\) is this affine quotient. Clearing powers of \(Z\) gives \(Z^N H\in(F,G)\) for some \(N\ge0\). The proved injectivity cancels these powers successively, so \(H\in(F,G)\). Taking degree \(n\) of any representation gives precisely \(H=U_{n-a}F+V_{n-b}G\), with absent negative-degree pieces zero. The reverse implication follows by dehomogenizing this identity in each local ring. Every step works in arbitrary characteristic. \(\square\)

**Theorem 5.4 (Brill–Noether residual theorem).** Suppose \(C\) has only ordinary singularities, \(D,D'\) are effective divisors on \(X\) with \(D'\sim D\), and an adjoint \(H\) of degree \(m\), not vanishing identically on \(C\), satisfies
\[
\operatorname{div}_X(H)=E+D+T
\]
with \(T\) effective. Then an adjoint \(H'\) of the same degree satisfies \(\operatorname{div}_X(H')=E+D'+T\).

**Proof.** Choose \(h\in L^*\) with \(\operatorname{div}(h)=D'-D\). Multiply the pulled-back rational section defined by \(H\) by \(h\). Its divisor is exactly \(E+D'+T\). After removing \(E\), it is consequently a regular section of \(L_m\): at every DVR its valuation in that line's frame is nonnegative. Proposition 5.2 lifts this section to a degree-\(m\) adjoint form \(H'\). Its restriction is the specified nonzero section, so it does not vanish identically on \(C\), and its actual zero divisor is \(E+D'+T\). In particular the effective divisor \(T\) is unchanged. \(\square\)

This is the historical residual theorem about divisors and linear series [Fulton, Section 8.1], distinct from the residue theorem for meromorphic differentials. The proof also gives the same statement for arbitrary plane singularities if adjoints are defined by the conductor and \(E\) is replaced by \(\Delta\).

All cuts of \(L_m\) are linearly equivalent. Thus, if \(D+T\) and \(D'+T'\) arise from degree-\(m\) adjoints, then \(D\sim D'\) exactly when \(T\sim T'\). The residual theorem proves more than this class calculation: the replacement preserving the actual \(T\) is realized by a form of the same degree.

## 6. The ideal-theoretic counterpart

**Theorem 6.1.** For an order \(O\) in a finite Dedekind normalization \(B\), extension and contraction give inverse, product-preserving bijections

\[
 \{I\subseteq O:I+\mathfrak c=O\}
 \longleftrightarrow
 \{J\subseteq B:J+\mathfrak c=B\},
 \quad I\mapsto IB,\quad J\mapsto J\cap O.
\]

**Proof.** If \(I+\mathfrak c=O\), write \(1=a+c\), \(a\in I,c\in\mathfrak c\). For \(x\in IB\cap O\), \(ax\in I\), and \(cx\in I\), since writing \(x=\sum i_jb_j\) gives \(cx=\sum i_j(cb_j)\) with \(cb_j\in O\). Therefore \(x=ax+cx\in I\), proving \(IB\cap O=I\). Extension also gives \(IB+\mathfrak c=B\).

Conversely take \(J+\mathfrak c=B\), and write \(1=b+c\), \(b\in J,c\in\mathfrak c\). Then \(b=1-c\in O\), so \(b\in I=J\cap O\) and \(I+\mathfrak c=O\). For \(x\in J\), the term \(bx\) belongs to \(IB\), while \(cx\in O\cap J=I\); thus \(x\in IB\). The reverse inclusion is automatic. Finally extension preserves products, and products of ideals prime to \(\mathfrak c\) remain prime to it: multiply their representations of one modulo \(\mathfrak c\). The bijection therefore preserves products in both directions. \(\square\)

This single proof covers number and function fields. Outside the conductor, the local rings of \(O\) and \(B\) agree, so primes and their factorizations agree there. In a monogenic order, factoring its polynomial modulo such a base prime gives the usual Kummer–Dedekind factorization, assuming that no prime above it lies in the conductor [Sutherland, Lecture 6, Theorem 6.14 and Corollary 6.33].

Theorem 6.1 concerns ideals, and it need not identify their ideal class groups. The obstruction can be tested directly. Suppose \(J=aB\) is prime to \(\mathfrak c\), and put \(I=J\cap O\). Then \(I\) is principal in \(O\) precisely when some \(\epsilon\in B^\times\) makes the residue of \(a\epsilon\) an element of \((O/\mathfrak c)^\times\) inside \((B/\mathfrak c)^\times\). Here \(\times\) denotes units; \(B^*\) continues to denote the trace-dual lattice.

Indeed, if \(I=bO\), extension gives \(bB=aB\), hence \(b=a\epsilon\) for a unit \(\epsilon\). Since \(I+\mathfrak c=O\), its residue \(b\) is a unit in \(O/\mathfrak c\). Conversely the stated residue condition first gives \(a\epsilon\in O\): an element of \(B\) whose residue lies in \(O/\mathfrak c\) differs from an element of \(O\) by an element of \(\mathfrak c\subset O\). It also gives \(a\epsilon O+\mathfrak c=O\). This principal ideal has extension \(J\), so Theorem 6.1 identifies it with \(I\). This proves the unit-congruence obstruction [Conrad, Section 5].

For an explicit nontrivial obstruction take \(O=\mathbb Z[3i]\subset B=\mathbb Z[i]\). Its normalization is \(B\) by the quadratic integer-basis proof in Algebraic integers and rings of integers, Theorem 1.4. Testing an element \(a+3bi\) and its product with \(i\) gives conductor \(\mathfrak c=3B\). We have \(O/\mathfrak c=\mathbb F_3\), while \(B/\mathfrak c=\mathbb F_3[i]\) is a field of nine elements because \(T^2+1\) has no root in \(\mathbb F_3\). The ideal \(J=(1+i)B\) is prime to \(\mathfrak c\), since its generator has nonzero residue in that field. Units of \(B\) are exactly \(\pm1,\pm i\), as the multiplicative norm \(a^2+b^2\) must be one. Their residues multiplied by the two nonzero scalars of \(\mathbb F_3\) still give only \(\pm1,\pm i\). The residue of \(1+i\) belongs to none of them. Thus \(I=J\cap O\) is not principal, although \(IB\) is.

This \(I\) is invertible, so the example concerns ideal classes, not merely arbitrary ideals. At a maximal ideal containing \(\mathfrak c\), \(I+\mathfrak c=O\) gives \(I_{\mathfrak m}=O_{\mathfrak m}\). At any other maximal ideal a conductor element is invertible, so \(O_{\mathfrak m}\) is the corresponding normal local ring of \(B\), a DVR; its localized ideal is principal. To pass back to the ring, put \(I^{-1}=(O:I)\). It is finite: for \(0\ne b\in I\), it is a submodule of \(b^{-1}O\). Localization of this finite-colon test commutes with localization (clear denominators for a finite generating family of \(I\)). Consequently \((II^{-1})_{\mathfrak m}=O_{\mathfrak m}\) everywhere. The maximal-localization detection argument used in Theorem 5.3 then gives \(II^{-1}=O\). Its nonzero invertible class therefore maps to the zero class in \(B\).

For the geometric ideal-class statement, let \(U=\operatorname{Spec}B\subset X\). To a finite-support divisor \(D=\sum_{Q\in U}n_Q Q\) attach the fractional ideal

\[
 I_D=\prod_{Q\in U}\mathfrak P_Q^{n_Q}.
\]

Unique ideal factorization proves \(I_{D+D'}=I_DI_{D'}\). For \(h\in L^*\), the exponent of \(\mathfrak P_Q\) in \(hB\) is exactly \(v_Q(h)\). Consequently

\[
 [I_D]=[I_{D'}]\text{ in }\operatorname{Cl}(B)
 \Longleftrightarrow
 D-D'=\operatorname{div}_U(h)\text{ for some }h\in L^*.
\tag{6.1}
\]

Divisors away from the conductor can also be transferred through the ideals of \(O\) by Theorem 6.1. Products representing adjoint cuts, with their forced conductor contribution removed, obey the same cancellation law: if \([I_DI_T]=[I_{D'}I_{T'}]\), then \([I_D]=[I_{D'}]\) exactly when \([I_T]=[I_{T'}]\). This is the proved ideal-theoretic counterpart of the residual class calculation.

There is one necessary boundary distinction. Formula (6.1) uses only finite places. On \(X\) a rational function also has zeros and poles at infinity. Thus \(\operatorname{Cl}(B)\) is the projective divisor class group modulo the classes of points in \(X\setminus U\): a principal finite divisor becomes a divisor supported at infinity in the projective group, and conversely. To translate projective adjoint equivalence into ideal equivalence without losing information, retain the infinity divisor or impose its specified valuations on \(h\). Equality of affine ideal classes alone cannot prove projective linear equivalence.

These are the three views compared by Emmy Noether in her 1919 paper: integral ideals after choosing \(z\), divisors including all places, and adjoint forms on a plane model. For \(k=\mathbb C\), the normalized smooth projective curve is also the compact Riemann surface of the field: Complex analytic spaces and analytification, Lemma 2.2, Theorem 3.2 and Proposition 5.2, supply its complex manifold charts, Hausdorff and second-countable topology, and compactness. Smooth dimension one gives a Riemann surface. The conductor and ideal factorization are algebraic over any \(k\) used here; analytic periods and prescribed-ramification existence questions belong to the further questions in her part 8. Number fields have archimedean places too, but these are not extra closed points of a smooth projective curve over a constant field.

## 7. Four conductor computations

**The cusp.** For \(s^2=z^3\), put \(z=t^2,s=t^3\). Then \(O=k[t^2,t^3]\) and \(B=k[t]\). The latter is integral over \(O\), has the same fraction field, and is normal, so it is the normalization. Only the exponent one is missing among the nonnegative powers of \(t\): \(B/O\) has basis the class of \(t\). Thus \(\delta=1\), and

\[
 \mathfrak c=t^2B=(z,s)O.
\]

Indeed every power from two onwards is in \(O\), while a nonzero constant in the conductor would require \(t\in O\). In characteristic different from two, \(B/k[z]\) has different \((2t)\), and \(f_s=2s=2t^3\), so \(t^2B\cdot(2t)=2t^3B\). The conductor and \(\delta\) calculation itself works in characteristic two as well; that projection is then inseparable and its trace formula is unavailable.

**The node.** Assume \(\operatorname{char}k\ne2\) and let \(s^2=z^2(z+1)\). With \(t=s/z\),

\[
 z=t^2-1,\qquad s=t(t^2-1),\qquad B=k[t].
\]

Over \(A=k[z]\), the two lattices are \(B=A\oplus At\) and \(O=A\oplus Azt\). Their quotient is \((A/zA)t\), of dimension one. If \(c=a+bt\in B\) is in \(O\), then \(z\mid b\); requiring \(ct=at+b(z+1)\in O\) also forces \(z\mid a\). Thus

\[
 \mathfrak c=zB=(z,s)O,\qquad\delta=1.
\]

The two points of the normalization over the origin are \(t=1,-1\). The different for \(t^2-z-1\) is \((2t)\), and \(\mathfrak c\mathfrak D=(2zt)=(2s)\), the required derivative.

**An integral ordinary triple point.** Assume \(\operatorname{char}k\ne3\) and choose

\[
 s^3=z^3(1+z).
\]

The equation is irreducible over \(k(z)\): \(1+z\) is not a cube, since its order at \(z=-1\) is one. The initial form \(s^3-z^3\) has three distinct tangents. Put \(t=s/z\), so \(z=t^3-1\) and \(s=zt\). Its normalization is \(B=k[t]\). Over \(A=k[z]\),

\[
 B=A\oplus At\oplus At^2,\qquad
 O=A\oplus Azt\oplus Az^2t^2.
\]

The quotient has lengths one and two in its last two components, giving \(\delta=3\), entirely at the origin. The different is \((3t^2)\); since \(f_s=3s^2=3z^2t^2\), formula (2.2) gives

\[
 \mathfrak c=z^2B=(z^2,zs,s^2)O=\mathfrak m^2.
\]

The equality of the displayed ideal with \(z^2B\) follows already from its three \(A\)-basis vectors \(z^2,z^2t,z^2t^2\).

**The quadratic number order.** Put \(s=\sqrt{-3}\), \(O=\mathbb Z[s]\) and \(B=\mathbb Z[\omega]\), \(\omega=(1+s)/2\). The maximal-ring assertion is the quadratic integer-basis criterion, Algebraic integers and rings of integers, Theorem 1.4, since \(-3\equiv1\pmod4\). Since \(\omega^2=\omega-1\), an element \(a+b\omega\) and its product with \(\omega\) both belong to \(O\) exactly when \(a,b\) are even. Thus \(\mathfrak c=2B\). The polynomial of \(\omega\) is \(T^2-T+1\), so \(\mathfrak D_{B/\mathbb Z}=(2\omega-1)=(s)\). For the generator \(s\) of the smaller order, \(f=T^2+3\) and \(f'(s)=2s\). Therefore \(\mathfrak c\mathfrak D=2sB\). The order has lattice index two; its nonnormality is concentrated over two, whereas the maximal ring's different is supported over three. These are distinct phenomena.

## 8. Exercises

1. **Easy.** Verify the conductor-different identity for \(\mathbb Z[\sqrt{-3}]\) in its maximal order.
2. **Medium.** Compute the normalization, conductor and \(\delta\) of the cusp and the node.
3. **Medium.** Prove Euler's lemma directly for \(A=k[z]\), \(f=T^2-z^3\), assuming \(\operatorname{char}k\ne2\).
4. **Medium.** Find the genus of a nonsingular plane quartic and of an integral quartic whose only singularity is one ordinary node.
5. **Hard.** Prove the ordinary-point conductor formula and its \(\delta\) value using branch interpolation.

## 9. Solutions

**1.** In \(1,\omega\), membership in \(O\) requires the second coefficient even. For \(a+b\omega\), multiplication by \(\omega\) gives \(-b+(a+b)\omega\). Testing both elements therefore requires \(b\) even and \(a+b\) even, equivalently \(a,b\) even. This proves \(\mathfrak c=2B\). The derivative of \(T^2-T+1\) at \(\omega\) is \(2\omega-1=s\), so \(\mathfrak D=(s)\). Their product is \((2s)\), the derivative ideal for \(T^2+3\).

**2.** For the cusp, \(t=s/z\) lies in the fraction field and satisfies \(t^2=z\); the integral normal ring \(k[t]\) is its normalization. All \(t^j\), \(j\ge2\), lie in \(O\), while \(t\) does not. Hence \(B/O=kt\), and precisely \(t^2B\) multiplies every power of \(t\) into \(O\). It is \((z,s)O\).

For the node, \(t=s/z\) satisfies \(t^2=z+1\), so again the normalization is \(k[t]\). The power bases over \(k[z]\) give \(B/O=(k[z]/(z))t\), of length one. Write \(c=a+bt\). Membership of \(c\) in \(O\) requires \(z\mid b\), and membership of \(ct\) requires \(z\mid a\). These two tests suffice because \(1,t\) generate \(B\) over \(k[z]\). Thus the conductor is \(zB=(z,s)O\). These node statements require characteristic different from two, ensuring two distinct branches.

**3.** Every fraction-field element is \(x=a+bs\), with \(a,b\in k(z)\). Its traces against the basis \(1,s\) are \(2a\) and \(2bz^3\). Therefore \(x\in O^*\) exactly when \(2a,2bz^3\in A\). Since two is invertible, this lattice has basis \(1,s/z^3\) over \(A\), equivalently \(1/2,1/(2s)\) because \(s^2=z^3\). It is exactly \((2s)^{-1}O=f'(s)^{-1}O\).

**4.** The arithmetic genus for degree four is \((4-1)(4-2)/2=3\). A nonsingular quartic has every \(\delta_P=0\), hence genus three. The single ordinary node contributes \(\delta=1\) by Theorem 3.1 or the explicit node computation, so the normalization has genus two. The assertion specifies no other singularities, including at infinity.

**5.** Choose a transverse \(x\) and write the completed smooth branches as \(y=\phi_i(x)\), with pairwise differences \(x\) times units. The normalization is \(A^r\), and interpolation identifies the conductor component in position \(i\) with the multiples of \(\prod_{j\ne i}(\phi_i-\phi_j)\), hence with \(x^{r-1}A\). Necessity comes from the leading interpolation coefficient; sufficiency follows by integrality of every coefficient. The degree-\(r-1\) monomials in \(x,y\) map to \(x^{r-1}\) times a Vandermonde matrix in \(\phi_i/x\), which is invertible modulo \(x\). Thus \(\mathfrak m^{r-1}\) is this entire conductor. The inclusion matrix for the power basis is the Vandermonde in the \(\phi_i\), with determinant valuation \(\binom r2\); Smith reduction gives the quotient length. Finite kernels, finite lengths and faithful flatness transfer both conclusions from completion to the original local ring, as in Theorem 3.1.

## Proof dependencies

The separating parameter, finite curve normalization, smooth projective model and completed branches are proved in Lemmas 1.2 and 1.3, using the exact earlier Noether-normalization, completion, regular–smooth, properness and ample-embedding proofs linked there. Euler's lemma, the general conductor formula and its higher-dimensional limitation, ordinary multiple-point formulas, plane conductor symmetry and the genus correction are proved here. Proposition 4.2 uses the earlier projective-space monomial computation, Theorem 2.2, and affine-cohomology Theorems 2.2 and 3.2. Riemann–Roch follows from the earlier complete projective duality proof, Theorem 4.2, and the point-quotient calculation here. Theorem 5.1 proves global adjunction and its regular-differential interpretation, including wild branches; Proposition 5.2 supplies the actual lifting of adjoint sections. Theorems 5.3 and 5.4 prove AF+BG and the residual theorem. The ideal correspondence, unit-congruence obstruction and its nontrivial example, and the affine ideal-class statement are also proved above. The quadratic integer bases and complex-analytic interpretation have the exact earlier proof locators at their applications.

These links identify supplied programme proofs, not future providers. The linked Noether-normalization and Kähler-differential combined editions retain their declared GNU FDL terms, and the analytification lesson retains its stated component terms; their expression is not reproduced here. The new arguments in this lesson are independently written CC0. An export omitting a linked component has that external proof dependency; it cannot claim the complete programme's proof coverage.

## References

- **[Noether]** Emmy Noether, [*Die arithmetische Theorie der algebraischen Funktionen einer Veränderlichen in ihrer Beziehung zu den übrigen Theorien und zu der Zahlkörpertheorie*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN37721857X_0028/LOG_0022.pdf), Jahresbericht der Deutschen Mathematiker-Vereinigung **28** (1919), 182–203, parts 1–8; conductor and different on p. 189, part 7 on residual systems and ideal theory, pp. 199–201, and part 8 on further existence questions, pp. 201–203. [English edition](https://github.com/KokunoYumeto/emmy-noether-en).
- **[Stacks]** The Stacks Project, Tags [03GR](https://stacks.math.columbia.edu/tag/03GR), [030Q](https://stacks.math.columbia.edu/tag/030Q), [030W](https://stacks.math.columbia.edu/tag/030W), [09N2](https://stacks.math.columbia.edu/tag/09N2), [09NW](https://stacks.math.columbia.edu/tag/09NW), [0C3Q](https://stacks.math.columbia.edu/tag/0C3Q), [0C3U](https://stacks.math.columbia.edu/tag/0C3U), [0BYD](https://stacks.math.columbia.edu/tag/0BYD), [0BYE](https://stacks.math.columbia.edu/tag/0BYE), and [0BS6](https://stacks.math.columbia.edu/tag/0BS6). Read in the [AI Integrated Stacks Project English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html), whose AI-proposed corrections and additions have not been reviewed by the Stacks Project's maintainers.
- **[Fulton]** William Fulton, [*Algebraic Curves*](https://poisson.phc.dm.unipi.it/~camponovo/libri/Fulton%20-%20CurveBook), free edition, 28 January 2008, Sections 5.5 (AF+BG), 7.5 (ordinary branches and Noether conditions), 8.1 (residual theorem), 8.3 (adjoint sections), 8.5, Proposition 8 (canonical adjoints), and 8.6 (Riemann–Roch).
- **[Sutherland]** Andrew V. Sutherland, *Number Theory I*, MIT 18.785 lecture notes, Fall 2021: [Lecture 6](https://math.mit.edu/classes/18.785/2021fa/LectureNotes6.pdf), *Ideal norms and the Dedekind-Kummer theorem*, including the conductor of an order, and [Lecture 12](https://math.mit.edu/classes/18.785/2021fa/LectureNotes12.pdf), *The different and the discriminant*.
- **[Conrad]** Keith Conrad, [*The conductor ideal of an order*](https://kconrad.math.uconn.edu/blurbs/gradnumthy/conductor.pdf), Sections 3 and 5.
- **[Vakil]** Ravi Vakil, [*The Rising Sea: Foundations of Algebraic Geometry*](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf), public draft of 27 July 2024, Sections 13.5 (regular curves and DVRs), 18.4 (Riemann–Roch and arithmetic genus), and 18.5 (Serre duality).
- **[Milne FT]** J. S. Milne, *Fields and Galois Theory*, Theorem 9.27 (separating transcendence bases over a perfect field), [author’s course notes](https://www.jmilne.org/math/CourseNotes/FT.pdf).
