# Finite covolume and arithmetic quotients

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI. Independent AI review remains separate; no human review is claimed. Original exposition and exercises are dedicated under CC0.*

A quotient measure can exist and still have infinite total mass. A **lattice** in a locally compact group is a discrete subgroup whose invariant quotient measure has finite positive mass. That mass is its **covolume**, once the Haar measures on the group and subgroup have been fixed. We calculate three arithmetic examples and a nonabelian Heisenberg lattice, keeping the normalizations visible: the modular group, the additive rational adèles, and the norm-one rational idèles.

## What to know first

The preceding [quotient lesson](quotient-measures-and-weils-integration-formula.md), Theorem 3.1, proves the modular criterion and the normalized Weil formula. Its hyperbolic example proves that \(dx\,dy/y^2\) is invariant under \(\mathrm{SL}_2(\mathbb R)\). [Haar measure on locally compact groups](haar-measure-on-locally-compact-groups.md), Theorems 2.2, 5.1, 10.1 and 11.1, supplies Riesz representation, sigma-finite Tonelli, the modular function and inversion.

For the last two examples, read these exact programme proofs:

- [Completions, the p-adic numbers and complete discretely valued fields](course:NT-LOC/NT-LOC-02), Theorem 2.1 and Proposition 2.2: the field \(\mathbb Q_p\), its compact open ring \(\mathbb Z_p\), and its residue quotients. Only the rational case of the construction is needed.
- [Restricted products and profinite completions](course:NT-ADL/NT-ADL-01), Propositions 1.1–1.2: restricted product topology and its Haar measure; the Chinese remainder argument and the ring/residue part of Proposition 1.4. Character duality in that lesson is not used here.
- [The adèle ring of a number field](course:NT-ADL/NT-ADL-02), the rational proof of Theorem 2.2: a half-open additive fundamental domain. We apply it to integration below.
- [Idèles and the idèle class group](course:NT-ADL/NT-ADL-03), Proposition 3.1: the idèle topology. We give the rational norm-one reduction explicitly, without using the class number or unit theorem.

These are specific internal proofs. The present lesson supplies the integration and normalization arguments; it does not assume the general number-field compactness theorem. Elementary integer arithmetic used in the reductions is recalled with proof next.

## 1. Two integer reductions

**Lemma 1.1.** If \(c,d\in\mathbb Z\) are relatively prime, they are the bottom row of a matrix in \(\mathrm{SL}_2(\mathbb Z)\). Every nonzero rational number has a unique expression \(\varepsilon\prod_p p^{e_p}\), with \(\varepsilon\in\{1,-1\}\), integer exponents, and only finitely many nonzero exponents. Consequently
\[
 |r|_\infty\prod_p|r|_p=1.
 \tag{1.1}
\]

*Proof.* Repeated division with remainder strictly decreases nonnegative remainders, so the Euclidean algorithm terminates. Back substitution expresses the greatest common divisor as an integer combination. For coprime \(c,d\), choose \(a,b\) with \(ad-bc=1\). This proves the first assertion and Bézout's identity.

For completeness, factor a positive integer by induction: a composite integer is a product of smaller positive integers. If a prime \(p\) divides \(uv\) and does not divide \(u\), Bézout gives \(sp+tu=1\); multiplying by \(v\) shows that \(p\) divides \(v\). This prime-divisor rule proves uniqueness by cancelling a prime from two proposed factorizations and inducting. Applying the result to numerator and denominator gives the rational factorization. Its real absolute value is \(\prod p^{e_p}\), and \(|r|_p=p^{-e_p}\), proving (1.1). This also proves directly that these rational absolute values are multiplicative and ultrametric: over a common denominator, the valuation of a sum is at least the lesser valuation. ∎

### Borel fundamental domains and covolume

The general quotient facts now have full proofs in [the preceding lesson](quotient-measures-and-weils-integration-formula.md#finite-covolume-unimodularity): a lattice forces its ambient group to be unimodular, and a closed discrete cocompact subgroup is a lattice. To calculate its covolume, the following result turns a Borel set of representatives into a measure calculation. Bekka, de la Harpe and Valette give a complementary treatment of fundamental domains; the proof below explicitly handles Borel representatives.

**Theorem 1.2.** Let \(G\) be a sigma-compact unimodular LCH group and \(\Gamma\) a closed discrete subgroup, equipped with counting measure. Then \(\Gamma\) is countable and there exists a Borel set \(D\subset G\) meeting each right coset \(g\Gamma\) exactly once. For the quotient measure \(\nu\) normalized by the Weil formula,
\[
\nu(G/\Gamma)=\mu(D),
\tag{1.2}
\]
allowing infinite values. Any Borel set of unique right-coset representatives gives the same equality.

*Proof.* A compact set meets \(\Gamma\) in finitely many points: its intersection with the closed discrete subgroup is a compact discrete space, whose singleton cover has a finite subcover. A countable compact cover of \(G\) therefore makes \(\Gamma\) countable.

Choose a relatively compact open identity neighborhood \(V\) with \(V^{-1}V\cap\Gamma=\{e\}\). It exists by continuity of multiplication and inversion and discreteness. Sigma-compactness gives a countable cover \(G=\bigcup_{n\geq1}U_n\), with \(U_n=g_nV\): each set of a countable compact cover has a finite subcover by translates of \(V\). The quotient map \(q\) is open, and its restriction to each \(U_n\) is injective, because \(u^{-1}u'\in\Gamma\) for two points of one coset. It is consequently a homeomorphism onto the open set \(q(U_n)\).

Define
\[
D_n=U_n\setminus\bigcup_{m<n}U_m\Gamma,
\qquad D=\bigcup_{n\geq1}D_n.
\]
The saturated sets \(U_m\Gamma\) are open, so \(D\) is Borel. Each coset has a first chart which meets it, and in that chart exactly one point; this point lies in \(D_n\), and later charts contribute none. Hence \(G\) is the disjoint union of \(D\gamma\), \(\gamma\in\Gamma\).

The same integration argument works for any Borel transversal \(D\). Put \(\nu_0(B)=\mu(D\cap q^{-1}(B))\) for Borel \(B\subset G/\Gamma\). This is a Borel measure. For a Borel \(B\subset q(U_n)\), write \(U_B=(q|_{U_n})^{-1}(B)\). The sets
\[
D\cap U_B\gamma^{-1},\qquad \gamma\in\Gamma,
\]
partition \(D\cap q^{-1}(B)\), and their right translates by \(\gamma\) partition \(U_B\). Right Haar invariance and countable additivity therefore give
\[
\nu_0(B)=\mu(U_B).
\tag{1.3}
\]
In particular, \(\nu_0\) is finite and Radon on every chart, as the transport of \(\mu|_{U_n}\). For completeness, one can establish its global Radon property without assuming a regularity theorem for arbitrary Borel transversals. The functional
\(F\mapsto\int_DF(q(g))\,d\mu(g)\)
is positive and finite on \(C_c(G/\Gamma)\): a finite chart cover of its support bounds its absolute integral by \(\|F\|_\infty\) times the sum of the finite \(\mu(U_n)\) in that cover. Riesz representation gives a Radon measure \(\nu_1\). For tests supported in a chart it agrees with the transported measure in (1.3), so local Radon uniqueness identifies \(\nu_1\) and \(\nu_0\) on that chart. Partitioning a Borel set among the first chart containing each point, using the countable cover \(q(U_n)\), proves equality on every Borel set. Thus \(\nu_0\) itself is Radon.

Finally, for \(f\in C_c(G)\), countable Tonelli and right invariance give
\[
\begin{aligned}
\int_{G/\Gamma}\sum_{\gamma\in\Gamma}f(g\gamma)\,d\nu_0(g\Gamma)
&=\int_D\sum_{\gamma\in\Gamma}f(d\gamma)\,d\mu(d)\\
&=\sum_{\gamma\in\Gamma}\int_{D\gamma}f(u)\,d\mu(u)
=\int_Gf(u)\,d\mu(u).
\end{aligned}
\]
For complex \(f\), absolute summability follows by applying the same calculation to \(|f|\), whose integral is finite. The quotient lesson's normalized uniqueness identifies \(\nu_0=\nu\). Taking the measure of the whole quotient proves (1.2). \(\square\)

## 2. A fundamental region in the upper half-plane

Write \(G=\mathrm{SL}_2(\mathbb R)\), \(\Gamma=\mathrm{SL}_2(\mathbb Z)\), and \(K=\mathrm{SO}(2)\). Integer matrices form a closed discrete subset of real matrix space, and a compact set meets them in finitely many points. Hence \(\Gamma\) is a closed discrete subgroup. Counting measure on \(\Gamma\) is unimodular.

We also need unimodularity of \(G\), rather than an unproved general assertion about Lie groups. Put
\[
 U(t)=\begin{pmatrix}1&t\\0&1\end{pmatrix},\quad
 L(t)=\begin{pmatrix}1&0\\t&1\end{pmatrix},\quad
 D(a)=\begin{pmatrix}a&0\\0&a^{-1}\end{pmatrix}.
\]
Conjugating \(U(t)\) by \(D(2)\) gives \(U(4t)=U(t)^4\). A homomorphism into an abelian group is constant on conjugacy classes. Thus its positive modular value satisfies \(\Delta(U(t))=\Delta(U(t))^4\), so it is one. Conjugation by \(D(1/2)\) gives the same conclusion for \(L(t)\). These matrices generate \(G\). Indeed,
\[
 W(a)=U(a)L(-1/a)U(a)=\begin{pmatrix}0&a\\-1/a&0\end{pmatrix},
 \qquad D(a)=W(a)W(1)^{-1}
\]
for \(a\ne0\), and a matrix \(\begin{pmatrix}a&b\\c&d\end{pmatrix}\) with \(a\ne0\) equals \(L(c/a)D(a)U(b/a)\). If \(a=0\), multiplication on the left by \(U(1)\) makes the top-left entry nonzero. Therefore \(\Delta_G=1\). The quotient criterion now applies.

Let \(\mathbb H=\{x+iy:y>0\}\) and
\[
 \mathcal F=\{z\in\mathbb H:|\operatorname{Re}z|\le1/2,\ |z|\ge1\}.
 \tag{2.1}
\]
The action is \(gz=(az+b)/(cz+d)\), with
\(\operatorname{Im}(gz)=y/|cz+d|^2\).

**Proposition 2.1.** Every \(\Gamma\)-orbit meets \(\mathcal F\). If two points of its interior lie in the same orbit, they are equal, and the transforming matrix is \(I\) or \(-I\).

*Proof.* For fixed \(z=x+iy\), there are only finitely many integer pairs \((c,d)\) with \(|cz+d|\le R\): the inequality bounds \(|c|y\), and then \(|cx+d|\). Among relatively prime pairs choose one minimizing the positive number \(|cz+d|\); the pair \((0,1)\) supplies an initial bound. Lemma 1.1 extends the minimizing pair to \(\gamma\in\Gamma\). The point \(w=\gamma z\) has greatest imaginary part in its orbit. An integer translation moves its real part into \([-1/2,1/2]\) without changing its imaginary part. If \(|w|<1\), the matrix \(\begin{pmatrix}0&-1\\1&0\end{pmatrix}\) increases that imaginary part, a contradiction. Thus \(w\in\mathcal F\).

For an interior point, \(|x|<1/2\) and \(y^2>1-x^2>3/4\). If \(c\ne0\), then \(|cz+d|>1\). For \(|c|\ge2\), its square is at least \(c^2y^2>3\). For \(|c|=1,d=0\), use \(|z|>1\). For \(|c|=1,|d|\ge1\), its square is at least
\[
 (1-|x|)^2+y^2>2-2|x|>1.
\]
Consequently a matrix with \(c\ne0\) strictly decreases the imaginary part of an interior point. If it sends one interior point to another, its inverse has nonzero bottom-left entry too, and would strictly decrease it back. This is impossible. If \(c=0\), the determinant and integrality give \(a=d=\pm1\); the action is an integer translation. Two real parts strictly between \(-1/2\) and \(1/2\) force that translation to be zero, leaving \(\gamma=\pm I\). ∎

The boundary consists of two vertical rays and a circular arc. Each has two-dimensional Lebesgue measure zero: their vertical sections are finite except at two abscissae, and sigma-finite Tonelli applies. Their hyperbolic area is also zero because the density \(y^{-2}\) is locally bounded. Countably many \(\Gamma\)-translates of this boundary still have area zero. Removing them leaves a full-measure invariant subset on which the region's interior gives unique orbit representatives modulo \(\pm I\).

Its area is finite and explicit:
\[
 \operatorname{area}(\mathcal F)
 =\int_{-1/2}^{1/2}\int_{\sqrt{1-x^2}}^\infty\frac{dy\,dx}{y^2}
 =\int_{-1/2}^{1/2}\frac{dx}{\sqrt{1-x^2}}
 =\frac\pi3.
 \tag{2.2}
\]
The last step uses the one-variable substitution \(x=\sin t\), with \(-\pi/6\le t\le\pi/6\). The integral identities used here are proved in the tools lesson, Lemma 6.1.

The required calculus and circle facts, including the value of sine at a sixth of a half-turn, are proved in [the preceding topology lesson](course:function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity), Appendix (B1)–(B2).

The positive square root exists by the least upper bound property: for \(r>0\), the set \(\{t\ge0:t^2\le r\}\) is nonempty and bounded, and its supremum \(q\) has square \(r\). If \(q^2<r\), a sufficiently small positive \(\eta\) gives \((q+\eta)^2<r\), contrary to the upper-bound property. If \(q^2>r\), choose \(0<\eta<q\) with \((q-\eta)^2>r\); every member of the set is then less than \(q-\eta\), contrary to its supremum. The root is unique and continuous by
\(|\sqrt r-\sqrt s|=|r-s|/(\sqrt r+\sqrt s)\) for positive \(r,s\).
For \(b>0\), the reciprocal rule in Appendix (B1) and its fundamental theorem give
\[
 \int_b^R y^{-2}\,dy=\frac1b-\frac1R\quad(R>b).
\]
Monotone convergence in the tools lesson, Theorem 2.1, gives \(\int_b^\infty y^{-2}\,dy=1/b\). Applying Tonelli to the region in (2.1) therefore gives the middle integral in (2.2). To evaluate it, use the substitution identity in (B1) with \(x=\sin t\). Appendix (B2) proves that this map is strictly increasing on \([-\pi/6,\pi/6]\), has endpoint values \(-1/2,1/2\), and has derivative \(\cos t>0\). The circle identity consequently gives
\[
 \int_{-1/2}^{1/2}\frac{dx}{\sqrt{1-x^2}}
 =\int_{-\pi/6}^{\pi/6}\frac{\cos t}{\sqrt{1-\sin^2t}}\,dt
 =\int_{-\pi/6}^{\pi/6}1\,dt=\frac\pi3.
\]

## 3. From area to group covolume

Area in \(\mathbb H\) and Haar volume in \(G\) have different normalizations. Let
\[
 s(x+iy)=\begin{pmatrix}\sqrt y&x/\sqrt y\\0&1/\sqrt y\end{pmatrix},
 \quad k_\theta=\begin{pmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{pmatrix}.
\]
Every \(g\in G\) has a unique expression \(s(z)k\): set \(z=gi\), and then \(s(z)^{-1}g\) fixes \(i\), so belongs to \(K\). These operations are continuous, giving a homeomorphism \(\mathbb H\times K\to G\). Fix the Haar normalization
\[
 dg=\frac{dx\,dy}{y^2}\,\frac{d\theta}{2\pi}.
 \tag{3.1}
\]
For completeness the notation \(d\theta/(2\pi)\) on \(K=\mathrm{SO}(2)\) means the following Haar probability. An orthogonal real matrix of determinant one has first row \((c,s)\) of length one and second row \((-s,c)\): orthogonality leaves the two choices \(\pm(-s,c)\), and the determinant selects the plus sign. Appendix (B2) therefore shows that every element is exactly one \(k_\theta\) for \(0\le\theta<2\pi\). Multiplying matrices and using the addition formulas gives \(k_\theta k_\eta=k_{\theta+\eta}\). The map from \([0,2\pi]\) onto \(K\) is continuous, and \(K\) is compact as the closed bounded matrix set, by the preceding topology provider.

Define a positive functional on \(C(K)\) by
\[
 I(F)=\frac1{2\pi}\int_0^{2\pi} F(k_\theta)\,d\theta.
\]
It is bounded by \(\|F\|_\infty\) and takes one to one. The internally proved Riesz theorem in the Haar lesson represents it by a Radon probability. For a continuous \(2\pi\)-periodic \(g\) and \(0\le\alpha<2\pi\), Appendix (B1)'s translation substitution, subdivision, and periodicity give
\[
 \int_0^{2\pi}g(t+\alpha)\,dt
 =\int_\alpha^{2\pi}g(t)\,dt+\int_0^\alpha g(t)\,dt
 =\int_0^{2\pi}g(t)\,dt.
\]
Reduce any real \(\alpha\) modulo \(2\pi\); thus \(I\) is translation invariant and its representing measure is Haar probability. The half-open arc \(A=\{k_\theta:0\le\theta<\pi\}\) is Borel: it is the compact image of \([0,\pi]\) with its endpoint \(k_\pi\) removed. Its translate by \(k_\pi=-I\) is its disjoint complement. Invariance therefore gives \(\mu_K(A)=1/2\), proving the compact-fiber factor in (3.3) directly. \(\square\)

This really is left Haar measure. For \(a\in G\),
\(a s(z)=s(az)\kappa(a,z)\) for a continuous \(K\)-valued function \(\kappa\). Left multiplication by \(a\) therefore sends \((z,k)\) to \((az,\kappa(a,z)k)\). Integrate first over Haar probability on \(K\), then over invariant hyperbolic area. The integral of every \(C_c(G)\) function is unchanged. The transported Radon product is consequently Haar.

**Theorem 3.1.** With (3.1) and counting measure on \(\Gamma\), both \(\Gamma\backslash G\) and \(G/\Gamma\) have covolume \(\pi/6\). The hyperbolic quotient has area \(\pi/3\). In particular, \(\Gamma\) is a lattice.

*Proof.* On the full-measure set of regular base points from Proposition 2.1, each left orbit first selects a unique \(z\in\mathcal F^\circ\), then selects \(k_\theta\) with \(0\le\theta<\pi\). The remaining ambiguity \(-I\in\Gamma\) changes \(\theta\) by \(\pi\). Thus the Borel set
\[
 \mathcal D=\{s(z)k_\theta:z\in\mathcal F^\circ,\ 0\le\theta<\pi\}
\]
and its \(\Gamma\)-translates partition a full-Haar-measure subset of \(G\). Omitted fibers lie over the null boundary translates; Tonelli and (3.1) show they have Haar measure zero. The group is sigma-compact, since \(\mathbb H\times K\) is, so ordinary sigma-finite Tonelli is available. Hence for \(f\in C_c(G)\),
\[
 \int_G f(g)\,dg
 =\int_{\mathcal D}\sum_{\gamma\in\Gamma}f(\gamma g)\,dg.
 \tag{3.2}
\]
First prove this for nonnegative \(f\) by the countable partition; apply it to \(|f|\) to justify complex summation. The discrete averaging sum is locally finite: on compact subsets, only finitely many \(\gamma\) can move one compact set to meet another, since those \(\gamma\) lie in a compact set intersected with \(\Gamma\).

Define a positive functional on \(C_c(\Gamma\backslash G)\) by integrating its pullback over \(\mathcal D\). It is finite because
\[
 \mu_G(\mathcal D)=\operatorname{area}(\mathcal F)\cdot\frac\pi{2\pi}=\frac\pi6.
 \tag{3.3}
\]
Riesz representation gives a Radon measure. Formula (3.2), positive surjectivity of discrete averaging, and right invariance of \(dg\) show that this measure is right \(G\)-invariant and has the normalized Weil formula. Its total mass is (3.3): an increasing family of compactly supported quotient cutoffs tends to one, since the quotient is sigma-compact; monotone convergence on \(\mathcal D\) proves the assertion. Such cutoffs are obtained from the compact exhaustion and bump functions of the preceding lesson.

Finally, inversion identifies \(\Gamma\backslash G\) with \(G/\Gamma\). The inversion formula has no density factor because \(\Delta_G=1\), so it preserves the normalization and covolume. Equation (2.2) gives the hyperbolic area. ∎

**Normalization example.** The measure \(d\theta\), in place of \(d\theta/(2\pi)\), multiplies the group covolume by \(2\pi\), giving \(\pi^2/3\). Passing instead to \(\mathrm{PSL}_2(\mathbb R)\) and normalizing its compact stabilizer to probability gives covolume \(\pi/3\). Indeed \(-I\) has disappeared there, so the full compact fiber is used. A claimed number for a lattice volume is incomplete without its group and Haar normalization.

## 4. Additive rational adèles

Put
\[
 \mathbb A=\mathbb R\times\prod_p'(\mathbb Q_p,\mathbb Z_p),
 \qquad Z=\prod_p\mathbb Z_p.
\]
Use Lebesgue measure at the real place and additive Haar measures of mass one on each \(\mathbb Z_p\). The restricted product provider constructs their compatible Haar measure. On the open subgroup \(\mathbb R\times Z\) it is Lebesgue measure times Haar probability on \(Z\).

Theorem 2.2 of the adèle lesson proves, with rational principal parts and integer reduction, that
\[
 D=[0,1)\times Z
 \tag{4.1}
\]
is a Borel fundamental domain for \(\mathbb A/\mathbb Q\), with unique representatives, and that this quotient is compact and Hausdorff. Its proof uses only the local residue construction: subtract each of the finitely many negative local digit strings, then subtract an integer. A rational integral at every prime is an integer; two representatives in (4.1) can therefore differ only by an integer whose real absolute value is less than one, hence by zero. This also shows why integer reduction must change the finite components as well as the real one.

**Theorem 4.1.** The normalized invariant measure on \(\mathbb A/\mathbb Q\) is probability, and
\[
 \int_{\mathbb A} f(x)\,dx
 =\int_D\sum_{r\in\mathbb Q}f(x+r)\,dx
 \qquad(f\in C_c(\mathbb A)).
 \tag{4.2}
\]

*Proof.* The translates \(D+r\) are a disjoint Borel partition. The group is sigma-compact: the compact sets \([-n,n]\times(n!)^{-1}Z\), \(n\ge1\), exhaust it. Countable additivity, translation invariance and Tonelli give (4.2), with absolute convergence for complex \(f\). Moreover only finitely many summands occur uniformly on \(D\): a contributing rational lies in \(\operatorname{supp}f-\overline D\), a compact set; a compact set meets the closed discrete \(\mathbb Q\) finitely.

The positive functional \(F\mapsto\int_D F(x+\mathbb Q)\,dx\) on the compact quotient is represented by a Radon measure. Equation (4.2) and the quotient theorem identify it with the normalized invariant quotient measure. Its total mass is \(\mu(D)=1\), since the real interval has length one and \(Z\) has mass one. ∎

**Worked reduction.** Take real component \(11/10\), local components \(1/4\) at \(2\), \(2/9\) at \(3\), and zero at all other primes. Subtract \(r=1/4+2/9=17/36\). At \(2\) the remainder is \(-2/9\in\mathbb Z_2\); at \(3\) it is \(-1/4\in\mathbb Z_3\); every other coordinate is integral. The real remainder is \(113/180\), so it already lies in (4.1). This is an additive representative, not an idèle reduction.

## 5. Norm-one rational idèles

Let
\[
 J=\mathbb R^\times\times\prod_p'(\mathbb Q_p^\times,\mathbb Z_p^\times),
 \quad |x|=|x_\infty|\prod_p|x_p|_p,
 \quad J^1=\ker |\cdot|.
\]
Use the restricted multiplicative topology, as proved in Proposition 3.1 of the idèle lesson. The norm is a continuous homomorphism: on each open chart it is a finite product of continuous local absolute values. Thus \(J^1\) is a closed LCA group. Lemma 1.1 puts the diagonal \(\mathbb Q^\times\) inside it.

**Theorem 5.1.** Put \(U=\prod_p\mathbb Z_p^\times\), embedded in \(J^1\) with real component one. Multiplication gives a topological group isomorphism
\[
 \mathbb Q^\times_{\mathrm{discrete}}\times U\longrightarrow J^1.
 \tag{5.1}
\]
Consequently \(J^1/\mathbb Q^\times\simeq U\) is compact. With counting measure on \(\mathbb Q^\times\) and Haar probability on \(U\), its covolume is one and
\[
 \int_{J^1}f(x)\,dx
 =\int_U\sum_{r\in\mathbb Q^\times}f(ru)\,du.
 \tag{5.2}
\]

*Proof.* For \(x\in J^1\), set \(e_p=v_p(x_p)\), a finitely supported integer family. Let \(r_0=\prod_p p^{e_p}>0\). Then each \(x_p/r_0\) is a unit. The norm-one equation gives \(|x_\infty|=r_0\). Taking \(r=\operatorname{sign}(x_\infty)r_0\) makes the real component of \(x/r\) one. Thus \(x=ru\) for \(u\in U\). If a diagonal rational belongs to \(U\), all its valuations vanish, so it is \(\pm1\); its real component is one, forcing it to be one. This proves uniqueness and algebraic bijectivity.

The subgroup \(U\) is compact and open in \(J^1\). Compactness follows from compactness of each \(\mathbb Z_p^\times\), a closed subset of \(\mathbb Z_p\), and arbitrary-product compactness. For openness, intersect \(J^1\) with the open idèle set whose real component is positive and whose finite components are all units. The norm forces its real component to be exactly one, so that intersection is \(U\). Its cosets \(rU\) are therefore open and closed and have their transported compact product topologies. This proves the topology assertion in (5.1), including discreteness and closedness of the diagonal factor.

Transport counting measure times Haar probability through (5.1). It is Haar on \(J^1\); on the open compact subgroup \(U\) it has mass one. Compact supports meet only finitely many open cosets \(rU\). Finite summation on such supports proves (5.2). Its quotient measure is Haar probability on \(U\), establishing the covolume. ∎

**Worked reduction.** Suppose \(x_\infty=-12/5\), \(x_2=4\), \(x_3=3\), \(x_5=1/5\), and \(x_p=1\) elsewhere. The norm is \((12/5)(1/4)(1/3)5=1\). The rational factor in (5.1) is \(-12/5\). Division by it gives real component one and finite components \(-5/3,-5/4,-1/12\) at \(2,3,5\), respectively, all local units. At the remaining primes the component is \(-5/12\), also a unit. The entire tuple, not just its exceptional coordinates, changes.

### Heisenberg lattice volume

**Example 5.2.** In the Heisenberg group \(N\) of [Example 12.3 of the Haar lesson](haar-measure-on-locally-compact-groups.md#heisenberg-haar-volume), the subgroup
\(\Gamma=\{(m,n,k):m,n,k\in\mathbb Z\}\)
is a uniform lattice. For Lebesgue Haar measure and counting measure on \(\Gamma\), its covolume is one.

*Proof.* The group law and inverse formula preserve integer coordinates, so \(\Gamma\) is a subgroup. It is closed and discrete in \(\mathbb R^3\). Let \(D=[0,1)^3\). For \(g=(x,y,z)\), define
\[
\begin{aligned}
m&=\lfloor x\rfloor,& n&=\lfloor y\rfloor,\\
u&=x-m,& v&=y-n.
\end{aligned}
\]
\[
k=\lfloor z-un\rfloor,\qquad w=z-un-k.
\]
Then \(d=(u,v,w)\in D\), \(\gamma=(m,n,k)\in\Gamma\), and
\[
d\gamma=(u+m,v+n,w+k+un)=(x,y,z).
\]
The half-open conditions first force \(m,n\), then \(k\), so the factorization is unique. Thus \(D\) is a Borel right-coset transversal. Its closure is compact and its quotient image covers \(N/\Gamma\); this proves cocompactness. The group is sigma-compact and unimodular by the Haar example, so Theorem 1.2 gives
\[
\nu(N/\Gamma)=\mu(D)=\int_0^1\int_0^1\int_0^1 dz\,dy\,dx=1.
\]
There is also a left transversal with the same cube: in the factorization \(g=\gamma d\), replace the third-coordinate reduction by \(k=\lfloor z-mv\rfloor\) and \(w=z-mv-k\). The product has third coordinate \(k+w+mv\), proving existence and uniqueness in that direction too. This checks the side of translation explicitly. \(\square\)

The upper triangular model and its lattice appear in Bekka, de la Harpe and Valette; Fischer and Ruzhansky explain its relation to homogeneous groups. The floor reductions above supply the exact representatives and normalization without a general theorem about nilpotent lattices.

## 6. Exercises with complete solutions

**1 (easy): a nonunit normalization.** Replace counting measure on a discrete subgroup by \(b\) times counting measure. Keeping group Haar fixed, find the covolumes in Theorems 3.1, 4.1 and 5.1.

*Solution.* Averaging is multiplied by \(b\); Weil's formula therefore divides the quotient measure by \(b\). The covolumes become \(\pi/(6b),1/b,1/b\), respectively. Discreteness does not impose a preferred scale until counting measure is chosen.

**2 (medium): another additive reduction.** Take real component \(-1/5\), components \(3/8\) at \(2\), \(1/5\) at \(5\), and zero elsewhere. Find its representative in \(D\).

*Solution.* Subtract the principal parts \(q_0=3/8+1/5=23/40\). The real remainder is \(-31/40\); subtracting the integer \(-1\) moves it to \(9/40\). Hence the total rational subtraction is \(q=-17/40\). The finite remainders are \(4/5\) at \(2\), \(5/8\) at \(5\), and \(17/40\) elsewhere. All are integral at their respective primes. Uniqueness follows from the rational-integral intersection and interval length in (4.1).

**3 (medium): finite-index lattice volumes.** If \(\Gamma'\le\Gamma\) has finite index \(m\), prove that its covolume in \(G\), with counting measure, is \(m\pi/6\).

*Solution.* Choose representatives \(t_1,\ldots,t_m\) with \(\Gamma=\bigsqcup_i\Gamma't_i\). The sets \(t_i\mathcal D\) form a fundamental domain for the left \(\Gamma'\)-action on the same full-measure set: an equality of two representatives would contradict the uniqueness of the \(\Gamma\)-representative and then the distinct cosets. Left Haar invariance gives total volume \(m\mu(\mathcal D)\). The proof of Theorem 3.1 applies to their union, and inversion gives the right quotient too. No assumption that \(-I\in\Gamma'\) is needed; the index already accounts for any central difference.

**4 (hard): splitting all rational idèles.** Prove
\(J\simeq\mathbb R_{>0}\times\mathbb Q^\times_{\mathrm{discrete}}\times U\), where the first coordinate is the idèle norm. Identify \(J/\mathbb Q^\times\) and decide whether it is compact.

*Solution.* Let \(s(t)\) be the idèle with real component \(t>0\) and all finite components one. It is a continuous homomorphism with norm \(t\). Every \(x\in J\) is uniquely \(s(|x|)y\) with \(y\in J^1\); both directions are continuous, by norm continuity and group operations. Apply (5.1) to \(y\). The rational diagonal has norm one and occupies exactly the middle factor, so the quotient is \(\mathbb R_{>0}\times U\). It is not compact: its continuous norm image is the noncompact \(\mathbb R_{>0}\). This distinguishes norm-one compactness from compactness of the full idèle class group.

## References and relation to the programme

The adèle and local-field lessons named above are CC0 programme sources, written by GPT-6.1 Sol at Ultra and self-checked by their writing AI. Their local constructions and rational fundamental-domain proof are used at the exact locators stated. This lesson's reductions, volume calculations and exercises were independently authored; their self-check does not claim a fresh independent review of those providers.

J. S. Milne’s [*Modular Functions and Modular Forms*, version 1.31](https://www.jmilne.org/math/CourseNotes/MF.pdf), treats the same modular region and its boundary identifications. K. Conrad’s [*The character group of Q*](https://kconrad.math.uconn.edu/blurbs/gradnumthy/characterQ.pdf) gives the same half-open rational adèle representatives through a pole-part reduction. Here the integer/CRT reductions, unfolding, central factor and Haar normalizations are proved explicitly. B. Bekka, P. de la Harpe and A. Valette’s [*Kazhdan’s Property (T)*](https://perso.univ-rennes1.fr/bachir.bekka/KazhdanTotal.pdf), author preprint dated 23 February 2007, gives a complementary treatment of lattices, fundamental domains and the Heisenberg example. V. Fischer and M. Ruzhansky’s [*Quantization on Nilpotent Lie Groups*](https://biblio.ugent.be/publication/8585474), 2016, develops the Heisenberg group and its homogeneous scaling. General number-field adèles and class groups remain in the adèle course; Fourier duality and Poisson summation remain in the abelian harmonic-analysis course.
