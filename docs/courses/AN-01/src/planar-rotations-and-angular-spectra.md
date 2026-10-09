# Planar rotations and angular spectra

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

In the plane, the Fourier transform of an even distribution of degree minus one is a quarter turn multiplied by \(2\pi\). This statement includes continuous angular profiles, integrable profiles with jumps, measures concentrated in a pair of directions, and derivatives of angular point masses. We prove the common formula on all Schwartz tests and distinguish the different kinds of spatial distributions it describes.

We use \(F\phi(\xi)=\int e^{-ix\cdot\xi}\phi(x)\,dx\), its bilinear transpose, and \(G=(2\pi)^{-n}F\mathcal R\), where \(\mathcal R\phi(x)=\phi(-x)\). The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves every Schwartz estimate, inversion and coordinate identity. [Radial powers and the logarithmic endpoint](radial-powers-and-the-logarithmic-endpoint.md), Theorems 1.1 and 3.1 and Lemma 3.3, supplies the whole radial transform and the logarithmic gradient. [Homogeneous extensions and angular moments](homogeneous-extensions-and-angular-moments.md), Lemma 1.1 and Theorems 1.2 and 3.1, supplies the angular classification and uniqueness through the origin. Its [angular foundation](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A1–A5, includes point jets, polar integration and circle measure.

For matrices we use the complete real symmetric diagonalization proof at the start of Section 2 in [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), and the [finite algebra foundation](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), Sections 10.1–10.6. The [scalar](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Sections 12.4–12.9, 13.1–13.5 and 13.7–13.10, and [integration](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15.0–15.1 and 16.1–16.2, foundations prove the calculus, cutoffs, convergence, Fubini and linear substitutions used below. The supplied [measure foundation](../prerequisites/U011-free-foundations/positive-measure-foundations-U008.md), Theorem M and M10–M11, proves positive representation and complex variation.

## A linear substitution rotates a planar quadratic form

**Theorem 1.1.** If \(Q\) is real symmetric positive definite, \(A(x)=x^TQx\) on \(\mathbb R^n\), and \(0<\operatorname{Re}a<n\), then
\[
 F(A^{-a/2})(\xi)
   =(\det Q)^{-1/2}C_{n,a}
          (\xi^TQ^{-1}\xi)^{(a-n)/2},
 \qquad
 C_{n,a}=2^{n-a}\pi^{n/2}
     \frac{\Gamma((n-a)/2)}{\Gamma(a/2)}.
 \tag{1.1}
\]
This is an equality of whole regular tempered distributions. For \(n=2,a=1\), put \(J(\xi_1,\xi_2)=(\xi_2,-\xi_1)\). Then
\[
 F(A^{-1/2})(\xi)=2\pi A(J\xi)^{-1/2}.
 \tag{1.2}
\]

**Proof: the whole linear transformation rule.** For any invertible real \(B\), define
\[
 u(B\cdot)(\phi)=|\det B|^{-1}u(\phi\circ B^{-1}).
\]
All derivatives of a linearly substituted Schwartz test are finite linear combinations of derivatives of the original test. The bounds \(|Bx|\le C_B|x|\), \(|x|\le C_{B^{-1}}|Bx|\) follow by summing its finitely many entries. They show continuity of this test map in every weighted seminorm. The absolute Jacobian substitution in the Fourier integral gives
\[
 F\phi(B^{-1}y)=|\det B|\,F[\phi\circ B^T](y).
\]
Consequently, directly on distributions,
\[
 \begin{aligned}
 (F[u(B\cdot)])(\phi)
 &=u(F[\phi\circ B^T])\\
 &=(Fu)(\phi\circ B^T)
 =\bigl[|\det B|^{-1}(Fu)(B^{-T}\cdot)\bigr](\phi).
 \end{aligned}
\]
This proof does not require the transformed distribution to have a density.

The proved real diagonalization of \(Q\) gives
\(Q=O^T\operatorname{diag}(\lambda_1,\ldots,\lambda_n)O\), with \(O\) orthogonal and all \(\lambda_j>0\). Set
\(B=O^T\operatorname{diag}(\sqrt{\lambda_j})O\).
Then \(B^TB=Q\), \(B^{-1}B^{-T}=Q^{-1}\), and \(\det B=\sqrt{\det Q}>0\), by determinant multiplication. Apply the preceding rule to \(g(y)=|y|^{-a}\) and U051's full radial identity. Local integrability and temperedness are preserved by the same linear change of variables. This proves (1.1).

For \(Q=\begin{pmatrix}p&r\\r&s\end{pmatrix}\), direct inversion gives
\[
 (\det Q)\xi^TQ^{-1}\xi
    =s\xi_1^2-2r\xi_1\xi_2+p\xi_2^2=A(J\xi).
\]
Both forms are positive off zero. Since \(C_{2,1}=2\pi\), taking their positive square roots in (1.1) gives (1.2). \(\square\)

## Continuous angular data need only a slice identity

The map \(J\) is orthogonal, \(J^2=-I\), and \(J^{-1}=-J\). Write
\(\omega(\theta)=(\cos\theta,\sin\theta)\). Thus \(J\omega(\theta)=\omega(\theta-\pi/2)\). Circle measure is \(d\theta\); scalar translation of the integral of a periodic function proves its invariance under \(J\) and under the antipodal map.

**Theorem 2.1.** Suppose \(u\) is continuous off zero, \(u(-x)=u(x)\), and \(u(tx)=t^{-1}u(x)\) for \(t>0\). Then \(u\) has a regular tempered extension through zero and
\[
 Fu(\xi)=2\pi u(J\xi).
 \tag{2.1}
\]

**Proof: integrability and the slice.** The profile \(a(\omega)=u(\omega)\) is bounded and even. Polar integration gives
\[
 u(\psi)=\int_{S^1}a(\omega)
                 \int_0^\infty\psi(r\omega)\,dr\,d\omega.
 \tag{2.2}
\]
For \(p_2(\psi)=\sup_x(1+|x|^2)|\psi(x)|\), the absolute integral is at most
\((\pi/2)\|a\|_1p_2(\psi)\), using the arctangent integral
\(\int_0^\infty(1+r^2)^{-1}dr=\pi/2\).
The integral of \(|u|\) on a radius-\(R\) ball is \(R\|a\|_1\). These statements prove local integrability and temperedness.

For \(\phi\in\mathcal S(\mathbb R^2)\), define
\(g_\omega(s)=\int_{\mathbb R}\phi(s\omega+tJ\omega)\,dt\).
This is a one-dimensional Schwartz function, with seminorms bounded uniformly in \(\omega\). In detail, its \(m\)-th \(s\)-derivative is the integral of \((\omega\cdot\nabla)^m\phi\); expand the finite binomial sum. With \(\langle t\rangle=(1+t^2)^{1/2}\),
\[
 \langle s\rangle^M\langle t\rangle^2
       \le\langle(s,t)\rangle^{M+2}
\]
bounds each term by an integrable multiple of \(\langle t\rangle^{-2}\), uniformly in \(s,\omega\). Dominated difference quotients prove all derivatives and their continuity. Fubini and the orthogonal coordinates \(\eta=s\omega+tJ\omega\) now give
\(F\phi(r\omega)=F_{\mathbb R}g_\omega(r)\).
One-dimensional Schwartz inversion at zero therefore proves
\[
 \int_{\mathbb R}F\phi(r\omega)\,dr
       =2\pi\int_{\mathbb R}\phi(tJ\omega)\,dt.
 \tag{2.3}
\]
Both line integrals are absolute and uniformly bounded in direction by fixed seminorms of \(F\phi\) and \(\phi\), respectively.

**Proof: fold the two half-lines.** Apply (2.2) to \(F\phi\). Evenness of \(a\), antipodal substitution, (2.3), and the same substitution once more give
\[
 \begin{aligned}
 Fu(\phi)
 &=\tfrac12\int_{S^1}a(\omega)
                  \int_{\mathbb R}F\phi(r\omega)\,dr\,d\omega\\
 &=\pi\int_{S^1}a(\omega)
                  \int_{\mathbb R}\phi(tJ\omega)\,dt\,d\omega\\
 &=2\pi\int_{S^1}a(\omega)
                  \int_0^\infty\phi(rJ\omega)\,dr\,d\omega.
 \end{aligned}
 \tag{2.4}
\]
Every interchange is justified by the preceding uniform absolute bounds. Set \(\nu=J\omega\). Because \(a\) is even, \(a(J^{-1}\nu)=a(J\nu)\). Polar integration identifies the last line with the whole regular distribution \(2\pi u(J\cdot)\), proving (2.1). \(\square\)

No differentiability of \(a\) was used. The result preserves an angular corner, rotating its location. Applying it twice gives \(F^2u=(2\pi)^2u\), consistent with inversion and evenness.

## Rough angular data and singular directions

Define the radial test average
\[
 A\phi(\omega)=\int_0^\infty\phi(r\omega)\,dr.
 \tag{2.5}
\]
An angular distribution means a continuous complex-linear functional on the sphere test space of angular foundation A1. It is even when \(T(h\circ(-I))=T(h)\). Our rotation conventions are
\[
 (J^*T)(h)=T(h\circ J^{-1}),\qquad
 (J^*U)(\phi)=U(\phi\circ J^{-1}).
 \tag{2.6}
\]
For a spatial density the latter is \(u(Jx)\), since \(|\det J|=1\).

**Theorem 2.2 (every even homogeneous distribution).** For every even angular distribution \(T\), set
\[
 U_T(\phi)=T(A\phi).
 \tag{2.7}
\]
This gives exactly all even distributions on \(\mathbb R^2\) homogeneous of degree \(-1\); in particular all such distributions are tempered. The correspondence is a linear bijection, continuous in both directions for the weak and strong dual topologies of the angular space and the corresponding subspace of \(\mathcal S'\). Moreover,
\[
 FU_T=2\pi U_{J^*T}=2\pi J^*U_T,\qquad
 GU_T=(2\pi)^{-1}J^*U_T.
 \tag{2.8}
\]

If \(a\in L^1(S^1)\) is even almost everywhere and \(T_a(h)=\int ah\,d\omega\), then \(U_{T_a}\) is the regular distribution \(u_a(r\omega)=a(\omega)/r\), with
\[
 \begin{gathered}
 \int_{|x|<R}|u_a(x)|\,dx=R\|a\|_1,\\
 |U_{T_a}(\phi)|\le\tfrac{\pi}{2}\|a\|_1p_2(\phi),\qquad
 |FU_{T_a}(\phi)|\le\pi^2\|a\|_1p_2(\phi).
 \end{gathered}
 \tag{2.9}
\]
Its transform has density \(2\pi u_a(J\xi)\). Angular \(L^1\) convergence implies strong convergence of both spatial distributions and transforms. An even finite complex angular measure gives a locally finite spatial measure, with the last two bounds replacing \(\|a\|_1\) by its total variation norm. An arbitrary angular distribution need not give a spatial measure.

**Proof: the angular topology and radial estimates.** On the circle the seminorms
\(\|h\|_{C^q}=\max_{0\le j\le q}\sup_\theta|d^j h(\omega(\theta))/d\theta^j|\)
are equivalent to the radial-lift seminorms of angular A1. To see both directions explicitly, differentiation along the circle is the ambient operator
\(-x_2\partial_1+x_1\partial_2\).
Conversely, for the degree-zero lift,
\[
 \partial_1 h^\circ=-\frac{\sin\theta}{r}h'(\theta),
 \qquad
 \partial_2 h^\circ=\frac{\cos\theta}{r}h'(\theta).
\]
On \(1/2\le r\le2\), repeated differentiation bounds every ambient derivative by finitely many angular derivatives. A smooth periodic \(h(\theta)\) has such a smooth lift. On \(x_1>0\) use \(\theta=\arctan(x_2/x_1)\), and on \(x_1<0\) add \(\pi\) to that expression. On \(x_2>0\) use \(\theta=\pi/2-\arctan(x_1/x_2)\); on \(x_2<0\) use \(\theta=-\pi/2-\arctan(x_1/x_2)\). The scalar trigonometric formulas identify their unit vectors with \(x/|x|\), and the angles on overlaps differ by multiples of \(2\pi\). Their lifts therefore agree by periodicity. The scalar foundation proves smoothness of each local expression. This also justifies the derivative formulas. Thus the stated seminorms describe precisely the existing sphere test topology.

For \(j\le q\), repeated chain rules in \(\phi(r\omega(\theta))\) yield a finite sum of
\[
 c_{\beta,\ell}(\theta)r^\ell
              (\partial^\beta\phi)(r\omega(\theta)),
 \qquad |\beta|=\ell\le j,
\]
with bounded smooth coefficients; for \(j=0\) include \(\ell=0\). Induction proves this description, since a new derivative either differentiates the coefficient or adds one coordinate derivative and one factor \(r\). Put
\[
 s_q(\phi)=\max_{|\beta|\le q}\sup_x
                  \langle x\rangle^{q+2}|\partial^\beta\phi(x)|.
\]
For \(0<r<1\) each \(r^\ell\) is integrable; for \(r\ge1\), \(r^\ell\langle r\rangle^{-q-2}\le r^{-2}\). Dominated differentiation under the radial integral therefore proves
\[
 \|A\phi\|_{C^q}\le C_qs_q(\phi).
 \tag{2.10}
\]
In particular \(A:\mathcal S\to C^\infty(S^1)\) is continuous and sends bounded sets to bounded sets. Angular A1's finite-order bound, now in these equivalent seminorms, shows that \(U_T\) is tempered.

Reflection commutes with radial averaging, proving evenness. With the dilation convention \(D_tU(\phi)=t^{-2}U(\phi(\cdot/t))\), the positive substitution \(r=ts\) gives
\[
 (D_tU_T)(\phi)
 =t^{-2}T\left(\int_0^\infty\phi(r\omega/t)\,dr\right)
 =t^{-1}U_T(\phi).
 \tag{2.11}
\]
Thus its degree is \(-1\).

**Proof: Fourier transformation before the angular functional.** The two sides of (2.3) are smooth functions of \(\omega\): apply the full estimates (2.10) to \(F\phi\), to \(\phi\), and to their reflected or rotated radial averages. All angular derivatives converge uniformly. Equation (2.3) is therefore an equality of smooth sphere tests. Evenness of \(T\) identifies its pairing with either half-line average as half its pairing with the full-line average. Hence
\[
 \begin{aligned}
 FU_T(\phi)
 &=\tfrac12T\left(\int_{\mathbb R}F\phi(r\omega)\,dr\right)\\
 &=\pi T\left(\int_{\mathbb R}\phi(tJ\omega)\,dt\right)
 =2\pi T((A\phi)\circ J).
 \end{aligned}
 \tag{2.12}
\]
Since \(J^{-1}=-J\), evenness gives \(T(h\circ J)=T(h\circ J^{-1})\). Also
\(A(\phi\circ J^{-1})=(A\phi)\circ J^{-1}\).
These two identities give both equalities for \(F\) in (2.8). On even angular or spatial distributions, \((J^*)^2=I\), so this map has inverse \((2\pi)^{-1}J^*\). It agrees with the full Fourier inverse \(G\).

**Proof: bijection and both topologies.** Normalize a nonnegative nonzero smooth bump \(\eta\) supported in \((1,2)\) so that \(\int\eta=1\), and set
\[
 Bh(x)=\eta(|x|)h(x/|x|).
 \tag{2.13}
\]
It is a compact smooth test on one fixed annulus; angular A2 and the product rule bound each Schwartz seminorm by finitely many angular seminorms. Thus \(B\) is continuous, preserves bounded sets, and \(ABh=h\). Therefore \(U_T(Bh)=T(h)\), proving injectivity and giving the inverse on the image.

Let now \(U\in\mathcal D'(\mathbb R^2)\) be even and homogeneous of degree \(-1\). Apply U018, Theorem 1.2, to its restriction off zero. The resulting radial exponent is \(-1+2-1=0\), so the angular test is exactly \(A\phi\) on tests supported away from zero. The inverse formula using \(B\) shows that its angular functional \(T\) is even. The already constructed \(U_T\) is another homogeneous extension. U018, Theorem 3.1, gives uniqueness: degree \(-1\) differs from every possible point-jet degree \(-2-|\alpha|\). Its full point-jet proof therefore gives \(U=U_T\), proving surjectivity and temperedness without assuming either in advance.

Weak dual continuity follows by evaluation at the fixed test \(A\phi\) or \(Bh\). A strong dual seminorm takes the supremum over a bounded family of tests. The image of that family under \(A\) or \(B\) is bounded by the estimates just established, proving continuity in both directions for those seminorms as well.

**Proof: densities, measures and limits.** For \(a\in L^1\), polar integration proves its asserted regular pairing and the first two bounds in (2.9), just as in (2.2). Rotation preserves \(p_2\) and the angular \(L^1\) norm; (2.8) gives the last bound. Apply both bounds to \(a-b\). On any bounded set of Schwartz tests, \(p_2\) is uniformly bounded, proving both strong convergence statements.

For a positive finite angular measure \(\mu\), the formula
\[
 I_\mu(f)=\int_{S^1}\int_0^\infty f(r\omega)\,dr\,d\mu(\omega),
 \qquad f\in C_c(\mathbb R^2),
\]
defines a positive functional. On tests supported in a radius-\(R\) ball it is bounded by \(R\mu(S^1)\|f\|_\infty\). Theorem M represents it by a locally finite positive Radon measure. Equivalently it is the pushforward of \(dr\,d\mu\): monotone convergence for continuous compact cutoffs inside an open set identifies both values on open sets, and the supplied finite-measure generating-class proof on bounded balls identifies all Borel values. For a finite complex \(\mu\), apply this to its four positive parts; the result does not depend on the decomposition because the integral against every test does not. Its variation on a ball is at most \(R\|\mu\|_{\rm TV}\): apply \(|\int h\,d\mu|\le\int|h|\,d|\mu|\) to the radial sections of a finite Borel partition and sum; their sections are disjoint. The same inequality with the weight \((1+r^2)^{-1}\) proves the remaining two bounds. This measure has pairing \(T_\mu(A\phi)\), as asserted. \(\square\)

**The two eigenprojections.** For every even \(T\), put
\[
 T_+=\tfrac12(T+J^*T),\qquad
 T_-=\tfrac12(T-J^*T).
 \tag{2.14}
\]
Expanding the products and using \((J^*)^2=I\) gives idempotence, zero mixed product, sum \(I\), and \(J^*T_\pm=\pm T_\pm\). Rotation of tests is continuous, so the projections are continuous in both dual topologies. Formula (2.8) gives \(FU_{T_\pm}=\pm2\pi U_{T_\pm}\). If \(FU_T=\lambda U_T\ne0\), applying \(F\) again gives \(\lambda^2=(2\pi)^2\); the two complex roots are \(\pm2\pi\). Injectivity then identifies precisely the corresponding angular eigenspace.

## Exercises

**Exercise 1 (foundation).** Transform \((4x_1^2+2x_1x_2+2x_2^2)^{-1/2}\). Verify positivity and display the determinant before simplifying.

**Exercise 2 (intermediate).** Let \(u(x)=(x_1^2-x_2^2)/|x|^3\), \(B=\begin{pmatrix}1&2\\3&1\end{pmatrix}\), and \(w(x)=u(Bx)\). Calculate \(Fw\) both by the linear transformation rule and by the quarter-turn theorem. Resolve the negative determinant explicitly.

**Exercise 3 (intermediate).** Transform \(r^{-1}[\cos(2\theta)+i\sin(4\theta)]\) and explain the signs of the two components.

**Exercise 4 (advanced).** For \(u(x)=|x_1|/|x|^2\), find the whole transform. For \(\varepsilon>0\), approximate its profile by \(\sqrt{\cos^2\theta+\varepsilon^2}\). Give explicit errors, measured by \(p_2(\phi)\), for both the distributions and their transforms.

**Exercise 5 (advanced).** Describe every nonzero continuous even degree-\(-1\) Fourier eigenfunction in the plane, including both angular eigenspaces and their projections.

**Exercise 6 (intermediate).** Compute \(F(x_1/|x|^2)\) on all Schwartz tests and compare it with its proposed quarter-turn expression. Specify the failed hypothesis.

**Exercise 7 (foundation).** Invert \(v(\xi)=(\xi_1^2+3\xi_2^2)/|\xi|^3\), and verify the answer with \(F\).

**Exercise 8 (advanced).** Evaluate the pairing of \(F(|x_1|/|x|^2)\) with \(\phi(\xi)=e^{-\xi_1^2-4\xi_2^2}\), once in each variable. Reduce both absolute integrals to the same elementary one-dimensional integral.

**Exercise 9 (intermediate).** Let \(E\) be the two closed circle arcs of half-width \(\pi/6\) about \(e_1\) and \(-e_1\). Transform the profile \(a=1_E\) and give all bounds in (2.9). Construct even continuous approximations with an explicit \(L^1\) error. Then use the atomic profile \(\mu=\delta_{e_1}+\delta_{-e_1}\): identify its spatial measure, Fourier transform and eigenprojections. Show that narrow integrable angular caps converge strongly to this example, and explain why its spatial measure has no planar density.

**Exercise 10 (advanced).** With angle derivatives, let \(T(h)=h''(0)+h''(\pi)\). Find \(U_T\) as a combination of a line distribution and its transverse derivatives. Calculate its Fourier transform by two methods. Prove it is not a locally finite measure using tests of bounded supremum on a fixed compact set, and give its nonzero eigenprojections.

## Solutions

**Solution 1.** Here \(Q=\begin{pmatrix}4&1\\1&2\end{pmatrix}\), \(\det Q=7\), and
\[
 x^TQx=4(x_1+x_2/4)^2+\tfrac74x_2^2>0\quad(x\ne0).
\]
Theorem 1.1 gives
\[
 \frac{2\pi}{\sqrt7}(\xi^TQ^{-1}\xi)^{-1/2}
 =2\pi(2\xi_1^2-2\xi_1\xi_2+4\xi_2^2)^{-1/2},
 \quad
 Q^{-1}=\tfrac17\begin{pmatrix}2&-1\\-1&4\end{pmatrix}.
\]
The inverse quadratic factor contributes \(\sqrt7\), cancelling the absolute Jacobian. These are whole regular tempered distributions by the theorem.

**Solution 2.** The profile of \(u\) is \(\cos2\theta\), so it is even and continuous. Since \(\det B=-5\), the linear rule gives
\[
 Fw(\xi)=\frac{2\pi}{5}u(JB^{-T}\xi).
\]
For \(B=\begin{pmatrix}b&c\\d&e\end{pmatrix}\), direct multiplication of
\(B^{-T}=(\det B)^{-1}\begin{pmatrix}e&-d\\-c&b\end{pmatrix}\)
gives \(JB^{-T}=(\det B)^{-1}BJ\). Evenness and positive homogeneity imply \(u(ty)=|t|^{-1}u(y)\) for every real \(t\ne0\). Thus \(u(-BJ\xi/5)=5u(BJ\xi)\), cancelling the factor \(1/5\). Writing out \(BJ\xi\) gives
\[
 Fw(\xi)=2\pi
 \frac{(\xi_2-2\xi_1)^2-(3\xi_2-\xi_1)^2}
      {[(\xi_2-2\xi_1)^2+(3\xi_2-\xi_1)^2]^{3/2}}.
\]
Alternatively \(w\) itself has all the hypotheses of Theorem 2.1, which gives \(Fw=2\pi w(J\cdot)\) immediately. Both calculations use \(|\det B|\); orientation reversal changes no integration sign.

**Solution 3.** The scalar trigonometric addition formulas give
\(\cos(2(\theta-\pi/2))=-\cos2\theta\) and
\(\sin(4(\theta-\pi/2))=\sin4\theta\). Both profiles are antipodally even. Therefore
\[
 Fu(r,\theta)=\frac{2\pi}{r}
               [-\cos2\theta+i\sin4\theta].
\]
The positive and negative signs are the two quarter-turn eigenvalues, and the theorem includes the whole locally integrable extension at zero.

**Solution 4.** The continuous even profile \(|\cos\theta|\) gives
\[
 Fu(\xi)=2\pi|\xi_2|/|\xi|^2.
\]
For real \(t\), squaring nonnegative quantities proves
\(|t|\le\sqrt{t^2+\varepsilon^2}\le |t|+\varepsilon\).
The profile error has \(L^1\) norm at most \(2\pi\varepsilon\). Apply (2.9) to obtain
\[
 |(u_\varepsilon-u)(\phi)|\le\pi^2\varepsilon p_2(\phi),
 \qquad
 |(Fu_\varepsilon-Fu)(\phi)|\le2\pi^3\varepsilon p_2(\phi).
\]
These bounds are uniform on every bounded Schwartz family. The transformed density retains a corner along the nonzero \(\xi_1\)-axis: with \(\xi_1\ne0\) fixed, the two one-sided \(\xi_2\)-derivatives at zero are \(2\pi/\xi_1^2\) and \(-2\pi/\xi_1^2\).

**Solution 5.** Set \(Ru=u\circ J\). On even functions \(R^2=I\), and \(F=2\pi R\). Thus
\[
 u_+=\tfrac12(u+Ru),\qquad u_-=\tfrac12(u-Ru)
\]
have eigenvalues \(2\pi\) and \(-2\pi\). The converse follows from the eigenprojection result after Theorem 2.2. For continuous profiles the angular equalities hold pointwise: a continuous nonzero difference has, after multiplication by a constant phase, strictly positive real part on a small arc, and a nonnegative smooth bump in that arc contradicts a zero distribution. Hence the two spaces are exactly
\[
 a(\theta+\pi/2)=a(\theta)
 \quad\hbox{and}\quad
 a(\theta+\pi/2)=-a(\theta),
\]
respectively. Both imply antipodal evenness after two shifts. For
\(a=c_0+c_2\cos2\theta+s_2\sin2\theta+c_4\cos4\theta\),
the positive projection keeps \(c_0,c_4\), and the negative one keeps \(c_2,s_2\). A profile with both nonzero projections is not an eigenprofile.

**Solution 6.** U051, Theorem 3.1, at \(n=2,\alpha=(1,0)\), gives
\[
 F(x_1/|x|^2)=-2\pi i\,\partial_{\xi_1}\log|\xi|.
\]
Its whole weak gradient is the regular function \(\xi_1/|\xi|^2\), as fully proved in U051, Lemma 3.3. Explicitly, punctured integration by parts has inner boundary error bounded by \(C\varepsilon|\log\varepsilon|\|\phi\|_\infty\); the gradient is locally integrable, so this error tends to zero. Schwartz decay controls the outer boundary. Consequently
\[
 F(x_1/|x|^2)=-2\pi i\,\xi_1/|\xi|^2.
\]
The quarter-turn expression would be \(2\pi\xi_2/|\xi|^2\), different already at \((1,0)\). The input is odd, so the antipodal folding in (2.4) is unavailable.

**Solution 7.** Formula (2.8) gives
\[
 Gv(x)=\frac{x_2^2+3x_1^2}{2\pi|x|^3}.
\]
Applying \(F\) again gives \(v(J^2\xi)=v(-\xi)=v(\xi)\). This verifies the normalization and the entire distribution.

**Solution 8.** The frequency calculation from Solution 4 is
\[
 \begin{aligned}
 Fu(\phi)
 &=2\pi\int_0^{2\pi}|\sin\theta|
       \int_0^\infty e^{-r^2(1+3\sin^2\theta)}\,dr\,d\theta\\
 &=\pi\sqrt\pi\int_0^{2\pi}
       \frac{|\sin\theta|}{\sqrt{1+3\sin^2\theta}}\,d\theta
 =4\pi\sqrt\pi I,
 \end{aligned}
\]
where \(I=\int_0^1(4-3t^2)^{-1/2}\,dt\), using \(t=\cos\theta\) on the first quadrant and symmetry. To evaluate \(I\), put \(t=(2/\sqrt3)\sin s\), \(0\le s\le\pi/3\). This is a strictly increasing smooth substitution with positive cosine; its differential cancels the square root, giving \(I=\pi/(3\sqrt3)\). The endpoint identity \(\sin(\pi/3)=\sqrt3/2\) follows from the scalar trigonometric formulas.

Independently, product Gaussian integration gives
\(F\phi(x)=(\pi/2)e^{-x_1^2/4-x_2^2/16}\).
With \(p(\theta)=(1+3\cos^2\theta)/16\), polar integration yields
\[
 \begin{aligned}
 u(F\phi)
 &=\frac{\pi\sqrt\pi}{4}
        \int_0^{2\pi}\frac{|\cos\theta|}{\sqrt{p(\theta)}}\,d\theta\\
 &=\pi\sqrt\pi\int_0^{2\pi}
        \frac{|\cos\theta|}{\sqrt{1+3\cos^2\theta}}\,d\theta
 =4\pi\sqrt\pi I.
 \end{aligned}
\]
Here \(t=\sin\theta\) on the first quadrant gives the same integral. Tonelli applies to all these nonnegative integrands, and the radial Gaussian integrals are finite. Both pairings equal \(4\pi^2\sqrt\pi/(3\sqrt3)\).

**Solution 9.** The two arcs have total length \(2\pi/3\). Formula (2.9) therefore gives
\[
 \int_{|x|<R}|u_a|\,dx=\tfrac{2\pi}{3}R,\qquad
 |u_a(\phi)|\le\tfrac{\pi^2}{3}p_2(\phi),\qquad
 |Fu_a(\phi)|\le\tfrac{2\pi^3}{3}p_2(\phi).
 \tag{3.1}
\]
The transformed density is \(2\pi 1_E(J\xi/|\xi|)/|\xi|\). Its two sectors have the same half-width and are centered on the vertical axis. Boundary-ray values are immaterial because those rays have zero planar measure.

For \(0<\varepsilon<\pi/6\), keep the value one on \(E\), taper linearly to zero in each of its four exterior angular strips of width \(\varepsilon\), and set the value zero elsewhere. The result \(a_\varepsilon\) is continuous and even. Each strip contributes the triangle area \(\varepsilon/2\), so \(\|a_\varepsilon-a\|_1=2\varepsilon\). Consequently
\[
 |(u_{a_\varepsilon}-u_a)(\phi)|\le\pi\varepsilon p_2(\phi),
 \qquad
 |(Fu_{a_\varepsilon}-Fu_a)(\phi)|\le2\pi^2\varepsilon p_2(\phi).
 \tag{3.2}
\]
This proves strong convergence of both families.

For \(\mu=\delta_{e_1}+\delta_{-e_1}\), the pairing is
\[
 U_\mu(\phi)=\int_0^\infty[\phi(r,0)+\phi(-r,0)]\,dr
             =\int_{\mathbb R}\phi(t,0)\,dt.
 \tag{3.3}
\]
Thus \(U_\mu=\delta(x_2)\), meaning Lebesgue measure along the first axis, with mass \(2R\) in a radius-\(R\) ball and no atom at zero. Equation (2.8) gives
\[
 F\delta(x_2)=2\pi\delta(\xi_1).
 \tag{3.4}
\]
Equation (2.3) at \(\omega=e_1\) independently proves the same line pairing by ordinary one-dimensional inversion.
This spatial measure has no locally integrable planar density. Indeed choose a nonnegative smooth compact \(\eta\) of positive integral on the first axis and a smooth compact \(\chi=1\) near zero with \(0\le\chi\le1\). The tests \(\eta(x_1)\chi(Nx_2)\) have one common compact support. Against any locally integrable density their pairings tend to zero by dominated convergence, since they tend to zero off the measure-zero axis. Against the line measure the pairings are the fixed positive number \(\int\eta\). Its eigenprojections are
\[
 \tfrac12[\delta(x_2)+\delta(x_1)],\qquad
 \tfrac12[\delta(x_2)-\delta(x_1)],
 \tag{3.5}
\]
with eigenvalues \(2\pi\) and \(-2\pi\).

To obtain this example as an actual limit, give each angular cap of half-width \(\varepsilon\) about \(0,\pi\) the height \(1/(2\varepsilon)\), obtaining \(b_\varepsilon\). Each cap has mass one. FTC and its mean distance \(\varepsilon/2\) from the center give
\[
 |T_{b_\varepsilon}(h)-\mu(h)|
       \le\varepsilon\|h'\|_\infty.
 \tag{3.11}
\]
Apply (2.10), \(q=1\), to obtain the spatial error
\(C_1\varepsilon s_1(\phi)\), and (2.8) to obtain the Fourier error
\(2\pi C_1\varepsilon s_1(\phi)\); \(J\) preserves \(s_1\). Both tend to zero uniformly on bounded tests. This is not angular \(L^1\) convergence: if an \(L^1\) density represented \(\mu\), bounded smooth functions supported in shrinking caps and equal to one at both centers would have integrals tending to zero by dominated convergence but \(\mu\)-values equal to two.

**Solution 10.** Angle derivative evaluation is bounded by \(2\|h\|_{C^2}\), and the shift by \(\pi\) exchanges the two terms, proving that \(T\) is an even angular distribution. Differentiation under the radial integral is justified by (2.10). At \(\theta=0\) the velocity of \(r\omega(\theta)\) is \((0,r)\) and its acceleration is \((-r,0)\); at \(\pi\) they are \((0,-r)\) and \((r,0)\). Combining the two rays with \(t=-r\) on the second gives
\[
 \begin{aligned}
 U_T(\phi)
 &=\int_{\mathbb R}
       [t^2\partial_2^2\phi(t,0)-t\partial_1\phi(t,0)]\,dt\\
 &=\int_{\mathbb R}
       [t^2\partial_2^2\phi(t,0)+\phi(t,0)]\,dt.
 \end{aligned}
 \tag{3.6}
\]
The last step is one full-line integration by parts; \(t\phi(t,0)\) vanishes at both ends. Therefore
\[
 W:=U_T=\delta(x_2)+x_1^2\partial_2^2\delta(x_2).
 \tag{3.7}
\]
The derivative is in the coordinate transverse to the line; all pairings are the full tempered pairings just displayed.

For the rotated distribution, substitute \(\psi(x)=\phi(J^{-1}x)\) into (3.6). Then \(\psi(t,0)=\phi(0,t)\), and \(\partial_2^2\psi(t,0)=\partial_1^2\phi(0,t)\), because \(J^{-1}(x_1,x_2)=(-x_2,x_1)\). This proves, including signs,
\[
 FW=2\pi[\delta(\xi_1)+\xi_2^2\partial_1^2\delta(\xi_1)].
 \tag{3.8}
\]
Independently apply the whole derivative and coordinate rules to (3.4):
\[
 F[x_1^2\partial_2^2\delta(x_2)]
 =-\partial_1^2[-\xi_2^2\,2\pi\delta(\xi_1)]
 =2\pi\xi_2^2\partial_1^2\delta(\xi_1).
 \tag{3.9}
\]
Together with the first line term, this agrees with (3.8).

For the measure obstruction, choose \(0\le\eta,\chi\le1\), with nonzero \(\eta\in C_c^\infty((1,2))\) and \(\chi\in C_c^\infty((-1,1))\) equal to one near zero. The tests
\(\phi_N(x)=\eta(x_1)\chi(x_2)e^{iNx_2}\)
have one common compact support and supremum at most one. Equation (3.6) gives
\[
 W(\phi_N)=\int\eta(t)\,dt-N^2\int t^2\eta(t)\,dt.
 \tag{3.10}
\]
The second integral is strictly positive, so the pairings are unbounded. A locally finite complex measure would bound them by its finite variation on that compact set, a contradiction.

Put \(V=J^*W=\delta(x_1)+x_2^2\partial_1^2\delta(x_1)\). The two projections are \((W+V)/2\) and \((W-V)/2\), with eigenvalues \(2\pi\) and \(-2\pi\). Both are nonzero: use \(\phi(x)=\eta(x_1)\chi(x_2)\) with the preceding supports. Then \(V(\phi)=0\), while \(W(\phi)=\int\eta>0\), because all derivatives of \(\chi\) vanish at zero. This also exhibits explicitly the positive-order case beyond measures.

## References

- [Radial powers and the logarithmic endpoint](radial-powers-and-the-logarithmic-endpoint.md), Theorems 1.1 and 3.1 and Lemma 3.3: the complete radial coefficient and weak logarithmic gradient.
- [Homogeneous extensions and angular moments](homogeneous-extensions-and-angular-moments.md), Lemma 1.1 and Theorems 1.2 and 3.1; [angular foundation](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A1–A5: the angular description, origin uniqueness, test spaces and polar integration.
- [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Section 2, “Real symmetric diagonalization”: the complete finite matrix proof used in Theorem 1.1. The other supplied foundations and exact sections are listed at the start.
- Peter Woit, [*Fourier Analysis Notes, Spring 2020*](https://www.math.columbia.edu/~woit/fourier-analysis/fouriernotes.pdf), September 3, 2020, Sections 4.3–4.3.1, pp. 45–48: free author notes on transposed rotations, Fourier commutation and planar angular coordinates. The source uses the exponent \(-2\pi i x\cdot p\); our convention and all constants are fixed above. The slice identity, homogeneous correspondence, measure statements and solved examples are fully proved here or in the supplied earlier programme lessons.
