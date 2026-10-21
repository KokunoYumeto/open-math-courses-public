# Simplicial rings and modules in a topos

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A simplicial ring of a topos is a ring object of the topos of simplicial objects: a family of rings \(A_n\) with faces and degeneracies that are ring homomorphisms. Modules over it, up to homotopy and quasi-isomorphism, form the derived category \(D_\bullet(A)\) in which the cotangent complex and its relatives live. When \(A\) is a ring \(\Lambda\) placed in every degree, normalization identifies simplicial \(\Lambda\)-modules with chain complexes, and \(D_\bullet(\Lambda)\) is the part of the usual derived category in nonpositive degrees. For a general simplicial ring there is no such identification, and the homotopy theory has to be built directly.

This lesson builds it. It defines homotopies of modules over a simplicial ring and shows that homotopy classes form an additive category. It makes the normalized complex of \(A\) a graded commutative differential graded ring. It constructs mapping cylinders, path objects, cones, suspensions and loops, and proves the lifting properties of fibrant quasi-isomorphisms. With these it proves Illusie's theorem: quasi-isomorphisms of modules admit a calculus of fractions on both sides, and quasi-isomorphisms of algebras admit one on the right. Triangles and Ext groups in \(D_\bullet(A)\) are treated in [*Triangles and Ext groups of simplicial modules*](triangles-and-ext-groups-of-simplicial-modules.md).

**Prerequisites.** [*Homotopy sheaves and the free abelian Whitehead theorem*](homotopy-sheaves-and-the-free-abelian-whitehead-theorem.md), Section 1; [*Décalage, nerves and the homotopy type of a category*](decalage-nerves-and-the-homotopy-type-of-a-category.md), Proposition 2.1 and Corollary 2.2; Lemma 1.1 of [*Stable derived functors*](stable-derived-functors.md); Theorems 1.1–1.3 and Proposition 1.4 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex#1-simplicial-algebra-and-the-standard-resolution) (normalization, Dold–Kan, Eilenberg–Zilber with the passage from chain homotopies to simplicial homotopies, homotopy groups of simplicial groups). From the AI-integrated Stacks project: Dold–Kan in abelian categories [[Stacks, Tag 019G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-theorem-dold-kan)]; homotopies of simplicial objects and of normalized complexes [[Tag 019L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-relations-homotopy), [Tag 019S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-homotopy-s-N)]; internal Hom and tensor products of modules on a ringed site [[Tag 04TT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-section-internal-hom)]; multiplicative systems and calculus of fractions [[Tag 04VC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-definition-multiplicative-system)].

## Conventions

\(T\) is a topos. Rings are commutative and unital. \(\operatorname{Simpl}(T)\), the category of simplicial objects of \(T\), is again a topos. A *simplicial ring* \(A\) is a ring of \(\operatorname{Simpl}(T)\), and an *\(A\)-module* is a module over it in \(\operatorname{Simpl}(T)\): a simplicial object \(E\) with \(A_n\)-module structures on the \(E_n\) compatible with the faces and degeneracies. They form an abelian category \(A\)-\(\operatorname{Mod}\) with exact filtered colimits. An *\(A\)-algebra* is a commutative \(A\)-algebra in \(\operatorname{Simpl}(T)\). A ring \(\Lambda\) of \(T\) is also the constant simplicial ring \(\Lambda\).

Simplicial sets are regarded as simplicial objects of \(T\) through constant sheaves. For a simplicial set \(K\) and an \(A\)-module \(E\) put
\[
\begin{gathered}K\odot E=A^{(K)}\otimes_AE,\\ (K\odot E)_n=\bigoplus_{K_n}E_n,\end{gathered}
\]
where \(A^{(K)}\) is the free \(A\)-module on \(K\). Let \(\underline{\operatorname{Homs}}_A(E,F)\) be the internal Hom of \(A\)-modules in the topos \(\operatorname{Simpl}(T)\). Its sheaf of \(n\)-simplices is the sheaf of \(A\)-linear maps \(\Delta[n]\odot E\to F\). For a simplicial set \(K\), \(\underline{\operatorname{Homs}}(K,F)=\underline{\operatorname{Homs}}_A(A^{(K)},F)\) has as \(n\)-simplices the maps \(K\times\Delta[n]\to F\). It is an \(A\)-module, and an \(A\)-algebra if \(F\) is one. The tensor–Hom adjunction [Stacks, Tag 04TT] gives natural bijections
\[
\begin{aligned}&\operatorname{Hom}_A(K\odot E,F)\\&\quad =\operatorname{Hom}_A\bigl(E,\underline{\operatorname{Homs}}(K,F)\bigr),\end{aligned}
\]
and \((K\times L)\odot E=K\odot(L\odot E)\).

For an \(A\)-module \(E\), \(NE\) is the Moore normalization of the underlying simplicial abelian sheaf: \(N_nE=\bigcap_{i=1}^n\ker d_i\), with differential \(d_0\). Its homology sheaves \(\pi_n(E)=H_n(NE)\) are the homotopy sheaves of the underlying simplicial sheaf at \(0\) (Proposition 1.4 of *The cotangent complex*, applied to sections and sheafified, and Section 1 of the lesson on homotopy sheaves). A map of \(A\)-modules or of \(A\)-algebras is a *quasi-isomorphism* if it induces isomorphisms on all \(\pi_n\). A module \(E\) is *acyclic* if \(\pi_*(E)=0\).

## 1. Homotopies

Let \(e_0,e_1\colon\Delta[0]\to\Delta[1]\) be the two vertices. An *\(A\)-homotopy* from \(u_0\) to \(u_1\colon E\to F\) is an \(A\)-linear map \(h\colon\Delta[1]\odot E\to F\) with \(h\circ(e_i\odot E)=u_i\). By the adjunction it is the same as an \(A\)-linear map \(E\to\underline{\operatorname{Homs}}(\Delta[1],F)\) whose two vertex evaluations are \(u_0\) and \(u_1\). Homotopies of \(A\)-algebras are defined in the same way, with \(E\to\underline{\operatorname{Homs}}(\Delta[1],F)\) a map of \(A\)-algebras.

**Lemma 1.1.** Let \(G\) be the simplicial abelian group of global sections of \(\underline{\operatorname{Homs}}_A(E,F)\), so that \(G_0=\operatorname{Hom}_A(E,F)\) and \(G_1\) is the group of \(A\)-homotopies. The relation "there is an \(A\)-homotopy from \(u_0\) to \(u_1\)" is an equivalence relation, compatible with sums and with composition on both sides. The set of classes is the abelian group
\[
\begin{aligned}&\operatorname{Hot}_A(E,F) =\pi_0(G)\\&\quad =G_0/(d_0-d_1)G_1.\end{aligned}
\]

**Proof.** A homotopy \(\omega\in G_1\) goes from \(d_1\omega\) to \(d_0\omega\). The degenerate \(s_0u\) goes from \(u\) to \(u\). If \(\omega\) goes from \(a\) to \(b\), then \(s_0a+s_0b-\omega\) goes from \(b\) to \(a\). If \(\omega'\) goes from \(b\) to \(c\), then \(\omega+\omega'-s_0b\) goes from \(a\) to \(c\). Composition with a map on either side is a map of simplicial abelian groups between the corresponding \(G\), so it preserves the relation, as do sums. \(\square\)

Let \(\operatorname{Hot}_\bullet(A)\) be the additive category with the \(A\)-modules as objects and the groups \(\operatorname{Hot}_A(E,F)\) as morphisms. A map is an *\(A\)-homotopy equivalence* if it becomes invertible there.

For \(A\)-algebras the formulas of Lemma 1.1 do not apply, because a sum of maps of algebras is not a map of algebras. Two maps of algebras are called *homotopic* if they are related by the equivalence relation generated by \(A\)-homotopies. A *zigzag interval* \(I\) is a chain of finitely many copies of \(\Delta[1]\), each glued by one of its vertices to a vertex of the next, with ends \(\partial I=\{a,b\}\). A chain of homotopies from \(u_0\) to \(u_1\), each in either direction, is the same as a map of algebras \(E\to\underline{\operatorname{Homs}}(I,F)\) with values \(u_0\) at \(a\) and \(u_1\) at \(b\). The relation is compatible with composition on both sides. Let \(\operatorname{Hot}(A\text{-}\mathrm{Alg})\) be the category of \(A\)-algebras with homotopy classes of maps.

**Lemma 1.2.** \(\operatorname{Hot}_\bullet(A)\) (respectively \(\operatorname{Hot}(A\text{-}\mathrm{Alg})\)) is the localization of \(A\)-\(\operatorname{Mod}\) (respectively \(A\)-\(\operatorname{Alg}\)) with respect to \(A\)-homotopy equivalences.

**Proof.** Let \(\pi\colon\Delta[1]\odot E\to E\) be induced by \(\Delta[1]\to\Delta[0]\). Then \(\pi\circ(e_0\odot E)=1\). The order-preserving map \([1]\times[1]\to[1]\), \((a,b)\mapsto\min(a,b)\), gives by Proposition 2.1 of the lesson on décalage a map \(\Delta[1]\times\Delta[1]\to\Delta[1]\). Applied to the second factor, it is a homotopy from \((e_0\odot E)\circ\pi\) to the identity of \(\Delta[1]\odot E\). So \(\pi\) is a homotopy equivalence. A functor \(\Phi\) that inverts homotopy equivalences inverts \(\pi\), so \(\Phi(e_0\odot E)=\Phi(\pi)^{-1}=\Phi(e_1\odot E)\). Hence \(\Phi(u_0)=\) \(\Phi(h)\Phi(e_0\odot E)=\) \(\Phi(h)\Phi(e_1\odot E)=\) \(\Phi(u_1)\) for every homotopy \(h\), and \(\Phi\) factors uniquely through the homotopy category. Conversely, homotopy equivalences become invertible there. For algebras use the path algebra: the evaluations \(\operatorname{ev}_0,\operatorname{ev}_1\colon\underline{\operatorname{Homs}}(\Delta[1],F)\to F\) both have the constant paths \(c\) as a section, and \(c\circ\operatorname{ev}_0\) is homotopic to the identity by the same contraction. So a functor \(\Phi\) inverting homotopy equivalences has \(\Phi(\operatorname{ev}_0)=\Phi(c)^{-1}=\Phi(\operatorname{ev}_1)\), and identifies the two ends \(\operatorname{ev}_iH\) of every homotopy \(H\). \(\square\)

## 2. Normalization and homology

**Proposition 2.1.** Let \(A\) be a simplicial ring and \(E\) an \(A\)-module. The shuffle map
\[
\operatorname{sh}\colon\operatorname{Tot}(NA\otimes NA)\to N(A\otimes A),
\]
followed by the normalization of the multiplication, makes \(NA\) a differential graded ring. It is associative and unital, and graded commutative: \(xy=(-1)^{pq}yx\) for \(x\in N_pA\), \(y\in N_qA\). In the same way \(NE\) is a differential graded \(NA\)-module. Hence \(H_*(A)=\bigoplus_n\pi_n(A)\) is a graded commutative ring and \(H_*(E)\) a graded \(H_*(A)\)-module. These structures are natural in \((A,E)\).

**Proof.** By Theorem 1.3 of *The cotangent complex*, the shuffle map is a natural chain map for simplicial modules. Its formula is a universal integer combination of degeneracies, so it applies to sections over every object of \(T\) and is compatible with sheafification. It is associative: both iterated shuffle maps \(NV\otimes NW\otimes NX\to N(V\otimes W\otimes X)\) are the sum over the \((p,q,r)\)-shuffles of the three lists with the sign of the shuffle permutation. It is unital, because the only shuffle of a degree-\(0\) element is trivial. It is graded commutative: exchanging the two lists is a bijection between \((p,q)\)-shuffles and \((q,p)\)-shuffles that multiplies the sign by \((-1)^{pq}\), so \(\operatorname{sh}(y\otimes x)=(-1)^{pq}\tau\operatorname{sh}(x\otimes y)\), where \(\tau\) exchanges the factors of \(A\otimes A\). Since \(A\) is commutative, the multiplication is invariant under \(\tau\). The same argument for \(A\otimes E\to E\) gives the module structure. A morphism of rings or modules commutes with all these maps. \(\square\)

**Proposition 2.2.** Let \(\Lambda\) be a ring of \(T\) and \(E,F\) simplicial \(\Lambda\)-modules. The natural map
\[
\begin{aligned}&\Psi \colon N\underline{\operatorname{Homs}}_\Lambda(E,F)\\&\quad \longrightarrow\tau_{\geq0}\operatorname{Hom}^\bullet_\Lambda(NE,NF),\end{aligned}
\]
defined in the proof, is a chain homotopy equivalence. Here \(\tau_{\geq0}\) keeps the degrees \(\geq0\), with the cycles in degree \(0\).

**Proof.** Write \(H=\underline{\operatorname{Homs}}_\Lambda(E,F)\) and \(\operatorname{ev}\colon H\otimes_\Lambda E\to F\) for the evaluation. The map \(\Psi\) of the statement is the adjoint of the chain map \(N(\operatorname{ev})\circ\operatorname{sh}\colon\) \(NH\otimes NE\to\) \(N(H\otimes E)\to\) \(NF\), where \(\operatorname{sh}\) is the shuffle map. It lands in \(\tau_{\geq0}\), because \(NH\) vanishes in negative degrees. Both sides are chain complexes of sheaves in degrees \(\geq0\). By the Yoneda lemma in the homotopy category of such complexes, it suffices that for every such complex \(L\) composition with \(\Psi\) is bijective on homotopy classes of maps from \(L\).

A map \(f\colon L\to NH\) corresponds by Dold–Kan to \(\tilde f\colon\Gamma L\to H\), and by adjunction to \(g=\operatorname{ev}\circ(\tilde f\otimes1)\colon\Gamma L\otimes E\to F\). These correspondences are bijective on homotopy classes, because homotopies are maps out of \(\Delta[1]\odot(-)\) [Stacks, Tag 019S], and chain homotopies give simplicial homotopies by the paragraph after Theorem 1.3 of *The cotangent complex*. Normalization identifies homotopy classes of maps \(\Gamma L\otimes E\to F\) with those of \(N(\Gamma L\otimes E)\to NF\) (Remark 4.3). Composition with the shuffle homotopy equivalence \(\operatorname{sh}\colon\) \(L\otimes NE=\) \(N\Gamma L\otimes NE\to\) \(N(\Gamma L\otimes E)\) identifies them with homotopy classes of maps \(L\otimes NE\to NF\), and these are homotopy classes of maps \(L\to\tau_{\geq0}\operatorname{Hom}^\bullet(NE,NF)\). By naturality of the shuffle map, \(N(\operatorname{ev})\circ\operatorname{sh}\circ(f\otimes1)=N(g)\circ\operatorname{sh}\). So the composite bijection is \(f\mapsto\Psi\circ f\). \(\square\)

## 3. Cylinders, paths and fibrations

**Definition 3.1.** A map \(f\colon X\to Y\) of \(A\)-modules is a *fibration* if \(N_nf\) is an epimorphism for every \(n\geq1\). A map of \(A\)-algebras is a fibration if its underlying map of modules is one.

**Lemma 3.2.**

1. \(f\) is a fibration if and only if its degreewise cokernel is a constant simplicial module. Then this cokernel is \(\operatorname{coker}\pi_0(f)\), and \(X\to Y\to\operatorname{coker}\pi_0(f)\to0\) is exact.
2. \(f\) is a fibration and a quasi-isomorphism if and only if \(f\) is an epimorphism with acyclic kernel. We then call \(f\) a *fibrant quasi-isomorphism*.
3. If \(f\) is a fibration with kernel \(K\), there is a long exact sequence
\[
\begin{aligned}&\quad \cdots \to\pi_nK \to\pi_nX\\&\quad \to\pi_nY \to\pi_{n-1}K\\&\quad \to\cdots\\&\quad \quad \to\pi_0K \to\pi_0X \to\pi_0Y\\&\quad \to\operatorname{coker}\pi_0(f) \to0.\end{aligned}
\]
4. Fibrations are stable under composition and base change, and the base change of a fibrant quasi-isomorphism is a fibrant quasi-isomorphism.

**Proof.** (1) Normalization is exact, so \(N(\operatorname{coker}f)=\operatorname{coker}Nf\). This vanishes in positive degrees exactly when \(f\) is a fibration. A simplicial module whose normalization is concentrated in degree \(0\) is constant, by Dold–Kan. Its degree-\(0\) term is \(\operatorname{coker}(f_0)\), which is \(\operatorname{coker}\pi_0(f)\): the boundaries \(d_0N_1Y=d_0N_1f(N_1X)\) already lie in \(f_0(X_0)\).

(2) If \(f\) is a fibrant quasi-isomorphism, its cokernel is the constant module \(\operatorname{coker}\pi_0(f)=0\), so \(f\) is an epimorphism, and its kernel is acyclic by the long exact sequence of \(0\to K\to X\to Y\to0\). Conversely, an epimorphism has \(Nf\) epimorphic, and acyclicity of the kernel gives a quasi-isomorphism.

(3) Let \(I\) be the image of \(f\). The long exact sequences of \(0\to K\to X\to I\to0\) and \(0\to I\to Y\to\operatorname{coker}f\to0\), together with \(\pi_n(\text{constant})=0\) for \(n\geq1\), give it.

(4) For a composite, \(N(gf)=N(g)N(f)\). For a base change \(f'\) of \(f\) along \(Y'\to Y\), the induced map \(\operatorname{coker}f'\to\operatorname{coker}f\) is a monomorphism, and a simplicial submodule of a constant module is constant (its degeneracies and faces are the identity). A base change of an epimorphism with kernel \(K\) is an epimorphism with kernel \(K\). \(\square\)

**Proposition 3.3 (mapping cylinder).** Let \(f\colon E\to F\) be a map of \(A\)-modules. Put \(M(f)=F\amalg_E(\Delta[1]\odot E)\), the pushout of \(f\) and \(e_0\odot E\). Let \(i\colon E\to M(f)\) be induced by \(e_1\) and \(p\colon M(f)\to F\) by \(\Delta[1]\to\Delta[0]\) and the identity of \(F\). Then \(f=pi\), \(i\) is a monomorphism, and \(p\) is an \(A\)-homotopy equivalence, with inverse the inclusion \(j\colon F\to M(f)\).

**Proof.** In degree \(n\), \((\Delta[1]\odot E)_n=\bigoplus_{\alpha\in\Delta[1]_n}E_n\), and \(e_0\) is the summand of the constant simplex \(0\). So \(M(f)_n=F_n\oplus\bigoplus_{\alpha\neq0}E_n\), and \(i_n\) is the inclusion of the summand of the constant simplex \(1\). Clearly \(pj=1\) and \(pi=f\). The contraction \(\min\colon\Delta[1]\times\Delta[1]\to\Delta[1]\) of the proof of Lemma 1.2 fixes the vertex \(0\). So it passes to the pushout and, together with the constant homotopy on \(F\), gives a homotopy from \(jp\) to the identity. \(\square\)

**Proposition 3.4 (path factorization).** Let \(f\colon E\to F\) be a map of \(A\)-modules or of \(A\)-algebras. Put \(\operatorname{Path}(F)=\underline{\operatorname{Homs}}(\Delta[1],F)\), with evaluations \(\operatorname{ev}_0,\operatorname{ev}_1\) at the vertices, and \(P_f=E\times_{F}\operatorname{Path}(F)\), the fibre product of \(f\) and \(\operatorname{ev}_0\). Let \(i(x)=(x,\text{constant path at }f(x))\) and \(p=\operatorname{ev}_1\circ\operatorname{pr}_2\). Then \(f=pi\), \(i\) is a homotopy equivalence with inverse \(\operatorname{pr}_1\), and \(p\) is a fibration. If \(f\) is a map of \(A\)-algebras over an \(A\)-algebra \(B\), and the structure maps \(E\to B\), \(F\to B\) are fibrations, the same holds over \(B\) with \(\operatorname{Path}(F/B)\), the paths whose image in \(B\) is constant.

**Proof.** The contraction \(\omega\mapsto\omega\circ\min(-,t)\) of paths to their initial vertex is a homotopy from \(i\circ\operatorname{pr}_1\) to the identity of \(P_f\), and \(\operatorname{pr}_1\circ i=1\). It is induced by a map of simplicial sets, so it respects the module and algebra structures, and the constancy over \(B\).

For the fibration property, let \(n\geq1\) and \(z\in N_nF\), over some object of \(T\). The order-preserving map \([1]\times[n]\to[n]\), \((0,j)\mapsto0\), \((1,j)\mapsto j\), gives \(H\colon\Delta[1]\times\Delta[n]\to\Delta[n]\). The path \(\omega=z\circ H\in\operatorname{Path}(F)_n\) has \(\operatorname{ev}_1\omega=z\). Its other end \(\operatorname{ev}_0\omega\) is the degenerate simplex on the vertex \(0\) of \(z\), which is \(0\) because \(d_nz=0\). So \((0,\omega)\in(P_f)_n\) and \(p(0,\omega)=z\). Applying the natural normalization projection of Theorem 1.1 of *The cotangent complex* to \((0,\omega)\) gives an element of \(N_nP_f\) over \(z\). This construction is a map of sheaves, so \(N_np\) is an epimorphism.

Over \(B\), let \(b\) be the image of \(z\) in \(N_nB\). Since \(E\to B\) is a fibration, locally \(b\) is the image of some \(x\in N_nE\). The difference \(z-f(x)\) lies in the kernel of \(F\to B\), and \(\omega=c(f(x))+(z-f(x))\circ H\), with \(c\) the constant path, is a path over \(B\) from \(f(x)\) to \(z\). Then \((x,\omega)\) lies over \(z\), and the normalization projection gives an element of \(N_nP_f\) over \(z\). \(\square\)

**Cones, paths and loops.** For an \(A\)-module \(X\):

- the *cone* \(\gamma X=(\Delta[1]\odot X)/(e_1\odot X)\), with the injection \(X\to\gamma X\) through \(e_0\). The contraction \(\max\colon\Delta[1]\times\Delta[1]\to\Delta[1]\) toward the vertex \(1\) is a homotopy from the identity of \(\gamma X\) to \(0\), so \(\gamma X\) is homotopy equivalent to \(0\);
- the *suspension* \(\sigma X=\gamma X/X\);
- the *path module* \(PX=\ker(\operatorname{ev}_1\colon\operatorname{Path}(X)\to X)\), the paths ending at \(0\), with the map \(\operatorname{ev}_0\colon PX\to X\). It is a fibration: for \(z\in N_nX\), \(n\geq1\), the proof of Proposition 3.4 gives a path \(\omega\) from \(0\) to \(z\), and \(c(z)-\omega\), with \(c(z)\) the constant path, goes from \(z\) to \(0\); the normalization projection of Theorem 1.1 of *The cotangent complex* turns it into an element of \(N_n(PX)\) over \(z\). The contraction \(\omega\mapsto\omega\circ\max(-,t)\) to the vertex \(1\) shows \(PX\simeq0\);
- the *loop module* \(\Omega X=\ker(\operatorname{ev}_0\colon PX\to X)\), the loops at \(0\);
- for \(f\colon X\to Y\), the *cone* \(C(f)=M(f)/i(X)=Y\amalg_X\gamma X\), and for \(t\colon X\to Y\) the *fibre* \(\operatorname{Fib}(t)=\ker(p\colon P_t\to Y)\), the pairs of a point \(x\) and a path from \(t(x)\) to \(0\); it is the fibre product \(X\times_YPY\) of \(t\) and \(\operatorname{ev}_0\).

**Lemma 3.5.** \(\pi_n(\sigma X)=\pi_{n-1}(X)\) and \(\pi_n(\Omega X)=\pi_{n+1}(X)\) for \(n\geq0\), with \(\pi_{-1}=0\). The cone \(C(f)\) is acyclic if and only if \(f\) is a quasi-isomorphism. If \(t\) is a quasi-isomorphism, \(\operatorname{Fib}(t)\) is acyclic.

**Proof.** The first two statements are the long exact sequences of \(0\to X\to\gamma X\to\sigma X\to0\) and of the fibration \(\operatorname{ev}_0\colon PX\to X\) with kernel \(\Omega X\) (Lemma 3.2 (3)), since \(\gamma X\) and \(PX\) are acyclic. For the cone, the sequence \(0\to X\xrightarrow{i}M(f)\to C(f)\to0\) is exact, and \(M(f)\to Y\) is a homotopy equivalence with \(pi=f\). Its long exact sequence reads \(\cdots\to\) \(\pi_nX\xrightarrow{f}\) \(\pi_nY\to\) \(\pi_nC(f)\to\) \(\pi_{n-1}X\to\) \(\cdots\). For the fibre, \(p\colon P_t\to Y\) is a fibration, and a quasi-isomorphism when \(t\) is, because \(i\) is a homotopy equivalence and \(pi=t\). By Lemma 3.2 (2) its kernel \(\operatorname{Fib}(t)\) is acyclic. \(\square\)

**Lemma 3.6 (lifting).** Let \(t\colon Y\to Z\) be a fibrant quasi-isomorphism of \(A\)-modules, and \(j\colon K\to L\) a monomorphism of simplicial sets with finitely many nondegenerate simplices.

1. Every lifting problem of \(j\) against \(t\) over an object \(U\) of \(T\) has solutions locally on \(U\).
2. The map \(\Phi\colon\) \(\underline{\operatorname{Homs}}(L,Y)\to\) \(\underline{\operatorname{Homs}}(K,Y)\times\) \(_{\underline{\operatorname{Homs}}(K,Z)}\underline{\operatorname{Homs}}(L,Z)\) is a fibrant quasi-isomorphism.

**Proof.** (1) Attaching the nondegenerate simplices of \(L\) outside \(K\) in order of dimension writes \(j\) as a finite composite of pushouts of boundary inclusions \(\partial\Delta[m]\to\Delta[m]\). Local solvability is preserved by pushouts and, after common refinement of coverings, by finite composites. So let \(j=\partial\Delta[m]\to\Delta[m]\), with \(a\colon\partial\Delta[m]\to Y\) and \(b\in Z_m\) over \(U\) such that \(t\circ a\) is the boundary of \(b\). Locally \(b=t(y)\), because \(t\) is an epimorphism. Then \(k=a-y|_{\partial\Delta[m]}\) is a map \(\partial\Delta[m]\to W\), \(W=\ker t\), and it suffices to extend it to \(\Delta[m]\) locally. By Dold–Kan, maps \(\mathbb Z(\partial\Delta[m])\to W\) are chain maps \(\varphi\colon C\to NW\), where \(C=N\mathbb Z(\partial\Delta[m])\), computed in the quotient model by degenerate simplices (Theorem 1.1 of *The cotangent complex*). The nondegenerate simplices of \(\Delta[m]\) are those of \(\partial\Delta[m]\) and the top simplex, so \(N\mathbb Z(\Delta[m])=C\oplus\mathbb Z\epsilon\), with \(\epsilon\) in degree \(m\) and \(d\epsilon=\beta\in C_{m-1}\) a cycle. An extension of \(\varphi\) is the choice of \(w\in N_mW\) with \(dw=\varphi(\beta)\). The cycle \(\varphi(\beta)\) is locally a boundary, because \(W\) is acyclic. With such a \(w\) and the corresponding extension \(\tilde k\), the simplex \(y+\tilde k\) solves the problem.

(2) In degree \(n\), surjectivity of \(\Phi\) is the lifting problem of \((K\times\Delta[n])\to(L\times\Delta[n])\) against \(t\), solvable locally by (1). Its kernel is \(V=\{c\colon L\to W,\ c|_K=0\}\). A simplicial abelian sheaf \(V\) is acyclic if and only if every map \(\partial\Delta[m]\to V\) extends locally to \(\Delta[m]\), for every \(m\geq1\). Indeed, by the description in (1) a map extends locally exactly when the cycle \(\varphi(\beta)\) is locally a boundary. And every cycle \(c\) of degree \(m-1\) is \(\varphi(\beta)\) for some chain map \(\varphi\): send the face \(d_0\epsilon\) to \(c\) and all other nondegenerate faces to \(0\). By adjunction, such an extension for \(V\) is a lifting problem of the monomorphism \((\partial\Delta[m]\times L)\cup(\Delta[m]\times K)\to\) \(\Delta[m]\times L\) against \(W\to0\). The map \(W\to0\) is a fibrant quasi-isomorphism, so (1) applies. So \(V\) is acyclic, and \(\Phi\) is an epimorphism with acyclic kernel, a fibrant quasi-isomorphism by Lemma 3.2 (2). \(\square\)

## 4. The derived category and fractions

Let \(D_\bullet(A)\) be the localization of \(A\)-\(\operatorname{Mod}\) with respect to quasi-isomorphisms, and \(D(A\text{-}\mathrm{Alg})\), \(D(A\text{-}\mathrm{Alg}/B)\) the corresponding localizations of \(A\)-algebras and of \(A\)-algebras over \(B\). Homotopy equivalences are quasi-isomorphisms, because homotopic maps induce homotopic maps of normalized complexes [Stacks, Tag 019S]. By Lemma 1.2, these are also the localizations of the homotopy categories.

**Lemma 4.1.** A pushout of a monomorphic quasi-isomorphism is a monomorphic quasi-isomorphism. A base change of a fibrant quasi-isomorphism is a fibrant quasi-isomorphism.

**Proof.** A pushout of a monomorphism \(u\) in an abelian category is a monomorphism with the same cokernel. The cokernel of \(u\) is acyclic by the long exact sequence, so the pushout is a quasi-isomorphism. The second statement is Lemma 3.2 (4). \(\square\)

**Theorem 4.2 (Illusie).** Let \(A\) be a simplicial ring.

1. In \(\operatorname{Hot}_\bullet(A)\), the quasi-isomorphisms admit a calculus of left fractions and a calculus of right fractions.
2. In \(\operatorname{Hot}(A\text{-}\mathrm{Alg})\), the quasi-isomorphisms admit a calculus of right fractions.
3. Let \(B\) be an \(A\)-algebra and \(\operatorname{Hotfib}(A\text{-}\mathrm{Alg}/B)\) the full subcategory of \(\operatorname{Hot}(A\text{-}\mathrm{Alg}/B)\), algebras over \(B\) up to homotopy over \(B\), formed by the algebras whose structure map is a fibration. There the quasi-isomorphisms admit a calculus of right fractions, and the localization is equivalent to \(D(A\text{-}\mathrm{Alg}/B)\).

**Proof.** In all cases the quasi-isomorphisms contain the identities, are stable under composition, satisfy two out of three, and are compatible with homotopy. These are the first axioms of [Stacks, Tag 04VC].

*Left Ore condition for modules.* Let \(s\colon X\to X'\) be a quasi-isomorphism and \(u\colon X\to Y\). By Proposition 3.3, \(s=pi\) with \(i\colon X\to M(s)\) monomorphic and \(p\) a homotopy equivalence, so up to an isomorphism of \(\operatorname{Hot}_\bullet(A)\) we may replace \(s\) by \(i\), a monomorphic quasi-isomorphism. Its pushout \(t\colon Y\to Y\amalg_XM(s)\) along \(u\) is a quasi-isomorphism by Lemma 4.1, and the pushout square gives \(u's=tu\).

*Left cancellation for modules.* Let \(h\colon X\to Y\) and a quasi-isomorphism \(s\colon X'\to X\) satisfy \(hs\simeq0\). We find a quasi-isomorphism \(t\) with \(th\simeq0\). Write \(s=pi\) as in Proposition 3.3, with \(j\) the homotopy inverse of \(p\). If \(t(hp)\simeq0\) then \(th=thpj\simeq0\), so we may replace \(s\) by the monomorphism \(i\) and \(h\) by \(hp\). A homotopy from \(hs\) to \(0\) is an \(A\)-linear map \(k\colon\gamma X'\to Y\) restricting to \(hs\) on \(X'\). Together with \(h\) it defines \(\tilde h\colon C(s)=X\amalg_{X'}\gamma X'\to Y\) with \(\tilde h\circ(X\to C(s))=h\). By Lemma 3.5, \(Q=C(s)\) is acyclic. Let \(t\colon Y\to Y'=Y\amalg_Q\gamma Q\) be the pushout of the injection \(Q\to\gamma Q\) along \(\tilde h\). Its cokernel \(\sigma Q\) is acyclic by Lemma 3.5, so \(t\) is a monomorphic quasi-isomorphism. And \(th\) factors through \(\gamma Q\), which is homotopy equivalent to \(0\), so \(th\simeq0\).

*Right Ore condition.* Let \(t\colon Y\to Z\) be a quasi-isomorphism and \(u\colon X\to Z\), of modules or of algebras. By Proposition 3.4, \(t=pi\) with \(i\) a homotopy equivalence and \(p\) a fibration, which is a quasi-isomorphism by two out of three. Replace \(t\) by \(p\). The base change \(s\colon X\times_ZP_t\to X\) is a fibrant quasi-isomorphism by Lemma 4.1, and the fibre square gives \(tu'=us\) up to the homotopy equivalence \(i\).

*Right cancellation for modules.* Let \(h\colon X\to Y\) and a quasi-isomorphism \(t\colon Y\to Z\) satisfy \(th\simeq0\). A homotopy from \(th\) to \(0\) is a map \(X\to\operatorname{Path}(Z)\) with ends \(th\) and \(0\). Together with \(h\) it gives \(\tilde h\colon X\to \operatorname{Fib}(t)\) with \(\operatorname{pr}\circ\tilde h=h\). By Lemma 3.5, \(\operatorname{Fib}(t)\) is acyclic. The fibration \(\operatorname{ev}_0\colon P(\operatorname{Fib}(t))\to \operatorname{Fib}(t)\) has the acyclic source \(P(\operatorname{Fib}(t))\), so it is a fibrant quasi-isomorphism. Its base change \(s\colon X'=X\times_{\operatorname{Fib}(t)}P(\operatorname{Fib}(t))\to X\) along \(\tilde h\) is a fibrant quasi-isomorphism, and \(hs\) factors through \(P(\operatorname{Fib}(t))\simeq0\). So \(hs\simeq0\). Since homotopy classes of maps of modules form groups, the two cancellation statements for a pair of maps \(f,g\) follow by taking \(h=f-g\). This proves (1).

*Right cancellation for algebras.* Let \(f,g\colon X\to Y\) be maps of algebras and \(t\colon Y\to Z\) a quasi-isomorphism with \(tf\simeq tg\). With \(t=pi\) as above, \(q=\operatorname{pr}_1\) a homotopy inverse of \(i\) with \(qi=1\), it suffices to treat \(if,ig\) and \(p\): if \((if)s\simeq(ig)s\), then \(fs=qifs\simeq qigs=gs\). So let \(t\) be a fibrant quasi-isomorphism. A chain of homotopies from \(tf\) to \(tg\) is a map of algebras \(H\colon X\to\underline{\operatorname{Homs}}(I,Z)\) for a zigzag interval \(I\). The pair \((f,g)\) and \(H\) define a map from \(X\) to the target of the map \(\Phi\) of Lemma 3.6 (2) for \(\partial I\subset I\). Since \(\Phi\) is a map of algebras and a fibrant quasi-isomorphism, its base change \(s\colon X'\to X\) is one too. The projection \(X'\to\underline{\operatorname{Homs}}(I,Y)\) is a chain of homotopies of algebras from \(fs\) to \(gs\). This proves (2).

*Over \(B\).* Path objects over \(B\) give the same arguments. For fibrant \(Y,Z\) over \(B\) and \(t\) over \(B\), the map \(\Phi_B\) for \(\operatorname{Path}(-/B)\) is the base change of \(\Phi\) to the elements of the target whose path lies over a constant path of \(B\). Indeed, a lift of such a path has the same image in \(B\). Base changes and composites of fibrations over \(B\) are fibrations, by Lemma 3.2 (4), so all constructions stay in the fibrant subcategory. For the equivalence, Proposition 3.4 applied to the structure map \(Q\to B\) gives, functorially in \(Q\), a homotopy equivalence \(Q\to R(Q)\) over \(B\) with \(R(Q)\to B\) a fibration. The functor \(R\) preserves quasi-isomorphisms, and the natural quasi-isomorphisms \(Q\to R(Q)\) show that \(R\) and the inclusion induce inverse equivalences of the localizations. \(\square\)

**Remark 4.3.** For the constant simplicial ring \(\Lambda\), normalization identifies simplicial \(\Lambda\)-modules with chain complexes of \(\Lambda\)-modules in degrees \(\geq0\), \(A\)-homotopies with chain homotopies [Stacks, Tag 019S] (and the paragraph after Theorem 1.3 of *The cotangent complex* for the converse), and quasi-isomorphisms with quasi-isomorphisms. So \(D_\bullet(\Lambda)\) is the category of Lemma 1.1 of the lesson on stable derived functors, equivalent to \(D^{\leq0}(\Lambda)\), and Theorem 4.2 (1) recovers the calculus of fractions for complexes.

## 5. Examples

**Example 5.1 (an exterior algebra).** Let \(V=K(\mathbb Z,1)=\Gamma(\mathbb Z[1])\) and let \(A=S(V)\) be its symmetric algebra, a simplicial ring. By the Koszul shift formula of the lesson on Koszul complexes, \(LS^n(\mathbb Z[1])=L\Lambda^n(\mathbb Z)[n]\), which is \(\mathbb Z\) in degree \(1\) for \(n=1\), and \(0\) for \(n\geq2\). So \(\pi_*(A)=\mathbb Z\oplus\mathbb Z[1]\), and by Proposition 2.1 \(H_*(A)\) is the exterior algebra on a class of degree \(1\). 

**Example 5.2 (suspensions of constant modules).** For a ring \(\Lambda\) of \(T\) and a \(\Lambda\)-module \(M\), regarded as a constant simplicial module, the suspension \(\sigma M\) has \(\pi_1=M\) and no other homotopy, by Lemma 3.5. Its normalized complex is \(M\) in degree \(1\), so \(\sigma M\cong K(M,1)\), the nerve of \(M\).

## 6. Exercises

**6.1.** Show that for every \(A\)-module \(X\), the cone \(C(1_X)\) is homotopy equivalent to \(0\), and that \(C(X\to0)=\sigma X\).

**6.2.** Let \(f\colon X\to Y\) be a fibration of \(A\)-modules with \(\pi_0(f)\) surjective. Show that \(f\) is an epimorphism.

**6.3.** Let \(f\colon X\to Y\) be a monomorphism of \(A\)-modules. Construct a natural map \(C(f)\to Y/X\) and show that it is a quasi-isomorphism.

## 7. Complete solutions

**6.1.** \(C(1_X)=X\amalg_X\gamma X=\gamma X\), which is homotopy equivalent to \(0\) by the contraction toward the vertex \(1\). For \(X\to0\), \(C=0\amalg_X\gamma X=\gamma X/X=\sigma X\).

**6.2.** By Lemma 3.2 (1), the cokernel of \(f\) is the constant module \(\operatorname{coker}\pi_0(f)=0\).

**6.3.** Define \(C(f)=Y\amalg_X\gamma X\to Y/X\) as the projection on \(Y\) and \(0\) on \(\gamma X\). It is well defined because \(X\subseteq Y\) goes to \(0\). The composite \(M(f)\to C(f)\to Y/X\) equals \(M(f)\xrightarrow{p}Y\to Y/X\): both are the projection on \(Y\), and both kill \(\Delta[1]\odot X\), because \(p\) maps it to \(f(X)\). So there is a map of short exact sequences from \(0\to X\to M(f)\to C(f)\to0\) to \(0\to X\to Y\to Y/X\to0\), which is the identity on \(X\) and \(p\) in the middle. Since \(p\) is a homotopy equivalence, the five lemma on the long exact sequences shows that \(C(f)\to Y/X\) is a quasi-isomorphism.

## Sources

The homotopy theory of simplicial rings and modules in a topos, with the calculus of fractions of Theorem 4.2, is due to Illusie, in his work on the cotangent complex. The description of fibrations of simplicial abelian groups through the normalized complex is due to Moore. The Dold–Kan correspondence and the Eilenberg–Zilber theorem are taken from the lesson *The cotangent complex* and the AI-integrated Stacks project.
