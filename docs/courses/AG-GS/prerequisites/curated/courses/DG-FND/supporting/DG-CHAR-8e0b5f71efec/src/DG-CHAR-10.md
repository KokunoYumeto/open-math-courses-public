# Pontryagin classes and the Euler square

*Written and self-checked by GPT-6 Astra (OpenAI), at Ultra, October 2026. CC0 1.0.*

Pontryagin classes are integral classes of real vector bundles. Their definition uses even Chern classes; the odd Chern classes of a complexified real bundle explain the two-torsion qualification in the direct-sum formula. We calculate this qualification explicitly, compute the classes of complex projective spaces and spheres, and prove the top Euler-square identity with its orientation sign.

All bundles have finite constant rank, and all bases are Hausdorff. Additional paracompactness assumptions are stated where used. We write products for cup products. The Chern classes, including their metric-free construction, are those of [DG-CHAR-09 B.2](DG-CHAR-09.md#theorem-b-2); their conjugation rule is [DG-CHAR-09 B.5](DG-CHAR-09.md#theorem-b-5). The real classes \(w_i\) are the Stiefel–Whitney classes of [DG-CHAR-09 A.2](DG-CHAR-09.md#theorem-a-2). Integral Euler classes use [DG-CHAR-06 T.4](DG-CHAR-06.md#theorem-t-4).

## A. Complexification and the torsion correction

**Lemma A.1 (complexification and the definition).** A real rank-\(n\) bundle \(E\) has a complex rank-\(n\) bundle \(E_{\mathbb C}\), whose underlying real bundle is \(E\oplus E\). It has a natural complex bundle isomorphism
\[
 E_{\mathbb C}\cong\overline{E_{\mathbb C}},
 \qquad 2c_{2j+1}(E_{\mathbb C})=0\quad(j\geq0).
\tag{A1}
\]
Define
\[
 p_0(E)=1,\qquad p_i(E)=(-1)^i c_{2i}(E_{\mathbb C})\in H^{4i}(B;\mathbb Z)
 \quad(i\geq1).
\tag{A2}
\]
Then \(p_i(E)=0\) for \(2i>n\). These classes are invariant under real bundle isomorphisms, natural under pullback, and stable under adjoining trivial real bundles, on every Hausdorff base. They do not require an orientation. Write \(p(E)=\sum_{i\geq0}p_i(E)\).

**Proof.** On the real bundle \(E\oplus E\) define
\[
 (a+ib)(x,y)=(ax-by,bx+ay),\qquad a,b\in\mathbb R.
\tag{A3}
\]
A real frame of \(E\) identifies \((x,y)\) with the complex coordinate vector \(x+iy\). A real transition matrix \(A\) sends it to \(Ax+iAy=A(x+iy)\), a complex-linear coordinate change. These charts establish the claimed rank and complex bundle structure, with its original direct-sum topology. This is also the tensor complexification: the real-bilinear map \(v\otimes(a+ib)\mapsto(av,bv)\) has inverse \((x,y)\mapsto x\otimes1+y\otimes i\); the two compositions are the identity by real bilinearity.

Let \(\kappa(x,y)=(x,-y)\). It is continuous, involutive and satisfies \(\kappa(\lambda z)=\overline\lambda\,\kappa(z)\). Scalar multiplication in the conjugate target is \(\lambda\cdot_{\overline{E_{\mathbb C}}}z=\overline\lambda z\), so \(\kappa\) is complex linear into that target. Isomorphism invariance and conjugation, [DG-CHAR-09 B.2](DG-CHAR-09.md#theorem-b-2) and [DG-CHAR-09 B.5](DG-CHAR-09.md#theorem-b-5), give
\[
 c_q(E_{\mathbb C})=(-1)^q c_q(E_{\mathbb C}).
\]
For odd \(q\) this is (A1). Annihilation by two allows the class to be zero.

The rank convention for Chern classes proves the vanishing assertion. Complexification commutes with pullback: on a fibre over \(b'\), both constructions have the two ordered vectors in \(E_{f(b')}\), with the scalar law (A3), and this identity is continuous in pullback charts. It commutes with real isomorphisms and with direct sums by applying the original maps to the two real coordinates and regrouping them. Finally \((\underline{\mathbb R}^{\,s})_{\mathbb C}=\underline{\mathbb C}^{\,s}\). Chern naturality, invariance and stability in [DG-CHAR-09 B.2](DG-CHAR-09.md#theorem-b-2) therefore prove all their Pontryagin counterparts. No step chooses an orientation of \(E\). All positive classes of a trivial real bundle vanish: complex Chern stability applied to the zero bundle gives \(c(\underline{\mathbb C}^{\,n})=1\). □

**Theorem A.2 (the integral direct-sum defect).** For real bundles \(E,F\) on a paracompact Hausdorff base and every \(k\geq0\),
\[
 2\left(p_k(E\oplus F)-\sum_{i+j=k}p_i(E)p_j(F)\right)=0.
\tag{A4}
\]
After mapping to cohomology with coefficients in a commutative unital ring in which \(2\) is invertible, \(p(E\oplus F)=p(E)p(F)\). Formula (A4) itself is an integral assertion.

**Proof.** By A.1, \((E\oplus F)_{\mathbb C}\cong E_{\mathbb C}\oplus F_{\mathbb C}\). The integral Chern Whitney formula [DG-CHAR-09 B.4](DG-CHAR-09.md#theorem-b-4) gives
\[
 p_k(E\oplus F)=
 (-1)^k\sum_{a+b=2k}c_a(E_{\mathbb C})c_b(F_{\mathbb C}).
\tag{A5}
\]
The indices \(a,b\) have the same parity. For \(a=2i,b=2j\), \(i+j=k\), the factor \((-1)^k\) equals \((-1)^i(-1)^j\), so these terms give the sum in (A4). Each remaining term has two odd indices. Its first factor is killed by \(2\) by A.1, and bilinearity of cup product kills the product by \(2\). Summing proves (A4). When \(k=0\), there are no odd-index terms and the difference is zero.

Changing integer cochain values by \(\mathbb Z\to R\) commutes with coboundary, pullback and cup product: their formulas are sums, signs and products of values, as in [DG-CHAR-06 K.5](DG-CHAR-06.md#lemma-k-5). Thus (A4) remains true after changing coefficients. Multiplication by the scalar \(2\) on the \(R\)-module \(H^q(B;R)\) then has inverse multiplication by \(2^{-1}\). Its vanishing forces the defect to vanish in each degree, proving the total-class formula over \(R\). □

**Theorem A.3 (reduction modulo two).** For a real bundle on a paracompact Hausdorff base,
\[
 \rho_2 p_i(E)=w_{2i}(E)^2,
\tag{A6}
\]
where \(\rho_2\) reduces integer cochain values modulo two.

**Proof.** The underlying real bundle of \(E_{\mathbb C}\) is \(E\oplus E\). [DG-CHAR-09 C.3](DG-CHAR-09.md#theorem-c-3) and the real Whitney formula [DG-CHAR-09 A.3](DG-CHAR-09.md#theorem-a-3) give
\[
 \rho_2c_{2i}(E_{\mathbb C})
 =w_{4i}(E\oplus E)
 =\sum_{a+b=4i}w_a(E)w_b(E).
\tag{A7}
\]
Graded commutativity [DG-CHAR-06 X.5](DG-CHAR-06.md#corollary-x-5) has no sign over \(\mathbb F_2\). Consequently the terms with \(a\ne b\) pair to zero, leaving \(w_{2i}(E)^2\). The coefficient image of \((-1)^i\) is one. Substituting (A2) proves (A6), including degree zero and the indices forced to vanish by rank. □

**Example A.4 (a nonzero integral defect).** Let \(L\) be the tautological real line on \(\mathbb RP^4\). Then
\[
 p(L)=1,\qquad
 p_1(L\oplus L)=-t^2\ne0,\qquad t=c_1(L_{\mathbb C}),\qquad 2t=0.
\tag{A8}
\]
In particular the integral total Pontryagin class need not be multiplicative.

**Proof.** This projective space is compact Hausdorff by [DG-CHAR-08 R.1](DG-CHAR-08.md#lemma-r-1). It is paracompact, since each open cover has a finite subcover, which is a locally finite open refinement. Write \(a=w_1(L)\). The line normalization in [DG-CHAR-09 A.2](DG-CHAR-09.md#theorem-a-2) identifies it with \(e_2(L)\). The projective ring calculation [DG-CHAR-08 R.3](DG-CHAR-08.md#theorem-r-3) gives
\[
 H^*(\mathbb RP^4;\mathbb F_2)=\mathbb F_2[a]/(a^5),
 \qquad a^4\ne0.
\tag{A9}
\]
Lemma A.1 gives \(2t=0\) and \(p(L)=1\), the latter because \(L\) has rank one. By [DG-CHAR-09 C.3](DG-CHAR-09.md#theorem-c-3) and [DG-CHAR-09 A.3](DG-CHAR-09.md#theorem-a-3),
\[
 \rho_2t=w_2((L_{\mathbb C})_{\mathbb R})
 =w_2(L\oplus L)=a^2.
\]
Here \(w(L)=1+a\), by the rank and line conventions. Reduction commutes with products, so \(\rho_2(t^2)=a^4\ne0\). Hence \(t^2\ne0\) integrally: a homomorphism sends zero to zero. Both summands of \(L_{\mathbb C}\oplus L_{\mathbb C}\) are complex lines with total class \(1+t\). Their degree-four Chern class is \(t^2\), by [DG-CHAR-09 B.4](DG-CHAR-09.md#theorem-b-4). Applying (A2) proves (A8). Finally \(2t^2=(2t)t=0\), so the defect is nonzero and killed by two, in agreement with A.2. □

## B. The underlying real bundle of a complex bundle

**Lemma B.1 (realification followed by complexification).** For every complex bundle \(V\) on a Hausdorff base,
\[
 (V_{\mathbb R})_{\mathbb C}\cong V\oplus\overline V.
\tag{B1}
\]
On a paracompact Hausdorff base this gives the integral identities
\[
 p_k(V_{\mathbb R})
 =(-1)^k\sum_{i+j=2k}(-1)^j c_i(V)c_j(V),
\tag{B2}
\]
and, in particular,
\[
 \begin{aligned}
 p_1(V_{\mathbb R})&=c_1(V)^2-2c_2(V),\\
 p_2(V_{\mathbb R})&=c_2(V)^2-2c_1(V)c_3(V)+2c_4(V).
 \end{aligned}
\tag{B3}
\]
Above-rank Chern classes in these expressions are zero.

**Proof.** Distinguish the original complex structure \(I\) on \(V_{\mathbb R}\) from the complex scalar action on its complexification. Represent a vector in the latter by \((x,y)\) as in (A3). Define
\[
 \Phi(x,y)=(x+Iy,x-Iy),\qquad
 \Phi^{-1}(v,w)=\left(\frac{v+w}{2},-\frac{I(v-w)}{2}\right).
\tag{B4}
\]
The symbols \(v,w\) in the inverse are regarded as vectors of the same underlying real fibre of \(V\); the second output of \(\Phi\) is a vector in \(\overline V\). Both compositions are the identity, using \(I^2=-1\). They are continuous real bundle maps because addition and \(I\) are continuous in every bundle chart.

Multiplication by the complex scalar \(i\) on the domain sends \((x,y)\) to \((-y,x)\). Applying \(\Phi\) gives \((-y+Ix,-y-Ix)\). Multiplying \(\Phi(x,y)\) by \(i\) in \(V\oplus\overline V\) gives \((I(x+Iy),-I(x-Iy))\), the same pair. Real linearity and this equality prove complex linearity. Equivalently, the map on a simple tensor sends \(x\otimes z\) to \((zx,\overline z x)\), with the second vector interpreted in the conjugate bundle.

When the base is paracompact Hausdorff, apply [DG-CHAR-09 B.4](DG-CHAR-09.md#theorem-b-4) to (B1) and [DG-CHAR-09 B.5](DG-CHAR-09.md#theorem-b-5) to its second summand. Taking the degree-\(4k\) component and the sign in (A2) yields (B2).

For \(k=1\), the three pairs of indices are \((0,2),(1,1),(2,0)\). Their signed sum before the outer minus sign is \(2c_2-c_1^2\). For \(k=2\), the five pairs give \(c_4-c_1c_3+c_2^2-c_3c_1+c_4\). The degrees of all Chern classes are even, so [DG-CHAR-06 X.5](DG-CHAR-06.md#corollary-x-5) gives \(c_3c_1=c_1c_3\). These two expansions prove (B3). □

**Theorem B.2 (the integral root formula).** Let \(V\) have complex rank \(r\) on a paracompact Hausdorff base. On its complex flag space \(f:F(V)\to B\), write \(f^*V=\bigoplus_{j=1}^r L_j\) and \(t_j=c_1(L_j)\). Then
\[
 f^*p(V_{\mathbb R})=\prod_{j=1}^r(1+t_j^2).
\tag{B5}
\]
The map \(f^*\) is injective on integral cohomology, so this identity determines the integral Pontryagin classes on the base, including their torsion.

**Proof.** The stated flag space, actual line splitting and integral injection are [DG-CHAR-08 M.4](DG-CHAR-08.md#theorem-m-4). Conjugating the splitting gives a splitting into the conjugate lines, since its coordinate matrices and inverse can be conjugated. By B.1 the complexification of the pulled-back real bundle is the direct sum of all \(L_j\) and \(\overline L_j\).

Introduce a formal variable \(u\), used only to count Chern indices. The Chern Whitney and conjugation rules [DG-CHAR-09 B.4](DG-CHAR-09.md#theorem-b-4) and [DG-CHAR-09 B.5](DG-CHAR-09.md#theorem-b-5) give
\[
 \sum_{q=0}^{2r}c_q((f^*V_{\mathbb R})_{\mathbb C})u^q
 =\prod_{j=1}^r(1+t_j u)(1-t_j u)
 =\prod_{j=1}^r(1-t_j^2u^2).
\tag{B6}
\]
All \(t_j\) have even degree and commute. To obtain the coefficient of \(u^{2i}\), choose the nonconstant term from precisely \(i\) of the factors on the right. Its value is
\[
 (-1)^i\sum_{\substack{J\subset\{1,\ldots,r\}\\|J|=i}}\prod_{j\in J}t_j^2.
\]
Definition (A2) cancels this sign. Naturality A.1 identifies the result with \(f^*p_i(V_{\mathbb R})\), and summing over \(i\) proves (B5). For rank zero the products are empty and equal to one. Integral injectivity means that two classes with these pullbacks are equal; no multiplication by two or division by two is involved in descending the identity. □

## C. Projective spaces and spheres

**Lemma C.1 (the stable complex tangent bundle).** For the tautological complex line \(\gamma\) on \(\mathbb CP^n\),
\[
 T\mathbb CP^n\oplus\underline{\mathbb C}
 \cong(\gamma^*)^{\oplus(n+1)}
\tag{C1}
\]
as complex vector bundles.

**Proof.** Give \(\mathbb C^{n+1}\) its usual Hermitian product. The tautological line and its orthogonal complement are smooth subbundles of the trivial bundle, by the projection charts of [DG-CHAR-03 A.1](DG-CHAR-03.md#proposition-a-1) and [DG-CHAR-03 A.2](DG-CHAR-03.md#theorem-a-2). The same tangent calculation identifies the real tangent fibre at a line \(\ell\) with \(\operatorname{Hom}_{\mathbb C}(\ell,\ell^\perp)\). We check its complex structure and its dependence on \(\ell\).

On a projective chart, a line has a unique representative \(u(z)\) whose chosen coordinate is one; its other coordinates are \(z_1,\ldots,z_n\). These are the affine charts of [DG-CHAR-08 R.1](DG-CHAR-08.md#lemma-r-1). Their derivatives on overlaps are complex linear, as proved explicitly for the coordinate quotients in [DG-CHAR-08 R.2](DG-CHAR-08.md#lemma-r-2). Thus they equip the real tangent bundle with its complex scalar action.

For a tangent coordinate \(h\), let \(\dot u\) have zero chosen coordinate and other coordinates \(h\). Set
\[
 A_h(u(z))=(I-P_\ell)\dot u,\qquad
 A_h(\lambda u(z))=\lambda(I-P_\ell)\dot u.
\tag{C2}
\]
This defines a complex-linear map \(\ell\to\ell^\perp\). It is complex linear in \(h\). Replacing the local representative of a varying line by \(\alpha(z)u(z)\) changes its derivative to \(\dot\alpha\,u+\alpha\,\dot u\). Projection kills the first term, and the second is exactly the required rescaling of the input frame. Hence (C2) is independent of the chart and representative. It agrees with the graph tangent map of [DG-CHAR-03 A.1](DG-CHAR-03.md#proposition-a-1): in a graph over \(\ell\), the derivative of a vector with fixed \(\ell\)-component is its orthogonal component.

For additional verification of invertibility, if \(A_h=0\), then \(\dot u\) is a multiple of \(u\). Its chosen coordinate is zero whereas that of \(u\) is one, forcing that multiple and \(h\) to be zero. Given any \(A:\ell\to\ell^\perp\), put \(q=A(u)\) and
\(\dot u=q-q_a u\), where \(a\) is the chosen coordinate. Then \(\dot u_a=0\) and \((I-P_\ell)\dot u=q\), so (C2) maps this tangent coordinate to \(A\). Both this inverse and (C2) vary smoothly, by the smooth projection formula. They therefore give a complex bundle isomorphism
\[
 T\mathbb CP^n\cong\operatorname{Hom}_{\mathbb C}(\gamma,\gamma^\perp).
\tag{C3}
\]

Every complex-linear map \(\ell\to\mathbb C^{n+1}\) splits uniquely by the projections \(P_\ell\) and \(I-P_\ell\). This gives a continuous complex bundle isomorphism
\[
 \operatorname{Hom}_{\mathbb C}(\gamma,\underline{\mathbb C}^{\,n+1})
 \cong
 \operatorname{Hom}_{\mathbb C}(\gamma,\gamma)
 \oplus\operatorname{Hom}_{\mathbb C}(\gamma,\gamma^\perp).
\tag{C4}
\]
The first right-hand summand is the trivial complex line: a scalar \(\lambda\) represents \(\lambda\,\operatorname{id}_\ell\), and its inverse reads that scalar in any line frame, independently of the chosen frame. On the left, taking the \(n+1\) coordinate functionals identifies each Hom space with \(n+1\) copies of \(\ell^*\). These maps and their inverses are coordinate-linear in the Hom bundle charts of [DG-CHAR-01 B.2](DG-CHAR-01.md#theorem-b-2). Substitution of (C3) into (C4), followed by swapping the summand order, proves (C1). The same formulas include \(n=0\), where the tangent bundle has rank zero. □

**Theorem C.2 (Pontryagin classes of complex projective space).** Let \(x=c_1(\gamma^*)\) on \(\mathbb CP^n\). With tangent understood as the underlying real tangent bundle,
\[
 H^*(\mathbb CP^n;\mathbb Z)=\mathbb Z[x]/(x^{n+1}),\qquad
 p(T\mathbb CP^n)=(1+x^2)^{n+1}.
\tag{C5}
\]
Consequently
\[
 p_i(T\mathbb CP^n)=\binom{n+1}{i}x^{2i}.
\tag{C6}
\]
Only degrees \(4i\leq2n\) can be nonzero. For the complex orientation,
\[
 \begin{aligned}
 p(T\mathbb CP^2)&=1+3x^2,&
 \langle p_1(T\mathbb CP^2),[\mathbb CP^2]\rangle&=3,\\
 p(T\mathbb CP^3)&=1+4x^2,&
 p(T\mathbb CP^4)&=1+5x^2+10x^4.
 \end{aligned}
\tag{C7}
\]

**Proof.** [DG-CHAR-09 B.2](DG-CHAR-09.md#theorem-b-2) identifies the first Chern class of a line with the Euler class of its canonically oriented real plane. The tautological line has its ambient Hermitian metric, so [DG-CHAR-08 R.2](DG-CHAR-08.md#lemma-r-2) gives
\[
 x=e((\gamma^*)_{\mathbb R})=-e(\gamma_{\mathbb R}).
\]
The ring and positive evaluation
\(\langle x^n,[\mathbb CP^n]\rangle=1\) are therefore precisely [DG-CHAR-08 R.4](DG-CHAR-08.md#theorem-r-4). The base is compact Hausdorff by [DG-CHAR-08 R.1](DG-CHAR-08.md#lemma-r-1), hence paracompact as in A.4.

Let \(W=(\gamma^*)^{\oplus(n+1)}\). This bundle is already a sum of lines. The computation (B6), directly on this sum on the base itself, gives \(p(W_{\mathbb R})=(1+x^2)^{n+1}\). This uses the integral Chern Whitney formula, not an unrestricted integral real Pontryagin product formula. By C.1, \(W_{\mathbb R}\cong (T\mathbb CP^n)_{\mathbb R}\oplus\underline{\mathbb R}^{\,2}\). Stability in A.1 now proves (C5).

In expanding the \(n+1\) identical factors, a term with \(i\) occurrences of \(x^2\) is specified by an \(i\)-element subset of the factors. There are \(\binom{n+1}{i}\) such subsets, giving (C6). If \(2i>n\), the power \(x^{2i}\) is zero by the ring relation. For \(n=2,3,4\), retaining just the permitted powers gives (C7): the coefficient of \(x^4\) for \(n=4\) is the number of two-element subsets of five elements, namely \(5\cdot4/2=10\). Finally the degree-four class on \(\mathbb CP^2\) evaluates as \(3\langle x^2,[\mathbb CP^2]\rangle=3\). □

**Corollary C.3 (spheres).** Every positive-degree Pontryagin class of \(TS^n\) is zero, for \(n\geq0\).

**Proof.** [DG-CHAR-01 D.2](DG-CHAR-01.md#example-d-2) proves the real bundle isomorphism
\[
 TS^n\oplus\underline{\mathbb R}\cong\underline{\mathbb R}^{\,n+1}.
\tag{C8}
\]
Its maps at \(x\in S^n\) are \((v,t)\mapsto v+tx\) and
\(w\mapsto(w-\langle w,x\rangle x,\langle w,x\rangle)\). A.1 gives stability on the left and vanishing of all positive classes on the right. This includes the rank-zero tangent bundle when \(n=0\). □

## D. The top Euler square

**Theorem D.1 (the integral Euler-square identity).** If \(E\) is an oriented real rank-\(2k\) bundle on any Hausdorff base, with \(k\geq1\), then
\[
 p_k(E)=e(E)^2\quad\hbox{in }H^{4k}(B;\mathbb Z).
\tag{D1}
\]
This equality is unchanged on reversing the orientation of \(E\).

**Proof.** Put \(m=2k\). By A.1, the underlying real bundle of \(E_{\mathbb C}\) is \(E\oplus E\). A local positive frame \(v_1,\ldots,v_m\) of \(E\) is a complex frame of \(E_{\mathbb C}\). Its canonical complex orientation, as in [DG-CHAR-08 R.2](DG-CHAR-08.md#lemma-r-2), is the interleaved real frame
\[
 v_1,iv_1,v_2,iv_2,\ldots,v_m,iv_m.
\tag{D2}
\]
The ordered sum orientation of \(E\oplus E\) is instead
\[
 v_1,\ldots,v_m,iv_1,\ldots,iv_m.
\tag{D3}
\]
Moving \(iv_j\) in (D2) past the later real vectors requires \(m-j\) transpositions. Their total is
\[
 \sum_{j=1}^{m}(m-j)=\frac{m(m-1)}2=k(2k-1).
\tag{D4}
\]
The determinant sign of the permutation is thus \((-1)^k\), by the permutation rule of [DG-CHAR-06 L.1](DG-CHAR-06.md#lemma-l-1). It is the same in every oriented chart.

The metric-free top Chern identity [DG-CHAR-09 B.2](DG-CHAR-09.md#theorem-b-2) and the full Hausdorff Euler product and orientation rules [DG-CHAR-06 T.4](DG-CHAR-06.md#theorem-t-4) give
\[
 \begin{aligned}
 c_{2k}(E_{\mathbb C})
 &=e((E_{\mathbb C})_{\mathbb R}\text{ with complex orientation})\\
 &=(-1)^k e(E\oplus E\text{ with ordered sum orientation})\\
 &=(-1)^k e(E)^2.
 \end{aligned}
\tag{D5}
\]
Multiplying by the sign \((-1)^k\) in (A2) proves (D1). These two earlier theorems require a Hausdorff base but no metric or paracompactness, so neither extra assumption has entered here. Reversing the orientation negates \(e(E)\) by [DG-CHAR-06 T.4](DG-CHAR-06.md#theorem-t-4) and leaves its square unchanged, while \(p_k(E)\) never depended on that orientation. □

## Further reading

Allen Hatcher, *Vector Bundles and K-Theory*, version 2.2, November 2017, [free author PDF](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf), printed page 94: complexification, the definition of Pontryagin classes and Proposition 3.15 relating them to Stiefel–Whitney and Euler classes.
