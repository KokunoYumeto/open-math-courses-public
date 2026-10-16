# Traces of projections and the Baum–Connes conjecture

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The reduced group \(C^*\)-algebra \(C_r^*(G)\) of a countable group \(G\) carries a canonical trace \(\tau\), and every projection \(b\) in it has a trace \(\tau(b)\in[0,1]\). The Baum–Connes conjecture predicts the \(K\)-theory of \(C_r^*(G)\) from the geometry of proper actions of \(G\), and a theorem of Lück shows that every class it predicts has a rational trace. OpenAI constructed in 2026 a finitely generated group \(G_{\mathrm{sur}}\) and a projection \(b_0\in C_r^*(G_{\mathrm{sur}})\) whose trace is the irrational number \(\sum_ip^{-k_i}\) [OpenAI-IT, Theorem 1.1]. So the assembly map of \(G_{\mathrm{sur}}\) is not surjective, and the reduced Baum–Connes conjecture fails. This course proves the construction. This lesson sets up traces of projections and the group \(K_0\), states the conjecture and Lück's theorem, deduces the failure from the construction, and lays out the proof.

- The reduced group \(C^*\)-algebra and its trace (Section 1).
- Projections and \(K_0\) (Section 2).
- The assembly map and the trace theorem (Section 3).
- The theorem (Section 4).
- Context (Section 5).
- The plan of the construction (Section 6).

## 1. The reduced group \(C^*\)-algebra and its trace

Let \(G\) be a countable group with identity \(1\), and let \(L(g)\), \(g\in G\), be the left translations of \(\ell^2(G)\), \(L(g)\delta_h=\delta_{gh}\). The *reduced group \(C^*\)-algebra* \(C_r^*(G)\) is the norm closure of the linear span of the operators \(L(g)\). It is a unital \(C^*\)-algebra of operators on \(\ell^2(G)\), and every element of the group ring \(\mathbb CG\) acts on \(\ell^2(G)\) as an element \(\sum_ga_gL(g)\) of it.

Every \(L(g)\) commutes with every right translation, and so does every norm limit of linear combinations of them. Hence \(C_r^*(G)\) lies in the algebra \(\mathcal M\) of operators that commute with the right translations, the algebra of [The regular trace and spectral phase](course:the-kervaire-conjecture/the-regular-trace-and-spectral-phase), Section 1, for the group \(G\). Its *canonical trace* is
\[
\tau(b)=\langle b\,\delta_1,\delta_1\rangle\qquad(b\in C_r^*(G)),
\]
so that \(\tau\bigl(\sum_ga_gL(g)\bigr)=a_1\) on the group ring. On the matrix algebra \(M_n(C_r^*(G))\subseteq M_n(\mathcal M)\) we use \(\tau_n(b)=\sum_{j}\tau(b_{jj})\), and we write \(\tau\) for \(\tau_n\) when the size is clear.

**Lemma 1.1.** For \(a,b\in M_n(C_r^*(G))\): \(\tau(ab)=\tau(ba)\); if \(b\ge0\), then \(\tau(b)\ge0\), with equality only for \(b=0\); and \(\tau(I_n)=n\).

*Proof.* The first two statements are Lemma 1.3 of [The regular trace and spectral phase](course:the-kervaire-conjecture/the-regular-trace-and-spectral-phase), applied to elements of \(M_n(C_r^*(G))\subseteq M_n(\mathcal M)\); positivity in \(M_n(C_r^*(G))\) is positivity as an operator on \(\ell^2(G)^n\), by spectral permanence (Theorem 3.2 of [C\*-algebras, continuous functional calculus, automatic continuity and positive cones](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones)). The last one holds because \(\tau(1)=\langle\delta_1,\delta_1\rangle=1\). \(\square\)

## 2. Projections and \(K_0\)

A *projection* in a \(C^*\)-algebra is an element \(p\) with \(p=p^*=p^2\). Let \(A\) be a unital \(C^*\)-algebra. Two projections \(p,q\in M_n(A)\) are *equivalent*, \(p\sim q\), if \(p=x^*x\) and \(q=xx^*\) for some \(x\in M_n(A)\). A projection \(p\in M_n(A)\) is identified with \(p\oplus0\in M_{n+1}(A)\), and the *direct sum* of \(p\in M_m(A)\) and \(q\in M_n(A)\) is the block-diagonal projection \(p\oplus q\in M_{m+n}(A)\). The equivalence classes form a commutative monoid under \(\oplus\), and \(K_0(A)\) is its Grothendieck group: its elements are formal differences \([p]-[q]\), with \([p]-[q]=[p']-[q']\) exactly when \(p\oplus q'\oplus r\sim p'\oplus q\oplus r\) for some projection \(r\) [Valette 2026, Definition 3.8].

**Lemma 2.1** (the trace on \(K_0\)). Let \(A=C_r^*(G)\).

1. If \(p\sim q\), then \(\tau(p)=\tau(q)\). Moreover \(\tau(p\oplus q)=\tau(p)+\tau(q)\), and \(\tau(p\oplus0)=\tau(p)\).
2. There is a unique homomorphism \(\tau_*:K_0(A)\to\mathbb R\) with \(\tau_*([p]-[q])=\tau(p)-\tau(q)\).
3. A projection \(p\in M_n(A)\) satisfies \(0\le\tau(p)\le n\), and \(\tau(p)=0\) only for \(p=0\). In particular \([p]\ne0\) in \(K_0(A)\) for every projection \(p\ne0\).

*Proof.* (1) If \(p=x^*x\) and \(q=xx^*\), Lemma 1.1 gives \(\tau(p)=\tau(x^*x)=\tau(xx^*)=\tau(q)\). The trace of a block-diagonal matrix is the sum of the traces of its blocks.

(2) By (1), \(p\mapsto\tau(p)\) is constant on equivalence classes and additive, so it is a homomorphism of monoids into \(\mathbb R\). If \([p]-[q]=[p']-[q']\), applying it to \(p\oplus q'\oplus r\sim p'\oplus q\oplus r\) gives \(\tau(p)+\tau(q')=\tau(p')+\tau(q)\). So the formula defines \(\tau_*\), which is additive; uniqueness is clear.

(3) A projection satisfies \(0\le p=p^*p\le I_n\), so \(0\le\tau(p)\le n\) by Lemma 1.1, and \(\tau(p)=0\) forces \(p=0\). If \([p]=0\), then \(\tau(p)=\tau_*([p])=0\). \(\square\)

So two projections with different traces have different classes in \(K_0\), and a projection with irrational trace has a class with irrational image under \(\tau_*\).

**Example 2.2.** If \(g\in G\) has finite order \(N\ge2\), then \(p_g=\frac1N\sum_{k=0}^{N-1}L(g^k)\) is a projection with \(\tau(p_g)=\frac1N\), different from \(0\) and \(1\) [Valette 2026, Example 4.3]. For a finite group \(G\), every projection in \(M_n(C_r^*(G))\) has trace in \(\frac1{|G|}\mathbb Z\) (Exercise 7.2).

## 3. The assembly map and the trace theorem

The Baum–Connes conjecture concerns a homomorphism
\[
\mu_0^G:K_0^G(\underline EG)\longrightarrow K_0(C_r^*(G)),
\]
the *assembly map*, and its analogue \(\mu_1^G\) in degree one. Here \(\underline EG\) is the classifying space for proper actions of \(G\): a proper \(G\)-space whose fixed-point set is contractible for every finite subgroup and empty for every infinite subgroup. The domain is its equivariant \(K\)-homology with \(G\)-compact supports, and \(\mu_j^G\) takes a geometric class to the index of an equivariant operator [Valette 2026, Sections 5 to 7, Definition 7.17]. The *reduced Baum–Connes conjecture* (without coefficients) asserts that \(\mu_0^G\) and \(\mu_1^G\) are isomorphisms for every countable group \(G\) [Valette 2026, Conjecture 2.1].

These objects are not constructed in the programme. The course uses them only through the following theorem, which is not proved in the programme and is recorded as an open obligation of this course.

**(LUCK)** (the trace of assembly; [Lück, Theorem 0.3]). For every countable group \(G\) and every \(x\in K_0^G(\underline EG)\),
\[
\begin{gathered}
\tau_*\bigl(\mu_0^G(x)\bigr)\in\Lambda_G,\\
\Lambda_G=\mathbb Z\Bigl[\tfrac1{|F|}:F\le G\text{ finite}\Bigr]\subseteq\mathbb Q .
\end{gathered}
\]

Lück states this with \(\Lambda_G\otimes_{\mathbb Z}K_0^G(\underline EG)\) as domain and the trace of the group von Neumann algebra, which restricts to \(\tau\) on \(C_r^*(G)\); an integral class \(x\) corresponds to \(1\otimes x\) [Lück, Section 0]. The domain is the same equivariant \(K\)-homology with \(G\)-compact supports [OpenAI-IT, Section 1].

## 4. The theorem

**Theorem 4.1** (OpenAI [OpenAI-IT, Theorem 1.1]). There are a finitely generated group \(G_{\mathrm{sur}}\), a prime \(p>2\), integers \(0<k_1<k_2<\cdots\) with \(k_{i+1}-k_i\to\infty\), and a projection \(b_0\in C_r^*(G_{\mathrm{sur}})\) with
\[
\tau(b_0)=\sum_{i\ge1}p^{-k_i}.
\]

The proof occupies the rest of the course. The number \(\tau(b_0)\) is irrational:

**Lemma 4.2.** Let \(p\ge2\) be an integer and \(0<k_1<k_2<\cdots\) integers with \(k_{i+1}-k_i\to\infty\). Then \(x=\sum_ip^{-k_i}\) is irrational.

*Proof.* For an integer \(n\ge0\), the number \(p^nx\) is the sum of the integer \(\sum_{k_i\le n}p^{n-k_i}\) and of \(\sum_{k_i>n}p^{n-k_i}\), which is a sum of distinct powers \(p^{-m}\), \(m\ge1\), missing infinitely many \(m\); so it is less than \(\sum_{m\ge1}p^{-m}\le1\). Hence \(\lfloor p^nx\rfloor=\sum_{k_i\le n}p^{n-k_i}\), and the digits
\[
d_n=\lfloor p^nx\rfloor-p\lfloor p^{n-1}x\rfloor\qquad(n\ge1)
\]
are \(d_n=1\) for \(n\in\{k_1,k_2,\ldots\}\) and \(d_n=0\) otherwise. Suppose \(x=a/b\) with integers \(a\ge0\), \(b\ge1\), and let \(r_n\in\{0,\ldots,b-1\}\) be the remainder of \(p^na\) modulo \(b\). Then \(p^nx-\lfloor p^nx\rfloor=r_n/b\), so \(d_n=\lfloor pr_{n-1}/b\rfloor\), and \(r_n\) is the remainder of \(pr_{n-1}\) modulo \(b\). The sequence \((r_n)\) takes finitely many values and each term determines the next, so it is eventually periodic, and so is \((d_n)\), with some period \(P\). An eventually periodic sequence with infinitely many terms equal to \(1\) has, from some point on, a \(1\) in every \(P\) consecutive terms. Then \(k_{i+1}-k_i\le P\) for all large \(i\), a contradiction. \(\square\)

**Corollary 4.3** (failure of Baum–Connes). The class \([b_0]\in K_0(C_r^*(G_{\mathrm{sur}}))\) is not in the image of \(\mu_0^{G_{\mathrm{sur}}}\). So the reduced Baum–Connes conjecture without coefficients fails for the countable group \(G_{\mathrm{sur}}\).

*Proof.* By Lemma 2.1, \(\tau_*([b_0])=\tau(b_0)\), which is irrational by Lemma 4.2. By (LUCK), every class in the image of \(\mu_0^{G_{\mathrm{sur}}}\) has a rational image under \(\tau_*\). \(\square\)

The same argument shows that \([b_0]\otimes1\) is not in the image of the rationalized map \(\mu_0^{G_{\mathrm{sur}}}\otimes\mathrm{id}_{\mathbb Q}\): every element of that image is a finite rational combination of assembly classes, whose trace is rational [OpenAI-IT, Section 6]. The group \(G_{\mathrm{sur}}\) has elements of order \(p\), so Example 2.2 already gives projections with trace \(\frac1p\); the point of Theorem 4.1 is a trace outside \(\mathbb Q\).

## 5. Context

Baum and Connes formulated the conjecture in 1982; it has been proved for amenable groups, for Gromov-hyperbolic groups and for many others, and before the work described here no counterexample without coefficients was known [Valette 2026, Section 2; OpenAI-IT, Section 1]. A counterexample with suitable commutative coefficients was found by Higson, Lafforgue and Skandalis, using expanders [OpenAI-IT, Section 1]. Groups whose Cayley graphs contain expanders isometrically were constructed by Osajda, and the Baum–Connes conjecture with coefficients fails for them [Osajda, Corollary 3.3]; such a group, with a module over a finite field attached, is the starting point of the construction here.

Baum and Connes also conjectured that the traces of projections over \(C_r^*(G)\) lie in the subgroup generated by the numbers \(1/|F|\) for finite subgroups \(F\); Roy disproved this form, and Lück proved that the Baum–Connes conjecture implies the weaker statement that the traces lie in the ring \(\Lambda_G\) [Lück, Section 0], which is (LUCK) together with surjectivity. Theorem 4.1 gives a trace outside \(\mathbb Q\) altogether.

Irrational traces were known for projections in the group von Neumann algebra, which is larger than \(C_r^*(G)\): they arise as dimensions of kernels of group-ring elements, in connection with Atiyah's question on \(L^2\)-Betti numbers, for instance for lamplighter groups, which satisfy the Baum–Connes conjecture [OpenAI-IT, Section 1]. The kernel projection of a self-adjoint element lies in \(C_r^*(G)\) itself when the spectrum has a gap at \(0\); the construction makes such a gap uniform, as in the work of Li, Nowak and Pooya on Kazhdan projections [OpenAI-IT, Section 1; Pooya–Ren–Wang]. The family of manuscripts containing Theorem 4.1 also gives a finitely generated torsion-free group with a projection of trace strictly between \(0\) and \(\frac12\), against the Kadison–Kaplansky conjecture [OpenAI-KK, Theorem 1.1]; see [Idempotents and integral traces](course:bass-trace-conjecture/idempotents-and-integral-traces), Section 6. A third manuscript of the family gives a finitely generated torsion-free group for which reduced assembly is not even rationally injective [OpenAI-BCI, Theorem 1.1]; see [The reduced assembly map and the torus class](course:reduced-baum-connes-injectivity/the-reduced-assembly-map-and-the-torus-class).

## 6. The plan of the construction

The group is \(G_{\mathrm{sur}}=V\rtimes\Gamma\), where \(\Gamma\) is a finitely generated group whose Cayley graph contains a sequence of finite expanders \(\Theta_i\) isometrically, and \(V\) is a quotient of the finitely supported functions \(\Gamma\to\mathbb F_p\) by relations taken from linear codes on the copies of the \(\Theta_i\). After a Fourier transform in \(V\), an operator \(T\in C_r^*(G_{\mathrm{sur}})\) becomes a family of graph Laplacians \(dI-\operatorname{Adj}(G_\omega)\) of random subgraphs \(G_\omega\) of the Cayley graph, indexed by points \(\omega\) of the compact dual of \(V\). The kernel of each of them is spanned by the constants on the copies of expanders that the random pattern leaves intact, and its spectrum has a uniform gap above \(0\). The kernel projection \(b_0\) therefore lies in \(C_r^*(G_{\mathrm{sur}})\), and its trace counts intact copies through the identity, with probabilities \(p^{-k_i}\).

- [Graphical presentations and coned diagrams](graphical-presentations-and-coned-diagrams.md): labelled graphs, the group \(\Gamma\), copies, the coned Cayley graph and the counting of arcs in minimal diagrams.
- [Thin triangles and simultaneous overlaps](thin-triangles-and-simultaneous-overlaps.md): hyperbolicity of the coned graph with a universal constant, and one small ball containing all overlaps of a copy with copies no farther from a root.
- [Labelled expanders and cycle spaces](labelled-expanders-and-cycle-spaces.md): the choice of expanders and of the labelling, and the decomposition of the cycle space of the Cayley graph into the cycle spaces of the copies.
- [Codes and the lamp module](codes-and-the-lamp-module.md): codes with large primal and dual distance, the module \(V\), the group \(G_{\mathrm{sur}}\), and the exact distribution of patterns on each copy.
- [Fourier decomposition and enabled graphs](fourier-decomposition-and-enabled-graphs.md): the decomposition of \(\ell^2(G_{\mathrm{sur}})\) over the dual of \(V\), the trace formula, the operator \(T\), and the edge deficits of invalid copies and of finite sets.
- [The spectral gap and an irrational trace](the-spectral-gap-and-an-irrational-trace.md): the uniform spectral gap, the projection \(b_0\) and its trace, and the proof of Theorem 4.1.

## 7. Exercises

**7.1** (easy). Let \(G=\{1,g\}\) be the group of order two. Show that the projections in \(C_r^*(G)\) are \(0\), \(1\), \(\frac12(1+L(g))\) and \(\frac12(1-L(g))\), and compute their traces.

**7.2** (medium). Let \(G\) be finite. Show that for \(b\in M_n(C_r^*(G))\) the operator trace of \(b\) on \(\mathbb C^n\otimes\ell^2(G)\) equals \(|G|\,\tau(b)\), and deduce that every projection in \(M_n(C_r^*(G))\) has trace in \(\frac1{|G|}\mathbb Z\).

**7.3** (easy). Let \(u\in M_n(C_r^*(G))\) be unitary and \(p\in M_n(C_r^*(G))\) a projection. Show that \(upu^*\sim p\), and that \(\tau(upu^*)=\tau(p)\).

**7.4** (medium). Find the digits \(d_n\) of Lemma 4.2 for \(x=\frac14\) in base \(p=3\), and check that they are eventually periodic. Then show that \(\sum_{i\ge1}3^{-i^2}\) is irrational.

## 8. Solutions

**7.1.** \(C_r^*(G)\) is spanned by \(1\) and \(L(g)\), and \(L(g)^2=1\). An element \(a+bL(g)\) is a projection exactly when \(a,b\) are real (self-adjointness) and \(a^2+b^2=a\), \(2ab=b\). If \(b=0\), then \(a\in\{0,1\}\); if \(b\ne0\), then \(a=\frac12\) and \(b=\pm\frac12\). The traces are \(0\), \(1\), \(\frac12\), \(\frac12\).

**7.2.** By Lemma 1.1 of [The regular trace and spectral phase](course:the-kervaire-conjecture/the-regular-trace-and-spectral-phase), the diagonal coefficient \(\langle b_{jj}\delta_x,\delta_x\rangle\) of an element of \(\mathcal M\) equals \(\langle b_{jj}\delta_1,\delta_1\rangle=\tau(b_{jj})\) for every \(x\). Summing over the \(n|G|\) basis vectors \(e_j\otimes\delta_x\) gives \(|G|\sum_j\tau(b_{jj})=|G|\,\tau(b)\). The operator trace of a projection on a finite-dimensional space is its rank, an integer, so \(\tau(p)\in\frac1{|G|}\mathbb Z\).

**7.3.** With \(x=pu^*\): \(x^*x=upu^*\) and \(xx^*=pu^*up=p\). Lemma 2.1(1) gives equal traces; directly, \(\tau(upu^*)=\tau(pu^*u)=\tau(p)\).

**7.4.** For \(x=\frac14\), \(b=4\) and \(r_0=1\); then \(r_n\) is the remainder of \(3r_{n-1}\) modulo \(4\), so \(r_n=3,1,3,1,\ldots\), and \(d_n=\lfloor3r_{n-1}/4\rfloor\) gives \(d_1=0\), \(d_2=2\), \(d_3=0\), \(d_4=2,\ldots\): indeed \(\frac14=\sum_{m\ge1}2\cdot3^{-2m}\). For \(\sum_i3^{-i^2}\), the exponents \(k_i=i^2\) satisfy \(k_{i+1}-k_i=2i+1\to\infty\), so Lemma 4.2 applies.

## References

- [OpenAI-IT] OpenAI, *An irrational-trace counterexample to reduced Baum–Connes*, OpenAI Math Release preprint, 23 September 2026, Theorems 1.1 and 1.2, Sections 1 and 6. https://github.com/openai/math/tree/main/preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026
- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Theorem 1.1. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Theorem 1.1. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
- [Lück] W. Lück, *The relation between the Baum–Connes conjecture and the trace conjecture*, Inventiones Mathematicae 149 (2002), 123–152; on the author's university page, Section 0 and Theorem 0.3. https://www.math.uni-bonn.de/people/lueck/data/trc.pdf
- [Valette 2026] A. Valette, *The Baum–Connes conjecture: a concise course*, arXiv:2610.01802, Conjecture 2.1, Definition 3.8, Example 4.3, Sections 5 to 7 and Definition 7.17. https://arxiv.org/abs/2610.01802
- [Osajda] D. Osajda, *Small cancellation labellings of some infinite graphs and applications*, Acta Mathematica 225 (2020); arXiv:1406.5015, Section 1 and Corollary 3.3. https://arxiv.org/abs/1406.5015
- [Pooya–Ren–Wang] S. Pooya, B. Ren and H. Wang, *Higher Kazhdan projections for one relator groups*, arXiv:2609.00493, abstract. https://arxiv.org/abs/2609.00493
