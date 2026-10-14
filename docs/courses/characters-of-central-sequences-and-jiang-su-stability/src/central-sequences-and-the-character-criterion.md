# Central sequences and the character criterion

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A unital separable C\*-algebra \(A\) absorbs the Jiang–Su algebra \(\mathcal Z\) tensorially exactly when its central sequence algebra \(F_\omega(A)\) contains, with the same unit, a separable subhomogeneous subalgebra without characters (Kirchberg and Rørdam). A character of \(F_\omega(A)\) would restrict to a character of such a subalgebra, so the absence of characters on \(F_\omega(A)\) is necessary; Kirchberg and Rørdam asked whether it is sufficient [KR, Question 3.1]. This course proves the theorem of [OpenAI-KRC]: it is. The new ingredient is a finite theorem: every nonzero unital C\*-algebra without characters has a finite maximal tensor power that receives a unital homomorphism from the dimension-drop algebra \(I(2,3)\).

This lesson states the theorems, introduces the tools, and derives the main theorem and a corollary on infinite tensor powers from the finite theorem and two results from the literature, which are named hypotheses of the course.

- Ultrapowers, central sequences and characters (Section 1).
- The theorems and the named hypotheses (Section 2).
- Maximal tensor products (Lemma 3.1).
- Dimension-drop algebras, separable reduction and commuting copies (Lemmas 4.1 to 4.3).
- Proofs of the main theorem and the corollary (Section 5).

The course follows [OpenAI-KRC]. All algebras are complex. Facts on C\*-algebras are taken from the course [Foundations of von Neumann algebras](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones): continuous functional calculus (Theorem 5.1 there), positivity (Theorem 8.2 there), Gelfand's theorem for commutative algebras (Theorem 2.1 there) and quotients (Theorem 15.1 there).

## 1. Ultrapowers, central sequences and characters

Let \(\omega\) be a free ultrafilter on \(\mathbb N\) and \(A\) a nonzero unital C\*-algebra. The *ultrapower* is
\[
A_\omega=\ell^\infty(\mathbb N,A)\big/c_\omega(A),
\]
where \(c_\omega(A)\) is the closed ideal of bounded sequences with \(\lim_{n\to\omega}\|a_n\|=0\). The norm of the class of \((a_n)\) is \(\lim_{n\to\omega}\|a_n\|\) ([Norm ultrapowers and a group with property (T)](course:kirchbergs-embedding-problem/norm-ultrapowers-and-a-group-with-property-t), Lemma 2.2). Identify \(A\) with the classes of constant sequences. The *central sequence algebra* is
\[
F_\omega(A)=A_\omega\cap A',
\]
the classes commuting with every constant sequence; it is a unital C\*-subalgebra of \(A_\omega\), and it is nonzero since \(\|1\|=1\).

A *character* of a C\*-algebra is a nonzero \(*\)-homomorphism to \(\mathbb C\); on a unital algebra it sends \(1\) to \(1\). A C\*-algebra is *subhomogeneous* if the dimensions of its irreducible representations have a common finite bound. For integers \(p,q\ge1\), the *dimension-drop algebra* is
\[
\begin{aligned}
I(p,q)=\{f\in{}&C([0,1],M_p\otimes M_q):\\
&f(0)\in M_p\otimes1_q,\\
&f(1)\in1_p\otimes M_q\}.
\end{aligned}
\]
The *Jiang–Su algebra* \(\mathcal Z\), constructed by Jiang and Su, is a simple unital separable C\*-algebra; it is an inductive limit of dimension-drop algebras \(I(p,q)\) with \(p,q\) coprime, and it contains \(I(2,3)\) unitally [KR, Section 2]. This course uses \(\mathcal Z\) only through the two named hypotheses below. A C\*-algebra \(A\) is *\(\mathcal Z\)-stable* if \(A\cong A\otimes_{\min}\mathcal Z\).

## 2. The theorems and the named hypotheses

**Theorem 2.1** ([OpenAI-KRC, Theorem 1.1]). Let \(A\) be a nonzero unital separable C\*-algebra and \(\omega\) a free ultrafilter on \(\mathbb N\). Then \(F_\omega(A)\) has no characters if and only if \(A\cong A\otimes_{\min}\mathcal Z\).

**Theorem 2.2** (the finite theorem; [OpenAI-KRC, Theorem 1.2]). Let \(D\) be a nonzero unital C\*-algebra without characters. There are an integer \(m\ge1\) and a unital \(*\)-homomorphism
\[
I(2,3)\longrightarrow D^{\otimes_{\max}m}.
\]

**Corollary 2.3** (infinite tensor powers; [OpenAI-KRC, Corollary 1.3]). Let \(D\) be a nonzero unital separable C\*-algebra without characters, and let \(B=D^{\otimes_{\min}\infty}\) be the inductive limit of the algebras \(D^{\otimes_{\min}n}\) under the maps \(x\mapsto x\otimes1_D\). Then \(B\cong B\otimes_{\min}\mathcal Z\), and \(B\) contains a unital copy of \(\mathcal Z\).

In Theorem 2.2 the exponent \(m\) depends on \(D\), and the conclusion is a unital homomorphism, not \(\mathcal Z\)-stability of a finite tensor power. Its image is a quotient of \(I(2,3)\), hence subhomogeneous and without characters (Lemma 4.1), and this is what the applications need. Theorem 2.2 is proved in the lessons [The Rørdam–Winter criterion](the-rordam-winter-criterion.md) to [From the cone to the dimension-drop algebra](from-the-cone-to-the-dimension-drop-algebra.md); its proof uses no separability, nuclearity or trace.

The two results from the literature, which this course does not prove:

**Hypothesis (KR)** (Kirchberg–Rørdam, [KR, Theorem 2.5]). For a unital separable C\*-algebra \(A\) and a free ultrafilter \(\omega\), \(A\cong A\otimes_{\min}\mathcal Z\) if and only if \(F_\omega(A)\) contains, with the same unit, a separable subhomogeneous C\*-algebra without characters.

**Hypothesis (DT)** (Dadarlat–Toms, as stated in [KR, Theorem 2.4]). For a unital separable C\*-algebra \(A\), if \(A^{\otimes_{\min}\infty}\) contains, with the same unit, a subhomogeneous C\*-algebra without characters, then \(A^{\otimes_{\min}\infty}\cong A^{\otimes_{\min}\infty}\otimes_{\min}\mathcal Z\).

Both rest on the theory of the Jiang–Su algebra and of strongly self-absorbing algebras, which the programme does not contain.

## 3. Maximal tensor products

Let \(A\) and \(B\) be unital C\*-algebras with algebraic tensor product \(A\odot B\), a unital \(*\)-algebra. For \(x\in A\odot B\) put
\[
\|x\|_{\max}=\sup_\pi\|\pi(x)\|,
\]
the supremum over all \(*\)-representations \(\pi\) of \(A\odot B\) on Hilbert spaces. For \(x=\sum_ia_i\otimes b_i\), each \(a\mapsto\pi(a\otimes1)\) and \(b\mapsto\pi(1\otimes b)\) is a \(*\)-homomorphism of a C\*-algebra, hence contractive, so \(\|x\|_{\max}\le\sum_i\|a_i\|\|b_i\|\). The supremum is a C\*-seminorm, and a norm because it dominates the minimal norm \(\|\cdot\|_{\min}\), which is realized by a representation ([Tensor products of C\*-algebras and the minimal norm](course:tensor-products-of-operator-algebras/tensor-products-of-c-star-algebras-and-the-minimal-norm), Theorem 2.2). The completion is the *maximal tensor product* \(A\otimes_{\max}B\). For several factors \(A_1,\dots,A_k\) the same definition gives \(A_1\otimes_{\max}\cdots\otimes_{\max}A_k\), and \(D^{\otimes_{\max}k}\) is the \(k\)-th maximal tensor power.

**Lemma 3.1.** Let \(A_1,\dots,A_k\) be unital C\*-algebras and \(P=A_1\otimes_{\max}\cdots\otimes_{\max}A_k\).

1. (Universal property.) If \(\varphi_j\colon A_j\to E\) are unital \(*\)-homomorphisms into a unital C\*-algebra with pairwise commuting ranges, there is exactly one unital \(*\)-homomorphism \(P\to E\) with \(a_1\otimes\cdots\otimes a_k\mapsto\varphi_1(a_1)\cdots\varphi_k(a_k)\).
2. Each leg \(a\mapsto1\otimes\cdots\otimes a\otimes\cdots\otimes1\) is an injective unital \(*\)-homomorphism \(A_j\to P\), and the legs commute.
3. (Regrouping.) For a partition of \(\{1,\dots,k\}\) into consecutive blocks, \(P\) is canonically isomorphic to the maximal tensor product of the maximal tensor products of the blocks.
4. (Functoriality.) Unital \(*\)-homomorphisms \(\psi_j\colon A_j\to B_j\) give a unital \(*\)-homomorphism \(\psi_1\otimes\cdots\otimes\psi_k\) from \(P\) to \(B_1\otimes_{\max}\cdots\otimes_{\max}B_k\).
5. The identity of the algebraic tensor product extends to a surjective unital \(*\)-homomorphism \(P\to A_1\otimes_{\min}\cdots\otimes_{\min}A_k\).
6. Every irreducible representation \(\pi\) of \(P\) is unital, and its restrictions \(\pi_j\) to the legs are unital representations with pairwise commuting ranges.
7. For \(y\in A_1\otimes_{\max}A_2\) and \(c\in A_3\), \(\|y\otimes c\|\le\|y\|\|c\|\) in \(A_1\otimes_{\max}A_2\otimes_{\max}A_3\).

*Proof.* (1) Represent \(E\) faithfully on a Hilbert space (Gelfand–Naimark, [Building representations from positive functionals](course:foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark), Theorem 7.2). The formula defines a \(*\)-representation of the algebraic tensor product, whose norm is at most \(\|\cdot\|_{\max}\) by definition; it extends to \(P\). Uniqueness holds because elementary tensors span a dense subalgebra. (2) The legs are \(*\)-homomorphisms; they are injective because the minimal norm, which is at most the maximal one, restricts to the norm of \(A_j\) on each leg ([Tensor products of C\*-algebras and the minimal norm](course:tensor-products-of-operator-algebras/tensor-products-of-c-star-algebras-and-the-minimal-norm), Lemma 3.1). (3) Both algebras have the universal property (1) for commuting unital homomorphisms of \(A_1,\dots,A_k\), the second by applying (1) twice; the maps given by (1) in both directions are mutually inverse on elementary tensors. (4) Apply (1) to the legs of the target composed with the \(\psi_j\). (5) The minimal norm is at most the maximal norm on the algebraic tensor product. (6) \(\pi(1)\) is a projection commuting with \(\pi(P)\), hence a scalar by Schur's lemma ([Building representations from positive functionals](course:foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark), Corollary 2.3), and nonzero; so \(\pi(1)=1\). Compose with the legs of (2). (7) In every representation, \(\pi(y\otimes c)=\pi(y\otimes1)\pi(1\otimes1\otimes c)\), and both factors are images of \(*\)-homomorphisms of C\*-algebras. \(\blacksquare\)

## 4. Dimension-drop algebras, separable reduction and commuting copies

**Lemma 4.1.** Every irreducible representation of \(I(2,3)\) is unitarily equivalent to the evaluation at a point \(t\in[0,1]\), followed by the identity representation of \(M_2\otimes1\cong M_2\) if \(t=0\), of \(1\otimes M_3\cong M_3\) if \(t=1\), and of \(M_6\) otherwise. So \(I(2,3)\) is subhomogeneous and has no characters, and the same holds for every quotient of \(I(2,3)\).

*Proof.* The scalar functions \(g(t)1\), \(g\in C([0,1])\), lie in \(I(2,3)\) and are central. Let \(\pi\) be irreducible. By Schur's lemma \(\pi(\iota1)=t_0\) for the function \(\iota(t)=t\) and a number \(t_0\in[0,1]\), and then \(\pi(g1)=g(t_0)\) by the functional calculus. If \(F(t_0)=0\), let \(g_n(t)=\min\{1,n|t-t_0|\}\); then \(\|F-Fg_n\|\to0\) and \(\pi(Fg_n)=\pi(F)g_n(t_0)=0\), so \(\pi(F)=0\). Hence \(\pi\) factors through the evaluation at \(t_0\), whose image is \(M_2\otimes1\), \(1\otimes M_3\) or \(M_2\otimes M_3=M_6\): functions \(g(t)X\) with \(g\) vanishing at the endpoints and \(g(t_0)=1\) give every \(X\) at an interior point. An irreducible representation \(\rho\) of a matrix algebra \(M_n\) on \(H\) is equivalent to the identity representation: for a unit vector \(\xi\) in \(\rho(e_{11})H\), the vectors \(\rho(e_{i1})\xi\) are orthonormal and span an invariant subspace, which is \(H\). So the irreducible representations have dimensions \(2\), \(3\) and \(6\), and none is a character. For a quotient map \(q\colon I(2,3)\to E\), an irreducible representation or a character of \(E\), composed with \(q\), is one of \(I(2,3)\). \(\blacksquare\)

**Lemma 4.2** (separable reduction; [OpenAI-KRC, Lemma 6.1], after [KR, Lemma 3.5]). Every nonzero unital C\*-algebra \(B\) without characters contains a separable C\*-subalgebra without characters with the unit of \(B\).

*Proof.* Let \(J\) be the closed ideal generated by the commutators \([b,c]\) of self-adjoint elements. In \(B/J\) self-adjoint elements commute, so it is commutative; if \(J\ne B\), \(B/J\) is a nonzero unital commutative C\*-algebra, which has a character (Gelfand), and composing with the quotient map gives a character of \(B\). So \(J=B\), and some element of the algebraic ideal generated by the commutators is within distance less than \(1\) of \(1\):
\[
\Bigl\|1-\sum_{i=1}^rh_i[b_i,c_i]k_i\Bigr\|<1 .
\]
Let \(D\) be the C\*-algebra generated by \(1\) and the elements \(h_i,k_i,b_i,c_i\); it is separable and unital. A character \(\chi\) of \(D\) kills the commutators, so \(\chi\) of the displayed element \(1-\sum_i\dots\) equals \(1\), while characters are contractive. \(\blacksquare\)

**Lemma 4.3** (commuting copies; [OpenAI-KRC, Proposition 2.2(1)], after [KR, Corollary 2.3]). Let \(A\) be a nonzero unital separable C\*-algebra, \(\omega\) a free ultrafilter, and \(D\subseteq F_\omega(A)\) a separable C\*-subalgebra containing the unit. For every \(m\ge1\) there is a unital \(*\)-homomorphism \(D^{\otimes_{\max}m}\to F_\omega(A)\).

*Proof.* *One new copy.* Let \(E\subseteq F_\omega(A)\) be a separable C\*-subalgebra. We construct a unital \(*\)-homomorphism \(\theta\colon D\to F_\omega(A)\cap E'\). Let \(D_0\) be a countable dense unital \(*\)-subalgebra of \(D\) over \(\mathbb Q+i\mathbb Q\). For \(x\in D_0\) choose a representing sequence \((a^x_l)_l\) with \(\sup_l\|a^x_l\|\le2\|x\|\): since \(\|x\|=\lim_{l\to\omega}\|a_l\|\) for any representative, replacing the terms of norm larger than \(2\|x\|\) by \(0\) changes the sequence only on a set outside \(\omega\) (if \(x\ne0\)); take the zero sequence for \(x=0\) and the constant unit for \(x=1\). Choose a countable dense subset \(\{a_k\}\) of \(A\), a countable dense subset \(\{e_j\}\) of \(E\), and bounded representing sequences \((b^j_s)_s\) of the \(e_j\).

The following countably many *tests* hold along \(\omega\): the defects \(a^{x+y}_l-a^x_l-a^y_l\), \(a^{\lambda x}_l-\lambda a^x_l\), \(a^{xy}_l-a^x_la^y_l\), \(a^{x^*}_l-(a^x_l)^*\) and \([a^x_l,a_k]\) tend to \(0\) in norm as \(l\to\omega\), for \(x,y\in D_0\), \(\lambda\in\mathbb Q+i\mathbb Q\) and all \(k\). Enumerate the tests and the pairs \((x,j)\). For each \(s\), choose an index \(l(s)\) at which the first \(s\) tests hold within \(1/s\) and \(\|[a^x_{l(s)},b^j_s]\|<1/s\) for the first \(s\) pairs \((x,j)\). Such an index exists: each of these finitely many requirements holds on a set of indices \(l\) belonging to \(\omega\), the last ones because \(b^j_s\) is a fixed element of \(A\) and \(x\) commutes with \(A\) in \(A_\omega\); a finite intersection of sets of \(\omega\) is in \(\omega\), hence nonempty.

The sequences \((a^x_{l(s)})_s\) satisfy every test in the ordinary limit \(s\to\infty\), hence along \(\omega\); being bounded and asymptotically central for a dense subset of \(A\), their classes \(\theta(x)\) lie in \(F_\omega(A)\), and \(\|[\theta(x),e_j]\|=\lim_\omega\|[a^x_{l(s)},b^j_s]\|=0\), so \(\theta(x)\in E'\). On \(D_0\), \(\theta\) is a unital \(*\)-homomorphism over \(\mathbb Q+i\mathbb Q\), and \(\|\theta(x)-\theta(y)\|=\|\theta(x-y)\|\le2\|x-y\|\). It extends by continuity to a unital \(*\)-homomorphism on \(D\), complex linear by continuity of scalar multiplication.

*Commuting copies.* Let \(\theta_1\) be the inclusion of \(D\), and for \(i=2,\dots,m\) let \(\theta_i\) be the map just constructed for the C\*-algebra \(E\) generated by \(\theta_1(D),\dots,\theta_{i-1}(D)\). The ranges commute pairwise, and Lemma 3.1(1) gives the homomorphism. \(\blacksquare\)

## 5. Proofs of the main theorem and the corollary

*Proof of Theorem 2.1.* Suppose \(F_\omega(A)\) has no characters. It is nonzero and unital, so Lemma 4.2 gives a separable C\*-subalgebra \(D\subseteq F_\omega(A)\) without characters containing the unit. Theorem 2.2 and Lemma 4.3 give unital \(*\)-homomorphisms
\[
I(2,3)\longrightarrow D^{\otimes_{\max}m}\longrightarrow F_\omega(A).
\]
The image \(E\) of the composite is separable, contains the unit of \(F_\omega(A)\), and is a quotient of \(I(2,3)\), hence subhomogeneous and without characters (Lemma 4.1). Hypothesis (KR) gives \(A\cong A\otimes_{\min}\mathcal Z\). Conversely, if \(A\cong A\otimes_{\min}\mathcal Z\), Hypothesis (KR) gives a subalgebra \(E\subseteq F_\omega(A)\) without characters containing the unit, and a character of \(F_\omega(A)\) would restrict to a character of \(E\). \(\blacksquare\)

*Proof of Corollary 2.3.* The maps \(x\mapsto x\otimes1_D\) are injective unital \(*\)-homomorphisms ([Tensor products of C\*-algebras and the minimal norm](course:tensor-products-of-operator-algebras/tensor-products-of-c-star-algebras-and-the-minimal-norm), Corollary 2.3 and Lemma 3.1), so \(B\) is a nonzero unital separable C\*-algebra and the canonical maps \(\iota_m\colon D^{\otimes_{\min}m}\to B\) are unital. Compose the homomorphism \(\varphi\) of Theorem 2.2 with the quotient map \(q_m\) of Lemma 3.1(5):
\[
I(2,3)\xrightarrow{\ \varphi\ }D^{\otimes_{\max}m}\xrightarrow{\ q_m\ }D^{\otimes_{\min}m}\xrightarrow{\ \iota_m\ }B .
\]
The image of the unital composite is separable, contains \(1_B\), and is a quotient of \(I(2,3)\), hence subhomogeneous and without characters (Lemma 4.1), even if the composite has a kernel. Hypothesis (DT) gives \(B\cong B\otimes_{\min}\mathcal Z\). Since \(B\ne0\), \(z\mapsto1_B\otimes z\) embeds \(\mathcal Z\) unitally into \(B\otimes_{\min}\mathcal Z\), and the inverse of an isomorphism \(B\cong B\otimes_{\min}\mathcal Z\), which is unital, carries it into \(B\). \(\blacksquare\)

## 6. Exercises

**6.1.** Show that a unital C\*-algebra has no characters if \(M_2\) embeds into it unitally, and that \(M_2\otimes_{\max}D\) has no characters for every unital \(D\).

**6.2.** Show that \(I(2,2)\) has no characters but \(I(1,3)\) has one.

**6.3.** Show that \(F_\omega(A)\) is a C\*-subalgebra of \(A_\omega\), that is, closed under the operations and in norm.

**6.4.** Why does the proof of Lemma 4.3 choose the indices \(l(s)\) depending on \(s\), rather than taking a fixed subsequence of the given representatives?

**6.5.** Show that a character \(\chi\) of a C\*-algebra satisfies \(|\chi(x)|\le\|x\|\).

## 7. Solutions

**6.1.** A character \(\chi\) would restrict to a unital homomorphism \(M_2\to\mathbb C\). Since scalars commute, \(\chi(e_{11})=\chi(e_{12})\chi(e_{21})\), which equals \(\chi(e_{21})\chi(e_{12})=\chi(e_{22})\), and \(\chi(e_{11})\chi(e_{22})=\chi(e_{11}e_{22})=0\); so both vanish, contradicting \(\chi(e_{11})+\chi(e_{22})=\chi(1)=1\). The leg \(M_2\to M_2\otimes_{\max}D\) is unital (Lemma 3.1(2)).

**6.2.** For \(I(2,2)\), every irreducible representation has dimension \(2\) or \(4\), by the argument of Lemma 4.1. For \(I(1,3)\), evaluation at \(0\) has the image \(\mathbb C\otimes1_3\cong\mathbb C\) and is a character.

**6.3.** \(A_\omega\) is a C\*-algebra (quotient by a closed ideal), and the commutant of a set is closed under sums, products, adjoints and norm limits.

**6.4.** The given representatives are asymptotically central only along \(\omega\), and the commutation with \(E\) must hold against the moving terms \(b^j_s\); a single subsequence chosen in advance cannot respond to the elements \(b^j_s\), which change with \(s\).

**6.5.** \(\chi\) is a \(*\)-homomorphism into the C\*-algebra \(\mathbb C\), hence contractive.

## References

- [OpenAI-KRC] OpenAI, *The Kirchberg–Rørdam character criterion*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026
- [KR] E. Kirchberg and M. Rørdam, *When central sequence C\*-algebras have characters*, arXiv:1409.1395v2: Proposition 2.2, Corollary 2.3, Theorem 2.4 (Dadarlat–Toms), Theorem 2.5, Question 3.1, Lemma 3.5. https://arxiv.org/abs/1409.1395
