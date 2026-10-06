# Covers of smooth varieties

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the Riemann existence theorem for smooth varieties: every finite covering of the space of complex points is the space of complex points of a finite étale cover. The proof places the variety inside a smooth projective variety whose boundary is a divisor with simple normal crossings. It extends the covering across the boundary as a sheaf of algebras, using the locally bounded functions of the previous lesson. GAGA then makes this sheaf algebraic, and the algebraic cover is read off from it.

We use [Finite étale covers and their analytification](finite-etale-covers-and-their-analytification.md), [Connectedness and full faithfulness](connectedness-and-full-faithfulness.md), [Finite covers of punctured polydiscs](finite-covers-of-punctured-polydiscs.md), [Principalization and resolution, Corollary 5.2](course:resolution-of-singularities-in-characteristic-zero/principalization-and-resolution#5-consequences-used-in-the-programme) (smooth compactification), [Serre's comparison theorems and Chow's theorem](course:AG-QC/serres-comparison-theorems-and-chows-theorem), and [Complex analytic spaces and analytification](course:AG-QC/complex-analytic-spaces-and-analytification).

## 1. Covers are determined by their sheaves of functions

Let \(M\) be a complex manifold. A finite covering \(p:E\to M\) carries a unique complex structure making \(p\) a local biholomorphism, and \(p_*\mathcal O_E\) is a locally free \(\mathcal O_M\)-algebra whose rank at \(x\) is the number of points over \(x\).

**Lemma 1.1.** Let \(p:E\to M\) and \(p':E'\to M\) be finite coverings of a complex manifold. Every isomorphism of \(\mathcal O_M\)-algebras \(\alpha:p_*\mathcal O_E\to p'_*\mathcal O_{E'}\) is induced by a unique homeomorphism \(g:E'\to E\) over \(M\), in the sense that \(\alpha(f)=f\circ g\).

**Proof.** Let \(W\subset M\) be a connected open set over which both coverings are trivial, \(p^{-1}(W)=\bigsqcup_{i=1}^dW_i\) and \(p'^{-1}(W)=\bigsqcup_{j=1}^{d'}W'_j\), each sheet mapping biholomorphically onto \(W\). Then \(p_*\mathcal O_E(W)\cong\mathcal O(W)^d\), and its primitive idempotents are the characteristic functions \(e_i\) of the sheets \(W_i\): since \(W\) is connected, \(\mathcal O(W)\) has no idempotents other than \(0\) and \(1\). The algebra isomorphism \(\alpha\) maps primitive idempotents to primitive idempotents, so \(d=d'\) and \(\alpha(e_i)=e'_{\sigma(i)}\) for a bijection \(\sigma\). On \(W'_{\sigma(i)}\) let \(g\) be the composite of \(p'\) with the inverse of \(p|_{W_i}\). For \(f\in p_*\mathcal O_E(W)\) write \(e_if=e_i\,(f_i\circ p)\) with \(f_i=f\circ(p|_{W_i})^{-1}\in\mathcal O(W)\). Since \(\alpha\) is \(\mathcal O(W)\)-linear and multiplicative, \(\alpha(e_if)=e'_{\sigma(i)}\,(f_i\circ p')\), which on \(W'_{\sigma(i)}\) is \(f\circ g\). Summing over \(i\) gives \(\alpha(f)=f\circ g\). The map \(g\) is determined by \(\alpha\), so the local definitions agree on overlaps, and \(g\) is a homeomorphism, being a bijective local homeomorphism with inverse obtained from \(\alpha^{-1}\). Uniqueness: \(g\) is determined on each sheet by which idempotent it pulls back to which. \(\square\)

## 2. The smooth quasi-projective case

**Theorem 2.1.** Let \(X\) be a smooth quasi-projective variety over \(\mathbf C\). For every finite covering \(E\to X(\mathbf C)\) there is a finite étale \(Y\to X\) with \(Y(\mathbf C)\cong E\) over \(X(\mathbf C)\).

**Proof.** By Corollary 3.3 of [Connectedness and full faithfulness](connectedness-and-full-faithfulness.md#3-full-faithfulness) we may treat the connected components of \(X\) separately, so let \(X\) be connected, hence irreducible, and let \(E\) have degree \(d\); by the same corollary we may also assume \(d\ge1\). By [Principalization and resolution, Corollary 5.2](course:resolution-of-singularities-in-characteristic-zero/principalization-and-resolution#5-consequences-used-in-the-programme) there is a smooth projective variety \(R\) containing \(X\) as a dense open subset, such that \(R\setminus X\) is the support of an snc divisor \(D\). Write \(j:X(\mathbf C)\to R(\mathbf C)\) for the inclusion and \(p:E\to X(\mathbf C)\) for the covering.

*Step 1: the extension sheaf.* For an open set \(W\subset R(\mathbf C)\) let \(\mathcal A(W)\) be the algebra of holomorphic functions on \(p^{-1}(W\cap X(\mathbf C))\) that are locally bounded on \(W\): every point of \(W\) has a neighbourhood \(W'\) on whose part \(p^{-1}(W'\cap X(\mathbf C))\) the function is bounded. This is a sheaf of \(\mathcal O_{R^{\rm an}}\)-algebras with \(\mathcal A|_{X(\mathbf C)}=p_*\mathcal O_E\). We claim that it is locally free of rank \(d\). At points of \(X(\mathbf C)\) this holds because \(p\) is a finite covering. Let \(x\in D(\mathbf C)\), and let \(z_1,\ldots,z_n\) be regular functions near \(x\), vanishing at \(x\), forming a coordinate system in which the components of \(D\) through \(x\) are \(V(z_1),\ldots,V(z_p)\). By Lemma 1.1 of [Connectedness and full faithfulness](connectedness-and-full-faithfulness.md#1-smooth-points-and-divisors-with-normal-crossings), \(z\) maps a neighbourhood of \(x\) biholomorphically onto an open neighbourhood of \(0\) in \(\mathbf C^n\), with \(D(\mathbf C)\) corresponding to \(\{z_1\cdots z_p=0\}\). After shrinking and rescaling the coordinates, a neighbourhood \(V\) of \(x\) becomes the unit polydisc \(\Delta^n\), with \(V\cap X(\mathbf C)\) corresponding to \((\Delta^*)^p\times\Delta^{n-p}\), the space \(V^*\) of the previous lesson. On \(V\), \(\mathcal A\) is by definition the sheaf \(\mathcal A_{E_V}\) of the restricted covering \(E_V=p^{-1}(V^*)\to V^*\), and by [Finite covers of punctured polydiscs, Theorem 3.3](finite-covers-of-punctured-polydiscs.md#3-the-extension) it is locally free of rank \(d\).

*Step 2: algebraization.* By the third comparison theorem ([Serre's comparison theorems and Chow's theorem, Theorem 5.2](course:AG-QC/serres-comparison-theorems-and-chows-theorem#5-the-third-comparison-theorem)) there is a coherent \(\mathcal O_R\)-module \(\mathcal B\) with an isomorphism \(\mathcal B^{\rm an}\cong\mathcal A\). Analytification commutes with tensor products ([Complex analytic spaces and analytification, Proposition 5.1](course:AG-QC/complex-analytic-spaces-and-analytification#5-coherent-modules-and-compactness)), so the multiplication \(\mathcal A\otimes\mathcal A\to\mathcal A\) and the unit \(\mathcal O_{R^{\rm an}}\to\mathcal A\) are morphisms \((\mathcal B\otimes\mathcal B)^{\rm an}\to\mathcal B^{\rm an}\) and \(\mathcal O_R^{\rm an}\to\mathcal B^{\rm an}\). By the second comparison theorem ([Serre's comparison theorems and Chow's theorem, Theorem 4.1](course:AG-QC/serres-comparison-theorems-and-chows-theorem#4-the-second-comparison-theorem)) they are the analytifications of unique morphisms \(\mathcal B\otimes\mathcal B\to\mathcal B\) and \(\mathcal O_R\to\mathcal B\). Associativity, commutativity and the unit axioms hold after analytification, hence before, because analytification is faithful. So \(\mathcal B\) is a coherent \(\mathcal O_R\)-algebra.

The module \(\mathcal B\) is locally free of rank \(d\). Indeed, at a closed point \(y\) the map \(\mathcal O_{R,y}\to\mathcal O_{R^{\rm an},y}\) is faithfully flat ([Complex analytic spaces and analytification, Theorem 4.1](course:AG-QC/complex-analytic-spaces-and-analytification#4-the-comparison-at-a-point)), and \(\mathcal B_y\otimes\mathcal O_{R^{\rm an},y}=\mathcal A_y\) is free of rank \(d\). So \(\mathcal B_y\) is flat, because flatness descends along faithfully flat ring maps ([Stacks, Tag 00HJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-flatness-descends)); a finitely generated flat module over a noetherian local ring is free ([Stacks, Tag 00NZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-flat-local)), and its rank is \(d\). The set of points where a coherent module is locally free is open, and it contains all closed points, so it is all of \(R\).

*Step 3: the algebraic cover.* Let \(Y=\operatorname{Spec}_X(\mathcal B|_X)\) and \(q:Y\to X\). Then \(q\) is finite and flat of degree \(d\). At a closed point \(x\in X\), its fibre is \(\operatorname{Spec}\) of

\[
\mathcal B\otimes\kappa(x)=\mathcal B^{\rm an}\otimes\kappa(x)=\mathcal A\otimes\kappa(x)=p_*\mathcal O_E\otimes\kappa(x)=\mathbf C^{p^{-1}(x)}.
\]

The first equality holds because analytification does not change fibres at complex points. The last holds because, over a neighbourhood on which \(E\) is trivial, the sections of \(p_*\mathcal O_E\) vanishing at \(x\) are the tuples of functions on the sheets vanishing at the points over \(x\). The fibre is a product of copies of \(\mathbf C\), so \(q\) is unramified at every point over a closed point, and, being flat, étale there. The étale locus of \(q\) is open and contains every closed point of the scheme \(Y\) of finite type over \(\mathbf C\), so it is all of \(Y\). Thus \(q\) is finite étale.

*Step 4: comparison.* By [Finite étale covers and their analytification, Proposition 3.1](finite-etale-covers-and-their-analytification.md#3-the-analytic-structure-of-a-cover), \(Y(\mathbf C)\to X(\mathbf C)\) is a finite covering, and

\[
q^{\rm an}_*\mathcal O_{Y^{\rm an}}\cong(q_*\mathcal O_Y)^{\rm an}=\mathcal B^{\rm an}|_{X(\mathbf C)}\cong\mathcal A|_{X(\mathbf C)}=p_*\mathcal O_E
\]

as \(\mathcal O_{X^{\rm an}}\)-algebras. By Lemma 1.1 there is a homeomorphism \(E\cong Y(\mathbf C)\) over \(X(\mathbf C)\). \(\square\)

**Corollary 2.2.** For every smooth scheme \(X\) of finite type over \(\mathbf C\), the functor \(\Phi_X:\operatorname{F\acute Et}(X)\to\operatorname{Cov}(X(\mathbf C))\) is an equivalence.

**Proof.** It is fully faithful by [Connectedness and full faithfulness, Corollary 3.1](connectedness-and-full-faithfulness.md#3-full-faithfulness). For essential surjectivity, cover \(X\) by affine opens; they are smooth quasi-projective varieties, so Theorem 2.1 applies to them, and [Connectedness and full faithfulness, Proposition 3.2](connectedness-and-full-faithfulness.md#3-full-faithfulness) glues. \(\square\)

**Remark 2.3.** The algebra \(\mathcal B\) extends the cover to a finite flat cover of the whole compactification \(R\), branched along \(D\). In the classical case of a smooth projective curve \(R\) and a finite set of points \(D\), \(\operatorname{Spec}\mathcal B\) is the projective curve obtained by filling in the punctures of a finite covering of \(R(\mathbf C)\setminus D(\mathbf C)\); this is the classical form of the Riemann existence theorem for curves. The construction used no normality of the extended cover; the cone of [Finite covers of punctured polydiscs, Example 4.3](finite-covers-of-punctured-polydiscs.md#4-examples) shows that the extension can be singular.

## 3. Examples

**Example 3.1 (the punctured line).** Let \(X=\mathbf G_m\), \(R=\mathbf P^1\), \(D=\{0,\infty\}\). A connected covering of \(\mathbf C^*\) of degree \(m\) is \(t\mapsto t^m\), up to isomorphism. Near \(0\) and \(\infty\) the extension sheaf \(\mathcal A\) is free with basis \(1,t,\ldots,t^{m-1}\), respectively \(1,t^{-1},\ldots,t^{1-m}\). Splitting by the characters of the group \(\mu_m\) acting by \(t\mapsto\zeta t\), the summand of character \(\zeta^k\), \(1\le k\le m-1\), is spanned by \(t^k\) near \(0\) and by \(t^{k-m}=z^{-1}t^k\) near \(\infty\), so it is \(\mathcal O(-1)\), and \(\mathcal B=\mathcal O\oplus\mathcal O(-1)^{\oplus(m-1)}\) on \(\mathbf P^1\). As a check, its Euler characteristic is \(1\), that of \(\mathcal O_{\mathbf P^1}\). The scheme \(\operatorname{Spec}\mathcal B\) is the curve \(\mathbf P^1\) mapping by \(t\mapsto t^m\). Over \(X\) this is the finite étale cover of Example 5.1 of the first lesson.

**Example 3.2 (an elliptic curve).** Let \(R=E_0\) be an elliptic curve and \(D=\emptyset\). For every finite covering of the torus \(E_0(\mathbf C)\), Theorem 2.1 gives a finite étale cover of \(E_0\). A connected one of degree \(n\) is a curve of genus one by the Riemann–Hurwitz formula, and with a suitable origin the cover is an isogeny of degree \(n\) onto \(E_0\). Here no boundary is involved, and Steps 2 to 4 are GAGA alone.

## 4. Exercises

**Exercise 4.1.** In Example 3.1 with \(m=2\), compute \(\mathcal B\) as an \(\mathcal O_{\mathbf P^1}\)-module and check that its rank is \(2\) and its fibre over \(t^2=1\) is \(\mathbf C^2\).

*Solution.* Over \(\mathbf A^1=\mathbf P^1\setminus\{\infty\}\), \(\mathcal B\) is free with basis \(1,t\), where \(t^2=z\). Over \(\mathbf P^1\setminus\{0\}\) it is free with basis \(1,t^{-1}\). On the overlap \(t^{-1}=z^{-1}t\), so the second summand is \(\mathcal O(-1)\), and \(\mathcal B=\mathcal O\oplus\mathcal O(-1)\), of rank \(2\). Over \(z=1\) the fibre is \(\mathbf C[t]/(t^2-1)\cong\mathbf C^2\).

**Exercise 4.2.** Where does the proof of Theorem 2.1 use that \(R\) is projective, and where that \(D\) has normal crossings?

*Solution.* Projectivity is needed for the comparison theorems in Step 2. Normal crossings are needed in Step 1, where the local structure \((\Delta^*)^p\times\Delta^{n-p}\) of the complement is used to show that \(\mathcal A\) is locally free.

**Exercise 4.3.** Show that Lemma 1.1 fails if the algebra isomorphism is only required to be an isomorphism of \(\mathcal O_M\)-modules.

*Solution.* For the trivial double covering of a connected \(M\), the module automorphism of \(\mathcal O_M^2\) given by a constant invertible matrix that is not a permutation matrix does not preserve the idempotents, so it is not induced by a map of coverings.

## References

- [SGA 1] A. Grothendieck et al., *Revêtements étales et groupe fondamental (SGA 1)*, Exposé XII, proof of Theorem 5.1, part c), and Section 4 (GAGA for finite covers); free re-edition arXiv:math/0206203. In this lesson the extension across the boundary is the locally free algebra of locally bounded functions. <https://arxiv.org/abs/math/0206203>
- [Serre] J.-P. Serre, *Géométrie algébrique et géométrie analytique*, Ann. Inst. Fourier 6 (1956), 1–42, free from Numdam. <https://www.numdam.org/item/AIF_1956__6__1_0/>
