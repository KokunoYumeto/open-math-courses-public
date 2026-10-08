# The Petersson inner product and Poincaré series

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Fourier coefficient is a linear functional on the finite-dimensional space of cusp forms. We will construct a cusp form that represents this functional by integration. The construction averages one exponential over the modular group; its convergence, its values at the cusps, and the integral obtained by unfolding will all be proved.

We assume Dimension formulas for congruence subgroups, the slash and cusp conventions of Modular forms, lattice functions and Eisenstein series, and real plane change of variables. The continuous series and improper integrals use The upper half-plane and the modular group, Lemma 0.3, together with the modular tiling argument below. Theorem 1.1 also retains the measure-theoretic prerequisite for arbitrary measurable fundamental domains. The Petersson pairing and the coefficient estimate apply to every finite-index subgroup \(\Gamma\subset\mathrm{SL}_2(\mathbb Z)\). The Poincaré series displayed below are for \(\Gamma_0(N)\), including level one, and even \(k\ge4\). We will also construct the Eisenstein complement for every finite-index group in those even weights.

Write \(z=x+iy\), \(d\mu=dx\,dy/y^2\), and
\[
d_\Gamma=[\mathrm{PSL}_2(\mathbb Z):\bar\Gamma].
\]
All scalar products are linear in their first variable.

**Lemma 0.1 (analytic consequences used below and in later lessons).** A bounded holomorphic function on a punctured disk has a removable singularity. A bounded entire function is constant. Every nonconstant complex polynomial has a complex root. If a function has a Laurent series converging uniformly on each compact subannulus about its only isolated singularity, its integral around a positively oriented simple contour enclosing that singularity is \(2\pi i\) times the coefficient of \(z^{-1}\).

**Proof.** We use the circle formula, its coefficient bounds, and contour deformation proved in The upper half-plane and the modular group, Lemma 0.2. For the removable assertion translate the puncture to zero and suppose \(|f|\le M\). Set \(g(z)=z^2f(z)\) off zero and \(g(0)=0\). Then \(g\) is continuous and \(g'(0)=\lim_{z\to0}zf(z)=0\), so it is holomorphic on the disk. Its local power series has zero constant and linear coefficients. Dividing the remaining series by \(z^2\) extends \(f\) holomorphically.

For a bounded entire function, the circle coefficient bound at any centre \(p\) gives \(|f'(p)|\le M/R\) for every \(R>0\). Letting \(R\) tend to infinity proves \(f'=0\), hence constancy by integration along segments. If a nonconstant polynomial \(P\) had no root, \(1/P\) would be entire. Its leading term gives \(|P(z)|\to\infty\), so the reciprocal is bounded outside a disk, and continuity makes it bounded inside. It is constant by the preceding assertion, contradicting the degree of \(P\).

For the last assertion, deform the contour to a small circle in the punctured region using the earlier triangle and homotopy proof. Uniform convergence permits integration of its Laurent series term by term on that circle. The integral of \(z^j\) is zero except for \(j=-1\), whose integral is \(2\pi i\). This argument also applies to the normally convergent product of the exponential series in (8.7); it does not assume that its isolated singularity is a simple pole. \(\square\)

## 1. The pairing and its normalization

Define the unnormalized pairing, whenever it converges absolutely, by
\[
I_\Gamma(f,g)=\int_{\Gamma\backslash\mathfrak H}
f(z)\overline{g(z)}y^k\,d\mu(z).
\tag{1.1}
\]
Our normalized Petersson pairing is
\[
\langle f,g\rangle_\Gamma=\frac{I_\Gamma(f,g)}{d_\Gamma}.
\tag{1.2}
\]
Neither expression divides by the hyperbolic volume. That volume is
\(d_\Gamma\pi/3\), so a pairing normalized by volume is \(3/\pi\) times (1.2).

**Theorem 1.1.** If \(f,g\in M_k(\Gamma)\) and either is cuspidal, (1.1) converges absolutely and is independent of the fundamental domain. Its restriction to \(S_k(\Gamma)\) is a positive definite Hermitian inner product. If both forms are modular for \(\Gamma\) and \(\Gamma'\subset\Gamma\) has finite index, their normalized pairings for the two groups agree.

**Proof.** For \(\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma\),
\[
f(\gamma z)\overline{g(\gamma z)}
=|cz+d|^{2k}f(z)\overline{g(z)},\qquad
\operatorname{Im}(\gamma z)^k=\frac{y^k}{|cz+d|^{2k}}.
\]
Thus their product with \(y^k\) is invariant. The derivative
\(\gamma'(z)=(cz+d)^{-2}\) gives the real Jacobian
\(|cz+d|^{-4}\); combined with the imaginary-part formula it proves invariance of \(d\mu\). These computations also hold when \(k\) is odd and \(-I\) is absent.

There are finitely many cusp neighborhoods, with a compact remainder. In a cusp coordinate \(\alpha z\), invariance of the measure and the slash factors replace the integrand by
\[
(f|_k\alpha)(z)\overline{(g|_k\alpha)(z)}\,y^{k-2}\,dx\,dy.
\]
A modular form is bounded for large \(y\), and a cusp form is \(O(e^{-ay})\) for some \(a>0\), uniformly over one horizontal period. This follows from its holomorphic cusp expansion and its positive first exponent. The exponent uses the actual width: at a regular cusp it is a positive multiple of \(1/h\); at an irregular cusp in odd weight it is a positive odd multiple of \(1/(2h)\). Therefore the absolute integral over that neighborhood is bounded by a constant times
\(\int_Y^\infty y^{k-2}e^{-ay}\,dy\), which is finite. On the compact remainder the integrand is continuous. This proves absolute convergence. An invariant integrable function gives the same integral on any measurable fundamental domain, by translating its pieces; boundary overlaps have measure zero.

Sesquilinearity and Hermitian symmetry follow from the integral. For a cusp form,
\[
I_\Gamma(f,f)=\int_{\Gamma\backslash\mathfrak H}|f(z)|^2y^k\,d\mu(z)\ge0.
\]
If \(f\ne0\), continuity makes the integrand positive on a small open disk, whose image in the quotient has positive measure. Thus the norm is positive.

Finally put \(r=[\bar\Gamma:\bar\Gamma']\). A domain for \(\bar\Gamma'\) is a union of \(r\) translates of a domain for \(\bar\Gamma\), up to boundaries. The invariant integrand has the same integral on each, so \(I_{\Gamma'}=rI_\Gamma\). Also \(d_{\Gamma'}=r d_\Gamma\), proving equality in (1.2). These are projective indices; using an index in \(\mathrm{SL}_2\) can introduce an extra factor two if the groups differ in whether they contain \(-I\). \(\square\)

The pairing is defined on \(M_k\times S_k\) and on \(S_k\times M_k\). A modular form with a nonzero cusp constant generally has an infinite integral against itself in the weights considered below, so we do not give all of \(M_k\) a norm by (1.1).

## 2. A coefficient estimate from compactness

**Theorem 2.1 (Hecke's bound).** For every \(f\in S_k(\Gamma)\), the function
\[
y^{k/2}|f(z)|
\tag{2.1}
\]
is bounded on \(\mathfrak H\). In particular, at a regular cusp of width \(h\), the coefficients in
\[
(f|_k\alpha)(z)=\sum_{n\ge1}a_n e^{2\pi inz/h}
\]
satisfy \(a_n=O_f(n^{k/2})\). At an irregular cusp in odd weight the same estimate holds for the odd-index coefficients in the period-\(2h\) expansion.

**Proof.** The transformation law and the imaginary-part identity make (2.1) invariant. At a cusp, its value in a scaling coordinate is \(y^{k/2}|f|_k\alpha(z)|\), which tends to zero uniformly over a period because exponential decay dominates a power of \(y\). The finitely many cusp neighborhoods and the compact remainder therefore give a global bound \(A\). The slash-transformed form has the same bound, since \(\alpha\in\mathrm{SL}_2(\mathbb Z)\) gives
\[
y^{k/2}|f|_k\alpha(z)|
=\operatorname{Im}(\alpha z)^{k/2}|f(\alpha z)|.
\]

At a regular cusp, Fourier integration gives, for every \(y>0\),
\[
a_n=\frac1h\int_0^h
(f|_k\alpha)(x+iy)e^{-2\pi in(x+iy)/h}\,dx.
\]
Hence
\[
|a_n|\le A y^{-k/2}e^{2\pi ny/h}.
\tag{2.2}
\]
Choose \(y=h/n\) to obtain
\(|a_n|\le A e^{2\pi}h^{-k/2}n^{k/2}\).
At an irregular cusp use the period \(2h\) in the same computation. Only odd indices occur, but the bound does not change its exponent. \(\square\)

The previous lesson proves that nonpositive weights have no cusp forms, so the substantial cases of this estimate have \(k>0\).

## 3. Averaging an exponential

In this section \(\Gamma=\Gamma_0(N)\), \(k\ge4\) is even, and
\[
\Gamma_\infty=\{\pm T^r:r\in\mathbb Z\},\qquad
e(t)=e^{2\pi it}.
\]
For an integer \(m\ge0\), define
\[
P_m(z)=
\sum_{\gamma\in\Gamma_\infty\backslash\Gamma}
(c_\gamma z+d_\gamma)^{-k}e(m\gamma z).
\tag{3.1}
\]
The seed \(e(mz)\) is invariant under weight-\(k\) slash by \(\Gamma_\infty\), so a summand does not depend on the representative. Even weight is needed for the element \(-I\).

The cosets in (3.1) correspond to primitive bottom rows \((c,d)\), with \(N\mid c\), modulo simultaneous change of sign. Indeed every such row can be completed to a determinant-one matrix in \(\Gamma_0(N)\). Two completions differ by left multiplication by \(T^r\). We may choose \(c>0\), together with the one row \((0,1)\).

**Lemma 3.1 (a uniform tail estimate).** For real \(k>2\), uniformly in \(x\) and \(y\ge1\),
\[
\sum_{c\ge1}\sum_{d\in\mathbb Z}|c(x+iy)+d|^{-k}
\le C_k\bigl(y^{-k}+y^{1-k}\bigr).
\tag{3.2}
\]

**Proof.** We give a shift-independent comparison, including a constant. For \(A>0\), put \(F_A(u)=(u^2+A^2)^{-k/2}\), which decreases for \(u\ge0\). Choose an integer nearest to \(-b\). Its term is at most \(A^{-k}\); the two tails have distances at least \(j-1/2\), \(j\ge1\). Since
\(\sum_{j\ge1}F_A(j-1/2)\le F_A(1/2)+\int_{1/2}^\infty F_A(u)du\), we obtain, uniformly in \(b\),
\[
\begin{gathered}
\sum_{d\in\mathbb Z}\bigl((d+b)^2+A^2\bigr)^{-k/2}
\le3A^{-k}+I_k A^{1-k},\\
I_k=\int_{\mathbb R}(1+u^2)^{-k/2}du.
\end{gathered}
\]
Scaling evaluates the comparison integral as \(I_kA^{1-k}\), and splitting it at \(|u|=1\) gives \(I_k\le2+2/(k-1)\) for \(k>1\). Set \(A=cy\), \(b=cx\), and sum over \(c\ge1\). Explicitly the left side of (3.2) is at most
\[
3y^{-k}\sum_{c\ge1}c^{-k}
+\left(2+\frac2{k-1}\right)y^{1-k}\sum_{c\ge1}c^{1-k}.
\]
Both numerical series converge precisely in the asserted range \(k>2\), by the integral comparison for positive decreasing powers. Taking the larger of the two finite coefficients proves (3.2). This estimate is uniform over an entire horizontal strip and tends to zero as \(y\to\infty\), as required for every cusp calculation below. \(\square\)

**Theorem 3.2.** The series (3.1) converges absolutely and locally uniformly, is holomorphic and modular of weight \(k\), and satisfies
\[
P_m\in S_k(\Gamma)\quad(m\ge1).
\]
For \(m=0\), it is a modular form with constant one at the cusp infinity and constant zero at every inequivalent cusp.

**Proof.** Since \(\operatorname{Im}(\gamma z)>0\),
\(|e(m\gamma z)|\le1\). On a compact subset of \(\mathfrak H\), the real-linear map \((c,d)\mapsto cz+d\) is uniformly invertible. Thus \(|cz+d|\ge\epsilon\sqrt{c^2+d^2}\) there. The sum of \((c^2+d^2)^{-k/2}\) over nonzero lattice points converges for \(k>2\): the annulus with radius between \(2^j\) and \(2^{j+1}\) has \(O(2^{2j})\) points and contributes \(O(2^{(2-k)j})\). This proves absolute locally uniform convergence and holomorphy. Right multiplication by an element of \(\Gamma\) permutes the left cosets, proving \(P_m|_k\delta=P_m\).

We check every cusp rather than only infinity. For \(\alpha\in\mathrm{SL}_2(\mathbb Z)\), the slash of (3.1) is a sum of seeds attached to the matrices \(\gamma\alpha\). Their bottom rows are still primitive and distinct modulo sign: equal rows would make the matrices differ by a left translation, hence the original \(\gamma\)'s lie in the same \(\Gamma_\infty\)-coset. The sum of the absolute values of terms with nonzero lower-left entry is at most (3.2), and tends to zero uniformly in \(x\).

There is a term with lower-left entry zero exactly when \(\alpha\infty\) is \(\Gamma\)-equivalent to infinity, and then there is just one coset of such terms. Its matrix is \(\pm T^r\), so for \(m\ge1\) its value is \(e(m(z+r))=e(mz)\), which also tends to zero. For \(m=0\) its value is one. All other cusps have no such term.

Consequently \(P_m|_k\alpha\) is bounded as \(y\to\infty\), with limit zero for \(m\ge1\); for \(m=0\) its limit is the stated constant. The function is periodic with the cusp width \(h\), so it defines a holomorphic function of \(q_h\) on a punctured disk. Boundedness makes the puncture removable. Its value there is the computed limit. This proves holomorphy and the cusp assertions. \(\square\)

If one uses only \(\langle T\rangle\) instead of \(\{\pm T^r\}\) in (3.1), every term appears twice. The resulting series and its unfolding constants are twice ours.

## 4. Unfolding and spanning

Set
\[
A_{k,m}=\frac{\Gamma(k-1)}{(4\pi m)^{k-1}}
=\frac{(k-2)!}{(4\pi m)^{k-1}}\qquad(m\ge1).
\tag{4.1}
\]
The equality follows by repeated integration by parts in the gamma integral.

### Continuous integrals and projected modular tiles

The integral of a nonnegative continuous function on an unbounded region is the supremum of its compact truncation integrals. For a complex function we require finiteness of the corresponding absolute integral and then take the limit of the compact integrals. These are the conventions of The upper half-plane and the modular group, Lemma 0.3. Its plane version already supplies the interchange for a locally uniformly convergent nonnegative series, with infinity allowed, and the interchange for a continuous series whose absolute integrals have finite sum. We now justify the partitions of regions to which those statements will be applied.

**Lemma 4.0 (integration over modular tiles).** Let \(\Gamma\) have finite index in \(\mathrm{SL}_2(\mathbb Z)\), and choose a fundamental region \(D\) as a finite union of translates of the closed level-one region
\[
 \mathcal F=\{z\in\mathfrak H:|\operatorname{Re}z|\le1/2,\ |z|\ge1\}.
\]
The projectively distinct translates of \(D\) cover \(\mathfrak H\), have disjoint cell interiors, and meet every compact subset in only finitely many tiles. Their boundaries have zero area on compact truncations. Integrals are therefore unchanged by assigning their boundary points to different tiles.

Suppose in addition that \(h\) is a positive integer and
\(\Gamma_{\infty,h}=\{\pm T^{hr}:r\in\mathbb Z\}\subset\Gamma\). Put
\[
\begin{gathered}
 S_h=\{x+iy:0\le x<h,\ y>0\},\\
 D_\gamma=\bigcup_{r\in\mathbb Z}
                  (T^{hr}\gamma D\cap S_h),
 \qquad \gamma\in\Gamma_{\infty,h}\backslash\Gamma.
\end{gathered}
\]
These projected tiles cover \(S_h\) with disjoint cell interiors; their pieces and boundaries are locally finite on every compact positive-height strip truncation. For every continuous nonnegative function \(G\) on \(\mathfrak H\) of horizontal period \(h\),
\[
\begin{gathered}
 \sum_{\Gamma_{\infty,h}\backslash\Gamma}\int_{\gamma D}G\,dx\,dy\\
 =\sum_{\Gamma_{\infty,h}\backslash\Gamma}\int_{D_\gamma}G\,dx\,dy\\
 =\int_{S_h}G\,dx\,dy.
\end{gathered}
 \tag{4.0a}
\]
with infinity allowed. If \(G\) is complex continuous and \(\int_{S_h}|G|\,dx\,dy<\infty\), the same identities hold and both series of integrals converge absolutely. A fixed nonnegative continuous density may be included in the integrand whenever the product has the stated continuity and periodicity.

**Proof.** The reduction and side-pairing analysis in the first lesson, Theorems 2.2 and 3.2, prove coverage by the level-one tiles and disjointness of their interiors. Representatives for \(\bar\Gamma\backslash\mathrm{PSL}_2(\mathbb Z)\) give the stated finite union \(D\); its subgroup translates partition the level-one cells. We check local finiteness explicitly. On a compact \(K\subset\mathfrak H\), choose \(\epsilon,M>0\) with
\(\epsilon\le\operatorname{Im}z\le M\) and \(|z|\le M\). If \(\eta\mathcal F\) meets \(K\), some \(z\in K\) has \(\eta^{-1}z\in\mathcal F\), of height at least \(\sqrt3/2\). Write \((c,d)\) for the bottom row of \(\eta^{-1}\). The imaginary-part identity gives
\[
\begin{gathered}
 |cz+d|^2\le 2M/\sqrt3,\\
 |c|\epsilon\le |cz+d|,\\
 |d|\le |cz+d|+|c|M.
\end{gathered}
\]
Thus only finitely many integer rows \((c,d)\) occur. For one row, fix a determinant-one completion \(\tau\). All other completions are \(T^n\tau\), \(n\in\mathbb Z\), by subtracting their upper rows. The real part of \(\tau z\) is bounded on \(K\); the condition \(\operatorname{Re}(T^n\tau z)\in[-1/2,1/2]\) bounds \(n\). Only finitely many projective matrices \(\eta\) occur. Every \(\Gamma\)-translate of \(D\) is a finite union of these level-one cells, so its family is locally finite as well.

On a compact truncation the boundaries consist of finitely many line and circle arcs and the truncation edges. To check their form after a group transformation, substitute its inverse \((az+b)/(cz+d)\) into the equations \(\operatorname{Re}w=\pm1/2\) and \(|w|=1\), and multiply by \(|cz+d|^2\). The resulting real equation is of the form \(A(x^2+y^2)+Bx+Cy+E=0\), hence describes a circle or a line; its denominator never vanishes in \(\mathfrak H\). Here is the zero-area estimate behind their omission. If a compact \(C^1\) arc has a parametrization with derivative bounded by \(L\), split its parameter interval into pieces of length at most \(\delta\). Each image lies in a square of side \(2(L+1)\delta\); there are \(O(\delta^{-1})\) squares, with total area \(O(\delta)\). Their finite union has arbitrarily small total area. Splitting piecewise \(C^1\) arcs into their finitely many pieces proves the same assertion. This is also the boundary estimate used for the compact plane integrals in Lemma 0.3 of the first lesson.

We need the finite-additivity consequence of that estimate. On a rectangle \(R\) meeting only finitely many cells, use one sufficiently fine rectangular grid for the continuous integrand and for all the intersected cells. Away from the boundary squares, each grid cell belongs to exactly one tile, and its Riemann-sum contribution occurs once. Uniform continuity makes the interior approximation errors tend to zero. The error on boundary squares is bounded by a fixed bound for the integrand times their total area, which also tends to zero. Consequently the integral on \(R\), or on its intersection with a finite union of cells, is the sum of the integrals on its tile pieces. All these intersections are Jordan regions: their boundaries are contained in finitely many line and circle arcs and rectangle edges.

For a locally finite tiling \(\{A_j\}\), take nested rectangular truncations \(R_m=[-m,m]\times[1/m,m]\) in \(\mathfrak H\); in \(S_h\) use \([0,h]\times[1/m,m]\). Finite additivity gives, for \(G\ge0\),
\[
 \int_{\Omega\cap R_m}G=\sum_j\int_{R_m\cap A_j}G.
\]
Only finitely many terms occur at each \(m\). Taking the supremum over \(m\) and over finite initial sets of tiles can be done in either order: both orders give the supremum of the same finite-partition integrals. For a fixed finite set, increasing truncations make the limit of the sum equal the sum of the limits, also when a limit is infinite. Hence
\[
 \int_\Omega G=\sum_j\int_{A_j}G
 \tag{4.0b}
\]
for the region \(\Omega\) being partitioned. Integrals of a tile use \(R_m\cap A_j\). They agree with exhaustion of its cell interiors: on each compact truncation the function is bounded, and deleting sufficiently small neighborhoods of its finitely many boundary arcs loses arbitrarily little integral. Cofinality of compact truncations proves exhaustion independence. For complex \(G\) with finite absolute integral, apply (4.0b) to \(|G|\). The sum of the absolute tile integrals is finite, and the error on any omitted collection of tiles is at most its absolute-integral tail. Passing through the finite partitions proves (4.0b) for \(G\).

Every element of \(\Gamma\) lies in exactly one left coset \(\Gamma_{\infty,h}\gamma\). Thus intersecting the \(\Gamma\)-tiling with \(S_h\) gives exactly the pieces defining \(D_\gamma\). Two of these pieces cannot share a cell interior, since they came from distinct subgroup tiles. In particular projection of the cell interiors of \(\gamma D\) into the strip is injective: a coincidence would put an interior point in both \(\gamma D\) and \(T^{hr}\gamma D\) for \(r\ne0\). Local finiteness follows from the already proved subgroup local finiteness on the compact rectangle \([0,h]\times[\epsilon,M]\); strip cuts add only finitely many boundary arcs there.

Finally cut \(\gamma D\) by the strips \(hr\le x<h(r+1)\), \(r\in\mathbb Z\). This is a locally finite partition. Translation by \(-hr\) sends its pieces to \(T^{-hr}\gamma D\cap S_h\) and preserves the integral of a period-\(h\) function, directly by translating its Riemann sums. Formula (4.0b) on both sides gives \(\int_{\gamma D}G=\int_{D_\gamma}G\). Apply (4.0b) to the projected strip tiling to obtain (4.0a), first for nonnegative functions and then for the absolutely integrable complex case. The original domains \(\gamma D\) need not lie inside a single strip. \(\square\)

For \(\Gamma_0(N)\), the infinity width is one, so we use \(h=1\). At any cusp of a finite-index group, conjugation by its integral scaling matrix gives a subgroup containing \(\{\pm T^{h_Pr}\}\) after adjoining \(-I\). The same lemma then uses the actual strip width \(h_P\).

**Theorem 4.1.** For \(f\in S_k(\Gamma_0(N))\) and \(m\ge1\),
\[
I_\Gamma(f,P_m)=A_{k,m}a_m(f),\qquad
\langle f,P_m\rangle_\Gamma
=\frac{A_{k,m}}{d_\Gamma}a_m(f).
\tag{4.2}
\]
Also \(I_\Gamma(f,P_0)=0\).

**Proof.** Choose the finite-cell fundamental region \(D\) of Lemma 4.0. Theorem 3.2 shows that the sum of the absolute Poincaré summands converges uniformly on every compact subset of \(\mathfrak H\). Multiplication by the continuous factor \(|f(z)|y^{k-2}\) preserves this property. The nonnegative plane-series assertion of the first lesson, Lemma 0.3, therefore identifies the integral of that absolute sum with the sum of its integrals, before any finiteness assumption. After the substitution \(w=\gamma z\), the absolute integral of one summand of
\(f(z)\overline{P_m(z)}y^k d\mu\) is
\[
\int_{\gamma D}|f(w)|\,e^{-2\pi m\operatorname{Im}w}
\operatorname{Im}(w)^{k-2}\,d(\operatorname{Re}w)\,d(\operatorname{Im}w),
\]
where \(D\) is a fundamental domain for \(\Gamma\). To verify cancellation, use
\(f(z)=j(\gamma,z)^{-k}f(w)\) and
\(y^k=\operatorname{Im}(w)^k|j(\gamma,z)|^{2k}\).
The function \(|f(w)|e^{-2\pi m\operatorname{Im}w}\operatorname{Im}(w)^{k-2}\) has period one. Lemma 4.0 identifies the sum of its integrals over \(\gamma D\) with its integral over the projected tiles and hence over \(0\le\operatorname{Re}w<1\).

On that strip near \(y=0\), Theorem 2.1 bounds the absolute integrand by \(A y^{k/2-2}\), which is integrable because \(k>2\). Near infinity, \(f\) decays exponentially. This works for both \(m\ge1\) and \(m=0\), and supplies a continuous integrable majorant depending only on \(y\), after joining the two bounds over a compact height interval. The sum of absolute integrals is consequently finite. The complex-series assertion of Lemma 0.3 now permits the interchange on \(D\), and the complex part of Lemma 4.0 unfolds the period-one function \(f(w)e^{-2\pi im\bar w}\operatorname{Im}(w)^{k-2}\). Lemma 0.3 also identifies the strip integral with its iterated rectangular integral:
\[
I_\Gamma(f,P_m)=
\int_0^\infty\int_0^1 f(x+iy)e^{-2\pi im(x-iy)}y^{k-2}\,dx\,dy.
\tag{4.3}
\]
At fixed \(y\), Fourier orthogonality makes the inner integral
\(a_m(f)e^{-4\pi my}\). Its integral in \(y\) is \(A_{k,m}a_m(f)\), after substituting \(t=4\pi my\). For \(m=0\), the inner integral is the cusp constant \(a_0(f)=0\). Dividing by \(d_\Gamma\) proves the normalized identity. \(\square\)

**Corollary 4.2.** The \(P_m\), \(m\ge1\), span \(S_k(\Gamma_0(N))\). Already
\[
P_1,\ldots,P_B,\qquad B=\lfloor k d_\Gamma/12\rfloor,
\tag{4.4}
\]
span it, with possible linear relations.

**Proof.** The space is finite dimensional by the preceding lesson. A form orthogonal to every \(P_m\) has every positive Fourier coefficient zero by (4.2), and its constant is zero because it is cuspidal. It is therefore zero. A proper subspace in a finite-dimensional positive definite inner-product space has a nonzero orthogonal complement, proving the first assertion. For the finite list, (4.2) and the proved complex coefficient bound make its orthogonal complement zero as well. If \(B=0\), that bound says the cusp space itself is zero. \(\square\)

Individual Poincaré series can vanish. The spanning assertion does not assert their linear independence.

## 5. The Eisenstein complement

For any weight and finite-index group, define
\[
E_k(\Gamma)=
\{f\in M_k(\Gamma):I_\Gamma(f,g)=0
\text{ for every }g\in S_k(\Gamma)\}.
\tag{5.1}
\]
This definition uses only pairings that converge by Theorem 1.1.

**Theorem 5.1.** There is a direct sum
\[
M_k(\Gamma)=E_k(\Gamma)\oplus S_k(\Gamma).
\tag{5.2}
\]
For even \(k\ge4\), the space \(E_k(\Gamma)\) has a basis of holomorphic Eisenstein series, one for each cusp, whose vectors of cusp constants are the coordinate vectors.

**Proof.** First note that every space here is finite dimensional. For even weights this was proved in the preceding lesson. In an odd positive weight, if \(M_k\ne0\), choose a nonzero \(f_0\in M_k\). Multiplication by \(f_0\) injects \(M_k\) into the finite-dimensional even-weight space \(M_{2k}\): a product of two holomorphic functions cannot vanish identically unless one factor does. Nonpositive weights were already determined.

First prove (5.2) using finite-dimensional linear algebra. Choose a basis \(g_1,\ldots,g_s\) of \(S_k\). Its Gram matrix is invertible by positive definiteness. For any \(f\in M_k\), there are unique coefficients \(b_j\) for which
\[
I_\Gamma\left(f-\sum_j b_jg_j,g_i\right)=0
\quad(1\le i\le s).
\]
This gives the sum in (5.2). Its intersection is zero because a cusp form orthogonal to itself has zero norm.

Now suppose \(k\ge4\) is even. We may replace \(\Gamma\) by
\(\Gamma^+=\langle\Gamma,-I\rangle\), since neither the even-weight spaces nor the quotient changes. Choose one scaling matrix \(\alpha_P\in\mathrm{SL}_2(\mathbb Z)\) for each cusp \(P\), and let \(\Gamma_P\) be its stabilizer in \(\Gamma^+\). If \(h_P\) is the width, then
\[
\alpha_P^{-1}\Gamma_P\alpha_P
=\{\pm T^{h_Pr}:r\in\mathbb Z\}.
\]
Define
\[
E_{P,k}(z)=
\sum_{\gamma\in\Gamma_P\backslash\Gamma^+}
(1|_k\alpha_P^{-1}\gamma)(z).
\tag{5.3}
\]
The constant seed is fixed by the conjugate stabilizer, so this is well-defined.

The bottom rows of \(\alpha_P^{-1}\gamma\) are primitive and distinct modulo sign. Equal rows would give a left translation; because both original matrices lie in \(\Gamma^+\), that translation is a multiple of \(h_P\) after conjugation, and hence represents the same \(\Gamma_P\)-coset. The lattice majorant used in Theorem 3.2 proves absolute locally uniform convergence, and reindexing proves modularity.

At a cusp \(Q\), slash (5.3) by \(\alpha_Q\). Lemma 3.1 makes the sum of the terms with nonzero lower-left entry tend uniformly to zero. A term with that entry zero exists exactly when some \(\gamma\) takes \(Q\) to \(P\). Since our chosen cusps are inequivalent, this happens exactly when \(Q=P\); then there is one such coset, represented by the identity, whose summand is one. Thus the series is holomorphic at every cusp and
\[
a_0(E_{P,k}|_k\alpha_Q)=\delta_{P,Q}.
\tag{5.4}
\]

Apply the width-\(h_P\) form of Lemma 4.0 to \(\alpha_P^{-1}\Gamma^+\alpha_P\). The locally uniform absolute convergence just proved and the nonnegative and complex-series assertions of the first lesson, Lemma 0.3, then unfold \(I_\Gamma(f,E_{P,k})\), for a cusp form \(f\), to
\[
\int_0^\infty\int_0^{h_P}
(f|_k\alpha_P)(x+iy)y^{k-2}\,dx\,dy.
\]
Absolute convergence follows from the same bound near zero and exponential decay near infinity as in Theorem 4.1. The inner integral is zero because \(f\) has zero constant term at \(P\). Consequently every \(E_{P,k}\) lies in (5.1).

Finally, for any \(f\in M_k\),
\[
f-\sum_P a_0(f|_k\alpha_P)E_{P,k}
\]
vanishes at all cusps, by (5.4), and is a cusp form. Thus the Eisenstein series span the complement in (5.2). Their constant vectors make them linearly independent. \(\square\)

In particular, for these even weights,
\[
\dim E_k(\Gamma)=c,\qquad E_k(\Gamma)\perp S_k(\Gamma),
\]
in agreement with the preceding lesson's dimension formula. For \(\Gamma_0(N)\), the series attached to infinity is exactly \(P_0\).

The pairing and the linear-algebra decomposition still hold in weight two, but the series (3.1) and (5.3) are not asserted to converge absolutely there. This lesson does not identify the weight-two complement by an absolutely convergent Eisenstein sum. The construction of that sum and the Poincaré spanning argument have the explicit hypothesis \(k>2\).

## 6. Two worked examples

### 6.1. A Poincaré series in the discriminant space

At level one, \(S_{12}=\mathbb C\Delta\) and \(a_1(\Delta)=1\), by the ring and dimension results already proved. Therefore \(P_1=C\Delta\) for some scalar. Formula (4.2) gives
\[
I(\Delta,P_1)=\frac{\Gamma(11)}{(4\pi)^{11}}.
\]
Because the pairing is linear in the first variable, the left side is
\(\overline C\,I(\Delta,\Delta)\). The right side and the norm are positive real numbers, so
\[
P_1=
\frac{10!}{(4\pi)^{11}I(\Delta,\Delta)}\,\Delta.
\tag{6.1}
\]
Here the projective index is one, so the normalized and unnormalized norms coincide. In particular this Poincaré series is nonzero, despite the possibility of vanishing at other weights.

### 6.2. Eisenstein and cusp coefficient growth

For an even \(k\ge4\), the normalized level-one series has coefficients
\[
a_n(E_k)=-\frac{2k}{B_k}\sigma_{k-1}(n)\qquad(n\ge1).
\]
The divisor \(n\) itself gives the lower bound, while replacing a divisor by its complementary divisor gives the upper bound:
\[
n^{k-1}\le\sigma_{k-1}(n)
=n^{k-1}\sum_{d\mid n}d^{1-k}
\le\zeta(k-1)n^{k-1}.
\tag{6.2}
\]
Thus the absolute Eisenstein coefficients have two-sided bounds by fixed positive multiples of \(n^{k-1}\). Cusp coefficients have the smaller upper bound \(O(n^{k/2})\). For example, the coefficients of \(E_{12}\) grow in this two-sided sense like \(n^{11}\), whereas \(\tau(n)=O(n^6)\) follows for \(\Delta\) from Theorem 2.1. No optimal cusp exponent is claimed here.

## 7. Exercises

1. **Easy.** Prove that \(y^k|f(z)|^2\) is \(\Gamma\)-invariant for \(f\in M_k(\Gamma)\). Check invariance of the measure as well.
2. **Medium.** Prove Hecke's bound. At a regular cusp of width \(h\), optimize the choice of \(y\) in (2.2) for \(k>0\).
3. **Medium.** Prove that every \(P_m\), \(m\ge1\), vanishes at every cusp of \(\Gamma_0(N)\), including cusps not equivalent to infinity.
4. **Medium.** Show that \(P_0\) is the Eisenstein series at infinity with constant one there and zero at the other cusps. At level one, determine its exact multiple of the full lattice series \(G_k\).
5. **Hard.** For even \(k\ge4\) and \(m\ge1\), compute all Fourier coefficients of \(P_m\) on \(\Gamma_0(N)\) in terms of Kloosterman sums and \(J\)-Bessel functions. Prove the coefficient formula, its sign and its absolute convergence, without using a bound for Kloosterman sums stronger than the trivial one.

## 8. Full solutions

### Solution 1

The modular law gives
\[
|f(\gamma z)|^2=|cz+d|^{2k}|f(z)|^2,
\]
and the imaginary part gives
\(\operatorname{Im}(\gamma z)^k=y^k|cz+d|^{-2k}\).
Their product is \(y^k|f(z)|^2\). The real Jacobian of a holomorphic change of coordinate is the squared absolute derivative, here \(|cz+d|^{-4}\). Since the new \(y^2\) is \(y^2|cz+d|^{-4}\), division by it cancels the Jacobian. Thus \(dx\,dy/y^2\) is invariant too.

### Solution 2

For a cusp form, invariance reduces boundedness of \(y^{k/2}|f|\) to a quotient domain. On its compact part this function has a maximum. In each of the finitely many scaled cusp strips, the positive leading Fourier exponent bounds it by a constant times \(y^{k/2}e^{-ay}\), which tends to zero. This produces a global constant \(A\), and the same constant works for every slash by a scaling matrix.

Fourier integration over the width \(h\) gives (2.2). For \(k>0\), minimize
\[
-\frac k2\log y+\frac{2\pi n}{h}y.
\]
Its derivative vanishes at \(y=kh/(4\pi n)\), and the function decreases before that point and increases afterwards. Consequently
\[
|a_n|\le
A\left(\frac{4\pi e}{kh}\right)^{k/2}n^{k/2}.
\]
This is the claimed bound with an explicit constant from \(A\). For an irregular cusp use period \(2h\) and the same optimization; its even-index coefficients are zero.

### Solution 3

Choose a scaling matrix \(\alpha\) for the cusp being tested. In \(P_m|_k\alpha\), the terms are attached to \(\gamma\alpha\). The primitive bottom rows are distinct modulo sign, and their nonzero lower-left entries contribute at most
\(C_k(y^{-k}+y^{1-k})\) by Lemma 3.1. This bound is uniform in the real part and tends to zero.

If this cusp is inequivalent to infinity, there is no matrix \(\gamma\alpha\) with lower-left entry zero, so this accounts for every term. If it is equivalent to infinity, there is one such coset and its term is \(e(mz)\), of absolute value \(e^{-2\pi my}\), which also tends to zero. Hence the entire slash tends uniformly to zero in both cases.

It is periodic with the cusp's width. Its holomorphic function on the punctured \(q_h\)-disk is bounded, so extends across zero, and the limit we computed makes its value there zero. This is precisely vanishing at that cusp, and the choice of cusp was arbitrary.

### Solution 4

The series \(P_0\) equals (5.3) for \(P=\infty\) and \(\alpha_P=I\). The proof of Theorem 5.1 shows that its constant vector is one at infinity and zero elsewhere, and that it is orthogonal to cusp forms. Those conditions characterize it uniquely: a difference would be a cusp form orthogonal to itself.

More explicitly,
\[
P_0(z)=\frac12
\sum_{\substack{(c,d)\in\mathbb Z^2\\\gcd(c,d)=1,\ N\mid c}}
(cz+d)^{-k}.
\]
At level one write every nonzero lattice row uniquely as a positive integer times a primitive row. Absolute convergence permits the grouping, giving
\[
G_k(z)=\zeta(k)\sum_{\gcd(c,d)=1}(cz+d)^{-k}
=2\zeta(k)P_0(z).
\]
Thus \(P_0=G_k/(2\zeta(k))=E_k\), in the earlier lesson's constant-one normalization.

### Solution 5: the Kloosterman–Bessel formula

For positive \(m,n,c\), define
\[
S(m,n;c)=
\sum_{\substack{d\bmod c\\(d,c)=1}}
e\left(\frac{m\bar d+nd}{c}\right),
\qquad d\bar d\equiv1\pmod c.
\tag{8.1}
\]
For \(c=1\) the sum is one, with the usual unique-residue convention. Define the Bessel function needed here by its convergent entire series
\[
J_\nu(x)=
\sum_{r\ge0}
\frac{(-1)^r(x/2)^{\nu+2r}}{r!(\nu+r)!},
\qquad \nu\in\mathbb Z_{\ge0}.
\tag{8.2}
\]
The factorial denominators prove convergence for every \(x\). We claim that
\[
\boxed{\displaystyle
a_n(P_m)=\delta_{m,n}
+2\pi i^{-k}\left(\frac nm\right)^{(k-1)/2}
\sum_{\substack{c>0\\N\mid c}}
\frac{S(m,n;c)}{c}
J_{k-1}\left(\frac{4\pi\sqrt{mn}}c\right)}
\quad(n\ge1).
\tag{8.3}
\]
Since \(k\) is even, \(i^{-k}=i^k=(-1)^{k/2}\). There is no missing factor two.

The row \((0,1)\) in (3.1) contributes \(e(mz)\), giving \(\delta_{m,n}\). For a fixed \(c>0\), group the remaining rows as
\(d=d_0+ct\), \(t\in\mathbb Z\), with \(d_0\) a unit modulo \(c\). Choose \(a\) with \(ad_0\equiv1\pmod c\). The determinant-one identity is
\[
\gamma z=\frac ac-\frac1{c(cz+d)}.
\]
Therefore the terms for this residue class are
\[
c^{-k}e(ma/c)
\sum_{t\in\mathbb Z}
(z+t+d_0/c)^{-k}
\exp\left(-\frac{2\pi im}{c^2(z+t+d_0/c)}\right).
\tag{8.4}
\]
Changing the completion of the row changes \(a\) by a multiple of \(c\), and hence leaves (8.4) unchanged.

Extract the \(n\)-th coefficient by integrating against \(e(-nz)\) along \(0\le x\le1\), with \(y>0\) fixed. The integer \(t\) concatenates these intervals into a horizontal line. Substituting \(w=z+t+d_0/c\) gives the contribution
\[
c^{-k}e((ma+nd_0)/c)\,L_{m,n,c},
\]
where
\[
L_{m,n,c}=
\int_{\mathbb R+iy}
w^{-k}\exp\left(-2\pi i\left(nw+\frac m{c^2w}\right)\right)\,dw.
\tag{8.5}
\]
These exchanges are justified absolutely. In the upper half-plane the second exponential in (8.4) has absolute value at most one. For fixed \(y\), the sum of the absolute coefficient integrals is consequently bounded by
\[
C_{n,y}\sum_{\substack{c>0\\N\mid c}}
c^{-k}\varphi(c)
\int_{\mathbb R}|u+iy|^{-k}\,du
\le C'_{n,y,k}\sum_{c\ge1}c^{1-k}<\infty.
\tag{8.6}
\]

We compute (8.5). If \(n\le0\), close the horizontal line by a large semicircle in the upper half-plane. There is no enclosed singularity. Both exponential factors are bounded there, and the arc integral is \(O(R^{1-k})\); thus \(L_{m,n,c}=0\). This also verifies that these terms have neither negative coefficients nor a constant.

For \(n>0\), close below the line. The orientation is clockwise and zero is enclosed. On a semicircle of radius \(R\) centered at \(iy\), the factor \(e^{-2\pi inw}\) is bounded by \(e^{2\pi ny}\), the factor involving \(1/w\) is bounded as \(R\to\infty\), and \(|w|^{-k}=O(R^{-k})\). The arc integral again tends to zero. Hence
\[
L_{m,n,c}=-2\pi i\,
\operatorname{Res}_{w=0}
\left[w^{-k}e^{-2\pi inw}e^{-2\pi im/(c^2w)}\right].
\tag{8.7}
\]
Expand the two exponentials. The coefficient of \(w^{-1}\) requires the first exponential's power to be \(k+r-1\) when the second's is \(-r\), so the residue is
\[
(-2\pi in)^{k-1}
\sum_{r\ge0}
\frac{(-4\pi^2mn/c^2)^r}{r!(k+r-1)!}.
\tag{8.8}
\]
Comparison with (8.2) gives
\[
L_{m,n,c}=
2\pi i^{-k}c^{k-1}
\left(\frac nm\right)^{(k-1)/2}
J_{k-1}\left(\frac{4\pi\sqrt{mn}}c\right).
\tag{8.9}
\]
For the sign, the prefactor in (8.7) contributes
\(-i(-i)^{k-1}=(-i)^k=i^{-k}\).

Sum over the units \(d_0\bmod c\). Their phases give exactly (8.1); multiplying \(c^{-k}\) by (8.9), then summing over \(c\), proves (8.3).

Finally \(|S(m,n;c)|\le\varphi(c)\le c\). The series (8.2) gives
\(J_{k-1}(x)=O_k(x^{k-1})\) for \(x\) in any fixed bounded interval near zero. With \(m,n\) fixed, the summands in (8.3) are therefore \(O_{k,m,n}(c^{1-k})\). The sum is absolutely convergent for \(k>2\), using only the trivial Kloosterman bound. This completes the solution.

The same residue calculation with \(m=0\) also yields, for \(n\ge1\),
\[
a_n(P_0)=
\frac{(-2\pi i)^k n^{k-1}}{(k-1)!}
\sum_{\substack{c>0\\N\mid c}}
\frac{S(0,n;c)}{c^k},
\tag{8.10}
\]
where \(S(0,n;c)\) is defined by (8.1) with \(m=0\). The residue then has only the power \(k-1\) of \(e^{-2\pi inw}\). The same bound (8.6) proves convergence.

## What this lesson does not prove

The local arguments establish pairing invariance and convergence (Theorem 1.1), Hecke's bound (Theorem 2.1), Poincaré convergence and vanishing at every cusp (Theorem 3.2), unfolding (Theorem 4.1), and spanning and the orthogonal decomposition (Corollary 4.2 and Theorem 5.1), subject to the integration foundations recorded below. Both examples and all five exercises retain their computations and solutions. The Kloosterman–Bessel formula, including its contour integral and convergence, is derived in Solution 5.

The earlier results used are the imaginary-part and slash identities and holomorphic cusp expansions from Modular forms, lattice functions and Eisenstein series, Proposition 1.1 and Sections 1–2; cusp widths and stabilizers from Congruence subgroups, cusps and elliptic points, Section 2 and Proposition 2.1, with regularity in Section 4; the coefficient bound from Dimension formulas for congruence subgroups, Theorem 6.1; and \(S_{12}=\mathbb C\Delta\), with \(a_1(\Delta)=1\), from The valence formula and the ring of modular forms of level one, Theorems 2.1–2.2. The coefficient bound also proves the finite dimensionality needed here: truncation to its finitely many coefficients is injective, so the space embeds in a finite-dimensional coordinate space. This avoids the unresolved general Riemann–Roch dimension input. The finite cusp neighborhoods and compact remainder come from Modular curves and their genus, Proposition 2.2 and Theorem 2.3. The quotient volume uses The upper half-plane and the modular group, Proposition 5.1, and the finite-domain union.

The circle, contour-deformation and locally uniform limit facts are proved in the first lesson, Lemma 0.2; removable singularities and the Laurent-contour calculation are proved in Lemma 0.1 here. Its Lemma 0.3 supplies the continuous improper-series and rectangular interchanges. Lemma 4.0 here proves local finiteness, compact boundary-nullity, finite-partition additivity and projected-strip unfolding, including the actual cusp width in Theorem 5.1. These arguments discharge the positive and absolute series interchanges in Theorem 4.1 without a general measurable Tonelli or Fubini theorem.

Real completeness, elementary continuous integration and compactness retain their foundational status. The real plane change-of-variables theorem used for the Möbius substitutions, beyond the computed Jacobian, has not been proved here. Theorem 1.1's independence for every measurable fundamental domain also retains its general measurable-integration prerequisite; the present finite-cell argument does not prove that broader assertion. The [Measure and Integration course](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) is a proposed provider for general integration, whose exact proofs have not been verified. Fremlin's freely available author text, Corollaries 252C and 252H, states the precise sigma-finite versions. Complex integrals follow by taking real and imaginary parts. The gamma integral at the positive integer \(k-1\) is evaluated by integration by parts, and the Bessel function used here is defined by its series. No special-function contour identity or nontrivial Kloosterman estimate is imported.

The absolute Poincaré and Eisenstein constructions require \(k>2\). Their weight-two regularization is not proved here. The Weil bound for Kloosterman sums and the optimal cusp-coefficient bound are not used or proved.

## References

- **Wiese 2018.** G. Wiese, *Computational Arithmetic of Modular Forms*, §6.1, Petersson scalar product. [Author's notes](https://arxiv.org/abs/1809.04645).
- **Elkies.** N. Elkies, *An upper bound on the coefficients of a PSL₂(Z) cusp form*, Math 259 notes, pages 1–3, for comparison of the Poincaré and Fourier calculations. The displayed series and integral normalizations used in this lesson are specified in (3.1) and (4.2). [Author's notes](https://people.math.harvard.edu/~elkies/M259.02/poincare.pdf).

- **Lebl.** J. Lebl, *Guide to Cultivating Complex Analysis*, version 1.9, Theorems 3.3.10–3.3.11, 5.2.2 and 5.3.2, as free background for the analytic facts proved in Lemma 0.1 and the earlier first lesson. [Author’s book](https://www.jirka.org/ca/ca.pdf).
- **Fremlin.** D. H. Fremlin, *Measure Theory*, Volume 2, Corollaries 252C and 252H, the authoritative original for the measure-and-integration prerequisite. [Author’s Chapter 25](https://www1.essex.ac.uk/maths/people/fremlin/chap25.pdf).
