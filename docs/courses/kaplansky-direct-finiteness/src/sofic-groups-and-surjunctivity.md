# Sofic groups and surjunctivity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A cellular automaton over a group \(G\) changes every coordinate of a configuration \(x:G\to A\) by one finite rule that looks at finitely many neighbours. For a finite group, an injective map of the finite set \(A^G\) to itself is surjective. Gottschalk conjectured that the same holds for every group, and Gromov and Weiss proved it for sofic groups, the groups whose multiplication can be imitated by maps of finite sets. This lesson proves the Gromov–Weiss theorem in full, and shows that elements \(a,b\) of a group algebra over a finite field with \(ab=1\ne ba\) give an injective automaton that is not surjective. Such a pair can therefore exist only over a group that is not sofic.

- Cellular automata (Section 1).
- Group-algebra elements as automata (Section 2).
- Sofic groups (Section 3).
- Two compactness lemmas (Section 4).
- The Gromov–Weiss theorem (Section 5).
- Consequences for group algebras (Section 6).

## 1. Cellular automata

Let \(G\) be a group with identity \(1\) and \(A\) a finite nonempty set, the *alphabet*. A *configuration* is any function \(x:G\to A\); the set of all configurations is \(A^G\). A *cellular automaton* is a map \(\tau:A^G\to A^G\) of the form
\[
\tau(x)(g)=\varphi\bigl((x(gu))_{u\in M}\bigr)\qquad(g\in G),
\]
where \(M\subseteq G\) is a finite set, the *memory*, and \(\varphi:A^M\to A\) is any map, the *local rule*. The value at \(g\) depends on the values at the right neighbours \(gu\), \(u\in M\).

The group acts on configurations by left translation, \((\lambda_hx)(g)=x(h^{-1}g)\), and every cellular automaton commutes with this action:
\[
\begin{aligned}
\tau(\lambda_hx)(g)&=\varphi\bigl((x(h^{-1}gu))_u\bigr)\\
&=\tau(x)(h^{-1}g)=(\lambda_h\tau(x))(g) .
\end{aligned}
\]
The group \(G\) is *surjunctive* if, for every finite alphabet \(A\), every injective cellular automaton \(\tau:A^G\to A^G\) is surjective. Gottschalk conjectured that every group is surjunctive [Pestov, Conjecture 6.1]. If \(G\) is finite, \(A^G\) is a finite set and every injective self-map is surjective.

## 2. Group-algebra elements as automata

Let \(K\) be a field. For \(c=\sum_uc_uu\in K[G]\) define \(T_c:K^G\to K^G\) by
\[
(T_cx)(g)=\sum_{u\in G}c_u\,x(gu) .
\]
The sum is finite for every configuration, also when \(x\) has infinite support. If \(K\) is finite, \(T_c\) is a cellular automaton with alphabet \(K\), memory \(\operatorname{supp}(c)\) and local rule \(p\mapsto\sum_uc_up(u)\). For \(h\in G\) let \(\delta_h\in K^G\) be \(1\) at \(h\) and \(0\) elsewhere.

**Lemma 2.1.** The map \(c\mapsto T_c\) is an injective homomorphism of \(K\)-algebras from \(K[G]\) to the algebra of \(K\)-linear maps \(K^G\to K^G\), with composition as product: \(T_c\circ T_d=T_{cd}\) and \(T_1=\mathrm{id}\). Moreover \((T_c\delta_h)(1)=c_h\).

*Proof.* Linearity in \(c\) and \(T_1=\mathrm{id}\) are immediate. For \(x\in K^G\) and \(g\in G\),
\[
\begin{aligned}
(T_c(T_dx))(g)&=\sum_uc_u\sum_vd_v\,x(guv)\\
&=\sum_w\Bigl(\sum_{uv=w}c_ud_v\Bigr)x(gw)\\
&=(T_{cd}x)(g),
\end{aligned}
\]
all sums being finite. Next, \((T_c\delta_h)(1)=\sum_uc_u\delta_h(u)=c_h\). So \(T_c=0\) forces every coefficient of \(c\) to vanish. \(\square\)

The order matters: with right neighbours, \(T_c\circ T_d\) is \(T_{cd}\), not \(T_{dc}\).

**Proposition 2.2.** Let \(K\) be a finite field and \(a,b\in K[G]\) with \(ab=1\). Then \(T_b\) is an injective cellular automaton, its image is
\[
\operatorname{im}(T_b)=\{y\in K^G:T_{ba}y=y\},
\]
and if \(ba\ne1\), then \(\delta_h\notin\operatorname{im}(T_b)\) for every \(h\) with \((ba-1)_h\ne0\). In particular \(T_b\) is not surjective when \(ba\ne1\).

*Proof.* By Lemma 2.1, \(T_a\circ T_b=T_{ab}=\mathrm{id}\), so \(T_b\) is injective. If \(y=T_bx\), then \(T_{ba}y=T_bT_aT_bx=T_bx=y\). Conversely, if \(T_{ba}y=y\), then \(y=T_b(T_ay)\) lies in the image. Finally, if \((ba-1)_h\ne0\), then by Lemma 2.1
\[
\begin{aligned}
(T_{ba}\delta_h-\delta_h)(1)&=(T_{ba-1}\delta_h)(1)\\
&=(ba-1)_h\ne0 ,
\end{aligned}
\]
so \(\delta_h\) is not fixed by \(T_{ba}\). \(\square\)

The configuration that is missed is supported at one point, and it has no preimage among all configurations, not only among finitely supported ones. The image is cut out by the local equations \(\sum_u(ba-1)_u\,y(gu)=0\), \(g\in G\).

## 3. Sofic groups

For a finite nonempty set \(\Omega\) and maps \(s,t:\Omega\to\Omega\), let \(d_\Omega(s,t)\) be the proportion of points \(\omega\in\Omega\) with \(s(\omega)\ne t(\omega)\).

**Definition 3.1** ([Elek–Szabó, Definition 4.2]). A group \(G\) is *sofic* if for every finite \(E\subseteq G\) and every \(\varepsilon\in(0,1)\) there are a finite nonempty set \(\Omega\) and a map \(\sigma:G\to\Omega^\Omega\) from \(G\) to the self-maps of \(\Omega\) such that
\[
\begin{aligned}
&d_\Omega\bigl(\sigma(gh),\sigma(g)\sigma(h)\bigr)\le\varepsilon\\
&\qquad(g,h\in E),\\
&d_\Omega\bigl(\sigma(1),\mathrm{id}\bigr)\le\varepsilon,\\
&d_\Omega\bigl(\sigma(g),\mathrm{id}\bigr)>1-\varepsilon\\
&\qquad(g\in E\setminus\{1\}).
\end{aligned}
\]

Products of maps are compositions. The map \(\sigma\) imitates the left multiplication of \(G\) on most points, and the elements of \(E\) other than \(1\) move almost all points. Finite groups are sofic, with \(\Omega=G\) and \(\sigma(g)\) the left multiplication by \(g\). The group \(\mathbb Z\) is sofic, with \(\Omega=\mathbb Z/N\) for large \(N\) and \(\sigma(n)\) the rotation by \(n\) (Exercise 7.1). Residually finite groups, free groups and amenable groups are sofic [Pestov, Examples 4.1–4.4], and so are all one-relator groups [Son 2026].

**Lemma 3.2.** A subgroup of a sofic group is sofic.

*Proof.* Let \(H\le G\). For finite \(E\subseteq H\) and \(\varepsilon\), the map \(\sigma\) given by the definition for \(G\), restricted to \(H\), satisfies the three conditions. \(\square\)

## 4. Two compactness lemmas

In this section \(G\) is countable, enumerated as \(g_1,g_2,\ldots\) (with repetitions if \(G\) is finite), and \(F_n=\{g_1,\ldots,g_n\}\). A sequence \(x_n\in A^G\) *converges* to \(x\) if for every \(g\) the values \(x_n(g)\) are eventually equal to \(x(g)\).

**Lemma 4.1.** Every sequence in \(A^G\) has a convergent subsequence. If \(x_n\) converges to \(x\), then \(\tau(x_n)\) converges to \(\tau(x)\) for every cellular automaton \(\tau\).

*Proof.* Since \(A\) is finite, infinitely many \(n\) share one value of \(x_n(g_1)\); among those, infinitely many share one value of \(x_n(g_2)\); and so on. Choosing the \(j\)-th term of the subsequence from the \(j\)-th of these nested infinite sets gives a subsequence along which every \(x_n(g_i)\) is eventually constant. For the second statement, \(\tau(x)(g)\) depends only on the finitely many values \(x(gu)\), \(u\in M\), which are eventually those of \(x_n\). \(\square\)

**Lemma 4.2** (a finite obstruction). Let \(\tau:A^G\to A^G\) be a cellular automaton that is not surjective. Then there are a finite set \(F\subseteq G\) and a pattern \(p\in A^F\) such that \(\tau(x)|_F\ne p\) for every \(x\in A^G\).

*Proof.* Let \(y\notin\operatorname{im}(\tau)\). Suppose that for every \(n\) some \(x_n\) satisfies \(\tau(x_n)|_{F_n}=y|_{F_n}\). By Lemma 4.1 a subsequence \(x_{n_j}\) converges to some \(x\), and \(\tau(x_{n_j})\) converges to \(\tau(x)\). For each \(i\), \(\tau(x_{n_j})(g_i)=y(g_i)\) as soon as \(n_j\ge i\), so \(\tau(x)(g_i)=y(g_i)\). Then \(\tau(x)=y\), a contradiction. So some \(n\) has no such \(x_n\); take \(F=F_n\) and \(p=y|_{F_n}\). \(\square\)

**Lemma 4.3** (uniform local injectivity). Let \(\tau:A^G\to A^G\) be an injective cellular automaton. Then there is a finite set \(N\subseteq G\) such that, for all \(x,x'\in A^G\),
\[
\tau(x)|_N=\tau(x')|_N\ \Longrightarrow\ x(1)=x'(1) .
\]

*Proof.* Suppose not. Then for every \(n\) there are \(x_n,x'_n\) with \(\tau(x_n)|_{F_n}=\tau(x'_n)|_{F_n}\) and \(x_n(1)\ne x'_n(1)\). Applying Lemma 4.1 to the pairs, viewed as configurations with values in \(A\times A\), gives a subsequence along which \(x_{n_j}\to x\) and \(x'_{n_j}\to x'\). Then \(x(1)\ne x'(1)\), because the two eventually constant values differ at every step. For each \(i\) and all \(j\) with \(n_j\ge i\), \(\tau(x_{n_j})(g_i)=\tau(x'_{n_j})(g_i)\); passing to the limit, \(\tau(x)(g_i)=\tau(x')(g_i)\). So \(\tau(x)=\tau(x')\) with \(x\ne x'\), contradicting injectivity. \(\square\)

## 5. The Gromov–Weiss theorem

**Theorem 5.1** (Gromov, Weiss; [Pestov, Theorem 6.3]). Every sofic group is surjunctive.

*Proof.* Let \(G\) be sofic, \(A\) a finite alphabet with \(k=|A|\) elements, and \(\tau\) an injective cellular automaton with memory \(M\) and local rule \(\varphi\). If \(k=1\) there is nothing to prove, so let \(k\ge2\).

*Reduction to a countable group.* Let \(H\) be the subgroup generated by \(M\); it is countable and, by Lemma 3.2, sofic. Choose a set \(R\) of representatives of the left cosets of \(H\), with \(1\in R\). For \(x\in A^G\) and \(r\in R\) put \(x_r(h)=x(rh)\), \(h\in H\). Let \(\tau_H:A^H\to A^H\) be the automaton with the same memory and rule. Since \(M\subseteq H\),
\[
\tau(x)(rh)=\varphi\bigl((x(rhu))_u\bigr)=\tau_H(x_r)(h),
\]
that is, \(\tau(x)_r=\tau_H(x_r)\). If \(\tau_H(z)=\tau_H(z')\) with \(z\ne z'\), the configurations with \(x_1=z\), \(x'_1=z'\) and \(x_r=x'_r\) constant for \(r\ne1\) have the same image under \(\tau\), which is impossible; so \(\tau_H\) is injective. If \(\tau_H\) is surjective, every \(y\in A^G\) has a preimage: choose \(z_r\) with \(\tau_H(z_r)=y_r\) for each \(r\) and let \(x_r=z_r\). So it suffices to treat \(H\), and we assume from now on that \(G\) is countable.

*The finite data.* Suppose that \(\tau\) is not surjective. Lemma 4.2 gives a finite set \(F\) and a pattern \(p\in A^F\) that never occurs as \(\tau(x)|_F\), and Lemma 4.3 gives a finite set \(N\). Let \(E\) be the finite set consisting of \(1\) and the elements
\[
u^{-1},\quad f,\quad f^{-1},\quad n^{-1},\quad f'f^{-1}
\]
for \(u\in M\), \(f,f'\in F\), \(n\in N\). Let \(\varepsilon>0\), to be fixed below, and let \(\sigma:G\to\Omega^\Omega\) be as in Definition 3.1 for \(E\) and \(\varepsilon\).

*Good points.* Call \(\omega\in\Omega\) *good* if \(\sigma(1)\omega=\omega\), if \(\sigma(g)\sigma(h)\omega=\sigma(gh)\omega\) for all \(g,h\in E\), and if \(\sigma(g)\omega\ne\omega\) for all \(g\in E\setminus\{1\}\). Each of these \(1+|E|^2+|E|\) conditions fails on at most \(\varepsilon|\Omega|\) points, so the set \(\Omega'\) of good points satisfies
\[
\begin{gathered}
|\Omega'|\ge(1-c_E\varepsilon)|\Omega|,\\
c_E=1+|E|+|E|^2 .
\end{gathered}
\]

*A simulated automaton.* For \(\xi\in A^\Omega\) define \(\tau_\sigma(\xi)\in A^\Omega\) and, for each \(\omega\in\Omega\), a configuration \(x^\xi_\omega\in A^G\) by
\[
\begin{aligned}
\tau_\sigma(\xi)(\eta)&=\varphi\bigl((\xi(\sigma(u^{-1})\eta))_{u\in M}\bigr),\\
x^\xi_\omega(g)&=\xi\bigl(\sigma(g^{-1})\omega\bigr).
\end{aligned}
\]
Let \(\omega\) be good and \(g\in F\cup N\). For \(u\in M\), both \(u^{-1}\) and \(g^{-1}\) lie in \(E\), so \(\sigma(u^{-1})\sigma(g^{-1})\omega=\sigma(u^{-1}g^{-1})\omega\), and
\[
\begin{aligned}
&\tau(x^\xi_\omega)(g)\\
&\quad=\varphi\bigl((\xi(\sigma((gu)^{-1})\omega))_u\bigr)\\
&\quad=\tau_\sigma(\xi)\bigl(\sigma(g^{-1})\omega\bigr).
\end{aligned}\tag{5.1}
\]

*A lower bound.* Suppose \(\tau_\sigma(\xi)=\tau_\sigma(\xi')\) and let \(\omega\) be good. By (5.1) with \(g\in N\), the configurations \(x^\xi_\omega\) and \(x^{\xi'}_\omega\) have images that agree on \(N\), so by Lemma 4.3 they agree at \(1\): \(\xi(\sigma(1)\omega)=\xi'(\sigma(1)\omega)\), that is \(\xi(\omega)=\xi'(\omega)\). So \(\tau_\sigma(\xi)\) determines the restriction of \(\xi\) to \(\Omega'\), and
\[
|\tau_\sigma(A^\Omega)|\ge k^{|\Omega'|} .
\]

*An upper bound.* For good \(\omega\), the *window* \(W_\omega=\{\sigma(f^{-1})\omega:f\in F\}\) has exactly \(|F|\) points. Indeed, if \(\sigma(f^{-1})\omega=\sigma(f'^{-1})\omega\) with \(f\ne f'\), applying \(\sigma(f')\) and using goodness gives \(\sigma(f'f^{-1})\omega=\sigma(1)\omega=\omega\) with \(f'f^{-1}\in E\setminus\{1\}\), which is excluded. By (5.1) with \(g=f\), the pattern \(f\mapsto\tau_\sigma(\xi)(\sigma(f^{-1})\omega)\) equals \(\tau(x^\xi_\omega)|_F\), so it is never \(p\).

If the windows of two good points \(\omega,\omega'\) meet, say \(\sigma(f^{-1})\omega=\sigma(f'^{-1})\omega'=\eta\), then \(\sigma(f')\eta=\sigma(f')\sigma(f'^{-1})\omega'=\sigma(1)\omega'=\omega'\). So the good points whose windows meet \(W_\omega\) lie in the set \(\{\sigma(f')\eta:f'\in F,\ \eta\in W_\omega\}\), of at most \(|F|^2\) points. Choosing good points one at a time and discarding each time the at most \(|F|^2\) good points whose windows meet the window just chosen, we obtain good points \(\omega_1,\ldots,\omega_r\) with pairwise disjoint windows and \(r\ge|\Omega'|/|F|^2\). On each window an image \(\tau_\sigma(\xi)\) takes one of at most \(k^{|F|}-1\) patterns, so
\[
\begin{aligned}
|\tau_\sigma(A^\Omega)|&\le k^{|\Omega|-r|F|}\bigl(k^{|F|}-1\bigr)^r\\
&=k^{|\Omega|}\bigl(1-k^{-|F|}\bigr)^r .
\end{aligned}
\]

*Comparison.* Put \(c=-\log_k(1-k^{-|F|})/|F|^2>0\). The two bounds and \(r\ge|\Omega'|/|F|^2\) give \(|\Omega'|\le|\Omega|-c|\Omega'|\), so
\[
1-c_E\varepsilon\le\frac{|\Omega'|}{|\Omega|}\le\frac1{1+c} .
\]
The constants \(c\) and \(c_E\) depend only on \(k\), \(F\), \(N\) and \(M\), which were fixed before \(\varepsilon\). Choosing \(\varepsilon<c/((1+c)c_E)\) makes the left side larger than the right, a contradiction. So \(\tau\) is surjective. \(\square\)

This counting argument is the one behind the entropy proofs in [Capraro–Lupini, Section II.13]: an injective automaton keeps almost all the information of a configuration, while a forbidden pattern loses a fixed proportion of it.

## 6. Consequences for group algebras

**Corollary 6.1.** Let \(K\) be a finite field, \(G\) a group and \(a,b\in K[G]\) with \(ab=1\) and \(ba\ne1\). Then \(G\) is not surjunctive, and \(G\) is not sofic.

*Proof.* By Proposition 2.2, \(T_b\) is an injective cellular automaton on \(K^G\) that is not surjective, so \(G\) is not surjunctive. By Theorem 5.1, \(G\) is not sofic. \(\square\)

Elek and Szabó proved more: for a sofic group, \(D[G]\) is stably finite over every division ring \(D\) [Elek–Szabó, Corollary 4.7]. Corollary 6.1 is the part needed in this course, since the counterexample of [Line partitions, girth and the counterexample](line-partitions-girth-and-the-counterexample.md) is over a finite field. The same transfer gives more for surjunctive groups: Phung showed that Gottschalk's conjecture implies stable finiteness of group algebras over every field [Phung, abstract].

## 7. Exercises

**7.1** (easy). Let \(E\subseteq\{-R,\ldots,R\}\subseteq\mathbb Z\) and \(N>2R\). Show that \(\sigma(n)(\omega)=\omega+n\) on \(\Omega=\mathbb Z/N\) satisfies the conditions of Definition 3.1 for \(E\) and every \(\varepsilon\).

**7.2** (medium). A group is *residually finite* if for every \(g\ne1\) there is a homomorphism \(\pi\) to a finite group with \(\pi(g)\ne1\). Show that residually finite groups are sofic.

**7.3** (easy). Let \(A=\{0,1\}=\mathbb F_2\) and \(G=\mathbb Z\). Show that \(\tau(x)(n)=x(n)+x(n+1)\) is a cellular automaton that is surjective but not injective.

**7.4** (medium). Let \(c\in K[G]\) with \(K\) finite. Show directly from the definition that \(T_c\) commutes with every left translation \(\lambda_h\), and that \(T_{c}\) is injective if \(c\) has a left inverse in \(K[G]\).

**7.5** (medium). In the proof of Theorem 5.1, explain why the configuration \(x^\xi_\omega\) is defined with \(\sigma(g^{-1})\) rather than \(\sigma(g)\): show that with \(\eta\mapsto\sigma(u)\eta\) in place of \(\eta\mapsto\sigma(u^{-1})\eta\) in the definition of \(\tau_\sigma\), the identity (5.1) would require \(\sigma(u)\sigma(g)\omega=\sigma(gu)\omega\), which the definition of soficity does not provide.

## 8. Solutions

**7.1.** Here \(\sigma\) is a homomorphism from \(\mathbb Z\) to the permutations of \(\Omega\), so the first two conditions hold exactly. For \(0\ne n\in E\), \(|n|\le R<N\), so \(n\not\equiv0\pmod N\) and \(\sigma(n)\) moves every point: \(d_\Omega(\sigma(n),\mathrm{id})=1>1-\varepsilon\).

**7.2.** Let \(E\) be finite. For each \(g\in E\setminus\{1\}\) choose a homomorphism \(\pi_g\) to a finite group with \(\pi_g(g)\ne1\), and let \(\pi:G\to Q=\prod_g\pi_g(G)\) be the product homomorphism; \(Q\) is finite and \(\pi(g)\ne1\) for every \(g\in E\setminus\{1\}\). Let \(\Omega=Q\) and let \(\sigma(g)\) be the left multiplication by \(\pi(g)\). Then \(\sigma(gh)=\sigma(g)\sigma(h)\) and \(\sigma(1)=\mathrm{id}\) exactly, and for \(g\in E\setminus\{1\}\) the left multiplication by \(\pi(g)\ne1\) fixes no point of \(Q\), since \(\pi(g)q=q\) forces \(\pi(g)=1\). So \(d_\Omega(\sigma(g),\mathrm{id})=1\).

**7.3.** \(\tau\) has memory \(\{0,1\}\) and rule \((p_0,p_1)\mapsto p_0+p_1\). The constant configurations \(0\) and \(1\) both map to \(0\), so \(\tau\) is not injective. Given \(y\), define \(x(0)=0\), \(x(n+1)=y(n)-x(n)\) for \(n\ge0\) and \(x(n)=y(n)-x(n+1)\) for \(n<0\); then \(\tau(x)=y\).

**7.4.** \((T_c\lambda_hx)(g)=\sum_uc_ux(h^{-1}gu)=(T_cx)(h^{-1}g)=(\lambda_hT_cx)(g)\). If \(dc=1\), then \(T_dT_c=T_{dc}=\mathrm{id}\) by Lemma 2.1, so \(T_c\) is injective.

**7.5.** With \(\tau'_\sigma(\xi)(\eta)=\varphi((\xi(\sigma(u)\eta))_u)\) and \(x(g)=\xi(\sigma(g)\omega)\), one has \(\tau(x)(g)=\varphi((\xi(\sigma(gu)\omega))_u)\), while \(\tau'_\sigma(\xi)(\sigma(g)\omega)=\varphi((\xi(\sigma(u)\sigma(g)\omega))_u)\). The definition controls \(\sigma(u)\sigma(g)\) against \(\sigma(ug)\), not \(\sigma(gu)\). With inverses, \(\sigma(u^{-1})\sigma(g^{-1})\) is compared with \(\sigma(u^{-1}g^{-1})=\sigma((gu)^{-1})\), which is exactly what (5.1) needs.

## References

- [OpenAI-DF2] OpenAI, *A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two*, OpenAI Math Release preprint, 23 September 2026, Section 7 (Lemma 7.1 and Proposition 7.2). https://github.com/openai/math/tree/main/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026
- [Elek–Szabó] G. Elek and E. Szabó, *Sofic groups and direct finiteness*, Journal of Algebra 280 (2004), 426–434; arXiv:math/0305440, Definition 4.2 and Corollary 4.7. https://arxiv.org/abs/math/0305440
- [Pestov] V. G. Pestov, *Hyperlinear and sofic groups: a brief guide*, The Bulletin of Symbolic Logic 14 (2008), 449–480; arXiv:0804.3968, Sections 4 and 6. https://arxiv.org/abs/0804.3968
- [Capraro–Lupini] V. Capraro and M. Lupini, *Introduction to sofic and hyperlinear groups and Connes' embedding conjecture*, Lecture Notes in Mathematics 2136 (2015); arXiv:1309.2034, Section II.13. https://arxiv.org/abs/1309.2034
- [Phung] X. K. Phung, *A geometric generalization of Kaplansky's direct finiteness conjecture*, Proceedings of the American Mathematical Society 151 (2023), 2863–2871; arXiv:2111.07930. https://arxiv.org/abs/2111.07930
- [Son 2026] J. Son, *Soficity of one-relator groups and reducible presentations*, arXiv:2610.02213 (October 2026). https://arxiv.org/abs/2610.02213
