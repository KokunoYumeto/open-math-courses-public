# Finite type I algebras and expected subalgebras

A finite type I algebra may have matrix blocks of unbounded size. Moreover, a central projection of that algebra need not belong to one of its subalgebras. We prove subalgebra inheritance with both points in view, then apply it to the centralizer of an integrable density.

A projection \(p\) is **abelian** if \(pAp\) is commutative. We call \(A\) type I when every nonzero projection contains a nonzero abelian projection. This is equivalent to requiring the property only for nonzero central projections: given a nonzero projection \(q\), select an abelian \(e\le c(q)\). The carrier test below gives a nonzero element of \(qAe\); its polar factor matches nonzero subprojections of \(e\) and \(q\). The latter is abelian, because the polar factor identifies their corners. Finiteness means that no projection is equivalent to a proper subprojection of itself. It suffices to test the identity: adding \(1-p\) to a proper isometry of \(pAp\) would give a proper isometry of \(A\).

We use the previously proved bounded polar decomposition, projection joins and bounded monotone limits, center of a corner, and central kernels and normal images. The proofs below allow arbitrary Hilbert-space dimensions and arbitrary families of central projections.

## Finite type I algebras have finite matrix pieces

For a projection \(e\), its central carrier \(c(e)\) projects onto \(\overline{AeH}\), as proved in EC05. The space is invariant under both \(A\) and \(A'\), including adjoints, so this projection is central. It is the least central projection above \(e\). For projections \(e,f\), orthogonality of \(\overline{AeH}\) and \(\overline{AfH}\) gives
\[
\begin{gathered}
 eAf=0\\
 \Longleftrightarrow\\
 c(e)c(f)=0.
\end{gathered}
 \tag{FTI.1}
\]
Indeed \(eAf=0\) makes the inner product of \(xe\xi\) and \(yf\eta\) zero for all \(x,y\in A\); the converse follows by inserting the two central carriers. If \(v^*v=e\) and \(vv^*=f\), a central projection annihilates \(e\) exactly when it annihilates \(v\), exactly when it annihilates \(f\). Thus equivalent projections have equal carriers. Partial isometries identify the corresponding corners and preserve abelianness.

**Comparing an abelian projection.** If \(e\) is abelian and \(c(e)\le c(f)\), then \(e\precsim f\). To prove this, choose a maximal family of partial isometries with mutually orthogonal initial projections under \(e\) and mutually orthogonal final projections under \(f\). Zorn's lemma applies, since a union along a chain still has these properties. Finite sums and their adjoints converge strongly: the squared norm of each tail is a sum over orthogonal initial, respectively final, projections. Their limit \(v\in A\) has initial projection \(e_0\le e\) and final projection \(f_0\le f\).

Maximality and polar decomposition give \((e-e_0)A(f-f_0)=0\). Because \(eAe\) is abelian, EC05 says that every projection under \(e\) is a central cut of \(e\). In particular \(e_0\) and \(e-e_0\) have orthogonal central carriers. Put \(z=c(e-e_0)\). Then \(zf_0=0\), since \(c(f_0)=c(e_0)\), and \(z(f-f_0)=0\) by (FTI.1). Hence \(zf=0\). But \(z\le c(e)\le c(f)\), so \(z=0\). Thus \(e_0=e\), and \(v\) proves the comparison. The zero case is included.

**Finding one matrix piece.** Suppose \(A\) is finite and type I. Inside any prescribed nonzero central summand choose a nonzero abelian \(e\), and work in \(Ac(e)\). Thus \(c(e)=1\) for this paragraph. Extend \(e\) to a maximal orthogonal family \((e_i)\) of projections equivalent to it. The family is finite. Otherwise choose countably many of its members. Partial isometries shifting the first to the second, the second to the third, and so on have a strong sum carrying their sum to that sum with the first member removed. This makes a subprojection of the finite identity infinite, a contradiction.

Write the family as \(e_1,\ldots,e_n\), and let \(r=1-\sum_i e_i\). If \(c(r)=1\), the comparison just proved supplies another copy of \(e\) under \(r\), contradicting maximality. Therefore \(z=1-c(r)\ne0\). The projections \(p_i=ze_i\) are nonzero, abelian and mutually equivalent, and sum to \(z\). Choose \(v_i\) with \(v_i^*v_i=p_1\), \(v_iv_i^*=p_i\), and \(v_1=p_1\). Put \(D=p_1Ap_1\), a commutative von Neumann algebra. The maps
\[
\begin{gathered}
 Az\longrightarrow M_n(D),\\
 x\longmapsto(v_i^*xv_j)_{i,j},\\
 (a_{ij})\longmapsto\\
 \sum_{i,j}v_i a_{ij}v_j^*
\end{gathered}
\tag{FTI.2}
\]
are inverse star homomorphisms. The identities \(v_i^*v_j=0\) for \(i\ne j\), \(v_i^*v_i=p_1\), and \(\sum_i v_iv_i^*=z\) check products and both compositions. All sums are finite. Multiplication by fixed bounded operators is normal by CP06, so both maps are normal.

Now take a maximal orthogonal family of nonzero central projections \(z_j\), each with a representation (FTI.2). Their sum is \(1\), since a nonzero central complement would contain another such piece. Central multiplication therefore identifies
\[
\begin{gathered}
 A\cong\prod_{j\in J}M_{n_j}(D_j),\\
 n_j<\infty.
\end{gathered}
 \tag{FTI.3}
\]
The product consists of uniformly bounded families. To see surjectivity, place a given bounded family on its orthogonal central summands; finite partial sums converge strongly to its block operator, which belongs to \(A\) by strong closedness. The index set \(J\) may be uncountable and the integers \(n_j\) need not be uniformly bounded. Finally, every corner of a type I algebra is type I: an abelian projection below a nonzero projection of the corner has the same corner algebra in the original algebra. Corners of a finite algebra are finite by the identity-extension argument in the introduction.

## A polynomial test for subalgebras of one matrix piece

Let \(D\) be commutative and let \(B\subseteq M_n(D)\) be a von Neumann subalgebra, possibly with a smaller identity. Set \(m=n^2+1\). For a permutation \(\sigma\), put \(P_\sigma=x_{\sigma(1)}\cdots x_{\sigma(m)}\). For any algebra define the alternating product
\[
\begin{gathered}
 S_m(x_1,\ldots,x_m)\\
 =\sum_{\sigma\in\mathfrak S_m}
 \operatorname{sgn}(\sigma)P_\sigma.
\end{gathered}
 \tag{FTI.4}
\]
This polynomial vanishes identically on \(M_n(D)\). Each matrix is a \(D\)-linear combination of its \(n^2\) scalar matrix units. Commutativity of \(D\) makes \(S_m\) multilinear over \(D\). On expanding all arguments in those units, every term has a repeated argument. Swapping the two identical arguments pairs summands with opposite signs, giving zero. Thus it vanishes on \(B\) as well.

Suppose a nonzero projection \(r\in B\) contained no nonzero abelian projection of \(B\). Every nonzero corner under \(r\) is then noncommutative. Such a corner contains two nonzero orthogonal equivalent projections: if every projection in it commuted with every element, spectral step approximation would make the corner commutative. Choose a noncentral projection \(p\). Some off-diagonal corner \(pB(r-p)\) is nonzero, after taking an adjoint if needed. The polar factor of a nonzero element matches nonzero subprojections of \(p\) and \(r-p\).

This supplies arbitrarily large finite families of nonzero orthogonal equivalent projections under \(r\). For the induction, split one member into two nonzero equivalent pieces as above, and transport those pieces to every other member by the equivalences. A family of size \(k\) becomes one of size \(2k\). All new corners still have no nonzero abelian projection. Starting with \(r\) and repeating gives enough members for a family of size \(m+1\).

Choose matrix units \((u_{ij})_{1\le i,j\le m+1}\) for that family: with common initial projection \(u_{11}\) and partial isometries \(w_i\) onto the chosen members, take \(u_{ij}=w_iw_j^*\). Put \(x_j=u_{j,j+1}\) for \(1\le j\le m\); then
\[
\begin{gathered}
 S_m(x_1,\ldots,x_m)\\
 =u_{1,m+1}\ne0.
\end{gathered}
 \tag{FTI.5}
\]
Only the listed ordering contributes a nonzero product: adjacent factors must be successive edges of the directed chain \(1\to2\to\cdots\to m+1\), and a permutation using all edges has this property only in that order. This contradicts (FTI.4). Hence every nonzero projection in \(B\) contains a nonzero abelian projection. Thus \(B\) is type I. We have proved the polynomial identity and the consequence actually used, without assuming a general classification theorem for algebras satisfying identities.

## Normal kernels handle ambient central cutoffs

First let \((\pi_j)\) be a family of normal star homomorphisms from a von Neumann algebra \(B\), with type I images, and suppose they jointly separate elements. UB07 proves that each kernel is \(B(1-s_j)\) for a central projection \(s_j\in B\). By UB02, the restriction to \(Bs_j\) is an isometric star isomorphism onto the image. Each image is a von Neumann algebra by the compact-ball argument of UB08: its unit ball is the normal image of the weak-star compact unit ball of \(Bs_j\), hence is ultraweakly closed; the bounded density theorem used there makes it the whole unit ball of the image's bicommutant. For a degenerate representation first restrict to the range of \(\pi_j(1)\); the zero image has \(s_j=0\).

Joint separation gives \(\bigvee_j s_j=1\), since its central complement lies in every kernel. Given a nonzero projection \(q\in B\), some \(qs_j\ne0\). The type I algebra \(Bs_j\) supplies a nonzero abelian projection \(p\le qs_j\). Since \(s_j\) is central, \(pBp=p(Bs_j)p\); hence \(p\) is abelian in \(B\). We have proved
\[
\begin{gathered}
 \text{jointly faithful}\\
 \text{normal}\\
 \text{homomorphisms}\\
 \text{with type I images}\\
 \Longrightarrow B\text{ is type I}.
\end{gathered}
\tag{FTI.6}
\]

Now let \(B\subseteq A\), with \(A\) finite type I. Use (FTI.3). Each coordinate restriction \(\pi_j:B\to M_{n_j}(D_j)\) is a normal star homomorphism. Its image is a von Neumann subalgebra and is type I by FTI02. The coordinate restrictions jointly separate elements, so (FTI.6) proves that \(B\) is type I. It is finite as well: a proper isometry in its identity corner would contradict finiteness of \(A\).

The projections \(z_j\) used to form these coordinate maps belong to \(A\). They need not belong to \(B\). The projections \(s_j\) used to finish the proof are different: they are the central carriers of the normal representations of \(B\), and do belong to \(B\). No assertion that \(z_j\) cuts \(B\) into its own central summands is required.

## An integrable density has a finite type I centralizer

Let \(A\) be type I, let \(\tau\) be a faithful normal semifinite trace on it, and let \(h\in L^1(A,\tau)_+\) have support \(1\). Let \(C\) be the set of elements of \(A\) commuting with every spectral projection of \(h\), and put
\[
\begin{gathered}
 c_k=1_{[1/k,k]}(h),\\
 k\ge1.
\end{gathered}
 \tag{FTI.7}
\]
The algebra \(C\) is a von Neumann algebra, being the intersection of commutants of projections with \(A\). Each \(c_k\) belongs to \(C\) and commutes with all of \(C\), so is central in \(C\). These projections increase strongly to \(1\), since \(h\) is a densely defined positive affiliated operator with zero kernel. The spectral integral gives
\[
\begin{gathered}
 \tau(c_k)\le k\tau(h)\\
 <\infty.
\end{gathered}
 \tag{FTI.8}
\]
The corner \(c_kAc_k\) is type I by FTI01, and its restricted trace is faithful and finite. It is a finite algebra: for \(v^*v=c_k\), \(vv^*\le c_k\), traciality gives \(\tau(c_k-vv^*)=0\), so faithfulness gives \(vv^*=c_k\).

The normal maps \(C\to c_kAc_k\), \(x\mapsto c_kx\), are star homomorphisms because \(c_k\) is central in \(C\). Their images are type I by FTI03, and they jointly separate elements because \(c_k\uparrow1\). Thus (FTI.6) proves that \(C\) is type I.

The functional \(\varphi(x)=\tau(hx)\) is normal and positive by TI06, and is faithful because \(h\) has support \(1\). Explicitly, if \(x\ge0\) and \(\varphi(x)=0\), then the \(L^2\) vector \(x^{1/2}h^{1/2}\) has squared norm \(\tau(h^{1/2}xh^{1/2})=\varphi(x)=0\), by the product and cyclicity identities of TI10. The range of \(h^{1/2}\) is dense, so the bounded operator \(x^{1/2}\) vanishes. On \(C\), this functional is tracial: for \(x,y\in C\), the bounded module products and cyclicity from TI06 give \(\tau(hxy)=\tau(yhx)=\tau(hyx)\). A faithful finite trace excludes a proper isometry, as in the preceding paragraph. Hence \(C\) is finite type I, and every von Neumann subalgebra of \(C\) is type I by FTI03.

Here is the density test used in expectations. If a faithful normal positive functional \(\varphi\) on \(A\) satisfies \(\varphi(nx)=\varphi(xn)\) for all \(n\) in a unital von Neumann subalgebra \(N\) and all \(x\in A\), TI06 supplies a unique positive density \(h\in L^1\). Its kernel projection has zero \(\varphi\)-value, hence is zero. For a unitary \(u\in N\), the assumed identity gives \(\varphi(u^*xu)=\varphi(x)\). Cyclicity and uniqueness of the TI06 density imply \(uhu^*=h\). Unitary transport of spectral projections therefore gives \(u\in C\). The unitary spanning argument BK08 puts all of \(N\) in \(C\), and consequently \(N\) is type I.

## Two checks on the central projections

**There need not be a uniform matrix size.** Take \(A=\prod_{n\ge1}M_n(\mathbb C)\) and \(\tau((x_n))=\sum_n\operatorname{Tr}(x_n)\) on positive elements. Finite coordinate projections show semifiniteness, and positivity of each scalar trace gives faithfulness. This algebra is finite, since an isometry in each finite matrix coordinate is unitary. It is type I: a nonzero projection has a nonzero coordinate, and a rank-one subprojection in that coordinate is abelian. For \(h_n=2^{-n}1_n/n\), the density \(h=(h_n)\) is injective and \(\tau(h)=1\). It is central, so its centralizer is all of \(A\). Its matrix sizes are unbounded. The subalgebra proof accordingly uses the separate identities for the coordinate maps, not one identity for the entire product.

**Ambient central projections can be absent from the subalgebra.** In \(A=M_2(\mathbb C)\oplus M_3(\mathbb C)\), take \(B=\{(\lambda1_2,\lambda1_3):\lambda\in\mathbb C\}\). The ambient central projection \((1_2,0)\) does not belong to \(B\). Both coordinate representations of \(B\) are faithful, so both of their kernel-carrier projections \(s_j\) equal the identity of \(B\). They are not the ambient coordinate projections. This is exactly the distinction used in FTI03.

The matrix-coordinate and abelian-projection arguments are classical. The programme's earlier *Projections and types of von Neumann algebras*, Sections 6, 10 and 13, supplies the comparison background; the required comparison, finite block construction and matrix obstruction have been proved here. Further reading: M. Takesaki, *Theory of Operator Algebras I*, Chapter V, §§1–2.
