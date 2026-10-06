# Curve selection and Łojasiewicz inequalities

*Human treatment: Guillaume Valette, [On subanalytic geometry](https://arxiv.org/abs/2507.23622v1), arXiv:2507.23622v1, 31 July 2025, §2.2, with the Puiseux statement from Proposition 1.8.4. Adapted by GPT-6.1 Sol (OpenAI), Ultra, October 2026. This adapted component is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); Guillaume Valette remains the author of the underlying exposition. Changes: notation and Markdown/MathML formatting; the vector in the inductive choice step is written explicitly; supremum, zero-fibre and uniform-constant details are supplied; the gradient proof explicitly chooses its final integer at least two. This adaptation implies no endorsement.*

Throughout this treatment, **definable** means globally subanalytic. Sets and functions have this property in their ambient Euclidean spaces; a function has it when its graph does. We use the following underlying results from Valette's Chapter 1: finite analytic cell decomposition, closure under Boolean operations and projections, and the one-variable Puiseux theorem. These are distinct prerequisites, not conclusions of the arguments below. The last says that a definable \(u:(0,\eta)\to\mathbb R\), on a smaller interval, has a convergent expansion

\[
u(r)=\sum_{i=m}^{\infty}a_i r^{i/p},\qquad m\in\mathbb Z,\quad p\in\mathbb Z_{>0}.
\]

For a bounded \(u\), negative nonzero powers cannot occur. For finitely many bounded functions choose \(p\) to be twice a common denominator of their Puiseux exponents. Then all \(u(t^p)\) are analytic across zero and agree with the actual compositions for both signs of the parameter. Cell decomposition and Boolean/projection closure also make derivatives, distance functions and bounded fibrewise suprema definable. For example, the graph of a supremum consists of the pairs \((r,s)\) for which \(s\) is an upper bound and every smaller number fails to be an upper bound; this is a formula with quantifiers over a definable graph.

The [analytic finiteness treatment](../analytic-finiteness-for-preparation.html) proves the real Noetherian, Artin–Rees, Krull, formal-linear and finite-coefficient steps behind preparation, reusing the existing analytic division provider. Its later sections now prove the full cell, complement, one-variable Puiseux and parameterized Puiseux providers under the stated projective product convention. We use those proved inputs here.

## Definable choice

Let \(A\subset\mathbb R^m\times\mathbb R^n\) be definable, and let \(B\) be its projection to \(\mathbb R^m\). There is a definable \(f:B\to\mathbb R^n\) with \((x,f(x))\in A\).

**Proof.** We prove it by induction on \(n\). First let \(n=1\). Take a cylindrical cell decomposition compatible with \(A\), refining the base decomposition as necessary. Over a base cell in \(B\), select one of the finitely many cells in \(A\) that projects onto it. For a graph, take its defining function. For a band with finite endpoints \(\zeta<\zeta'\), take \((\zeta+\zeta')/2\). For endpoints \(\zeta,+\infty\), take \(\zeta+1\); for \(-\infty,\zeta'\), take \(\zeta'-1\); for two infinite endpoints, take zero. Each choice lies in the fibre. Combining the finitely many base cells gives a definable function.

For the induction, project \(A\) onto its first \(m+n-1\) coordinates and call the image \(A'\). The induction hypothesis selects \(g:B\to\mathbb R^{n-1}\) in \(A'\). The one-coordinate case selects \(h:A'\to\mathbb R\) with \((x,z,h(x,z))\in A\). Then

\[
f(x)=\bigl(g(x),h(x,g(x))\bigr)
\]

is the required vector. Its graph is definable by Boolean operations and projection. \(\square\)

Continuity of this selection is not asserted over all of \(B\). On a sufficiently small one-dimensional interval, cell decomposition and Puiseux expansion provide the regularity used next.

## Curve selection

Let \(A\subset\mathbb R^n\) be definable and \(x_0\in\overline A\). There is an analytic arc \(\gamma:[0,\epsilon)\to\mathbb R^n\), analytic across its endpoint, with \(\gamma(0)=x_0\) and \(\gamma(r)\in A\) for \(0<r<\epsilon\).

**Proof.** Apply definable choice to

\[
\{(r,x):0<r<1,\ x\in A,\ |x-x_0|<r\}.
\]

Every positive \(r<1\) has a nonempty fibre. We obtain a definable selection \(\beta(r)\) with \(|\beta(r)-x_0|<r\). Thus it is bounded and tends to \(x_0\). Apply the Puiseux theorem to its finitely many coordinates. A common denominator \(p\) and a smaller interval make \(\gamma(t)=\beta(t^p)\) analytic at zero; its constant term is \(x_0\). The positive points stay in \(A\). The convergent power series supplies the stated analytic extension across zero. \(\square\)

## An inequality detected by arcs

Let \(f,g:A\to\mathbb R\) be definable functions on a definable set. Assume \(f\) is bounded. Assume also that along every definable arc \(\gamma:(0,\epsilon)\to A\),

\[
g(\gamma(t))\longrightarrow0
\quad\Longrightarrow\quad f(\gamma(t))\longrightarrow0.
\]

Then there are a positive integer \(N\) and \(C>0\) such that

\[
|f(x)|^N\le C|g(x)|\qquad(x\in A).
\]

**Proof.** Replace the functions by their absolute values. Constant arcs show that \(g(x)=0\) implies \(f(x)=0\). For \(r>0\) in \(g(A)\), define

\[
\phi(r)=\sup\{f(x):x\in A,\ g(x)=r\}.
\]

It is finite by boundedness and definable by the supremum formula. If it did not tend to zero as \(r\) tends to zero in its domain, some \(\delta>0\) would have arbitrarily small positive \(r\) with \(\phi(r)>\delta\). Definable choice would select \(x(r)\) with \(g(x(r))=r\) and \(f(x(r))>\delta\). A definable subset of the line with zero as an accumulation point contains a positive interval ending at zero. Shrinking that interval, the selection is an arc by cell decomposition. It violates the hypothesis. Therefore \(\phi(r)\to0\).

If positive values of \(g\) stay away from zero, boundedness of \(f\) proves the result immediately. Otherwise its positive range contains \((0,\eta)\). If \(\phi\) vanishes on a smaller such interval, the same argument applies outside it. In the remaining case Puiseux expansion gives

\[
\phi(r)=a r^\alpha+\text{higher powers},\qquad a>0,\quad \alpha\in\mathbb Q_{>0}.
\]

Thus \(\phi(r)\le D r^\alpha\) for small \(r>0\). Choose \(N\ge1/\alpha\), shrink so \(r<1\), and obtain \(f(x)^N\le D^N g(x)\) for these fibres. On \(g\ge\eta>0\), a bound \(f\le M\) gives \(f^N\le(M^N/\eta)g\). The zero fibres were already checked. Taking the larger constant proves the claim. \(\square\)

In particular, for continuous definable \(f,g\) on a compact definable \(A\), the condition \(g^{-1}(0)\subset f^{-1}(0)\) suffices. Indeed, a bounded definable arc has a limit by coordinatewise Puiseux expansion. Compactness puts that limit in \(A\); continuity and the zero-set inclusion give the required implication along every arc.

## The gradient inequality

Let \(M\subset\mathbb R^n\) be a definable \(C^1\) submanifold, and let \(f:M\to\mathbb R\) be a definable \(C^1\) function. Write \(\nabla_M f\) for its gradient in the metric induced from Euclidean space. Suppose \(a\in\overline M\) and \(f\) extends continuously at \(a\). There are \(C>0\), a rational \(\rho\in(0,1)\), and a neighborhood of \(a\) such that

\[
|f(x)-f(a)|^\rho\le C|\nabla_M f(x)|\qquad(x\in M).
\]

**Proof of the preliminary radial estimate.** First we prove

\[
|f(x)-f(a)|\le C_0|x-a|\,|\nabla_M f(x)|
\]

near \(a\). Translate so that \(a=0,f(a)=0\). If no such uniform constant existed, definable choice applied to increasingly bad ratios would supply a definable arc \(\gamma(s)\to0\) on which

\[
\frac{|\gamma(s)|\,|\nabla_M f(\gamma(s))|}{|f(\gamma(s))|}\longrightarrow0,
\qquad f(\gamma(s))\ne0.
\]

One can select with \(|\gamma(s)|<s\) and the ratio \(<s\). Puiseux expansions give \(\gamma(s)=bs^k+\cdots\), \(b\ne0,k>0\), and \(f(\gamma(s))=d s^q+\cdots\), \(d\ne0,q>0\). If the gradient vanished identically along the arc, the chain rule would make \(f\circ\gamma\) constant, contrary to its nonzero values and zero limit. Otherwise write \(\nabla_M f(\gamma(s))=c s^\ell+\cdots\), \(c\ne0\). The chain rule and Cauchy–Schwarz give

\[
|(f\circ\gamma)'(s)|
\le|\nabla_M f(\gamma(s))|\,|\gamma'(s)|.
\]

Comparison of leading powers forces \(q-1\ge \ell+k-1\), so \(q\ge k+\ell\). The purported ratio consequently has order \(k+\ell-q\le0\) and cannot tend to zero. This contradiction proves the uniform estimate, including points where the gradient is zero.

**From the radial estimate to the exponent.** Choose a bounded neighborhood on which the radial estimate holds. It implies that a zero gradient has value \(f(a)\). On the definable set \(V\) where the gradient is nonzero, put

\[
G(x)=\frac{|f(x)-f(a)|}{|\nabla_M f(x)|},
\qquad H(x)=|f(x)-f(a)|.
\]

The radial estimate makes \(G\) bounded. We check that \(H\to0\) along any definable arc in \(V\) implies \(G\to0\). Such an arc is bounded and has a limit \(b\). For a constant arc with \(H\to0\), \(G=0\). For a nonconstant arc with nonzero \(H\), Puiseux expansions yield constants \(D>0,\alpha\in\mathbb Q_{>0}\) such that \(H(\gamma(t))\le D|\gamma(t)-b|^\alpha\). The arc lies eventually in the open submanifold

\[
M'=\{x\in V:H(x)<2D|x-b|^\alpha\}.
\]

On \(M'\), the restriction of \(f\) extends continuously at \(b\) with value \(f(a)\). Its intrinsic gradient equals \(\nabla_M f\), because \(M'\) is open in \(M\). The radial estimate applied at \(b\) gives \(G(\gamma(t))\le C_b|\gamma(t)-b|\to0\). If \(H\) is identically zero on the arc, \(G=0\) directly.

The preceding arc inequality applied to \(G,H\) now gives \(G^N\le D_1H\). Increase \(N\) to at least two if necessary: boundedness of \(G\) preserves such an inequality after increasing the exponent and the constant. At \(H>0\), substitution and taking \(N\)-th roots give

\[
H^{1-1/N}\le D_1^{1/N}|\nabla_M f|.
\]

At \(H=0\) the desired inequality holds directly. Set \(\rho=1-1/N\in(0,1)\cap\mathbb Q\). This proves the gradient inequality. \(\square\)

The foundational cell and Puiseux theorems remain the explicit inputs of this treatment. No assertion about a globally finite triangulation of an arbitrary noncompact analytic manifold follows from these definable statements.

