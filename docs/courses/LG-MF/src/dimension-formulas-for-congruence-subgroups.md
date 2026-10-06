# Dimension formulas for congruence subgroups

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A modular form changes when its argument is changed by a matrix, but a suitable differential built from it is invariant. The differential may have poles at the cusps and at elliptic points. Computing the allowed pole orders turns the problem of counting modular forms into a problem about line bundles on a compact curve.

We assume Modular curves and their genus and The valence formula and the ring of modular forms of level one. The slash operator and cusp expansions are those of Modular forms, lattice functions and Eisenstein series. We retain the even-weight formulas for every finite-index subgroup, odd weights, characters and arithmetic coefficient bounds. The degree formula and complex bound are derived below by a finite norm from the earlier valence proof. Appendix A proves the compact-curve theorem of Section 1, including arbitrary line bundles and the analytic/topological genus comparison. The elementary real and Hilbert-space framework listed there still needs exact programme proof verification, and the arithmetic input in Section 6.1 remains unproved; full proof closure is not claimed.

Let \(\Gamma\) be such a subgroup, let \(\bar\Gamma\) be its image in \(\mathrm{PSL}_2(\mathbb Z)\), and write
\[
X=X(\Gamma),\qquad
d=[\mathrm{PSL}_2(\mathbb Z):\bar\Gamma].
\]
Let \(g\) be the genus, \(e_2,e_3\) the numbers of elliptic orbits of projective orders two and three, and \(c\) the number of cusps. Let
\[
C=\sum_{\text{cusps }P}P
\]
be the reduced cusp divisor. In particular \(c\ge1\). All dimensions below are over \(\mathbb C\).

## 1. The compact-curve theorem we use

A holomorphic line bundle \(\mathcal L\) is locally a product with a one-dimensional vector space, with nonvanishing holomorphic transition functions. Its holomorphic sections form the vector space \(H^0(X,\mathcal L)\), of dimension \(h^0(\mathcal L)\). Write \(\mathcal K=\Omega_X^1\) for the canonical bundle.

For an integral divisor \(D=\sum n_PP\), the bundle \(\mathcal L(D)\) allows its meromorphic sections to have order at least \(-n_P\) relative to a holomorphic frame of \(\mathcal L\) at \(P\). Its degree is
\[
\deg\mathcal L(D)=\deg\mathcal L+\sum n_P.
\]
Degrees add under tensor products. A nonzero holomorphic section has an effective zero divisor of degree \(\deg\mathcal L\); consequently a bundle of negative degree has no such section.

Appendix A proves the following theorem, including duality and existence of meromorphic sections, relative to the elementary analytic framework stated there. Its genus identification uses the finite-polygon proof in the preceding lesson 03, Appendix A.

**Riemann–Roch and duality.** On a compact connected Riemann surface of genus \(g\), every holomorphic line bundle satisfies
\[
h^0(\mathcal L)-h^0(\mathcal K\otimes\mathcal L^{-1})
=\deg\mathcal L+1-g.
\tag{1.1}
\]
Also
\[
\deg\mathcal K=2g-2,\qquad h^0(\mathcal K)=g.
\tag{1.2}
\]
Here the analytic and topological genera agree.

The free analytic notes [McMullen, *Riemann Surfaces*, Theorems 11.1–11.2, Corollaries 9.10–9.11 and Corollary 14.4] contain source material for this dependency. The alternative algebraic route is [Stacks, Tag 0BS6], after constructing a smooth projective model and proving the comparison in the free original article [Serre 1956, §3, no. 12, Theorems 1–3]. Algebraization is a separate theorem, recorded in [Teleman 2003, Lecture 14]. These free sources are writing material; the analytic argument used here is written in Appendix A. The alternative algebraic route requires its own algebraization and comparison proofs. For the modular surface used here the canonical-degree part of (1.2) can nevertheless be established locally, as follows.

**Lemma 1.1 (canonical degree for this modular curve).** The divisor of a nonzero meromorphic differential on \(X\) has total order \(2g-2\).

*Proof.* Let \(J=j\circ\pi\), using the modular covering from lesson 03, Proposition 3.2, and the biholomorphism \(j:X(1)\to\mathbb P^1\) proved in lesson 05, Theorem 3.1. The sphere differential \(dt\) has no finite zero and has order \(-2\) at infinity, since \(t=1/v\) gives \(dt=-v^{-2}dv\). Under a local map \(t-t_0=u^r\), its pullback has order \(r-1\); at a pole \(t=u^{-r}\), it has order \(-r-1\). Proposition 3.2 gives all these indices. At the cusps their sum is \(d\), so the total order of \(dJ\) is
\[
-2d+\sum_P(r_P-1)=2g-2,
\]
where the last equality is the explicit modular-cover cell count in lesson 03, Section 3. This differential is nonzero because the displayed local derivatives are nonzero away from branching.

Any other nonzero meromorphic differential is \(h\,dJ\) for a meromorphic function \(h\) on \(X\). The divisor of \(h\) has total order zero: remove small coordinate discs around its finitely many zeros and poles, integrate the globally defined \(dh/h\) along their boundaries, and subdivide the remaining surface cells into coordinate triangles. Cauchy's theorem on each triangle gives zero, and internal edge integrals cancel. The boundary circles therefore sum to zero, while each circle contributes \(2\pi i\operatorname{ord}_P(h)\) by lesson 05, Lemma 0.1. This proves the claim, using the Cauchy proof in lesson 01, Lemma 0.2, and the elementary surface subdivision foundations still recorded there. It proves \(\deg\mathcal K=2g-2\) here without Riemann–Roch. It does not prove \(h^0(\mathcal K)=g\) or general duality. \(\square\)

## 2. Descending an even-weight form

For an even integer \(k=2m\), a meromorphic modular form produces
\[
\omega_f=f(z)(dz)^m.
\tag{2.1}
\]
Indeed, \(\gamma'(z)=(cz+d)^{-2}\) cancels the weight-\(2m\) transformation factor. The differential is invariant and descends away from the elliptic points and cusps. Tensor powers with negative \(m\) mean powers of the dual canonical bundle. Even-weight forms are unchanged on replacing \(\Gamma\) by the subgroup generated by \(\Gamma\) and \(-I\), so all local calculations depend only on \(\bar\Gamma\).

### 2.1. The elliptic rounding

At an elliptic point \(p\) of order \(e\), choose the rotation coordinate \(w\) used in the modular-curve lesson: the stabilizer acts by \(w\mapsto\zeta w\), with \(\zeta\) a primitive \(e\)-th root of unity, and the quotient coordinate is \(u=w^e\).

Write the pulled-back differential as \(\Phi(w)(dw)^m\). Since \(z\) and \(w\) are ordinary local coordinates, \(\Phi\) and \(f\) have the same order \(v_p(f)\). Invariance says
\[
\Phi(\zeta w)\zeta^m=\Phi(w).
\]
Thus every nonzero Laurent coefficient with exponent \(n\) satisfies \(n+m\equiv0\pmod e\). Since
\[
(dw)^m=e^{-m}w^{-m(e-1)}(du)^m,
\]
the descended order at the quotient point \(P\) is the integer
\[
\operatorname{ord}_P(\omega_f)
=\frac{v_p(f)-m(e-1)}e.
\tag{2.2}
\]
The factor \(e^{-m}\) is nonzero and has no effect on the order.

It follows that holomorphy of \(f\) at \(p\) is equivalent to
\[
\operatorname{ord}_P(\omega_f)
\ge-\left\lfloor m\left(1-\frac1e\right)\right\rfloor.
\tag{2.3}
\]
This is where rounding enters. The ordinary zero order \(v_p(f)\), the weighted order \(v_p(f)/e\), and the integral order of the differential on \(X\) are three distinct quantities.

### 2.2. The cusp order

At a cusp \(P=\alpha\infty\), let \(h\) be its projective width and put \(q_h=e^{2\pi iz/h}\). Set \(F=f|_{2m}\alpha\). Even weight removes the possible negative sign in the cusp generator, so \(F\) is periodic with period \(h\). Let \(v_P(f)\) be its order as a meromorphic function of \(q_h\). Then
\[
F(z)(dz)^m
=\left(\frac h{2\pi i}\right)^m
F(q_h)q_h^{-m}(dq_h)^m,
\]
and hence
\[
\operatorname{ord}_P(\omega_f)=v_P(f)-m.
\tag{2.4}
\]
A holomorphic form allows a pole of order at most \(m\); a cusp form allows at most \(m-1\). These assertions are order inequalities and remain meaningful for negative \(m\).

Define the integral elliptic divisor
\[
D_m=
\sum_{\text{elliptic }P}
\left\lfloor m\left(1-\frac1{e_P}\right)\right\rfloor P.
\tag{2.5}
\]

**Theorem 2.1 (the differential dictionary).** For every even integer \(k=2m\), the map (2.1) induces isomorphisms
\[
\begin{aligned}
M_{2m}(\Gamma)&\simeq
H^0\bigl(X,\mathcal K^m(D_m+mC)\bigr),\\
S_{2m}(\Gamma)&\simeq
H^0\bigl(X,\mathcal K^m(D_m+(m-1)C)\bigr).
\end{aligned}
\tag{2.6}
\]
In particular \(S_2(\Gamma)\simeq H^0(X,\mathcal K)\).

**Proof.** On the ordinary part of the quotient, (2.1) is invariant and holomorphic. Equations (2.3)–(2.4) give exactly the allowed orders encoded by the two bundles in (2.6). Thus the map has the stated target.

Conversely, pull back a section of the first bundle to the half-plane and divide its local expression by \((dz)^m\). This produces a meromorphic function \(f\) with the weight-\(2m\) law. At an elliptic point, an integral order \(\ell\) downstairs becomes the order
\[
e\ell+m(e-1)
\]
of \(f\) upstairs. The bound \(\ell\ge-\lfloor m(e-1)/e\rfloor\) makes this number nonnegative. At a cusp, (2.4) makes the \(q_h\)-order \(\ell+m\), which is nonnegative for the first bundle and at least one for the second. Therefore the pulled-back function extends holomorphically and has precisely the required cusp conditions. Pullback and descent are inverse operations. Finally \(m=1\) gives \(D_1=0\) and \((m-1)C=0\), proving the weight-two assertion. \(\square\)

## 3. A zero count at every level

For a nonzero meromorphic form of even weight \(k\), sum the ordinary orders over ordinary orbits, the ordinary orders divided by \(e_P\) at elliptic orbits, and the cusp orders in their own coordinates \(q_h\).

**Theorem 3.1 (degree formula).** With these conventions,
\[
\sum_{\text{ordinary }P}v_P(f)
+\sum_{\text{elliptic }P}\frac{v_p(f)}{e_P}
+\sum_{\text{cusps }P}v_P(f)=\frac{kd}{12}.
\tag{3.1}
\]

**Proof by a finite norm.** Put \(\Gamma^+=\langle\Gamma,-I\rangle\). Even weight makes \(f\) invariant under this group. Choose left coset representatives \(\alpha_1,\ldots,\alpha_d\) for \(\Gamma^+\backslash\mathrm{SL}_2(\mathbb Z)\), and define
\[
\mathcal N(f)=\prod_{a=1}^d(f|_k\alpha_a).
\]
Changing representatives does not change a factor. Right multiplication by an integral determinant-one matrix permutes the cosets, so the right slash law of lesson 04, Proposition 1.1, makes \(\mathcal N(f)\) a nonzero meromorphic level-one form of weight \(kd\). Every factor has a meromorphic cusp expansion with a finite principal part. Their product is periodic with period one; hence it has such a Laurent expansion in the ordinary \(q\) coordinate.

At a base interior point with projective stabilizer order \(E\), an upstairs point with stabilizer order \(e_P\) corresponds to a cycle of \(E/e_P\) cosets under that stabilizer. Each associated slash factor has the same ordinary zero order \(v_p(f)\): its fractional linear substitution is a local coordinate change with nonzero derivative and its automorphy factor is nonvanishing. This cycle contributes \((E/e_P)v_p(f)\) to the ordinary order of the norm. Dividing by \(E\), as the level-one valence formula does, gives exactly \(v_p(f)/e_P\). This includes ordinary points above an elliptic base point, for which \(e_P=1\).

At a cusp of width \(h\), the corresponding translation cycle gives factors \(F(z+a)\), \(0\le a<h\), where \(F=f|_k\alpha\). If its leading term is \(Aq_h^n\), the product has leading term
\[
A^h\exp\left(\frac{2\pi i n}{h}\sum_{a=0}^{h-1}a\right)q_h^{hn}
=A' q^n,\qquad A'\ne0.
\]
Thus this cusp contributes \(n=v_P(f)\) to the norm's order at infinity. The translation cycles exhaust all cosets, by lesson 02, Section 2.

Apply lesson 05, Theorem 1.1, to \(\mathcal N(f)\). Its weighted interior and cusp orders are exactly the sum in (3.1), by the preceding two calculations, and its weight is \(kd\). This proves (3.1). The orders have finite support because the quotient is compact and each local meromorphic expansion has isolated zeros and poles. This norm proof uses neither Riemann–Roch nor the analytic genus comparison. \(\square\)

As an exact check on the norm's cusp orders, regard \(\Delta\) as a form for \(\Gamma_0(2)\). The three coset factors all equal \(\Delta\), since it has level one, so its norm is \(\Delta^3\). Upstairs the width-one cusp has order one and the width-two cusp has order two: there \(\Delta(z)=q+O(q^2)=q_2^2+O(q_2^4)\). Their sum is three, the norm's downstairs cusp order, and also \(12\cdot3/12\). This checks the use of integral cusp orders rather than orders divided by widths.

For a holomorphic form every term on the left is nonnegative. In particular there are no nonzero forms of negative even weight. Forms of negative odd weight also vanish: their square would be a nonzero holomorphic form of negative even weight.

Cusp widths are already included in the choice \(q_h\). If a local term is expressed as \(q^{n/h}\), its cusp order is \(n\), rather than \(n/h\). At infinity for \(\Gamma_0(N)\), the width is one, so the ordinary \(q\)-order can be used directly.

## 4. Dimensions, including the weight-two exception

**Theorem 4.1.** For every even \(k\ge4\),
\[
\begin{aligned}
\dim M_k(\Gamma)
&=(k-1)(g-1)
+\left\lfloor\frac k4\right\rfloor e_2
+\left\lfloor\frac k3\right\rfloor e_3
+\frac k2c,\\
\dim S_k(\Gamma)&=\dim M_k(\Gamma)-c.
\end{aligned}
\tag{4.1}
\]
In weight two,
\[
\dim S_2(\Gamma)=g,\qquad
\dim M_2(\Gamma)=g+c-1.
\tag{4.2}
\]
Also \(M_0(\Gamma)=\mathbb C\), \(S_0(\Gamma)=0\), and all negative-weight spaces vanish.

**Proof using Appendix A, with its stated elementary foundation requirements.** Let
\[
\mathcal A_m=\mathcal K^m(D_m+mC),\qquad
\mathcal B_m=\mathcal K^m(D_m+(m-1)C).
\]
We first identify the dual correction term in Riemann–Roch. For every integer \(m\) and positive integer \(e\),
\[
\left\lfloor(1-m)\left(1-\frac1e\right)\right\rfloor
=-\left\lfloor m\left(1-\frac1e\right)\right\rfloor.
\tag{4.3}
\]
Indeed, the right-hand floor equals \(m-\lceil m/e\rceil\). The left-hand floor is
\(1-m+\lfloor(m-1)/e\rfloor=\lceil m/e\rceil-m\), because
\(\lfloor(m-1)/e\rfloor+1=\lceil m/e\rceil\) for every integer \(m\).
Hence \(D_{1-m}=-D_m\).

It follows that
\[
\mathcal K\otimes\mathcal B_m^{-1}=\mathcal A_{1-m},
\qquad
\mathcal K\otimes\mathcal A_m^{-1}=\mathcal B_{1-m}.
\tag{4.4}
\]
By Theorem 2.1 their section spaces are \(M_{2-k}(\Gamma)\) and \(S_{2-k}(\Gamma)\). If \(k\ge4\), these vanish by the negative-weight conclusion of Theorem 3.1. Thus (1.1) gives
\[
h^0(\mathcal A_m)=\deg\mathcal A_m+1-g,\qquad
h^0(\mathcal B_m)=\deg\mathcal B_m+1-g.
\]
The degree of \(D_m\) is
\(\lfloor m/2\rfloor e_2+\lfloor2m/3\rfloor e_3\). Substituting
\[
\deg\mathcal A_m=m(2g-2)+\deg D_m+mc
\]
gives the first formula in (4.1). The bundles differ by \(C\), whose degree is \(c\), so their dimensions differ by \(c\).

For \(k=2\), the cusp bundle is \(\mathcal K\), giving \(g\) by (1.2). The modular bundle is \(\mathcal K(C)\), with dual correction bundle \(\mathcal O_X(-C)\). A holomorphic function on compact connected \(X\) is constant, and one vanishing at a cusp is zero. Consequently that correction term vanishes, and
\[
h^0(\mathcal K(C))=(2g-2+c)+1-g=g+c-1.
\]
The same constancy proves the weight-zero assertions. Negative odd weights were disposed of by squaring. \(\square\)

The constant-term map sends \(M_k(\Gamma)\) to \(\mathbb C^c\), with kernel \(S_k(\Gamma)\). For even \(k\ge4\), the proved dimension difference implies that every vector of cusp constants occurs. For weight two, there is one relation: the differential corresponding to \(f\) has residue
\[
\operatorname{Res}_P(f\,dz)
=\frac{h_P}{2\pi i}a_0(f|_2\alpha_P)
\]
at cusp \(P\). The residue theorem says
\[
\sum_P h_Pa_0(f|_2\alpha_P)=0.
\tag{4.5}
\]
The image has dimension \(c-1\) by (4.2), so it is exactly this hyperplane.

### 4.1. Recovering level one

For \(\mathrm{SL}_2(\mathbb Z)\), insert \(g=0,e_2=e_3=c=1\) into (4.1):
\[
\dim M_k=-(k-1)+\lfloor k/4\rfloor+\lfloor k/3\rfloor+k/2.
\]
Write \(k=12a+r\), with \(r\in\{0,2,4,6,8,10\}\). For \(k\ge4\), this is \(a\) plus the value
\[
1-r+\lfloor r/4\rfloor+\lfloor r/3\rfloor+r/2,
\]
whose six values are \(1,0,1,1,1,1\). Thus we recover exactly the preceding lesson's formula. In weight two, (4.2) gives \(\dim M_2=\dim S_2=0\). The modular-dimension expression in the first line of (4.1) still gives the correct value at \(k=2\), but subtracting \(c\) for the cusp dimension would give \(-1\). The weight-two correction concerns that subtraction.

## 5. Odd weights and character spaces

Odd weights require the actual subgroup in \(\mathrm{SL}_2(\mathbb Z)\), rather than only its projective image. If \(-I\in\Gamma\), every odd-weight space is zero. If a cusp has generator \(-T^h\), an odd-weight form has only odd powers of \(q_{2h}\); it has no constant term there. We call that cusp irregular. A regular cusp has generator \(T^h\).

### 5.1. The torsion-free case with regular cusps

For \(\Gamma_1(N)\), \(N\ge5\), all elliptic stabilizers are trivial and all cusps are regular, as proved in the congruence-subgroup lesson. For odd \(k\ge3\),
\[
\begin{aligned}
\dim M_k(\Gamma_1(N))&=(k-1)(g-1)+\frac k2c,\\
\dim S_k(\Gamma_1(N))&=(k-1)(g-1)+\left(\frac k2-1\right)c.
\end{aligned}
\tag{5.1}
\]
Solution 4 gives the complete line-bundle derivation, including the square-root relation
\(\mathcal L^2\simeq\mathcal K(C)\).

Weight one retains a correction term:
\[
\dim M_1(\Gamma_1(N))-\dim S_1(\Gamma_1(N))=\frac c2.
\tag{5.2}
\]
Neither individual dimension follows from \(g,c\) alone. The same derivation proves (5.2); it does not replace \(h^0\) by degree when the dual bundle has nonzero sections.

For the remaining small levels, the odd-weight cusp dimensions for \(k\ge3\) are
\[
\begin{array}{c|c|c}
N&\dim S_k(\Gamma_1(N))&\dim M_k(\Gamma_1(N))\\ \hline
1,2&0&0\\
3&\lfloor k/3\rfloor-1&\lfloor k/3\rfloor+1\\
4&(k-3)/2&(k+1)/2.
\end{array}
\tag{5.3}
\]
The level-three formulas follow from the character calculation in Section 5.2.6. The level-four formulas, including the contribution from its irregular cusp, are derived in Section 7.4 below.

### 5.2. The Cohen–Oesterlé formula

A Dirichlet character \(\chi\) modulo \(N\) is extended by zero away from units. The space \(M_k(N,\chi)\) consists of forms holomorphic at every cusp with
\[
f(\gamma z)=\chi(d)(cz+d)^k f(z),
\qquad
\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma_0(N).
\]
Its cusp subspace is \(S_k(N,\chi)\). If \(\chi(-1)\ne(-1)^k\), both spaces are zero, by applying \(-I\).

Here is the character formula for \(k\ge2\), recorded in the free [Stein author PDF, §6.3], with the cusp contribution also in [Best et al., §4.3]. The argument below derives the local frames and conductor count explicitly, but the dimension step remains conditional on the unresolved Riemann–Roch and duality dependency of Section 1. Let \(F\mid N\) be the conductor of \(\chi\), put
\[
\mu=N\prod_{p\mid N}(1+1/p),
\]
and, for \(r=v_p(N)>0\) and \(s=v_p(F)\), define
\[
\lambda(r,s,p)=
\begin{cases}
p^{r/2}+p^{r/2-1},&2s\le r,\ r\text{ even},\\
2p^{(r-1)/2},&2s\le r,\ r\text{ odd},\\
2p^{r-s},&2s>r.
\end{cases}
\]
Set \(E_\chi=\prod_{p\mid N}\lambda(v_p(N),v_p(F),p)\), with empty product one. Define
\[
A_4(N)=\{x\in\mathbb Z/N\mathbb Z:x^2+1=0\},
\quad
A_3(N)=\{x:x^2+x+1=0\},
\]
and
\[
\gamma_4(k)=
\begin{cases}1/4&k\equiv0\pmod4,\\-1/4&k\equiv2\pmod4,\\0&k\text{ odd},\end{cases}
\quad
\gamma_3(k)=
\begin{cases}1/3&k\equiv0\pmod3,\\-1/3&k\equiv2\pmod3,\\0&k\equiv1\pmod3.\end{cases}
\]
**Theorem 5.1 (character dimensions).** For parity-compatible \(\chi\),
\[
\begin{aligned}
\dim S_k(N,\chi)
={}&\frac{(k-1)\mu}{12}-\frac{E_\chi}{2}
\\&+\gamma_4(k)\sum_{x\in A_4(N)}\chi(x)
\\&+\gamma_3(k)\sum_{x\in A_3(N)}\chi(x)
+\delta_{k,2}\delta_{\chi,1},\\
\dim M_k(N,\chi)
={}&\dim S_k(N,\chi)\\
&+E_\chi-\delta_{k,2}\delta_{\chi,1}.
\end{aligned}
\tag{5.4}
\]
The level-one convention in the root sums is the unique residue modulo one, on which the trivial character has value one.

These are complex dimensions for one character. A sum over its Galois conjugates is a different space. No assertion about a rational coefficient field or descent is used in this formula.

#### 5.2.1. Local frames with a character

**Proof of Theorem 5.1, conditional on the Section 1 compact-curve theorem.** Work on the coarse compact curve \(X_0(N)\), whose genus and cusp and elliptic counts were computed in the earlier lessons. Parity compatibility makes the automorphy factor \(\chi(d)(cz+d)^k\) trivial on \(-I\). Away from elliptic points and cusps its cocycle therefore defines a line bundle.

At a cusp represented by the first column \((a,c)^t\) of \(\alpha\), the positive parabolic generator and width are
\[
\begin{gathered}
h=\frac{N}{\gcd(N,c^2)},\qquad P=\alpha T^h\alpha^{-1},\\
P=\begin{pmatrix}1-ach&a^2h\\-c^2h&1+ach\end{pmatrix}.
\end{gathered}
\tag{5.5}
\]
Write \(\chi(1+ach)=e^{2\pi i\theta_P}\) with \(0\le\theta_P<1\). The transformation law gives
\[
\begin{aligned}
(f|_k\alpha)(z+h)&=e^{2\pi i\theta_P}(f|_k\alpha)(z),\\
(f|_k\alpha)(z)&=q_h^{\theta_P}\sum_{n\ge0}b_nq_h^n.
\end{aligned}
\tag{5.6}
\]
The branch of \(q_h^{\theta_P}\) on the covering punctured disk is a frame with this monodromy. The quotient by that frame is single-valued, and extending its holomorphic coefficient to \(q_h=0\) defines the bundle at the cusp. A form is cuspidal there precisely when \(b_0=0\) if \(\theta_P=0\); if \(\theta_P>0\), every holomorphic form already vanishes there. Let \(c_\chi\) be the number of cusps with \(\theta_P=0\), and let \(C_\chi\) be their reduced divisor.

For an elliptic point of order \(e\), choose a lift \(\gamma\) fixing \(z_0\), put \(j_0=c_\gamma z_0+d_\gamma\), and use
\[
w=\frac{z-z_0}{z-\overline{z_0}},\qquad \zeta=j_0^{-2}.
\]
Then \(w(\gamma z)=\zeta w(z)\) and
\(c_\gamma z(w)+d_\gamma=j_0(1-\zeta w)/(1-w)\).
Consequently \(\psi(w)=(1-w)^{-k}f(z(w))\) satisfies
\[
\begin{aligned}
\psi(\zeta w)&=\chi(d_\gamma)j_0^k\psi(w),\\
\zeta^{r_P}&=\chi(d_\gamma)j_0^k,\qquad 0\le r_P<e,\\
\psi(w)&=w^{r_P}H(w^e).
\end{aligned}
\tag{5.7}
\]
Parity makes the multiplier an \(e\)-th root of unity, so the integer \(r_P\) exists and is unique. The coefficient \(H\) is holomorphic in the coarse coordinate \(u=w^e\). Taking \(w^{r_P}\) as the frame extends the bundle over this point. Changes of covering coordinate or scaling matrix give nonvanishing transition functions between these frames; the local orders and monodromies are unchanged.

Denote the resulting modular bundle by \(\mathcal L_{k,\chi}\), and put \(\mathcal B_{k,\chi}=\mathcal L_{k,\chi}(-C_\chi)\). The local descriptions prove
\[
\begin{aligned}
M_k(N,\chi)&=H^0(X_0(N),\mathcal L_{k,\chi}),\\
S_k(N,\chi)&=H^0(X_0(N),\mathcal B_{k,\chi}).
\end{aligned}
\tag{5.8}
\]

#### 5.2.2. Degree and the duality correction

Every line bundle on a compact curve has a nonzero meromorphic section: twist by a divisor of sufficiently large degree, apply (1.1), and regard a nonzero section of the twist as a meromorphic section of the original bundle. Apply this to \(\mathcal L_{k,\chi}\). Its corresponding meromorphic form \(f\), raised to the order of \(\chi\), has trivial character and even weight. Theorem 3.1 applies to that power. Dividing its weighted order sum by this order, and then removing the frame orders \(r_P/e_P\) and \(\theta_P\), gives
\[
\begin{aligned}
\deg\mathcal L_{k,\chi}
&=\frac{k\mu}{12}\\
&\quad-\sum_{P\text{ elliptic}}\frac{r_P}{e_P}
-\sum_{P\text{ cusp}}\theta_P,\\
\deg\mathcal B_{k,\chi}&=\deg\mathcal L_{k,\chi}-c_\chi.
\end{aligned}
\tag{5.9}
\]
Cusp orders here use their own \(q_h\); no additional width factor is inserted.

Multiplication of forms, followed by \(fg\,dz\), gives bundle isomorphisms
\[
\begin{aligned}
\mathcal K\otimes\mathcal B_{k,\chi}^{-1}
&\simeq\mathcal L_{2-k,\chi^{-1}},\\
\mathcal K\otimes\mathcal L_{k,\chi}^{-1}
&\simeq\mathcal B_{2-k,\chi^{-1}}.
\end{aligned}
\tag{5.10}
\]
Here is a local check that rules out a hidden correction divisor. At a cusp with nonzero \(\theta_P\), the inverse character has exponent \(1-\theta_P\); the product has order one, cancelling the pole of \(dz=(h/2\pi i)dq_h/q_h\). At a cusp with zero exponent, the factor from the cusp bundle supplies that order one. At an elliptic point the weight-two product has multiplier \(\zeta^{-1}\), so its two frame exponents add to \(e-1\). Also \(dz\) is a nonzero constant times \((1-w)^{-2}dw\). Thus the product becomes a nonzero multiple of \(w^{e-1}dw=du/e\), a frame of \(\mathcal K\).

A holomorphic form of negative weight and finite-order character is zero: raise it to the character order and apply the negative even-weight consequence of Theorem 3.1. A weight-zero form with character is also easy to determine. Its corresponding power is a holomorphic function on the compact curve, hence constant. A nonzero such form is constant on \(\mathfrak H\), so its transformation law forces \(\chi\) to be trivial; the map \(\Gamma_0(N)\to(\mathbb Z/N\mathbb Z)^\times\), \(\gamma\mapsto d\), is surjective by the congruence-subgroup lesson. No nonzero constant is a cusp form. Therefore Riemann–Roch and (5.10), for \(k\ge2\), give
\[
\begin{aligned}
\dim S_k(N,\chi)&=\deg\mathcal B_{k,\chi}+1-g
\\&\quad+\delta_{k,2}\delta_{\chi,1},\\
\dim M_k(N,\chi)&=\deg\mathcal L_{k,\chi}+1-g.
\end{aligned}
\tag{5.11}
\]
This argument retains exactly the weight-two correction and makes no vanishing claim in weight one.

Reflection of a cusp \(a/c\) to \(-a/c\) pairs its exponent with the inverse-character exponent. Indeed \(N\mid c^2h\) implies \((1+ach)(1-ach)\equiv1\pmod N\). Reflection preserves cusp equivalence and width: conjugation by \(\operatorname{diag}(-1,1)\) preserves \(\Gamma_0(N)\). Nonzero paired exponents sum to one, and zero exponents remain zero. A reflected cusp fixed by this pairing has exponent zero or one half. Hence
\[
\sum_{P\text{ cusp}}\theta_P=\frac{c-c_\chi}{2}.
\tag{5.12}
\]
Substitute (5.9) and the genus formula into (5.11):
\[
\begin{aligned}
\dim S_k(N,\chi)
={}&\frac{(k-1)\mu}{12}-\frac{c_\chi}{2}
\\&+\frac{e_2}{4}-\sum_{e_P=2}\frac{r_P}{2}\\
&+\frac{e_3}{3}-\sum_{e_P=3}\frac{r_P}{3}
+\delta_{k,2}\delta_{\chi,1},\\
\dim M_k(N,\chi)
={}&\dim S_k(N,\chi)\\
&+c_\chi-\delta_{k,2}\delta_{\chi,1}.
\end{aligned}
\tag{5.13}
\]
It remains to evaluate the elliptic terms and \(c_\chi\).

#### 5.2.3. The elliptic terms

Use the fixed-coset description from Theorem 3.1 of the congruence-subgroup lesson. A coset represented by \(g\), with bottom row \((c,d)\), is fixed by right multiplication by \(S\) precisely when
\((d,-c)=x(c,d)\pmod N\). Here \(c\) is a unit, \(x^2=-1\), and the lower-right entry of \(gSg^{-1}\) is \(x\) modulo \(N\). At \(i\), the standard lift has \(j_0=i\) and \(\zeta=-1\). Its contribution to (5.13) is therefore
\[
\frac14-\frac{r_P}{2}=\frac{i^k\chi(x)}4.
\tag{5.14}
\]
For even \(k\) this is the prescribed \(\gamma_4(k)\chi(x)\). For odd \(k\), the root permutation \(x\mapsto-x\) and \(\chi(-1)=-1\) make the sum zero. This includes a fixed root of that permutation, if present: its character value would have to equal its own negative, so an odd character cannot occur with that root.

For order three use \(R=-ST=\begin{pmatrix}0&1\\-1&-1\end{pmatrix}\), which fixes \(\rho=e^{2\pi i/3}\). Its fixed-row condition is
\((-d,c-d)=x(c,d)\), giving \(x^2+x+1=0\) and lower-right entry \(x\) for \(gRg^{-1}\). Now \(j_0=\rho^2\), \(\zeta=\rho^2\). Write \(\chi(x)=\rho^t\), \(t\in\{0,1,2\}\). Equation (5.7) yields
\[
\begin{gathered}
r_P\equiv k-t\pmod3,\\
0\le r_P<3.
\end{gathered}
\tag{5.15}
\]
The contribution is \((1-r_P)/3\). The root permutation \(x\mapsto x^{-1}\) interchanges the values \(\rho\) and \(\rho^2\); they therefore occur equally often. A root fixed by inversion has character value one. For \(k\equiv0,1,2\pmod3\), respectively, a root of character value one contributes \(1/3,0,-1/3\), and a pair of character values \(\rho,\rho^2\) contributes \(-1/3,0,1/3\). Since \(\rho+\rho^2=-1\), summing gives exactly \(\gamma_3(k)\sum_{x\in A_3(N)}\chi(x)\). This equality uses the paired sum; the individual contributions need not equal a complex character value times \(\gamma_3(k)\).

#### 5.2.4. Which cusps admit a constant term?

Use the cusp representatives \(a/c\) with \(c\mid N\) from Theorem 2.2 of the congruence-subgroup lesson. For each \(c\), their number is \(\varphi(\gcd(c,N/c))\). Fix \(p^r\Vert N\), put \(j=v_p(c)\), and let \(s=v_p(F)\). From (5.5),
\[
v_p(ch)=\max(j,r-j)=:t.
\tag{5.16}
\]
If \(j=0\) or \(j=r\), then \(1+ach\equiv1\pmod{p^r}\). Otherwise \(a\) is a unit at \(p\), so \(1+ach=1+p^tu\) modulo \(p^r\) for a unit \(u\), and \(2t\ge r\). The subgroup
\(H_t=\{1+p^tb\pmod{p^r}\}\)
has multiplication corresponding to addition of \(b\) modulo \(p^{r-t}\), because \(p^{2t}\) vanishes modulo \(p^r\). Thus \(1+p^tu\) generates \(H_t\). The local character is trivial on this generator precisely when it is trivial on \(H_t\), which is precisely the conductor condition \(s\le t\). This argument works for \(p=2\) as well.

Decompose \(\chi\) into its local characters by the Chinese remainder theorem. Each local value on the parabolic generator has \(p\)-power order. Values at different primes have relatively prime orders, so their product is one if and only if each is one. For example, raising the product to an integer that is one modulo one such order and zero modulo all the others isolates that factor. Consequently the cusp is counted by \(c_\chi\) exactly when \(\max(j,r-j)\ge s\) at every prime. The condition is independent of its numerator.

The number of numerator classes factors over primes, so
\[
c_\chi=
\prod_{p^r\Vert N}
\sum_{\substack{0\le j\le r\\\max(j,r-j)\ge s}}
\varphi\bigl(p^{\min(j,r-j)}\bigr).
\tag{5.17}
\]
Use \(\sum_{j=0}^a\varphi(p^j)=p^a\). If \(2s\le r\), every \(j\) is allowed. For \(r=2m\) the sum is
\(2p^{m-1}+\varphi(p^m)=p^m+p^{m-1}\); for \(r=2m+1\) it is \(2p^m\). If \(2s>r\), the allowed ranges \(j\le r-s\) and \(j\ge s\) are disjoint, and their sum is \(2p^{r-s}\). These are exactly the three branches of \(\lambda(r,s,p)\). Thus \(c_\chi=E_\chi\). Combining this with Section 5.2.3 and (5.13) proves (5.4). \(\square\)

#### 5.2.5. A conductor changes the cusp contribution

At level \(25\), the unit \(2\) generates the group of order twenty. Put \(\zeta_5=e^{2\pi i/5}\) and define \(\chi(2)=\zeta_5\). This character is even, since \(-1=2^{10}\), and has conductor \(25\), since \(2^4=16\equiv1\pmod5\) but \(\chi(16)=\zeta_5^4\ne1\). Here \(r=s=2\), so \(E_\chi=2\): only the denominator classes \(c=1,25\) admit constant terms. The four cusps with \(c=5\) have nontrivial monodromy.

The index is \(30\), the order-two roots are \(7=2^5\) and \(18=2^{15}\), both with character value one, and there are no order-three roots. Weight two therefore gives
\[
\begin{aligned}
\dim S_2(25,\chi)&=\frac{30}{12}-1-\frac24=1,\\
\dim M_2(25,\chi)&=1+2=3.
\end{aligned}
\tag{5.18}
\]
These are the dimensions for this one character, not the sum for its four Galois conjugates. Exercise 6 compares them with a character of conductor five.

#### 5.2.6. The level-three odd-weight formula

Let \(\chi_3\) be the nontrivial character modulo three. The quotient \(\Gamma_0(3)/\Gamma_1(3)\) has order two and is represented by \(\pm I\). Hence every odd-weight form on \(\Gamma_1(3)\) has the \(\chi_3\) transformation law on \(\Gamma_0(3)\). The same statement holds for cusp forms. Now \(\mu=4\), \(E_{\chi_3}=2\), \(A_4(3)\) is empty, and \(A_3(3)=\{1\}\). For odd \(k\ge3\), (5.4) becomes
\[
\begin{aligned}
\dim S_k(\Gamma_1(3))
&=\frac{k-1}{3}-1+\gamma_3(k)
\\&=\left\lfloor\frac k3\right\rfloor-1,\\
\dim M_k(\Gamma_1(3))
&=\left\lfloor\frac k3\right\rfloor+1.
\end{aligned}
\tag{5.19}
\]
The floor equality follows by checking the three residues of \(k\) modulo three. This proves the remaining level-three row of (5.3).

## 6. How many coefficients determine a form?

**Theorem 6.1 (the complex coefficient bound).** If \(f\in M_k(\Gamma_0(N))\) and
\[
a_n(f)=0\quad\text{for every integer }0\le n\le
\left\lfloor\frac{k[\mathrm{SL}_2(\mathbb Z):\Gamma_0(N)]}{12}\right\rfloor,
\tag{6.1}
\]
then \(f=0\).

**Proof.** Negative-weight spaces are zero and odd-weight spaces vanish by \(-I\), so assume \(k\ge0\) is even. The projective and linear indices of \(\Gamma_0(N)\) agree, since it contains \(-I\). Its cusp at infinity has width one. If a nonzero form satisfied (6.1), its order at that cusp would be at least
\[
\left\lfloor kd/12\right\rfloor+1>kd/12.
\]
This contradicts Theorem 3.1, whose other terms are all nonnegative. \(\square\)

The same bound holds for \(M_k(N,\chi)\). To see this, let \(r\) be the finite order of \(\chi\). Then \(f^r\) has trivial character, weight \(rk\), and order \(r\,v_\infty(f)\). That weight is even by the character parity condition. If \(v_\infty(f)>kd/12\), the order of \(f^r\) exceeds \(rkd/12\), giving the same contradiction. Thus this extension also has a proof.

The endpoint in (6.1) is inclusive, and coefficient zero is required for modular forms. For cusp forms it vanishes automatically. This is a uniqueness theorem over \(\mathbb C\). Congruences between integral coefficient sequences modulo a prime require the arithmetic argument below.

### 6.1. Reduction modulo a prime

Let \(K\) be a number field with ring of integers \(\mathcal O_K\), and let \(\mathfrak p\) be a nonzero prime ideal. For a series with coefficients integral at \(\mathfrak p\), define
\[
v_{\mathfrak p}(f)=\min\{r:a_r(f)\notin\mathfrak p\},
\tag{6.2}
\]
with value \(\infty\) when every coefficient reduces to zero. The exponents may lie in \(L^{-1}\mathbb Z\). Since the residue ring is a field, the first nonzero coefficients multiply without cancellation. Thus the order of a product is the sum of the orders.

The next arithmetic statement is a required but unresolved proof dependency. Its free source is available, but its model construction and comparison have neither been reproduced here nor matched to an earlier programme proof. The statements needed are these: For principal level \(L\ge3\), the complex modular-form space has a basis whose Fourier expansions are defined over \(\mathbb Q(\zeta_L)\). The determinant-one slash action preserves this field structure. Each such form has bounded denominators in its expansions at the cusps: one nonzero integer clears all coefficients of each expansion. The geometric statements supplying this input are [Deligne–Rapoport free original scan, VII.3.8, VII.3.10–3.11 and VII.4.6], with the formal cusp description in VII.2.4. Their model construction and GAGA comparison are stated inputs here. Bounded denominators do not assert that the slash action preserves the integral lattice at a prime dividing \(L\).

Here is why the input applies to a form whose coefficients at infinity lie in \(K\). Choose finitely many coefficient functionals that are independent on the principal-level space; they exist because a form with zero Fourier expansion is zero. Their matrix on the field-defined basis is invertible over \(\mathbb Q(\zeta_L)\). Solving for the coordinates of our form puts them in \(K(\zeta_L)\). Applying any determinant-one slash operator therefore gives coefficients in this same number field, with bounded denominators. This is finite-dimensional descent, rather than applying a field automorphism to an infinite series.

**Theorem 6.2 (the arithmetic coefficient bound).** Let \(\Gamma\) contain \(\Gamma(L)\), put \(m=[\mathrm{SL}_2(\mathbb Z):\Gamma]\), and let \(k\ge0\). If \(f\in M_k(\Gamma)\) has coefficients in \(\mathcal O_K\) and
\[
v_{\mathfrak p}(f)>km/12,
\tag{6.3}
\]
then all its coefficients belong to \(\mathfrak p\). There is no restriction on whether the residue characteristic divides the level.

**Proof of the norm argument, conditional on the arithmetic input above.** First suppose \(\Gamma=\mathrm{SL}_2(\mathbb Z)\). Write \(d=\dim M_k\). If \(d=0\), there is nothing to prove. Otherwise the integral basis constructed in Solution 5 of the level-one ring lesson satisfies
\[
\begin{aligned}
F_j&=q^j+O(q^d),\quad 0\le j<d,\\
d-1&\le\lfloor k/12\rfloor.
\end{aligned}
\tag{6.4}
\]
In any expansion \(f=\sum_{j=0}^{d-1}c_jF_j\), its first \(d\) coefficients are exactly \(c_j\). This is a basis over \(\mathbb C\), and each \(F_j\) has integer coefficients. If those \(c_j\) lie in the prime ideal, every coefficient does too. The same argument works in the localization of any number ring at a prime ideal. It includes weight zero; the vanishing odd, negative and weight-two spaces were proved earlier.

For general \(\Gamma\), enlarge \(L\) if necessary so that \(L\ge3\), and choose left coset representatives \(\gamma_1=I,\gamma_2,\ldots,\gamma_m\). If \(f=0\) as a complex form, the claim is immediate. Otherwise set \(K'=K(\zeta_L)\) and choose a prime \(\mathfrak P\) over \(\mathfrak p\). Work in the discrete valuation ring \(D=(\mathcal O_{K'})_{\mathfrak P}\), with uniformizer \(\pi\) and maximal ideal \(\mathfrak P D\).

For each \(i\ge2\), the nonzero series \(f|_k\gamma_i\) has coefficient valuations bounded below. Its nonzero coefficients consequently have a least valuation \(t_i\in\mathbb Z\). Define
\[
h_i=\pi^{-t_i}(f|_k\gamma_i).
\tag{6.5}
\]
Every coefficient of \(h_i\) lies in \(D\), and at least one is a unit. Its reduction is therefore nonzero. All exponents are nonnegative because the original form is holomorphic at every cusp. We have used a separate scalar for each expansion and have made no integral-stability assertion about the slash action.

Consider the product
\[
\begin{aligned}
G&=f\prod_{i=2}^m h_i\\
&=\left(\prod_{i=2}^m\pi^{-t_i}\right)
 \prod_{i=1}^m(f|_k\gamma_i).
\end{aligned}
\tag{6.6}
\]
Right multiplication permutes the left cosets. The weight slash law therefore makes the second product invariant of weight \(km\) under the full modular group. It is holomorphic at the cusp, so \(G\in M_{km}(\mathrm{SL}_2(\mathbb Z))\). Its coefficients initially lie in \(D[[q^{1/L}]]\); invariance under \(z\mapsto z+1\) makes all noninteger exponents vanish. Thus its ordinary q-expansion has coefficients in \(D\).

The contraction of \(\mathfrak P\) to \(\mathcal O_K\) is \(\mathfrak p\), so the reduction of \(f\) has order \(v_{\mathfrak p}(f)\) over the residue field of \(D\). All the other factors have nonnegative order. Condition (6.3) gives
\[
v_{\mathfrak P}(G)\ge v_{\mathfrak p}(f)>km/12.
\tag{6.7}
\]
The full-level case proves that the reduction of \(G\) is zero. If the reduction of \(f\) were nonzero, its product with the nonzero reductions of the \(h_i\) would be nonzero in the power-series ring over a field. This contradicts (6.6). Hence every coefficient of \(f\) belongs to \(\mathfrak p\). \(\square\)

The proof also supplies the usual cusp-form refinement. With \(\Gamma(L)\subset\Gamma\) fixed, every \(h_i\) is cuspidal, so its reduction has order at least \(1/L\). It is enough to assume
\[
v_{\mathfrak p}(f)>km/12-(m-1)/L.
\tag{6.8}
\]
This refinement uses the chosen principal level \(L\); (6.3) is the uniform bound we will use.

**Corollary 6.3 (characters and integer congruences).** For \(f,g\in M_k(N,\chi)\) with coefficients in \(\mathcal O_K\), congruence of the coefficients with indices
\[
\begin{gathered}
0\le n\le B_0,\\
B_0=\left\lfloor\frac{k[\mathrm{SL}_2(\mathbb Z):\Gamma_0(N)]}{12}\right\rfloor.
\end{gathered}
\tag{6.9}
\]
modulo \(\mathfrak p\) implies congruence of every coefficient modulo \(\mathfrak p\).

**Proof.** Put \(h=f-g\), and let \(s\) be the order of \(\chi\). Then \(h^s\in M_{ks}(\Gamma_0(N))\). If \(h\) has nonzero reduction, its order is an integer at least \(B_0+1>k[\mathrm{SL}_2(\mathbb Z):\Gamma_0(N)]/12\). Its \(s\)-th power has \(s\) times that order. Theorem 6.2 forces this power to reduce to zero, contrary to the fact that a power-series ring over a field is a domain. Thus \(h\) reduces to zero. \(\square\)

For integer-coefficient forms, the same endpoint determines congruence modulo every positive integer \(M\). For a prime power \(p^e\), apply the prime case to \(h\), divide the entire form by \(p\) once its coefficients are divisible by \(p\), and repeat \(e\) times. Division changes neither weight nor level nor character, and preserves integer coefficients at each step. For general \(M\), do this for each prime power in its factorization. The analogous statement for \(\Gamma_1(N)\) uses its linear index in place of that of \(\Gamma_0(N)\). We do not replace that index by the projective index for odd weights.

**Corollary 6.4 (arbitrary ideal congruences).** If \(f,g\in M_k(N,\chi)\) have coefficients in \(\mathcal O_K\), congruence of their coefficients through the inclusive endpoint \(B_0\) of (6.9) modulo any nonzero integral ideal \(\mathfrak a\subset\mathcal O_K\) implies congruence of every coefficient modulo \(\mathfrak a\).

**Proof.** First work in the discrete valuation ring \(D=(\mathcal O_K)_{\mathfrak p}\), with uniformizer \(\pi\). The prime-congruence proof in Section 6.1 works for coefficients in \(D\): its full-level triangular-basis step already uses that localization. In the norm step choose a prime \(\mathfrak P\) above \(\mathfrak p\) in the coefficient-field extension. Elements of \(D\) are integral in its localization, and an element reduces to zero there exactly when it lies in \(\mathfrak pD\). The nonidentity slash transforms still have bounded valuations and are individually made primitive by scalars. Neither this normalization nor the residue-field power-series argument requires integrality at any other prime. The character-power argument is unchanged. Thus the endpoint also forces prime congruence for \(D\)-coefficient forms.

Put \(h=f-g\). If its first coefficients lie in \(\pi^eD\), the prime case makes every coefficient lie in \(\pi D\). The analytic form \(h/\pi\) has the same weight, level and character, has coefficients in \(D\), and has its first coefficients in \(\pi^{e-1}D\). Repeating \(e\) times puts every coefficient of \(h\) in \(\pi^eD\). Their original membership in \(\mathcal O_K\) gives
\[
\mathfrak p^eD\cap\mathcal O_K=\mathfrak p^e.
\tag{6.13}
\]
Finally factor \(\mathfrak a=\prod\mathfrak p^{e_{\mathfrak p}}\). Distinct prime powers are comaximal, so their intersection is their product. Applying the preceding argument at each factor proves the assertion. We used the standard prime-ideal factorization and localization properties of a number ring; no globally principal ideal is assumed. \(\square\)

### 6.2. A denominator at a prime dividing the level

Take \(f(z)=E_4(5z)\). For \(\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma_0(5)\), the matrix \(\begin{pmatrix}a&5b\\c/5&d\end{pmatrix}\) is integral of determinant one. The transformation of \(E_4\) consequently gives the weight-four law for \(f\). The two cusp classes are represented by infinity and zero. The expansion at infinity is holomorphic, and the transformation at zero is
\[
\begin{aligned}
(f|_4S)(z)&=5^{-4}E_4(z/5),\\
S&=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\end{aligned}
\tag{6.10}
\]
This follows by substituting \(w=z/5\) into \(E_4(-1/w)=w^4E_4(w)\); its expansion in \(q^{1/5}\) is holomorphic. Thus \(f\in M_4(\Gamma_0(5))\). Its q-coefficients at infinity are integers, but the constant coefficient in (6.10) is \(1/625\). The slash action has not preserved integrality at five.

The coset representatives \(I,ST^b\), \(0\le b<5\), are distinct and complete: their bottom rows modulo five are \((0:1)\) and \((1:b)\), the six points of \(\mathbb P^1(\mathbb F_5)\). Each nonidentity expansion becomes primitive integral at a prime above five after multiplication by \(625\):
\[
\begin{aligned}
625(f|_4ST^b)(z)&=E_4((z+b)/5)\\
&=1+240\sum_{r\ge1}\sigma_3(r)\zeta_5^{br}q^{r/5}.
\end{aligned}
\tag{6.11}
\]
Its constant coefficient is a unit. The normalized norm in the proof is therefore
\[
\begin{gathered}
G(z)=E_4(5z)\prod_{b=0}^4E_4((z+b)/5),\\
G\in M_{24}(\mathrm{SL}_2(\mathbb Z)).
\end{gathered}
\tag{6.12}
\]
All its coefficients are integral at that prime; periodicity removes the fractional exponents. Its constant coefficient is one, so its reduction is nonzero. This is exactly the separate normalization used in (6.5), at a prime dividing the level. The bound for \(f\) is \(\lfloor4\cdot6/12\rfloor=2\); its nonzero constant coefficient correctly prevents it from satisfying the vanishing hypothesis.

## 7. Worked examples

### 7.1. Weight two and the first positive genus

Here are the level counts for \(\Gamma_0(N)\), obtained in the congruence-subgroup and modular-curve lessons:

| \(N\) | \(d\) | \(e_2\) | \(e_3\) | \(c\) | \(g\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 0 |
| 2 | 3 | 1 | 0 | 2 | 0 |
| 3 | 4 | 0 | 1 | 2 | 0 |
| 4 | 6 | 0 | 0 | 3 | 0 |
| 5 | 6 | 2 | 0 | 2 | 0 |
| 6 | 12 | 0 | 0 | 4 | 0 |
| 7 | 8 | 0 | 2 | 2 | 0 |
| 8 | 12 | 0 | 0 | 4 | 0 |
| 9 | 12 | 0 | 0 | 4 | 0 |
| 10 | 18 | 2 | 0 | 4 | 0 |
| 11 | 12 | 0 | 0 | 2 | 1 |

For example, at level seven the genus computation is
\(1+8/12-2/3-2/2=0\); at level ten it is
\(1+18/12-2/4-4/2=0\).
Since \(S_2\) is the space of holomorphic differentials, the table proves
\[
S_2(\Gamma_0(N))=0\quad(1\le N\le10),
\qquad
\dim S_2(\Gamma_0(11))=1.
\]
At level eleven, \(\dim M_2=g+c-1=2\). Thus the one-dimensional cusp space is a proper subspace of a two-dimensional modular-form space.

### 7.2. Level five and an explicit cusp form

For \(\Gamma_0(5)\), the data are \(d=6,e_2=2,e_3=0,c=2,g=0\). The dimensions in weights two, four and six are therefore
\[
\begin{array}{c|c|c}
k&\dim M_k&\dim S_k\\ \hline
2&1&0\\
4&-3+2+4=3&1\\
6&-5+2+6=3&1.
\end{array}
\tag{7.1}
\]
We prove that the weight-four cusp space is spanned by
\[
F(z)=\eta(z)^4\eta(5z)^4
=q\prod_{n\ge1}(1-q^n)^4(1-q^{5n})^4.
\tag{7.2}
\]
It is not enough to recognize its leading power: its transformation and its other cusp must be checked.

Put \(H=\eta^4\) and \(\zeta_6=e^{\pi i/3}\). The product definition and \(\eta^{24}=\Delta\) from the preceding lesson give
\[
H(z+1)=\zeta_6 H(z),\qquad H(-1/z)=-z^2H(z).
\tag{7.3}
\]
For the second identity, the sixth power of
\(H(-1/z)/(z^2H(z))\) is one, by the weight-twelve law of \(\Delta\). This quotient is holomorphic and nonzero on connected \(\mathfrak H\), so it is constant. At \(i\) its value is \(-1\), proving (7.3).

Since \(S,T\) generate \(\mathrm{SL}_2(\mathbb Z)\), the weight-two slash action gives
\[
H|_2\gamma=\zeta_6^{\,t(\gamma)}H
\]
for a homomorphism \(t:\mathrm{SL}_2(\mathbb Z)\to\mathbb Z/6\mathbb Z\) with \(t(S)=3,t(T)=1\). This homomorphism is well-defined: each matrix word acts on the fixed nonzero function \(H\), so two words representing the same matrix yield the same scalar.

For \(\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma_0(5)\), set
\[
\gamma'=\begin{pmatrix}a&5b\\c/5&d\end{pmatrix}\in\mathrm{SL}_2(\mathbb Z).
\]
Then \(5\gamma z=\gamma'(5z)\), and the two weight-two factors have the same denominator \(cz+d\). Consequently
\[
F|_4\gamma=\zeta_6^{\,t(\gamma)+t(\gamma')}F.
\tag{7.4}
\]
We now verify that this scalar is one on a generating set.

Left coset representatives for \(\Gamma_0(5)\) are
\(I,S,ST,ST^2,ST^3,ST^4\); their projective bottom rows are
\((0:1),(1:0),(1:1),(1:2),(1:3),(1:4)\).
For \(x=1,2,3,4\), let \(y\in\{1,2,3,4\}\) represent \(-x^{-1}\pmod5\), and set
\[
A_x=ST^xST^{-y}S^{-1}.
\]
The respective values of \(y\) are \(4,2,3,1\). Also put \(U=ST^5S^{-1}\).
The coset transitions under \(S,T\) give the generators
\[
T,\ -I,\ A_1,A_2,A_3,A_4,\ U.
\tag{7.5}
\]
For completeness, the \(T\)-transitions move \(ST^x\) to \(ST^{x+1}\), with the last transition contributing \(U\); the \(I\)-transition contributes \(T\). Under \(S\), \(I\) and \(S\) are exchanged, giving \(I\) and \(-I\), while the four nonzero \(x\)'s give \(A_x\). These transitions generate the subgroup: for a word \(g_1\cdots g_n\), choose the representative \(r_j\) of its \(j\)-th prefix coset. Then the elements \(r_{j-1}g_jr_j^{-1}\) telescope to the word when its final coset is the identity. Edges for inverse generators are inverses of forward edges, so the listed transitions suffice.

Direct matrix multiplication gives the following transformed words. The last columns are read by adding the \(S,T\) exponents modulo six.

| \(\gamma\) | Word for \(\gamma'\) | \(t(\gamma)\) | \(t(\gamma')\) |
|---|---|---:|---:|
| \(T\) | \(T^5\) | 1 | 5 |
| \(-I\) | \(-I=S^2\) | 0 | 0 |
| \(A_1\) | \(T^{-4}ST\) | 0 | 0 |
| \(A_2\) | \(T^{-2}ST^2\) | 3 | 3 |
| \(A_3\) | \(T^{-1}ST^2ST^2\) | 3 | 3 |
| \(A_4\) | \(T^{-1}ST^4\) | 0 | 0 |
| \(U\) | \(STS^{-1}\) | 5 | 1 |

For instance \(A_3=\begin{pmatrix}-3&-1\\10&3\end{pmatrix}\) and
\(A_3'=\begin{pmatrix}-3&-5\\2&3\end{pmatrix}=T^{-1}ST^2ST^2\).
Every row has sum zero modulo six, so (7.4) proves the required weight-four law on all of \(\Gamma_0(5)\).

The two cusps are infinity, of width one, and zero, of width five. At infinity, (7.2) begins with \(q\), so the order is one. At zero, (7.3) gives
\[
(F|_4S)(z)=\frac1{25}H(z)H(z/5).
\]
In \(q_5=e^{2\pi iz/5}\), this is
\[
\frac1{25}q_5
\prod_{n\ge1}(1-q_5^{5n})^4(1-q_5^n)^4.
\tag{7.6}
\]
It is holomorphic with cusp order one. All these products converge locally uniformly and are nonzero on \(\mathfrak H\), by the logarithm argument in the preceding lesson. Thus \(F\in S_4(\Gamma_0(5))\), and \(F\ne0\). The dimension in (7.1) makes it a basis.

As a coefficient check, multiplication of the factors contributing through \(q^5\) gives
\[
F=q-4q^2+2q^3+8q^4-5q^5-8q^6+O(q^7).
\]
The two cusp orders also exhaust the degree \(4\cdot6/12=2\), agreeing with its absence of interior zeros.

### 7.3. The dimensions needed for four squares

For \(\Gamma_0(4)\), the index is six, there are three cusps, no elliptic points, and genus zero. Hence
\[
\dim M_2(\Gamma_0(4))=0+3-1=2,\qquad
\dim S_2(\Gamma_0(4))=0,
\]
and
\[
\dim M_4(\Gamma_0(4))=-3+2\cdot3=3,\qquad
\dim S_4(\Gamma_0(4))=0.
\]
These are the spaces used later when theta series turn counting lattice points into coefficient identities.

### 7.4. The single irregular cusp at level four

The group \(\Gamma_1(4)\) has no elliptic points, does not contain \(-I\), and has two regular cusps and one irregular cusp \(P_*\). Its compactified curve has genus zero.

On the ordinary quotient, the weight-one automorphy factor defines a line bundle \(\mathcal L\). At a regular cusp extend its frame by the constant Fourier mode. At \(P_*\), use the frame with leading term \(q_h^{1/2}\): an odd-weight form is antiperiodic and dividing by this term makes it a single-valued holomorphic function of \(q_h\). Let \(C_{\mathrm{reg}}\) be the sum of the two regular cusps.

The local differential calculation gives
\[
\mathcal L^2\simeq\mathcal K(C_{\mathrm{reg}}).
\tag{7.7}
\]
At a regular cusp, the square of the weight-one frame corresponds to \(dz\), which has a simple pole. At the irregular cusp, its square contains \(q_h\), so \(q_h\,dz\) is a holomorphic nonzero differential. This proves the stated extension of the isomorphism at both types of cusp. Thus \(\deg\mathcal L=(-2+2)/2=0\).

For odd \(k\ge1\), the frame of \(\mathcal L^k\) at \(P_*\) starts with \(q_h^{k/2}\), whereas a holomorphic weight-\(k\) form may start with \(q_h^{1/2}\). Therefore
\[
\begin{aligned}
M_k(\Gamma_1(4))
&\simeq H^0\bigl(X,\mathcal L^k((k-1)P_*/2)\bigr),\\
S_k(\Gamma_1(4))
&\simeq H^0\bigl(X,\mathcal L^k((k-1)P_*/2-C_{\mathrm{reg}})\bigr).
\end{aligned}
\tag{7.8}
\]
There is no extra cusp condition at \(P_*\), because its permitted half-integral powers already tend to zero. As in Theorem 2.1, pullback of these sections proves both directions.

The degrees in (7.8) are \((k-1)/2\) and \((k-5)/2\). On genus-zero \(X\), Riemann–Roch gives \(h^0(\mathcal A)=\deg\mathcal A+1\) when \(\deg\mathcal A\ge-1\): its dual correction has degree \(-2-\deg\mathcal A<0\). Thus for odd \(k\ge3\),
\[
\dim M_k=(k+1)/2,\qquad \dim S_k=(k-3)/2,
\]
as claimed in (5.3). For \(k=1\), the modular bundle has degree zero and dimension one, while the cusp bundle has negative degree and no sections.

In particular \(M_3\) has dimension two and \(S_3=0\). The modular-minus-cusp dimension is two, the number of regular cusps. An irregular cusp must not be counted as another independent constant term.

## 8. Exercises

1. **Easy.** Compute \(\dim M_k(\Gamma_0(5))\) and \(\dim S_k(\Gamma_0(5))\) for \(k=2,4,6\), displaying the substitution into the formulas.
2. **Medium.** Prove that \(S_2(\Gamma_0(N))=0\) for every \(N\le10\) and for \(N=12,13,16,18,25\).
3. **Medium.** Apply the coefficient bound to \(S_2(\Gamma_0(11))\) and \(M_4(\Gamma_0(4))\). Specify the coefficient indices, including the constant coefficient when necessary. Determine whether the bound is optimal in these two examples.
4. **Hard.** For odd \(k\ge3\) and \(N\ge5\), derive (5.1) from Riemann–Roch. Construct the weight-one line bundle, check its square at every cusp, and identify the dual correction. Explain what changes in weight one.

5. **Medium.** Let \(f,g\in M_{24}(\mathrm{SL}_2(\mathbb Z))\) have integer coefficients. Show that congruence of \(a_0,a_1,a_2\) modulo \(25\) implies congruence of every coefficient. Using the integral basis \(F_1,F_2\) from Solution 5 of the level-one ring lesson, construct a form for which \(a_0,a_1\) vanish modulo \(25\) but \(a_2\) does not. Explain why the endpoint must be included.
6. **Medium.** Let \(\eta\) be the quadratic character modulo five, regarded as a character modulo twenty-five, and let \(\chi(2)=\zeta_5\) as in Section 5.2.5. Determine both conductors, the numbers of cusps admitting constant terms, and the dimensions of their modular and cusp spaces in weights two and four. Check the parabolic character values at the four cusps with denominator five. Explain why equal level and parity do not imply equal dimensions.

## 9. Full solutions

### Solution 1

The level-five data are \(g=0,e_2=2,e_3=0,c=2\). Weight two has its own formula:
\[
\dim S_2=g=0,\qquad \dim M_2=g+c-1=1.
\]
For weight four, \(\lfloor4/4\rfloor=1\), so
\[
\dim M_4=3(-1)+1\cdot2+0+2\cdot2=3,
\quad
\dim S_4=3-2=1.
\]
For weight six, \(\lfloor6/4\rfloor=1\), so
\[
\dim M_6=5(-1)+1\cdot2+0+3\cdot2=3,
\quad
\dim S_6=3-2=1.
\]
The elliptic contribution is two in both weights, while the cusp contribution grows from four to six. The exceptional weight-two formula gives the missing distinction.

### Solution 2

By Theorem 2.1 and (1.2), it suffices to verify genus zero. For \(N=1,\ldots,10\), the complete count table in Section 7.1 has genus zero in every row.

For the remaining levels the counts and genus substitutions are:

| \(N\) | \(d\) | \(e_2\) | \(e_3\) | \(c\) | \(1+d/12-e_2/4-e_3/3-c/2\) |
|---:|---:|---:|---:|---:|---|
| 12 | 24 | 0 | 0 | 6 | \(1+2-3=0\) |
| 13 | 14 | 2 | 2 | 2 | \(1+7/6-1/2-2/3-1=0\) |
| 16 | 24 | 0 | 0 | 6 | \(1+2-3=0\) |
| 18 | 36 | 0 | 0 | 8 | \(1+3-4=0\) |
| 25 | 30 | 2 | 0 | 6 | \(1+5/2-1/2-3=0\) |

Here is also a direct arithmetic check of the less immediate cusp counts. For level twelve, the divisors \(1,2,3,4,6,12\) all contribute one to
\(\sum_{a\mid N}\varphi(\gcd(a,N/a))\), giving six. At level sixteen the five divisors \(1,2,4,8,16\) contribute \(1,1,2,1,1\), again six. At level eighteen the divisors \(1,2,3,6,9,18\) contribute \(1,1,2,2,1,1\), giving eight. At level twenty-five the contributions are \(1,4,1\), giving six. A prime level has two cusps, so \(c(13)=2\).

The previously proved elliptic formulas give no elliptic points at levels divisible by four, and none at eighteen because it is even and divisible by nine. At thirteen there are two of each order, because \(13\equiv1\pmod{12}\); at twenty-five there are two of order two and none of order three. The indices follow from \(N\prod_{p\mid N}(1+1/p)\). Thus every entry in the table follows from the established counting formulas, and every listed weight-two cusp space has dimension zero.

### Solution 3

For \(\Gamma_0(11)\), the index is twelve. In weight two the coefficient endpoint is
\(\lfloor2\cdot12/12\rfloor=2\). Therefore \(a_0,a_1,a_2\) determine a modular form by the bound. In the cusp space \(a_0=0\) is known in advance, so the bound uses the two coefficients \(a_1,a_2\).

Here one can sharpen it. A nonzero cusp form vanishes to order at least one at each of the two cusps. Its degree sum is exactly \(2\cdot12/12=2\). Thus its order at infinity is exactly one, and \(a_1\ne0\). The linear map \(f\mapsto a_1(f)\) on the one-dimensional cusp space is injective. One coefficient therefore suffices, although the general bound supplies two.

For \(\Gamma_0(4)\), the index is six and the weight is four. The endpoint is
\(\lfloor4\cdot6/12\rfloor=2\), so the three coefficients
\(a_0,a_1,a_2\) determine an element of \(M_4(\Gamma_0(4))\).
This space has dimension three. An injective linear map from it to \(\mathbb C^3\) is an isomorphism; no two scalar linear coefficient measurements can be injective on a three-dimensional vector space. Thus this coefficient count is optimal in the usual linear sense.

### Solution 4

The action of \(\Gamma_1(N)\), \(N\ge5\), on \(\mathfrak H\) is free: it has neither \(-I\) nor elliptic elements. Form a line bundle on the ordinary quotient by identifying
\[
(z,t)\sim(\gamma z,(cz+d)t).
\tag{9.1}
\]
The cocycle identity makes these identifications consistent. A section is exactly a holomorphic function with the weight-one law.

Every cusp is regular. In a scaling coordinate, the weight-one function \(f|_1\alpha\) is periodic with period \(h\); extend the bundle by the Fourier coordinate \(q_h\), allowing this periodic function to be holomorphic at \(q_h=0\). This specifies a holomorphic line bundle \(\mathcal L\) on all of \(X\). Changing a scaling matrix changes the frame by a nonzero constant and rotates \(q_h\), so the extension is independent of that choice.

On the half-plane the square of (9.1) is identified with differentials by \(f\mapsto f\,dz\). At a cusp the frame corresponds to
\[
dz=\frac h{2\pi i}\frac{dq_h}{q_h},
\]
a local nonzero frame of \(\mathcal K(C)\). Consequently
\[
\mathcal L^2\simeq\mathcal K(C),\qquad
\deg\mathcal L=g-1+\frac c2.
\tag{9.2}
\]
This also proves that \(c\) is even. The genus formula, with \(e_2=e_3=0\), gives
\[
g-1+\frac c2=\frac d{12}>0.
\tag{9.3}
\]

Since there are no elliptic points or irregular cusps, the same local frames identify
\[
M_k(\Gamma_1(N))=H^0(X,\mathcal L^k),\qquad
S_k(\Gamma_1(N))=H^0(X,\mathcal L^k(-C)).
\tag{9.4}
\]
For cusp forms the dual correction bundle in Riemann–Roch is
\[
\mathcal K\otimes(\mathcal L^k(-C))^{-1}
\simeq\mathcal L^{2-k},
\]
by (9.2). For \(k\ge3\) it has negative degree by (9.3), so it has no sections. Thus
\[
\begin{aligned}
\dim S_k
&=\deg(\mathcal L^k(-C))+1-g\\
&=k(g-1+c/2)-c+1-g\\
&=(k-1)(g-1)+(k/2-1)c.
\end{aligned}
\]
For modular forms the dual correction bundle is
\(\mathcal L^{2-k}(-C)\), also of negative degree. Hence
\[
\dim M_k=k(g-1+c/2)+1-g
=(k-1)(g-1)+kc/2.
\]
This proves both formulas, including the absence of an unaccounted duality term.

As examples, \(\Gamma_1(5)\) has \(d=12,c=4,g=0\), so
\(\dim S_3=-2+2=0\) and \(\dim M_3=-2+6=4\).
For \(\Gamma_1(11)\), \(d=60,c=10,g=1\), so
\(\dim S_3=5\) and \(\dim M_3=15\).
The cusp counts follow respectively from
\(\frac12(4+4)=4\) and \(\frac12(10+10)=10\), using the formula proved in the congruence-subgroup lesson.

When \(k=1\), the dual of \(\mathcal L\) in (1.1) is
\(\mathcal K\mathcal L^{-1}\simeq\mathcal L(-C)\), whose sections are \(S_1\). Riemann–Roch now gives
\[
\dim M_1-\dim S_1
=\deg\mathcal L+1-g=c/2.
\]
It gives no automatic vanishing of \(S_1\). Retaining this term is exactly what prevents an incorrect universal weight-one dimension formula.

### Solution 5

The index is one and the weight is twenty-four, so (6.9) gives the inclusive endpoint \(B_0=2\). Put \(h=f-g\). Its first three coefficients are divisible by \(25\). Theorem 6.2 with \(p=5\) makes every coefficient divisible by \(5\), so \(h/5\) is an integer-coefficient modular form of the same weight. Its first three coefficients are still divisible by \(5\). Applying the theorem again makes every coefficient of \(h/5\) divisible by \(5\), proving the required congruence modulo \(25\).

The already constructed integral forms have
\[
F_1=q+O(q^3),\qquad F_2=q^2+O(q^3).
\]
Thus \(u=25F_1+F_2\) is a weight-twenty-four form with integer coefficients and
\[
\begin{aligned}
a_0(u)&=0,\\
a_1(u)&=25,\\
a_2(u)&=1.
\end{aligned}
\tag{9.5}
\]
Its coefficients through index one vanish modulo \(25\), while the next one does not. In particular the same example fails the shortened bound modulo \(5\). The valid bound is through index two, rather than stopping before it. This also follows directly from the triangular integral basis, whose first three coefficients are independent coordinates.

### Solution 6

The character \(\eta\) has \(\eta(2)=-1\), is even, and has conductor five. It is nontrivial modulo five, so cannot have conductor one. For \(\chi\), the computations \(2^{10}\equiv-1\) and \(2^4\equiv16\ne1\pmod{25}\) show that two has order twenty; the first excludes orders dividing ten, and the second excludes order four. Thus its prescribed value defines a character. The calculation \(\chi(16)=\zeta_5^4\ne1\) shows that it does not factor modulo five, so its conductor is twenty-five. Both characters have value one at \(-1\).

For \(\eta\), the conductor exponents are \(r=2,s=1\), giving \(E_\eta=5+1=6\). For \(\chi\), they are \(r=s=2\), giving \(E_\chi=2\). The denominator classes \(1,5,25\) have respectively one, four and one cusps. At denominator five the width is one and the parabolic lower-right entry is \(1+5a\), with \(a=1,2,3,4\). The character \(\eta\) is one on all four entries. Since
\[
1+5a\equiv6^a\equiv2^{8a}\pmod{25},
\]
their values under \(\chi\) are \(\zeta_5^{3a}\), all nontrivial. For the ordered cusps \(a/5\), \(a=1,2,3,4\), their cusp exponents are respectively \(3/5,1/5,4/5,2/5\). The first congruence follows by expanding \((1+5)^a\), and the second from \(2^8\equiv6\pmod{25}\). They sum to two, agreeing with \((c-c_\chi)/2=(6-2)/2\) in (5.12).

The two order-two roots \(7,18\) have \(\eta\)-values \(-1,-1\) and \(\chi\)-values \(1,1\); there are no order-three roots. The index is thirty and neither character has the weight-two trivial-character correction. Consequently
\[
\begin{gathered}
\begin{array}{c|cc}
&\dim S_2&\dim M_2\\ \hline
\eta&0&6\\
\chi&1&3
\end{array}\\[6pt]
\begin{array}{c|cc}
&\dim S_4&\dim M_4\\ \hline
\eta&4&10\\
\chi&7&9
\end{array}
\end{gathered}
\tag{9.6}
\]
For example, \(\dim S_2(25,\eta)=30/12-3+1/2=0\), whereas (5.18) gives one for \(\chi\). In weight four, \(\gamma_4(4)=1/4\), so the cusp dimensions are respectively \(90/12-3-1/2=4\) and \(90/12-1+1/2=7\). Adding the relevant \(E\) gives the modular dimensions. The different cusp monodromies and elliptic character values explain both differences.

## Appendix A. Compact curves, duality and Riemann–Roch

Let \(X\) be any compact connected Riemann surface without boundary, let \(L\) be any holomorphic line bundle, and write \(K=\Omega_X^1\). The proof below establishes duality, meromorphic-section existence and Riemann–Roch for every such \(X,L\). It first uses the analytic genus \(g_a=h^0(K)\); A.7 constructs finite polygon cells and invokes the earlier proof in lesson 03, Appendix A, Theorem S, to show that \(g_a\) equals the number of torus handles. The theorem is not restricted to divisor bundles, a special genus or a particular modular level.

The remaining elementary foundations are completeness of \(\mathbb R,\mathbb C\), compactness, real integration and its change-of-variables and convergence properties, weak derivatives, and Hilbert-space completion. Exact earlier programme proofs of that framework still require verification. The specific singular-kernel interchange is proved in A.3 by grid sums and explicit errors; general measurable Fubini is not used for it. The Fourier compactness, elliptic estimates, closed range, local solvability, finite-dimensionality, point-addition sequence and duality are proved below. Cauchy, Taylor series, the identity theorem and local inverses are lesson 01, Lemma 0.2 and its consequences; Laurent expansions are lesson 04, Lemma 0.1. Neither Riemann–Roch, algebraization, a general Fredholm theorem nor a sheaf-duality theorem is assumed.

### A.1. Cutoffs, integration, and the Fourier estimates

Choose finitely many coordinate disks on \(X\), together with smaller disks whose interiors still cover \(X\). This follows by first choosing a pair of concentric disks at each point and then taking a finite subcover of the smaller ones. A smooth bump supported in an outer disk and positive on its smaller disk can be made from \(\eta(t)=e^{-1/t}\) for \(t>0\), zero for \(t\le0\). Divide the finitely many bumps by their positive sum. We obtain smooth functions \(\rho_i\) with compact support in their disks and \(\sum_i\rho_i=1\).

A Hermitian metric on \(L\) is obtained by taking the weighted sum, with these \(\rho_i\), of positive fiber norms in local frames. Similarly, the weighted sum of the chart metrics \(|dz_i|^2\) is a smooth conformal metric on \(X\): holomorphic changes of coordinate multiply each such expression by a positive function. On each relatively compact chart, these metrics and their inverses have bounded positive coefficients.

We will use the following integration fact. For a smooth one-form \(\nu\) on a compact oriented surface with smooth boundary,
\[
 \int_X d\nu=\int_{\partial X}\nu.
 \tag{R1}
\]
Here is the reduction to the real foundations, rather than an imported surface theorem. Multiply by the finite partition of unity. Since \(\sum d\rho_i=0\),
\(\sum d(\rho_i\nu)=d\nu\). Each term has support in one coordinate chart. For a rectangle the formula is exactly the fundamental theorem of calculus applied to the coefficients of \(\nu=A\,dx+B\,dy\), followed by Fubini. Subdivision cancels interior sides. Smooth boundary arcs follow by approximation with inscribed coordinate polygons and change of variables; continuity of the coefficients and their first derivatives makes both integrals converge. Adding the chart formulas gives (R1). In particular the integral of an exact two-form on closed \(X\) is zero. This uses the stated real integration foundations, not a compact-curve or genus theorem.

For functions supported inside a coordinate rectangle, extend by zero and regard the result as periodic on a larger rectangle. The exponential functions form a complete orthogonal system in its \(L^2\) space. To see completeness directly, the period-one Fejér kernels
\[
 F_N(t)=N^{-1}\left|\sum_{j=0}^{N-1}e^{2\pi ijt}\right|^2
\]
are nonnegative, have integral one, and have mass tending to zero outside every fixed neighborhood of zero. Uniform continuity proves that their convolutions converge uniformly to continuous periodic functions. Step functions, with their finitely many discontinuities smoothed on intervals of arbitrarily small total length, show that continuous functions are dense in \(L^2\). Products of the kernels give the assertion on a rectangle. Orthogonal projection onto the finite Fourier spans then gives Parseval's equality. Integration by parts identifies the Fourier coefficients of weak derivatives.

Throughout these Fourier estimates, \(s\in\mathbb Z_{\ge0}\). If \(v\) has Fourier coefficients \(\widehat v(m,n)\), define its nonnegative integer Sobolev norm by
\[
 \|v\|_{W^s}^2=\sum_{m,n}(1+m^2+n^2)^s|\widehat v(m,n)|^2.
\]
Rescaling the rectangle changes these norms by fixed positive comparison constants. The multiplier of
\(\partial_{\bar z}=(\partial_x+i\partial_y)/2\) has squared modulus
\(\pi^2(m^2/a^2+n^2/b^2)\) on a rectangle of side periods \(a,b\). Hence
\[
 \begin{gathered}
 \|v\|_{W^{s+1}}\\
 \le C_s\bigl(\|\partial_{\bar z}v\|_{W^s}+\|v\|_{W^s}\bigr).
 \end{gathered}
 \tag{R2}
\]
The identical estimate holds with \(\partial_z\). The zero Fourier coefficient explains the second term. Formula (R2) also holds for weak derivatives: it is an inequality between the displayed coefficient sums, so follows first for finite sums and then by completion. Multiplication by a fixed smooth cutoff is bounded on every such \(W^s\), by the finite Leibniz rule and Parseval. No negative-order Sobolev assertion is needed here.

A bounded set in \(W^1\) has Fourier tail \(\sum_{m^2+n^2>A^2}|\widehat v(m,n)|^2\le C/A^2\). Extract a convergent subsequence in each finite set of coefficients and use this tail bound. It converges in \(L^2\). A finite coordinate partition therefore proves compactness of
\[
 W^1(X,L)\longrightarrow L^2(X,L).
 \tag{R3}
\]
The same statement holds for bundle-valued one-forms. These global spaces are the completions in the coordinate norms just constructed; changing frames or partitions gives equivalent norms by the product rule and bounded smooth transition functions. Limits in overlapping coordinates agree because equality there is preserved in \(L^2\). This verifies completeness of the global space from the local Hilbert completions.

The completed \(W^1\) space injects into \(L^2\). Indeed, if a \(W^1\)-Cauchy sequence has zero \(L^2\) limit, each localized Fourier coefficient tends to zero. Its weighted coefficient vectors are Cauchy in the displayed square-sum norm, so their limit has every coordinate zero and is the zero vector. Thus each localized \(W^1\) norm tends to zero, and the finite partition gives zero global norm. This proves injectivity, rather than identifying completion elements merely by name. The Fourier multiplier identities also pass to the limit against smooth test functions; the resulting first derivatives are therefore weak derivatives of the same \(L^2\) limit.

The Fourier proof also supplies regularity. If \(u\in L^2_{\mathrm{loc}}\) and \(\partial_{\bar z}u\) is smooth in distributions, multiply by a cutoff. Its derivative is in \(L^2\), so (R2) gives one weak derivative. Repeating with cutoffs supported successively farther inside the disk gives every nonnegative integer Sobolev order. For a derivative of order \(r\), Cauchy–Schwarz on its Fourier series gives absolute uniform convergence whenever the available Sobolev order exceeds \(r+1\):
\(\sum_{m,n}(1+m^2+n^2)^{-q}<\infty\) for \(q>1\), by counting square shells. Thus \(u\) is smooth. The same proof works for \(\partial_z\), and for smooth nonvanishing multiples of these operators after multiplying the unknown by the corresponding smooth factor.

### A.2. The closed-range statement for a line bundle

Let
\[
 D=\bar\partial_L:W^1(X,L)\longrightarrow L^2(X,L\otimes\overline K).
\]
In a holomorphic frame \(e\), it is simply
\(D(f e)=f_{\bar z}\,d\bar z\,e\). By (R2), cutoffs and equivalence of the metrics on each chart,
\[
 \|u\|_{W^1}\le C(\|Du\|_2+\|u\|_2).
 \tag{R4}
\]
The cutoff commutator is multiplication by \(\partial_{\bar z}\rho_i\), a bounded zeroth-order term. This proves the global estimate for smooth sections and then for the completed domain.

The kernel consists of smooth holomorphic sections, by the regularity argument in A.1. It is finite dimensional. Otherwise an infinite orthonormal sequence in its \(L^2\) kernel would be bounded in \(W^1\) by (R4), and (R3) would give an \(L^2\)-convergent subsequence, contradicting the distance \(\sqrt2\) between different members.

On the \(L^2\)-orthogonal complement of this kernel,
\[
 \|u\|_{W^1}\le C'\|Du\|_2.
 \tag{R5}
\]
Indeed, if the weaker \(\|u\|_2\le C'\|Du\|_2\) failed, choose orthogonal sections with \(\|u_j\|_2=1\) and \(Du_j\to0\). Estimate (R4) and compactness give an \(L^2\)-convergent subsequence. Its limit has norm one, is orthogonal to the kernel, and satisfies \(Du=0\) in distributions, a contradiction. Combining that weaker estimate with (R4) proves (R5).

It follows that the range of \(D\) is closed. For a sequence \(Du_j\) converging in \(L^2\), subtract the finite-dimensional kernel projection from each \(u_j\). Estimate (R5) makes the resulting sections Cauchy in \(W^1\), and their limit maps to the specified \(L^2\) limit.

For clarity, the Hilbert orthogonal decomposition used here can be obtained without a Fredholm theorem. For a closed linear subspace \(V\) and a vector \(x\), choose \(v_j\in V\) with \(\|x-v_j\|^2\) approaching its infimum. The parallelogram identity makes \(v_j\) Cauchy. Its limit \(v\in V\) minimizes the norm. Variation in real and imaginary multiples of every vector of \(V\) gives \(x-v\perp V\). Thus
\[
 \begin{gathered}
 L^2(X,L\otimes\overline K)\\
 =\operatorname{ran}D\oplus(\operatorname{ran}D)^\perp.
 \end{gathered}
 \tag{R6}
\]

Compute the formal adjoint. Write the conformal metric as \(ds^2=\lambda|dz|^2\), and the Hermitian norm of \(e\) as \(h=|e|^2\). With \(|d\bar z|^2=2/\lambda\), the section and form norms are respectively
\[
 \begin{gathered}
 \int \lambda h|f|^2dxdy,\\
 \int 2h|a|^2dxdy\\
 \text{for }\alpha=a\,d\bar z\,e.
 \end{gathered}
\]
Integration by parts against a compactly supported test section gives
\[
 D^*\alpha=-\frac{2}{\lambda h}\partial_z(h a)\,e.
 \tag{R7}
\]
Consequently (R2) proves the analogue of (R4) for \(D^*\). Its weak kernel is smooth by the regularity proof applied to \(h a\), and finite dimensional by (R3). The perpendicular space in (R6) is exactly this weak kernel: perpendicularity says \(\langle D\phi,\alpha\rangle=0\) for every smooth test section, which is the distribution equation \(D^*\alpha=0\).

If a smooth \(\alpha\) is written by (R6) as \(Du+\eta\), then \(\eta\) is smooth and \(Du=\alpha-\eta\) is smooth. The regularity proof makes \(u\) smooth. We have therefore proved the smooth quotient decomposition
\[
 \frac{A^{0,1}(X,L)}{D A^{0,0}(X,L)}
 \simeq\ker D^*,
 \tag{R8}
\]
including its finite dimensionality. This is the exact closed-range and regularity input needed below; no unproved general elliptic theorem has been substituted for it.

### A.3. Local solvability and the meaning of \(H^1\)

The local equation \(\partial_{\bar z}u=b\) is solvable for every smooth \(b\) on a smaller disk. Multiply \(b\) by a cutoff supported in the original disk and put
\[
 u(z)=\frac1\pi\int_{\mathbb C}\frac{b(\zeta)}{z-\zeta}\,dA(\zeta).
 \tag{R9}
\]
Here and in the next paragraphs the singular area integrals are defined by limits after deleting a centered square of side \(2\delta\) around the singularity, with \(\delta\downarrow0\). We prove their existence and the precise interchange needed in (R9) from compact Riemann sums.

First, planar translation preserves these integrals without a general change-of-variables theorem. For a continuous function on a rectangle, translate every cell and tag of a grid partition by the same vector. Corresponding Riemann sums have exactly the same values and cell areas. Passing to their limits proves the translation identity. The same argument applies to a rectangular region with finitely many rectangular holes, by subdivision. It therefore applies to the nonsingular truncated integrals used below.

Put \(Q_r=\{w:|\operatorname{Re}w|\le r,\ |\operatorname{Im}w|\le r\}\). On the square shell \(Q_{2^{-j}r}\setminus\operatorname{int}Q_{2^{-j-1}r}\), one has \(|w|\ge2^{-j-1}r\); its area is at most \(4(2^{-j}r)^2\). Thus the integral of \(1/|w|\) over that shell is at most \(8r2^{-j}\). For finite unions of shells the bounds add. The resulting increasing nonnegative truncated integrals are bounded, so real completeness gives their limit. Summing the geometric bound gives
\[
 \int_{Q_r}\frac{dA(w)}{|w|}\le16r.
 \tag{R9a}
\]
The same argument starting with \(Q_\delta\) bounds its singular tail by \(16\delta\). Consequently arbitrary square deletions have the same limit as the dyadic deletions. An omitted Euclidean disk of radius \(r\) lies inside \(Q_r\) and has the same upper bound; no polar area substitution is used. Translation of the nonsingular truncations gives these bounds about any center, uniformly in that center. For an inner \(\zeta\)-integral use the translation \(w=\zeta-z\) and the equality \(|z-\zeta|=|w|\); for an inner \(z\)-integral use \(w=z-\zeta\). Thus the estimates require only translations, not a reflection or a general planar substitution.

Set \(K(w)=1/(\pi w)\). Choose a continuous nondecreasing function \(\vartheta:[0,\infty)\to[0,1]\), zero on \([0,1/2]\) and one on \([1,\infty)\), for example linear between those intervals. Let
\(K_\epsilon(w)=\vartheta(|w|/\epsilon)K(w)\), extended by zero at \(w=0\). This is continuous everywhere. For a bounded continuous coefficient \(c\) on a support rectangle, with \(|c|\le M\), two square-deleted integrals with radii \(\delta,\delta'\) differ by at most \(16M\max(\delta,\delta')/\pi\). Thus these complex integrals are Cauchy and have a limit; their absolute-value integrals are increasing and bounded by (R9a) on a sufficiently large translated square, so the limit is absolutely finite. Replacing \(K\) by \(K_\epsilon\) in any such inner area integral changes that integral by at most \(16M\epsilon/\pi\), because the difference is supported in \(|w|<\epsilon\). This follows first on nonsingular truncations from (R9a), then by their limit.

For the compactly supported smooth \(b\) in (R9), write
\(u_\epsilon(z)=\int b(\zeta)K_\epsilon(z-\zeta)dA(\zeta)\).
On every compact set of \(z\)'s the continuous integrand is uniformly continuous on its product with a support rectangle for \(b\), so \(u_\epsilon\) is continuous there by the compact uniform error bound for Riemann integrals. The preceding tail bound shows that the singular integral defining \(u\) exists absolutely and
\(\sup_z|u(z)-u_\epsilon(z)|\le16\|b\|_\infty\epsilon/\pi\).
To bound \(u\) on a fixed compact set, choose \(R\) so large that all differences \(z-\zeta\) in that set and the support of \(b\) lie in \(Q_R\); (R9a) gives \(|u(z)|\le16R\|b\|_\infty/\pi\). Thus \(u\) is continuous and locally bounded, hence belongs to the local \(L^2\) completion used in A.1.

We next justify the double integral. Let \(\psi\) be any continuous compactly supported function, including a test derivative \(\partial_{\bar z}\phi\), and choose rectangles \(Z,B\) containing the supports of \(\psi,b\). For each \(\epsilon>0\),
\(F_\epsilon(z,\zeta)=\psi(z)b(\zeta)K_\epsilon(z-\zeta)\)
is continuous on \(Z\times B\). Both iterated plane integrals are limits of the same finite double grid sums
\(\sum_{j,k}F_\epsilon(z_j,\zeta_k)\Delta A_j\Delta A_k\): uniform continuity makes the error at most the product of the rectangle areas times the modulus of continuity at the grid diameter. Finite sums commute, so these two continuous iterated integrals agree. Their inner integrals are continuous in the outer variable by the same uniform continuity bound.

Write \(M=\|\psi\|_\infty\) and \(C=\|b\|_\infty\). In the order with outer \(z\)-integration, the absolute omitted contribution is at most
\(16CM\epsilon\operatorname{area}(Z)/\pi\); in the other order it is at most
\(16CM\epsilon\operatorname{area}(B)/\pi\). These bounds are independent of the retained outer variable. They show that the singular inner integrals, and also their absolute-value counterparts, exist and are uniform limits of continuous truncated integrals on the outer rectangles. The outer integrals therefore exist and are absolutely finite. Passing both orders through these explicit error bounds to the same limit of the continuous double integrals proves the following identity. Put
\[
 V(\zeta)=\int\psi(z)K(z-\zeta)dA(z).
\]
Using \(u(z)=\int b(\zeta)K(z-\zeta)dA(\zeta)\), the equality of the two integration orders is
\[
 \begin{gathered}
 \int \psi(z)u(z)dA(z)\\
 =\int b(\zeta)V(\zeta)dA(\zeta).
 \end{gathered}
 \tag{R9b}
\]
This is the specific singular-kernel interchange required here. It imports neither a measurable Fubini theorem nor dominated convergence.

In distributions, \(\partial_{\bar z}K=\delta_0\). To verify the identity, integrate against a smooth compactly supported test function \(\phi\), delete a circle of radius \(\epsilon\), and apply the planar form of (R1). The outer boundary contributes zero; the inner boundary has negative orientation. Its integral of \(\phi(z)/(\pi z)\,dz\) tends to \(-2i\phi(0)\). On the punctured region,
\(d[(\phi/(\pi z))dz]=2i(\pi z)^{-1}\partial_{\bar z}\phi\,dA\).
The omitted area integral tends to zero by (R9a), so integrating and using that negative inner-boundary sign gives
\(-\int K(z)\partial_{\bar z}\phi(z)dA(z)=\phi(0)\).
Apply (R9b) with \(\psi=\partial_{\bar z}\phi\), and use the translation identity on the inner test integral. We obtain
\[
 \begin{gathered}
 -\int u(z)\partial_{\bar z}\phi(z)dA(z)\\
 =\int b(\zeta)\phi(\zeta)dA(\zeta).
 \end{gathered}
 \tag{R9c}
\]
Thus (R9) solves the equation in distributions. A.1 makes this solution smooth on the smaller disk. A local holomorphic frame gives the same local solvability for \(D\). The real calculus, planar Stokes and weak/Hilbert foundations explicitly retained in the opening paragraphs of this appendix are still required; the particular singular-kernel interchange is now proved above.

We can now identify (R8) with holomorphic cohomology explicitly. Here \(H^1(X,L)\) means degree-one analytic holomorphic Čech cohomology in the direct limit over open-cover refinements. We do not assert that a fixed arbitrary cover computes it. Compactness permits finite covers; local solvability below is obtained on refined coordinate disks whose closures lie in larger trivializing disks. A holomorphic Čech one-cocycle consists of sections \(g_{ij}\) on overlaps, with \(g_{ij}+g_{jk}=g_{ik}\). For a smooth partition subordinate to the cover, put
\[
 u_i=\sum_j\rho_j g_{ij}.
\]
Terms extend smoothly by zero off their overlaps, since the supports of \(\rho_j\) lie inside \(U_j\). The cocycle identity gives \(u_i-u_j=g_{ij}\). The forms \(Du_i\) therefore glue to a global \(\alpha\). Changing a cocycle by a holomorphic coboundary changes \(\alpha\) by an exact smooth form; changing the partition has the same effect, since the differences of the resulting \(u_i\)'s glue to a global smooth section.

Conversely, refine to those coordinate disks and solve \(Dv_i=\alpha\) there by (R9), using a cutoff in each larger disk. Then \(v_i-v_j\) are holomorphic and form a cocycle. If \(\alpha=Du\) globally, the cocycle is the coboundary of the holomorphic sections \(v_i-u\). Starting with a cocycle, the first construction's \(u_i\) are themselves local primitives, so recovery gives the original cocycle on every common refinement. Starting instead with \(\alpha\) and the primitives \(v_i\), the first construction gives
\(u_i=\sum_j\rho_j(v_i-v_j)=v_i-W\), where \(W=\sum_j\rho_jv_j\) is a global smooth section. It therefore recovers \(Du_i=\alpha-DW\), the same quotient class. Changes of local primitives differ by holomorphic local sections. These two constructions are inverse in the direct limit over refinements. Thus the degree-one analytic holomorphic Čech group over refinements is exactly
\[
 \begin{gathered}
 H^1(X,L)\\
 =A^{0,1}(X,L)/D A^{0,0}(X,L).
 \end{gathered}
 \tag{R10}
\]
For the smooth Čech complexes, the exact sequence of sheaves
\(0\to\mathcal O(L)\to A^{0,0}(L)\xrightarrow D A^{0,1}(L)\to0\)
has the local exactness just proved, and the smooth sheaves have the explicit Čech contraction \((hc)_{i_0\ldots i_{q-1}}=\sum_j\rho_jc_{j i_0\ldots i_{q-1}}\), for which expansion gives \(\delta h+h\delta=1\). There are no higher-degree Dolbeault forms on a complex curve. The concrete degree-one identification above therefore needs no sheaf-duality theorem. A comparison with an independently defined derived-functor cohomology, or with algebraic cohomology, is outside the present proof unless its comparison theorem is separately written or verified earlier.

### A.4. Duality from the adjoint, with its bundle transitions checked

For a holomorphic section \(\omega\) of \(K\otimes L^{-1}\), set
\[
 B([\alpha],\omega)=\int_X\omega\wedge\alpha.
 \tag{R11}
\]
If \(\alpha=Ds\), the integrand is the negative exterior derivative of \(s\omega\). Formula (R1) therefore makes its integral zero. Thus the pairing is well defined on (R10).

An adjoint-kernel form \(\alpha=a\,d\bar z\,e\) satisfies \(\partial_z(h a)=0\). Consequently
\[
 J\alpha=h\overline a\,dz\,e^{-1}
 \tag{R12}
\]
is holomorphic. This is a global, conjugate-linear map. Indeed, under \(\zeta=\zeta(z)\) and \(e'=t e\),
\[
 \begin{gathered}
 a'=a/(t\overline{\zeta_z}),\\
 h'=|t|^2h.
 \end{gathered}
\]
so
\(h'\overline{a'}\,d\zeta\,(e')^{-1}=h\overline a\,dz\,e^{-1}\).
Conversely any holomorphic \(w\,dz\,e^{-1}\) gives an adjoint-kernel form with \(a=\overline w/h\). The transition calculation also proves that this inverse is global. Thus (R12) is a conjugate-linear bijection
\(\ker D^*\to H^0(X,K\otimes L^{-1})\).

Moreover,
\[
 \begin{aligned}
 B([\alpha],J\alpha)
 &=\int h|a|^2\,dz\wedge d\bar z\\
 &=-2i\int h|a|^2dxdy\\
 &=-i\|\alpha\|_2^2.
 \end{aligned}
 \tag{R13}
\]
It is nonzero for every nonzero \(\alpha\in\ker D^*\). Equations (R8), (R12) and (R13), together with finite dimensionality, prove that (R11) is a perfect complex bilinear pairing. They prove the complex-linear duality in Section 1 for every holomorphic line bundle. This is not limited to the trivial bundle or to bundles already known to come from divisors.

### A.5. Adding one point: an exact sequence with every map constructed

Fix \(P\in X\). In a local coordinate \(z(P)=0\) and holomorphic frame \(e\), the bundle \(L(P)\) has frame \(e/z\). Its sections are meromorphic \(L\)-sections with at most a simple pole at \(P\). Recording the coefficient of \(e/z\) gives a one-dimensional principal-part space \(C_P\); choosing \(z,e\) identifies it with \(\mathbb C\). Such a choice affects maps by a nonzero scalar and does not affect their exactness.

Choose a smooth cutoff \(\chi\), equal to one near \(P\) and supported in this chart. The derivative of \(\chi b e/z\) is supported away from \(P\), and is a global smooth \(L\)-valued \((0,1)\)-form. Two choices of cutoff give a difference supported away from \(P\), hence the derivative of a smooth global \(L\)-section. A change of local frame or coordinate preserves the principal-part line; expressions for the same principal part differ by a holomorphic local \(L\)-section, whose cutoff likewise contributes only an exact global form. Thus the following map is independent of those choices:
\[
 \delta(b)=[D(\chi b e/z)]\in H^1(X,L).
\]
We claim the following sequence is exact, including its final surjection:
\[
 \begin{gathered}
 0\to H^0(L)\to H^0(L(P)),\\
 H^0(L(P))\xrightarrow{\mathrm{pp}}C_P\\
 \xrightarrow\delta H^1(L),\\
 H^1(L)\to H^1(L(P))\to0.
 \end{gathered}
 \tag{R14}
\]

The rows of (R14) are one sequence. Successive rows overlap at the same \(H^0(L(P))\) and \(H^1(L)\); the middle row displays both maps at \(C_P\). At \(H^0(L(P))\), a zero principal part removes the pole and gives a section of \(L\). If \(s\) has principal part \(b e/z\), then \(s-\chi b e/z\) is globally smooth in \(L\) and has derivative \(-D(\chi b e/z)\). Hence \(\delta(b)=0\). Conversely, if \(D(\chi b e/z)=Du\) for a smooth global \(L\)-section, then \(s=\chi b e/z-u\) is holomorphic as a section of \(L(P)\) and has principal part \(b\). This proves exactness at \(C_P\).

For exactness at \(H^1(L)\), suppose a smooth \(L\)-form \(\alpha\) becomes \(Dv\) in \(L(P)\). Solve \(Dw=\alpha\) in a local holomorphic \(L\)-frame near \(P\), by (R9). Then \(v-w\) is holomorphic in the frame \(e/z\), so its meromorphic \(L\)-expression is \(b e/z\) plus a holomorphic \(L\)-section. It follows that \(v-\chi b e/z\) is a smooth global \(L\)-section. Therefore \([\alpha]=\delta(b)\). The reverse inclusion follows directly because \(\chi b e/z\) is a smooth section of \(L(P)\), making its derivative exact there.

Finally, given any smooth \(L(P)\)-form \(\eta\), solve \(Dv=\eta\) near \(P\) in its local holomorphic frame. Subtract \(D(\chi v)\). The result vanishes near \(P\), and so is the image of a smooth global \(L\)-form. This proves the final surjection. All groups in (R14) are finite dimensional by A.2–A.4.

Define \(\chi(L)=h^0(L)-h^1(L)\). In a finite exact sequence, rank-nullity makes adjacent image dimensions cancel in its alternating sum. Applied to (R14), it gives
\[
 \chi(L(P))=\chi(L)+1.
 \tag{R15}
\]
Applying this statement to \(L(-P)\) gives the corresponding subtraction formula. Thus for every integral divisor \(D\),
\(\chi(L(D))=\chi(L)+\sum_P D(P)\).

This point-addition argument does not assume Riemann–Roch, the existence of a meromorphic section of \(L\), an algebraic model, or an unproved long exact sequence. The particular long sequence needed was constructed above.

### A.6. Meromorphic sections, degree, and analytic Riemann–Roch

Every \(L\) has a nonzero meromorphic section. Choose an integer \(n\) so large that \(\chi(L)+n>0\). By (R15),
\[
 h^0(L(nP))=\chi(L)+n+h^1(L(nP))>0.
\]
A nonzero holomorphic section of \(L(nP)\) is precisely a meromorphic section of \(L\) with a possible pole of order at most \(n\) at \(P\). This proves existence without using the desired Riemann–Roch formula as a premise.

Its divisor \(D=(s)\) has finite support. Local Taylor/Laurent expansions show that zeros and poles are isolated; a nonzero section cannot vanish on a disk by the identity theorem. Compactness then gives finiteness. Locally write \(s=z^{D(P)}u e\), where \(u\) is nonvanishing and holomorphic. Multiplication by \(s\) identifies \(\mathcal O(D)\) with \(L\), since the local frame \(z^{-D(P)}\) maps to \(u e\).

The total order is independent of the meromorphic section. If \(s'\) is another, its ratio \(f=s'/s\) is a meromorphic function. On the complement of small disks about its zeros and poles, the one-form \(df/f\) is closed. Formula (R1) makes the sum of its boundary integrals zero. At a point with \(f=z^r u\), its positively oriented small-circle integral is \(2\pi i r\), because \(u'/u\) is holomorphic. Thus \(\sum_P\operatorname{ord}_P f=0\). This proves that
\[
 \deg L=\sum_P\operatorname{ord}_P s
\]
is well defined, and that degrees add under tensor products. It also proves that a negative-degree line bundle has no nonzero holomorphic section.

A holomorphic function on connected compact \(X\) is constant: its modulus attains a maximum, and the local maximum argument of lesson 01 makes it constant on a disk and then everywhere. Hence \(h^0(\mathcal O)=1\). By A.4, \(h^1(\mathcal O)=h^0(K)\). Put \(g_a=h^0(K)\). The divisor representation and (R15) give
\[
 \chi(L)=\chi(\mathcal O)+\deg L=1-g_a+\deg L.
\]
Using the already proved duality, we obtain for every \(L\)
\[
 \begin{gathered}
 h^0(L)-h^0(K\otimes L^{-1})\\
 =\deg L+1-g_a.
 \end{gathered}
 \tag{R16}
\]
Apply it to \(L=K\). Duality gives \(h^1(K)=h^0(\mathcal O)=1\), so
\(g_a-1=\deg K+1-g_a\), and consequently
\[
 \deg K=2g_a-2.
 \tag{R17}
\]
All assertions in (R16)–(R17) and the duality hold for arbitrary compact connected complex curves and arbitrary holomorphic line bundles, relative to the real-analysis foundations stated in the opening paragraphs of this appendix. They have not yet used the topological genus or the finite-polygon surface theorem.

### A.7. The analytic and topological genera

The preceding argument also supplies a nonconstant meromorphic function on every \(X\). For \(n>g_a\), formula (R16) applied to \(\mathcal O(nP)\) gives \(h^0(\mathcal O(nP))\ge n+1-g_a>1\). Since constants form a one-dimensional subspace, there is a nonconstant \(f\) with its only possible pole at \(P\). Regard it as a holomorphic map \(f:X\to\mathbb P^1\), using \(1/f\) as the target coordinate at a pole.

The local power-series/branching proof of lesson 01 makes this map locally \(u\mapsto u^{r_Q}\). It is open. Its compact image is closed, so connectedness of the sphere makes it surjective. Every fiber is discrete and compact and therefore finite. There are finitely many critical points: the meromorphic differential \(df\) is nonzero by the identity theorem and has only finitely many zeros and poles; possible ramification at poles is read in \(1/f\). Thus the branch-value set is finite.

Away from those values the local inverses and compactness give a finite covering. More explicitly, take the finitely many points in one regular fiber and small inverse neighborhoods around them. A sequence of additional preimages of targets tending to that regular value would have a convergent subsequence in compact \(X\), producing an additional point in its fiber, a contradiction. These inverse neighborhoods therefore exhaust all preimages of a sufficiently small target disk. The number of sheets is locally constant; the sphere with finitely many points removed is path connected, so it is a fixed positive integer \(d\). Near any exceptional fiber, the same compactness argument and the local powers show
\[
 \sum_{Q\in f^{-1}(b)}r_Q=d.
 \tag{R18}
\]

Construct a finite polygonal decomposition of the sphere with every branch value as a vertex. This needs no general surface triangulation theorem. In a planar chart containing the finitely many marked points, draw all horizontal and vertical lines through their coordinates inside a sufficiently large rectangle. Their rectangular cells can be cut by diagonals into triangles. The exterior rectangle together with the point at infinity is a closed disk: if its radial boundary is \(r=R(\theta)\), the explicit map \(r e^{i\theta}\mapsto(R(\theta)/r)e^{i\theta}\), with infinity sent to zero, gives such a disk. Connect its center to its finitely many boundary vertices. This adds finitely many triangles. Subdivide if necessary so every marked point is a vertex.

Each open edge has \(d\) lifts, and each open triangular face has \(d\) lifts. To justify the second assertion, continue a local inverse along paths using its small inverse disks. Compactness prevents a missing endpoint. Two continuations along homotopic paths agree by subdividing the path homotopy into rectangles mapping inside these inverse disks and using uniqueness on each small rectangle. The triangle interior is simply connected, so each inverse branch is single valued there. The local maps \(u^{r_Q}\) attach the closures at the vertex fibers. This constructs a finite cell decomposition of \(X\), including possible identifications in its attaching boundaries.

If the sphere decomposition has \(V,E,F\) cells, its direct planar subdivision count is \(V-E+F=2\). Indeed, the starting rectangle boundary, its interior and its exterior disk have \(V=4,E=4,F=2\). Inserting a vertex in an edge increases \(V,E\) equally; inserting an edge that divides a face increases \(E,F\) equally. Building the grid and its diagonals by these operations preserves the count. In the exterior disk, inserting its center and the spokes to its \(k\) boundary vertices changes the count by \(1-k+(k-1)=0\). This proves the specific count without a general invariance theorem. The lifted edges and faces number \(dE,dF\). By (R18), the vertex count is \(dV-\sum_Q(r_Q-1)\). Hence this particular decomposition has Euler count
\[
 \chi_{\mathrm{cell}}(X)=2d-\sum_Q(r_Q-1).
 \tag{R19}
\]
No general Riemann–Hurwitz theorem has been cited as a proof of (R19).

Now compare with a differential. The sphere differential \(dt\) has order zero at finite points and order \(-2\) at infinity. Its pullback \(df\) has order \(r_Q-1\) over a finite value and order \(-r_Q-1\) over infinity. Using (R18) over infinity gives
\[
 \begin{aligned}
 \deg K&=\operatorname{deg}(df)\\
 &=-2d+\sum_Q(r_Q-1)\\
 &=-\chi_{\mathrm{cell}}(X).
 \end{aligned}
 \tag{R20}
\]
Combining (R17) and (R20) proves
\[
 \chi_{\mathrm{cell}}(X)=2-2g_a.
 \tag{R21}
\]
Apply lesson 03, Appendix A, Theorem S, to the finite polygonal cells just constructed. Their charts and local power maps give the oriented surface and disk-neighborhood hypotheses of that theorem. The same count is therefore \(2-2g_t\), where \(g_t\) counts torus handles. Equations (R17) and (R21) give \(g_a=g_t\), so (R16) is the full formula (1.1), with \(h^0(K)=g_t\) and \(\deg K=2g_t-2\). This is an equality of the pre-existing analytic and handle genera, not a definition of genus from the count.

For the modular curve of lesson 06, its already constructed modular-cover cells can be used instead of this new general map. The finite-coset degree formula remains independent of all the arguments here. The earlier finite-polygon theorem supplies the genus identification for either cell presentation, so the dimension formulas use (R16) with the same genus as the modular-cover calculation. The arithmetic model, GAGA, bad-prime and bounded-denominator gaps are separate and are not repaired by this analytic proof.

## What this lesson does not prove

The differential dictionary (Theorem 2.1) has a local chart proof. Theorem 3.1 now has a finite-norm proof using only the earlier level-one valence formula; it no longer relies on Riemann–Roch. The complex coefficient bound (Theorem 6.1), including its character-power extension, follows from that proof. Lemma 1.1 derives the canonical degree for this modular curve from the earlier modular covering and the explicit \(j\)-coordinate. The analytic foundations recorded in lessons 03–05 remain prerequisites for these local arguments.

Theorem 4.1, Theorem 5.1, the small-level-three odd-weight formula, Solution 4 and the level-four irregular calculation use (1.1) and/or \(h^0(\mathcal K)=g\). Appendix A now supplies the full arbitrary-line-bundle Riemann–Roch and duality arguments, meromorphic-section existence and the analytic/topological genus bridge. The real integration, weak-derivative and Hilbert foundations listed in its opening remain to be proved or bound to exact earlier programme proofs. The dimension computations inherit that remaining foundation requirement. All examples, exercises and solutions are retained.

Theorem 6.2 writes out the normalized norm argument for prime congruences, but it is conditional on Section 6.1's principal-level field structure, determinant-one action and bounded-denominator input. The free original Deligne–Rapoport scan supplies VII.3.8, VII.3.10–3.11 and VII.4.6; its geometric construction and GAGA foundations remain unproved here and lack verified earlier programme proof locators. Corollaries 6.3–6.4 inherit this gap. The number-field facts about extension primes, discrete valuation localizations, prime-ideal factorization, contraction of localized prime powers and comaximality also remain without verified earlier programme proofs. The norm argument does not assert integral slash stability at bad primes.

The earlier LG-MF proof dependencies are the cusp counts, widths, stabilizers and regularity in Congruence subgroups, cusps and elliptic points, Proposition 2.1, Theorems 2.2, 3.1 and 4.2 and Proposition 3.2; the quotient charts, covering and explicit genus count in Modular curves and their genus, Propositions 1.3, 2.2 and 3.2 and Theorem 3.3; and the valence formula, \(j\)-coordinate, discriminant product and integral triangular basis in The valence formula and the ring of modular forms of level one, Theorems 1.1, 3.1 and 4.1 and Solution 5. The slash law is lesson 04, Proposition 1.1. Every one of these lessons precedes lesson 06. The unresolved foundations named earlier in this section are not proved in this lesson.

## References

- **Deligne–Rapoport free original scan.** P. Deligne and M. Rapoport, *Les schémas de modules de courbes elliptiques*, VII.2.4, VII.3.8, VII.3.10–3.11 and VII.4.6 304–306 and 312. This complete original article is freely accessible in Deligne's IAS publication archive. [Free original scan](https://publications.ias.edu/sites/default/files/Number22.pdf).
- **Stein author PDF.** W. Stein, *Modular Forms: A Computational Approach*, freely distributed PDF on the author's website, Chapter 6, Propositions 6.1 and 6.6 and §6.3; §9.4, Theorem 9.18 and its norm argument. These locators refer to this accessible file. [Free author PDF](https://wstein.org/books/modform/stein-modform.pdf).
- **Best et al.** A. J. Best and collaborators, *Computing classical modular forms*, arXiv:2002.04717v4, §4.3 and §8.2; the consulted source is version four. [Paper](https://arxiv.org/abs/2002.04717v4).
- **McMullen.** C. McMullen, *Riemann Surfaces*, Harvard Math 213b course notes, 28 April 2026 version, Theorems 11.1–11.2, Corollaries 9.10–9.11 and Corollary 14.4. [Author's notes](https://people.math.harvard.edu/~ctm/papers/home/text/class/harvard/213b/course/course.pdf).
- **Stacks.** *The Stacks project*, [Tag 0BS6: Riemann–Roch](https://stacks.math.columbia.edu/tag/0BS6). The AI Integrated Stacks Project edition keeps this tag; its AI-proposed corrections and additions have not been reviewed by the official Stacks project maintainers.
- **Serre 1956.** J.-P. Serre, *Géométrie algébrique et géométrie analytique*, §3, no. 12, Theorems 1–3. [Original article](https://www.numdam.org/item/AIF_1956__6__1_0/).
- **Teleman 2003.** C. Teleman, *Riemann Surfaces*, Lecture 14, opening algebraization theorem. [Author's notes](https://math.berkeley.edu/~teleman/math/Riemann.pdf).
- **Voight open book.** J. Voight, *Quaternion Algebras*, freely distributed stable post-publication version 1.0.5 (10 January 2024), §40.3 and Exercise 5 of Chapter 40. [Author's stable free PDF](https://jvoight.github.io/quat-book-v1.0.5.pdf).

- **Lebl.** J. Lebl, *Guide to Cultivating Complex Analysis*, version 1.9, §§3.2–3.4 and 5.6. [Author's free text](https://www.jirka.org/ca/ca.pdf). The exact earlier complex proof inputs for Appendix A are lessons 01 and 04.
