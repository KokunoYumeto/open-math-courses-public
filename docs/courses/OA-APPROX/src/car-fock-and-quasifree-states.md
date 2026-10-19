# Fermions, Fock space and quasi-free factors

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

Anticommuting generators can produce ordinary matrix algebras. Parity strings explain how: they absorb the signs between successive modes. Positive occupation densities on these finite algebras fit together into a state for every covariance. A reduced doubled exterior space then realizes its completed cyclic representation and proves that its generated von Neumann algebra is a factor.

The proofs use finite Hilbert tensor products, positive square roots, finite matrix algebras and completion of a cyclic inner-product space. Their exact constructions are supplied in Sections 9–12 below and [ITP Section 10](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice). Section 6 constructs bounded finite-mode approximants directly; its constant-state conclusions use the completed product model and modular graph in [ITP Section 11](infinite-tensor-products.md#11-modular-action-of-the-faithful-identical-two-level-product), and the finite-corner trace construction in Sections 18–20 below. The AF comparison is AF-algebras, Section 4 and Example 5.3. No classification theorem is used in the factor or approximation proofs.

Inner products are linear in the second variable. Accordingly, **creation** \(c(f)\) is linear in \(f\), and **annihilation** \(a(f)=c(f)^*\) is conjugate-linear. Our CAR convention is
\[
\{a(f),a(g)\}=0,\qquad
\{a(f),a(g)^*\}=\langle f,g\rangle1,\qquad
\{x,y\}=xy+yx. \tag{1}
\]
The occupation covariance is \(\omega(a(f)^*a(g))=\langle g,Tf\rangle\). Thus the empty vacuum has \(T=0\). Using a linear creation generator instead changes the placement of adjoints and the covariance parameter. These conventions must be changed together.

The one-particle Hilbert space \(K\) may be arbitrary. We explicitly distinguish finite dimension, separable infinite dimension and a general directed finite-mode approximation. The finite-mode, state and factor phenomena are compared with the selected freely accessible CAR materials below.

## 1. Exterior space and bounded operators

For \(n\ge1\), let \(U_\sigma\) permute tensor coordinates according to the left action of the symmetric group, using \(\sigma^{-1}\) on indices. Define
\[
A_n=\frac1{n!}\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)U_\sigma,
\qquad \Lambda^nK=A_nK^{\otimes n},\qquad \Lambda^0K=\mathbb C.
\]
The group law gives \(A_n^2=A_n\): in the double sum each resulting permutation occurs \(n!\) times with its sign. The adjoint of \(U_\sigma\) is \(U_{\sigma^{-1}}\), whose sign is the same, so \(A_n^*=A_n\). Thus these are orthogonal projections.

For an orthonormal basis \((e_j)\), indexed by an arbitrarily ordered set, put
\[
[f_1,\ldots,f_n]=\sqrt{n!}\,A_n(f_1\otimes\cdots\otimes f_n).
\]
The vectors \([e_{j_1},\ldots,e_{j_n}]\), with \(j_1<\cdots<j_n\), form an orthonormal basis of \(\Lambda^nK\). Distinct increasing tuples have disjoint permutation orbits, while a tuple with repeated entries has zero antisymmetrization. Expanding the tensor basis proves completeness. More generally,
\[
\langle[f_1,\ldots,f_n],[g_1,\ldots,g_n]\rangle
=\det[\langle f_i,g_j\rangle]_{i,j=1}^n. \tag{2}
\]
This follows by expanding \(A_n\) and taking the product of the coordinate inner products.

The Hilbert direct sum
\[
\mathcal F(K)=\bigoplus_{n\ge0}\Lambda^nK
\]
is the fermionic Fock space; \(\Omega=1\in\Lambda^0K\) is its vacuum. If \(\dim K=d<\infty\), then
\[
\dim\Lambda^nK=\binom dn,\qquad \dim\mathcal F(K)=2^d.
\]
The unscaled exterior product of homogeneous vectors is
\(\eta\wedge\zeta=A_{p+q}(\eta\otimes\zeta)\), for degrees \(p,q\). It is associative: both iterated products equal the full antisymmetrization of the three tensor factors, since full antisymmetrization absorbs a preceding antisymmetrization of any consecutive block. It defines a product on the algebraic sum of finite-degree vectors.

On that sum define
\[
c(f)\eta=\sqrt{n+1}\,A_{n+1}(f\otimes\eta),
\quad \eta\in\Lambda^nK. \tag{3}
\]
In particular \(c(f)[g_1,\ldots,g_n]=[f,g_1,\ldots,g_n]\).
For a unit vector \(f\), choose a basis beginning with \(f\). On the occupation basis, \(c(f)\) carries a vector not containing \(f\) to the corresponding vector containing \(f\), up to its sign, and kills those already containing \(f\). It is an isometry on the first closed span and zero on its orthogonal complement. Therefore \(c(f)\) is bounded with norm one. Linearity and scaling give \(\|c(f)\|=\|f\|\).

The adjoint has the contraction formula
\[
a(f)[g_1,\ldots,g_n]
=\sum_{j=1}^n(-1)^{j-1}\langle f,g_j\rangle
[g_1,\ldots,\widehat{g_j},\ldots,g_n],\qquad a(f)\Omega=0. \tag{4}
\]
To verify it, take inner products with arbitrary product vectors and expand the determinant (2) along its first row. Alternation gives \(\{c(f),c(g)\}=0\). Formula (4) gives
\[
a(f)c(g)\eta=\langle f,g\rangle\eta-c(g)a(f)\eta
\]
on the occupation core. Adjoints give the other relations in (1). Boundedness extends all identities to \(\mathcal F(K)\).

**Lemma 1.1.** The Fock CAR representation is irreducible.

**Proof.** A vector annihilated by every \(a(f)\) is a multiple of \(\Omega\): a nonzero coefficient at a nonempty finite occupation set gives a nonzero coefficient after contraction by one of its basis vectors. If \(x\) commutes with all creators and annihilators, then \(a(f)x\Omega=0\), so \(x\Omega=\lambda\Omega\). Products of creators applied to \(\Omega\) span a dense subspace. Commutation makes \(x=\lambda1\) on it and hence everywhere. \(\square\)

## 2. Finite modes are full matrix algebras

Consider any CAR family on a nonzero representation Hilbert space. For a unit \(f\), write \(a=a(f)\) and \(n=a^*a\). Relations (1) give
\[
a^2=0,\quad aa^*=1-n,\quad n^2=n,\quad an=a,\quad na=0.
\]
Neither \(n\) nor \(1-n\) is zero: either possibility together with the relations would force \(a=0\) and then \(1=0\). Hence \(\|a\|=1\). Scaling shows
\[
\|a(f)\|=\|f\|. \tag{5}
\]
The operators
\[
e_{11}=1-n,\quad e_{12}=a,\quad e_{21}=a^*,\quad e_{22}=n
\]
are matrix units. The two products \(aa^*=e_{11}\) and \(a^*a=e_{22}\), together with the displayed relations, verify every matrix-unit product and adjoint.

For orthonormal \(f_1,\ldots,f_d\), put \(a_j=a(f_j)\), \(n_j=a_j^*a_j\), and
\[
Z_j=1-2n_j,\qquad
b_j=Z_1\cdots Z_{j-1}a_j. \tag{6}
\]
The \(Z_j\) are commuting selfadjoint unitaries. Two anticommutations show that \(n_i\) commutes with \(a_j,a_j^*\) for \(i\ne j\); \(Z_j\) anticommutes with \(a_j,a_j^*\). Each \(b_j\) therefore gives a copy of the above matrix units. The copies for distinct \(j\) commute. Indeed, moving the \(i\)-th annihilator or creator past the \(j\)-th generator contributes one CAR sign, and moving it past the factor \(Z_i\) in the later string contributes a second sign. They cancel. Their diagonal projections commute with all the other copies as well.

**Theorem 2.1.** For a \(d\)-dimensional subspace \(E\subset K\), the unital C*-algebra generated by its CAR family is \(M_{2^d}\).

**Proof.** Multiply one matrix unit from each commuting system to obtain \(E_{\alpha\beta}\), with \(\alpha,\beta\in\{1,2\}^d\). These satisfy
\[
E_{\alpha\beta}E_{\mu\nu}=\delta_{\beta\mu}E_{\alpha\nu},\qquad
E_{\alpha\beta}^*=E_{\beta\alpha},\qquad
\sum_\alpha E_{\alpha\alpha}=1.
\]
Fix an index \(o\). The space \(Q=E_{oo}H\) is nonzero: if \(E_{oo}=0\), then \(E_{\alpha o}^*E_{\alpha o}=0\), hence every \(E_{\alpha\alpha}=E_{\alpha o}E_{o\alpha}=0\), contradicting their sum. The map
\[
U(\delta_\alpha\otimes\eta)=E_{\alpha o}\eta\quad(\eta\in Q)
\]
is isometric, because the displayed products make different summands orthogonal and preserve each summand's inner product. It is onto, since every \(E_{\alpha\alpha}H=E_{\alpha o}Q\). Under \(U\), \(E_{\alpha\beta}\) is the usual matrix unit tensored with \(1_Q\). Thus for every scalar matrix \(X=[x_{\alpha\beta}]\),
\[
\left\|\sum_{\alpha,\beta}x_{\alpha\beta}E_{\alpha\beta}\right\|
=\|X\otimes1_Q\|=\|X\|.
\]
The upper bound follows by expanding in an orthonormal basis of \(Q\); the lower bound follows by testing \(v\otimes\eta\) for a fixed unit \(\eta\in Q\) and a maximizing finite-dimensional unit vector \(v\). This proves an onto isometric matrix identification, including arbitrary representation multiplicity. Formula (6) recovers the original \(a_j\), so the two generated algebras agree. For \(d=0\), the algebra is the scalar identity algebra. The complete finite-unit construction is in [Sections 10.3–10.4](#10-4-full-finite-matrix-units-and-their-exact-concrete-norm). \(\square\)

Define \(\operatorname{CAR}(K)\) using the concrete Fock family and the identity. The theorem gives a canonical embedded \(\operatorname{CAR}(E)\) for every finite-dimensional \(E\). The union over \(E\) is norm dense: every polynomial uses finitely many vectors, and (5) makes approximation of generator vectors norm continuous.

The finite automorphism assertion used in Exercise 9 also follows from matrix units. If \(\beta\) is an automorphism of \(M_N\), the corner of \(\beta(E_{oo})\) is scalar, so its range in \(\mathbb C^N\) has dimension one. Choose a unit vector \(\eta\) in that range. The vectors \(\beta(E_{\alpha o})\eta\) form an orthonormal basis by the matrix-unit products and diagonal sum. The resulting unitary \(U\delta_\alpha=\beta(E_{\alpha o})\eta\) satisfies \(\beta(E_{\alpha\beta})=UE_{\alpha\beta}U^*\), hence \(\beta=\operatorname{Ad}U\).

Any other CAR family induces isomorphisms of these finite matrix algebras by matching generators. The maps are compatible on overlaps, since they match the same polynomials. Their isometric union map extends to an isomorphism onto the generated C*-algebra. This proves representation independence and the CAR universal property without choosing a norm on a free algebra.

**Corollary 2.2.** The CAR algebra is simple. For separable infinite-dimensional \(K\),
\[
\operatorname{CAR}(K)\cong\bigotimes_{j=1}^\infty M_2.
\tag{7}
\]
For finite-dimensional \(K\) it is \(M_{2^{\dim K}}\).

**Proof.** Suppose a closed two-sided ideal \(J\) contains \(0\ne x\), and put \(r=\|x\|\). Choose a local matrix element \(y\) with \(\|x-y\|<r/16\). Then
\[
\|x^*x-y^*y\|<33r^2/256<r^2/4,\qquad \|y\|>15r/16.
\]
In that finite matrix algebra, choose a rank-one projection \(e\) onto an eigenvector of \(y^*y\) with largest eigenvalue \(t=\|y\|^2>3r^2/4\). Finite-dimensional diagonalization is proved in [Section 10.7](#10-7-elementary-finite-maximum-and-eigenvector-lemma). Hence \(ey^*ye=te\), and \(h=ex^*xe\in J\cap e\operatorname{CAR}(K)e\) satisfies \(\|h-te\|<r^2/4<t\). The corner has identity \(e\); the geometric series
\[
h^{-1}=t^{-1}\sum_{k\ge0}(e-h/t)^k
\]
converges in it. Thus \(e=h^{-1}h\in J\). Within the same local full matrix algebra, choose partial isometries \(v_i\) carrying \(e\) to its orthogonal rank-one diagonal projections. Their sum gives \(1=\sum_i v_i e v_i^*\in J\). Thus every nonzero closed ideal is the whole algebra. This argument also applies when the chosen local algebra is scalar; the full corner estimates are in [Sections 10.8–10.9](#10-8-a-geometric-series-inverse-in-a-closed-corner).

For a countable orthonormal basis, the strings (6) identify the first \(d\) modes with the first \(d\) tensor factors, compatibly under \(x\mapsto x\otimes1\). Their dense union gives (7). For an arbitrary nonseparable \(K\), the finite-subspace directed limit remains valid; (7) is asserted here only with a countable basis. \(\square\)

It is the dimension of \(K\) that decides the finite versus infinite case. An infinite-dimensional representation space alone does not: amplifying one mode on \(\mathbb C^2\otimes\ell^2\) still generates \(M_2\otimes1\).

## 3. Parity, orthogonal subspaces and automorphisms

For a unitary \(u\) on \(K\), the family \(a(uf)\) satisfies (1). The universal property gives an automorphism
\[
\alpha_u(a(f))=a(uf),\qquad \alpha_u\alpha_v=\alpha_{uv}. \tag{8}
\]
If \(u_\lambda\to u\) strongly, then
\[
\|\alpha_{u_\lambda}(a(f))-\alpha_u(a(f))\|
=\|(u_\lambda-u)f\|\to0.
\]
Telescoping finite products proves convergence on polynomials; their norm density and the automorphisms' isometric bounds prove point-norm convergence on the whole algebra. This applies in particular to the strong* topology on the unitary group.

Let \(\gamma=\alpha_{-1}\). Its even and odd spaces are
\[
\operatorname{CAR}(K)_{\rm ev}=\{x:\gamma(x)=x\},\qquad
\operatorname{CAR}(K)_{\rm odd}=\{x:\gamma(x)=-x\}.
\]
Every element splits by the bounded projections \((\operatorname{id}\pm\gamma)/2\). Polynomials of even, respectively odd, total generator degree are dense in these spaces.

If \(L\perp N\), all generators and adjoint generators from the two spaces anticommute. Moving a homogeneous word of degree \(p\) past one of degree \(q\) gives the sign \((-1)^{pq}\). By polynomial approximation,
\[
xy=(-1)^{pq}yx
\quad\text{for }x\in\operatorname{CAR}(L)_p,\ y\in\operatorname{CAR}(N)_q.
\tag{9}
\]
Thus even elements commute across the spaces; two odd elements anticommute.

**Proposition 3.1.** Multiplication gives faithful spatial tensor identifications
\[
C^*(\operatorname{CAR}(L),\operatorname{CAR}(N)_{\rm ev})
\cong\operatorname{CAR}(L)\otimes_{\min}\operatorname{CAR}(N)_{\rm ev},
\tag{10}
\]
and the analogous identification with the first leg even.

**Proof.** Take finite-dimensional \(E\subset L,F\subset N\), and order the \(E\)-modes before the \(F\)-modes in (6). On \(E\oplus F\), a generator of the second leg becomes
\[
P_E\otimes a_F(f),\qquad P_E=Z_1\cdots Z_{\dim E}.
\]
An even second-leg word has an even number of these strings, so is exactly \(1\otimes y\). The first leg is \(x\otimes1\). To check the norm in arbitrary faithful representations, diagonalize finite Fock parity. If \(f=\dim F>0\), its even and odd occupation spaces both have dimension \(2^{f-1}\), and the even algebra is
\[
\operatorname{CAR}(F)_{\rm ev}
=M_{2^{f-1}}\oplus M_{2^{f-1}}.
\]
Every faithful representation contains both central blocks. On each block Theorem 2.1's matrix-unit unitary removes only a nonzero multiplicity space; it leaves the matrix norm unchanged. Thus for \(z=\sum_k x_k\otimes y_k\), the tensor norm is the maximum of the two finite matrix norms of \(\sum_k x_k\otimes y_k^\pm\), independently of those faithful representations. In the parity-string realization these are exactly the two blocks of \(\sum_k x_ky_k\). For \(f=0\) the second leg is scalar and the same assertion is immediate. This proves injectivity and the exact spatial norm on every finite tensor algebra, rather than only commutation of its generators.

The unions of the finite subalgebras are dense in both legs. For the even leg apply \((\operatorname{id}+\gamma)/2\) to a local polynomial approximation. Approximating both entries in a finite sum of simple tensors, with \(\|x\otimes y\|=\|x\|\|y\|\), makes these finite tensor algebras dense in the spatial completion. Their compatible isometries therefore extend onto the algebra generated by multiplication: their ranges contain the two legs and have dense polynomial span. Interchanging the order of the legs proves the other assertion. [Section 12](#12-the-exact-even-leg-spatial-tensor-identification) supplies the block and completion details. \(\square\)

Every word can also be put in **normal order** by using
\[
a(g)a(f)^*=\langle g,f\rangle1-a(f)^*a(g).
\]
Move each creator left; each swap either reduces the number of inversions or removes two letters. Repetition terminates and gives a linear combination of
\[
a(f_1)^*\cdots a(f_n)^*a(g_m)\cdots a(g_1),\qquad n,m\ge0. \tag{11}
\]
This includes the identity. Their span is a dense *-subalgebra. A bounded functional, and in particular a state, is determined by its values there.

## 4. A positive state for every covariance

Let \(T\in B(K)\) with \(0\le T\le1\). For every finite-dimensional \(E\subset K\), its compression \(S_E=P_ET|_E\) is a positive contraction. Choose an ordered orthonormal eigenbasis of \(S_E\), with eigenvalues \(p_1,\ldots,p_d\), and use the finite matrix identification of Section 2 to define the positive occupation density
\[
\rho_E=\bigotimes_{j=1}^d\operatorname{diag}(1-p_j,p_j),
\qquad \varphi_E(x)=\operatorname{Tr}(\rho_Ex).
\]
Its diagonal entries are nonnegative and sum to one, including at \(p_j=0,1\); hence \(\varphi_E\) is a positive state. No global eigenbasis of \(T\), and no reducing condition on \(E\), is being assumed.

We will first fit these finite states together. For the later cyclic model put \(A=(1-T)^{1/2}\), \(B=T^{1/2}\). Their commuting positive roots are supplied by the norm-series construction in [Sections 8.1–8.2 of the periodic CAR lesson](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative). On the conjugate Hilbert space, inner products satisfy
\(\langle\bar f,\bar g\rangle=\langle g,f\rangle\).
Let
\[
K_0=\overline{AK}=(\ker A)^\perp,\qquad
K_1=\overline{BK}=(\ker B)^\perp,\qquad
\mathcal L=K_0\oplus\overline{K_1}.
\]
Use ordinary Fock annihilators and creators on \(\mathcal F(\mathcal L)\), denoted by \(a_{\mathcal L},c_{\mathcal L}\). Define
\[
\pi_T(a(f))=
a_{\mathcal L}(Af\oplus0)
+c_{\mathcal L}(0\oplus\overline{Bf}). \tag{12}
\]
Both terms are conjugate-linear in \(f\). The two legs are orthogonal, so their mixed CAR terms vanish. The remaining scalar anticommutator is
\[
\langle Af,Ag\rangle+\langle\overline{Bg},\overline{Bf}\rangle
=\langle f,(A^2+B^2)g\rangle=\langle f,g\rangle.
\]
The anticommutator without an adjoint is zero. Thus (12) is a CAR representation. We will identify its vacuum state with the state constructed from the finite densities.

**Theorem 4.1.** There is exactly one state with the normal-ordered moments
\[
\omega_T\!\left(a(f_1)^*\cdots a(f_n)^*
a(g_m)\cdots a(g_1)\right)
=\begin{cases}
\det[\langle g_i,Tf_j\rangle]_{i,j=1}^n,&m=n,\\
0,&m\ne n.
\end{cases} \tag{13}
\]
It is invariant under the gauge action \(\alpha_{e^{i\theta}1}\), and hence even. These states are called gauge-invariant quasi-free states.

**Proof.** Compute first in an eigenbasis \(h_1,\ldots,h_d\) of \(S_E\). A normal word with a repeated creation or annihilation index is zero. A word with different creation and annihilation index sets changes the occupation set, so has zero diagonal expectation under \(\rho_E\). If the sets agree, move each list into increasing order. The two sorting signs are also the row and column signs of the diagonal-covariance determinant. The resulting word is \(\prod_{j\in I}a(h_j)^*a(h_j)\), whose expectation is \(\prod_{j\in I}p_j\). The empty product is one. Multilinearity, with creation linear and annihilation conjugate-linear, proves (13) on \(\operatorname{CAR}(E)\) with entries \(\langle g_i,S_Ef_j\rangle=\langle g_i,Tf_j\rangle\).

Formula (11) now makes this finite state independent of the chosen eigenbasis. If \(E\subset F\), restriction of \(\varphi_F\) to \(\operatorname{CAR}(E)\) has exactly those same normal moments and is therefore \(\varphi_E\). Any two finite spaces lie in their finite sum. Consequently these states define a well-defined positive functional on the directed local union, with \(|\varphi(x)|\le\|x\|\) and \(\varphi(1)=1\). Extend it by norm continuity to \(\operatorname{CAR}(K)\). If local \(x_\lambda\to x\) in norm, then \(x_\lambda^*x_\lambda\to x^*x\); positivity of each finite density gives \(\omega_T(x^*x)\ge0\). This constructs an actual positive state for arbitrary \(K\). Uniqueness follows from (11). Under \(\alpha_{e^{i\theta}1}\), a normal word acquires the phase \(e^{i(n-m)\theta}\); its value in (13) is unchanged. Thus the state is gauge invariant and, at \(\theta=\pi\), even.

It remains to check the doubled model, independently of this existence argument. Second quantization of \(e^{i\theta}1_{K_0}\oplus e^{-i\theta}1_{\overline{K_1}}\) fixes the vacuum and multiplies (12) by \(e^{-i\theta}\), so its unbalanced moments vanish. In a balanced word, the creator component of the leftmost adjoint in (12) has zero expectation against the left vacuum. The other component is \(a_{\mathcal L}(0\oplus\overline{Bf_1})\). Move it to the right; its scalar anticommutators with the remaining adjoints vanish. Against the generator labelled \(g_i\), its scalar term is
\[
\langle\overline{Bf_1},\overline{Bg_i}\rangle
=\langle g_i,Tf_1\rangle.
\]
Moving past the intervening letters gives the sign \((-1)^{i+1}\). The final annihilator kills the right vacuum. This is the expansion along the first column of (13); induction from the empty word proves all its moments. By uniqueness, this vector state is the finite-density state just constructed. The full contraction induction, including unbalanced words, is in [Section 11.2](#11-2-all-determinant-signs-including-unequal-lengths). \(\square\)

The state with \(T=0\) is the ordinary annihilation vacuum. With \(T=1\) the representation in (12) is the filled, or anti-Fock, representation. For finite-dimensional \(E\subset K\), restriction to \(\operatorname{CAR}(E)\) has covariance \(P_ET|_E\); \(E\) need not reduce \(T\). This follows directly by restricting the entries of (13).

The vacuum is cyclic for (12), including when \(T\) has a kernel or a one-eigenspace. Indeed the one-particle creation components of its generators and adjoints span densely
\[
AK\oplus\overline{BK}\subset\mathcal L.
\]
Products of such operators applied to the vacuum give the desired wedge of their creation components plus terms of smaller particle degree. Inductively all those smaller-degree terms lie in the closed cyclic subspace; subtracting them puts the wedge there too. By continuity and the occupation basis, these wedges span all of \(\mathcal F(\mathcal L)\). On the state quotient, the map \([x]\mapsto\pi_T(x)\Omega\) preserves inner products \(\omega_T(x^*y)\), kills exactly the null space, and intertwines multiplication on its whole dense domain. Its extension to the completed quotient is an onto unitary by the just proved cyclicity. Thus (12) with its vacuum is the completed state GNS representation. This also proves the asserted identification at the covariance endpoints; [Sections 11.3–11.4](#11-3-the-whole-reduced-doubled-fock-space-is-cyclic) give the full dense-degree and completion estimates.

## 5. Why the quasi-free representation is a factor

The implication from cyclic irreducibility to purity used in Exercise 8 can be proved on the same completed quotient. If a positive functional \(\psi\) satisfies \(0\le\psi\le\omega_T\), its form \(B([x],[y])=\psi(x^*y)\) is well-defined and bounded there: positive-form Cauchy–Schwarz gives \(|B([x],[y])|^2\le\omega_T(x^*x)\omega_T(y^*y)\). Riesz representation produces \(0\le D\le1\) with \(B(\xi,\eta)=\langle\xi,D\eta\rangle\). The equality \(B(\pi_T(a^*)\xi,\eta)=B(\xi,\pi_T(a)\eta)\) for every algebra element \(a\) makes \(D\) commute with the representation. If it is irreducible, \(D=\lambda1\), so \(\psi=\lambda\omega_T\). Applied to the dominated functional \(t\psi_1\) in a nontrivial state decomposition \(\omega_T=t\psi_1+(1-t)\psi_2\), evaluation at \(1\) gives \(\lambda=t\) and \(\psi_1=\psi_2=\omega_T\). Thus the state is pure. The bounded-form and Riesz constructions are supplied in [Section 18.5](#18-5-full-concrete-vector-realization-under-vector-domination) and [ITP Section 10.2](infinite-tensor-products.md#10-2-riesz-representation-adjoints-and-the-operator-c-identity); this implication needs no converse criterion.

Let \(M_T=\pi_T(\operatorname{CAR}(K))''\) on this cyclic Fock space. The following argument does not require diagonalizing \(T\), a separable \(K\), or a faithful state.

Split off the endpoint spaces and write
\[
K_{\rm m}=(\ker T\oplus\ker(1-T))^\perp.
\]
Both \(A\) and \(B\) preserve this middle space. For \(f\in K_{\rm m}\) define the complementary field
\[
b(f)=a_{\mathcal L}(Bf\oplus0)
-c_{\mathcal L}(0\oplus\overline{Af}). \tag{14}
\]
Every field in (12), and its adjoint, anticommutes with every \(b(f)\) and \(b(f)^*\). For the mixed adjoint anticommutator, the only possible scalar terms cancel because
\[
\langle Ag,Bf\rangle-\langle Bg,Af\rangle=0;
\]
here \(AB=BA\). All other terms vanish by orthogonality of the legs and the CAR.

Let \(P\) be Fock parity, acting as \((-1)^n\) on \(\Lambda^n\mathcal L\). It anticommutes with every annihilator and creator, so each \(Pb(f)\) commutes with (12) and its adjoint. Thus
\[
Pb(f)\in M_T'. \tag{15}
\]
The untwisted families \(\pi_T(a(g))\) and \(b(f)\) together generate all ordinary Fock fields. On the middle space,
\[
a_{\mathcal L}(f\oplus0)=\pi_T(a(Af))+b(Bf),\qquad
c_{\mathcal L}(0\oplus\bar f)=\pi_T(a(Bf))-b(Af). \tag{16}
\]
The cancellation again uses \(AB=BA\), and the remaining coefficients are \(A^2+B^2=1\). On \(\ker T\), the first-leg field is already (12); on \(\ker(1-T)\), the second-leg creator is already (12). These spaces and the middle space span the active legs \(\mathcal L\). Lemma 1.1 therefore makes the joint untwisted family irreducible.

**Theorem 5.1.** \(M_T\) is a factor for every positive contraction \(T\).

**Proof.** Parity preserves \(M_T\), since it sends each generator to its negative, and hence preserves its center. If a central \(x\) is even, it commutes with \(P\). It also commutes with every \(Pb(f)\), because \(x\in M_T\) and (15) holds. These two commutations imply that \(x\) commutes with every \(b(f)\). Centrality supplies commutation with (12). Irreducibility of the joint family makes \(x\) scalar.

Every central element splits into its even and odd parts under \(x\mapsto PxP\). If the odd part of the center were nonzero, one of its real or imaginary parts would give a nonzero selfadjoint odd central \(z\). Its square is even and central, hence a scalar \(c1\), with \(c=\|z\|^2>0\). Rescale so that \(z^2=1\). For any odd central \(w\), the product \(zw\) is even and scalar, so \(w\) is a scalar multiple of \(z\). The center would therefore be exactly \(\mathbb C1+\mathbb Cz\).

Let \(V_\theta=e^{i\theta}1_{K_0}\oplus e^{-i\theta}1_{\overline{K_1}}\) and let \(U_\theta=\Gamma(V_\theta)\) be its degreewise second quantization. On a finite occupation vector with \(r\) first-leg and \(s\) second-leg entries, \(U_\theta\) has scalar \(e^{i(r-s)\theta}\). Continuity on finite linear combinations and their density, with \(\|U_\theta\|=1\), prove strong continuity on the entire Fock space, without a countability assumption on its basis. The defining creator formula gives \(U_\theta\pi_T(a(f))U_\theta^*=e^{-i\theta}\pi_T(a(f))\), so conjugation preserves \(M_T\) and its center; it commutes with parity. It is concretely normal, since conjugation transforms each summand in a square-summable vector-coefficient functional into another such summand.

For the normalized odd \(z\), conjugation must therefore give \(U_\theta zU_\theta^*=\varepsilon(\theta)z\), where \(\varepsilon(\theta)\in\{1,-1\}\): the odd central space is one-dimensional, and selfadjointness and \(z^2=1\) force this sign. Strong continuity at zero makes \(\varepsilon(\theta)=1\) for all sufficiently small \(|\theta|\). Indeed, for a fixed nonzero \(\xi\), the alternative sign would make \(\|(U_\theta zU_\theta^*-z)\xi\|=2\|\xi\|\). For any real \(\theta\), choose an integer \(n\) with \(\theta/n\) in that neighbourhood. The group law gives \(\varepsilon(\theta)=\varepsilon(\theta/n)^n=1\). But \(V_\pi=-1\) on both active legs, so \(U_\pi=P\), which sends the odd \(z\) to \(-z\). This contradiction removes the odd center. The even center was scalar, so \(\mathcal Z(M_T)=\mathbb C1\). [Section 13](#13-factorality-for-every-positive-contraction) supplies the full endpoint and complementary-field verification. \(\square\)

The twisted fields were used only to control the center. We have not assumed, or needed, that they generate the whole commutant.

## 6. Finite-dimensional approximation and product states

**Theorem 6.1.** For separable \(K\), every representation of \(\operatorname{CAR}(K)\) generates an AFD von Neumann algebra. In particular every \(M_T\) is an AFD factor. For arbitrary \(K\), the same proof gives an increasing directed family of finite-dimensional subalgebras with strong* dense union.

**Proof.** For any representation \(\pi\) put \(e=\pi(1)\) and
\[
D_E=\pi(\operatorname{CAR}(E))+\mathbb C(1-e),
\qquad A_0=\bigcup_{E\subset K,\ \dim E<\infty}D_E.
\]
On \(eH\), Theorem 2.1 gives a finite full matrix algebra; the complementary block is scalar. Thus every \(D_E\) is a finite-dimensional unital algebra on the full representation space. The matrix-unit coefficients recover its finitely many entries, so a WOT limit of elements of \(D_E\) again lies in \(D_E\). These are finite-dimensional von Neumann subalgebras. They increase with \(E\). Polynomial norm density and continuity of \(\pi\) give \(A_0''=\pi(\operatorname{CAR}(K))''\); adjoining \(1-e\) adds no commutation condition, since a commutant already commutes with \(e\).

Here is the bounded approximation step. The finite-vector amplification proof of the bicommutant theorem in [ITP Section 10.5](infinite-tensor-products.md#10-5-the-unital-bicommutant-theorem-by-finite-vector-amplification) makes \(A_0\) WOT dense in \(A_0''\). Apply it simultaneously to the finite lists \(x\xi_j\) and \(x^*\xi_j\). Their image set as \(x\) runs over \(A_0\) is a real linear subspace of a finite Hilbert direct sum. If the desired tuple were outside its norm closure, orthogonal projection would separate it by a real continuous functional. That functional is a finite sum of WOT coefficients of \(x\) and \(x^*\), hence is WOT continuous as a real functional. This would contradict WOT density. Consequently every \(z\in A_0''\) has a net \(x_\lambda\in A_0\) tending strongly* to it.

To retain an exact norm bound, use
\[
F(x)=2x(1+x^*x)^{-1}.
\]
The geometric inverse stays in the same complete local algebra as \(x\), and
\[
1-F(x)^*F(x)
=(1+x^*x)^{-1}(1-x^*x)^2(1+x^*x)^{-1}\ge0.
\]
Thus \(F(x)\) is a contraction. For \(R_z=(1+z^*z)^{-1}\), the inverse identity in [Section 14.2](#14-2-elementary-inverses-and-a-bounded-rational-map) gives
\[
\tfrac12\|(F(x)-F(z))\xi\|
\le\|(x-z)R_z\xi\|
+\tfrac12\|(z^*-x^*)zR_z\xi\|.
\]
The same inequality for adjoints proves strong* continuity at each fixed \(z\), even for nets with no common norm bound. If \(y\in A_0''\) is a contraction, put \(s=(1-y^*y)^{1/2}\) and \(G(y)=y(1+s)^{-1}\). Commuting multiplication gives \(1+G(y)^*G(y)=2(1+s)^{-1}\), hence \(F(G(y))=y\). Choose the preceding local strong* net toward \(G(y)\); its images under \(F\) are local contractions tending strongly* to \(y\). Scaling proves bounded strong* density at every radius.

For separable \(K\), choose finite-dimensional \(E_n\) increasing to a dense subspace. Their generator union is norm dense by (5), so the same proof uses the increasing sequence \(D_{E_n}\). This is AFD by a sequence of finite algebras; the approximating operators can still require nets when the representation space is nonseparable. For arbitrary \(K\), all finite subspaces give the asserted directed family. When \(e=0\), all the \(D_E\) are scalar; when \(H=0\), the assertion is immediate. Factorality for \(\omega_T\) is Theorem 5.1. The complete approximation argument is in [Section 14](#14-directed-finite-dimensional-approximation-in-every-car-representation). \(\square\)

If \(K=\bigoplus_jK_j\) and \(T\) reduces each \(K_j\), (13) proves the full finite-block product identity
\[
\omega_T(x_1\cdots x_r)=\prod_{\ell=1}^r\omega_T(x_\ell),
\qquad x_\ell\in\operatorname{CAR}(K_{j_\ell}),
\quad j_\ell\text{ distinct}. \tag{17}
\]
To see it, put each local polynomial in normal order and expand into basis vectors in its own block. Cross-block contractions vanish. A nonzero determinant term requires equal numbers of creators and annihilators in every block; then each block word is even. Regrouping those balanced blocks contributes no sign, and the determinant splits into their determinants. If some block is unbalanced, both sides vanish. Density extends (17) to arbitrary local elements. Thus reducing spectral blocks give product states. Merely pairwise independence would be weaker than (17).

For a finite-dimensional subspace \(E\), use the eigenvalues \(p_1,\ldots,p_d\) of its compression \(S_E=P_ET|_E\). The occupation basis gives the density matrix
\[
\rho_T=\bigotimes_{j=1}^d
\begin{pmatrix}1-p_j&0\\0&p_j\end{pmatrix},
\qquad
\omega_T(x)=\operatorname{Tr}(\rho_Tx). \tag{18}
\]
Here \(\rho_T\) denotes the density of the restriction to \(\operatorname{CAR}(E)\) in this finite basis. The entire diagonal normal-word computation was used in Theorem 4.1; it proves (18) even when \(E\) does not reduce \(T\). When a family of spaces does reduce \(T\), (17) additionally gives compatibility with its block product.

For a countable eigenbasis the compatible Jordan–Wigner identifications (7), together with (18), give a normal GNS identification
\[
M_T\cong\bigotimes_{j=1}^\infty
\left(M_2,\ x\mapsto\operatorname{Tr}
\left(\begin{pmatrix}1-p_j&0\\0&p_j\end{pmatrix}x\right)\right).
\tag{19}
\]
For completeness, set \(\rho_j=\operatorname{diag}(1-p_j,p_j)\), let \(s_j\) be its support projection, and take the finite Hilbert space
\[
H_j=M_2s_j,\qquad \langle X,Y\rangle=\operatorname{Tr}(X^*Y),
\qquad \Omega_j=\rho_j^{1/2},
\]
with left matrix action. Its cyclic span is all \(H_j\): every supported column matrix equals \(x\rho_j^{1/2}\), by inversion only on the positive diagonal entries. This includes the rank-one endpoint supports. Complete the increasing finite tensor spaces under the embeddings \(\xi\mapsto\xi\otimes\Omega_{n+1}\). For local \(x,y\), (18) gives the exact inner product
\[
\langle x\Omega,y\Omega\rangle
=\operatorname{Tr}(\rho_1\otimes\cdots\otimes\rho_n\,x^*y)
=\omega_T(x^*y).
\]
The map from the CAR cyclic quotient \([x]\) to \(x\Omega\) is therefore isometric, respects all compatible local embeddings, and intertwines every generator. Local cyclicity gives dense range in the pointed completion, so its extension is an onto unitary from the whole completed GNS space. By boundedness and norm density it intertwines every CAR element. Taking commutants twice gives (19) on every element of the generated von Neumann algebras, with inverse. Both directions are concretely normal: conjugation carries a square-summable vector-coefficient functional to the series with both vector lists conjugated, preserving their sums of squared norms. [Sections 15.3–15.8](#15-3-the-cyclic-one-mode-matrix-model-including-endpoints) give the complete bridge, including finite and endpoint cases.

At \(T=\tfrac12 1\), every finite restriction is normalized matrix trace. A finite matrix trace is unique: traciality makes all diagonal matrix-unit values equal and makes every off-diagonal value zero. Norm density therefore makes \(\omega_{1/2}\) the unique tracial state on the CAR algebra. Its vector extension \(\tau(x)=\langle\Omega,x\Omega\rangle\) on \(M_{1/2}\) is tracial on every pair \(x,y\): choose uniformly bounded local strong* nets for both; the estimate
\[
\|(x_\lambda y_\mu-xy)\xi\|
\le\|x_\lambda\|\|(y_\mu-y)\xi\|+\|(x_\lambda-x)y\xi\|
\]
and its adjoint counterpart pass their finite trace identity to the joint directed limit. The vector functional is concretely normal. It is faithful: if \(\tau(x^*x)=0\), then for \(y\in M\),
\[
\|xy\Omega\|^2=\tau(y^*x^*xy)
=\tau(x^*xyy^*)\le\|y\|^2\tau(x^*x)=0.
\]
Cyclicity gives \(x=0\). The displayed inequality does not assert positivity of \(x^*xyy^*\): traciality rewrites its value as \(\tau(xyy^*x^*)\), and \(0\le xyy^*x^*\le\|y\|^2xx^*\). If a partial isometry had initial \(1\) and proper final projection \(q<1\), traciality would give \(\tau(1-q)=0\), contradicting faithfulness. Thus the factor is finite.

To justify its type when \(K\) is infinite-dimensional, suppose it had a minimal projection \(q\). Positive parts and their support projections make \(qMq=\mathbb Cq\). Every nonzero projection \(r\) then contains a projection equivalent to \(q\): factor contact gives \(0\ne rMq\), and polar decomposition of such an element has initial projection \(q\) and final projection below \(r\). A maximal orthogonal family of copies of \(q\) has at most \(1/\tau(q)\) members, since each has the same strictly positive trace. Its complement must vanish by the preceding contact argument. Partial isometries between this finite family give matrix units; every corner between two members is scalar because \(qMq=\mathbb Cq\). Hence \(M\) would be a finite full matrix algebra. This contradicts its local subalgebras \(M_{2^d}\) for arbitrarily large \(d\). An abelian projection in a factor would have scalar corner, because that corner is itself a factor, and hence would be minimal. There are therefore no nonzero abelian projections, while \(1\) is finite. This is exactly type \(\mathrm{II}_1\). The projection, contact and finite-matrix arguments are fully supplied in [Section 16](#16-the-half-state-trace-and-the-type-ii1-conclusion). They use no separability of \(K\). In the separable infinite-dimensional case (19) is exactly the tracial infinite product of \(M_2\).

For \(T=p1\), \(0<p<1\), on separable infinite-dimensional \(K\), we now prove directly that
\[
M_p\text{ is not semifinite if }p\ne\tfrac12. \tag{20}
\]
Use (19) with \(\rho=\operatorname{diag}(1-p,p)\), and denote the pointed product algebra by \(M\). Its left and right finite matrix orbits of \(\Omega=\bigotimes\rho^{1/2}\) are dense, since \(\rho\) is invertible. Let \(X_j=E_{12}^{(j)}\) be the left matrix in coordinate \(j\); in the CAR model it is the parity-corrected mode \(b_j\) of (6), not the odd mode with its prefix string. Right multiplication in that coordinate by \(\rho^{-1/2}E_{12}\rho^{1/2}\) gives an operator \(R_j\in M'\) with
\[
X_j\Omega=R_j\Omega,\qquad
\|R_j\|\le C(p)=\sqrt{\frac{\max(p,1-p)}{\min(p,1-p)}}.
\]
For \(u\in M\), choose a left-local \(z\) with \(\|(u-z)\Omega\|<\varepsilon\). Beyond its finite support, \(z\) commutes with \(X_j\), so
\[
\|[u,X_j]\Omega\|\le(C(p)+1)\varepsilon.
\]
On every right-local \(r\Omega\), the commutator equals \(r[u,X_j]\Omega\). These vectors are dense, and \(\|[u,X_j]\|\le2\|u\|\); therefore \([u,X_j]\to0\) strongly on the entire Hilbert space. The same argument for \(X_j^*\) gives the adjoint limit. On pairs of finite-stage vectors, the untouched reference tail gives
\[
X_j^*X_j\longrightarrow p1,\qquad
X_jX_j^*\longrightarrow(1-p)1\quad\text{in WOT}.
\]
Their norm-one bounds extend these coefficient limits to arbitrary vectors.

Suppose \(M\) had a nonzero finite projection \(e\). The corner \(eMe\) is a finite factor on the separable space \(eH\). The complete finite-factor construction in [Sections 18–19](#18-order-normal-positive-functionals-and-the-concrete-ultraweak-topology) supplies a faithful concretely normal tracial state \(\vartheta\) on this corner, with \(\vartheta(e)=1\); no trace on all of \(M\) is assumed. Put \(B_j=eX_je\). The strong commutator limits with \(u=e\) give
\[
\begin{aligned}
eX_j^*X_je-B_j^*B_j&=eX_j^*(1-e)X_je\longrightarrow0,\\
eX_jX_j^*e-B_jB_j^*&=eX_j(1-e)X_j^*e\longrightarrow0
\end{aligned}
\quad\text{strongly}.
\]
For example, the first difference on \(\xi\) has norm at most \(\|(1-e)[X_j,e]\xi\|\). Consequently \(B_j^*B_j\to pe\) and \(B_jB_j^*\to(1-p)e\) in WOT, with a common norm bound. Concrete normality passes \(\vartheta\) through these bounded limits: truncate its square-summable coefficient series, pass the finite head through WOT, and bound the remaining tail uniformly by Cauchy–Schwarz. Traciality now gives
\[
p=\lim_j\vartheta(B_j^*B_j)
=\lim_j\vartheta(B_jB_j^*)=1-p.
\]
For \(p\ne1/2\) this is impossible. Thus \(0\) is the only finite projection. By the type definitions, \(M\) is type III and its nonzero identity summand makes it not semifinite. The onto unitary in (19) transports every projection and partial isometry, proving (20) for \(M_p\). [Section 20](#20-constant-faithful-car-states-have-no-nonzero-finite-projection-away-from-half) supplies the entire finite-corner argument with its trace and continuity inputs.

We can also compute the modular inner-time group without a general infinite-product overlap criterion:
\[
\{t:\sigma_t^{\omega_p}\text{ is inner}\}
=\frac{2\pi}{\log(p/(1-p))}\mathbb Z. \tag{21}
\]
Put \(a=1-p\), \(b=p\), \(v=\rho^{it}\), and \(v_n=v^{\otimes n}\). The completed diagonal Tomita graph in [ITP Sections 11.4–11.8](infinite-tensor-products.md#11-4-positive-diagonal-operators-exact-adjoints-and-graph-cores) gives \(\sigma_t|_{A_n}=\operatorname{Ad}v_n\) on the left finite algebra \(A_n\). Its actual product expectations \(E_n:M\to A_n\) are bimodular contractions, satisfy \(E_nE_m=E_n\) for \(m\ge n\), and give \(E_n(x)\Omega=P_nx\Omega\to x\Omega\). These assertions are proved by finite Hilbert-space compression, not assumed as an abstract expectation theorem.

If \(\sigma_t=\operatorname{Ad}u\) with \(u\in M\) unitary, bimodularity implies that \(v_n^*E_n(u)\) commutes with \(A_n\). Its center is scalar, so \(E_n(u)=\lambda_nv_n\), with \(|\lambda_n|\le1\). For \(m\ge n\), compatibility and the reference-tail trace give
\[
\lambda_n=\lambda_m c^{m-n},\qquad
c=\operatorname{Tr}(\rho v)=a\,a^{it}+b\,b^{it}.
\]
If \(|c|<1\), geometric decay makes every \(\lambda_n=0\), contrary to \(E_n(u)\Omega\to u\Omega\) and \(\|u\Omega\|=1\). The elementary identity
\[
|c|^2=1-ab|a^{it}-b^{it}|^2
\]
therefore forces \(a^{it}=b^{it}\). Conversely, when those phases coincide, the completed matrix-unit tensor basis has modular phase one on every entry. Hence \(\Delta^{it}=1\) on the whole pointed Hilbert space, and \(\sigma_t\) is the identity on \(M\). The pointed unitary in (19) transports the entire initial Tomita graph \(x\Omega\mapsto x^*\Omega\), its closure, adjoint and diagonal powers to the actual CAR representation; innerness transfers in both directions. Finally the scalar exponential calculation in [Section 17.1](#17-the-exact-inner-times-of-the-faithful-constant-car-state) gives \(t\log(a/b)\in2\pi\mathbb Z\). Since \(\log(a/b)=-\log(p/(1-p))\), its integer-multiple subgroup is exactly (21). [Sections 17.2–17.7](#17-2-the-exact-pointed-algebra-and-its-finite-expectations) supply this proof on the whole algebra.

Equation (21) alone does not prove the finer designation \(\mathrm{III}_{p/(1-p)}\) for \(p<1/2\). [Constant CAR states and the periodic core](constant-car-states-and-the-periodic-core.md) proves the factorial centralizer and computes the center flow; its explicitly stated modular-invariant input then gives this parameter. Equations (20)–(21) concern separable infinite-dimensional \(K\) with \(0<p<1\); in finite dimension the algebra remains a matrix factor. The endpoints lack the invertible reference density used by the tail and modular arguments, and the half-state has its separate type \(\mathrm{II}_1\) proof.

## 7. Problems with complete solutions

**Exercise 1.** For a two-dimensional one-particle space, compute the four occupation basis vectors and the actions of \(c(e_2)\) and \(a(e_2)\), including their signs.

*Solution.* The occupation sets \(\varnothing,\{1\},\{2\},\{1,2\}\) give the orthonormal basis
\[
\Omega,\quad e_1,\quad e_2,\quad
[e_1,e_2]=\frac{e_1\otimes e_2-e_2\otimes e_1}{\sqrt2}.
\]
Insert \(e_2\) at the front for creation, and remove its entry using (4) for annihilation:
\[
\begin{array}{c|rrrr}
\eta&\Omega&e_1&e_2&[e_1,e_2]\\ \hline
c(e_2)\eta&e_2&-[e_1,e_2]&0&0\\
a(e_2)\eta&0&0&\Omega&-e_1
\end{array}
\]
The repeated-vector wedge is zero. The other minus signs come from moving \(e_2\) past the earlier occupied \(e_1\). Each nonzero row sends two orthonormal vectors to two orthonormal vectors and kills their orthogonal complement, so both operators are partial isometries of norm one. The table also verifies that they are adjoints.

**Exercise 2.** On the two-mode algebra, write \(a_1,a_2\) in tensor coordinates, and explain why the ordinary commutator \([a_1,a_2]\) need not vanish.

*Solution.* In each one-mode occupation basis let
\[
s=E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
The first mode has no prefix string, while the second has the first mode's parity:
\[
a_1=s\otimes1,\qquad a_2=Z\otimes s.
\]
Matrix multiplication gives \(sZ=-s\) and \(Zs=s\). Hence
\[
a_1a_2=-s\otimes s,\qquad a_2a_1=s\otimes s,\qquad
[a_1,a_2]=-2s\otimes s\ne0.
\]
Their anticommutator is zero, exactly as the CAR require. Removing the parity prefix yields \(b_2=(Z\otimes1)a_2=1\otimes s\); this operator commutes with \(a_1\). Thus the ordinary commuting tensor modes are the \(b_j\), whereas the \(a_j\) retain the anticommuting parity strings.

**Exercise 3.** Exhibit an infinite-dimensional representation space whose CAR algebra is only \(M_2\). Identify the hypothesis that makes (7) valid.

*Solution.* Choose \(K=\mathbb C\) and \(H=\mathbb C^2\otimes\ell^2\), and use the one-mode matrix \(s=E_{12}\). Define
\[
a(z)=\bar z(s\otimes1)\qquad(z\in K).
\]
Then \(a(z)a(w)+a(w)a(z)=0\), while
\[
a(z)a(w)^*+a(w)^*a(z)
=\bar zw\,(ss^*+s^*s)\otimes1
=\langle z,w\rangle1.
\]
The four one-mode matrix units generated by \(s\otimes1\) span precisely \(M_2\otimes1\). The map \(X\mapsto X\otimes1\) is isometric, so this algebra is \(M_2\), despite its infinite-dimensional representation space. Formula (7) instead assumes that the one-particle space \(K\) is separable and infinite-dimensional: a countable infinite basis supplies infinitely many distinct tensor modes. A finite-dimensional \(K\) gives \(M_{2^{\dim K}}\); representation multiplicity does not increase that mode count.

**Exercise 4.** In one mode, evaluate the vacuum expectations of \(a^*a\) and \(aa^*\). If the generator is instead the linear creator \(c=a^*\), what covariance parameter does the expectation of \(c^*c\) have?

*Solution.* Take the empty and occupied basis vectors as \(e_1,e_2\), so \(a=E_{12}\) and \(\Omega=e_1\). Then
\[
a^*a=E_{22},\qquad aa^*=E_{11},\qquad
\langle\Omega,a^*a\Omega\rangle=0,\qquad
\langle\Omega,aa^*\Omega\rangle=1.
\]
Equivalently \(a\Omega=0\), whereas \(c\Omega=e_2\) for the linear creator \(c=a^*\). With \(c\) as the generator in the placement \(c^*c\), one has \(c^*c=aa^*\), so the vacuum covariance parameter is \(1\). With the conjugate-linear annihilator and placement \(a^*a\), it is \(0\). Taking an adjoint changes both linearity and the covariance placement.

**Exercise 5.** Let \(u_\lambda\to1\) strongly on \(K\). Give a point-norm estimate for the image of the quadratic word \(a(f)^*a(g)\).

*Solution.* Put \(X=a(f)^*\), \(Y=a(g)\), \(X_\lambda=a(u_\lambda f)^*\) and \(Y_\lambda=a(u_\lambda g)\). Add and subtract \(XY_\lambda\):
\[
X_\lambda Y_\lambda-XY
=(X_\lambda-X)Y_\lambda+X(Y_\lambda-Y).
\]
The exact generator norm (5), adjoint isometry and unitarity of \(u_\lambda\) give
\[
\|\alpha_{u_\lambda}(a(f)^*a(g))-a(f)^*a(g)\|
\le\|(u_\lambda-1)f\|\|g\|
+\|f\|\|(u_\lambda-1)g\|.
\]
Strong convergence makes both vector errors tend to zero, so this quadratic word converges in norm. The estimate tests only \(f\) and \(g\); it requires no convergence of \(\|u_\lambda-1\|\).

**Exercise 6.** For \(K=\mathbb C^2\), take
\[
T=\begin{pmatrix}1/2&1/4\\1/4&1/2\end{pmatrix}.
\]
Compute \(\omega_T(n_1)\), \(\omega_T(n_2)\), and \(\omega_T(n_1n_2)\). Are the two coordinate subalgebras independent in this state?

*Solution.* The one-mode occupation values are the diagonal covariance entries:
\[
\omega_T(n_1)=\langle e_1,Te_1\rangle=\tfrac12,\qquad
\omega_T(n_2)=\langle e_2,Te_2\rangle=\tfrac12.
\]
Two CAR swaps put their product into the precise order of (13):
\[
n_1n_2=a_1^*a_1a_2^*a_2
=a_1^*a_2^*a_2a_1.
\]
The determinant then gives
\[
\omega_T(n_1n_2)=\det T=\tfrac14-\tfrac1{16}=\tfrac3{16}.
\]
Independence would give \(1/2\cdot1/2=1/4\). The actual difference is \(-1/16\), so even these two occupation projections disprove independence of the coordinate subalgebras. The obstruction is the off-diagonal covariance: \(Te_1=\tfrac12e_1+\tfrac14e_2\), so the first coordinate line, and likewise the second, does not reduce \(T\). Equal one-mode marginals do not determine their joint state.

**Exercise 7.** On a finite \(d\)-mode space, determine the dimension and matrix structure of the even algebra.

*Solution.* On the full matrix algebra \(B(\mathcal F(K))=M_{2^d}\), the parity automorphism is conjugation by \(P\), whose occupation eigenvalue is \((-1)^{|S|}\). An operator is fixed precisely when it preserves the two parity eigenspaces. For \(d\ge1\), toggling any fixed mode is a bijection between even and odd subsets of \(\{1,\ldots,d\}\), so each eigenspace has dimension \(2^{d-1}\). Therefore
\[
\operatorname{CAR}(K)_{\rm ev}
=M_{2^{d-1}}\oplus M_{2^{d-1}},\qquad
\dim_{\mathbb C}\operatorname{CAR}(K)_{\rm ev}
=2(2^{d-1})^2=2^{2d-1}.
\]
In the same decomposition, the odd operators are exactly the two off-diagonal blocks. For \(d=0\), Fock space consists only of its vacuum: the even algebra is \(\mathbb C\) and the odd space is zero. This separate endpoint avoids applying the equal-block formula when there is no mode to toggle.

**Exercise 8.** For a projection \(T\), show directly that the quasi-free representation is irreducible and the state is pure.

*Solution.* There is no middle space: \(K_m=(\ker T\oplus\operatorname{ran}T)^\perp=0\). Since \(T^2=T=T^*\), its roots in (12) are \(B=T\) and \(A=1-T\), and the active one-particle space is
\[
\mathcal L=\ker T\oplus\overline{\operatorname{ran}T}.
\]
For \(f\in\ker T\), \(\pi_T(a(f))=a_{\mathcal L}(f\oplus0)\). For \(f\in\operatorname{ran}T\), it is \(c_{\mathcal L}(0\oplus\bar f)\). Adjoints consequently supply every creator and annihilator on both active legs. The representation is cyclic by Section 4, and its commutant is scalar by the ordinary Fock argument of Lemma 1.1. Thus it is irreducible, for arbitrary \(K\).

Here is the purity step explicitly. If \(\omega_T=t\psi_1+(1-t)\psi_2\), with \(0<t<1\), the dominated positive functional \(t\psi_1\le\omega_T\) defines on the completed cyclic quotient a bounded positive form
\[
B([x],[y])=t\psi_1(x^*y).
\]
Positive-form Cauchy–Schwarz bounds it by \(\|[x]\|\|[y]\|\), so it has a representing positive contraction \(D\), with \(B([x],[y])=\langle[x],D[y]\rangle\). The equality
\[
B(\pi_T(a)[x],[y])=B([x],\pi_T(a^*)[y])
\]
gives \(\pi_T(a^*)D=D\pi_T(a^*)\) on the dense cyclic quotient and hence on its completion. Thus \(D\) commutes with the representation. Irreducibility makes \(D=\lambda1\), hence \(t\psi_1=\lambda\omega_T\). Evaluating at \(1\) gives \(\lambda=t\), and therefore \(\psi_1=\psi_2=\omega_T\). There is no nontrivial state decomposition, so the state is pure. This conclusion uses irreducibility; the factor result alone also covers mixed quasi-free states.

**Exercise 9.** Take \(p=1/3\) on countably infinitely many modes. Determine whether the resulting factor is semifinite and compute its modular inner-time group. Contrast a system with exactly three modes.

*Solution.* The one-mode density is \(\rho=\operatorname{diag}(2/3,1/3)\). The ratio of the occupied to empty density phases is
\[
e^{it\log(1/2)}.
\]
It equals one exactly when \(t\log2\in2\pi\mathbb Z\). The finite-expectation argument of Section 6 makes this condition necessary and sufficient for the modular automorphism to be inner, so
\[
\{t:\sigma_t^{\omega_{1/3}}\text{ is inner}\}
=\frac{2\pi}{\log2}\mathbb Z.
\]

Replacing the generator \(2\pi/\log2\) by its negative leaves this subgroup unchanged.

For the type assertion, use the direct finite-corner proof there, or Section 20. A nonzero finite projection \(e\) would provide a normalized normal trace \(\vartheta\) on \(eM_{1/3}e\). For the parity-corrected tails \(X_j=E_{12}^{(j)}\), the compressed operators \(B_j=eX_je\) satisfy
\[
B_j^*B_j\longrightarrow\tfrac13e,\qquad
B_jB_j^*\longrightarrow\tfrac23e
\quad\text{in WOT},
\]
with a common norm bound. Normality and traciality would give \(1/3=2/3\). Hence there is no nonzero finite projection: the infinite factor is type III and is not semifinite.

The modulus-defect computation is also explicit. For
\(c(t)=\tfrac23(2/3)^{it}+\tfrac13(1/3)^{it}\),
\[
|c(t)|^2=1-\tfrac29|e^{it\log(1/2)}-1|^2.
\]
Away from the displayed time group, \(1-|c(t)|>0\) is the same at every coordinate, so its infinite sum diverges. Here the type conclusion has already been established by the finite-corner contradiction, without importing a general summability classification.

For exactly three modes, Theorem 2.1 gives \(M_8\). It has the ordinary finite matrix trace and is semifinite. Every automorphism is inner: its image matrix units construct an implementing orthonormal basis and unitary, as proved in Section 2. The infinite tail argument and infinite summability test are not finite-mode type criteria.

**Exercise 10.** On countably infinitely many modes, let
\(\psi=\tfrac12(\omega_0+\omega_1)\).
Show that it is not quasi-free, and that its generated von Neumann algebra is not a factor despite having AFD approximation.

*Solution.* Write \(n_j=a(e_j)^*a(e_j)\). The empty state has every occupation zero and the filled state has every occupation one. Hence
\[
\psi(n_j)=\tfrac12,\qquad
\psi(n_in_j)=\tfrac12\quad(i\ne j).
\]
More generally \(\psi(a(f)^*a(g))=\tfrac12\langle g,f\rangle\), so its occupation covariance in the stated adjoint placement is \(\tfrac12 1\), whereas (13) for that covariance gives \(\omega_{1/2}(n_in_j)=1/4\). Thus the mixture is not quasi-free.

Let \(\pi=\pi_0\oplus\pi_1\) and \(\Xi=(\Omega_0,\Omega_1)/\sqrt2\). This vector realizes \(\psi\). To identify its completed cyclic representation and its center, put
\[
q_N=\frac1N\sum_{j=1}^Nn_j.
\]
On an empty-state occupation vector indexed by a finite set \(S\), \(\pi_0(q_N)\) has eigenvalue \(|S\cap\{1,\ldots,N\}|/N\). On the filled representation, with \(S\) now the finite hole set, the eigenvalue is one minus that number. Thus for finite particle or hole vectors with at most \(k\) varying modes,
\[
\|\pi_0(q_N)\eta\|\le\frac{k}{N}\|\eta\|,\qquad
\|(1-\pi_1(q_N))\eta\|\le\frac{k}{N}\|\eta\|.
\]
Both \(q_N\) and \(1-q_N\) are contractions. Density extends these estimates to strong limits on the entire two summands:
\[
\pi(q_N)\longrightarrow z=0\oplus1.
\]
The generated von Neumann algebra contains \(z\) by strong closedness. It is a nonzero proper projection and commutes with every block-diagonal \(\pi(x)\), hence is central in \(\pi(A)''\).

The vector \(\Xi\) is cyclic on the whole direct sum. Indeed \(\pi(q_N)\Xi=(0,\Omega_1)/\sqrt2\) for every \(N\); subtracting this from \(\Xi\) gives \((\Omega_0,0)/\sqrt2\). Applying the algebra and using cyclicity in each component generates a dense span of both summands. Equivalently the cyclic quotient map \([x]\mapsto\pi(x)\Xi\), whose squared norm is \(\psi(x^*x)\), extends to an onto unitary. This is the mixture's GNS representation, so its central \(z\) proves nonfactorality there. Theorem 6.1 nevertheless gives AFD approximation, which does not force a represented state to be quasi-free or its algebra to be a factor.

## 8. The faithful constant-state completed GNS identification

This supplies the exact countable identical faithful \(T=pI\), \(0<p<1\), instance of formula (19) and the model identification used by [*Constant CAR states and the periodic core*, formula (2)](constant-car-states-and-the-periodic-core.md#1-the-constant-faithful-product-state). Its additional hypothesis \(p\ne\tfrac12\) is retained when this proof is used there. The proof itself includes \(p=\tfrac12\) and asserts no classification result.

The foundation boundary is ZFC, real and complex scalar completeness, elementary finite matrix algebra, finite permutations and determinants, and the definition of a Hilbert space with the specified countable complete orthonormal basis. The full concrete Hilbert/operator proofs are in [*Infinite tensor products and their reference states*, Sections 10.1–10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice); its [Sections 11.1–11.3](infinite-tensor-products.md#11-modular-action-of-the-faithful-identical-two-level-product) supply the faithful pointed matrix product and dense right orbit. Every additional CAR, state, density, quotient and completion step is proved below.

Inner products are linear in their second variable. Annihilation is conjugate linear and creation is linear in its one-particle argument. Concrete normality means ultraweak continuity for the square-summable coefficient topology defined in ITP Section 10.6.

### 8.1. A complete occupation model and its Fock identification

Let \(K\) have the specified countably infinite orthonormal basis \((e_j)_{j\ge1}\). Its finite coefficient map is an isometry from finite-support sequences onto the finite span of the \(e_j\). Completion and basis density identify \(K\) with \(\ell^2(\mathbb N)\). Let \(\mathcal F_{\mathrm{occ}}=\ell^2(\operatorname{Fin}(\mathbb N))\), the Hilbert completion of the finite-support vectors on the set of finite subsets of \(\mathbb N\), with orthonormal basis \(\delta_S\). This set is countable: the subsets with maximum at most \(n\) form a finite set, and their union contains every finite subset. Put \(\Omega_{\mathrm{vac}}=\delta_\varnothing\).

For each \(j\), set \(q_j(S)=|\{s\in S:s<j\}|\) and define on the basis
\[
 c_j\delta_S=\begin{cases}(-1)^{q_j(S)}\delta_{S\cup\{j\}},&j\notin S,\\0,&j\in S,\end{cases}
 \qquad
 a_j\delta_S=\begin{cases}(-1)^{q_j(S)}\delta_{S\setminus\{j\}},&j\in S,\\0,&j\notin S.\end{cases}                 \tag{PG1}
\]
These signed partial permutations are contractions on finite-support vectors and extend uniquely to the completion. Comparing basis coefficients gives \(a_j^*=c_j\). They have norm one. For the same index, \(a_j^2=c_j^2=0\), and \(a_jc_j+c_ja_j=1\), because exactly one of the two terms is the identity on each occupation vector.

For distinct \(i,j\), two removals are both possible precisely when both indices are present; otherwise both composed removals vanish. If \(i<j\) and both are present, removing \(i\) decreases \(q_j\) by one, whereas removing \(j\) leaves \(q_i\) unchanged. The two nonzero coefficients therefore have opposite signs. For removal of \(i\) and insertion of \(j\ne i\), both orders are possible precisely when \(i\in S\) and \(j\notin S\). If \(i<j\), removal of \(i\) changes \(q_j\) by one; if \(j<i\), insertion of \(j\) changes \(q_i\) by one. In either case the coefficients have opposite signs. Taking adjoints covers two insertions. Thus
\[
 \{a_i,a_j\}=0,\qquad \{a_i,a_j^*\}=\delta_{ij}1.               \tag{PG2}
\]

For finite-support \(f=\sum f_je_j\), define \(a(f)=\sum\overline{f_j}a_j\). Finite expansion gives \(a(f)^2=0\) and
\(a(f)a(f)^*+a(f)^*a(f)=\|f\|^2 1\), as well as the two-vector CAR. If \(f\ne0\), let \(d=a(f)/\|f\|\). Then \(d^2=0\), \(dd^*+d^*d=1\), and
\[
 (d^*d)^2=d^*(1-d^*d)d=d^*d.
\]
The projection \(d^*d\) is nonzero: if it vanished, the C*-identity would give \(d=0\), contradicting the displayed identity. A nonzero orthogonal projection has norm one (upper bound from orthogonal decomposition and lower bound on a unit vector in its range). The C*-identity yields \(\|a(f)\|=\|f\|\). The zero case is immediate. Approximation by finite-support vectors consequently defines \(a(f)\) for every \(f\in K\) by an operator-norm limit. The CAR and conjugate-linearity pass to this limit; in particular
\[
 \{a(f),a(g)\}=0,\qquad \{a(f),a(g)^*\}=\langle f,g\rangle 1,
 \qquad \|a(f)\|=\|f\|.                                    \tag{PG3}
\]

For precision, this occupation model is the antisymmetric Fock model used in the earlier lesson. On \(K^{\otimes r}\), the permutations \(U_\sigma\) are unitaries: their inner products agree on elementary tensors, whose span is dense, and the inverse permutation supplies the inverse. The finite sum
\(A_r=(r!)^{-1}\sum_{\sigma\in S_r}\operatorname{sgn}(\sigma)U_\sigma\)
is self-adjoint and idempotent by the finite group multiplication law, so its range \(\Lambda^r K\) is closed. The tensors of basis vectors form a complete orthonormal basis of \(K^{\otimes r}\): approximate each factor by finite sums and use a telescoping tensor expansion, then the definition of the tensor completion. Applying \(A_r\), repeated indices give zero; for every increasing \(j_1<\cdots<j_r\),
\[
 [e_{j_1},\ldots,e_{j_r}]=\sqrt{r!}\,A_r(e_{j_1}\otimes\cdots\otimes e_{j_r})
\]
has norm one, since its \(r!\) distinct tensor coefficients have magnitude \(1/\sqrt{r!}\). Different sets have disjoint tensor supports and are orthogonal. These vectors span densely the range of \(A_r\), since that range is the image of a dense tensor span under a bounded projection. Therefore \(\delta_{\{j_1,\ldots,j_r\}}\mapsto[e_{j_1},\ldots,e_{j_r}]\), with the empty vector mapped to the scalar vacuum, extends to an onto unitary
\(\mathcal F_{\mathrm{occ}}\to\bigoplus_{r\ge0}\Lambda^rK\).

The formula \(c(f)\eta=\sqrt{r+1}A_{r+1}(f\otimes\eta)\) agrees with (PG1) on this occupation basis. Indeed, for a permutation \(\tau\) of the last \(r\) slots, the finite group law gives \(A_{r+1}(1\otimes U_\tau)=\operatorname{sgn}(\tau)A_{r+1}\), so averaging shows \(A_{r+1}(1\otimes A_r)=A_{r+1}\). On a normalized \(r\)-particle basis vector the coefficient is therefore \(\sqrt{r+1}\sqrt{r!}=\sqrt{(r+1)!}\). A repeated index gives zero, and insertion into increasing order gives exactly \((-1)^{q_j(S)}\). Continuity on each fixed tensor degree extends this agreement from its basis span to the full degree. Agreement for arbitrary \(f\) follows by approximating \(f\), since the displayed fixed-degree tensor formula is continuous in \(f\), as is the bounded creator by (PG3). Thus the formula defines the same bounded creator on the full Fock direct sum, and the contraction is its adjoint. This proves the exact Fock identification without an implicit normalization or completeness claim.

Define \(A=\operatorname{CAR}(K)\) here as the concrete norm-closed unital *-algebra generated on this Fock space by all the \(a(f)\). If \(A_n\) is generated by \(a_1,\ldots,a_n\), then \(\bigcup_n A_n\) is norm dense in \(A\). Indeed finite-support annihilators approximate every annihilator in norm by (PG3); telescoping products then approximate each *-polynomial, and those polynomials define the generating norm closure.

### 8.2. Finite CAR algebras, matrix norms and compatible parity strings

The following finite argument holds for any bounded CAR family \(a_1,\ldots,a_n\) on a nonzero Hilbert space. Put
\[
 n_j=a_j^*a_j,\qquad Z_j=1-2n_j,\qquad
 b_j=Z_1\cdots Z_{j-1}a_j.                                  \tag{PG4}
\]
As above, \(n_j\) is a projection. For \(i\ne j\), moving \(a_i\) past each of the two factors of \(n_j\) gives two minus signs and no scalar contraction, so \(n_j\) commutes with \(a_i,a_i^*\). Thus the \(n_j\), and hence the \(Z_j\), commute. Each \(Z_j\) is a self-adjoint unitary. The one-mode identities are
\(a_jn_j=a_j\), \(n_ja_j=0\), \(a_ja_j^*=1-n_j\); they give \(Z_ja_j=a_j\), \(a_jZ_j=-a_j\), and anticommutation also with \(a_j^*\).

Each prefix in (PG4) commutes with its own \(a_j\). Hence \(b_j^2=0\), \(b_j^*b_j=n_j\), and \(b_jb_j^*=1-n_j\). For \(i<j\), cancel the common parity prefix in a product involving \(b_i\) and \(b_j\). In reversing the order, the \(a_i\) or \(a_i^*\) passes its own factor \(Z_i\) in the second prefix and acquires one minus sign, and then passes \(a_j\) or \(a_j^*\) and acquires a second minus sign. The remaining \(Z\)'s commute with these fields. Consequently the \(i\)- and \(j\)-mode \(b\)'s and their adjoints commute, for every choice of the two adjoint exponents.

In each mode the four operators
\[
 e^{(j)}_{00}=1-n_j,\quad e^{(j)}_{01}=b_j,\quad
 e^{(j)}_{10}=b_j^*,\quad e^{(j)}_{11}=n_j
\]
satisfy \(e_{rs}^{(j)}e_{tu}^{(j)}=\delta_{st}e_{ru}^{(j)}\), \((e_{rs}^{(j)})^*=e_{sr}^{(j)}\), and \(e_{00}^{(j)}+e_{11}^{(j)}=1\), by the preceding one-mode identities. Different-mode entries commute. For bit tuples \(\alpha,\beta\in\{0,1\}^n\), put \(E_{\alpha\beta}=\prod_{j=1}^n e^{(j)}_{\alpha_j\beta_j}\). Direct multiplication gives the full matrix-unit identities
\[
 E_{\alpha\beta}E_{\gamma\delta}=\delta_{\beta\gamma}E_{\alpha\delta},\quad
 E_{\alpha\beta}^*=E_{\beta\alpha},\quad
 \sum_\alpha E_{\alpha\alpha}=1.                             \tag{PG5}
\]

These identities also prove faithfulness and the matrix norm, without a general CAR norm or a simplicity theorem. Fix the all-zero tuple \(0\). The projection \(E_{00}\) is nonzero: if zero, \(E_{\alpha0}^*E_{\alpha0}=E_{00}=0\) gives \(E_{\alpha0}=0\) by the C*-identity, then \(E_{\alpha\alpha}=E_{\alpha0}E_{0\alpha}=0\) for every \(\alpha\), contradicting (PG5). Let \(Q=E_{00}H\ne\{0\}\). The map
\[
 V:\mathbb C^{2^n}\otimes Q\longrightarrow H,
 \qquad V(e_\alpha\otimes\eta)=E_{\alpha0}\eta
\]
is isometric because \(E_{0\alpha}E_{\beta0}=\delta_{\alpha\beta}E_{00}\). It is onto because every \(\xi\in H\) equals
\(\sum_\alpha E_{\alpha0}(E_{0\alpha}\xi)\), and each \(E_{0\alpha}\xi\in Q\). It conjugates \(\sum x_{\alpha\beta}E_{\alpha\beta}\) to \(X\otimes1_Q\). This amplification has norm \(\|X\|\): the upper bound is the tensor amplification bound of ITP10.4, and a unit \(\eta\in Q\) with vectors \(v\otimes\eta\) gives the lower bound. Thus the matrix-unit map is an isometric unital *-isomorphism onto its span. That span is closed (a Cauchy sequence corresponds to Cauchy matrix coefficients in finite dimension), contains the \(b_j\), and contains \(a_j=Z_1\cdots Z_{j-1}b_j\). Conversely all its entries are generated by the \(a_j\). It is exactly their generated C*-algebra.

Apply this to Section 8.1. Denote by \(\theta_n:A_n\to M_2^{\otimes n}\) the inverse matrix-unit identification. It sends \(b_j\) to \(E_{12}\) in coordinate \(j\), with indices \(0,1\) corresponding to the usual matrix indices \(1,2\). In particular
\[
 \theta_n(a_j)=Z^{\otimes(j-1)}\otimes E_{12}\otimes1^{\otimes(n-j)},
 \qquad Z=\operatorname{diag}(1,-1).                         \tag{PG6}
\]
The same expression in \(n+1\) coordinates is the old one tensored with \(1\). Because the generators determine the algebra, \(\theta_{n+1}(x)=\theta_n(x)\otimes1\) for all \(x\in A_n\). This is exact compatibility, including all parity prefixes, not merely agreement of dimensions.

### 8.3. The pointed product and the completed countable C*-identification

Use the concrete product of ITP11.1–11.3: \(H_0=M_2\) with Hilbert–Schmidt inner product \(\langle u,v\rangle=\operatorname{Tr}(u^*v)\) and unit vector \(\Omega_0=\rho^{1/2}\). Form the nested finite Hilbert tensor products \(H^{(n)}=H_0^{\otimes n}\), embedded by \(\xi\mapsto\xi\otimes\Omega_0\), and let \(H_\rho\) be the Hilbert completion of their union. The finite-coordinate left matrix algebra \(B_n=M_2^{\otimes n}\) acts on \(H_\rho=H^{(n)}\otimes H_{>n}\), using the grouping unitary proved in ITP11.2; \(B_{n+1}\) contains \(B_n\otimes1\). Write \(\Omega_\rho=\Omega_0^{\otimes\infty}\).

Left multiplication on \(M_d\) in Hilbert–Schmidt norm has the matrix operator norm. The upper bound follows by applying the matrix bound separately to each column and summing the squared norms. For the lower bound take a matrix with one column a unit vector \(v\); its image has Hilbert–Schmidt norm \(\|Xv\|\), and take the supremum over \(v\). Tensor amplification preserves this norm, by Section 8.2 or ITP10.4. Thus every \(\theta_n\), viewed as mapping into \(B_n\subset B(H_\rho)\), is isometric. Let \(B=\overline{\bigcup_n B_n}^{\|\cdot\|}\). Compatibility and isometry define \(\theta\) on \(\bigcup_n A_n\); taking Cauchy limits extends it uniquely to an isometric unital *-map
\[
 \theta:A\longrightarrow B.                                \tag{PG7}
\]
Products and adjoints pass to operator-norm limits. Its range is closed by completeness of \(A\), and contains the norm-dense local union of \(B\); it is onto. This proves the countable concrete C*-identification directly, without a universal CAR norm, an abstract tensor C*-norm, or an inductive-limit theorem.

The product vector state is \(\varphi(x)=\langle\Omega_\rho,x\Omega_\rho\rangle\). On \(B_n\), finite Hilbert tensor inner products give
\[
 \varphi(x)=\operatorname{Tr}(\rho_n x),\qquad
 \rho_n=\rho^{\otimes n}.                                   \tag{PG8}
\]
This follows first on elementary tensor matrices from \(\operatorname{Tr}(\rho^{1/2}x\rho^{1/2})=\operatorname{Tr}(\rho x)\), and then on their finite linear span. The finite states are compatible under \(x\mapsto x\otimes1\), since \(\operatorname{Tr}(\rho)=1\). Define the state on \(A\) by \(\omega=\varphi\circ\theta\).

### 8.4. The exact finite normal moments, with every occupation sign

In the standard tensor basis of \((\mathbb C^2)^{\otimes n}\), label a vector by the occupied set \(S\subset\{1,\ldots,n\}\), using \(e_2\) for an occupied site. Its density weight is \(w(S)=p^{|S|}(1-p)^{n-|S|}\). Formula (PG6) acts exactly as (PG1), because \(E_{12}e_2=e_1\) and each preceding occupied coordinate contributes the sign \(-1\).

For an increasing set \(I=(i_1<\cdots<i_k)\), put
\(C_I=a_{i_1}^*\cdots a_{i_k}^*\) and \(D_I=a_{i_k}\cdots a_{i_1}=C_I^*\). If \(I\subset S\) and \(R=S\setminus I\), execution of \(D_I\) removes \(i_1,\ldots,i_k\) in that order. All earlier removed \(I\)-indices are absent when the next sign is counted, so
\[
 D_I|S\rangle=\epsilon(I,R)|R\rangle,
 \qquad \epsilon(I,R)=(-1)^{\sum_{i\in I}|\{t\in R:t<i\}|}.
\]
Execution of \(C_I\) inserts \(i_k,\ldots,i_1\) in that order; earlier inserted indices are larger than the next one, so it has exactly the same sign. Hence \(C_ID_I=\prod_{i\in I}n_i\). If \(I\not\subset S\), both sides vanish on \(|S\rangle\), confirming the operator identity on the entire basis.

For increasing \(I,J\), a nonzero \(C_ID_J|S\rangle\) removes \(J\), then inserts \(I\), which must be disjoint from \(S\setminus J\). A diagonal coefficient requires \((S\setminus J)\cup I=S\), forcing \(I=J\). In particular unequal lengths have zero diagonal coefficient. When \(I=J\) has \(k\) entries,
\[
 \operatorname{Tr}(\rho_n C_ID_I)
 =\sum_{S\supset I}p^{|S|}(1-p)^{n-|S|}
 =p^k\sum_{R\subset I^c}p^{|R|}(1-p)^{n-k-|R|}=p^k.          \tag{PG9}
\]
The last finite sum is \((p+(1-p))^{n-k}=1\).

Repeated indices in either creator tuple or annihilator tuple give zero: same-type anticommutation moves repeats together, and their squares vanish. For a distinct tuple which is a permutation \(\pi\) of an increasing tuple, its creator product gains \(\operatorname{sgn}(\pi)\); the reversed annihilator product gains the same permutation sign by taking adjoints of that creator identity. Thus for arbitrary basis tuples the normal moment is zero unless the two sets match, in which case it is \(p^k\) times the product of their two permutation signs. This is exactly the determinant \(\det[p\delta_{g_i,f_j}]\), including repeated rows or columns, with the annihilation tuple reversed as displayed below.

For finite-support \(f_j,g_i\in K\), both this moment and the determinant are separately linear in the \(f_j\) and conjugate-linear in the \(g_i\). Expanding in the basis equates every term by the preceding basis-tuple calculation. Thus
\[
 \omega\big(a(f_1)^*\cdots a(f_r)^*a(g_s)\cdots a(g_1)\big)
 =\begin{cases}\det[p\langle g_i,f_j\rangle]_{i,j=1}^k,&r=s=k,\\0,&r\ne s.\end{cases}       \tag{PG10}
\]
The empty determinant is \(1\). All finite-support vectors in one such word fit into a sufficiently large initial coordinate block. For arbitrary vectors, choose finite-support approximations to each one. Formula (PG3) and a telescoping product estimate give norm convergence of the word, while its finitely many determinant entries converge. Since \(\omega\) is a bounded vector state, (PG10) extends to all \(f_j,g_i\in K\). No pairing or Wick theorem is used in this calculation.

### 8.5. Normal ordering proves state uniqueness on the whole algebra

Every *-polynomial in annihilators and creators is a linear combination of normal words, with all creators on the left. To prove termination explicitly, for a word count pairs consisting of an annihilator to the left of a creator. An adjacent such pair can be replaced by
\(a(f)a(g)^*=\langle f,g\rangle1-a(g)^*a(f)\).
The swapped word has the same length and one fewer such inversion; the scalar-contraction word has length two less. Induction first on word length, then on the nonnegative inversion count, terminates and proves the claim. The annihilators on the right can be labelled in the reversed order \(a(g_s)\cdots a(g_1)\) without changing any operator. These normal words span a norm-dense subspace of \(A\).

Consequently any two bounded states on \(A\) satisfying (PG10) agree on all of \(A\). This is a precise uniqueness argument for the given constant-\(p\) state; it does not silently import a general quasifree-state theorem. Section 8.3 and Section 8.4 already prove existence and positivity for this state. We next compare it to the earlier lesson's actual doubled-Fock construction, with that construction and its cyclicity also proved at this specialization.

### 8.6. The faithful constant-\(p\) doubled fields and their determinant moments

Let \(L=K\oplus\overline K\). In the conjugate Hilbert space, \(\langle\overline f,\overline g\rangle_{\overline K}=\langle g,f\rangle_K\), and \(f\mapsto\overline f\) is conjugate-linear. Use the countable ordered basis \((e_1\oplus0,0\oplus\overline e_1,e_2\oplus0,0\oplus\overline e_2,\ldots)\). Section 8.1 constructs its complete antisymmetric Fock space \(\mathcal F(L)\), vacuum \(\Omega_L\), and bounded annihilators \(a_L\) and creators \(c_L=a_L^*\), with their exact CAR. Define
\[
 d(f)=\sqrt{1-p}\,a_L(f\oplus0)+\sqrt p\,c_L(0\oplus\overline f).                          \tag{PG11}
\]
Both terms are conjugate-linear in \(f\). Different summands are supported on orthogonal one-particle subspaces. Expanding their CAR gives \(\{d(f),d(g)\}=0\) and
\[
 \{d(f),d(g)^*\}=(1-p)\langle f,g\rangle1+p\langle\overline g,\overline f\rangle1
 =\langle f,g\rangle1.
\]
The Section 8.1 projection argument therefore gives \(\|d(f)\|=\|f\|\). For each finite family \(d(e_1),\ldots,d(e_n)\), Section 8.2 supplies exactly the same faithful matrix-unit identification and matrix norm. It follows that the map \(a_j\mapsto d(e_j)\) defines an isometric unital *-map on \(A_n\). These maps agree on overlaps by the generators, and extend by norm limits to a faithful isometric *-representation \(\pi_D:A\to B(\mathcal F(L))\), satisfying \(\pi_D(a(f))=d(f)\) for all \(f\). There is no universal norm assumption in this extension.

Let \(\Psi(X)=\langle\Omega_L,X\Omega_L\rangle\) for \(X\in B(\mathcal F(L))\), and let \(\psi=\Psi\circ\pi_D\) be the state on \(A\). We calculate its normal moments directly. Write
\(F_j=c_L(f_j\oplus0)\), \(B_j=a_L(0\oplus\overline f_j)\), so \(d(f_j)^*=\sqrt{1-p}F_j+\sqrt p B_j\). A creator on the far left has zero vacuum expectation, because its adjoint kills the vacuum. An annihilator on the far right kills the vacuum. For a pure word \(d(g_s)\cdots d(g_1)\Omega_L\), only second-summand creators survive: a first-summand annihilator has zero scalar anticommutators with them and can be moved right until it kills the vacuum. Its surviving vectors have degree \(s\), so the vacuum expectation is zero for \(s>0\). The pure adjoint word similarly leaves only first-summand creators and has degree \(r\), so has zero expectation for \(r>0\). The empty word has expectation \(1\).

If \(r,s>0\), expand the leftmost \(d(f_1)^*\). Its first-summand creator contributes zero on the far left. Move its second-summand annihilator \(B_1\) through the remaining \(r-1\) adjoint fields; all those anticommutators vanish. Continue through \(d(g_s),\ldots,d(g_1)\). Its contraction against \(d(g_i)\), including the outer coefficient \(\sqrt p\), is
\(p\langle\overline f_1,\overline g_i\rangle=p\langle g_i,f_1\rangle\).
There are \(r-1+s-i\) intervening fields for this contraction. The term left with \(B_1\) at the far right vanishes. We have the exact finite recurrence
\[
 \Psi(d(f_1)^*\cdots d(f_r)^*d(g_s)\cdots d(g_1))
 =\sum_{i=1}^s(-1)^{r-1+s-i}p\langle g_i,f_1\rangle
 \Psi(d(f_2)^*\cdots d(f_r)^*d(g_s)\cdots\widehat{d(g_i)}\cdots d(g_1)).       \tag{PG12}
\]
When \(r\ne s\), induction decreases both lengths by one until it reaches a nonempty pure word, so every term is zero. When \(r=s=k\), the sign is \((-1)^{2k-i-1}=(-1)^{i+1}\), precisely the cofactor sign for row \(i\) in the first column of \([p\langle g_i,f_j\rangle]\). Induction from the empty determinant proves (PG10) for \(\psi\), with all signs and repeated vectors included. This proves the specialized doubled-field moment formula without Wick's theorem. Section 8.5 gives \(\psi=\omega\) on the whole norm-closed \(A\).

### 8.7. The entire doubled-Fock space is cyclic at \(0<p<1\)

Let \(C\) be the closed linear span of \(\pi_D(A)\Omega_L\). For each coordinate,
\[
 d(e_j)\Omega_L=\sqrt p\,(0\oplus\overline e_j),\qquad
 d(e_j)^*\Omega_L=\sqrt{1-p}\,(e_j\oplus0).                  \tag{PG13}
\]
Here one-particle vectors are identified with the corresponding occupation vectors. Both coefficients are nonzero, which is the exact place where the faithful assumption is needed.

For an arbitrary finite increasing list \(w_1,\ldots,w_r\) of distinct basis vectors of \(L\), choose
\(h_i=d(e_j)^*/\sqrt{1-p}\) if \(w_i=e_j\oplus0\), and
\(h_i=d(e_j)/\sqrt p\) if \(w_i=0\oplus\overline e_j\).
Each \(h_i\) is the creator \(c_L(w_i)\) plus a scalar multiple of an annihilator in the other leg. Expand the finite product \(h_1\cdots h_r\Omega_L\). The term taking every creator is \(c_L(w_1)\cdots c_L(w_r)\Omega_L=[w_1,\ldots,w_r]\), with the normalization of Section 8.1. Every other term contains at least one annihilator, and, if nonzero, has particle degree at most \(r-2\): each creation increases degree by one and each annihilation decreases it by one. These are finite linear combinations of occupation vectors, since every participating one-particle vector is a basis vector.

Induct on \(r\). The vacuum belongs to \(C\), and formula (PG13) supplies degree one. Assume all occupation vectors of degrees below \(r\) lie in \(C\). The product \(h_1\cdots h_r\Omega_L\) lies in \(C\), and so does its entire lower-degree sum by induction. Subtracting proves that \([w_1,\ldots,w_r]\in C\). Section 8.1 proves these occupation vectors form a complete basis of \(\mathcal F(L)\), so \(C=\mathcal F(L)\). This proves cyclicity of the whole concrete doubled-Fock representation, rather than only a finite cyclic subspace. It asserts no cyclicity at \(p=0,1\).

### 8.8. The completed GNS quotient and the explicit onto intertwining unitary

For completeness, construct the GNS Hilbert space at this state. Define
\(N_\omega=\{x\in A:\omega(x^*x)=0\}\). Because \(\omega=\varphi\circ\theta\),
\[
 \omega(x^*y)=\langle\theta(x)\Omega_\rho,\theta(y)\Omega_\rho\rangle.        \tag{PG14}
\]
In particular \(N_\omega\) is the kernel of the linear map \(x\mapsto\theta(x)\Omega_\rho\), so it is a linear subspace, and the indicated form descends to a positive definite inner product on \(A/N_\omega\). It is a left ideal because
\(\|\theta(zx)\Omega_\rho\|\le\|z\|\,\|\theta(x)\Omega_\rho\|\).
Left multiplication \([x]\mapsto[zx]\) is bounded by \(\|z\|\) and has adjoint given by left multiplication by \(z^*\), as follows directly from (PG14). Completing this inner-product space (the Cauchy-sequence completion of ITP10.3) gives \(H_\omega\), representation \(\pi_\omega\), and unit vector \(\Omega_\omega=[1]\). It is cyclic because \(\pi_\omega(x)[1]=[x]\), and the quotient classes are dense in the completion. Local classes are dense too: if \(x_n\) from the local union tend in norm to \(x\), then \(\|[x_n-x]\|\le\|x_n-x\|\).

Equation (PG14) gives the isometry
\[
 U_\rho[x]=\theta(x)\Omega_\rho\quad\text{on }A/N_\omega.
\]
It extends uniquely to \(H_\omega\). It is onto \(H_\rho\): for each \(n\), finite left multiplication sends \(x\mapsto x\rho_n^{1/2}\), a linear bijection of \(M_{2^n}\) because \(\rho_n\) is invertible. Thus \(B_n\Omega_\rho=H^{(n)}\) in its product embedding. The local union is dense in \(H_\rho\) by its definition; an isometry from a complete space has closed range (Cauchy preimages prove this), so the dense range is all of \(H_\rho\).

Since \(\psi=\omega\), the same calculation gives an isometry
\(U_D[x]=\pi_D(x)\Omega_L\). It extends to \(H_\omega\) and is onto \(\mathcal F(L)\) by Section 8.7 and the same closed-range argument. For all \(z,x\in A\),
\(U_\rho\pi_\omega(z)[x]=\theta(z)U_\rho[x]\), and
\(U_D\pi_\omega(z)[x]=\pi_D(z)U_D[x]\).
The operators are bounded and the quotient classes are dense, so these equalities hold everywhere. Therefore
\[
 W=U_\rho U_D^*:\mathcal F(L)\longrightarrow H_\rho
\]
is an onto unitary satisfying
\[
 W\Omega_L=\Omega_\rho,\qquad W\pi_D(z)W^*=\theta(z)\quad(z\in A).        \tag{PG15}
\]
In particular its equality for every \(a(f)\), including non-finite-support \(f\), follows from the norm extensions already proved. This is the whole completed GNS identification, with no finite-moment-to-completion gap.

### 8.9. Generated von Neumann algebras and concrete normality

Let \(M_\omega=\pi_\omega(A)''\), \(M_D=\pi_D(A)''\), and
\(M_\rho=(\bigcup_n B_n)''\subset B(H_\rho)\). Norm density gives \(B''=(\bigcup_n B_n)''\): commuting with a norm-dense set is equivalent to commuting with its norm closure, since multiplication by a fixed bounded operator is norm continuous. Unitary conjugation maps a commutant onto the commutant of its image, because the equality of the two products is preserved in both directions. Applying this twice to (PG15) gives
\[
 W M_D W^*=M_\rho,
 \qquad U_\rho M_\omega U_\rho^*=M_\rho.                    \tag{PG16}
\]
The concrete bicommutant theorem of ITP10.5 identifies these algebras with their weak-operator generated algebras as well. No abstract normal extension is needed to produce the maps: they are the already constructed unitary conjugations on every bounded operator.

These maps are normal in the concrete ultraweak sense. Recall the concrete ultraweak defining functionals on \(B(H)\) are
\(F_{u,v}(x)=\sum_{k\ge1}\langle u_k,xv_k\rangle\), where both sequences are square-summable. The series converges absolutely by Cauchy–Schwarz and the operator bound. Under conjugation by \(W\),
\[
 F_{u,v}(WxW^*)=F_{W^*u,W^*v}(x),
\]
and both transformed square sums are preserved. Pulling back each defining functional therefore gives another such functional, proving ultraweak continuity; the inverse has the same proof. The conclusion restricts to (PG16), and the proof for \(U_\rho\) is identical. This is the exact concrete meaning of the normal isomorphism claimed here; abstract predual equivalence is neither assumed nor proved here.

The vacuum-preserving identity gives the state equality on every \(y\in M_D\),
\[
 \langle\Omega_L,y\Omega_L\rangle
 =\langle\Omega_\rho,WyW^*\Omega_\rho\rangle.                \tag{PG17}
\]
ITP11.3 proves that the product vector is cyclic and separating for \(M_\rho\), using the dense commuting right orbit and invertibility of \(\rho\); thus its vector state is faithful and concretely normal. Transport by these unitaries gives the same assertions in \(M_D\) and \(M_\omega\). No classification or normality theorem for arbitrary representations has been used.

### 8.10. Exact admission boundary and proof mechanism

The conclusion proved here is the countable identical faithful \(2\)-level parity-string completed-GNS identification, its specified finite determinant moments, and its concrete normal generated-algebra/state identification. At the current consumer's hypotheses \(0<p<1\), \(p\ne\tfrac12\), it yields exactly
\[
 (M,\varphi)\cong\overline{\bigotimes_{j\ge1}}(M_2,\operatorname{Tr}(\rho\,\cdot)),
 \quad \rho=\operatorname{diag}(1-p,p),
\]
where the bar means the pointed Hilbert–Schmidt product von Neumann algebra just constructed. The chosen ordering of the countable basis is part of the explicit parity strings; compatibility proves the same ordered representation at every finite block. This proof supplies the exact \(T=pI\) specialization of the earlier lesson's formula (19), not that formula in its other stated settings.

The maps proved above have the following domains and codomains. The finite maps are compatible with the specified coordinate inclusions; the norm and Hilbert completions are distinct steps.

| Map | Domain and codomain | Proof |
| --- | --- | --- |
| \(\theta_n\) | \(A_n\to M_2^{\otimes n}\), onto isometric *-map with the specified parity strings | Section 8.2 |
| \(\theta\) | \(A\to B\), onto isometric *-map of norm completions | Section 8.3 |
| \(U_D\) | \(H_\omega\to\mathcal F(K\oplus\overline K)\), onto cyclic isometry | Sections 8.7–8.8 |
| \(U_\rho\) | \(H_\omega\to H_\rho\), onto cyclic isometry | Section 8.8 |
| \(W=U_\rho U_D^*\) | \(\mathcal F(K\oplus\overline K)\to H_\rho\), vacuum-preserving unitary intertwining every generator | Section 8.8 |

Sections 8.4 and 8.6 equate all specified normal moments. Section 8.5 turns that into equality of bounded states on the entire norm-closed algebra. Section 8.8 completes the common cyclic inner products, with surjectivity proved on both sides. Section 8.9 transports the generated von Neumann algebras and all vector-state values.

Not proved here: arbitrary/nonidentical covariance, uncountable index products, nonfaithful endpoints \(p=0,1\), a universal CAR C*-norm or general CAR simplicity theorem, a general pairing/Wick theorem, general quasifree-state classification, general representation normal-extension or abstract-predual equivalence, a general infinite tensor commutant theorem, general modular theory, factorial/type/semifiniteness/AFD or type-III subtype conclusions. Those exclusions do not qualify any step of the proved faithful countable constant-\(p\) identification; they delimit separate scopes.

The selected free human comparisons are [Jan Dereziński, *Introduction to representations of the canonical commutation and anticommutation relations*, arXiv:math-ph/0511030v2](https://arxiv.org/pdf/math-ph/0511030v2), printed pp.16–17, Sections 4.2; pp.20–23, Sections 5.3–5.7; and p.46, Sections 10.1–10.2; and [Huzihiro Araki, *On quasifree states of CAR and Bogoliubov automorphisms*](https://ems.press/content/serial-article-files/41673?nt=1), printed pp.387–390, especially the complete cyclic-isometry proof of Lemma 4.2 across pp.389–390. Dereziński gives the Jordan–Wigner, antisymmetric and doubled-field methods. His Theorems 10, 17 and 19 have no complete proofs on these selected pages, so the exact consumed steps are proved independently above. Araki’s general norm-uniqueness, quasifree-existence, Bogoliubov and purity chains are likewise not inputs.

## 9. Arbitrary Hilbert-space Fock foundations

This supplies the arbitrary one-particle Hilbert-space construction and the full irreducibility argument used in earlier CAR Section 1 and Lemma 1.1. It is known-proof reconstruction. The baseline is ZFC, real and complex scalar completeness, Hilbert-space definitions, and the full concrete proofs in [ITP Sections 10.1–10.4](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) and ITP Section 10.6. Those sections prove Hilbert Cauchy–Schwarz, orthogonal projection, bounded adjoints, operator norms, finite tensor positivity/completion and the complete countable sum with one fixed Hilbert summand. Section 9.3 supplies the needed sum with varying particle sectors directly. No positive-operator functional calculus, GNS theorem, trace, von Neumann algebra, Kaplansky density or countability of the one-particle space is used here. Inner products are linear in the second variable.

### 9.1. Complete coordinates for arbitrary index sets

An orthonormal set extends to a maximal orthonormal set by Zorn's lemma: the union of an inclusion-ordered chain of orthonormal sets is orthonormal, since every finite pair occurs in a member of the chain. Let \((e_i)_{i\in I}\) be such a maximal set. Its closed linear span is all of \(K\). Otherwise the orthogonal projection onto that closed span, supplied in ITP Section 10.1, gives a nonzero vector in its orthogonal complement, whose normalization can be added to the set, contrary to maximality. This also proves that a specified unit vector can be included in a basis. ZFC permits a well-order on \(I\); for a specified unit vector we can choose it as the first element. The zero Hilbert space has the empty basis.

For \(h\in K\) and a finite \(F\subset I\), put
\[
p_Fh=\sum_{i\in F}e_i\langle e_i,h\rangle.
\]
The finite orthonormal identities show that \(p_F\) is an orthogonal projection and
\[
\|p_Fh\|^2=\sum_{i\in F}|\langle e_i,h\rangle|^2\le\|h\|^2.
\]
Let \(s\) be the supremum of these nonnegative finite sums. Given \(\varepsilon>0\), choose finite \(F_0\) with its sum greater than \(s-\varepsilon^2\). Every finite subset of \(I\setminus F_0\) then has sum at most \(\varepsilon^2\), by adjoining it to \(F_0\). Thus for \(F,G\supseteq F_0\),
\[
\|p_Fh-p_Gh\|^2
=\sum_{i\in F\triangle G}|\langle e_i,h\rangle|^2\le\varepsilon^2.
\]
The finite-set net is Cauchy. Its convergence follows directly from Hilbert completeness: choose a sequence of its indices after which all differences have norm at most \(2^{-n}\), replace the chosen indices by their successive finite unions, and take the limit of that Cauchy sequence. The same bounds show that the entire net converges to that limit. Call it \(h_0\). For each \(i\), the coefficient of the limit is \(\langle e_i,h\rangle\), since all sufficiently large finite sets contain \(i\). Hence \(h-h_0\) is orthogonal to the total basis and is zero. We have proved
\[
h=\lim_{F\Subset I}p_Fh,
\qquad \|h\|^2=\sup_{F\Subset I}\sum_{i\in F}|\langle e_i,h\rangle|^2. \tag{AF1}
\]
Here \(F\Subset I\) means that \(F\) is finite. For each positive integer \(n\), the set of coefficients with modulus at least \(1/n\) is finite, since its arbitrarily large finite subsets would violate the displayed bound. The nonzero coefficient set is the countable union of these finite sets. No cardinality restriction on the basis itself follows or is assumed.

For completeness, define \(\ell^2(I)\) as all scalar families \(z=(z_i)\) with \(\sup_{F\Subset I}\sum_{i\in F}|z_i|^2<\infty\). Each such family has countable support by the same argument. Its inner product is the absolutely convergent sum of \(\overline{z_i}w_i\) on the union of the two countable supports; scalar Cauchy–Schwarz bounds each finite sum and the tails, and therefore proves convergence and independence from the enumeration. To prove completeness, let \(z^{(n)}\) be Cauchy. Each coordinate has a scalar limit \(z_i\). A uniform norm bound and passage to the limit in every finite coordinate sum give \(\sup_F\sum_{i\in F}|z_i|^2<\infty\). For \(n\ge n_0\) with \(\|z^{(n)}-z^{(m)}\|\le\varepsilon\) for all \(m\ge n_0\), pass to the coordinate limit in each finite sum and then take its supremum to obtain \(\|z^{(n)}-z\|\le\varepsilon\). Thus \(\ell^2(I)\) is complete. Finite-support families are dense by choosing a finite sum within \(\varepsilon^2\) of the supremum. Equation (AF1) makes the coefficient map \(K\to\ell^2(I)\) an onto isometry: it is an isometry with closed range, and its range contains every finite-support family, which is dense. A complete isometric range is closed because a convergent range sequence has Cauchy preimages.

### 9.2. Completed tensors and antisymmetric occupation basis

Finite Hilbert tensor products are the positive-inner-product completions constructed in ITP Section 10.3. Inductively the vectors
\(e_{i_1}\otimes\cdots\otimes e_{i_n}\), indexed by \(I^n\), form a complete orthonormal basis of \(K^{\otimes n}\). Orthogonality follows from the product inner product. To check totality, approximate every factor of an elementary tensor by a finite basis sum using (AF1). The tensor-product norm of an elementary tensor is the product of the factor norms. Replacing factors successively therefore gives norm convergence of these finite expansions. Elementary tensors span a dense subspace by the definition of the completion. This proves totality, including for uncountable \(I\).

Define \(U_\sigma\) on those basis tensors by replacing the index list \((i_1,\ldots,i_n)\) by \((i_{\sigma^{-1}(1)},\ldots,i_{\sigma^{-1}(n)})\). It is an isometry of the basis span onto itself; its inverse is \(U_{\sigma^{-1}}\), so both extend to mutually inverse unitaries. We have \(U_\sigma U_\tau=U_{\sigma\tau}\). Consequently
\[
A_n=\frac1{n!}\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)U_\sigma
\]
is selfadjoint and idempotent: the adjoint replaces each permutation by its inverse, without changing its sign; in the square each resulting permutation occurs \(n!\) times with its sign. It is the orthogonal projection onto its range, since its kernel and range are orthogonal by selfadjointness and every vector is the sum of its image and complementary image. Thus \(\Lambda^nK=A_nK^{\otimes n}\) is closed and complete.

For \(f_1,\ldots,f_n\in K\), write
\[
[f_1,\ldots,f_n]=\sqrt{n!}\,A_n(f_1\otimes\cdots\otimes f_n).
\]
Take a finite increasing list \(i_1<\cdots<i_n\) in the chosen order of \(I\). The \(n!\) permutations of its tensor are distinct orthonormal vectors; each has coefficient of modulus \(1/\sqrt{n!}\) in its normalized antisymmetrization. Its norm is therefore one. Distinct finite increasing lists have disjoint permutation orbits and are orthogonal. A repeated index gives zero antisymmetrization: pair every term with the term obtained by interchanging the two equal tensor positions; their signs differ and their tensors agree. Applying the bounded projection \(A_n\) to the dense tensor basis span proves that these normalized increasing wedges span densely in its range. They are its complete orthonormal basis.

The finite permutation expansion also gives, with no limiting operation,
\[
\langle[f_1,\ldots,f_n],[g_1,\ldots,g_n]\rangle
=\det[\langle f_i,g_j\rangle]_{i,j=1}^n. \tag{AF2}
\]
Indeed one can absorb one of the two antisymmetrizers by its selfadjoint idempotence, leaving \(n!\langle f_1\otimes\cdots\otimes f_n,A_n(g_1\otimes\cdots\otimes g_n)\rangle\). The remaining sum is the permutation formula for the determinant (using inverse permutations gives the same sum). This proves the claimed normalization and sign convention.

### 9.3. Full Fock completion and bounded creation

Put \(\Lambda^0K=\mathbb C\). Define \(\mathcal F(K)=\bigoplus_{n\ge0}\Lambda^nK\) as the families \(\eta=(\eta_n)\), with \(\eta_n\in\Lambda^nK\) and \(\sum_n\|\eta_n\|^2<\infty\), with inner product \(\sum_n\langle\eta_n,\zeta_n\rangle\). Scalar Cauchy–Schwarz bounds the absolute inner-product sum, giving a well-defined Hilbert norm. Here the summands vary with \(n\), so completeness is proved directly. If \(\eta^{(j)}\) is Cauchy in this norm, each degree coordinate has a limit \(\eta_n\) in its complete sector. A uniform norm bound \(\|\eta^{(j)}\|\le C\) and passage to the coordinate limit in each finite initial sum give \(\sum_{n=0}^N\|\eta_n\|^2\le C^2\). Taking the supremum over \(N\) puts \(\eta\) in the sum. If \(\|\eta^{(j)}-\eta^{(k)}\|\le\varepsilon\) for \(j,k\ge j_0\), passing to the coordinate limit in each finite difference sum and then taking its supremum gives \(\|\eta^{(j)}-\eta\|\le\varepsilon\) for \(j\ge j_0\). This proves completeness. Finite-degree truncations are dense by the vanishing square-sum tails.

Let \(\Omega=1\) in degree zero. The complete occupation basis is indexed by all finite subsets \(S\subset I\): the empty subset is \(\Omega\), and a nonempty subset in its chosen increasing order is the corresponding normalized wedge. Totality follows by first truncating degrees and then using the complete occupation basis in each of the finitely many remaining sectors. There is no countability restriction on this set of basis labels. Section 9.1 applies to it; finite linear combinations of occupation vectors are dense in the whole Fock space, and each Fock vector has square-summable occupation coefficients.

On degree \(n\), define
\[
c(f)\eta=\sqrt{n+1}\,A_{n+1}(f\otimes\eta). \tag{AF3}
\]
This is a bounded map from degree \(n\) to degree \(n+1\), with bound \(\sqrt{n+1}\|f\|\), by the elementary tensor norm and the projection norm. The formula respects the finite-degree algebraic direct sum and is linear in \(f\). It satisfies
\[
c(f)[g_1,\ldots,g_n]=[f,g_1,\ldots,g_n], \tag{AF4}
\]
because \(A_{n+1}(1\otimes A_n)=A_{n+1}\): average permutations of the last \(n\) positions inside the full antisymmetrizer; the signs cancel the alternating effect, leaving the latter unchanged.

For a unit \(f\), choose a basis beginning with \(f\), as Section 9.1 permits. Equation (AF4) says that \(c(f)\) sends each occupation vector not containing \(f\) to a distinct occupation vector containing \(f\), with coefficient one in this order, and kills the occupation vectors already containing \(f\). The two sets span orthogonal subspaces. Hence it has norm at most one on the dense finite occupation span. On each fixed degree this description agrees with the already bounded map (AF3), since occupation vectors are total in that degree. It therefore gives the same map on all finite-degree vectors. On those vectors its norm is at most one, and it extends uniquely to a contraction on the whole Fock space. Since \(c(f)\Omega=f\), its norm is one. Scaling, and the case \(f=0\), give
\[
\|c(f)\|=\|f\|. \tag{AF5}
\]
The identities expressing linearity in \(f\) hold on the dense core and extend to all of Fock by the bounds. Set \(a(f)=c(f)^*\); ITP Section 10.2 supplies this bounded adjoint and its equal norm. Annihilation is conjugate-linear in \(f\).

### 9.4. Contraction, CAR and arbitrary-space irreducibility

The bounded adjoint has the exact formula
\[
a(f)[g_1,\ldots,g_n]
=\sum_{j=1}^n(-1)^{j-1}\langle f,g_j\rangle
[g_1,\ldots,\widehat{g_j},\ldots,g_n],
\qquad a(f)\Omega=0. \tag{AF6}
\]
To prove it, test against arbitrary degree \(n-1\) product wedges. The adjoint identity, (AF4) and (AF2) yield the determinant whose first row is \((\langle f,g_j\rangle)_j\); expansion along that row gives exactly the displayed sum. Those test wedges are total in the degree. Tests in other degrees vanish by orthogonality, so this proves the full vector equality. The degree-zero assertion follows because creation raises degree.

Applying (AF6) after (AF4) gives
\[
a(f)c(g)\eta=\langle f,g\rangle\eta-c(g)a(f)\eta
\]
for every product wedge \(\eta\). Alternation gives \(c(f)c(g)=-c(g)c(f)\) there. Product wedges span a dense subspace; all participating operators are bounded, so these identities hold everywhere. Taking adjoints gives the annihilation anticommutator. Thus the full CAR hold on the completed Fock space:
\[
\{a(f),a(g)\}=0,
\qquad \{a(f),a(g)^*\}=\langle f,g\rangle1. \tag{AF7}
\]

For an occupation vector labelled by finite \(S\), (AF6) removes \(i\in S\) with sign \((-1)^{|\{j\in S:j<i\}|}\), and gives zero if \(i\notin S\). The count is finite even when the ordered basis is uncountable. If \(a(e_i)\xi=0\) for all \(i\), fix any nonempty finite \(S\) and choose \(i\in S\). The coefficient at \(S\setminus\{i\}\) of \(a(e_i)\xi\) is precisely that sign times the coefficient at \(S\) of \(\xi\): \(S\) is the unique source occupation label which can produce this label by removing \(i\). This assertion for arbitrary \(\xi\) follows from the formula on finite occupation vectors by boundedness and continuity of the coefficient functional. Its coefficient must be zero. Every nonempty occupation coefficient of \(\xi\) is consequently zero, so Section 9.1 gives \(\xi\in\mathbb C\Omega\).

If \(x\in B(\mathcal F(K))\) commutes with all creators and annihilators, then \(a(f)x\Omega=xa(f)\Omega=0\), so \(x\Omega=\lambda\Omega\). Products of basis creators applied to the vacuum are exactly all occupation vectors by (AF4). Commutation gives \(x=\lambda1\) on their dense span and hence on the whole Fock space. The commutant of the concrete Fock CAR algebra is therefore \(\mathbb C1\), the irreducibility assertion of original Lemma 1.1. If \(K=\{0\}\), its Fock space is \(\mathbb C\) and the same conclusion holds directly.

### 9.5. Exact scope and freely accessible comparison

The proof supplies the full arbitrary-Hilbert-space antisymmetric completion, complete occupation coordinates, normalization, bounded creation and annihilation, CAR, and original Lemma 1.1 irreducibility. It does not use or prove covariance square roots, a quasifree GNS theorem, normal representation existence, a tensor commutant theorem, a general minimal tensor norm theorem, Kaplansky density, modular theory or any factor classification. Separate matrix-algebra or covariance arguments must explicitly select their own supports.

[Jan Dereziński, *Introduction to representations of the canonical commutation and anticommutation relations*, arXiv:math-ph/0511030v2](https://arxiv.org/pdf/math-ph/0511030v2), printed pp.20–23, Sections 5.3–5.7, supplies the selected antisymmetry, normalization, CAR and parity comparisons. The selected Theorems 17 and 19 are statements without full proofs on those pages. Sections 9.1–9.4 supply the complete construction independently.

## 10. Concrete CAR matrix algebras, completions and simplicity

This supplies Theorem 2.1, Corollary 2.2 and their intervening construction at the original scope. The one-particle Hilbert space K is arbitrary, including zero-dimensional, finite-dimensional and nonseparable spaces. Representation Hilbert spaces are arbitrary and nonzero. The countable tensor conclusion is asserted only when K is separable and infinite-dimensional.

The foundation boundary is ZFC and its choice principle, real/complex scalar completeness, elementary scalar arithmetic, and concrete Hilbert/operator definitions. The complete [ITP Sections 10.1–10.4](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) supply inner-product Cauchy–Schwarz, orthogonal projections, Hilbert Riesz and bounded adjoints, norm completeness and the operator C\*-identity, finite Gram–Schmidt, Hilbert tensor completion, tensor operator bounds and elementary-vector totality. No spectral theorem, fundamental theorem of algebra, compactness theorem, abstract C\*-representation existence theorem, generic injective-homomorphism isometry, quotient-isometry theorem, GNS construction, predual or modular theorem is an input.

Sections 10.1–2 construct an available concrete CAR family without importing the earlier lesson's countable Fock proof as an arbitrary-index result. Sections 10.3–6 apply to **any given nonzero concrete CAR families**, and prove their finite and completed norm identifications directly. The earlier antisymmetric Fock family, when supplied as a bounded CAR family, is covered by that statement; this support does not certify the separate full exterior-Fock theorem or its irreducibility. The explicit occupation model below ensures that the family hypothesis has an actual realization for every K. Thus no abstract universal representation existence is required.

Inner products are conjugate linear in the first variable and linear in the second. A concrete CAR family on H means a conjugate-linear map

\[
a:K\longrightarrow B(H),\qquad H\ne\{0\},
\]

satisfying

\[
a(f)a(g)+a(g)a(f)=0,
\qquad
a(f)a(g)^*+a(g)^*a(f)=\langle f,g\rangle1_H. \tag{GM1}
\]

The generated algebra is the operator-norm closed unital \*-subalgebra
\(A_a=C^*(1_H,a(f):f\in K)\). “Simple” means that every norm-closed complex linear two-sided ideal is zero or the whole algebra. No selfadjointness of an ideal is assumed in the proof.

### 10.1. An arbitrary-index concrete occupation model

Zorn's lemma gives a maximal orthonormal subset \((e_i)_{i\in I}\) of K: unions of chains of orthonormal subsets remain orthonormal. Its closed span is K. Otherwise the orthogonal projection onto that span, provided by ITP Section 10.1, gives a nonzero vector in its orthogonal complement, which can be normalized and adjoined, a contradiction. ZFC also allows a well-order of I; only the induced order on each finite subset is used below. When K is zero, I is empty.

Let \(\operatorname{Fin}(I)\) be the set of finite subsets of I. On the finite-support scalar functions on this set use the inner product with orthonormal coordinate vectors \(\delta_S\), and complete it to a Hilbert space \(H_{\rm occ}\). Concretely the completion consists of Cauchy-sequence classes, with two sequences identified when their difference tends to zero and with inner products defined by termwise limits. Cauchy–Schwarz makes these limits well defined; a Cauchy sequence of classes is represented by approximants whose errors are less than \(2^{-n}\), and those approximants form a Cauchy sequence. This is the completion argument of ITP Section 10.3, applied to the finite-support inner-product space. No countability of I or \(\operatorname{Fin}(I)\) is used. The coordinate vectors have total finite span by construction, and \(\delta_\varnothing\) has norm one, so the space is nonzero.

For \(i\in I\), put \(q_i(S)=|\{s\in S:s<i\}|\), and define on coordinate vectors

\[
\begin{aligned}
C_i\delta_S&=\begin{cases}(-1)^{q_i(S)}\delta_{S\cup\{i\}},&i\notin S,\\0,&i\in S,\end{cases}\\
A_i\delta_S&=\begin{cases}(-1)^{q_i(S)}\delta_{S\setminus\{i\}},&i\in S,\\0,&i\notin S.\end{cases}
\end{aligned} \tag{GM2}
\]

Each nonzero part is a signed injection between coordinate sets. Therefore its squared output norm on a finite sum is the sum of a subset of the squared input coefficients. Both operators are contractions and extend uniquely by continuity. Coordinate coefficients show \(A_i^*=C_i\); testing the vacuum for C_i and \(\delta_{\{i\}}\) for A_i gives norm one.

Same-index relations are \(A_i^2=C_i^2=0\) and \(A_iC_i+C_iA_i=1\), since exactly one of the two products fixes each coordinate vector. For distinct i and j, both orders of two removals are possible exactly when both indices are in S; otherwise both orders vanish. If i<j, removing i lowers q_j by one while removing j leaves q_i unchanged. Their two nonzero signs are opposite. For removal of i and insertion of j, both orders are possible exactly when i is in S and j is absent. If i<j, the removal changes q_j by one; if j<i, the insertion changes q_i by one. Again the signs are opposite. Taking adjoints covers two insertions and the remaining mixed relation. Thus

\[
\{A_i,A_j\}=0,
\qquad \{A_i,A_j^*\}=\delta_{ij}1.
\]

These calculations involve only two indices and a finite S and are valid for an arbitrarily large ordered I. Equality on the total finite span and boundedness extend them to the completion.

For a finite basis sum \(f=\sum_i f_i e_i\), define \(a_{\rm occ}(f)=\sum_i\overline{f_i}A_i\). Finite expansion gives (GM1) for such f and g. Section 10.3 below proves directly that \(\|a_{\rm occ}(f)\|=\|f\|\). Consequently, for arbitrary f in K, choose finite basis sums converging to f and take the operator-norm limit. The exact norm estimate makes it Cauchy and independent of the approximating sequence. Conjugate linearity, adjoints and both products pass to these limits; the scalar inner product also passes by Cauchy–Schwarz. This produces a concrete family (GM1) on \(H_{\rm occ}\) for every K. For K=0 the sole generator is zero and the generated unital algebra is \(\mathbb C1\).

This is an explicit bounded occupation model. By itself it does not prove the arbitrary exterior-space, covariance, quasifree-state or Fock irreducibility statements.

### 10.2. The finite-subspace directed system

For a concrete family a and a finite-dimensional subspace E of K, put

\[
A_a(E)=C^*(1_H,a(f):f\in E)\subseteq A_a.
\]

The finite-dimensional subspaces form a directed set under inclusion: E+F is finite-dimensional and contains E and F. If E is contained in F, then \(A_a(E)\subseteq A_a(F)\) by the definition of the generated algebra. Any \*-polynomial in finitely many generators and their adjoints belongs to \(A_a(E)\) for the finite span E of its one-particle arguments. Such polynomials and the identity define the norm-dense generating subalgebra of \(A_a\). Hence

\[
\mathcal A_a:=\bigcup_{\dim E<\infty} A_a(E)
\quad\hbox{is a unital *-algebra dense in }A_a. \tag{GM3}
\]

Directedness ensures that sums and products of elements from different finite subspaces belong to a common finite algebra. This assertion uses all finite subspaces, rather than a selected countable basis. It is valid for arbitrary K.

### 10.3. Exact generator norms and all one-mode matrix identities

Let f be a unit vector in K and write \(u=a(f)\), \(n=u^*u\). From (GM1),

\[
u^2=0,\quad uu^*=1-n,\quad
n^2=u^*(1-u^*u)u=n,
\quad un=u,\quad nu=0. \tag{GM4}
\]

The expressions n and 1-n are selfadjoint projections. If n were zero, the operator C\*-identity would give u=0, contradicting \(uu^*+u^*u=1\) on nonzero H. If 1-n were zero, the same identity for \(uu^*\) would again give u=0 and the same contradiction. A nonzero orthogonal projection has norm one: the orthogonal decomposition bounds its norm by one, and a unit vector in its range gives the reverse bound. Thus \(\|u\|^2=\|u^*u\|=1\). Conjugate linearity and scaling give, including f=0,

\[
\boxed{\ \|a(f)\|=\|f\|,\qquad
\|a(f)-a(g)\|=\|f-g\|.\ } \tag{GM5}
\]

This derivation also proves the norm assertion used for finite sums in Section 10.1 and does not require the existence of a CAR family for all f before applying it there. The operator norm satisfies the triangle inequality directly: \(\|(S+T)\xi\|\le\|S\xi\|+\|T\xi\|\) and taking the unit-vector supremum gives \(\|S+T\|\le\|S\|+\|T\|\). Applying this twice gives \(|\|S\|-\|T\||\le\|S-T\|\), the reverse triangle bound used below.

If b satisfies (GM4), the four operators

\[
e_{00}=1-b^*b,\quad e_{01}=b,\quad
e_{10}=b^*,\quad e_{11}=b^*b
\]

have the following complete product table. It follows from (GM4), its adjoints and \(bb^*=1-b^*b\):

| Left factor / right factor | e00 | e01 | e10 | e11 |
| --- | --- | --- | --- | --- |
| e00 | e00 | e01 | 0 | 0 |
| e01 | 0 | 0 | e00 | e01 |
| e10 | e10 | e11 | 0 | 0 |
| e11 | 0 | 0 | e10 | e11 |

The adjoints interchange e01 and e10 and fix the other two. The diagonal sum is one. These are all matrix-unit identities, including the zero products.

### 10.4. Full finite matrix units and their exact concrete norm

Choose an ordered orthonormal basis \(f_1,\ldots,f_d\) of E, using finite Gram–Schmidt. Write \(a_j=a(f_j)\), \(n_j=a_j^*a_j\) and

\[
Z_j=1-2n_j,\qquad P_j=\prod_{k<j}Z_k,
\qquad b_j=P_j a_j. \tag{GM6}
\]

For i different from j, moving a_j past the two factors of n_i gives two minus signs and no scalar contraction, hence n_i commutes with a_j and a_j^*. It follows that all n_j commute, and so do the selfadjoint unitaries Z_j. The single-mode identities give

\[
Z_j a_j=a_j,\quad a_jZ_j=-a_j,
\quad Z_j a_j^*=-a_j^*,\quad a_j^*Z_j=a_j^*.
\]

P_j commutes with its own mode. Therefore b_j has the one-mode relations of Section 10.3 and \(b_j^*b_j=n_j\). All b_i, b_i^* commute with b_j, b_j^* for i different from j. To check every adjoint choice, let i<j and write \(P_j=P_i Z_i W\), with \(W=\prod_{i<k<j}Z_k\). P_i and W commute with both fields in modes i,j. For \(u_i\in\{a_i,a_i^*\}\), \(u_j\in\{a_j,a_j^*\}\), cancellation of P_i squared gives the forward product \(u_iZ_iWu_j\); the reverse is \(Z_iWu_ju_i\). Reversing u_i,u_j gives one CAR sign and moving u_i past Z_i gives a second sign. They cancel, proving equality for all four choices.

In each mode use the Section 10.3 matrix units with b_j. For bit tuples \(\alpha,\beta\in\{0,1\}^d\), set

\[
E_{\alpha\beta}=\prod_{j=1}^d e^{(j)}_{\alpha_j\beta_j}.
\]

The different-mode commutations and complete one-mode table prove

\[
E_{\alpha\beta}^*=E_{\beta\alpha},\qquad
E_{\alpha\beta}E_{\gamma\delta}
=\delta_{\beta\gamma}E_{\alpha\delta},\qquad
\sum_\alpha E_{\alpha\alpha}=1. \tag{GM7}
\]

These statements include every tuple and no representation-specific assumption. Put m=2^d, fix the all-zero tuple o and let \(Q=E_{oo}H\). This is a closed subspace, since Eoo is a bounded orthogonal projection. It is nonzero: if Eoo=0, then
\(E_{\alpha o}^*E_{\alpha o}=E_{oo}=0\), so the C\*-identity gives \(E_{\alpha o}=0\). Consequently every \(E_{\alpha\alpha}=E_{\alpha o}E_{o\alpha}\) is zero, contradicting their sum 1 on nonzero H.

On the finite tensor product define

\[
V:\mathbb C^m\otimes Q\longrightarrow H,
\qquad V(\delta_\alpha\otimes\eta)=E_{\alpha o}\eta. \tag{GM8}
\]

The relation \(E_{o\alpha}E_{\beta o}=\delta_{\alpha\beta}E_{oo}\) proves preservation of inner products on finite sums, so V extends to an isometry by tensor completion. It is onto: every \(\xi\in H\) equals

\[
\sum_\alpha E_{\alpha o}(E_{o\alpha}\xi),
\qquad E_{o\alpha}\xi\in Q.
\]

For a complex m by m matrix X,

\[
V^*\left(\sum_{\alpha,\beta}X_{\alpha\beta}E_{\alpha\beta}\right)V
=X\otimes1_Q. \tag{GM9}
\]

The amplification has norm exactly \(\|X\|\), using the finite tensor bound of ITP Section 10.4 for the upper bound and a unit vector eta in nonzero Q with vectors \(\xi\otimes\eta\) for the lower bound. Unitary conjugation preserves norm directly from its action on unit vectors. Hence

\[
\left\|\sum_{\alpha,\beta}X_{\alpha\beta}E_{\alpha\beta}\right\|=\|X\|. \tag{GM10}
\]

The matrix-unit map is therefore injective and isometric by explicit calculation, without a simplicity theorem or a generic C\*-isometry theorem. Its range is norm closed. Indeed, a matrix-norm Cauchy sequence has Cauchy coefficients because \(|X_{\alpha\beta}|\le\|X\|\). Their scalar limits define a matrix; the norm difference is bounded by the sum of the absolute coefficient differences, since the ordinary matrix units have norm one. This proves convergence to that matrix and completeness of the finite range.

The range contains b_j and n_j by summing matrix entries over the other modes, and hence Z_j and \(a_j=P_j b_j\). Conversely every Ealpha,beta is a polynomial in the a_j and their adjoints. Since \(a(f)=\sum_j\overline{\langle f_j,f\rangle}a_j\) for f in E, the range is exactly \(A_a(E)\). Thus

\[
\boxed{\ A_a(E)\cong M_{2^{\dim E}}(\mathbb C)
\text{ by an onto isometric unital *-map.}\ } \tag{GM11}
\]

For E=0, the empty tuple is the single index, Eoo=1, Q=H and V is the natural \(\mathbb C\otimes H\) unitary. The generated algebra is \(\mathbb C1=M_1\), so the argument includes d=0. H can have any dimension: the matrix algebra may act with the arbitrary multiplicity Q.

The ordinary finite product \(M_2^{\otimes d}\) in this assertion means its concrete action on \((\mathbb C^2)^{\otimes d}\). The bit-tensor vectors are an orthonormal basis by the finite tensor construction; products of coordinate matrix units are its full matrix units. Consequently its matrix algebra and norm are exactly the M_m just calculated. No general minimal tensor-product theorem is required.

### 10.5. Any two families: basis independence and arbitrary overlaps

Let a and c be two concrete families (GM1) for the same arbitrary K, on arbitrary nonzero H and L. For a finite E choose the same ordered orthonormal basis in both families. The constructions above give their matrix units \(E^a_{\alpha\beta}\) and \(E^c_{\alpha\beta}\). Define

\[
\Phi_E\left(\sum X_{\alpha\beta}E^a_{\alpha\beta}\right)
=\sum X_{\alpha\beta}E^c_{\alpha\beta}. \tag{GM12}
\]

The full matrix products and adjoints show it is a unital \*-map; the norm calculation (GM10) shows it is an onto isometry, with inverse obtained by reversing the two families. It sends each a_j to c_j by the parity formula and therefore sends a(f) to c(f) for **every** f in E by conjugate linearity.

The map is independent of the chosen ordered basis. Two such constructions both send all a(f) to c(f), preserve adjoints and products, and consequently agree on every \*-polynomial in those generators. Those polynomials have dense span in \(A_a(E)\); the two maps are norm continuous isometries, so they agree everywhere. This also proves uniqueness among norm-continuous generator-matching unital \*-maps at this finite scope.

If E is contained in F, \(\Phi_F\) maps \(A_a(E)\) into \(A_c(E)\): it does so on polynomials in E, and its norm continuity gives the assertion on their closure. Its restriction agrees with \(\Phi_E\) by the same generator and density argument. The equality holds on all of \(A_a(E)\), not just a selected matrix basis.

For arbitrary finite E,F with no inclusion, let G=E+F. The preceding restriction equalities give

\[
\Phi_E(x)=\Phi_G(x)=\Phi_F(x)
\qquad(x\in A_a(E)\cap A_a(F)). \tag{GM13}
\]

Thus full **algebra overlaps** are compatible, even without an assertion identifying their intersection with \(A_a(E\cap F)\). Each finite tuple of local elements fits into one G, so (GM12) defines a well-defined isometric unital \*-map \(\Phi_{\rm loc}:\mathcal A_a\to\mathcal A_c\), onto the entire local union. This supplies arbitrary finite-subspace overlap compatibility and does not rely on finding a basis shared by E and F.

### 10.6. The whole norm-completion map and concrete universal property

Both generated algebras are complete: they are norm-closed subspaces of B(H) and B(L), whose completeness is proved in ITP Section 10.2. For \(x\in A_a\), choose \(x_n\in\mathcal A_a\) with \(x_n\to x\) in norm and define

\[
\Phi(x)=\lim_n\Phi_{\rm loc}(x_n). \tag{GM14}
\]

The image sequence is Cauchy by the local norm equality. Any second approximating sequence gives the same limit, because the norm of the difference of its n-th term and the first image term equals the input norm, which tends to zero. The limit belongs to Ac by its norm closedness. Taking limits in \(\|\Phi_{\rm loc}(x_n)\|=\|x_n\|\) gives \(\|\Phi(x)\|=\|x\|\). Addition, scalar multiplication, the adjoint and the identity pass to the limit. For products use local approximants x_n,y_n and the estimate

\[
\|x_ny_n-xy\|
\le\|x_n\|\,\|y_n-y\|+\|x_n-x\|\,\|y\|.
\]

Their norms are bounded; their products belong to the local union by directedness. The same estimate in Ac proves multiplicativity of Phi. Thus Phi is an isometric unital \*-map sending **every** a(f) to c(f), including f not in a selected countable span. The map obtained by reversing the two families has compositions equal to the identity on the dense local unions; norm continuity gives that equality on the whole algebras. Therefore

\[
\boxed{\ \Phi:A_a\longrightarrow A_c
\text{ is an onto isometric unital *-isomorphism.}\ } \tag{GM15}
\]

For completeness, no continuity assumption has to be smuggled into uniqueness if “unital \*-homomorphism” is defined algebraically. Every such map \(\pi:A\to B(L)\) from a unital norm-closed concrete \*-algebra is contractive by the following elementary argument. Fix x in A and a real R greater than \(\|x\|\). Put \(B=x^*x/R^2\), so \(B=B^*\) and \(\|B\|<1\). Set \(c_1=1/2\) and

\[
c_{n+1}=\frac{n-1/2}{n+1}c_n\quad(n\ge1).
\]

Thus \(0<c_n\le1/2\), and \(F(z)=1-\sum_{n\ge1}c_nz^n\) has absolutely convergent operator substitution at B. Its coefficient identity is \(F(z)^2=1-z\). To verify it without an analytic theorem, define formal differentiation by coefficients, \(D(\sum f_nz^n)=\sum(n+1)f_{n+1}z^n\). The product rule is a finite coefficient-sum identity. The recurrence gives \((1-z)DF=-F/2\); for \(G=F^2=\sum g_nz^n\), it gives \((1-z)DG=-G\), or \((n+1)g_{n+1}=(n-1)g_n\). Since g0=1, this forces g1=-1 and every later coefficient zero. Absolute convergence at \(\|B\|<1\) justifies the operator Cauchy product and grouping: the norm of the double series is bounded by the product of two scalar geometric majorants, and finite truncations make its tails vanish. Therefore

\[
c=R\left(1-\sum_{n\ge1}c_n B^n\right)\in A,
\qquad c=c^*,\qquad c^*c+x^*x=R^2 1.
\]

The series converges in the norm-complete A. Real coefficients and selfadjoint B give the adjoint identity by norm continuity; no assertion of positivity of c is needed. Applying the **algebraic** unital \*-map to the last finite identity yields

\[
\pi(c)^*\pi(c)+\pi(x)^*\pi(x)=R^2 1_L.
\]

Both squares have nonnegative Hilbert quadratic forms, so \(\|\pi(x)\eta\|^2\le R^2\|\eta\|^2\) for every eta in L. The operator-norm definition gives \(\|\pi(x)\|\le R\), and letting R decrease to \(\|x\|\) gives contractivity. This proves the precise continuity fact used for uniqueness; it is not an injective-map isometry or quotient theorem.

Any other algebraic unital generator-matching \*-map into a concrete operator algebra is therefore norm continuous. It agrees on polynomials and then on the whole norm closure. The construction above is the precise concrete universal property for every **already given** nonzero bounded CAR family: a generator-matching map exists, is unique and has the displayed norm and range. No universal norm on a free algebra or existence theorem for an abstract representation is asserted. Degenerate representations with a different identity convention, zero Hilbert spaces and abstract target algebras require their own statements and are not silently included.

One can now use any supplied nonzero concrete CAR family to form CAR(K); all such choices have this unique generator-matching completed identification. In particular the explicit family of Section 10.1 is available for every K. Applying (GM15) to a supplied concrete Fock CAR family identifies its generated algebra as well, without importing additional Fock theorems into this support.

### 10.7. Elementary finite maximum and eigenvector lemma

The simplicity proof needs only the following finite matrix fact, which we prove from scalar completeness rather than assume a spectral or compactness theorem.

Every bounded real sequence has a convergent subsequence. Start with a closed interval [-R,R] containing it. At each bisection, at least one closed half contains infinitely many terms. Choose such a half, creating nested closed intervals whose lengths tend to zero. Their increasing left endpoints have a supremum ell by real completeness; the decreasing right endpoints have the same limit, since their differences tend to zero. Thus ell lies in every interval. Recursively choose a term with an index larger than the preceding chosen index in the n-th interval. The selected terms converge to ell, bounded in distance by its length. An initially constant interval needs no bisection. For a bounded sequence in \(\mathbb C^m\), repeat this procedure for each of its 2m real coordinates, keeping a subsequence of the preceding one each time. After finitely many procedures all coordinates converge along one subsequence; the sum-of-squares norm shows convergence in \(\mathbb C^m\). Limits of unit vectors remain unit vectors.

Let \(B=B^*\) be a positive m by m matrix, m at least one. Set

\[
t=\sup_{\|v\|=1}\langle v,Bv\rangle,
\qquad 0\le t\le\|B\|.
\]

Choose unit vectors whose quadratic values tend to t. The finite subsequence argument yields a convergent subsequence with unit limit u. The quadratic form is continuous: for v,w,

\[
|\langle v,Bv\rangle-\langle w,Bw\rangle|
\le\|B\|\,(\|v\|+\|w\|)\|v-w\|,
\]

by expanding the difference and applying Cauchy–Schwarz. Hence \(\langle u,Bu\rangle=t\).

For v perpendicular to u and any complex z, maximality applied to \((u+zv)/\|u+zv\|\) gives

\[
2\operatorname{Re}\bigl(z\langle u,Bv\rangle\bigr)
\le |z|^2\bigl(t\|v\|^2-\langle v,Bv\rangle\bigr). \tag{GM16}
\]

Taking z to be positive and negative real numbers tending to zero makes the real part of \(\langle u,Bv\rangle\) zero. Taking positive and negative imaginary z does the same for its imaginary part. Thus \(Bu\) has zero coefficient against u-perp; selfadjointness gives that claim from the computed coefficients, while \(\langle u,Bu\rangle=t\) gives \(Bu=tu\).

The orthogonal complement of u is invariant under B, since for v in that complement \(\langle u,Bv\rangle=\langle Bu,v\rangle=0\). The restriction there is positive and selfadjoint. Induction on finite dimension, using finite Gram–Schmidt to identify that complement, gives an orthonormal eigenbasis with real nonnegative eigenvalues \(\lambda_1,\ldots,\lambda_m\). Maximality gives \(\lambda_i\le t\) and one eigenvalue t. For \(v=\sum v_i u_i\),

\[
\|Bv\|^2=\sum_i\lambda_i^2|v_i|^2
\le t^2\|v\|^2,
\]

and a unit t-eigenvector gives equality when t>0. Therefore \(t=\|B\|\). In particular if B is nonzero and positive, t>0 and the ordinary rank-one projection e onto a unit t-eigenvector satisfies

\[
eBe=te,\qquad \|e\|=1. \tag{GM17}
\]

All positivity facts used here follow from the Hilbert quadratic-form definition. In particular \(Y^*Y\) is positive because its quadratic form is \(\|Yv\|^2\). The same applies on an arbitrary representation space to \(x^*x\) and to \(e x^*x e=(xe)^*(xe)\). Norms of products, adjoints and compressions obey the ITP Section 10.2 bounds; compression by a projection e has norm at most the original norm. This finite argument proves every eigenvalue/norm assertion subsequently used, without a dimension-dependent trace estimate.

### 10.8. A geometric-series inverse in a closed corner

For a unital norm-closed concrete \*-algebra A and a projection e in A, the corner eAe is norm closed. It is exactly the set of z in A satisfying ez=ze=z; these equalities pass to norm limits by bounded multiplication. It is consequently complete, and its identity is e.

If h is in eAe, t>0 and \(\|h-te\|<t\), put \(k=e-h/t\). Then k belongs to eAe and \(\|k\|<1\). The series

\[
g=t^{-1}\sum_{n=0}^\infty k^n,
\qquad k^0=e,
\]

converges in norm in eAe: the tail norm is bounded by a scalar geometric tail. For a partial sum, multiplication by \(h=t(e-k)\) on either side gives e minus the next power of k. That power tends to zero in norm. Passing to the limit proves gh=hg=e. This establishes invertibility in the actual corner rather than in an unspecified ambient algebra. Positivity of h is not required for this inverse argument.

### 10.9. Closed two-sided ideal simplicity with absolute error control

Let J be a nonzero norm-closed complex linear two-sided ideal in Aa and choose \(0\ne x\in J\). Set \(r=\|x\|>0\), \(L=r^2\), \(\delta=L/4\). We have \(x^*x\in J\) because x is in J and \(x^*\) is in Aa; **no assumption that J contains \(x^*\) is made**. The C\*-identity gives \(\|x^*x\|=L\).

Choose \(y\in A_a(E)\) for some finite E with \(\|x-y\|<r/16\), by (GM3). Norm continuity of the adjoint and multiplication yields

\[
\begin{aligned}
\|x^*x-y^*y\|
&\le (\|x\|+\|y\|)\|x-y\|\\
&< (2r+r/16)r/16
=33L/256<\delta. \tag{GM18}
\end{aligned}
\]

This error tolerance depends on x and not on the dimension of the chosen finite matrix algebra. Put \(a=y^*y\). By (GM11) it corresponds to the finite positive matrix \(Y^*Y\); (GM9) verifies both the square and the norm under the concrete realization. Its norm t satisfies

\[
t=\|a\|\ge\|x^*x\|-\|a-x^*x\|>3L/4>\delta. \tag{GM19}
\]

Section 10.7 gives a rank-one matrix eigenprojection e in \(A_a(E)\) with eae=te. Here “rank-one” means rank one in the **finite matrix algebra**; it need not have rank one on the representation Hilbert space, whose multiplicity Q may be arbitrary. The concrete formula (GM9) puts its projection and norm properties in Aa. Thus

\[
h=e x^*x e\in J\cap eA_a e,
\qquad \|h-te\|
=\|e(x^*x-a)e\|<\delta<t. \tag{GM20}
\]

The ideal inclusion uses the two-sided property. Section 10.8 gives g in eAa e with gh=e. Since h is in J and g is in Aa, this proves e is in J.

To pass from e to 1, let u be its unit eigenvector in the finite physical matrix space \(\mathbb C^m\), and let \(\delta_1,\ldots,\delta_m\) be any of that space's standard orthonormal basis vectors. Define matrices

\[
v_i\xi=\delta_i\langle u,\xi\rangle.
\]

Their adjoints are \(v_i^*\xi=u\langle\delta_i,\xi\rangle\). Hence \(v_i^*v_i=e\), \(v_i e v_i^*\) is the projection onto the span of delta_i, and their finite sum is 1. These finite matrices correspond to elements of Aa(E) by formula (GM11). Since e is in J,

\[
1=\sum_{i=1}^m v_i e v_i^*\in J.
\]

A two-sided ideal containing 1 contains every element of Aa, so J=Aa. This proof works also for m=1, including K=0. We have proved

\[
\boxed{\ A_a\text{ is simple for every arbitrary }K.\ } \tag{GM21}
\]

The proof is local after choosing y; it does not use a trace, quotient norm, general quotient C\*-algebra, generic injective-map isometry or prior simplicity of full matrix algebras. In particular it independently gives the full-matrix simplicity statement used in the original Theorem 2.1 proof, while Section 10.4 already proves its required injectivity directly.

### 10.10. The countable finite-tensor completion and its concrete norm

For n at least zero let \(R_n=(\mathbb C^2)^{\otimes n}\), with \(R_0=\mathbb C\), and \(T_n=B(R_n)=M_2^{\otimes n}\) under the concrete finite matrix convention of Section 10.4. The connecting maps are

\[
\iota_n:T_n\to T_{n+1},\qquad X\mapsto X\otimes1_2.
\]

They are unital \*-maps by the finite tensor operator rules and isometric by the upper/lower amplification estimate of ITP Section 10.4. Thus they are injective. The algebraic union can be defined without any abstract inductive-limit theorem: identify (n,X) and (m,Y) when their identity-amplifications agree at a common later stage, and perform addition, multiplication and adjoints there. Injectivity and compatibility make this equivalence relation and those operations well defined; the norm is the common matrix norm at any later stage. Its completion has the continuously extended products and adjoint by the same Cauchy-sequence and product estimates as Section 10.6, and the C\*-identity passes to limits from its finite stages.

For a concrete realization, fix the unit vector \(e_0=(1,0)\in\mathbb C^2\), embed Rn into Rn+1 by \(\xi\mapsto\xi\otimes e_0\), and form the Hilbert completion \(H_{\rm spin}\) of their increasing union. For X in Tn and a vector at a stage Rm with m at least n, act by \(X\otimes1_{2^{m-n}}\). These actions are compatible with every later vector embedding. Every union vector can be moved to a stage m at least n. The finite amplification bound proves the resulting operator on the union has norm at most \(\|X\|\), so it extends to \(H_{\rm spin}\). Testing vectors at stage Rn gives the reverse norm bound. The finite coefficient rules prove multiplication and the adjoint on the dense union and then on its completion. These operators give compatible isometric unital concrete \*-maps of every Tn into B(Hspin).

Their norm-closed generated algebra is therefore the just constructed finite-stage norm completion, with its norm verified concretely. In this proof this is exactly the countable infinite tensor product

\[
\mathcal T=\bigotimes_{j=1}^\infty M_2
\]

appearing in the original formula (7): the completion of the finite spatial matrix tensor algebras under X mapping to X tensor identity. No normal tensor product, state-dependent infinite von Neumann product or general minimal-tensor norm theorem is asserted. The chosen reference vector serves only to exhibit the prescribed finite-stage completion concretely.

### 10.11. Exact compatible countable CAR tensor identification

When K is separable, a countable dense sequence gives an orthonormal basis by finite Gram–Schmidt: at each step subtract its components along the previously chosen finite family, discard a zero residual and normalize each nonzero residual. Each original dense-sequence vector belongs to the span of the family obtained up to its step. Their closed span is consequently K. If K is infinite-dimensional, the retained family cannot be finite; enumerate it as \(f_1,f_2,\ldots\). This proves the needed countable basis existence directly. For finite-dimensional K, formula (GM11) in Section 10.4 already gives the original finite conclusion.

Let \(E_n=\operatorname{span}\{f_1,\ldots,f_n\}\). Every f in K is a norm limit of its finite basis combinations: the coefficient truncations are the orthogonal projections onto En by the finite inner-product formula, their error decreases to zero because the basis span is dense. By (GM5) the corresponding annihilators converge in operator norm, as do their adjoints. For a finite product, approximate each factor and use its finite telescoping expansion; convergent factors have bounded norms, so that expansion makes the product errors tend to zero. This proves

\[
\bigcup_n A_a(E_n)\text{ is norm dense in }A_a. \tag{GM22}
\]

Order these first n basis modes in the displayed order. The finite matrix identification \(\theta_n:A_a(E_n)\to T_n\) from Section 10.4 sends

\[
\theta_n(b_j)=1^{\otimes(j-1)}\otimes E_{12}\otimes1^{\otimes(n-j)},
\]

and consequently, since \(a_j=P_jb_j\),

\[
\theta_n(a_j)=Z^{\otimes(j-1)}\otimes E_{12}\otimes1^{\otimes(n-j)},
\qquad Z=\operatorname{diag}(1,-1),\quad 1\le j\le n. \tag{GM23}
\]

The occupation labels 0,1 of Section 10.4 correspond here to the standard matrix indices 1,2. In n+1 coordinates the same generator expression is the n-coordinate one tensored with 1. Hence

\[
\theta_{n+1}(x)=\theta_n(x)\otimes1
\qquad(x\in A_a(E_n)), \tag{GM24}
\]

first on every generator and \*-polynomial, and then on the entire finite algebra by norm continuity. This supplies exact parity and coordinate inclusion compatibility. It is stronger than agreement of dimensions.

The compatible onto isometries define an onto isometric \*-map of the two algebraic unions. The completed map is constructed by the limits of Section 10.6, using (GM22) on the CAR side and the defining density of the finite tensor stages on the other. Its reversed union map has the same extension; their compositions equal the identity by density. Thus

\[
\boxed{\ A_a\cong\bigotimes_{j=1}^\infty M_2
\quad(K\text{ separable and infinite-dimensional}).\ } \tag{GM25}
\]

For arbitrary nonseparable K, Section 10.2 and Sections 10.5–6 give the directed finite-subspace construction, its overlap-compatible norm completion and representation independence. No countable tensor conclusion is silently extended to that case.

### 10.12. Exact supplied scope and proof mechanism

Section 10.4 proves the complete original finite-mode conclusion of Theorem 2.1 for any finite-dimensional E in arbitrary K and every nonzero concrete CAR family, including d=0 and arbitrary representation multiplicity. Sections 10.5–6 supply the entire intervening generator-matching, finite-subspace overlap and completed-norm construction for **any two** such families. Section 10.9 proves closed two-sided ideal simplicity for arbitrary K. Sections 10.10–11 supply precisely the compatible countable tensor conclusion and Section 10.4 supplies the finite-dimensional conclusion in Corollary 2.2.

The argument combines the arbitrary finite-subspace compatibility/completion arguments and the closed-ideal inverse-corner proof with its elementary finite eigenvalue support. The finite parity and matrix-unit method in Section 8.2 has the explicit “any bounded CAR family on a nonzero Hilbert space” hypothesis. This text reproves each used identity and norm map at that scope. The countable construction in Section 8.1 is not reused as an arbitrary-index theorem. The needed arbitrary-index occupation model is explicitly reconstructed in Section 10.1.

This is a self-contained exact concrete-family support at the stated Hilbert/scalar/choice boundary. It does not close arbitrary covariance or quasifree-state existence/classification, full exterior-Fock or irreducibility proofs, an abstract universal representation theorem, general tensor minimal norms, arbitrary abstract target C\*-algebras, normal representation extensions, GNS/state/predual foundations, strong* Kaplansky density, factor/type/AFD statements, modular theory or any typeIII/core/flow result.


[Jan Dereziński, *Introduction to representations of the canonical commutation and anticommutation relations*, arXiv:math-ph/0511030v2](https://arxiv.org/pdf/math-ph/0511030v2), printed pp.16–17, Section 4.2, supplies the selected Jordan–Wigner method comparison. Its Theorem 10 has no complete proof there. Sections 10.1–10.11 prove the actual identities, norms, compatibility, simplicity and countable completion used here independently.

## 11. Arbitrary covariance and the completed cyclic model

This supplies Theorem 4.1 and its complete Section 4 construction. The one-particle Hilbert space \(K\) is arbitrary; \(T\in B(K)\) is any positive contraction, including a nontrivial kernel or one-eigenspace. Inner products are linear in the second variable. The proof uses this lesson’s Sections 9.1–9.4 for complete arbitrary Fock space, this lesson’s Sections 10.2–10.6 for concrete CAR matrices and norm completions, [ITP Sections 10.1–10.4](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) for concrete Hilbert/operator/tensor foundations, and the positive-root proofs in [*Constant CAR states and the periodic core*, Sections 8.1–8.2](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative). These are the exact consumed inputs. No general spectral theorem, abstract GNS existence theorem, trace, Kaplansky density or modular theorem is required.

### 11.1. Actual roots, endpoint spaces and bounded CAR fields

The periodic CAR lesson’s Sections 8.1–8.2 construct the unique positive square root of every bounded positive operator by an absolutely norm-convergent binomial series. Use that construction in \(B(K)\) to obtain
\[
A=(1-T)^{1/2},\qquad B=T^{1/2}.
\]
It proves \(A^2=1-T\) and \(B^2=T\), with both operators positive and selfadjoint. Their norms are at most one: the concrete C\*-identity of ITP Section 10.2 gives \(\|A\|^2=\|1-T\|\le1\) and \(\|B\|^2=\|T\|\le1\); the selfadjoint quadratic-form norm estimate in the periodic CAR lesson’s Section 8.1 proves the first inequality from \(0\le1-T\le1\). Both roots are norm limits of polynomials in \(T\). Since these polynomials commute, continuity of multiplication gives \(AB=BA\). This conclusion invokes exactly the proved norm-series construction, without diagonalizing \(T\).

The orthogonal-projection and adjoint identities in ITP Section 10.1–10.2 give
\(\overline{\operatorname{ran}C}=(\ker C^*)^\perp\) for any bounded \(C\): a vector is perpendicular to the range precisely when its adjoint image is zero. Therefore put
\[
K_0=\overline{AK}=(\ker A)^\perp,
\qquad K_1=\overline{BK}=(\ker B)^\perp,
\qquad L=K_0\oplus\overline{K_1}.
\]
They are closed Hilbert spaces, and the conjugate-space scalar and inner-product definitions give \(\langle\bar u,\bar v\rangle=\langle v,u\rangle\). Sections 9.1–4 supply the complete antisymmetric Fock space \(\mathcal F(L)\), its unit vacuum \(\Omega_L\), bounded creators \(c_L\) and annihilators \(a_L=c_L^*\), with all their CAR and exact norms. Define
\[
d(f)=a_L(Af\oplus0)+c_L(0\oplus\overline{Bf}). \tag{QC1}
\]
It is conjugate-linear in \(f\). The two one-particle summands are orthogonal. Expanding the anticommutators using Section 9.4 gives \(\{d(f),d(g)\}=0\) and
\[
\begin{aligned}
\{d(f),d(g)^*\}
&=\big(\langle Af,Ag\rangle+\langle\overline{Bg},\overline{Bf}\rangle\big)1\\
&=\langle f,(A^2+B^2)g\rangle1
=\langle f,g\rangle1. \tag{QC2}
\end{aligned}
\]
The cross terms vanish by orthogonality and the same-type CAR. The Fock vacuum makes this representation space nonzero even if \(L=\{0\}\). The arbitrary finite-subspace norm-completion construction gives a unital isometric \*-representation
\(\pi_T:\operatorname{CAR}(K)\to B(\mathcal F(L))\), sending \(a(f)\) to \(d(f)\). It applies to this concrete nonzero CAR family without any abstract universal C\*-norm or representation-existence theorem. The vector functional
\[
\omega_T(x)=\langle\Omega_L,\pi_T(x)\Omega_L\rangle \tag{QC3}
\]
is bounded with norm at most one by Cauchy–Schwarz and the isometric representation; it takes the value one at the identity and is positive because \(\omega_T(x^*x)=\|\pi_T(x)\Omega_L\|^2\). It is consequently a norm-one state on the entire norm-closed algebra.

### 11.2. All determinant signs, including unequal lengths

Let
\[
W_{r,s}=\langle\Omega_L,d(f_1)^*\cdots d(f_r)^*
d(g_s)\cdots d(g_1)\Omega_L\rangle.
\]
A creator on the far left has zero vacuum expectation, since its adjoint kills \(\Omega_L\). An annihilator on the far right kills \(\Omega_L\). In a pure product of the \(d(g_i)\), any first-leg annihilator anticommutes through the remaining second-leg creators with zero scalar contraction and ultimately kills the vacuum. The surviving term uses only second-leg creators, so has particle degree \(s\). For \(s>0\) its vacuum expectation is zero. A pure product of adjoints has the same argument with the two legs interchanged and has degree \(r\), so its vacuum expectation is zero for \(r>0\). The empty product has expectation one.

When \(r,s>0\), expand the leftmost
\(d(f_1)^*=c_L(Af_1\oplus0)+a_L(0\oplus\overline{Bf_1})\).
Its creator term has zero expectation on the far left. Write \(b_1=a_L(0\oplus\overline{Bf_1})\). Its anticommutator with each of the remaining \(r-1\) adjoint fields is zero, so moving it past those fields contributes \((-1)^{r-1}\). Moving it next through \(d(g_s),\ldots,d(g_1)\) gives the scalar contraction
\[
\{b_1,d(g_i)\}=\langle\overline{Bf_1},\overline{Bg_i}\rangle1
=\langle g_i,Tf_1\rangle1.
\]
There are exactly \(s-i\) preceding fields in that reversed list. The term finally carrying \(b_1\) to the far right is zero. Thus the finite CAR expansion yields the exact recurrence
\[
W_{r,s}=\sum_{i=1}^s(-1)^{r-1+s-i}\langle g_i,Tf_1\rangle
\langle\Omega_L,d(f_2)^*\cdots d(f_r)^*
d(g_s)\cdots\widehat{d(g_i)}\cdots d(g_1)\Omega_L\rangle. \tag{QC4}
\]
If \(r\ne s\), each recurrence term decreases both lengths by one, eventually reaching a nonempty pure product whose expectation is zero. Induction proves \(W_{r,s}=0\). If \(r=s=n\), its sign is \((-1)^{2n-i-1}=(-1)^{i+1}\), exactly the cofactor sign of row \(i\) in the first column of \([\langle g_i,Tf_j\rangle]_{i,j=1}^n\). Induction from the empty determinant gives
\[
W_{r,s}=
\begin{cases}
\det[\langle g_i,Tf_j\rangle]_{i,j=1}^n,&r=s=n,\\
0,&r\ne s.
\end{cases} \tag{QC5}
\]
All vectors here are arbitrary. The proof uses their actual bounded fields, not finite-support restrictions. Repeated or linearly dependent entries are included by the same finite recurrence; no Wick or pairing theorem is used.

Every word in the original CAR algebra is a finite linear combination of normal words with all creators on the left. For a proof of termination, order the pair of nonnegative integers (word length, number of annihilator-before-creator inversions) lexicographically. Replacing an adjacent inverted pair by its scalar CAR contraction minus its swapped pair strictly lowers that pair in each resulting term: the scalar term lowers length by two, and the swapped term preserves length but lowers inversions by one. Induction terminates. Thus normal words span the polynomial \*-algebra, which is norm dense by the definition of \(\operatorname{CAR}(K)\). Two bounded states having (QC5) agree there and hence on the whole algebra. This proves the full existence and uniqueness statement of original Theorem 4.1 without presupposing an abstract quasifree state theorem.

### 11.3. The whole reduced doubled Fock space is cyclic

Let \(C\) be the closed span of \(\pi_T(\operatorname{CAR}(K))\Omega_L\). It contains the vacuum. Direct action on the vacuum gives
\[
d(f)^*\Omega_L=Af\oplus0,
\qquad d(f)\Omega_L=0\oplus\overline{Bf}. \tag{QC6}
\]
Define the accessible one-particle set as the union of these two sets of vectors. Its linear span is dense in \(L\), by the definitions of \(K_0\) and \(K_1\). No inverse of \(A\) or \(B\) is claimed or required.

For an accessible vector \(w=Af\oplus0\), choose \(h=d(f)^*\); for \(w=0\oplus\overline{Bf}\), choose \(h=d(f)\). In either case \(h\) is \(c_L(w)\) plus an annihilator from the other leg. For a finite list \(w_1,\ldots,w_n\) of accessible vectors with their chosen fields \(h_1,\ldots,h_n\), expand \(h_1\cdots h_n\Omega_L\). The term choosing every creator is exactly \([w_1,\ldots,w_n]\) by Section 9.3. A different term includes at least one annihilator. Applying Section 9.4 successively shows that any nonzero such term is a finite linear combination of wedges made from a subset of the creator vectors in that term, of final degree at most \(n-2\): each creator raises degree by one and each annihilator lowers it by one; acting on the vacuum with negative degree gives zero. All those creator vectors are accessible.

Induct on \(n\). The vacuum and accessible degree-one vectors lie in \(C\). Assume all accessible wedges of lower degrees lie in \(C\). The entire product vector lies in \(C\), because all fields are in the represented algebra. So does its lower-degree sum, by the induction hypothesis. Subtraction puts \([w_1,\ldots,w_n]\) in \(C\). Multilinearity puts wedges from the linear span of accessible vectors in \(C\). They are dense in \(\Lambda^nL\): approximate each factor of an arbitrary product wedge by that dense linear span, using the tensor product norm and the bound
\(\|[v_1,\ldots,v_n]\|\le\sqrt{n!}\prod_j\|v_j\|\); these arbitrary product wedges are total by Section 9.2. Since \(C\) is closed, it contains every particle degree, and finite-degree vectors are dense in Fock by Section 9.3. Therefore \(C=\mathcal F(L)\).

This proves cyclicity of the entire completed reduced doubled model, including endpoints. For \(T=0\), \(K_1=0\) and the model is the ordinary Fock vacuum. For \(T=1\), \(K_0=0\) and the second leg gives the filled model. No assertion of cyclicity on the larger unreduced \(\mathcal F(K\oplus\overline K)\) is substituted at these endpoints.

### 11.4. The explicit completed GNS identification and gauge invariance

For this actual state put
\(N=\{x:\omega_T(x^*x)=0\}\).
Equation (QC3) shows that \(N\) is the kernel of the linear map \(x\mapsto\pi_T(x)\Omega_L\), so it is a linear subspace. It is a left ideal because
\(\|\pi_T(yx)\Omega_L\|\le\|y\|\|\pi_T(x)\Omega_L\|\).
The vector identity
\[
\omega_T(x^*y)=\langle\pi_T(x)\Omega_L,\pi_T(y)\Omega_L\rangle
\]
makes this a well-defined positive definite inner product on the quotient \(\operatorname{CAR}(K)/N\). Left multiplication by \(y\) is bounded there with norm at most \(\|y\|\), and its adjoint is left multiplication by \(y^*\), directly from that identity. Complete the quotient by the Cauchy-sequence Hilbert completion proved in ITP Section 10.3. The left maps extend to its completion \(H_{\omega_T}\), and the class \([1]\) is a unit cyclic vector, since the quotient classes themselves form the dense orbit.

The rule
\[
U[x]=\pi_T(x)\Omega_L
\]
is an isometry on the quotient. It extends to the Hilbert completion. Its range is closed by completeness of the domain and the Cauchy-preimage argument, and dense by Section 11.3, so it is onto \(\mathcal F(L)\). It sends \([1]\) to \(\Omega_L\) and intertwines every left multiplication with \(\pi_T(y)\), first on quotient classes and then everywhere by boundedness. This proves exactly the whole completed cyclic model in Section 4; an abstract GNS theorem is not an additional prerequisite of this construction.

For a scalar \(z\) with \(|z|=1\), define the unitary on \(L\) by \(V_z=z1_{K_0}\oplus\bar z1_{\overline{K_1}}\). Its finite tensor powers commute with the antisymmetrizers, since applying the same map in every tensor coordinate commutes with every coordinate permutation. Restricting those tensor unitaries to \(\Lambda^nL\) gives unitaries with their inverse restrictions, and their orthogonal direct sum \(\Gamma(V_z)\) is a unitary on full Fock: it preserves every squared degree norm and has inverse \(\Gamma(V_z^{-1})\). It fixes the vacuum. The creation formula (AF4) in Section 9.3, applied to product wedges, gives
\[
\Gamma(V_z)c_L(w)\Gamma(V_z)^*=c_L(V_zw),
\qquad
\Gamma(V_z)a_L(w)\Gamma(V_z)^*=a_L(V_zw).
\]
Density and boundedness extend both identities to all of Fock. Substitution in (QC1), using conjugate linearity of annihilation, gives
\[
\Gamma(V_z)d(f)\Gamma(V_z)^*=\bar z\,d(f)=d(zf). \tag{QC7}
\]
The arbitrary finite-subspace norm-completion map identifies the assignment \(a(f)\mapsto a(zf)\) with an isometric automorphism of \(\operatorname{CAR}(K)\): the inverse assignment uses \(\bar z\), and the finite maps match generators. Equation (QC7) and vacuum preservation prove \(\omega_T\circ\alpha_{z1}=\omega_T\) on every element. Taking \(z=e^{i\theta}\) gives original gauge invariance; \(z=-1\) gives evenness. This also proves the second-quantization implementation rather than assuming its existence.

### 11.5. Exact admission boundary and human comparison

The proof here covers the original arbitrary \(K\), arbitrary positive contraction \(T\), all normal-ordered determinant moments, uniqueness, gauge invariance/evenness, and whole reduced doubled-Fock completed GNS identification. It leaves the general factor-center, every-representation AFD, normal-predual, infinite product, modular, semifiniteness, type and core/flow results separate. Positive roots are selected only from their actual proved bounded-operator norm-series scope.

[Jan Dereziński, *Introduction to representations of the canonical commutation and anticommutation relations*, arXiv:math-ph/0511030v2](https://arxiv.org/pdf/math-ph/0511030v2), printed pp.20–23 and p.46, supplies selected Fock and doubled-field comparisons; [Huzihiro Araki, *On quasifree states of CAR and Bogoliubov automorphisms*](https://ems.press/content/serial-article-files/41673?nt=1), printed pp.387–390, supplies the covariance conventions and the complete cyclic-isometry proof of Lemma 4.2 across pp.389–390. Araki’s general norm-reference and existence-to-Lemma-4.6 chain and the unproved selected Fock statements are not inputs. Sections 11.1–11.4 prove the exact consumed construction independently.

## 12. The exact even-leg spatial tensor identification

This supplies the finite and completed spatial norm in original CAR Proposition 3.1. The orthogonal Hilbert subspaces \(L,N\subset K\) may be arbitrary and nonseparable. It uses the supplied arbitrary concrete CAR matrix/norm support, the arbitrary Fock support, and ITP Section 10.1–10.4 only. A representation here is a norm-continuous \*-map into bounded operators; faithfulness means injectivity. We first work on nonzero representation spaces where the unit acts as the identity. Any faithful representation on a larger ambient space reduces to this case: its image \(p\) of the unit is a nonzero orthogonal projection, every image satisfies \(\pi(x)=p\pi(x)p\), and the operators vanish on \((pH)^\perp\). Restriction to \(pH\) preserves their norms and faithfulness. We prove the isometric property and the needed tensor norm independence for these particular algebras explicitly. No general minimal-tensor norm theorem, normal tensor product, trace, GNS, Kaplansky density or modular theorem is assumed.

### 12.1. Parity and exact finite even matrix blocks

The generator-matching completed norm map of the arbitrary matrix support supplies the automorphism \(\gamma\) taking \(a(f)\) to \(-a(f)\); its inverse is itself and it is isometric. Hence \(P_+=(\operatorname{id}+\gamma)/2\) is a bounded projection of norm at most one onto the even algebra. Every even element is a norm limit of even polynomials: apply \(P_+\) to polynomial approximants. Every such polynomial uses only a finite-dimensional subspace of its one-particle space.

For finite-dimensional \(F\subset N\), of dimension \(f\), use its ordered parity/matrix construction. The product parity \(P_F=Z_1\cdots Z_f\) is diagonal on the finite bit basis, with value \((-1)^{|\alpha|}\) at \(\alpha\in\{0,1\}^f\). Each generator anticommutes with it by its single-mode identity and commutation with the other \(Z_j\). Consequently conjugation by \(P_F\) implements \(\gamma\) on this finite algebra, first on its generators and then on every polynomial and its norm closure. The even algebra is precisely
\[
D_F=\{X\in M_{2^f}:P_FX=XP_F\}.
\]
For a matrix unit \(E_{\alpha\beta}\), the commutation relation is equivalent to \((-1)^{|\alpha|}=(-1)^{|\beta|}\). Thus the commuting matrices have exactly their within-parity-block entries. If \(f\ge1\), each parity class has \(2^{f-1}\) elements, by toggling the first bit. Therefore
\[
D_F=M_{2^{f-1}}\oplus M_{2^{f-1}} \tag{ET1}
\]
with its actual block matrix norm, the maximum of the two norms. The parity projections \(p_+,p_-\) are both nonzero and sum to the identity. If \(f=0\), then \(D_F=\mathbb C1\) and there is just one block. These statements follow from the finite explicit matrices, including their full matrix-unit and norm identification; no structure theorem for abstract finite-dimensional C\*-algebras is needed.

### 12.2. Exact norms in any faithful representations of the finite legs

Fix a finite \(E\subset L\), and let \(m=2^{\dim E}\). If \(\pi\) is a faithful representation of \(\operatorname{CAR}(L)\), its restriction to the finite algebra \(\operatorname{CAR}(E)\) has full matrix units summing to \(1\). The explicit multiplicity-unitary construction in the arbitrary matrix support identifies it on its whole representation space as \(X\mapsto X\otimes1_Q\) on \(\mathbb C^m\otimes Q\), for nonzero \(Q\). That construction proves its norm exactly \(\|X\|\), and requires only the matrix-unit identities, not a general isometry theorem.

If \(\rho\) is a faithful representation of \(\operatorname{CAR}(N)_{\rm ev}\), its restriction to \(D_F\) is faithful. For \(f\ge1\), the images of the two parity projections are nonzero orthogonal projections with sum \(1\), by faithfulness and the \*-map identities. Their ranges give an orthogonal decomposition of its whole Hilbert space. On each range the corresponding block matrix units sum to that range's identity. Apply the same multiplicity construction to each block on that range. It identifies the representation of \(D_F\) as
\[
(Y_+,Y_-)\longmapsto
(Y_+\otimes1_{Q_+})\oplus(Y_-\otimes1_{Q_-}),
\quad Q_+,Q_-\ne\{0\}. \tag{ET2}
\]
For \(f=0\), it is the scalar identity representation on its nonzero Hilbert space. The restriction is isometric in each case by the same amplification norm bounds and the direct-sum maximum norm.

The norm continuity of \(\pi,\rho\) makes these local isometries isometric on their whole algebras: finite-subspace elements approximate any element in norm, and their represented images converge in norm by continuity. Taking norms in that convergence yields the whole norm equality. Even local approximation was supplied by Section 12.1, so this step does not require every representation of the even algebra to extend to the whole CAR algebra.

For an algebraic tensor \(z=\sum_j X_j\otimes Y_j\) in \(M_m\odot D_F\), the product representation \(\pi\otimes\rho\) is computed on the Hilbert tensor completion of its representation spaces. Finite tensor associativity, leg interchange and tensor distribution over a two-summand orthogonal sum are unitaries directly from their maps on elementary vectors: product inner products are preserved, their elementary ranges are total, and their inverse elementary maps give surjectivity. The unitary identifications in the preceding paragraphs consequently give the two represented blocks
\[
\left(\sum_jX_j\otimes Y_{j,+}\right)\otimes1_{Q\otimes Q_+},
\qquad
\left(\sum_jX_j\otimes Y_{j,-}\right)\otimes1_{Q\otimes Q_-}. \tag{ET3}
\]
Both multiplicity Hilbert spaces are nonzero, since unit elementary tensors have norm one. ITP Section 10.4 proves that each amplification has exactly the norm of its finite matrix coefficient. Thus
\[
\|z\|_{\pi\otimes\rho}
=\max\left\{\left\|\sum_jX_j\otimes Y_{j,+}\right\|,
             \left\|\sum_jX_j\otimes Y_{j,-}\right\|\right\}. \tag{ET4}
\]
For \(f=0\), the same argument has one block. The matrices here act on \(\mathbb C^m\otimes\mathbb C^{2^{f-1}}\), with the finite Hilbert tensor norm; their entries are the elementary finite tensor matrix entries. Equation (ET4) proves norm independence among every pair of faithful representations of these two particular legs at this finite scope. It also proves injectivity of the represented algebraic tensor: zero in both matrix blocks means all entries of the direct-sum tensor are zero. This is a finite-coordinate assertion, not a general tensor faithfulness theorem.

### 12.3. Completion of the particular spatial tensor norm

At least one faithful representation of each whole leg is available: the complete Fock CAR representation is faithful on its generated algebra by its definition, and its restriction to the even subalgebra is faithful. Use this pair to define the spatial norm on the algebraic tensor \(\operatorname{CAR}(L)\odot\operatorname{CAR}(N)_{\rm ev}\).

It is a genuine norm. To see the required algebraic injectivity for a general finite sum, express it as \(z=\sum_{j=1}^r x_j\otimes y_j\) with linearly independent \(x_j\) in the first leg, by taking a basis of the finite span of its first coefficients and collecting the second ones. Vector coefficient functionals of the faithful first-leg operators separate that finite span: a bounded operator all of whose coefficients are zero is zero, by testing against its image of each vector. Their restrictions therefore span the full dual of this finite-dimensional span. Indeed if that span of functionals were proper, finite linear algebra would give a nonzero vector in its annihilator, contrary to separation. Choose finite linear combinations of those coefficient functionals \(\ell_i\) with \(\ell_i(x_j)=\delta_{ij}\). If the represented tensor is zero, its coefficients between elementary tensors give
\[
\sum_j\langle h,\pi(x_j)k\rangle\langle u,\rho(y_j)v\rangle=0
\]
for every \(h,k,u,v\). Taking each of the finite coefficient combinations \(\ell_i\) gives \(\langle u,\rho(y_i)v\rangle=0\) for all \(u,v\), so \(\rho(y_i)=0\) and faithfulness gives \(y_i=0\). Hence \(z=0\) in the algebraic tensor. This supplies the omitted general finite-sum faithfulness step for these concrete representations.

Finite local tensor elements are dense for this norm. For \(z=\sum_jx_j\otimes y_j\), approximate its finitely many first coefficients by elements in one finite \(E\), and its even second coefficients by elements in one finite \(F\), using directed finite-subspace density and Section 12.1. The tensor operator bound from ITP Section 10.4 gives
\[
\left\|\sum_jx_j\otimes y_j-\sum_jx'_j\otimes y'_j\right\|
\le\sum_j\big(\|x_j-x'_j\|\,\|y_j\|
                   +\|x'_j\|\,\|y_j-y'_j\|\big), \tag{ET5}
\]
which tends to zero. The same estimate holds for any other faithful representation pair, since Section 12.2 proved that both whole representations are isometric. Equation (ET4) equates the norms of every local approximant; taking limits using (ET5) equates the norms of every algebraic tensor. This proves the needed spatial norm independence for these specific CAR/even legs in full generality, and defines their minimal tensor product as the completion for this common faithful spatial norm. No general theorem about arbitrary C\*-algebra tensor norms is used.

### 12.4. Parity cancellation and the onto multiplication map

Take finite \(E\subset L\), \(F\subset N\), and order an orthonormal basis of \(E\oplus F\) with its \(E\) modes first. The exact finite parity-string matrix map gives
\[
a(e_j)\longmapsto a_E(e_j)\otimes1,
\qquad a(f_j)\longmapsto P_E\otimes a_F(f_j). \tag{ET6}
\]
The same second-leg expression with \(P_E\) holds for adjoints. An even second-leg word has an even number of these factors, and \(P_E^2=1\), so it becomes precisely \(1\otimes y\). The first leg becomes \(x\otimes1\). Finite even polynomials span all of \(D_F\) by Section 12.1; in the finite matrix algebra their norm closure is the same finite space. Therefore the finite multiplication map
\[
\operatorname{CAR}(E)\odot\operatorname{CAR}(F)_{\rm ev}
\longrightarrow\operatorname{CAR}(E\oplus F),
\qquad x\otimes y\longmapsto xy
\]
is exactly the inclusion of the finite matrix block tensor in (ET4). The arbitrary matrix support proves that \(\operatorname{CAR}(E\oplus F)\) has that same norm even when it acts with a larger representation multiplicity. Thus multiplication is injective and isometric at every finite scope.

All first-leg operators commute with all even second-leg operators. On a first-leg homogeneous polynomial of degree \(p\) and an even second-leg word of degree \(2q\), moving every field past the other fields gives \((-1)^{2pq}=1\): orthogonality of \(L,N\) makes every mixed scalar CAR contraction zero. General elements follow from norm approximation of their polynomials, using Section 12.1 for the even leg and bounded multiplication. Hence multiplication of algebraic tensors is a \*-map. The finite maps are compatible on overlaps simply because each sends a tensor of actual elements to their same actual product. Every finite list of subspaces is contained in the pair of their finite sums; no common infinite basis or ordering is required.

The isometry on the local tensor union therefore extends uniquely to an isometry on its completion from Section 12.3. Its range is closed, since its domain is complete. It contains every product \(xy\) of arbitrary elements of the two legs by their finite norm approximations. Conversely all its local values are such products. The commuting-leg \*-algebra of finite sums of these products includes the two whole legs, by taking the other factor to be \(1\); it is closed under multiplication and adjoints by commutation. Its norm closure is precisely their generated unital C\*-algebra. We have proved the onto isometric \*-identification
\[
\operatorname{CAR}(L)\otimes_{\min}\operatorname{CAR}(N)_{\rm ev}
\cong C^*(\operatorname{CAR}(L),\operatorname{CAR}(N)_{\rm ev}). \tag{ET7}
\]
For the assertion with the first leg even, order the finite \(N\) modes before the finite \(L\) modes. The same parity cancellation identifies \(\operatorname{CAR}(N)\otimes_{\min}\operatorname{CAR}(L)_{\rm ev}\) with that generated algebra. The Hilbert tensor flip, unitary by product inner products and total elementary ranges, equates the two spatial tensor norms in reverse order, giving precisely \(\operatorname{CAR}(L)_{\rm ev}\otimes_{\min}\operatorname{CAR}(N)\). Zero-dimensional legs have only their scalar identity algebra and are included by the one-block cases above.

### 12.5. Exact boundary and human comparison

This supplies the full original Proposition 3.1 at arbitrary \(L\perp N\), including finite even-block structure, the exact finite norms in every faithful representation, whole algebraic tensor faithfulness, density/norm independence, compatible multiplication completion and both choices of the even leg. It does not supply normal tensor products, tensor commutants, general tensor norm theorems, states, factors, AFD, trace, modular or type conclusions.

[Jan Dereziński, *Introduction to representations of the canonical commutation and anticommutation relations*, arXiv:math-ph/0511030v2](https://arxiv.org/pdf/math-ph/0511030v2), printed pp.16–17, Section 4.2, and pp.20–23, Sections 5.3–5.7, supplies selected Jordan–Wigner, antisymmetry and parity comparisons. Those selected statements do not supply a general spatial tensor-norm proof. Sections 12.1–12.4 give the exact argument independently.

## 13. Factorality for every positive contraction

This section supplies the complete proof of Section 5 and Theorem 5.1 at its original boundary: an arbitrary complex Hilbert space \(K\), an arbitrary bounded positive contraction \(T\) on \(K\), and its full cyclic reduced doubled-Fock representation. Zero-dimensional, nonseparable and endpoint cases are included. Inner products are conjugate-linear in the first variable. Annihilators are conjugate-linear in their vector, and creators are linear.

The proof uses this lesson’s Sections 9.1–9.4 for complete arbitrary Fock space, with irreducibility specifically in Section 9.4; Sections 10.2–10.6, through Section 11.1, for concrete CAR matrices and norm completions; and Sections 11.1–11.4 for the arbitrary-covariance cyclic model, completed GNS identification and Fock gauge implementer. The concrete Hilbert/operator inputs are [ITP Sections 10.1–10.2 and 10.5–10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice), and the positive norm-series roots are supplied by [Constant CAR states and the periodic core, Sections 8.1–8.2](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative). Only these exact proved scopes are used below. This is known-proof reconstruction.

### 13.1. Representation and bounded roots at the exact boundary

Put
\[
A=(1-T)^{1/2},\qquad B=T^{1/2},\qquad
K_0=\overline{AK},\qquad K_1=\overline{BK},\qquad
L=K_0\oplus\overline{K_1}.
\]
The roots here are the positive, norm-convergent series of [Constant CAR Section 8.2](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative). In the norm-closed algebra generated by \(1,T\), the series gives positive selfadjoint operators with
\[
A^2=1-T,\quad B^2=T,\quad AB=BA,\quad A^2+B^2=1.
\tag{GF1}
\]
Indeed, each root is a norm limit of polynomials in \(T\); polynomial commutation passes to the limit by the operator product inequality. The concrete C\*-identity of [ITP Section 10.2](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) gives \(\|A\|^2=\|1-T\|\le1\) and \(\|B\|^2=\|T\|\le1\), using the positive quadratic-form norm estimate of [Constant CAR Section 8.1](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative). All these constructions work in \(B(K)\), including its zero-dimensional instance, without a spectral theorem.

Sections 9.1–9.4 give the complete Hilbert space
\[
\mathcal F_-(L)=\bigoplus_{n\ge0}\Lambda^nL
\]
and bounded fields \(c_L(w)\), \(a_L(w)=c_L(w)^*\), with norm \(\|w\|\) and their CAR. Its vacuum sector is \(\mathbb C\), so this representation space is nonzero even if \(K=0\). Define on it
\[
d(f)=a_L(Af\oplus0)+c_L(0\oplus\overline{Bf}),\qquad f\in K.
\tag{GF2}
\]
Sections 11.1–11.4 supply the CAR, its whole norm-completed representation \(\pi_T(a(f))=d(f)\), the exact quasi-free state, full reduced-Fock cyclicity and the completed GNS unitary. Sections 10.2–10.6 supply only the required concrete norm-completed CAR representation identification in Section 11.1. Thus the model here is precisely the original \(\pi_T\), and
\[
M=\pi_T(\operatorname{CAR}(K))''
\]
is its concrete generated von Neumann algebra. The state need not be faithful. A GNS identification at any smaller faithful/countable boundary would not substitute for Section 11's original-scope result.

### 13.2. The endpoint and middle decomposition, with active legs

Write
\[
H_0=\ker T,\qquad H_1=\ker(1-T),\qquad
H_m=(H_0\oplus H_1)^\perp.
\]
The two kernels are closed by boundedness. They are orthogonal: for \(u\in H_0\), \(v\in H_1\),
\(\langle u,v\rangle=\langle u,Tv\rangle=\langle Tu,v\rangle=0\).
Their sum is closed, since a Cauchy sequence in the sum has Cauchy orthogonal components by Pythagoras. Orthogonal projection ([ITP Section 10.1](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice)) gives
\[
K=H_0\oplus H_m\oplus H_1.
\tag{GF3}
\]
Each endpoint kernel is invariant under \(T=T^*\); its orthogonal complement is invariant by the adjoint identity. Consequently all three spaces reduce \(T\), all polynomials in \(T\), and their norm limits \(A,B\).

One has \(\ker B=H_0\): if \(Tf=0\), then
\(\|Bf\|^2=\langle f,B^2f\rangle=0\); the converse follows from \(T=B^2\). The same argument gives \(\ker A=H_1\). On \(H_0\), the positive restriction of \(A\) squares to the identity and therefore equals the identity by the proved uniqueness of positive roots ([Constant CAR Section 8.2](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative)), while \(B=0\). On \(H_1\), \(A=0\) and \(B=1\) by the same argument. This also covers a zero endpoint space.

For any bounded operator \(S\), the adjoint definition gives
\((\operatorname{ran}S)^\perp=\ker S^*\). Orthogonal projection then gives
\(\overline{\operatorname{ran}S}=(\ker S^*)^\perp\); no closed-range hypothesis is needed. Apply this to the selfadjoint \(A,B\) to obtain
\[
K_0=H_0\oplus H_m,\qquad K_1=H_m\oplus H_1.
\tag{GF4}
\]
Equivalently, the selfadjoint restrictions of \(A,B\) to \(H_m\) have zero kernel and dense range there. In particular, if \(f\in H_m\), then both \(Af\) and \(Bf\) lie in both active legs \(K_0,K_1\). Every field used below is therefore defined on \(L\). None of these conclusions uses an inverse of \(A\) or \(B\).

### 13.3. All complementary anticommutators

For \(f\in H_m\), define
\[
b(f)=a_L(Bf\oplus0)-c_L(0\oplus\overline{Af}).
\tag{GF5}
\]
It is conjugate-linear and bounded, with \(\|b(f)\|\le\|Bf\|+\|Af\|\le2\|f\|\). For the following computation set
\[
u_g=Ag\oplus0,\quad v_g=0\oplus\overline{Bg},\quad
s_f=Bf\oplus0,\quad t_f=0\oplus\overline{Af}.
\]
The first and second legs are orthogonal; on the conjugate leg
\(\langle\overline h,\overline k\rangle_{\overline{K_1}}=\langle k,h\rangle_K\).
Using the CAR \(\{a(u),c(v)\}=\langle u,v\rangle1\), and zero anticommutators of two creators or two annihilators, gives
\[
\begin{aligned}
\{d(g),b(f)\}
 &= -\langle u_g,t_f\rangle1+\langle s_f,v_g\rangle1=0,\\
\{d(g),b(f)^*\}
 &=\big(\langle u_g,s_f\rangle-\langle t_f,v_g\rangle\big)1\\
 &=\big(\langle Ag,Bf\rangle-\langle Bg,Af\rangle\big)1\\
 &=\big(\langle g,ABf\rangle-\langle g,BAf\rangle\big)1=0.
\end{aligned}
\tag{GF6}
\]
Taking adjoints of the first and second equalities, and reversing the order in the symmetric anticommutator, gives respectively
\(\{d(g)^*,b(f)^*\}=0\) and \(\{d(g)^*,b(f)\}=0\).
Thus all four claimed anticommutators vanish for every \(g\in K\), \(f\in H_m\), without a diagonalization or a restriction on \(g\).

### 13.4. Parity twisting belongs to the actual commutant

On the complete Fock direct sum let \(P\) multiply the \(n\)-particle sector by \((-1)^n\). The direct-sum norm shows that \(P=P^*=P^{-1}\). On finite exterior vectors, creators increase degree by one and annihilators decrease it by one (and vanish on the vacuum). Hence \(Pa_L(w)=-a_L(w)P\) and \(Pc_L(w)=-c_L(w)P\). Section 9.3's finite-degree density and boundedness extend both equalities to the whole space. In particular \(P\) anticommutes with \(d,d^*,b,b^*\).

If \(h\) is either \(d(g)\) or \(d(g)^*\), GF6 gives
\[
(Pb(f))h=P(-hb(f))=hPb(f).
\]
The same holds for \(Pb(f)^*\). Therefore \(Pb(f)\) and \(Pb(f)^*\) commute with the selfadjoint algebra of all represented CAR polynomials, and with its norm closure \(\mathcal A=\pi_T(\operatorname{CAR}(K))\), since multiplication by a fixed bounded operator is norm continuous.

For any operator set \(S\), \(S\subseteq S''\). This implies \(S'''\subseteq S'\); conversely every element of \(S'\) commutes with every element of \(S''=(S')'\), so \(S'\subseteq S'''\). Thus
\[
M'=\mathcal A'''=\mathcal A',\qquad
Pb(f),\ Pb(f)^*\in M'.
\tag{GF7}
\]
[ITP Section 10.5](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) supplies that \(M\) is a unital selfadjoint weak-operator closed algebra, so its center and adjoints below are concrete operators in the same algebra. GF7 needs no claim that the twisted fields exhaust the commutant.

### 13.5. The exact inverse field identities and joint irreducibility

Since \(A,B\) preserve \(H_m\), for \(f\in H_m\) all terms in the following expressions are valid. GF1 and commutation give
\[
\begin{aligned}
d(Af)+b(Bf)
 &=a_L((A^2+B^2)f\oplus0)
   +c_L(0\oplus\overline{BAf-ABf})\\
 &=a_L(f\oplus0),\\
d(Bf)-b(Af)
 &=a_L((AB-BA)f\oplus0)
   +c_L(0\oplus\overline{(B^2+A^2)f})\\
 &=c_L(0\oplus\overline f).
\end{aligned}
\tag{GF8}
\]
All coefficients here are real signs, so conjugate-linearity of annihilators introduces no hidden change of sign. Taking adjoints gives the corresponding creators and annihilators. For \(f\in H_0\), Section 13.2 gives \(d(f)=a_L(f\oplus0)\). For \(f\in H_1\), it gives \(d(f)=c_L(0\oplus\overline f)\). Their adjoints supply the other two ordinary fields.

By GF4, any \(w\in L\) has the unique form
\[
w=(h_0+h_m)\oplus\overline{k_m+h_1},
\qquad h_0\in H_0,\ h_m,k_m\in H_m,\ h_1\in H_1.
\]
Additivity and adjoints of the preceding identities express \(a_L(w),c_L(w)\) as finite linear combinations of the \(d,d^*,b,b^*\) fields. Therefore an operator commuting with this whole joint selfadjoint family commutes with every ordinary Fock field. The arbitrary-\(L\) irreducibility proved in Section 9.4 makes it scalar. This includes \(H_m=0\) (no complementary fields), \(T=0\), \(T=1\), and \(K=0\).

### 13.6. The implemented gauge action on the whole bicommutant

Section 11.4 supplies, for every scalar \(z\) of modulus one, the one-particle unitary
\[
V_z=z1_{K_0}\oplus\overline z1_{\overline{K_1}},
\]
and the full Fock unitary \(U_z=\Gamma(V_z)\), which fixes the vacuum and satisfies
\[
U_zd(f)U_z^*=d(zf)=\overline z\,d(f).
\tag{GF9}
\]
On every finite exterior vector, composition of the tensor powers gives \(U_zU_w=U_{zw}\); boundedness and finite-degree density extend this to the entire Fock space. Thus \(U_z^*=U_{\overline z}\). It preserves every particle sector and commutes with \(P\). Also \(V_{-1}=-1_L\), so its \(n\)-fold exterior power is \((-1)^n\), giving the whole-space identity
\[
U_{-1}=P.
\tag{GF10}
\]

GF9 and adjoints show that conjugation by \(U_z\) maps represented polynomials onto represented polynomials. A unitary preserves operator norm: the product inequality gives \(\|UxU^*\|\le\|x\|\), and applying it to \(x=U^*(UxU^*)U\) gives the reverse inequality. It therefore maps the entire norm closure \(\mathcal A\) onto itself. For any unitary \(U\) and any operator set \(S\), the defining commutation equations give
\[
(USU^*)'=US'U^*.
\]
Apply this twice to obtain \(U_zMU_z^*=M\). Consequently
\[
\beta_z(x)=U_zxU_z^*,\qquad x\in M,
\tag{GF11}
\]
is a unital \*-automorphism of the whole bicommutant, with inverse \(\beta_{\overline z}\). It maps the center onto itself: if \(x\) commutes with all \(y\in M\), then \(\beta_z(x)\) commutes with all \(\beta_z(y)\in M\). Because \(U_zP=PU_z\), it preserves each parity part of the center. This construction is already on the completed GNS/Fock space furnished by Section 11.4; no abstract normal-GNS extension is invoked.

### 13.7. Concrete normality of the complete gauge action

The actual concrete ultraweak topology of [ITP Section 10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) is generated by
\[
F_{\boldsymbol h,\boldsymbol k}(x)
 =\sum_{n\ge1}\langle h_n,xk_n\rangle,
\quad\sum_n\|h_n\|^2<\infty,\quad\sum_n\|k_n\|^2<\infty.
\]
[ITP Section 10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) proves absolute convergence and the Hilbert sequence construction behind this definition. For each fixed \(z\), unitarity gives square summability of \((U_z^*h_n)_n\), \((U_z^*k_n)_n\), with their square sums unchanged. Termwise the adjoint identity gives
\[
F_{\boldsymbol h,\boldsymbol k}(\beta_z(x))
 =F_{U_z^*\boldsymbol h,U_z^*\boldsymbol k}(x).
\tag{GF12}
\]
Thus every defining ultraweak functional pulls back to another defining functional. Both \(\beta_z\) and its inverse are continuous on \(B(\mathcal F_-(L))\), hence on the relative topology of \(M\), and on its center. They are concrete normal automorphisms in precisely the source's stated sense. No trace, abstract predual or equivalence with an order definition of normality is used.

### 13.8. Scalar phase continuity, including a proved parity phase

For precision the continuity needed next can be built from scalar arithmetic and convergent power series. Set
\[
E(v)=\sum_{n=0}^\infty\frac{v^n}{n!},\qquad z(t)=E(it),\quad t\in\mathbb R.
\]
For \(|v|\le R\), the series is uniformly absolutely convergent: after \(n+1>2R\), the successive absolute terms have ratio at most \(1/2\), which bounds their tail by a geometric series. Absolute convergence permits the Cauchy product; the binomial theorem gives \(E(v)E(w)=E(v+w)\). Conjugation of the series gives \(\overline{E(it)}=E(-it)\), hence \(|z(t)|=1\), \(z(s+t)=z(s)z(t)\), and \(z(-t)=\overline{z(t)}\). For \(|s|,|t|\le R\), the identity for differences of powers gives
\[
|z(t)-z(s)|
 \le |t-s|\sum_{n\ge1}\frac{nR^{n-1}}{n!}
 =|t-s|E(R).
\tag{GF13}
\]
Thus this phase group is continuous at every real parameter.

There is a real parameter \(t_*\) with \(z(t_*)=-1\); the proof does not require importing connectedness of \(\mathbb R\) or the trigonometric period theorem. Let \(C(t)=\operatorname{Re}z(t)\), \(S(t)=\operatorname{Im}z(t)\). Then \(C(0)=1\) and
\[
C(2)=1-2+\frac23+
\sum_{n\ge3}(-1)^n\frac{2^{2n}}{(2n)!}\le-\frac13<0.
\]
Indeed the absolute terms decrease for \(n\ge1\), since their successive ratio is \(4/((2n+2)(2n+1))<1\); pair each negative odd term \(n\ge3\) with its following smaller positive even term. Absolute convergence justifies this pairing and yields a nonpositive tail. By continuity and scalar completeness, there is \(r\in(0,2)\) with \(C(r)=0\). Here is the specific intermediate-value step: take the supremum of the \(s\in[0,2]\) for which \(C(s)>0\). It lies strictly between the endpoints by continuity there. If its value under \(C\) were positive, continuity would produce a larger such \(s\); if negative, continuity would exclude a whole interval just below the supremum, contradicting its defining approximation. Its value is therefore zero. Since \(C(r)^2+S(r)^2=|z(r)|^2=1\), \(z(r)=i\) or \(-i\). Put \(t_*=2r\); the group identity yields \(z(t_*)=z(r)^2=-1\). This supplies the parity phase needed in the original \(\theta=\pi\) step directly: the contradiction consumes occurrence of the phase \(-1\), rather than a numerical value of its real parameter.

### 13.9. Strong and strong\* parameter continuity on the complete space

Choose arbitrary orthonormal bases of \(K_0\) and \(\overline{K_1}\), as supplied by Section 9.1's Zorn argument, and use their disjoint union as an orthonormal basis of \(L\). Sections 9.2–9.3 prove that its finite occupation wedges together with the vacuum are a complete orthonormal basis of the entire Fock space, irrespective of the cardinality of the one-particle basis. A wedge with \(r\) basis vectors from the first leg and \(s\) from the second is multiplied by \(U_{z(t)}\) by the scalar
\[
z(t)^r\overline{z(t)}^{s}=z((r-s)t).
\tag{GF14}
\]
This follows directly from the tensor-power construction in Section 11.4, not from a claim about arbitrary infinite tensor products. GF13 makes the image of any finite linear combination of these wedges continuous in Hilbert norm.

For arbitrary \(\xi\) and \(\varepsilon>0\), choose such a finite linear combination \(\eta\) with \(\|\xi-\eta\|<\varepsilon\). Since all the \(U_{z(t)}\) are unitary,
\[
\|(U_{z(t)}-U_{z(s)})\xi\|
 \le2\varepsilon+\|(U_{z(t)}-U_{z(s)})\eta\|.
\]
First let \(t\to s\), then let \(\varepsilon\downarrow0\). This proves strong continuity on every vector. Its adjoint family is \(U_{z(-t)}\), so it is strongly continuous too: the unitary family is strong\* continuous on the whole completed space.

Write \(U_t=U_{z(t)}\) and \(\beta_t=\beta_{z(t)}\). For a fixed bounded operator \(x\) and vector \(\xi\),
\[
\|(\beta_t(x)-\beta_s(x))\xi\|
\le \|x\|\,\|(U_t^*-U_s^*)\xi\|
    +\|(U_t-U_s)xU_s^*\xi\|\longrightarrow0.
\tag{GF15}
\]
Apply the same estimate to \(x^*\), using \(\beta_t(x)^*=\beta_t(x^*)\), to get strong\* parameter continuity for every \(x\in B(\mathcal F_-(L))\), in particular every \(x\in M\) and every central \(x\). Also \(\beta_{s+t}=\beta_s\beta_t\) and \(\beta_0=\mathrm{id}\) by the already proved scalar and Fock group identities. These are whole-operator assertions; continuity merely on polynomials would not suffice.

### 13.10. The even center is scalar

Equations (GF10)–(GF11) show that conjugation by \(P\) preserves \(M\), its center, and adjoints. Suppose \(x\in\mathcal Z(M)\) is even: \(PxP=x\), equivalently \(Px=xP\). Every \(y\in M'\) commutes with \(x\), because \(x\in M=(\mathcal A')'\) and \(M'=\mathcal A'\) by GF7. In particular \(x\) commutes with \(Pb(f)\) and \(Pb(f)^*\). Multiplying the first equality by \(P\) and using \(Px=xP\) gives \(xb(f)=b(f)x\); the second gives \(xb(f)^*=b(f)^*x\). Centrality gives commutation with every \(d(g),d(g)^*\in M\). The joint irreducibility proved in Section 13.5 therefore makes \(x\) scalar. Thus
\[
\mathcal Z(M)_{\mathrm{even}}=\mathbb C1.
\tag{GF16}
\]

### 13.11. A hypothetical odd center and its elimination

Every \(x\in\mathcal Z(M)\) splits as
\[
x=\frac{x+PxP}{2}+\frac{x-PxP}{2},
\]
an even and an odd central element. If the odd part is nonzero, choose a nonzero odd central \(w\). Its real and imaginary parts
\((w+w^*)/2\) and \((w-w^*)/(2i)\) are selfadjoint odd central elements, since parity preserves adjoints. At least one is nonzero; call it \(z_0\). Its square is even central, so GF16 gives \(z_0^2=c1\). For a unit vector \(\xi\), \(c=\langle\xi,z_0^2\xi\rangle=\|z_0\xi\|^2\ge0\); this also shows \(c\) is real. The concrete C\*-identity gives \(c=\|z_0^2\|=\|z_0\|^2>0\). Normalize \(z=z_0/\sqrt c\). Then
\[
z=z^*,\quad z^2=1,\quad PzP=-z.
\tag{GF17}
\]
For any odd central \(w\), \(zw\) is even central and therefore scalar. Multiplication by \(z\), whose square is one, gives \(w\in\mathbb Cz\). Hence
\(\mathcal Z(M)=\mathbb C1\oplus\mathbb Cz\); the sum is direct because a nonzero odd element cannot be scalar.

By Section 13.6, each \(\beta_t\) preserves the odd center. Thus \(\beta_t(z)=\lambda_tz\) for a scalar \(\lambda_t\). Preservation of the adjoint makes \(\lambda_t\) real, and preservation of the square gives \(\lambda_t^2=1\). Therefore its only values are \(+1,-1\).

Fix one unit vector \(\xi\) in the nonzero Fock space. Strong continuity at zero, GF15, gives \(\delta>0\) such that
\[
\|(\beta_h(z)-z)\xi\|<1\quad\text{whenever }|h|<\delta.
\]
If \(\lambda_h=-1\), the left side is \(2\|z\xi\|=2\), since GF17 makes \(z\) unitary. Hence \(\beta_h(z)=z\) for every such \(h\). For any real \(t\), choose a positive integer \(n\) with \(|t|/n<\delta\). The group identity gives
\(\beta_t=\beta_{t/n}^{n}\), so \(\beta_t(z)=z\). This is the complete discrete-sign argument; it uses the Archimedean property and explicit parameter continuity, with no connectedness theorem.

For the real \(t_*\) constructed in Section 13.8, \(z(t_*)=-1\). GF10 gives \(U_{t_*}=P\), so GF17 gives
\(\beta_{t_*}(z)=PzP=-z\), contradicting the preceding conclusion. The odd center is zero. Together with GF16 this proves
\[
\boxed{\mathcal Z(M_T)=\mathbb C1}
\]
for every positive contraction \(T\) on every complex Hilbert space \(K\). Thus the full original Theorem 5.1 follows at all its declared endpoints.

### 13.12. Closure map and limits of this support

The exact chain is: concrete Hilbert/projection/adjoint/C\*-identity ([ITP Sections 10.1–10.2](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice)); positive norm-series roots ([Constant CAR states and the periodic core, Sections 8.1–8.2](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative)); arbitrary completed Fock space and its ordinary-field irreducibility (Sections 9.1–9.4, with irreducibility in Section 9.4); concrete norm-completed CAR representation (Sections 10.2–10.6 through Section 11.1); all-covariance reduced cyclic GNS identification and gauge implementer (Sections 11.1–11.4); and the bridges in Sections 13.2–13.11. [ITP Section 10.5](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) supplies only concrete generated-algebra closure, and [ITP Section 10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) supplies only the square-summable coefficient topology for the normality sentence. The center contradiction itself is already established by the strong continuity proved here.

Every assertion used in Section 5 has a full proof in this exact chain. The continuous normally acting gauge group is justified by Sections 13.6–13.9, and the connectedness step is supplied directly by the elementary subdivision argument in Section 13.11. Thus Theorem 5.1 holds at its original arbitrary-space and arbitrary-positive-contraction boundary, including all endpoints.

This argument does not assert generation of the full commutant by twisted fields, arbitrary tensor minimal-norm results, abstract normal-GNS extension, AFD/hyperfiniteness, modular action, type classification, continuous core or flow of weights. Those assertions are outside the Section 5 chain.

## 14. Directed finite-dimensional approximation in every CAR representation

This section proves the approximation assertion in Theorem 6.1 for arbitrary one-particle Hilbert spaces and every representation. It proves bounded strong\* density of the actual directed finite-dimensional subalgebras, including degenerate and zero representations. In separable K the subalgebras can form an increasing sequence; the approximating operators still form nets when the representation space is arbitrary. The separate conclusion that each quasifree M\_T is a factor uses Theorem 5.1, with its complete proof in Section 13.

The foundations are ZFC, scalar completeness and concrete Hilbert/operator definitions; [ITP Sections 10.1–10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice); the norm/quadratic-form and norm-series positive-root facts in [Sections 8.1–8.2 of the periodic CAR lesson](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative); and the concrete CAR matrix proofs in this lesson’s Sections 10.2–10.6. Section 10.11's complete separable initial-mode construction is used only for the countable-family conclusion. No normal realization of an abstract algebra, trace duality, Krein–Šmulian, general continuous functional calculus, separability of the representation space, state/GNS theorem or factor classification is used. Inner products are conjugate linear in the first variable.

### 14.1. Strong\* density from the actual unital bicommutant proof

Let A\_0 be a unital selfadjoint complex algebra of bounded operators on an arbitrary Hilbert space H, and put M=A\_0''. [ITP Section 10.5](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) proves that A\_0 is WOT dense in M, using only finite lists of vectors. Here we supply the simultaneous-adjoint refinement explicitly.

First a closed real linear subspace V of a complex Hilbert space, viewed with real inner product Re〈·,·〉, has a nearest-point projection. For x, choose v\_n in V with squared distances tending to the infimum. The real parallelogram identity, applied to their midpoint in V, makes this sequence Cauchy. Its limit v is in V and minimizes the distance. Expanding the squared distance from x to v+tw for every real t proves Re〈x-v,w〉=0 for w in V. This also gives uniqueness, by testing the difference of two minimizers in V. Thus a vector outside V has a nonzero residual orthogonal to V for this real inner product. No complex-linearity of V is assumed.

Fix ξ\_1,…,ξ\_n in H. In the complete finite Hilbert sum H^(2n), use the real-linear map
\[
J(a)=(a\xi_1,\ldots,a\xi_n,a^*\xi_1,\ldots,a^*\xi_n),
\qquad a\in A_0.
\]
Let V be the norm closure of J(A\_0), a real linear subspace. If J(x) were outside V for some x in M, let r=(h\_1,…,h\_n,k\_1,…,k\_n) be its nonzero projection residual. The real functional
\[
\ell(a)=\operatorname{Re}\sum_{j=1}^n
 \left(\langle h_j,a\xi_j\rangle+
       \langle k_j,a^*\xi_j\rangle\right)
\]
would vanish on A\_0, while ℓ(x)=‖r‖²>0. But Re〈k,a\*ξ〉=Re〈ξ,ak〉, so ℓ is a finite sum of real parts of WOT coefficient functionals. WOT density makes it vanish on M too, a contradiction. Therefore J(x) is in V.

For every ε>0 there is a in A\_0 with
\[
\sum_{j=1}^n\left(
 \|(a-x)\xi_j\|^2+\|(a^*-x^*)\xi_j\|^2\right)<\varepsilon^2. \tag{DA1}
\]
These are precisely finite strong\* tests. Indexing choices by finite vector sets and positive error tolerances, with vector sets increasing and tolerances decreasing, gives a net a\_λ→x strongly\*. No norm bound is asserted at this step; no countable test set or uniform-boundedness principle for an unbounded net is used.

### 14.2. Elementary inverses and a bounded rational map

For any bounded x, put
\[
R_x=(1+x^*x)^{-1},\qquad L_x=(1+xx^*)^{-1}.
\]
Their actual inverses exist by a norm geometric series. For Q=1+x\*x choose a real R>max{1,‖Q‖}, and set d=1-Q/R. The quadratic-form bounds give 0≤d≤(1-1/R)1; the selfadjoint norm equality in [Section 8.1 of the periodic CAR lesson](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative) gives ‖d‖≤1-1/R<1. Consequently \(R^{-1}\sum_{n=0}^{\infty}d^n\) converges in norm and multiplies Q on either side to 1 by the finite geometric identity. It is selfadjoint and has norm at most one, since 〈η,Qη〉≥‖η‖² implies ‖Qη‖≥‖η‖. The same reasoning applies to 1+xx\*. If x belongs to a unital norm-closed concrete algebra, these series belong to that algebra. They commute with their defining squares.

The finite identity (1+xx\*)x=x(1+x\*x) implies L\_xx=xR\_x. Define
\[
F(x)=2xR_x=2L_xx. \tag{DA2}
\]
It is a contraction. Indeed,
\[
1-F(x)^*F(x)
=R_x(1-x^*x)^2R_x
=\big((1-x^*x)R_x\big)^*\big((1-x^*x)R_x\big)\ge0.
\]
Applying this quadratic-form inequality to every vector gives ‖F(x)‖≤1. The inverse intertwining also gives F(x)\*=F(x\*) and ‖L\_xx‖≤1/2.

For arbitrary x,z the following identity is exact:
\[
xR_x-zR_z
=L_x\left[(x-z)+x(z^*-x^*)z\right]R_z.
\]
For a fixed vector ξ it yields
\[
\frac12\|(F(x)-F(z))\xi\|
\le \|(x-z)R_z\xi\|
 +\frac12\|(z^*-x^*)zR_z\xi\|. \tag{DA3}
\]
Therefore F is strongly continuous along every strongly\* convergent net to a fixed z, even when that net has no common norm bound. Applying the same estimate to x\*,z\* and using F(x)\*=F(x\*) proves convergence of the adjoints too. Thus F is continuous for the full strong\* topology on B(H).

### 14.3. Bounded strong\* density of a directed locally complete algebra

Suppose A\_0 is an increasing directed union of norm-closed unital concrete \*-algebras D\_i, all with the same identity, and M=A\_0''. For a contraction y in M the positive operator 1-y\*y has its positive root s in M, by the actual norm-series construction in [Section 8.2 of the periodic CAR lesson](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative). Its commutation assertion gives sy\*y=y\*ys. The positive inverse
\[
r=(1+s)^{-1}\in M
\]
is supplied by the same geometric-series proof, or by the proof in Section 14.2 for a positive operator bounded below by 1. It commutes with s and y\*y.

Put G(y)=yr. As r commutes with s, finite multiplication gives
\[
G(y)^*G(y)=r(1-s^2)r=(1-s)(1+s)^{-1},
\]
and hence
\[
1+G(y)^*G(y)=2(1+s)^{-1},\qquad F(G(y))=y. \tag{DA4}
\]
Section 14.1 gives a net a\_λ in A\_0 tending strongly\* to G(y). Each a\_λ lies in one D\_i. The inverse series in Section 14.2 then stays in that complete D\_i, so F(a\_λ) belongs to D\_i and has norm at most one. Section 14.2 continuity proves
\[
F(a_\lambda)\longrightarrow y\quad\text{strongly*}.
\]
Thus the unit ball of the actual directed local union is strong\* dense in the unit ball of M. Scaling gives the assertion for any fixed radius, with no inflation of the norm bound. Conversely every strong\* limit belongs to M by WOT closedness, and a limit of contractions is a contraction by its vector norm bounds.

This is the required specialized Kaplansky step. It consumes no assertion that the union of bounded closures is closed, no abstract predual identification, no Krein–Šmulian theorem and no general functional-calculus continuity theorem.

### 14.4. Every CAR representation, including degeneracy

Let π:CAR(K)→B(H) be a complex \*-representation, and put e=π(1). Then e is an orthogonal projection and π(x)=eπ(x)e. On eH the representation is unital. Its norm continuity follows even if not included in the definition of representation: the algebraic concrete unital \*-map contractivity proved in Section 10.6 applies on eH; the zero complementary action preserves its norm on H. The zero representation is handled separately below.

For finite-dimensional E⊂K, write
\[
A_E=\pi(\operatorname{CAR}(E)),\qquad
D_E=A_E+\mathbb C(1-e). \tag{DA5}
\]
When e≠0, the represented fields on eH are an actual bounded CAR family with identity 1\_(eH). Sections 10.3–10.4 give an onto isometric matrix identification A\_E≅M\_(2^dim E), with arbitrary representation multiplicity and including E=0. In particular A\_E is finite-dimensional and norm closed. Its operators vanish on (1-e)H. If that complement is nonzero, D\_E is the direct sum of this matrix algebra and its scalar identity algebra; if the complement is zero, D\_E=A\_E. In either case D\_E is a norm-closed finite-dimensional unital \*-algebra on H.

If e=0 then π=0 and D\_E=ℂ1\_H for every E. If H=0 these are the zero operator algebra and every density assertion is immediate. These zero cases require no nonzero-representation matrix assertion.

These finite algebras are WOT closed, so they are finite-dimensional von Neumann subalgebras on H. To check this directly, use Section 10.4's onto unitary to write an active matrix image as X⊗1\_Q, with Q nonzero. Fix a unit η in Q. Its coefficients between δ\_α⊗η and δ\_β⊗η recover every finite matrix entry of X. On a nonzero complementary scalar block fix a unit vector to recover its scalar. If a net in D\_E has a WOT limit, these finitely many scalar entries converge. Their limits define an element of D\_E, and the finite matrix-unit expansion bounds the norm difference by the sum of their absolute entry differences. Thus the net also converges in norm to that element; uniqueness of the WOT limit proves closedness. The scalar-only and zero cases give the same conclusion directly.

Finite-dimensional subspaces of arbitrary K form a directed set under inclusion, since a finite sum of them is finite-dimensional. E⊂F gives D\_E⊂D\_F. Their union D\_0 is a unital selfadjoint algebra. Every polynomial in finitely many represented fields lies in one A\_E. Section 10.2 polynomial density and the just established continuity show that ∪\_E A\_E is norm dense in π(CAR(K)). Thus D\_0 and π(CAR(K)) have exactly the same commutant: commuting passes to norm limits, and adjoining 1-e adds no condition because any operator commuting with π(CAR(K)) already commutes with e. Consequently
\[
D_0''=\pi(\operatorname{CAR}(K))''=M_\pi. \tag{DA6}
\]
Section 14.3 proves that the directed union of the D\_E has strong\* dense unit ball in M\_π. This proves the full directed finite-dimensional approximation claim for every K and every representation.

The degenerate bicommutant description also follows directly. For H=eH⊕(1-e)H, commutation with e forces block diagonality, giving
\[
\pi(\operatorname{CAR}(K))'
=\pi_e(\operatorname{CAR}(K))'\oplus B((1-e)H).
\]
The commutant of B(J) is ℂ1\_J for every nonzero Hilbert space J: fix a unit u; an operator commuting with the projection onto ℂu sends u to λu. Commuting with all rank-one maps ξ↦h〈u,ξ〉 then gives Th=λh for every h. Zero J is included with its zero identity. Therefore
\[
M_\pi=\pi_e(\operatorname{CAR}(K))''\oplus\mathbb C1_{(1-e)H}.
\]
Adding ℂ(1-e) to each local image approximates this full bicommutant, rather than only the supported active corner.

### 14.5. What separability changes, and what it does not

If K is separable, the complete finite Gram–Schmidt and density construction in Section 10.11 supplies a finite or countable orthonormal basis. Take E\_n to be its initial finite spans, with repetitions if K is finite-dimensional and E\_n=0 when K=0. Section 10.11, using Section 10.3 generator norm continuity and telescoping finite products, proves that ∪\_n CAR(E\_n) is norm dense in CAR(K). Thus the increasing sequence D\_(E\_n) has the same bicommutant as the directed family, and Section 14.3 applies to this union as well.

This is a sequence of finite-dimensional subalgebras whose union is strong\* dense. It does not assert that every operator in an arbitrary representation space is a strong\* limit of a sequence of local operators. The proof uses finite-vector-test nets. Neither a separable representation Hilbert space nor a metrizable strong\* unit ball follows from separability of K alone.

For nonseparable K, the family remains indexed by all finite-dimensional subspaces. No countable family is substituted. Increasing refers to the inclusion-ordered family of algebras, not to operator-order monotonicity of the approximating contractions.

### 14.6. Normal tests and the conclusion of Theorem 6.1

The strong\* approximants from Section 14.3 have an explicit common norm bound. They also converge under the concrete countable-amplification tests used in [ITP Section 10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice). If x\_λ→x strongly and ‖x\_λ‖,‖x‖≤C, and (ξ\_n) is square summable, then
\[
\sum_n\|(x_\lambda-x)\xi_n\|^2
\]
tends to zero: a finite initial sum tends to zero, and its remaining tail is at most 4C²∑\_(n>N)‖ξ\_n‖². The same argument for adjoints proves the corresponding amplified strong\* convergence.

For the concrete ultraweak coefficients from [ITP Section 10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice), finite initial sums converge and the remaining difference tail obeys
\[
\left|\sum_{n>N}\langle h_n,(x_\lambda-x)k_n\rangle\right|
\le2C\left(\sum_{n>N}\|h_n\|^2\right)^{1/2}
       \left(\sum_{n>N}\|k_n\|^2\right)^{1/2}.
\]
Consequently bounded strong\* approximation also supplies concrete ultraweak approximation. No normal representation of the starting C\*-algebra, faithful state, trace or abstract normal-functional decomposition is needed for the AFD clause.

This proves the approximation conclusion in Theorem 6.1: a countable increasing family when K is separable and an increasing directed family when K is arbitrary, in every representation including the degenerate full-space bicommutant. In particular each supplied quasifree representation is approximated at its actual one-particle/representation cardinality. The assertion that M\_T is a factor is the separate conclusion of Theorem 5.1, proved in Section 13; factorality is not inferred from approximation.

For comparison, the rational map and inverse branch also appear in the retained complete solution to Exercise 14.1 in Kaplansky's density theorem and its consequences. Sections 14.1–14.6 prove all the identities and topology steps needed here, including the inverse and positive-root constructions at their stated scope. The comparison is not a construction premise; the trace-duality and Krein–Šmulian dependencies of that lesson's Section 7 are not used.

## 15. Reducing blocks, finite densities and completed product states

This section proves the product identity, finite density formula and normal product identification in Section 6, equations (17), (18) and (19). For (17), the orthogonal reducing blocks may be arbitrary Hilbert spaces and the block index set may be arbitrary; only finitely many distinct blocks occur in each product. For (18), the reducing subspace is finite-dimensional and its eigenvalues belong to \([0,1]\). For (19), an actual finite or countably infinite complete eigenbasis is supplied, with an arbitrary sequence \(p_j\in[0,1]\). No eigenbasis is asserted for a general infinite-dimensional covariance.

The proof uses the arbitrary Fock construction in this lesson’s [Sections 9.1–9.4](car-fock-and-quasifree-states.md#9-arbitrary-hilbert-space-fock-foundations), concrete matrix/norm maps and finite positive eigenbasis proof in [Sections 10.2–10.7](car-fock-and-quasifree-states.md#10-concrete-car-matrix-algebras-completions-and-simplicity), finite tensor completion and initial-mode compatibility in [Sections 10.10–10.11](car-fock-and-quasifree-states.md#10-concrete-car-matrix-algebras-completions-and-simplicity), and determinant, normal-ordering and completed cyclic quasifree construction in [Sections 11.1–11.4](car-fock-and-quasifree-states.md#11-arbitrary-covariance-and-the-completed-cyclic-model). Hilbert completions, finite tensor operators, the bicommutant theorem and the concrete ultraweak topology are proved in [ITP Sections 10.1–10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice). The norm-series positive-root construction used in the covariance model is in [Sections 8.1–8.2 of the periodic CAR lesson](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative). The [even-leg spatial result in Section 12](car-fock-and-quasifree-states.md#12-the-exact-even-leg-spatial-tensor-identification) supplies no normal tensor-product or tensor-commutant premise here. The baseline is ZFC, scalar completeness and concrete Hilbert/operator definitions. Inner products are conjugate linear in the first argument.

Write \(a(f)\) for the conjugate-linear CAR annihilator. The actual bounded state \(\omega_T\) and its reduced doubled-Fock representation \((\pi_T,\mathcal F(L_T),\Omega_T)\) are those of [CAR Section 11](car-fock-and-quasifree-states.md#11-arbitrary-covariance-and-the-completed-cyclic-model). Their whole norm-closed CAR algebra is used below. In particular the consumed determinant formula, including unequal lengths, is
\[
\omega_T\!\left(a(f_1)^*\cdots a(f_n)^*
a(g_m)\cdots a(g_1)\right)
=
\begin{cases}
\det[\langle g_i,Tf_j\rangle]_{i,j=1}^n,&m=n,\\
0,&m\ne n.
\end{cases} \tag{VP1}
\]
The empty determinant is one. [CAR Section 11.2](car-fock-and-quasifree-states.md#11-arbitrary-covariance-and-the-completed-cyclic-model) proves that normal words span the polynomial algebra by induction on word length and adjacent annihilator-before-creator inversions; its operator-norm closure is the entire CAR algebra. All uses of this formula therefore refer to an existing positive bounded state, rather than to an unverified prescription of moments.

### 15.1. The full finite reducing-block product identity

Suppose \(K=\bigoplus_{j\in J}K_j\) is an orthogonal Hilbert sum and the positive contraction \(T\) reduces every \(K_j\). A generator-matching inclusion identifies \(\operatorname{CAR}(K_j)\) with its actual norm-closed subalgebra of \(\operatorname{CAR}(K)\), by [CAR Sections 10.5–10.6](car-fock-and-quasifree-states.md#10-concrete-car-matrix-algebras-completions-and-simplicity). Its state restriction has covariance \(T|_{K_j}\), because all the entries in (VP1) restrict to those vectors. In particular, for distinct blocks,
\[
\langle g,Tf\rangle=0
\quad(f\in K_j,\ g\in K_k,\ j\ne k). \tag{VP2}
\]
No dimension restriction or diagonalization is involved.

Fix \(r\) distinct blocks in a specified order. First take in block \(\ell\) a normal word
\[
w_\ell=
a(f_{\ell,1})^*\cdots a(f_{\ell,n_\ell})^*
a(g_{\ell,m_\ell})\cdots a(g_{\ell,1}),
\qquad f_{\ell,i},g_{\ell,i}\in K_{j_\ell}.
\]
Empty creator or annihilator lists are allowed. Move the annihilators in each earlier block past the creators in the later blocks. Every cross-block scalar CAR contraction is zero by orthogonality. Hence the resulting global normal word has the sign
\[
(-1)^{\sum_{\ell<k}m_\ell n_k}. \tag{VP3}
\]
Its creator list consists of blocks \(1,\ldots,r\) in order. Its annihilator factors consist of the block annihilator lists in that same order. Consequently the \(g\)-list in the convention of (VP1) consists of blocks \(r,\ldots,1\), with the \(g_{\ell,i}\) in their original internal order.

If \(\sum_\ell n_\ell\ne\sum_\ell m_\ell\), the global expectation is zero by (VP1), and at least one local expectation is zero. If the two totals agree but some \(n_\ell\ne m_\ell\), every term in the determinant is zero: (VP2) forces each row of block \(\ell\) to be paired with a column of that same block, which cannot give a bijection unless their counts agree in every block. The right-hand product again has a zero local factor.

In the remaining case \(n_\ell=m_\ell\) for every \(\ell\). Reordering the determinant's row blocks from \(r,\ldots,1\) to \(1,\ldots,r\) has the sign
\((-1)^{\sum_{\ell<k}n_\ell n_k}\): exchanging two blocks of respective lengths \(n_\ell,n_k\) crosses exactly \(n_\ell n_k\) individual rows. The reordered matrix is block diagonal. Its determinant is the product of the local determinants, by the finite permutation expansion: only permutations preserving each row/column block contribute, and their signs and entries multiply. The row-block sign and (VP3) are equal and cancel. We obtain, in all cases,
\[
\omega_T(w_1\cdots w_r)=\prod_{\ell=1}^r\omega_T(w_\ell). \tag{VP4}
\]
This explicitly accounts for the occupation signs; parity alone is not used to suppress an unbalanced block.

Normal ordering within each block expresses every local polynomial as a finite linear combination of these words. Multilinearity gives (VP4) for all those polynomials. For arbitrary \(x_\ell\in\operatorname{CAR}(K_{j_\ell})\), choose polynomial approximants \(x_{\ell,q}\to x_\ell\) in norm. The norms of each approximating sequence are bounded. The finite telescoping product identity and the boundedness of \(\omega_T\) then give convergence of the left side, and scalar multiplication gives convergence of the right side. Thus
\[
\boxed{\ \omega_T(x_1\cdots x_r)=\prod_{\ell=1}^r\omega_T(x_\ell)
\quad(j_1,\ldots,j_r\ {\rm distinct}).\ } \tag{VP5}
\]
This is original (17) for arbitrary block Hilbert spaces and all finite products, including zero-dimensional blocks. It is not limited to pairwise independence or to even local inputs.

### 15.2. Every finite diagonal covariance density matrix

Let \(E\subset K\) be finite-dimensional and reduce \(T\). Its positive contraction \(T_E=T|_E\) has an orthonormal eigenbasis \(e_1,\ldots,e_d\), with eigenvalues \(p_j\in[0,1]\). The finite positive eigenbasis proof is exactly [CAR Section 10.7](car-fock-and-quasifree-states.md#10-concrete-car-matrix-algebras-completions-and-simplicity): maximize the quadratic form using finite-coordinate convergent subsequences, obtain an eigenvector by scalar variations, restrict to its invariant orthogonal complement, and induct on dimension. The bound \(0\le p_j\le1\) follows by evaluating \(0\le T_E\le1\) on a unit eigenvector. The \(d=0\) case has the empty basis. No infinite-dimensional spectral theorem is used.

Use the isometric occupation-matrix map \(\theta_d:\operatorname{CAR}(E)\to M_{2^d}\) in this order. It sends \(a(e_j)\) to its exact Jordan–Wigner matrix
\(Z^{\otimes(j-1)}\otimes b\otimes1^{\otimes(d-j)}\), where
\[
b=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
In particular \(n_j=a(e_j)^*a(e_j)\) becomes the \(j\)-th bit occupation projection.
Put
\[
q_j(0)=1-p_j,\quad q_j(1)=p_j,\qquad
\rho_d=\bigotimes_{j=1}^d\operatorname{diag}(1-p_j,p_j),\qquad
w_\alpha=\prod_{j=1}^d q_j(\alpha_j). \tag{VP6}
\]
On the occupation basis \(\delta_\alpha\), \(\rho_d\delta_\alpha=w_\alpha\delta_\alpha\).
All weights are nonnegative and their sum is
\(\prod_j(q_j(0)+q_j(1))=1\), by finite expansion. Zero weights at endpoints cause no exception. For \(d=0\), \(\rho_0=1\) on \(\mathbb C\). Define the finite matrix functional explicitly by
\[
\varphi_d(X)=\operatorname{Tr}(\rho_dX)
=\sum_{\alpha\in\{0,1\}^d}w_\alpha\langle\delta_\alpha,X\delta_\alpha\rangle. \tag{VP7}
\]
Here \(\operatorname{Tr}\) is just the finite sum of diagonal matrix entries. The formula proves positivity, \(\varphi_d(1)=1\), and \(|\varphi_d(X)|\le\|X\|\) without trace duality.

We check all normal moments explicitly. By finite expansion of their vector arguments it suffices to use eigenbasis-mode words. Repetition within a creator list or annihilator list makes that word zero by its anticommutators and square-zero relations; it makes the corresponding right-hand side of (VP1) zero too. With distinct indices in each list, a word with unequal lengths, or with unequal creator and annihilator index sets, has no diagonal occupation entry: its nonzero action removes the annihilator index set and inserts the creator index set, so it cannot return an occupation vector to itself unless the two sets are equal.

If both sets are the same set \(S=\{i_1<\cdots<i_n\}\), first sort both lists. The two sorting signs multiply. For the sorted lists the normal word is exactly
\[
a(e_{i_1})^*\cdots a(e_{i_n})^*
a(e_{i_n})\cdots a(e_{i_1})=\prod_{i\in S} n_i. \tag{VP8}
\]
To verify this finite identity, each occupation projection \(n_i\) commutes with all fields of every other mode, because moving either field past its two factors gives two CAR signs. Starting with the innermost pair, then successively commuting its projection past the other modes, proves (VP8) by induction. Its diagonal coefficient is one precisely on occupation labels containing \(S\). Thus its expectation is
\[
\sum_{\alpha:\ \alpha_i=1\ (i\in S)}w_\alpha
=\prod_{i\in S}p_i,
\]
using \(q_j(0)+q_j(1)=1\) on the remaining bits. The sorted diagonal-covariance determinant has the same value. Permuting either of the original lists multiplies both its determinant and its normal word by that list's sorting sign. Therefore all mode words, with every ordering, have exactly (VP1)'s moments. Multilinearity gives every vector normal word, and normal ordering gives the whole finite algebra.
Consequently
\[
\boxed{\ \omega_T(x)=\operatorname{Tr}(\rho_d\,\theta_d(x))
\quad(x\in\operatorname{CAR}(E)).\ } \tag{VP9}
\]
This is original (18) in its actual occupation coordinates. The same proof applies to any finite diagonal covariance; reduction is used here to identify that covariance with \(T|_E\).

### 15.3. The cyclic one-mode matrix model, including endpoints

For each supplied eigenvalue \(p_j\in[0,1]\), write \(q_j(0)=1-p_j\), \(q_j(1)=p_j\), and put
\[
\rho_j=\operatorname{diag}(1-p_j,p_j),\quad
r_j=\operatorname{diag}(\sqrt{1-p_j},\sqrt{p_j}),\quad
C_j=\{\beta\in\{0,1\}:q_j(\beta)>0\},\quad
s_j=\sum_{\beta\in C_j}E_{\beta\beta}.
\]
Every \(C_j\) is nonempty. Define
\[
H_j=M_2s_j,\qquad
\langle Y,V\rangle=\sum_{\alpha=0}^1\sum_{\beta\in C_j}
\overline{Y_{\alpha\beta}}V_{\alpha\beta},\qquad
\Omega_j=r_j. \tag{VP10}
\]
Thus \(H_j\) consists exactly of matrices whose unsupported columns are zero, with its finite Euclidean Hilbert norm. It is complete and nonzero. The vector has norm one since \(\|\Omega_j\|_{H_j}^2=(1-p_j)+p_j=1\).

Left multiplication gives the representation
\(\lambda_j(X)Y=XY\).
It preserves these supported columns. Applying the matrix operator bound separately to each column gives
\(\|\lambda_j(X)Y\|^2\le\|X\|^2\|Y\|^2\).
Conversely choose any supported column \(\beta\); matrices with only that column equal to a unit vector \(v\in\mathbb C^2\) have Hilbert norm one and their image has norm \(\|Xv\|\). Taking the supremum over \(v\) gives
\[
\|\lambda_j(X)\|=\|X\|. \tag{VP11}
\]
Finite coefficient calculation gives the adjoint
\(\lambda_j(X)^*=\lambda_j(X^*)\), and multiplication and the identity are actual left matrix multiplication. This is a unital faithful isometric representation of the full \(M_2\), even at endpoints.

It is cyclic with cyclic vector \(\Omega_j\). Given \(Y\in H_j\), choose \(X\) with column \(Y_{\cdot\beta}/\sqrt{q_j(\beta)}\) for every \(\beta\in C_j\), and set unsupported columns to zero. Then \(Xr_j=Y\). Each division is by a positive scalar in this finite construction; no bound uniform over \(j\) or over nonzero \(q_j(\beta)\) is asserted. Direct summation gives
\[
\langle\Omega_j,\lambda_j(X)\Omega_j\rangle
=\operatorname{Tr}(\rho_jX),\qquad
\langle Xr_j,Yr_j\rangle=\operatorname{Tr}(\rho_jX^*Y). \tag{VP12}
\]
For \(p_j=0\), only column \(0\) is supported and \(\dim H_j=2\); for \(p_j=1\), only column \(1\) is supported and again \(\dim H_j=2\). For \(0<p_j<1\), both columns are supported and \(\dim H_j=4\). In particular an endpoint state has this two-dimensional cyclic space, not the full four-dimensional matrix Hilbert space with an uncoupled column.

The finite matrix state \(\operatorname{Tr}(\rho_jX)\) is concretely normal: it is the sum of the two vector coefficients \(q_j(\beta)\langle\delta_\beta,X\delta_\beta\rangle\), with zero terms allowed. The represented state is the unit-vector coefficient in (VP12), so it is normal for the same concrete topology. No assertion of faithfulness of either state is needed.

### 15.4. The entire countable pointed Hilbert product and its bounded local algebras

Assume first that the supplied complete eigenbasis is infinite, indexed by \(j\in\mathbb N\). Let
\[
H^{(n)}=H_1\otimes\cdots\otimes H_n,\quad H^{(0)}=\mathbb C,
\qquad \Omega^{(n)}=\Omega_1\otimes\cdots\otimes\Omega_n.
\]
These are the actual finite Hilbert tensor completions of [ITP Section 10.3](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice). The embeddings
\(v\mapsto v\otimes\Omega_{n+1}\) preserve inner products because \(\|\Omega_{n+1}\|=1\).
Take the algebraic union by identifying vectors that agree at a common later stage and defining their inner products at that stage. The isometric embeddings make this well defined and positive definite. Complete this inner-product space by Cauchy-sequence classes, exactly as in [ITP Section 10.3](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice). Denote the resulting nonzero Hilbert space by \(H_{\rm prod}\). For clarity, completeness follows by choosing union-vector approximants to each term of a Cauchy sequence of classes with error less than \(2^{-k}\); the resulting union-vector sequence is Cauchy and its class is the limit. The embedded union of all \(H^{(n)}\) is dense by this construction. The consistent images of the \(\Omega^{(n)}\) define a unit vector \(\Omega_{\rm prod}\).

Write \(R_n=(\mathbb C^2)^{\otimes n}\) and \(T_n=B(R_n)=M_{2^n}\). There is an explicit unitary
\[
H^{(n)}\longrightarrow M_{2^n}s^{(n)},\qquad
E_{\alpha_1\beta_1}\otimes\cdots\otimes E_{\alpha_n\beta_n}
\longmapsto E_{\alpha\beta}, \tag{VP13}
\]
where \(\beta_j\in C_j\) and \(s^{(n)}\) is the diagonal projection onto those supported column tuples.
Both sides have exactly this orthonormal basis, so the elementary map is onto and isometric. It sends \(\Omega^{(n)}\) to
\(r^{(n)}=\bigotimes_{j\le n}r_j=\rho_n^{1/2}\).
The finite product representation \(\lambda^{(n)}\) acts under this unitary by left multiplication by \(X\in T_n\). As in (VP11), summing column norms gives the upper bound and a single supported column gives the lower bound:
\[
\|\lambda^{(n)}(X)\|=\|X\|,\qquad
\langle\Omega^{(n)},\lambda^{(n)}(X)\Omega^{(n)}\rangle
=\operatorname{Tr}(\rho_nX). \tag{VP14}
\]
Every supported column tuple has strictly positive product weight. Dividing its column by the corresponding entry of \(r^{(n)}\) proves
\(\lambda^{(n)}(T_n)\Omega^{(n)}=H^{(n)}\).
This is finite-stage cyclic surjectivity, including every combination of endpoint and interior modes.

For \(X\in T_n\), define \(L_n(X)\) on a union vector at stage \(m\ge n\) by
\(\lambda^{(n)}(X)\otimes1_{H_{n+1}\otimes\cdots\otimes H_m}\).
A vector at an earlier stage is first embedded into such a stage. The local actions respect all later pointed embeddings; their multiplication and adjoints do also. [ITP Section 10.4](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) gives the uniform bound \(\|X\|\) on the entire union. Thus they extend uniquely to bounded operators on \(H_{\rm prod}\). Testing vectors at stage \(n\) and using (VP14) proves their exact norms. Their adjoint coefficient identities on the dense union extend everywhere. Therefore
\[
L_n:T_n\longrightarrow B(H_{\rm prod})
\quad\hbox{is a unital isometric *-map},\qquad
L_{n+1}(X\otimes1_2)=L_n(X). \tag{VP15}
\]
In particular \(B_n=L_n(T_n)\) is a full finite matrix algebra and \(B_n\subset B_{n+1}\). Since every stage vector is \(L_n(X)\Omega_{\rm prod}\), the union local orbit is dense in the entire \(H_{\rm prod}\). Let
\[
C_{\rm prod}=\overline{\bigcup_n B_n}^{\,\|\cdot\|}.
\]
It is a concrete unital norm-closed \*-algebra and \(\Omega_{\rm prod}\) is cyclic for it. Its vector state is positive, bounded and of norm one, directly from its action on this unit vector. At every stage it is the product of the \(\operatorname{Tr}(\rho_j\,\cdot)\), by (VP14) and finite sums of tensor matrix units. No theorem constructing an abstract infinite product state has been used.

Each \(B_n\) is already a von Neumann algebra on the whole product space. Fix one supported column tuple \(\beta\). The stage vectors \(E_{\alpha\beta}\) and \(E_{\gamma\beta}\), embedded in \(H_{\rm prod}\), recover the matrix entry \(X_{\alpha\gamma}\) as a coefficient of \(L_n(X)\). If a net in \(B_n\) has a WOT limit, these finitely many entries converge to entries of a matrix \(X\). The matrix-unit expansion and the norm-one local matrix units bound the norm difference to \(L_n(X)\) by the finite sum of absolute entry differences. Thus the same net converges in norm to \(L_n(X)\); uniqueness of WOT limits puts its given limit in \(B_n\). This proves WOT closedness directly.

The maps \(L_n:T_n\to B_n\) are also concretely normal, with normal inverses. For forward continuity, expand \(L_n(X)\) as the finite sum of its matrix entries times the fixed operators \(L_n(E_{\alpha\gamma})\). Any defining countable ultraweak coefficient of that finite sum is a finite linear combination of the input entries; each coefficient series converges absolutely by [ITP Section 10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice). Every input entry is a vector coefficient on \(R_n\), hence a defining ultraweak functional. Inverse continuity follows from the stage-vector entry recoveries just proved. This supplies the finite factors and their represented normality at their actual scope.

### 15.5. Compatible whole CAR norms and local inner products

Let \(Te_j=p_je_j\) be the given complete eigenbasis and \(E_n=\operatorname{span}\{e_1,\ldots,e_n\}\). Each \(E_n\) reduces \(T\). [CAR Section 10.11](car-fock-and-quasifree-states.md#10-concrete-car-matrix-algebras-completions-and-simplicity) proves initial-mode norm density using the exact generator norm and telescoping polynomial products, and supplies onto isometric maps
\[
\theta_n:\operatorname{CAR}(E_n)\longrightarrow T_n,\qquad
\theta_{n+1}(x)=\theta_n(x)\otimes1_2
\quad(x\in\operatorname{CAR}(E_n)). \tag{VP16}
\]
These are the actual parity-string maps, not an identification from matrix dimensions. Combining (VP15) and (VP16) gives a compatible onto isometric map of local algebras,
\[
\Psi_n=L_n\theta_n,\qquad
\|\Psi_n(x)\|=\|x\|,\qquad
\Psi_{n+1}|_{\operatorname{CAR}(E_n)}=\Psi_n. \tag{VP17}
\]
Addition, products and adjoints of elements from different stages are calculated in a common later stage, so this defines an isometric unital \*-map \(\Psi_{\rm loc}\) from the entire initial-mode CAR union onto \(\bigcup_n B_n\).

For local \(x,y\) move to one common stage \(n\). Equations (VP9) and (VP14) give the complete local inner-product identity
\[
\langle\Psi_{\rm loc}(x)\Omega_{\rm prod},
        \Psi_{\rm loc}(y)\Omega_{\rm prod}\rangle
=\operatorname{Tr}\!\big(\rho_n\theta_n(x)^*\theta_n(y)\big)
=\omega_T(x^*y). \tag{VP18}
\]
This includes zero-norm local vectors at endpoints. The actual representation \(\pi_T\) has the same inner products by its defining vector state, and its CAR norm is the same concrete norm by [CAR Section 11.1](car-fock-and-quasifree-states.md#11-arbitrary-covariance-and-the-completed-cyclic-model) and the finite-family norm support.

For any \(x\in\operatorname{CAR}(K)\), choose initial-mode local \(x_k\to x\) in norm and define
\(\Psi(x)=\lim_k\Psi_{\rm loc}(x_k)\).
Local isometry makes these image sequences Cauchy and proves independence of approximants. The limits lie in \(C_{\rm prod}\). The norm equality, addition and adjoints pass to limits. Multiplication passes by
\(\|x_ky_k-xy\|\le\|x_k\|\|y_k-y\|+\|x_k-x\|\|y\|\)
and the same inequality in the target. Thus \(\Psi\) is an isometric unital \*-map.
Its range is closed: convergence of a range sequence gives a Cauchy sequence of preimages by isometry and hence a range limit by completeness. The range contains the whole local union, which is norm dense in \(C_{\rm prod}\), so it is onto. We have proved
\[
\Psi:\operatorname{CAR}(K)\overset{\cong}{\longrightarrow} C_{\rm prod}
\quad\hbox{is onto and isometric},\qquad
\langle\Omega_{\rm prod},\Psi(x)\Omega_{\rm prod}\rangle=\omega_T(x)
\quad(x\in\operatorname{CAR}(K)). \tag{VP19}
\]
The state equality follows first locally from (VP18) with the first argument \(1\), then on the entire algebra by norm continuity. The complete inner-product identity (VP18) likewise extends to all \(x,y\).

### 15.6. Both completed cyclic isometries are onto

For the actual state \(\omega_T\), put
\[
N_T=\{x:\omega_T(x^*x)=0\}.
\]
The equality
\(\omega_T(x^*y)=\langle\pi_T(x)\Omega_T,\pi_T(y)\Omega_T\rangle
=\langle\Psi(x)\Omega_{\rm prod},\Psi(y)\Omega_{\rm prod}\rangle\)
shows that \(N_T\) is the kernel of both linear cyclic-vector maps. It is a linear subspace. It is a left ideal, since
\[
\|\pi_T(zx)\Omega_T\|\le\|z\|\|\pi_T(x)\Omega_T\|.
\]
The same estimate holds in the product representation, by (VP19).
The displayed inner-product equality makes
\(\langle[x],[y]\rangle=\omega_T(x^*y)\)
a well-defined positive definite inner product on \(\operatorname{CAR}(K)/N_T\). There is no division by a zero eigenvalue in this quotient construction. Left multiplication by \(z\) is bounded by \(\|z\|\), has adjoint left multiplication by \(z^*\) from the coefficient identity, and obeys the algebra multiplication rules. Complete the quotient by the actual Cauchy-sequence Hilbert construction to \(H_{\omega_T}\). The left maps extend to a unital representation \(\pi_\omega\) on that whole completion, and \([1]\) is a unit cyclic vector because the quotient classes are its dense orbit.

Define on quotient classes
\[
U_F[x]=\pi_T(x)\Omega_T,\qquad
U_P[x]=\Psi(x)\Omega_{\rm prod}. \tag{VP20}
\]
Their kernels have already been removed, and their full inner-product identities make both maps isometries. Therefore they extend to isometries from \(H_{\omega_T}\) onto closed subspaces of their respective complete targets.
The first range is dense in the entire reduced doubled-Fock space by the proved [CAR Section 11.3](car-fock-and-quasifree-states.md#11-arbitrary-covariance-and-the-completed-cyclic-model) cyclicity: accessible creation components span densely the two active one-particle legs; induction subtracts lower-degree terms from field products to obtain all their wedges; particle-sector totality and finite-degree density give all of \(\mathcal F(L_T)\), including endpoints. The second range contains the dense union of all the finite \(H^{(n)}\), by Section 15.4. Thus both closed ranges are their full targets.

Both maps send \([1]\) to the specified unit cyclic vector. For every \(z\in\operatorname{CAR}(K)\), left multiplication on the quotient gives
\[
U_F\pi_\omega(z)=\pi_T(z)U_F,\qquad
U_P\pi_\omega(z)=\Psi(z)U_P. \tag{VP21}
\]
These equalities extend from the dense quotient classes to all vectors by boundedness. The resulting onto unitary
\[
W=U_PU_F^*:\mathcal F(L_T)\longrightarrow H_{\rm prod}
\]
therefore satisfies
\[
W\Omega_T=\Omega_{\rm prod},\qquad
W\pi_T(x)W^*=\Psi(x)\quad(x\in\operatorname{CAR}(K)). \tag{VP22}
\]
This supplies the completed representation equivalence. An equality of finite moments alone would not provide the closed-range and target-cyclicity assertions proved here.

### 15.7. The actual generated von Neumann algebra and concrete normal state

Define the right-hand side of original (19) by its concrete pointed construction above:
\[
M_{\rm prod}:=\left(\bigcup_n B_n\right)''
=C_{\rm prod}''\subset B(H_{\rm prod}). \tag{VP23}
\]
The equality follows directly because commuting with bounded operators passes to their norm limits. [ITP Section 10.5](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) proves that this bicommutant is the weak-operator generated algebra of the local unital selfadjoint union, on the entire constructed Hilbert space. Thus it is the von Neumann infinite product of the displayed \(M_2\) with their displayed cyclic matrix states in precisely this representation. No tensor-commutant formula or faithful-state assumption enters this definition.

For any set \(S\) of bounded operators, the elementary equivalence
\[
t\in(WSW^*)'\quad\Longleftrightarrow\quad W^*tW\in S'
\]
follows by multiplying each commutation identity by \(W\) or \(W^*\). Applying it twice to (VP22) gives
\[
\Theta:M_T=\pi_T(\operatorname{CAR}(K))''
\longrightarrow M_{\rm prod},\qquad
\Theta(a)=WaW^*, \tag{VP24}
\]
an onto unital \*-isomorphism, with inverse \(b\mapsto W^*bW\).
It is concretely normal in both directions. In the exact ultraweak topology of [ITP Section 10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice), for square-summable vector lists \((h_n),(k_n)\) in \(H_{\rm prod}\),
\[
\sum_n\langle h_n,\Theta(a)k_n\rangle
=\sum_n\langle W^*h_n,aW^*k_n\rangle. \tag{VP25}
\]
The transformed lists are square summable with the same squared norm sums, because \(W\) is unitary. The series converge absolutely by the actual coefficient bound of [ITP Section 10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice). Thus each defining ultraweak coefficient pulls back to another defining coefficient. Applying the same reasoning to \(W^*\) proves continuity of the inverse. This is actual topology transport on these concrete algebras, without trace duality, an abstract predual or a normal representation existence theorem.

The extensions of both states to their generated algebras are their unit-vector coefficients:
\[
\widehat\omega_T(a)=\langle\Omega_T,a\Omega_T\rangle,\qquad
\widehat\varphi_{\rm prod}(b)=
\langle\Omega_{\rm prod},b\Omega_{\rm prod}\rangle.
\]
They are positive states and concretely normal, since a unit-vector coefficient is a one-term defining ultraweak coefficient. Equation (VP22) gives
\[
\widehat\varphi_{\rm prod}(\Theta(a))=\widehat\omega_T(a)
\quad(a\in M_T). \tag{VP26}
\]
In particular all local states are transported with their actual eigenvalue weights. Endpoint vector states are not asserted faithful. These arguments prove the precise normal GNS/state identification in original (19):
\[
\boxed{\ (M_T,\widehat\omega_T)\cong
\bigotimes_{j=1}^{\infty}
\left(M_2,\ X\mapsto\operatorname{Tr}
\big(\operatorname{diag}(1-p_j,p_j)X\big)\right),\
p_j\in[0,1].\ } \tag{VP27}
\]
The infinite product means (VP10)–(VP15), (VP23) and its specified vector state, including every endpoint and every variable sequence.

### 15.8. Finite, empty and excluded cases

If the supplied eigenbasis is finite, use its final finite tensor \(H^{(d)}\), the local algebra \(T_d\), and \(\rho_d\) from Sections 15.2–15.4. Finite-stage cyclic surjectivity replaces the dense infinite union, and the same quotient/completed-unitary and bicommutant/state arguments give the finite product identification. If \(K=0\), the CAR algebra and its state are \(\mathbb C\) with the scalar identity state, the Fock, quotient and empty product Hilbert spaces are all \(\mathbb C\), and the maps above are their identity identifications. These cases do not append spurious extra modes to a finite eigenbasis.

For arbitrary orthogonal reducing blocks, Section 15.1 asserts every finite product identity at their actual arbitrary Hilbert-space scope. It neither requires a countable block family nor asserts an uncountable pointed von Neumann product construction. Section 15.2 proves finite density matrices at all eigenvalue endpoints. Sections 15.3–15.7 supply the whole countable variable-eigenvalue product representation, its norms and cyclic completions, and its normal generated-algebra/state transport.

No conclusion here concerns the unique half-state trace, faithfulness of that trace, typeII1, constant-state typeIII, modular operators, core/flow, factor classification or general tensor-commutant identities. Factorality and AFD may have their separate proved supports; neither is an input needed to identify this pointed product. The scope is the finite reducing-block product identity, finite occupation densities, and the completed pointed identification for a supplied finite or countable complete eigenbasis.

### 15.9. State support and the central GNS kernel in the actual product

In the one-mode model (VP10), the support of the represented vector state is \(\lambda_j(s_j)\). For an interior value \(0<p_j<1\), it is the identity. At \(p_j=0\) it is \(\lambda_j(E_{00})\), and at \(p_j=1\) it is \(\lambda_j(E_{11})\). Directly, left multiplication by a positive matrix has zero expectation precisely when it kills every supported occupation vector, so the state is faithful on this support corner. Each represented algebra is the faithful full \(M_2\) by (VP11); its center is scalar by commuting with the explicit matrix units. Thus the central carrier of each nonzero support is one, including both endpoints.

The full arbitrary-product support proof, specialized to these actual pointed legs, gives
\[
s_{M_{\rm prod}}(\widehat\varphi_{\rm prod})
=\operatorname*{s-lim}_{F\subset\mathbb N\ \mathrm{finite}}
\prod_{j\in F}\lambda_j(s_j),
\qquad z_{M_{\rm prod}}(s(\widehat\varphi_{\rm prod}))=1.
\]
The product state is faithful exactly when every \(p_j\) is interior. Its normal GNS representation is faithful in every case, because its central kernel is zero, as proved in the component's Section 8. These assertions distinguish the state from its representation; (VP24)–(VP27) already give the exact normal represented-algebra and state identification without requiring any tensor commutant theorem. The general component therefore supplements that completed product model rather than substituting a faithful-state special case for its endpoints. The finite and empty eigenbasis cases use the finite and empty products specified in Section 15.8.

## 16. The half-state trace and the type-II1 conclusion

This section proves the complete half-state trace and type-II1 conclusion in Section 6, beginning “At \(T=\tfrac12 1\).” Its one-particle space \(K\) is arbitrary: zero, finite-dimensional, infinite-dimensional, or nonseparable. The countable pointed-product conclusion is asserted exactly when \(K\) is separable and infinite-dimensional. The finite and zero-dimensional cases have their separate scalar or matrix-factor conclusions.

The baseline is ZFC, real/complex scalar completeness, elementary finite algebra, and concrete Hilbert/operator definitions. Inner products are conjugate linear in the first variable. The proof uses these complete local constructions. [CAR Sections 9.1–9.4](car-fock-and-quasifree-states.md#9-arbitrary-hilbert-space-fock-foundations) provide arbitrary completed Fock space; [CAR Sections 10.2–10.6](car-fock-and-quasifree-states.md#10-concrete-car-matrix-algebras-completions-and-simplicity) provide the finite matrix units, norms and directed norm completion; [CAR Sections 11.1–11.4](car-fock-and-quasifree-states.md#11-arbitrary-covariance-and-the-completed-cyclic-model) provide the actual state and its whole reduced-Fock cyclic representation; [CAR Section 13](car-fock-and-quasifree-states.md#13-factorality-for-every-positive-contraction) provides factorality; and [CAR Section 14](car-fock-and-quasifree-states.md#14-directed-finite-dimensional-approximation-in-every-car-representation) provides bounded strong\* local approximation. [ITP Sections 10.1–10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) supply the stated concrete Hilbert, operator, tensor, bicommutant and ultraweak boundary. The positive-root and support constructions used below are the actual norm-series/root and strong support proofs of [periodic CAR Sections 8.1–8.3](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative). The minimal-corner argument of [periodic CAR Section 8.7](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative) is made explicit at the point of use.

The complete product construction in [CAR Sections 15.1–15.8](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states) supplies the product identity (17), finite density formula (18) and completed normal GNS/state identification (19), including endpoint-aware cyclic completions and normal state transport. [CAR Section 15.2](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states) supplies the finite density support; [CAR Sections 15.3–15.8](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states) supply the whole pointed product identification at its supplied finite or countable complete-eigenbasis boundary.

### 16.1. The actual half-state and its full finite-subspace restrictions

Write \(A=\operatorname{CAR}(K)\), with the annihilator \(a(f)\) conjugate linear in \(f\). For each finite-dimensional \(E\subset K\), write \(A_E=\operatorname{CAR}(E)\subset A\), using the generator-matching isometric inclusion of [CAR Sections 10.5–10.6](car-fock-and-quasifree-states.md#10-concrete-car-matrix-algebras-completions-and-simplicity). The family is directed by inclusion, because \(E+F\) is finite-dimensional. [CAR Section 10.2](car-fock-and-quasifree-states.md#10-concrete-car-matrix-algebras-completions-and-simplicity) proves
\[
A_{\mathrm{loc}}=\bigcup_{\dim E<\infty}A_E
\quad\text{is a unital *-algebra norm dense in }A. \tag{HT1}
\]
Indeed every polynomial in finitely many fields and their adjoints belongs to the algebra of their finite one-particle span, and those polynomials are dense by the definition of \(A\). No countable cofinal family of subspaces is assumed.

Take \(T=\tfrac12 I_K\). The positive roots in [CAR Section 11.1](car-fock-and-quasifree-states.md#11-arbitrary-covariance-and-the-completed-cyclic-model) are
\[
(I_K-T)^{1/2}=T^{1/2}=2^{-1/2}I_K.
\]
Both are the unique positive roots supplied by [periodic CAR Section 8.2](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative). Their ranges are \(K\), including the zero-space instance. Thus the actual reduced doubled one-particle space and Fock representation are
\[
L=K\oplus\overline K,\qquad
H=\mathcal F_-(L),\qquad
d(f)=2^{-1/2}\bigl(a_L(f\oplus0)+c_L(0\oplus\overline f)\bigr).
\tag{HT2}
\]
The scalar \(2^{-1/2}\) is real, so conjugate linearity creates no coefficient ambiguity. [CAR Section 11](car-fock-and-quasifree-states.md#11-arbitrary-covariance-and-the-completed-cyclic-model) supplies a unital isometric representation \(\pi:A\to B(H)\), with \(\pi(a(f))=d(f)\), its unit vacuum \(\Omega\), and the actual bounded positive norm-one state
\[
\omega(x)=\langle\Omega,\pi(x)\Omega\rangle. \tag{HT3}
\]
The full completed space \(H\) is cyclic for \(\pi(A)\), by [CAR Section 11.3](car-fock-and-quasifree-states.md#11-arbitrary-covariance-and-the-completed-cyclic-model), and [CAR Section 11.4](car-fock-and-quasifree-states.md#11-arbitrary-covariance-and-the-completed-cyclic-model) identifies this whole cyclic model with the completed GNS quotient. In particular no general normal-extension or GNS-existence theorem is an additional premise.

For arbitrary vector lists the actual determinant moments in [CAR Section 11.2](car-fock-and-quasifree-states.md#11-arbitrary-covariance-and-the-completed-cyclic-model) are
\[
\omega\bigl(a(f_1)^*\cdots a(f_r)^*a(g_s)\cdots a(g_1)\bigr)
=
\begin{cases}
2^{-r}\det[\langle g_i,f_j\rangle]_{i,j=1}^r,&r=s,\\
0,&r\ne s.
\end{cases} \tag{HT4}
\]
The empty determinant is one. Normal ordering in that same section proves that these words span the polynomial algebra. Thus their moments refer to a previously constructed positive bounded state on the full CAR algebra.

Fix \(E\) of dimension \(d\), and choose an ordered orthonormal basis \(e_1,\ldots,e_d\). [CAR Section 10.4](car-fock-and-quasifree-states.md#10-concrete-car-matrix-algebras-completions-and-simplicity) gives an onto isometric unital \*-map
\[
\theta_E:A_E\longrightarrow M_{2^d}(\mathbb C)
\]
with the exact Jordan–Wigner occupation coordinates
\[
\theta_E(a(e_j))=
Z^{\otimes(j-1)}\otimes b\otimes I^{\otimes(d-j)},\qquad
b=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
Z=\operatorname{diag}(1,-1). \tag{HT5}
\]
For \(d=0\) this is the empty-mode scalar algebra \(M_1=\mathbb C\). On the bit occupation basis \((\delta_\alpha)_{\alpha\in\{0,1\}^d}\), define
\[
t_E(x)=2^{-d}\sum_{\alpha\in\{0,1\}^d}
\langle\delta_\alpha,\theta_E(x)\delta_\alpha\rangle.
\tag{HT6}
\]
The finite sum proves directly that \(t_E(1)=1\), \(t_E(x^*x)\ge0\), and \(|t_E(x)|\le\|x\|\).

Here is a complete moment check of \(\omega|_{A_E}=t_E\), without treating a finite density formula as an unsupported trace theorem. Expand the vector arguments of a normal word in the finite basis. Repeating an index within either the creator list or the annihilator list makes that word zero by square-zero CAR and anticommutation; its determinant is also zero. For distinct indices in the two lists, unequal lengths or unequal index sets give zero diagonal occupation entries: every nonzero action removes the annihilator indices and inserts the creator indices, and cannot return a bit label to itself unless those two sets agree. Formula (HT4) also gives zero: its unequal-length clause applies in the first case, and in the equal-length/unequal-set case the identity-covariance matrix has a zero row or column.

When both index sets equal \(S=\{i_1<\cdots<i_r\}\), sort each list into that order. The two sorting signs multiply on the word and multiply identically on the determinant. For sorted lists,
\[
a(e_{i_1})^*\cdots a(e_{i_r})^*
a(e_{i_r})\cdots a(e_{i_1})
=\prod_{i\in S}n_i,\qquad n_i=a(e_i)^*a(e_i). \tag{HT7}
\]
Every \(n_i\) commutes with the fields of a different mode: moving either such field past the two factors of \(n_i\) produces two CAR signs and zero contractions. Pair the innermost creator/annihilator and commute its projection past the other modes; induction proves (HT7). Its occupation diagonal equals one exactly on labels containing \(S\). There are \(2^{d-r}\) such labels, so (HT6) gives \(2^{-r}\), exactly the sorted moment in (HT4). Sorting back restores the same two signs on both sides. Finite multilinearity proves equality for every vector normal word, and normal ordering proves equality on all of \(A_E\). Therefore
\[
\boxed{\ \omega|_{A_E}=t_E=2^{-d}\operatorname{Tr}\circ\theta_E
\quad\text{for every finite-dimensional }E\subset K.\ } \tag{HT8}
\]
Here \(\operatorname{Tr}\) means only the finite sum of diagonal entries. Equivalently its density matrix is \(2^{-d}I_{2^d}\), the \(p_j=\tfrac12\) specialization of the complete [CAR Section 15.2](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states) formula (18), proved above explicitly at this specialization. Every finite \(E\) reduces this scalar covariance; no infinite spectral theorem or chosen infinite eigenbasis is involved.

### 16.2. Finite matrix-unit uniqueness and the unique trace on the entire CAR algebra

For finite matrices \(X,Y\) of size \(m=2^d\),
\[
m^{-1}\operatorname{Tr}(XY)
=m^{-1}\sum_{\alpha,\beta}X_{\alpha\beta}Y_{\beta\alpha}
=m^{-1}\sum_{\beta,\alpha}Y_{\beta\alpha}X_{\alpha\beta}
=m^{-1}\operatorname{Tr}(YX). \tag{HT9}
\]
This uses only a finite sum and commutation of scalars. Thus every \(t_E\) is tracial.

Let \(\varphi\) be any tracial state on a full finite matrix algebra \(M_m\), and let \((E_{\alpha\beta})\) be its full matrix units. For \(\alpha\ne\beta\),
\[
\varphi(E_{\alpha\beta})
=\varphi(E_{\alpha\alpha}E_{\alpha\beta})
=\varphi(E_{\alpha\beta}E_{\alpha\alpha})=0.
\]
For any \(\alpha,\beta\),
\[
\varphi(E_{\alpha\alpha})
=\varphi(E_{\alpha\beta}E_{\beta\alpha})
=\varphi(E_{\beta\alpha}E_{\alpha\beta})
=\varphi(E_{\beta\beta}).
\]
Since the \(m\) diagonal units sum to one and \(\varphi(1)=1\), each has value \(1/m\). Their finite linear span is the whole matrix algebra, so \(\varphi=m^{-1}\operatorname{Tr}\). The proof includes \(m=1\). This is finite matrix-unit uniqueness, rather than an assertion of trace uniqueness imported from a structure theorem.

For arbitrary \(x,y\in A\), choose local \(x_n\to x\) and \(y_n\to y\) in norm using (HT1). Each pair fits in one common finite algebra, so (HT8)–(HT9) give \(\omega(x_ny_n)=\omega(y_nx_n)\). Convergent sequences have bounded norms, and
\[
\|x_ny_n-xy\|
\le\|x_n\|\,\|y_n-y\|+\|x_n-x\|\,\|y\|\longrightarrow0.
\]
The reverse products converge by the same estimate. The bound \(|\omega(z)|\le\|z\|\) from (HT3) therefore gives \(\omega(xy)=\omega(yx)\).

If \(\varphi\) is any tracial state on the whole \(A\), its restriction to each \(A_E\) is a tracial state, because all local identities are the identity of \(A\). Finite matrix-unit uniqueness makes it equal to \(t_E=\omega|_{A_E}\). Their equality on the norm-dense union and the boundedness of both states give equality on \(A\). We have proved
\[
\boxed{\ \omega=\omega_{1/2}\text{ is the unique tracial state on }\operatorname{CAR}(K),
\text{ for every }K.\ } \tag{HT10}
\]
The norm-approximation sequences here approximate individual elements of a normed algebra. They assert no countable exhaustion of a nonseparable one-particle space.

### 16.3. The actual concrete normal extension

Let
\[
M=\pi(A)''\subset B(H).
\]
[ITP Section 10.5](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) proves that this bicommutant is precisely the WOT-generated unital selfadjoint algebra on the entire \(H\). [CAR Section 13](car-fock-and-quasifree-states.md#13-factorality-for-every-positive-contraction) proves that \(M\) is a factor for every positive contraction on every \(K\), in this actual completed reduced-Fock representation. In particular
\[
Z(M)=\mathbb C I_H,\qquad H\ne0. \tag{HT11}
\]
This factor input precedes every type argument below; it is not inferred from finite-dimensional approximation.

Define on the entire \(M\)
\[
\tau(x)=\langle\Omega,x\Omega\rangle. \tag{HT12}
\]
It is a positive norm-one state, since \(\|\Omega\|=1\) and
\(\tau(x^*x)=\|x\Omega\|^2\). Its restriction to \(\pi(A)\), transported by the isometric \(\pi\), is exactly \(\omega\). It is concretely normal in the precise topology proved in [ITP Section 10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice): a defining ultraweak functional is
\[
F_{\boldsymbol h,\boldsymbol k}(x)=
\sum_{n\ge1}\langle h_n,xk_n\rangle,\qquad
\sum_n\|h_n\|^2<\infty,\quad\sum_n\|k_n\|^2<\infty,
\]
and (HT12) is the one-term instance \(h_1=k_1=\Omega\), all other terms zero. No trace-class duality, abstract predual, abstract normal representation theorem, or equivalence of topology definitions is invoked.

[CAR Sections 14.3–14.4](car-fock-and-quasifree-states.md#14-directed-finite-dimensional-approximation-in-every-car-representation) apply to this unital representation with \(\pi(1)=I_H\). Their actual directed local algebras are \(D_E=\pi(A_E)\), and for every \(x\in M\) there is a net
\[
x_i\in\bigcup_{\dim E<\infty}D_E,\qquad
\|x_i\|\le\|x\|,\qquad
x_i\longrightarrow x\ \text{strongly*}. \tag{HT13}
\]
For \(x=0\) use the constant zero net; for other radii this is the proved scaling of the local unit-ball density. All elements of each approximating net are local, but need not lie in a common finite-dimensional algebra. The indices are finite-vector tests and errors; no sequential strong\* assertion is made for a nonseparable \(H\).

For completeness the normal extension (HT12) is unique among concretely ultraweak continuous linear functionals extending the original state: the uniformly bounded net in (HT13) converges ultraweakly by [CAR Section 14.6](car-fock-and-quasifree-states.md#14-directed-finite-dimensional-approximation-in-every-car-representation), as verified by a finite head and a square-summable coefficient-tail estimate. Any two such functionals agree on the local approximants and, by that continuity, at their limit \(x\). This proves uniqueness at the actual concrete topology boundary, rather than assuming a general normal-extension theorem.

### 16.4. Traciality on all of \(M\) through bounded local product limits

Fix arbitrary \(x,y\in M\). Choose nets \((x_i)_{i\in I}\) and \((y_j)_{j\in J}\) as in (HT13), with bounds \(\|x\|\) and \(\|y\|\). Use the product directed set \(I\times J\). Each pair of local approximants lies in a common \(D_{E+F}\); (HT8)–(HT9) therefore give
\[
\tau(x_i y_j)=\tau(y_j x_i)\quad\text{for every }(i,j). \tag{HT14}
\]
For every vector \(\xi\in H\),
\[
\|(x_i y_j-xy)\xi\|
\le \|x_i\|\,\|(y_j-y)\xi\|
   +\|(x_i-x)y\xi\|\longrightarrow0. \tag{HT15}
\]
The first term is uniformly bounded in \(i\) by
\(\|x\|\,\|(y_j-y)\xi\|\), and the second tends to zero independently of \(j\). These facts give convergence on the product directed set. Interchanging \(x,y\) gives \(y_jx_i\to yx\) strongly. Applying the same calculation to the adjoint nets gives
\((x_i y_j)^*=y_j^*x_i^*\to y^*x^*\) and
\((y_j x_i)^*=x_i^*y_j^*\to x^*y^*\) strongly. Thus both product nets actually converge strongly\*, with norm bounds \(\|x\|\|y\|\).

In particular Cauchy–Schwarz and (HT15) with \(\xi=\Omega\) give
\(\tau(x_iy_j)\to\tau(xy)\), and likewise for the reverse products. Taking the limit in (HT14) yields
\[
\boxed{\ \tau(xy)=\tau(yx)\quad(x,y\in M).\ } \tag{HT16}
\]
The normality of \(\tau\) was proved independently in Section 16.3. This passage uses explicit vector continuity and product estimates; it does not use an unjustified assertion that a tracial state remains tracial on an arbitrary completion.

### 16.5. The full trace inequality, separation and faithfulness

The displayed inequality in the original paragraph needs a positivity justification because \(x^*x\) and \(yy^*\) may not commute. Here is that justification for arbitrary \(x,y\in M\). The operator
\[
b=\|y\|^2I_H-yy^*
\]
is positive: \(\langle\xi,b\xi\rangle=\|y\|^2\|\xi\|^2-\|y^*\xi\|^2\ge0\), using \(\|y^*\|=\|y\|\) from [ITP Section 10.2](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice). Therefore \(xbx^*\ge0\), by its quadratic form at \(x^*\xi\). Positivity of the vector state gives
\[
\tau(xyy^*x^*)\le\|y\|^2\tau(xx^*)
=\|y\|^2\tau(x^*x). \tag{HT17}
\]
Using the already established whole-algebra trace identity (HT16), first with
\(a=y^*,\,b=x^*xy\), and then with \(a=x^*,\,b=xyy^*\), proves
\[
\begin{aligned}
\|xy\Omega\|^2
&=\tau(y^*x^*xy)\\
&=\tau(x^*xyy^*)\\
&=\tau(xyy^*x^*)\\
&\le\|y\|^2\tau(x^*x).
\end{aligned} \tag{HT18}
\]
This establishes the precise original inequality while placing its positivity comparison between actual positive operators. No positive-product assumption for two noncommuting factors is made.

If \(\tau(x^*x)=0\), (HT18) gives \(xy\Omega=0\) for every \(y\in M\). The orbit \(M\Omega\) is dense in the whole \(H\), since it contains the dense orbit \(\pi(A)\Omega\) furnished by [CAR Section 11.3](car-fock-and-quasifree-states.md#11-arbitrary-covariance-and-the-completed-cyclic-model). Boundedness of \(x\) then gives \(x=0\). Equivalently \(\Omega\) is separating for \(M\), because \(x\Omega=0\) is precisely \(\tau(x^*x)=0\).

This also proves the positive-element definition of faithfulness. If \(a\in M_+\) and \(\tau(a)=0\), [periodic CAR Section 8.2](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative) gives the actual positive root \(c=a^{1/2}\in M\); then \(\tau(c^*c)=\tau(a)=0\), so the result just proved gives \(c=0\) and \(a=0\). Consequently
\[
\boxed{\ \tau\text{ is a faithful normal tracial state on }M,\quad\tau(I_H)=1.\ } \tag{HT19}
\]
Faithfulness is derived after traciality and full cyclicity; neither it nor product-state faithfulness was assumed in Sections 16.1–16.4.

### 16.6. Finiteness and the finite-dimensional endpoints

If \(v\in M\) satisfies \(v^*v=I_H\), then \(vv^*\) is a projection and
\[
\tau(I_H-vv^*)=\tau(I_H)-\tau(vv^*)
=1-\tau(v^*v)=0.
\]
Faithfulness in (HT19) makes \(I_H-vv^*=0\). Hence every isometry in \(M\) is unitary, precisely the finiteness of its identity projection. More generally, if a partial isometry has initial projection \(p\) and final projection \(q\le p\), traciality gives \(\tau(p-q)=0\), so \(p=q\). Thus every projection is finite in the defining Murray–von Neumann sense. Together with (HT11), \(M\) is a finite factor.

If \(\dim K=d<\infty\), the whole \(A\) is \(A_K\cong M_{2^d}\). Its represented image \(D_K\) is the same full matrix algebra with its actual representation multiplicity. [CAR Section 14.4](car-fock-and-quasifree-states.md#14-directed-finite-dimensional-approximation-in-every-car-representation) proves that \(D_K\) is WOT closed by recovering its finitely many matrix entries from vector coefficients and passing to their finite matrix-unit sum; [ITP Section 10.5](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) then gives
\[
M=D_K''=D_K\cong M_{2^d}. \tag{HT20}
\]
Its state is the normalized matrix trace by (HT8), with the faithful normal extension already proved above. The matrix identification and its inverse are concretely normal: the finitely many entries of the image are recovered by vector coefficients, and each image is a finite linear combination of fixed represented matrix units; applying any defining absolutely convergent ultraweak coefficient to this finite sum yields a finite linear combination of entries. These are finite-dimensional topology facts, with no predual theorem.

For \(d=0\), \(A=\mathbb C\), \(L=0\), \(H=\mathbb C\), \(\Omega=1\), \(\pi\) is the scalar identity representation, and \(M=\mathbb C=M_1\), with \(\tau(z)=z\). For positive finite \(d\), (HT20) is a type \(I_{2^d}\) matrix factor. A rank-one projection in the physical \(2^d\)-dimensional matrix space is minimal in this algebra; its represented Hilbert-space range may have multiplicity, so algebraic minimality is not confused with rank one on the Fock representation space. These finite cases have no type-II1 conclusion.

### 16.7. Infinite \(K\): exclude minimal projections directly

We first prove the exact finite-factor alternative needed here, retaining all its hypotheses. Suppose a concrete factor \(N\subset B(G)\), a nonzero unital WOT-closed selfadjoint algebra with scalar center, has a faithful tracial state \(\sigma\), \(\sigma(1)=1\), and a minimal projection \(e\ne0\). We apply this below to \(N=M\), \(\sigma=\tau\). The Hilbert space \(G\) need not be separable.

The scalar-corner statement \(eNe=\mathbb Ce\) is the complete proved statement of [periodic CAR Section 8.7](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative). Its mechanism is explicit: if a selfadjoint \(a\in eNe\) were nonscalar, its unit quadratic values could not all agree, by polarization. Subtract \(te\) for a real \(t\) strictly between two values to obtain \(h\) with positive and negative quadratic values. Using the norm-series positive root \(A=(h^2)^{1/2}\) in the corner, the selfadjoint contraction \(h(A+\varepsilon e)^{-1}\) gives \(A+\varepsilon e\pm h\ge0\); taking the norm limit gives \(A\pm h\ge0\). The two positive nonzero elements
\[
b=(A+h)/2,\qquad c=(A-h)/2
\]
commute, satisfy \(bc=0\), and have nonzero orthogonal supports under \(e\). [Periodic CAR Section 8.3](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative) supplies these supports in the actual corner by the bounded strong limit \(b(b+\varepsilon e)^{-1}\), and similarly for \(c\). Thus \(s(b)\) is a nonzero proper subprojection of \(e\), contrary to minimality. Every selfadjoint corner element is scalar, and real/imaginary decomposition gives \(eNe=\mathbb Ce\). Conversely a scalar corner immediately has no nonzero proper projection.

We give the needed corner-contact argument directly from the supplied bicommutant foundations, so no abstract central-support or comparison theorem is a premise. Let
\[
Q=\overline{\operatorname{span}\{xe\xi:x\in N,\ \xi\in G\}}.
\]
This subspace is invariant under \(N\) and its adjoints. It is also invariant under \(N'\) and its adjoints: an element of \(N'\) commutes with \(x,e\) and maps \(eG\) into itself. [ITP Section 10.1](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) and [ITP Section 10.5](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) therefore put its orthogonal projection \(z\) in both \(N'\) and \((N')'=N\). It is a nonzero central projection since it majorizes \(e\), so the factor condition gives \(z=1\) and \(Q=G\).

For every nonzero projection \(p\in N\), it follows that \(pNe\ne0\): otherwise \(p\) annihilates all \(xeG\), hence their dense span, and would be zero. Choose \(0\ne x\in pNe\). [Periodic CAR Section 8.3](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative) constructs its actual polar partial isometry \(v\in N\), with initial support \(v^*v\le e\) and final support \(vv^*\le p\), both nonzero. Minimality of \(e\) forces \(v^*v=e\). Its final projection \(f=vv^*\le p\) is minimal: a nonzero projection \(g\le f\) pulls back to the nonzero projection \(v^*gv\le e\); it equals \(e\), and conjugating back gives \(g=f\). Therefore every nonzero projection contains a minimal projection equivalent to \(e\). This is the direct consequence in [periodic CAR Section 8.8](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative), with its support membership justified.

Choose, by Zorn's lemma, a maximal family \((e_i)_{i\in I}\) of mutually orthogonal projections equivalent to \(e\), including \(e\). The union of an inclusion-ordered chain of such families has the same properties, because each finite pair appears in one chain member; thus Zorn applies. Traciality and faithfulness give the common value
\[
\sigma(e_i)=\sigma(v_iv_i^*)=\sigma(v_i^*v_i)=\sigma(e)=a>0
\]
whenever \(v_i^*v_i=e\), \(v_iv_i^*=e_i\). For any finite \(F\subset I\),
\[
|F|a=\sigma\left(\sum_{i\in F}e_i\right)\le\sigma(1)=1. \tag{HT21}
\]
The finite orthogonal sum is a projection under one, which justifies the inequality by positivity. Choose an integer \(n>1/a\). There cannot be \(n\) distinct elements of \(I\); if there were, their finite subset would violate (HT21). Thus \(I\) is finite. Its finite sum is one: a nonzero complementary projection would contain another equivalent minimal projection by the preceding corner argument, contradicting maximality.

Enumerate this finite family by \(i=1,\ldots,N_0\), choose its partial isometries \(v_i\), and put \(E_{ij}=v_iv_j^*\). Orthogonal final projections give \(v_i^*v_j=0\) for \(i\ne j\); for \(i=j\) this product is \(e\). Hence
\[
E_{ij}^*=E_{ji},\quad E_{ij}E_{kl}=\delta_{jk}E_{il},
\quad\sum_i E_{ii}=1. \tag{HT22}
\]
All units are nonzero, since \(E_{ij}^*E_{ij}=e_j\ne0\). They are linearly independent: multiplying a finite linear combination by \(E_{ki}\) and \(E_{jl}\), or equivalently by the corresponding diagonal units, isolates each coefficient times a nonzero matrix unit.

For any \(x\in N\), the corner \(v_i^*xv_j\) belongs to \(eNe=\mathbb Ce\); call its coefficient \(x_{ij}\). The finite identity decomposition gives
\[
x=\sum_{i,j}e_i x e_j=\sum_{i,j}x_{ij}E_{ij}. \tag{HT23}
\]
Therefore the full matrix-unit map is onto \(N\), rather than merely an embedding: \(N\cong M_{N_0}(\mathbb C)\), with vector-space dimension \(N_0^2\). This is the first finite-trace conclusion of [periodic CAR Section 8.10](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative), proved here by a finite surjectivity argument once the trace bound makes the maximal family finite. It requires no general type I structure theorem, general type decomposition, separability or abstract normality theorem.

Now assume \(K\) is infinite-dimensional. For every integer \(d\ge1\), it has a \(d\)-dimensional subspace: inductively choose a vector outside the span of the previous finite orthonormal family, subtract its orthogonal projection onto that span, and normalize the nonzero residual. A finite span is closed by its finite coefficient coordinates, so the supplied orthogonal-projection construction applies. [CAR Section 10.4](car-fock-and-quasifree-states.md#10-concrete-car-matrix-algebras-completions-and-simplicity) and [CAR Section 11.1](car-fock-and-quasifree-states.md#11-arbitrary-covariance-and-the-completed-cyclic-model) give inside \(M\) the actual unital local full matrix algebra
\[
D_E=\pi(A_E)\cong M_{2^d}(\mathbb C),
\]
with \(4^d\) linearly independent matrix units. The local map is isometric and injective in this actual representation, independently of trace faithfulness.

If \(M\) had a minimal projection, (HT19), (HT11) and the finite-factor alternative just proved would give \(M\cong M_{N_0}\) for a finite \(N_0\). Choose \(d\) so large that \(4^d>N_0^2\). An injective linear map of the \(4^d\)-dimensional local matrix algebra into the \(N_0^2\)-dimensional \(M\) is impossible. Hence
\[
\boxed{\ K\text{ infinite-dimensional}\quad\Longrightarrow\quad
M_{1/2}\text{ has no minimal projection.}\ } \tag{HT24}
\]
Only arbitrary finite subspaces were selected. This argument covers nonseparable \(K\) without a countable exhaustion. It fills the implication suppressed by the original sentence about unbounded local matrix dimensions.

### 16.8. The type-II1 naming step at its exact definition

Under the standard concrete factor-type definition recorded in [periodic CAR Section 8.10](constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative) and [ITP Section 12](infinite-tensor-products.md#12-the-type-ii1-conclusion-for-arbitrary-trace-products), a finite factor with a faithful normal normalized trace and no minimal projection is a type \(\mathrm{II}_1\) factor. We have proved all four properties: factorality in (HT11), the faithful normal normalized trace in (HT19), finiteness in Section 16.6, and absence of minimal projections in (HT24). Consequently
\[
\boxed{\ M_{1/2}\text{ is a type }\mathrm{II}_1\text{ factor for every infinite-dimensional }K.\ } \tag{HT25}
\]
This uses that definition, not a general type decomposition or modular classification. [ITP Section 12](infinite-tensor-products.md#12-the-type-ii1-conclusion-for-arbitrary-trace-products)'s proof for arbitrary trace products provides an exact comparison of the minimal-projection exclusion; its generic product-factor, trace and expectation inputs from earlier ITP sections are not imported. Here those properties were proved for the actual CAR model in Sections 16.1–16.7.

### 16.9. The whole separable pointed tracial \(M_2\)-product identification

Assume \(K\) is separable and infinite-dimensional. [CAR Section 10.11](car-fock-and-quasifree-states.md#10-concrete-car-matrix-algebras-completions-and-simplicity) constructs an actual complete countable orthonormal basis \(e_1,e_2,\ldots\), by finite Gram–Schmidt from a countable dense set. It cannot terminate in finitely many basis vectors because \(K\) is infinite-dimensional. Every \(e_j\) is an eigenvector of \(T=\tfrac12 I_K\), with \(p_j=\tfrac12\). Thus the complete [CAR Sections 15.1–15.8](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states) bridge applies at its supplied countable complete-eigenbasis boundary.

The exact specialization of its one-mode spaces is
\[
\rho_j=\tfrac12 I_2,\qquad s_j=I_2,\qquad
H_j=M_2,\qquad
\langle U,V\rangle=\sum_{\alpha,\beta=0}^1
\overline{U_{\alpha\beta}}V_{\alpha\beta},\qquad
\Omega_j=2^{-1/2}I_2. \tag{HT26}
\]
Left multiplication \(\lambda_j(X)Y=XY\) is the actual unital faithful isometric representation on this four-dimensional Hilbert space. Its specified vector state is
\[
\langle\Omega_j,\lambda_j(X)\Omega_j\rangle
=\tfrac12\operatorname{Tr}(X).
\]
[CAR Section 15.3](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states) proves these assertions by column norms, the finite adjoint identities and cyclic surjectivity \(M_2\Omega_j=H_j\). This is the whole cyclic matrix space appropriate to \(p_j=\tfrac12\).

Let \(H_{\rm prod}\) be the Hilbert completion of the union of
\(H^{(n)}=\bigotimes_{j=1}^n H_j\), with the isometric embeddings
\(v\mapsto v\otimes\Omega_{n+1}\). Its unit pointed vector is \(\Omega_{\rm prod}\). [CAR Section 15.4](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states) supplies bounded compatible local maps
\[
L_n:M_{2^n}\to B(H_{\rm prod}),\qquad
\|L_n(X)\|=\|X\|,\qquad L_{n+1}(X\otimes I_2)=L_n(X),
\]
and its entire local cyclic union is dense in \(H_{\rm prod}\). Put
\[
C_{\rm prod}=\overline{\bigcup_n L_n(M_{2^n})}^{\,\|\cdot\|},
\qquad M_{\rm prod}=\left(\bigcup_n L_n(M_{2^n})\right)''.
\tag{HT27}
\]
These are the concrete norm algebra and generated von Neumann algebra of the pointed product. No abstract infinite-product existence or commutant theorem is a premise.

[CAR Section 15.1](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states) proves the full finite reducing-block product identity (17), at arbitrary block scope, with every ordering sign; [CAR Section 15.2](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states) proves all finite diagonal densities (18); and [CAR Section 15.5](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states) uses the exact compatible Jordan–Wigner maps from [CAR Section 10.11](car-fock-and-quasifree-states.md#10-concrete-car-matrix-algebras-completions-and-simplicity) to supply an onto isometric \*-isomorphism
\(\Psi:A\to C_{\rm prod}\). At every common finite stage it satisfies the full cyclic inner-product identity, and its completed version is
\[
\langle\Psi(x)\Omega_{\rm prod},\Psi(y)\Omega_{\rm prod}\rangle
=\omega(x^*y)\quad(x,y\in A). \tag{HT28}
\]
Thus this bridge uses (17)–(19) with the whole norm completion, rather than only matching finitely many moments.

In [CAR Section 15.6](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states) the two cyclic maps from the actual GNS quotient are
\[
U_F[x]=\pi(x)\Omega,\qquad U_P[x]=\Psi(x)\Omega_{\rm prod}.
\]
Their common null space is \(\{x:\omega(x^*x)=0\}\). Their complete inner-product identity makes their extensions isometries on the full Hilbert quotient completion. Each has closed range by completeness; the first has dense range in the entire reduced Fock space by [CAR Section 11.3](car-fock-and-quasifree-states.md#11-arbitrary-covariance-and-the-completed-cyclic-model), and the second has dense range in the entire pointed product completion by finite-stage cyclic surjectivity. Hence both are onto, and
\[
W=U_PU_F^*:H\to H_{\rm prod}
\]
is an onto unitary satisfying
\[
W\Omega=\Omega_{\rm prod},\qquad
W\pi(x)W^*=\Psi(x)\quad(x\in A). \tag{HT29}
\]
These full-target assertions are essential to the completed GNS identification in (19).

Conjugating commutation equations twice gives
\[
\Theta:M\longrightarrow M_{\rm prod},\qquad
\Theta(a)=WaW^*, \tag{HT30}
\]
an onto unital \*-isomorphism, with inverse \(b\mapsto W^*bW\), as [CAR Section 15.7](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states) proves. It and its inverse are concretely normal on the exact [ITP Section 10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) topology: for square-summable vector lists in the target,
\[
\sum_n\langle h_n,\Theta(a)k_n\rangle
=\sum_n\langle W^*h_n,aW^*k_n\rangle.
\]
Unitarity preserves both square sums, and [ITP Section 10.6](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice) proves absolute convergence, so this is another defining ultraweak coefficient. Apply the same calculation to the inverse.

The actual product vector state
\(\tau_{\rm prod}(b)=\langle\Omega_{\rm prod},b\Omega_{\rm prod}\rangle\)
satisfies
\[
\tau_{\rm prod}(\Theta(a))=\tau(a)\quad(a\in M). \tag{HT31}
\]
The state already proved faithful normal tracial in Sections 16.4–16.5 is therefore transported to the entire product algebra. Its finite restrictions are the normalized matrix traces \(2^{-n}\operatorname{Tr}\), by the displayed local construction. We conclude the actual pointed normal identification
\[
\boxed{\ (M_{1/2},\tau)\cong
\bigotimes_{j=1}^{\infty}
\bigl(M_2,\tfrac12\operatorname{Tr}\bigr)
\quad(K\text{ separable and infinite-dimensional}),\ } \tag{HT32}
\]
where the right side means exactly (HT26)–(HT27), its completed local actions and its product vector state. Its factor, trace and type conclusions follow from the proved CAR transport and HT25, so no generic ITP Corollary 5.3 hypotheses or unproved trace-product theorem are needed.

For finite \(K\), [CAR Section 15.8](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states) stops at its final finite tensor stage, with no appended modes, and the empty case is the scalar pointed product. For nonseparable \(K\), Sections 16.1–16.8 retain the directed finite-subspace proof; (HT32) asserts no countable eigenbasis or uncountable pointed-product construction.

### 16.10. Exact conclusions and scope

The supplied conclusions are the complete original half-state paragraph: every finite normalized matrix trace; uniqueness of the full tracial CAR state by finite matrix-unit uniqueness and norm density; its actual completed reduced-Fock normal vector-state extension; traciality on the entire generated algebra from bounded strong\* local nets and product limits; the fully justified trace inequality and faithfulness from full cyclicity; finiteness; the absence of minimal projections for every infinite-dimensional \(K\); the exact type-II1 definition step; and the whole separable infinite tracial pointed \(M_2\)-product identification.

All one-particle cardinalities and the zero/finite exceptions are explicit. The finite-factor contradiction uses the factor and faithful trace actually proved here, scalar minimal corners and actual polar-support membership, and finite matrix-unit surjectivity. It imports no general type I structure theorem or type classification. Normality always means the declared concrete countable-amplification topology. There is no spectral theorem, abstract predual/trace duality, normal realization theorem, automatic faithfulness assumption, modular theory, semifiniteness/typeIII, core/flow conclusion or conclusion about other course results.

The complete argument proves the original half-state paragraph at this declared concrete foundation boundary.

## 17. The exact inner times of the faithful constant CAR state

This section proves the complete inner-time formula (21) in Section 6. Its hypotheses are a separable infinite-dimensional complex Hilbert space \(K\) with an ordered countable orthonormal basis, \(0<p<1\), and \(p\ne\tfrac12\). All inner products in this proof are linear in the second variable. An inner automorphism means \(x\mapsto uxu^*\) for a unitary belonging to the algebra in question. No half-state trace argument, general semifiniteness criterion, type III classification, centralizer theorem, continuous core, or abstract trace/predual duality is an input.

The exact inputs are the completed pointed-product bridge in [CAR Sections 15.2–15.8](car-fock-and-quasifree-states.md#15-2-every-finite-diagonal-covariance-density-matrix) (including its complete endpoint-aware construction), and [ITP Sections 10.1–10.6](infinite-tensor-products.md#10-1-inner-product-estimates-and-orthogonal-projection) and [11.1–11.8](infinite-tensor-products.md#11-1-scalar-powers-and-the-local-hilbert-schmidt-model). The latter supply the concrete countable identical faithful \(M_2\) product, its whole Tomita graph and modular powers, and its finite-leg expectations. [CAR Section 8](car-fock-and-quasifree-states.md#8-the-faithful-constant-state-completed-gns-identification) supplies a second complete proof of the same faithful constant specialization.

### 17.1. The elementary scalar period, including the meaning of \(2\pi\)

[ITP Section 11.1](infinite-tensor-products.md#11-1-scalar-powers-and-the-local-hilbert-schmidt-model) constructs the real exponential, its inverse logarithm on \((0,\infty)\), and the complex exponential by its absolutely convergent power series. We supply the precise imaginary-period fact needed to turn a phase equality into equation (21). Write
\[
 e^{ix}=C(x)+iS(x),\quad
 C(x)=\sum_{k\ge0}\frac{(-1)^k x^{2k}}{(2k)!},\quad
 S(x)=\sum_{k\ge0}\frac{(-1)^k x^{2k+1}}{(2k+1)!}.                 \tag{CT1}
\]
The series and their derivative series converge uniformly on every bounded real interval: each tail is dominated by the corresponding tail of \(\sum R^j/j!\), and the derivative tails by that of \(\sum R^j/j!\) after shifting the index. Here is the exact differentiation argument without an integration theorem. If polynomial partial sums \(F_N\) converge uniformly to \(F\), and \(F_N'\) uniformly to \(g\), the mean-value theorem gives
\[
 \left|\frac{F_N(x+h)-F_N(x)}h-F_N'(x)\right|
 \le\sup_{s\ \mathrm{between}\ x,x+h}|F_N'(s)-F_N'(x)|.
\]
Pass to the uniform limits for fixed \(h\ne0\). The right side tends to at most \(\sup_s|g(s)-g(x)|\). A uniform limit of continuous functions is continuous (approximate it uniformly by one continuous partial sum), so this last bound tends to zero with \(h\). Therefore \(F'=g\). Applied to the real series in (CT1), this proves \(C'=-S\), \(S'=C\). The mean-value theorem itself is proved in the next paragraph. The exponential product law, proved by the absolutely convergent double series in [ITP Section 11.1](infinite-tensor-products.md#11-1-scalar-powers-and-the-local-hilbert-schmidt-model), gives \(C^2+S^2=1\).

For clarity, the elementary real-calculus facts used here require no spectral or measure theorem. A continuous function on a compact interval is bounded: otherwise choose points with value magnitudes tending to infinity and extract a convergent subsequence by successive bisection of the bounded interval, contradicting continuity at the limit. Take a sequence approaching its finite supremum and apply the same extraction; continuity gives that supremum at its limit. Apply this to the negative function for the minimum. Rolle's theorem follows because a differentiable function with equal endpoint values either is constant or has an interior extremum with derivative zero. Applying Rolle to a function minus its endpoint secant proves the mean-value theorem. All these steps use only real completeness.

There is a smallest positive zero \(q\) of \(C\), with \(0<q<2\). Indeed \(C(0)=1\) makes \(C\) positive on an initial interval. At \(2\), its first three terms sum to \(-1/3\); the remaining alternating tail starts negative and has strictly decreasing term magnitudes, since each successive magnitude ratio is \(4/((2k+1)(2k+2))<1\). Pairing negative terms with their smaller following positive terms proves \(C(2)<0\). The intermediate-value theorem supplies a zero in \((0,2)\). To justify that theorem from completeness, take the supremum of points on the starting-sign side and use continuity at that supremum; a nonzero value would permit an extension or leave a gap. The infimum of the positive zeros is attained by continuity and bounded away from zero by the initial positive interval. It is \(q\); on \([0,q)\), \(C>0\).

Since \(S'=C>0\) on \([0,q)\), the mean-value theorem gives \(S(x)>0\) for \(0<x\le q\), and \(C(q)=0\), \(C(q)^2+S(q)^2=1\) give \(S(q)=1\). Therefore \(e^{iq}=i\). On the interval \((0,q)\) its real and imaginary coordinates are both strictly positive. The product law rotates these coordinates by \(i^j\) on each interval \((jq,(j+1)q)\), \(j=0,1,2,3\). None of these points is \(1\); at their intervening endpoints the values are \(i,-1,-i\), and at \(4q\) the value is \(1\).

Use the usual analytic scalar normalization \(\pi=2q\): twice the first positive cosine zero, equivalently the imaginary exponential parameter of a half turn. For every real \(x\), the Archimedean property chooses an integer \(k\) with \(k(4q)\le x<(k+1)(4q)\). Subtract that multiple and use the product law and the preceding quadrant calculation. It follows that
\[
 e^{ix}=1\quad\Longleftrightarrow\quad x\in2\pi\mathbb Z.       \tag{CT2}
\]
No circumference or integration theorem is an input to this analytic period assertion. For positive \(a,b\), [ITP Section 11.1](infinite-tensor-products.md#11-1-scalar-powers-and-the-local-hilbert-schmidt-model)'s logarithm and exponential rules now give
\[
 a^{it}=b^{it}
 \quad\Longleftrightarrow\quad
 t\log(b/a)\in2\pi\mathbb Z.                                 \tag{CT3}
\]

### 17.2. The exact pointed algebra and its finite expectations

Put \(a=1-p\), \(b=p\), and \(\rho=\operatorname{diag}(a,b)\). Both entries are positive and \(a+b=1\). Let \(H_0=M_2(\mathbb C)\) with Hilbert–Schmidt inner product, \(\Omega_0=\rho^{1/2}\), and let
\[
 H=\overline{\bigcup_{n\ge1}H_0^{\otimes n}},\qquad
 \xi\longmapsto\xi\otimes\Omega_0
\]
be the specified pointed completion. Write \(\Omega\) for its reference vector, \(A_n=M_2^{\otimes n}\) for the finite left multiplication algebra, and \(M=(\bigcup_n A_n)''\). [ITP Section 11.2](infinite-tensor-products.md#11-2-the-pointed-countable-product-and-its-complete-basis) proves the grouping unitary \(H=H_0^{\otimes n}\otimes H_{>n}\); [ITP Section 11.3](infinite-tensor-products.md#11-3-the-concrete-algebra-and-faithful-product-vector) proves the vector is cyclic and separating by the dense commuting right orbit. Consequently \(\varphi(x)=\langle\Omega,x\Omega\rangle\) is faithful and concretely normal, without any trace assumption.

Let \(H_n=H_0^{\otimes n}\), \(V_n:H_n\to H\) insert the reference tail, and \(P_n=V_nV_n^*\). [ITP Section 11.6](infinite-tensor-products.md#11-6-finite-leg-expectations-with-bounded-strong-approximation) proves
\[
 E_n(x)=(V_n^*xV_n)\otimes1_{H_{>n}},\quad
 E_n(M)=A_n,\quad \|E_n(x)\|\le\|x\|,\quad
 E_n(cxd)=cE_n(x)d\ (c,d\in A_n),                            \tag{CT4}
\]
as well as \(E_n(x)\Omega=P_nx\Omega\) and \(P_n\to1\) strongly. Its proof constructs the compression on every bounded operator, checks its whole finite matrix expansion, and proves strong\* convergence; it is not an appeal to abstract expectations or a preadjoint.

We shall need the tower identity, which we now prove. For \(m\ge n\), let \(V_n^m:H_n\to H_m\) append \(\Omega_0^{\otimes(m-n)}\). Then \(V_mV_n^m=V_n\). Compressing \(E_m(x)\), whose tail beyond \(m\) is the identity, gives
\[
 V_n^*E_m(x)V_n
 =(V_n^m)^*(V_m^*xV_m)V_n^m=V_n^*xV_n.
\]
Amplifying on the tail beyond \(n\) proves, on all \(B(H)\),
\[
 E_nE_m=E_n.                                                \tag{CT5}
\]
For \(x_j\in M_2\), finite tensor inner products also give
\[
 E_n(x_1\otimes\cdots\otimes x_m)
 =(x_1\otimes\cdots\otimes x_n)
       \prod_{j=n+1}^m\operatorname{Tr}(\rho x_j).             \tag{CT6}
\]
Every factor on the right is the one-leg reference-vector coefficient. This finite formula includes nonselfadjoint matrices.

### 17.3. The modular automorphisms and their sign

[ITP Sections 11.4–11.8](infinite-tensor-products.md#11-4-positive-diagonal-operators-exact-adjoints-and-graph-cores) identify the closure of the initial Tomita involution \(x\Omega\mapsto x^*\Omega\) on its entire graph domain. Its positive operator \(\Delta=S^*S\) has the completed diagonal basis and exact spectral domain supplied there. Its imaginary powers are the strongly continuous diagonal unitaries \(U_t=\Delta^{it}\). They preserve \(M\), and
\[
 \sigma_t(x)=U_txU_t^*,\qquad
 \sigma_t|_{A_n}=\operatorname{Ad}v_n,\qquad
 v_n=(\rho^{it})^{\otimes n}.                               \tag{CT7}
\]
The equality on the finite legs is exactly \(\rho_n^{it}x\rho_n^{-it}\), rather than conjugation by its inverse. In particular
\[
 \sigma_t(E_{12}^{(j)})=(a/b)^{it}E_{12}^{(j)}.              \tag{CT8}
\]
On \(E_{21}^{(j)}\) the phase is its inverse.

The parity-corrected CAR mode \(b_j=Z_1\cdots Z_{j-1}a(e_j)\), with \(Z_i=1-2a(e_i)^*a(e_i)\), is \(E_{12}^{(j)}\) in the exact CAR bridge. Each \(Z_i\) is diagonal and fixed by (CT7). Hence both \(b_j\) and the original annihilator \(a(e_j)\) have phase \((a/b)^{it}=((1-p)/p)^{it}\). This is consistent with (21), whose written generator uses the reciprocal ratio \(b/a\): replacing a nonzero generator by its negative leaves its integer-multiple subgroup unchanged.

### 17.4. Every inner time forces equality of the two phases

Fix \(t\in\mathbb R\), and abbreviate
\[
 v=\rho^{it}=\operatorname{diag}(a^{it},b^{it}),\qquad
 c=\operatorname{Tr}(\rho v)=a\,a^{it}+b\,b^{it}.             \tag{CT9}
\]
Both entries of \(v\) have modulus one, so \(v\) and \(v_n=v^{\otimes n}\) are unitaries, and \(|c|\le a+b=1\) by the scalar triangle inequality.

Suppose \(\sigma_t=\operatorname{Ad}u\) for a unitary \(u\in M\). For \(x\in A_n\), this says \(ux=\sigma_t(x)u=v_nxv_n^*u\). Bimodularity of (CT4) gives
\[
 E_n(u)x=v_nxv_n^*E_n(u).
\]
Thus \(v_n^*E_n(u)\in A_n\) commutes with every element of \(A_n\). The center of the full finite matrix algebra is scalar: commuting with all diagonal matrix units annihilates all off-diagonal entries, and commuting with \(E_{\alpha\beta}\) equates all diagonal entries. There exists a scalar \(\lambda_n\) such that
\[
 E_n(u)=\lambda_n v_n,\qquad |\lambda_n|\le1.                \tag{CT10}
\]
The bound follows from \(\|E_n(u)\|\le1\) and \(\|v_n\|=1\).

For \(m\ge n\), (CT5), (CT6) and (CT9) imply
\[
 \lambda_n v_n=E_nE_m(u)=\lambda_m E_n(v_m)
 =\lambda_m c^{m-n}v_n,\qquad
 \lambda_n=\lambda_m c^{m-n}.                              \tag{CT11}
\]
If \(|c|<1\), holding \(n\) fixed and letting \(m\to\infty\) gives \(\lambda_n=0\). This uses only \(|\lambda_m|\le1\) and geometric decay; no limit of implementing unitaries or infinite product is asserted. Equation (CT10) would give \(E_n(u)\Omega=0\) for every \(n\). But (CT4) makes these vectors \(P_nu\Omega\to u\Omega\), so \(u\Omega=0\), contrary to \(\|u\Omega\|=\|\Omega\|=1\). Therefore
\[
 \sigma_t\ \hbox{inner}\quad\Longrightarrow\quad |c|=1.       \tag{CT12}
\]

For unit complex numbers \(z,w\), a direct multiplication proves
\[
 |az+bw|^2
 =a^2+b^2+2ab\operatorname{Re}(z\overline w)
 =1-ab|z-w|^2.                                             \tag{CT13}
\]
Since \(ab>0\), (CT9), (CT12), and (CT13) force \(a^{it}=b^{it}\).

### 17.5. Coincident phases give the identity on the entire completion

Conversely, if \(a^{it}=b^{it}\), the finite \(v_n\) is scalar, so (CT7) fixes every \(A_n\). The whole diagonal construction in [ITP Section 11](infinite-tensor-products.md#11-modular-action-of-the-faithful-identical-two-level-product) gives an even more explicit conclusion: each finite matrix-unit tensor has \(\Delta^{it}\)-eigenvalue equal to a product of the ratios \(a^{it}/a^{it}\), \(a^{it}/b^{it}\), \(b^{it}/a^{it}\), \(b^{it}/b^{it}\), all equal to one. These finite tensor vectors span the dense pointed Hilbert space. Hence the bounded unitary \(U_t\) is the identity on \(H\). In particular \(\sigma_t\) is the identity on every \(x\in M\), and is implemented by \(1\in M\).

Alternatively, the local identity passes to the whole weak-operator closure because conjugation by a fixed bounded unitary is weak-operator continuous; [ITP Section 10.5](infinite-tensor-products.md#10-5-the-unital-bicommutant-theorem-by-finite-vector-amplification) identifies the bicommutant with that closure. Neither argument presumes that arbitrary weak-operator nets are bounded. We have proved both directions, and also equality with the literal identity-time group:
\[
 \{t:\sigma_t\hbox{ inner}\}
 =\{t:\sigma_t=\operatorname{id}\}
 =\{t:a^{it}=b^{it}\}.                                     \tag{CT14}
\]

### 17.6. Transport the whole modular graph to the actual CAR representation

The [completed bridge in CAR Section 15](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states) gives an onto pointed unitary
\[
 W:H_{\mathrm{CAR},p}\longrightarrow H,\qquad
 W\Omega_p=\Omega,\qquad WM_pW^*=M,                         \tag{CT15}
\]
where \(H_{\mathrm{CAR},p}\) is the actual completed reduced doubled-Fock cyclic representation, and \(M_p\) its generated von Neumann algebra. At \(0<p<1\) the reduced doubled one-particle legs are the whole two legs. The equality is a concrete normal isomorphism on every element, with inverse, not just finite moments or an algebraic dense subspace. [CAR Sections 8.6–8.9](car-fock-and-quasifree-states.md#8-6-the-faithful-constant-p-doubled-fields-and-their-determinant-moments) provides a second direct faithful-constant proof with the same endpoint restrictions.

Faithfulness transports: if \(x\in(M_p)_+\) has \(\langle\Omega_p,x\Omega_p\rangle=0\), then \(\varphi(WxW^*)=0\) and product faithfulness forces \(WxW^*=0\), hence \(x=0\). Cyclicity and separation transport by the onto unitary as well. Thus the initial CAR Tomita operator is defined unambiguously on \(M_p\Omega_p\).

For every \(x\in M_p\), including nonlocal \(x\), (CT15) gives
\[
 W(x\Omega_p)=(WxW^*)\Omega,\qquad
 W(x^*\Omega_p)=(Wx^*W^*)\Omega.                            \tag{CT16}
\]
Consequently \(WS_{p,0}W^*=S_0\) on their entire initial domains. Unitary conjugation maps graph closures onto graph closures: both are closures of the same transported set of ordered vector pairs under the isometry \(W\oplus W\). Since [ITP Section 11](infinite-tensor-products.md#11-modular-action-of-the-faithful-identical-two-level-product) proves that \(S_0\) is closable with closure \(S\), \(S_{p,0}\) is closable and its closure satisfies \(WS_pW^*=S\). The adjoint identity follows from its defining inner-product relation tested against every vector in the domain; the onto unitary preserves that relation and its bounded representability. Therefore
\[
 W(S_p^*S_p)W^*=\Delta
\]
with equality of full domains. Transporting the diagonal basis of [ITP Section 11](infinite-tensor-products.md#11-modular-action-of-the-faithful-identical-two-level-product) and its square-summability domain identifies the powers of this positive operator explicitly: each coefficient is multiplied by the same \(\mu^{it}\) as in the product basis. Thus
\[
 W\Delta_p^{it}W^*=U_t,\qquad
 W\sigma_t^{\omega_p}(x)W^*=\sigma_t(WxW^*)\quad(x\in M_p).  \tag{CT17}
\]
This proves the whole completed modular transport, rather than assuming a general modular-invariance theorem for normal isomorphisms. The conjugating maps are concretely normal by [CAR Section 15](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states)'s square-summable coefficient calculation. An implementing unitary in either algebra transports to an implementing unitary in the other, so their inner-time groups are identical.

### 17.7. Equation (21), its signed generator, and the exact conclusion

Since \(p\ne\tfrac12\), the real number \(\ell=\log(p/(1-p))=\log(b/a)\) is nonzero. Equations (CT3), (CT14) and (CT17) yield
\[
 \boxed{\{t:\sigma_t^{\omega_p}\text{ is inner}\}
 =\{t:\sigma_t^{\omega_p}=\operatorname{id}\}
 =\frac{2\pi}{\log(p/(1-p))}\mathbb Z.}                    \tag{CT18}
\]
The least positive period is \(2\pi/|\ell|\). For \(p<1/2\), the generator displayed in the original equation is negative; its integer multiples are still the same subgroup. At \(t=\pi/\ell\), the phase ratio \((b/a)^{it}=-1\), so (CT13) gives a strict overlap defect and the action is outer. More precisely
\[
 |c|=|a-b|=|1-2p|<1,\qquad
 1-|c|=1-|1-2p|>0.                                        \tag{CT19}
\]
Every summand of the original identical-component overlap criterion is this positive constant at that time, so its scalar series diverges. This proves the scalar computation used in (20); it does not silently supply the criterion's trace/modular prerequisites.

The proof of (21) is complete relative to the explicitly selected concrete CAR/ITP foundations and the elementary scalar argument in Section 17.1. It also proves a particular outer modular time and the exact annihilator sign. It does not assert (20), the absence of finite projections, type III, a type III subtype, factoriality of the fixed algebra, or any center-flow calculation. Those conclusions require their separate trace, projection, modular and core arguments.

## 18. Order-normal positive functionals and the concrete ultraweak topology

This section reconstructs the normal-continuity theorem needed for the finite-corner argument below. It proves the following theorem for an arbitrary complex Hilbert space, with no separability or faithful-state assumption.

**Theorem NC.** Let \(A\subseteq B(H)\) be a unital weak-operator-closed selfadjoint algebra. Let \(\mu:A\to\mathbb C\) be a bounded positive linear functional. Suppose that, for every bounded increasing net \((a_i)\) in \(A_+\), with supremum \(a\in A_+\),
\[
\mu(a)=\sup_i\mu(a_i).
\tag{NC.1}
\]
Then there exist sequences \((u_j)\), \((v_j)\) in the *given concrete space* \(H\) such that
\[
\sum_j\|u_j\|^2<\infty,\qquad \sum_j\|v_j\|^2<\infty,\qquad
\mu(x)=\sum_j\langle u_j,xv_j\rangle\quad(x\in A).
\tag{NC.2}
\]
Consequently \(\mu\) is continuous for the relative concrete ultraweak topology on \(A\). Conversely, an ultraweakly continuous positive functional satisfies (NC.1).

**Theorem NC-P (complete projection additivity suffices).** Under the same concrete-algebra and bounded-positive-functional hypotheses, suppose only that for every set-indexed family \((p_\alpha)_{\alpha\in I}\) of mutually orthogonal projections in \(A\),
\[
\mu\!\left(\sum_{\alpha\in I}p_\alpha\right)
=\sup_{F\subseteq I,\ F\ {\rm finite}}\sum_{\alpha\in F}\mu(p_\alpha).
\]
Then the whole coefficient representation (NC.2) holds. In particular \(\mu\) is globally concrete ultraweakly continuous and, by [Section 18.8](car-fock-and-quasifree-states.md#18-8-order-normality-complete-additivity-and-the-reverse-implication), order normal. [Section 18.1](car-fock-and-quasifree-states.md#18-1-positive-forms-and-the-topology-that-must-be-proved)–[Section 18.7](car-fock-and-quasifree-states.md#18-7-a-countable-square-summable-assembly-for-the-whole-functional) prove this theorem directly from complete projection additivity. They do not assume (NC.1). [Section 18.8](car-fock-and-quasifree-states.md#18-8-order-normality-complete-additivity-and-the-reverse-implication) separately derives their complete-additivity hypothesis from (NC.1) to prove the originally stated order-normal version.

All orthogonal families below are set-indexed; their sums mean nets of finite partial sums. The inner product is conjugate linear in its first variable. If \(H=0\), then \(A=0\) and both theorems hold with zero sequences; subsequently assume \(H\ne0\).

The explicitly selected supplied inputs are the whole arguments in [ITP Sections 10.1–10.6](infinite-tensor-products.md#10-1-inner-product-estimates-and-orthogonal-projection), and the elementary norm/order, norm-series square-root, support, and projection-join arguments in [periodic CAR Sections 8.1–8.4](constant-car-states-and-the-periodic-core.md#8-1-the-elementary-operator-facts-used-below). In particular, the square root used below is the positive root constructed by a norm-convergent scalar coefficient series; its membership and commutation properties have full supplied proofs. No continuous or Borel spectral theorem, trace-class duality, abstract predual, bidual representation, normal–singular decomposition, normal representation theorem, or Krein–Smulian theorem is an input.

### 18.1. Positive forms and the topology that must be proved

For a positive linear functional \(\theta\), a selfadjoint \(x\) has \(\|x\|1\pm x\ge0\); hence \(\theta(x)\) is real. Decomposing an arbitrary element into its real and imaginary selfadjoint parts gives \(\theta(x^*)=\overline{\theta(x)}\). The form
\[
(x,y)\longmapsto\theta(x^*y)
\]
is therefore a positive sesquilinear form. Expanding its value at \(x+ty\), for scalar \(t\), proves
\[
|\theta(x^*y)|^2\le\theta(x^*x)\theta(y^*y).
\tag{NC.3}
\]
For example, when \(\theta(y^*y)>0\), minimize this nonnegative quadratic expression in \(t\); when it is zero, letting \(t\) vary forces the cross term to vanish.

The concrete inequality \(x^*x\le\|x\|^2 1\) and positivity give
\[
|\theta(x)|^2\le\theta(1)\theta(x^*x)
 \le\theta(1)^2\|x\|^2.
\tag{NC.4}
\]
Thus \(\|\theta\|=\theta(1)\); in particular \(\theta(1)=0\) implies \(\theta=0\). Write \(m=\mu(1)\). The case \(m=0\) is now finished.

The concrete ultraweak topology is exactly the topology generated by
\[
x\longmapsto F_{\boldsymbol u,\boldsymbol v}(x)
 =\sum_j\langle u_j,xv_j\rangle,
\quad
\sum_j\|u_j\|^2<\infty,\quad \sum_j\|v_j\|^2<\infty.
\tag{NC.5}
\]
[ITP Section 10.6](infinite-tensor-products.md#10-6-the-concrete-ultraweak-boundary-without-trace-or-spectral-theory) supplies the complete Hilbert direct-sum construction and the absolute convergence estimate for these coefficients. To establish global ultraweak continuity it is enough to construct one representation (NC.2). Continuity only on the unit ball will not be substituted for this conclusion.

### 18.2. Finite positive projection approximation without a spectral theorem

We first prove that every \(a\in A_+\) is a norm limit of finite nonnegative linear combinations of mutually orthogonal projections in \(A\).

For \(h=h^*\in A\), let \(d=(h^2)^{1/2}\in A\). The supplied norm-series construction makes \(d\) commute with \(h\). For \(\varepsilon>0\), the operator
\[
h(d+\varepsilon1)^{-1}
\]
is selfadjoint and contractive. Indeed, its squared norm on a vector equals that of \(d(d+\varepsilon1)^{-1}\) on the same vector, using \(h^2=d^2\); the latter operator is a positive contraction by the supplied positive-inverse construction. Therefore \(1\pm h(d+\varepsilon1)^{-1}\ge0\). Conjugating by \((d+\varepsilon1)^{1/2}\), with all the commutations supplied by the series construction, gives
\[
d+\varepsilon1\pm h\ge0.
\]
Norm closure of positivity yields \(d\pm h\ge0\). Consequently
\[
h_+=(d+h)/2,\qquad h_-=(d-h)/2
\tag{NC.6}
\]
are positive, commute, satisfy \(h=h_+-h_-\), and have \(h_+h_-=0\).

For \(t\ge0\) set
\[
e_t=s((a-t1)_+)\in A.
\]
Here the supplied support construction is the strong limit
\[
s(b)=\mathop{\mathrm{s\!-\!lim}}_{\varepsilon\downarrow0}
 b(b+\varepsilon1)^{-1},
\qquad b\in A_+,
\tag{NC.7}
\]
and is the projection onto \(\overline{bH}\). Its complete proof uses the kernel/range orthogonal decomposition and the estimate on \(bH\), rather than a spectral projection theorem.

The operators \((a-t1)_+\), their support regularizations, and their supports commute with \(a\) and with each other: the roots are norm limits of polynomials in \((a-t1)^2\), and multiplication by a fixed bounded operator preserves strong convergence. In (NC.6), the negative part kills the range of the positive part, and hence its closure. It follows that
\[
ae_t\ge t e_t,\qquad a(1-e_t)\le t(1-e_t).
\tag{NC.8}
\]
These are inequalities on reducing subspaces, equivalently compressed operator inequalities.

If \(s>t\), the commuting projection \(q=e_s(1-e_t)\) reduces \(a\). On \(qH\), (NC.8) gives simultaneously \(aq\ge sq\) and \(aq\le tq\). A nonzero vector in \(qH\) would contradict \(s>t\); therefore \(q=0\) and \(e_s\le e_t\).

Choose \(R>0\) with \(R\ge\|a\|\), let \(\delta=R/N\), and put \(e_k=e_{k\delta}\) for \(0\le k\le N\). We have \(e_N=0\): since \(a-R1\le0\), the positive root of \((a-R1)^2\) is \(R1-a\), by uniqueness of the supplied positive root, so its positive part is zero. The projections
\[
1-e_0,\qquad p_k=e_k-e_{k+1}\quad(0\le k<N)
\]
are mutually orthogonal and sum to \(1\). The first is in the kernel of \(a\). On \(p_kH\), (NC.8) gives
\[
k\delta\,p_k\le ap_k\le(k+1)\delta\,p_k.
\]
Thus for \(a_N=\sum_{k=0}^{N-1}k\delta\,p_k\),
\[
0\le a-a_N\le\delta1,\qquad \|a-a_N\|\le\delta\longrightarrow0.
\tag{NC.9}
\]
The case \(a=0\) is also covered, or can be taken separately.

The same construction applies in a corner \(eAe\), acting on \(eH\) with identity \(e\). Consequently an inequality between two bounded positive functionals on that corner can be checked on all its projections: apply it to each \(a_N\) and pass to the norm limit. Neither traciality nor complete additivity is needed for this particular observation.

### 18.3. A nonzero corner dominated by a vector functional

Let \(\theta\) be any bounded positive functional on a nonzero concrete von Neumann algebra \(B\subseteq B(L)\), with \(L\ne0\). Choose \(v\in L\) such that \(\|v\|^2=\theta(1_B)\), and put \(\omega_v(x)=\langle v,xv\rangle\). Such a vector exists by scaling a unit vector; if \(\theta(1_B)=0\), use \(v=0\). We prove that some nonzero projection \(e\in B\) satisfies
\[
\theta(y)\le\omega_v(y)\qquad(y\in(eBe)_+).
\tag{NC.10}
\]

Consider families of mutually orthogonal nonzero projections \(p\in B\) satisfying the strict inequality \(\omega_v(p)<\theta(p)\). A chain of such families has their union as an upper bound. Zorn's lemma supplies a maximal family \(\mathcal P\). If it is empty, no projection satisfies that strict inequality, and [Section 18.2](car-fock-and-quasifree-states.md#18-2-finite-positive-projection-approximation-without-a-spectral-theorem) gives (NC.10) with \(e=1_B\).

Suppose it is nonempty and fix \(p_0\in\mathcal P\). Put
\[
d_0=\theta(p_0)-\omega_v(p_0)>0,\qquad
f=\sum_{p\in\mathcal P}p\in B.
\]
The projection sum exists by the supplied arbitrary-join construction. For every finite \(F\subseteq\mathcal P\) containing \(p_0\),
\[
\sum_{p\in F}\omega_v(p)
\le\sum_{p\in F}\theta(p)-d_0
=\theta\!\left(\sum_{p\in F}p\right)-d_0
\le\theta(1_B)-d_0.
\tag{NC.11}
\]
Finite orthogonal sums converge strongly to \(f\). Applying their coefficients to \(v\) gives \(\omega_v(f)\le\theta(1_B)-d_0\). Since \(\omega_v(1_B)=\theta(1_B)\), we have \(f\ne1_B\). This strict-gap argument does not assume any additivity of \(\theta\) on an infinite family.

Let \(e=1_B-f\ne0\). Every nonzero projection \(q\le e\) is orthogonal to the maximal family, so maximality implies \(\theta(q)\le\omega_v(q)\). The inequality also holds at \(q=0\), and [Section 18.2](car-fock-and-quasifree-states.md#18-2-finite-positive-projection-approximation-without-a-spectral-theorem) now proves (NC.10).

### 18.4. A maximal orthogonal collection of dominated corners

For the direct proof of NC-P, assume complete projection additivity as in its statement. Apply [Section 18.3](car-fock-and-quasifree-states.md#18-3-a-nonzero-corner-dominated-by-a-vector-functional) successively through Zorn's lemma, using the following precise partially ordered set. Its elements are sets of pairs \((e_\alpha,v_\alpha)\), with \(e_\alpha\in A\) nonzero mutually orthogonal projections, \(v_\alpha\in H\), and
\[
\mu(y)\le\langle v_\alpha,yv_\alpha\rangle
\quad (y\in(e_\alpha A e_\alpha)_+).
\tag{NC.12}
\]
Order these sets by inclusion. Chain unions remain such sets, so a maximal collection exists.

Its projection sum is \(1\). Otherwise \(r=1-\sum_\alpha e_\alpha\ne0\), and \(rAr\), acting on \(rH\), is a nonzero concrete von Neumann algebra. To see closedness in this representation directly, extend each operator in \(B(rH)\) by zero on \((1-r)H\); weak operator convergence on \(rH\) then gives weak operator convergence on \(H\). The defining identities \(rxr=x\) and weak closedness of \(A\) put the limit in \(rAr\). [Section 18.3](car-fock-and-quasifree-states.md#18-3-a-nonzero-corner-dominated-by-a-vector-functional) on this corner supplies another nonzero projection and vector in \(rH\), contradicting maximality.

Write \(w_\alpha=e_\alpha v_\alpha\). The right side of (NC.12) is unchanged on the corner by this replacement. Complete additivity gives
\[
m=\mu(1)=\sup_{F\text{ finite}}\sum_{\alpha\in F}\mu(e_\alpha).
\tag{NC.13}
\]
For each integer \(n\ge1\), choose a finite set \(G_n\) such that, after replacing it by \(F_n=G_1\cup\cdots\cup G_n\),
\[
f_n=\sum_{\alpha\in F_n}e_\alpha,\qquad
f_n\le f_{n+1},\qquad
\mu(1-f_n)\le m\,2^{-4n}.
\tag{NC.14}
\]
For \(m>0\) these sets can be chosen nonempty: (NC.13) permits approximation with any positive error. There is no claim that \(f_n\to1\) strongly on the original \(H\). The conclusion needed here is the scalar bound (NC.14), which remains valid for a nonseparable \(H\) and an uncountable original collection.

### 18.5. Full concrete vector realization under vector domination

We prove the elementary domination lemma needed to turn a finite compression into actual concrete coefficients.

Let \(K\) be a Hilbert space, let \(D:A\to B(K)\) be a unital selfadjoint algebra representation, let \(\Xi\in K\), and let \(\theta\) be a positive functional such that
\[
0\le\theta(x)\le\langle\Xi,D(x)\Xi\rangle\quad(x\in A_+).
\tag{NC.15}
\]
There exists \(\eta\in K\) such that
\[
\theta(x)=\langle\eta,D(x)\eta\rangle\quad(x\in A),
\qquad \|\eta\|^2=\theta(1).
\tag{NC.16}
\]
No normality property of \(D\) is assumed.

Let \(L=\overline{\{D(x)\Xi:x\in A\}}\subseteq K\). On this dense orbit define
\[
\beta(D(x)\Xi,D(y)\Xi)=\theta(x^*y).
\]
It is well defined. If \(D(x)\Xi=0\), (NC.15) gives \(\theta(x^*x)=0\), and (NC.3) makes all cross terms containing \(x\) zero; the same argument applies in the second variable. Moreover
\[
|\beta(D(x)\Xi,D(y)\Xi)|
\le\sqrt{\theta(x^*x)\theta(y^*y)}
\le\|D(x)\Xi\|\|D(y)\Xi\|.
\tag{NC.17}
\]
It extends uniquely to a bounded positive sesquilinear form on \(L\). Hilbert Riesz representation, supplied in [ITP Section 10.2](infinite-tensor-products.md#10-2-riesz-representation-adjoints-and-the-operator-c-identity), gives a bounded operator \(T\in B(L)\) with
\[
\beta(h,k)=\langle h,Tk\rangle,\qquad 0\le T\le1_L.
\]
For precision, Riesz is applied to the bounded conjugate-linear functional in the first variable for each fixed second variable; uniqueness makes \(T\) linear, and (NC.17) gives \(\|T\|\le1\). Conjugate symmetry makes \(T=T^*\), and its diagonal values establish the stated operator inequalities.

The subspace \(L\) is preserved by every \(D(a)\) and \(D(a)^*=D(a^*)\). For orbit vectors,
\[
\begin{aligned}
\langle D(x)\Xi,T D(a)D(y)\Xi\rangle
 &=\theta(x^*ay)\\
 &=\langle D(a^*)D(x)\Xi,T D(y)\Xi\rangle\\
 &=\langle D(x)\Xi,D(a)T D(y)\Xi\rangle.
\end{aligned}
\]
Density shows that \(T\) commutes with \(D(a)|_L\). The norm-series positive root \(T^{1/2}\in B(L)\) consequently does too. Since \(D(1)\Xi=\Xi\), set \(\eta=T^{1/2}\Xi\in L\subseteq K\). Then
\[
\theta(x)=\langle\Xi,T D(x)\Xi\rangle
 =\langle T^{1/2}\Xi,D(x)T^{1/2}\Xi\rangle.
\]
Evaluation at \(1\) proves the norm identity in (NC.16). This proves the entire lemma; it has not invoked a Radon–Nikodym theorem or automatic normality of a dominated functional.

### 18.6. Finite compressions and their exact coefficient norms

For a finite nonempty \(F\) from [Section 18.4](car-fock-and-quasifree-states.md#18-4-a-maximal-orthogonal-collection-of-dominated-corners), set
\[
f=\sum_{\alpha\in F}e_\alpha,\qquad
\mu_f(x)=\mu(fxf),\qquad k=|F|.
\]
This is a bounded positive functional. For \(x\ge0\), write \(r=x^{1/2}\in A\). In the positive form of [Section 18.1](car-fock-and-quasifree-states.md#18-1-positive-forms-and-the-topology-that-must-be-proved) the inequality
\[
\mu\!\left(\left(\sum_{\alpha\in F}re_\alpha\right)^*
                    \left(\sum_{\alpha\in F}re_\alpha\right)\right)
\le k\sum_{\alpha\in F}\mu(e_\alpha x e_\alpha)
\tag{NC.18}
\]
follows by summing Cauchy–Schwarz on its cross terms and applying scalar Cauchy–Schwarz to the finite sum of their square roots. Equivalently this is the elementary squared triangle estimate in a positive semidefinite form; it is valid even when that form is degenerate. Thus (NC.12) gives
\[
\mu_f(x)\le k\sum_{\alpha\in F}\langle w_\alpha,xw_\alpha\rangle.
\tag{NC.19}
\]

Take \(K_F=H^{\oplus k}\), with \(D_F(x)\) the diagonal action, and \(\Xi_F=\sqrt{k}\,(w_\alpha)_{\alpha\in F}\). This is a Hilbert space by finite completeness, and \(D_F\) is a bounded unital selfadjoint representation by coordinate calculation. [Section 18.5](car-fock-and-quasifree-states.md#18-5-full-concrete-vector-realization-under-vector-domination) applies to (NC.19). It supplies a vector \(\eta_F\in K_F\) such that
\[
\mu_f(x)=\langle\eta_F,D_F(x)\eta_F\rangle,\qquad
\|\eta_F\|^2=\mu(f)\le m.
\tag{NC.20}
\]
Writing its finitely many components in \(H\) gives actual finite concrete vector coefficients. The norm bound in (NC.20) has no factor depending on \(k\); this is essential for the infinite assembly.

For \(q=1-f\) and \(\|x\|\le1\), the identity \(x-fxf=qx+fxq\), followed by (NC.3), gives
\[
\begin{aligned}
|\mu(x)-\mu_f(x)|
&\le\sqrt{\mu(q)\mu(x^*x)}
    +\sqrt{\mu(fxx^*f)\mu(q)}\\
&\le2\sqrt{m\,\mu(q)}.
\end{aligned}
\tag{NC.21}
\]
Here \(fxx^*f\le f\), so its value is at most \(m\). In particular
\[
\|\mu-\mu_{f_n}\|\le2m\,2^{-2n}\longrightarrow0.
\tag{NC.22}
\]
We next construct coefficients for this limit; a general norm-closedness assertion about a predual is unnecessary.

### 18.7. A countable square-summable assembly for the whole functional

For each \(n\), realize \(\mu_{f_{n+1}}\) by [Section 18.6](car-fock-and-quasifree-states.md#18-6-finite-compressions-and-their-exact-coefficient-norms) on the finite direct sum \(K_{n+1}\). Write its representing vector as \(\eta\), and abbreviate its diagonal representation by \(D\). Set
\[
\zeta=D(f_n)\eta,\qquad d=\eta-\zeta.
\]
Since \(f_n\le f_{n+1}\), direct multiplication gives
\[
\langle\zeta,D(x)\zeta\rangle
 =\mu_{f_{n+1}}(f_nxf_n)=\mu_{f_n}(x).
\]
Also
\[
\|\eta\|,\|\zeta\|\le\sqrt m,\qquad
\|d\|^2
=\mu_{f_{n+1}}(1-f_n)
=\mu(f_{n+1}-f_n)
\le m\,2^{-4n}.
\tag{NC.23}
\]
Therefore the difference \(\Delta_n=\mu_{f_{n+1}}-\mu_{f_n}\) has the exact two-coefficient expression
\[
\Delta_n(x)
=\langle d,D(x)\eta\rangle+\langle\zeta,D(x)d\rangle.
\tag{NC.24}
\]
On writing all components of these vectors in \(H\), this becomes a finite list of pairs \((a,b)\) with coefficients \(\langle a,xb\rangle\). Scalar Cauchy–Schwarz on the components proves that the sum of their products of norms is at most
\[
\|d\|\|\eta\|+\|\zeta\|\|d\|
\le2m\,2^{-2n}.
\tag{NC.25}
\]
This includes every off-diagonal contribution of the original functional; merely summing its diagonal corner restrictions would not do so.

Start with the finite diagonal list representing \(\mu_{f_1}\), whose product-of-norms sum is \(\|\eta_{F_1}\|^2=\mu(f_1)\le m\). Append all the finite lists in (NC.24), in the order \(n=1,2,\ldots\). This is a countable list. Delete a pair when either vector is zero. For each remaining pair define
\[
\lambda=\sqrt{\frac{\|b\|}{\|a\|}},\qquad
u=\lambda a,\qquad v=\lambda^{-1}b.
\]
The number \(\lambda\) is positive real, so the coefficient is unchanged, and
\[
\|u\|^2=\|v\|^2=\|a\|\|b\|.
\]
The resulting concatenated sequences satisfy
\[
\sum_j\|u_j\|^2=\sum_j\|v_j\|^2
\le m+\sum_{n\ge1}2m\,2^{-2n}
=\frac53m<\infty.
\tag{NC.26}
\]
If the list is finite, append zero vectors.

For every \(x\in A\), the coefficient series is absolutely convergent, since
\[
\sum_j|\langle u_j,xv_j\rangle|
\le\|x\|\sum_j\|u_j\|\|v_j\|
\le\tfrac53m\|x\|.
\]
Its partial sums taken after full difference blocks telescope to \(\mu_{f_N}(x)\). By (NC.22), those converge to \(\mu(x)\). Absolute convergence identifies the entire coefficient series with this same limit. This proves (NC.2), and (NC.5) proves *global* concrete ultraweak continuity.

### 18.8. Order normality, complete additivity and the reverse implication

For an arbitrary orthogonal family \((p_\alpha)\subseteq A\), the finite sums \(p_F\) converge strongly to the projection \(p\) onto the closed span of their ranges. Its membership in \(A\) is supplied by the projection-join proof. It is also their supremum as positive operators: if a selfadjoint \(b\) majorizes every \(p_F\), taking scalar quadratic limits gives \(b\ge p\). Thus \(p_F\uparrow p\) is a bounded increasing positive net with that supremum. Applying (NC.1) yields
\[
\mu(p)=\sup_F\sum_{\alpha\in F}\mu(p_\alpha).
\tag{NC.27}
\]
This proves the complete-additivity hypothesis used in [Section 18.4](car-fock-and-quasifree-states.md#18-4-a-maximal-orthogonal-collection-of-dominated-corners) when starting from (NC.1). For NC-P that hypothesis is already assumed, and the entire [Section 18.1](car-fock-and-quasifree-states.md#18-1-positive-forms-and-the-topology-that-must-be-proved)–[Section 18.7](car-fock-and-quasifree-states.md#18-7-a-countable-square-summable-assembly-for-the-whole-functional) proof applies without this reduction or any order-normality premise. No equivalence between two meanings of normality has been assumed.

For the converse, we first verify an elementary fact about the concrete topology. If \(x_i\to x\) in WOT and \(\sup_i\|x_i\|\le C\), then \(\|x\|\le C\), because the bounds on all vector coefficients pass to the limit and Hilbert Riesz, or the Hilbert norm supremum, gives this norm bound. For one coefficient family in (NC.5), the tail estimate is
\[
\left|\sum_{j>N}\langle u_j,(x_i-x)v_j\rangle\right|
\le2C
 \left(\sum_{j>N}\|u_j\|^2\right)^{1/2}
 \left(\sum_{j>N}\|v_j\|^2\right)^{1/2}.
\tag{NC.28}
\]
Choose \(N\) to make this uniformly small, and then use WOT convergence on the finite initial sum. This proves bounded WOT convergence implies concrete ultraweak convergence, for nets as well as sequences and without a separability assumption. If \(C=0\), all operators are zero.

The supplied bounded-monotone proof in [periodic CAR Section 8.1](constant-car-states-and-the-periodic-core.md#8-1-the-elementary-operator-facts-used-below) gives \(a_i\to a\) strongly for every bounded increasing positive net with supremum \(a\) in \(A\). Alternatively its limiting quadratic form constructs that supremum directly, and the square-root inequality \(d^2\le C d\) proves the strong convergence. Hence \(a_i\to a\) in WOT and, by (NC.28), ultraweakly. Ultraweak continuity of \(\mu\) gives \(\mu(a_i)\to\mu(a)\); positivity makes this scalar net increasing, so its limit is its supremum. This is (NC.1).

### 18.9. The exact finite-corner consequence and remaining scope

Let \(M\subseteq B(H)\) be any concrete von Neumann algebra and \(e\in M\) a projection. The corner \(eMe\) is a concrete von Neumann algebra on \(eH\), by the extension-by-zero argument in [Section 18.4](car-fock-and-quasifree-states.md#18-4-a-maximal-orthogonal-collection-of-dominated-corners). Let \(\theta:eMe\to\mathbb C\) be bounded, positive, and order normal, with the corner identity \(e\). Applying the proved theorem on \(eH\) gives its coefficient representation and ultraweak continuity there. For bounded \(x_i,x\in eMe\) that converge in WOT on \(H\), their restrictions converge in WOT on \(eH\). Formula (NC.28) and the coefficient representation therefore give
\[
\theta(x_i)\longrightarrow\theta(x).
\tag{NC.29}
\]

For a semifinite order-normal trace \(\tau\), whenever a projection \(e\) satisfies \(0<\tau(e)<\infty\), the bounded positive linear restriction \(\theta=\tau|_{eMe}\), once its linear extension has been constructed, is order normal: the corner supremum of a bounded increasing positive net is also its supremum in \(M\) by the same strong limiting form, so order normality of \(\tau\) passes to the restriction. Thus (NC.29) supplies the continuity passage for a *hypothetical* finite-trace corner.

This section proves positive-functional normal continuity. The separate finite-factor trace construction is supplied in [Section 19](car-fock-and-quasifree-states.md#19-a-normal-trace-on-a-finite-factor-acting-on-a-separable-hilbert-space), and the constant-state projection contradiction in [Section 20](car-fock-and-quasifree-states.md#20-constant-faithful-car-states-have-no-nonzero-finite-projection-away-from-half). Extension of a corner trace to the whole algebra, general trace/semifiniteness equivalences, type III subtype, modular classification and continuous-core results are outside this normal-continuity argument. The full linear coefficient-space norm closure and completeness are proved in [Section 19.1](car-fock-and-quasifree-states.md#19-1-hahn-banach-and-the-concrete-coefficient-banach-space); they are not premises of the direct coefficient assembly above.

### 18.10. Human-source comparison and proof routes

The domination-corner method also appears in Jacob Lurie, [Math 261y, Lecture 11](https://www.math.ias.edu/~lurie/261ynotes/lecture11.pdf), Proposition 11 and the following maximal-family argument, and in the proof of Théorème 3 of Jacques Dixmier, [Formes linéaires sur un anneau d'opérateurs](https://www.numdam.org/item/BSMF_1953__81__9_0/), *Bulletin de la Société Mathématique de France* 81 (1953), 9–39. The present proof explicitly constructs the finite projection approximations and the final coefficient series.

Lurie's [Lecture 12](https://www.math.ias.edu/~lurie/261ynotes/lecture12.pdf) completes the topology passage using a Banach predual and Krein–Smulian. Dixmier passes from finite approximants to strong continuity on the unit ball, which gives ultraweak continuity by his Théorème 2. Those completion steps are not consumed here. [Section 18.5](car-fock-and-quasifree-states.md#18-5-full-concrete-vector-realization-under-vector-domination)–[Section 18.7](car-fock-and-quasifree-states.md#18-7-a-countable-square-summable-assembly-for-the-whole-functional) instead realize finite positive compressions, retain their exact vector norms, and assemble one square-summable coefficient pair directly.

A different supplied route, normal and singular parts, Sections 10–11 through Example 11.8, proves Corollary 11.5 using normal–singular splitting, a singular-functional projection criterion, universal bidual central projections, and spectral projection approximation. Those results are comparison context. The present positive-functional proof uses the explicitly constructed concrete Hilbert/operator arguments above.

## 19. A normal trace on a finite factor acting on a separable Hilbert space

This section gives a proof reconstruction of faithful normal trace existence for a nonzero finite factor acting on a separable Hilbert space. Its later application is a hypothetical nonzero finite projection in the faithful countable constant CAR factor. The proof supplies the finite-factor trace-existence branch, including the compactness and separable fixed-point arguments. Its exact positive normal-continuity input is Theorem NC-P in [Section 18](car-fock-and-quasifree-states.md#18-order-normal-positive-functionals-and-the-concrete-ultraweak-topology).

The concrete prerequisites are the supplied [ITP Sections 10.1–10.6](infinite-tensor-products.md#10-1-inner-product-estimates-and-orthogonal-projection) Hilbert/operator and bicommutant constructions, [periodic CAR Sections 8.1–8.7](constant-car-states-and-the-periodic-core.md#8-1-the-elementary-operator-facts-used-below) roots, supports, joins, polar decompositions, orthogonal partial-isometry sums, comparison and positive parts, and the positive NC-P assertion: a bounded positive functional completely additive on arbitrary orthogonal projection families is a square-summable concrete coefficient functional. The order-normal version follows separately and is not substituted for NC-P. All these inputs are kept at their actual scope. No abstract universal bidual, spectral measure, general semifiniteness/type classification or continuous core is used.

F. J. Yeadon, [A new proof of the existence of a trace in a finite von Neumann algebra](https://www.ams.org/journals/bull/1971-77-02/S0002-9904-1971-12708-8/), *Bulletin of the American Mathematical Society* 77 (1971), 257–260, proves the general center-valued theorem by the same compactness and fixed-point route. Positive continuity is Théorème 3 of Dixmier's [Formes linéaires sur un anneau d'opérateurs](https://www.numdam.org/item/BSMF_1953__81__9_0/). The compactness criterion is the sufficiency direction of Theorem II.2 in Charles A. Akemann, [The dual space of an operator algebra](https://www.ams.org/journals/tran/1967-126-02/S0002-9947-1967-0206732-8/), *Transactions of the American Mathematical Society* 126 (1967), 286–302; its converse is not used. Yeadon's Lemmas 1 and 2 give the projection-uniformity argument. Yeadon's theorem applies the Ryll-Nardzewski fixed-point theorem and proves a broader center-valued conclusion. Here the needed fixed-point theorem is proved for the separable coefficient Banach space, and the conclusion retains the nonzero finite-factor hypotheses. Full linear coefficient-space completeness is established below; the present proof does not import the predual results used in Yeadon's proof or the center-valued trace theorem.

### 19.1. Hahn–Banach and the concrete coefficient Banach space

We first spell out the elementary Banach facts needed below. For a real linear functional f on a subspace, dominated by a sublinear function P, adjoining one vector z outside its domain is possible: choose its value alpha between
\[
 \sup_w(f(w)-P(w-z))\quad\hbox{and}\quad
 \inf_w(P(w+z)-f(w)).                                      \tag{FT1}
\]
The first bound is at most the second, since for any w,v the inequality f(w+v)≤P(w+v)≤P(w-z)+P(v+z) proves the corresponding pairwise bound. Scaling positive or negative coefficients of z verifies domination on the enlarged subspace. Unions of chains of extensions remain linear and dominated. Zorn therefore extends f to the whole real space. For a complex functional start with its real part g, apply this to P(x)=C||x||, and define F(x)=g(x)-ig(ix). This is complex linear, extends the original functional, and has norm at most C: rotate each x by a scalar phase to make F(x) real nonnegative and apply the real bound. In particular the norm of a Banach-space vector is the supremum of the absolute values of its evaluations under norm-one functionals, by starting with that vector's one-dimensional norming functional.

Let G be a complex Hilbert space. Form the algebraic tensor space \(\overline G\otimes G\), with the projective norm
\[
 \|s\|_\pi=\inf\left\{\sum_j\|\xi_j\|\|\eta_j\|:
           s=\sum_j\overline{\xi_j}\otimes\eta_j\right\}.
                                                               \tag{FT2}
\]
Each bounded operator T defines a bounded functional \(s\mapsto\sum_j\langle\xi_j,T\eta_j\rangle\) of norm at most ||T||. This norm is nondegenerate: for a nonzero finite tensor, choose orthonormal bases for its finite first and second leg spans. A nonzero matrix coefficient is detected by the rank-one operator sending the corresponding second basis vector to the first. Such an operator's evaluation has absolute value bounded by every sum in (FT2). The triangle and scalar identities follow by concatenating decompositions and scaling; hence (FT2) is a norm. Let S be its completion.

Conversely, a bounded linear functional on S restricts to a bounded sesquilinear form on G×G, of bound its norm. Hilbert Riesz gives a unique bounded operator T representing that form. Testing unit elementary tensors shows equality of the functional norm and ||T||. Consequently
\[
                        S^*=B(G)\quad\hbox{isometrically}.    \tag{FT3}
\]
Every element of S is a convergent series of elementary tensors with summable products of leg norms. Indeed approximate it successively by finite tensors with errors at most 2^{-2k}, telescope the approximants, and choose finite decompositions of each difference within 2^{-2k} of its projective norm. Collecting all terms gives a summable total. Zero terms can be omitted; replacing each pair by a reciprocal scalar rescaling makes both squared leg norms equal to its original product. The resulting two leg sequences have finite square sums. Conversely every two square-summable leg sequences give a projectively summable series, by scalar Cauchy–Schwarz. Thus S gives exactly the concrete square-summable coefficient functionals on B(G), allowing a kernel.

For a unital von Neumann algebra N⊂B(G), let Y be the closed subspace of S whose coefficient functionals vanish on N, and let B=S/Y. Completeness of this quotient follows directly: pass from any quotient Cauchy sequence to a subsequence with successive distances below 2^{-k}, lift successive differences with norms below 2^{1-k}, and sum them in S; then the whole original sequence converges in the quotient. Its dual consists isometrically of the elements of S\* annihilating Y, by lifting bounded quotient functionals and by the quotient norm definition.

That annihilator is exactly N. One inclusion is the definition of Y. If T∉N=N'', choose a∈N' with Ta−aT≠0, and vectors ξ,η for which its coefficient is nonzero. The finite coefficient functional
\[
 x\longmapsto\langle\xi,x a\eta\rangle
                   -\langle a^*\xi,x\eta\rangle              \tag{FT4}
\]
vanishes on N and detects T. Hence T fails to annihilate Y. We have proved B\*=N isometrically. Hahn–Banach norm duality therefore makes the natural coefficient map B→N\* isometric: its norm is the supremum of |b(x)| over x∈N with ||x||≤1. Its image is exactly the restrictions of concrete square-summable coefficient functionals, and this image is norm closed because B is complete. This proves full linear coefficient-space completeness without a universal bidual or an unproved norm-closure theorem.

If G is separable, choose a countable dense set of finite rational complex linear combinations of a countable orthonormal basis. Finite elementary tensors from this set, with rational complex coefficients, form a countable dense subset of S in (FT2): approximate each leg of a finite tensor and use ||bar(ξ)⊗η||π≤||ξ||||η||. Thus B is separable. Below B has its Banach weak topology σ(B,B\*)=σ(B,N).

### 19.2. Finite-factor cancellation and increasing subequivalence

Assume N is a factor and its identity is finite: no partial isometry has initial projection 1 and final projection a proper subprojection of 1. Every projection e is finite. Otherwise a partial isometry from e onto f<e, added to 1−e, would violate finiteness of 1.

[periodic CAR Section 8.6](constant-car-states-and-the-periodic-core.md#8-6-full-projection-comparison-with-no-countability-restriction) proves comparison of every two projections in a factor by an actual maximal orthogonal family of partial isometries. If p~q in N, apply comparison to 1−p and1−q. If 1−p embeds into a projection r≤1−q, adding its implementing partial isometry to one implementing p~q gives initial1 and final q+r. Finiteness forces q+r=1. Thus 1−p~1−q. The reverse comparison gives the same conclusion by interchanging p,q. This proves complement cancellation. It holds also in a finite factor corner; the same argument only uses factor comparison and its finite identity.

In particular, if a≤b, a~c≤F, and b≾F, then b−a≾F−c. If F=0, all four projections are zero and the assertion is immediate. Assume F≠0. Embed b into d≤F, with the image a'≤d of a. The equivalence a'~c gives 1−a'~1−c by the preceding argument. Compressing the implementing equivalence to d−a' yields d−a'≾1−c, but the required refinement inside F follows by applying cancellation in FNF. This corner is a factor: if a central selfadjoint element of FNF is nonscalar, the positive-part/support construction in [periodic CAR Section 8.7](constant-car-states-and-the-periodic-core.md#8-7-minimal-projections-have-scalar-corners) gives a nonzero proper central projection z<F. [Corner contact in periodic CAR Section 8.5](constant-car-states-and-the-periodic-core.md#8-5-central-support-and-contact-between-two-corners) then gives zN(F−z)≠0, contrary to centrality in FNF. Hence its center is scalar. F is finite, as just proved. Cancellation inside F gives F−a'~F−c, proving the asserted refinement.

Suppose e\_k increases, e=∨e\_k, and e\_k≾F for all k. Inductively choose orthogonal projections f\_k≤F and equivalences e\_1~f\_1, e\_k−e\_{k−1}~f\_k for k>1. At a step the sum of the earlier f's is equivalent to e\_{k−1}, so the refinement just proved embeds the next difference under the remaining part of F. The supplied strong and adjoint-strong orthogonal partial-isometry sum then implements
\[
                       e\sim\sum_k f_k\le F.                \tag{FT5}
\]
This proves increasing subequivalence continuity, rather than quoting a projection-dimension theorem.

For projections p,q, the polar decomposition of (1−p)q gives
\[
                       (p\vee q)-p\sim q-(p\wedge q).        \tag{FT6}
\]
Indeed its kernel on qG is pG∩qG. Its closed range is (p∨q)G∩pG-perpendicular: apply1−p to the dense span pG+qG in (p∨q)G. The initial and final polar supports are exactly the displayed projections. The polar partial isometry belongs to N by [periodic CAR Section 8.3](constant-car-states-and-the-periodic-core.md#8-3-supports-and-polar-decomposition-inside-m).

### 19.3. Uniform orthogonal smallness of a positive unitary orbit

Take a positive concrete coefficient functional φ on N, and let Q be the norm-closed convex hull of \(\{\phi(u^*\cdot u):u\in\mathcal U(N)\}\) in B. All its elements are positive and have the same value φ(1); positivity and that value pass to norm limits.

We prove that for every orthogonal sequence of projections f\_n,
\[
                         \sup_{\psi\in Q}\psi(f_n)\to0.       \tag{FT7}
\]
It suffices to check the orbit, since convex combinations and norm limits preserve the uniform bound. If this fails, pass to a subsequence (still written f\_n) and choose unitaries u\_n with φ(g\_n)≥δ>0, where g\_n=u\_n^\*f\_nu\_n~f\_n. Put
\[
 p_{m,n}=\bigvee_{j=n}^{m}g_j,\qquad
 p_n=\bigvee_{j\ge n}g_j,\qquad p=\bigwedge_n p_n.             \tag{FT8}
\]
By induction p\_{m,n}≾sum\_{j=n}^m f\_j. At an induction step (FT6) shows that the newly added projection difference is subequivalent to g\_{m+1}~f\_{m+1}; orthogonal partial-isometry addition gives the claim. Apply (FT5) to get p\_n≾F\_n=∑\_{j≥n}f\_j. Refinement or complement cancellation gives1−F\_n≾1−p\_n≤1−p. The projections1−F\_n increase strongly to1, so a further (FT5) yields1≾1−p. Finiteness forces p=0. Thus p\_n decreases strongly to0 by the supplied projection meet construction. Since0≤g\_n≤p\_n, positive-form Cauchy–Schwarz or the norm-one projection estimate gives g\_n→0 strongly too. Bounded strong convergence implies concrete coefficient convergence, by truncating the two square-summable leg sequences and uniformly controlling the tails. Therefore φ(g\_n)→0, contradicting δ. This proves (FT7).

### 19.4. Compactness of the entire positive convex hull

First, any bounded ball in N\* is compact for pointwise convergence on N. Here is the compactness input explicitly. A maximal filter extending any given proper filter exists by Zorn; maximality makes it an ultrafilter. An ultrafilter on a compact scalar disk converges: otherwise finitely many neighborhoods excluding its limit candidates would cover the disk and contradict the filter property; finite-dimensional disk compactness follows from real completeness and successive bisection. For a bounded family of functionals, each coordinate x lies in the disk of radius C||x||. An ultrafilter therefore has a limit in every coordinate. These limits respect addition, complex scaling and the bound, so form an element of the same dual ball. The ultrafilter compactness criterion follows from the finite-intersection characterization of compactness: any family of closed sets with the finite-intersection property extends to an ultrafilter; a limit belongs to all of them. Conversely a nonconvergent ultrafilter supplies a finite-cover contradiction. This proves the required dual-ball compactness without an unproved product compactness theorem.

Let Q1 be the pointwise closure of Q in that ball. It is compact and consists of positive functionals with value φ(1). Every ψ∈Q1 is completely additive on projections. To see this, let(e\_j) be any orthogonal family, e=∑e\_j. Each original θ∈Q is concretely normal, hence θ(e)=∑θ(e\_j). If these sums did not converge uniformly for θ∈Q, a fixed δ>0 would allow inductive disjoint finite subsets J\_n and functionals θ\_n∈Q with θ\_n(∑\_{j∈J\_n}e\_j)>δ. Indeed, after choosing the earlier finite sets, choose a θ with tail>δ and use its actual sum equality to choose a new finite portion in that tail. The resulting orthogonal sequence violates(FT7). Thus
\[
 \sup_{\theta\in Q}\left|\theta(e)-\theta\left(\sum_{j\in F}e_j\right)\right|
                         \longrightarrow0                    \tag{FT9}
\]
over the directed finite sets F. The inequalities pass to Q1 by pointwise closure, and prove ψ(e)=∑ψ(e\_j).

The exact positive NC-P theorem used here takes complete additivity on arbitrary orthogonal projection families as its hypothesis and constructs a concrete square-summable coefficient representation. Its vector-dominated-corner proof is supplied separately; order normality is not substituted for this hypothesis. Applying that exact NC-P assertion from [Section 18](car-fock-and-quasifree-states.md#18-order-normal-positive-functionals-and-the-concrete-ultraweak-topology) to each positive ψ∈Q1 gives Q1⊂B.

Under that exact positive complete-additivity-to-coefficient NC input, Q1⊂B. Since B\*=N, the pointwise topology restricted to B is its full Banach weak topology. Moreover Q is weakly closed. For completeness, a norm-closed convex subset C of a Banach space is weakly closed. The empty set needs no argument. Otherwise take x outside C, choose d>0 with the open d-ball at x disjoint from C, fix c0∈C, and put D=C+ball(0,d/2)−c0. This is an open convex set containing ball(0,d/2), and x−c0 is outside D. On the underlying real vector space define
\[
 p_D(v)=\inf\{s>0:v\in sD\}.
\]
The contained ball makes this gauge finite and gives \(0\le p_D(v)\le2\|v\|/d\). Its positive homogeneity follows by changing s. If \(v\in aD\) and \(w\in bD\), convexity gives \(v+w\in(a+b)D\); taking a and b arbitrarily close above the two infima proves subadditivity. Also \(D=\{v:p_D(v)<1\}\): a representation in sD with s<1 lies in D by convexity and 0∈D; conversely openness lets a point of D be scaled slightly outward while remaining in D, so its gauge is less than one. In particular \(p_D(x-c0)\ge1\).

On the real line through x−c0 define \(\ell(t(x-c0))=t p_D(x-c0)\). For t≥0 this equals the gauge, and for t<0 it is nonpositive and therefore at most the nonnegative gauge. The full real Hahn–Banach argument in (FT1) extends this linear functional with \(\ell(v)\le p_D(v)\) everywhere. Applying the same bound to −v gives \(|\ell(v)|\le2\|v\|/d\), so it is bounded and nonzero. Choose b with \(\|b\|<d/2\) and \(\delta=\ell(b)>0\). For each c∈C, the vector c−c0+b belongs to D, whence \(\ell(c-c0)<1-\delta\), while \(\ell(x-c0)\ge1\). These uniform inequalities give a weakly open half-space around x disjoint from C. In a complex Banach space, \(L(v)=\ell(v)-i\ell(iv)\) is bounded and complex linear, with real part ℓ, so the same half-space is open for its complex weak topology. Thus Q is weakly closed. It follows Q=Q1 and Q is weakly compact. Only compactness sufficiency for this positive Q is proved or consumed; the converse of Akemann's criterion and Eberlein–Smulian are unnecessary.

### 19.5. The separable Banach isometry fixed-point theorem

Let B be a separable Banach space and Q a nonempty weakly compact convex subset, invariant under a group of affine surjective norm isometries which are weakly continuous. We give the entire fixed-point argument for this exact scope.

Choose, by Zorn and compactness of nested intersections, a minimal nonempty weakly compact convex invariant subset Q0⊂Q. Inside Q0 similarly choose a minimal nonempty weakly closed invariant subset K, without a convexity requirement. Every orbit in K is weakly dense: its weak closure is a nonempty closed invariant subset, hence equals K.

For any ε>0, separability covers K by countably many closed norm balls of radius ε/4. These balls are weakly closed by Hahn–Banach norm duality. The compact Hausdorff space K is a Baire space. Here is the version needed: if countably many closed subsets of K had empty interior, recursively choose nonempty relatively open neighborhoods with closures inside the preceding neighborhood and excluding the next closed set; compact Hausdorff regularity permits these choices, and compactness gives a point in all nested closures, contradicting the alleged cover. Regularity follows by separating a point from every point of a compact closed set by Hausdorff neighborhoods and taking a finite subcover. Thus one of the closed balls has nonempty relative weak interior U in K. Its norm diameter is at most ε/2.

Density of every orbit implies the translates gU cover K: for each k some g^{-1}k belongs to U. Compactness reduces this to finitely many translates. Each has norm diameter at most ε/2, since the action is isometric. Choosing one point from each nonempty translate gives a finite ε-net. Hence K is norm totally bounded. It is norm closed and lies in complete B, so it is norm compact: extract a Cauchy subsequence by successive finite nets from any sequence, and use completeness; the finite-net argument also proves compactness directly.

If its norm diameter d were positive, cover K by finitely many norm balls of radius d/4 centered at k1,…,kn∈K. Their average y lies in Q0. For every k∈K at least one distance ||k−ki||≤d/4, and all others are at most d, so
\[
                         \|y-k\|\le d-\frac{3d}{4n}=r<d.     \tag{FT10}
\]
The set C={x∈Q0:||x−k||≤r for every k∈K} is nonempty, convex, weakly closed and invariant. It is proper: since r<d, some two points of K have distance>r, so one of them is outside C. This contradicts minimality of Q0. Hence d=0 and K is a singleton. Its invariance means its unique point is fixed by every group element. This proves the exact fixed-point theorem used below, with no strict-convex renorming, amenability, invariant mean or general Ryll-Nardzewski theorem imported.

### 19.6. A faithful normal normalized trace

Let N be a nonzero finite factor on separable G. Choose a unit vector η and the positive normal functional φ(x)=<η,xη>. The conjugation maps L\_uψ(x)=ψ(u^\*xu) act as onto linear norm isometries on B: operator conjugation is isometric and maps N's unit ball onto itself. They are weakly continuous since evaluation at x after L\_u is evaluation at u^\*xu. They preserve Q, and [Section 19.4](car-fock-and-quasifree-states.md#19-4-compactness-of-the-entire-positive-convex-hull) makes Q weakly compact using Theorem NC-P in [Section 18](car-fock-and-quasifree-states.md#18-order-normal-positive-functionals-and-the-concrete-ultraweak-topology). The separable fixed-point theorem gives τ∈Q satisfying L\_uτ=τ for every unitary u. Positivity and τ(1)=1 hold on all Q, and τ is concretely normal because τ∈B.

It is a trace. For a unitary u and arbitrary x, apply invariance to ux to obtain τ(xu)=τ(ux). Every element is a linear combination of unitaries by [periodic CAR Section 8.5](constant-car-states-and-the-periodic-core.md#8-5-central-support-and-contact-between-two-corners)'s norm-series root construction, so τ(xy)=τ(yx) for all x,y. In particular τ(x\*x)=τ(xx\*).

We also prove faithfulness. Let z be the join of every projection q with τ(q)=0. Finite joins still have zero trace: for q,r of zero trace, (FT6) makes (q∨r)−q equivalent to r−q∧r, whose trace is at most τ(r)=0; trace equivalence uses the actual polar partial isometry. Normality and increasing finite joins give τ(z)=0. Unitary invariance makes the family of zero-trace projections invariant, so z is central. In a factor z is0 or1; since τ(1)=1, it is0.

If a≥0 and τ(a)=0 but a≠0, its nonzero positive part b=(a−δ1)\_+ for some δ>0 has nonzero support e and a≥δe. This positive-part/support inequality is the complete norm-series construction in [Section 18.2](car-fock-and-quasifree-states.md#18-2-finite-positive-projection-approximation-without-a-spectral-theorem): choose δ smaller than a positive unit quadratic value, form the positive part from((a−δ1)^2)^{1/2}, and use its orthogonal positive/negative supports. Therefore0≤δτ(e)≤τ(a)=0, contradicting the absence of nonzero zero-trace projections. Thus τ is faithful on N+.

The conclusion is a faithful concrete-normal tracial state on a finite factor acting on separable G. No uniqueness or center-valued trace theorem is claimed or needed. Its hypotheses keep both finiteness and factoriality; the proof does not infer finiteness from an unrelated product trace.

### 19.7. Exact boundary and the constant CAR application

A nonzero finite projection e in the already proved constant CAR factor yields the finite factor eMe on separable eH. Factoriality follows from the central projection/contact argument in [Section 19.2](car-fock-and-quasifree-states.md#19-2-finite-factor-cancellation-and-increasing-subequivalence); its identity e is finite by definition. The construction therefore supplies a faithful normal finite-corner trace by Theorem NC-P in [Section 18](car-fock-and-quasifree-states.md#18-order-normal-positive-functionals-and-the-concrete-ultraweak-topology) and the complete finite-factor construction above. Under the tail-centrality and occupation-limit estimates proved in [Section 20.2](car-fock-and-quasifree-states.md#20-2-the-whole-tail-commutator-limit) and [Section 20.3](car-fock-and-quasifree-states.md#20-3-both-occupation-limits-on-the-entire-completion), the two compressed-tail products have trace limits pτ(e) and(1−p)τ(e), while traciality equates them. This contradicts p≠1/2 and τ(e)>0. The completed argument in [Section 20](car-fock-and-quasifree-states.md#20-constant-faithful-car-states-have-no-nonzero-finite-projection-away-from-half) excludes all nonzero finite projections and proves the exact typeIII naming step for this constant state.

The complete application to original (20) is proved in [Section 20](car-fock-and-quasifree-states.md#20-constant-faithful-car-states-have-no-nonzero-finite-projection-away-from-half). The exact input at the compactness step is the complete-projection-additivity version NC-P from [Section 18](car-fock-and-quasifree-states.md#18-order-normal-positive-functionals-and-the-concrete-ultraweak-topology); its order-normal version alone is not substituted. General product semifiniteness criteria, typeIII subtype, modular fixed-factor spectrum, continuous core and center flow remain outside this finite-factor trace construction.

## 20. Constant faithful CAR states have no nonzero finite projection away from half

This is a full proof reconstruction of original CAR equation(20) and its immediately stated typeIII conclusion, for separable infinite-dimensional complex K and0<p<1, p≠1/2. It preserves the original exclusions of finite-dimensionalK and endpoint densities. It uses neither the general ITP semifiniteness criterion nor a trace extension from a finite corner to the whole algebra.

The completed pointed algebra is supplied by [CAR Sections 15.2–15.8](car-fock-and-quasifree-states.md#15-2-every-finite-diagonal-covariance-density-matrix) and [ITP Sections 11.1–11.3](infinite-tensor-products.md#11-1-scalar-powers-and-the-local-hilbert-schmidt-model). [CAR Section 13](car-fock-and-quasifree-states.md#13-factorality-for-every-positive-contraction) supplies the full factor proof for the actual CAR von Neumann algebra. The whole finite-factor trace-existence construction in [Sections 19.1–19.6](car-fock-and-quasifree-states.md#19-1-hahn-banach-and-the-concrete-coefficient-banach-space) is used with its exact positive NC-P input from [Section 18](car-fock-and-quasifree-states.md#18-order-normal-positive-functionals-and-the-concrete-ultraweak-topology). Bounded finite-corner continuity is supplied by [Sections 18.8–18.9](car-fock-and-quasifree-states.md#18-8-order-normality-complete-additivity-and-the-reverse-implication). No broader generic trace/type theorem is inferred from those scoped inputs.

### 20.1. The actual entire completed algebra and factor

Put a=1−p, b=p and rho=diag(a,b). Let H0=M2(C) with Hilbert–Schmidt inner product linear in the second variable, Omega0=rho^(1/2), and let H be the pointed completion of the increasing finite spaces H0^tensor n, embedded by appending Omega0. Write Omega for its reference vector, An for the left finite matrix algebra, and M=(union An)''. [ITP Section 11.2](infinite-tensor-products.md#11-2-the-pointed-countable-product-and-its-complete-basis) supplies the onto grouping H=H0^tensor n tensor H>n, with its whole complete dense finite-vector span. [ITP Section 11.3](infinite-tensor-products.md#11-3-the-concrete-algebra-and-faithful-product-vector) proves that the left and commuting right local orbits of Omega are both dense. Density of finite products over a finite-dimensional leg makes H separable: take the union of finite rational complex linear combinations of a fixed finite leg basis on every finite stage; it is a countable dense set.

[CAR Sections 15.2–15.8](car-fock-and-quasifree-states.md#15-2-every-finite-diagonal-covariance-density-matrix) supplies an onto pointed unitary W from the actual completed reduced doubled-Fock cyclic CAR representation onto H, with WMpW\*=M on every element, both directions concretely normal, and WOmega\_p=Omega. [CAR Section 13](car-fock-and-quasifree-states.md#13-factorality-for-every-positive-contraction) proves Mp is a factor at the same constant covariance, so M is a nonzero factor: its center conjugates onto the center of Mp; its identity acts on the nonzero reference vector. No finite-dimensional moment identity is being substituted for this whole normal algebra identification.

### 20.2. The whole tail commutator limit

For X∈M2 let Xj be its left action in coordinatej. On one Hilbert–Schmidt leg, right multiplication by Y=rho^(−1/2)Xrho^(1/2) has norm at most C(p)||X||, where C(p)=sqrt(max(p,1−p)/min(p,1−p))<infinity. This follows by the finite matrix norm bound on rows, summed over their squared norms; the tensor amplification bound is the complete [ITP Section 10.4](infinite-tensor-products.md#10-4-tensor-operators-and-bounded-mixed-compressions) proof. Its coordinatej right action Rj commutes with every left local matrix. Commutation with a fixed bounded operator is WOT closed; [ITP Section 10.5](infinite-tensor-products.md#10-5-the-unital-bicommutant-theorem-by-finite-vector-amplification) supplies the whole bicommutant closure, so Rj commutes with every element of M. Matrix multiplication at the reference vector gives
\[
 X_j\Omega=R_j\Omega,\qquad \|R_j\|\le C(p)\|X\|.             \tag{CF1}
\]

For u∈M, choose z∈An with ||(u−z)Omega||<epsilon by left cyclicity. For j>n, z commutes with Xj. The exact reference relation and right commutation then give
\[
 \|[u,X_j]\Omega\|
 \le\|(u-z)X_j\Omega\|+\|X_j(u-z)\Omega\|
 \le(C(p)+1)\|X\|\varepsilon.                                \tag{CF2}
\]
Thus [u,Xj]Omega→0. For every bounded right-local r, both u and Xj commute with r, so [u,Xj]rOmega=r[u,Xj]Omega→0. Those vectors are dense, while ||[u,Xj]||≤2||u||||X||. Approximate an arbitrary vector by one from that dense orbit, use the common bound on the approximation error, and then use the proved limit on the orbit. This proves
\[
 [u,X_j]\to0\quad\hbox{strongly on all of }H.                 \tag{CF3}
\]
Applying the same argument to X\* also proves the adjoint strong limit. No operator-norm approximation of u and no boundedness assertion about arbitrary WOT nets is used.

Take X=E12. In the actual CAR bridge, this is the parity-corrected mode bj=Z1…Z(j−1)a(ej), where Zi=1−2a(ei)\*a(ei). The original odd mode has a prefix parity string and is not substituted for this commuting tail. Its occupation is unchanged: bj\*bj=a(ej)\*a(ej).

### 20.3. Both occupation limits on the entire completion

Let Nj=Xj\*Xj=E22 in coordinatej and Dj=XjXj\*=E11 in coordinatej. For xi,eta in the embedded finite Hilbert space Hn and j>n, the reference-tail inner product gives
\[
 \langle\xi,N_j\eta\rangle=p\langle\xi,\eta\rangle,
 \qquad\langle\xi,D_j\eta\rangle=(1-p)\langle\xi,\eta\rangle.    \tag{CF4}
\]
All these projections have norm one. Approximate arbitrary xi and eta by finite-stage vectors. Expanding the coefficient difference and applying the operator norm-one bound to each error proves
\[
                  N_j\to p1,\qquad D_j\to(1-p)1\quad\hbox{in WOT}.
                                                               \tag{CF5}
\]
This is a full two-vector estimate, with no claim of strong convergence for the occupations themselves.

### 20.4. A hypothetical finite projection supplies a finite normal corner trace

Suppose0≠e∈M is a finite projection, meaning no partial isometry in M has initial e and a proper final subprojection of e. The corner N=eMe on eH is a nonzero concrete von Neumann algebra, by extension by zero on(1−e)H and WOT closedness. Its identity e is finite by the hypothesis. It is a factor, by the full [Section 19.2](car-fock-and-quasifree-states.md#19-2-finite-factor-cancellation-and-increasing-subequivalence) corner argument: if a central selfadjoint in eMe were nonscalar, positive parts and their supports give a nonzero proper central projection f<e. Factor corner contact in M gives fM(e−f)≠0, whereas centrality of f in eMe makes that corner zero. Thus the corner's center is scalar. The space eH is separable as a closed subspace of the separableH; projecting a countable dense set in H gives a countable dense set in eH.

[Sections 19.1–19.6](car-fock-and-quasifree-states.md#19-1-hahn-banach-and-the-concrete-coefficient-banach-space) now supplies a faithful concretely normal tracial state theta on eMe, with theta(e)=1. The proof of that exact finite-factor theorem is supplied separately, not imported from an unproved arbitrary-algebra trace-existence assertion. In particular theta is bounded, positive and ultraweakly continuous on the actual concrete space eH. No extension of theta to a trace on M is needed.

### 20.5. The two compressed tail products contradict traciality

Set Bj=eXje∈eMe. The full strong commutator limits in (CF3) with u=e imply
\[
 \begin{aligned}
 eN_je-B_j^*B_j&=eX_j^*(1-e)X_je\to0,\\
 eD_je-B_jB_j^*&=eX_j(1-e)X_j^*e\to0
 \end{aligned}\quad\hbox{strongly}.                          \tag{CF6}
\]
For the first limit the rightmost factor(1−e)Xje=(1−e)[Xj,e] tends strongly to zero, and the other factors are uniformly bounded contractions. The second has the identical justified estimate with Xj\*. For every vector xi, the first difference has norm at most ||(1-e)[Xj,e]xi||, since ||eXj\*||<=1; this tends to zero. The second difference is bounded identically by ||(1-e)[Xj\*,e]xi||. These are the full needed bounded-product strong-limit estimates; the underlying operator norm bound is supplied in [ITP Section 10.2](infinite-tensor-products.md#10-2-riesz-representation-adjoints-and-the-operator-c-identity). Therefore (CF5) gives
\[
 B_j^*B_j\to pe,\qquad B_jB_j^*\to(1-p)e\quad\hbox{in WOT}.    \tag{CF7}
\]
The operators in these limits belong to eMe and are uniformly bounded by one. Their restrictions converge in WOT on eH. Concrete coefficient normality of theta passes through that bounded limit: truncate its square-summable vector series, make the tail uniformly small by Cauchy–Schwarz, and pass the finite head through WOT convergence, as fully proved in [Sections 18.8–18.9](car-fock-and-quasifree-states.md#18-8-order-normality-complete-additivity-and-the-reverse-implication). Hence traciality and theta(e)=1 give
\[
 p=\lim_j\theta(B_j^*B_j)
   =\lim_j\theta(B_jB_j^*)=1-p.                              \tag{CF8}
\]
This contradicts p≠1/2. We have proved that0 is the only finite projection in M.

### 20.6. Exact equation(20), type naming and transport

Definition 7.1 in Projections and types of von Neumann algebras defines typeIII as having0 as its only finite projection, and semifinite as having no nonzero central summand of typeIII. By the just proved projection exclusion, the nonzero algebra M is typeIII. Its whole identity summand is a nonzero central summand of typeIII, so it is not semifinite, directly from these definitions. No central type decomposition, arbitrary trace/semifiniteness equivalence or extension theorem is consumed by that naming step.

The onto algebra conjugation W transports finite projections in both directions, since it transports every partial isometry, its initial/final projections and the order relation among projections. Thus Mp has no nonzero finite projection and is typeIII and not semifinite. This is the complete original equation(20) and the immediately following typeIII claim at their exact hypotheses. Its original scalar overlap computation has its separately supplied proof in [Section 17.7](car-fock-and-quasifree-states.md#17-7-equation-21-its-signed-generator-and-the-exact-conclusion); the general infinite-product semifiniteness criterion is not needed to prove this particular conclusion.

The excluded endpoints0,1 do not have the invertible density or uniform right bound used in [Section 20.2](car-fock-and-quasifree-states.md#20-2-the-whole-tail-commutator-limit). The half-state p=1/2 has no contradiction in (CF8) and is handled by its separate trace/typeII1 proof. Finite-dimensionalK has no arbitrarily far infinite tail and retains its matrix-factor conclusion. There is no claimed typeIII subtype, factorial centralizer, modular spectrum/core/center flow, general product semifiniteness criterion or whole-course prerequisite closure in this proof.

## References and continuation

Huzihiro Araki, [*On Quasifree States of CAR and Bogoliubov Automorphisms*](https://ems.press/content/serial-article-files/41673?nt=1), *Publ. RIMS* 6 (1970/71), 385–442, supplies the selfdual covariance and doubled-projection comparison in Sections 2–4, especially the complete selected proofs of Lemmas 3.2–3.3 and 4.5–4.8, and the full trace calculation of Lemma 6.1. The printed volume gives 1970/71; the publisher dates the issue 1970. Further comparisons are the factor Lemma 4.11, printed pp.393–395, and the Hilbert–Schmidt Lemmas 5.1–5.3, pp.395–396. That factor route uses a changed basis projection, an overlap/equivalence theorem later in the paper and an external projection lemma; these additional results are not premises of the factor proof in Section 5. Its Fock-state existence and purity discussion also cites prior work. Section 4 here instead constructs positivity from compatible finite occupation densities, while Section 5 supplies a gauge-center proof on the reduced doubled space for arbitrary \(K\).

Jan Dereziński, [*Introduction to representations of the canonical commutation and anticommutation relations*, arXiv:math-ph/0511030v2](https://arxiv.org/pdf/math-ph/0511030v2), version dated 9 November 2005, gives the finite parity-string comparison on PDF pp.16–17, the exterior/Fock comparison on pp.20–23, and the Araki–Wyss definitions, covariance and entire selected factor proof of Theorem 43 on pp.46–50. Its occupation covariance \(\chi\) has the orientation \(\langle z_2,\chi z_1\rangle\), matching \(\langle g,Tf\rangle\) here. The source's factor proof explicitly invokes a separable diagonal-perturbation exercise in Takesaki I, and its constant type III subtype assertion cites Takesaki II. Those are comparison boundaries, not substitute free proofs. Its finite representation theorem and several Fock identities are asserted with abbreviated proofs. This lesson supplies explicit matrix-unit norms, determinant contractions, cyclicity and completion arguments instead of inferring those whole proofs from the source's statements. No full commutant theorem or type classification is required for these arguments.

[Constant CAR states and the periodic core](constant-car-states-and-the-periodic-core.md) computes the factorial centralizer and center flow, keeping its subtype prerequisite explicit. Sections 9–12 supply the detailed local foundations for Fock space, finite-mode norms, simplicity, even-leg tensor products and arbitrary covariance. Sections 13–16 supply general factorality, every-representation approximation, the completed variable-eigenvalue product model and the half-state type-II1 proof. Sections 17–20 supply the exact constant-state inner-time and finite-corner type III arguments used in Section 6, with their concrete normality and finite-factor trace inputs. The factor, approximation and type conclusions use the hypotheses stated in their respective constructions. The finer type III parameter is treated in the continuation lesson.
