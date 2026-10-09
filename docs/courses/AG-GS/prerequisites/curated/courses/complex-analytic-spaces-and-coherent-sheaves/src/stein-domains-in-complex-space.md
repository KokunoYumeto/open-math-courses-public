# Stein domains in complex space

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Hörmander's existence theorem solves \(\bar\partial u=g\) with locally square integrable data on every open subset of \(\mathbf C^n\) with a smooth strictly plurisubharmonic exhaustion. This lesson turns it into statements about holomorphic functions and coherent sheaves on such sets, which we call Stein domains. The cohomology of the structure sheaf vanishes in positive degrees; holomorphic functions on a sublevel set of the exhaustion are limits of holomorphic functions on the whole domain; and every coherent sheaf with a finite free resolution has no higher cohomology on any Stein domain inside the domain of the resolution. Since every point of a complex space has such resolutions nearby, this gives each point a basis of neighbourhoods on which a given coherent sheaf is acyclic.

We use The Dolbeault complex, Plurisubharmonic functions and Stein manifolds, [Hörmander's L² estimates on pseudoconvex domains](hormanders-l2-estimates-on-pseudoconvex-domains.md), and, for coherent sheaves, [Coherent sheaves and Oka's coherence theorem](coherent-sheaves-and-okas-theorem.md) and Cartan's coherence theorem and complex spaces.

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

**Proof.** Exactness at \(\mathcal L^{0,0}\) is Lemma 1.2. For \(q\geq1\), a \(\bar\partial\)-closed germ of \(\mathcal L^{0,q}\) at \(x\) is represented by a form \(g\) on a ball \(B\) about \(x\), which is a Stein domain Plurisubharmonic functions and Stein manifolds, Examples 2.3. By [Hörmander's L² estimates, Corollary 5.2](hormanders-l2-estimates-on-pseudoconvex-domains.md#5-the-existence-theorem) there is \(u\) on \(B\) with locally square integrable coefficients and \(\bar\partial u=g\); then \(u\in\mathcal L^{0,q-1}(B)\). Each \(\mathcal L^{0,q}\) is a module over smooth functions, because \(\bar\partial(\chi f)=\bar\partial\chi\wedge f+\chi\,\bar\partial f\) in the sense of distributions; so it has no higher cohomology on any open set, by The Dolbeault complex, Lemma 3.1. An acyclic resolution computes cohomology [Stacks, Tag 015E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-leray-acyclicity). \(\square\)

**Theorem 2.2.** If \(\Omega\subset\mathbf C^n\) is a Stein domain, then \(H^q(\Omega,\mathcal O)=0\) for every \(q\geq1\). Consequently \(H^q(\Omega,\mathcal O^p)=0\) for \(q\geq1\) and every \(p\).

**Proof.** A \(\bar\partial\)-closed element of \(\mathcal L^{0,q}(\Omega)\) has locally square integrable coefficients, so it is \(\bar\partial\)-exact in \(\mathcal L^{0,\bullet}(\Omega)\) by Corollary 5.2(2) of the previous lesson. Apply Theorem 2.1. \(\square\)

By the examples of Plurisubharmonic functions and Stein manifolds, Section 2, this applies to balls, polydiscs (also with infinite radii), finite intersections of these, the sets \((\mathbf C^*)^a\times\mathbf C^{n-a}\) and the sublevel sets of the exhaustions of Stein domains. In particular \(H^q(\Delta(R),\mathcal O)=0\) for \(q\geq1\), completing Corollary 3.4 of the Dolbeault lesson.

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

**Proof.** (1) Choose a local model \(A\subset\Omega\) around the point. The sheaf \(i_*\mathcal S\) is coherent on \(\Omega\) by Cartan's coherence theorem and complex spaces, Theorem 3.2, and by the local syzygy theorem [Coherent sheaves and Oka's coherence theorem, Theorem 3.4](coherent-sheaves-and-okas-theorem.md#3-the-category-of-coherent-analytic-sheaves) it has a finite free resolution on a smaller neighbourhood \(\Omega_0\) of the point; replace \(\Omega\) by \(\Omega_0\) and \(A\) by \(A\cap\Omega_0\). Restricting a resolution to a smaller open set gives a resolution. (2) \(H^k(A\cap V,\mathcal S)=H^k(V,i_*\mathcal S)\) by Theorem 3.2(3) of the lesson on complex spaces, and Theorem 4.1 applies to \(i_*\mathcal S\) on \(V\). (3) Take \(W=A\cap B\) for small balls \(B\subset\Omega\) about the point. On a manifold, take \(A=\Omega\); finite intersections of balls are Stein domains (Proposition 2.2(4) of the lesson on Stein manifolds). \(\square\)

On a singular complex space, intersections of patches embedded in different charts need a separate argument, given in the lesson on finiteness on compact complex spaces.

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
