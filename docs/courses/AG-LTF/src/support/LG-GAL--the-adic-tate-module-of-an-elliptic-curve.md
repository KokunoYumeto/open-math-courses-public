# The ℓ-adic Tate module of an elliptic curve

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Point counts on an elliptic curve become traces of a two-dimensional representation. The determinant comes from a pairing; the trace comes from the kernel of a geometric endomorphism. The positivity of its degree then bounds the point count. This chapter develops those three connections, so that the passage from geometry to a Galois representation has a concrete meaning.

We assume Frobenius elements and determination by traces and the elementary geometry in *Complex tori, elliptic curves and the moduli interpretation of modular curves*. Because complex uniformization does not supply positive-characteristic facts, we state the additional facts about algebraic elliptic curves explicitly below. Basic references are [Sutherland 2023] and [Milne 2021]. The Tate module is covariant, and Frobenius is arithmetic. In particular its cyclotomic determinant at a good prime is \(p\), not \(p^{-1}\).

## 1. The geometric facts we need

An elliptic curve over a field \(K\) is a smooth projective geometrically connected genus-one curve with a specified \(K\)-point \(O\), equipped with its algebraic group law. A nonzero homomorphism of elliptic curves is an **isogeny**. It is finite and surjective, and its degree is a positive integer. The zero homomorphism has degree zero. These assertions include inseparable isogenies in positive characteristic.

Here are the elliptic-curve facts used in this chapter, with their precise scope.

1. Multiplication by an integer \(m\ne0\) has degree \(m^2\). If \(m\) is prime to the characteristic, it is separable and \(E[m](\bar K)\simeq(\mathbb Z/m\mathbb Z)^2\). Multiplication by \(\ell\) maps \(E[\ell^{a+1}]\) onto \(E[\ell^a]\).
2. Every isogeny \(\alpha:E\to E'\) has a dual \(\widehat\alpha:E'\to E\), with \(\widehat\alpha\alpha=[\deg\alpha]\) and \(\alpha\widehat\alpha=[\deg\alpha]\).
3. For \(m\) prime to the characteristic, the Weil pairing \(e_m:E[m]\times E[m]\to\mu_m\) is perfect, bilinear, alternating and Galois equivariant. It is compatible with the transition maps between ℓ-power torsion groups. It satisfies
   \[
   e_m(\alpha P,Q)=e_m(P,\widehat\alpha Q)
   \tag{1}
   \]
   for an isogeny between the corresponding two curves.
4. Good reduction over a complete discretely valued field means that the elliptic curve extends to a smooth proper elliptic group scheme over its valuation ring. Multiplication by an integer prime to the residue characteristic on this group scheme is finite étale of degree \(m^2\). A finite étale scheme over a strictly henselian local ring is a disjoint union of copies of that ring.

Items 1–3 are [Sutherland 2023, §§5, 6 and 23], with the ℓ-adic form of (1) in [Milne 2008, Chapter I, §13]. Good reduction and prime-to-residue-characteristic torsion are [Milne 2021, Chapter II, §§4 and 7]. These are prerequisites, rather than a replacement for the arithmetic deductions proved here. A Weierstrass equation is used to compute examples, and its discriminant tests nonsingularity.

## 2. A representation from all ℓ-power torsion

Assume \(\ell\ne\operatorname{char}K\). Define
\[
 T_\ell E=\varprojlim_a E[\ell^a](\bar K),
 \qquad V_\ell E=T_\ell E\otimes_{\mathbb Z_\ell}\mathbb Q_\ell,
\]
with transition map multiplication by \(\ell\). Choosing a basis at level \(\ell\), lift it successively to bases at every higher level. A lift is a basis because its reduction is a basis and each torsion group is free of rank two over \(\mathbb Z/\ell^a\mathbb Z\). Thus
\[
 T_\ell E\simeq\mathbb Z_\ell^2,
 \qquad V_\ell E\simeq\mathbb Q_\ell^2.
\]
Galois acts on every torsion group and respects the transition maps. The resulting homomorphism
\[
 \rho_{E,\ell}:G_K\longrightarrow\operatorname{GL}(T_\ell E)
\]
is continuous: prescribing the matrix modulo \(\ell^a\) prescribes its action on a finite set of algebraic points and hence is an open condition.

The compatible Weil pairings give a perfect alternating pairing
\[
 T_\ell E\times T_\ell E\longrightarrow\mathbb Z_\ell(1).
 \tag{2}
\]
Here \(\mathbb Z_\ell(1)=\varprojlim_a\mu_{\ell^a}\), with the Galois action of the cyclotomic character.

**Theorem 2.1 (cyclotomic determinant).** For an elliptic curve over any field \(K\), with \(\ell\ne\operatorname{char}K\),
\[
 \det\rho_{E,\ell}=\chi_\ell|_{G_K}.
\]

**Proof.** A perfect alternating pairing on a rank-two module identifies its exterior square with the target of the pairing. Thus (2) identifies \(\bigwedge^2T_\ell E\) with \(\mathbb Z_\ell(1)\). On the exterior square a matrix acts by its determinant; on the target Galois acts by \(\chi_\ell\). Equivariance gives their equality. Equivalently, in a basis \(P,Q\) modulo \(\ell^a\), bilinearity and alternation give \(e_{\ell^a}(gP,gQ)=e_{\ell^a}(P,Q)^{\det g}\), whereas Galois equivariance gives exponent \(\chi_\ell(g)\). Perfection makes the pairing value primitive, so the exponents agree modulo \(\ell^a\) for every \(a\). \(\square\)

The same argument applied to an endomorphism gives a second interpretation of determinant.

**Theorem 2.2 (degree as determinant).** For every endomorphism \(\alpha\) of an elliptic curve and every \(\ell\) different from the field characteristic,
\[
 \det(\alpha\mid T_\ell E)=\deg\alpha
 \quad\text{in }\mathbb Z_\ell.
 \tag{3}
\]

**Proof.** The zero endomorphism satisfies (3). Otherwise it is an isogeny. Substitute \(Q=\alpha Q'\) into (1). The dual-isogeny identity gives
\[
 e_{\ell^a}(\alpha P,\alpha Q')
 =e_{\ell^a}(P,\widehat\alpha\alpha Q')
 =e_{\ell^a}(P,Q')^{\deg\alpha}.
\]
In a torsion basis the left side is also \(e_{\ell^a}(P,Q')^{\det\alpha}\). Its primitive order gives \(\det\alpha\equiv\deg\alpha\pmod{\ell^a}\) for every \(a\). Taking the inverse limit proves equality, including for an inseparable isogeny. \(\square\)

The action of \(\operatorname{End}(E)\) on \(T_\ell E\) is faithful. Indeed an endomorphism with zero action kills every \(E[\ell^a]\), since the projections from the inverse limit are surjective. A nonzero endomorphism is an isogeny and has a finite geometric kernel, which cannot contain these groups of unbounded size. Consequently a polynomial identity on the Tate module is also an identity of elliptic-curve endomorphisms.

## 3. Good reduction makes Frobenius visible

Let \(K_v\) have residue field \(\mathbb F_q\) of characteristic \(p\), and let \(E/K_v\) have good reduction \(\widetilde E\). Assume \(\ell\ne p\).

**Theorem 3.1 (unramified torsion).** Reduction identifies the prime-to-\(p\) torsion groups equivariantly:
\[
 E[\ell^a](\overline{K_v})\simeq
 \widetilde E[\ell^a](\overline{\mathbb F}_q).
\]
Inertia acts trivially on \(T_\ell E\), and arithmetic Frobenius acts through the endomorphism \(\varphi:(x,y)\mapsto(x^q,y^q)\) of \(\widetilde E\).

**Proof.** On the good elliptic group scheme, the kernel of multiplication by \(\ell^a\) is finite étale. Pass to the strict henselization of the valuation ring, whose residue field is \(\overline{\mathbb F}_q\). This kernel is a disjoint union of \(\ell^{2a}\) sections. Reduction gives a bijection between these sections and the torsion points of the special fibre. Their generic points are already defined over the maximal unramified extension, so inertia fixes every one of them. The bijection respects Galois actions and addition. On the residue field arithmetic Frobenius is the \(q\)-power map, which acts on coordinates as \(\varphi\). The identifications also commute with multiplication by \(\ell\), so they pass to the Tate module. \(\square\)

To compute the trace we work entirely on the special fibre. The degree of its \(q\)-power Frobenius is \(q\). Its differential is zero. Consequently the differential of \(1-\varphi\) is the identity, so \(1-\varphi\) is a separable isogeny. Its geometric kernel consists exactly of the \(\mathbb F_q\)-points. For a separable isogeny, degree equals the number of geometric points in its kernel. Thus
\[
 \#\widetilde E(\mathbb F_q)=\deg(1-\varphi).
 \tag{4}
\]

**Theorem 3.2 (Frobenius polynomial).** Put \(a_q=q+1-\#\widetilde E(\mathbb F_q)\). Then
\[
 \det(X-\varphi\mid V_\ell\widetilde E)=X^2-a_qX+q.
 \tag{5}
\]
For \(E/\mathbb Q\) and a prime \(p\ne\ell\) of good reduction, this is the arithmetic-Frobenius polynomial of \(\rho_{E,\ell}\). It is independent of \(\ell\).

**Proof.** Write \(t=\operatorname{tr}(\varphi\mid V_\ell\widetilde E)\). Formula (3) gives \(\det\varphi=q\). Since the space has dimension two,
\[
 \det(1-\varphi)=1-t+q.
\]
Equations (3) and (4) give \(\#\widetilde E(\mathbb F_q)=1-t+q\), so \(t=a_q\). This proves (5). Theorem 3.1 identifies this operator with arithmetic Frobenius on the original Tate module. Both coefficients of (5) are integer point-counting data, so no choice of \(\ell\ne p\) affects them. \(\square\)

This establishes more than the determinant assertion alone. In particular, it identifies the trace as an integer without needing to show separately that an endomorphism has an integral trace.

## 4. Positivity gives the Hasse bound

**Theorem 4.1 (Hasse).** Every elliptic curve over \(\mathbb F_q\) satisfies
\[
 |q+1-\#E(\mathbb F_q)|\le2\sqrt q.
\]

**Proof.** Let \(a=q+1-\#E(\mathbb F_q)\). For integers \(m,n\), the endomorphism \([m]+[n]\varphi\) has nonnegative degree. By Theorem 2.2 and the trace and determinant in (5),
\[
 0\le\deg([m]+[n]\varphi)
 =\det(m+n\varphi)=m^2+amn+qn^2.
 \tag{6}
\]
If \(a^2>4q\), the real polynomial \(z^2+az+q\) is negative on a nonempty open interval around \(-a/2\). That interval contains a rational number \(m/n\), with \(n\ne0\). Multiplying its negative value by \(n^2\) contradicts (6). Hence \(a^2\le4q\). \(\square\)

The two roots \(\alpha,\beta\) of (5) have complex absolute value \(\sqrt q\). If the discriminant is negative, they are complex conjugates with product \(q\). If it is zero, both are \(\pm\sqrt q\). The bound excludes a positive discriminant. This observation will control convergence of the elliptic-curve Euler product.

The cohomological normalization deserves care. There are natural identifications
\[
 H^1_{\mathrm{et}}(E_{\bar K},\mathbb Q_\ell)
 \simeq(V_\ell E)^\vee\simeq V_\ell E(-1).
\]
The second follows from the Weil pairing. Arithmetic Frobenius on the dual has the inverses of the eigenvalues in (5). Geometric Frobenius on the dual has the original eigenvalues. These identities explain which operator the cohomological trace formula uses; they do not change our covariant convention.

## 5. Two point-counting examples

For a nonsingular projective Weierstrass cubic there is one point at infinity. Count the affine points one \(x\)-coordinate at a time.

**Example 5.1.** Let \(E:y^2+y=x^3-x^2\). Its integral discriminant is \(-11\), so the displayed equation is nonsingular modulo each prime other than \(11\). In increasing order \(x=0,1,\dots,p-1\), the numbers of \(y\)-solutions are:

| \(p\) | Numbers of solutions for successive \(x\) | \(\#E(\mathbb F_p)\) | \(a_p\) |
|---|---|---|---|
| 2 | 2, 2 | 5 | −2 |
| 3 | 2, 2, 0 | 5 | −1 |
| 5 | 2, 2, 0, 0, 0 | 5 | 1 |
| 7 | 2, 2, 0, 0, 2, 2, 1 | 10 | −2 |
| 13 | 2, 2, 2, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0 | 10 | 4 |

For odd \(p\), these entries are obtained by setting \(u=2y+1\): one solves \(u^2=1+4x^3-4x^2\). A zero right side gives one solution, a nonzero square gives two, and a nonsquare gives none. At \(p=2\), the left side \(y^2+y\) is zero for both elements and so is \(x^3-x^2\).

The good-prime traces coincide with the coefficients of \(f=\eta(z)^2\eta(11z)^2\). Indeed
\[
 f=q\prod_{n\ge1}(1-q^n)^2(1-q^{11n})^2.
\]
Multiplying only factors with exponent at most \(12\) gives
\[
 f=q-2q^2-q^3+2q^4+q^5+2q^6-2q^7
 -2q^9-2q^{10}+q^{11}-2q^{12}+4q^{13}+O(q^{14}).
\]
Thus the prime coefficients through \(13\) agree with the counts. The absence of a \(q^8\) term means its coefficient is zero. Identification with a modular form is treated in *Galois representations of weight-two newforms*; this calculation itself only multiplies a finite product.

At \(11\) the cubic is singular, so Theorem 3.2 does not apply. Its projective point count is \(11\), computed from the affine counts \(2,2,0,0,0,2,0,1,1,0,2\) and the point at infinity. Its bad-prime coefficient is \(1\), as will also follow from split multiplicative reduction. Counting a singular cubic must not be presented as good reduction.

**Example 5.2.** Let \(E':y^2=x^3-x\), with discriminant \(64\). At odd primes,
\[
 \#E'(\mathbb F_p)=p+1+\sum_{x\in\mathbb F_p}
 \left(\frac{x^3-x}{p}\right),
\]
where the Legendre symbol is zero at zero. When \(p\equiv3\pmod4\), the substitution \(x\mapsto-x\) negates the symbol, since \((-x)^3-(-x)=-(x^3-x)\) and \(\left(\frac{-1}{p}\right)=-1\). The sum is therefore zero, and \(a_p=0\) for every such prime, not just the small examples. In particular \(\#E'(\mathbb F_p)=p+1\) at \(p=3,7,11,19,23\).

At \(5\) the successive affine counts are \(1,1,2,2,1\), giving \(\#E'=8\) and \(a_5=-2\). At \(13\) they are \(1,1,0,0,0,2,0,0,2,0,0,0,1\), giving \(\#E'=8\) and \(a_{13}=6\). Each satisfies the Hasse bound. The curve has bad reduction at \(2\), which is excluded from these statements.

## 6. Exercises and complete solutions

**Exercise 6.1 (easy).** Count the points of \(y^2+y=x^3-x^2\) at every prime at most \(13\), distinguishing the bad prime.

**Solution.** Use the six lists in Example 5.1. Their affine totals at \(2,3,5,7,11,13\) are \(4,4,4,9,10,9\); adding the unique point at infinity gives \(5,5,5,10,11,10\). The good-prime traces are respectively \(-2,-1,1,-2,4\) with \(11\) omitted. The discriminant \(-11\) identifies \(11\) as bad. Its singular cubic has \(11\) projective points; the associated multiplicative coefficient is \(1\), but its local factor has degree one rather than the degree-two good factor.

**Exercise 6.2 (medium).** Derive \(\deg\alpha=\det(\alpha\mid T_\ell E)\) from the Weil pairing, allowing an inseparable endomorphism.

**Solution.** A nonzero endomorphism is an isogeny and has a dual. Equation (1) applied to \(\alpha P,\alpha Q\) gives exponent \(\deg\alpha\); the rank-two determinant identity gives exponent \(\det\alpha\). Since a torsion basis has primitive Weil-pairing value, the two exponents agree modulo every \(\ell^a\). The inverse limit gives equality in \(\mathbb Z_\ell\). The dual-isogeny identity applies to inseparable isogenies as well, so no separability condition has entered. The zero map has zero degree and zero determinant.

**Exercise 6.3 (medium).** Prove the Hasse bound from nonnegativity of degree, and justify the passage from integer pairs to a real discriminant inequality.

**Solution.** Equation (6) holds for all integer pairs. A negative value of \(z^2+az+q\) would persist on an open interval, and rational density supplies an integer pair \((m,n)\), \(n\ne0\), making (6) negative. Thus the polynomial is nonnegative on the real line. Its minimum at \(-a/2\) is \(q-a^2/4\), so \(a^2\le4q\).

**Exercise 6.4 (hard).** Prove \(a_p=0\) for \(y^2=x^3-x\) when \(p\equiv3\pmod4\), and explain the supersingular conclusion.

**Solution.** The character sum in Example 5.2 changes sign under the bijection \(x\mapsto-x\), so it equals its negative as an integer and is zero. With \(a_p=0\), Theorem 3.2 and Cayley–Hamilton give \(\varphi^2+[p]=0\) on the Tate module. Faithfulness, proved after Theorem 2.2, gives the same identity in \(\operatorname{End}(E')\). Thus \([p]=-\varphi^2\) is purely inseparable: \(\varphi\) is purely inseparable, and multiplication by \(-1\) is an automorphism. Its geometric kernel has only one point. This is exactly the definition of a supersingular elliptic curve, \(E'[p](\overline{\mathbb F}_p)=\{O\}\); see [Sutherland 2023, §13]. The argument includes \(p=3\).

## What this lesson does not prove

The algebraic group law, torsion structure, dual isogenies and the construction and properties of the Weil pairing are the four precise prerequisites in Section 1; their elliptic-curve references are [Sutherland 2023, §§4–6 and 23], [Milne 2008, Chapter I, §13] and [Milne 2021, Chapter II, §§3–7]. The prime-to-characteristic torsion and pairing statements apply over arbitrary fields, and the determinant theorem requires only \(\ell\ne\operatorname{char}K\). The degree of the \(q\)-power Frobenius on a curve is \(q\), and a separable isogeny has degree equal to its number of geometric kernel points; see [Sutherland 2023, §§4–5]. The finite étale lifting property over a strictly henselian local ring is [Stacks, Tag 04GK]: finite étale algebras over a henselian local ring are equivalent to finite étale algebras over its residue field. With separably closed residue field these are products of the residue field, so the lifted finite étale schemes are disjoint copies of the base. Reduction therefore gives the point bijection used in Section 3. The identification of étale first cohomology with the dual Tate module is the degree-one comparison in *ℓ-adic sheaves*, with a primary proof in [Milne 2008, Chapter I, §12, Theorem 12.1(a)] and Galois equivariance in Remark 12.5; it applies when ℓ differs from the field characteristic. The eta-product's modularity and the conductor assertion are established in later chapters. All five arithmetic results of this chapter—the two determinants, unramifiedness, the Frobenius trace, and the Hasse bound—are proved here.

## References

- [Sutherland 2023] Andrew V. Sutherland, MIT 18.783 *Elliptic Curves* lecture notes, Fall 2023: §4, *Isogenies*; §5, *Isogeny kernels and division polynomials*; §6, *Torsion subgroups and endomorphism rings*; §13, *Ordinary and supersingular elliptic curves*; §23, *Divisors and the Weil pairing*. Open notes: [§4](https://math.mit.edu/classes/18.783/2023/LectureNotes4.pdf), [§5](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf), [§6](https://math.mit.edu/classes/18.783/2023/LectureNotes6.pdf), [§13](https://math.mit.edu/classes/18.783/2023/LectureNotes13.pdf), [§23](https://math.mit.edu/classes/18.783/2023/LectureNotes23.pdf).
- [Milne 2021] J. S. Milne, *Elliptic Curves*, second edition, 2021, Chapter II, §§3–7: reduction modulo a prime, elliptic curves over p-adic fields, torsion points, endomorphisms and Néron models. [Author's edition](https://www.jmilne.org/math/Books/EC2.pdf).
- [Stacks, Tag 04GK] Finite étale algebras over a henselian local ring: [original statement and proof](https://stacks.math.columbia.edu/tag/04GK); [AI Integrated Stacks Project reading edition](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-henselian-cat-finite-etale). The reading edition retains the upstream tag and is not reviewed by the Stacks project's maintainers.
- [Milne 2008] J. S. Milne, *Abelian Varieties*, version 2.0 (2008), Chapter I, §12, Theorem 12.1(a) and Remark 12.5, and §13 on Weil pairings. [Author’s notes](https://www.jmilne.org/math/CourseNotes/AV.pdf).
