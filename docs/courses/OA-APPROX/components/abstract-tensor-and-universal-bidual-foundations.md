# Finite tensor norms and universal biduals

The minimal tensor norm is determined by finite Hilbert-space tests. The Banach bidual is determined by all state coefficients. These two constructions supply the algebraic tensor inclusions and normal extensions needed for infinite tensor products.

The scalar and Hilbert inputs are the retained scalar foundations; the retained coefficient-predual construction supplies the concrete preduals. The linked GNS, cyclic-vector and density proofs use these scalar inputs in the arguments below. Two elementary implications used by those proofs are supplied here explicitly.

<a id="abf-positive-norm-criterion"></a>
## A scalar norm criterion for positivity

Let \(G\) be a bounded functional on a nonzero unital C*-algebra with \(G(1)=\|G\|=c\ge0\). If \(c=0\), then \(G=0\). Otherwise, for \(h=h^*\), write \(G(h)=\alpha+i\beta\). For every real \(t\), scalar calculus and the C*-identity give
\[
 (c-t\beta)^2+t^2\alpha^2=|G(1+ith)|^2
 \le c^2(1+t^2\|h\|^2).
\]
The resulting inequality \(-2ct\beta\le t^2(c^2\|h\|^2-\alpha^2-\beta^2)\), first with \(t>0\) and then with \(t<0\), forces \(\beta=0\). For \(0\le h\le1\), \(\|1-h\|\le1\), so \(|c-G(h)|\le c\). Since \(G(h)\) is real, it is nonnegative. Scaling proves positivity on the entire positive cone. This is the implication required after the positive functional's norm-preserving extension to a forced unitization.

<a id="abf-real-hilbert-closure"></a>
## Weak closure of a real Hilbert subspace

Let \(L\) be a real linear subspace of a real Hilbert space, and let \(Q\) be the orthogonal projection onto its norm closure. If \(w\) lies in its weak closure but \(v=w-Qw\ne0\), the continuous real functional \(x\mapsto(v,x)\) vanishes on \(L\) and has value \(\|v\|^2>0\) at \(w\), a contradiction. Thus its weak and norm closures agree. Applying this to the real subspace \(\{(h\xi_1,\ldots,h\xi_r):h=h^*\in\pi(A)\}\) gives the self-adjoint strong-density step of the linked operator-density proof. Orthogonal projection is the complete Hilbert projection theorem in the scalar foundations. No general convex-separation theorem is needed for this step.

## The minimal tensor norm from finite Hilbert compressions

A finite tensor of C*-algebras can be represented on two independent Hilbert spaces. Its operator norm is determined by finite matrix compressions on either leg. This gives an intrinsic norm before any von Neumann closure or reference state is chosen.

The scalar inputs are continuous C*-calculus, positivity, forced unitization and completion, proved in the scalar foundations. The [scalar GNS and matrix constructions](../scalar-gns-and-matrix-cstar-norms.html#mg01) supply faithful representations at arbitrary cardinality. The Hilbert tensor construction below supplies the complete Hilbert spaces used here. All Hilbert inner products are linear in their second variable.

<a id="mtn-theorem"></a>
### The tensor-norm theorem

Let \(A,B\) be arbitrary complex C*-algebras. They may be nonunital or zero. For faithful *-representations \(\pi:A\to B(H)\) and \(\rho:B\to B(K)\), put
\[
\|z\|_{\min}
=\left\|\sum_{i=1}^m\pi(a_i)\otimes\rho(b_i)\right\|,
\qquad z=\sum_{i=1}^m a_i\odot b_i\in A\odot B.
\]
This is a C*-norm independent of the faithful pair, without any separability or nondegeneracy assumption. It is a cross norm:
\[
\|a\odot b\|_{\min}=\|a\|\,\|b\|.
\]
Its completion is denoted \(A\otimes_{\min}B\). Every spatial tensor representation \(\sigma\odot\tau\), for arbitrary possibly degenerate representations of the two factors, is contractive and extends to this completion. Tensor products of *-homomorphisms are contractive; if both maps are injective, their tensor product is isometric. Finite permutations and regroupings give the canonical isometric *-isomorphisms, and the empty tensor is \(\mathbb C\).

For nonzero unital factors \((A_i)_{i\in I}\), insertion of units gives isometric compatible maps between all finite products. Their directed completion is independent of finite orderings and agrees with regrouping into any disjoint blocks covering \(I\). These last unit-padding assertions require the stated units and nonzero factors.

<a id="mtn-hilbert"></a>
### 1. Hilbert tensors and the faithful algebraic action

The algebraic tensor space is the quotient of the free vector space on pairs by the bilinearity relations. Its universal bilinear property defines all algebraic maps below. On \(H\odot K\), set
\[
\left\langle\sum_i h_i\odot k_i,\sum_j u_j\odot v_j\right\rangle
=\sum_{i,j}\langle h_i,u_j\rangle\langle k_i,v_j\rangle.
\]
The form respects those relations. Expanding the finitely many first coordinates in an orthonormal basis of their span writes a tensor as \(\sum_{r=1}^d e_r\odot w_r\), with squared norm \(\sum_r\|w_r\|^2\). Its coefficients \(w_r\) are recovered by the linear maps induced by \((h,k)\mapsto\langle e_r,h\rangle k\). Thus zero squared norm implies zero tensor. Completing this inner product space gives \(H\otimes K\), with total elementary tensors and
\[
\|h\otimes k\|=\|h\|\,\|k\|.
\]
Only finite orthonormal spans are needed.

For \(S\in B(H)\), the map \(h\odot k\mapsto Sh\odot k\) is bounded: expand over an orthonormal basis of the finite second-coordinate span to get
\[
\left\|(S\otimes I)\sum_r h_r\otimes f_r\right\|^2
=\sum_r\|Sh_r\|^2
\leq\|S\|^2\sum_r\|h_r\|^2.
\]
It therefore extends to \(S\otimes I\). The same argument on the other leg defines \(I\otimes T\). They commute on elementary tensors and hence on the completion. Their product is \(S\otimes T\), with norm at most \(\|S\|\|T\|\). If both Hilbert spaces are nonzero, testing unit elementary vectors whose individual images approach the two norm suprema proves equality. The zero-space cases give the zero operator. Coefficient testing gives
\[
(S\otimes T)^*=S^*\otimes T^*,\qquad
(S\otimes T)(S'\otimes T')=SS'\otimes TT'.
\]
Consequently \(z\mapsto(\pi\odot\rho)(z)\) is an algebraic *-homomorphism.

It is injective when \(\pi,\rho\) are faithful. Write \(z=\sum_{i=1}^m a_i\odot b_i\), with the \(a_i\) linearly independent, by choosing a basis of their finite span and collecting coefficients. For \(\eta,\zeta\in K\), the bounded maps \(R_\zeta h=h\otimes\zeta\) have adjoints \(R_\eta^*(h\otimes k)=\langle\eta,k\rangle h\). Thus a zero represented tensor gives
\[
0=R_\eta^*(\pi\odot\rho)(z)R_\zeta
=\sum_i\langle\eta,\rho(b_i)\zeta\rangle\pi(a_i).
\]
Faithfulness preserves the linear independence. Every coefficient is therefore zero for every pair \(\eta,\zeta\). Hence \(\rho(b_i)=0\), and faithfulness gives \(b_i=0\). This proves injectivity on the algebraic tensor itself, not merely on its image closure. If a factor algebra is zero, its algebraic tensor is zero and the assertion is immediate.

<a id="mtn-matrices"></a>
### 2. The intrinsic matrix C*-norm

We use the following scalar fact, whose complete proof is also in [the faithful representation construction](../scalar-gns-and-matrix-cstar-norms.html#mg03): every algebraic *-homomorphism of C*-algebras is contractive, and every injective one is isometric. Here is the norm argument. A unital *-homomorphism sends algebraic inverses to inverses, so spectral inclusion and scalar C*-calculus give
\[
\|\theta(x)\|^2
=r(\theta(x^*x))\leq r(x^*x)=\|x\|^2.
\]
For nonunital maps, apply this argument to the map between forced unitizations \((x,\lambda)\mapsto(\theta(x),\lambda)\) and restrict to the original closed ideals. No continuity is assumed in obtaining this bound.

If \(\theta\) is injective and \(h\geq0\), suppose \(\|\theta(h)\|<\|h\|\). A continuous function that vanishes on \([0,\|\theta(h)\|]\) and is positive at \(\|h\|\) gives a nonzero \(f(h)\). Contractivity and uniform polynomial approximation give \(\theta(f(h))=f(\theta(h))=0\), contrary to injectivity. The function can be chosen with \(f(0)=0\), so the same proof works in a nonunital algebra. Thus positive norms are preserved; applying this to \(x^*x\) proves isometry for every \(x\).

Choose any faithful representation \(\Gamma:B\to B(L)\), whose existence for arbitrary \(B\) is proved by the scalar norming-state and GNS direct-sum construction. Represent an algebraic matrix \(c=[c_{rs}]\in M_d(B)\), \(d\geq1\), on \(L^d\) by \([\Gamma(c_{rs})]\). Coordinate inclusions and projections give
\[
\max_{r,s}\|c_{rs}\|
\leq\|[\Gamma(c_{rs})]\|
\leq\sum_{r,s}\|c_{rs}\|.
\]
The lower bound uses isometry of \(\Gamma\). Matrix products and adjoints match the entry operations. Entrywise limits of a Cauchy sequence exist in \(B\), and the upper bound shows convergence of the operator matrices to that entrywise limit. Thus this image is a complete C*-algebra. Pulling its norm back defines the C*-norm of \(M_d(B)\).

Any other faithful representation gives another complete C*-matrix algebra by the same two bounds. Entrywise identification is an algebraic *-isomorphism; the scalar isometry result above makes it isometric. More generally, any C*-norm on the algebraic matrix algebra has a C*-completion. The identity from the complete matrix algebra just constructed into that completion is an injective algebraic *-homomorphism, hence isometric. This proves uniqueness even without initially assuming the other norm complete. In particular,
\[
\|[\rho(c_{rs})]\|=\|[c_{rs}]\|_{M_d(B)}
\]
for every faithful \(\rho\), including degenerate representations and arbitrary Hilbert spaces. For \(B=0\), all these spaces of matrix entries are zero. This is precisely the [matrix norm construction](../scalar-gns-and-matrix-cstar-norms.html#mg04).

<a id="mtn-compressions"></a>
### 3. Recovering an operator norm from all finite compressions

Let \(\mathcal F(H)\) be the set of all finite-dimensional subspaces of \(H\), directed by inclusion. It is directed because the span of two finite-dimensional subspaces is finite-dimensional. Let \(P_F\) be orthogonal projection onto \(F\) and put
\[
Q_F=P_F\otimes I_K.
\]
Every elementary finite sum whose first coordinates lie in \(F\) is fixed by \(Q_F\). Totality of such sums, and the bound \(\|Q_F\|\leq1\), give \(Q_F\to I\) strongly on the full \(H\otimes K\). The projection range is the closed copy of \(F\otimes K\): this follows first on elementary tensors and then by density.

For every \(T\in B(H\otimes K)\) and every vector \(v\),
\[
Q_FTQ_Fv-Tv
=Q_FT(Q_Fv-v)+(Q_F-I)Tv\longrightarrow0.
\]
The same calculation for \(T^*\) proves strong-star convergence. If \(M=\sup_F\|Q_FTQ_F\|\), contraction of the projections gives \(M\leq\|T\|\), while the displayed strong limit gives \(\|Tv\|\leq M\|v\|\) for all \(v\). Therefore
\[
\boxed{\ \|T\|=\sup_{F\in\mathcal F(H)}\|Q_FTQ_F\|.\ }
\tag{MTN1}
\]
For \(F\subseteq G\), the smaller compression is a compression of the larger, so their norms also increase. This entire directed set works for nonseparable \(H\); no sequence exhausting \(H\) is required.

<a id="mtn-independence"></a>
### 4. Changing either faithful representation

Fix \(\pi:A\to B(H)\) and two faithful representations \(\rho:B\to B(K)\), \(\rho':B\to B(K')\). For \(z=\sum_i a_i\odot b_i\), set \(T=(\pi\odot\rho)(z)\). For a nonzero finite \(F\subset H\), choose an orthonormal basis \(e_1,\ldots,e_d\). The unitary
\[
F\otimes K\longrightarrow K^d,\qquad
\sum_{s=1}^d e_s\otimes v_s\longmapsto(v_s)_{s=1}^d
\]
identifies the restriction of \(Q_FTQ_F\) with the matrix \([\rho(c^F_{rs})]\), where
\[
c^F_{rs}=\sum_i\langle e_r,\pi(a_i)e_s\rangle b_i\in B.
\tag{MTN2}
\]
It vanishes on the orthogonal complement of its projection range, so the full compressed norm is this matrix norm. The zero subspace gives zero and can be omitted whenever \(H\ne0\). By the intrinsic matrix result and (MTN1),
\[
\|(\pi\odot\rho)(z)\|
=\sup_{F\in\mathcal F(H)}\|[c^F_{rs}]\|_{M_{\dim F}(B)}
=\|(\pi\odot\rho')(z)\|,
\tag{MTN3}
\]
with the zero-dimensional term understood as zero. The compressed operators need not themselves define a representation of \(A\); their entries are simply elements of \(B\), for which the matrix norm has already been constructed.

The Hilbert flip \(h\otimes k\mapsto k\otimes h\) preserves inner products on the total algebraic span, has total range, and extends to a unitary. It conjugates \(\pi(a)\otimes\rho(b)\) to \(\rho(b)\otimes\pi(a)\). Applying (MTN3) after this flip changes the faithful representation of \(A\) as well. Thus every faithful pair gives the same norm. The [faithful algebraic action](#mtn-hilbert) makes it a norm. The *-homomorphism into bounded operators gives the triangle inequality, submultiplicativity, adjoint isometry and C*-identity. Its norm completion is the operator-norm closure of that image, a C*-algebra, and the cross-norm assertion follows from the elementary operator norm and faithful isometry.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 600" role="img" aria-labelledby="mn-title mn-desc">
<title id="mn-title">Finite matrix compressions determine the intrinsic tensor norm</title>
<desc id="mn-desc">All finite dimensional subspaces F of H are directed by inclusion. Compressing the first Hilbert leg gives a matrix over B. Its intrinsic matrix norm is independent of either faithful representation of B. Taking the supremum over all F recovers the entire operator norm.</desc>
<defs><marker id="mn-arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#315f83"/></marker></defs>
<rect x="1" y="1" width="1178" height="598" rx="14" fill="#fff" stroke="#c5d2dc"/>
<g font-family="Segoe UI, Arial, sans-serif" fill="#18384e">
<text x="40" y="45" font-size="26" font-weight="600">An arbitrary Hilbert space is tested on its finite subspaces</text>
<text x="40" y="80" font-size="20">T = Σ π(aᵢ) ⊗ ρ(bᵢ),     Q_F = P_F ⊗ I_K,     d = dim F ≥ 1</text>
<rect x="40" y="125" width="300" height="305" rx="12" fill="#eaf3fa" stroke="#6f9dbb"/>
<text x="60" y="162" font-size="22" font-weight="600">Choose F ⊂ H</text>
<text x="60" y="200" font-size="20">Finite orthonormal basis</text>
<text x="60" y="230" font-size="20">e₁, …, e_d of F</text>
<rect x="75" y="258" width="230" height="65" rx="8" fill="#fff" stroke="#6f9dbb"/>
<text x="105" y="299" font-size="24">F ⊗ K ≅ Kᵈ</text>
<text x="60" y="362" font-size="19">Q_F → I strongly</text>
<text x="60" y="392" font-size="19">for the full directed set</text>
<rect x="395" y="125" width="360" height="305" rx="12" fill="#f0f7ed" stroke="#7ba073"/>
<text x="415" y="162" font-size="22" font-weight="600">The intrinsic matrix over B</text>
<text x="415" y="200" font-size="19">c_rs = Σ ⟨e_r, π(aᵢ)e_s⟩ bᵢ</text>
<path d="M443 234 h-12 v95 h12 M704 234 h12 v95 h-12" fill="none" stroke="#315f83" stroke-width="2"/>
<text x="463" y="261" font-size="23">c₁₁</text><text x="553" y="261" font-size="23">…</text><text x="639" y="261" font-size="23">c₁d</text>
<text x="463" y="291" font-size="23">⋮</text><text x="553" y="291" font-size="23">⋱</text><text x="643" y="291" font-size="23">⋮</text>
<text x="463" y="320" font-size="23">cd₁</text><text x="553" y="320" font-size="23">…</text><text x="638" y="320" font-size="23">cdd</text>
<text x="415" y="362" font-size="19">Q_F T Q_F on F ⊗ K</text>
<text x="415" y="392" font-size="19">is [ρ(c_rs)] on Kᵈ</text>
<rect x="810" y="125" width="330" height="305" rx="12" fill="#fff6e6" stroke="#c3a56a"/>
<text x="830" y="162" font-size="22" font-weight="600">A representation-free norm</text>
<text x="830" y="215" font-size="21">‖[ρ(c_rs)]‖ = ‖[c_rs]‖</text>
<text x="830" y="250" font-size="21">= ‖[ρ′(c_rs)]‖</text>
<text x="830" y="295" font-size="19">ρ and ρ′ are faithful;</text>
<text x="830" y="325" font-size="19">K and K′ are arbitrary.</text>
<text x="830" y="380" font-size="19">MG04 fixes the matrix norm.</text>
<path d="M345 285 H386 M760 285 H801" stroke="#315f83" stroke-width="3" fill="none" marker-end="url(#mn-arrow)"/>
<rect x="40" y="465" width="1100" height="92" rx="10" fill="#edf2f6"/>
<text x="60" y="501" font-size="23">‖T‖ = sup_F ‖Q_F T Q_F‖ = sup_F ‖[c_rs]‖ in M_d(B)</text>
<text x="60" y="536" font-size="19">Proof: finite compressions converge strongly to T; no countable basis is required.</text>
</g></svg>

For each nonzero finite \(F\), the coefficient matrix in (MTN2) is the same for \(\rho\) and \(\rho'\). Its intrinsic norm is supplied by MG04; taking the directed supremum gives (MTN3). The diagram uses \(d=\dim F\), not a prescribed finite dimension.

<a id="mtn-contractivity"></a>
### 5. Arbitrary spatial representations and tensor maps

Let \(\sigma:A\to B(H_0)\) and \(\tau:B\to B(K_0)\) be arbitrary representations. Choose faithful \(\pi:A\to B(H)\), \(\rho:B\to B(K)\). The direct sums \(\sigma\oplus\pi\) and \(\tau\oplus\rho\) are faithful. The coordinate inclusions induce an isometry
\[
J:H_0\otimes K_0\longrightarrow
(H_0\oplus H)\otimes(K_0\oplus K),
\]
by the Hilbert tensor inner-product formula. Elementary-vector testing gives
\[
J^*\big((\sigma\oplus\pi)\odot(\tau\oplus\rho)\big)(z)J
=(\sigma\odot\tau)(z).
\]
Taking norms and using faithful-pair independence gives
\[
\|(\sigma\odot\tau)(z)\|\leq\|z\|_{\min}.
\tag{MTN4}
\]
This includes zero Hilbert spaces and degenerate actions. A bounded map extends uniquely to a completion; continuity of multiplication and involution then makes the extension a *-homomorphism. A faithful pair is isometric, so its extension is faithful. Consequently the norm is also the supremum of all spatial tensor-representation norms, and that supremum is attained by each faithful pair.

For completeness, restricting a representation to its essential space does not alter its operator norms. This space is the closure of \(\pi(A)H\). It is invariant under \(\pi(a)\) and \(\pi(a)^*\); its orthogonal complement is killed, since \(\langle u,\pi(a)v\rangle=\langle\pi(a)^*u,v\rangle=0\) whenever \(v\) lies in that complement. On the essential space the action is nondegenerate: a vector in \(H_{\rm ess}\) orthogonal to \(\pi(A)H_{\rm ess}\) is killed by all adjoints, and therefore belongs to both \(H_{\rm ess}\) and its orthogonal complement. It vanishes. Faithfulness is retained by restriction. If \(A\) is unital, this essential space is the range of \(\pi(1)\), and the restriction is unital. Thus the spatial supremum can also be taken over nondegenerate representations.

Now let \(f:A\to C\) and \(g:B\to D\) be *-homomorphisms. In a faithful spatial pair for \(C,D\), composing with \(f,g\) and applying (MTN4) gives
\[
\|(f\odot g)(z)\|_{C\otimes_{\min}D}\leq\|z\|_{A\otimes_{\min}B}.
\]
It extends to \(f\otimes_{\min}g\). If both maps are injective, these compositions are faithful, so (MTN3) gives equality of norms before completion. Equality passes to the completion, proving isometry. In particular, inclusion of C*-subalgebras and inclusion into forced unitizations remain isometric under minimal tensoring.

<a id="mtn-regrouping"></a>
### 6. Finite regrouping, permutations and empty products

The Hilbert associator
\[
(H\otimes K)\otimes L\longrightarrow H\otimes(K\otimes L),
\qquad (h\otimes k)\otimes\ell\longmapsto h\otimes(k\otimes\ell),
\]
preserves the inner product on elementary triples. Their linear span is dense on both sides, by two applications of Hilbert tensor totality. It therefore extends to a unitary. It intertwines each elementary triple of bounded operators.

Take faithful representations of \(A,B,C\). Their faithful spatial product represents \(A\otimes_{\min}B\) isometrically on \(H\otimes K\). Representing its minimal product with \(C\), and using the associator, gives the same norm on every algebraic triple as representing \(A\otimes_{\min}(B\otimes_{\min}C)\). Algebraic triples are dense in both products: in a finite sum \(\sum_j x_j\otimes c_j\), approximate each \(x_j\in A\otimes_{\min}B\) by algebraic tensors, and use
\[
\left\|\sum_j(x_j-x_j')\otimes c_j\right\|
\leq\sum_j\|x_j-x_j'\|\,\|c_j\|.
\]
The other bracketing has the same density argument. Thus reassociation extends to an onto isometric *-isomorphism.

The Hilbert flip similarly proves the isometric algebra flip. Repeated associators and flips handle every finite regrouping and finite permutation. Any two resulting maps having the same permutation and grouping agree on elementary tensors, a dense set; their extensions therefore agree. This proves the needed compatibility without choosing a permanent ordering. The Hilbert map \(\mathbb C\otimes H\to H\), \(\lambda\otimes h\mapsto\lambda h\), gives \(\mathbb C\otimes_{\min}A=A\) and the corresponding right identity. The empty algebra product is consequently \(\mathbb C\), consistently with all finite regroupings. Zero factors give zero products throughout.

<a id="mtn-padding"></a>
### 7. Units give isometric connecting maps

Let all \(A_i\) be nonzero and unital. A faithful representation restricted to its essential space is faithful and unital on a nonzero Hilbert space. For finite \(F\subseteq G\), choose such representations of all factors in \(G\). After finite regrouping, unit insertion represents a local element by
\[
T\longmapsto T\otimes I_{H_{G\setminus F}}.
\]
The extra finite Hilbert tensor space is nonzero; for an empty extra set it is \(\mathbb C\). The elementary operator norm formula gives \(\|T\otimes I\|=\|T\|\). Faithful-representation independence therefore proves that the algebraic connecting map is isometric for the intrinsic minimal norms, and it extends isometrically to the finite C*-products. It is unital. For \(F=\varnothing\), it is the isometric map \(\lambda\mapsto\lambda1\).

For \(F\subseteq G\subseteq L\), both compositions insert exactly the same units into an elementary tensor, so they agree. These compatible isometric maps define the algebraic directed limit: two local elements represent the same element when their images agree at some common finite stage. Operations are performed at a common stage, and the norm is the norm at any such stage, independent of the choice by isometry. This normed *-algebra satisfies the C*-identity because each stage does. Completion gives
\[
A_I=\bigotimes_{i\in I,\min}A_i,
\qquad A_\varnothing=\mathbb C.
\]
Every local stage embeds isometrically, and their union is dense. A bijection of the index set sends finite elementary tensors to the relabeled ones. Finite permutation isometries and compatibility extend it to the canonical isometric *-isomorphism of directed completions.

The binary construction and its functoriality also apply to nonunital algebras, but the present connecting map requires \(1_{A_i}\) in each added factor. If a factor has no unit, that element is outside the specified algebra. Passing to forced unitizations supplies an isometric inclusion into a different tensor construction; it does not specify these unit-padding maps inside the original nonunital factors.

<a id="mtn-blocks"></a>
### 8. Regrouping into arbitrary disjoint blocks

Suppose \(I=\coprod_{j\in J}I_j\) and keep the nonzero unital hypotheses. Construct each block product \(A_{I_j}\) by the preceding directed limit, allowing empty blocks with value \(\mathbb C\). Then construct \(B_J=\bigotimes_{j\in J,\min}A_{I_j}\).

A finite set \(F\subset I\) meets only finitely many blocks. Finite regrouping identifies \(A_F\) with the product of \(A_{F\cap I_j}\) over those blocks. Their local inclusions into \(A_{I_j}\) are isometric *-homomorphisms; The [tensor-map construction](#mtn-contractivity) makes their finite tensor product isometric. Padding the remaining blocks in the directed system for \(B_J\) is also isometric. These maps are compatible with enlarging \(F\), by elementary-tensor checking. They therefore extend to an isometric *-homomorphism
\[
\Phi:A_I\longrightarrow B_J.
\]
Its range is closed because \(A_I\) is complete.

To prove onto, take a finite block tensor \(x_1\otimes\cdots\otimes x_m\). Approximate each \(x_r\) in its block product by a local \(y_r\), with norms remaining bounded. The telescoping expansion and cross-norm bound give
\[
\left\|\bigotimes_{r=1}^m x_r-\bigotimes_{r=1}^m y_r\right\|
\leq\sum_{r=1}^m
\left(\prod_{s<r}\|y_s\|\right)
\|x_r-y_r\|
\left(\prod_{s>r}\|x_s\|\right).
\]
The right side tends to zero. The local \(y_r\) involve finitely many original indices, whose union is finite, so their tensor lies in \(\Phi(A_I)\). Finite sums of these block tensors are dense in each finite block product, and the finite block products have dense union in \(B_J\). Hence the closed range of \(\Phi\) is all of \(B_J\). This proves arbitrary disjoint-block regrouping, even when the blocks or their index set are infinite. The maps are canonical because their values on all local elementary tensors are specified.

### Source and terms

The finite-compression method and the direct-sum compression argument are presented in Kristin Courtney's freely readable [Tensor Lecture 1](https://kristincourtney.com/wp-content/uploads/2023/04/tensor_lecture_1.pdf), Propositions 2.3–2.7, pages 5–8. The directed finite-subspace argument above applies at arbitrary Hilbert cardinality and includes the complete compression and direct-sum steps. The scalar representation and matrix proofs are linked at their full local arguments.

This exposition and its reproducible inline SVG are dedicated under CC0-1.0 to the extent of any rights held. The human lecture retains its own rights; its free author-hosted availability is not an adaptation licence.


## Universal biduals from state coefficients

Inner products are linear in the second variable. The [scalar GNS and matrix C*-norm proofs](../scalar-gns-and-matrix-cstar-norms.html), [positive functionals and essential cyclic vectors](../positive-functionals-and-essential-cyclic-vectors.html), and [operator density from finite vector tests](../operator-density-foundations.html) provide their full constructions. The retained scalar and concrete-predual foundations prove Hahn–Banach, product compactness, Hilbert representation, and the duality of a concrete von Neumann algebra with its coefficient predual. The [positive approximate-identity construction](../infinite-tensor-products.html#f09) applies to every C*-algebra and every closed ideal used below.

<a id="abf-four-positive-parts"></a>

### Every bounded functional is a state coefficient

We first prove the decomposition needed for the universal representation, before giving the bidual any multiplication. Let \(A\) be a complex C*-algebra, and let \(f\in A^*\) be hermitian. Its restriction \(g\) to the real Banach space \(A_h\) has the same norm: for any \(a\), choose \(|\lambda|=1\) with \(f(\lambda a)=|f(a)|\); then \(h=(\lambda a+(\lambda a)^*)/2\) satisfies \(\|h\|\leq\|a\|\) and \(g(h)=|f(a)|\).

Suppose first that \(A\ne0\) is unital. Its state set \(S\) is weak-star compact. Indeed, embed the closed dual unit ball by evaluation in
\[
 \prod_{a\in A}\{z\in\mathbb C:|z|\leq\|a\|\}.
\]
Each disc is compact. The product is compact by the scalar-foundation ultrafilter proof: a proper filter extends by the maximal principle to an ultrafilter; its image in each compact coordinate converges, and every neighbourhood of the resulting tuple restricts only finitely many coordinates and belongs to that ultrafilter. The closed linearity conditions identify the dual ball, and its coordinate topology is exactly the weak-star topology. Positivity and the equation \(s(1)=1\) are closed conditions in that ball. Conversely those conditions give states, by the positive norm-at-the-unit theorem. This proves the assertion about \(S\).

Restricting states to \(A_h\), form the subset of its real dual
\[
 K=\{\alpha s-\beta t:s,t\in S,
       \ \alpha,\beta\geq0,\ \alpha+\beta\leq1\}.
\]
It is compact, as the continuous image of the compact product of two state sets and the closed coefficient triangle. It is convex: a positive combination of states normalizes to a state whenever its coefficient sum is nonzero; a zero coefficient may use any state. It is symmetric and lies in the real dual unit ball. The state norming proof PCY04 gives
\[
 \sup_{k\in K}k(h)=\sup_{s\in S}|s(h)|=\|h\|,
 \qquad h=h^*.
\]
For completeness, if a real functional \(g_0\) of norm at most one lay outside \(K\), compactness makes \(K\) closed. Some weak-star neighbourhood of \(g_0\), defined by finitely many evaluations \(h_1,\ldots,h_n\), misses \(K\). Hence its evaluation vector \(v\in\mathbb R^n\) is outside the compact convex evaluation image \(C\) of \(K\). Let \(w\in C\) minimize \(\|v-w\|\). For \(u\in C\), the segment from \(w\) to \(u\) belongs to \(C\); expanding its squared distance from \(v\) at parameter \(t\downarrow0\) gives
\[
 \langle v-w,u-w\rangle\leq0.
\]
Thus the real linear functional \(u\mapsto\langle v-w,u\rangle\) strictly separates \(v\) from \(C\). Combining its coefficients with the \(h_j\) gives \(h\in A_h\) with \(g_0(h)>\sup_{k\in K}k(h)=\|h\|\), contradicting \(\|g_0\|\leq1\). Therefore \(K\) is the entire real dual unit ball.

Apply this to \(g/\|f\|\) when \(f\ne0\). It gives positive functionals \(f_+,f_-\) with \(f=f_+-f_-\) and \(\|f_+\|+\|f_-\|\leq\|f\|\). Equality follows from the triangle inequality. For \(f=0\) use two zero functionals. If \(A\) is nonunital, extend \(g\) by real Hahn–Banach to the self-adjoint part of the forced C*-unitization, preserving its norm. Complexification gives a hermitian extension \(F\); the first paragraph proves \(\|F\|=\|g\|\). Decompose \(F\) by the unital case and restrict the positive parts to \(A\). Their norms sum to at most \(\|f\|\), and the triangle inequality again forces equality. The zero algebra is immediate. No bidual product was used.

For arbitrary \(f\in A^*\), write \(f=h_1+ih_2\), where
\[
 h_1(a)=\tfrac12(f(a)+\overline{f(a^*)}),\qquad
 h_2(a)=\tfrac1{2i}(f(a)-\overline{f(a^*)}).
\]
Both are hermitian of norm at most \(\|f\|\). Their decompositions give
\[
 f=\sum_{k=0}^3i^k f_k,\qquad f_k\geq0,\qquad
 \sum_k\|f_k\|\leq2\|f\|.
\]
Put \(\psi=\sum_k f_k\). The complete positive-functional GNS construction PCY03 gives a cyclic, nondegenerate representation \((\pi,H,\xi)\) with \(\psi(a)=\langle\xi,\pi(a)\xi\rangle\) and \(\|\xi\|^2=\|\psi\|\). For every \(a\in A\), scalar Cauchy–Schwarz gives
\[
 |f_k(a)|^2\leq\|f_k\|f_k(a^*a)
 \leq\|f_k\|\psi(a^*a)
 =\|f_k\|\|\pi(a)\xi\|^2.
\]
The functional \(\pi(a)\xi\mapsto f_k(a)\) is consequently well defined and bounded on the dense cyclic span. Hilbert representation gives \(\eta_k\) with \(f_k(a)=\langle\eta_k,\pi(a)\xi\rangle\) and \(\|\eta_k\|\leq\|f_k\|^{1/2}\). Taking \(\eta=\sum_k\overline{i^k}\eta_k\) gives
\[
 f(a)=\langle\eta,\pi(a)\xi\rangle,\qquad
 \|\eta\|\|\xi\|\leq4\|f\|.
\]
For the last bound, \(\|\psi\|\leq2\|f\|\) and finite scalar Cauchy–Schwarz gives \(\sum_k\|f_k\|^{1/2}\leq2(2\|f\|)^{1/2}\). If \(\psi=0\), all four parts and \(f\) vanish. Otherwise normalization to the state \(\psi/\|\psi\|\), with cyclic vector \(\xi/\|\psi\|^{1/2}\), leaves the same representation. Thus every bounded functional is a vector coefficient of one state GNS representation.

<a id="abf-universal-predual"></a>

### Restriction of the universal concrete predual

For \(A\ne0\), take one GNS representation \((\pi_s,H_s,\xi_s)\) for every state \(s\), and set
\[
 H_U=\bigoplus_{s\in S(A)}H_s,\qquad
 \pi_U(a)=\bigoplus_s\pi_s(a),\qquad
 M_U=\pi_U(A)''.
\]
For an arbitrary index set the squared norm of a direct-sum vector is the supremum of its finite component sums. Finite-support vectors are dense: the tail outside a sufficiently large finite set has arbitrarily small squared norm by that supremum. A Cauchy sequence converges in each component, and passage of its Cauchy bound to every finite component sum proves that the resulting family lies in the direct sum and is its norm limit. This proves completeness at arbitrary cardinality.

The componentwise operators have norm at most \(\|a\|\), first on finite-support vectors and then on their completion; their products and adjoints are componentwise. Each summand is nondegenerate by PCY03, so finite-support density makes the direct sum nondegenerate. For \(a\ne0\), PCY04 gives \(\sup_s s(a^*a)=\|a^*a\|\). Testing \(\pi_U(a)\) on the unit cyclic vectors in the corresponding summands yields \(\|\pi_U(a)\|\geq\|a\|\). Thus this representation is faithful and isometric.

Write \((M_U)_*\) for its concrete coefficient predual. The complete concrete-predual proof identifies \(((M_U)_*)^*=M_U\). Normal vector functionals are restrictions of one-term coefficients, and the full predual consists of restrictions of absolutely norm-summable coefficient series. Restriction defines
\[
 R:(M_U)_*\longrightarrow A^*,\qquad
 R(\rho)=\rho\circ\pi_U.
\]
The full contraction-density theorem ODF07 gives, for every \(x\in M_U\), \(\|x\|\leq1\), a net \(a_i\in A\), \(\|a_i\|\leq1\), with \(\pi_U(a_i)\to x\) strongly-star and ultraweakly. Therefore
\[
 \|R(\rho)\|
 =\sup_{\|a\|\leq1}|\rho(\pi_U(a))|
 =\sup_{\|x\|\leq1}|\rho(x)|
 =\|\rho\|.
\]
This argument uses the actual bounded approximation, rather than assuming that the norm of an arbitrary strong-convergent net is bounded.

The map \(R\) is onto: the preceding coefficient construction places every \(f\in A^*\) in one state summand, so a normal vector coefficient on \(M_U\) restricts to \(f\). It is thus a surjective isometry of Banach spaces. This proves surjectivity for all functionals, not only for states.

<a id="abf-bidual-product"></a>

### Transporting the product to the Banach bidual

The correctly directed adjoint is
\[
 U=R^*:A^{**}\longrightarrow M_U.
\]
Since \(R\) is a surjective isometry, \(U\) is a surjective isometry, its inverse is \((R^{-1})^*\), and both maps are continuous for the full weak-star topologies. For the canonical evaluation embedding \(j_A:A\to A^{**}\),
\[
 \rho(U(j_A(a)))=j_A(a)(R\rho)=\rho(\pi_U(a))
\]
for every \(\rho\in(M_U)_*\); hence \(Uj_A=\pi_U\).

Transport the product and involution of \(M_U\) through \(U\). These make \(A^{**}\) a von Neumann algebra, with its original norm and predual \(A^*\), and extend the operations on \(A\). Fixed multiplication is ultraweakly continuous: for a coefficient series, multiplying its operator argument by a fixed \(b\) replaces one vector by \(b\) times that vector, with total coefficient norm bounded by \(\|b\|\) times the original sum. Involution is weak-star continuous as a conjugate-linear map, by swapping the two vectors and conjugating the coefficients. These properties pass through \(U\).

The unit ball of \(j_A(A)\) is weak-star dense in the unit ball of \(A^{**}\), because \(U\) maps those two balls to the corresponding balls in the preceding contraction-density theorem. Scaling gives density of \(j_A(A)\) in all of \(A^{**}\). Any other separately weak-star continuous product extending that of \(A\) agrees with this product: approximate the first variable from \(A\) with the second fixed in \(A\), then approximate the second variable. One-variable density similarly determines the involution. This proves uniqueness without asserting joint weak-star continuity of multiplication.

The predual identification is the original evaluation pairing. If \(f=R\rho\), its normal extension is \(X\mapsto X(f)=\rho(U(X))\), with unchanged norm. If \(f\geq0\), ODF06 approximates each positive contraction in \(M_U\) by \(\pi_U(a_i)\), where \(a_i\in A_+\) are contractions. Its values under \(\rho\) are limits of \(f(a_i)\geq0\); therefore \(\rho\geq0\). No converse theorem equating every order-normal map with an ultraweakly continuous map is an input. If \(A=0\), use zero spaces and zero maps for this entire construction.

<a id="abf-normal-extension"></a>

### Normal extension, its complete image and its unit ball

Let \(\pi:A\to B(K)\) be any *-representation, including a degenerate one, and let \(q\) project onto
\[
 K_0=\overline{\operatorname{span}\{\pi(a)\zeta:a\in A,\ \zeta\in K\}}.
\]
Every \(\pi(a)\) is supported on \(K_0\): it preserves this subspace, its adjoint preserves it, and a vector orthogonal to it is killed by \(\pi(a)\), by testing against \(\pi(a^*)\zeta\). Thus \(\pi(a)=q\pi(a)q\). For any positive contractive two-sided approximate identity \((e_i)\) in \(A\),
\[
 \pi(e_i)\pi(a)\zeta=\pi(e_i a)\zeta\longrightarrow\pi(a)\zeta.
\]
The norm bound \(\|\pi(e_i)\|\leq1\) extends convergence from the dense span to \(K_0\), while every approximant is zero on its orthogonal complement. Hence \(\pi(e_i)\to q\) strongly and ultraweakly. In particular the restricted representation \(\pi_0\) on \(K_0\) is nondegenerate.

The complete finite-vector density proof gives
\[
 N=\overline{\pi(A)}^{\mathrm{uw}}
   =\pi_0(A)''\oplus0\quad\text{on }K_0\oplus K_0^\perp.
\]
Its unit is \(q\). The full ambient bicommutant instead satisfies
\[
 \pi(A)''=N+\mathbb C(1-q).
\]
Indeed every operator commuting with \(\pi(A)\) commutes with its strong-limit support \(q\), and the commutant is \(\pi_0(A)'\oplus B(K_0^\perp)\). Taking its commutant gives the formula. It is a direct sum when \(q\ne1\). The commutant of \(B(K_0^\perp)\) is scalar: commuting with rank-one projections and matrix units forces an operator to be diagonal with equal diagonal entries.

Concrete-predual restriction gives the bounded map
\[
 S:B(K)_*\longrightarrow A^*,\qquad S(\rho)=\rho\circ\pi.
\]
Set \(T=S^*:A^{**}\to B(K)\). This is weak-star-to-ultraweak continuous and satisfies \(Tj_A=\pi\). Density makes it the unique such linear extension. We prove the algebra identities explicitly. For \(a\in A\) and a net \(j_A(b_i)\to Y\), separate continuity gives
\[
 T(j_A(a)Y)
 =\lim_i\pi(ab_i)=\pi(a)T(Y).
\]
Next approximate \(X\) by \(j_A(a_i)\), keeping \(Y\) fixed:
\[
 T(XY)=\lim_i T(j_A(a_i)Y)=T(X)T(Y).
\]
The weak-star continuous involutions and one limit give \(T(X^*)=T(X)^*\). In the universal representation, \(\pi_U(e_i)\to1\) strongly and ultraweakly, so the homeomorphism \(U\) gives \(j_A(e_i)\to1_{A^{**}}\) weak-star. Therefore \(T(1)=q\). Each \(T(X)\) is an ultraweak limit of \(\pi(A)\), so belongs to \(N\).

The image of the closed unit ball of \(A^{**}\) under \(T\) is ultraweakly compact, since that ball is compact by the dual-ball proof above and \(T\) is continuous. In the Hausdorff ultraweak topology it is closed. For every contraction \(x\in N\), ODF07 provides \(a_i\in A\), \(\|a_i\|\leq1\), with \(\pi(a_i)\to x\) ultraweakly. These are \(T(j_A(a_i))\), so closedness puts \(x\) in the image. Conversely \(T\) is contractive, either directly from its adjoint construction or from the C*-homomorphism norm estimate. Thus
\[
 T(B_{A^{**}})=B_N,
 \qquad T(A^{**})=N.
\]
This proves onto-ness for the generated supported algebra. It does not make a unital representation onto an arbitrary target algebra containing its image.

<a id="abf-central-quotient"></a>

### The central quotient and its globally normal inverse

The kernel \(I=\ker T\) is an ultraweakly closed self-adjoint two-sided ideal of \(A^{**}\). Represent this algebra faithfully as \(M_U\), and put \(L=\overline{I H_U}\). Both \(M_U\) and its commutant preserve \(L\) and its orthogonal complement: invariance under \(M_U\) follows from the two-sided ideal property, and invariance under the commutant follows by commuting past elements of \(I\). The projection \(p\) onto \(L\) therefore belongs to the center of \(M_U\). The ideal is norm closed, so its positive contractive approximate identity exists. The essential-space argument of the preceding section makes this approximate identity converge strongly to \(p\). Bounded strong convergence implies ultraweak convergence, and the ultraweak closedness of \(I\) gives \(p\in I\). Each \(x\in I\) is supported on \(L\), hence \(x=px\); conversely \(p\in I\) and the ideal property give \(pM_U\subseteq I\). Consequently \(I=pM_U\). Transporting back and writing \(z=1-p\) gives the unique central projection with
\[
 \ker T=A^{**}(1-z).
\]
Uniqueness follows because the projection onto the closed span of an ideal's ranges is determined by the ideal.

The restriction \(V=T|_{zA^{**}}:zA^{**}\to N\) is an injective onto *-homomorphism. It is isometric by the faithful C*-homomorphism norm theorem; explicitly, a positive element losing norm would have a nonzero continuous spectral cutoff killed by \(V\), contradicting injectivity, and application to \(x^*x\) gives every norm. Multiplication by \(z\) contracts the norm and does not change \(T(X)\), so \(V\) also maps its unit ball onto \(B_N\).

We prove the inverse normal on the entire weak-star spaces. Here is the corner predual explicitly. Write \(B=A^*\), and regard its elements as the normal evaluation functionals on \(A^{**}\). Fixed multiplication by \(z\) is weak-star continuous, so
\[
 (Pf)(X)=f(zX)
\]
defines a bounded projection \(P:B\to B\) of norm at most one. Its kernel is exactly the annihilator of \(zA^{**}\). Its closed range \(E=P(B)\) is isometric to the quotient by this kernel: contraction gives \(\|Pf\|\leq\inf_{k\in\ker P}\|f+k\|\), while \(f-Pf\in\ker P\) gives the reverse inequality. For \(\ell\in E^*\), the functional \(f\mapsto\ell(Pf)\) on \(B\) has the same norm as \(\ell\), because \(P\) maps the unit ball onto the unit ball of its range. It is represented by \(X\in B^*=A^{**}\); its invariance under \(P\) gives \(X=zX\). Conversely evaluation by every \(X=zX\) restricts to \(E\), with the same norm by that unit-ball identity. This proves \(E^*=zA^{**}\) with the original pairing and topology. Restriction of normal functionals gives the preadjoint
\[
 V_*:N_*\longrightarrow E.
\]
Its norm is preserved, since \(V\) maps unit balls onto unit balls. Hence its range is norm closed. If the range were a proper closed subspace of \(E\), Hahn–Banach would give a nonzero \(X\in E^*=zA^{**}\) annihilating it. Every \(\rho\in N_*\) would then vanish on \(V(X)\), forcing \(V(X)=0\); injectivity forces \(X=0\), a contradiction. Thus \(V_*\) is a surjective isometry. Its inverse is bounded and
\[
 V^{-1}=(V_*^{-1})^*
\]
is weak-star continuous globally. Compactness of individual balls was not substituted for this last conclusion. All assertions include zero algebras and zero essential spaces.

For a nondegenerate representation, \(q=1_K\) and \(N=\pi(A)''\). For a degenerate representation, the complementary scalar corner can be present in the ambient bicommutant and is absent from the normal extension's image. For example, \(\pi(\lambda)=\lambda\oplus0\) on \(\mathbb C^2\) has image \(\mathbb C\oplus0\), while its ambient bicommutant is \(\mathbb C\oplus\mathbb C\).

<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="abf-title abf-desc" width="920" height="470" viewBox="0 0 920 470">
<title id="abf-title">The universal bidual and the image of a normal extension</title>
<desc id="abf-desc">Restriction R from the universal concrete predual to A star is an onto isometry. Its adjoint U equals R star, from A double star onto the universal represented algebra. The evaluation embedding j and the normal extension T give pi equals T composed with j. The image is the ultraweak closure N, with unit q, and the supported central restriction V has a globally normal inverse.</desc>
<defs><marker id="abf-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#285d7d"/></marker></defs>
<rect x="1" y="1" width="918" height="468" rx="12" fill="#f7fafc" stroke="#a4b9c8"/>
<g font-family="Arial,sans-serif" fill="#15394f">
<text x="26" y="33" font-size="21" font-weight="bold">A state-coefficient construction determines the whole bidual</text>
<text x="26" y="60" font-size="16">R : (M_U)* → A* is an onto isometry; U = R* : A** → M_U.</text>
<rect x="328" y="82" width="264" height="76" rx="9" fill="#edf4fb" stroke="#285d7d"/>
<text x="460" y="108" text-anchor="middle" font-size="18">M_U = π_U(A)″</text>
<text x="460" y="136" text-anchor="middle" font-size="15">one GNS summand for every state</text>
<rect x="26" y="226" width="184" height="79" rx="9" fill="#edf4fb" stroke="#285d7d"/>
<text x="118" y="254" text-anchor="middle" font-size="20">A</text>
<text x="118" y="282" text-anchor="middle" font-size="15">any C*-algebra</text>
<rect x="328" y="226" width="264" height="79" rx="9" fill="#edf4fb" stroke="#285d7d"/>
<text x="460" y="254" text-anchor="middle" font-size="20">A** with predual A*</text>
<text x="460" y="282" text-anchor="middle" font-size="15">product transported through U</text>
<rect x="710" y="226" width="184" height="79" rx="9" fill="#edf7f1" stroke="#2b7553"/>
<text x="802" y="254" text-anchor="middle" font-size="19">N = closureᵘʷ π(A)</text>
<text x="802" y="282" text-anchor="middle" font-size="15">unit q = P_K₀</text>
<path d="M218 265H319" fill="none" stroke="#285d7d" stroke-width="2" marker-end="url(#abf-arrow)"/>
<text x="268" y="244" text-anchor="middle" font-size="17">j_A</text>
<path d="M600 265H701" fill="none" stroke="#285d7d" stroke-width="2" marker-end="url(#abf-arrow)"/>
<text x="650" y="244" text-anchor="middle" font-size="17">T = S*</text>
<path d="M447 215V168" fill="none" stroke="#285d7d" stroke-width="2" marker-end="url(#abf-arrow)"/>
<path d="M473 168V215" fill="none" stroke="#285d7d" stroke-width="2" marker-end="url(#abf-arrow)"/>
<text x="424" y="196" text-anchor="end" font-size="16">U</text>
<text x="496" y="196" font-size="16">U⁻¹</text>
<path d="M118 315V344H802V315" fill="none" stroke="#285d7d" stroke-width="2" marker-end="url(#abf-arrow)"/>
<text x="460" y="333" text-anchor="middle" font-size="16">π = T j_A</text>
<text x="26" y="379" font-size="16">ker T = (1−z)A**, z central; V : zA** → N is an isometric isomorphism.</text>
<text x="26" y="407" font-size="16">V_* : N_* → (zA**)_* is onto isometry; V⁻¹ = (V_*⁻¹)* is globally normal.</text>
<text x="26" y="435" font-size="15">Degenerate π : π(A)″ = N + ℂ(1−q). The complementary scalar corner is absent from T(A**).</text>
<text x="26" y="456" font-size="14">K₀ = closure span π(A)K; T(B_(A**)) = B_N. Proof: normal extension and central quotient above.</text>
</g></svg>


*Figure.* The triangle commutes because \(Tj_A=\pi\). The onto isometry \(R:(M_U)_*\to A^*\) yields \(U=R^*\). The projection \(q\) acts on the essential Hilbert space, while \(z\) is central in \(A^{**}\). The onto isometry \(V_*\) of the entire preduals proves that the supported inverse is globally normal. The formulas describe the actual maps and unit balls proved above, including the complementary corner for a degenerate representation.

### Reading and terms

Bruce Blackadar's [author-hosted edition of *Operator Algebras*](https://www.bruceblackadar.com/Mathematics/Cycr.pdf) discusses the GNS construction in II.6.4.1–3 and the universal representation, predual restriction and normal extension in III.5.2.1 and III.5.2.5–9. The positive-functional decomposition, arbitrary direct-sum construction, bounded image argument and globally normal inverse are proved in full above. The linked edition retains its own rights. New expression in this component is dedicated under CC0-1.0 to the extent of rights held.
