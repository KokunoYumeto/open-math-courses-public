# Energy, density and the linear programming bound

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Place infinitely many points in the plane, on average one per unit of area, and let every two of them repel each other with a force that depends on their distance. Which arrangement has the least energy per point? For a wide class of repulsions the answer was conjectured by H. Cohn and A. Kumar to be the same [Cohn–Kumar]: the triangular lattice, in which every point has six nearest neighbours at the corners of a regular hexagon. In September 2026 OpenAI released a proof [OpenAI-T]. This lesson sets up the problem and proves the mechanism that turns it into a question of Fourier analysis.

- The energy \(E_g(\mathcal C)\) of a point configuration \(\mathcal C\) of density one, for an interaction \(g\) of the squared distance, and its value for a lattice (Section 1).
- The *linear programming bound* (Theorem 3.1): if a function \(f\) lies below the interaction and has a nonnegative Fourier transform, then every configuration of density one has energy at least \(\widehat f(0)-f(0)\). No periodicity or separation of the points is assumed.
- The bound can never exceed the energy of a lattice, and it equals the energy of the triangular lattice exactly if \(f\) touches the interaction at the lattice points and \(\widehat f\) vanishes at the dual lattice points (Proposition 4.1). Such a function is a *sharp pair*; if one exists for the Gaussian interaction \(e^{-\pi\alpha t}\), the triangular lattice has the least energy for it (Theorem 4.2).

The existence of sharp pairs for all Gaussians is the main work of [OpenAI-T]; it is not proved in this lesson. The bound of Theorem 3.1 goes back to [Cohn–Kumar] for periodic configurations; the form for arbitrary configurations of a given density is due to H. Cohn and M. de Courcy-Ireland [Cohn-de Courcy-Ireland]. The presentation follows [OpenAI-T, Sections 1 and 6].

The lesson uses Lebesgue integration in the plane (core course [Measure and Integration (D10)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)) and two theorems of the course on harmonic analysis on locally compact abelian groups: Fourier inversion and the Poisson summation formula for a lattice.

## 1. Configurations and their energy

A *configuration* is a subset \(\mathcal C\) of \(\mathbb R^2\) that is *locally finite*: every bounded set contains finitely many of its points. Let \(B_R\) be the closed disk of radius \(R\) around the origin, \(\mathcal C_R=\mathcal C\cap B_R\) and \(N_R=\#\mathcal C_R\). The configuration has *density one* if
\[
\frac{N_R}{\pi R^2}\longrightarrow1\qquad(R\to\infty).
\]
Then \(N_R>0\) for all large \(R\), and \(N_R\to\infty\).

An *interaction* is a function \(g\colon(0,\infty)\to[0,\infty]\). The *energy* of a configuration \(\mathcal C\) of density one is
\[
E_g(\mathcal C)=\liminf_{R\to\infty}\frac1{N_R}\sum_{\substack{x,y\in\mathcal C_R\\x\ne y}}g(|x-y|^2).
\]
The sum is over ordered pairs, so every pair of points is counted twice. The energy is an element of \([0,\infty]\). The argument of \(g\) is the squared distance; a Gaussian repulsion is \(g(t)=e^{-\pi\alpha t}\) with \(\alpha>0\), and an inverse power law is \(g(t)=t^{-s/2}\).

A *lattice* is a set \(\Lambda=M\mathbb Z^2\) with an invertible real matrix \(M\); its *covolume* is \(|\det M|\). Let \(b=\sqrt3/2\). The *triangular lattice* of covolume one is
\[
A=b^{-1/2}\{j(1,0)+k(\tfrac12,b)\mid j,k\in\mathbb Z\}.
\]
Its matrix has determinant \(b^{-1}\cdot b=1\).

**Lemma 1.1.** Let \(\Lambda\) be a lattice of covolume one. Then \(\Lambda\) has density one, and for every interaction \(g\)
\[
E_g(\Lambda)=\sum_{a\in\Lambda\setminus\{0\}}g(|a|^2).
\]

**Proof.** Let \(P=M[0,1)^2\). The translates \(a+P\), \(a\in\Lambda\), are pairwise disjoint, cover the plane and have area one. Let \(\rho\) be the largest distance of a point of the closure of \(P\) from the origin. For \(R>\rho\), the union of the cells \(a+P\) with \(a\in\Lambda\cap B_R\) lies in \(B_{R+\rho}\) and contains \(B_{R-\rho}\): a point \(z\) of \(B_{R-\rho}\) lies in a cell \(a+P\), and then \(|a|\le|z|+\rho\le R\). The area of the union is \(N_R\). So
\[
\pi(R-\rho)^2\le N_R\le\pi(R+\rho)^2 ,
\]
and \(\Lambda\) has density one.

*Upper bound.* For \(x\in\Lambda_R\) the differences \(y-x\), \(y\in\Lambda_R\), \(y\ne x\), are distinct elements of \(\Lambda\setminus\{0\}\). So the inner sum over \(y\) is at most \(L=\sum_{a\ne0}g(|a|^2)\), and the average over \(x\) is at most \(L\).

*Lower bound.* Let \(S\) be a finite subset of \(\Lambda\setminus\{0\}\) and \(\sigma\) the largest length of its elements. For \(x\in\Lambda_{R-\sigma}\) all points \(x+a\), \(a\in S\), lie in \(\Lambda_R\). So the double sum is at least \(N_{R-\sigma}\sum_{a\in S}g(|a|^2)\). Since \(N_{R-\sigma}/N_R\to1\), we get \(E_g(\Lambda)\ge\sum_{a\in S}g(|a|^2)\) for every finite \(S\), hence \(E_g(\Lambda)\ge L\). This also covers \(L=\infty\). \(\blacksquare\)

The question is whether \(E_g(\mathcal C)\ge E_g(A)\) for every configuration \(\mathcal C\) of density one. A configuration may contain points that are arbitrarily close together, and the numbers of its points in unit squares may be unbounded; only the counts \(N_R\) in the disks around the origin are controlled.

## 2. Fourier transforms and a positive form

For an integrable function \(f\) on \(\mathbb R^2\) let
\[
\widehat f(\xi)=\int_{\mathbb R^2}f(x)\,e^{-2\pi ix\cdot\xi}\,dx .
\]
We call a function \(f\colon\mathbb R^2\to\mathbb R\) *admissible* if it is continuous and even, \(f(-x)=f(x)\), and there are \(C,\delta>0\) with
\[
|f(x)|+|\widehat f(x)|\le C(1+|x|)^{-2-\delta}
\]
for all \(x\in\mathbb R^2\). The function \((1+|x|)^{-2-\delta}\) is integrable over the plane ([The Poisson summation formula](course:HA-LCA/src/the-poisson-summation-formula), Lemma 2.0), so \(f\) and \(\widehat f\) are integrable. Since \(f\) is real and even, \(\widehat f\) is real and even. Rapidly decreasing smooth functions, in particular the Gaussians \(e^{-\pi\alpha|x|^2}\), are admissible; this is not needed below.

**Lemma 2.1.** Let \(f\) be admissible.

1. For every \(x\in\mathbb R^2\),
\[
f(x)=\int_{\mathbb R^2}\widehat f(\xi)\,e^{2\pi ix\cdot\xi}\,d\xi .
\]
2. Let \(\mu,\nu\) be finite positive Borel measures on \(\mathbb R^2\), and \(\widehat\mu(\xi)=\int e^{-2\pi ix\cdot\xi}\,d\mu(x)\). Let \(Q(\mu,\nu)\) be the integral of \(f(x-y)\) with respect to the product measure \(d\mu(x)\,d\nu(y)\). Then
\[
Q(\mu,\nu)=\int\widehat f\;\overline{\widehat\mu}\;\widehat\nu\,d\xi .
\]
3. If \(\widehat f\ge0\), then \(Q(\mu,\mu)\ge0\), \(Q(\nu,\nu)\ge0\) and
\[
Q(\mu,\nu)^2\le Q(\mu,\mu)\,Q(\nu,\nu).
\]

**Proof.** (1) is the inversion theorem for integrable functions with integrable transform ([The Pontryagin duality theorem](course:HA-LCA/src/the-pontryagin-duality-theorem), Theorem 4.1) for the group \(\mathbb R^2\), whose characters are \(x\mapsto e^{2\pi ix\cdot\xi}\) and whose Lebesgue measure is its own dual measure ([The Fourier inversion theorem and the dual Haar measure](course:HA-LCA/src/the-fourier-inversion-theorem-and-the-dual-haar-measure), Proposition 3.2); the formula holds at every point because \(f\) is continuous.

(2) Insert (1) for \(f(x-y)\). The integrand \(\widehat f(\xi)e^{2\pi i(x-y)\cdot\xi}\) is integrable for the product of \(d\xi\), \(\mu\) and \(\nu\), because \(\widehat f\) is integrable and the measures are finite. By Fubini's theorem the integrations over \(x\) and \(y\) can be carried out first; they give \(\overline{\widehat\mu(\xi)}\) and \(\widehat\nu(\xi)\). The value \(Q(\mu,\nu)\) is real and symmetric in \(\mu,\nu\), because \(f\) is real and even.

(3) By (2), \(Q(\mu,\mu)=\int\widehat f\,|\widehat\mu|^2\ge0\). For real \(t\),
\[
\begin{aligned}
0&\le\int\widehat f\,|\widehat\mu+t\widehat\nu|^2\,d\xi\\
&=Q(\mu,\mu)+2tQ(\mu,\nu)+t^2Q(\nu,\nu).
\end{aligned}
\]
A real quadratic polynomial in \(t\) without negative values has discriminant at most zero. \(\blacksquare\)

## 3. The linear programming bound

**Theorem 3.1.** Let \(f\) be an admissible function with \(\widehat f\ge0\). For every configuration \(\mathcal C\) of density one,
\[
\begin{gathered}
\liminf_{R\to\infty}\frac1{N_R}\sum_{\substack{x,y\in\mathcal C_R\\x\ne y}}f(x-y)\\
\ge\ \widehat f(0)-f(0).
\end{gathered}
\]
Consequently, if \(g\) is an interaction with \(g(|z|^2)\ge f(z)\) for all \(z\ne0\), then
\[
E_g(\mathcal C)\ge\widehat f(0)-f(0).
\]

**Proof.** Let \(a=\widehat f(0)=\int f\); it is \(\ge0\). Let \(\mu_R\) be the sum of the unit point masses at the points of \(\mathcal C_R\). Then
\[
Q(\mu_R,\mu_R)=N_Rf(0)+\sum_{\substack{x,y\in\mathcal C_R\\x\ne y}}f(x-y),
\]
so the assertion is \(\liminf_RQ(\mu_R,\mu_R)/N_R\ge a\). If \(a=0\), this holds because \(Q(\mu_R,\mu_R)\ge0\). Let \(a>0\).

Fix \(\varepsilon>0\). Let \(\nu_R\) be Lebesgue measure on the disk \(B'=B_{(1+\varepsilon)R}\), of area \(V_R=\pi(1+\varepsilon)^2R^2\).

*The mixed term.* For \(x\in\mathcal C_R\),
\[
\int_{B'}f(x-y)\,dy=\int_{x-B'}f(z)\,dz ,
\]
and the set \(x-B'\) contains \(B_{\varepsilon R}\), because \(|x|\le R\). So this integral differs from \(a=\int f\) by at most
\[
\eta(R)=\int_{|z|>\varepsilon R}|f(z)|\,dz ,
\]
which tends to \(0\) as \(R\to\infty\), since \(f\) is integrable. Summing over \(x\in\mathcal C_R\):
\[
|Q(\mu_R,\nu_R)-N_Ra|\le N_R\,\eta(R).
\]
The bound does not depend on where the points of \(\mathcal C_R\) lie.

*The term of the disk.* By the substitution \(z=x-y\),
\[
\frac{Q(\nu_R,\nu_R)}{V_R}=\int f(z)\,\frac{|B'\cap(B'+z)|}{V_R}\,dz ,
\]
where \(|\cdot|\) is the area. The quotient lies between \(0\) and \(1\). For fixed \(z\) and \((1+\varepsilon)R>|z|\) the set \(B'\cap(B'+z)\) contains the disk of radius \((1+\varepsilon)R-|z|\) around \(z/2\), so the quotient tends to \(1\). By dominated convergence, \(Q(\nu_R,\nu_R)/V_R\to a\).

*Conclusion.* For large \(R\) we have \(\eta(R)<a\) and \(Q(\nu_R,\nu_R)>0\). By Lemma 2.1(3),
\[
\begin{aligned}
\frac{Q(\mu_R,\mu_R)}{N_R}&\ge\frac{Q(\mu_R,\nu_R)^2}{N_R\,Q(\nu_R,\nu_R)}\\
&\ge\frac{N_R}{V_R}\cdot\frac{(a-\eta(R))^2}{Q(\nu_R,\nu_R)/V_R}.
\end{aligned}
\]
As \(R\to\infty\), \(N_R/V_R\to(1+\varepsilon)^{-2}\) by the density, and the second factor tends to \(a^2/a=a\). So \(\liminf_RQ(\mu_R,\mu_R)/N_R\ge a/(1+\varepsilon)^2\) for every \(\varepsilon>0\), hence \(\ge a\).

The statement on \(g\) follows by comparing the finite sums term by term. \(\blacksquare\)

The name comes from the fact that the conditions on \(f\), namely \(f\le g\) and \(\widehat f\ge0\), are linear inequalities, and the bound \(\widehat f(0)-f(0)\) is a linear function of \(f\); finding the best \(f\) is a linear programme in infinitely many variables.

## 4. When the bound is sharp

The *dual lattice* of a lattice \(\Lambda=M\mathbb Z^2\) is the set \(\Lambda^*\) of all \(w\in\mathbb R^2\) with \(w\cdot a\in\mathbb Z\) for all \(a\in\Lambda\). It is the lattice \(M^{-T}\mathbb Z^2\), where \(M^{-T}\) is the inverse of the transpose: \(w\cdot Mk\in\mathbb Z\) for all \(k\in\mathbb Z^2\) means \(M^Tw\in\mathbb Z^2\).

**Proposition 4.1.** Let \(\Lambda\) be a lattice of covolume one, \(g\) an interaction, and \(f\) an admissible function with \(\widehat f\ge0\) and \(f(z)\le g(|z|^2)\) for \(z\ne0\). Then
\[
\widehat f(0)-f(0)\le\sum_{a\in\Lambda\setminus\{0\}}g(|a|^2)=E_g(\Lambda).
\]
If the right side is finite, equality holds exactly if
\[
\begin{gathered}
f(a)=g(|a|^2)\quad(a\in\Lambda\setminus\{0\}),\\
\widehat f(w)=0\quad(w\in\Lambda^*\setminus\{0\}).
\end{gathered}
\]

**Proof.** By the Poisson summation formula for the lattice \(\Lambda\) of covolume one ([The Poisson summation formula](course:HA-LCA/src/the-poisson-summation-formula), Corollary 2.2, at the point \(0\)), both series converge absolutely and
\[
\sum_{a\in\Lambda}f(a)=\sum_{w\in\Lambda^*}\widehat f(w).
\]
The right side is at least \(\widehat f(0)\), with equality exactly if \(\widehat f\) vanishes on \(\Lambda^*\setminus\{0\}\). The left side is at most \(f(0)+\sum_{a\ne0}g(|a|^2)\), with equality, when this sum is finite, exactly if \(f(a)=g(|a|^2)\) for all \(a\ne0\). \(\blacksquare\)

So the linear programming bound can prove at most that a lattice is optimal, and for a given lattice it does so only through a function \(f\) with all these contacts.

For \(\alpha>0\) let \(G_\alpha(x)=e^{-\pi\alpha|x|^2}\). A *sharp pair* for \(\alpha\) is an admissible function \(f\) such that
\[
\begin{gathered}
f\le G_\alpha,\qquad\widehat f\ge0,\\
f(a)=G_\alpha(a)\quad(a\in A\setminus\{0\}),\\
\widehat f(w)=0\quad(w\in A^*\setminus\{0\}).
\end{gathered}
\]

**Theorem 4.2.** Let \(\alpha>0\), and suppose there is a sharp pair for \(\alpha\). Then every configuration \(\mathcal C\) of density one satisfies
\[
E_g(\mathcal C)\ \ge\ \sum_{a\in A\setminus\{0\}}e^{-\pi\alpha|a|^2}=E_g(A)
\]
for the interaction \(g(t)=e^{-\pi\alpha t}\).

**Proof.** Let \(f\) be a sharp pair. By Theorem 3.1, \(E_g(\mathcal C)\ge\widehat f(0)-f(0)\). By Proposition 4.1 for \(\Lambda=A\), whose energy is finite, \(\widehat f(0)-f(0)=E_g(A)\). \(\blacksquare\)

*What is known.* [OpenAI-T] constructs, for every \(\alpha>0\), a sharp pair that is a rapidly decreasing radial function (its Theorem on normalized pairs and its lemma on Gaussian duality). The construction is long, and parts of it are verified by exact computer calculations. With it, Theorem 4.2 gives the optimality of the triangular lattice for every Gaussian interaction. In this lesson and the next the existence statement is a hypothesis. The later lessons of the course prove it; the last step is Theorem 4.1 of [The tail and the theorem](the-tail-and-the-theorem.md).

*What the theorem does not say.* It gives the least value of the energy and does not describe all configurations that attain it. Removing one point from \(A\) does not change the energy (Exercise 5.3). This is pointed out in [OpenAI-T, Section 1], and for the formal version of the theorem in [Callens].

## 5. Exercises

**5.1.** Let \(\mathcal C\) be a configuration with \(N_R/(\pi R^2)\to\rho\) for some \(\rho>0\). Show that under the assumptions of Theorem 3.1 the lower limit is at least \(\rho\widehat f(0)-f(0)\).

**5.2.** Let \(f\) be admissible with \(\widehat f\ge0\), and \(\Lambda\) a lattice of covolume one. Show without Theorem 3.1 that \(\sum_{a\in\Lambda\setminus\{0\}}f(a)\ge\widehat f(0)-f(0)\).

**5.3.** Let \(g\) be an interaction with \(L=\sum_{a\in A\setminus\{0\}}g(|a|^2)<\infty\), and let \(\mathcal C=A\setminus\{0\}\). Show that \(\mathcal C\) has density one and \(E_g(\mathcal C)=E_g(A)\).

**5.4.** Let \(\mathcal C\) be a configuration of density one. Show that every translate \(c+\mathcal C\), \(c\in\mathbb R^2\), has density one, and that the energy is not changed by a rotation of the configuration about the origin.

## 6. Solutions

**5.1.** In the proof only the limit of \(N_R/V_R\) changes: it is \(\rho(1+\varepsilon)^{-2}\). So \(\liminf Q(\mu_R,\mu_R)/N_R\ge\rho a\).

**5.2.** By Poisson summation, \(f(0)+\sum_{a\ne0}f(a)=\sum_{w\in\Lambda^*}\widehat f(w)\ge\widehat f(0)\).

**5.3.** The counts change by one, \(N_R(\mathcal C)=N_R(A)-1\), so the density is one. The double sum for \(\mathcal C_R\) is the double sum for \(A_R\) minus the terms with \(x=0\) or \(y=0\); these are at most \(2L\) in total. So the two double sums differ by at most \(2L\), and after division by \(N_R\to\infty\) the lower limits agree.

**5.4.** The points of \(c+\mathcal C\) in \(B_R\) correspond to the points of \(\mathcal C\) in the disk of radius \(R\) around \(-c\). This disk contains \(B_{R-|c|}\) and lies in \(B_{R+|c|}\). So the count for \(c+\mathcal C\) lies between \(N_{R-|c|}\) and \(N_{R+|c|}\), and both are \(\pi R^2\) times a factor that tends to \(1\). A rotation about the origin maps \(B_R\) to itself and preserves distances; so \(N_R\) and all the sums are unchanged.

## References

- [OpenAI-T] OpenAI, *Universal optimality of the triangular lattice*, OpenAI Math Release preprint, 23 September 2026, Sections 1 and 6. https://github.com/openai/math/tree/main/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026
- [Cohn–Kumar] H. Cohn and A. Kumar, *Universally optimal distribution of points on spheres*, Journal of the American Mathematical Society 20 (2007), Section 9. https://arxiv.org/abs/math/0607446
- [Cohn-de Courcy-Ireland] H. Cohn and M. de Courcy-Ireland, *The Gaussian core model in high dimensions*, Duke Mathematical Journal 167 (2018), Proposition 2.2. https://arxiv.org/abs/1603.09684
- [Callens] X. Callens, *Planar universal optimality, tiered*, preprint, 11 October 2026. https://zenodo.org/records/23293429
