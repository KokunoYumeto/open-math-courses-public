# Invariant connections on homogeneous bundles

Symmetry reduces a connection to linear data, but isotropy, disconnected groups and smoothness at singular orbits still matter. We prove the closed-subgroup and transitive-orbit prerequisites, classify homogeneous connections, compute curvature and holonomy, and reconstruct invariant connections for arbitrary group actions. Complete examples include integral Hopf weights, noncommutative rectangle transport, gauge obstructions, dilation, rotational connections and both lifts of Euclidean symmetry. Smooth-jet and even-function proofs establish the classification at the origin.

All used prerequisites are proved here or at exact earlier programme locators. The four freely accessible construction versions are credited in the relevant parts; external sources do not replace programme proofs.

## A. Closed subgroups and transitive actions

All manifolds and Lie groups are finite dimensional, Hausdorff, second countable and smooth. Groups need not be connected. **Local** refers to [Local tools for bundles and transport](local-tools-for-bundles-and-transport.md), **PB** to [Principal bundles and associated bundles](principal-bundles-and-associated-bundles.md), and **Conn** to [Connections and parallel transport](connections-and-parallel-transport.md). The proofs below use the complete earlier proofs of finite dimensional compactness, differentiation, local inversion, constant rank, ordinary differential equations and the group exponential in Local 0.1–0.4, 1.2–1.4 and 2.1–2.3. No closed-subgroup theorem is assumed by those earlier results.

The freely accessible construction source for this part is Peter W. Michor's [author manuscript, *Topics in Differential Geometry*](https://www.mat.univie.ac.at/~michor/dgbook.pdf), §5.5 and §6.4, printed pages 64–65 and 70. We supply the transitivity argument and all other needed proofs below or at exact earlier programme results. We do not use the manuscript's onward references as proof providers.

**Theorem A.1 (a closed subgroup is embedded).** Every closed subgroup \(L\) of a Lie group \(K\) is an embedded Lie subgroup. Its Lie algebra is
\[
\mathfrak l=\{X\in\mathfrak k:\exp(tX)\in L\text{ for every }t\in\mathbb R\}.
\tag{A.1}
\]
Consequently \(K/L\), with its quotient topology, is a smooth Hausdorff second countable manifold, and \(K\to K/L\) is a principal \(L\)-bundle with smooth local sections.

**Proof.** Initially define \(E\subset\mathfrak k=T_eK\) as the set of velocities \(c'(0)\) of smooth curves in \(K\) defined near zero, taking values in \(L\), with \(c(0)=e\). This definition uses only the ambient smooth structure. The constant curve gives zero. If \(c_1,c_2\) have velocities \(X_1,X_2\), then \(c_1(at)c_2(bt)\), restricted to a common interval, has velocity \(aX_1+bX_2\). Indeed multiplication has derivative \((X,Y)\mapsto X+Y\) at \((e,e)\), by differentiating separately on its two factors. Thus \(E\) is a vector subspace.

We first record the effect of closedness. Suppose \(s_j>0\), \(s_j\to0\), \(X_j\to X\), and \(\exp(s_jX_j)\in L\). For each fixed real \(t\), choose an integer \(m_j\) with
\[
m_js_j\le t<(m_j+1)s_j.
\]
Then \(m_js_jX_j\to tX\). The exponential law of Local 2.3 and the subgroup property give
\[
\exp(m_js_jX_j)=\exp(s_jX_j)^{m_j}\in L.
\]
Continuity of the exponential and closedness of \(L\) imply \(\exp(tX)\in L\). Negative \(m_j\) cause no problem because inverses belong to \(L\).

For a curve defining \(X\in E\), take its logarithm \(v(t)\) in the exponential chart of Local 2.3. Since \(d\exp_0\) is the identity, \(v(0)=0\) and \(v'(0)=X\). For sufficiently large \(j\), put \(s_j=1/j\), \(X_j=jv(1/j)\). Then \(X_j\to X\) and \(\exp(s_jX_j)=c(1/j)\in L\). The preceding argument proves that the entire one-parameter subgroup of \(X\) is in \(L\). Conversely such a one-parameter subgroup is itself a curve defining \(X\in E\). This proves the equality in (A.1) with \(E\) in place of \(\mathfrak l\).

Choose a vector-space complement \(V\) of \(E\) in \(\mathfrak k\), using Local 0.2, and a Euclidean norm. There is a neighbourhood \(W_0\) of zero in \(V\) for which
\[
\exp(W_0)\cap L=\{e\}.
\tag{A.2}
\]
Otherwise, choose nonzero \(Y_j\in V\) with \(Y_j\to0\) and \(\exp(Y_j)\in L\), staying inside the injective exponential chart. Compactness of the unit sphere, Local 0.1, gives a subsequence on which \(Y_j/\|Y_j\|\to Y\in V\) with \(\|Y\|=1\). Apply the preceding closedness argument with \(s_j=\|Y_j\|\). It shows \(\exp(tY)\in L\) for all \(t\), so \(Y\in E\cap V=\{0\}\), a contradiction. If \(V=\{0\}\), (A.2) holds immediately.

The map
\[
F:E\times V\longrightarrow K,\qquad F(X,Y)=\exp(X)\exp(Y)
\]
has derivative \((X,Y)\mapsto X+Y\) at zero. Local 1.2 gives product neighbourhoods \(U_E,U_V\), with \(U_V\subset W_0\), on which it is a diffeomorphism onto an open neighbourhood \(O\) of \(e\). If \(F(X,Y)\in L\), then \(\exp(X)\in L\) by (A.1), so \(\exp(Y)=\exp(-X)F(X,Y)\in L\). Equation (A.2) and injectivity force \(Y=0\). Conversely \(F(X,0)\in L\). Therefore
\[
O\cap L=F(U_E\times\{0\}).
\tag{A.3}
\]
Left translation by every element of \(L\) supplies such a slice chart at every point of \(L\). These are embedded-submanifold charts with the subspace topology. In particular \(T_eL=E\), and Hausdorffness and second countability are inherited from \(K\).

The restrictions of ambient multiplication and inversion to \(L\) are smooth as maps into \(L\): in a target slice chart their transverse coordinates vanish, and the remaining coordinates are restrictions of smooth ambient functions. Their domains are the corresponding product or single submanifold charts. Thus \(L\) is a Lie group. Its bracket agrees with the restriction of the bracket on \(\mathfrak k\). For completeness, the left invariant ambient field for \(X\in E\) is tangent to \(L\), because at \(l\in L\) it is the velocity of \(l\exp(tX)\). In slice coordinates a tangent field has zero transverse coefficients along the slice. Tangential derivatives of these zero restrictions also vanish. The coordinate commutator formula of PB C.3 consequently makes the bracket of two such fields tangent to the slice. Evaluating at \(e\) proves bracket closure and agreement. This proves the embedded Lie-subgroup assertion and (A.1).

Local 4.1 now applies with its embeddedness hypothesis established. Its complete quotient-chart proof gives the stated topology, countability, local sections and principal-bundle trivializations. This also covers discrete subgroups and zero-dimensional groups. □

**Theorem A.2 (transitivity gives a submersion).** Let \(K\) act smoothly and transitively on a nonempty manifold \(M\). Fix \(x_0\in M\), put \(L=\{k\in K:kx_0=x_0\}\), and let \(a(k)=kx_0\). Then \(a\) is a submersion and
\[
\bar a:K/L\longrightarrow M,\qquad kL\longmapsto kx_0
\tag{A.4}
\]
is a diffeomorphism. No connectedness of \(K\) or \(L\) is required.

**Proof.** The stabilizer is a subgroup, and is closed as the inverse image of the closed point \(x_0\) under \(a\). Theorem A.1 gives its embedded structure and the smooth quotient. Define the fundamental field
\[
X_M(x)=\left.\frac{d}{dt}\right|_0\exp(tX)x.
\]
It is smooth by differentiation of the smooth action. The curve \(t\mapsto\exp(tX)x\) solves this field's differential equation: use \(\exp((t+s)X)=\exp(sX)\exp(tX)\) and differentiate in \(s\). If \(X_M(x_0)=0\), the constant curve at \(x_0\) solves the same equation. Uniqueness in Local 2.1 makes \(\exp(tX)x_0=x_0\) for all \(t\); uniqueness propagates along every finite interval. Conversely that identity immediately gives \(X_M(x_0)=0\). By A.1,
\[
\ker da_e=\mathfrak l.
\tag{A.5}
\]

The map (A.4) is a bijection by transitivity and the definition of \(L\). It is smooth: composing a smooth local section of \(K\to K/L\) with \(a\) gives its expression on that quotient chart. The quotient projection has kernel \(\mathfrak l\) at \(e\), as its product charts in Local 4.1 show. Thus (A.5) makes \(d\bar a\) injective at \(eL\). Equivariance under the diffeomorphisms given by left translation and the action of \(K\) makes it injective everywhere. Hence \(\bar a\) is an immersion of dimension \(r=\dim K-\dim L\) into \(M\), whose dimension is \(n\), and \(r\le n\).

We prove \(r=n\), including the countability step. Suppose instead that \(r<n\). Local 1.4 gives each point of \(K/L\) an open coordinate neighbourhood on which \(\bar a\) is an embedding into a coordinate \(r\)-plane in an open chart of \(M\). These neighbourhoods have a countable subcover. Indeed from a countable basis select, for each basis member contained in one of the neighbourhoods, one such neighbourhood; the selected collection covers every point. Inside each selected source chart, closed coordinate balls with rational centres and positive rational radii whose closures stay in the chart give a countable compact cover. Their compactness is Local 0.1. Enumerate all these compact subsets as \(C_j\).

Each \(\bar a(C_j)\) is compact by continuity and closed in the Hausdorff space \(M\). The latter elementary assertion follows by separating a point outside a compact set from each of its points, choosing a finite subcover of the resulting neighbourhoods of the compact set, and intersecting the finitely many disjoint neighbourhoods of the outside point. Its interior is empty: it lies in a coordinate \(r\)-plane, which contains no open \(n\)-dimensional ball when \(r<n\). Thus \(M\), by the surjectivity of \(\bar a\), would be a countable union of closed sets with empty interior.

Here that is impossible by the following direct nested-ball argument. Choose a closed positive-radius ball \(B_0\) in one coordinate chart of \(M\), with its closure inside the chart. Since \(\bar a(C_1)\) is closed and has empty interior, the interior of \(B_0\) contains a smaller closed positive-radius ball \(B_1\) disjoint from it. Continue with
\[
B_j\subset\operatorname{int}B_{j-1}\setminus\bar a(C_j),
\qquad \operatorname{radius}(B_j)<2^{-j}.
\]
At each step the indicated set is a nonempty open subset of the fixed coordinate chart. The centres have a convergent subsequence in the compact ball \(B_0\). For every fixed \(j\), all later centres belong to the closed set \(B_j\), so the limit belongs to every \(B_j\). It belongs to none of the sets \(\bar a(C_j)\), contradicting their covering of \(M\). The case \(n=0\) cannot have \(r<n\) in the first place.

It follows that \(d\bar a\) is everywhere bijective. Local 1.2 makes \(\bar a\) a local diffeomorphism. Its bijectivity makes the local smooth inverses agree to give a global smooth inverse. Finally \(a=\bar a\circ q\), with \(q:K\to K/L\) a submersion by A.1, proves the submersion assertion. □

## B. The linear data of a homogeneous connection

Continue the conventions of Part A. **Curv** denotes [Curvature and holonomy groups](curvature-and-holonomy-groups.md). The construction source is Hsien-Chung Wang's freely accessible original article, [*On Invariant Connections over a Principal Fibre Bundle*, Nagoya Mathematical Journal 13 (1958), 1–19](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7AC585E9DDCEF66E15F24C3481EEF592/S0027763000023461a.pdf/on-invariant-connections-over-a-principal-fibre-bundle.pdf), §§3–6, especially Theorem 1 on pages 8–9. We use the programme's right principal action, positive value on fundamental vectors and curvature \(d\omega+\frac12[\omega,\omega]\). The formulas and signs are derived below in these conventions; the article uses a left structure-group action and a different normalization. No external citation replaces a proof.

**Theorem B.1 (the bundle determined by isotropy).** Suppose \(K\) acts smoothly on a right principal \(G\)-bundle \(P\to M\) by principal automorphisms and acts transitively on \(M\). Choose \(p_0\in P_{x_0}\), let \(L=K_{x_0}\), and define \(\lambda:L\to G\) by
\[
lp_0=p_0\lambda(l).
\tag{B.1}
\]
Then \(\lambda\) is a smooth group homomorphism, and
\[
P_\lambda=(K\times G)/L,\qquad
(k,g)\cdot l=(kl,\lambda(l)^{-1}g),
\tag{B.2}
\]
is a right principal \(G\)-bundle over \(K/L\). The map
\[
\Xi:P_\lambda\longrightarrow P,\qquad [k,g]\longmapsto kp_0g
\tag{B.3}
\]
is a smooth principal-bundle isomorphism covering A.2 and intertwining the left \(K\)-actions. Conversely every smooth homomorphism \(\lambda:L\to G\), for a closed subgroup \(L\subset K\), defines such a homogeneous principal bundle by (B.2).

**Proof.** Freeness and transitivity of the principal action on a fibre give a unique \(\lambda(l)\). PB A.2's smooth division map gives \(\lambda(l)=\delta(p_0,lp_0)\), so it is smooth. Since the \(K\)-action commutes with the principal action,
\[
(l_1l_2)p_0=l_1(p_0\lambda(l_2))
=p_0\lambda(l_1)\lambda(l_2).
\]
Freeness proves the homomorphism identity. A.1 makes \(K\to K/L\) a principal \(L\)-bundle. Apply the associated-bundle construction PB B.1 to the left \(L\)-action \(l:g\mapsto\lambda(l)g\) on \(G\). It gives precisely (B.2), its actual quotient topology and its smooth Hausdorff second countable total space. Its quotient map \(q:K\times G\to P_\lambda\) is a submersion and a principal \(L\)-bundle.

Right multiplication \([k,g]h=[k,gh]\) is well defined because it commutes with the equivalence in (B.2). For a local section \(\sigma:U\to K\) of \(K\to K/L\), the associated-bundle chart is
\[
U\times G\longrightarrow P_\lambda|_U,
\qquad(x,g)\longmapsto[\sigma(x),g].
\tag{B.4}
\]
It intertwines right multiplication with multiplication in the second factor, proving the principal-bundle assertion. Left multiplication \(a[k,g]=[ak,g]\) is well defined and smooth. To check joint smoothness without a quotient-action assumption, lift a point locally using (B.4); the expression \((a,x,g)\mapsto q(a\sigma(x),g)\) is smooth. These local expressions cover the domain. The left action commutes with the right action and induces the transitive left action on \(K/L\).

Equation (B.3) is independent of the representative because
\[
(kl)p_0\lambda(l)^{-1}g=kp_0g.
\]
It is onto: for \(p\in P_x\), choose \(k\) with \(kx_0=x\), then divide in the fibre to get the unique \(g\) with \(p=kp_0g\). If \(kp_0g=k'p_0g'\), the base equality gives \(k'=kl\) for some \(l\in L\); freeness then gives \(g=\lambda(l)g'\), exactly the relation (B.2). Thus it is also one-to-one.

In the chart (B.4), it is \((x,g)\mapsto\sigma(x)p_0g\). Here \(x\mapsto\sigma(x)p_0\) is a smooth section over \(U\) after the base identification A.2. PB A.2 proves that this map and its inverse are smooth bundle charts. Hence \(\Xi\) is a diffeomorphism. Its two equivariances follow directly from (B.3). The converse uses only the construction (B.2)–(B.4), already proved for an arbitrary smooth \(\lambda\). □

**Theorem B.2 (Wang's classification with the full isotropy group).** Put \(\lambda_*=d\lambda_e\). Invariant principal connections on \(P_\lambda\) correspond bijectively to linear maps \(W:\mathfrak k\to\mathfrak g\) such that
\[
W|_{\mathfrak l}=\lambda_*,\qquad
W(\operatorname{Ad}(l)X)=\operatorname{Ad}(\lambda(l))W(X)
\quad(l\in L,\ X\in\mathfrak k).
\tag{B.5}
\]
Write \(b(k)=[k,e]\), and let \(\theta^K,\theta^G\) be the left Maurer forms. The correspondence and its reconstruction are
\[
W=(b^*\omega)_e,\qquad
q^*\omega=\operatorname{Ad}(g^{-1})W(\theta^K)+\theta^G
\quad\text{on }K\times G.
\tag{B.6}
\]
The conditions in (B.5) concern every component of \(L\).

**Proof.** First let \(\omega\) be invariant. The equality \(b(ak)=a\,b(k)\) makes \(b^*\omega\) left invariant on \(K\), hence equal to \(W\theta^K\): evaluating a left invariant one-form on \(dL_kX\) recovers its value at \(e\). For \(Z\in\mathfrak l\), the homomorphism \(\lambda\) carries \(\exp(tZ)\) to \(\exp(t\lambda_*Z)\). This follows by differentiating its homomorphism identity along the one-parameter subgroup and using the uniqueness of the invariant equation, Local 2.1–2.3. Therefore
\[
b(\exp(tZ))=[e,\lambda(\exp(tZ))]=p_0\exp(t\lambda_*Z),
\]
where \(p_0=[e,e]\). Vertical reproduction in Conn A.2 gives \(W(Z)=\lambda_*Z\). For \(l\in L\),
\[
b(lkl^{-1})=l\,b(k)\lambda(l)^{-1}.
\]
Pull back \(\omega\) through this identity, using \(K\)-invariance and right equivariance from Conn A.2, and evaluate at \(k=e\). It gives the second identity of (B.5), with \(\operatorname{Ad}(\lambda(l))\) on the right. This argument includes disconnected isotropy.

Since \(q(k,g)=b(k)g\), splitting its differential between its two factors and using reproduction and equivariance gives (B.6), by exactly the calculation in Conn A.3. In particular \(W\) determines \(q^*\omega\). A submersion has surjective differential, so equality of pullbacks of one-forms implies equality of the forms; hence this proves uniqueness.

Conversely suppose (B.5) holds and call the right side of (B.6) \(\widetilde\omega\). We verify that it descends through \(q\). For fixed \(l\in L\), the transformation in (B.2) sends \(\theta^K\) to \(\operatorname{Ad}(l^{-1})\theta^K\) and leaves \(\theta^G\) unchanged, since the latter factor is left multiplication by a constant. Its first term becomes
\[
\operatorname{Ad}(g^{-1}\lambda(l))W(\operatorname{Ad}(l^{-1})\theta^K)
=\operatorname{Ad}(g^{-1})W(\theta^K),
\]
using (B.5). Thus \(\widetilde\omega\) is invariant under the entire \(L\)-action.

The vertical tangent for \(q\) generated by \(Z\in\mathfrak l\) at \((k,g)\) is the velocity of
\[
(k\exp(tZ),\exp(-t\lambda_*Z)g).
\]
The first Maurer value is \(Z\). The second Maurer value is \(-\operatorname{Ad}(g^{-1})\lambda_*Z\), by the right-translation identity for the left Maurer form in Conn A.3. Therefore \(\widetilde\omega\) vanishes on this vertical vector by \(W(Z)=\lambda_*Z\). These vectors span \(\ker dq\), since B.1 identifies \(q\) as a principal \(L\)-bundle.

Here is the descent argument explicitly. At \(z\in P_\lambda\), choose a lift \(\tilde z\) and for \(v\in T_zP_\lambda\) a tangent lift \(\tilde v\), and set \(\omega_z(v)=\widetilde\omega_{\tilde z}(\tilde v)\). Two tangent lifts at the same point differ by a vertical vector, on which the form vanishes. Two point lifts differ by a unique element of \(L\); translating a tangent lift by that fixed element and using invariance proves independence of the point lift. Linearity follows by choosing all tangent lifts at one point. In a smooth local section \(s\) of \(q\), the defined form is \(s^*\widetilde\omega\), proving smoothness. Local sections exist by B.1 and PB B.1. This constructs the unique descended one-form.

Left multiplication on the \(K\)-factor preserves both terms of \(\widetilde\omega\), so the descended form is \(K\)-invariant. Right multiplication on the \(G\)-factor sends it to \(\operatorname{Ad}(h^{-1})\widetilde\omega\), by Conn A.3's Maurer identity and \(\operatorname{Ad}((gh)^{-1})=\operatorname{Ad}(h^{-1})\operatorname{Ad}(g^{-1})\). Its value on the principal \(G\)-fundamental vector represented by \((0,dL_gY)\) is \(Y\). These identities descend, so Conn A.2 proves that \(\omega\) is a principal connection. Evaluating its pullback at \((e,e)\) on \((X,0)\) recovers \(W(X)\). Both constructions are inverse. □

**Theorem B.3 (curvature is the bracket defect).** For the connection associated to \(W\), define
\[
C_W(X,Y)=[W(X),W(Y)]-W([X,Y]).
\tag{B.7}
\]
Then \(\Omega=d\omega+\frac12[\omega,\omega]\) satisfies
\[
\begin{aligned}
(b^*\Omega)_k(dL_kX,dL_kY)&=C_W(X,Y),\\
(q^*\Omega)_{(k,g)}((v,\eta),(w,\xi))
&=\operatorname{Ad}(g^{-1})C_W(\theta^K_kv,\theta^K_kw).
\end{aligned}
\tag{B.8}
\]
In particular \(C_W\) vanishes when either argument is in \(\mathfrak l\), and the connection is flat exactly when \(W\) is a Lie algebra homomorphism.

**Proof.** Curv A.1–A.4 prove the exterior-bracket identities, the exterior evaluation formula, the Maurer identity, and the curvature's horizontality and right equivariance. Pulling back the curvature and using B.2 gives
\[
b^*\Omega=d(W\theta^K)+\tfrac12[W\theta^K,W\theta^K].
\]
On the left invariant fields for \(X,Y\), the one-form has constant values \(W(X),W(Y)\). The exterior evaluation formula, Curv A.2, makes its derivative equal to \(-W([X,Y])\); Curv A.1 makes the half bracket equal to \([W(X),W(Y)]\). This proves the first formula in (B.8).

For \(q(k,g)=b(k)g\), its differential applied to \((v,\eta)\) is the sum of \(dR_g\,db(v)\) and a principal vertical vector. Horizontality of \(\Omega\) removes that vertical term from each argument, and right equivariance extracts \(\operatorname{Ad}(g^{-1})\). The first formula, writing \(v=dL_k\theta^K_kv\), proves the second. This also proves that all curvature values are accounted for, because \(q\) is a submersion.

To check the isotropy vanishing directly, put \(l=\exp(tZ)\) in (B.5) with \(Z\in\mathfrak l\) and differentiate at zero. Curv A.3 gives
\[
W([Z,Y])=[\lambda_*Z,W(Y)]=[W(Z),W(Y)].
\]
Thus \(C_W(Z,Y)=0\), and antisymmetry handles the other argument. Finally \(\Omega=0\) implies \(C_W=0\) by the first formula at \(e\), and \(C_W=0\) implies \(q^*\Omega=0\) by the second. Surjectivity of \(dq\) then gives \(\Omega=0\). By its definition (B.7), \(C_W=0\) is exactly bracket preservation by the linear map \(W\). □

## C. Holonomy from the linear connection data

The free primary source for the homogeneous holonomy formula is Wang's [original article](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7AC585E9DDCEF66E15F24C3481EEF592/S0027763000023461a.pdf/on-invariant-connections-over-a-principal-fibre-bundle.pdf), §9, Theorem 3. Its reductive construction is §6, Corollary 3. The proof below uses the complete curvature-generation proof in **Curv G.3**, together with the intrinsic holonomy groups proved in **Curv C.5**. **Flat** denotes [Flat connections and infinitesimal holonomy](flat-connections-and-infinitesimal-holonomy.md); its A.1 proves uniqueness of the connected immersed subgroup integrating a Lie subalgebra. None of Wang's onward references is used in place of these programme proofs.

**Theorem C.1 (the homogeneous holonomy algebra).** Assume that \(M=K/L\) is connected. Let \(W\) satisfy (B.5) and let \(C_W\) be its bracket defect (B.7). Define subspaces of \(\mathfrak g\) recursively by
\[
V_0=\operatorname{span}_{\mathbb R}\{C_W(X,Y):X,Y\in\mathfrak k\},
\qquad
V_{j+1}=V_j+\operatorname{span}_{\mathbb R}\{[W(X),Z]:X\in\mathfrak k,\ Z\in V_j\}.
\tag{C.1}
\]
The increasing sequence stabilizes after finitely many steps. Its final space \(V\) is the Lie algebra of both full and restricted holonomy at \(p_0=[e,e]\). In particular \(V\) is a Lie subalgebra, and
\[
\operatorname{Hol}_{p_0}^{0}
=\langle\exp(tZ):t\in\mathbb R,\ Z\in V\rangle
\tag{C.2}
\]
with its intrinsic connected immersed Lie-group structure. The formula determines restricted holonomy, not the discrete components of full holonomy. Neither \(K\), \(L\), nor \(G\) is required to be connected.

**Proof.** Every \(V_j\) is a subspace of the finite dimensional vector space \(\mathfrak g\). A strict inclusion increases dimension. Once \(V_{j+1}=V_j\), that space is preserved by every \(\operatorname{ad}(W(X))\), so the recursion remains stationary. Thus it stabilizes; this includes \(V_0=\{0\}\). Its final space is precisely the smallest vector subspace containing \(V_0\) and preserved by all these adjoint operators. We do not assume bracket closure at this stage.

Write \(H^0\) and \(\mathfrak h\) for the restricted holonomy group and its Lie algebra, as constructed in Curv C.5. Curv G.3 implies \(V_0\subset\mathfrak h\), by evaluating curvature at the initial point and using B.3. We show that \(\mathfrak h\) is preserved by \(\operatorname{ad}(W(X))\). Fix \(X\in\mathfrak k\) and put
\[
k(t)=\exp(tX),\qquad
p(t)=k(t)p_0\exp(-tW(X)).
\tag{C.3}
\]
Formula (B.6) gives
\[
\omega(p'(t))
=\operatorname{Ad}(\exp(tW(X)))W(X)-W(X)=0.
\]
Here conjugation by the one-parameter subgroup fixes its generator, by differentiating its commutation with itself. Thus (C.3) is the horizontal lift, from \(p_0\), of \(k(t)L\).

A connection-preserving principal automorphism carries a horizontal lift to a horizontal lift: it preserves the zero value of \(\omega\), and uniqueness of transport identifies the resulting lift. Acting by \(k(t)\) therefore identifies the holonomy groups at \(p_0\) and \(k(t)p_0\) as the same subgroups of \(G\). This holds for restricted groups too, because the base diffeomorphism sends a based contraction to a based contraction. On the other hand Curv C.5 identifies the restricted group at the horizontally transported \(p(t)\) with \(H^0\), and its change-of-frame formula gives
\[
H^0
=\exp(tW(X))H^0\exp(-tW(X)).
\tag{C.4}
\]
This equality also identifies the intrinsic smooth structures. In Curv C.5 that structure is built from all smooth identity-containing parameter families in the subgroup; conjugation in \(G\) carries this family to itself when it preserves the subgroup. The same word charts used there make the restriction of conjugation a smooth automorphism. Differentiating it in the subgroup gives
\(\operatorname{Ad}(\exp(tW(X)))\mathfrak h=\mathfrak h\).
For \(Z\in\mathfrak h\), differentiate this curve of vectors at \(t=0\). A finite dimensional subspace contains the derivative of any curve lying in it, as projection onto a linear complement verifies. Curv A.3 now gives \([W(X),Z]\in\mathfrak h\). The minimality just proved for \(V\) implies
\[
V\subseteq\mathfrak h.
\tag{C.5}
\]

For the opposite inclusion take any finitely piecewise \(C^1\) base path \(\gamma\) starting at \(eL\). The principal \(L\)-bundle \(K\to K/L\) has a smooth connection by Conn B.1, with no invariance required of this auxiliary connection. Its global lifting theorem Conn C.1, extended to this time regularity in Curv C.2, gives a finitely piecewise \(C^1\) lift \(k(t)\) of \(\gamma\) with \(k(0)=e\). Set
\[
u(t)=\theta^K_{k(t)}k'(t),\qquad a(t)=W(u(t)).
\]
These are continuous on each closed time piece. By Local 2.2 the equation
\[
g'(t)=-(dR_{g(t)})_e a(t),\qquad g(0)=e,
\tag{C.6}
\]
has a unique solution on the entire path interval. Formula (B.6) and the left Maurer form of (C.6) show that \([k(t),g(t)]\) is horizontal, so it is the lift of \(\gamma\) from \(p_0\).

We claim \(\operatorname{Ad}(g(t)^{-1})V=V\). Put \(T(t)=\operatorname{Ad}(g(t)^{-1})\). On each time piece, differentiation of the adjoint homomorphism, using Curv A.3, gives
\[
T'(t)=T(t)\operatorname{ad}(a(t)),\qquad T(0)=I.
\tag{C.7}
\]
To verify the order and sign intrinsically, the right logarithmic derivative in (C.6) is \(-a(t)\). Differentiating \(\operatorname{Ad}(g(t))\) gives \(-\operatorname{ad}(a(t))\operatorname{Ad}(g(t))\); differentiate the identity between this operator and its inverse to obtain (C.7). These are derivatives of group multiplication, not a matrix assumption on \(G\).

Choose a complement of \(V\) in \(\mathfrak g\), Local 0.2. Since \(\operatorname{ad}(a(t))\) preserves \(V\), its block from \(V\) to the complement is zero. In the equation (C.7), the corresponding lower-left block \(B(t)\) of \(T(t)\) satisfies
\[
B'=B A_{11}(t),\qquad B(0)=0,
\]
where \(A_{11}\) is the restriction of \(\operatorname{ad}(a(t))\) to \(V\). Uniqueness for this linear equation gives \(B=0\). The uniqueness proof in Local 2.1 applies to continuous time coefficients, as explicitly verified in Local 2.2; transpose the equation if desired to give a right matrix equation. Apply this on successive pieces, passing the zero endpoint value forward. Consequently \(T(t)V\subset V\). Since \(T(t)\) is invertible and \(V\) has finite dimension, its restriction has image of the same dimension, hence \(T(t)V=V\). If \(V\) or its complement has dimension zero the same assertion is immediate.

At every point of this horizontal lift, formula (B.8) puts all curvature values in
\(\operatorname{Ad}(g(t)^{-1})V_0\subset V\).
Every point horizontally reachable from \(p_0\) is obtained by such a path. Curv G.3 says that the ordinary linear span of exactly these values is \(\mathfrak h\). Thus \(\mathfrak h\subseteq V\), completing equality with (C.5). This proves bracket closure too, since \(\mathfrak h\) is a Lie algebra. Curv C.5 identifies restricted holonomy as the full group's connected identity component, and Flat A.1 gives (C.2) with the asserted smooth structure. No discrete-component assertion follows from a Lie algebra computation. □

**Theorem C.2 (reductive splittings and the canonical connection).** Suppose
\[
\mathfrak k=\mathfrak l\oplus\mathfrak m,
\qquad\operatorname{Ad}(l)\mathfrak m=\mathfrak m\quad(l\in L).
\tag{C.8}
\]
For any smooth \(\lambda:L\to G\), invariant connections on \(P_\lambda\) correspond to the linear maps \(\alpha:\mathfrak m\to\mathfrak g\) satisfying
\[
\alpha(\operatorname{Ad}(l)X)=\operatorname{Ad}(\lambda(l))\alpha(X).
\tag{C.9}
\]
Their Wang maps are \(W(Z+X)=\lambda_*Z+\alpha(X)\). In particular \(\alpha=0\) defines the canonical connection for the chosen splitting. For \(X,Y\in\mathfrak m\), their curvature defects are
\[
C_W(X,Y)=[\alpha(X),\alpha(Y)]
-\lambda_*([X,Y]_{\mathfrak l})-\alpha([X,Y]_{\mathfrak m}).
\tag{C.10}
\]
On \(K\to K/L\) itself, take \(G=L\) and \(\lambda=\mathrm{id}\); the canonical horizontal space at \(k\) is \(dL_k\mathfrak m\).

**Proof.** The subspace \(\mathfrak l\) is preserved by \(\operatorname{Ad}(L)\), because conjugation by \(L\) maps its embedded subgroup to itself. Together with (C.8) this means that the two projections in that direct sum commute with \(\operatorname{Ad}(l)\). Differentiating
\(\lambda(lhl^{-1})=\lambda(l)\lambda(h)\lambda(l)^{-1}\)
at \(h=e\) gives
\(\lambda_*\operatorname{Ad}(l)=\operatorname{Ad}(\lambda(l))\lambda_*\) on \(\mathfrak l\). Therefore a map with the prescribed restriction \(\lambda_*\) satisfies (B.5) precisely when its remaining component satisfies (C.9). B.2 proves the classification and existence for \(\alpha=0\). Substitution in (B.7) gives (C.10); B.3 already proves that pairs involving \(\mathfrak l\) contribute zero.

For the last assertion, the map \([k,h]\mapsto kh\) identifies \(K\times_L L\) with \(K\); its inverse is \(k\mapsto[k,e]\), and the local charts B.4 verify smoothness in both directions. The canonical one-form on \(K\) is consequently \(\operatorname{pr}_{\mathfrak l}\theta^K\), by (B.6). Its kernel is exactly \(dL_k\mathfrak m\). In particular it is a connection for the full subgroup \(L\), including its disconnected components. □

## D. Complete computations on homogeneous bundles

These examples use the free-source constructions proved in Parts A–C. The circle, Hopf bundle and its connection are constructed and proved in **PB E.1**, **Conn E.1–E.3** and **Curv D.1**. We give the additional matrix algebra, isotropy calculations and transport equations explicitly. The historical exercise statements are used only to check coverage; their former solutions supply none of these proofs.

**Example D.1 (the special unitary model of the Hopf bundle).** For \(z=(z_0,z_1)\in S^3\subset\mathbb C^2\), put
\[
k(z)=\begin{pmatrix}z_0&-\bar z_1\\z_1&\bar z_0\end{pmatrix}.
\tag{D.1}
\]
These matrices form \(K=\mathrm{SU}(2)\), with its smooth group structure identified with \(S^3\). Its transitive action on \(\mathbb {CP}^1\) has stabilizer
\[
L=\left\{\begin{pmatrix}a&0\\0&a^{-1}\end{pmatrix}:a\in U(1)\right\}
\tag{D.2}
\]
at \([1:0]\). A real basis of its Lie algebra is
\[
H=\begin{pmatrix}i&0\\0&-i\end{pmatrix},\quad
E=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
F=\begin{pmatrix}0&i\\i&0\end{pmatrix},
\tag{D.3}
\]
with
\[
[H,E]=-2F,\qquad [H,F]=2E,\qquad [E,F]=-2H.
\tag{D.4}
\]
The splitting \(\mathfrak {su}(2)=\mathbb RH\oplus\operatorname{span}_{\mathbb R}\{E,F\}\) is \(\operatorname{Ad}(L)\)-invariant. For \(\lambda_1(\operatorname{diag}(a,a^{-1}))=a\), the homogeneous principal \(U(1)\)-bundle is the Hopf bundle of PB E.1.

**Proof.** The columns of (D.1) have length one and inner product zero, and its determinant is \(|z_0|^2+|z_1|^2=1\). Conversely, for a unitary determinant-one matrix with first column \(z\), its second column must be \(c(-\bar z_1,\bar z_0)\) for some \(c\in U(1)\). To see the one-dimensional orthogonal complement directly, solve \(\bar z_0u+\bar z_1v=0\) using whichever component of \(z\) is nonzero; unit length gives \(|c|=1\). The determinant equals \(c\), so \(c=1\). This proves the bijection with the set of unitary determinant-one matrices. That set is closed under multiplication and inverse: conjugate-transpose multiplication reverses the factors, and determinants of two-by-two matrices multiply by direct expansion. In (D.1) and its inverse, which extracts the first column, all coordinates are real polynomial expressions. PB E.1 proves the smooth sphere structure; the resulting group operations are smooth restrictions of matrix multiplication and conjugate transpose. Thus this is a Lie group smoothly identified with \(S^3\).

Its linear action on complex lines is smooth: in either projective chart from PB E.1, use a spanning column \((1,w)\) or \((v,1)\), multiply by the matrix, and divide by the nonzero output component. These formulas cover the action domain. Every line contains a unit vector, and (D.1) maps \((1,0)\) to that vector, proving transitivity. A matrix preserving the first coordinate line has first column \((a,0)\), \(|a|=1\), and the proved second-column formula gives (D.2). The stabilizer is closed, and A.2 identifies \(K/L\) smoothly with \(\mathbb {CP}^1\).

At \(z=(1,0)\), differentiation of the sphere equation gives a tangent first component \(ir\), \(r\in\mathbb R\), and an arbitrary second component \(u+iv\). Differentiating (D.1) therefore gives exactly \(rH+uE+vF\), proving the basis assertion. Matrix multiplication and subtraction give (D.4), with the matrix Lie-bracket convention proved in Curv A.3. Conjugation by \(\operatorname{diag}(a,a^{-1})\) fixes \(H\) and sends a matrix with zero diagonal to one with zero diagonal; within this real Lie algebra those are exactly the span of \(E,F\). It is invertible, proving preservation of that plane in both directions. This proves the splitting assertion.

The map
\[
[k,a]\longmapsto k(1,0)^T a
\tag{D.5}
\]
is the bundle identification B.3, applied to the unit-column Hopf bundle and the natural left action of \(K\). Indeed the action commutes with scalar multiplication, and the isotropy formula at \((1,0)\) is exactly \(\lambda_1\). B.1 proves that (D.5) is a smooth principal-bundle isomorphism. This verifies the Hopf identification with the same right-action convention as PB E.1. □

**Exercise D.2 (all integral Hopf weights).** For \(m\in\mathbb Z\), let
\[
\lambda_m(\operatorname{diag}(a,a^{-1}))=a^m,\qquad
P_m=\mathrm{SU}(2)\times_{\lambda_m}U(1).
\tag{D.6}
\]
Determine all invariant connections, their curvature and both holonomy groups. Identify the case \(m=1\) with the earlier Hopf connection.

**Solution.** Every integer power is a smooth homomorphism of \(U(1)\), including negative powers by smooth inversion. Differentiating a product of \(m\) factors, or its inverse for \(m<0\), gives \((\lambda_m)_*(H)=im\). The target Lie algebra is \(i\mathbb R\) with trivial adjoint action. For the particular isotropy element \(l=\operatorname{diag}(i,-i)\), direct matrix conjugation sends both \(E\) and \(F\) to their negatives. Thus (B.5) forces \(W(E)=W(F)=0\); its other condition forces \(W(H)=im\). Conversely this map is equivariant for all of \(L\), because D.1 proves that \(H\) is fixed and its complementary plane is invariant. There is therefore exactly one invariant connection for each \(m\), namely the canonical connection C.2 with
\[
W_m(rH+uE+vF)=imr.
\tag{D.7}
\]

For vectors represented at \(p_0\) by \(E,F\), equations (B.7) and (D.4) give
\[
C_{W_m}(E,F)=2im,
\qquad C_{W_m}(H,E)=C_{W_m}(H,F)=0.
\tag{D.8}
\]
These determine the curvature at every point by (B.8). More concretely, for a local section \(\sigma\) of \(K\to K/L\), the corresponding section \([\sigma,e]\) of \(P_m\) has potential \(W_m\sigma^*\theta^K\), hence \(m\) times the potential for \(m=1\).

In the identification D.1 with \(S^3\), the one-form \(z^*dz\) of Conn E.3 is invariant under \(K\), because for a constant unitary matrix \(k\) one has \((kz)^*d(kz)=z^*k^*k\,dz=z^*dz\). Its values at \((1,0)\) on the velocities \(H(1,0), E(1,0), F(1,0)\) are \(i,0,0\). Thus it is the unique \(m=1\) connection just determined. The unit section of Conn E.3 consequently gives the potential and curvature for every \(m\):
\[
A_m=m\,\frac{\bar w\,dw-w\,d\bar w}{2(1+|w|^2)},
\qquad
F_m=\frac{2im}{(1+x^2+y^2)^2}\,dx\wedge dy,
\quad w=x+iy.
\tag{D.9}
\]
The curvature computation for \(m=1\) is Curv D.1; the target is abelian, so exterior differentiation gives the displayed scaling for every integer \(m\).

The base is connected. For example every finite projective coordinate \(w\) is joined to zero by \(t\mapsto tw\); the remaining line lies in the second coordinate chart and is joined there to a point of the overlap. If \(m\ne0\), (D.8) spans all of \(i\mathbb R\). Theorem C.1 makes this the restricted holonomy algebra. Its integrated connected subgroup is all of \(U(1)\), since the circle exponential in Conn E.1 is onto and (C.2) includes every such exponential. Consequently full and restricted holonomy are both \(U(1)\).

For \(m=0\), the isotropy homomorphism is trivial. The map \([k,a]\mapsto(kL,a)\) and its chartwise inverse identify \(P_0\) with the product bundle. Formula (D.7) gives \(W_0=0\), so (B.6) is just the left Maurer form on the second factor. Thus the global product potential is zero, transport preserves that coordinate, and both holonomy groups are the identity group. This last conclusion uses the actual product transport, rather than inferring full holonomy from a zero Lie algebra. □

**Exercise D.3 (central holonomy and the rectangle sign).** On \(\mathbb R^2\), let the structure group \(N\) consist of upper triangular real three-by-three matrices with diagonal entries one. Put \(P=E_{12}\), \(Q=E_{23}\), \(Z=E_{13}\), and take potential \(A=P\,dx+Q\,dy\). Determine curvature, full and restricted holonomy, and the exact transport around the rectangle traversed right, up, left, down.

**Solution.** Write an element as \(I+uP+vQ+wZ\). Matrix multiplication gives
\[
(u,v,w)(u',v',w')=(u+u',v+v',w+w'+uv'),
\qquad
(u,v,w)^{-1}=(-u,-v,uv-w).
\tag{D.10}
\]
These polynomial formulas make \(N\) a Lie group on \(\mathbb R^3\). Its tangent algebra consists of \(uP+vQ+wZ\); direct products give \(PQ=Z\), \(QP=0\), and every product of \(Z\) with \(P,Q,Z\) is zero. Hence \([P,Q]=Z\) and \(Z\) is central. The local curvature formula in Curv A.4 gives
\[
F=Z\,dx\wedge dy.
\tag{D.11}
\]
Translations of the base, leaving the group coordinate fixed, preserve the potential, so this is also the homogeneous case with \(K=\mathbb R^2\), \(L=\{0\}\), and \(W(a,b)=aP+bQ\). In C.1, \(V_0=\mathbb RZ\) and all further adjoint brackets vanish. Thus restricted holonomy has algebra \(\mathbb RZ\) and group \(\{I+cZ:c\in\mathbb R\}\), since \(t\mapsto I+tcZ\) is the one-parameter subgroup with tangent \(cZ\).

We also compute every loop transport directly, which proves the full-group assertion and the sign. For a path \((x(t),y(t))\) starting at \((x_0,y_0)\), write its identity-starting group lift as \(g(t)=I+u(t)P+v(t)Q+w(t)Z\). The equation from Conn C.1 is \(g'=-(Px'+Qy')g\), so
\[
u'=-x',\qquad v'=-y',\qquad w'=-x'v.
\tag{D.12}
\]
With zero initial values, \(u=x_0-x\), \(v=y_0-y\), and
\[
w(t)=\int_0^t (y(s)-y_0)x'(s)\,ds.
\tag{D.13}
\]
The integrals are taken on each of the finitely many \(C^1\) pieces. Local 0.3 and (D.12) verify the equations and initial values; uniqueness identifies the lift. For a loop the endpoint has \(u=v=0\), so every full holonomy element is central. On a rectangle of side lengths \(a,b\), only its leftward edge contributes to (D.13), giving \(-ab\). Therefore its exact multiplier is
\[
I-abZ=\exp(-abZ).
\tag{D.14}
\]
With positive sides this yields every negative central parameter by varying the area, and reversing the loop yields every positive parameter; zero comes from the constant loop. All these loops contract linearly in the plane. Consequently both full and restricted holonomy are exactly \(\{I+cZ:c\in\mathbb R\}\). Starting at any other group coordinate multiplies it on the right of these endpoint multipliers, by principal equivariance. □

**Exercise D.4 (isotropy and flat circle monodromy).** Let \(K=\mathbb R\), \(L=2\pi\mathbb Z\), \(G=U(1)\), and
\[
\lambda(2\pi n)=e^{2\pi i\beta n},\qquad W(1)=i\alpha,
\quad\alpha,\beta\in\mathbb R.
\tag{D.15}
\]
Compute positive-generator transport on \(P_\lambda\), give its potential in a global section, and determine its holonomy groups.

**Solution.** Conn E.1 proves that \(t\mapsto e^{it}\) identifies \(\mathbb R/2\pi\mathbb Z\) with the circle and gives smooth local inverse angles. The subgroup \(L\) is closed and discrete, so \(\mathfrak l=0\). Both adjoint actions in (B.5) are trivial. Thus every real \(\alpha\) defines an invariant connection with
\[
q^*\omega=i\alpha\,dt+g^{-1}dg.
\tag{D.16}
\]
Its curvature is zero, either by B.3 or because the base is one dimensional. Along the positive generator parametrized by \(0\le t\le2\pi\), the horizontal lift from \([0,1]\) is \([t,e^{-i\alpha t}]\), as substitution in (D.16) verifies. Since \([t+2\pi n,g]=[t,e^{2\pi i\beta n}g]\), its endpoint is
\[
[0,e^{2\pi i(\beta-\alpha)}].
\tag{D.17}
\]

The rule
\[
s(e^{it})=[t,e^{-i\beta t}]
\tag{D.18}
\]
is independent of the chosen angle: replacing \(t\) by \(t+2\pi n\) cancels the two factors \(e^{2\pi i\beta n}\) and \(e^{-2\pi i\beta n}\). It is smooth in every local angle chart and is a global section. Pulling (D.16) back gives
\[
A=i(\alpha-\beta)\,d\theta.
\tag{D.19}
\]
Here \(d\theta\) is a globally defined one-form: local inverse angles differ by a locally constant multiple of \(2\pi\), so their differentials agree. The potential also checks the sign in (D.17), using Conn E.1's negative sign in the horizontal equation.

Flat F.2 proves \(\pi_1(U(1))=\mathbb Z\) by lifting angles, and Flat E.1 proves homotopy invariance of transport for flat connections. Thus
\[
\operatorname{Hol}_{[0,1]}
=\langle e^{2\pi i(\beta-\alpha)}\rangle,
\qquad \operatorname{Hol}_{[0,1]}^0=\{1\}.
\tag{D.20}
\]
For instance \(\alpha=0,\beta=1/2\) gives the nontrivial group \(\{1,-1\}\), even though \(W=0\). For \(\alpha=\beta\), transport is trivial. These computations exhibit precisely the discrete data that C.1's Lie algebra formula does not recover. The holonomy representation convention in Flat E.2 uses the inverse of the actual multiplier (D.17). □

**Exercise D.5 (disconnected isotropy cannot be omitted).** Let \(K=\mathbb R\rtimes\{1,-1\}\) act on \(\mathbb R\) by \((a,\varepsilon)x=a+\varepsilon x\), and lift it to \(\mathbb R\times U(1)\) by leaving the group coordinate fixed. Classify its invariant connections, and compare checking the full isotropy condition with checking only its differential.

**Solution.** The multiplication
\((a,\varepsilon)(b,\delta)=(a+\varepsilon b,\varepsilon\delta)\)
and inverse \((a,\varepsilon)^{-1}=(-\varepsilon a,\varepsilon)\) give a Lie group with two line components. Its action is smooth and transitive. At \(0\), the stabilizer is \(L=\{(0,1),(0,-1)\}\); at \((0,1)\) in the principal bundle the homomorphism \(\lambda\) is trivial because the lifted action fixes the group coordinate. The Lie algebra of \(K\) is the translation line, and conjugation by \((0,-1)\) sends its generator to its negative. Equation (B.5) therefore gives
\[
W(-X)=W(X).
\]
Linearity implies \(W=0\). Conversely this map satisfies both conditions in B.5 and determines a unique invariant connection. In the global section \(s(x)=(x,1)\), this is the zero potential, since the translation orbit of \((0,1)\) is that section and its Wang values vanish.

If one checked only infinitesimal isotropy, \(\mathfrak l=0\) would impose no condition. Every map \(W(1)=ic\), \(c\in\mathbb R\), would then appear to qualify. Its actual potential is \(ic\,dx\), invariant under translations, but reflection pulls it back to \(-ic\,dx\). It is invariant under the specified full action precisely when \(c=0\). Thus the full-group condition excludes exactly the spurious nonzero family. □

## E. Invariant connections for arbitrary group actions

Transitivity is not needed if connection data are given on submanifolds transverse to the group orbits. This part reconstructs the general classification from Maximilian Hanusch's free corrected author version, [*A Characterization of Invariant Connections*, arXiv:1310.0318v3, 27 January 2015](https://arxiv.org/abs/1310.0318v3), §§2–4, especially Theorem 4.9. The source is available under [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/); the exposition and complete proofs below are newly written. We use our existing notation \(K\) for the symmetry group and \(G\) for the principal structure group. The source's externally cited stabilizer facts are proved here from A.1 and the programme's differential-equation results.

Let \(K\) act smoothly by principal automorphisms on \(P\to M\), with no transitivity, properness or constant orbit-dimension assumption. Its induced base action is smooth: in a local section \(s\) it is \((k,x)\mapsto\pi(ks(x))\), independent of the section because the action commutes with right multiplication. Define
\[
Q=K\times G,\qquad
\Theta((k,a),p)=kp a^{-1},\qquad
\rho(k,a)=\operatorname{Ad}(a).
\tag{E.1}
\]
The product-group law makes \(\Theta\) a left action: applying \((k_2,a_2)\) and then \((k_1,a_1)\) gives \(k_1k_2p a_2^{-1}a_1^{-1}\). The map \(\rho\) is a representation by PB C.3. Write \(\Theta_q\) for the diffeomorphism associated with a fixed \(q\), \(X_P\) for the fundamental field of \(X\in\mathfrak k\), and \(A^\#\) for the principal fundamental field of \(A\in\mathfrak g\). Then
\[
D_p(X,A,v)=X_P(p)-A^\#(p)+v
\tag{E.2}
\]
is the derivative of \(Q\times P\to P\) at \((e,p)\). We identify tangents of an injectively immersed submanifold with their images in the ambient tangent space. Its own manifold topology is retained; global embeddedness is not assumed.

**Lemma E.1 (transverse patches and their coordinates).** An injectively immersed submanifold \(S\subset P\) is called a transverse patch when
\[
T_pP=T_pS+\{X_P(p):X\in\mathfrak k\}+V_pP
\quad(p\in S).
\tag{E.3}
\]
The sum need not be direct. For such a patch the action map
\[
F_S:Q\times S\to P,\qquad(q,p)\mapsto\Theta_q(p)
\tag{E.4}
\]
is a submersion. At every \(p\in S\), some submanifold \(H\subset Q\) through \(e\) and neighbourhood \(S'\subset S\) give a diffeomorphism \(F_S:H\times S'\to U\) onto an open neighbourhood of \(p\) in \(P\). Conversely, existence of these coordinates at every point implies (E.3).

A family \((S_\alpha)\) is a transverse covering when \(\bigcup_\alpha Q S_\alpha=P\), equivalently when every base \(K\)-orbit meets some \(\pi(S_\alpha)\). Such coverings exist. At \(p\in S\), with \(x=\pi(p)\),
\[
\dim S\ge\dim M-\dim K+\dim K_x.
\tag{E.5}
\]
At each prescribed point there exists a local patch attaining equality there. In particular, zero-dimensional patches are permitted wherever the \(Q\)-orbit has full tangent dimension.

**Proof.** The orbit derivative of \(Q\) at \(p\) has image \(\{X_P(p)-A^\#(p)\}\). Conn A.2 identifies the principal fundamental vectors with all of \(V_pP\). Hence (E.3) says exactly that (E.2), with \(v\in T_pS\), is onto. For general \(q\), differentiation of the action identity gives
\[
dF_S|_{(q,p)}(dL_q(X,A),v)
=d\Theta_q|_p\,D_p(X,A,v).
\tag{E.6}
\]
The left and right differentials of the fixed group actions are isomorphisms. Surjectivity follows everywhere, proving the submersion assertion.

Choose a subspace of the orbit image complementary to \(T_pS\) in \(T_pP\), and choose a subspace \(J\subset\mathfrak q\) which the orbit derivative maps isomorphically to that complement. These finite dimensional choices are supplied by Local 0.2: choose bases of the complement and tangent preimages. The local exponential identifies a neighbourhood of zero in \(J\) with a submanifold \(H\subset Q\) through \(e\), by Local 2.3. Restricted to \(T_eH\oplus T_pS\), the derivative in (E.6) at \(q=e\) is a linear isomorphism. Local 1.2, in a manifold chart on \(S\), gives a local diffeomorphism from a neighbourhood in \(H\times S\). Restrict to a product of two open neighbourhoods inside it. Its image remains open, and the restricted map remains a diffeomorphism. This proves the required coordinates, even if the original immersion of \(S\) is not globally embedded. Conversely their derivative at \((e,p)\) is onto and is a restriction of (E.2), proving (E.3).

For the dimension statement we verify the stabilizer calculation without transitivity. For any smooth action of a Lie group \(B\) on a manifold and a point \(z\), its stabilizer \(B_z\) is closed and thus embedded by A.1. A vector \(Y\in\mathfrak b\) belongs to the kernel of the orbit derivative precisely when its fundamental field vanishes at \(z\). The curve \(\exp(tY)z\) solves that field's equation, by differentiation of the action law. If the field vanishes at \(z\), the constant curve is also a solution; uniqueness in Local 2.1 gives \(\exp(tY)z=z\) for every \(t\). A.1 now gives \(Y\in\mathfrak b_z\). The converse follows by differentiating this same identity. Thus the kernel is exactly \(\mathfrak b_z\).

Apply this first to \(K_x\). For \(k\in K_x\), principal division defines the smooth homomorphism \(\lambda_p(k)=\delta(p,kp)\). Smoothness is PB A.2, and \((k_1k_2)p=p\lambda_p(k_1)\lambda_p(k_2)\) proves the homomorphism identity by freeness. It follows that
\[
Q_p=\{(k,\lambda_p(k)):k\in K_x\}.
\tag{E.7}
\]
The displayed graph map and its inverse projection are smooth in the embedded structures. For the graph map, its ambient smooth expression takes values in \(Q_p\), and target submanifold charts make it smooth into \(Q_p\), as in the slice argument in A.1. Consequently \(\dim Q_p=\dim K_x\). The orbit derivative of \(Q\) therefore has rank \(\dim Q-\dim Q_p=\dim K+\dim G-\dim K_x\). Equation (E.3), together with \(\dim P=\dim M+\dim G\), proves (E.5).

To attain equality at a fixed \(p\), choose a complement \(V\) to the orbit image in \(T_pP\). A linear subspace in a coordinate chart on \(P\) gives a local embedded submanifold through \(p\) with tangent \(V\). Choose \(J\subset\mathfrak q\) mapping isomorphically to the orbit image and take \(H=\exp(J)\) locally. The same inverse-function argument gives a diffeomorphism on \(H\times S\) after shrinking. Its derivative stays invertible at every \((e,p')\) in this product, so this \(S\) is a transverse patch throughout. Its dimension is the right side of (E.5) at the chosen point. This proves the minimality assertion without requiring constant orbit dimension near \(p\).

Finally, the images of local principal-bundle sections are embedded submanifolds with tangent complement to \(V_pP\), by the bundle charts in PB A.2. They satisfy (E.3) for any symmetry action. A principal atlas thus supplies a transverse covering. For the claimed equivalence in the definition, if \(\pi(p)=k\pi(p_\alpha)\), then \(p=kp_\alpha b\) for a unique \(b\in G\), so \(p=\Theta((k,b^{-1}),p_\alpha)\). The converse follows by applying \(\pi\). □

Fix a transverse covering. A collection of reduced data consists of smooth maps
\[
\psi_\alpha:\mathfrak k\times TS_\alpha\longrightarrow\mathfrak g,
\tag{E.8}
\]
whose restrictions to \(\mathfrak k\oplus T_pS_\alpha\) are jointly linear for each \(p\). Thus \(\psi_\alpha(X,v)\) splits linearly between \(X\) and \(v\); the value of the zero tangent specifies its base point. Impose the following two conditions for every \(q=(k,a)\in Q\) and every \(p\in S_\alpha\), \(p'\in S_\beta\) with \(p'=\Theta_q(p)\):
\[
\begin{split}
&D_{p'}(X,A,v')=d\Theta_q(v),\quad
v\in T_pS_\alpha,\ v'\in T_{p'}S_\beta\\
&\hspace{8mm}\Longrightarrow\quad
\psi_\beta(X,v')-A=\rho(q)\psi_\alpha(0,v),
\end{split}
\tag{E.9}
\]
and
\[
\psi_\beta(\operatorname{Ad}(k)X,0_{p'})
=\rho(q)\psi_\alpha(X,0_p)
\quad(X\in\mathfrak k).
\tag{E.10}
\]
In (E.9), \(X\) and \(A\) range over \(\mathfrak k\) and \(\mathfrak g\), respectively. In particular \(d\Theta_q(v)\) is not assumed tangent to \(S_\beta\); the other terms of the decomposition are essential.

**Theorem E.2 (Hanusch's reconstruction).** For an arbitrary smooth action of \(K\) by principal automorphisms, invariant principal connections on \(P\) correspond bijectively to the reduced data (E.8) satisfying (E.9)–(E.10). The forward map is
\[
\psi_\alpha(X,v)=\omega_p(X_P(p)+v),\qquad v\in T_pS_\alpha.
\tag{E.11}
\]
For reconstruction put
\[
\lambda_{\alpha,p}(X,A,v)=\psi_\alpha(X,v)-A.
\tag{E.12}
\]
This factors uniquely as \(\lambda_{\alpha,p}=\ell_{\alpha,p}\circ D_p\), with \(\ell_{\alpha,p}:T_pP\to\mathfrak g\) linear. The reconstructed form is
\[
\omega_{\Theta_q(p)}(w)
=\rho(q)\ell_{\alpha,p}(d\Theta_{q^{-1}}w).
\tag{E.13}
\]
It is independent of all choices and smooth on the entire bundle, including points on singular orbits.

**Proof.** An invariant principal connection satisfies
\(\Theta_q^*\omega=\rho(q)\omega\): the \(K\)-action preserves it and right multiplication by \(a^{-1}\) pulls it back by \(\operatorname{Ad}(a)\), Conn A.2. Applying this identity and vertical reproduction to (E.2) gives (E.9). For (E.10), differentiate
\[
\Theta_q(\exp(tX)p)=\exp(t\operatorname{Ad}(k)X)\Theta_q(p),
\tag{E.14}
\]
which follows from the exponential conjugation identity and commutation with the principal action. Invariance then gives (E.10). Formula (E.11) is smooth and jointly linear as required. This proves necessity.

Conversely take reduced data satisfying the two conditions. Set \(q=e\), \(\beta=\alpha\), and \(v=0_p\) in (E.9). It gives
\[
D_p(X,A,v')=0\quad\Longrightarrow\quad
\lambda_{\alpha,p}(X,A,v')=0.
\tag{E.15}
\]
Since \(D_p\) is onto by E.1, define \(\ell_{\alpha,p}(w)\) by evaluating \(\lambda_{\alpha,p}\) on any preimage of \(w\). Two preimages differ by a vector in \(\ker D_p\), and (E.15) makes their values equal. Linearity of \(D_p\) and \(\lambda_{\alpha,p}\) proves linearity of \(\ell\). Surjectivity proves uniqueness. In particular,
\[
\ell_{\alpha,p}(X_P(p))=\psi_\alpha(X,0_p),\quad
\ell_{\alpha,p}(v)=\psi_\alpha(0,v),\quad
\ell_{\alpha,p}(A^\#(p))=A.
\tag{E.16}
\]
For the last identity, use the preimage \((0,-A,0_p)\).

The implication (E.15) is the kernel inclusion \(\ker D_p\subseteq\ker\lambda_{\alpha,p}\) needed for factorization. The displayed inclusion in the cited version's Lemma 4.7(3) is reversed; its compatibility condition gives (E.15), which is what we have proved and use here.

We next prove compatibility on all ambient tangent vectors at patch points. If \(p'=\Theta_q(p)\), then
\[
\ell_{\beta,p'}\circ d\Theta_q=\rho(q)\ell_{\alpha,p}
\quad\text{on }T_pP.
\tag{E.17}
\]
For a vector \(X_P(p)\), this is (E.14), (E.16) and (E.10). For a principal vector, differentiating
\(\Theta_q(p\exp(tA))=p'\exp(t\operatorname{Ad}(a)A)\)
and using (E.16) proves it. For \(v\in T_pS_\alpha\), surjectivity at \(p'\) provides \(X,A,v'\) with \(D_{p'}(X,A,v')=d\Theta_q(v)\). Condition (E.9) and the factorization of \(\lambda\) give (E.17) on \(v\). These three types of vectors span \(T_pP\) by (E.3), proving (E.17) everywhere.

Every point of \(P\) can be represented as \(\Theta_q(p)\) with \(p\) on a patch. To check independence in (E.13), suppose also \(z=\Theta_r(p')\). Then \(p'=\Theta_{r^{-1}q}(p)\). Applying (E.17) with \(r^{-1}q\), and using \(\rho(r)\rho(r^{-1}q)=\rho(q)\), proves equality of the two expressions in (E.13). The chain rule supplies the same identity for the tangent maps. Thus the formula defines a linear form on every tangent space, without yet assuming smoothness.

Its covariance under \(\Theta\) is immediate from the definition: representing \(z\) by \((q,p)\) represents \(\Theta_hz\) by \((hq,p)\), so
\[
\omega_{\Theta_hz}(d\Theta_hw)=\rho(h)\omega_z(w).
\tag{E.18}
\]
Vertical reproduction holds at patch points by (E.16). At \(z=\Theta_{(k,a)}p\), the inverse differential sends \(A^\#(z)\) to \((\operatorname{Ad}(a^{-1})A)^\#(p)\), by the same principal-vector identity used in (E.17). Formula (E.13) therefore gives \(\omega_z(A^\#(z))=A\).

It remains to establish smoothness; this is the step for which transversality matters. On \(Q\times S_\alpha\), define the one-form
\[
\eta_\alpha|_{(q,p)}(\dot q,v)
=\rho(q)\lambda_{\alpha,p}(\theta^Q_q\dot q,v),
\tag{E.19}
\]
where \(\theta^Q_q\dot q\in\mathfrak q=\mathfrak k\oplus\mathfrak g\) supplies the first two arguments of \(\lambda\). The Maurer form is smooth, \(\psi_\alpha\) is smooth, and \(\rho\) is smooth, so (E.19) is a smooth one-form. Formula (E.6), the factorization of \(\lambda\), and (E.13) give the pointwise pullback identity
\[
F_{S_\alpha}^*\omega=\eta_\alpha.
\tag{E.20}
\]
E.1 supplies a diffeomorphism \(f:H\times S'\to U\) obtained by restricting this action map. Thus on \(U\), the defined form is \((f^{-1})^*(\eta_\alpha|_{H\times S'})\), which is smooth. Translates \(\Theta_q(U)\) cover \(P\); equation (E.18) expresses \(\omega\) on each translate as the pullback of this smooth local form by \(\Theta_{q^{-1}}\), followed by the fixed linear map \(\rho(q)\). This proves global smoothness, with no assumption about orbit dimensions elsewhere.

Taking \(h=(k,e)\) in (E.18) gives \(K\)-invariance. Taking \(h=(e,a^{-1})\) gives principal equivariance under right multiplication by \(a\). Together with the proved reproduction identity, Conn A.2 shows that \(\omega\) is a principal connection. At \(q=e\) and \(w=X_P(p)+v\), equations (E.12)–(E.13) recover \(\psi_\alpha(X,v)\). Conversely an invariant connection with these data must satisfy the factorization and (E.13), so it is uniquely determined. This proves both inverse identities and the bijection.

For comparison, in the transitive situation a single patch \(S=\{p_0\}\) suffices. In (E.9) there is then no patch tangent, and \(D_{p_0}(X,A,0)=0\) means \(X\in\mathfrak k_{x_0}\), \(A=(\lambda_{p_0})_*X\), by the stabilizer calculation in E.1. Thus (E.9) reduces to the restriction of \(W\) in (B.5). The returning elements \(q\) are exactly the graph (E.7), so (E.10) reduces to its full isotropy-equivariance condition. This recovers B.2 with the same signs. □

## F. Sections, gauge actions and nontransitive examples

The construction source for this part is Maximilian Hanusch's free [corrected author version, *A Characterization of Invariant Connections*, arXiv:1310.0318v3](https://arxiv.org/abs/1310.0318v3), the single-patch discussion in §4.1, Example 4.10 and §5. Its [CC BY-NC-SA 3.0 terms](https://creativecommons.org/licenses/by-nc-sa/3.0/) are retained here with the attribution. All arguments below are written out using E.1–E.2 and the exact earlier programme results. In particular, the gauge-change and radial formulas are derived directly with our right principal action; source formulas are not accepted without checking them.

**Theorem F.1 (a transverse section with constant stabilizer).** Let \(N\) be an injectively immersed submanifold of \(M\) meeting each \(K\)-orbit in exactly one point. Suppose
\[
T_xN+\{X_M(x):X\in\mathfrak k\}=T_xM
\quad(x\in N),
\tag{F.1}
\]
and let \(s:N\to P\) be a smooth section. Suppose the stabilizer \(K_x=H\) and the homomorphism \(\lambda_x:H\to G\), defined by \(h s(x)=s(x)\lambda_x(h)\), are independent of \(x\in N\); write the common homomorphism as \(\lambda\). Assume also
\[
\dim N=\dim M-\dim K+\dim H.
\tag{F.2}
\]
Then invariant connections correspond bijectively to a smooth family \(W_x:\mathfrak k\to\mathfrak g\) of linear maps and a smooth \(\mathfrak g\)-valued one-form \(\mu\) on \(N\) such that
\[
\begin{split}
W_x(Z)&=\lambda_*Z &&(Z\in\mathfrak h),\\
W_x(\operatorname{Ad}(h)X)&=\operatorname{Ad}(\lambda(h))W_x(X)
 &&(h\in H),\\
\mu_x(v)&=\operatorname{Ad}(\lambda(h))\mu_x(v)
 &&(h\in H,\ v\in T_xN).
\end{split}
\tag{F.3}
\]
Equivalently, the constant-stabilizer hypothesis says that \(Q_{s(x)}\subset K\times G\) is the same subgroup for every \(x\in N\).

The corresponding reduced data on \(s(N)\) are
\(\psi(X,ds(v))=W_x(X)+\mu_x(v)\). No compactness or connectedness of \(H\) is required.

**Proof.** By (E.7), \(Q_{s(x)}\) is the graph of \(\lambda_x:K_x\to G\). Equality of these graphs implies equality of their first-coordinate projections, hence a common subgroup \(H=K_x\). For each \(h\in H\), equality of the unique second coordinate in the graph then gives a common value \(\lambda_x(h)\). Conversely, common \(H\) and \(\lambda\) give equal graphs. This proves the stated equivalence, including all disconnected components.

Since \(\pi s\) is the inclusion of \(N\), the map \(s\) is an injective immersion, with its own manifold structure. Equation (F.1) implies that \(s(N)\) is a transverse patch: project an arbitrary tangent vector to \(M\), write its projection as a sum of an orbit vector and an \(N\)-tangent, lift these using \(X_P\) and \(ds\), and represent the remaining vertical vector by Conn A.2. Each base orbit meets \(N\), so E.1 makes this a transverse covering with one patch.

The orbit image at \(x\) has dimension \(\dim K-\dim H\), by E.1's stabilizer-kernel proof. Equations (F.1)–(F.2) therefore make the sum in (F.1) direct. If two points of \(s(N)\) belong to the same \(Q\)-orbit, their base points belong to the same \(K\)-orbit and hence are equal. As \(s\) is a section, the two points themselves are equal. The returning elements are exactly \((h,\lambda(h))\), by (E.7). Each such element fixes every point of \(s(N)\), since \(H\) and \(\lambda\) are common to the entire section. Its differential on \(T s(N)\) is consequently the identity, as follows by differentiating curves in \(s(N)\).

At \(p=s(x)\), the equality
\[
D_p(X,A,ds(v'))=ds(v)
\tag{F.4}
\]
projects to \(X_M(x)+v'=v\). Directness of (F.1) gives \(X\in\mathfrak h\) and \(v'=v\). Differentiating \(\exp(tX)s(x)=s(x)\lambda(\exp(tX))\) then shows that (F.4) is equivalent to these conditions together with \(A=\lambda_*X\), because principal fundamental vectors are injectively parametrized. Thus the kernel condition in (E.9), with \(q=e\), is precisely the first identity of (F.3).

For a returning \(q=(h,\lambda(h))\), its differential fixes \(ds(v)\). In (E.9) we again have exactly (F.4). Subtracting \(A=\lambda_*X\) leaves \(\mu_x(v)\) on the left, and the right is \(\operatorname{Ad}(\lambda(h))\mu_x(v)\). This is the last identity of (F.3). Condition (E.10) is exactly the middle identity. Every jointly linear smooth \(\psi\) splits uniquely as \(W+\mu\), so necessity, sufficiency and the bijection all follow from E.2. □

**Theorem F.2 (actions by gauge transformations).** Suppose every element of \(K\) induces the identity on \(M\). Choose local sections \(s_\alpha:U_\alpha\to P\). On an overlap define the smooth map \(\delta_{k,\alpha\beta}:U_\alpha\cap U_\beta\to G\) by
\[
s_\beta(x)=k s_\alpha(x)\,\delta_{k,\alpha\beta}(x).
\tag{F.5}
\]
Invariant connections correspond bijectively to families \(A_\alpha\in\Omega^1(U_\alpha,\mathfrak g)\) satisfying, for every \(k\in K\),
\[
A_\beta
=\operatorname{Ad}(\delta_{k,\alpha\beta}^{-1})A_\alpha
 +\delta_{k,\alpha\beta}^*\theta^G.
\tag{F.6}
\]
Here \(k\) is held fixed when differentiating \(\delta\). For \(k=e\) this is the usual transition rule for local connection potentials.

**Proof.** Smoothness of \(\delta\), jointly in \(k,x\), follows from the principal division map PB A.2. If \(h_{\alpha\beta}=\delta_{e,\alpha\beta}\) and \(k s_\alpha(x)=s_\alpha(x)\lambda_{\alpha,x}(k)\), freeness gives
\(\delta_{k,\alpha\beta}=\lambda_{\alpha,x}(k)^{-1}h_{\alpha\beta}\).
An invariant connection has potential \(A_\alpha\) in the section \(k s_\alpha\) as well as in \(s_\alpha\). Applying the proved change-of-section formula Conn A.3 to (F.5) gives (F.6), including its inverse inside the adjoint.

Conversely, the \(k=e\) identities glue the family to a unique principal connection \(\omega\), by Conn A.3. For fixed \(k\), its pullback \(k^*\omega\) is a principal connection: the automorphism commutes with right translations and carries \(A^\#\) to \(A^\#\), so both axioms of Conn A.2 hold. Let \(B_\alpha=s_\alpha^*k^*\omega\), the potential of \(\omega\) in \(k s_\alpha\). The actual change-of-section identity is
\[
A_\beta=\operatorname{Ad}(\delta_{k,\alpha\beta}^{-1})B_\alpha
 +\delta_{k,\alpha\beta}^*\theta^G.
\]
Compare with (F.6), taking \(\beta=\alpha\) on \(U_\alpha\). Invertibility of the adjoint gives \(B_\alpha=A_\alpha\) throughout every chart. A connection is determined by these potentials, again by Conn A.3. Hence \(k^*\omega=\omega\) for every \(k\). This proves the converse and uniqueness. The source's displayed gauge-consistency equation uses \(\operatorname{Ad}(\delta)\) with the same convention (F.5); the direct calculation above gives \(\operatorname{Ad}(\delta^{-1})\), which is the formula used here. □

**Theorem F.3 (one patch at a common orbit-closure point).** Suppose \(x_0\) belongs to the closure of every base \(K\)-orbit. If a transverse patch \(S\subset P\) contains any point over \(x_0\), then \(\{S\}\) is a transverse covering. Thus E.2 describes all invariant connections from the reduced data on that single patch, with both of its compatibility conditions retained.

**Proof.** At \(p_0\in S\) over \(x_0\), E.1 gives a diffeomorphism from \(H\times S'\) onto an open neighbourhood \(U\subset P\), where \(S'\subset S\). The principal projection is open: in each bundle chart it is a product projection, which maps a union of open rectangles to a union of open base sets. Thus \(\pi(U)\) is an open neighbourhood of \(x_0\). Every base orbit meets it, by the definition of closure. Given such an intersection point, choose \(z\in U\) over it and write \(z=\Theta_q(p)\) with \(p\in S'\). Its projection belongs to the orbit of \(\pi(p)\). Therefore every orbit meets \(\pi(S)\), and E.1's covering criterion applies. E.2 now gives the claimed classification. □

**Theorem F.4 (partial translations, curvature and a rectangle).** Let a finite dimensional real vector space split as \(X=V\oplus W\), and let \(K=(V,+)\) act on \(X\times G\) by translation in \(V\) and trivially in the principal coordinate. Every invariant connection is determined by an arbitrary smooth family \(a_w:V\to\mathfrak g\) of linear maps and an arbitrary \(\beta\in\Omega^1(W,\mathfrak g)\). Its potential in the global identity section and its full form are
\[
\begin{split}
A_{(v,w)}(u,z)&=a_w(u)+\beta_w(z),\\
\omega_{(v,w,g)}(u,z,\eta)&=
\operatorname{Ad}(g^{-1})\bigl(a_w(u)+\beta_w(z)\bigr)+\theta^G_g(\eta).
\end{split}
\tag{F.7}
\]
On constant vectors \((u,z),(u',z')\), its curvature potential is
\
\begin{split}
F((u,z),(u',z'))={}&(da)_w[z-(da)_wz'
 +(d\beta)_w(z,z')\\
&+[a_w(u)+\beta_w(z),\ a_w(u')+\beta_w(z')].
\end{split}
\tag{F.8}
\]

For the additive structure group \(G=(\mathbb R,+)\) on \(\mathbb R^2\), the potential \(A=y^2dx\) has \(F=-2y\,dx\wedge dy\). Horizontal transport around the rectangle starting at \((0,y_0)\), then moving right by \(a\), up by \(b\), left by \(a\) and down by \(b\), adds
\[
a\bigl(2y_0b+b^2\bigr)
\tag{F.9}
\]
to the principal coordinate.

**Proof.** The patch \(S=W\times\{e\}\) gives the global action map
\[
(V\times G)\times (W\times\{e\})\longrightarrow X\times G,
\qquad ((v,g),(w,e))\longmapsto(v+w,g^{-1}).
\]
Its inverse is \((v+w,h)\mapsto((v,h^{-1}),(w,e))\), where the unique \(v,w\) are the two linear projections of \(X=V\oplus W\). Both maps are smooth by linearity and smooth group inversion, and substitution verifies both inverse identities. Thus this action map is a diffeomorphism; every orbit meets the patch once and its stabilizers are trivial.

By Conn A.3 every connection is uniquely described by a smooth \(\mathfrak g\)-valued one-form \(A\) on \(X\). The lifted translation preserves the global identity section. Therefore it preserves \(\omega\) exactly when it preserves \(A\), since pullback connections are determined by their potentials. In the linear product coordinates this says that all coefficients of \(A\) are independent of \(v\). Splitting a tangent into its \(V\) and \(W\) components gives the unique \(a\) and \(\beta\) in (F.7), with their smoothness and linearity. Conversely such a form is invariant under every translation, and its full expression follows from Conn A.3.

For two constant vector fields their bracket is zero. The exterior derivative formula in Curvature A.2 gives the first three terms of (F.8); the coefficient \(\frac12[A,A]\) on the two vectors is the last bracket, by Curvature A.1. Curvature A.4 gives \(F=dA+\frac12[A,A]\), proving the formula.

In the additive example the Lie bracket vanishes and direct differentiation gives \(d(y^2dx)=2y\,dy\wedge dx\). The horizontal equation is \(g'=-y^2x'\), by Conn C.1. Only the horizontal sides contribute to its integral; the integral of \(A\) is \(a y_0^2-a(y_0+b)^2\). Taking its negative yields (F.9). This is the actual transport with the stated orientation, rather than a curvature-area approximation. □

**Example F.5 (why a cubic section is insufficient).** Let horizontal translations act on \(\mathbb R^2\times G\) as in F.4, and assume \(\mathfrak g\) contains a nonzero \(B\). The smooth embedded curve
\[
s(t)=((t,t^3),e),\qquad t\in\mathbb R,
\]
meets each base orbit once, but fails transversality at \(t=0\). The smooth jointly linear data
\[
\psi_t(u,ds_t(r))=3trB
\tag{F.10}
\]
obey the algebraic compatibility conditions (E.9)–(E.10) wherever those conditions are interpreted on this curve. Nevertheless no smooth invariant connection induces them.

**Proof.** The curve is embedded because projection to the first coordinate is its smooth inverse onto the parameter line, and its derivative has first coordinate one. Cubing is a bijection of \(\mathbb R\), so each horizontal orbit meets the curve exactly once. At zero, its base tangent is horizontal, equal to the orbit tangent, and their sum has dimension one rather than two. Hence (E.3) fails.

Two curve points lie in the same \(Q\)-orbit only when their parameters agree, and then the returning element is the identity: a translation fixing a point is zero and freeness forces its principal component to be \(e\). Thus (E.10) is automatic. In (E.9), the equality of tangents is
\[
(u+r',\ 3t^2r',\ -A)=(r,\ 3t^2r,\ 0)
\]
at the principal identity. If \(t\ne0\), it gives \(r'=r\), \(u=0\), \(A=0\). If \(t=0\), it gives \(u+r'=r\), \(A=0\), and both values in (F.10) are zero. Thus (E.9) holds in both cases.

By F.4, the potential of any putative invariant connection is \(A=a(y)dx+b(y)dy\), with smooth \(\mathfrak g\)-valued coefficients. Its reduced data would be
\[
a(t^3)(u+r)+3t^2 b(t^3)r.
\]
Comparing the coefficient of \(u\) with (F.10) shows \(a=0\) everywhere. Comparing the coefficient of \(r\) then gives \(b(t^3)=B/t\) for \(t\ne0\). Choose a linear coordinate of \(\mathfrak g\) nonzero on \(B\); its value diverges as \(t\to0\). This contradicts continuity of \(b\). Thus algebraic compatibility on a nontransverse set does not supply the smooth reconstruction in E.2. □

**Example F.6 (gauge symmetries can exclude every connection).** For a smooth real function \(f\) on \(M\), let \(K=(\mathbb R,+)\) act on \(M\times U(1)\) by
\[
t\cdot(x,g)=(x,e^{it f(x)}g).
\tag{F.11}
\]
If \(df\) is nonzero at any point, no invariant connection exists. If \(df=0\) everywhere, every connection is invariant. In particular \(f(x)=x\) on \(\mathbb R\) gives the first case, whereas constant \(f\) gives the second.

**Proof.** The exponential identity proves the action law, and it commutes with the principal action. Let \(A\) be any potential in the global identity section. By Conn A.3, its potential after pullback by \(t\) is
\[
A+(e^{it f})^{-1}d(e^{it f})=A+it\,df,
\]
since the adjoint representation of the abelian group \(U(1)\) is the identity. Differentiation of sine and cosine gives the displayed derivative directly. Equality for every \(t\) is therefore equivalent to \(df=0\), independent of \(A\). Conn A.3 identifies equality of potentials with equality of full connections, proving both assertions. □

**Example F.7 (an upper-triangular obstruction).** Let \(B\subset\operatorname{GL}(2,\mathbb R)\) be the subgroup of invertible upper-triangular matrices. The principal bundle
\[
\operatorname{GL}(2,\mathbb R)\longrightarrow\operatorname{GL}(2,\mathbb R)/B
\tag{F.12}
\]
has no connection invariant under left multiplication by \(B\).

**Proof.** The group \(B\) is closed in \(\operatorname{GL}(2,\mathbb R)\), since its lower-left entry is zero. It is a subgroup by direct multiplication and the inverse formula. A.1 makes it an embedded Lie subgroup, with Lie algebra \(\mathfrak b\) all upper-triangular matrices: tangents have lower-left entry zero, and every such tangent is realized by \(I+tT\) for sufficiently small \(t\). Local 4.1 therefore proves that (F.12) is a smooth principal \(B\)-bundle. Left multiplication commutes with its principal right action.

If an invariant connection existed, its value \(L=\omega_I:\mathfrak{gl}(2,\mathbb R)\to\mathfrak b\) would be the identity on \(\mathfrak b\), by vertical reproduction. For each \(b\in B\), the map \(p\mapsto b p b^{-1}\) fixes \(I\). Left invariance and right principal equivariance imply
\[
L(bTb^{-1})=bL(T)b^{-1}.
\tag{F.13}
\]
Set \(U=E_{12}\), \(V=E_{21}\), \(H=E_{11}-E_{22}\), and \(b=I+U\). Then \(U^2=0\), so \(b^{-1}=I-U\), and multiplication gives
\[
bVb^{-1}=V+H-U.
\]
By linearity and reproduction, (F.13) gives
\(H-U=bL(V)b^{-1}-L(V)\).
For an upper-triangular matrix \(T=\left(\begin{smallmatrix}a&c\\0&d\end{smallmatrix}\right)\), multiplication gives
\(bTb^{-1}-T=\left(\begin{smallmatrix}0&d-a\\0&0\end{smallmatrix}\right)\).
Its diagonal is zero. The left side \(H-U\) has first diagonal entry one, a contradiction. No orbit decomposition or externally cited structural theorem is needed. □

**Theorem F.8 (dilation and smoothness at the origin).** Let \(n\ge1\) and let \(\mathbb R_{>0}\) act on \(\mathbb R^n\times G\) by \(\lambda\cdot(x,g)=(\lambda x,g)\). The only invariant connection on the whole bundle has potential \(A=0\), hence full form \(\theta^G\).

On the punctured bundle, put \(r=\|x\|\) and \(n_x=x/r\). Every invariant connection instead has an arbitrary smooth function \(b:S^{n-1}\to\mathfrak g\) and arbitrary \(\beta\in\Omega^1(S^{n-1},\mathfrak g)\), with
\[
\begin{split}
A_x(v)&=b(n_x)\frac{\langle n_x,v\rangle}{r}
 +\beta_{n_x}\left(\frac{v-n_x\langle n_x,v\rangle}{r}\right),\\
\omega_{(x,g)}(v,\eta)&=\operatorname{Ad}(g^{-1})A_x(v)+\theta^G_g(\eta).
\end{split}
\tag{F.14}
\]
It extends smoothly across the origin precisely when both \(b\) and \(\beta\) vanish.

**Proof.** The global identity section is preserved by dilation, so invariance of the connection is exactly
\(\lambda A_{\lambda x}(v)=A_x(v)\), by Conn A.3. On the whole space, continuity of \(A\) at the origin makes \(A_{\lambda x}(v)\) bounded as \(\lambda\downarrow0\), for fixed \(x,v\). Multiplication by \(\lambda\) gives \(A_x(v)=0\). Conversely the zero potential is preserved by all dilations.

On the punctured space the polar-coordinate map \((r,n)\mapsto rn\) is a smooth diffeomorphism from \(\mathbb R_{>0}\times S^{n-1}\), with inverse \((\|x\|,x/\|x\|)\). The sphere's charts are obtained by solving a nonzero coordinate as \(\pm\sqrt{1-\sum y_i^2}\); the square root is smooth on the positive half-line by the inverse-function theorem Local 1.2. These charts also show \(T_nS^{n-1}=n^\perp\) by differentiating \(\langle n,n\rangle=1\); every orthogonal vector is realized by differentiating \((n+tz)/\|n+tz\|\). For \(n=1\) the sphere has two discrete points and the angular tangent space is zero, with the same formulas.

Write the polar pullback as \(C_{(r,n)}(\dot r,z)\). Dilation sends \((r,n)\) to \((\lambda r,n)\) and the tangent to \((\lambda\dot r,z)\). Invariance, applied with \(\lambda=1/r\), gives
\[
C_{(r,n)}(\dot r,z)=C_{(1,n)}(\dot r/r,z)
=b(n)\dot r/r+\beta_n(z).
\]
Here \(b(n)=C_{(1,n)}(1,0)\) and \(\beta_n(z)=C_{(1,n)}(0,z)\); these are smooth, unique and arbitrary. Differentiation gives \(dr_x(v)=\langle n_x,v\rangle\) and \(d(n_x)(v)=(v-n_x\langle n_x,v\rangle)/r\), proving (F.14). Conversely this expression is smooth on the punctured space and is invariant by the same calculation. Conn A.3 gives its full principal form.

If such a connection extends smoothly over zero, each dilated pullback equals it off zero and hence also at zero by continuity of the coefficients. Its extension is therefore invariant on the whole space and must have zero potential by the first paragraph. The uniqueness of \(b,\beta\) then forces both to vanish. Conversely their vanishing gives the smooth zero extension. For instance, \(b=B\ne0\), \(\beta=0\) gives \(A=B\,dr/r\), a smooth invariant punctured potential with no extension. The angular factor \(1/r\) and the adjoint factor in (F.14) are both required by differentiation and principal equivariance. □

**Theorem F.9 (an arbitrary lift on a trivial bundle).** Let \(K\) act by principal automorphisms on \(P=M\times G\). There is a unique smooth map \(c:K\times M\to G\) with
\[
k\cdot(x,g)=(\varphi_k(x),c(k,x)g),\qquad
c(kk',x)=c(k,\varphi_{k'}x)c(k',x).
\tag{F.15}
\]
Invariant connections correspond exactly to smooth \(A\in\Omega^1(M,\mathfrak g)\) satisfying
\[
A_x(v)=\operatorname{Ad}(c(k,x)^{-1})
A_{\varphi_kx}(d\varphi_kv)
 +(c(k,\cdot)^*\theta^G)_x(v)
\tag{F.16}
\]
for every \(k,x,v\). Set
\(\chi_x(X)=\left.\frac{d}{dt}\right|_0c(\exp(tX),x)\in T_eG=\mathfrak g\).
The reduced data on the transverse covering \(M\times\{e\}\) are then
\[
\psi_x(X,v)=A_x(X_M(x)+v)+\chi_x(X).
\tag{F.17}
\]
In particular \(A_x(v)=\psi_x(0,v)\); reduced data satisfying E.2 recover precisely (F.16)–(F.17), with no additional arbitrary symmetry-direction term.

**Proof.** Apply the automorphism to \((x,e)\) to define \(\varphi\) and \(c\); smoothness is inherited from the action. Commutation with right multiplication gives its value on \((x,g)\), and composing two actions proves the cocycle identity. The identity element acts trivially, so \(c(e,x)=e\). Differentiation at \(t=0\) therefore defines the smooth family of linear maps \(\chi_x\); linearity also follows from its being the derivative in the group variable at \(e\).

By Conn A.3, an arbitrary connection is uniquely given by
\(\omega_{(x,g)}(v,\eta)=\operatorname{Ad}(g^{-1})A_x(v)+\theta^G_g(\eta)\).
Pulling this formula back along \(x\mapsto k\cdot(x,e)=(\varphi_kx,c(k,x))\) gives exactly the right side of (F.16). The pullback by a principal automorphism is a principal connection, as checked in F.2; equality with \(\omega\) is thus equivalent to equality of these potentials in the identity section. This proves necessity and sufficiency of (F.16), as well as uniqueness.

The fundamental field at \((x,e)\) is \((X_M(x),\chi_x(X))\). Adding the section tangent \((v,0)\) and applying the formula for \(\omega\) at \(g=e\) proves (F.17). The identity section is a transverse covering by E.1. Hence E.2 says exactly that every admissible \(\psi\) arises from the unique invariant connection just described. Taking \(X=0\) gives \(A\), and substituting back gives its forced value on symmetry directions. This proves the last assertion in both directions. When \(c(k,x)\) is independent of \(x\), (F.16) reduces to \(\varphi_k^*A=\operatorname{Ad}(c(k))A\); for the trivial lift it reduces to ordinary invariance of \(A\). □

## G. Smooth functions of squared radius

The next two proofs supply the smooth-extension step needed at the origin. For the jet construction we use Bill Casselman's freely accessible author note [*Variations on a theorem of Émile Borel*, revised 21 October 2020](https://personal.math.ubc.ca/~cass/research/pdf/Emile.pdf), §1, Theorem 1.1 and Lemma 1.2, native pages 1–3. We write out the estimates and convergence argument below. Smooth cutoffs are already proved in Local 3.1; integration and uniform-limit estimates are proved in Local 0.2–0.3. No external extension theorem is a proof provider.

**Lemma G.1 (prescribing a smooth jet at one point).** For every real sequence \((a_j)_{j\ge0}\), there is a smooth \(b:\mathbb R\to\mathbb R\) with \(b^{(j)}(0)=a_j\) for all \(j\).

**Proof.** Choose a smooth cutoff \(\phi\), equal to one near zero and supported in \((-1,1)\), by Local 3.1. For \(j\ge1\) set
\[
b_j(t)=\frac{a_j}{j!}t^j\phi(t/\varepsilon_j).
\tag{G.1}
\]
The higher product rule, obtained by induction from Local 0.3, gives, for \(0\le k<j\),
\[
\sup_{t\in\mathbb R}|b_j^{(k)}(t)|
\le |a_j|\sum_{i=0}^k
\binom{k}{i}\frac{\sup|\phi^{(i)}|}{(j-k+i)!}
\varepsilon_j^{j-k}.
\tag{G.2}
\]
Indeed the \(i\)-th derivative falling on the cutoff contributes \(\varepsilon_j^{-i}\), while the polynomial contributes \(t^{j-k+i}/(j-k+i)!\); all terms vanish outside \(|t|\le\varepsilon_j\). The suprema are finite by compactness, Local 0.1. Since \(j-k>0\), choose \(0<\varepsilon_j\le2^{-j}\) so that (G.2) is at most \(2^{-j}\) for every \(k<j\). There are only finitely many such requirements for each \(j\).

Let \(S_N=a_0+\sum_{j=1}^N b_j\). For every fixed \(k\), the derivatives \(S_N^{(k)}\) converge uniformly on \(\mathbb R\) to a continuous function \(u_k\): the finitely many terms \(j\le k\) cause no convergence issue, and the remaining tail is bounded by \(\sum_{j>k}2^{-j}\). Completeness and the uniform continuity-of-limit argument are Local 0.2. To justify differentiation of the limit, fix \(s,t\). Local 0.3 gives
\[
S_N^{(k)}(t)-S_N^{(k)}(s)
=\int_s^t S_N^{(k+1)}(v)\,dv.
\]
Uniform convergence and the integral bound in Local 0.3 allow passage to the limit. Thus \(u_k(t)-u_k(s)=\int_s^t u_{k+1}(v)\,dv\), so \(u_k'=u_{k+1}\). Induction proves that \(b=u_0\) is smooth with derivatives \(u_k\). Near zero each individual \(b_j\) equals \(a_jt^j/j!\). Consequently \(b_j^{(k)}(0)\) is \(a_j\) if \(j=k\) and zero otherwise; evaluation of the uniformly convergent derivative series at zero proves \(b^{(k)}(0)=a_k\). □

**Lemma G.2 (even and odd smooth extension).** If \(f:\mathbb R\to\mathbb R\) is smooth and even, there is a smooth \(F:\mathbb R\to\mathbb R\) with \(f(r)=F(r^2)\). The restriction of \(F\) to \([0,\infty)\) is unique. If \(b\) is smooth and odd, it has the form \(b(r)=rG(r^2)\) with smooth \(G\) on \(\mathbb R\). If \(c\) is smooth and even with \(c(0)=0\), then \(c(r)=r^2H(r^2)\) with smooth \(H\). The restrictions of \(G,H\) to the nonnegative half-line are also unique.

**Proof.** Define \(h(s)=f(\sqrt{s})\) for \(s>0\), and \(h(0)=f(0)\). Smoothness away from zero follows from Local 1.2 applied to squaring on the positive half-line. We first prove that \(h\) has derivatives of every order continuous from the right at zero.

All odd derivatives of \(f\) vanish at zero: differentiate \(f(-r)=f(r)\) and set \(r=0\). Fix \(N\ge0\), and subtract the even polynomial
\[
P_N(r)=\sum_{j=0}^N\frac{f^{(2j)}(0)}{(2j)!}r^{2j}.
\tag{G.3}
\]
The remainder \(R_N=f-P_N\) and all its derivatives through order \(2N+1\) vanish at zero. Its \((2N+2)\)-nd derivative is bounded near zero by Local 0.1. Repeated integration from zero using Local 0.3 gives, for \(0\le i\le2N+2\),
\[
|R_N^{(i)}(r)|\le C_N\frac{|r|^{2N+2-i}}{(2N+2-i)!}
\quad\text{for sufficiently small }|r|.
\tag{G.4}
\]
For negative \(r\), reverse the integral orientation and apply the same bound.

For \(r>0\), differentiation in \(s=r^2\) is the operator \(L=(2r)^{-1}d/dr\). By induction, \(L^k\), for \(k\ge1\), is a finite linear combination of operators \(r^{i-2k}(d/dr)^i\) with \(1\le i\le k\): differentiating a coefficient and differentiating the function give exactly the next exponents. Equation (G.4) therefore implies
\[
L^kR_N(r)=O(r^{2N+2-2k})\qquad(0\le k\le N),
\tag{G.5}
\]
where \(k=0\) is (G.4) itself. Applying this to the polynomial (G.3) shows that every derivative of \(h\) on \((0,\infty)\) has a finite right limit at zero, namely
\[
\lim_{s\downarrow0}h^{(k)}(s)
=\frac{k!}{(2k)!}f^{(2k)}(0)=:d_k.
\tag{G.6}
\]
For each fixed \(k\), use any \(N\ge k\) in (G.5).

These limits are genuine one-sided derivatives of the continuous extensions. On \([\epsilon,s]\), the fundamental theorem gives the difference of consecutive derivatives as the integral of the next one. Let \(\epsilon\downarrow0\). Boundedness of the extended next derivative makes its integral on \([0,\epsilon]\) tend to zero, so
\(h^{(k)}(s)-d_k=\int_0^s h^{(k+1)}(t)\,dt\).
Local 0.3 at the endpoint now proves the assertion for all orders.

Apply G.1 to the sequence \((d_k)\), obtaining a smooth \(b\) on \(\mathbb R\) with these derivatives at zero. On \([0,\infty)\) the function \(h-b\) has every right derivative equal to zero at zero. Extend it to be zero on the negative half-line. This extension \(q\) is smooth: its piecewise \(k\)-th derivative is continuous at zero for every \(k\); the preceding integral identity proves its derivative at zero is the next, zero, value. Inducting on \(k\) verifies all derivatives across the join. Set \(F=b+q\). It is smooth everywhere and equals \(h\) on \([0,\infty)\). Evenness of \(f\) gives \(f(r)=F(r^2)\) for both signs of \(r\), and every nonnegative number is a square, proving uniqueness on that half-line.

For the remaining assertions, any smooth function \(u\) with \(u(0)=0\) admits the smooth division
\[
u(r)=r\,v(r),\qquad v(r)=\int_0^1 u'(tr)\,dt.
\tag{G.7}
\]
The identity is Local 0.3. To verify smoothness, difference quotients of the integrand converge uniformly for \(t\in[0,1]\) on compact \(r\)-intervals, by the segment formula and uniform continuity of the next derivative. The integral bound therefore gives \(v^{(j)}(r)=\int_0^1t^ju^{(j+1)}(tr)\,dt\) for every \(j\), with continuous derivatives. If \(u\) is odd, \(v\) is even, first for \(r\ne0\) by division and then at zero by continuity. Apply the proved even case to \(v\). If \(u=c\) is even and vanishes at zero, its first quotient is odd and vanishes at zero, so applying (G.7) once more yields a smooth even second quotient. Applying the even case to it proves the quadratic factorization. Uniqueness for positive squared radius follows by division; continuity determines the value at zero. □

## H. Rotational connections, Euclidean lifts and flat examples

The free construction source is Maximilian Hanusch's [*A Characterization of Invariant Connections*, corrected arXiv:1310.0318v3](https://arxiv.org/abs/1310.0318v3), Example 5.8, Example 5.12 and Appendix B, under [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/). We prove the matrix, representation and smooth-extension ingredients here; in particular G.1–G.2 replace the external smooth-function references used in that source. The arguments and worked calculations below are newly written.

**Lemma H.1 (the adjoint rotations and their normalization).** Define
\[
\tau_1=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\quad
\tau_2=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
\tau_3=\begin{pmatrix}-i&0\\0&i\end{pmatrix},\qquad
\zeta(v)=v_1\tau_1+v_2\tau_2+v_3\tau_3.
\tag{H.1}
\]
Then \(\zeta:\mathbb R^3\to\mathfrak{su}(2)\) is a linear isomorphism, and
\[
\zeta(u)\zeta(v)=-\langle u,v\rangle I+\zeta(u\times v),\qquad
[\zeta(u),\zeta(v)]=2\zeta(u\times v).
\tag{H.2}
\]
Every \(\sigma\in\mathrm{SU}(2)\) has the unique form \(aI+\zeta(b)\), with \(a^2+|b|^2=1\). The equation
\[
\sigma\zeta(v)\sigma^{-1}=\zeta(R_\sigma v)
\tag{H.3}
\]
defines a smooth surjective homomorphism \(\mathrm{SU}(2)\to\mathrm{SO}(3)\), with kernel \(\{I,-I\}\), which is a two-sheeted covering. Explicitly,
\[
R_{aI+\zeta(b)}v=(a^2-|b|^2)v+2b\langle b,v\rangle+2a(b\times v).
\tag{H.4}
\]
The map \(J(v)w=v\times w\) identifies \(\mathbb R^3\) with \(\mathfrak{so}(3)\), and
\[
[J(u),J(v)]=J(u\times v),\qquad
RJ(v)R^{-1}=J(Rv)\quad(R\in\mathrm{SO}(3)).
\tag{H.5}
\]

**Proof.** D.1's sphere coordinates for \(\mathrm{SU}(2)\) give the unique expression \(aI+\zeta(b)\): in those coordinates \(z_0=a-ib_3\), \(z_1=b_2-ib_1\). Differentiating the sphere equation at \((a,b)=(1,0)\) leaves precisely the three \(b\)-coordinates, proving the asserted Lie algebra identification. Direct multiplication of the three matrices gives
\(\tau_i\tau_j=-\delta_{ij}I+\sum_k\epsilon_{ijk}\tau_k\).
For equal indices this is \(\tau_i^2=-I\); the three cyclic products are \(\tau_1\tau_2=\tau_3\), \(\tau_2\tau_3=\tau_1\), \(\tau_3\tau_1=\tau_2\), and reversing a distinct pair changes its sign. Bilinearity proves (H.2). In particular
\[
(aI+\zeta(b))(cI+\zeta(d))
=(ac-b\cdot d)I+\zeta(ad+cb+b\times d),
\tag{H.6}
\]
and the inverse of a unit element is \(aI-\zeta(b)\).

Conjugation preserves the real tangent space \(\mathfrak{su}(2)\), by differentiating curves in the group, so (H.3) defines an invertible real linear map. Applying conjugation to the symmetric and antisymmetric parts of (H.2) shows that it preserves inner products and cross products. Thus it is orthogonal and carries an oriented orthonormal basis to an oriented orthonormal basis; its determinant is one. Group composition proves the homomorphism property. Formula (H.6), applied twice, yields (H.4), and gives smoothness directly. If the conjugation is trivial, \(\zeta(b)\) commutes with all \(\zeta(v)\). By (H.2), \(b\times v=0\) for every \(v\), forcing \(b=0\); hence the kernel is exactly \(\{I,-I\}\).

For surjectivity, let \(R\in\mathrm{SO}(3)\). The determinant identities give
\[
\det(I-R)=\det(R^{-1}-I)=\det(R^T-I)
=\det(R-I)=-\det(I-R).
\]
Thus \(R\) fixes a unit vector \(n\). It preserves \(n^\perp\). Choose a unit \(e\perp n\); the pair \((e,n\times e)\) orients that plane. Its restriction there is a two-dimensional orthogonal matrix of determinant one, hence has matrix \(\left(\begin{smallmatrix}c&-d\\d&c\end{smallmatrix}\right)\), with \(c^2+d^2=1\), by its orthonormal columns. If \(c=-1\), take \(a=0\), \(b=n\). Otherwise take \(a=\sqrt{(1+c)/2}\), \(b=(d/(2a))n\). The unit equation holds, and (H.4) agrees with \(R\) on both \(n\) and its orthogonal plane. This proves surjectivity.

For completeness, \(\mathrm{SO}(3)\) is a closed subgroup of the matrix Lie group \(\mathrm{GL}(3,\mathbb R)\), defined by \(R^TR=I\), \(\det R=1\); the ambient group operations are smooth by matrix multiplication and the determinant inverse formula. A.1 supplies its embedded smooth structure. Differentiation shows its Lie algebra is contained in the skew matrices. Conversely, for skew \(T\), Local 2.3's exponential solves \(U'=TU\); differentiation gives \((U^TU)'=0\). Thus \(\exp(tT)\) is orthogonal, with determinant one by continuity from \(t=0\), proving the reverse inclusion. All skew matrices have the unique form \(J(v)\). Differentiating (H.3) at the identity gives \(\zeta(b)\mapsto2J(b)\), an isomorphism. Local 1.2 therefore gives a neighbourhood \(V\) of \(I\) on which \(\sigma\mapsto R_\sigma\) is a diffeomorphism onto an open neighbourhood. Shrink \(V\) to be disjoint from \(-V\). Every point over its image differs from its unique preimage in \(V\) by a kernel element, so the full preimage is the disjoint union \(V\cup(-V)\). Translation gives such neighbourhoods everywhere, proving the two-sheeted covering assertion.

Finally, coordinate expansion of the cross product gives
\(u\times(v\times w)=v(u\cdot w)-w(u\cdot v)\).
One way to check every component is the contraction identity
\(\sum_k\epsilon_{ijk}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}\); if a pair of indices repeats both sides reduce to the corresponding two Kronecker terms, and if the distinct pairs differ both sides vanish. Applying the triple-product identity twice gives the commutator in (H.5). An orientation-preserving orthogonal map preserves the cross product, since \(\langle u\times v,w\rangle=\det(u,v,w)\); this proves the conjugation identity in (H.5). □

**Theorem H.2 (all smooth rotational connections, including the origin).** Let \(\mathrm{SU}(2)\) act on \(\mathbb R^3\times\mathrm{SU}(2)\) by
\(\sigma\cdot(x,g)=(R_\sigma x,\sigma g)\).
Its invariant connections are exactly
\[
\begin{split}
\omega_{(x,g)}(v,\eta)&=\operatorname{Ad}(g^{-1})A_x(v)+g^{-1}\eta,\\
A_x(v)&=\zeta\bigl(f(s)v+g_0(s)(x\times v)+h(s)x\langle x,v\rangle\bigr),
\qquad s=|x|^2,
\end{split}
\tag{H.7}
\]
where \(f,g_0,h\) are arbitrary smooth real functions on \(\mathbb R\). Their restrictions to \([0,\infty)\) are uniquely determined by the connection; their values at negative arguments are immaterial. In particular, \(A_0(v)=f(0)\zeta(v)\).

In the alternative double-bracket notation the same potential is
\[
A_x(v)=(f+sh)\zeta(v)
 +\frac{g_0}{2}[\zeta(x),\zeta(v)]
 +\frac h4[\zeta(x),[\zeta(x),\zeta(v)]],
\tag{H.8}
\]
with all coefficient functions evaluated at \(s\).

**Proof.** By F.9 and the constant principal lift \(c(\sigma,x)=\sigma\), invariance is exactly
\[
A_{R_\sigma x}(R_\sigma v)=\operatorname{Ad}(\sigma)A_x(v).
\]
Use H.1 to write \(A_x(v)=\zeta(B(x)v)\). Then \(B\) is a smooth real \(3\)-by-\(3\) matrix-valued function and the condition becomes
\[
B(Rx)=RB(x)R^{-1}\qquad(R\in\mathrm{SO}(3)).
\tag{H.9}
\]
At \(x=re_3\), rotations about \(e_3\) fix the base point. Commutation with the half-turn about that axis makes both off-diagonal blocks between \(\mathbb R e_3\) and its orthogonal plane zero. Commutation with the quarter-turn \(\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\) makes the planar block \(\left(\begin{smallmatrix}a&-b\\b&a\end{smallmatrix}\right)\), by multiplying a general two-by-two matrix on the two sides. Hence
\[
B(re_3)=\begin{pmatrix}a(r)&-b(r)&0\\b(r)&a(r)&0\\0&0&c(r)\end{pmatrix}.
\tag{H.10}
\]
Its entries are smooth functions of all real \(r\). The half-turn about \(e_1\) sends \(re_3\) to \(-re_3\) and conjugates the planar rotation generator to its negative. Equation (H.9) therefore makes \(a,c\) even and \(b\) odd.

At zero, \(B(0)\) commutes with every rotation. Commutation with the half-turns about the three coordinate axes kills every off-diagonal entry; commutation with quarter-turns interchanging each pair of coordinate axes makes the three diagonal entries equal. Consequently \(a(0)=c(0)\) and \(b(0)=0\). The complete extension lemma G.2 now gives smooth functions on \(\mathbb R\) with
\[
a(r)=f(r^2),\qquad b(r)=r g_0(r^2),\qquad
c(r)-a(r)=r^2h(r^2).
\tag{H.11}
\]
The matrix expression \(f(|x|^2)I+g_0(|x|^2)J(x)+h(|x|^2)xx^T\) agrees with (H.10) on the entire axis. Both this expression and \(B\) satisfy (H.9). Every nonzero vector is a rotation of a point on the positive axis: complete its unit direction to an oriented orthonormal basis, whose column matrix is such a rotation. Thus the two expressions agree everywhere, including zero, proving necessity of (H.7).

Conversely the displayed expression in (H.7) is smooth in \(x\), linear in \(v\), and satisfies (H.9) because dot products and cross products are preserved by rotations. F.9 and Conn A.3 prove that it yields an invariant principal connection. Equations (H.10)–(H.11) determine the three functions for positive squared radius; continuity determines their values at zero. This gives the stated uniqueness. Finally \(x\times(x\times v)=x\langle x,v\rangle-sv\), and (H.2) converts each bracket to twice a cross product. Substitution proves (H.8), including its factors two and four. □

**Theorem H.3 (the rotational curvature).** For (H.7), write \(g_0=g_0(s)\), with primes denoting differentiation in \(s\). Set
\[
T=\langle x,v\rangle w-\langle x,w\rangle v,\quad
C=v\times w,\quad D=x\langle x,C\rangle.
\]
The curvature potential is
\[
\begin{split}
F_x(v,w)=\zeta\bigl(&[2f'-h-2g_0(f+sh)]T\\
&+[2g_0+2f^2+2s(g_0'+fh)]C\\
&+[2g_0^2-2g_0'-2fh]D\bigr).
\end{split}
\tag{H.12}
\]
The full principal curvature is its adjoint-equivariant horizontal extension as in Curvature A.4. At the origin, \(F_0(v,w)=2(g_0(0)+f(0)^2)\zeta(v\times w)\).

**Proof.** Let \(a_x(v)=\zeta^{-1}A_x(v)\) and introduce
\(U=\langle x,v\rangle(x\times w)-\langle x,w\rangle(x\times v)\).
The cross-product identity in H.1 gives \(U=sC-D\). For constant vector fields \(v,w\), differentiate the three terms of \(a\). The derivatives of \(s\) are \(2\langle x,v\rangle\); the two terms involving \(h'\) cancel. The remaining terms give
\[
(da)_x(v,w)=(2f'-h)T+2g_0'U+2g_0C.
\tag{H.13}
\]
For clarity, differentiating \(h(s)x\langle x,w\rangle\) and subtracting its version with \(v,w\) exchanged leaves \(-hT\); the terms containing \(x\langle v,w\rangle\) also cancel.

Expanding the cross product of the two values of \(a\) gives
\[
a_x(v)\times a_x(w)
=f^2C-g_0(f+sh)T+fhU+g_0^2D.
\tag{H.14}
\]
Here the terms with coefficients \(fg_0,fh,g_0h,g_0^2\) are respectively \(-fg_0T,fhU,-sg_0hT,g_0^2D\), and the \(h^2\)-term is zero. Each follows by the triple-product identity in H.1; in particular \((x\times v)\times(x\times w)=x\langle x,v\times w\rangle\). This last equality also follows directly by contracting the same two epsilon symbols used there.

Curvature A.4 gives \(F=dA+\frac12[A,A]\). By (H.2), its vector counterpart is \(da(v,w)+2a(v)\times a(w)\). Add (H.13) and twice (H.14), then replace \(U\) by \(sC-D\). The result is (H.12). At zero, \(T=D=0\) and \(s=0\), giving the claimed value. □

**Theorem H.4 (two lifts of Euclidean symmetry).** For \(S=\mathrm{SU}(2)\), put \(R_\sigma\) as in H.1; for \(S=\mathrm{SO}(3)\), put \(R_\sigma=\sigma\). The semidirect group \(\mathbb R^3\rtimes S\) has two principal lifts on \(\mathbb R^3\times S\):
\[
\begin{split}
(a,\sigma)\cdot(x,g)&=(a+R_\sigma x,\sigma g),\\
(a,\sigma)\cdot_0(x,g)&=(a+R_\sigma x,g).
\end{split}
\tag{H.15}
\]
For the first lift, every invariant potential is \(A_x(v)=c\zeta(v)\) in the \(\mathrm{SU}(2)\) case, or \(A_x(v)=cJ(v)\) in the \(\mathrm{SO}(3)\) case, with arbitrary real constant \(c\). Its curvature is respectively \(2c^2\zeta(v\times w)\) or \(c^2J(v\times w)\). For the second lift the only invariant potential is zero. In both cases the full connection is given by Conn A.3.

**Proof.** The multiplication is \((a,\sigma)(b,\tau)=(a+R_\sigma b,\sigma\tau)\), and its inverse is \((-R_{\sigma^{-1}}a,\sigma^{-1})\). The homomorphism property of \(R\) verifies associativity and the action laws in (H.15); all operations are smooth. Both actions commute with principal right multiplication.

For either lift, translations force the potential to be constant in \(x\), by F.4 with the whole space as the translation subspace. Write it as a linear map \(W:\mathbb R^3\to\mathfrak s\). For the first lift, F.9 requires \(W(R_\sigma v)=\operatorname{Ad}(\sigma)W(v)\). In the \(\mathrm{SU}(2)\) case, write \(W=\zeta\circ T\), and in the \(\mathrm{SO}(3)\) case write \(W=J\circ T\). By (H.3) or (H.5), the condition is that \(T\) commute with all rotations. H.2's half-turn and quarter-turn calculation proves \(T=cI\). Conversely every such map obeys the condition and hence defines an invariant connection. Its exterior derivative is zero, so Curvature A.4 and the brackets (H.2), (H.5) give the stated curvatures.

For the second lift, F.9 instead requires \(W(Rv)=W(v)\) for every rotation \(R\). For each nonzero \(v\), a half-turn about any perpendicular unit axis sends \(v\) to \(-v\); such a rotation is present in either group by H.1. Linearity then gives \(W(v)=-W(v)\), hence \(W=0\). The zero potential is invariant, completing the classification. □

**Example H.5 (continuous extension is weaker than smooth extension).** On the punctured \(\mathbb R^3\times\mathrm{SU}(2)\), the rotational potential \(A_x(v)=\zeta(v)/|x|\) has no continuous extension across zero. Replacing \(1/|x|\) by \(|x|\) gives a continuous extension but no smooth one.

**Proof.** Both satisfy rotational covariance by (H.3), so Conn A.3 gives invariant punctured connections. Restrict to \(x=te_3\) and evaluate on the fixed vector \(e_1\). In the first case the \(\tau_1\)-coefficient is \(1/|t|\), which has no finite limit. A continuous full connection would pull back to a continuous potential in the identity section, so it cannot exist. In the second case the potential tends to the zero linear map as \(x\to0\); the estimate \(\|A_x(v)\|\le C|x|\,|v|\), for a fixed norm constant of \(\zeta\), proves continuity of that extension. On the same line its coefficient is \(|t|\), whose left and right derivatives at zero differ. Any continuous extension is forced to have the value zero there; thus no differentiable, and in particular no smooth, extension exists. □

**Example H.6 (a nonzero flat rotational connection).** For \(c\in\mathbb R\), put \(u_c(x)=\exp(c\zeta(x))\). The potential \(A=u_c^{-1}du_c\) is smooth, rotationally invariant in the sense of H.2, and flat. In (H.7), its coefficients for \(s>0\), with \(r=\sqrt{s}\), are
\[
f(s)=\frac{\sin(2cr)}{2r},\qquad
g_0(s)=-\left(\frac{\sin(cr)}r\right)^2,\qquad
h(s)=\frac{c-f(s)}s.
\tag{H.16}
\]
They extend smoothly as functions of squared radius, with
\[
f(0)=c,\qquad g_0(0)=-c^2,\qquad h(0)=\frac23c^3.
\tag{H.17}
\]
For \(c\ne0\) the connection has a nonzero potential, even though its curvature vanishes.

**Proof.** Smoothness of the group exponential is proved in Local 2.3, so \(u_c\), its inverse, and its Maurer pullback are smooth on the whole space. For \(r>0\), (H.2) gives \(\zeta(x)^2=-r^2I\). The matrix curve
\(\cos(tr)I+\sin(tr)\zeta(x)/r\)
solves \(U'=\zeta(x)U\), \(U(0)=I\), by direct differentiation. Uniqueness in Local 2.1 identifies it with \(\exp(t\zeta(x))\). Thus \(u_c=aI+\zeta(b)\), where \(a=\cos(cr)\), \(b=q x\), and \(q=\sin(cr)/r\).

Differentiate (H.6). Since \(a^2+|b|^2=1\), the scalar part of \(u_c^{-1}du_c\) is zero, and its vector part is
\[
a\,db-b\,da-b\times db.
\tag{H.18}
\]
For a tangent \(v\), insert \(db(v)=qv+2q'(s)x\langle x,v\rangle\) and \(da(v)=2a'(s)\langle x,v\rangle\). The three coefficients in (H.7) are
\(f=aq\), \(g_0=-q^2\), \(h=2(aq'-a'q)\).
Using \(dr/ds=1/(2r)\) and differentiating sine and cosine reduces these to (H.16). In particular the last coefficient is \(c/r^2-\sin(2cr)/(2r^3)\), equal to the stated \((c-f)/s\).

To justify the values and smoothness at zero without relying on the quotients there, use
\(\sin(cr)/r=c\int_0^1\cos(ctr)\,dt\).
The right side is a smooth even function of all real \(r\), by the differentiation-under-the-integral argument in G.2. So are \(aq\), \(-q^2\), and \(c-aq\); the last vanishes at zero. G.2 provides the smooth squared-radius extensions of all three coefficients, using its quadratic division for \(h\). The first two values in (H.17) follow directly. For the last, write \(f(r^2)=c\int_0^1\cos(2ctr)\,dt\); its second derivative in \(r\) at zero is \(-4c^3/3\). Twice applying the fundamental theorem as in (G.4) gives \(h(0)=-\tfrac12(-4c^3/3)=2c^3/3\).

The resulting formula has exactly the form (H.7), proving rotational invariance. The Maurer equation is completely proved in Curvature A.3. Pullback commutes with exterior differentiation and the valued bracket by Curvature A.1–A.2; hence \(dA+\frac12[A,A]=0\), proving flatness everywhere, including zero. Finally \(A_0(v)=c\zeta(v)\), which is nonzero for \(c\ne0\) and suitable \(v\). This also checks the origin term in (H.12): \(g_0(0)+f(0)^2=0\). □
