# Holomorphic functions and convergent power series

*Selected from the independently written programme lesson by Claude Opus 5.5 (Anthropic), with scalar prerequisite integration by GPT-6 Astra (OpenAI), in Codex at Ultra. GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026, selected the polydisc and Taylor proofs, supplied the direct power-series converse and local reading links, and self-checked those edits. The programme component is CC0; independent or human review is not asserted. The [source and edition notice](assets/notices/holomorphic-power-series-source-notice.html) preserves the human mathematical credit and exact programme revision.*

Read [The scalar Cauchy formula and power series](scalar-cauchy.md) first: Lemma 0.1 supplies scalar Riemann integration and rectangle interchange, Lemma 1.1 supplies the index of a circle, Theorems 2.1–2.3 supply the disc formula, and Lemma 3.1 supplies termwise differentiation. The scalar real and exponential proofs precede that companion. Here we prove that holomorphic germs have unique convergent power series; the sheaf examples use the cases of one and two complex variables.

## Polydiscs and holomorphy

We write points of \(\mathbf C^n\) as \(z=(z_1,\ldots,z_n)\). For \(a\in\mathbf C^n\) and a vector of radii \(r=(r_1,\ldots,r_n)\) with \(r_j>0\), the **polydisc** and its **distinguished boundary** are

\[
\Delta(a;r)=\{z:\ |z_j-a_j|<r_j\ \text{for all } j\},\qquad
T(a;r)=\{\zeta:\ |\zeta_j-a_j|=r_j\ \text{for all } j\}.
\tag{1.1}
\]

The closed polydisc \(\overline\Delta(a;r)\) is the product of the closed discs. The distinguished boundary is an \(n\)-dimensional torus; for \(n\geq2\) it is much smaller than the topological boundary of the polydisc. Multi-index notation is used throughout: for \(\alpha\in\mathbf N^n\), \(|\alpha|=\alpha_1+\cdots+\alpha_n\), \(\alpha!=\alpha_1!\cdots\alpha_n!\), \(z^\alpha=z_1^{\alpha_1}\cdots z_n^{\alpha_n}\) and \(r^\alpha=r_1^{\alpha_1}\cdots r_n^{\alpha_n}\).

**Definition 1.1.** Let \(U\subset\mathbf C^n\) be open. A function \(f:U\to\mathbf C\) is **holomorphic** if it is continuous and, for every \(j\) and every choice of the other coordinates, the function of one variable \(z_j\mapsto f(z_1,\ldots,z_n)\) is holomorphic on the open set of \(\mathbf C\) where it is defined. The holomorphic functions on \(U\) form a ring \(\mathcal O(U)\).

Continuity is part of this definition.

**Theorem 1.2 (Cauchy formula on a polydisc).** Let \(f\) be holomorphic on a neighbourhood of a closed polydisc \(\overline\Delta(a;r)\). Then for every \(z\in\Delta(a;r)\),

\[
f(z)=\frac1{(2\pi i)^n}\int_{T(a;r)}\frac{f(\zeta)}{(\zeta_1-z_1)\cdots(\zeta_n-z_n)}\,d\zeta_1\cdots d\zeta_n ,
\tag{1.2}
\]

where the integral is the iterated integral over the \(n\) circles \(|\zeta_j-a_j|=r_j\), each oriented counterclockwise.

**Proof.** Induction on \(n\); the case \(n=1\) is [Cauchy's formula, Theorem 2.3](scalar-cauchy.md), with the circle index equal to one by [Lemma 1.1](scalar-cauchy.md). Let \(n\geq2\) and write \(z=(z',z_n)\). For fixed \(\zeta'\) with \(|\zeta_j-a_j|=r_j\) for \(j<n\), the function \(z_n\mapsto f(\zeta',z_n)\) is holomorphic near the closed disc \(|z_n-a_n|\leq r_n\), so

\[
f(\zeta',z_n)=\frac1{2\pi i}\int_{|\zeta_n-a_n|=r_n}\frac{f(\zeta',\zeta_n)}{\zeta_n-z_n}\,d\zeta_n .
\]

For fixed \(z_n\), the function \(z'\mapsto f(z',z_n)\) is holomorphic in \(n-1\) variables near \(\overline\Delta(a';r')\), so the induction hypothesis gives \(f(z',z_n)\) as the \((n-1)\)-fold integral of \(f(\zeta',z_n)/\prod_{j<n}(\zeta_j-z_j)\). Substituting the one-variable formula for \(f(\zeta',z_n)\) gives (1.2) as an iterated integral. The integrand is continuous on the compact torus \(T(a;r)\). Parametrizing each circle and applying [Lemma 0.1(3)](scalar-cauchy.md) interchanges any two adjacent integrations, hence permits every order. \(\square\)

## Power series and regularity

**Theorem 2.1 (power series expansion).** Let \(f\) be holomorphic on a neighbourhood of \(\overline\Delta(a;r)\). Put

\[
c_\alpha=\frac1{(2\pi i)^n}\int_{T(a;r)}\frac{f(\zeta)}{(\zeta-a)^{\alpha+\mathbf 1}}\,d\zeta,
\qquad (\zeta-a)^{\alpha+\mathbf 1}=\prod_{j=1}^n(\zeta_j-a_j)^{\alpha_j+1}.
\tag{2.1}
\]

Then:

1. (Cauchy estimates) \(|c_\alpha|\,r^\alpha\leq\sup_{T(a;r)}|f|\) for every \(\alpha\);
2. the series \(\sum_\alpha c_\alpha(z-a)^\alpha\) converges absolutely and uniformly on every smaller closed polydisc \(\overline\Delta(a;\rho)\), \(\rho_j<r_j\), and its sum is \(f(z)\);
3. \(f\) is infinitely differentiable on \(\Delta(a;r)\); every partial derivative \(\partial^\alpha f=\partial^{|\alpha|}f/\partial z_1^{\alpha_1}\cdots\partial z_n^{\alpha_n}\) is holomorphic and \(\partial^\alpha f(a)=\alpha!\,c_\alpha\).

**Proof.** (1) Estimate (2.1) directly: the torus has total length \(\prod 2\pi r_j\) and \(|\zeta-a|^{\alpha+\mathbf 1}=r^{\alpha+\mathbf 1}\).

(2) For \(z\in\overline\Delta(a;\rho)\) and \(\zeta\in T(a;r)\), put \(q_j=|z_j-a_j|/r_j\leq\rho_j/r_j<1\). The geometric series

\[
\frac1{\zeta_j-z_j}=\sum_{k\geq0}\frac{(z_j-a_j)^k}{(\zeta_j-a_j)^{k+1}}
\]

converges absolutely, with the \(k\)-th term bounded by \(q_j^k/r_j\). Multiplying the \(n\) series, the kernel of (1.2) becomes \(\sum_\alpha(z-a)^\alpha/(\zeta-a)^{\alpha+\mathbf 1}\), with the \(\alpha\)-th term bounded by \(\prod_j q_j^{\alpha_j}/r_j\). This multiple series converges uniformly in \((z,\zeta)\in\overline\Delta(a;\rho)\times T(a;r)\), since \(\sum_\alpha\prod_j(\rho_j/r_j)^{\alpha_j}=\prod_j(1-\rho_j/r_j)^{-1}\). Integrating term by term against the bounded function \(f\) gives \(f(z)=\sum c_\alpha(z-a)^\alpha\), and the Cauchy estimates give \(|c_\alpha(z-a)^\alpha|\leq\sup_T|f|\prod_j(\rho_j/r_j)^{\alpha_j}\), which proves absolute and uniform convergence.

(3) A power series converging absolutely on \(\overline\Delta(a;\rho)\) may be differentiated term by term in each variable on the open polydisc \(\Delta(a;\rho)\), the differentiated series again converging locally uniformly: in each variable this is [Lemma 3.1 and its difference-quotient proof](scalar-cauchy.md), and the bound \(|c_\alpha|\leq M r^{-\alpha}\) shows that \(\sum|\alpha_j c_\alpha(z-a)^{\alpha-e_j}|\) converges uniformly on \(\overline\Delta(a;\rho)\) whenever \(\rho_j<r_j\). Iterating, all partial derivatives \(\partial^\alpha f\) exist, are given by power series, and are continuous; since every point of \(\Delta(a;r)\) is the centre of a closed polydisc on which \(f\) is holomorphic, this holds on all of \(\Delta(a;r)\). The derivatives are holomorphic, being continuous and given by convergent power series in each variable. On each coordinate slice, complex differentiability gives the real partial derivatives \(\partial/\partial x_j=\partial/\partial z_j\) and \(\partial/\partial y_j=i\,\partial/\partial z_j\). Their continuity implies real differentiability: telescope an increment along its finitely many coordinates and use the one-variable fundamental theorem to bound the remainder by the increment size times the local variation of these partial derivatives. Repeating the same argument for their derivatives proves the stated real smoothness. Evaluating the differentiated series at \(a\) gives \(\partial^\alpha f(a)=\alpha!\,c_\alpha\). \(\square\)

**Proposition 2.2 (Holomorphy and locally convergent power series).** A function \(f\) on an open set \(U\subseteq\mathbb C^n\) is holomorphic in the sense of Definition 1.1 if and only if every point has a neighbourhood on which \(f\) is the sum of a power series that converges absolutely on some polydisc and uniformly on each smaller closed polydisc.

**Proof.** If \(f\) is holomorphic, choose about any point \(a\) a closed polydisc whose neighbourhood lies in \(U\), and apply Theorem 2.1.

Conversely, suppose near \(a\)
\[
f(z)=\sum_{\alpha\in\mathbb N^n}c_\alpha(z-a)^\alpha.
\]
Choose positive radii \(R_j\) inside the polydisc of absolute convergence, and write \(A=\sum_\alpha|c_\alpha|R^\alpha<\infty\). Then \(|c_\alpha|\leq A R^{-\alpha}\). For \(0<\rho_j<R_j\), the sum of the absolute values on \(\overline\Delta(a;\rho)\) is bounded by
\[
A\prod_j\sum_{m\geq0}(\rho_j/R_j)^m<\infty.
\]
The corresponding tail bounds prove uniform convergence there. Finite partial sums are continuous; uniform convergence makes \(f\) jointly continuous, by splitting a difference into two uniformly small tails and one continuous finite sum.

For a fixed coordinate slice, group the absolutely convergent sum according to that coordinate's exponent. The finite sum identities and the same absolute tail bound justify the grouping. Its one-variable coefficient series is absolutely convergent at every smaller radius, so Lemma 3.1 of [The scalar Cauchy formula and power series](scalar-cauchy.md) makes the slice complex differentiable. Thus \(f\) is continuous and holomorphic in each coordinate, exactly Definition 1.1. Applying the same lemma repeatedly in each coordinate, with the coefficient bounds above, gives \(\partial^\alpha f(a)=\alpha!c_\alpha\). Consequently every local power-series representation has these uniquely determined coefficients. \(\square\)


## Sources and sheaf examples

The programme's analytic lesson credits Jean-Pierre Demailly and Jiří Lebl. Background readings are Demailly's [Complex Analytic and Differential Geometry](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf) and Lebl's [Tasty Bits of Several Complex Variables, version 3.4](https://www.jirka.org/scv/scv-3.4.pdf). These are scholarly reading links; the full proof used here is the preceding programme argument. The [source and edition notice](assets/notices/holomorphic-power-series-source-notice.html) identifies its selected scope and sources.

Theorems 1.2 and 2.1 and Proposition 2.2 give the local expansions and convergent division used in the holomorphic curve residue resolution and the surface Koszul resolution of the sheaf course.
