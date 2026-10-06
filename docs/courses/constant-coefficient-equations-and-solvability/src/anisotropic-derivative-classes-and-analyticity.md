# Anisotropic derivative classes and analyticity

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Smoothness says that every derivative exists. A derivative class also controls how its size grows with the order of differentiation. For homogeneous constant-coefficient equations, the optimal directional exponents give an anisotropic class: some coordinates can have analytic derivative bounds while others have a larger Gevrey order. We derive the full mixed estimate and prove that universal analyticity of homogeneous solutions is equivalent to ellipticity.

Read [Uniform interior estimates with distance weights](uniform-interior-estimates-with-distance-weights.md) for the uniform boundary-loss estimate, and [Directional growth and complex-zero geometry](directional-growth-and-complex-zero-geometry.md) for the optimal exponents and their flag. The fixed-cutoff Sobolev and Cauchy arguments are linked below. We also use Taylor’s formula. Grubb [Grubb] gives the distribution and Sobolev background. The one-dimensional distributional inputs are the specific constant and ODE results in *Weak equations and classical functions* [Weak].

Throughout, \(P\) is a nonzero constant-coefficient polynomial with possibly complex coefficients, and \(D=-i\partial\).

[Fixed-support derivatives and logarithmic Fourier graphs](fixed-support-derivatives-and-fourier-graphs.md), Section 1, proves the fixed-cutoff Sobolev bound with a constant independent of the high derivative order. [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md), Sections 1 and 3, proves the polydisk estimates and local complex extension of a real analytic function.

## The mixed derivative class

For a vector of exponents \(\boldsymbol\rho=(\rho_1,\ldots,\rho_n)\), \(\rho_j\geq1\), let
\(\mathcal G^{\boldsymbol\rho}(X)\) be the smooth functions such that every compact \(K\subset X\) has a constant \(C\geq1\) satisfying
\[
\begin{gathered}
\sup_{x\in K}|D^\alpha u(x)|
\leq C^{|\alpha|+1}\prod_{j=1}^n\alpha_j^{\rho_j\alpha_j},
\\ \text{for every }\alpha.
\end{gathered}
\tag{1}
\]
We use \(0^0=1\). Equivalently the product can be
\(\prod_j(\alpha_j!)^{\rho_j}\): for integers \(k\geq1\),
\[
k!\leq k^k\leq e^k k!,
\tag{2}
\]
and the extra exponential factors enter \(C^{|\alpha|+1}\).

The class is associated with the specified coordinates. Under an adapted orthonormal basis for the directional flag, its exponents are the corresponding optimal directional values.

**Theorem 1.1.** Let \(n\geq2\) and let \(P\) be nonconstant and hypoelliptic. Choose an orthonormal basis adapted to its directional flag, and set \(\rho_j=\rho_P(e_j)\). Every distributional solution of \(P(D)u=0\) in \(X\) belongs to \(\mathcal G^{\boldsymbol\rho}(X)\).

**Proof.** Hypoellipticity makes \(u\) smooth. Fix a compact \(K\subset X\). Choose a relatively compact open neighborhood \(U\) of \(K\), with closure inside \(X\), and \(0<c<1\) so small that \(K\subset U_{2c}\). All the finitely many fixed derivatives used below have finite \(L^2(U)\) norms.

For \(N=|\alpha|\geq1\), set \(\delta=c/N\), and use the energy
\[
\begin{gathered}
E_\delta(v;V)^2
\\ =\sum_{0<|\gamma|\leq m}\delta^{-2|\gamma|}
\|P^{(\gamma)}(D)v\|_{L^2(V)}^2.
\end{gathered}
\tag{3}
\]
Every differentiated homogeneous solution is again homogeneous. Applying the boundary-loss estimate successively to the \(N\) coordinate derivatives gives
\[
E_\delta(D^\alpha u;U_c)
\leq C_0^N
\delta^{-\sum_j\rho_j\alpha_j}E_\delta(u;U).
\tag{4}
\]
The erosion losses add on arbitrary open sets, as proved in the distance-weight lesson. There are only \(n\) directional constants, so their maximum is the single \(C_0\).

Some symbol derivative of degree \(m\) is a nonzero constant. Since \(\delta<1\), the energy controls the unweighted \(L^2\) norm with a constant independent of \(\delta\). Also
\[
E_\delta(u;U)\leq C_u\delta^{-m},
\tag{5}
\]
because the sum in (3) contains finitely many fixed derivatives. The factor \(N^m\) from (5) is bounded by a fixed exponential in \(N\).

Apply (4) separately to \(D^\beta u\) for each fixed \(|\beta|\leq n\). Their initial energies satisfy the same type of bound (5), with finitely many constants. Local Sobolev embedding on the fixed pair \(K\subset U_c\) therefore gives
\[
\sup_K|D^\alpha u|
\leq C_1^{N+1}N^{\sum_j\rho_j\alpha_j}.
\tag{6}
\]
One can obtain this Sobolev estimate by multiplying by a cutoff supported in \(U_c\), applying the Fourier \(H^n\)-to-supremum inequality, and expanding its finitely many cutoff derivatives. The cutoff and its constants are fixed independently of \(\alpha\).

We now retain the exact anisotropic product. Put \(w_j=\alpha_j/N\) and \(\rho_*=\max_j\rho_j\). Omitting zero entries,
\[
\begin{gathered}
\sum_j\rho_j\alpha_j\log(N/\alpha_j)
\\ \leq \rho_*N\sum_jw_j\log(1/w_j)
\leq \rho_*N\log n.
\end{gathered}
\tag{7}
\]
The last inequality is the entropy bound for a probability vector. For completeness, concavity of \(\log\), with weights \(w_j\), gives
\(\sum_jw_j\log(1/w_j)\leq\log\sum_{w_j>0}1\leq\log n\).
Exponentiating (7) yields
\[
N^{\sum_j\rho_j\alpha_j}
\leq n^{\rho_*N}\prod_j\alpha_j^{\rho_j\alpha_j}.
\tag{8}
\]
Absorb the fixed exponential in (6). The case \(\alpha=0\) follows by boundedness on \(K\). This proves (1). \(\square\)

The same iteration in one fixed direction proves the following form without choosing flag coordinates.

**Corollary 1.2.** Assume that the symbol is nonconstant and hypoelliptic. If
\[
|y\cdot\xi|\leq C(1+d_P(\xi))^\rho,\qquad \rho\geq1,
\tag{9}
\]
then every homogeneous solution near a compact \(K\) has
\[
\begin{gathered}
\sup_K|(y\cdot D)^ju|\leq C_u^{j+1}j^{\rho j},
\\ j\geq1.
\end{gathered}
\tag{10}
\]
The constants may depend on \(K,u,P,y\), but not \(j\). For \(y=0\), the left side vanishes.

**Proof.** Use \(\delta=c/j\) and repeat the same directional boundary-loss estimate \(j\) times. Apply it also to finitely many fixed derivatives \(D^\beta u\) before the Sobolev step. The energy contributes at most a fixed power \(j^m\), absorbed into an exponential. This is the proof above with all \(j\) iterations in the same direction. \(\square\)

For a nonzero direction in dimensions at least two, the sharp lower theorem from the complex-zero lesson shows that the exponent \(\rho_P(y)\) in (10) cannot be reduced in an estimate valid for every homogeneous solution, even at a single point.

## The class with exponent one

**Proposition 2.1.** \(\mathcal G^{(1,\ldots,1)}(X)\) is exactly the class of real-analytic functions on \(X\).

**Proof.** By (2), membership is equivalent to the local factorial estimates
\[
\begin{gathered}
\sup_K|\partial^\alpha u|\leq C^{|\alpha|+1}\alpha!,
\\ \alpha!=\prod_j\alpha_j!.
\end{gathered}
\tag{11}
\]
The factors between \(D^\alpha\) and \(\partial^\alpha\) have modulus one.

Choose a closed box around \(x_0\) compactly contained in \(X\), and its constant \(C\). For a small real increment \(h\), apply one-variable Taylor's formula to \(g(t)=u(x_0+th)\), \(0\leq t\leq1\). Expanding \((h\cdot\partial)^N\) and using (11) bounds the Taylor remainder by
\[
C^{N+1}\sum_{|\alpha|=N}|h^\alpha|
\leq C\bigl(C\sum_j|h_j|\bigr)^N.
\tag{12}
\]
The multinomial coefficients in the power of the sum are at least one, proving the last inequality. If \(C\sum_j|h_j|<1\), the remainder tends to zero. The Taylor series therefore represents \(u\) near \(x_0\), proving real analyticity.

Conversely a real-analytic function has a holomorphic extension to a complex neighborhood of each point. On a smaller complex polydisk where the extension is bounded, Cauchy's formula gives factorial derivative bounds with powers of the reciprocal radii. A finite such cover of any compact \(K\) and the largest of its constants prove (11). \(\square\)

## Universal analyticity characterizes ellipticity

Recall that a nonzero degree-\(m\) symbol is elliptic if its ordinary principal part \(P_m\) is nonzero at every nonzero real covector. Nonzero constants are elliptic of order zero.

**Theorem 3.1.** Every local distributional homogeneous solution of \(P(D)u=0\) is real analytic if and only if \(P\) is elliptic.

**Proof in dimensions \(n\geq2\), for nonconstant \(P\).** If \(P\) is elliptic, it is hypoelliptic and its symbol derivative ratios satisfy
\[
\left|\frac{P^{(\alpha)}(\xi)}{P(\xi)}\right|
\leq C_\alpha|\xi|^{-|\alpha|}
\tag{13}
\]
at large real frequency. The derivative-distance comparison gives \(d_P(\xi)\geq c|\xi|\) there. Thus every coordinate has directional exponent at most one, and the complex-zero theorem makes it exactly one. Theorem 1.1 and Proposition 2.1 prove analyticity.

Conversely suppose every homogeneous solution is analytic. Then \(P\) is hypoelliptic. Indeed, if it were not, the localization and singularity-carrier results in [Geometry of singular supports](geometry-of-singular-supports.md) would supply a non-smooth global homogeneous solution. The finite differentiability in that construction can be chosen at least \(m\), so this contradiction also applies if the premise is stated only for classical solutions.

Fix a point in a nonempty open set. Analyticity of each homogeneous solution gives, by a local holomorphic extension and Cauchy estimates,
\[
\begin{gathered}
|(y\cdot D)^ju(x_0)|\leq C_u^{j+1}j!
\leq \widetilde C_u^j j^j,
\\ j\geq1.
\end{gathered}
\tag{14}
\]
The fixed prefactor enters \(\widetilde C_u^j\). The sharp universal lower bound forces \(\rho_P(y)\leq1\) for every nonzero \(y\): a larger exponent would make \(j^{(\rho_P(y)-1)j}\) grow faster than any fixed exponential. Hence all these exponents are one.

Apply their real-frequency bounds to a coordinate basis. We get
\[
|\xi|\leq C(1+d_P(\xi)),
\]
and therefore \(d_P(\xi)\geq c|\xi|\) at large frequency. Choose \(\alpha\) of order \(m\) with \(P^{(\alpha)}\) a nonzero constant. The derivative-distance estimate then gives
\[
|P(\xi)|\geq c\,d_P(\xi)^m
\geq c'|\xi|^m.
\tag{15}
\]
If \(P_m(\eta)=0\) at a real unit vector \(\eta\), the ray value \(P(t\eta)\) would be \(O(t^{m-1})\), contradicting (15). Thus \(P\) is elliptic. \(\square\)

## One dimension and constant operators

Every nonzero polynomial in one variable has nonvanishing principal symbol away from zero. Thus every such ordinary differential operator is elliptic.

Here is its analytic homogeneous solution argument, retaining the original coefficients and the distributional input. For an operator of degree \(m\geq1\), write
\[
\begin{aligned}
P(\xi)&=\sum_{j=0}^m a_j\xi^j,\qquad a_m\ne0,\\
b_j&=(-i)^j a_j,\qquad b_m\ne0.
\end{aligned}
\tag{15a}
\]
Since \(D=-i\partial_x\), the equation is exactly \(\sum_{j=0}^m b_j u^{(j)}=0\). Its monic comparison has coefficients \(b_j/b_m\). The higher-order scalar equation result in [Weak], Corollary 3.2, makes a distributional solution classical. Its derivative vector
\[
U=(u,u',\ldots,u^{(m-1)})^{\mathsf T}
\]
satisfies \(U'=AU\), where indices run from zero to \(m-1\) and
\[
\begin{aligned}
A_{i,i+1}&=1,\\
A_{m-1,j}&=-b_j/b_m.
\end{aligned}
\tag{15b}
\]
In the first line \(0\leq i<m-1\); in the second \(0\leq j<m\). All other entries are zero. Thus the last row retains every original coefficient ratio. The distributional product rule gives
\[
(e^{-xA}U)'=0.
\]
The distributional constants result in [Weak], Theorem 1.1, implies, on each interval component,
\[
\begin{gathered}
U(x)=e^{xA}c,
\\ \text{for a constant vector }c.
\end{gathered}
\tag{16}
\]
The convergent matrix exponential makes every component analytic. This proves Theorem 3.1 in dimension one.

On each fixed compact interval, \(U^{(j)}=A^jU\) gives an exponential derivative upper bound. If \(A\) is nilpotent, high derivatives can vanish identically; for example \(D^mu=0\) gives a polynomial of degree at most \(m-1\). If \(P\) has a nonzero complex root \(\lambda\), the exponential \(e^{ix\lambda}\) has positive derivative magnitudes proportional to \(|\lambda|^j\). These cases explain why a positive multidimensional lower bound \(c^jj^{\rho j}\) is not a universal one-dimensional assertion.

For a nonzero constant \(P\), \(P(D)u=0\) forces \(u=0\). Its analyticity and ellipticity of order zero complete the remaining case of Theorem 3.1.

## Examples of mixed classes

For a semielliptic polynomial with weights \(m_j\) and ordinary order \(m=\max_jm_j\), the exact directional exponents are
\[
\rho_j=m/m_j.
\tag{17}
\]
Theorem 1.1 therefore gives
\[
\sup_K|D^\alpha u|
\leq C^{|\alpha|+1}
\prod_j(\alpha_j!)^{m/m_j}.
\tag{18}
\]
In dimensions at least two, the lower complex-zero argument proves that each coordinate exponent is optimal for universal homogeneous estimates. In one dimension the upper analytic estimate holds, with the separate ODE degeneracies described above.

For the heat symbol \(i\tau+\xi^2\), (18) becomes
\[
\sup_K|D_t^aD_x^bu|
\leq C^{a+b+1}(a!)^2b!.
\tag{19}
\]
Its homogeneous solutions are analytic in the spatial direction with uniform local bounds, and have time Gevrey order two. This is a statement on compact subsets of the open solution domain, without an assertion about initial-boundary limits.

For \(P(\xi,\eta)=\xi^4+\eta^2\), the weights are \((4,2)\). Its bounds are analytic in the first coordinate and Gevrey order two in the second. Swapping variable names swaps those roles. Ordinary ellipticity would require both exponents to be one.

## Exercises with complete solutions

**Exercise 1. Introductory: factorial equivalence.** Prove (2) without Stirling's formula, and deduce equivalence of the two products in (1).

**Solution.** Every factor of \(k!\) is at most \(k\), giving \(k!\leq k^k\). Since \(\log\) is increasing,
\[
\log(k!)\geq\int_1^k\log t\,dt
=k\log k-k+1.
\]
Thus \(k^k\leq e^{k-1}k!\leq e^kk!\). Raise these inequalities to each \(\rho_j\) and multiply. The extra factor is at most \(e^{\rho_*|\alpha|}\), absorbed into \(C^{|\alpha|+1}\). Zero entries contribute one under either convention.

**Exercise 2. Introductory: an anisotropic example.** Find the exact coordinate exponents and mixed class for \(P(\xi,\eta)=\xi^6+\eta^2+1\).

**Solution.** The anisotropic principal part \(\xi^6+\eta^2\) is positive away from real zero, with weights \((6,2)\). The ordinary order is six. Hence the exponents are \((1,3)\), and every local homogeneous solution satisfies
\[
\sup_K|D_x^aD_y^bu|
\leq C^{a+b+1}a!(b!)^3.
\]
The constant term is of lower anisotropic degree and does not change these sharp exponents.

**Exercise 3. Intermediate: the entropy correction.** For \(N=|\alpha|\), prove (8). Explain why retaining only \(N^{\rho_*N}\) loses information.

**Solution.** For the positive entries \(w_j=\alpha_j/N\), Jensen's inequality gives
\(\sum w_j\log(1/w_j)\leq\log n\).
Each \(\log(N/\alpha_j)\geq0\), so replacing its coefficient \(\rho_j\) by \(\rho_*\) gives (7). Subtract
\(\sum\rho_j\alpha_j\log\alpha_j\) from
\((\sum\rho_j\alpha_j)\log N\), then exponentiate, to obtain (8). The cruder bound uses the largest exponent even when all derivatives are in a smaller-exponent direction; it no longer proves that direction's sharper class.

**Exercise 4. Intermediate: the Taylor remainder.** Under (11), derive (12), keeping the multinomial coefficients and the factor \(N!\) from one-variable Taylor's formula.

**Solution.** Along \(g(t)=u(x_0+th)\),
\[
g^{(N)}(t)
=\sum_{|\alpha|=N}\frac{N!}{\alpha!}
h^\alpha\partial^\alpha u(x_0+th).
\]
The remainder after degree \(N-1\) is bounded by \(\sup_{0\leq t\leq1}|g^{(N)}(t)|/N!\). The \(\alpha!\) in (11) cancels its reciprocal and the \(N!\) cancels the Taylor denominator. This leaves
\(C^{N+1}\sum_{|\alpha|=N}|h^\alpha|\).
The expansion of \((\sum|h_j|)^N\) has the same monomials with coefficients at least one, proving (12).

**Exercise 5. Advanced: analyticity forces the principal symbol.** Suppose \(d_P(\xi)\geq c|\xi|\) for large real \(\xi\). Derive (15) from one highest symbol derivative and use a ray to prove ellipticity.

**Solution.** Choose \(|\alpha|=m\) with \(P^{(\alpha)}=a\ne0\). The derivative-distance estimate gives
\(|a/P(\xi)|\leq C_\alpha d_P(\xi)^{-m}\).
At large real frequency the assumed distance is positive, so \(P(\xi)\ne0\). Rearranging gives
\(|P(\xi)|\geq (|a|/C_\alpha)d_P(\xi)^m\geq c'|\xi|^m\).
If \(P_m(\eta)=0\) for a real unit \(\eta\), homogeneity and the lower-order terms give \(P(t\eta)=O(t^{m-1})\), contradicting that bound as \(t\to\infty\).

**Exercise 6. Advanced: a nilpotent ODE case.** Prove that a distributional solution of \(D^mu=0\) on an interval is a polynomial of degree at most \(m-1\), and explain the consequence for universal positive derivative lower bounds.

**Solution.** The derivative vector in (16) has the shift companion matrix with ones immediately above the diagonal and zeros elsewhere. It satisfies \(A^m=0\), so
\[
e^{xA}=\sum_{k=0}^{m-1}\frac{x^kA^k}{k!}.
\]
The exact distributional constants argument gives this expression for every distributional solution vector, hence a polynomial first component. All derivatives of order at least \(m\) vanish. A universal estimate may therefore take \(M_j=0\) for those orders, excluding any positive bound \(M_j\geq c^jj^{\rho j}\) for all \(j\). Analyticity is fully consistent with this degeneracy.

## References

- **[Grubb]** Gerd Grubb, *Distributions and Operators*, open lectures on Fourier transformation, Sobolev embedding, and elliptic regularity. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- **[Weak]** *Weak equations and classical functions*, Theorem 1.1 on distributional constants and Corollary 3.2 on higher-order scalar equations. [Published source](../prerequisites/weak-equations-and-classical-functions.html).
