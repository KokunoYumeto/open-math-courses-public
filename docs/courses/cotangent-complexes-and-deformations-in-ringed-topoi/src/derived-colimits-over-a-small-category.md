# Derived colimits over a small category

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A diagram \(X\colon I\to\mathcal A\) in an abelian category has a colimit, but the colimit functor is only right exact. Its left derived functor is computed by an explicit complex, the simplicial replacement of the diagram, whose \(n\)-th term is the sum of the values of \(X\) at the sources of the strings of \(n\) composable arrows of \(I\). This lesson constructs the derived colimit on bounded-above complexes, identifies it with the simplicial replacement, and proves its adjunction with the constant diagram. It then applies Deligne's contractibility theorem: over the category of finite ordinals and injective maps, a diagram that is eventually locally constant has no higher derived colimits, and its colimit is its value at any stage from which it is locally constant.

**Prerequisites.** [*Strict simplicial objects and Deligne's contractibility theorem*](strict-simplicial-objects-and-deligne-s-contractibility-theorem.md); left derived functors on bounded-above derived categories [[Stacks, Tag 05T7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-subcategory-left-resolution), [Tag 05T9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-subcategory-left-acyclics), [Tag 05TA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-proposition-enough-acyclics)] and their adjunctions [[Stacks, Tag 0DVC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-pre-derived-adjoint-functors)].

Throughout, \(\mathcal A\) is an abelian category with all small colimits in which filtered colimits are exact (Grothendieck's axiom AB5). Examples are the categories of modules over a ring and of sheaves of modules on a ringed topos. In particular direct sums are exact, and the cohomology of a complex commutes with filtered colimits of complexes.

## 1. Diagrams and their simplicial replacement

Let \(I\) be a small category. The functors \(I\to\mathcal A\) form an abelian category \(\mathcal A^I\), in which kernels, cokernels, sums and filtered colimits are computed objectwise. The constant-diagram functor \(c\colon\mathcal A\to\mathcal A^I\) is exact, and the colimit \(\varinjlim_I\colon\mathcal A^I\to\mathcal A\) is its left adjoint. It is right exact.

**Induced diagrams.** Let \(\omega_*\colon\mathcal A^I\to\mathcal A^{\operatorname{Ob}I}\) forget the arrows. It has the left adjoint
\[
\omega^*(Y)(i)=\bigoplus_{a\colon j\to i}Y_j,\qquad Y=(Y_j)_{j\in\operatorname{Ob}I},
\]
where an arrow \(b\colon i\to i'\) sends the summand of \(a\) to the summand of \(ba\). By the Yoneda lemma, a morphism \(\omega^*(Y)\to X\) is the same as a family of morphisms \(Y_j\to X(j)\). Diagrams isomorphic to some \(\omega^*(Y)\) are called *induced*. The counit \(\omega^*\omega_*X\to X\) is surjective, since the summand of \(a=\mathrm{id}_i\) maps identically onto \(X(i)\). The composite of left adjoints \(\varinjlim_I\circ\,\omega^*\) is left adjoint to \(\omega_*\circ c\), so \(\varinjlim_I\omega^*(Y)=\bigoplus_jY_j\).

**The simplicial replacement.** For \(X\in\mathcal A^I\) and \(n\geq0\), put
\[
C_n(X)=\bigoplus_{\sigma=(i_0\to i_1\to\cdots\to i_n)}X(i_0),
\]
the sum over the \(n\)-simplices \(\sigma\) of the nerve \(N(I)\). The face \(d_0\) maps the summand of \(\sigma\) to that of \(d_0\sigma\) by \(X(i_0\to i_1)\). The faces \(d_k\), \(k\geq1\), and the degeneracies map it identically to the summand of the corresponding face or degeneracy of \(\sigma\). This defines a simplicial object \(C_\bullet(X)\) of \(\mathcal A\), functorial and exact in \(X\), since sums and evaluations are exact. The cokernel of \(d_0-d_1\colon C_1(X)\to C_0(X)\) is the usual presentation of the colimit. So the augmentation \(C_0(X)\to\varinjlim_IX\) identifies \(H_0\) of the chain complex \(sC_\bullet(X)\) with \(\varinjlim_IX\).

Since \(\varinjlim_I\omega^*=\bigoplus\), the object \(C_n(X)\) is also \(\varinjlim_I\omega^*(Y^{(n)})\), where \(Y^{(n)}_j=\bigoplus_{i_0\to\cdots\to i_{n-1}\to j}X(i_0)\).

**Lemma 1.1.** For every \(Y\in\mathcal A^{\operatorname{Ob}I}\), the augmented complex \(sC_\bullet(\omega^*Y)\to\bigoplus_jY_j\) is contractible.

**Proof.** The summands of \(C_n(\omega^*Y)\) are indexed by strings \(j\xrightarrow{a}i_0\to\cdots\to i_n\) and the summand \(Y_j\). Such a string is an \(n\)-simplex of the nerve of the category \(j/I\) of arrows out of \(j\), and the faces and degeneracies of \(C_\bullet(\omega^*Y)\) are those of \(N(j/I)\). The face \(d_0\) composes \(a\) with the first arrow. So \(sC_\bullet(\omega^*Y)\), with its augmentation, is the direct sum over \(j\) of \(Y_j\otimes\bigl(s\mathbb Z(N(j/I))\to\mathbb Z\bigr)\). Here \(Y\otimes\mathbb Z(S)\) denotes the sum of copies of \(Y\) indexed by the set \(S\), and integer matrices act on it in the evident way. The category \(j/I\) has the initial object \(\mathrm{id}_j\), so the augmented complex \(s\mathbb Z(N(j/I))\to\mathbb Z\) is contractible (Lemma 2.2 of the lesson on strict simplicial objects). Tensoring with \(Y_j\) and summing preserves contractibility. \(\square\)

## 2. The derived colimit

Call \(X\in\mathcal A^I\) *colimit-acyclic* if \(H_n(sC_\bullet(X))=0\) for all \(n>0\). Induced diagrams are colimit-acyclic, by Lemma 1.1.

For a complex \(X\) of \(\mathcal A^I\), written cohomologically, let \(L(X)\) be the total complex of the double complex \(C_p(X^q)\). Its horizontal differential is \(\sum_i(-1)^id_i\colon C_p\to C_{p-1}\), and its vertical differential is induced by \(X\). The total degree of \(C_p(X^q)\) is \(q-p\), and the total complex is formed with direct sums. The augmentations \(C_0(X^q)\to\varinjlim_IX^q\) define a morphism of complexes \(\varepsilon\colon L(X)\to\varinjlim_IX\), where the colimit is taken termwise.

**Lemma 2.1.** If \(X\) is acyclic, so is \(L(X)\). Hence \(L\) takes quasi-isomorphisms to quasi-isomorphisms.

**Proof.** For each \(p\), the column \(C_p(X^\bullet)\) is acyclic, because \(C_p\) is a sum of evaluation functors. Let \(F_P\subseteq L(X)\) be the sum of the columns \(p\leq P\). It is a subcomplex, because the horizontal differential lowers \(p\). By induction on \(P\), each \(F_P\) is an iterated extension of shifted acyclic columns, hence acyclic. Every element of \(L(X)\) is a finite sum of components, so \(L(X)=\bigcup_PF_P\) is a filtered union, and it is acyclic by AB5. For the second assertion, apply the first to the cone of a quasi-isomorphism, using that \(L\) commutes with cones. \(\square\)

**Lemma 2.2.** If \(X\) is a bounded-above complex of colimit-acyclic diagrams, then \(\varepsilon\colon L(X)\to\varinjlim_IX\) is a quasi-isomorphism.

**Proof.** Up to a shift, the cone of \(\varepsilon\) is the total complex of the double complex obtained by adding the column \(\varinjlim_IX^q\) in position \(p=-1\). Its row \(q\) is the augmented complex \(sC_\bullet(X^q)\to\varinjlim_IX^q\), which is acyclic because \(X^q\) is colimit-acyclic. Let \(X^q=0\) for \(q>Q\). The sum \(G_k\) of the rows \(q\geq Q-k\) is a subcomplex, because the vertical differential raises \(q\). Each \(G_k\) is acyclic, by induction on \(k\). The total complex is the filtered union of the \(G_k\), so it is acyclic by AB5. \(\square\)

**Theorem 2.3.** The colimit functor has a left derived functor
\[
L\varinjlim_I\colon D^-(\mathcal A^I)\longrightarrow D^-(\mathcal A),
\]
which is exact. Every bounded-above complex of colimit-acyclic diagrams computes it, in particular every bounded-above complex of induced diagrams. For every \(X\in D^-(\mathcal A^I)\) there is a canonical isomorphism \(L\varinjlim_IX\cong L(X)\). The functor \(L\varinjlim_I\) takes \(D^{\leq m}(\mathcal A^I)\) into \(D^{\leq m}(\mathcal A)\).

**Proof.** Let \(\mathcal P\) be the class of colimit-acyclic diagrams. Every diagram is a quotient of an induced diagram, which lies in \(\mathcal P\). Let \(0\to P\to Q\to R\to0\) be exact with \(Q,R\in\mathcal P\). Since \(C_\bullet\) is exact, the long exact homology sequence of \(sC_\bullet\) shows that \(H_n(sC_\bullet(P))=0\) for \(n\geq2\). It also gives an exact sequence
\[
\begin{gathered}0=H_1(sC_\bullet(R))\to\varinjlim_IP\\\to\varinjlim_IQ\to\varinjlim_IR\to0\end{gathered}
\]
together with \(H_1(sC_\bullet(P))=0\), the latter because \(H_2(sC_\bullet(R))=0=H_1(sC_\bullet(Q))\). So \(P\in\mathcal P\), and the colimit is exact on the sequence. By [Stacks, Tag 05T9], every object of \(\mathcal P\) is acyclic for \(L\varinjlim_I\). By [Stacks, Tag 05TA], \(L\varinjlim_I\) is defined on \(D^-(\mathcal A^I)\), is exact, and is computed by bounded-above complexes with terms in \(\mathcal P\).

Given \(X\), choose by [Stacks, Tag 05T7] a quasi-isomorphism \(P\to X\) from a bounded-above complex with terms in \(\mathcal P\). Then \(L\varinjlim_IX=\varinjlim_IP\). By Lemmas 2.2 and 2.1, \(L(P)\to\varinjlim_IP\) and \(L(P)\to L(X)\) are quasi-isomorphisms. This gives the isomorphism \(L\varinjlim_IX\cong L(X)\), independent of the choice because the morphisms involved are natural. If \(H^q(X)=0\) for \(q>m\), choose \(P\) with \(P^q=0\) for \(q>m\) (loc. cit.). Then \(\varinjlim_IP\) vanishes above degree \(m\). \(\square\)

**Corollary 2.4 (adjunction).** For \(X\in D^-(\mathcal A^I)\) and \(Y\in D(\mathcal A)\) there is a canonical isomorphism
\[
\begin{aligned}&\operatorname{Hom}_{D(\mathcal A)}\bigl(L\varinjlim_IX,Y\bigr)\\&\quad\cong\operatorname{Hom}_{D(\mathcal A^I)}(X,cY),\end{aligned}
\]
functorial in \(X\) and \(Y\). In particular \(\operatorname{Ext}^i_{\mathcal A}(L\varinjlim_IX,Y)\cong\operatorname{Ext}^i_{\mathcal A^I}(X,cY)\) for every \(i\).

**Proof.** The constant-diagram functor \(c\) is exact, so it is its own derived functor and is defined on all of \(D(\mathcal A)\). It is right adjoint to \(\varinjlim_I\), and \(L\varinjlim_I\) is defined at \(X\). Apply [Stacks, Tag 0DVC]. The second statement is the first for \(Y[i]\). \(\square\)

The natural morphism \(X_i\to L(X)\), the inclusion of the summand of the \(0\)-simplex \(i\) in \(C_0\), is a morphism of complexes, because no horizontal differential leaves column \(0\). Composed with \(\varepsilon\), it is the canonical morphism \(X_i\to\varinjlim_IX\). Through Theorem 2.3, it gives canonical morphisms \(X_i\to L\varinjlim_IX\) in \(D(\mathcal A)\), natural in \(X\).

## 3. Colimits over injective ordinals

Now let \(I=\bar\Delta'\), the category of finite totally ordered sets and injective increasing maps, as in the lesson on strict simplicial objects. Write \(X_n=X([n])\). A diagram \(F\) is *locally constant on* \(\bar\Delta'_{\geq n}\) if it sends every arrow between objects of \(\bar\Delta'_{\geq n}\) to an isomorphism.

**Lemma 3.1.** (a) Let \(S\) be a diagram with \(S_n=0\) for \(n\neq k\). Then \(S\) is colimit-acyclic and \(\varinjlim S=0\). (b) Let \(M\in\mathcal A\) and \(n\ge-1\), and let \(M_{\geq n}\) be the diagram with value \(M\) and identity maps on \(\bar\Delta'_{\geq n}\), and \(0\) on the objects \([m]\), \(m<n\). Then \(M_{\geq n}\) is colimit-acyclic, and \(M=(M_{\geq n})_n\to\varinjlim M_{\geq n}\) is an isomorphism.

**Proof.** (a) Only strings that start at \([k]\) contribute to \(C_\bullet(S)\). The face \(d_0\) of such a string is \(0\) unless the first arrow is the identity of \([k]\). So \(C_\bullet(S)\) is \(S_k\otimes Q_\bullet\), where \(Q_\bullet\) is the quotient of \(\mathbb Z(N(\bar\Delta'_{\geq k}))\) by \(\mathbb Z(N(\bar\Delta'_{\geq k+1}))\). By Deligne's theorem (Theorem 4.2 of the lesson on strict simplicial objects), the chain complex of \(Q_\bullet\) is acyclic. It is a complex of free abelian groups in degrees \(\geq0\), hence contractible: every group of cycles is free, so every short exact sequence of cycles and boundaries splits. So \(sC_\bullet(S)\) is contractible.

(b) Every string that starts in \(\bar\Delta'_{\geq n}\) stays there. So \(C_\bullet(M_{\geq n})=M\otimes\mathbb Z(N(\bar\Delta'_{\geq n}))\), with its augmentation to \(M\). The augmented complex \(s\mathbb Z(N(\bar\Delta'_{\geq n}))\to\mathbb Z\) is acyclic by Corollary 4.3 of the lesson on strict simplicial objects. It is a complex of free abelian groups bounded below, hence contractible, as in (a). So \(sC_\bullet(M_{\geq n})\to M\) is a quasi-isomorphism. The composite \(M_n\to\varinjlim M_{\geq n}\cong M\) is the identity. \(\square\)

**Proposition 3.2.** Let \(F\colon\bar\Delta'\to\mathcal A\) be locally constant on \(\bar\Delta'_{\geq n}\) for some \(n\geq-1\). Then \(F\) is colimit-acyclic, and the canonical map \(F_n\to\varinjlim F\) is an isomorphism.

**Proof.** Let \(F''\subseteq F\) agree with \(F\) on \(\bar\Delta'_{\geq n}\) and vanish on the objects \([m]\), \(m<n\). It is a subdiagram, because arrows only go to larger objects. The quotient \(F'=F/F''\) vanishes on \(\bar\Delta'_{\geq n}\). By Proposition 3.1 of the lesson on strict simplicial objects, \(F''\) restricted to \(\bar\Delta'_{\geq n}\) is isomorphic to a constant diagram, so \(F''\cong(F_n)_{\geq n}\). By Lemma 3.1 (b), \(F''\) is colimit-acyclic and \(F_n\to\varinjlim F''\) is an isomorphism. The diagram \(F'\) has the finite filtration by the subdiagrams \(F'_{\geq k}\), equal to \(F'\) on the objects \([m]\), \(m\geq k\), and \(0\) below, for \(-1\le k\le n\). Its successive quotients are concentrated at single objects. By Lemma 3.1 (a) and the long exact sequences of \(sC_\bullet\), the diagram \(F'\) is colimit-acyclic with \(\varinjlim F'=0\). The long exact sequence for \(0\to F''\to F\to F'\to0\) then shows that \(F\) is colimit-acyclic and that \(\varinjlim F''\to\varinjlim F\) is an isomorphism. The canonical map \(F_n\to\varinjlim F\) is the composite \(F_n=F''_n\to\varinjlim F''\to\varinjlim F\). \(\square\)

**Theorem 3.3.** Let \(X\) be a bounded-above complex of diagrams \(\bar\Delta'\to\mathcal A\). Suppose that for every \(i\) there is \(n(i)\geq-1\) such that the cohomology diagram \(H^i(X)\) is locally constant on \(\bar\Delta'_{\geq n(i)}\).

1. For every \(i\), the canonical map \(H^i(X_{n(i)})\to H^i(L\varinjlim X)\) is an isomorphism.
2. If moreover every term \(X^q\) is colimit-acyclic, for instance locally constant on some \(\bar\Delta'_{\geq m_q}\), then \(L\varinjlim X\to\varinjlim X\) is an isomorphism, so \(H^i(X_{n(i)})\to H^i(\varinjlim X)\) is an isomorphism.

**Proof.** (1) Fix \(i\). By Theorem 2.3, the functor \(L\varinjlim\) takes \(\tau_{\leq i-1}X\) into degrees \(\leq i-1\). The triangle \(\tau_{\leq i-1}X\to X\to\tau_{\geq i}X\) therefore gives \(H^i(L\varinjlim X)\cong H^i(L\varinjlim\tau_{\geq i}X)\). Also \(H^i(X_n)=H^i((\tau_{\geq i}X)_n)\), because evaluation is exact. So we may replace \(X\) by \(\tau_{\geq i}X\), which has finitely many nonzero cohomology diagrams. Let \(N\) be the largest of the corresponding \(n(j)\). Each \(H^j(X)\) is then locally constant on \(\bar\Delta'_{\geq N}\), and \(H^i(X)_{n(i)}\to H^i(X)_N\) is an isomorphism. So it suffices to show that \(H^j(X_N)\to H^j(L\varinjlim X)\) is an isomorphism for all \(j\). For a complex with a single nonzero cohomology diagram \(F\) in degree \(j\), we have \(L\varinjlim X\cong(L\varinjlim F)[-j]=(\varinjlim F)[-j]\), and the claim is Proposition 3.2. In general, induct on the number of nonzero cohomology diagrams. Use the triangle \(\tau_{<j}X\to X\to H^j(X)[-j]\) for the top degree \(j\), and apply the five lemma to the morphism between the long exact sequences of \(H^*((-)_N)\) and of \(H^*(L\varinjlim(-))\).

(2) By Theorem 2.3, a bounded-above complex with colimit-acyclic terms computes \(L\varinjlim\). Proposition 3.2 shows that diagrams which are eventually locally constant are colimit-acyclic. \(\square\)

## 4. Exercises

**Exercise 4.1.** Let \(I\) have two objects \(a,b\) and two arrows \(f,g\colon a\to b\) besides the identities. For \(X=(X_a\rightrightarrows X_b)\), with \(u=X(f)\) and \(v=X(g)\), show that \(\varinjlim X=X_b/\operatorname{im}(u-v)\), that \(L_1\varinjlim X\cong\ker(u-v)\), and that \(L_n\varinjlim X=0\) for \(n\geq2\). Conclude that the colimit over \(I\) is not exact.

**Exercise 4.2.** Suppose \(I\) has a final object \(t\). Show that every diagram is colimit-acyclic and that \(\varinjlim_IX=X(t)\).

## 5. Complete solutions

**4.1.** The nerve of \(I\) has no strings of two composable non-identity arrows. By [Stacks, Tag 019C], the chain complex \(sC_\bullet(X)\) is quasi-isomorphic to its quotient by the degenerate part. That quotient is \(X_a\oplus X_a\to X_a\oplus X_b\) in degrees \(1\) and \(0\), with the two summands of degree \(1\) belonging to \(f\) and to \(g\). The differential \(d_0-d_1\) sends \(x\) in the summand of \(f\) to \((-x,u(x))\), and \(x\) in the summand of \(g\) to \((-x,v(x))\). Eliminating the summand \(X_a\) of degree \(0\), the cokernel is \(X_b/\operatorname{im}(u-v)\). The kernel consists of the pairs \((x,y)\) with \(x+y=0\) and \(u(x)+v(y)=0\), that is \(y=-x\) and \(x\in\ker(u-v)\). There is nothing in degrees \(\geq2\). For \(u=v=0\) and \(X_a\neq0\), the first derived colimit \(\ker(u-v)=X_a\) is nonzero, so the colimit is not exact.

**4.2.** A cocone from \(X\) to an object \(Z\) is determined by its component at \(t\), since every \(X(i)\to Z\) factors through \(X(i)\to X(t)\). So \(\varinjlim_IX=X(t)\). For the acyclicity, append \(t\) to every string: send the summand of \(i_0\to\cdots\to i_n\) identically to the summand of \(i_0\to\cdots\to i_n\to t\) in \(C_{n+1}(X)\), and send \(X(t)\) to the summand of the \(0\)-simplex \(t\). These maps satisfy \(d_{n+1}h=1\) and \(d_kh=hd_k\) for \(k\leq n\). So, as in Corollary 1.2 (2) of the lesson on décalage, the maps \((-1)^{n+1}h\) form a contracting homotopy of the augmented complex \(sC_\bullet(X)\to X(t)\).

## Sources

The derived colimit computed by the simplicial replacement, and its application to colimits over the category of finite ordinals and injective maps, are in Illusie's work on the cotangent complex. The general framework of derived functors on bounded-above derived categories and of adjoint derived functors used here is that of the Stacks project, Chapter *Derived Categories*.
