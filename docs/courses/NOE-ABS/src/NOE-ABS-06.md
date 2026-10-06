# Algebraic functions of one variable: conductors and adjoints

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A singular plane curve can put several branches at one point or omit functions that are regular on its normalization. The conductor measures that omission. Trace duality relates it to the different; at an ordinary multiple point it gives precisely the vanishing conditions of an adjoint curve.

We assume Noether's axioms for Dedekind domains, Three differents, finite normalization for curves, and elementary divisors on a smooth curve. Throughout the geometric discussion, \(k\) is algebraically closed and the curves are integral. Arithmetic analogues use orders in number fields, as in **Orders in number fields and their Picard groups**. Prime factorization in a monogenic order is governed by Decomposition of primes in extensions, Theorem 5.3 (Kummer–Dedekind). Geometric results used without proof are identified when they occur. Basic references are [Noether], [Fulton], [Stacks] and [Vakil].

## 1. A function field, a plane model and its normalization

Let \(L/k\) be finitely generated of transcendence degree one. A nonconstant \(z\in L\) makes \(L/k(z)\) finite. The integral closure \(B\) of \(k[z]\) in \(L\) is finite and Dedekind. Finiteness here follows from the normalization theorem over a Nagata base, applied to \(k[z]\) [Stacks, Tag 03GR]; when the extension is separable it also follows from the trace finiteness proof in the first lesson. The prime ideals of \(B\) give the places where \(z\) is finite. The places at infinity are obtained from the normalization over \(k[1/z]\). Together they are the closed points of the smooth projective curve with function field \(L\).

For trace arguments choose \(z\) **separating**, so that \(L/k(z)\) is separable. Such a choice exists over the perfect field \(k\) [Milne FT, Theorem 9.27]. Tags 030Q and 030W describe separating bases and characterize separability; their hypotheses alone do not assert existence over a perfect ground field. An arbitrary transcendental element need not be separating in positive characteristic.

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

where \(\widetilde{O_P}\) denotes the semilocal normalization. It is finite and supported at the singular points [Stacks, Section 0C3Q].

**Proposition 1.1.** The conductor is the unit ideal at a point exactly when that point is nonsingular.

**Proof.** A conductor equal to the unit ideal means \(1\cdot\widetilde{O_P}\subseteq O_P\), hence equality of the two rings. Conversely equality makes the conductor the unit ideal. A one-dimensional Noetherian normal local domain is a DVR; a nonsingular point on a curve over a perfect field has a regular one-dimensional local ring, also a DVR. These implications give the equivalence. Thus \(\operatorname{Supp}(B/O)\), the vanishing locus of its annihilator, is exactly the singular locus. \(\square\)

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

with inclusion \(q(y)\mapsto(q(\phi_i))_i\). Formal reduction of a power series by \(g\) converges \(x\)-adically and gives a unique remainder of degree less than \(r\); thus the stated polynomial presentation also represents the power-series quotient. The normalization description is the branch description of a curve with these smooth formal branches. Finite normalization and completion commute here because curves of finite type over a field are excellent; equivalently, completing each normalized branch DVR gives exactly the factors in (3.1).

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

Let \(C\subset\mathbb P^2_k\) be an integral curve of degree \(d\), and let \(X\to C\) be its normalization. Its arithmetic genus is \((d-1)(d-2)/2\) [Stacks, Tag 0BYD]. The exact sequence

\[
 0\to\mathcal O_C\to\nu_*\mathcal O_X\to Q\to0
\]

has \(\dim_k H^0(Q)=\sum_P\delta_P\); \(Q\) has finite support and no higher cohomology. Both curves have only constant global regular functions. Taking Euler characteristics therefore proves

\[
 g(X)=\frac{(d-1)(d-2)}2-\sum_P\delta_P.
\tag{4.2}
\]

Over our perfect field, the normalized projective curve is smooth and this is its geometric genus [Stacks, Section 0BYE]. The dimension theorem that completes the picture is Riemann–Roch:

\[
 \ell(D)-\ell(K_X-D)=\deg D+1-g(X),
\]

where \(\ell(D)=\dim_k H^0(X,\mathcal O_X(D))\) and \(K_X\) is a canonical divisor. This is a stated input [Stacks, Tag 0BS6, in Section 0B5B; Vakil, Section 18.4 and the duality form of Riemann–Roch]. Its role in point counting is explained in Weil's proof for curves and what is missing over the integers.

## 5. Adjoints and the residual theorem

An adjoint condition is a conductor condition. For a projective plane curve \(C\) with only ordinary singularities, write

\[
 E=\sum_{P\in\operatorname{Sing}C}\ \sum_{Q\mapsto P}(r_P-1)Q
\]

on its normalization \(X\). Theorem 3.1 says that a form \(H\) is an **adjoint** precisely when it has multiplicity at least \(r_P-1\) at each singular point. Its pulled-back section has a zero divisor containing \(E\). Thus adjoints of degree \(m\) give residual divisors in

\[
 \nu^*\mathcal O_C(m)(-E).
\tag{5.1}
\]

This removes the forced zeros from the branch divisor of the form. In degree \(d-3\), adjunction identifies (5.1) with the canonical bundle of \(X\) [Fulton, Section 8.5, Proposition 8; the adjoint-section description is Section 8.3, Corollary 3(a)]. On an affine chart its sections are represented by \(H\,dz/f_s\); the conductor identity (2.2) supplies the regularity condition at the singular branches. The degree of the adjoint form also accounts for its behavior at infinity. We use the global adjunction statement as a cited input.

**Max Noether's AF+BG theorem (stated).** Let \(F,G\) be homogeneous plane forms of degrees \(a,b\) having no common component, and \(H\) a form of degree \(n\). There exist forms \(U,V\), of degrees \(n-a,n-b\), with

\[
 H=UF+VG
\]

if and only if, at every point of \(V(F)\cap V(G)\), the dehomogenization of \(H\) lies in the local ideal generated by those of \(F,G\). A form of negative degree is interpreted as zero [Fulton, Section 5.5, *Max Noether's Fundamental Theorem*]. Set-theoretic vanishing at the intersection is insufficient when the intersection has multiplicity.

**Brill–Noether residual theorem (stated).** Suppose \(C\) has only ordinary singularities, \(D,D'\) are effective divisors on \(X\) with \(D'\sim D\), and an adjoint \(H\) of degree \(m\) satisfies

\[
 \operatorname{div}_X(H)=E+D+T
\]

with \(T\) effective. Then an adjoint \(H'\) of the same degree satisfies \(\operatorname{div}_X(H')=E+D'+T\) [Fulton, Section 8.1, *Residue Theorem*]. This is the historical residual theorem about divisors and linear series; it is distinct from the residue theorem for meromorphic differentials.

The conclusion keeps the residual divisor \(T\) fixed, which is stronger than merely keeping its class fixed. The class calculation behind it is immediate: all cuts of (5.1) are linearly equivalent, so if \(D+T\) and \(D'+T'\) arise from degree-\(m\) adjoints, then \(D\sim D'\) if and only if \(T\sim T'\). The theorem asserts that the effective replacement can actually be cut by a form of that same degree.

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

Theorem 6.1 is a bijection of ideals. It does not identify all the ideal class groups of the two rings: a generator in \(B\) need not be a permitted generator of an invertible ideal of \(O\). This is the unit-congruence obstruction for arithmetic orders [Conrad, Section 5].

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

These are the three views compared by Emmy Noether in her 1919 paper: integral ideals after choosing \(z\), divisors including all places, and adjoint forms on a plane model. For \(k=\mathbb C\), the normalized smooth projective curve is also the compact Riemann surface of the field. The conductor and ideal factorization are algebraic over any \(k\) used here; analytic periods and prescribed-ramification existence questions belong to the further questions in her part 8. Number fields have archimedean places too, but these are not extra closed points of a smooth projective curve over a constant field.

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

**The quadratic number order.** Put \(s=\sqrt{-3}\), \(O=\mathbb Z[s]\) and \(B=\mathbb Z[\omega]\), \(\omega=(1+s)/2\). Since \(\omega^2=\omega-1\), an element \(a+b\omega\) and its product with \(\omega\) both belong to \(O\) exactly when \(a,b\) are even. Thus \(\mathfrak c=2B\). The polynomial of \(\omega\) is \(T^2-T+1\), so \(\mathfrak D_{B/\mathbb Z}=(2\omega-1)=(s)\). For the generator \(s\) of the smaller order, \(f=T^2+3\) and \(f'(s)=2s\). Therefore \(\mathfrak c\mathfrak D=2sB\). The order has lattice index two; its nonnormality is concentrated over two, whereas the maximal ring's different is supported over three. These are distinct phenomena.

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

## What this lesson does not prove

The inputs are finite normalization and its completed branch description for curves over a field, existence of a separating transcendence basis, the projective smooth model, the plane arithmetic genus formula [Stacks, Tag 0BYD], Riemann–Roch [Stacks, Tag 0BS6], global adjunction for plane adjoints, Max Noether's AF+BG theorem and the Brill–Noether residual theorem with the Fulton locators above. Euler's lemma, the general conductor formula and its limitation, the ordinary multiple-point formulas, plane conductor symmetry, the normalization correction to the genus, the ideal correspondence and the affine ideal-class statement are proved here.

## References

- **[Noether]** Emmy Noether, [*Die arithmetische Theorie der algebraischen Funktionen einer Veränderlichen in ihrer Beziehung zu den übrigen Theorien und zu der Zahlkörpertheorie*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN37721857X_0028/LOG_0022.pdf), Jahresbericht der Deutschen Mathematiker-Vereinigung **28** (1919), 182–203, parts 1–8; conductor and different on p. 189, part 7 on residual systems and ideal theory, pp. 199–201, and part 8 on further existence questions, pp. 201–203. [English edition](https://github.com/KokunoYumeto/emmy-noether-en).
- **[Stacks]** The Stacks Project, Tags [03GR](https://stacks.math.columbia.edu/tag/03GR), [030Q](https://stacks.math.columbia.edu/tag/030Q), [030W](https://stacks.math.columbia.edu/tag/030W), [09N2](https://stacks.math.columbia.edu/tag/09N2), [09NW](https://stacks.math.columbia.edu/tag/09NW), [0C3Q](https://stacks.math.columbia.edu/tag/0C3Q), [0C3U](https://stacks.math.columbia.edu/tag/0C3U), [0BYD](https://stacks.math.columbia.edu/tag/0BYD), [0BYE](https://stacks.math.columbia.edu/tag/0BYE), and [0BS6](https://stacks.math.columbia.edu/tag/0BS6). Read in the [AI Integrated Stacks Project English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html), whose AI-proposed corrections and additions have not been reviewed by the Stacks Project's maintainers.
- **[Fulton]** William Fulton, [*Algebraic Curves*](https://poisson.phc.dm.unipi.it/~camponovo/libri/Fulton%20-%20CurveBook), free edition, 28 January 2008, Sections 5.5 (AF+BG), 7.5 (ordinary branches and Noether conditions), 8.1 (residual theorem), 8.3 (adjoint sections), 8.5, Proposition 8 (canonical adjoints), and 8.6 (Riemann–Roch).
- **[Sutherland]** Andrew V. Sutherland, *Number Theory I*, MIT 18.785 lecture notes, Fall 2021: [Lecture 6](https://math.mit.edu/classes/18.785/2021fa/LectureNotes6.pdf), *Ideal norms and the Dedekind-Kummer theorem*, including the conductor of an order, and [Lecture 12](https://math.mit.edu/classes/18.785/2021fa/LectureNotes12.pdf), *The different and the discriminant*.
- **[Conrad]** Keith Conrad, [*The conductor ideal of an order*](https://kconrad.math.uconn.edu/blurbs/gradnumthy/conductor.pdf), Sections 3 and 5.
- **[Vakil]** Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, Sections 13.5 (regular curves and DVRs), 18.4 (Riemann–Roch and arithmetic genus), and 18.5 (Serre duality).
- **[Milne FT]** J. S. Milne, *Fields and Galois Theory*, Theorem 9.27 (separating transcendence bases over a perfect field), [author’s course notes](https://www.jmilne.org/math/CourseNotes/FT.pdf).
