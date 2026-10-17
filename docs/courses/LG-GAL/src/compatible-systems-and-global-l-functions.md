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

**Proof.** The normalized cube, symmetric ample existence, multiplication degrees, compatible Tate rank and all isogeny/nonisogeny integral determinant comparisons are proved in §2D, CU4–CU11. CE1–CE7 in §2B proves the multivariable Euler polynomial, proper-image degree bound and finite-flat Euler comparison; EH6–EH7 in §2C proves all-field Euler homogeneity and ample positivity. Here are the polynomial interpolation and root-valuation comparison steps.

Extend the ground field to its algebraic closure. Choose a symmetric ample bundle \(H\). Define \(\delta(f)=\deg(f)\) for isogenies, and zero for other endomorphisms. Then
\[
\delta(f)=\frac{\chi(B,f^*H)}{\chi(B,H)}.
\tag{6B}
\]
For an isogeny this is the full finite commutative torsor proof CE6, applied in CE7. Otherwise factor \(f\) through its closed image, whose dimension is less than \(g\) by CU11. The proved higher-image Euler formula and proper-image degree bound CE4 show that \(\chi(B,(f^*H)^a)\) has degree less than \(g\) in \(a\). The all-field homogeneity proof EH6 says it is \(a^g\chi(B,f^*H)\), so its coefficient is zero. The denominator in (6B) is positive by EH7.

For fixed \(f,h\), pull the normalized cube CU5 back along \((nf+h,f,f)\). It says that the classes of \((nf+h)^*H\) have constant second difference; they are quadratic polynomials in \(n\) with values in the rational Picard group. The full multivariable Euler polynomial CE2 has total degree at most \(g\). Formula (6B) therefore makes \(\delta(nf+h)\) a rational polynomial of degree at most \(2g\). Moreover \(\delta(nf)=n^{2g}\delta(f)\), by CU8.

These assertions extend \(\delta\) to \(\operatorname{End}(B)\otimes\mathbf Q\) by \(\delta(f/n)=n^{-2g}\delta(f)\), independently of the denominator. They make it a homogeneous polynomial function of degree \(2g\) on every finite-dimensional subspace. To check the last assertion, choose coordinates on such a subspace and interpolate in each coordinate at \(2g+1\) distinct rational values. The line-degree bound produces a polynomial in all coordinates. Substituting arbitrary rational affine lines forces its total degree to be at most \(2g\); homogeneity forces its nonzero terms to have degree \(2g\). Multiplicativity \(\delta(fh)=\delta(f)\delta(h)\) holds: degrees multiply for isogenies, and a composition containing a map with smaller-dimensional image again has smaller-dimensional image. Polynomial interpolation extends this identity after any extension of the rational coefficient field.

Set \(P_u(T)=\delta(T-u)\). Its leading coefficient is \(\delta(1)=1\), and its degree is \(2g\). If \(a_i\) are its roots, multiplicativity after scalar extension gives, for any \(F\in\mathbf Q[T]\),
\[
\delta(F(u))=\prod_{i=1}^{2g}F(a_i).
\tag{6C}
\]
Indeed, factor \(F(T)=c\prod_j(T-b_j)\), apply multiplicativity and homogeneity to \(F(u)\), and interchange the two finite products. The even degree \(2g\) removes the possible sign.

For an isogeny \(h\), CU10 proves that its geometric \(\ell\)-primary point kernel has order \(\ell^{v_\ell(\deg h)}\), for \(\ell\ne\operatorname{char}k\). Its proof includes the entire finite scheme length: after a separable field factor splits, the purely inseparable factor contributes its full characteristic-power local length. The exact torsion sequence (CU24) and integral Smith computation (CU25) give the determinant index, using the compatible integral Tate bases from CU9.

The \(\ell\)-primary point kernel is the kernel on \((\mathbf Q_\ell/\mathbf Z_\ell)^{2g}\). Diagonalizing the integral map \(T_\ell h\) by the DVR module theorem identifies this kernel with its finite lattice cokernel. Consequently
\[
|\delta(h)|_\ell=|\det(T_\ell h)|_\ell.
\tag{6D}
\]
For a nonisogeny both sides are zero: its positive-dimensional reduced kernel has nonzero rational Tate module. CU9–CU11 supply the Tate ranks,the full finite-kernel length comparison and the nonzero Tate kernel for a nonisogeny. Thus (6D) applies to every \(F(u)\) with integral \(F\).

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

These give the Euler comparison and the lower-image bound in Lemma 2.2 directly in this lesson. EH6–EH7 supplies the homogeneous Euler polynomial and positive denominator; CU4–CU11 below supplies the normalized cube,symmetric ample existence,multiplication degrees,Tate ranks and full integral determinant comparison. CE1–CE7 alone supplies an Euler polynomial,and EH1–EH6 supplies its additional homogeneity argument. Theorem 2.4 still requires its full semistable,toric,monodromy-pairing and finite descent proofs.

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

For the geometric application, CU5 and CU7–CU8 prove the cube relation \([m]^*H\simeq H^{m^2}\), the existence of a symmetric ample line and finiteness of multiplication. EH6–EH7 prove a nonzero Euler leading coefficient of degree exactly \(g\). CE6 supplies the Euler functional equation used above. CU9–CU11 supply the general kernel and Tate-rank inputs. These conclusions use the geometric proofs beyond this formal polynomial exercise. The general semistable models, pairing and finite descent in Theorem 2.4 remain separate requirements.

### 2C. Euler homogeneity in every characteristic

Let \(A/k\) be an abelian variety of dimension \(g\), and let \(L\) be any line bundle. We prove
\[
 \chi(A,L^n)=n^g\chi(A,L)\qquad(n\in\mathbf Z).
 \tag{EH1}
\]
Here \(n^0\) is the constant polynomial one, including at zero. The argument covers arbitrary ground fields and does not assume projectivity of \(A\). We also prove positivity for any ample line already given.

The actual earlier proofs used are CE1–CE6 for proper Euler polynomials, families and finite commutative torsors; GQ1 for normalization, dimension and group components; Lesson 3, SF1–SF3 and Lesson 1, EA1–EA18, for standard smooth/étale charts and their flatness; Lesson 3, CG4 and PF1–PF9, for projective Chow covers and properness; FC10 and FC16 for flat-family cohomology and its marked unit; and Lesson 8, NM1–NM2, for regular local rings and the flat regular-fibre test. We write the finite-coefficient and closed-point steps, rather than treating spreading as an omitted theorem.

#### 2C.1. Frobenius gives homogeneity in positive characteristic

**EH1.** Formula (EH1) holds in characteristic \(p>0\).

*Proof.* Coherent cohomology commutes with a field extension: tensor the finite affine Čech complex with the field and use exactness. The dimensions over the new field are the old dimensions. We may therefore extend \(k\) to an algebraic closure and assume it perfect.

For a finite-type \(k\)-algebra \(B\), its finitely many algebra generators \(x_i\) give a finite spanning list over its \(p\)-power subring:
\[
 B=\sum_{0\le a_i<p}B^p\,x_1^{a_1}\cdots x_r^{a_r}.
 \tag{EH2}
\]
To verify this, write each exponent as \(pb_i+a_i\), and each scalar as a \(p\)-th power using perfectness. Relations do not obstruct the spanning assertion. Thus absolute Frobenius is finite on each affine; its inverse image of an open is that same open, since a prime contains \(b^p\) exactly when it contains \(b\). It is surjective on points.

We compute its generic degree. If \(F/k\) is a finitely generated field of transcendence degree \(g\), take a transcendence basis and put \(E=k(t_1,\ldots,t_g)\). The extension \(F/E\) is finite, of some degree \(d\). Polynomial exponent residues show that the monomials \(t^{\mathbf a}\), \(0\le a_i<p\), are a basis over the rational function field in the \(t_i^p\): independence follows by collecting distinct exponent residues, and the spanned finite-dimensional domain is a field and hence contains every rational function. Consequently
\[
 [E:E^p]=p^g,\qquad [F^p:E^p]=[F:E]=d,\qquad
 [F:F^p]=p^g .
 \tag{EH3}
\]
The middle equality uses the Frobenius field isomorphism; the last cancels \(d\) in the two degree computations of \(F/E^p\). No separability of \(F/E\) is required.

Let \(q:A^{(p)}=A\times_{k,F_k}k\to A\) be the projection, and let \(F_{A/k}:A\to A^{(p)}\) be relative Frobenius. On rings its map is \(b\otimes c\mapsto b^pc\). Perfectness makes \(q\) an isomorphism of underlying schemes, semilinear for the scalar automorphism \(c\mapsto c^p\). Absolute Frobenius factors as \(qF_{A/k}\). Naturality of the group operations makes relative Frobenius a group homomorphism. It is finite and surjective by the preceding affine calculation, and (EH3) gives degree \(p^g\). Thus it is an isogeny. CE6 proves its finite flat torsor property and Euler comparison, with its entire possibly nonreduced kernel.

The line \(q^*L\) has the same cohomology dimensions as \(L\), since twisting scalars by a field automorphism preserves a vector-space basis. Absolute Frobenius raises every transition unit of a line to its \(p\)-th power. Hence
\[
 F_{A/k}^*q^*L\simeq L^p,\qquad
 \chi(A,L^{pn})=p^g\chi(A,L^n)\quad(n\in\mathbf Z).
 \tag{EH4}
\]
The second assertion applies CE6 to \((q^*L)^n\), also for negative \(n\). By CE2, \(P(n)=\chi(A,L^n)\) is a rational polynomial of degree at most \(g\). Equation (EH4) is a polynomial identity, since it holds on all integers. The coefficient of \(T^j\) for \(j<g\) is multiplied by \(p^j-p^g\), a nonzero rational number, so is zero. Thus \(P(T)=\chi(A,L)T^g\). Field base change returns the same conclusion over the original, possibly imperfect, field. \(\square\)

#### 2C.2. Finite equations, gluing and smooth charts descend

**EH2 (finite-coefficient descent).** A separated finite-type scheme over a characteristic-zero field, a finite list of morphisms and identities between such schemes and their finite products, and a finite list of line bundles can be defined over one finitely generated subring of that field. Closed projective presentations and a finite covering by standard smooth charts, when supplied, can be preserved.

*Proof.* Every affine chart is a quotient of a finite polynomial algebra by a finitely generated ideal. Algebra maps specify images of finitely many generators. Equality of two such maps is equality on those generators. An equality modulo an ideal has a finite witness expressing its difference as a polynomial combination of the finite relation list. Only finitely many field coefficients enter each of these data.

We give the open-cover details as well. Choose a finite affine cover and all of its finite intersections; they are affine because the scheme is separated. An affine intersection maps as a quasi-compact open into each larger chart. Choose finitely many principal opens of the larger chart contained in that intersection and covering it. On them the ring maps are localization isomorphisms. Record their inverse maps and the finitely many identities on algebra generators. Their functions generate the unit ideal in the intersection ring; record an actual finite expression for one. These finite equations ensure, after descent, that the map is still an isomorphism onto the specified open union.

Record also the affine fibre-product identifications of intersections and the triple-overlap cocycles. There are finitely many indices. Their maps, inverse identities and unit-ideal cover expressions again use finitely many coefficients. The descended affine charts consequently glue with exactly those overlaps. The diagonal is still closed: on a pair of affine charts its ring map to the intersection ring is surjective. That ring has a finite algebra generator list; record expressions of each generator in the image of the two chart rings. These expressions preserve surjectivity after descent, and hence separatedness.

For a morphism, refine each source affine by finitely many principal opens whose images lie in target affines. They cover because the original inverse images do; a unit-ideal expression in the source records the cover. Specify the ring maps and their overlap equalities. The same procedure preserves a finite list of morphism equalities, including group laws on finite products. A line bundle is specified on a finite principal refinement by its transition units, their inverses and cocycles. Recording these data gives an actual invertible sheaf on the model, with no choice needed separately for its integer powers.

If a scheme is supplied as a closed subscheme of projective space, use its finite homogeneous ideal to define that model. PF1–PF6 prove the scalar-extension and affine-chart identities. The morphism construction just given applies to these charts and preserves maps to or from it.

Finally SF1–SF3 give standard smooth charts with presentations
\[
 R[T_1,\ldots,T_g,Z_1,\ldots,Z_c]_{h\Delta}/(f_1,\ldots,f_c),
 \qquad
 \Delta=\det\left(\frac{\partial f_i}{\partial Z_j}\right)
       \text{ invertible}.
 \tag{EH5}
\]
Include the given chart isomorphisms, their cover expressions and the displayed relations among the finite data. The same presentation after descent is étale over \(R[T_1,\ldots,T_g]\), by the square-zero Jacobian algorithm and the full étale criterion EA1–EA18. It is flat over that polynomial base and hence over \(R\), and its geometric fibres have the same standard smooth presentations.

Adjoin all the finitely many coefficients and inverse scalar coefficients used above to \(\mathbf Z\). The result is a finitely generated domain \(R\) inside the original field. Every recorded equality has its polynomial witness over this ring, not merely an unverified equality after extending to the field. Adding finitely many data or inverting one further nonzero scalar preserves finite generation. This proves the assertion. \(\square\)

#### 2C.3. A proper model without a projectivity assumption

**EH3.** In EH2, a proper integral scheme can be given a proper model after enlarging the finite coefficient ring and inverting a nonzero element.

*Proof.* Apply the actual projective Chow modification CG4 in Lesson 3 over the original field. It supplies a projective scheme \(Z\) and a proper surjective map \(Z\to X\). Spread the separated scheme \(X\), a closed projective presentation of \(Z\), and that map by EH2. Thus
\[
 \pi:Z_R\longrightarrow X_R
 \tag{EH6}
\]
has projective source over \(R\) and separated target over \(R\). The proper-source graph factorization CG3 makes \(\pi\) proper. Its generic fibre is surjective: failure at a point would persist after the faithful field extension to the original field, contrary to the given surjectivity.

Here is the scalar-removal argument. If a quasi-compact \(R\)-scheme \(V\) has empty fibre over \(\operatorname{Frac}R\), cover it by finitely many affines \(\operatorname{Spec}D_i\). In each localized zero ring, \(1/1=0\); therefore some nonzero \(a_i\in R\) kills one in \(D_i\). Inverting the product makes \(V\) empty. Apply this to the open
\(X_R\setminus\pi(Z_R)\). It is open because \(\pi\) is proper, and is quasi-compact because the model is Noetherian. Its generic fibre is empty. After one such localization, \(\pi\) is surjective.

A surjective proper map remains surjective under every base change: its nonempty finite-type field fibres stay nonempty after any field extension, since field tensor is faithful. For an arbitrary base change \(T\), the inverse image in \(Z_T\) of a closed subset \(C\subset X_T\) is closed and has the same image in \(T\) as \(C\). That image is closed because \(Z_R/R\) is proper. Hence \(X_R/R\) is universally closed. It is already separated and of finite type by EH2, so it is proper. No statement that the model itself is projective was needed. \(\square\)

#### 2C.4. Spreading the abelian scheme and its line

**EH4.** For an abelian variety in characteristic zero and a line on it, the preceding construction can be localized to a proper smooth commutative group model with geometrically integral fibres of dimension \(g\), carrying that line.

*Proof.* In EH2 include a finite standard smooth cover of the original variety, its origin, addition, inverse and all group identities. Use EH3 to retain properness, enlarging the coefficient ring for the Chow cover if necessary. These are finitely many additional data, so all earlier presentations survive. The charts (EH5) make the model flat.

We spell out their geometric-fibre regularity. Over an algebraically closed residue field, a closed point has that residue field by the finite-type field lemma. Its map to affine \(g\)-space is the point with its \(T_i\)-values. The local ring of affine space there is regular of dimension \(g\): its maximal ideal is generated by those \(g\) coordinate differences; their prime chain and the dimension formula GQ1 give the dimension. The local fibre of the étale chart is the residue field, by EA1–EA18. The flat regular-fibre test following NM2 makes the local ring at the chosen point regular. It is a domain by NM1.

The geometric fibre is reduced: a nonzero nilpotent ideal in a finite-type Noetherian affine chart would have nonempty support containing a closed point, where the local ring just proved to be a domain has no nilpotents. By GQ1 its irreducible group components are disjoint open and closed.

It remains to make every geometric fibre connected. Let \(K_0=\operatorname{Frac}R\). The generic unit section is a basis of \(H^0(X_{K_0},\mathcal O)\): after the faithful extension to the original ground field, this is the actual proper-geometrically-integral constants proof FC20. Field base change and faithful tensor detect that the unit already is a basis over \(K_0\). Apply the actual marked-section argument FC16 at this generic base point. After one nonzero scalar localization,
\[
 \mathcal O_R\xrightarrow{\ \sim\ }p_*\mathcal O_{X_R}
 \quad\text{with its unit basis after every base change}.
 \tag{EH7}
\]
No vanishing of fibre \(H^1\) is required. Thus every geometric fibre has a one-dimensional constant ring. It is nonempty and connected: a disconnection would give a nontrivial idempotent global function. The disjoint-component result above now makes it irreducible; reducedness makes it integral.

Its dimension is \(g\). Any nonempty chart of this integral geometric fibre is étale over affine \(g\)-space. Its image is open by EA14, hence dominant. The generic residue extension is finite algebraic by the étale field calculation. GQ1 then makes its function-field transcendence degree, and its dimension, equal to \(g\). This applies to every fibre. The group identities and the line bundle were already preserved by EH2. We have therefore obtained the asserted abelian scheme and line over the localized domain. \(\square\)

#### 2C.5. A positive-characteristic closed point really exists

**EH5.** Every field finitely generated as a \(\mathbf Z\)-algebra is finite. Consequently every nonzero finitely generated \(\mathbf Z\)-algebra has a closed point with finite residue field.

*Proof.* Recall the finite-type field lemma, with its algebraic reason. A field finitely generated over a field \(\kappa\) is finite over a polynomial subalgebra by normalization GQ1. If a field is integral over a domain, that domain is a field: a monic equation for \(a^{-1}\), multiplied by a suitable power of \(a\), expresses \(a^{-1}\) in the domain. A polynomial ring is a field only when it has no variables. Thus the extension of \(\kappa\) is finite.

Now let \(K=\mathbf Z[\alpha_1,\ldots,\alpha_r]\) be a field. If its characteristic is \(p>0\), the preceding lemma over \(\mathbf F_p\) makes it finite. If its characteristic were zero, it would also be finitely generated as a \(\mathbf Q\)-algebra and hence be a number field. Choose a nonzero integer \(D\) such that every \(D\alpha_i\) is integral over \(\mathbf Z\). Such a \(D\) is obtained by clearing the finitely many coefficients of their monic rational equations and scaling their roots. Hence
\[
 \mathbf Z[\alpha_1,\ldots,\alpha_r]\subset
             \mathcal O_K[1/D].
 \tag{EH8}
\]
Choose a rational prime \(p\) not dividing \(D\), for example a prime factor of \(1+|D|\) when needed. If \(1/p\) belonged to the ring on the right, \(D^a/p\) would be integral over \(\mathbf Z\) for some \(a\). A rational number integral over \(\mathbf Z\) is an integer: in a reduced fraction, multiplying its monic equation by the denominator power forces that denominator to divide its coprime numerator. But \(D^a/p\) is not an integer. This contradicts that \(K\) is a field. Thus characteristic zero is impossible.

Finally any nonzero ring has a maximal ideal by the prime/maximal-ideal existence argument. Its residue field is still finitely generated as a \(\mathbf Z\)-algebra, and hence is finite by what we just proved. This applies after every finite coefficient enlargement and every nonzero scalar localization made above. \(\square\)

#### 2C.6. Transfer to characteristic zero, at every integer power

**EH6.** Formula (EH1) holds over every field, for every abelian variety and every line bundle, in full dimension.

*Proof.* EH1 proves positive characteristic. In characteristic zero use the model \(p:X_R\to\operatorname{Spec}R\) and line \(M\) of EH4. This base is nonempty and connected, being the spectrum of a domain. EH5 gives a closed point \(s\) of characteristic \(p_s>0\), with finite residue field. Its fibre is an abelian variety of the same dimension \(g\).

For each integer \(n\), the line \(M^n\) is flat over the base: the model is flat and the line is locally free. The actual family complex FC10, or CE3's Euler consequence, makes its fibre Euler characteristic locally constant and therefore constant on this connected base. Field base change at the generic point then gives
\[
 \chi(A,L^n)=\chi(X_s,M_s^n)
      =n^g\chi(X_s,M_s)=n^g\chi(A,L).
 \tag{EH9}
\]
The middle equality is EH1. The same fixed closed point works for every integer \(n\): every tensor power is already a line on the one fixed model, and Euler constancy does not require a new shrinking for each power. This avoids an intersection of infinitely many chosen base opens. The argument includes negative powers and the zeroth power, so proves (EH1) as stated. \(\square\)

#### 2C.7. Positivity for ample lines and the exact remaining scope

**EH7.** If \(H\) is an ample line on an abelian variety, then
\[
 \chi(A,H)>0,\qquad
 \chi(A,H^n)=n^g\chi(A,H).
 \tag{EH10}
\]
The Euler polynomial therefore has degree exactly \(g\) and positive leading coefficient.

*Proof.* Use the usual ample-line convention on a proper variety: some positive power \(H^a\) is the hyperplane pullback of a closed projective immersion. For this immersion the actual Serre-vanishing proof PF8–PF9 in Lesson 3 gives no positive cohomology of \(H^{am}\) for all sufficiently large \(m\). It has a nonzero section: choose a projective coordinate not identically zero on the nonempty integral variety and raise it to the \(m\)-th power. Thus its Euler characteristic is positive. EH6 gives
\[
 0<\chi(A,H^{am})=(am)^g\chi(A,H),
 \tag{EH11}
\]
which proves positivity and the asserted polynomial degree. No cube or multiplication-degree identity was used. \(\square\)

EH6–EH7 supplies the Euler homogeneity and positive denominator used in Lemma 2.2. CU4–CU11 below supplies the normalized cube,symmetric ample existence over the original field,all multiplication degrees,and the kernel/Tate determinant comparison. The general semistable comparison,toric monodromy pairing and finite descent in Theorem 2.4 remain separate requirements.

Free primary comparisons are the Stacks project authors' [Frobenius constructions](https://stacks.math.columbia.edu/tag/0CC6), [finite-presentation descent](https://stacks.math.columbia.edu/tag/01ZM) and [finite-type arithmetic rings](https://stacks.math.columbia.edu/tag/00FZ). The field degree, finite equations, proper-cover and closed-point arguments needed here have their proofs above; these references do not replace them.

#### 2C.8. Graded exercise: Frobenius, finite models and Euler homogeneity

This exercise is worth **100 points**. Use the actual proofs in §§2A–2C and the earlier programme proofs identified there. Distinguish a finite calculation from the general theorem it illustrates.

**(a) Function-field degrees (12 points).** Over a perfect field \(k\) of characteristic \(p\), give a basis of \(k(t_1,\ldots,t_g)\) over its \(p\)-power subfield. In the purely inseparable example \(F=\mathbf F_p(u)\), \(E=\mathbf F_p(u^p)\), compute all four degrees in the two towers over \(E^p\). Explain why imperfect constants prevent the same absolute-Frobenius degree count: take \(k=\mathbf F_p(s)\), \(F=k(t)\).

**(b) Relative Frobenius and line bundles (10 points).** Explain why absolute Frobenius need not be a \(k\)-morphism, even for perfect \(k\). Write the relative-Frobenius ring map and the pullback of line transition functions. Identify precisely which previously proved statement makes its Euler comparison valid when its kernel is nonreduced.

**(c) The polynomial equation (10 points).** If \(P\in\mathbf Q[T]\) has degree at most \(g\) and \(P(pT)=p^gP(T)\), determine \(P\). Treat \(g=0\), \(T=0\) and negative integers. Show why the degree bound and integer-valuedness alone do not imply this equation, using \(P(T)=\binom T2\).

**(d) Finite equations and smooth charts (10 points).** Describe the finite witnesses needed to descend an affine overlap and a line-bundle transition. For
\[
 B=R[t,z,w]/(z^2-t,\;2zw-1)
\]
show that \(\operatorname{Spec}B\to\mathbf A^1_R\) is étale and flat. What happens to this chart over a field of characteristic two? Explain why a chart that disappears does not by itself make a descended covering invalid.

**(e) Removing an empty generic fibre (10 points).** Let
\[
 V=\operatorname{Spec}\mathbf Z[x]/(6x,\;1-3x).
\]
Find a nonzero integer that kills one in its coordinate ring, determine that ring, and give a localization making \(V\) empty. Prove the corresponding assertion for any quasi-compact scheme with empty generic fibre over a domain.

**(f) Proper covers (10 points).** Prove that a separated finite-type \(R\)-scheme with a proper surjective cover by a proper \(R\)-scheme is proper. Include arbitrary base changes. Show that the surjectivity condition is necessary by considering a point mapping to the affine line over a field.

**(g) The marked unit and shrinking (10 points).** Over \(R=\mathbf Z[1/6]\), consider the complex
\[
 C=[\,R^2\xrightarrow{(0,\;5)}R\,]
\]
in degrees zero and one, with marked cycle \(e_1\). Compute its cohomology and its fibre at five. Give an open on which the marked cycle is a basis in degree zero after every base change. Explain the role of actual cycles in EH4 and why nonzero higher cohomology is not an obstruction to the marked-section argument.

**(h) A finite residue field (10 points).** Exhibit a closed point of
\[
 R=\mathbf Z[1/30,t]/(t^2-2)
\]
with residue field \(\mathbf F_7\). Reproduce the denominator argument ruling out characteristic-zero fields finitely generated as \(\mathbf Z\)-algebras. Explain why inverting infinitely many different primes is outside that argument.

**(i) One model, every integer power (10 points).** Explain why the one closed point in EH6 works for all integers without infinitely many shrinkings. If \(g=3\) and \(\chi(A,H)=2\), compute \(\chi(A,H^{-2})\) and \(\chi(A,\mathcal O_A)\). Prove positivity for a given ample line, specifying which existence claim this does not supply.

**(j) Image dimension (8 points).** Let \(f:A\to B\) be a morphism of proper abelian varieties, with \(g=\dim A\), and let \(L\) be any line on \(B\). If \(\dim f(A)<g\), prove \(\chi(A,f^*L)=0\). For an isogeny of degree \(N\), state the Euler formula, including inseparable isogenies. Explain why these conclusions do not yet supply the normalized cube or the general Tate-module rank.

**Complete solution.**

**(a)** The basis is
\[
 \{t_1^{a_1}\cdots t_g^{a_g}:0\le a_i<p\}.
 \tag{EHX1}
\]
A polynomial relation over \(k(t_1^p,\ldots,t_g^p)\) becomes, after clearing denominators, a relation among disjoint exponent-residue classes. All coefficients vanish. The span is closed under multiplication, finite-dimensional over that field and a domain; multiplication by any nonzero element is injective and therefore surjective, so it contains that element's inverse. It is consequently the entire rational function field. The rank is \(p^g\).

In the specified one-variable example,
\[
 \begin{gathered}
 E^p=\mathbf F_p(u^{p^2}),\qquad F^p=E,\\
 [F:E]=p,\quad [E:E^p]=p,\quad
 [F^p:E^p]=p,\quad [F:F^p]=p,\quad [F:E^p]=p^2.
 \end{gathered}
 \tag{EHX2}
\]
Thus the auxiliary degree \(d=p\) cancels just as in EH3; a separability assumption on \(F/E\) would exclude a valid example. With imperfect \(k=\mathbf F_p(s)\), one has
\[
 F^p=\mathbf F_p(s^p,t^p),\qquad [F:F^p]=p^2.
 \tag{EHX3}
\]
The two-variable monomial-basis argument proves the last degree. Here the relative dimension is one. The extra factor comes from constants; EH1 first extends the ground field to an algebraic closure and preserves cohomology dimensions. It never inserts this absolute degree into a relative isogeny formula over imperfect constants.

**(b)** A \(k\)-morphism must fix scalar functions, whereas absolute Frobenius sends \(c\) to \(c^p\). Perfectness makes this scalar map an automorphism, which need not be the identity. Forming the twist gives the \(k\)-map
\[
 B\otimes_{k,F_k}k\longrightarrow B,\qquad
 b\otimes c\longmapsto b^pc.
 \tag{EHX4}
\]
For the projection \(q:A^{(p)}\to A\), the composite \(qF_{A/k}\) is absolute Frobenius. If \(u_{ij}\) are the transition units for \(L\), its pullback has transitions \(u_{ij}^p\); hence \(F_{A/k}^*q^*L=L^p\). The scalar twist does not change vector-space dimensions of cohomology. CE6 proves that a finite surjective homomorphism here is a finite flat torsor under its finite commutative kernel and proves its Euler formula using a character filtration, including nonsemisimple representations. Counting geometric kernel points or assuming a reduced kernel would not establish that statement.

**(c)** Write \(P(T)=\sum_{j=0}^g a_jT^j\). The coefficient equations are
\[
 (p^j-p^g)a_j=0,\qquad 0\le j\le g.
 \tag{EHX5}
\]
Over \(\mathbf Q\) all \(a_j\) for \(j<g\) vanish. Thus \(P(T)=P(1)T^g\). For \(g=0\) this is a constant, with its value at zero unchanged. For \(g>0\), \(P(0)=0\) and \(P(-n)=(-1)^gP(n)\). The polynomial \(\binom T2=T(T-1)/2\) has degree two and is integer-valued, but
\[
 P(1)=0,\qquad P(p)=p(p-1)/2\ne p^2P(1).
 \tag{EHX6}
\]
Neither the degree bound nor the integrality condition replaces the Frobenius identity.

**(d)** For an overlap, record finitely many principal opens in the larger affine, localization maps and their inverses, generator identities, a unit-ideal cover expression, and the compatibility maps on intersections. For a transition, record its unit, inverse and cocycle identities on a finite refinement. Each equality needs a finite ideal-membership expression, so that it holds over the coefficient ring.

In the displayed example \(w\) is the inverse of \(2z\), so
\[
 B=(R[t,z]/(z^2-t))_{2z},\qquad
 \frac{\partial(z^2-t)}{\partial z}=2z\in B^\times.
 \tag{EHX7}
\]
This is the standard étale presentation proved in EA1–EA18; the same proof supplies flatness over \(R[t]\), and hence over \(R\). In characteristic two the second relation is \(-1=0\), so the chart is empty. A covering is preserved by its recorded finite unit-ideal expressions on the schemes being covered. Empty charts are allowed; it is the covering identities, not the nonemptiness of every chart at every prime, that ensure coverage. A single such chart cannot cover a nonempty characteristic-two fibre.

**(e)** The relation combination
\[
 6x+2(1-3x)=2
 \tag{EHX8}
\]
shows that two is zero in the quotient. There \(3x=x\), so \(x=1\); conversely these assignments satisfy both relations over \(\mathbf F_2\). The ring is therefore \(\mathbf F_2\), with one nonempty fibre at two. Inverting two makes it the zero ring.

In general choose a finite affine cover \(\operatorname{Spec}D_i\). Empty generic fibre means \(D_i\otimes_R\operatorname{Frac}R=0\); the localization criterion for \(1/1=0\) gives a nonzero \(a_i\in R\) with \(a_i1=0\) in \(D_i\). The product of the finitely many \(a_i\) is nonzero in the domain and makes every chart empty upon localization. Quasi-compactness is what makes this one finite product possible.

**(f)** Write \(\pi:Z\to X\). Its proper surjectivity is universal: for a point after any base change the original nonempty field fibre stays nonempty under the residue-field extension, by faithful field tensor. For every \(T\to\operatorname{Spec}R\) and closed \(C\subset X_T\), its inverse image under \(\pi_T\) is closed in \(Z_T\). It has the same image in \(T\) as \(C\), by surjectivity. Since \(Z_T/T\) is proper, that image is closed. Thus \(X/R\) is universally closed; its given separatedness and finite type make it proper.

A rational point is proper over a field and maps into \(\mathbf A^1\), but does not cover it. The affine line is not universally closed: the closed subset
\[
 \{(u,t):ut=1\}\subset\mathbf A^1_u\times\mathbf A^1_t
 \tag{EHX9}
\]
has image \(D(u)\), which is not closed in \(\mathbf A^1_u\). This verifies the failure directly.

**(g)** Since five is a nonzero divisor in \(R\),
\[
 H^0(C)=Re_1,\qquad H^1(C)=R/5R.
 \tag{EHX10}
\]
At five the differential becomes zero, so the fibre cohomology has dimensions two and one. The marked section spans only one of the two degree-zero fibre dimensions there. On \(D(5)\), the map from the second coordinate to the target is an isomorphism. Cancelling that two-term summand leaves just \(R[1/5]e_1\) in degree zero; every further base change preserves this cancellation and basis.

EH4 uses the actual unit as a cycle which is a basis at the generic point. FC16 first cancels unit matrix entries near that point and makes these actual cycles a basis of the remaining degree-zero free term. Their cycle equations force its entire outgoing matrix to be zero. Higher cohomology terms may still remain; their vanishing is not part of this argument. Merely knowing the dimension of fibre \(H^0\), without lifting its basis to actual cycles, would not force that matrix to vanish on nilpotent thickenings.

**(h)** Send \(t\) to three modulo seven and the inverted thirty to its invertible residue. Since \(3^2-2=7\), this defines a surjection
\[
 R\longrightarrow\mathbf F_7,\qquad
 \ker=(7,t-3).
 \tag{EHX11}
\]
The kernel is maximal because the quotient is a field.

If a characteristic-zero field were \(\mathbf Z[\alpha_1,\ldots,\alpha_r]\), it would also be a finite-type field over \(\mathbf Q\). The normalization proof in EH5 makes it a number field. A single nonzero integer \(D\) makes every \(D\alpha_i\) integral, so the proposed field lies in \(\mathcal O_K[1/D]\). Choose a prime \(p\nmid D\). The inverse of \(p\) in that ring would make \(D^a/p\) integral over \(\mathbf Z\) for some \(a\), impossible for that noninteger rational number. All finite localizations are still finite-type \(\mathbf Z\)-algebras, so this proof applies to them.

In contrast, inverting all primes produces \(\mathbf Q\), which is not a finite-type \(\mathbf Z\)-algebra by the same argument. Equivalently, the intersection in \(\operatorname{Spec}\mathbf Z\) of the opens \(D(p)\) for all primes consists of the generic point and has no positive-characteristic closed point. This is precisely why the specialization proof avoids separately shrinking infinitely many times.

**(i)** The one model carries \(M^n\) for every integer \(n\), including dual powers and the unit power. Each is flat over the same connected base. FC10 makes its Euler characteristic locally constant on that entire base. Thus for each \(n\) it has the same value at the fixed generic and fixed closed points. No new localization is introduced. In the numerical example,
\[
 \chi(A,H^{-2})=(-2)^3\cdot2=-16,\qquad
 \chi(A,\mathcal O_A)=0.
 \tag{EHX12}
\]
For a given ample line choose a positive power giving a closed projective immersion. PF8–PF9 kill higher cohomology of sufficiently large positive powers; a nonzero coordinate section and its powers give positive \(H^0\). Homogeneity then divides their positive Euler characteristic by a positive integer power to prove \(\chi(A,H)>0\). This proves positivity for a line already given. It does not construct an ample or symmetric ample line on every proper abelian variety.

**(j)** By CE4 the polynomial
\[
 Q(n)=\chi(A,f^*L^n)
 \tag{EHX13}
\]
has degree at most \(\dim f(A)\). By EH6 the same polynomial is \(n^g\chi(A,f^*L)\). If its degree bound is strictly smaller than \(g\), the coefficient \(\chi(A,f^*L)\) must be zero. This compares two proved polynomial descriptions; it does not assume that the image fibres have vanishing higher cohomology. For an isogeny, CE6 gives
\[
 \chi(A,f^*L)=N\chi(B,L).
 \tag{EHX14}
\]
It includes the scheme length of an inseparable kernel. Neither Euler identity computes a general multiplication degree without further line-bundle geometry, nor identifies the kernel's prime-power torsion modules. The normalized cube and the full kernel/Tate-rank proofs therefore remain separate inputs.

### 2D. The cube, projectivity and the integral Tate comparison

The characteristic-polynomial argument needs line-bundle identities, an ample line, multiplication degrees and a comparison of finite scheme lengths with integral Tate determinants. We prove those inputs here over arbitrary fields and in arbitrary dimension. Our convention remains that an abelian variety is a proper smooth geometrically integral commutative group variety; projectivity is a conclusion.

The earlier proofs used are GQ1–GQ3, CE1–CE6 and EH1–EH7 in this lesson; Lesson 1's finite-diagonal total-complex argument SH9 and étale criteria EA1–EA18; Lesson 3's affine Čech comparison SC0–SC15, finite family complex FC10–FC16, constants FC20, Krull intersection DFR1–DFR3, proper finite-fibre theorem 0.F.1, finite-cover projective coordinates 0.F.7, proper closed-immersion criterion CIE1, smooth charts SF1–SF3 and faithfully flat descent FD1–FD5; and Lesson 8's regular-local proofs NM1–NM2. We give the additional tensor, infinitesimal, divisor and finite-field-extension arguments explicitly.

#### 2D.1. Rigidity of maps and the two cohomological axes

**CU1 (map rigidity).** Let \(X,Y\) be geometrically integral varieties over \(k\), with \(X\) proper and \(x_0\in X(k)\). Let \(Z\) be separated. If \(f:X\times Y\to Z\) is constant on one fibre \(X\times\{y_0\}\), for \(y_0\in Y(k)\), then
\[
 f(x,y)=f(x_0,y).
 \tag{CU1}
\]
In particular a morphism of abelian varieties carrying origin to origin is a group homomorphism.

*Proof.* Work first over an algebraic closure. Choose an affine neighbourhood \(W\) of the constant value. The image in \(Y\) of the closed complement of \(f^{-1}W\) is closed, because \(X\times Y\to Y\) is proper. Its complement is an open \(V\) containing \(y_0\), and \(f(X\times V)\subset W\).

For every affine \(T=\operatorname{Spec}R\subset V\), the finite affine Čech complex of \(X\), tensored over \(k\) with \(R\), computes the product. Exactness of field tensor and FC20 give \(\Gamma(X\times T,\mathcal O)=R\). A map to the affine \(W\) therefore factors through \(T\). It agrees with \(f(x_0,-)\). The two maps on all of \(X\times Y\) have closed equalizer, since \(Z\) is separated; their functions agree on the dense open \(X\times V\), and the source is integral. A regular function vanishing on that dense open is zero in every domain chart. Thus the maps agree everywhere. Faithful scalar extension detects their equality over the original field.

For a pointed morphism \(a:A\to B\), apply this result to \(a(x+y)-a(x)-a(y)\). Both axis restrictions are zero, so the difference is zero. This proves the group assertion. \(\square\)

**CU2 (the degree-one product formula).** For proper geometrically integral \(X,Y\), with rational base points, restriction to the two axes is an isomorphism
\[
 H^1(X\times Y,\mathcal O)\xrightarrow{\ \sim\ }
 H^1(X,\mathcal O_X)\oplus H^1(Y,\mathcal O_Y).
 \tag{CU2}
\]

*Proof.* We supply the Čech comparison rather than identifying two different Čech complexes term by term. Choose finite affine covers \(U_i\) and \(V_j\). Put \(C_X=\check C(U,\mathcal O_X)\), \(C_Y=\check C(V,\mathcal O_Y)\). On each affine intersection, product coordinates identify functions with the tensor product of the two coordinate algebras. The bicomplex with term
\[
 D^{p,q}=
 \prod_{\substack{i_0<\cdots<i_p\\j_0<\cdots<j_q}}
 \Gamma(U_{i_0\cdots i_p},\mathcal O)
       \otimes_k\Gamma(V_{j_0\cdots j_q},\mathcal O),
 \qquad d=d_X+(-1)^p d_Y
 \tag{CU3}
\]
has total cohomology \(H^*(X\times Y,\mathcal O)\). Here is a comparison proof. Resolve the structure sheaf by injectives and take the two covering Čech directions as well. The augmented covering complex of an injective is exact: the covering-nerve proof SH9 contracts its free augmented nerve after restriction to a member, and injectivity extends the resulting functionals. On an affine intersection of the two covers, positive cohomology of \(\mathcal O\) is zero by SC0–SC15. Eliminating the injective direction therefore leaves \(D\); eliminating the two augmented covering directions leaves global injective cohomology. The signs in (CU3) make the two differentials anticommute. The finite-diagonal elimination SH9 proves both comparisons, with no convergence assumption. Finite covers make every diagonal finite. Thus \(D\), which is \(C_X\otimes C_Y\), has the claimed cohomology; it need not equal the ordinary Čech complex of the single product cover.

For completeness, every complex of vector spaces splits into its cohomology and contractible pairs. In degree \(r\), choose a complement \(H^r\) to the boundaries inside the cycles, and a complement \(T^r\) to the cycles in the entire term. The differential is an isomorphism from \(T^r\) to the next boundary space. Its inverse contracts that pair. Tensoring a contracted pair with another complex remains contracted: the inverse in the first factor has degree minus one, and the two cross terms cancel with the sign in (CU3). Hence
\[
 H^n(D)=\bigoplus_{p+q=n}H^p(X,\mathcal O_X)
                                  \otimes_kH^q(Y,\mathcal O_Y).
 \tag{CU4}
\]
FC20 gives both degree-zero factors \(k\). In degree one the two summands are pullbacks from the two factors. Restriction to its own axis is the identity; restriction to the other factors through \(H^1(\operatorname{Spec}k,\mathcal O)=0\). This proves (CU2), including the identification of the maps. The same argument tensors with any \(k\)-vector space of coefficients. \(\square\)

#### 2D.2. Triviality on every infinitesimal thickening

**CU3.** Work over an algebraically closed field. Let \(X,Y\) be proper integral varieties, put \(W=X\times Y\), and let \(S\) be a local Artinian \(k\)-algebra with residue field \(k\). A line on \(W_S\) which is trivial on its closed fibre and on both full axes is trivial. Compatible axis trivializations can be preserved through every quotient of \(S\).

*Proof.* Use induction on the powers of the maximal ideal. More generally consider a quotient \(S'\twoheadrightarrow S\) with kernel \(J\) killed by the maximal ideal of \(S'\). Then \(J^2=0\), and the ideal of \(W_S\) in \(W_{S'}\) is \(\mathcal O_W\otimes_kJ\). Fix an already normalized trivialization over \(S\).

On an affine chart of \(W\) a line over \(S'\) with trivial reduction is free. Indeed lift a generator of its reduction in its finite projective module of sections. The cokernel of this generating map is killed by nilpotent Nakayama, so the map is surjective; projectivity splits it, and the kernel has zero reduction and is zero by the same argument. Thus choose local frames lifting the prescribed frame over \(S\). Their transitions are
\[
 1+c_{ij},\qquad
 c_{ij}\in\Gamma(U_i\cap U_j,\mathcal O_W)\otimes_kJ,\qquad
 c_{ij}+c_{jk}=c_{ik}.
 \tag{CU5}
\]
Changing the lifted frames changes this additive cocycle by a Čech boundary. The two axis trivializations show that its restrictions to the axes are boundaries. CU2, with coefficients \(J\), says its class is zero. Local additive corrections consequently make every transition one, giving a global trivialization lifting the previous one.

Its two restrictions differ from the fixed axis trivializations by units of \(S'\): proper constants commute with this scalar algebra, as in CU1. These units agree at the axis intersection, so are the same unit. Multiplying the trivialization by its inverse normalizes both axes. The unit reduces to one, preserving the earlier normalization. Starting on the closed fibre and repeating proves the assertion for every Artinian quotient. \(\square\)

#### 2D.3. From all thickenings to the cube

**CU4 (the cube).** Let \(X,Y,Z\) be proper geometrically integral varieties with rational base points \(x_0,y_0,z_0\). A line \(M\) on their product that is trivial on
\[
 X\times Y\times\{z_0\},\qquad
 X\times\{y_0\}\times Z,\qquad
 \{x_0\}\times Y\times Z
 \tag{CU6}
\]
is trivial.

*Proof.* First suppose \(k\) algebraically closed. Normalize the three face trivializations at the common base point. Their restrictions to each pairwise intersection agree, since the only units on each proper integral intersection are constants.

Put \(R=\mathcal O_{Z,z_0}\), with maximal ideal \(\mathfrak m\). CU3 makes \(M\) trivial on \(W\times\operatorname{Spec}(R/\mathfrak m^r)\) for every \(r\ge1\), where \(W=X\times Y\). These assertions concern the full nilpotent thickenings.

Apply the actual family complex FC10 to \(M\), and cancel unit differential entries near \(z_0\) as in FC13–FC14. Its degree-zero term over \(R\) has rank one, because the closed fibre is the trivial line on \(W\), with \(H^0=k\). Its outgoing differential is a column \(d^0\). For every \(r\), the trivial line over \(R/\mathfrak m^r\) has a section reducing to a nonzero closed-fibre section. Under the natural comparison FC10 this section is a cycle in that rank-one term with unit coordinate. Therefore
\[
 d^0=0\pmod{\mathfrak m^r}\quad\hbox{for every }r,\qquad
 d^0=0\quad\hbox{over }R.
 \tag{CU7}
\]
The second implication is precisely DFR3. To recall its justification, Artin–Rees applied to the finite submodule \(\bigcap_r\mathfrak m^rN\) makes it its own product with \(\mathfrak m\); finite Nakayama makes it zero. Apply this to each finite free target coordinate. A matrix vanishing only on residue fields would not give (CU7).

The finite matrix and its cancellation data spread to an affine neighbourhood of \(z_0\). After shrinking, its degree-zero term is a free line and \(d^0=0\). Its basis gives a section of \(M\) on that neighbourhood. On the closed fibre it is nowhere zero. Its failure to generate \(M\) is a closed coherent support, whose projection to the base is closed by properness of \(W\). Excluding that projection gives a nonempty open \(V\subset Z\) on which \(M\) is trivial.

We also need a closedness assertion. On a proper integral variety over an algebraically closed field a line \(L\) is trivial if and only if both \(L\) and \(L^{-1}\) have a nonzero section. Their product is a nonzero constant: it is nonzero at the generic point and constants are \(k\). Thus both sections are units in their line frames. In a family, each condition \(h^0\ge1\) is closed. Indeed FC10 computes \(H^0\) as the kernel of its first matrix; the relevant upper bound on matrix rank is cut out by minors, after making its degree-zero rank constant. Consequently the geometric-fibre triviality locus of \(M\) over \(Z\) is closed. It contains \(V\), so is all of the integral \(Z\). The reduced-base see-saw CE3 now gives \(M=p_Z^*N\); restriction to \((x_0,y_0)\times Z\) makes \(N\) trivial. This proves the assertion over the algebraic closure.

Over the original field, use field base change on the finite affine Čech complex of the proper product. Triviality after algebraic closure makes \(H^0(M)\) one-dimensional over \(k\), and evaluation at the common rational base point is an isomorphism after that faithful extension, hence already an isomorphism. The section with the prescribed value is nowhere zero, again detected after faithful extension. It trivializes \(M\) over \(k\). \(\square\)

#### 2D.4. The normalized cube and every integer recurrence

**CU5.** For a line \(L\) on a proper geometrically integral commutative group \(A\), put
\(\widetilde L=L\otimes_k(e^*L)^{-1}\), with its canonical origin trivialization. Write \(m_{ij}\) and \(m_{123}\) for the indicated sums on \(A^3\), and \(p_i\) for its projections. Then the origin-normalized line
\[
 \mathcal C(\widetilde L)=
 m_{123}^*\widetilde L\otimes
 (m_{12}^*\widetilde L\otimes m_{13}^*\widetilde L
                         \otimes m_{23}^*\widetilde L)^{-1}
 \otimes p_1^*\widetilde L\otimes p_2^*\widetilde L
                         \otimes p_3^*\widetilde L
 \tag{CU8}
\]
is canonically trivial, compatibly with the coordinate faces. Without replacing \(L\) by \(\widetilde L\), include the additional constant factor \((e^*L)^{-1}\) in (CU8).

*Proof.* Each coordinate-face restriction cancels in pairs, with the remaining origin factor canonically one. CU4 makes the cube trivial. A trivialization with specified value one at the origin is unique, since every global unit on \(A^3\) is constant. On a coordinate face it therefore agrees with its cancellation trivialization. Pulling back along any three maps to \(A\) gives the cube identity on their source, including nonreduced source schemes.

Here are its needed consequences, in line-bundle classes. Write \(B_n=[n]^*\widetilde L\). Pull back by \(([n],1,[-1])\). Since \(B_0\) is trivial, the resulting recurrence and its solution are
\[
 \begin{split}
 B_{n+1}\otimes B_{n-1}
       &\simeq B_n^{\,2}\otimes\widetilde L\otimes[-1]^*\widetilde L,\\
 [n]^*\widetilde L
       &\simeq \widetilde L^{\,n(n+1)/2}
                  \otimes([-1]^*\widetilde L)^{\,n(n-1)/2}
                  \qquad(n\in\mathbf Z).
 \end{split}
 \tag{CU9}
\]
Both exponent sequences have second difference one and the correct values at zero and one. The recurrence determines the next or previous term by tensor inverses, proving the formula in both directions on the integers. In particular a symmetric line \(H\) satisfies \([n]^*H\simeq H^{n^2}\).

For maps \(f,h:T\to A\), set \(G_n=(nf+h)^*\widetilde L\). Pull back (CU8) by \((nf+h,f,f)\). It gives
\[
 \begin{split}
 Q_f&=(2f)^*\widetilde L\otimes(f^*\widetilde L)^{-2},\\
 G_{n+2}\otimes G_n\otimes G_{n+1}^{-2}&\simeq Q_f,\\
 G_n&\simeq G_0\otimes(G_1\otimes G_0^{-1})^n
                                      \otimes Q_f^{\,n(n-1)/2}.
 \end{split}
 \tag{CU10}
\]
Again the second-difference recurrence proves the formula at every positive and negative integer. CE2's multivariable Euler polynomial, substituted into the three exponent expressions \(1,n,n(n-1)/2\), consequently has degree at most twice the support dimension.

Finally constants \(x,y\) and the identity map in the cube give the square identity
\[
 t_{x+y}^*L\otimes L\simeq t_x^*L\otimes t_y^*L.
 \tag{CU11}
\]
Constant one-dimensional field factors do not affect these line classes. The normalized version above retains their canonical identifications. \(\square\)

#### 2D.5. An affine boundary and a finite linear system

**CU6.** Over an algebraically closed field, every positive-dimensional abelian variety has an ample line bundle.

*Proof.* Choose an affine open \(U\) containing the origin. Its boundary is nonempty: a proper affine integral variety over this field has its coordinate ring equal to its finite-dimensional ring of constants, and is a point. We first justify that this boundary is the support of an effective Cartier divisor. Closed-point local rings of \(A\) are regular: use the standard smooth charts SF1–SF3, étale flatness EA1–EA18 and NM2's flat regular-fibre test, exactly as in EH4. They are factorial and normal by NM1–NM2.

Suppose a boundary component had codimension at least two, with generic point \(\xi\). Choose a closed point on it avoiding all other boundary components. Its local ring is factorial; localization at the prime of \(\xi\) remains factorial, by localizing prime factorizations. Call that ring \(R\), with maximal ideal \(\mathfrak m\). The intersection of \(U\) with \(\operatorname{Spec}R\) is the punctured spectrum and is affine: intersections of two affine opens in a separated scheme are affine, and this assertion survives localization. Its global functions equal \(R\). In fact they are rational functions belonging to all height-one localizations, all of which occur in the punctured spectrum; a reduced fraction in a factorial ring with no height-one denominator pole has a unit denominator. But an affine punctured spectrum with coordinate ring \(R\), and structural ring map the identity, would be all of \(\operatorname{Spec}R\). This contradiction proves that every boundary component has codimension one.

There are finitely many such components. The sum of their reduced prime divisors is Cartier: at each closed point factoriality provides local prime equations, and equations with identical prime orders have unit ratio on overlaps. These local equations extend to open neighbourhoods; a complement missing every closed point is empty by EA2. Denote this effective divisor by \(D\), and put \(L=\mathcal O_A(D)\). Its support \(S\) is exactly \(A\setminus U\).

We prove that the support stabilizer is finite. Impose, for every \(s\in S(k)\), the two closed conditions
\[
 a+s\in S,\qquad -a+s\in S.
 \tag{CU12}
\]
The sum of their ideal sheaves is coherent on the Noetherian \(A\): on a finite affine cover its ideal is finitely generated, so finitely many conditions suffice. They define a closed subscheme \(H_S\). At a closed point of \(H_S\) both inclusions of the translated support hold, hence \(a+S=S\) and \(a+U=U\). Since \(0\in U\), this puts \(a\) in \(U\). A nonempty closed subset of \(H_S\cap S\) would have a closed point, so \(H_S\) factors through \(U\). It is therefore affine and proper. Proper coherent finiteness CG13 makes its affine coordinate ring finite-dimensional over \(k\); thus \(H_S\) is finite, including its possible nilpotents. Any support-stabilizing point after any algebraically closed extension satisfies all of its finitely many defining conditions, and hence belongs to that finite base change.

The square identity gives effective divisors
\[
 E_x=t_x^*D+t_{-x}^*D\sim 2D.
 \tag{CU13}
\]
For any closed point \(a\), choose \(x\) outside \((S-a)\cup(a-S)\). This is possible since \(A\) is integral and these are proper closed sets. Then \(a\notin E_x\). Thus the finite-dimensional space \(H^0(A,L^2)\) generates \(L^2\), and PF4 gives a proper morphism \(\phi:A\to\mathbf P^N\), with \(\phi^*\mathcal O(1)=L^2\).

We prove finiteness on every geometric fibre. Extend to any algebraically closed field \(\Omega\). Suppose a fibre had a positive-dimensional reduced integral component \(T\), and write \(S_i\) for the integral components of \(S_\Omega\). They have dimension \(g-1\); components over the original algebraically closed field remain integral by GQ1's product/scalar argument. Let
\(V_T=\{x:T\subset S_\Omega-x\}\). This is closed, as an intersection of closed translates, and lies in \(t_0-S_\Omega\) for any \(t_0\in T(\Omega)\), so has dimension at most \(g-1\).

Every section of \(L_\Omega^2\) restricts to a section of a constant line on the proper integral \(T\). It is therefore zero everywhere or nowhere zero. If \(x\in T-S_i\), the section with divisor \(E_x\) vanishes at some point of \(T\); it vanishes on all of \(T\). Irreducibility gives \(T\subset S_\Omega-x\) or \(T\subset S_\Omega+x\). Consequently
\[
 T-S_i\subset V_T\cup(-V_T).
 \tag{CU14}
\]
The left side is a closed integral image of the proper integral product \(T\times S_i\). It contains \(t-S_i\) for every \(t\in T(\Omega)\), so has dimension at least \(g-1\). The right side bounds it by \(g-1\). Each closed integral \(t-S_i\) of that same dimension must therefore equal \(T-S_i\), by the strict dimension drop for proper closed integral subsets proved in GQ1. It follows that every \(t-t_0\) stabilizes every \(S_i\), hence \(S_\Omega\). Thus \(T-t_0\) lies in the finite \((H_S)_\Omega\), contradicting its positive dimension.

All geometric fibres are zero-dimensional and finite. The proper finite-fibre theorem 0.F.1 makes \(\phi\) finite. The explicit finite-cover coordinate theorem 0.F.7 then makes a power of \(L^2\) very ample. Hence \(L\) is ample. \(\square\)

#### 2D.6. Projectivity and symmetric ample lines over the original field

**CU7.** Every abelian variety over any field is projective and has a symmetric ample line defined over that field.

*Proof.* In dimension zero the variety is \(\operatorname{Spec}k\): after algebraic closure its proper integral zero-dimensional scheme is a point, and faithful scalar extension detects this equality. The trivial line suffices. Assume positive dimension.

CU6 gives a projective embedding after algebraic closure. Its finitely many chart, transition and section equations descend to a finite algebraic extension \(E/k\): the finite-witness argument EH2 applies with coefficients adjoined to \(k\). The descended morphism is a closed immersion. To check this without a limit assertion, it is proper, and after algebraic closure every geometric fibre is empty or the entire reduced one-point scheme. The proper criterion CIE1, proved by finite-fibre finiteness and the finite cokernel of the coordinate map, detects a closed immersion already over \(E\).

We give both parts of the remaining field descent. For a finite extension \(E/k\), let \(E_s\) be its maximal separable subfield. Then \(E_s/k\) is finite separable and \(E/E_s\) is purely inseparable. Indeed for any element its irreducible polynomial is \(h(T^{p^r})\) with \(h'\ne0\); its \(p^r\)-power is separable. For a finite generating list choose one common power \(q=p^r\), giving \(E^q\subset E_s\). In characteristic zero take \(E_s=E\).

Suppose first \(E/E_s\) purely inseparable with that power \(q\), and let \(M\) be a very ample line on \(A_E\), with embedding sections \(s_j\). The finite projection \(A_E\to A_{E_s}\) is a universal homeomorphism. On a residue-field tensor its elements have \(q\)-th powers in the base, and after an algebraic closure each such polynomial has only one root; the nonzero tensor is therefore supported at one prime. Integral lying over and closedness make the projection a homeomorphism, also after base change.

Choose affine opens \(U_i\subset A_{E_s}\) whose inverse images trivialize \(M\). For any algebra \(B\) over \(E_s\),
\[
 (B\otimes_{E_s}E)^q\subset B\otimes1,
 \tag{CU15}
\]
by the characteristic-\(p\) binomial formula and \(E^q\subset E_s\). Raising the transition units to the \(q\)-th power thus descends them uniquely to units on \(U_i\cap U_j\); their inverses and cocycles descend too. This constructs a line \(P\) whose pullback is \(M^q\). The local coefficients of \(s_j^q\) descend by the same calculation. They generate \(P\) and give a morphism to projective space. After extension to \(E\) it is the given embedding followed by the coordinate map \([X_i]\mapsto[X_i^q]\). That coordinate map is finite: on each coordinate chart the algebra is generated over the \(q\)-th-power coordinates by monomials with every exponent less than \(q\). Every geometric fibre of the descended morphism is therefore finite. It is proper, so 0.F.1 makes it finite. Theorem 0.F.7 supplies a very ample power of \(P\). This proves projectivity over \(E_s\).

Choose a finite Galois extension \(F/k\) containing \(E_s\), with group \(G\), and pull the ample line just obtained to \(A_F\). The tensor product of all its conjugates,
\[
 N_F=\bigotimes_{\sigma\in G}\sigma^*P_F,
 \tag{CU16}
\]
has its canonical permutation descent datum; the cocycle identity is the identity for composing permutations. The identification \(F\otimes_kF\simeq\prod_{\sigma\in G}F\) follows by factoring a separable primitive polynomial and the Chinese remainder theorem, so this is precisely a faithfully flat descent datum. FD1–FD4 descend its invertible module on affine charts and glue a line \(N\) on \(A\).

A common positive power of every conjugate is very ample. Their product is very ample by the product of their closed embeddings and the Segre embedding PF1–PF6. Therefore \(N_F^a\) is very ample for some \(a>0\). Field Čech base change gives all sections of \(N_F^a\) by extending \(H^0(A,N^a)\). The evaluation map for these sections is surjective, detected after the faithful field extension, and defines a morphism over \(k\). After \(F\) it is a closed immersion. Using all sections preserves a closed immersion supplied by a subsystem: on a chart where one subsystem section is a frame, its coordinate functions already surject onto the source ring, and adjoining further coordinate functions preserves that surjectivity; properness closes the image. Applying CIE1 again descends the closed immersion. Hence \(N\) is ample over \(k\).

Finally
\[
 H=N\otimes[-1]^*N
 \tag{CU17}
\]
is symmetric. A common very ample power of its two factors, followed by their product embedding and Segre, proves that it is ample. Thus the ample and symmetric ample lines have been constructed over the original field, including imperfect fields. \(\square\)

#### 2D.7. Multiplication, including inseparable multiplication

**CU8.** For every nonzero integer \(n\), multiplication on a \(g\)-dimensional abelian variety is a finite flat surjective map, and
\[
 [n]^*H\simeq H^{n^2},\qquad \deg[n]=n^{2g}
 \tag{CU18}
\]
for a symmetric ample line \(H\).

*Proof.* The line identity is CU5. A positive-dimensional proper integral component of a geometric fibre would carry a trivial restriction of \([n]^*H\), since that map is constant there. The same line is a positive power of an ample line restricted to that component. This is impossible: a very ample power of a trivial line on a proper integral positive-dimensional variety would define a constant projective map, since all functions are constants. Positive powers of an ample line are ample, as follows by repeating the product embedding and Segre construction. Thus every geometric fibre is finite. Proper finite-fibre finiteness makes \([n]\) finite.

Its closed image has dimension \(g\): a finite map from an integral variety to its scheme-theoretic image has an integral finite coordinate extension, and hence equal transcendence degree and dimension by GQ1. A proper closed subset of \(A\) has smaller dimension. The image is therefore all of \(A\). CE6's generic basis and translation argument makes this isogeny finite flat. Apply its torsor Euler comparison, EH6 and EH7:
\[
 \deg[n]\;\chi(A,H)
   =\chi(A,[n]^*H)
   =\chi(A,H^{n^2})
   =n^{2g}\chi(A,H),\qquad \chi(A,H)>0.
 \tag{CU19}
\]
Cancellation proves the degree, also when the characteristic divides \(n\). In dimension zero multiplication is the identity, of degree one. For \(g>0\), multiplication by zero is the constant map and is not an isogeny. \(\square\)

#### 2D.8. Compatible torsion bases and the Tate rank

**CU9.** If \(\ell\ne\operatorname{char}k\), then
\[
 A[\ell^r](\bar k)\simeq(\mathbf Z/\ell^r)^{2g},
 \qquad T_\ell A\simeq\mathbf Z_\ell^{\,2g}.
 \tag{CU20}
\]
The bases can be chosen compatibly with the multiplication-by-\(\ell\) transitions.

*Proof.* Invertible multiplication is étale by the full square-zero correction in GQ3: lift a point by smoothness, and correct its error in the tangent kernel by the inverse of the integer; uniqueness is the same tangent calculation. The étale criterion EA1–EA18 turns that lifting property into étaleness. CU8 supplies its finite rank. Over \(\bar k\) the kernel consequently has exactly \(\ell^{2gr}\) reduced points.

Multiplication by \(\ell\) maps \(A[\ell^{r+1}](\bar k)\) onto \(A[\ell^r](\bar k)\). Lift any point using the surjective isogeny on the whole variety; the lift is killed by the next power. Choose a basis \(a_{i,1}\) of the \(\mathbf F_\ell\)-space \(A[\ell](\bar k)\), of dimension \(2g\) by its order. Lift each basis point compatibly to \(a_{i,r}\) at every level. The map
\[
 (\mathbf Z/\ell^r)^{2g}\longrightarrow A[\ell^r](\bar k),
       \qquad (c_i)\longmapsto\sum_i c_i a_{i,r}
 \tag{CU21}
\]
is injective. In a relation, apply \(\ell^{r-1}\): every coefficient is divisible by \(\ell\). Divide those coefficients by \(\ell\) and use the preceding-level relation; induction makes all divisible by \(\ell^r\). The equal finite orders give surjectivity. Transitions are coordinate reduction in these bases. Taking compatible sequences gives (CU20), with its integral topology, and also identifies \(T_\ell A/\ell^r\) with the actual torsion group. Each finite torsion scheme is defined over \(k\); its finite étale points have open Galois stabilizers, so the inverse-limit action is continuous. \(\square\)

#### 2D.9. Isogeny length and integral determinant

**CU10.** For an isogeny \(f:A\to B\) of degree \(N\), and \(\ell\ne\operatorname{char}k\), its geometric point kernel has \(\ell\)-primary order \(\ell^{v_\ell(N)}\), and
\[
 T_\ell f\text{ is injective},\qquad
 v_\ell(\det T_\ell f)=v_\ell(N).
 \tag{CU22}
\]

*Proof.* Extend to an algebraic closure. CE6 identifies \(N\) with the full finite-kernel length and all geometric fibres with translates of that kernel. We compute the length of each connected point directly from the function fields. For any finite field extension \(L/K\), its maximal separable subextension has degree \(s\), and the remainder has degree \(p^a\) and is purely inseparable in characteristic \(p\); in characteristic zero put \(a=0\) and \(p^a=1\). The power argument in CU7 proves this decomposition: a common \(p\)-power of a finite generating list is separable, and each purely inseparable simple step has \(p\)-power degree.

After an algebraic closure of \(K\), the separable subextension splits into \(s\) copies by the distinct-root Chinese remainder theorem. Each purely inseparable factor has a unique point, since each generating equation has a unique root; its vector-space dimension, and hence its local length, is \(p^a\). Applying this to the generic fibre of \(f\), and translating that fibre to its kernel over the algebraic closure of the generic field, gives
\[
 N=s p^a,\qquad \#\ker f(\bar k)=s.
 \tag{CU23}
\]
The point count and local lengths of a finite algebra over the algebraically closed constant field do not change upon a larger algebraically closed extension: its Artinian local factors have that constant residue field, and their nilpotent filtration layers tensor faithfully. This justifies transferring the generic computation back to the constant-field kernel. Thus \(v_\ell(N)=v_\ell(s)\). No annihilation of the kernel scheme by its rank is an input to this argument.

Write \(K=\ker f(\bar k)\), a finite abstract abelian group. It is killed by its order \(s\): the order of each cyclic subgroup divides \(s\), by its cosets. If a compatible Tate sequence lies in \(K\), write \(s=\ell^e m\) with \(m\) prime to \(\ell\). Its coordinates are killed by \(\ell^e\), since multiplication by \(m\) is invertible on a group of \(\ell\)-power exponent. Compatibility makes the coordinate at level \(r\) equal \(\ell^e\) times the coordinate at level \(r+e\), hence zero. This proves injectivity of \(T_\ell f\). Both free modules have rank \(2g\), so its integral matrix has nonzero determinant.

At finite level there is the exact sequence
\[
 0\longrightarrow K[\ell^r]\longrightarrow A[\ell^r](\bar k)
 \xrightarrow{\,f\,}B[\ell^r](\bar k)
 \longrightarrow K/\ell^rK\longrightarrow0.
 \tag{CU24}
\]
For the last map, lift \(b\) to \(a\in A(\bar k)\), using surjectivity of \(f\), and take \(\ell^r a\) modulo \(\ell^rK\). This is well-defined, exact at the middle, and onto because multiplication by \(\ell^r\) is surjective on \(A(\bar k)\). For \(r\ge e\), the last group has order \(\ell^{v_\ell(s)}\), by the elementary coprime-primary splitting of the finite group.

Diagonalize \(T_\ell f\) over the DVR. To recall the algorithm, choose an entry of least valuation, move it to the top left, divide the other entries in its row and column by it and clear them with elementary invertible operations; repeat on the remaining submatrix. This gives diagonal entries units times \(\ell^{a_i}\). Its cokernel modulo \(\ell^r\) has order \(\ell^{\sum_i\min(a_i,r)}\). CU9 identifies that reduction with the finite-level map in (CU24). For large \(r\) this gives
\[
 v_\ell(\det T_\ell f)=\sum_i a_i
                =v_\ell(s)=v_\ell(N),
 \tag{CU25}
\]
as required. The field-length step includes every inseparable contribution to \(N\). \(\square\)

#### 2D.10. Nonisogenies and the complete field-geometric input

**CU11.** A nonisogeny endomorphism \(f:A\to A\) has smaller-dimensional image and singular rational Tate matrix. Thus, with \(\delta(f)=0\) for nonisogenies,
\[
 |\delta(f)|_\ell=|\det(T_\ell f)|_\ell
 \tag{CU26}
\]
holds for every endomorphism, with the isogeny case supplied by CU10.

*Proof.* A dominant endomorphism is generically finite: its finite-type function-field extension is algebraic, since both transcendence degrees are \(g\), hence finite. A geometric generic fibre is therefore finite. Translating one of its points identifies it with the scalar-extended kernel, so that kernel is finite. All fibres are translates of it. Proper finite-fibre finiteness then makes the morphism finite and surjective. Conversely a finite kernel makes all fibres finite; the same theorem and the finite-image dimension argument of CU8 make the endomorphism an isogeny. A nonisogeny consequently has smaller-dimensional image and a positive-dimensional kernel.

Work over \(\bar k\). Let \(C\) be the reduced identity component of that kernel. GQ1 makes it proper and integral. Its product is reduced and integral, so addition and inverse factor through the reduced component: they preserve its underlying identity component and annihilate its radical ideal. It is a proper integral commutative group. We need not assume its smoothness. The symmetric ample line of \(A\) restricts to a symmetric ample line \(J\) on \(C\).

Multiplication by \(\ell\) on \(C\) is finite and surjective, by the same ample-fibre and dimension arguments as in CU8. It is finite flat: the generic fraction-field basis is a free basis on a nonempty open, and translations cover every closed point; this is the complete generic-basis argument of CE6, which uses integrality and the group law, not smoothness. Its kernel torsor has CE6's Euler formula for the same reason: the kernel is finite commutative, and the character filtration and coherent tensor argument apply unchanged. If its degree is \(d\), CE2 therefore gives
\[
 P(\ell^2 t)=dP(t),\qquad
       P(t)=\chi(C,J^t).
 \tag{CU27}
\]
This polynomial is unbounded and positive for large \(t\). For a direct verification, take a very ample power \(J^a\). Some two projective coordinate sections \(s_0,s_1\) have nonconstant ratio, since the embedded integral \(C\) has positive dimension. That ratio is transcendental over the algebraically closed field; thus the \(m+1\) sections \(s_0^{m-i}s_1^i\) are independent. Serre vanishing PF8–PF9 makes their dimension a lower bound for \(P(am)\) for large \(m\). Hence \(\deg P=b\ge1\). Comparing its leading coefficient in (CU27) gives \(d=\ell^{2b}>1\).

The kernel \(C[\ell]\) is a closed subscheme of the finite étale \(A[\ell]\); over the algebraically closed field a closed subscheme of a product of fields is again a product of a subset of those fields. It is therefore reduced and has \(d>1\) points. Choose a nonzero point, and lift it repeatedly under the surjective multiplication map on \(C\). The resulting nonzero compatible sequence belongs to \(T_\ell C\), injects into \(T_\ell A\), and is killed by \(T_\ell f\). Since \(T_\ell A\) is free, its rational Tate map has a nonzero kernel and determinant zero. The isogeny case of (CU26) is CU10. \(\square\)

**CU12 (scope of the characteristic-polynomial argument).** CU4–CU11, CE2, CE4, CE6 and EH6–EH7 supply all the field-geometric inputs used in Lemma 2.2: the normalized cube, quadratic line recurrence, symmetric ample existence, all multiplication degrees, the rank \(2g\) of the Tate module, and the full isogeny/nonisogeny determinant comparison.

CU10 supplies the finite-kernel comparison by the direct separable/purely-inseparable field-length argument. It does not require a general theorem that every finite group scheme is killed by its rank. The polynomial interpolation and root-valuation comparison are the remaining explicit argument in Lemma 2.2. The full semistable model, toric-monodromy pairing and finite descent in Theorem 2.4, modularity and exact local comparison in Theorem 5.3, and the general cohomological comparison and purity requirements remain separate.

Free comparisons are the Stacks project authors' [coherent product formula](https://stacks.math.columbia.edu/tag/0BEC), Akhil Mathew's [infinitesimal cube discussion](https://amathew.wordpress.com/2012/06/04/the-theorem-of-the-cube/), and Andrew Snowden's [algebraic abelian-variety lecture](https://websites.umich.edu/~asnowden/teaching/2013/679/L04.html). The Čech, matrix, affine-boundary, inseparable descent and integral index arguments used here have their proofs above; these comparisons do not replace them.

#### 2D.11. Graded exercise: from the cube to the Tate determinant

This exercise is worth **100 points**. Give the indicated arguments as well as the numerical answers. A computation with a finite matrix is an illustration of the proof, and does not establish the general geometric theorem by itself.

**(a) Map rigidity (8 points).** Prove the factorization in CU1 from properness and functions on \(X\times T\). Explain where integralness and separatedness enter. Show that \(f(x,y)=xy\) on \(\mathbf A^1\times\mathbf A^1\), with both base points zero, disproves the same assertion when properness of the first factor is omitted.

**(b) The signed tensor complex (8 points).** Over any field, let
\[
 C=[\,kc_0\longrightarrow kc_1\oplus ku\longrightarrow kv\,],
 \quad d(c_0)=d(c_1)=0,\quad d(u)=v,
\]
in degrees zero to two. Let \(D\) have degree-zero basis \(d_0,a\), degree-one basis \(d_1,b\), and differential \(d(d_0)=0,\ d(a)=b\). Compute the ranks of the three differentials and all cohomology dimensions of \(\operatorname{Tot}(C\otimes D)\). Check its differential twice on \(u\otimes a\), including characteristic two.

**(c) The infinitesimal axes (10 points).** Explain the cocycle \(1+c_{ij}\) in CU3 and how the two restriction maps detect its class. Using a genus-one curve \(E\) and a nonzero class in \(H^1(E,\mathcal O_E)\), give a first-order line on \(E\times E\) with trivial closed fibre and one trivial full axis that is nevertheless nontrivial. Identify the axis that fails.

**(d) Every thickening is essential (10 points).** Let \(R=k[t]_{(t)}\) and take the complex \([R\xrightarrow{t^m}R]\), for \(m\ge1\). Compute its degree-zero cohomology over \(R\) and over \(R/(t^r)\). Determine for which \(r\) a cycle can reduce to one modulo \(t\). Explain why any fixed finite set of thickening tests cannot replace the intersection argument in CU4. No geometric realization of this complex is assumed.

**(e) Normalize and solve the recurrence (8 points).** Restrict the unnormalized seven-factor cube of \(L\) to the face with third coordinate zero. Identify its remaining constant factor. Compute \([-2]^*L\) in terms of \(L\) and \([-1]^*L\). If \(G_0=M,\ G_1=N\), and the constant multiplicative second difference is \(Q\), compute \(G_{-2}\).

**(f) Boundary and stabilizer (10 points).** Prove that the punctured spectrum of \(k[x,y]_{(x,y)}\) is not affine. Explain how that mechanism rules out a boundary component of codimension at least two in CU6. For the finite subset \(S=\{0,P\}\) of an elliptic curve, where \(P\) has order five, compare its translation stabilizer with \(S-S\). Explain why support preservation is imposed by all the closed inclusion conditions in CU12.

**(g) Purely inseparable descent (8 points).** In characteristic \(p\), let \(E=k(\alpha)\), with \(\alpha^q=c\in k\) and \(q=p^r\). In
\[
 B=k[t,(1+ct^q)^{-1}]
\]
show that \(u=1+\alpha t\) is a unit after extension to \(E\), and compute its descended \(q\)-th power and inverse. Explain how this calculation applies to line transition units and section coefficients. Compute the degree and the full zero fibre of the coordinate map \(\mathbf P^1\to\mathbf P^1,\ [X:Y]\mapsto[X^q:Y^q]\).

**(h) Products of elliptic curves (8 points).** Let \(A=E^g\), \(g\ge1\), and let
\[
 D=\sum_{i=1}^g\operatorname{pr}_i^*(0),\qquad L=\mathcal O_A(D).
\]
Use the actual genus-one computation and CU2's tensor proof to compute \(h^0(A,L)\), its higher cohomology, and \(h^0(A,L^2)\). Identify the morphism of \(L^2\), its finite degree, and the degree of \([n]\). Include characteristics dividing \(2n\).

**(i) Compatible torsion (8 points).** Carry out the injectivity proof of CU21, and explain why an independently chosen basis at every finite level is insufficient to identify the transition maps. State the rank of \(T_\ell A\), its quotient modulo \(\ell^r\), and its topology. Must the compatible basis be Galois invariant?

**(j) Scheme length and Smith index (8 points).** On \(E^2\) in characteristic three, take \(f=[6]\) and \(\ell=2\). Compute its degree and the integral Tate index. If \(E[3](\bar k)\) has respectively one or three points, compute the point-kernel order and the local length at each kernel point. Separately, for a Smith matrix with diagonal valuations \(0,1,3,4\), compute the orders of its cokernels modulo \(2,4,8,16\), and its final integral index.

**(k) A nonisogeny (8 points).** On \(E^3\) in characteristic five take \(f=([2],0,[5])\), with the maps applied to the three coordinates. For \(\ell=3\), compute the Tate determinant, image dimension and a nonzero Tate submodule in its kernel. Explain why \(\chi(E^3,f^*H)=0\) for any line \(H\), using the image bound.

**(l) Polynomial degree and scope (6 points).** Explain how the integer recurrence CU10 and CE2 give degree at most \(2g\) for \(\delta(nf+h)\). Identify the additional proved fact giving \(\delta(nf)=n^{2g}\delta(f)\). Does this field-geometric conclusion prove the semistable monodromy pairing in Theorem 2.4?

**Complete solution.**

**(a)** Choose an affine neighbourhood of the constant fibre value. Proper projection of the closed complement of its inverse image leaves an open base neighbourhood \(V\) whose whole fibres map to that affine. The product Čech complex gives \(\Gamma(X\times\operatorname{Spec}R,\mathcal O)=R\), since \(H^0(X,\mathcal O_X)=k\); hence the restricted map factors through \(V\). The factor is \(f(x_0,-)\). Separatedness makes the equalizer of the two global maps closed. Their coordinate functions agree on a dense open in the integral source, so agree everywhere. In the affine example both axis maps are zero, whereas \(f(1,1)=1\). Thus that map is not the claimed constant factorization.

**(b)** The total term dimensions are \(2,6,6,2\). Its differential has ranks \(1,3,2\), respectively, so the cohomology dimensions are
\[
 (1,\;2,\;1,\;0).
 \tag{CUX1}
\]
For explicit rank witnesses, the first map sends \(c_0\otimes a\) to \(c_0\otimes b\). The next map has independent images \(-c_1\otimes b,\ v\otimes d_0,\ v\otimes a-u\otimes b\). The last has independent images \(v\otimes b,\ v\otimes d_1\). These vectors remain independent in every characteristic. The sign test is
\[
 d(u\otimes a)=v\otimes a-u\otimes b,\qquad
 d^2(u\otimes a)=v\otimes b-v\otimes b=0.
 \tag{CUX2}
\]
In characteristic two the two minus signs become plus signs, and the two equal summands still sum to zero. Omitting the sign over a field of characteristic other than two would give \(2v\otimes b\), a nonzero error. The two degree-one classes are the cohomology generator from each factor tensored with the degree-zero generator of the other.

**(c)** Nilpotent lifting of local free generators makes the transition ratios one modulo the square-zero ideal \(J\). Their differences from one are sections of \(\mathcal O_{E\times E}\otimes_kJ\); products add because \(J^2=0\). They form an additive Čech cocycle, with frame changes giving its boundaries. The restriction isomorphism CU2 tensored with \(J\) says that a class vanishing on both axes is zero, so those frame changes trivialize the line. Proper constants then allow simultaneous normalization of the two axes.

For the counterexample take a nonboundary \(c_{ij}\) on \(E\), and use
\[
 g_{ij}=1+\epsilon c_{ij},\qquad \epsilon^2=0,
 \tag{CUX3}
\]
pulled back from the first factor. It is trivial on the closed fibre and on \(\{0\}\times E\) over the full dual-number base. Its restriction to \(E\times\{0\}\) is the original nontrivial deformation: a trivialization would reduce to a nonzero constant, which can be divided out, leaving units \(1+\epsilon a_i\) and forcing \(c\) to be a boundary. Thus that second axis is the one that fails. The nonzero genus-one class is supplied by the written genus-one cohomology, not by an existence citation.

**(d)** Since \(R\) is a domain, multiplication by \(t^m\) has zero kernel over \(R\). Over \(R_r=R/(t^r)\),
\[
 H^0=
 \begin{cases}
 R_r,&r\le m,\\
 (t^{r-m})R_r,&r>m.
 \end{cases}
 \tag{CUX4}
\]
The second description follows by comparing the first nonzero coefficient of a polynomial representative of degree below \(r\). A cycle reducing to one exists exactly when \(r\le m\). Given any finite upper bound on the tests, choose \(m\) at least that bound; all of those quotients miss the nonzero outgoing matrix. CU4 uses all powers, and DFR3 makes their intersection zero. It does not infer a zero matrix from finitely many quotient tests or from the closed fibre alone.

**(e)** On the face \(z=0\), the sum and projection factors cancel in pairs except for the constant line \(e^*L\). The additional inverse constant factor, or the normalized \(\widetilde L\), cancels this last factor as well. At \(n=-2\) the exponents in CU9 are one and three:
\[
 [-2]^*L\simeq L\otimes([-1]^*L)^3.
 \tag{CUX5}
\]
Constant field lines can be removed for this isomorphism of classes. For a symmetric line it is \(L^4\). The second formula is
\[
 G_{-2}\simeq M^3\otimes N^{-2}\otimes Q^3.
 \tag{CUX6}
\]
It follows by substituting \(-2\) in \(G_n=G_0(G_1G_0^{-1})^nQ^{n(n-1)/2}\), or by running the recurrence backwards twice. In particular the signs and the factor three are forced by the integer second difference.

**(f)** Let \(R=k[x,y]_{(x,y)}\). All height-one primes lie in its punctured spectrum. A rational function regular there has no height-one denominator factor; unique factorization therefore makes it an element of \(R\). Thus the punctured spectrum has coordinate ring \(R\). Were it affine, its structural open immersion, inducing the identity ring map, would be an isomorphism onto \(\operatorname{Spec}R\), contradicting the missing maximal point. The same argument applies to the factorial local ring at a generic boundary component of codimension at least two: the localized affine intersection would be precisely such a punctured spectrum. This is the purity mechanism used before constructing \(D\).

For \(S=\{0,P\}\),
\[
 \{a:a+S=S\}=\{0\},\qquad S-S=\{0,P,-P\}.
 \tag{CUX7}
\]
A stabilizing translation must send zero into \(S\), so is zero or \(P\). Translation by \(P\) fails, since \(2P\) is neither zero nor \(P\) when \(P\) has order five. In contrast the difference set records the existence of a pair of points, not preservation of the entire support. Conditions CU12 require both inclusions for every support point. They define a closed subscheme which lies in the affine complement because a stabilizing translation sends zero into that complement. Properness and coherent finiteness then make it finite.

**(g)** The binomial formula gives
\[
 u^q=1+ct^q,\qquad
 u^{-1}=\frac{u^{q-1}}{1+ct^q},\qquad
 (u^{-1})^q=(1+ct^q)^{-1}.
 \tag{CUX8}
\]
Both powers on the right belong to \(B\); the original \(u\) need not. For line transitions, powers preserve the unit inverses and cocycle equations, giving actual descent data on the descended open cover. Section coefficients obey the same formula and glue with the powered transitions.

On the coordinate chart the projective map is \(k[s]\to k[t]\), \(s\mapsto t^q\). The basis \(1,t,\ldots,t^{q-1}\) proves degree \(q\) and local freeness. Its full zero fibre is
\[
 \operatorname{Spec}k[t]/(t^q),
 \tag{CUX9}
\]
of length \(q\) and with one geometric point. The other projective chart gives the same finiteness and the corresponding infinity fibre. A point count of one would lose the entire inseparable degree.

**(h)** The actual genus-one calculation gives \(h^0(E,\mathcal O(0))=1\), no positive cohomology of that line, and \(h^0(E,\mathcal O(2(0)))=2\), again with no positive cohomology. The line \(L\) is their external tensor product. The signed tensor calculation in CU2 consequently gives
\[
 h^0(A,L)=1,\quad H^i(A,L)=0\ (i>0),\qquad
 h^0(A,L^2)=2^g.
 \tag{CUX10}
\]
The complete system of \(L^2\) is the product of the degree-two genus-one maps to \(\mathbf P^1\), followed by Segre. Its image is the Segre product and its finite degree is \(2^g\): on product affine charts the finite free ranks multiply by tensoring their bases. This includes inseparable or ramified fibres. The line is symmetric, and CU8 gives
\[
 \deg[n]=n^{2g}\quad(n\ne0).
 \tag{CUX11}
\]
None of these degrees is the number of geometric points in a characteristic-primary fibre.

**(i)** Suppose \(\sum_i c_i a_{i,r}=0\). Multiplying by \(\ell^{r-1}\) gives a relation in the chosen basis at level one, so every \(c_i\) is divisible by \(\ell\). Writing \(c_i=\ell d_i\) gives \(\sum_i d_i a_{i,r-1}=0\); induction makes \(d_i\) divisible by \(\ell^{r-1}\), hence \(c_i=0\) modulo \(\ell^r\). The equal cardinalities prove that these lifted generators form a basis. Arbitrary unrelated bases at successive levels need not put the transition maps into reduction coordinates.

The resulting Tate module is free of rank \(2g\), and its quotient modulo \(\ell^r\) is the actual \(A[\ell^r](\bar k)\). Its topology is the inverse-limit topology, whose open neighbourhoods of zero are the kernels of these reductions. A compatible basis is an abstract module basis; it need not be Galois invariant. Galois acts continuously by integral matrices, because it acts continuously at every finite étale level.

**(j)** Here \(g=2\), so
\[
 N=6^4=1296=2^4\,3^4,\qquad
 [T_2(E^2):T_2[6](T_2(E^2))]=2^4=16.
 \tag{CUX12}
\]
The matrix is \(6I_4\). If \(E[3]\) has one point, the point kernel on \(E^2\) has \(2^4=16\) points, each of local length \(3^4=81\). If \(E[3]\) has three points, its point kernel has \(2^4\,3^2=144\) points, each of length \(3^2=9\). The coprime splitting gives the stated products; translation makes all the local lengths equal, and their sum is \(N\). Both cases have the same two-primary point order and the same two-adic determinant valuation, four.

For the other matrix, the exponents \(\sum_i\min(a_i,r)\) at \(r=1,2,3,4\) are \(3,5,7,8\). Thus the four orders and the final index are
\[
 8,\quad32,\quad128,\quad256;\qquad
 \text{integral index }256.
 \tag{CUX13}
\]
The largest elementary-divisor exponent is four, so later reductions have that same cokernel order.

**(k)** In compatible Tate coordinates the matrix has blocks \(2I_2,0I_2,5I_2\), so its determinant is zero. The middle copy \(T_3E\simeq\mathbf Z_3^2\) is a nonzero Tate submodule in the kernel. Both nonzero coordinate multiplications are surjective isogenies, including \([5]\) in characteristic five. The image is therefore \(E\times\{0\}\times E\), of dimension two.

For any line \(H\), CE4 makes the Euler polynomial of its pullback have degree at most two. EH6 makes the same polynomial
\[
 \chi(E^3,(f^*H)^n)=n^3\chi(E^3,f^*H).
 \tag{CUX14}
\]
Its cubic coefficient must vanish. Thus \(\chi(E^3,f^*H)=0\), in agreement with both the geometric image bound and the singular Tate matrix. No claim that the higher direct images vanish is used.

**(l)** In CU10 the exponents of three fixed lines are \(1,n,n(n-1)/2\). A monomial of total line degree at most \(g\) in CE2 becomes a polynomial in \(n\) of degree at most \(2g\). Since the ample denominator in the Euler ratio is a fixed positive constant by EH7, the same bound holds for \(\delta(nf+h)\). CU8 gives the multiplication degree \(n^{2g}\); multiplicativity for finite isogenies and the smaller-image case give the stated homogeneity of \(\delta\). These facts supply the field geometry used by the characteristic-polynomial interpolation. They do not construct the toric monodromy pairing, the general semistable comparison or its finite descent; those are the separate requirements of Theorem 2.4.

**Lemma 2.3 (potentially good compatibility, in every dimension).** If an abelian variety \(B/F\), over a characteristic-zero nonarchimedean local field, acquires good reduction over a finite extension, then all its \(V_\ell B\), \(\ell\ne p(F)\), have one Galois-invariant Frobenius-semisimple Weil–Deligne class over \(\overline{\mathbf Q}\); its monodromy is zero.

**Proof.** Choose a finite Galois extension \(F'/F\) of good reduction. The full graph-closure extension proof GQ1–GQ2 in §2A extends the descent action to its abelian scheme over \(\mathcal O_{F'}\). Reduction of invertible torsion is equivariant and identifies its Tate module with that of the special abelian variety \(B_0\). The finite étale lifting proof GQ3–GQ4 supplies this reduction, with every level and transition; GQ5 proves compatibility with the semilinear action. The common subgroup \(I_{F'}\) consequently acts trivially, so \(N_\ell=0\).

Write \(m(w)=-v(w)\) for the arithmetic residue exponent, opposite to the geometric exponent of Lesson 7. For \(m(w)\ge0\), the action of \(w\in W_F\) on special torsion is an algebraic endomorphism: compose the relative residue Frobenius with the descent isomorphism from the Frobenius-twisted special fibre back to \(B_0\). This is precisely the semilinear descent action of \(w\). Relative Frobenius is an isogeny, and the descent map is an isomorphism, so Lemma 2.2 gives rational characteristic polynomials independent of \(\ell\). For \(m(w)<0\), apply that assertion to \(w^{-1}\). Its Tate operator \(M\) is invertible by CU10. With \(P_M(T)=\det(T-M)\) and \(d=2\dim B\), the inverse characteristic polynomial is \(\det(T-M^{-1})=T^dP_M(T^{-1})/P_M(0)\), with \(P_M(0)\ne0\). Factoring into eigenvalues proves this reciprocal identity, as written explicitly in PM5 below. Thus every \(w\) has a common rational trace and characteristic polynomial, with its finite inertia component included.

For completeness, this character comparison gives a common algebraic isomorphism class. The fixed finite group \(I_F/I_{F'}\) works for every coefficient prime, without requiring that its action be faithful. Some power \(\Phi^m\) centralizes it. The unipotent part of \(\Phi\) consequently commutes with inertia: its \(m\)-th power is the unipotent part of that centralizing power, and the unipotent \(m\)-th root is its finite binomial polynomial. It commutes with the semisimple part of \(\Phi\) as well. Removing it preserves all traces of \(i\Phi^a\): the product of its nilpotent part with any commuting operator has trace zero, as follows by the filtration by kernels of its powers. After Frobenius semisimplification, \(\Phi^m\) is semisimple, with algebraic eigenvalues by Lemma 2.2. On an eigenspace with eigenvalue \(c\), choose an algebraic \(m\)-th root \(b\) of \(c\), and replace \(\Phi\) there by \(b^{-1}\Phi\). Inertia together with this operator is a representation of a finite cyclic extension of its finite inertia group, because the new operator has \(m\)-th power one. Over an algebraically closed field of characteristic zero, the group algebra of a finite group splits into matrix blocks: averaging complements gives semisimplicity, and Schur's lemma identifies a block with the full matrix algebra on its simple module. The simple modules can all be defined over \(\overline{\mathbf Q}\), by splitting that finite group algebra there. Thus the original semisimple Weil representation has an algebraic model.

Equal traces on every group element force equal simple multiplicities. One can see this without choosing complex embeddings: for the finite-dimensional semisimple image algebra, its central idempotents and matrix units isolate each simple block, and equality of trace functionals on their spanning group elements gives its multiplicity. This is also the characteristic-zero case of the proved Brauer–Nesbitt theorem in the first lesson. The common rational traces are fixed by every automorphism of \(\overline{\mathbf Q}\), so the common isomorphism class is Galois-invariant. ∎

### 2E. Period modules and their full monodromy calculation

A semistable comparison needs a calculation with the toric part, the good abelian part and the periods. We give that calculation for explicit integral period data, including a finite semilinear action and ramification. Applying it to every abelian variety still requires constructing the data and proving that their quotient has the variety's actual torsion.

Fix a finite Galois extension \(L/F\) of characteristic-zero nonarchimedean local fields. Put \(R=\mathcal O_L\), let \(p\) be the residue characteristic, let \(e=e(L/F)\), and write \(\Gamma=\operatorname{Gal}(L/F)\). The data in this section are:

- a smooth separated commutative finite-type \(R\)-group \(\mathcal G\), an abelian scheme \(\mathcal B/R\) of relative dimension \(a\), and a split torus \(\mathcal T=\mathbf G_{m,R}^{\,t}\), in an exact sequence of group schemes
\[
 0\longrightarrow\mathcal T\longrightarrow\mathcal G
                  \longrightarrow\mathcal B\longrightarrow0;
 \tag{PM1}
\]
- exactness here includes that \(\mathcal G\to\mathcal B\) is a \(\mathcal T\)-torsor for the faithfully flat topology;
- compatible semilinear \(\Gamma\)-actions on these schemes and maps, satisfying the group-action cocycle;
- a free lattice \(Y\simeq\mathbf Z^t\) with a \(\Gamma\)-action, and an equivariant injection \(u:Y\hookrightarrow G(L)\), where \(G=\mathcal G_L\).

These are supplied mathematical data, not consequences of a semistable reduction theorem asserted here. The action on generic fibres and scalar extension gives \(G(\bar F)\), and hence
\[
 Q=G(\bar F)/u(Y),
 \tag{PM2}
\]
a \(G_F\)-module. The quotient in (PM2) is an abstract commutative group; representability is not assumed. We compute its finite torsion and Tate modules directly.

The actual earlier inputs are CU8–CU10 for multiplication and Tate ranks; GQ3–GQ5 for prime-to-\(p\) finite étale lifting and semilinear good-model reduction; Lesson 3, FD1–FD5, for module, algebra and finite-cover morphism descent; Lesson 7, §§1–5 and §6A, for tame characters, the Weil–Deligne equivalence, Frobenius semisimplification, nilpotent blocks and the proved Tate uniformization; and Lemma 2.3 for the character argument on the good abelian part.

#### 2E.1. Finite multiplication on the supplied semiabelian scheme

**PM1.** For every positive integer \(n\) prime to \(p\),
\[
 0\longrightarrow\mathcal T[n]\longrightarrow\mathcal G[n]
                  \longrightarrow\mathcal B[n]\longrightarrow0
 \tag{PM3}
\]
is exact as faithfully flat group sheaves. The three kernels are finite étale of respective ranks \(n^t,n^{2a+t},n^{2a}\). Multiplication by \(n\) on \(\mathcal G\) itself is finite étale and surjective.

*Proof.* The coordinate algebras \(R[z_i^{\pm1}]/(z_i^n-1)\) give \(\mathcal T[n]\), with monomial basis and invertible derivatives \(nz_i^{n-1}\). On \(\mathcal B\), GQ3 proves étaleness by the square-zero correction. Proper finite-fibre finiteness makes multiplication finite. Its finite étale rank is constant on the connected \(R\); CU8 on its generic fibre gives \(n^{2a}\).

To lift a section of \(\mathcal B[n]\), first lift it to \(\mathcal G\) on a faithfully flat cover, using the given torsor. Its multiple by \(n\) belongs to \(\mathcal T\). Taking \(n\)-th roots in the torus, on a finite faithfully flat root cover, corrects the lift into \(\mathcal G[n]\). Two corrected lifts differ by \(\mathcal T[n]\). This proves exactness and the torsor assertion over \(\mathcal B[n]\).

Here is also an explicit local finiteness proof. A torsor under \(\mathbf G_m^t\) is locally the product of \(t\) frame torsors of invertible modules. Indeed its transition units give the one-dimensional descent data; FD1–FD4 construct the invertible modules, whose local bases trivialize their frame torsors. This argument uses no Picard representability. Over an affine open of \(\mathcal B[n]\) choose such a lift \(g\) into \(\mathcal G\). Its multiple \(ng\) has torus coordinates \(c_i\) which are units. The lifts lying in \(\mathcal G[n]\) have coordinate algebra
\[
 A[z_1^{\pm1},\ldots,z_t^{\pm1}]
                   /(z_i^n-c_i^{-1}:1\le i\le t).
 \tag{PM4}
\]
It is finite free of rank \(n^t\) over \(A\), with invertible Jacobian. These target-local descriptions prove finite étaleness of \(\mathcal G[n]\to\mathcal B[n]\), and its stated total rank.

Multiplication on \(\mathcal G\) is étale by smooth lifting and correction of its tangent error by \(n^{-1}\), exactly as in GQ3. It is surjective as a faithfully flat sheaf: lift a division of the image in \(\mathcal B\), then correct its torus multiple. Its two-fold fibre product is the kernel torsor, by \((g,h)\mapsto(g,g+h)\).

We spell out the descent used to conclude finiteness from this torsor. On an affine target choose a finite affine cover of the inverse image of the étale surjection. Its disjoint union is affine and faithfully flat over that target; after this cover the torsor is the product with the finite étale kernel. FD2–FD4 descend its finite locally free algebra and multiplication. The resulting affine scheme is the original source after the cover and therefore before it. To justify the last identification for maps, the proof FD5 applies also to a faithfully flat open cover: the inverse image of a target affine is saturated, and its image is open because the cover is open; coordinate maps descend by the faithful equalizer FD1, and glue. Étale openness was proved in EA1–EA18. Equality of maps is detected by that same equalizer. Thus the torsor is finite locally free. Its already proved étaleness completes the assertion. \(\square\)

#### 2E.2. The integral valuation quotient

Let \(X=\operatorname{Hom}_R(\mathbf G_m,\mathcal T)\), the cocharacter lattice. A split coordinate system identifies it with \(\mathbf Z^t\).

**PM2.** There is a canonical group isomorphism
\[
 G(L)/\mathcal G(R)\xrightarrow{\ \sim\ }X.
 \tag{PM5}
\]
For the supplied periods it gives an integral map \(\nu_L:Y\to X\). It is \(\Gamma\)-equivariant. Under a further finite extension \(L'/L\) and base change of the supplied model, it is multiplied by \(e(L'/L)\).

*Proof.* The image of \(g\in G(L)\) in \(B(L)\) extends uniquely to \(\mathcal B(R)\). Here is the point version of the actual graph argument GQ2. Its integral generic graph closure is proper and flat over the DVR. Its generic fibre has dimension zero, and GQ1's primitive-coefficient dimension bound gives dimension at most zero for its special fibre. Proper finite-fibre finiteness makes the graph closure finite over \(R\). Its finite birational coordinate ring is contained in the fraction field of the normal DVR \(R\), so equals \(R\), exactly as in GQ2. Separatedness gives uniqueness. The inverse-image torus torsor of this section has an \(R\)-section: the frame description in PM1 reduces this to invertible modules over the local ring \(R\), and each such module is free by finite Nakayama and its rank-one basis map. Choose an integral lift \(g_0\). Then \(g-g_0\in T(L)\), and its coordinate valuations define a cocharacter.

Two choices of \(g_0\) differ by \(\mathcal T(R)\). In fact an integral section which lies generically in \(T\) maps to zero in \(\mathcal B\) everywhere, since \(\mathcal B\) is separated and \(\operatorname{Spec}R\) integral. Torus units have valuation zero. This proves independence. Products of integral lifts prove additivity. The kernel consists precisely of integral sections, and every vector occurs using powers of a uniformizer in the torus. This proves (PM5).

For clarity, group automorphisms of the split torus over connected \(R\) have integer invertible matrices. In one coordinate, compare coefficients in the grouplike identity for a Laurent polynomial. Its different coefficients are orthogonal idempotents, their sum is one, and each is idempotent. Connectedness leaves one coefficient equal to one. Thus every coordinate is a monomial; an inverse gives an inverse integer exponent matrix. This also proves the natural cocharacter description used above. The semilinear actions preserve integral sections, and field automorphisms preserve the valuation. Therefore (PM5) and \(\nu_L\) are equivariant.

A uniformizer of \(L\) has valuation \(e(L'/L)\) in \(L'\), while an \(R\)-unit remains a unit. Base-changing the chosen integral lift consequently multiplies every valuation by this factor. Hence the normalized rational map
\[
 \nu=\frac1{e(L/F)}\,\nu_L:
          Y_{\mathbf Q}\longrightarrow X_{\mathbf Q}
 \tag{PM6}
\]
is unchanged under further base change of these data. \(\square\)

#### 2E.3. Every torsion level and every transition

**PM3.** For \(\ell\ne p\), all finite torsion groups and transitions give exact sequences
\[
 \begin{gathered}
 0\longrightarrow T_\ell T\longrightarrow T_\ell G
                         \longrightarrow T_\ell B\longrightarrow0,\\
 T_\ell T=X\otimes_{\mathbf Z}\mathbf Z_\ell(1),\\
 0\longrightarrow T_\ell G\longrightarrow T_\ell Q
                         \longrightarrow Y\otimes\mathbf Z_\ell\longrightarrow0.
 \end{gathered}
 \tag{PM7}
\]
Their free ranks are \(t,2a+t,2a,2a+2t,t\), respectively. The action on \(T_\ell G\) is unramified over \(L\). All finite and inverse-limit actions are continuous.

*Proof.* The torus assertion follows by evaluating cocharacters on roots of unity. PM1 and the strict-Henselian splitting proof GQ4 identify every generic torsion level of \(\mathcal G\) with its special level, equivariantly. Over the strict unramified extension all of these finite étale schemes are constant. Thus inertia of \(L\) acts trivially.

On geometric points (PM3) is exact. Its transition maps are multiplication by \(\ell\), and taking inverse limits is exact here by an explicit correction. Given a compatible sequence in \(B[\ell^r]\), lift its first term. If a lift at level \(r+1\) has multiple different from the already chosen lift at level \(r\), their difference is in \(T[\ell^r]\). Lift that difference to \(T[\ell^{r+1}]\) and subtract it. This makes the lifts compatible. Surjectivity of the torus transitions and CU9 give the first sequence and ranks.

On \(G(\bar F)\) multiplication by every positive integer is surjective: lift a division in the abelian quotient, and correct the difference by a torus division over the algebraically closed field. Since \(Y\) is free and \(u\) injective, it meets \(G[n]\) trivially. The torsion in the abstract quotient (PM2) therefore satisfies
\[
 0\longrightarrow G[\ell^r](\bar F)\longrightarrow Q[\ell^r]
           \longrightarrow Y/\ell^rY\longrightarrow0.
 \tag{PM8}
\]
For the last map, a lift \(g\) of a quotient point has \(\ell^r g=u(y)\); take \(y\) modulo \(\ell^rY\). Changing \(g\) by a period has exactly that effect. Surjectivity follows by dividing \(u(y)\) in \(G(\bar F)\). This proves all parts of exactness, and gives the order \(\ell^{r(2a+2t)}\).

To see the inverse-limit surjection directly, fix a basis \(y_j\) of \(Y\) and compatible divisions \(g_{j,r}\) of \(u(y_j)\), chosen recursively with \(\ell g_{j,r+1}=g_{j,r}\). Their classes give compatible lifts of the basis of \(Y/\ell^rY\). Together with \(T_\ell G\) these prove the second sequence in (PM7). Its free quotient and the first sequence's free quotient split as \(\mathbf Z_\ell\)-modules by lifting bases. This proves the asserted freeness, without claiming equivariant splittings.

The finite-level identifications are actual as well. Multiplication by \(\ell\) surjects on \(G(\bar F)\); its finite kernels have orders \(\ell^{r(2a+t)}\). The compatible-basis proof CU9 therefore applies with rank \(2a+t\), identifying \(T_\ell G/\ell^r\) with \(G[\ell^r]\). Add the compatible period lifts to those basis vectors. A relation at finite level first gives zero coefficients in the free quotient \(Y/\ell^rY\), and then in \(G[\ell^r]\); their cardinalities give a basis of the whole (PM8). Thus \(T_\ell Q/\ell^r\simeq Q[\ell^r]\), naturally with its transitions.

Each finite-level set is finite and consists of classes represented by algebraic points. Fixing their representatives and the finite lattice action gives an open subgroup of \(G_F\) fixing them all. The finite actions are continuous; the inverse-limit topology gives continuity on the Tate modules. \(\square\)

#### 2E.4. The entire inertia operator and the ramification factor

Choose compatible roots of unity, and use the same basis \(\tau_\ell\) of \(\mathbf Z_\ell(1)\) for the tame characters of \(F\) and \(L\). Write \(V_\ell(-)=T_\ell(-)\otimes\mathbf Q_\ell\), and let \(\operatorname{pr}:V_\ell Q\to Y\otimes\mathbf Q_\ell\).

**PM4.** On \(I_L\) the action is
\[
 \rho_\ell(\sigma)=1+t_{\ell,L}(\sigma)N_L,\qquad
 N_L=\operatorname{incl}\circ(\nu_L\otimes\tau_\ell)
                                  \circ\operatorname{pr},\qquad N_L^2=0.
 \tag{PM9}
\]
Relative to the tame character of \(F\), its monodromy is
\[
 N_F=\frac1e\,N_L
     =\operatorname{incl}\circ(\nu\otimes\tau_\ell)
                                      \circ\operatorname{pr}.
 \tag{PM10}
\]

*Proof.* It suffices to compute a compatible lift of each period basis vector. Write \(u(y_j)\) as an integral section plus a torus point. Split each torus coordinate into a power of a uniformizer \(\pi_L\) and a unit. Integral sections have compatible \(\ell\)-power divisions over the strict unramified ring: pull back the finite étale surjection of PM1 and use GQ4 at every level. The roots can be chosen recursively. Units likewise have all compatible \(\ell\)-power roots in the unramified field, by residue-field roots and Hensel's invertible derivative, as in Lesson 7, Proposition 6.3.

Only powers of \(\pi_L^{1/\ell^r}\) contribute to inertia. The difference between a division and its conjugate is the root of unity raised to the coordinate valuation times \(t_{\ell,L}(\sigma)\). Thus its toric Tate cocycle is \(\nu_L(y_j)t_{\ell,L}(\sigma)\tau_\ell\). Inertia is the identity on \(T_\ell G\) and \(Y\), so this gives the whole matrix in (PM9), not only an associated graded statement. Its square is zero because the image lies in \(T_\ell T\subset T_\ell G\), on which it vanishes. Arbitrary choices of division points give the same inertia matrix: their differences lie in the unramified \(T_\ell G\).

Write \(\pi_F=v\pi_L^e\), with \(v\) a unit of \(R\). Its prime-to-\(p\) roots can be chosen unramified over \(L\). Comparing its compatible roots with those of \(\pi_L\) gives
\[
 t_{\ell,F}|_{I_L}=e\,t_{\ell,L}.
 \tag{PM11}
\]
The tame-character image on \(I_L\) contains nonzero values, by the full radical-tower proof in Lesson 7. The polynomial logarithm of (PM9), in the fixed convention \(\rho(\sigma)=\exp(t_{\ell,F}(\sigma)N_F)\), is therefore \(N_L/e\). This is (PM10), also when \(\ell\) divides \(e\). Its entries need not be integral on the displayed lattice in that case. \(\square\)

#### 2E.5. Equivariance and the good abelian part

**PM5.** Let \(\rho_X,\rho_Y\) denote the rational finite-image representations of \(W_F\) on \(X_{\mathbf Q},Y_{\mathbf Q}\). The normalized map \(\nu\) intertwines them. In the associated Weil–Deligne representation, the three supplied graded representations are
\[
 X_{\mathbf Q_\ell}\|\cdot\|,\qquad
 D_{B,\ell},\qquad Y_{\mathbf Q_\ell},
 \tag{PM12}
\]
in that order. The middle, after Frobenius semisimplification, has a common Galois-invariant algebraic class \(D_B\) for all \(\ell\ne p\).

*Proof.* Equivariance of \(\nu\) is PM2. Both lattice actions factor through the finite \(\Gamma\); they are integer representations. On torus torsion the full action is the cocharacter action tensored with the cyclotomic action. With Lesson 7's geometric Frobenius convention the latter is \(\|\cdot\|\): roots of unity are unramified and geometric Frobenius raises their coordinates by \(q_F^{-1}\). This proves the bottom representation; the quotient is the given \(Y\).

The filtration in (PM7) is stable under the full action. Its monodromy vanishes on \(V_\ell G\) and on the quotient \(Y_{\mathbf Q_\ell}\), by PM4. Removing the exponential in the Weil–Deligne equivalence therefore leaves the usual action on both \(V_\ell G\) and that quotient. The middle quotient of \(V_\ell G\) is \(V_\ell B\), with its supplied semilinear action.

Apply the character argument of Lemma 2.3 to this good abelian model and its specified actions. Reduction on every torsion level is equivariant by GQ4–GQ5. Write \(m(w)=-v(w)\) for the arithmetic residue exponent, opposite to Lesson 7's geometric exponent. For \(m(w)\ge0\), the action of \(w\), with its finite descent component included, is the corresponding relative algebraic Frobenius composed with the semilinear isomorphism of the special fibre. Lemma 2.2 gives rational traces and characteristic polynomials independent of \(\ell\).

For a negative exponent apply that assertion to the inverse Weil element. Its positive-exponent operator \(M\) is invertible by CU10. If \(P_M(T)=\det(T-M)\) and \(b=2a\), then
\[
 \det(T-M^{-1})=\frac{T^bP_M(T^{-1})}{P_M(0)}.
\]
Indeed, after scalar extension write the eigenvalues as \(\alpha_i\ne0\); both sides are \(\prod_i(T-\alpha_i^{-1})\). The constant term \(P_M(0)\) is a nonzero rational number independent of the coefficient prime. This proves the negative-exponent comparison without requiring an inverse isogeny in the rational endomorphism algebra.

The finite-inertia and Frobenius-semisimplicity argument in Lemma 2.3 now gives the common algebraic class and its Galois invariance. This argument uses the given semilinear good-model actions; it does not identify a ramified integral action with faithfully flat integral descent. \(\square\)

#### 2E.6. Full block reconstruction, including degenerate valuation maps

Define
\[
 U=\operatorname{im}\nu,\qquad Y_0=\ker\nu,\qquad
 X_0=X_{\mathbf Q}/U,\qquad d=\operatorname{rank}_{\mathbf Q}\nu.
 \tag{PM13}
\]
These are finite-image rational \(W_F\)-representations. Write \(\mathrm{Sp}(2)\) for the block with \(r(w)=\operatorname{diag}(\|w\|,1)\) and \(Ne_2=e_1\).

**PM6.** The full Frobenius-semisimple Weil–Deligne class of \(V_\ell Q\) is
\[
 D_B\ \oplus\ X_0\|\cdot\|\ \oplus\ Y_0\
                              \oplus\bigl(U\otimes\mathrm{Sp}(2)\bigr).
 \tag{PM14}
\]
It is common and Galois-invariant over \(\overline{\mathbf Q}\), for all coefficient primes. If \(\nu\) is an isomorphism, this becomes
\[
 D_B\oplus\bigl(X_{\mathbf Q}\otimes\mathrm{Sp}(2)\bigr).
 \tag{PM15}
\]
In that case the centered nilpotent filtration is
\[
 0\subset\operatorname{im}N=X_{\mathbf Q_\ell}(1)
 \subset\ker N=V_\ell G\subset V_\ell Q,
 \quad
 \operatorname{gr}_{-1}=X(1),\quad
 \operatorname{gr}_0=V_\ell B,\quad
 \operatorname{gr}_1=Y_{\mathbf Q_\ell}.
 \tag{PM16}
\]

*Proof.* The unipotent Frobenius component commutes with \(N\) and preserves the two stable subspaces of (PM7), by Lesson 7, Proposition 4.1. Removing it preserves the induced graded representations and \(N\). The resulting smooth Weil representation is semisimple by the proved Lemma 4.0 of that lesson. We may consequently split its invariant subspaces and quotients equivariantly.

In such splittings, \(N\) is zero on \(V_\ell G\), maps the lifted \(Y\) into the toric subspace, and is exactly the matrix \(\nu\) there, with the fixed Tate basis. The finite-group averaging argument splits \(\ker\nu\) and \(\operatorname{im}\nu\) over \(\mathbf Q\): average any projection over the finite image of \(\Gamma\), dividing by its order. On a complement to the kernel, \(\nu\) is an equivariant rational isomorphism to \(U\). Use that isomorphism to identify the two linked summands. Their lower action is \(\rho_U\|\cdot\|\), their upper action is \(\rho_U\), and the nilpotent map is the identity from upper to lower. This is \(U\otimes\mathrm{Sp}(2)\). The two remaining lattice quotients have zero monodromy, and the middle is \(D_B\). This proves (PM14).

All spaces, maps and finite lattice actions in this construction are rational and independent of \(\ell\); the middle has the common algebraic class from PM5. Extending them along any embedding into \(\overline{\mathbf Q}_\ell\) gives the original class. Every automorphism of \(\overline{\mathbf Q}\) fixes the rational summands and preserves the class of \(D_B\), proving the asserted Galois invariance. No choice of complements changes the resulting isomorphism class.

If \(\nu\) is invertible, its kernel and cokernel are zero, giving (PM15) and (PM16). More generally the nilpotent filtration for \(N^2=0\) is \(\operatorname{im}N\subset\ker N\subset V\), with the map from the top quotient to the bottom an isomorphism. The explicit matrix proves this assertion and the stated centered indices; it makes no assertion of a geometric weight theorem. \(\square\)

#### 2E.7. Conductors of the computed modules

**PM7.** Let \(a(-)\) be the Artin conductor of a finite-inertia Weil representation, and let \(I=I_F\) act through the given finite image on the lattice spaces. Then
\[
 a(D_Q)=a(D_B)+a(X_{\mathbf Q})+a(Y_{\mathbf Q})+\dim U^I.
 \tag{PM17}
\]
If \(\nu\) is invertible,
\[
 a(D_Q)=a(D_B)+2a(X_{\mathbf Q})+\dim X_{\mathbf Q}^{\,I}.
 \tag{PM18}
\]
Over \(L\) the conductor is \(d\), and is \(t\) in the invertible case.

*Proof.* The underlying semisimple Weil representation has the three constituents (PM12). Unramified twists do not change inertia or its ramification filtration, so its Artin conductor is the sum of the first three terms in (PM17). The Weil–Deligne conductor formula proved in Lesson 7, equation (22), adds \(\dim V^I-\dim(\ker N)^I\). Taking invariants is exact for the finite inertia image over characteristic zero: average a lift over that finite group. Consequently this difference is the dimension of the invariant image of \(N\), namely \(\dim U^I\); the Tate twist is trivial on inertia. This proves (PM17), including wild finite inertia. If \(\nu\) is invertible, \(Y_{\mathbf Q}\simeq X_{\mathbf Q}\) and \(U=X_{\mathbf Q}\), proving (PM18).

Over \(L\) both lattice actions and the good abelian action are unramified. The underlying Weil conductor is zero, and (PM9) gives monodromy rank \(d\). Thus the conductor there is exactly \(d\). All these formulas concern the modules just computed from the supplied data. \(\square\)

#### 2E.8. Actual Tate products and ramified quadratic interchange

**PM8.** The calculation applies to actual products of the proved Tate curves and good abelian varieties. It also gives an explicit two-dimensional example with ramified finite descent.

*Proof.* For split data \(G=B\times\mathbf G_m^t\), put the \(j\)-th period in its \(j\)-th torus coordinate, with parameter \(q_j\) of positive valuation. Lesson 7, §6A proves the full Galois-equivariant Tate quotient at every torsion level. Taking products therefore identifies (PM2) with
\[
 \bigl(B\times E_{q_1}\times\cdots\times E_{q_t}\bigr)(\bar F),
 \qquad \nu_F=\operatorname{diag}(v_F(q_1),\ldots,v_F(q_t)).
 \tag{PM19}
\]
Thus (PM15) proves its complete local comparison, with the given integral period factors retained in (PM10).

For a ramified example let \(F\) have odd residue characteristic, let \(\pi_F\) be a uniformizer, and put \(L=F(\pi)\), with \(\pi^2=\pi_F\). The Eisenstein polynomial gives a ramified quadratic extension; its nontrivial automorphism is \(\sigma(\pi)=-\pi\). On \(\mathcal G=\mathbf G_{m,R}^2\) take the semilinear action which applies \(\sigma\) to coefficients and interchanges the coordinates. Let \(\sigma\) interchange \(y_1,y_2\), and set
\[
 u(y_1)=(\pi,1),\qquad u(y_2)=(1,-\pi),\qquad
 \nu_L=I_2,\quad e=2,\quad \nu=\tfrac12 I_2.
 \tag{PM20}
\]
Both period parameters have positive valuation. The two displayed periods are interchanged by the semilinear action, including its sign, so the injection is equivariant and its action has square one.

Over \(L\) the actual abelian variety is \(E_\pi\times E_{-\pi}\). Applying \(\sigma\) to the Tate equations and uniformization interchanges those two curves. Interchanging the factors accordingly defines a semilinear action satisfying the cocycle. It descends to a projective group variety over \(F\). Here is an effective descent justification. Tensor a very ample line with all its conjugates; the permutation isomorphisms give its descent datum, and a sufficiently high power is very ample by Segre. FD2 descends its finite-dimensional section space. Its resulting equivariant projective embedding has a stable homogeneous ideal; FD3 descends that ideal, on homogeneous coordinate charts, to give a projective \(F\)-scheme with the prescribed scalar extension. Addition, inverse and origin descend by FD5 under the finite faithfully flat field cover, and their identities are detected after that cover. The standard Jacobian test SF1–SF3 and geometric scalar extension detect smoothness and geometric integralness. Thus the descended object is an abelian variety of dimension two, with the stated action on its actual Tate module.

Let \(\eta\) be the ramified quadratic character of \(L/F\). The permutation lattice is \(1\oplus\eta\) over \(\mathbf Q\). Formulas (PM15), (PM18) and (PM20) give
\[
 D=(1\oplus\eta)\otimes\mathrm{Sp}(2),\qquad
 N_F=\tfrac12 N_L,\qquad a(D)=2\cdot1+1=3.
 \tag{PM21}
\]
Here \(\eta\) is tame, of conductor one; its permutation representation has one-dimensional inertia invariants. This includes coefficient prime two: the rational monodromy normalization is still one half, while its Weil–Deligne block class is unchanged by the allowed basis isomorphism. \(\square\)

The general geometric construction in Theorem 2.4 must supply the semiabelian integral extension, periods and locally covering maps with compatible finite model actions. PM1–PM7 compute the module for specified period data, and PM8 supplies the stated actual product families and ramified example. Section 2F proves that a local-field period presentation has a full-rank valuation pairing and gives every actual torsion level and transition. The existence and covering properties of that presentation for arbitrary abelian varieties remain to be constructed.

Free primary comparisons are Brian Conrad's [*Semistable reduction for abelian varieties*, author lecture notes](https://math.stanford.edu/~conrad/DarmonCM/2011Notes/SemistableReduction.pdf), for finite torsion and reduction filtrations, and Matthew Bisatt's [*Explicit root numbers of abelian varieties*, author preprint](https://arxiv.org/abs/1711.09961), for the abelian and special-block decomposition. Bisatt uses the cohomological dual Tate convention; the twists here follow Lesson 7's homological convention. The torsor equations, full inertia cocycle, normalized ramification factor, equivariant splitting and example used here have proofs in this section.

#### 2E.9. Graded exercise: periods, ramification and finite descent

This exercise is worth **100 points**, with **10 points for each part**. Use the supplied period data of §2E unless a part specifies an abstract matrix example. Keep finite torsion, integral Tate modules and rational Weil–Deligne classes distinct.

**(a) Finite ranks.** Take \(a=2,\ t=3,\ n=8\), with residue characteristic five. Compute the ranks of \(\mathcal T[n]\), \(\mathcal B[n]\), \(\mathcal G[n]\), the order of \(Q[n]\), and the ranks of the toric, semiabelian and quotient Tate modules in (PM7). Explain why the local root algebra (PM4) remains finite étale when its unit coefficients have no roots in the original ring.

**(b) Valuations and units.** In the split torus over a local field with uniformizer \(\pi\), take
\[
 u(y_1)=(\pi^2c_1,c_2),\qquad
 u(y_2)=(\pi c_3,\pi^3c_4),\qquad c_i\in R^\times.
\]
Find \(\nu_F\), prove injectivity of \(u:\mathbf Z^2\to G(F)\), and compute the monodromy rank of the abstract quotient. Which inertia calculations can the units change? No proper quotient variety is assumed.

**(c) The quotient at every level.** Prove the exact sequence (PM8), including its last map and its transition compatibility. For the rank-two torus example in (b), compute the three group orders at level \(n=4\). Explain how compatible divisions of a period basis give a surjection on inverse limits, and why this gives a saturated integral submodule \(T_\ell G\subset T_\ell Q\).

**(d) A nonprimitive monodromy image.** For
\[
 M=\begin{pmatrix}2&1\\0&3\end{pmatrix},\qquad
 N=\begin{pmatrix}0&M\\0&0\end{pmatrix},
\]
take inertia matrices \(1+tN\), with \(t\) ranging over \(\mathbf Z_\ell\), and residue characteristic five. Compute the ranks of \(N\), \(N^2\), the integral invariants and the invariants modulo \(\ell^r\), for \(\ell=2,3,7\). Determine the Smith factors of \(M\). Does reduction modulo \(\ell^r\) commute with taking these inertia invariants?

**(e) Normalize the ramified example.** For (PM20), use \(t_F|_{I_L}=2t_L\) to recover the inertia matrix at \(t_L=1\). Compare the correct \(N_F\) with the choices \(N_L\) and \(2N_L\). Under further base change of ramification index three, compute the new integral valuation map and verify the unchanged rational \(\nu\). Check the covariance with geometric Frobenius.

**(f) Injective periods with degenerate valuation.** Take \(F=\mathbf Q_p\), \(p\) odd, a good abelian factor of dimension one, and two torus periods
\[
 u(y_1)=(p^2,p),\qquad
 u(y_2)=(p^4(1+p),p^2).
\]
Show that \(u\) is injective but \(\nu\) has rank one. Compute \(U,Y_0,X_0\), the dimension of the full module, its nilpotent filtration dimensions and its block decomposition. Show that the period subgroup is not discrete in the torus topology.

**(g) Why a character is insufficient.** Compare the two Weil–Deligne pairs with
\[
 r(w)=\begin{pmatrix}\|w\|&0\\0&1\end{pmatrix},
 \qquad
 N_1=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad N_0=0.
\]
They have the same trace on every Weil element. Prove they are not isomorphic and compute their conductors when their finite inertia action is trivial. Explain which additional datum in PM6 distinguishes them.

**(h) Rational finite descent at coefficient prime two.** Let a group of order two interchange the coordinates of \(X=Y=\mathbf Q^2\), and let \(\nu=\tfrac12I_2\). Compute the invariant and anti-invariant subspaces, their projection matrices and the index of their integral eigenlattice in \(\mathbf Z_2^2\). In the tamely ramified situation of (PM20), compute \(a(X)\), \(\dim X^I\), the conductor over \(F\), and the conductor after passage to \(L\).

**(i) Inverting Frobenius.** If an invertible arithmetic Frobenius operator has characteristic polynomial \(T^2-bT+q\), compute the polynomial of its geometric inverse. Prove the general reciprocal identity used in PM5. Why does this suffice for comparison of negative arithmetic residue exponents without constructing an inverse quasi-isogeny?

**(j) The remaining geometric application.** List the actual geometric constructions needed to apply PM1–PM7 to every abelian variety in Theorem 2.4. Distinguish them from the constructions proved for the actual families in PM8. Explain why a semilinear integral group action alone is not a faithfully flat descent datum for a ramified extension of DVRs.

**Complete solution.**

**(a)** The respective orders are
\[
 8^3=512,\qquad 8^4=4096,\qquad
 8^7=2097152,\qquad 8^{10}=1073741824.
 \tag{PMX1}
\]
The ranks of \(T_\ell T,T_\ell G,T_\ell Q\) are \(3,7,10\); the good abelian quotient has rank four and the period quotient rank three. Each equation \(z_i^8=c_i^{-1}\) has the free monomial basis of exponents from zero to seven. The constant term is a unit, so \(z_i\) is a unit; its derivative \(8z_i^7\) is a unit in residue characteristic five. The finite Jacobian criterion therefore proves étaleness over the original ring. Having sections over that ring is a separate matter: the algebra becomes a product after a suitable étale extension.

**(b)** Valuation ignores the four units, giving
\[
 \nu_F=\begin{pmatrix}2&1\\0&3\end{pmatrix},
 \qquad \det\nu_F=6.
 \tag{PMX2}
\]
If a product of periods is the identity, its exponent vector lies in the kernel of this matrix. That rational kernel is zero, so both integer exponents are zero. Thus \(u\) is injective. On the four-dimensional quotient Tate module, monodromy maps the two-dimensional period quotient to the two-dimensional toric subspace by this matrix, so has rank two and square zero.

All compatible prime-to-\(p\) roots of a unit can be chosen in the maximal unramified extension, by the residue roots and Hensel lifting. They therefore contribute zero to its inertia Kummer cocycle. The units do not change this monodromy matrix or its Frobenius-semisimple block class. This computation supplies no representability or polarization assertion for the abstract quotient.

**(c)** Represent a class killed by \(n\) by \(g\in G(\bar F)\); then \(ng=u(y)\). Send it to \(y\bmod nY\). A different representative adds \(u(y')\) and changes \(y\) by \(ny'\), so the map is well-defined. A zero image can be represented by \(g-u(y')\in G[n]\). No nonzero period is torsion, so the kernel inclusion is injective. Divisibility of \(G(\bar F)\) gives a lift for every \(y\), proving surjectivity. At level \(4\) the orders in the example are
\[
 \#G[4]=4^2=16,\qquad
 \#Q[4]=4^4=256,\qquad
 \#(Y/4Y)=4^2=16.
 \tag{PMX3}
\]
Multiplying a representative at level \(\ell^{r+1}\) by \(\ell\) preserves its period coefficient modulo \(\ell^rY\); thus the last transitions are reductions. Recursively dividing each basis period gives compatible lifts at all levels. Their \(\mathbf Z_\ell\)-linear combinations prove inverse-limit surjectivity. Its quotient \(Y\otimes\mathbf Z_\ell\) is free, so the included submodule is saturated: a quotient element killed by a nonzero power of \(\ell\) must be zero.

**(d)** The full \(N\) has rank two, \(N^2=0\), and its integral kernel is the upper \(\mathbf Z_\ell^2\). Integer row and column operations give Smith entries \(1,6\): the entry one can be made the first pivot, leaving the determinant six as the second pivot. On a vector \((x,y)\), invariance under every \(1+tN\) is \(My=0\). Over \(\mathbf Z_\ell\) the matrix is injective, but modulo \(\ell^r\) its kernel has order \(\ell^{\min(v_\ell(6),r)}\). Consequently
\[
 \#(Q[\ell^r])^{I}
   =\ell^{\,2r+\min(v_\ell(6),r)}.
 \tag{PMX4}
\]
For \(\ell=2,3\) this is \(\ell^{2r+1}\), whereas reduction of the integral invariant module has order \(\ell^{2r}\). For \(\ell=7\) both orders are \(7^{2r}\). Thus reduction and invariants fail to commute at the first two primes. This is invariance under an infinite unipotent inertia action on finite torsion; it is not the characteristic-zero averaging operation on the finite inertia representation \(r\).

**(e)** On \(I_L\), the operator is \(1+t_LN_L\). At \(t_L=1\) the base-field formula must give
\[
 1+2N_F=1+N_L,\qquad N_F=\tfrac12N_L.
 \tag{PMX5}
\]
Choosing \(N_F=N_L\) instead gives \(1+2N_L\); choosing \(2N_L\) gives \(1+4N_L\). Both have the wrong Kummer coefficient in the fixed basis. After the stated further extension the integral map is \(3I_2\), while the total ramification index is six. Thus \(\nu=(3I_2)/6=\tfrac12I_2\), as before.

On each special block, geometric Frobenius has matrix \(\operatorname{diag}(q_F^{-1},1)\). Direct multiplication gives
\[
 r(\Phi)Nr(\Phi)^{-1}=q_F^{-1}N.
 \tag{PMX6}
\]
The finite permutation action commutes with the common scalar period matrix, so the same covariance holds in the quadratic example.

**(f)** The valuation map is
\[
 \nu=\begin{pmatrix}2&4\\1&2\end{pmatrix}.
 \tag{PMX7}
\]
A zero valuation relation has \(y_1\)-coefficient minus twice its \(y_2\)-coefficient. Its remaining first torus coordinate is \((1+p)^m\). This equals one only when \(m=0\): these are rational numbers in a characteristic-zero field, and a positive power of the integer \(1+p>1\) is not one. Thus the periods are independent.

The image is the line spanned by \((2,1)\), the kernel is spanned by \((-2,1)\), and both \(X_0\) and \(Y_0\) have dimension one. All these actions are trivial. The full module has dimension six, \(N\) has rank one, and \(\ker N\) has dimension five. The three centered graded dimensions are \(1,4,1\), with common block description
\[
 D_B\oplus\|\cdot\|\oplus1\oplus\mathrm{Sp}(2).
 \tag{PMX8}
\]
Injectivity of \(u\) has not made its valuation map invertible.

Moreover \(u(-2y_1+y_2)=(1+p,1)\), and its \(p^r\)-th powers tend to the identity. For a direct valuation proof, if \(v_p(h)\ge1\), the binomial expansion for odd \(p\) gives \(v_p((1+h)^p-1)=v_p(h)+1\): the term \(ph\) has that valuation, and every other term has strictly larger valuation. Induction gives \(v_p((1+p)^{p^r}-1)=r+1\). These are distinct nonidentity period points tending to one, so the subgroup is not discrete. No proper abelian quotient is claimed for these data.

**(g)** An isomorphism of pairs conjugates the nilpotent operators, and therefore preserves their rank. Here those ranks are one and zero, so the pairs are not isomorphic. Both underlying Weil characters are \(\|\cdot\|+1\). Their finite Weil conductor is zero. The formula of Lesson 7 adds the codimension of the nilpotent kernel, giving conductors one and zero, respectively. PM6 keeps the actual image and kernel of \(\nu\), and hence the linked special blocks, rather than only the underlying Weil character.

**(h)** With \(S=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), the projectors are
\[
 P_+=\tfrac12(I+S),\qquad P_-=\tfrac12(I-S).
 \tag{PMX9}
\]
Their images are \(\mathbf Q(1,1)\) and \(\mathbf Q(1,-1)\). The two integral eigenvectors form a matrix of determinant minus two. They generate the index-two sublattice of \(\mathbf Z_2^2\) consisting of pairs with equal parity. Hence rational averaging splits the representation even at coefficient prime two, but it is not an integral direct-sum splitting there.

In the tamely ramified quadratic case \(X=1\oplus\eta\), so \(a(X)=1\) and \(\dim X^I=1\). There is no abelian middle part. Formula (PM18) gives conductor three over \(F\). Over \(L\) the lattice action is unramified and the monodromy rank is two, so the conductor is two. Thus one must include both the finite inertia term and the monodromy correction before descending.

**(i)** Reversing and dividing by the nonzero constant term gives
\[
 P_{\mathrm{geom}}(T)=T^2-\frac bqT+\frac1q.
 \tag{PMX10}
\]
In general, for \(P_M(T)=\prod_{i=1}^s(T-\alpha_i)\), with every \(\alpha_i\ne0\),
\[
 \frac{T^sP_M(T^{-1})}{P_M(0)}
       =\prod_{i=1}^s(T-\alpha_i^{-1}).
 \tag{PMX11}
\]
This follows by factoring \(1-\alpha_iT\) and using \(P_M(0)=\prod_i(-\alpha_i)\); it includes the empty product. The matrix operator for the inverse Weil element is the actual inverse of \(M\). Its rational characteristic polynomial is therefore determined by that of \(M\), with no geometric construction of an inverse quasi-isogeny. Algebraic Frobenius is the positive arithmetic action; the positive geometric exponent used in Lesson 7 has the opposite sign.

**(j)** For a general abelian variety one must construct a finite-extension semiabelian period presentation with a good abelian quotient and torus, its lattice and equivariant period injection, and an identification of every actual prime-to-\(p\) torsion level and transition with (PM8). The geometric pairing and its nondegeneracy and the compatible finite model actions also require proofs. PM1–PM7 calculates the module for specified data; it does not supply those constructions for arbitrary varieties. PM8 supplies them for the actual product families and the indicated quadratic interchange using the already proved Tate uniformization and effective generic-field Galois descent.

Finally the tensor ring for an integral ramified cover need not decompose into the Galois translates. For a ramified quadratic extension with \(\pi^2=\pi_F\),
\[
 R\otimes_{\mathcal O_F}R
       \simeq R[z]/(z^2-\pi_F),\qquad
 z\longmapsto(\pi,-\pi)
 \tag{PMX12}
\]
maps to \(R\times R\). In the bases \(1,z\) its determinant is \(-2\pi\), not a unit. Thus it is not the product isomorphism available over the fraction fields. A semilinear group action specifies maps on those translates; faithfully flat integral descent needs its equality on the full tensor overlap. GQ5 already proves this distinction, including the nilpotent overlap, and the matrix above displays it again.

### 2F. Proper period quotients, nondegeneracy and actual torsion

A list of periods in a semiabelian group need not uniformize a proper variety: Exercise 2E(f) gives independent periods accumulating at the identity. We now prove exactly what properness and a local covering map supply. In particular, the rank and nondegeneracy of the valuation lattice will be conclusions. We do not assume a perfect integral pairing or infer an integral descent datum from a ramified group action.

#### 2F.0. Integer lattices and Smith reduction

**PC0.** Every subgroup of \(\mathbf Z^n\) is finitely generated and free of rank at most \(n\). For an arbitrary integer matrix \(A\) of size \(m\) by \(n\), there are invertible integer matrices \(U,V\), of determinant \(\pm1\), such that
\[
 UAV=\operatorname{diag}(d_1,\ldots,d_r,0),\qquad
 d_i>0,\quad d_i\mid d_{i+1}.
 \tag{PC0.1}
\]
Here \(r\) is the rational rank; the diagonal is rectangular if necessary. Its cokernel and its full-rank square index are
\[
 \operatorname{coker} A\simeq
   \bigoplus_{i=1}^r\mathbf Z/d_i\mathbf Z\ \oplus\mathbf Z^{m-r},
 \qquad
 [\mathbf Z^n:A\mathbf Z^n]=|\det A|
       \quad(m=n=r).
 \tag{PC0.2}
\]
For \(1\le k\le r\), let \(\Delta_k(A)\) be the positive greatest common divisor of its \(k\)-rowed minors, and put \(\Delta_0=1\). Then
\[
 \Delta_k(A)=d_1\cdots d_k,\qquad
 d_k=\Delta_k(A)/\Delta_{k-1}(A).
 \tag{PC0.3}
\]
Thus the positive divisibility-ordered diagonal is unique. All assertions include the zero matrix and rank zero.

*Proof.* First, every nonzero ideal in \(\mathbf Z\) has a least positive member \(d\). For any \(a\) in that ideal, division with remainder gives \(a=qd+r\), \(0\le r<d\). The remainder is in the ideal, so is zero by minimality. The ideal is therefore \(d\mathbf Z\). The division itself follows by choosing the integer \(q\) with \(q\le a/d<q+1\); equivalently subtract consecutive multiples until reaching that interval. The zero ideal is principal as well.

Let \(N\subset\mathbf Z^n\), without any finite-generation assumption on \(N\). Project it onto the first coordinate. If the image is zero, induct in the remaining \(n-1\) coordinates. Otherwise the image is \(d\mathbf Z\); choose \(z\in N\) with first coordinate \(d\). Subtracting the appropriate integer multiple of \(z\) from an arbitrary member gives a unique decomposition
\[
 N=\mathbf Zz\oplus
       \bigl(N\cap(0\times\mathbf Z^{n-1})\bigr).
 \tag{PC0.4}
\]
The intersection is free on at most \(n-1\) generators by induction. This proves the first assertion, including finite generation and rank. A quotient of a finitely generated abelian group is finitely generated by the images of any generating set; no separate finiteness theorem is being invoked.

For the matrix reduction, the allowed operations are row or column interchange, multiplication of one row or column by minus one, and addition of an integer multiple of another row or column. Every operation has an inverse of the same kind and determinant \(\pm1\). Their products therefore give the required invertible \(U,V\).

If the matrix is nonzero, move a nonzero entry to the top left and change its sign to make the pivot \(d>0\). For an entry \(a\) in its first column, write \(a=qd+r\), \(0\le r<d\), and subtract \(q\) times the first row from that row. If \(r>0\), interchange these two rows: the new positive pivot is strictly smaller. Restart the process with this pivot. If \(r=0\), the operation clears that entry. Apply the same division process to the first row, using column operations. Any nonzero remainder again becomes a strictly smaller positive pivot after a column interchange, and the process restarts. Because a positive integer cannot decrease indefinitely, eventually these operations clear the whole first row and column outside the pivot, giving
\[
 \begin{pmatrix}d&0\\0&B\end{pmatrix}.
 \tag{PC0.5}
\]
At each fixed pivot, clearing the first column takes finitely many operations; subsequent exact first-row divisions preserve that cleared column. A restart occurs only after a strict decrease, so the assertion is a finite algorithm, not just an appeal to a minimal entry of the original matrix.

If an entry of \(B\) is not divisible by \(d\), add its row to the first row. The first pivot remains \(d\), but the first row now has an entry not divisible by it. Divide that entry by the pivot by a column operation and move its nonzero remainder to the pivot position. This again strictly decreases the positive pivot; restart the clearing procedure. There can only be finitely many such decreases. We therefore arrive at (PC0.5) with every entry of \(B\) divisible by \(d\).

Induct on the smaller matrix \(B\). All row and column operations performed inside it preserve divisibility of every entry by \(d\), so its first positive diagonal entry is a multiple of \(d\). The induction gives divisibility of each subsequent entry by its predecessor. If \(B\) is zero, stop; if one dimension is zero, no further entry remains. These steps prove (PC0.1) in every rectangular size. Since invertible row and column operations preserve rational rank, the number of nonzero diagonal entries is exactly \(r\).

Left multiplication changes the target basis and right multiplication the source basis, so the cokernel is the diagonal cokernel in (PC0.2). A nonzero diagonal entry has exactly \(d_i\) residue classes, by integer division. A zero target row leaves a free copy of \(\mathbf Z\). In the full-rank square case the quotient order is \(\prod_i d_i\), while the determinants of \(U,V\) have absolute value one; hence this order is \(|\det A|\). A finite-index subgroup of \(\mathbf Z^n\) has rank \(n\): multiply each coordinate basis vector by the order of the finite quotient to put it in the subgroup, which therefore spans \(\mathbf Q^n\).

Finally the ideal generated by the \(k\)-rowed minors is unchanged by the allowed operations. For a row addition, determinant multilinearity writes each new minor as an old minor plus an integer multiple of another old minor; if both relevant rows already occur, the extra term has repeated rows and is zero. Row permutations and signs only permute minors up to sign. Column operations have the same property. Applying the inverse operation proves equality of the two ideals, not merely one inclusion.

On the divisibility-ordered diagonal, every nonzero \(k\)-minor is the product of \(k\) selected diagonal entries. If their ordered indices are \(i_1<\cdots<i_k\), then \(i_j\ge j\), so \(d_j\mid d_{i_j}\). Hence every such minor is divisible by \(d_1\cdots d_k\), and the first \(k\) entries give a minor equal to that product. This proves the first formula in (PC0.3); division proves the second and uniqueness. The rank-zero assertions have empty products and a zero map, as stated. \(\square\)

**Worked example.** The diagonal matrix with entries \(6,10,15\) is not in divisibility-ordered Smith form. Its entry gcd is one, its nonzero two-rowed minors are \(60,90,150\) with gcd \(30\), and its determinant is \(900\). Thus
\[
 \operatorname{diag}(6,10,15)
   \ \sim\ \operatorname{diag}(1,30,30),\qquad
 \operatorname{coker} A\simeq(\mathbf Z/30\mathbf Z)^2.
 \tag{PC0.6}
\]
This quotient has order \(900\) and exponent \(30\). In particular a nonzero determinant proves finite index, whereas a perfect integral pairing requires determinant of absolute value one. PC0 supplies the integer module and matrix arguments used in PC3, PC4 and PC7; the discrete-valuation-ring arguments of Lesson 1 are used only in their stated scope.

For freely accessible background see [*Smith normal form over the integers*, university lecture notes](https://www3.nd.edu/~sevens/smithform.pdf). The subgroup, terminating matrix reduction, minors and cokernel arguments needed here are proved in PC0.

#### 2F.1. The topology of algebraic points

**PC1.** Let \(K\) be a complete discretely valued field with finite residue field, \(R_K\) its valuation ring, and \(\mathscr Z/R_K\) a separated scheme of finite type. Its integral points are a compact open subset of \(\mathscr Z_K(K)\). If \(A/K\) is an abelian variety, then \(A(K)\) is compact and Hausdorff.

*Proof.* Give an affine finite-type \(K\)-scheme its point topology by a presentation as polynomial equations in \(K^N\). This is independent of the presentation: every additional coordinate is a polynomial in the first coordinates. On a principal open, regular coordinates are quotients with nonzero denominators, and those are continuous. Consequently affine charts glue to a topology, regular maps are continuous, and open immersions induce open inclusions. The point topology on a product is the product topology, as follows on pairs of affine charts. For a separated scheme the diagonal is a closed immersion, hence is closed in the point topology. If two points differ, their ordered pair has an open product neighbourhood outside this diagonal; its two factors are disjoint. Thus this topology is Hausdorff.

The ring \(R_K\) is the inverse limit of the finite discrete rings \(R_K/\pi^nR_K\). Injectivity is the separated valuation, and surjectivity is completeness, by choosing compatible representatives. The finite-product compactness argument of Lesson 1, §0C proves compactness of this inverse limit. The ring and all its cosets are open in \(K\): the ball \(\pi^nR_K\) around zero is an open ball after replacing its radius by the next larger value. Polynomial equations define closed subsets of finite powers of this compact ring.

Choose a finite affine cover \(\mathscr U_i=\operatorname{Spec}R_K[z_1,\ldots,z_{N_i}]/I_i\) of \(\mathscr Z\). Every integral point factors through one of these opens: choose an open containing its special point; its inverse image in \(\operatorname{Spec}R_K\) contains the closed point and therefore the whole spectrum. The points of \(\mathscr U_i(R_K)\) form a closed subset of \(R_K^{N_i}\), so are compact. They form an open subset of \(\mathscr U_{i,K}(K)\), because all coordinate integrality conditions are open. Their images cover \(\mathscr Z(R_K)\), which is therefore compact and open. Distinct integral points have distinct generic points: their equality locus is closed by separatedness and contains the dense generic point of \(\operatorname{Spec}R_K\).

For the last assertion CU7 gives a projective embedding of \(A\) over this very field \(K\). Projective space is the continuous image of the compact set
\[
 S_N=\{(z_0,\ldots,z_N)\in R_K^{N+1}:\max_i|z_i|=1\}
       \longrightarrow\mathbf P^N(K),\qquad z\longmapsto[z].
 \tag{PC1}
\]
The set is closed, since its complement inside \(R_K^{N+1}\) is \((\pi R_K)^{N+1}\), a closed and open set. Every projective point can be scaled into it, by choosing a coordinate of largest absolute value. Continuity follows on each chart from the coordinate ratios. The closed embedding makes \(A(K)\) a closed subset of this compact space, so it is compact. Hausdorffness was proved above. No assertion about a relative projective embedding of an integral model was needed. \(\square\)

#### 2F.2. The covering properties and descent of a point

Retain the supplied semiabelian scheme of §2E over \(R=\mathcal O_L\), but for the moment let \(Y\) be any torsion-free abelian group, with an injection \(u:Y\to G(L)\). We specify the additional geometric input to be used. Let \(A/L\) be an abelian variety. A **local-field period presentation** here consists of group homomorphisms
\[
 j_E:G(E)\longrightarrow A(E)\quad(E/L\text{ finite}),
 \qquad \ker j_E=u(Y),
 \tag{PC2}
\]
compatible with embeddings over \(L\), including automorphisms, and with the following properties:

* every \(a\in A(E)\) has a lift in \(G(E')\) after some finite extension \(E'/E\);
* \(j_E\) is continuous, and on a neighbourhood of the identity it is a homeomorphism onto an open neighbourhood of the identity in \(A(E)\).

These are point-lifting and local-covering requirements, not torsion comparison, a period-rank assumption or a pairing assumption. In applying this definition to an analytic uniformization, its geometric construction must establish these requirements. We are not asserting their existence for every \(A\).

**PC2.** Such a presentation is surjective on \(E\)-points for every finite \(E/L\). It induces a topological group isomorphism
\[
 G(E)/u(Y)\ \xrightarrow{\ \sim\ } A(E).
 \tag{PC3}
\]
Its kernel is closed and discrete in \(G(E)\).

*Proof.* Choose a lift \(g\in G(E')\) of \(a\in A(E)\), and enlarge \(E'\) to a finite Galois extension of \(E\). This is possible by the finite Galois theory of Lesson 1. For \(\sigma\in\operatorname{Gal}(E'/E)\), compatibility gives a unique \(c_\sigma\in Y\) with
\[
 \sigma g-g=u(c_\sigma),\qquad
 c_{\sigma\tau}=c_\sigma+c_\tau.
 \tag{PC4}
\]
The second identity uses that all \(u(y)\) are already \(L\)-rational, so this finite group acts trivially on them. Its image in the torsion-free group \(Y\) is zero: an element of order \(m\) maps to an element killed by \(m\). Thus \(g\) is fixed by this Galois group and is an \(E\)-point. This last descent is the finite faithfully flat point descent proved in FD1–FD5, or its coordinate equalizer on affine charts. It proves surjectivity without a completed algebraic closure or a theorem about its fixed field.

The kernel is closed because \(j_E\) is continuous and the identity of the Hausdorff group \(A(E)\) is closed. Its intersection with an identity neighbourhood on which \(j_E\) is injective is just zero; translations make it discrete. The local homeomorphism condition also makes \(j_E\) open everywhere. Indeed, for an open neighbourhood \(V\) of \(g\), intersect \(V-g\) with that fixed identity neighbourhood. Its image is open, contains zero and lies in \(j_E(V)-j_E(g)\). The images of these neighbourhoods cover \(j_E(V)\). A continuous open surjection induces exactly the quotient topology, proving (PC3). \(\square\)

#### 2F.3. The full lattice criterion

**PC3.** Let \(G_0\) be a Hausdorff abelian topological group, \(H\) a compact open subgroup, and \(G_0/H=X\simeq\mathbf Z^t\). Let \(Y\) be a torsion-free subgroup of \(G_0\), and write \(\lambda:Y\to X\) for the quotient map. Then the following conditions are equivalent:

1. \(Y\) is closed and discrete, and \(G_0/Y\) is compact;
2. \(\lambda\) is injective and has finite cokernel.

Either condition makes \(Y\) free of rank \(t\). There is an exact sequence of topological groups
\[
 0\longrightarrow H\longrightarrow G_0/Y
       \longrightarrow C:=X/\lambda(Y)\longrightarrow0,
 \tag{PC5}
\]
with \(C\) finite and discrete, and the first map identifies \(H\) with a compact open subgroup.

*Proof.* Under the first condition \(Y\cap H\) is closed in compact \(H\), hence compact, and is discrete. The cover of this subspace by its singletons has a finite subcover, so it is finite. As a subgroup of torsion-free \(Y\) it is zero. This proves injectivity of \(\lambda\). The map \(G_0\to X/\lambda(Y)\) is continuous for the discrete topology: each fibre is a union of cosets of the open subgroup \(H\). It factors continuously and surjectively through compact \(G_0/Y\). A compact discrete space is finite, proving the cokernel assertion.

Conversely assume the second condition. Each open coset of \(H\) contains at most one point of \(Y\). In that coset, remove this point if it occurs. The resulting set is open, since the group is Hausdorff. Taking these sets over all cosets shows that the complement of \(Y\) is open; thus \(Y\) is closed. An identity neighbourhood inside \(H\) meets \(Y\) only at zero, so \(Y\) is discrete. Choose lifts \(g_1,\ldots,g_m\) in \(G_0\) of representatives of \(X/\lambda(Y)\). Every coset modulo \(Y\) has a representative in some \(g_i+H\). Their finite union is compact and maps onto \(G_0/Y\), which is therefore compact.

For clarity, this quotient is Hausdorff. If \(z\notin Y\), closedness gives an identity neighbourhood \(W\) such that \((z+W)\cap Y\) is empty. By continuity of subtraction choose an identity neighbourhood \(V\) with \(V-V\subset W\). The images in the quotient of the two corresponding translates of \(V\) are disjoint: an intersection would put \(z+(V-V)\) in \(Y\). The quotient map is open since the saturation of an open set is the union of its translates by \(Y\). These disjoint images separate any two different quotient points.

The kernel in (PC5) is precisely the image of \(H\), and its injection is continuous. A continuous bijection from compact \(H\) to its image in this Hausdorff quotient is a homeomorphism: a closed subset of \(H\) is compact, and its image is compact and hence closed. The image is open because the quotient map is open. Finally a subgroup of \(\mathbf Z^t\) is finitely generated and free by PC0. A finite-index subgroup spans \(\mathbf Q^t\): multiply each of the \(t\) basis classes by the order of the finite quotient. Its rank is therefore \(t\). \(\square\)

Apply this to \(G_0=G(L)\) and \(H=\mathcal G(R)\). PC1 makes \(H\) compact open, and PM2 identifies its quotient with the cocharacter lattice \(X\). PC2 and compactness of \(A(L)\) give the first condition. We have proved, without assuming the rank of \(Y\),
\[
 Y\simeq\mathbf Z^t,\qquad
 \nu_L:Y\hookrightarrow X,\qquad [X:\nu_LY]<\infty.
 \tag{PC6}
\]
The finite group in (PC5) is the **period valuation quotient** of this presentation. Identifying it with the component group of a specified Néron model requires a comparison with that model; no such identification is part of PC3.

#### 2F.4. The integral pairing and its finite discriminant

**PC4.** Put \(M=X^*=\operatorname{Hom}(X,\mathbf Z)\), the character lattice of the split torus. The pairing
\[
 b_L:Y\times M\longrightarrow\mathbf Z,\qquad
 b_L(y,m)=m(\nu_L(y))
 \tag{PC7}
\]
is nondegenerate on both arguments and perfect after tensoring with \(\mathbf Q\). If \(C=X/\nu_LY\), it gives an exact sequence and a perfect finite pairing
\[
 \begin{gathered}
 0\longrightarrow M\xrightarrow{\nu_L^*}Y^*
       \longrightarrow\operatorname{Hom}(C,\mathbf Q/\mathbf Z)
       \longrightarrow0,\\
 (Y^*/\nu_L^*M)\times C\longrightarrow\mathbf Q/\mathbf Z,
 \qquad (h,\bar x)\longmapsto\widetilde h(x)\bmod\mathbf Z.
 \end{gathered}
 \tag{PC8}
\]
Here \(\widetilde h\) is the unique rational functional on \(X_{\mathbf Q}\) with \(\widetilde h\circ\nu_L=h\). Integral perfection is not asserted.

*Proof.* The rational map \(\nu_L\) is an isomorphism by PC3. A nonzero \(y\) therefore has nonzero image, which some coordinate functional detects. If \(m\) pairs to zero with every \(y\), it vanishes on their rational span \(X_{\mathbf Q}\), so is zero. This proves nondegeneracy and rational perfection.

The functional in (PC8) exists uniquely by this same rational isomorphism. Adding \(\nu_L(y)\) to \(x\) changes its value by the integer \(h(y)\), so the pairing is well-defined. Its kernel on \(Y^*\) consists exactly of those rational extensions integral on all of \(X\), namely \(M\). To prove surjectivity and perfection, use PC0's integer Smith reduction to choose bases with
\[
 \nu_L=\operatorname{diag}(d_1,\ldots,d_t),\qquad
 d_i>0,\quad d_i\mid d_{i+1}.
 \tag{PC9}
\]
Then \(C=\bigoplus_i\mathbf Z/d_i\mathbf Z\). The class of the \(i\)-th dual basis vector of \(Y^*\) pairs with the \(i\)-th class of \(X\) to \(1/d_i\) modulo \(\mathbf Z\), and with the other classes to zero. A homomorphism from \(\mathbf Z/d_i\mathbf Z\) to \(\mathbf Q/\mathbf Z\) is uniquely a multiple of this character: its value on one lies in \(\frac1{d_i}\mathbf Z/\mathbf Z\). Thus these classes generate the full dual and separate every nonzero class in either factor. This proves (PC8), including rank zero.

If the finite group \(\Gamma=\operatorname{Gal}(L/F)\) acts on the presentation as in §2E, PM2 gives \(\nu_L(\gamma y)=\gamma\nu_L(y)\). With the contragredient action on \(M\), this says
\[
 b_L(\gamma y,\gamma m)=b_L(y,m),\qquad
 b_F:=\frac1{e(L/F)}b_L.
 \tag{PC10}
\]
The finite pairing is equivariant for the same reason: rational extension of a functional is unique. Under a further extension \(E/L\) of ramification index \(e'\), PM2 gives \(\nu_E=e'\nu_L\). Thus \(b_E=e'b_L\), while \(b_F\) is unchanged. In particular
\[
 \begin{gathered}
 C_E\simeq\bigoplus_i\mathbf Z/(e'd_i)\mathbf Z,\qquad
 |C_E|=(e')^t|C|,\\
 |C|=\prod_i d_i=|\det\nu_L|.
 \end{gathered}
 \tag{PC11}
\]
The normalized pairing may be rational rather than integral; this also occurs when a coefficient prime divides \(e(L/F)\). These are assertions about the period valuation pairing. Symmetry or positivity from a polarization, or identification with a separately defined pairing on a dual model, requires that additional geometric construction. \(\square\)

#### 2F.5. Every actual torsion level follows from the cover

**PC5.** For a local-field period presentation, the maps \(j_E\) identify the abstract period quotient with the actual algebraic point group:
\[
 G(\bar L)/u(Y)\xrightarrow{\ \sim\ }A(\bar L).
 \tag{PC12}
\]
Consequently every finite torsion level, its multiplication transitions and its Galois action are the ones computed in PM1–PM4. In particular
\[
 \begin{gathered}
 0\longrightarrow G[\ell^r]\longrightarrow A[\ell^r]
          \longrightarrow Y/\ell^rY\longrightarrow0,\\
 0\longrightarrow T_\ell G\longrightarrow T_\ell A
          \longrightarrow Y\otimes\mathbf Z_\ell\longrightarrow0,
 \qquad\dim A=a+t.
 \end{gathered}
 \tag{PC13}
\]
The first sequence is a sequence of geometric point groups, for \(\ell\ne p\). The Tate submodule is saturated.

*Proof.* Every algebraic point belongs to a finite extension, since its finitely many coordinates on an affine chart are algebraic. PC2 is surjective over each such field, with kernel exactly \(u(Y)\), and the maps are compatible on these fields. Their union is therefore (PC12). This map is a group isomorphism, not merely a bijection between torsion cardinalities. It is equivariant for every automorphism over \(L\) by the defining compatibility. If \(A\) is defined over \(F\) and the presentation has compatible semilinear \(\Gamma\)-actions, require \(j(\sigma g)=\sigma j(g)\) also for those actions. The same argument then makes (PC12) equivariant for \(G_F\).

Taking kernels of multiplication by \(\ell^r\) in this actual isomorphism gives the first sequence from PM3, with its explicit last map: a lift \(g\) of \(x\) has \(\ell^rg=u(y)\), and one takes \(y\bmod\ell^rY\). Multiplication by \(\ell\) on successive lifts preserves this \(y\) modulo the smaller power. Thus every transition commutes, and the compatible-division argument of PM3 proves the second sequence. Its free quotient makes the submodule saturated: an element of the quotient killed by a nonzero power of \(\ell\) must be zero. All actions are continuous by the finite-level argument of PM3. The ranks from PM3 are \(2a+t,t\); CU9 gives rank \(2\dim A\) for the actual abelian Tate module. Hence \(2\dim A=2a+2t\), proving the dimension assertion without inferring analytic dimension from a mere homeomorphism. \(\square\)

#### 2F.6. Rational and finite-level inertia invariants

**PC6.** For this genuine presentation, the valuation is invertible over \(\mathbf Q\). Its full Frobenius-semisimple Weil–Deligne class, finite conductor and centered nilpotent filtration are therefore
\[
 \begin{gathered}
 D_A=D_B\oplus(X_{\mathbf Q}\otimes\mathrm{Sp}(2)),\\
 a_F(A)=a(D_B)+2a(X_{\mathbf Q})+\dim X_{\mathbf Q}^{I_F},
 \qquad a_L(A)=t,\\
 \operatorname{im}N=X_{\mathbf Q_\ell}(1),\qquad
 \ker N=V_\ell G.
 \end{gathered}
 \tag{PC14}
\]
At the integral and finite levels over \(L\), let \(s_i=v_\ell(d_i)\) for (PC9). Then
\[
 \begin{gathered}
 (T_\ell A)^{I_L}=T_\ell G,\\
 \#(A[\ell^r]^{I_L})=
   \ell^{\,r(2a+t)+\sum_{i=1}^t\min(s_i,r)},\\
 \#\bigl((T_\ell A)^{I_L}/\ell^r\bigr)=\ell^{\,r(2a+t)}.
 \end{gathered}
 \tag{PC15}
\]
Here (PC14) presupposes the compatible finite model actions of PM5 when descending to \(F\); over \(L\) the lattice and good part are unramified.

*Proof.* PC3 gives the rational invertibility required in PM6–PM7, and PC5 identifies those computed modules with the actual Tate module. Their proved formulas give (PC14). This uses the full inertia matrix, rather than just a Weil character.

To compute the other assertions, choose the integral module splittings of PM3: lift a basis of \(T_\ell B\) to \(T_\ell G\), and compatible period divisions to \(T_\ell A\). The three coordinates have ranks \(t,2a,t\). PM4 gives the entire \(I_L\)-action by adding \(t_{\ell,L}(\sigma)\nu_Ly\) to the first coordinate and leaving the other two fixed. The character \(t_{\ell,L}:I_L\to\mathbf Z_\ell\) is surjective by Lesson 7's full radical-tower proof. Invariance is consequently exactly \(\nu_Ly=0\). On the integral lattice this forces \(y=0\), since its determinant is nonzero and the lattice is torsion-free. This proves the first equality.

Modulo \(\ell^r\), invariance is instead \(\nu_Ly=0\bmod\ell^r\). The Smith basis changes are integral and invertible over \(\mathbf Z_\ell\). The kernel of multiplication by \(d_i\) on \(\mathbf Z/\ell^r\mathbf Z\) has order \(\ell^{\min(s_i,r)}\): write \(d_i=\ell^{s_i}v_i\) with \(v_i\) a unit, and count the multiples of \(\ell^{\max(r-s_i,0)}\). The free first two coordinates give \(\ell^{r(2a+t)}\) choices. This proves the second and third formulas. Hence invariants and reduction commute here exactly when no \(d_i\) is divisible by \(\ell\). This calculation concerns the full infinite unipotent inertia action on finite torsion; it is not the exact-invariants averaging argument for a finite group over characteristic zero. \(\square\)

#### 2F.7. What changes before the period lattice is split

**PC7.** Suppose the presentation over \(L\) has compatible semilinear actions over the finite Galois extension \(L/F\). Write \(\Gamma=\operatorname{Gal}(L/F)\). There is an exact sequence
\[
 \begin{gathered}
 0\longrightarrow Y^\Gamma\longrightarrow G(L)^\Gamma
    \longrightarrow A(F)\xrightarrow{\delta}H^1(\Gamma,Y),\\
 \delta(a)=[c],\qquad u(c_\sigma)=\sigma g-g
       \quad\text{for a lift }g\in G(L).
 \end{gathered}
 \tag{PC16}
\]
The group on the right is finite and killed by \(|\Gamma|\). No surjectivity of \(G(L)^\Gamma\to A(F)\) is asserted.

*Proof.* Surjectivity over \(L\) gives a lift \(g\) of \(a\). Equivariance and the kernel calculation give unique \(c_\sigma\) with

\[
 c_{\sigma\tau}=c_\sigma+\sigma c_\tau.
 \tag{PC17}
\]
Changing the lift by \(u(y)\) adds the coboundary \(\sigma y-y\). Thus the class is well-defined, and it vanishes precisely when a lift can be changed to a \(\Gamma\)-fixed one. This proves exactness at \(A(F)\); the kernel and left-hand exactness follow directly from injectivity of \(u\). Fixed \(L\)-points of the \(F\)-variety \(A\) are exactly \(A(F)\), by finite faithfully flat descent. The generic \(\Gamma\)-fixed group \(G(L)^\Gamma\) has the same interpretation if the generic semiabelian group has been descended. Neither statement descends an integral model along a ramified extension.

By PC3 the group \(Y\) is finitely generated free. The cocycles form a subgroup of \(Y^{|\Gamma|}\), so are finitely generated by PC0's subgroup argument. Their quotient by coboundaries is also finitely generated. Put \(S=\sum_{\sigma\in\Gamma}c_\sigma\). Summing (PC17), with its first argument \(\tau\) fixed, gives
\[
 |\Gamma|c_\tau=S-\tau S.
 \tag{PC18}
\]
This is the coboundary of \(-S\), so every cohomology class is killed by \(|\Gamma|\). A finitely generated group killed by a positive integer is finite: its finite generating set exhibits it as a quotient of a finite power of \(\mathbf Z/|\Gamma|\mathbf Z\). This proves the assertion. For example, on the sign lattice \(\mathbf Z\) of a group of order two, every integer is the value of a cocycle on the nonidentity element, while coboundaries are the even integers. Thus \(H^1=\mathbf Z/2\mathbf Z\); the trivial-action argument of PC2 cannot be applied before splitting the lattice. \(\square\)

#### 2F.8. Functoriality of the valuation pairing

**PC8.** Consider two such presentations over the same splitting field \(L\). Suppose a homomorphism of their supplied integral extensions respects the torus and abelian factors and is compatible with maps on periods and on the actual abelian varieties. Let \(f_X:X\to X'\) and \(f_Y:Y\to Y'\) be the resulting maps. Then
\[
 \nu'_Lf_Y=f_X\nu_L,\qquad
 b'_L(f_Yy,m')=b_L(y,f_X^*m').
 \tag{PC19}
\]
These identities induce compatible maps on every torsion level, its transition, its inertia matrix and its rational Weil–Deligne pair. If the map on actual abelian varieties is an isogeny, their torus ranks are equal, both lattice maps are rational isomorphisms, and
\[
 |\det f_X|\,|\det\nu_L|
       =|\det\nu'_L|\,|\det f_Y|.
 \tag{PC20}
\]

*Proof.* The integral homomorphism takes integral sections to integral sections. In the quotient of PM2 it sends the valuation of a torus coordinate by its integer cocharacter map \(f_X\): the monomial-coordinate proof is part of PM2. Apply it to \(u(y)\), whose image is \(u'(f_Yy)\), to obtain the first identity. Evaluating a character gives the second. Multiplication by every integer commutes with all these homomorphisms. The explicit maps in (PC13) therefore commute, including their multiplication transitions. PM4 then identifies their actual inertia matrices and the Weil–Deligne equivalence preserves these maps.

For an isogeny, CU10 gives an isomorphism on rational Tate modules. Equivariance makes it commute with \(N\): choose inertia elements in the common splitting field with a nonzero tame-character value in PM4 and cancel this scalar. It therefore induces isomorphisms on the images and kernels of \(N\). By (PC14) the images have dimensions \(t\) and \(t'\), giving \(t=t'\). On those images the induced map is \(f_X\otimes\mathbf Q_\ell(1)\), so \(f_X\) is a rational isomorphism. The first identity of (PC19), with both valuations invertible over \(\mathbf Q\), then makes \(f_Y\) a rational isomorphism. Taking determinants and absolute values in that integer identity proves (PC20). This asserts functoriality for a supplied map of presentations; construction of such a lift for an arbitrary homomorphism remains part of the geometric uniformization theory. \(\square\)

The geometric uniformization problem is still to construct these extensions, periods and locally covering maps for every abelian variety after finite extension, with the compatible finite model actions. Once that construction establishes (PC2), its lifting and local-covering properties, PC2–PC6 prove the full-rank period pairing and actual torsion comparison; these conclusions need no separate citation to an unproved nondegeneracy statement. The free article [*Uniformisation des variétés abéliennes*, Fresnel and van der Put, §6.2](https://www.numdam.org/item/AFST_1989_5_S10__7_0.pdf) describes the geometric setting. Its general existence theorem is not used in place of the missing local construction. The compactness, finite descent, lattice, discriminant and torsion arguments used here have all been proved above.

#### 2F.9. Graded exercise: properness and the period lattice

This exercise is worth **100 points**, with **10 points for each part**. All local fields below have finite residue field. A period valuation quotient is the group defined in PC3; do not identify it with a Néron component group without a model comparison.

**(a) Integral topology.** Explain why \(\mathbf A^1(R)\) is compact open in \(\mathbf A^1(L)\), while \(L\) is not compact. The separated finite-type \(R\)-scheme \(\operatorname{Spec}R[z]/(\pi z-1)\) has an \(L\)-point but no \(R\)-point. Explain why this agrees with PC1. Give the finite affine-cover argument that proves compactness for an arbitrary separated finite-type integral model, rather than only affine space.

**(b) Descent of one lift.** Let \(E'/E\) be cyclic Galois of degree three, with a lift \(g\in G(E')\) of \(a\in A(E)\), and let the periods be a constant torsion-free group \(Y\). If \(\sigma g-g=u(y)\), compute \(\sigma^3g-g\) and prove that \(g\) is \(E\)-rational. Specify which hypotheses would fail in trying to apply this argument to a nonsplit sign lattice.

**(c) An actual nondiagonal period lattice.** Work over \(L=\mathbf Q_7\), put \(\pi=7\), and take torus periods
\[
 u(y_1)=(\pi^2,1),\qquad u(y_2)=(\pi,\pi^3).
 \tag{PCX1}
\]
Compute \(\nu_L\) and find integer matrices \(U,V\) of determinant \(\pm1\) with \(U\nu_LV=\operatorname{diag}(1,6)\). Give the associated torus coordinate change and the new period basis. Use the proved Tate uniformization of Lesson 7 to identify this quotient with an actual product of two Tate curves. Determine the period valuation quotient and the conductor over \(L\).

**(d) Ramified base change.** For the presentation in (c), pass to a finite extension \(E/L\) of ramification index two. Compute the new Smith entries, period valuation quotient, its order and the normalized valuation map relative to \(L\). Explain why its conductor over \(E\) need not equal the order of this finite quotient.

**(e) Actual finite inertia invariants.** For (c), compute the orders of \(A[\ell^3]^{I_L}\) and of the reduction of \((T_\ell A)^{I_L}\) for \(\ell=2,3,5\). For the extension in (d), compute the orders of \(A[2^r]^{I_E}\) for \(r=1,2,3\). Describe the integral invariant submodule and explain the failure of invariants to commute with reduction.

**(f) A period subgroup inside a compact group.** For \(p\) odd, prove that the injective map \(\mathbf Z\to1+p\mathbf Z_p\) sending \(n\) to \((1+p)^n\) does not have discrete image. Why can it not be the kernel of a local-field period presentation with a proper abelian quotient? Explain separately why closedness matters in the compact-intersection argument of PC3, and why torsion-freeness matters.

**(g) The finite descent obstruction.** Let \(\Gamma=\{1,s\}\) act on \(Y=\mathbf Z\) by \(sy=-y\). Compute every \(1\)-cocycle, every coboundary and \(H^1(\Gamma,Y)\). Verify the averaging identity (PC18). Explain what the connecting map in (PC16) proves, and why it does not prove that every class in \(H^1(\Gamma,Y)\) occurs.

**(h) Discriminant duality and rational normalization.** For the matrix in (c), show that the class of \(e_2\) generates \(C=X/\nu_LY\simeq\mathbf Z/6\mathbf Z\). Find a generator of \(Y^*/\nu_L^*M\) pairing to \(1/6\) with it, by writing out its rational extension to \(X_{\mathbf Q}\). If this same integral data is viewed over a base with ramification index two, exhibit an entry of the normalized pairing which is not an integer. Distinguish nondegeneracy, rational perfection and integral perfection.

**(i) A map of presentations.** Suppose a compatible isogeny of two toric presentations has the following maps in their chosen bases:
\[
 \nu_L=\begin{pmatrix}2&0\\0&3\end{pmatrix},\quad
 \nu'_L=\begin{pmatrix}1&0\\0&6\end{pmatrix},\quad
 f_X=\begin{pmatrix}3&0\\0&2\end{pmatrix},\quad
 f_Y=\begin{pmatrix}6&0\\0&1\end{pmatrix}.
 \tag{PCX2}
\]
Check the commuting square, the pairing adjunction and (PC20). Compute the determinant valuation on the full Tate module at every coefficient prime. Determine the degree directly from the geometric kernel: prove the exact kernel sequence using surjectivity of the torus map, rather than infer a possible residue-characteristic factor from the coefficient primes alone.

**(j) Geometric scope.** State the geometric constructions that remain necessary to apply Theorem 2.4 to an arbitrary abelian variety. Which rank, nondegeneracy and torsion assertions follow from PC1–PC6 once the local-field period presentation is constructed? Which assertions about a polarized dual model, arbitrary lifted homomorphisms, and ramified integral descent have not been supplied by this point-topological argument?

**Complete solution.**

**(a)** The ring \(R\) is the inverse limit of its finite residue rings, hence compact; it is an open ball in \(L\). The increasing open cover \(L=\bigcup_{n\ge0}\pi^{-n}R\) has no finite subcover, because the valuation on \(L^\times\) is unbounded below. Thus \(L\) is not compact. The displayed model requires \(z=\pi^{-1}\), which is not integral, so its set of integral points is empty, a compact open set. PC1 does not identify all generic points with integral points.

On each of a finite number of affine model charts, integral points are a closed subset of a finite power of \(R\), and are therefore compact. Every integral point lies in a chart containing its special point; the preimage of this open chart contains all of \(\operatorname{Spec}R\). Their finite union is the full integral point set. Coordinate integrality is open on each generic affine chart. Separatedness gives the injection into generic points and Hausdorffness, as proved in PC1.

**(b)** Constancy makes \(\sigma u(y)=u(y)\), so adding the three differences gives
\[
 \sigma^3g-g=3u(y)=u(3y)=0.
 \tag{PCX3}
\]
Injectivity of \(u\) and torsion-freeness give \(y=0\), hence \(g\) is fixed and descends by finite field descent. More generally \(c_\sigma=\sigma g-g\), expressed in period coordinates, is a homomorphism from this finite Galois group to \(Y\), so is zero. For the sign lattice the action on \(Y\) is nontrivial. Differences obey the twisted cocycle identity; they need not form a homomorphism to a trivial module. Over the splitting field the action is trivial, which is exactly where PC2 applies.

**(c)** The columns are the coordinate valuations:
\[
 M=\nu_L=\begin{pmatrix}2&1\\0&3\end{pmatrix},\quad
 U=\begin{pmatrix}1&0\\3&-1\end{pmatrix},\quad
 V=\begin{pmatrix}0&1\\1&-2\end{pmatrix},\quad
 UMV=\begin{pmatrix}1&0\\0&6\end{pmatrix}.
 \tag{PCX4}
\]
Both basis changes have determinant minus one. The torus automorphism is
\[
 (x_1,x_2)\longmapsto(x_1,x_1^3/x_2).
 \tag{PCX5}
\]
The columns of \(V\) replace the basis by \(y'_1=y_2\) and \(y'_2=y_1-2y_2\). Their original torus values are \((\pi,\pi^3)\) and \((1,\pi^{-6})\); (PCX5) sends them to \((\pi,1)\) and \((1,\pi^6)\). Thus the actual product \(E_\pi\times E_{\pi^6}\) supplies the presentation, using Lesson 7's proved Galois-equivariant Tate uniformization. The quotient is \(\mathbf Z/6\mathbf Z\). Its torus rank is two and its good abelian part has dimension zero, so its conductor over \(L\) is two by PC6.

**(d)** Valuations are multiplied by two. The same \(U,V\) give Smith entries \(2,12\), so
\[
 C_E\simeq\mathbf Z/2\mathbf Z\oplus\mathbf Z/12\mathbf Z,
 \qquad |C_E|=24,\qquad
 \frac{\nu_E}{e(E/L)}=M.
 \tag{PCX6}
\]
The conductor over \(E\) is still two: the toric monodromy has rank two and the finite Weil part is unramified there. The finite quotient instead measures the index of the integral period valuation lattice, which changed under ramification. These are different measurements, with the stated values derived separately.

**(e)** Here \(a=0,t=2\) and the Smith entries are \(1,6\). The integral inertia invariants are \(T_\ell\mathbf G_m^2=\mathbf Z_\ell(1)^2\), of rank two and saturated in the rank-four full Tate module. Formula (PC15) gives
\[
 \begin{array}{c|r|r}
 \ell &\#A[\ell^3]^{I_L}&
    \#\bigl((T_\ell A)^{I_L}/\ell^3\bigr)\\ \hline
 2&128&64\\
 3&2187&729\\
 5&15625&15625
 \end{array}.
 \tag{PCX7}
\]
After the ramified extension the two \(2\)-adic Smith valuations are \(1,2\). For \(r=1,2,3\) the invariant exponents are \(2r+\min(1,r)+\min(2,r)\), giving
\[
 \#A[2]^{I_E}=16,\qquad
 \#A[4]^{I_E}=128,\qquad
 \#A[8]^{I_E}=512.
 \tag{PCX8}
\]
On the integral lattice the valuation matrix is injective, so the period coordinate of an invariant vector is zero. Modulo \(\ell^r\) the matrix can have a nonzero kernel; its extra period coordinates are precisely the additional finite invariants. Thus this is not an application of exact averaging over finite inertia in characteristic zero.

**(f)** An integer power of the rational number \(1+p>1\) is one only for exponent zero, so the map is injective. If \(v_p(h)\ge1\), the binomial expansion for odd \(p\) gives
\[
 v_p((1+h)^p-1)=v_p(h)+1:
 \tag{PCX9}
\]
the term \(ph\) has that valuation, every middle term has strictly larger valuation since its binomial coefficient is divisible by \(p\), and the last term \(h^p\) has larger valuation because \(p\ge3\). Induction starting with \(h=p\) gives \(v_p((1+p)^{p^r}-1)=r+1\). Thus distinct period points approach the identity, contradicting discreteness of the kernel of a local homeomorphism.

The intersection of a discrete subgroup with a compact subgroup is finite only if that intersection is closed: compactness passes to closed subsets, not arbitrary subsets. For example the infinite subset \(\{1/n:n\ge1\}\) of the compact real interval \([0,1]\) is discrete in its subspace topology and is not closed. This elementary topological example illustrates the missing condition; the local-field period proof obtains closedness from the continuous map to a Hausdorff quotient. Torsion-freeness is separately needed to turn a finite intersection into zero. In the finite discrete group \(G_0=H=Y=\mathbf Z/2\mathbf Z\), the subgroup is closed and discrete and the quotient is compact, but \(Y\to G_0/H=0\) is not injective.

**(g)** A cocycle has \(c_1=0\) and arbitrary value \(c_s=n\), because \(c_{s^2}=n+sn=n-n=0\). A coboundary has value \(sy-y=-2y\). Hence
\[
 H^1(\Gamma,Y)=\mathbf Z/2\mathbf Z,\qquad
 S=n,\qquad 2c_s=S-sS=2n.
 \tag{PCX10}
\]
The last cochain is the coboundary of \(-S\), as in PC7. For an actual point \(a\in A(F)\), its boundary vanishes exactly when a lift in \(G(L)\) can be made \(\Gamma\)-fixed. Exactness makes the image of \(G(L)^\Gamma\) the kernel of the boundary. It supplies no assertion that the boundary is onto; further obstructions can prevent a cocycle from being represented by an actual point of \(A(F)\).

**(h)** The columns of \(M\) give relations \(2e_1=0\), \(e_1+3e_2=0\). Therefore \(e_1=-3e_2\) and \(6e_2=0\). The quotient has order six by its determinant, so \(e_2\) has order six. Take \(h=-y_1^*\). Its extension to \(X_{\mathbf Q}\) is
\[
 \widetilde h=(-1,0)M^{-1}
       =(-\tfrac12,\tfrac16),\qquad
 \widetilde h(e_2)=\tfrac16.
 \tag{PCX11}
\]
This gives a character of exact order six and hence a generator of the dual discriminant. The entry \(b_L(y_2,e_1^*)=1\) becomes \(b_F(y_2,e_1^*)=1/2\) when the normalization divides by two. The integral pairing is nondegenerate and has determinant six, so it is perfect over \(\mathbf Q\), while its integral cokernel has order six. Integral perfection would require determinant a unit in \(\mathbf Z\), namely absolute value one. The normalized rational matrix is not an integral matrix at coefficient prime two in this basis.

**(i)** Both products in the square are \(\operatorname{diag}(6,6)\). For a column \(y\) and character column \(m'\), the adjunction is the equality
\[
 (m')^{\mathsf t}\nu'_Lf_Yy
    =(m')^{\mathsf t}f_X\nu_Ly
    =(f_X^{\mathsf t}m')^{\mathsf t}\nu_Ly.
 \tag{PCX12}
\]
All four determinant absolute values are six, so (PC20) reads \(36=36\). In toric and period coordinates the Tate map is block upper triangular with diagonal maps \(f_X\) and \(f_Y\). Its determinant therefore has valuation \(2v_\ell(6)\) at every coefficient prime: two for \(\ell=2,3\), zero otherwise.

For the actual degree use the given compatible isogeny and its surjective torus lift \(\varphi(x_1,x_2)=(x_1^3,x_2^2)\). Lifting a point of its geometric kernel to the source torus, its image is a target period. The period class is well-defined modulo \(f_Y(Y)\). Every target period has a torus lift over the algebraically closed field, by taking a cube root and a square root. A zero period class can be corrected by a source period to lie in \(\ker\varphi\). Since the target period map is injective and \(f_Y\) is injective, a source period in \(\ker\varphi\) is zero. This proves
\[
 0\longrightarrow\mu_3\times\mu_2
   \longrightarrow\ker f_A(\bar L)
   \longrightarrow Y'/f_YY\longrightarrow0.
 \tag{PCX13}
\]
The orders are six and six, so the kernel has order \(36\). By CU10 its degree is its geometric kernel cardinality in characteristic zero: the geometric generic fibre is a translate of the kernel, and the generic field extension is separable. Its degree is therefore \(36\). In particular no power of the residue characteristic is left undetermined by this direct count. The problem assumes the compatible algebraic isogeny; the matrix check alone does not construct one.

**(j)** One must still construct, after finite extension, a semiabelian integral extension with a good abelian quotient and split torus, its period injection and maps to the actual abelian variety. The maps must be natural on finite extensions, satisfy the finite point-lifting requirement, have the stated local covering property and kernel, and be compatible with the finite model actions needed for descent. PC1–PC3 then prove that the periods are free of exactly the torus rank and that their valuation is injective with finite cokernel. PC4 proves nondegeneracy and rational perfection of the period valuation pairing. PC2 and PC5 identify the quotient with the actual algebraic point group and every torsion level, transition and action. PC6 supplies the actual block, conductor and invariants.

This does not construct a polarized dual-model pairing or identify its integral form, lift every abelian homomorphism to a map of presentations, or turn a ramified semilinear group action into faithfully flat integral descent. Those geometric assertions require their own constructions. In particular the existence of the presentation for arbitrary abelian varieties remains an obligation of the full theorem.

#### 2F.10. Graded exercise: integer relations and finite descent

This exercise is worth **20 points**, with **10 points for each part**. Use the full integer statement PC0.

**(a)** Compute the kernel rank, cokernel and rational rank of
\[
 A=\begin{pmatrix}6&0&0&0\\0&10&0&0\\0&0&15&0\end{pmatrix}:
       \mathbf Z^4\longrightarrow\mathbf Z^3.
 \tag{PCZ1}
\]
Over \(\mathbf Q_7\), consider the four torus periods
\[
 (7^6,1,1),\quad(1,7^{10},1),\quad(1,1,7^{15}),\quad(8,1,1).
 \tag{PCZ2}
\]
Prove that they are independent as an abstract integer period map. Explain why the finite cokernel of their valuation map does not make them a proper period presentation.

**(b)** Let a group of order three act on \(Y=\mathbf Z^2\) by
\[
 S=\begin{pmatrix}0&-1\\1&-1\end{pmatrix}.
 \tag{PCZ3}
\]
Compute its integral \(1\)-cocycles modulo coboundaries using PC0. Give a generator of \(H^1\), a formula detecting its class, and the averaging identity for that generator. Explain why the resulting finite obstruction group does not assert surjectivity of the connecting map from actual rational points.

**Complete solution.**

**(a)** Its rational rank is three and its integer kernel is the free group on the fourth coordinate vector. The nonzero minors have the same gcds as \(\operatorname{diag}(6,10,15)\). PC0 therefore gives
\[
 \operatorname{coker}A\simeq(\mathbf Z/30\mathbf Z)^2,
 \qquad \#\operatorname{coker}A=900,\qquad
 \operatorname{rank}\ker A=1.
 \tag{PCZ4}
\]
An integer relation among the four periods has zero valuation in each coordinate. Its first three coefficients are consequently zero. The remaining relation is \(8^n=1\), which for integer \(n\) in characteristic zero forces \(n=0\): the positive rational number \(8\) has no nonzero power equal to one. The period map is therefore injective.

Its valuation map nevertheless kills the fourth generator. That generator lies in the compact integral torus and has infinite order. The lattice criterion PC3 forbids this for the kernel of a proper local period quotient. More concretely \(8^{7^r}\) tends to one, since the binomial proof of Exercise 2F(f) gives \(v_7(8^{7^r}-1)=r+1\). Thus the period subgroup is not discrete. Finite index of the valuation image is only one of the two necessary conditions.

**(b)** Direct multiplication gives \(S^3=I\) and \(I+S+S^2=0\). A cyclic-group cocycle is determined by its value \(x\) on the generator; its values on the other elements must be zero at the identity and \(x+Sx\) at the square. The final cocycle condition is \((I+S+S^2)x=0\), so every \(x\in\mathbf Z^2\) is allowed. Its coboundaries form \((S-I)\mathbf Z^2\), where
\[
 S-I=\begin{pmatrix}-1&-1\\1&-2\end{pmatrix},
 \qquad d_1=1,\quad d_2=3.
 \tag{PCZ5}
\]
Indeed the entries have gcd one and the determinant is three, so PC0 gives those Smith entries. The homomorphism \((a,b)\mapsto a+b\bmod3\) vanishes on both columns and is onto. Its kernel has index three, which equals the index of the column subgroup; hence the two kernels agree. Consequently
\[
 H^1(\langle S\rangle,Y)\simeq\mathbf Z/3\mathbf Z,
 \qquad [x]\longmapsto x_1+x_2\bmod3.
 \tag{PCZ6}
\]
A generator is the cocycle with values \(c_1=0\), \(c_S=(1,0)\), \(c_{S^2}=(1,1)\). Their sum is \(T=(2,1)\), and
\[
 3c_S=(3,0)=T-ST,\qquad ST=(-1,1).
 \tag{PCZ7}
\]
This is the coboundary of \(-T\), as in PC7. The group measures possible descent obstructions. Exactness says that an actual point has zero obstruction precisely when it has a fixed lift. It does not say that every cocycle class arises from such a point; that would require additional geometric information.

### 2G. Integral multiplication and finite subgroup kernels

The period-cover construction must accommodate isogenies whose degree is divisible by the residue characteristic. Finite étale torsion alone does not provide their integral kernels. We prove the finite flat statements, including the special fibres as schemes.

Let \(R\) be a discrete valuation ring with fraction field \(K\) of characteristic zero and residue field \(k\). Suppose that an integral semiabelian extension is given:
\[
 0\longrightarrow\mathcal T\longrightarrow\mathcal G
       \longrightarrow\mathcal B\longrightarrow0,\qquad
 \mathcal T=\mathbf G_{m,R}^{\,t},\qquad
 \dim(\mathcal B/R)=a.
 \tag{FF1}
\]
Here \(\mathcal B\) is an abelian scheme, \(\mathcal G\) is smooth, separated and of finite type, and \(\mathcal G\to\mathcal B\) is a torsor under the displayed split torus. No restriction on a positive multiplication integer will be imposed.

#### 2G.1. Rank, openness and the descent needed below

**FF1.** The following three elementary facts will be used.

First, let \(D\) be a Noetherian domain and \(M\) a finite \(D\)-module of generic dimension \(r\). If \(\dim_{\kappa(x)}(M\otimes\kappa(x))=r\), then \(M_x\) is free of rank \(r\). Indeed lift a basis of this fibre to \(M_x\). Nakayama gives a surjection \(D_x^r\to M_x\). Its kernel becomes zero over the fraction field, since source and target have the same generic dimension. A submodule of the torsion-free module \(D_x^r\) cannot be nonzero and vanish in that field. The surjection is therefore an isomorphism. The argument does not apply to a nonreduced base in place of \(D\).

Second, a finite locally free morphism of positive rank is surjective and universally open. Work on an affine base where its algebra \(C/D\) is free of rank \(r>0\). For \(c\in C\), write the characteristic polynomial of multiplication by \(c\) as
\[
 P_c(T)=T^r+b_1T^{r-1}+\cdots+b_r.
 \qquad
 \operatorname{image}(D(c)\subset\operatorname{Spec}C)
       =\bigcup_{i=1}^rD(b_i)\subset\operatorname{Spec}D.
 \tag{FF2}
\]
To prove this, a fibre meets \(D(c)\) exactly when \(c\) is not nilpotent in its finite-dimensional fibre algebra. Multiplication by a nilpotent element is a nilpotent operator and has characteristic polynomial \(T^r\): a basis adapted to its kernel filtration makes it triangular with zero diagonal. Conversely that polynomial makes the operator nilpotent by Cayley–Hamilton, and applying it to the identity makes \(c\) nilpotent. The adjugate proof of Cayley–Hamilton works over any commutative ring: compare coefficients in \((TI-A)\operatorname{adj}(TI-A)=\det(TI-A)I\), express the adjugate coefficients recursively as polynomials in \(A\), and substitute \(T=A\). Thus the condition is precisely the nonvanishing of some \(b_i\), proving (FF2). Principal opens form a basis. The proof survives every base change. Surjectivity follows since each fibre algebra has positive dimension and hence a prime ideal. Flatness and surjectivity make this a faithfully flat cover.

Third, affine faithfully flat universally open covers suffice to descend finite locally free morphisms, without assuming the cover finite. Here are the scheme details. The module, algebra and finite-local-freeness descent FD1–FD4 apply to every faithfully flat ring map; none of their proofs assumes finiteness of that map. For descent of an invariant morphism, the inverse image of an affine target open is a saturated open of the covering scheme. Saturation follows by taking a common point in the fibre product of any two points above the same base point: their residue-field tensor product is nonzero and has a prime. The image of this saturated open is open because the cover is open, and its inverse image is the original open. On affine opens of that image, coordinates descend by the equalizer FD1. The resulting maps agree on overlaps, with equality detected by the same equalizer. This proves morphism descent for these covers and their base changes.

Now if \(X\to S\) becomes finite locally free after such a cover, work with \(S\) affine. Its covered affine algebra descends by FD2–FD4 to a finite locally free algebra \(C\) on \(S\). The two inverse isomorphisms with \(\operatorname{Spec}C\) descend by the preceding morphism argument; their composites are identities after a faithful cover and hence before it. Thus the original morphism is finite locally free with the same rank. We will use covers built only from finite locally free maps and finite unions of affine open immersions, which are affine over an affine target and universally open. \(\square\)

#### 2G.2. Every multiplication integer on an abelian scheme

**FF2.** For every \(n\ge1\), multiplication on \(\mathcal B\) is finite locally free and surjective, of rank \(n^{2a}\). Its kernel is finite locally free of that rank over \(R\).

*Proof.* The map is proper: its graph is closed in the fibre product because the target is separated over \(R\), and projection of this graph is proper because \(\mathcal B/R\) is proper. For every target geometric point, the map on the corresponding geometric abelian fibre is multiplication by \(n\). CU8 proves in all characteristics that this map is finite, flat and surjective of degree \(n^{2a}\). A preimage of the chosen point exists, and its translation identifies the full scheme-theoretic fibre with the zero fibre. Consequently every geometric fibre of our proper map is finite and has length \(n^{2a}\), including when \(n\) is divisible by \(\operatorname{char}k\). The proper finite-fibre theorem of Lesson 3, §0.F.1 makes the integral map finite.

The target \(\mathcal B\) is integral. To check this directly, its generic fibre is geometrically integral. On every nonempty affine open of \(\mathcal B\), flatness over \(R\) embeds its coordinate ring into its localization over \(K\). This localization is nonzero, since multiplication by a uniformizer is injective, and it is the ring of a nonempty open of the integral generic fibre. It is a domain. The affine ring is therefore a domain, and the generic fibre is dense in every such open; these opens show that the whole scheme is integral.

On a target affine open, the finite source algebra is a finite module of generic rank \(n^{2a}\). At each target point its fibre has that same dimension, by the geometric-fibre computation and faithful scalar extension to an algebraic closure of the residue field. The first assertion of FF1 makes this module free at that point. It is therefore locally free everywhere, of the asserted rank. Positive rank gives surjectivity, or it follows directly from the fibres. Pulling back along the identity section proves the kernel assertion. No relative ample line or omitted miracle-flatness theorem was used. \(\square\)

#### 2G.3. Finite flat multiplication on the semiabelian extension

**FF3.** In (FF1), for every \(n\ge1\) there is an exact sequence of fppf sheaves represented by finite locally free group schemes
\[
 0\longrightarrow\mathcal T[n]\longrightarrow\mathcal G[n]
       \longrightarrow\mathcal B[n]\longrightarrow0.
 \tag{FF3}
\]
Their ranks over \(R\) are \(n^t,n^{2a+t},n^{2a}\), respectively. Multiplication by \(n\) on \(\mathcal G\) itself is finite locally free, surjective and of rank \(n^{2a+t}\).

*Proof.* The torus kernel has coordinate algebra
\[
 R[z_1^{\pm1},\ldots,z_t^{\pm1}]/(z_1^n-1,\ldots,z_t^n-1),
 \tag{FF4}
\]
free on monomials whose exponents lie between zero and \(n-1\). Division by each monic polynomial gives spanning and uniqueness; negative exponents can be removed using \(z_i^n=1\). Thus this calculation retains the full kernel even in residue characteristic dividing \(n\).

A section of \(\mathcal B[n]\) lifts locally for the faithfully flat topology to \(\mathcal G\), by the torsor in (FF1). Its \(n\)-multiple lies in the torus, and adjoining \(n\)-th roots of its inverse coordinates corrects the lift into \(\mathcal G[n]\). Each root algebra is finite free of positive rank, so provides a faithfully flat cover by FF1. Two corrected lifts differ by \(\mathcal T[n]\), which proves exactness and the torsor assertion over \(\mathcal B[n]\).

There is an explicit finite flat local description. The frame-torsor argument in PM1, proved using FD1–FD4, identifies a torsor under a split torus with the product of frame torsors of invertible modules; hence it has sections on a Zariski open cover of its base. On an affine open of \(\mathcal B[n]\), choose a lift \(g\) and write the torus coordinates of \(ng\) as units \(c_i\). Corrected lifts then have algebra
\[
 A[z_1^{\pm1},\ldots,z_t^{\pm1}]
       /(z_1^n-c_1^{-1},\ldots,z_t^n-c_t^{-1}).
 \tag{FF5}
\]
It is free of rank \(n^t\) on the same monomial basis; here \(z_i^{-1}=c_i z_i^{n-1}\). These are target-local descriptions, so the map to \(\mathcal B[n]\) is finite locally free. FF2 gives the total rank \(n^{2a+t}\) over \(R\). The Jacobian is not being inverted when \(n\) is not a unit.

To prove the assertion about multiplication on all of \(\mathcal G\), take an affine target open \(S\). Pull back the finite locally free cover \([n]:\mathcal B\to\mathcal B\) along the image of its universal point; this gives an affine finite locally free cover \(S_1\to S\) on which its image in \(\mathcal B\) has a division. On a finite affine open cover of \(S_1\), lift that division to the torus torsor, and correct its torus error by the finite free root covers (FF5). The resulting finite disjoint union is affine and faithfully flat over \(S\), and universally open by FF1 and openness of open immersions. It supplies an actual division in \(\mathcal G\).

After this cover, multiplication becomes the projection of the trivial torsor under \(\mathcal G[n]\): a chosen division identifies a fibre by adding a kernel point. Thus it is finite locally free of the stated rank after the cover. The descent proof in FF1 proves that property before the cover. It also proves surjectivity. \(\square\)

#### 2G.4. Transitions and the integral finite-part division tower

**FF4.** For positive \(m,n\), the multiplication transition is finite locally free and gives an fppf exact sequence
\[
 0\longrightarrow\mathcal G[n]\longrightarrow\mathcal G[mn]
       \xrightarrow{[n]}\mathcal G[m]\longrightarrow0.
 \tag{FF6}
\]
If \(m,n\) are coprime and \(an+bm=1\), the maps
\[
 \mathcal G[mn]\xrightarrow{\ \sim\ }\mathcal G[m]\times\mathcal G[n],
 \quad x\longmapsto(nx,mx),\qquad
 (u,v)\longmapsto au+bv
 \tag{FF7}
\]
are mutually inverse over \(R\), as group schemes, not just on geometric points.

*Proof.* For a section \(y\) killed by \(m\), FF3 gives locally a section \(x\) with \(nx=y\). Then \(mnx=0\), so this is a lift in \(\mathcal G[mn]\). The kernel is exactly \(\mathcal G[n]\), and translation makes the transition a torsor under that finite locally free group. The same descent argument as in FF3 proves finite local freeness of rank \(n^{2a+t}\) over \(\mathcal G[m]\), even though that target can have nilpotents. The identities in (FF7) follow from \(an+bm=1\) and \(mu=nv=0\), on every test scheme. Yoneda therefore gives the scheme isomorphism.

If the residue characteristic is \(p>0\), these kernels and transitions construct a \(p\)-divisible group of height \(2a+t\):
\[
 \operatorname{rank}_R\mathcal G[p^r]=p^{r(2a+t)},\qquad
 0\longrightarrow\mathcal G[p]\longrightarrow\mathcal G[p^{r+1}]
       \xrightarrow{[p]}\mathcal G[p^r]\longrightarrow0.
 \tag{FF8}
\]
Here the term means precisely this compatible system of finite locally free groups, with the inclusions as successive multiplication kernels and the exact transitions just proved. The toric and abelian heights are \(t\) and \(2a\), by (FF3). If \(n\) is a unit of \(R\), the square-zero tangent correction of GQ3, applied to the smooth group \(\mathcal G\), proves that multiplication by \(n\) is étale: its tangent correction is multiplication by the invertible scalar \(n\). If the special fibre has positive dimension and \(p\mid n\), that scalar is zero on its nonzero Lie algebra; the tangent space of its kernel at the identity is therefore nonzero, so the finite kernel is not étale.

This constructs the integral finite part attached to the supplied semiabelian extension. For a degenerating proper abelian variety, its additional period directions have not been made into an integral finite flat model by this calculation. No residue-characteristic comparison theorem or general period cover is asserted. \(\square\)

#### 2G.5. Why every finite group in characteristic zero is étale

**FF5.** A finite group scheme over a characteristic-zero field is finite étale. In particular every finite subgroup of \(G_K\) is killed by its rank as a finite scheme.

*Proof.* We first prove an algebraic fact. In a finite-dimensional Hopf algebra over a characteristic-zero field, a primitive element must be zero. A primitive element \(D\) satisfies \(\Delta(D)=D\otimes1+1\otimes D\). Its powers satisfy a monic relation of least degree \(q\), since the algebra is finite-dimensional. If \(q=1\), then \(D\) is a scalar, and the primitive equality forces that scalar to be zero. If \(q>1\), the elements \(1,D,\ldots,D^{q-1}\) are independent. Apply the algebra homomorphism \(\Delta\) to the relation. In the tensor product of this basis with itself, the coefficient of \(D^{q-1}\otimes D\) is \(q\ne0\): it comes from the binomial expansion of \((D\otimes1+1\otimes D)^q\). Lower-degree terms cannot contribute, and reduction of the two outer terms \(D^q\otimes1\), \(1\otimes D^q\) cannot contribute to this mixed tensor. This is a contradiction. The proof does not require the Hopf algebra to be commutative.

Now extend the finite group to an algebraic closure, and let \(A\) be its finite coordinate Hopf algebra, with augmentation ideal \(I\). A nonzero functional on \(I/I^2\) defines a nonzero functional \(D\) on \(A\) by applying it to \(a-\epsilon(a)\). It satisfies
\[
 D(ab)=D(a)\epsilon(b)+\epsilon(a)D(b).
 \tag{FF9}
\]
The finite-dimensional dual \(A^*=\operatorname{Hom}(A,k)\) is a Hopf algebra: its product is dual to the comultiplication of \(A\), and its comultiplication is dual to multiplication of \(A\). The unit is \(\epsilon\). Thus (FF9) says exactly that \(D\) is primitive in \(A^*\), which is impossible. Consequently \(I/I^2=0\).

For the finite-algebra decomposition used here, there are only finitely many maximal ideals: any collection of distinct ones gives a surjection onto their residue-field product by the Chinese remainder equations, so their number is bounded by the algebra's vector-space dimension. Powers of their intersection eventually stabilize by that same dimension bound; Nakayama makes that stabilized power zero, since the intersection is the Jacobson radical. The pairwise comaximal powers and the Chinese remainder equations therefore decompose the algebra into local Artinian factors.

At the identity, the maximal ideal in its local Artinian coordinate algebra equals its square. Nakayama makes that ideal zero, so this component is the residue field. Every component has an algebraic point over the algebraically closed field, and translation by that point identifies it with the identity component. Hence every component is reduced and is a single field point. The coordinate algebra is a product of copies of the field, proving geometric étaleness. The original algebra is reduced because it injects into this scalar extension. Its same local Artinian decomposition is consequently a product of finite field extensions; those fields are separable in characteristic zero. Thus the original group is finite étale as well.

For a finite subgroup of the commutative \(G_K\), its geometric point group has cardinality equal to its scheme rank \(N\). Every element is killed by \(N\): its cyclic subgroup partitions that finite group into equal-size cosets, so its order divides \(N\). On the finite étale scheme, equality of morphisms is detected on geometric points. Thus \([N]\) is the zero map on this subgroup, and it is contained in \(G_K[N]\). This rank-annihilation conclusion has been proved here in characteristic zero; no corresponding blanket claim in positive characteristic is being imported. \(\square\)

#### 2G.6. Saturated finite flat closure in the integral group

**FF6.** Every finite subgroup \(H_K\subset G_K\) has a canonical finite locally free schematic closure \(\mathcal H\subset\mathcal G\), of the same rank. It commutes with extension of discrete valuation rings. It is independent of the positive integer used to contain it in a multiplication kernel. Actual maps of integral semiabelian extensions carry such closures functorially to one another.

*Proof.* By FF5 choose \(N\) with \(H_K\subset G_K[N]\). The finite locally free group \(\mathcal G[N]\) is affine over \(R\); write its finite free Hopf algebra as \(A\), and let \(J_K\subset A_K\) define \(H_K\). Set
\[
 J=A\cap J_K\subset A_K,\qquad C=A/J.
 \tag{FF10}
\]
The quotient embeds in \(A_K/J_K\), so is torsion-free over \(R\). It is finite over \(R\), and therefore free by the DVR module proof of Lesson 1, §0A: put its finitely many generators in a lattice of its generic vector space by clearing denominators and apply the submodule induction. Its rank is \(\dim_K(A_K/J_K)\).

The Hopf maps descend. For example, the image of \(\Delta(J)\) in \(C\otimes_R C\) becomes zero over \(K\). This tensor product is free over \(R\), so the image was already zero. The counit and antipode have the same property, with targets \(R\) and \(C\). Thus \(C\) is a Hopf quotient, and \(\mathcal H=\operatorname{Spec}C\) is a finite locally free closed subgroup.

It is the schematic closure: a function on this affine multiplication kernel vanishes on the generic subgroup exactly when it lies in \(A\cap J_K\). It is also the unique finite flat closed model there with that generic fibre. Indeed if \(A/J'\) is flat and \(J'_K=J_K\), then \(J'\) is saturated: an element whose nonzero scalar multiple lies in \(J'\) already lies there. Clearing a denominator in the equality of generic ideals consequently gives \(J'=A\cap J_K\).

For an extension \(R\to R'\) of discrete valuation rings with fraction extension \(K\to K'\), the quotient \(C\otimes_R R'\) remains free and has generic fibre \(H_K\otimes_K K'\). Inside \(\mathcal G[N]_{R'}\), uniqueness identifies it with the closure computed over \(R'\). If two annihilating integers are used, embed both kernels in the kernel for a common multiple. Both closures there are finite flat with the same generic fibre, so uniqueness identifies them. The resulting closed subgroup of \(\mathcal G\) is independent of that integer.

Finally let an actual integral group map carry \(H_K\) into \(H'_K\). Pull back the defining ideal of \(\mathcal H'\) to \(\mathcal H\). Every such function is zero generically, and is zero already because the coordinate functions of the finite flat \(\mathcal H\) are torsion-free over \(R\). The restriction therefore factors through \(\mathcal H'\). Composition and equality are preserved, giving functoriality. This assumes the integral ambient map; it does not construct such a lift for an arbitrary generic morphism. \(\square\)

#### 2G.7. Generic equality does not identify integral models

**FF7.** Let \(p\) be prime, \(K=\mathbf Q_p(\zeta_p)\), \(R=\mathcal O_K\), and \(\pi=\zeta_p-1\). The generic groups \(\mu_{p,K}\) and \((\mathbf Z/p\mathbf Z)_K\) are isomorphic, but their finite flat \(R\)-models are not. The natural evaluation map on coordinate algebras has determinant valuation
\[
 R[z]/(z^p-1)\longrightarrow R^p,\qquad
 f\longmapsto\bigl(f(1),f(\zeta_p),\ldots,f(\zeta_p^{p-1})\bigr),
 \qquad
 v_\pi(\det)=\frac{p(p-1)}2.
 \tag{FF11}
\]

*Proof.* The polynomial \(\Phi_p(1+X)=((1+X)^p-1)/X\) is monic, all its nonleading coefficients are divisible by \(p\), and its constant is \(p\), not divisible by \(p^2\). It is irreducible over \(\mathbf Q_p\): monic factors would have integral coefficients, since their roots are integral and \(\mathbf Z_p\) is integrally closed. Modulo \(p\) both nonconstant factors would be powers of \(X\), so both constants would be divisible by \(p\), a contradiction. This is the Eisenstein argument, including the degree-one case \(p=2\).

Thus \([K:\mathbf Q_p]=p-1\). The root \(\zeta_p\) is a unit and reduces to one, since over the residue field its \(p\)-th power is one and \(X^p-1=(X-1)^p\). The polynomial equation for \(\pi\) gives \(\pi^{p-1}\) equal to \(p\) times a unit. The valuation-extension result of Lesson 1, §0E then gives \(e(K/\mathbf Q_p)=p-1\) and \(v_K(\pi)=1\): the ramification index is at least \(p-1\), at most the degree, and the displayed equation forces equality. This also proves that the residue field is \(\mathbf F_p\).

In the monomial basis the evaluation matrix is \((\zeta_p^{ij})_{0\le i,j<p}\). Subtracting columns successively, or regarding its determinant as an alternating polynomial in the \(p\) distinct roots, gives the Vandermonde product of their pairwise differences. Each difference is \(\zeta_p^i\pi(1+\cdots+\zeta_p^{j-i-1})\), whose last factor reduces to the nonzero residue \(j-i\). Each difference therefore has valuation one. There are \(p(p-1)/2\) differences, proving (FF11). In particular this generic algebra isomorphism is not an integral isomorphism. Its cokernel has that length: over a DVR an entry of smallest valuation divides every entry of a finite matrix; clear its row and column, continue inductively, and sum the valuations of the nonzero diagonal entries. Each quotient \(R/\pi^bR\) has length \(b\) by its successive residue-field quotients. The sum is the determinant valuation.

The special fibre of \(\mu_p\) is
\[
 k[z]/(z^p-1)\simeq k[u]/u^p,
 \tag{FF12}
\]
of length \(p\) and with one geometric point. The constant group's special fibre is the reduced disjoint union of \(p\) points. The evaluation morphism sends all these points to the identity, so cannot be an isomorphism. The closure in the fixed ambient \(\mathbf G_{m,R}\) of the generic subgroup is \(\mu_p\), by FF6. The constant model illustrates the failure of uniqueness of an abstract integral model without that fixed closed embedding. \(\square\)

#### 2G.8. Prime-to-residue morphisms and finite actions

**FF8.** If \(R\) is complete and \(H,H'\) are finite étale \(R\)-schemes, every \(K\)-morphism \(H_K\to H'_K\) extends uniquely over \(R\). For group schemes the extension is a group homomorphism when its generic restriction is. Compatible finite semilinear actions on such generic groups extend, with their identities and cocycles.

*Proof.* Choose a finite Galois separable extension \(k'/k\) splitting the finite étale special fibres. Choose a primitive element of this extension and lift its monic minimal polynomial to \(f\in R[T]\). The primitive-element proof of Lesson 1, §0E applies when the base field is infinite; for a finite field its multiplicative-group construction in §0F supplies a generator. Put \(R'=R[T]/f\). It is finite free and complete over \(R\), with special fibre \(k'\). Every maximal ideal lies over the maximal ideal of \(R\), by the integral-extension argument of §0E, so it is local. Its maximal ideal is generated by a uniformizer of \(R\); division by that uniformizer terminates on any nonzero element because the finite free module is separated. Every remaining factor is a unit, by the geometric-series unit lift. This makes \(R'\) a complete discrete valuation ring, and the invertible derivative of \(f\) modulo the maximal ideal makes it finite étale. Its fraction field is a finite unramified extension of \(K\). This construction works for arbitrary residue fields.

After this base change the finite étale special algebras of \(H,H'\) are products of \(k'\). Their idempotents lift by Hensel's lemma, as in GQ4. Each factor has rank one and its unit is a basis, by Nakayama and finite freeness; thus each factor is \(R'\). Both schemes have therefore split into finite disjoint unions of copies of \(\operatorname{Spec}R'\). A map of their generic schemes is a function between these finite component sets and extends by that same function. It is unique, since the two functions must agree generically.

For a map originally over \(K\), the two pullbacks of this extension to \(R'\otimes_R R'\) agree: that tensor product is finite étale and hence flat over \(R\), and their component functions agree on the generic fibre. Equivalently, coordinate equality is detected by injection of the finite free coordinate algebra into its generic algebra. FD5 descends the map through the finite faithfully flat cover \(R'/R\). Uniqueness descends with it. All homomorphism diagrams can be checked generically, because the finite étale sources and their products have torsion-free coordinate algebras. Thus they hold integrally.

A ring automorphism of \(R\) can be handled by viewing a semilinear map as an ordinary map to the corresponding twist. The twist is still finite étale. Extend each generic map as above; uniqueness makes all action and cocycle identities hold. In particular FF6 applied to a subgroup killed by an integer invertible in \(R\) produces a finite étale closure. Here is a direct verification over the complete ring, without an additional descent theorem. The special algebra of the finite étale \(\mathcal G[n]\) is a product of finite separable residue fields. Lift its idempotents by Hensel's lemma in the complete finite free ambient algebra. Each factor is local with maximal ideal generated by the base uniformizer, and is separated and torsion-free over \(R\). The division-by-uniformizer argument used above makes each such factor a DVR. A quotient by an ideal of one factor is torsion-free over \(R\) only when that ideal is zero or the unit ideal. The finite flat closure therefore picks a subproduct of these finite étale factors, and is finite étale. These groups are covered by the extension assertion.

This finite-level assertion does not extend to arbitrary \(p\)-power models: FF7 gives a generic isomorphism whose inverse does not extend. Nor does it construct the semiabelian ambient models or their period cover for an arbitrary abelian variety. The uniformization construction still must produce those objects, compatible ambient actions and the required local covering map. Finite flat quotient representability, where needed in transferring that construction through isogenies, must also be proved. The results here supply the all-integer kernels and their canonical closures, with their nilpotents retained. \(\square\)

Free background for these integral group-scheme objects is [Brinon and Conrad, *CMI Summer School Notes on p-adic Hodge Theory*, §7.1](https://math.stanford.edu/~conrad/papers/notes.pdf), and the author notes [*Finite flat group schemes*](https://web.stanford.edu/~dkim04/sags-2510/2025-10-08/). The flatness, covering descent, characteristic-zero primitive-element argument, saturated closure and integral model computations used here are proved in this section. No crystalline, semistable or residue-characteristic comparison theorem is being invoked.

#### 2G.9. Graded exercise: finite flat kernels and their integral models

This exercise is worth **100 points**, with **10 points for each part**. All kernels and special fibres are scheme-theoretic unless a point count is explicitly requested.

**(a) The rank test.** Over \(R=\mathbf Z_p\), compute the generic dimension and special-fibre dimension of \(M=R\oplus R/p^2R\). Explain why FF1 does not declare this module free. Over \(D=k[\epsilon]/\epsilon^2\), the module \(D/(\epsilon)\) has fibre dimension one at its only point. Explain precisely why the integral-domain hypothesis of the rank test cannot be discarded.

**(b) Openness with a nilpotent fibre.** In \(C=\mathbf Z_p[z]/(z^p-1)\), put \(u=z-1\). Compute the characteristic polynomial of multiplication by \(u\), and use (FF2) to determine the image of \(D(u)\) in \(\operatorname{Spec}\mathbf Z_p\). Compare the generic and special fibres. Does universal openness assert that every nonempty open of the source surjects onto the target?

**(c) All-integer semiabelian ranks.** In (FF1) take residue characteristic five, \(a=2,t=3,n=5\). Compute the ranks of the toric, abelian and semiabelian kernels, and the rank of multiplication on \(\mathcal G\). Compute the dimension of the tangent space of its special kernel at the identity. If this data occurs in a genuine period presentation of a proper abelian variety, compare its generic \(5\)-torsion order with the rank of the integral finite part. Explain what has not been constructed for the period directions.

**(d) A root cover over a nonreduced base.** For \(A=\mathbf F_p[\epsilon]/\epsilon^2\), consider
\[
 C=A[z^{\pm1}]/(z^p-(1+\epsilon)^{-1}).
 \tag{FFX1}
\]
Give its free \(A\)-basis. With \(u=z-1\), identify it as an \(\mathbf F_p\)-algebra with a truncated polynomial algebra, retaining its full nilpotent length. Is this root cover finite flat? Is it étale?

**(e) Primitive elements in characteristic \(p\).** In the dual Hopf algebra of \(\alpha_p=\operatorname{Spec}\mathbf F_p[x]/x^p\), let \(D\) be the derivative-at-zero functional. Prove that \(D\) is primitive, that \(D^p=0\), and that its lower powers span the dual. For \(\mu_p\), use the basis \(z^i\), \(0\le i<p\), and the functional \(D(z^i)=i\) to compute \(D^p\). Identify the exact step in FF5 that fails in these two examples.

**(f) A nonsaturated subgroup model.** In \(\mu_{p,\mathbf Z_p}\), let \(\mathcal H\) be the closed subscheme with coordinate algebra
\[
 B=\mathbf Z_p[z]/(z^p-1,\ p(z-1)).
 \tag{FFX2}
\]
Prove that it is a subgroup scheme, compute its generic and special fibres and its underlying \(\mathbf Z_p\)-module, and find the saturated finite flat closure of its generic subgroup. Why is this not a counterexample to uniqueness in FF6?

**(g) The cyclotomic model map.** Compute the determinant valuations in (FF11) for \(p=2,3,5\). Explain why the abstract generic groups are isomorphic and the special models are not. Check directly for \(p=2\) that the generic inverse evaluation map requires a nonunit denominator.

**(h) Full transitions.** Take \(p=3,a=1,t=2\). Compute the ranks of the kernels at levels \(3,9,27\), the degree of the transition at each step, and the rank of its toric part at level nine. How many geometric special points does that toric part have? Prove the Chinese remainder maps (FF7) for \(m=4,n=9\) by finding suitable integers \(a,b\); the argument must work on every test scheme.

**(i) Extending morphisms.** Compare the two evaluation maps from the constant group of order two to \(\mu_2\) over \(\mathbf Z_3\) and over \(\mathbf Z_2\). Determine which is an isomorphism, including its inverse on coordinate algebras. Explain how the finite étale hypothesis in FF8 gives uniqueness and coherence for generic semilinear group actions, and why it does not give the analogous claim for all finite flat \(p\)-power models.

**(j) The geometric application.** State exactly which all-integer multiplication, subgroup-closure and finite-level action inputs have been proved in this section. Explain why they do not construct a general semistable period cover or a full integral \(p\)-divisible model of a degenerating proper abelian variety. Identify the quotient representability and ambient-model questions still required when transferring a period construction through isogenies.

**Complete solution.**

**(a)** Tensoring with \(\mathbf Q_p\) kills the torsion summand, giving dimension one. Tensoring with \(\mathbf F_p\) gives two copies of that field, so gives dimension two. The equal-dimension hypothesis of FF1 fails. The module is not free, since it has nonzero elements killed by \(p^2\).

For the dual numbers there is no fraction field to which the domain argument could be applied. The fibre module has dimension one, but the module itself has \(k\)-dimension one, while a free rank-one \(D\)-module has \(k\)-dimension two. The kernel of the surjection \(D\to D/(\epsilon)\) is nonzero, and the proof's assertion that a submodule of a free module cannot vanish generically is unavailable on this nonreduced base. Fibre dimension alone does not prove flatness there.

**(b)** The monomial basis in \(u\) identifies multiplication by \(u\) with the companion operator of its monic defining polynomial. Its characteristic polynomial is
\[
 P_u(T)=(1+T)^p-1
       =T^p+\binom p{p-1}T^{p-1}+\cdots+pT.
 \tag{FFX3}
\]
The ideal of its nonleading coefficients is \((p)\): every one is divisible by \(p\), and the coefficient of \(T\) is \(p\). Formula (FF2) therefore gives image \(D(p)=\operatorname{Spec}\mathbf Q_p\). The generic fibre contains nonidentity roots on which \(u\ne0\), while the special fibre has \(u^p=0\), so its whole underlying point set has \(u=0\). This is an open image and agrees with universal openness. That property says that images of opens are open, not that every such image is the whole base.

**(c)** The respective ranks are
\[
 5^3=125,\qquad 5^4=625,\qquad
 5^7=78125,\qquad \deg[5]_{\mathcal G}=78125.
 \tag{FFX4}
\]
The special semiabelian group has dimension \(a+t=5\). Its derivative under multiplication by five is zero, so the tangent kernel at the identity has dimension five; in particular the finite kernel is not étale. For a genuine period presentation PC5 gives a proper abelian variety of dimension five and generic \(5\)-torsion order \(5^{10}=9765625\). The factor \(5^3\) from its three period directions accounts for the difference in generic orders. FF3–FF4 constructs the integral finite part of rank \(5^7\); it has not extended those generally nonintegral periods into an additional finite flat kernel model over \(R\).

**(d)** The elements \(1,z,\ldots,z^{p-1}\) are an \(A\)-basis: the defining equation is monic, its constant is a unit and \(z^{-1}=(1+\epsilon)z^{p-1}\). In this characteristic \((1+\epsilon)^{-1}=1-\epsilon\), and \(u=z-1\) satisfies \(u^p=-\epsilon\). Thus
\[
 C\simeq\mathbf F_p[\epsilon,u]/(\epsilon^2,u^p+\epsilon)
     \simeq\mathbf F_p[u]/u^{2p},\qquad
 \dim_{\mathbf F_p}C=2p.
 \tag{FFX5}
\]
It is free of rank \(p\) over the length-two base and therefore finite flat, with faithful positive rank. Its relative derivative is \(pz^{p-1}=0\); the relative differential \(dz\) has no additional relation, so its module of relative differentials is nonzero. It is not étale. Replacing this algebra by its one geometric point would lose length \(2p\).

**(e)** For the additive group law \(\Delta(x)=x\otimes1+1\otimes x\), the convolution powers satisfy
\[
 D^r(x^j)=
 \begin{cases}r!&j=r,\\0&j\ne r,\end{cases}
 \quad(0\le r,j<p),\qquad D^p=0.
 \tag{FFX6}
\]
This follows by expanding the iterated sum of \(r\) tensor coordinates and applying the derivative functional to each. A monomial contributes only when its degree is \(r\) and every coordinate has degree one. These lower factorials are nonzero in \(\mathbf F_p\), so the \(p\) powers are a basis of the dual. The derivative product rule makes \(D\) primitive there. Hence this dual is the Hopf algebra \(\mathbf F_p[D]/D^p\).

For the multiplicative coordinate, \(\Delta(z^i)=z^i\otimes z^i\), so
\[
 D^r(z^i)=i^r,\qquad D^p=D.
 \tag{FFX7}
\]
The product rule at the identity follows from \(i+j\) reduced modulo \(p\), so again \(D\) is primitive. The functions of \(i\in\mathbf F_p\) given by \(1,i,\ldots,i^{p-1}\) are a basis: the Vandermonde determinant on these distinct field elements is nonzero. Thus this dual is \(\mathbf F_p[D]/(D^p-D)\). In both examples the degree-\(p\) relation is compatible with primitiveness because the mixed binomial coefficient \(p\) is zero. The nonzero characteristic-zero coefficient used in FF5 is exactly what has failed.

**(f)** Put \(u=z-1\). The relation \(pu=0\) kills all nonleading intermediate terms in \((1+u)^p-1\), giving
\[
 B\simeq\mathbf Z_p[u]/(pu,u^p)
   \simeq\mathbf Z_p\oplus
     \bigoplus_{j=1}^{p-1}(\mathbf Z_p/p\mathbf Z_p)u^j.
 \tag{FFX8}
\]
The ideal generated by \(pu\) in the coordinate Hopf algebra of \(\mu_p\) is a Hopf ideal: since \(\Delta(u)=u\otimes z+1\otimes u\), its comultiplication is \(pu\otimes z+1\otimes pu\); its counit is zero, and the antipode sends \(pu\) to \(-z^{-1}pu\). This proves the subgroup assertion scheme-theoretically.

Generically \(u=0\), so the subgroup is the identity. Specially its algebra is \(\mathbf F_p[u]/u^p\), of length \(p\). The displayed nonzero \(p\)-torsion shows that this model is not flat. Saturation replaces the ideal \((pu)\) by \((u)\), giving the identity section \(\operatorname{Spec}\mathbf Z_p\) as the unique finite flat closure. FF6 asserts uniqueness among flat closed models in the fixed ambient scheme; the nonsaturated model fails that hypothesis.

**(g)** The valuations and corresponding cokernel lengths are
\[
 p=2:\ 1,\qquad p=3:\ 3,\qquad p=5:\ 10.
 \tag{FFX9}
\]
Over \(K\) the \(p\) distinct roots give the evaluation algebra isomorphism and identify the abstract groups. Modulo the uniformizer all roots reduce to one, while the constant group still has \(p\) distinct points. For \(p=2\), its matrix and inverse over the fraction field are
\[
 E=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
 E^{-1}=\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
 \tag{FFX10}
\]
Here \(K=\mathbf Q_2\), and \(1/2\) is not integral. Thus the inverse has no integral extension. This agrees with the nonreduced special fibre of \(\mu_2\).

**(h)** The height is \(2a+t=4\). The levels and transition ranks are
\[
 3^4=81,\qquad 3^8=6561,\qquad
 3^{12}=531441,\qquad \deg[3]=81.
 \tag{FFX11}
\]
At level nine its toric part is \(\mu_9^2\), of rank \(9^2=81\) and with one geometric special point: in characteristic three each coordinate has algebra \(k[u]/u^9\). Its scheme length, rather than that point count, is the relevant rank.

For \(m=4,n=9\), use \(a=1,b=-2\), since \(9-8=1\). The maps are \(x\mapsto(9x,4x)\) and \((u,v)\mapsto u-2v\). If \(4u=0\) and \(9v=0\), their composites give
\[
 9(u-2v)=u,\qquad4(u-2v)=v,\qquad
 9x-2(4x)=x.
 \tag{FFX12}
\]
The equalities use only the group laws and integer relations on the sections of every test scheme. Yoneda therefore proves the isomorphism of finite flat group schemes, including all nilpotents.

**(i)** Both maps have the matrix \(E\) in (FFX10). Over \(\mathbf Z_3\) its determinant \(-2\) is a unit and the displayed inverse is integral. This is an isomorphism of the two finite étale models. Over \(\mathbf Z_2\) the determinant is a nonunit and the inverse does not extend; the target has the nonreduced special fibre computed above.

For finite étale models over the complete DVR, a common finite unramified cover splits the schemes into components. The generic component function extends uniquely, and finite faithfully flat descent gives the integral map. A generic identity between any two composites then gives an integral identity, since the finite free source coordinates inject into their generic algebra. This proves the coherence of extended group actions. The \(2\)-adic example violates finite étaleness and shows why that proof cannot be applied indiscriminately to finite flat \(p\)-power models.

**(j)** FF2–FF4 construct multiplication and every kernel for every positive integer, their full finite flat ranks, transitions and integral finite-part division towers. FF5 supplies the characteristic-zero finiteness/étaleness and annihilating integer, and FF6 constructs the saturated closure of each finite generic subgroup in the supplied integral group, with its base-change and map functoriality. FF8 gives actual generic-morphism and finite-action extension for finite étale models over the complete DVR.

The input integral semiabelian group itself is still supplied. These statements do not construct it from an arbitrary abelian variety, make the period injection or local uniformizing map, prove the needed quotient scheme exists for every finite flat subgroup, or show the quotient remains in the required smooth semiabelian/good-reduction class. Those quotient and ambient-model constructions are required in an isogeny-transfer argument. Nor has the extra generic period part of the proper abelian torsion been extended to a full integral \(p\)-divisible group. The general period-cover construction, compatible ambient actions and any claimed dual-model pairing identification remain to be proved.

### 2H. Finite flat quotients and preservation of good reduction

A multiplication map supplies the affine charts needed for the quotient. This is useful even when no relatively ample line on the integral model has been constructed. Throughout this section \(R\) is a discrete valuation ring as in §2G, or a field. The supplied commutative group \(\mathcal G/R\) is either an abelian scheme of relative dimension \(a\), or the semiabelian extension in (FF1), with torus rank \(t\). Put \(t=0\) in the abelian case. Fix
\[
 \mathcal H\hookrightarrow\mathcal G[N],\qquad
 N\ge1,\qquad \operatorname{rank}_R\mathcal H=h.
 \tag{FQ1}
\]
The subgroup is finite locally free. It need not be étale, and \(N\) need not be a unit. FF2–FF3 prove that \([N]_{\mathcal G}\) is finite faithfully flat of rank \(N^{2a+t}\). Over a field the same root-cover proof, with CU8 for the abelian part, proves this assertion.

The earlier affine quotient proof is Lesson 3, §0.F.4.17, QS2–QS5. Its algebra uses a Noetherian base, a finite locally free group acting on an affine scheme, and a closed free action relation. It does not use the dimension or properness of an elliptic curve. We spell out its application below. Free comparisons are the Stacks project's [affine finite flat quotient](https://stacks.math.columbia.edu/tag/03BM) and [flat smooth-fibre criterion](https://stacks.math.columbia.edu/tag/00TF). The proofs used here are the actual programme proofs and the arguments in this section.

#### 2H.1. Invariant charts and the scheme quotient

**FQ1.** The fppf quotient \(\mathcal Q=\mathcal G/\mathcal H\) is represented by a separated finite-type commutative group scheme. Its quotient map and relation satisfy
\[
 q:\mathcal G\longrightarrow\mathcal Q
 \text{ finite faithfully flat of rank }h,\qquad
 \mathcal H\times_R\mathcal G
       \xrightarrow{\sim}\mathcal G\times_{\mathcal Q}\mathcal G,
 \quad (z,x)\longmapsto(x,x+z).
 \tag{FQ2}
\]
These are full scheme identities. The quotient and its invariant-map universal property commute with every base change.

*Proof.* For every affine open \(V\subset\mathcal G\), the open \(U=[N]^{-1}V\) is affine because multiplication is finite. It is invariant under \(\mathcal H\), as the equality
\([N](x+z)=[N]x\) holds on every test scheme when \([N]z=0\). These opens cover \(\mathcal G\). The action relation on \(U\) is closed in \(U^2\): its inverse image under the difference map \((x,y)\mapsto y-x\) is exactly \(\mathcal H\), and the inverse identification is \((x,y)\mapsto(y-x,x)\). Here and below the squares are over \(R\).

Write \(U=\operatorname{Spec}A\), \(\mathcal H=\operatorname{Spec}C\), and let \(\rho:A\to A\otimes_R C\) be the coaction. Its two maps are \(s(a)=a\otimes1\) and \(u(a)=\rho(a)\). Put
\[
 D=\{a\in A:\rho(a)=a\otimes1\},\qquad
 A\otimes_D A\longrightarrow A\otimes_R C,\quad
 a\otimes b\longmapsto(a\otimes1)\rho(b).
 \tag{FQ3}
\]
The map is surjective by the closed relation. The characteristic polynomial of multiplication by \(\rho(a)\), on the rank-\(h\) algebra over \(s(A)\), has invariant coefficients: translation of the orbit conjugates this multiplication after pullback along the relation. Its identity-section specialization gives a monic equation for \(a\) over \(D\). Hence \(A/D\) is integral and finite, using bounded powers of finitely many algebra generators. QS2 proves that \(D\) is Noetherian and of finite type over \(R\): collect the finite multiplication-table coefficients in a finite-type subring \(D_0\), make \(A\) finite over \(D_0\), and use that its submodule \(D\) is finite.

The common-basis argument QS3–QS4 proves more than integrality. At each localization of \(D\), extend faithfully flat to a local ring with infinite residue field. The finitely many maximal ideals of the resulting finite algebra \(A\) admit one choice of \(x_1,\ldots,x_h\) for which the \(\rho(x_i)\) are a basis over \(s(A)\): avoid the finitely many nonzero determinant polynomials over that infinite field. If
\(\rho(a)=\sum_i(c_i\otimes1)\rho(x_i)\), coassociativity compares the two expansions after a second coaction and gives \(\rho(c_i)=c_i\otimes1\). The identity section then gives \(a=\sum_i c_ix_i\), and independence follows by applying \(\rho\) again. Thus \(A\) is free of rank \(h\) over \(D\) on that faithfully flat local extension, and (FQ3) is an isomorphism there. FD1 and FD4 descend both assertions. Consequently \(A/D\) is finite locally free of positive rank \(h\), hence faithfully flat, and (FQ3) is an isomorphism before extension. This is exactly the already proved QS3–QS4 argument; no division by \(h\) occurs.

For completeness, the gluing does not assume that the intersection of two charts is affine. If \(W\subset U\) is invariant and open, its complement has closed image under the finite map \(U\to\operatorname{Spec}D\). The complement of that image is an open with inverse image \(W\). Indeed a geometric fibre is a single orbit by (FQ3), including its scheme relation; invariance decides whether the whole fibre lies in \(W\). On that open, FD5 gives the invariant-map quotient property. Apply this to each pairwise intersection of invariant charts. The resulting identifications of quotient opens are unique, so satisfy the triple cocycle and glue. Finiteness and the rank assertion are local on these target opens. FD5 also descends addition under the product cover, inversion and the origin. Their identities are detected on finite faithfully flat product covers. This proves (FQ2) and the group assertions.

The preimage of the diagonal of \(\mathcal Q\) under \(q^2\) is the closed action relation. FD6 descends the closed immersion, proving separatedness. Finite type follows from the finite-type rings \(D\) and a finite choice of charts. Finally, after any \(R\to R'\), the finite faithfully flat map and the relation isomorphism (FQ2) persist. FD1 applied to that cover gives
\[
 (A\otimes_R R')^{\mathcal H_{R'}}=D\otimes_R R'.
 \tag{FQ4}
\]
This conclusion uses the proved torsor, and does not assume that an arbitrary kernel commutes with nonflat tensor. A point of the quotient sheaf lifts after this finite cover; two lifts differ by a unique section of \(\mathcal H\). This proves its fppf sheaf representation and the base-change assertion, even for non-Noetherian or nonreduced \(R'\). \(\square\)

#### 2H.2. The complementary finite flat map

**FQ2.** There is a unique homomorphism \(d:\mathcal Q\to\mathcal G\) with
\[
 d q=[N]_{\mathcal G},\qquad qd=[N]_{\mathcal Q}.
 \tag{FQ5}
\]
It is finite faithfully flat of rank \(N^{2a+t}/h\). In particular this quotient is an integer. Moreover
\[
 \ker d\simeq\mathcal G[N]/\mathcal H
 \quad\text{as fppf sheaves and finite locally free group schemes}.
 \tag{FQ6}
\]

*Proof.* Multiplication by \(N\) is invariant under \(\mathcal H\). FD5 descends it along \(q\), giving \(d\), and descends its group identity. After composition with \(q\), the second identity of (FQ5) is the first identity followed by \(q\); faithful descent cancels \(q\) and proves it.

On the chart \(V=\operatorname{Spec}B\) used in FQ1, let \(U=\operatorname{Spec}A=[N]^{-1}V\) and \(U/\mathcal H=\operatorname{Spec}D\). The ring maps for the factorization are
\[
 B\longrightarrow D\longrightarrow A,\qquad
 A/B\text{ finite locally free of rank }N^{2a+t},
 \quad A/D\text{ finite locally free of rank }h.
 \tag{FQ7}
\]
The invariant ring \(D\subset A\) is a finite \(B\)-module, because \(B\) is Noetherian and \(A\) is finite over it. For an injection of \(B\)-modules, tensor first with \(D\), then with \(A\). The composite tensor is injective by flatness of \(A/B\). Faithful flatness of \(A/D\) detects injectivity already after \(D\). Thus \(D/B\) is flat; it is finite and finitely presented, so is finite locally free by Lesson 3, T4–T5. Multiplication is surjective and factors through \(d\), so \(d\) is surjective. Its local rank \(r\) satisfies \(hr=N^{2a+t}\): take a residue field of \(B\), decompose the finite algebra \(D\) into its local factors, and use that the locally free \(D\)-module \(A\) has rank \(h\). Equivalently its vector-space dimension over that residue field is \(h\) times the dimension of \(D\). This proves the rank.

Pulling the \(q\)-torsor back over \(\ker d\) gives its inverse image \(\mathcal G[N]\), by (FQ5). The same quotient property therefore proves (FQ6). Its rank is \(N^{2a+t}/h\). All these identities survive arbitrary base change by FQ1. \(\square\)

#### 2H.3. Smoothness of the quotient

**FQ3.** The group \(\mathcal Q/R\) is smooth, with geometrically integral fibres of dimension \(a+t\). If \(\mathcal G/R\) is an abelian scheme, so is \(\mathcal Q/R\).

*Proof.* First \(\mathcal Q/R\) is flat. On the charts \(R\to D\to A\), the last ring is flat over \(R\) because it is an open of the smooth \(\mathcal G\); the same tensor-injection argument as in FQ2 descends this flatness through the faithfully flat \(D\to A\).

Let \(k\) be an algebraically closed residue extension. The fibre \(\mathcal G_k\) is integral. In the semiabelian case it is connected: its map to the connected abelian variety is a surjective smooth torsor with connected torus fibres. If the total space were disconnected, a partition into its finitely many open-and-closed components would partition the base into disjoint open images, since a connected fibre meets only one part. This contradicts connectedness of the base. Its smooth local rings are regular domains by the polynomial-chart regularity argument NM1 in Lesson 8; distinct irreducible components are therefore disjoint, so connectedness makes the fibre irreducible and reduced. The abelian case has these same properties by its definition and the field results above.

On every nonempty quotient affine, (FQ4) embeds \(D_k\) in the domain \(A_k\). Thus the quotient fibre is reduced, and it is irreducible as the surjective image of \(\mathcal G_k\). Its dimension is \(a+t\): integral finite maps preserve dimension by lying over, going up and incomparability, proved in Lesson 3, §0.A. We now prove the smoothness assertion for this integral algebraic group, rather than inferring it from a possibly nonétale quotient map.

Here is the needed generic smoothness fact over a perfect field \(k\). Every finitely generated field \(K/k\) of transcendence degree \(r\) has a separating transcendence basis. In characteristic zero, choose any transcendence basis; the remaining finite algebraic extension is separable because an irreducible polynomial has nonzero derivative. In characteristic \(p\), the degree calculation (EH3) gives \([K:K^p]=p^r\). Starting from \(K^p\), successively adjoin an element not yet in the subfield. Each step has degree \(p\), since its \(p\)-th power is already in \(K^p\). This produces \(u_1,\ldots,u_r\) whose \(p\)-restricted monomials form a basis over \(K^p\). Differentiating those unique expansions defines derivations \(\partial_i\) with \(\partial_i u_j=\delta_{ij}\); the relations \(u_i^p\in K^p\) verify the product rule. Every \(k\)-derivation of \(K\) is determined by its values on the \(u_i\), because it kills \(K^p\).

The \(u_i\) are algebraically independent over \(k\). Otherwise choose a nonzero polynomial relation of smallest total degree. Applying each \(\partial_i\) makes each nonzero partial derivative a relation of smaller degree. Hence all polynomial partial derivatives must vanish. Perfectness makes the polynomial a \(p\)-th power of a polynomial of smaller degree, giving the same contradiction. Put \(F=k(u_1,\ldots,u_r)\). The finite extension \(K/F\) has no nonzero \(F\)-derivation. This implies separability, as follows. Let \(E\) be the subfield of elements of \(K\) separable over \(F\). It is a finite separable extension, and \(K/E\) is purely inseparable: some \(p\)-power of each element is separable, by writing its irreducible polynomial as a separable polynomial in \(T^{p^s}\). If \(K\ne E\), then \(K\ne E K^p\). Indeed equality could be iterated to \(K=E K^{p^s}\), whereas a sufficiently large power lies in \(E\). A \(p\)-restricted basis obtained by adjoining elements over \(E K^p\) then defines a nonzero \(E\)-derivation exactly as above. It is an \(F\)-derivation, a contradiction. Thus \(K=E\).

This field statement produces a nonempty smooth open in any integral finite-type \(k\)-scheme. Write its function field as \(k(u_1,\ldots,u_r)(\theta)\), using the finite separable primitive-element proof of Lesson 1, §0E. Clear denominators in the monic minimal polynomial \(f(T)\) of \(\theta\), and invert \(f'(\theta)\ne0\). The resulting algebra
\[
 k[u_1,\ldots,u_r,s^{-1},T,f'(T)^{-1}]/(f(T))
 \tag{FQ8}
\]
is a standard smooth algebra of relative dimension \(r\), by Lesson 3, SF3. It is a domain with the desired fraction field. It and any chosen affine coordinate domain with that fraction field have isomorphic nonempty principal opens: put the finitely many generators of the second algebra in a localization of the first by clearing their denominators, and then clear the generators of the first and that denominator in the second. Localizing these two inclusions at the product of the finitely many additional nonzero denominators makes them inverse. This proves the claimed nonempty smooth open. When the function field already equals the rational field, one may omit \(T\), or use \(f(T)=T\).

Apply this to the integral group \(\mathcal Q_k\). Its nonempty smooth open contains a closed \(k\)-point by the finite-type closed-point lemma of Lesson 3, B1. Translation takes this point to any other closed point and is a scheme isomorphism. Thus every closed point has a smooth chart. The complement of their open union, if nonempty, would again have a closed point by B1. Hence the whole geometric fibre is smooth.

Smoothness descends from this algebraic closure to the residue field itself by the relation-gradient argument in QS6: in any finite polynomial presentation, the split injection of the relation module and finite projectivity of the differential module are detected and descended by FD1 and FD4; SF1–SF2 then give the smooth charts. Finally QS6's proof of the flat smooth-fibre criterion applies in every dimension. In its notation \(P/I=D\), flatness gives the exact fibre presentation. Lift generators of the smooth fibre ideal with an invertible gradient minor. Nakayama applied to the finite module \(I/(f_1,\ldots,f_c)\) at the chosen point shows these lifts generate the whole local ideal; invert the lifted minor. SF3 gives an actual smooth chart over \(R\). This retains every nilpotent layer in the base.

If \(\mathcal G\) is proper, then so is \(\mathcal Q\). For every base change, a closed subset of \(\mathcal Q\) and its closed inverse image in \(\mathcal G\) have exactly the same image in the base. That image is closed by properness of \(\mathcal G\). Thus \(\mathcal Q\) is universally closed, and already separated and of finite type. Its geometric fibres are connected, so the proper smooth group with its descended origin is an abelian scheme. Relative projectivity was not an input to this argument. \(\square\)

#### 2H.4. Good reduction transfers through every isogeny

**FQ4.** Let \(R\) be a discrete valuation ring with characteristic-zero fraction field \(K\), and let \(\mathcal B/R\) be an abelian scheme. If \(f:\mathcal B_K\to A\) is an isogeny of abelian varieties, then \(A\) has a good abelian model over \(R\). Every generic isogeny between two good abelian models extends uniquely to a finite faithfully flat isogeny of those models. Its kernel is the canonical finite flat closure in FF6, including when its degree is divisible by the residue characteristic.

*Proof.* The generic kernel \(H_K\) is finite étale by FF5. Put \(n=\operatorname{rank}_K H_K\). The finite group coset proof in FF5 gives \([n]H_K=0\) as a scheme identity. FF6 therefore constructs its finite flat closure \(\mathcal H\subset\mathcal B[n]\), of rank \(n\). FQ1–FQ3 construct the abelian scheme \(\mathcal C=\mathcal B/\mathcal H\).

The generic isogeny \(f\) is the quotient by \(H_K\). One can use the finite flat isogeny proof CE6; here is also a characteristic-zero verification. Proper finite fibres make \(f\) finite. The finite étale kernel has zero tangent space, so the differential at the origin is an isomorphism between tangent spaces of the same dimension. Translation and SF1–SF3 make the whole map étale. It is surjective by the isogeny hypothesis, hence finite faithfully flat. The difference map identifies its relation with \(H_K\times\mathcal B_K\). FD5 gives the scheme-valued quotient property. Uniqueness of that property identifies \(\mathcal C_K\) with \(A\), compatibly with \(f\).

If \(A\) already has a good model \(\mathcal B'\), GQ2 extends this generic isomorphism and its inverse between \(\mathcal C\) and \(\mathcal B'\). Uniqueness in GQ2 makes their composites identities. Thus the extended \(f\) is \(q\) followed by an isomorphism; its kernel and finite flat rank are exactly \(\mathcal H\) and \(n\). Uniqueness also identifies it with the generic-map extension originally given by GQ2.

For any supplied positive annihilator \(N\), FQ2 gives the complementary integral homomorphism \(d:\mathcal B'\to\mathcal B\), with
\[
 df=[N]_{\mathcal B},\qquad fd=[N]_{\mathcal B'},\qquad
 \deg f=n,\qquad \deg d=N^{2a}/n.
 \tag{FQ9}
\]
In particular \(N=n\) is allowed. All assertions commute with extensions of discrete valuation rings, by FF6 and FQ1. No prime-to-residue restriction was introduced. \(\square\)

#### 2H.5. Maps, finite actions and torsion

**FQ5.** Suppose \(v:\mathcal G\to\mathcal G'\) is an actual integral homomorphism and \(v(\mathcal H)\subset\mathcal H'\). There is a unique homomorphism
\[
 \bar v:\mathcal G/\mathcal H\longrightarrow
             \mathcal G'/\mathcal H',\qquad
 \bar v q=q'v.
 \tag{FQ10}
\]
This construction respects identities, composition and arbitrary base change. Stable finite semilinear actions on the supplied ambient models and subgroups descend to their quotients.

*Proof.* The right side of (FQ10) is invariant under \(\mathcal H\) as a full scheme map. FD5 descends it uniquely. The group law is detected after the product cover, and identities and composites are detected after \(q\). For a semilinear map use the corresponding base twist. Apply the same uniqueness to each group element and to each pairwise composite; their cocycles therefore hold on the quotient. This constructs actions from supplied actions, and does not create an unspecified integral ambient action.

For a generic isogeny of good models, every prime-to-residue Tate-module map is the actual generic map, since FQ4 extends that map itself. CU10 gives
\[
 [T_\ell\mathcal B'_K:fT_\ell\mathcal B_K]
       =\ell^{v_\ell(n)},\qquad
 V_\ell\mathcal B_K\xrightarrow{\sim}V_\ell\mathcal B'_K.
 \tag{FQ11}
\]
GQ4 gives the unramified actions from both good models; the maps commute with them because the morphisms do. These conclusions concern the actual modules and their transitions. They do not identify a general \(p\)-adic comparison functor or a full integral period model. \(\square\)

#### 2H.6. The geometric fibres in the semiabelian case

**FQ6.** In the supplied semiabelian case, each geometric fibre of \(\mathcal Q\) is semiabelian of torus rank \(t\), and its abelian quotient is isogenous to the corresponding fibre of \(\mathcal B\).

*Proof.* Work over an algebraically closed residue field \(k\), and write \(G,T,B,H,Q\) for the fibres. The group \(K_0=H\cap T\) is finite over \(k\), hence finite locally free. First \(T/K_0\) is a torus of rank \(t\), with a direct coordinate proof. Write the character lattice of \(T\) as \(M=\mathbf Z^t\). The images in \(k[K_0]\) of its Laurent monomials are group-like elements, and span that algebra since \(K_0\) is closed. Distinct group-like elements in any coalgebra over a field are linearly independent. To prove this, take a dependence with a minimal number of distinct terms, express the last as a linear combination of the others, and apply comultiplication. Independence of those others in the first tensor factor forces every element with a nonzero coefficient to equal the last, a contradiction. Their counits are one, so none is zero.

The images therefore form a finite group \(M/L\), and the quotient Hopf algebra is precisely \(k[M/L]\); there are no further linear relations. The invariant subalgebra of \(k[M]\) is \(k[L]\), by comparing those independent group-like coefficients. Since \(M/L\) is finite, PC0 gives \(L\simeq\mathbf Z^t\). Coset representatives give
\[
 k[M]=\bigoplus_{\gamma\in M/L}k[L]\chi^\gamma,\qquad
 T/K_0=\operatorname{Spec}k[L]\simeq\mathbf G_m^t.
 \tag{FQ12}
\]
The coordinate tensor identity, or FQ1's affine proof, shows that this is the full finite flat \(K_0\)-torsor quotient, including nonreduced \(K_0\).

Next the scheme-theoretic image \(J\) of \(H\to B\) is a finite closed subgroup, killed by \(N\). Indeed the map is finite, by its proper finite fibres, and its image is the finite algebra obtained as the image of the target coordinates in the finite \(k\)-algebra of \(H\); these local descriptions glue. Quotient \(H\) by \(K_0\) using the affine proof QS2–QS4: \(H\) itself is an affine finite scheme, its translation action is free and closed, so that proof applies without smoothness. The induced map \(H/K_0\to B\) is a monomorphism. Its kernel is trivial as a sheaf, since a section lifts fppf locally to \(H\) and an element mapping to zero belongs to \(K_0\). A homomorphism with trivial kernel is a monomorphism by subtraction.

This finite monomorphism is a closed immersion. To check the hypothesis of the already proved proper criterion CIE1, its geometric fibres have at most one point and no nonzero tangent vector: any such vector would contradict the monomorphism on dual-number points. A nonempty finite local algebra over an algebraically closed field with zero cotangent space is that field, by Nakayama on its maximal ideal. Hence each geometric fibre is empty or the full reduced point, and CIE1 applies. Its image is \(J\), because the preceding quotient is faithfully flat. Thus \(H\to J\) is finite faithfully flat, with kernel \(K_0\).

FQ1–FQ3 over \(k\) make \(B/J\) an abelian variety. The map \(G\to B/J\) descends to \(Q\). It is fppf surjective. Its kernel is exactly \(T/K_0\): a section of the kernel lifts locally to \(G\); its image in \(B\) lies in \(J\), so lift that image locally to \(H\) and subtract. The result belongs to \(T\). Two such torus lifts differ exactly by \(K_0\). We obtain the full fppf exact sequence
\[
 0\longrightarrow T/K_0\longrightarrow Q
       \longrightarrow B/J\longrightarrow0.
 \tag{FQ13}
\]
The kernel is the torus (FQ12). The surjective map is its torsor by subtraction, so this is a semiabelian variety of the stated torus rank. \(\square\)

FQ1–FQ6 give a smooth separated integral-model quotient, its semiabelian geometric fibres, and good abelian quotients with full generic isogeny transfer. In applying them to uniformization one must still construct the initial semiabelian integral extension and its period cover. If that argument needs a particular integral torus-by-abelian sequence for the quotient, that sequence and its compatible maps must be constructed as well; a fibrewise sequence (FQ13) alone is not that construction. No quotient of the period lattice, local covering property, general ambient lift or independently constructed dual-model pairing is supplied by these finite quotient arguments.

#### 2H.7. Graded exercise: quotient algebras and good models

**Exercise 2H (100 points; ten parts of 10 points each).** Use FQ1–FQ6 and the indicated earlier proofs. Include the full scheme kernels, rather than only their geometric point sets.

**(a) A quotient with nonreduced special kernel.** Over \(R=\mathbf Z_p\), let \(\mu_p\) act on \(\mathbf G_m=\operatorname{Spec}R[x,x^{-1}]\) by multiplication. Compute the invariant algebra, a free module basis, the torsor tensor identity, and the complementary map for \(N=p\). Decide whether the quotient, the quotient map and its special fibre map are smooth.

**(b) A two-dimensional torus.** For any integer \(m\), embed \(\mu_p\) in \(\mathbf G_m^2\) by \(z\mapsto(z,z^m)\). Construct the full quotient map in coordinates, its invariant character lattice and its complementary map for \(N=p\). Compute both degrees, the special differential rank and the special kernel length.

**(c) Why an integral inclusion is insufficient.** Let \(D=k[t^2,t^3]\subset A=k[t]\). Prove that \(A/D\) is finite and has generic rank one, but is not flat at the cusp. Identify the additional algebra assertions in FQ1 that this example does not provide.

**(d) Invariant affine charts.** For \(\mathcal H\subset\mathcal G[N]\), prove directly on test schemes that \([N]^{-1}V\) is invariant for every affine \(V\subset\mathcal G\). Explain why these charts do not require a relatively ample line, and why the group law on their quotient is a full scheme map.

**(e) Complementary degrees.** Let \(\mathcal G/R\) have abelian dimension two and torus rank one. Suppose \(\mathcal H\subset\mathcal G[6]\) is finite flat of rank twelve. Compute the degrees of \([6]\), \(q\), \(d\), and the rank of \(\ker d\). Does the existence of such a subgroup follow from those four numbers alone?

**(f) Good reduction and a residue-divisible isogeny.** A good abelian surface over a characteristic-zero local field admits an isogeny of degree twenty-five to an abelian variety \(A\). Prove that \(A\) has good reduction even when the residue characteristic is five. Use \(N=25\) to compute the complementary degree. Compute the integral Tate-module indices at \(\ell=2,3,5,7\), distinguishing the good-model unramified conclusion from what is available at five.

**(g) A separating basis in positive characteristic.** Over a perfect field \(k\) of characteristic \(p\), put \(K=k(s,t)\). Prove that \(u=s^p+t,\ v=t^p\) are algebraically independent and that \(K/k(u,v)\) is finite purely inseparable of degree \(p^2\). Compute \([K:K^p]\), and give instead a separating transcendence basis. Explain why an arbitrary transcendence basis cannot replace the argument in FQ3.

**(h) Quotients and nonflat base change.** In part (b), reduce first modulo \(p\) and then base change to \(k[\epsilon]/(\epsilon^2)\), with \(k=\mathbf F_p\). Compute the invariant algebra after this change and the finite free rank. Explain why this calculation follows from the torsor, even though taking invariants of a general action need not commute with a nonflat base change.

**(i) A descended finite action.** Let \(\mathbf G_m^2\) have the coordinate-interchange involution and let \(\mathcal H=\{(z,z):z^n=1\}\), over any DVR and with \(n\ge1\). Use quotient coordinates \(U=x^n,\ V=y/x\). Compute the induced involution on \(U,V\), verify its square and check equivariance of the quotient map and the complementary map for \(N=n\). Include the case where the residue characteristic divides \(n\).

**(j) The geometric scope.** State the quotient and isogeny inputs now proved for good abelian models and for supplied semiabelian models. Identify which data still must be constructed for the full general period presentation in Theorem 2.4. Explain why neither an fppf quotient sheaf by itself nor the exact sequence of each geometric fibre substitutes for the required integral and analytic constructions.

**Full solution.**

**(a)** The coaction is \(x\mapsto x\otimes z\), where \(z^p=1\). The monomials \(1,z,\ldots,z^{p-1}\) are a basis over \(R\), including after reduction modulo \(p\). Comparing their coefficients shows that precisely the powers \(x^{pj}\) are invariant. Thus
\[
 D=R[u,u^{-1}],\quad u=x^p,\qquad
 A=\bigoplus_{i=0}^{p-1}Dx^i,\qquad
 A\otimes_D A\simeq A[z]/(z^p-1).
 \tag{FQX1}
\]
In the last map the second copy of \(x\) is \(xz\); conversely \(z=x_2/x_1\). The quotient is the torus with coordinate \(u\), and \(q(x)=x^p\). The complementary \(d\) sends \(u\) to that same unit as a coordinate on the original torus, so is a degree-one isomorphism. Both compositions are multiplication by \(p\) on their respective tori.

The quotient torus is smooth over \(R\). The map \(q\) has differential \(p x^{p-1}\), which vanishes on the special fibre. There its kernel is
\(k[z]/(z^p-1)=k[w]/(w^p)\), of length \(p\), rather than a smooth zero-dimensional scheme. Consequently \(q\) is not smooth, and its special map is finite purely inseparable of degree \(p\). Smoothness of the quotient does not assert smoothness of \(q\).

**(b)** A character \(x^a y^b\) restricts to \(z^{a+mb}\), so its invariant lattice is
\[
 L=\{(a,b)\in\mathbf Z^2:a+mb\equiv0\pmod p\}
   =\mathbf Z(p,0)+\mathbf Z(-m,1).
 \tag{FQX2}
\]
The equality follows by writing \(a+mb=pc\). Hence the quotient torus has coordinates \(U=x^p,\ V=y/x^m\), and
\[
 q(x,y)=(x^p,y/x^m),\qquad
 d(U,V)=(U,U^mV^p),\qquad
 \deg q=\deg d=p.
 \tag{FQX3}
\]
The degree of \(q\) is also certified by the free basis \(1,x,\ldots,x^{p-1}\) over \(R[U^{\pm1},V^{\pm1}]\), since \(y=Vx^m\). Its kernel is exactly \(x^p=1,\ y=x^m\), the given \(\mu_p\) with its full algebra. Direct substitution in both orders gives \((x^p,y^p)\) and \((U^p,V^p)\), proving the complementary identities. On logarithmic differentials the matrix of \(q\) is
\[
 \begin{pmatrix}p&0\\-m&1\end{pmatrix},
 \tag{FQX4}
\]
whose rank modulo \(p\) is one for every \(m\). The special kernel has one geometric point and length \(p\). These statements include negative \(m\), since all coordinates are units.

**(c)** The element \(t\) is integral over \(D\), satisfying \(X^2-t^2=0\), and \(1,t\) span \(A\) over \(D\). Their fraction fields are the same, since \(t=t^3/t^2\), so the generic rank is one. At the cusp maximal ideal \(\mathfrak m=(t^2,t^3)\),
\[
 A/\mathfrak mA=k[t]/(t^2)
 \quad\text{has dimension }2,\qquad
 A\otimes_D\operatorname{Frac}D=\operatorname{Frac}D.
 \tag{FQX5}
\]
If the finite module were flat at that point, finite presentation and T4–T5 would make it free there. Its generic rank would force rank one and therefore a one-dimensional residue fibre, a contradiction. Thus integrality and a finite module generating set do not establish flatness. This example has no proved finite flat free action relation, no common basis with coassociativity, and no torsor identity as in (FQ3). FQ1 supplies exactly those additional assertions.

**(d)** A test-scheme point of the action consists of \(x\in\mathcal G(T)\), \(z\in\mathcal H(T)\). The equation \([N]z=0\) gives \([N](x+z)=[N]x\). Therefore a point over \(V\) remains over \(V\) after translation, and the inverse translation gives equality of the invariant open subfunctors. Since \([N]\) is finite, its preimage of \(V\) is affine. These are actual inverse images under a finite map, requiring no projective embedding.

Addition followed by \(q\) is invariant under the product action of \(\mathcal H^2\) on \(\mathcal G^2\): adding translated inputs changes their sum by an element of \(\mathcal H\). The finite faithfully flat product cover and FD5 descend it uniquely to \(\mathcal Q^2\to\mathcal Q\). Triple product covers detect associativity, and the inverse and origin identities are detected similarly. This proves the group law as a scheme morphism, including nilpotent test bases.

**(e)** Here \(2a+t=5\), so
\[
 \deg[6]=6^5=7776,\qquad
 \deg q=12,\qquad
 \deg d=\operatorname{rank}\ker d=648.
 \tag{FQX6}
\]
The equality is \(12\cdot648=7776\). These are consequences of a supplied subgroup, rather than a construction of one. Divisibility of the rank alone does not specify a closed subgroup, its Hopf algebra, embedding, flatness or compatible integral fibres.

**(f)** The generic kernel is finite étale in characteristic zero, has rank twenty-five, and is killed by twenty-five by FF5. Its FF6 closure is finite flat inside the all-integer kernel \(\mathcal B[25]\). FQ1–FQ4 give the good abelian quotient model of \(A\), even in residue characteristic five. With \(a=2\),
\[
 \deg d=25^4/25=25^3=15625,\qquad
 [T_\ell A:fT_\ell B]=\ell^{v_\ell(25)}
   =\begin{cases}25&\ell=5,\\1&\ell=2,3,7.\end{cases}
 \tag{FQX7}
\]
The index formula is CU10 over the characteristic-zero generic field, so also holds at five. GQ4's good-model unramified statement applies only when \(\ell\) differs from the residue characteristic. In residue characteristic five it proves unramifiedness at two, three and seven; it makes no such assertion at five. The integral finite flat model at five does not replace a \(p\)-adic comparison proof.

**(g)** The field \(K\) is algebraic over \(F=k(u,v)\), since
\[
 t^p=v,\qquad s^p=u-t,\qquad s^{p^2}=u^p-v.
 \tag{FQX8}
\]
It therefore has transcendence degree two over \(k\), forcing \(u,v\) to be algebraically independent: if they were dependent, their field would have transcendence degree at most one, and algebraic extension would not change that degree. This last dimension statement is the field normalization/transcendence calculation GQ1.

Over the rational field \(k(u,v)\), \(v\) has no \(p\)-th root: its exponent valuation at the irreducible polynomial \(v\) is one, whereas every \(p\)-th power has valuation divisible by \(p\). Thus adjoining \(t\) has degree \(p\). The resulting field is \(k(u,t)\). In that rational field \(u-t\) has valuation one at its irreducible linear polynomial, so adjoining \(s\) again has degree \(p\). Both extensions are purely inseparable, giving \([K:F]=p^2\). On the other hand \([K:K^p]=p^2\) by the monomial basis \(s^i t^j\), \(0\le i,j<p\). The pair \(s,t\) itself is a separating transcendence basis, since the remaining field extension is the identity. The arbitrary basis \(u,v\) gives a purely inseparable remaining extension and does not yield the nonvanishing derivative chart (FQ8).

**(h)** Put \(R'=k[\epsilon]/(\epsilon^2)\). The invariant algebra is
\[
 R'[U,U^{-1},V,V^{-1}],\qquad
 A'=R'[x^{\pm1},y^{\pm1}]
    =\bigoplus_{i=0}^{p-1}R'[U^{\pm1},V^{\pm1}]x^i.
 \tag{FQX9}
\]
The torus relation is still \(U=x^p,\ y=Vx^m\). The quotient kernel is the full rank-\(p\) algebra \(R'[w]/(w^p)\), with \(w=z-1\). The basis proves the rank over the ring retaining \(\epsilon\); its length over \(k\) is \(2p\), not \(p\). The tensor identity of part (a), with the extra invariant \(V\), survives this base change. FD1 applied to that faithfully flat cover gives its invariant algebra, which is exactly FQ4. It is not an argument that all equalizer kernels survive a nonflat tensor operation.

**(i)** The quotient map is \(q(x,y)=(x^n,y/x)\); its free rank is \(n\) as in part (b) with \(p\) replaced by \(n\) and \(m=1\). The interchange sends
\[
 \sigma(U,V)=(UV^n,V^{-1}),\qquad
 d(U,V)=(U,UV^n).
 \tag{FQX10}
\]
Substitution gives
\(\sigma^2(U,V)=(UV^n(V^{-1})^n,V)=(U,V)\), and
\(q(y,x)=(y^n,x/y)=\sigma(q(x,y))\). Also
\(d(\sigma(U,V))=(UV^n,U)\), the interchange of \(d(U,V)\). The complementary identities follow by the same substitution as (FQX3). All formulas are Laurent polynomial scheme identities over the original DVR; they still hold when \(n\) is zero in the residue field. In that case the kernel can be nonreduced, but the action and cocycle do not disappear.

**(j)** FQ1 constructs the scheme quotient by each supplied finite locally free subgroup in a multiplication kernel, including all nilpotents and arbitrary base changes. FQ2 gives the complementary finite flat map and its exact degree and kernel. FQ3 proves smoothness of the quotient model and good abelian reduction in the proper case. FQ4 transfers good reduction through every characteristic-zero generic isogeny, and extends isogenies between good models as finite flat maps. FQ5 descends supplied compatible integral maps and finite semilinear actions. FQ6 identifies the semiabelian geometric fibres and their torus rank.

For an arbitrary abelian variety, one still must construct the initial integral semiabelian extension, the actual lattice and equivariant period injection, and the locally covering map to the analytification with its kernel and finite-extension point-lifting properties. A required particular integral torus-by-abelian sequence on a quotient, its compatible maps, and any claimed independent dual-model pairing also need their own construction. A sheaf quotient without representability supplies no scheme charts or model. A collection of geometric-fibre exact sequences supplies neither the required integral morphisms nor an analytic covering. Once a genuine period presentation is constructed, PC1–PC6 prove its period rank, valuation nondegeneracy, all torsion levels and transition-compatible Galois action. The full general theorem remains the requested scope.

### 2I. Integral semiabelian sequences and isogeny transfer of periods

We now construct the integral sequence that was left separate from the fibre sequence (FQ13). This also permits transfer of the precise local-field period presentations used in PC2. The initial period presentation is still an input; the transfer will apply to every isogeny from a variety for which that input has been constructed.

For the integral statements, \(R\) is a complete discrete valuation ring with fraction field \(K\) of characteristic zero, uniformizer \(\pi\) and arbitrary residue field \(k\). The supplied extension and subgroup are
\[
 0\longrightarrow\mathcal T\longrightarrow\mathcal G
   \xrightarrow{b}\mathcal B\longrightarrow0,\qquad
 \mathcal T=\mathbf G_{m,R}^{\,t},\qquad
 \mathcal H\subset\mathcal G[N]\text{ finite locally free}.
 \tag{IS1}
\]
Write \(h=\operatorname{rank}\mathcal H\). All intersections below are scheme-theoretic. The finite flat quotient, arbitrary base change and good abelian quotient proofs are FQ1–FQ5. The required elementary rigidity and subgroup lifting are proved first. For free comparisons, see Conrad's author version of [*Reductive group schemes*, Appendix B, Corollary B.2.7 and Theorem B.3.2](https://math.stanford.edu/~conrad/papers/luminysga3smf.pdf), and the Stacks project's [lifting over henselian pairs](https://stacks.math.columbia.edu/tag/0D49). Only the finite, commutative arguments given here are needed.

#### 2I.1. Finite Cartier duals and torus subgroups

**IS1.** If \(A\) is a finite free commutative and cocommutative Hopf algebra over \(R\), then \(A^\vee=\operatorname{Hom}_R(A,R)\) is again such a Hopf algebra, and its double dual is canonically \(A\). For a finite abelian group \(C\), put
\[
 D_R(C)=\operatorname{Spec}R[C],\qquad
 \Delta[e_c]=[e_c]\otimes[e_c],\quad
 \epsilon[e_c]=1,\quad S[e_c]=[e_{-c}].
 \tag{IS2}
\]
Here \(R[C]\) has basis \([e_c]\) with \([e_c][e_d]=[e_{c+d}]\). The Cartier dual of \(D_R(C)\) is the constant group \(C_R\).

*Proof.* A finite basis gives the isomorphism
\((A\otimes_R A)^\vee=A^\vee\otimes_R A^\vee\), independent of the basis because both sides act by the same evaluation pairing on pure tensors. Dualize comultiplication to define multiplication, and multiplication to define comultiplication; dualize counit, unit and antipode for the other three maps. Each Hopf identity is an identity between maps of finite tensor powers, so dualizing it proves the corresponding identity for the dual maps. Commutativity and cocommutativity interchange. Evaluation identifies the double dual with the original algebra and all its structure maps. These constructions commute with every base change, since a finite free basis and its dual remain bases.

In the basis \(\delta_c\) dual to \([e_c]\), multiplication on \(R[C]^\vee\) satisfies
\[
 \delta_c\delta_d=
 \begin{cases}\delta_c&c=d,\\0&c\ne d,\end{cases}
 \qquad
 \Delta\delta_c=\sum_{a+b=c}\delta_a\otimes\delta_b .
 \tag{IS3}
\]
Thus it is the coordinate algebra \(R^C\) of the constant group, with its actual addition law.

We also record the torus-subgroup calculation over any field \(E\). If \(M=\mathbf Z^t\) and a finite closed subgroup of \(\operatorname{Spec}E[M]\) has coordinate algebra \(C_0\), the images of the Laurent monomials are group-like and span \(C_0\). Distinct group-like elements are linearly independent by the minimal-dependence and comultiplication argument of FQ6; that proof works over any field. Their images consequently form a finite group \(M/L\), and
\[
 C_0=E[M/L],\qquad
 \ker(E[M]\to C_0)=(\chi^\lambda-1:\lambda\in L).
 \tag{IS4}
\]
Indeed monomials in the same coset have the same image, and images of distinct cosets are independent. The group \(M/L\) is finite because those independent images lie in a finite-dimensional space.

In particular the canonical flat closure of such a generic subgroup in \(\mathcal T\) is \(D_R(M/L)\). Its displayed equations define a finite free quotient \(R[M/L]\), and its generic fibre is the given subgroup, so the saturation uniqueness of FF6 identifies it with the closure. The torus quotient is
\[
 \mathcal T/D_R(M/L)=\operatorname{Spec}R[L],\qquad
 R[M]=\bigoplus_{\gamma\in M/L}R[L]\chi^\gamma .
 \tag{IS5}
\]
PC0 makes \(L\) free of rank \(t\). Comparing the independent basis monomials proves the invariant-ring assertion and the torsor tensor identity, or one may apply the affine proof QS2–QS4. Thus (IS5) is a split torus quotient of finite flat degree \(|M/L|\), not just a quotient of points. \(\square\)

#### 2I.2. Rigidity on reduction

**IS2.** Let \(C\) be finite abelian and \(\mathcal P/R\) a smooth separated commutative group scheme. Reduction is injective on homomorphisms
\[
 \operatorname{Hom}_{R\text{-gp}}(D_R(C),\mathcal P)
    \longrightarrow
 \operatorname{Hom}_{k\text{-gp}}(D_k(C),\mathcal P_k).
 \tag{IS6}
\]

*Proof.* Subtract two homomorphisms, so it suffices to prove that a homomorphism \(u\) reducing to zero is zero. The algebra of a diagonalizable group has no primitive element, over any coefficient ring \(V\). If \(w=\sum_c a_c[e_c]\) satisfies
\(\Delta w=w\otimes1+1\otimes w\), compare the coefficient of \([e_c]\otimes[e_c]\) for \(c\ne0\). It is \(a_c\) on the left and zero on the right, so \(a_c=0\). The coefficient at \(0,0\) then says \(a_0=2a_0\), hence \(a_0=0\), including in characteristic two. The same proof works with coefficients in any module.

Suppose by induction that \(u\) is zero modulo \(\pi^r\), with \(r\ge1\). The ideal \(I=(\pi^r)/(\pi^{r+1})\) is square-zero. The difference of a map to a smooth scheme and its zero-section map, when they agree modulo \(I\), is a derivation along that section. This is the coordinate calculation SF1: differences of products are
\(\delta(fg)=f(e)\delta(g)+g(e)\delta(f)\), since the product of two differences is zero. It is therefore an element of
\[
 \operatorname{Lie}(\mathcal P_k)\otimes_k
       I\otimes_k k[C].
 \tag{IS7}
\]
The tangent map of addition at \((e,e)\) is \((v,w)\mapsto v+w\): its restrictions to either factor are identity by the two unit laws. The homomorphism identity for \(u\) consequently says that every coordinate of (IS7) is primitive in \(k[C]\), with coefficients in \(I\). The preceding comparison makes it zero. This proves the induction step and hence equality to zero modulo every \(\pi^r\).

Finally this formal equality is an actual equality. Choose an affine open of \(\mathcal P\) containing the special identity. Its complement has closed inverse image in the finite \(R\)-scheme \(D_R(C)\). If that closed subset were nonempty, its image under the finite map to \(\operatorname{Spec}R\) would be a nonempty closed subset and would meet the closed point; this contradicts zero reduction. Thus \(u\) and the zero map land in the same affine open. Their coordinate differences lie in every \(\pi^rR[C]\), whose intersection is zero in the finite free module \(R[C]\). They are equal. This proves (IS6). \(\square\)

#### 2I.3. Lifting a multiplicative subgroup of the special fibre

**IS3.** Let \(\mathcal A/R\) be finite locally free and commutative. Every specified closed embedding \(D_k(C)\hookrightarrow\mathcal A_k\) lifts uniquely to a closed embedding \(D_R(C)\hookrightarrow\mathcal A\).

*Proof.* Let \(A\) be the Hopf algebra of \(\mathcal A\), and \(A^\vee\) its dual from IS1. The given embedding is a surjection of finite-dimensional Hopf algebras \(A_k\to k[C]\). Its dual is an injection
\[
 k^C\hookrightarrow A^\vee/\pi A^\vee .
 \tag{IS8}
\]
Let \(\bar e_c\) be the images of its coordinate idempotents. Lift each to an idempotent \(e_c\in A^\vee\). Here is the precise lifting argument. Over a square-zero ideal, if \(x^2-x\) lies in that ideal, \(2x-1\) is a unit since its square is \(1+4(x^2-x)\), and
\[
 x'=x-(2x-1)^{-1}(x^2-x)
 \tag{IS9}
\]
is idempotent. Two lifts differ by a square-zero element \(d\); their idempotent equations give \((2x-1)d=0\), hence equality. Apply this successively modulo \(\pi^r\), and use completeness of the finite free module \(A^\vee\) to obtain unique lifts. Products of distinct lifts and their sum are idempotents lifting zero and one, so the lifts are orthogonal and sum to one. This is also the HS1 lifting argument in Lesson 3, with the complete limit now taken explicitly.

They define an algebra map \(R^C\to A^\vee\). It is a Hopf map. For example, in the complete algebra \(A^\vee\otimes_R A^\vee\), the two elements
\[
 \Delta(e_c),\qquad\sum_{a+b=c}e_a\otimes e_b
 \tag{IS10}
\]
are idempotents lifting the same special idempotent. Uniqueness makes them equal. Counit and antipode compatibility follow in the same way, using the complete rings \(R\) and \(A^\vee\). Thus this map lifts (IS8) as a Hopf map.

We must check the dual map is surjective over \(R\), not just on the generic fibre. Each summand \(e_cA^\vee\) is a direct summand of a finite free \(R\)-module and is free by Lesson 1, §0A. Its unit \(e_c\) has nonzero reduction, by injectivity of (IS8). A vector in a finite free module over the local DVR with nonzero residue has a unit coordinate; projecting to that coordinate and dividing by its value gives an \(R\)-linear functional sending \(e_c\) to one. On these summands the functionals give an \(R\)-linear retraction of \(R^C\to A^\vee\). Dualizing therefore gives a surjection
\[
 A\longrightarrow (R^C)^\vee=R[C].
 \tag{IS11}
\]
It is a Hopf map by IS1, so defines the required closed subgroup. Its special map is the specified one by double-dual evaluation. Any other lift would dualize to another lift of the same orthogonal idempotents, so would be equal. This proves uniqueness as well. \(\square\)

#### 2I.4. The toric intersection is finite flat

**IS4.** In (IS1) the intersection \(\mathcal K=\mathcal H\cap\mathcal T\) is finite locally free and diagonalizable. The image \(\mathcal J\) of \(\mathcal H\to\mathcal B\) is a closed finite locally free subgroup, and
\[
 0\longrightarrow\mathcal K\longrightarrow\mathcal H
       \longrightarrow\mathcal J\longrightarrow0
 \tag{IS12}
\]
is fppf exact, with all three finite locally free group schemes. In particular \(h=h_T h_B\), where \(h_T=\operatorname{rank}\mathcal K\) and \(h_B=\operatorname{rank}\mathcal J\).

*Proof.* Begin with \(K_K=H_K\cap T_K\). By IS1 its flat closure \(\mathcal K_0\subset\mathcal T\) is diagonalizable. It is also a closed subgroup of \(\mathcal H\): pull back the ideal of \(\mathcal H\) to \(\mathcal K_0\); it vanishes generically and therefore vanishes because the latter is \(R\)-flat. This identifies the two canonical closures in the fixed ambient \(\mathcal G[N]\).

Form \(\mathcal G_1=\mathcal G/\mathcal K_0\) by FQ1. The map to \(\mathcal B\) descends. Its kernel is the split torus
\(\mathcal T_1=\mathcal T/\mathcal K_0\) of (IS5), and it is fppf surjective. Indeed a section in the kernel lifts locally to \(\mathcal G\), where its image in \(\mathcal B\) is zero, so the lift is in \(\mathcal T\); two such lifts differ exactly by \(\mathcal K_0\). Thus this is already an actual integral extension of \(\mathcal B\) by \(\mathcal T_1\).

The quotient \(\mathcal H_1=\mathcal H/\mathcal K_0\) is finite locally free by the affine proof QS2–QS4 applied to translation on the affine finite scheme \(\mathcal H\). It embeds as a closed subgroup of \(\mathcal G_1\). To see this without a reduced-point argument, the fppf preimage of this subgroup under \(\mathcal G\to\mathcal G_1\) is exactly \(\mathcal H\), by the quotient relations. That preimage is a closed immersion. FD6 descends that closed immersion along the finite faithfully flat quotient cover. Its generic intersection with \(T_{1,K}\) is trivial by the definition of \(K_K\).

Consider the finite special intersection
\(M=\mathcal H_{1,k}\cap\mathcal T_{1,k}\). As a closed subgroup of a split torus it is \(D_k(C)\) for some finite \(C\), by IS1. IS3 lifts it to a closed subgroup \(D_R(C)\hookrightarrow\mathcal H_1\). Its composite into \(\mathcal B\) is zero on the special fibre. IS2, with \(\mathcal P=\mathcal B\), makes this composite zero over \(R\). Therefore its generic fibre lies in the trivial intersection \(H_{1,K}\cap T_{1,K}\). The closed embedding then forces \(|C|=1\), since \(D_R(C)\) has rank \(|C|\). Thus the special intersection is trivial as a scheme, not merely as a set of points.

The whole finite intersection \(\mathcal H_1\cap\mathcal T_1\) is now trivial. Its finite coordinate module has generic dimension one and special dimension one. FF1's local rank lemma over the domain \(R\) makes it free of rank one; its unit is a basis by Nakayama, so its algebra is \(R\). Hence \(\mathcal H_1\to\mathcal B\) has trivial kernel as a sheaf and is a monomorphism by subtraction. It is finite: the source is finite over \(R\), the target is separated over \(R\), so the graph and proper projection make it proper with finite fibres; the proper finite-fibres theorem of Lesson 3 applies.

This finite monomorphism is a closed immersion by CIE1. Its geometric fibres are empty or a single reduced point: a monomorphism gives at most one point and kills all dual-number tangent vectors, and a finite local algebra with zero cotangent space is its residue field by Nakayama. Let its image be \(\mathcal J\). It is finite locally free, since it is isomorphic to \(\mathcal H_1\). Thus \(\mathcal H\to\mathcal J\) is the already proved finite flat quotient with kernel \(\mathcal K_0\). Its kernel is also the original intersection \(\mathcal H\cap\mathcal T\), as the map to \(\mathcal B\) has that kernel. This proves \(\mathcal K=\mathcal K_0\), (IS12), and the rank product by the finite flat torsor. \(\square\)

#### 2I.5. The full integral quotient sequence

**IS5.** The quotient \(\mathcal Q=\mathcal G/\mathcal H\) has the fppf exact integral sequence and compatible quotient maps
\[
 \begin{array}{ccccccccc}
 0&\longrightarrow&\mathcal T&\longrightarrow&\mathcal G&
   \longrightarrow&\mathcal B&\longrightarrow&0\\
 &&\downarrow q_T&&\downarrow q&&\downarrow q_B\\
 0&\longrightarrow&\mathcal T'&\longrightarrow&\mathcal Q&
   \longrightarrow&\mathcal B'&\longrightarrow&0,
 \end{array}
 \quad
 \mathcal T'=\mathcal T/\mathcal K,\quad
 \mathcal B'=\mathcal B/\mathcal J.
 \tag{IS13}
\]
Here \(\mathcal T'\) is split of rank \(t\), \(\mathcal B'\) is an abelian scheme of dimension \(a\), and the three vertical maps have finite flat degrees \(h_T,h,h_B\). In particular the lower row is a torus torsor over the good abelian quotient.

*Proof.* IS1 constructs the torus quotient and FQ3 constructs the abelian quotient. The map \(\mathcal G\to\mathcal B'\) is invariant under \(\mathcal H\), so FQ1 descends it to \(\mathcal Q\). It is fppf surjective. In the intermediate extension of IS4, the subgroup \(\mathcal H_1\) maps isomorphically onto \(\mathcal J\) and has trivial intersection with \(\mathcal T_1\). A section of the kernel of \(\mathcal Q\to\mathcal B'\) lifts locally to \(\mathcal G_1\); subtract the unique section of \(\mathcal H_1\) over its image in \(\mathcal J\). The result belongs to \(\mathcal T_1\), and no two such torus sections differ by a nonzero element of \(\mathcal H_1\). This gives an isomorphism of the kernel sheaf with \(\mathcal T_1=\mathcal T'\), and hence of the representing schemes. The quotient by the intermediate groups equals \(\mathcal G/\mathcal H\) by the same lift-and-difference argument. This proves (IS13) on all test schemes, with nilpotents retained. The subtraction map then gives the torus-torsor identity. The rank statements are IS4 and the displayed torus and abelian quotients.

In character coordinates, if \(\mathcal T=\operatorname{Spec}R[M]\) and \(\mathcal K=D_R(M/L)\), the pullback on character lattices is the inclusion \(L\hookrightarrow M\) of index \(h_T\). Inverting the rational character matrix shows that the complementary map of FQ2 preserves both rows and has toric and abelian degrees
\[
 \deg d_T=N^t/h_T,\qquad
 \deg d_B=N^{2a}/h_B,\qquad
 \deg d=(N^t/h_T)(N^{2a}/h_B).
 \tag{IS14}
\]
More directly, \([N]\) descends separately through \(q_T,q_B\), giving \(d_T,d_B\); their composites with the maps in (IS13) equal the corresponding composites of \(d\) after \(q\). Faithful descent cancels \(q\). The torus basis (IS5), the abelian FQ2 rank and \(h=h_T h_B\) prove (IS14). All these equations, torsors and degree assertions survive any subsequent base change. \(\square\)

#### 2I.6. Functoriality, actions and valuations

**IS6.** Supplied integral homomorphisms respecting the original torus-by-abelian sequences and subgroups induce homomorphisms of (IS13). Stable finite semilinear actions induce such actions on the entire lower sequence. Over a local field \(K\), the actual quotient maps satisfy
\[
 \nu_{\mathcal Q}(qg)=q_X\,\nu_{\mathcal G}(g),\qquad
 [X_*(T'):q_X X_*(T)]=h_T .
 \tag{IS15}
\]
The valuations use the same base-field normalization on both sides.

*Proof.* A supplied map carries the toric intersection into the target toric intersection, and therefore carries its image \(\mathcal J\) into the target \(\mathcal J'\). Use the invariant-map uniqueness of FQ5 for all three quotients. It proves the commuting squares, identities and composition. A base automorphism is handled by twisting; the same uniqueness proves each finite-action cocycle. No unspecified ambient map is created.

PM2 constructs the valuation quotient for each actual integral torus torsor over an abelian scheme. Its functoriality, proved by evaluation of characters, gives the first equation in (IS15). For the second, PC0 diagonalizes the integral character inclusion \(L\hookrightarrow M\) with invariant factors \(d_i\). Its index is \(\prod_i d_i=h_T\). The dual cocharacter matrix has the same diagonal invariant factors in dual bases, hence the same index. This proves the integral assertion, including residue-divisible degrees. \(\square\)

#### 2I.7. Local-field inverse charts for generic isogenies

**IS7.** A finite étale morphism between smooth varieties over a characteristic-zero local field induces a local homeomorphism on rational points at each rational point. Every point in the target of a surjective finite morphism lifts over some finite field extension.

*Proof.* We give the analytic input for the first assertion. Give a finite-dimensional local-field vector space its maximum norm in a basis. For a convergent power-series map with invertible derivative at a point, translate the point to zero and use that derivative to make its expansion \(f(x)=x+g(x)\), with \(g(0)=0\) and \(dg(0)=0\). On a sufficiently small closed ball, the power-series difference identity for each monomial shows
\[
 \|g(x)-g(y)\|\le c\|x-y\|,\qquad c<1.
 \tag{IS16}
\]
Indeed all terms of degree at least two acquire a ball-radius factor after taking a difference; convergence bounds the remaining coefficients, and shrinking the radius makes their supremum less than one. The same applies to convergent rational functions after shrinking to keep their denominators units.

For each \(z\) in that ball, \(x\mapsto z-g(x)\) preserves the ball and is a contraction. Its iterates are Cauchy since successive differences are bounded by successive powers of \(c\); completeness gives a fixed point. Two fixed points coincide by the same bound. The ultrametric inequality gives \(\|f(x)-f(y)\|=\|x-y\|\) on the ball, so this inverse is continuous. Thus \(f\) is a homeomorphism there.

The polynomial smooth charts SF2–SF3 convert this into the stated scheme assertion. At a rational point choose the defining relations with an invertible Jacobian minor. The map consisting of the free coordinates and those relations has invertible full derivative, so the preceding inverse gives local analytic coordinates on their zero set. For an étale morphism the derivative on these coordinates is invertible, by the zero-relative-dimension version of the same Jacobian criterion. Apply the inverse argument again. In particular a generic finite flat group quotient in characteristic zero is covered: FF5 makes its finite kernel étale; translation gives zero tangent kernel and invertible differential between the equal-dimensional smooth groups, as in FQ4.

For the lifting assertion, a nonempty finite fibre over a rational point has a maximal ideal in its finite-dimensional coordinate algebra. Its residue field is finite over the original field, by its finite vector-space dimension. That field gives a point in the fibre. In characteristic zero take a finite Galois closure as well if desired. This does not assert surjectivity on the original rational points. \(\square\)

#### 2I.8. Transfer of a genuine period presentation through an isogeny

**IS8.** Let \(A/K\) have a local-field period presentation in the precise sense of PC2: the supplied integral extension (IS1), a free lattice \(Y\subset G(K)\), and compatible homomorphisms \(j_E:G(E)\to A(E)\) for every finite \(E/K\), with kernel \(Y\), the stated local homeomorphism at the identity and finite-extension point-lifting property. Let \(f:A\to A'\) be any isogeny, of degree \(n\). After a finite extension of \(K\), there is such a period presentation of \(A'\), with an actual integral semiabelian extension of the same torus and abelian dimensions. The quotient maps and period injections are compatible. Supplied finite semilinear actions for which \(f\) is equivariant are preserved. The degree decomposes as
\[
 n=|Z|\,[Y_{\mathrm{new}}:qY],
 \tag{IS17}
\]
where \(Z\subset G[n]\) is the finite generic torus-and-abelian covering kernel defined below. It need not be the whole kernel of \(f\).

*Proof.* PC2–PC3 already show that the original lattice is finitely generated, free of rank \(t\), and that every original point map is surjective. Work first in a fixed algebraic closure, using the compatible union of the maps \(j_E\). The finite-extension lifting property also directly makes \(j:G(\bar K)\to A(\bar K)\) surjective. Put
\[
 H=\ker f,\qquad
 \widetilde Y=j^{-1}(H(\bar K)),\qquad
 Z=\operatorname{Tor}(\widetilde Y).
 \tag{IS18}
\]
Since \(H\) is finite étale of rank \(n\) in characteristic zero, this gives an exact sequence of abelian groups
\[
 0\longrightarrow Y\longrightarrow\widetilde Y
     \xrightarrow{j}H(\bar K)\longrightarrow0,\qquad
 Z=\widetilde Y\cap G[n](\bar K).
 \tag{IS19}
\]
For the last equality, \(n\widetilde Y\subset Y\), because \(H\) is killed by \(n\). If \(z\) is torsion, \(nz\in Y\) is torsion and hence zero. Conversely an element in the displayed intersection is torsion. The finite group \(Z\) injects into \(H(\bar K)\), since the torsion-free \(Y\) meets it trivially. The group \(\widetilde Y\) is finitely generated: lift the finitely many elements of \(H(\bar K)\) and add a finite basis of \(Y\). PC0 and Smith reduction therefore show
\[
 \widetilde Y/Z\text{ is free of rank }\operatorname{rank}Y,\qquad
 [\widetilde Y/Z:Y]=n/|Z|.
 \tag{IS20}
\]
The rank follows equally by tensoring (IS19) with \(\mathbf Q\). No assertion that \(\widetilde Y\) was torsion-free has been made.

The subgroup \(Z\) is a finite closed subgroup scheme of \(G_K[n]\). Its geometric point subset is Galois stable by (IS18). After a finite Galois splitting field the ambient finite étale scheme is a disjoint union of rational points, and the subset is a closed subscheme. Descent of its ideal by FD3, or the finite Galois algebra decomposition of Lesson 1, constructs it over \(K\). Its group identities hold on that finite étale scheme because they hold on the points.

Take its FF6 flat closure \(\mathcal Z\subset\mathcal G[n]\) and apply IS5 to construct
\[
 q:\mathcal G\longrightarrow\mathcal G_{\mathrm{new}}
       =\mathcal G/\mathcal Z,\qquad
 0\longrightarrow\mathcal T_{\mathrm{new}}
   \longrightarrow\mathcal G_{\mathrm{new}}
   \longrightarrow\mathcal B_{\mathrm{new}}\longrightarrow0.
 \tag{IS21}
\]
This is an actual split torus torsor over a good abelian scheme, of the same dimensions as the input. Put \(Y_{\mathrm{new}}=q(\widetilde Y)\). The kernel of \(q\) on geometric points is \(Z\), so (IS20) identifies this with an embedded free lattice. Choose a finite extension \(K_1/K\) containing the coordinates of the finitely many chosen generators of \(\widetilde Y\), enlarging to a Galois extension when finite actions are being retained. The new lattice then lies in \(G_{\mathrm{new}}(K_1)\). The index in (IS20) proves (IS17).

Here is the map on every finite \(E/K_1\); its existence does not assume surjectivity of \(q:G(E)\to G_{\mathrm{new}}(E)\). Given \(x\in G_{\mathrm{new}}(E)\), lift it to \(g\in G(E')\) for a finite Galois extension \(E'/E\), using IS7. Define
\[
 j^{\mathrm{new}}_E(x)=f(j_{E'}(g)).
 \tag{IS22}
\]
For \(\sigma\in\operatorname{Gal}(E'/E)\), the difference \(\sigma g-g\) is in \(Z(E')\), and \(j(Z)\subset H\). Thus the right side is Galois fixed and is an \(E\)-point of \(A'\), by finite Galois descent for scheme points. Any two lifts differ by \(Z\) after a common finite extension, proving independence. Taking lifts of two points proves additivity. The same argument proves compatibility with every extension and field embedding, and
\[
 j^{\mathrm{new}}_E(qg)=f(j_Eg)
 \quad\text{whenever }g\in G(E).
 \tag{IS23}
\]
Its kernel is exactly \(Y_{\mathrm{new}}\): lift a kernel element as above; its image under \(j\) lies in \(H\), so the lift belongs to \(\widetilde Y\). Conversely every such lift maps to zero. All those new period points already lie in \(G_{\mathrm{new}}(K_1)\).

Near the identity over \(E\), both generic isogenies \(q\) and \(f\) have inverse local charts by IS7. On that neighbourhood the new map is the composition \(f\circ j_E\circ q^{-1}\) by (IS22), so it is continuous and a local homeomorphism. Translation gives continuity everywhere. To lift any \(a'\in A'(E)\), first lift along \(f\) after a finite field extension by IS7, then use the given finite-extension lifting property for \(j\), and apply \(q\). This proves the required finite-extension lifting property for the new maps. They therefore satisfy every hypothesis of PC2. Its proved finite-Galois cocycle argument then gives surjectivity on every \(G_{\mathrm{new}}(E)\to A'(E)\), since the new kernel is a constant torsion-free lattice. PC1–PC6 give its closed discrete kernel, full period rank, nondegenerate valuation and all actual torsion levels and transitions.

Finally any supplied compatible finite semilinear action stabilizes \(H,\widetilde Y,Z\). FF6 and IS6 descend the integral action through (IS21), and uniqueness of (IS22) proves equivariance of the new point maps. A finite Galois extension containing the chosen generators keeps the lattice action finite. This proves the claimed compatibility.

The construction proves transfer of the exact local-field presentations used in PC2, with local analytic inverse charts when the input has them. It has not assumed a global rigid-analytic descent theorem to replace this point-map construction, nor constructed the initial presentation for an arbitrary abelian variety. Those initial semistable geometric and covering constructions, and any separately claimed dual-model pairing, remain part of the full theorem. \(\square\)

#### 2I.9. Graded exercise: integral intersections and transferred periods

**Exercise 2I (100 points; ten parts of 10 points each).** Use IS1–IS8 and the actual earlier proofs indicated. Retain the scheme algebras and all nilpotents.

**(a) Finite Cartier duality.** For \(C=\mathbf Z/4\mathbf Z\oplus\mathbf Z/2\mathbf Z\), write the Hopf algebra of \(D_R(C)\), its dual idempotents and their coproducts. Verify the double-dual evaluation on bases. What are the ranks, and in residue characteristic two how many geometric points does \(D_k(C)\) have?

**(b) Primitive coordinates and the dual distinction.** Prove directly in characteristic \(p\) that \(k[\mathbf Z/p\mathbf Z]\) has no nonzero primitive element. Compare it with the primitive coordinate of \(\alpha_p\) and the primitive generator in the Cartier dual algebra of \(\mu_p\) calculated in Exercise 2G. Explain why neither is a counterexample.

**(c) An idempotent lift without division by two.** Suppose \(I^2=0\) and \(x^2-x\in I\) in a commutative ring. Prove (IS9), its uniqueness and the invertibility needed in that formula. Apply the formula over \(\mathbf Z/4\mathbf Z\) to \(x=2\) and \(x=3\). Explain how complete finite free algebras allow all the successive lifts to be taken.

**(d) Why the multiplicative hypothesis matters.** Over \(R=\mathbf Z_p[\zeta_p]\), consider \((\mathbf Z/p\mathbf Z)_R\to\mu_{p,R}\), \(i\mapsto\zeta_p^i\). Prove that it is nonzero generically but zero on the special fibre as a scheme map. Why does it not contradict IS2? Include \(p=2\).

**(e) A full integral quotient diagram.** Let \(\mathcal B/R\) be a good elliptic scheme and \(\mathcal G=\mathbf G_m^2\times\mathcal B\). Embed
\(\mathcal K=\mu_6\) in the torus by \(z\mapsto(z,z^2)\), and put
\(\mathcal H=\mathcal K\times\mathcal B[3]\).
Use \(N=12\). Give both rows of (IS13) and all three quotient degrees. Compute all three complementary degrees, and explicit complementary torus coordinates. The residue characteristic may be two or three.

**(f) Excluding an extra special intersection.** Suppose \(\mathcal H_1\) is a finite flat subgroup of an actual integral extension by a split torus, and its generic intersection with that torus is trivial. Reproduce the argument showing that its special intersection is the trivial scheme. Explain precisely where completeness, finite freeness, smoothness and the full subgroup scheme enter.

**(g) A generic inverse despite bad special reduction.** Prove that squaring gives a homeomorphism
\(1+4\mathbf Z_2\to1+8\mathbf Z_2\).
Relate this to the finite map \([2]:\mathbf G_{m,\mathbf Z_2}\to\mathbf G_{m,\mathbf Z_2}\). Why can the generic local-field inverse exist when that integral map is not étale?

**(h) Two different contributions to the degree.** Use the actual Tate curve \(A=E_{p^6}\) over a finite extension of \(\mathbf Q_p\), with its proved Tate presentation. First quotient by the subgroup represented by \(\mu_3\); then, separately, quotient by the subgroup represented by \(p^{2\mathbf Z}/p^{6\mathbf Z}\). For each algebraic elliptic quotient, compute \(n,Z,\widetilde Y\), the new torus quotient, the new period lattice and (IS17). These are quotient constructions; no unexplained identification of two elliptic curves from point-set bijections is permitted.

**(i) Both contributions at once.** Enlarge the field to contain \(\mu_4\), and let \(H\subset E_{p^6}\) be generated by the images of \(\mu_4\) and \(p^2\). Construct the algebraic quotient \(A'=E_{p^6}/H\) using Lesson 3. Determine the degree, the torsion subgroup \(Z\), the new cover, the period index and the normalized valuation relation. Explain which point maps to \(A'\) are actually constructed by IS8.

**(j) Rational lifts, actions and the remaining theorem.** In (IS22), explain why a finite Galois extension may be needed to lift a rational point, why the output nevertheless belongs to the original field, and why its kernel is a constant torsion-free lattice after one fixed finite extension. State the precise condition needed to preserve a supplied finite semilinear action. Identify the initial geometric construction still required for Theorem 2.4.

**Full solution.**

**(a)** With coordinates \(u,v\) for the two generators, the algebra and full free basis are
\[
 R[C]=R[u,v]/(u^4-1,v^2-1),\qquad
 \{u^iv^j:0\le i<4,\ 0\le j<2\}.
 \tag{ISX1}
\]
The coordinates are automatically units. Each basis element is group-like; its counit is one and its antipode is \(u^{-i}v^{-j}\). The dual basis \(\delta_{i,j}\) consists of eight pairwise orthogonal idempotents summing to one, and
\[
 \Delta\delta_{i,j}=
   \sum_{\substack{a+b=i\ (4)\\c+d=j\ (2)}}
      \delta_{a,c}\otimes\delta_{b,d}.
 \tag{ISX2}
\]
Evaluation sends \(u^iv^j\) to the functional on the dual basis taking value one at \(\delta_{i,j}\) and zero at the others. This is the inverse of the double-dual basis identification; (ISX2) and the pointwise dual products verify both Hopf operations. All ranks are eight. In characteristic two, \(u^4-1=(u-1)^4\), \(v^2-1=(v-1)^2\), so there is one geometric point and an algebra of length eight. The dual is the constant eight-point scheme; its rank is the same, although its number of points differs.

**(b)** Write \(w=\sum_{i=0}^{p-1}a_i z^i\), with \(z^p=1\). In the basis \(z^i\otimes z^j\), a primitive equality has coefficient \(a_i\) at \((i,i)\) on the left and zero on the right for \(i\ne0\). Hence those coefficients vanish. At \((0,0)\) it gives \(a_0=2a_0\), so \(a_0=0\), even for \(p=2\).

By contrast the algebra of \(\alpha_p\) has \(\Delta u=u\otimes1+1\otimes u\), so \(u\) is a nonzero primitive element. Its relation \(u^p=0\) and its coproduct differ from the group-like monomial basis of \(\mu_p\). The primitive \(D\) of the dual of \(\mu_p\) has \(D^p=D\), as proved in Exercise 2G; it lies in the dual algebra \(k^{\mathbf Z/p\mathbf Z}\), rather than the original group algebra. These are distinct Hopf algebras in characteristic \(p\).

**(c)** Put \(a=x^2-x\in I\). The identity
\((2x-1)^2=1+4a\) makes \(2x-1\) invertible, because \(a^2=0\) gives \((1+4a)^{-1}=1-4a\). Let \(d=-(2x-1)^{-1}a\). Then \(d^2=0\), and
\[
 (x+d)^2-(x+d)
   =a+(2x-1)d+d^2=0.
 \tag{ISX3}
\]
If two idempotents lifting the same residue differ by \(d\in I\), their equations give \((2e-1)d+d^2=0\). For the idempotent \(e\), \((2e-1)^2=1\), so \(d=0\).

In \(\mathbf Z/4\mathbf Z\), \(x=2\) has \(a=2\), \(2x-1=3\), and the lift is \(2-3\cdot2=0\). For \(x=3\), \(a=2\), \(2x-1=1\), and the lift is \(3-2=1\). No division by two occurs. Applying the formula between successive \(\pi\)-power quotients gives unique compatible idempotents; completeness of a finite free algebra identifies it with the inverse limit of those quotients. Multiplication and the Hopf maps are continuous module maps, so the identities pass to that limit.

**(d)** On algebras the map sends \(z\) to the tuple \((\zeta_p^i)_{i\in\mathbf Z/p\mathbf Z}\) in \(R^p\). Generically these are all distinct roots and the evaluation map is an isomorphism by the Vandermonde calculation FF7. In the residue field every \(\zeta_p^i\) is one, so the entire algebra map is
\[
 k[z]/(z^p-1)\longrightarrow k^p,\qquad
 z\longmapsto(1,\ldots,1).
 \tag{ISX4}
\]
It factors through evaluation at the identity, proving zero reduction as a scheme map, including the nilpotent coordinate \(z-1\). The source group of the original morphism is the constant group, whose special fibre has \(p\) reduced points. It is not \(D_R(\mathbf Z/p\mathbf Z)\), whose special fibre is nonreduced with one point. Thus the diagonalizable-source hypothesis of IS2 fails. For \(p=2\), \(\zeta_2=-1\), the two values \(1,-1\) are distinct generically and coincide modulo two, giving exactly the same example.

**(e)** On torus coordinates set \(U=x^6,\ V=y/x^2\). The invariant character lattice is generated by \((6,0),(-2,1)\), so the lower torus is again \(\mathbf G_m^2\). The abelian quotient by \(\mathcal B[3]\) is \(\mathcal B\), with quotient map \([3]\), by FF2 and its kernel-torsor identity. Consequently one can write
\[
 q(x,y,b)=(x^6,y/x^2,[3]b),\qquad
 h_T=6,\quad h_B=9,\quad h=54.
 \tag{ISX5}
\]
The lower row is the product extension \(\mathbf G_m^2\times\mathcal B\), with its displayed maps. For \(N=12\), the complementary torus map is
\[
 d_T(U,V)=(U^2,U^4V^{12}),\qquad d_B=[4].
 \tag{ISX6}
\]
Substitution with \(q_T\) in either order gives multiplication by twelve. Its exponent matrix has determinant \(24\), so its degree is \(24\); \(d_B\) has degree \(16\) by CU8 or FF2. Thus
\[
 \deg[12]_{\mathcal G}=12^4=20736,\qquad
 \deg d_T=24,\quad\deg d_B=16,\quad\deg d=384,
 \quad54\cdot384=20736.
 \tag{ISX7}
\]
These ranks and coordinate algebras remain valid in residue characteristics two and three. The kernels can be nonétale; no inverse of six or three was used.

**(f)** The special intersection is a finite closed subgroup of a split torus, so IS1 identifies it with \(D_k(C)\), with its full algebra rather than only its points. IS3 lifts the embedding into \(\mathcal H_1\) to \(D_R(C)\). Completeness and finite freeness enter when lifting all the dual idempotents and their tensor identities; the split module retraction makes the lifted dual map an actual closed immersion. Its composite into the good abelian quotient has zero reduction. IS2 uses the smooth identity tangent module, primitive-coordinate vanishing, and the complete separated finite source algebra to make that composite zero over \(R\). Thus its generic fibre lies in the trivial generic intersection. A closed immersion of a rank-\(|C|\) finite flat group into the trivial generic group forces \(|C|=1\). Hence the special intersection is the trivial scheme. Comparing only geometric points would miss, for example, a possible \(\mu_p\) special kernel, which has one point but rank \(p\).

**(g)** Write \(x=1+4u\). Then
\[
 x^2=1+8(u+2u^2).
 \tag{ISX8}
\]
For \(w\in\mathbf Z_2\), the equation \(u+2u^2=w\) is the fixed-point equation \(u=w-2u^2\). This map preserves \(\mathbf Z_2\), and
\[
 |2u^2-2v^2|_2
   =|2(u-v)(u+v)|_2\le\tfrac12|u-v|_2.
 \tag{ISX9}
\]
Its iterates converge to a unique solution; the same estimate shows that \(u\mapsto u+2u^2\) is an isometry and its inverse continuous. This proves the claimed homeomorphism. The integral map has special kernel \(\mu_{2,\mathbf F_2}\), hence is not étale over \(\mathbf Z_2\). On the generic field its derivative \(2x\) is nonzero and therefore invertible as a field scalar. IS7 permits shrinking both neighbourhoods to account for that scalar; an integral unit derivative is unnecessary for this generic inverse.

**(h)** Let \(Y=p^{6\mathbf Z}\) inside \(\bar K^\times\). The Tate presentation identifies its quotient with the actual points of \(A\), over all finite extensions. The image of \(\mu_3\) is a finite subgroup of order three: a root of unity cannot be a nonidentity period, by valuation. Its finite étale subgroup scheme is defined after a finite splitting extension if necessary, and Lesson 3, QS1–QS8 constructs the algebraic elliptic quotient \(A_1\). For its isogeny \(f_1\),
\[
 n=3,\quad
 \widetilde Y=\mu_3\,p^{6\mathbf Z},\quad
 Z=\mu_3,\quad
 q_T(x)=x^3,\quad
 Y_{\mathrm{new}}=p^{18\mathbf Z},\quad
 [Y_{\mathrm{new}}:q_TY]=1.
 \tag{ISX10}
\]
The equality for the preimage follows because two lifts of the same \(A\)-point differ by an old period. The factorization (IS17) is \(3=3\cdot1\).

For the second subgroup, the class of \(p^2\) has order three, since its cube is \(p^6\) and its smaller positive powers are not periods. It gives another finite subgroup and algebraic elliptic quotient \(A_2\), with
\[
 n=3,\quad
 \widetilde Y=p^{2\mathbf Z},\quad
 Z=0,\quad
 q_T=\mathrm{id},\quad
 Y_{\mathrm{new}}=p^{2\mathbf Z},\quad
 [Y_{\mathrm{new}}:Y]=3.
 \tag{ISX11}
\]
There is no torsion in this preimage because valuation is injective on \(p^{2\mathbf Z}\). Now (IS17) is \(3=1\cdot3\). In both cases IS8 constructs actual compatible maps from the new torus points to the indicated algebraic quotient. An algebraic identification of those quotients with other named Tate curves is not needed or inferred from a point-set bijection.

**(i)** The root-of-unity subgroup injects with order four, and the class of \(p^2\) has order three. Their intersections in \(A\) are trivial: a relation \(\zeta p^{2r}\in p^{6\mathbf Z}\) first gives \(r\equiv0\pmod3\) by valuation and then \(\zeta=1\). Thus the subgroup has order twelve, is finite étale in characteristic zero, and gives the actual algebraic quotient by QS1–QS8. Its data are
\[
 n=12,\quad
 \widetilde Y=\mu_4\,p^{2\mathbf Z},\quad
 Z=\mu_4,\quad
 q_T(x)=x^4,\quad
 Y_{\mathrm{new}}=p^{8\mathbf Z},\quad
 q_TY=p^{24\mathbf Z}.
 \tag{ISX12}
\]
The period index is three and \(12=4\cdot3\). If \(v\) is the valuation of the common finite base field, then
\(v(q_Tx)=4v(x)\); in particular the old generator of valuation \(6v(p)\) maps to valuation \(24v(p)\), which is three times the new period generator's valuation \(8v(p)\). The cocharacter index is four, agreeing with IS15.

For every finite extension of the fixed field, IS22 defines a map to the algebraic \(A'\) by lifting through the fourth-power quotient after a finite Galois extension and then applying the quotient isogeny to the original Tate point. The independence and descent proof makes this an actual point of \(A'\) over the original field. The new torus cover and its period subgroup have therefore been constructed for that algebraic quotient, with no asserted global rigid descent or unexplained algebraic curve identification.

**(j)** A finite étale fibre over a rational point can be a finite separable field extension rather than a product with an original-field factor; for instance a unit need not have the required root in the original field. IS7 gives a lift over a finite extension and one may take a finite Galois closure. Differences of its conjugates belong to \(Z\); applying \(j\) puts those differences in \(H=\ker f\). Hence \(f(j(g))\) is fixed by the finite Galois group and descends as a scheme point. A common further extension compares any two choices.

The group \(\widetilde Y\) has finitely many cosets over the original finite-rank \(Y\), so finitely many algebraic generators. One fixed finite extension contains their coordinates. Its torsion is exactly \(Z\), killed by \(n\), and PC0 makes \(\widetilde Y/Z\) free. The quotient map embeds it as the new period lattice over that fixed field. Thus it is constant for every later finite extension. The maps retain a supplied finite semilinear action precisely when the input period maps are equivariant and the isogeny \(f\) is equivariant for the specified actions on its source and target. Under that condition \(H,\widetilde Y,Z\) are stable, and the unique quotient maps and (IS22) are equivariant.

The initial integral semiabelian extension and actual period presentation after finite extension for an arbitrary abelian variety remain to be constructed. IS4–IS5 supplies the full integral quotient sequence, and IS8 supplies transfer of an already genuine presentation through every isogeny; neither asserts that an initial presentation has appeared without that geometric construction. Any separately claimed dual-model pairing and the other global arithmetic and full-course proof and review obligations also remain separate.

### 2J. Divisor parameter schemes for the geometric construction

The Jacobian construction requires a parameter scheme for divisors, including divisors with repeated points. We construct it here without assuming a Hilbert scheme or a Picard scheme exists. Let \(C/k\) be a smooth projective geometrically integral curve over any field, and let \(n\ge0\). On a \(k\)-scheme \(T\), consider closed subschemes
\[
 D\hookrightarrow C_T=C\times_kT,\qquad
 D\longrightarrow T\text{ finite locally free of rank }n.
 \tag{DR1}
\]
Isomorphisms here preserve the closed embedding, so the objects are ideals, rather than arbitrary finite schemes. We will represent this functor by a smooth proper geometrically integral scheme \(S_n(C)\) of dimension \(n\). Every universal family is a relative effective Cartier divisor, with arbitrary base changes retained.

The free primary comparisons are Milne's author version of [*Jacobian Varieties*, §3](https://www.jmilne.org/math/xnotes/JVs.pdf), and the Stacks project's [Hilbert schemes of points](https://stacks.math.columbia.edu/tag/0B94) and [divisors on smooth curves](https://stacks.math.columbia.edu/tag/0B9C). The matrix charts, completion arguments, collisions and nonreduced families used below have their proofs here. The Picard scheme and the initial period cover are not being admitted as prerequisites.

#### 2J.1. The completion facts used by the construction

**DR1.** For a Noetherian ring \(A\), an ideal \(I\) and a finite \(A\)-module \(M\), completion is exact on short exact sequences of finite modules, and
\[
 \widehat M^{\,I}=\widehat A^{\,I}\otimes_A M.
 \tag{DR2}
\]
The completed ring is flat over \(A\). For a local \(A\) and \(I\) contained in its maximal ideal, this map is faithfully flat.

*Proof.* For \(N\subset M\), the actual Artin–Rees proof CS2 of Lesson 3, §0.C.4.2 gives
\[
 I^rM\cap N=I^{r-c}(I^cM\cap N)\quad(r\ge c).
 \tag{DR3}
\]
Thus the induced filtration on \(N\) and its own ideal-power filtration are cofinal. The exact sequences
\[
 0\to N/(N\cap I^rM)\to M/I^rM
       \to (M/N)/I^r(M/N)\to0
 \tag{DR4}
\]
have surjective transition maps on their left terms. Their inverse limit is exact: for a compatible element on the right, lift at the first level, lift at the next level, and correct the difference with a lift from the left term; surjectivity permits that correction at each step. This inductively produces a compatible lift. Left exactness follows directly by testing every coordinate. Cofinality identifies the left inverse limit with \(\widehat N^{\,I}\), proving exactness.

Complete a finite presentation \(A^a\to A^b\to M\to0\). Exactness just proved identifies its completed cokernel with the cokernel after tensoring with \(\widehat A^{\,I}\), giving (DR2). If \(N\subset A^b\) is any finite submodule, completion exactness and (DR2) show that tensoring with \(\widehat A^{\,I}\) preserves this inclusion. These tests give flatness: a relation in a tensor product uses finitely many coefficients and relations, hence occurs in a presentation by a finite free module and its finite kernel; preservation of these inclusions is the finite-relations tensor criterion proved in Lesson 3, T1. Noetherianity supplies that finite kernel.

In the local case, apply (DR2) to the residue field to obtain
\(\widehat A^{\,I}/\mathfrak m\widehat A^{\,I}=A/\mathfrak m\).
For any nonzero module, choose a nonzero cyclic submodule \(A/J\). Its extension remains nonzero because \(J\subset\mathfrak m\) and the quotient still maps onto that residue field. Flatness preserves its inclusion in the original module. This proves faithful flatness. In particular completion detects equality and vanishing of finite modules; DFR3 also gives the explicit injectivity into completion in the local ideal-adic situation. \(\square\)

#### 2J.2. The ordered-root algebra, over every coefficient ring

**DR2.** For any ring \(R\), the elementary-symmetric map makes \(R[x_1,\ldots,x_n]\) finite free of rank \(n!\) over \(R[e_1,\ldots,e_n]\), with basis
\[
 x_1^{a_1}\cdots x_n^{a_n},
 \qquad 0\le a_i<n-i+1.
 \tag{DR5}
\]
In particular the elementary symmetric functions are algebraically independent over \(R\), and the full algebra
\[
 R[x_1,\ldots,x_n]/(e_1,\ldots,e_n)
 \tag{DR6}
\]
is free of rank \(n!\) over \(R\), including in residue characteristics dividing \(n!\).

*Proof.* Start with the independent coefficient ring \(B_0=R[E_1,\ldots,E_n]\) and the monic polynomial
\[
 P_0(T)=T^n-E_1T^{n-1}+\cdots+(-1)^nE_n.
 \tag{DR7}
\]
Adjoin a root \(x_1\), taking \(B_1=B_0[x_1]/(P_0(x_1))\). Monic division proves it is free of rank \(n\), with the first-variable powers in (DR5). In this ring divide \(P_0(T)\) by \(T-x_1\). Its remainder is zero, so the quotient \(P_1(T)\) is monic of degree \(n-1\). Adjoin \(x_2\) as a root of \(P_1\), and continue. The successive ranks are \(n,n-1,\ldots,1\), giving the displayed basis.

The final ring satisfies \(P_0(T)=\prod_i(T-x_i)\), so every \(E_i\) is the corresponding elementary symmetric function of the roots. It is therefore generated by the \(x_i\) over \(R\). Conversely substituting those elementary symmetric functions into the coefficients and using the same ordered roots satisfies every monic root relation, giving a map back to \(R[x_1,\ldots,x_n]\). The two maps fix the roots and all coefficients, so are inverse. This proves the freeness assertion. The coefficient-ring map is injective because its final free extension has positive rank and contains its coefficient unit as a basis element. Base change \(E_i\mapsto0\) proves (DR6). The case \(n=0\) has the empty basis monomial and rank \(0!=1\). \(\square\)

#### 2J.3. Explicit affine charts for finite quotients

**DR3.** If \(V=\operatorname{Spec}A\) is affine of finite type over \(k\), its rank-\(n\) closed finite locally free quotient functor is represented by a finite-type scheme \(H_n(V)\). Its charts are explicit polynomial matrix schemes and work over every parameter ring.

*Proof.* Present \(A=k[z_1,\ldots,z_s]/(f_1,\ldots,f_r)\), using Noetherianity for the finite relation list. Let \(B\) be a set of \(n\) monomials, containing \(1\), closed under taking divisors. Use these as names for a basis of a rank-\(n\) module, with basis vectors \(v_b\). For \(n>0\), introduce \(s\) square matrices \(M_i\) of size \(n\) and impose the finite polynomial equations
\[
 M_iM_j=M_jM_i,\qquad
 f_\alpha(M_1,\ldots,M_s)=0,\qquad
 b(M_1,\ldots,M_s)v_1=v_b\quad(b\in B).
 \tag{DR8}
\]
They define an affine scheme over \(k\).

Over any ring \(R\), these equations make \(R^n\) a cyclic \(A_R\)-module generated by \(v_1\). The map \(A_R\to R^n\), \(a\mapsto a(M)v_1\), is surjective by the last equations. Its kernel is an ideal: if \(a(M)v_1=0\), then for every \(b\), commutation gives \(a(M)b(M)v_1=b(M)a(M)v_1=0\), and those vectors span. Multiplication of two vectors may therefore be defined by multiplying their polynomial representatives; this is independent of the representatives, associative, commutative and has unit \(v_1\). It gives a finite free quotient algebra of \(A_R\). Conversely such a quotient with the named monomial basis gives its unique multiplication matrices and satisfies (DR8). These constructions are inverse and commute with base change.

There are enough such charts, with only finitely many \(B\) required for fixed \(s,n\). In a finite-dimensional residue quotient, order monomials by degree and then lexicographically, and retain a monomial precisely when it adds a vector to the span of earlier ones. The retained monomials form a basis. They are closed under divisors: if a divisor were an earlier dependent monomial, multiply its relation by the complementary monomial. Multiplicativity of the order would make the original monomial dependent as well. Every monomial in this basis has degree at most \(n-1\), since all monomials on a chain of its divisors are retained. Thus only finitely many choices occur. In a family, the locus where any named list is a basis is open, by the determinant of its map to the finite locally free quotient. These opens cover.

On an overlap with another basis \(B'\), let \(S\) have columns \(b'(M)v_1\). Invert \(\det S\) and replace
\[
 M_i\longmapsto S^{-1}M_iS.
 \tag{DR9}
\]
The first column preserves the unit, since both lists start with \(1\). Formula (DR9) gives inverse change-of-basis morphisms. Their cocycles are matrix multiplication. The charts therefore glue and represent the affine functor. No choice of a module trivialization remains: the basis consists of the specified images of the monomials. For \(n=0\), the empty quotient is represented by \(\operatorname{Spec}k\). \(\square\)

#### 2J.4. Global gluing, separatedness and the full Cartier ideal

**DR4.** The functor (DR1) is represented by a separated finite-type scheme \(S_n(C)\). Its universal closed subscheme is a relative effective Cartier divisor. These assertions, including representation on nonreduced parameter schemes, commute with every field extension and every later change of the parameter base.

*Proof.* First choose finitely many affine opens of \(C\) such that every geometric subset of at most \(n\) points lies in one of them. Embed \(C\) in projective space. Construct \(n+1\) positive-degree hypersurface divisors on it with pairwise disjoint supports: at each step choose a homogeneous polynomial avoiding the finite support of all previous divisors. The finite homogeneous-prime avoidance proof QS1 works over finite fields as well. The polynomial is nonzero on the integral curve, and its vanishing is a finite effective divisor. Its projective standard-open complement is affine. A set of at most \(n\) geometric points cannot meet all \(n+1\) disjoint supports, giving the required cover.

In a family \(D/T\), the condition that \(D\) lies in a selected affine \(V\) is open in \(T\): the intersection with \(C_T\setminus V_T\) is closed in the finite \(D\), hence has closed image in \(T\). On the complementary open the family is exactly an object of DR3. The quotients over \(V\cap W\) give the common open subfunctor of the two affine constructions. The intersection is affine since \(C\) is separated; its affine construction is DR3 again. The open identifications are unique on ideals and satisfy the cocycle. They glue to \(S_n(C)\) with its universal family. The finite cover of \(C\) just constructed and DR3's finite chart lists show finite type. This gluing represents the functor over all parameter schemes, since basis choices and containment in affine opens are local statements and ideals glue.

We verify separatedness with equations on an arbitrary parameter base. Given two families \(D_1,D_2\), the condition \(D_1\subset D_2\) is closed: locally choose an affine open of \(C\) containing both fibre supports, possible using the same construction with \(2n\) in place of \(n\), and shrink the parameter base so both families remain inside it. On affine basis charts the ideal of \(D_2\) is generated by a finite list: the universal chart rings are Noetherian, and their ideal lists pull back to every parameter ring. Evaluate these generators in the finite free algebra of \(D_1\). The finitely many coefficients are zero exactly on a closed subscheme of the parameter base. This represents containment, after arbitrary further base change. Containment gives a surjection of two finite locally free algebras of equal rank \(n\), hence an isomorphism: locally its square matrix has invertible residue determinant, and therefore invertible determinant. Thus containment is equality. The same construction represents the diagonal by closed immersions. This proves separatedness without replacing equality by equality of geometric fibres.

Now work over the Noetherian universal parameter scheme. Locally on a parameter base and the curve, let \(P\) be the curve algebra and \(Q=P/J\) the finite flat quotient. Both \(P\) and \(Q\) are flat over that base, and their kernel \(J\) is flat as well: tensoring a short exact sequence with any module and using flatness of the first two terms proves the tensor injection for this kernel. On a geometric fibre the ideal of a finite subscheme in a smooth curve is generated by a nonzero divisor, since the curve local ring is a DVR by SF5–SF6.

Lift that generator to \(f\in J\) at a selected point. Flatness of \(Q\) identifies the fibre of \(J\) with the actual fibre ideal, by tensoring \(0\to J\to P\to Q\to0\). Nakayama therefore gives \(J=fP\) locally. The finite kernel of \(P\to J\), \(a\mapsto fa\), remains injective on the fibre because \(J\) is flat over the base. There it is zero, since \(f\) is a nonzero divisor. Nakayama kills that kernel. Thus \(J\) is an invertible ideal generated by a nonzero divisor. These local conclusions spread to neighbourhoods by finite kernel and cokernel witnesses. They prove the universal family is Cartier. For a non-Noetherian parameter change, tensoring the universal sequence preserves its injection because its quotient is flat; the ideal remains invertible. This proves the full arbitrary-base assertion. \(\square\)

#### 2J.5. Smoothness and the actual deformation space

**DR5.** The scheme \(S_n(C)\) is smooth of dimension \(n\) over \(k\). At a geometric divisor \(D\) its tangent space is
\[
 T_D S_n(C)=
    \operatorname{Hom}_{\mathcal O_C}(\mathcal I_D,\mathcal O_D)
    =H^0(D,\mathcal O_D(D)),
 \qquad \dim T_D S_n(C)=n .
 \tag{DR10}
\]

*Proof.* We may first extend to an algebraically closed field, since the chart equations and universal property in DR3–DR4 commute with that change. Consider a divisor over a local Artinian algebra \(B\), and a surjection \(B'\to B\) of local Artinian algebras with the same residue field. The support of the divisor is finite. On a suitable affine open \(V\) of the curve containing that support, its Cartier ideal has one generator. To justify the choice, choose a generator in each of the finitely many residue fibres of that invertible ideal and lift them simultaneously by Chinese remaindering. The resulting section generates near all support points. A principal open containing that finite support and inside the generation locus exists by finite prime avoidance, as in QS1. Replace \(V\) by it.

Write the generator as \(f\in\mathcal O(V)\otimes_kB\), and lift it arbitrarily to \(f'\in\mathcal O(V)\otimes_kB'\). Its special reduction is a nonzero divisor on the integral affine curve. For every \(B'\)-module \(N\), the finite filtration by powers of its maximal ideal has associated graded terms that are vector spaces over the residue field. On each associated graded term of
\((\mathcal O(V)\otimes_kB')\otimes_{B'}N\), multiplication by \(f'\) is multiplication by that same nonzero special function. It is injective. Induction on this finite filtration makes multiplication by \(f'\) injective on the whole module. The sequence defined by this multiplication consequently proves that its quotient is flat over \(B'\), using the tensor criterion.

That quotient is finite over \(B'\). Its residue quotient has finite dimension \(n\). Lift a residue basis. Those lifts span modulo the maximal ideal; successively substituting this spanning assertion and using nilpotence of the maximal ideal shows they span the whole module, without applying finite Nakayama to an unproved finite module. A finite flat module over the local Artinian ring is free by T4–T5, of rank \(n\). The resulting closed subscheme of \(V_{B'}\) is also closed in \(C_{B'}\): its finite map to the base and the separated curve make its image closed by the graph and proper projection argument. Equivalently glue its ideal with the unit ideal off that closed support. This gives the required lifted divisor.

For the tangent assertion take \(B'=k[\epsilon]/(\epsilon^2)\). A local generator lifts to \(f+\epsilon g\); changing its unit frame changes \(g\) by a multiple of \(f\). These classes glue with precisely the transition factors of \(\mathcal I_D^\vee|_D\), giving (DR10), and every such section gives the corresponding first-order ideal. The line on the length-\(n\) scheme has \(n\) independent coefficients over the field, proving its dimension.

Here is the passage from these Artinian lifts to an actual smooth chart. At a geometric point choose a polynomial presentation of a DR3 chart, and eliminate independent linear relations by SF3's formal implicit calculation. Its completed local ring has the form
\[
 k[[t_1,\ldots,t_n]]/J,\qquad J\subset(t_1,\ldots,t_n)^2,
 \tag{DR11}
\]
because (DR10) gives tangent dimension \(n\). Completion of the quotient is justified by DR1. If \(J\ne0\), let \(d\ge2\) be the least order of a nonzero element. In
\(B'=k[[t]]/(t)^{d+1}\), its degree-\(d\) image ideal \(J_d\) is nonzero and square-zero. The natural point over \(B=B'/J_d\) would lift to \(B'\) by the divisor lifting just proved. Each coordinate would then lift as \(t_i+\delta_i\), with \(\delta_i\in J_d\). Substitution cannot change the degree-\(d\) initial term of a relation of order \(d\), since every correction has order at least \(2d-1\ge d+1\). That initial term remains nonzero in \(B'\), a contradiction. Thus \(J=0\).

In the algebraic presentation, retain the relations used to eliminate the independent linear terms. They define a standard smooth chart of dimension \(n\), surjecting onto the given local ring. Its remaining finite ideal has zero completion by (DR11), hence is zero by DR1. Finite witnesses spread the equality to a neighbourhood. This gives an actual smooth chart, not merely a tangent count. These charts cover after algebraic closure by closed-point detection B1. Smoothness descends to \(k\) by the split relation-gradient and projective-differential argument SF1–SF3 and FD1–FD4, already used in QS6 and FQ3. \(\square\)

#### 2J.6. Formal coordinates at colliding divisors

**DR6.** At a geometric divisor \(D=\sum_i n_iP_i\), with distinct \(P_i\), choose a formal parameter \(u_i\) at each point. Its completed parameter ring is
\[
 \widehat{\mathcal O}_{S_n(C),D}
    \simeq k[[c_{i,j}:1\le j\le n_i]],\qquad
 P_i(U)=U^{n_i}+c_{i,1}U^{n_i-1}+\cdots+c_{i,n_i}.
 \tag{DR12}
\]
For an ordered list of points specializing to these supports, the pullback of the \(c_{i,j}\) is \((-1)^j e_j(u_{i,1},\ldots,u_{i,n_i})\).

*Proof.* In an Artinian deformation the finite divisor algebra splits into factors at the distinct support points: its special orthogonal idempotents lift uniquely by HS1. In the \(i\)-th factor, the powers \(1,u_i,\ldots,u_i^{n_i-1}\) form a basis. They do on the special fibre \(k[u_i]/(u_i^{n_i})\), and Nakayama and the determinant criterion preserve the basis over the local Artinian base. Its multiplication by \(u_i\) gives a unique monic relation \(P_i\) of degree \(n_i\). All the lower coefficients lie in the base maximal ideal. Monic division proves that the divisor algebra is exactly the polynomial quotient by \(P_i\), since both free modules have that basis.

This calculation also works in the completed curve ring. Its parameter gives \(k[[u_i]]\) by the smooth one-coordinate formal chart. The companion matrix of \(u_i\) in the quotient is nilpotent: it is nilpotent modulo the base maximal ideal, and that ideal is nilpotent. Therefore every power series evaluates by a finite sum. Polynomial division and that nilpotence identify the quotient of the completed ring with the same polynomial quotient. Conversely any lower coefficients in the Artinian maximal ideal define this finite free quotient of the completed curve ring. Its nilpotence makes the curve-coordinate map factor through an algebraic finite infinitesimal neighbourhood of \(P_i\), so it defines an actual closed divisor on the curve, glued with the unit ideal off the support. These constructions are inverse and natural.

Thus deformations over every local Artinian algebra are exactly the lists of these coefficients. This identifies the complete local ring with (DR12): homomorphisms of complete Noetherian local rings to all their Artinian quotients determine the maps and their inverse limits, so the natural coefficient maps are inverse on completions. For a sum of ordered graphs, the local equation is \(\prod_j(U-u_{i,j})\); comparing its coefficients gives the last assertion, including nilpotent parameters and all signs. \(\square\)

#### 2J.7. The ordered cover and proper symmetric power

**DR7.** The sum of graphs gives a finite faithfully flat map
\[
 \sigma_n:C^n\longrightarrow S_n(C),\qquad
 (P_1,\ldots,P_n)\longmapsto P_1+\cdots+P_n,
 \qquad \operatorname{rank}\sigma_n=n!.
 \tag{DR13}
\]
The target is proper and geometrically integral, and is the symmetric power of the curve. The rank retains all collision multiplicities.

*Proof.* On \(C\times C^n\), each section graph is Cartier: the smooth curve diagonal has a one-parameter ideal in its smooth local charts, and its pullback under the flat product projection retains that ideal. Multiply these invertible ideals. The resulting sum is Cartier and has every geometric fibre of length \(n\). It is proper over \(C^n\) and has finite fibres, so is finite by the proved proper finite-fibres theorem of Lesson 3. The target \(C^n\) is integral. Its finite coordinate module has generic rank \(n\) and every fibre dimension \(n\), so FF1's local domain rank lemma makes it finite locally free of rank \(n\). This constructs the universal family defining \(\sigma_n\), with all later base changes.

Over an algebraically closed field every finite subscheme of a smooth curve is a unique effective divisor \(\sum_i n_iP_i\), by its DVR ideals. It therefore has ordered preimages, and only the finitely many orders of that multiset. Thus \(\sigma_n\) is surjective with finite geometric fibres. Its source is proper and its target is separated by DR4, so the graph and proper projection make it proper. The same proper finite-fibres theorem makes it finite.

We compute its scheme length at a fibre. In the completed source at one ordering, DR6 identifies the coefficient map with the elementary symmetric functions in each block of \(n_i\) local parameters. Consequently the local fibre algebra has dimension \(\prod_i n_i!\), by (DR6) and DR2's free basis, now completed at the unique zero point. Completion does not change a finite local Artinian algebra. There are \(n!/\prod_i n_i!\) orderings, so the total fibre length is exactly \(n!\). This calculation applies over every algebraically closed field extension, including one over a generic residue field.

The smooth target is geometrically reduced by DR5. It is geometrically irreducible as the surjective image of the geometrically integral \(C^n\), so its local rings are domains. The finite module of \(\sigma_n\) has generic rank \(n!\) and fibre dimension \(n!\) at every point. FF1 again makes it finite locally free, and positive rank makes it faithful. This proves (DR13).

Properness of \(S_n(C)\) follows without a separate valuative criterion. After any base change, a closed subset of \(S_n(C)\) and its closed inverse image in the proper \(C^n\) have exactly the same image in the base. That image is closed. Thus the target is universally closed; it is already separated and of finite type. Its dimension is \(n\) by DR5.

To verify the symmetric quotient assertion as schemes, take an affine open \(V\subset C\) and the open \(Q=S_n(V)\) classifying divisors supported there. Its finite faithfully flat cover is \(X=V^n\), an affine scheme. We supply the needed affine-target argument; having an affine source alone is not an application of FD6.

Write \(X=\operatorname{Spec}A\). The relation \(X\times_QX=\operatorname{Spec}B\) is affine and finite locally free of rank \(r=n!\) over either copy of \(X\). It is closed in \(X\times_kX\), because \(Q\) is separated. Write its two algebra maps as \(s,t:A\to B\), and put \(D=\{a:s(a)=t(a)\}\). FD5, applied to maps to the affine line, identifies \(D\) with \(\Gamma(Q,\mathcal O_Q)\). Multiplication by \(a\in A\) is an endomorphism of the rank-\(r\) bundle \(q_*\mathcal O_X\) on \(Q\). Its characteristic coefficients are global functions on \(Q\), hence lie in \(D\), and Cayley–Hamilton makes \(a\) integral over \(D\). Thus \(A/D\) is finite, and the multiplication-table argument QS2 makes \(D\) a finite-type Noetherian \(k\)-algebra.

The closed relation gives a surjection \(A\otimes_DA\to B\). The common-basis argument QS3 applies: after faithfully flat local extensions of \(D\) with infinite residue fields, choose \(x_1,\ldots,x_r\in A\) such that the \(t(x_i)\) are a basis of \(B\) over \(s(A)\). Expand \(t(a)=\sum_i s(c_i)t(x_i)\). On the triple relation \(X\times_QX\times_QX\), compare its expansions using the first and the second copy of \(X\). Their third-copy basis is the scalar extension of the same basis along the second-coordinate map. Its independence forces \(s(c_i)=t(c_i)\), so \(c_i\in D\). The diagonal section gives \(a=\sum_i c_ix_i\); applying \(t\) proves independence. Thus \(A\) is free of rank \(r\) over \(D\) after these local extensions, and \(A\otimes_DA\simeq B\) there. FD1 and FD4 descend the isomorphism and finite local freeness. Hence \(X\to\operatorname{Spec}D\) is a finite faithfully flat cover with exactly the same relation as \(X\to Q\). FD5 descends the identity of \(X\) to maps between these two targets in both directions, and detects that the composites are identities. Therefore \(Q=\operatorname{Spec}D\).

The symmetric group acts on \(A=\mathcal O(V)^{\otimes n}\), and \(D\subset A^{\mathfrak S_n}\). This is equality. It can be checked after algebraic closure and after completing at each target closed point, by DR1 and faithful field extension. The completed finite algebra splits into the factors for the ordered preimages, by the finite Artinian decomposition and lifted idempotents of HS1–HS2. In each factor the source maximal-ideal powers and the target maximal-ideal powers are cofinal: the finite special algebra is Artinian, so some power of its maximal ideal is zero, giving the needed reverse power inclusion. Thus these are exactly the completed source local rings. The group permutes the factors transitively, and the stabilizer of one ordering permutes its blocks of equal support points. Its invariant completed ring is the power-series ring in their elementary symmetric functions, exactly (DR12). For the power-series invariant assertion, decompose into homogeneous terms and apply the polynomial symmetric-function elimination: cancel the lexicographically largest monomial by the corresponding product of elementary functions and continue by degree. Each finite degree needs finitely many steps, so the resulting formal series converges by degree. The elementary-function weights lie between one and \(n\), making weighted and ordinary adic degrees cofinal. This proof uses no averaging or inverse of \(n!\). The same leading-monomial argument proves uniqueness and algebraic independence, also supplied by DR2. Completion commutes with the invariant kernel because all the modules here are finite over the Noetherian \(D\) and DR1 is exact. Faithful detection proves
\[
 \mathcal O(S_n(V))=
       \bigl(\mathcal O(V)^{\otimes_k n}\bigr)^{\mathfrak S_n}.
 \tag{DR14}
\]
The finite-cover opens and these invariant rings glue with the invariant-map universal property: an invariant map into a scheme has invariant preimages of affine opens; the complements have closed images under the finite map, so these are quotient opens, and on their affine subopens (DR14) gives the coordinate factorization. Uniqueness makes the factorizations glue. This proves the symmetric-power assertion. \(\square\)

#### 2J.8. Addition, full families and the Picard construction ahead

**DR8.** Multiplying the two invertible universal ideals gives a morphism
\[
 a_{r,s}:S_r(C)\times S_s(C)\longrightarrow S_{r+s}(C),
 \quad(D,E)\longmapsto D+E,
 \qquad \deg a_{r,s}=\binom{r+s}{r}.
 \tag{DR15}
\]
It is finite faithfully flat, including at coincident divisors and in characteristics dividing the displayed degree. All its universal-family and rank assertions commute with arbitrary base change.

*Proof.* Pull back the two universal ideals to the curve over the product base and multiply them. Their product is an invertible ideal generated by a nonzero divisor: this follows by pulling back the finite faithfully flat ordered covers of DR7, where it is the actual sum of section graphs, and faithfully detecting the injection. Its quotient there is the rank-\((r+s)\) ordered universal family; FD4–FD6 descend its finite local freeness. DR4 therefore supplies the displayed morphism.

It is proper because its source is proper and the target separated. On geometric points a fibre amounts to choosing integers between zero and the given point multiplicities with sum \(r\); there are finitely many choices. The proper finite-fibres theorem makes it finite. On affine target charts its algebra factorization is
\[
 B\longrightarrow D\longrightarrow A,
 \quad A/D\text{ finite faithfully flat of rank }r!s!,
 \quad A/B\text{ finite locally free of rank }(r+s)!.
 \tag{DR16}
\]
Here the last composite is the ordered cover for all \(r+s\) points, and the first cover groups them into the two ordered blocks. The intermediate map is flat by the tensor-injection argument FQ2: test an injection over \(B\), tensor with \(D\), then with the faithfully flat \(A/D\). The composite is injective by flatness of \(A/B\), so it was injective after \(D\). A finite flat module over the Noetherian target is finite locally free by T4–T5. Comparing ranks in (DR16) gives (DR15), and surjectivity follows from the surjective ordered composite. Base change preserves the proved covers, ideals and ranks.

Thus \(S_n(C)\) represents actual relative effective divisors, rather than unordered geometric support alone, and its complete local parameters include every infinitesimal collision direction. The next Picard construction must still glue line-bundle classes and prove its group, properness and universal properties. No Jacobian representability, stable reduction, initial semiabelian period cover or general analytic comparison theorem follows merely from these divisor parameter schemes. \(\square\)

#### 2J.9. Graded exercise: collisions, matrix charts and full families

**Exercise 2J (100 points; ten parts of 10 points each).** Use DR1–DR8 and the indicated earlier proofs. A support count alone is not a length calculation.

**(a) The six ordered roots.** For \(n=3\), write the successive monic root polynomials from DR2 and its six-element basis. Set all symmetric coefficients to zero. Compute the resulting algebra's graded dimensions and a nonzero element in its highest degree. Include characteristics two and three.

**(b) Two points collide.** In local coordinates for \(C^2\to S_2(C)\), compute the coefficient map, its differential determinant and the full fibre at the double divisor \(2P\). Compare it with a divisor \(P+Q\) with distinct points. Why is the target smooth at the collision?

**(c) Two unequal multiplicities.** For \(D=2P+3Q\), compute the number of ordered preimages, each local fibre length, the total rank of the ordered cover and the tangent dimension of \(S_5(C)\). For \(a_{2,3}\), list the possible subdivisors of degree two and their local fibre lengths. Verify the total degree.

**(d) Degrees zero and one.** Identify \(S_0(C)\) and \(S_1(C)\) as schemes by their functors, over arbitrary parameter bases. Explain why rank-one finite locally free algebras have their unit as a basis.

**(e) A matrix chart with a curve relation.** For quotients of \(k[x,y]\) of rank two, use the basis \(1,x\). Write the multiplication matrices, solve their commutation equations and identify this chart. Then impose the curve equation \(y=x^2\). Over \(R=k[\epsilon]/(\epsilon^2)\), specialize to the divisor with quotient \(R[x]/(x^2-\epsilon)\); give both matrices and the full \(k\)-dimension.

**(f) Equality of families is more than equality on fibres.** On \(\mathbf A^1_R\), with the same \(R\), compare \(D_1=(x^2)\) and \(D_2=(x^2-\epsilon)\). They have the same geometric fibres. Compute the scheme in \(\operatorname{Spec}R\) on which they become equal, and relate this to the separated diagonal in DR4.

**(g) A nonreduced Artinian lift.** Let \(B=\mathbf F_p[\epsilon]/(\epsilon^2)\), \(B'=\mathbf F_p[\epsilon]/(\epsilon^3)\), and
\(P(T)=T^3+aT^2+bT+c\), with \(a,b,c\in(\epsilon)\subset B\).
Count its monic coefficient lifts to \(B'\). Prove that each gives a finite flat divisor, compute its rank and its total \(\mathbf F_p\)-dimension, and explain its three independent infinitesimal directions. Do not invert three.

**(h) Completion keeps the infinitesimal layer.** For \(A=k[t]_{(t)}\), \(I=(t)\), \(M=A\) and \(N=t^3A\), compute \(I^rM\cap N\) and \(I^rN\), and give an Artin–Rees index. Compute the completed inclusion. For \(Q=A/(t^2)\), compare its completion with its reduction modulo \(t\).

**(i) Divisors on the projective line.** Construct \(S_n(\mathbf P^1)\simeq\mathbf P^n\) from the universal homogeneous polynomial of degree \(n\), including multiple roots and arbitrary characteristic. Justify that the resulting map is an actual scheme isomorphism; a bijection on geometric points does not suffice.

**(j) The first Jacobian chart.** Let \(C\) have genus \(g\). Prove that
\[
 U=\{D\in S_g(C):H^1(C,\mathcal O_C(D))=0\}
 \tag{DRX1}
\]
is a nonempty geometrically open subscheme, and that every geometric divisor in it has \(h^0=1\). Explain what further line-bundle gluing and universal properties are still needed to construct the Jacobian and the general period cover.

**Full solution.**

**(a)** The first root satisfies
\(P_0(T)=T^3-E_1T^2+E_2T-E_3\). Division by \(T-x_1\) gives
\[
 P_1(T)=T^2+(x_1-E_1)T+(x_1^2-E_1x_1+E_2).
 \tag{DRX2}
\]
Adjoin \(x_2\) as a root, and the last root is \(x_3=E_1-x_1-x_2\). The full basis is
\[
 1,\ x_1,\ x_1^2,\ x_2,\ x_1x_2,\ x_1^2x_2.
 \tag{DRX3}
\]
At \(E_1=E_2=E_3=0\), the algebra is
\[
 k[x_1,x_2]/(x_1^3,\ x_2^2+x_1x_2+x_1^2).
 \tag{DRX4}
\]
Its displayed monic basis remains a basis, so the dimensions in degrees zero through three are \(1,2,2,1\), with no higher-degree part. The class \(x_1^2x_2\) is nonzero. In particular \(x_2^3=0\), by substituting the second relation twice, and every degree-four monomial is zero. The full length is six even when there is just one underlying point. All equations and the free-basis proof work in characteristics two and three; no averaging occurs.

**(b)** Use coefficient coordinates \(c_1=-(x+y),\ c_2=xy\), so the divisor polynomial is \(T^2+c_1T+c_2\). Its differential matrix and determinant are
\[
 \begin{pmatrix}-1&-1\\y&x\end{pmatrix},
 \qquad \det=y-x.
 \tag{DRX5}
\]
At the double point the fibre is
\(k[x,y]/(x+y,xy)\simeq k[x]/(x^2)\), of length two and with one geometric point, including in characteristic two. At distinct points there are two ordered preimages, each a reduced length-one point, since the two linearized coordinates have invertible determinant. In both cases the rank is two. DR6 makes the target completed ring \(k[[c_1,c_2]]\), and DR5 proves the corresponding algebraic smooth chart. Ramification of the cover does not make that target singular.

**(c)** The ordered multiset has \(5!/(2!3!)=10\) distinct orderings. Each local fibre length is \(2!3!=12\), so the total is \(120\), while the tangent dimension is five. The degree-two subdivisors are
\[
 2Q,\qquad P+Q,\qquad 2P.
 \tag{DRX6}
\]
Their local lengths under \(a_{2,3}\) are respectively
\[
 \binom20\binom32=3,\qquad
 \binom21\binom31=6,\qquad
 \binom22\binom30=1.
 \tag{DRX7}
\]
Here is the length argument. Near a support point of multiplicity \(m\), splitting it into degrees \(a,m-a\) means factoring a monic polynomial into those two monic factors. Its coefficient ring embeds in the ordered-root ring; the latter is free of rank \(a!(m-a)!\) over the factor-coefficient ring, and free of rank \(m!\) over the full coefficient ring, by DR2 on the two blocks and on the whole list. The intermediate ring is finite because it is a submodule of the finite ordered-root ring over the Noetherian full coefficient ring. The tensor-injection proof FQ2 therefore gives finite flat rank \(\binom ma\) for the factor map. Complete at the single repeated-root point to obtain its local fibre length. Independent support points give the product of these lengths, proving (DRX7). Their sum is ten, agreeing with \(\binom52\). Counting the three support allocations would miss seven units of fibre length.

**(d)** A rank-zero quotient is the empty subscheme, uniquely, so \(S_0(C)=\operatorname{Spec}k\). If \(D/T\) is finite locally free of rank one, its unit has nonzero residue at every point: a nonzero one-dimensional algebra over a field has a nonzero identity. In a local free frame that unit is therefore a unit multiple of the frame. It is a basis, and the unit map \(\mathcal O_T\to\mathcal O_D\) is an algebra isomorphism. A closed embedding \(D\hookrightarrow C_T\) is consequently precisely the graph of a section \(T\to C\). Thus \(S_1(C)=C\) as functors and schemes. The ordered maps in degrees zero and one are identities and have rank one.

**(e)** Multiplication by \(x\) and \(y\) initially has the form
\[
 X=\begin{pmatrix}0&a\\1&b\end{pmatrix},\qquad
 Y=\begin{pmatrix}c&d\\e&f\end{pmatrix}.
 \tag{DRX8}
\]
The equations \(XY=YX\) give \(d=ae\), \(f=c+be\); the remaining two entries then agree. Hence \(Y=cI+eX\), and the chart is the affine four-space with coordinates \(a,b,c,e\), with universal quotient
\[
 k[x,y]/(x^2-bx-a,\ y-c-ex).
 \tag{DRX9}
\]
For the parabola, \(X^2=aI+bX\). The relation \(Y=X^2\) is therefore exactly \(c=a,e=b\), leaving affine two-space with coordinates \(a,b\). In the specified family \(a=\epsilon,b=0\),
\[
 X=\begin{pmatrix}0&\epsilon\\1&0\end{pmatrix},\qquad
 Y=\epsilon I .
 \tag{DRX10}
\]
The algebra is free of rank two over \(R\), with basis \(1,x\), and has dimension four over \(k\). It retains the equation \(x^2=\epsilon\); replacing the family by its double-point special support would erase that equation.

**(f)** Both quotients have basis \(1,x\) over \(R\). Evaluate the generator \(x^2-\epsilon\) of the second ideal in the first quotient: it is \(-\epsilon\). Its coordinates vanish after a parameter change exactly when the image of \(\epsilon\) is zero. On that closed subscheme both ideals are \((x^2)\), while elsewhere as a functor condition they are unequal. Thus the equality locus is
\[
 \operatorname{Spec}(R/(\epsilon))
       \hookrightarrow\operatorname{Spec}R.
 \tag{DRX11}
\]
All geometric fibres factor through this locus, but the identity map of the nonreduced base does not. This is the actual closed diagonal condition in DR4. Equality of geometric fibres would incorrectly give the entire base.

**(g)** Each coefficient has \(p\) possible lifts, differing by a scalar multiple of \(\epsilon^2\), so there are \(p^3\) monic lifts. Each quotient by its monic cubic is free with basis \(1,T,T^2\), of rank three over \(B'\), and total dimension nine over \(\mathbf F_p\). It is a Cartier divisor on the affine line because multiplication by a monic polynomial in \(B'[T]\) is injective, by its highest nonzero coefficient. The three differences in its coefficients give the three independent tangent directions at the special divisor \(3[0]\), exactly DR10. These are coefficient directions, not three independently moving reduced points. The argument holds for \(p=2\) and \(p=3\) without any inverse of the factorial.

**(h)** The two filtrations are
\[
 I^rM\cap N=t^{\max(r,3)}A,\qquad
 I^rN=t^{r+3}A.
 \tag{DRX12}
\]
They differ, but for \(r\ge3\) the first is \(I^{r-3}(I^3M\cap N)\). Thus \(c=3\) is an Artin–Rees index. Completion gives the injection
\(t^3k[[t]]\hookrightarrow k[[t]]\), with its full quotient \(k[[t]]/(t^3)\). For \(Q\), (DR2) gives \(k[[t]]/(t^2)\), of length two; reduction gives only \(k\), of length one. Completion retains the nilpotent class of \(t\), while reduction kills it. Cofinality of filtrations does not assert equality with the same exponent at every level.

**(i)** On \(\mathbf P^1\times\mathbf P^n\), take the zero scheme of
\[
 F(X,Y)=a_0X^n+a_1X^{n-1}Y+\cdots+a_nY^n.
 \tag{DRX13}
\]
Every geometric coefficient point has a nonzero polynomial and therefore a divisor of degree \(n\), including its multiplicities. The zero scheme is proper with finite fibres over the integral \(\mathbf P^n\), hence finite by the proper finite-fibres theorem. The rank test FF1, with generic rank and every fibre length equal to \(n\), makes it finite locally free. It therefore defines a morphism \(m:\mathbf P^n\to S_n(\mathbf P^1)\), and its universal family survives all parameter changes.

Over an algebraically closed field every divisor gives exactly one homogeneous polynomial up to scalar, so \(m\) is bijective on geometric points. To check the scheme structure, choose a projective coordinate whose point at infinity avoids the finite support. In the corresponding coefficient chart the polynomial is monic. At a multiple support point, its local coefficient deformation is exactly the monic polynomial in DR12. At several distinct support points, coprime monic factor lifting is unique by the Hensel factor proof of Lesson 1, §0D, applied successively over Artinian thickenings. Thus the global monic coefficients and the lists of local coefficients give isomorphic complete local deformation rings. In particular the differential of \(m\) is an isomorphism at every geometric point. Both schemes are smooth of dimension \(n\), so SF1–SF3 make \(m\) étale. It is proper by the graph argument and finite by its finite fibres. Each geometric fibre is now one reduced point, so it is finite locally free of rank one. Its unit is a basis by part (d), proving it is an isomorphism. This also handles arbitrary characteristic; \(n=0\) gives the two one-point schemes.

**(j)** Apply FC10 to the universal line \(\mathcal O(D)\) on \(C\times S_g(C)\). Its finite complex makes the condition \(h^1=0\) open: after removing higher zero terms by local splitting, vanishing of the cokernel of its final matrix is an open rank condition. The curve has no higher coherent cohomology by the earlier curve proof. Riemann–Roch SD1–SD7 gives \(\chi(\mathcal O(D))=g+1-g=1\), so \(h^0=1\) on that open.

It is nonempty after algebraic closure. If \(g=0\), use the empty divisor. For \(g>0\), begin with the \(g\)-dimensional space \(H^0(C,\omega_C)\). As long as its subspace vanishing at already chosen points is nonzero, choose a nonzero differential in that subspace and a new point where it does not vanish. Its zero set is finite, whereas the algebraically closed smooth curve has infinitely many points by the finite-type closed-point and nonconstant-parameter argument of Lesson 3. Evaluation at the chosen point reduces that subspace's dimension by one. After \(g\) choices, the effective divisor \(D\) has \(H^0(C,\omega_C(-D))=0\). Curve duality identifies this with the dual of \(H^1(C,\mathcal O(D))\), so \(D\in U\). The construction of \(S_g\) and its universal line commutes with every field extension, proving the geometric openness and nonemptiness asserted.

This constructs a genuine open space of nonspecial effective divisors. To obtain the Jacobian one still must identify the corresponding line-bundle subfunctor over full parameter bases, glue its translates, construct and verify the group and universal line, and prove the required properness and mapping properties. The stable curve model and the formal/analytic initial period cover remain additional geometric constructions. Neither the divisor parameter scheme nor a citation to the free Jacobian or uniformization theorem supplies those remaining proofs.

### 2K. The Picard scheme and Jacobian of a pointed curve

Let \(C/k\) be a smooth projective geometrically integral curve of genus \(g\), and fix \(P\in C(k)\). We construct its Jacobian, including its universal line bundle and its divisor maps on arbitrary parameter schemes. The point matters: it lets us normalize a line bundle along a section, rather than confuse a relative class with a globally chosen line bundle.

The free primary comparisons are the Stacks project's [Picard scheme of a curve](https://stacks.math.columbia.edu/tag/0B9R) and Milne's author version of [*Jacobian Varieties*, §4](https://www.jmilne.org/math/xnotes/JVs.pdf). The arguments below use the actual divisor schemes DR1–DR8, curve duality SD1–SD7, finite cohomology complexes FC10–FC20, and module descent FD1–FD4 already proved in this programme. They include the family arguments needed over nilpotent bases.

#### 2K.1. Sections that remain regular over a parameter base

**JC1.** Let \(T\) be a \(k\)-scheme, \(\pi:C_T\to T\), and let \(s\) be a section of a line bundle \(L\). Suppose \(s\) is nonzero on every geometric fibre. Its zero scheme is a relative effective Cartier divisor, flat over \(T\); where the fibre degree of \(L\) is \(d\), that divisor is finite locally free of rank \(d\).

First assume \(T\) Noetherian. At a point of \(C_T\), trivialize \(L\), and put
\[
 R=\mathcal O_{T,t},\qquad Q=\mathcal O_{C_T,x},\qquad
 f=s|_{\operatorname{Spec}Q},\qquad \mathfrak m=\mathfrak m_R .
 \tag{JC1}
\]
The ring \(Q\) is Noetherian, local and \(R\)-flat. On the smooth integral fibre, a nonzero section is a nonzerodivisor, so \(\bar f\) is a nonzerodivisor in \(Q/\mathfrak mQ\). For every finite \(R\)-module \(N\), flatness gives
\[
 \operatorname{gr}_{\mathfrak m}(Q\otimes_RN)
 \simeq (Q/\mathfrak mQ)\otimes_{R/\mathfrak m}
                   \operatorname{gr}_{\mathfrak m}N .
 \tag{JC2}
\]
Multiplication by \(f\) is injective on each graded term. An element killed by \(f\) therefore belongs successively to every \(\mathfrak m^r(Q\otimes_RN)\). This intersection is zero by DFR3: the module is finite over the Noetherian local ring \(Q\), and \(\mathfrak mQ\) lies in its maximal ideal. Thus \(f\) is injective on \(Q\otimes_RN\). Any \(R\)-module is the filtered union of its finite submodules, and tensor products commute with that union, so the conclusion holds for every \(N\).

In particular \(f\) is regular on \(Q\). To prove flatness of \(Q/fQ\), tensor an injection \(N'\hookrightarrow N\) and its quotient with \(Q\). If an element of \(Q\otimes N'\) becomes \(f v\) in \(Q\otimes N\), the image of \(v\) in \(Q\otimes(N/N')\) is killed by \(f\); it is zero by the preceding paragraph. Hence \(v\) comes from \(Q\otimes N'\). Passing to the quotients by \(f\) preserves the injection. This is precisely flatness, by T1. Consequently
\[
 0\longrightarrow L^{-1}\xrightarrow{\ s\ }\mathcal O_{C_T}
   \longrightarrow\mathcal O_{Z(s)}\longrightarrow0
 \tag{JC3}
\]
is exact and stays exact after arbitrary base change. The zero scheme is proper over \(T\), and its geometric fibres have finite length \(d\), by the degree calculation DC1–DC6. Properness with finite fibres, proved in Lesson 3, makes it finite. Its finite, finitely presented flat algebra is locally free, with rank \(d\), by T4–T5.

Here is the finite-equation step extending this statement, and later uses of FC10, to arbitrary \(T\). Work locally on \(T=\operatorname{Spec}A\). A line bundle on the finitely presented, quasi-compact separated scheme \(C_A\) can be described on finitely many affine principal opens by rank-one bases, unit transition functions, inverse transitions and cocycle identities. A section and a rigidification require finitely many additional elements and equations. Include the coefficients of the opens, of a finite witness that they cover, and of all these equations in a finitely generated \(k\)-subalgebra \(A_0\subset A\). This gives the same data over \(A_0\); inverse and cocycle equations ensure it is an actual line bundle. Isomorphisms and any finite list of commutative diagrams descend in the same way.

The locus in \(\operatorname{Spec}A_0\) where the descended section is nonzero on the fibre is open. To see this without a reduced-base assumption, near any base point twist by a sufficiently large power of a fixed effective ample divisor on \(C\). Curve duality and FC15 make the pushforward of that twist a vector bundle with all base changes. The section, multiplied by the fixed divisor section, is a vector in that bundle. It is nonzero on a fibre exactly when at least one coordinate of that vector is nonzero there. Multiplication by the fixed section is injective on each integral curve fibre, so it detects the original section. This proves the assertion about the open locus. Euler characteristic and degree are locally constant by CE3 and DC6. The map from \(\operatorname{Spec}A\) lands in the relevant good open because the hypothesis holds on all its fibres. Pull back (JC3) and its finite flat zero scheme from that Noetherian open. This proves JC1 on all bases and also justifies applying finite-complex and open-locus arguments below after finite-equation descent. \(\square\)

#### 2K.2. Rigidification and effective descent

**JC2.** Define \(\mathcal P_d(T)\) to consist of isomorphism classes of pairs
\[
 (L,\rho),\qquad
 \rho:P_T^*L\xrightarrow{\sim}\mathcal O_T,\qquad
 \deg L_{\bar t}=d\quad(\bar t\to T).
 \tag{JC4}
\]
Isomorphisms preserve \(\rho\). Every automorphism of a line bundle on \(C_T\) is multiplication by a global unit. FC20, with arbitrary base change, identifies these units with \(\Gamma(T,\mathcal O_T^\times)\). Preserving the rigidification forces that unit to be \(1\). Thus between two isomorphic rigidified bundles there is exactly one isomorphism.

For an unrigidified line bundle put
\[
 L^\natural=L\otimes\pi^*(P_T^*L)^{-1}.
 \tag{JC5}
\]
Its restriction to \(P_T\) has its canonical evaluation trivialization. Tensoring \(L\) by a bundle pulled back from \(T\) does not change \(L^\natural\) as a rigidified object. Conversely (JC5), applied to a rigidified bundle, recovers that bundle using \(\rho\). Therefore \(\mathcal P_d\) is the degree-\(d\) part of
\[
 \operatorname{Pic}(C_T)/\pi^*\operatorname{Pic}(T).
 \tag{JC6}
\]
This equality is on full schemes, not just on fields.

The functor is a sheaf for faithfully flat quasi-compact covers. Indeed two local representatives with equal classes have unique rigidified isomorphisms on overlaps. Uniqueness gives the cocycle identity on triple overlaps. On affine pieces the modules and their descent isomorphisms descend effectively by FD2; their rank-one projectivity descends by FD4. Restriction maps, multiplication, the rigidification and its inverse descend by FD1–FD3. Glue on affine overlaps using the same uniqueness. Fibre degrees descend after field extension. This proves both existence and uniqueness of the descended object. Tensor product and inverse make \(\mathcal P_0\) a group functor, acting on every \(\mathcal P_d\). \(\square\)

#### 2K.3. The nonspecial chart, on full families

**JC3.** Let \(U\subset S_g(C)\) be the open subset on which
\[
 H^1(C_{\bar t},\mathcal O(D_{\bar t}))=0 .
 \tag{JC7}
\]
Its openness follows by cancelling unit entries in FC10–FC14; on a curve the remaining complex has terms only in degrees zero and one. Riemann–Roch makes \(h^0=1\) there. The rigidified universal divisor line
\[
 L_U=\mathcal O(\Delta_U)\otimes
       \pi_U^*\bigl(P_U^*\mathcal O(\Delta_U)\bigr)^{-1}
 \tag{JC8}
\]
represents the subfunctor of \(\mathcal P_g\) whose geometric fibres have \(H^1=0\).

Here are the inverse and its base-change verification. For such \((L,\rho)\) on \(C_T\), FC15 gives an invertible module \(E=\pi_*L\), with formation commuting with every base change. Evaluation defines a section
\[
 \pi^*E\longrightarrow L,\qquad
 s\in H^0(C_T,L\otimes\pi^*E^{-1}) .
 \tag{JC9}
\]
Its restriction to every geometric fibre generates the one-dimensional space of sections, so is nonzero. JC1 produces a finite locally free Cartier divisor \(D\) of degree \(g\), and
\[
 \mathcal O(D)\simeq L\otimes\pi^*E^{-1},\qquad
 \mathcal O(D)^\natural\simeq L .
 \tag{JC10}
\]
The second isomorphism uses \(\rho\) and respects rigidification.

Conversely, start with \(D\in U(T)\). Locally on \(T\), choose a basis of the inverse of \(P_T^*\mathcal O(D)\). The canonical divisor section then gives a section of the rigidified line (JC8). On every fibre it is a nonzero basis of \(H^0\). FC15 and the actual determinant test make it a basis of its rank-one pushforward locally on \(T\). Evaluation therefore has exactly the original zero scheme \(D\). Changing that chosen basis multiplies the section by a base unit and does not change the zero scheme. These operations are inverse and commute with arbitrary base changes by (JC3) and FC15. JC1's finite-equation argument supplies the same assertions on non-Noetherian bases.

In particular, no value of the divisor section at \(P\) is divided out. A divisor can contain \(P\); the invertible module \(P_T^*\mathcal O(D)\) still exists, although that section's value vanishes. It is the module, rather than its possibly zero section, which occurs in (JC8). Finally, for any family in \(\mathcal P_g(T)\), the locus satisfying (JC7) is open by FC10–FC14 and JC1. Hence \(U\to\mathcal P_g\) is an open immersion of functors. \(\square\)

#### 2K.4. Enough translates, including extension-field points

**JC4.** Suppose for the moment that \(k\) is separably closed; perfection is not assumed. There are infinitely many points of \(C(k)\). Indeed a standard smooth curve chart gives an étale map from a nonempty open of \(C\) to \(\mathbf A^1_k\). Its image is open by EA1–EA18. A nonempty étale fibre over a \(k\)-point is a finite disjoint union of finite separable extensions of \(k\), hence has a \(k\)-point. There are infinitely many \(k\)-points in that open image. Different fibres give different points of \(C\).

For every extension field \(F/k\) and degree-\(g\) line \(L\) on \(C_F\), there is a degree-zero line \(M\) defined over \(k\) for which \(L\otimes M_F^{-1}\) is nonspecial. Choose an ample line \(H\) on \(C\), of degree \(h>0\). For a sufficiently large integer \(m\), duality or Serre vanishing gives
\[
 H^1(C_F,L\otimes H_F^m)=0,\qquad
 h^0(C_F,L\otimes H_F^m)=1+mh.
 \tag{JC11}
\]
Choose a nonzero section. Its zero divisor is finite, while the distinct points of \(C(k)\) remain infinitely many distinct \(F\)-points. Choose \(Q_1\in C(k)\) where that section is nonzero. Evaluation at \(Q_1\) is surjective onto its one-dimensional fibre, and the exact sequence for subtracting \(Q_1\) reduces \(h^0\) by one while keeping \(H^1=0\). Repeat \(mh\) times, avoiding the finite zero set at each step. Thus
\[
 M=\mathcal O_C(Q_1+\cdots+Q_{mh})\otimes H^{-m},\qquad
 \deg M=0,\qquad H^1(C_F,L\otimes M_F^{-1})=0.
 \tag{JC12}
\]
Normalize \(M\) at \(P\) by (JC5). This changes none of these statements. This argument is needed even when \(F\) contains transcendental elements: we did not assume that \(L\) itself descends to \(k\).

For each isomorphism class \(M\in\mathcal P_0(k)\), take a copy \(U_M\) of \(U\), mapping to \(\mathcal P_g\) by tensoring (JC8) with \(M\). The inverse image of \(U_M\) under any \(T\to\mathcal P_g\) is the open where \(L\otimes M^{-1}\) is nonspecial. By JC3 it is represented by that open of \(T\). Given a point of \(T\), apply (JC12) to its residue field: some \(U_M\) contains that point, hence a neighbourhood of it. Thus these open subfunctors cover.

On \(U_M\), the overlap with \(U_N\) is the open where \(L_{U_M}\otimes M\otimes N^{-1}\) is nonspecial. JC3 gives its map to \(U_N\). The two universal rigidified bundles are isomorphic there, uniquely by JC2. The two directions are inverse because JC3's operations are inverse; uniqueness gives the triple-overlap identities. Gluing these schemes along those actual open isomorphisms produces a scheme \(J_g\) representing \(\mathcal P_g\). The universal rigidified lines glue as well. It is locally of finite type and smooth of dimension \(g\), since its charts are opens of the smooth \(g\)-dimensional scheme \(S_g(C)\).

For completeness, the open \(U\) is nonempty over \(k\). Apply (JC12) to \(L=\mathcal O_C(gP)\) over \(F=k\); JC3 then supplies a \(k\)-point of \(U\). This also covers \(g=0\), when \(S_0(C)\) is a point. \(\square\)

#### 2K.5. A closed diagonal that detects infinitesimal differences

**JC5.** The diagonal of \(J_g\) is a closed immersion. It suffices to check on products of its Noetherian charts. For two rigidified degree-\(g\) lines there, put \(N=L_1\otimes L_2^{-1}\), with its induced rigidification. Equality is precisely existence of a normalized isomorphism \(\mathcal O\to N\), which is unique if it exists.

Work near a point \(t\) of an affine chart product \(\operatorname{Spec}R\). A degree-zero line over a field has a section if and only if it is trivial: a nonzero section has an effective degree-zero zero divisor, hence no zeros, and trivializes the line. If \(N_{\bar t}\) is nontrivial, its \(H^0\) is zero. FC10–FC14 give \(P^0=0\) in a finite free complex near \(t\); no normalized section exists after any nonempty base change into that neighbourhood.

If \(N_{\bar t}\) is trivial, the residue-field dimensions are \(h^0=1\) and \(h^1=g\). The same cancellation gives, locally,
\[
 P^\bullet=[R e\xrightarrow{\ d\ }R^g],\qquad
 d(e)=(a_1,\ldots,a_g),
 \tag{JC13}
\]
computing cohomology after every base change. There is an \(R\)-linear evaluation map \(P^0\to R\) along \(P\). To construct it, use the actual comparison chain map from the finite complex to the affine Čech complex in FC10. Take the degree-zero component on an affine of \(C_R\) containing \(P_R\), restrict to \(P_R\), and apply the rigidification. On cycles this is ordinary evaluation, with the same assertion after every base change. On the residue-field basis its value is nonzero, since the trivial degree-zero fibre line has a normalized constant section. Shrink and rescale \(e\) to make its evaluation \(1\).

For every \(R\)-algebra \(R'\), a normalized cycle in \(P^0\otimes R'\) must now be \(e\otimes1\). It is a cycle exactly when
\[
 a_1=\cdots=a_g=0\text{ in }R'.
 \tag{JC14}
\]
The resulting section of \(N_{R'}\) evaluates to \(1\) at \(P_{R'}\). On every geometric fibre it is therefore nonzero, and degree zero makes it nowhere zero. A map between invertible modules which is a unit at every residue field is an isomorphism on stalks, even on a nonreduced scheme. Thus (JC14) represents the normalized isomorphism functor by the closed subscheme \(\operatorname{Spec}R/(a_1,\ldots,a_g)\).

These local closed subschemes glue: they represent the same subfunctor, and the rigidified isomorphism is unique. The empty locus in the other case glues in the same way. Consequently the diagonal is a closed immersion. In particular, (JC14) is an ideal of actual equations, not just a statement about which geometric points have trivial line bundle. \(\square\)

#### 2K.6. Properness, the group law and the universal line

**JC6.** The universal divisor defines an Abel map
\[
 b_g:S_g(C)\longrightarrow J_g,\qquad D\longmapsto\mathcal O(D)^\natural .
 \tag{JC15}
\]
It is surjective, including after every field extension: Riemann–Roch gives \(h^0(L)\ge1\) for every degree-\(g\) line, whose nonzero section supplies its divisor. Surjectivity on arbitrary base changes follows by this assertion on geometric fibres. Since \(S_g(C)\) is quasi-compact, its surjective image \(J_g\) is quasi-compact. A locally finite-type scheme which is quasi-compact is of finite type here: choose finitely many finite-type affine chart opens covering it. It is separated by JC5.

For any \(k\)-scheme \(T\) and closed subset \(Z\subset (J_g)_T\), its inverse image in \(S_g(C)_T\) is closed. Its image in \(T\) is closed by properness of \(S_g(C)\), and equals the image of \(Z\) because (JC15) is universally surjective. Thus \(J_g\to\operatorname{Spec}k\) is universally closed. Along with finite type and separatedness, this proves properness. After every algebraically closed field extension it is irreducible, as the surjective image of the geometrically integral \(S_g(C)\), and is reduced because it is smooth. Hence \(J_g\) is geometrically integral.

The normalized line \(A_g=\mathcal O_C(gP)^\natural\) gives an isomorphism of functors \(\mathcal P_0\to\mathcal P_g\) by tensor product. Transporting the representation along it gives \(J=J_0\), with identity the trivial rigidified line. The tensor and inverse operations on all families, represented using Yoneda, give morphisms
\[
 +:J\times_kJ\longrightarrow J,\qquad
 -:J\longrightarrow J,\qquad 0:\operatorname{Spec}k\longrightarrow J .
 \tag{JC16}
\]
Associativity, commutativity, identity and inverse hold on every parameter scheme because they hold for tensor products of rigidified lines. They are therefore equalities of scheme morphisms. Thus \(J\) is a smooth proper geometrically connected group of dimension \(g\), an abelian variety; CU7 supplies its projectivity and a symmetric ample line, without making projectivity an extra hypothesis.

Translating the universal line on \(J_g\) gives a line \(\mathscr L\) on \(C\times J\), trivialized along \(P\times J\), whose fibre at \(0\) is the trivial rigidified line. For every \(T\),
\[
 \operatorname{Hom}_k(T,J)\xrightarrow{\sim}\mathcal P_0(T),\qquad
 u\longmapsto(\operatorname{id}_C\times u)^*\mathscr L .
 \tag{JC17}
\]
The construction so far proves this over separably closed fields, including imperfect ones. We next descend the scheme and this full universal property. \(\square\)
#### 2K.7. Descent over an arbitrary field

**JC7.** Return to arbitrary \(k\), still with \(P\in C(k)\), and put \(k_s=k^{\mathrm{sep}}\). The construction over \(k_s\) gives a projective \(J_s\), its group morphisms and its rigidified universal line. These data descend to some finite separable extension \(E/k\), enlarged to be Galois.

Here is why finite descent uses no assumption on characteristic. Choose projective equations for \(J_s\), finite affine covers for its finite products, and finite affine descriptions of the group maps and the line on \(C_{k_s}\times J_s\). Transition maps, their inverses, rigidity maps, identity diagrams and witnesses for the covers involve finitely many coefficients. Include all these coefficients in \(E\). Every coefficient of \(k_s\) lies in a finite separable extension, and a finite list lies in one finite separable extension. The same equations and identities then hold over \(E\), since they already hold after its faithful field extension to \(k_s\). This is the finite-equation proof used in JC1, now applied to the projective presentation and its finite auxiliary data. In particular we obtain a projective \(J_E\) and a rigidified line \(\mathscr L_E\) whose base changes are the specified \(J_s,\mathscr L_s\).

They represent \(\mathcal P_0\) already over \(E\). We spell out detection after \(k_s/E\). This field extension is an affine faithfully flat universally open cover. To verify the last property, for any \(E\)-algebra \(A\) a basic open in
\[
 \operatorname{Spec}(A\otimes_E k_s)
 \tag{JC18}
\]
is defined by an element with coefficients in a finite separable intermediate extension \(E'/E\). Its image is the same as the image of the corresponding basic open in \(\operatorname{Spec}(A\otimes_E E')\), since further field extension is faithfully flat and surjective. The latter map is finite locally free and open by FF1. Unions of basic opens prove universal openness. The extension of FD5 proved in FF1 therefore descends scheme morphisms along this cover.

Given any rigidified line on \(C_T\), its pullback to \(T_{k_s}\) gives a unique morphism to \((J_E)_{k_s}=J_s\) by JC6. On the double overlap the two pullbacks agree, since the represented rigidified line agrees and (JC17) holds on all \(k_s\)-schemes. Morphism descent gives \(T\to J_E\). The line obtained by pulling back \(\mathscr L_E\) equals the original line after the cover, hence before it by JC2. Uniqueness is detected after the same cover. Thus \(J_E,\mathscr L_E\) have the claimed universal property over \(E\).

Write \(\Gamma=\operatorname{Gal}(E/k)\). For \(\sigma\in\Gamma\), the conjugate of \(J_E,\mathscr L_E\) represents the same functor, because \(C,P\) are defined over \(k\). Yoneda gives a unique isomorphism between the two representing objects. Composition gives the cocycle identity by uniqueness. The universal rigidified lines also have unique compatible isomorphisms. It remains to make this descent datum effective as a scheme; no quotient by geometric points suffices.

The underlying \(k\)-scheme \(J_E\) is projective: it is closed in \(\mathbf P^n_E\), and the finite map \(\mathbf P^n_E\to\mathbf P^n_k\), together with the finite-cover projectivity proof in Lesson 3, supplies projectivity over \(k\). Each finite \(\Gamma\)-orbit has an affine open neighbourhood by homogeneous avoidance QS1. One may choose closed specializations of any nonclosed orbit points first; an open containing a specialization contains its generizations. Intersect the finitely many translates of such a neighbourhood. The intersection is affine, since in a separated \(k\)-scheme the intersection of two affine opens is the closed inverse image of the diagonal in their affine product. We obtain \(\Gamma\)-stable affine opens \(V=\operatorname{Spec}B\) covering \(J_E\).

On each one, the semilinear action is an algebra descent datum: the field identity \(E\otimes_kE\simeq\prod_{\sigma\in\Gamma}E\) of Lesson 1 turns its cocycle into the ordinary affine descent cocycle. FD2–FD3 give
\[
 D=B^\Gamma,\qquad E\otimes_kD\xrightarrow{\sim}B .
 \tag{JC19}
\]
Thus \(V\to\operatorname{Spec}D\) is the base change of the finite étale cover \(\operatorname{Spec}E\to\operatorname{Spec}k\). No division by \(|\Gamma|\) is used. The images of stable overlaps are open: their complements are stable closed subsets of \(V\), whose images are closed under this finite map; the inverse images of those images are exactly the complements. Indeed \(\Gamma\) acts transitively on the points of each fibre, as follows by splitting \(E\otimes_k\kappa\) over an algebraic closure of \(\kappa\) and permuting the embeddings of \(E\). The overlap morphisms descend by FD5, and their inverse and triple identities descend too. Glue the \(\operatorname{Spec}D\)'s on these opens to obtain \(J/k\) with
\[
 J\times_kE\simeq J_E .
 \tag{JC20}
\]
Finite presentation descends by FD4, and the closed diagonal by FD6. Smoothness is detected after the field extension by the standard smooth-chart and fibre argument SF1–SF3 and QS6. Geometric integrality follows after embedding \(E\) into an algebraic closure. For any \(T\) and closed subset of \(J_T\), pull it back to \((J_E)_T\); properness of \(J_E\) over \(k\) and surjectivity of the finite cover show that its image in \(T\) is closed. Hence \(J\) is proper. The group maps descend by FD5, and their identities do also. It is therefore an abelian variety of dimension \(g\), projective by CU7.

FD2–FD4 descend the universal line on \(C\times J_E\) and its rigidification; the unique rigidified isomorphisms give its descent cocycle. The sheaf property JC2 and finite-cover morphism descent FD5 detect (JC17) after \(E/k\), so (JC17) holds over the original field for every \(T\). Tensoring with
\[
 A_d=\mathcal O_C(dP)^\natural
 \tag{JC21}
\]
represents every \(\mathcal P_d\) by a translated copy \(J_d\) of \(J\). Degree is locally constant by CE3 and DC6, so \(\coprod_{d\in\mathbf Z}J_d\) represents the whole rigidified Picard functor. This proves representability and the universal line over arbitrary fields with the specified rational point.

If the original curve has no rational point, it has one after a finite separable extension: a smooth chart over \(k_s\) gives a \(k_s\)-point as in JC4, and its finitely many coordinates lie in a finite separable extension. The pointed construction is therefore available after such an extension. We have not identified the unpointed relative Picard sheaf over \(k\) with the raw quotient (JC6) on every \(k\)-scheme without a section. \(\square\)

#### 2K.8. The high-degree Abel map is a projective bundle

**JC8.** Let \(d\ge\max(0,2g-1)\). Use (JC17) and (JC21) to put the universal degree-\(d\) line \(L_d\) on \(C\times J\). Duality SD1–SD7 gives, on every geometric fibre,
\[
 H^1(C_{\bar t},(L_d)_{\bar t})^\vee
 =H^0(C_{\bar t},\omega_C\otimes(L_d)_{\bar t}^{-1})=0,
 \qquad h^0=d+1-g .
 \tag{JC22}
\]
The vanishing holds because \(2g-2-d<0\); a negative-degree line has no nonzero section. By FC15,
\[
 E_d=\pi_*L_d\quad\text{is locally free of rank }d+1-g,
 \quad (E_d)_T\simeq(\pi_T)_*(L_d)_T
 \tag{JC23}
\]
for every \(T\to J\).

Let \(\mathbf P_{\mathrm{lines}}(E_d)\) parameterize rank-one subbundles \(M\hookrightarrow(E_d)_T\) whose quotients are locally free. This is a scheme: on a trivializing open for the rank-\(r\) bundle, glue the \(r\) affine spaces with coordinates \(v_j/v_i\), where the \(i\)-th coordinate of a local generator is a unit. On overlaps the ratios change by the invertible basis matrices of \(E_d\). A locally split rank-one submodule is locally represented by such a vector, and vectors differing by a unit give the same line. This verifies the representing property and gives the usual projective-space bundle with fibre \(\mathbf P^{r-1}\).

Evaluation sends a line subbundle to a section of
\[
 (L_d)_T\otimes\pi_T^*M^{-1}.
 \tag{JC24}
\]
On every fibre its vector of sections is nonzero. JC1 gives a finite locally free divisor of degree \(d\), whose rigidified line is \((L_d)_T\): tensoring by the base line \(M^{-1}\) disappears under normalization. Conversely, for a divisor \(D\) representing this degree-\(d\) class, the unique rigidified isomorphism gives
\[
 \mathcal O(D)\simeq(L_d)_T\otimes\pi_T^*N,\qquad
 N=P_T^*\mathcal O(D).
 \tag{JC25}
\]
The canonical divisor section gives a map \(N^{-1}\to(E_d)_T\). Its vector is nonzero in each residue field, so locally some coordinate is a unit. Elementary row operations then split this inclusion with a locally free quotient. Its image is the required line subbundle. Changing local generators does not change it.

The two constructions are inverse: a section of a line has the same zero ideal under these identifications, and the associated section line is recovered from the canonical divisor section. They commute with every base change by JC1 and (JC23). Therefore, as schemes over \(J\),
\[
 S_d(C)\xrightarrow{\sim}\mathbf P_{\mathrm{lines}}(E_d),\qquad
 b_d(D)=\bigl[\mathcal O(D-dP)^\natural\bigr].
 \tag{JC26}
\]
In particular \(b_d\) is smooth and surjective of relative dimension \(d-g\), with Zariski local sections: on each trivializing open choose a coordinate line. This includes \(g=d=0\), with a rank-one bundle and zero-dimensional fibre. \(\square\)

#### 2K.9. Tangents and the differential of the Abel map

**JC9.** There is a natural identification
\[
 T_0J\simeq H^1(C,\mathcal O_C).
 \tag{JC27}
\]
To prove it, a rigidified degree-zero line over \(k[\epsilon]/(\epsilon^2)\), with specified reduction to the identity, is trivial on each member of an affine cover of \(C\). Indeed a basis of its reduction lifts on an affine, and Nakayama with nilpotent ideal makes that lift a basis. Its transition functions have form \(1+\epsilon c_{ij}\). The cocycle and change-of-basis equations are
\[
 c_{ij}+c_{jk}=c_{ik},\qquad
 c_{ij}\longmapsto c_{ij}+b_j-b_i .
 \tag{JC28}
\]
Affine Čech cohomology SC1–SC12 thus identifies their classes with \(H^1(C,\mathcal O_C)\). The rigidification does not change those classes: after gluing any representative, its value along \(P\) can be normalized by multiplying by a scalar \(1+\epsilon b\); any two such choices are isomorphic by that scalar. Addition of lines adds cocycles, and replacing \(\epsilon\) by \(a\epsilon\) multiplies them by \(a\), proving the vector-space identification. Its dimension is \(g\), agreeing with the constructed smooth charts.

For an effective divisor \(D\) of degree \(n\), DR5 identifies the divisor tangent space with \(H^0(D,\mathcal O_D(D))\). The differential of the Abel map at \(D\) is the connecting map
\[
 H^0(D,\mathcal O_D(D))\xrightarrow{\ \delta\ }H^1(C,\mathcal O_C)
 \tag{JC29}
\]
in the sequence \(0\to\mathcal O_C\to\mathcal O_C(D)\to\mathcal O_D(D)\to0\). To check its sign with the Čech boundary convention, write the local equations as \(f_i\), and a deformation as \(f_i+\epsilon h_i\). The bases \(1/f_i\) of \(\mathcal O(D)\) have transition functions \(f_j/f_i\). Their deformations differ by
\[
 \frac{f_j+\epsilon h_j}{f_i+\epsilon h_i}
 =\frac{f_j}{f_i}
   \left(1+\epsilon\left(\frac{h_j}{f_j}-\frac{h_i}{f_i}\right)\right).
 \tag{JC30}
\]
The ratios \(h_i/f_i\) lift the corresponding principal parts in \(\mathcal O_D(D)\), and their difference is exactly the Čech boundary in (JC29). This calculation also respects normalization at \(P\), since multiplying a line by a base line changes no class in (JC27).

If \(D\in U\) has degree \(g\), then \(H^0(\mathcal O_C)\to H^0(\mathcal O_C(D))\) is an isomorphism and \(H^1(\mathcal O_C(D))=0\). The long exact sequence makes (JC29) an isomorphism, explaining the degree-\(g\) chart. For \(n\ge\max(0,2g-1)\), its kernel has dimension \(n-g\), the relative dimension of (JC26).

We have constructed the Jacobian and the full divisor maps, not yet the Albanese factorization for maps from \(C\) to other abelian varieties. That factorization, and the geometric construction of the initial semistable period cover, require their own arguments. \(\square\)

#### 2K.10. Graded exercise: the Jacobian on nilpotent families

**Exercise 2K (100 points; ten parts of 10 points).** Use the constructions JC1–JC9, rather than a classification by geometric points.

1. Compute \(J(\mathbf P^1_k)\), its degree-\(d\) components, and the Abel map for \(d\ge0\).
2. Let \(R=\mathbf F_p[\epsilon]/(\epsilon^3)\) and consider the normalized degree-zero cohomology model
   \[
    [Re\xrightarrow{d}R^2],\qquad d(e)=(\epsilon,\epsilon^2),
    \qquad \operatorname{ev}_P(e)=1.
    \tag{JCX1}
   \]
   Find its kernel, its normalized trivialization locus, and its reductions to \(R/(\epsilon^2)\) and \(\mathbf F_p\). State exactly what this algebraic model does and does not prove geometrically.
3. On \(\mathbf P^1\), let \(D=P\). Explain why (JC8) is defined even though the canonical divisor section is zero at \(P\).
4. Over \(R=k[\epsilon]/(\epsilon^2)\), compare the sections \(x^2-\epsilon\) and \(\epsilon\) of the trivial line on \(\mathbf A^1_R\). Check regularity and flatness on arbitrary coefficient modules where applicable.
5. Replace (JCX1) by \(d(e)=(\epsilon^2,0)\). Compute the normalized locus and the base-change map on \(H^0\) to the residue field. Explain why constancy of geometric fibre dimensions would lose information.
6. In the translation argument take \(g=4\), \(\deg H=3\) and \(m=2\), assuming the twist has \(H^1=0\). How many points are subtracted, what are all the degrees and section dimensions, and why may they be chosen over the separably closed ground field even for a transcendental extension field?
7. For \(g=3,d=5\), compute the Abel fibre, the bundle rank and the dimensions. Give two overlapping projective-bundle charts and a valid nilpotent section vector over \(\mathbf F_p[\epsilon]/(\epsilon^3)\). Contrast a vector whose coordinates are all nilpotent.
8. Calculate the differential of the Abel map at a nonspecial degree-\(g\) divisor, and its kernel for high degree \(d\). Check the transition-function sign in (JC30).
9. Let \(\operatorname{char}k\ne2\), \(E=k(\theta)\) with \(\theta^2=a\in k^\times\) nonsquare, and \(B=E[z]\). Give \(B\) the semilinear involution \(\sigma(\theta)=-\theta,\sigma(z)=-z\). Compute its invariant algebra and the descent isomorphism. Explain why this is an affine descent example, rather than a construction of a Jacobian.
10. If \(g=1\), prove that \(Q\mapsto[\mathcal O(Q-P)^\natural]\) is an isomorphism \(C\to J\) of pointed schemes. State the corresponding identity for the degree components and their group operation.

**Full solution.**

1. The two-affine Čech calculation gives \(H^1(\mathbf P^1,\mathcal O)=k[x,x^{-1}]/(k[x]+k[x^{-1}])=0\). Thus \(g=0\). Every degree-zero line over a field is trivial by Riemann–Roch: it has a nonzero section and an effective degree-zero zero divisor. In the construction \(U=S_0\) is a point and there is consequently only one translating class. This proves the full family assertion \(J_0=\operatorname{Spec}k\), rather than just a statement about field points. Tensoring with \(\mathcal O(d)^\natural\) gives all degree components; in particular \(\operatorname{Pic}(\mathbf P^1_k)=\mathbf Z[\mathcal O(1)]\). Thus
   \[
    J_0=\operatorname{Spec}k,\qquad J_d\simeq\operatorname{Spec}k,\qquad
    E_d=H^0(\mathbf P^1,\mathcal O(d))\simeq k^{d+1}.
    \tag{JCX2}
   \]
   Tensoring with the one-dimensional normalization factor changes none of the vector-space ranks. JC8 gives \(S_d(\mathbf P^1)\simeq\mathbf P^d_k\), and its Abel map is the structure map to \(J_d\). This agrees with the homogeneous polynomial construction in Exercise 2J.

2. Write \(r=r_0+r_1\epsilon+r_2\epsilon^2\). Then
   \[
    d(re)=(r_0\epsilon+r_1\epsilon^2,r_0\epsilon^2),\qquad
    \ker d=(\epsilon^2)e .
    \tag{JCX3}
   \]
   A normalized section has coefficient \(1\), not an arbitrary nonzero element of this kernel. It is a cycle only after the coefficients \(\epsilon,\epsilon^2\) vanish. The normalized locus is therefore
   \[
    \operatorname{Spec}R/(\epsilon,\epsilon^2)
      =\operatorname{Spec}\mathbf F_p .
    \tag{JCX4}
   \]
   Over \(R/(\epsilon^2)\) the differential is \((\epsilon,0)\), its kernel is \((\epsilon)e\), and its normalized locus is again the residue field. Over the residue field the differential is zero, its kernel is the whole one-dimensional space, and \(e\) is normalized. Each residue-field observation sees a trivialization, while the actual ring equations exclude one over \(R\). This is an exact finite-complex model of JC5's normalized-cycle calculation. It does not by itself assert that this particular complex is the cohomology of a specified geometric family.

3. If \(x\) is a uniformizer at \(P\), \(\mathcal O(P)\) has local basis \(1/x\). Its canonical section is
   \[
     1=x(1/x).
     \tag{JCX5}
   \]
   Its fibre value is zero, but \(P^*\mathcal O(P)\) is the one-dimensional module with basis the class of \(1/x\). Tensoring by the pullback of that module's inverse makes sense. It requires neither a nonzero value of the section nor division by \(x\) in the residue field. This is exactly why (JC8) uses a line and its inverse.

4. For every \(R\)-module \(N\), multiplication by the monic polynomial \(x^2-\epsilon\) is injective on \(N[x]\): the highest nonzero coefficient of a nonzero polynomial remains its highest coefficient, shifted by degree two. Monic division also works with coefficients in \(N\), so
   \[
    N[x]/(x^2-\epsilon)N[x]\simeq N\oplus Nx.
    \tag{JCX6}
   \]
   In particular its zero algebra is free of rank two over \(R\), with multiplication \(x^2=\epsilon\); over \(k\) its dimension is four, rather than two. Its special fibre has length two and a double point. In contrast \(\epsilon\) is killed by \(\epsilon\), and is zero on the special fibre. Its quotient algebra is \(k[x]\), which is not \(R\)-flat: tensoring \((\epsilon)\hookrightarrow R\) with \(k[x]\) gives a nonzero source mapped to zero. This second section fails the nonzero-fibre hypothesis of JC1.

5. Now
   \[
    \ker d=(\epsilon)e,\qquad
    \text{normalized locus}=\operatorname{Spec}R/(\epsilon^2).
    \tag{JCX7}
   \]
   The module \((\epsilon)\) has length two over \(R\); its tensor with the residue field is one-dimensional, represented by \(\epsilon e\) modulo \(\epsilon^2e\). The base-change map sends that class to zero in the one-dimensional kernel of the zero residue-field differential. It is not an isomorphism. Every geometric point is nevertheless the same residue point, and sees \(h^0=1\). The equation \(\epsilon^2=0\) describes a larger infinitesimal locus than \(\epsilon=0\); geometric points cannot distinguish them.

6. The twist has degree \(4+2\cdot3=10\), hence \(h^0=10+1-4=7\). Subtract six points where successive nonzero sections do not vanish. After \(j\) subtractions,
   \[
    \deg L_j=10-j,\qquad h^0(L_j)=7-j,\qquad H^1(L_j)=0
       \quad(0\le j\le6).
    \tag{JCX8}
   \]
   The final line has degree four and exactly one section. The translating bundle is
   \[
     M=\mathcal O(Q_1+\cdots+Q_6)\otimes H^{-2},
     \qquad \deg M=6-6=0 .
     \tag{JCX9}
   \]
   Infinitely many \(k\)-rational points remain distinct over the extension field. Any given nonzero section on the integral extension curve vanishes at only finitely many of them, so a suitable next point always exists over \(k\). No descent of the original extension-field line is required.

7. Here \(d+1-g=3\), so the Abel fibre is \(\mathbf P^2\); \(J\) has dimension three and \(S_5(C)\) has dimension five. On a trivializing open for \(E_5\), let \(v=(v_0,v_1,v_2)\). The charts with \(v_0\) and \(v_1\) invertible have coordinates
   \[
     (u,w)=(v_1/v_0,v_2/v_0),\qquad
     (u',w')=(v_0/v_1,v_2/v_1)=(u^{-1},w/u)
     \quad(u\text{ invertible}).
     \tag{JCX10}
   \]
   The vector \((1,\epsilon,\epsilon^2)\) spans a direct summand over the specified nilpotent ring; its quotient is free of rank two, and JC8 gives a divisor family. The vector \((\epsilon,\epsilon^2,0)\) reduces to zero and spans no line subbundle. Calling it nonzero as a vector over the ring does not make it an admissible projective-bundle point.

8. The exact sequence gives
   \[
    0\to k\to H^0(C,\mathcal O(D))
      \to H^0(D,\mathcal O_D(D))
      \xrightarrow{\delta}H^1(C,\mathcal O_C)
      \to H^1(C,\mathcal O(D))\to0 .
    \tag{JCX11}
   \]
   At a nonspecial degree-\(g\) divisor the first nontrivial map is an isomorphism \(k\to k\) and the final term is zero; consequently \(\delta\) is an isomorphism of \(g\)-dimensional spaces. In high degree it is surjective, with
   \[
       \ker\delta=H^0(C,\mathcal O(D))/k,\qquad
       \dim\ker\delta=d-g.
       \tag{JCX12}
   \]
   Expanding the quotient of the equations gives \(h_j/f_j-h_i/f_i\), the boundary with convention \(a_j-a_i\); replacing it by its negative while keeping that convention would change the differential sign.

9. Write a polynomial as \(\sum c_nz^n\), with \(c_n=b_n+d_n\theta\), \(b_n,d_n\in k\). Invariance requires \(c_n=(-1)^n\sigma(c_n)\). Thus \(c_n\in k\) for even \(n\) and \(c_n\in k\theta\) for odd \(n\). For \(w=\theta z\), both kinds of invariant monomials are \(k\)-multiples of powers of \(w\), since \(a\) is invertible. Therefore
   \[
     B^\Gamma=k[w],\qquad
     E\otimes_k k[w]\xrightarrow{\sim}E[z],\qquad
     w\longmapsto\theta z,\quad z\longmapsto\theta^{-1}w .
     \tag{JCX13}
   \]
   The last map denotes the inverse substitution. This verifies algebra descent, including its full ring structure. The affine line in this example is not a proper variety, and no curve Picard universal property was specified for it, so it is not a Jacobian example.

10. Duality gives \(\deg\omega_C=0\); for every degree-one line \(L\), the line \(\omega_C L^{-1}\) has degree \(-1\), so \(H^1(L)=0\). Hence \(U=S_1(C)=C\). JC3 identifies this entire scheme with \(J_1\), and tensoring by \(\mathcal O(-P)^\natural\) identifies \(J_1\) with \(J\). This is an isomorphism on all schemes, with \(P\) sent to the identity. Its group law is characterized by tensor product:
    \[
      [\mathcal O(Q-P)^\natural]+[\mathcal O(R-P)^\natural]
        =[\mathcal O(Q+R-2P)^\natural].
      \tag{JCX14}
    \]
    More generally tensor product sends \(J_d\times J_e\) to \(J_{d+e}\). These are morphisms of the represented functors, not just rules on rational points. \(\square\)

### 2L. Albanese maps and norms of curve line bundles

The Jacobian \(J_C\) of the pointed curve \((C,P)\) represents rigidified degree-zero lines by JC1–JC9. We now prove its mapping property and the functorial maps needed when curves are related by finite morphisms. All curves in this section are smooth, projective and geometrically integral over a field \(k\). All abelian varieties are over \(k\).

Write
\[
 i_P:C\longrightarrow J_C,\quad
 R\longmapsto[\mathcal O_C(R-P)^\natural],\qquad
 q_d:S_d(C)\longrightarrow J_C,\quad
 D\longmapsto[\mathcal O_C(D-dP)^\natural].
 \tag{AL1}
\]
These are morphisms defined by the universal divisor lines, including families of points. For \(d\ge\max(0,2g-1)\), JC8 identifies \(q_d\) with a projective-space bundle having Zariski local sections.

Free primary comparisons are Milne's author version of [*Jacobian Varieties*, §6, Proposition 6.1](https://www.jmilne.org/math/xnotes/JVs.pdf) and the Stacks project's [norm construction](https://stacks.math.columbia.edu/tag/0BCX). We use a projective-bundle argument with full parameter schemes, rather than import extension of rational maps as an additional theorem. The norm and infinitesimal calculations below are also proved here.

#### 2L.1. The finite torsors used on the projective line

**AL1.** Over an algebraically closed field \(K\), every finite locally free torsor on \(\mathbf P^1_K\) under \(\mu_\ell^r\), with \(\ell\) prime to the characteristic, has a section.

A finite locally free torsor here means a finite faithfully flat map \(X\to\mathbf P^1_K\) with the group action and an isomorphism \(\mu_\ell^r\times X\simeq X\times_{\mathbf P^1}X\) given by the action and projection. The cover \(X\) itself then trivializes the torsor. Write its finite algebra as \(\mathcal B\). The diagonalizable-group coaction gives an actual grading
\[
 \mathcal B=\bigoplus_{\chi\in(\mathbf Z/\ell)^r}\mathcal B_\chi,\qquad
 \mathcal B_0=\mathcal O_{\mathbf P^1},\qquad
 \mathcal B_\chi\otimes\mathcal B_\psi\xrightarrow{\sim}
                         \mathcal B_{\chi+\psi}.
 \tag{AL2}
\]
Indeed expand the coaction in the basis of the character group algebra. Its counit and coassociativity say that these coefficients are orthogonal projections with sum the identity. On a trivializing cover their images are the rank-one character summands of the group algebra, and the multiplication maps are isomorphisms there. Their being invertible modules and the displayed maps' being isomorphisms descend faithfully by FD1–FD4. This proves (AL2) without choosing points of the torsor.

For a coordinate character \(e_j\), multiplication gives \(\mathcal B_{e_j}^{\otimes\ell}\simeq\mathcal O\). Exercise 2K proved \(\operatorname{Pic}(\mathbf P^1_K)=\mathbf Z[\mathcal O(1)]\), so \(\mathcal B_{e_j}\) is trivial. Choose a global basis \(u_j\). Its \(\ell\)-th power is a unit \(c_j\in K^\times\), since global functions on \(\mathbf P^1_K\) are \(K\). Rescale using an \(\ell\)-th root of \(c_j\). The multiplication isomorphisms in (AL2) show that the monomials in the \(u_j\), with exponents between zero and \(\ell-1\), are bases of all character summands. Thus
\[
 \mathcal B\simeq
 \mathcal O_{\mathbf P^1}[u_1,\ldots,u_r]/
                (u_1^\ell-1,\ldots,u_r^\ell-1).
 \tag{AL3}
\]
Evaluation \(u_j\mapsto1\) is an algebra retraction and gives the required section. This also covers \(r=0\). \(\square\)

#### 2L.2. No rational curves in an abelian variety

**AL2.** Every morphism \(\mathbf P^s_k\to A\) is constant, for \(s\ge0\).

First take \(s=1\) over an algebraic closure \(K\), and choose a prime \(\ell\ne\operatorname{char}K\). CU8–CU9 identifies the finite étale group \(A[\ell]\) with the constant group \((\mathbf Z/\ell)^{2a}\), where \(a=\dim A\). Choosing a primitive \(\ell\)-th root identifies it with \(\mu_\ell^{2a}\). Multiplication \([\ell]:A\to A\) is a torsor under its kernel: for every base scheme, two points with the same multiple differ uniquely by a kernel point, so
\[
 A[\ell]\times A\xrightarrow{\sim}A\times_{[\ell],A,[\ell]}A,
 \qquad (h,x)\longmapsto(x+h,x).
 \tag{AL4}
\]
The map \([\ell]\) is faithfully flat by CU8 and trivializes its own torsor. Pulling it back along \(f:\mathbf P^1_K\to A\) gives the torsor in AL1. A section supplies a lift \(f_1\) with \([\ell]f_1=f\). Repeat to obtain \(f_n\) with \([\ell^n]f_n=f\).

Let \(H\) be a symmetric ample line on \(A\), supplied by CU7. CU5 gives \([\ell^n]^*H\simeq H^{\otimes\ell^{2n}}\), up to a constant one-dimensional factor which has degree zero on a curve. Therefore
\[
 \deg f^*H=\ell^{2n}\deg f_n^*H\qquad(n\ge1).
 \tag{AL5}
\]
The left side is a nonnegative integer divisible by arbitrarily large powers of \(\ell\), hence zero. A nonconstant \(f\) would give positive degree: choose a very ample power of \(H\), and a hyperplane containing one image point but not another. Its pulled-back section has a nonempty effective zero divisor, so has positive degree by DC4. This contradiction proves constancy.

Any two \(K\)-points of \(\mathbf P^s_K\) lie on a line, so the result for \(s=1\) makes their images equal. The closed equalizer with the constant map at a chosen point is the whole scheme: on each affine chart, its defining functions vanish at every closed point; B1's closed-point detection and reducedness make those functions zero. Constancy over \(k\) follows by faithful scalar extension, with constant value the image of a \(k\)-point of \(\mathbf P^s_k\). Dimension zero is immediate. \(\square\)

#### 2L.3. Factoring families through a projective-space bundle

**AL3.** Let \(B\) be any \(k\)-scheme, \(E\) a vector bundle of positive rank on \(B\), and \(\pi:\mathbf P_{\mathrm{lines}}(E)\to B\). Every morphism \(F:\mathbf P_{\mathrm{lines}}(E)\to A\) has a unique factorization through \(\pi\), including when \(B\) is nonreduced.

Work on an affine open \(V\subset B\) trivializing \(E\), and choose a coordinate section \(s:V\to\mathbf P^{r-1}_V\). Put \(a=Fs\), and subtract it using the group law:
\[
 G=F-a\pi:\mathbf P^{r-1}_V\longrightarrow A.
 \tag{AL6}
\]
On every geometric fibre, AL2 makes \(F\) constant; its value is the value at \(s\). Hence \(G\) has value zero on every geometric fibre. Its topological image lies in the origin of \(A\), so it factors through any affine open \(W\subset A\) containing the origin. This says only that its image lies in \(W\), not that the morphism is already zero.

FC20 applied to the proper flat scheme \(\mathbf P^{r-1}_V\) gives the actual ring equality
\[
 \Gamma(\mathbf P^{r-1}_V,\mathcal O)=\Gamma(V,\mathcal O),
 \tag{AL7}
\]
also for nonreduced \(V\). Since \(W\) is affine, the map into \(W\) factors through \(V\). Its restriction to \(s\) is the zero morphism, so that factor and \(G\) are zero as scheme morphisms. Thus \(F=a\pi\). The factors on different trivializing opens agree: on an overlap they become equal after \(\pi\), and \(\pi\) has local sections. They glue uniquely. The same argument proves compatibility with every base change on \(B\).

Notice that the factor \(a\) can be a nonzero infinitesimal family through the origin even when all its geometric fibres are zero. Subtracting \(a\), and then using (AL7), is the step which retains that information. \(\square\)

#### 2L.4. Symmetric maps over parameter rings

**AL4.** For every \(k\)-scheme \(T\), a permutation-invariant morphism \((C^d)_T\to Z\) into a \(T\)-scheme factors uniquely through \(S_d(C)_T\).

On an affine curve open \(V\), DR7 gives \(S_d(V)=\operatorname{Spec}D\), with
\[
 A=\mathcal O(V)^{\otimes_kd},\qquad
 D=A^{\mathfrak S_d}
   =\ker\left(A\longrightarrow\bigoplus_{\gamma\in\mathfrak S_d}A,\ 
                         a\longmapsto(\gamma a-a)_\gamma\right).
 \tag{AL8}
\]
For \(T=\operatorname{Spec}R\), tensoring over the field \(k\) is exact. Hence
\[
 (A\otimes_kR)^{\mathfrak S_d}=D\otimes_kR.
 \tag{AL9}
\]
The same assertion holds on affine subopens of the quotient by localization at invariant functions. The ordered cover is finite faithfully flat, with geometric fibres the permutation orbits. Consequently a stable open in its source is saturated and descends to an open in the quotient: the complement has closed image under the finite map, and its inverse image is exactly that complement. For an invariant map into \(Z\), apply this to inverse images of affine target opens. On affine subopens of their quotient opens, (AL9) factors the coordinate maps. Uniqueness glues these factorizations. Curve opens \(V\) covering the finite supports, as in DR4, give the global assertion. Affine opens in \(T\) then give it for arbitrary \(T\).

This proof extends the ground field to the parameter ring \(R\); it does not assert that invariants commute with arbitrary restriction to a subscheme of \(S_d(C)\). In characteristic dividing \(d!\), that latter assertion can fail, as the exercise shows. \(\square\)

#### 2L.5. The Albanese homomorphism, on full parameter schemes

**AL5.** For every \(k\)-scheme \(T\) and abelian variety \(A/k\), restriction along \(i_P\) gives a natural bijection
\[
 \operatorname{Hom}_{T\text{-groups}}((J_C)_T,A_T)
 \xrightarrow{\sim}
 \{f:C_T\to A_T:\ fP_T=0_T\}.
 \tag{AL10}
\]
The equality at \(P_T\) is an equality of scheme morphisms.

Choose \(d\ge\max(1,2g-1)\). For a pointed \(f\) on the right, form the symmetric sum of its values on \((C^d)_T\). AL4 supplies \(h_d\) and JC8 supplies the indicated projective bundle:
\[
 (C^d)_T\xrightarrow{\sigma_d}S_d(C)_T
       \xrightarrow{q_d}(J_C)_T,\qquad
 h_d\sigma_d(R_1,\ldots,R_d)=\sum_{j=1}^d f(R_j).
 \tag{AL11}
\]
Regard \(h_d\) as a map to \(A\) together with its fixed map to \(T\). AL3 gives a unique \(T\)-morphism \(\phi_d:(J_C)_T\to A_T\) with \(h_d=\phi_dq_d\).

Insert \(R+(d-1)P\) as a family of divisors. Its class under \(q_d\) is \(i_P(R)\), and its value under \(h_d\) is \(f(R)\). The divisor \(dP\) similarly shows \(\phi_d(0_T)=0_T\). These identities are identities of line bundles and morphisms on all families. They do not rely on density of rational points.

To prove that \(\phi_d\) is a homomorphism, perform the construction with \(2d\). Adding the fixed divisor \(dP\) gives \(j:S_d(C)_T\to S_{2d}(C)_T\), with
\[
 q_{2d}j=q_d,\qquad h_{2d}j=h_d,\qquad
 \phi_{2d}q_d=\phi_dq_d.
 \tag{AL12}
\]
The first equality is tensoring the divisor lines. The second is checked after the finite faithfully flat ordered cover, where it says that adding \(d\) values \(f(P)=0\) changes no sum; equality then descends by FD5. Since \(q_d\) has local sections, the third equality gives \(\phi_{2d}=\phi_d\) as morphisms.

For addition of divisors \(a:S_d(C)_T\times_T S_d(C)_T\to S_{2d}(C)_T\), the same reasoning gives
\[
 q_{2d}a=+\,(q_d\times q_d),\qquad
 h_{2d}a=h_d\operatorname{pr}_1+h_d\operatorname{pr}_2.
 \tag{AL13}
\]
Consequently the two group-law expressions for \(\phi_d\) become equal after \(q_d\times q_d\), which also has local sections. They are equal before that cover. Thus \(\phi_d\) is a group homomorphism, with \(\phi_di_P=f\).

If \(\psi\) is any other such homomorphism, the actual divisor-line identity
\[
 q_d\sigma_d=\sum_{j=1}^d i_P\operatorname{pr}_j
 \tag{AL14}
\]
gives \(\psi q_d\sigma_d=h_d\sigma_d=\phi_dq_d\sigma_d\). Cancel the finite faithfully flat cover \(\sigma_d\) by FD5 and then \(q_d\) using its local sections. This proves uniqueness. It also proves independence of \(d\), naturality under every \(T'\to T\), and compatibility with homomorphisms of the target.

An arbitrary \(f:C_T\to A_T\) has the unique form
\[
 f(R)=a+\phi i_P(R),\qquad a=f(P_T),\qquad
 \phi:(J_C)_T\to A_T\text{ a group homomorphism}.
 \tag{AL15}
\]
Subtract \(a\) and apply (AL10). If \(Q\) is another rational base point, the Picard quotient (JC6) canonically identifies the two Jacobians, and
\[
 i_Q(R)=i_P(R)-i_P(Q).
 \tag{AL16}
\]
The same \(\phi\) occurs in (AL15); the new constant is \(f(Q)\). Thus changing the base point changes the translation, not the homomorphism. \(\square\)

#### 2L.6. Norms for a finite morphism of curves

**AL6.** Let \(u:(C,P)\to(D,Q)\) be a nonconstant pointed morphism. It is finite locally free of a positive degree \(m\). For every parameter scheme \(T\), its base change has a norm operation on line bundles,
\[
 N_u(L)=\det (u_T)_*L\otimes
                     \bigl(\det (u_T)_*\mathcal O_{C_T}\bigr)^{-1}.
 \tag{AL17}
\]
It commutes with arbitrary base change, is multiplicative, and satisfies
\[
 N_u(u_T^*M)\simeq M^{\otimes m},\qquad
 N_u(\pi_C^*B)\simeq\pi_D^*(B^{\otimes m})
 \tag{AL18}
\]
for lines \(M\) on \(D_T\) and \(B\) on \(T\).

We justify every finiteness and module assertion used here. The nonconstant map is dominant; after extending the field, a fibre containing a curve component would make the map constant on the geometrically integral source. Its geometric fibres are therefore finite. It is proper, so the proved proper finite-fibres theorem makes it finite. On a target local DVR its finite algebra is torsion-free: a nonzero target function is a nonzero function on the integral source and cannot annihilate a nonzero element. The DVR module theorem of Lesson 1 makes it free. Its rank is the function-field degree \(m\). This proves finite local freeness and preserves it under every base change.

Here is a useful elementary observation about any finite locally free algebra \(B/R\) and invertible \(B\)-module \(L\). Locally on \(\operatorname{Spec}R\), \(L\) has a single \(B\)-basis. At a residue field, \(B\) is a finite-dimensional algebra, a product of Artinian local algebras by B1 and HS2. An invertible module has a basis on each factor by Nakayama; their sum is a basis on the product. Lift that basis to \(L\). As an \(R\)-module, \(L\) is finite projective: it is a direct summand of a finite free \(B\)-module, which is projective over \(R\). Its fibre rank equals \(\operatorname{rank}_RB\). On a neighbourhood where both are free, the determinant of the map \(B\to L\) given by the lift is a unit at the chosen point. Invert that determinant. The map is then an isomorphism, proving the observation.

Use such \(B\)-bases for a line on the inverse images of target opens. A change of basis by a unit \(v\in B^\times\) changes its determinant line by
\[
 N_{B/R}(v)=\det_R(\text{multiplication by }v).
 \tag{AL19}
\]
The identity \(\det(M_vM_w)=\det(M_v)\det(M_w)\) shows that these transitions multiply, and hence proves multiplicativity of (AL17). Changing the chosen bases gives the same determinant line, so the construction is canonical. A base unit \(b\) acts on a rank-\(m\) module by \(bI_m\), with determinant \(b^m\); this proves (AL18). Determinants and finite affine pushforwards commute with all base changes, proving that assertion as well. The argument uses actual finite projective modules and is valid over nilpotent and non-Noetherian parameter rings. \(\square\)

#### 2L.7. Covariant and contravariant maps on Jacobians

**AL7.** The pointed map \(u\) gives homomorphisms
\[
 u^*:J_D\longrightarrow J_C,\qquad
 u_*:J_C\longrightarrow J_D,\qquad
 u_*u^*=[m]_{J_D},\qquad u_*i_P=i_Q u .
 \tag{AL20}
\]
Here \(u^*\) is pullback of lines and \(u_*\) is norm followed by normalization at \(Q\). These identities hold on all parameter schemes, and no separability assumption on \(u\) is needed.

First we check degrees, so these operations really preserve the specified components. For a divisor \(E=\sum_R n_R[R]\) on \(C\), the determinant construction gives
\[
 N_u(\mathcal O_C(E))\simeq\mathcal O_D(u_*E),\qquad
 u_*E=\sum_{S\in D}
       \left(\sum_{R\mapsto S}n_R[\kappa(R):\kappa(S)]\right)[S].
 \tag{AL21}
\]
To see this, work at a target closed point \(S\), with local DVR \(R_S\). The finite algebra there is semilocal, with localizations the DVRs at the points above \(S\). The two line lattices \(\mathcal O_C\) and \(\mathcal O_C(E)\) are free over this semilocal algebra by AL6's basis argument. After adding a sufficiently large multiple of \(u^*[S]\), first suppose \(E\) effective there. The inclusion between these lattices has cokernel of length \(n_R\) at \(R\). A composition series shows that its length as an \(R_S\)-module is \(\sum n_R[\kappa(R):\kappa(S)]\). The DVR Smith calculation identifies this length with the valuation of the determinant of the inclusion. That determinant is the canonical rational section of the norm line (AL17). This proves (AL21) in the effective case. Subtract the added divisor using multiplicativity and (AL18) to obtain the general case. Rational sections of any line give divisors by DC3, so this covers all lines over the field.

Since \([\kappa(R):k]=[\kappa(R):\kappa(S)][\kappa(S):k]\), (AL21) gives
\[
 \deg N_u(L)=\deg L,\qquad \deg u^*M=m\deg M .
 \tag{AL22}
\]
The second equality is the finite-map degree formula DC7, also proved there by local DVR lengths. Applying these equations on geometric fibres and using AL6's arbitrary base change proves preservation of degree zero on all \(T\).

Pullback preserves rigidification because \(u(P)=Q\). For the norm, take \(N_u(L)^\natural\) on \(D_T\). Multiplicativity and normalization make this a natural transformation of the represented degree-zero group functors; thus Yoneda gives the homomorphisms in (AL20). If \(L\) changes by a base line, its norm changes by the \(m\)-th power of that base line by (AL18), which normalization removes. The first identity in (AL18) therefore proves \(u_*u^*=[m]\) on every \(T\).

For a geometric point \(R\) over an algebraic closure, (AL21) sends \([R]-[P]\) to \([u(R)]-[Q]\). Thus \(u_*i_P\) and \(i_Q u\) agree on every geometric point of \(C\). Their closed equalizer is the entire reduced curve, by B1's closed-point detection as in AL2. Equality descends faithfully to \(k\), proving the last identity of (AL20) as morphisms. AL5 then also characterizes \(u_*\) uniquely.

The norm map is surjective: \([m]\) is surjective by CU8, and factors through \(u_*\). For \(\ell\ne\operatorname{char}k\), all \(\ell\)-adic Tate maps consequently satisfy
\[
 T_\ell(u_*)T_\ell(u^*)=mI,\qquad
 V_\ell(u^*)\text{ injective},\qquad
 V_\ell(u_*)\text{ surjective}.
 \tag{AL23}
\]
These follow directly by tensoring the actual equality in (AL20) with \(\mathbf Q_\ell\), where the nonzero integer \(m\) is invertible. If \(\ell\nmid m\), the integral maps split: \(m^{-1}T_\ell(u_*)\) is a retraction of \(T_\ell(u^*)\). If \(\ell\mid m\), (AL23) alone does not imply an integral splitting or saturation; the exercise gives the precise module obstruction.

For a second pointed finite map \(v:D\to E\), one has \((vu)^*=u^*v^*\) by line pullback, and
\[
 (vu)_*=v_*u_* .
 \tag{AL24}
\]
Both homomorphisms in the second equality agree after \(i_P\), by (AL20), so AL5's uniqueness proves the equality. Isomorphisms give inverse maps. The constructions commute with field extension and with parameter base change because their line operations do. They retain the scheme kernels when the degree is divisible by the characteristic; no assertion about those kernels is inferred merely from their geometric points. \(\square\)

#### 2L.8. Infinitesimal norm and trace

**AL8.** Under \(T_0J_C=H^1(C,\mathcal O_C)\) and \(T_0J_D=H^1(D,\mathcal O_D)\) of JC9, the differentials are
\[
 d(u^*)=H^1(u^\#),\qquad
 d(u_*)=H^1(\operatorname{Tr}_{u_*\mathcal O_C/\mathcal O_D}),\qquad
 d(u_*)d(u^*)=mI .
 \tag{AL25}
\]
The trace is trace of multiplication on the finite locally free algebra; it remains defined when that algebra is not étale.

Use an affine open cover of \(D\), whose inverse images in \(C\) are affine since \(u\) is finite. A first-order line trivial on reduction has bases over these inverse images, by affine lifting and Nakayama as in JC9. Write its transition functions \(1+\epsilon c_{ij}\). On each overlap, multiplication by \(c_{ij}\) has a finite matrix \(M_{c_{ij}}\), and expansion of the determinant gives
\[
 \det(I+\epsilon M_{c_{ij}})
       =1+\epsilon\operatorname{Tr}(M_{c_{ij}}),\qquad \epsilon^2=0 .
 \tag{AL26}
\]
Indeed the identity permutation contributes the constant and the sum of the diagonal linear terms; any other nonzero permutation term uses at least two off-diagonal entries and is divisible by \(\epsilon^2\). Thus the norm sends the Čech cocycle to its trace. Coboundaries map to coboundaries because trace is additive and commutes with restriction. Normalization along \(Q\) changes only the base-line factor and no class in \(H^1\), by JC9. This proves the norm differential. Pullback just pulls back each \(c_{ij}\), giving the other assertion. A base scalar acts by its scalar matrix of rank \(m\), whose trace is \(m\) times that scalar; hence their composite is \(mI\), agreeing with differentiation of (AL20).

For example, in characteristic \(p\), the purely inseparable field algebra \(B=K[t]/(t^p-a)\), with \(a\notin K^p\), has basis \(1,t,\ldots,t^{p-1}\). Multiplication by \(t^j\), for \(1\le j<p\), has zero diagonal in that basis, while multiplication by \(1\) has trace \(p=0\). Therefore every element has trace zero. Nevertheless
\[
 N_{B/K}(t)=a,\qquad
 N_{B\otimes_K K[\epsilon]/(\epsilon^2)\,/\,K[\epsilon]/(\epsilon^2)}
          (1+\epsilon b)=1 .
 \tag{AL27}
\]
The first equality is the determinant of the companion matrix: its sign is \((-1)^{p-1}\), which is \(1\) for odd \(p\) and also \(1\) in characteristic two. The second follows from (AL26). A norm operation can therefore be nontrivial while its infinitesimal trace is zero.

AL1–AL8 proves the Albanese property and finite-curve pullback/norm functoriality. It supplies these geometric inputs to the period construction. The domination and reducibility arguments for arbitrary abelian varieties, semistable curve reduction and the initial formal/analytic period cover still require their actual proofs. \(\square\)

#### 2L.9. Graded exercise: Albanese maps, collision invariants and norms

**Exercise 2L (100 points; ten parts of 10 points).** All assertions about maps below are assertions about scheme morphisms, except where a module calculation is explicitly requested.

1. Let \(\ell\ne\operatorname{char}K\), with \(K\) algebraically closed. Prove directly from a torsor grading that every \(\mu_\ell\)-torsor on \(\mathbf P^1_K\) splits. Explain why the affine equation \(v^\ell=x\) on \(\mathbf G_{m,K}\) is instead a nonsplit torsor.
2. For \(f:\mathbf P^1_K\to A\), suppose a symmetric ample line \(H\) has \(\deg f^*H=18\). Use repeated lifting through multiplication by \(5\), assuming \(5\ne\operatorname{char}K\), to give the contradiction. Explain why merely proving \(df=0\) would not suffice in positive characteristic.
3. Over \(R=k[\epsilon]/(\epsilon^2)\), choose a nonzero tangent vector \(v\in T_0A\) and let \(a:\operatorname{Spec}R\to A\) be the corresponding point through the origin. Describe \(F=a\pi:\mathbf P^2_R\to A\). What do its geometric fibres detect, and what does its coordinate-section restriction detect?
4. In characteristic two, compute the permutation invariants of the collision algebra
   \[
    B=k[x,y]/(x+y,xy).
    \tag{ALX1}
   \]
   Compare them with the restriction of \(k[x+y,xy]\) to that quotient point. Explain precisely why this does not contradict (AL9).
5. Take \(g=3\) and \(d=5\). For a pointed \(f:C_T\to A_T\), list the two Abel projective bundles used to prove that its factor is a homomorphism, their ranks and fibre dimensions. Justify both cancellations in the uniqueness proof on a nonreduced \(T\).
6. For a second point \(Q\in C(k)\), compute the effect of changing \(P\) to \(Q\) on \(i_P\), on the factor \(\phi\), and on the constant part of a general map \(f:C_T\to A_T\). What does AL5 imply when \(C=\mathbf P^1\), and when \(C\) has genus one?
7. Let \(B=R[t]/(t^2-a)\). Compute multiplication matrices, trace and norm for \(b=b_0+b_1t\). Over \(R[\epsilon]/(\epsilon^3)\), calculate the norm of \(1+\epsilon b+\epsilon^2c\). Give a characteristic-two example with zero first-order norm differential and nontrivial second-order norm.
8. For \(u:\mathbf P^1_t\to\mathbf P^1_x\), \(x=t^m\), compute the pullback and pushforward of the divisors at zero and infinity. Compute \(N_{k(t)/k(x)}(t)\), including its sign. Discuss \(m=p\) in characteristic \(p\).
9. Construct maps of free \(\mathbf Z_\ell\)-modules \(A:\mathbf Z_\ell^2\to\mathbf Z_\ell^2\) and \(B\) with \(BA=\ell^2I\), for which \(A\) has nonsaturated image. Give its cokernel and its reductions modulo \(\ell^r\). Contrast the conclusion if \(BA=mI\) with \(\ell\nmid m\). Do not infer an actual curve map merely from these matrices.
10. For \(C\xrightarrow{u}D\xrightarrow{v}E\), prove the composition laws on both pullback and norm Jacobian maps using their full universal properties. Identify the two tangent composites and check that trace after scalar pullback is multiplication by the degree even for a nonétale algebra.

**Full solution.**

1. The graded summand \(L=\mathcal B_1\) is an invertible module, with \(L^{\otimes\ell}\simeq\mathcal O\). The proved Picard group of \(\mathbf P^1\) has no torsion, so choose a basis \(v\) of \(L\). Its \(\ell\)-th power is a nonzero constant. Rescale \(v\) by a root of that constant in \(K\). Multiplication identifies all the summands with powers of \(v\), and
   \[
    \mathcal B\simeq\mathcal O_{\mathbf P^1}[v]/(v^\ell-1);
    \qquad v\longmapsto1
    \tag{ALX2}
   \]
   is a section. On \(\mathbf G_m\), a section of \(v^\ell=x\) would be a unit \(c x^n\) in \(K[x,x^{-1}]\), satisfying \(c^\ell x^{n\ell}=x\). Units are exactly such monomials: lowest and highest exponents of a product add, so a product equal to one forces each factor to have only one exponent. The equation \(n\ell=1\) has no integer solution. The cover is nonetheless a finite étale torsor: the monic equation gives a free rank-\(\ell\) algebra, its root is a unit, and its derivative \(\ell v^{\ell-1}\) is a unit. After the cover, division by its chosen root gives the trivial \(\mu_\ell\)-torsor.

2. A lift through \([5]\) would give
   \[
       18=25\deg f_1^*H ,
       \tag{ALX3}
   \]
   impossible for an integer degree. The general proof uses all powers when a degree is divisible by one such square. In characteristic \(p\), the map \([X:Y]\mapsto[X^p:Y^p]\) of \(\mathbf P^1\) has zero differential on both standard charts and is nonconstant. Thus zero differential alone would not prove constancy; the torsor lifts and integer degrees supply the stronger argument.

3. The map is constant along each projective-space fibre but can vary infinitesimally with the base. Every geometric point of \(\operatorname{Spec}R\) kills \(\epsilon\), so every geometric fibre maps to zero. Yet for a suitable local function \(z\) at \(0\in A\), the nonzero tangent vector gives
   \[
       a^*z=\lambda\epsilon,\qquad\lambda\ne0 .
       \tag{ALX4}
   \]
   Consequently \(a\), and hence \(F\), is not the zero scheme morphism. Any coordinate section \(s\) has \(Fs=a\) and recovers the infinitesimal parameter. AL3 subtracts exactly this \(a\) before using global functions, so it retains the family rather than discarding it.

4. The equation \(x+y=0\) gives \(y=x\) in characteristic two, and \(xy=0\) gives \(x^2=0\). The transposition acts by \(x\leftrightarrow y=x\), so
   \[
       B=k[x]/(x^2),\qquad B^{\mathfrak S_2}=B .
       \tag{ALX5}
   \]
   The base quotient ring \(D=k[e_1,e_2]\), \(e_1=x+y,e_2=xy\), restricts to \(D/(e_1,e_2)=k\); its map to \(B^{\mathfrak S_2}\) misses the nonzero nilpotent \(x\). This is base change along a nonflat map from the quotient \(D\). In (AL9) the tensor product is over the ground field \(k\), for which every module is flat, and the kernel calculation is exact. These are different base changes. In odd characteristic the transposition instead acts on this fibre by \(x\mapsto-x\), whose invariants are just \(k\).

5. Here \(E_5\) has rank \(5+1-3=3\), so \(q_5:S_5(C)\to J_C\) is a \(\mathbf P^2\)-bundle. For \(2d=10\), \(E_{10}\) has rank eight and \(q_{10}\) is a \(\mathbf P^7\)-bundle. Their source dimensions are five and ten; the Jacobian dimension is three. Addition of the fixed divisor \(5P\) compares their factors, and addition of two varying degree-five divisors proves the group law. In uniqueness, equality after the ordered cover descends because it is finite faithfully flat and FD5 detects equality of morphisms. Equality after \(q_5\) cancels because it has Zariski local sections. Both statements concern the actual structure sheaves and apply on nonreduced \(T\); equality on geometric points is not substituted for either one.

6. Under the canonical identity of the represented degree-zero Picard quotients,
   \[
      i_Q(R)=i_P(R)-i_P(Q),\qquad
      f(R)=f(P)+\phi i_P(R)=f(Q)+\phi i_Q(R).
      \tag{ALX6}
   \]
   In particular \(f(Q)=f(P)+\phi i_P(Q)\) as \(T\)-points, and the homomorphism \(\phi\) is unchanged. For \(\mathbf P^1\), its Jacobian is the point by Exercise 2K, so every such family \(f\) factors through its base \(T\), in agreement with AL3. For genus one, Exercise 2K identifies \(i_P:C\simeq J_C\); every map into an abelian variety is uniquely a translation of a group homomorphism after this identification.

7. In the basis \(1,t\),
   \[
      M_b=\begin{pmatrix}b_0&a b_1\\ b_1&b_0\end{pmatrix},
      \qquad\operatorname{Tr}(b)=2b_0,\qquad N(b)=b_0^2-a b_1^2.
      \tag{ALX7}
   \]
   Put \(c=c_0+c_1t\). Expanding that same determinant modulo \(\epsilon^3\) gives
   \[
     N(1+\epsilon b+\epsilon^2c)
       =1+2b_0\epsilon+
          (2c_0+b_0^2-a b_1^2)\epsilon^2 .
       \tag{ALX8}
   \]
   This identity uses no inverse of \(2\). In characteristic two with \(b=t,c=0,a\ne0\), the result is \(1-a\epsilon^2\ne1\), although \(dN=\operatorname{Tr}=0\). It is a unit with a nontrivial second-order coefficient. Thus passing only to the residue field or to first-order tangent information loses this norm value.

8. The map extends at infinity by the local equation \(x^{-1}=(t^{-1})^m\), so it is a finite map of degree \(m\). Its divisor operations are
   \[
    u^*[0_x]=m[0_t],\quad u^*[\infty_x]=m[\infty_t],
    \qquad u_*[0_t]=[0_x],\quad u_*[\infty_t]=[\infty_x].
    \tag{ALX9}
   \]
   The multiplication companion matrix for \(t\) has \(m-1\) subdiagonal ones and top-right entry \(x\). Its determinant is
   \[
        N(t)=(-1)^{m-1}x .
        \tag{ALX10}
   \]
   Its divisor is \([0_x]-[\infty_x]\), as predicted by (AL21); the scalar sign affects no divisor. For \(m=p=\operatorname{char}k\), the extension is purely inseparable and the fibre at zero has algebra \(k[t]/(t^p)\), of length \(p\) with one geometric point. Its trace is zero as in AL8, while \(N(t)=x\). These are genuine curve/algebra examples, although both Jacobians here are zero-dimensional.

9. Take
   \[
       A=\begin{pmatrix}\ell&0\\0&1\end{pmatrix},
       \qquad
       B=\begin{pmatrix}\ell&0\\0&\ell^2\end{pmatrix},
       \qquad BA=\ell^2I .
       \tag{ALX11}
   \]
   The cokernel of \(A\) is \(\mathbf Z/\ell\), so its image is not saturated. On \((\mathbf Z/\ell^r)^2\), its kernel has \(\ell\) elements, its image has \(\ell^{2r-1}\) elements, and its cokernel has \(\ell\) elements, for every \(r\ge1\). Indeed the second coordinate is unchanged and the first is multiplication by \(\ell\). Over \(\mathbf Q_\ell\), both maps are invertible. If \(\ell\nmid m\) instead, \(m^{-1}B\) is an integral left inverse, so the source embeds as a direct summand and its image is saturated. This is the exact implication justified by (AL23). The displayed matrices alone do not produce a curve morphism or identify its geometric kernel.

10. Pulling back a line along a composite gives \((vu)^*=u^*v^*\) on every parameter scheme. The norm maps \(v_*u_*\) and \((vu)_*\) both restrict along \(i_P\) to \(i_{v(Q)}vu\), by (AL20). AL5 gives their equality as homomorphisms. Differentiating gives the corresponding identities on \(H^1\). Locally a scalar \(b\) acts on a rank-\(m\) finite algebra by \(bI_m\), whether or not the algebra is étale, hence
    \[
       \operatorname{Tr}_{B/R}(b\cdot1)=m b,\qquad
       \operatorname{Tr}_{B/R}\circ(R\to B)=m\,\operatorname{id}_R .
       \tag{ALX12}
    \]
    Applying the affine Čech complex gives the composite \(mI\) on \(H^1\). In characteristic dividing \(m\) this composite can be zero; the group-scheme equality \(u_*u^*=[m]\) still holds and need not be the zero morphism. \(\square\)

### 2M. A curve whose Jacobian dominates an abelian variety

Let \(A/k\) be an abelian variety of dimension \(a\). We will construct, after a finite separable extension \(E/k\), a pointed smooth projective geometrically integral curve \((C,P)\) and a smooth surjective homomorphism
\[
 \Phi:J_C\longrightarrow A_E .
 \tag{CD1}
\]
The construction includes one connected curve and prescribed tangent directions. Its proof supplies the smooth-section and connectedness arguments; neither is admitted as an unnamed Bertini input. It does not yet supply a complementary abelian subvariety or an isogeny splitting (CD1).

Free comparisons are the Stacks project's [smooth hyperplane incidence argument](https://stacks.math.columbia.edu/tag/0FD6) and Milne's author notes [*Abelian Varieties*, Chapter III, §10](https://www.jmilne.org/math/CourseNotes/AV.pdf). The latter argument uses reducibility. We instead arrange independent tangent directions so that surjectivity follows from an actual invertible Jacobian. PF1–PF9, SF1–SF6, DR1, CU7–CU9 and AL5 provide the earlier projective, smooth-chart, completion, abelian and Albanese results used below.

#### 2M.1. Finite graded resolutions over a polynomial ring

**CD1.** For \(S=K[X_0,\ldots,X_N]\), every finite graded \(S\)-module has a finite resolution by finite direct sums of shifted copies of \(S\), of length at most \(N+1\).

All graded modules here are bounded below, and all maps preserve degree. Choose homogeneous generators whose classes form a \(K\)-basis modulo \(\mathfrak n=(X_0,\ldots,X_N)\), and continue with each kernel. Noetherianity makes the kernels finite. The graded Nakayama assertion used at each step has an elementary proof: a nonzero bounded-below graded module \(M\) with \(M=\mathfrak nM\) would have a nonzero homogeneous element of smallest possible degree, which cannot be a sum of positive-degree variables times elements of smaller degree. Hence the chosen lifts generate. Their independence modulo \(\mathfrak n\) makes every differential matrix in the resulting resolution have its entries in \(\mathfrak n\).

The variables form a regular sequence: after quotienting by any initial set, the remaining polynomial ring is a domain, and its next variable is regular. The Koszul complex on them resolves \(K=S/\mathfrak n\). For one variable this is the injective two-term multiplication complex; adjoining another variable is its mapping cone, whose homology is exact except at the new quotient because that variable is regular there. Induction proves exactness and the differential
\[
 \partial(e_{i_1}\wedge\cdots\wedge e_{i_r})
 =\sum_{j=1}^r(-1)^{j-1}X_{i_j}
    e_{i_1}\wedge\cdots\widehat e_{i_j}\cdots\wedge e_{i_r}.
 \tag{CD2}
\]
Tensor the constructed free resolution \(F_\bullet\) of \(M\) with this length-\((N+1)\) resolution of \(K\). In its signed double complex, resolving in the \(F\) direction gives the Koszul complex tensored with \(M\); resolving in the other direction gives \(F_\bullet\otimes_SK\). Both assertions follow by exactness when tensoring with a free module and the finite-diagonal elimination SH9. Each total degree has finitely many terms, so the initially unbounded resolution causes no infinite-sum problem.

The second complex has zero differentials, by minimality, while the first has no terms in degrees \(>N+1\). Consequently
\[
 F_i\otimes_SK=0\quad(i>N+1).
 \tag{CD3}
\]
The finite free graded modules \(F_i\) there are zero, since every nonzero shifted free summand has a nonzero reduction. This proves the finite resolution, including its bound. Sheafification is exact: on each standard projective chart it is graded localization followed by taking the degree-zero component, both exact operations. Thus a closed projective subscheme has a finite resolution of its structure sheaf by finite sums of twists \(\mathcal O(b)\). \(\square\)

#### 2M.2. The finite-complex projective duality calculation

**CD2.** Put \(\omega=\mathcal O_{\mathbf P^N_K}(-N-1)\). If \(F^\bullet\) is a bounded complex of finite sums of twists on \(\mathbf P^N_K\), then there is a perfect pairing of finite-dimensional vector spaces
\[
 \mathbb H^i(F^\bullet)\ \times\
 \mathbb H^{N-i}\bigl(\mathcal Hom(F^\bullet,\omega)\bigr)
       \longrightarrow K .
 \tag{CD4}
\]
Here \(\mathbb H\) means the cohomology of the finite affine Čech total complex, with the usual signed total differential; the internal Hom complex has differential \(d(h)=-(-1)^{\deg h}h\,d_F\), since \(\omega\) has zero differential.

We give the calculation rather than assuming a general duality theorem. PF5–PF6 gives the monomial bases of the cohomology of every twist. For \(N\ge1\), only degrees zero and \(N\) can be nonzero. Multiplication, followed by taking the coefficient of
\[
       X_0^{-1}\cdots X_N^{-1}
       \quad\text{in }H^N(\mathbf P^N,\omega),
 \tag{CD5}
\]
pairs the basis \(X^\alpha\), \(\alpha_i\ge0\), with the basis \(X^{-\alpha-\mathbf1}\). It is therefore perfect between \(H^q(\mathcal O(b))\) and \(H^{N-q}(\mathcal O(-b-N-1))\), for every integer \(b\). When both groups vanish the assertion is the perfect pairing of zero spaces. For \(N=0\), use the single frame \(X_0^b\), pairing it with \(X_0^{-b-1}\), and send the frame \(X_0^{-1}\) to \(1\).

The coefficient functional in (CD5) vanishes on Čech boundaries: a term supported on a proper subset of the coordinate opens has at least one exponent nonnegative, whereas all the exponents in (CD5) are negative. Thus it is a chain map from the Čech complex of \(\omega\), placed in degree \(N\), to \(K\). Ordered Čech cup product and evaluation \(F\otimes\mathcal Hom(F,\omega)\to\omega\), with the sign for passing a Čech degree past a complex degree, give a chain map
\[
 \check C\bigl(\mathcal Hom(F,\omega)\bigr)[N]
          \longrightarrow \operatorname{Hom}_K(\check C(F),K).
 \tag{CD6}
\]
We use the cohomological convention \(D[N]^j=D^{j+N}\). The identity \(d(uv)=d(u)v+(-1)^{\deg u}u\,d(v)\) for the cup product and the displayed Hom differential check the chain identity, including the signs.

Filter by the finite set of degrees of \(F\). On each associated successive quotient, (CD6) is the single-twist cohomology pairing just computed, extended to its finite direct sums and duals. It is a quasi-isomorphism on that quotient. Induction up the filtration, using the long exact cohomology sequence and the elementary five-lemma chase, proves it is a quasi-isomorphism on the whole complex. Algebraic duality over \(K\) is exact, by choosing vector-space bases, so the right complex has cohomology dual to that of \(\check C(F)\). This proves (CD4). The same finite filtration and PF cohomology show that all these cohomology spaces are finite-dimensional. No higher-dimensional duality theorem has been used in this argument. \(\square\)

#### 2M.3. Negative twists and connected smooth sections

**CD3.** Let \(X/K\) be smooth projective geometrically integral of dimension \(n>0\), with a fixed projective embedding and hyperplane line \(H\). For all sufficiently large \(r\),
\[
       H^i(X,H^{-r})=0\qquad(0\le i<n).
       \tag{CD7}
\]
In particular, if \(n\ge2\), every smooth zero divisor of a nonzero section of \(H^r\), for such \(r\), is nonempty and geometrically integral.

To prove the vanishing, extend to an algebraic closure; field base change is the exact tensor of the affine Čech complex, so vanishing there detects vanishing over \(K\). Write \(X\hookrightarrow\mathbf P^N\), \(c=N-n\), and take the finite twist resolution \(F^\bullet\to\mathcal O_X\) from CD1, with \(F\) in nonpositive degrees. The complex
\[
       G^\bullet=\mathcal Hom(F^\bullet,\omega)
       \tag{CD8}
\]
has just one nonzero cohomology sheaf, in degree \(c\).

Here is the local justification, in all dimensions. For the local ring \(R\) at a geometric closed point of a standard smooth \(n\)-dimensional chart, SF4 gives a basis of the cotangent space by the free coordinates. Nakayama makes those coordinates generate the maximal ideal. They therefore give a surjection \(K[[t_1,\ldots,t_n]]\to\widehat R\): lift each successive homogeneous term of a completed element by monomials in those coordinates, and sum by completeness. Conversely SF3's successive coordinate corrections solve the defining equations in that power-series ring, giving a map from \(R\), and hence its completion, back to \(K[[t_1,\ldots,t_n]]\). The composite on the free coordinates is the identity. The other composite is the identity too: solutions with the same free coordinates are unique modulo each power of the maximal ideal, by SF3's invertible-gradient correction; pass to the inverse limit. Thus the completion is precisely that power-series ring. Faithful completion DR1 makes \(R\to\widehat R\) injective, so \(R\) is a domain. All other points on the chart have domain local rings by localization at a closed point containing their prime. This proves the local-domain assertion in every dimension; SF5 alone was a curve statement.

For the closed embedding above, the completed ambient ring and completed smooth quotient are consequently \(K[[z_1,\ldots,z_N]]\) and \(K[[t_1,\ldots,t_n]]\). The quotient map is surjective on cotangents. Choose \(n\) source coordinates whose images are a parameter basis in the quotient, and use the same degree-by-degree formal inverse to identify their images with the \(t_i\). The other \(c\) coordinates map to formal series in the \(t_i\); subtract those series. The completed kernel is generated by these \(c\) new coordinates. It is a regular sequence, since its successive quotients are power-series rings.

These generators and the equality of the completed ideal can be detected algebraically. Lift a cotangent basis of the local ideal. Nakayama and faithful exact completion DR1 show that its \(c\) lifts generate the local ideal. Their Koszul complex becomes exact on completion by the coordinate description; its finite homology modules are therefore zero before completion. The dual Koszul complex is the same exterior complex in reversed degrees, up to the signs of (CD2), and has cohomology only in degree \(c\).

Any two finite free resolutions of a module on this local affine neighbourhood are homotopy equivalent. Lift their augmentations recursively using freeness and exactness; lift the differences recursively to give the homotopies of their composites with the identity. Applying \(\operatorname{Hom}(-,\omega)\) preserves these homotopies. Thus the local cohomology of (CD8) is the same as for the dual Koszul complex. It vanishes outside degree \(c\). The assertion at all points follows because a nonzero coherent cohomology sheaf would have a closed point in its support, by B1. Its degree-\(c\) cohomology sheaf is coherent.

For \(r\) sufficiently large, Serre vanishing PF8 applies to the finitely many terms, cycles, boundaries and cohomology sheaves of \(G^\bullet(r)\). Their positive cohomology groups all vanish. Short exact sequences for cycles and boundaries then show directly that its Čech total cohomology is the cohomology of its global-sections complex, and is concentrated in degree \(c\): taking global sections of those short exact sequences is exact. CD2, applied to \(F^\bullet(-r)\), now gives
\[
       H^i(X,H^{-r})^\vee
          \simeq \mathbb H^{N-i}(G^\bullet(r))=0
             \quad\text{if }N-i\ne c .
       \tag{CD9}
\]
This proves (CD7), with no general duality premise.

For a nonzero section with zero divisor \(Y\), the integral scheme \(X\) makes its equation regular, so
\[
 0\longrightarrow H^{-r}\longrightarrow\mathcal O_X
                    \longrightarrow\mathcal O_Y\longrightarrow0 .
 \tag{CD10}
\]
If \(n\ge2\), (CD7) in degrees zero and one, and the constant-function theorem FC20, give \(H^0(Y,\mathcal O_Y)=K\). The same holds after algebraic closure. Hence \(Y\) is nonempty and geometrically connected: a disconnected decomposition would produce a nonconstant idempotent global function. If \(Y\) is smooth, its geometric local rings are domains by the all-dimensional formal-coordinate argument just proved; different irreducible components cannot meet. There are finitely many components, so connectedness makes there be just one. The same domain argument gives reducedness. Thus \(Y\) is geometrically integral. \(\square\)

#### 2M.4. Prescribed jets and uniform freedom away from the marks

**CD4.** Let \(X\hookrightarrow\mathbf P^N_K\) be smooth projective, let \(P_1,\ldots,P_s\) be distinct \(K\)-points with \(s\ge1\), and put \(Z=\coprod_i\operatorname{Spec}(\mathcal O_{X,P_i}/\mathfrak m_{P_i}^2)\). For all sufficiently large \(r\), any specified first jets at the \(P_i\) are the jets of a section of \(H^r\). Moreover
\[
 V_r=H^0(X,\mathcal I_ZH^r)\longrightarrow
             H^r_x/\mathfrak m_x^2H^r_x
 \tag{CD11}
\]
is surjective after extension to a geometric residue field, at every geometric point \(x\notin\{P_i\}\), provided \(r\ge2s+1\).

The first assertion follows from the exact sequence with quotient \(H^r|_Z\) and Serre vanishing \(H^1(X,\mathcal I_ZH^r)=0\), proved in PF8. This is a finite closed scheme \(Z\), so its section space is exactly the direct sum of the specified finite jet spaces.

For the uniform assertion, work over an algebraic closure and fix \(x\ne P_i\). For each \(i\), choose a hyperplane equation \(l_i\) vanishing at \(P_i\) and nonzero at \(x\). Such an equation exists because the projective embedding separates the two points. Choose a coordinate linear form \(h\) nonzero at \(x\). Then
\[
 b=\left(\prod_{i=1}^s l_i^2\right)h^{\,r-2s-1}
 \tag{CD12}
\]
is a degree-\((r-1)\) section, vanishes to order at least two at every mark, and is a unit in a local frame at \(x\). Multiplying it by all coordinate linear forms gives sections in \(V_r\).

Those linear forms span the full first-jet space of \(H\) at \(x\): the form \(h\) supplies the value, and the differences \(l-(l/h)(x)h\), divided by \(h\), generate the cotangent space because the affine coordinate functions of a closed embedding generate its local algebra. Multiplication by the unit \(b\) is an invertible linear map on the local algebra modulo \(\mathfrak m_x^2\). Thus these products span all first jets in (CD11). In a smooth \(n\)-fold that jet space has dimension \(n+1\). This proof uses squares to preserve the marked jets in every characteristic, not a division by \(2\). \(\square\)

#### 2M.5. A smooth integral section with fixed tangent constraints

**CD5.** Assume \(K\) infinite, \(X/K\) smooth projective geometrically integral of dimension \(n\ge2\), and \(P_i\) as above. Choose nonzero covectors \(\alpha_i\in T_{P_i}^*X\). For sufficiently large \(r\), after choosing frames of \(H^r\) at the marks, there is a section \(s\) whose zero divisor \(Y\) is smooth geometrically integral and satisfies
\[
 s(P_i)=0,\qquad ds(P_i)=\alpha_i,\qquad
                T_{P_i}Y=\ker\alpha_i .
 \tag{CD13}
\]
The derivative at a zero of a line-bundle section is well-defined with values in that line's fibre; the chosen frame identifies it with the displayed covector.

Choose \(r\) so that CD3 and CD4 apply. The sections with the prescribed jets form a nonempty affine space
\[
       W=s_0+V_r,\qquad M=\dim_KV_r .
       \tag{CD14}
\]
We verify that the bad sections lie in a proper closed subset of \(W\).

On an affine smooth chart with local parameters \(u_1,\ldots,u_n\) and a frame for \(H^r\), write the universal section as \(f(x,w)\). The differentials \(du_j\) form a basis, so its coefficients \(\partial f/\partial u_j\) are regular functions. The locus
\[
 \Sigma:\quad f=\frac{\partial f}{\partial u_1}
                  =\cdots=\frac{\partial f}{\partial u_n}=0
             \quad\subset X\times_KW
 \tag{CD15}
\]
glues to a closed locus: changing parameters changes the derivative coefficients by an invertible matrix, and changing frame adds multiples of \(f\) to those coefficients. By the standard Jacobian chart SF3, a section's zero scheme is smooth of dimension \(n-1\) exactly where its value vanishes and not all these derivatives vanish. At a mark, the fixed nonzero \(\alpha_i\) excludes \(\Sigma\), for every parameter value.

Away from the marks, CD4 says that value and all \(n\) derivatives are independent affine linear conditions on \(W\). More explicitly, on an open where one \((n+1)\)-column minor of the jet matrix of \(V_r\) is invertible, solve for those \(n+1\) parameter coordinates. The restriction of \(\Sigma\) is an affine-space bundle of rank \(M-n-1\) over that open of \(X\). Such opens cover, by the rank assertion and B1. Thus every component of \(\Sigma\) has dimension at most
\[
                  n+M-n-1=M-1 .
                  \tag{CD16}
\]
The dimension calculation uses the actual local affine-bundle coordinates and GQ1's dimension-as-transcendence-degree proof.

The projection \(X\times W\to W\) is proper, hence the image of the closed \(\Sigma\) is closed. Its dimension is at most \(M-1\): on an irreducible component dominating an image component, the induced injection of function fields bounds transcendence degree. Therefore the image is a proper closed subset of the \(M\)-dimensional affine space \(W\). Its complement is a nonempty open defined over \(K\). It has a \(K\)-point because \(K\) is infinite: a nonzero polynomial cannot vanish on all \(K^M\), by induction on the variables; a nonempty open contains a principal open defined by such a polynomial.

Take the section at that point. It is nonzero, since it has a specified nonzero derivative at every mark. Its zero divisor is smooth, satisfies (CD13), and is geometrically integral by CD3. All the smoothness and connectedness assertions were checked after geometric scalar extension, so they apply even if the infinite field \(K\) is imperfect. \(\square\)

#### 2M.6. One curve with finitely many prescribed tangent lines

**CD6.** Over an infinite field \(K\), let \(X/K\) be smooth projective geometrically integral, of dimension \(n\ge2\). Given distinct \(K\)-points \(P_i\) and lines \(L_i\subset T_{P_i}X\), there is a smooth projective geometrically integral curve \(C\hookrightarrow X\) through the marks, with
\[
                         T_{P_i}C=L_i .
                         \tag{CD17}
\]
In each \(n\)-dimensional marked tangent space choose a complete flag ending in \(L_i\). Apply CD5 with covectors whose kernels are the next \((n-1)\)-dimensional flag spaces. It gives one smooth geometrically integral divisor with exactly those tangent spaces. Its restricted hyperplane line remains very ample, because it is still closed in the original projective space. Repeat on this divisor, choosing new sufficiently large powers at each stage and the next flag covectors. Until dimension one, the ambient dimension at each cut is at least two, so CD3's connectedness applies. After \(n-1\) steps the result is the stated single curve. Every cut is an actual closed divisor, with the prescribed tangent kernels; no component is selected or discarded.

Apply this over the separable closure \(K=k^{\mathrm{sep}}\) to \(A_K\). This field is infinite. The smooth \(A_K\) has infinitely many \(K\)-points when \(a>0\): a standard étale chart maps to an open of \(\mathbf A^a_K\); every nonempty finite étale fibre over a \(K\)-point splits over the separably closed field, and the open has infinitely many \(K\)-points. Choose distinct \(P_1,\ldots,P_a\in A(K)\), a basis \(v_1,\ldots,v_a\) of \(\operatorname{Lie}(A_K)=T_0A_K\), and the translated tangent lines
\[
            L_i=d(t_{P_i})_0(Kv_i)\subset T_{P_i}A_K .
            \tag{CD18}
\]
For \(a\ge2\), construct \(C\) with these tangent lines by the preceding argument. All equations of its finitely many cuts, the marked points, the vectors and the witnessing nonzero minors involve finitely many elements of \(k^{\mathrm{sep}}\). They lie in one finite separable extension \(E/k\). The same equations define \(C\hookrightarrow A_E\), the points and the tangent identities there. Smoothness and geometric integrality hold over \(E\), since they hold after the algebraic closure and these equations base change to the constructed curve. Put \(P=P_1\), and use the pointed map \(f:C\to A_E\), \(R\mapsto R-P\).

If \(a=1\), take \(C=A\), \(P=0\), \(f=\operatorname{id}\), with no cuts. If \(a=0\), CU7's dimension-zero argument gives \(A=\operatorname{Spec}k\); take \(C=\mathbf P^1_k\), whose Jacobian is a point by Exercise 2K. These choices prove the same existence assertion in the boundary dimensions. In particular no assertion that an open has a point over the original finite field is needed; the finite separable extension is part of the construction. \(\square\)

#### 2M.7. An invertible sum Jacobian and the surjective homomorphism

**CD7.** The pointed map \(f\) in CD6 induces (CD1), and that homomorphism is smooth. For \(a\ge1\), the actual sum map
\[
 F:C^a\longrightarrow A_E,\qquad
     (R_1,\ldots,R_a)\longmapsto\sum_{j=1}^a f(R_j)
 \tag{CD19}
\]
is surjective and generically finite separable.

For \(a\ge2\), identify the tangent spaces of \(A_E\) with \(\operatorname{Lie}A_E\) by translation to the origin. The differential of addition at the origin is addition on tangent vectors: its restrictions to the two axes are the identity, and a linear map on their direct sum is determined by those restrictions. Translation gives the same rule at every tuple of points. At the marked tuple \(\mathbf P=(P_1,\ldots,P_a)\), (CD17)–(CD18) therefore identify \(dF\) with
\[
 E^a\xrightarrow{\sim}\operatorname{Lie}A_E,\qquad
               (c_1,\ldots,c_a)\longmapsto\sum_i c_iv_i .
               \tag{CD20}
\]
It is an isomorphism. Both source and target are smooth of dimension \(a\). In their standard smooth coordinates, the invertible matrix in (CD20) makes \(F\) étale on a neighbourhood of \(\mathbf P\): combine its coordinate functions with the defining smooth-chart equations, and the full gradient minor is invertible, giving a relative-dimension-zero chart SF3 and its flatness from EA1–EA18.

Étale maps are open by the earlier EA proof. Thus \(F\) has image containing a nonempty open in the integral \(A_E\), and is dominant. It is proper because its source is projective and its target separated. Its image is closed, so it is all of \(A_E\). Equality of the dimensions and GQ1 give a finite algebraic extension of function fields. The nonempty étale source open contains the generic point of the integral \(C^a\), so that field extension is separable. For \(a=1\), CD6 chose \(F=\operatorname{id}_A\), giving the same conclusions directly.

By AL5 there is a unique homomorphism \(\Phi:J_C\to A_E\) with \(\Phi i_P=f\). Its composition with the sum of the \(a\) maps \(i_P\) is \(F\), an equality of morphisms on all parameter schemes by (AL14). Surjectivity of \(F\) makes \(\Phi\) surjective.

The differential of \(\Phi\) is surjective at the image in \(J_C\) of \(\mathbf P\), because its composition with the differential of that sum map is the isomorphism (CD20). The homomorphism identity and translation make \(d\Phi_0\) surjective as well. For a map between smooth varieties, this gives a smooth chart of relative dimension \(g_C-a\): choose \(g_C-a\) additional source coordinates complementary to the independent target coordinate differentials, and apply the same invertible-Jacobian argument to the map into \(A_E\times\mathbf A^{g_C-a}\). Its composition with the smooth projection is \(\Phi\).

After algebraic closure, translation takes this smooth chart to a chart at every closed point of \(J_C\). The nonsmooth closed complement, if nonempty, would have a closed point by B1, so there is none. Smoothness descends by SF1–SF3 and FD1–FD4. This proves that \(\Phi\) is smooth and surjective, with the stated relative dimension. The case \(a=0\) is the map between points already constructed. \(\square\)

#### 2M.8. The full kernel, components and the rational Tate sequence

**CD8.** Let \(K=\ker\Phi\). It is a smooth proper group scheme of dimension \(g_C-a\), and (CD1) is an actual faithfully flat quotient:
\[
 K\times_EJ_C\xrightarrow{\sim}J_C\times_{A_E}J_C,\quad
       (h,x)\longmapsto(x+h,x),\qquad
 0\longrightarrow K\longrightarrow J_C
               \xrightarrow{\Phi}A_E\longrightarrow0 .
 \tag{CD21}
\]
Exactness in the second display is for the faithfully flat topology, not an assertion that every original-field point lifts.

The kernel is the base change of the identity along the smooth proper \(\Phi\); hence it is smooth and proper, of that relative dimension. The first map in (CD21) has inverse \((y,x)\mapsto(y-x,x)\) on every scheme, giving an actual inverse of schemes. Smooth surjectivity is faithfully flat and locally of finite presentation; properness makes it quasi-compact. Thus this cover itself gives local lifts and proves the asserted quotient exactness.

Over an algebraic closure \(\bar E\), write \(K^0\) for the connected component of the origin. CD3's all-dimensional formal-coordinate argument makes the local rings of the smooth Noetherian \(K\) domains. Its finitely many irreducible components are therefore disjoint and open, so its connected components are integral. Translation identifies the component through a point with the translate of \(K^0\). Multiplication and inverse preserve \(K^0\): their connected images contain the origin. The product is connected because the field Čech calculation gives \(H^0(K^0\times K^0,\mathcal O)=\bar E\) from \(H^0(K^0,\mathcal O)=\bar E\), so it has no nontrivial idempotent; this is also the degree-zero case of CU2. Thus \(K^0\) is an abelian variety of dimension \(g_C-a\), and the components form a finite group
\[
                \Pi=K(\bar E)/K^0(\bar E),\qquad N=|\Pi|.
                \tag{CD22}
\]
Every component has a \(\bar E\)-point by B1. The group is therefore exactly the set of geometric components, with its indicated cosets. The origin component is stable under every element of \(G_E\).

For \(\ell\ne\operatorname{char}E\), the actual homomorphisms give
\[
 \begin{gathered}
 N\,T_\ell(A_E)\subset
       \operatorname{image}\bigl(T_\ell(J_C)\to T_\ell(A_E)\bigr),\\
 0\longrightarrow V_\ell(K^0)\longrightarrow V_\ell(J_C)
            \longrightarrow V_\ell(A_E)\longrightarrow0 .
 \end{gathered}
 \tag{CD23}
\]
These are \(G_E\)-stable assertions; the action on \(K^0\)'s geometric torsion is the restricted action on \(K\).

To prove the first, take \(b\in A_E[\ell^r](\bar E)\) and lift it to \(x\in J_C(\bar E)\), using surjectivity and a closed point in the geometric fibre. Then \(\ell^rx\in K\), so \(N\ell^rx\in K^0\), since the finite group \(\Pi\) is killed by its order. By CU8 choose \(y\in K^0(\bar E)\) with \(\ell^ry=N\ell^rx\). Consequently
\[
       z=Nx-y\in J_C[\ell^r](\bar E),\qquad \Phi(z)=Nb .
       \tag{CD24}
\]
For a compatible sequence \(b_r\), these levelwise lifts give compatible lifts of every finite initial segment by projecting any lift at its highest level. The sets of such finite segments are finite and nonempty. Their inverse limit is nonempty by the finite-product compactness argument of Lesson 1: the finitely many compatibility equations have the finite-intersection property. This supplies a compatible lift of \(Nb_r\), proving the first line of (CD23), not just its levelwise analogue.

If \((x_r)\in T_\ell(J_C)\) maps to zero, all \(x_r\) lie in \(K\). Their component classes \(\xi_r\in\Pi\) are killed by \(\ell^r\) and satisfy \(\ell\xi_{r+1}=\xi_r\). They lie in the \(\ell\)-primary subgroup of the finite \(\Pi\), killed by some \(\ell^e\). Hence \(\xi_r=\ell^e\xi_{r+e}=0\). Thus every \(x_r\) lies in \(K^0\), proving the exact integral kernel \(T_\ell(K^0)\). CU9 makes all three Tate modules finite free. Tensoring with \(\mathbf Q_\ell\) and using the first line of (CD23), where \(N\) becomes invertible, proves its exact rational sequence.

If \(\ell\nmid N\), the Tate map is already onto integrally. For primes dividing \(N\), we assert only that its cokernel is killed by \(N\). In particular (CD23) does not choose a Galois-equivariant splitting or a complementary abelian variety. If \(g_C=a\), the smooth proper zero-dimensional kernel is finite étale, and the proper finite-fibres theorem makes \(\Phi\) an isogeny. In general its positive-dimensional kernel must be handled by the required reducibility argument before the already proved isogeny-transfer theorem can be applied.

CD1–CD8 constructs the curve and its smooth surjective Jacobian homomorphism after a finite separable extension in every characteristic. Reducibility, semistable curve geometry and the initial formal/analytic period cover remain separate proof obligations. \(\square\)

#### 2M.9. Graded exercise: connected sections and dominating curves

**Exercise 2M (100 points; ten parts of 10 points).** Use the actual constructions CD1–CD8.

1. Write the Koszul resolution of \(K\) over \(K[x,y,z]\), including its matrices and signs. Compute its reduction modulo \((x,y,z)\) and explain the length bound for a minimal graded resolution.
2. Give dual monomial bases for \(H^0(\mathbf P^2,\mathcal O(2))\) and \(H^2(\mathbf P^2,\mathcal O(-5))\), using (CD5). Compute \(\dim H^3(\mathbf P^3,\mathcal O(-7))\). State why the same calculation applies to a finite complex of twists.
3. Let \(X\subset\mathbf P^3_K\) be a smooth geometrically integral hypersurface of degree \(d>0\). Prove directly that \(H^0(X,\mathcal O_X(-r))=H^1(X,\mathcal O_X(-r))=0\) for every \(r>0\). Deduce connectedness and integrality of a smooth positive-degree section. Identify the degree-one cohomology sheaf of its dual resolution.
4. In the affine plane, mark \((0,0),(1,0)\), and put \(q=x^2(x-1)^2\). Compute the first-jet matrix at a point \((u,v)\) of the three polynomials \(q,xq,yq\), its determinant, and its behaviour in characteristic two. Give a point in \(\mathbf F_4\) where \(q\ne0\).
5. A smooth threefold and a section parameter space \(W=\mathbf A^{12}\) satisfy CD4's jet-surjectivity. Compute the dimension of the section parameters singular at a fixed unmarked point and the dimension bound for the entire singular incidence. Explain why the bad-parameter image is closed here.
6. On a smooth fourfold, prescribe four marked tangent lines corresponding under translation to \(e_1,e_2,e_3,e_4\). Give explicit local flags and normal covectors for all three cuts at each mark. Compute the final sum-map Jacobian. Explain which global result turns these local flags into one curve.
7. Let \(A\) be an abelian surface, and let \(C\subset A_E\) have the two prescribed translated tangent axes of CD6. Prove that the resulting map \(J_C\to A_E\) is smooth and onto, and state what can be concluded about \(g_C\), the kernel and the generic degree of \(C^2\to A_E\).
8. In characteristic \(p\), compare the differential of \([p]:A\to A\) with the differential of the constructed \(\Phi\). Why does surjectivity alone not prove smoothness or give the tangent argument (CD20)?
9. Suppose the geometric component group in (CD22) is \(\mathbf Z/6\). Determine the restrictions on the Tate cokernel for \(\ell=2,3,5\), and prove the compatible component classes in the Tate kernel vanish. Distinguish an annihilator bound from an exact cokernel computation.
10. Explain the finite separable field-extension step, including the polynomial \(T^q-T\) over \(\mathbf F_q\) as a warning about rational points. Treat the case \(\dim A=0\), and explain why a positive-dimensional kernel in (CD21) does not yet give an isogeny decomposition.

**Full solution.**

1. With bases \((e_x,e_y,e_z)\) and \((e_x\wedge e_y,e_x\wedge e_z,e_y\wedge e_z)\), the sequence is
   \[
    0\to S(-3)\xrightarrow{\ d_3\ }S(-2)^3
      \xrightarrow{\ d_2\ }S(-1)^3
      \xrightarrow{\ d_1\ }S\to K\to0,
    \tag{CDX1}
   \]
   where
   \[
    d_1=\begin{pmatrix}x&y&z\end{pmatrix},\quad
    d_2=\begin{pmatrix}-y&-z&0\\x&0&-z\\0&x&y\end{pmatrix},
    \quad d_3=\begin{pmatrix}z\\ -y\\ x\end{pmatrix}.
    \tag{CDX2}
   \]
   Multiplying gives \(d_1d_2=d_2d_3=0\), with the same cancellations in characteristic two. Exactness follows from the regular-sequence mapping-cone proof of CD1, not just those zero products. Modulo the variables all matrices are zero, and the resulting vector spaces have dimensions \(1,3,3,1\). Thus they compute the four Tor groups. For any finite graded module, the double-resolution argument in CD1 identifies its minimal resolution modulo the variables with the homology of the length-three Koszul complex tensored with that module. There is no homology in higher degrees, so the higher minimal free modules are zero.

2. List the six monomials \(X_0^2,X_0X_1,X_0X_2,X_1^2,X_1X_2,X_2^2\). The monomial \(X^\alpha\) is paired with \(X^{-\alpha-\mathbf1}\); its pairing with that partner is one. Its pairing with another listed partner is zero: the coefficient of \(X_0^{-1}X_1^{-1}X_2^{-1}\) occurs precisely when the nonnegative exponents coincide. This gives the identity \(6\times6\) pairing matrix. On \(\mathbf P^3\), write the four strictly negative exponents as \(-b_i-1\). Their sum is \(-7\) exactly when \(\sum b_i=3\), so
   \[
       \dim H^3(\mathbf P^3,\mathcal O(-7))
                     =\binom{6}{3}=20 .
       \tag{CDX3}
   \]
   For a finite twist complex, the Čech evaluation map (CD6) respects the finite filtration by its terms. Each quotient has the just-proved perfect pairing; induction with the exact cohomology sequences gives perfection for the total complexes, with the internal Hom differential signs.

3. A nonzero degree-\(d\) equation is regular in the homogeneous polynomial domain, and gives
   \[
    0\to\mathcal O_{\mathbf P^3}(-d-r)
      \to\mathcal O_{\mathbf P^3}(-r)
      \to\mathcal O_X(-r)\to0 .
    \tag{CDX4}
   \]
   For \(r>0\), both left terms have no \(H^0\), and twists on \(\mathbf P^3\) have no \(H^1\) or \(H^2\). The long exact sequence proves the asserted zero groups. Apply \(0\to\mathcal O_X(-r)\to\mathcal O_X\to\mathcal O_Y\to0\) to get \(H^0(Y,\mathcal O_Y)=K\), also after algebraic closure. Thus \(Y\) is nonempty and geometrically connected. If smooth, its regular local domains make its components disjoint; connectedness forces one component, giving geometric integrality.

   The two-term resolution of \(\mathcal O_X\) has dual into \(\mathcal O_{\mathbf P^3}(-4)\)
   \[
        [\,\mathcal O(-4)\xrightarrow{\ F\ }
                            \mathcal O(d-4)\,]
        \quad\text{in degrees }0,1 .
        \tag{CDX5}
   \]
   Its degree-zero kernel is zero and its degree-one cohomology sheaf is \(\mathcal O_X(d-4)\). This explicitly illustrates the codimension-one concentration used in CD3.

4. Put \(q_0=q(u)\), \(q_1=q'(u)\). In the value,\(\partial_x,\partial_y\) rows, the first jets give
   \[
     J(u,v)=
     \begin{pmatrix}
        q_0&u q_0&v q_0\\
        q_1&q_0+u q_1&v q_1\\
        0&0&q_0
     \end{pmatrix},\qquad
                    \det J=q_0^3 .
     \tag{CDX6}
   \]
   Subtract \(u\) times column one from column two and \(v\) times column one from column three. The determinant is then the product of the three diagonal \(q_0\)'s. Each polynomial vanishes to order at least two at both marks, so these variations preserve their fixed jets.

   In characteristic two, \(q=x^4+x^2\) and \(q'=0\), but (CDX6) still has determinant \(q_0^3\); the derivatives of the multiplying coordinates supply the missing directions. In \(\mathbf F_4=\mathbf F_2[\omega]/(\omega^2+\omega+1)\), one has \(\omega^3=1\) and
   \[
                         q(\omega)=1 .
                         \tag{CDX7}
   \]
   Thus the matrix is invertible there. Vanishing derivative of \(q\) alone does not prevent full jet separation by \(q,xq,yq\).

5. A first jet on a smooth threefold has four coefficients. Surjectivity makes their vanishing four independent affine linear conditions, so the fibre of the singular incidence has dimension \(12-4=8\). Allowing its point to vary gives dimension at most \(3+8=11\). The incidence is closed in the product with the projective threefold, and its projection to \(W\) is proper, hence closed. Its image has dimension at most eleven by the function-field argument. Therefore its complement in the twelve-dimensional \(W\) is a nonempty open. One cannot replace the properness step by an unsupported assertion that every projection of a closed set is closed.

6. At the \(i\)-th mark list the other indices as \(j_1<j_2<j_3\). Use the flags
   \[
    E^4\supset\ker e_{j_1}^*
     \supset\ker e_{j_1}^*\cap\ker e_{j_2}^*
     \supset\bigcap_{h=1}^3\ker e_{j_h}^*=Ee_i .
     \tag{CDX8}
   \]
   At the successive stages use \(e_{j_1}^*\), then the restriction of \(e_{j_2}^*\), then the restriction of \(e_{j_3}^*\). Each is nonzero on the current tangent space and kills the required line. CD5 realizes these fixed first jets by actual smooth integral divisors, with high powers chosen anew on each stage. CD3 preserves connectedness at all three cuts, so CD6 gives one curve. After translation to the Lie algebra, the four final line directions are the four basis vectors. The sum-map derivative is
   \[
                       dF_{\mathbf P}=I_4 .
                       \tag{CDX9}
   \]
   The local matrix alone would not produce a global curve; the proved section construction is essential.

7. The map \(C^2\to A_E\) has invertible derivative at the chosen pair of marks. It is therefore étale there, has image containing a nonempty open, and is onto by properness and integrality of \(A_E\). It factors through \(\Phi:J_C\to A_E\) by AL5, so \(\Phi\) is onto. Its differential is onto because its composition with the differential of the sum of the Abel maps is that invertible matrix. Translation and the smooth-coordinate argument in CD7 prove that \(\Phi\) is smooth. Hence
   \[
                  g_C\ge2,\qquad \dim\ker\Phi=g_C-2 .
                  \tag{CDX10}
   \]
   The sum map is generically finite separable of a positive degree. That degree is not determined by its being étale at one point. The genus is not asserted to be two, and the kernel is not asserted connected. If \(g_C=2\), it is finite étale and \(\Phi\) is an isogeny; for larger genus it has positive dimension.

8. The differential of multiplication by an integer \(n\) at the origin is \(nI\), by adding tangent vectors. Thus \(d[p]=0\) in characteristic \(p\). Yet CU8 proves \([p]\) finite flat and surjective, of degree \(p^{2a}\); for \(a>0\) it is not étale. By contrast, the constructed \(\Phi\) has surjective differential of rank \(a\), and hence is smooth. Its differential need not be an isomorphism when \(g_C>a\). Surjectivity on the underlying points alone would not distinguish these maps or justify the tangent argument.

9. The Tate cokernel is killed by \(N=6\). Since it is a quotient of the rank-\(2a\) free \(\mathbf Z_\ell\)-module \(T_\ell(A_E)\), this gives
   \[
    \begin{array}{c|c|c}
      \ell&\text{cokernel exponent divides}&\text{cokernel order at most}\\ \hline
      2&2&2^{2a}\\
      3&3&3^{2a}\\
      5&1&1
    \end{array}
    \tag{CDX11}
   \]
   Indeed an \(\ell\)-primary quotient killed by \(\ell^e\) with at most \(2a\) generators has order at most \(\ell^{2ae}\), by mapping \((\mathbf Z/\ell^e)^{2a}\) onto it. For a compatible kernel sequence, each component class \(\xi_r\) is killed by \(\ell^r\), so lies in the finite \(\ell\)-primary subgroup of \(\mathbf Z/6\). That subgroup is killed by \(\ell\) for \(\ell=2,3\), and is zero for \(\ell=5\). Compatibility gives \(\xi_r=\ell\xi_{r+1}=0\) in the first two cases as well. This proves the exact Tate kernel \(T_\ell(K^0)\). The bounds do not determine a cokernel to be nonzero, nor specify its isomorphism class; they can be strict.

10. The construction over \(k^{\mathrm{sep}}\) uses finitely many hyperplane coefficients, marked coordinates and derivative data. A finite list of separable algebraic elements lies in one finite separable extension \(E/k\). Keeping those actual equations defines the same curve after base change and detects its geometric smoothness/integrality, as in CD6. This works for finite ground fields too. A nonempty open over a finite field need not have a point over that field:
    \[
          D(T^q-T)\subset\mathbf A^1_{\mathbf F_q}
          \quad\text{is nonempty but has no }\mathbf F_q\text{-point}.
          \tag{CDX12}
    \]
    The polynomial has derivative \(-1\), so its roots are exactly the \(q\) distinct elements of \(\mathbf F_q\). Any element of \(\mathbf F_{q^2}\setminus\mathbf F_q\) gives a point of the open, a finite separable extension. When \(a=0\), \(A\) is a point and \(J_{\mathbf P^1}\) is a point, so the map is the identity of points.

    Finally a positive-dimensional kernel cannot be the finite kernel of an isogeny. Even the exact rational Tate sequence (CD23) is not a construction of a complementary abelian subvariety or a Galois-equivariant splitting. The reducibility argument must construct that additional geometry before using isogeny transfer to obtain the desired general period presentation. \(\square\)

### 2N. Translation lines detected by one curve

Let \(A/k\) be an abelian variety. We construct, after a finite separable extension \(E/k\), a pointed smooth projective geometrically integral curve \(C\subset A_E\) and a factorization
\[
 A_E\xrightarrow{\ h\ }Q\hookrightarrow J_C
 \tag{NL1}
\]
in which \(Q\) is an abelian variety and \(h\) is a finite flat isogeny. The construction keeps the full kernel scheme, including possible nilpotents in positive characteristic. It also gives a line on \(A_E\times Q\) whose pullback along \(h\) is the normalized translation line of a symmetric ample line on \(A_E\). This is a particular family of degree-zero lines; we do not assume a dual abelian variety or a general Picard scheme for \(A\).

A free comparison for ample translation kernels is Milne's author notes [*Abelian Varieties*, Chapter I, §8, Proposition 8.1](https://www.jmilne.org/math/CourseNotes/AV.pdf). Our kernel is represented using the curve Jacobian already constructed in JC1–JC9. The family test below supplies the scheme-theoretic assertion on arbitrary bases. CD1–CD6 supply the resolutions, negative twists and connected smooth cuts; FC10 and FC13–FC14 supply the finite complexes used for base change. Reducibility and a complementary abelian subvariety remain separate requirements.

#### 2N.1. Negative twists of a line and degree-zero section tests

**NL1.** Let \(X/K\) be smooth projective geometrically integral of dimension \(n>0\), let \(H\) be very ample, and let \(L\) be any line on \(X\). Then
\[
 H^i(X,L\otimes H^{-r})=0\qquad(0\le i<n,\ r\gg0).
 \tag{NL2}
\]
If \(L\) has degree zero on every smooth projective geometrically integral curve in \(X\), after every algebraically closed field extension, a nonzero global section of \(L\) makes \(L\) trivial. For every \(r>0\),
\[
 H^0(X,L\otimes H^{-r})=0.
 \tag{NL3}
\]

For (NL2), embed \(X\) by \(H\) in \(\mathbf P^N\), and write \(i:X\hookrightarrow\mathbf P^N\). PF7 gives a surjection from a finite sum of twists to \(i_*L\), and another such surjection to its coherent kernel. The resulting presentation matrix is a matrix of homogeneous polynomials: PF6 identifies each map between two twists with a homogeneous polynomial of the corresponding degree, or zero when that degree is negative. The cokernel of this matrix of shifted graded free modules is a finite graded module whose associated sheaf is \(i_*L\). CD1 therefore gives a finite twist resolution \(F^\bullet\to i_*L\).

Put \(c=N-n\) and \(\omega=\mathcal O_{\mathbf P^N}(-N-1)\). Locally on \(X\), the line \(L\) is free of rank one. CD3's completed smooth-coordinate calculation and its faithfully detected Koszul resolution apply there without change to \(i_*L\). Thus
\[
 G^\bullet=\mathcal Hom(F^\bullet,\omega)
 \quad\hbox{has cohomology sheaves only in degree }c.
 \tag{NL4}
\]
More explicitly, the local ideal is a regular sequence of length \(c\); its dual Koszul complex is its reversed exterior complex, with cohomology only in the top degree. Comparing free resolutions by recursively lifted chain maps and homotopies identifies this calculation with that for \(F^\bullet\). This uses CD3's all-dimensional completion argument, rather than the curve-only local-ring assertion SF5.

Apply PF8 to the finitely many terms, cycles, boundaries and cohomology sheaves of \(G^\bullet(r)\). For sufficiently large \(r\) their positive cohomology vanishes. Their short exact sequences then show that the Čech total cohomology of \(G^\bullet(r)\) is concentrated in degree \(c\). CD2 consequently gives
\[
 H^i(X,L\otimes H^{-r})^\vee
   \simeq\mathbb H^{N-i}(G^\bullet(r))=0
       \quad(i<n).
 \tag{NL5}
\]
The calculation can be made over an algebraic closure; tensoring the affine Čech complex with a field extension is exact and detects vanishing. Hence it proves the assertion over \(K\).

For the section assertions, we may likewise extend to an algebraic closure. If a nonzero section of \(L\) has a zero at \(x\), choose a point \(y\) where it is nonzero. When \(n\ge2\), CD6 gives one smooth integral curve through both points, by connected smooth cuts. When \(n=1\), use \(X\) itself. The restricted section is nonzero and has a zero, so DC4 makes its line have positive degree, a contradiction. The section is therefore nowhere zero and trivializes \(L\).

A nonzero section of \(L\otimes H^{-r}\) would remain nonzero on a smooth integral curve through a point where its value is nonzero, using CD6 again. On that curve its degree is \(-r\deg H<0\), contradicting DC4. To verify the strict positivity used here, choose two distinct points of the embedded curve and a hyperplane containing one and not the other. Its nonzero restricted section has a zero, so DC4 gives \(\deg H>0\). The assertions descend by faithful field extension. \(\square\)

#### 2N.2. One negative twist for an entire family

**NL2.** Suppose \(K\) is infinite, \(n=\dim X\ge2\), and \(S\) is a quasi-compact noetherian \(K\)-scheme. Let \(\mathcal M\) be a line on \(X\times S\) whose geometric fibres have degree zero on every smooth projective curve, also after algebraically closed extension. There are arbitrarily large integers \(r>0\), and smooth geometrically integral divisors \(Y\in|H^r|\), for which
\[
 R^j\pi_{T*}(\mathcal M_T\otimes H^{-r})=0
 \qquad(j=0,1)
 \tag{NL6}
\]
for every scheme \(T\to S\). In particular \(T\) may be nonreduced or nonnoetherian.

Choose first a smooth geometrically integral divisor \(D\in|H^e|\), with \(e>0\), using CD3–CD5. Its dimension is at least one. For every geometric parameter \(s\) and every \(r>0\), NL1 on curves in \(D\) gives
\[
 H^0\bigl(D,\mathcal M_s|_D\otimes H^{-r}|_D\bigr)=0.
 \tag{NL7}
\]
The restriction sequence and its cohomology sequence therefore give an injection
\[
 H^1(X,\mathcal M_s\otimes H^{-(r+e)})
       \hookrightarrow
 H^1(X,\mathcal M_s\otimes H^{-r}).
 \tag{NL8}
\]
This is the reason a finite cover of the parameter scheme suffices: once the right side is zero at a positive multiple of \(e\), it stays zero at all larger multiples.

For each point \(s\) of \(S\), NL1 supplies such a multiple \(r_s\). The finite projective cohomology complex FC10, followed by the unit cancellations FC13–FC14, makes the vanishing locus of fibre \(H^1\) open near \(s\). Indeed \(H^0\) is already zero by NL1. After cancellation of an injective degree-zero differential modulo the residue field, cancel the injective remaining degree-one differential. The relevant invertible minors persist on an open neighbourhood. Call this neighbourhood \(U_s\). Quasi-compactness gives a finite cover by \(U_{s_1},\ldots,U_{s_m}\). Choose a multiple \(r\) of \(e\) at least as large as their \(r_{s_i}\). Injection (NL8) gives fibre \(H^1=0\) at every geometric point of \(S\).

Apply the same finite-complex cancellation at every point for this fixed \(r\). Locally the cohomology complex is homotopy equivalent to a finite projective complex with no terms in degrees zero and one. The cancelled summands are contractible by actual unit matrices. After any base change they remain contractible, and the remaining complex still has no terms in those degrees. FC10's arbitrary-base-change identification now proves (NL6), not merely vanishing after residue-field tensor. This also proves the assertion for sheaves \(R^j\pi_*\), by making the argument locally on the parameter scheme.

The same reasoning works at every larger multiple of \(e\). Choose one also beyond CD3's connectedness bound and CD4's marked-jet bound. CD5 then gives the required smooth integral \(Y\); it can be required to pass through any fixed finite collection of distinct rational points with prescribed nonzero normal covectors. The bound for (NL6) depends on the degree \(r\), not on which section defines \(Y\). \(\square\)

#### 2N.3. A curve test that retains nilpotent parameters

**NL3.** Assume \(K\) is infinite and \(X\) has a rational point \(P\). Give \(\mathcal M\) of NL2 a rigidification on \(\{P\}\times S\). There is a pointed smooth projective geometrically integral curve \(C\subset X\), containing \(P\), such that for every \(T\to S\)
\[
 \pi_{T*}\mathcal M_T
       \xrightarrow{\ \sim\ }
 \pi_{C,T*}(\mathcal M_T|_{C\times T}).
 \tag{NL9}
\]
Restriction detects rigidified triviality on all those bases:
\[
 (\mathcal M_T,\rho_T)\simeq(\mathcal O,1)
 \quad\Longleftrightarrow\quad
 (\mathcal M_T|_{C\times T},\rho_T)\simeq(\mathcal O,1).
 \tag{NL10}
\]

If \(X\) is a curve, take \(C=X\). Otherwise NL2 chooses a smooth integral cut \(Y\) through \(P\) with universally vanishing negative-twist \(R^0\) and \(R^1\). The exact sequence
\[
 0\to\mathcal M_T\otimes H^{-r}
     \to\mathcal M_T\to\mathcal M_T|_{Y\times T}\to0
 \tag{NL11}
\]
is exact after every \(T\to S\): the defining regular equation remains regular after tensor over the field, and \(\mathcal M_T\) is invertible. Its direct-image sequence gives the isomorphism of section sheaves. The restricted family on \(Y\) still has degree zero on every smooth projective curve after field extension. Repeat in dimension \(\dim Y\) until reaching one curve. Composing the isomorphisms proves (NL9); all restrictions preserve evaluation at \(P\).

If the right side of (NL10) holds, its normalized section \(1\) lifts uniquely by (NL9), locally and hence globally on \(T\). At a geometric point \(t\), this section of \(\mathcal M_t\) has value \(1\) at \(P\). NL1 makes it nowhere zero on \(X_t\). Therefore its coefficient in a local frame is outside every maximal ideal at every point of \(X\times T\), and is a unit in each local ring. It trivializes \(\mathcal M_T\), even when \(T\) has nilpotents. Its normalization is the prescribed one. Uniqueness follows either from (NL9) or from FC20's equality \(\pi_*\mathcal O_{X_T}=\mathcal O_T\). The converse is restriction. Thus the proof uses a full finite-complex base-change argument, rather than applying the reduced-base see-saw statement CE3 to a nonreduced scheme. \(\square\)

#### 2N.4. Normalized translation lines and their curve homomorphism

**NL4.** Work first over the infinite separably closed field \(K=k^{\mathrm{sep}}\). Let \(H\) be a symmetric ample line on \(A_K\), supplied by CU7, and put \(\widetilde H=H\otimes_K H_0^{-1}\), with its canonical trivialization at zero. For addition \(m\) define
\[
 \mathcal P_H
   =m^*\widetilde H\otimes p_1^*\widetilde H^{-1}
                         \otimes p_2^*\widetilde H^{-1}
       \quad\hbox{on }A_K\times A_K .
 \tag{NL12}
\]
It has canonical trivializations on both axes. It is symmetric in the two factors and additive in each, as a rigidified line family. In particular, for any parameter scheme and any two parameter maps \(a,a'\), its restrictions satisfy
\[
 \mathcal P_{a+a'}\simeq\mathcal P_a\otimes\mathcal P_{a'}.
 \tag{NL13}
\]

To check this on schemes, pull CU5's normalized cube identity to the three maps \(x,a,a'\). Its eight factors are \(\widetilde H_{x+a+a'}\), the inverses of the three pairwise sums, the three single factors, and the inverse of the zero factor. Rearranging gives exactly (NL13), with the normalization at \(x=0\). FC20 makes a rigidification-preserving isomorphism unique: its ratio with another would be a unit pulled back from the parameter scheme and equal to one on that axis. Consequently the associative and commutative compatibility diagrams commute. Symmetry of (NL12) gives additivity in the first factor too. All assertions retain arbitrary nonreduced parameters.

More generally let \(B\subset A_K\) be a positive-dimensional abelian subvariety, and restrict the first factor of \(\mathcal P_H\) to \(B\). This family has degree zero on every smooth projective curve in every geometric fibre. Indeed fix any such curve \(D\subset B_\Omega\) over an algebraically closed extension \(\Omega/K\). On \(D\times A_\Omega\), CE3 makes the Euler characteristic of this flat line family locally constant in the parameter. DC5 identifies the difference of Euler characteristics with the degree. The connected scheme \(A_\Omega\) contains the parameter zero, where the line is trivial. Its degree is therefore zero at every parameter. This argument applies over every algebraically closed extension and to every such \(D\).

Apply NL3 to \(X=B\), \(S=A_K\), \(P=0\) and this family, taking a very ample power of \(H|_B\) for the cuts. We obtain one pointed curve \(C\subset B\). The full curve Picard representation JC4–JC7 gives a morphism
\[
 h_{A,B}:A_K\longrightarrow J_C,\qquad
 a\longmapsto[\mathcal P_H|_{C\times\{a\}}],
 \tag{NL14}
\]
with its actual rigidified universal-line identification. Equation (NL13) proves it is a group homomorphism on every parameter scheme. Its restriction \(h_B:B\to J_C\) satisfies
\[
 \ker h_B(T)=
 \{b\in B(T):\mathcal P_{H|_B,b}
                 \text{ is rigidified-trivial on }B_T\}
 \tag{NL15}
\]
for every \(K\)-scheme \(T\), by (NL10). Thus the kernel here is the closed kernel scheme of a morphism into the separated scheme \(J_C\); its description is not just a set of geometric translation stabilizers. For \(B=A_K\), write \(h=h_{A,A}\). \(\square\)

#### 2N.5. Finiteness of the full ample translation kernel

**NL5.** The kernel scheme \(K_B=\ker h_B\) in (NL15) is finite over \(K\).

It is a closed proper scheme in \(B\). Extend to an algebraic closure \(\Omega\). Suppose its support has a positive-dimensional irreducible component. Give that component its reduced structure and translate one of its closed points to zero. Translation by a point of the kernel is an automorphism of the full kernel scheme, so we obtain a proper integral positive-dimensional subscheme \(Z\subset(K_B)_\Omega\) through zero. The line \(\mathcal P_{H|_B}\) on \(B_\Omega\times Z\) has trivial geometric fibres by (NL15). Since \(Z\) is reduced, the reduced-base see-saw theorem CE3 applies here: its direct image is a line and evaluation is an isomorphism. The rigidification on \(\{0\}\times Z\) identifies that direct-image line with \(\mathcal O_Z\). Hence
\[
 \mathcal P_{H|_B}|_{B_\Omega\times Z}\simeq\mathcal O.
 \tag{NL16}
\]
Pull this along \(z\mapsto(-z,z)\). Addition becomes zero; the two other factors in (NL12) become the restrictions of \([-1]^*\widetilde H|_B\) and \(\widetilde H|_B\). Since \(H\) is symmetric, (NL16) gives
\[
       (H|_Z)^{\otimes2}\simeq\mathcal O_Z .
 \tag{NL17}
\]
Constant one-dimensional factors from normalization do not change this line-isomorphism assertion. But \(H|_Z\) is ample: a very ample power of \(H|_B\) restricts to a closed projective immersion of \(Z\). Its square is ample as well. A trivial line cannot be ample on a proper integral positive-dimensional scheme over \(\Omega\). Indeed every global function there is constant: its map to \(\mathbf P^1\) has closed irreducible image by properness, and a nonconstant such map would have image all of \(\mathbf P^1\), contradicting its avoidance of infinity. A very ample trivial power would therefore give a constant map to projective space. This contradicts the positive dimension of \(Z\).

Thus the geometric support of \(K_B\) is zero-dimensional. A zero-dimensional noetherian scheme has finitely many points: a finite affine cover reduces this to a zero-dimensional noetherian ring, whose finitely many minimal primes are maximal. Proper finite-fibre finiteness from Lesson 3 makes \(K_B\to\operatorname{Spec}K\) finite. This conclusion is about the full kernel scheme. Its rank may exceed its number of geometric points, and the argument does not assert that it is étale. \(\square\)

#### 2N.6. The finite flat image inside a curve Jacobian

**NL6.** For \(B=A_K\), let \(Q\) be the scheme-theoretic image of \(h:A_K\to J_C\). Then \(Q\) is an abelian variety and
\[
       h:A_K\longrightarrow Q
 \quad\hbox{is finite flat of degree }
       d=\dim_K\mathcal O(K_A).
 \tag{NL18}
\]

The map \(h\) is proper: its graph is closed in \(A_K\times J_C\), and projection to \(J_C\) is proper. Each nonempty geometric fibre is a translate of \(K_A\) as a scheme. To see the scheme assertion, choose a point \(a\) in that fibre over the algebraically closed residue field; the inverse maps are \(x\mapsto x-a\) and \(u\mapsto a+u\), and their defining equations are exactly \(h(x)=h(a)\) and \(h(u)=0\). By NL5 all such fibres are finite. The proper finite-fibre theorem makes \(h\) finite.

On an affine open \(U\subset J_C\), its inverse image is affine and its coordinate ring is finite over \(\mathcal O(U)\). The quotient of \(\mathcal O(U)\) by the kernel of this map defines \(Q\cap U\). These kernels sheafify and glue, by localization. At a nonempty inverse image the coordinate ring is a domain, so its image subring is a domain. More globally finite \(h\) gives a closed image, which is irreducible because \(A_K\) is; these affine descriptions show that the image is reduced. The construction commutes with every field extension: kernel and finite pushforward on an affine open commute with flat scalar extension. Since \(A_K\) is geometrically integral, the same argument after algebraic closure shows that \(Q\) is geometrically integral. Lying-over for the finite integral extension shows that \(A_K\to Q\) is surjective.

Every geometric fibre over \(Q\), including a geometric generic fibre, is a translate of \(K_A\), so its length is the same integer \(d\). On an affine domain \(R\subset Q\), put \(M=\mathcal O(h^{-1}\operatorname{Spec}R)\). Its generic rank and all residue-field fibre dimensions are \(d\). FF1's domain fibre-rank lemma makes \(M\) locally free of rank \(d\). Explicitly, at a local point choose \(d\) lifts of a residue-field basis, giving \(R^d\to M\) onto by Nakayama. The kernel has rank zero after tensor with the fraction field, and is a submodule of the torsion-free module \(R^d\). It is therefore zero. This proves finite flatness and faithful flatness, since \(d>0\).

The group structure on \(J_C\) restricts to \(Q\). For example, the ideal defining \(Q\) pulls back to zero under the composite \(A_K\times A_K\to J_C\) given by addition, because this composite is \(h\) after addition on \(A_K\). The finite faithfully flat cover \(A_K\times A_K\to Q\times Q\) detects the vanishing of that ideal, proving that addition factors through \(Q\). Inversion and zero factor in the same manner. The group axioms follow from those on \(J_C\), or after the same faithful covers. Thus \(Q\) is a proper geometrically integral group scheme.

Over \(\Omega\), generic smoothness for reduced finite-type schemes over a perfect field, proved by the separating-transcendence-basis calculation in FQ3, gives a nonempty smooth open in \(Q_\Omega\). Translating a smooth closed point to any other closed point makes all closed points smooth. The nonsmooth closed locus must be empty, since a nonempty finite-type closed locus has a closed point. Hence \(Q_\Omega\) is smooth. The smooth-chart and faithful-field-descent criteria SF1–SF4 imply smoothness over \(K\). It is connected and proper, so it is an abelian variety, with projectivity also supplied by CU7. Its dimension equals \(\dim A_K\), either by the finite integral function-field extension or by finite flatness. This proves (NL18). \(\square\)

#### 2N.7. Descent of the normalized translation line

**NL7.** There is a unique rigidified line \(\mathcal P_Q\) on \(A_K\times Q\), with its descent identification, such that
\[
 (1\times h)^*\mathcal P_Q\simeq\mathcal P_H .
 \tag{NL19}
\]
Its restriction to \(C\times Q\) is the universal rigidified curve line pulled back by \(Q\hookrightarrow J_C\). Consequently the natural map
\[
 Q(T)\longrightarrow
 \{\text{isomorphism classes of lines on }A_K\times T
                       \text{ rigidified at }0\times T\}
 \tag{NL20}
\]
is injective for every \(K\)-scheme \(T\). Its image consists exactly of the classes that become a normalized translation line \(\mathcal P_a\), for some \(a\in A_K(T')\), after an fppf cover \(T'\to T\).

The relation scheme of the cover \(h\) has the explicit isomorphism
\[
 A_K\times_Q A_K\simeq A_K\times K_A,\qquad
 (a,a')\longmapsto(a,a'-a).
 \tag{NL21}
\]
This follows on all points with values in every scheme, from the equations for a group kernel; addition gives its inverse. On \(A_K\times K_A\), with the first factor now the object on which the line lives, the line \(\mathcal P_H\) is canonically trivial. Indeed its restriction to \(C\times K_A\) is rigidified-trivial by the defining Jacobian kernel, and (NL10), applied to \(T=K_A\to A_K\), gives a unique normalized trivialization on the whole \(A_K\times K_A\). This includes a nonreduced kernel.

Biadditivity (NL13) now gives a normalized isomorphism between the two pullbacks of \(\mathcal P_H\) to \(A_K\times(A_K\times_Q A_K)\). Over the triple relation scheme the two composites agree: they are rigidification-preserving isomorphisms of the same lines, and FC20 makes such an isomorphism unique. We have an actual descent datum. Apply effective faithfully flat module descent FD2, preservation of finite locally free rank one FD4, and the gluing of these affine constructions. Since \(1\times h\) is finite faithfully flat, this gives \(\mathcal P_Q\) and (NL19), with its descended rigidification. Its isomorphism is unique with the specified descent identification.

Let \(\mathcal U\) be the curve's universal rigidified line on \(C\times J_C\). By definition of \(h\), both \(\mathcal P_Q|_{C\times Q}\) and \(\mathcal U|_{C\times Q}\) pull back to the same rigidified line on \(C\times A_K\). The isomorphism and its cocycle are unique by FC20, so faithful descent identifies them. If two maps \(T\to Q\) give isomorphic rigidified lines on \(A_K\times T\), restriction to \(C\times T\) and the full Jacobian representation make their composites \(T\to J_C\) equal. The closed immersion \(Q\hookrightarrow J_C\) is a monomorphism, proving injectivity in (NL20).

A map \(q:T\to Q\) lifts fppf locally to \(a:T'\to A_K\), since \(h\) is finite faithfully flat; (NL19) then gives its line as \(\mathcal P_a\). Conversely, suppose a rigidified line \(\mathcal L\) on \(A_K\times T\) has that property. Its restriction to \(C\times T\) defines a map \(u:T\to J_C\). On the cover \(T'\), this map factors as \(h(a)\), hence through \(Q\). The ideal of \(Q\) pulls back to zero after a faithful flat cover, and is therefore zero already on \(T\). Thus \(u\) factors uniquely through \(q:T\to Q\). On the cover the two rigidified lines \(\mathcal L\) and \(\mathcal P_q\) are isomorphic; uniqueness makes the isomorphisms compatible on overlaps, so they descend. This proves the precise image assertion.

We have not identified that image with every line that might be called algebraically trivial on \(A_K\). Nor can triviality after pulling back by an isogeny, in the other factor, be used without checking its descent datum. The construction establishes exactly (NL19)–(NL20). \(\square\)

#### 2N.8. Finite separable descent and the integral Tate image

**NL8.** The data in (NL1), (NL12) and (NL19) can be constructed over a finite separable extension \(E/k\). For every prime \(\ell\ne\operatorname{char}k\), they give \(G_E\)-equivariant injections
\[
 T_\ell A_E\xrightarrow{\ T_\ell h\ }T_\ell Q
                  \hookrightarrow T_\ell J_C .
 \tag{NL22}
\]
The first cokernel has order \(\ell^{v_\ell(d)}\), where \(d=\deg h\). The second image is saturated: if a class in \(T_\ell J_C/T_\ell Q\) is killed by a power of \(\ell\), it is zero. Hence
\[
 \operatorname{Sat}_{T_\ell J_C}(\operatorname{im}T_\ell h)
       =T_\ell Q,\qquad
 V_\ell A_E\simeq V_\ell Q\subset V_\ell J_C .
 \tag{NL23}
\]
Here saturation means the elements whose some \(\ell\)-power multiple lies in the given submodule.

The curves and finitely many cuts constructed over \(k^{\mathrm{sep}}\) use finitely many equations and coefficients. They, their marked zero, and their embeddings therefore descend to a finite separable \(E/k\). Use the symmetric ample line already defined over \(k\) in CU7. JC7 gives the pointed curve Jacobian and its universal line over \(E\), and its representation defines \(h\) there from (NL12). The construction of the finite scheme image commutes with faithful field extension as proved in NL6. Finiteness, finite flatness, the kernel length and geometric smoothness are consequently detected after \(k^{\mathrm{sep}}/E\).

The curve test and its normalized isomorphisms descend too. For any \(E\)-scheme \(T\), apply the test after the faithfully flat cover \(T_{k^{\mathrm{sep}}}\to T\). A normalized trivialization is unique by FC20; its two pullbacks agree, so FD2 descends it. Thus the actual full kernel and descent construction over \(E\) are those just proved over \(K\), not a replacement by geometric points. Alternatively apply finite faithfully flat descent directly to the already constructed \(E\)-map \(h\) and its relation scheme.

CU10 gives injectivity of \(T_\ell h\) and the asserted exact finite index for any isogeny, including one whose degree has an inseparable factor. The closed immersion \(Q\hookrightarrow J_C\) gives an injection of torsion points and inverse limits. To prove saturation, write \(t=(t_r)_{r\ge1}\in T_\ell J_C\), with \(t_r=\ell t_{r+1}\). If \(\ell^e t\in T_\ell Q\), then for every \(r\)
\[
             t_r=\ell^e t_{r+e}\in Q.
 \tag{NL24}
\]
Each \(t_r\) is already killed by \(\ell^r\) and all transition equations hold in \(Q\), so \(t\in T_\ell Q\). Since the finite cokernel of the first map in (NL22) is killed by an \(\ell\)-power, its image saturates to all \(T_\ell Q\). Saturation inside the larger module is exactly \(T_\ell Q\), by the result just proved. Tensor with \(\mathbf Q_\ell\) to obtain (NL23). All maps come from maps over \(E\), so they commute with \(G_E\); no equivariant splitting has been inferred.

If \(\dim A=0\), take \(C=\mathbf P^1_E\), \(A_E=Q=J_C=0\), \(d=1\), and the trivial lines. For positive dimension, the constructed \(Q\) has dimension \(\dim A\); the inclusion in \(J_C\) need not have the same dimension as \(J_C\). An abelian complement to \(Q\), or an isogeny retraction from \(J_C\) onto it, has not been constructed here. Likewise the earlier surjection CD7 has not acquired a splitting merely from (NL1). Those are the remaining reducibility assertions. \(\square\)

#### 2N.9. Graded exercise: families, kernels and Tate saturation

**Exercise 2N (100 points; ten parts of 10 points).**

1. On \(\mathbf P^2_K\), take \(H=\mathcal O(1)\) and \(L=\mathcal O(a)\), \(a\in\mathbf Z\). Determine exactly when \(H^0(LH^{-r})\) and \(H^1(LH^{-r})\) vanish, for \(r>0\). Explain which part of NL1 needs the degree-zero hypothesis.
2. In NL2 take \(e=6\), and suppose three opens covering the parameter scheme have respective vanishing thresholds \(6,12,18\), all in the progression of positive multiples of \(e\). List the first three common allowable degrees. State the direction of the cohomology injection that makes the argument work. Explain why no relative duality theorem was needed.
3. Let \(R=K[\epsilon]/(\epsilon^2)\). Compare the complexes \([R\xrightarrow{1}R]\) and \([R\xrightarrow{\epsilon}R]\) in degrees zero and one, before and after reduction modulo \(\epsilon\). For a genus-one curve, construct a line over \(R\) with trivial closed fibre that is not itself trivial. Identify why NL3 can nevertheless test the actual family on a curve.
4. Expand the ratio \(\mathcal P_{a+a'}\otimes\mathcal P_a^{-1}\otimes\mathcal P_{a'}^{-1}\) using (NL12), including its parameter-only factors. Match it with the normalized cube at \((x,a,a')\). Explain why the resulting biadditivity isomorphisms satisfy the cocycle identity.
5. Compute the pullback of \(\mathcal P_H\) by \(z\mapsto(-z,z)\), with the normalization at zero included. Suppose \(H\) is symmetric and the resulting line is trivial on a proper integral \(Z\). Prove \(\dim Z=0\) when \(H|_Z\) is ample. Explain the role of reducedness in the use of see-saw.
6. Let \(E\) be an elliptic curve and \(H=\mathcal O_E(m[0])\), \(m>0\). Take \(C=E\) and identify \(J_E\) with \(E\) using \(a\mapsto\mathcal O_E([a]-[0])\). Compute \(h\), its full kernel and its degree. In characteristic \(p\), discuss \(m=p\) and the indices on \(T_\ell\) for \(\ell\ne p\).
7. In characteristic \(p\), prove that \(K[x]\) is free of rank \(p\) over \(K[u]\) under \(u\mapsto x^p\). Compute every geometric fibre and the relation algebra of the cover. Explain why a single geometric point in each fibre does not imply an isomorphism or an étale map.
8. Over a field of characteristic \(p\), set \(R=K[u,u^{-1}]\), \(B=K[x,x^{-1}]\), \(u=x^p\). Compute the \(\mu_p\)-grading and the weight-one descent module. Write the character cocycle on the relation scheme. Distinguish a trivial underlying line after pullback from the trivial descent identification.
9. Let \(M=\mathbf Z_\ell^4\), \(Q_0=\mathbf Z_\ell e_1\oplus\mathbf Z_\ell e_2\), and \(I=\mathbf Z_\ell\ell^2e_1\oplus\mathbf Z_\ell\ell^3e_2\). Compute \(Q_0/I\), its order, and the saturation of \(I\) in \(M\). Give the compatible-torsion argument proving saturation for an actual abelian subvariety.
10. Prove the image description in (NL20) by descending a local lift through \(A\to Q\). Explain why finite separable descent is available, and why the constructed inclusions and surjections involving Jacobians do not yet prove an isogeny decomposition.

**Full solution.**

1. PF5–PF6 gives
   \[
    h^0(\mathbf P^2,\mathcal O(a-r))=
    \begin{cases}\binom{a-r+2}{2}&a-r\ge0,\\0&a-r<0,\end{cases}
    \qquad H^1(\mathbf P^2,\mathcal O(a-r))=0.
    \tag{NLX1}
   \]
   Thus both groups vanish exactly for \(r>a\), subject to \(r>0\); degree-one cohomology vanishes for every integer twist. The eventual negative vanishing of NL1 holds for every line. The conclusions that a section of the line trivializes it, and that every strictly negative twist has no section, use degree zero on curves. For example \(a=2,r=1\) has three sections, so eventual vanishing for arbitrary lines cannot be replaced by vanishing at every positive \(r\).

2. The first three choices guaranteed by the three bounds are \(18,24,30\). They may be enlarged further for the smooth-section and marked-jet bounds. The injection is
   \[
    H^1(\mathcal M_sH^{-(r+6)})
          \hookrightarrow H^1(\mathcal M_sH^{-r}).
    \tag{NLX2}
   \]
   Its source is the group at the larger positive integer \(r+6\). A zero target forces that source to be zero. The preceding \(H^0\) on the auxiliary divisor is zero by the negative-degree curve test. Individual eventual vanishing came from a finite resolution and the explicit projective duality calculation CD2. Openness and arbitrary base change came from the finite complexes FC10 and their actual unit cancellations. The proof therefore needs neither a uniform relative dualizing complex nor a general relative duality theorem.

3. The identity complex is contractible over \(R\), with inverse differential one, and stays so after every base change. For the other complex,
   \[
      H^0=\epsilon R,\qquad H^1=R/\epsilon R.
      \tag{NLX3}
   \]
   After reduction its differential is zero and both cohomology spaces are \(K\). In particular the map \(H^0\otimes_RK\to H^0([K\xrightarrow0K])\) is zero: the inclusion \(\epsilon R\hookrightarrow R\) reduces to zero. Fibre dimensions do not give a trivialized complex.

   For a smooth projective genus-one curve \(D\), choose a nonzero Čech class \((c_{ij})\) in \(H^1(D,\mathcal O_D)\), whose dimension is one by SD. On an affine cover glue frames by \(1+\epsilon c_{ij}\). The additive cocycle equation and \(\epsilon^2=0\) give the multiplicative cocycle equation. A trivialization would have reduction a nowhere-zero function, hence a constant by FC20; divide by that constant. Its frames would then be \(1+\epsilon b_i\), making \(c_{ij}=b_j-b_i\), a contradiction. Tensoring off the line at a chosen point gives a rigidification without changing this conclusion.

   Consequently reduced-fibre triviality alone is insufficient on a nonreduced parameter scheme. NL3 instead proves an isomorphism of section sheaves after **every** base change. Its lifted section has value one at the marked point and is fibrewise nowhere zero; its local coefficients are then units. For \(X=D\), the testing curve is \(D\) itself, so the nontrivial infinitesimal line is detected.

4. Write \(H_b\) for the pullback of \(\widetilde H\) by the indicated map \(b\). Direct expansion gives
   \[
    H_{x+a+a'}H_{x+a}^{-1}H_{x+a'}^{-1}
       H_x H_a H_{a'}H_{a+a'}^{-1}.
    \tag{NLX4}
   \]
   Tensor products of the written line factors are understood. The zero factor of the normalized cube is \(H_0^{-1}\), canonically trivial. With that factor inserted, (NLX4) is exactly its eight-factor expression. The factors \(H_a,H_{a'},H_{a+a'}^{-1}\) are necessary; omitting them destroys the rigidification. The cube trivialization respects \(x=0\). Any two such isomorphisms have a unit ratio pulled back from the parameter scheme, by FC20; its value at \(x=0\) is one. Thus the isomorphisms are unique, and the two composites for three parameters agree. This proves the cocycle compatibility on nonreduced bases as well.

5. Since addition is zero on the anti-diagonal, the pullback is
   \[
     \widetilde H_0\otimes
           ([-1]^*\widetilde H|_Z)^{-1}
                   \otimes(\widetilde H|_Z)^{-1}.
     \tag{NLX5}
   \]
   The first factor is canonically trivial. Symmetry identifies the last two unnormalized line factors with \(H|_Z^{-2}\), up to constant lines. Triviality therefore implies \(H|_Z^2\simeq\mathcal O_Z\). A high power is very ample and also trivial. Every global function on \(Z\) is constant, by the proper-map-to-\(\mathbf P^1\) argument of NL5, so its projective map is constant. It cannot embed a positive-dimensional \(Z\).

   The \(Z\) used in NL5 is explicitly the reduced structure of a translated irreducible component of the geometric kernel support. Thus CE3's reduced-base hypothesis holds exactly where it is used. Reducedness is not asserted for the full kernel; its nilpotents remain part of its finite length.

6. Translation pulls the divisor \([0]\) back to \([-a]\). Parameter-only factors disappear in the divisor class, so
   \[
       h(a)=-[m]a,\qquad K_A=E[m],\qquad d=m^2.
       \tag{NLX6}
   \]
   The identification \(J_E\simeq E\) is JC's genus-one Abel isomorphism; tensoring divisor lines corresponds to addition under it. Thus the displayed formula is an equality of morphisms, including their full kernel schemes, since both arise from the same universal rigidified family.

   For \(m=p=\operatorname{char}K\), the kernel has rank \(p^2\); it must not be replaced by its geometric points. The differential of \([p]\) is multiplication by \(p\) on the tangent line, hence zero, so this positive-degree finite map is not étale. For \(\ell\ne p\), \(v_\ell(d)=0\); CU10 gives an isomorphism on \(T_\ell\). This does not make the original finite map an isomorphism.

7. Division of an exponent by \(p\) uniquely writes every polynomial as
   \[
          \sum_{j=0}^{p-1} f_j(x^p)x^j .
          \tag{NLX7}
   \]
   The monomials occurring in different summands have distinct residues modulo \(p\), proving independence as well as generation. Over an algebraically closed residue field at \(u=b\), choose the unique \(a\) with \(a^p=b\). Its fibre algebra is
   \[
       \Omega[x]/(x^p-b)\simeq\Omega[v]/(v^p),
       \qquad v=x-a.
       \tag{NLX8}
   \]
   It has length \(p\) and one geometric point. The relation algebra is
   \[
       K[x,x']/(x'^p-x^p)
              \simeq K[x,v]/(v^p),\qquad v=x'-x.
       \tag{NLX9}
   \]
   These nilpotents rule out étaleness and, for \(p>1\), an isomorphism. The basis proves finite flatness directly. This affine model illustrates why NL6 keeps fibre lengths, rather than counting points.

8. The same exponent calculation, now allowing negative powers, gives the grading
   \[
     B=\bigoplus_{j=0}^{p-1}R x^j,\qquad
       \delta(x)=x\otimes z,\qquad
       \mathcal O(\mu_p)=K[z]/(z^p-1).
       \tag{NLX10}
   \]
   The weight-one module is \(B_1=Rx\), free of rank one over \(R\). Multiplication by \(x\) trivializes its pullback to \(B\). The relation scheme is \(B[z]/(z^p-1)\), with \(x'=xz\); its character transition is \(z=x'/x\). On the triple relation scheme,
   \[
       \frac{x'}x\,\frac{x''}{x'}=\frac{x''}x.
       \tag{NLX11}
   \]
   This proves the cocycle identity. In characteristic \(p\), \(z^p-1=(z-1)^p\), so its character is one at the sole geometric point while remaining different from one as a function. The underlying descended module here is indeed free, but its specified pullback identification has transition \(z\), rather than transition one. Ignoring that identification erases real descent information. NL7 supplies the normalized transition isomorphisms and checks their cocycle, including on nilpotent relation schemes.

9. The coordinates are independent, so
   \[
       Q_0/I\simeq
        \mathbf Z_\ell/\ell^2\oplus\mathbf Z_\ell/\ell^3,
        \qquad [Q_0:I]=\ell^5.
        \tag{NLX12}
   \]
   Every element of \(Q_0\) is sent into \(I\) by \(\ell^3\). An element of \(M\) with a nonzero third or fourth coordinate has no \(\ell\)-power multiple in \(I\), since \(\mathbf Z_\ell\) is torsion-free. Thus the saturation is precisely \(Q_0\).

   For a closed abelian subvariety \(Q\subset J\), suppose \(\ell^e t\in T_\ell Q\). Compatibility gives \(t_r=\ell^e t_{r+e}\); the right side belongs to \(Q\), so each \(t_r\) is a point of \(Q[\ell^r]\). The same compatibility holds there, proving \(t\in T_\ell Q\). This geometric argument proves the saturation assertion without assuming a complement or a Galois-equivariant direct-sum decomposition.

10. A map \(q:T\to Q\) lifts along the finite faithfully flat map \(A\to Q\) after the cover \(T'=T\times_QA\to T\). Equation (NL19) identifies its line with a normalized translation line there. Conversely a rigidified line locally of that form restricts to \(C\) and yields \(u:T\to J_C\). After the cover its map is \(h(a)\), so the ideal of \(Q\) vanishes after faithful flat pullback and hence before it. This gives a unique \(q:T\to Q\). The local line isomorphisms descend because their rigidifications make them unique on overlaps. This proves precisely the image statement of (NL20).

   The chosen curves and cuts have finitely many coefficients in \(k^{\mathrm{sep}}\), so they descend to a finite separable extension. The Jacobian is constructed there from its pointed curve; the line family defines its map there. The kernel, finite flatness, image and normalized descent are detected by faithful field extension as in NL8. Finally a saturated submodule of a Tate module is not a constructed abelian complement. Neither an algebraic retraction \(J_C\to Q\) nor a complementary subvariety has been provided by this argument. The smooth surjection from CD7 and the finite map into a possibly different curve Jacobian here retain their stated directions. Poincaré reducibility still requires its own proof.

### 2O. Abelian complements and a Jacobian isogeny factor

We now construct the complement needed after CD7. If \(B\hookrightarrow A\) is an abelian subvariety over \(k\), then there is an abelian subvariety \(D\subset A\), defined over \(k\), such that addition is an isogeny
\[
             B\times D\longrightarrow A.
             \tag{NR1}
\]
Applied to the connected kernel of CD7, this makes \(A_E\) an actual isogeny factor of the dominating curve Jacobian. The proof uses the translation-line families of §2N, not an assumed general Picard scheme for an abelian variety.

A free comparison is Conrad's [*Abelian Varieties*, §§5.1 and 7.6](https://math.stanford.edu/~conrad/249CS15Page/handouts/abvarnotes.pdf). We prove the cohomological dimension bound, the degree-one coproduct argument, the image and flatness assertions, and the full-kernel descent used below. No Hopf structure theorem, dual abelian variety or complement is being taken from a citation.

#### 2O.1. Coherent dimension and the coproduct bound

**NR1.** If \(X/K\) is smooth projective geometrically integral of dimension \(g\), then \(H^i(X,\mathcal O_X)=0\) for \(i>g\). If \(X=A\) is an abelian variety, then
\[
                 \dim_K H^1(A,\mathcal O_A)\le g.
                 \tag{NR2}
\]

We first justify the dimension bound using exactly the projective calculation already proved. Extend to an algebraic closure, where field base change on the affine Čech complex is exact. Embed \(X\) in \(\mathbf P^N\) and take CD1's finite twist resolution \(F^\bullet\to\mathcal O_X\). Write \(c=N-g\). By CD3's local smooth-coordinate and dual Koszul calculation, \(G^\bullet=\mathcal Hom(F^\bullet,\mathcal O(-N-1))\) has coherent cohomology sheaves only in degree \(c\).

Consequently its Čech total cohomology vanishes below \(c\). Here is the truncation argument. Replace its degree-\(c\) term by its kernel and discard higher terms, then map that truncated complex onto its single cohomology sheaf in degree \(c\). Both comparison maps are quasi-isomorphisms. On every intersection of standard projective affine opens, sections of coherent sheaves are exact by SC; their mapping-cone complexes are therefore exact there. The finite signed total-complex argument SH9 makes their Čech total complexes quasi-isomorphic as well. The single sheaf in degree \(c\) has no total terms below that degree. CD2 now identifies
\[
 H^i(X,\mathcal O_X)^\vee\simeq\mathbb H^{N-i}(G^\bullet)=0
                      \qquad(i>g).
 \tag{NR3}
\]
This proof uses neither a general cohomological dimension theorem nor an unproved higher-dimensional duality theorem.

We need the product calculation in all degrees. Take finite affine covers of proper separated \(X,Y\). Their intersections and their products are affine. The two augmented Čech resolutions tensor to a double resolution of the structure sheaf on \(X\times Y\): locally a chosen covering index contracts each augmented direction. Its terms are acyclic on these product affines. The resulting global total complex is the signed tensor product of the two Čech complexes. Over a field, every complex of vector spaces splits as its cohomology with zero differential plus contractible two-term summands, by choosing complements to cycles and boundaries. Tensoring preserves the contractions. Thus external cup product gives
\[
 H^q(X\times Y,\mathcal O)=
       \bigoplus_{u+v=q}H^u(X,\mathcal O_X)\otimes_K H^v(Y,\mathcal O_Y).
 \tag{NR4}
\]
This is CU2's computation in every degree, with the same natural maps. Tensor multiplication has the sign for passing a class in the second factor past one in the first.

For completeness, the needed interchange of degree-one Čech classes has an explicit homotopy. If \(\alpha_{ij},\beta_{ij}\) are additive one-cocycles, put \(h_{ij}=\alpha_{ij}\beta_{ij}\). Their cocycle equations give
\[
    (\delta h)_{ijk}
       =-\alpha_{ij}\beta_{jk}-\beta_{ij}\alpha_{jk}.
       \tag{NR5}
\]
Hence their cup products anticommute in cohomology, in characteristic two as well. Ordered cup product is associative and natural under pullback. Formula (NR5) verifies the signs needed when multiplying the degree-one external classes used next.

Let \(V=H^1(A,\mathcal O_A)\), \(r=\dim V\), and let \(v_1,\ldots,v_r\) be a basis. The multiplication morphism induces a coproduct on cohomology. CU2 identifies its degree-one part, since both axis restrictions are the identity:
\[
       m^*v=v\otimes1+1\otimes v,\qquad v\in V.
       \tag{NR6}
\]
Iterate addition to \(A^r\). Pull back the product \(v_1\cdots v_r\) and project (NR4) to multidegree \((1,\ldots,1)\). Naturality, associativity and the tensor signs give
\[
 \sum_{\sigma\in S_r}\operatorname{sgn}(\sigma)\,
                v_{\sigma(1)}\otimes\cdots\otimes v_{\sigma(r)}.
 \tag{NR7}
\]
Every summand is a different tensor-basis vector; the identity permutation has coefficient one. Thus (NR7) is nonzero over every field. In particular there is no division by \(r!\), which could be zero in the field. It follows that \(H^r(A,\mathcal O_A)\ne0\) when \(r>0\). Bound (NR3) implies \(r\le g\); for \(r=0\) the inequality is immediate. This proves (NR2). \(\square\)

#### 2O.2. Tangent lines give the reverse bound

**NR2.** For every abelian variety \(A/K\),
\[
                 \dim_K H^1(A,\mathcal O_A)=\dim A.
                 \tag{NR8}
\]
The vector space of first-order deformations of the trivial line on \(A\), rigidified at zero, is \(H^1(A,\mathcal O_A)\).

To prove the last assertion, put \(R=K[\epsilon]/(\epsilon^2)\), and use a finite affine cover. A line on \(A_R\) whose reduction is trivial is free on each lifted affine: lift a generator and use nilpotent Nakayama and the rank-one projective-module splitting, exactly as in CU3. After choosing frames with prescribed trivial reduction, its transitions have the form \(1+\epsilon c_{ij}\). The line cocycle equation is precisely the additive Čech cocycle equation for \(c\), and frame changes \(1+\epsilon b_i\) change it by a boundary. Any trivialization of the reduced line differs by a global constant, by FC20; scaling a frame by that constant does not change the class. Tensoring off its fibre at zero supplies a rigidification. Conversely two rigidifications differ by a unit of \(R\), which extends as a global unit, so they give the same isomorphism class. Tensor product of lines adds the cocycles, and \(\epsilon\mapsto\lambda\epsilon\) scales them. This proves the stated vector-space identification.

After the finite separable extension used in NL6–NL8, the abelian variety \(Q\) there has dimension \(g=\dim A\). NL20 gives a monomorphism from its point functor to rigidified line classes on \(A\). At the identity, this induces an injective linear map
\[
                    T_0Q\hookrightarrow H^1(A,\mathcal O_A).
                    \tag{NR9}
\]
Injectivity can be checked directly: a tangent vector is a map from the dual numbers reducing to zero, and the zero line class has only the zero such map by NL20. Group addition and scalar substitution give linearity. Since \(Q\) is smooth of dimension \(g\), the left side has dimension \(g\). Combine with NR1's upper bound. Field extension does not change the cohomology dimension, by the exact Čech tensor comparison, so the result holds over the original field. \(\square\)

#### 2O.3. Images of homomorphisms and faithful flatness

**NR3.** The scheme-theoretic image \(R\) of a homomorphism \(f:X\to Y\) of abelian varieties is an abelian subvariety of \(Y\), and \(X\to R\) is faithfully flat and of finite presentation. Its kernel is retained as a full scheme.

The map \(f\) is projective, hence proper: its graph is closed, and projection from the projective \(X\) is projective. The kernel of \(\mathcal O_Y\to f_*\mathcal O_X\) is a coherent ideal by the earlier projective direct-image result. It defines \(R\). On any affine open of \(Y\) with nonempty inverse image, sections on that inverse image form a domain, because \(X\) is integral. The image quotient ring is a domain. Properness makes the underlying image closed and irreducible, so \(R\) is integral and \(X\to R\) is surjective.

This formation commutes with field extension. For an affine open of \(Y\), compute sections on its quasi-compact separated inverse image by the kernel of the first map of a finite affine Čech complex. Flat extension commutes with that kernel and with the coordinate rings of the affine intersections. It therefore commutes with \(f_*\mathcal O_X\) and the defining ideal. Since \(X\) is geometrically integral, the same domain argument shows that \(R\) is geometrically integral.

Over an algebraic closure \(\Omega\), every \(\Omega\)-point of \(R\) lifts to an \(\Omega\)-point of \(X\): a nonempty finite-type fibre has a closed point. Addition and inversion on \(Y\) consequently preserve the geometric points of \(R\). Their pulled-back defining equations vanish on all closed points of the reduced schemes \(R_\Omega\times R_\Omega\) and \(R_\Omega\), so they vanish as functions, by the finite-type radical-ideal assertion B1. Thus these maps restrict as scheme maps. The restrictions descend by faithful field extension. Their group axioms follow from those on \(Y\).

FQ3's separating-transcendence-basis proof gives a nonempty smooth open in the integral \(R_\Omega\). Translation carries a smooth closed point to every other closed point, so smoothness holds everywhere. A nonempty closed complement would contain a closed point. Smoothness descends to the ground field by SF's relation-gradient criterion. Hence the proper geometrically integral group \(R\) is an abelian variety.

We give the generic-flatness calculation needed for \(X\to R\). If \(D\) is a noetherian domain, \(F\) its fraction field, and \(C=D[t_1,\ldots,t_s]/I\) is a finite-type algebra, then some nonzero localization \(C_a\) is free, possibly of infinite rank, over \(D_a\). Choose a monomial order. The ideal of leading monomials of \(I_F\) is finitely generated, since the polynomial ring is noetherian. Choose monic polynomials \(g_1,\ldots,g_m\in I_F\) with these leading monomials. Division terminates because that order is well ordered and decreases each leading monomial.

Clear the finitely many denominators of the \(g_i\), their expressions in a fixed finite generating set for \(I\), and the expressions of those generators in the \(g_i\). After inverting one \(a\ne0\), they generate \(I_a\) and remain monic. Monic division now works over \(D_a\). The monomials not divisible by any leading monomial span the quotient. They are independent: a nonzero relation among them would remain a nonzero element of \(I_F\) over \(F\), contradicting the definition of its leading-monomial ideal. This proves freeness. If \(I_F\) is the whole ring, the same denominator clearing makes \(C_a=0\), also a free module.

Apply this on a finite affine cover of the inverse image of a nonempty affine open in \(R_\Omega\). A common localization makes every coordinate algebra flat over that base open. Thus \(f\) is flat over some nonempty open \(U\) of \(R_\Omega\). Fix \(u\in U(\Omega)\). For any \(r\in R(\Omega)\), choose \(x\in X(\Omega)\) with \(f(x)=r-u\). The translation square for \(x\) on \(X\) and \(r-u\) on \(R\) identifies the map over \(U+r-u\) with the map over \(U\). These flat opens cover all closed points and therefore all of \(R_\Omega\). Flatness descends from \(\Omega\), by faithful tensor detection. Surjectivity and finite presentation were already established, so the map is an fppf cover. \(\square\)

#### 2O.4. The restricted translation family has the right dimension

**NR4.** Let \(0\ne B\subset A\), and choose a symmetric ample line \(H\) on \(A\). After a finite separable extension, NL4's homomorphism
\[
       f=h_{A,B}:A\longrightarrow J_C
       \tag{NR10}
\]
has image equal to the image \(Q_B\) of its restriction \(h_B:B\to J_C\). In particular \(f:A\to Q_B\) is an fppf cover, and \(h_B:B\to Q_B\) is an isogeny.

Work first over \(k^{\mathrm{sep}}\). The pointed curve \(C\subset B\) in NL4 tests the full family \(\mathcal M=\mathcal P_H|_{B\times A}\), on every parameter scheme mapping to \(A\). By NR3, the image \(R\subset J_C\) is an abelian variety and \(f:A\to R\) is faithfully flat. The finite-kernel assertion NL5 and the proper finite-fibre theorem make \(h_B\) finite onto its image. The finite-image proof NL6, applied to this same curve and its full translation kernel on \(B\), makes \(Q_B\) an abelian variety of dimension \(b=\dim B\), with finite flat map \(h_B\). It is a closed subvariety of \(R\).

We must bound \(\dim R\); the differential of \(f\) alone would not do so in positive characteristic. Instead descend the actual line \(\mathcal M\) to \(B\times R\). On the full kernel \(K=\ker(A\to R)\), the curve restriction is rigidified-trivial by the curve Jacobian representation. NL3, with the parameter map \(K\to A\), makes \(\mathcal M|_{B\times K}\) canonically rigidified-trivial, including all nilpotents of \(K\). Biadditivity gives the normalized transition isomorphisms on
\[
        A\times_R A\simeq A\times K.
        \tag{NR11}
\]
They satisfy the cocycle identity by FC20's uniqueness. Effective descent of invertible modules FD2–FD4 now gives a rigidified line \(\mathcal M_R\) on \(B\times R\).

This descent works although the fppf cover \(A\to R\) need not be finite. On an affine open of \(B\times R\), take a finite affine open cover of its quasi-compact inverse image in \(B\times A\). The finite disjoint union of these affines is an affine faithfully flat cover of that open. Apply FD2 to this affine cover and its full overlap datum; rank-one projectivity descends by FD4. Uniqueness glues the descended modules on overlapping target affines. Thus only the already proved faithfully flat module descent is used.

Restriction of \(\mathcal M_R\) to \(C\times R\) is the universal curve line pulled back along the closed immersion \(R\hookrightarrow J_C\). Indeed their pullbacks along the cover \(A\to R\) agree, and the normalized isomorphisms descend uniquely. Therefore \(R(T)\) injects into rigidified line classes on \(B_T\), for every \(T\), by restriction to \(C\). NR2's dual-number calculation gives
\[
                T_0R\hookrightarrow H^1(B,\mathcal O_B).
                \tag{NR12}
\]
It follows that \(\dim R\le b\), by smoothness and (NR8). Since \(Q_B\subset R\) already has dimension \(b\), the two integral closed varieties are equal: a proper closed subset of an integral finite-type variety has smaller dimension by GQ1. This proves the assertions.

All chosen curve equations and marked data involve finitely many coefficients of \(k^{\mathrm{sep}}\); descend them to a finite separable extension. Their Jacobian and map are defined there by JC7 and the universal line. NR3's image formation commutes with faithful field extension. Equality of the two images, finiteness and flatness are consequently detected there, so all conclusions hold over that finite extension. No representation of every algebraically trivial line on \(B\) was needed. \(\square\)

#### 2O.5. Killing a finite kernel and reversing an isogeny

**NR5.** A finite commutative group scheme \(K/k\) of rank \(d\) is killed by some positive integer defined solely from \(d\) and the characteristic. One may take
\[
 n=d!\quad(\operatorname{char}k=0),\qquad
 n=d!\,p^d\quad(\operatorname{char}k=p>0).
 \tag{NR13}
\]
Consequently any isogeny \(q:X\to Y\) of abelian varieties admits an isogeny \(u:Y\to X\), over the same field, with
\[
                  uq=[n]_X,\qquad qu=[n]_Y.
                  \tag{NR14}
\]

Extend first to an algebraic closure \(\Omega\). In characteristic zero, FF5's finite-group Cartier proof makes \(K_\Omega\) a product of points. Its point group has order \(d\), hence is killed by \(d!\). In characteristic \(p\), its geometric point group has order at most \(d\), so every point is killed by \(d!\), by the elementary coset proof of Lagrange's theorem. Thus \([d!]\) maps the whole scheme into the open-and-closed identity component \(K^0_\Omega\): the inverse image of any other component has empty support and is empty.

The coordinate ring of \(K^0_\Omega\) is a local Artinian algebra of length at most \(d\), with augmentation ideal \(\mathfrak m\). Its powers satisfy \(\mathfrak m^d=0\). Indeed an equality of two consecutive powers makes that finite module zero by Nakayama; until then every strict inclusion reduces its vector-space dimension by at least one. On the cotangent space at the identity, multiplication by \(p\) is the sum of \(p\) identity maps, hence zero. This follows directly by applying the two augmentations to the coproduct: modulo the product of the two augmentation ideals, its expression is \(x\otimes1+1\otimes x\). Thus
\[
              [p]^*\mathfrak m\subset\mathfrak m^2,\qquad
              [p^e]^*\mathfrak m\subset\mathfrak m^{2^e}.
              \tag{NR15}
\]
Taking \(e=d\) kills that ideal, since \(2^d\ge d\). The morphism \([p^d]\) on \(K^0_\Omega\) is therefore the identity-section constant map. Composition with \([d!]\) proves (NR13). Faithful field extension detects equality of morphisms, so the annihilation holds over \(k\), not only on its geometric points.

For (NR14), \(q\) is finite faithfully flat by CE6. Its relation scheme is \(X\times\ker q\), with the two maps differing by kernel translation. Formula (NR13) makes \([n]_X\) invariant on that full relation. Finite faithfully flat morphism descent FD5 gives \(u\) and \(uq=[n]_X\). Faithful descent detects the group law. Composing with \(q\) and cancelling the same cover gives \(qu=[n]_Y\).

The map \(u\) is proper. Each of its geometric fibres lies in a fibre of \(qu=[n]_Y\), so is finite. Proper finite-fibre finiteness makes \(u\) finite. Its image contains that of \(uq=[n]_X\), hence is all \(X\). CE6 then makes it finite flat. If \(\dim X=\dim Y=b\), composition of the finite function-field degrees and CU8 give
\[
                   \deg u=\frac{n^{2b}}{\deg q}.
                   \tag{NR16}
\]
This proves both existence of the reverse isogeny and integrality of this degree without assuming that a nonreduced kernel is killed by the number of its geometric points. \(\square\)

#### 2O.6. An integral multiple of a projector over the original field

**NR6 (abelian complement).** For any abelian subvariety \(\iota:B\hookrightarrow A\) over \(k\), there are an integer \(t>0\), a homomorphism \(r:A\to B\), and an abelian subvariety \(D\subset A\), all over \(k\), such that
\[
 r\iota=[t]_B,\qquad
 v=[t]_A-\iota r,\qquad
 D=\operatorname{im}v,\qquad rv=0.
 \tag{NR17}
\]
Addition \(g:B\times D\to A\) is an isogeny.

For \(B=0\), take \(t=1\), \(D=A\), and the zero \(r\). Otherwise NR4, after a finite separable extension \(E/k\), gives \(f:A_E\to Q_B\) whose restriction \(q:B_E\to Q_B\) is an isogeny. Choose \(u:Q_B\to B_E\) from NR5. Then \(r_E=uf\) satisfies \(r_E\iota=[n]_B\).

We descend a multiple of this map, so the complement will be over \(k\) itself. Enlarge \(E\) to a finite Galois extension \(L/k\), with group \(\Gamma\). On \(A_L\), form the sum of conjugate homomorphisms
\[
                 r_L'=\sum_{\sigma\in\Gamma}\sigma(r_E).
                 \tag{NR18}
\]
Conjugation permutes the summands, so this map has the actual Galois descent datum. The field relation \(L\otimes_k L\simeq\prod_{\sigma\in\Gamma}L\) and FD5's finite faithfully flat morphism descent give a homomorphism \(r:A\to B\). Its restriction to \(B\) is multiplication by \(t=n|\Gamma|>0\). This remains a nonzero multiplication isogeny when the characteristic divides \(t\), by CU8.

Define \(v\) by (NR17). Direct composition gives \(v\iota=0\) and \(rv=tr-r\iota r=0\). NR3 makes its scheme-theoretic image \(D\) an abelian subvariety over \(k\), with fppf cover \(A\to D\). In particular the zero composite \(rv\) implies \(r|_D=0\), detected after that cover; hence \(v|_D=[t]_D\).

Let \(K=B\times_A D\), the full scheme intersection inside \(A\). Since \(r|_B=[t]\) and \(r|_D=0\), it is a closed subgroup scheme of \(B[t]\), and is finite. The kernel of addition is exactly
\[
       K\xrightarrow{\ \sim\ }\ker g,\qquad
                  b\longmapsto(b,-b).
       \tag{NR19}
\]
Both inverse identities are valid on every parameter scheme. Every nonempty geometric fibre of \(g\) is consequently a translate of this finite kernel. The map \(g\) is proper, so the proper finite-fibre theorem makes it finite. It is surjective because the morphism
\[
       w:A\longrightarrow B\times D,\qquad a\longmapsto(r(a),v(a))
       \tag{NR20}
\]
satisfies \(gw=[t]_A\), whose image is all of \(A\). Thus \(g\) is an isogeny, and CE6 makes it finite flat. The dimension identity \(\dim D=\dim A-\dim B\) follows from the finite integral function-field extension for \(g\) and the dimension of a product. This proves (NR1) over the original field. The construction never takes a reduced identity component of a possibly nonreduced kernel over an imperfect field. \(\square\)

#### 2O.7. Degrees, actual kernels and rational projectors

**NR7.** Write \(a=\dim A\) and \(\delta=\operatorname{rank}_k K\), with \(K\) as in (NR19). Then
\[
        \deg g=\delta,\qquad
        gw=[t]_A,\qquad wg=[t]_{B\times D}.
        \tag{NR21}
\]
The map \(w\) is an isogeny of degree \(t^{2a}/\delta\). For every \(\ell\ne\operatorname{char}k\),
\[
 V_\ell A=V_\ell B\oplus V_\ell D
 \quad\text{via addition, and}\quad
 \#\operatorname{coker}T_\ell g=\ell^{v_\ell(\delta)}.
 \tag{NR22}
\]
These statements respect \(G_k\).

The kernel degree statement is (NR19) with CE6's full scheme length. The first composition identity was proved above. On a pair \((b,d)\), the two components of \(wg\) are \(r(b+d)=tb\) and \(v(b+d)=td\), proving the second on all schemes. The map \(w\) is proper and its fibres lie in those of \(gw=[t]\), so it is finite. Its image has dimension \(a\) by finiteness and the integral dimension calculation; the target \(B\times D\) is integral of that dimension. Thus the image is the entire target. CE6 gives finite flatness, and finite degree multiplication gives its claimed degree.

After tensoring homomorphisms with \(\mathbf Q\), or on \(V_\ell A\), the two maps
\[
              e=\frac{\iota r}{t},\qquad
              1-e=\frac v t
              \tag{NR23}
\]
are complementary idempotents. Indeed \(r\iota=t\) gives \((\iota r)^2=t\iota r\); (NR17) gives the sum and the zero mixed products. Their images are respectively \(V_\ell B\) and \(V_\ell D\), since multiplication by \(t\) is invertible on rational Tate spaces and both maps restrict to that multiplication on their corresponding subvariety. CU10 applied to \(g\) gives the exact integral cokernel order in (NR22). If \(\ell\nmid\delta\), addition already identifies \(T_\ell A=T_\ell B\oplus T_\ell D\). For other primes the rational projectors need not preserve \(T_\ell A\); the actual maps \(te=\iota r\) and \(t(1-e)=v\) do preserve it.

All maps and subvarieties are over \(k\), so these decompositions are \(G_k\)-equivariant. They concern the subspaces supplied by abelian subvarieties. They do not assert that every Galois-stable subspace arises from a subvariety or prove general semisimplicity of a Galois representation. \(\square\)

#### 2O.8. A factor of the dominating curve Jacobian

**NR8.** Let \(\Phi:J_C\to A_E\) be the smooth surjective map constructed in CD7, over its finite separable field \(E/k\). There are abelian subvarieties \(B,D\subset J_C\), defined over \(E\), such that
\[
 B=(\ker\Phi)^0,\qquad
 B\times D\longrightarrow J_C\text{ is an isogeny},\qquad
 q=\Phi|_D:D\longrightarrow A_E\text{ is an isogeny}.
 \tag{NR24}
\]
If \(N\) is the number of geometric components of \(\ker\Phi\), and \(\delta=\operatorname{rank}(B\cap D)\), then
\[
                  \deg q=N\delta.
                  \tag{NR25}
\]

First the indicated identity component is an abelian variety over \(E\), without replacing the whole kernel by it. CD8 gives a proper smooth kernel \(K\). Over an algebraic closure its connected components are smooth integral: their local rings are domains by CD3, and connectedness leaves one component. Their global functions are constants by properness. Thus \(H^0(K,\mathcal O_K)\), a finite-dimensional \(E\)-algebra, becomes \(\overline E^N\) after field extension. Field base change follows from the affine Čech kernel, so this algebra is finite étale: its finite field factors have separable minimal polynomials, as detected by the reduced geometric algebra. Evaluation at the identity picks an \(E\)-factor. The corresponding idempotent cuts out an open-and-closed subscheme \(B\subset K\) whose geometric fibre is the identity component. Addition and inversion preserve that component; their scheme factorizations follow on the reduced geometric products and descend exactly as in NR3. Thus \(B\) is a subgroup. It is proper, smooth and geometrically connected, hence an abelian variety. Its dimension is \(\dim J_C-\dim A\), by the relative smooth dimension of \(\Phi\). The remaining components of \(K\) are retained in \(N\).

Apply NR6 over \(E\) to \(B\subset J_C\). It gives \(D\), \(r:J_C\to B\), and \(v=[t]-\iota r\) with image \(D\). Since \(\Phi\iota=0\), we have \(\Phi v=[t]\Phi\). Surjectivity of \(\Phi\) and of \([t]\) therefore makes \(\Phi(D)=A_E\). Its full kernel is \(D\cap K\). Over an algebraic closure, each component of \(K\) meets \(D\): express any one of its points as \(b+d\) using the surjective addition \(B\times D\to J_C\); then \(\Phi(d)=0\), and \(b\) is in the identity component. Translation by such a \(d\) identifies that component's intersection with \(D\), as a scheme, with \(B\cap D\). Thus \(D\cap K\) is finite of total length \(N\delta\). Proper finite-fibre finiteness makes \(q\) finite, and CE6 makes it finite flat. This proves (NR24)–(NR25), including possible nonreduced intersections.

In particular CD8's rational exact sequence is now split by an actual isogeny factor:
\[
 V_\ell J_C=V_\ell B\oplus V_\ell D,\qquad
 V_\ell\Phi|_{V_\ell D}:V_\ell D\xrightarrow{\ \sim\ }V_\ell A_E.
 \tag{NR26}
\]
The section is the inclusion of \(V_\ell D\) composed with the inverse of this isomorphism, and is \(G_E\)-equivariant. At integral level CU10 gives index \(\ell^{v_\ell(N\delta)}\) for \(T_\ell q\). If \(\ell\nmid N\delta\), it is an isomorphism and the addition decomposition is integral too. In general a finite \(\mathbf Z_\ell\)-module of order \(\ell^m\) is killed by \(\ell^m\): its cyclic subgroups have orders dividing that order. Hence the rational section satisfies
\[
       \ell^{v_\ell(N\delta)}s(T_\ell A_E)
                                \subset T_\ell J_C .
       \tag{NR27}
\]
This does not remove CD8's distinction between rational exactness and an integral surjection at primes dividing the component order.

The dimension-zero cases use point factors and degree one. For positive dimension, (NR24) is the required abelian reducibility step: it supplies an isogeny between \(A_E\) and a factor of a genuinely constructed curve Jacobian. It does not construct a semistable curve model, a formal or analytic period cover, or the later modularity and comparison results of the course. Those constructions still need their own proofs. \(\square\)

#### 2O.9. Graded exercise: coproducts and abelian projectors

**Exercise 2O (100 points; ten parts of 10 points).**

1. Explain why the dual finite resolution in NR1 implies vanishing of \(H^i(X,\mathcal O_X)\) above \(\dim X\). Identify the two quasi-isomorphisms in its truncation argument. State the geometric hypotheses.
2. For independent degree-one primitive elements \(x,y,z\), compute the multidegree \((1,1,1)\) part of the iterated coproduct of \(xyz\). Explain why it is nonzero in characteristics two and three, even though \(3!=0\) there. Generalize to \(r\) independent degree-one classes.
3. Derive the first-order rigidified line classification using \(1+\epsilon c_{ij}\), and explain why NL20's monomorphism gives the reverse inequality in (NR8). Does this prove a full exterior-algebra description of coherent cohomology?
4. For \(R=K[t]\), study \(R[x]/(tx)\) and \(R[x,y]/(ty-x^2)\) after inverting \(t\). Give free bases there. Explain why a generic flat open alone does not prove flatness everywhere, and what the homomorphism translation square adds in NR3.
5. In characteristic \(p\), write \(\mu_{p^h}\) as a local Artinian algebra at its sole geometric point and compute \([p]^*(z-1)\). Prove it is killed by \(p^h\), although the geometric point group has order one. Compare this with the deliberately generous bound (NR13).
6. Let \(q:X\to Y\) be an isogeny with kernel killed by \(n\). Construct its reverse map \(u\) by the full finite faithfully flat relation, prove both identities in (NR14), and compute its degree. Which part would fail if annihilation had only been checked on geometric points?
7. Take \(k=\mathbf Q\), \(L=\mathbf Q(i)\), \(E:y^2=x^3-x\), and \(\alpha(x,y)=(-x,iy)\). For \(A=E\times E\), \(B=E\times0\), consider \(r_L(x,y)=2x+\alpha(y)\). Compute its Galois average and the descended complement obtained from NR6.
8. On \(A=E\times E\) over any field, take \(r(x,y)=2x+y\), \(t=2\). Determine \(v,D,B\cap D\), the addition map \(g\), and \(w\). Compute both degrees and both rational projectors. Discuss the integral Tate decomposition at \(\ell=2\) and at odd \(\ell\ne\operatorname{char}k\).
9. In NR8 suppose \(N=6\), \(\delta=4\). Compute \(\deg q\), the orders of the Tate cokernel for \(\ell=2,3,5\), and the corresponding section denominator bounds. Explain why these data do not give all Smith factors. Give a connected-kernel example where the chosen \(D\) still has a nonintegral section at \(2\).
10. Construct the identity component of CD8's smooth proper kernel over its actual field \(E\). Prove that every component meets \(D\) and that its intersection has length \(\delta\). State exactly which geometric requirement is now supplied for the period construction and which remains.

**Full solution.**

1. Let \(X\hookrightarrow\mathbf P^N\) be smooth projective geometrically integral of dimension \(g\), put \(c=N-g\), and let \(F^\bullet\) be CD1's twist resolution. The dual \(G^\bullet\) has cohomology only in degree \(c\), by the regular-embedding and dual Koszul calculation CD3. The good truncation \(\tau_{\le c}G\) has \(\ker d^c\) in degree \(c\); its inclusion into \(G\) and its map onto \(\mathcal H^c(G)\) placed in degree \(c\) are both quasi-isomorphisms. Coherent affine sections and the finite Čech total comparison preserve them. Hence
   \[
       \mathbb H^j(G)=0\ (j<c),\qquad
       H^i(X,\mathcal O_X)^\vee=\mathbb H^{N-i}(G)=0\ (i>g).
       \tag{NRX1}
   \]
   Smoothness supplies the regular embedding used in the local calculation. Geometric integrality keeps the dimension pure and permits the faithful algebraic-closure comparison used here. This is a consequence of the proved finite-complex projective pairing, not an invocation of a general duality theorem.

2. Distributing the three primitive coproducts and retaining one degree-one element in each factor gives
   \[
   \begin{aligned}
      &x\otimes y\otimes z-x\otimes z\otimes y
       -y\otimes x\otimes z+y\otimes z\otimes x\\
      &\hspace{2em}+z\otimes x\otimes y-z\otimes y\otimes x.
   \end{aligned}
   \tag{NRX2}
   \]
   These six tensors are different basis vectors. In characteristic two all their signs are positive, but their coefficients remain one on six different coordinates. In characteristic three the negative coefficients are two, also nonzero. Adding the coefficients into \(3!\) would incorrectly identify distinct tensor vectors. For \(r\) basis elements the same argument gives \(r!\) different tensor vectors, each with coefficient \(1\) or \(-1\), so the sum is nonzero in every characteristic. Vanishing in degrees \(>g\) then forces \(\dim H^1\le g\).

3. A line with trivial reduction has local frames lifting that reduction. Their transitions \(1+\epsilon c_{ij}\) satisfy the additive cocycle equation because \(\epsilon^2=0\); replacing frames by \(1+\epsilon b_i\) adds a Čech boundary. Tensor product and scalar substitution give the vector-space operations. Proper constants show that changing the trivial reduced frame, or the rigidification at zero, adds no new class. Thus the deformation space is \(H^1(A,\mathcal O_A)\).

   NL20 injects tangent vectors of the smooth \(g\)-dimensional \(Q\) into that space. Together with the coproduct bound this gives dimension exactly \(g\). The proof has not determined all higher cohomology dimensions or proved that squares of degree-one classes vanish in characteristic two. It therefore does not by itself assert a full exterior-algebra identification.

4. In the first algebra, after inverting \(t\) the relation is \(x=0\), so the algebra is \(R_t\), free on \(1\). Before localization, \(x\ne0\) but \(tx=0\); thus it is not flat over \(R\), since the injective multiplication-by-\(t\) map of \(R\) stops being injective after tensor.

   In the second algebra, invert \(t\) and eliminate \(y=t^{-1}x^2\). The result is \(R_t[x]\), with basis
   \[
                          1,x,x^2,x^3,\ldots .
                          \tag{NRX3}
   \]
   Infinite rank is allowed in the generic algebra freeness argument. At \(t=0\) its fibre is \(K[x,y]/(x^2)\); generic freeness does not imply that every fibre is reduced or smooth. For a surjective group homomorphism, translation carries a flat base open to a neighbourhood of every closed point, using lifts of the corresponding target translations. Those opens cover the target, and faithful field extension detects flatness. That group argument is what extends the generic result in NR3.

5. Put \(w=z-1\). Then
   \[
       \mathcal O(\mu_{p^h})=K[w]/(w^{p^h}),\qquad
       [p]^*w=(1+w)^p-1=w^p,\qquad
       [p^h]^*w=w^{p^h}=0.
       \tag{NRX4}
   \]
   Its full rank is \(p^h\), although its only geometric point is the identity. Multiplication by one plainly does not kill its nonzero augmentation ideal. The general bound \((p^h)!\,p^{p^h}\) from (NR13) is a multiple of a valid annihilator; it is not a proposed minimal exponent. Its proof uses the nilpotent augmentation ideal, so does not make the geometric-point error.

6. The relation is \(X\times_YX\simeq X\times\ker q\), with the second point obtained by adding a kernel element. Full scheme annihilation gives equality of the two pullbacks of \([n]_X\). FD5 descends this map uniquely to \(u:Y\to X\) and its group law. Then \(uq=[n]_X\), and composition with the faithfully flat cover \(q\) proves \(qu=[n]_Y\). The proper finite-fibre argument makes \(u\) finite and onto, and CE6 makes it flat. If \(b=\dim X\),
   \[
                      \deg u=n^{2b}/\deg q.
                      \tag{NRX5}
   \]
   Checking only point annihilation would not establish equality on the relation scheme with nilpotents. Part 5 is an explicit obstruction to that shortcut.

7. The indicated coordinate map preserves the elliptic equation, fixes zero, and has inverse \((x,y)\mapsto(-x,-iy)\); CU1 therefore makes it a group automorphism. Its square is inversion, and its Galois conjugate is \(-\alpha\). Consequently
   \[
       r_L+\overline r_L:(x,y)\longmapsto4x,\qquad
       t=4,\qquad v(x,y)=(0,4y).
       \tag{NRX6}
   \]
   The descended \(D\) is the second factor, since \([4]\) is onto. Addition from \(B\times D\) is the product identification and has degree one. The finite Galois sum, rather than the original noninvariant map, is what descends. The scalar \(t\) need not be the degree of the resulting addition isogeny.

8. Here
   \[
        v(x,y)=(-y,2y),\qquad
        D=\{(-z,2z):z\in E\},\qquad B\cap D\simeq E[2].
        \tag{NRX7}
   \]
   The parametrization is a closed immersion, since its first coordinate is an automorphism. The intersection statement holds on all schemes: its second coordinate vanishes exactly when \(2z=0\). Hence \(\delta=4\), including in characteristic two. Using \(z\) as the coordinate on \(D\), the two maps have matrices
   \[
       G=\begin{pmatrix}1&-1\\ 0&2\end{pmatrix},
       \qquad W=\begin{pmatrix}2&1\\ 0&1\end{pmatrix},
       \qquad GW=WG=2I.
       \tag{NRX8}
   \]
   Both maps have degree four: each is a product of an automorphism with identity on one elliptic factor and \([2]\) on the other. Their degree product is \(16=2^{2\dim A}\), as required.

   The projectors in the original coordinates are
   \[
        e=\begin{pmatrix}1&1/2\\ 0&0\end{pmatrix},
        \qquad1-e=\begin{pmatrix}0&-1/2\\ 0&1\end{pmatrix}.
        \tag{NRX9}
   \]
   For odd \(\ell\), these preserve the Tate lattice and the addition map has index one. At \(\ell=2\ne\operatorname{char}k\), the rational projector sends \((0,z)\) with primitive \(z\in T_2E\) to \((z/2,0)\), which is not integral. The addition cokernel is \((\mathbf Z_2/2)^2\), of order four. In characteristic two the full addition kernel still has rank four, while its differential is singular; that prime is excluded from this Tate-module assertion.

9. We have
   \[
   \begin{array}{c|c|c|c}
     \ell&\deg q&\#\operatorname{coker}T_\ell q&
                  \text{section multiple guaranteed integral}\\ \hline
     2&24&8&8s\\
     3&24&3&3s\\
     5&24&1&s
   \end{array}
   \tag{NRX10}
   \]
   The orders determine the sum of the Smith exponents, not their individual list. For instance order eight permits \(\mathbf Z_2/8\), \(\mathbf Z_2/4\oplus\mathbf Z_2/2\), or \((\mathbf Z_2/2)^3\), subject to the actual rank bound.

   Take the smooth surjection \(\Phi:E^2\to E\), \((x,y)\mapsto y\). Its kernel \(B=E\times0\) is connected, so \(N=1\). Choose part 8's \(D\). Then \(\Phi|_D=[2]\), of degree four, and its rational section is nonintegral at two. In contrast \(T_2\Phi\) itself is onto. Thus a chosen complement's section denominator and the component obstruction to integral surjectivity are different quantities.

10. For the proper smooth kernel \(K\), geometric components are proper connected smooth integral schemes. Their functions are constants, so
   \[
             H^0(K,\mathcal O_K)\otimes_E\overline E
                       \simeq\overline E^N.
                       \tag{NRX11}
   \]
   Proper coherent finiteness and the affine Čech base change make the algebra on the left finite étale over \(E\). Evaluation at the identity chooses an \(E\)-factor and its idempotent, defining \(B\). Group operations preserve that geometric component and descend as scheme maps, so \(B\) is an abelian subvariety over \(E\).

   The surjective addition \(B\times D\to J_C\) expresses any point of a component of \(K\) as \(b+d\). Then \(d\in D\cap K\) lies in the same component. Translating by it identifies that entire scheme intersection with \(D\cap B\), including nilpotents. Summing the equal lengths gives \(N\delta\), and the proper finite-fibre argument makes \(\Phi|_D\) the stated isogeny. The curve domination and its abelian isogeny factor are now constructed. A semistable curve model, the associated integral semiabelian extension, and an actual formal or analytic period cover remain separate substantive tasks; reducibility does not supply them by itself.

### 2P. Nodal curves and their generalized Jacobians

We construct the degree-zero line-bundle group of a split nodal curve. Its torus is governed by cycles in the dual graph, and its abelian quotient is the product of the smooth component Jacobians. The construction represents families on arbitrary parameter schemes, including schemes with nilpotents.

The input is a finite collection of smooth projective geometrically integral curves \(C_v/K\), indexed by a nonempty finite set \(V\). A finite edge set \(E\) specifies disjoint pairs of distinct rational points \(P_e^-,P_e^+\) on the disjoint union of these curves. Write \(s(e),t(e)\) for their components. A loop is allowed; all the marked branch points are distinct. Assume the resulting graph \(\Gamma\) is connected, and choose an additional unmarked rational point \(P_v\) on each component. We will construct their pinched curve \(C\), with root point \(P=P_{v_0}\), and an exact sequence of algebraic groups
\[
 0\longrightarrow T_\Gamma\longrightarrow J_C^0
       \longrightarrow\prod_{v\in V}J_{C_v}\longrightarrow0,
 \qquad X^*(T_\Gamma)=H_1(\Gamma,\mathbf Z).
 \tag{NC1}
\]
The notation \(J_C^0\) here means the group of multidegree-zero line bundles, rigidified at \(P\); its representability and its identification as an identity component are proved below.

Free comparisons are the Stacks project's [point gluing and Picard calculation](https://stacks.math.columbia.edu/tag/0C1H) and [torsion under normalization](https://stacks.math.columbia.edu/tag/0C1Y). The affine gluing, projectivity, full-family patching and representing group used here are proved explicitly. This is geometry of a nodal fibre. Existence of a semistable model and construction of its formal or analytic period cover remain separate tasks.

#### 2P.1. The finite pinching algebra

**NC1.** Identifying each prescribed pair produces a reduced finite-type curve \(C\), with finite normalization
\[
             \nu:\widetilde C=\coprod_v C_v\longrightarrow C.
             \tag{NC2}
\]
It is an isomorphism away from the prescribed pairs. Its nodes are distinct \(K\)-points indexed by \(E\), and its affine algebra there is a fibre product.

Choose affine opens on the components containing all branch points and all the \(P_v\). Such opens exist by QS1's finite-point homogeneous avoidance: the complement of a projective hypersurface avoiding the finite prescribed set is affine. The finite disjoint union is affine, say \(\operatorname{Spec}B\). Evaluation at the \(2|E|\) distinct rational points is surjective by the Chinese remainder equations. Let \(I\subset B\) be their common vanishing ideal, so \(B/I=K^{2E}\), and put
\[
 A=\{b\in B:b(P_e^-)=b(P_e^+)\text{ for every }e\}
       =B\times_{K^{2E}}K^E.
 \tag{NC3}
\]
The last map sends each coordinate diagonally into its two branch coordinates. Thus \(I\subset A\), \(A/I=K^E\), and \(B/A\) has dimension \(|E|\) over \(K\). A basis of that quotient, lifted to \(B\), together with \(1\), generates \(B\) as an \(A\)-module. Therefore \(B\) is finite over \(A\).

We also verify finite type of \(A\). Choose a finite \(A\)-module generating list \(x_i\) for \(B\), containing \(1\), and a finite \(K\)-algebra generating list \(b_j\) for \(B\). Express every \(b_j\) and every \(x_ix_h\) in the \(x_i\), with coefficients in \(A\). Let \(D\) be the \(K\)-algebra generated by this finite coefficient list. The \(D\)-span of the \(x_i\) is a subalgebra containing all \(b_j\), hence is \(B\). Thus \(B\) is finite over the noetherian \(D\). Its \(D\)-submodule \(A\) is finite, so \(A\) is a finite-type \(K\)-algebra. It is reduced because it embeds in the reduced \(B\).

For \(c\in I\), we have \(A_c=B_c\): for every \(b\in B\), the product \(cb\) is in \(I\subset A\). Such principal opens cover the complement of the marked points. Hence \(\operatorname{Spec}A\) glues to \(\widetilde C\) away from them along these identical opens. This constructs \(C\) and the finite map (NC2); finiteness is checked on the displayed affine and on the unchanged opens. Its fibre at each new point is exactly its two branch points, since the corresponding quotient of \(B\) is \(K^2\).

The source is normal: its smooth curve local rings are discrete valuation rings by SF5–SF6. It is finite and birational on each component. If an element of the total fraction ring is integral over \(A\), its monic equation is also an equation over \(B\); normality puts it in \(B\). Thus \(B\) is the integral closure of \(A\), proving the normalization assertion.

For any \(K\)-algebra \(R\), tensor the exact sequence of \(K\)-vector spaces
\[
 0\longrightarrow A\longrightarrow B\oplus K^E
          \longrightarrow K^{2E}\longrightarrow0.
 \tag{NC4}
\]
The last arrow is the difference of evaluation and the diagonal map, and is onto. Tensor is exact over the field. Consequently
\[
          A_R=B_R\times_{R^{2E}}R^E.
          \tag{NC5}
\]
This is the full base-changed gluing algebra, also for nonreduced or nonnoetherian \(R\). No claim that a base-changed nonreduced scheme is normal is involved. \(\square\)

#### 2P.2. Nodes, properness and explicit projectivity

**NC2.** The curve \(C\) is projective, geometrically reduced and geometrically connected. At each new point its completed local ring is
\[
 \widehat{\mathcal O}_{C,e}
       \simeq K[[u]]\times_KK[[v]]
       \simeq K[[x,y]]/(xy).
       \tag{NC6}
\]
All other points are smooth.

To compute the completion, localize (NC3) at a single new point. The branch algebra is finite and semilocal, with the two rational branch maximal ideals. Its conductor \(I\) is their intersection, and it is the maximal ideal of the pinched local ring. Products \(I^r\), computed in the branch algebra or the pinched ring, coincide: multiplication by a branch coefficient can be absorbed into one of the factors, because \(I\) is already an ideal of the branch algebra. The Chinese remainder equations identify the branch quotients by \(I^r\) with the two branch local quotients. Smooth curve coordinates give their inverse limits \(K[[u]],K[[v]]\). Condition (NC3) retains equality of the two constant terms at every level. Passing to the inverse limit proves the first isomorphism in (NC6). The second sends \(x\) to \((u,0)\) and \(y\) to \((0,v)\); every equal-constant pair is uniquely a constant plus a series in \(u\) with zero constant and a series in \(v\) with zero constant. This proves the ring isomorphism, in every characteristic.

We give the separation argument before using properness. The inverse image of the diagonal of \(C\) under the finite surjective \(\nu\times\nu\) is, as a closed set, the diagonal of \(\widetilde C\) together with the finitely many ordered branch pairs. A finite surjective map is a closed quotient map, by the integral lying-over calculation. Hence the diagonal of \(C\) has closed underlying set. It is an immersion: the open union of \(U\times U\), for affine opens \(U\subset C\), contains the diagonal, and its restriction on each such open is the affine quotient-ring closed immersion. Since its image is closed in the whole product, those local ideals glue with the unit ideal off its image to give a closed immersion. Thus \(C\) is separated.

For any base change, a closed subset of \(C\) and its inverse image under the finite surjective \(\nu\) have the same image in the base. The latter image is closed because \(\widetilde C\) is proper. Therefore \(C\) is universally closed; it is separated and of finite type, hence proper. Construction (NC5) commutes with field extension and embeds each affine gluing algebra in the reduced branch algebra. This proves geometric reducedness. Each component remains connected, and the connected graph identifies them into one connected space, after any field extension. Thus \(C\) is geometrically connected.

We construct a finite map to \(\mathbf P^1\) to prove projectivity. If there are no edges, connectedness leaves one component and \(C=C_v\) is already projective. Otherwise every component has a branch mark. On \(C_v\), choose a positive very ample line power and a section \(b_v\) nonzero at all its branch marks. Prescribing nonzero values at those finitely many points is possible by PF8 applied to their ideal. Its zero divisor is finite and nonempty: its line has positive degree by DC4. After replacing \(b_v\) by a positive power, PF8 permits a section \(a_v\) of the same line which vanishes at every branch mark and is nonzero at every point in the support of that zero divisor. These conditions concern disjoint finite subschemes, so their evaluation map is onto; over a nonrational closed point choose a nonzero value in its residue line. Thus \(a_v,b_v\) have no common zero.

They define a nonconstant map \(C_v\to\mathbf P^1\), with value zero at every branch mark and a pole at each zero of \(b_v\). Near the marks, the functions \(a_v/b_v\) satisfy (NC3), so these maps glue to a map \(C\to\mathbf P^1\). Each geometric fibre is finite, as its inverse image on every smooth component is finite. The map is proper by its closed graph and proper source. The proper finite-fibre theorem of Lesson 3 makes it finite. The explicit finite-cover embedding of Lesson 3, Theorem 0.F.7 and Corollary 0.F.8, now makes \(C\) projective. This uses an actual finite map, rather than assuming projectivity of the pinching. \(\square\)

#### 2P.3. Invertible modules patch on every parameter scheme

**NC3.** For every \(K\)-scheme \(S\), a line on \(C_S\) is equivalent to lines \(M_v\) on \((C_v)_S\), together with isomorphisms
\[
     \lambda_e:M_{s(e)}|_{P_e^-\times S}
                       \xrightarrow{\ \sim\ }
                    M_{t(e)}|_{P_e^+\times S}
              \qquad(e\in E).
     \tag{NC7}
\]
Morphisms are the component line isomorphisms commuting with these edge maps. The equivalence is compatible with every base change on \(S\).

It suffices to prove the affine statement for (NC5). An equivalent description keeps a line \(N_e\) on each node section and identifies both branch restrictions with \(N_e\). Choosing the first branch as \(N_e\) removes it and gives exactly (NC7). With the node lines retained, form
\[
 M=\ker\left(M_B\oplus M_{R^E}
                   \longrightarrow M_{R^{2E}}\right),
                   \tag{NC8}
\]
using the difference of the two specified identifications. We show this is invertible over \(A_R\) and recovers the given modules.

Off the conductor, \(A_R=B_R\), so this is immediate. At a prime over a node, localize \(A_R\). The finite branch algebra is semilocal; its quotient along the two branches is the product of two copies of the corresponding local ring of \(R\). Its conductor is contained in every maximal ideal of that semilocal algebra, since every such maximal ideal lies over the node prime.

A rank-one projective module over a semilocal ring is free. To see this, choose a nonzero generator in each of its finitely many residue lines, lift them simultaneously by the Chinese remainder equations, and apply finite Nakayama. The resulting surjection from the ring splits by projectivity; its kernel has zero reduction at every maximal ideal and is zero by Nakayama locally. Thus choose frames for the branch and node modules. Their mismatch is a unit in the product branch quotient. Lift that unit to the branch algebra; it is a unit there, because its quotient kernel lies in the Jacobson radical. Changing the branch frame by this unit makes the two identifications agree with the node frame. In these frames (NC8) is precisely \(A_R\), and its pullbacks are the prescribed free modules.

These local descriptions show that (NC8) is a line and recovers the given data. They require no noetherian hypothesis on \(R\). Conversely, tensoring (NC4) with an invertible \(A_R\)-module preserves exactness, so every line is recovered by this kernel. Compatible maps patch by the same equalizer. The local free-frame description also proves base-change compatibility, even when tensoring a general kernel would not be exact. Gluing these affine constructions proves the assertion over arbitrary \(S\), including nilpotent parameters. \(\square\)

#### 2P.4. Cycle coordinates and constants on the curve

**NC4.** Put
\[
 \partial:\mathbf Z^E\longrightarrow\mathbf Z^V,\qquad
       e\longmapsto t(e)-s(e),\qquad
 X=H_1(\Gamma,\mathbf Z)=\ker\partial.
 \tag{NC9}
\]
Then \(X\) is free of rank \(r=|E|-|V|+1\). The group of branch gluing scalars modulo component frame changes, with one root frame fixed, is the split torus
\[
             T_\Gamma=\operatorname{Hom}(X,\mathbf G_m).
             \tag{NC10}
\]
Moreover \(\pi_*\mathcal O_{C_S}=\mathcal O_S\) for every \(K\)-scheme \(S\).

Choose a spanning tree \(\mathcal T\) of the connected graph, with root \(v_0\), and orient its edges away from the root. A spanning tree exists by successively adjoining an edge reaching a new vertex; absence of cycles gives exactly \(|V|-1\) edges. Every non-tree edge closes a unique path in the tree, and gives a cycle with its own non-tree coefficient one and all other non-tree coefficients zero. These cycles form a basis of \(X\). Indeed subtract their multiples from any cycle to leave one supported on the tree; at a terminal vertex its incident coefficient must be zero, and induction removes the tree. This also proves the rank, without division or a field hypothesis.

For an affine parameter \(\operatorname{Spec}R\), component frame changes \(c_v\in R^\times\) change gluing scalars by
\[
                 \lambda_e\longmapsto c_{s(e)}c_{t(e)}^{-1}\lambda_e.
                 \tag{NC11}
\]
Fix \(c_{v_0}=1\). Successively along the tree there is a unique choice making every tree scalar one: set \(c_{t(e)}=c_{s(e)}\lambda_e\) on each tree edge. The remaining \(r\) edge scalars are arbitrary units, giving \(\mathbf G_m^r\) on every ring \(R\). The intrinsic character for a cycle \(z=(z_e)\in X\) is
\[
                       \chi_z(\lambda)=\prod_e\lambda_e^{z_e}.
                       \tag{NC12}
\]
It is unchanged by (NC11), since the exponent at each vertex is the negative of its boundary coefficient. On the fundamental cycle basis these are exactly the remaining coordinates. Thus (NC10) is independent of the chosen tree, and \(X^*(T_\Gamma)=X\).

Finally FC20 on each smooth component gives \(H^0((C_v)_R,\mathcal O)=R\). By (NC3), global functions on \(C_R\) are precisely tuples in \(R^V\) agreeing across every edge. A tree forces all entries equal. Hence \(H^0(C_R,\mathcal O)=R\), for every \(R\), not just residue fields. This local calculation on \(S\) proves the sheaf assertion. In particular an automorphism of a line on \(C_S\) is a base unit, and a rigidification at \(P\) makes it the identity. \(\square\)

#### 2P.5. The universal multidegree-zero group

**NC5.** The functor of lines on \(C_S\) of degree zero on every geometric component, rigidified at \(P\), is represented by a smooth geometrically connected commutative algebraic group \(G=J_C^0\). It has the fppf exact sequence (NC1), and
\[
                         \dim G=\sum_v g_v+r,
                         \tag{NC13}
\]
where \(g_v\) is the genus of \(C_v\).

Put \(J=\prod_v J_{C_v}\), using the full pointed curve representations JC1–JC9, and let \(\mathcal L_v\) denote the universal component line and its pullback to \(C_v\times J\), rigidified at \(P_v\). On \(J\) define the fibre lines
\[
 F_e=\mathcal L_{t(e)}|_{P_e^+\times J}
             \otimes\bigl(\mathcal L_{s(e)}|_{P_e^-\times J}\bigr)^{-1}.
 \tag{NC14}
\]
Use the rooted tree of NC4 and define base lines \(N_v\) recursively by
\[
           N_{v_0}=\mathcal O_J,\qquad
           N_{t(e)}=N_{s(e)}\otimes F_e^{-1}\quad(e\in\mathcal T).
           \tag{NC15}
\]
Set \(\mathcal L_v'=\mathcal L_v\otimes p_J^*N_v\). Their fibre lines at the two ends of each tree edge have a canonical isomorphism: their ratio \(F_eN_{t(e)}N_{s(e)}^{-1}\) is canonically trivial by (NC15). For each remaining edge set
\[
           E_e=F_e\otimes N_{t(e)}\otimes N_{s(e)}^{-1},
           \qquad
           G=\prod_{e\notin\mathcal T,\ J} E_e^\times .
           \tag{NC16}
\]
Here \(E_e^\times\) is the scheme of nowhere-zero frames of the line \(E_e\), an open in its total vector bundle. Its universal frame supplies the gluing isomorphism on that edge. Tree edges use their canonical isomorphisms. NC3 therefore gives a universal line on \(C\times G\), rigidified at the root.

We prove the representation on arbitrary \(S\), including component base lines which need not be trivial. Given a line \(M\) and its root rigidification, write \(M_v=M|_{(C_v)_S}\), and put \(Q_v=M_v|_{P_v\times S}\). Normalizing \(M_v\) by \(Q_v^{-1}\) gives, by JC's full representation, a unique map \(a_v:S\to J_{C_v}\) and a normalized isomorphism
\[
                         M_v\simeq a_v^*\mathcal L_v\otimes Q_v.
                         \tag{NC17}
\]
Take the product map \(a:S\to J\). The root rigidification gives \(Q_{v_0}=\mathcal O_S\). The edge isomorphisms along the tree then identify, recursively and uniquely, \(Q_v\simeq a^*N_v\): an isomorphism from source fibre to target fibre says \(Q_{t(e)}\simeq Q_{s(e)}\otimes a^*F_e^{-1}\). After these identifications, the non-tree edge maps are exactly nowhere-zero sections of the \(a^*E_e\). They give a unique map \(S\to G\).

Conversely, such a map pulls back the universal glued line. The two procedures are inverse by their explicit component lines and edge maps in NC3. Their isomorphisms are unique by NC4's root normalization, so they are natural in \(S\). This proves the full functor statement, not merely a description of geometric line classes.

Tensor product, inverse and the trivial line now define morphisms giving \(G\) its commutative group structure; all identities hold on every parameter scheme by the corresponding line identities. Restriction to the components is its homomorphism \(G\to J\). Over zero the universal component lines and all their marked fibres are canonically trivial, so (NC16) identifies its full kernel with NC4's torus. The map \(G\to J\) is a Zariski locally trivial product of line-frame bundles, hence smooth and surjective. It is a torsor under this kernel, with relation isomorphism supplied by subtracting two points in a fibre. This proves the fppf exact sequence.

The total space in (NC16) is smooth over the smooth \(J\), has relative dimension \(r\), and is geometrically integral: over a nonempty trivializing open it is the product of an integral open with \(\mathbf G_m^r\), and the same holds locally over every point. Thus it is geometrically connected and has (NC13). It is quasi-projective: each line-frame bundle is an open in the projective bundle of \(\mathcal O_J\oplus E_e\), and their finite product over the projective \(J\) is projective. Removing the zero and infinity sections gives (NC16).

One can also identify the identity component without presupposing a Picard scheme. The smooth points \(P_v\) are Cartier divisors on \(C\), and \(\mathcal O_C(\sum_v d_vP_v)\) has component degree vector \(d\in\mathbf Z^V\). Give each such line a root rigidification. Tensoring with it represents the degree-\(d\) functor by a copy of \(G\). Degrees in a line family are locally constant, by CE3's Euler calculation on the smooth components and DC5. For an arbitrary affine base, this assertion reduces to a noetherian one: local line frames, their finite presentation matrices and their transition inverses involve finitely many coefficients in that base ring, so descend to a finite-type \(K\)-subalgebra; all the required inverse identities descend with those coefficients. The disjoint union of these copies, indexed by \(\mathbf Z^V\), therefore represents the whole rigidified line functor. Its zero-degree copy is its geometrically connected identity component. No general Picard representability theorem is assumed here. \(\square\)

#### 2P.6. Normalization cohomology and infinitesimal gluing

**NC6.** If \(g=1-\chi(C,\mathcal O_C)\) is the arithmetic genus, then
\[
                    g=\sum_v g_v+r.
                    \tag{NC18}
\]
There is a natural exact sequence
\[
 0\longrightarrow H^1(\Gamma,K)\longrightarrow H^1(C,\mathcal O_C)
       \longrightarrow\bigoplus_v H^1(C_v,\mathcal O_{C_v})
       \longrightarrow0.
 \tag{NC19}
\]
It is the tangent sequence of (NC1), including its signs.

The affine difference map in (NC3) gives the sheaf exact sequence
\[
 0\longrightarrow\mathcal O_C\longrightarrow\nu_*\mathcal O_{\widetilde C}
       \xrightarrow{\ \text{value at }P_e^+-\text{value at }P_e^-\ }
                   \bigoplus_e K_e\longrightarrow0.
 \tag{NC20}
\]
The last map is onto locally at each node by the Chinese remainder equations. A finite morphism is affine, and coherent affine cohomology is zero in positive degree. Computing on an affine cover of \(C\), whose finite inverse images are affine, therefore identifies cohomology of the middle sheaf with that of \(\widetilde C\). Each skyscraper \(K_e\) has no positive cohomology. The resulting long exact sequence begins
\[
 0\to K\to K^V\xrightarrow{\ d\ }K^E
       \to H^1(C,\mathcal O_C)\to\bigoplus_vH^1(C_v,\mathcal O_{C_v})\to0,
 \qquad (da)_e=a_{t(e)}-a_{s(e)}.
 \tag{NC21}
\]
The same sequence and NR1's smooth-curve dimension bound give \(H^i(C,\mathcal O_C)=0\) for \(i>1\).

A tree solves the vertex difference equations without dividing by an integer. Thus the kernel of \(d\) is the diagonal \(K\), and its cokernel is \(H^1(\Gamma,K)=\operatorname{Hom}(X,K)\), of dimension \(r\). This proves (NC19), and its dimension gives (NC18), using \(H^0(C,\mathcal O_C)=K\).

For the tangent identification, a first-order line with trivial reduction has transitions \(1+\epsilon c_{ij}\), exactly as in NR2; that affine proof did not require smoothness. NC4's constant-function calculation supplies uniqueness after root normalization. Hence \(T_0G=H^1(C,\mathcal O_C)\). Restriction to the normalization sends these cocycles to their component restrictions. On the kernel, gluing scalars \(1+\epsilon a_e\) change under component frames \(1+\epsilon b_v\) by adding \(b_{s(e)}-b_{t(e)}\). Their quotient is exactly the cokernel of \(d\); the sign is reversed on the map from vertex frames, without changing its image. The cycle character (NC12) differentiates to \(z\mapsto\sum_e z_ea_e\), identifying \(T_0T_\Gamma=\operatorname{Hom}(X,K)\). Thus the differentiated sequence is precisely (NC19). This retains the infinitesimal gluing directions at every node. \(\square\)

#### 2P.7. Full multiplication kernels, Tate modules and actions

**NC7.** Write \(b=\sum_v g_v\). For every positive integer \(n\), multiplication by \(n\) on \(G\) is finite faithfully flat of rank \(n^{2b+r}\), and
\[
 0\longrightarrow T_\Gamma[n]\longrightarrow G[n]
       \longrightarrow J[n]\longrightarrow0
       \quad\text{is fppf exact},\qquad
 \operatorname{rank}G[n]=n^{2b+r}.
 \tag{NC22}
\]
For \(n=\ell^m\) with \(\ell\ne\operatorname{char}K\), multiplication is étale and gives
\[
 0\longrightarrow\operatorname{Hom}(X,\mathbf Z_\ell(1))
       \longrightarrow T_\ell G\longrightarrow
                       \bigoplus_vT_\ell J_{C_v}\longrightarrow0.
 \tag{NC23}
\]
In particular \(T_\ell G\) is free of rank \(2b+r=2g-r\).

The torus multiplication is finite free of rank \(n^r\): in one coordinate its algebra has basis \(1,t,\ldots,t^{n-1}\) over \(K[t^n,t^{-n}]\), and take tensor products. It is surjective as an fppf map. Over a parameter ring, adjoining an \(n\)-th root of a unit gives a monic finite free rank-\(n\) algebra in which that root is a unit. This applies also when the characteristic divides \(n\).

For a section of \(J[n]\), lift it locally to \(G\) using its line-frame torsor. The multiple of the lift lies in the torus. Divide that torus element by \(n\) after the finite free root cover, and subtract it from the lift. This produces a section of \(G[n]\), on actual parameter schemes. Its kernel is \(T_\Gamma[n]\). The relation of two lifts is torus-kernel translation, so \(G[n]\to J[n]\) is a torsor under \(T_\Gamma[n]\). CU8 gives rank \(n^{2b}\) for \(J[n]\). Faithfully flat descent FD4 therefore makes \(G[n]\) finite locally free of rank \(n^{2b+r}\).

The same division argument, starting with any section of \(G\), first divides its image in \(J\) and then corrects its torus difference. Thus \([n]:G\to G\) is fppf surjective. Its full relation scheme is \(G\times G[n]\), with the usual difference and addition maps. It is a torsor under that finite locally free kernel, so finite faithful flatness and its stated rank descend. When \(n\) is prime to the characteristic, its tangent correction is multiplication by the unit \(n\) on the smooth group. The standard smooth lifting calculation SF1–SF3 makes this map étale. These arguments concern the full schemes \(G[n]\), not their point counts.

At prime-to-characteristic levels, the algebraically closed points of (NC22) are exact and finite; multiplication transitions are onto. Compatible torus torsion is \(\operatorname{Hom}(X,\mathbf Z_\ell(1))\), by its cycle characters and the root-of-unity tower. A compatible sequence in \(J[\ell^m]\) lifts compatibly in \(G[\ell^m]\): any finite initial segment lifts by choosing its last lift and multiplying down, and the nested nonempty finite compatibility sets have a point by the finite inverse-limit compactness of Lesson 1. This proves (NC23). Both end modules are free, of ranks \(r\) and \(2b\), by CU9 and the torus calculation. Lifting a basis of the right free module gives a \(\mathbf Z_\ell\)-linear section, so the middle module is free of their sum rank. No Galois-equivariant section is asserted.

The construction is natural in curve isomorphisms. If \(a:C\to C\) moves the root, pull back a line and normalize it by the inverse of its fibre at \(P\). NC4's uniqueness makes this a well-defined morphism on the representing group, with the full pullback composition identities. For a cycle \(z\) and a torus gluing class \(t\), direct edge substitution in (NC12) gives
\[
                   \chi_z(a^*t)=\chi_{a_*z}(t).
                   \tag{NC24}
\]
Reversing a branch orientation sends the corresponding edge coordinate to its inverse and its cycle coefficient to its negative; the formula includes this sign. A left action of curve automorphisms consequently acts on the group by inverse pullback. The component Jacobian maps and the exact sequences commute with these actual maps.

The same argument gives full semilinear action identities over a finite Galois splitting field when such curve descent data are supplied: pullback of families, base normalization and the representing property construct the semilinear group maps and their cocycle, independently of the chosen tree or component base points. In cycle coordinates their compatibility reads
\[
            \chi_{\sigma z}(\sigma t)=\sigma\bigl(\chi_z(t)\bigr),
 \qquad
            (\sigma f)(z)=\sigma\bigl(f(\sigma^{-1}z)\bigr)
            \quad\bigl(f\in\operatorname{Hom}(X,\mathbf Z_\ell(1))\bigr).
            \tag{NC25}
\]
Thus the graph part carries the signed edge-permutation action together with the cyclotomic action. The Tate exact sequence respects it. This supplies actions for the given curve data, without asserting that an unconstructed model or period map already has such data. \(\square\)

#### 2P.8. A nontrivial extension and the remaining period directions

**NC8.** The torus rank of \(G\) is \(r\). It is proper exactly when \(r=0\), in which case restriction gives \(G\simeq\prod_vJ_{C_v}\). For \(r>0\) the extension need not split, even for one component and one node.

When \(r=0\), every edge is in the tree and (NC16) has no frame factors, so its restriction map is an isomorphism to \(J\). If \(r>0\), the closed subgroup \(T_\Gamma\) contains a closed copy of \(\mathbf G_m\). That group is not proper: its map into \(\mathbf P^1\) has nonclosed image, whereas any map from a proper scheme into the separated \(\mathbf P^1\) is proper by its graph. Hence \(G\) is not proper.

There is no larger geometric torus in \(G\). A homomorphism \(\mathbf G_m\to J\) extends across zero and infinity to \(\mathbf P^1\to J\), by properness and the curve DVR-extension proof of Lesson 3. AL2 says that such a map is constant. A homomorphism from a split torus is generated by its coordinate one-parameter subgroups, so is zero. Every torus over an algebraic closure splits. Consequently any torus subgroup of \(G\) lies in the kernel of \(G\to J\), which is \(T_\Gamma\). This proves the maximal torus rank assertion.

For a concrete nonsplit case, take an elliptic curve \(E\), root zero, and distinct nonzero rational points \(a,b\), and pinch \(a\) to \(b\). Then \(J=J_E\simeq E\) by the proved genus-one Abel isomorphism, the graph has one loop, and
\[
                     G=F^\times\longrightarrow E,
       \qquad F=\mathcal L|_{b\times E}\otimes
                            (\mathcal L|_{a\times E})^{-1}.
                     \tag{NC26}
\]
Its line is \(F\simeq\mathcal O_E([b]-[a])\). To check this, the universal pointed line on \(E\times E\) is, up to the constant factor fixed by its rigidification,
\[
 \mathcal O_{E\times E}(\Delta)
        \otimes p_1^*\mathcal O_E(-[0])
        \otimes p_2^*\mathcal O_E(-[0]).
 \tag{NC27}
\]
On the fibre with parameter \(z\), it is \(\mathcal O_E([z]-[0])\); this and the root normalization identify it with the universal line by the full curve Picard property. Evaluating at \(a\) and \(b\), both different from zero, cancels the parameter \(-[0]\) factors and gives the claimed \(F\). The genus-one Abel isomorphism makes this line nontrivial for \(a\ne b\). A section of \(F^\times\to E\) would trivialize \(F\); therefore the torus torsor has no section, and the extension is not a product extension.

For this one-node elliptic example, \(g=2\), \(r=1\), and \(T_\ell G\) has rank three. A smooth curve Jacobian of genus \(g\) has Tate rank \(2g\) by CU9. In general the nodal-fibre group constructed here has rank \(2g-r\); the additional \(r\) directions required by a smooth generic Jacobian are not produced by merely naming \(G\) its special group. One must still construct a semistable curve model, the associated integral or formal semiabelian extension, and an actual period covering with its lattice and compatible actions. No identification of a graph form with a geometric monodromy pairing is claimed without that construction. \(\square\)

#### 2P.9. Graded exercise: nodes, cycles and torus directions

**Exercise 2P (100 points; ten parts of 10 points).**

1. Pinch \(0\) to \(1\) on the affine line. Put \(q=t(t-1)\), \(z=tq\). Prove that its pinching algebra is \(K[q,z]\), give its single relation, and prove the presentation in every characteristic. Identify the completed node and the generalized Jacobian after adding the point at infinity.
2. On the resulting rational nodal projective curve, glue the trivial line on its normalization by \(\lambda=1+\epsilon\), over \(R=K[\epsilon]/(\epsilon^2)\). Show that the closed fibre is trivial but the line family is not. Explain why local freeness at the node does not make that global line trivial.
3. Let \(\Gamma\) have two vertices and three edges, all oriented from the first vertex to the second. Choose the third edge as a tree. Compute the incidence matrix, an integral cycle basis, and the two torus coordinates. Prove the vertex gauge leaves them unchanged over any ring.
4. Join an elliptic component \(E\) to a rational component by a single edge from \(a\ne0\) on \(E\) to a point of \(\mathbf P^1\). Root the curve at \(0\in E\). Describe \(F_e,N_{\mathbf P^1}\) over \(J=E\). Why can the universal glued line exist although \(F_e\) has no global frame?
5. Take a triangle of three rational components. Compute its arithmetic genus and coherent tangent sequence. Determine the action of a cyclic rotation and of a reflection on its torus. In characteristic two, show on \(K[\epsilon]/(\epsilon^3)\) that the reflection can be nontrivial even though its tangent action is the identity.
6. For the graph in part 3, suppose the component genera are one and two. Compute the dimension of \(G\), arithmetic genus, full rank of \(G[n]\), and prime-to-characteristic Tate rank. Compare it with the Tate rank of a smooth genus-\(g\) Jacobian. Discuss the torus part of \(G[p]\) in characteristic \(p\).
7. On \(E:y^2=x^3-x\) over \(\mathbf Q\), pinch \(a=(0,0)\) to \(b=(1,0)\), with root infinity. Determine the line \(F\) whose frame bundle represents \(G\to E\), prove it is nontrivial, and deduce that this is a nonsplit torus extension. Compute its dimensions and Tate rank.
8. Prove (NC22) on arbitrary parameter schemes by dividing first on \(J\) and then on the torus. Explain how the proof retains nilpotent torsion. Prove the compatible lifting step in (NC23).
9. For the three-edge graph, compute the cycle-lattice actions of exchanging edges one and two, and of reversing all edges while exchanging the two vertices. Give the corresponding action on \(\operatorname{Hom}(X,\mathbf Z_\ell(1))\). Explain the inverse-pullback convention for a left automorphism action.
10. Give the three edges positive integer weights \(m_1,m_2,m_3\). Compute the Gram matrix of \(\sum_e m_ez_ew_e\) on part 3's cycle basis and prove positivity. For weights \(1,2,3\), compute its determinant, Smith factors and rational inverse. State when an edge permutation preserves it and whether it has already been identified with geometric monodromy.

**Full solution.**

1. The equality of values at zero and one is equivalent to
   \[
       A=K+qK[t],\qquad q=t^2-t,\qquad z=tq.
       \tag{NCX1}
   \]
   The algebra \(K[t]\) is free on \(1,t\) over \(K[q]\): the presentation \(K[q,t]/(t^2-t-q)\) is \(K[t]\) by eliminating \(q\), while monic division in \(t\) gives that free basis. Therefore \(qf(t)\) is a polynomial in \(q\) plus \(z\) times a polynomial in \(q\), proving \(A=K[q,z]\). Moreover
   \[
                    z^2=qz+q^3,\qquad
       A\simeq K[Q,Z]/(Z^2-QZ-Q^3).
       \tag{NCX2}
   \]
   Surjectivity was just proved. For injectivity, monic division in \(Z\) leaves \(a(Q)+b(Q)Z\); its image \(a(q)+qb(q)t\) is zero only when both coefficients in the free \(K[q]\)-basis vanish. The argument includes characteristic two.

   The two preimages of the node are \(t=0,1\), and its completed ring is \(K[[u]]\times_KK[[v]]\simeq K[[x,y]]/(xy)\), by NC2. Pinching these points on \(\mathbf P^1\) has one vertex, one loop, component genus zero and \(r=1\). Thus \(J_C^0=\mathbf G_m\). This conclusion is about the projective pinched curve, rather than the Picard group of the affine open alone.

2. The unit \(1+\epsilon\) supplies a valid full edge isomorphism by NC3. Its reduction is one, so its closed-fibre line is trivial. There is one component and the edge is a loop. Any global automorphism of its trivial component line is a single base unit, which changes \(\lambda\) by \(c/c=1\). Hence \(\lambda\ne1\) cannot be transformed into the trivial gluing.

   Locally at the node the line is free: the two branch frames can be adjusted independently in the finite semilocal branch algebra, as in (NC8). They cannot in general be adjusted independently by a global function on the projective normalization, whose functions are only base constants. This is precisely the distinction between a locally free line and a globally trivial one. The example is also the nonzero tangent direction of \(\mathbf G_m\).

3. With columns \(e_1,e_2,e_3\), we have
   \[
    \partial=\begin{pmatrix}-1&-1&-1\\ 1&1&1\end{pmatrix},
    \quad z_1=e_1-e_3,\quad z_2=e_2-e_3,\quad
    (u_1,u_2)=(\lambda_1/\lambda_3,\lambda_2/\lambda_3).
    \tag{NCX3}
   \]
   Every cycle has coefficients \((a,b,-a-b)\), so \(z_1,z_2\) are an integral basis. A vertex change multiplies all three \(\lambda_i\) by the same unit, so both ratios are unchanged over any ring, including a ring with nilpotents. Conversely choose the root frame one and the other frame \(\lambda_3\); this makes the third edge one and gives exactly these two ratios.

4. The normalized universal line on \(E\times E\) evaluates at \(a\) to \(\mathcal O_E([a]-[0])\), by (NC27). The rational component has trivial Jacobian and trivial universal component line. Therefore
   \[
       F_e\simeq\mathcal O_E([0]-[a]),\qquad
       N_{\mathbf P^1}=F_e^{-1}\simeq\mathcal O_E([a]-[0]).
       \tag{NCX4}
   \]
   This base-line twist on the rational component makes its branch fibre equal to the elliptic branch fibre. The tree edge then glues canonically. There are no non-tree edges, so \(G=E\). A naive construction insisting that every component base line be trivial would wrongly require a global frame of the nontrivial \(F_e\); the recursive \(N_v\) is what removes that false requirement.

5. Orient the triangle cyclically. Its cycle lattice is generated by \(e_1+e_2+e_3\), so \(r=1\), \(g=1\), \(G=\mathbf G_m\), and
   \[
       0\to K\to K^3\xrightarrow{d}K^3
                 \to H^1(C,\mathcal O_C)\to0,
       \qquad H^1(C,\mathcal O_C)\simeq K.
       \tag{NCX5}
   \]
   A rotation preserves the cycle generator and acts trivially on the torus. A reflection reverses it and acts by \(t\mapsto t^{-1}\). Its tangent is multiplication by \(-1\), which is \(+1\) in characteristic two. Nevertheless
   \[
          (1+\epsilon)^{-1}=1+\epsilon+\epsilon^2
                \ne1+\epsilon
          \quad\text{in }K[\epsilon]/(\epsilon^3),\quad \operatorname{char}K=2.
          \tag{NCX6}
   \]
   Thus the whole automorphism is not determined by that tangent action.

6. Here \(b=3,r=2\). Consequently
   \[
       \dim G=g=5,\qquad \operatorname{rank}G[n]=n^8,
       \qquad\operatorname{rank}_{\mathbf Z_\ell}T_\ell G=8.
       \tag{NCX7}
   \]
   A smooth genus-five Jacobian has Tate rank ten. The difference is two, the cycle rank. In characteristic \(p\), the torus kernel is
   \[
       T_\Gamma[p]=\mu_p^2,\qquad
       \mathcal O(\mu_p^2)=K[u,v]/(u^p,v^p),
       \quad t_1=1+u,\quad t_2=1+v.
       \tag{NCX8}
   \]
   It has full length \(p^2\) and only one geometric point. It is a subgroup of \(G[p]\), whose rank remains \(p^8\). Replacing the torus kernel by its point count would destroy the finite flat rank formula.

7. The specified curve is smooth in characteristic zero and both points are distinct from infinity. By NC8,
   \[
          F=\mathcal O_E([b]-[a]),\qquad G=F^\times\to E.
          \tag{NCX9}
   \]
   The genus-one Abel isomorphism identifies its class with \(b-a\), which is nonzero since \(a\ne b\). Both displayed points are two-torsion, so this is a nonzero two-torsion line, in particular nontrivial. A section of its frame bundle would be a nowhere-zero section of the line and would trivialize it. Hence there is no section, and no product extension over \(E\). Here \(b=1,r=1,g=2,\dim G=2\), and its prime-to-characteristic Tate rank is three.

8. Lift a section of \(J[n]\) locally to \(G\). Its multiple is in the torus; divide that element after adjoining monic \(n\)-th roots of units, then subtract the division. This makes the lift \(n\)-torsion. The kernel and relation are the full \(T_\Gamma[n]\), so this is a torsor on all schemes, not only on fields. Finite flat descent and CU8 give rank \(n^{2b+r}\). Dividing an arbitrary section first in \(J\), lifting, and correcting its torus difference proves fppf surjectivity of multiplication on \(G\).

   For a compatible sequence in the quotient Tate module, any finite initial segment lifts by lifting its last term and multiplying down. These are finite nonempty compatibility sets, nested under extension. Finite inverse-limit compactness gives a simultaneous lift. The kernel is the compatible torus tower, giving exactly (NC23). It does not supply an equivariant splitting of that extension.

9. Exchanging the first two edges swaps \(z_1,z_2\). Reversing all edges and exchanging the two vertices sends each \(z_i\) to \(-z_i\). Their matrices on \(X\) are
   \[
       S=\begin{pmatrix}0&1\\ 1&0\end{pmatrix},\qquad
       R=-I_2.
       \tag{NCX10}
   \]
   On the dual Tate lattice, the edge part is the inverse transpose; these two matrices happen to equal their own inverse transposes. A semilinear action also acts on the values in \(\mathbf Z_\ell(1)\), as in (NC25). Omitting that cyclotomic action changes the representation. Pullback of lines reverses composition, so a left action of curve automorphisms uses inverse pullback on the group. The character identity (NC24) records the convention without suppressing the orientation signs.

10. In the basis \(z_1,z_2\), the inclusion into the edge lattice and its weighted Gram matrix are
   \[
       C=\begin{pmatrix}1&0\\ 0&1\\ -1&-1\end{pmatrix},\qquad
       Q=C^{\mathsf T}\operatorname{diag}(m_1,m_2,m_3)C
         =\begin{pmatrix}m_1+m_3&m_3\\ m_3&m_2+m_3\end{pmatrix}.
       \tag{NCX11}
   \]
   For any nonzero rational or real cycle vector, \(Cz\ne0\), so its quadratic value is a sum of positive weights times squares and is strictly positive. Its determinant is \(m_1m_2+m_1m_3+m_2m_3>0\). For \(1,2,3\) it becomes
   \[
       Q=\begin{pmatrix}4&3\\ 3&5\end{pmatrix},\quad
       \det Q=11,\quad
       \operatorname{coker}Q\simeq\mathbf Z/11,\quad
       Q^{-1}=\frac1{11}\begin{pmatrix}5&-3\\ -3&4\end{pmatrix}.
       \tag{NCX12}
   \]
   The first Smith factor is the gcd of its entries, one, and their product is the determinant, by PC0's full integer Smith proof. A signed edge permutation preserves the form when it preserves the edge weights; the signs simply change orientation coordinates. Swapping weights one and two in the displayed numerical example does not preserve this fixed weighted form. These are integral graph calculations. Identifying such weights or this pairing with geometric thickness or monodromy still requires the model and period construction, and has not been inferred here.

### 2Q. Line bundles through the infinitesimal neighbourhood of a nodal fibre

The group in §2P describes a nodal fibre. We now deform its line bundles over a supplied proper flat family. The construction keeps the nilpotent coefficients and produces an actual formal group at the identity. A compatible formal line bundle will mean a system on the finite thickenings with its restriction isomorphisms; algebraization of that system is a separate assertion.

Fix a complete discrete valuation ring \(R\), with uniformizer \(\pi\), residue field \(k\), and a proper flat finitely presented morphism
\[
 f:\mathcal C\longrightarrow\operatorname{Spec}R,\qquad
 P:\operatorname{Spec}R\longrightarrow\mathcal C .
 \tag{NQ1}
\]
Assume that the closed fibre \(C\), with root \(P_k\), is the split connected nodal curve constructed in NC1–NC8. Put
\[
 b=\sum_v g_v,\qquad r=|E|-|V|+1,\qquad g=b+r .
 \tag{NQ2}
\]
There is no assumption here that an arbitrary smooth curve already has such a model. For an \(R\)-algebra \(A\), write \(\mathcal P(A)\) for isomorphism classes of lines \(L\) on \(\mathcal C_A\) with an isomorphism \(P_A^*L\simeq\mathcal O_A\). Tensor product gives its group law. On local Artinian \(R\)-algebras with specified residue field \(k\), define
\[
 \widehat{\mathcal P}(A)=
 \ker\bigl(\mathcal P(A)\longrightarrow\mathcal P(k)\bigr).
 \tag{NQ3}
\]
Here a test algebra is a local \(R\)-algebra with specified residue field \(k\) and finite length as a module over itself. Its maximal ideal is nilpotent: finite length makes every ideal finitely generated and the descending sequence of its powers stationary; Nakayama applied to a stationary power makes that power zero. Morphisms are local \(R\)-algebra maps inducing the identity on \(k\).

Free comparisons for the deformation terminology are the Stacks project's [Picard groups of thickenings](https://stacks.math.columbia.edu/tag/0C6Q) and [smooth deformation functors](https://stacks.math.columbia.edu/tag/06HF). The proofs below use the already written affine Čech and finite-complex arguments; no representability or algebraization theorem is taken from those comparisons.

#### 2Q.1. Cohomology of the supplied family, with every coefficient module

**NQ1.** The module \(M=H^1(\mathcal C,\mathcal O_{\mathcal C})\) is free of rank \(g\). For every \(R\)-module \(N\), the natural coefficient maps give
\[
 H^0(\mathcal C,\mathcal O_{\mathcal C}\otimes_RN)=N,\qquad
 H^1(\mathcal C,\mathcal O_{\mathcal C}\otimes_RN)=M\otimes_RN,\qquad
 H^q(\mathcal C,\mathcal O_{\mathcal C}\otimes_RN)=0\ (q\ge2).
 \tag{NQ4}
\]
For every \(R\)-algebra \(A\), the analogous formulas on \(\mathcal C_A\) hold with coefficients in any \(A\)-module \(I\), viewed on the right as an \(R\)-module. In particular,
\[
 \Gamma(\mathcal C_A,\mathcal O_{\mathcal C_A})=A .
 \tag{NQ5}
\]
The identifications of degree zero send \(a\) to the constant section \(a\).

*Proof.* Apply Lesson 3, FC10, to the flat structure sheaf of the proper family. It gives a bounded nonnegative finite free complex after choosing bases over the local ring \(R\), and an actual comparison with the flat affine Čech complex which stays a quasi-isomorphism after tensoring with any module, by FC9. Cancel every unit entry as in FC13. The remaining differential matrices have entries in \((\pi)\), so reduction modulo \(\pi\) makes every differential zero. NC4 and NC6 say that the closed-fibre cohomology has dimensions \(1,g,0,0,\ldots\). Thus the remaining terms have ranks \(1,g,0,0,\ldots\).

The actual global section \(1\) is a degree-zero cycle whose reduction is the closed-fibre basis. FC16 makes it a basis of the degree-zero term and forces its outgoing differential to be zero. We have therefore obtained a comparison, valid under every tensor specialization, with
\[
                    [\,R\xrightarrow{\ 0\ }R^g\,]
                     \quad\hbox{in degrees }0,1 .
                     \tag{NQ6}
\]
This proves (NQ4), and identifies the second term with \(M\). The module is free without choosing a preferred basis.

For the asserted coefficient formula after \(R\to A\), choose the same finite affine cover of \(\mathcal C\). Each intersection is affine by separatedness. Its coordinate module \(B\) becomes \(B\otimes_RA\); tensoring further with \(I\) gives \(B\otimes_RI\). The resulting coefficient Čech complex is consequently the same tensor specialization used in (NQ4). Affine acyclicity and the signed affine Čech comparison SC11–SC12 apply over arbitrary rings. These are the natural restriction and coefficient maps, so all identifications commute with algebra maps and coefficient homomorphisms. The actual unit gives (NQ5). \(\square\)

An automorphism of an invertible sheaf is multiplication by a global unit: locally it is multiplication by a function, and the functions agree under a change of rank-one frame. By (NQ5) that unit comes from \(A^\times\). Preserving the root trivialization forces it to be \(1\). Thus between isomorphic rigidified lines there is a unique rigidified isomorphism, on nonreduced bases as well.

#### 2Q.2. Lifting lines and measuring all the choices

**NQ2.** Let \(A'\twoheadrightarrow A\) be a surjection of arbitrary \(R\)-algebras, with square-zero kernel \(I\). There is a natural exact sequence of groups
\[
 0\longrightarrow M\otimes_R I
   \longrightarrow\mathcal P(A')
   \longrightarrow\mathcal P(A)\longrightarrow0 .
 \tag{NQ7}
\]
In particular each nonempty fibre of restriction is a torsor under \(M\otimes_RI\): its elements differ by a unique such class. There is no preferred lift in general.

*Proof.* Flatness of \(\mathcal C_{A'}\) over \(A'\) identifies the ideal of \(\mathcal C_A\) with
\[
                 \mathcal J=\mathcal O_{\mathcal C_A}\otimes_A I .
                 \tag{NQ8}
\]
It has square zero. On an affine chart the restriction of functions is a surjection. A lift of a unit is a unit: if its product with a lifted inverse is \(1+j\), then multiplication by \(1-j\) supplies an inverse. Hence functions and units can be lifted on affine intersections.

Start with a line on \(\mathcal C_A\). Choose a finite affine cover of \(\mathcal C_{A'}\), refined by finitely many principal opens so that the restricted line is free on every reduced chart. This is possible because principal opens form an affine basis and the base change is quasi-compact. A principal function on a quotient chart lifts to its original affine chart. The lifted principal opens still cover: the square-zero closed immersion is a homeomorphism. All intersections in this cover are affine.

Write the transition units as \(u_{ij}\), with \(u_{ij}u_{jk}=u_{ik}\), and lift them to units \(\widetilde u_{ij}\), choosing reverse transitions as inverses. On triple intersections define
\[
 \widetilde u_{ij}\widetilde u_{jk}\widetilde u_{ik}^{-1}
                   =1+c_{ijk},\qquad c_{ijk}\in\mathcal J .
 \tag{NQ9}
\]
Multiplying the two associations of a four-fold product shows
\[
             c_{jkl}-c_{ikl}+c_{ijl}-c_{ijk}=0 .
             \tag{NQ10}
\]
Products of two elements of \(\mathcal J\) vanish, so no omitted higher terms occur. Thus \(c\) is an additive Čech 2-cocycle. NQ1 gives \(H^2(\mathcal C_A,\mathcal J)=0\). The affine comparison therefore writes \(c=\delta d\) for a Čech 1-cochain \(d\). Replace \(\widetilde u_{ij}\) by \(\widetilde u_{ij}(1-d_{ij})\). Equation (NQ9) then becomes the exact cocycle identity. Gluing free rank-one modules with these units constructs a line \(L'\).

To rigidify it, replace \(L'\) by
\[
       (L')^\natural=L'\otimes f_{A'}^*(P_{A'}^*L')^{-1}.
       \tag{NQ11}
\]
Evaluation supplies the root trivialization. On reduction this recovers the given rigidified line using its given trivialization; it does not require that the root line on \(\operatorname{Spec}A'\) be globally free.

Now compare two lifts and their unique rigidified identification over \(A\). After a common affine refinement, their transition ratios are \(1+a_{ij}\), with \(a\) an additive 1-cocycle in \(\mathcal J\). Changing compatible local frames changes \(a\) by a Čech boundary. Conversely every such 1-cocycle gives a line trivial on reduction. If its class is zero, the frames give a trivialization of the line; normalize that trivialization at the root. More explicitly, a chosen reduction trivialization can be matched because a unit of \(A\) lifts to a unit of \(A'\). This also shows that there is no quotient by an unaccounted group of global units. NQ1 identifies the resulting classes with \(M\otimes_R I\). Tensor product adds \(a\), since
\[
                       (1+a)(1+a')=1+a+a' .
                       \tag{NQ12}
\]
This proves exactness, freeness and transitivity in (NQ7). Restricting the equations proves naturality. \(\square\)

A surjection of local Artinian rings can be factored into square-zero surjections: use successive powers of its nilpotent kernel. It can also be factored into **small** surjections, whose kernels \(I\) satisfy \(\mathfrak m_{A'}I=0\). For a nonzero ideal in an Artinian local ring, take its last nonzero product by a power of the maximal ideal and then a one-dimensional residue-field subspace; it is an ideal killed by that maximal ideal. Quotient by it and induct on length. Consequently every rigidified line over \(k\) lifts through every Artinian test ring. For a small extension the choice module is
\[
                 M\otimes_RI=H^1(C,\mathcal O_C)\otimes_k I .
                 \tag{NQ13}
\]

#### 2Q.3. A compatible universal line system

**NQ3.** Choose a basis \(e_1,\ldots,e_g\) of \(H^1(C,\mathcal O_C)\), and put
\[
 S=R[[t_1,\ldots,t_g]],\qquad
 \mathfrak n=(\pi,t_1,\ldots,t_g),\qquad S_n=S/\mathfrak n^{\,n+1}.
 \tag{NQ14}
\]
There are compatible rigidified lines \(\xi_n\) on \(\mathcal C_{S_n}\), reducing to the trivial line over \(k\), whose first-order class in the variable directions is
\[
                             \sum_{i=1}^g e_i\otimes t_i .
                             \tag{NQ15}
\]
They may be chosen to restrict to the trivial rigidified line under \(t_1=\cdots=t_g=0\) at every order.

*Proof.* Start with the trivial line on \(S_0=k\). The map \(S_1\to R/(\pi^2)\) setting all variables to zero has square-zero kernel freely spanned over \(k\) by the \(t_i\). NQ2 identifies the lifts of the trivial line with \(H^1(C,\mathcal O_C)\otimes_k k^g\). Choose (NQ15).

Suppose \(\xi_n\) has been chosen with the stated augmentation property. The kernel of \(S_{n+1}\to S_n\) is \(\mathfrak n^{n+1}/\mathfrak n^{n+2}\), a square-zero ideal. NQ2 lifts \(\xi_n\) to a line \(\eta\) on \(S_{n+1}\). Its augmentation is a rigidified line \(\eta_0\) on \(R/(\pi^{n+2})\), trivial modulo \(\pi^{n+1}\). Pull \(\eta_0\) back along the constant-coefficient map
\[
                     R/(\pi^{n+2})\longrightarrow S_{n+1}
                     \tag{NQ16}
\]
and tensor \(\eta\) with its inverse. The new augmentation is trivial and its restriction to \(S_n\) is still \(\xi_n\). The restriction isomorphisms are unique after rigidification, so their further compatibility is automatic. This constructs the entire system. For \(g=0\) it is simply the trivial system on the quotients of \(R\). \(\square\)

The construction gives actual finite-level line bundles. It does not identify a power series with an algebraic transition function on \(\mathcal C\).

#### 2Q.4. Why these coordinates represent every infinitesimal line

**NQ4.** Pullback of this system gives natural bijections
\[
 \theta_A:\operatorname{Hom}^{\rm loc,cont}_{R}(S,A)
       =\mathfrak m_A^g\xrightarrow{\ \sim\ }\widehat{\mathcal P}(A)
 \tag{NQ17}
\]
for every local Artinian test algebra \(A\). Thus \(S\), together with the system just constructed, prorepresents this formal functor. Both existence and uniqueness are part of (NQ17).

*Proof.* A tuple in \(\mathfrak m_A^g\) defines the substitution map from \(S\), since the maximal ideal of \(A\) is nilpotent. The map factors through some \(S_n\). Compatibility of \(\xi_n\) makes its pulled-back class independent of \(n\), defining \(\theta_A\).

We first compute how this map changes across a small extension \(A'\twoheadrightarrow A\) with kernel \(I\). Fix a tuple \(a\in\mathfrak m_{A'}^g\) and \(z\in I^g\). Then
\[
              \theta_{A'}(a+z)-\theta_{A'}(a)
                             =\sum_i e_i\otimes z_i
       \quad\hbox{in }H^1(C,\mathcal O_C)\otimes_k I .
       \tag{NQ18}
\]
Here the left difference means tensoring the first line with the inverse of the second, with its canonical reduction trivialization.

To check (NQ18), use a fixed finite affine cover of \(\mathcal C\). On each chart a line whose reduction is free modulo a nilpotent ideal is free: lift a generator of its rank-one projective module; nilpotent Nakayama makes the resulting map onto, projectivity splits it, and the reduction of its kernel is zero, so nilpotent Nakayama kills that kernel. Local frames of \(\xi_n\) can be chosen compatibly as \(n\) increases, since units lift across nilpotent ideals. Modulo \(\mathfrak n\) choose the trivial frame. Their transition units have first-order variable terms representing the \(e_i\).

In any sufficiently large finite quotient \(S_n\), subtracting the evaluations of a transition coefficient at \(a+z\) and \(a\) keeps only its linear variable terms modulo \(\mathfrak n\). Indeed every term involving a factor \(\pi\), another variable, or a second \(z\) vanishes after multiplication by \(z_i\): the hypotheses give
\[
                       \mathfrak m_{A'}I=0,\qquad I^2=0 .
                       \tag{NQ19}
\]
This calculation is valid on the affine coefficient modules as well; it is an identity in their tensor products with \(A'\). Dividing by the original transition unit changes nothing, since that unit is \(1\) modulo \(\mathfrak m_{A'}\). Thus the ratio cocycle is the sum of the first-order variable cocycles times the \(z_i\), which is (NQ18). No coefficient-field embedding into the mixed-characteristic ring \(R\) has been used.

Now induct on the finite length of \(A'\). For \(k\), both sides of (NQ17) have one element. Choose a one-dimensional small ideal \(I\subset A'\) and write \(A=A'/I\). By induction a class in \(\widehat{\mathcal P}(A')\) has a unique coordinate tuple over \(A\). Lift the tuple arbitrarily to \(A'\). NQ2 says that its pulled-back line differs from the desired line by one element of \(H^1(C,\mathcal O_C)\otimes_k I\). Since the \(e_i\) are a basis, (NQ18) gives exactly one coordinate correction in \(I^g\) removing that difference. This proves existence and uniqueness on each fibre over \(A\), and hence the bijection on \(A'\).

Pullback of lines commutes with substitution, so the bijections are natural. This proof constructs the representing object directly; no hull or representability criterion is being invoked. \(\square\)

The smallness condition is used only in the constant-derivative formula (NQ18), not in NQ2's square-zero lifting theorem.

#### 2Q.5. Tensor product gives a formal group law

**NQ5.** There is a commutative \(g\)-dimensional formal group law over \(R\) representing tensor product in (NQ17). In the chosen coordinates it consists of power series
\[
 F(X,Y)\in R[[X_1,\ldots,X_g,Y_1,\ldots,Y_g]]^g,\qquad
 F(X,0)=X,\quad F(0,Y)=Y ,
 \tag{NQ20}
\]
with an inverse series \(\iota(X)\), and it satisfies
\[
 F(F(X,Y),Z)=F(X,F(Y,Z)),\qquad
 F(X,Y)=F(Y,X),\qquad F(X,\iota(X))=0 .
 \tag{NQ21}
\]
Its linear term and multiplication series are
\[
 F(X,Y)=X+Y+\text{terms of total variable degree at least }2,\qquad
 [n]_F(X)=nX+\text{terms of degree at least }2 .
 \tag{NQ22}
\]
Its closed-fibre tangent space is \(H^1(C,\mathcal O_C)\); its tangent module over \(R\) is \(M\).

*Proof.* In each Artinian quotient of \(R[[X,Y]]\) by a power of \((\pi,X,Y)\), pull back the universal lines at \(X\) and at \(Y\), tensor them, and use NQ4 to get its unique coordinate tuple. These tuples are compatible under restriction. Taking the inverse limit gives the power series \(F\); completeness here is the definition of the power-series ring with its \((\pi,X,Y)\)-adic topology. The inverse-line operation similarly gives \(\iota\). The augmentation property of NQ3 identifies coordinate zero with the trivial line at every level, giving the unit equations.

Tensor associativity, symmetry, and evaluation of a line with its dual give the equations in (NQ21) in every finite quotient. Equality in their separated inverse limit proves the actual series identities. The unit equations imply that no constant term occurs and that the terms involving just one variable are exactly \(X\) and \(Y\). This proves the first formula in (NQ22), and induction under addition proves the second for every positive \(n\); inverse gives the analogous formula for negative \(n\).

For the tangent assertion apply NQ2 to the square-zero extension \((R/\pi^m)[\epsilon]/(\epsilon^2)\to R/\pi^m\). Its identity fibre is \(M/\pi^mM\), with addition of cocycles. These identifications commute with \(m\). Their inverse limit is \(M\), since \(M\) is finite free and \(R\) is complete. For \(m=1\) it is the closed-fibre space. The representing series give the same fibres and addition by NQ4, proving the claim. A change of the chosen universal system gives an invertible formal coordinate substitution by applying the two representing bijections to each other; composition is identity on every quotient. Thus the functor and formal group are intrinsic, although the coordinates are not. \(\square\)

#### 2Q.6. Prime-to-characteristic torsion through every thickening

**NQ6.** If \(n\) is a unit of \(R\), multiplication by \(n\) is an automorphism of \(\widehat{\mathcal P}\), and reduction gives natural bijections
\[
                         \mathcal P(A)[n]\xrightarrow{\ \sim\ }\mathcal P(k)[n]
                         \tag{NQ23}
\]
on all Artinian test algebras. The bijections commute with multiplication, tensor product and transitions between torsion orders.

*Proof.* We first invert \([n]_F\) as a series over \(R\). Its linear coefficient is the invertible matrix \(nI_g\). Suppose a substitution \(h(Y)\), with linear part \(n^{-1}Y\), has been chosen to make \([n]_F(h(Y))=Y\) through degree \(d-1\). Its error in degree \(d\) is a homogeneous tuple \(E_d\). Correct the degree-\(d\) part of \(h\) by \(-n^{-1}E_d\). Higher terms of \([n]_F\) cannot change this new degree except through its linear term. This recursively gives a right inverse. Uniqueness by the first nonzero homogeneous difference proves that the same series is a left inverse: applying the equation to \(h([n]_F(X))\) forces that tuple to equal \(X\). Thus multiplication is bijective on every nilpotent coordinate set in (NQ17).

Given \(x_0\in\mathcal P(k)[n]\), use NQ2 successively to lift it to \(y\in\mathcal P(A)\). Then \(ny\) lies in \(\widehat{\mathcal P}(A)\). There is a unique \(z\) in that subgroup with \(nz=ny\). Hence \(y-z\) is an \(n\)-torsion lift of \(x_0\). Two such lifts differ by an element of \(\widehat{\mathcal P}(A)[n]\), which is zero. This proves (NQ23). Every stated compatibility follows from uniqueness after reduction. \(\square\)

In particular there are compatible \(n\)-torsion line systems on the thickenings \(R/\pi^{m+1}\), one for each \(n\)-torsion class on \(C\). This statement concerns finite-level line bundles and their formal systems. It has not turned those systems into algebraic line bundles on \(\mathcal C\), or identified them with all torsion of the generic Jacobian.

#### 2Q.7. Supplied automorphisms act on the actual formal group

**NQ7.** Every \(R\)-automorphism \(\alpha\) of the supplied curve family acts functorially on these groups, even when it moves the root section. For a left action on the curve, the corresponding left action on rigidified lines is
\[
       [L]\longmapsto
       \bigl((\alpha^{-1})^*L\bigr)^\natural .
       \tag{NQ24}
\]
It induces a formal group automorphism whose tangent action is \((\alpha^{-1})^*\) on \(M\). The torsion lifts of NQ6 respect these actions.

*Proof.* Root normalization is (NQ11). It removes any line pulled back from the base. Applying two pullbacks and then normalizing therefore gives the same rigidified class as their composite followed by normalization. Since pullback reverses composition, inverse pullback has the left-action identity in (NQ24). Every possible intervening isomorphism preserving rigidification is unique by NQ1, so the identities hold on full families, not merely on closed points. Tensor product commutes with pullback and normalization.

At every finite universal quotient NQ4 now assigns a unique coordinate tuple to this transformed universal line. Compatibility produces a formal series \(A_\alpha(t)\), just as in NQ5. Its inverse is \(A_{\alpha^{-1}}\); the group identities and
\[
          A_{\alpha\beta}=A_\alpha\circ A_\beta,\qquad
          A_\alpha(F(X,Y))=F(A_\alpha(X),A_\alpha(Y))
          \tag{NQ25}
\]
follow by equality at each finite level. On a square-zero cocycle, pullback sends \(1+\epsilon c_{ij}\) to its pulled-back cocycle. Root normalization removes a base line, whose class is zero in NQ2's kernel description. This gives exactly the asserted action on \(M/\pi^mM\), and then on \(M\) by inverse limit. Finally an automorphism takes an \(n\)-torsion lift to a lift of the transformed closed class; uniqueness in NQ6 proves equivariance. Only automorphisms of the supplied family have been used. \(\square\)

#### 2Q.8. Constant nodal curves and the scope of the formal construction

**NQ8.** Suppose \(R=k[[\pi]]\) and the family, with its root, is the constant family \(C\times_k R\). On Artinian test algebras there is an exact sequence of formal group functors
\[
 0\longrightarrow\widehat{T_\Gamma}(A)
   \longrightarrow\widehat{\mathcal P}(A)
   \longrightarrow\prod_v\widehat{J_{C_v}}(A)\longrightarrow0 .
 \tag{NQ26}
\]
In cycle coordinates its kernel has parameters \(x_1,\ldots,x_r\) with group law
\[
       (x\mathbin{\star} y)_i=x_i+y_i+x_iy_i,\qquad
       [n](x)_i=(1+x_i)^n-1 .
       \tag{NQ27}
\]
Its tangent sequence is the normalization sequence (NC19).

*Proof.* NC5 identifies full multidegree-zero rigidified line families with \(G=J_C^0\). A line reducing to the trivial line has multidegree zero, since every geometric point of a local Artinian test ring factors through its residue field. Thus its identity formal functor is exactly the kernel of \(G(A)\to G(k)\).

The map \(G\to\prod J_{C_v}\) in NC5 is a product of line-frame bundles. After pullback to the local affine scheme \(\operatorname{Spec}A\), each of its finitely many lines is free: lift a residue-field generator and apply the local rank-one projective argument used in NQ4. Hence any quotient point lifts to \(G(A)\). If that point reduces to the identity, the reduction of such a lift lies in \(T_\Gamma(k)\). The coordinates of that torus point are units of \(k\), which lift to units of \(A\); translating by their inverse makes the lift reduce to the identity. The full kernel remains \(T_\Gamma(A)\), so the kernel on these identity fibres is \(\widehat{T_\Gamma}(A)\). This proves exactness in (NQ26).

NC4's cycle basis identifies that kernel with tuples of units \(\lambda_i\) reducing to \(1\). Write \(\lambda_i=1+x_i\), with \(x_i\in\mathfrak m_A\). Multiplying the units proves both identities in (NQ27). Differentiating the full line restriction and gluing maps gives NC6's cocycle sequence, which is the asserted tangent sequence. \(\square\)

Already for a rational curve with one node, the formal law is \(x+y+xy\), rather than the assertion that all higher coefficients vanish. In characteristic \(p\) it has \([p](x)=x^p\); on test algebras with nilpotents this is a substantive distinction from the additive law.

NQ1–NQ8 constructs the identity formal Picard group of the supplied family, with full square-zero lifting, unique formal coordinates, torsion lifting and supplied actions. For a varying nodal family it has not lifted the *entire* nodal-fibre semiabelian group, its torus and abelian quotient to a formal or algebraic extension. Nor has it constructed a semistable model of an arbitrary curve, proved algebraization of compatible lines, or produced an analytic period cover. Those remain necessary geometric steps toward Theorem 2.4.

#### 2Q.9. Graded exercise: infinitesimal lines and formal multiplication

**Exercise 2Q (100 points; ten parts of 10 points).**

1. Let \(R\) be a discrete valuation ring. Cancel the unit differential in the direct sum of the complexes \(R\xrightarrow{1}R\) in degrees \(0,1\) and \([R\xrightarrow{0}R^g]\). Explain why replacing that unit by \(\pi\) changes the closed-fibre ranks and cannot be cancelled. Explain the role of the actual section \(1\) in NQ1.
2. On a cover with three opens suppose lifted transition units satisfy \(\widetilde u_{01}\widetilde u_{12}\widetilde u_{02}^{-1}=1+c\), with \(c\) in a square-zero ideal. Write a correction on that triple when \(c=(\delta d)_{012}\). On four opens derive the additive cocycle identity, with signs.
3. Let \(A'=k[u]/(u^4)\), \(A=k[u]/(u^2)\), \(I=(u^2)\). Prove \(I^2=0\) but \(\mathfrak m_{A'}I\ne0\). Compute \((1+u+u^2)/(1+u)\) and explain why the constant-derivative formula NQ18 is restricted to small extensions.
4. For a split nodal curve with two smooth components of genera \(1,2\), joined by three edges, compute \(b,r,g\), the number of formal coordinates, and the dimension of the graph tangent subspace. For a one-dimensional small kernel \(I\) over \(k=\mathbf F_q\), count all lifts of any fixed rigidified line through that extension.
5. Starting from NQ15, explain the augmentation correction from order \(n\) to \(n+1\). Prove that this correction preserves the existing line and its first-order variable class. Distinguish this construction from choosing a canonical line at each order.
6. Let \(A'\twoheadrightarrow A\) be small with \(\dim_k I=d\). Prove that the coordinate fibre has \(I^g\) as its simply transitive translation group and that NQ18 identifies it with all line lifts. Explain both the surjectivity and the injectivity step of NQ4.
7. For the multiplicative formal law \(F(X,Y)=X+Y+XY\), compute its inverse and \([2]\), \([3]\). If \(2\) is a unit, compute the inverse of \([2]\) through degree three, with its precise denominators.
8. In characteristic \(p\), for \(a\ge1\) and \(N\ge1\), compute the full kernel of multiplication by \(p^a\) on the identity formal multiplicative group over \(A=k[\epsilon]/(\epsilon^N)\). Give its defining coordinate algebra as a formal subgroup and count its \(A\)-points when \(k=\mathbf F_q\). Compare it with the kernel on the additive formal group.
9. For a constant rational one-loop nodal curve, let an automorphism reverse the loop orientation. Compute its formal torus action, verify it is an involution and preserves \(F\), and identify its tangent action. In characteristic two, decide whether it is the identity on \(k[\epsilon]/(\epsilon^3)\).
10. Let \(k\) be algebraically closed, \(n\) invertible in \(k\), and suppose the closed nodal curve has invariants \(b,r,g=b+r\). Count its \(n\)-torsion classes and all their lifts to any Artinian test ring. Compare that number with \(n^{2g}\), the torsion rank of a smooth genus-\(g\) Jacobian. State precisely which model, group, algebraization and period assertions have not followed from the formal identity construction.

**Full solution.**

1. In bases separating the two summands, the degree-zero and degree-one modules have ranks \(2\) and \(g+1\), and the only nonzero differential entry is \(1\). The degree-\(-1\) map taking its target basis vector to its source contracts that pair. What remains is exactly
\[
                         [\,R\xrightarrow{0}R^g\,] .
                         \tag{NQX1}
\]
If the entry is \(\pi\), reduction makes it zero, so the closed-fibre cohomology dimensions are \(2,g+1\), not \(1,g\). The corresponding pair has zero degree-zero cohomology over \(R\) and degree-one cohomology \(k\), so it is not a contractible complex. In NQ1, the actual global unit is a cycle lifting the unique closed-fibre degree-zero basis. Its coefficient in the remaining rank-one term is a unit, forcing the entire outgoing differential to vanish over \(R\), including all powers of \(\pi\). A residue-field equality alone would not do that.

2. The additive differential is
\[
                 (\delta d)_{012}=d_{12}-d_{02}+d_{01}.
                 \tag{NQX2}
\]
Replace each transition by \(\widetilde u_{ij}(1-d_{ij})\). Its triple defect is
\[
 (1+c)(1-d_{01})(1-d_{12})(1+d_{02})
                      =1+c-d_{01}-d_{12}+d_{02}=1 .
 \tag{NQX3}
\]
All products of two ideal elements are zero, which justifies both the inverse and the last equality. Associating the product of transitions from \(0\) to \(3\) along the two possible successive triples gives
\[
                        c_{123}-c_{023}+c_{013}-c_{012}=0 .
                        \tag{NQX4}
\]
This is the signed 2-cocycle equation. Its solvability as a coboundary on the full cover uses NQ1's actual vanishing of \(H^2\), rather than just the presence of three chosen local lifts.

3. The ideal is spanned by \(u^2,u^3\); its square vanishes modulo \(u^4\), but \(u\cdot u^2=u^3\ne0\). Since \((1+u)^{-1}=1-u+u^2-u^3\), direct multiplication gives
\[
                  \frac{1+u+u^2}{1+u}=1+u^2-u^3 .
                  \tag{NQX5}
\]
The change is not \(1+u^2\). In a small extension the base-point factor \(u\) would annihilate the increment; here it does not. NQ2 still applies and classifies the square-zero difference, but NQ18's particular identification by the closed tangent basis alone requires smallness.

4. The edge boundary has rank one, so
\[
                  b=3,\qquad r=3-2+1=2,\qquad g=5 .
                  \tag{NQX6}
\]
There are five formal coordinates. The graph tangent subspace has dimension two, while the quotient component-Jacobian tangent space has dimension three. NQ2 makes the lift set a torsor under \(k^5\), so it has \(q^5\) elements. This is a count of every infinitesimal lift of the fixed line, and is independent of whether the fixed line is the trivial one.

5. Choose any lift \(\eta\) over \(S_{n+1}\) by NQ2. Its value at \(t=0\) is \(\eta_0\), trivial over \(R/\pi^{n+1}\). The corrected class is
\[
                    \xi_{n+1}=\eta-f^*\eta_0
                    \quad\hbox{in }\mathcal P(S_{n+1}),
                    \tag{NQX7}
\]
where \(f^*\) here denotes pullback by the constant-coefficient base map (NQ16). Its augmentation is zero. Its difference from \(\eta\) restricts to zero at order \(n\), so it still restricts to \(\xi_n\). Consequently its restriction to \(S_1\) is unchanged, proving preservation of NQ15. Several corrected lifts can remain: their differences lie in the kernel described by NQ2 subject to the augmentation condition. The construction chooses a compatible system; it does not assert that those choices are canonical.

6. Each coordinate lift can be changed by one element of \(I\), giving a simply transitive \(I^g\)-action on the fibre of tuples. On line lifts the action group is \(H^1(C,\mathcal O_C)\otimes_k I\). In the basis \(e_i\), the map is
\[
                I^g\longrightarrow H^1(C,\mathcal O_C)\otimes_k I,
                \qquad(z_i)\longmapsto\sum_i e_i\otimes z_i .
                \tag{NQX8}
\]
It is an isomorphism, with inverse given by basis coefficients. NQ18 says that the two fibre actions correspond under pullback. Thus an arbitrary discrepancy has a coordinate correction, proving surjectivity; two corrections giving the same line have zero image, hence are equal, proving injectivity. In particular over a finite field each fibre has \(q^{gd}\) elements. A proof of existence alone would establish neither unique coordinates nor prorepresentability.

7. The inverse, and the two multiplication series, are
\[
 \iota(X)=\frac{-X}{1+X}=-X+X^2-X^3+\cdots,\quad
 [2](X)=2X+X^2,\quad [3](X)=3X+3X^2+X^3 .
 \tag{NQX9}
\]
They follow by writing the coordinate as \(\lambda-1\). Write the inverse of \([2]\) as \(aY+bY^2+cY^3+\cdots\). Substituting in \(2h+h^2=Y\) gives \(2a=1\), \(2b+a^2=0\), \(2c+2ab=0\). Therefore
\[
                [2]^{-1}(Y)=\frac12Y-\frac18Y^2+\frac1{16}Y^3
                                  +\text{terms of degree at least }4 .
                \tag{NQX10}
\]
Only powers of two occur in the displayed denominators, so these coefficients lie in any ring where two is a unit. The calculation does not assume all positive integers are invertible.

8. Repeated Frobenius gives \([p^a](X)=X^{p^a}\). With \(h=p^a\), the full formal kernel has algebra
\[
          k[[X]]/(X^h),\qquad
          \Delta(X)=X\otimes1+1\otimes X+X\otimes X .
          \tag{NQX11}
\]
It has length \(h\). An \(A\)-point is an \(x\in(\epsilon)\) with \(x^h=0\). Write \(x=\sum_{j=1}^{N-1}c_j\epsilon^j\). Frobenius makes
\[
                x^h=\sum_{jh<N}c_j^h\epsilon^{jh}.
                \tag{NQX12}
\]
The exponents \(jh\) are distinct, and Frobenius is injective on a field. Thus exactly the coefficients with \(j<\lceil N/h\rceil\) must vanish. Over \(\mathbf F_q\) the kernel has
\[
                                  q^{\,N-\lceil N/h\rceil}
                                  \tag{NQX13}
\]
points. For the additive formal group multiplication by \(p^a\) is the zero series, so its kernel is the entire formal group, with all \(q^{N-1}\) identity points on this test ring. These assertions concern the full nilpotent functors, not only their one closed point.

9. Reversing the cycle takes \(\lambda\) to \(\lambda^{-1}\), so its coordinate is
\[
                                A(X)=\frac{-X}{1+X}.
                                \tag{NQX14}
\]
The identity \(1+A(X)=(1+X)^{-1}\) proves both \(A(A(X))=X\) and \(A(F(X,Y))=F(A(X),A(Y))\), by multiplication of units. Its tangent is \(-1\). In characteristic two it is \(+1\) on tangent space, but
\[
                  A(\epsilon)=\epsilon+\epsilon^2\ne\epsilon
                       \quad\hbox{in }k[\epsilon]/(\epsilon^3).
                  \tag{NQX15}
\]
Thus the tangent action does not determine the full finite action on the formal group.

10. NC7 supplies the finite étale group on the closed fibre with rank \(n^{2b+r}\). Over the algebraically closed field its algebra is a product of that many copies of \(k\): a finite reduced algebra splits into its maximal-field factors, and each finite extension of \(k\) is \(k\). Hence it has exactly that many points. Any torsion line has component degree zero because its degree vector is killed by \(n\) in the torsion-free group \(\mathbf Z^V\). Thus these are exactly \(\mathcal P(k)[n]\). NQ6 gives one and only one torsion lift of each class at every Artinian test algebra, compatibly at all orders. The count remains
\[
                        n^{2b+r}=n^{2g-r}.
                        \tag{NQX16}
\]
If a smooth generic genus-\(g\) Jacobian is also supplied, CU8 gives its full multiplication rank \(n^{2g}\); for \(n>1,r>0\) the ratio of these two numbers is \(n^r\). The formal identity neighbourhood has no nonzero \(n\)-torsion because \([n]\) is an automorphism there. Neither that fact nor the unique lifts of closed torsion proves that all generic torsion has been captured. A model of an arbitrary curve, a lift of the entire special semiabelian group with its torus and abelian quotient, algebraization of compatible lines, and a genuine analytic period cover with its lattice, lifting and action properties remain to be constructed. This conclusion retains those requirements; it does not replace them with the formal identity group.

### 2R. Algebraizing formal lines on a supplied projective model

A compatible line system is now turned into an actual line bundle. We prove the required existence statement, rather than using formal GAGA as a reference in place of an argument. Projectivity is part of the supplied input in this section; existence of a projective semistable model remains a separate geometric task.

The free comparison is the Stacks project's [projective existence theorem](https://stacks.math.columbia.edu/tag/087V), Lemmas 30.24.1–30.24.3. We prove the finite locally free case directly using the earlier finite-complex theorem, high-twist generation and Krull intersection. We do not require a category of arbitrary coherent formal modules or a general formal-functions theorem.

#### 2R.1. Recovering actual maps from all their finite restrictions

**NA1.** Let \((A,\mathfrak m,k)\) be a complete Noetherian local ring, let \(X\to\operatorname{Spec}A\) be proper, flat and finitely presented, and put
\[
 A_n=A/\mathfrak m^{n+1},\qquad X_n=X\times_A A_n\quad(n\ge0).
 \tag{NA1}
\]
For finite locally free sheaves \(V,W\) on \(X\), restriction induces an isomorphism
\[
 \operatorname{Hom}_X(V,W)
       \xrightarrow{\ \sim\ }
       \varprojlim_n\operatorname{Hom}_{X_n}(V|_{X_n},W|_{X_n}).
 \tag{NA2}
\]
Compatible isomorphisms algebraize to an isomorphism.

*Proof.* The sheaf \(E=V^\vee\otimes W\) is coherent and flat over \(A\), since \(X\) is flat over \(A\). Lesson 3, FC9–FC10, supplies a bounded nonnegative complex \(Q^\bullet\) of finite projective \(A\)-modules, and natural identifications of its tensor-specialized cohomology with that of \(E\). Finite projective modules over a local ring are free by T4–T5. Since there is no degree \(-1\), its degree-zero groups are actual kernels:
\[
 H^0(X,E)=\ker(d^0:Q^0\to Q^1),\qquad
 H^0(X_n,E_n)=\ker(Q^0/\mathfrak m^{n+1}Q^0\to
                              Q^1/\mathfrak m^{n+1}Q^1).
 \tag{NA3}
\]
Naturality in FC10 identifies the transition maps with restriction of these kernels. Finite free modules are complete and separated because \(A\) is. A compatible tuple in the kernels on the right therefore comes from one \(q\in Q^0\). Its differential is zero modulo every power of \(\mathfrak m\), hence zero in \(Q^1\). Conversely a degree-zero cycle gives exactly such a tuple. This proves (NA2). In particular we did not assume that all the restriction maps on sections are surjective.

If the finite-level maps are isomorphisms, their inverses are compatible too. Apply (NA2) to those inverses. The two composites restrict to identity at every order and are identity by injectivity in (NA2). \(\square\)

#### 2R.2. One finite presentation for every order

**NA2.** Assume also that a projective embedding \(X\hookrightarrow\mathbf P^N_A\) is supplied, and write \(H=\mathcal O_X(1)\). Suppose \(V_n\) are finite locally free sheaves on \(X_n\), with specified compatible identifications
\[
                        V_{n+1}|_{X_n}\simeq V_n .
                        \tag{NA4}
\]
There exist integers \(d,e\ge0\), finite integers \(a,c\), and compatible presentations, exact at every level,
\[
             H_n^{-e\,\oplus c}\longrightarrow H_n^{-d\,\oplus a}
                            \longrightarrow V_n\longrightarrow0 .
             \tag{NA5}
\]
Here \(H_n^{-d\,\oplus a}\) means the direct sum of \(a\) copies of \(H_n^{-d}\); both integers and both twists are fixed as \(n\) varies.

*Proof.* PF7–PF8 in Lesson 3 give \(d\) for which \(V_0(d)\) is generated by finitely many global sections and \(H^1(X_0,V_0(d))=0\). Write their number as \(a\). Flatness of \(X_{n+1}\) over \(A_{n+1}\) and local freeness of \(V_{n+1}\) give the exact layer sequence
\[
 0\to V_0(d)\otimes_k(\mathfrak m^{n+1}/\mathfrak m^{n+2})
       \to V_{n+1}(d)\to V_n(d)\to0 .
 \tag{NA6}
\]
For clarity, tensor the injection of the ideal layer into \(A_{n+1}\) with the flat \(A_{n+1}\)-module on each affine chart. The ideal layer is killed by \(\mathfrak m\), so its tensor depends only on \(V_0\). This gives (NA6) locally and hence globally.

The coefficient layer is a finite-dimensional \(k\)-space. Choosing a basis identifies the left sheaf with a finite direct sum of \(V_0(d)\), so its \(H^1\) is zero. The cohomology sequence makes restriction on global sections onto. Lift the \(a\) chosen generators successively and compatibly. They generate \(V_n(d)\): the cokernel of their evaluation has zero reduction modulo the nilpotent ideal \(\mathfrak m\mathcal O_{X_n}\), and nilpotent Nakayama kills that cokernel on each affine chart.

Let \(K_n\) be the kernel of the resulting surjection \(H_n^{-d\,\oplus a}\to V_n\). Locally the surjection onto the finite free target splits. Thus \(K_n\) is finite locally free and its formation commutes with restriction. Apply the same argument to \(K_0(e)\), choosing \(e\) with global generation and vanishing \(H^1\), and lift its finitely many generators. Their maps into \(H_n^{-d\,\oplus a}\) give (NA5). If a sheaf or kernel is zero, use the empty generator list. No bound on the number of infinitesimal orders enters \(a,c,d,e\). \(\square\)

#### 2R.3. Algebraizing the presentation and proving local freeness

**NA3.** Every compatible system (NA4) is the restriction of a finite locally free sheaf \(V\) on \(X\).

*Proof.* Put \(F_0=H^{-d\,\oplus a}\), \(F_1=H^{-e\,\oplus c}\). The first arrows of (NA5) are compatible maps between their restrictions. NA1 gives one actual map
\[
                        D:F_1\longrightarrow F_0 .
                        \tag{NA7}
\]
Let \(V=\operatorname{coker}D\). It is coherent, and right exactness of restriction gives compatible isomorphisms
\[
                             V/\mathfrak m^{n+1}V\simeq V_n .
                             \tag{NA8}
\]
It remains to prove that \(V\) is locally free; a compatible system of locally free quotients alone has not yet proved this.

Take \(x\in X_0\), set \(B=\mathcal O_{X,x}\), \(J=\mathfrak mB\), and \(U=V_x\). This is a finite module over the Noetherian local ring \(B\), and \(J\) lies in its maximal ideal. The given modules \(U/J^{n+1}U\) are free of a common finite rank \(s\): their rank is the rank of \(V_0\) at \(x\), by their restriction isomorphisms. Lift a basis of \(U/JU\) to \(U\). Nakayama gives a surjection \(B^s\to U\). Modulo \(J^{n+1}\) it is a map between free modules of the same rank and is invertible modulo \(J\). Its determinant is a unit modulo the nilpotent ideal \(J/J^{n+1}\), and hence a unit. Thus that map is an isomorphism at every order. Its kernel \(K\) satisfies
\[
                      K\subseteq\bigcap_{n\ge0}J^{n+1}B^s=0 ,
                      \tag{NA9}
\]
by the proved Krull intersection DFR3. Hence \(U\) is free.

For a finitely presented module, a free basis at one stalk extends to a neighborhood: lift the finitely many basis elements and the maps in an inverse presentation, and clear the finitely many denominators in their inverse identities. The associated finite kernel and cokernel vanish near the point. Applied on affine charts, this shows that the locus where \(V\) is locally free is open. Its closed complement \(Z\) misses \(X_0\). Since \(X\) is proper, its image in \(\operatorname{Spec}A\) is closed. Every nonempty closed subset of the spectrum of a local ring contains the closed point: it is \(V(I)\) for a proper ideal \(I\subseteq\mathfrak m\). Thus \(Z\) must be empty. This proves local freeness everywhere, including away from the closed fibre. \(\square\)

#### 2R.4. Equivalence, tensors and rigidification

**NA4.** For a supplied flat projective \(X/A\) as above, restriction is an equivalence between finite locally free sheaves on \(X\) and compatible finite locally free systems on the \(X_n\). It respects tensor products, duals, maps, and all specified commutative diagrams.

*Proof.* NA3 proves essential surjectivity, and NA1 proves full faithfulness. An isomorphism or diagram among the completed objects has a unique corresponding algebraic map or diagram. Indeed both sides of each asserted identity restrict to the same map at every finite order, so NA1 detects equality. Tensor and dual restriction are their local free-basis identities. Consequently the algebraization is unique up to its unique isomorphism inducing a specified isomorphism of systems. This is an equivalence for finite locally free sheaves; no assertion for arbitrary coherent systems is needed.

If a section \(P:\operatorname{Spec}A\to X\) is supplied, a compatible trivialization of \(P_n^*L_n\) algebraizes as well. The algebraized \(P^*L\) is a finite projective \(A\)-module of rank one, hence free over the local ring. Maps from it to \(A\) and back are the inverse limits of their maps modulo \(\mathfrak m^{n+1}\), by completeness of finite free modules. The compatible inverse trivializations therefore give actual inverse maps. This proves the equivalence for rigidified lines, with their prescribed trivializations. It also proves every tensor or action identity for those lines by equality at all finite orders. \(\square\)

#### 2R.5. The universal formal line is an actual line over a complete parameter ring

**NA5.** Return to the family \(\mathcal C/R\) of §2Q and assume it has a supplied projective embedding. With
\[
                   S=R[[t_1,\ldots,t_g]],\qquad
                   \mathfrak n=(\pi,t_1,\ldots,t_g),
                   \tag{NA10}
\]
the universal system \(\xi_n\) of NQ3 is the restriction of one rigidified line \(\Xi\) on the actual scheme \(\mathcal C_S\).

We first verify the ring hypothesis. The ring \(S\) is local: a series is a unit exactly when its constant term is a unit of \(R\), by solving its inverse coefficients recursively in the variable degree. Compatible quotients by \(\mathfrak n^{n+1}\) determine each variable coefficient modulo arbitrarily high powers of \(\pi\), so completeness of \(R\) gives completeness and separatedness of \(S\). Taking initial total orders gives
\[
                       \operatorname{gr}_{\mathfrak n}S
                                  \simeq k[U,T_1,\ldots,T_g].
                       \tag{NA11}
\]
Here \(U\) is the initial class of \(\pi\). In degree \(d\), the monomials \(\pi^a t^\alpha\), with \(a+|\alpha|=d\), have independent coefficients in \(k\); comparison of each formal variable coefficient modulo the appropriate power of \(\pi\) proves independence and spanning. Multiplication is the corresponding monomial multiplication. No coefficient-field embedding in \(R\) is required.

The polynomial ring in (NA11) is Noetherian by the proved Hilbert basis theorem N2. For an ideal \(I\subseteq S\), its initial forms are a homogeneous ideal there. Choose finitely many homogeneous generators and lift them to \(f_1,\ldots,f_c\in I\), with orders \(d_i\). For \(f\in I\), express its initial form as a sum of the initial \(f_i\) times homogeneous coefficients. Lift those coefficients to \(S\) and subtract the corresponding sum of \(f_i\), raising the order of the remainder. Repeat at each succeeding order. The corrections to the coefficient of \(f_i\) at remainder order \(d\) have order at least \(d-d_i\), so their sums converge in \(S\). Separatedness gives \(f=\sum_i a_if_i\). Thus \(I\) is generated by the finite list \(f_i\), proving that \(S\) is Noetherian without assuming that all its ideals are already closed.

Now base change the supplied projective embedding of \(\mathcal C\) to \(S\). The resulting scheme is projective, flat and finitely presented over the complete Noetherian local ring \(S\). NA4 applies to NQ3's compatible rigidified line system and gives \(\Xi\). In particular the line is algebraic over \(\operatorname{Spec}S\); this has not asserted that it descends to a polynomial parameter ring or a finite-type group scheme over \(R\).

There is a corresponding actual tensor identity over \(\mathcal C_{R[[X,Y]]}\):
\[
                              \Xi_{F(X,Y)}\simeq\Xi_X\otimes\Xi_Y .
                              \tag{NA12}
\]
The subscripts mean base change along the indicated continuous substitutions from \(S\). NQ5 proves this identity on every quotient by a power of \((\pi,X,Y)\). NA1 and NA4 make those compatible rigidified isomorphisms into the actual isomorphism (NA12), with all its associativity and symmetry identities. The same argument algebraizes NQ7's supplied action identities. \(\square\)

#### 2R.6. Actual line bundles and torsion on the projective model

**NA6.** Under NA5's hypotheses, write \(\mathcal P(R)\) for actual rigidified lines on \(\mathcal C\). There is an exact sequence
\[
 0\longrightarrow(\pi R)^g_F\longrightarrow\mathcal P(R)
                    \longrightarrow\mathcal P(k)\longrightarrow0 .
 \tag{NA13}
\]
The left set consists of tuples in \((\pi R)^g\), with the convergent group law \(F\) of NQ5. If \(n\) is a unit of \(R\), restriction gives a bijection of actual torsion groups
\[
                              \mathcal P(R)[n]\simeq\mathcal P(k)[n].
                              \tag{NA14}
\]
The statements commute with supplied family automorphisms and with base change to a supplied finite free extension of complete discrete valuation rings.

*Proof.* Rigidified lines have no nonidentity rigidified automorphisms by NQ1. Consequently a compatible sequence of their classes on \(\mathcal C_{R/\pi^{m+1}}\) has unique compatible restriction isomorphisms. NA4 identifies those classes with \(\mathcal P(R)\).

Every closed-fibre line lifts successively through those quotients by NQ2. Its compatible system algebraizes by NA4, proving the surjectivity in (NA13). For the kernel, NQ4 identifies each finite-order identity class with a tuple in the maximal ideal of \(R/\pi^{m+1}\). Taking compatible tuples gives exactly \((\pi R)^g\), by completeness of \(R\). The corresponding group laws are the substitutions of \(F\). The series converge on these tuples: a monomial of variable degree \(d\) is divisible by \(\pi^d\), and there are finitely many monomials of each degree. This proves (NA13) as a sequence of actual groups.

For \(n\) invertible, NQ6 gives a unique \(n\)-torsion lift of each closed class at every order, compatible with restriction. Algebraize the line and its compatible trivializations of its \(n\)-th tensor power by NA4; the result is actual \(n\)-torsion. Conversely a model torsion line with trivial closed class has trivial reduction at every order by NQ6, and is trivial by NA4. This proves (NA14).

Pullback of an actual line and its rigidification has the prescribed pullback at every order. For the finite free extension \(R\to R'\), the base-changed scheme remains flat and projective; its closed fibre is the scalar extension of the same split nodal curve. Repeat the proved statements there. The pullback of the original torsion lift is a torsion lift of the pulled-back closed class; uniqueness proves compatibility. The same uniqueness and NQ7 prove compatibility with supplied automorphisms. \(\square\)

#### 2R.7. Detecting a torsion line on the generic fibre

**NA7.** Assume in addition that the supplied model \(\mathcal C\) is normal and integral. Write \(K=\operatorname{Frac}R\). For every positive integer \(n\), generic restriction is injective on actual rigidified torsion:
\[
                         \mathcal P(R)[n]\longrightarrow\mathcal P(K)[n].
                         \tag{NA15}
\]
Here \(\mathcal P(K)\) denotes rigidified line classes on \(\mathcal C_K\). Normality in this statement is an explicit extra hypothesis.

*Proof.* Let \(L\) represent an element of the kernel. Choose its rigidified isomorphism \(L^{\otimes n}\simeq\mathcal O_{\mathcal C}\) and its rigidified generic trivializing section \(s_K\). NQ1 gives \(\Gamma(\mathcal C_K,\mathcal O)=K\), so the two generic trivializations of \(L^{\otimes n}\) agree: their scalar ratio is \(1\) at the root and hence \(1\) everywhere.

On an affine open trivializing \(L\), write \(s_K=z e\), where \(e\) is the local frame. Since the model is integral, its section \(z\), defined on the dense generic open, is a rational function in the fraction field of that affine domain. If the tensor-power isomorphism sends \(e^n\) to the unit \(a\), then
\[
                                  z^n=a^{-1}.
                                  \tag{NA16}
\]
Both \(z\) and \(z^{-1}\) are integral over the affine ring, by the monic equations \(Z^n-a^{-1}=0\) and \(Z^n-a=0\). Normality puts both in that ring, so \(z\) is an actual unit. To spell out this affine consequence of local normality, an integral rational function belongs to each integrally closed local ring; its local representations agree in the fraction field and therefore glue to a section of the affine structure sheaf. Thus \(s_K\) extends to a nowhere-zero section on every such open. These extensions agree on overlaps by equality of their rational functions. Their value at the root is \(1\), because its value in \(K\) is \(1\) and \(R\hookrightarrow K\). They give a rigidified trivialization of \(L\), proving injectivity. \(\square\)

This argument uses neither a claim that every generic line extends nor a divisor-class description of the model.

#### 2R.8. An actual saturated special-fibre Tate submodule

**NA8.** Suppose all the preceding model hypotheses hold, that \(k\) is algebraically closed, and that the supplied generic fibre is smooth geometrically integral of genus \(g\). Let \(J_K\) be its pointed Jacobian, and let \(G=J_C^0\) be NC5's special-fibre generalized Jacobian. For a prime \(\ell\ne\operatorname{char}k\), unique model torsion lifting and generic restriction give an injection
\[
                    T_\ell G\longrightarrow T_\ell J_K
                    \tag{NA17}
\]
with saturated image, fixed by \(\operatorname{Gal}(\overline K/K)\), of rank
\[
                         2b+r=2g-r .
                         \tag{NA18}
\]
The quotient as an abstract \(\mathbf Z_\ell\)-module is free of rank \(r\). This constructs the special-fibre Tate submodule inside the actual generic Tate module; it has not identified all Galois invariants or constructed the missing period lattice.

*Proof.* A torsion line on \(C\) has multidegree zero: its degree vector lies in the torsion-free group \(\mathbf Z^V\). Thus \(\mathcal P(k)[\ell^m]=G(k)[\ell^m]\). NA6 lifts it uniquely to model torsion, and NA7 injects it into \(\mathcal P(K)[\ell^m]\). Torsion has generic degree zero too, so JC's pointed representation identifies this with \(J_K(K)[\ell^m]\). These maps commute with multiplication and inclusions, by their construction, giving the injection in (NA17) after taking the compatible towers. All its finite-level points are \(K\)-rational, which proves the fixedness assertion.

We verify saturation rather than inferring it from an injection at each level. Suppose \(t\in T_\ell J_K\) and \(\ell^a t\) lies in the image of a tower \(s\in T_\ell G\). At level \(m+a\), regard all the torsion points as points of \(J_K(\overline K)\). The transition identity gives
\[
                         t_m=\ell^a t_{m+a}
                               =\operatorname{lift}(s_{m+a}) .
                         \tag{NA19}
\]
The model lift on the right is killed on the generic fibre by \(\ell^m\). Its \(\ell^m\)-multiple is model \(\ell^{m+a}\)-torsion and is generically trivial, so NA7 makes that multiple trivial on the model. Thus the lift is already model \(\ell^m\)-torsion. By NA6 it is the lift of its closed-fibre class \(u_m\in G(k)[\ell^m]\). The classes \(u_m\) are compatible: the generic restrictions of \(\ell\,\operatorname{lift}(u_{m+1})\) and \(\operatorname{lift}(u_m)\) are both \(t_m\), and NA7 detects their equality. Hence \(u\) is a tower mapping to \(t\). This proves saturation.

NC7 gives \(T_\ell G\) free of rank \(2b+r\), and CU9 gives \(T_\ell J_K\) free of rank \(2g\). Their quotient is finitely generated as a \(\mathbf Z_\ell\)-module because it is a quotient of a finite free module, and saturation says it is torsion-free. The DVR module proof in Lesson 1, 0A.1, makes it free; its rank is the difference \(r\). An abstract basis of this quotient may be lifted to give an abstract module splitting. No Galois-equivariant splitting is asserted. \(\square\)

The hypotheses above supply a model and impose its projectivity and normality; NA1–NA8 has not constructed that model from an arbitrary curve. Nor has it lifted the *whole* special semiabelian group and its quotient to a relative algebraic group, constructed an analytic covering, or identified the free rank-\(r\) quotient with a period lattice and its valuation pairing. Those obligations remain in Theorem 2.4.

#### 2R.9. Graded exercise: algebraization and the actual generic Tate module

**Exercise 2R (100 points; ten parts of 10 points).**

1. For a complete discrete valuation ring \(R\) and an integer \(a\ge1\), consider \(Q=[R\xrightarrow{\pi^a}R]\) in degrees zero and one. Compute every degree-zero kernel after reduction modulo \(\pi^{n+1}\), its transition map, and their inverse limit. Explain why NA1 does not require surjective transitions on sections.
2. In NA2, prove the ideal-layer identification (NA6) on an affine chart. If \(k=\mathbf F_q\), the layer \(\mathfrak m^{n+1}/\mathfrak m^{n+2}\) has dimension \(d\), and \(h^0(X_0,V_0(d_0))=h\) with \(H^1=0\), count all lifts of a fixed section through this layer. State why the same twist works at every order.
3. On \(\mathbf P^1_A\), algebraize the compatible presentations with quotient \(\mathcal O(1)\), middle term \(\mathcal O^{\oplus2}\), and relation column \((-X_1,X_0)^{\mathsf T}\). Verify exactness on both affine charts over every \(A_n\), including nonreduced \(A_n\). Identify \(a,c,d,e\) in (NA5).
4. On the nonproper scheme \(X=\operatorname{Spec}R[t]\), study multiplication by \(1-\pi t\) on \(\mathcal O_X\). Prove it is an isomorphism on every \(X_n\), find its compatible inverses, and prove it is not an isomorphism on \(X\). Compute its nonzero cokernel and all its reductions.
5. Let \(B\) be Noetherian local, \(J\) an ideal in its maximal ideal, and \(U\) a finite module whose quotients \(U/J^{n+1}U\) are free of fixed rank \(s\), compatibly with reduction. Prove \(U\) is free using only lifted generators, determinants and Krull intersection. Explain exactly where properness is subsequently used in NA3.
6. For the constant rational one-node curve over \(R=k[[\pi]]\), use its cycle coordinate to describe the universal line over \(S=R[[t]]\). Prove that the gluing unit \(1+t\) is valid over \(S\), compute its inverse, and explain why the same expression does not define that gluing over the whole affine parameter line \(\operatorname{Spec}R[t]\). Give an open polynomial parameter scheme where it does.
7. For the same constant nodal family and \(k=\mathbf F_q\), describe the exact sequence (NA13) and count its actual \(n\)-torsion model lines when \(p=\operatorname{char}k\) does not divide \(n\). Prove the lifts are constant in the cycle coordinate.
8. In characteristic different from two, let \(q=t(t-1)\), \(A=k+qk[t]\), and localize \(A\) at the node. In its fraction field put \(w=1-2t\). Show that \(w^2\) is a unit of the node local ring, that \(w\) and \(w^{-1}\) are integral over it, and that neither belongs to it. Explain what this example says about the normality hypothesis used in NA7, without claiming a global torsion-line counterexample.
9. Under NA8's hypotheses take two components of genera \(1,2\) joined by three edges. Compute the special and generic Tate ranks and the quotient rank. Given \(\ell^2t\) in the special-fibre image, carry out the saturation proof at each finite level. Explain why knowing only an injection of free modules would not suffice.
10. Under NA8's hypotheses take \(b=r=1\) and \(\ell=3\). Compute the orders of the special torsion subgroup and the full generic torsion at level \(3^2\), the finite-level quotient order, and the rank of the Tate-module quotient. Prove that this is a quotient of different ranks rather than a finite lattice index. State which geometric constructions are still needed to turn that quotient into an actual period lattice.

**Full solution.**

1. Put \(N=n+1\). An element of \(R/\pi^N\) is killed by \(\pi^a\) exactly when its lift has valuation at least \(\max(N-a,0)\), except that zero is always included. Therefore
\[
 H^0(Q\otimes_R R/\pi^N)=
                  \pi^{\max(N-a,0)}R/\pi^NR .
                  \tag{NAX1}
\]
The transition is ordinary reduction modulo \(\pi^{N-1}\). For \(N>a\), its image is the ideal generated by \(\pi^{N-a}\) modulo \(\pi^{N-1}\); it is smaller than the next kernel generated by \(\pi^{N-1-a}\) whenever those powers give distinct nonzero ideals. In particular the transitions are not eventually surjective. A compatible tuple gives a single element \(x\in R\), by completeness, with \(\pi^a x\) zero modulo every power. Separatedness makes \(\pi^a x=0\), and the domain \(R\) gives \(x=0\). Thus the inverse limit is zero, which agrees with \(H^0(Q)=0\). NA1's proof takes kernels inside finite complete free terms, so it uses precisely this argument and not surjectivity of the kernel transitions.

2. On an affine chart the module for \(V_{n+1}\) is flat over \(A_{n+1}\), since it is locally projective over a flat chart algebra. Tensor the exact ideal sequence
\[
 0\to\mathfrak m^{n+1}/\mathfrak m^{n+2}
          \to A_{n+1}\to A_n\to0 .
          \tag{NAX2}
\]
Because the ideal is killed by \(\mathfrak m\), its tensor is \(V_0\) tensored over \(k\) with that ideal. This is exactly (NA6), including after twisting. The resulting map on sections is onto because the left \(H^1\) is zero. The difference of any two lifts is a unique section of the left sheaf, whose space is \(k^{hd}\). There are \(q^{hd}\) lifts. The sheaf in every layer is a finite direct sum of the *same* \(V_0(d_0)\), so one vanishing twist suffices at every order.

3. Use the maps
\[
 0\to\mathcal O(-1)\xrightarrow{\,(-X_1,X_0)^{\mathsf T}\,}
        \mathcal O^{\oplus2}\xrightarrow{\,(X_0,X_1)\,}
        \mathcal O(1)\to0 .
        \tag{NAX3}
\]
Their composite is zero over any commutative coefficient ring. On \(X_0\ne0\), write \(u=X_1/X_0\) and trivialize the target by \(X_0\). The last map is \((a,b)\mapsto a+ub\), which is split onto, with kernel the free column \((-u,1)^{\mathsf T}\). On \(X_1\ne0\), with \(v=X_0/X_1\), it is \((a,b)\mapsto va+b\), with free kernel \((-1,v)^{\mathsf T}\). These are precisely the two frames of the displayed \(\mathcal O(-1)\) map. No division by a nilpotent coefficient occurs. Thus the maps are exact on both charts over every \(A_n\), and the identical matrix over \(A\) algebraizes them. Here
\[
                           a=2,\quad c=1,\quad d=0,\quad e=1 .
                           \tag{NAX4}
\]

4. Modulo \(\pi^{n+1}\), the inverse is the polynomial
\[
                1+\pi t+\cdots+(\pi t)^n .
                \tag{NAX5}
\]
Its product with \(1-\pi t\) is \(1-(\pi t)^{n+1}=1\) in that quotient, and the inverses are compatible. In the domain \(R[t]\), the degrees of two nonzero polynomials add, so its only polynomial units have degree zero. Thus \(1-\pi t\) is not a unit. Its cokernel is
\[
                         R[t]/(1-\pi t)\simeq R[1/\pi]\ne0 .
                         \tag{NAX6}
\]
The isomorphism sends \(t\) to \(\pi^{-1}\) and follows from the defining universal property of inverting \(\pi\). Every reduction of this cokernel is zero because \(\pi\) is invertible on it. Its support lies over the generic point. On this nonproper scheme, that nonempty support can have an image missing the closed point. The compatible inverse polynomials have unbounded degree and do not assemble to a polynomial inverse.

5. Lift a basis of \(U/JU\) and use Nakayama to obtain an onto map \(B^s\to U\). On every quotient it becomes a square matrix of rank \(s\), invertible modulo the nilpotent ideal \(J/J^{n+1}\), hence invertible. Thus its kernel lies in all \(J^{n+1}B^s\), whose intersection is zero by DFR3. This proves \(U\simeq B^s\). The proof applies at each point of the closed fibre in NA3. Finite presentation then makes the free locus open. Properness is used after this local argument: the closed bad locus has closed image in the local base, so a nonempty bad locus would meet its closed point. It does not, and therefore is empty. Part 4 shows why this last step cannot be discarded.

6. NC4–NC5 gives \(J_C^0=\mathbf G_m\); its pointed line is specified by a trivial line on the normalization and the one branch gluing unit
\[
                            \lambda=1+t .
                            \tag{NAX7}
\]
It is a unit in \(R[[t]]\), with inverse \(1-t+t^2-t^3+\cdots\). The full-family line-patching theorem NC3 constructs an actual invertible sheaf over that parameter scheme, with its root normalization; its finite restrictions are the identity universal line system in this coordinate. In \(R[t]\), \(1+t\) is not a unit, by the same degree argument as in part 4. Thus it does not define that branch *isomorphism* everywhere on the affine parameter line. It does define it on
\[
                         \operatorname{Spec}R[t,(1+t)^{-1}] .
                         \tag{NAX8}
\]
This is the open corresponding to the multiplicative coordinate \(\lambda\ne0\). The distinction is between a valid formal substitution and a claimed globally valid polynomial parameter, not a failure of the proved algebraization over the complete ring.

7. All degree-zero rigidified lines are the gluing units \(R^\times\), by NC's full-family construction for the constant curve. Reduction gives
\[
           1\to 1+\pi R\to R^\times\to k^\times\to1 .
           \tag{NAX9}
\]
Writing a unit in the kernel as \(1+x\) gives the law \(x+y+xy\) on \(\pi R\). The field's multiplicative group is cyclic of order \(q-1\), by the finite-field proof in Lesson 1. Its \(n\)-torsion therefore has order \(\gcd(n,q-1)\). Each such root is a constant element of \(k^\times\subset k[[\pi]]^\times\), and is already an actual \(n\)-torsion lift. NA6 proves that this lift is unique. Thus the model has exactly \(\gcd(n,q-1)\) such lines, all constant in the gluing coordinate. The inclusion \(k\subset R\) is part of this equal-characteristic example, rather than an assumed mixed-characteristic coefficient field.

8. In the fraction field \(t=(tq)/q\), and
\[
                            w^2=1+4(t^2-t)=1+4q .
                            \tag{NAX10}
\]
At the node this is a unit, as its residue is \(1\). The monic equations for \(w\) and \(w^{-1}\) are
\[
                    Z^2-(1+4q)=0,\qquad
                    Z^2-(1+4q)^{-1}=0 .
                    \tag{NAX11}
\]
They prove integrality of both. A function in the node local ring has equal values at the two normalization branches: its numerator has equal values at \(0,1\), and a denominator outside the node ideal has the same nonzero value at both. But \(w\) has branch values \(1,-1\), different in the stated characteristic. Thus \(w\) is not in that local ring. If \(w^{-1}\) were in it, multiplication by its unit \(w^2\) would put \(w\) there too, a contradiction. This shows that the integral-root argument in NA7 really uses normality. It does not by itself construct a global model torsion line that is generically trivial.

9. Here \(b=3\), \(r=3-2+1=2\), and \(g=5\). Hence
\[
                   \operatorname{rank}T_\ell G=8,\qquad
                   \operatorname{rank}T_\ell J_K=10,\qquad
                   \operatorname{rank}(T_\ell J_K/T_\ell G)=2 .
                   \tag{NAX12}
\]
If \(\ell^2t\) is the lift of \(s\), then at level \(m+2\) the transition identity gives \(t_m=\operatorname{lift}(s_{m+2})\) as a geometric generic point. That model lift is generically killed by \(\ell^m\); NA7 kills its \(\ell^m\)-multiple on the model as well. It is consequently already model \(\ell^m\)-torsion. Its closed class \(u_m\) lifts to \(t_m\), and generic injectivity makes the \(u_m\) compatible. Thus \(t\) belongs to the image. Without this argument an injection could have a torsion quotient: the inclusion \(\ell\mathbf Z_\ell\subset\mathbf Z_\ell\) is an injection of free rank-one modules and has quotient \(\mathbf Z/\ell\). The levelwise model argument proves the stronger saturated conclusion.

10. Now \(g=2\), and the two Tate ranks are \(3\) and \(4\). At order \(3^2=9\), the special group has \(9^3\) points over the algebraically closed residue field. Its unique model lifts form a subgroup of the full generic geometric torsion, which has \(9^4\) points. Numerically,
\[
                            9^3=729,\qquad 9^4=6561,\qquad
                            6561/729=9 .
                            \tag{NAX13}
\]
The Tate quotient is free of rank one by NA8. To compare its reduction with this finite-level quotient, NC7 makes projection of \(T_\ell G\) onto \(G[\ell^m]\) onto: choose successive lifts along the onto torsion transitions. CU9 gives the same statement for the generic Jacobian. A basis of the free Tate quotient can be lifted abstractly, giving a direct sum of free modules. Reducing that sum modulo \(\ell^m\) identifies the quotient of the finite-level torsion by the lifted special torsion with \(\mathbf Z/\ell^m\). In particular its order here is \(9\), as computed directly.

The Tate inclusion has different ranks, so its quotient is infinite and it has no finite lattice index. The finite ratio in (NAX13) measures a finite-level quotient, rather than an index of full lattices in one rational space. To interpret the rank-one quotient as a period direction one still needs an actual semiabelian integral extension, a genuine analytic covering and its kernel, finite-extension lifting and local-covering properties, compatible finite actions, and the resulting period valuation pairing. The supplied projective normal model must itself be constructed in the general theorem. NA1–NA8 supplies actual line algebraization and a saturated generic Tate submodule under those stated hypotheses; it has not replaced the remaining constructions.

### 2S. Projective closure and resolution of a supplied nodal model

There are two different geometric tasks here: obtaining a model, and arranging the shape of its special fibre. We construct a projective flat closure of an embedded generic curve. We then resolve a model whose nodes already have the explicitly supplied charts below. The missing step in general semistable reduction is producing those nodal charts after a finite extension.

Throughout, \(R\) is a discrete valuation ring, \(\pi\) a uniformizer, \(K\) its fraction field and \(k\) its residue field. Completeness is required only when we subsequently apply §2R. The elementary free comparisons are the Stacks project's [affine blowup algebras](https://stacks.math.columbia.edu/tag/052P), [blowup construction](https://stacks.math.columbia.edu/tag/01OF), and [nodal chart calculation](https://stacks.math.columbia.edu/tag/0CDC). All constructions used here are proved below.

#### 2S.1. A flat projective closure with a supplied section

**NS1.** Suppose \(C\subset\mathbf P^N_K\) is a smooth geometrically integral projective curve with homogeneous ideal \(J_K\). There is an integral flat projective finitely presented \(R\)-scheme \(\mathcal C\), with this generic fibre and embedding, obtained by contracting the equations:
\[
 J=J_K\cap R[X_0,\ldots,X_N],\qquad
 \mathcal C=V_+(J)\subset\mathbf P^N_R.
 \tag{NS1}
\]
Every supplied \(P\in C(K)\) extends uniquely to a section of this closure.

*Proof.* The polynomial ring is Noetherian by Lesson 3, N1–N2, so the homogeneous ideal \(J\) has finitely many homogeneous generators. On a nonempty standard affine chart the quotient coordinate ring injects into the coordinate ring of the generic curve. Indeed, homogenizing a polynomial relation on that chart shows that it lies in the contracted ideal if it vanishes generically; powers of the chart coordinate clear the denominators. Conversely, extension to \(K\) recovers \(J_K\), because a finite collection of coefficients has a common nonzero denominator in \(R\). Thus the generic fibre is exactly \(C\).

These chart rings are domains and contain \(R\); their generic opens are dense and belong to the same integral generic curve. Hence the charts glue to an integral scheme, and multiplication by \(\pi\) is injective in every chart. A torsion-free \(R\)-module is flat: its finitely generated submodules are free by Lesson 1, §0A; they form a directed union. Tensor products commute with this union, since every tensor and every relation uses finitely many elements. An element in the kernel of a tensor-specialized injection is therefore detected at a finite free stage, and is zero at a later such stage. This proves flatness without a finiteness assumption on the module. Apply it to each chart ring.

Write \(P=[a_0:\cdots:a_N]\). Scale its coordinates so that all \(a_i\in R\) and at least one is a unit, using the minimum of their valuations. They define an \(R\)-point of projective space. All equations in \(J\) vanish there, since their values vanish in \(K\) and \(R\hookrightarrow K\). This gives the section. For uniqueness, two such sections agree generically; the projective-space diagonal is closed, being defined by the cross products \(a_i b_j-a_j b_i\). These products vanish already over \(R\), so the sections agree. This proves the assertion. It proves no regularity or nodality of the special fibre. \(\square\)

#### 2S.2. Constructing the projective blowup and its universal property

**NS2.** Let \(X/R\) be integral, Noetherian and projective, and let \(I\subset\mathcal O_X\) be a nonzero coherent ideal. There is a projective modification \(b:X'\to X\), an isomorphism off \(V(I)\), with the following affine charts:
\[
 b^{-1}(\operatorname{Spec}B)
   =\bigcup_{a\in\{a_1,\ldots,a_s\},\ a\ne0}
       \operatorname{Spec}B[I/a],\qquad
 B[I/a]\subset\operatorname{Frac}B,
 \tag{NS2}
\]
where \(a_1,\ldots,a_s\) generate \(I\) on the chart. Its pullback ideal is invertible and is an effective Cartier ideal. It is universal for this property, commutes with flat base change, and has unique lifts of automorphisms preserving \(I\). If the centre is vertical, \(X'\) has the same generic fibre as \(X\) and is flat over \(R\).

*Proof.* Choose a projective embedding and write \(H=\mathcal O_X(1)\). By Lesson 3, PF7, some \(I(d)=I\otimes H^d\) has finitely many global generators \(s_1,\ldots,s_s\). Off \(V(I)\) they give a morphism to \(\mathbf P^{s-1}_R\). Take the scheme-theoretic closure of its graph in \(X\times_R\mathbf P^{s-1}_R\). This product is projective: the Segre coordinates \(Z_{ij}=X_iY_j\) give a closed embedding, with equations \(Z_{ij}Z_{ab}=Z_{ib}Z_{aj}\). On each open \(Z_{ab}\ne0\), these equations reconstruct the two affine coordinate lists and their products. These inverses verify the embedding on a cover, including rings with nilpotents.

Trivialize \(H^d\) on an affine open and write \(s_i=a_i\). In the projective chart indexed by a nonzero \(a_j\), the graph closure has coordinate ring equal to the image of
\[
 B[T_i:i\ne j]\longrightarrow\operatorname{Frac}B,\qquad
 T_i\longmapsto a_i/a_j.
 \tag{NS3}
\]
Indeed its kernel consists precisely of equations vanishing on the dense graph. This image is \(B[I/a_j]\). A zero \(a_j\) contributes an empty chart. On a nonempty chart, \(IB[I/a_j]=a_jB[I/a_j]\) and \(a_j\) is a nonzerodivisor. Away from the centre some \(a_j\) is already a unit, and that chart is unchanged.

Suppose \(f:Y\to X\) has \(I\mathcal O_Y\) locally generated by a nonzerodivisor \(t\). Write \(f(a_i)=t c_i\). The \(c_i\) generate the unit ideal: the \(a_i\) generate \((t)\), and \(t\) can be cancelled. On the opens where \(c_j\) is a unit, send \(a_i/a_j\) to \(c_i/c_j\). Every relation in (NS3), after multiplication by a power of \(a_j\), is a relation in \(B\); its pullback is zero, and cancellation of \(t c_j\) proves the original relation. This defines and glues the map \(Y\to X'\). It is unique: every ratio must satisfy that same identity, and cancellation makes its value unique on the indicated opens. Thus the construction is independent of generators and embeddings. An automorphism preserving \(I\) lifts by this property; its inverse and all composition identities lift uniquely as well.

Here is the required flat-base-change argument, including when the new ring is not a domain. The chart in (NS2) is the direct limit of \(R\)-modules \(I^n\), with transition multiplication by \(a\), and the multiplication of fractions supplies its algebra structure. If \(B\to D\) is flat, the inclusions \(I^n\subset B\) remain injective after tensoring, with images \((ID)^n\). Tensoring the direct limit gives the algebra of fractions
\[
 (f/a^n)=(g/a^m)
 \ \Longleftrightarrow\
 a^q(a^m f-a^n g)=0\text{ for some }q\ge0.
 \tag{NS4}
\]
The identifications respect overlap localizations, so they give the cartesian base-change statement. This also constructs the base-changed charts directly. Each original chart is a domain. If the centre is vertical its generic ideal is the unit ideal, so its generic blowup is the identity; its chart rings are torsion-free over \(R\), hence flat by NS1. \(\square\)

#### 2S.3. The node algebra, normality and exact dimension

**NS3.** For an integer \(h\ge1\), set
\[
 A_h=R[x,y]/(xy-\pi^h),\qquad
 \mathfrak m_h=(\pi,x,y).
 \tag{NS5}
\]
This is a flat normal domain. Its local ring at \(\mathfrak m_h\) has dimension two, and is regular exactly when \(h=1\). Away from this special point it is regular and smooth over \(R\). Put also \(A_0=R[x,x^{-1}]\), a smooth chart.

*Proof.* Sending \(y\) to \(\pi^h/x\) embeds \(A_h\) in \(K[x,x^{-1}]\). Reduction of mixed monomials and independence of Laurent monomials prove the unique finite normal form
\[
 a_0+\sum_{i\ge1}a_i x^i+\sum_{j\ge1}b_j y^j,
       \qquad a_i,b_j\in R.
 \tag{NS6}
\]
Thus \(A_h\) is free over \(R\) with the displayed basis.

We prove normality directly. The Laurent ring \(R[z,z^{-1}]\) is integrally closed. In fact its localization \(K[z,z^{-1}]\) is integrally closed: reduce a rational function to coprime numerator and denominator in the Euclidean ring \(K[z]\); a monic integral equation forces the denominator to be a unit after allowing powers of \(z\). Thus an integral element is a Laurent polynomial with coefficients in \(K\). The minimum valuation \(w\) of those coefficients is multiplicative under products: divide each polynomial by the appropriate power of \(\pi\) and reduce modulo \(\pi\), where the product of two nonzero Laurent polynomials is nonzero. If \(w(f)<0\), in a monic equation for \(f\) its highest power has strictly smaller valuation than all other terms, an impossibility. Consequently its coefficients lie in \(R\).

Inside \(K(x)\) we now have
\[
 A_h=R[x,x^{-1}]\cap R[y,y^{-1}],\qquad y=\pi^h/x.
 \tag{NS7}
\]
For the coefficient of \(x^i\), the two membership conditions are \(v(c_i)\ge0\) and \(v(c_i)\ge-hi\). These are exactly (NS6). An element integral over \(A_h\) is integral over each of the two Laurent rings, belongs to both, and hence belongs to \(A_h\).

For dimension, introduce \(s=x+y\). There is an isomorphism
\[
 A_h=R[s,x]/(x^2-sx+\pi^h),
 \tag{NS8}
\]
so this is a finite free integral extension of \(R[s]\). Every prime chain in \(R[s]\) has length at most two. Primes avoiding \(\pi\) correspond to primes in the principal ideal domain \(K[s]\); primes containing it correspond to primes in \(k[s]\). The only possible extra step would require a nonzero prime \(P\subset(\pi)\) avoiding \(\pi\). For \(0\ne f\in P\), divide all its coefficients by their largest common power of \(\pi\). Primality would put the resulting primitive polynomial in \(P\subset(\pi)\), a contradiction.

In an integral extension a strict prime inclusion has strict contraction. To see this, if its contractions both equal \(p\), quotient by the smaller prime and localize the nonzero elements of the base domain modulo \(p\). The resulting integral domain is integral over a field, hence a field: the monic equation of a nonzero element expresses its inverse as a polynomial in it. The purported larger prime cannot then survive; primality shows it does survive if the inclusion was strict. This contradiction proves the claim. It follows from (NS8) that the local dimension is at most two. The chain
\[
 (0)\subsetneq(\pi,x)\subsetneq(\pi,x,y)
 \tag{NS9}
\]
proves that it is exactly two.

For \(h=1\), \(\pi=xy\) and the maximal ideal has the two generators \(x,y\), so the local ring is regular. For \(h>1\), there is no linear relation among \(\pi,x,y\) modulo \(\mathfrak m_h^2\): present the local ring as the quotient of \(R[x,y]_{(\pi,x,y)}\), whose cotangent basis is precisely these three elements, and observe that \(xy-\pi^h\) belongs to the square. Its embedding dimension is three and its dimension is two, so it is not regular. Away from \(\mathfrak m_h\), either the point is generic or \(x\) or \(y\) is invertible. The resulting charts are open parts of a Laurent polynomial ring over \(R\) or \(K\), hence smooth; regularity follows from the flat regular-fibre test proved in Lesson 8, NM2. \(\square\)

#### 2S.4. The three saturated point-blowup charts

**NS4.** For \(h\ge2\), blow up \(\operatorname{Spec}A_h\) in \(\mathfrak m_h\). Its three charts, as subrings of \(K(x)\), are
\[
 \begin{aligned}
 B_\pi&=R[a,b]/(ab-\pi^{h-2}),&
       x&=\pi a,& y&=\pi b,\\
 B_x&=R[x,u]/(xu-\pi),&
       u&=\pi/x,& y&=\pi^{h-1}u,\\
 B_y&=R[y,v]/(yv-\pi),&
       v&=\pi/y,& x&=\pi^{h-1}v.
 \end{aligned}
 \tag{NS10}
\]
For \(h=2\), interpret \(B_\pi\) as \(R[a,a^{-1}]\).

*Proof.* The generators in NS2 are \(x/\pi,y/\pi\) in the first chart. Their product is \(\pi^{h-2}\); NS3's Laurent normal form proves that there are no other relations. In the \(x\)-chart the generators are \(x,u=\pi/x,y/x\), but
\[
 y/x=\pi^{h-2}u^2,\qquad xu=\pi.
 \tag{NS11}
\]
These show surjectivity of the stated chart map. The same normal-form injection for \(R[x,u]/(xu-\pi)\) into \(K(x)\) proves injectivity. The \(y\)-chart is symmetric.

This cancellation matters. Substitution into the unsaturated equation gives \(\pi^2(ab-\pi^{h-2})=0\) in the first chart and \(x^2(y/x-\pi^{h-2}u^2)=0\) in the second. The graph closure lies in a field, so the indicated factors can and must be cancelled. Retaining them would add components which are not part of the blowup.

On \(B_\pi\cap B_x\), the invertible coordinates satisfy \(a=u^{-1}\), \(x=\pi a\), and \(b=\pi^{h-2}u\). Both overlap rings are \(R[u,u^{-1}]\); the other overlap is symmetric. For \(B_x\cap B_y\) one additionally inverts \(\pi^{h-2}u^2\). The outer charts are regular thickness-one charts. The sole possible remaining nonregular point is the origin in \(B_\pi=A_{h-2}\), and it exists only when \(h-2>1\). The special fibre on every chart is reduced: its equation is a product of two distinct variables, or is the Laurent chart when \(h=2\). \(\square\)

#### 2S.5. Exceptional curves and termination

**NS5.** Repeating NS4 only at the remaining nonregular point takes \(\lfloor h/2\rfloor\) point blowups. The final special fibre replaces the original node by a chain of \(h-1\) copies of \(\mathbf P^1_k\) between the original branches, with \(h\) thickness-one nodes. For \(h=1\) the chain is empty.

*Proof.* For \(h=2\), the exceptional part of \(B_x\) is the affine line \(x=0\), with coordinate \(u\); that of \(B_y\) has coordinate \(v\). The central chart has coordinate \(a\ne0\), and identifies \(u=a^{-1}\) and \(v=a\). This is exactly the two standard affine lines of one projective line. The two original branches meet it at \(u=0\) and \(v=0\), respectively.

For \(h>2\), the exceptional fibre in the central chart consists of the \(a\)-axis and \(b\)-axis. The first glues by \(u=a^{-1}\) to the exceptional affine line of \(B_x\), and the second similarly glues to that of \(B_y\). They are two projective lines, meeting at the central node of thickness \(h-2\); their other ends meet the original branches. Thus the procedure subtracts two from the only unresolved thickness while inserting two end components, until it reaches \(1\), or reaches the final \(2\)-case just described. Induction gives \(h-1\) components and \(h\) edges, and the stated number of blowup rounds.

There is a necessary stopping rule. In the regular chart \(xy=\pi\), the maximal ideal is \((x,y)\). Its \(x\)-blowup chart has \(t=y/x\) and
\[
 R[x,t]/(x^2t-\pi),\qquad
 (R[x,t]/(x^2t-\pi))\otimes_R k=k[x,t]/(x^2t).
 \tag{NS12}
\]
The injection into the fraction field proves this chart identity; equivalently reduce every mixed monomial with \(x^2t=\pi\). The special fibre is not reduced: the nonzero class of \(xt\) is nilpotent. Thus blowing up every special-fibre node, including regular ones, would not prove the assertion. \(\square\)

#### 2S.6. Global resolution and supplied actions

**NS6.** Suppose \(\mathcal C/R\) is integral, flat and projective, with smooth geometrically integral generic curve. Assume its special fibre is split nodal and that it is smooth over \(R\) except at finitely many rational nodes. At each node assume an actual étale neighbourhood with an étale map to an open of \(\operatorname{Spec}A_{h_e}\), taking the node to \(\mathfrak m_{h_e}\), with residue-field identity and with that origin's inverse image equal to the single reduced node after shrinking. These are algebraic chart hypotheses, not merely isomorphisms of completed rings.

Blowing up the reduced union of the total space's nonregular points, and repeating this operation, produces a regular integral flat projective model \(\widetilde{\mathcal C}\) with reduced split nodal special fibre and unchanged generic curve. At most \(\max_e\lfloor h_e/2\rfloor\) rounds are needed. A supplied action on the original model lifts uniquely at every step; a section in its smooth locus lifts uniquely.

*Proof.* NS3 identifies the centre precisely as the nodes with \(h_e>1\). It is a finite reduced closed subscheme, and its coherent ideal is intrinsic. The étale neighbourhoods are flat, so NS2 identifies the blowup there with NS4, because the centre ideal pulls back to the reduced origin ideal.

Here are the local dimension and regularity details. Étale fibres are finite products of separable fields by Lesson 1, EA10. A strict inclusion of primes upstairs cannot have the same contraction: both primes would survive as a strict inclusion in that zero-dimensional fibre. Thus contraction bounds any local prime-chain length by the corresponding length downstairs. Flat going down, proved in EA14, gives the opposite inequality for local faithfully flat maps. Their local dimensions therefore agree. At our residue-identical node the local closed fibre is \(k\), so the base maximal ideal generates the new maximal ideal; flatness identifies its cotangent space with the scalar extension of the base cotangent space. Dimension and embedding dimension are thus exactly those of NS3, so the nonregular points are precisely the stated nodes. At all other points the flat regular-fibre test of NM2 proves regularity on the étale neighbourhoods. The same chain and cotangent argument descends regularity from a surjective étale neighbourhood: both dimensions are preserved, so equality of dimension with embedding dimension descends. This justifies the intrinsic centre used above.

Each step is projective, integral and flat by NS2 and is the identity on the generic fibre and off its finite centre. Every new potential centre is exactly the middle point of NS4. NS5 proves termination, including the bound. The exceptional fibres over a rational node are the actual projective lines just computed: the chosen étale neighbourhood has the same residue field and its fibre over that node is \(\operatorname{Spec}k\), so its exceptional fibre is the same fibre of the blowup. Reducedness and the nodal chart equations also descend along the faithfully flat neighbourhoods. Thus the claimed global fibre has exactly the stated components and intersections. Its regular local rings are normal by Lesson 8, NM1–NM2.

An automorphism, including a supplied semilinear automorphism over \(R\), preserves regularity and hence this reduced centre. NS2 lifts it uniquely. Lifting inverse and composition identities gives an action, rather than a set of unrelated maps. A smooth section avoids every centre and thus lifts through the isomorphism there. This does not extend a generic action which was never supplied on the starting model. \(\square\)

#### 2S.7. Cycles, genera and the actual special-fibre Tate module

**NS7.** Suppose the normalization components of the supplied split nodal fibre are smooth geometrically integral projective curves with genera \(g_v\). Put \(b=\sum_v g_v\), and let \(\Gamma\) be its connected dual graph. Resolution replaces each edge \(e\) by a path of \(h_e\) edges. Its integral cycle lattice is canonically the original one:
\[
 X=H_1(\Gamma,\mathbf Z)
   \xrightarrow{\ \sim\ }H_1(\widetilde\Gamma,\mathbf Z),
 \qquad (z_e)_e\longmapsto
      (z_e\text{ on every segment of the }e\text{-path}).
 \tag{NS13}
\]
The total component genus \(b\), cycle rank \(r\), and arithmetic genus \(b+r\) are unchanged.

*Proof.* Orient each new path from the old initial vertex to its old terminal vertex. At a new interior vertex the cycle boundary equation forces the two adjacent coefficients to agree. Thus every new cycle is uniquely of the displayed form, and its remaining boundary equations are exactly the old ones, including for loops and multiple edges. This proves the integral isomorphism without tensoring with a field. Each added component is \(\mathbf P^1_k\), whose \(H^1(\mathcal O)\) is zero by PF5's two-chart Laurent computation. The component genus is therefore unchanged. Adding \(h_e-1\) edges and as many vertices leaves \(|E|-|V|+1\) unchanged; NC6's normalization cohomology proves the arithmetic-genus formula. All statements commute with supplied graph actions by their definitions.

There is also a useful exact lattice calculation. On the subdivided graph use the sum of the products of segment coefficients. Under (NS13) it becomes
\[
 Q(z,w)=\sum_e h_e z_e w_e.
 \tag{NS14}
\]
Its positive definiteness follows because all \(h_e>0\); its integral matrix and cokernel can be calculated by PC0. This calculation alone does not identify \(Q\) with a geometric monodromy pairing.

If \(R\) is complete, \(k\) is algebraically closed, and a smooth section and the genus hypotheses of NQ1 are supplied, NS6 now supplies the projective normal model required in NA8. The already proved construction then gives, for \(\ell\ne\operatorname{char}k\),
\[
 T_\ell G_{\widetilde C}\hookrightarrow
 T_\ell J_C,\qquad
 \operatorname{rank}T_\ell G_{\widetilde C}=2b+r,\qquad
 \operatorname{rank}(T_\ell J_C/T_\ell G_{\widetilde C})=r.
 \tag{NS15}
\]
Here \(G_{\widetilde C}\) is the actual generalized Jacobian constructed in NC1–NC8, and the map is NA8's unique model-torsion lift followed by generic restriction. Its image is saturated and fixed by the absolute Galois group of \(K\). Those properties are NA7–NA8's proved conclusions, not consequences of comparing ranks. No period lattice or equality with all inertia invariants is inferred. \(\square\)

#### 2S.8. Ramification and the remaining model-existence step

**NS8.** Under a finite flat extension of discrete valuation rings \(R\to R'\), write \(\pi=\epsilon\varpi^e\), where \(\epsilon\in(R')^\times\). An old node of thickness \(h\) becomes one of thickness \(eh\):
\[
 xy=\epsilon^h\varpi^{eh}
 \quad\Longleftrightarrow\quad
 x(\epsilon^{-h}y)=\varpi^{eh}.
 \tag{NS16}
\]
When these remain the supplied nodal charts, NS6 applies again. It inserts \(eh-1\) components at that node. Under the canonical cycle identifications, (NS14) is multiplied by \(e\).

*Proof.* The unit change of variable in (NS16) is invertible over \(R'\). The assertion therefore follows directly from NS4–NS7. The length form has one coefficient for each of the \(eh\) unit segments, proving the scaling assertion integrally.

There is no contradiction with flat base change of a fixed blowup. A regular thickness-one node requires no resolution over \(R\); after a ramified extension with \(e>1\), it has thickness \(e\) and does require resolution. The choice of nonregular centre has changed. NS2 commutes a blowup of a specified ideal with flat base change; it does not assert that selecting the new nonregular locus commutes with ramified extension.

NS1 supplies a projective flat model of an embedded smooth generic curve, and NS6 makes an already nodal model regular. The theorem that some finite extension and modification of an arbitrary initial model have the algebraic nodal charts of NS6 is still required. Neither construction assumes that theorem or proves it by calling the starting model semistable. The whole semiabelian lift and the initial analytic period covering in Theorem 2.4 also retain their separate construction requirements. \(\square\)

#### 2S.9. Graded exercise: saturated charts and subdivided cycles

**Exercise 2S (100 points; ten parts of 10 points).** Use NS1–NS8, including their actual chart rings.

1. In \(\mathbf P^2_K\), take \(X_0X_1=\pi^4X_2^2\). Compute the contracted homogeneous ideal over \(R\). Extend the point \([\pi:\pi^3:1]\) to the model. Determine the special-fibre equation and the thickness at \([0:0:1]\).
2. Explain why \(\operatorname{Spec}R[t]/(\pi t)\) is not the flat closure of its generic fibre in \(\mathbf A^1_R\). Compute the actual contracted ideal. Prove the torsion-free flatness assertion needed for that closure.
3. Give the normal form in \(A_5\) of \(x^4y^2+x^2y^3\). For a Laurent polynomial \(\sum c_i x^i\), give the exact coefficient condition for membership in \(A_5\). Test \(x^{-1}\), \(\pi^4x^{-1}\), and \(\pi^5x^{-1}\).
4. Write all three blowup charts for \(h=2\), including the overlap transition between the exceptional \(u\) and \(v\) coordinates. Explain why the exceptional fibre is one projective line rather than two intersecting projective lines.
5. Perform the resolution for \(h=7\). List the successive unresolved thicknesses, the number of rounds, the number of exceptional components and the final number of nodes between the old branches. Locate the two outer regular charts in the first round.
6. In the first central chart for \(h=4\), compare the actual equation with \(\pi^2(ab-\pi^2)=0\). Exhibit the unwanted vertical component of the latter chart, and explain the required saturation. Then compute the special fibre of the blowup of a regular thickness-one node.
7. A connected graph has two vertices and three edges, all oriented from the first vertex to the second. Its component genera are \(1\) and \(2\), and its edge thicknesses are \(1,2,3\). Compute the resolved graph's vertex and edge counts, \(b,r,g\), the cycle basis \(f_1=(1,0,-1)\), \(f_2=(0,1,-1)\), and the matrix and Smith invariants of \(Q\).
8. Repeat the graph and matrix calculations in part 7 after ramification of index two, resolving the new nodes. Compute the order and invariant factors of the matrix cokernel. Explain why this is not yet a computation of a geometric component group.
9. A supplied involution exchanges \(x\) and \(y\) in a thickness-five node. Give its maps on the three first-round charts and describe its action on the final four exceptional components. Explain why the global construction respects the involution even when the residue characteristic is two.
10. Under NS7's complete algebraically closed residue-field hypotheses, compute the ranks in (NS15) for the graph of part 7. For \(\ell=3\), assuming \(\operatorname{char}k\ne3\), compute the orders of the special generalized-Jacobian and generic-Jacobian \(9\)-torsion groups over algebraic closures. State precisely which model-existence and period assertions these rank calculations do not establish.

**Full solution.**

1. The contracted ideal is
   \[
   (X_0X_1-\pi^4X_2^2).
   \tag{NSX1}
   \]
   On monomials reduce every product containing both \(X_0\) and \(X_1\) by their displayed relation. The remaining monomials are independent after passage to \(K\), as is seen by substituting \(X_1=\pi^4X_2^2/X_0\) in the Laurent ring \(K[X_0,X_0^{-1},X_2]\): a fixed pair of Laurent exponents has a unique reduced monomial. The quotient is thus torsion-free over \(R\), so no further element enters the contraction. The given coordinates already lie in \(R\) and \(X_2=1\) is a unit; their equation is \(\pi\pi^3=\pi^4\). The special fibre is \(X_0X_1=0\), two projective lines, meeting at the stated point. On \(X_2=1\) its model equation is \(xy=\pi^4\), so the thickness is \(4\). The section specializes to the node; it is not an example of a section in the smooth locus required for NS6's automatic lift statement.
2. Its generic ideal is \((t)\), whose contraction is still \((t)\). In the proposed larger scheme the nonzero class of \(t\) is killed by \(\pi\), so the ring is not torsion-free. The true closure is \(\operatorname{Spec}R\). For any torsion-free module take the directed collection of finitely generated submodules. Each is free by the DVR module theorem. Tensor products and relations use finitely many elements, so tensoring an injection remains injective in their directed limit, exactly as in NS1. This proves the required flatness.
3. Reduction gives
   \[
   x^4y^2+x^2y^3=\pi^{10}x^2+\pi^{10}y.
   \tag{NSX2}
   \]
   The coefficient condition is \(v(c_i)\ge\max(0,-5i)\). Thus the three proposed elements are respectively outside, outside, and inside; the last is exactly \(y\). Coefficient cancellation is already accounted for by writing the Laurent polynomial uniquely before testing.
4. The charts are
   \[
   R[a,a^{-1}],\qquad R[x,u]/(xu-\pi),\qquad
   R[y,v]/(yv-\pi).
   \tag{NSX3}
   \]
   Their exceptional coordinates satisfy \(u=a^{-1}\), \(v=a\), hence \(uv=1\) on the overlap. The central exceptional chart is \(\mathbf G_{m,k}\), not a pair of axes: its equation is \(ab=1\). Gluing its two ends to the exceptional affine lines gives one \(\mathbf P^1_k\), with the old branches meeting its two distinct endpoints.
5. The unresolved thicknesses are
   \[
   7\longmapsto5\longmapsto3\longmapsto1.
   \tag{NSX4}
   \]
   There are three rounds, six exceptional components, and seven thickness-one nodes. The first outer charts are \(R[x,u]/(xu-\pi)\) with \(y=\pi^6u\), and \(R[y,v]/(yv-\pi)\) with \(x=\pi^6v\). They are already regular. Only the central thickness-five point is blown up in the next round.
6. The actual central equation is \(ab-\pi^2=0\). In the unsaturated quotient the nonzero class of \(ab-\pi^2\) is killed by \(\pi^2\); it is nonzero, for example because mapping \(\pi\) to zero sends it to \(ab\ne0\) in \(k[a,b]\). The whole special fibre of that quotient is the affine plane \(k[a,b]\), instead of the required axes \(k[a,b]/(ab)\). This is an unwanted vertical component. Saturation by powers of \(\pi\) removes it and is forced by the field-subring definition of the blowup chart. For the thickness-one blowup the special fibre is
   \[
   k[x,t]/(x^2t).
   \tag{NSX5}
   \]
   Its element \(xt\) is nonzero but has square zero, and the exceptional component \(x=0\) has multiplicity two. This verifies the stopping rule.
7. The graph has \(6\) edges and \(2+(0+1+2)=5\) vertices. Thus \(r=6-5+1=2\), \(b=3\), and \(g=5\). A cycle \((z_1,z_2,z_3)\) satisfies \(z_1+z_2+z_3=0\), so it is uniquely \(z_1f_1+z_2f_2\), integrally. Repeating its coefficients on the paths gives
   \[
   [Q]_{f_1,f_2}=
      \begin{pmatrix}4&3\\3&5\end{pmatrix},
   \qquad \det Q=11,\qquad
      \operatorname{Smith}(Q)=(1,11).
   \tag{NSX6}
   \]
   The entries have greatest common divisor \(1\); PC0's integer row and column operations therefore give first invariant \(1\), and their product is the determinant \(11\). The added projective lines have genus zero, so they do not change \(b\).
8. The new path lengths are \(2,4,6\). There are \(12\) edges and \(2+(1+3+5)=11\) vertices, again \(r=2\), \(b=3\), \(g=5\). The matrix is
   \[
   \begin{pmatrix}8&6\\6&10\end{pmatrix},\qquad
   \det=44,\qquad
   \operatorname{Smith}=(2,22),\qquad
   \operatorname{coker}\simeq\mathbf Z/2\oplus\mathbf Z/22.
   \tag{NSX7}
   \]
   Its entry gcd is \(2\), and determinant divided by \(2\) is \(22\). These are the cokernel invariants of a specifically computed integral form. Identification with the component group of a geometric model would require a proved geometric pairing and comparison; the matrix computation does not supply them.
9. The central chart \(ab=\pi^3\) has \(a\leftrightarrow b\). The \(x\)-chart maps to the \(y\)-chart by \(x\leftrightarrow y\) and \(u\leftrightarrow v\). These maps respect the overlap ratios in NS4, square to the identity, and exchange the two newly inserted end components. Repeating at the central thickness-three point gives the final reversal
   \[
   (E_1,E_2,E_3,E_4)\longmapsto(E_4,E_3,E_2,E_1).
   \tag{NSX8}
   \]
   The construction uses the invariant centre ideal and uniqueness of the lift, with no division by two or averaging. It therefore works in residue characteristic two as well.
10. The actual special-fibre Tate rank is \(2b+r=8\), the generic Jacobian Tate rank is \(2g=10\), and its saturated free quotient has rank \(2\). Over algebraic closures the prime-to-characteristic torsion orders are
   \[
   |G_{\widetilde C}[9]|=9^8,\qquad
   |J_C[9]|=9^{10}.
   \tag{NSX9}
   \]
   Here the question presupposes residue characteristic different from \(3\). These follow from NC7 and CU9; the quotient of the two orders is \(9^2=81\). They do not construct nodal charts after finite extension for an arbitrary initial curve, extend an unsupplied generic action to a model, construct the whole integral semiabelian group or the analytic period covering, or identify the length form with monodromy. They do give NA8's actual saturated generic submodule once the stated model hypotheses hold.

**Theorem 2.4 (full local abelian compatibility; remaining geometric proof obligation).** For every abelian variety over a nonarchimedean local field of characteristic zero, its prime-to-residue-characteristic rational Tate modules have a common Galois-invariant Frobenius-semisimple Weil–Deligne class over \(\overline{\mathbf Q}\).

The potentially good comparison is Lemma 2.3, with the good-model and torsion proofs GQ1–GQ5. For supplied integral period data, PM1–PM8 give the full inertia matrix, ramification normalization, finite equivariance, Frobenius-semisimple blocks and actual examples. From a genuine local-field period presentation, PC0–PC8 give the integral period lattice, nondegenerate rational valuation pairing, all torsion levels and transitions, compactness and supplied-map functoriality. FF1–FF8 prove all-integer finite flat multiplication, canonical subgroup closures and extension for finite étale models; FQ1–FQ6 and IS1–IS8 construct finite flat quotients, the full integral torus-by-abelian quotient sequence, good reduction under isogeny and transfer of genuine period presentations through arbitrary isogenies. DR1–DR8 construct divisor parameter schemes, full collision algebras and finite flat ordered and addition maps. JC1–JC9 construct pointed curve Picard components and Jacobians over arbitrary fields, their universal rigidified line bundles, full nonreduced families, field descent, high-degree projective-bundle Abel maps and tangent differentials. AL1–AL8 in §2L gives the Albanese property on full parameter schemes,finite-curve norm and pullback maps,their degree and composition identities,and the infinitesimal trace. CD1–CD8 in §2M constructs one smooth projective geometrically integral marked curve after a finite separable extension and a smooth surjective map from its Jacobian, with its full kernel and rational Tate sequence. NL1–NL8 in §2N constructs a curve test for the full normalized translation-line family, its finite ample kernel and a finite flat isogeny onto an abelian subvariety of a curve Jacobian, with descended line and saturated Tate image. NR1–NR8 in §2O proves the coherent degree-one dimension,constructs abelian complements over the original field and makes the dominating curve Jacobian an isogeny product with a factor isogenous to the given abelian variety,with full kernel degrees and rational Tate projectors. NC1–NC8 in §2P constructs split nodal curves and their full-family generalized Jacobians,with cycle-character torus,component-Jacobian quotient,normalization cohomology,full multiplication kernels,Tate sequence and finite actions. NQ1–NQ8 in §2Q constructs the identity formal Picard group of a supplied proper flat nodal family,with every square-zero line lift,unique formal coordinates,prime-to-characteristic torsion lifting and supplied family actions. This does not lift the entire semiabelian special group or construct a model or period covering. NA1–NA8 in §2R proves finite locally free and line algebraization on a supplied flat projective model over a complete local base,and constructs a saturated special-fibre Tate submodule of the actual generic Jacobian when the model is normal and integral. Model existence,the whole semiabelian lift and the initial period covering remain to be constructed. NS1–NS8 in §2S constructs a flat projective closure of an embedded generic curve and resolves supplied algebraic nodal charts by intrinsic point blowups,with exceptional chains,supplied actions,cycle lattices and ramification. Producing nodal charts after finite extension for an arbitrary curve remains a separate proof obligation. A curve acquires a rational point after a finite separable extension. For an arbitrary abelian variety, the remaining geometric work includes the semistable curve and formal/analytic constructions producing the initial integral extension and genuinely locally covering period maps, with finite point-lifting, kernel and compatible finite-action properties. Identification with a separately constructed dual-model pairing requires its own duality argument. Deligne’s freely accessible Example 8.10, printed p.571, states the full theorem without proving it and does not discharge these constructions. The theorem is retained in full generality; its full proof is not claimed complete.

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

Lemma 2.2 gives the common characteristic-polynomial argument for every abelian-variety endomorphism. CE1–CE7 in §2B proves the coherent Euler polynomial,proper pushforward and image bound,reduced-base see-saw,and finite commutative torsor Euler comparison. EH6–EH7 in §2C proves all-field Euler homogeneity and ample positivity. CU1–CU12 in §2D proves rigidity,the normalized cube,projectivity and symmetric ample existence over every field,all multiplication degrees,compatible Tate rank,and the full isogeny/nonisogeny integral determinant comparison. These local proofs supply the field-geometric inputs of the interpolation argument;recursive proof-origin checks and independent full-lesson review remain required. Lemma 2.3 proves strict local compatibility for potentially good abelian varieties of every dimension, using the good-model extension, finite étale lifting and semilinear proofs GQ1–GQ5 in §2A. For elliptic curves, potentially multiplicative descent and the proved Tate curve complete the local comparison. PM1–PM7 calculate the full monodromy and finite descent action from supplied period data, and PM8 gives the stated actual examples. PC1–PC8 prove compactness, the full lattice criterion, period valuation nondegeneracy, actual torsion comparison, integral and finite inertia invariants, finite descent obstruction and functoriality for a genuine local-field period presentation. The full arbitrary-abelian-variety theorem, Theorem 2.4, still requires construction of that presentation and its covering and finite point-lifting properties, compatible integral model actions, and any claimed dual-model pairing identification. These general geometric constructions are not supplied by the abstract module or point-topological calculations. No assertion at \(\ell=p(v)\) is part of strict compatibility here.

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
