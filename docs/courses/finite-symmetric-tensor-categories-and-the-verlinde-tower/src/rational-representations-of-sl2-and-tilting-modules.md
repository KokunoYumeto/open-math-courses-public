# Rational representations of SL₂ and tilting modules

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The higher Verlinde categories are built from tilting modules of \(\mathrm{SL}_2\), and the main new theorem of the course, Theorem 5.2 of Lesson 1, is a statement about them. This lesson collects the representation theory of \(\mathrm{SL}_2\) over a field of characteristic \(p\) that the course uses. The classification of simple modules, Steinberg's tensor product theorem, the vanishing of extensions between Weyl and costandard modules, and Donkin's formula are taken from the literature (named result N3). Everything else is proved: the simplicity of small symmetric powers, the degree of the unipotent action on a simple module, the good filtrations of tensor products, and the lemma that tensoring with a Steinberg module makes a module with bounded highest weights tilting [BEO, Lemma 3.3].

**Prerequisites.** [*Finite symmetric tensor categories and fibre functors*](finite-symmetric-tensor-categories-and-fibre-functors.md), Sections 1 and 4. [*Representations of sl(2)*](course:RT-LIE/RT-LIE-05) for comparison with characteristic zero.

## 1. Rational modules, weights and degree

Let \(k\) be algebraically closed of characteristic \(p>0\), \(G=\mathrm{SL}_2\) over \(k\), and \(V=k^2\) the standard module with basis \(e_1,e_2\). Put
\[
u(t)=\begin{pmatrix}1&t\\0&1\end{pmatrix},\qquad h_a=\begin{pmatrix}a&0\\0&a^{-1}\end{pmatrix},
\]
and let \(U=\{u(t)\}\cong\mathbb G_a\) and \(H=\{h_a\}\cong\mathbb G_m\). A *rational \(G\)-module* is a finite-dimensional comodule over the coordinate ring of \(G\), that is, a representation whose matrix coefficients are regular functions on \(G\). Unless said otherwise, modules are finite dimensional. A rational \(U\)-module \(M\) is given, in a basis, by a matrix
\[
\begin{gathered}
\rho_M(u(t))=\sum_{j=0}^NA_jt^j,\\
A_j\in M_{\dim M}(k),
\end{gathered}
\]
with \(A_0=1\) and \(\rho_M(u(t+s))=\rho_M(u(t))\rho_M(u(s))\). The *weights* of a rational \(G\)-module \(M\) are the integers \(j\) with \(M_j=\{m:h_am=a^jm\text{ for all }a\}\ne0\), and \(M=\bigoplus_jM_j\).

**Definition 1.1.** The *degree* \(\deg M\) of a rational \(U\)-module \(M\ne0\) is the largest degree in \(t\) of an entry of \(\rho_M(u(t))\). The zero module has degree \(-\infty\).

**Lemma 1.2.**

1. The degree does not depend on the basis, and it does not increase on passing to submodules and quotient modules.
2. \(\deg(M\otimes N)\le\deg M+\deg N\).
3. Let \(F\colon G\to G\) be the Frobenius morphism, which raises matrix entries to the \(p\)-th power, and let \(M^{(i)}\) be the pullback of \(M\) along \(F^i\). Then \(\rho_{M^{(i)}}(u(t))=\rho_M(u(t^{p^i}))\), so \(\deg M^{(i)}=p^i\deg M\).
4. Every nonzero rational \(U\)-module \(M\) contains a nonzero vector fixed by \(U\).

*Proof.* (1) A change of basis replaces \(\rho_M(u(t))\) by \(C\rho_M(u(t))C^{-1}\) with \(C\) constant, which does not raise the degree; applying the inverse change shows that the degree is unchanged. In a basis extending a basis of a submodule \(M'\), the matrix is block upper triangular, with the matrices of \(M'\) and of \(M/M'\) as diagonal blocks. (2) In a tensor product basis, \(\rho_{M\otimes N}(u(t))\) is the Kronecker product of the two matrices, whose entries are products of entries. (3) \(F^i(u(t))=u(t^{p^i})\). (4) Since \(u(t)^p=u(pt)=1\), the operator \(\rho(u(t))-1\) satisfies \((\rho(u(t))-1)^p=\rho(u(t))^p-1=0\). The operators \(\rho(u(t))-1\), \(t\in k\), are nilpotent and commute. Commuting nilpotent operators on a nonzero space have a common nonzero kernel vector: the kernel of the first is nonzero and stable under the others, and induction on the dimension applies to the restrictions. As \(M\) is finite dimensional, finitely many of the operators span the linear space they generate, so a common kernel vector of those is fixed by \(U\). \(\square\)

## 2. Simple modules and Steinberg's tensor product theorem

**Theorem 2.1** (named result N3, part 1).

1. For each integer \(h\ge0\) there is a simple rational \(G\)-module \(L(h)\) whose largest weight is \(h\), occurring with multiplicity one, and every simple rational \(G\)-module is isomorphic to exactly one \(L(h)\) [Ric, Chapter 1, Theorem 1.16; Ste, Section 6].
2. (Steinberg's tensor product theorem.) For \(0\le a\le p-1\) and \(b\ge0\),
\[
L(a+pb)\cong L(a)\otimes L(b)^{(1)}
\]
[Ste, Theorem 1.1; Ric, Chapter 1, Theorem 2.12].

The number \(h\) is the *highest weight* of \(L(h)\). The simple modules with highest weight below \(p\) are symmetric powers of \(V\).

**Lemma 2.2.** For \(0\le a\le p-1\) the module \(\operatorname{Sym}^a(V)\) is simple, so \(\operatorname{Sym}^a(V)\cong L(a)\). Its only \(U\)-fixed vectors are the multiples of \(e_1^a\).

*Proof.* A vector \(v=\sum_ic_ie_1^ie_2^{a-i}\) satisfies
\[
\begin{aligned}
&u(t)v-v\\
&\quad=\sum_ic_i\sum_{j\ge1}\binom{a-i}{j}t^je_1^{i+j}e_2^{a-i-j}.
\end{aligned}
\]
Let \(i<a\) be the smallest index with \(c_i\ne0\), if there is one. The coefficient of \(t\,e_1^{i+1}e_2^{a-i-1}\) on the right is \(c_i(a-i)\), since only the term with index \(i\) and \(j=1\) contributes to it, and \(c_i(a-i)\ne0\) because \(0<a-i<p\). So a \(U\)-fixed vector is a multiple of \(e_1^a\).

Let \(W\) be a nonzero submodule. By Lemma 1.2(4) it contains a \(U\)-fixed vector, hence \(e_1^a\). The lower unitriangular matrix with entry \(s\) below the diagonal sends \(e_1^a\) to
\[
(e_1+se_2)^a=\sum_{j=0}^a\binom ajs^je_1^{a-j}e_2^j\in W.
\]
Since \(k\) is infinite, a Vandermonde argument in \(s\) shows that each term \(\binom aje_1^{a-j}e_2^j\) lies in \(W\), and \(\binom aj\ne0\) in \(k\) because \(a<p\). So \(W\) contains every monomial and \(W=\operatorname{Sym}^a(V)\). The weights of \(\operatorname{Sym}^a(V)\) are \(a,a-2,\dots,-a\), with \(e_1^a\) of weight \(a\), so it is \(L(a)\). \(\square\)

Write \(h=\sum_ih_ip^i\) with digits \(0\le h_i\le p-1\). Theorem 2.1(2) and Lemma 2.2, applied repeatedly, give
\[
L(h)\cong\bigotimes_i\operatorname{Sym}^{h_i}(V)^{(i)}.\tag{2.1}
\]

**Lemma 2.3.** The degree of \(L(h)\) as a \(U\)-module is \(h\).

*Proof.* On \(\operatorname{Sym}^{h_i}(V)\), the entries of \(\rho(u(t))\) have degree at most \(h_i\), and the coefficient of \(e_1^{h_i}\) in \(u(t)e_2^{h_i}=(e_2+te_1)^{h_i}\) is \(t^{h_i}\). By Lemma 1.2(3), on the twist by \(F^i\) the degrees are at most \(h_ip^i\), and the coefficient of \(e_1^{h_i}\) in the image of \(e_2^{h_i}\) is \(t^{h_ip^i}\). On the tensor product (2.1), Lemma 1.2(2) bounds the degree by \(\sum_ih_ip^i=h\), and the coefficient of \(\bigotimes_ie_1^{h_i}\) in the image of \(\bigotimes_ie_2^{h_i}\) is the product \(t^h\). \(\square\)

**Corollary 2.4.** If a rational \(G\)-module \(M\) has degree less than \(q\) as a \(U\)-module, then every composition factor \(L(h)\) of \(M\) has \(h<q\).

*Proof.* Composition factors are subquotients, so Lemma 1.2(1) and Lemma 2.3 give \(h\le\deg M<q\). \(\square\)

## 3. Costandard and Weyl modules

The determinant pairing \(V\otimes V\to k\), \(v\otimes w\mapsto\det(v,w)\), is \(G\)-invariant and nondegenerate, so \(V\cong V^*\). Put
\[
\begin{gathered}
\nabla(a)=\operatorname{Sym}^a(V^*),\\
\Delta(a)=\nabla(a)^*\qquad(a\ge0).
\end{gathered}
\]
These are the *costandard* and *Weyl* modules of highest weight \(a\) [Ric, Chapter 1, Section 1]. A *good filtration* of a module is a filtration by submodules whose successive quotients are costandard modules; a *Weyl filtration* is one whose successive quotients are Weyl modules. A module is *tilting* if it has both.

**Theorem 3.1** (named result N3, part 2).

1. \(\operatorname{Ext}^i_G(\Delta(a),\nabla(b))=0\) for all \(a,b\ge0\) and \(i\ge1\), extensions being taken in the category of rational \(G\)-modules [Ric, Chapter 1, Proposition 2.6].
2. A module \(M\) has a good filtration if and only if \(\operatorname{Ext}^1_G(\Delta(a),M)=0\) for all \(a\), and a Weyl filtration if and only if \(\operatorname{Ext}^1_G(M,\nabla(a))=0\) for all \(a\) [Ric, Chapter 4, Proposition 1.1].
3. For each \(a\ge0\) there is, up to isomorphism, a unique indecomposable tilting module \(T(a)\) with highest weight \(a\), and every tilting module is a direct sum of modules \(T(a)\) [Ric, Chapter 4, Theorem 1.5].

**Lemma 3.2.** If \(M\) has a Weyl filtration and \(N\) has a good filtration, then \(\operatorname{Ext}^1_G(M,N)=0\).

*Proof.* By induction on the lengths of the two filtrations, using the long exact sequences of \(\operatorname{Ext}\) in each variable, the claim reduces to \(M=\Delta(a)\), \(N=\nabla(b)\), which is Theorem 3.1(1). \(\square\)

**Lemma 3.3.** The classes of modules with good filtrations, with Weyl filtrations, and of tilting modules are closed under extensions, finite direct sums and direct summands.

*Proof.* Filtrations of the outer terms of a short exact sequence splice to a filtration of the middle term. Direct summands inherit the vanishing conditions of Theorem 3.1(2). \(\square\)

Write \(V^*\) with dual basis \(x,y\), so that \(\operatorname{Sym}(V^*)\otimes\operatorname{Sym}(V^*)\) is the polynomial ring \(k[x_1,y_1,x_2,y_2]\) on two copies of \(V^*\), and put \(d=x_1y_2-y_1x_2\), a \(G\)-invariant element of bidegree \((1,1)\).

**Lemma 3.4.** For \(a,b\ge1\) the sequence
\[
\begin{gathered}
0\to\nabla(a-1)\otimes\nabla(b-1)\\
\xrightarrow{\ \cdot d\ }\nabla(a)\otimes\nabla(b)\\
\xrightarrow{\ \mu\ }\nabla(a+b)\to0,
\end{gathered}
\]
with \(\mu\) the multiplication map \(x_1,x_2\mapsto x\), \(y_1,y_2\mapsto y\), is an exact sequence of \(G\)-modules. Consequently \(\nabla(a)\otimes\nabla(b)\) has a good filtration for all \(a,b\ge0\).

*Proof.* Both maps are \(G\)-equivariant, since \(d\) is invariant. Multiplication by \(d\) is injective in the polynomial ring, \(\mu\) is surjective, and \(\mu(d)=xy-yx=0\), so the image of the first map lies in the kernel of \(\mu\). The dimensions agree: \((a+1)(b+1)-(a+b+1)=ab\). For the consequence, induct on \(\min(a,b)\): if it is \(0\), the product is a single costandard module, and otherwise the sequence exhibits \(\nabla(a)\otimes\nabla(b)\) as an extension of \(\nabla(a+b)\) by \(\nabla(a-1)\otimes\nabla(b-1)\), which has a good filtration by induction. \(\square\)

**Proposition 3.5.** Tensor products of modules with good filtrations have good filtrations, tensor products of modules with Weyl filtrations have Weyl filtrations, and tensor products of tilting modules are tilting.

*Proof.* If \(M\) and \(N\) have good filtrations, \(M\otimes N\) has a filtration whose quotients are the modules \(\nabla(a)\otimes\nabla(b)\); Lemma 3.4 and Lemma 3.3 give a good filtration. The dual of a good filtration is a Weyl filtration and conversely, and \((M\otimes N)^*\cong M^*\otimes N^*\), which gives the second claim; the third combines the two. \(\square\)

## 4. Tilting modules and Steinberg modules

**Lemma 4.1.** For \(0\le a\le p-1\) the modules \(\nabla(a)\), \(\Delta(a)\) and \(L(a)=\operatorname{Sym}^a(V)\) are isomorphic, and they are \(T(a)\).

*Proof.* The isomorphism \(V^*\cong V\) gives \(\nabla(a)\cong\operatorname{Sym}^a(V)=L(a)\). The pairing \(\operatorname{Sym}^a(V^*)\otimes\operatorname{Sym}^a(V)\to k\) that sends \(f_1\cdots f_a\otimes v_1\cdots v_a\) to \(\sum_{\sigma\in S_a}\prod_if_i(v_{\sigma(i)})\) is \(G\)-invariant, and in monomial bases it is diagonal with entries \(i!\,(a-i)!\), which are nonzero in \(k\) because \(a<p\). So \(\operatorname{Sym}^a(V^*)^*\cong\operatorname{Sym}^a(V)\), that is, \(\Delta(a)\cong L(a)\). A module isomorphic to both \(\nabla(a)\) and \(\Delta(a)\) is tilting, and \(L(a)\) is indecomposable with highest weight \(a\). \(\square\)

The *Steinberg modules* are \(\operatorname{St}_m=L(p^m-1)\) for \(m\ge0\). Since the digits of \(p^m-1\) are all \(p-1\), formula (2.1) gives
\[
\begin{gathered}
\operatorname{St}_m\cong\bigotimes_{j=0}^{m-1}\operatorname{St}_1^{(j)},\\
\operatorname{St}_1=\operatorname{Sym}^{p-1}(V),\quad(4.1)
\end{gathered}
\]
so \(\operatorname{St}_0=k\), \(\operatorname{St}_m\cong\operatorname{St}_1\otimes\operatorname{St}_{m-1}^{(1)}\), and \(\dim\operatorname{St}_m=p^m\).

**Theorem 4.2** (named result N3, part 3: Donkin's formula). For every \(b\ge0\),
\[
\operatorname{St}_1\otimes T(b)^{(1)}\cong T(p-1+pb)
\]
[Ric, Chapter 4, Proposition 1.15; BEO, Proposition 3.1(iii)].

## 5. Steinberg modules and bounded highest weights

**Lemma 5.1** ([BEO, Lemma 3.3]). Let \(m\ge0\) and let \(M\) be a rational \(G\)-module all of whose composition factors are \(L(h)\) with \(0\le h<p^{m+1}\). Then \(\operatorname{St}_m\otimes M\) is tilting.

*Proof.* Tensoring a composition series of \(M\) with \(\operatorname{St}_m\) gives a filtration of \(\operatorname{St}_m\otimes M\) with quotients \(\operatorname{St}_m\otimes L(h)\). By Lemma 3.3 it suffices to show that each of these is tilting. We induct on \(m\). For \(m=0\), \(\operatorname{St}_0\otimes L(h)=L(h)\) with \(h<p\), which is tilting by Lemma 4.1.

Let \(m\ge1\) and write \(h=d+ph'\) with \(0\le d\le p-1\) and \(h'<p^m\). By Theorem 2.1(2) and (4.1),
\[
\begin{aligned}
&\operatorname{St}_m\otimes L(h)\\
&\quad\cong L(d)\otimes\operatorname{St}_1\otimes\bigl(\operatorname{St}_{m-1}\otimes L(h')\bigr)^{(1)},
\end{aligned}
\]
because the twist \((-)^{(1)}\) commutes with tensor products. Since \(h'<p^{(m-1)+1}\), the induction hypothesis makes \(\operatorname{St}_{m-1}\otimes L(h')\) tilting, so it is a direct sum of modules \(T(b)\) by Theorem 3.1(3). Theorem 4.2 makes each \(\operatorname{St}_1\otimes T(b)^{(1)}\) tilting. Finally \(L(d)=T(d)\) by Lemma 4.1, and Proposition 3.5 shows that the tensor product with it is tilting. \(\square\)

## 6. Exercises

**6.1.** Let \(p=2\). Show that the span of \(e_1^2\) and \(e_2^2\) is a submodule of \(\operatorname{Sym}^2(V)\) isomorphic to \(V^{(1)}=L(2)\), with trivial quotient. Compute \(\rho(u(t))\) on \(\operatorname{Sym}^2(V)\) and check that its degree is \(2\).

**6.2.** Let \(p=2\). Show that \(L(2)\) has no good filtration, so it is not tilting. Conclude that the bound \(h<p^{m+1}\) in Lemma 5.1 cannot be replaced by \(h\le p^{m+1}\) when \(m=0\).

**6.3.** Use Lemma 3.4 to write down a good filtration of \(\nabla(1)\otimes\nabla(1)\) and to compute its weights with multiplicities.

**6.4.** Let \(p=3\). Use Theorem 2.1(2), Lemma 4.1 and Theorem 4.2 to show that \(\operatorname{St}_1\otimes L(4)\cong L(1)\otimes T(5)\), and that this module is tilting. What is its dimension?

## 7. Solutions

**6.1.** In characteristic \(2\), \(u(t)e_1^2=e_1^2\), \(u(t)e_1e_2=e_1(e_2+te_1)=te_1^2+e_1e_2\) and \(u(t)e_2^2=(e_2+te_1)^2=e_2^2+t^2e_1^2\). For a general matrix \(g\) with \(ge_1=\alpha e_1+\gamma e_2\) and \(ge_2=\beta e_1+\delta e_2\), squaring gives \(ge_1^2=\alpha^2e_1^2+\gamma^2e_2^2\) and \(ge_2^2=\beta^2e_1^2+\delta^2e_2^2\), because the cross terms have coefficient \(2\). So the span of the squares is a submodule on which \(g\) acts by the matrix with squared entries, which is \(V^{(1)}\), and \(V^{(1)}\cong L(0)\otimes L(1)^{(1)}=L(2)\) by Theorem 2.1(2). The quotient is spanned by the image of \(e_1e_2\), of weight \(0\), so it is trivial. In the basis \(e_1^2,e_1e_2,e_2^2\) the matrix of \(u(t)\) has columns \((1,0,0)\), \((t,1,0)\), \((t^2,0,1)\), of degree \(2\).

**6.2.** The weights of \(L(2)=V^{(1)}\) are \(2\) and \(-2\), each with multiplicity one. The weights of \(\nabla(b)\) are \(b,b-2,\dots,-b\). A good filtration of \(L(2)\) would have quotients \(\nabla(b)\) whose weights, with multiplicity, add up to \(\{2,-2\}\); \(\nabla(0)\) and \(\nabla(2)\) contain the weight \(0\), and every other \(\nabla(b)\) contains a weight outside \(\{2,-2\}\). So there is no good filtration. With \(m=0\) and \(h=2=p^{m+1}\), the module \(\operatorname{St}_0\otimes L(2)=L(2)\) is not tilting.

**6.3.** With \(a=b=1\), Lemma 3.4 gives the exact sequence \(0\to\nabla(0)\to\nabla(1)\otimes\nabla(1)\to\nabla(2)\to0\), whose first map sends \(1\) to \(d=x_1y_2-y_1x_2\). So \(0\subset\nabla(0)\subset\nabla(1)\otimes\nabla(1)\) is a good filtration. The weights are \(2,0,0,-2\): the weights \(\pm1\) of \(\nabla(1)\) add in pairs.

**6.4.** Here \(\operatorname{St}_1=L(2)\) and \(4=1+3\cdot1\), so \(L(4)\cong L(1)\otimes L(1)^{(1)}\) by Theorem 2.1(2). Hence \(\operatorname{St}_1\otimes L(4)\cong L(1)\otimes\bigl(\operatorname{St}_1\otimes L(1)^{(1)}\bigr)\). By Lemma 4.1, \(L(1)=T(1)\), and Theorem 4.2 with \(b=1\) gives \(\operatorname{St}_1\otimes T(1)^{(1)}\cong T(2+3)=T(5)\). The module \(L(1)\otimes T(5)\) is tilting by Proposition 3.5. Its dimension is \(\dim\operatorname{St}_1\cdot\dim L(4)=3\cdot4=12\). This is the case \(m=1\), \(h=4<9\) of Lemma 5.1.

## Sources

- [OpenAI-208] OpenAI, *Fiber functors for finite symmetric tensor categories in positive characteristic*, OpenAI Math Release preprint, 24 September 2026, Section 3.1 (the degree of the unipotent action on simple modules), Section 3.2 (Steinberg modules and bounded weights) and Section 3.3 (good filtrations of tensor products). https://github.com/openai/math/tree/main/preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026
- [BEO] D. Benson, P. Etingof and V. Ostrik, *New incompressible symmetric tensor categories in positive characteristic*, Duke Math. J. 172 (2023), numbering of arXiv:2003.10499v4: Proposition 3.1 and Lemma 3.3. https://arxiv.org/abs/2003.10499v4
- [Ric] S. Riche, *Lectures on modular representation theory of reductive algebraic groups*, lecture notes: Chapter 1, Theorems 1.16 and 2.12 and Proposition 2.6; Chapter 4, Proposition 1.1, Theorem 1.5 and Proposition 1.15. https://riche.perso.math.cnrs.fr/curso-riche-total.pdf
- [Ste] R. Steinberg, *Representations of algebraic groups*, Nagoya Math. J. 22 (1963), 33–56, Theorem 1.1 and Section 6. https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/representations-of-algebraic-groups/02AE5498AF62BCAB6B313C75016E6015
- [DH] S. Doty and A. Henke, *Decomposition of tensor products of modular irreducibles for SL₂*, Quart. J. Math. 56 (2005), Lemma 1.1, for the form (2.1) of Steinberg's theorem. https://arxiv.org/abs/math/0205186
