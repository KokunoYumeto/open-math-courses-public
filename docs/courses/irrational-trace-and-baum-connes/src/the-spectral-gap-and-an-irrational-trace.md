# The spectral gap and an irrational trace

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson finishes the proof of Theorem 4.1 of [Traces of projections and the Baum–Connes conjecture](traces-of-projections-and-the-baum-connes-conjecture.md). The deficit estimate of [Fourier decomposition and enabled graphs](fourier-decomposition-and-enabled-graphs.md) turns, by the discrete Cheeger argument, into a lower bound \(\frac{c^2}{8d}\) for the Laplacian \(\pi_\omega(T)\) on the part of the enabled graph outside the valid copies; on each valid copy the Laplacian of an expander has its own gap \(\rho\) above the constants. So in every representation \(\pi_\omega\) the spectrum of \(T\) lies in \(\{0\}\cup[\varepsilon,2d]\) for one \(\varepsilon>0\), and the kernel projection \(b_0\) is a continuous function of \(T\): it lies in \(C_r^*(G_{\mathrm{sur}})\) itself, not only in the group von Neumann algebra [OpenAI-IT, Lemma 5.4 and Proposition 5.5]. Its trace counts the valid copies through the identity, and equals \(\sum_ip^{-k_i}\) [OpenAI-IT, Proposition 6.1].

- The uniform spectral gap (Section 1).
- The projection (Section 2).
- The trace and the theorem (Section 3).

We use the continuous functional calculus (Theorem 5.1), spectral permanence (Theorem 3.2), the isometry of injective \(*\)-homomorphisms (Corollary 4.6) and the compatibility of the calculus with \(*\)-homomorphisms (Corollary 5.4) from [C\*-algebras, continuous functional calculus, automatic continuity and positive cones](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones).

## 1. The uniform spectral gap

Fix \(\omega\in\Omega\). On \(U_\omega\), the set of elements of \(\Gamma\) in no valid copy, write \(\deg_\omega(x)\) for the number of enabled edges at \(x\) and \(q(x)=d-\deg_\omega(x)\ge0\). Since no enabled edge leaves \(U_\omega\), the space \(\ell^2(U_\omega)\) is invariant under \(\pi_\omega(T)=dI-\operatorname{Adj}(G_\omega)\), and for finitely supported \(\xi\) on \(U_\omega\)
\[
\begin{aligned}
\mathcal E(\xi)&=\langle\pi_\omega(T)\xi,\xi\rangle\\
&=\sum_{\{x,y\}}|\xi(x)-\xi(y)|^2\\
&\quad+\sum_xq(x)|\xi(x)|^2 ,
\end{aligned}\tag{1.1}
\]
the first sum over the enabled edges in \(U_\omega\). For a finite set \(F\subseteq U_\omega\), counting the incidences at \(F\),
\[
\begin{aligned}
&d|F|-2|E(G_\omega|_F)|\\
&\quad=|\partial F|+\sum_{x\in F}q(x),
\end{aligned}\tag{1.2}
\]
where \(\partial F\) is the set of enabled edges with one end in \(F\), the other necessarily in \(U_\omega\setminus F\).

**Lemma 1.1** (uniform spectral gap; [OpenAI-IT, Lemma 5.4]). For every \(\omega\in\Omega\):

1. \(\pi_\omega(T)\ge\frac{c^2}{8d}I\) on \(\ell^2(U_\omega)\);
2. with \(\varepsilon=\min\{\rho,c^2/(8d)\}>0\), the kernel of \(\pi_\omega(T)\) is the closed span of the indicator functions \(\mathbf1_P\) of the valid copies \(P\), and \(\pi_\omega(T)\ge\varepsilon I\) on its orthogonal complement;
3. the spectrum of \(\pi_\omega(T)\) is contained in \(K=\{0\}\cup[\varepsilon,2d]\).

*Proof.* (1) Let \(\xi\) be finitely supported on \(U_\omega\) and \(s=|\xi|\). For \(t\ge0\), the set \(F_t=\{x:s(x)^2>t\}\) is finite, and Lemma 3.2 of the previous lesson with (1.2) gives \(|\partial F_t|+\sum_{F_t}q\ge\frac c2|F_t|\). Integrate over \(t\in[0,\infty)\): an edge \(\{x,y\}\) lies in \(\partial F_t\) exactly for \(t\) between \(s(x)^2\) and \(s(y)^2\), and \(x\in F_t\) exactly for \(t<s(x)^2\), so
\[
\begin{aligned}
\frac c2\|\xi\|^2&\le\sum_{\{x,y\}}|s(x)^2-s(y)^2|\\
&\quad+\sum_xq(x)s(x)^2 .
\end{aligned}
\]
Write \(|s(x)^2-s(y)^2|\) as \(|s(x)-s(y)|\,(s(x)+s(y))\) and \(q(x)s(x)^2\) as \((\sqrt{q(x)}s(x))^2\), and apply the Cauchy–Schwarz inequality to all the terms together: \(\frac c2\|\xi\|^2\le\mathcal A^{1/2}\mathcal B^{1/2}\), where
\[
\begin{aligned}
\mathcal A&=\sum_{\{x,y\}}|s(x)-s(y)|^2+\sum_xq\,s^2,\\
\mathcal B&=\sum_{\{x,y\}}(s(x)+s(y))^2+\sum_xq\,s^2.
\end{aligned}
\]
Here \(\mathcal A\le\mathcal E(\xi)\), since \(\bigl||\xi(x)|-|\xi(y)|\bigr|\le|\xi(x)-\xi(y)|\). In \(\mathcal B\), \((s(x)+s(y))^2\le2s(x)^2+2s(y)^2\), so \(\mathcal B\le\sum_x(2\deg_\omega(x)+q(x))s(x)^2\), which is at most \(2d\|\xi\|^2\) because \(2\deg_\omega+q=d+\deg_\omega\le2d\). Hence \(\mathcal E(\xi)\ge\frac{c^2}{8d}\|\xi\|^2\). Finitely supported vectors are dense in \(\ell^2(U_\omega)\) and \(\pi_\omega(T)\) is bounded, so (1) follows.

(2) The valid copies are pairwise disjoint components of \(G_\omega\), each with exactly its own edges (Section 2 of the previous lesson), so \(\ell^2(\Gamma)\) is the orthogonal sum of the spaces \(\ell^2(P)\), \(P\) valid, and \(\ell^2(U_\omega)\), each invariant. On \(\ell^2(P)\), with \(P\) of type \(i\), \(\pi_\omega(T)\) is \(dI-\operatorname{Adj}(P)\), which by (1.1) of the lesson on labelled expanders vanishes exactly on the constants, \(P\) being connected, and is at least \(\rho I\) on their orthogonal complement (Proposition 2.1 there, transported by \(\psi_P\)). Together with (1), this gives (2), also when there are infinitely many valid copies or none, since both lower bounds are uniform.

(3) \(\pi_\omega(T)\) is self-adjoint with \(0\le\pi_\omega(T)\le2dI\) (Lemma 2.2 of the previous lesson). For real \(\lambda\notin K\), \(\pi_\omega(T)-\lambda\) is \(-\lambda\ne0\) on the kernel, and on its invariant orthogonal complement it is at least \(\varepsilon-\lambda>0\) if \(\lambda<\varepsilon\), and at most \(2d-\lambda<0\) if \(\lambda>2d\); so it is invertible. Nonreal \(\lambda\) are not in the spectrum of a self-adjoint operator. \(\square\)

## 2. The projection

**Proposition 2.1** (a projection in the reduced algebra; [OpenAI-IT, Proposition 5.5]). Let \(\chi(x)=\max\{0,1-x/\varepsilon\}\) on \(\mathbb R\). Then \(b_0=\chi(T)\) is a projection in \(C_r^*(G_{\mathrm{sur}})\), and for every \(\omega\), \(\pi_\omega(b_0)\) is the orthogonal projection onto the kernel of \(\pi_\omega(T)\). In particular \(\langle\pi_\omega(b_0)\delta_1,\delta_1\rangle\) is \(1/n_i\) if \(1\) lies in a valid copy of type \(i\), and \(0\) if \(1\in U_\omega\); the valid copy in the first case is unique.

*Proof.* Let \(\Phi=\bigoplus_\omega\pi_\omega\), a \(*\)-homomorphism from \(C_r^*(G_{\mathrm{sur}})\) to the bounded operators on \(H=\bigoplus_\omega\ell^2(\Gamma)\). By Proposition 1.1(3) of the previous lesson it is isometric, so it is a \(*\)-isomorphism onto a \(C^*\)-subalgebra of \(B(H)\), and by spectral permanence the spectrum of \(T\) in \(C_r^*(G_{\mathrm{sur}})\) is the spectrum of the operator \(\Phi(T)\). For \(\lambda\notin K\), Lemma 1.1(3) and the continuous functional calculus give \(\|(\pi_\omega(T)-\lambda)^{-1}\|\le1/\operatorname{dist}(\lambda,K)\) for every \(\omega\), so the direct sum of these inverses is a bounded inverse of \(\Phi(T)-\lambda\). Hence the spectrum of \(T\) in \(C_r^*(G_{\mathrm{sur}})\) is contained in \(K\).

On \(K\), \(\chi\) takes the value \(1\) at \(0\) and \(0\) on \([\varepsilon,2d]\), so \(\chi=\bar\chi=\chi^2\) there, and \(b_0=\chi(T)\), defined by the continuous functional calculus in \(C_r^*(G_{\mathrm{sur}})\), is a projection. The calculus commutes with the \(*\)-homomorphism \(\pi_\omega\), so \(\pi_\omega(b_0)=\chi(\pi_\omega(T))\), which by Lemma 1.1 is the identity on the kernel of \(\pi_\omega(T)\) and zero on its orthogonal complement. By Lemma 1.1(2), this is the orthogonal projection onto the closed span of the \(\mathbf1_P\), \(P\) valid, which are pairwise orthogonal; at a vertex of a valid copy \(P\) of type \(i\), its diagonal entry is that of the projection onto \(n_i^{-1/2}\mathbf1_P\), namely \(1/n_i\), and at a vertex of \(U_\omega\) it is \(0\). The valid copy containing \(1\) is unique because distinct valid copies are disjoint. \(\square\)

The gap is essential. In the group von Neumann algebra every self-adjoint element has a kernel projection, but a continuous function of \(T\) can only isolate the point \(0\) of the spectrum when it is isolated (Exercise 4.4). Here it is isolated uniformly in \(\omega\), and this is what puts \(b_0\) into the reduced \(C^*\)-algebra.

## 3. The trace and the theorem

**Proposition 3.1** (the trace; [OpenAI-IT, Proposition 6.1]).
\[
\tau(b_0)=\sum_{i\ge1}p^{-k_i}.\tag{3.1}
\]

*Proof.* For each \(i\), exactly \(n_i\) copies of type \(i\) contain \(1\): the copies \(P_{\phi_i(v)^{-1},i}\), \(v\) a vertex of \(\Theta_i\) (Exercise 6.2 of [Graphical presentations and coned diagrams](graphical-presentations-and-coned-diagrams.md)). For each such copy \(P\), the set \(E_P\) of \(\omega\) for which \(P\) is valid has measure \(p^{-k_i}\), by Lemma 3.1 of [Codes and the lamp module](codes-and-the-lamp-module.md). Distinct valid copies are disjoint, so the sets \(E_P\) for the copies containing \(1\), of all types, are pairwise disjoint. By Proposition 2.1, the integrand of the trace formula of Proposition 1.1(4) of the previous lesson is \(\sum_i\sum_{P\ni1,\ \text{type }i}\frac1{n_i}\mathbf1_{E_P}\), a sum of nonnegative measurable functions. Hence
\[
\tau(b_0)=\sum_{i\ge1}n_i\cdot\frac1{n_i}\,p^{-k_i}=\sum_{i\ge1}p^{-k_i},
\]
which is (3.1). \(\square\)
No independence between the events \(E_P\) is needed, only their disjointness.

*Proof of Theorem 4.1 of the first lesson.* The group \(G_{\mathrm{sur}}\) is finitely generated (Lemma 2.3 of [Codes and the lamp module](codes-and-the-lamp-module.md)); \(p>2\) is prime; the integers \(k_i=\lfloor n_i/2\rfloor\) increase strictly with \(k_{i+1}-k_i\to\infty\) (Proposition 2.1 of [Labelled expanders and cycle spaces](labelled-expanders-and-cycle-spaces.md)); \(b_0\in C_r^*(G_{\mathrm{sur}})\) is a projection (Proposition 2.1); and its trace is \(\sum_ip^{-k_i}\) (Proposition 3.1). \(\square\)

With Lemma 4.2 and Corollary 4.3 of the first lesson, \(\tau(b_0)\) is irrational, and \([b_0]\) is not in the image of the Baum–Connes assembly map of \(G_{\mathrm{sur}}\), given Lück's theorem (LUCK).

**What the course proves and what it assumes.** The lessons prove the construction and the trace computation completely, with these inputs from outside the programme, each stated where it is used and recorded as an open obligation: (EXP) expanders of logarithmic girth and (OSA) Osajda's labelling theorem (lesson on labelled expanders); and, for the consequence on the Baum–Connes conjecture only, the assembly map with Lück's theorem (LUCK) (first lesson). The \(C^*\)-algebra facts, the trace and the product measure come from earlier courses of the programme, van Kampen diagrams and plane maps from the course [Van Kampen diagrams](course:van-kampen-diagrams/van-kampens-lemma), and thin triangles from short fillings from [Thin triangles, overlap balls and the residual forest](course:kadison-kaplansky-projections/thin-triangles-overlap-balls-and-the-residual-forest), Lemma 2.1.

## 4. Exercises

**4.1** (easy). Show that the function \(\chi\) of Proposition 2.1 could be replaced by any continuous \(\chi'\) with \(\chi'(0)=1\) and \(\chi'=0\) on \([\varepsilon,2d]\), with the same \(b_0\).

**4.2** (medium). Let \(P\) be a finite connected \(d\)-regular graph with \(n\) vertices. Show that the orthogonal projection onto the kernel of \(dI-\operatorname{Adj}(P)\) has all diagonal entries equal to \(1/n\), and compute its trace.

**4.3** (medium). In the \(3\)-regular tree, show that every finite vertex set \(F\) has \(|\partial F|\ge|F|+2\). Following the proof of Lemma 1.1(1) with \(\frac c2\) replaced by \(1\), deduce \(\langle(3I-\operatorname{Adj})\xi,\xi\rangle\ge\frac16\|\xi\|^2\) for all \(\xi\in\ell^2\).

**4.4** (medium). Let \(A=C([0,1])\) and \(T(x)=x\). Show that \(T\) has spectrum \([0,1]\), that \(0\) is not an isolated point, and that no projection \(e\in A\) satisfies \(e(0)=1\) and \(e(x)=0\) for \(x>0\). Relate this to the remark after Proposition 2.1.

## 5. Solutions

**4.1.** \(\chi\) and \(\chi'\) agree on \(K\), which contains the spectrum of \(T\); the continuous functional calculus depends only on the restriction to the spectrum.

**4.2.** By (1.1) of the lesson on labelled expanders, the kernel consists of the functions that are constant on every edge, hence constant, \(P\) being connected. The projection onto \(n^{-1/2}\mathbf1\) has matrix entries \(1/n\), so diagonal entries \(1/n\) and trace \(1\).

**4.3.** A finite set \(F\) of vertices of a tree spans a forest, with at most \(|F|-1\) edges if \(F\ne\varnothing\). So \(|\partial F|=3|F|-2e(F)\ge|F|+2\). In the proof of Lemma 1.1(1) take \(q=0\), \(d=3\) and the bound \(|\partial F_t|\ge|F_t|\): the same computation gives \(\|\xi\|^2\le\mathcal E(\xi)^{1/2}\sqrt6\,\|\xi\|\), so \(\mathcal E(\xi)\ge\frac16\|\xi\|^2\).

**4.4.** \(T-\lambda\) is invertible in \(A\) exactly when \(x-\lambda\) has no zero on \([0,1]\), so the spectrum is \([0,1]\), and \(0\) is a limit of spectral points. A projection in \(A\) is a continuous function with values in \(\{0,1\}\), hence constant on the connected set \([0,1]\); it cannot be \(1\) at \(0\) and \(0\) elsewhere. The kernel projection of \(T\), which exists as the indicator of \(\{0\}\) in the bounded Borel functions, is not continuous. In Proposition 2.1, the uniform gap makes \(0\) isolated, and then the kernel projection is a continuous function of \(T\).

## References

- [OpenAI-IT] OpenAI, *An irrational-trace counterexample to reduced Baum–Connes*, OpenAI Math Release preprint, 23 September 2026, Sections 5.3 and 6, Lemma 5.4, Propositions 5.5 and 6.1. https://github.com/openai/math/tree/main/preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026
