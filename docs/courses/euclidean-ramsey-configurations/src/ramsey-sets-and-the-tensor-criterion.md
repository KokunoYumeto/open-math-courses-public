# Ramsey sets and the tensor criterion

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Colour every point of a Euclidean space with one of finitely many colours. Which finite shapes are forced to appear with all their points of one colour, at their original size, once the dimension is large enough? This course proves the complete answer found by OpenAI [OpenAI-ER]: an exact algebraic condition on the coordinates of the shape.

**Definition.** Let \(A\) be a finite nonempty subset of a Euclidean space. A *congruent copy* of \(A\) in \(\mathbb R^D\) is a set \(A'\subseteq\mathbb R^D\) with a bijection \(A\to A'\) that preserves all distances. The set \(A\) is *Ramsey* if for every integer \(r\ge2\) there is an integer \(D\ge1\) such that every map \(c:\mathbb R^D\to\{1,\dots,r\}\) is constant on some congruent copy of \(A\).

The colourings are arbitrary maps; no measurability or continuity is assumed. Two points at distance \(\delta\) form a Ramsey set: the \(r+1\) vertices of a regular simplex of side \(\delta\) in \(\mathbb R^r\) receive \(r\) colours, so two of them share a colour.

Euclidean Ramsey theory was introduced by Erdős, Graham, Montgomery, Rothschild, Spencer and Straus, who proved that every Ramsey set lies on a sphere [EGMRSS]. Graham conjectured the converse. Frankl and Rödl proved that all triangles and all simplices are Ramsey, Kříž treated sets with a soluble transitive symmetry group and all trapezoids, and Cantwell the vertex sets of regular polytopes; the survey [Graham] describes the state of the subject in 1994, and [OpenAI-ER, Section 1] gives references for these results. Leader, Russell and Walters proposed that a finite set is Ramsey exactly when it embeds in a finite set whose isometry group acts transitively [LRW-T]. In 2026 a paper by Pálvölgyi, which attributes its construction and proofs to ChatGPT, exhibited seven points on a circle that do not form a Ramsey set [Pal], so lying on a sphere is not sufficient.

## The classification

A singleton is Ramsey. For a set with at least two points, let \(d\ge1\) be the dimension of its affine span, and choose a congruent copy \(A=\{a_1,\dots,a_s\}\subset\mathbb R^d\) whose affine span is \(\mathbb R^d\). Put
\[
p_i=\begin{pmatrix}1\\a_i\end{pmatrix}\in\mathbb R^{1+d},
\]
and index the entries of \(p_i\), and the rows and columns of \((d+1)\times(d+1)\) matrices, by \(0,1,\dots,d\); the index \(0\) is the constant coordinate. Let \(F\subseteq\mathbb R\) be the field generated over \(\mathbb Q\) by all coordinates of all \(a_i\), let
\[
B=F\otimes_{\mathbb Q}F ,
\]
and let \(m_F:B\to F\) be the multiplication map, \(m_F(x\otimes y)=xy\). Tensor products over \(\mathbb Q\) are recalled in Section 1.

**Theorem** (classification [OpenAI-ER]). Let \(A=\{a_1,\dots,a_s\}\subset\mathbb R^d\) have at least two points and affine span \(\mathbb R^d\). Then \(A\) is Ramsey if and only if there is a matrix \(P\in\mathrm{Mat}_{d+1}(B)\) such that
\[
\begin{gathered}
(p_i\otimes1)^{\mathsf T}P(1\otimes p_i)=0\quad(1\le i\le s),\\
m_F(P_{\alpha\beta})=\delta_{\alpha\beta}\quad(1\le\alpha,\beta\le d).
\end{gathered}
\]

Here \((p_i\otimes1)^{\mathsf T}P(1\otimes p_i)\) means \(\sum_{\alpha,\beta=0}^d(p_{i\alpha}\otimes1)P_{\alpha\beta}(1\otimes p_{i\beta})\), computed in the ring \(B\). There is no condition on the row and the column of index \(0\) after multiplication. Applying \(m_F\) to the first equations turns them into equations of a sphere through the points (Proposition 3.1); the theorem demands that these equations hold before multiplication, in \(B\), where \(x\otimes y\) and \(xy\otimes1\) are different elements. This is the difference between lying on a sphere and being Ramsey.

**The course.**

1. This lesson: tensor products over \(\mathbb Q\), the criterion as a condition on affine functions, invariance under congruence, and the sphere through a set satisfying it.
2. [A colouring obstruction](a-colouring-obstruction.md): if the criterion fails, a fixed number of colours avoids the set in every dimension.
3. [A finite lattice identity](a-finite-lattice-identity.md): the criterion gives signed weights on a lattice with exact cancellations.
4. [Two-scale configurations](two-scale-configurations.md): two copies of the set at very different scales whose corresponding points have the same coordinates in different orders.
5. [The Hales–Jewett theorem](the-hales-jewett-theorem.md).
6. [Ultrafilters and idempotents](ultrafilters-and-idempotents.md): a group inside the compact semigroup of ultrafilters on strings.
7. [The path criterion](the-path-criterion.md): products of scaled copies in a free group force monochromatic copies.
8. [Equal endpoints](equal-endpoints.md): the two-scale configurations give such products; proof of the theorem.
9. [Examples on circles](examples-on-circles.md): transitive sets, five points on a circle, kites, and two sets on a circle that are not Ramsey.

**What the course assumes.** Linear algebra over a field, including Gaussian elimination, and the diagonalization of real symmetric matrices by orthogonal matrices; Zorn's lemma; the definition of a Noetherian ring and of the completion of a ring at an ideal, with the Hilbert basis theorem and the flatness of completion from the programme's lessons [Noetherian and Artinian rings](course:AG-CA/noetherian-and-artinian-rings) (Theorem 2.1) and [Completion](course:AG-CA/completion) (Theorem 3.2); and, in the fourth lesson, the Riemann integral in several variables with Fubini's theorem, linear changes of variables and differentiation under the integral sign, from the core course [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20) (exact theorems are cited there). Everything else is proved in the lessons, including the theorem of Leader, Russell and Walters that certain kites embed in no finite transitive set [LRW-K].

## 1. Tensor products over the rationals

All vector spaces in this section are over \(\mathbb Q\). The real numbers form an infinite-dimensional vector space over \(\mathbb Q\).

**Lemma 1.1.** Every linearly independent subset of a vector space is contained in a basis.

*Proof.* Order the linearly independent sets containing the given one by inclusion. The union of a chain is linearly independent, because a linear relation involves finitely many vectors, which lie in one member of the chain. By Zorn's lemma there is a maximal one. A vector outside its span could be added to it, so it spans. \(\square\)

Let \(V\) and \(V'\) be vector spaces with bases \((x_\lambda)_{\lambda\in\Lambda}\) and \((y_\mu)_{\mu\in M}\). The *tensor product* \(V\otimes V'\) is the vector space with basis the symbols \(x_\lambda\otimes y_\mu\), and for \(x=\sum a_\lambda x_\lambda\) and \(y=\sum b_\mu y_\mu\) one puts \(x\otimes y=\sum a_\lambda b_\mu\,x_\lambda\otimes y_\mu\). The map \((x,y)\mapsto x\otimes y\) is bilinear, and every bilinear map \(\beta:V\times V'\to U\) factors uniquely as \(\beta(x,y)=\tilde\beta(x\otimes y)\) through a linear map \(\tilde\beta\), defined on the basis by \(\tilde\beta(x_\lambda\otimes y_\mu)=\beta(x_\lambda,y_\mu)\). This universal property shows that other choices of bases give the same space up to a unique isomorphism respecting \(\otimes\). In particular:

- (T1) for any bases of \(V\) and \(V'\), the products of basis vectors form a basis of \(V\otimes V'\);
- (T2) linear maps \(f:V\to U\) and \(g:V'\to U'\) give a linear map \(f\otimes g\) with \(x\otimes y\mapsto f(x)\otimes g(y)\); if \(f\) and \(g\) are injective, so is \(f\otimes g\), because bases of \(V\) and \(V'\) map to linearly independent sets, which extend to bases of \(U\) and \(U'\) by Lemma 1.1;
- (T3) the *flip* \(\tau:V\otimes V\to V\otimes V\), \(x\otimes y\mapsto y\otimes x\), is linear, and a tensor \(T\) is *symmetric* if \(\tau T=T\).

If \(F\subseteq\mathbb R\) is a subfield, then \(F\otimes F\) is a commutative ring with \((a\otimes b)(a'\otimes b')=aa'\otimes bb'\), and \(m_F(a\otimes b)=ab\) is a ring homomorphism onto \(F\). By (T2) the inclusion \(F\otimes F\to\mathbb R\otimes\mathbb R\) is injective. The map \(m_F\) is usually not injective: in \(\mathbb Q(\sqrt2)\otimes\mathbb Q(\sqrt2)\) the element \(\sqrt2\otimes\sqrt2-2\otimes1\) is nonzero, by (T1) with the basis \(1,\sqrt2\), but its product is zero.

## 2. The criterion in terms of affine functions

Keep \(A=\{a_1,\dots,a_s\}\subset\mathbb R^d\), with \(s\ge2\) and affine span \(\mathbb R^d\). Let \(W=\mathbb R\times\mathbb R^d\), regarded as a vector space over \(\mathbb Q\). An element \(w=(v,u)\in W\) stands for the affine function \(a\mapsto v+a\cdot u\) on \(\mathbb R^d\), with *gradient* \(u\). For each point define the \(\mathbb Q\)-linear evaluation
\[
e_i:W\to\mathbb R,\qquad e_i(v,u)=v+a_i\cdot u .
\]
Let \(\mathcal T(W)\subseteq W\otimes W\) be the subspace of symmetric tensors. The map \((v,u)\otimes(v',u')\mapsto u\,u'^{\mathsf T}\) is well defined and \(\mathbb Q\)-linear on \(W\otimes W\), by the universal property, and its restriction to \(\mathcal T(W)\) is called \(G:\mathcal T(W)\to\mathrm{Sym}_d(\mathbb R)\); thus \(G(w\otimes w)=uu^{\mathsf T}\).

**Tensor condition.** There is \(T\in\mathcal T(W)\) with
\[
\begin{gathered}
(e_i\otimes e_i)(T)=0\quad(1\le i\le s),\\
G(T)=I_d .
\end{gathered}
\]
The first equations hold in \(\mathbb R\otimes\mathbb R\), before multiplication.

**Proposition 2.1.** The matrix condition of the classification theorem holds if and only if the tensor condition holds.

*Proof.* Write \(\mathscr B=\mathbb R\otimes\mathbb R\), with flip \(\tau\) and multiplication \(m_{\mathbb R}:\mathscr B\to\mathbb R\). Using the coordinates of \(W=\mathbb R^{1+d}\), an element of \(W\otimes W\) is the same as an array \(Q=(Q_{\alpha\beta})_{0\le\alpha,\beta\le d}\) over \(\mathscr B\): the coordinate tensor \(\varepsilon_\alpha\otimes\varepsilon_\beta\) with coefficient \(x\otimes y\) corresponds to the array with the single entry \(x\otimes y\) at \((\alpha,\beta)\). In these terms
\[
\begin{aligned}
&(e_i\otimes e_i)(Q)\\
&\quad=\sum_{\alpha,\beta}(p_{i\alpha}\otimes1)\,Q_{\alpha\beta}\,(1\otimes p_{i\beta}),
\end{aligned}
\]
and the gradient matrix of \(Q\) is the block \((m_{\mathbb R}(Q_{\alpha\beta}))_{1\le\alpha,\beta\le d}\). The flip becomes \(Q^*_{\alpha\beta}=\tau(Q_{\beta\alpha})\).

*From a matrix to a tensor.* Let \(P\) satisfy the matrix condition, and view it as an array over \(\mathscr B\) through the inclusion \(B\subseteq\mathscr B\). From the evaluation formula, \((e_i\otimes e_i)(P^*)=\tau\bigl((e_i\otimes e_i)(P)\bigr)=0\), and the multiplied spatial block of \(P^*\) is the transpose of that of \(P\), namely \(I_d\). So \(T=\frac12(P+P^*)\) is symmetric and satisfies the tensor condition.

*From a tensor to a matrix.* Let an array \(Q\) over \(\mathscr B\) satisfy the evaluation equations and have multiplied spatial block \(I_d\). Choose a basis \((r_\lambda)_{\lambda\in\Lambda}\) of \(\mathbb R\) over the field \(F\) (Lemma 1.1 over \(F\)). By (T1), applied over \(\mathbb Q\) to the bases \(\{c\,r_\lambda\}\) formed from a \(\mathbb Q\)-basis of \(F\), every element of \(\mathscr B\) can be written uniquely as \(\sum_{\lambda,\mu}(r_\lambda\otimes r_\mu)\,b_{\lambda\mu}\) with \(b_{\lambda\mu}\in B\), finitely many nonzero; here \(B\) acts on \(\mathscr B\) by multiplication. So
\[
\begin{gathered}
Q=\sum_{(\lambda,\mu)\in J}(r_\lambda\otimes r_\mu)\,P^{\lambda\mu},\\
P^{\lambda\mu}\in\mathrm{Mat}_{d+1}(B),
\end{gathered}
\]
for a finite set \(J\). The coefficients \(p_{i\alpha}\otimes1\) and \(1\otimes p_{i\beta}\) lie in \(B\), so by uniqueness of the expansion each \(P^{\lambda\mu}\) satisfies the evaluation equations. Let \(C^{\lambda\mu}\in\mathrm{Mat}_d(F)\) be the multiplied spatial block of \(P^{\lambda\mu}\). Multiplying the expansion gives
\[
I_d=\sum_{(\lambda,\mu)\in J}r_\lambda r_\mu\,C^{\lambda\mu} .
\]
This is a finite system of linear equations for the unknown scalars \(r_\lambda r_\mu\), with coefficients and right side in \(F\). It has a real solution, so Gaussian elimination over \(F\) gives a solution \(c_{\lambda\mu}\in F\) with \(I_d=\sum c_{\lambda\mu}C^{\lambda\mu}\). Then \(P=\sum(c_{\lambda\mu}\otimes1)P^{\lambda\mu}\) satisfies the evaluation equations, and its multiplied spatial block is \(\sum c_{\lambda\mu}C^{\lambda\mu}=I_d\). \(\square\)

**Remark 2.2** (congruent representatives). Let \(a_i'=Ra_i+t\) with \(R\) orthogonal. The invertible \(\mathbb Q\)-linear map \(\Theta(v,u)=(v-t\cdot Ru,\,Ru)\) of \(W\) satisfies \(e_i'\circ\Theta=e_i\), where \(e_i'\) is the evaluation at \(a_i'\), and \(G((\Theta\otimes\Theta)T)=R\,G(T)R^{\mathsf T}\). So \(\Theta\otimes\Theta\) carries tensors certifying \(A\) to tensors certifying \(A'\), and \(\Theta^{-1}\) goes back. Two copies of \(A\) in \(\mathbb R^d\) that span \(\mathbb R^d\) differ by such a map (Lemma 1.1 of the next lesson), so the tensor condition, and with Proposition 2.1 the matrix condition, does not depend on the chosen copy, although the fields \(F\) of two copies may differ.

## 3. A sphere through the points

**Proposition 3.1.** If \(A=\{a_1,\dots,a_s\}\subset\mathbb R^d\), with \(s\ge2\) and affine span \(\mathbb R^d\), satisfies the matrix condition, then \(A\) lies on a sphere.

*Proof.* Let \(P\) be a matrix as in the theorem and \(H=m_F(P)\), entrywise. Multiplying the evaluation equations gives \(p_i^{\mathsf T}Hp_i=0\), that is,
\[
\begin{gathered}
\|a_i\|^2+\ell\cdot a_i+c=0,\\
c=H_{00},\qquad\ell_\alpha=H_{0\alpha}+H_{\alpha0},
\end{gathered}
\]
for every \(i\), because the spatial block of \(H\) is \(I_d\). So the points lie on the set of \(x\) with \(\|x+\ell/2\|^2=\|\ell\|^2/4-c\). This set contains two distinct points, so the right side is positive, and it is a sphere. \(\square\)

With the necessity direction of the theorem (next lesson), Proposition 3.1 recovers the theorem of Erdős, Graham, Montgomery, Rothschild, Spencer and Straus that every Ramsey set lies on a sphere.

## 4. Exercises

**4.1** (easy). Show directly that a Ramsey set remains Ramsey after scaling by any positive factor, and that every nonempty subset of a Ramsey set is Ramsey.

**4.2** (medium). Let \(A=\{0,1\}\subset\mathbb R\). Show that
\[
\begin{aligned}
T=\tfrac12\bigl[{}&(0,1)\otimes(0,1)\\
&+(1,-1)\otimes(1,-1)\\
&-(1,0)\otimes(1,0)\bigr]
\end{aligned}
\]
satisfies the tensor condition.

**4.3** (medium). Let \(F=\mathbb Q(\sqrt2)\). Show that the ring \(F\otimes F\) is not a field, by exhibiting a zero divisor.

**4.4** (easy). In the proof of Proposition 2.1, why is it necessary to solve the linear system over \(F\), rather than to use the real numbers \(r_\lambda r_\mu\) directly as coefficients?

## 5. Solutions

**4.1.** If \(c\) is a colouring of \(\mathbb R^D\) and \(\kappa>0\), then \(x\mapsto c(\kappa x)\) is a colouring; a monochromatic copy of \(A\) for it gives, after multiplication by \(\kappa\), a monochromatic copy of \(\kappa A\) for \(c\). A monochromatic copy of \(A\) contains a monochromatic copy of each subset.

**4.2.** Here \(d=1\), \(e_1(v,u)=v\) and \(e_2(v,u)=v+u\). The gradients are \(1,-1,0\), so \(G(T)=\frac12(1+1-0)=1\). At \(a_1=0\) the three evaluations are \(0,1,1\), and \((e_1\otimes e_1)(T)\) is \(\frac12(0+1\otimes1-1\otimes1)=0\). At \(a_2=1\) they are \(1,0,1\), and \((e_2\otimes e_2)(T)\) is \(\frac12(1\otimes1+0-1\otimes1)=0\). The tensor is symmetric because each term is.

**4.3.** Put \(x=\sqrt2\otimes1+1\otimes\sqrt2\) and \(y=\sqrt2\otimes1-1\otimes\sqrt2\). Then \(xy=2\otimes1-1\otimes2=0\), since \(1\otimes2=2(1\otimes1)=2\otimes1\). By (T1) with the basis \(1,\sqrt2\), neither \(x\) nor \(y\) is zero.

**4.4.** The coefficients of the matrix \(P\) must lie in \(B=F\otimes F\). The element \(c\otimes1\) lies in \(B\) only for \(c\in F\); a real number such as \(r_\lambda r_\mu\) need not lie in \(F\).

## References

- [OpenAI-ER] OpenAI, *A classification of finite Euclidean Ramsey configurations*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026
- [EGMRSS] P. Erdős, R. L. Graham, P. Montgomery, B. L. Rothschild, J. Spencer and E. G. Straus, *Euclidean Ramsey theorems I*, Journal of Combinatorial Theory, Series A 14 (1973), 341–363. https://doi.org/10.1016/0097-3165(73)90011-3
- [Graham] R. L. Graham, *Recent trends in Euclidean Ramsey theory*, Discrete Mathematics 136 (1994), 119–127. https://doi.org/10.1016/0012-365X(94)00110-5
- [LRW-T] I. Leader, P. A. Russell and M. Walters, *Transitive sets in Euclidean Ramsey theory*, Journal of Combinatorial Theory, Series A 119 (2012), 382–396; arXiv:1012.1350. https://arxiv.org/abs/1012.1350
- [LRW-K] I. Leader, P. A. Russell and M. Walters, *Transitive sets and cyclic quadrilaterals*, Journal of Combinatorics 2 (2011), 457–462; arXiv:1012.5468. https://arxiv.org/abs/1012.5468
- [Pal] D. Pálvölgyi, *A cyclic non-Ramsey heptagon*, arXiv:2609.23327 (2026). https://arxiv.org/abs/2609.23327
