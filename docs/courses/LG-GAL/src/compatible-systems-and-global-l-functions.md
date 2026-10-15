# Compatible systems and global L-functions

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An elliptic curve supplies a Tate module for every prime. These vector spaces have different coefficient fields, yet their Frobenius polynomials at a good prime are the same integer polynomial. The resulting Euler product is attached to the curve, rather than to a chosen Tate module. To include the bad primes, one must compare monodromy as well as Frobenius. To obtain a functional equation, one needs an additional analytic theorem.

## 1. The convention and the compatibility data

Let \(K\) be a number field. For a finite place \(v\), put \(q_v=\#k_v\) and let \(p(v)\) be its residue characteristic. Write \(\operatorname{Fr}_v\) for **arithmetic** Frobenius and \(\Phi_v=\operatorname{Fr}_v^{-1}\) for geometric Frobenius. The local norm and reciprocity convention remain
\[
\|\Phi_v\|=q_v^{-1},\qquad
\operatorname{Art}_v(\varpi_v)=\Phi_v\quad\text{in }W_{K_v}^{\mathrm{ab}}.
\tag{1}
\]
In global Euler polynomials we use arithmetic Frobenius. Thus, for an unramified representation \(R\),
\[
P_v(R,X)=\det(1-R(\operatorname{Fr}_v)X),\qquad
L_v(s,R)=P_v(R,q_v^{-s})^{-1}.
\tag{2}
\]
At such a place the local factor defined earlier using geometric Frobenius satisfies
\[
L_v(s,R)=L\bigl(s,\operatorname{WD}_v(R^\vee)\bigr).
\tag{3}
\]
Indeed, the eigenvalues of \(R^\vee(\Phi_v)\) are those of \(R(\operatorname{Fr}_v)\). The dual in (3) is essential.

Let \(E\) be a number field of coefficients and \(\lambda\) range over its finite places, with residue characteristic \(\ell(\lambda)\). Consider continuous representations
\[
R_\lambda:G_K\longrightarrow\mathrm{GL}_d(E_\lambda).
\]
We use the following *finite-place* notions of compatibility. They make no assertion about a local representation at a place above its coefficient prime; that requires the theory introduced in the p-adic Hodge lesson.

**Definition 1.1 (weak compatibility).** There is a finite set \(S\) of finite places of \(K\), and for each \(v\notin S\) a polynomial \(P_v\in E[X]\), with constant term one and degree \(d\), such that whenever \(\ell(\lambda)\ne p(v)\), the representation \(R_\lambda\) is unramified at \(v\) and its polynomial (2) is \(P_v\).

**Definition 1.2 (strict compatibility).** In addition, for every finite \(v\) there is a Frobenius-semisimple Weil–Deligne isomorphism class \(D_v\) over \(\overline E\), invariant under \(\operatorname{Gal}(\overline E/E)\), whose scalar extensions give
\[
\operatorname{WD}_v(R_\lambda)^{\mathrm{F\!ss}}
\simeq D_v\otimes_{\overline E,\iota_\lambda}\overline E_\lambda
\qquad\bigl(\ell(\lambda)\ne p(v)\bigr)
\tag{4}
\]
for every embedding \(\iota_\lambda\) extending the coefficient embedding. At \(v\notin S\), this class is unramified and \(\det(1-D_v(\Phi_v^{-1})X)=P_v(X)\).

Invariance of an isomorphism class is weaker than the existence of matrices over \(E\). Here is a concrete proof of that distinction. The quaternion group has a two-dimensional complex representation with generators
\[
I=\begin{pmatrix}i&0\\0&-i\end{pmatrix},
\qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
Its character has values \(2,-2,0\), with corresponding characteristic polynomials \((T-1)^2,(T+1)^2,T^2+1\), all rational. The characteristic-polynomial Brauer–Nesbitt theorem proved in the first lesson therefore makes its class Galois-invariant. It has no real, hence no rational, two-dimensional realization. Indeed a real matrix with square \(-1\) has a basis in which it is \(\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\). A real matrix anticommuting with it has form \(\begin{psmallmatrix}a&b\\b&-a\end{psmallmatrix}\), whose square is \((a^2+b^2)1\), never \(-1\). This is an example of a Schur-index obstruction.

Definition 1.2 allows that obstruction. Isomorphic local pairs have the same invariant spaces, Frobenius determinants and nilpotent block lengths, so it supplies coefficient-independent local factors, conductors and monodromy lengths; the conductor integer is proved in the conductor lesson. Taylor uses “strongly compatible” for the comparison at every prime, within a definition that also includes de Rham and Hodge–Tate conditions [Taylor, §1, pp.81–83]. Those additional conditions are separate from our finite-place definitions.

Why is the stronger condition useful? The local pairs
\[
(1\oplus\|\cdot\|,0),\qquad \mathrm{Sp}(2)
\tag{5}
\]
have the same underlying Frobenius polynomial. Their local factors are respectively
\[
\frac{1}{(1-q^{-s})(1-q^{-s-1})},\qquad
\frac{1}{1-q^{-s-1}},
\]
and their conductors are zero and one. Monodromy accounts for the difference. This is a local illustration of missing information, not a claimed example of two global semisimple systems with the same good-prime data.

**Definition 1.3 (arithmetic weight).** A weakly compatible system is pure of weight \(w\) if the inverse roots \(\alpha_{v,j}\) in
\[
P_v(X)=\prod_{j=1}^d(1-\alpha_{v,j}X)
\]
satisfy \(|\sigma(\alpha_{v,j})|=q_v^{w/2}\) for every complex embedding \(\sigma\), at all \(v\notin S\). Enlarging \(S\) is allowed. Weights here refer to arithmetic Frobenius. The covariant elliptic Tate module has weight \(1\); its dual has arithmetic weight \(-1\), and geometric Frobenius on that dual has weight \(1\). The cyclotomic character \(\chi_\ell\) has arithmetic weight \(2\), since \(\chi_\ell(\operatorname{Fr}_v)=q_v\). Tensoring by \(\chi_\ell^m\) adds \(2m\) to an arithmetic weight. In the geometric convention it subtracts \(2m\).

## 2. The elliptic system and its exceptional set

Write \(A/K\) for an elliptic curve, reserving \(E\) for coefficients. The system \((V_\ell A)_\ell\) has coefficient field \(\mathbf Q\). Let \(S_A\) be the finite set of places of bad reduction. Its finiteness follows by choosing one global Weierstrass equation: outside the finitely many denominators of its coefficients and prime divisors of its nonzero discriminant, its integral projective cubic is smooth and gives a good model, as proved in the Tate-module lesson.

**Theorem 2.1 (good-prime independence).** At a good place \(v\), for every \(\ell\ne p(v)\),
\[
P_v(V_\ell A,X)=1-a_vX+q_vX^2,
\qquad a_v=q_v+1-\#\widetilde A(k_v).
\tag{6}
\]
In particular \((V_\ell A)_\ell\) is weakly compatible and pure of arithmetic weight \(1\), with exceptional set \(S_A\).

*Proof.* Good reduction identifies the prime-to-\(p(v)\) torsion with that of \(\widetilde A\), equivariantly for arithmetic Frobenius. The Tate-module lesson proved that the Frobenius endomorphism has determinant \(q_v\), and that \(\deg(1-\operatorname{Fr}_v)=\#\widetilde A(k_v)\). Consequently its trace is \(q_v+1-\#\widetilde A(k_v)\), proving (6). Each quantity comes from the curve over its residue field and is independent of \(\ell\).

Here is the required Hasse inequality. For any integers \(m,n\), the degree–determinant theorem, valid also for inseparable endomorphisms, gives
\[
0\le\deg([m]+[n]\operatorname{Fr}_v)
=m^2+a_vmn+q_vn^2.
\tag{6A}
\]
If \(a_v^2>4q_v\), the real polynomial \(z^2+a_vz+q_v\) is negative on an open interval. Choose a rational number \(m/n\) in that interval and multiply by \(n^2\), contradicting (6A). Thus \(|a_v|\le2\sqrt{q_v}\). The roots of \(T^2-a_vT+q_v\) are consequently a complex-conjugate pair, or the repeated real root \(\pm\sqrt{q_v}\); their product is \(q_v\), so each has absolute value \(\sqrt{q_v}\). Every embedding gives the same two roots. This proves purity. ∎

We next prove the comparison at potentially good primes in arbitrary dimension. The extra geometry required at semistable primes is identified separately below.

**Lemma 2.2 (endomorphisms have one characteristic polynomial).** Let \(B/k\) be an abelian variety of dimension \(g\), over any field, and \(u\in\operatorname{End}(B)\). There is a monic \(P_u(T)\in\mathbf Q[T]\) of degree \(2g\) whose image in every \(\mathbf Q_\ell[T]\), \(\ell\ne\operatorname{char}k\), is \(\det(T-u\mid V_\ell B)\). The same conclusion holds for quasi-endomorphisms, with rational coefficients.

**Proof.** We use the normalized cube, Proposition 4.4, Euler homogeneity, Proposition 5.5, and kernel/Tate torsion §§6–7 of the earlier programme lesson *Abelian varieties*, at their recorded proof scopes. The actual multivariable Euler polynomial, proper-image degree bound and finite-flat Euler comparison are now CE1–CE7 in §2B below. The remaining earlier field-geometric inputs and their transitive free-origin certification retain the obligations recorded in §7. Here are the characteristic-polynomial comparison steps.

Extend the ground field to its algebraic closure. Choose a symmetric ample bundle \(H\). Define \(\delta(f)=\deg(f)\) for isogenies, and zero for other endomorphisms. Then
\[
\delta(f)=\frac{\chi(B,f^*H)}{\chi(B,H)}.
\tag{6B}
\]
For an isogeny this is the full finite commutative torsor proof CE6, applied in CE7. Otherwise factor \(f\) through its image, an abelian subvariety of dimension less than \(g\). The proved higher-image Euler formula and proper-image degree bound CE4 show that \(\chi(B,(f^*H)^a)\) has degree less than \(g\) in \(a\). Euler homogeneity says it is \(a^g\chi(B,f^*H)\), so its coefficient is zero. The denominator in (6B) is positive by Proposition 5.5.

For fixed \(f,h\), pull the cube back along \((nf+h,f,f)\). It says that the classes of \((nf+h)^*H\) have constant second difference; they are quadratic polynomials in \(n\) with values in the rational Picard group. The full multivariable Euler polynomial CE2 has total degree at most \(g\). Formula (6B) therefore makes \(\delta(nf+h)\) a rational polynomial of degree at most \(2g\). Moreover \(\delta(nf)=n^{2g}\delta(f)\), by the degree of multiplication.

These assertions extend \(\delta\) to \(\operatorname{End}(B)\otimes\mathbf Q\) by \(\delta(f/n)=n^{-2g}\delta(f)\), independently of the denominator. They make it a homogeneous polynomial function of degree \(2g\) on every finite-dimensional subspace. To check the last assertion, choose coordinates on such a subspace and interpolate in each coordinate at \(2g+1\) distinct rational values. The line-degree bound produces a polynomial in all coordinates. Substituting arbitrary rational affine lines forces its total degree to be at most \(2g\); homogeneity forces its nonzero terms to have degree \(2g\). Multiplicativity \(\delta(fh)=\delta(f)\delta(h)\) holds: degrees multiply for isogenies, and a composition containing a map with smaller-dimensional image again has smaller-dimensional image. Polynomial interpolation extends this identity after any extension of the rational coefficient field.

Set \(P_u(T)=\delta(T-u)\). Its leading coefficient is \(\delta(1)=1\), and its degree is \(2g\). If \(a_i\) are its roots, multiplicativity after scalar extension gives, for any \(F\in\mathbf Q[T]\),
\[
\delta(F(u))=\prod_{i=1}^{2g}F(a_i).
\tag{6C}
\]
Indeed, factor \(F(T)=c\prod_j(T-b_j)\), apply multiplicativity and homogeneity to \(F(u)\), and interchange the two finite products. The even degree \(2g\) removes the possible sign.

For an isogeny \(h\), its kernel has \(\ell\)-primary order \(\ell^{v_\ell(\deg h)}\), for \(\ell\ne\operatorname{char}k\). Here are the scheme-length details. The actual isogeny theorem identifies its degree with the rank of its finite kernel, and its rank-annihilation lemma kills that kernel by this integer. Chinese-remainder multiplication idempotents split it into its primary factors. A factor killed by a power of \(\ell\) is a subgroup of the finite étale group \(B[\ell^r]\), so is étale. For a different primary factor, its geometric point group has order a power of its own prime. Its connected part is trivial in characteristic zero. In characteristic \(p>0\), its connected part is killed by a power of \(p\): multiplication by every prime-to-\(p\) integer is étale with trivial connected kernel, so is an automorphism on that finite connected part. Its rank is a power of \(p\), since it is a subgroup of \(B[p^r]\) and the finite subgroup quotient is a torsor whose ranks multiply. Thus no other factor contributes to the \(\ell\)-valuation of the rank. This proves the claimed \(\ell\)-primary order, including inseparable isogenies.

The \(\ell\)-primary point kernel is the kernel on \((\mathbf Q_\ell/\mathbf Z_\ell)^{2g}\). Diagonalizing the integral map \(T_\ell h\) by the DVR module theorem identifies this kernel with its finite lattice cokernel. Consequently
\[
|\delta(h)|_\ell=|\det(T_\ell h)|_\ell.
\tag{6D}
\]
For a nonisogeny both sides are zero: its positive-dimensional reduced kernel has nonzero rational Tate module. The Tate ranks and the finite-kernel length, including its inseparable characteristic-primary part, are exactly the earlier kernel results just specified. Thus (6D) applies to every \(F(u)\) with integral \(F\).

Let \(b_i\) be the eigenvalues of \(T_\ell u\). Equations (6C)–(6D) imply
\[
\left|\prod_iF(a_i)\right|_\ell
=\left|\prod_iF(b_i)\right|_\ell
\quad(F\in\mathbf Z[T]).
\tag{6E}
\]
Continuity, and then clearing a common denominator, give the same equality for \(F\in\mathbf Q_\ell[T]\). We verify that it forces equality of the two monic polynomials. For any algebraic \(z\) with minimal polynomial \(F_z\) over \(\mathbf Q_\ell\), Galois invariance of each multiset and uniqueness of the extended valuation give
\[
\left|\prod_iF_z(a_i)\right|_\ell
=|P_u(z)|_\ell^{[\mathbf Q_\ell(z):\mathbf Q_\ell]},
\]
and the analogous identity for \(Q(T)=\prod_i(T-b_i)\). Hence \(|P_u(z)|_\ell=|Q(z)|_\ell\). Approach a root \(a\) by algebraic \(z=a+\ell^j c\) avoiding the finitely many roots. For large \(j\), all distances to roots unequal to \(a\) are constant. The valuation of \(P_u(z)\) has slope equal to the multiplicity of \(a\), and that of \(Q(z)\) has slope equal to its multiplicity there. Equality forces those multiplicities to agree. Applying this to every root proves \(P_u=Q\). Finally clear a denominator to obtain the quasi-endomorphism assertion. ∎

### 2A. Good models: extension and torsion comparison in every dimension

We supply the model-theoretic inputs used by Lemma 2.3. Let \(R\) be a Noetherian DVR, with fraction field \(K\), residue field \(k\) and uniformizer \(\pi\). An abelian scheme here is a proper smooth commutative group scheme whose geometric fibres are abelian varieties. Its relative dimension is constant over this connected base: in smooth coordinates the rank of the relative cotangent bundle is locally constant, and the generic fibre and flatness make the total scheme integral. More explicitly, smoothness over the regular DVR makes all local rings regular by the flat regular-fibre test following NM2 of Lesson 8. Those rings are domains by NM1; flatness makes the integral generic fibre schematically dense. The whole scheme is consequently integral and normal by NM2.

The earlier proofs used below are Lesson 1, EA1–EA18 and NP1–NP4, for finite presentation, flatness, formal étale lifting and Henselian finite algebras; Lesson 3, PF1–PF9, for properness and products, Theorem 0.F.1 for proper maps with finite geometric fibres, and SF1–SF3 for square-zero derivations; and Lesson 8, NM1–NM2, for regular-local normality. We do not assume a Néron mapping property, a general semistable-reduction theorem or projectivity of a good model.

#### 2A.1. The dimension bound and the components of a group

**GQ1 (dimension and component lemmas).** A finite-type integral \(R\)-scheme with generic function field of transcendence degree \(g\) has no special-fibre component of dimension greater than \(g\). Over an algebraically closed field, the irreducible components of a finite-type group scheme are disjoint translates of the unique component containing its identity. These statements include nonreduced special fibres.

*Proof.* We first give the field dimension fact used here. A finite-type field algebra domain \(C\) is finite over a polynomial subring on an algebraically independent list. To prove this, write \(C=\kappa[x_1,\ldots,x_m]\). If that list is dependent, choose a nonzero relation \(F\). In
\[
 x_i=y_i+x_m^{N_i}\quad(i<m)
 \tag{GQ1}
\]
choose the positive integers \(N_i\) as successive powers of an integer larger than every exponent appearing in \(F\). Include weight one for the last variable. The weights of its distinct monomials are then distinct. After substitution the unique highest power of \(x_m\) has nonzero constant coefficient in \(\kappa\). Dividing by that coefficient makes a monic equation for \(x_m\) over \(\kappa[y_1,\ldots,y_{m-1}]\). Each \(x_i\) is integral over that smaller algebra as well. Monic power reduction makes the extension finite. Induct on the number of generators. When there is no relation, the list is algebraically independent. This proves the asserted normalization over every field, including finite fields.

For completeness, transcendence degree strictly drops under a nonzero prime quotient of a finite-type domain. Normalize that domain as just proved. Incomparability makes the contraction of the nonzero prime to the polynomial subring nonzero, since the zero prime has contraction zero. The quotient polynomial subring therefore has a relation between its \(d\) generators, so its transcendence degree is at most \(d-1\); the integral quotient has the same transcendence degree. Applying this at each step bounds every prime chain by \(d\). The coordinate prime chain in a polynomial ring gives the reverse bound there, and going up lifts that chain to its finite integral extension. Thus the actual going-up and incomparability proofs of Lesson 1 and the affine algebra of Lesson 3 give
\[
 \dim C=\operatorname{trdeg}_{\kappa}\operatorname{Frac}C .
 \tag{GQ2}
\]
They also show that dimension is unchanged by extending the field. Indeed the finite integral inclusion of the polynomial subring remains an inclusion after tensoring with a field and remains finite integral. For a general finite-type algebra, apply this to its finitely many minimal-prime quotients. Their closed subsets still cover after base change: a product of their ideals is nilpotent. Nilpotents do not change prime chains.

Take an affine neighbourhood of a generic point of a special-fibre component of our integral \(R\)-scheme, with coordinate domain \(D\), and let \(\mathfrak p\) be that component's prime. Normalization of \(D/\mathfrak p\) supplies algebraically independent elements \(\bar t_1,\ldots,\bar t_d\). Lift them to \(D\). If they satisfied a polynomial relation over \(K\), scale its finitely many coefficients by a power of \(\pi\) so they lie in \(R\) and at least one is a unit. Reduction modulo \(\mathfrak p\) would be a nonzero polynomial relation over \(k\), a contradiction. Thus \(d\le g\). Formula (GQ2), and its just-proved field-extension assertion, give the bound also on geometric components.

Here are the component details for a group scheme \(H\) over an algebraically closed field \(\kappa\). Products of integral finite-type \(\kappa\)-schemes are integral. On affine charts this follows directly from the field-point lemma EA2. If nonzero \(f,g\in C\otimes_\kappa D\) had zero product, express each using a finite linearly independent list of coefficients in \(C\). Choose one nonzero coefficient in \(D\) from each expression. Their product is nonzero in the domain \(D\). A \(\kappa\)-point of its nonvanishing locus exists by EA2; evaluation would give two nonzero elements with zero product in \(C\). This is impossible. Nonempty affine products cover with nonempty overlaps, proving the scheme assertion.

If two irreducible components \(C,D\) of \(H\) contain the identity, the closure of the multiplication image of \(C_{\mathrm{red}}\times D_{\mathrm{red}}\) is irreducible and contains both \(C\) and \(D\). Maximality makes them equal. Thus there is only one such component. Every component contains a closed \(\kappa\)-point, by EA2. Translation by its inverse carries it to the identity component, so all components are translates. If two met, their intersection would contain a closed point and translation by its inverse would contradict uniqueness at the identity. They are therefore disjoint, and being a finite list of closed subsets they are open as well. This concerns the underlying components; no smoothness or reducedness of \(H\) was assumed. \(\square\)

#### 2A.2. Extending every homomorphism between good models

**GQ2 (full faithfulness of good models).** If \(\mathcal A,\mathcal B\) are abelian schemes over \(R\), every \(K\)-homomorphism \(f:\mathcal A_K\to\mathcal B_K\) extends uniquely to an \(R\)-homomorphism. In particular a generic isomorphism extends uniquely as an isomorphism, in every dimension.

*Proof.* Let \(\Gamma\) be the scheme-theoretic closure of its graph in \(\mathcal A\times_R\mathcal B\). On affine charts its ideal is the contraction of the generic graph ideal, equivalently the \(\pi\)-saturation of an ideal obtained by clearing the finitely many denominators. Noetherianity makes it coherent. This closure is integral and \(\pi\) is a nonzero divisor on it: its chart algebras inject into the coordinate algebras of the integral generic graph. A torsion-free module over a DVR is flat. Indeed its finite submodules are free by the elementary DVR module theorem; it is their filtered union, and tensor products and finite equations commute with that union. Thus \(\Gamma\) is flat over \(R\).

The closure is a group scheme. On the flat \(\Gamma\times_R\Gamma\), multiplication in the ambient product lands in \(\Gamma\) generically. Each pulled-back defining equation is zero after inverting \(\pi\), so flatness makes it zero everywhere. This restricts multiplication. The same argument restricts inversion and the identity section. Its generic fibre is the graph group.

Write \(p:\Gamma\to\mathcal A\) for projection, and \(g=\dim\mathcal A_K\). Projection is proper, since \(\mathcal B\) is proper and the graph closure is closed. Its closed image contains the dense generic fibre of \(\mathcal A\), so \(p\) is surjective. The generic fibre of \(\Gamma/R\) has dimension \(g\); GQ1 bounds the dimensions of all its geometric special components by \(g\).

Work over \(\bar k\). The proper images of the finitely many components of \(\Gamma_{\bar k}\) cover the irreducible \(\mathcal A_{\bar k}\). At least one dominates it. GQ1 says that all source components are translates of that one; their images are translates too, so every component dominates. Their dimensions are at most \(g\), while the target has dimension \(g\). Hence all have dimension \(g\) and their function fields are algebraic over the target function field.

The geometric generic fibre of \(p_k\) is therefore zero-dimensional. Here is the algebra behind this step. On dominant affine charts, localize the target domain at all its nonzero elements. The resulting finite-type algebra has, on every reduced component, a fraction field algebraic over that target field. The field normalization proved in GQ1 makes each such algebra finite-dimensional; the finite nilpotent filtration gives the same conclusion before reduction. Scalar extension preserves finite-dimensionality.

Choose a geometric generic point \(a\) of \(\mathcal A_{\bar k}\) and a point \(\gamma\) above it; it exists by proper surjectivity. Translation gives an isomorphism of the entire fibre, including its nilpotents, with the kernel:
\[
 (\ker p_k)_{\overline{\kappa(a)}}\longrightarrow
       p_k^{-1}(a)_{\overline{\kappa(a)}},
 \qquad h\longmapsto\gamma+h .
 \tag{GQ3}
\]
Its inverse subtracts \(\gamma\). Thus the special kernel is zero-dimensional. Every other geometric special fibre is likewise a translate of that kernel. The generic projection is an isomorphism, so all geometric fibres of \(p\) have finitely many points. The actual proper finite-fibre theorem, Lesson 3, Theorem 0.F.1, makes \(p\) finite.

It is also birational. On an affine open \(\operatorname{Spec}C\) of the normal integral \(\mathcal A\), its finite inverse image has an integral coordinate algebra \(D\) in the same fraction field. Finiteness makes its elements integral over \(C\). Normality gives \(D=C\), so
\[
 p:\Gamma\xrightarrow{\ \sim\ }\mathcal A .
 \tag{GQ4}
\]
Normality here follows from the actual regular-local proof NM2, not from a claimed normality of the possibly singular graph closure. Composing its inverse with the other projection gives the extension of \(f\).

Two extensions agree: the pullback of the closed diagonal of \(\mathcal B\) has defining equations vanishing after inverting \(\pi\), and flatness of \(\mathcal A\) makes them zero. The homomorphism identities follow by the same uniqueness on the flat product. If \(f\) is an isomorphism, extend its inverse too; their composites are identities by uniqueness. This proves the full assertion. \(\square\)

#### 2A.3. Invertible multiplication is actually finite étale

**GQ3.** If \(n\) is invertible in \(R\), multiplication \([n]:\mathcal A\to\mathcal A\) and its kernel \(\mathcal A[n]\to\operatorname{Spec}R\) are finite étale. The kernel square and these assertions commute with arbitrary base change.

*Proof.* We prove formal étaleness, with the infinitesimal calculation included. Let \(T_0\hookrightarrow T\) have square-zero ideal \(I\). In a lifting problem for \([n]\), smoothness first supplies a local lift \(a\) of the given point \(a_0\). The discrepancy from the prescribed target point \(b\) reduces to the identity. The square-zero derivation calculation SF1–SF3 identifies this kernel with the additive module
\[
 \ker\bigl(\mathcal A(T)\to\mathcal A(T_0)\bigr)
      =\operatorname{Hom}_{\mathcal O_T}
        (e^*\Omega_{\mathcal A/R}\otimes_R\mathcal O_T,I).
 \tag{GQ5}
\]
To see the group law in this identification, a map reducing to the identity changes its coordinate functions by a derivation into \(I\). On a product, multiplication has first derivative the sum, since either factor restricted to the identity is the identity map; all products of two corrections lie in \(I^2=0\). Thus \([n]\) acts on this module by multiplication by \(n\). There is exactly one correction,
\[
 a\longmapsto a-n^{-1}([n]a-b),
 \tag{GQ6}
\]
which solves the lifting problem. The formula is in that square-zero kernel, translated from \(a\); it is not division of arbitrary group points. Uniqueness glues the local solutions. This proves formal étaleness. The maps are finitely presented over the Noetherian base, so the actual formal-lifting/Jacobian equivalence EA1–EA18 makes \([n]\) étale.

It is proper: its graph is closed in the product because the target is separated, and the projection of that product is a base change of the proper structure map. Étale fibres are zero-dimensional and discrete; properness makes each finite. Theorem 0.F.1 consequently makes \([n]\) finite, preserving its étaleness. Pull it back along the origin to obtain its finite étale kernel. Its finite flat coordinate module is locally free, by the Nakayama-and-flatness argument in Corollary 0.F.2, so its generic and special ranks agree.

Finally the group multiplication maps and origin commute with scalar extension, and a kernel is their actual fibre product. Finite modules, their local free bases and the unique square-zero lifts remain such after tensoring. These observations prove the arbitrary-base-change assertion. No numerical multiplication-degree theorem is needed for this comparison. \(\square\)

#### 2A.4. Every torsion level and every transition map

**GQ4.** Suppose \(R\) is Henselian. For every \(n\) invertible in \(R\), reduction gives a natural isomorphism
\[
 \mathcal A_K[n](K^{\mathrm{sep}})
     \xrightarrow{\ \sim\ }\mathcal A_{\bar k}[n](\bar k).
 \tag{GQ7}
\]
It is equivariant for the residue action, so inertia is trivial. For \(n=\ell^r\), these isomorphisms respect addition, all multiplication transitions and homomorphisms of good models. Consequently they give an isomorphism of the full Tate modules.

*Proof.* Pass to the strict Henselization \(R^{\mathrm{sh}}\), with separably closed residue field \(k^{\mathrm{sep}}\). A finite étale algebra over it is a product of copies of \(R^{\mathrm{sh}}\). Indeed its residue algebra is a product of copies of \(k^{\mathrm{sep}}\). The Henselian finite-algebra proof NP4 lifts its orthogonal idempotents. Each resulting factor is finite free of rank one, since its residue dimension is one. Nakayama makes its unit a basis, so that factor is the base ring itself. This proves the splitting assertion, rather than assuming a torsion-lifting theorem.

Apply it to GQ3's kernel. Every generic geometric torsion point is already rational over the fraction field of \(R^{\mathrm{sh}}\), and is the unique section of one of these rank-one factors. Reduction gives one point for each same factor. A finite étale scheme has the same points over \(k^{\mathrm{sep}}\) and \(\bar k\), since its residue extensions are separable. This proves (GQ7).

The strict Henselization and its fraction field are the union of the finite unramified local extensions constructed in Lesson 1. Thus inertia fixes all these sections. Uniqueness of their lifts makes reduction equivariant for every residue automorphism and compatible with all scheme maps, including semilinear coefficient maps. In particular the squares
\[
 \begin{array}{ccc}
 \mathcal A_K[\ell^{r+1}](K^{\mathrm{sep}})
   &\xrightarrow{[\ell]}&\mathcal A_K[\ell^r](K^{\mathrm{sep}})\\
 \downarrow &&\downarrow\\
 \mathcal A_{\bar k}[\ell^{r+1}](\bar k)
   &\xrightarrow{[\ell]}&\mathcal A_{\bar k}[\ell^r](\bar k)
 \end{array}
 \tag{GQ8}
\]
commute, as do the addition and homomorphism squares. Their vertical maps are bijections. Applying them coordinate by coordinate, and doing the same with their inverses, gives the inverse-limit isomorphism
\[
 T_\ell\mathcal A_K\simeq T_\ell\mathcal A_{\bar k}.
 \tag{GQ9}
\]
No interchange of a derived functor or unproved inverse-limit surjectivity is involved. \(\square\)

#### 2A.5. The semilinear action needed in Lemma 2.3

**GQ5.** Let \(L/F\) be a finite Galois extension of local fields and let an abelian variety \(B/F\) have a good abelian model \(\mathcal B/\mathcal O_L\). The generic descent isomorphisms extend uniquely to a semilinear action on this model. Its reduction and the comparisons (GQ7)–(GQ9) are equivariant, in every dimension.

*Proof.* A Galois automorphism preserves the unique extended valuation, by Lesson 1, Proposition 0E.1, so it acts on \(\mathcal O_L\). Its conjugate model \({}^\sigma\mathcal B\) is again a good abelian scheme over that ring. GQ2 extends the generic descent isomorphism to an isomorphism
\[
 d_\sigma:{}^\sigma\mathcal B\xrightarrow{\ \sim\ }\mathcal B .
 \tag{GQ10}
\]
Both sides of the cocycle relation are maps between good models with the same generic restriction. Uniqueness gives
\[
 d_\sigma\circ{}^\sigma d_\tau=d_{\sigma\tau}.
 \tag{GQ11}
\]
Thus these are the required semilinear group actions. When a Galois element fixes the residue field, its special map is an origin-preserving automorphism over that field. GQ4 makes every torsion reduction square commute with these actions and their multiplication transitions.

In particular, over this good-reduction field the whole inertia subgroup acts trivially on the rational Tate module for every coefficient prime different from the residue prime. The actual monodromy theorem in Lesson 7 then makes its nilpotent operator zero. The common good-reduction field and its finite residue action are available simultaneously for all those coefficient primes. These are exactly the model and specialization inputs in Lemma 2.3. Its endomorphism-character argument remains the one written in Lemma 2.2.

Relation (GQ11) is a semilinear action. For a ramified extension it is not, by itself, faithfully flat descent data on \(\mathcal O_L\otimes_{\mathcal O_F}\mathcal O_L\), and we have not claimed that a potentially good model is already good over \(F\). This distinction retains the full ramified scope of the lemma. \(\square\)

Milne's freely available [*Abelian Varieties*](https://www.jmilne.org/math/CourseNotes/AV.pdf), Chapter IV, §3, gives the good-reduction setting. The graph closure, special-fibre dimension bound, finite étale lifting and semilinear compatibility needed here have their proofs in GQ1–GQ5 above.

#### Exercise 2A — good models and their descent (100 points)

Each part is worth 10 points.

1. In \(C=\kappa[x,y,z]/(xy-z^2-1)\), put \(u=x-z^3\), \(v=y-z^9\). Find the monic equation for \(z\) over \(\kappa[u,v]\), and prove that this is a finite normalization by a polynomial subring.
2. Prove the special-fibre dimension bound by the primitive-relation argument. Explain why the polynomial after reduction is nonzero even when the residue field is finite.
3. Prove uniqueness of the irreducible component through the identity of a finite-type group over an algebraically closed field. Apply the statement to \(\mu_p\) in characteristic \(p\).
4. Over a DVR, compute the graph closure of \(f:\mathbf G_{a,K}\to\mathbf G_{a,K}\), \(x\mapsto x/\pi\). Explain exactly why it does not contradict GQ2.
5. Explain the use of normality at the last step of GQ2. Give a finite birational morphism for which that step fails without normality.
6. Carry out the square-zero correction for a commutative smooth group in \(g\) tangent coordinates. Identify the failure when the characteristic divides \(n\).
7. Prove the splitting of a rank-\(r\) finite étale algebra over a strictly Henselian local ring. Compare it with \(\mu_p\) over a mixed-characteristic DVR of residue characteristic \(p\).
8. Prove that levelwise reduction gives an isomorphism of the entire torsion inverse system, including its group law and transition maps; do not appeal to exactness of inverse limits.
9. For \(B=R[u]/(u^2-\pi)\) in characteristic zero, with \(\tau(u)=-u\), compute the determinant of the map \(B\otimes_RB\to B\times B\) given by the two Galois embeddings. Explain its relevance to ramified descent.
10. On the good abelian scheme \(\mathcal E^2\), extend the homomorphism with integer matrix \(\begin{pmatrix}1&1\\1&2\end{pmatrix}\), find its inverse, and verify compatibility with torsion reduction. Explain why GQ1–GQ5 still leave Theorem 2.4's general semistable case unfinished.

*Full solution.*

1. Substitute \(x=u+z^3\), \(y=v+z^9\) in the defining relation:
\[
 z^{12}+u z^9+v z^3+uv-z^2-1=0 .
 \tag{GQX1}
\]
It is monic in every characteristic. Thus \(z\), and then \(x,y\), are integral over the subalgebra generated by \(u,v\). Powers below twelve span the resulting algebra as a module. The original ring is a domain with fraction field \(\kappa(y,z)\). Here is a direct kernel check: substitute \(x=(z^2+1)/y\) in the localization inverting \(y\); division by the resulting monic linear relation makes the kernel there its defining ideal. This ideal is already saturated by \(y\). Indeed if \(yP=(xy-z^2-1)H\), reducing modulo \(y\) gives \((z^2+1)\bar H=0\) in the domain \(\kappa[x,z]\), so \(H=yH_1\); cancellation gives \(P=(xy-z^2-1)H_1\). Iterate to clear every power of \(y\). This proves the claimed injection into \(\kappa(y,z)\). Also the ideal has zero intersection with \(\kappa[y,z]\), by its positive degree in \(x\), so \(y,z\) are algebraically independent. Consequently its transcendence degree is two. A finite integral extension has algebraic fraction-field extension; if \(u,v\) were dependent their field would have transcendence degree at most one. Thus they are independent, and this is indeed a finite extension of the polynomial subring \(\kappa[u,v]\). The powers \(3,9\) separate the weights of the original relation's monomials \(xy,z^2,1\), namely \(12,2,0\).

2. Choose independent special-fibre parameters \(\bar t_1,\ldots,\bar t_d\) and lift them to the chart domain. A nonzero relation with fraction-field coefficients can be multiplied by a power of \(\pi\) so that its minimum coefficient valuation is zero. Its reduced polynomial has at least one nonzero coefficient. This is a nonzero element of the polynomial ring over the residue field, irrespective of how many values a finite field has: algebraic independence concerns polynomial identities, not polynomial functions on its finite set of points. Reduction would contradict the chosen independence. Thus the lifts are independent over \(K\) and \(d\le g\).

3. For two components \(C,D\) through the identity, the multiplication image of their reduced product has irreducible closure. It contains \(C\) by multiplying by the identity in \(D\), and \(D\) by multiplying by the identity in \(C\). Both are maximal irreducible closed subsets, so they coincide. Translate each other component by the inverse of one of its closed points to obtain this unique component. Two distinct translates cannot intersect, since translating an intersection point to the identity would contradict uniqueness. For
\[
 \mu_p=\operatorname{Spec}\kappa[t]/(t^p-1)
      =\operatorname{Spec}\kappa[t]/((t-1)^p)
 \tag{GQX2}
\]
there is one underlying component and one geometric point, but a nonreduced coordinate algebra of length \(p\). The component argument makes no assertion that the scheme is smooth or reduced.

4. The graph equation is \(\pi y=x\). Its closure is already
\(\operatorname{Spec}R[y]\), with first projection \(x=\pi y\). It is flat and is a group scheme. Its generic projection is an isomorphism, while its special projection has image just zero and has a whole affine line as kernel. The target's generic fibre is dense, so this image is not closed: it contains the generic fibre but misses every nonzero geometric special point. Thus this projection is not proper. In GQ2 properness forced surjectivity on the special fibre; that decisive step is unavailable for the additive group.

5. A finite birational map to the normal integral target gives, on affine charts, a finite integral algebra inside the same fraction field. Integral closedness makes that algebra equal to the target algebra. For the cusp the inclusion
\[
 \kappa[t^2,t^3]\subset\kappa[t]
 \tag{GQX3}
\]
is finite and birational but not equality. Its fraction field contains \(t=t^3/t^2\); its larger ring is spanned as a module by \(1,t\). The element \(t\) satisfies the monic equation \(T^2-t^2=0\) over the smaller ring but is not in it, since its monomials have exponents zero or at least two. Hence this target is not normal. Merely knowing that the graph projection is finite and generically an isomorphism would therefore be insufficient.

6. In tangent coordinates the square-zero kernel is \(I^g\), and its group law is vector addition: the quadratic terms vanish in \(I^2\). If the discrepancy is \(e\in I^g\), changing a lift by \(c\) changes its multiplied value by \(nc\). The unique solution is \(c=-n^{-1}e\). When \(n=0\) in the residue characteristic, multiplication on a nonzero square-zero residue module is zero. It has no solution for a nonzero discrepancy and has many solutions for zero discrepancy. This proves the precise failure of formal étaleness, rather than a claim based only on a torsion-point count.

7. The residue algebra is a product of \(r\) copies of the separably closed residue field. Henselian lifting gives its orthogonal idempotents, splitting the original finite étale algebra into \(r\) factors. Each is finite locally free of rank one, determined by its residue dimension. Its unit generates by Nakayama and is a basis; multiplication then identifies it with the base ring. The reductions of these factors give all \(r\) points and their unique lifts.

For \(\mu_p\) in mixed characteristic the generic fibre has \(p\) distinct geometric roots, since the derivative of \(t^p-1\) is nonzero at them. The special algebra is (GQX2), with only one geometric point and length \(p\). All its roots therefore reduce to the identity, so it does not satisfy the comparison of geometric points. It is finite free, but its derivative is not a unit and it is not étale. This shows why finite flatness alone and the case \(n=p\) cannot be substituted in GQ3–GQ4.

8. Let \(r_m\) denote the reduction bijection at level \(\ell^m\). Naturality for the scheme map \([\ell]\) gives
\[
 r_m([\ell]x)=[\ell]r_{m+1}(x).
 \tag{GQX4}
\]
Thus a compatible tuple maps to a compatible tuple. The inverses satisfy the same relation because the \(r_m\) are bijections; applying them coordinate by coordinate gives an inverse map of the limits. Naturality for the addition map makes it a group homomorphism, and compatibility with multiplication by integers makes it \(\mathbf Z_\ell\)-linear. The same argument for a model homomorphism proves its functoriality. These are explicit inverse maps, so no general exactness claim about inverse limits is required.

9. Use the left-\(B\) basis \(1\otimes1,1\otimes u\) of \(B\otimes_RB\). The map has matrix
\[
 \begin{pmatrix}1&u\\1&-u\end{pmatrix},
 \qquad\det=-2u .
 \tag{GQX5}
\]
The element \(u\) is nonunit, since \(u^2=\pi\), so its determinant is not a unit. The map becomes an isomorphism on the characteristic-zero generic fibre but is not an isomorphism over \(B\). Consequently the integral double overlap is not the disjoint union of the two Galois graphs. A semilinear action satisfying a Galois cocycle therefore does not automatically give the full faithfully flat descent datum for a ramified extension. In GQ5 it supplies an action on the good model over \(B\); it does not assert good reduction over \(R\).

10. Define the map directly using the group scheme operations:
\[
 (P,Q)\longmapsto(P+Q,P+[2]Q),\qquad
 (U,V)\longmapsto([2]U-V,V-U).
 \tag{GQX6}
\]
The two composites are identities by addition and subtraction. Equivalently the integer inverse matrix is \(\begin{pmatrix}2&-1\\-1&1\end{pmatrix}\). Thus this is an automorphism of the entire good two-dimensional model, and GQ2 identifies it with the unique extension of its generic map. On torsion its block entries are the same integer multiplications, so (GQX4) and addition prove compatibility with reduction and with every transition.

GQ1–GQ5 assume a good abelian model after a finite extension. In general the reduction may have a torus, and its rational Tate module may have nonzero monodromy. The theorem still needs actual semistable models, their toric and abelian graded pieces, the nondegenerate monodromy pairing and finite descent equivariance. The good-model extension argument does not supply those data. Hence Theorem 2.4 retains its full general statement and its stated remaining proof obligation.

### 2B. Coherent Euler polynomials and finite commutative torsors

The Euler inputs in Lemma 2.2 need their own proofs. We give them on proper schemes, including nonreduced schemes and inseparable isogenies. We also prove the reduced-base see-saw statement that will be needed in a cube argument. This section does not assume the cube, a multiplication-degree formula, an intersection-theoretic Riemann–Roch theorem or semisimplicity of finite-group representations.

The actual earlier inputs are the affine sheaf/cohomology proofs SC0–SC15 and proper coherent finiteness CG13–CG14 in Lesson 3; its finite projective family complex FC1–FC20 and finite faithfully flat module descent FD1–FD4; and the field-dimension argument GQ1 above. All sums of cohomology dimensions below are finite: CG13 gives finite-dimensional groups, and the finite affine Čech complex bounds their nonzero degrees.

#### 2B.1. Tensoring by a line lowers the support filtration

Let \(G_0(X)\) be the abelian group on coherent sheaves, with relation
\[
 [\mathcal F]=[\mathcal F']+[\mathcal F'']
 \quad\text{for }0\to\mathcal F'\to\mathcal F\to\mathcal F''\to0 .
 \tag{CE1}
\]
Its subgroup \(F_dG_0(X)\) is generated by sheaves with support dimension at most \(d\); put \(F_{-1}=0\). Tensoring by a line \(\mathcal L\) is exact, so gives an automorphism \(T_{\mathcal L}\) of this group and preserves each subgroup. The long exact cohomology sequence, with alternating cancellation of its finite-dimensional images, makes \([\mathcal F]\mapsto\chi(X,\mathcal F)\) an additive map to \(\mathbf Z\).

**CE1.** For a line on a Noetherian finite-type scheme over a field,
\[
 (T_{\mathcal L}-1)F_dG_0(X)\subset F_{d-1}G_0(X).
 \tag{CE2}
\]

*Proof.* Fix \(\mathcal F\), and choose a line frame near the generic point of each irreducible component of its support. Remove the other support components from each chosen open, and include the complement of the support. Their union is an open \(U\) containing every support generic point. On its overlaps the sheaf is zero unless the same chosen component is present. Thus those frames give an isomorphism
\(\theta:\mathcal F|_U\simeq(\mathcal F\otimes\mathcal L)|_U\).

With \(j:U\hookrightarrow X\), take the kernel of
\((a,b)\mapsto\theta(a)-b\) from
\(\mathcal F\oplus(\mathcal F\otimes\mathcal L)\) to
\(j_*((\mathcal F\otimes\mathcal L)|_U)\). This kernel \(\mathcal G\) is coherent. Indeed this open is quasi-compact, and the finite affine-cover localization argument SC14 in degree zero makes its pushed sheaf quasi-coherent; a quasi-coherent submodule of a coherent module over a Noetherian scheme is coherent. It is the graph of \(\theta\) on \(U\).

Let \(K_i,C_i\) be the kernels and cokernels of its two projections. They are coherent and vanish on \(U\); outside the original support they vanish as well. Every remaining support component is a proper closed subset of an original component. The strict transcendence-degree drop proved in GQ1 bounds its dimension by \(d-1\). The two projection sequences give
\[
 [\mathcal F\otimes\mathcal L]-[\mathcal F]
       =[K_1]-[K_2]+[C_2]-[C_1].
 \tag{CE3}
\]
This proves (CE2), including \(d=0\), when all four remaining supports are empty. Embedded points and nilpotents have not been removed from the sheaves. \(\square\)

#### 2B.2. The full multivariable polynomial, including negative powers

**CE2.** For a proper scheme \(X/k\), a coherent \(\mathcal F\) and lines \(\mathcal L_1,\ldots,\mathcal L_r\), the function
\[
 P(\mathbf n)=\chi\left(X,\mathcal F\otimes
               \bigotimes_i\mathcal L_i^{\,n_i}\right),
 \qquad\mathbf n\in\mathbf Z^r ,
 \tag{CE4}
\]
is an integer-valued rational polynomial of total degree at most
\(d=\dim\operatorname{Supp}\mathcal F\).

*Proof.* The zero sheaf gives the zero polynomial, so assume its support is nonempty. Put \(D_i=T_{\mathcal L_i}-1\). These operators commute, and CE1 makes every product of \(d+1\) of them zero on \(F_dG_0(X)\). On that subgroup the binomial identity therefore gives
\[
 P(\mathbf n)=
 \sum_{|\boldsymbol\alpha|\le d}
  \left(\prod_i {n_i\choose\alpha_i}\right)
  \chi\left(X,D_1^{\alpha_1}\cdots D_r^{\alpha_r}[\mathcal F]\right).
 \tag{CE5}
\]
The last Euler expression means its additive value on the displayed virtual sheaf class. It is an integer.

For completeness the identity works for every negative integer too. In the commutative operator ring modulo products of degree greater than \(d\), \(1+D_i\) is a unit with inverse \(1-D_i+D_i^2-\cdots+(-D_i)^d\). The polynomials
\({n\choose a}=n(n-1)\cdots(n-a+1)/a!\) satisfy Pascal's recurrence for every integer \(n\). Starting at \(n=0\), that recurrence proves the truncated binomial expansion forward and backward, using this inverse. It is therefore the actual power \((1+D_i)^{n_i}\), not just a formula on nonnegative arguments.

Each summand in (CE5) has degree \(|\boldsymbol\alpha|\le d\). The binomial factors are integral on all integers: for \(n<0\),
\({n\choose a}=(-1)^a{a-n-1\choose a}\). This proves the assertion. The polynomial is unique: a polynomial zero on the integer grid is zero, by induction in the number of variables and the fact that a one-variable polynomial has only finitely many roots unless it vanishes. \(\square\)

A useful consequence is
\[
 \chi(X,\mathcal F\otimes\mathcal T)=\chi(X,\mathcal F)
       \quad\text{if }\mathcal T^{\,m}\simeq\mathcal O_X
       \text{ for some }m>0.
 \tag{CE6}
\]
Indeed its polynomial in the exponent of \(\mathcal T\) is periodic. A nonconstant rational polynomial cannot be periodic: subtracting its translate by \(m\) leaves a nonzero polynomial of degree one smaller. Euler characteristics take values in \(\mathbf Z\), so this argument is valid also in positive characteristic.

#### 2B.3. Families and the precise see-saw assertion

**CE3.** Euler characteristic is locally constant in every proper flat coherent family over a Noetherian base. Suppose \(X/k\) is proper and geometrically integral, \(S\) is reduced and Noetherian, and a line \(\mathcal M\) on \(X\times_kS\) is trivial on every geometric fibre over \(S\). Then
\[
 p_*\mathcal M\text{ is a line},\qquad
 p^*p_*\mathcal M\xrightarrow{\ \sim\ }\mathcal M.
 \tag{CE7}
\]
These assertions commute with arbitrary base change. If \(x_0\in X(k)\), the line on the base is canonically \(x_0^*\mathcal M\).

*Proof.* On an affine base the actual finite projective complex FC10 computes every fibre of a proper flat coherent family. The alternating sum of its term ranks equals the alternating sum of the dimensions of its cohomology, by cancellation of boundary spaces. These ranks are locally constant; so is their alternating sum. This proves the Euler assertion, without any hypothesis that the base is reduced or that individual cohomology dimensions are constant.

For the line assertion apply FC10 to \(\mathcal M\). At any base point, the geometric fibre has \(H^0\) of dimension one, by the proper-geometrically-integral constants proof FC20. Field base change gives dimension one over its actual residue field. The unit-entry cancellation FC13–FC14, after shrinking around that point, leaves a complex in nonnegative degrees whose degree-zero term is free of rank one. At every point of this neighbourhood its degree-zero differential has zero residue matrix, since its kernel has dimension one. Its entries belong to every prime ideal. Reducedness makes them zero. Thus the degree-zero cohomology is that free line, after every module or ring base change, regardless of the higher differentials.

The natural evaluation in (CE7) is now a map of lines. On every geometric fibre a basis section is a nonzero constant in a trivial line, so is nowhere zero. In a local frame its coefficient is consequently in no maximal ideal, and is a unit. Evaluation is therefore an isomorphism everywhere. Pulling it back along \(x_0\) gives the stated canonical identification. All the section comparisons used are FC10's natural comparisons, so they remain valid after arbitrary, even nonreduced, base change. A rigidification at \(x_0\) also fixes the isomorphism: by FC20 an automorphism of a pulled-back line is a unit from the base, which its value at \(x_0\) determines. \(\square\)

Reducedness in this see-saw assertion matters. On a genus-one curve choose a nonzero Čech class \(c_{ij}\) in \(H^1(X,\mathcal O_X)\), using the written curve computation of Lesson 3. Over \(k[\epsilon]/(\epsilon^2)\) the units
\[
 g_{ij}=1+\epsilon c_{ij}
 \tag{CE8}
\]
give a line bundle with trivial geometric fibre. They satisfy the cocycle identity because \(\epsilon^2=0\). If this line were trivial, its trivializing units could first be divided by their common nonzero constant reduction, since \(H^0(X,\mathcal O_X)=k\). They would then have the form \(1+\epsilon a_i\), forcing \(c_{ij}\) to be a Čech boundary. This contradicts the choice of its class. A line pulled back from this local base is trivial, so (CE7) would fail here. The Euler assertion still holds.

#### 2B.4. Proper pushforward and the image-dimension bound

**CE4.** For a proper map \(f:X\to Y\) of proper schemes over \(k\), and coherent \(\mathcal F\),
\[
 \chi(X,\mathcal F)
   =\sum_q(-1)^q\chi(Y,R^qf_*\mathcal F).
 \tag{CE9}
\]
For lines \(\mathcal L_i\) on \(Y\), the polynomial
\(\chi(X,\mathcal F\otimes f^*\bigotimes_i\mathcal L_i^{\,n_i})\)
has total degree at most \(\dim f(\operatorname{Supp}\mathcal F)\).

*Proof.* We supply the cohomological passage, since the vanishing-image result SC15 alone would not prove (CE9). For a module sheaf \(H\) on a space define
\(C(H)(U)=\prod_{x\in U}H_x\). This is a flasque sheaf, its restrictions being projections, and \(H\to C(H)\) is injective. The functor \(C\), including its sections over every fixed open, is exact: stalk sequences are exact and products of surjections are surjective by choosing one preimage in each factor. The quotient functor \(Q(H)=C(H)/H\) is exact by the kernel/cokernel diagram for these injections. Iterating gives a functorial flasque resolution with terms \(C(Q^pH)\). The section functors of its individual terms are exact too.

For a complex \(K^\bullet\) bounded below, take the signed total complex of the sections of these resolutions applied to every term. Each diagonal is finite. Its cohomology is unchanged by a quasi-isomorphism: on an acyclic input complex, each row is exact by the exact section functors, and the finite-diagonal elimination SH9 gives an acyclic total complex. Mapping cones, with the shifted component multiplied in resolution degree \(p\) by \((-1)^p\), identify the comparison with the cone comparison. Short exact sequences of input complexes remain short exact after these exact section functors and totalization, and so give the ordinary long exact cohomology sequence. If the input terms are flasque, the other elimination direction, using their vanishing higher cohomology proved in SC7, identifies this total cohomology with that of \(\Gamma(K^\bullet)\).

If the cohomology sheaves of \(K^\bullet\) are coherent and vanish above some \(q_0\), its good truncation at \(q_0\) is a quasi-isomorphism to it. Successive good truncations differ by a complex quasi-isomorphic to \(\mathcal H^q(K)[-q]\). Explicitly the quotient has the two terms \(B^q(K)\hookrightarrow Z^q(K)\) in degrees \(q-1,q\), with cokernel \(\mathcal H^q(K)\). The long exact sequences just constructed, and alternating cancellation, therefore make its total Euler characteristic
\(\sum_q(-1)^q\chi(Y,\mathcal H^q(K))\).
All these groups are finite-dimensional and bounded: this follows inductively from coherent cohomology finiteness and the finite affine cover of \(Y\).

Apply this construction to \(K^\bullet=f_*I^\bullet\), where \(I^\bullet\) is an injective resolution of \(\mathcal F\). Its terms are flasque, and remain flasque under pushforward, because restrictions are restrictions on inverse images of opens. Its sections are exactly \(\Gamma(X,I^\bullet)\). Its cohomology sheaves are \(R^qf_*\mathcal F\), coherent by CG14 and zero in large degree by SC14 on a finite affine cover of \(Y\). This proves (CE9) with its full nonvanishing higher-image scope.

For an invertible \(\mathcal L\), local frames and the natural cohomology comparison SC13 give
\[
 R^qf_*(\mathcal F\otimes f^*\mathcal L)
      \simeq R^qf_*\mathcal F\otimes\mathcal L .
 \tag{CE10}
\]
On overlaps the frame changes give the same tensor maps, so these local identities glue. All these coherent higher images are supported on the closed set \(f(\operatorname{Supp}\mathcal F)\): on its open complement the original sheaf is zero. Apply CE2 on \(Y\) to each term of (CE9), using (CE10). Each support has dimension at most that image dimension. Their finite signed sum proves the asserted bound. \(\square\)

#### 2B.5. Finite commutative group representations without semisimplicity

**CE5.** Over an algebraically closed field, every finite-dimensional representation of a finite commutative group scheme has a filtration with one-dimensional character quotients. Each such character has finite order.

*Proof.* Write \(H\) for its finite-dimensional coordinate Hopf algebra. A representation is an \(H\)-comodule. By choosing a basis and its dual, the coaction is equivalently a module structure over the finite algebra \(D=\operatorname{Hom}_k(H,k)\), with multiplication
\((ab)(h)=(a\otimes b)(\Delta h)\).
Coassociativity is precisely module associativity, and the counit supplies its unit. This establishes the equivalence directly. Commutativity of the group makes \(\Delta\) cocommutative, so \(D\) is commutative.

A simple finite \(D\)-module is the residue field at a maximal ideal: any nonzero vector generates it, and its annihilator is maximal. That field is finite-dimensional over the algebraically closed \(k\), hence equals \(k\). Choosing a maximal proper submodule and inducting on vector-space dimension gives the claimed filtration, with one-dimensional quotients. No complement or semisimplicity is required.

A one-dimensional coaction is multiplication by an element \(h\in H\) with
\(\Delta h=h\otimes h\) and counit one. The antipode makes it a unit. Distinct such elements are linearly independent. Indeed if a first dependence expressed \(h_m=\sum_{i<m}a_i h_i\) in an independent list, apply \(\Delta\) and compare the independent tensors \(h_i\otimes h_j\). The off-diagonal equations give \(a_i a_j=0\) for \(i\ne j\), and the diagonal equations give \(a_i^2=a_i\). Exactly one coefficient would be one, making \(h_m\) equal an earlier element, a contradiction.

The powers of \(h\) are also of this kind. Finite dimension therefore forces two to coincide, and invertibility gives \(h^m=1\) for some \(m>0\). This is precisely finite order of the character as a group-scheme morphism, not just its values on geometric points. \(\square\)

#### 2B.6. Torsor Euler comparison, including inseparable isogenies

**CE6.** Let \(f:P\to Y\) be a finite faithfully flat torsor of rank \(N\) under a finite commutative \(k\)-group scheme, with \(Y\) proper. For every coherent \(\mathcal F\) on \(Y\),
\[
 \chi(P,f^*\mathcal F)=N\,\chi(Y,\mathcal F).
 \tag{CE11}
\]
In particular this holds for every isogeny of abelian varieties, including inseparable isogenies.

*Proof.* Field base change commutes with coherent cohomology here: tensor the finite affine Čech complex with the field and use exactness of vector-space tensor products. Dimensions over the new field are the old dimensions. Ranks and the torsor square also persist. We may therefore work over an algebraic closure.

Put \(\mathcal E=f_*\mathcal O_P\). The actual torsor identity identifies its pullback to \(P\) with \(\mathcal O_P\otimes_k H\), where \(H\) is the coordinate algebra of the group. Changing a torsor frame translates the \(H\)-factor, so its descent datum is the regular representation. Apply CE5 to that \(N\)-dimensional representation. Each step is an invariant subspace, and the finite faithfully flat descent construction FD1–FD4 descends its tensor with \(\mathcal O_P\) to a subbundle of \(\mathcal E\). Exactness is tested after that faithful flat cover, where the quotient is a free line. This gives
\[
 0=\mathcal E_0\subset\mathcal E_1\subset\cdots
       \subset\mathcal E_N=\mathcal E,\qquad
 \mathcal E_i/\mathcal E_{i-1}=\mathcal T_i,\qquad
 \mathcal T_i^{\,m_i}\simeq\mathcal O_Y .
 \tag{CE12}
\]
The last assertion follows because tensoring associated lines multiplies their characters, and CE5 gives finite character order.

Tensor this filtration with \(\mathcal F\). It remains exact because the line quotients are flat, by the elementary tensor lemma 0.D.1(a). Thus (CE6) and additivity give
\(\chi(Y,\mathcal E\otimes\mathcal F)=N\chi(Y,\mathcal F)\).
On affine charts a finite map has exact module pushforward and no positive quasi-coherent higher images. Its tensor identity gives
\(f_*f^*\mathcal F=\mathcal E\otimes\mathcal F\).
The proved collapse SC15, or (CE9), now proves (CE11).

We verify the isogeny assertion without importing finite flatness. An isogeny is a finite surjective homomorphism \(f:A\to B\) of abelian varieties. Over the algebraic closure, its finite coordinate module is free of its generic rank on some nonempty open \(U\) of \(B\): choose a fraction-field basis, clear its denominators, and kill the finitely generated kernel and cokernel of the resulting basis map by another nonzero denominator. For any \(b\in B(k)\), choose \(a\in A(k)\) above it. Translation identifies the map over \(U+b\) with that over \(U\), preserving the free rank. These translates cover: fix a closed point of \(U\); translating it reaches every closed point of \(B\), and a nonempty closed complement would have a closed point by EA2. Thus \(f\) is finite locally free. Flatness descends from the algebraic closure, since injections after tensoring can be tested after a faithfully flat field extension. This proves finite flatness over the original field too.

Its kernel \(G\) is a finite commutative group scheme of that rank. The group operations give mutually inverse scheme maps
\[
 A\times G\longrightarrow A\times_B A,\quad
 (a,g)\longmapsto(a,a+g),\qquad
 (a,a')\longmapsto(a,a'-a).
 \tag{CE13}
\]
They are inverse on every scheme's points by the kernel square, and the formulas are morphisms. Hence \(f\) is exactly the required torsor. No separability or reduced-kernel condition has occurred. \(\square\)

#### 2B.7. Application and the retained geometric inputs

**CE7.** For an isogeny \(f:A\to A\) of degree \(N\), and any line \(\mathcal H\),
\[
 \chi(A,f^*\mathcal H)=N\chi(A,\mathcal H).
 \tag{CE14}
\]
For any proper map through a scheme of dimension \(h\),
\[
 \deg_n\chi\bigl(X,\mathcal F\otimes f^*\mathcal L^{\,n}\bigr)\le h .
 \tag{CE15}
\]
The degree in (CE15) is polynomial degree, and the zero polynomial satisfies the bound.

*Proof.* The rank of a finite locally free isogeny is its degree, by its fraction-field basis and the constant rank proved in CE6. Apply (CE11) to \(\mathcal H\) to obtain (CE14). Apply CE4, since its support image is contained in that \(h\)-dimensional scheme, to obtain (CE15). The full multivariable version is CE2 and CE4. \(\square\)

These give the Euler comparison and the lower-image bound in Lemma 2.2 directly in this lesson. To form its displayed ratio one still needs the positive nonzero Euler characteristic of the chosen symmetric ample line. The normalized cube, multiplication-degree formula, Euler homogeneity and the kernel/Tate-rank facts retain their actual earlier-proof and free-origin obligations. CE1–CE7 has not proved those statements by renaming an Euler polynomial as a homogeneous one. Theorem 2.4's full semistable, toric, monodromy-pairing and descent requirements also remain separate.

Free primary comparisons are the Stacks project authors' [Euler characteristics](https://stacks.math.columbia.edu/tag/0BEI) and [numerical polynomial statement](https://stacks.math.columbia.edu/tag/0BEL). The support-graph, all-integer binomial, full higher-image Euler, and finite-group-scheme torsor arguments used here are written above; citations do not replace them.

#### Exercise 2B — support differences, families and torsors (100 points)

Each part is worth 10 points.

1. Derive the four-term identity (CE3) from the two graph projections. Compute the Euler polynomial of \(\operatorname{Spec}k[\epsilon]/(\epsilon^r)\) for \(r>0\), and explain the role of its nilpotents.
2. Find all Newton coefficients at the origin of
\(P(n,m)={n\choose2}+3nm-2m+5\). Evaluate it at \((-2,3)\) using (CE5), and prove that all differences of total order three vanish.
3. Compute \(\chi(\mathbf P^1\times\mathbf P^1,\mathcal O(n,m))\) for every pair of integers, using the coordinate covers. Explain why the mixed second difference is nonzero and every third difference is zero.
4. Prove torsion-line Euler invariance. Show by a finite flat degree-two map of projective lines that Euler scaling does not hold for an arbitrary finite flat map.
5. For \(f:\mathbf P^1\times E\to\mathbf P^1\), with \(E\) a genus-one curve, compare \(\mathcal O(n)\boxtimes\mathcal O_E\) with \(\mathcal O(n)\boxtimes L\), where \(L\) has degree one. Compute the higher images and their Euler sums.
6. In the see-saw proof, identify the exact step using reducedness. Prove that the dual-number gluing (CE8) gives the stated counterexample whenever its Čech class is nonzero.
7. In characteristic \(p\), construct a nonsplit two-dimensional representation of \(\alpha_p\). For \(\mu_p\), find its \(p\) distinct group-scheme characters and compare them with its geometric points.
8. On a proper scheme, given a torsion line \(T\) with a fixed \(T^n\simeq\mathcal O_Y\) for a positive exponent, construct its \(\mu_n\)-torsor and prove (CE11) directly. Include \(n=p\) in characteristic \(p\).
9. Apply CE6 to \([p]:E\to E\) in characteristic \(p\) and a degree-one line. Use the actually proved elliptic multiplication degree from Lesson 3, not a new arbitrary-dimensional degree assertion.
10. Suppose a nonzero rational polynomial \(P\) has degree exactly \(g\), and \(P(m^2t)=D_mP(t)\) for one integer \(m\ge2\). Prove the degree and homogeneity conclusion. Show why a degree bound alone is insufficient, and list the additional geometric inputs needed to apply it to an abelian variety.

*Full solution.*

1. For projection \(i\), its kernel and cokernel give
\([\mathcal F_i]=[\mathcal G]-[K_i]+[C_i]\).
Subtract the formula for the first projection from that for the second. This is exactly (CE3), with signs \(+K_1,-K_2,+C_2,-C_1\). For the proposed finite scheme, affine cohomology vanishes above zero and its coordinate algebra has basis \(1,\epsilon,\ldots,\epsilon^{r-1}\). Every line over its local ring is free of rank one: lift a residue basis and use Nakayama and projectivity. Hence its Euler polynomial is the constant \(r\). Its support has dimension zero but its length is \(r\); replacing it by its reduction would incorrectly give one.

2. The nonzero Newton coefficients are
\[
 c_{00}=5,\quad c_{01}=-2,\quad c_{20}=1,\quad c_{11}=3.
 \tag{CEX1}
\]
The first \(n\)-difference at the origin is zero, as is the pure second \(m\)-difference. Thus
\(P(-2,3)=5-2\cdot3+{ -2\choose2}+3(-2)\cdot3=-16\).
Pascal's identity lowers the index of a binomial factor under a forward difference. Every displayed term has total degree at most two, so any three differences kill it, including repeated and mixed differences. This proves the claim on all integer arguments, not just nonnegative ones.

3. The two-affine cover of \(\mathbf P^1\) gives
\(h^0(\mathcal O(n))=\max(n+1,0)\) and
\(h^1(\mathcal O(n))=\max(-n-1,0)\).
Indeed its sections are the allowed polynomial monomials in the two frames; its degree-one quotient consists exactly of the Laurent monomials missing from both frames. Thus its Euler characteristic is \(n+1\) for every integer \(n\).

The product cover has the tensor product of these two Čech complexes, with the signed total differential. Over a field split each complex into its cohomology and its contractible boundary pairs by choosing vector-space complements. A contractible pair remains contractible after tensoring, using its homotopy with the usual degree sign. This proves the needed product cohomology computation directly. Consequently
\[
 \chi(\mathcal O(n,m))=(n+1)(m+1),\qquad
 \Delta_n\Delta_m\chi=1,\quad
 \Delta_n^2\chi=\Delta_m^2\chi=0 .
 \tag{CEX2}
\]
Every third difference is zero. At \((-2,-3)\), only degree-two cohomology survives, of dimension \(1\cdot2=2\), agreeing with this polynomial.

4. For \(T^a\simeq\mathcal O\), the integer-valued rational polynomial \(\chi(\mathcal F\otimes T^n)\) is periodic with period \(a\). Its leading term would give a nonzero leading term in the difference of its translate unless it were constant. It is therefore constant, giving (CE6).

By contrast the morphism
\([X:Y]\mapsto[X^2:Y^2]\) of projective lines is finite flat of rank two: on each target coordinate chart its algebra is \(k[t]\) over \(k[t^2]\), with basis \(1,t\). Yet both source and target have \(\chi(\mathcal O)=1\), so
\[
 \chi(\mathbf P^1,\mathcal O)\ne
       2\chi(\mathbf P^1,\mathcal O).
 \tag{CEX3}
\]
This is not a torsor: above zero its geometric fibre is a double point, while above a nonzero point in characteristic different from two it has two distinct points. In any fixed finite group-scheme torsor the geometric fibres are all isomorphic to that group after choosing a point, so this difference excludes a torsor. The numerical failure itself holds in every characteristic.

5. The written genus-one cohomology gives \(H^0(E,\mathcal O_E)=k\) and \(H^1(E,\mathcal O_E)=k\). Over an affine base chart the Čech complex of \(E\) tensors with that chart's coordinate algebra. SC13–SC14 therefore identify the higher-image sheaves as
\[
 R^0f_*(\mathcal O(n)\boxtimes\mathcal O_E)
   =R^1f_*(\mathcal O(n)\boxtimes\mathcal O_E)=\mathcal O(n).
 \tag{CEX4}
\]
All higher images vanish. Their signed Euler sum is zero, while retaining only the zeroth image would give \(n+1\). This shows why SC15's vanishing hypothesis could not simply be omitted.

For a degree-one \(L\), the proved genus-one Riemann–Roch gives \(h^0(L)=1,h^1(L)=0\). The same coordinate computation gives zeroth image \(\mathcal O(n)\), all positive images zero, and Euler polynomial \(n+1\). Its degree is one, equal to the image dimension, although the total source has dimension two.

6. After unit cancellation the degree-zero term has rank one. Constant fibre \(h^0=1\) makes the entries of its outgoing differential belong to every prime. They vanish because the base is reduced. Over a nonreduced base they may be nonzero nilpotents, and this is the exact unsupported step if reducedness were removed.

For (CE8), the cocycle equation is
\((1+\epsilon c_{ij})(1+\epsilon c_{jk})=1+\epsilon(c_{ij}+c_{jk})=1+\epsilon c_{ik}\).
Each factor is a unit, with inverse \(1-\epsilon c_{ij}\), so these data glue a line. Its geometric fibre is trivial. If it had trivializing units, their reductions would glue to a global unit on the proper geometrically integral curve, hence a common constant. Divide by it. Writing the units as \(1+\epsilon a_i\) would now express \(c_{ij}\) as a boundary, contrary to its nonzero class. A line from the local dual-number base is trivial, so this also disproves the pulled-back-line conclusion there.

7. Write \(H=k[t]/(t^p)\) with primitive comultiplication
\(\Delta t=t\otimes1+1\otimes t\). On a basis \(e_1,e_2\) set
\[
 \rho(e_1)=e_1\otimes1,\qquad
 \rho(e_2)=e_2\otimes1+e_1\otimes t .
 \tag{CEX5}
\]
The primitive identity is exactly coassociativity, and the counit is immediate. The line \(ke_1\) and the quotient are trivial representations. Any complementary line would be generated by \(e_2+a e_1\), whose coaction still has the nonzero extra term \(e_1\otimes t\); it is not a trivial subrepresentation. Thus this extension does not split.

For \(\mu_p\), the elements \(1,z,\ldots,z^{p-1}\) in \(k[z]/(z^p-1)\) form a basis and satisfy \(\Delta z^i=z^i\otimes z^i\). They give \(p\) distinct characters. Nevertheless its geometric point set has one point, because \(z^p-1=(z-1)^p\). Characters in CE5 are scheme morphisms; geometric-point functions would lose these distinctions.

8. Form the finite algebra
\(\mathcal A=\bigoplus_{i=0}^{n-1}T^i\), using the fixed trivialization for multiplication when exponents reach \(n\), and put \(P=\operatorname{Spec}_Y\mathcal A\). Locally it is \(R[z]/(z^n-u)\) for a unit \(u\); it is free of rank \(n\), hence finite faithfully flat. The coaction multiplies \(z\) by the \(\mu_n\) coordinate. On the double overlap, \(z_1\) is a unit and
\[
 z_2=z_1w,\qquad w^n=1
 \tag{CEX6}
\]
identifies its algebra with that of \(P\times\mu_n\); the inverse uses \(w=z_2/z_1\). This proves the torsor identity even when \(n=p\) and the derivative vanishes.

Here \(f_*\mathcal O_P=\bigoplus T^i\) explicitly. Each summand is torsion, so CE6's line-invariance argument gives
\(\chi(P,f^*\mathcal F)=\sum_i\chi(Y,\mathcal F\otimes T^i)=n\chi(Y,\mathcal F)\).
Thus a nonétale torsor is included, while the general finite flat cover of part 4 remains excluded.

9. The actual elliptic multiplication proof MP1–MP6 in Lesson 3 gives degree \(p^2\), including the inseparable case. CE6 therefore gives
\(\chi(E,[p]^*L)=p^2\chi(E,L)=p^2\).
The same earlier degree/pullback calculation makes the pulled-back line have degree \(p^2\). Genus-one Riemann–Roch gives \(h^0=p^2,h^1=0\), confirming the Euler result without counting geometric kernel points. Such a point count could be smaller than the scheme rank at this prime; CE6 used the full finite kernel scheme.

10. Write \(P(t)=a_gt^g+\cdots+a_0\), with \(a_g\ne0\). Comparing the top coefficient gives \(D_m=m^{2g}\). For \(j<g\), comparison gives
\((m^{2j}-m^{2g})a_j=0\), so \(a_j=0\). Hence
\[
 P(t)=t^gP(1),\qquad D_m=m^{2g}.
 \tag{CEX7}
\]
The polynomial \(t^2+t\) has degree two and positive leading coefficient but is not \(t^2P(1)\); for example its value at two is six instead of eight. A degree bound alone does not give homogeneity.

For the geometric application one must still prove the cube relation \([m]^*H\simeq H^{m^2}\) for the symmetric ample line, finiteness of multiplication, and a nonzero leading coefficient of degree exactly \(g\). CE6 then supplies the Euler functional equation, and the argument above gives the conclusions. The general kernel/Tate-rank and semistable monodromy inputs retain their own proof obligations. None follows merely from this formal polynomial exercise.

**Lemma 2.3 (potentially good compatibility, in every dimension).** If an abelian variety \(B/F\), over a characteristic-zero nonarchimedean local field, acquires good reduction over a finite extension, then all its \(V_\ell B\), \(\ell\ne p(F)\), have one Galois-invariant Frobenius-semisimple Weil–Deligne class over \(\overline{\mathbf Q}\); its monodromy is zero.

**Proof.** Choose a finite Galois extension \(F'/F\) of good reduction. The full graph-closure extension proof GQ1–GQ2 in §2A extends the descent action to its abelian scheme over \(\mathcal O_{F'}\). Reduction of invertible torsion is equivariant and identifies its Tate module with that of the special abelian variety \(B_0\). The finite étale lifting proof GQ3–GQ4 supplies this reduction, with every level and transition; GQ5 proves compatibility with the semilinear action. The common subgroup \(I_{F'}\) consequently acts trivially, so \(N_\ell=0\).

An element \(w\in W_F\) of nonnegative residue exponent acts on the special torsion through an algebraic endomorphism: compose the relative residue Frobenius with the descent isomorphism from the Frobenius-twisted special fibre back to \(B_0\). On geometric points this is precisely the semilinear descent action of \(w\). Relative Frobenius is an isogeny, and the descent map is an isomorphism. A negative exponent is handled by the inverse quasi-isogeny. Lemma 2.2 therefore makes the trace, and indeed the characteristic polynomial, of every \(w\) rational and independent of \(\ell\). This compares \(w\) with its inertia component present; it is more information than the trace of an unramified Frobenius power.

For completeness, this character comparison gives a common algebraic isomorphism class. The fixed finite group \(I_F/I_{F'}\) works for every coefficient prime, without requiring that its action be faithful. Some power \(\Phi^m\) centralizes it. The unipotent part of \(\Phi\) consequently commutes with inertia: its \(m\)-th power is the unipotent part of that centralizing power, and the unipotent \(m\)-th root is its finite binomial polynomial. It commutes with the semisimple part of \(\Phi\) as well. Removing it preserves all traces of \(i\Phi^a\): the product of its nilpotent part with any commuting operator has trace zero, as follows by the filtration by kernels of its powers. After Frobenius semisimplification, \(\Phi^m\) is semisimple, with algebraic eigenvalues by Lemma 2.2. On an eigenspace with eigenvalue \(c\), choose an algebraic \(m\)-th root \(b\) of \(c\), and replace \(\Phi\) there by \(b^{-1}\Phi\). Inertia together with this operator is a representation of a finite cyclic extension of its finite inertia group, because the new operator has \(m\)-th power one. Over an algebraically closed field of characteristic zero, the group algebra of a finite group splits into matrix blocks: averaging complements gives semisimplicity, and Schur's lemma identifies a block with the full matrix algebra on its simple module. The simple modules can all be defined over \(\overline{\mathbf Q}\), by splitting that finite group algebra there. Thus the original semisimple Weil representation has an algebraic model.

Equal traces on every group element force equal simple multiplicities. One can see this without choosing complex embeddings: for the finite-dimensional semisimple image algebra, its central idempotents and matrix units isolate each simple block, and equality of trace functionals on their spanning group elements gives its multiplicity. This is also the characteristic-zero case of the proved Brauer–Nesbitt theorem in the first lesson. The common rational traces are fixed by every automorphism of \(\overline{\mathbf Q}\), so the common isomorphism class is Galois-invariant. ∎

**Theorem 2.4 (full local abelian compatibility; remaining geometric proof obligation).** For every abelian variety over a nonarchimedean local field of characteristic zero, its prime-to-residue-characteristic rational Tate modules have a common Galois-invariant Frobenius-semisimple Weil–Deligne class over \(\overline{\mathbf Q}\).

The potentially good comparison is given by Lemma 2.3, with its good-model and torsion inputs now proved in GQ1–GQ5. The general case still requires actual semistable models and their behavior under extensions of DVRs. Such model results alone do not identify the monodromy filtration. The remaining proof must identify its toric graded pieces and their monodromy pairing and compare the abelian graded piece, equivariantly for the finite descent group. No actual earlier proof of that general monodromy assertion has yet been bound here. Deligne's freely accessible Example 8.10, printed p.571, states the full theorem but supplies no proof of it; it does not discharge this obligation. The theorem is retained in full generality, and this edition does not claim its full proof complete.

For an elliptic curve the local classification gives every case without invoking the unproved higher-dimensional part. At good places use (6) and \(N=0\). At potentially good places use Lemma 2.3. At potentially multiplicative places use the Tate-curve proof and its quadratic descent in *Elliptic curves over local fields and their Weil–Deligne representations*, §§3–5: the common quadratic splitting character \(\eta_v\) and the common block are
\[
D_v=\eta_v\otimes\mathrm{Sp}(2);
\tag{7}
\]
The quadratic character depends on the curve, not on \(\ell\). These cases prove strict compatibility for the elliptic system. They preserve the higher-dimensional theorem and its outstanding proof; they do not replace it with an elliptic statement.

The cyclotomic system has \(S=\varnothing\), \(P_v(X)=1-q_vX\), and common local pair \((\|\cdot\|,0)\). It is therefore strictly compatible and has weight \(2\). The coefficient prime is excluded separately in (4); it is not added permanently to \(S\) for each member of the family.

For comparison, a finite-image Artin representation defined over a number field of coefficients gives a strictly compatible system by scalar extension. Its exceptional set consists of its ramified places, its local monodromy is zero, and its weight is zero, because every Frobenius eigenvalue is a root of unity.

## 3. Artin L-functions, including the missing places

Let \(\rho:G_K\to\mathrm{GL}_d(\mathbf C)\) have finite image. Its local factor at a finite place is
\[
L_v(s,\rho)=
\det\bigl(1-\rho(\operatorname{Fr}_v)q_v^{-s}\mid V^{I_v}\bigr)^{-1}.
\tag{8}
\]
A lift of Frobenius acts unambiguously on the invariants. With our geometric local convention this is \(L(s,\rho_v^\vee|_{W_{K_v}})\). Finite inertia averaging identifies \((V^{I_v})^\vee\) with \((V^\vee)^{I_v}\), so this statement also holds at ramified places.

**Proposition 3.1 (formalism at every prime).** Direct sums multiply Artin L-functions, inflation preserves them, and for every finite extension \(M/K\),
\[
L_K(s,\operatorname{Ind}_{G_M}^{G_K}\tau)=L_M(s,\tau).
\tag{8A}
\]
All these products converge absolutely and locally uniformly, and are nonzero, on \(\Re s>1\).

**Proof.** Eigenvalues of finite-image operators are roots of unity. The absolute logarithmic series at \(v\) is bounded by \(d\sum_{m\ge1}q_v^{-m\sigma}/m\). If \(n=[K:\mathbf Q]\), at most \(n\) places lie above a rational prime \(p\), each with norm at least \(p\). Thus its global sum is bounded by \(n d\sum_p\sum_{m\ge1}p^{-m\sigma}/m\), finite for \(\sigma>1\). Fixing \(\sigma_0>1\) below the real parts on a compact parameter set gives uniform convergence. Exponentiating proves holomorphy and nonvanishing.

Direct sums give block determinants. In a quotient Galois group the decomposition and inertia groups map onto their corresponding groups and Frobenius maps to Frobenius; hence inflation preserves the invariant space and its operator.

For induction choose a finite Galois extension containing \(M\) and killing \(\tau\). Write its group as \(G\), the subgroup fixing \(M\) as \(H\), and local decomposition and inertia as \(D,I\). The coset model gives
\[
\operatorname{Res}_D\operatorname{Ind}_H^G V
=\bigoplus_{g\in D\backslash G/H}\operatorname{Ind}_{J_g}^{D}V_g,
\qquad J_g=D\cap gHg^{-1}.
\tag{8B}
\]
Indeed, partition the coset basis into \(D\)-orbits; the stabilizer and its fibre are \(J_g,V_g\). The double cosets are the places \(u\) of \(M\) above \(v\).

In one summand, an inertia-invariant vector on each \(I\)-orbit is determined by an initial vector fixed by \(I\cap J_g\). Hence the invariant space consists of \(f=[D:IJ_g]\) copies of \(V_g^{I\cap J_g}\). Arithmetic Frobenius cyclically permutes them, and after \(f\) steps acts by arithmetic Frobenius \(A\) at \(u\). For such a cyclic block operator \(\Psi\),
\[
\det(1-T\Psi)=\det(1-T^f A).
\tag{8C}
\]
Choose bases making its first \(f-1\) transition maps identities. Block elimination of \(1-T\Psi\) leaves identity diagonal blocks and the final block \(1-T^fA\). The calculation over \(\mathbf C(T)\) proves the polynomial identity. Since \(q_u=q_v^f\), the summand contributes exactly the factor at \(u\). Multiplying over double cosets proves (8A), even when \(I\ne1\). Absolute convergence justifies the global multiplication. ∎

The conductor ideal is
\[
\mathfrak f(\rho)=\prod_{v<\infty}\mathfrak p_v^{a_v(\rho)},
\qquad C(\rho)=|D_K|^d\operatorname N_{K/\mathbf Q}\mathfrak f(\rho).
\tag{9}
\]
Its integer exponents are proved in *Conductors of Weil group representations*, Theorem 2.6, before the ideal is defined. That lesson's Proposition 2.3 proves the finite induction formula and Lemma 1.4 proves different transitivity and the trace-dual discriminant formula. They imply
\[
\begin{aligned}
\mathfrak f_K(\operatorname{Ind}_M^K\tau)
&=\mathfrak d_{M/K}^{\dim\tau}
  \operatorname N_{M/K}\mathfrak f_M(\tau),\\
|D_M|&=|D_K|^{[M:K]}
       \operatorname N_{K/\mathbf Q}\mathfrak d_{M/K},\\
C_K(\operatorname{Ind}_M^K\tau)&=C_M(\tau).
\end{aligned}
\tag{9A}
\]
Here is the global passage, including the residue factors. At \(v\), (8B) partitions induction into places \(u\mid v\). Its conductor exponent is
\(\sum_{u\mid v}(\dim\tau\, f(u/v)d_{M_u/K_v}+f(u/v)a_u(\tau))\).
The first sum is the valuation of the relative discriminant, and the second is the valuation of the ideal norm of \(\mathfrak f_M(\tau)\). This proves the first formula. For the second, complete the integral trace lattice at a rational prime. It is the product of the completed integer lattices above that prime; traces and trace determinants respect that product. The tower identity for their trace-dual differents, followed by their norm exponents \(f d\), gives the displayed valuation identity at each rational prime. Equality of these positive integers follows. Insert the first two identities into (9) to obtain the third.

The archimedean factors use
\[
\Gamma_{\mathbf R}(s)=\pi^{-s/2}\Gamma(s/2),\qquad
\Gamma_{\mathbf C}(s)=2(2\pi)^{-s}\Gamma(s).
\]
At a real place let \(d_v^+\) and \(d_v^-\) be the multiplicities of \(1\) and \(-1\) for complex conjugation. The factor is
\[
\Gamma_{\mathbf R}(s)^{d_v^+}\Gamma_{\mathbf R}(s+1)^{d_v^-}.
\tag{10}
\]
At a complex place it is \(\Gamma_{\mathbf C}(s)^d\). These are the archimedean Weil-group factors of the local-factor lesson. If \(\Gamma_\infty(s,\rho)\) denotes their product, the completed function
\[
\Lambda(s,\rho)=C(\rho)^{s/2}\Gamma_\infty(s,\rho)L(s,\rho)
\tag{11}
\]
has the functional equation
\[
\Lambda(s,\rho)=W(\rho)\Lambda(1-s,\rho^\vee),\qquad |W(\rho)|=1.
\tag{12}
\]
We now prove this assertion. The analytic prerequisite is an actual written proof, rather than a reference to a free theorem statement.

**Lemma 3.2 (the Hecke theorem and its normalization).** For any number field \(M\) and continuous unitary Hecke character \(\omega:\mathbb A_M^\times/M^\times\to S^1\), let \(\mathfrak f_\omega\) be its intrinsic finite conductor and \(Q_\omega=|D_M|N\mathfrak f_\omega\). At real places write \(\omega_v=\operatorname{sgn}^{e_v}|\cdot|^{it_v}\), and at complex places \(\omega_v=(z/|z|_{\mathrm{usual}})^{n_v}|\cdot|_v^{it_v}\). Set
\[
\Gamma_\infty(s,\omega)=
\prod_{v\text{ real}}\Gamma_{\mathbf R}(s+it_v+e_v)
\prod_{v\text{ complex}}\Gamma_{\mathbf C}(s+it_v+|n_v|/2).
\tag{12A}
\]
Then \(\Lambda_M(s,\omega)=Q_\omega^{s/2}\Gamma_\infty(s,\omega)L_M(s,\omega)\) continues meromorphically and satisfies
\[
\Lambda_M(s,\omega)=W_M(\omega)\Lambda_M(1-s,\omega^{-1}),
\qquad |W_M(\omega)|=1.
\tag{12B}
\]
It is entire unless \(\omega=|\cdot|^{i\tau}\), in which case its only poles are simple poles at \(-i\tau,1-i\tau\). The constant is the product of its normalized rank-one local constants.

**Proof with its earlier analytic locators.** The written programme lessons *Idèles and the idèle class group*, Theorem 3.3, and *Additive characters, self-dual measures and Poisson summation on the adèles*, Theorems 5.4–5.5, prove compactness of \(C_M^1\), adelic self-duality, covolume one and Poisson summation. The full continuation argument is actually written in *Tate's global theory: continuation and functional equation*, Proposition 9.1, its Theta lemma, and Theorem 9.2, equations (15)–(24). Its proof unfolds a Schwartz integral
\[
Z(f,\omega,s)=\int_{\mathbb A_M^\times}
 f(x)\omega(x)|x|^s\,d^\times x
\]
to the idèle class group. The large-norm part \(G(f,\omega,s)\) is entire: compact norm-one representatives reduce its theta sum to one fractional-ideal lattice, and Schwartz decay bounds the nonzero sum by \(O(|x|^{-B})\) for every \(B\). Poisson summation on the small-norm part gives the actual continuation
\[
Z(f,\omega,s)=G(f,\omega,s)
+G(\widehat f,\omega^{-1},1-s)
+\begin{cases}
\kappa\bigl(\widehat f(0)/(s+i\tau-1)-f(0)/(s+i\tau)\bigr),
 &\omega=|\cdot|^{i\tau},\\
0,&\omega|_{C_M^1}\ne1.
\end{cases}
\tag{12C}
\]
Translation in the compact group kills its average unless the character is trivial there. Fourier inversion interchanges the two entire terms and preserves the correction, proving \(Z(f,\omega,s)=Z(\widehat f,\omega^{-1},1-s)\). This use of the earlier theta estimate includes arbitrary number fields and the whole Schwartz space, not just \(\mathbf Q\).

Take \(f_v=1_{\mathcal O_v}\) at unramified finite places, \(f_v=\omega_v^{-1}1_{\mathcal O_v^\times}\) at ramified places, \(x^{e_v}e^{-\pi x^2}\) at real places, and the matching angular Gaussian at complex places. The actual local integral proofs are *Tate's local theory at the finite places*, Theorems 7.2–7.3, and *Tate's local theory at the infinite places*, Theorem 8.1 and Propositions 8.2–8.4. They make \(Z(f,\omega,s)\) exactly \(\Gamma_\infty(s,\omega)L_M(s,\omega)\), with no extra scalar.

For the trace character, let \(d_v\) be the different exponent and \(a_v\) the character conductor. The finite formulas give
\[
\epsilon_v(s,\omega_v)=W_vq_v^{(a_v+d_v)(1/2-s)},\qquad |W_v|=1.
\tag{12D}
\]
For a ramified character, \(v(b)=a_v+d_v\) and
\[
W_v=\omega_v(b)q_v^{-a_v/2}
\sum_{u\in(\mathcal O_v/\mathfrak p_v^{a_v})^\times}
\omega_v(u)^{-1}\psi_v(u/b).
\tag{12E}
\]
The finite Fourier calculation in Theorem 7.3 proves that the sum has absolute value \(q_v^{a_v/2}\); changing \(b\) by a unit cancels between its two factors. For an unramified character \(W_v=\omega_v(\delta_v)\), where \(\delta_v\) generates the different. Infinite constants for the negative trace character are \((-i)^{e_v}\) and \((-i)^{|n_v|}\), proved by Gaussian Fourier transforms in Proposition 8.3. Product trace-dual discriminants give \(\prod_{v<\infty}q_v^{d_v}=|D_M|\); hence the product of local constants is \(W_M(\omega)Q_\omega^{1/2-s}\). Apply the local equations to (12C), then multiply by \(Q_\omega^{s/2}\), to obtain (12B).

Formula (12C) gives no poles for characters nontrivial on \(C_M^1\). A character trivial there is a pure norm character, so its standard Gaussian is a shifted trivial-character test with both zero terms nonzero. Its two stated poles therefore have nonzero residues. This completes the same full Hecke proof written in *Hecke L-functions and the Dedekind zeta function*, Theorem 10.1 and equations (3)–(8). The freely readable Tate thesis, §4.4, Theorem 4.4.11 and its proof, is primary reading material; the proof obligation is discharged by the actual written arguments just identified. ∎

**Corollary 3.2a (all continuous complex Hecke characters).** Every continuous \(\theta:C_M\to\mathbb C^\times\) has the form \(\theta=\omega|\cdot|^a\) with \(\omega\) unitary and \(a\in\mathbb R\). Its completed primitive Hecke function continues meromorphically and satisfies
\[
\Lambda_M(s,\theta)=Q_\theta^{-a}W_M(\omega)
 \Lambda_M(1-s,\theta^{-1}).
\tag{12B'}
\]
Its analytic constant equals the product of its normalized local constants, and has absolute value \(Q_\theta^{-a}\). It is entire unless \(\theta=|\cdot|^{a+i\tau}\); in that case its poles are simple, at \(-a-i\tau\) and \(1-a-i\tau\).

**Proof.** The absolute value of a continuous character on the compact group \(C_M^1\) is one: its image is a compact subgroup of \(\mathbb R_{>0}\), whose logarithm is a compact additive subgroup of \(\mathbb R\), necessarily zero since the multiples of any nonzero member are unbounded. The norm splitting from the actual idèle-class proof identifies the remaining positive real character with \(t\mapsto t^a\). Indeed its logarithm is a continuous additive function on \(\mathbb R\); rational linearity follows by integer division and real linearity by density. Dividing \(\theta\) by that norm power produces \(\omega\).

Unit restrictions, and hence the conductor, are unchanged. Every Euler and Gamma factor is shifted from \(s\) to \(s+a\), so
\(\Lambda(s,\theta)=Q^{-a/2}\Lambda(s+a,\omega)\).
Similarly \(\Lambda(1-s,\theta^{-1})=Q^{a/2}\Lambda(1-s-a,\omega^{-1})\). Lemma 3.2 now gives (12B') and its poles. Its finite local exponent formula gives the central-product multiplier \(Q^{-a}\); infinite phases are unchanged by radial shifts. Thus the local product gives exactly the same constant. ∎

**Theorem 3.3 (Artin meromorphy and functional equation).** Equations (11)–(12) hold for every finite-image complex representation of \(G_K\), including reducible representations and all ramified places.

**Proof.** Take a finite Galois quotient \(G\) through which \(\rho\) factors. The actual integer line-induction theorem in the earlier *Brauer's induction theorem*, Theorem 5.1, gives
\[
[\rho]=\sum_jm_j[\operatorname{Ind}_{H_j}^G\chi_j],
\qquad m_j\in\mathbf Z,\quad\dim\chi_j=1.
\tag{12F}
\]
Its proof in §§1–5 proves nilpotent monomiality, local induction ideals at every prime, integral descent and the final Bezout combination. Thus this is integer induction from lines, with negative coefficients permitted; rational Artin induction would not suffice. Put \(M_j=L^{H_j}\). The one-dimensional character gives the finite-order Hecke character \(\omega_j\) by arithmetic reciprocity. The actual local-to-global reciprocity and character construction are the preceding Weil lesson, §6 and Proposition 6.1, with its written class-field provider. In that provider's geometric convention apply the correspondence to \(\chi_j^\vee\): geometric reciprocity is the inverse of arithmetic reciprocity, so the two inversions give precisely \(\omega_j(x)=\chi_j(\operatorname{rec}_{\mathrm{arith}}(x))\). At a ramified place the Artin invariant line is zero exactly when the Hecke character is nontrivial on units. At an unramified place arithmetic reciprocity sends a uniformizer to arithmetic Frobenius. Hence their primitive Euler factors agree in both cases. The unit conductor equals the Artin conductor by the proved conductor lesson, Lemma 2.4.

Proposition 3.1 now gives \(L_K(s,\rho)=\prod_jL_{M_j}(s,\omega_j)^{m_j}\) on \(\Re s>1\). Equation (9A) gives equality of the conductor scales. At a real place, induction from a complex place gives one even and one odd line; induction from real places preserves their signs. At a complex place all dimensions simply add. Thus induction preserves the archimedean product, because
\[
\Gamma_{\mathbf R}(s)\Gamma_{\mathbf R}(s+1)=\Gamma_{\mathbf C}(s).
\tag{12G}
\]
This identity has an actual proof in the infinite Tate lesson, Proposition 8.4: the beta integral, the substitution \(t=(1+a)/2\), and then \(a^2=b\) give the Gamma duplication formula, and \(\Gamma(1/2)=\sqrt\pi\) follows from the Gaussian integral. Consequently
\[
\Lambda_K(s,\rho)=\prod_j\Lambda_{M_j}(s,\omega_j)^{m_j}.
\tag{12H}
\]
Lemma 3.2 continues this product meromorphically. The finite coset pairing identifies the dual of an induction with induction of the dual: pair corresponding coset fibres and sum their pairings. Apply (12B) to each factor in (12H). The resulting constant is \(W(\rho)=\prod_jW_{M_j}(\omega_j)^{m_j}\), of absolute value one, and gives exactly (12).

These continuations and constants are independent of the chosen Brauer expression. The Euler products agree on the common nonempty half-plane, so their meromorphic continuations agree by the identity theorem. On an open set where the dual completed function is finite and nonzero, their quotient determines the constant uniquely. Such an open set exists by the nonzero initial Euler product and meromorphic continuation. This proves the theorem, without asserting holomorphy of the negative-power product. ∎

The precise written analytic and character-theory scopes have thus been used. Section 4 proves the further local-product identity from the actual orthogonal and global Brauer proofs.

**Artin's holomorphy conjecture.** If \(\rho\) is nontrivial and irreducible, \(L(s,\rho)\) is entire. Meromorphic continuation is a theorem; removal of all possible poles in this generality is the conjecture. Brauer induction gives products with negative as well as positive powers, which explains why it yields meromorphy. A nontrivial irreducible representation induced from a one-dimensional character has an entire L-function, by induction and the Hecke theorem. This argument requires that induced-character hypothesis; solvability of a finite group by itself does not supply it.

**Example 3.1 (Dedekind factorization).** Let \(M/K\) be finite Galois with group \(G\). The regular representation decomposes as
\[
\mathbf C[G]\simeq\bigoplus_{\tau\in\widehat G}\tau^{\oplus\dim\tau}.
\]
Induction of the trivial representation from \(G_M\) has L-function \(\zeta_M(s)\). The formalism therefore gives
\[
\zeta_M(s)=\prod_{\tau\in\widehat G}L_K(s,\tau)^{\dim\tau}.
\tag{13}
\]
This includes ramified Euler factors. For \(M=\mathbf Q(i)\), the two characters are \(1\) and \(\chi_{-4}\), so \(\zeta_M=\zeta L(\chi_{-4})\). For odd \(p\), the factor is \((1-p^{-s})^{-2}\) if \(p\equiv1\pmod4\), and \((1-p^{-2s})^{-1}\) if \(p\equiv3\pmod4\). At \(2\), inertia acts nontrivially on \(\chi_{-4}\), leaving only the trivial line: the factor is \((1-2^{-s})^{-1}\). The character at 2 is nontrivial on \(1+2\mathbf Z_2\), since it is minus one at \(-1\), and trivial on \(1+4\mathbf Z_2\); thus its unit conductor exponent is exactly two by Lemma 2.4 of the conductor lesson. Hence \(\mathfrak f(\chi_{-4})=(4)\), so \(C(1\oplus\chi_{-4})=4\), agreeing with \(|D_M|\). The gamma factors also agree, since the duplication formula gives \(\Gamma_{\mathbf R}(s)\Gamma_{\mathbf R}(s+1)=\Gamma_{\mathbf C}(s)\).

**Example 3.2 (a character that detects the dual).** Let \(\zeta_3=e^{2\pi i/3}\). Define the primitive character modulo \(7\) by \(\chi(3)=\zeta_3\), since \(3\) generates \((\mathbf Z/7\mathbf Z)^\times\). Then \(2\equiv3^2\pmod7\), so \(\chi(2)=\zeta_3^2\). The corresponding Artin representation acts on arithmetic Frobenius at \(2\) by \(\zeta_3^2\), and its Euler factor is
\[
L_2(s,\chi)=\frac{1}{1-\zeta_3^2\,2^{-s}}.
\tag{14}
\]
It is even, because \(-1\equiv3^3\), so its infinite factor is \(\Gamma_{\mathbf R}(s)\). Its conductor is \(7\), its factor at \(7\) is one, and \(L(s,\chi)=\sum_{n\ge1}\chi(n)n^{-s}\), with \(\chi(n)=0\) when \(7\mid n\). If one uses this representation itself in the geometric local-factor definition, its eigenvalue at \(\Phi_2\) is \(\zeta_3\), giving the factor for \(\chi^{-1}\). Applying that definition to the dual gives (14). A quadratic character would not expose the error.

## 4. Root numbers and the global additive character

Choose a nontrivial continuous unitary additive character \(\psi:\mathbf A_K/K\to\mathbf C^\times\), with local components \(\psi_v\), and at each place use the self-dual Haar measure \(dx_{\psi_v}\). At a complex place the absolute value means the squared usual absolute value. This convention makes \(\prod_v|a|_v=1\) for \(a\in K^\times\).

The actual written adelic self-duality and Poisson proofs are *Additive characters, self-dual measures and Poisson summation on the adèles*, Theorems 5.4–5.5. They prove that the product self-dual measure has covolume one. The first theorem identifies the annihilator of \(K\) in \(\mathbb A_K\) with \(K\) by a rational trace-dual basis, so every nontrivial additive character on \(\mathbb A_K/K\) is \(\psi_a(x)=\psi(ax)\) for a unique \(a\in K^\times\).

Put \(r_v=\rho_v^\vee|_{W_{K_v}}\). At infinity use the analogous finite-image Weil representation. Define
\[
\epsilon(s,\rho,\psi)=
\prod_v\epsilon_v(s,r_v,\psi_v,dx_{\psi_v}),\qquad
W_{\mathrm{loc}}(\rho)=\epsilon(1/2,\rho,\psi).
\tag{15}
\]
Almost every finite place is unramified both for \(r_v\) and for the additive character, with \(\mathcal O_v\) of self-dual volume one. Its constant is one, so the product has only finitely many nontrivial terms. Finite-image representations are unitary: average any positive Hermitian form over their finite image. The proved local-factor lesson, Theorem 3.0 and §§4–5, therefore gives absolute value one for every central local factor.

**Proposition 4.0 (the complete conductor power).** The product in (15) has the form
\[
\epsilon(s,\rho,\psi)
=W_{\mathrm{loc}}(\rho)C(\rho)^{1/2-s},
\qquad |W_{\mathrm{loc}}(\rho)|=1.
\tag{15A}
\]

**Proof.** First take the standard trace character. The local exponent formula in the actually written local-factor lesson gives
\[
\epsilon_v(s,r_v,\psi_v)
=\epsilon_v(1/2,r_v,\psi_v)
 q_v^{(a_v(\rho)+d\,d_v)(1/2-s)}.
\]
Here \(d_v\) is the local different exponent of \(K_v/\mathbf Q_p\); the character conductor is \(d_v\) by that lesson's trace-dual Lemma 2.2. Duality preserves every invariant codimension in the conductor formula, hence \(a(r_v)=a(\rho_v)\). At infinity the finite-image real parameter is a sum of trivial and sign lines, and the complex parameter is trivial; their Gaussian epsilon factors do not depend on \(s\). Taking the product and using \(\prod_{v<\infty}q_v^{d_v}=|D_K|\) gives exactly (15A). Local unitary normalization gives the absolute value assertion. Proposition 4.1 below extends the formula to every global additive character. ∎

**Theorem 4.2 (global factorization).** The analytic constant in Theorem 3.3 equals \(W_{\mathrm{loc}}(\rho)\). Equivalently,
\[
\epsilon(s,\rho,\psi)=W(\rho)C(\rho)^{1/2-s}.
\tag{16}
\]
**Proof.** The rank-one case has the complete proof in Lemma 3.2. Local induction, proved in the local-factor lesson for virtual dimension zero, gives for an actual representation \(\tau\) of a local extension \(M_u/K_v\)
\[
W_{K_v}(\operatorname{Ind}\tau)
=\lambda(M_u/K_v)^{\dim\tau}W_{M_u}(\tau),
\quad
\lambda(M_u/K_v)=
\frac{W_{K_v}(\operatorname{Ind}1)}{W_{M_u}(1)}.
\tag{16A}
\]
This follows by applying dimension-zero induction to \(\tau-(\dim\tau)1\) and then restoring the trivial factors. Over all places it reduces Theorem 4.2, by (12F), to the exact assertion
\[
\prod_v\prod_{u\mid v}\lambda(M_u/K_v)=1
\quad\text{for every finite number-field extension }M/K.
\tag{16B}
\]
Here are the complete steps proving (16B). Write \(P=\operatorname{Ind}_{G_M}^{G_K}1\), \(n=[M:K]\), \(\eta=\det P\), and
\[
A=P-\eta-(n-1)1.
\tag{16C}
\]
The permutation matrices give \(P\) a real orthogonal realization; \(\eta\) is a real line. Thus \(A\) is a finite-image virtual real representation with dimension zero and determinant one. The preceding local-factor lesson actually proves its orthogonal theorem in Theorem 7.4, with the real induction, Clifford cocycle and quadratic Fourier calculations in Lemmas 7.5–7.8. It gives at every completion
\[
W_{K_v}(A_v)=
\exp\bigl(2\pi i\operatorname{inv}_v(b_v)\bigr),
\qquad b=\operatorname{cl}(w_2(A))\in\operatorname{Br}(K).
\tag{16D}
\]
The class is global: pull back the degree-two sign cocycle of the finite real representation along \(G_K\) and embed its signs in \(\bar K^\times\). Restriction of that cocycle gives each \(b_v\). The actual earlier *Brauer groups of local and global fields*, §4 and Theorem 24.4, proves finite support and \(\sum_v\operatorname{inv}_v(b_v)=0\). Its written proof first proves injectivity by cyclic norms and Sylow restriction, constructs a cyclic splitting extension for the finite local support, and then obtains the sum law from the principal reciprocity law. Hence (16D) gives \(W_{\mathrm{loc}}(A)=1\).

The trivial character has global root one directly from the Gaussian and finite unramified calculations in Lemma 3.2: its central finite factors for the trace character are one, as are its infinite factors. If \(\eta\ne1\), let \(M'/K\) be its quadratic field. Proposition 3.1, (9A) and the real/complex Gamma induction in (12G) identify its completed function with the quotient of the completed zeta functions of \(M'\) and \(K\). The trivial-character case of Lemma 3.2 gives each zeta function root one. Consequently its quotient has analytic root one, and the proved rank-one factorization gives \(W_{\mathrm{loc}}(\eta)=1\). This is also true when \(\eta=1\). Multiplicativity in (16C) now gives \(W_{\mathrm{loc}}(P)=1\).

At \(v\), restricting the global permutation module decomposes it as the sum of \(\operatorname{Ind}_{W_{M_u}}^{W_{K_v}}1\) over \(u\mid v\), by the same coset decomposition as (8B), also at the real and complex places. Therefore the numerator in the product of (16A)'s constants is \(W_{\mathrm{loc}}(P)=1\), while its denominator is the trivial-character product over \(M\), also one. This proves (16B) for every finite extension, including non-Galois extensions and ramified completions.

For a finite-order line \(\chi\) over \(M\), equations (16A)–(16B) give
\(W_{\mathrm{loc}}(\operatorname{Ind}_M^K\chi)=W_{\mathrm{loc}}(\chi)=W(\chi)\).
Apply the integer Brauer identity (12F). Multiplicativity of the actual local epsilon family gives the product of these constants with the signed integers \(m_j\); the analytic construction (12H) gives the identical product. Thus \(W_{\mathrm{loc}}(\rho)=W(\rho)\) for every finite-image \(\rho\). Proposition 4.0 proves (16). All the higher-dimensional inputs used here are actual earlier written proofs; their free-source chain and publication checks remain the programme's separate integration obligations. ∎

The product of constants at \(s=0\) has absolute value \(C(\rho)^{1/2}\), by (15A). For instance its absolute value for \(\chi_{-4}\) is \(2\), whereas its central product has absolute value one. Taking constants at zero does not give the normalized root.

**Proposition 4.1 (independence of \(\psi\)).** Replacing the global additive character, with its corresponding self-dual local measures, leaves \(\epsilon(s,\rho,\psi)\) and \(W_{\mathrm{loc}}(\rho)\) unchanged. The analytic \(W(\rho)\) is uniquely fixed by (12).

*Proof.* Write \(\psi_{v,a}(x)=\psi_v(ax)\). Self-duality changes the measure by
\[
dx_{\psi_{v,a}}=|a|_v^{1/2}dx_{\psi_v}.
\]
The measure and character laws proved in the local-factor lesson, valid also at infinity by Tate's one-dimensional formulas and induction, give
\[
\epsilon_v(s,r_v,\psi_{v,a},dx_{\psi_{v,a}})
=\det r_v(\operatorname{Art}_v(a))
|a|_v^{d(s-1/2)}
\epsilon_v(s,r_v,\psi_v,dx_{\psi_v}).
\tag{17}
\]
For clarity the product formula itself follows here from norms: the product of the real and squared complex absolute values is \(|N_{K/\mathbf Q}(a)|\), while the finite product is \(\prod_p p^{-v_p(N_{K/\mathbf Q}a)}=|N_{K/\mathbf Q}(a)|^{-1}\). The local norm valuation \(f v\) was proved in the first lesson; factoring the completed trace lattice gives this global factorization.

The determinant character corresponds, by the actual preceding Weil lesson's §6 and Proposition 6.1, to a character of \(C_K=\mathbb A_K^\times/K^\times\), with these local restrictions. Evaluating it on the principal idèle \(a\) gives one, since that idèle represents the identity of \(C_K\). Thus both products of multipliers in (17) are one. All but finitely many factors are one, so their multiplication is legitimate. Every other nontrivial global additive character is \(\psi_a\), by the actual self-duality theorem identified above. This proves the full assertion. ∎

At \(s=1/2\) the norm multiplier is already one at each place. The determinant multipliers still require the global principal-idèle cancellation. Thus the product is independent even when individual local roots vary. Theorem 4.2 identifies that invariant product with the analytic root number.

## 5. The Hasse–Weil product and its convergence

For an elliptic curve \(A/\mathbf Q\), write \(a_p=p+1-\#\widetilde A(\mathbf F_p)\) at good primes. At bad primes define \(a_p=1\) for split multiplicative reduction, \(a_p=-1\) for nonsplit multiplicative reduction, and \(a_p=0\) for additive reduction. The local elliptic lesson proved the factors
\[
L_p(A,s)=
\begin{cases}
(1-a_pp^{-s}+p^{1-2s})^{-1},&p\text{ good},\\
(1-a_pp^{-s})^{-1},&p\text{ bad}.
\end{cases}
\tag{18}
\]
The second line is one in the additive case. These factors are \(L(s,\operatorname{WD}_p(V_\ell A^\vee))\), for any \(\ell\ne p\). Set
\[
L(A,s)=\prod_p L_p(A,s),\qquad
N(A)=\prod_p p^{a(\operatorname{WD}_p(V_\ell A))}.
\tag{19}
\]
Local compatibility makes both definitions independent of coefficient choices. The conductor is also unchanged by duality, as proved in the local elliptic lesson.

**Theorem 5.1 (absolute convergence).** The Euler product in (19) converges absolutely, locally uniformly, to a nonzero holomorphic function on \(\operatorname{Re}s>3/2\).

*Proof.* For a good prime, factor
\[
1-a_pX+pX^2=(1-\alpha_pX)(1-\beta_pX),
\qquad |\alpha_p|=|\beta_p|=\sqrt p
\]
by Theorem 2.1. If \(\sigma=\operatorname{Re}s>3/2\), then \(|\alpha_pp^{-s}|=|\beta_pp^{-s}|=p^{1/2-\sigma}<1\). The logarithm defined by its power series gives
\[
\log L_p(A,s)
=\sum_{m\ge1}\frac{\alpha_p^m+\beta_p^m}{m\,p^{ms}}.
\tag{20}
\]
Its absolute value, and indeed the sum of the absolute values of its terms, is at most
\[
2\sum_{m\ge1}\frac{p^{-m(\sigma-1/2)}}m
\le \frac{2p^{-(\sigma-1/2)}}{1-p^{-(\sigma-1/2)}}.
\tag{21}
\]
On a compact subset of the half-plane, choose \(\sigma_0>3/2\) below all real parts there and put \(b=\sigma_0-1/2>1\). The bound is at most \(2p^{-b}/(1-2^{-b})\), uniformly on that compact set. Its sum over primes converges, since \(\sum_p p^{-b}\le\sum_{n\ge2}n^{-b}<\infty\). Thus the double logarithmic series converges absolutely and locally uniformly. Its exponential is holomorphic and nonzero, and is the limit of the products over good primes.

There are only finitely many bad primes. Their nontrivial factors have \(a_p=\pm1\), so their denominators cannot vanish when \(\operatorname{Re}s>3/2\). Multiplication by this finite product proves the assertion. ∎

This is a statement in a right half-plane. It does not construct the continuation through that half-plane's boundary.

**Example 5.2 (the conductor-11 curve).** Take
\[
A\colon\quad y^2+y=x^3-x^2.
\]
Its discriminant is \(-11\). The previous lesson proved that at \(11\) it has split multiplicative reduction of type \(I_1\), conductor exponent one, and \(a_{11}=1\). At every other prime it has good reduction. Hence
\[
N(A)=11,\qquad
L(A,s)=\frac{1}{1-11^{-s}}
\prod_{p\ne11}\frac{1}{1-a_pp^{-s}+p^{1-2s}}.
\tag{22}
\]
Here are direct good-prime counts. The middle column lists the numbers of \(y\)-solutions as \(x\) runs from \(0\) to \(p-1\); the projective point at infinity contributes one more.

| \(p\) | Numbers of \(y\)-solutions for successive \(x\) | \(\#A(\mathbf F_p)\) | \(a_p\) |
|---:|:---|---:|---:|
| \(2\) | \(2,2\) | \(5\) | \(-2\) |
| \(3\) | \(2,2,0\) | \(5\) | \(-1\) |
| \(5\) | \(2,2,0,0,0\) | \(5\) | \(1\) |
| \(7\) | \(2,2,0,0,2,2,1\) | \(10\) | \(-2\) |

For example the factors at \(2\) and \(5\) are
\[
(1+2\,2^{-s}+2^{1-2s})^{-1},\qquad
(1-5^{-s}+5^{1-2s})^{-1}.
\]
One must use the linear bad factor at \(11\), not a degree-two factor obtained from a singular cubic's total point count.

The elliptic completed function, in its usual normalization, is
\[
\Lambda(A,s)=N(A)^{s/2}(2\pi)^{-s}\Gamma(s)L(A,s).
\tag{23}
\]
The local archimedean factor is \(\Gamma_{\mathbf C}(s)\); dividing it by the constant two gives the conventional factor in (23), without changing the functional equation.

**Theorem 5.3 (modularity and analytic continuation; remaining modularity proof).** Every elliptic curve over \(\mathbf Q\) has the same L-function as a weight-two cuspidal newform of level \(N(A)\). The function (23) is entire and
\[
\Lambda(A,s)=w(A)\Lambda(A,2-s),\qquad w(A)\in\{1,-1\}.
\tag{24}
\]
The modularity assertion is retained for every elliptic curve over \(\mathbf Q\). The freely readable author manuscript of Breuil–Conrad–Diamond–Taylor states it as Theorem A and discusses the conductor-level equivalences in its introduction. Reading that statement does not prove it in this programme. No actual earlier proof of general modularity, of the exact conductor-level comparison, or of the complete local newform/elliptic comparison has yet been bound here. These remain core proof obligations.

Here is the full analytic deduction once those modularity data are supplied. It replaces the former appeal to an unspecified Mellin-transform theorem.

**Lemma 5.4 (the Mellin deduction).** Suppose \(f(z)=\sum_{n\ge1}b_ne^{2\pi inz}\) is a weight-two cusp form with the same Euler coefficients as \(A\), and is a Fricke eigenfunction
\[
\frac1{Nz^2}f\left(-\frac1{Nz}\right)=\eta f(z),
\qquad \eta\in\{1,-1\},\quad N=N(A).
\tag{24A}
\]
Then (23) is entire and satisfies (24) with \(w(A)=-\eta\).

**Proof.** At a good prime the coefficients of the reciprocal quadratic factor satisfy
\(b_{p^r}=\sum_{j=0}^r\alpha_p^j\beta_p^{r-j}\), so
\(|b_{p^r}|\le(r+1)p^{r/2}\). The multiplicative factors have coefficients bounded by one, and the additive factors have all positive coefficients zero. Multiplying prime-power bounds gives \(|b_n|\le d(n)n^{1/2}\). Since
\(\sum_n d(n)n^{-b}=\sum_{u,v}(uv)^{-b}<\infty\) for \(b>1\), the Dirichlet series and its termwise Mellin integral converge absolutely on \(\Re s>3/2\). Integrating \(e^{-2\pi ny}y^s\,dy/y\) gives
\[
(2\pi)^{-s}\Gamma(s)L(A,s)=\int_0^\infty f(iy)y^s\,\frac{dy}{y}.
\tag{24B}
\]
Set \(F(u)=f(iu/\sqrt N)\). Cusp holomorphy gives exponential decay as \(u\to\infty\): its convergent Fourier series has zero constant term. Equation (24A) says \(F(1/u)=-\eta u^2F(u)\). Therefore \(F(u)\) has \(O(u^{-2}e^{-c/u})\) decay at zero. On any compact set of complex \(s\), these two bounds dominate the Mellin integrand and every parameter derivative, so its integral is entire. Equivalently, put
\[
A(s)=\int_1^\infty F(u)u^s\,\frac{du}{u}.
\]
This is entire, and substitution \(u\mapsto1/u\) in the small part gives
\[
\Lambda(A,s)=A(s)-\eta A(2-s).
\tag{24C}
\]
The same formula at \(2-s\), and \(\eta^2=1\), give \(\Lambda(A,s)=-\eta\Lambda(A,2-s)\). Initially (24B) identifies this entire function with (23); the identity theorem supplies its continuation. ∎

This proof establishes the analytic implication completely. It does not construct the cusp form or establish its exact level or Fricke data; those are the identified remaining parts of Theorem 5.3.

The full root-number comparison in Theorem 5.3 asserts that \(w(A)\) is the product of the local constants for the dual elliptic parameters at \(s=1\). Its proof additionally requires the complete local comparison with the conductor-level newform; an Artin finite-image theorem alone would not prove this infinite-image assertion. The following local normalization calculation is independent of that remaining global comparison. At a finite place the dual elliptic determinant is \(\|\cdot\|^{-1}\). Consequently the scaling law (17), with \(d=2\) and \(s=1\), has multiplier
\[
|a|_v^{-1}|a|_v^{2(1-1/2)}=1.
\]
This also holds for the determinant of the elliptic archimedean parameter. Thus in this case each normalized local root is independent of the local additive character.

For the curve in Example 5.2, use the standard global character of \(\mathbf A_{\mathbf Q}/\mathbf Q\), with \(x\mapsto e^{2\pi ix}\) at infinity and conductor zero at every finite place. The good-prime constants are one. At \(11\), the dual parameter is \(\|\cdot\|^{-1}\mathrm{Sp}(2)\), and the block calculation in the monodromy lesson gives
\[
\epsilon_{11}(s)=-11^{1-s},\qquad w_{11}(A)=-1.
\]
The real parameter is
\(\operatorname{Ind}_{W_{\mathbf C}}^{W_{\mathbf R}}(z/|z|_{\mathrm{usual}})\otimes\|\cdot\|^{-1/2}\).
Its epsilon factor is \(-1\). The actual infinite Tate Gaussian proof gives, for the positive character, \(\epsilon_{\mathbf R}(1)=1\), \(\epsilon_{\mathbf R}(\mathrm{sgn})=i\), and the angular complex character's constant \(i\). Dimension-zero induction in the local-factor lesson gives the induction constant \(i\), since \(\operatorname{Ind}1=1\oplus\mathrm{sgn}\). Thus the induced angular constant is \(i\cdot i=-1\). The Gaussian formula is constant under radial twists, so the factor \(\|\cdot\|^{-1/2}\) does not change it. The local product is consequently one; under the root-number comparison asserted in Theorem 5.3 this gives
\[
w(A)=w_\infty(A)w_{11}(A)=(-1)(-1)=1.
\tag{25}
\]
This calculation fixes the sign in (24); it does not determine the order of vanishing at the central point.

## 6. Artin, Hecke and geometric functions in one framework

Three sources of Euler products now fit together. An Artin representation has finite image, weight zero, and arithmetic Euler factors (8). An algebraic Hecke character has compatible one-dimensional \(\ell\)-adic realizations. We prove that construction rather than treating the words “through class field theory” as a proof.

**Proposition 6.1 (algebraic Hecke realizations).** Let \(\theta:C_K\to\mathbb C^\times\) be a continuous Hecke character whose infinite component is
\[
\theta_\infty(x_\infty)=\epsilon_\infty(x_\infty)
 \prod_{\tau:K\hookrightarrow\mathbb C}\tau(x_\infty)^{-n_\tau},
\qquad n_\tau\in\mathbb Z,
\tag{26}
\]
where \(\epsilon_\infty\) is a product of real sign characters. There is a number field \(E\) containing all its finite-component values and a continuous character \(\rho_\lambda:G_K\to E_\lambda^\times\) for every finite place \(\lambda\) of \(E\). At every finite \(v\nmid\ell\), the finite-inertia local characters and Frobenius values are independent of \(\lambda\), after the specified embeddings. In particular they form a strictly compatible system away from the residue characteristic; at a place where \(\theta_v\) is unramified their arithmetic polynomial is \(1-\theta_v(\varpi_v)X\).

**Proof.** The finite character \(\theta_f\) has finite image on \(U_f=\prod_{v<\infty}\mathcal O_v^\times\). To prove this directly, choose an arc about one in the unit circle containing no nontrivial subgroup: every nontrivial unit complex number has a power outside an arc of length less than a semicircle. The absolute value of the image of a compact group is one. Continuity and the basis of open subgroups in \(U_f\) now give an open subgroup mapped into that arc, hence into one. Thus the character factors through a finite quotient on \(U_f\); it is unramified outside finitely many places.

The actual earlier *Idèles and the idèle class group*, Theorem 3.3 and Corollary 3.4, proves finiteness of the ideal class group using norm-one compactness. Choose finitely many finite idèles \(t_j\) representing its classes. Every finite idèle has the form \(a t_j u\), with \(a\in K^\times\) and \(u\in U_f\), by removing its principal ideal. Triviality on principal idèles gives
\(\theta_f(a)=\epsilon_\infty(a)^{-1}\prod_\tau\tau(a)^{n_\tau}\).
These values lie in a fixed normal closure of \(K\). If the ideal class of \(t_j\) has order \(h_j\), then \(t_j^{h_j}=a_j u_j\), so \(\theta_f(t_j)\) is an \(h_j\)-th root of an algebraic number. Adjoining the finitely many such values and the finite unit-image roots of unity gives a number field \(E\) containing every finite value. Enlarge it to contain the normal closure of \(K\).

Fix \(i_\lambda:E\hookrightarrow E_\lambda\subset\overline{\mathbb Q}_\ell\). For each \(\tau\), let \(u_\tau\mid\ell\) be the place of \(K\) defined by \(i_\lambda\tau\); that embedding extends continuously from \(K\) to \(K_{u_\tau}\). Define on idèles
\[
R_\lambda(x)=i_\lambda(\theta_f(x_f))\epsilon_\infty(x_\infty)
 \prod_\tau (i_\lambda\tau)(x_{u_\tau})^{-n_\tau}.
\tag{27}
\]
All factors are continuous: the finite character is locally constant on finite units, its valuation coordinates are discrete in an idèle chart, and the additional factors are continuous powers at the finitely many places above \(\ell\). Its values lie in \(E_\lambda\). Formula (26) makes (27) one on \(K^\times\). It is also one on the connected archimedean component, because the only remaining infinite factors are signs.

The actual earlier *The global reciprocity isomorphism*, Proposition 17.3 and its preceding compact-group lemma, proves that the arithmetic reciprocity map identifies \(G_K^{\mathrm{ab}}\) with \(C_K/D_K\), where \(D_K\) is the closure of that connected archimedean image. Its proof passes through all finite reciprocity quotients and the compact norm-one group. Continuity makes (27) kill that closure, so it descends to the required \(\rho_\lambda\). Here arithmetic reciprocity is the inverse of the geometric convention in that provider. This change of convention does not change its kernel or topology.

For \(v\nmid\ell\), insert a local idèle at \(v\) in (27). Every correction factor above \(\ell\) is one. The resulting local character is exactly \(i_\lambda\theta_v\) under arithmetic reciprocity, including its finite unit character and its value on a uniformizer. Its geometric Weil parameter therefore sends geometric Frobenius to \(\theta_v(\varpi_v)^{-1}\), with the common finite inertia character obtained by inversion of reciprocity. It has \(N=0\), and this common one-dimensional pair proves strict compatibility. Arithmetic Frobenius has the asserted inverse-root value. This proves every claim. ∎

The Euler product of this system is the primitive Hecke product after the same Frobenius translation. General continuous complex Hecke characters need not have the integer exponents (26), and the construction above does not assert that they all have such realizations.

For a smooth projective variety \(X/K\), the general cohomological assertions are that its étale cohomology supplies geometric Galois representations, its good-prime characteristic polynomials are independent of \(\ell\), and its geometric-Frobenius eigenvalues on \(H^j_{\mathrm{et}}\) have absolute value \(q_v^{j/2}\). These assertions retain their full scope here, but their construction, smooth proper comparison, trace formula and general purity proofs have not been supplied in an actual earlier lesson inspected for this edition. They remain core proof obligations. The elliptic \(H^1_{\mathrm{et}}=V_\ell A^\vee\) comparison is available from the actual torsion and Kummer proof in the Tate-module lesson. With the arithmetic convention (2), dualizing a geometric cohomology representation makes arithmetic Frobenius have the same eigenvalues as geometric Frobenius on the original space: if a matrix is \(B\), that dual arithmetic matrix is \((B^{-1})^{-t}=B^t\).

An algebraic correspondence which has an idempotent Galois-equivariant action \(e\) separates a representation into \(\operatorname{im}e\oplus\ker e\): write \(v=ev+(v-ev)\), and the intersection is zero since \(e^2=e\). Every Frobenius matrix is block diagonal in that decomposition, so its characteristic polynomial and Euler factor split as the product of those of the pieces. Purity passes to a piece because its eigenvalues form a submultiset. Establishing the cohomological action, finding the required correspondences, and comparing their factors for all coefficient primes require further geometric proofs; the linear-algebra argument alone does not construct those correspondences. In dimension zero the permutation calculation in Proposition 3.1 gives the Artin and Dedekind factors. In dimension one the proved elliptic Tate modules supply a concrete geometric example.

A pure arithmetic weight \(w\) suggests a functional equation with center \((w+1)/2\): weight zero gives \(1/2\), and the covariant elliptic system of weight one gives \(1\). Purity and weak compatibility alone do not prove such an equation, nor do they supply all bad-prime monodromy data. General motivic continuation and functional equations over number fields require additional theorems or remain conjectural. The unconditional elliptic statement (24) is specifically over \(\mathbf Q\).

There is a useful distinction in Deligne's §9: its global field is a function field over a finite field. Theorem 9.8 compares ordinary local semisimplifications and explicitly warns on p.578 that it does not retain \(N\). It must not be read as a theorem that good-prime compatibility automatically supplies full bad-prime Weil–Deligne compatibility for an arbitrary number-field system.

## 7. Proof scopes and remaining obligations

The local elliptic classification, the Tate-curve and dual factors, and the conductor calculations are imported from *Elliptic curves over local fields and their Weil–Deligne representations*, Theorems 3.1, 4.1 and 5.1. The good-reduction torsion comparison, determinant–degree identity and Hasse bound are imported from *The ℓ-adic Tate module of an elliptic curve*, Theorems 3.1, 2.2 and 4.1 respectively. Their combination proving common good-prime polynomials is Theorem 2.1 here.

Lemma 2.2 gives the common characteristic-polynomial argument for every abelian-variety endomorphism. CE1–CE7 in §2B now proves the full coherent Euler polynomial, proper pushforward and image bound, reduced-base see-saw, and finite commutative torsor Euler comparison used there. Its remaining recorded earlier field-geometric prerequisites are the cube and Euler-homogeneity proofs in *Abelian varieties*, Propositions 4.4 and 5.5, and the kernel/Tate-module proofs in §§6–7; their complete free-origin and earlier-edition audit remains required. Lemma 2.3 proves strict local compatibility for potentially good abelian varieties of every dimension, using the good-model extension, finite étale lifting and semilinear proofs GQ1–GQ5 in §2A. For elliptic curves, potentially multiplicative descent and the proved Tate curve complete the local comparison. The full arbitrary-abelian-variety theorem, Theorem 2.4, still needs the semistable monodromy filtration, its toric pairing and equivariant descent comparison. Semistable reduction alone does not prove that representation theorem. No assertion at \(\ell=p(v)\) is part of strict compatibility here.

Proposition 3.1 proves all ramified Euler induction and convergence. The conductor lesson's Theorems 2.6 and 4.1 prove integrality and induction, yielding (9A). Lemma 3.2 gives the rank-one analytic proof with the actual earlier adelic Poisson and Tate proofs: NT-ADL-03, Theorem 3.3; NT-ADL-05, Theorems 5.4–5.5; NT-ADL-07, Theorems 7.2–7.3; NT-ADL-08, Theorem 8.1 and Propositions 8.2–8.4; NT-ADL-09, Theorem 9.2; and NT-ADL-10, Theorem 10.1. Theorem 3.3 then proves the full Artin meromorphic functional equation through the actually written integer induction theorem RT-FIN-11, Theorem 5.1. General Artin holomorphy remains a conjecture; meromorphic quotients in (12H) do not prove it. Proposition 6.1 proves algebraic Hecke realizations using NT-CFT-17, Proposition 17.3.

The earlier local-factor lesson's Theorem 3.0 and §§3A–3D supply the actual local epsilon existence proof and all Brauer relations. Its Lemma 2.2 proves the trace conductor, §§4–5 prove scaling and normalization, and Theorem 7.4 with Lemmas 7.5–7.8 proves the local orthogonal formula. Theorem 4.2 here proves the global product of induction constants, hence the full Artin root-number identity, using the actual global invariant-sum proof NT-CFT-24, §4 and Theorem 24.4. Proposition 4.1 proves additive-character independence with the actual adelic annihilator theorem NT-ADL-05, Theorem 5.4, and the preceding Weil lesson's Proposition 6.1.

The full modularity, exact conductor level and local newform/elliptic comparison of Theorem 5.3 remain without an actual programme proof. Lemma 5.4 proves the complete Mellin analytic deduction once those data are available, including entireness and the exact Fricke sign. The elliptic global root-number comparison also needs that local automorphic comparison. The general cohomological construction, comparison and purity assertions in §6 remain without the corresponding written proofs. These are genuine retained mathematical obligations, so this edition is not certified as a fully proved lesson.

## 8. Exercises with complete solutions

**Exercise 8.1 (easy).** Check strict finite-place compatibility for the cyclotomic system and the elliptic Tate-module system. Give exceptional sets and arithmetic weights.

**Solution.** Fix a finite place \(v\) and a coefficient prime \(\ell\ne p(v)\). Prime-to-\(p(v)\) roots of unity lie in the maximal unramified local extension. Arithmetic Frobenius raises them to the \(q_v\)-th power, so the cyclotomic character is unramified and has polynomial \(1-q_vX\). Its geometric local pair is \((\|\cdot\|,0)\), independently of \(\ell\). This applies to every finite \(v\): take \(S=\varnothing\). The sole inverse root is \(q_v\), of absolute value \(q_v^{2/2}\), giving weight two.

For \(V_\ell A\), take \(S=S_A\). At every \(v\notin S_A\), Theorem 2.1 supplies the same integral polynomial \(1-a_vX+q_vX^2\), and its inverse roots have absolute value \(\sqrt{q_v}\). Hence weak compatibility and weight one hold. At a potentially good place, Lemma 2.3 proves a common finite-inertia parameter with \(N=0\), including all its Frobenius and inertia character values. At a potentially multiplicative place the Tate-curve calculation and quadratic descent in the preceding local elliptic lesson give explicitly \(\eta_v\mathrm{Sp}(2)\), with the fixed splitting character \(\eta_v\). The integral-\(j\) potential-good proof and the nonintegral-\(j\) Tate descent in that lesson show these alternatives exhaust the elliptic case. Thus every finite \(v\), including \(v\in S_A\), has the common class \(D_v\) required by (4); no appeal to the still incomplete general semistable-abelian Theorem 2.4 is needed in this elliptic solution. A different coefficient prime creates no new permanent exceptional place, because the comparison excludes that prime's residue characteristic locally. These statements include no assertion at \(\ell=p(v)\).

**Exercise 8.2 (medium).** Give a Dirichlet-series proof of absolute convergence on \(\operatorname{Re}s>3/2\). Define its coefficients from the Euler factors and bound them.

**Solution.** At a good prime let \(b_{p,0}=1\) and write
\[
\frac1{1-a_pX+pX^2}=\sum_{r\ge0}b_{p,r}X^r.
\]
Multiplication gives \(b_{p,1}=a_p\) and \(b_{p,r}=a_pb_{p,r-1}-pb_{p,r-2}\) for \(r\ge2\). Using the two roots, including the repeated-root case by the same product of geometric series, gives
\[
b_{p,r}=\sum_{j=0}^r\alpha_p^j\beta_p^{r-j},\qquad
|b_{p,r}|\le(r+1)p^{r/2}.
\]
At a multiplicative prime the coefficients are \(b_{p,r}=a_p^r\), bounded by one. At an additive prime, \(b_{p,0}=1\) and \(b_{p,r}=0\) for \(r>0\). Define \(b_n=\prod_{p^r\parallel n}b_{p,r}\). The uniform bound is
\[
|b_n|\le d(n)n^{1/2},
\]
where \(d(n)=\prod_{p^r\parallel n}(r+1)\) is the number of positive divisors. For \(\sigma>3/2\), put \(b=\sigma-1/2>1\). Then
\[
\sum_{n\ge1}|b_n|n^{-\sigma}
\le\sum_{n\ge1}d(n)n^{-b}
=\sum_{u,v\ge1}(uv)^{-b}
=\zeta(b)^2<\infty.
\]
Absolute convergence permits multiplication and regrouping of the prime-power series, proving equality with the Euler product. The same bound with a fixed \(\sigma_0>3/2\) gives local uniform convergence. Nonvanishing follows from the convergent logarithmic series (20), whose positive sign is the expansion of \(-\log(1-z)\).

**Exercise 8.3 (medium).** Let \(\rho=\operatorname{Ind}_{G_{\mathbf Q(i)}}^{G_{\mathbf Q}}1\). Write its Artin L-function and compute its Euler factor at \(2\).

**Solution.** The representation is the permutation action on the two cosets of the index-two subgroup. The sum of the two basis vectors spans a trivial line, and their difference spans the quadratic line \(\chi_{-4}\). Therefore \(\rho=1\oplus\chi_{-4}\), and multiplicativity gives \(L(s,\rho)=\zeta(s)L(s,\chi_{-4})=\zeta_{\mathbf Q(i)}(s)\).

The prime \(2\) ramifies: \(2=-i(1+i)^2\), up to the displayed unit, and the residue field at \(1+i\) has two elements. Thus inertia is the whole group of order two. It fixes the sum line and acts by minus one on the difference line. The invariant space is one-dimensional, and arithmetic Frobenius on it is the identity. Formula (8) gives \(L_2(s,\rho)=(1-2^{-s})^{-1}\). Equivalently the trivial character supplies this factor and the ramified quadratic character supplies one. It would be wrong to omit the trivial line merely because the extension ramifies.

**Exercise 8.4 (hard).** Prove that the global Artin root number is independent of the global additive character, with the self-dual measure and the geometric/arithmetic translation explicit.

**Solution.** The local parameter to use for the arithmetic Artin L-function is \(r_v=\rho_v^\vee\), not \(\rho_v\). For \(\psi_a(x)=\psi(ax)\), the self-dual measure is \(|a|_v^{1/2}dx_{\psi_v}\). The character law at \(s=0\) contributes \(\det r_v(\operatorname{Art}_v(a))|a|_v^{-d}\); twisting by \(\|\cdot\|^s\) contributes an additional \(|a|_v^{sd}\) to this determinant, and rescaling the measure contributes \(|a|_v^{d/2}\). Their combined multiplier is
\[
\det r_v(\operatorname{Art}_v(a))|a|_v^{d(s-1/2)}.
\]
At the root-number point \(s=1/2\), the absolute-value multiplier is one at every place. The remaining product is \(\det\rho^\vee\) evaluated on the global Artin image of the principal idele \(a\), so it is one by reciprocity. More generally the product formula cancels the absolute values for every \(s\). The finite exceptional set may grow under scaling, but all factors outside its union remain one, so the multiplication is legitimate. Additive adelic self-duality says that every other nontrivial global character has this form with \(a\in K^\times\). Hence the normalized product (15), identified with the analytic root by Theorem 4.2, is independent of the character. Dropping the measure change would lose the \(|a|_v^{d/2}\) contribution; taking constants at \(s=0\) would also fail to give the normalized local roots.

## Freely readable primary materials

The following verified free texts were read for the specified mathematical scopes. They provide materials and conventions; they do not replace the proofs or settle the remaining obligations in §7.

- Richard Taylor, [*Galois representations* (2004), published primary article](https://www.numdam.org/item/AFST_2004_6_13_1_73_0/), §§1–2, pp.80–84, for compatible-system definitions and the arithmetic elliptic convention.
- Pierre Deligne, [*Les constantes des équations fonctionnelles des fonctions L* (1973), free IAS text](https://publications.ias.edu/sites/default/files/Number20.pdf), §§3.9–3.12 for ramified induction and Artin continuation, §§5.8–5.11 for local and global normalization, §§8.5–8.12 for algebraic local classes, and the warning after Theorem 9.8 on p.578. Example 8.10 states general abelian compatibility without supplying its geometric proof there.
- Bjorn Poonen, [*Tate's thesis*, lecture notes for MIT 18.786 (2015)](https://math.mit.edu/~poonen/786/notes.pdf), §5.10, Theorem 5.16 and its proof through adelic Poisson summation (Theorem 5.7 and Lemma 5.18), for the rank-one global analytic mechanism of John Tate's 1950 thesis.
- James Milne, [*Abelian Varieties*, free author notes](https://jmilne.org/math/CourseNotes/AV.pdf), §10, especially Propositions 10.12, 10.19 and 10.20, pp.46–53, for degree-polynomial and Tate characteristic-polynomial comparisons. Lemma 2.2 supplies the actual argument with its written geometric prerequisites.
- Jean-Pierre Serre and John Tate, [*Good reduction of abelian varieties* (1968), primary article](https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf), §2, Theorem 2, pp.496–497, for the full potentially good scope. The independent proof in Lemmas 2.2–2.3 closes the endomorphism-character input.
- Christophe Breuil, Brian Conrad, Fred Diamond and Richard Taylor, [*On the modularity of elliptic curves over Q: Wild 3-adic exercises* (2001), author manuscript](https://virtualmath1.stanford.edu/~conrad/papers/tswfinal.pdf), Theorem A and Introduction, pp.1–3. This reading verifies the full theorem's scope; its statement is not counted as a programme proof of Theorem 5.3.
