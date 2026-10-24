# Free modules preserve n-quasi-isomorphisms on every topos

*Written by Claude Opus 5.5 (Anthropic) on 23 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it and refereed and revised by Claude Opus 5.5 in two further sessions. Public domain (CC0).*

Let \(f\) be an \(n\)-quasi-isomorphism of simplicial sheaves on an arbitrary topos, with no hypothesis on points. This lesson proves that, for every sheaf of rings \(R\) and every fixed \(n\geq1\), the map \(R^{(f)}\) of free simplicial \(R\)-modules is again an \(n\)-quasi-isomorphism. This is Illusie's conjecture in its finite-\(n\) form, for free modules over any sheaf of rings. It contains the case \(R=\mathbb Z\) and, letting \(n\) vary, the case of quasi-isomorphisms. The proof uses neither points nor Boolean localization. It combines four ingredients:

- the Kan replacement and a path-space factorization, both performed on sections;
- local lifting against boundaries of simplices of dimension \(\leq n\), with one covering sieve for each finite lifting problem;
- the finite support of chains.

**Prerequisites.** [*Homotopy sheaves and the free abelian Whitehead theorem*](homotopy-sheaves-and-the-free-abelian-whitehead-theorem.md) (Conventions, (1.1), Definition 1.1, Lemmas 1.2 and 1.3, Proposition 1.4, Definition 2.1, Lemmas 3.2, 3.3 and 3.4 with their proofs, Exercise 8.1). From the programme lesson [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes): Section 5.2, anodyne extensions, in particular, for an inclusion \(A\subseteq L\) of finite simplicial sets and \(\epsilon\in\{0,1\}\), the anodyne inclusions
\[
\begin{aligned}&(L\times\{\epsilon\})\cup(A\times\Delta[1])\\&\qquad\subseteq L\times\Delta[1],\\
&(\Lambda^k[m]\times\Delta[1])\\&\qquad\cup(\Delta[m]\times\partial\Delta[1])\\&\qquad\subseteq\Delta[m]\times\Delta[1],\end{aligned}
\tag{0.1}
\]
against which Kan fibrations lift; Section 5.3, the relation (5.12), Theorem 5.3f and the change of base point in its proof, and the exact sequence (5.17). From the programme lesson [*Sites and sheaves*](course:ag-etale-cohomology/sites-and-sheaves): Theorems 3.1–3.3 and 4.1.

## Conventions

The Conventions of the lesson on homotopy sheaves are used. \(\mathcal C\) is a small site, \(T=\operatorname{Sh}(\mathcal C)\), \(a\) is sheafification and \(\iota\colon T\to\widehat{\mathcal C}\) is the inclusion into presheaves. \(R\) is a sheaf of associative unital rings, and modules are left modules.

For a ring \(S\) and a simplicial set \(K\), let \(C_S(K)=N(S[K])\) be the quotient of \(S[K]\) by the submodule spanned by the degenerate simplices. The sequence \(0\to D_q\to\mathbb Z[K_q]\to N_q\mathbb Z[K]\to0\) is split, its quotient being free on the nondegenerate simplices. Applying \(S\otimes_{\mathbb Z}-\) therefore gives
\[
C_S(K)=S\otimes_{\mathbb Z}N\mathbb Z[K],
\tag{0.2}
\]
naturally in \(K\) and in \(S\). Each term is free on the nondegenerate simplices.

For a simplicial subset \(L\subseteq K\), the map \(C_S(L)\to C_S(K)\) is injective and split in each degree. Indeed, if \(x\in L\) and \(x=s_iy\) in \(K\), then \(y=d_ix\in L\), so \(x\) is already degenerate in \(L\).

In a Kan complex with a vertex \(b\), the relation (5.12) is used in the following form. Let \(\sigma\in K_r\), \(r\geq1\), have all its faces equal to the constant \((r-1)\)-simplex at \(b\), and write \(b\) also for the constant simplices at \(b\). Then \([\sigma]=1\) in \(\pi_r\) exactly when there is \(\omega\in K_{r+1}\) with \(d_i\omega=b\) for \(i<r+1\) and \(d_{r+1}\omega=\sigma\). This is (5.12) for the pair \((b,\sigma)\); the relation being symmetric, it can be applied in this order.

## 1. Homology sheaves of presheaves

For a simplicial presheaf \(P\), let \(F_R(P)\) be the simplicial presheaf of \(R\)-modules with \(F_R(P)_q(U)=R(U)[P_q(U)]\) and the restrictions \(r[\sigma]\mapsto r|_V[\sigma|_V]\). Put
\[
\mathcal H^R_q(P)=a\bigl(U\mapsto H_qC_{R(U)}(P(U))\bigr).
\]

**Lemma 1.1.** There is an isomorphism of simplicial \(R\)-modules \(\theta_P\colon aF_R(P)\to R^{(aP)}\), natural in \(P\). It induces isomorphisms \(\chi_{P,q}\colon\mathcal H^R_q(P)\to H_q(NR^{(aP)})\) in \(\operatorname{Mod}_R(T)\), natural in \(P\).

**Proof.** Let \(M\) be an \(R\)-module of \(T\). By the universal property of sheafification, the maps of modules \(aF_R(P)_q\to M\) are the maps of presheaves of modules \(F_R(P)_q\to\iota M\). These are the maps of presheaves \(P_q\to\iota M\), hence the maps of sheaves \(aP_q\to M\), hence the \(R\)-linear maps \(R^{(aP_q)}\to M\).

So \(\theta_P\) sends the image of a generator \([\sigma]\) to the generator \([a\sigma]\). Its inverse is the \(R\)-linear extension of the map \(aP_q\to aF_R(P)_q\). Both are compatible with faces, degeneracies and maps \(P\to Q\).

Sheafification is exact, and \(N\) and \(H_q\) are built from kernels and cokernels. Hence \(H_q(NaF_R(P))\) is the sheaf associated with \(U\mapsto H_qC_{R(U)}(P(U))\). Composing with \(H_q(N\theta_P)\) gives \(\chi_{P,q}\). \(\square\)

For a simplicial presheaf \(P\), put \((KP)(U)=P(U)^{\mathrm{Kan}}\). This is a simplicial presheaf, functorial in \(P\), because \(A\mapsto A^{\mathrm{Kan}}\) is a functor. Let \(\eta_P\colon P\to KP\) be the inclusion.

**Lemma 1.2.** \(\mathcal H^R_q(\eta_P)\) is an isomorphism for every \(q\).

**Proof.** Let \(A\) be a simplicial set and \(S\) a ring. By the proof of Lemma 3.2 of the lesson on homotopy sheaves, each map \(N\mathbb Z[A^{(r)}]\to N\mathbb Z[A^{(r+1)}]\) is injective and split in each degree. Its quotient is a direct sum of complexes \(\mathbb Z\xrightarrow{(-1)^k}\mathbb Z\), which is contractible.

Apply \(S\otimes_{\mathbb Z}-\) and (0.2). The sequences stay exact, the quotients stay contractible, and each stage induces isomorphisms on the homology of \(C_S\). The functors \(S[-]\) and \(N\) commute with increasing unions, and so does homology. Hence \(C_S(A)\to C_S(A^{\mathrm{Kan}})\) is a quasi-isomorphism.

Take \(A=P(U)\) and \(S=R(U)\), and sheafify. \(\square\)

## 2. Transfer of the hypothesis to a fibration of presheaves

**2.0. Setting.** Let \(n\geq1\) and let \(f\colon X\to Y\) be an \(n\)-quasi-isomorphism of simplicial sheaves. Put \(A=K(\iota X)\), \(B=K(\iota Y)\) and \(g=K(\iota f)\colon A\to B\). Let \(B^{\Delta[1]}\) be the simplicial presheaf with
\[
(B^{\Delta[1]})_q(U)=\operatorname{Hom}(\Delta[q]\times\Delta[1],B(U)),
\]
with the endpoint maps \(\mathrm{ev}_0\) and \(\mathrm{ev}_1\). Put
\[
\begin{aligned}E&=A\times_{g,B,\mathrm{ev}_0}B^{\Delta[1]},\\ p&=\mathrm{ev}_1\circ\mathrm{pr}_2\colon E\to B.\end{aligned}
\]
Let \(j\colon A\to E\) be \(j(x)=(x,\text{the constant path at }g(x))\), and let \(r=\mathrm{pr}_1\). Then \(rj=1_A\) and \(pj=g\).

Let \(H\colon E\times\Delta[1]\to E\) be \(((x,\gamma),t)\mapsto(x,\gamma\circ(1\times\min(-,t)))\), with \(\min\) induced by the monotone map \(\min\colon[1]\times[1]\to[1]\). Since \(\min(0,t)=0\), the path still starts at \(g(x)\), so \(H\) lands in \(E\). It is a homotopy from \(jr\) to \(1_E\).

A map \(u\colon P\to Q\) of simplicial presheaves with Kan sections *satisfies \((\mathrm H_n)\)* if two conditions hold:

- \(a\pi_0(u)\) is an isomorphism;
- for every \(U\) and every \(e\in P_0(U)\), the map of sheaves on \(\mathcal C_{/U}\) associated with \(V\mapsto(\pi_i(P(V),e|_V)\to\) \(\pi_i(Q(V),u(e)|_V))\) is an isomorphism for \(1\leq i<n\) and an epimorphism for \(i=n\).

**Lemma 2.1.** In 2.0, every \(p(U)\) is a Kan fibration, every \(E(U)\) is Kan, and \(p\) satisfies \((\mathrm H_n)\).

**Proof.** *The fibration.* Maps \(\Lambda^k[m]\to B(U)^{\Delta[1]}\) correspond to maps \(\Lambda^k[m]\times\Delta[1]\to B(U)\), and maps \(\Delta[m]\to B(U)\times B(U)\) to maps \(\Delta[m]\times\partial\Delta[1]\to B(U)\). So a lifting problem for \((\mathrm{ev}_0,\mathrm{ev}_1)\) against \(\Lambda^k[m]\subseteq\Delta[m]\) is an extension problem along the second inclusion of (0.1). It is solvable because \(B(U)\) is Kan.

The map \((r,p)\colon E(U)\to A(U)\times B(U)\) is the pullback of \((\mathrm{ev}_0,\mathrm{ev}_1)\) along \(g\times1\), hence a Kan fibration. So is the projection \(A(U)\times B(U)\to B(U)\), \(A(U)\) being Kan. Hence \(p(U)\) is a Kan fibration, and \(E(U)\) is Kan because \(B(U)\) is.

*The condition for \(g\).* By Proposition 1.4 of the lesson on homotopy sheaves, applied on \(\mathcal C_{/U}\), and by Definition 1.1 there, \(\pi_i(X|U,x)\) is the sheaf associated with \(V\mapsto\pi_i(A(V),x|_V)\). The same holds for \(Y\) and \(B\). So the second condition of \((\mathrm H_n)\) holds for \(g\) at the vertices of \(\iota X\).

Sheafification preserves the coequalizer defining \(\pi_0\), so \(a\pi_0(\iota X)=\pi_0(X)\). By Lemma 1.2 (3) there, \(\pi_0(\iota X)\to\pi_0(A)\) is bijective on sections. Hence \(a\pi_0(g)\) is identified with \(\pi_0(f)\), an isomorphism by Exercise 8.1 there.

By the proof of Lemma 1.2 (3) there, every vertex \(y\) of \(A(U)\) is joined to a vertex \(x\) of \(X(U)\) by a finite path of edges of \(A(U)\). Change of base point along this path and along its image in \(B(U)\) gives isomorphisms \(\pi_i(A(V),y|_V)\cong\pi_i(A(V),x|_V)\). They are natural in \(V\) and commute with \(g\). So the condition holds at \(y\).

*Transfer to \(p\).* Sectionwise, \(j\) is a homotopy equivalence with inverse \(r\). By Theorem 5.3f of the programme lesson it induces bijections on \(\pi_0\) and isomorphisms on \(\pi_i\) at the vertices \(j(x)\), naturally in \(V\). As \(pj=g\), the second condition holds for \(p\) at \(j(x)\), and \(a\pi_0(p)=a\pi_0(g)\circ a\pi_0(j)^{-1}\) is an isomorphism.

A vertex \(e=(x,\gamma)\) of \(E(U)\) is joined to \(j(x)\) by the edge \(H(e,-)\). The image of this edge under \(p\) is \(u\mapsto\gamma(\min(1,u))=\gamma\). Change of base point along these two edges, natural in \(V\) and compatible with \(p\), gives the condition at \(e\). \(\square\)

## 3. Local lifting

A square of simplicial sets \(K_0\to E(U)\), \(L_0\to B(U)\) over \(p\), with \(K_0\subseteq L_0\), *lifts locally* if the arrows \(v\colon V\to U\) for which the restricted square has a lift \(L_0\to E(V)\) form a covering sieve. No compatibility between the lifts for different arrows \(v\) is required.

**Lemma 3.1.** Let \(p\) be as in Lemma 2.1 and \(b\in B_0(U)\). Let \(F\) be the presheaf on \(\mathcal C_{/U}\) with \(F(V)=E(V)\times_{B(V)}\{b|_V\}\). Then:

1. every \(F(V)\) is Kan;
2. locally on \(U\), \(F\) has a vertex;
3. any two vertices of \(F(V)\) are locally joined by an edge of \(F\);
4. for every vertex \(e\) of \(F(V)\) and \(1\leq r<n\), the sheaf on \(\mathcal C_{/V}\) associated with \(\pi_r(F,e)\) vanishes.

**Proof.** (1) holds by pullback.

(2) Locally, the class of \(b\) in \(a\pi_0(B)\) is the image of the class of a vertex \(e'\) of \(E\). After a further covering, \(p(e')\) and \(b\) lie in one component of \(B(V)\) (Theorem 3.1 of *Sites and sheaves*), so they are joined by an edge, \(B(V)\) being Kan. Lifting this edge against \(\Delta[0]\subseteq\Delta[1]\), starting at \(e'\), gives a vertex over \(b\).

(3) Let \(e,e'\in F_0(V)\). Since \(a\pi_0(p)\) is injective, they are locally joined by an edge \(w\colon e\to e'\) of \(E\). The edge \(p(w)\) is a loop at \(b\). The map \(a\pi_1(E,e)\to a\pi_1(B,b)\) is an epimorphism, for \(n=1\) as for \(n>1\). So, after a further covering, there is a loop \(\gamma\) at \(e\) with \([p\gamma]=[pw]\).

Fill the horn \(\Lambda^0[2]\) in \(E\) with the faces \(d_2=\gamma\) and \(d_1=w\). The face \(d_0\) is an edge \(u\colon e\to e'\), and \([pw]=[p\gamma][pu]\). Hence \([pu]=1\), and the Conventions give \(\tau\in B_2\) with \(d_0\tau=d_2\tau=s_0b\) and \(d_1\tau=pu\).

Lift \(\tau\) against \(\Lambda^0[2]\subseteq\Delta[2]\), with the faces \(d_1=u\) and \(d_2=s_0e\). These lie over \(d_1\tau\) and \(d_2\tau\). The face \(d_0\) of the lift is an edge from \(e\) to \(e'\) over \(s_0b\), that is, an edge of \(F\).

(4) The sequences (5.17) of the fibrations \(p(V')\), for arrows \(V'\to V\), are natural in \(V'\). Let \(\alpha\) be a local section of \(a\pi_r(F,e)\), represented by a class in \(\pi_r(F(V'),e)\). Its image in \(\pi_r(E(V'),e)\) maps to \(1\) in \(\pi_r(B(V'),b)\). Since \(r<n\), the sheaf map \(a\pi_r(E,e)\to a\pi_r(B,b)\) is injective, so that image is locally \(1\). By exactness, \(\alpha\) is locally \(\delta(\beta)\) with \(\beta\in\pi_{r+1}(B,b)\). Since \(r+1\leq n\), \(\beta\) is locally \(p_*\gamma\), and \(\delta p_*\gamma=1\). So \(\alpha\) is locally trivial. \(\square\)

**Lemma 3.2.** With \(F\) as in Lemma 3.1 and \(1\leq m\leq n\), every map \(\alpha\colon\partial\Delta[m]\to F(V)\) extends locally to \(\Delta[m]\).

**Proof.** For \(m=1\) this is Lemma 3.1 (3). Let \(m\geq2\), and put \(L=\Lambda^m[m]\) and \(v=\alpha(m)\). The monotone map \((i,0)\mapsto i\), \((i,1)\mapsto m\) defines \(\Delta[m]\times\Delta[1]\to\Delta[m]\). It carries \(\sigma\times\Delta[1]\) into \(L\) for every face \(\sigma\) missing a vertex \(i\neq m\), since the image still misses \(i\). Composing with \(\alpha|_L\) gives a homotopy from \(\alpha|_L\) to the constant map at \(v\).

By (0.1) with \(A=L\) and \(\epsilon=0\), this homotopy and \(\alpha\) extend to a homotopy \(J\colon\partial\Delta[m]\times\Delta[1]\to F(V)\) from \(\alpha\) to some \(\beta\) that is constant at \(v\) on \(L\). The faces of \(\sigma=d_m\beta\) lie in \(L\), so \(\sigma\) is an \((m-1)\)-cycle at \(v\).

By Lemma 3.1 (4) with \(r=m-1\), its class is locally \(1\). The Conventions then give, locally, \(\omega\in F_m\) with \(d_i\omega=v\) for \(i<m\) and \(d_m\omega=\sigma\). Thus \(\partial\omega=\beta\).

By (0.1) with \(A=\partial\Delta[m]\) and \(\epsilon=1\), the map given by \(J\) and by \(\omega\) on \(\Delta[m]\times\{1\}\) extends to \(\Delta[m]\times\Delta[1]\). Its end at \(0\) extends \(\alpha\). \(\square\)

**Proposition 3.3.** Let \(p\) be as in Lemma 2.1, and let \(K_0\subseteq L_0\) be finite simplicial sets such that every nondegenerate simplex of \(L_0\) not in \(K_0\) has dimension \(\leq n\). Then every square \(K_0\to E(U)\), \(L_0\to B(U)\) over \(p\) lifts locally.

**Proof.** *A single simplex.* Let \(K_0=\partial\Delta[m]\) and \(L_0=\Delta[m]\) with \(m\leq n\), and let the square be given by \(\alpha\) and \(\beta\). For \(m=0\) the claim is Lemma 3.1 (2). Let \(m\geq1\).

The monotone map \((i,0)\mapsto0\), \((i,1)\mapsto i\) defines \(c\colon\Delta[m]\times\Delta[1]\to\Delta[m]\), with \(c_0\) constant at \(0\) and \(c_1=1\). By (0.1) with \(A=\varnothing\) and \(\epsilon=1\), the restriction of \(\beta c\) to \(\partial\Delta[m]\times\Delta[1]\) lifts to a map \(\tilde\alpha\) ending at \(\alpha\). Its start \(\alpha_0\) lies in the fibre over \(\beta(0)\).

By Lemma 3.2, \(\alpha_0\) extends locally to \(u\colon\Delta[m]\to F\). By (0.1) with \(A=\partial\Delta[m]\) and \(\epsilon=0\), the map given by \(u\) and \(\tilde\alpha\) lifts \(\beta c\) on the whole cylinder. Its end at \(1\) extends \(\alpha\) and lies over \(\beta\).

*The general case.* As in the proof of Lemma 3.4 of the lesson on homotopy sheaves, \(L_0\) is built from \(K_0\) by attaching the missing nondegenerate simplices, in increasing dimension, along their boundaries. Let \(\sigma\) be a nondegenerate \(m\)-simplex whose boundary lies in the subset \(K'\) already built.

Every simplex is uniquely a degeneracy of a nondegenerate one. So the simplices of \(K'\cup\langle\sigma\rangle\) outside \(K'\) are the distinct degeneracies \(\phi^*\sigma\) of \(\sigma\), with \(\phi\) surjective. Hence a lift on \(K'\) and a lift \(\Delta[m]\to E\) agreeing with it on \(\partial\Delta[m]\) define a lift on \(K'\cup\langle\sigma\rangle\).

*Locality.* Let \(\mathcal S_k\) be the sieve of arrows over which a lift exists on the \(k\)-th stage. For \(v\in\mathcal S_k\), choose one lift over \(v\). The arrows into \(V\) over which it extends form a covering sieve, by the single-simplex case, and they lie in \(v^*\mathcal S_{k+1}\). By the transitivity axiom, \(\mathcal S_{k+1}\) covers \(U\). Finitely many stages reach \(L_0\). \(\square\)

## 4. The theorem

**Proposition 4.1.** Let \(p\) be as in Lemma 2.1. Then \(\mathcal H^R_q(p)\) is an epimorphism for \(q\leq n\) and a monomorphism for \(q<n\).

**Proof.** *Epimorphism.* A section of \(\mathcal H^R_q(B)\) is locally the class of a cycle \(z\in C_{R(U)}(B(U))_q\). Let \(L_0\subseteq B(U)\) be the finite simplicial subset generated by its simplices. Its dimension is \(\leq q\leq n\), and \(z\) is a cycle of \(C_{R(U)}(L_0)\).

Proposition 3.3, applied to \(\varnothing\subseteq L_0\), gives locally maps \(s\colon L_0\to E(V)\) with \(p(V)s\) equal to \(L_0\to B(V)\). With \(z_V\) the image of \(z\) in \(C_{R(V)}(L_0)\), the chain \(s_*z_V\) is a cycle with \(p_*s_*z_V=z|_V\).

*Monomorphism.* Let \(q<n\), and let a local section of \(\mathcal H^R_q(E)\) with image \(0\) be the class of a cycle \(z\in C_{R(U)}(E(U))_q\). By Theorem 3.1 of *Sites and sheaves*, after a covering (still written \(U\)) there is \(w\in C_{R(U)}(B(U))_{q+1}\) with \(p_*z=dw\).

Let \(K_0\subseteq E(U)\) be generated by the simplices of \(z\), and \(L_0\subseteq B(U)\) by \(p(K_0)\) and the simplices of \(w\). They are finite, with \(\dim K_0\leq q\) and \(\dim L_0\leq q+1\leq n\). The equality \(p_*z=dw\) holds in \(C_{R(U)}(L_0)\), the map to \(C_{R(U)}(B(U))\) being injective.

Proposition 3.3 gives locally \(s\colon L_0\to E(V)\) over \(B(V)\). Apply it again to \(K_0\times\partial\Delta[1]\subseteq K_0\times\Delta[1]\), whose nondegenerate simplices have dimension \(\leq q+1\). The top map is the inclusion at \(0\) and \(s\circ p|_{K_0}\) at \(1\), and the bottom map is \((x,t)\mapsto p(x)\). The square commutes since \(ps\) is the inclusion of \(L_0\). This gives locally a homotopy from the inclusion to \(sp|_{K_0}\).

Lemma 3.3 of the lesson on homotopy sheaves, tensored with the coefficient ring by (0.2), gives \(P\) with \(dP+Pd=(sp)_*-1\). Since \(dz=0\),
\[
\begin{aligned}z&=s_*p_*z-dP(z)\\&=d\bigl(s_*w-P(z)\bigr),\end{aligned}
\]
with all chains taken in the restricted coefficients. So the class is locally zero.

After restriction, the maps of \(K_0\) and \(L_0\) into \(E(V)\) and \(B(V)\) may identify simplices. This is harmless: \(K_0\) and \(L_0\) are fixed sources, and identities of chains persist under change of coefficients. \(\square\)

**Theorem 4.2.** Let \(T=\operatorname{Sh}(\mathcal C)\) be any topos, \(R\) a sheaf of associative unital rings, \(n\geq1\), and \(f\colon X\to Y\) an \(n\)-quasi-isomorphism of simplicial sheaves. Then
\[
H_q(NR^{(X)})\to H_q(NR^{(Y)})
\]
is an isomorphism for \(q<n\) and an epimorphism for \(q=n\). Equivalently, \(R^{(f)}\) is an \(n\)-quasi-isomorphism of simplicial abelian sheaves.

**Proof.** *The fibration \(p\).* In 2.0, Proposition 4.1 applies to \(p\), by Lemma 2.1.

*The map \(j\).* By Lemma 3.3 of the lesson on homotopy sheaves and (0.2), the homotopy \(H\) makes \(C_{R(U)}(jr)\) chain homotopic to \(1\). Together with \(rj=1\), this makes \(H_qC_{R(U)}(j)\) bijective for every \(U\), so \(\mathcal H^R_q(j)\) is an isomorphism. Hence \(\mathcal H^R_q(g)=\mathcal H^R_q(p)\,\mathcal H^R_q(j)\) is an isomorphism for \(q<n\) and an epimorphism for \(q=n\).

*The original map.* Since \(\eta_Y\circ\iota f=g\circ\eta_X\) and \(\mathcal H^R_q(\eta)\) is invertible (Lemma 1.2), \(\mathcal H^R_q(\iota f)\) has the same property. Lemma 1.1, with \(a\iota=1\), carries \(\mathcal H^R_q(\iota f)\) to \(H_q(NR^{(f)})\).

*The equivalence.* It is (1.1) of the lesson on homotopy sheaves, natural in maps of simplicial abelian sheaves, together with Definition 2.1 there. \(\square\)

**Corollary 4.3.**

1. If \(f\) is a quasi-isomorphism, so is \(R^{(f)}\).
2. If \(\pi_0(f)\) is an epimorphism, so is \(H_0(NR^{(f)})\).

**Proof.** (1) Apply Theorem 4.2 with \(n=q+1\) for each \(q\).

(2) For a simplicial set \(K\), \(H_0C_S(K)=\) \(S[K_0]/\operatorname{im}(d_0-d_1)=\) \(S[\pi_0K]\), naturally in \(K\). By Lemma 1.1 in degree \(0\), applied to the presheaf of sets \(\pi_0(\iota X)\), whose sheafification is \(\pi_0(X)\), this gives \(H_0(NR^{(X)})\cong R^{(\pi_0X)}\), naturally in \(X\). The functor \(R^{(-)}\) is left adjoint to the forgetful functor, so it preserves epimorphisms. \(\square\)

The proof uses no points of \(T\) and no Boolean localization. Each covering sieve comes from one finite lifting problem or one equality of sections, and finitely many are composed by the transitivity axiom. Theorems 4.1 and 7.1 of the lesson on homotopy sheaves, and the statement on quasi-isomorphisms recalled in its Remark 7.3, are thus special cases of Theorem 4.2 and Corollary 4.3. The case \(n=0\) is Corollary 4.3 (2).

## 5. Exercises

**Exercise 5.1.** Show that a degreewise split injection of complexes of abelian groups with contractible cokernel stays a quasi-isomorphism after applying \(S\otimes_{\mathbb Z}-\), for any ring \(S\). Explain why Lemma 1.2 needs no flatness of \(S\).

**Exercise 5.2.** Let \(\mathcal C\) be the one-point site, so that \(T\) is the topos of sets. Show that Theorem 4.2 gives Theorem 3.1 of the lesson on homotopy sheaves for \(n\geq1\), with coefficients in any ring \(S\).

## 6. Complete solutions

**5.1.** A degreewise split short exact sequence stays exact under the additive functor \(S\otimes-\). A contraction \(h\) of the cokernel, with \(dh+hd=1\), gives the contraction \(1\otimes h\). The long exact homology sequence then shows that the injection is a quasi-isomorphism. In Lemma 1.2 the injections are split because the cokernels are free on simplices, so no flatness of \(S\) is used.

**5.2.** Every covering sieve on the point is maximal, so "locally" means "globally" and sheafification is the identity. Theorem 4.2 states that \(H_qC_S(f)\) is bijective for \(q<n\) and surjective for \(q=n\); for \(S=\mathbb Z\) this is Theorem 3.1 there. The proof here differs from the one given there in the factorization: it uses the path space \(E\) of 2.0 instead of the factorization (5.19).

## Sources

The notions of homotopy sheaves and of \(n\)-quasi-isomorphisms, and the conjecture proved here, are due to Illusie, in his work on the cotangent complex. For quasi-isomorphisms, a proof by Boolean localization and the history of the statement are given in J. F. Jardine, *Local homotopy theory*, lecture notes, lecture 6a, Lemma 13.1 and Remark 13.2 ([math.uwo.ca](https://www.math.uwo.ca/faculty/jardine/courses/localhom/localhom-lecture06a.pdf)). Local lifting arguments of the kind used in Section 3 appear in D. Dugger and D. C. Isaksen, *Weak equivalences of simplicial presheaves*, [arXiv:math/0205025](https://arxiv.org/abs/math/0205025). The main argument follows a solution produced with ChatGPT (OpenAI) in October 2026 and completed here.
