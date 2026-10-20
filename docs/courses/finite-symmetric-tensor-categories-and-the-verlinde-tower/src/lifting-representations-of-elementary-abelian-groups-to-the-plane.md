# Lifting representations of elementary abelian groups to the plane

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson and the next prove the restricted tilting theorem, Theorem 5.2 of Lesson 1. Fix \(r\ge1\), put \(q=p^r\) and \(E_r=(\mathbb Z/p)^r\), and fix an injective homomorphism \(\iota\colon E_r\to U(k)\). Given a representation \(D\) of \(E_r\), we construct an \(\mathrm{SL}_2\)-equivariant vector bundle on the affine plane whose fibre at \((1,0)\) restricts to \(D\) along \(\iota\), and whose fibre at the origin, a representation of all of \(\mathrm{SL}_2\), has all highest weights below \(q\) (Proposition 4.2). The two fibres need not be related on restriction to \(E_r\); Lesson 4 compares them after tensoring with a Steinberg module.

**Prerequisites.** [*Rational representations of SL₂ and tilting modules*](rational-representations-of-sl2-and-tilting-modules.md), Sections 1 and 2. Coherent sheaves and vector bundles on varieties, and the dual of a coherent sheaf.

## 1. Lifting to the unipotent group

We keep the notation of Lesson 2: \(G=\mathrm{SL}_2\) over \(k\), \(U=\{u(t)\}\), \(h_a=\operatorname{diag}(a,a^{-1})\), and \(V=k^2\) with basis \(e_1,e_2\). The image of \(\iota\) is a subgroup \(\{u(t):t\in H\}\), where \(H\subset k\) is an additive subgroup of order \(q\), an \(\mathbb F_p\)-subspace of dimension \(r\).

**Lemma 1.1.** Every finite-dimensional representation \(D\) of \(E_r\) is the restriction along \(\iota\) of a rational \(U\)-module \(\widehat D\) of degree less than \(q\).

*Proof.* Write \(\rho_D(t)\) for the matrix by which \(\iota^{-1}(u(t))\) acts, for \(t\in H\). By Lagrange interpolation there is a unique matrix \(P(t)\) with polynomial entries of degree less than \(q\) such that \(P(t)=\rho_D(t)\) for all \(t\in H\). The polynomials \(P(t+s)\) and \(P(t)P(s)\) in two variables have degree less than \(q\) in \(t\) and in \(s\) separately, and they agree on \(H\times H\) because \(\rho_D\) is a homomorphism. A polynomial in two variables of degree less than \(q\) in each variable that vanishes on \(H\times H\) is zero: for each fixed \(s\in H\) it vanishes at the \(q\) points of \(H\) as a polynomial in \(t\), so its coefficients, which are polynomials in \(s\) of degree less than \(q\), vanish on \(H\) and are therefore zero. Hence \(P(t+s)=P(t)P(s)\), and \(P(0)=\rho_D(0)=1\). So \(u(t)\mapsto P(t)\) is a rational representation \(\widehat D\) of \(U\), of degree less than \(q\), whose restriction to the image of \(\iota\) is \(D\). \(\square\)

The lift is a construction on individual representations; it does not respect tensor products. In terms of coalgebras, evaluation at the points of \(H\) identifies the polynomials of degree less than \(q\), a subcoalgebra of the coordinate ring \(k[t]\) of \(U\), with the coordinate ring of the finite group \(H\), and \(\widehat D\) is \(D\) transported along this identification.

## 2. The associated bundle on the punctured plane

Let \(\mathbb A^2\) be the plane with coordinates \(x,y\), on which \(G\) acts linearly, and \(\mathbb A^2_\circ=\mathbb A^2\setminus\{0\}\). Put \(e_1=(1,0)\).

**Lemma 2.1.** The orbit map \(\pi\colon G\to\mathbb A^2_\circ\), \(g\mapsto ge_1\), is surjective, its fibres are the cosets \(gU\), and it has the sections
\[
\begin{gathered}
s_x(x,y)=\begin{pmatrix}x&0\\y&x^{-1}\end{pmatrix}\ \text{on }\{x\ne0\},\\
s_y(x,y)=\begin{pmatrix}x&-y^{-1}\\y&0\end{pmatrix}\ \text{on }\{y\ne0\}.
\end{gathered}
\]
On the overlap, \(s_x^{-1}s_y=u(-1/(xy))\).

*Proof.* The vector \(ge_1\) is the first column of \(g\). A matrix of determinant one with first column \(e_1\) has the form \(\bigl(\begin{smallmatrix}1&b\\0&1\end{smallmatrix}\bigr)\), so the stabilizer of \(e_1\) is \(U\) and the fibres of \(\pi\) are the cosets \(gU\). Both displayed matrices have determinant one and first column \((x,y)\). The last formula is Exercise 6.3. \(\square\)

So \(\pi\) is a principal \(U\)-bundle, trivial over the two open sets \(\{x\ne0\}\) and \(\{y\ne0\}\). For a rational \(U\)-module \(\widehat D\), the *associated bundle* \(\mathcal E=G\times^U\widehat D\) is the quotient of \(G\times\widehat D\) by \((gu,d)\sim(g,ud)\); its class of \((g,d)\) is written \([g,d]\). Concretely, \(\mathcal E\) is the vector bundle on \(\mathbb A^2_\circ\) that is trivial with fibre \(\widehat D\) over \(\{x\ne0\}\) and over \(\{y\ne0\}\), via \((w,d)\mapsto[s_x(w),d]\) and \((w,d)\mapsto[s_y(w),d]\), glued on the overlap by the regular matrix function \(\rho_{\widehat D}(u(-1/(xy)))\). The group \(G\) acts by \(g'[g,d]=[g'g,d]\), which makes \(\mathcal E\) a \(G\)-equivariant vector bundle.

The fibre of \(\mathcal E\) at \(e_1\) is \(\{[u,d]\}=\{[1,d]\}\), identified with \(\widehat D\) by \(d\mapsto[1,d]\). The stabilizer \(U\) of \(e_1\) acts on it by \(u'[1,d]=[u',d]=[1,u'd]\): the fibre at \(e_1\) is \(\widehat D\) as a \(U\)-module.

## 3. Extension across the origin

**Theorem 3.1** (named result N4: reflexive sheaves [Stacks, Tags 0G41, 0AY4, 0B3N and 0EBJ]). Let \(X\) be an integral noetherian scheme.

1. If \(W\subset X\) is open, every coherent sheaf on \(W\) is the restriction of a coherent sheaf on \(X\) (Lemma 28.23.5).
2. If \(\mathcal G\) is coherent and reflexive, then \(\mathcal{H}om(\mathcal F,\mathcal G)\) is reflexive for every coherent \(\mathcal F\); in particular the double dual \(\mathcal F^{**}\) of a coherent sheaf is reflexive (Lemma 31.13.8).
3. If \(X\) is regular of dimension at most two, a coherent sheaf is reflexive if and only if it is locally free (Lemma 31.13.15).
4. Let \(j\colon W\to X\) be open with complement \(Z\), and suppose the local ring of \(X\) at every point of \(Z\) has depth at least two. Then \(j^*\) and \(j_*\) are inverse equivalences between coherent reflexive sheaves on \(X\) and on \(W\) (Lemma 31.13.12).

On a regular scheme, the local ring at a point of codimension at least two is regular of dimension at least two, so it has depth at least two. This applies to the origin of \(\mathbb A^2\), and to the points of \(Y\times\{0\}\) in \(Y\times\mathbb A^2\) for a smooth variety \(Y\).

**Proposition 3.2.** Let \(\mathcal E\) be a \(G\)-equivariant vector bundle on \(\mathbb A^2_\circ\). There is a \(G\)-equivariant vector bundle \(\mathcal M\) on \(\mathbb A^2\) whose restriction to \(\mathbb A^2_\circ\) is \(\mathcal E\) with its equivariant structure.

*Proof.* By Theorem 3.1(1) there is a coherent sheaf \(\mathcal F\) on \(\mathbb A^2\) with \(\mathcal F|_{\mathbb A^2_\circ}=\mathcal E\). Put \(\mathcal M=\mathcal F^{**}\). Duals commute with restriction to open sets, and \(\mathcal E\) is locally free, hence reflexive, so \(\mathcal M|_{\mathbb A^2_\circ}=\mathcal E^{**}=\mathcal E\). By Theorem 3.1(2) and (3), \(\mathcal M\) is locally free.

Let \(a,\mathrm{pr}\colon G\times\mathbb A^2\to\mathbb A^2\) be the action and the projection. The equivariant structure of \(\mathcal E\) is an isomorphism \(\phi\colon\mathrm{pr}^*\mathcal E\to a^*\mathcal E\) over \(G\times\mathbb A^2_\circ\) satisfying the identity and cocycle conditions. The sheaves \(\mathrm{pr}^*\mathcal M\) and \(a^*\mathcal M\) are locally free on the smooth variety \(G\times\mathbb A^2\), so \(\mathcal Hom(\mathrm{pr}^*\mathcal M,a^*\mathcal M)\) is locally free, hence reflexive. The complement of \(G\times\mathbb A^2_\circ\) is \(G\times\{0\}\), of codimension two, so by Theorem 3.1(4) the sections \(\phi\) and \(\phi^{-1}\) extend uniquely to sections over \(G\times\mathbb A^2\). Their composites are the identity over \(G\times\mathbb A^2_\circ\), hence everywhere by uniqueness. The identity and cocycle conditions hold over the dense open sets \(\mathbb A^2_\circ\) and \(G\times G\times\mathbb A^2_\circ\), and by the same uniqueness over \(\mathbb A^2\) and \(G\times G\times\mathbb A^2\). \(\square\)

The origin is fixed by \(G\), so the fibre \(\mathcal M_0\) of \(\mathcal M\) at \(0\) is a rational \(G\)-module.

## 4. The weights at the origin

**Lemma 4.1.** Let \(\mathcal M\) be a \(G\)-equivariant vector bundle on \(\mathbb A^2\) whose fibre at \(e_1\), as a \(U\)-module, has degree less than \(q\). Then the \(U\)-module \(\mathcal M_0\) has degree less than \(q\), and every composition factor \(L(h)\) of the \(G\)-module \(\mathcal M_0\) has \(h<q\).

*Proof.* The line \(\ell=ke_1=\{y=0\}\) is fixed pointwise by \(U\), since \(u(t)(x,0)=(x,0)\). For \(a\in k^\times\) the stabilizer of \(ae_1\) is also \(U\), and
\[
h_a^{-1}u(t)h_a=u(a^{-2}t),\qquad h_ae_1=ae_1.
\]
Let \(b\colon\mathcal M_{e_1}\to\mathcal M_{ae_1}\) be the action of \(h_a\) on fibres. Equivariance gives \(\rho_{ae_1}(u(t))=b\,\rho_{e_1}(u(a^{-2}t))\,b^{-1}\), so the \(U\)-module \(\mathcal M_{ae_1}\) has degree less than \(q\) for every \(a\ne0\).

The restriction of \(\mathcal M\) to \(\ell\cong\mathbb A^1\) is a vector bundle on the affine line, given by a finitely generated projective \(k[x]\)-module, which is free because \(k[x]\) is a principal ideal domain. In a basis of sections, the action of \(U\), which fixes \(\ell\) pointwise, is a matrix \(C(x,t)\) with entries in \(k[x,t]\). Write \(C(x,t)=\sum_jB_j(x)t^j\). For \(j\ge q\) and every \(a\ne0\), the matrix \(B_j(a)\) vanishes by the previous paragraph, so the polynomial entries of \(B_j\) have infinitely many zeros and \(B_j=0\). At \(x=0\), the matrix \(C(0,t)\) is the action of \(U\) on \(\mathcal M_0\), which therefore has degree less than \(q\). The last claim is Corollary 2.4 of Lesson 2. \(\square\)

**Proposition 4.2** ([OpenAI-208, Proposition 3.2]). For every finite-dimensional representation \(D\) of \(E_r\) there is a \(G\)-equivariant vector bundle \(\mathcal M\) on \(\mathbb A^2\) such that the action of the stabilizer \(U\) on the fibre \(\mathcal M_{e_1}\) restricts along \(\iota\) to \(D\), and every composition factor of the rational \(G\)-module \(\mathcal M_0\) is \(L(h)\) with \(h<q\).

*Proof.* Lemma 1.1 gives a rational \(U\)-module \(\widehat D\) of degree less than \(q\) restricting to \(D\). Section 2 gives the \(G\)-equivariant bundle \(\mathcal E=G\times^U\widehat D\) on \(\mathbb A^2_\circ\), with fibre \(\widehat D\) at \(e_1\). Proposition 3.2 extends it to \(\mathcal M\) on \(\mathbb A^2\) without changing the fibre at \(e_1\). Lemma 4.1 bounds the highest weights of \(\mathcal M_0\). \(\square\)

The argument applies unchanged for \(p=2\).

## 5. Exercises

**5.1.** Let \(p=2\), \(r=1\), \(H=\{0,1\}\), and let \(D\) be the two-dimensional representation of \(\mathbb Z/2\) in which the generator acts by \(\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)\). Find \(\widehat D\), and identify it with the restriction of a \(G\)-module.

**5.2.** Let \(p\) be odd, \(r=1\), \(H=\mathbb F_p\), and let \(D=J_i\) be the Jordan block representation of \(\mathbb Z/p\) of dimension \(i\le p\), where the generator acts by \(1+N\) with \(N\) nilpotent. Show that \(P(t)=\sum_{j=0}^{i-1}\binom tjN^j\), with \(\binom tj=t(t-1)\cdots(t-j+1)/j!\), is the lift of Lemma 1.1.

**5.3.** Verify the formula \(s_x^{-1}s_y=u(-1/(xy))\) of Lemma 2.1, and write down the transition function of \(\mathcal E\).

**5.4.** Suppose that \(\widehat D\) is the restriction to \(U\) of a rational \(G\)-module \(W\). Show that \([g,d]\mapsto(ge_1,gd)\) is a \(G\)-equivariant isomorphism from \(\mathcal E\) to the trivial bundle \(\mathbb A^2_\circ\times W\) with the diagonal action, and conclude that one may take \(\mathcal M=\mathbb A^2\times W\) and \(\mathcal M_0=W\).

## 6. Solutions

**5.1.** The interpolating polynomial matrix of degree less than \(2\) with \(P(0)=1\) and \(P(1)=\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)\) is \(P(t)=\bigl(\begin{smallmatrix}1&t\\0&1\end{smallmatrix}\bigr)=u(t)\). So \(\widehat D\) is the restriction of \(V\) to \(U\).

**5.2.** Each \(\binom tj\) with \(j\le i-1\le p-1\) is a polynomial of degree \(j<p=q\), since \(j!\) is invertible in \(k\). For \(t\in\mathbb F_p\), represented by an integer \(0\le t<p\), the binomial theorem gives \((1+N)^t=\sum_j\binom tjN^j\), and \(N^j=0\) for \(j\ge i\). So \(P(t)=\rho_D(t)\) on \(H\), and by the uniqueness of the interpolation \(P\) is the lift.

**5.3.** With \(s_x^{-1}=\bigl(\begin{smallmatrix}x^{-1}&0\\-y&x\end{smallmatrix}\bigr)\),
\[
\begin{aligned}
s_x^{-1}s_y&=\begin{pmatrix}x^{-1}&0\\-y&x\end{pmatrix}\begin{pmatrix}x&-y^{-1}\\y&0\end{pmatrix}\\
&=\begin{pmatrix}1&-x^{-1}y^{-1}\\0&1\end{pmatrix}.
\end{aligned}
\]
A point of \(\mathcal E\) over \(w\) in the overlap is \([s_y(w),d]\)\(=[s_x(w)\,s_x^{-1}s_y(w),d]\)\(=[s_x(w),\rho_{\widehat D}(u(-1/(xy)))d]\). So the coordinate \(d\) in the second chart corresponds to \(\rho_{\widehat D}(u(-1/(xy)))d\) in the first, and this matrix function is the transition function.

**5.4.** The map is well defined: \([gu,u^{-1}d]\mapsto(gue_1,gd)=(ge_1,gd)\). It is linear on fibres and commutes with the action of \(G\). Its inverse sends \((w,v)\) to \([s(w),s(w)^{-1}v]\) for either local section \(s\), which is independent of the section because two sections differ by an element of \(U\). The trivial bundle \(\mathbb A^2\times W\) with the diagonal action is a \(G\)-equivariant vector bundle on \(\mathbb A^2\) extending it, with fibre \(W\) at the origin.

## Sources

- [OpenAI-208] OpenAI, *Fiber functors for finite symmetric tensor categories in positive characteristic*, OpenAI Math Release preprint, 24 September 2026, Section 3.1 (Proposition 3.2 and its proof). https://github.com/openai/math/tree/main/preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026
- [Stacks] The Stacks Project Authors, *The Stacks Project*: Lemma 28.23.5 (Tag 0G41), Lemma 31.13.8 (Tag 0AY4), Lemma 31.13.15 (Tag 0B3N) and Lemma 31.13.12 (Tag 0EBJ). https://stacks.math.columbia.edu
