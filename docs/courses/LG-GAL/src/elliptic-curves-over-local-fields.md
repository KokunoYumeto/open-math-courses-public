# Elliptic curves over local fields and their Weil–Deligne representations

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Reduction tells us what happens to an elliptic curve at a prime. Its Galois representation tells the same story in linear algebra: trivial inertia for good reduction, a nilpotent extension for multiplicative reduction, and a finite ramified part for additive reduction. The Tate curve makes the extension completely explicit. At the small primes, the wild contribution requires additional computation.

## 1. Reduction and the convention for the elliptic-curve factor

Let \(F/\mathbf Q_p\) be finite, with normalized valuation \(v:F^\times\to\mathbf Z\), residue field \(k\) of size \(q\), and uniformizer \(\varpi\). Let \(E/F\) be an elliptic curve and choose \(\ell\ne p\). We use
\[
V_\ell E=T_\ell E\otimes\mathbf Q_\ell,
\qquad H_\ell(E)=(V_\ell E)^\vee,
\qquad \|\Phi\|=q^{-1}
\tag{1}
\]
for geometric Frobenius \(\Phi\). The Weil pairing gives \(\det V_\ell E=\chi_\ell\); its restriction to \(W_F\) is \(\|\cdot\|\), and it is trivial on inertia. The arithmetic elliptic-curve factor, with center \(s=1\), is
\[
L_F(E,s)=L\bigl(s,\mathrm{WD}(H_\ell(E))\bigr).
\tag{2}
\]
Thus we calculate the covariant Tate-module pair first and dualize for the usual factor. This agrees with the good-reduction convention of the Tate-module lesson.

Take a minimal integral Weierstrass equation
\[
y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6.
\tag{3}
\]
The reduced cubic is smooth for good reduction, nodal for multiplicative reduction, and cuspidal for additive reduction. A node is split when its two tangent directions are defined over \(k\). In the split case its nonsingular part is \(\mathbf G_m\); in the nonsplit case it is the nonsplit one-dimensional torus, with \(q+1\) points rather than \(q-1\). At a cusp the nonsingular part is \(\mathbf G_a\).

The geometric assertions behind these descriptions need proofs before they can be used. We give the coordinate and potential-good arguments here, prove Tate uniformization in §3, and use the proved good-reduction criterion in the earlier programme lesson *Néron models*, Theorem 7.4. That theorem concerns actual abelian schemes and their torsion; it is not a criterion deduced from a local factor.

### 1.1. Integral equations, minimality and the singular cubic

Write \(b_2,b_4,b_6,b_8,c_4,\Delta\) for the integer polynomials displayed in (19), and put \(j=c_4^3/\Delta\). The discriminant convention in (19) has no extra factor \(1728\). The spaces of functions with poles of order at most two and three at the origin have bases \(1,x\) and \(1,x,y\), by the genus-one Riemann–Roch argument in the Tate-module lesson. Consequently an isomorphism of pointed Weierstrass curves has the form
\[
x=u^2x'+r,\qquad y=u^3y'+s u^2x'+t,\qquad u\ne0.
\tag{3a}
\]
Indeed the leading coefficients \(\alpha,\beta\) of \(x',y'\) satisfy \(\beta^2=\alpha^3\), so \(u=\beta/\alpha\) gives these powers without adjoining a root. Substitution gives
\[
\begin{aligned}
ua'_1&=a_1+2s,\quad u^2a'_2=a_2-sa_1+3r-s^2,\\
u^3a'_3&=a_3+ra_1+2t,\\
u^4a'_4&=a_4-sa_3+2ra_2-(t+rs)a_1+3r^2-2st,\\
u^6a'_6&=a_6+ra_4+r^2a_2+r^3-ta_3-rta_1-t^2.
\end{aligned}
\tag{3b}
\]
Inserting these expressions in the integer polynomials (19) and cancelling terms proves
\[
c'_4=u^{-4}c_4,\qquad \Delta'=u^{-12}\Delta,\qquad j'=j.
\tag{3c}
\]
These are polynomial identities, so they hold in residue characteristics 2 and 3 as well. Scaling first makes any Weierstrass equation integral. The nonnegative integers \(v(\Delta)\) of its integral equations have a minimum, which defines a minimal equation. Their differences are multiples of 12 by (3c). In particular an integral equation with \(v(\Delta)<12\) is minimal. An integral equation with unit \(c_4\) is also minimal: a scaling which lowered its discriminant would make the new \(c_4\) nonintegral.

Here is the smoothness test, including the small characteristics. The point at infinity is always smooth, as its linear term in the chart \(y=1\) is the projective coordinate \(z\). In odd characteristic, completing the square turns the affine equation into
\[
(2y+a_1x+a_3)^2=4x^3+b_2x^2+2b_4x+b_6.
\]
The discriminant of the cubic on the right is \(16\Delta\), by the cubic resultant formula, obtained by eliminating its derivative. Thus it is smooth exactly when \(\Delta\ne0\). In characteristic 2 the partial derivative with respect to \(y\) is \(a_1x+a_3\). If \(a_1=0,a_3\ne0\), there is no singularity and \(\Delta=a_3^4\ne0\). If \(a_1=a_3=0\), the other derivative has a root over the algebraic closure, and the equation has a singularity there; \(\Delta=0\). If \(a_1\ne0\), a singularity must have
\[
x_0=a_3/a_1,\qquad y_0=(x_0^2+a_4)/a_1.
\]
Substitution in the cubic shows \(\Delta=a_1^6 f(x_0,y_0)\), where \(f\) is its defining polynomial. This proves the same test in characteristic 2.

Move a singular point to the origin over \(\bar k\). The reduced coefficients then satisfy \(a_3=a_4=a_6=0\), and the equation and its tangent cone are
\[
y^2+a_1xy=x^3+a_2x^2,\qquad y^2+a_1xy-a_2x^2.
\tag{3d}
\]
The tangent cone has two distinct factors exactly when \(b_2=a_1^2+4a_2\ne0\); at this singular equation \(c_4=b_2^2\). It is therefore a node exactly when \(c_4\ne0\), and otherwise a cusp. The normalization is explicitly
\[
x=t^2+a_1t-a_2,\qquad y=t(t^2+a_1t-a_2).
\]
The excluded parameters are the roots of \(t^2+a_1t-a_2\). At a node with roots \(r_1,r_2\), the coordinate \((t-r_1)/(t-r_2)\), normalized to be one at infinity, identifies the smooth part with \(\mathbf G_m\). To verify its group law, restrict a line to the parameter: its three intersection parameters give, by its cubic leading and constant coefficients, the product of these coordinates equal to one. The chord law then multiplies the coordinates. At a cusp with double root \(r\), use \(1/(t-r)\); the same coefficient comparison makes the sum of its three intersection coordinates zero, so the chord law adds them. These calculations also prove the tangent cases by polynomial specialization.

Over \(k\), the two nodal roots are either both rational or are exchanged by the quadratic residue extension. In the second case the coordinate is changed to its reciprocal by residue Frobenius, and its rational points have norm one in \(k_2^\times\). Their number is \(q+1\): the normalization \(\mathbf P^1\) has that many rational points, and neither excluded root is rational. In the split case two rational roots are excluded, and at a cusp one is excluded. Thus the smooth parts have respectively \(q-1,q+1,q\) points. The unit-discriminant and unit-\(c_4\) tests are independent of the minimal equation by (3c); they prove the asserted geometric reduction classification in every residue characteristic.

A unit-discriminant projective cubic really gives a good group model. It is proper and smooth, and its origin is a section. The generic invariant differential
\(\omega=dx/(2y+a_1x+a_3)\), using \(-dy/F_x\) where necessary, generates its differential line on every affine smooth chart. At infinity put \([x:y:z]=[u:1:z]\) and
\[
G=z+a_1uz+a_3z^2-u^3-a_2u^2z-a_4uz^2-a_6z^3.
\]
The equation \(G=0\) gives \(\omega=-du/G_z\); this follows by differentiation and the identity
\(zG_z+uG_u=-z(2+a_1u+a_3z)\). Since \(G_z(O)=1\), it is a generator there too, including at 2 and 3. Properness extends all points over the strict henselization, making this smooth cubic a weak model. The earlier *Néron models*, Lemma 8.2, proves that a proper smooth weak model with a generating invariant differential equals the Néron model. It therefore extends the generic group law and is an abelian scheme.

Conversely any good abelian scheme of relative dimension one gives a unit-discriminant integral equation. Here is a direct construction over the local field in this lesson. Its origin is a Cartier section, by the smooth relative curve parameter. For \(n>0\), put \(M_n=\mathcal O(nO)\) and \(V_n=H^0(E_F,M_n|_{E_F})\), of dimension \(n\) by the genus-one Riemann–Roch proof in the Tate-module lesson. The smooth model is regular and integral, with one irreducible special fibre. Let \(w\) be the valuation at its generic special point, normalized by \(w(\varpi)=1\). The actual earlier programme proof in *Discrete valuation rings, normal rings and Serre's criterion*, Corollary 4.5 and Theorem 3.3, proves regularity implies normality and that absence of poles at every codimension-one point extends a rational section. Therefore
\[
H^0(M_n)=\{f\in V_n:w(f)\ge0\}.
\]
Indeed the horizontal pole bounds are exactly the generic condition defining \(V_n\), and the only additional codimension-one bound is the special fibre. The same argument applies in any local trivialization of \(M_n\).

This module is finite without importing a proper-cohomology theorem. Define the norm \(|f|_w=|\varpi|^{w(f)}\) on \(V_n\). In a fixed \(F\)-basis it is bounded above by a constant times the maximum coefficient norm, by the valuation inequality, so it is continuous. The coefficient unit sphere is compact: the residue quotients of \(\mathcal O_F\) are finite, and a successive-subsequence argument gives convergence of every sequence in its complete unit ball. The norm consequently has a positive minimum on that sphere. Thus it is also bounded below by a positive constant times the coefficient norm. Its unit ball lies between two powers of the coordinate lattice. It is a submodule of a finite free DVR module and contains a lattice, hence is finite free of rank \(n\).

Restriction of its sections to the special fibre has kernel exactly \(\varpi H^0(M_n)\): vanishing generically on that integral fibre means \(w(f)\ge1\), and the same pole criterion applies to \(f/\varpi\). Its reduction thus injects into the special-fibre space of sections. Both spaces have dimension \(n\), the latter again by the earlier genus-one Riemann–Roch proof. It follows that
\[
H^0(M_n)/\varpi H^0(M_n)=H^0(E_k,M_n|_{E_k}).
\]
Localization recovers \(V_n\), since the displayed module contains a lattice. These conclusions provide exactly the lifting and base-change facts needed below.

Choose \(x,y\) extending the pole filtrations of degrees two and three. The constant 1 is a basis at degree one. The special-fibre inclusions of successive pole spaces are injective; lifting their bases shows that the corresponding lattice inclusions have free successive quotients, so these choices exist over the DVR. Their special pole orders are exactly two and three. The six sections \(1,x,y,x^2,xy,x^3\) consequently form a basis at degree six, by their distinct pole orders and Nakayama. Expressing \(y^2\) in that basis gives a Weierstrass equation with coefficients in the DVR and a unit leading coefficient \(\alpha\) of \(x^3\). Replacing \(x,y\) by \(\alpha x,\alpha y\) makes that coefficient one and preserves integrality. On both fibres the degree-three Riemann–Roch embedding proved in the Tate-module lesson identifies this equation with the elliptic curve itself. Its special cubic is smooth, hence its discriminant is a unit by the already-proved test. This proves both directions of the agreement between the integral-equation and abelian-scheme definitions of good reduction, and justifies using integral \(j\) for a good model.

### 1.2. The good-reduction criterion and descent

We spell out the mechanism of the earlier proved criterion to fix its exact scope. The programme lesson *Néron models*, Lemmas 7.1–7.3 and Theorem 7.4, constructs a smooth separated finite-type Néron model \(\mathcal E\), proves its mapping property and proves the following steps. Over the strict henselization, reduction bijects its \(\ell^n\)-torsion sections with the special-fibre torsion: multiplication by \(\ell^n\) is étale because its differential is the invertible scalar \(\ell^n\), and the henselian lifting property gives unique sections. If inertia is trivial, these sections are all \(\ell^{2n}\) geometric torsion points, by the torsion theorem proved in the Tate-module lesson.

The special identity component is an extension of an abelian variety of dimension \(a\) by a smooth connected affine group of dimension \(d\), with \(a+d=1\). Lemma 7.2 proves that the affine group has at most \(\ell^{nd}\) torsion points: simultaneous triangularization of its commuting matrices injects prime-to-characteristic torsion into the diagonal torus. If the special fibre has \(c\) components, its torsion therefore has at most \(c\ell^{n(2-d)}\) points. The equality \(\ell^{2n}\) for every \(n\) forces \(d=0\). Lemma 7.3 then proves that the model is proper: a projective closure of the identity model has connected special fibre, since its global functions and the inverse limit of those on its infinitesimal special fibres are respectively the DVR and its completion. The proper identity fibre is both open and closed in that connected fibre, leaving no boundary. This makes the model an abelian scheme. Conversely an abelian scheme has finite étale prime-to-characteristic torsion, and all its torsion lifts over the strict henselization; inertia is trivial. These are the two implications of the criterion used below.

An isomorphism between two good generic fibres extends uniquely over the DVR by the Néron mapping property, and its inverse extends as well; the two composites are identity by separatedness and generic-fibre density. Hence a good model over a finite Galois extension carries its unique semilinear descent action. Restriction to inertia gives origin-preserving automorphisms of its geometric special elliptic curve. The good-reduction specialization proof in the Tate-module lesson makes this compatible with the Tate modules. An automorphism acting trivially on that module is identity by the faithful endomorphism theorem there. This proves the faithful descent action needed in §2, including at 2 and 3.

### 1.3. Integral \(j\) produces a good model

**Lemma 1.1.** The curve \(E\) has potential good reduction exactly when \(v(j(E))\ge0\).

*Proof.* A good integral equation has unit discriminant, so its \(j\)-invariant is integral. Integrality is preserved and detected by a finite extension of the valuation. For the converse put \(J=j(E)\in\mathcal O_F\). If \(p\ne3\), consider
\[
C_a:\ y^2+a xy+y=x^3,\qquad
c_4=a^4-24a,\quad \Delta=a^3-27.
\]
Choose a root of the monic polynomial
\[
a^3(a^3-24)^3-J(a^3-27)=0
\tag{3e}
\]
in a finite extension of \(F\). Its coefficients are integral, so its roots are integral: a root of negative valuation would give the leading monomial uniquely the smallest valuation. If \(a^3-27\) vanished in the residue field, the other side of (3e) would reduce to \(27\cdot3^3=729\), a nonzero element because \(p\ne3\). Therefore its discriminant is a unit and it is a good curve with \(j=J\). This argument includes \(p=2\).

For \(p=3\) instead use
\[
D_a:\ y^2=x^3+a x^2-x,\qquad
c_4=16(a^2+3),\quad \Delta=16(a^2+4).
\]
The equation \(256(a^2+3)^3-J(a^2+4)=0\) becomes monic after division by the unit 256. Its roots are again integral. If its discriminant vanished modulo 3, then \(a^2+4=0\) and \(a^2+3=-1\), contradicting that equation. It also supplies a good curve with \(j=J\).

Over a field of characteristic zero, two elliptic curves with the same \(j\)-invariant become isomorphic over a finite extension. Here is the elementary check. Put their equations in short form \(y^2=x^3+Ax+B\). If \(AB\ne0\), equality of \(j\) gives \(t^3=s^2\), where \(t=A'/A,s=B'/B\). Taking \(u^2=s/t\) gives \(u^4=t,u^6=s\), so scaling by \(u\) is an isomorphism. If \(A=0\) or \(B=0\), equality of \(j\) forces the same vanishing for the second curve and one takes a sixth or fourth root of the remaining coefficient ratio. All these roots lie in finite extensions. Transporting the displayed good model to \(E\) proves potential good reduction. ∎

This proof does not exclude small residue characteristics or require a semistable-reduction theorem. For nonintegral \(j\), the complementary construction and its quadratic descent are proved in §§3–4.

## 2. Good and potentially good reduction

**Proposition 2.1.** Good reduction gives an unramified Weil–Deligne pair with \(N=0\). If
\[
a_E=q+1-\#\widetilde E(k),
\tag{4}
\]
then arithmetic Frobenius on \(V_\ell E\), and geometric Frobenius on \(H_\ell(E)\), have characteristic polynomial \(X^2-a_EX+q\). In particular
\[
L_F(E,s)=(1-a_Eq^{-s}+q^{1-2s})^{-1}.
\tag{5}
\]

*Proof.* Unramifiedness implies \(N=0\) by the uniqueness part of the monodromy theorem. The good-reduction identification and finite-field Frobenius polynomial were proved in the Tate-module lesson. Geometric Frobenius on the dual has matrix the transpose of arithmetic Frobenius on the original module, giving (5).

This Frobenius is semisimple. If its two roots are distinct, this is elementary. If they coincide, \(a_E^2=4q\), so \(q\) is a square and \(a_E/2\) is an integer. The finite-field Frobenius endomorphism \(\phi\) satisfies \((\phi-[a_E/2])^2=0\), by its Tate-module identity and the faithfulness of the endomorphism action proved earlier. A nonzero endomorphism of an elliptic curve is an isogeny and cannot have square zero. Hence \(\phi=[a_E/2]\), whose action is scalar. ∎

**Proposition 2.2.** Potential good reduction is equivalent to \(N=0\) for \(V_\ell E\). In that case \(r(I)\) is finite. If reduction is additive, then
\[
(V_\ell E)^I=0,
\qquad a(V_\ell E)=2+\mathrm{Sw}(V_\ell E).
\tag{6}
\]
For \(p\ge5\), the nontrivial inertia image has order \(2,3,4\) or \(6\), and the Swan term is zero.

*Proof.* Good reduction over a finite extension makes an open inertia subgroup act trivially, so (6) of the monodromy lesson forces \(N=0\). Conversely, if \(N=0\), the original inertia action equals the finite smooth inertia action. Choose an open subgroup of \(G_F\) whose intersection with \(I\) lies in its kernel; this is possible by the subspace topology on the closed subgroup \(I\). The corresponding finite extension has unramified Tate module, hence good reduction by Néron–Ogg–Shafarevich.

Assume reduction is additive but potentially good. The finite inertia representation has determinant one. If it had a line fixed pointwise by inertia, averaging over the finite image would provide a stable complement. The character on that complement would also be trivial, because the determinant and the character on the first line are trivial. This would make all inertia trivial, contradicting the good-reduction criterion. A two-dimensional fixed space gives the same contradiction, so the fixed space is zero. This argument concerns fixed vectors: a stable line can have a nontrivial character. The Artin-conductor formula gives (6).

Acquire good reduction over a finite Galois extension. Its smooth special fiber inherits the inertia action by descent of the good model; inertia fixes the residue field, so this action is by automorphisms fixing the origin. Reduction identifies the prime-to-\(p\) Tate modules, and an automorphism acting trivially on that Tate module is the identity. Thus the finite inertia image embeds in the automorphism group of the special elliptic curve.

When \(p\ge5\), write this special curve over \(\bar k\) as \(y^2=x^3+Ax+B\). An origin-preserving automorphism has the form \((x,y)\mapsto(u^2x,u^3y)\): in the general Weierstrass change of coordinates, absence of \(xy,y,x^2\) terms forces the translation and shear terms to vanish, since 2 and 3 are invertible. It must satisfy \(u^4A=A\) and \(u^6B=B\). Accordingly its group has order 2 if \(AB\ne0\), order 4 if \(B=0\), and order 6 if \(A=0\). Its nontrivial subgroups have exactly the stated possible orders. These orders are prime to \(p\), so the pro-\(p\) wild inertia has trivial image. ∎

The extension and faithfulness of the descent action were proved in §1.2. We now give the corresponding automorphism calculations at the small primes, where a wild subgroup can occur.

**Lemma 2.3.** In potentially good reduction, the possible nontrivial finite inertia groups have the following orders:
\[
\begin{array}{c|c|c}
p&\text{possible orders}&\text{ambient exceptional automorphism group}\\ \hline
p\ge5&2,3,4,6&\mu_4\text{ or }\mu_6\\
3&2,3,4,6,12&C_3\rtimes C_4\\
2&2,3,4,6,8,24&Q_8\rtimes C_3.
\end{array}
\tag{6a}
\]
Here the action of \(C_4\) on \(C_3\) is inversion, and that of \(C_3\) on \(Q_8\) cyclically permutes its three subgroups of order four. The table restricts the group of an individual curve; it does not assert that each group occurs over every specified field \(F\).

*Proof.* We work over \(\bar k\). In characteristic 3, completing the square gives \(y^2=x^3+a_2x^2+a_4x+a_6\), with \(c_4=a_2^2\). If \(a_2\ne0\), the coefficient comparisons in (3b) force an automorphism to have \(u^2=1,r=0\), and hence it is \(\pm1\). If \(a_2=0\), smoothness forces \(a_4\ne0\). Translation of \(x\) removes \(a_6\), and scaling reduces the equation to \(y^2=x^3-x\). Its automorphisms are
\[
x\mapsto u^2x+r,\qquad y\mapsto u^3y,
\qquad u^4=1,\quad r^3-r=0.
\]
They form the stated group of order 12. The translation subgroup is \(C_3\); an element with \(u\) of order four acts on it by \(u^2=-1\), and its square is the central involution \([-1]\). A subgroup has trivial or full translation intersection. In the first case it injects into \(C_4\), giving orders 1,2,4. In the second its image in \(C_4\) has order 1,2 or 4, giving orders 3,6 or 12. These are all the possibilities at 3.

In characteristic 2, if \(j\ne0\), normalize the equation to
\(y^2+xy=x^3+a_2x^2+a_6\), with \(a_6\ne0\). This normalization follows successively from \(a_1\ne0\), scaling it to one, translating to remove \(a_3\), and shearing/translating \(y\) to remove \(a_4\). Equations (3b) then force \(u=1,r=t=0,s^2+s=0\). The two automorphisms are identity and \((x,y)\mapsto(x,y+x)=[-1]\).

If \(j=0\), then \(a_1=0\) and smoothness forces \(a_3\ne0\). Scaling makes \(a_3=1\). The coefficient comparisons permit removing \(a_2,a_4\): choose \(s\) solving \(s^4+s=a_4+a_2^2\), then \(r=a_2+s^2\); finally choose \(t\) solving the remaining equation \(t^2+t=\text{constant}\). These choices exist over \(\bar k\). The resulting equation is \(y^2+y=x^3\). Its automorphisms have the form
\[
x\mapsto u^2x+r,\quad y\mapsto y+s u^2x+t,
\quad u^3=1,\quad r=s^2,\quad s^4=s,\quad t^2+t=s^6.
\tag{6b}
\]
There are \(3\cdot4\cdot2=24\) of them. The eight with \(u=1\) form \(Q_8\): their unique nonidentity element with \(s=0\) is the central involution \(y\mapsto y+1\), and squaring any element with \(s\ne0\) gives that involution, since its new constant is \(s^3=1\). Their quotient by this involution has the additive group of \(\mathbf F_4\), so these relations identify the quaternion group. The three choices of \(u\) split off a \(C_3\), whose conjugation cycles the three nonzero values of \(s\), and hence the three cyclic groups of order four.

For a subgroup \(H\) of this group, let \(K=H\cap Q_8\). If its image in \(C_3\) is trivial, its orders are 1,2,4,8. If that image is full, an element above its generator permutes the three order-four subgroups, so its stable subgroup \(K\) is only 1, the center, or all \(Q_8\). The resulting orders are 3,6,24. This exhausts the possibilities at 2. Finally §1.2 embeds inertia faithfully into these automorphism groups. The wild image is a normal \(p\)-subgroup and the tame quotient is cyclic, by the ramification proof in the monodromy lesson; the displayed groups satisfy these restrictions. ∎

The potentially good pair is not specified by the words “additive reduction” alone. It is \((r,0)\), with \(r(I)\) the descent action on the Tate module of the good special fiber; Frobenius is obtained from its finite-field Frobenius and the same descent data. It is Frobenius-semisimple: after a finite Galois extension with good reduction, a sufficiently large power of any Frobenius lift belongs to that extension’s Galois group and acts as a power of a good-reduction Frobenius. Proposition 2.1 makes that power semisimple, hence the original matrix is semisimple in characteristic zero.

For tame inertia of order \(e\), over algebraically closed coefficients its generator has eigenvalues \(\zeta_e,\zeta_e^{-1}\), with \(\zeta_e\) primitive. These eigenvalues follow from faithfulness, determinant one, and semisimplicity of a finite-order matrix. Frobenius conjugates this generator by its \(q^{-1}\)-power. If \(q\equiv1\pmod e\), it preserves the two eigenlines; its diagonal entries have product \(q^{-1}\). If \(q\equiv-1\pmod e\), and \(e>2\), it interchanges them, so in a suitable basis
\[
r(\Phi)=\begin{pmatrix}0&b\\a&0\end{pmatrix},
\qquad ab=-q^{-1}.
\tag{7}
\]
For \(e=2\) inertia is scalar \(-1\), and Frobenius is determined separately. This describes the possible matrices while keeping the required Frobenius data visible.

All four nontrivial orders occur. With \(p\ge5\), the following curves acquire good reduction after adjoining \(u=\varpi^{1/e}\) and using \(x=u^2X,y=u^3Y\). The roots of unity needed to make the extension Galois can be supplied by an unramified extension.

| Curve | \(e\) | Good equation after scaling | \(v(\Delta)\) |
|---|---:|---|---:|
| \(y^2=x^3+\varpi^3\) | 2 | \(Y^2=X^3+1\) | 6 |
| \(y^2=x^3+\varpi^2\) | 3 | \(Y^2=X^3+1\) | 4 |
| \(y^2=x^3+\varpi x\) | 4 | \(Y^2=X^3+X\) | 3 |
| \(y^2=x^3+\varpi\) | 6 | \(Y^2=X^3+1\) | 2 |

Indeed a generator sends \(u\) to \(\zeta_eu\), and acts on the good equation by \((X,Y)\mapsto(\zeta_e^{-2}X,\zeta_e^{-3}Y)\), of exact order \(e\). The good discriminants are units because \(p\ge5\). The original discriminants are respectively \(-432\varpi^6,-432\varpi^4,-64\varpi^3,-432\varpi^2\). Their valuations are below 12, so the integral models are minimal: lowering a discriminant valuation through an integral minimal-model scaling subtracts a positive multiple of 12. Each has additive reduction, conductor exponent 2, \(N=0\), and factor 1 by the vanishing invariant space.

## 3. The Tate extension is the Kummer class

To distinguish the Tate parameter from the residue cardinality, call it \(Q\in F^\times\), with \(m=v(Q)>0\). We first prove the uniformization that will be used in the torsion calculation.

### 3.0. Construction and proof of the uniformization

Put
\[
S_r(Q)=\sum_{n\ge1}\frac{n^rQ^n}{1-Q^n},\quad
A_4=-5S_3(Q),\quad A_6=-\frac{5S_3(Q)+7S_5(Q)}{12}.
\tag{8a}
\]
The coefficients of \(A_6\) are integers: \(12\mid5n^3+7n^5\), because \(n^3(n^2-1)\) is divisible by 12. Thus these are integral convergent power series, even at 2 and 3. Define
\[
\begin{aligned}
X(z)&=\sum_{n\in\mathbf Z}\frac{Q^nz}{(1-Q^nz)^2}-2S_1(Q),\\
Y(z)&=\sum_{n\in\mathbf Z}\frac{(Q^nz)^2}{(1-Q^nz)^3}+S_1(Q).
\end{aligned}
\tag{8b}
\]
They converge uniformly on closed annuli avoiding \(Q^{\mathbf Z}\). For negative \(n\), replacing \(Q^nz\) by its reciprocal bounds the summand by a constant times \(|Q|^{-n}\); for positive \(n\) the bound is a constant times \(|Q|^n\). Rearrangement gives
\[
X(Qz)=X(z)=X(z^{-1}),\quad
Y(Qz)=Y(z),\quad Y(z^{-1})=-X(z)-Y(z).
\tag{8c}
\]

**Lemma 3.0.** The equation
\[
E_Q:\quad y^2+xy=x^3+A_4x+A_6
\tag{8d}
\]
is an elliptic curve. Sending \(z\notin Q^{\mathbf Z}\) to \((X(z),Y(z))\) and \(Q^{\mathbf Z}\) to its origin induces a Galois-equivariant group isomorphism
\[
E_Q(\bar F)\simeq\bar F^\times/Q^{\mathbf Z}.
\tag{8}
\]
Its displayed equation is minimal, \(v(\Delta)=v(Q)\), its reduction is a split node, and
\[
j(E_Q)=Q^{-1}+744+196884Q+\cdots.
\tag{8e}
\]
For each \(J\in F\) of negative valuation there is a unique \(Q\in F\) of positive valuation with \(j(E_Q)=J\).

*Proof.* Direct substitution of (8a) in (19) gives the integer series \(\Delta=Q+O(Q^2)\), \(c_4=1+O(Q)\). For the complex argument restrict \(Q\) to a sufficiently small punctured disc on which \(\Delta\ne0\); the cubic is therefore smooth before its group law is used. This open set suffices to establish the universal coefficient identities. Put \(z=e^u\) and \(\Lambda=2\pi i\mathbf Z+\log(Q)\mathbf Z\). The function \(L(u)=X(e^u)+1/12\) is periodic for this lattice, and has only double poles at its points. Expanding the geometric series in (8b) gives
\[
L(u)=u^{-2}+\left(\frac1{240}+S_3(Q)\right)u^2
       +\left(-\frac1{6048}+\frac{S_5(Q)}{12}\right)u^4+O(u^6).
\]
Its derivative is \(H(u)=X(e^u)+2Y(e^u)\). With
\(g_2=1/12+20S_3(Q)\), \(g_3=-1/216+(7/3)S_5(Q)\), the periodic function
\(H^2-4L^3+g_2L+g_3\) has no poles: the displayed Laurent coefficients cancel its terms of degrees \(-6,-2,0\). It is bounded on a compact period parallelogram and therefore on the plane, and hence constant. Here is the complex-analysis proof needed for that implication and for the following contour calculation. Every analytic function used here is locally a convergent power series, by the normally convergent explicit series (8b). Such a series has a local primitive by termwise integration. Subdivide a compact region avoiding poles into sufficiently small cells lying in these power-series discs; integrals around each cell vanish, and cancellation of common edges proves the contour theorem for that region. Removing a small disc about \(a\) and applying it to \(F(u)/(u-a)\) gives
\[
F(a)=\frac1{2\pi i}\int_{|u-a|=R}\frac{F(u)}{u-a}\,du.
\]
Expanding the denominator for a variable point near \(a\) gives its Taylor coefficient formula and the bound \(|c_n|\le \sup_{|u-a|=R}|F(u)|/R^n\). If \(F\) is entire and bounded, let \(R\to\infty\); every positive-degree coefficient vanishes. It is constant. Applying this to the periodic expression above, its constant Laurent coefficient is zero, so it vanishes. Expanding gives exactly (8d).

We also justify its addition law without assuming an analytic uniformization theorem. For a meromorphic \(\Lambda\)-periodic function, its zeros and poles, counted with multiplicities, have equal number and the sum of their locations differs by a lattice point. Indeed near a zero or pole write \(f(u)=(u-a)^m h(u)\), with \(h\) nonvanishing. Its logarithmic derivative has residue \(m\), and \(u f'/f\) has residue \(ma\). The just-proved contour theorem, after removing small circles about these points, shows that their boundary integrals are \(2\pi i\sum m\) and \(2\pi i\sum ma\). For \(f'/f\), opposite sides of a period parallelogram cancel. For \(u f'/f\), pairing them gives a period times the integral of \(f'/f\) along each of the other two sides. Such a side integral is \(2\pi i\) times an integer: if \(J(t)\) is its integral up to time \(t\), differentiating \(e^{-J(t)}f(u(t))\) makes it constant, and equality of the endpoint values of \(f\) gives \(e^{J(1)}=1\). Since the kernel of the complex exponential is \(2\pi i\mathbf Z\), the weighted integral belongs to \(2\pi i\Lambda\). These facts prove both assertions. Choose the parallelogram to avoid its finitely many zeros and poles on the boundary; isolated zeros follow from the first nonzero Taylor coefficient, so such a choice exists.

The function \(Y(e^u)-\lambda X(e^u)-\nu\) has a triple pole at the lattice origin and no other poles. Its three intersection parameters therefore sum to zero modulo \(\Lambda\). They give the three cubic intersection points for a generic line: \(X-c\) has just two zeros, since its only pole has order two, and these are the parameters \(u,-u\) by (8c). Their \(Y\)-values are opposite and distinct away from the finitely many zeros of \(H=X+2Y\). Thus the parametrization is generically injective, so those three generic line zeros represent three distinct intersections. The divisor form of the cubic group law, proved in the Tate-module lesson, and (8c) now show that multiplication of \(z\)'s is addition of points. Equivalently, for generic \(z_1,z_2\), set
\[
\lambda=\frac{Y(z_2)-Y(z_1)}{X(z_2)-X(z_1)},\quad
\nu=Y(z_1)-\lambda X(z_1),\quad
x_3=\lambda^2+\lambda-X(z_1)-X(z_2).
\]
The identities are \(X(z_1z_2)=x_3\) and \(Y(z_1z_2)=-(\lambda+1)x_3-\nu\).

These are universal identities, rather than assertions restricted to complex points. Write (8b) as power series in \(Q\); every coefficient is a rational function with integer coefficients in \(z,z^{-1},(1-z)^{-1}\). After clearing the displayed denominators, each coefficient of the curve and addition identities is a rational function that vanishes on an open set of complex parameters. Its numerator polynomial is therefore identically zero. Specializing their convergent series proves the identities over every complete nonarchimedean field here.

For nonarchimedean \(Q\), the integral leading terms already computed give \(\Delta\ne0\), \(v(\Delta)=m\), and unit \(c_4\). Section 1.1 proves minimality. Reduction is \(y^2+xy=x^3\), whose two tangent lines \(y=0,y=-x\) are distinct even in characteristic 2. Expanding \(c_4^3/\Delta\) gives (8e). The map \(\phi\) defined by (8b) is periodic, and its preimage of the origin is exactly \(Q^{\mathbf Z}\), since its other values have finite affine coordinates.

The generic addition identities extend to every pair. To see this without dividing by a vanishing slope denominator, observe that the image is infinite: at \(z=1+Q^h\), for sufficiently large positive integers \(h\), the term \(z/(1-z)^2\) uniquely dominates \(X(z)\), and \(|X(z)|=|Q|^{-2h}\). Given \(a,b\), choose \(w\) so that the three additions involving \((w,a),(wa,b),(w,ab)\) all have distinct affine \(x\)-coordinates. Only finitely many image points are excluded: for the middle pair use the already valid identity \(\phi(wa)=\phi(w)+\phi(a)\). Such a \(w\) exists by the infinite image. Comparing \(\phi(wab)\) by those identities and cancelling \(\phi(w)\) proves \(\phi(ab)=\phi(a)+\phi(b)\). Identity or inverse cases are covered by (8c) and the same auxiliary-point argument. This proves the homomorphism and its kernel.

For surjectivity we need a power-series fact, whose proof is useful here. If
\(f(T)=T+\sum_{h\ge1}c_hT^{h+1}\) with \(|c_h|\le\rho^h\), formal recursive solution of \(f(g(T))=T\) gives
\(g(T)=T+\sum_{h\ge1}d_hT^{h+1}\) with \(|d_h|\le\rho^h\). At each step the new coefficient is a sum of integer multiples of products of earlier coefficients with total weight \(h\); the ultrametric inequality gives this bound by induction. Both series converge on \(|T|<\rho^{-1}\), their correction terms have smaller norm than \(T\), and formal composition converges there. Thus \(f\) bijects that disc with itself, with inverse \(g\).

Let \((x,y)\in E_Q(L)\), where \(L/F\) is any finite extension. Set \(\rho=|Q|^{1/2}<1\). First suppose \(|x|>\rho\). Put \(r=z+z^{-1}-2\). The integer polynomials
\(F_n(r)=z^n+z^{-n}-2\) satisfy
\[
F_0=0,\quad F_1=r,\quad
F_{n+1}=(r+2)F_n-F_{n-1}+2r;
\]
they have degree \(n\), zero constant term and integer coefficients. Expansion of (8b) consequently gives
\[
X(z)=r^{-1}+\sum_{h\ge1}a_h r^h,\qquad |a_h|\le|Q|^h.
\]
Its reciprocal is \(r+\sum_{h\ge1}c_h r^{h+1}\), with \(|c_h|\le\rho^h\): the denominator terms have weights \(h+1\) and norms at most \(|Q|^h\le\rho^{h+1}\). The inverse fact uniquely solves \(1/x=1/X\) for \(|r|<\rho^{-1}\). A root of \(z^2-(r+2)z+1=0\) lies in an extension of degree at most two. Both roots have norms between \(\rho\) and \(\rho^{-1}\), or both have norm one, by comparing the three terms of the quadratic. Thus the series expansions used are valid and give \(X(z)=x\).

Second suppose \(|x|<1\). Put \(s=z+Q/z\). The polynomials \(G_n(s,Q)=z^n+(Q/z)^n\) satisfy
\(G_0=2,G_1=s,G_{n+1}=sG_n-QG_{n-1}\). On \(|Q|<|z|<1\), (8b) becomes
\[
X(z)=-2S_1(Q)+\sum_{n\ge1}\frac{n}{1-Q^n}G_n(s,Q)
     =c_0+c_1s+\sum_{h\ge2}c_hs^h.
\]
The recurrence gives \(|c_0|<1\), \(c_1\in1+Q\mathcal O_L\), and \(|c_h|\le1\). Apply the inverse fact with \(\rho=1\) after subtracting \(c_0\) and dividing by \(c_1\). It supplies \(|s|<1\) with this value \(x\). The roots of \(z^2-sz+Q=0\) both have norm less than one: otherwise its quadratic term would uniquely dominate. Their product is \(Q\), so each also has norm greater than \(|Q|\). Hence this expansion applies and again \(X(z)=x\). The two cases cover every \(x\), since \(\rho<1\).

The two points \(\phi(z),\phi(z^{-1})\) have the same \(x\)-coordinate and are negatives by (8c); they are precisely the roots of the quadratic equation for \(y\). Replace \(z\) by its inverse if necessary to obtain \((x,y)\). The quadratics used are separable, except for repeated roots already in \(L\) and one case if one also applies this construction to a complete field of characteristic 2: the second quadratic with \(s=0\), namely \(z^2=Q\). That case has direct descent. Periodicity gives \(\phi(z^{-1})=\phi(z)\), since \(z^{-1}=z/Q\); (8c) therefore forces \(x=0\), and (8d) gives \(y^2=A_6(Q)\). In characteristic 2 separate the even and odd coefficients of its integer series to write
\[
A_6(Q)=c(Q)^2+Q b(Q)^2,
\qquad b(Q)\in1+Q\mathbf F_2[[Q]],\quad c(Q)\in Q\mathbf F_2[[Q]].
\]
Indeed each prime-field coefficient is its own square, and the coefficient of \(Q\) in \(A_6\) is one. The convergent series \(b,c\) belong to \(L\), and
\(z=(y+c(Q))/b(Q)\in L\), by uniqueness of a square root in characteristic 2. Thus no inseparable descent assertion is used.

In all the remaining cases \(z\) lies in a finite separable extension of \(L\). For any automorphism \(\sigma\) of its Galois closure over \(L\), equivariance and the kernel imply \(\sigma(z)/z=Q^a\). An automorphism of a finite extension of a complete valued field preserves its unique extended absolute value, so \(a=0\). Thus \(z\in L\). This proves surjectivity over every finite \(L/F\), and taking their union proves (8). All series coefficients lie in \(F\), proving Galois equivariance.

Finally \(1/j(E_Q)=Q+O(Q^2)\) is an integer power series. The inverse-series fact with \(\rho=1\) bijects the maximal ideal of \(F\) with itself. Given \(v(J)<0\), its inverse at \(J^{-1}\) yields the unique \(Q\in F\) with \(v(Q)>0\) and \(j(E_Q)=J\). ∎

This proof follows the actual constructions in Tate's freely accessible *A review of non-Archimedean elliptic functions*, first part, pp.2–12, including both inverse-series arguments. The formal identities, kernel and surjectivity have all been established above; the source link supplies a primary account, not an omitted implication.

**Theorem 3.1.** There is a short exact sequence
\[
0\longrightarrow\mathbf Z_\ell(1)
\longrightarrow T_\ell E_Q
\longrightarrow\mathbf Z_\ell
\longrightarrow0,
\tag{9}
\]
whose class is the Kummer class \(\kappa(Q)\in H^1(G_F,\mathbf Z_\ell(1))\). On inertia it satisfies
\[
\kappa(Q)(\sigma)=m\,t_\ell(\sigma).
\tag{10}
\]
Consequently the rational extension is nonsplit on inertia and the inertia image is infinite.

*Proof.* A class \([z]\) in (8) is killed by \(\ell^n\) exactly when \(z^{\ell^n}=Q^b\) for some integer \(b\). Send it to \(b\bmod\ell^n\). Replacing \(z\) by \(zQ^a\) changes \(b\) by \(a\ell^n\), so this is well defined. Its kernel is the group of \(\ell^n\)-th roots of unity, and it is surjective by choosing a root of \(Q\). Thus
\[
0\to\mu_{\ell^n}\to E_Q[\ell^n]\to\mathbf Z/\ell^n\to0.
\tag{11}
\]
Choose compatible roots \(Q_n\) with \(Q_n^{\ell^n}=Q\), and compatible primitive roots \(\zeta_n\). They form a basis of (11); multiplication by \(\ell\) gives the compatible bases at the previous level. Taking the inverse limit proves (9) directly, including surjectivity from the compatible choices. With the first basis vector denoted \(e_1\) and the second \(e_2\), write
\[
g(Q_n)/Q_n=\zeta_n^{\kappa_n(g)}.
\]
Then
\[
\rho(g)=\begin{pmatrix}\chi_\ell(g)&\kappa(Q)(g)\\0&1\end{pmatrix},
\qquad
\kappa(Q)(gg')=\kappa(Q)(g)+\chi_\ell(g)\kappa(Q)(g').
\tag{12}
\]
Changing the compatible roots adds a coboundary. This is precisely the Kummer cocycle and hence the extension class.

Write \(Q=\varpi^m u\), with \(u\in\mathcal O_F^\times\). Every \(\ell^n\)-th root of \(u\) can be chosen in the maximal unramified extension: choose its residue root in \(\bar k\) and lift by Hensel’s lemma, whose derivative is a unit because \(\ell\ne p\). Compatible choices give trivial inertia action on these roots. The cocycle for \(\varpi\) on inertia is the tame character, and the cocycle for \(\varpi^m\) is its \(m\)-fold multiple. This proves (10). Inertia also acts trivially on \(\mu_{\ell^n}\).

Thus inertia has matrices \(1+m t_\ell(\sigma)E_{12}\). Since \(m\ne0\) and \(t_\ell(I)=\mathbf Z_\ell\), their image is infinite. A split extension over \(\mathbf Q_\ell\) would have trivial inertia, because both endpoint characters are trivial there. Hence it is nonsplit. ∎

The integral and residual conclusions differ. Reduction of (12) modulo \(\ell\) has nontrivial inertia exactly when \(\ell\nmid m\). If \(\ell\mid m\), its inertia matrices are identity even though the rational inertia image is infinite. This distinction will matter for residual representations.

## 4. Multiplicative and potentially multiplicative pairs

**Lemma 4.0.** If \(v(j(E))<0\), then \(E\) is a quadratic twist of the uniquely specified \(E_Q\) of Lemma 3.0. Its twisting character is trivial, unramified nontrivial, or ramified according as its reduction is split multiplicative, nonsplit multiplicative, or additive.

*Proof.* Here \(j\) is neither 0 nor 1728. In the short equations in Lemma 1.1, both \(A\) and \(B\) are nonzero. That proof obtains an isomorphism by adjoining only \(u\) with \(u^2=s/t\). The only pointed geometric automorphisms of such a short curve are \(\pm1\): (3b) forces the shear and translations to vanish, and \(u^4=u^6=1\) forces \(u^2=1\). Galois descent of this isomorphism is therefore a homomorphism \(\chi:G_F\to\{\pm1\}\). On every prime-to-\(p\) torsion group the involution is multiplication by \(-1\), so the Tate module is the \(\chi\)-twist of that of \(E_Q\).

We include the nodal geometry that identifies this character. In a split nodal integral equation, lift the two distinct tangent lines by Hensel's lemma. The Hessian of the local defining polynomial at the reduced node is invertible: in the coordinates (3d) its determinant is \(-b_2\), a unit, including in characteristic 2. Thus its critical point lifts uniquely. Explicitly, for the two derivative equations start from any lifts of the residue coordinates, multiply their error vector by minus the inverse Hessian, and correct the coordinates by that vector. Taylor expansion doubles the valuation of the error at each step, the Hessian remains invertible, and completeness gives a root. Subtracting two such roots and using the invertible linear term proves uniqueness in this residue class. Formal changes of its two coordinates put its completed equation in the form
\[
uv=h,\qquad h\in\varpi\mathcal O_F.
\tag{15a}
\]
Here is the coordinate elimination: its quadratic part factors into two distinct linear forms over the complete DVR, which become \(u,v\). At each higher degree, every monomial belongs to \((u,v)\), so writing that degree as \(u f+v g\) and replacing \(v,u\) by \(v-f,u-g\) eliminates it modulo the next degree. These corrections converge formally; the constant is the value at the critical point. The integer discriminant has a simple zero at a node. More explicitly, translate the reduced node to the origin, where \(a_3=a_4=a_6=0\) modulo \(\varpi\); then
\(\partial\Delta/\partial a_6=-b_2^3\) is a unit. The critical coordinates depend on the other coefficients but not on \(a_6\). The unique nearby value of \(a_6\) for which the critical point lies on the cubic is exactly the nearby zero of \(\Delta\), by the singularity test in §1.1. Factoring this polynomial at that simple root shows
\(v(h)=v(\Delta)=n\).

After absorbing its unit in \(v\), (15a) is \(uv=\varpi^n\). Its regular resolution has the charts
\[
U_iV_i=\varpi,\quad
u=\varpi^{i-1}U_i,\quad v=\varpi^{n-i}V_i,
\qquad 1\le i\le n.
\tag{15b}
\]
Consecutive charts glue by \(U_{i+1}=V_i^{-1}\), \(V_{i+1}=\varpi V_i\). They are obtained successively by blowing up \((u,\varpi)\); in its \(u=\varpi u_1\) chart the remaining singularity is \(u_1v=\varpi^{n-1}\), and the other chart is regular. This proves properness and exhausts the singularities inductively. The exceptional curves form a chain of \(n-1\) projective lines between the two branches of the original component. Its normalization is the projective line in §1.1, so the full fibre is a cycle with \(n\) components, each of multiplicity one, denoted \(I_n\). For \(n>1\), each component has self-intersection \(-2\): intersect the principal total fibre with that component, whose intersections with the others total two. There is no exceptional curve of self-intersection \(-1\), so this regular model is relatively minimal. For \(n=1\) the original nodal model is already regular.

We verify its Néron interpretation for this arbitrary nodal equation. Let \(W\) be the relative smooth locus of the resolved projective model. Every point over the maximal unramified extension extends by properness. Its section cannot meet a crossing: there the equation is \(UV=\varpi\), and both \(U,V\) in the maximal ideal would give valuation at least two for \(\varpi\). Thus \(W\) is a smooth quasi-projective weak model. Its generic invariant differential is a generator there. On the original normalized component it reduces to
\[
\frac{dt}{(t-r_1)(t-r_2)}
=\frac1{r_1-r_2}\,\frac{dz}{z},
\qquad z=\frac{t-r_1}{t-r_2},
\]
with unit \(r_1-r_2\). Near the formal node it is a unit times \(du/u=-dv/v\); the formal coordinate change multiplies a residue differential by a unit. In chart (15b), relative differentiation makes this \(dU_i/U_i\), which generates at every smooth point of that component. It also generates at infinity by the calculation in §1.1. The earlier *Néron models*, Lemma 8.2, now embeds \(W\) as a fibre-dense open of the Néron model. Its special components are the \(n\) disjoint copies of \(\mathbf G_m\). Two cannot enter the same geometric component of the smooth Néron curve, because disjoint nonempty open sets cannot lie in an irreducible smooth connected curve. Its differential at the origin is a generator; translation in the smooth Néron group extends it to a regular invariant differential everywhere. The component containing a copy of \(\mathbf G_m\) has function field \(\bar k(z)\) and projective normalization \(\mathbf P^1\). Adjoining either omitted endpoint would make the nonzero simple pole of \(dz/z\) a regular differential there, which is impossible. Hence no endpoint is added and \(W\) is the full Néron model. Its identity special fibre is exactly the multiplicative group in §1.1. This proves semistability of every nodal equation. Its identity part then persists under every extension of DVRs by the actual earlier proof in *Néron models*, Theorem 8.20.

For a nonsplit node, first make the unramified quadratic extension which separates its tangent lines; the same calculation applies. Residue Frobenius exchanges the branches exactly when it inverts their multiplicative coordinate. The automorphism \([-1]\) of \(E_Q\) is inversion on that coordinate, by (8c). Thus trivial \(\chi\) gives the split node, and the unramified nontrivial \(\chi\) gives the nonsplit node. To see that the latter descent really supplies an integral nodal model, its semilinear involution on the homogeneous coordinates is \((x,y,z)\mapsto(x,-y-x,z)\). Descend this rank-three module and its invariant cubic equation along the finite étale extension, using the proved Module descent lemma in *Quotients and torsors*, “Faithfully flat affine descent”. The invariant module is finite and torsion-free over the DVR, hence free; its rank is three after faithful scalar extension. Its stable pole filtration \(\langle1\rangle\subset\langle1,x\rangle\subset\langle1,x,y\rangle\) also descends, and its successive free rank-one quotients permit a compatible basis. This gives a Weierstrass equation for the descended cubic and origin. After the unramified extension its coordinate change has unit leading coefficients, so its \(c_4\) is a unit and its discriminant valuation is unchanged. Its geometric node is checked after that extension, so it is minimal by §1.1. Unramified base change of its Néron model is proved in *Néron models*, Theorem 5.2.

If \(\chi\) is ramified and \(E\) had multiplicative reduction, its semistable Néron identity model would commute with extension to the field which splits \(\chi\), by that same Theorem 8.20. An inertia element acts trivially on the geometric special torus of this base change: it acts only on coefficients and fixes the residue field. But its action after the Tate identification is the nontrivial inversion supplied by \(\chi\), a contradiction. Good reduction is excluded by the negative valuation of \(j\). The remaining reduction is additive. Conversely an unramified \(\chi\) descends the nodal identity model and hence is multiplicative. This proves all three alternatives. ∎

**Theorem 4.1.** The covariant Tate-module pair of a split Tate curve is \(\mathrm{Sp}(2)\). More generally, if \(v(j(E))<0\), then
\[
\mathrm{WD}(V_\ell E)\simeq\chi\otimes\mathrm{Sp}(2),
\tag{13}
\]
where \(\chi\) is the quadratic splitting character described in §1.

*Proof.* In the basis of (12), inertia has \(\rho(\sigma)=\exp(t_\ell(\sigma)N)\), with \(N=mE_{12}\). Removing monodromy therefore makes \(r(I)=1\). Frobenius has the shape
\[
r(\Phi)=\rho(\Phi)=\begin{pmatrix}q^{-1}&b\\0&1\end{pmatrix}.
\tag{14}
\]
Replace \(e_2\) by \(e_2+b/(1-q^{-1})\,e_1\). Its Frobenius eigenvalue becomes one, while \(e_1\) has eigenvalue \(q^{-1}\). Monodromy still sends that new vector to \(m e_1\). In the ordered basis consisting of the new \(e_2\) and \(m e_1\), the matrices are exactly the degree-zero and degree-one lines of \(\mathrm{Sp}(2)\).

Lemma 4.0 supplies the Tate curve, the quadratic character, and its reduction-theoretic interpretation. Removing monodromy commutes with this finite character twist, proving (13). ∎

The cohomological pair in (2) is therefore
\[
\mathrm{WD}(H_\ell(E))\simeq
\chi\|\cdot\|^{-1}\otimes\mathrm{Sp}(2).
\tag{15}
\]
Indeed the dual of \(\mathrm{Sp}(2)\) has the reversed two lines and monodromy \(-N^{\mathsf T}\); reversing and rescaling the basis identifies it with \(\|\cdot\|^{-1}\mathrm{Sp}(2)\). The kernel in (15) has character \(\chi\), so its geometric Frobenius eigenvalue is \(\chi(\Phi)\), rather than \(q^{-1}\chi(\Phi)\).

## 5. Conductors and the four factors

Let \(f_F(E)\) be the Artin conductor exponent of \(V_\ell E\). For its Weil–Deligne pair, write \(\delta=\mathrm{Sw}(r)\). The conductor formula is
\[
f_F(E)=\delta+2-\dim(\ker N)^I.
\tag{16}
\]
Dualizing leaves the conductor unchanged: averaging over finite inertia identifies invariant spaces in a representation and its dual; the ranks of \(N\) and its transpose on them agree. The Swan terms agree as well because finite-group invariant dimensions agree at every ramification subgroup.

**Theorem 5.1.** The conductor exponent is zero for good reduction, one for multiplicative reduction, and \(2+\delta\ge2\) for additive reduction. For \(p\ge5\), additive reduction has \(\delta=0\). The local factors in the convention (2) are
\[
L_F(E,s)=
\begin{cases}
(1-a_Eq^{-s}+q^{1-2s})^{-1},&\text{good},\\
(1-q^{-s})^{-1},&\text{split multiplicative},\\
(1+q^{-s})^{-1},&\text{nonsplit multiplicative},\\
1,&\text{additive}.
\end{cases}
\tag{17}
\]

*Proof.* For good reduction, \(N=0\), inertia is trivial, and the Swan term is zero; (16) gives zero and Proposition 2.1 gives the factor. For multiplicative reduction, \(\chi\) in (13) is unramified. The invariant kernel is one-dimensional, so (16) gives one. Equation (15) gives a one-dimensional kernel with Frobenius eigenvalue one in the split case and minus one in the nonsplit case, proving the two linear factors.

For additive potentially good reduction, Proposition 2.2 gives \(N=0\) and no inertia invariants. For additive potentially multiplicative reduction, \(\chi\) is ramified, so the smooth inertia action in (13) is a nontrivial scalar quadratic character. It also has no invariant vectors, hence no invariant kernel. In both cases (16) gives \(2+\delta\), and the corresponding invariant kernel of the dual is zero, giving factor 1.

When \(p\ge5\), Proposition 2.2 makes potential-good inertia tame. A ramified quadratic character is also tame when \(p\ne2\), since a pro-\(p\) group has no nontrivial quotient of order two. This covers the potentially multiplicative additive case as well. ∎

In the latter case one can say more: the smooth representation is \(\chi\oplus\chi\|\cdot\|\), so \(f_F(E)=2a(\chi)=2+2\mathrm{Sw}(\chi)\). At \(p=3\) such a quadratic twist is tame; positive Swan terms there come from potentially good reduction. No universal claim \(f=2\) is made at 2 or 3.

The general geometric conductor-discriminant theorem is Ogg's formula
\[
f_F(E)=v(\Delta_{\min})+1-M,
\tag{18}
\]
where \(M\) is the number of geometric irreducible components of the special fiber of the minimal regular model. For every good curve the smooth model has \(M=1\), \(v(\Delta)=0\) and \(f=0\), proving (18). For every multiplicative curve, the resolution in Lemma 4.0 proves \(M=n=v(\Delta)\), while Theorem 5.1 proves \(f=1\), again proving (18); unramified tangent splitting does not change these geometric counts or valuations. Tate's algorithm determines the Kodaira type and this number in general. Lemmas 6.0A–F and Proposition 6.0G below prove all additive preparations, termination and their regular-model fibre graphs directly. A proof of (18) for every additive elliptic curve, and the general minimal-model identification and uniqueness, remain required geometric obligations in this draft; §7 records them explicitly. The concrete branches and wild conductors used in §6 are proved there by resolutions and torsion-field ramification, independently of (18). In particular the general theorem is retained, without treating a citation or a numerical check as its proof.

## 6. Three complete local computations

For checking the arithmetic, use
\[
\begin{aligned}
b_2&=a_1^2+4a_2,& b_4&=a_1a_3+2a_4,\\
b_6&=a_3^2+4a_6,& b_8&=a_1^2a_6-a_1a_3a_4+4a_2a_6+a_2a_3^2-a_4^2,\\
c_4&=b_2^2-24b_4,&
\Delta&=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6.
\end{aligned}
\tag{19}
\]
All three discriminant valuations below are less than 12, which already proves local minimality.

We shall calculate the two wild conductors directly, so their values do not depend on invoking (18). The following elementary ramification calculation supplies the needed details. We may make an unramified base extension, which changes neither inertia nor its conductor, and work over the maximal unramified henselian extension \(K\). Every finite field and coordinate calculation used below descends to a finite unramified extension of the original field. More concretely, the finite faithful inertia image is detected at a sufficiently high prime-to-\(p\) torsion level: its decreasing kernels stabilize at the trivial kernel. That torsion field is finite Galois. After taking its finite unramified subfield as base, its Galois group is precisely the inertia image and the remaining extension is totally ramified. This justifies applying the ordinary finite local-field different calculations to the full inertia fields below.

**Lemma 6.0.** Let \(M\) have residue characteristic 2, normalized valuation \(v_M\), and \(e=v_M(2)\). Suppose a nonsquare unit \(d\) has a unit approximation \(a\) with
\(v_M(d-a^2)=2h+1<2e\). Then this odd valuation is the best square approximation, \(M(\sqrt d)/M\) is totally ramified, and its different exponent is \(2e-2h\).

*Proof.* Changing \(a\) by \(b\) changes its square by \(2ab+b^2\). If \(v_M(b)<e\), that change has even valuation \(2v_M(b)\); if \(v_M(b)\ge e\), it has valuation at least \(2e\). Neither can cancel the specified odd term. A better approximation would have the same residue as \(a\), so these are all the possibilities. If \(\pi_M\) is a uniformizer, then
\(\beta=(\sqrt d-a)/\pi_M^h\) satisfies
\[
\beta^2+(2a/\pi_M^h)\beta-(d-a^2)/\pi_M^{2h}=0.
\tag{19a}
\]
This polynomial is Eisenstein. Its root is a uniformizer of the quadratic extension, and \(1,\beta\) give an integral basis: the two terms in \(A+B\beta\) have valuations \(2v_M(A)\) and \(2v_M(B)+1\), of different parity, so integrality forces \(A,B\) to be integral. Its derivative at \(\beta\) has valuation \(2e-2h\) in the extension, since its two terms have valuations \(2e+1\) and \(2e-2h\).

For completeness, the derivative calculates the different for a monogenic separable extension because the trace-dual of its power basis is contained in \(f'(\beta)^{-1}\mathcal O_M[\beta]\) and spans that fractional ideal. Lagrange interpolation gives
\(\operatorname{Tr}(\beta^j/f'(\beta))=0\) for \(j<\deg f-1\), and one for \(j=\deg f-1\); applying this successively gives the dual basis. Thus the inverse different, defined by integral traces, is exactly that ideal. Trace composition and the composed dual bases also prove transitivity
\[
d(L/K)=e(L/M)d(M/K)+d(L/M)
\tag{19b}
\]
for totally ramified towers. For a totally ramified Galois extension, use a uniformizer integral basis and factor its derivative as \(\prod_{g\ne1}(\pi_L-g\pi_L)\). The definition of the lower ramification groups then proves
\[
d(L/K)=\sum_{i\ge0}(|G_i|-1).
\tag{19c}
\]
For the Galois formula, a uniformizer has degree equal to the total ramification degree; its power basis is integral by the same argument with valuations in distinct classes modulo that degree. A tame totally ramified quadratic extension in odd residue characteristic has a uniformizer satisfying \(T^2-\pi_M u\), with \(u\) a unit, and derivative valuation one. Units whose residues are squares are squares by Hensel lifting, which proves this description after our unramified base extension. These arguments prove all the local different formulas used below. ∎

**Lemma 6.0U (finite unramified splitting and regularity descent).** Let \(R\) be a complete DVR with residue field \(k\). Every finite separable extension of \(k\) is the residue field of a finite free complete DVR extension \(R'/R\) with the same uniformizer. Thus finitely many separable residue equations split after such an extension. These statements apply to infinite perfect \(k\) as well as finite \(k\). Regularity of the finite-type models below can be checked after this extension.

*Proof.* First adjoin one residue element, with monic separable irreducible polynomial \(\bar f\in k[T]\). Lift its coefficients to a monic \(f\in R[T]\) and put \(B=R[T]/(f)\). Monic division gives the basis \(1,T,\ldots,T^{d-1}\), so \(B\) is finite free and complete, and \(B/\pi B=k[T]/(\bar f)\) is a field. An element with nonzero residue is a unit: lift its residue inverse; the remaining factor is \(1+\pi z\), inverted by its convergent geometric series. For any nonzero element, the minimum valuation of its finitely many basis coordinates gives a factorization \(\pi^a u\), with \(u\) a unit. Multiplication by \(\pi\) is injective by freeness. These facts prove that \(B\) is a domain and that every nonzero ideal is generated by a power of \(\pi\), by taking the least such exponent in that ideal. It is a complete DVR, with ramification index one and the required residue field. A finite separable extension has finitely many generators; applying this construction to their successive separable minimal polynomials proves the general assertion.

The derivative \(f'\) is a unit in \(B\), because \(\bar f\) is separable. Its simple roots lift uniquely by the complete-DVR Hensel proof in lesson 1, Lemma 0D.1. In a finite Galois residue splitting field, each residue automorphism consequently lifts uniquely through the chosen generator tower, and uniqueness gives the group law. Invariant centres and their blowups therefore descend; the flat base-change calculation for their Rees algebras is *Blowing up*, Theorem 4.1(4).

Here is also the local regularity check. At a point over a local ring \((A,\mathfrak m,\kappa)\) of a model, let \((A',\mathfrak n,\kappa')\) be the localized base change. Its residue fibre is the localization of a finite separable \(\kappa\)-algebra, hence a field: the separable minimal polynomials factor into distinct irreducibles after extension, and the Chinese remainder theorem gives that product of fields. Thus \(\mathfrak n=\mathfrak mA'\). Flatness identifies
\(\mathfrak n/\mathfrak n^2=(\mathfrak m/\mathfrak m^2)\otimes_\kappa\kappa'\).
The actually proved flat local dimension formula in *Dimension theory of Noetherian local rings*, Theorem 5.1, gives \(\dim A'=\dim A\), since the fibre has dimension zero. Their cotangent dimensions are equal as well. Equality of dimension and cotangent dimension therefore holds for one exactly when it holds for the other. This proves the asserted regularity descent. ∎

**Lemma 6.0A (the first three additive resolutions, in every residue characteristic).** Let \(R\) be a complete DVR with perfect residue field, uniformizer \(\pi\), and a nonsingular generic Weierstrass cubic. Translate its singular special point to \((0,0)\), so \(\pi\mid a_3,a_4,a_6\), and suppose \(\pi\mid b_2\). The following tests construct proper regular models with the indicated geometric special fibres:

| First test that terminates | Fibre | Geometric components |
|:---|:---|---:|
| \(\pi^2\nmid a_6\) | one cuspidal cubic, type \(II\) | 1 |
| \(\pi^2\mid a_6,\ \pi^3\nmid b_8\) | two smooth rational curves tangent with intersection length two, type \(III\) | 2 |
| \(\pi^2\mid a_6,\ \pi^3\mid b_8,\ \pi^3\nmid b_6\) | three smooth rational curves through one point, each pair of intersection length one, type \(IV\) | 3 |

These calculations do not use the conductor-discriminant formula.

*Proof.* We may check the geometry after an unramified extension splitting the finitely many residue equations. All such extensions descend to finite unramified extensions. The repeated tangent is a square: in odd characteristic complete the square in
\(Y^2+\bar a_1XY-\bar a_2X^2\); in characteristic two, \(\bar b_2=0\) gives \(\bar a_1=0\), and perfection supplies the square root of \(\bar a_2\). Replacing \(y\) by \(y+\alpha x\), for a lift of this tangent slope, makes
\(\pi\mid a_1,a_2\) as well, without changing \(a_6\), \(b_6\), \(b_8\), or \(\Delta\). The special equation is now \(y^2=x^3\).

In the first case the local equation has a nonzero linear term in \(\pi\) in the regular ambient local ring with parameters \(\pi,x,y\): write \(a_6=\pi A_6\), with \(A_6\) a unit. Hence its maximal ideal on the surface is generated by \(x,y\), and its dimension is two, proving regularity. The other fibre points, including infinity, are smooth over \(R\). The projective cubic itself is therefore a regular proper model with its single cuspidal component.

For the other two cases write
\[
a_1=\pi A_1,\quad a_2=\pi A_2,\quad
a_3=\pi A_3,\quad a_6=\pi^2A_6.
\]
Blow up the ambient closed point \((\pi,x,y)\) and take the strict transform of the cubic. Its exceptional curve is the projective tangent conic
\[
Q(X,Y,T)=Y^2+\bar A_3YT-\overline{a_4/\pi}\,XT-\bar A_6T^2=0.
\tag{19d}
\]
The terms in \(b_8/\pi^2\) other than \(-(a_4/\pi)^2\) vanish modulo \(\pi\), since \(a_1,a_2,a_3\) are divisible by \(\pi\). Thus the second case makes \(A_4=a_4/\pi\) a unit. The conic is smooth in every characteristic: its \(X\)-partial forces \(T=0\) at a proposed singular point, its equation then forces \(Y=0\), and its \(T\)-partial forces \(X=0\). No projective point satisfies these conditions.

Here is the full regularity check for this blowup rule. In each of the three affine ambient blowup charts, divide the cubic equation by the square of the chart parameter. On its exceptional divisor the resulting equation is an affine chart of \(Q\). Smoothness of the conic makes one of its two affine partial derivatives a unit at each point, so the strict-transform local ring has a two-generator maximal ideal and dimension two. It is regular there. Away from the exceptional divisor the blowup is an isomorphism and the original cubic is smooth. The exceptional conic is a projective line over the algebraically closed residue field. The strict transform of the original cusp is its smooth rational normalization.

To check their intersection, the \(x\)-chart has \(\pi=xv,\ y=xu\) and equation
\[
u^2+xvA_1u+vA_3u-x-xvA_2-vA_4-v^2A_6=0.
\tag{19e}
\]
Their common point is \(x=u=v=0\). The \(v\)-coefficient there is the unit \(-A_4\), giving regularity once more. The two components are \(x=0\) and \(v=0\). Their scheme-theoretic intersection sets \(x=v=0\) in (19e), leaving \(u^2=0\); it has length two. Each component has multiplicity one, as \(\pi=xv\) shows at its generic point. The total fibre is principal, so intersection with it is zero; each component consequently has self-intersection \(-2\).

In the third case \(b_8/\pi^2\equiv0\) instead gives \(a_4=\pi^2A_4\). Now (19d) is
\[
Y^2+\bar A_3YT-\bar A_6T^2
=(Y-\beta T)(Y-\gamma T),\qquad \beta\ne\gamma,
\]
because its discriminant is \(b_6/\pi^2\not\equiv0\). In characteristic two that discriminant is \(\bar A_3^2\); its nonvanishing is exactly separability of this quadratic. The two exceptional lines are regular away from their intersection, by the same affine-partial argument. Their sole intersection, and the point of the strict transform of the cusp, is \([X:Y:T]=[1:0:0]\). The \(x\)-chart at this point has
\[
x(1+vA_2+v^2A_4-vA_1u)
=u^2+vA_3u-v^2A_6,\qquad \pi=xv.
\tag{19f}
\]
The parenthesized factor is a unit. The surface maximal ideal is therefore generated by \(u,v\): the equation expresses \(x\) in their square, and \(\pi=xv\) then lies in their cube. Dimension two proves regularity. On its special fibre (19f) eliminates \(x\) and gives, up to a unit,
\[
v(u-\beta v)(u-\gamma v)=0.
\]
This proves that all three components have multiplicity one, have three distinct tangent directions, and meet pairwise with length one. Both exceptional components are projective lines; the remaining component is the now smooth normalization of the cubic. They each have self-intersection \(-2\), since the other two intersections contribute two to the principal total fibre. Thus these regular models contain no geometric rational fibre component of self-intersection \(-1\); the type-\(II\) model's sole component has self-intersection zero. The relative-minimality condition is verified directly. The general existence, uniqueness and contraction theory of minimal regular models remains a foundation needed for the full algorithm, together with the later additive branches and the conductor theorem; none is inferred from this local calculation. ∎

**Lemma 6.0B (three simple cubic roots).** Suppose the integral equation has
\[
a_1=\pi A_1,\quad a_2=\pi A_2,\quad
a_3=\pi^2A_3,\quad a_4=\pi^2A_4,\quad a_6=\pi^3A_6.
\]
If
\[
\bar P(T)=T^3+\bar A_2T^2+\bar A_4T+\bar A_6
\]
has three distinct geometric roots, the following blowups give a regular proper fibre of type \(I_0^*\): a multiplicity-two projective line with four multiplicity-one projective lines attached at distinct points. In particular it has five geometric components, all of self-intersection \(-2\). This assertion includes residue characteristics two and three.

*Proof.* Blow up \((\pi,x,y)\). In the \(\pi\)-chart, \(x=\pi x_1,\ y=\pi y_1\), the strict transform is
\[
y_1^2+\pi(A_1x_1+A_3)y_1
=\pi P(x_1),\qquad
P(T)=T^3+A_2T^2+A_4T+A_6.
\tag{19g}
\]
The exceptional line \(y_1=\pi=0\) has multiplicity two. At a point where \(\bar P(x_1)\ne0\), its equation solves \(\pi\) as \(y_1^2\) times a unit, so the local surface is regular. The only singular points in this chart are the three roots of \(\bar P\). Indeed at such a point the equation has no linear term in the regular ambient parameters \(\pi,y_1,x_1-r\), whereas elsewhere the \(\pi\)-linear term is a unit.

For completeness the part of the exceptional line missing from this chart lies in the \(x\)-chart. Put \(\pi=xv,\ y=xu\). Its equation is
\[
x\,U(u,v)=u^2,\qquad
U=1+vA_2+v^2A_4+v^3A_6-vA_1u-v^2A_3u.
\tag{19h}
\]
At \(x=u=v=0\), \(U\) is a unit, so the surface maximal ideal is generated by \(u,v\). It is regular. The base parameter is \(u^2v/U\). Thus the strict transform of the cubic, \(v=0\), has multiplicity one, and the exceptional component, \(u=0\), has multiplicity two; they meet transversely. The cubic has been normalized there by \(x=u^2,\ y=u^3\) on the special fibre. Every other point of the \(x\)-chart with \(v\ne0\) belongs to the \(\pi\)-chart; the \(y\)-chart has no further exceptional point, since the projective tangent cone is \(Y^2=0\). All remaining original points were smooth. Consequently no further singularity was omitted.

Lift each geometric root \(r\) to \(R\), after the finite unramified residue extension needed to split \(\bar P\), and put \(s=x_1-r\). Then \(P(r)\in\pi R\) and \(P'(r)\) is a unit. The tangent cone of (19g) at this point, with coordinates \([\Pi:S:Y]\), is
\[
Y^2+c\Pi Y-d\Pi S-b\Pi^2=0,\qquad
d=\overline{P'(r)}\ne0,\quad
b=\overline{P(r)/\pi},\quad
c=\overline{A_1r+A_3}.
\tag{19i}
\]
It is smooth in every characteristic. The \(S\)-partial first gives \(\Pi=0\) at a proposed singular point; the equation then gives \(Y=0\), and the \(\Pi\)-partial gives \(S=0\). The all-chart blowup proof following (19d) therefore resolves this point with one smooth projective conic, geometrically a projective line. Its multiplicity is one: on its dense chart \(\Pi\ne0\), the base parameter \(\pi\) is the blowup parameter times a unit.

Its intersection with the old doubled line is the unique tangent direction \([0:1:0]\). In the \(s\)-chart write \(\pi=s v,\ y_1=s w\). Dividing (19g) by \(s^2\) gives a \(v\)-linear coefficient \(-P'(r)\), a unit at this point. Thus \(s,w\) are regular surface parameters, and the equation expresses \(v=w^2\) times a unit there. The total fibre parameter \(\pi=sv\) is consequently \(s w^2\) times a unit. The new component \(s=0\) and the old component \(w=0\) meet with length one and have multiplicities one and two. The three root points were distinct, so these new components are pairwise disjoint and disjoint from the original endpoint.

There are now five components: the strict cubic normalization, the first exceptional line and the three conics. Intersecting the principal total fibre with a multiplicity-one endpoint gives \(C^2+2=0\). For the central line the four endpoints give \(2C^2+4=0\). Thus every self-intersection is \(-2\); the displayed fibre satisfies the relative-minimality condition and is the \(I_0^*\) graph. The blowups are projective, preserve the generic fibre and are regular everywhere by the preceding checks. The splitting calculation descends since the three centres form the separable root locus of \(\bar P\); blowing up their invariant union commutes with the finite unramified extension. This proves the stated resolution over the original DVR and its geometric fibre description. It does not prove the remaining general minimal-model uniqueness or conductor identity. ∎

**Lemma 6.0C (the separated quadratic in the triple-cubic branch).** Suppose the already prepared equation has
\[
a_1=\pi A_1,\quad a_2=\pi^2A_2,\quad
a_3=\pi^2A_3,\quad a_4=\pi^3A_4,\quad a_6=\pi^4A_6.
\]
If \(\bar Q(T)=T^2+\bar A_3T-\bar A_6\) has two distinct geometric roots, its regular proper resolution has the \(IV^*\) fibre: a central multiplicity-three projective line, three multiplicity-two projective lines attached to it, and a multiplicity-one endpoint attached to each of those. All seven components have self-intersection \(-2\). The proof holds in every residue characteristic. Preparation of this equation from every equation in the algorithm is a separate assertion.

*Proof.* The first blowup has \(\pi\)-chart
\[
y_1^2+\pi A_1x_1y_1+\pi A_3y_1
 =\pi x_1^3+\pi^2 A_2x_1^2+\pi^2 A_4x_1+\pi^2 A_6.
\tag{19j}
\]
Its exceptional component has multiplicity two. Only its origin is singular: away from \(x_1=0\) the coefficient of the linear term in \(\pi\) is \(-x_1^3\), a unit. In the missing \(x\)-chart, \(\pi=xv,\ y=xu\), the equation is
\[
x\bigl(1-vA_1u-v^2A_3u+
             x(v^2A_2+v^3A_4+v^4A_6)\bigr)=u^2.
\]
The bracket is a unit at \(x=u=v=0\). Thus this point is regular, the fibre parameter is \(u^2v\) times a unit, and the original multiplicity-one component meets the doubled component transversely there. Every other exceptional point is in (19j); the tangent cone \(Y^2=0\) leaves no additional \(y\)-chart point.

Blow up the origin of (19j). Its \(\pi\)-chart is
\[
y_2^2+\pi A_1x_2y_2+A_3y_2
 =\pi^2x_2^3+\pi^2A_2x_2^2+\pi A_4x_2+A_6.
\tag{19k}
\]
The exceptional locus consists of the two distinct lines \(\bar Q(y_2)=0\). At each, \(2y_2+A_3\) is a unit, even in characteristic two. This chart is regular, and both lines have multiplicity one. Their missing points lie in the \(x_1\)-chart. Put \(x_1=t,\ \pi=tv,\ y_1=tw\); its equation is
\[
w^2+vA_3w-v^2A_6+
 tvA_1w-tv^2A_4-t^2v-t^2v^2A_2=0,\qquad \pi=tv.
\tag{19l}
\]
At \(t=0\), the two directions \(w/v\) are the roots of \(\bar Q\). If \(v\ne0\), the derivative in \(w\) is a unit. On the strict old doubled component \(v=w=0\), if \(t\ne0\), the derivative in \(v\) is a unit. Thus only \(t=v=w=0\) remains singular. The projective tangent cone of the second blowup is \(Q(Y,\Pi)=0\), so its \(y_1\)-chart adds no exceptional direction beyond the \(\pi\)- and \(x_1\)-charts just checked.

Work after the finite unramified extension splitting \(\bar Q\). Choose a lift \(\beta\) of one root and set
\[
z=w-\beta v,\qquad d=2\beta+A_3,\qquad
B=(\beta^2+A_3\beta-A_6)/\pi,\qquad E=A_1\beta-A_4.
\]
Here \(d\) is a unit and \(B\) is integral; these are exact coefficient identities. Since \(\pi=tv\), (19l) becomes
\[
z^2+dvz+tvA_1z+tv^2E+tBv^3-t^2v(1+vA_2)=0.
\tag{19m}
\]
Its tangent cone consists of the two planes \(z=0\) and \(z=-dv\).

Blow up its origin. In the \(t\)-chart, \(v=tV,\ z=tZ\), the strict transform is
\[
Z^2+dVZ+tVA_1Z+tV^2E+t^2BV^3-tV-t^2V^2A_2=0,
\qquad \pi=t^2V.
\tag{19n}
\]
The two new exceptional lines \(t=0,\ Z=0\) and \(t=0,\ Z=-dV\) have multiplicity two at their generic points, where \(V\ne0\). All their points with \(V\ne0\) are regular, since the derivative in \(Z\) is \(dV\) or \(-dV\). Only their common point \(t=V=Z=0\) remains singular in this chart. The strict old doubled component is \(V=Z=0\); at its points with \(t\ne0\), the derivative in \(V\) is a unit.

The other essential chart is the \(v\)-chart, \(t=vX,\ z=vZ\):
\[
Z^2+dZ+vXA_1Z+vXE+v^2XB-vX^2-v^2X^2A_2=0,
\qquad \pi=v^2X.
\tag{19o}
\]
On \(v=0\) the roots \(Z=0,-d\) have nonzero derivative in \(Z\), so this entire exceptional part is regular. The old multiplicity-one lines have \(X=0\), and meet these doubled lines transversely: eliminate \(Z\) to use the regular parameters \(v,X\), for which the fibre parameter is exactly \(v^2X\). The \(z\)-chart has no further direction, because its exceptional directions satisfy \(z(z+dv)=0\), and a direction with \(z\ne0\) necessarily has \(v\ne0\). Outside the exceptional locus the blowup is an isomorphism. This checks every chart.

At the remaining origin of (19n), the tangent cone, in projective coordinates \([T:V:Z]\), is
\[
Z^2+dVZ-TV=0.
\tag{19p}
\]
It is smooth in all characteristics: the \(T\)-partial forces \(V=0\), the equation forces \(Z=0\), and the \(V\)-partial then forces \(T=0\). The conic-chart argument in Lemma 6.0A resolves this point by one blowup and adds a smooth projective conic, geometrically a projective line. Its generic multiplicity is three, since the fibre parameter \(t^2V\) has degree three in the blowup parameters and is not identically zero on that conic.

We also check the intersections, rather than deduce them from a named graph. The three doubled components have the distinct tangent directions
\[
[1:0:0],\qquad [0:1:0],\qquad [0:1:-d]
\]
on (19p). In the last \(t\)-chart, put \(V=ta,\ Z=tb\). Its equation has initial expression \(b^2+dab-a\); its derivative in \(a\) at \(a=b=t=0\) is a unit. The equation expresses \(a=b^2\) times a unit. Thus \(\pi=t^3a\) is \(t^3b^2\) times a unit: the new tripled line and the strict old doubled line meet transversely. In the last \(V\)-chart, put \(t=Va,\ Z=Vb\). Along its exceptional divisor its equation is \(b^2+db-a=0\). At \(a=0,\ b=0\) or \(-d\), the derivative in \(b\) is a unit. The regular surface parameters are \(V,a\), with \(\pi=V^3a^2\). This proves the other two transverse intersections and their multiplicities. The distinct tangent directions separate the doubled components from each other.

The three endpoints remain the original cubic normalization and the two lines from (19k); the preceding charts prove each endpoint meets just its own doubled line. There are therefore exactly seven geometric components with the stated multiplicities and incidence. Intersecting the principal total fibre with an endpoint gives \(C^2+2=0\); with a doubled line gives \(2C^2+3+1=0\); with the central line gives \(3C^2+2+2+2=0\). Every self-intersection is \(-2\). These projective blowups preserve the generic curve and give a regular proper model satisfying the relative-minimality condition.

The blowup centres are the successive invariant singular points, and the unordered pair of separated lines is intrinsic. The construction descends from the finite unramified splitting extension. Choosing \(\beta\) only describes its charts; it introduces no extra centre or field-dependent modification. This proves the stated all-characteristic \(IV^*\) branch. General minimal-model uniqueness, preparation and the conductor identity remain separate proof obligations. ∎

**Lemma 6.0D (the \(III^*\) branch).** Suppose the prepared equation satisfies
\[
\pi\mid a_1,\quad \pi^2\mid a_2,\quad \pi^3\mid a_3,\quad
v(a_4)=3,\quad \pi^5\mid a_6.
\]
Its regular proper resolution has eight geometric projective-line components: a central component of multiplicity four, two arms of multiplicities \(3,2,1\) starting from that centre, and one additional multiplicity-two component attached directly to it. All self-intersections are \(-2\). This is the \(III^*\) fibre, in every residue characteristic.

*Proof.* First arrange \(\pi^6\mid a_6\). Put \(a_4=\pi^3A_4,\ a_6=\pi^5C_6\), with \(A_4\) a unit, and translate \(x=X+\pi^2r\), choosing \(r\equiv-C_6/A_4\pmod\pi\). The constant coefficient becomes
\[
a_6+\pi^2ra_4+\pi^4r^2a_2+\pi^6r^3,
\]
which is divisible by \(\pi^6\). The new coefficients are \(a_2+3\pi^2r\), \(a_3+\pi^2ra_1\) and \(a_4+2\pi^2ra_2+3\pi^4r^2\); they preserve all the displayed divisibilities and the unit value of \(a_4/\pi^3\). This translation does not change the discriminant. Write the resulting coefficients as
\[
a_1=\pi A_1,\quad a_2=\pi^2A_2,\quad
a_3=\pi^3A_3,\quad a_4=\pi^3A_4,\quad a_6=\pi^6A_6.
\]

The first blowup of the singular cubic has one doubled exceptional line and the original multiplicity-one endpoint, meeting as in (19j). Its \(\pi\)-chart is
\[
y_1^2+\pi A_1x_1y_1+\pi^2A_3y_1
 =\pi x_1^3+\pi^2A_2x_1^2+\pi^2A_4x_1+\pi^4A_6.
\]
Only its origin is singular. In the missing \(x\)-chart the coefficient of \(x\) is a unit at the intersection with the original component, and the fibre parameter is \(u^2v\) times a unit, exactly as in Lemma 6.0C.

The second blowup's \(\pi\)-chart is
\[
y_2^2+\pi A_1x_2y_2+\pi A_3y_2
 =\pi^2x_2^3+\pi^2A_2x_2^2+\pi A_4x_2+\pi^2A_6.
\tag{19q}
\]
Its exceptional line has multiplicity two. Away from its origin the linear \(\pi\)-coefficient is a unit, since \(A_4\) is a unit. At its origin the tangent cone is
\[
Y^2+\bar A_3\Pi Y-\bar A_4\Pi X-\bar A_6\Pi^2=0.
\]
It is smooth by the same partial-derivative test as (19i). One blowup resolves this point and adds a multiplicity-one endpoint. The old doubled line has tangent direction \([0:1:0]\), and the corresponding \(x_2\)-chart has fibre parameter \(s w^2\) times a unit, as in the root-point calculation of Lemma 6.0B. Thus this endpoint meets that doubled line transversely.

There is a different singular point missing from (19q). In the second \(x_1\)-chart set \(x_1=t,\ \pi=tv,\ y_1=tw\). Its exact equation is
\[
w^2+tv(A_1+vA_3)w-t^2v(1+vA_2)-tv^2A_4-t^2v^4A_6=0.
\tag{19r}
\]
Only \(t=v=w=0\) is singular here. Indeed on \(t=0,\ w=0,\ v\ne0\), its \(t\)-linear coefficient is \(-v^2A_4\), a unit; on \(v=w=0,\ t\ne0\), the \(v\)-linear coefficient is \(-t^2\), a unit. The old doubled line and the new doubled line meet at this origin. The \(\pi\)-chart origin just resolved is its other endpoint, corresponding to \(v=\infty\); hence the two centres are distinct.

Blow up the origin of (19r). Its two essential charts are
\[
\begin{aligned}
W^2+tVA_1W+t^2V^2A_3W-tV-t^2V^2A_2-tV^2A_4-t^4V^4A_6&=0,
&\pi&=t^2V,\\
W^2+vXA_1W+v^2XA_3W-vX^2-v^2X^2A_2-vXA_4-v^4X^2A_6&=0,
&\pi&=v^2X.
\end{aligned}
\tag{19s}
\]
The substitutions are \(v=tV,\ w=tW\) and \(t=vX,\ w=vW\), respectively. The exceptional component is geometrically one line. Its multiplicity is four: at a generic point the first equation solves \(t=W^2\) times a unit because \(V(1+A_4V)\ne0\), and \(\pi=t^2V\). The only singular points on this line are \(V=0\), \(V=-1/\bar A_4\), and the missing point \(X=0\). The middle point is also \(X=-\bar A_4\) in the other chart, so it is counted once. The \(w\)-chart has no extra exceptional direction because the tangent cone of (19r) is \(w^2=0\).

At \(V=0\) the tangent cone of the first equation in (19s) is \(W^2-tV\); at \(X=0\) the second has tangent cone \(W^2-\bar A_4vX\). Both are smooth conics in every characteristic. Blow up these two points. Each new component has multiplicity three, since \(\pi=t^2V\) or \(v^2X\) has degree three and is not identically zero on the conic. Each separates its old multiplicity-two line from the multiplicity-four line. More precisely, in the \(t\)-chart at \(V=0\), write \(V=ta,\ W=tb\). The strict-transform equation is \(b^2-a\) plus terms divisible by \(a\) and by \(t\); hence \(a=b^2\) times a unit and \(\pi=t^3b^2\) times a unit. In the \(V\)-chart, write \(t=Va,\ W=Vb\); again \(a=b^2\) times a unit, now with \(\pi=V^3b^4\) times a unit. These are the transverse intersections of the tripled line with the old doubled and quadrupled lines. At \(X=0\), the identical calculation has \(b^2-\bar A_4a\) in place of \(b^2-a\); the unit \(A_4\) gives the same two multiplicities and transverse intersections.

It remains to resolve the third point. Choose a lift \(r\) of \(-1/\bar A_4\), and put \(s=V-r\). The polynomial \(q(V)=V(1+A_4V)\) has \(q(r)\in\pi R\), and \(q'(r)\) is a unit, since its reduction at this root is \(-1\). Also \(\pi=t^2V\), so \(q(r)\in t^2R[V]\) locally. The quadratic tangent cone is therefore
\[
W^2+c\,tW-d\,ts-b\,t^2=0,\qquad d=\overline{q'(r)}\ne0
\]
for suitable residue coefficients \(b,c\). The \(s\)-partial, equation and \(t\)-partial show successively that \(t=W=s=0\) at a proposed projective singular point; the conic is smooth. Its blowup adds a component of multiplicity two, since \(V\) is a unit and \(\pi=t^2V\). In the \(s\)-chart \(t=sa,\ W=sb\), the equation has a unit \(a\)-linear coefficient. It gives \(a=b^2\) times a unit, so \(\pi=s^2b^4\) times a unit. This new doubled component meets the quadrupled one transversely and meets no other component.

The conic-chart argument proves regularity at every point of these last three blowups; away from their centres the preceding charts were regular. We have checked all exceptional directions, so the resolution is complete. Its eight components are the original endpoint, the first doubled line, the second doubled line and its endpoint, the quadrupled line, and the three last conics of multiplicities \(3,3,2\). The first two tripled conics give the arms \(4\!-\!3\!-\!2\!-\!1\); the last conic gives the third arm \(4\!-\!2\). All intersections are transverse of length one, as just proved.

The principal fibre equation gives self-intersection \(-2\) on every component: adjacent multiplicities are respectively \(2\), \(3+1\), \(4+2\), \(3+3+2\), or \(4\), each twice the multiplicity of that component. Thus no geometric rational vertical \(-1\) component occurs. All centres and blowups are intrinsic and defined over the original residue field; no splitting extension is needed. The resolution is projective and proper. This proves the prepared \(III^*\) branch, while the general conductor identity and minimal-model uniqueness remain separate obligations. ∎

**Lemma 6.0E (the \(II^*\) branch).** Suppose the prepared equation satisfies
\[
a_1=\pi A_1,\quad a_2=\pi^2A_2,\quad
a_3=\pi^3A_3,\quad a_4=\pi^4A_4,\quad a_6=\pi^5A_6,
\qquad A_6\in R^\times.
\]
Its regular proper resolution has the \(II^*\) fibre in every residue characteristic. Its central component has multiplicity six; its three arms, starting from that centre, have multiplicities \(5,4,3,2,1\), \(4,2\), and \(3\). All nine geometric components are projective lines of self-intersection \(-2\).

*Proof.* The first blowup has
\[
y_1^2+\pi A_1x_1y_1+\pi^2A_3y_1
 =\pi x_1^3+\pi^2A_2x_1^2+\pi^3A_4x_1+\pi^3A_6
\]
in its \(\pi\)-chart. Only its origin is singular. Its doubled line meets the original multiplicity-one component transversely at the regular missing \(x\)-chart point, by the same unit-coefficient and \(u^2v\) calculation as Lemma 6.0C. Blow up its remaining origin. The second \(\pi\)-chart is
\[
y_2^2+\pi A_1x_2y_2+\pi A_3y_2
 =\pi^2x_2^3+\pi^2A_2x_2^2+\pi^2A_4x_2+\pi A_6.
\tag{19t}
\]
This whole exceptional chart is regular: its coefficient of the linear term in \(\pi\), on \(\pi=y_2=0\), is \(-A_6\), a unit. Its exceptional component has multiplicity two, since \(\pi=y_2^2\) times a unit there.

In the second \(x_1\)-chart, put \(x_1=t,\ \pi=tv,\ y_1=tw\). Its equation is
\[
w^2+tvA_1w+tv^2A_3w
 -t^2v(1+vA_2+v^2A_4)-tv^3A_6=0.
\tag{19u}
\]
Its only singular point is the origin. At \(t=w=0,\ v\ne0\), the \(t\)-linear coefficient is \(-v^3A_6\), a unit; at \(v=w=0,\ t\ne0\), the \(v\)-linear coefficient is \(-t^2\), a unit. The tangent cone is \(w^2=0\), so the \(y_1\)-chart leaves no exceptional direction beyond these \(\pi\)- and \(x_1\)-charts.

Blow up that origin. The essential \(t\)- and \(v\)-charts are
\[
\begin{aligned}
W^2+tVA_1W+t^2V^2A_3W-tV-t^2V^2A_2-t^3V^3A_4-t^2V^3A_6&=0,
&\pi&=t^2V,\\
W^2+vXA_1W+v^2XA_3W-vX^2-v^2X^2A_2-v^3X^2A_4-v^2XA_6&=0,
&\pi&=v^2X.
\end{aligned}
\tag{19v}
\]
The exceptional line has multiplicity four: at its generic point in the first chart \(V\ne0\), the equation gives \(t=W^2\) times a unit. That chart has just one singular point, \(t=V=W=0\). Its tangent cone is \(W^2-tV\), a smooth conic in all characteristics. Blow up this point. The new conic has multiplicity three and separates the first doubled line from the quadrupled line. The two intersection calculations are exactly the \(V=0\) calculation after (19s): in its \(t\)-chart the fibre parameter is \(t^3b^2\) times a unit, and in its \(V\)-chart it is \(V^3b^4\) times a unit. Hence both intersections are transverse. This produces the chain of multiplicities \(1,2,3,4\).

The second chart in (19v) has a different singular point, \(v=X=W=0\). It is the remaining end of the quadrupled line and the meeting point with the second doubled line. At its other exceptional points \(X\ne0\), the \(v\)-linear coefficient is \(-X^2\), a unit. Its tangent cone is again \(W^2=0\). Blow up this origin. The essential \(v\)- and \(X\)-charts, respectively \(X=vY,\ W=vZ\) and \(v=XU,\ W=XZ\), are
\[
\begin{aligned}
Z^2+vYA_1Z+v^2YA_3Z-vY^2-v^2Y^2A_2-v^3Y^2A_4-vYA_6&=0,
&\pi&=v^3Y,\\
Z^2+XUA_1Z+X^2U^2A_3Z-XU-X^2U^2A_2-X^3U^3A_4-XU^2A_6&=0,
&\pi&=X^3U^2.
\end{aligned}
\tag{19w}
\]
Its exceptional component has multiplicity six. In the first chart, away from \(Y=0,-\bar A_6\), its \(v\)-linear coefficient is \(-Y(Y+A_6)\), a unit; thus \(v=Z^2\) times a unit and \(\pi=v^3Y\) has multiplicity six. In the second chart the same statement uses the unit \(-U(1+A_6U)\) and \(\pi=X^3U^2\). There are precisely three singular points on this line: \(Y=0\), \(Y=-\bar A_6\), and \(U=0\). The second point also occurs as \(U=-1/\bar A_6\), so it is counted only once. No \(W\)-chart direction was omitted, since the previous tangent cone was \(W^2=0\).

At \(Y=0\) the quadratic tangent cone is
\[
Z^2-\bar A_6vY=0.
\]
At \(U=0\) it is
\[
Z^2-XU=0.
\]
They are smooth: in each case the two mixed-term partials force both other coordinates zero, and the equation then forces \(Z=0\). Blow up both points. The new conics have multiplicities four and five respectively, because the fibre parameters \(v^3Y\) and \(X^3U^2\) have degrees four and five, and neither vanishes identically on its conic.

The exact local intersections follow from the same divisions. At \(Y=0\), in the \(v\)-chart \(Y=va,\ Z=vb\), the equation gives \(a=b^2\) times a unit, and the fibre parameter is \(v^4b^2\) times a unit. In the \(Y\)-chart \(v=Ya,\ Z=Yb\), it gives \(a=b^2\) times a unit, and the fibre parameter is \(Y^4b^6\) times a unit. Thus the new multiplicity-four component joins the old second doubled line to the central sixfold line, with transverse intersections. At \(U=0\), the \(X\)-chart \(U=Xa,\ Z=Xb\) gives \(\pi=X^5b^4\) times a unit; the \(U\)-chart \(X=Ua,\ Z=Ub\) gives \(\pi=U^5b^6\) times a unit. The new multiplicity-five line therefore joins the old quadrupled line to the central sixfold one, again transversely.

Finally choose a lift \(r\) of \(-\bar A_6\) and put \(s=Y-r\). The polynomial \(q(Y)=Y(Y+A_6)\) has \(q(r)\in\pi R\) and \(q'(r)\) a unit, with residue \(-\bar A_6\). Since \(\pi=v^3Y\), the term \(-v q(r)\) has order at least four locally. The tangent cone at this last point is
\[
Z^2+c\,vZ-d\,vs-b\,v^2=0,\qquad d=\overline{q'(r)}\ne0.
\]
The mixed \(vs\) coefficient makes it a smooth conic by the test already used for (19i). Blowing up adds a multiplicity-three component, since \(Y\) is a unit and \(\pi=v^3Y\). The only old component meeting it is the sixfold line, in direction \([v:s:Z]=[0:1:0]\). In the \(s\)-chart \(v=sa,\ Z=sb\), the equation has unit \(a\)-linear coefficient and gives \(a=b^2\) times a unit. Hence \(\pi=s^3b^6\) times a unit. This proves the transverse intersection and both multiplicities.

Each last blowup is regular in every chart by its smooth tangent conic; all other points were checked regular in (19t)–(19w). These three points are distinct because \(A_6\) is a unit, so their blowups do not interfere. There are now nine geometric components. The initial \(1,2,3,4\) chain attaches through the new fivefold line to the sixfold centre; the other doubled line attaches through the new fourfold line; the last tripled line is the third arm. This is exactly the incidence claimed in the statement.

For each component, adjacent multiplicities add to twice its own multiplicity: along the long arm these sums are \(2\), \(1+3\), \(2+4\), \(3+5\), \(4+6\); on the shorter arm they are \(4\) and \(2+6\); on the last arm it is \(6\); at the centre it is \(5+4+3\). The principal fibre therefore gives self-intersection \(-2\) everywhere. The intrinsic centres and projective blowups are defined over the original DVR, and give a regular proper model with no geometric rational vertical \(-1\) component. This proves the prepared \(II^*\) branch, including residue characteristics two and three, without asserting the unproved general conductor or minimal-model uniqueness theorem. ∎

**Lemma 6.0F (coefficient preparations and termination).** Over a complete DVR with perfect residue field, the arithmetic preparations for every additive branch can be carried out after a finite unramified extension. Starting with the tangent normalization of Lemma 6.0A, its three stopping tests, the separated-cubic test of Lemma 6.0B, the separated-quadratic test of Lemma 6.0C, and the prepared tests of Lemmas 6.0D–E exhaust the cases except for the following finite alternating double-cubic procedure. That procedure prepares the \(I_n^*\) branch for every \(n>0\); its geometric resolution is a separate assertion. If none of the triple-cubic stopping tests applies, one integral rescaling reduces the discriminant valuation by twelve. Neither the preparations nor their termination uses the conductor-discriminant identity.

*Proof.* We use the complete-DVR and finite unramified constructions already proved in lesson 1 and Lemma 6.0U. All residue roots below lie in finite extensions: perfection makes their minimal polynomials separable, even when the displayed polynomial itself is inseparable. Moreover every repeated root we use belongs to the current perfect residue field itself. A quadratic has only one repeated geometric root. A cubic has only one root of multiplicity at least two. That root is fixed by every residue automorphism, so separability and the finite Galois correspondence in lesson 1 put it in the residue field. Thus repeated preparations take place in one complete DVR; they do not require an increasing infinite tower of residue extensions. A finite extension is needed only to separate the terminal simple roots.

For later reference, substituting \(x=x'+r,\ y=y'+t\) into the Weierstrass equation gives
\[
\begin{aligned}
a_1'&=a_1,&a_2'&=a_2+3r,\\
a_3'&=a_3+a_1r+2t,&
a_4'&=a_4+2a_2r+3r^2-a_1t,\\
a_6'&=a_6+a_4r+a_2r^2+r^3-a_3t-a_1rt-t^2.
\end{aligned}
\]
This identity follows by expansion, including in residue characteristics two and three. These translations have unit leading coefficients and preserve the discriminant.

After moving the singular residue point to the origin and making its repeated tangent \(y=0\), all five coefficients are divisible by \(\pi\). If the first stopping test fails, \(a_6\) is divisible by \(\pi^2\). If the second fails, \(b_8\) is divisible by \(\pi^3\). In the identity
\[
b_8=a_1^2a_6+4a_2a_6-a_1a_3a_4+a_2a_3^2-a_4^2
\]
every term other than \(-a_4^2\) is then divisible by \(\pi^3\). Thus \(a_4\) is divisible by \(\pi^2\). This argument works when two is not a unit.

Failure of the third test means \(\pi^3\mid b_6=a_3^2+4a_6\). The quadratic
\[
T^2+(a_3/\pi)T-a_6/\pi^2
\]
therefore has a repeated residue root \(\beta\). In odd residue characteristic this is the ordinary zero-discriminant criterion. In characteristic two its linear coefficient is zero, and perfection supplies the root of its constant term. Translate \(y\) by \(\pi\beta_0\), for any lift \(\beta_0\). The root equation makes \(a_6'\) divisible by \(\pi^3\); the vanishing derivative makes \(a_3'\) divisible by \(\pi^2\). The displayed translation formulas preserve \(a_1,a_2\in\pi R\) and \(a_4\in\pi^2R\). We have consequently prepared
\[
v(a_1),v(a_2),v(a_3),v(a_4),v(a_6)\ \ge\ (1,1,2,2,3).
\]

Set
\[
\bar P(T)=T^3+\overline{a_2/\pi}T^2+
              \overline{a_4/\pi^2}T+\overline{a_6/\pi^3}.
\]
If it has three distinct roots, Lemma 6.0B applies. Otherwise choose a repeated root \(\gamma\) and translate \(x\) by \(\pi\gamma_0\). Modulo \(\pi\), the new quotients \(a_4'/\pi^2,a_6'/\pi^3\) are respectively \(\bar P'(\gamma)\) and \(\bar P(\gamma)\), hence zero. The new polynomial is \(\bar P(T+\gamma)\). It is either \(T^2(T+c)\) with \(c\ne0\), or \(T^3\). Thus the exact-double case has
\[
v(a_1),v(a_2),v(a_3),v(a_4),v(a_6)\ \ge\ (1,1,2,3,4),
\qquad a_2/\pi\in R^\times,
\]
whereas the triple case has the prepared valuations \((1,2,2,3,4)\) of Lemma 6.0C. These conclusions use factorization of a monic cubic, so cover inseparable residue cubics as well.

In the triple case, examine the quadratic with coefficients \(a_3/\pi^2,-a_6/\pi^4\). If its roots are distinct, Lemma 6.0C applies. If its root is repeated, translating \(y\) by \(\pi^2\) times a root lift makes \(a_3\) divisible by \(\pi^3\) and \(a_6\) by \(\pi^5\), exactly by the preceding quadratic root-and-derivative calculation. It preserves \(a_4\in\pi^3R\). If \(a_4/\pi^3\) is a unit, the equation is the prepared one in Lemma 6.0D. Its further translation \(x\mapsto x+\pi^2r\), with
\(\bar r=-\overline{a_6/\pi^5}/\overline{a_4/\pi^3}\),
makes \(a_6\) divisible by \(\pi^6\), as used there. If \(a_4\) is divisible by \(\pi^4\) and \(a_6/\pi^5\) is a unit, Lemma 6.0E applies. In the remaining case every \(a_i\) is divisible by \(\pi^i\). Substitution \(x=\pi^2x',\ y=\pi^3y'\) gives an integral Weierstrass equation with coefficients \(a_i/\pi^i\) and discriminant \(\Delta/\pi^{12}\). The weight-twelve scaling identity for \(\Delta\) is proved in §1.1. Its valuation drops by twelve.

Here is the complete double-cubic procedure. At its \(y\)-test stage, for an integer \(r\ge2\), the coefficients satisfy
\[
a_1\in\pi R,\quad a_2/\pi\in R^\times,\quad
a_3\in\pi^rR,\quad a_4\in\pi^{r+1}R,\quad a_6\in\pi^{2r}R.
\]
Examine
\[
\bar Q_y(T)=T^2+\overline{a_3/\pi^r}T-\overline{a_6/\pi^{2r}}.
\]
If its roots are distinct, this is the arithmetic terminal test for \(n=2r-3\). If the root is repeated, translate \(y\) by \(\pi^r\) times a root lift. Its equation and derivative give
\[
a_3\in\pi^{r+1}R,\qquad a_6\in\pi^{2r+1}R.
\]
The \(a_4\) divisibility is preserved because its change is \(-a_1\pi^r\) times that lift. This reaches the \(x\)-test
\[
\bar Q_x(T)=\overline{a_2/\pi}T^2+
             \overline{a_4/\pi^{r+1}}T+
             \overline{a_6/\pi^{2r+1}}.
\]
Its leading coefficient is nonzero. If its roots are distinct, this is the terminal test for \(n=2r-2\). If its root \(\gamma\) is repeated, translate \(x\) by \(\pi^r\gamma_0\). Dividing the formulas for \(a_4'\) and \(a_6'\) by \(\pi^{r+1}\) and \(\pi^{2r+1}\), their residues are respectively \(\bar Q_x'(\gamma)\) and \(\bar Q_x(\gamma)\). The cubic extra terms vanish because \(r\ge2\). Thus
\[
a_4'\in\pi^{r+2}R,\quad a_6'\in\pi^{2r+2}R,\quad
a_3'\in\pi^{r+1}R,\quad a_2'/\pi\in R^\times.
\]
We have reached the \(y\)-test at \(r+1\). In characteristic two a repeated quadratic still has a root over the perfect residue field; none of these operations divides by two. The integers \(2r-3,2r-2\) run successively through every \(n>0\).

This alternating procedure terminates. Its repeated-root translations have \(x\)- and \(y\)-increments of valuation at least \(r\), so their sums converge in the complete DVR. The limiting translation is an invertible coordinate change. The successive valuations just proved make the limiting \(a_3,a_4,a_6\) zero. The generic equation becomes
\[
y^2+a_1xy=x^3+a_2x^2,
\]
which is singular at the origin: both partial derivatives and the equation vanish there. That contradicts the original nonsingular generic cubic. Hence a separated quadratic occurs after finitely many stages. This is a proof of termination, not a discriminant-based bound assumed during the process.

Finally, only finitely many nonminimal rescalings can occur, since each lowers the nonnegative integer \(v(\Delta)\) by twelve. Between rescalings the tests are finite, and any double-cubic procedure terminates by the preceding argument. This proves the complete arithmetic preparation and termination claims. Proposition 6.0G below supplies the regular-model graph for every prepared \(I_n^*\) terminal test. The Artin-conductor identity and general minimal-model existence/uniqueness are separate obligations. ∎

We now give the remaining double-cubic resolution. It applies over a complete DVR with perfect residue field in every residue characteristic. The coefficient preparation and termination are the proved Lemma 6.0F. The proof uses the finite unramified splitting and regularity descent of Lemma 6.0U, the all-chart smooth-tangent-conic calculation of Lemma 6.0A, and the earlier Rees, regular-local and Cartier-degree proofs identified in §7. The alternating tests agree with [Tate's free original scan](https://wstein.org/Tables/antwerp/tate/tate.pdf), printed pp. 49–51, and [Cremona's free author edition](https://johncremona.github.io/book/fulltext/chapter3.pdf), §3.2, printed pp. 66–68. Their test statements supply no conductor or minimal-model uniqueness proof.

### 6.0G.1. The precise prepared hypotheses and conclusion

Write
\[
a_1=\pi A_1,\qquad a_2=\pi A_2,\qquad A_2\in R^\times.
\tag{GS1}
\]
For an integer \(r\ge2\), assume one of the following two terminal preparations.

| Terminal test | Integral coefficient factorizations | Separated residue quadratic | Index |
|:---|:---|:---|:---|
| Odd | \(a_3=\pi^rA_3,\ a_4=\pi^{r+1}A_4,\ a_6=\pi^{2r}A_6\) | \(Q_y(T)=T^2+\bar A_3T-\bar A_6\) has two distinct geometric roots | \(n=2r-3\) |
| Even | \(a_3=\pi^{r+1}B_3,\ a_4=\pi^{r+1}B_4,\ a_6=\pi^{2r+1}B_6\) | \(Q_x(T)=\bar A_2T^2+\bar B_4T+\bar B_6\) has two distinct geometric roots | \(n=2r-2\) |

The displayed factorizations allow any higher valuations: no quotient besides \(A_2\) is required to be a unit. In characteristic two, “distinct” means separable; the argument will not divide by two. The two rows cover every positive integer \(n\).

**Proposition 6.0G.** Under either row of these hypotheses, the blowups below give a proper regular model whose geometric special fibre consists of \(n+5\) smooth rational components. There is a chain
\[
C_0-C_1-\cdots-C_n
\tag{GS2}
\]
of \(n+1\) components of multiplicity two, two components of multiplicity one attached to \(C_0\), and two components of multiplicity one attached to \(C_n\). Each displayed intersection is transverse of length one, there are no other intersections, and every component has self-intersection \(-2\). This is the \(I_n^*\) fibre graph, computed directly in every residue characteristic. The construction and regularity descend to \(R\).

Here is a diagram of the proved incidences; a label is the multiplicity in \(\operatorname{div}(\pi)\).

```text
       A(1)                                  L+(1)
        |                                      |
       C0(2) — ... — Cn(2)
        |                                      |
       B(1)                                  L−(1)
```

The chain contains every index from \(0\) through \(n\), each once. For \(n=1\) it is exactly \(C_0-C_1\), with no middle vertex. Each edge denotes exactly one intersection of length one, and the four endpoints are distinct components.

### 6.0G.2. How the strict-transform and regularity checks are made

All calculations may first be made after a finite unramified extension splitting the terminal separated quadratic, by Lemma 6.0U. Further finite residue extensions can be used to check an individual closed point, and regularity descends by the same lemma. Thus the affine computations at a residue point may use lifts of its coordinates. They also apply at generic points by localization of regular local rings (AG-CA-14, Theorem 3.2).

Blowups are computed with the actual Rees charts of AG-MO-16, §1, not just the unsaturated total-transform equations. Each hypersurface blowup below has order two at its centre. Substitution pulls its equation back to the square of the chart parameter times the displayed equation. The displayed equation really is the strict transform: in the ambient chart modulo the exceptional parameter, its reduction is a nonzero equation in a polynomial domain. Consequently the parameter and that equation are a regular pair. Explicitly, if \(t z=f w\), reduction modulo \(t\) forces \(w=t w_1\), and cancellation of the regular element \(t\) gives \(z=f w_1\). Hence multiplication by \(t\) is injective modulo \(f\), so no exceptional power torsion remains. This is exactly the saturation in AG-MO-16, Theorem 5.1. An exceptional chart whose reduced equation is a unit contains no exceptional point.

The ambient \(\pi\)-charts are polynomial rings over \(R\). The other ambient charts near the exceptional locus have relations of the form
\[
\pi=t v,\qquad \pi=t^2a,\qquad
\pi=v^2a,\qquad\text{or}\qquad \pi=w^2ab.
\tag{GS3}
\]
Before the relation, the ambient local ring is a regular polynomial local ring, by AG-CA-14, Proposition 3.3. At an exceptional closed point the relation has nonzero linear \(\pi\)-term in its cotangent space. AG-CA-14, Corollary 1.2, therefore gives a regular three-dimensional ambient ring. One surface equation reduces its dimension to two by AG-CA-11, Theorem 3.2. A nonzero affine partial of its exceptional tangent conic gives a nonzero linear term in that regular local ring, and the same corollary proves regularity of the surface. This proves the smooth-tangent-conic rule in all ambient charts used here, including mixed characteristic; it does not assume smoothness over \(R\).

The conics used below have a unit mixed term and are linearly equivalent over their residue field to \(XY-Z^2\). Their smoothness will also be checked directly. Their being projective lines in every characteristic follows from the two-chart parametrization in AG-MO-16, Solution 6.5. This avoids an unproved classification of conics.

### 6.0G.3. The first doubled line and its two initial endpoints

Both terminal rows imply the initial bounds
\[
v(a_1),v(a_2),v(a_3),v(a_4),v(a_6)
\ge(1,1,2,3,4),\qquad a_2/\pi\in R^\times.
\tag{GS4}
\]
Put \(C_3=a_3/\pi^2\), \(C_4=a_4/\pi^3\), \(C_6=a_6/\pi^4\). The special cubic is \(y^2=x^3\). Its only singular point is the origin: if \(y=0\), its equation forces \(x=0\); if \(x\ne0\), the partials \(-3x^2,2y\) cannot both vanish, including characteristics two and three. At the projective point at infinity the homogenized equation has a unit partial with respect to its third coordinate. The linear-term test in 6.0G.2 therefore proves that the original surface is regular at every special point away from the origin; the generic fibre is already nonsingular by hypothesis.

Blow up the ambient point \((\pi,x,y)\), and take the strict transform. In the \(\pi\)-chart, put \(x=\pi x_1\), \(y=\pi y_1\). Its equation is
\[
y_1^2+\pi(A_1x_1+C_3)y_1
=\pi P(x_1),\qquad
P(T)=T^3+A_2T^2+\pi C_4T+\pi C_6.
\tag{GS5}
\]
The exceptional reduced line \(E_1\) is \(\pi=y_1=0\), and
\(\bar P(T)=T^2(T+\bar A_2)\). Away from its two roots, the equation gives \(\pi=y_1^2\) times a unit. There the surface is regular and \(E_1\) has multiplicity two. At either root the equation has no linear term in the ambient parameters \(\pi,y_1,x_1-c\); these are precisely the two singular points in this chart.

The missing direction is checked in the \(x\)-chart, \(\pi=xv\), \(y=xu\):
\[
xU=u^2,\qquad
U=1+vA_2-vA_1u-v^2C_3u+x(v^3C_4+v^4C_6).
\tag{GS6}
\]
At \(x=u=v=0\), \(U\) is a unit. The surface parameters are \(u,v\), and \(\pi=u^2v/U\). Thus the strict original component \(A\), given by \(v=0\), is smooth of multiplicity one, and \(E_1\), given there by \(u=0\), has multiplicity two; they meet transversely with length one. On \(A\) this is the cusp normalization \(x=u^2,\ y=u^3\), completed by the original nonsingular point at infinity. Explicitly the parametrization \([s:t]\mapsto[s^2t:s^3:t^3]\) of the special cubic has parameter \(u=s/t\) in this chart and parameter \(t/s=1/u=X/Y\) at infinity. The resolved component is these two affine lines glued by inverse parameters, hence \(A\cong\mathbb P^1\). Every other exceptional direction in this chart with \(v\ne0\) is in the \(\pi\)-chart. There is no additional direction confined to the \(y\)-chart: the initial tangent cone is \(Y^2=0\), so a projective direction with both \(X=\Pi=0\) is impossible.

Resolve the simple root \(\bar c=-\bar A_2\ne0\) of \(\bar P\) separately. Choose a lift \(c\), put \(s=x_1-c\), and note that \(P(c)\in\pi R\) and \(P'(c)\) is a unit, whose residue is \(\bar A_2^2\). The tangent conic at this point is
\[
Y^2+\bar h\Pi Y-\bar d\Pi S-\bar b\Pi^2=0,
\quad h=A_1c+C_3,\quad d=P'(c),\quad b=P(c)/\pi.
\tag{GS7}
\]
Its \(S\)-partial forces \(\Pi=0\) at any proposed singular point; its equation forces \(Y=0\), and its \(\Pi\)-partial then forces \(S=0\). Thus it is smooth in every characteristic. Replacing \(S\) by \(dS+b\Pi-hY\) makes its equation \(Y^2-\Pi S'=0\). One blowup resolves the point, by 6.0G.2, and adds a projective line \(B\) of multiplicity one: \(\pi\) has order one on the dense exceptional chart \(\Pi\ne0\).

In its \(s\)-chart put \(\pi=s v\), \(y_1=s w\). The divided equation has form \(w^2+vH=0\), where \(H\) has constant term \(-P'(c)\) and is a unit at \(s=v=w=0\). Indeed, expanding \(P(c+s)\) gives \(P(c)+sP'(c)+s^2(3c+A_2)+s^3\), and \(P(c)=\pi b=s v b\); all terms besides \(w^2\) contain \(v\). Hence \(v=w^2\) times a unit and
\[
\pi=s w^2\times\text{unit}.
\tag{GS8}
\]
The new \(B\) and the old doubled \(E_1\) meet transversely. The endpoint \(A\) meets \(E_1\) at its direction at infinity, \(B\) at \(x_1=\bar c\), and the remaining singular point is \(x_1=0\). These are distinct because \(\bar A_2\ne0\). Resolving \(\bar c\) has not changed a neighbourhood of that remaining point. The simple-root calculation is valid even though the other cubic root is double; no three-simple-roots hypothesis is used.

### 6.0G.4. The general repeated chart and all its missing directions

For \(1\le j\le r\), let
\(X_j=x/\pi^j\), \(Y_j=y/\pi^j\). The successive distinguished \(\pi\)-charts have exact equations
\[
F_j:\quad
Y_j^2+\pi A_1X_jY_j+(a_3/\pi^j)Y_j
=\pi^jX_j^3+\pi A_2X_j^2+(a_4/\pi^j)X_j+a_6/\pi^{2j}.
\tag{GS9}
\]
All quotients used here are integral by either terminal row. For \(j<r\), the last three coefficient bounds are
\[
a_3/\pi^j\in\pi R,\qquad
a_4/\pi^j\in\pi^2R,\qquad
a_6/\pi^{2j}\in\pi^2R.
\tag{GS10}
\]
For \(2\le j<r\), the \(\pi\)-linear term on the exceptional reduced line is \(-\bar A_2X_j^2\). Thus its only singular point in this chart is \(X_j=Y_j=\pi=0\). Away from zero it is regular, with \(\pi=Y_j^2\) times a unit; this line is the doubled \(E_j\). At zero the equation has order exactly two, since it contains \(Y_j^2\). For \(j=1\), the cubic term supplies the additional simple root already resolved in 6.0G.3. This proves that the repeated distinguished centre is the origin at every stage \(j<r\). In particular the terminal valuations themselves imply that all preceding residue tests have their repeated root at zero; we do not need an undocumented history of earlier translations.

Blowing up the origin of \(F_{j-1}\), for \(2\le j\le r\), gives \(F_j\) in its \(\pi\)-chart by the substitutions \(X_{j-1}=\pi X_j\), \(Y_{j-1}=\pi Y_j\). To check its missing part, use the \(X_{j-1}\)-chart
\[
X_{j-1}=t,\qquad \pi=t v,\qquad Y_{j-1}=t w,
\quad
D_{3j}=a_3/\pi^j,\quad D_{4j}=a_4/\pi^{j+1},\quad D_{6j}=a_6/\pi^{2j}.
\tag{GS11}
\]
Direct substitution in \(F_{j-1}\) and division by \(t^2\) gives
\[
w^2+t vA_1w+vD_{3j}w
-t^jv^{j-1}-t vA_2-t v^2D_{4j}-v^2D_{6j}=0,
\qquad \pi=t v.
\tag{GS12}
\]
This identity is valid for every integer \(j\ge2\); in particular its cubic term has exponent \(t^jv^{j-1}\), not the exponent from a three-step sample.

On the new exceptional divisor \(t=0\) its equation is
\[
q_j(w,v)=w^2+\bar D_{3j}v w-\bar D_{6j}v^2=0.
\tag{GS13}
\]
The points with \(v\ne0\) overlap \(F_j\), so any of their singularities are exactly those described there. If \(v=0\), the equation forces \(w=0\), giving the sole missing exceptional point \(t=v=w=0\). The tangent cone of \(F_{j-1}\) has the equation \(q_j(Y,\Pi)=0\), independent of its \(X\)-coordinate. A direction confined to its \(Y\)-chart would have \(X=\Pi=0\), forcing \(Y=0\); hence no direction is omitted by these two charts.

For clarity, points of (GS12) on the strict old component with \(v=w=0\) and \(t\ne0\) are outside this blowup centre. Their \(v\)-linear coefficient is \(-t\bar A_2\) if \(j>2\), and \(-t(t+\bar A_2)\) if \(j=2\). The latter has the simple-root singularity at \(t=-\bar A_2\): it is exactly the point resolved separately in 6.0G.3, rather than an additional missing centre. All its neighbourhoods are replaced by that already regular blowup. This records the entire overlap with the first exceptional line.

### 6.0G.5. Each missing point contributes one doubled connecting conic

At the origin of (GS12), the ambient ring has regular parameters \(t,v,w\) and relation \(\pi=t v\). Its tangent conic is
\[
q_j(W,V)-\bar A_2T V=0.
\tag{GS14}
\]
The \(T\)-partial forces \(V=0\), its equation forces \(W=0\), and the \(V\)-partial then forces \(T=0\). It is smooth even when \(q_j\) is a square and even in characteristic two. It is linearly equivalent to \(W^2-VT'=0\) by
\(T'=\bar A_2T-\bar D_{3j}W+\bar D_{6j}V\).
Blow up this point once. By 6.0G.2 it becomes regular in all charts and the exceptional conic \(H_j\) is \(\mathbb P^1\). The order of \(\pi=t v\) on its generic point is two: both \(T\) and \(V\) are nonzero on a dense open of the smooth conic. Thus \(H_j\) has multiplicity two.

The two necessary affine charts give the incidences as well as regularity. In the \(t\)-chart, put \(v=t a\), \(w=t b\); its exact equation is
\[
b^2+D_{3j}a b-D_{6j}a^2
+t aA_1b-t^{2j-3}a^{j-1}-A_2a-t a^2D_{4j}=0,
\qquad \pi=t^2a.
\tag{GS15}
\]
At \(t=a=b=0\) all terms other than \(b^2\) contain \(a\), and its coefficient there is \(-A_2\), a unit. Hence \(a=b^2\) times a unit, the surface parameters are \(t,b\), and
\[
\pi=t^2b^2\times\text{unit}.
\tag{GS16}
\]
The old \(E_{j-1}\) is \(b=0\), the new \(H_j\) is \(t=0\), and they meet transversely with length one. Their tangent direction on the conic is \([T:V:W]=[1:0:0]\).

In the \(v\)-chart put \(t=v a\), \(w=v b\); the exact equation is
\[
b^2+D_{3j}b-D_{6j}
+v aA_1b-v^{2j-3}a^j-A_2a-v aD_{4j}=0,
\qquad \pi=v^2a.
\tag{GS17}
\]
On its exceptional conic \(v=0\), it is
\(q_j(b,1)-\bar A_2a=0\). If \(q_j(b,1)\) has two distinct roots \(\beta,\gamma\), the strict transforms of the two new lines meet \(H_j\) at \((a,b)=(0,\beta),(0,\gamma)\). At each, the \(b\)-partial is a unit. Regular parameters are \(v,a\), and \(\pi=v^2a\). Thus the connecting conic has multiplicity two, each new line multiplicity one, and each intersection has length one. The two attachment directions \([0:1:\beta]\), \([0:1:\gamma]\) are distinct from one another and from the old direction \([1:0:0]\).

In the repeated-root stages here, that root is zero and \(D_{3j},D_{6j}\in\pi R\). Write \(D_{3j}=\pi U_3\), \(D_{6j}=\pi U_6\). Since \(\pi=v^2a\), (GS17) becomes the exact factored equation
\[
b^2+a\bigl(v^2U_3b-v^2U_6+vA_1b
-v^{2j-3}a^{j-1}-A_2-vD_{4j}\bigr)=0.
\tag{GS18}
\]
The parenthesized coefficient is a unit at \(v=a=b=0\). Consequently \(a=b^2\) times a unit and the parameters there are \(v,b\). Now
\[
\pi=v^2b^2\times\text{unit},
\tag{GS19}
\]
so the new doubled \(E_j\), given by \(b=0\), meets \(H_j\), given by \(v=0\), transversely. Its conic direction is \([0:1:0]\), distinct from the old attachment. There are no further conic directions confined to the \(w\)-chart, because (GS14) has no point with \(T=V=0\). The smooth-conic check also covers all its other points.

For \(j<r\), both terminal rows give \(D_{3j},D_{6j}\in\pi R\), so this repeated case always applies. In the even terminal row it also applies at \(j=r\). In the odd terminal row \(q_r(b,1)=Q_y(b)\) is separated, so the other case applies there. These assertions are direct coefficient bounds, rather than a claim that a repeated test automatically improves coefficients.

After a repeated stage, the connecting conic attaches to \(E_j\) at its point at infinity, outside the finite \(F_j\)-chart. The next distinguished origin is \(X_j=0\), in that finite chart. Thus no subsequent blowup changes that already regular intersection. The all-chart arguments of 6.0G.4–6.0G.5 show inductively that no singularity outside the next distinguished chart has been left behind.

### 6.0G.6. Stopping at the odd test

In the odd terminal case, reduction of \(F_r\) gives
\[
Y_r^2+\bar A_3Y_r-\bar A_6=0.
\tag{GS20}
\]
It is the union of two distinct affine lines with coordinate \(X_r\). At every finite point its \(Y_r\)-partial is a unit, so the surface is regular there. The parameters include \(\pi\), and both lines have multiplicity one. Their closures, denoted \(L_+,L_-\), are projective lines: the missing points are precisely the two distinct points on \(H_r\) proved regular in (GS17). They meet that conic transversely and meet no other component. In particular they do not meet each other after the connecting-conic blowup.

The doubled chain is
\[
E_1,H_2,E_2,H_3,\ldots,E_{r-1},H_r.
\tag{GS21}
\]
The precise indexing, which also removes any small-\(r\) ambiguity in the displayed pattern, is \(C_{2j-2}=E_j\) for \(1\le j\le r-1\) and \(C_{2j-3}=H_j\) for \(2\le j\le r\). For \(r=2\) the chain is just \(E_1,H_2\). It contains \(2r-2=n+1\) components. Its first end has the distinct leaves \(A,B\) from 6.0G.3, and its last end the two leaves \(L_+,L_-\). These give \(2r+2=n+5\) total components. The finite charts, both missing-direction charts and all conic charts are regular by the preceding calculations. Together with the original smooth locus, they cover the entire model.

### 6.0G.7. Stopping at the even test

In the even terminal case, the bridge calculation is the repeated case and leaves the doubled line \(E_r\). Its finite chart is
\[
Y_r^2+\pi(A_1X_r+B_3)Y_r
=\pi H(X_r),\qquad
H(T)=A_2T^2+B_4T+B_6+\pi^{r-1}T^3.
\tag{GS22}
\]
Away from the two distinct roots of \(\bar H=Q_x\), this is regular with \(\pi=Y_r^2\) times a unit. At each root it has no linear term, so these are exactly its two singular points. They lie in the finite chart, are distinct from each other, and are disjoint from the bridge intersection at infinity.

Choose a lift \(\alpha\) of one root and put \(s=X_r-\alpha\). Then \(H(\alpha)\in\pi R\) and \(d=H'(\alpha)\in R^\times\), because \(Q_x\) is separable. With \(h=A_1\alpha+B_3\) and \(b=H(\alpha)/\pi\), the tangent conic is
\[
Y^2+\bar h\Pi Y-\bar d\Pi S-\bar b\Pi^2=0.
\tag{GS23}
\]
The same partial-derivative and linear-change calculation as for (GS7) proves it is a smooth projective line in every characteristic. One blowup at each of these two disjoint points resolves them completely. The exceptional lines \(L_+,L_-\) have multiplicity one because \(\pi\) has order one in the dense conic chart \(\Pi\ne0\). In the \(s\)-chart put \(\pi=s v\), \(Y_r=s w\); expansion of \(H(\alpha+s)\) gives \(w^2+vU=0\), where \(U\) has constant term \(-H'(\alpha)\), a unit. Thus the surface parameters are \(s,w\) and
\[
\pi=s w^2\times\text{unit}.
\tag{GS24}
\]
Each \(L_\pm\) meets the old doubled \(E_r\) transversely with length one. The two centres were distinct, so their exceptional lines are disjoint, and neither meets \(H_r\). Their other charts are regular by 6.0G.2, and all original points away from these centres were already regular.

The doubled chain is now
\[
E_1,H_2,E_2,H_3,\ldots,H_r,E_r,
\tag{GS25}
\]
Here \(C_{2j-2}=E_j\) for \(1\le j\le r\) and \(C_{2j-3}=H_j\) for \(2\le j\le r\); for \(r=2\) the chain is exactly \(E_1,H_2,E_2\). Its length is \(2r-1=n+1\). Adding \(A,B,L_+,L_-\) gives \(2r+3=n+5\) components. This proves the same graph (GS2) for every positive even \(n\), including \(r=2\), \(n=2\).

### 6.0G.8. Multiplicities, self-intersections, properness and descent

The local expressions (GS6), (GS8), (GS16), (GS17), (GS19) and (GS24) prove the multiplicities and the length-one transverse intersections at every edge. The attachment directions proved distinct in 6.0G.3 and 6.0G.5, and the disjoint finite terminal centres in 6.0G.7, prove that no extra edge or triple point occurs. The repeated blowups take place at the finite origin of \(E_j\), whereas its previously resolved connecting-conic intersection is at infinity; thus they never create an intersection with a nonadjacent component. The reduced exceptional lines, connecting conics, simple-root conics and original cusp normalization are all smooth projective lines. Their subsequent strict transforms remain such lines: the centre ideal restricts to the principal point ideal on each smooth old curve, whose blowup is the identity by AG-MO-16, Theorem 4.1(1); its strict transform is that blowup by Theorem 5.1. The explicit regular branch charts above supply their incidences on the new surface.

For clarity, self-intersection means the degree on the component of its Cartier-divisor line bundle on the regular surface. AG-CA-14, Theorem 5.3, and AG-MO-17, §2, give the required Cartier equations. Restricting the section of another component's divisor bundle gives its zero divisor on the chosen component: a transverse length-one intersection contributes one, because its local equation is a regular parameter there. Degrees are additive under tensor product by AG-MO-15, §§1–2, and the projective-line degree calculation is AG-MO-17, Proposition 4.1. The total fibre
\[
D=A+B+L_++L_-+2\sum_{i=0}^{n}C_i
=\operatorname{div}(\pi)
\tag{GS26}
\]
has trivial divisor line bundle, so has degree zero on each component. A leaf therefore gives \(C^2+2=0\). An end of the doubled chain gives \(2C^2+2+1+1=0\), and an interior doubled component gives \(2C^2+2+2=0\). Hence every component has self-intersection \(-2\). For \(n=1\) both chain components are ends and the same end formula applies. These regular models have no geometric rational vertical component of self-intersection \(-1\); this checks that condition directly and asserts no general contraction or uniqueness theorem.

The original projective Weierstrass model is proper by *Proper morphisms and the valuative criterion of properness* (AG-MO-07), Theorems 2.1 and 4.1, or the inspected projective-implies-proper proof in AG-MO-10, Theorem 1.1. It is integral as well. To check the latter without a model-existence theorem, let \(f\) be its homogeneous cubic. Its reduction is the nonzero polynomial \(y^2z-x^3\). If \(\pi g=f h\), reduction modulo \(\pi\) in the polynomial domain forces \(h=\pi h_1\), and cancellation gives \(g=f h_1\). Thus \(\pi\) is injective on \(R[x,y,z]/(f)\), which embeds in its generic localization; that generic ring is a domain because the generic Weierstrass curve is integral. Its homogeneous affine Proj charts are consequently domains as well. Each later strict transform is the blowup of this integral surface at its indicated centre by AG-MO-16, Theorem 5.1, and remains integral by Theorem 4.1(2). This also proves that no surface component supported solely in the special fibre has been introduced.

Each step has a finite vertical centre with finite-type ideal, so AG-MO-16, Theorem 4.1(3), proves projectivity and properness. Its map is an isomorphism over the nonsingular generic fibre. The nonzero element \(\pi\) is a nonzerodivisor in every integral chart. Torsion-free modules over the DVR are flat: every finitely generated submodule is free by lesson 1, Lemma 0A.1, and these submodules form a directed union. Tensor products commute with that union by their bilinear universal property. An element in the kernel of a tensored injection is represented at one finite free stage; its image becomes zero at some later stage, where freeness makes the tensored map injective. It was consequently already zero in the union. Thus this is a proper flat regular model of the original generic curve.

All equations and connecting centres are defined over \(R\). The initial simple root \(-\bar A_2\) is already rational over \(k\). In the even terminal case the two final centres form the separable root locus of \(Q_x\), so their union is defined over \(k\); blowing up that union gives both disjoint root blowups after splitting. In the odd case the two separated lines require no additional individual centre, and the connecting conic is defined over \(k\). A finite Galois residue splitting extension and its unramified lift exist by Lemma 6.0U. The invariant centres, their Rees blowups and strict transforms commute with that flat base change, by AG-MO-16, Theorem 4.1(4) and its strict-transform saturation. Regularity descends by the cotangent/dimension proof in Lemma 6.0U. Hence the proper regular model exists over the original complete DVR, with the geometric fibre description stated in Proposition 6.0G. ∎

**Corollary 6.0G.2 (the complete prepared double-cubic branch).** Start with the double-cubic equation (GS4). The alternating tests of Lemma 6.0F, terminate with an \(I_n^*\) regular-resolution graph for some \(n>0\), in every residue characteristic.

*Proof.* Lemma 6.0F's double-cubic paragraphs prove both valuation recurrences by the exact translation identities: a repeated \(y\)-test at \(r\) improves \(a_3,a_6\) to exponents \(r+1,2r+1\); a repeated \(x\)-test improves \(a_4,a_6\) to exponents \(r+2,2r+2\), preserving the other requirements and \(a_2/\pi\) as a unit. Its final limiting-translation argument proves termination inside one complete DVR, by contradiction with nonsingularity of the generic cubic. Hence a separated test really occurs, with exactly one row of 6.0G.1. Those translations are invertible changes of the generic curve. Apply Proposition 6.0G to that actual terminal equation. Its graph gives \(n=2r-3\) at a separated \(y\)-test and \(n=2r-2\) at a separated \(x\)-test, proving the claim. ∎

**Example 6.1: the level-11 curve.** For \(y^2+y=x^3-x^2\), the coefficients give
\[
(b_2,b_4,b_6,b_8)=(-4,0,1,-1),
\quad c_4=16,
\quad \Delta=-11.
\tag{20}
\]
At 11, the unique singular point is \((8,5)\): the derivatives require \(2y+1=0\) and \(x(2-3x)=0\), and only this candidate lies on the curve. Put \(x=X+8,y=Y+5\). Modulo 11 the equation becomes
\[
Y^2=X^2(X+1).
\tag{21}
\]
Its two tangent directions are \(Y=\pm X\), both rational. Thus the reduction is split multiplicative. The resolution proved in Lemma 4.0 gives type \(I_1\), since \(v_{11}(\Delta)=1\). Its exponent is one and its covariant pair is \(\mathrm{Sp}(2)\).

For a full point-count check, the normalization parameter \(t=Y/X\) gives \(X=t^2-1,Y=t(t^2-1)\). The nonsingular points correspond to \(t\in\mathbf P^1(\mathbf F_{11})\) excluding \(t=\pm1\), so there are ten; adding the node gives eleven points on the singular cubic. The multiplicative coefficient is therefore \(a_{11}=12-11=1\). Equation (17) gives \((1-11^{-s})^{-1}\). The discriminant has no other prime factor, so the global conductor is 11. The degree-two good-reduction polynomial does not apply at this prime.

**Example 6.2: wild reduction at 3.** For \(y^2+y=x^3-7\),
\[
b_2=b_4=b_8=0,
\quad b_6=-27,
\quad c_4=0,
\quad\Delta=-3^9,
\quad j=0.
\tag{22}
\]
The reduced curve has a cusp at \((0,1)\); translating that point gives \(Y^2=x^3\) modulo 3. The integral model is minimal at 3. Its integral \(j\)-invariant makes it potentially good, so \(N=0\), but reduction is additive and the local factor is 1.

Here is the conductor computation. Complete the square over \(\mathbf Z_3\): with \(Y=y+1/2\), the equation is \(Y^2=x^3-27/4\). In Tate’s algorithm the tests for types II, III and IV pass to the next branch: \(v_3(a_6)=3\), \(b_8=0\), and \(v_3(b_6)=3\). The auxiliary cubic after division by the relevant powers of 3 is
\[
T^3-1/4\equiv(T-1)^3\pmod3.
\tag{23}
\]
Translate its triple root by putting \(x=X+3\). Then
\[
Y^2=X^3+9X^2+27X+81/4.
\tag{24}
\]
The next auxiliary quadratic is \(T^2-1/4\) modulo 3, with distinct roots. The resolution and ramification proofs below identify this as type \(IV^*\), with seven geometric components, and establish
\[
f_3(E)=9+1-7=3,
\qquad \delta=3-2=1.
\tag{25}
\]
Here are independent geometric and Galois verifications of the two quantities in (25). Write \(\pi=3\) and use (24). Blow up its singular point \((\pi,X,Y)\). In the \(\pi\)-chart, \(X=\pi x_1,Y=\pi y_1\), its equation is
\[
y_1^2=\pi x_1^3+\pi^2(x_1+1/2)^2.
\tag{25a}
\]
The exceptional line has multiplicity two; the only singular point of this chart is \(x_1=y_1=\pi=0\). The \(X\)-chart is regular because its equation has a unit linear coefficient in \(X\); it contains the intersection of the original component with that line. Blow up the remaining point. Its \(\pi\)-chart is
\[
y_2^2=1/4+\pi x_2+\pi^2x_2^2+\pi^2x_2^3.
\]
Its exceptional divisor is the two distinct lines \(y_2=\pm1/2\), and this chart is regular since \(2y_2\) is a unit. In the \(x_1\)-chart put \(\pi=x_1v\), \(y_1=x_1y_2\), and \(w=y_2-v(x_1+1/2)\). The remaining equation and base parameter are
\[
w^2+(1+2x_1)vw-vx_1^2=0,\qquad \pi=x_1v.
\tag{25b}
\]
Its only singular point is the origin. Blow it up. Its tangent cone \(w(w+v)=0\) gives two more exceptional lines, each of multiplicity two. The only remaining singularity is in the \(x_1\)-chart, where \(v=x_1v_1,w=x_1w_1\):
\[
w_1^2+(1+2x_1)v_1w_1-v_1x_1=0,
\qquad \pi=x_1^2v_1.
\tag{25c}
\]
The tangent cone \(w_1^2+v_1w_1-v_1x_1\) is a smooth projective conic over \(\bar k\): its three partial derivatives cannot vanish at a projective point. Blowing up this ordinary double point resolves it and introduces one projective line of multiplicity three. To justify this last resolution rule, in a blowup chart divide the hypersurface equation by the square of the chart parameter. Along the exceptional divisor it is the conic equation; one of its two affine partial derivatives is a unit at each of its points. The local hypersurface is therefore regular, by elimination of that variable. The other charts are the corresponding two affine conic charts. The same derivative checks in (25b) show that its charts away from the stated remaining point are regular; thus no singularity was omitted.

The complete fibre has seven components. Its central multiplicity-three component meets three multiplicity-two components, and each of those meets a distinct multiplicity-one endpoint. This follows directly from the three tangent directions in (25c): the original doubled line has direction \([1:0:0]\), and the other two have \([0:1:0]\), \([0:1:-1]\). The endpoint of the first is the original cubic component, and the other endpoints are the two lines from the second blowup. Intersecting the principal total fibre with each component gives self-intersection \(-2\): the adjacent multiplicities total twice its own multiplicity. Hence this is the relatively minimal regular fibre, called \(IV^*\), and \(M=7\). This supplies the geometric proof of the triple-root and distinct-quadratic-root branches actually executed here.

For its conductor, its 2-torsion after completing the square has \(Y=0\) and \(x^3=27/4\). If \(\alpha^3=4\), the field of one root is \(K(\alpha)\), of degree three: \(\alpha-1\) satisfies the Eisenstein polynomial
\(T^3+3T^2+3T-3\). Its derivative gives different exponent three. Its splitting field is \(M_2=K(\alpha,\zeta_3)\), a totally ramified extension of degree six with group \(S_3\); adjoining \(\zeta_3\) is the disjoint tame quadratic extension. Its different exponent is therefore \(2\cdot3+1=7\), by (19b). The special good curve has \(j=0\) in characteristic 3. Lemma 2.3 restricts its faithful inertia to \(C_3\rtimes C_4\), whose subgroups of order six are cyclic. Since inertia already surjects onto the nonabelian group \(S_3\) on 2-torsion, its full image must be the group of order twelve.

Let \(L/K\) be the finite extension killing that image; it can be detected on a sufficiently high 2-power torsion level because the image is finite and the Tate module is its faithful inverse limit. Then \(L/M_2\) is tame quadratic, and \(d(L/K)=2\cdot7+1=15\). Its lower groups have \(G_0\) of order twelve and \(G_1\) the wild \(C_3\). Formula (19c) forces
\(G_1=G_2=C_3\), \(G_3=1\): after the contributions \(11+2\), exactly two remain. Each nontrivial finite subgroup has zero fixed vectors on this two-dimensional determinant-one representation, since a finite-order matrix with both eigenvalues one is identity. Thus
\[
\delta=\frac3{12}\,2+\frac3{12}\,2=1,
\qquad f_3=2+\delta=3.
\tag{25d}
\]
This proves the conductor directly and verifies the equality \(3=9+1-7\) in this example. The discriminant has only the prime 3, so the global conductor is 27.

**Example 6.3: wild reduction at 2.** For \(y^2=x^3-x\),
\[
b_2=b_6=0,
\quad b_4=-2,
\quad b_8=-1,
\quad c_4=48,
\quad\Delta=64,
\quad j=1728.
\tag{26}
\]
The singular point modulo 2 is \((1,0)\). Translate \(x=X+1\) to obtain
\[
y^2=X^3+3X^2+2X.
\tag{27}
\]
Modulo 2 its tangent cone is \((y+X)^2\), so it is additive rather than nodal. Now \(a_6=0\) passes the type-II test, while the translated \(b_8=-4\) has valuation two and is not divisible by \(2^3\). The resolution below proves that this is the type-III branch, with two geometric components, and the ramification proof gives
\[
f_2(E)=6+1-2=5,
\qquad \delta=5-2=3.
\tag{28}
\]
To verify the type-III resolution, blow up the point \((2,X,y)\) in (27). Its tangent cone in the regular three-dimensional ambient local ring is
\[
Y^2+X^2+TX=0\quad\text{in }\mathbf P^2_{\bar k},
\]
where \(T\) denotes the initial form of 2. This conic is smooth: its derivatives are \(T,0,X\), whose simultaneous vanishing cannot lie on the conic. The blowup is therefore regular by the conic-chart argument above, and its exceptional curve is one projective line. In its \(X\)-chart, put \(2=Xt,y=Xw\); the equation is \(w^2=X+3+t\). At the intersection point set \(W=w-1\). Eliminating \(t\) gives
\[
2(1+X-XW)=X(W^2-X).
\tag{28a}
\]
The factor on the left is a unit. The two multiplicity-one components of the special fibre are \(X=0\) and \(X=W^2\); their intersection has length two. Intersecting the total principal fibre with either gives self-intersection \(-2\). This is a minimal regular fibre with two tangent components, the definition of type \(III\), so \(M=2\). Thus the type-III branch used here has been proved geometrically.

For an independent conductor computation, work over an unramified \(K/\mathbf Q_2\) containing \(\zeta_3\), and let \(b=1+2\zeta_3\), so \(b^2=-3\). The nonzero 3-torsion \(x\)-coordinates satisfy
\[
3x^4-6x^2-1=0,\qquad
x^2=1+2a/3,\quad a^2=3.
\tag{28b}
\]
The quartic follows directly from the doubling formula: for a point of order three, \(x(2P)=x(P)\), giving \((3x^2-1)^2=12x(x^3-x)\), which is the displayed polynomial. These roots are nonzero and are not 2-torsion, so the converse holds as well. The field \(K(a)/K\) is ramified quadratic, with different exponent two by Lemma 6.0, using the approximation 1 to \(a\). In this field, whose normalized \(v(2)\) is two,
\[
(1+2a/3)-a^2=2(a-3)/3
\]
has valuation three, since \(a-3\) has valuation one. Lemma 6.0 therefore gives another ramified quadratic \(K_x=K(a,x)\), with different exponent two over \(K(a)\), and \(d(K_x/K)=6\). All four quartic roots belong to \(K_x\): they are \(\pm x\), \(\pm b/(3x)\). Their automorphisms are the two commuting involutions \(x\mapsto-x\) and \(x\mapsto b/(3x)\), so \(K_x/K\) is the biquadratic extension.

Adjoin the corresponding \(y\), with \(y^2=x(x^2-1)\), and put \(r=y/(x-1)\). In \(K_x\) the normalized valuations are
\[
v(2)=4,\quad v(x-1)=2,\quad v(x-a)=3.
\]
The second and third follow by factoring \(x^2-1=2a/3\) and \(x^2-a^2=2(a-3)/3\); in each case the two factors have equal valuation because their difference has larger valuation. Consequently
\[
r^2-a^2=\frac{x^2-2x+3}{x-1}
=\frac{2(2+a/3-x)}{x-1}
\]
has valuation \(4+3-2=5\). Indeed \(2+a/3-x=2(1-a/3)-(x-a)\), whose terms have valuations six and three. Lemma 6.0 gives a ramified quadratic \(K(x,y)/K_x\), of different exponent four, and hence
\(d(K(x,y)/K)=2\cdot6+4=16\).

This is the full inertia field. To justify that assertion, the automorphism \((x,y)\mapsto(-x,iy)\) of the original curve is defined over \(K(i)=K(a)\) and has order four. It extends to the good model, by §1.2. In the special automorphism group \(Q_8\rtimes C_3\), the centralizer of any element of order four is its \(C_4\): inside \(Q_8\) this is the quaternion relation, and outside it the order-three quotient permutes the three such cyclic subgroups. Inertia over \(K(i)\) commutes with that automorphism, and hence has order at most four. Thus full inertia has order at most eight. The degree-eight totally ramified point field just constructed forces order at least eight. Lemma 2.3 now identifies the image with \(Q_8\); its action on that point has an orbit of size eight, so its stabilizer is trivial and the point field kills the whole image. This argument may be made over the maximal unramified henselian field, or after a sufficiently large finite unramified base extension; all the valuations and different exponents above persist.

The center of \(Q_8\) fixes \(x\) and negates \(y\); its quadratic extension over \(K_x\) has different exponent four, so its nontrivial element has \(v(\sigma(\pi_L)-\pi_L)=4\), or last lower index three. Since the whole group is wild, \(G_0=G_1=Q_8\). Formula (19c) and the different exponent sixteen then force
\[
G_2=G_3=\{\pm1\},\qquad G_4=1:
\]
the first two groups contribute fourteen, and the center contributes the two remaining units. The central involution acts as \(-1\) on the Tate module, so every nontrivial group here has zero fixed vectors. Therefore
\[
\delta=2+\frac2{8}\,2+\frac2{8}\,2=3,
\qquad f_2=2+\delta=5.
\tag{28c}
\]
This proves the conductor directly and verifies \(5=6+1-2\) in this example. Here \(N=0\) by potential good reduction and the local factor is 1. The curve has good reduction at every odd prime, so its global conductor is \(2^5=32\). The valuation six of its discriminant is not its conductor exponent.

## 7. Proof dependencies and the remaining geometric obligation

Sections 1.1 and 1.3 prove the coordinate, discriminant, minimality, singular-cubic and potential-good claims. The direct pole-lattice construction of a good integral equation uses the actual earlier proofs in *Discrete valuation rings, normal rings and Serre's criterion*, Theorem 3.3 and Corollary 4.5. Section 1.2 uses the actual earlier programme proof of Néron–Ogg–Shafarevich, *Néron models*, Lemmas 7.1–7.3 and Theorem 7.4, and its mapping property to extend good-model isomorphisms. Its Lemma 8.2 identifies our smooth projective cubic models with good group models. Proposition 2.2 and Lemma 2.3 prove the finite-inertia assertions in every residue characteristic. The Tate-module lesson supplies the proved pairing, torsion, specialization and faithful endomorphism results; the monodromy lesson supplies the proved tame/wild structure, monodromy and Weil–Deligne conductor definition (22). The earlier conductor lesson, Lemmas 1.1–1.6 and Theorem 2.1, proves the lower ramification groups, different formulas, quotient independence and lower-group Swan sum (4) used in §6.

Lemma 3.0 proves the whole uniformization used here: the equation and addition identities, kernel, surjectivity over every finite extension, Galois equivariance, and the unique parameter from a nonintegral \(j\). Theorem 3.1 proves its Kummer extension and inertia formula. Lemma 4.0 proves the quadratic twist and splitting alternatives. Its identity-component base-change step uses the inspected earlier proof in *Néron models*, Theorem 8.20, following the explicit semistable node construction in Lemma 8.6 and Proposition 8.7. Section 6 proves the specific \(III\) and \(IV^*\) resolutions and computes both wild conductors directly from torsion fields. These establish all three examples and the four exercise solutions without using (18).

Lemmas 6.0A–6.0E give direct all-characteristic regular resolutions for \(II,III,IV\), the separated-cubic \(I_0^*\) branch the separated-quadratic \(IV^*\) branch, and the prepared \(III^*,II^*\) branches. Every component multiplicity and intersection is computed in their charts. Lemma 6.0F proves all coefficient preparations and arithmetic termination, including the full alternating double-cubic procedure for every \(n>0\). Proposition 6.0G computes the regular-model graph for that procedure for every \(n>0\), including every missing chart, multiplicity and length-one intersection; Corollary 6.0G.2 binds it to the proved preparations. The branch tests are material from Cremona's freely available author edition, Chapter III, §3.2; they supply no proof of the conductor formula. Projectivity, exceptional Cartier divisors, strict-transform saturation and flat base change use the actually written earlier lesson *Blowing up*, §§1–5, especially Theorems 4.1 and 5.1. Its Exercise 6.5 and complete solution identify the split smooth tangent conic with \(\mathbf P^1\), by the two charts and the parametrization \([a:b]\mapsto[a^2:b^2:ab]\). Lemma 6.0U supplies finite unramified splitting and regularity descent over every perfect residue field. The local parameter criterion is the written argument in *Regular local rings*, Theorem 1.1 and Proposition 1.3. Intersection here means the degree of a component's Cartier line bundle restricted to another proper component; the principal fibre has degree zero on each. The Cartier-to-line-bundle and projective-line degree arguments are the actual proofs in *Effective Cartier divisors and invertible sheaves*, §2, and *Weil divisors and the class group*, §2 and Proposition 4.1. The transitive free-source and current public-edition verification of these programme prerequisites remains part of the course audit.

The freely available author preprint of Berger, §II.4.1–II.4.2, is useful for comparing the series and torsion basis. Two typographical errors in its **arXiv version 1**, submitted October 12, 2002, require correction. The series need \(a_4(q)=-5s_3(q)\), whereas that text prints \(-s_3(q)\). For instance, at \(v=2\) its series give \(x=2+q/2+O(q^2)\) and \(y=-4+q/2+O(q^2)\), so \(y^2+xy-x^3=-11q+O(q^2)\); the printed \(a_4x+a_6\) instead begins \(-3q\). The full torsion range is \(0\le i,j<p^n\), whereas that text prints \(0\le i,j<p^n-1\). Valuation followed by primitivity of the root of unity proves distinctness, as in Theorem 3.1; the correct range has \(p^{2n}\) classes. These diagnostics refer to the freely accessible manuscripts checked here.

**Remaining proof obligation.** Formula (18) is asserted in its full generality, but its general proof has not been supplied here or located in an inspected earlier programme lesson. Lemma 6.0F now proves the complete arithmetic preparation and termination of the additive algorithm. Proposition 6.0G now proves the prepared \(I_n^*\) resolution for every \(n>0\), so all additive branches have their direct regular-model graph calculation. General minimal-model foundations and the conductor interpretation are still required. Cremona's freely available author edition, Chapter III, §3.2, gives the precise algorithm, including lines 23–24 and 65–72, but its algorithm statement does not prove the required regular-model or Artin-conductor interpretation. Consequently this draft cannot yet be certified as a fully proved account of the general conductor-discriminant theorem and algorithm. A complete proof must establish those general geometric assertions; deleting their statements, replacing the Artin conductor by a new definition, or citing the algorithm would not close the obligation.

## 8. Graded exercises with complete solutions

**Exercise 8.1 (easy).** Determine the reduction at 11 of \(y^2+y=x^3-x^2\). Verify the sign of its linear factor by a point count.

*Solution.* Formula (19) gives \(\Delta=-11\) and \(c_4=16\), so the model is minimal and has multiplicative reduction. The singular point is \((8,5)\); translation gives \(Y^2=X^2(X+1)\). Both tangent slopes are rational, hence the reduction is split. Its nonsingular points are parametrized by \(\mathbf P^1(\mathbf F_{11})\setminus\{1,-1\}\), a set of size ten, and the singular cubic has eleven points. Therefore \(a_{11}=12-11=1\), the conductor exponent is one, and the arithmetic factor is \((1-11^{-s})^{-1}\).

**Exercise 8.2 (medium).** Construct the Tate-module extension class for \(E_Q\), prove that the inertia image is infinite, and determine when its reduction modulo \(\ell\) is unramified.

*Solution.* A torsion class in \(\bar F^\times/Q^{\mathbf Z}\) has \(z^{\ell^n}=Q^b\); its quotient coordinate is \(b\bmod\ell^n\), with kernel \(\mu_{\ell^n}\). Compatible choices of roots \(Q_n\) and \(\zeta_n\) give (9) and the matrix (12). The off-diagonal entry is defined by \(g(Q_n)/Q_n=\zeta_n^{\kappa_n(g)}\), which is the Kummer class of \(Q\). Unit roots are unramified by Hensel’s lemma, so on inertia the entry is \(v(Q)t_\ell\). Its image is the infinite subgroup \(v(Q)\mathbf Z_\ell\) of \(\mathbf Q_\ell\), proving the rational nonsplit assertion. Modulo \(\ell\), inertia is trivial exactly when \(\ell\mid v(Q)\); otherwise the tame character surjects onto the nonzero off-diagonal additive subgroup of \(\mathbf F_\ell\).

**Exercise 8.3 (medium).** Prove that an additive potentially good curve at \(p\ge5\) has conductor exponent two. Why does this argument not give two at 2 or 3?

*Solution.* Potential good reduction gives \(N=0\) and finite inertia. A line fixed pointwise by inertia would have a stable complement by averaging. Determinant one and the trivial character on the fixed line would make the complement trivial too; Néron–Ogg–Shafarevich would then imply good reduction, a contradiction. A two-dimensional fixed space would also imply good reduction. Thus the fixed-space dimension is zero. The inertia image embeds in the origin-preserving automorphism group of a good special elliptic curve. In characteristic at least five that group has order 2, 4 or 6, by the short-Weierstrass coordinate calculation in Proposition 2.2. Wild inertia has trivial image, so the conductor is \(2-0=2\). In characteristics 2 and 3 that automorphism calculation and its prime-to-\(p\) conclusion fail; the examples in §6 have Swan terms three and one respectively.

**Exercise 8.4 (hard).** Derive the local factor at a nonsplit multiplicative prime from its Weil–Deligne pair. Include the conductor and explain why using the covariant block directly changes the factor.

*Solution.* The splitting character \(\chi\) is unramified quadratic, so \(\chi(\Phi)=-1\), and the covariant pair is \(\chi\mathrm{Sp}(2)\). Its smooth inertia is trivial, its monodromy has rank one, and its invariant kernel has dimension one. Formula (16) gives conductor one. For the arithmetic elliptic-curve factor use the dual pair \(\chi\|\cdot\|^{-1}\mathrm{Sp}(2)\); its kernel is the line of character \(\chi\), with Frobenius eigenvalue minus one. Thus the factor is \((1+q^{-s})^{-1}\). The covariant block instead has kernel character \(\chi\|\cdot\|\), with eigenvalue \(-q^{-1}\), giving \((1+q^{-s-1})^{-1}\). The shift comes from the dualization required by geometric Frobenius, rather than from a different reduction type.

## References and next reading

- J. Tate, *A review of non-Archimedean elliptic functions*, first part, pp.2–12; [freely accessible primary manuscript](https://web.ma.utexas.edu/users/voloch/Preprints/nonarch-ams.pdf). The two surjectivity arguments and their power-series lemma occur on pp.8–12.
- L. Berger, *An introduction to the theory of p-adic representations*, arXiv math/0210184v1, §II.4.1–§II.4.2; [version 1 manuscript](https://arxiv.org/abs/math/0210184v1) and [free author PDF](https://perso.ens-lyon.fr/laurent.berger/articles/article05.pdf).
- J. E. Cremona, *Algorithms for Modular Elliptic Curves*, [author's free online edition](https://johncremona.github.io/book/), [Chapter III](https://johncremona.github.io/book/fulltext/chapter3.pdf), §§3.1–3.2. Its scope and the remaining general proof obligation are distinguished in §7.

Continue with *Compatible systems and global L-functions*. The local pairs just computed will supply the bad-prime data that good-prime characteristic polynomials alone do not record.
