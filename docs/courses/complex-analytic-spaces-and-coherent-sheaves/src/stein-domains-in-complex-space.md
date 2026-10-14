# Stein domains in complex space

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Hörmander's existence theorem solves \(\bar\partial u=g\) with locally square integrable data on every open subset of \(\mathbf C^n\) with a smooth strictly plurisubharmonic exhaustion. This lesson turns it into statements about holomorphic functions and coherent sheaves on such sets, which we call Stein domains. The cohomology of the structure sheaf vanishes in positive degrees; holomorphic functions on a sublevel set of the exhaustion are limits of holomorphic functions on the whole domain; and every coherent sheaf with a finite free resolution has no higher cohomology on any Stein domain inside the domain of the resolution. Since every point of a complex space has such resolutions nearby, this gives each point a basis of neighbourhoods on which a given coherent sheaf is acyclic.

We use [The Dolbeault complex](the-dolbeault-complex.md), [Plurisubharmonic functions and Stein manifolds](plurisubharmonic-functions-and-stein-manifolds.md), Hörmander's L² estimates on pseudoconvex domains, and, for coherent sheaves, [Coherent sheaves and Oka's coherence theorem](coherent-sheaves-and-okas-theorem.md) and [Cartan's coherence theorem and complex spaces](cartans-coherence-theorem-and-complex-spaces.md).

Basic references are [Demailly] and [Hörmander 1965].

A **Stein domain** in this lesson is an open subset of \(\mathbf C^n\) with a smooth strictly plurisubharmonic exhaustion function, that is, an open subset of \(\mathbf C^n\) that is a Stein manifold.

## 1. Square integrable holomorphic functions

**Lemma 1.1 (mean value inequality).** If \(F\) is holomorphic near a closed polydisc \(\overline\Delta(a;r)\), then

\[
|F(a)|^2\leq\frac1{\lambda(\Delta(a;r))}\int_{\Delta(a;r)}|F|^2\,d\lambda .
\]

**Proof.** For \(0<s_j\leq r_j\), the Cauchy formula of Holomorphic functions of several variables, Theorem 1.2, written in polar coordinates, gives \(F(a)=(2\pi)^{-n}\int F(a_1+s_1e^{i\theta_1},\ldots,a_n+s_ne^{i\theta_n})\,d\theta\). Multiply by \(s_1\cdots s_n\) and integrate over \(0<s_j<r_j\): \(F(a)\) is the average of \(F\) over \(\Delta(a;r)\). Apply the Cauchy–Schwarz inequality. \(\square\)

**Lemma 1.2 (holomorphy of weak solutions).** Let \(U\subset\mathbf C^n\) be open and \(u\) locally integrable on \(U\) with \(\partial u/\partial\bar z_j=0\) for all \(j\) in the sense of distributions. Then \(u\) agrees almost everywhere with a holomorphic function.

**Proof.** Let \(\rho_\varepsilon\) be a mollifier and \(U_\varepsilon\) the set of points at distance more than \(\varepsilon\) from the complement of \(U\). Then \(u_\varepsilon=u*\rho_\varepsilon\) is smooth on \(U_\varepsilon\) with \(\partial u_\varepsilon/\partial\bar z_j=(\partial u/\partial\bar z_j)*\rho_\varepsilon=0\), so \(u_\varepsilon\) is holomorphic, and \(u_\varepsilon\to u\) in \(L^1\) on compact subsets. Lemma 1.1 holds with \(|F|\) and the \(L^1\) average in place of \(|F|^2\) and the \(L^2\) average (by the same averaging), so on each compact set \(K\subset U\) the functions \(u_\varepsilon\) are uniformly Cauchy as \(\varepsilon\to0\). Their uniform limit on compact sets is holomorphic by Holomorphic functions of several variables, Theorem 3.1 and equals \(u\) almost everywhere. \(\square\)

By Lemma 1.1, on \(\mathcal O(U)\) the \(L^2\) norms over polydiscs control the supremum norms over smaller polydiscs. Hence a sequence of holomorphic functions converging in \(L^2\) on a neighbourhood of a compact set \(K\) converges uniformly on \(K\).

## 2. The square integrable Dolbeault complex

Let \(U\subset\mathbf C^n\) be open. For \(q\geq0\), let \(\mathcal L^{0,q}(U)\) be the space of \((0,q)\)-forms \(f\) on \(U\) whose coefficients are locally square integrable and whose distributional \(\bar\partial f\) also has locally square integrable coefficients. These spaces form sheaves \(\mathcal L^{0,q}\), and \(\bar\partial\) maps \(\mathcal L^{0,q}\) to \(\mathcal L^{0,q+1}\).

**Theorem 2.1.** On every open set of \(\mathbf C^n\), the sequence of sheaves

\[
0\longrightarrow\mathcal O\longrightarrow\mathcal L^{0,0}\xrightarrow{\ \bar\partial\ }\mathcal L^{0,1}\xrightarrow{\ \bar\partial\ }\cdots\xrightarrow{\ \bar\partial\ }\mathcal L^{0,n}\longrightarrow0
\tag{2.1}
\]

is exact, the sheaves \(\mathcal L^{0,q}\) have no higher cohomology on any open set, and consequently

\[
H^q(U,\mathcal O)\cong\frac{\ker\bigl(\bar\partial:\mathcal L^{0,q}(U)\to\mathcal L^{0,q+1}(U)\bigr)}{\bar\partial\,\mathcal L^{0,q-1}(U)}\qquad(q\geq0,\ U\text{ open}).
\]

**Proof.** Exactness at \(\mathcal L^{0,0}\) is Lemma 1.2. For \(q\geq1\), a \(\bar\partial\)-closed germ of \(\mathcal L^{0,q}\) at \(x\) is represented by a form \(g\) on a ball \(B\) about \(x\), which is a Stein domain [Plurisubharmonic functions and Stein manifolds, Examples 2.3](plurisubharmonic-functions-and-stein-manifolds.md#2-stein-manifolds). By Hörmander's L² estimates, Corollary 5.2 there is \(u\) on \(B\) with locally square integrable coefficients and \(\bar\partial u=g\); then \(u\in\mathcal L^{0,q-1}(B)\). Each \(\mathcal L^{0,q}\) is a module over smooth functions, because \(\bar\partial(\chi f)=\bar\partial\chi\wedge f+\chi\,\bar\partial f\) in the sense of distributions; so it has no higher cohomology on any open set, by [The Dolbeault complex, Lemma 3.1](the-dolbeault-complex.md#3-fine-sheaves-and-the-dolbeault-isomorphism). An acyclic resolution computes cohomology [Stacks, Tag 015E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-leray-acyclicity). \(\square\)

**Theorem 2.2.** If \(\Omega\subset\mathbf C^n\) is a Stein domain, then \(H^q(\Omega,\mathcal O)=0\) for every \(q\geq1\). Consequently \(H^q(\Omega,\mathcal O^p)=0\) for \(q\geq1\) and every \(p\).

**Proof.** A \(\bar\partial\)-closed element of \(\mathcal L^{0,q}(\Omega)\) has locally square integrable coefficients, so it is \(\bar\partial\)-exact in \(\mathcal L^{0,\bullet}(\Omega)\) by Corollary 5.2(2) of the previous lesson. Apply Theorem 2.1. \(\square\)

By the examples of [Plurisubharmonic functions and Stein manifolds, Section 2](plurisubharmonic-functions-and-stein-manifolds.md#2-stein-manifolds), this applies to balls, polydiscs (also with infinite radii), finite intersections of these, the sets \((\mathbf C^*)^a\times\mathbf C^{n-a}\) and the sublevel sets of the exhaustions of Stein domains. In particular \(H^q(\Delta(R),\mathcal O)=0\) for \(q\geq1\), completing Corollary 3.4 of the Dolbeault lesson.

<span id="l2-dolbeault-exact-inputs"></span>

**Exact inputs for the locally square-integrable resolution.** Theorem 2.1 uses the original locally \(L^2\) domains, not a replacement by smooth forms or a different norm. If a germ \(g\) of degree \(q\geq1\) is closed, choose a representative on a neighbourhood and shrink until \(\bar\partial g=0\) there. A smaller Euclidean ball \(B\) has a smooth strictly plurisubharmonic exhaustion by [Examples 2.3](course:complex-analytic-spaces-and-coherent-sheaves/plurisubharmonic-functions-and-stein-manifolds#2-stein-manifolds). The [complete weight construction and shell argument for Hörmander Corollary 5.2](course:complex-analytic-spaces-and-coherent-sheaves/hormanders-l2-estimates-on-pseudoconvex-domains#weighted-shell-integrability) give a locally square-integrable \(u\) on \(B\) with \(\bar\partial u=g\). Since \(g\) is itself locally square integrable, \(u\) belongs to the precise sheaf \(\mathcal L^{0,q-1}\), including its weak-derivative condition. In degree zero, the local \(L^2\) function is locally \(L^1\) by Cauchy–Schwarz on compact neighbourhoods, so Lemma 1.2 identifies the kernel with \(\mathcal O\), as an almost-everywhere class with a holomorphic representative.

For a smooth function \(\chi\), both \(\chi\) and its first derivatives are bounded on every compact subset. The distributional product rule therefore gives
\[
\bar\partial(\chi f)=\bar\partial\chi\wedge f+\chi\,\bar\partial f\in L^2_{\mathrm{loc}}
\quad\text{when }f\in\mathcal L^{0,q}.
\]
Thus each term is a smooth-module sheaf. Its acyclicity on every open set follows from the [section-lifting proof in Dolbeault, Lemma 3.1](course:complex-analytic-spaces-and-coherent-sheaves/the-dolbeault-complex#smooth-module-acyclicity-programme-proof), with no need to infer derived cohomology from one chosen cover. Again \(\bar\partial\) is not smooth-function-linear, so this complex is considered in abelian sheaves, or in holomorphic modules using the proved coefficient comparison.

The resolution is finite in degrees \(0,\ldots,n\). Apply [the bounded-below acyclic-resolution theorem](course:derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors#why-acyclic-terms-suffice-in-the-bounded-below-case) to \(\Gamma(U,-)\). This proves the displayed cohomology quotient in Theorem 2.1 for every open \(U\), including \(q=0\) with zero incoming term. On a Stein domain, Corollary 5.2(2) solves every closed positive-degree global element in this same domain sheaf, giving Theorem 2.2. For \(\mathcal O^p\), use the finite direct sum of these resolutions; kernels and images are computed componentwise, so the same vanishing holds. This argument uses neither approximation from Section 3 nor the later coherent-sheaf vanishing theorem, and therefore does not reverse that dependency order.

## 3. Approximation on sublevel sets

**Theorem 3.1.** Let \(\Omega\subset\mathbf C^n\) be a Stein domain with smooth strictly plurisubharmonic exhaustion \(\psi_0\), and let \(\Omega_b=\{\psi_0<b\}\). Every holomorphic function on \(\Omega_b\) is the limit, uniformly on compact subsets of \(\Omega_b\), of holomorphic functions on \(\Omega\).

**Proof.** Let \(h\in\mathcal O(\Omega_b)\) and let \(L\subset\Omega_b\) be compact. Choose \(b_0<b'<b\) with \(L\subset\Omega_{b_0}\), possible because \(\psi_0\) attains a maximum smaller than \(b\) on \(L\). The closure of \(\Omega_{b'}\) is compact in \(\Omega_b\), so there is a smooth \(\eta\) with compact support in \(\Omega_b\) and \(\eta=1\) on \(\Omega_{b'}\). The \((0,1)\)-form \(g=\bar\partial(\eta h)=h\,\bar\partial\eta\) is smooth, \(\bar\partial\)-closed, and has compact support contained in \(\{b'\leq\psi_0\}\). Choose a smooth convex nondecreasing \(\theta\) with \(\theta=0\) on \((-\infty,b_0]\) and \(\theta\geq1\) on \([b',\infty)\).

Fix \(\psi\) as in (3.1) and \(\varphi\) satisfying (5.1) of the previous lesson. For \(\nu=1,2,\ldots\) the weight \(\varphi+\nu\,\theta\circ\psi_0\) still satisfies (5.1), by Corollary 5.2(1) there, so Theorem 5.1 there gives \(u_\nu\) with \(\bar\partial u_\nu=g\) and

\[
\int_\Omega|u_\nu|^2e^{-\varphi-\nu\theta\circ\psi_0+2\psi}\leq\int_\Omega|g|^2e^{-\varphi-\nu\theta\circ\psi_0+\psi}\leq e^{-\nu}\int_\Omega|g|^2e^{-\varphi+\psi},
\]

because \(\theta\circ\psi_0\geq1\) on the support of \(g\). Since \(\theta\circ\psi_0=0\) on \(\Omega_{b_0}\) and the weight \(e^{-\varphi+2\psi}\) is bounded below on the relatively compact set \(\Omega_{b_0}\), \(u_\nu\to0\) in \(L^2(\Omega_{b_0})\).

Put \(h_\nu=\eta h-u_\nu\) on \(\Omega\). Then \(\bar\partial h_\nu=g-g=0\), so \(h_\nu\in\mathcal O(\Omega)\) by Lemma 1.2. On \(\Omega_{b'}\), \(\bar\partial u_\nu=g=0\), so \(u_\nu\) is holomorphic there, and \(u_\nu\to0\) in \(L^2(\Omega_{b_0})\). By Lemma 1.1, \(u_\nu\to0\) uniformly on \(L\), which is a compact subset of \(\Omega_{b_0}\); hence \(h_\nu=h-u_\nu\to h\) uniformly on \(L\). Choosing an exhaustion of \(\Omega_b\) by compact sets and a diagonal sequence gives convergence on every compact subset. \(\square\)

The same holds for \(\mathbf C^p\)-valued holomorphic functions, component by component.

<span id="stein-approximation-convex-ramp"></span>

**The convex ramp, the quantitative compact estimate, and the diagonal choice.** Here are the construction and convergence details in Theorem 3.1. If \(\Omega_b\) is empty the claim is vacuous, with the zero functions on \(\Omega\) as an approximating sequence. Otherwise a prescribed nonempty compact \(L\subset\Omega_b\) has \(\max_L\psi_0<b\); choose \(b_0<b'<b\) as in the proof. The closed set \(\overline{\Omega_{b'}}\) is compact and lies in \(\Omega_b\). By [Local tools, Theorem 3.1](course:DG-FND/local-tools-for-bundles-and-transport#3-smooth-weights-with-controlled-support), there is a smooth cutoff equal to one on a neighbourhood of this closure and supported in \(\Omega_b\). Its support is compact: it is closed in \(\Omega\) and contained in the compact closure of \(\Omega_b\). The product \(\eta h\), extended by zero to \(\Omega\), is smooth. Its derivative \(g\) has compact support in \(\{\psi_0\geq b'\}\), and \(\bar\partial g=\bar\partial^2(\eta h)=0\).

Use the already-constructed normalized smooth step \(\sigma\) from [the convex-weight construction](course:complex-analytic-spaces-and-coherent-sheaves/hormanders-l2-estimates-on-pseudoconvex-domains#convex-weight-construction). It satisfies \(\sigma=0\) on \(( -\infty,0]\), \(\sigma=1\) on \([1,\infty)\), \(\sigma'\geq0\), and \(J=\int_0^1\sigma(s)\,ds>0\). With \(\delta=b'-b_0>0\), define
\[
\theta(t)=\frac1J\int_0^{(t-b_0)/\delta}\sigma(s)\,ds.
\]
It is smooth on all of \(\mathbf R\), and
\[
\theta'(t)=\frac{\sigma((t-b_0)/\delta)}{\delta J}\geq0,\qquad
\theta''(t)=\frac{\sigma'((t-b_0)/\delta)}{\delta^2J}\geq0.
\]
For \(t\leq b_0\) the integral is zero, including the reversed integration interval. At \(t=b'\) it equals one. Hence \(\theta=0\) on \(( -\infty,b_0]\) and \(\theta\geq1\) on \([b',\infty)\), exactly the two cutoff levels required in the proof.

Choose the fixed \(\varphi\) using Corollary 5.2(1); it is independent of \(\nu\). The same corollary, with its proved Levi-form calculation, says that every \(\Phi_\nu=\varphi+\nu\theta\circ\psi_0\) satisfies the hypothesis (5.1) of [Theorem 5.1](course:complex-analytic-spaces-and-coherent-sheaves/hormanders-l2-estimates-on-pseudoconvex-domains#5-the-existence-theorem). Put
\[
C=\int_\Omega|g|^2e^{-\varphi+\psi}\,d\lambda<\infty.
\]
Smoothness and compact support make this finite. In particular \(g\) belongs to every required weighted space and is weakly closed. The theorem supplies solutions with the exact bound
\[
\int_\Omega|u_\nu|^2e^{-\Phi_\nu+2\psi}\,d\lambda\leq e^{-\nu}C.
\]
The closure of \(\Omega_{b_0}\) is a nonempty compact subset of \(\Omega\). Thus
\[
c_0=\min_{\overline{\Omega_{b_0}}}e^{-\varphi+2\psi}>0,\qquad
\int_{\Omega_{b_0}}|u_\nu|^2\,d\lambda\leq c_0^{-1}C e^{-\nu}.
\]
This uses \(\theta\circ\psi_0=0\) on \(\Omega_{b_0}\); it does not require a positive lower bound for the varying weight on all of \(\Omega\).

On \(\Omega_{b'}\), the functions \(u_\nu\) have holomorphic representatives by Lemma 1.2. Choose a single \(r>0\) such that every closed polydisc \(\overline\Delta(z;r,\ldots,r)\), \(z\in L\), lies in \(\Omega_{b_0}\); compactness of \(L\) inside that open set gives such an \(r\). Write \(v_r=\lambda(\Delta(0;r,\ldots,r))>0\). Lemma 1.1, at each original centre \(z\), gives the uniform estimate
\[
\sup_{z\in L}|u_\nu(z)|\leq
\left(\frac{C}{c_0v_r}\right)^{1/2}e^{-\nu/2}.
\]
Globally, \(\eta h-u_\nu\) is locally square integrable and weakly holomorphic. Take its holomorphic representative \(h_\nu\) by Lemma 1.2. On \(\Omega_{b'}\) the identity \(h_\nu=h-u_\nu\) holds everywhere for the chosen holomorphic representatives: it holds almost everywhere, and a continuous function zero almost everywhere is zero, since any nonzero value would persist on an open set of positive measure. The displayed bound therefore proves uniform approximation on \(L\).

Finally choose a compact exhaustion \(L_j\subset\operatorname{int}L_{j+1}\) of \(\Omega_b\), as supplied by Local tools, Lemma 3.A. For each \(j\), carry out the preceding construction for \(L_j\), and choose one resulting holomorphic function \(H_j\in\mathcal O(\Omega)\) with
\[
\sup_{L_j}|H_j-h|\leq 2^{-j}.
\]
Such a choice is possible from the explicit exponential bound; if its constant is zero, any \(\nu\geq1\) suffices. Empty initial exhaustion sets may be discarded. Every compact subset of \(\Omega_b\) is contained in some \(L_N\), since the interiors cover it and compactness gives a finite subcover. For \(j\geq N\) the same error bound holds there, and tends to zero. This constructs one sequence converging on every compact subset, rather than a separate limiting family for each compact set. Finite-dimensional vector-valued approximation follows componentwise, with the finite sum of squared component errors controlling the original Euclidean norm.

*Stein-domain dependency integration and approximation details: GPT-6 Astra (OpenAI), Ultra, 13 October 2026; author self-check, CC0. Original statements, proofs, variants, citations and author credits remain. No independent whole-course review is claimed.*

## 4. Coherent sheaves on Stein domains

**Theorem 4.1.** Let \(\Omega\subset\mathbf C^N\) be open and \(\mathcal S\) a coherent sheaf on \(\Omega\) with a finite free resolution

\[
0\longrightarrow\mathcal O^{p_m}\longrightarrow\cdots\longrightarrow\mathcal O^{p_1}\longrightarrow\mathcal O^{p_0}\longrightarrow\mathcal S\longrightarrow0
\tag{4.1}
\]

on \(\Omega\). Then for every Stein domain \(V\subset\Omega\), \(H^k(V,\mathcal S)=0\) for \(k\geq1\), and \(\mathcal O^{p_0}(V)\to\mathcal S(V)\) is surjective.

**Proof.** Let \(\mathcal Z_l\) be the kernel of \(\mathcal O^{p_l}\to\mathcal O^{p_{l-1}}\) (with \(\mathcal O^{p_{-1}}=\mathcal S\)), so that there are exact sequences \(0\to\mathcal Z_l\to\mathcal O^{p_l}\to\mathcal Z_{l-1}\to0\), with \(\mathcal Z_{-1}=\mathcal S\) and \(\mathcal Z_{m-1}=\mathcal O^{p_m}\). By Theorem 2.2, \(H^k(V,\mathcal O^p)=0\) for \(k\geq1\). The long exact cohomology sequences give \(H^k(V,\mathcal Z_{l-1})\cong H^{k+1}(V,\mathcal Z_l)\) for \(k\geq1\), and \(H^k(V,\mathcal Z_{m-1})=0\) for \(k\geq1\). By descending induction on \(l\), \(H^k(V,\mathcal Z_l)=0\) for all \(k\geq1\) and all \(l\geq-1\). For \(l=0\), \(H^1(V,\mathcal Z_0)=0\) gives the surjectivity of \(\mathcal O^{p_0}(V)\to\mathcal S(V)\). \(\square\)

**Definition 4.2.** Let \(X\) be a complex space and \(\mathcal S\) a coherent \(\mathcal O_X\)-module. A **distinguished patch** for \(\mathcal S\) is an open set \(U\subset X\) with an isomorphism of \(U\) onto a local model \(A=V(\mathcal J)\subset\Omega\subset\mathbf C^N\), such that the pushforward \(i_*\mathcal S\) to \(\Omega\) has a finite free resolution (4.1) on \(\Omega\).

**Proposition 4.3.** Let \(\mathcal S\) be a coherent sheaf on a complex space \(X\).

1. Every point of \(X\) has a neighbourhood which is a distinguished patch for \(\mathcal S\), and every open subset \(A\cap\Omega'\), \(\Omega'\subset\Omega\) open, of a distinguished patch is again one.
2. If \(U\cong A\subset\Omega\) is a distinguished patch and \(V\subset\Omega\) is a Stein domain, then \(H^k(A\cap V,\mathcal S)=0\) for all \(k\geq1\), and \(\mathcal O^{p_0}(V)\to\mathcal S(A\cap V)\) is surjective.
3. Consequently every point of \(X\) has a basis of open neighbourhoods \(W\) such that \(H^k(W,\mathcal S)=0\) for all \(k\geq1\), and, if \(X\) is a manifold, such that every finite intersection of such neighbourhoods inside one chart is again acyclic.

**Proof.** (1) Choose a local model \(A\subset\Omega\) around the point. The sheaf \(i_*\mathcal S\) is coherent on \(\Omega\) by [Cartan's coherence theorem and complex spaces, Theorem 3.2](cartans-coherence-theorem-and-complex-spaces.md#3-complex-spaces), and by the local syzygy theorem [Coherent sheaves and Oka's coherence theorem, Theorem 3.4](coherent-sheaves-and-okas-theorem.md#3-the-category-of-coherent-analytic-sheaves) it has a finite free resolution on a smaller neighbourhood \(\Omega_0\) of the point; replace \(\Omega\) by \(\Omega_0\) and \(A\) by \(A\cap\Omega_0\). Restricting a resolution to a smaller open set gives a resolution. (2) \(H^k(A\cap V,\mathcal S)=H^k(V,i_*\mathcal S)\) by Theorem 3.2(3) of the lesson on complex spaces, and Theorem 4.1 applies to \(i_*\mathcal S\) on \(V\). (3) Take \(W=A\cap B\) for small balls \(B\subset\Omega\) about the point. On a manifold, take \(A=\Omega\); finite intersections of balls are Stein domains (Proposition 2.2(4) of the lesson on Stein manifolds). \(\square\)

On a singular complex space, intersections of patches embedded in different charts need a separate argument, given in the lesson on finiteness on compact complex spaces.

<span id="finite-resolution-stein-application"></span>

**Exact resolution and patch inputs for Section 4.** The finite resolution used in Proposition 4.3 is genuinely available on one open neighbourhood. [Oka, Corollary 3.3 and Theorem 3.4](coherent-sheaves-and-okas-theorem.md#3-the-category-of-coherent-analytic-sheaves) prove this in two steps: the finite coordinate Koszul complex and minimal-resolution argument bound the stalk resolution length by the ambient dimension, and coherent kernels plus Proposition 3.2 spread the finitely many chosen maps and the final free kernel to one common neighbourhood. We use that complete existing argument, not an assumption that all stalkwise free choices automatically glue to a global resolution. For a singular local model it is the coherent ambient pushforward that receives this resolution, not a claim that every module on the singular local ring has finite projective dimension.

In Theorem 4.1, a resolution of length zero says directly \(\mathcal S\cong\mathcal O^{p_0}\); [Theorem 2.2](stein-domains-in-complex-space.md#2-the-square-integrable-dolbeault-complex) gives positive-degree vanishing, and the displayed map on sections is already an isomorphism. This includes rank zero. For \(m\geq1\), the leftmost injection identifies \(\mathcal Z_{m-1}\) with \(\mathcal O^{p_m}\). For \(l=m-1,m-2,\ldots,0\), use only the exact sequences
\[
0\longrightarrow\mathcal Z_l\longrightarrow\mathcal O^{p_l}
\longrightarrow\mathcal Z_{l-1}\longrightarrow0,
\qquad\mathcal Z_{-1}=\mathcal S.
\]
Restriction to the open Stein domain is exact. The [long exact cohomology sequence](course:AG-QC/cohomology-of-sheaves-on-ringed-spaces#1-the-obstruction-that-cohomology-records), with its [derived-functor construction](course:derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors#4-right-derived-functors-on-bounded-below-complexes), gives the dimension-shifting isomorphisms in the original proof. Starting with the acyclic free \(\mathcal Z_{m-1}\) and descending proves all the claimed vanishings, including \(\mathcal Z_0\). The initial segment then gives the required surjection on sections. No \(\mathcal Z_m\) or negative-length resolution is needed.

For a distinguished patch, [the closed-model proof of Cartan Theorem 3.2(3)](cartans-coherence-theorem-and-complex-spaces.md#closed-model-module-and-cohomology-inputs) proves both the coherence needed before applying local syzygies and the equality
\[
H^k(A\cap V,\mathcal S)=H^k(V,(i_*\mathcal S)|_V).
\]
Here the same notation \(V\) as in Proposition 4.3 denotes the ambient Stein open; \(A\cap V\) is closed in it. The exact pushforward argument applies to the actual, possibly nonreduced, model. Moreover \((i_*\mathcal S)(V)=\mathcal S(A\cap V)\) by definition, so the surjectivity conclusion of Theorem 4.1 is precisely the asserted map to sections on the patch.

For the neighbourhood basis, choose small balls inside the ambient resolution neighbourhood. They are Stein by [Examples 2.3](plurisubharmonic-functions-and-stein-manifolds.md#2-stein-manifolds), so the preceding comparison gives acyclicity of their intersections with \(A\). Such sets form a relative neighbourhood basis. On a manifold, for a finite intersection of the chosen balls in one chart, [Proposition 2.2(4)](plurisubharmonic-functions-and-stein-manifolds.md#2-stein-manifolds) proves the intersection is Stein by summing bounded-below strictly plurisubharmonic exhaustions. The intersection lies in the resolution neighbourhood belonging to any one of its balls; restrict that resolution and apply Theorem 4.1. Thus no simultaneous global choice of resolutions for all the balls is required. An empty intersection has zero sections and cohomology and causes no exception. This proves the stated same-chart conclusion; the separate singular-space chart-intersection argument remains in its later lesson.

*Coherent-sheaf application integration: GPT-6 Astra (OpenAI), Ultra, 13 October 2026; author self-check, CC0. This is a scoped dependency reconciliation, not independent review or whole-course certification.*

## 5. Exercises

**Exercise 5.1.** Use Theorem 2.2 to show that \(H^1(\mathbf C^*,\mathcal O)=0\), and deduce that for every holomorphic \(f\) on \(\mathbf C^*\) one can write \(f=h_1-h_2\) with \(h_1\) entire and \(h_2\) holomorphic on \(\mathbf C^*\) and tending to \(0\) at infinity; then verify this directly with Laurent series.

*Solution.* \(\mathbf C^*\) is a Stein domain (Examples 2.3), so \(H^1(\mathbf C^*,\mathcal O)=0\). Directly: write \(f=\sum_{k\in\mathbf Z}a_kz^k\) on \(\mathbf C^*\); then \(h_1=\sum_{k\geq0}a_kz^k\) is entire (the Laurent series converges on all of \(\mathbf C^*\), so its nonnegative part converges on \(\mathbf C\)), and \(h_2=-\sum_{k<0}a_kz^k\) is holomorphic on \(\mathbf C^*\) and tends to \(0\) at infinity.

**Exercise 5.2.** Let \(\Omega=\{|z|<1\}\subset\mathbf C\) and \(\Omega_b=\{|z|<1/2\}\). Show directly that every \(h\in\mathcal O(\Omega_b)\) is a uniform limit on compact subsets of \(\Omega_b\) of functions in \(\mathcal O(\Omega)\), and that the analogous statement fails for the annulus \(\Omega_b'=\{1/4<|z|<1/2\}\subset\Omega\).

*Solution.* The partial sums of the Taylor series of \(h\) at \(0\) are polynomials, hence holomorphic on \(\Omega\), and they converge uniformly on compact subsets of \(\Omega_b\). For the annulus, \(1/z\) is not a limit: if \(p_\nu\in\mathcal O(\Omega)\) converged uniformly to \(1/z\) on the circle \(|z|=3/8\), then \(\int_{|z|=3/8}p_\nu\,dz=0\) would converge to \(\int_{|z|=3/8}dz/z=2\pi i\). The annulus is not a sublevel set of a strictly subharmonic exhaustion of \(\Omega\): such a set has no holes, by the maximum principle.

**Exercise 5.3.** Let \(\mathcal S=\mathcal O/(z_1,z_2)\) on \(\mathbf C^2\), the skyscraper sheaf at \(0\). Write down a finite free resolution and verify Theorem 4.1 on the ball.

*Solution.* The Koszul complex \(0\to\mathcal O\xrightarrow{(-z_2,\,z_1)}\mathcal O^2\xrightarrow{(z_1,\,z_2)}\mathcal O\to\mathcal S\to0\) is exact: at \(\mathcal O^2\), a relation \(g_1z_1+g_2z_2=0\) is a multiple of \((-z_2,z_1)\) by Exercise 4.1 of the lesson on Oka's theorem, and the first map is injective. On a ball \(B\), \(\mathcal S(B)=\mathbf C\) if \(0\in B\) and \(0\) otherwise, \(H^k(B,\mathcal S)=0\) for \(k\geq1\) since a skyscraper sheaf is flasque, and \(\mathcal O(B)\to\mathcal S(B)\) is evaluation at \(0\), which is surjective.

## References

- [Demailly] J.-P. Demailly, *Complex Analytic and Differential Geometry*, version of 21 June 2012, freely available from the author with permission to copy, modify and redistribute with credit. <https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf>
- [Hörmander 1965] L. Hörmander, \(L^2\) estimates and existence theorems for the \(\bar\partial\) operator, *Acta Mathematica* 113 (1965), 89–152. <https://doi.org/10.1007/BF02391775>
- [Stacks] The Stacks project, cited by tag; each tag links to the same result in the AI Integrated Stacks Project. <https://stacks.math.columbia.edu/>
