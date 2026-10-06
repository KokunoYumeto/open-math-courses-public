# Finite étale covers and their analytification

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The Riemann existence theorem says that for a scheme \(X\) of finite type over \(\mathbf C\), the finite étale covers of \(X\) are the same as the finite covering spaces of the topological space \(X(\mathbf C)\). For a smooth projective curve this contains the classical statement that every compact Riemann surface covering it is algebraic. This course proves the theorem in general, without any normality hypothesis on \(X\).

This first lesson sets up the comparison. We put the classical topology on the set of complex points of any scheme locally of finite type over \(\mathbf C\), show that finite étale morphisms become finite covering maps, and, for varieties, compare the structure sheaves of a cover and of its analytification.

We use [Complex analytic spaces and analytification](course:AG-QC/complex-analytic-spaces-and-analytification), which constructs the analytic space \(X^{\rm an}\) of a variety (a reduced separated scheme of finite type over \(\mathbf C\)). All schemes in this course are locally of finite type over \(\mathbf C\) unless stated otherwise.

## 1. The space of complex points

Let \(X\) be a scheme locally of finite type over \(\mathbf C\). By the Nullstellensatz ([Stacks, Tag 00FV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-nullstellensatz)) the closed points of \(X\) are exactly the points with residue field \(\mathbf C\), so we identify the set \(X(\mathbf C)\) of \(\mathbf C\)-points with the set of closed points. Every nonempty scheme locally of finite type over \(\mathbf C\) has a closed point, and every nonempty closed subset contains one.

**Definition 1.1.** If \(X\) is affine, choose a closed immersion \(i:X\to\mathbf A^n_{\mathbf C}\) and give \(X(\mathbf C)\) the topology for which \(i\) is a homeomorphism onto the subset \(i(X)(\mathbf C)\subset\mathbf C^n\) with its Euclidean topology. In general, \(X(\mathbf C)\) carries the topology in which a subset is open if and only if its intersection with \(U(\mathbf C)\) is open for every affine open \(U\subset X\). We call it the *classical topology*.

**Lemma 1.2.**

1. For affine \(X\) the topology of Definition 1.1 does not depend on \(i\), and a morphism of affine schemes of finite type induces a continuous map.
2. If \(X\) is affine and \(h\in\mathcal O(X)\), then \(D(h)(\mathbf C)=\{x:h(x)\ne0\}\) is open in \(X(\mathbf C)\), and its own topology is the subspace topology.
3. For general \(X\), each \(U(\mathbf C)\) with \(U\subset X\) affine open is an open subspace of \(X(\mathbf C)\) with the topology of Definition 1.1, and a morphism \(f:X\to Y\) induces a continuous map \(f(\mathbf C):X(\mathbf C)\to Y(\mathbf C)\). The space \(X(\mathbf C)\) is locally compact, and each \(U(\mathbf C)\) is Hausdorff.
4. If \(X\) is a variety, \(X(\mathbf C)\) is the underlying topological space of \(X^{\rm an}\).
5. The closed immersion \(X_{\rm red}\to X\) induces a homeomorphism \(X_{\rm red}(\mathbf C)\to X(\mathbf C)\).
6. For morphisms \(Y\to X\leftarrow Z\), the canonical bijection \((Y\times_XZ)(\mathbf C)\to Y(\mathbf C)\times_{X(\mathbf C)}Z(\mathbf C)\) is a homeomorphism, where the right side has the subspace topology of the product.

**Proof.** (1) If \(i:X\to\mathbf A^n\) and \(i':X\to\mathbf A^m\) are closed immersions, the coordinate functions of \(i'\) are elements of \(\mathcal O(X)\), which is a quotient of \(\mathbf C[x_1,\ldots,x_n]\) through \(i\). Lifting them gives a polynomial map \(P:\mathbf C^n\to\mathbf C^m\) with \(i'=P\circ i\) on complex points. So the identity of \(X(\mathbf C)\) is continuous from the \(i\)-topology to the \(i'\)-topology, and by symmetry it is a homeomorphism. A morphism \(X\to Y\) of affine schemes is given on coordinates by polynomials in the same way.

(2) The principal open \(D(h)\) is the closed subscheme \(\{th=1\}\) of \(X\times\mathbf A^1\). Its complex points correspond to \(\{x:h(x)\ne0\}\) through \(x\mapsto(x,1/h(x))\), which is a homeomorphism onto its image, with inverse the projection.

(3) Two affine opens \(U,U'\) of \(X\) have intersection covered by opens that are principal in both ([Stacks, Tag 01IW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-standard-open-two-affines)). By (2) the topologies of \(U(\mathbf C)\) and \(U'(\mathbf C)\) induce the same topology on these, so the definition is consistent and each \(U(\mathbf C)\) is an open subspace. Continuity is local and follows from (1) and (2). Each \(U(\mathbf C)\) is a closed subset of some \(\mathbf C^n\), hence locally compact and Hausdorff.

(4) The analytification of a variety is built from the same affine charts, with the Euclidean topology on the complex points of each closed subvariety of affine space, glued along principal opens ([Complex analytic spaces and analytification, Theorem 3.2](course:AG-QC/complex-analytic-spaces-and-analytification#3-constructing-the-analytic-space-of-a-variety)).

(5) The closed immersion \(X_{\rm red}\to X\) is bijective on closed points, and a closed immersion \(X\to\mathbf A^n\) restricts to a closed immersion of \(X_{\rm red}\) with the same set of complex points.

(6) The question is local, so let \(X,Y,Z\) be affine with closed immersions \(Y\to\mathbf A^a\), \(Z\to\mathbf A^b\). Then \(Y\times_XZ\) is a closed subscheme of \(Y\times Z\subset\mathbf A^{a+b}\), and its complex points are the pairs \((y,z)\) with the same image in \(X(\mathbf C)\). \(\square\)

A *finite covering map* is a continuous map \(p:E\to M\) such that every point of \(M\) has an open neighbourhood \(W\) with a homeomorphism \(p^{-1}(W)\cong W\times F\) over \(W\), for some finite set \(F\) with the discrete topology. The number of points of \(p^{-1}(x)\) is then a locally constant function of \(x\), the *degree*. We write \(\operatorname{Cov}(M)\) for the category of finite covering maps \(E\to M\), with continuous maps over \(M\) as morphisms, and \(\operatorname{F\acute Et}(X)\) for the category of finite étale morphisms \(Y\to X\), with \(X\)-morphisms.

## 2. Finite morphisms and étale morphisms

**Lemma 2.1 (finite morphisms are proper).** Let \(q:Y\to X\) be a finite morphism with \(X\) affine. Then \(q(\mathbf C)\) has finite fibres, and the inverse image of every compact subset of \(X(\mathbf C)\) is compact.

**Proof.** Write \(X=\operatorname{Spec}A\) with a closed immersion into \(\mathbf A^n\), and \(Y=\operatorname{Spec}B\) with \(B\) generated as an \(A\)-module, hence as an \(A\)-algebra, by \(b_1,\ldots,b_m\). Then \(y\mapsto(q(y),b_1(y),\ldots,b_m(y))\) is a closed immersion of \(Y\) into \(\mathbf A^n\times\mathbf A^m\). Each \(b_j\) satisfies an equation \(b_j^k+a_{j1}b_j^{k-1}+\cdots+a_{jk}=0\) with \(a_{ji}\in A\). A root \(\beta\) of a monic polynomial \(T^k+c_1T^{k-1}+\cdots+c_k\) satisfies \(|\beta|\le\max\bigl(1,\sum_i|c_i|\bigr)\): if \(|\beta|>1\), then \(|\beta|^k\le\sum_i|c_i||\beta|^{k-i}\le\bigl(\sum_i|c_i|\bigr)|\beta|^{k-1}\). So over a compact \(K\subset X(\mathbf C)\) the coordinates \(b_j\) are bounded, and \(q(\mathbf C)^{-1}(K)\) is a closed and bounded subset of \(\mathbf C^{n+m}\), hence compact. The fibre over \(x\) is the spectrum of the finite-dimensional \(\mathbf C\)-algebra \(B\otimes_A\kappa(x)\), which has finitely many points. \(\square\)

**Lemma 2.2 (étale morphisms are local homeomorphisms).** Let \(q:Y\to X\) be étale and \(y\in Y(\mathbf C)\). There is an open neighbourhood \(O\) of \(y\) in \(Y(\mathbf C)\) that \(q(\mathbf C)\) maps homeomorphically onto an open subset of \(X(\mathbf C)\). More precisely, there are an affine open \(\operatorname{Spec}A\subset X\) containing \(q(y)\), with a closed immersion into \(\mathbf A^n\), an affine open neighbourhood of \(y\) isomorphic over \(\operatorname{Spec}A\) to \(\operatorname{Spec}\bigl(A[t]_g/(f)\bigr)\), with \(f\) monic in \(t\) and \(\partial f/\partial t\) invertible there, lifts \(F,G\in\mathbf C[x_1,\ldots,x_n,t]\) of \(f,g\), and a holomorphic function \(\varphi\) on a neighbourhood \(W\) of \(q(y)\) in \(\mathbf C^n\) such that, near \(y\), \(Y(\mathbf C)\) is the graph of \(\varphi\) over \(X(\mathbf C)\cap W\cap\{G(x,\varphi(x))\ne0\}\), and

\[
F(x,t)=(t-\varphi(x))\,u(x,t)
\]

near \((q(y),t(y))\) for a holomorphic function \(u\) without zeros.

**Proof.** By [Stacks, Tag 02GT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-locally-standard-etale), \(q\) is standard étale near \(y\), which gives the presentation. Write \(y=(x_0,t_0)\) in \(\mathbf C^{n+1}\). Then \(F(x_0,t_0)=0\) and \(\partial F/\partial t(x_0,t_0)\ne0\), since \(\partial f/\partial t\) is invertible at \(y\). By the holomorphic implicit function theorem ([Complex analytic spaces and analytification, Lemma 2.2](course:AG-QC/complex-analytic-spaces-and-analytification#2-local-analytic-algebra)) there are neighbourhoods \(W\) of \(x_0\) and \(I\) of \(t_0\), and a holomorphic \(\varphi:W\to I\), such that \(\{(x,t)\in W\times I:F(x,t)=0\}\) is the graph of \(\varphi\). The set of complex points of \(Y\) inside \(W\times I\) is therefore \(\{(x,\varphi(x)):x\in X(\mathbf C)\cap W,\ G(x,\varphi(x))\ne0\}\), and the projection maps it homeomorphically, with inverse \(x\mapsto(x,\varphi(x))\), onto the open subset of \(X(\mathbf C)\cap W\) where \(G(x,\varphi(x))\ne0\). Finally

\[
F(x,t)=F(x,t)-F(x,\varphi(x))=(t-\varphi(x))\int_0^1\frac{\partial F}{\partial t}\bigl(x,\varphi(x)+s(t-\varphi(x))\bigr)\,ds,
\]

and the integral \(u\) is holomorphic and equals \(\partial F/\partial t(x_0,t_0)\ne0\) at \((x_0,t_0)\), so it has no zeros near that point. \(\square\)

**Proposition 2.3.** Let \(q:Y\to X\) be finite étale. Then \(q(\mathbf C)\) is a finite covering map, and the number of points of \(q(\mathbf C)^{-1}(x)\) is the rank at \(x\) of the locally free sheaf \(q_*\mathcal O_Y\).

**Proof.** The statement is local on \(X\), so let \(X\) be affine; then \(Y\) is affine and \(Y(\mathbf C)\) is Hausdorff. Let \(x\in X(\mathbf C)\) with fibre \(\{y_1,\ldots,y_r\}\) (Lemma 2.1). By Lemma 2.2 choose pairwise disjoint open neighbourhoods \(O_i\) of \(y_i\) that \(q(\mathbf C)\) maps homeomorphically onto open sets. Let \(K\) be a compact neighbourhood of \(x\). The set \(C=q(\mathbf C)^{-1}(K)\setminus\bigcup_iO_i\) is compact by Lemma 2.1, so \(q(C)\) is compact, hence closed, and it does not contain \(x\). Then

\[
W=\operatorname{int}K\cap\bigcap_iq(O_i)\setminus q(C)
\]

is an open neighbourhood of \(x\), its inverse image lies in \(\bigcup_iO_i\), and each \(O_i\cap q(\mathbf C)^{-1}(W)\) maps homeomorphically onto \(W\). So \(q(\mathbf C)^{-1}(W)\cong W\times\{1,\ldots,r\}\).

A finite étale morphism is finite, flat and of finite presentation, so \(q_*\mathcal O_Y\) is locally free ([Stacks, Tag 02KB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-finite-flat)). The fibre over \(x\) is the spectrum of the finite étale \(\mathbf C\)-algebra \(q_*\mathcal O_Y\otimes\kappa(x)\), which is a product of copies of \(\mathbf C\) ([Stacks, Tag 00U3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-etale-over-field)); the number of factors is the rank, and it is the number of points. \(\square\)

So \(Y\mapsto Y(\mathbf C)\) is a functor

\[
\Phi_X:\operatorname{F\acute Et}(X)\longrightarrow\operatorname{Cov}(X(\mathbf C)),
\]

and by Lemma 1.2(6) it commutes with fibre products and with pull-back along morphisms \(X'\to X\). The Riemann existence theorem says that \(\Phi_X\) is an equivalence of categories.

## 3. The analytic structure of a cover

For varieties we also compare structure sheaves. This is used when a cover is constructed from its sheaf of functions.

**Proposition 3.1.** Let \(X\) be a variety and \(q:Y\to X\) finite étale of constant degree \(d\). Then \(Y\) is a variety, \(q^{\rm an}:Y^{\rm an}\to X^{\rm an}\) is a local isomorphism of analytic spaces, and the natural map

\[
(q_*\mathcal O_Y)^{\rm an}\longrightarrow q^{\rm an}_*\mathcal O_{Y^{\rm an}}
\]

is an isomorphism of locally free \(\mathcal O_{X^{\rm an}}\)-algebras of rank \(d\).

**Proof.** The scheme \(Y\) is separated, being finite over \(X\), and reduced, being étale, hence smooth, over the reduced \(X\) ([Stacks, Tag 034E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-reduced-local-smooth)). In the presentation of Lemma 2.2, the analytic space \(Y^{\rm an}\) near \(y\) is the analytic subspace of \(X^{\rm an}\times\mathbf C\) defined by \(F\) on \(\{G\ne0\}\), by [Complex analytic spaces and analytification, Theorem 3.2 and Lemma 3.1](course:AG-QC/complex-analytic-spaces-and-analytification#3-constructing-the-analytic-space-of-a-variety): \(Y\) is a reduced locally closed subvariety of \(\mathbf A^{n+1}\), and the analytic ideal of its analytification is generated by the algebraic equations. Since \(F=(t-\varphi(x))u\) with \(u\) a unit near \(y\), the ideal generated by the equations of \(X^{\rm an}\) and \(F\) equals the ideal generated by those equations and \(t-\varphi(x)\). So the projection is an isomorphism of analytic spaces from a neighbourhood of \(y\) in \(Y^{\rm an}\) onto an open subset of \(X^{\rm an}\), with inverse \(x\mapsto(x,\varphi(x))\).

The natural map sends a section of \(q_*\mathcal O_Y\) over a Zariski open \(V\), that is, a regular function on \(q^{-1}(V)\), to the corresponding holomorphic function on \((q^{\rm an})^{-1}(V^{\rm an})\), and is extended \(\mathcal O_{X^{\rm an}}\)-linearly. The source is the analytification of a locally free module of rank \(d\). The target is locally free of rank \(d\): over an open \(W\) as in Proposition 2.3, on which \(q^{\rm an}\) is a disjoint union of \(d\) sheets each isomorphic to \(W\), it is \(\mathcal O_W^d\). On fibres at \(x\in X(\mathbf C)\) both sides are the functions on the \(d\) points over \(x\), and the map is the identity: the fibre of the source is \(q_*\mathcal O_Y\otimes\kappa(x)=\mathbf C^{q^{-1}(x)}\), because analytification does not change fibres at complex points ([Complex analytic spaces and analytification, Theorem 4.1](course:AG-QC/complex-analytic-spaces-and-analytification#4-the-comparison-at-a-point)). A map of free modules of the same finite rank over a local ring that is surjective modulo the maximal ideal is surjective by Nakayama's lemma, hence an isomorphism. \(\square\)

## 4. Nonreduced schemes

**Proposition 4.1.** For every scheme \(X\) locally of finite type over \(\mathbf C\), pull-back along \(X_{\rm red}\to X\) is an equivalence \(\operatorname{F\acute Et}(X)\to\operatorname{F\acute Et}(X_{\rm red})\), compatible with \(\Phi_X\), \(\Phi_{X_{\rm red}}\) and the homeomorphism \(X_{\rm red}(\mathbf C)=X(\mathbf C)\). Hence \(\Phi_X\) is an equivalence if and only if \(\Phi_{X_{\rm red}}\) is.

**Proof.** The morphism \(X_{\rm red}\to X\) is a universal homeomorphism, so pull-back is an equivalence on finite étale covers ([Stacks, Tag 0BQN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-universal-homeomorphism)). For \(Y\) finite étale over \(X\), the space \((Y\times_XX_{\rm red})(\mathbf C)\) is \(Y(\mathbf C)\) by Lemma 1.2(5),(6). \(\square\)

## 5. Examples

**Example 5.1 (powers on the multiplicative group).** The morphism \(\mathbf G_m\to\mathbf G_m\), \(z\mapsto z^n\), is finite étale of degree \(n\): it is \(\operatorname{Spec}\mathbf C[z,z^{-1}][w]/(w^n-z)\), and \(\partial(w^n-z)/\partial w=nw^{n-1}\) is invertible. On complex points it is the \(n\)-sheeted covering \(\mathbf C^*\to\mathbf C^*\).

**Example 5.2 (a covering that is not finite).** The exponential map \(\mathbf C\to\mathbf C^*\) is a covering map with infinite fibres. It is not \(\Phi(Y)\) for any finite étale \(Y\), and the Riemann existence theorem says nothing about it. It is not even the complex points of an algebraic morphism: compare Section 6 of [Complex analytic spaces and analytification](course:AG-QC/complex-analytic-spaces-and-analytification).

**Example 5.3 (a cover of a nodal curve).** Let \(X\) be the nodal cubic \(y^2=x^2(x+1)\). Its normalization is \(\mathbf A^1\to X\), \(t\mapsto(t^2-1,t(t^2-1))\), identifying \(t=1\) and \(t=-1\). Let \(Y\) be the curve obtained from two copies of \(\mathbf A^1\) by identifying \(t=1\) on each copy with \(t=-1\) on the other; it has two nodes. The two normalization maps induce a finite morphism \(Y\to X\) of degree \(2\), which near each node of \(Y\) induces an isomorphism of complete local rings onto that of the node of \(X\), and is therefore étale. Its complex points form a connected double cover of \(X(\mathbf C)\), a space homotopy equivalent to a circle. Every finite étale cover of \(X\) is singular over the node, because an étale morphism induces isomorphisms of complete local rings at complex points; so such covers are invisible to constructions that only produce normal schemes. This is why the proof of the general theorem passes through descent.

## 6. Exercises

**Exercise 6.1.** Show that the classical topology of \(\mathbf P^1(\mathbf C)\), obtained from the two affine charts by Definition 1.1, is that of the Riemann sphere, and that it is compact.

*Solution.* The charts \(U_0,U_1\cong\mathbf A^1\) give two copies of \(\mathbf C\) glued along \(\mathbf C^*\) by \(z\mapsto1/z\), which is the Riemann sphere. It is compact, being the union of the two compact discs \(|z|\le1\) and \(|1/z|\le1\).

**Exercise 6.2.** Let \(X\) be the affine line with the origin doubled. Describe \(X(\mathbf C)\), and show that the identity covering of \(X(\mathbf C)\) is the only connected finite covering of degree one, while \(X(\mathbf C)\) is not Hausdorff.

*Solution.* \(X(\mathbf C)\) is two copies of \(\mathbf C\) glued along \(\mathbf C^*\). The two origins have no disjoint neighbourhoods, since every neighbourhood of either contains a punctured disc around zero. A covering of degree one is a homeomorphism onto the base, so it is isomorphic to the identity covering.

**Exercise 6.3.** In Lemma 2.2, take \(X=\mathbf A^1\), \(Y=\mathbf G_m\) and \(q(w)=w^2\) restricted to \(Y=\{w\ne0\}\). Find \(F\), \(\varphi\) and \(u\) near the point \(w=1\).

*Solution.* Here \(Y=\operatorname{Spec}\mathbf C[x][t]_t/(t^2-x)\), so \(F=t^2-x\) and \(G=t\). Near \((x,t)=(1,1)\), \(\varphi(x)=\sqrt x\), the branch with \(\sqrt1=1\), and \(F=(t-\sqrt x)(t+\sqrt x)\), so \(u=t+\sqrt x\), which is near \(2\).

**Exercise 6.4.** Show that Proposition 2.3 fails for étale morphisms that are not finite, using the open immersion \(\mathbf A^1\setminus\{0\}\to\mathbf A^1\).

*Solution.* The open immersion is étale, and on complex points it is the inclusion \(\mathbf C^*\to\mathbf C\). The fibre over \(0\) is empty while nearby fibres have one point, so the degree is not locally constant and the map is not a covering map. Properness, from Lemma 2.1, is what fails.

## References

- [SGA 1] A. Grothendieck et al., *Revêtements étales et groupe fondamental (SGA 1)*, Exposé XII, Sections 1–3, for the analytic space of a scheme and the comparison of properties of morphisms; free re-edition arXiv:math/0206203. <https://arxiv.org/abs/math/0206203>
- [Serre] J.-P. Serre, *Géométrie algébrique et géométrie analytique*, Ann. Inst. Fourier 6 (1956), 1–42, free from Numdam. <https://www.numdam.org/item/AIF_1956__6__1_0/>
