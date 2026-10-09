# Couplings and supporting potentials

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In the limit of strong interaction, density functional theory leads to a transport problem: \(N\) electrons with a prescribed one-particle density \(\rho\) are placed so as to minimize their total Coulomb repulsion, and the joint law of their positions is a coupling of \(N\) copies of \(\rho\) [SGS, FGG]. The *Monge*, or co-motion, ansatz asserts that an optimal configuration is described by maps: the position of the first electron determines the positions of all the others. For two electrons, Cotar, Friesecke and Klüppelberg proved that an optimal map exists and is unique for every absolutely continuous density [CFK, Theorem 3.6]; on the line, Colombo, De Pascale and Di Marino constructed optimal maps for any number of particles; and Colombo and Di Marino proved that the smallest cost over maps equals the smallest cost over all couplings for every density without atoms [CDM]. Whether an optimal map must exist for three particles in space remained open [Friesecke, Section 3.2]. This course presents OpenAI's answer [OpenAI-CM]:

**Theorem** (OpenAI 2026). For every dimension \(d\ge2\) and every exponent \(s>0\) there is a probability density \(\rho\) on \(\mathbb R^d\), smooth with compact support and with a smooth square root, such that for the three-particle cost \(\sum_{i<j}|x_i-x_j|^{-s}\) and the measure \(\mu=\rho\,dx\):

1. the smallest cost over couplings of three copies of \(\mu\) is finite and attained;
2. no pair of measure-preserving Borel maps attains it;
3. pairs of measure-preserving Borel maps come arbitrarily close to it.

The Coulomb case is \(d=3\), \(s=1\). Parts 1 and 2 are Theorem 4.2 of [Two branches with a shared potential](two-branches-with-a-shared-potential.md), and part 3 is Theorem 4.1 of [Monge plans approach the minimum](monge-plans-approach-the-minimum.md).

The mechanism goes back to Gerolin, Kausamo and Rajala, who used it for the repulsive harmonic cost \(-\sum_{i<j}|x_i-x_j|^2\) [GKR]. A *supporting potential* forces every optimal coupling onto two prescribed families of triples (Section 2), and an imbalance of masses prevents a map from choosing between the families (Section 3). This lesson proves these two abstract steps; the next lesson builds the potential and the density for the Riesz costs.

## 1. Couplings and maps

Let \(\mu\) be a Borel probability measure on \(\mathbb R^d\). A *coupling* of three copies of \(\mu\) is a Borel probability measure \(\pi\) on \((\mathbb R^d)^3\) whose three coordinate projections all have law \(\mu\); write \(\Pi(\mu)\) for the set of couplings. For a Borel map \(T\colon\mathbb R^d\to\mathbb R^m\), the *image measure* is \(T_\#\mu(A)=\mu(T^{-1}(A))\), and \(\int f\,d(T_\#\mu)=\int f\circ T\,d\mu\) for every Borel \(f\ge0\). We say that \(T\colon\mathbb R^d\to\mathbb R^d\) *preserves* \(\mu\) if \(T_\#\mu=\mu\).

Let \(c\colon(\mathbb R^d)^3\to[0,\infty]\) be Borel. The *Kantorovich value* and the *Monge value* are
\[
\mathcal E_c(\mu)=\inf_{\pi\in\Pi(\mu)}\int c\,d\pi,\qquad \mathcal M_c(\mu)=\inf_{T_2,T_3}\int c\bigl(x,T_2(x),T_3(x)\bigr)\,d\mu(x),
\]
the second infimum running over pairs of Borel maps \(T_2,T_3\) that preserve \(\mu\). The coupling \((\mathrm{id},T_2,T_3)_\#\mu\) has the three marginals \(\mu\), \(T_{2\#}\mu=\mu\) and \(T_{3\#}\mu=\mu\), and its cost is \(\int c(x,T_2(x),T_3(x))\,d\mu(x)\). Hence
\[
\mathcal M_c(\mu)\ge\mathcal E_c(\mu).\tag{1.1}
\]
A coupling of the form \((\mathrm{id},T_2,T_3)_\#\mu\) is a *Monge plan*, and a Monge plan attaining \(\mathcal E_c(\mu)\) is a *Monge optimizer*.

For \(d\ge1\) and \(s>0\), the *Riesz cost* is
\[
c_s(x_1,x_2,x_3)=|x_1-x_2|^{-s}+|x_1-x_3|^{-s}+|x_2-x_3|^{-s},
\]
with the value \(+\infty\) when two points coincide; \(|\cdot|\) is the Euclidean norm. It is lower semicontinuous, hence Borel, and symmetric under permutations of the three points. The *Coulomb cost* is \(c_1\) on \((\mathbb R^3)^3\).

## 2. Supporting potentials

**Proposition 2.1.** Let \(c\colon(\mathbb R^d)^3\to[0,\infty]\) be Borel, let \(U\subseteq\mathbb R^d\) be a Borel set with \(\mu(U)=1\), and let \(u\colon U\to\mathbb R\) be a bounded Borel function with
\[
c(x_1,x_2,x_3)\ge u(x_1)+u(x_2)+u(x_3)\qquad\text{for all }(x_1,x_2,x_3)\in U^3 .\tag{2.1}
\]
Let \(\Gamma\subseteq U^3\) be the set where (2.1) is an equality.

1. Every \(\pi\in\Pi(\mu)\) satisfies \(\pi(U^3)=1\) and \(\int c\,d\pi\ge3\int_Uu\,d\mu\).
2. If some \(\pi_0\in\Pi(\mu)\) satisfies \(\pi_0(\Gamma)=1\), then \(\mathcal E_c(\mu)=3\int_Uu\,d\mu\) is finite, \(\pi_0\) attains it, and every \(\pi\in\Pi(\mu)\) that attains it satisfies \(\pi(\Gamma)=1\).

**Proof.** 1. The complement of \(U^3\) is covered by the three sets \(\{x_i\notin U\}\), each of \(\pi\)-measure \(\mu(\mathbb R^d\setminus U)=0\). On \(U^3\), integrate (2.1); the function \(u(x_1)+u(x_2)+u(x_3)\) is bounded, and its integral is \(3\int_Uu\,d\mu\) because every marginal of \(\pi\) is \(\mu\).

2. On \(\Gamma\) the cost equals the bounded function \(\sum_iu(x_i)\), so \(\int c\,d\pi_0=3\int_Uu\,d\mu<\infty\), and part 1 shows that this is the smallest possible value. If \(\pi\) attains it, then \(c\) is finite \(\pi\)-almost everywhere, and the nonnegative function \(c-\sum_iu(x_i)\) on \(U^3\) has \(\pi\)-integral \(\mathcal E_c(\mu)-3\int_Uu\,d\mu=0\). So it vanishes \(\pi\)-almost everywhere, that is, \(\pi(\Gamma)=1\). \(\square\)

The function \(u\) is a *supporting potential*: it certifies optimality and confines every optimal coupling to the *contact set* \(\Gamma\). Only this elementary half of multi-marginal duality is needed.

## 3. A mass imbalance

A homeomorphism \(H\) from an open set \(B\subseteq\mathbb R^d\) onto an open set maps Borel sets to Borel sets: \(H(S)\) is the preimage of \(S\) under the continuous inverse \(H(B)\to B\).

**Lemma 3.1** (OpenAI, after Gerolin, Kausamo and Rajala). Let \(B\subseteq\mathbb R^d\) be open, let \(\nu\) be a Borel probability measure with \(\nu(B)=1\), and let \(H_1,\dots,H_4\) be homeomorphisms of \(B\) onto open sets such that \(B,H_1(B),\dots,H_4(B)\) are pairwise disjoint. Put
\[
\mu=\frac13\nu+\frac16\sum_{j=1}^4H_{j\#}\nu .\tag{3.1}
\]
There is no Borel map \(T\colon\mathbb R^d\to\mathbb R^d\) that preserves \(\mu\) and satisfies \(T(x)\in\{H_1(x),\dots,H_4(x)\}\) for \(\nu\)-almost every \(x\in B\).

**Proof.** Suppose \(T\) is such a map, and let \(S_j=\{x\in B:T(x)=H_j(x)\}\), a Borel set. Since \(H_{j\#}\nu\) is carried by \(H_j(B)\), which is disjoint from \(B\) and from the other images, and \(H_j\) is injective,
\[
\mu(S_j)=\tfrac13\nu(S_j),\qquad \mu\bigl(H_j(S_j)\bigr)=\tfrac16\nu\bigl(H_j^{-1}(H_j(S_j))\bigr)=\tfrac16\nu(S_j).
\]
Every point of \(S_j\) is mapped by \(T\) into \(H_j(S_j)\), so \(S_j\subseteq T^{-1}(H_j(S_j))\), and since \(T\) preserves \(\mu\),
\[
\tfrac13\nu(S_j)=\mu(S_j)\le\mu\bigl(T^{-1}(H_j(S_j))\bigr)=\mu\bigl(H_j(S_j)\bigr)=\tfrac16\nu(S_j).
\]
Hence \(\nu(S_j)=0\) for every \(j\). But the four sets \(S_j\) cover \(\nu\)-almost all of \(B\), and \(\nu(B)=1\), a contradiction. \(\square\)

The proof compares, for each branch separately, the mass that \(T\) sends into the branch with the mass that the branch can receive. It uses no regularity of \(T\) and no property of \(\nu\) beyond \(\nu(B)=1\); points from outside \(B\) that \(T\) sends into \(H_j(S_j)\) only make the inequality stronger. The factor \(2\) between the central weight \(\frac13\) and the branch weights \(\frac16\) is what breaks every selection; with equal weights a selection is possible (Exercise 5.2).

## 4. How the two steps combine

**Corollary 4.1.** Let \(c\) be a Borel cost, symmetric under permutations of its three arguments, and let \(\mu\), \(U\), \(u\), \(\Gamma\) be as in Proposition 2.1, with \(\mu\) of the form (3.1). Suppose that some coupling is carried by \(\Gamma\), and that whenever \(x\in B\) and \((x,y,z)\in\Gamma\), the point \(y\) belongs to \(\{H_1(x),\dots,H_4(x)\}\). Then \(\mathcal E_c(\mu)\) is finite and attained, but by no Monge plan.

**Proof.** By Proposition 2.1, \(\mathcal E_c(\mu)\) is finite and attained, and every optimal coupling is carried by \(\Gamma\). If \((\mathrm{id},T_2,T_3)_\#\mu\) were optimal, then \((x,T_2(x),T_3(x))\in\Gamma\) for \(\mu\)-almost every \(x\), hence for \(\nu\)-almost every \(x\in B\), because \(\mu\ge\frac13\nu\). So \(T_2(x)\in\{H_1(x),\dots,H_4(x)\}\) for \(\nu\)-almost every \(x\in B\), and \(T_2\) preserves \(\mu\), contradicting Lemma 3.1. \(\square\)

The next lesson constructs, for the Riesz cost \(c_s\) in every dimension \(d\ge2\), a ball \(B\), four branches \(H_j\), and a potential \(u\) on five small balls whose contact set consists exactly of the permutations of the triples \((x,H_1(x),H_2(x))\) and \((x,H_3(x),H_4(x))\) with \(x\in B\). The two families meet at the central point \(x\), which is why one potential can support both. They point in two different directions, which needs \(d\ge2\); on the line, Colombo, De Pascale and Di Marino showed that optimal maps exist for a class of repulsive costs that includes the Coulomb cost.

## 5. Exercises

**Exercise 5.1** (easy). Let \(c\) be symmetric. Show that averaging a coupling \(\pi\in\Pi(\mu)\) over the six permutations of the coordinates gives a coupling in \(\Pi(\mu)\) with the same cost. Why does this not produce a Monge optimizer from a Monge plan?

**Exercise 5.2** (easy). Let \(B\) and \(H\) be as in Lemma 3.1, with one branch only, and let \(\mu=\frac12\nu+\frac12H_\#\nu\). Show that the map \(T\) equal to \(H\) on \(B\), to \(H^{-1}\) on \(H(B)\) and to the identity elsewhere is Borel, preserves \(\mu\), and satisfies \(T(x)=H(x)\) on \(B\).

**Exercise 5.3** (medium). Show that in Proposition 2.1 the hypothesis that \(u\) is bounded can be replaced by \(\int_U|u|\,d\mu<\infty\).

**Exercise 5.4** (medium). A discrete model. On the five points \(0,1,2,3,4\) let \(\mu\) give mass \(\frac13\) to \(0\) and \(\frac16\) to each other point, and let \(\Gamma\) consist of the permutations of \((0,1,2)\) and \((0,3,4)\). Find a coupling of three copies of \(\mu\) carried by \(\Gamma\), and show that no map \(T\) with \(T(0)\in\{1,2,3,4\}\) preserves \(\mu\).

## 6. Solutions

**5.1.** Each coordinate of the averaged measure is an average of the coordinates of \(\pi\), all of law \(\mu\); the cost is unchanged because \(c\) is symmetric. The average of the six permutations of a Monge plan \((\mathrm{id},T_2,T_3)_\#\mu\) is in general not of the form \((\mathrm{id},T_2',T_3')_\#\mu\): given its first coordinate, the other two coordinates are random.

**5.2.** On the open sets \(B\) and \(H(B)\) the map \(T\) is continuous, and it is the identity on the Borel set outside them, so it is Borel. For a Borel set \(A\), \(\mu(T^{-1}(A))=\frac12\nu(T^{-1}(A)\cap B)+\frac12H_\#\nu(T^{-1}(A)\cap H(B))=\frac12\nu(H^{-1}(A))+\frac12\nu(A\cap B)=\frac12H_\#\nu(A)+\frac12\nu(A)=\mu(A)\).

**5.3.** In the proof, \(\sum_iu(x_i)\) is \(\pi\)-integrable with integral \(3\int_Uu\,d\mu\) because \(\int|u(x_i)|\,d\pi=\int_U|u|\,d\mu\) for each \(i\); boundedness was used only for this.

**5.4.** Take \(\pi_0\) uniform on the twelve permutations of \((0,1,2)\) and \((0,3,4)\). In each coordinate the point \(0\) has probability \(\frac4{12}=\frac13\), and each other point \(\frac2{12}=\frac16\). If \(T(0)=j\neq0\), then \(T_\#\mu(\{j\})\ge\mu(\{0\})=\frac13>\frac16=\mu(\{j\})\).

## References

- [OpenAI-CM] OpenAI, *A counterexample to the Monge ansatz for the three-marginal Coulomb cost*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/A-counterexample-to-the-Monge-ansatz-for-the-three-marginal-Coulomb-cost-September-25-2026
- [SGS] M. Seidl, P. Gori-Giorgi and A. Savin, *Strictly correlated electrons in density-functional theory: a general formulation with applications to spherical densities*, Physical Review A 75 (2007), 042511. https://arxiv.org/abs/cond-mat/0701025
- [FGG] G. Friesecke, A. Gerolin and P. Gori-Giorgi, *The strong-interaction limit of density functional theory*, in: Density Functional Theory, Springer, 2023, 183–266. https://arxiv.org/abs/2202.09760
- [CFK] C. Cotar, G. Friesecke and C. Klüppelberg, *Density functional theory and optimal transportation with Coulomb cost*, Communications on Pure and Applied Mathematics 66 (2013), 548–599. https://arxiv.org/abs/1104.0603
- [CDM] M. Colombo and S. Di Marino, *Equality between Monge and Kantorovich multimarginal problems with Coulomb cost*, Annali di Matematica Pura ed Applicata 194 (2015), 307–320; author's version. https://cvgmt.sns.it/paper/2127/
- [GKR] A. Gerolin, A. Kausamo and T. Rajala, *Non-existence of optimal transport maps for the multi-marginal repulsive harmonic cost*, SIAM Journal on Mathematical Analysis 51 (2019), 2359–2371. https://arxiv.org/abs/1805.00417
- [Friesecke] G. Friesecke, *Mass splitting in the time-discrete generalized Euler equations and non-Monge solutions in multi-marginal optimal transport*, 2026. https://arxiv.org/abs/2601.02616
