<span id="tensor-operators-their-full-domains-and-tensor-weights"></span>
# Tensor operators, their full domains, and tensor weights

<span id="oa-mod-tg-01--positive-tensors-and-a-graph-core"></span>
<span id="OA-MOD-TG-01"></span>
<span id="oa-mod-tg-01"></span>
## OA-MOD-TG-01 — Positive tensors and a graph core

Let \(A_i\geq0\) be positive self-adjoint operators on \(H_i\), \(i=1,2\). The initial operator on \(D(A_1)\odot D(A_2)\) sends \(\xi\otimes\eta\) to \(A_1\xi\otimes A_2\eta\). We construct its positive self-adjoint closure without a separability assumption or an implicit product-measure theorem.

Set \(R_i=(1+A_i)^{-1}\), and on \(H=H_1\otimes H_2\) set \(R=R_1\otimes I\), \(Q=I\otimes R_2\). These bounded positive contractions commute, so \(Z=R+iQ\) is normal. Use its spectral measure \(E\) from SK-04. Its real and imaginary coordinate functions give \(R\) and \(Q\). Both lifts are injective: expand a vector along any orthonormal basis of the other factor; if the lifted operator annihilates that vector, it annihilates every coordinate. Each vector has only countably many nonzero coordinates even for an uncountable basis. Thus the coordinate axes \(r=0\) and \(q=0\) have zero spectral projection.

On the remaining spectral set put \(a(r)=r^{-1}-1\), \(b(q)=q^{-1}-1\). Give these functions any finite value on the null axes. SK-05 defines the positive self-adjoint operator
\[
C=(ab)(E),\qquad
D(C)=\left\{\zeta\in H:\int a(r)^2b(q)^2\,d\langle E(r,q)\zeta,\zeta\rangle<\infty\right\}.
\tag{TG.1}
\]
Here and below the integral uses the finite positive spectral measure of the particular vector. No common countable decomposition of \(H\) is needed.

Write
\[
P_n=1_{[0,n]}(A_1),\quad Q_n=1_{[0,n]}(A_2),\quad
E_n=P_n\otimes Q_n.
\tag{TG.2}
\]
Coordinate spectral projections for \(Z\) equal the corresponding lifts of those for \(R_i\): this follows first for polynomials, then for continuous functions, and then for bounded Borel functions by spectral bounded convergence. Products give the rectangular projection in (TG.2). On \(E_nH\), coordinate inversion is bounded and gives
\[
C|_{E_nH}=(A_1P_n)\otimes(A_2Q_n)|_{E_nH},\qquad
\|C|_{E_nH}\|\leq n^2.
\tag{TG.3}
\]
The projections increase strongly to \(I\), commute with \(C\), and for every \(\zeta\in D(C)\) satisfy
\[
E_n\zeta\longrightarrow\zeta,\qquad CE_n\zeta\longrightarrow C\zeta.
\tag{TG.4}
\]
The second convergence follows by applying monotone convergence to the integrable function in (TG.1) on the complements of the rectangles.

Finite sums from \(P_nH_1\odot Q_nH_2\) are Hilbert dense in \(E_nH\). The bound (TG.3) makes this approximation also a graph approximation. Combining it with (TG.4) proves that \(D(A_1)\odot D(A_2)\) is a graph core for \(C\). To check agreement on every elementary vector in that larger algebraic domain, truncate both factors. Their tensor vectors and tensor images converge in norm; closedness of \(C\) identifies the limit. Consequently
\[
A_1\otimes A_2:=C
=\overline{A_1\odot A_2}.
\tag{TG.5}
\]

The same calculus gives its support and its square:
\[
s(C)=s(A_1)\otimes s(A_2),\qquad
C^2=\overline{A_1^2\odot A_2^2}.
\tag{TG.6}
\]
Indeed the product vanishes precisely where one coordinate eigenvalue is zero; the kernel is the closed sum of \(\ker A_1\otimes H_2\) and \(H_1\otimes\ker A_2\). For the square, use \(a^2b^2\) and the same rectangles, now bounded by \(n^4\); its domain is the integral condition with \(a^4b^4\). If both factors are injective, the bounded functions \((ab)^{it}=a^{it}b^{it}\) on the nonzero spectral set similarly give
\[
(A_1\otimes A_2)^{it}=A_1^{it}\otimes A_2^{it},\qquad t\in\mathbb R.
\tag{TG.7}
\]
To justify the factorization, first work on rectangles bounded away from both zero and infinity, where continuous functional calculus applies, and then exhaust their spectral supports. All imaginary powers are unitary in this injective case. Kernels require support projections rather than an arbitrary convention for \(0^{it}\).

The domain (TG.1) can be strictly larger than the intersection of the two separate lifted domains. TG-06 calculates an explicit example. Even the entire Hilbert space can be the domain when one factor is zero.

<span id="oa-mod-tg-02--closed-tensors-adjoints-and-polar-supports"></span>
<span id="OA-MOD-TG-02"></span>
<span id="oa-mod-tg-02"></span>
## OA-MOD-TG-02 — Closed tensors, adjoints, and polar supports

Let \(T_i\) be densely defined closed linear operators on \(H_i\). Use QF-03 on the closed forms \(\|T_i\xi\|^2\) to obtain \(A_i=|T_i|\), with \(D(A_i)=D(T_i)\). The map \(A_i\xi\mapsto T_i\xi\) is isometric and extends by zero on \(\ker A_i\) to a partial isometry \(V_i\). Thus \(T_i=V_iA_i\) on the full domain. Set \(C=A_1\otimes A_2\), \(V=V_1\otimes V_2\), and \(p=s(A_1)\otimes s(A_2)\). By (TG.6), \(p=s(C)=V^*V\). Therefore
\[
T=VC,\qquad D(T)=D(C),\qquad \|T\zeta\|=\|C\zeta\|.
\tag{TG.8}
\]
This is closed: convergence of \(\zeta_j\) and \(T\zeta_j\) implies convergence of \(C\zeta_j=V^*T\zeta_j\), and then closedness of \(C\) applies. The graph-core proof of TG-01 and the norm equality prove
\[
T_1\otimes T_2:=\overline{T_1\odot T_2}=VC.
\tag{TG.9}
\]
Its complete adjoint domain is
\[
T^*=CV^*,\qquad D(T^*)=\{\eta\in H:V^*\eta\in D(C)\}.
\tag{TG.10}
\]
This follows directly from the definition of the adjoint and self-adjointness of \(C\). In particular every vector in \(\ker V^*\) belongs to this domain, irrespective of whether it lies in \(D(C)\).

We prove equality with the tensor of the two adjoints, rather than only an inclusion of cores. Put \(q_i=V_iV_i^*\). On \(q_iH_i\), let \(B_i\) be the unitary transport of \(A_i|_{s(A_i)H_i}\) by \(V_i\); put it equal to zero on \((1-q_i)H_i\). This is a positive self-adjoint operator, with
\[
D(B_i)=\{\eta:V_i^*\eta\in D(A_i)\},\qquad
T_i^*=A_iV_i^*=V_i^*B_i.
\tag{TG.11}
\]
The formula for \(T_i^*\) is the one-factor adjoint argument of (TG.10). The displayed factorization has the correct polar support, since \(s(B_i)=q_i\).

Let \(B=B_1\otimes B_2\). Its support is \(q=q_1\otimes q_2=VV^*\). Spectral transport on this support identifies \(B\) with \(VCV^*\), while on \((1-q)H\) it is zero. Hence
\[
D(B)=\{\eta:V^*\eta\in D(C)\},\qquad V^*B=CV^*.
\tag{TG.12}
\]
Applying (TG.9) to the polar factorizations in (TG.11) now proves the full assertion
\[
(T_1\otimes T_2)^*
=\overline{T_1^*\odot T_2^*}=T_1^*\otimes T_2^*.
\tag{TG.13}
\]
This is Lemma VIII.4.1 at its densely defined closed-operator scope. It includes noninjective operators and zero factors.

For the antilinear operators used next, suppose \(S_i=J_iD_i\), with \(J_i\) antiunitary conjugations and \(D_i\) positive injective self-adjoint operators. The elementary prescription \(J(\xi\otimes\eta)=J_1\xi\otimes J_2\eta\) is well defined and antilinear: moving a scalar between factors conjugates it in either position. Tensor inner products show that it extends to an antiunitary conjugation. The operator
\[
S=J(D_1\otimes D_2),\qquad
S^*=(D_1\otimes D_2)J
\tag{TG.14}
\]
has the full domain given by (TG.1), and adjoint domain given by its preimage under \(J\). The same rectangular graph-core proof applies to \(S\). For the adjoint, conjugate the positive factors: \(JD J\), with \(D=D_1\otimes D_2\), is the tensor of \(J_iD_iJ_i\). Its rectangular core, followed by \(J\), proves that \(S^*\) is the closure of \(S_1^*\odot S_2^*\). This supplies the antilinear adjoint assertion actually needed below.

<span id="oa-mod-tg-03--comparing-spatial-representations"></span>
<span id="OA-MOD-TG-03"></span>
<span id="oa-mod-tg-03"></span>
## OA-MOD-TG-03 — Comparing spatial representations

The tensor weight must live on the prescribed algebra \(M\bar\otimes N\), even when its support corners are represented in different GNS spaces. We supply the required representation comparison using the existing normal-functional standard-form theorem SF-10/11, the cyclic argument of FU-01, and the image theorem WH-02. Their existing prerequisite contracts remain in force.

Fix a standard representation of \(M\) on \(L\). Every normal unital representation on \(H\) embeds isometrically as a reducing subrepresentation of \(L\otimes\ell^2(I)\) for some arbitrary set \(I\). To prove this, choose a maximal orthogonal family of cyclic reducing subspaces of \(H\). Their sum is all of \(H\), since any nonzero orthogonal complement contains another cyclic subspace. On each cyclic subspace, its normal vector functional is represented by a cone vector \(v\in L\). The map \(av\mapsto a\xi\) preserves all inner products, hence extends to an intertwining isometry of the corresponding cyclic subspaces. This is the left-action version of the explicit proof in FU-01. Its orthogonal sum gives the claimed embedding. Denote its range projection by \(e\).

The commutant of \(M\otimes I\) on this amplification consists of bounded matrices with entries in \(M'\). Finite coordinate compressions prove this assertion: commutation is equivalent to commutation of each matrix entry, and those compressions converge strongly to the whole operator. If the original representation is faithful, \(e\) has central support one in this commutant. Indeed, the projection onto the closed span of all commutant translates of \(e\)'s range is central in the commutant. Its complement is also in \(M\otimes I\), hence equals \(z\otimes I\) for a central projection \(z\in M\). It annihilates \(e\)'s range, so faithfulness gives \(z=0\).

Apply this construction to faithful normal representations of \(M\) on \(H\) and \(N\) on \(K\), with standard spaces \(L_M,L_N\). Write
\[
P=(M\odot N)''\subseteq B(L_M\otimes L_N).
\tag{TG.15}
\]
After regrouping tensor factors, the amplifications act on \((L_M\otimes L_N)\otimes\ell^2(I\times J)\). Their joint range projection \(e\otimes f\) commutes with the amplification of \(P\). Compression gives a normal representation of \(P\) on \(H\otimes K\).

It is faithful. If \(x\in P\) annihilates this range, its amplification annihilates all translates of that range by the two amplified commutants, since it commutes with those operators. Their translates span the whole Hilbert space: each individual range is total under its commutant by the preceding central-support argument, and elementary tensors of those total subspaces are total. Thus \(x=0\). WH-02 makes the compression an isomorphism onto a von Neumann algebra. Its image is exactly the algebra generated by the original elementary tensors: one inclusion holds because it contains them, and the other follows by normality and ultraweak density of the algebraic generators in \(P\). We have proved a normal spatial comparison that fixes every \(a\otimes b\).

Consequently faithful normal changes of the two representations transport their spatial tensor products uniquely. Uniqueness follows from normality and density of elementary tensors. This also gives
\[
(e_0Me_0)\bar\otimes(f_0Nf_0)
\simeq (e_0\otimes f_0)(M\bar\otimes N)(e_0\otimes f_0)
\tag{TG.16}
\]
for arbitrary projections \(e_0,f_0\): in the original concrete spaces the corner is generated by compressed elementary tensors, by ultraweak density; the two restricted representations are faithful on the corners. No formula for the full commutant of a spatial tensor product was assumed in this argument. Zero corners are included.

<span id="oa-mod-tg-04--tensor-hilbert-algebras-and-tomita-domains"></span>
<span id="OA-MOD-TG-04"></span>
<span id="oa-mod-tg-04"></span>
## OA-MOD-TG-04 — Tensor Hilbert algebras and Tomita domains

Let \(\varphi,\psi\) be faithful normal semifinite weights on \(M,N\). In their faithful normal GNS representations put
\[
\mathcal A_1=\Lambda_\varphi(\mathfrak n_\varphi\cap\mathfrak n_\varphi^*),\qquad
\mathcal A_2=\Lambda_\psi(\mathfrak n_\psi\cap\mathfrak n_\psi^*).
\tag{TG.17}
\]
These are full left Hilbert algebras by WH-09/10. Give \(\mathcal A=\mathcal A_1\odot\mathcal A_2\) its factorwise product and involution and its tensor inner product. A simple left multiplication is \(L_\xi\otimes L_\eta\); a finite sum is bounded by the sum of the product operator norms. The inner-product adjoint identity is verified on elementary tensors and then by linearity. Products span a dense subspace, since the product span is dense in each factor. It remains to prove closability and identify the full closed involution.

Write \(S_i=J_i\Delta_i^{1/2}\) for the two closed Tomita operators from MF-01/06. Their cores are \(\mathcal A_i\). Since \(J_i\) preserves norm, these are also graph cores for \(D_i=\Delta_i^{1/2}\). By TG-01, \(D(D_1)\odot D(D_2)\) is a core for \(D=D_1\otimes D_2\). Replacing each factor of each finite sum by its graph approximation from \(\mathcal A_i\) proves that \(\mathcal A\) is itself a core: the errors in both the tensor vector and its product image tend to zero. Therefore its sharp map has precisely the closure
\[
S=JD,\qquad F=S^*=DJ,\qquad J=J_1\otimes J_2.
\tag{TG.18}
\]
The domains in this equality are the full integral domain of (TG.1) and its \(J\)-preimage, respectively. TG-02 also identifies \(F\) with the closure of the factorwise adjoint involutions. This proves all left Hilbert algebra axioms, rather than assuming them to invoke the weight construction.

Its generated left algebra is \(M\bar\otimes N\). For detail, the finite positive contraction nets of WG-008 belong to the two finite-star algebras and converge strongly to their identities in GNS. Thus bounded strong limits of \(L_\xi\otimes L_{e_\alpha}\) give \(L_\xi\otimes I\), and similarly give \(I\otimes L_\eta\). Their von Neumann algebras generate the spatial tensor product. The reverse inclusion follows from the displayed simple multiplication operators. TG-03 transports this assertion to any prescribed faithful concrete representations.

Apply WH-03–08 to the tensor Hilbert algebra, completing it before taking the weight. This yields a faithful normal semifinite weight \(\theta\) and a canonical GNS identification with \(H_\varphi\otimes H_\psi\). Under it,
\[
\Lambda_\theta(x\otimes y)=\Lambda_\varphi(x)\otimes\Lambda_\psi(y)
\quad(x\in\mathfrak n_\varphi\cap\mathfrak n_\varphi^*,\ y\in\mathfrak n_\psi\cap\mathfrak n_\psi^*).
\tag{TG.19}
\]
Indeed the elementary tensor is the multiplication vector of the elementary operator, and WH-08 identifies that multiplication vector with its GNS vector. Full completion leaves the closed sharp operator unchanged, so polar uniqueness, (TG.6) and (TG.18) give
\[
J_\theta=J_\varphi\otimes J_\psi,\qquad
\Delta_\theta=\Delta_\varphi\otimes\Delta_\psi,\qquad
\Delta_\theta^{it}=\Delta_\varphi^{it}\otimes\Delta_\psi^{it}.
\tag{TG.20}
\]
The middle equality denotes the closed tensor, with its full spectral domain, rather than the algebraic tensor. The last equality follows from (TG.7).

MF-06 now implements the modular automorphisms. On elementary operators its conjugation formula gives
\[
\sigma_t^\theta(a\otimes b)=\sigma_t^\varphi(a)\otimes\sigma_t^\psi(b),\qquad
\sigma_t^\theta=\sigma_t^\varphi\bar\otimes\sigma_t^\psi.
\tag{TG.21}
\]
TG-03 supplies the normal spatial automorphism on the right. Equality on the entire von Neumann algebra follows by normality and ultraweak density. This proves Proposition VIII.4.3, including normality, semifiniteness and faithfulness of its tensor weight.

<span id="oa-mod-tg-05--all-positive-values-and-nonfaithful-support-corners"></span>
<span id="OA-MOD-TG-05"></span>
<span id="oa-mod-tg-05"></span>
## OA-MOD-TG-05 — All positive values and nonfaithful support corners

The construction of TG-04 defines \(\varphi\otimes\psi\) in the faithful case. WH-10 shows that the associated weight is unique for the specified full Hilbert algebra, and TG-03 makes this definition independent of the faithful normal concrete representations.

For every \(a\in M_+,b\in N_+\) it satisfies
\[
(\varphi\otimes\psi)(a\otimes b)=\varphi(a)\psi(b),\qquad 0\cdot\infty=0.
\tag{TG.22}
\]
When both values are finite, their square roots belong to the finite-star algebras; (TG.19) and the GNS norm prove the formula. Infinite values need a separate argument. A finite positive cone need not provide positive approximants below an arbitrary positive operator.

Let \(\omega\leq\varphi\) and \(\nu\leq\psi\) be bounded normal positive functionals. OW-02/03 provide implementing vectors \(\eta_\omega,\eta_\nu\) and positive contractions \(h_\omega^{1/2},h_\nu^{1/2}\) in the respective commutants, such that
\[
x\eta_\omega=h_\omega^{1/2}\Lambda_\varphi(x),\qquad
y\eta_\nu=h_\nu^{1/2}\Lambda_\psi(y)
\tag{TG.23}
\]
on the respective finite left ideals. Thus these vectors are right bounded for the factor Hilbert algebras. The tensor vector \(\eta=\eta_\omega\otimes\eta_\nu\) is right bounded for their algebraic tensor, with right multiplication operator
\(R_\eta=h_\omega^{1/2}\otimes h_\nu^{1/2}\), of norm at most one; verify the equality on finite sums of elementary vectors. The mixed bounded-vector identity WH-04 extends it to every vector of the completed left multiplication domain. No adjoint-domain membership of \(\eta\) is required for that identity.

For \(X\geq0\) with \(\theta(X)<\infty\), write \(X^{1/2}=\lambda_\xi\). The normal vector functional \(\Omega(X)=\langle X\eta,\eta\rangle\) then satisfies
\[
\Omega(X)=\|\lambda_\xi\eta\|^2=\|R_\eta\xi\|^2\leq\|\xi\|^2=\theta(X).
\tag{TG.24}
\]
For infinite \(\theta(X)\) the same domination is automatic. On elementary operators this functional equals \(\omega(a)\nu(b)\). NW-11 recovers each normal weight from its dominated bounded normal functionals. Taking the two independent suprema in (TG.24) gives \(\theta(a\otimes b)\geq\varphi(a)\psi(b)\). If either value is infinite and the other is strictly positive this forces infinity. In the faithful case a zero value forces the corresponding positive operator to be zero, so the convention in (TG.22) is correct. Together with the finite case this proves every extended value.

Now let \(\varphi,\psi\) be arbitrary normal semifinite weights, with supports \(e=s(\varphi)\), \(f=s(\psi)\). WS-05/06 give faithful normal semifinite restrictions \(\varphi_e,\psi_f\) to their corners and the identities \(\varphi(a)=\varphi_e(eae)\), \(\psi(b)=\psi_f(fbf)\). Put \(P=e\otimes f\). Use TG-03/04 to construct the faithful tensor weight \(\theta_P\) on the corner in (TG.16), and define on the whole algebra
\[
\theta(X)=\theta_P(PXP),\qquad X\in(M\bar\otimes N)_+.
\tag{TG.25}
\]
Additivity and homogeneity follow from linearity of compression. Normality follows because compression preserves bounded increasing positive suprema. Its support is exactly \(P\): the complement has zero weight; if a projection \(q\) has zero weight, faithfulness in the corner gives \(PqP=0\), hence \(qP=0\).

It is semifinite. Choose finite positive contractions \(u_\alpha\uparrow e\), \(v_\beta\uparrow f\) for the corner weights using WG-008. Their product contractions increase strongly to \(P\) and have finite tensor weight by (TG.22). The finite positive contractions
\[
u_\alpha\otimes v_\beta+(1-P)\uparrow1
\tag{TG.26}
\]
therefore prove semifiniteness by the finite-cone criterion WG-008/WS-02. If either support is zero, (TG.25) is simply the zero weight; the same conclusion holds. Compressing an elementary positive tensor in (TG.25) reduces (TG.22) to its faithful corner case, so it also proves the all-positive formula for nonfaithful weights.

Definition VIII.4.2 is precisely (TG.25), with the corner weight associated to the algebraic tensor of the two full support-corner Hilbert algebras. Its support and that specified corner weight determine it uniquely by WS-05. The modular group formula (TG.21) applies to the faithful weights, or to their faithful support restrictions. It does not assert that the full GNS space of a nonfaithful weight equals its support-corner GNS space: a noncentral support can leave additional left-action directions. TG-06 exhibits this distinction.

