# The stable ring of a ring and the Mac Lane resolution

*Written by Claude Opus 5.5 (Anthropic) on 21 October 2026. Self-checked by the writing AI. Public domain (CC0).*

The stabilization of the free abelian group functor, applied to a ring \(A\) of a topos, is a simplicial abelian sheaf \(\mathbb Z^{\mathrm{st}}(A)\) with homology \(A\) in degree \(0\) and none in degree \(1\) ([*Stable derived functors*](stable-derived-functors.md), Example 2.1). This lesson shows that it is a simplicial ring, flat over \(\mathbb Z\), and that its augmentation to \(A\) is a ring homomorphism. The ring structure comes from the spectrum \(A(1)^\times\) of [*Graded rings and the spectra of modules*](graded-rings-and-the-spectra-of-modules.md): the free abelian group functor turns its multiplication into the multiplication of a ring of type \(C_\bullet(S_1)\), and the double diagonal of [*Diagonal rings and adjunction formulas*](diagonal-rings-and-adjunction-formulas.md) turns that into \(\mathbb Z^{\mathrm{st}}(A)\). An \(A\)-module \(M\) gives a \(\mathbb Z^{\mathrm{st}}(A)\)-module \(\mathbb Z^{\mathrm{st}}(M)\).

Two applications follow. Truncating the normalized ring \(N\mathbb Z^{\mathrm{st}}(A)\) gives a flat presentation of \(A\), which computes the derived tensor product \(A\otimes^{\mathbf L}_{\mathbb Z}B\) of two rings. And Mac Lane's theorem says that \(A\otimes^{\mathbf L}_{N\mathbb Z^{\mathrm{st}}(A)}N\mathbb Z^{\mathrm{st}}(M)\) is \(M\). Combined with the bar construction, it gives a resolution of \(M\), functorial in \(M\), whose terms are sums of direct summands of the free modules \(A(A^p\times M^q)\) on products of copies of \(A\) and \(M\).

**Prerequisites.** [*Diagonal rings and adjunction formulas*](diagonal-rings-and-adjunction-formulas.md) (Construction 2.1, Lemma 2.2, Proposition 2.3); [*Graded rings and the spectra of modules*](graded-rings-and-the-spectra-of-modules.md) (Definitions 1.2 and 3.2, Propositions 2.1 and 2.2); [*Stabilization of non-additive functors*](stabilization-of-non-additive-functors.md) (Definition 3.2, Lemma 3.4, Corollary 3.7); [*Stable derived functors*](stable-derived-functors.md) (Proposition 1.4 and Example 2.1); [*Differential graded modules in a topos*](differential-graded-modules-in-a-topos.md) (Propositions 1.3, 2.4–2.6, Lemmas 2.1, 2.2, 3.1 and 3.2); [*Simplicial rings and modules in a topos*](simplicial-rings-and-modules-in-a-topos.md), Proposition 2.1; [*Derived tensor products of simplicial modules*](derived-tensor-products-of-simplicial-modules.md) (Lemma 1.1, Lemma 5.1, Proposition 5.2); [*Non-additive functors of complexes in a ringed topos*](non-additive-functors-of-complexes-in-a-ringed-topos.md) (Section 3 and Construction 4.3); local inductive limits, Section 5 of [*Homotopy sheaves and the free abelian Whitehead theorem*](homotopy-sheaves-and-the-free-abelian-whitehead-theorem.md); Theorems 1.1–1.3 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex#1-simplicial-algebra-and-the-standard-resolution). From the AI-integrated Stacks project: bounded above complexes of flat modules are K-flat [[Stacks, Tag 06YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-bounded-flat-K-flat)]; the standard simplicial resolution of an adjunction [[Tag 08NC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-standard-simplicial)].

## Conventions

\(T\) is the topos of sheaves on a site. Rings are associative and unital, not necessarily commutative, and modules are left modules. For a sheaf of sets \(X\), \(\mathbb Z(X)\) is the free abelian sheaf on \(X\), the sheafification of \(U\mapsto\mathbb Z[X(U)]\), and \(R(X)=R\otimes_{\mathbb Z}\mathbb Z(X)\) the free \(R\)-module on \(X\) for a ring \(R\). Since sheafification commutes with finite limits and with tensor products, \(\mathbb Z(X\times Y)=\mathbb Z(X)\otimes\mathbb Z(Y)\), and \(\mathbb Z(X)\otimes F\) is the sheafification of \(U\mapsto\bigoplus_{X(U)}F(U)\), which is exact in \(F\). So \(\mathbb Z(X)\) is flat. A morphism \(X\times Y\to Z\) of sheaves of sets therefore induces a map \(\mathbb Z(X)\otimes\mathbb Z(Y)\to\mathbb Z(Z)\), and a monoid \(G\) of \(T\) gives the ring \(\mathbb Z(G)\), with \([g][h]=[gh]\).

Differential graded rings, their modules, derived categories, the derived tensor products \(\otimes^{\mathbf L}\) and the category \(D(\mathbf{Andg}(T))\) of differential graded rings in nonpositive degrees localized at the quasi-isomorphisms are those of the lesson on differential graded modules; left modules over a ring are modules over its opposite. For a simplicial ring \(R\), \(NR\) is the normalized differential graded ring, placed in degrees \(\leq0\), and \(NE\) the normalized module of an \(R\)-module \(E\) (Proposition 2.1 of the lesson on simplicial rings, whose proof uses commutativity only for graded commutativity). For a differential graded ring \(P\) in nonpositive degrees, \(t_1(P)=(P^{-1}/dP^{-2}\to P^0)\) is its truncated ring (Proposition 1.3 of the lesson on differential graded modules).

## 1. Derived tensor products of rings

**Lemma 1.1 (presentations).** Let \(S\) be a ring, \(q\colon Q\to S\) a surjective ring homomorphism with \(Q\) flat over \(\mathbb Z\), and \(J=\ker q\). Then \(J\) is flat over \(\mathbb Z\), and the complex \(Q_J=(J\to Q)\), with \(J\) in degree \(-1\), \(Q\) in degree \(0\) and the inclusion as differential, is a differential graded ring in nonpositive degrees for the multiplication of \(Q\) on \(Q\times Q\), \(Q\times J\) and \(J\times Q\) and zero on \(J\times J\). The projection \(Q_J\to S\) is a quasi-isomorphism of differential graded rings.

**Proof.** An abelian sheaf whose groups of sections have no torsion is flat: its tensor product with a sheaf \(G\) is the sheafification of \(U\mapsto F(U)\otimes G(U)\), which is exact in \(G\) because torsion-free abelian groups are flat, and sheafification is exact. Conversely, the sections of a flat sheaf have no torsion, since multiplication by \(n\) on \(\mathbb Z\) is injective. So \(Q\) has torsion-free sections, hence so has its subsheaf \(J\), and \(J\) is flat. The products lie in the stated terms because \(J\) is a two-sided ideal, and associativity holds because it holds in \(Q\). The Leibniz rule needs checking only on \(J\times J\), \(J\times Q\) and \(Q\times J\): for \(x,y\in J\), \(d(xy)=0\) and \((dx)y-x(dy)=xy-xy=0\); for \(x\in J\) and \(z\in Q\), \(d(xz)=xz=(dx)z\) and \(d(zx)=zx=z(dx)\). The cohomology of \(Q_J\) is \(Q/J=S\) in degree \(0\) and \(0\) in degree \(-1\). \(\square\)

**Proposition 1.2.** Let \(R\) and \(S\) be rings, and \(Q\to S\) a presentation as in Lemma 1.1. Put
\[
R\otimes^{\mathbf L}_{\mathbb Z}S=R\otimes_{\mathbb Z}Q_J,
\]
a differential graded ring in degrees \(-1\) and \(0\), with the homomorphism \(R\to R\otimes_{\mathbb Z}Q_J\), \(r\mapsto r\otimes1\).

1. Up to isomorphism in \(D(\mathbf{Andg}(T))\) under \(R\), it does not depend on the presentation. In \(D(\mathbb Z)\) it is the derived tensor product of \(R\) and \(S\).
2. If \(R\) and \(S\) are commutative, it is isomorphic under \(R\), in \(D(\mathbf{Andg}(T))\), to the normalization of the derived tensor product \(R\otimes^\ell_{\mathbb Z}S\) of Proposition 5.2 of the lesson on derived tensor products.

The same construction applies with the presented ring on the left; by Proposition 2.6 of the lesson on differential graded modules, its derived category is defined up to equivalence.

**Proof.** (1) Let \(Q'\to S\) be a second presentation. The fibre product \(Q''=Q\times_SQ'\) is a ring with a surjection onto \(S\), and it is flat over \(\mathbb Z\), being a subsheaf of \(Q\oplus Q'\). The projections to \(Q\) and \(Q'\) induce homomorphisms of differential graded rings \(Q''_{J''}\to Q_J\) and \(Q''_{J''}\to Q'_{J'}\), which are quasi-isomorphisms because all three resolve \(S\). The three complexes are bounded complexes of flat sheaves, hence K-flat [Tag 06YQ], so \(R\otimes-\) preserves these quasi-isomorphisms (Lemma 2.2 of the lesson on differential graded modules), under \(R\). For the same reason \(R\otimes Q_J\) computes \(R\otimes^{\mathbf L}_{\mathbb Z}S\) in \(D(\mathbb Z)\).

(2) Let \(P=P^{\mathrm{alg}}(S)\to S\) be the resolution of Lemma 5.1 of the lesson on derived tensor products, over the constant ring \(\mathbb Z\): each \(P_n\) is a polynomial ring, flat over \(\mathbb Z\), and \(H_0P=S\), \(H_1P=0\). So \(P_0\to S\) is a presentation, and \(t_1(NP)=(N_1P/dN_2P\to P_0)\) is \(Q_J\) for \(Q=P_0\): the differential is injective because \(H_1P=0\), with image the kernel of \(P_0\to S\). The projection \(NP\to t_1(NP)\) is a homomorphism of differential graded rings and a quasi-isomorphism, both complexes resolving \(S\). Tensoring with \(R\), which commutes with normalization because \(R\) is constant, gives quasi-isomorphisms of differential graded rings \(N(R\otimes_{\mathbb Z}P)\to R\otimes t_1(NP)=R\otimes Q_J\) under \(R\). By Proposition 5.2 of the lesson on derived tensor products, \(R\otimes_{\mathbb Z}P\) is \(R\otimes^\ell_{\mathbb Z}S\). \(\square\)

A homomorphism \(\varphi\colon P\to P'\) of differential graded rings in nonpositive degrees, or more generally a morphism of \(D(\mathbf{Andg}(T))\), gives adjoint functors between \(D(P)\) and \(D(P')\), equivalences when \(\varphi\) is a quasi-isomorphism (Propositions 2.5 and 2.6 of the lesson on differential graded modules). This applies in particular to \(R\to R\otimes^{\mathbf L}_{\mathbb Z}S\).

## 2. The stable ring of a ring

**Construction 2.1.** Let \(A\) be a ring, and \(A(1)^\times\) its spectrum, an \(S_1\)-graded monoid of \(T\) (Definition 3.2 of the lesson on graded rings). Applying \(\mathbb Z(-)\) componentwise gives the \(S_1\)-graded ring \(\mathbb Z(A(1)^\times)\), with the multiplications \(\mathbb Z(A\langle m\rangle(p))\otimes\mathbb Z(A\langle n\rangle(p'))\to\) \(\mathbb Z(A\langle m+n\rangle(p,p'))\) induced by those of \(A(1)^\times\). Let
\[
Q_A=\mathbb Z\bigl(C_\bullet(A(1)^\times)\bigr)=C_\bullet\bigl(\mathbb Z(A(1)^\times)\bigr),
\]
a ring of type \(C_\bullet(S_1)\). By Propositions 2.1 and 2.2 of that lesson, \(Q_A^{\mathrm{red}}(-1)=C_\bullet(\mathbb Z(A(1)^\times)^{\mathrm{red}}(-1))\) is a ring of type \(C_\bullet(S_0)\). Put
\[
\mathbb Z^{\mathrm{st}}(A)=\Delta^2Q_A^{\mathrm{red}}(-1),
\]
a simplicial ring (Construction 2.1 of the lesson on diagonal rings).

By Lemma 2.2 of the lesson on diagonal rings, \(\mathbb Z^{\mathrm{st}}(A)=\Delta C_\bullet(\Delta X)\) with \(X=\mathbb Z(A(1)^\times)^{\mathrm{red}}(-1)\). The diagram \(\Delta X\) of \(\bar\Delta'\) is the diagram \(D_F(A)\) of Definition 3.2 of the lesson on stabilization for the functor \(F=\mathbb Z(-)\) and the constant simplicial abelian sheaf \(A\), and \(\Delta C_\bullet(D_F(A))\) is its stabilization \(F^{\mathrm{st}}(A)\). So the underlying simplicial abelian sheaf of \(\mathbb Z^{\mathrm{st}}(A)\) is the stabilization of \(\mathbb Z(-)\) at \(A\), whose homology is \(A\) in degree \(0\) and \(0\) in degree \(1\) (Example 2.1 (3) and (4) of the lesson on stable derived functors). For a simplicial ring \(A\), \(\mathbb Z^{\mathrm{st}}(A)\) is the diagonal of \(q\mapsto\mathbb Z^{\mathrm{st}}(A_q)\), again a simplicial ring.

**Proposition 2.2.**

1. The terms of \(\mathbb Z^{\mathrm{st}}(A)\) are direct sums of direct summands of abelian sheaves \(\mathbb Z(A^k)\); in particular they are flat. In degree \(0\),
\[
\begin{aligned}&\mathbb Z^{\mathrm{st}}(A)_0\\&\quad =\mathbb Z(A)\oplus I(A)\oplus I(A)\oplus\cdots,\end{aligned}
\]
the sum over \(k\geq0\) of the values at the ordinals \([k-1]\), where \(I(A)\) is the kernel of the augmentation \(\mathbb Z(A)\to\mathbb Z\), \([a]\mapsto1\). The summand of \([k-1]\) times that of \([l-1]\) lies in that of \([k+l-1]\), through the multiplication \([a][b]=[ab]\).
2. Let \(s\colon\mathbb Z(A)\to A\), \([a]\mapsto a\), a ring homomorphism. The stabilization of the natural transformation \(s\colon\mathbb Z(M)\to M\), followed by the canonical quasi-isomorphism \(\operatorname{id}^{\mathrm{st}}(A)\to A\) of Corollary 3.7 of the lesson on stabilization, is a homomorphism of simplicial rings
\[
\varepsilon\colon\mathbb Z^{\mathrm{st}}(A)\to A,
\]
the *augmentation*. In degree \(0\) it is \(s\) on every summand of (1). It induces an isomorphism \(H_0\mathbb Z^{\mathrm{st}}(A)\cong A\).

**Proof.** (1) The term of \(\Delta^2Q_A^{\mathrm{red}}(-1)\) in degree \(r\) is the sum, over the \(r\)-simplices \(\sigma\) of the nerve of \(\bar\Delta'\), of the values at \((r,\ldots,r)\) of \(\mathbb Z(A\langle k\rangle)^{\mathrm{red}}[-\mathbf 1]=\) \(\Gamma\bigl((N\mathbb Z(A\langle k\rangle))_{\geq\mathbf 1}[-\mathbf 1]\bigr)\), where \(k\) is the size of the first vertex of \(\sigma\). The terms of the normalization are direct summands of the values \(\mathbb Z(A\langle k\rangle(p))=\mathbb Z(A^{p_0\cdots p_{k-1}})\) (Theorem 1.1 of *The cotangent complex*), and \(\Gamma\) takes finite sums of them. In degree \(0\), the value for \(k=0\) is \(\mathbb Z(A)\), and for \(k\geq1\) it is the normalized part of \(\mathbb Z(A\langle k\rangle)\) in multidegree \(\mathbf 1\): the intersection of the kernels of the faces \(d_1\) in each coordinate, which go to \(\mathbb Z(A\langle k\rangle\text{ at a vertex})=\mathbb Z(\mathrm{pt})=\mathbb Z\). This is \(I(A)\). The multiplication is that of \(Q_A\), on the summands of \([k-1]\) and \([l-1]\) of \(N_0(\bar\Delta')\).

(2) The map \(s\colon\mathbb Z(A\langle n\rangle(p))\to A\langle n\rangle(p)\) is additive and, by the formula for the multiplication of spectra, multiplicative from the ring \(\mathbb Z(A(1)^\times)\) to the ring \(A(1)\) (Remark 3.3 of the lesson on graded rings). So it is a homomorphism of \(S_1\)-graded rings, and \(\Delta^2C_\bullet((-)^{\mathrm{red}}(-1))\) of it is a homomorphism of simplicial rings \(\mathbb Z^{\mathrm{st}}(A)\to\Delta^2C_\bullet(A(1)^{\mathrm{red}}(-1))\). Here \(A(1)^{\mathrm{red}}(-1)=cA\), the trivial \(S_0\)-graded ring, and \(\Delta^2C_\bullet(cA)\) is the simplicial ring \(A\otimes\mathbb Z(N(\bar\Delta'))\), the ring of the simplicial monoid \(N(\bar\Delta')\) under the sum of strings, with coefficients in \(A\) (Proposition 3.4 (2) of the lesson on diagonal rings). Its augmentation to \(A\), induced by \(\sigma\mapsto1\), is a homomorphism of simplicial rings. On underlying simplicial abelian sheaves this composite is the stabilization of \(s\) followed by the augmentation of the simplicial replacement of the constant diagram \(A\), which is the map of Corollary 3.7 of the lesson on stabilization. In degree \(0\) the composite is \(s\) on the summand of each ordinal. On \(H_0\) it is the isomorphism of Example 2.1 (3) of the lesson on stable derived functors. \(\square\)

**Remark 2.3.** The projection of \(\mathbb Z^{\mathrm{st}}(A)_0\) onto the summand \(\mathbb Z(A)\) of the empty ordinal, followed by \(s\), is a ring homomorphism, but it is not compatible with the faces. Let \(\delta\colon[-1]\to[0]\) be the \(1\)-simplex from the empty ordinal to \([0]\), and \(x=[1]\) in the summand of \(\delta\), with value \(\mathbb Z(A)\) constant in the simplicial direction. Then \(d_1x=[1]\) in the summand of \([-1]\), and \(d_0x\) is the image of \([1]\) under the structure map \(\mathbb Z(A)\to I(A)\), \([a]\mapsto[a]-[0]\), in the summand of \([0]\) (Lemma 3.4 of the lesson on stabilization). The projection followed by \(s\) gives \(1\) and \(0\), while \(\varepsilon\) gives \(1\) and \(1\). So the augmentation in degree \(0\) is \(s\) on all summands, not only on the first.

**Proposition 2.4.** Let \(A\) and \(B\) be rings.

1. \(t_1(N\mathbb Z^{\mathrm{st}}(A))\to A\), induced by \(\varepsilon\), is \(Q_J\) for the presentation \(\varepsilon_0\colon\mathbb Z^{\mathrm{st}}(A)_0\to A\) of Lemma 1.1.
2. Let \(B^{\mathrm{st}}(A)=\mathbb Z^{\mathrm{st}}(A)\otimes_{\mathbb Z}B\), a simplicial ring. There is an isomorphism, in \(D(\mathbf{Andg}(T))\) and under \(B\),
\[
A\otimes^{\mathbf L}_{\mathbb Z}B\cong t_1\bigl(NB^{\mathrm{st}}(A)\bigr),
\]
and so a homomorphism \(NB^{\mathrm{st}}(A)\to A\otimes^{\mathbf L}_{\mathbb Z}B\), the projection onto \(t_1\).
3. For every \(n\), restriction of scalars along this homomorphism induces an equivalence between the full subcategories of \(D(A\otimes^{\mathbf L}_{\mathbb Z}B)\) and of \(D(NB^{\mathrm{st}}(A))\) formed by the objects with cohomology in \([n,n+1]\).

**Proof.** (1) The term \(\mathbb Z^{\mathrm{st}}(A)_0=N_0\mathbb Z^{\mathrm{st}}(A)\) is flat, and \(\varepsilon_0\) is surjective because \(s\colon\mathbb Z(A)\to A\) is. Since \(H_1\mathbb Z^{\mathrm{st}}(A)=0\), the differential \(N_1/dN_2\to N_0\) is injective; its image is the kernel of \(\varepsilon_0\), because \(H_0(\varepsilon)\) is an isomorphism. The multiplication of \(t_1\) is that of \(Q_J\), since products of two terms of degree \(-1\) vanish in \(t_1\).

(2) By (1) and Proposition 1.2, \(A\otimes^{\mathbf L}_{\mathbb Z}B=t_1(N\mathbb Z^{\mathrm{st}}(A))\otimes_{\mathbb Z}B\). Tensoring with \(B\) is right exact, so it commutes with the quotient defining \(t_1\), and it commutes with normalization, which is the image of an idempotent made of faces and degeneracies. Hence this is \(t_1(N(\mathbb Z^{\mathrm{st}}(A)\otimes B))=t_1(NB^{\mathrm{st}}(A))\), as differential graded rings.

(3) This is Proposition 1.3 of the lesson on differential graded modules for \(n=1\), together with Proposition 2.6 there for the isomorphism of (2). \(\square\)

## 3. Modules and Mac Lane's theorem

**Construction 3.1.** Let \(M\) be an \(A\)-module. Its spectrum \(M(1)^\times\) is an \(S_1\)-graded \(A(1)^\times\)-object, so \(X_M=\mathbb Z(C_\bullet(M(1)^\times))=C_\bullet(\mathbb Z(M(1)^\times))\) is a \(Q_A\)-module of type \(C_\bullet(S_1)\), and
\[
\mathbb Z^{\mathrm{st}}(M)=\Delta^2X_M^{\mathrm{red}}(-1)
\]
is a \(\mathbb Z^{\mathrm{st}}(A)\)-module, whose underlying simplicial abelian sheaf is the stabilization of \(\mathbb Z(-)\) at \(M\), as in Construction 2.1. Its terms are direct sums of direct summands of sheaves \(\mathbb Z(M^k)\), hence flat. The stabilization of \(s\colon\mathbb Z(M)\to M\), followed by the quasi-isomorphism of Corollary 3.7 of the lesson on stabilization, is a map of modules
\[
\varepsilon_M\colon\mathbb Z^{\mathrm{st}}(M)\to M
\]
over \(\varepsilon\), by the argument of Proposition 2.2 (2). Everything is functorial in \(M\). For a simplicial ring \(A\) and a simplicial \(A\)-module \(M\), the same construction, applied in each degree and followed by the diagonal, makes \(\mathbb Z^{\mathrm{st}}(M)\) a \(\mathbb Z^{\mathrm{st}}(A)\)-module with an augmentation over \(\varepsilon\).

Let \(B_A=N\mathbb Z^{\mathrm{st}}(A)\), with the homomorphism \(\varepsilon\colon B_A\to A\) of differential graded rings, \(A\) being concentrated in degree \(0\). The map \(N\varepsilon_M\colon N\mathbb Z^{\mathrm{st}}(M)\to M\) is \(B_A\)-linear, \(M\) being a \(B_A\)-module through \(\varepsilon\). By the adjunction between extension and restriction of scalars along \(\varepsilon\) (Proposition 2.5 of the lesson on differential graded modules), it corresponds to a morphism
\[
c_M\colon A\otimes^{\mathbf L}_{B_A}N\mathbb Z^{\mathrm{st}}(M)\to M
\]
of \(D(A)\), the derived category of \(A\)-modules, natural in \(M\).

**Theorem 3.2 (Mac Lane).** For every \(A\)-module \(M\), \(c_M\) is an isomorphism.

**Proof.** Restriction of scalars from \(D(A)\) to \(D(\mathbb Z)\) detects isomorphisms, so it suffices to show that \(c_M\) is a quasi-isomorphism. Choose a quasi-isomorphism \(P'\to A\) of right \(B_A\)-modules from a K-flat module (Lemma 2.1 of the lesson on differential graded modules). For every left \(B_A\)-module \(N\), \(A\otimes^{\mathbf L}_{B_A}N\) is represented by \(P'\otimes_{B_A}N\) (Lemma 2.2 there), and \(c_M\) by the composite \(P'\otimes_{B_A}N\mathbb Z^{\mathrm{st}}(M)\to\) \(A\otimes_{B_A}N\mathbb Z^{\mathrm{st}}(M)\to\) \(M\).

*Step 1: \(M=A\).* Here \(\mathbb Z^{\mathrm{st}}(M)\) is \(\mathbb Z^{\mathrm{st}}(A)\) as a module over itself, \(A\otimes_{B_A}B_A=A\), and \(c_A\) is the identity of \(A\).

*Step 2: \(M=A^r\).* The inclusions of the summands induce a \(\mathbb Z^{\mathrm{st}}(A)\)-linear map \(\mathbb Z^{\mathrm{st}}(A)^{\oplus r}\to\mathbb Z^{\mathrm{st}}(A^r)\), compatible with the augmentations. It is a quasi-isomorphism by the additivity of stable derived functors (Proposition 1.4 of the lesson on stable derived functors), since \(\mathbb Z^{\mathrm{st}}\) is its own stable derived functor (Example 2.1 (1) there). So \(c_{A^r}\) is a quasi-isomorphism by Step 1.

*Step 3: local inductive limits.* Let \(M=\varinjlim_LM_i\) be the local inductive limit of a local system of modules, \(M_i\) being a module over \(T/U\) for \(i\in L(U)\). All constructions commute with restriction to \(T/U\). The functor \(\mathbb Z^{\mathrm{st}}\) commutes with local inductive limits (proof of Example 2.1 (4) of the lesson on stable derived functors), and so do normalization and \(P'\otimes_{B_A}-\). Local inductive limits are exact and commute with homology (Section 3 of the lesson on non-additive functors). So if every \(c_{M_i}\) is a quasi-isomorphism, so is \(c_M\).

*Step 4: \(M=A(X)\) for a sheaf of sets \(X\).* The abelian sheaf \(\mathbb Z(X)\) is flat, so by the theorem of Deligne and Lazard (Theorem 3.2 of the lesson on non-additive functors, for the ring \(\mathbb Z\)) it is the local inductive limit of a local system of finite free abelian sheaves \(\mathbb Z_U^{r}\). Tensoring with \(A\) commutes with local inductive limits, so \(A(X)=A\otimes\mathbb Z(X)\) is the local inductive limit of the modules \(A_U^r\). Steps 2 and 3, over each \(T/U\), give the claim.

*Step 5: general \(M\).* Let \(P\to M\) be the standard resolution of Construction 4.3 of the lesson on non-additive functors: a simplicial \(A\)-module with \(P_q=A(X_q)\) for sheaves of sets \(X_q\), whose augmentation to the constant simplicial module \(M\) is a quasi-isomorphism. Since \(\mathbb Z^{\mathrm{st}}\) carries quasi-isomorphisms to quasi-isomorphisms (Example 2.1 (1) of the lesson on stable derived functors), \(\mathbb Z^{\mathrm{st}}(P)\to\mathbb Z^{\mathrm{st}}(M)\) is a quasi-isomorphism of \(\mathbb Z^{\mathrm{st}}(A)\)-modules, and by naturality it suffices to show that \(c_P\colon P'\otimes_{B_A}N\mathbb Z^{\mathrm{st}}(P)\to NP\) is a quasi-isomorphism. Write \(\mathbb Z^{\mathrm{st}}(P)\) as the diagonal of the bisimplicial module \(W\) with \(W_{q,\bullet}=\mathbb Z^{\mathrm{st}}(P_q)\), on which \(\mathbb Z^{\mathrm{st}}(A)\) acts in the second index and is constant in the first. The shuffle map \(\operatorname{Tot}NW\to N\operatorname{diag}W\) is a quasi-isomorphism (Lemma 2.6 of the lesson on multisimplicial objects), and it is \(B_A\)-linear by Lemma 3.1 of the lesson on differential graded modules. Tensoring with the K-flat module \(P'\) preserves it. The complex \(P'\otimes_{B_A}\operatorname{Tot}NW\) is the total complex of the double complex with columns \(P'\otimes_{B_A}N\mathbb Z^{\mathrm{st}}(P_q)\), normalized in \(q\), and its map to \(\operatorname{Tot}\) of the columns \(P_q\), which is \(NP\), is given by the maps \(c_{P_q}\). These are quasi-isomorphisms by Step 4, so the map of total complexes is one, by the row filtration in \(q\). Composed with the shuffle map, it is \(c_P\), because the shuffle map of a bisimplicial object constant in one index is the identity on normalizations. \(\square\)

## 4. Bar resolutions and the Mac Lane resolution

**Proposition 4.1 (bar resolutions).** Let \(K\to R\) be a homomorphism of rings and \(X\) an \(R\)-module. Let \(\operatorname{Bar}(R/K,X)\) be the simplicial \(R\)-module with \(\operatorname{Bar}_n=R^{\otimes(n+1)}\otimes X\), tensor products over \(K\), with \(R\) acting on the first factor, faces
\[
\begin{aligned}&d_i(r_1\otimes\cdots\otimes r_{n+1}\otimes x)\\ &\quad =r_1\otimes\cdots\otimes r_{i+1}r_{i+2}\otimes\cdots\otimes x,\\ &d_n(r_1\otimes\cdots\otimes r_{n+1}\otimes x)\\ &\quad =r_1\otimes\cdots\otimes r_n\otimes r_{n+1}x,\end{aligned}
\]
for \(0\leq i<n\), degeneracies inserting \(1\) after \(r_{i+1}\), and augmentation \(\operatorname{Bar}_0=R\otimes X\to X\), \(r\otimes x\mapsto rx\).

1. The augmented simplicial object is \(K\)-linearly contractible: \(h(y)=1\otimes y\) satisfies \(d_0h=\mathrm{id}\) and \(d_{i+1}h=hd_i\), so its normalized complex, augmented to \(X\), is contractible over \(K\).
2. If \(R\) and \(X\) are flat over \(K\), then every \(\operatorname{Bar}_n\) is a flat \(R\)-module, and \(\operatorname{Bar}(R/K,X)\to X\) is a resolution of \(X\) by flat \(R\)-modules.

The same holds for a homomorphism of simplicial rings and a simplicial module, in each simplicial degree.

**Proof.** (1) The identities hold on generators: inserting \(1\) in front and then multiplying it into \(r_1\) gives back \(y\), and the other faces commute with inserting \(1\) in front, with an index shift. So \(\pm h\) is a contracting homotopy of the augmented complex \(\sum(-1)^id_i\), as for every augmented simplicial object with an extra degeneracy; its normalized complex is a direct summand, as a complex, and is contractible as well. (2) \(\operatorname{Bar}_n=R\otimes_KY\) with \(Y=R^{\otimes n}\otimes_KX\) flat over \(K\). For a right \(R\)-module \(N\), \(N\otimes_R(R\otimes_KY)=N\otimes_KY\), which is exact in \(N\). \(\square\)

The flatness of \(R\) over \(K\) cannot be omitted in (2) (Exercise 5.3).

**Theorem 4.2 (the Mac Lane resolution).** Let \(M\) be an \(A\)-module, \(R=\mathbb Z^{\mathrm{st}}(A)\) and \(\operatorname{Bar}=\operatorname{Bar}(R/\mathbb Z,\mathbb Z^{\mathrm{st}}(M))\), a bisimplicial \(R\)-module, \((n,r)\mapsto R_r^{\otimes(n+1)}\otimes\mathbb Z^{\mathrm{st}}(M)_r\). The map
\[
A\otimes_R\Delta\operatorname{Bar}\to M,
\]
given by the augmentation of the bar construction and \(a\otimes x\mapsto a\,\varepsilon_M(x)\), is a quasi-isomorphism of simplicial \(A\)-modules. Its term of degree \(n\) is
\[
A\otimes_{\mathbb Z}\mathbb Z^{\mathrm{st}}(A)_n^{\otimes n}\otimes_{\mathbb Z}\mathbb Z^{\mathrm{st}}(M)_n,
\]
a direct sum of direct summands of free modules \(A(A^p\times M^q)\).

**Proof.** The terms: \(A\otimes_R(R^{\otimes(n+1)}\otimes V)=A\otimes R^{\otimes n}\otimes V\), and by Proposition 2.2 (1) and Construction 3.1 these are sums of direct summands of \(A\otimes\mathbb Z(A^{k_1})\otimes\cdots\otimes\mathbb Z(M^l)=\) \(A(A^{k_1+\cdots}\times M^l)\).

For each \(r\), the row \(\operatorname{Bar}_{\bullet,r}\to\mathbb Z^{\mathrm{st}}(M)_r\) is a homotopy equivalence by Proposition 4.1 (1), so \(\Delta\operatorname{Bar}\to\mathbb Z^{\mathrm{st}}(M)\) is a quasi-isomorphism (Lemma 1.1 of the lesson on derived tensor products). With \(P'\to A\) as in the proof of Theorem 3.2, it follows that \(P'\otimes_{B_A}N\Delta\operatorname{Bar}\to P'\otimes_{B_A}N\mathbb Z^{\mathrm{st}}(M)\) is a quasi-isomorphism, and by Theorem 3.2 the latter maps quasi-isomorphically to \(M\). It remains to compare \(P'\otimes_{B_A}N\Delta\operatorname{Bar}\) with \(N(A\otimes_R\Delta\operatorname{Bar})\).

For fixed \(n\), the column \(\operatorname{Bar}_{n,\bullet}\) is the induced module \(R\otimes V_n\), with \(V_n=R^{\otimes n}\otimes\mathbb Z^{\mathrm{st}}(M)\), a simplicial abelian sheaf with flat terms, and its faces and degeneracies in the index \(r\) act on all factors. The shuffle map \(B_A\otimes NV_n\to N(R\otimes V_n)\) is a \(B_A\)-linear quasi-isomorphism, by the proof of Lemma 3.2 of the lesson on differential graded modules, which does not use commutativity. Tensoring with \(P'\) preserves it, and \(P'\otimes_{B_A}(B_A\otimes NV_n)=\) \(P'\otimes NV_n\to\) \(A\otimes NV_n\) is a quasi-isomorphism because \(NV_n\) is K-flat [Tag 06YQ]. Since \(A\) is constant, \(A\otimes NV_n=\) \(N(A\otimes V_n)=\) \(N(A\otimes_R\operatorname{Bar}_{n,\bullet})\). So the natural map \(P'\otimes_{B_A}N\operatorname{Bar}_{n,\bullet}\to N(A\otimes_R\operatorname{Bar}_{n,\bullet})\) is a quasi-isomorphism for each \(n\), compatibly with the faces in \(n\). By the row filtration in \(n\), the map of total complexes is a quasi-isomorphism. The shuffle maps from the total complexes to the normalized diagonals are quasi-isomorphisms (Lemma 2.6 of the lesson on multisimplicial objects), \(B_A\)-linear on the side of \(\Delta\operatorname{Bar}\) (Lemma 3.1 of the lesson on differential graded modules), and natural. So \(P'\otimes_{B_A}N\Delta\operatorname{Bar}\to N(A\otimes_R\Delta\operatorname{Bar})\) is a quasi-isomorphism, compatible with the maps to \(M\). \(\square\)

Since the terms are sums of direct summands of free modules on products \(A^p\times M^q\), Theorem 4.2 gives, functorially in \(M\), a resolution of \(M\) whose terms are built from the sheaves of sets underlying \(A\) and \(M\) alone. Computing \(\operatorname{Ext}\) groups of \(M\) with such a resolution expresses them through diagrams built from these products.

## 5. Exercises

**5.1.** Let \(A\) and \(M\) be as in Theorem 3.2. Show directly that \(H_0(A\otimes^{\mathbf L}_{B_A}N\mathbb Z^{\mathrm{st}}(M))\cong M\), using \(H_0\mathbb Z^{\mathrm{st}}(A)=A\) and \(H_0\mathbb Z^{\mathrm{st}}(M)=M\).

**5.2.** Let \(A=\mathbb F_2\) (in the topos of sets). List the summands of \(\mathbb Z^{\mathrm{st}}(A)_0\) of the ordinals \([-1]\) and \([0]\) with bases, and check by hand that \(\varepsilon\) is multiplicative on them and that the map of Remark 2.3 is not compatible with the faces.

**5.3.** Let \(p\) be a prime, \(K=\mathbb Z\), \(R=\mathbb Z[t]/(pt)\) and \(X=\mathbb Z\) (in the topos of sets). Show that \(X\) is flat over \(K\) but \(\operatorname{Bar}_1(R/K,X)\cong R\otimes_{\mathbb Z}R\) is not a flat \(R\)-module.

## 6. Complete solutions

**5.1.** The ring \(B_A\) lies in nonpositive degrees, and \(H^0B_A=A\). Let \(Q\to N\mathbb Z^{\mathrm{st}}(M)\) be a quasi-isomorphism from a K-flat module in nonpositive degrees (Lemma 2.1 of the lesson on differential graded modules), so that \(A\otimes^{\mathbf L}_{B_A}N\mathbb Z^{\mathrm{st}}(M)\) is \(A\otimes_{B_A}Q\). Since \(A\) and \(Q\) vanish in positive degrees, the term of degree \(0\) of \(A\otimes_{B_A}Q\) is \(A\otimes_{B^0_A}Q^0\), and \(H^0\) is its quotient by the image of \(A\otimes Q^{-1}\), that is, \(A\otimes_{B^0_A}H^0Q\). The ring \(B^0_A\) acts on \(H^0Q\) through its quotient \(H^0B_A=A\), so this is \(A\otimes_AH^0Q=H^0Q=H_0\mathbb Z^{\mathrm{st}}(M)=M\).

**5.2.** The summand of \([-1]\) is \(\mathbb Z(A)\) with basis \([0],[1]\), and that of \([0]\) is \(I(A)\) with basis \([1]-[0]\). The products: \([0][a]=[0]\), \([1][1]=[1]\), and in \(I(A)\), \(([1]-[0])([1]-[0])=[1]\) \(-[0]-[0]+[0]=[1]\) \(-[0]\), lying in the summand of \([1]\). The map \(\varepsilon\) sends \([0]\mapsto0\), \([1]\mapsto1\) and \([1]-[0]\mapsto1\), and these values multiply correctly. For Remark 2.3: \(d_1x=[1]\) in the summand of \([-1]\) and \(d_0x=[1]-[0]\) in the summand of \([0]\); the projection onto the first summand followed by \(s\) gives \(1\) and \(0\).

**5.3.** \(X=\mathbb Z\) is flat over \(\mathbb Z\). As an abelian group \(R=\mathbb Z\oplus\bigoplus_{k\geq1}(\mathbb Z/p)t^k\), so \(R\otimes_{\mathbb Z}R=R\oplus\bigoplus_{k\geq1}R/pR\) as left \(R\)-modules, and a direct summand of a flat module is flat. Here \(R/pR=\mathbb F_p[t]\). The annihilator of \(p\) in \(R\) is \(tR\), so \(pR\cong R/tR\), and \(pR\otimes_R\mathbb F_p[t]\cong\mathbb F_p[t]/t\mathbb F_p[t]=\mathbb F_p\). Its map to \(R\otimes_R\mathbb F_p[t]=\mathbb F_p[t]\), induced by the inclusion \(pR\to R\), sends the generator \(p\otimes1\) to \(p\cdot1=0\). So tensoring the injection \(pR\to R\) with \(\mathbb F_p[t]\) is not injective, and \(\mathbb F_p[t]\) is not flat over \(R\).

## Sources

The ring structure on the stable homology complex \(\mathbb Z^{\mathrm{st}}(A)\), the description of \(A\otimes^{\mathbf L}_{\mathbb Z}B\) through it and the comparison with modules are due to Illusie, in his work on the cotangent complex. The theorem that \(A\otimes^{\mathbf L}_{\mathbb Z^{\mathrm{st}}(A)}\mathbb Z^{\mathrm{st}}(M)\) is \(M\) goes back to Mac Lane's work on the homology of rings. Resolutions of modules by sums of free modules on products of copies of \(A\) and \(M\) were constructed by Breen and by Deligne, answering a question of Grothendieck; the bar construction used here is classical.
