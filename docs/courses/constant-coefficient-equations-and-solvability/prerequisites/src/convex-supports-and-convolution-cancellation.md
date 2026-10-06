# Convex supports and convolution cancellation

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

Convolution can cancel individual pieces of support. For two compactly supported distributions, it cannot cancel an extreme supporting direction. We prove this for complex distributions, then distinguish it from the stronger support equality available for positive measures.

The spatial dimension \(n\) is a positive integer. We use complex-linear distributional pairings and \(\partial_j=\partial/\partial x_j\). The [convolution lesson](convolution-as-addition-of-supports.md), Theorems 1.1, 2.1, 3.1, 3.2 and 5.2, supplies convolution under proper addition, its support inclusion, smoothing, compact associativity, convergence on fixed supports and shrinking approximate identities. The [jet lesson](jets-supported-distributions-and-local-operators.md), Theorem 3.1 at a point, supplies uniqueness of finite point jets.

Two exact stronger results are reused from Fourier transforms, finite spectra and convex separation: Theorem 4.1 separates a point from a nonempty open convex set in any finite-dimensional real space, including a boundary point; Proposition 5.1 gives the support function of a Minkowski sum for arbitrary nonempty sets, including unbounded ones. Its proof of Theorem 1.1 also supplies the real Gaussian mass normalization used below. These proofs remain in that GFDL 1.2 source; the arguments and learner material here are independently written.

## Every finite support function determines a compact convex set

For nonempty bounded \(E\subset\mathbb R^n\), define

\[
H_E(\xi)=\sup_{x\in E}x\cdot\xi.
\tag{1.1}
\]

Taking the closed convex hull, denoted \(\operatorname{ch}E\), does not change this supremum: linearity bounds every finite convex combination, and continuity bounds its closure. The hull is compact because it is closed and bounded. We put \(\operatorname{ch}\varnothing=\varnothing\), but only take support functions of nonempty sets.

**Theorem 1.1 (the full support-function converse).** Let \(H:\mathbb R^n\to\mathbb R\) be finite, convex and positively homogeneous, with \(H(t\xi)=tH(\xi)\) for \(t\geq0\). Then there is exactly one nonempty compact convex set \(K\) with \(H_K=H\). It is

\[
K=\bigcap_{\xi\in\mathbb R^n}
\{x:x\cdot\xi\leq H(\xi)\}.
\tag{1.2}
\]

No symmetry or nonnegativity of \(H\) is assumed.

**Proof.** Homogeneity gives \(H(0)=0\), and convexity applied to a midpoint gives subadditivity. If \(e_j\) are the coordinate vectors, set

\[
M=\max_j\{|H(e_j)|,|H(-e_j)|\}.
\]

Splitting a vector into signed coordinate directions bounds \(H(\xi)\leq M\|\xi\|_1\). Since \(H(\xi)+H(-\xi)\geq0\), it also bounds \(H(\xi)\geq-M\|\xi\|_1\). Subadditivity in both directions now gives

\[
|H(\xi)-H(\eta)|\leq M\|\xi-\eta\|_1.
\tag{1.3}
\]

In particular \(H\) is continuous. Its strict epigraph

\[
C=\{(\xi,t):t>H(\xi)\}
\]

is a nonempty open convex cone. Fix \(\eta\) and put \(p=(\eta,H(\eta))\), a boundary point. Apply the imported separation theorem to \(C\) and \(p\). Write its nonzero covector as

\[
\begin{gathered}
\ell(\xi,t)=a\cdot\xi+bt,\\
\ell(y)<\ell(p)\quad(y\in C).
\end{gathered}
\]

Allowing \(t\) to increase forces \(b\leq0\). If \(b=0\), every \(\xi\) occurs in \(C\), so \(a\cdot\xi\) would be bounded above on all of \(\mathbb R^n\). This forces \(a=0\), a contradiction. Hence \(b<0\).

Scaling any \(y\in C\) by arbitrary positive factors shows that \(\ell(y)\leq0\), and scaling toward zero shows \(0\leq\ell(p)\). Since \(p\in\overline C\), continuity also gives \(\ell(p)\leq0\). Thus \(\ell(p)=0\). Letting \(t\downarrow H(\xi)\) yields

\[
a\cdot\xi+bH(\xi)\leq0.
\]

Consequently \(x_\eta=-a/b\) lies in \(K\), and \(x_\eta\cdot\eta=H(\eta)\). This proves nonemptiness and equality \(H_K=H\) in every direction.

The set \(K\) is closed and convex, and its defining coordinate inequalities give

\[
-H(-e_j)\leq x_j\leq H(e_j).
\tag{1.4}
\]

Thus \(K\) is compact.

For uniqueness, let \(L\) be nonempty compact convex and \(y\notin L\). Choose \(0<\varepsilon<\operatorname{dist}(y,L)\). The open convex set \(L+B(0,\varepsilon)\) excludes \(y\), so the imported separation theorem gives a nonzero \(\xi\) with

\[
H_L(\xi)+\varepsilon|\xi|\leq y\cdot\xi.
\tag{1.5}
\]

Here we used the imported sum formula and \(H_{B(0,\varepsilon)}(\xi)=\varepsilon|\xi|\), obtained from Cauchy–Schwarz and points approaching the radial boundary. Thus \(y\cdot\xi>H_L(\xi)\). Every point outside \(L\) violates a defining half-space inequality. Therefore \(L\) equals the intersection in (1.2) with \(H_L\), proving uniqueness. \(\square\)

This also proves the useful equivalence, for nonempty compact convex sets,

\[
K\subset L
\quad\Longleftrightarrow\quad H_K\leq H_L.
\tag{1.6}
\]

The imported sum identity specializes to \(H_{K+L}=H_K+H_L\). Directly from (1.1), dilation gives \(H_{tK}(\xi)=tH_K(\xi)\) for \(t\geq0\), while for \(t<0\) it gives \(H_{tK}(\xi)=(-t)H_K(-\xi)\). Negative dilation reverses the supporting direction.

For arbitrary nonempty compact \(E,F\), the same sum identity and uniqueness give
\(\operatorname{ch}(E+F)=\operatorname{ch}E+\operatorname{ch}F\):
both compact convex sets have support function \(H_E+H_F\).

For example, a translated possibly singular ellipsoid \(K=c+A\overline B(0,1)\) has

\[
H_K(\xi)=c\cdot\xi+|A^T\xi|.
\tag{1.7}
\]

Cauchy–Schwarz gives this maximum, even when \(A\) is singular. A negative support value can simply mean that the set lies on the negative side of the corresponding hyperplane.

## Two square-integral identities locate a self-convolution

For a compact smooth complex function \(u\), put \(\widetilde u(x)=\overline{u(-x)}\).

**Lemma 2.1 (reflection identity).** One has

\[
\|u*\widetilde u\|_2^2=\|u*u\|_2^2.
\tag{2.1}
\]

**Proof.** For every compact smooth \(g\), Fubini gives \(\|g\|_2^2=(g*\widetilde g)(0)\). Reflection with conjugation respects convolution. Compact associativity and commutativity therefore make both sides of (2.1) equal to

\[
(u*u*\widetilde u*\widetilde u)(0).
\]

Every integral is absolutely convergent. \(\square\)

**Lemma 2.2 (a fixed-box evaluation bound).** Let \(Q=\prod_{j=1}^n[-R_j,R_j]\), with \(R_j>0\). For every compact smooth \(g\) supported in \(Q\),

\[
\begin{gathered}
\|g\|_\infty\leq C_Q\|\mathscr Dg\|_2,\\
\mathscr D=\partial_1^2\cdots\partial_n^2,
\end{gathered}
\tag{2.2}
\]

where \(C_Q=3^{-n/2}\prod_j(2R_j)^{3/2}\).

**Proof.** Integrating twice from minus infinity in each coordinate gives

\[
\begin{aligned}
g(x)&=\int_{y<x}
k_x(y)\,\mathscr Dg(y)\,dy,\\
k_x(y)&=\prod_j(x_j-y_j).
\end{aligned}
\tag{2.3}
\]

Here \(y<x\) means \(y_j<x_j\) in every coordinate. The boundary terms vanish because \(g\) has compact support. For \(x\in Q\), Cauchy–Schwarz bounds the square of the kernel norm by

\[
\prod_j\int_{-R_j}^{x_j}(x_j-y_j)^2\,dy_j
\leq\prod_j\frac{(2R_j)^3}{3}.
\]

Outside \(Q\), \(g=0\). This proves (2.2). Any prescribed compact support fits in such a box. \(\square\)

**Proposition 2.3 (no extreme cancellation in a square).** If \(u\in C_c^\infty(\mathbb R^n)\) is nonzero and \(q=u*u\), then \(q\ne0\) and

\[
2\operatorname{ch}\operatorname{supp}u
=\operatorname{ch}\operatorname{supp}q.
\tag{2.4}
\]

**Proof.** Set \(w=u*\widetilde u\). Its support lies in a fixed compact difference set, and \(w(0)=\|u\|_2^2\). Let \(v=\partial_1\cdots\partial_nu\). Differentiating convolution in both factors gives

\[
\mathscr Dw
=(-1)^n v*\widetilde v,
\qquad
\mathscr Dq=v*v.
\]

Lemmas 2.1 and 2.2 imply

\[
\|u\|_2^2\leq C\|\mathscr Dq\|_2.
\tag{2.5}
\]

Thus \(q=0\) would force \(u=0\).

For real \(\xi\), apply (2.5) to \(u_\xi(x)=e^{x\cdot\xi}u(x)\). Its support is unchanged, and \(u_\xi*u_\xi=e^{x\cdot\xi}q(x)\). The box constant is independent of \(\xi\). Leibniz's rule bounds the resulting derivatives by finitely many fixed \(L^2\) norms of derivatives of \(q\), times a polynomial of degree at most \(2n\) and the largest exponential on its support. Hence

\[
\begin{aligned}
&\int e^{2x\cdot\xi}|u(x)|^2\,dx\\
&\quad\leq C_u(1+|\xi|)^{2n}
e^{H_{\operatorname{supp}q}(\xi)}.
\end{aligned}
\tag{2.6}
\]

If \(u(x_0)\ne0\), continuity supplies \(c>0\) and a sufficiently small ball of radius \(r\) around \(x_0\) on which \(|u|\geq c\). Replace \(\xi\) in (2.6) by \(t\xi\), \(t>0\). The ball contributes at least

\[
c^2|B(0,r)|
e^{2t(x_0\cdot\xi-r|\xi|)}.
\]

Take logarithms, divide by \(t\), let \(t\to\infty\), and then let \(r\downarrow0\). This gives \(2x_0\cdot\xi\leq H_{\operatorname{supp}q}(\xi)\). Continuity extends it to all \(x_0\in\operatorname{supp}u\). The half-space characterization gives the inclusion from left to right in (2.4). The reverse inclusion is the convolution support inclusion. \(\square\)

## Polynomial localization prevents cancellation between different factors

**Theorem 3.1 (compact convolution support theorem).** For all \(u,v\in\mathcal E'(\mathbb R^n)\), including complex distributions,

\[
\begin{aligned}
&\operatorname{ch}\operatorname{supp}(u*v)\\
&\quad=\operatorname{ch}\operatorname{supp}u
+\operatorname{ch}\operatorname{supp}v.
\end{aligned}
\tag{3.1}
\]

If a factor is zero, both sides are empty under the convention \(\varnothing+E=\varnothing\).

**Proof for smooth nonzero factors.** First let \(u,v\in C_c^\infty\) be nonzero. For each integer \(j\geq0\), let

\[
\begin{gathered}
K_j=\operatorname{ch}
\bigcup_{\deg p+\deg q\leq j}S_{p,q},\\
S_{p,q}=\operatorname{supp}\bigl((pu)*(qv)\bigr).
\end{gathered}
\tag{3.2}
\]

All these sets lie in the fixed compact convex set
\(S=\operatorname{ch}\operatorname{supp}u+\operatorname{ch}\operatorname{supp}v\), and they are nested. Only finitely many monomial pairs are needed at each degree: every polynomial pair expands into their linear combination, whose support lies in the union of the monomial supports. In particular each \(K_j\) is compact, though we have not yet excluded emptiness.

For \(j\geq1\) we claim

\[
2K_j\subset K_{j-1}+K_{j+1}.
\tag{3.3}
\]

Consider a monomial pair of total degree at most \(j\), and write \(f=(pu)*(qv)\). If its degree is at most \(j-1\), Proposition 2.3 and the support inclusion put \(2\operatorname{supp}f\) inside the right side of (3.3). This remains true when \(f=0\).

For degree exactly \(j\), interchange the factors if necessary so that \(p=x_\ell r\) for a monomial \(r\). Set

\[
\begin{aligned}
a&=(ru)*(qv),\\
b&=(ru)*(x_\ell qv),\\
c&=(pu)*(x_\ell qv).
\end{aligned}
\]

The coordinate multiplication identity for convolution is \(x_\ell a=f+b\), as follows directly by writing \(x_\ell=y_\ell+(x-y)_\ell\) in its integral. Associativity also gives \(b*f=a*c\). Therefore

\[
f*f=(x_\ell a)*f-a*c.
\tag{3.4}
\]

Here \(a\) and \(x_\ell a\) have support in \(K_{j-1}\), \(f\) has support in \(K_j\subset K_{j+1}\), and \(c\) has support in \(K_{j+1}\). Thus \(\operatorname{supp}(f*f)\subset K_{j-1}+K_{j+1}\). Proposition 2.3 puts \(2\operatorname{supp}f\) there too. Taking closed convex hulls over the finite monomial list proves (3.3); the right side is compact and convex.

We must first prove \(K_0\ne\varnothing\). Otherwise (3.3) at \(j=1\) gives \(K_1=\varnothing\), and induction gives \(K_j=\varnothing\) for every \(j\). Every polynomial-weighted convolution would then vanish.

Choose \(x_0,y_0\) where \(u(x_0)v(y_0)\ne0\). For fixed \(t>0\), the entire real Gaussian weights

\[
G_{t,z}(x)=(4\pi t)^{-n/2}
e^{-|x-z|^2/(4t)}
\tag{3.5}
\]

are limits of their Taylor polynomials in every derivative on each fixed compact set. One can see this directly from the exponential power series on complex polydisks: absolute convergence persists after each fixed derivative, since a polynomial in the series index is dominated by its factorial. Multiplication by \(u\) and \(v\) therefore gives compact smooth convergence on fixed supports. The fixed-support convolution continuity theorem implies
\((G_{t,x_0}u)*(G_{t,y_0}v)=0\).

On the other hand,

\[
\begin{aligned}
G_{t,x_0}u&\longrightarrow u(x_0)\delta_{x_0},\\
G_{t,y_0}v&\longrightarrow v(y_0)\delta_{y_0}
\end{aligned}
\tag{3.6}
\]

weakly as \(t\downarrow0\). Indeed, change variables \(x=x_0+\sqrt t\,z\) in the pairing. The Gaussian has unit mass by the imported normalization, the remaining smooth compact function tends pointwise to its value at \(x_0\), and its supremum bounds it by an integrable Gaussian. Dominated convergence proves the assertion. Both sequences have the fixed compact supports of \(u,v\). Joint weak sequential convolution continuity consequently gives the nonzero limit
\(u(x_0)v(y_0)\delta_{x_0+y_0}\), a contradiction. Thus \(K_0\) and every \(K_j\) are nonempty.

Fix \(\xi\), and write \(H_j=H_{K_j}(\xi)\). The sum formula and (3.3) give

\[
0\leq H_j-H_{j-1}
\leq H_{j+1}-H_j.
\tag{3.7}
\]

The inequality holds for every \(j\geq1\). All \(H_j\) are bounded above by \(H_S(\xi)\). A positive increment would persist at every subsequent index and force unbounded growth. Every increment is therefore zero. The half-space characterization now gives \(K_j=K_0\) for all \(j\).

The same Taylor approximation shows that the convolution of the two Gaussian-weighted factors in (3.6) is supported in \(K_0\) for each \(t>0\). Distributions supported in a fixed closed set retain that support in a weak limit: test functions supported outside it pair to zero at every stage. The nonzero point-mass limit therefore puts \(x_0+y_0\) in \(K_0\). Approximate arbitrary support points by points where the smooth functions are nonzero and use closedness. We obtain

\[
\begin{gathered}
\operatorname{supp}u+\operatorname{supp}v
\subset K_0,\\
K_0=\operatorname{ch}\operatorname{supp}(u*v).
\end{gathered}
\tag{3.8}
\]

Taking convex hulls proves the required lower inclusion, and the usual support inclusion proves the upper one.

**Passage to compact distributions.** Choose a nonnegative compact smooth approximate identity \(\rho_\varepsilon\), of mass one and support in \(\overline B(0,\varepsilon)\). Put \(u_\varepsilon=u*\rho_\varepsilon\), \(v_\varepsilon=v*\rho_\varepsilon\). These are compact smooth functions converging strongly, hence weakly, to \(u,v\), by the shrinking-profile theorem. Associativity gives

\[
u_\varepsilon*v_\varepsilon
=(u*v)*\rho_\varepsilon*\rho_\varepsilon.
\]

The smooth result and the support inclusion imply

\[
\begin{gathered}
\operatorname{supp}u_\varepsilon
+\operatorname{supp}v_\varepsilon\\
\subset K+\overline B(0,2\varepsilon),\\
K=\operatorname{ch}\operatorname{supp}(u*v).
\end{gathered}
\tag{3.9}
\]

To justify simultaneous approximation of support points, let \(x\in\operatorname{supp}u\), \(y\in\operatorname{supp}v\). In any neighborhoods of \(x,y\), there are tests with nonzero respective pairings. Weak convergence makes both pairings with \(u_\varepsilon,v_\varepsilon\) nonzero for all sufficiently small \(\varepsilon\). Hence both neighborhoods meet the respective smoothed supports for the same \(\varepsilon\). Taking shrinking neighborhoods and a common sequence \(\varepsilon_k\downarrow0\) gives points \(x_k\to x\), \(y_k\to y\) in those supports.

If \(K\) were empty, (3.9) would contradict these points. Otherwise it is compact and closed, and (3.9) gives \(\operatorname{dist}(x_k+y_k,K)\leq2\varepsilon_k\). Thus \(x+y\in K\). This proves (3.8) for arbitrary nonzero compact distributions, and finishes (3.1). Zero factors were handled in the statement. \(\square\)

For instance \((\delta_0-\delta_a)*(\delta_0+\delta_a)=\delta_0-\delta_{2a}\), \(a\ne0\). The middle point cancels, while the convex hull remains the complete segment from \(0\) to \(2a\).

## Positivity, affine confinement and differential operators

**Proposition 4.1 (full support equality for positive measures).** If \(\mu,\nu\) are positive locally finite measures and at least one has compact support, then

\[
\begin{aligned}
\operatorname{supp}(\mu*\nu)
&=\operatorname{supp}\mu\\
&\quad+\operatorname{supp}\nu.
\end{aligned}
\tag{4.1}
\]

The other measure need not be compact.

**Proof.** The sum on the right is closed: from a convergent sequence of sums, take a subsequence converging in the compact factor, and then use closedness of the other support. Proper addition supplies convolution and its upper support inclusion. For \(x,y\) in the two supports and any neighborhood \(O\) of \(x+y\), choose relatively compact neighborhoods \(U,W\) of \(x,y\) whose sum lies in \(O\). Choose a nonnegative compact smooth test \(\phi\) in \(O\) bounded below by a positive constant on smaller such neighborhoods. Each neighborhood has positive measure by the definition of support. The nonnegative convolution integral is consequently positive. Its local finiteness follows because the compact first factor and the compact test support restrict the second integration to a compact set. Thus \(x+y\) belongs to the convolution support. Zero measures give empty sets on both sides. \(\square\)

**Corollary 4.2 (zero divisors and affine confinement).** Nonzero compact distributions have nonzero convolution. If both \(u,v\) are nonzero and compact, and \(\operatorname{supp}(u*v)\subset V\) for an affine subspace \(V\), then each factor's support lies in an affine subspace parallel to \(V\).

**Proof.** A nonzero distribution has nonempty support, so its compact convex hull is nonempty. The right side of (3.1) is then nonempty, proving the first assertion. For the second, (3.8) gives \(\operatorname{supp}u+\operatorname{supp}v\subset V\), since an affine subspace is closed and convex. Fix \(a\in\operatorname{supp}u\) and \(b\in\operatorname{supp}v\). Then

\[
\operatorname{supp}u\subset V-b,
\qquad \operatorname{supp}v\subset V-a.
\]

Both containing subspaces are translates of \(V\). \(\square\)

**Example 4.1 (the zero-factor exception).** The nonzero assumption is essential in the confinement assertion. Take \(u=0\), \(v=\delta_0+\delta_{e_1}\), and \(V=\{0\}\). The empty convolution support lies in \(V\), but the support of \(v\) lies in no translate of that point.

Compactness of both factors is essential for the zero-divisor assertion. The nonzero compact distribution \(\delta_0-\delta_a\), \(a\ne0\), annihilates the nonzero constant distribution \(1\), since both its translations equal \(1\).

**Corollary 4.3 (constant differential operators preserve the convex hull).** If \(P\) is a nonzero complex polynomial and \(u\ne0\) is compactly supported, then

\[
\operatorname{ch}\operatorname{supp}(P(\partial)u)
=\operatorname{ch}\operatorname{supp}u.
\tag{4.2}
\]

**Proof.** The point-jet uniqueness theorem makes \(P(\partial)\delta_0\) nonzero, with support exactly \(\{0\}\). Differentiated convolution gives
\(P(\partial)u=(P(\partial)\delta_0)*u\).
Apply (3.1). \(\square\)

The actual support can shrink substantially. Here is a complete example.

**Proposition 4.4 (every support for a square indicator).** Let \(h=1_{(-1,1)}\), \(u=h\otimes h\), and decompose an arbitrary polynomial uniquely as

\[
\begin{aligned}
P(s,t)&=c+sA(s)+tB(t)\\
&\quad+stC(s,t).
\end{aligned}
\tag{4.3}
\]

Let \(Q=[-1,1]^2\), \(E_v=\{-1,1\}\times[-1,1]\), \(E_h=[-1,1]\times\{-1,1\}\), and \(F=\{-1,1\}^2\). Then the complete classification is:

- If \(P=0\), the support is \(\varnothing\).
- If \(c\ne0\), the support is the full square \(Q\).
- If \(c=0\), \(A\ne0\) and \(B\ne0\), it is \(E_v\cup E_h=\partial Q\).
- If \(c=0\), \(A\ne0\) and \(B=0\), it is the two vertical edges \(E_v\).
- If \(c=0\), \(A=0\) and \(B\ne0\), it is the two horizontal edges \(E_h\).
- If \(c=A=B=0\) and \(C\ne0\), it is the four vertices \(F\).

In the three edge cases, \(C\) is arbitrary.

**Proof.** Integration by parts on \((-1,1)\) gives \(h'=\delta_{-1}-\delta_1\); further derivatives give the corresponding point jets. Thus

\[
\begin{aligned}
P(\partial)u={}&c\,h\otimes h\\
&+A(\partial_1)h'\otimes h\\
&+h\otimes B(\partial_2)h'\\
&+C(\partial_1,\partial_2)(h'\otimes h').
\end{aligned}
\tag{4.4}
\]

Inside the square only the constant term survives. If \(c\ne0\), every interior point is in the support, whose closure is \(Q\).

Suppose \(c=0\). On each open vertical edge, only the \(A\) term remains; it is nonzero there exactly when \(A\ne0\), by uniqueness of the point jets in the normal coordinate. Tensoring with the nonvanishing interval density makes every point of that edge belong to the support. The same argument with \(B\) describes the horizontal edges. Closure of any present pair of edges includes all four vertices, regardless of any corner cancellation.

If both edge terms vanish, the remaining expression is supported at the four vertices. At each vertex it is, up to a nonzero sign, the point-jet polynomial \(C(\partial_1,\partial_2)\delta\). It is nonzero at every vertex exactly when \(C\ne0\). Point-jet uniqueness also makes it zero only when \(C=0\). This proves all cases and excludes every other support pattern. \(\square\)

Every nonempty support in the classification has convex hull \(Q\), as predicted by (4.2). Boundary edges, four corners and a filled square can therefore have the same supporting directions.

## Exercises

**Exercise 1 (basic).** Let \(c=(3,0)\), \(A=\begin{pmatrix}2&0\\1&2\end{pmatrix}\), and \(K=c+A\overline B(0,1)\). Find its support function, a maximizing point for every nonzero direction, its Cartesian equation and its area.

**Solution 1.** Since \(A^T\xi=(2\xi_1+\xi_2,2\xi_2)\), (1.7) gives

\[
H_K(\xi)=3\xi_1+
\sqrt{4\xi_1^2+4\xi_1\xi_2+5\xi_2^2}.
\]

The matrix is invertible, so \(A^T\xi\ne0\) when \(\xi\ne0\). Cauchy–Schwarz is maximized at the disk point \(A^T\xi/|A^T\xi|\); its image is

\[
x_\xi=c+\frac{AA^T\xi}{|A^T\xi|}.
\]

Writing \(X=x_1-3\), \(Y=x_2\), one has \(A^{-1}(x-c)=(X/2,Y/2-X/4)\). Thus the ellipse is

\[
\frac{X^2}{4}+
\left(\frac Y2-\frac X4\right)^2\leq1.
\]

Its area is \(|\det A|\pi=4\pi\). The support value in direction \((-1,0)\) is \(-1\), so this example also checks that a finite support function need not be nonnegative.

**Exercise 2 (basic).** In \(\mathbb R^2\), put \(a=(2,-1)\), \(b=(-1,3)\),
\(u=\delta_0-i\delta_a\), and \(v=\delta_b+i\delta_{a+b}\).
Compute their convolution, its actual support, its convex hull and its support function.

**Solution 2.** The two contributions at \(a+b\) have coefficients \(i\) and \(-i\), and the far contribution has coefficient \((-i)i=1\). Hence

\[
u*v=\delta_b+\delta_{2a+b}.
\]

Since \(a\ne0\), its support consists of the distinct points \((-1,3)\) and \((3,1)\). Its convex hull is the segment between them, equivalently \(b+[0,2]a\). Its support function is

\[
H(\xi)=b\cdot\xi+2\max(0,a\cdot\xi).
\]

This is the sum of the support functions of the two factor segments. The cancelled middle atom changes actual support and leaves the extreme directions unchanged.

**Exercise 3 (intermediate).** Let \(\mu=2\delta_{-3}+\delta_2\) on the line and let \(\nu\) be Lebesgue measure restricted to \([0,\infty)\). Determine the density, support and singular support of \(\mu*\nu\). Justify the convolution even though \(\nu\) is not compact.

**Solution 3.** The compact first factor makes addition proper on the factor supports above every compact test support. Translation of the half-line density gives

\[
\mu*\nu=2\,1_{[-3,\infty)}
+1_{[2,\infty)}.
\]

Changing endpoint values does not change a regular distribution. The density is zero below \(-3\), two between \(-3\) and \(2\), and three above \(2\). Thus the support is \([-3,\infty)\), agreeing with the sum of the positive-measure supports. Away from the two endpoints it is locally constant, hence smooth. At each endpoint its distributional derivative has a nonzero point mass, respectively \(2\delta_{-3}\) and \(\delta_2\), so it cannot be smooth there. Its singular support is exactly \(\{-3,2\}\).

**Exercise 4 (intermediate).** Put

\[
u(x)=
\begin{cases}
e^{-1/(1-x^2)}e^{ix^3},&|x|<1,\\
0,&|x|\geq1.
\end{cases}
\]

Show that
\(\lim_{t\to\infty}t^{-1}\log\int e^{2tx}|u(x)|^2\,dx=2\).
Deduce both endpoints of the convex hull of \(\operatorname{supp}(u*u)\).

**Solution 4.** The cutoff is smooth: each derivative on the interior is a finite sum of powers of \((1-x^2)^{-1}\) times a bounded polynomial and \(e^{-1/(1-x^2)}\); exponential decay dominates every such power at either endpoint. Its support is \([-1,1]\). The upper bound is
\(\int e^{2tx}|u|^2\leq e^{2t}\|u\|_2^2\).
For every \(\delta\in(0,1)\), choose a closed interval \(I\subset(1-\delta,1)\). There is \(c_I>0\) with \(|u|\geq c_I\) on \(I\), so the integral is at least
\(c_I^2|I|e^{2t(1-\delta)}\).
Taking logarithms and limits gives a lower limit at least \(2(1-\delta)\); let \(\delta\downarrow0\). The limit is two. Reflecting the argument recovers the negative endpoint. Proposition 2.3 then gives \(\operatorname{ch}\operatorname{supp}(u*u)=[-2,2]\). Infinite-order boundary vanishing and a complex phase do not remove either extreme direction.

**Exercise 5 (intermediate).** Fix nonzero \(a\in\mathbb R^n\), and let \(T_a u=\delta_a*u\). Prove that \(I-T_a\) is injective on compact distributions, and that \((I-T_a)u=\delta_0\) has no compact distributional solution. Compare the constant distribution.

**Solution 5.** The kernel \(\delta_0-\delta_a\) is nonzero and compact. Corollary 4.2 makes convolution by it injective on \(\mathcal E'\). If a compact solution to the displayed inhomogeneous equation existed, it would be nonzero and Theorem 3.1 would give

\[
\{0\}=[0,a]+\operatorname{ch}\operatorname{supp}u.
\]

For any point \(x\) in the nonempty second hull, the right side contains both \(x\) and \(x+a\). These are distinct, contradicting its being a point. A compact solution therefore cannot exist. For the noncompact constant distribution \(1\), \(T_a1=1\), so injectivity fails on the larger distribution space.

**Exercise 6 (advanced).** Let \(A=\begin{pmatrix}2&1\\-1&3\end{pmatrix}\), \(c=(4,-2)\), and let \(u\) be the indicator of the open parallelogram \(c+A(-1,1)^2\). Define the constant directional derivatives \(L_1=(2,-1)\cdot\nabla_x\), \(L_2=(1,3)\cdot\nabla_x\). Find the exact supports of

\[
\begin{aligned}
f_1&=(L_1+L_1L_2^2)u,\\
f_2&=(L_1^2+L_2)u,\\
f_3&=L_1L_2u.
\end{aligned}
\]

Give the complete point-mass formula for \(f_3\), including its density factor.

**Solution 6.** In coordinates \(x=c+Ay\), the chain rule makes \(L_j=\partial_{y_j}\) on functions pulled forward from \(y\). The absolute density Jacobian is \(\det A=7\). The three polynomials are \(s+st^2\), \(s^2+t\), and \(st\). Proposition 4.4 therefore gives, respectively, the images of the two vertical closed edges, the full boundary, and the four vertices under \(y\mapsto c+Ay\).

For the last formula, the \(y\)-coordinate distribution is
\((\delta_{-1}-\delta_1)\otimes(\delta_{-1}-\delta_1)\). The pairing of the ordinary indicator in the \(x\) coordinates contains the density factor seven; integration by parts in \(y\) keeps it. Consequently

\[
f_3=7\sum_{\epsilon_1,\epsilon_2=\pm1}
\epsilon_1\epsilon_2\,
\delta_{c+A(\epsilon_1,\epsilon_2)}.
\]

The vertices are \((1,-4),(3,2),(5,-6),(7,0)\), with signs \(+,-,-,+\) in that order. The sign at a corner is the product of the two one-dimensional endpoint signs; those signs are \(-\epsilon_j\), so their product is \(\epsilon_1\epsilon_2\).

**Exercise 7 (advanced).** Let \(U\) be the indicator of \((-1,1)^3\). For a polynomial \(P(s_1,s_2,s_3)\), group its monomials according to the set \(S\) of coordinates with positive exponent:

\[
P=\sum_{S\subset\{1,2,3\}}P_S,
\qquad
P_S=\sum_{\{j:\alpha_j>0\}=S}c_\alpha s^\alpha.
\]

Prove that the support of \(P(\partial)U\) is exactly the union, over all nonzero \(P_S\), of the closed faces on which the coordinates in \(S\) are endpoints \(\pm1\). In particular, determine the support for \(P=s_1s_2+s_2s_3\).

**Solution 7.** A monomial with positive exponents exactly in \(S\) differentiates the interval indicators into point jets in those coordinates and leaves interval densities in the others. Its support is contained in the indicated union \(F_S\) of closed faces. This proves the upper inclusion for the proposed union.

For the lower inclusion, retain only the inclusion-minimal sets \(S\) among those with \(P_S\ne0\). Every other \(F_T\) is contained in some such \(F_S\), since \(S\subset T\) implies \(F_T\subset F_S\). On the relative interior of any face of \(F_S\), every grouped term with a positive derivative in a coordinate outside \(S\) vanishes locally. Terms with derivative set properly inside \(S\) are absent by minimality. The only remaining term is \(P_S\).

At that face its normal point-jet polynomial has coefficients, up to one common nonzero endpoint sign, \(c_\alpha\), and normal derivative orders \((\alpha_j-1)_{j\in S}\). Distinct monomials give distinct jets, so this polynomial is nonzero by point-jet uniqueness. The undifferentiated interval densities are nonzero on the relative interior. Tensor-product tests consequently detect the distribution in every relative neighborhood there. Taking closures includes the whole face, proving the lower inclusion. The empty set \(S\) gives the full cube by the same argument.

For the requested polynomial, the two minimal sets are \(\{1,2\}\) and \(\{2,3\}\). The support consists of four edges parallel to the third axis and four edges parallel to the first axis:

\[
\begin{gathered}
\{x_1,x_2\in\{-1,1\},\ |x_3|\leq1\}\\
\cup\ \{|x_1|\leq1,\ x_2,x_3\in\{-1,1\}\}.
\end{gathered}
\]

It includes all eight vertices, and none of the edges parallel to the second axis except their endpoints. Its convex hull is the full closed cube, consistent with Corollary 4.3.

**Exercise 8 (advanced).** Let \(a,b\in\mathbb R^2\) be linearly independent. Put \(w=\delta_0+\delta_a+\delta_b\). For a prescribed compact distribution \(g\ne0\), show that \(w*u=g\) has at most one compact solution, and derive a necessary condition on the width of \(\operatorname{ch}\operatorname{supp}g\) in every direction. Use it to exclude a compact solution when \(g\) is supported on a line.

**Solution 8.** The kernel is nonzero and compact. The difference of two compact solutions would be annihilated by \(w\), so Corollary 4.2 gives uniqueness. Write \(T=\operatorname{ch}\{0,a,b\}\) and \(K=\operatorname{ch}\operatorname{supp}u\). Any solution is nonzero, and Theorem 3.1 gives \(\operatorname{ch}\operatorname{supp}g=T+K\).

For a nonempty compact set \(E\), its directional width is
\(W_E(\xi)=H_E(\xi)+H_E(-\xi)\geq0\).
The support-sum formula therefore gives

\[
W_{\operatorname{supp}g}(\xi)
=W_T(\xi)+W_K(\xi)\geq W_T(\xi),
\]

where

\[
\begin{aligned}
W_T(\xi)&=\max(0,a\cdot\xi,b\cdot\xi)\\
&\quad-\min(0,a\cdot\xi,b\cdot\xi).
\end{aligned}
\]

For every nonzero \(\xi\), this last width is positive: zero would force both \(a\cdot\xi=b\cdot\xi=0\), impossible by linear independence. A compact set contained in a line has zero width in a nonzero normal direction. Thus the necessary condition fails, and no compact solution exists. The width condition is necessary; no sufficiency is claimed.

## References

- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, [author-hosted book](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf), Section 2.5, separating and supporting hyperplanes. This is human background for the convex geometry.
- Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, [author-hosted notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), September 28, 2026, Chapters 6 and 8, compact distributions, approximation and convolution. The course's exact convolution interfaces are cited at the start of the lesson.
- Fourier transforms, finite spectra and convex separation, Theorem 4.1, Proposition 5.1 and the Gaussian normalization in the proof of Theorem 1.1. This identifies the reused proof locations, under that source's GFDL 1.2 license.
