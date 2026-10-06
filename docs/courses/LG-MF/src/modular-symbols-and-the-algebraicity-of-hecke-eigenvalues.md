# Modular symbols and the algebraicity of Hecke eigenvalues

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The periods of a cusp form lie in a cohomology space defined by integer matrices. Reflection will give us a lattice of the same dimension as the holomorphic cusp space. Hecke operators preserve it, so their eigenvalues are algebraic integers. The Fourier-coefficient pairing then provides a rational structure on cusp forms.

In weight two, finite symbols describe paths on the modular curve. We will prove the completeness of their relations and their pairing with cusp forms, then compute the newforms at levels \(11,23,37\).

Throughout, \(k\ge2\), \(m=k-2\), \(q=e^{2\pi iz}\), and \(S=S_k(\Gamma_1(N))\), unless another group is specified. We keep the polynomial action of Group cohomology and the Eichler–Shimura isomorphism:
\[
\rho(\gamma)P(v)=P(\gamma^{-1}v),\qquad v=\binom XY.
\tag{0.1}
\]
A coboundary is \((\rho(\gamma)-1)b\). For \(\delta=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) of positive determinant, our slash normalization is
\[
(f|_k\delta)(z)=\det(\delta)^{k-1}(cz+d)^{-k}f(\delta z).
\tag{0.2}
\]
This is the normalization of Hecke operators for \(\Gamma_0\) and \(\Gamma_1\). All \(T_n\), including \(U_p=T_p\) for \(p\mid N\), are included below.

## 1. Double cosets on cocycles

Let \(\Gamma\) have finite index and let \(\Delta\) be a finite union of left \(\Gamma\)-cosets of integral matrices with positive determinant, stable under right multiplication by \(\Gamma\). Choose representatives \(\delta_i\) and write
\[
\delta_i\gamma=h_i(\gamma)\delta_{\sigma_\gamma(i)},\qquad h_i(\gamma)\in\Gamma.
\tag{1.1}
\]
Define
\[
A_\delta P(v)=P(\delta v).
\tag{1.2}
\]
This integral coefficient operator satisfies \(A_{\delta\eta}=A_\eta A_\delta\); for determinant one, \(A_\gamma=\rho(\gamma^{-1})\).

**Proposition 1.1.** For a cocycle \(c\), the formula
\[
(T_\Delta c)(\gamma)=\sum_iA_{\delta_i}c(h_i(\gamma))
\tag{1.3}
\]
defines an integral cocycle, sends coboundaries to coboundaries, and induces an operator on cohomology independent of the representatives.

**Proof.** Identity (1.1) implies
\[
A_{\delta_i}\rho(h_i(\gamma))
=\rho(\gamma)A_{\delta_{\sigma_\gamma(i)}}.
\tag{1.4}
\]
Also \(h_i(\gamma\eta)=h_i(\gamma)h_{\sigma_\gamma(i)}(\eta)\). Apply the cocycle rule, use (1.4), and reindex the second sum. This gives
\(T_\Delta c(\gamma\eta)=T_\Delta c(\gamma)+\rho(\gamma)T_\Delta c(\eta)\).
If \(c(\gamma)=(\rho(\gamma)-1)b\), the same calculation gives the coboundary with primitive \(\sum_iA_{\delta_i}b\).

Replace \(\delta_i\) by \(u_i\delta_i\), with \(u_i\in\Gamma\), after reindexing. Then
\(h'_i=u_i h_i u_{\sigma(i)}^{-1}\) and
\(A_{\delta'_i}=A_{\delta_i}\rho(u_i^{-1})\).
Expanding the three-factor cocycle value shows that the new sum minus the old one is \(b-\rho(\gamma)b\), where
\[
b=\sum_iA_{\delta_i}\rho(u_i^{-1})c(u_i).
\]
Thus it is a coboundary. The coefficient operators have integer entries in the monomial basis, proving the integral assertion. \(\square\)

For \(T_n\) on \(\Gamma_1(N)\) take
\[
\Delta_n=\left\{\delta\in\operatorname{Mat}_2(\mathbb Z):
\det\delta=n,\quad
\delta\equiv\begin{pmatrix}1&*\\0&n\end{pmatrix}\pmod N\right\}.
\tag{1.5}
\]
Its cosets have representatives
\[
\sigma_a\begin{pmatrix}a&b\\0&n/a\end{pmatrix},
\quad a\mid n,\ (a,N)=1,\quad 0\le b<n/a,\qquad
\sigma_a\equiv\begin{pmatrix}a^{-1}&0\\0&a\end{pmatrix}\pmod N.
\tag{1.6}
\]
Here is the proof for all indices. Apply the Euclidean algorithm to the first column of \(\delta\in\Delta_n\), using determinant-one row operations. It gives \(g\delta=\begin{pmatrix}a&b\\0&d\end{pmatrix}\), with \(a,d>0\), \(ad=n\), and \(0\le b<d\) after adding a multiple of the second row. The first column of \(\delta\) is \((1,0)^t\pmod N\), so \(a\) is a unit modulo \(N\), and \(g\)'s first column is \((a,0)^t\pmod N\). Thus \(\sigma_ag\in\Gamma_1(N)\), proving existence of (1.6). A lift \(\sigma_a\) exists by reduction surjectivity from the second lesson. Two such representatives in the same \(\Gamma_1(N)\)-coset are also in the same \(\mathrm{SL}_2(\mathbb Z)\)-coset; the gcd of the first column first forces \(a\) to agree and then \(d=n/a\). A determinant-one matrix carrying \((a,0)^t\) to itself is \(\left(\begin{smallmatrix}1&t\\0&1\end{smallmatrix}\right)\), so the two upper-right entries differ by \(td\). Their chosen range makes them equal. It follows also directly from the congruences that every listed representative belongs to \(\Delta_n\).

On a character space, \(f|_k\sigma_a=\chi(a)f\). Summing the \(d\) translations in (1.6) kills Fourier indices not divisible by \(d\), and its remaining factor is \(n^{k-1}d^{1-k}=a^{k-1}\). Its coefficient at \(q^r\), when \(a\mid r\), is \(\chi(a)a^{k-1}a_{nr/a^2}(f)\). Summing over \(a\mid\gcd(n,r)\) gives exactly the ninth lesson's Theorem 3.1. Hence the coset sum is our \(T_n\) at every index.

Diamonds use a single coset represented by a determinant-one matrix in \(\Gamma_0(N)\) with lower-right residue \(d\). These sets satisfy the hypotheses above.

### 1.1. Change of variables and equivariance

Put \(I_f(u,v)=\int_u^v f(z)(X-zY)^m\,dz\). Cusp convergence and covariance were proved in the fifteenth lesson, Theorem 3.1. If \(\det\delta=n>0\), direct substitution gives
\[
A_\delta(X-\delta zY)^m
=\left(\frac n{cz+d}\right)^m(X-zY)^m,\qquad
d(\delta z)=\frac n{(cz+d)^2}\,dz.
\]
Consequently
\[
I_{f|_k\delta}(u,v)=A_\delta I_f(\delta u,\delta v).
\tag{1.7}
\]
The same calculation applies to
\(\overline{g(z)}(X-\bar zY)^m\,d\bar z\).

Use an interior base point \(z_0\) and put \(v_i=I_f(z_0,\delta_i z_0)\). Concatenation and covariance give
\[
I_f(\delta_i z_0,h_i\delta_{\sigma(i)}z_0)
=c_f(h_i)+\rho(h_i)v_{\sigma(i)}-v_i.
\]
Sum (1.7) and use (1.4) to obtain
\[
c_{T_\Delta f}(\gamma)
=T_\Delta c_f(\gamma)
+(\rho(\gamma)-1)\sum_iA_{\delta_i}v_i.
\tag{1.8}
\]
The two sides differ by a coboundary. This proves the required Hecke equivariance for \(T_n\) and diamonds, including the determinant factor.

### 1.2. Finite-index descent

For \(H\subset\Gamma\) of finite index \(D\), choose left \(H\)-coset representatives \(\delta_i\in\Gamma\). Formula (1.3), with the \(h_i\) in \(H\), sends an \(H\)-cocycle to a \(\Gamma\)-cocycle. This is corestriction; restriction just restricts a cocycle.

The proof of Proposition 1.1 applies. If \(c\) was a \(\Gamma\)-cocycle, expand \(c(\delta_i\gamma)\) in the two ways supplied by (1.1). It follows that
\[
\operatorname{cores}\operatorname{res}[c]=D[c].
\tag{1.9}
\]
The difference of cocycles is the coboundary with primitive
\(-\sum_i\rho(\delta_i^{-1})c(\delta_i)\).
For a normal \(H\), these conjugations give an action on cohomology independent of the representative: an inner conjugation by \(u\in H\) changes \(c(\gamma)\) by
\((1-\rho(\gamma))\rho(u^{-1})c(u)\), a coboundary. The same calculation with a \(\Gamma\)-cocycle shows that its restricted class is invariant. Restriction of corestriction then gives
\[
\operatorname{res}\operatorname{cores}[c]
=\sum_i\left[\gamma\longmapsto
\rho(\delta_i^{-1})c(\delta_i\gamma\delta_i^{-1})\right].
\tag{1.10}
\]
Thus, over characteristic zero, restriction is injective and its image is exactly the invariant subspace: for an invariant class (1.10) is \(D[c]\), and division by \(D\) supplies its preimage.

This also holds for parabolic classes. Restriction preserves parabolicity. Conversely \(H\cap\Gamma_P\) has finite index in each cusp stabilizer. Applying (1.9) to those two groups proves that a cusp restriction zero on \(H\cap\Gamma_P\) is already zero on \(\Gamma_P\). Hence parabolicity descends too.

## 2. An integral lattice of holomorphic dimension

### 2.1. Eichler–Shimura in all the weights used here

The fifteenth lesson gives a local injectivity proof and a surjectivity argument using the sixth lesson's Riemann–Roch dimension formula. The compact-curve proof is now written in lesson 06, Appendix A; its explicit elementary analytic foundations remain dependencies of that isomorphism and the argument here. To cover the remaining odd weights on \(\Gamma_1(N)\), choose a multiple \(M\) of \(N\), with \(M\ge5\), and let \(H=\Gamma(M)\). This normal subgroup has no elliptic stabilizers and does not contain \(-I\). All its cusps are regular: a negative unipotent has trace \(-2\), while a matrix congruent to \(I\pmod M\) has trace \(2\pmod M\); these residues differ when \(M\ge5\).

Let its genus and cusp count be \(g,c\), and let \(\mu_H\) be its projective index. Its surface presentation is the fifteenth lesson's (4.1) without elliptic generators, lifted to the actual group. Proposition 4.1 there applies to every self-dual coefficient module, including odd polynomial degree. For \(m>0\), the upper and lower translation fixed lines intersect in zero, while each regular cusp has one invariant. Therefore
\[
\dim H^1_{\rm par}(H,V_m(\mathbb C))
=(2g+c-2)(k-1)-c
=2(k-1)(g-1)+(k-2)c.
\tag{2.1}
\]
In weight two the global invariant dimension is one and the answer is \(2g\).

The regular-cusp dimension proof of the sixth lesson, Solution 4, applies to \(H\) as well: the periodic cusp frames of the weight-one bundle \(\mathcal L\) give
\(\mathcal L^2=\mathcal K(C)\), where \(C\) is the cusp divisor. Thus
\[
\deg\mathcal L=g-1+c/2=\mu_H/12>0,\qquad
S_k(H)=H^0(X(H),\mathcal L^k(-C)).
\]
Riemann–Roch's dual correction is \(\mathcal L^{2-k}\), of negative degree for \(k\ge3\). Hence
\[
\dim S_k(H)=(k-1)(g-1)+(k/2-1)c.
\tag{2.2}
\]
The compact-support cup proof and positivity in the fifteenth lesson, Lemma 5.1 and Proposition 5.2, require covariance, self-duality and cusp decay. They impose no even-degree restriction on this free quotient. They therefore prove injectivity of its period map in odd weight too. Equations (2.1)–(2.2) prove surjectivity.

Taking \(\Gamma_1(N)/H\)-invariants and using (1.9)–(1.10) now gives
\[
S_k(\Gamma_1(N))\oplus\overline{S_k(\Gamma_1(N))}
\xrightarrow{\ \sim\ }
H^1_{\rm par}(\Gamma_1(N),V_m(\mathbb C)).
\tag{2.3}
\]
The invariant condition on forms is exactly the slash law for the larger group; the finite covering preserves the cusp condition in both directions. Formula (1.7), for a single normalizing determinant-one matrix, identifies its action with conjugation on periods. If \(-I\) acts in odd degree, both invariant spaces are zero, as required.

Together with (1.8), (2.3) is Hecke-equivariant for every \(k\ge2\). It also proves that the rational cohomological Hecke operators preserve the parabolic subspace, since after complexification their images are cusp-form periods.

An irregular cusp must not be counted as regular in (2.1). In odd degree a negative unipotent has no invariant and contributes zero. Passing to \(H\) ensures that only regular cusps enter our calculation.

### 2.2. Integral cohomology and reflection

Put \(V_{\mathbb Z}=\mathbb Z[X,Y]_m\). A finite coset-transition argument for the generators \(S,T\) gives finitely many generators for \(\Gamma=\Gamma_1(N)\). Evaluation on them embeds its integral cocycles into \(V_{\mathbb Z}^r\). The relations are integer linear equations, so the cocycle module, the coboundary module and their quotient are finitely generated abelian groups.

Scalar extension can be checked directly. The rows of all relation equations span a finite-dimensional rational row space. Finitely many rows therefore define the same kernel over \(\mathbb Q\) and \(\mathbb C\). Clearing denominators of a rational solution gives an integral cocycle. The coboundary map is an integer matrix as well. Its quotient consequently satisfies
\[
\bigl(H^1(\Gamma,V_{\mathbb Z})/\mathrm{torsion}\bigr)\otimes\mathbb Q
=H^1(\Gamma,V_m(\mathbb Q)).
\]
Further extension gives complex cohomology. The finitely many cusp restriction maps are linear, so their kernels commute with these field extensions too.

Let \(L_0\) be the image of the torsion-free integral cohomology in rational cohomology, and define
\[
L=L_0\cap H^1_{\rm par}(\Gamma,V_m(\mathbb Q)).
\tag{2.4}
\]
It is a full lattice in the rational parabolic subspace: clear denominators of a rational basis expressed in a basis of \(L_0\). Proposition 1.1 and parabolic preservation show that every \(T_n\) and diamond preserves \(L\). Torsion has been discarded before using this lattice.

The matrix \(\varepsilon=\operatorname{diag}(-1,1)\) normalizes \(\Gamma_1(N)\). Define
\[
(Jc)(\gamma)=A_\varepsilon c(\varepsilon\gamma\varepsilon).
\tag{2.5}
\]
It is an integral involution on cohomology, preserves cusp restrictions and \(L\), and commutes with all \(T_n\) and diamonds. Indeed
\(A_\varepsilon\rho(\varepsilon\gamma\varepsilon)=\rho(\gamma)A_\varepsilon\)
proves the cocycle and coboundary assertions. Reflection preserves the matrix set (1.5), and preserves a diamond coset's lower-right residue. Apply (1.3) to the conjugated representatives to prove commutation.

Define
\[
f^\#(z)=\overline{f(-\bar z)}.
\tag{2.6}
\]
Reflection conjugates the modular matrix to \(\varepsilon\gamma\varepsilon\); conjugating its automorphy factor gives \((cz+d)^k\). Reflecting a cusp scaling similarly preserves the cusp vanishing condition. Thus \(f^\#\in S\), with coefficients \(\overline{a_n(f)}\).

Use base point \(i\), fixed by \(z\mapsto-\bar z\). Substitution \(z=-\bar w\) in the period integral gives \(dz=-d\bar w\), while \(A_\varepsilon\) multiplies the polynomial by \((-1)^m\). Therefore
\[
J[c_f]=(-1)^{k-1}[c_{\overline{f^\#}}].
\tag{2.7}
\]
It exchanges the two summands of (2.3). The maps
\[
f\longmapsto[c_f]\pm J[c_f]
\tag{2.8}
\]
are complex-linear Hecke-equivariant isomorphisms from \(S\) onto the two eigenspaces of \(J\). They are injective because their holomorphic component is \([c_f]\); an eigenvector's antiholomorphic component is determined by that component, which also proves surjectivity.

The groups \(L^\pm=L\cap\ker(J\mp1)\) are full lattices in these eigenspaces. The projections \((1\pm J)/2\) are rational, and multiplying projected lattice generators by two verifies fullness.

**Theorem 2.1 (integrality).** The characteristic polynomial of every \(T_n\) on \(S_k(\Gamma_1(N))\) lies in \(\mathbb Z[X]\). Every eigenvalue, including a bad-prime eigenvalue, is an algebraic integer.

**Proof.** Each \(T_n\) is an integer matrix in a basis of \(L^+\). By (2.8) its characteristic polynomial is exactly that of \(T_n\) on \(S\). The polynomial is monic and integral and annihilates every eigenvalue. \(\square\)

Reflection is what identifies the individual holomorphic characteristic polynomial. The lattice on the full space (2.3) alone would concern both summands together.

## 3. Fourier coefficients and Galois conjugation

Let \(\mathbb T_{\mathbb Z}\) be the algebra generated by all \(T_n\) and diamonds in \(\operatorname{End}_{\mathbb C}(S)\). Its action on \(L^+\) is faithful, so it embeds in \(\operatorname{End}_{\mathbb Z}(L^+)\). It is therefore free of finite rank. The elementary fact used here is that a subgroup of \(\mathbb Z^r\) is finitely generated: project onto the first coordinate, choose a preimage of a generator of the resulting ideal, and induct on the kernel. Put
\[
\mathbb T_{\mathbb Q}=\mathbb T_{\mathbb Z}\otimes\mathbb Q,\qquad
\mathbb T_{\mathbb C}=\mathbb T_{\mathbb Q}\otimes\mathbb C.
\]

**Theorem 3.1 (the perfect Fourier pairing).** The pairing
\[
\mathbb T_{\mathbb C}\times S\longrightarrow\mathbb C,\qquad
(T,f)\longmapsto a_1(Tf)
\tag{3.1}
\]
is perfect. In particular \(\dim\mathbb T_{\mathbb Q}=\dim_{\mathbb C}S\).

**Proof.** The ninth lesson's coefficient formula gives
\[
a_1(T_nf)=a_n(f)\qquad(n\ge1).
\tag{3.2}
\]
A form pairing to zero with every operator has every coefficient zero, hence is zero. Conversely, suppose \(a_1(Tf)=0\) for every \(f\). Commutativity gives
\[
a_n(Tf)=a_1(T_nTf)=a_1(TT_nf)=0
\]
for every \(n,f\). Thus \(Tf=0\) for every \(f\), and \(T=0\) because these are actual endomorphisms. Nondegeneracy on both sides of a finite-dimensional pairing implies equality of dimensions and perfectness. Rational matrices on \(L^+\) have the same linear rank over \(\mathbb Q\) and \(\mathbb C\), proving the final assertion. \(\square\)

Define the coefficient span
\[
A=\sum_{n\ge1}\mathbb ZT_n\subset\mathbb T_{\mathbb Z}.
\tag{3.3}
\]
It is finite free. It spans \(\mathbb T_{\mathbb Q}\): its complex span has zero annihilator in \(S\), by (3.2), so perfectness forces that span to be all of \(\mathbb T_{\mathbb C}\). Rational matrix rank gives the assertion over \(\mathbb Q\).

**Theorem 3.2 (an integral Fourier basis).** The group
\[
S(\mathbb Z)=\{f\in S:a_n(f)\in\mathbb Z\text{ for every }n\ge1\}
\]
is a full lattice, and \(S\) has a complex basis of forms in \(S(\mathbb Z)\).

**Proof.** Extend a functional on \(A\) complex-linearly to \(\mathbb T_{\mathbb C}\). Theorem 3.1 supplies a unique analytic cusp form, whose coefficients are \(\phi(T_n)\). Hence the exact identification is
\[
S(\mathbb Z)=\operatorname{Hom}_{\mathbb Z}(A,\mathbb Z).
\tag{3.4}
\]
The dual of a \(\mathbb Z\)-basis of \(A\) supplies forms with integer coefficients. They are a complex basis because \(A\otimes\mathbb C=\mathbb T_{\mathbb C}\). \(\square\)

Similarly,
\[
S(\mathbb Q)=\{f\in S:a_n(f)\in\mathbb Q\ \forall n\}
=\operatorname{Hom}_{\mathbb Q}(\mathbb T_{\mathbb Q},\mathbb Q),
\qquad S=S(\mathbb Q)\otimes\mathbb C.
\tag{3.5}
\]
A finite set of \(T_n\) is a rational basis, so rational values on all \(T_n\) give a rational functional. The full algebra acts rationally by
\((T\phi)(U)=\phi(UT)\).

We can strengthen (3.4) to a perfect pairing with the full integral algebra. The additional ingredient concerns the diamonds, whose integrality does not follow merely from the perfect complex pairing.

**Outstanding arithmetic proof (a model with the required properties).** For \(N>4\), the stronger integral-duality argument below is conditional on constructing a model \(X=\mathcal X_\mu(N)\) for the moduli problem defined by an embedding of \(\mu_N\) into a generalized elliptic curve, with precisely the following properties: \(X\) is a separated curve of finite type, smooth over \(\mathbb Z\), with geometrically irreducible fibers, and its generic fiber is proper. Properness over \(\mathbb Z\) is not a hypothesis. The construction and these properties, particularly at primes dividing \(N\), are not proved in this lesson or in the earlier programme proofs checked here. They must therefore remain a required proof task rather than an available theorem.

The further hypotheses are a cuspidal line bundle \(\mathcal F=\omega^{\otimes(k-2)}\otimes\Omega^1_{X/\mathbb Z}\), included in \(\omega^{\otimes k}\), whose complex global sections identify with our analytic cusp forms; a section \(s_\infty:\operatorname{Spec}\mathbb Z\to X\) with formal neighborhood \(\operatorname{Spf}\mathbb Z[[q]]\); and a canonical differential trivializing the completed weight sheaf so that cuspidal expansions lie in \(q\mathbb Z[[q]]\), compatibly with passage to fields. Finally, changing the embedding \(i:\mu_N\hookrightarrow E\) to \(a i\) must define an automorphism over \(\mathbb Z\) preserving \(\mathcal F\) and inducing the analytic diamond \(\langle a\rangle\).

The free original Deligne–Rapoport paper, Chapters IV–VII, develops algebraic level structures, reduction and formal cusp comparisons. Katz's author-distributed paper, §1.6, proves a q-expansion principle after inverting the principal level. That inverted-level statement alone does not establish the hypotheses above at bad primes, and we do not use it as a replacement for them. The following lemma proves the integer-coefficient consequence from the listed hypotheses; it does not construct the model.

**Lemma (integrality detected at infinity).** Under these model properties,
\[
H^0(X,\mathcal F)=S(\mathbb Z)
\]
inside \(S\), by the analytic comparison and q-expansion map.

**Proof.** First consider a field \(K\) equal to \(\mathbb Q\) or \(\mathbb F_p\). Smoothness and geometric irreducibility make \(X_K\) integral. A section with zero q-expansion has zero germ at \(s_\infty\): the local ring there is a discrete valuation ring, and its map to its power-series completion is injective, since a nonzero element has finite valuation. Trivialize the line bundle there to apply this observation. The section then vanishes on an open neighborhood. A section of a line bundle on an integral scheme that vanishes on a nonempty open set vanishes everywhere, by trivialization and injection into the function field. Thus q-expansion is injective on \(H^0(X_K,\mathcal F_K)\), including when \(p\mid N\).

We also need flat change of scalars for global sections. Take a finite affine cover of the separated scheme \(X\). Global sections are the kernel of the two restriction maps from the finite sum of sections on its members to the finite sum on their intersections. The intersections are affine, and sections of a quasi-coherent sheaf on an affine scheme commute with scalar extension. Flat tensoring preserves this kernel. Consequently
\[
H^0(X,\mathcal F)\otimes\mathbb Q=H^0(X_{\mathbb Q},\mathcal F_{\mathbb Q}),\qquad
H^0(X_{\mathbb Q},\mathcal F_{\mathbb Q})\otimes\mathbb C=S.
\]
Write \(V=H^0(X_{\mathbb Q},\mathcal F_{\mathbb Q})\). Its dimension \(D\) is finite because \(X_{\mathbb Q}\) is a proper curve. The q-coefficient functionals span \(V^*\): otherwise their common annihilator would contain a nonzero section, contradicting injectivity. Choose \(D\) of them forming a basis of \(V^*\). For a rational basis of \(V\), their matrix has rational entries and nonzero determinant. A form \(f\in S\) with integer q-coefficients therefore has rational coordinates in this basis, by the inverse matrix. Hence \(f\in V\). The zero-dimensional case is immediate.

The first scalar-change identity gives a positive integer \(M\) with \(g=Mf\in H^0(X,\mathcal F)\). If a prime \(p\) divides \(M\), every q-coefficient of \(g\) is divisible by \(p\). Its reduction is a section on \(X_{\mathbb F_p}\) with zero expansion, so is zero by the first paragraph. Since \(X\) is flat over \(\mathbb Z\) and \(\mathcal F\) is invertible, the sheaf sequence
\[
0\longrightarrow\mathcal F\xrightarrow{\ p\ }\mathcal F
\longrightarrow\mathcal F/p\mathcal F\longrightarrow0
\]
is exact. Left exactness of global sections supplies \(h\in H^0(X,\mathcal F)\) with \(g=ph\). Thus \((M/p)f=h\) is integral. Repeating removes every prime factor of \(M\), proving that \(f\) is an integral section. Conversely, an integral section has integer q-coefficients by the canonical formal trivialization. This proves the equality. We used neither properness of \(X\) over \(\mathbb Z\) nor a theorem identifying all modular forms in positive characteristic with reductions of classical forms. \(\square\)

**Proposition 3.2a (full integral Hecke duality, conditional on the model hypotheses above for \(N>4\)).** Every \(T_n\) and diamond preserves \(S(\mathbb Z)\). Moreover,
\[
A=\mathbb T_{\mathbb Z},\qquad
S(\mathbb Z)=\operatorname{Hom}_{\mathbb Z}(\mathbb T_{\mathbb Z},\mathbb Z),
\tag{3.4a}
\]
with pairing \((T,f)\mapsto a_1(Tf)\).

**Proof.** For \(N>4\), apply the preceding lemma to \(f\in S(\mathbb Z)\). Pulling its integral section back by the automorphism above gives another integral cusp section. Its analytic form is \(\langle a\rangle f\), so this form has integer coefficients. This argument uses the integral model, rather than assuming integrality of Fourier expansions at all cusps. For \(N\le4\), every unit class is represented by \(1\) or \(-1\). The corresponding diamonds act by \(1\) or \((-1)^k\), since one can use \(I\) or \(-I\) as representatives. Thus diamond stability holds at every level.

The ninth lesson's all-index coefficient formula now gives, for \(r\ge1\),
\[
a_r(T_nf)=\sum_{\substack{d\mid(n,r)\\(d,N)=1}}
 d^{k-1}a_{nr/d^2}(\langle d\rangle f)\in\mathbb Z.
\tag{3.4b}
\]
It includes indices divisible by \(N\). Hence all generators, and every element of \(\mathbb T_{\mathbb Z}\), preserve \(S(\mathbb Z)\).

Choose a \(\mathbb Z\)-basis \(E_1,\ldots,E_D\) of \(A\), and let \(f_1,\ldots,f_D\) be its dual basis in (3.4). These are also complex bases of \(\mathbb T_{\mathbb C}\) and \(S\). For \(T\in\mathbb T_{\mathbb Z}\), stability shows that each \(a_1(Tf_i)\) is an integer. Perfectness of (3.1) therefore gives
\[
T=\sum_{i=1}^D a_1(Tf_i)E_i\in A.
\tag{3.4c}
\]
Indeed, both sides pair equally with every \(f_j\). The reverse inclusion is the definition of \(A\). Substituting this equality in (3.4) proves the asserted integral perfect pairing. \(\square\)

For any commutative ring \(R\), finite freeness also gives
\[
S(\mathbb Z)\otimes R\simeq
\operatorname{Hom}_{\mathbb Z}(\mathbb T_{\mathbb Z},R).
\tag{3.4d}
\]
In this module the coefficient at \(q^n\) is \(\phi(T_n)\), and \((T\phi)(U)=\phi(UT)\). Its coefficient map is injective because the \(T_n\) span \(\mathbb T_{\mathbb Z}\). This defines the base change of the classical integral lattice; comparison with all geometric modular forms in positive characteristic requires a separate base-change theorem.

### 3.1. A bounded integral Hecke span

The complex coefficient bound gives a rational span of finitely many \(T_n\). To prove that this span is the whole integer lattice, we need the arithmetic bound as well.

**Theorem 3.2b (bounded integral generation, with the arithmetic proof dependencies specified).** In addition to Proposition 3.2a, this argument needs the arithmetic Sturm theorem of the sixth lesson, including its principal-level field structure and bounded-denominator construction. Those geometric prerequisites still require programme proofs. Retaining these dependencies explicitly, put
\[
\begin{aligned}
m&=[\mathrm{SL}_2(\mathbb Z):\Gamma_1(N)],\\
r_c&=\frac{km}{12}-\frac{m-1}{N},\\
B&=\max(0,\lfloor r_c\rfloor),\\
A_B&=\sum_{1\le n\le B}\mathbb ZT_n.
\end{aligned}
\tag{3.4e}
\]
Then \(A_B=\mathbb T_{\mathbb Z}\). Consequently, for every commutative ring \(R\), the coefficient map
\[
\begin{aligned}
S(\mathbb Z)\otimes R&\longrightarrow R^B,\\
f&\longmapsto(a_1(f),\ldots,a_B(f)).
\end{aligned}
\tag{3.4f}
\]
is injective. This refers to the base change of the classical lattice in (3.4d).

**Proof.** Let \(p\) be any prime. The finite free duality in Proposition 3.2a gives a perfect pairing after reduction modulo \(p\). Every element \(\bar f\in S(\mathbb Z)\otimes\mathbb F_p\) has a lift \(f\in S(\mathbb Z)\), by reducing the integer coordinates in a lattice basis. If it annihilates the image of \(A_B\), then
\[
\begin{gathered}
a_n(f)=a_1(T_nf)\equiv0\pmod p,\\
1\le n\le B.
\end{gathered}
\tag{3.4g}
\]
Its constant coefficient is zero because it is cuspidal. We apply the cusp refinement in Theorem 6.2 of the dimension-formulas lesson with its actual period \(N\). To justify that period even at \(N=1,2\), note that every slash transform is a form on \(\Gamma(N)\), since this principal subgroup is normal and contained in \(\Gamma_1(N)\). It is therefore periodic with period \(N\). Its cuspidal expansion has positive exponents in \(N^{-1}\mathbb Z\), so each primitive nonidentity factor in the norm proof starts at exponent at least \(1/N\). The scalar making it primitive does not change its exponents. Acquiring the arithmetic input at a larger principal level \(L\ge3\) divisible by \(N\) preserves this period identity.

If the reduction of \(f\) were nonzero, its first exponent would be at least \(B+1>r_c\), including the case \(r_c<0\). The full norm would then have order greater than
\[
r_c+\frac{m-1}{N}=\frac{km}{12},
\tag{3.4i}
\]
contradicting the full-level arithmetic bound. Thus every coefficient of \(f\) is divisible by \(p\). The analytic form \(f/p\) is still a cusp form with integer coefficients, so \(f\in pS(\mathbb Z)\), or \(\bar f=0\).

A proper subspace of a finite-dimensional vector space has a nonzero linear functional vanishing on it: extend a basis of that subspace to a basis of the vector space and take a complementary coordinate. Perfect duality and the preceding paragraph therefore imply that \(A_B\otimes\mathbb F_p\) maps onto \(\mathbb T_{\mathbb Z}\otimes\mathbb F_p\). Right exactness gives
\[
\begin{gathered}
(\mathbb T_{\mathbb Z}/A_B)\otimes\mathbb F_p=0,\\
\text{for every prime }p.
\end{gathered}
\tag{3.4h}
\]
The quotient is a finitely generated abelian group. Its decomposition into a free part and finite cyclic groups shows that a nonzero quotient has a nonzero tensor product with \(\mathbb F_p\) for some prime: any prime detects a free summand, and a prime divisor detects a torsion summand. Hence the quotient is zero.

Finally, under (3.4d), a functional with its first \(B\) coefficients zero vanishes on \(T_1,\ldots,T_B\). These generate the whole integer module just proved, so it vanishes everywhere, proving (3.4f) for every \(R\). The zero-dimensional and empty-span cases are included. \(\square\)

The proof includes \(p\mid N\) and uses all indices through \(B\), including bad-prime powers and composite indices. Knowing only that \(A_B\) has the same rational rank would leave a possible finite quotient. It is precisely the argument for every prime in (3.4h) that removes that quotient.

For example, at \(k=2,N=11\) the linear index is \(120\), so \(r_c=20-119/11=101/11\) and \(B=9\). The unrefined bound would give twenty. Nine is a sufficient bound for the entire \(\Gamma_1(11)\) cusp space; this example asserts no optimality. At level one the subtraction is zero, so the endpoint used in Solution 5 remains one in weight twelve.

### 3.2. Number fields and arbitrary automorphisms

For a normalized simultaneous eigenform \(f\), the eigencharacter
\(\lambda_f:\mathbb T_{\mathbb Q}\to\mathbb C\) satisfies
\(\lambda_f(T_n)=a_n(f)\).
Its image is a finite-dimensional rational subalgebra of \(\mathbb C\), hence a field: multiplication by a nonzero element is injective on this finite-dimensional domain, so is surjective. The \(T_n\) span the rational algebra, and therefore
\[
K_f=\mathbb Q(a_n(f):n\ge1)=\lambda_f(\mathbb T_{\mathbb Q})
\tag{3.6}
\]
is a number field of degree at most \(\dim S\). Theorem 2.1 makes all its Fourier coefficients algebraic integers.

For \(\sigma\in\operatorname{Aut}(\mathbb C)\), act semilinearly on the scalar factor in (3.5). Equation (3.2) identifies the resulting cusp form with
\[
f^\sigma=\sum_{n\ge1}\sigma(a_n(f))q^n.
\tag{3.7}
\]
It is analytic because the finite-dimensional structure (3.5) supplies a cusp form. We have not applied a possibly discontinuous automorphism to an infinite analytic limit. Rationality of the Hecke matrices proves
\[
T_nf^\sigma=\sigma(a_n(f))f^\sigma.
\tag{3.8}
\]
The diamond character becomes \(\sigma\chi\).

**Theorem 3.3 (newforms and Galois action).** If \(f\) is a normalized newform of weight \(k\) and primitive level \(N\), then \(f^\sigma\) is a normalized newform of the same weight and primitive level \(N\).

**Proof.** Every degeneracy map \(V_d:g(z)\mapsto g(dz)\) sends rational coefficient sequences to rational coefficient sequences. By (3.5) at source and target it is a rational map. Rational bases of the lower-level spaces span its images, so the old space is stable under \(\sigma\) and \(\sigma^{-1}\).

A nonzero newform is not old, by positive Petersson orthogonality. Thus \(f^\sigma\) is not old either. To conclude newness, use the primitive decomposition in Oldforms, newforms and the theory of Atkin–Lehner and Li, Theorem 4.5. Every full good-prime eigenvalue space at level \(N\) is the degeneracy space of one primitive newform of level \(M\mid N\). By (3.8), \(f^\sigma\) belongs to one such space. If \(M<N\), its entire space is old, a contradiction. Hence \(M=N\), and that space is a single new line. Its first coefficient is \(\sigma(1)=1\). This proves normalization and primitive level as well as newness, without assuming that \(\sigma\) preserves an analytic orthogonal complement. \(\square\)

## 4. The complete Manin presentation in weight two

In \(G=\mathrm{PSL}_2(\mathbb Z)\), put
\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
T=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
V=TS,\quad R=ST^{-1}=V^{-1}.
\tag{4.1}
\]
Thus \(S^2=R^3=1\). The matrix \(R\) describes our symbol triangles; the previous lesson's period-polynomial convention \(U=ST\) uses a different triangle.

Let \(D_0\) be the augmentation-zero part of \(\mathbb Q[\mathbb P^1(\mathbb Q)]\), and write
\(\{\alpha,\beta\}=[\beta]-[\alpha]\).
Then \(\{\alpha,\beta\}+\{\beta,\gamma\}=\{\alpha,\gamma\}\).
For \(\Gamma=\Gamma_0(N)\), define the relative modular-symbol space
\(\mathcal M=(D_0)_\Gamma\), the coinvariants for the action on cusps. Its boundary is
\[
\partial\{\alpha,\beta\}=[\beta]-[\alpha]
\quad\text{in }\mathbb Q[\Gamma\backslash\mathbb P^1(\mathbb Q)].
\tag{4.2}
\]
Let \(\mathcal D=\ker\partial\).

**Theorem 4.1 (Manin symbols).** The space \(\mathcal M\) is generated by
\[
e_{c:d}=\{g0,g\infty\},\qquad
g=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathrm{SL}_2(\mathbb Z),
\]
indexed by \((c:d)\in\mathbb P^1(\mathbb Z/N\mathbb Z)\), with exactly the relations
\[
e_{c:d}+e_{d:-c}=0,\qquad
e_{c:d}+e_{d:-c-d}+e_{-c-d:c}=0.
\tag{4.3}
\]

**Proof.** The bottom-row coset parametrization is the second lesson's Proposition 1.2. Directly, left multiplication by \(\Gamma_0(N)\) multiplies the bottom row by a unit modulo \(N\); proportional rows conversely make the lower-left entry of \(g'g^{-1}\) zero modulo \(N\). Every primitive row lifts to a determinant-one matrix by the reduction-surjectivity proof there.

We prove completeness before taking coinvariants. Put \(B=\mathbb Q[G]\). The presentation \(G=C_2*C_3\), proved in the fifteenth lesson, Lemma 2.1, remains valid with \(S,V\), since \(V\) is conjugate to \(ST\). Its coset graph has vertices \(G/\langle S\rangle\) and \(G/\langle V\rangle\); the edge \(g\) joins its two cosets. It is a tree: reduced free-product words give connectivity, and a reduced closed path would give a nonempty alternating reduced word equal to one.

We have
\[
B(1-S)\cap B(1-V)=0.
\tag{4.4}
\]
An element of the intersection has coefficient sum zero at each vertex of either type. Its finite edge support lies in a finite forest. A leaf's only coefficient must be zero, and successive deletion of leaves proves that every coefficient is zero. Also the kernels of right multiplication by \(1-S,1-V\) are \(B(1+S)\) and \(B(1+V+V^2)\): a vector fixed by a finite cyclic right action is a sum of its orbit norms.

Infinity's stabilizer in \(G\) is \(\langle T\rangle\), so the kernel of \(B\to\mathbb Q[\mathbb P^1(\mathbb Q)]\), \(g\mapsto[g\infty]\), is \(B(1-T)\). The map
\[
B\longrightarrow D_0,\qquad x\longmapsto x(1-S)[\infty]
\tag{4.5}
\]
is onto. Indeed the augmentation ideal is generated by \(1-S,1-T\), from
\(1-gh=(1-g)+g(1-h)\); the \(1-T\) part vanishes at infinity.

If \(x\) is in the kernel of (4.5), write
\(x(1-S)=y(1-T)\). Since
\(1-T=(1-V)-T(1-S)\), we have
\((x+yT)(1-S)=y(1-V)\).
Both sides vanish by (4.4). Hence \(y\) lies in \(B(1+V+V^2)\), giving \(yV=y\), so \(yT=yS\). Thus
\((x-y)(1-S)=0\), and
\(x\in B(1+S)+B(1+V+V^2)\).
Conversely these two norm subspaces kill (4.5): their edges reverse or close around a triangle. Replacing \(V\) by \(R=V^{-1}\) leaves its norm unchanged.

Taking \(\Gamma\)-coinvariants of this quotient gives
\(\mathbb Q[\Gamma\backslash G]\) modulo these norms. Right multiplication of the bottom row by \(S,R,R^2\) gives (4.3). There are no additional relations. \(\square\)

### 4.1. Dimension and the cusp-form pairing

Let \(\mu=[G : \bar\Gamma]\), and let \(g,c,e_2,e_3\) be the curve's signature. In the transitive permutation module \(W=\mathbb Q[\Gamma\backslash G]\), the norm images are \(W^S,W^V\), intersecting in the one-dimensional \(W^G\). The numbers of \(S\)- and \(V\)-orbits are
\((\mu+e_2)/2\) and \((\mu+2e_3)/3\): fixed cosets give the elliptic points, and the other orbits have length two or three. The genus formula therefore gives
\[
\dim\mathcal M
=\mu-\frac{\mu+e_2}{2}-\frac{\mu+2e_3}{3}+1
=2g+c-1.
\tag{4.6}
\]
The boundary map is onto the degree-zero cusp-class space, by choosing any two cusp representatives. Its image has dimension \(c-1\), so
\[
\dim\mathcal D=2g.
\tag{4.7}
\]

For \(f,g\in S_2(\Gamma)\), integration defines
\[
\ell_{f,\bar g}(\{\alpha,\beta\})
=\int_\alpha^\beta\bigl(f(z)\,dz+\overline{g(z)}\,d\bar z\bigr).
\tag{4.8}
\]
Cusp decay, path independence and \(\Gamma\)-invariance make this well defined. If it vanishes on \(\mathcal D\), then every \(\{P,\gamma P\}\), with fixed cusp \(P\), has zero integral, since its boundary is zero. These are the group periods with base point \(P\). In weight two coboundaries are zero. Eichler–Shimura injectivity therefore gives \(f=g=0\). The weight-two dimension formula and (4.7) now prove
\[
S_2(\Gamma)\oplus\overline{S_2(\Gamma)}
\simeq\mathcal D^*\otimes\mathbb C.
\tag{4.9}
\]
This establishes the nondegenerate symbol pairing directly.

Reflection induces
\[
Je_{c:d}=e_{-c:d}.
\tag{4.10}
\]
Conjugate \(g\) by \(\varepsilon\): its bottom row is \((-c,d)\), and its endpoints are the reflected endpoints. Substitution \(z=-\bar w\) yields
\(\ell_f(Js)=-\ell_{\overline{f^\#}}(s)\).
Thus \(J\) exchanges the two summands of (4.9), and both \(\mathcal D^\pm\) have dimension \(g\). Restriction gives
\[
S_2(\Gamma)\simeq(\mathcal D^\pm)^*\otimes\mathbb C.
\tag{4.11}
\]
For example, vanishing of \(\ell_f\) on \(\mathcal D^+\) implies
\(\ell_f=-\ell_f\circ J=\ell_{\overline{f^\#}}\) on all of \(\mathcal D\); (4.9) forces \(f=0\). Dimension proves surjectivity. Changing the sign gives the other case.

On paths the weight-two Hecke operator is
\[
T_n\{\alpha,\beta\}
=\sum_{\substack{ad=n,\ (a,N)=1\\0\le b<d}}
\left\{\frac{a\alpha+b}{d},\frac{a\beta+b}{d}\right\}
\quad\text{for }\Gamma_0(N).
\tag{4.12}
\]
Coset independence and right-coset permutation make it well defined, as in Proposition 1.1. It acts on cusp-class boundaries too, so preserves \(\mathcal D\). Reflection commutes with the sum. In weight two (1.7) has constant coefficient factor, giving
\[
\ell_{T_nf}(s)=\ell_f(T_ns).
\tag{4.13}
\]
Thus either rational symbol sector computes the cusp-form eigenvalues. The matrices on the dual are transposes and have the same characteristic polynomials.

## 5. Complete computations at levels 11, 23 and 37

### 5.1. How to reproduce the reductions

For a prime level \(P\), write \(e_r=e_{r:1}\), \(0\le r<P\), and \(t=e_\infty=e_{1:0}\). We compute the quotient with \(Je=e\), so also impose
\[
e_r=e_{P-r}.
\tag{5.1}
\]
The two Manin relations become row relations by reducing each projective pair modulo \(P\). At these prime levels, the two cusp classes are \(0,\infty\), fixed by reflection. With boundary coordinate \([\infty]-[0]\), we have
\[
\partial e_0=1,\qquad \partial t=-1,\qquad
\partial e_r=0\quad(1\le r<P).
\tag{5.2}
\]
Indeed for \(r\ne0\), both endpoints of
\(\begin{pmatrix}1&0\\r&1\end{pmatrix}\) have denominator prime to \(P\) and represent the cusp zero. The boundary is onto, so (4.11) gives relative plus dimension \(g+1\). Taking the plus part preserves this exact sequence, by averaging with \((1+J)/2\); equivalently the quotient by \(J-1\) is the plus eigenspace.

The tables below specify coordinates for every generator, using (5.1) for the omitted half. Substitution in the two relations (4.3) verifies that each table defines a map from the quotient. The indicated basis generators map to the coordinate basis. Since their number is \(g+1\), the proved dimension implies that this map is an isomorphism. Thus the tables certify the entire relation reduction, rather than just selected symbol values.

Here is a complete rational procedure for the path operations. For a reduced rational \(x=a/b\), use the Euclidean continued fraction and its convergents
\[
x_{-1}=\infty,\quad x_0,\ldots,x_s=x.
\]
Successive convergents have determinant \(1\) or \(-1\). Decompose
\[
\{\infty,x\}=\sum_{j=0}^s\{x_{j-1},x_j\},\qquad
\{u,v\}=\{\infty,v\}-\{\infty,u\}.
\tag{5.3}
\]
For \(u=a/c,v=b/d\) with \(bc-ad=1\), the edge has bottom row \((d:c)\), from the matrix with columns \((b,d)^t,(a,c)^t\). If the determinant is \(-1\), negate the first column; its cusp is unchanged and the row is \((-d:c)\). Reduce that row modulo \(P\) and use the table.

For a good prime \(p\), define
\[
A_{p,b}=\begin{pmatrix}1&b\\0&p\end{pmatrix}\quad(0\le b<p),
\qquad B_p=\begin{pmatrix}p&0\\0&1\end{pmatrix}.
\tag{5.4}
\]
Their path sum is \(T_p\). Each column contribution displayed below is obtained by (5.3) from the transformed endpoints. Matrix columns always record images of basis vectors.

The Heilbronn–Merel shortcut is retained as a further proof task. Its precise locator is Stein's freely distributed online book, §8.3, equation (8.3.3) and Proposition 8.8:
\[
T_ne_{c:d}
=\sum_{\substack{a>b\ge0,\ d'>c'\ge0\\ad'-bc'=n}}
e_{(c,d)\left(\begin{smallmatrix}a&b\\c'&d'\end{smallmatrix}\right)}.
\tag{5.5}
\]
Omit a summand whose resulting row is not primitive modulo \(N\). This shortcut is not proved in these lessons and is not used as a proved result. The computations that follow use the independently derived path formula (4.12) and (5.3), so do not depend on (5.5).

### 5.2. Level 11

The signature is \(\mu=12,e_2=e_3=0,c=2,g=1\). All weight-two cusp forms are new, since the only proper divisor level is one and \(S_2(\mathrm{SL}_2(\mathbb Z))=0\).

Choose \(u=e_9=e_2,t=e_\infty\). The full table, with \(e_{11-r}=e_r\), is
\[
\begin{array}{c|rrrrrr|r}
r&0&1&2&3&4&5&\infty\\ \hline
[u]&0&0&1&1/2&-1/2&-1&0\\
[t]&-1&0&0&0&0&0&1
\end{array}.
\tag{5.6}
\]
For example, the two-term relations give \(e_1=0\), \(e_5=-e_2\), \(e_4=-e_3\). The triangle for \(r=2\) gives \(e_2+2e_4=0\), so \(e_3=e_2/2\). Together with \(e_0=-t\) and reflection these give every entry. The boundary row is \((0,-1)\); hence the cusp sector is \(\mathbb Qu\).

| Representative | \(\delta u\) | \(\delta t\) |
|---|---|---|
| \(A_{2,0}\) | \((\frac{-1}{2},0)\) | \((0,1)\) |
| \(A_{2,1}\) | \((0,0)\) | \((1,1)\) |
| \(B_2\) | \((\frac{-3}{2},0)\) | \((0,1)\) |

The three columns sum to
\[
[T_2]_{(u,t)}=\begin{pmatrix}-2&1\\0&3\end{pmatrix}.
\tag{5.7}
\]
On the cusp kernel \(T_2=-2\). The corresponding normalized newform therefore has \(a_2=-2\).

For \(T_3\) the complete four contributions are:

| Representative | \(\delta u\) | \(\delta t\) |
|---|---|---|
| \(A_{3,0}\) | \((-1,0)\) | \((0,1)\) |
| \(A_{3,1}\) | \((1,0)\) | \((\frac{1}{2},1)\) |
| \(A_{3,2}\) | \((\frac{-3}{2},0)\) | \((\frac{1}{2},1)\) |
| \(B_3\) | \((\frac{1}{2},0)\) | \((0,1)\) |

They give \([T_3]_{(u,t)}=\begin{pmatrix}-1&1\\0&4\end{pmatrix}\), hence \(a_3=-1\). The prime-square formula yields \(a_4=a_2^2-2=2\). Thus the unique normalized newform starts
\[
f_{11}=q-2q^2-q^3+2q^4+O(q^5).
\tag{5.8}
\]
It is the form \(\eta(z)^2\eta(11z)^2\) whose modularity and normalization were established in the ninth lesson's level-eleven example. The symbol computation independently recovers its Hecke eigenvalues.

### 5.3. Level 23

Here \(\mu=24,e_2=e_3=0,c=2,g=2\), so the whole two-dimensional cusp space is new. Put
\(u=e_{20}=e_3,\ v=e_{21}=e_2,\ t=e_\infty\).
With reflection for the remaining rows, the complete coordinates are
\[
\begin{array}{c|rrr}
r&[u]&[v]&[t]\\ \hline
0&0&0&-1\\
1&0&0&0\\
2&0&1&0\\
3&1&0&0\\
4&1&-1/2&0\\
5&0&1/2&0\\
6&-1&1/2&0\\
7&-1&1&0\\
8&-1&0&0\\
9&0&-1/2&0\\
10&1&-1&0\\
11&0&-1&0\\
\infty&0&0&1
\end{array}.
\tag{5.9}
\]
Substitution verifies both families (4.3) for all \(24\) rows and reflection. The coordinate map has three independent images and the relative plus dimension is \(g+1=3\), so it is an isomorphism. Boundary row \((0,0,-1)\) makes \(u,v\) the cusp basis.

The \(T_2\) contributions in this basis are:

| Representative | \(\delta u\) | \(\delta v\) | \(\delta t\) |
|---|---|---|---|
| \(A_{2,0}\) | \((-1,\frac{1}{2},0)\) | \((1,\frac{-1}{2},0)\) | \((0,0,1)\) |
| \(A_{2,1}\) | \((1,0,0)\) | \((0,0,0)\) | \((0,1,1)\) |
| \(B_2\) | \((1,-1,0)\) | \((1,\frac{-3}{2},0)\) | \((0,0,1)\) |

Summing gives
\[
[T_2]_{(u,v,t)}
=\begin{pmatrix}1&2&0\\-1/2&-2&1\\0&0&3\end{pmatrix},
\qquad
[T_2]_{\mathcal D^+}
=\begin{pmatrix}1&2\\-1/2&-2\end{pmatrix}.
\tag{5.10}
\]
Its trace is \(-1\) and determinant is \(-1\), so
\[
\det(X-T_2)=X^2+X-1.
\tag{5.11}
\]
In the cyclic basis \((u,T_2u)\), where
\(T_2u=u-v/2\), its matrix is
\(\begin{pmatrix}0&1\\1&-1\end{pmatrix}\).
The two eigenvalues \(a=(-1\pm\sqrt5)/2\) give the two normalized newforms.

The \(T_3\) contributions are:

| Representative | \(\delta u\) | \(\delta v\) | \(\delta t\) |
|---|---|---|---|
| \(A_{3,0}\) | \((0,\frac{-1}{2},0)\) | \((-1,\frac{1}{2},0)\) | \((0,0,1)\) |
| \(A_{3,1}\) | \((0,0,0)\) | \((0,1,0)\) | \((1,0,1)\) |
| \(A_{3,2}\) | \((-1,\frac{-1}{2},0)\) | \((-2,\frac{1}{2},0)\) | \((1,0,1)\) |
| \(B_3\) | \((-2,2,0)\) | \((-1,1,0)\) | \((0,0,1)\) |

Their cusp sum is
\[
[T_3]_{\mathcal D^+}
=\begin{pmatrix}-3&-4\\1&3\end{pmatrix}
=-I-2[T_2]_{\mathcal D^+}.
\tag{5.12}
\]
Thus \(a_3=-1-2a\), and \(a_4=a^2-2=-1-a\). The expansions are
\[
f_a=q+aq^2+(-1-2a)q^3+(-1-a)q^4+O(q^5),
\qquad a^2+a-1=0.
\tag{5.13}
\]
All Hecke matrices are rational and commute with \(T_2\). A rational matrix commuting with the cyclic \(T_2\) is a polynomial in it: its value on \(u\) determines its value on the basis \((u,T_2u)\). Hence every coefficient is in \(\mathbb Q(a)\), and \(a_2=a\) shows that the coefficient field is exactly \(\mathbb Q(\sqrt5)\). The two forms are exchanged by its nontrivial automorphism.

### 5.4. Level 37

Here \(\mu=38,e_2=e_3=2,c=2\), and
\[
g=1+38/12-2/4-2/3-2/2=2.
\]
Again the whole cusp space is new. Choose
\(u=e_{32}=e_5,\ v=e_{35}=e_2,\ t=e_\infty\).
The complete table is
\[
\begin{array}{c|rrr}
r&[u]&[v]&[t]\\ \hline
0&0&0&-1\\
1&0&0&0\\
2&0&1&0\\
3&0&1/2&0\\
4&0&1/2&0\\
5&1&0&0\\
6&0&0&0\\
7&1&0&0\\
8&1&-1/2&0\\
9&0&-1/2&0\\
10&0&0&0\\
11&0&0&0\\
12&0&-1/2&0\\
13&0&1/2&0\\
14&-1&1/2&0\\
15&-1&0&0\\
16&-1&0&0\\
17&0&-1/2&0\\
18&0&-1&0\\
\infty&0&0&1
\end{array}.
\tag{5.14}
\]
For example, \(e_6=0\) also follows from its fixed order-two row: \(6^2\equiv-1\pmod{37}\), so \(2e_6=0\). Fixed order-three rows similarly give zero where appropriate. Checking (4.3) on every row verifies the whole table. The three independent basis images and dimension \(g+1=3\) again prove completeness. The boundary row is \((0,0,-1)\), so \(u,v\) span the cusp kernel.

The three \(T_2\) contributions are:

| Representative | \(\delta u\) | \(\delta v\) | \(\delta t\) |
|---|---|---|---|
| \(A_{2,0}\) | \((0,0,0)\) | \((0,\frac{1}{2},0)\) | \((0,0,1)\) |
| \(A_{2,1}\) | \((-1,1,0)\) | \((0,0,0)\) | \((0,1,1)\) |
| \(B_2\) | \((-1,0,0)\) | \((0,\frac{-1}{2},0)\) | \((0,0,1)\) |

They sum to
\[
[T_2]_{(u,v,t)}
=\begin{pmatrix}-2&0&0\\1&0&1\\0&0&3\end{pmatrix},
\qquad
[T_2]_{\mathcal D^+}=\begin{pmatrix}-2&0\\1&0\end{pmatrix}.
\tag{5.15}
\]
One of the nontrivial path reductions is worth spelling out. For \(u=e_{32}\), the representative edge is \(\{0,1/32\}\). The \(A_{2,1}\) term is \(\{1/2,33/64\}\). The continued fraction
\(33/64=[0;1,1,15,2]\) has the relevant consecutive endpoints
\(1/2,16/31,33/64\). Their edge rows reduce to
\((31:2)=(34:1)\) and \((-64:31)=(23:1)\) modulo \(37\). The table gives
\[
e_{34}+e_{23}=v/2+(-u+v/2)=-u+v,
\]
which is the indicated column. The \(A_{2,0}\) term is
\(\{0,1/64\}=e_{27}=0\). The \(B_2\) term is
\(\{0,1/16\}=e_{16}=-u\). This verifies the full first column of (5.15) directly.

For \(T_3\), all four contributions are:

| Representative | \(\delta u\) | \(\delta v\) | \(\delta t\) |
|---|---|---|---|
| \(A_{3,0}\) | \((-1,0,0)\) | \((0,0,0)\) | \((0,0,1)\) |
| \(A_{3,1}\) | \((-1,\frac{1}{2},0)\) | \((0,\frac{1}{2},0)\) | \((0,\frac{1}{2},1)\) |
| \(A_{3,2}\) | \((-1,1,0)\) | \((0,1,0)\) | \((0,\frac{1}{2},1)\) |
| \(B_3\) | \((0,\frac{1}{2},0)\) | \((0,\frac{-1}{2},0)\) | \((0,0,1)\) |

Their sum on the cusp kernel is
\[
[T_3]_{\mathcal D^+}
=\begin{pmatrix}-3&0\\2&1\end{pmatrix}.
\tag{5.16}
\]
The \(T_2\) eigenvectors and both simultaneous eigenvalues are
\[
\begin{array}{c|cc}
\text{symbol eigenvector}&T_2&T_3\\ \hline
-2u+v&-2&-3\\
v&0&1
\end{array}.
\tag{5.17}
\]
For instance
\(T_3(-2u+v)=6u-3v=-3(-2u+v)\), and \(T_3v=v\).

Every Hecke operator commutes with \(T_2\), so it preserves its two distinct rational eigenlines. Its eigenvalue on either line is rational. Under (4.11)–(4.13) these are exactly the two eigenvalue systems of the cusp forms. Their eigenvalues are also algebraic integers by Theorem 2.1, so they are integers. Both coefficient fields are therefore \(\mathbb Q\). There are exactly two normalized newforms, distinguished by
\[
(a_2(f_{37}),a_3(f_{37}))=(-2,-3),\qquad
(a_2(g_{37}),a_3(g_{37}))=(0,1).
\tag{5.18}
\]
Their first coefficients and the good-prime square relation give
\[
f_{37}=q-2q^2-3q^3+2q^4+O(q^5),\qquad
g_{37}=q+q^3-2q^4+O(q^5).
\tag{5.19}
\]
These eigenvalue conditions identify both forms uniquely because the cusp space is entirely new and both \(T_2\) eigenspaces are one-dimensional. No elliptic-curve identification is needed for the computation.

## 6. Exercises

1. **Easy.** Starting from the two expansions (5.13), compute the matrix and characteristic polynomial of \(T_2\) on \(S_2(\Gamma_0(23))\), using only the first two coefficients of its images.
2. **Medium.** Carry out the complete plus-sector Manin computation at level \(11\): reduce all generators, find the boundary kernel, compute \(T_2\), and identify its normalized newform.
3. **Medium.** Prove perfectness of \((T,f)\mapsto a_1(Tf)\). Explain why using only good-prime operators does not give the same argument.
4. **Hard.** Prove that every \(f^\sigma\), for \(f\) a normalized newform and \(\sigma\in\operatorname{Aut}(\mathbb C)\), is a newform of the same primitive level. Make the rationality of the old space and the use of primitive multiplicity explicit.

5. **Hard.** On \(S_{12}(\mathrm{SL}_2(\mathbb Z))=\mathbb C\Delta\), let \(I=T_1\) and \(M=2\mathbb ZI\subset\mathbb T_{\mathbb Z}\). Show that \(M\) has full rational rank, but restriction of the Fourier pairing to \(M\) is not perfect over \(\mathbb Z\). Compute the map \(M\otimes\mathbb F_2\to\mathbb T_{\mathbb Z}\otimes\mathbb F_2\). Explain how the argument in Theorem 3.2b rules out this defect for the actual bounded span.

## 7. Full solutions

### Solution 1

Let \(\alpha,\beta\) be the distinct roots of \(X^2+X-1\), with corresponding forms \(F=f_\alpha,G=f_\beta\). The rational combinations
\[
h=\frac{F-G}{\alpha-\beta},\qquad
g=\frac{\alpha G-\beta F}{\alpha-\beta}
\]
have expansions, by (5.13),
\[
g=q-q^3-q^4+O(q^5),\qquad
h=q^2-2q^3-q^4+O(q^5).
\]
They form a basis: the matrix of their first two coefficients is the identity. Consequently those two coefficients determine every form in this space.

The good-prime coefficient formula gives
\(a_1(T_2s)=a_2(s)\) and \(a_2(T_2s)=a_4(s)+2a_1(s)\).
For \(g\), these are \(0,1\), so \(T_2g=h\).
For \(h\), they are \(1,-1\), so \(T_2h=g-h\).
Thus
\[
[T_2]_{(g,h)}=\begin{pmatrix}0&1\\1&-1\end{pmatrix},
\qquad
\det(X-T_2)=X(X+1)-1=X^2+X-1.
\]
The determinant calculation agrees with (5.11) without using the symbol matrix.

### Solution 2

There are twelve projective rows, \(e_0,\ldots,e_{10},t\). Reflection gives \(e_{11-r}=e_r\), and the two-term relation at zero gives \(e_0=-t\). For a nonzero \(r\), that relation is \(e_r+e_{-r^{-1}}=0\). At \(r=1\), reflection makes it \(2e_1=0\), so \(e_1=e_{10}=0\). At \(r=2,3\), it gives
\(e_5=-e_2\) and \(e_4=-e_3\). The triangle relation at \(r=2\) is
\(e_2+e_7+e_4=0\); reflection gives \(e_7=e_4\), so \(e_4=-e_2/2\), \(e_3=e_2/2\).

Put \(u=e_2\). Every generator is therefore in the list
\[
\begin{array}{c|rrrrrrrrrrrr}
r&0&1&2&3&4&5&6&7&8&9&10&\infty\\ \hline
e_r&-t&0&u&u/2&-u/2&-u&-u&-u/2&u/2&u&0&t
\end{array}.
\]
Substitution in all two- and three-term relations confirms consistency. The signature has \(g=1,c=2\); the relative plus dimension is two, so \(u,t\) are independent and the table is the full quotient. The boundary row is \((0,-1)\), hence its cusp kernel is \(\mathbb Qu\).

Use the edge \(e_9=\{0,1/9\}=u\), as a representative for computing \(T_2\). Its three transformed paths are
\[
\{0,1/18\},\quad \{1/2,5/9\},\quad \{0,2/9\}.
\]
The first is \(e_7=-u/2\).
For the second, \(5/9=[0;1,1,4]\); its last edge from \(1/2\) to \(5/9\) has row \((9:2)=(10:1)\), so is zero.
For the third, \(2/9=[0;4,2]\). The two edges from zero through \(1/4\) to \(2/9\) have rows \((4:1)\) and \((-9:4)=(6:1)\). They give \(-u/2-u=-3u/2\).
Thus \(T_2u=-2u\).

For \(t=\{\infty,0\}\), the three images are
\(t,\{\infty,1/2\},t\). The middle path is
\(t+\{0,1/2\}=t+u\). Hence \(T_2t=u+3t\).
The full matrix is \(\begin{pmatrix}-2&1\\0&3\end{pmatrix}\) and its cusp restriction is \(-2\).

Since level one has no weight-two cusp forms, the one-dimensional level-eleven space is new. Its normalized eigenform has \(a_2=-2\) and is
\(\eta(z)^2\eta(11z)^2\), by the independently established cusp form in the ninth lesson, Section 6. Normalization \(a_1=1\) determines it uniquely.

### Solution 3

Let \(\mathbb T_{\mathbb C}\) be the commuting algebra of all Hecke operators and diamonds. If \(f\) pairs to zero with every operator, then
\(a_n(f)=a_1(T_nf)=0\) for every \(n\ge1\). Fourier uniqueness gives \(f=0\).

If \(T\) pairs to zero with every \(f\), use \(T_nf\) as the test form. Commutation yields
\[
0=a_1(TT_nf)=a_1(T_nTf)=a_n(Tf).
\]
This holds for every \(n,f\), so \(Tf=0\) for all \(f\), giving \(T=0\). Both spaces are finite-dimensional; two nondegenerate maps into the other's dual force equal dimensions, so the pairing is perfect.

Both arguments use every \(T_n\), including the bad-prime powers. Restricting to good indices would only show vanishing of coefficients prime to the level. That does not imply Fourier uniqueness: an oldform \(V_pg\), with \(p\mid N\), can have all those coefficients zero while being nonzero. The asserted proof consequently needs the full algebra.

### Solution 4

By (3.5), rational Fourier coefficients define a rational structure on every relevant level space. A map \(V_d\) inserts zeros and moves coefficient \(a_n\) to position \(dn\), so it sends rational forms to rational forms. Taking rational bases of the finitely many lower-level spaces proves that the old space is the complexification of a rational subspace. It is stable under \(\sigma\) and \(\sigma^{-1}\).

The form \(f^\sigma\) is supplied by this rational structure, and rational Hecke matrices give
\(T_nf^\sigma=\sigma(a_n(f))f^\sigma\), together with the transformed diamond character. It is normalized because its first coefficient is one. Since \(f\) is nonzero and new, it cannot be old; otherwise positive orthogonality would give \(\langle f,f\rangle=0\). Stability under \(\sigma^{-1}\) then shows that \(f^\sigma\) cannot be old.

Apply the primitive decomposition, Theorem 4.5 of the newforms lesson, to its good-prime system. That eigenspace consists of the degeneracies of one primitive newform at some \(M\mid N\). If \(M<N\), every such degeneracy is old at level \(N\), contrary to the preceding paragraph. Therefore \(M=N\). The eigenspace is now its single new line, so \(f^\sigma\) is the normalized newform of primitive level \(N\). Its weight remains \(k\), and its character is \(\sigma\chi\). The argument uses rational old spaces and primitive eigenvalue separation, without applying \(\sigma\) to the Petersson integral.

### Solution 5

The level-one discriminant is normalized by \(a_1(\Delta)=1\) and has integer coefficients. Since the complex cusp space is its line, its integer lattice is exactly \(\mathbb Z\Delta\): the first coefficient gives the scalar, and an integer scalar gives an integral expansion. Integral duality therefore gives \(\mathbb T_{\mathbb Z}=\mathbb ZI\), with \(a_1(I\Delta)=1\).

The submodule \(M=2\mathbb ZI\) has rank one and rational span \(\mathbb QI\), but quotient \(\mathbb T_{\mathbb Z}/M=\mathbb Z/2\mathbb Z\). A functional on \(M\) can assign the value one to \(2I\). It cannot extend to an integer-valued functional on \(\mathbb ZI\), since the extension would have to assign \(1/2\) to \(I\). More explicitly, pairing an integer multiple \(c\Delta\) with \(2I\) gives \(2c\). The restriction map to \(\operatorname{Hom}(M,\mathbb Z)\simeq\mathbb Z\) consequently has image \(2\mathbb Z\) and cokernel \(\mathbb Z/2\mathbb Z\). Equal rank has not supplied perfectness.

Both tensor products with \(\mathbb F_2\) have dimension one. Nevertheless their inclusion map is zero, because the generator represented by \(2I\) maps to twice \(I\), which is zero modulo two. Thus the image, rather than the dimension of \(M\otimes\mathbb F_2\), is what matters. The nonzero reduction of \(\Delta\) annihilates that image.

For the actual coefficient span the bound is \(B=\lfloor12/12\rfloor=1\), so \(A_B=\mathbb ZT_1=\mathbb ZI\). In the general proof, a form annihilating the image of \(A_B\) has all bounded Fourier coefficients zero modulo the chosen prime. Arithmetic Sturm then makes every coefficient zero modulo that prime. Hence this annihilator is zero, the image is the whole reduced Hecke algebra, and the finite quotient illustrated here cannot survive. Checking every prime also excludes torsion at primes dividing the level.

## What this lesson does not prove

The local arguments establish Hecke equivariance (Proposition 1.1 and (1.7)–(1.8)) and the Manin presentation (Theorem 4.1). The remaining rational-structure arguments use the Eichler–Shimura dimension comparison, whose compact-curve prerequisite still needs a programme proof. These arguments give integral characteristic polynomials (Theorem 2.1), perfect pairing (Theorem 3.1), an integral Fourier basis (Theorem 3.2), number fields ((3.6)) and the Galois argument (Theorem 3.3) once that dependency and the newform dependencies named below are proved. Proposition 3.2a is additionally conditional on the canonical-model hypotheses stated explicitly above. Theorem 3.2b uses those hypotheses and the sixth lesson's geometric arithmetic-Sturm prerequisites. Its reduction-at-every-prime argument is local, but does not prove those prerequisites. The symbol-to-cusp comparison, computations and solutions retain the same dependency status. None of these conditional chains is counted as closed merely because its final linear-algebra step is written out.

The Heilbronn shortcut (5.5) is located in the author's free online Stein edition, §8.3, equation (8.3.3) and Proposition 8.8, pages 131–132 in that PDF. Its proof remains required. The example computations use (4.12) instead.

Earlier course dependencies, with the unresolved prerequisites identified above, are the following:

- The bottom-row coset parametrization and integral reduction-surjectivity argument: Congruence subgroups, cusps and elliptic points, Lemma 1.1 and Proposition 1.2. The cusp counts and elliptic counts used in the examples are in its Sections 2–3.
- The genus formula: Modular curves and their genus, Theorem 3.3.
- The weight-two dimension, regular odd-weight bundle argument and arithmetic coefficient bound: Dimension formulas for congruence subgroups, Theorem 4.1, Solution 4 and Theorem 6.2 in Section 6.1. The arithmetic theorem states its principal-level field structure and bounded-denominator input with exact Deligne–Rapoport locators. Its Appendix A writes the analytic Riemann–Roch, duality and genus proofs, with the remaining elementary analytic framework stated explicitly.
- The prime representatives, Fourier formula, commutativity and all-index product relation: Hecke operators for \(\Gamma_0\) and \(\Gamma_1\), Lemma 2.1, Theorem 2.3 and Theorem 3.1. Its Section 6 and Solution 1 prove the level-eleven eta product and coefficients.
- The primitive decomposition and separation across levels: Oldforms, newforms and the theory of Atkin–Lehner and Li, Theorem 4.5, with the main-lemma and character-recovery inputs explicitly stated in its Sections 3 and 4.1.
- The coefficient pairing, free-product presentation, convergent periods, cohomological dimension and cup injectivity: Group cohomology and the Eichler–Shimura isomorphism, Section 1, equations (1.5)–(1.7), Lemma 2.1, Theorem 3.1, Proposition 4.1, Lemma 5.1 and Proposition 5.2. Section 2 above extends its isomorphism to the odd-weight cases needed here.

The integrality lemma and Proposition 3.2a prove the integer-coefficient q-expansion consequence and \(A=\mathbb T_{\mathbb Z}\) from the listed model properties. Their geometric construction is unresolved here, including smoothness and irreducibility at primes dividing the level, the weight sheaf, and the analytic/formal comparisons. Katz's free §1.6 q-expansion theorem over an inverted-level base cannot by itself close this bad-prime gap. Weight one and integral torsion phenomena before passing to lattices are also not treated. Deligne's étale construction and its comparison with classical periods are not used in these local arguments; the free original article, §§3.9–3.20, formulates that further arithmetic interpretation.

## References

- **Deligne–Rapoport 1973.** P. Deligne and M. Rapoport, *Les schémas de modules de courbes elliptiques*, original paper, Chapters IV–VII. [Author's free article](https://publications.ias.edu/sites/default/files/Number22.pdf). These chapters locate the arithmetic constructions whose required local or earlier programme proofs remain outstanding.
- **Katz 1973.** N. M. Katz, *p-adic properties of modular schemes and modular forms*, §1.6, Theorem 1.6.1 and Corollary 1.6.2, with the principal level inverted. [Author's free original paper](https://web.math.princeton.edu/~nmk/old/padicpropMFMS.pdf).
- **Wiese 2018.** G. Wiese, *Computational Arithmetic of Modular Forms*, arXiv:1809.04645v1, §§1.2–1.3, 2, 5 and 7.3–7.5. [Exact version](https://arxiv.org/abs/1809.04645v1).
- **Stein, free online edition.** W. Stein, *Modular Forms: A Computational Approach*, Chapters 3 and 8, and §9.3; §8.3, Proposition 8.8 and equation (8.3.3) locate the retained shortcut. [Exact author's free PDF](https://wstein.org/books/modform/stein-modform.pdf). The author's [distribution notice](https://wstein.org/books/modform/README.html) explicitly makes this online edition freely available.
- **Best et al.** A. J. Best and collaborators, *Computing classical modular forms*, arXiv:2002.04717v4, §5.1, for the modular-symbol comparison. [Exact version](https://arxiv.org/abs/2002.04717v4).
- **Deligne 1969.** P. Deligne, *Formes modulaires et représentations \(l\)-adiques*, Séminaire Bourbaki 355, §3. [Original French article](https://www.numdam.org/item/SB_1968-1969__11__139_0/).
