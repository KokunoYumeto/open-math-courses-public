# The reduced assembly map and the torus class

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The Baum–Connes assembly map compares the topology of a group with the operator algebra of its regular representation. For a countable group \(\Gamma\) and the trivial coefficient algebra, its reduced form is a homomorphism
\[
\mu^r_\Gamma:RK^\Gamma_*(\mathcal E\Gamma)\longrightarrow K_*(C^*_r(\Gamma))
\]
from the equivariant \(K\)-homology with \(\Gamma\)-compact supports of a universal proper \(\Gamma\)-space to the \(K\)-theory of the reduced group \(C^*\)-algebra. The Baum–Connes conjecture asserts that it is an isomorphism; it is stated in [The Baum–Connes assembly map and the conjecture](course:KT-KK/KT-KK-20). For a torsion-free group the domain is the \(K\)-homology with compact supports of a classifying space \(B\Gamma\) [Valette, Section 7.4.1]. This course proves OpenAI's theorem (2026) that the map can fail to be injective, even rationally, for a finitely generated torsion-free group [OpenAI-BCI, Theorem 1.1].

**Theorem 1.1** (OpenAI). There are a finitely generated torsion-free group \(G_{\rm inj}\), an injective homomorphism \(i:\mathbb Z^2\to G_{\rm inj}\) and a class \(c\in H^2(BG_{\rm inj};\mathbb Z)\) with
\[
\begin{gathered}
\bigl\langle(Bi)^*c,[T^2]\bigr\rangle=1,\\
i_*(\beta)=0\ \text{ in }K_0(C^*_r(G_{\rm inj})),
\end{gathered}
\]
where \(\beta\) is a rank-zero Bott generator of \(K_0(C^*_r(\mathbb Z^2))\). In particular, the class \(h\) of the Dirac operator of the torus, induced along \(i\), has infinite order in \(RK_0^{G_{\rm inj}}(\mathcal EG_{\rm inj})\), while \(\mu^r_{G_{\rm inj}}(h)=0\).

Here \(BG\) is the bar model of a group \(G\), \(T^2=\mathbb R^2/\mathbb Z^2\) carries the standard orientation, and the map \(Bi:T^2\to BG_{\rm inj}\) and the class \(h\) are defined in Section 3. In the description of the domain by \(K\)-homology of the classifying space, \(h\) is the class \((Bi)_*[D_{T^2}]\) of [OpenAI-BCI, Section 9.2]; the proof below works with the domain of assembly directly.

- The assembly map and the Bott generator (Section 1).
- The plan of the course (Section 2).
- The torus class (Section 3).
- Proof of the theorem (Section 4).
- Maximal assembly and related results (Section 5).
- Named statements (Section 6).

## 1. The assembly map and the Bott generator

We use the construction of assembly in [The Baum–Connes assembly map and the conjecture](course:KT-KK/KT-KK-20), with its numbering. Let \(G\) be a countable discrete group. A *stage* is a closed \(G\)-compact subspace of the universal proper \(G\)-space of Theorem A.7 there. At a free proper \(G\)-compact space \(X\), assembly is a homomorphism
\[
\mu^r_X:KK^G_*(C_0(X),\mathbb C)\longrightarrow K_*(C^*_r(G)),
\]
natural for proper equivariant maps, \(\mu^r(f_*x)=\mu^r_X(x)\) ((A12) in Theorem A.4), and the domain of \(\mu^r_G\) is the direct limit (U6) over the stages. A free proper \(G\)-compact space maps into a stage by a cutoff map (proof of Theorem A.7), so its classes define classes in the domain. Three further results of that lesson are used.

1. For a free proper \(G\)-compact space \(X\) with compact quotient \(Y\), there is an isomorphism \(\Theta_X\) from \(KK^G_*(C_0(X),\mathbb C)\) to \(KK_*(C(Y),\mathbb C)\) ((Q5)). It is natural: for a proper equivariant map \(f:X\to Z\) of such spaces, with quotient map \(f_0\), \(\Theta_Z(f_*x)=f_{0,*}\Theta_X(x)\). The proof of Theorem A.10 establishes this naturality by pulling a cutoff back along \(f\), an argument that uses only that \(f\) is proper and equivariant.
2. (Theorem A.8, the Mishchenko comparison.) With the Mishchenko bundle \(\mathcal L_X=X\times_GC^*_r(G)\) of \(X\),
\[
\begin{aligned}
&\mu^r_X(x)=[\mathcal L_X]\\
&\quad{}\otimes_{C(Y)\otimes C^*_r(G)}\\
&\quad\bigl(\Theta_X(x)\boxtimes1_{C^*_r(G)}\bigr).
\end{aligned}\tag{1.1}
\]
3. (Proof of Theorem A.10, (R8) and (R10).) For torsion-free \(G\), the canonical trace \(\tau\) of \(C^*_r(G)\) satisfies
\[
\begin{gathered}
\tau_*\bigl(\mu^r_X(x)\bigr)\\
=\bigl\langle[1_Y],\Theta_X(x)\bigr\rangle .
\end{gathered}\tag{1.2}
\]

For \(G=\mathbb Z^2\), the plane \(\mathbb R^2\) with translations is a universal proper space and is itself a cofinal stage ((U8)), and assembly is an isomorphism (Theorem A.9).

By Lemma 1.1 of [Compact Bott projections and spreading](compact-bott-projections-and-spreading.md), continuous functions \(F\) on \(\mathbb T^2=(\mathbb R/\mathbb Z)^2\), with coordinates \((\vartheta,\xi)\), act as \(F(\lambda(z),\lambda(x))\) in \(C^*_r(\langle z,x\rangle)\), with \(e^{2\pi i(c\vartheta+n\xi)}\) acting as \(\lambda(z^cx^n)\). Composed with the isomorphism \(\mathbb Z^2\to\langle z,x\rangle\) that sends the ordered basis to \((z,x)\), this identifies \(C^*_r(\mathbb Z^2)\) with \(C(\mathbb T^2)\), the canonical trace becoming the integral. In the lesson [Commutative and noncommutative tori](course:KT-OPK/commutative-and-noncommutative-tori), Corollary 3.7 with parameter \(a=0\), generators \(U=e^{2\pi i\vartheta}\), \(V=e^{2\pi i\xi}\) and derivations \(\delta_1=\partial_\vartheta\), \(\delta_2=\partial_\xi\) shows that
\[
\begin{gathered}
K_0(C(\mathbb T^2))\to\mathbb Z^2,\\
x\mapsto\bigl(\tau_*(x),\kappa(x)\bigr),
\end{gathered}\tag{1.3}
\]
is an isomorphism, where on a smooth projection the Chern number is
\[
\kappa(p)=\frac1{2\pi i}\int_{\mathbb T^2}\operatorname{Tr}\bigl(p\,[\partial_\vartheta p,\partial_\xi p]\bigr)\,d\vartheta\,d\xi .
\]
A *rank-zero Bott generator* is a class \(\beta\) with \(\tau_*(\beta)=0\) and \(\kappa(\beta)=\pm1\). By (1.3) there are exactly two, and they differ by sign.

**Lemma 1.1** (the Bott class of the course). For a height \(k\), let \(\mathsf p_k\) be the scaled projection (3.1) of [Compact Bott projections and spreading](compact-bott-projections-and-spreading.md), and let \(e=\operatorname{diag}(0,1)\), written \(e_\infty\) there. The class \(\beta=[\mathsf p_k]-[e]\), which is the class \(\beta\) of (1.2) of [Carriers, trimming and constant extraction](carriers-trimming-and-constant-extraction.md) and does not depend on \(k\), is the rank-zero Bott generator with \(\kappa(\beta)=1\).

*Proof.* Both \(\mathsf p_k\) and \(e\) have trace one at every point, so \(\tau_*(\beta)=0\), and \(\kappa(e)=0\) because \(e\) is constant. On the chart, \(\mathsf p_k(\vartheta,\xi)=p(t,u)\) with \((t,u)=(Z_k(\vartheta-\alpha),N_k\xi)\); outside the chart \(\mathsf p_k=e\) has zero derivatives. Then \(\partial_\vartheta\mathsf p_k=Z_k\,\partial_tp\) and \(\partial_\xi\mathsf p_k=N_k\,\partial_up\), and the substitution has Jacobian \(Z_kN_k>0\), so
\[
\begin{aligned}
\kappa(\mathsf p_k)&=\frac1{2\pi i}\int_{\mathbb R^2}\operatorname{Tr}\bigl(p\,[\partial_tp,\partial_up]\bigr)\,dt\,du\\
&=1
\end{aligned}
\]
by (2.2) of the lesson on compact Bott projections, which is computed with the orientation \(dt\wedge du\). \(\square\)

## 2. The plan of the course

The group is built in three stages, and each stage serves both conclusions of the theorem.

1. **A labelled tower** (lessons [Streams, coefficient pools and universal corrections](streams-coefficient-pools-and-universal-corrections.md) to [Thetas and the pruned old graph](thetas-and-the-pruned-old-graph.md)). An infinite layered graph whose vertices are bit strings and whose edges are solutions of triangular equations; two incident labels recover a vertex block by block, so long words occur once; random permutation tables make every layer incidence expand with a uniform gap; and a first-moment count removes short cycles and short bicycles. By [The Heisenberg group and its laws](the-heisenberg-group-and-its-laws.md), short closed paths are then not laws in the Heisenberg group \(\mathsf H\).
2. **Voltages and symbols** (lessons [Compact Bott projections and spreading](compact-bott-projections-and-spreading.md) to [Polynomial avoidance, norm tests and moments](polynomial-avoidance-norm-tests-and-moments.md)). Every edge receives a voltage in \(\mathsf H\) and a matrix weight, drawn so that short closed walks lift to open walks and every weighted incidence is close, in the full regular norm, to a spread Bott symbol of the torus \(\langle z,x\rangle\).
3. **The group and the two conclusions** (lessons [The private completion and the graphical group](the-private-completion-and-the-graphical-group.md) to [Parity cancellation and the finite witness](parity-cancellation-and-the-finite-witness.md)). Imposing the closed walks of the covering graph as relators gives a torsion-free group \(\Gamma\) containing \(\mathsf H\), with an integral class detecting the torus; disjoint domains in its sheets carry the Bott symbols into the reduced group algebra, where a swindle in finitely many steps, carried out on bounded families of symbols, kills the Bott class; a finite witness gives a finitely generated subgroup.

## 3. The torus class

Let \(D_{T^2}\) be the Dirac operator of the flat torus \(T^2=\mathbb R^2/\mathbb Z^2\) with periodic spinors, written \(D_2\) in Section 6.3 of [The Baum–Connes assembly map and the conjecture](course:KT-KK/KT-KK-20), and \([D_{T^2}]\in KK_0(C(T^2),\mathbb C)\) its class. It is the operator of the flat torus in [Dirac classes and the cotangent Dolbeault element](course:KT-KK/KT-KK-15), whose scalar index \(\langle[1],[D_{T^2}]\rangle\) is computed there to be zero.

For a countable group \(G\) and an injective homomorphism \(i:\mathbb Z^2\to G\), let
\[
X_i=G\times_{\mathbb Z^2}\mathbb R^2 ,
\]
the quotient of \(G\times\mathbb R^2\) by \(n\cdot(g,p)=(g\,i(n)^{-1},p+n)\), with \(G\) acting on the first factor from the left. It is a disjoint union of planes indexed by \(G/i(\mathbb Z^2)\), a free proper \(G\)-compact space with \(X_i/G=T^2\). Put
\[
x_i=\Theta_{X_i}^{-1}[D_{T^2}]\in KK^G_0(C_0(X_i),\mathbb C),
\]
and let \(h_i\) be its class in the domain of \(\mu^r_G\). For \(G=\mathbb Z^2\) and the identity, \(X=\mathbb R^2\), and we write \(h_0\) for this class.

Triangulate \(\mathbb R^2\) by the unit squares, each cut by its diagonal from \((u,v)\) to \((u+1,v+1)\), with the vertices of every triangle ordered by increasing coordinates; translations preserve this. The *grid map* \(\phi_i:X_i\to EG\) is the \(G\)-equivariant simplicial map to the bar model (Section 6) sending the vertex \((g,(u,v))\) to \(g\,i(u,v)\), and each ordered triangle to the corresponding ordered simplex. Its quotient is a map
\[
Bi:T^2\longrightarrow BG ,
\]
which is the composite of the grid map of the torus into \(B\mathbb Z^2\) with the cellular map induced by \(i\). For \(i\) sending the ordered basis to \((z,x)\), Lemma 3.1 of [Cone chains, torsion-freeness and the integral detector](cone-chains-torsion-freeness-and-the-integral-detector.md) shows that it carries the fundamental class to the bar cycle \([z|x]-[x|z]\).

**Lemma 3.1** (assembly of the torus). \(\mu^r_{\mathbb Z^2}(h_0)=\varepsilon\beta\) for a sign \(\varepsilon\in\{1,-1\}\).

*Proof.* By (U8), assembly for \(\mathbb Z^2\) is defined on \(KK^{\mathbb Z^2}_0(C_0(\mathbb R^2),\mathbb C)\), and by Theorem A.9 and (Q5) of [The Baum–Connes assembly map and the conjecture](course:KT-KK/KT-KK-20), \(\mu^r_{\mathbb R^2}\circ\Theta_{\mathbb R^2}^{-1}\) is an isomorphism from \(KK_0(C(T^2),\mathbb C)\) onto \(K_0(C^*_r(\mathbb Z^2))\). By Lemma A.9a there, \(KK_0(C(T^2),\mathbb C)\) is free with basis \(\epsilon\boxtimes\epsilon\) and \(d\boxtimes d\), where \(\epsilon\) (written \(e\) there) is the class of evaluation at \(1\) on the circle and \(d\) the class of the circle Dirac operator, and by (T3) there \([D_{T^2}]=-d\boxtimes d\). So \(\epsilon\boxtimes\epsilon\) and \([D_{T^2}]\) form a basis. The class \(\epsilon\boxtimes\epsilon\) is the class of evaluation at a point, so \(\langle[1],\epsilon\boxtimes\epsilon\rangle=1\), while \(\langle[1],[D_{T^2}]\rangle=0\). By (1.2), in the coordinates (1.3) the images of the two basis elements are \((1,k')\) and \((0,k)\) for some integers \(k,k'\). These images form a basis of \(\mathbb Z^2\), so the determinant \(k\) is \(\pm1\), and \(\mu^r_{\mathbb Z^2}(h_0)=(0,\pm1)=\pm\beta\) by Lemma 1.1. \(\square\)

The sign depends on orientation and grading conventions and is not used. Lemma 3.1 is the full-torus case of the assembly formula of Emerson and Hudson for subtori, in which the dual subtorus is a point [EH, Theorem 1.3]; here it follows from the lattice assembly isomorphism.

**Lemma 3.2** (induction along a subgroup). Let \(i:\mathbb Z^2\to G\) be injective and \(j:C^*_r(\mathbb Z^2)\to C^*_r(G)\) the induced inclusion. Then
\[
\mu^r_G(h_i)=j_*\bigl(\mu^r_{\mathbb Z^2}(h_0)\bigr).
\]

*Proof.* Write \(A=C^*_r(\mathbb Z^2)\), \(B=C^*_r(G)\), \(y=[D_{T^2}]\). The Mishchenko bundle of \(X_i\) is
\[
\begin{gathered}
X_i\times_GB\cong\mathbb R^2\times_{\mathbb Z^2}B\\
\cong\bigl(\mathbb R^2\times_{\mathbb Z^2}A\bigr)\otimes_jB ,
\end{gathered}
\]
where the first map restricts to the plane of the identity coset, and the second sends \(([p,a],b)\) to \([p,j(a)b]\): the balancing relations and the fibrewise inner products agree because \(j\) sends each group unitary of \(\mathbb Z^2\) to the group unitary of its image, and local trivializations give dense range. On section modules this says \([\mathcal L_{X_i}]=(\mathrm{id}\otimes j)_*[\mathcal L_{\mathbb R^2}]\) in \(KK(\mathbb C,C(T^2)\otimes B)\). The cycles \((\mathrm{id}\otimes j)^*(y\boxtimes1_B)\) and \(j_*(y\boxtimes1_A)\) are unitarily equivalent: if \(y\) is represented by \((H,\pi,F)\), both are \(H\otimes B\) with the action \(\pi\otimes j\) and the operator \(F\otimes1\), the second through \((\xi\otimes a)\otimes b\mapsto\xi\otimes j(a)b\). By (1.1) for both groups and the naturality identities of Proposition 5.1 of [Homotopy, associativity, the index pairing and KK-equivalence](course:KT-KK/KT-KK-10),
\[
\begin{gathered}
\mu^r_G(h_i)=(\mathrm{id}\otimes j)_*[\mathcal L_{\mathbb R^2}]\otimes(y\boxtimes1_B)\\
=[\mathcal L_{\mathbb R^2}]\otimes(\mathrm{id}\otimes j)^*(y\boxtimes1_B)\\
=[\mathcal L_{\mathbb R^2}]\otimes j_*(y\boxtimes1_A)\\
=j_*\bigl([\mathcal L_{\mathbb R^2}]\otimes(y\boxtimes1_A)\bigr)=j_*\bigl(\mu^r_{\mathbb Z^2}(h_0)\bigr).
\end{gathered}
\]
The first equality also uses (A12) for the cutoff map that defines \(h_i\). \(\square\)

**Lemma 3.3** (maps into the bar model). Let \(G\) be a countable torsion-free group.

1. Every stage \(Z\) admits a continuous \(G\)-map \(F:Z\to EG\).
2. For every injective homomorphism \(i:\mathbb Z^2\to G\), any two continuous \(G\)-maps \(X_i\to EG\) are \(G\)-homotopic. In particular, the quotient map \(T^2\to BG\) of every continuous \(G\)-map \(X_i\to EG\) is homotopic to \(Bi\).

*Proof.* (1) The action on \(Z\) is free, since finite stabilizers of a torsion-free group are trivial, and \(Z\) is proper and \(G\)-compact (Lemma A.7b of [The Baum–Connes assembly map and the conjecture](course:KT-KK/KT-KK-20)). The proof of Lemma A.10a there gives a continuous \(G\)-map from \(Z\) into the join of finitely many copies of \(G\), a simplicial complex whose simplices have at most one vertex \((\gamma,k)\) for each tag \(k\). Order the vertices of every simplex by their tags; tags are \(G\)-invariant, so this order is preserved by \(G\) and by passage to faces. The map sending a simplex with vertices \((\gamma_0,k_0),\ldots,(\gamma_n,k_n)\), \(k_0<\cdots<k_n\), linearly onto the simplex \((\gamma_0,\ldots,\gamma_n)\) of \(EG\) is therefore a continuous \(G\)-map from the join to \(EG\); compose.

(2) Let \(F',F''\) be the two maps. The cells \(\sigma\times\{0\}\), \(\sigma\times\{1\}\) and \(\sigma\times(0,1)\), for the open simplices \(\sigma\) of \(X_i\), make \(X_i\times[0,1]\) a CW complex on which \(G\) permutes the cells freely. Put \(H=F'\) on \(X_i\times\{0\}\) and \(H=F''\) on \(X_i\times\{1\}\). Choose one cell in each \(G\)-orbit of cells \(\sigma\times(0,1)\) and treat them in order of increasing dimension of \(\sigma\). The boundary of \(\sigma\times[0,1]\) is a sphere on which \(H\) is already defined and continuous, and \(EG\) is contractible (statement (BG)), so \(H\) extends continuously over \(\sigma\times[0,1]\); extend it to the other cells of the orbit by \(H(gw)=gH(w)\), which is consistent because \(G\) acts freely on cells and \(H\) is already equivariant on the boundaries. The resulting \(H\) is continuous on every closed cell, hence continuous, and it is a \(G\)-homotopy from \(F'\) to \(F''\). Its quotient is a homotopy of the quotient maps. The second assertion follows by taking \(F''=\phi_i\). \(\square\)

**Lemma 3.4** (detection). Let \(G\) be a countable torsion-free group, \(i:\mathbb Z^2\to G\) injective and \(c\in H^2(BG;\mathbb Z)\) with \(\langle(Bi)^*c,[T^2]\rangle=\pm1\). Then \(h_i\) has infinite order in \(RK_0^G(\mathcal EG)\).

*Proof.* By statement (LB) there is a complex line bundle \(L\) on \(BG\) with first Chern class \(c\). Suppose that \(Nh_i=0\) for some \(N\ge1\). A class that vanishes in a direct limit vanishes at some stage, so there are a stage \(Z\) and a proper \(G\)-map \(\iota:X_i\to Z\), a cutoff map followed by an inclusion of stages, with \(N\iota_*x_i=0\) in \(KK^G_0(C_0(Z),\mathbb C)\). Let \(F:Z\to EG\) be given by Lemma 3.3(1), with quotient map \(F_0:Z/G\to BG\). Its image is compact, so it lies in a finite subcomplex \(K\) [Hatcher, Proposition A.1]. Let \(a\in K_0(C(Z/G))\) be the image of \([L|_K]-[1]\) under \(F_0^*:C(K)\to C(Z/G)\), and define a homomorphism
\[
\begin{gathered}
\psi:KK^G_0(C_0(Z),\mathbb C)\to\mathbb Z,\\
\psi(w)=a\otimes_{C(Z/G)}\Theta_Z(w).
\end{gathered}
\]
By the naturality of \(\Theta\) (item 1 of Section 1), \(\Theta_Z(\iota_*x_i)=\iota_{0,*}[D_{T^2}]\) for the quotient map \(\iota_0:T^2\to Z/G\). Proposition 5.1 of [Homotopy, associativity, the index pairing and KK-equivalence](course:KT-KK/KT-KK-10), applied to the homomorphism \(\iota_0^*\), moves the pull-back to the \(K\)-theory class, and the module of sections of a pulled-back bundle is the pulled-back module of sections. With \(f=F_0\circ\iota_0\),
\[
\psi(\iota_*x_i)=\bigl([f^*L]-[1]\bigr)\otimes_{C(T^2)}[D_{T^2}] .
\]
By statement (IND) this is \(\varepsilon_D\langle c_1(f^*L),[T^2]\rangle=\varepsilon_D\langle f^*c,[T^2]\rangle\), with a sign \(\varepsilon_D\in\{1,-1\}\), using the naturality of \(c_1\) in (LB). The map \(f\) is the quotient of the \(G\)-map \(F\circ\iota:X_i\to EG\), so it is homotopic to \(Bi\) by Lemma 3.3(2), and \(\psi(\iota_*x_i)=\pm1\). But \(N\psi(\iota_*x_i)=\psi(N\iota_*x_i)=0\), a contradiction. \(\square\)

## 4. Proof of the theorem

The constructions of the course give a sequence of graphical groups \(\Gamma_\nu\), each containing \(\mathsf H\) (Proposition 5.1 of [The private completion and the graphical group](the-private-completion-and-the-graphical-group.md)).

*The detector.* By Proposition 5.1 of [Cone chains, torsion-freeness and the integral detector](cone-chains-torsion-freeness-and-the-integral-detector.md), every \(\Gamma_\nu\) is torsion-free, the homomorphism \(i_\nu:\mathbb Z^2\to\Gamma_\nu\) sending the ordered basis to \((z,x)\) is injective, and there is \(c_\nu\in H^2(B\Gamma_\nu;\mathbb Z)\) with \(\langle(Bi_\nu)^*c_\nu,[T^2]\rangle=-1\).

*The vanishing.* By Proposition 5.2 of [Parity cancellation and the finite witness](parity-cancellation-and-the-finite-witness.md), for all large \(\nu\) the image of the class \(\beta\) of Lemma 1.1 is zero in \(K_0(C^*_r(\Gamma_\nu))\). Fix such a \(\nu\) and a height \(k\); then \([\mathsf p_k]=[e]\) in \(K_0(C^*_r(\Gamma_\nu))\), for these projections in \(M_2(C^*_r(\langle z,x\rangle))\). By Lemma 5.3 there, applied to \(H=\mathsf H\) (generated by \(x\) and \(y\)) and these two projections, there is a finitely generated subgroup \(\mathsf H\le G_{\rm inj}\le\Gamma_\nu\) in which the equality already holds. As a subgroup of \(\Gamma_\nu\), \(G_{\rm inj}\) is torsion-free. Let \(i:\mathbb Z^2\to G_{\rm inj}\) send the ordered basis to \((z,x)\), and let \(c\) be the pull-back of \(-c_\nu\) along the cellular map \(BG_{\rm inj}\to B\Gamma_\nu\) induced by the inclusion. The grid map of \(i_\nu\) is the grid map of \(i\) followed by the inclusion of bar models, so
\[
\bigl\langle(Bi)^*c,[T^2]\bigr\rangle=1,\qquad i_*(\beta)=0 .
\]
This proves the first assertion.

*The class \(h\).* Let \(h=h_i\). By Lemma 3.4, \(h\) has infinite order, so its image in \(RK_0^{G_{\rm inj}}(\mathcal EG_{\rm inj})\otimes\mathbb Q\) is nonzero (Exercise 7.2). By Lemmas 3.2 and 3.1,
\[
\mu^r_{G_{\rm inj}}(h)=j_*(\varepsilon\beta)=\varepsilon\,i_*(\beta)=0 ,
\]
integrally. So reduced assembly for \(G_{\rm inj}\) is not injective, even after tensoring with \(\mathbb Q\). \(\square\)

The first assertion is proved in the programme from the statements (BG) and (CC) of Section 6. The deduction of infinite order also uses (LB) and (IND); the vanishing of \(\mu^r(h)\) uses only results of the programme.

## 5. Maximal assembly and related results

Let \(\mu^{\max}_G\) be assembly with values in the full group \(C^*\)-algebra and \(\lambda_G:C^*(G)\to C^*_r(G)\) the regular quotient; then \(\mu^r_G=(\lambda_G)_*\mu^{\max}_G\) ((A14) in Theorem A.4 of [The Baum–Connes assembly map and the conjecture](course:KT-KK/KT-KK-20)). Hanke and Schick proved that maximal assembly does not vanish on a class whose homological Chern character pairs nontrivially with the subring of rational cohomology generated in degrees at most two [HS, Theorem 1.2]. The class \(h\) and all its nonzero multiples are such classes, by statement (HS) below, so
\[
\begin{gathered}
\mu^{\max}(h)\otimes1\ne0,\\
(\lambda_{G_{\rm inj}})_*\bigl(\mu^{\max}(h)\bigr)=0 :
\end{gathered}
\]
maximal assembly detects \(h\), and the regular quotient kills its image [OpenAI-BCI, Section 1.2]. The name strong Novikov conjecture is used for both the maximal and the reduced rational injectivity. In the reduced form stated by Valette, it asserts that \(K_*(BG)\to K_*(C^*_r(G))\), the map to the domain of assembly followed by reduced assembly, is rationally injective [Valette, Conjecture 7.19]; for torsion-free \(G\) the first map identifies the two domains, and Theorem 1.1 is a counterexample. It disproves neither maximal rational injectivity nor the classical Novikov conjecture on higher signatures, which is known for the higher signatures of classes in that subring [HS, Corollary 1.3]. The group \(G_{\rm inj}\) is finitely generated; the construction gives neither finite presentation nor exactness.

Earlier counterexamples concern assembly with coefficients. Higson, Lafforgue and Skandalis found failures of surjectivity for discrete groups with suitable commutative coefficient algebras, and graphical constructions of Osajda together with a coefficient result of Willett and Yu give a coefficient algebra for which reduced assembly is injective and not surjective [OpenAI-BCI, Section 1.1]. For a torsion-free group, a nontrivial projection in \(C^*_r(G)\) would obstruct surjectivity of coefficient-free assembly (Theorem A.10 of [The Baum–Connes assembly map and the conjecture](course:KT-KK/KT-KK-20)). The companion course [A projection of irrational trace and the Baum–Connes conjecture](course:irrational-trace-and-baum-connes/traces-of-projections-and-the-baum-connes-conjecture) treats OpenAI's projection of irrational trace, and [A torsion-free counterexample to the Kadison–Kaplansky conjecture](course:kadison-kaplansky-projections/the-conjecture-and-scalar-compression) its torsion-free projection; the present course uses the same architecture of labelled towers, voltage covers and sheets.

## 6. Named statements

Van Kampen diagrams and plane maps, the statements (VK) and (MAP) of Section 3 of [Graphical presentations and coned diagrams](course:irrational-trace-and-baum-connes/graphical-presentations-and-coned-diagrams#3-diagrams), are used in the lessons on the graphical group and on polygons through sheets; they are proved in the course [Van Kampen diagrams](course:van-kampen-diagrams/van-kampens-lemma). The following standard statements are used without proof in the programme; they are open obligations of this course.

- **(BG)** and **(CC)**: the bar model \(EG\) of a group \(G\) is a contractible \(\Delta\)-complex on which \(G\) acts freely, with quotient \(BG\) a \(K(G,1)\), functorial in \(G\); and cellular cohomology computes singular cohomology [Hatcher, Example 1B.7, Theorems 1B.8 and 3.5]. They are stated in full in [Cone chains, torsion-freeness and the integral detector](cone-chains-torsion-freeness-and-the-integral-detector.md).
- **(LB)**: on a CW complex, the first Chern class \(c_1\) is a bijection from isomorphism classes of complex line bundles onto \(H^2(-;\mathbb Z)\) [Hatcher-VB, Proposition 3.10], natural under pull-back [Hatcher-VB, Theorem 3.2]; and over a compact Hausdorff space a vector bundle is a direct summand of a trivial bundle [Hatcher-VB, Proposition 1.4], so its module of continuous sections is finitely generated projective and defines a class in \(K_0\).
- **(IND)**: for every complex line bundle \(E\) on \(T^2\), the index pairing \(([E]-[1])\otimes_{C(T^2)}[D_{T^2}]\), an element of \(KK_0(\mathbb C,\mathbb C)=\mathbb Z\), equals \(\varepsilon_D\langle c_1(E),[T^2]\rangle\), with a sign \(\varepsilon_D\in\{1,-1\}\) fixed by the orientation and grading conventions of \(D_{T^2}\) and independent of \(E\). This is the case of the torus in the index theorem of Atiyah and Singer for Dirac operators twisted by vector bundles [AS], [BvE, Theorem 1]: the index of \(D_{T^2}\) twisted by \(E\) is \((\operatorname{ch}(E)\operatorname{Td}(T^2))[T^2]\), the Todd class of the flat torus with its trivial \(\mathrm{spin}^c\) structure is \(1\), \(\operatorname{ch}(E)=1+c_1(E)\) on a surface, and the index pairing with \([E]\) is the index of the twisted operator.
- **(HS)**: the theorem of Hanke and Schick [HS, Theorem 1.2], together with the computation that the degree-two part of the homological Chern character of \(h\) is \(\pm(Bi)_*[T^2]\), on which \(c\) takes the value \(\pm1\); used only in Section 5.

## 7. Exercises

**Exercise 7.1.** Show that the rank-zero Bott generators are exactly the two generators of the subgroup of classes of rank zero, using (1.3).

**Exercise 7.2.** Show that an element \(a\) of an abelian group \(M\) has nonzero image \(a\otimes1\) in \(M\otimes\mathbb Q\) if and only if \(a\) has infinite order.

**Exercise 7.3.** Show that a subgroup of a torsion-free group is torsion-free, and that the inclusion \(C^*_r(G)\to C^*_r(\Gamma)\) induced by a subgroup \(G\le\Gamma\) is isometric.

**Exercise 7.4.** In Lemma 3.3(1), why must the vertices of every simplex be ordered before mapping into \(EG\), and why does the order by tags work where an arbitrary order of each simplex would not?

## 8. Solutions

**7.1.** By (1.3), the classes of rank zero form the subgroup \(\{0\}\times\mathbb Z\), and its generators are the two elements with \(\kappa=\pm1\).

**7.2.** \(M\otimes\mathbb Q\) is the localization of \(M\) at the nonzero integers: every element is \(m\otimes\frac1n\), and \(a\otimes1=0\) exactly when \(na=0\) for some integer \(n\ge1\). So \(a\otimes1\ne0\) if and only if no positive multiple of \(a\) vanishes.

**7.3.** An element of finite order of the subgroup has finite order in the group. The restriction of the regular representation of \(\Gamma\) to \(G\) is the direct sum, over the right cosets \(Gk\), of copies of the regular representation of \(G\), so an element of the group algebra of \(G\) has the same norm in both.

**7.4.** The simplices of \(EG\) are ordered tuples, and different orders of the same vertices are different simplices. A simplicial map must choose one order for every simplex, compatibly with passage to faces, so that the maps on two simplices agree on their common face; and the map is \(G\)-equivariant only if \(g\) carries the chosen order of a simplex to the chosen order of its translate. The tags satisfy both requirements because they are invariant under \(G\) and distinct within a simplex. Orders chosen independently on different simplices need not agree on a common face.

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Theorem 1.1 and Sections 1 and 9.2. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
- [HS] B. Hanke and T. Schick, *The strong Novikov conjecture for low degree cohomology*, Geom. Dedicata 135 (2008), 119–127, Theorem 1.2 and Corollary 1.3; arXiv:0705.2578. https://arxiv.org/abs/0705.2578
- [Valette] A. Valette, *The Baum–Connes conjecture: a concise course*, arXiv:2610.01802 (2026), Section 7.4.1 and Conjecture 7.19. https://arxiv.org/abs/2610.01802
- [EH] H. Emerson and D. Hudson, *Baum–Connes and the Fourier–Mukai transform*, arXiv:2001.06124 (2020), Theorem 1.3. https://arxiv.org/abs/2001.06124
- [AS] M. F. Atiyah and I. M. Singer, *The index of elliptic operators on compact manifolds*, Bull. Amer. Math. Soc. 69 (1963), 422–433. https://www.ams.org/journals/bull/1963-69-03/S0002-9904-1963-10957-X/S0002-9904-1963-10957-X.pdf
- [BvE] P. F. Baum and E. van Erp, *K-homology and Fredholm operators I: Dirac operators*, J. Geom. Phys. 134 (2018), 101–118, Theorem 1; arXiv:1604.03502. https://arxiv.org/abs/1604.03502
- [Hatcher] A. Hatcher, *Algebraic Topology*, author's edition, Example 1B.7, Theorems 1B.8 and 3.5, Proposition A.1. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
- [Hatcher-VB] A. Hatcher, *Vector Bundles and K-Theory*, author's edition, version 2.2, Propositions 1.4 and 3.10, Theorem 3.2. https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf
