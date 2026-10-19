# Inductive limits and quasi-free factors



Finite matrix algebras fit together in two useful ways: by norm completion and by passage to the von Neumann algebra in a state representation. The CAR algebra makes both constructions explicit. We prove its representation independence and simplicity, construct every gauge-invariant quasi-free state, identify its completed GNS space and prove factoriality, including the nonfaithful endpoints. The final comparison retains the full type \(\mathrm{III}_\lambda\) conclusion for a constant covariance.

The source scope is Takesaki, *Theory of Operator Algebras III*, XIV.1, Definitions 1.1, 1.3 and 1.4, Example 1.2 and all six exercises, printed pages 82–84 and 91–94. The earlier programme proofs are Infinite tensor products, Section 1 and F05, F07, F10, Fermions, Fock space and quasi-free factors, Sections 1–6, 11 and 13, and the all-weight comparison in Constant CAR states and the periodic core, Section 6. Their named foundational inputs remain in force.

Inner products here are linear in the first variable. Creation \(c(f)\) is linear in \(f\), and annihilation \(a(f)=c(f)^*\) is conjugate-linear:

\[
 \{a(f),a(g)\}=0,\qquad
 \{a(f),a(g)^*\}=\langle g,f\rangle1 .
 \tag{CAR.1}
\]

We use the occupation covariance \(S\), specified by
\(\omega_S(a(f)^*a(g))=\langle Sf,g\rangle\).
The source instead calls the linear creation generator \(a(f)\) and uses a covariance \(T\) for the opposite order. The precise dictionary is

\[
 q(f)=a(f)^*,\qquad
 \gamma_T=\omega_{1-T},\qquad
 \gamma_T(q(g)^*q(f))=\langle Tf,g\rangle .
 \tag{CAR.2}
\]

We return to the resulting correction to its vacuum assertion in Section 8.

## Norms and kernels in an inductive sequence

Let \(A_n\) be \(C^*\)-algebras and \(\phi_n:A_n\to A_{n+1}\) star homomorphisms, without injectivity or unit assumptions. The sequence is unital when every algebra has a unit and every map preserves it; the compatible unit classes then give a unit in the completed limit. Write \(\phi_{m,n}\) for the composite from stage \(n\) to stage \(m\), and \(\phi_{n,n}=\mathrm{id}\). In the algebraic direct limit, \(a\in A_n\) and \(b\in A_k\) represent the same element when their images agree at some common later stage. Transitivity follows by moving two such equalities to one further stage. Addition, multiplication, scalar multiplication and adjoint are computed at a common stage; moving further preserves them, so they are independent of representatives.

The precise \(C^*\)-norm facts needed here are proved in the earlier F05, F07 and F10: star homomorphisms are contractive, injective ones are isometric, and

\[
 \|\phi(a)\|=\operatorname{dist}(a,\ker\phi).
 \tag{CAR.3}
\]

The last identity uses the \(C^*\)-quotient norm and injective isometry, not merely contractivity.

Contractivity makes \(\|\phi_{m,n}(a)\|\) decrease. Define on the algebraic limit

\[
 p([a])=\inf_{m\geq n}\|\phi_{m,n}(a)\|.
 \tag{CAR.4}
\]

Equivalent representatives have equal late images and hence equal infima. Computing two elements at a common stage and passing to the decreasing limits gives the triangle inequality, scalar homogeneity, submultiplicativity,
\(p(x^*)=p(x)\), and \(p(x^*x)=p(x)^2\).
Thus \(N=\{x:p(x)=0\}\) is a two-sided star ideal. Quotient by \(N\) and complete. Multiplication and adjoint extend continuously and preserve the \(C^*\)-identity, so the result \(A\) is a \(C^*\)-algebra, with compatible maps \(\iota_n\) and

\[
 \|\iota_n(a)\|=p([a]),\qquad
 A=\overline{\bigcup_n\iota_n(A_n)}^{\|\cdot\|}.
 \tag{CAR.5}
\]

If \(\psi_n:A_n\to B\) are compatible star homomorphisms, their common-stage map on the algebraic limit satisfies
\(\|\psi_n(a)\|\leq\|\phi_{m,n}(a)\|\) for every \(m\geq n\).
It therefore kills \(N\), is contractive for (CAR.4), and extends uniquely to \(A\). This proves the universal property, including the zero limit.

Put \(K_n=\bigcup_{m\geq n}\ker\phi_{m,n}\). The kernels increase, and (CAR.3) gives

\[
 p([a])=\inf_{m\geq n}\operatorname{dist}(a,\ker\phi_{m,n})
       =\operatorname{dist}(a,K_n).
 \tag{CAR.6}
\]

The algebraic stage kernel is \(K_n\), whereas the kernel of \(\iota_n\) is its norm closure. If \(K_n\) is closed for every sufficiently large \(n\), every algebraic class can be represented at such a stage, where zero limiting norm means eventual zero. Thus \(N=0\). This is exactly the source's properness condition. It permits direct completion of the algebraic limit; it is not needed for existence of the completed \(C^*\)-limit. If all connecting maps are injective, their isometry makes all \(\iota_n\) isometric.

For the source example \(A_n=C_0([n,\infty))\), let the maps be restrictions. The eventual kernel is \(C_c([n,\infty))\): eventual vanishing is precisely compact support. Continuous cutoffs show this is dense, but the function \(e^{-t}\) is not in it. Its algebraic germ is nonzero, while every germ has limiting norm zero, since every function vanishes at infinity. Thus the completed \(C^*\)-limit is zero. Any star representation of the algebraic germ algebra on a Hilbert space restricts to a contractive star homomorphism on every \(A_n\), so its norm on a germ is bounded by every tail supremum and is zero. This proves the source's representation assertion as well.

A morphism of sequences is a family \(\theta_n:A_n\to B_n\) intertwining the connecting maps. Composing with the \(B\)-limit maps and using the universal property gives a homomorphism of limits. If all \(\theta_n\) are isomorphisms, their inverses also intertwine, and the induced maps are inverse on the dense stage unions and hence everywhere. This proves the conjugacy assertion.

Finally, a sequential AF \(C^*\)-algebra is exactly a norm closure of an increasing sequence of finite-dimensional star subalgebras. One direction uses the finite-dimensional stage images in (CAR.5), which are closed; the other uses the inclusion sequence and its universal property. A finite-dimensional subspace is closed because its coordinate unit sphere is compact and its norm has a positive minimum there. Rational complex coordinates then give a countable dense subset at each stage, so every sequential AF algebra is separable. A directed finite-dimensional approximation without a countable cofinal sequence is a different assertion.

## Matrix units, parity strings and simplicity

Consider any family satisfying (CAR.1) on a nonzero representation Hilbert space. For a unit vector \(f\), put \(b=a(f)\), \(n=b^*b\). The CAR give

\[
 b^2=0,\quad bb^*=1-n,\quad n^2=n,\quad bn=b,\quad nb=0 .
 \tag{CAR.7}
\]

Neither \(n\) nor \(1-n\) is zero: either case, together with these identities, would force \(b=0\) and then \(1=0\). Hence \(\|b\|^2=\|n\|=1\), and scaling gives \(\|a(f)\|=\|f\|\). The four operators

\[
 e_{11}=1-n,\quad e_{12}=b,\quad e_{21}=b^*,\quad e_{22}=n
 \tag{CAR.8}
\]

are matrix units: (CAR.7) and its adjoint verify \(e_{ij}e_{kl}=\delta_{jk}e_{il}\), and their diagonal sum is one.

For orthonormal \(f_1,\ldots,f_d\), write \(a_j=a(f_j)\),
\(n_j=a_j^*a_j\), and \(Z_j=1-2n_j\). Two CAR interchanges show that \(n_i\) commutes with \(a_j,a_j^*\) for \(i\ne j\). Each \(Z_j\) is a selfadjoint unitary, anticommutes with its own \(a_j,a_j^*\), and commutes with the other modes. Thus the \(Z_j\) commute. Define

\[
 b_j=Z_1\cdots Z_{j-1}a_j .
 \tag{CAR.9}
\]

Each \(b_j\) gives (CAR.8). These matrix systems commute for distinct \(j\): moving an earlier field past a later one gives a CAR minus sign and a second minus sign from its own parity factor in the later string. The signs cancel. The diagonal projections commute as already shown.

Products of one matrix unit from each system give \(2^d\)-by-\(2^d\) matrix units \(E_{\alpha\beta}\) whose diagonals sum to one. For a fixed index \(o\), \(Q=E_{oo}H\ne0\); otherwise the matrix-unit relations would make all diagonal units zero. The map

\[
 \delta_\alpha\otimes\eta\longmapsto E_{\alpha o}\eta
 \quad(\eta\in Q)
 \tag{CAR.10}
\]

is unitary from \(\mathbb C^{2^d}\otimes Q\) onto the representation space. Its isometry and surjectivity follow from the matrix-unit products and the diagonal sum. It identifies each \(E_{\alpha\beta}\) with the usual matrix unit tensored with \(1_Q\). The norm of a scalar matrix is therefore unchanged, by testing on \(v\otimes\eta\) and expanding along a basis of \(Q\). Since (CAR.9) also recovers every original mode, the algebra of a \(d\)-dimensional one-particle subspace is exactly \(M_{2^d}\).

Any two nonzero CAR families consequently have compatible isometric maps on every finite-dimensional one-particle subspace, matching the generators. The maps agree on overlaps because they agree on polynomials in the same generators. They extend isometrically to the norm closures, which proves representation independence and the concrete universal property. Section 3 constructs one such family and hence the unital algebra \(\operatorname{CAR}(K)\). For \(K=0\), this means \(\mathbb C1\).

Here is simplicity without a classification theorem. If a closed two-sided ideal \(J\) contains \(x\ne0\), put \(r=\|x\|\) and choose a local matrix element \(y\) with \(\|x-y\|<r/16\). Then

\[
 \|x^*x-y^*y\|<r^2/4,\qquad
 t=\|y\|^2>3r^2/4.
\]

Choose a rank-one maximal-eigenvalue projection \(e\) of \(y^*y\) in that local matrix algebra. Then \(h=ex^*xe\in J\cap e\operatorname{CAR}(K)e\) and
\(\|h-te\|<t\).
The series \(t^{-1}\sum_{k\geq0}(e-h/t)^k\) is its inverse in the corner. Hence \(e\in J\). Conjugating \(e\) by local matrix partial isometries and summing gives \(1\in J\), so \(J\) is the whole algebra.

For a countable infinite orthonormal basis, (CAR.9) identifies the first \(d\) modes with \(M_2^{\otimes d}\), compatibly under \(x\mapsto x\otimes1\). Their union is dense: generator norm continuity and telescoping finite products reduce each polynomial to finite-support vectors. Thus

\[
 \operatorname{CAR}(K)\cong\bigotimes_{j=1}^{\infty}M_2
 \quad\text{if }\dim K=\infty\text{ and }K\text{ is separable}.
 \tag{CAR.11}
\]

For \(\dim K=d<\infty\), the algebra is \(M_{2^d}\). Infinite representation multiplicity does not change this distinction: one mode on \(\mathbb C^2\otimes\ell^2\) still generates only \(M_2\otimes1\). Thus the infinite-dimensional hypothesis in the source's Exercise 1(f) must concern the one-particle space, not merely its representation space.

## Exterior completion and the Fock vacuum

On \(K^{\otimes n}\), use the left permutation representation

\[
 U_\sigma(f_1\otimes\cdots\otimes f_n)
 =f_{\sigma^{-1}(1)}\otimes\cdots\otimes f_{\sigma^{-1}(n)},\qquad
 A_n=\frac1{n!}\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)U_\sigma .
 \tag{CAR.12}
\]

The inverse indices make \(U_\sigma U_\tau=U_{\sigma\tau}\) under the usual composition convention. Replacing every permutation by its inverse leaves the sum \(A_n\) unchanged, so this also resolves the convention in the source's permutation formula. Since \(U_\sigma^*=U_{\sigma^{-1}}\), the average is selfadjoint. In its square each resulting permutation occurs \(n!\) times with its sign; hence \(A_n^2=A_n\).

Put \(\Lambda^nK=A_nK^{\otimes n}\), \(\Lambda^0K=\mathbb C\), and

\[
 [f_1,\ldots,f_n]=\sqrt{n!}\,A_n(f_1\otimes\cdots\otimes f_n).
\]

For an ordered orthonormal basis, the increasing occupation wedges form an orthonormal basis of \(\Lambda^nK\). Different increasing tuples have disjoint permutation orbits, and repeated entries antisymmetrize to zero. Applying \(A_n\) to the tensor basis proves completeness. Expansion of the same average gives

\[
 \langle[f_1,\ldots,f_n],[g_1,\ldots,g_n]\rangle
       =\det[\langle f_i,g_j\rangle].
 \tag{CAR.13}
\]

Thus in dimension \(d\), the \(n\)-particle dimension is \(\binom dn\), with value zero for \(n>d\), and the full exterior dimension is \(2^d\).

The Hilbert direct sum \(\mathcal F(K)=\bigoplus_{n\geq0}\Lambda^nK\) is Fock space, with vacuum \(\Omega=1\). On its algebraic finite-degree sum, the unscaled product
\(\eta\wedge\zeta=A_{p+q}(\eta\otimes\zeta)\) for homogeneous degrees \(p,q\) is associative. Full antisymmetrization absorbs a preceding antisymmetrization on any consecutive block, so both parenthesizations of a triple product equal its full antisymmetrization. This is an algebraic product; no bounded multiplication on the entire Hilbert direct sum is asserted.

Define creation on a vector of degree \(n\) by

\[
 c(f)\eta=\sqrt{n+1}\,A_{n+1}(f\otimes\eta).
 \tag{CAR.14}
\]

It sends \([g_1,\ldots,g_n]\) to \([f,g_1,\ldots,g_n]\). For unit \(f\), choose an orthonormal basis beginning with \(f\). Creation carries occupation vectors not containing \(f\) isometrically, up to sign, to those containing \(f\), and annihilates the other basis vectors. It therefore extends boundedly to Fock space with norm one. Scaling gives \(\|c(f)\|=\|f\|\), including \(f=0\).

Expanding (CAR.13) along the first row verifies its adjoint:

\[
 a(f)[g_1,\ldots,g_n]
  =\sum_{j=1}^n(-1)^{j-1}\langle g_j,f\rangle
       [g_1,\ldots,\widehat{g_j},\ldots,g_n],
 \qquad a(f)\Omega=0 .
 \tag{CAR.15}
\]

Alternation gives two-creation anticommutation. The displayed contraction gives
\(a(f)c(g)+c(g)a(f)=\langle g,f\rangle1\).
Adjoints give the other CAR; boundedness extends them from the occupation span to the whole space. This constructs the nonzero family needed in Section 2.

The Fock family is irreducible. A vector killed by every \(a(f)\) is a multiple of the vacuum: any nonzero coefficient at a nonempty occupation set survives a suitable contraction. If an operator \(x\) commutes with all creators and annihilators, then \(x\Omega\) is such a vector, hence equals \(\lambda\Omega\). Products of creators applied to \(\Omega\) span a dense subspace, so commutation makes \(x=\lambda1\) everywhere.

## Bogoliubov actions and the even tensor legs

For a unitary \(u\) on \(K\), the family \(a(uf)\) satisfies (CAR.1). Representation independence gives an automorphism

\[
 \alpha_u(a(f))=a(uf),\qquad
 \alpha_u\alpha_v=\alpha_{uv},\qquad
 \alpha_u^{-1}=\alpha_{u^{-1}} .
 \tag{CAR.16}
\]

If \(u_i\to u\) strongly, then generator norms give
\(\|\alpha_{u_i}(a(f))-\alpha_u(a(f))\|=\|(u_i-u)f\|\to0\).
Telescoping proves convergence on polynomials, and density together with the automorphisms' unit norm proves point-norm convergence everywhere. In particular the source's strong* continuity holds.

Let \(\gamma=\alpha_{-1}\). The bounded maps \((\mathrm{id}\pm\gamma)/2\) split the algebra into even and odd parts. Polynomials of the corresponding total degree parity are dense there. If \(L\perp N\), every field from one subspace anticommutes with every field or adjoint field from the other. Moving homogeneous words past each other gives

\[
 xy=(-1)^{rs}yx,\qquad
 x\in\operatorname{CAR}(L)_r,\quad y\in\operatorname{CAR}(N)_s .
 \tag{CAR.17}
\]

Norm approximation extends the identity to the closed parity subspaces.

Commutation alone does not prove the desired tensor identification; injectivity matters. Take finite-dimensional \(E\subset L,F\subset N\), and order the \(E\)-modes first in (CAR.9). A second-leg generator becomes \(P_E\otimes a_F(f)\), with \(P_E\) the first-leg parity product. Every even second-leg word loses its parity strings and is \(1\otimes y\); first-leg words are \(x\otimes1\). If \(f=\dim F>0\), even and odd occupation spaces each have dimension \(2^{f-1}\), and

\[
 \operatorname{CAR}(F)_{\mathrm{ev}}
       =M_{2^{f-1}}\oplus M_{2^{f-1}}.
 \tag{CAR.18}
\]

The equality follows because the full finite CAR algebra is every matrix, while commuting with parity means preserving its two eigenspaces. Any faithful representation contains both nonzero central blocks. The matrix-unit unitary (CAR.10) shows that multiplicities do not change their matrix norms. Thus the spatial norm of a finite sum \(z=\sum x_j\otimes y_j\) is exactly the maximum of its two finite matrix block norms, which is also the norm of \(\sum x_jy_j\) in the parity-string model. If \(F=0\), the second leg is scalar and the same conclusion holds.

Local even elements are dense in the even algebra by applying \((\mathrm{id}+\gamma)/2\) to polynomial approximants. Approximating both factors of finite tensor sums proves that the preceding compatible isometries extend to

\[
 \begin{split}
 C^*(\operatorname{CAR}(L),\operatorname{CAR}(N)_{\mathrm{ev}})
   &\cong\operatorname{CAR}(L)\otimes_{\min}\operatorname{CAR}(N)_{\mathrm{ev}},\\
 C^*(\operatorname{CAR}(L)_{\mathrm{ev}},\operatorname{CAR}(N))
   &\cong\operatorname{CAR}(L)_{\mathrm{ev}}\otimes_{\min}\operatorname{CAR}(N).
 \end{split}
 \tag{CAR.19}
\]

The ranges contain the two legs and their polynomial products, so the maps are onto. Reversing the ordering of the legs proves the second formula.

Normal ordering uses
\(a(g)a(f)^*=\langle f,g\rangle1-a(f)^*a(g)\).
Each replacement either removes two letters or reduces the number of annihilator-before-creator inversions. Induction on these two nonnegative integers gives a span by

\[
 a(f_1)^*\cdots a(f_n)^*a(g_m)\cdots a(g_1),\qquad n,m\geq0 .
 \tag{CAR.20}
\]

This is a dense star subalgebra, with the identity as its empty word. Both zero lengths are necessary; positive lengths alone would omit even the identity and the odd generators in the one-mode algebra. In particular a bounded functional is determined by its normal moments.

## Every covariance and its completed GNS model

Let \(0\leq S\leq1\) on \(K\). For every finite-dimensional subspace \(E\), the compression \(S_E=P_ES|_E\) is a positive contraction. Diagonalize it in an orthonormal basis, with eigenvalues \(p_1,\ldots,p_d\), and use the matrix units of Section 2. On the corresponding occupation matrix algebra put

\[
 \rho_E=\bigotimes_{j=1}^d
       \begin{pmatrix}1-p_j&0\\0&p_j\end{pmatrix}.
 \tag{CAR.21}
\]

This is a positive trace-one matrix, also when some \(p_j\) equals zero or one.

A normal word with repeated creation or annihilation basis indices vanishes. A word with different creation and annihilation index sets changes the occupation set and has zero diagonal expectation. With equal index sets, ordering both lists contributes their two permutation signs; the resulting word is the product of the corresponding number projections, with expectation \(\prod p_j\). These are precisely the signs and products of the determinant. Sesquilinear expansion gives

\[
 \omega_S\!\left(a(f_1)^*\cdots a(f_n)^*
                         a(g_m)\cdots a(g_1)\right)
 =\begin{cases}
   \det[\langle Sf_j,g_i\rangle]_{i,j=1}^n,&m=n,\\
   0,&m\ne n.
  \end{cases}
 \tag{CAR.22}
\]

The empty determinant is one. Since the entries are \(\langle S_Ef_j,g_i\rangle=\langle Sf_j,g_i\rangle\), (CAR.20) makes the finite state independent of its diagonalizing basis and compatible under \(E\subset F\). Any finite list of subspaces lies in their finite sum. These finite states therefore define a positive norm-one functional on the local union and extend by norm continuity to the full CAR algebra. Positivity passes to limits of local \(x^*x\). Equation (CAR.20) proves uniqueness. This constructs the state without assuming a global eigenbasis of \(S\), or that \(E\) reduces it.

We next construct its whole cyclic representation. Set

\[
 A=(1-S)^{1/2},\quad B=S^{1/2},\quad
 K_0=\overline{AK},\quad K_1=\overline{BK},\quad
 \mathcal L=K_0\oplus\overline{K_1}.
\]

The bounded positive functional calculus gives commuting roots, with \(A^2+B^2=1\). The earlier arbitrary-covariance proof, Section 11.1, also constructs these roots by norm-convergent series. On the Fock space of \(\mathcal L\), put

\[
 d(f)=a_{\mathcal L}(Af\oplus0)
           +c_{\mathcal L}(0\oplus\overline{Bf}).
 \tag{CAR.23}
\]

The conjugate-space inner product is
\(\langle\bar v,\bar w\rangle=\langle w,v\rangle\).
Orthogonality of the two legs and (CAR.1) give
\(\{d(f),d(g)\}=0\) and
\(\{d(f),d(g)^*\}=\langle g,(A^2+B^2)f\rangle1=\langle g,f\rangle1\).
Thus Section 2 extends the field assignment to a representation \(\pi_S\).

Its vacuum state has (CAR.22). To verify the determinant directly, expand the leftmost adjoint \(d(f_1)^*\). Its creator term has zero expectation against the left vacuum. Move its remaining annihilator \(a_{\mathcal L}(0\oplus\overline{Bf_1})\) to the right. It has zero scalar contractions with the other adjoints and scalar contraction \(\langle Sf_1,g_i\rangle\) with \(d(g_i)\). At equal lengths \(n\), its sign is
\((-1)^{n-1+n-i}=(-1)^{i+1}\), the first-column cofactor sign. The term reaching the right vacuum vanishes. Induction proves the determinant. At unequal lengths the same recurrence reduces both lengths until a nonempty pure product remains, whose expectation is zero by the orthogonality of the two legs. Hence all moments agree with the positive state already constructed.

The vacuum is cyclic on this reduced doubled space. The creation parts of \(d(f)^*\Omega\) and \(d(f)\Omega\) are \(Af\oplus0\) and \(0\oplus\overline{Bf}\), whose span is dense in \(\mathcal L\). A product of chosen fields with those creation parts gives the desired wedge plus terms of smaller particle degree. Induction, subtraction of those lower-degree terms, and density of product wedges put every particle sector in the closed cyclic subspace. Finite-degree vectors are dense in Fock space. Thus the entire space is cyclic, without inverting either root.

Consequently

\[
 [x]\longmapsto\pi_S(x)\Omega
 \tag{CAR.24}
\]

extends to an onto GNS unitary: its squared norm is \(\omega_S(x^*x)\), it kills exactly the null ideal, preserves inner products and intertwines multiplication. At \(S=0\) the second active leg is absent; at \(S=1\) the first is absent. No assertion of endpoint cyclicity on the larger unreduced doubled space is being made.

On \(\mathcal L\), let \(V_\theta=e^{i\theta}1_{K_0}\oplus e^{-i\theta}1_{\overline{K_1}}\). Its exterior tensor powers give a unitary \(U_\theta\) fixing the vacuum and satisfying

\[
 U_\theta d(f)U_\theta^*=e^{-i\theta}d(f).
 \tag{CAR.25}
\]

The creator formula proves this first on wedges and then by boundedness. This implements the gauge automorphism on the whole represented algebra and proves that \(\omega_S\) is gauge invariant, hence even.

## Factoriality without diagonalizing the covariance

We prove that \(M_S=\pi_S(\operatorname{CAR}(K))''\) is a factor for every \(S\), including all endpoints. Split

\[
 K=H_0\oplus H_m\oplus H_1,\qquad
 H_0=\ker S,\quad H_1=\ker(1-S),\quad
 H_m=(H_0\oplus H_1)^\perp .
\]

The endpoint spaces are orthogonal and reduce \(S,A,B\). On \(H_0\), \(A=1,B=0\); on \(H_1\), \(A=0,B=1\).
The range-kernel identity for selfadjoint operators gives
\(K_0=H_0\oplus H_m\), \(K_1=H_m\oplus H_1\).

For \(f\in H_m\) the complementary field

\[
 b(f)=a_{\mathcal L}(Bf\oplus0)
                -c_{\mathcal L}(0\oplus\overline{Af})
 \tag{CAR.26}
\]

is defined on the same active legs. It anticommutes with every \(d(g)\) and \(d(g)^*\). The same-type and cross-leg scalar contractions are zero; the two remaining terms cancel because \(AB=BA\). Taking adjoints verifies all four anticommutators.

Let \(P\) be Fock parity, equal to \((-1)^n\) on particle degree \(n\). It anticommutes with every ordinary field and hence with \(d,d^*,b,b^*\). Therefore \(Pb(f)\) and its adjoint commute with every represented CAR generator and belong to \(M_S'\).

The untwisted fields together generate an irreducible family. On \(H_m\),

\[
 \begin{split}
 d(Af)+b(Bf)&=a_{\mathcal L}(f\oplus0),\\
 d(Bf)-b(Af)&=c_{\mathcal L}(0\oplus\bar f).
 \end{split}
 \tag{CAR.27}
\]

These follow by \(A^2+B^2=1\) and cancellation of \(AB-BA\); no bounded inverses are involved. On \(H_0\) the first-leg field is already \(d(f)\), and on \(H_1\) the second-leg creator is already \(d(f)\). Adjoints and linear combinations give all ordinary Fock fields. Their irreducibility was proved in Section 3.

Parity preserves \(M_S\) and its centre. If a central \(x\) is even, it commutes with \(P\). Since \(x\in M_S\), it also commutes with every \(Pb(f)\) and its adjoint. Therefore it commutes with \(b,b^*\); centrality gives commutation with \(d,d^*\). Equation (CAR.27) makes \(x\) scalar.

If the odd centre were nonzero, its real or imaginary part would contain a nonzero selfadjoint odd \(z_0\). Its square is even central, hence \(z_0^2=c1\), with \(c=\|z_0\|^2>0\). Normalize to \(z=z^*\), \(z^2=1\). For every odd central \(w\), \(zw\) is even central and scalar, so \(w\in\mathbb Cz\). Thus the entire centre would be \(\mathbb C1+\mathbb Cz\).

The group (CAR.25) is strongly continuous on the full Fock space. On a finite occupation vector with \(r\) first-leg and \(s\) second-leg entries it is multiplication by \(e^{i(r-s)\theta}\). Continuity follows first on finite spans and then on the completion by unitary boundedness. The adjoint group is also strongly continuous, so conjugation of each bounded operator is strongly continuous. It preserves \(M_S\), its centre and parity, and must send \(z\) to \(\varepsilon(\theta)z\), with \(\varepsilon(\theta)\in\{1,-1\}\). Continuity at zero forces the sign to be \(1\) near zero: the other sign changes \(z\xi\) by norm \(2\|\xi\|\). Subdivide any real parameter into sufficiently small pieces and use the group law to obtain sign \(1\) everywhere. But \(U_\pi=P\), which sends the odd \(z\) to \(-z\). This contradiction eliminates the odd centre. Hence

\[
 Z(M_S)=\mathbb C1 .
 \tag{CAR.28}
\]

The proof uses only inclusion of the twisted fields in the commutant; it does not claim that they generate the whole commutant.

## Bounded finite-mode approximation and product states

For any representation \(\pi\), possibly degenerate, put \(e=\pi(1)\) and

\[
 D_E=\pi(\operatorname{CAR}(E))+\mathbb C(1-e)
 \quad(\dim E<\infty).
\]

On the active subspace \(eH\) the first summand is a full finite matrix algebra when \(e\ne0\), by simplicity and Section 2; the inactive block is scalar. Thus each \(D_E\) is a finite-dimensional unital von Neumann algebra. They increase with \(E\). Their union \(D_0\) has the same commutant as the represented CAR algebra: polynomials are locally contained and norm dense, and adjoining \(1-e\) adds no condition to a commutant already commuting with \(e\).

For completeness we retain bounded strong* density, rather than just algebraic generation. The earlier concrete bicommutant proof, Section 10.5, makes \(D_0\) weak-operator dense in \(D_0''\). For a finite list of vectors, the tuples \((x\xi_j,x^*\xi_j)_j\), \(x\in D_0\), form a real linear subspace of a finite Hilbert sum. If a target tuple from \(z\in D_0''\) were outside its norm closure, orthogonal projection would give a separating real functional. This functional is a finite sum of weak-operator coefficients of \(x,x^*\), contradicting weak density. Thus there is a local net tending strongly* to \(z\), initially without a common norm bound.

Use the bounded rational map

\[
 F(x)=2x(1+x^*x)^{-1}.
\]

The inverse stays in the same complete local algebra. Direct multiplication gives

\[
 1-F(x)^*F(x)
  =(1+x^*x)^{-1}(1-x^*x)^2(1+x^*x)^{-1}\geq0,
\]

so \(F(x)\) is a contraction. For \(R_z=(1+z^*z)^{-1}\), the resolvent identity gives

\[
 \frac12(F(x)-F(z))
  =(1+xx^*)^{-1}(x-z)R_z
       +x(1+x^*x)^{-1}(z^*-x^*)zR_z .
 \tag{CAR.29}
\]

The two left coefficients have norms at most \(1\) and \(1/2\). Consequently this expression tends strongly to zero if \(x\to z\) strongly*, without requiring a norm bound on that net. The same holds for adjoints, using \(F(x)^*=F(x^*)\).

For a contraction \(y\in D_0''\), put
\(G(y)=y(1+\sqrt{1-y^*y})^{-1}\).
Commuting multiplication verifies \(F(G(y))=y\): if \(s=\sqrt{1-y^*y}\), then \(1+G(y)^*G(y)=2(1+s)^{-1}\). Approximate \(G(y)\) by the preceding local strong* net and apply \(F\). This gives local contractions converging strongly* to \(y\). Scaling proves density with each exact norm bound.

If \(K\) is separable, take the first \(n\) vectors of an orthonormal basis, with the finite and zero-dimensional cases understood. Generator norm continuity makes their local union norm dense, so the resulting sequence \(D_{E_n}\) generates the full bicommutant and has the bounded approximation just proved. This is sequential AFD. The approximating elements may still require nets in a nonseparable representation space. For arbitrary \(K\), all finite subspaces give the directed version. Combined with (CAR.28), every quasi-free GNS algebra is an AFD factor at the source's separable one-particle scope.

Suppose \(K=\bigoplus_jK_j\) and \(S\) reduces each \(K_j\). Then

\[
 \omega_S(x_1\cdots x_r)=\prod_{\ell=1}^r\omega_S(x_\ell),
 \qquad
 x_\ell\in\operatorname{CAR}(K_{j_\ell}),\quad j_\ell\text{ distinct}.
 \tag{CAR.30}
\]

For normal local words, all cross-block contractions in (CAR.22) are zero. A surviving term must be balanced in every block. Those blocks are even, so regrouping them introduces no sign, and the determinant splits into the block determinants. If some block is unbalanced, both sides vanish. Linearity and norm density prove (CAR.30) for all local elements. This proves joint finite-block factorization, which is stronger than the source's pairwise formulation.

If \(S\) has a countable orthonormal eigenbasis with eigenvalues \(p_j\), the compatible finite matrix identifications give

\[
 (M_S,\omega_S)\cong
 \bigotimes_j\left(M_2,\operatorname{Tr}(\rho_j\,\cdot)\right),
 \qquad \rho_j=\operatorname{diag}(1-p_j,p_j).
 \tag{CAR.31}
\]

To justify the completion, let \(s_j=s(\rho_j)\),
\(H_j=M_2s_j\) with \(\langle X,Y\rangle=\operatorname{Tr}(Y^*X)\), and reference vector \(\rho_j^{1/2}\). Left multiplication is cyclic, by inversion only on the positive diagonal entries; this includes rank-one endpoint densities. On finite products,
\(\langle x\Omega,y\Omega\rangle=\omega_S(y^*x)\)
by (CAR.21). Therefore matching local GNS vectors is an isometry with dense range in the pointed completion and extends onto it. It intertwines the complete norm-closed CAR algebra, and unitary conjugation gives the claimed normal isomorphism of the generated von Neumann algebras, with normal inverse. A spectral decomposition into reducing blocks gives (CAR.30) even if the individual blocks are not one-dimensional; no global eigenbasis is assumed in the general state or factor proofs.

## Trace, subtype and the source conventions

If \(S=\frac12 1\), every finite restriction is normalized matrix trace. The matrix-unit identities show that this trace is unique: diagonal values agree, their sum is one, and off-diagonal values vanish. Norm density makes \(\omega_{1/2}\) the unique CAR tracial state. Equation (CAR.31), including its completed GNS unitary, identifies its von Neumann algebra with the normalized trace product. For separable infinite-dimensional \(K\), State supports, full corners and traces proves that this is a type \(\mathrm{II}_1\) factor.

For \(S=p1\), \(0<p<1\), \(p\ne1/2\), put

\[
 \lambda=\frac{\min(p,1-p)}{\max(p,1-p)}.
 \tag{CAR.32}
\]

The product density in (CAR.31) is \(\operatorname{diag}(1-p,p)\). If \(p>1/2\), this equals
\(h_\lambda=(1+\lambda)^{-1}\operatorname{diag}(\lambda,1)\).
If \(p<1/2\), the fixed two-by-two flip conjugates it to \(h_\lambda\). In the latter case, conjugation of each Hilbert–Schmidt leg sends its reference square root to the new square root, so its pointed product is an onto unitary. Thus in both cases (CAR.31) gives the specific Powers product \(R_\lambda\), with its state and its complete representation.

The earlier 2. The specified Powers product proof, through the all-weight proof in periodic CAR Section 6, establishes

\[
 S(R_\lambda)=
 \bigcap_{\psi\ {\rm faithful\ normal\ semifinite}}
       \operatorname{Sp}(\Delta_\psi)
       =\{0\}\cup\lambda^{\mathbb Z}.
 \tag{CAR.33}
\]

That proof gives the upper inclusion by the full coefficient-domain spectrum of the product modular operator. For the lower inclusion it proves that every integer modular degree survives in every nonzero fixed corner and compares those spectra with every faithful normal semifinite weight using balanced weights and closed GNS graphs. Its quantifier includes weights of infinite total mass. We use this proved result, not an inference from the period of one chosen state.

Normal isomorphism preserves (CAR.33). Indeed weights correspond by composition with the isomorphism; the map matching their finite-ideal GNS vectors is an onto isometry, carries the initial Tomita maps and their adjoints to one another, and hence carries their closed modular operators with their full domains. Thus the spectra agree weight by weight and so do their intersections. It follows that the separable infinite product in (CAR.31) is type \(\mathrm{III}_\lambda\).

For an explicit domain check, in the constant faithful Hilbert–Schmidt product use in each leg the reference vector, its orthogonal diagonal vector, \(e_{12}\) and \(e_{21}\). Their finite-excitation tensors form an orthonormal basis \((\xi_\kappa)\). If \(m_\kappa=\#e_{12}-\#e_{21}\) and \(r=(1-p)/p\), the product modular operator has eigenvalues \(r^{m_\kappa}\), and Faithful states and maximal modular domains gives

\[
 D(\Delta^z)=
 \left\{\sum_\kappa t_\kappa\xi_\kappa:
       \sum_\kappa r^{2\operatorname{Re}(z)m_\kappa}|t_\kappa|^2<\infty\right\}.
 \tag{CAR.34}
\]

Finite excitation vectors are graph cores, but usually are not the whole domain. The modular action period is \(2\pi/|\log\lambda|\). The subtype in (CAR.33) uses the all-weight invariant; it is not obtained by exponentiating the negative of that action period.

We finish the dictionary with the printed exercises. The source's linear generator is \(q(f)=a(f)^*\), and its balanced moments are

\[
 \gamma_T\!\left(q(g_m)^*\cdots q(g_1)^*
                         q(f_1)\cdots q(f_n)\right)
   =\delta_{mn}\det[\langle Tf_i,g_j\rangle]_{i,j=1}^n .
 \tag{CAR.35}
\]

Moving annihilators past creators using (CAR.1), or repeating the cofactor recurrence of Section 5 in the opposite order, proves (CAR.35) for \(\gamma_T=\omega_{1-T}\). Unequal lengths vanish by gauge invariance. This also proves existence, positivity, uniqueness and evenness at the source's exact moment convention.

In the Fock construction (CAR.14), \(q(f)\Omega=f\), so for every unit \(f\),

\[
 \langle q(f)^*q(f)\Omega,\Omega\rangle=1.
 \tag{CAR.36}
\]

Consequently its vacuum has source covariance \(T=1\). The source's Exercise 4(c), which says \(T=0\) while retaining that creation formula and moment order, is false as printed. The familiar statement that the vacuum has covariance zero is correct for our annihilation occupation covariance \(S=0\), not for that \(T\). At \(S=1\) one obtains the filled Fock model. Both endpoint models are irreducible by Section 3, after using the appropriate active leg.

For source \(T=\mu1\), \(0<\mu<1/2\), the dictionary gives \(S=(1-\mu)1\), so (CAR.32) yields exactly \(\lambda=\mu/(1-\mu)\). This proves Exercise 5(f) with its requested parameter. For finite-dimensional \(K\), every state GNS algebra is instead the finite matrix factor \(M_{2^{\dim K}}\), by representation independence and simplicity; neither an infinite type \(\mathrm{II}_1\) conclusion nor a type \(\mathrm{III}_\lambda\) conclusion applies. For \(K=0\) it is \(\mathbb C\). All these cases remain AFD factors, as required by Exercise 6.
