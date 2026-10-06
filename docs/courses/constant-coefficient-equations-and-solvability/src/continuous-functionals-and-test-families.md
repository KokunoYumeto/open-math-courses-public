# Continuous functionals, test families and compact limits

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Density, solvability and compactness arguments need functionals with the right bound and test families with controlled support. We derive those tools from normed Hahn–Banach, then prove the compact subsequence arguments that the Fourier and distributional lessons use.

Read [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html), Sections 5–6 and 14, for normed Hahn–Banach, complete-metric Baire and the Fréchet closed graph theorem. [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html), Sections 4–5 and 13.10, supplies compact exhaustion and smooth cutoffs.

Grubb provides background on distributions. The normed extension and locally convex tools used here are supplied by the linked internal foundation proofs. The seminorm, test-family and compactness arguments required here are proved below.

## From normed extension to seminorm bounds

**Proposition 1.1.** Let \(E\) be a real or complex vector space, let \(p\) be a seminorm, and let \(f:M\to\mathbb K\) be linear on a subspace with \(|f(v)|\le C p(v)\), \(C\ge0\). There is a linear extension \(F:E\to\mathbb K\) with the same bound. If \(p\) is continuous in a locally convex topology, \(F\) is continuous.

**Proof.** The kernel \(N=\{v:p(v)=0\}\) is a subspace by the seminorm inequalities. The quotient \(E/N\) has the norm

\[
 \|v+N\|=p(v).
 \tag{1}
\]

The expression is independent of representative: adding \(n\in N\) gives \(p(v+n)\le p(v)\), and adding \(-n\) gives the reverse inequality. Its zero set is exactly the zero coset, and the other norm axioms descend from the seminorm. The functional descends to the image of \(M\): if \(m-m'\in N\), the stated bound gives \(f(m)=f(m')\). That descended functional has norm at most \(C\). Apply the full normed-space theorem in [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) Section 5; no completeness is needed. Pull its extension back along \(E\to E/N\). This proves \(|F(v)|\le Cp(v)\), including \(C=0\) and the zero quotient. A continuous \(p\) and this bound prove continuity at zero, hence everywhere by linearity. \(\square\)

**Proposition 1.2.** If \(M\) is a closed linear subspace of a Hausdorff locally convex real or complex space \(E\), and \(x\notin M\), there is a continuous linear \(F\) with \(F|_M=0\) and \(F(x)=1\).

**Proof.** Choose a balanced convex open neighborhood \(V\) of zero such that \((x+V)\cap M=\varnothing\). Such a neighborhood is contained in a sufficiently small neighborhood supplied by closedness and local convexity; balance ensures \(V=-V\). Its gauge is

\[
 p(v)=\inf\{t>0:v\in tV\}.
 \tag{2}
\]

It is finite because \(V\) is absorbing: continuity of \(t\mapsto tv\) at zero puts small multiples of each \(v\) in \(V\). Convexity proves \(p(v+w)\le p(v)+p(w)\) by choosing any admissible positive \(a,b\), writing \((v+w)/(a+b)\) as a convex combination of \(v/a,w/b\), and taking infima. Balance gives invariance under unit scalars; rescaling the defining set gives \(p(cv)=|c|p(v)\). Thus it is a seminorm. Also \(V=\{p<1\}\): if \(p(v)<1\), an admissible \(t<1\) and balance put \(v\in V\); if \(v\in V\), openness and continuity of real scalar multiplication give \((1+\varepsilon)v\in V\) for some \(\varepsilon>0\), so \(p(v)<1\). Rescaling gives \(\{p<a\}=aV\) for every \(a>0\), proving continuity of the gauge.

No \(x-m\), \(m\in M\), is in \(V\), so \(p(x-m)\ge1\). On \(M+\mathbb Kx\) define \(f(m+cx)=c\); the representation is unique since \(x\notin M\). If \(c\ne0\), homogeneity gives

\[
\begin{gathered}
p(m+cx)=|c|p(x+m/c)\\
\ge |c|=|f(m+cx)|.
\end{gathered}
\tag{3}
\]

For \(c=0\) the same bound holds. Proposition 1.1 extends this functional with bound \(p\). It is continuous, vanishes on \(M\), and takes value one at \(x\). This proves precisely the closed-subspace separation used for density in [the global approximation lesson](approximation-and-global-support-solvability.md) and the polynomial approximation lesson; normability and metrizability of \(E\) are unnecessary. \(\square\)

**The range adapter for [the distributional solvability lesson](singular-supports-and-distribution-data.md).** The seminorm on \(\mathcal D(X)\oplus\ell^1\) is \(p(w,a)=C(q(w)+\|a\|_1)\). The estimate in that lesson kills the kernel of \(Tv=(P^tv,(v(\psi_j))_j)\), so \(Tv\mapsto f(v)\) is a well-defined functional bounded by \(p\). Proposition 1.1 supplies exactly the extension used there, with every original factor retained. For its \(\ell^1\) restriction, let \(c_j=F(0,e_j)\). Then \(|c_j|\le C\), finite sums give \(F(0,a)=\sum c_ja_j\) for finite-support \(a\), and truncation convergence in \(\ell^1\) gives that equality for every \(a\in\ell^1\). Conversely a bounded sequence defines such a functional by an absolutely convergent sum, with norm \(\sup_j|c_j|\), attained in the supremum sense by coordinate vectors. There is no conjugation in this complex-linear pairing.

## Fixed-support topology and countable tests

Fix an open \(X\subset\mathbb R^n\). For compact \(K\subset X\), \(\mathcal D_K(X)\) consists of smooth functions supported in \(K\), with

\[
\begin{gathered}
p_{K,N}(\phi)=\max_{|\alpha|\le N}\sup_{x\in X}
                         |\partial^\alpha\phi(x)|,\\
\quad N\ge0.
\end{gathered}
\tag{4}
\]

These are the actual complete Fréchet spaces proved in [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) Section 14.2; no boundary regularity of \(K\) is assumed.

**Proposition 2.1.** The test topology is the finest locally convex topology for which all inclusions \(\mathcal D_K(X)\to\mathcal D(X)\) are continuous. A seminorm \(q\) is continuous precisely when its restriction to each \(\mathcal D_K(X)\) is continuous. A linear map into a locally convex space is continuous precisely when every fixed-support restriction is continuous.

**Proof.** On the algebraic union \(\mathcal D(X)=\bigcup_{K\Subset X}\mathcal D_K(X)\), take the topology generated by all seminorms having these continuous restrictions. A family of seminorms gives a locally convex vector topology: finite intersections of seminorm balls are balanced and convex, the triangle inequality controls addition, and

\[
\begin{gathered}
q(av-a_0v_0)\le |a|q(v-v_0)\\
+|a-a_0|q(v_0)
\end{gathered}
\tag{5}
\]

controls scalar multiplication. The inclusions are continuous by construction. Any other locally convex topology with continuous inclusions has continuous gauges of its balanced convex open neighborhoods, by the gauge proof in Proposition 1.2. Each such gauge belongs to the defining family; those gauges generate that other topology. Hence the constructed topology is finest.

The forward seminorm criterion follows by composing with inclusions. The reverse follows because precisely those seminorms were placed in the defining family. For a linear map \(T\), apply this criterion to every continuous target seminorm composed with \(T\); target seminorm balls characterize continuity. Finally, the induced topology on \(\mathcal D_K\) equals (4). It is at most that topology because all restricted defining seminorms are continuous there. It is at least that topology because the global seminorms \(\phi\mapsto\max_{|\alpha|\le N}\sup_X|\partial^\alpha\phi|\) are finite on compact tests and continuous on every fixed-support space. Their restrictions are (4). \(\square\)

**Proposition 2.2.** Each \(\mathcal D_K(X)\) is separable. There is one countable set of tests dense in \(\mathcal D(X)\) with the preceding topology.

**Proof.** First prove the needed compact metric assertion. For nonempty compact \(K\), a countable dense set \(A=\{a_j\}\) can be chosen by taking one point from every rational-coordinate open box meeting \(K\). Those boxes form a countable basis; every relative neighborhood meets a chosen point. For \(C(K;\mathbb C)\), consider the following countable family: finite lists of \(a_j\)'s, a positive rational \(r\), and rational complex coefficients \(c_j\), restricted to lists for which the radius-\(r\) open balls cover \(K\), give

\[
 g(x)=\frac{\sum_{j=1}^J c_j(r-|x-a_j|)_+}
            {\sum_{j=1}^J (r-|x-a_j|)_+}.
 \tag{6}
\]

Its denominator is positive on \(K\), so \(g\) is continuous. Given continuous \(f\) and \(\varepsilon>0\), uniform continuity supplies a sufficiently small positive rational \(r\) with \(|f(x)-f(y)|<\varepsilon/2\) for \(|x-y|<r\). Compactness and density of \(A\) give a finite radius-\(r/2\) cover with centers in \(A\). Choose \(|c_j-f(a_j)|<\varepsilon/2\). At each \(x\), only centers within distance \(r\) have positive weight; the normalized weights in (6) sum to one. Therefore \(|g(x)-f(x)|<\varepsilon\). This proves separability. Real coefficients give the real case. The empty \(K\) gives the zero space.

Open balls centered at this countable family with positive rational radii form a countable basis for the supremum topology of \(C(K)\): approximate a point in an open ball by a family member closely enough, and choose a smaller rational-radius ball containing that point and lying in the original ball. A countable product of such spaces is second countable, since finite-coordinate basic conditions from countable lists form a countable list. The map

\[
 \phi\longmapsto(\partial^\alpha\phi|_K)_{\alpha\in\mathbb N^n}
                 \quad\hbox{into }\prod_{\alpha\in\mathbb N^n}C(K)
 \tag{7}
\]

is injective and induces exactly (4): derivatives vanish outside \(K\), and each finite derivative maximum is a finite-coordinate product condition. A subspace of a second-countable space is second countable by intersecting its basic open sets with that subspace. Choose one actual smooth function from each nonempty basic set in the image of (7); this is a countable dense set in \(\mathcal D_K\). This argument does not assert that the approximate functions (6) themselves are smooth or supported in \(K\).

For nonempty \(X\), choose compact \(K_j\subset\operatorname{int}K_{j+1}\) with interiors covering \(X\), using \(|x|\le j\) and \(\operatorname{dist}(x,\mathbb R^n\setminus X)\ge1/j\), omitting the distance condition when \(X=\mathbb R^n\). A compact subset of \(X\) lies in an interior \(K_j\) by its positive distance to the complement and bounded coordinate norm. Take the union of the countable dense sets for \(\mathcal D_{K_j}\). If an open test-space set contains \(\phi\), choose such a \(j\) containing its support. The inverse image of that open set in \(\mathcal D_{K_j}\) is an open neighborhood of \(\phi\), and therefore meets that fixed-support dense set. The union is dense in the LF topology. For empty \(X\), use \(\{0\}\); for \(n=0\), the nonempty space is a point and rational scalar tests suffice. \(\square\)

Thus the countable family \((\eta_a)\) used in [the distributional solvability lesson](singular-supports-and-distribution-data.md) Lemma 5.1 can be chosen once, with a fixed-support approximation available for each individual test. If \(\|v_j\|_\infty\le1\), the pairing estimate

\[
\begin{gathered}
|v_j(\phi-\eta)|\le |K|\,\|\phi-\eta\|_\infty
       \\
\quad\text{when }\phi,\eta\in\mathcal D_K(X)
\end{gathered}
\tag{8}
\]

has one fixed finite compact-volume factor. Pointwise convergence on the union of the dense sets therefore gives convergence on each test. An unrestricted LF approximation with wandering supports is not used in this estimate.

## Compact families and smooth limits

**Proposition 3.1.** Let \(K\) be a compact metric space, and let \(f_j:K\to\mathbb C\) be uniformly bounded and equicontinuous. Then some subsequence converges uniformly to a continuous function.

**Proof.** Choose a countable dense set as in Proposition 2.2; for a general compact metric space use finite radius-\(1/r\) covers and take their centers for all integers \(r\). At its first point, boundedness gives a convergent scalar subsequence; at its second point, refine that subsequence, and continue. The diagonal subsequence converges at every chosen point. Given \(\varepsilon>0\), equicontinuity supplies \(\delta>0\) with \(|f_j(x)-f_j(y)|<\varepsilon/3\) whenever \(d(x,y)<\delta\), for every \(j\). Finitely many radius-\(\delta\) balls centered in the chosen dense set cover \(K\). On their finitely many centers, two sufficiently late diagonal terms differ by less than \(\varepsilon/3\). At an arbitrary point, the two errors to one covering center plus that center difference total less than \(\varepsilon\). Thus the subsequence is uniformly Cauchy. Scalar completeness gives its pointwise limit; the same uniform Cauchy estimate gives uniform convergence. A three-term estimate with any one continuous term proves that the limit is continuous. Empty \(K\) is immediate. \(\square\)

In [the embedding and compactness lesson](local-regularity-and-compactness.md), the compact frequency sets are closed balls. The displayed uniform derivative bounds on a slightly larger ball give equicontinuity on each ball by the coordinate-segment fundamental theorem. Apply Proposition 3.1 to ball one, then ball two within the first subsequence, and continue. The diagonal subsequence converges uniformly on every fixed compact frequency set. This supplies exactly the subsequence used before the weighted-tail estimate, including \(p=\infty\).

**Proposition 3.2.** If smooth functions \(f_j\) on an open \(Y\subset\mathbb R^n\) have all derivatives uniformly bounded on every compact subset, a subsequence converges in \(C^\infty\) on compact subsets of \(Y\).

**Proof.** Choose the compact exhaustion from Proposition 2.2. On each compact \(K_r\), the positive margin inside \(K_{r+1}\) and the bound on the next derivatives give equicontinuity of every \(\partial^\alpha f_j|_{K_r}\). For nearby points their segment lies in that larger compact neighborhood; the derivative bound controls the difference. For pairs beyond that small distance, the uniform zeroth bound supplies a finite Lipschitz bound if needed. Apply Proposition 3.1 to the countable list of pairs \((r,\alpha)\), refining subsequences successively and taking the diagonal. Every derivative has a uniform limit on each \(K_r\), and limits agree on overlaps.

On a coordinate segment inside an interior \(K_r\), pass to the limit in

\[
\begin{gathered}
\partial^\alpha f_j(x+h e_i)-\partial^\alpha f_j(x)
       \\
=\int_0^h\partial^{\alpha+e_i}f_j(x+t e_i)\,dt.
\end{gathered}
\tag{9}
\]

The integration error is at most \(|h|\) times the uniform derivative error. Divide the limit identity by \(h\) and use continuity of the next limit to identify its derivative. Telescoping across the finitely many coordinate segments proves full differentiability from continuous coordinate partial derivatives, as in [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) Section 14.2 proof. Induct on derivative order. The common zeroth limit is smooth and all uniform limits are its actual derivatives. This proves convergence in the stated smooth topology. Empty \(Y\) is immediate, and finite-component families use finitely many additional indices. \(\square\)

For [the distributional solvability lesson](singular-supports-and-distribution-data.md) Lemma 4.1, closed graph gives the required bounds on every output derivative before 3.2 is invoked. This adapter neither assumes that arbitrary bounded distribution families are smoothly compact nor supplies the separate singular-support hull theorem.

## Exercises with complete solutions

**Exercise 1 (basic).** Let \(E=\mathcal D(X)\oplus\ell^1\), \(p(w,a)=q(w)+\|a\|_1\), and suppose \(f\) on the range of a linear \(T\) has \(|f(Tv)|\le Cp(Tv)\). Show that the extension bound survives a nontrivial kernel of both \(T\) and \(p\), and identify the \(\ell^1\) term.

**Solution 1.** If \(Tv=Tv'\), the estimate for their difference gives \(f(T(v-v'))=0\); the range functional is well defined. If a range vector belongs to \(\ker p\), its value is zero. It therefore descends to the image of the range in \(E/\ker p\), with norm at most \(C\). Normed Hahn–Banach and pullback give \(|F(w,a)|\le C(q(w)+\|a\|_1)\). The coefficients \(c_j=F(0,e_j)\) satisfy \(|c_j|\le C\); finite sums and their \(\ell^1\) limits give \(F(0,a)=\sum_jc_ja_j\). This is a complex-linear sum with every scalar coefficient retained.

**Exercise 2 (intermediate).** Why does Proposition 2.2 not identify every member of its countable \(C(K)\) approximating family with a compact smooth test? What conclusion nevertheless supplies the test family?

**Solution 2.** The positive-part distance functions in (6) need not be differentiable and their normalized sum has no prescribed support outside \(K\). They only prove that each \(C(K)\) factor is second countable. The derivative embedding (7) makes the image of the actual smooth test space a second-countable subspace. Choosing actual members of its nonempty basic sets supplies a countable dense set inside that image and hence inside \(\mathcal D_K\). The countable union over the compact exhaustion is dense in the LF topology by continuity of each inclusion. No nonsmooth approximant is used as a test.

**Exercise 3 (advanced).** A bounded smooth family has uniformly bounded derivatives on compact subsets of \(Y\). Explain why uniform convergence of selected functions alone would not prove \(C^\infty\) convergence, and give the missing step.

**Solution 3.** Uniform limits of smooth functions can fail to be differentiable; convergence of their values does not control derivative limits. Apply Proposition 3.1 simultaneously, by one countable diagonal choice, to every derivative and every compact exhaustion set. The resulting derivative limits are continuous. Passing through the segment integral (9) identifies each next limit as the actual coordinate derivative of the preceding one. Full differentiability and induction then identify all limits as derivatives of the zeroth limit. The selected subsequence thus converges in every original smooth seminorm.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Internal normed extension: [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html#section-5), Section 5, proves the real and complex norm-preserving Hahn–Banach theorem with its stated maximality assumption.
- Internal Fréchet foundations: [the original seminorms and complete metric](../prerequisites/banach-foundation-bridges.html#section-14-1), Section 14.1, and [fixed-support smooth completeness](../prerequisites/banach-foundation-bridges.html#section-14-2), Section 14.2.
- Internal cutoff construction: [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html#section-13-10), Section 13.10.
- The seminorm extension, closed-subspace separation, fixed-support test topology and compact-limit arguments are proved in this lesson, Propositions 1.1–1.2, 2.1–2.2 and 3.1–3.2.
