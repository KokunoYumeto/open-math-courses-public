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

**Theorem 2.4 (full local abelian compatibility; remaining geometric proof obligation).** For every abelian variety over a nonarchimedean local field of characteristic zero, its prime-to-residue-characteristic rational Tate modules have a common Galois-invariant Frobenius-semisimple Weil–Deligne class over \(\overline{\mathbf Q}\).

The potentially good comparison is Lemma 2.3, with the good-model and torsion proofs GQ1–GQ5. PM1–PM7 in §2E prove the entire inertia matrix, ramification normalization, finite equivariance and Frobenius-semisimple blocks for supplied integral period data; PM8 gives the stated actual examples. PC1–PC6 in §2F prove that a genuine local-field period presentation gives a nondegenerate rational period valuation pairing and every actual torsion level, transition and action. For an arbitrary abelian variety one must still construct the semiabelian integral extension and locally covering period maps after finite extension, prove their finite point-lifting and kernel properties, and supply the compatible finite model actions. Identification with a separately constructed dual-model pairing requires its own duality argument. Deligne’s freely accessible Example 8.10, printed p.571, states the full theorem without proving it; it does not discharge these constructions. The theorem is retained in full generality, and this draft does not claim its full proof complete.

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
