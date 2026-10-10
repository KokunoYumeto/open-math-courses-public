# Sharp support for irreducible Cauchy equations

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A compact initial set cannot produce a nonzero solution whose unbounded support fits a characteristic cone translated to a point outside that set. An oblique slab and two Cauchy cuts prove the precise statement.

Read [Uniqueness in a slab with bounded support](bounded-support-slab-uniqueness.md), [Compact Cauchy data and local coherence](compact-cauchy-data-and-local-coherence.md), [Small Gevrey solutions of the full Cauchy problem](small-gevrey-cauchy-solutions.md).

The local distributional Holmgren theorem is proved in [Analytic coefficients and one-sided uniqueness](../AN02-L191.html#3-a-continuously-differentiable-surface-needs-no-analytic-flattening), Theorem 3.2: a distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic \(C^1\) surface vanishes near that surface. The uses of the Holmgren theorem draw on that complete proof.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs below use the linked prerequisite lessons and the stated planned results.

## Statement, support and cone conventions

Let \(P\in\mathbb C[\zeta_1,\ldots,\zeta_n]\) be irreducible and nonconstant, of total degree \(m\ge1\), with principal homogeneous part \(F=P_m\). Let \(N\in\mathbb R^n\setminus\{0\}\). Assume \(F\) is hyperbolic with respect to \(N\): \(F(N)\ne0\), and every root of
\[
\begin{gathered}
s\longmapsto F(\xi+sN)
 \\
\quad\hbox{is real for every }\xi\in\mathbb R^n.
\end{gathered}
\tag{1}
\]
Define
\[
\begin{gathered}
\Sigma=\{x:x\cdot N=0\},\\
\qquad H=\{x:x\cdot N\ge0\},
 \\
\Gamma=\text{the connected component of }N
                 \\
\text{ in }\{F\ne0\}\subset\mathbb R^n,
 \\
C=\Gamma^*=\{c:c\cdot\theta\ge0\\
\text{ for every }\theta\in\Gamma\}.
\end{gathered}
\tag{2}
\]
The star denotes the positive polar cone, including its boundary. In particular \(N\in\Gamma\) gives \(C\subset H\). The set \(C\) is closed and convex, being an intersection of closed halfspaces. No convexity assertion about \(\Gamma\) is needed in this proof.

**Theorem.** Let \(K\subset\Sigma\) be compact and convex, and let \(y\in\Sigma\setminus K\). Suppose \(u\in C^m(H)\) solves \(P(D)u=0\), where \(D=-i\partial\). Suppose all its \(m\) Cauchy traces vanish outside \(K\):
\[
 \langle D,N\rangle^j u|_{\Sigma\setminus K}=0,\qquad 0\le j<m.
 \tag{3}
\]
Here \(C^m(H)\) means that the derivatives in the interior through total order \(m\) extend continuously to the closed halfspace. If there is a bounded set \(B\subset H\) such that
\[
 \operatorname{supp}_H u\subset (y+C)\cup B,
 \tag{4}
\]
then \(u=0\) throughout \(H\), using the available Holmgren theorem.

Support in (4) is relative to \(H\). Replacing \(B\) by a sufficiently large closed ball intersected with \(H\) preserves the hypothesis, so its closure causes no boundedness issue.

If \(K\) is empty, (3) says that every initial trace is zero everywhere. The one-sided cone uniqueness lemma applies at every point with positive normal coordinate and gives \(u=0\) there; continuity gives the same conclusion on \(\Sigma\). If \(n=1\) and \(K\ne\varnothing\), the plane \(\Sigma\) is the single point \(0\), so no \(y\in\Sigma\setminus K\) exists. Thus only the case \(n\ge2\), \(K\ne\varnothing\), needs the construction below. Degree zero and dimension zero are outside the stated nonconstant hyperbolic hypothesis.

## A separated characteristic normal

Choose a point \(k_0\in K\) nearest to \(y\), and put
\[
\begin{gathered}
\xi=y-k_0,\\
\qquad g=|\xi|^2>0,\\
\qquad \varepsilon=g/2.
\end{gathered}
\tag{5}
\]
Both points lie in \(\Sigma\), so \(\xi\cdot N=0\). Convexity implies
\[
\begin{gathered}
(k-k_0)\cdot\xi\le0,\\
\qquad
 k\cdot\xi\le y\cdot\xi-g
 \\
\quad(k\in K).
\end{gathered}
\tag{6}
\]
Indeed, \(k_0+t(k-k_0)\in K\) for \(0\le t\le1\). The right derivative at zero of its squared distance from \(y\) is nonnegative. That derivative is \(-2(k-k_0)\cdot\xi\), proving the first inequality; \(k_0=y-\xi\) gives the second.

The polynomial \(F(\xi+sN)\) has degree exactly \(m\), with nonzero leading coefficient \(F(N)\). By (1), all its roots are real. Let \(s_0\) be the largest root and set
\[
 \eta=\xi+s_0N.
 \tag{7}
\]
Then \(\eta\ne0\), since its tangential part is the nonzero vector \(\xi\), and \(F(\eta)=0\).

We now prove \(\eta\in\partial\Gamma\). The component \(\Gamma\) is open: every point in \(\{F\ne0\}\) has a small connected ball still in that set, and this ball belongs to the same component. It is invariant under positive dilation: for \(z\in\Gamma\) and \(a>0\), the path \(r z\), with \(r\) between 1 and \(a\), has \(F(rz)=r^mF(z)\ne0\), so \(az\) is in the same component as \(z\).

For all sufficiently large positive \(s\), the point \(N+\xi/s\) is in a small ball about \(N\) contained in \(\Gamma\). Positive dilation puts \(\xi+sN\) in \(\Gamma\). There is no root of \(F(\xi+sN)\) for \(s>s_0\). The entire ray with \(s>s_0\) is therefore connected inside \(\{F\ne0\}\), and belongs to \(\Gamma\), since it meets that component at large \(s\). As \(s\downarrow s_0\), the ray tends to \(\eta\). Consequently \(\eta\in\overline\Gamma\); because \(F(\eta)=0\), it is outside \(\Gamma\) and hence on its boundary. This proves precisely the boundary fact used here, without the full cone theorem.

For \(k\in K\), both \(k\cdot N\) and \(y\cdot N\) are zero. Thus (6) gives
\[
\begin{gathered}
k\cdot\eta\le y\cdot\eta-g<y\cdot\eta-\varepsilon,
 \\
\qquad
 c\cdot\eta\ge0\quad(c\in C).
\end{gathered}
\tag{8}
\]
The second inequality follows by taking the limit of the defining polar inequalities along the ray in \(\Gamma\).

## Vanishing in the oblique slab

Consider the open slab
\[
 S=\{x:y\cdot\eta-\varepsilon<x\cdot\eta<y\cdot\eta\}.
 \tag{9}
\]
The first part of (8) makes \(S\cap K\) empty. The second makes \(S\cap(y+C)\) empty.

On \(S\), define a locally integrable distribution \(v\) to equal \(u\) in \(H\) and zero on the negative side of \(\Sigma\). We require only a distributional zero extension here. In coordinates \(t=x\cdot N/|N|\), condition (3) makes every \(D_t\)-trace of order below \(m\) zero on \(S\cap\Sigma\). Their tangential derivatives of the orders used by \(P\) are zero there as well. The jump identity ([equation 3 in Compact Cauchy data and local coherence](compact-cauchy-data-and-local-coherence.md)) therefore gives
\[
 P(D)v=0\quad\hbox{in }S.
 \tag{10}
\]
No term supported on the initial plane remains. This use does not silently infer \(C^m\) regularity of an arbitrary zero extension from only \(m\) zero traces.

By (4) and disjointness of the translated cone, the support of \(v\) in \(S\) is bounded. Apply the full bounded-support slab uniqueness theorem with normal \(\eta\). Its hypothesis is that the principal part of every nonconstant irreducible factor fails to be hyperbolic in that normal. Here \(P\) itself is irreducible and \(F(\eta)=0\), so its principal part is not hyperbolic with respect to \(\eta\). The theorem applies to the finite open slab (9) and gives \(v=0\). Hence
\[
 u=0\quad\hbox{on }S\cap H.
 \tag{11}
\]

## Cutting off the translated cone

Define, on the closed halfspace,
\[
 u_1(x)=
 \begin{cases}
 u(x),&x\cdot\eta\ge y\cdot\eta,\\
 0,&x\cdot\eta<y\cdot\eta.
 \end{cases}
 \tag{12}
\]
We check the regularity at this new cut, including its intersection with the initial plane. The linear forms \(x\cdot\eta\) and \(x\cdot N\) are independent, since \(\xi\ne0\). Complete them to linear coordinates, and write \(r=x\cdot\eta-y\cdot\eta\), \(t=x\cdot N/|N|\). The open strip \(-\varepsilon<r<0\), \(t\ge0\), is a zero region by (11). Every derivative of \(u\) through total order \(m\) vanishes in its interior and, by continuity up to \(H\), on its boundary \(r=0,t\ge0\). The usual one-variable gluing across \(r=0\), applied successively to these derivatives, shows that (12) is \(C^m\) up to \(t=0\). This coordinate argument also covers the corner \(r=t=0\).

For \(r>0\), \(u_1\) solves the equation; for \(r<0\), it is zero. At \(r=0\), every derivative entering \(P(D)\) is zero, so \(P(D)u_1=0\) throughout \(H\). Its initial \(m\) traces all vanish. On the upper part \(r\ge0\) of \(\Sigma\), this follows from (8), which places all of \(K\) strictly below the cut, and from (3). On the lower part it is identically zero. The just-proved gluing covers their interface.

The one-sided \(C^m\) cone uniqueness lemma now applies at every positive-time point, with homogeneous equation on a neighborhood of the required closed cone and zero data on its base. Thus \(u_1=0\) in the interior of \(H\), and by continuity on its boundary. Since (8) puts \(y+C\) in the upper part of the cut, we obtain
\[
 u=0\quad\hbox{on }y+C.
 \tag{13}
\]

It follows that the support of \(u\) is bounded. More explicitly, replace \(B\) in (4) by its bounded closed-ball enlargement. Outside this enlargement, points outside \(y+C\) are outside the original support, while points in \(y+C\) have value zero by (13). Thus \(u\) is zero at every point of the relative open complement of that enlargement, and its relative support is contained in the enlargement.

Choose a horizontal plane \(t=T>0\) strictly above this bounded support. The solution and all its derivatives through order \(m\) vanish on a neighborhood of the whole plane. For an arbitrary point with \(0<t<T\), apply the reversed-time cone uniqueness lemma based at \(t=T\). Its cone stays in \(t>0\), where the homogeneous equation holds on a neighborhood, and all initial jets on that upper plane are zero. The lemma gives local vanishing at the chosen point. Points with \(t\ge T\) already lie above the support. Continuity gives zero on \(t=0\). Therefore \(u=0\) everywhere in \(H\), proving the theorem. \(\square\)

The final step uses a noncharacteristic upper plane and reversed-time Cauchy uniqueness. It does not apply the slab theorem with normal \(N\), where the principal part is hyperbolic, and it does not extend potentially nonzero initial jets across the original plane.

## Exercises with complete solutions

**Exercise 1 — basic: an explicit oblique slab.** In \(\mathbb R^2\), with coordinates \((x,t)\), take \(P(\xi,s)=s^2-\xi^2-1\), \(N=(0,1)\), \(K=[-1,1]\times\{0\}\), and \(y=(2,0)\). Compute the cone, polar and slab in the proof, and verify irreducibility.

**Solution.** The principal part is \(F=s^2-\xi^2\). The component of \(N\) is \(\Gamma=\{(\xi,s):s>|\xi|\}\). Its positive polar is \(C=\{(x,t):t\ge|x|\}\): in this set \(x\xi+ts\ge t s-|x||\xi|\ge0\) for every \(s>|\xi|\). Conversely, if \(t<|x|\), choose \(s=1\) and \(\xi\) of opposite sign to \(x\) with magnitude tending to 1; the pairing becomes negative. If \(x=0,t<0\), use \((\xi,s)=(0,1)\).

The nearest point is \(k_0=(1,0)\), so \(\xi=(1,0)\), \(g=1\), and \(\varepsilon=1/2\). The largest root of \(F(\xi+sN)=s^2-1\) is 1; hence \(\eta=(1,1)\). The slab is
\[
 3/2<x+t<2.
 \tag{14}
\]
Every point of \(K\) has \(x+t\le1\). Every point of \(y+C\) has \(x+t=2+c_x+c_t\ge2\). Thus both disjointness assertions hold exactly.

As a monic quadratic in \(s\), a factorization of \(P\) over \(\mathbb C[\xi,s]\) would give a root over \(\mathbb C(\xi)\), and would make \(\xi^2+1\) a square in that rational-function field. Its simple zeros at \(i\) and \(-i\) have odd multiplicity, whereas every rational square has even orders at every zero and pole. This is impossible. Gauss's lemma therefore proves irreducibility, so all the theorem's algebraic hypotheses are met. Any \(C^2\) solution with the specified initial support and the support enclosure (4) must vanish.

**Exercise 2 — intermediate: the two different gluing steps.** Explain why \(m\) zero initial traces alone do not justify saying that a zero extension is \(C^m\), and why the later oblique cut in this proof is \(C^m\).

**Solution.** On \(t\ge0\), the function \(t^m\) has all ordinary initial derivatives of order below \(m\) zero. Its zero extension \(t_+^m\) has \(m\)-th ordinary derivative \(m!\,1_{\{t>0\}}\), so it is \(C^{m-1}\), but not \(C^m\). Its next distributional derivative is \(m!\delta_0\). This example concerns regularity of an extension; \(t^m\) does not solve \(D_t^m u=0\), so it is not a counterexample to the theorem.

In the first extension, ([equation 3 in Compact Cauchy data and local coherence](compact-cauchy-data-and-local-coherence.md)) requires only the traces through \(m-1\) to remove the boundary distributions for an operator of order \(m\). We apply a theorem for distributions and need no additional gluing claim. At the later oblique cut, the full open strip on one side is already zero. Continuity forces *all* derivatives through order \(m\) to vanish on the cut, including at its transverse intersection with the initial plane. These stronger matching conditions justify \(C^m\) gluing and permit the \(C^m\) cone uniqueness lemma.

**Exercise 3 — advanced: why irreducibility cannot be dropped.** For \(P(\xi,s)=(s-\xi)(s+\xi)\), retain \(K\), \(y\), \(H\) and \(C\) from Exercise 1. Construct a nonzero smooth solution satisfying the same support enclosure except for a bounded set.

**Solution.** Choose a nonzero \(f\in C_c^\infty((-1,1))\) and put \(u(x,t)=f(x-t)\), \(t\ge0\). Its second \(x\)- and \(t\)-derivatives agree, so \(P(D)u=0\). Its \(D_t\)-traces are \(f(x)\) and \(if'(x)\), both supported in \(K\).

On its support, write \(a=x-t\in[-1,1]\). Since \(x=t+a\), membership in \(y+C\) is \(t\ge|t+a-2|\). One side of this inequality always holds: \(t+a-2\le t\), because \(a\le1\). The other is equivalent to
\[
 2t\ge2-a.
 \tag{15}
\]
Failure can occur only when \(0\le t<3/2\), with \(-1\le x\le5/2\). Thus the part of the support outside \(y+C\) lies in the bounded rectangle \([-1,5/2]\times[0,3/2]\). All analytic and support hypotheses hold, but \(u\ne0\). The omitted irreducibility hypothesis is exactly the issue: for the proof's characteristic normal \(\eta=(1,1)\), the factor \(s+\xi\) is hyperbolic in that normal, so the full factorwise slab uniqueness hypothesis fails.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
