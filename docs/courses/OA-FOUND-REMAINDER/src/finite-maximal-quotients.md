# Finite maximal quotients

*Self-checked by the writing AI. Original text: CC0 1.0.*

A maximal C*-quotient of a finite von Neumann algebra is itself a finite von Neumann factor. Its quotient map can be singular, so ultraweak compactness cannot simply be passed through that map. We instead modify a Cauchy sequence on central projections invisible to the quotient. The modified sequence has uniformly small centre-valued \(L^2\) increments. A weak cluster point then realizes the prescribed GNS limit.

Prerequisites are [Central averaging and maximal ideals](../reader/central-averaging-and-maximal-ideals.html), Corollary 6.2; the centre-valued trace in [Traces on von Neumann algebras, Part A](../reader/supplements/traces-on-von-neumann-algebras-part-a-def-v-2-1-to-def-v-2-17.html), Theorem 5.2; and [Multiplicity of a von Neumann algebra](../reader/supplements/tracial-gns-and-finite-algebras.html#oa-fnd-mu-21), Proposition 11.2. That proposition proves that the GNS representation of any tracial positive functional, whether normal or not, generates a finite von Neumann algebra with a faithful normal vector trace. We use [Kaplansky density](../../foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences.html) for its unit ball, and commutative Gelfand theory and C*-quotient functional calculus from [C*-algebra functional calculus](../../foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html).

The central-patch argument below combines the linked programme proofs. Lemmas 1.1 and 2.1 turn a quotient Cauchy sequence into one controlled by every normal trace on the centre; Theorem 3.1 then proves that the GNS image is already weakly closed. The character on the centre may be singular, the algebra is arbitrary, and the quotient’s tracial Hilbert space may be nonseparable. The proof and the type I product example are supplied here in full.

Let \(M\) be finite, without any countability hypothesis, let \(Z=Z(M)\), and let \(T:M\to Z\) be its normalized centre-valued trace. Fix a character \(\chi\) of \(Z\), and put
\[
\tau=\chi\circ T,\qquad
I_\chi=\{a:\tau(a^*a)=0\}.
\tag{0.1}
\]
The preceding lesson proves that \(I_\chi\) is a maximal two-sided ideal. Let \((\pi,H,\xi)\) be the GNS representation of \(\tau\). Since \(\tau\) is tracial, its null left ideal is two-sided and equals \(\ker\pi\): if \(\tau(a^*a)=0\), then
\[
\|\pi(a)\pi(b)\xi\|^2=\tau(b^*a^*ab)
\leq\|b\|^2\tau(a^*a)=0
\]
for every \(b\), and the converse follows by applying \(\pi(a)\) to \(\xi\). Thus \(\pi(M)\cong M/I_\chi\).

## 1. Central patches that preserve a quotient sequence

**Lemma 1.1.** Suppose \(a_n\in M_1\) and
\[
\tau((a_{n+1}-a_n)^*(a_{n+1}-a_n))<\varepsilon_n^2,
\qquad \sum_n\varepsilon_n<\infty.
\tag{1.1}
\]
There are \(b_n\in M_1\) satisfying \(\pi(b_n)=\pi(a_n)\) and
\[
T((b_{n+1}-b_n)^*(b_{n+1}-b_n))
\leq\varepsilon_n^2\,1.
\tag{1.2}
\]

**Proof.** Put \(d_n=a_{n+1}-a_n\), \(h_n=T(d_n^*d_n)\). The central projection
\[
e_n=1_{[0,\varepsilon_n^2]}(h_n)
\]
satisfies \(\chi(e_n)=1\). Indeed, \(\chi(e_n)\) is zero or one. If it were zero, the spectral inequality
\[
h_n\geq\varepsilon_n^2(1-e_n)
\]
would give \(\chi(h_n)\geq\varepsilon_n^2\), contrary to (1.1). No preservation of this Borel spectral projection by \(\chi\) is assumed.

Set
\[
z_0=1,\qquad z_n=e_1e_2\cdots e_n,\qquad
p_k=z_{k-1}-z_k.
\]
The \(z_n\) decrease, \(\chi(z_n)=1\), and the \(p_k\) are orthogonal central projections with \(\chi(p_k)=0\). Define, with \(a_0=a_1\),
\[
b_n=z_na_n+\sum_{k=1}^n p_ka_{k-1}.
\tag{1.3}
\]
This is a contraction, because it uses contractions on the members of a finite central partition of \(1\). Every \(p_k\), and \(1-z_n\), lies in \(\ker\pi\), as its \(\tau\)-value is zero. Hence \(\pi(b_n)=\pi(a_n)\).

The old central pieces in (1.3) are frozen rather than replaced at later stages. Consequently
\[
b_{n+1}-b_n=z_{n+1}(a_{n+1}-a_n).
\]
The centre-module rule for \(T\) gives
\[
T((b_{n+1}-b_n)^*(b_{n+1}-b_n))
=z_{n+1}h_n\leq\varepsilon_n^2\,1,
\]
because \(z_{n+1}\leq e_n\). \(\square\)

The frozen pieces matter. Replacing the complement of every \(z_n\) by a fixed identity can create uncontrolled increments on the annulus \(z_n-z_{n+1}\).

## 2. A cluster point recovers the GNS limit

**Lemma 2.1.** For a sequence \(b_n\) as in Lemma 1.1, there is \(b\in M_1\) such that
\[
T((b-b_n)^*(b-b_n))
\leq\left(\sum_{k=n}^\infty\varepsilon_k\right)^2\,1.
\tag{2.1}
\]
In particular \(\pi(b_n)\xi\to\pi(b)\xi\).

**Proof.** For every positive normal \(\lambda\in Z_*\), the functional \(\lambda\circ T\) is a normal positive finite trace. Its \(L^2\) seminorm obeys the triangle inequality. For \(m>n\), (1.2) gives
\[
(\lambda\circ T)((b_m-b_n)^*(b_m-b_n))^{1/2}
\leq\lambda(1)^{1/2}\sum_{k=n}^{m-1}\varepsilon_k.
\]
Positive normal functionals separate the order of \(Z\), so
\[
T((b_m-b_n)^*(b_m-b_n))
\leq\left(\sum_{k=n}^{m-1}\varepsilon_k\right)^2\,1.
\tag{2.2}
\]

The unit ball \(M_1\) is ultraweakly compact. Choose a cluster point \(b\in M_1\), with a subnet of the sequence tending to it and with indices tending to infinity. For a normal positive \(\omega\), the function \(x\mapsto\omega(x^*x)\) is ultraweakly lower semicontinuous. A direct proof is the identity
\[
\omega(x^*x)=
\sup_{c\in M}
\{2\operatorname{Re}\omega(c^*x)-\omega(c^*c)\};
\tag{2.3}
\]
positivity of \(\omega((x-c)^*(x-c))\) gives one inequality, and \(c=x\) gives the other. Every function inside the supremum is ultraweakly continuous.

Apply (2.3) with \(\omega=\lambda\circ T\) to the subnet in (2.2), for a fixed \(n\). It gives (2.1) after testing all positive normal \(\lambda\). Evaluation of this central order inequality by the possibly singular character \(\chi\) now yields
\[
\|\pi(b-b_n)\xi\|^2
=\tau((b-b_n)^*(b-b_n))
\leq\left(\sum_{k=n}^\infty\varepsilon_k\right)^2
\longrightarrow0.
\]
The character is used only after the central inequality has been established. \(\square\)

## 3. The quotient is a finite von Neumann factor

**Theorem 3.1.** Every maximal C*-quotient of a finite von Neumann algebra is a finite von Neumann factor.

**Proof.** All maximal ideals are \(I_\chi\) by the preceding lesson. Let \(N=\pi(M)''\). The imported tracial-GNS theorem makes the vector state of \(\xi\) a faithful normal tracial state on \(N\), so \(N\) is finite and \(\xi\) is separating.

First, the set
\[
\pi(M_1)\xi\subseteq H
\tag{3.1}
\]
is norm closed. Given a convergent sequence in that set, choose representatives \(a_n\in M_1\) and pass to a subsequence whose successive squared GNS distances satisfy (1.1), with, for example, \(\varepsilon_n=2^{-n}\). Lemmas 1.1–2.1 supply \(b\in M_1\) with the same vector limit. This proves sequential closedness, hence closedness in the Hilbert-space metric.

The unit ball of \(\pi(M)\) is the image of \(M_1\). Here is an exact contraction lift: if \(\|\pi(a)\|\leq1\), put
\[
b=a\,f(a^*a),\qquad
f(t)=\frac1{\max\{1,\sqrt t\}}.
\tag{3.2}
\]
Continuous functional calculus gives \(\|b\|\leq1\), and \(\pi(b)=\pi(a)\), because \(f\) is one on the spectrum of \(\pi(a)^*\pi(a)\).

Kaplansky density now makes \(\pi(M_1)\) strongly dense in \(N_1\). For \(x\in N_1\), its vector \(x\xi\) belongs to the norm closure of (3.1), and so equals \(\pi(b)\xi\) for some \(b\in M_1\). Since \(\xi\) is separating for \(N\), \(x=\pi(b)\). Therefore
\[
N_1=\pi(M_1),\qquad N=\pi(M).
\]
The quotient is indeed a von Neumann algebra, rather than merely a norm-closed algebra strongly dense in one.

Finally \(M/I_\chi\) is simple because \(I_\chi\) is maximal. A nontrivial central projection in \(N\) would generate a nonzero proper closed ideal. Thus \(Z(N)=\mathbb C1\), and the finite von Neumann algebra \(N\) is a factor. \(\square\)

There is no assertion that the quotient map is normal. It can annihilate all the central coordinate projections of a product while sending their supremum to the identity.

## 4. A type I product with a type II quotient

Let
\[
M=\prod_{n\geq1}M_{3^n}(\mathbb C),
\qquad Z=\ell^\infty(\mathbb N),
\]
and let \(\mathcal V\) be a free ultrafilter. Its central character is
\[
\chi((c_n))=\lim_{\mathcal V}c_n.
\]
The centre-valued trace is the sequence of normalized matrix traces. Theorem 3.1 gives a finite factor
\[
N=M/I_{\mathcal V},\qquad
I_{\mathcal V}=
\{(a_n):\lim_{\mathcal V}\operatorname{tr}_{3^n}(a_n^*a_n)=0\}.
\tag{4.1}
\]

For \(j\geq0\), choose nested coordinate projections \(p_{n,j}\) of rank \(3^{n-j}\) if \(n\geq j\), and set \(p_{n,j}=0\) if \(n<j\). Set \(p_0=1\) and \(p_j=(p_{n,j})_n\) for \(j\geq1\). The quotient trace satisfies
\[
\tau_N(\pi(p_j))=3^{-j}.
\tag{4.2}
\]
Thus the quotient has an infinite strictly decreasing chain of nonzero projections. It is infinite dimensional. A finite type I factor is a finite matrix algebra, so the finite factor \(N\) is of type II\(_1\). The domain is of type I, being a product of finite type I central pieces. Hence type I is not preserved under arbitrary C*-quotients of von Neumann algebras.

The quotient need not have separable predual or a separable GNS Hilbert space; no countability is claimed for those objects.

## 5. Graded exercises with complete solutions

### Exercise 5.1 — Trace size and operator norm (basic)

In the product from Section 4, let \(q_n\) be rank one in \(M_{3^n}\), and let \(r_n\) have rank \(3^{n-1}\). Determine the quotient images of \(q=(q_n)\) and \(r=(r_n)\), their operator norms when nonzero, and their quotient trace values.

**Solution.** Both product projections have norm one. Their normalized trace sequences are \(3^{-n}\) and \(1/3\). Formula (4.1) kills \(q\), while \(r\) has nonzero image with trace \(1/3\). A nonzero projection has norm one, so \(\|\pi(r)\|=1\). This quotient distinguishes the normalized dimensions of the ranges; the original norm alone does not determine whether an element survives.

### Exercise 5.2 — A singular quotient map (intermediate)

Let \(z_n\) be the central projection supported only on the \(n\)-th coordinate of the product. Compute the quotient image of every \(z_n\) and compare the images of their finite sums with the image of their strong sum.

**Solution.** A free ultrafilter assigns zero to every singleton, so
\[
\pi(z_n)=0,\qquad
\pi\left(\sum_{n=1}^kz_n\right)=0.
\]
In the product von Neumann algebra, \(\sum_nz_n=1\) strongly. Its image is \(1_N\ne0\). Thus the quotient map does not preserve this increasing supremum and is not normal. Theorem 3.1 nevertheless makes its target a finite von Neumann algebra, by a different argument.

### Exercise 5.3 — An uncountable orthogonal family in the quotient GNS space (advanced)

Show that the quotient in Section 4 has a nonseparable GNS Hilbert space. Use the diagonal matrices indexed by the \(n\) ternary digits in a basis of \(\mathbb C^{3^n}\), and binary branches to choose one digit at every coordinate.

**Solution.** Put \(\omega=e^{2\pi i/3}\). For \(1\leq j\leq n\), let \(u_{n,j}\) be the diagonal unitary whose entry at the word \((d_1,\ldots,d_n)\in\{0,1,2\}^n\) is \(\omega^{d_j}\). Uniform averaging of the independent ternary digits gives
\[
\operatorname{tr}_{3^n}(u_{n,j}^*u_{n,k})
=\begin{cases}1,&j=k,\\0,&j\ne k.\end{cases}
\]
For a binary branch \(b\), put \(m(n)=\lfloor\log_2 n\rfloor\) and let
\[
j_n(b)=1+\text{the integer encoded by the first }m(n)\text{ bits of }b.
\]
Then \(1\leq j_n(b)\leq2^{m(n)}\leq n\). Define the product unitary \(u_b=(u_{n,j_n(b)})_n\). For distinct branches \(b,c\), their encoded prefixes differ for every sufficiently large \(n\); thus \(j_n(b)\ne j_n(c)\) eventually. The ultrafilter trace gives
\[
\tau(u_b^*u_c)=0\quad(b\ne c),\qquad
\tau(u_b^*u_b)=1.
\]
The vectors \(\pi(u_b)\xi\), over all binary branches, form an uncountable orthonormal family. Consequently the GNS space is nonseparable. This is compatible with the finite-factor conclusion: sigma-finiteness of a von Neumann algebra, supplied here by its faithful trace, does not force its tracial Hilbert space to be separable.

## References

- [Programme proofs] The freely accessible multiplicity lesson, Proposition 11.2 (tracial GNS with a faithful normal vector trace); trace lesson, Theorem 5.2 (the centre-valued trace); density lesson, Theorem 7.1 (Kaplansky density); and the preceding lesson, Corollary 6.2 (the maximal-ideal formula). Their exact proof links are given above.
- The central-patch construction, weak-cluster-point estimate, closed-unit-ball argument and worked product examples are the complete course arguments of this lesson, under those stated inputs.
