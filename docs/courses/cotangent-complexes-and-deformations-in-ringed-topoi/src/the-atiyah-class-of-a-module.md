# The Atiyah class of a module

*Written by Claude Opus 5.5 (Anthropic) on 21 October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(A\to B\) be a map of rings of a topos and \(M\) a \(B\)-module. The *Atiyah class* of \(M\) is a morphism
\[
\operatorname{at}_{B/A}(M)\colon M\longrightarrow L_{B/A}\otimes^{\mathbf L}_BM[1]
\]
of the derived category of \(B\)-modules. It is built from modules of principal parts over the standard resolution \(P\) of \(B\): the exact sequence \(0\to\) \(\Omega_{P/A}\otimes_PM\to\) \(P^1_{P/A}(M)\to\) \(M\to\) \(0\) gives a triangle, and \(\Omega_{P/A}\otimes_PM\) is \(L_{B/A}\otimes_BM\). The lesson proves:

- the class is natural in \(M\) and in \(A\to B\), and it vanishes for modules extended from \(A\) by a flat module, for instance free modules;
- it is the boundary map of the degree-one part of the graded transitivity triangle of \(A\to B\to B\oplus M\), \(M\) in degree one (lesson [*Graded modules and the graded cotangent complex*](graded-modules-and-the-graded-cotangent-complex.md)); this is how the class enters the deformation theory of modules in [*Deformations of modules and of their morphisms*](deformations-of-modules-and-of-their-morphisms.md);
- its image in \(\operatorname{Ext}^1_B(M,\Omega_{B/A}\otimes_BM)\) is the class of the extension of principal parts of \(M\), whose splittings are the connections on \(M\) relative to \(A\). When \(L_{B/A}\to\Omega_{B/A}\) is a quasi-isomorphism onto a flat module, for instance for smooth morphisms of schemes, a flat \(M\) has \(\operatorname{at}_{B/A}(M)=0\) exactly when it has a connection. For a locally free module on a smooth scheme, this extension corresponds, with no sign, to the Atiyah sequence of its torsor of coframes.

**Prerequisites.** [*Graded modules and the graded cotangent complex*](graded-modules-and-the-graded-cotangent-complex.md) (Lemma 1.2, Proposition 2.2, Lemma 3.1, Theorems 3.3 and 3.4 and the proof of Theorem 3.4); [*Simplicial rings and modules in a topos*](simplicial-rings-and-modules-in-a-topos.md) (Theorem 4.2); [*Triangles and Ext groups of simplicial modules*](triangles-and-ext-groups-of-simplicial-modules.md) (Proposition 2.4, Lemma 3.2, Propositions 3.3 and 3.10); [*Derived tensor products of simplicial modules*](derived-tensor-products-of-simplicial-modules.md) (Lemma 2.1, Propositions 2.2, 3.2, 3.4, 4.2 and Corollary 4.3); [*Torsors, co-Lie complexes and the Atiyah class*](torsors-co-lie-complexes-and-the-atiyah-class.md) (Propositions 4.1 and 4.2 and the solution of Exercise 5.3), for Proposition 3.5; [*The cotangent complex*](course:AG-HP/the-cotangent-complex#4-the-fundamental-triangle) (Lemma 4.A). From the AI-integrated Stacks project: modules of principal parts [[Stacks, Tag 09CW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-sequence-of-principal-parts)]; the Atiyah class of a sheaf of modules [[Tag 09DI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-definition-atiyah-class-general)]; morphisms between objects in degree \(0\) [[Tag 06XS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-negative-exts)]; triangles of short exact sequences [[Tag 0152](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-derived-canonical-delta-functor)].

## Conventions

\(T\) is a topos and \(A\to B\) a map of rings of \(T\); \(P=P_A(B)\) is the standard resolution, a simplicial \(A\)-algebra augmented to \(B\) by a quasi-isomorphism, and \(L_{B/A}=\Omega_{P/A}\otimes_PB\), a simplicial \(B\)-module whose terms are free. For a simplicial ring \(R\), \(D_\bullet(R)\) is the derived category of simplicial \(R\)-modules (Theorem 4.2 of the lesson on simplicial rings and modules), with suspension \(\sigma\); for a ring \(\Lambda\), \(D_\bullet(\Lambda)\) is identified with \(D^{\leq0}(\Lambda)\) through normalization, \(\sigma\) becoming \([1]\) (Proposition 2.4 of the lesson on triangles). Since \(P\to B\) is a quasi-isomorphism of simplicial rings, \(B\otimes^\ell_P-\colon D_\bullet(P)\to D_\bullet(B)\) and restriction of scalars are inverse equivalences (Corollary 4.3 of the lesson on derived tensor products); we use them to regard triangles of \(D_\bullet(P)\) whose terms are \(B\)-modules as triangles of \(D_\bullet(B)\). Short exact sequences give distinguished triangles as in Lemma 3.2 of the lesson on triangles; for constant rings the third map induces the connecting homomorphisms (Proposition 3.10 there and [Tag 0152]).

## 1. Principal parts

**Definition 1.1.** Let \(R\to S\) be a map of rings of \(T\), \(J=\ker(S\otimes_RS\to S)\), and \(P^1_{S/R}=(S\otimes_RS)/J^2\). For an \(S\)-module \(N\), the module of *principal parts* is \(P^1_{S/R}(N)=P^1_{S/R}\otimes_SN\), the tensor product taken through the right factor \(s\mapsto1\otimes s\), with the \(S\)-module structure of the left factor. Equivalently \(P^1_{S/R}(N)=(S\otimes_RN)/J^2(S\otimes_RN)\). Write \(\mathrm d^1_N(n)=1\otimes n\), \(\pi_N((s\otimes s')\otimes n)=ss'n\), and \(\iota_N(\mathrm ds\otimes n)=(1\otimes s-s\otimes1)\otimes n\), where \(\mathrm ds\) is the class of \(1\otimes s-s\otimes1\) in \(J/J^2=\Omega_{S/R}\).

**Lemma 1.2.** In the situation of Definition 1.1:

1. The sequence of \(S\)-modules \(0\to\) \(\Omega_{S/R}\otimes_SN\xrightarrow{\iota_N}\) \(P^1_{S/R}(N)\xrightarrow{\pi_N}\) \(N\to\) \(0\) is exact. It is natural for commutative squares of rings \((R\to S)\to(R'\to S')\) and maps \(N\to N'\) that are \(S\)-linear for the \(S\)-module structure of \(N'\) through \(S\to S'\).
2. \(\mathrm d^1_N\) is \(R\)-linear, \(\pi_N\mathrm d^1_N=\mathrm{id}\), and \(\mathrm d^1_N(sn)=s\,\mathrm d^1_N(n)+\iota_N(\mathrm ds\otimes n)\).
3. For \(N=S\) the sequence splits: \(s\mapsto s\cdot\mathrm d^1_S(1)=s\otimes1\) is an \(S\)-linear section of \(\pi_S\). Hence it splits for every free \(S\)-module, and its formation commutes with \(-\otimes_{\mathbb Z}V\) for every abelian sheaf \(V\).

**Proof.** The sequence \(0\to J/J^2\to P^1_{S/R}\to S\to0\) is exact, and split as a sequence of right \(S\)-modules by \(s\mapsto1\otimes s\). So it stays exact after \(-\otimes_SN\) through the right factor; this is (1) [Tag 09CW], and naturality is clear from the formulas. (2) \((1\otimes s)\otimes n=\) \((s\otimes1)\otimes n+(1\otimes s-s\otimes1)\otimes n\). (3) \(\pi_S(s\otimes1)=s\), and \(s\mapsto s\otimes1\) is left \(S\)-linear. Principal parts commute with sums and with \(-\otimes_{\mathbb Z}V\), being a tensor product. \(\square\)

**Lemma 1.3 (principal parts and graded differentials).** Let \(R\to S\) be a map of rings and \(C\in S\text{-}\mathrm{Alggr}^+\), so that \(C^0=S\). The rule \((s\otimes s')\otimes m\mapsto s\,\mathrm d(s'm)\) defines a map
\[
\varphi_C\colon P^1_{S/R}(C^1)\longrightarrow k^1(\Omega_{C/R}),
\]
natural in \(C\). It is a morphism from the sequence of Lemma 1.2 (1) for \(N=C^1\) to the degree-one part of the sequence \(\Omega_{S/R}\otimes_SC\to\Omega_{C/R}\to\Omega_{C/S}\to0\) (Lemma 3.1 (2) of the lesson on graded modules), which induces the identity on \(\Omega_{S/R}\otimes_SC^1\) and, through \(k^1(\Omega_{C/S})\cong C^1\) (Lemma 3.1 (4) there), on \(C^1\). If \(C=S[Y]\) for some \(Y\in T^{\mathrm{gr}+}\), then \(\varphi_C\) is an isomorphism.

**Proof.** The map \(S\otimes_RC^1\to k^1(\Omega_{C/R})\), \(s\otimes m\mapsto s\,\mathrm dm\), is well defined because \(\mathrm d\) is \(R\)-linear. For \(a\in S\), \((a\otimes1-1\otimes a)(s\otimes m)=\) \(as\otimes m-s\otimes am\) goes to \(as\,\mathrm dm-s\,\mathrm d(am)=-sm\,\mathrm da\). Applying this twice, \((a\otimes1-1\otimes a)(b\otimes1-1\otimes b)(s\otimes m)\) goes to
\[
\begin{aligned}&\quad abs\,\mathrm dm -bs\,\mathrm d(am) -as\,\mathrm d(bm)\\ &\quad +s\,\mathrm d(abm)\\ &\quad =-bsm\,\mathrm da -asm\,\mathrm db\\ &\quad +asm\,\mathrm db +bsm\,\mathrm da =0,\end{aligned}
\]
so the map kills \(J^2(S\otimes_RC^1)\) and defines \(\varphi_C\). On \(\Omega_{S/R}\otimes C^1\): \(\iota(\mathrm da\otimes m)=(1\otimes a-a\otimes1)\otimes m\) goes to \(\mathrm d(am)-a\,\mathrm dm=m\,\mathrm da\), which is the image of \(\mathrm da\otimes m\) in \(k^1(\Omega_{C/R})\). On the quotients: \(s\,\mathrm dm\in k^1(\Omega_{C/R})\) goes to \(s\,\mathrm dm\in k^1(\Omega_{C/S})\), which corresponds to \(sm\in C^1\), and \(\pi((s\otimes1)\otimes m)=sm\). So \(\varphi_C\) is a morphism of sequences with the stated outer components. If \(C=S[Y]\), the degree-one part of the second sequence is exact on the left (Lemma 3.1 (2) there), and the five lemma shows that \(\varphi_C\) is an isomorphism. Naturality is clear. \(\square\)

## 2. The Atiyah class

**Construction 2.1.** Let \(M\) be a simplicial \(B\)-module; each \(M_n\) is a \(P_n\)-module through \(P_n\to B\). The modules \(P^1_{P_n/A}(M_n)\), with the maps induced by the faces and degeneracies of \(P\) and \(M\) (Lemma 1.2 (1)), form a simplicial \(P\)-module \(P^1_{P/A}(M)\), and Lemma 1.2 (1) gives an exact sequence of simplicial \(P\)-modules
\[
\begin{aligned}&0 \to\Omega_{P/A}\otimes_PM\\&\quad \to P^1_{P/A}(M) \to M \to0.\end{aligned} \tag{2.1}
\]
Its first term is \(L_{B/A}\otimes_BM\), because \(\Omega_{P_n/A}\otimes_{P_n}M_n=(\Omega_{P_n/A}\otimes_{P_n}B)\otimes_BM_n\); as \(L_{B/A}\) has free terms, this computes \(L_{B/A}\otimes^\ell_BM\) (Proposition 3.2 of the lesson on derived tensor products).

**Definition 2.2.** The *Atiyah class* of \(M\) relative to \(A\to B\) is the third map of the triangle of (2.1),
\[
\begin{aligned}&\operatorname{at}_{B/A}(M) \colon M\\&\quad \longrightarrow\sigma(L_{B/A}\otimes^\ell_BM)\quad\text{in }D_\bullet(B),\end{aligned}
\]
the first and third terms being \(B\)-modules and the morphism being taken in \(D_\bullet(B)\) through the equivalence of the conventions. For a \(B\)-module \(M\) it is a morphism \(M\to L_{B/A}\otimes^{\mathbf L}_BM[1]\) of \(D(B)\), that is, an element of \(\operatorname{Ext}^1_B(M,L_{B/A}\otimes^{\mathbf L}_BM)\). Write \(\operatorname{PP}_{B/A}(M)=B\otimes^\ell_PP^1_{P/A}(M)\) for the middle term in \(D_\bullet(B)\), so that
\[
\begin{aligned}&L_{B/A}\otimes^\ell_BM \to\operatorname{PP}_{B/A}(M)\\&\quad \to M\\&\quad \xrightarrow{\operatorname{at}_{B/A}(M)}\sigma(L_{B/A}\otimes^\ell_BM)\end{aligned} \tag{2.2}
\]
is distinguished. This is the Atiyah class of [Tag 09DI], formulated there with derived functors on the category of polynomial algebras; we do not use that formulation.

**Proposition 2.3.**

1. \(\operatorname{at}_{B/A}(M)\) is natural in \(M\): for a map \(f\colon M\to M'\) of simplicial \(B\)-modules, \(\operatorname{at}(M')\circ f=\sigma(1\otimes f)\circ\operatorname{at}(M)\). It is additive: \(\operatorname{at}(M\oplus M')=\operatorname{at}(M)\oplus\operatorname{at}(M')\).
2. Let \((A\to B)\to(A'\to B')\) be a commutative square of rings and \(f\colon M\to M'\) a \(B\)-linear map from a simplicial \(B\)-module to a simplicial \(B'\)-module. Then \(\operatorname{at}_{B'/A'}(M')\circ f=\) \(\sigma(c\otimes f)\circ\operatorname{at}_{B/A}(M)\) in \(D_\bullet(B)\), where \(c\colon L_{B/A}\to L_{B'/A'}\) is the functoriality map. In particular, for \(A\to A'\to B\), \(\operatorname{at}_{B/A'}(M)=\sigma(c\otimes1)\circ\operatorname{at}_{B/A}(M)\).
3. If \(N\) is a flat \(A\)-module and \(M=B\otimes_AN\), then \(\operatorname{at}_{B/A}(M)=0\). In particular the Atiyah class of a free \(B\)-module is zero.

**Proof.** (1) A map \(f\) induces a map of the sequences (2.1), hence a morphism of triangles (Lemma 3.2 (2) of the lesson on triangles). Sums of sequences give sums of triangles.

(2) The functoriality map \(P_A(B)\to P_{A'}(B')\) of standard resolutions, with \(f\), induces a map from the sequence (2.1) for \(M\) to the restriction of the sequence (2.1) for \(M'\) (Lemma 1.2 (1)), whose first component is \(c\otimes f\). It is a morphism of triangles of \(D_\bullet(P_A(B))\), restriction of scalars along \(P_A(B)\to P_{A'}(B')\) carrying distinguished triangles to distinguished triangles (Proposition 3.3 of the lesson on triangles).

(3) The map \(\tau\colon P\otimes_AN\to P^1_{P/A}(B\otimes_AN)\), \(p\otimes n\mapsto p\cdot\mathrm d^1(1\otimes n)\), is well defined because \(a\otimes1=1\otimes a\) in \(P^1_{P/A}\) for \(a\in A\), and it is \(P\)-linear and compatible with the simplicial structure. Its composite with \(\pi\) is the augmentation \(P\otimes_AN\to B\otimes_AN\), which is a quasi-isomorphism: \(N\) is flat over \(A\) and \(P\to B\) is a quasi-isomorphism of simplicial \(A\)-modules (Lemma 2.1 of the lesson on derived tensor products). So \(\pi\) has a section in \(D_\bullet(P)\), and the third map of the triangle is zero. For a free module \(B^{(Y)}=B\otimes_AA^{(Y)}\). \(\square\)

**Theorem 2.4 (the graded description).** Let \(M\) be a \(B\)-module and \(C=B\oplus M\) the algebra of dual numbers, a graded \(B\)-algebra with \(M\) in degree one. The degree-one part of the graded transitivity triangle of \(A\to B\to C\) (Theorem 3.4 of the lesson on graded modules), with its first term \(k^1(L_{B/A}\otimes^{\mathbf L}_BC)=L_{B/A}\otimes^{\mathbf L}_BM\) and its third term \(k^1(L^{\mathrm{gr}}_{C/B})\cong M\) (Theorem 3.3 (5) there), is isomorphic to the triangle (2.2) by an isomorphism of triangles that is the identity on the first and third terms. In particular \(\operatorname{at}_{B/A}(M)\) is the third map of the degree-one part of the graded transitivity triangle. The same holds with \(C\) replaced by any \(C\in B\text{-}\mathrm{Alggr}^+\) with \(C^1=M\).

**Proof.** Let \(R=P_A(C)^{\mathrm{gr}}\). By Proposition 2.2 (3) of the lesson on graded modules, \(k^0R=P_A(B)=P\), and \(R_n=P_n[X_n^{\geq1}]\) is a graded polynomial algebra over \(P_n\) on the generators of positive degree. Its degree-one part \(F=k^1R\) is a simplicial \(P\)-module with \(F_n=P_n^{(X_n^1)}\) free, and the degree-one part of the augmentation, \(\varepsilon\colon F\to M\), is a quasi-isomorphism (Proposition 2.2 (2) there).

Since \(B\) is concentrated in degree \(0\), \(P_A(B)^{\mathrm{gr}}=P\), and the functoriality map \(P\to R\) is the inclusion of \(k^0R\). The map \(B\to C\) is injective, so the graded transitivity triangle is, by the proof of Theorem 3.4 there, the triangle of the exact sequence
\[
\begin{gathered}0 \to\Omega_{P/A}\otimes_PC \to\Omega_{R/A}\otimes_RC\\ \to\Omega_{\overline R/B}\otimes_{\overline R}C \to0,\\ \overline R=R\otimes_PB,\end{gathered}
\]
whose third term is identified with \(L^{\mathrm{gr}}_{C/B}\) by maps compatible with the augmentations to \(\Omega_{C/B}\). We compute its degree-one part. For a graded \(R\)-module \(X\), \(k^1(X\otimes_RC)\) is generated by the \(x\otimes c\) with \(x\in X^0,c\in C^1\) or \(x\in X^1,c\in C^0\), subject to the relations of \(R^0=P\)-bilinearity and \(xr\otimes c=x\otimes rc\) for \(x\in X^0\), \(r\in R^1=F\), \(c\in C^0\): it is the pushout of \(X^1\otimes_PB\leftarrow\) \(X^0\otimes_PF\otimes_PB\to\) \(X^0\otimes_PM\), the maps being \(x\otimes r\otimes b\mapsto xr\otimes b\) and \(x\otimes r\otimes b\mapsto x\otimes b\varepsilon(r)\). For \(X=\Omega_{R/A}\) we have \(X^0=\Omega_{P/A}\) (Lemma 3.1 (3) there) and \(X^1\cong P^1_{P/A}(F)\) by Lemma 1.3, the map \(X^0\otimes F\to X^1\) being \(\iota_F\). Since \(F\) is free, the sequence of Lemma 1.2 (1) for \(F\) is split in each degree, hence stays exact after \(-\otimes_PB\). So the degree-one part of the exact sequence above is
\[
\begin{aligned}&0 \to\Omega_{P/A}\otimes_PM \to Y\\&\quad \to F\otimes_PB \to0,\end{aligned} \tag{2.3}
\]
where \(Y\) is the pushout of \(P^1_{P/A}(F)\otimes_PB\) along \(\Omega_{P/A}\otimes_PF\otimes_PB\to\Omega_{P/A}\otimes_PM\), and where \(F\otimes_PB=k^1(\Omega_{\overline R/B}\otimes C)\) because \(\overline R_n=B[X_n^{\geq1}]\). Its identification with \(M\) is \(x\otimes b\mapsto b\,\varepsilon(x)\): the variable \([m]\) of degree one goes to \(\mathrm dm\in\Omega_{C/B}\), and then to \(m\).

Consider the sequences of simplicial \(P\)-modules
\[
\begin{aligned}&\quad (a)\quad0 \to\Omega_{P/A}\otimes_PF\\ &\quad \to P^1_{P/A}(F) \to F \to0,\\ &\quad (b)\quad0 \to\Omega_{P/A}\otimes_PM\\ &\quad \to P^1_{P/A}(M) \to M \to0,\end{aligned}
\]
and (2.3). The map \(\varepsilon\) induces a map (a)\(\to\)(b) (Lemma 1.2 (1)), and the maps \(P^1_{P/A}(F)\to P^1_{P/A}(F)\otimes_PB\to Y\) and \(F\to F\otimes_PB\) give a map (a)\(\to\)(2.3); both have the same first component \(1\otimes\varepsilon\colon\Omega_{P/A}\otimes_PF\to\Omega_{P/A}\otimes_PM\). This component is a quasi-isomorphism, since \(\Omega_{P/A}\) has flat terms over \(P\) and \(\varepsilon\) is a quasi-isomorphism (Proposition 2.2 of the lesson on derived tensor products). The third components \(\varepsilon\) and \(F\to F\otimes_PB\) are quasi-isomorphisms, the latter by Lemma 4.A of *The cotangent complex*, \(F\) having free terms and \(P\to B\) being a quasi-isomorphism. By the five lemma both maps are quasi-isomorphisms, so they give isomorphisms of triangles in \(D_\bullet(P)\) (Lemma 3.2 (2) of the lesson on triangles). Composing the first inverse with the second gives an isomorphism from the triangle of (b), which is (2.2), to the triangle of (2.3), whose first component is the identity of \(\Omega_{P/A}\otimes_PM\) and whose third component is the composite \(M\xleftarrow{\varepsilon}F\to F\otimes_PB\to M\), the identity in \(D_\bullet(P)\) because \(F\to F\otimes_PB\to M\) is \(\varepsilon\). The triangle of (2.3) is a triangle of \(B\)-modules, and restriction of scalars is fully faithful, so the third maps agree in \(D_\bullet(B)\).

For another \(C'\in B\text{-}\mathrm{Alggr}^+\) with \(C'^1=M\), the quotient map \(C'\to C'/C'^{\geq2}=B\oplus M\) induces a morphism of graded transitivity triangles (Theorem 3.4 there), whose degree-one part is the identity on \(L_{B/A}\otimes^{\mathbf L}_BM\) and is compatible with the identifications of the third terms with \(M\), these being natural in \(C\) (Theorem 3.3 (5) there). So it is an isomorphism of triangles and the third maps agree. \(\square\)

## 3. Principal parts of the module and connections

**Corollary 3.1.** Let \(M\) be a simplicial \(B\)-module and \(\alpha\colon L_{B/A}\to\Omega_{B/A}\) the augmentation.

1. The composite \(\sigma(\alpha\otimes1)\circ\operatorname{at}_{B/A}(M)\colon\) \(M\to\) \(\sigma(\Omega_{B/A}\otimes^\ell_BM)\) is the third map of the triangle of the exact sequence \(0\to\) \(\Omega_{B/A}\otimes_BF\to\) \(P^1_{B/A}(F)\to\) \(F\to\) \(0\) of simplicial \(B\)-modules, for every quasi-isomorphism \(F\to M\) from a simplicial \(B\)-module with flat terms.
2. If \(M\) is a \(B\)-module, then the composite of \(\operatorname{at}_{B/A}(M)\) with \(L_{B/A}\otimes^{\mathbf L}_BM\to\Omega_{B/A}\otimes_BM\) (the augmentation, then \(H^0\)) is the class in \(\operatorname{Ext}^1_B(M,\Omega_{B/A}\otimes_BM)\) of the extension of principal parts \(0\to\) \(\Omega_{B/A}\otimes_BM\to\) \(P^1_{B/A}(M)\to\) \(M\to\) \(0\).

**Proof.** The augmentation \(P\to B\) and the identity of \(M\) induce a map from the sequence (2.1) to the sequence \(0\to\) \(\Omega_{B/A}\otimes_BM\to\) \(P^1_{B/A}(M)\to\) \(M\to\) \(0\), regarded as a sequence of \(P\)-modules; its first component is \(\alpha\otimes1\). So the third map of the second triangle is \(\sigma(\alpha\otimes1)\circ\operatorname{at}(M)\), which proves (2) and, for \(F\) in place of \(M\), the case of flat terms of (1), where \(\Omega_{B/A}\otimes_BF\) computes \(\Omega_{B/A}\otimes^\ell_BM\). By Proposition 2.3 (1), \(\operatorname{at}(M)\) and \(\operatorname{at}(F)\) correspond under the isomorphism \(F\to M\). \(\square\)

**Proposition 3.2 (connections).** Let \(M\) be a \(B\)-module. An \(A\)-linear map \(\nabla\colon M\to\Omega_{B/A}\otimes_BM\) is a *connection* if \(\nabla(bm)=b\nabla(m)+\mathrm db\otimes m\). The rule \(\nabla\mapsto s_\nabla=\mathrm d^1_M-\iota_M\circ\nabla\) is a bijection from the connections on \(M\) to the \(B\)-linear sections of \(\pi_M\colon P^1_{B/A}(M)\to M\). Consequently \(M\) admits a connection exactly when the extension of principal parts of \(M\) splits. If \(M\) is locally a direct summand of a finite free module, connections exist locally and the local connections form a torsor under \(\mathcal Hom_B(M,\Omega_{B/A}\otimes_BM)\); \(M\) has a global connection exactly when this torsor is trivial.

**Proof.** By Lemma 1.2 (2), \(s_\nabla(bm)=\) \(b\,\mathrm d^1(m)+\) \(\iota(\mathrm db\otimes m)-\) \(\iota(b\nabla m+\mathrm db\otimes m)=\) \(b\,s_\nabla(m)\), and \(\pi s_\nabla=\pi\mathrm d^1=\mathrm{id}\) since \(\pi\iota=0\). Conversely, for a \(B\)-linear section \(s\), \(\mathrm d^1-s\) takes values in \(\ker\pi=\iota(\Omega\otimes M)\), and \(\nabla=\iota^{-1}(\mathrm d^1-s)\) satisfies \(\nabla(bm)=\) \(\iota^{-1}(b\,\mathrm d^1m+\iota(\mathrm db\otimes m)-b\,s(m))=\) \(b\nabla m+\mathrm db\otimes m\). The two rules are inverse. Two connections differ by a \(B\)-linear map \(M\to\Omega\otimes M\), and every such map can be added. For \(M\) locally a direct summand of a finite free module, connections exist locally: on a free module \(\nabla(\sum b_ie_i)=\sum\mathrm db_i\otimes e_i\), and a direct summand \(M\subseteq B^n\) with projection \(q\) inherits \((1\otimes q)\circ\nabla|_M\). So the local connections form a torsor, which is trivial exactly when a global connection exists. \(\square\)

**Corollary 3.3.** Suppose that \(\alpha\colon L_{B/A}\to\Omega_{B/A}\) is a quasi-isomorphism and \(\Omega_{B/A}\) is flat over \(B\) (for instance, \(B\) is a polynomial algebra over \(A\), or \(A\to B\) is induced by a smooth morphism of schemes). Then for every \(B\)-module \(M\) the Atiyah class \(\operatorname{at}_{B/A}(M)\in\operatorname{Ext}^1_B(M,\Omega_{B/A}\otimes^{\mathbf L}_BM)\) is the class of the principal parts extension of a flat resolution of \(M\), and if \(M\) is flat, \(\operatorname{at}_{B/A}(M)=0\) if and only if \(M\) admits a connection relative to \(A\).

**Proof.** By hypothesis \(\sigma(\alpha\otimes1)\) is an isomorphism, so Corollary 3.1 (1) determines \(\operatorname{at}(M)\). If \(M\) is flat, take \(F=M\): \(\Omega\otimes^{\mathbf L}M=\Omega\otimes M\) and the class is that of the principal parts extension of \(M\); an extension of modules has zero class exactly when it splits, which by Proposition 3.2 is the existence of a connection. \(\square\)

**Remark 3.4.** For a morphism of schemes \(f\colon Y\to S\), \(A=f^{-1}\mathcal O_S\to B=\mathcal O_Y\) on the Zariski site and \(M\) a locally free module of finite rank, Corollary 3.1 (2) and Proposition 3.2 show that the image of \(\operatorname{at}_{Y/S}(M)\) in \(\operatorname{Ext}^1_{\mathcal O_Y}(M,\Omega_{Y/S}\otimes M)\) vanishes exactly when \(M\) has a connection relative to \(S\); this image is the classical Atiyah class of a vector bundle.

**Proposition 3.5 (the torsor of coframes).** Let \(Y\to S\) be a smooth morphism of schemes, \(M\) a locally free \(\mathcal O_Y\)-module of rank \(n\), and \(f\colon X\to Y\) the torsor of coframes, \(X=\mathcal Isom(M,\mathcal O_Y^n)\) under \(\mathrm{GL}_n\) acting by \(A\cdot\varphi=A\circ\varphi\). For a basis \(e=(e_1,\dots,e_n)\) of \(M\) over an open \(V\), with dual basis \(e^\vee\), let \(s_e\in X(V)\) be the coframe with \(s_e(e_k)=\varepsilon_k\), the standard basis. Let \(x=(x_{kl})\) be the coordinates of \(\mathrm{GL}_n\), \(\omega_{\mathrm{GL}_n}\) its co-Lie module, and \(\tau_s\) the isomorphisms of Proposition 4.1 (2) of the lesson on torsors.

1. There is a unique isomorphism \(\nu\colon\ell_{X/Y}\to M\otimes M^\vee\) with \(\nu(\tau_{s_e}^{-1}(dx_{kl}))=e_l\otimes e^\vee_k\) for every local basis \(e\).
2. Let \(\mathrm{ev}\colon\Omega_{Y/S}\otimes M\otimes M^\vee\to\Omega_{Y/S}\) be the evaluation \(\omega\otimes m\otimes\phi\mapsto\phi(m)\,\omega\). The Atiyah sequence (4.2) of the lesson on torsors is isomorphic, by the identity of \(\Omega_{Y/S}\) and \(\nu\), to the push-out along \(\mathrm{ev}\) of the principal parts extension of \(M\) tensored with \(M^\vee\).
3. Consequently, with \(a_M\in\operatorname{Ext}^1(M,\Omega_{Y/S}\otimes M)\) the class of the principal parts extension (Corollary 3.1 (2)),
\[
\begin{aligned}&\mathrm{at}(X/Y/S)\\&\quad=\mathrm{ev}[1]\circ(a_M\otimes1_{M^\vee})\circ\nu.\end{aligned}
\]

Through \(M\otimes M^\vee=\mathcal End(M)\), \(m\otimes\phi\mapsto\phi(-)\,m\), the isomorphism \(\nu\) identifies \(\ell_{X/Y}\) with \(\mathcal End(M)\), and the pairing \((A,m\otimes\phi)\mapsto\phi(Am)\) is the trace form. So the class of the Atiyah sequence of the coframe torsor and the class of the principal parts extension of \(M\) correspond, with no sign, under the operations of (3).

**Proof.** (1) Let \(e'=eg\) be another basis over \(V\), \(e'_l=\sum_ke_kg_{kl}\). The coordinates of a section of \(M\) in the two bases satisfy \(s_e=g\cdot s_{e'}\), so by Proposition 4.1 (3) of the lesson on torsors \(\tau_{s_e}=c(\operatorname{int}(g^{-1}))\circ\tau_{s_{e'}}\). The automorphism \(h\mapsto g^{-1}hg\) carries the matrix \(dx\) to \(g^{-1}dx\,g\). Write \(\Xi\) and \(\Xi'\) for the matrices with entries \(\tau_{s_e}^{-1}(dx_{kl})\) and \(\tau_{s_{e'}}^{-1}(dx_{kl})\). Then \(\Xi'=g^{-1}\Xi g\), entrywise. The dual bases satisfy \(e'^\vee_k=\sum_p(g^{-1})_{kp}e^\vee_p\), so the matrices \(N\) and \(N'\) with entries \(e_l\otimes e^\vee_k\) and \(e'_l\otimes e'^\vee_k\) satisfy \(N'=g^{-1}Ng\) as well. Hence the local isomorphisms \(\Xi\mapsto N\) agree on overlaps and glue.

(2) Over \(V\), let \(h\colon X_V\to\mathrm{GL}_n\), \(\varphi\mapsto\varphi(e)\), be the matrix whose column \(l\) is \(\varphi(e_l)\). Then \(h(A\cdot\varphi)=A\,h(\varphi)\), so the entries of \(\theta=h^{-1}dh\) are invariant forms, that is, sections of \(\omega^1_{X/S}\) over \(V\) (as in the solution of Exercise 5.3 of the lesson on torsors). The isomorphism \(\psi_{s_e}\) carries \(h\) to the coordinate \(x\), and \(x^{-1}dx\) restricts to \(dx\) at the unit, so the image of \(\theta\) in \(\ell_{X/Y}\) is \(\Xi\). Thus \(\sigma_e(\Xi)=\theta\) defines a splitting \(\sigma_e\) of (4.2) over \(V\). For \(e'=eg\), \(h'=hg\), so \(\theta'=g^{-1}\theta g+g^{-1}dg\). By (1), \(\sigma_e(\Xi')=g^{-1}\theta g=\theta'-g^{-1}dg\), hence
\[
(\sigma_e-\sigma_{e'})(\Xi')=-g^{-1}dg.
\]
On the other side, the connection \(\nabla_e\) with \(\nabla_e(e_k)=0\) gives the splitting \(s_e=\mathrm d^1-\iota\nabla_e\) of the principal parts extension (Proposition 3.2), and \(\sigma'_e=\mathrm{ev}_*(s_e\otimes1)\) splits its push-out. Since \(e_k=\sum_me'_m(g^{-1})_{mk}\), \(\nabla_e(e'_l)=\sum_kdg_{kl}\otimes e_k=\) \(\sum_m(g^{-1}dg)_{ml}\otimes e'_m\), while \(\nabla_{e'}(e'_l)=0\). So
\[
\begin{aligned}&(\sigma'_e-\sigma'_{e'})(e'_l\otimes e'^\vee_k)\\&\quad=-\mathrm{ev}\bigl(\textstyle\sum_m(g^{-1}dg)_{ml}\otimes e'_m\otimes e'^\vee_k\bigr)\\&\quad=-(g^{-1}dg)_{kl},\end{aligned}
\]
that is, \(\sigma_e-\sigma_{e'}=(\sigma'_e-\sigma'_{e'})\circ\nu\). Let \(\Phi_e\) be the isomorphism of extensions over \(V\) that is the identity on \(\Omega_{Y/S}\) and sends \(\sigma_e(\xi)\) to \(\sigma'_e(\nu\xi)\). On an overlap, \(\Phi_e(\sigma_{e'}(\xi))=\) \(\sigma'_e(\nu\xi)-(\sigma_e-\sigma_{e'})(\xi)=\) \(\sigma'_{e'}(\nu\xi)\), so \(\Phi_e=\Phi_{e'}\), and the \(\Phi_e\) glue.

(3) A morphism of short exact sequences gives a morphism of triangles [Tag 0152]. By Proposition 4.2 (2) of the lesson on torsors, \(\mathrm{at}(X/Y/S)\) is the third map of the triangle of (4.2), so by (2) it is \(\delta\circ\nu\), with \(\delta\) the third map of the triangle of the push-out. The morphism from the tensored extension to its push-out, with first component \(\mathrm{ev}\), gives \(\delta=\mathrm{ev}[1]\circ\delta'\), where \(\delta'\) is the third map for the tensored extension. Tensoring with the locally free module \(M^\vee\) is exact and commutes with cones, so \(\delta'=a_M\otimes1_{M^\vee}\). \(\square\)

## 4. Exercises

**Exercise 4.1.** Let \(k\) be a ring of \(T\), \(B=k[x]/(x^2)\), \(A=k\), and \(M=B/xB=k\). Show that \(M\) has no connection relative to \(k\), so that the image of \(\operatorname{at}_{B/k}(k)\) in \(\operatorname{Ext}^1_B(k,\Omega_{B/k}\otimes_Bk)\) is nonzero.

**Exercise 4.2.** Let \(M=B^n\) be free. Show that the connections on \(M\) are the maps \(\nabla(\sum b_ie_i)=\) \(\sum_i\mathrm db_i\otimes e_i+\sum_{i,j}b_i\,\omega_{ji}\otimes e_j\) for a matrix \((\omega_{ij})\) of global sections of \(\Omega_{B/A}\), and that a change of basis \(e'=eg\), \(g\in\mathrm{GL}_n(\Gamma(T,B))\), changes the matrix of a given connection into \(g^{-1}\omega g+g^{-1}\mathrm dg\).

**Exercise 4.3.** Let \(A\to B\) be a map of rings and \(M\) a \(B\)-module. Show that \(\operatorname{at}_{B/B}(M)=0\), and deduce from Proposition 2.3 (2) that \(\operatorname{at}_{B/A}(M)\) maps to zero under \(L_{B/A}\to L_{B/B}\). Why is this not a contradiction with Exercise 4.1?

## 5. Complete solutions

**Solution 4.1.** Here \(\Omega_{B/k}=B\,\mathrm dx/(2x\,\mathrm dx)\), so \(\Omega_{B/k}\otimes_Bk=k\,\mathrm dx\) is free of rank one: the relation \(2x\,\mathrm dx\) becomes \(0\) after \(x\mapsto0\). Suppose \(\nabla\) were a connection on \(k=B/xB\). For a local section \(m\) of \(k\), \(xm=0\), so \(0=\) \(\nabla(xm)=\) \(x\nabla(m)+\mathrm dx\otimes m=\) \(\mathrm dx\otimes m\), because \(x\) acts by zero on \(\Omega\otimes k\). Taking \(m=1\) gives \(\mathrm dx=0\) in \(k\,\mathrm dx\), a contradiction (unless \(k=0\)). By Proposition 3.2 the principal parts extension of \(k\) does not split, so its class is nonzero; by Corollary 3.1 (2) it is the image of \(\operatorname{at}_{B/k}(k)\).

**Solution 4.2.** For a connection \(\nabla\), write \(\nabla(e_i)=\sum_j\omega_{ji}\otimes e_j\); the Leibniz rule gives the formula, and conversely the formula defines a connection. If \(e'_i=\sum_je_jg_{ji}\), then \(\nabla(e'_i)=\sum_j\mathrm dg_{ji}\otimes e_j+\sum_jg_{ji}\nabla(e_j)\); writing \(e=e'g^{-1}\), the matrix of \(\nabla\) in the basis \(e'\) is \(g^{-1}\mathrm dg+g^{-1}\omega g\).

**Solution 4.3.** \(B\) is the polynomial algebra over \(B\) on no variables, so \(L_{B/B}\simeq\Omega_{B/B}=0\) by Theorem 3.3 (3) of the lesson on graded modules (with everything in degree \(0\)). So \(\operatorname{at}_{B/B}(M)\) is a map into \(0\), and Proposition 2.3 (2) for \(B\to B\) gives that the image of \(\operatorname{at}_{B/A}(M)\) in \(\sigma(L_{B/B}\otimes M)=0\) is zero. In Exercise 4.1 the class is nonzero in \(\operatorname{Ext}^1(M,\Omega_{B/k}\otimes M)\), relative to \(k\); relative to \(B\) there is nothing to obstruct: every module has the zero connection with values in \(\Omega_{B/B}=0\).

## Sources

The Atiyah class of a vector bundle, as the obstruction to the existence of a holomorphic connection, is due to Atiyah. Its definition for modules over a map of ringed topoi through the cotangent complex, its description through the graded cotangent complex of the dual numbers, and its comparison with the principal parts extension are due to Illusie, in his work on the cotangent complex. The Atiyah sequence of the bundle of frames, and its relation with connections on the vector bundle, are due to Atiyah, in his work on complex analytic connections in fibre bundles. The AI-integrated Stacks project, Chapter *The Cotangent Complex*, defines the Atiyah class of a sheaf of modules through principal parts over the standard resolution. Modules of principal parts are due to Grothendieck.
