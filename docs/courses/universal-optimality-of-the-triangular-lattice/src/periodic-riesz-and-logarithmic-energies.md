# Periodic Riesz and logarithmic energies

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For the interaction \(|x|^{-s}\) with \(0<s\le2\), and for \(-\log|x|\), the energy of a lattice in the sense of this course is infinite or has no meaning: the sum over the lattice diverges. For such interactions one neutralizes the points by a uniform background of the opposite charge. For a configuration that is periodic this has a simple form: the interaction is replaced by the periodic function with mean zero that has the same singularity, and the energy per point is a finite number. This lesson defines this energy for \(0\le s<2\) and proves that the triangular lattice has the least energy among all periodic configurations of density one, whatever their period lattice is.

The proof writes the energy as an integral of Gaussian energies over all widths of the Gaussian, with a positive weight. For each width the theorem of the course applies.

- Periodic configurations and their Gaussian energies (Lemmas 1.1 and 1.2).
- The periodic heat kernel (Lemma 2.1).
- The periodic kernel of order \(s\), its Fourier coefficients and its singular part (Propositions 3.1 to 3.3).
- The energy as an integral over Gaussian energies (Theorem 4.1) and the comparison of two configurations (Corollary 4.2).
- The triangular lattice has the least energy (Theorem 5.1).

The lesson follows a part of [OpenAI-T, Section 8]; according to [OpenAI-T], the passage from Gaussians to these energies by the heat kernel is due to M. Petrache and S. Serfaty. It uses Theorem 4.2 of [The tail and the theorem](the-tail-and-the-theorem.md), the notions of [Energy, density and the linear programming bound](energy-density-and-the-linear-programming-bound.md), the Fourier transform of the Gaussian from [Shells and Gaussian duality](shells-and-gaussian-duality.md), and the Poisson summation formula for a lattice of the course on harmonic analysis on locally compact abelian groups.

## 1. Periodic configurations

A *periodic configuration of density one* is a set
\[
\mathcal C=\bigcup_{i=1}^N(a_i+L),
\]
where \(L\) is a lattice of covolume \(N\ge1\) and \(a_1,\dots,a_N\in\mathbb R^2\) are points no two of which differ by an element of \(L\). The pair of \(L\) and the points is a *representation* of \(\mathcal C\); a configuration has many representations, for example with \(2L\) and \(4N\) points. A lattice of covolume one is the case \(N=1\).

**Lemma 1.1.** A periodic configuration \(\mathcal C\) of density one is a configuration of density one. For every interaction \(g\),
\[
E_g(\mathcal C)=\frac1N\sum_{i=1}^N\ \sum_{y\in\mathcal C,\ y\ne a_i}g(|a_i-y|^2).
\]

**Proof.** By the proof of Lemma 1.1 of the lesson on the linear programming bound, applied to the lattice \(L\) with its cells of area \(N\), the number \(N^{(i)}_R\) of the points of \(a_i+L\) in the disk \(B_R\) lies between \(\pi(R-\rho)^2/N\) and \(\pi(R+\rho)^2/N\) for a fixed \(\rho\). So \(N^{(i)}_R/(\pi R^2)\to1/N\), the configuration has density one, and \(N^{(i)}_R/N_R\to1/N\).

For \(x\in a_i+L\) the sum \(S_i=\sum_{y\in\mathcal C,\,y\ne x}g(|x-y|^2)\) does not depend on \(x\), because \(\mathcal C\) is invariant under translations by \(L\). *Upper bound.* For \(x\in\mathcal C_R\) of the class \(a_i+L\), the sum over the \(y\in\mathcal C_R\), \(y\ne x\), is at most \(S_i\). So the average in the definition of the energy is at most \(\sum_i(N^{(i)}_R/N_R)S_i\), which tends to \(\tfrac1N\sum_iS_i\) if all \(S_i\) are finite; if one of them is infinite, the lower bound suffices. *Lower bound.* For every \(i\) let \(F_i\) be a finite set of nonzero vectors \(y-a_i\), \(y\in\mathcal C\), and \(\sigma\) the largest length of these vectors. For \(x\in(a_i+L)\cap B_{R-\sigma}\) all points \(x+f\), \(f\in F_i\), lie in \(\mathcal C_R\). So the double sum is at least \(\sum_iN^{(i)}_{R-\sigma}\sum_{f\in F_i}g(|f|^2)\). Divide by \(N_R\) and let \(R\to\infty\): the energy is at least \(\tfrac1N\sum_i\sum_{f\in F_i}g(|f|^2)\) for all finite sets \(F_i\), hence at least \(\tfrac1N\sum_iS_i\). \(\blacksquare\)

**The heat kernel.** For \(t>0\) let
\[
\Psi_t(x)=\frac1{4\pi t}\,e^{-|x|^2/(4t)}\qquad(x\in\mathbb R^2).
\]
Its integral over the plane is \(1\). For a lattice \(L\) let
\[
P_{t,L}(x)=\sum_{v\in L}\Psi_t(x-v),
\]
a function with the periods \(L\). For a periodic configuration with the representation \(L\), \(a_1,\dots,a_N\) let
\[
H_{\mathcal C}(t)=\frac1N\sum_{i,j=1}^NP_{t,L}(a_i-a_j)-\Psi_t(0).
\]
The subtracted term removes, for every point, its interaction with itself; its interactions with its own translates remain.

**Lemma 1.2.** Let \(g_t(u)=e^{-u/(4t)}\). For every periodic configuration \(\mathcal C\) of density one and every \(t>0\),
\[
H_{\mathcal C}(t)=\frac1{4\pi t}\,E_{g_t}(\mathcal C).
\]
So \(H_{\mathcal C}\) depends only on the set \(\mathcal C\), not on its representation. For the triangular lattice \(A\) of covolume one and every \(t>0\),
\[
H_{\mathcal C}(t)\ \ge\ H_A(t)=\sum_{a\in A\setminus\{0\}}\Psi_t(a).
\]

**Proof.** The points \(y\ne a_i\) of \(\mathcal C\) are the points \(a_j+v\) with \((j,v)\ne(i,0)\). So in Lemma 1.1, \(\tfrac1{4\pi t}S_i=\sum_jP_{t,L}(a_i-a_j)-\Psi_t(0)\), because \(\Psi_t\) is even and \(L=-L\). The mean over \(i\) is \(H_{\mathcal C}(t)\). The function \(g_t\) is completely monotone, so \(E_{g_t}(\mathcal C)\ge E_{g_t}(A)\) by Theorem 4.2 of the lesson on the tail. \(\blacksquare\)

## 2. The periodic heat kernel

Let \(L\) be a lattice of covolume \(N\), \(L^*\) its dual lattice, and \(\lambda_\xi=4\pi^2|\xi|^2\) for \(\xi\in L^*\). Let \(\lambda_1>0\) be the smallest of the numbers \(\lambda_\xi\) with \(\xi\ne0\).

**Lemma 2.1.**

1. For all \(t>0\) and \(x\in\mathbb R^2\),
\[
P_{t,L}(x)=\frac1N\sum_{\xi\in L^*}e^{-\lambda_\xi t}\,e^{2\pi i\xi\cdot x}.
\]
2. There is a number \(C\) with \(|P_{t,L}(x)-\tfrac1N|\le Ce^{-\lambda_1t}\) for all \(t\ge1\) and all \(x\).
3. For every \(\rho>0\) there is a number \(C_\rho\) such that for \(0<t\le1\) and all \(x\in\mathbb R^2\) the sum of \(\Psi_t(x-v)\) over the \(v\in L\) with \(|x-v|\ge\rho\) is at most
\[
\frac{C_\rho}t\,e^{-\rho^2/(8t)} .
\]
4. The integral of \(P_{t,L}\) over a cell of \(L\) is \(1\), and for \(\xi\in L^*\) the integral of \(P_{t,L}(x)e^{-2\pi i\xi\cdot x}\) over a cell is \(e^{-\lambda_\xi t}\).

**Proof.** (1) \(\Psi_t=\tfrac1{4\pi t}G_\beta\) with \(G_\beta(x)=e^{-\pi\beta|x|^2}\) and \(\beta=1/(4\pi t)\). By Lemma 3.1 of the lesson on shells and Gaussian duality its Fourier transform is \(\tfrac1{4\pi t}\beta^{-1}G_{1/\beta}(\xi)=e^{-4\pi^2t|\xi|^2}\). The Poisson summation formula for the lattice \(L\) of covolume \(N\) ([The Poisson summation formula](course:HA-LCA/src/the-poisson-summation-formula), Corollary 2.2) gives the claim.

(2) By (1), \(|P_{t,L}(x)-\tfrac1N|\le\tfrac1N\sum_{\xi\ne0}e^{-\lambda_\xi t}\). For \(t\ge1\), \(e^{-\lambda_\xi t}\le e^{-\lambda_1(t-1)}e^{-\lambda_\xi}\), and \(\sum_\xi e^{-\lambda_\xi}\) is finite.

(3) For \(|x-v|\ge\rho\) and \(t\le1\),
\[
e^{-|x-v|^2/(4t)}\le e^{-\rho^2/(8t)}\,e^{-|x-v|^2/8}.
\]
The sum \(\sum_{v\in L}e^{-|x-v|^2/8}\) is a continuous function of \(x\) with the periods \(L\) (Lemma 2.0 of the lesson on the Poisson summation formula), hence bounded.

(4) Let \(Q\) be a cell of \(L\); the plane is the disjoint union of the sets \(Q-v\), \(v\in L\). For \(\xi\in L^*\) the function \(e^{-2\pi i\xi\cdot x}\) has the periods \(L\). So the integral over \(Q\) of \(\sum_v\Psi_t(x-v)e^{-2\pi i\xi\cdot x}\) is the integral of \(\Psi_t(x)e^{-2\pi i\xi\cdot x}\) over the plane, which is \(e^{-\lambda_\xi t}\); for \(\xi=0\) it is \(1\). \(\blacksquare\)

## 3. The periodic kernel

Let \(0\le s<2\) and
\[
\sigma=1-\frac s2\in(0,1].
\]
Let \(\Gamma(z)=\int_0^\infty u^{z-1}e^{-u}\,du\) for \(z>0\); then \(\int_0^\infty t^{z-1}e^{-\lambda t}\,dt=\Gamma(z)\lambda^{-z}\) for \(\lambda>0\).

**Definition.** For a lattice \(L\) of covolume \(N\) and \(x\notin L\),
\[
\begin{aligned}
&K_{s,L}(x)\\
&\quad=\frac1{\Gamma(\sigma)}\int_0^\infty\Bigl(P_{t,L}(x)-\frac1N\Bigr)\,t^{\sigma-1}\,dt .
\end{aligned}
\]

**Proposition 3.1.** The integral converges absolutely. The function \(K_{s,L}\) has the periods \(L\), is even, and is continuous outside \(L\).

**Proof.** Let \(x\notin L\) and \(\rho>0\) the distance of \(x\) from \(L\). For \(t\ge1\) the integrand is at most \(Ce^{-\lambda_1t}t^{\sigma-1}\) by Lemma 2.1 (2). For \(t\le1\) it is at most \((C_\rho t^{-1}e^{-\rho^2/(8t)}+\tfrac1N)\,t^{\sigma-1}\) by Lemma 2.1 (3), and \(\sigma>0\). These bounds hold uniformly for the points at a distance of at least \(\rho\) from \(L\), which gives the continuity by dominated convergence. The symmetries are those of \(P_{t,L}\). \(\blacksquare\)

**Proposition 3.2.** The function \(K_{s,L}\) is integrable over a cell \(Q\) of \(L\), and for \(\xi\in L^*\)
\[
\int_QK_{s,L}(x)\,e^{-2\pi i\xi\cdot x}\,dx=\begin{cases}\lambda_\xi^{-\sigma},&\xi\ne0,\\0,&\xi=0.\end{cases}
\]

**Proof.** For \(t\le1\), \(|P_{t,L}-\tfrac1N|\le P_{t,L}+\tfrac1N\), whose integral over \(Q\) is \(2\) by Lemma 2.1 (4); for \(t\ge1\) use Lemma 2.1 (2). So the integral of \(|P_{t,L}(x)-\tfrac1N|\,t^{\sigma-1}\) over \(Q\times(0,\infty)\) is finite, and by Fubini's theorem the integration over \(x\) can be carried out first. By Lemma 2.1 (4) it gives \(e^{-\lambda_\xi t}\) for \(\xi\ne0\) and \(1-1=0\) for \(\xi=0\). Then \(\tfrac1{\Gamma(\sigma)}\int_0^\infty e^{-\lambda_\xi t}t^{\sigma-1}\,dt=\lambda_\xi^{-\sigma}\). \(\blacksquare\)

Since \(\lambda_\xi\) is the factor by which \(-\Delta\) multiplies \(e^{2\pi i\xi\cdot x}\), the proposition says that \(K_{s,L}\) is the periodic function with mean zero that the operator \((-\Delta)^\sigma\) sends to a unit point charge at the points of \(L\) minus the uniform charge \(1/N\). For \(s=0\) this is the equation \(-\Delta K=\delta-1/N\) of electrostatics in the plane.

**The singular part.** Let \(g_s(x)=|x|^{-s}\) for \(0<s<2\) and \(g_0(x)=-\log|x|\). Let \(q_0=2\pi\) and, for \(0<s<2\),
\[
q_s=\frac{2^{2-s}\,\pi\,\Gamma(1-s/2)}{\Gamma(s/2)} .
\]
Let \(P^*_{t,L}(x)=P_{t,L}(x)-\Psi_t(x)\) be the sum over the \(v\ne0\), and let \(e_0\) be the number
\[
e_0=\int_0^1\frac{e^{-u}-1}u\,du+\int_1^\infty\frac{e^{-u}}u\,du .
\]

**Proposition 3.3.** The limit
\[
r_{s,L}=\lim_{x\to0}\Bigl(K_{s,L}(x)-\frac{g_s(x)}{q_s}\Bigr)
\]
exists. For \(0<s<2\),
\[
r_{s,L}=\frac1{\Gamma(\sigma)}\int_0^\infty\Bigl(P^*_{t,L}(0)-\frac1N\Bigr)t^{\sigma-1}\,dt .
\]
For \(s=0\), with \(c_0=(\log4+e_0)/(4\pi)\),
\[
\begin{aligned}
r_{0,L}=c_0&+\int_0^1\Bigl(P^*_{t,L}(0)-\frac1N\Bigr)dt\\
&+\int_1^\infty\Bigl(P_{t,L}(0)-\frac1N\Bigr)dt .
\end{aligned}
\]

**Proof.** *The case \(0<s<2\).* With \(u=|x|^2/(4t)\),
\[
\begin{aligned}
&\int_0^\infty\Psi_t(x)\,t^{\sigma-1}\,dt\\
&\quad=\frac1{4\pi}\int_0^\infty t^{\sigma-2}e^{-|x|^2/(4t)}\,dt\\
&\quad=\frac1{4\pi}\Bigl(\frac{|x|^2}4\Bigr)^{\sigma-1}\int_0^\infty u^{-\sigma}e^{-u}\,du\\
&\quad=\frac{\Gamma(1-\sigma)}{4\pi}\,2^{s}\,|x|^{-s},
\end{aligned}
\]
since \(2\sigma-2=-s\). Divided by \(\Gamma(\sigma)\) this is \(|x|^{-s}/q_s\). So
\[
\begin{aligned}
&K_{s,L}(x)-\frac{g_s(x)}{q_s}\\
&\quad=\frac1{\Gamma(\sigma)}\int_0^\infty\Bigl(P^*_{t,L}(x)-\frac1N\Bigr)t^{\sigma-1}\,dt .
\end{aligned}
\]
Let \(\rho\) be half the smallest length of a nonzero element of \(L\), and \(|x|\le\rho\). For \(t\le1\), \(P^*_{t,L}(x)\le C_\rho t^{-1}e^{-\rho^2/(8t)}\) by Lemma 2.1 (3). For \(t\ge1\), \(|P^*_{t,L}(x)-\tfrac1N|\le Ce^{-\lambda_1t}+\tfrac1{4\pi t}\), and \(t^{\sigma-2}\) is integrable at infinity because \(\sigma<1\). By dominated convergence the integral tends to its value at \(x=0\).

*The case \(s=0\).* Here \(\sigma=1\). With the same substitution,
\[
\int_0^1\Psi_t(x)\,dt=\frac1{4\pi}\int_{|x|^2/4}^\infty\frac{e^{-u}}u\,du .
\]
For \(0<z<1\),
\[
\begin{aligned}
&\int_z^\infty\frac{e^{-u}}u\,du\\
&\quad=-\log z+\int_z^1\frac{e^{-u}-1}u\,du\\
&\qquad+\int_1^\infty\frac{e^{-u}}u\,du ,
\end{aligned}
\]
and the last two terms tend to \(e_0\) as \(z\to0\). So, as \(x\to0\),
\[
\begin{aligned}
\int_0^1\Psi_t(x)\,dt&=-\frac1{2\pi}\log|x|\\
&\quad+c_0+o(1).
\end{aligned}
\]
The rest of \(K_{0,L}(x)\) is the sum of \(\int_0^1(P^*_{t,L}(x)-\tfrac1N)\,dt\) and \(\int_1^\infty(P_{t,L}(x)-\tfrac1N)\,dt\), which tends to its value at \(x=0\) by the same bounds. \(\blacksquare\)

So \(q_sK_{s,L}(x)=g_s(x)+q_sr_{s,L}+o(1)\) at the origin: the function \(q_sK_{s,L}\) is the interaction \(g_s\), made periodic with the mean zero.

## 4. The energy

**Definition.** Let \(0\le s<2\), and let \(\mathcal C\) be a periodic configuration of density one with the representation \(L\), \(a_1,\dots,a_N\). Its *periodic energy of order \(s\)* is
\[
\begin{aligned}
&V_s(\mathcal C)\\
&\quad=q_s\Bigl[\frac1N\sum_{i\ne j}K_{s,L}(a_i-a_j)+r_{s,L}\Bigr].
\end{aligned}
\]

The first term is the energy per point of the interactions of the different points of a cell through the periodic kernel; it contains the interactions with all translates. The second term is the energy of a point with its own translates and with the background. The next theorem shows that the number does not depend on the representation.

**Theorem 4.1.** For \(0<s<2\),
\[
V_s(\mathcal C)=\frac{q_s}{\Gamma(\sigma)}\int_0^\infty\bigl(H_{\mathcal C}(t)-1\bigr)\,t^{-s/2}\,dt ,
\]
and for \(s=0\)
\[
\begin{aligned}
V_0(\mathcal C)&=q_0c_0+q_0\int_0^1\bigl(H_{\mathcal C}(t)-1\bigr)\,dt\\
&\quad+q_0\int_1^\infty\Bigl(H_{\mathcal C}(t)-1+\frac1{4\pi t}\Bigr)dt .
\end{aligned}
\]
The integrals converge absolutely. In particular \(V_s(\mathcal C)\) depends only on the set \(\mathcal C\).

**Proof.** Let \(0<s<2\). By the definition of \(K_{s,L}\) and Proposition 3.3, the bracket in the definition of \(V_s\) is \(\tfrac1{\Gamma(\sigma)}\int_0^\infty I(t)\,t^{\sigma-1}dt\) with
\[
\begin{aligned}
I(t)&=\frac1N\sum_{i\ne j}\Bigl(P_{t,L}(a_i-a_j)-\frac1N\Bigr)\\
&\quad+P_{t,L}(0)-\Psi_t(0)-\frac1N\\
&=\frac1N\sum_{i,j}P_{t,L}(a_i-a_j)-\Psi_t(0)\\
&\quad-\frac{N-1}N-\frac1N\\
&=H_{\mathcal C}(t)-1 .
\end{aligned}
\]
Here the \(N\) terms with \(i=j\) of the double sum are \(P_{t,L}(0)\) each, and there are \(N(N-1)\) pairs \(i\ne j\). Each of the finitely many integrals converges absolutely by Propositions 3.1 and 3.3. For \(s=0\) the same computation applies for \(t\le1\); for \(t>1\) the term \(r_{0,L}\) contributes \(P_{t,L}(0)-\tfrac1N\) in place of \(P^*_{t,L}(0)-\tfrac1N\), so \(I(t)=H_{\mathcal C}(t)-1+\Psi_t(0)\), and \(\Psi_t(0)=1/(4\pi t)\). By Lemma 1.2 the function \(H_{\mathcal C}\) depends only on \(\mathcal C\). \(\blacksquare\)

In the formula, \(H_{\mathcal C}(t)\) is the Gaussian energy of the points and \(-1\) is the background. As \(t\to\infty\), \(H_{\mathcal C}(t)=1-1/(4\pi t)\) up to an exponentially small term, by Lemma 2.1 (2).

**Corollary 4.2.** Let \(0\le s<2\), and let \(\mathcal C\), \(\mathcal D\) be periodic configurations of density one, with any period lattices, and \(\Delta(t)=H_{\mathcal C}(t)-H_{\mathcal D}(t)\). Then
\[
\begin{aligned}
&V_s(\mathcal C)-V_s(\mathcal D)\\
&\quad=\frac{q_s}{\Gamma(1-s/2)}\int_0^\infty\Delta(t)\,t^{-s/2}\,dt ,
\end{aligned}
\]
and the integral converges absolutely.

**Proof.** Subtract the formulas of Theorem 4.1; for \(s=0\) the terms \(q_0c_0\) and \(1/(4\pi t)\) cancel, and \(\Gamma(1)=1\). \(\blacksquare\)

## 5. The triangular lattice has the least energy

**Theorem 5.1.** Let \(0\le s<2\), and let \(A\) be the triangular lattice of covolume one. Every periodic configuration \(\mathcal C\) of density one in the plane satisfies
\[
V_s(\mathcal C)\ \ge\ V_s(A).
\]

**Proof.** By Corollary 4.2 with \(\mathcal D=A\), the difference is the integral of \(H_{\mathcal C}(t)-H_A(t)\) with the positive weight \(q_s\,t^{-s/2}/\Gamma(1-s/2)\). By Lemma 1.2 the integrand is not negative. \(\blacksquare\)

For example, for every \(n\ge1\): among all sets of \(n^2\) points on the torus \(\mathbb R^2/nA\), the \(n^2\) points of \(A\) have the least energy for the periodic kernel of order \(s\) of this torus. The theorem compares configurations with different period lattices as well. For the square lattice \(\mathbb Z^2\) the inequality is strict (Exercise 6.6).

**What is not in this lesson.** [OpenAI-T, Section 8] goes further. It defines energies through fields in the plane, or in a space with one more coordinate for \(s>0\): for \(N\) points on a torus an energy that it shows to be \(\kappa_sV_s\), with \(\kappa_0=2\pi\) and \(\kappa_s=4\pi\) for \(s>0\), and an energy \(W_s\) for configurations that need not be periodic. From an approximation of the infimum of \(W_s\) by periodic configurations it derives that \(A\) minimizes \(W_s\) among all configurations, and from theorems on the thermodynamic limit that the least energy per point of \(N\) points in a square with a uniform background tends to \(V_s(A)\). These steps use theorems of the literature that this course does not have: the theory of the renormalized energy of Petrache and Serfaty, the thermodynamic limits of M. Lewin, E. Lieb and R. Seiringer and of A. Lauritsen, and a minimum principle for degenerate elliptic equations of E. Fabes, C. Kenig and R. Serapioni. They are not proved in the course.

## 6. Exercises

**6.1.** Compute \(q_1\). What does Proposition 3.2 say for \(s=1\)?

**6.2.** Let \(\Lambda\) be a lattice of covolume one. Write \(H_\Lambda(t)\) and, for \(0<s<2\), \(V_s(\Lambda)\) as an integral.

**6.3.** Let \(\mathcal C=\mathbb Z^2\). Compute \(H_{\mathcal C}(t)\) from the representation with \(L=2\mathbb Z^2\) and the four points \((0,0),(1,0),(0,1),(1,1)\), and check that it is the same as from \(L=\mathbb Z^2\), \(N=1\).

**6.4.** Show that \(H_{\mathcal C}(t)\to0\) as \(t\to0\), and that \(H_{\mathcal C}(t)\to1\) as \(t\to\infty\).

**6.5.** Why does the proof of Theorem 5.1 need the theorem of the course for all Gaussians, and not only for one?

**6.6.** Show that \(V_s(\mathbb Z^2)>V_s(A)\) for \(0\le s<2\). Use that the shortest nonzero vectors of \(A\) have the squared length \(1/b=2/\sqrt3>1\).

## 7. Solutions

**6.1.** \(q_1=2\pi\,\Gamma(\tfrac12)/\Gamma(\tfrac12)=2\pi\), and \(\sigma=\tfrac12\). The periodic kernel \(K_{1,L}\) has the Fourier coefficients \(\lambda_\xi^{-1/2}=1/(2\pi|\xi|)\), and \(2\pi K_{1,L}(x)=|x|^{-1}+2\pi r_{1,L}+o(1)\): it is the Coulomb interaction of three-dimensional space between points of the plane, made periodic.

**6.2.** \(H_\Lambda(t)=\sum_{v\in\Lambda\setminus\{0\}}\Psi_t(v)\), and
\[
V_s(\Lambda)=\frac{q_s}{\Gamma(\sigma)}\int_0^\infty\bigl(H_\Lambda(t)-1\bigr)\,t^{-s/2}\,dt .
\]

**6.3.** For \(N=4\): \(\tfrac14\sum_{i,j}P_{t,2\mathbb Z^2}(a_i-a_j)\). For a fixed \(i\) the differences \(a_i-a_j\) run through the four classes of \(\mathbb Z^2\) modulo \(2\mathbb Z^2\), so \(\sum_jP_{t,2\mathbb Z^2}(a_i-a_j)=P_{t,\mathbb Z^2}(0)\). The mean over \(i\) is \(P_{t,\mathbb Z^2}(0)\), and \(H_{\mathcal C}(t)=P_{t,\mathbb Z^2}(0)-\Psi_t(0)\), as for \(N=1\).

**6.4.** \(H_{\mathcal C}(t)\) is a mean of sums of \(\Psi_t\) over the nonzero differences of points of \(\mathcal C\); these have a length of at least some \(\rho>0\), and Lemma 2.1 (3) gives the bound \(C t^{-1}e^{-\rho^2/(8t)}\to0\). As \(t\to\infty\), \(\tfrac1N\sum_{i,j}P_{t,L}(a_i-a_j)\to\tfrac1N\cdot N^2\cdot\tfrac1N=1\) by Lemma 2.1 (2), and \(\Psi_t(0)\to0\).

**6.5.** The energy \(V_s\) is an integral over all \(t>0\) of the Gaussian energies for \(g_t\). The inequality between the integrands is needed for every \(t\); a configuration that is better than \(A\) for some widths could have a smaller integral. This is the reason why the notion of universal optimality asks for all Gaussians.

**6.6.** \(H_{\mathbb Z^2}(t)\ge4\Psi_t((1,0))=\tfrac1{\pi t}e^{-1/(4t)}\). For \(a\in A\setminus\{0\}\) and \(t\le1\), \(|a|^2\ge1/b\) gives \(e^{-|a|^2/(4t)}\le e^{-1/(4bt)}e^{-(|a|^2-1/b)/4}\), so \(H_A(t)\le\tfrac{C}{4\pi t}e^{-1/(4bt)}\) with the finite number \(C=\sum_{a\ne0}e^{-(|a|^2-1/b)/4}\). The quotient \(H_{\mathbb Z^2}(t)/H_A(t)\) is at least \(\tfrac4Ce^{(1/b-1)/(4t)}\), which tends to infinity as \(t\to0\). So \(H_{\mathbb Z^2}(t)>H_A(t)\) for all small \(t\). The integrand in Corollary 4.2 is not negative, and it is positive for all small \(t\); so the integral is positive.

## References

- [OpenAI-T] OpenAI, *Universal optimality of the triangular lattice*, OpenAI Math Release preprint, 23 September 2026, Section 8. https://github.com/openai/math/tree/main/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026
