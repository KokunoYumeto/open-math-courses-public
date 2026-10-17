# Symmetric powers and the Foulkes–Howe map

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(V\) be a finite-dimensional complex vector space. A product of \(b\) homogeneous polynomials of degree \(a\) can be read in two ways: as an element of \(\operatorname{Sym}^b(\operatorname{Sym}^aV)\), a polynomial of degree \(b\) in polynomials of degree \(a\), or, by multiplying out factor by factor, as an element of \(\operatorname{Sym}^a(\operatorname{Sym}^bV)\). Section 2 makes this precise as a linear map
\[
\begin{aligned}
\mu_{a,b,V}:{}&\operatorname{Sym}^b(\operatorname{Sym}^aV)\\
&\longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^bV),
\end{aligned}
\]
the *Hermite–Hadamard–Howe map*, also called the *Foulkes–Howe map*. The survey of Landsberg [Landsberg, Section 7] records its history. For \(\dim V=2\) it is an isomorphism, a form of Hermite's reciprocity. Hadamard defined it in general, showed that its kernel describes the equations of the variety of products of linear forms (the Chow variety), and asked whether it always has maximal rank; Howe later expressed the same expectation. That expectation fails: \(\mu_{5,5,V}\) is not injective for suitable \(V\), as a computation of Müller and Neunhöffer showed; Cheung, Ikenmeyer and Mkrtchyan determined the kernel and found a nonzero kernel for \((a,b)=(6,6)\) as well [CIM, Theorem 6]. Brion proved that \(\mu_{a,b,V}\) is surjective for all large \(b\), with an explicit bound depending on \(a\) and \(\dim V\), and Landsberg asked for a polynomial bound [Landsberg, Problem 7.18]. The least such \(b\) is not known in general [RSW, Section 2].

## The theorem

This course proves the following theorem of OpenAI [OpenAI-FH].

**Theorem A** (OpenAI). For every integer \(a\ge2\), every integer \(b\ge a(a-1)\) and every finite-dimensional complex vector space \(V\), the map \(\mu_{a,b,V}\) is surjective.

The bound depends on \(a\) only, not on \(\dim V\), and it is not claimed to be the least possible. For \(a=1\) the map is the identity.

Foulkes conjectured that for \(a\le b\) the representation \(\operatorname{Sym}^a(\operatorname{Sym}^bV)\) of \(\mathrm{GL}(V)\) embeds equivariantly in \(\operatorname{Sym}^b(\operatorname{Sym}^aV)\) [RSW, Conjecture 2.10]. Theorem A gives such an embedding in its range:

**Corollary B** (OpenAI). For \(a\ge2\) and \(b\ge a(a-1)\) there is an injective \(\mathrm{GL}(V)\)-equivariant linear map \(\operatorname{Sym}^a(\operatorname{Sym}^bV)\to\operatorname{Sym}^b(\operatorname{Sym}^aV)\).

**The course.**

1. This lesson: symmetric powers, the map \(\mu_{a,b,V}\), its image, and a criterion for surjectivity in terms of symmetric multilinear forms.
2. [A differential injectivity lemma](a-differential-injectivity-lemma.md): the directional derivative that moves one degree from a vector variable \(U\) to a variable \(Y\) is injective when the \(U\)-degree exceeds the \(Y\)-degree.
3. [Vanishing on products](vanishing-on-products.md): an induction on \(a\) proves the criterion for \(b\ge a(a-1)\); Theorem A and Corollary B.

**What the course assumes.** Linear algebra over \(\mathbb C\): tensor products, quotient spaces, dual spaces, Hermitian inner products and adjoints; polynomials in several variables and their partial derivatives.

## 1. Symmetric powers and averaging

For a complex vector space \(W\) and \(k\ge1\), the symmetric group \(\mathfrak S_k\) acts on \(W^{\otimes k}\) by permuting the factors. The *symmetric power* \(\operatorname{Sym}^kW\) is the quotient of \(W^{\otimes k}\) by the span of the tensors \(x-\pi x\), and \(w_1\cdots w_k\) denotes the class of \(w_1\otimes\cdots\otimes w_k\); \(\operatorname{Sym}^0W=\mathbb C\). These classes multiply to a commutative graded algebra \(\operatorname{Sym}W\), the polynomial ring in a basis of \(W\). A linear map on \(W^{\otimes k}\) that is invariant under \(\mathfrak S_k\), equivalently a symmetric \(k\)-linear map on \(W\), factors through \(\operatorname{Sym}^kW\). A *product of \(k\) vectors* is an element \(u_1\cdots u_k\) with \(u_i\in W\); the \(u_i\) may repeat or vanish.

**Lemma 1.1** (averaging). The linear map
\[
\begin{aligned}
&\operatorname{Av}(w_1\cdots w_k)\\
&\quad=\frac1{k!}\sum_{\pi\in\mathfrak S_k}w_{\pi(1)}\otimes\cdots\otimes w_{\pi(k)}
\end{aligned}
\]
is well defined on \(\operatorname{Sym}^kW\) and is an isomorphism onto the invariant tensors \((W^{\otimes k})^{\mathfrak S_k}\); its inverse is the quotient map restricted to invariant tensors. For a linear map \(f:W\to W'\), \(\operatorname{Av}\circ\operatorname{Sym}^kf=f^{\otimes k}\circ\operatorname{Av}\).

*Proof.* The symmetrization \(x\mapsto\frac1{k!}\sum_\pi\pi x\) on \(W^{\otimes k}\) is invariant under \(\mathfrak S_k\), so it factors through \(\operatorname{Sym}^kW\). For an invariant tensor \(t\), \(\operatorname{Av}[t]=\frac1{k!}\sum_\pi\pi t=t\); and \([\operatorname{Av}[x]]=\frac1{k!}\sum_\pi[\pi x]=[x]\). The last identity holds on products \(w_1\cdots w_k\) by inspection. \(\square\)

**Lemma 1.2** (polarization). For \(u_1,\dots,u_k\in W\), in \(\operatorname{Sym}^kW\),
\[
\begin{aligned}
&k!\,u_1\cdots u_k\\
&\quad=\sum_{J\subseteq\{1,\dots,k\}}(-1)^{k-|J|}\Bigl(\sum_{j\in J}u_j\Bigr)^k .
\end{aligned}
\]
Consequently the pure powers \(u^k\) span \(\operatorname{Sym}^kW\).

*Proof.* Expanding, \((\sum_{j\in J}u_j)^k\) is the sum of \(u_{s_1}\cdots u_{s_k}\) over the sequences \(s\in J^k\). A sequence \(s\) whose set of entries is \(S\) occurs for the \(J\supseteq S\), with total coefficient \(\sum_{J\supseteq S}(-1)^{k-|J|}\), which is \(0\) unless \(S=\{1,\dots,k\}\) and \(1\) if it is. The sequences with all entries distinct are the \(k!\) permutations, each giving \(u_1\cdots u_k\). Products of \(k\) vectors span \(\operatorname{Sym}^kW\), and \(k!\ne0\). \(\square\)

## 2. The map

Fix \(a\ge1\). The algebra \((\operatorname{Sym}V)^{\otimes a}\), with factorwise multiplication, carries the action of \(\mathfrak S_a\) by permutation of the factors, by algebra automorphisms. So the invariants of degree \(j\) in each factor,
\[
R_j=\bigl((\operatorname{Sym}^jV)^{\otimes a}\bigr)^{\mathfrak S_a},
\]
form a graded commutative algebra \(R=\bigoplus_jR_j\). By Lemma 1.1, \(\operatorname{Av}\) identifies \(\operatorname{Sym}^aV\) with \(R_1\), and \(\operatorname{Sym}^a(\operatorname{Sym}^bV)\) with \(R_b\) (take \(W=\operatorname{Sym}^bV\)). Multiplication of \(b\) elements of \(R_1\) is symmetric and multilinear with values in \(R_b\), so it induces a linear map \(\operatorname{Sym}^bR_1\to R_b\).

**Definition 2.1.** The map \(\mu_{a,b,V}\) from \(\operatorname{Sym}^b(\operatorname{Sym}^aV)\) to \(\operatorname{Sym}^a(\operatorname{Sym}^bV)\) is the map induced by multiplication \(\operatorname{Sym}^bR_1\to R_b\), transported by the two identifications of Lemma 1.1.

For \(u\in V\), \(\operatorname{Av}(u^a)=u^{\otimes a}\), and in \((\operatorname{Sym}V)^{\otimes a}\), with \(P=u_1\cdots u_b\in\operatorname{Sym}^bV\),
\[
\begin{aligned}
u_1^{\otimes a}\cdots u_b^{\otimes a}&=(u_1\cdots u_b)^{\otimes a}\\
&=\operatorname{Av}(P^a),
\end{aligned}
\]
where \(P^a\) is the \(a\)-th power of \(P\) in \(\operatorname{Sym}(\operatorname{Sym}^bV)\). Hence
\[
\mu_{a,b,V}\bigl(u_1^a\cdots u_b^a\bigr)=(u_1\cdots u_b)^a .
\]

**Proposition 2.2** (the image). The image of \(\mu_{a,b,V}\) is spanned by the powers \(P^a\) of the products \(P\) of \(b\) vectors.

*Proof.* By Lemma 1.2 the pure powers \(u^a\) span \(\operatorname{Sym}^aV\), so the products \(u_1^a\cdots u_b^a\) span \(\operatorname{Sym}^b(\operatorname{Sym}^aV)\). Their images are the \(P^a\). \(\square\)

An invertible linear map \(g\) of \(V\) acts on all these spaces through \(\operatorname{Sym}^k\) and tensor powers, and \(\mu_{a,b,V}\) commutes with these actions, by the last statement of Lemma 1.1 and because \(g\) acts on \(\operatorname{Sym}V\) by algebra automorphisms. So \(\mu_{a,b,V}\) is \(\mathrm{GL}(V)\)-equivariant.

## 3. The diagonal criterion

Put \(E=\operatorname{Sym}^bV\). Linear functionals \(\lambda\) on \(\operatorname{Sym}^aE\) correspond bijectively to symmetric \(a\)-linear forms on \(E\), by \(T_\lambda(w_1,\dots,w_a)=\lambda(w_1\cdots w_a)\), since \(\operatorname{Sym}^aE\) is the quotient of \(E^{\otimes a}\) by the relations \(x-\pi x\). Then \(T_\lambda(P,\dots,P)=\lambda(P^a)\).

**Proposition 3.1** (OpenAI; diagonal criterion). The map \(\mu_{a,b,V}\) is surjective if and only if every symmetric \(a\)-linear form \(T\) on \(\operatorname{Sym}^bV\) with \(T(P,\dots,P)=0\) for every product \(P\) of \(b\) vectors is zero.

*Proof.* A subspace of the finite-dimensional space \(\operatorname{Sym}^aE\) is everything exactly when no nonzero functional vanishes on it. By Proposition 2.2, \(\lambda\) vanishes on the image of \(\mu_{a,b,V}\) exactly when \(\lambda(P^a)=0\) for all products \(P\), that is, when \(T_\lambda\) vanishes on the diagonal at all products. \(\square\)

So Theorem A is equivalent to a vanishing statement, proved in [Vanishing on products](vanishing-on-products.md): a symmetric \(a\)-linear form on \(\operatorname{Sym}^bV\) that vanishes on the diagonal at all products of \(b\) vectors is zero when \(b\ge a(a-1)\).

## 4. Exercises

**4.1** (easy). Let \(\dim V=1\). Show that both sides of \(\mu_{a,b,V}\) are one-dimensional and that \(\mu_{a,b,V}\) is an isomorphism.

**4.2** (easy). Write out Lemma 1.2 for \(k=2\) and \(k=3\).

**4.3** (medium). Let \(\dim V=3\), \(a=3\) and \(b=2\). Compute the dimensions of the two sides of \(\mu_{3,2,V}\) and conclude that it is not surjective. Why does this not contradict Theorem A?

**4.4** (medium). For \(\dim V=2\), show that the two sides of \(\mu_{a,b,V}\) have the same dimension for all \(a,b\).

## 5. Solutions

**4.1.** With \(V=\mathbb Cv\), \(\operatorname{Sym}^kV=\mathbb Cv^k\), so both sides are spanned by \((v^a)^b\) and \((v^b)^a\) respectively, and \(\mu_{a,b,V}((v^a)^b)=(v^b)^a\) by the formula before Proposition 2.2.

**4.2.** \(2u_1u_2=(u_1+u_2)^2-u_1^2-u_2^2\), and
\[
\begin{aligned}
6u_1u_2u_3={}&(u_1+u_2+u_3)^3\\
&-(u_1+u_2)^3-(u_1+u_3)^3\\
&-(u_2+u_3)^3\\
&+u_1^3+u_2^3+u_3^3 .
\end{aligned}
\]

**4.3.** \(\dim\operatorname{Sym}^kW=\binom{\dim W+k-1}k\). Here \(\dim\operatorname{Sym}^3V=10\) and \(\dim\operatorname{Sym}^2V=6\), so the domain has dimension \(\binom{11}2=55\) and the codomain \(\binom83=56\). Theorem A requires \(b\ge a(a-1)=6\).

**4.4.** \(\dim\operatorname{Sym}^aV=a+1\), so the domain has dimension \(\binom{a+b}b\) and the codomain \(\binom{b+a}a\), which are equal.

## References

- [OpenAI-FH] OpenAI, *Quadratic stabilization of the canonical Foulkes–Howe map*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026
- [Landsberg] J. M. Landsberg, *Geometric complexity theory: an introduction for geometers*, Annali dell'Università di Ferrara 61 (2015), 65–117; arXiv:1305.7387, Section 7 and Problem 7.18 (numbering of the arXiv version). https://arxiv.org/abs/1305.7387
- [CIM] M.-W. Cheung, C. Ikenmeyer and S. Mkrtchyan, *Symmetrizing tableaux and the 5th case of the Foulkes conjecture*, Journal of Symbolic Computation 80 (2017), 833–843; arXiv:1509.03944, Theorem 6. https://arxiv.org/abs/1509.03944
- [RSW] C. Raicu, S. V. Sam and J. Weyman, *On some modules supported in the Chow variety*, Vietnam Journal of Mathematics 50 (2022), 501–521; arXiv:2108.10910, Section 2 and Conjecture 2.10. https://arxiv.org/abs/2108.10910
