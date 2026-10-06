# Uniform bounds for algebraic analytic branches

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A single algebraic root can be bounded using its leading coefficient. Uniform estimates for a family are more delicate: a leading coefficient can vanish in a limit, and a nearby polynomial can have extra roots far away. We use a circle in the root variable as a barrier, then move that barrier along regular spatial paths. This gives uniform analytic-branch bounds without dividing by a coefficient which might tend to zero.

Read [Regular balls, moving roots and complex gauges](regular-balls-moving-roots-and-complex-gauges.md), [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz Fourier inversion; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies finite coordinates, scalar calculus and compact cutoffs; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the norm, extension and integration estimates.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs use the linked prerequisite lessons and any stated planned theorem.

## The family and its scalar normalizations

Let \(Z\subset\mathbb C^d\), \(d\ge1\), be connected and open, and let \(m\ge1\). Let \(\mathcal A_m(Z)\) consist of the holomorphic functions \(f\) for which there is a nonzero polynomial \(R\) of total degree at most \(m\) in \(d+1\) variables such that
\[
 R(z,f(z))=0\quad(z\in Z).
 \tag{1}
\]
The polynomial can depend on \(f\). Total degree, rather than just degree in the last variable, is bounded. The family is preserved by \(f\mapsto af+b\), for \(a\ne0\): substitute \((w-b)/a\) in a relation and multiply by a nonzero scalar. The substitution is invertible, does not turn a nonzero polynomial into zero and does not increase total degree. Constant functions belong to the family through \(R(z,w)=w-b\). Degree zero has no such nonzero relation and gives an empty family.

Write \(U\Subset Z\) when \(U\) is open and its closure is a compact subset of \(Z\).

**Theorem 1 (uniform comparison).** If \(Z_1,Z_2\Subset Z\) are nonempty, there is a finite constant \(C\), depending only on these sets, \(Z\) and \(m\), for which
\[
 \sup_{Z_2}|f|\le C\sup_{Z_1}|f|,
                    \qquad f\in\mathcal A_m(Z).
 \tag{2}
\]

**Proof.** It suffices to bound every \(f\in\mathcal A_m(Z)\) with \(\sup_{Z_1}|f|\le1\). If the original supremum is positive, divide by it and use the preceding invariance. If it is zero, the identity principle on connected \(Z\) gives \(f=0\).

Normalize a relation by its coefficient norm:
\[
\begin{gathered}
R(z,w)=\sum_{|\beta|+j\le m}a_{\beta j}z^\beta w^j,
             \\
\qquad \sum_{\beta,j}|a_{\beta j}|=1.
\end{gathered}
\tag{3}
\]
The coefficient sphere is compact in its actual finite complex coordinate space. We construct a uniform branch bound in a neighborhood of every point \(R_0\) of that sphere; finitely many such neighborhoods will suffice.

Write \(R_0(z,w)=\sum_{j=0}^q a_j(z)w^j\), where \(a_q\ne0\) and \(q\) is the last-variable degree of this limiting polynomial. The possibility \(q=0\) must be retained. Let \(E=\{z\in Z:a_q(z)\ne0\}\). It is dense and open: a nonzero polynomial cannot vanish on a complex open set, by the iterated one-variable identity argument.

The set \(E\) is path connected. Here is the needed proof. A connected open set is joined by finite chains of overlapping open balls: the points reachable from a fixed ball by such chains form an open set, and their complement is also open, so connectedness makes the reachable set all of \(Z\). Choose connecting points in the overlaps outside the polynomial zero set, using density. Two successive regular points in a common ball can be joined while avoiding that zero set. On the complex line through them the restriction of \(a_q\) is a nonzero one-variable polynomial, since it is nonzero at each endpoint. It has finitely many zeros. In its line parameter, replace small pieces of the interval \([0,1]\) at those zeros by small semicircular arcs. The image stays in the ball: the original compact segment has a positive distance from the complement, and the detours can be chosen smaller than that distance after division by the nonzero direction length. Concatenating the finitely many detoured paths gives a path in \(E\). Coincident endpoints need no detour.

Choose \(b\in Z_1\cap E\). Fix a point \(c\in\overline{Z_2}\), which may lie outside \(E\). Choose a complex unit vector \(e\) so that \(a_q(c+\lambda e)\) is not identically zero. If \(a_q\) is constant, any unit vector works. Otherwise its top homogeneous part is nonzero at some unit vector \(e\); that part is the leading coefficient of the polynomial in \(\lambda\) for every \(c\).

Choose a small radius \(\rho>0\) such that the closed disk \(c+\lambda e\), \(|\lambda|\le\rho\), lies in \(Z\), and the leading coefficient has no zero on its boundary circle. Only finitely many forbidden radii occur. Compactness and continuity now give \(\sigma>0\) with
\[
\begin{gathered}
K_c=\{z+\lambda e:|z-c|\le\sigma,\ |\lambda|=\rho\}
                    \\
\subset E,
 \\\{z+\lambda e:|z-c|\le\sigma,\ |\lambda|\le\rho\}
                    \\
\subset Z.
\end{gathered}
\tag{4}
\]
Indeed shrink \(\sigma\) both for the positive distance of the disk from the complement of \(Z\) and for the positive minimum of \(|a_q|\) on its boundary. The set \(K_c\) is compact and path connected, as the continuous image of a closed ball times a circle. Join \(b\) to one point of its central circle by a path in \(E\). The union of that path and \(K_c\) is compact and path connected and contains \(b\).

The neighborhoods \(\{|z-c|<\sigma\}\), constructed for every \(c\in\overline{Z_2}\), have a finite subcover. Let \(K\) be the union of their finitely many compact circle families and paths. They all contain or connect to \(b\), so \(K\) is compact and path connected in \(E\). If \(q\ge1\), the coefficients of the monic polynomial \(R_0(z,w)/a_q(z)\) are bounded on \(K\), because \(|a_q|\) has a positive minimum there. The scalar root bound gives one \(W>1\) larger than every last-variable root for \(z\in K\). If \(q=0\), choose \(W=2\). In both cases
\[
 R_0(z,w)\ne0\quad(z\in K,\ |w|=W).
 \tag{5}
\]
Its modulus has a positive minimum on this compact set. Polynomial evaluation is uniformly continuous in the finitely many coefficients there. Consequently(5) holds also for every coefficient-normalized polynomial \(R\) in some neighborhood of \(R_0\), with the same \(K,W\).

For any such \(R\) and any analytic \(f\) satisfying its relation and \(\sup_{Z_1}|f|\le1\), we have \(|f(z)|\ne W\) on \(K\). At \(b\), its modulus is at most one and hence is less than \(W\). Along every path in \(K\), continuity prevents crossing that circle in the root variable. Thus \(|f|<W\) on \(K\). For each of the finitely many neighborhoods of \(c\), fix \(z\) in it and restrict \(f\) to its disk \(z+\lambda e\). The boundary belongs to \(K\), so maximum modulus gives
\[
 |f(z)|\le W,\qquad z\in Z_2.
 \tag{6}
\]
This bounds all eligible branches for every \(R\) in the chosen coefficient neighborhood, even if a nearby polynomial has higher last-variable degree than \(R_0\). Compactness of the coefficient sphere supplies finitely many neighborhoods; take the largest of their \(W\)'s. This proves(2). \(\square\)

## The compactness consequence with its proof

**Lemma 2 (normalized families).** For a fixed nonempty \(U\Subset Z\), every sequence in \(\mathcal A_m(Z)\) satisfying \(\sup_U|f_j|\le1\) has a subsequence converging locally uniformly on \(Z\). Its limit still belongs to \(\mathcal A_m(Z)\). If every \(\sup_U|f_j|=1\), the limit also has that supremum.

**Proof.** Theorem1 bounds the sequence on every relatively compact open subset of \(Z\). Cauchy estimates then bound its first coordinate derivatives on every smaller compact set, by enclosing each point in a closed polydisk with a slightly larger closed polydisk in \(Z\). A finite cover gives uniform equicontinuity locally on each compact set.

Choose a countable dense set in \(Z\), for example the complex rational-coordinate points which lie there. On this set each sequence of values is bounded. Finite-dimensional subsequence compactness, followed by a diagonal selection, gives one subsequence converging at every such point. It is uniformly Cauchy on every compact subset: choose a slightly larger compact neighborhood, use its derivative bounds on finitely many small balls, and approximate that compact subset by finitely many dense points in those balls. For a prescribed error, two late subsequence members are close at the finitely many points; equicontinuity bounds each of their changes from a point of the compact set to its chosen dense point. The sum of these three errors proves the uniform Cauchy property. Complex scalar completeness supplies its uniform limit on each compact set, and these limits agree on overlaps.

The locally uniform limit is holomorphic by the Cauchy-integral limit argument in Lemma1.2 of [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md). All fixed derivatives converge on smaller compact subsets by that same argument.

For each \(f_j\), choose and normalize a relation \(R_j\) by(3). After taking a further subsequence, finite coefficient compactness gives \(R_j\to R\), with coefficient norm one. The limit polynomial is therefore nonzero. Local uniform convergence and finite polynomial evaluation give
\[
\begin{gathered}
0=\lim_j R_j(z,f_j(z))=R(z,f(z)),\\
\qquad z\in Z.
\end{gathered}
\tag{7}
\]
Thus \(f\in\mathcal A_m(Z)\). Uniform convergence on the compact closure of \(U\) also gives
\[
\begin{gathered}
\left|\sup_U|f_j|-\sup_U|f|\right|
                         \\
\le\sup_{\overline U}|f_j-f|\\
\longrightarrow0.
\end{gathered}
\tag{8}
\]
This proves both normalization assertions. For an explicit exhaustion, take the sets \(\{|z|\le j,\ \operatorname{dist}(z,\mathbb C^d\setminus Z)\ge1/j\}\), \(j\ge1\), with distance to the empty complement interpreted as infinity. Distance to a nonempty closed set is Lipschitz with constant one, by taking the infimum in the triangle inequality. Thus each such set is closed and bounded, hence compact; they are increasing and cover \(Z\). Every compact subset of \(Z\) has a positive minimum distance from the complement, by its continuous distance function, and is bounded, so it is contained in one of these sets, and indeed in the interior of a later one. The construction therefore applies to the whole open domain; it does not assume a uniform root labeling on \(Z\). \(\square\)

We need only this sequential form, not a separate assertion that an infinite-dimensional closed ball is compact.

## Positive imaginary parts control derivatives

**Theorem 3.** Let \(Z_1,Z_2\Subset Z\) be nonempty and let \(Z_0\Subset Z_1\) be nonempty. For each nonzero multi-index \(\beta\), there is a finite \(C_\beta\), and there are constants \(C_0\ge1\), \(r>0\), depending only on the fixed sets and \(m\), such that every \(f\in\mathcal A_m(Z)\) with \(\sup_{Z_0}\operatorname{Im}f\ge0\) satisfies
\[
 \sup_{Z_2}|\partial^\beta f|
       \le C_\beta\sup_{Z_1}\operatorname{Im}f,\qquad \beta\ne0,
 \tag{9}
\]
and, for some ball \(B_f\subset Z_1\) of radius exactly \(r\),
\[
 \sup_{Z_1}\operatorname{Im}f
                     \le C_0\inf_{B_f}\operatorname{Im}f.
 \tag{10}
\]
The same derivative estimate holds with \(D^\beta=(-i)^{|\beta|}\partial^\beta\), since the factor has modulus one.

**Proof.** The compact closure of \(Z_0\) lies inside \(Z_1\). Let \(a\) maximize \(\operatorname{Im}f\) there, and put \(b=\operatorname{Im}f(a)=\sup_{Z_0}\operatorname{Im}f\ge0\). Subtract the complete complex value \(f(a)\), not only its real part, and set \(h=f-f(a)\). If \(h=0\), then \(f\) is constant; all derivatives in(9) vanish, while(10) holds on any fixed ball in \(Z_1\), with \(C_0\ge1\). We will choose \(r\) small enough for one such ball.

If \(h\ne0\), let \(L=\sup_{Z_2}|h|>0\), and define
\[
\begin{gathered}
g=\frac{f-f(a)}L,\\
\qquad
 \sup_{Z_2}|g|=1,\\
\quad g(a)=0,\\
\quad
 \operatorname{Im}f=b+L\operatorname{Im}g.
\end{gathered}
\tag{11}
\]
These changes preserve the degree-bounded graph family. Consider all normalized functions \(g\) for which \(g(a)=0\) at some \(a\in\overline{Z_0}\). Lemma2 makes this set sequentially compact for local uniform convergence. For the zero condition, take a convergent subsequence of the points \(a_j\) in their compact set; uniform convergence near that set gives \(g(a)=0\). The supremum normalization and algebraic relation remain true by Lemma2.

Every such \(g\) has
\[
 S(g)=\sup_{Z_1}\operatorname{Im}g>0.
 \tag{12}
\]
If its imaginary part were nonpositive on \(Z_1\), its value zero at the interior point \(a\) would be a local maximum. On every sufficiently small complex-line circle about \(a\), the mean of \(\operatorname{Im}g\) is zero by the Cauchy formula. All its values there are nonpositive, so continuity forces every value on that circle to be zero. Varying the line and radius gives \(\operatorname{Im}g=0\) in a neighborhood of \(a\). The coordinate Cauchy–Riemann equations make its real part constant there, and \(g(a)=0\) makes the constant zero. The identity principle on connected \(Z\) would give \(g=0\), contrary to its supremum one on \(Z_2\).

The function \(S\) is continuous under local uniform convergence, by the supremum bound on the compact closure of \(Z_1\). Sequential compactness and(12) therefore give constants \(c>0\), \(A<\infty\), with
\[
\begin{gathered}
c\le S(g)\le A
 \\
\quad\text{for every normalized }g.
\end{gathered}
\tag{13}
\]
For example, if there were no positive lower bound, a sequence with \(S(g_j)\to0\) would converge along a subsequence to another normalized function with \(S=0\), a contradiction. The upper bound follows from Theorem1 with \(Z_2\) as normalizing set. Cauchy estimates on a compact neighborhood of \(\overline{Z_2}\) similarly give bounds \(\sup_{Z_2}|\partial^\beta g|\le A_\beta\).

There are also fixed \(r>0\), \(\nu>0\) such that every normalized \(g\) has a ball of radius \(r\) in \(Z_1\) on which
\[
 \inf_{B_g}\operatorname{Im}g\ge\nu.
 \tag{14}
\]
To prove uniformity, suppose no such pair existed. For each integer \(j\), choose a normalized \(g_j\) for which no ball of radius \(1/j\) contained in \(Z_1\) has imaginary infimum at least \(1/j\). A subsequence converges locally uniformly to a normalized \(g\). By(12), \(g\) has positive imaginary part at some point of \(Z_1\); continuity gives a closed ball there, contained in \(Z_1\), on which it is at least a fixed positive number. Uniform convergence on that closed ball gives half that bound for every late subsequence member. For large \(j\), its centered subball of radius \(1/j\) has infimum greater than \(1/j\), contradicting its choice. Thus(14) holds. Decrease \(r\), if necessary, to fit the fixed constant-function ball as well; the same infimum bound persists on centered subballs.

Return to(11). Since \(b\ge0\), equations(13)–(14) give
\[
\begin{gathered}
\sup_{Z_2}|\partial^\beta f|
   \le LA_\beta
    \\
\le (A_\beta/c)\,[b+LS(g)],\\
 \sup_{Z_1}\operatorname{Im}f
   =b+LS(g)\\
\le b+LA
    \\
\le \max(1,A/\nu)\,[b+L\inf_{B_g}\operatorname{Im}g].
\end{gathered}
\tag{15}
\]
Choose \(C_\beta=A_\beta/c\) and \(C_0=\max(1,A/\nu)\). This proves both assertions. If the normalized set is empty, every function under consideration is constant, and the earlier fixed ball proves the result directly. The construction tracks the nonnegative imaginary shift \(b\); it does not confuse an arbitrary additive real constant with the size controlled by the imaginary part. \(\square\)

## A product cannot hide all its factors

**Theorem 4.** If \(U\Subset Z\) is nonempty and \(\ell\) is a positive integer, there is a finite constant \(C\), depending on \(U,Z,m,\ell\), such that
\[
\begin{gathered}
\prod_{j=1}^{\ell}\sup_U|f_j|
       \le C\sup_U\left|\prod_{j=1}^{\ell}f_j\right|,
                    \\
\qquad f_j\in\mathcal A_m(Z).
\end{gathered}
\tag{16}
\]

**Proof.** If any individual supremum is zero, the left side is zero and the assertion follows. Otherwise divide each function by that positive supremum; the family remains unchanged and every normalized factor has supremum one.

For normalized factors, their product is not identically zero on \(U\). Indeed none of the factors is identically zero on connected \(Z\). Its zero set is closed with empty interior, by the identity principle. In a nonempty open part of \(U\), choose successively a smaller nonempty open neighborhood avoiding each of the finitely many zero sets. After \(\ell\) steps there is a point where all factors are nonzero. Hence
\[
 \sup_U\left|\prod_{j=1}^{\ell}f_j\right|>0.
 \tag{17}
\]
If these positive suprema had no positive lower bound across normalized \(\ell\)-tuples, choose a sequence tending to zero. Apply Lemma2 to the first factor, then to the second within its subsequence, and so on through the finite list. Every factor converges locally uniformly to a normalized algebraic analytic function. Their products converge uniformly on \(\overline U\), since all factors are uniformly bounded there. The limiting product has supremum zero, contradicting(17). Therefore there is a positive lower bound; its reciprocal is the required \(C\). Restore the scalar normalizations to obtain(16). No degree bound for the product itself was used. \(\square\)

## Exercises with complete solutions

**Exercise 1 — basic: why the outer set is relatively compact.** For \(Z=\{|z|<1\}\), consider \(f(z)=1/(1-z)\). Find its total-degree graph relation and compare its exact suprema on concentric disks of radii \(0<r_1<r_2<1\). Explain why an estimate with the outer set equal to \(Z\) fails.

**Solution.** The relation is \((1-z)w-1=0\), of total degree two. The reverse triangle inequality gives \(|1-z|\ge1-|z|\), and values on the positive real radius approach equality. Consequently
\[
\begin{gathered}
\sup_{|z|<r}|f(z)|=\frac1{1-r},\\
\qquad
 \frac{\sup_{|z|<r_2}|f|}{\sup_{|z|<r_1}|f|}
                    =\frac{1-r_1}{1-r_2}.
\end{gathered}
\tag{18}
\]
These finite suprema match Theorem1 on relatively compact disks. On all of \(Z\), the supremum is infinite, while the inner supremum is finite. A finite constant cannot give the proposed comparison there. Holomorphy on an open domain does not supply a bound up to its boundary.

**Exercise 2 — intermediate: real shifts and the imaginary hypothesis.** On \(Z_1=\{|z|<r_1\}\), let \(f(z)=H+Az\), with \(H\in\mathbb R\), \(A>0\), and \(0<r_1<1\). Compute the quantities in Theorem3 and give one positive ball. Then exhibit failure of the derivative estimate when its nonnegative-imaginary-part hypothesis is omitted.

**Solution.** These functions have a degree-one graph relation. Their derivative and imaginary supremum are
\[
\begin{gathered}
|f'|=A,\\
\qquad
 \sup_{Z_1}\operatorname{Im}f=Ar_1,\\
\qquad
 \inf_{|z-ir_1/2|<r_1/4}\operatorname{Im}f=Ar_1/4.
\end{gathered}
\tag{19}
\]
The indicated ball lies in \(Z_1\), since its center distance plus radius is \(3r_1/4\). Thus \(C_1=1/r_1\) and \(C_0=4\) suffice for this family. They are independent of \(H\), even though \(\sup|f|\) grows without bound as \(|H|\to\infty\).

For the failure, take \(f(z)=z-iH\) with \(H>1\), on the unit disk \(Z_1\) inside a larger connected disk \(Z\). Its derivative is one while \(\sup_{Z_1}\operatorname{Im}f=1-H<0\). No nonnegative derivative constant can bound one by that negative right side. Every smaller centered \(Z_0\) also has negative imaginary supremum, so this function is precisely excluded by the theorem's hypothesis.

**Exercise 3 — advanced: dependence on the number of factors.** On the unit disk, let \(\omega=e^{2\pi i/\ell}\) and \(f_j(z)=1-\omega^jz\), \(0\le j<\ell\). Compute both sides of(16) without the constant. Deduce a necessary lower bound on a universal constant for \(\ell\) factors.

**Solution.** Each factor has supremum two on the open disk: the triangle inequality bounds it by two, and radial points approaching the opposite boundary direction approach that bound. Their product is \(1-z^\ell\). This identity follows by its degree, its \(\ell\) distinct unit-circle zeros and its constant term one, or by scalar factorization. Its supremum is also two, by the triangle inequality and radial points for which \(z^\ell\to-1\). Hence
\[
\begin{gathered}
\prod_{j=0}^{\ell-1}\sup_{|z|<1}|f_j|=2^\ell,\\
\qquad
 \sup_{|z|<1}\left|\prod_{j=0}^{\ell-1}f_j(z)\right|=2.
\end{gathered}
\tag{20}
\]
Each factor has a degree-one graph relation and is analytic on, for example, the disk \(Z=\{|z|<2\}\); the unit disk is relatively compact there. Therefore any constant covering all such \(\ell\)-tuples must be at least \(2^{\ell-1}\). The factor count in Theorem4 is essential even for linear functions. The functions attain their large individual suprema in different boundary directions, while the product comparison still gives a finite bound at every fixed count.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
