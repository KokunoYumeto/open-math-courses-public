# Amplified traces and concrete representations

The tracial Hilbert space of a matrix amplification has three factors: the original tracial space, the matrix space, and its conjugate. Left multiplication acts on the first two; right multiplication acts on the first and third. This separation lets us realize every concrete semifinite von Neumann algebra on a space of the form \(eL^2(N,T)f\), with both corner projections having full central support.

Inner products are linear in the first variable. For \(u,v\) in a Hilbert space \(K\), write \(\theta_{u,v}w=\langle w,v\rangle u\). Its conjugate space \(\overline K\) has \(\langle\overline v,\overline w\rangle=\langle w,v\rangle\). All index sets and Hilbert dimensions below are arbitrary. A positive sum over an index set is the supremum of its finite subsums.

## The square-integrable matrix entries

Let \(M\) have a faithful normal semifinite trace \(\tau\), let \(K\) be a Hilbert space, and put
\[
 N=M\mathbin{\overline\otimes}B(K).
\]
The matrix trace construction, TB05, supplies a faithful normal semifinite trace \(T\) on \(N\). For an orthonormal basis \((k_i)_{i\in I}\), with matrix entries in \(M\), its formula is
\[
 \begin{gathered}
 T(X)=\sum_i\tau(X_{ii}),\\
 X\geq0.
 \end{gathered}
 \tag{AR.1}
\]
That construction proves basis independence, including for uncountable bases. Its positive column-sum calculation gives, for every bounded \(x\in N\),
\[
 \begin{gathered}
 T(x^*x)\\
 {}=\sum_{i,j}\tau(x_{ij}^*x_{ij}).
 \end{gathered}
 \tag{AR.2}
\]
In particular, if \(x\in\mathfrak n_T\), then each entry belongs to \(\mathfrak n_\tau\).

Let \(P_F\) denote the projection in \(K\) onto finitely many basis vectors. For finite \(F,G\subset I\), set
\[
 \begin{gathered}
 x_{F,G}\\
 {}=(1\otimes P_F)x(1\otimes P_G)\\
 {}=\sum_{i\in F,j\in G}
 x_{ij}\otimes\theta_{k_i,k_j}.
 \end{gathered}
\]
The finite trace domain is a two-sided ideal by TB01. Thus \(x-x_{F,G}\in\mathfrak n_T\). With \(S=F\times G\), equation (AR.2) yields
\[
 \begin{gathered}
 \|x-x_{F,G}\|_{2,T}^2\\
 {}=\sum_{(i,j)\notin S}
       \tau(x_{ij}^*x_{ij}).
 \end{gathered}
 \tag{AR.3}
\]
The right side tends to zero as \(F,G\) increase: the total nonnegative sum is finite, and every finite subset of \(I\times I\) lies in a finite rectangle. Since \(\mathfrak n_T\) is dense in its tracial Hilbert space, this proves density of
\(\mathfrak n_\tau\odot\mathcal F(K)\) in \(L^2(N,T)\), where \(\mathcal F(K)\) is the finite-rank ideal and \(\odot\) denotes algebraic tensor product. No finite-coordinate compression was assumed to have finite trace independently of its entries.

## The unitary tensor identification

Put \(H_0=L^2(M,\tau)\). The tracial Hilbert model and its agreement with the GNS completion are proved in TI15. There is a unitary
\[
 \begin{gathered}
 U:L^2(N,T)\\
 {}\longrightarrow H_0\otimes K\otimes\overline K,\\
 U(a\otimes\theta_{u,v})\\
 {}=a\otimes u\otimes\overline v,\\
 a\in\mathfrak n_\tau.
 \end{gathered}
 \tag{AR.4}
\]
To prove it, put \(x=a\otimes\theta_{u,v}\) and \(y=b\otimes\theta_{u',v'}\). Rank-one multiplication and (AR.1), extended linearly on the finite trace ideal, give
\[
 \begin{aligned}
 T(y^*x)&=\tau(b^*a)\\
 &\quad\cdot\langle u,u'\rangle\langle v',v\rangle.
 \end{aligned}
\]
For the scalar rank-one trace, the formula is
\(\sum_i\langle\theta_{u,v}k_i,k_i\rangle=\langle u,v\rangle\), by Parseval; this also checks the complex conjugations in the preceding equality. The product \(b^*a\) is integrable by the tracial Cauchy–Schwarz inequality, or by TI10.

The displayed pairing is exactly the tensor inner product of the proposed images. By linearity the map preserves norms on every finite sum and is therefore well defined there. AR01 makes its domain dense. Its range contains all finite tensors with first coordinate in the dense subspace \(\mathfrak n_\tau\subset H_0\), so is dense as well. The isometry extends uniquely to the stated onto unitary. The construction of Hilbert tensor products and their bounded elementary operators is given in TB05.

For \(a\in M\), let \(L_a\) and \(R_a\) be left and right multiplication on \(H_0\). Use \(L^N_x,R^N_x\) for the corresponding actions on \(L^2(N,T)\). Direct multiplication on the dense domain in (AR.4) gives
\[
 \begin{gathered}
 UL^N_{a\otimes b}U^*\\
 {}=L_a\otimes b\otimes1,\\
 UR^N_{a\otimes b}U^*\\
 {}=R_a\otimes1\otimes\overline{b^*},\\
 b\in B(K).
 \end{gathered}
 \tag{AR.5}
\]
Here \(\overline{b^*}\,\overline v=\overline{b^*v}\). This is a linear operator on \(\overline K\); the assignment \(b\mapsto\overline{b^*}\) is linear and reverses products. It is precisely the third-factor action required by right multiplication.

The full tracial action theorem, TA02, proves normality of these actions and that their images are von Neumann algebras. Commutation with the images of the elementary tensors is equivalent to commutation with the whole image: the set of elements satisfying any fixed commutation equation is ultraweakly closed, and the elementary tensors generate \(N\). Normality and separate ultraweak continuity of multiplication justify that assertion; see CP06. On the three-factor Hilbert space, put
\[
 \begin{gathered}
 \mathcal A_L=L(M)\mathbin{\overline\otimes}B(K)\otimes1,\\
 \mathcal A_R=R(M)\otimes1\mathbin{\overline\otimes}B(\overline K).
 \end{gathered}
\]
Taking bicommutants in (AR.5) consequently proves
\[
 \begin{gathered}
 UL^N(N)U^*=\mathcal A_L,\\
 UR^N(N)U^*=\mathcal A_R.
 \end{gathered}
 \tag{AR.6}
\]
In particular, (AR.4) identifies the represented left algebras, not just the underlying Hilbert spaces.

Taking adjoints of the elementary tensors also identifies the canonical conjugation:
\[
 \begin{gathered}
 UJ_TU^*(\eta\otimes u\otimes\overline v)\\
 {}=J_\tau\eta\otimes v\otimes\overline u.
 \end{gathered}
 \tag{AR.7}
\]
This is first checked for \(\eta\in\mathfrak n_\tau\) and then extended by continuity. The exchange of the last two factors is necessary.

## Matrix commutants and the center

We record the operator tests needed for the corner construction. If \(A\subseteq B(E)\) is a von Neumann algebra and \(F\) is any Hilbert space, then
\[
 \begin{gathered}
 (A\otimes1_F)'\\
 {}=A'\mathbin{\overline\otimes}B(F).
 \end{gathered}
 \tag{AR.8}
\]
Indeed, in a basis of \(F\), commutation with \(a\otimes1\) says exactly that every matrix entry belongs to \(A'\). Finite square compressions of such an operator are finite sums of elementary tensors in \(A'\odot B(F)\). They converge strongly to the operator and have norm bounded by its norm. This proves one inclusion; elementary tensors in the right side commute with \(A\otimes1\), and strong closedness proves the other. The entry and strong-compression arguments are the same Hilbert direct-sum calculations supplied in TB05.

An operator on \(E\otimes F\) commuting with \(1_E\otimes B(F)\) is of the form \(s\otimes1_F\). Commutation with the diagonal matrix units makes its off-diagonal entries zero; commutation with all matrix units makes its diagonal entries equal. Testing finite-coordinate vectors proves the equality on the whole tensor space, and bounds \(\|s\|\) by the original operator norm. Applied inside \(M\mathbin{\overline\otimes}B(K)\), whose entries belong to \(M\), this gives, for \(K\ne0\),
\[
 \begin{gathered}
 Z(N)\\
 {}=Z(M)\otimes1_K.
 \end{gathered}
 \tag{AR.9}
\]
An element of that form is central exactly when its coefficient commutes with \(M\).

We will also use a compression identity. If \(q\in A'\) is a projection, then
\[
 \begin{gathered}
 (A|_{qE})'\\
 {}=qA'q|_{qE}.
 \end{gathered}
 \tag{AR.10}
\]
To prove the nontrivial inclusion, extend an operator commuting with \(A|_{qE}\) by zero on \((1-q)E\). Both subspaces reduce \(A\), so the extension commutes with \(A\) on all of \(E\); its compression is the given operator. The reverse inclusion follows by multiplication. This proof requires only that \(q\) be in the commutant, and makes no assertion about a projection in \(A\) in its place.

## Every normal representation embeds in an amplification

Let \(\pi:M\to B(H)\) be a normal unital star representation. Every normal positive functional on \(M\) is a vector functional in \(H_0\). In fact TI06 gives its unique positive density \(h\in L^1(M,\tau)\). Put \(\eta=h^{1/2}\). Spectral calculus and \(\tau(h)<\infty\) put \(\eta\) in \(L^2\). The product and cyclicity statements of TI10 give
\[
 \begin{gathered}
 \langle a\eta,\eta\rangle_2\\
 {}=\tau(h^{1/2}a h^{1/2})\\
 {}=\tau(ha).
 \end{gathered}
 \tag{AR.11}
\]
These products are integrable, so neither equality involves an undefined expression. No faithfulness of the functional is needed.

Decompose \(H\) as an orthogonal sum of nonzero cyclic reducing subspaces
\[
 \begin{gathered}
 H=\bigoplus_{i\in I}H_i,\\
 H_i=[\pi(M)\xi_i].
 \end{gathered}
 \tag{AR.12}
\]
Here is the existence argument. Order orthogonal families of nonzero cyclic subspaces by inclusion. The union of a chain is again such a family, so a maximal family exists. Each cyclic subspace reduces \(\pi(M)\), because the algebra is closed under adjoints. If the orthogonal complement of their sum were nonzero, any nonzero vector in that reducing complement would generate one more orthogonal cyclic subspace, contradicting maximality.

For each \(i\), apply (AR.11) to
\(\varphi_i(a)=\langle\pi(a)\xi_i,\xi_i\rangle\), obtaining \(\eta_i\in H_0\). The functional is normal by normality of \(\pi\) and the normality of vector functionals, CP07. The map
\[
 V_i(\pi(a)\xi_i)=a\eta_i
 \tag{AR.13}
\]
preserves inner products: test two such vectors using \(\varphi_i(b^*a)\). It is well defined, extends to a unitary onto \([M\eta_i]\subseteq H_0\), and intertwines the two left actions. Let \(q_i\) be the projection onto that reducing subspace. Then \(q_i\in L(M)'=R(M)\), by TA02. There is a unique projection \(f_i\in M\) with \(q_i=R_{f_i}\): the right action is faithful, onto its image, preserves adjoints, and reverses multiplication, so its inverse carries projections to projections.

Take \(K=\ell^2(I)\), with basis \((k_i)\). The direct sum of the \(V_i\), placed in the coordinates \(\overline{k_i}\), is a unitary
\[
 \begin{gathered}
 V:H\longrightarrow\\
 q(H_0\otimes\overline K),\\
 q=\sum_i R_{f_i}\otimes p_{\overline{k_i}},\\
 V\pi(a)\\
 {}=(L_a\otimes1)V.
 \end{gathered}
 \tag{AR.14}
\]
The sum defining \(q\) is a strong sum of orthogonal projections. The direct-sum norm identity proves that the map on finite sums is isometric, and each coordinate range is exactly the corresponding range of \(q\); density extends it to the onto unitary in (AR.14). Thus there is no countable-generation assumption hidden in the amplification.

## The two full corners

Now let \(M\subseteq B(H)\) be a concrete semifinite von Neumann algebra, acting unitally. The arbitrary-algebra trace-existence theorem, TE11, supplies a faithful normal semifinite trace \(\tau\) on \(M\). Apply AR04 to the given inclusion, which is faithful and normal. If \(H=0\), take \(N=0\), \(e=f=0\), and the zero trace; the central-support assertions read \(0=1_N\) and the representation is the zero one. Assume henceforth \(H\ne0\), so \(I\) and \(K\) are nonempty.

Choose a unit vector \(k_0\in K\), and form \(N=M\mathbin{\overline\otimes}B(K)\) with trace \(T\) as in AR01. Define two projections in this same algebra:
\[
 \begin{gathered}
 e=1\otimes p_{k_0},\\
 f=\sum_i f_i\otimes p_{k_i}.
 \end{gathered}
 \tag{AR.15}
\]
The second sum exists strongly because its terms are orthogonal projections bounded in finite sum by one; BK04 supplies the limit. Its square equals itself on each coordinate, hence on the whole Hilbert space.

The notation \(\mathcal H=eL^2(N,T)f\) means the range of the commuting projections \(L^N_eR^N_f\). In the tensor model of AR02, \(L^N_e\) selects \(\mathbb Ck_0\) in the middle factor. Define
\[
 Q:H_0\otimes\overline K\longrightarrow eL^2(N,T)
\]
by \(Q(\eta\otimes\overline v)=U^*(\eta\otimes k_0\otimes\overline v)\). This is unitary. Equation (AR.5), normality of the right action on the increasing finite sums in (AR.15), and (AR.14) give
\[
 Q^*R^N_fQ=q.
 \tag{AR.16}
\]
Consequently \(W=QV\) is a unitary from \(H\) onto \(eL^2(N,T)f\). The map \(a\mapsto a\otimes p_{k_0}\) identifies \(M\) with \(eNe\): entry compression in the one-dimensional corner gives every element of that corner and is its inverse. Equations (AR.5) and (AR.14) therefore prove the spatial identification
\[
 \begin{gathered}
 W a W^*\\
 {}=L^N_{a\otimes p_{k_0}}
             |_{\mathcal H},\\
 WM W^*\\
 {}=L^N(eNe)|_{\mathcal H}.
 \end{gathered}
 \tag{AR.17}
\]

Both projections in (AR.15) have central support one. For \(e\), (AR.9) shows that a central projection annihilating it has the form \(z\otimes1\) with \(z\otimes p_{k_0}=0\). Testing a tensor with second coordinate \(k_0\) gives \(z=0\).

For \(f\), suppose \((z\otimes1)f=0\) for a central projection \(z\in M\). The diagonal entries give \(zf_i=0\) for every \(i\). Central left and right actions agree on the entire tracial Hilbert space, by SJ06. Since \(\eta_i=R_{f_i}\eta_i\), we get \(L_z\eta_i=R_zR_{f_i}\eta_i=0\). Equation (AR.13) implies \(z\xi_i=0\). Centrality then makes \(z\) vanish on every cyclic subspace \([M\xi_i]\), hence on \(H\). Faithfulness of the given concrete representation gives \(z=0\). The complement of a central carrier is precisely the largest central projection annihilating the projection, so
\[
 \begin{gathered}
 c_N(e)=1,\\
 c_N(f)=1.
 \end{gathered}
 \tag{AR.18}
\]
This proves the full two-corner representation, including the carrier condition on \(f\).

## The commutant on the corner space

The same construction identifies the commutant, with no extra representation theorem. On \(eL^2(N,T)\), the unitary \(Q\) identifies the left action of \(eNe\) with \(L(M)\otimes1_{\overline K}\). By (AR.8) and TA02 its commutant is
\[
 R(M)\mathbin{\overline\otimes}B(\overline K).
\]
Equation (AR.6) shows that this is exactly the restriction of \(R^N(N)\) to \(eL^2(N,T)\). Indeed the right action is the identity on the middle factor of the tensor model; restriction to \(\mathbb Ck_0\) removes that factor and leaves the entire displayed algebra.

Now compress by \(R^N_f\), which lies in this commutant, and write \(\mathcal H=eL^2(N,T)f\). Equation (AR.10) gives
\[
 \begin{gathered}
 \bigl(L^N(eNe)|_{\mathcal H}\bigr)'\\
 {}=R^N(fNf)|_{\mathcal H}.
 \end{gathered}
 \tag{AR.19}
\]
The order of multiplication in the right action causes no ambiguity: \(R^N_fR^N_bR^N_f=R^N_{fbf}\). This right action of \(fNf\) on the corner space is faithful. In fact its restriction to \(eL^2(N,T)\) is faithful, since under (AR.6) an operator acting as the identity on the middle factor cannot vanish just on a nonzero middle-factor line unless it vanishes everywhere. If \(b=fbf\) and \(R^N_b\) vanishes on \(eL^2(N,T)f\), then \(R^N_b=R^N_bR^N_f\) on \(eL^2(N,T)\), so it vanishes there too and \(b=0\).

Thus the original represented algebra and its commutant appear as the left and right corners of one tracial Hilbert space. In (AR.19) the right corner is represented as an opposite algebra, exactly as required by \(R^N_bR^N_d=R^N_{db}\).

## Three boundary checks

**Full central support does not mean equivalence.** Let \(M=\mathbb C\) act by scalars on an infinite-dimensional \(H\), with basis indexed by \(I\). Its cyclic decomposition consists of the coordinate lines. With \(\tau(1)=1\), the above construction has \(f_i=1\), \(N=B(\ell^2(I))\), \(e\) rank one, and \(f=1\). Both projections have full central support. They are not equivalent: a partial isometry with rank-one initial projection has one-dimensional final range. The space \(eL^2(N,T)\) is naturally \(\overline{\ell^2(I)}\), of precisely the required Hilbert dimension. This works for uncountable \(I\) as well. In particular, (AR.18) does not assert finite trace of \(f\).

**Faithfulness is what fills the second central carrier.** Take \(M=\mathbb C\oplus\mathbb C\) with \(\tau(a,b)=a+b\) for positive pairs, and the normal unital representation \(\pi(a,b)=a\) on \(\mathbb C\). The single vector density is \(h=(1,0)\), its cyclic range in \(L^2(M,\tau)\) is the first coordinate, and the construction gives \(K=\mathbb C\), \(e=1\), \(f=(1,0)\). The representation formula still holds, but \(c(f)=(1,0)\ne1\). This is exactly where the faithful concrete hypothesis of AR05 is used.

**The conjugate factor fixes the scalar convention.** For \(\lambda\in\mathbb C\),
\(\theta_{u,\lambda v}=\overline\lambda\theta_{u,v}\). Its image under (AR.4) must therefore scale by \(\overline\lambda\), as \(\overline{\lambda v}\) does in \(\overline K\). Replacing that factor by \(v\in K\) would instead scale by \(\lambda\), so would fail to define a linear unitary. Similarly, the right matrix action is \(\overline{b^*}\), rather than \(\overline b\); (AR.5) follows from \(\theta_{u,v}b=\theta_{u,b^*v}\).

**Source.** M. Takesaki, *Theory of Operator Algebras I*, Chapter V, §3, Propositions 3.6–3.7, pp. 337–338. The amplification and corner identifications are proved here by matrix entries, trace densities and an explicit cyclic decomposition, including both central-carrier assertions.
