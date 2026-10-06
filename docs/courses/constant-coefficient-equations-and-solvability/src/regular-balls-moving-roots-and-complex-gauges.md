# Regular balls, moving roots and complex gauges

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The characteristic Cauchy problem permits a leading time coefficient that depends on tangential frequency. This changes both the root bounds and the geometry of the frequency regions on which individual roots can be followed. We prove the uniform zero-free-ball lemma, the precise weighted root bound, an inset lower bound for the leading coefficient, and full analytic labeling on a ball. We also prove the support-preserving complex gauge change and exhibit its effect on the Schrödinger equation.

Read [Primitive factors and moving polynomial roots](primitive-factors-and-moving-roots.md), [Uniqueness in a slab with bounded support](bounded-support-slab-uniqueness.md), [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz Fourier inversion; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies finite coordinates, scalar calculus and compact cutoffs; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the norm, extension and integration estimates.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs use the linked prerequisite lessons and any stated planned theorem.

## A uniformly large zero-free ball, with a real center

**Lemma 1.** Fix \(d\ge1\) and an integer \(M\ge0\). There is \(\gamma_{d,M}>0\) such that every nonzero complex polynomial \(R\) of degree at most \(M\), and every complex Euclidean ball \(B(c,t)\), \(t>0\), contain a ball \(B(c',\gamma_{d,M}t)\) on which \(R\) has no zeros. We can choose \(c'\in c+t\mathbb R^d\). In particular a real original center gives a real new center. No assumption on \(R(c)\) is made.

**Proof.** The degree-zero case is immediate with \(\gamma=1/4\). Suppose \(M\ge1\). In local coordinates, write
\[
\begin{gathered}
Q(w)=\sum_{|\alpha|\le M}b_\alpha w^\alpha,\\
\qquad
 \|Q\|_{\rm coeff}=\sum_{|\alpha|\le M}|b_\alpha|.
\end{gathered}
\tag{1}
\]
The coefficient unit sphere is a nonempty closed bounded subset of a finite-dimensional complex coordinate space, hence compact. For that sphere define
\[
\begin{gathered}
q(Q)=\max_{x\in\mathbb R^d,\ |x|\le1/2}|Q(x)|,\\
\qquad
 c_{d,M}=\min_{\|Q\|_{\rm coeff}=1}q(Q).
\end{gathered}
\tag{2}
\]
The maxima exist. Moreover \(|q(Q)-q(Q')|\le\|Q-Q'\|_{\rm coeff}\), since each monomial has modulus at most one on the real half-ball. Thus the minimum exists as well.

It is positive. A polynomial zero on a real ball is the zero polynomial: take a real coordinate box inside the ball, regard the polynomial as a polynomial in its first coordinate, and use that a nonzero one-variable polynomial has only finitely many zeros. Its coefficient polynomials therefore vanish on the remaining real box; repeat through all coordinates. The coefficient unit sphere excludes that zero polynomial. Positivity at every point of this compact sphere, together with continuity and attainment of the minimum, gives \(c_{d,M}>0\). This is uniform across polynomials of smaller degree too.

For \(\|Q\|_{\rm coeff}=1\), every \(|w|\le1\) and complex direction \(h\) satisfy
\[
\begin{gathered}
|dQ(w)h|
 \\
\le \sum_\alpha |b_\alpha|\sum_j\alpha_j|h_j|
 \\
\le M|h|_2.
\end{gathered}
\tag{3}
\]
Indeed all factors of the differentiated monomials have modulus at most one, \(|h_j|\le|h|_2\), and \(\sum_j\alpha_j\le M\). The ordinary real parameter along a complex line segment gives the same derivative and the usual integral bound.

Choose a maximizing real point \(x\) in the half-ball and set
\[
 \gamma_{d,M}=\min\left(\frac14,\frac{c_{d,M}}{2M}\right).
 \tag{4}
\]
If \(|w-x|<\gamma_{d,M}\), the entire segment between \(x,w\) is in the unit ball. By(3),
\[
\begin{gathered}
|Q(w)|\\
\ge |Q(x)|-M|w-x|>c_{d,M}/2>0.
\end{gathered}
\tag{5}
\]
Also that new ball lies in the original unit ball because \(|x|+\gamma\le3/4\).

For the original polynomial use \(Q(w)=R(c+tw)/\|R(c+t\,\cdot)\|_{\rm coeff}\). Translation and positive dilation preserve degree and do not turn a nonzero polynomial into zero. The denominator is positive even if \(R(c)=0\). Set \(c'=c+tx\). This proves the whole assertion, including the requested reality. In dimension zero a nonzero polynomial is a nonzero constant on the single point; any \(\gamma\le1\) gives the vacuous-dimensional assertion. \(\square\)

## The leading coefficient belongs in the root bound

**Lemma 2.** Let
\[
\begin{gathered}
P(z,s)=\sum_{j=0}^m a_j(z)s^j,\\
\qquad
 a=a_m\not\equiv0,\\
\qquad 1\le m\le M,\\
\qquad
 \deg P\le M,\\
\qquad \kappa=M-m+1.
\end{gathered}
\tag{6}
\]
There is \(C_P\) such that, for all complex \(z,s\) with \(P(z,s)=0\),
\[
 |a(z)s|\le C_P(1+|z|)^\kappa.
 \tag{7}
\]
The integer \(m\) is the degree in \(s\); it need not be the total order \(M\).

**Proof.** If \(a(z)=0\), the left side is zero, even at a fiber on which \(P(z,\cdot)\) vanishes identically. Otherwise put \(w=a(z)s\) and multiply the equation by \(a(z)^{m-1}\). It becomes
\[
 w^m+\sum_{k=1}^m a_{m-k}(z)a(z)^{k-1}w^{m-k}=0.
 \tag{8}
\]
The coefficient of \(w^{m-k}\) has degree at most
\[
\begin{gathered}
(M-m+k)+(k-1)(M-m)\\
=k\kappa.
\end{gathered}
\tag{9}
\]
Consequently its modulus is at most \(A_k(1+|z|)^{k\kappa}\), with a fixed nonnegative coefficient bound \(A_k\). This follows directly by summing its finitely many monomials, using \(|z_j|\le1+|z|\). Divide by \((1+|z|)^{m\kappa}\) and put \(v=w/(1+|z|)^\kappa\). The resulting monic polynomial has its \(k\)-th coefficient bounded by \(A_k\).

Take \(L=2\max(1,\max_k A_k^{1/k})\). If \(|v|>L\), division by \(v^m\) would give \(1\le\sum_k A_k|v|^{-k}<\sum_{k=1}^m2^{-k}<1\). Thus \(|v|\le L\), proving(7). Repeated roots require no separate argument. \(\square\)

## A lower bound inside a zero-free neighborhood

**Lemma 3.** Let \(a\not\equiv0\) be a complex polynomial of degree \(q\). If \(q\ge1\), choose a fixed unit vector \(v\in\mathbb C^d\) with \(a_q(v)\ne0\), where \(a_q\) is its highest homogeneous part. If \(a\) has no zeros in \(B(z,r)\), \(r>0\), then
\[
 |a(z)|\ge |a_q(v)|r^q.
 \tag{10}
\]
For \(q=0\), the bound is the fixed positive constant \(|a|\). The constant is independent of the center \(z\).

**Proof.** A nonzero homogeneous polynomial is nonzero somewhere and hence on some unit vector by positive scaling. The one-variable polynomial \(a(z+\lambda v)\) has degree exactly \(q\) and leading coefficient \(a_q(v)\), independent of \(z\). Factor it with multiplicities:
\[
\begin{gathered}
a(z+\lambda v)=a_q(v)\prod_{\nu=1}^q(\lambda-\lambda_\nu),\\
\qquad
 |\lambda_\nu|\ge r.
\end{gathered}
\tag{11}
\]
The root inequality follows because \(|\lambda v|=|\lambda|\) and the open radius-\(r\) ball is zero-free. Evaluation at \(\lambda=0\) proves(10). A zero exactly at distance \(r\) does not spoil the weak lower bound. \(\square\)

If \(a\) is zero-free on \(B(c,R+1)\), every \(z\in B(c,R)\) has a zero-free radius-one ball. Lemma3 supplies a fixed positive lower bound for \(|a(z)|\). Together with Lemma2 this gives
\[
\begin{gathered}
|s|\le C(1+|z|)^{M-m+1}
 \\
\quad\hbox{if }z\in B(c,R),\ P(z,s)=0,
\end{gathered}
\tag{12}
\]
where \(C\) depends on \(P\), and not on \(c,R\). This proves the inset root bound used in the characteristic Cauchy necessity argument without an unstated reciprocal-polynomial estimate.

## Analytic labels on a whole ball

**Lemma 4.** Suppose \(a_m(z)\ne0\) on a complex ball \(B\), and all roots of \(P(z,\cdot)\) are simple there. Then there are \(m\) distinct holomorphic functions \(s_1,\ldots,s_m\) on \(B\) such that
\[
\begin{gathered}
P(z,s)=a_m(z)\prod_{j=1}^m(s-s_j(z)),\\
\qquad z\in B.
\end{gathered}
\tag{13}
\]
Choosing the labels at one point determines them everywhere.

**Proof.** At any point the holomorphic implicit-function theorem gives one graph for each simple root. Shrink their common base neighborhood so the graphs remain distinct. They account for all \(m\) roots: the leading coefficient stays nonzero and the scalar polynomial has degree \(m\). These neighborhoods evenly cover the root set over \(B\).

A continuous path admits unique continuation of a chosen root through those graph neighborhoods. For completeness, cover its compact image by finitely many such neighborhoods. Uniform continuity and the finite-cover distance property subdivide the parameter interval so that each subpath lies in one neighborhood. Its graph uniquely continues the preceding endpoint. The graph choices agree on overlaps, since a common simple root has a unique local graph. This gives existence, uniqueness, and continuation all the way to the endpoint.

Two paths with the same endpoints give the same final root when they are homotopic with endpoints fixed. Here is the needed finite argument. A homotopy has compact image; choose finitely many evenly covered neighborhoods and a uniform subdivision of its parameter square fine enough that the image of each closed small rectangle lies in one neighborhood. Such a subdivision follows from uniform continuity and the compact-cover distance property. Continuation around each rectangle returns to the same graph, and therefore to the same root. Cancel the oppositely traversed internal edges of the rectangular grid. The continuations along the two boundary paths have equal endpoints. The two fixed-endpoint sides are constant and introduce no change.

Fix a point \(z_0\in B\) and its \(m\) roots. Continue each along the straight segment from \(z_0\) to \(z\). The ball is convex. Every other path is homotopic to this segment by straight interpolation between the two paths, with fixed endpoints, inside the ball. Thus the labels are well-defined independently of the path.

To prove holomorphy near \(z\), continue first to \(z\), then along a short path inside its graph neighborhood. That concatenation is homotopic to the straight segment to the nearby endpoint. The globally continued value therefore agrees with the local holomorphic graph. The labels cannot meet: reverse continuation from a hypothetical meeting point would identify two distinct initial roots. They enumerate all \(m\) roots, and scalar factorization gives(13). \(\square\)

For irreducible \(P\) of positive \(s\)-degree, the full Sylvester calculation in the slab-uniqueness lesson supplies a nonzero exceptional polynomial whose complement has precisely full-degree simple fibers. Its degree is finite and bounded in terms of the degree and dimension of \(P\): the determinant has size \(2m-1\), and every entry is a coefficient polynomial or a scalar multiple of one. Lemma1 therefore gives, inside every tangential ball, a uniformly proportional subball with all \(m\) analytic labels. This statement concerns a ball, rather than all of the generally multiply connected exceptional-set complement.

## Complex gauge changes preserve the support question

For \(\theta\in\mathbb C^n\), let \(M_\theta u=e^{ix\cdot\theta}u\), defined for distributions by multiplication by that smooth nowhere-zero function. The product rule, first on smooth functions and then by distributional transposition, gives
\[
\begin{gathered}
(D_j-\theta_j)M_\theta u=M_\theta D_j u,\\
\qquad
 P(D-\theta)M_\theta u=M_\theta P(D)u.
\end{gathered}
\tag{14}
\]
The polynomial identity follows by applying the first identity repeatedly; the operators commute. Multiplication does not change distributional support: one inclusion follows from multiplication, and the reverse follows from multiplication by the smooth inverse \(e^{-ix\cdot\theta}\). If \(P(D)E=\delta_0\), then \(P(D-\theta)M_\theta E=\delta_0\), since the multiplier equals one at the origin. In particular existence of a fundamental distribution with a specified halfspace support is invariant under complex translation of the symbol. This assertion imposes no global tempered-growth bound.

An explicit example makes the distinction from a real-frequency root bound visible. In coordinates \((x,t)\), take \(P(\xi,\tau)=\tau-\xi^2\), \(D=-i\partial\). Define, for a compactly supported smooth test \(\phi\),
\[
\begin{gathered}
E(\phi)=\frac{i}{2\pi}\\
\int_0^\infty\int_{\mathbb R}
       e^{it\xi^2}\widehat{\phi}(-\xi,t)\,d\xi\,dt,
 \\\widehat{\phi}(\xi,t)=\int_{\mathbb R}e^{-ix\xi}\phi(x,t)\,dx.
\end{gathered}
\tag{15}
\]
This is a distribution. On any fixed compact test support, \(t\) ranges over a bounded interval, and two spatial integrations by parts give a bound \(C_K(1+|\xi|)^{-2}\) times a fixed finite derivative seminorm. Thus the integral is absolutely convergent and continuous on that test stage. It vanishes for tests supported in \(t<0\), so its support is in \(\{t\ge0\}\).

The formal transpose of \(P(D)=-i\partial_t+\partial_x^2\) is \(i\partial_t+\partial_x^2\). If \(h(\xi,t)=\widehat\phi(-\xi,t)\), then
\[
\begin{gathered}
e^{it\xi^2}\widehat{P(D)^{\rm t}\phi}(-\xi,t)
   \\
=i\,\partial_t\bigl(e^{it\xi^2}h(\xi,t)\bigr).
\end{gathered}
\tag{16}
\]
Four spatial integrations by parts bound both terms of this derivative integrably in \(\xi\), uniformly on the compact time interval. Fubini and time integration by parts are therefore valid. The coefficient \(i/(2\pi)\) makes \(E(P(D)^{\rm t}\phi)=(2\pi)^{-1}\int h(\xi,0)\,d\xi=\phi(0,0)\) by the Schwartz inversion theorem. Hence this is a halfspace fundamental distribution, with its phase proved directly.

Now translate the spatial symbol by \(i\): \(P_1(\xi,\tau)=\tau-(\xi+i)^2\). Its real-frequency roots have imaginary part \(2\xi\), unbounded below. The uniform lower imaginary-root bound in the elementary Petrowsky sufficient condition fails. Nevertheless \(E_1=e^xE\) is a fundamental distribution for \(P_1(D)\), by(14) with \(\theta=(-i,0)\), and it has the same halfspace support. A sufficient real-frequency bound cannot be used as a necessary condition.

## Exercises with complete solutions

**Exercise 1 — basic: a zero at the original center.** For \(d=M=1\), prove that \(\gamma=1/6\) works for every nonzero affine polynomial, including \(R(c)=0\). Identify the normalization that would fail in the latter case.

**Solution.** In normalized local coordinates write \(Q(w)=b+aw\), \(|a|+|b|=1\). Set \(L=\max(|b+a/2|,|b-a/2|)\). Their sum and difference give \(L\ge|b|\) and \(L\ge|a|/2\), hence \(3L\ge|a|+|b|=1\). Choose \(x=1/2\) or \(-1/2\) where that maximum is attained. On \(|w-x|<1/6\), \[
\begin{gathered}
|Q(w)|\\
\ge L-|a||w-x|>1/3-1/6\\
=1/6
\end{gathered}
\]

The ball is inside the unit ball. Scale back. Dividing by \(R(c)\) is invalid when that value is zero; the coefficient norm of \(R(c+t\,\cdot)\) remains positive and is the correct normalization.

**Exercise 2 — intermediate: the weighted root and the inset margin.** Apply the root and inset lemmas to \(P(z,s)=zs-1\). Explain why the coefficient factor cannot be discarded globally.

**Solution.** Here the total degree is \(M=2\), the \(s\)-degree is \(m=1\), \(\kappa=2\), and \(a(z)=z\). Every actual root has \(z\ne0\), \(s=1/z\), and \(|a(z)s|=1\), satisfying Lemma2 with a stronger constant bound. At \(z=0\) the polynomial is \(-1\) and has no roots. For \(a(z)=z\), choose \(v=1\); its highest homogeneous value is one. If \(B(z,r)\) has no zero, then \(|z|\ge r\), exactly the bound in Lemma3, and \(|s|\le1/r\). For example on \(B(2,1)\), \(|s|<1\). Globally \(z\to0\) through nonzero values makes \(|s|\to\infty\) although \(|z|\) stays bounded. The weighted product remains bounded and no unweighted global estimate follows.

**Exercise 3 — advanced: the ball hypothesis and monodromy.** Show that the two simple roots of \(s^2-z\) can be labeled on \(B(1,1/4)\), but cannot be labeled by a single-valued holomorphic square root on \(1/2<|z|<2\).

**Solution.** The leading coefficient is one, and \(z\ne0\) on the ball. Both roots are simple, so Lemma4 gives the two holomorphic labels there, once their values at \(z=1\) are chosen as \(1,-1\). On the annulus, suppose a single-valued holomorphic \(s(z)\) satisfied \(s(z)^2=z\). Put \(g(t)=s(e^{it})\), \(0\le t\le2\pi\). Differentiating \(g^2=e^{it}\), and using \(g\ne0\), gives \(g'=ig/2\). Differentiation of \(e^{-it/2}g(t)\) makes it constant, so \(g(2\pi)=-g(0)\). Single-valuedness at \(e^{2\pi i}=1\) requires \(g(2\pi)=g(0)\), a contradiction. Simple local roots alone do not imply global labels on an annulus; the convex ball and its explicit path-homotopy argument supply that missing step.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
