# Wave powers and complex potentials

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

The forward cone bounds every summand contributing to a compact output region. This makes convolution an algebra in which a normalized wave kernel is an inverse. Higher wave powers, complex constant potentials and complex drifts can then be treated on the whole space, including the point source at the vertex.

The full entire Riesz construction used here is [U027](causal-point-sources-and-characteristic-cones.md), Lemma 4.0 and formulas (4.0a)–(4.0h). Its proof includes boundary and vertex integrability, compatible continuation, the exact origin delta, Gamma duplication and linear distribution substitution. Its one-dimensional input is [U022](causal-integration-of-complex-order.md), §1, formulas (1.3)–(1.6), and Theorems 2.1–2.2. The [Gamma foundations](../prerequisites/U011-free-foundations/gamma-foundations-U016.md), (G0)–(G2) and (W4a)–(W4e), supply the reciprocal Gamma function and its zeros and recurrence; the [angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4–A5, supply polar integration and the Gaussian constant.

Proper convolution, derivative transfer, associativity and continuity are fully proved in [U021](convolution-as-addition-of-supports.md), B0–B3, Theorems 1.1, 3.1–3.2 and Corollary 3.4. Finite-order continuity is [U008](order-positivity-and-limits.md), Proposition 1.2. For scalar operations we use the [calculus foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12, 13.1–13.5 and 13.7–13.10, and the [integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.2 and 16. The local holomorphic series and identity principle are [U013](cauchy-kernels-and-boundary-limits.md), Corollary 2.2, and [U014](gluing-holomorphic-sides.md), Lemma 3.2. Pairings are complex linear. No growth condition at infinity is imposed.

## The normalization of every wave power

Let \(n\ge1\), with coordinates \((t,x)\in\mathbb R\times\mathbb R^n\), and set
\[
\Box=\partial_t^2-\Delta_x,\qquad q=t^2-|x|^2,\qquad
C_+=\{t\ge|x|\}.
\]
Write \(R_\lambda=\mathcal R_\lambda\) for the spacetime family of U027 Lemma 4.0; this notation is distinct from the one-dimensional family in U022. The proved global identities are
\[
\Box R_{\lambda+1}=R_\lambda,\qquad
R_0=\delta_{(0,0)},\qquad
\operatorname{supp}R_\lambda\subset C_+.
\tag{1.1}
\]
For \(\operatorname{Re}\lambda>\max(0,(n-1)/2)\), its density is
\[
\begin{gathered}
R_\lambda=A_{\lambda,n}\boldsymbol1_{\{t>|x|\}}
q^{\lambda-(n+1)/2},\\
A_{\lambda,n}=
\frac{2^{1-2\lambda}\pi^{(1-n)/2}}
{\Gamma(\lambda)\Gamma(\lambda+(1-n)/2)}.
\end{gathered}
\tag{1.2}
\]
In U027, absolute spatial integration reduces the vertex condition to integrability of \(t^{2\operatorname{Re}\lambda-1}\). Continuation is \(R_\lambda=\Box^N R_{\lambda+N}\), with overlapping definitions proved equal. Coordinate multiplication forces \(R_0\) to be a point mass, and its explicitly evaluated time marginal gives mass one. Thus (1.1) includes the vertex.

We first explain the cone expression away from that vertex. Define
\(\chi_+^\alpha(s)=s_+^\alpha/\Gamma(\alpha+1)\) initially for \(\operatorname{Re}\alpha>-1\), continued by U022 formulas (1.3)–(1.6) and their proofs. In its notation this is the scalar family at parameter \(\alpha+1\); in particular
\(\chi_+^{-r}=\delta_0^{(r-1)}\) for integers \(r\ge1\).

On \(t>0\), coordinates \((u,x)=(q,x)\) have the explicit inverse
\[
t=\sqrt{u+|x|^2},\qquad
dt\,dx=\frac{du\,dx}{2\sqrt{u+|x|^2}}.
\]
Here is the substitution justification. For a continuous \(g\) on a compact interval, put \(H(y)=\int_{y_0}^y g(v)\,dv\). The FTC and chain rule give \((H\circ h)'=g(h)h'\); integrating proves substitution for a smooth increasing \(h\). Apply this for fixed \(x\) with \(h(t)=t^2-|x|^2\), on intervals in \(t>0\), then use Fubini. For a singular but integrable power at \(u=0\), apply the same calculation off a deleted neighborhood and pass to the limit in the absolute integrals. The exponents \(\operatorname{Re}\alpha>-1\) make that passage integrable.

The positive square root is continuous by its monotonicity and the identity
\[
\sqrt{y+h}-\sqrt y=\frac{h}{\sqrt{y+h}+\sqrt y}.
\]
The denominator stays bounded below near \(y>0\). Dividing by \(h\) gives \(v'=1/(2v)\); induction through this formula proves smoothness on the positive half-line.

For \(\psi\in C_c^\infty(\{t>0\})\), extend
\[
G_\psi(u,x)=
\frac{\psi(\sqrt{u+|x|^2},x)}{2\sqrt{u+|x|^2}}
\]
by zero wherever the square root is unavailable. This extension is smooth and compactly supported: the original support has \(t\ge d>0\), so the expression is identically zero near \(u+|x|^2=0\); its coordinate image is compact. Differentiation under its compact \(x\)-integral is the parameter-integral proof in U021 B1. Define the distribution \(\chi_+^\alpha(q)\) on \(t>0\) by
\[
\chi_+^\alpha(q)(\psi)
=\chi_+^\alpha\!\left(u\longmapsto\int G_\psi(u,x)\,dx\right).
\]
The transformed test has common compact support and bounded seminorms when \(\psi\) does, so this is a distribution and is entire in \(\alpha\). In the integrable range it agrees with the ordinary composed density. Comparison with (1.2) and the scalar identity principle therefore give, on \(t>0\),
\[
R_\lambda=
\frac{2^{1-2\lambda}\pi^{(1-n)/2}}{\Gamma(\lambda)}
\chi_+^{\,\lambda-(n+1)/2}(q)
\]
for every parameter, with \(1/\Gamma\) understood as its entire reciprocal. No critical substitution at the vertex is required.

**Theorem 1.1 (forward inverses of the wave powers).** For every integer \(k\ge0\), the unique \(C_+\)-supported fundamental solution of \(\Box^{k+1}\) is
\[
E_k=R_{k+1}.
\tag{1.3}
\]
On \(t>0\) it has the cone expression
\[
\begin{gathered}
E_k=\kappa_{k,n}\chi_+^{\,k+(1-n)/2}(q),\\
\kappa_{k,n}=\frac{2^{-2k-1}\pi^{(1-n)/2}}{k!}.
\end{gathered}
\tag{1.4}
\]
At the vertex, the notation means the global distribution (1.3). If \(n=2m+1\) is odd and \(k<m\), its exact support is the closed boundary \(\partial C_+\). In every other case its exact support is \(C_+\). For every cone-supported distribution \(g\), \(E_k*g\) is the unique cone-supported solution of \(\Box^{k+1}u=g\).

**Proof: normalization and support.** Iterating (1.1) gives \(\Box^{k+1}R_{k+1}=R_0=\delta\). The preceding coordinate construction and \(\Gamma(k+1)=k!\) give (1.4), with its exact coefficient.

For odd \(n=2m+1\) and \(k<m\), the scalar factor is
\(\chi_+^{k-m}=\delta_0^{(m-k-1)}\).
It is zero off \(q=0\). It is nonzero in every neighborhood of a nonvertex cone point: choose small coordinate product supports about \((u,x)=(0,x_0)\), and a test of the form
\[
\psi(t,x)=2t\,h(t^2-|x|^2)\rho(x)
\]
within that chart, where \(\int\rho=1\) and \(h^{(m-k-1)}(0)\ne0\). Its transformed integrated test is \(h\), so its pairing is a nonzero multiple of that derivative. Such supports can be arbitrarily small, because \(x_0\ne0\) and \(t_0=|x_0|>0\). A cutoff supported in \(t>0\) and equal to one on the positive inverse image makes the displayed expression a global test there. This proves that all nonvertex cone points belong to the support. There is no interior support, by the same scalar formula; off-cone support is excluded by (1.1). Closedness adds the vertex and gives exactly \(\partial C_+\).

For the remaining odd-dimensional cases the scalar exponent in (1.4) is a nonnegative integer, so the interior density is nonzero. For even \(n\) it is a half-integer. The reciprocal Gamma normalization is nonzero at that half-integer plus one, since its only zeros are the nonpositive integers, as proved in the supplied Gamma foundation. Thus the interior density is again a nonzero smooth power. A nonzero continuous density has nonzero pairing on a sufficiently small nonnegative bump after multiplication by a constant phase; hence every interior point belongs to the support. Closedness and (1.1) give \(C_+\).

**Proof: all sources and uniqueness.** Addition of any finite number of points in \(C_+\) is proper. If their sum lies in a compact set with time coordinate at most \(T\), each summand satisfies \(0\le t_j\le T\) and \(|x_j|\le t_j\). The contributing set is bounded and closed, hence compact. The triangle inequality gives \(C_++C_+=C_+\). Consequently all convolutions below exist and stay in this cone, by U021.

If \(V\) is another cone-supported fundamental solution, derivative transfer and the identity distribution give
\[
\begin{aligned}
V&=(\Box^{k+1}E_k)*V\\
 &=E_k*(\Box^{k+1}V)=E_k.
\end{aligned}
\tag{1.5}
\]
For arbitrary cone-supported \(g\), derivative transfer gives \(\Box^{k+1}(E_k*g)=g\). Any other solution \(w\) satisfies \(w=E_k*(\Box^{k+1}w)=E_k*g\) by the same calculation. This also proves uniqueness for zero source. \(\square\)

**Example 1.2 (a regular wave power on the line).** When \(n=1\), formula (1.2) applies to every \(\lambda=k+1\), and Gamma recurrence gives
\[
E_k=\frac{\boldsymbol1_{C_+}q^k}{2^{2k+1}(k!)^2}.
\]
In particular \(E_0=\boldsymbol1_{C_+}/2\). The boundary \(t=|x|\) has measure zero by Fubini, since every fixed-\(x\) time section is a singleton. Values of this density there can therefore be chosen arbitrarily without changing its distribution. The source equation holds globally.

## A convergent series for every complex potential

**Theorem 2.1 (the entire mass family).** For every \(a\in\mathbb C\), the series
\[
F_a=\sum_{j=0}^{\infty}a^jR_{j+1}
\tag{2.1}
\]
converges as distributions, locally uniformly in \(a\), also uniformly on bounded families of tests. Each test pairing is entire. Every parameter derivative is a distribution with a common finite test-order bound on fixed compact spacetime and parameter sets. The sum is the unique \(C_+\)-supported fundamental solution of \(\Box-a\). For every cone-supported \(g\), \(F_a*g\) is the unique cone-supported solution of \((\Box-a)u=g\).

**Proof: a majorant for the densities.** Set \(J=n\). For \(j\ge J\), the initial density formula applies and gives
\[
\begin{gathered}
R_{j+1}=C_{j,n}\boldsymbol1_{\{t>|x|\}}q^{\alpha_j},
\qquad \alpha_j=j+(1-n)/2,\\
C_{j,n}=\frac{2^{-2j-1}\pi^{(1-n)/2}}
{j!\Gamma(j+(3-n)/2)}.
\end{gathered}
\tag{2.2}
\]
The exponent is positive, since \(\alpha_J=(n+1)/2\); extension by zero is continuous, including at the vertex. All \(C_{j,n}\) in this range are positive, because the Gamma integral is positive on the positive real axis.

Let a compact test region \(K\) be contained in \(|t|\le T\), let \(L=\max(1,T^2)\), and bound \(|a|\le A\) with \(A\ge1\). On \(K\cap C_+\), \(0\le q\le L\). Put \(b_J=(n+3)/2\), and use the notation \((b)_0=1\), \((b)_m=b(b+1)\cdots(b+m-1)\). Gamma recurrence gives
\[
\begin{gathered}
D=A^JC_{J,n}L^{\alpha_J},\\
\sup_K|a^{J+m}R_{J+m+1}|
\le D\frac{(AL/4)^m}{(J+1)_m(b_J)_m}.
\end{gathered}
\tag{2.3}
\]
The ratio of consecutive majorant terms is
\[
\frac{AL}{4(J+m+1)(b_J+m)}\longrightarrow0.
\tag{2.4}
\]
In particular this ratio is at most \(1/2\) after some index. The remaining tail is bounded by a convergent geometric series, whose tails tend uniformly to zero. Multiplication by any fixed power of \(J+m\) preserves this conclusion: its extra successive ratio tends to one. This proves uniform convergence of the continuous density tail on \(K\) and on the parameter disk.

**Proof: differentiation and distribution bounds.** For an integer \(r\ge0\),
\[
\partial_a^r a^j=
\begin{cases}
j(j-1)\cdots(j-r+1)a^{j-r},&j\ge r,\\
0,&j<r.
\end{cases}
\]
For \(A\ge1\), its modulus on the disk is at most \(j^r A^j\) when \(j\ge r\); the finitely many small indices cause no issue. Hence (2.3) with a polynomial factor bounds every derivative series uniformly on compact disks and compact spacetime sets.

Here is the differentiation justification. Each polynomial partial sum \(S_N\), paired with a fixed test, satisfies
\[
S_N(a+h)-S_N(a)
=h\int_0^1 S_N'(a+\theta h)\,d\theta.
\]
The segment lies in a slightly larger fixed disk. Uniform convergence of both series permits passage to the limit in this finite integral. Its derivative-series limit is continuous, so division by \(h\) and passage \(h\to0\) gives the complex derivative. Apply the same argument to every derivative series. Thus every pairing is entire, with exactly the indicated derivatives.

The tail and all its parameter derivatives have pairing bounded by their uniform density bound times the volume of a fixed box containing \(K\), times \(\|\psi\|_\infty\). Each of the finitely many distributions \(R_{j+1}\), \(j<J\), has some finite order on that compact box, by U008 Proposition 1.2 (also directly by the continuation in U027). Choose their maximum order \(M\). Their finitely many polynomial coefficients and each fixed derivative are uniformly bounded on the parameter disk. Adding these estimates proves
\[
|\partial_a^r F_a(\psi)|\le C_{K,A,r}\|\psi\|_{C^M},
\qquad \operatorname{supp}\psi\subset K,\quad |a|\le A.
\]
The same \(M\) works for all \(r\), though the constant depends on \(r\). Density-tail errors tend to zero times \(\|\psi\|_\infty\), which proves convergence on bounded test families. Low-index kernels need not be densities.

**Proof: the equation retains the vertex.** At every finite \(N\), (1.1) gives the telescoping identity
\[
(\Box-a)\sum_{j=0}^Na^jR_{j+1}
=\delta_{(0,0)}-a^{N+1}R_{N+1}.
\tag{2.5}
\]
Indeed the differentiated \(j=0\) term is \(R_0\), and the differentiated \(j\)-th term for \(j\ge1\) cancels the potential term with index \(j-1\). For \(N\ge J\), the last term is bounded by \(A\) times the \(j=N\) term of (2.3), and tends to zero on compact tests uniformly in the parameter disk. Differentiation of distributions is continuous because it differentiates the fixed test. Taking the limit proves \((\Box-a)F_a=\delta\). Tests outside \(C_+\) pair to zero with every summand and therefore with the limit.

Proper convolution gives \((\Box-a)(F_a*g)=g\). If \(w\) is another cone-supported solution, then
\[
w=((\Box-a)F_a)*w=F_a*((\Box-a)w)=F_a*g.
\tag{2.6}
\]
This proves the asserted uniqueness and all source equations. \(\square\)

**Corollary 2.2 (resolvents and higher powers).** For all \(a,b\in\mathbb C\),
\[
\begin{gathered}
F_a-F_b=(a-b)F_a*F_b,\\
\partial_aF_a=F_a*F_a,\qquad
\left.\partial_a^kF_a\right|_{a=0}=k!R_{k+1}.
\end{gathered}
\tag{2.7}
\]
For every integer \(k\ge0\),
\[
G_{a,k}=\frac1{k!}\partial_a^kF_a
\tag{2.8}
\]
is the unique cone-supported fundamental solution of \((\Box-a)^{k+1}\).

**Proof.** The equation for \(F_b\) gives
\((\Box-a)F_b=\delta+(b-a)F_b\).
Convolve with \(F_a\). Derivative transfer turns the left side into \(F_b\); the right side is \(F_a+(b-a)F_a*F_b\). Rearrangement proves the first identity. For \(b\ne a\), divide by \(a-b\) and let \(b\to a\). The proved parameter derivative gives the left limit, while U021 Theorem 3.2, on the fixed cone supports, gives \(F_a*F_b\to F_a*F_a\). Termwise differentiation at zero proves the third identity.

Differentiating the source equation \(k\) times, by the established test bounds, gives
\[
(\Box-a)\partial_a^kF_a
=k\,\partial_a^{k-1}F_a\qquad(k\ge1).
\]
Iteration and \((\Box-a)F_a=\delta\) give \((\Box-a)^{k+1}\partial_a^kF_a=k!\delta\). Every parameter derivative still has cone support, because its pairings outside the cone differentiate the identically zero scalar function. The inverse-convolution argument of (2.6) with the higher operator proves uniqueness. \(\square\)

**Example 2.3 (an entire cosine without a square-root choice).** Define
\[
\mathcal C(z)=\sum_{j=0}^{\infty}\frac{z^j}{(2j)!}.
\]
The factorial ratio proves locally uniform convergence of every derivative series as above, so this is entire. Gamma recurrence and \(\Gamma(1/2)=\sqrt\pi\) give, by induction,
\[
\Gamma(j+1/2)=\frac{(2j)!\sqrt\pi}{4^j j!}.
\]
For \(n=2\), all \(R_{j+1}\), including \(j=0\), lie in the initial integrable range. Substituting this Gamma formula gives
\[
F_a=\frac{\boldsymbol1_{\{t>|x|\}}}{2\pi\sqrt q}\mathcal C(aq).
\tag{2.9}
\]
Indeed the \(j\)-th coefficient is \(q^{j-1/2}/[2\pi(2j)!]\). On a compact set the entire series is bounded uniformly for bounded \(a\). The leading \(q^{-1/2}\) density is locally integrable, including at the vertex, by U027's actual integrability proof. Dominated convergence therefore identifies the distributional sum with (2.9). For \(a=-\mu^2\), the scalar cosine series gives \(\mathcal C(aq)=\cos(\mu\sqrt q)\) inside the cone. Formula (2.9) itself uses no square root of \(a\).

## Complex drift is exponential conjugation

**Theorem 3.1 (all constant complex drift coefficients).** For arbitrary \(b_0,\ldots,b_n,c\in\mathbb C\), let
\[
P=\Box+2b_0\partial_t+2\sum_{j=1}^nb_j\partial_{x_j}+c.
\]
Set
\[
\ell(t,x)=-b_0t+\sum_{j=1}^nb_jx_j,\qquad
a=b_0^2-\sum_{j=1}^nb_j^2-c.
\tag{3.1}
\]
Then the unique \(C_+\)-supported fundamental solution is
\[
F=e^\ell F_a.
\tag{3.2}
\]
The squares in (3.1) are complex bilinear squares, without conjugation.

**Proof.** For a smooth \(h\), define \(hT(\psi)=T(h\psi)\). The product rule and compact bounds on derivatives of \(h\) preserve the finite test estimate, so this is a distribution. Directly on tests,
\[
\partial_j(hT)(\psi)=-T(h\partial_j\psi)
=\bigl(h\partial_jT+(\partial_jh)T\bigr)(\psi).
\]
The scalar exponential identities give \(e^\ell e^{-\ell}=1\) and its usual derivatives, even for complex coefficients. Applying the proved product rule twice yields
\[
\begin{aligned}
e^{-\ell}P(e^\ell T)
&=(\partial_t-b_0)^2T-\sum_j(\partial_{x_j}+b_j)^2T\\
&\quad+2b_0(\partial_t-b_0)T
+2\sum_jb_j(\partial_{x_j}+b_j)T+cT\\
&=(\Box-a)T.
\end{aligned}
\tag{3.3}
\]
The time first derivatives cancel, as do the spatial first derivatives. The remaining scalar is \(c-b_0^2+\sum_jb_j^2=-a\). Thus \(P(e^\ell F_a)=e^\ell\delta=\delta\), since \(\ell(0)=0\).

Multiplication by a nowhere-zero smooth function preserves support: multiplication cannot enlarge support, and the inverse multiplier proves the reverse inclusion. Every other forward inverse becomes an inverse of \(\Box-a\) after multiplication by \(e^{-\ell}\), so Theorem 2.1 proves uniqueness. This includes \(a=0\) and imposes no boundedness condition on the exponential. \(\square\)

## Exercises

**Exercise 1 (basic: an oscillating interior).** In two spatial dimensions find the forward fundamental solution of \(\Box+4\) and determine its exact support.

**Exercise 2 (intermediate: a third wave power).** In one spatial dimension compute the forward inverse of \(\Box^3\), and compare it with \(\left.\partial_a^2F_a\right|_{a=0}\).

**Exercise 3 (intermediate: a convolution resolvent).** Express \(F_3*F_{-2}\) without a convolution integral. Find the coincident-parameter limit.

**Exercise 4 (advanced: two singular cone layers).** In five spatial dimensions compute the two singular layers of \(F_a\) off the vertex and its complete regular tail. Determine the exact support for zero and nonzero \(a\).

**Exercise 5 (intermediate: complex squares).** In two spatial dimensions set \(b_0=i\), \(b_1=1+i\), \(b_2=2\), \(c=3i\). Find the forward inverse and the exact source error obtained by replacing the coefficient squares with absolute squares.

**Exercise 6 (intermediate: an anisotropic cone).** Find the forward fundamental solution of
\[
\partial_t^2-4\partial_{x_1}^2-9\partial_{x_2}^2-a
\]
with support in \(t\ge\sqrt{x_1^2/4+x_2^2/9}\). Include its point-source Jacobian and an explicit density.

**Exercise 7 (advanced: convolution of wave powers).** For integers \(p,q\ge0\), prove \(E_p*E_q=E_{p+q+1}\). In one spatial dimension compute \(E_0*E_0\) directly in characteristic coordinates.

**Exercise 8 (advanced: a third massive power).** In two spatial dimensions compute the unique forward inverse of \((\Box-a)^3\) in terms of \(\mathcal C\), and verify its normalization at \(a=0\).

## Complete solutions

**Solution 1.** Taking \(a=-4\) in (2.9) gives
\[
F_{-4}=\frac{\boldsymbol1_{\{t>|x|\}}}{2\pi\sqrt q}\cos(2\sqrt q).
\]
Local integrability and the global source equation follow from Theorem 2.1 and Example 2.3.

We justify the exact support, including the nodal issue. A nonzero entire function cannot vanish on a real interval. If it did, at an interior point of that interval its local power series could have no first nonzero coefficient: such a coefficient would factor the function into a power times a function nonzero nearby, contradicting accumulating zeros. Thus it would vanish in a disk, and U014's identity principle would make it identically zero. The local series is proved in U013 Corollary 2.2.

Here the entire function \(r\mapsto\mathcal C(-4r)\) has value one at zero, so it vanishes on no interval. Every spacetime open set meeting the cone interior contains an interval of \(q\)-values: fix its spatial coordinate and vary \(t>0\) slightly, so \(q=t^2-|x|^2\) strictly increases. Some point in that open set has nonzero density, hence some smaller bump has nonzero pairing. Every interior point is therefore in the distributional support, and its closure is \(C_+\). Nodal hypersurfaces do not remove any open subset from this support.

**Solution 2.** Example 1.2 at \(k=2\) gives
\[
E_2=\frac{\boldsymbol1_{C_+}q^2}{128},
\qquad \Box^3E_2=\delta.
\]
Equation (2.7) gives
\[
\left.\partial_a^2F_a\right|_{a=0}
=2!R_3=2E_2=\frac{\boldsymbol1_{C_+}q^2}{64}.
\]
The factor two is precisely the parameter factorial. Both densities are nonzero everywhere in the cone interior, so their exact support is \(C_+\).

**Solution 3.** Cone addition is proper, and the resolvent identity gives
\[
F_3*F_{-2}=\frac{F_3-F_{-2}}5.
\]
More generally the divided difference \((F_a-F_b)/(a-b)\) tends to \(\partial_aF_a\) as \(b\to a\). The fixed-support continuity used in Corollary 2.2 identifies this with \(F_a*F_a\). The parameter limit holds as distributions and on bounded test families by the derivative estimates and the segment-FTC argument in Theorem 2.1.

**Solution 4.** For \(n=5\), the exponent in (1.4) is \(k-2\). Consequently on \(t>0\),
\[
R_1=\frac{\delta'(q)}{2\pi^2},\qquad
R_2=\frac{\delta(q)}{8\pi^2},\qquad
R_3=\frac{\boldsymbol1_{C_+}}{64\pi^2}.
\]
The first two mean the explicitly defined noncritical coordinate distributions there. Globally they mean the already constructed \(R_1,R_2\), including their vertex behavior.

For the remaining indices write \(j=m+2\). Formula (1.2) and \(\Gamma(m+1)=m!\) give the density
\[
R_{m+3}
=\frac{2^{-2m-5}}{\pi^2(m+2)!m!}
\boldsymbol1_{C_+}q^m.
\]
Hence the full global decomposition is
\[
\begin{gathered}
F_a=R_1+aR_2+
\frac{a^2\boldsymbol1_{C_+}}{32\pi^2}\mathcal B_2(aq/4),\\
\mathcal B_2(z)=\sum_{m=0}^{\infty}\frac{z^m}{m!(m+2)!}.
\end{gathered}
\]
The ratio for successive absolute terms is \(|z|/[(m+1)(m+3)]\). The same geometric-tail and derivative argument as in Theorem 2.1 proves entire dependence and local uniform convergence. The regular tail is a locally bounded density, beginning with \(a^2\boldsymbol1_{C_+}/(64\pi^2)\).

If \(a\ne0\), its interior profile \(r\mapsto a^2\mathcal B_2(ar/4)/(32\pi^2)\) is entire and nonzero at \(r=0\). Solution 1's interval argument shows that every cone-interior open set meets a nonzero density point. The singular layers vanish in the interior, so cannot cancel this density. The exact support is \(C_+\). For \(a=0\), only \(R_1\) remains, whose exact boundary support is Theorem 1.1.

**Solution 5.** Compute the actual complex squares:
\[
\begin{gathered}
a=i^2-(1+i)^2-2^2-3i=-5-5i,\\
\ell=-it+(1+i)x_1+2x_2.
\end{gathered}
\]
The inverse is \(e^\ell F_{-5-5i}\), explicitly
\[
F=\frac{e^{-it+(1+i)x_1+2x_2}\boldsymbol1_{\{t>|x|\}}}
{2\pi\sqrt q}\mathcal C((-5-5i)q).
\]
Absolute squares instead give \(\widetilde a=1-2-4-3i=-5-3i\). For \(\widetilde F=e^\ell F_{\widetilde a}\), the true conjugation formula gives
\[
\begin{aligned}
P\widetilde F
&=e^\ell(\Box-a)F_{\widetilde a}\\
&=\delta+(\widetilde a-a)\widetilde F
=\delta+2i\widetilde F.
\end{aligned}
\]
This error is nonzero: \(F_{\widetilde a}\) has full cone support by the interval argument of Solution 1, since \(\mathcal C(0)=1\); the exponential is nowhere zero. The erroneous candidate therefore fails the point-source equation.

**Solution 6.** Let \(A(t,x_1,x_2)=(t,x_1/2,x_2/3)\), whose absolute determinant is \(1/6\). U027's proved linear distribution formula gives
\[
F_G=\tfrac16 A^*F_a,\qquad
F_G(\psi)=F_a\bigl((t,y)\longmapsto\psi(t,2y_1,3y_2)\bigr).
\]
This last pairing also verifies normalization directly. The chain rule transforms the adjoint test operator into \(\partial_t^2-\Delta_y-a\), so applying the anisotropic operator to \(F_G\) gives \(\psi(0)\). Equivalently \(A^*\delta=6\delta\), canceled by \(1/6\).

With
\[
q_G=t^2-x_1^2/4-x_2^2/9,\qquad
C_G=\{t\ge\sqrt{x_1^2/4+x_2^2/9}\},
\]
the density is
\[
F_G=\frac{\boldsymbol1_{\{t>\sqrt{x_1^2/4+x_2^2/9}\}}}
{12\pi\sqrt{q_G}}\mathcal C(aq_G).
\]
It is locally integrable by the invertible linear substitution in (2.9). The same map sends \(C_G\) onto \(C_+\), so properness of addition transfers to \(C_G\). The derivative-transfer inverse argument proves uniqueness on that cone. Its support is exactly \(C_G\), by the entire-profile argument and the homeomorphism \(A\).

**Solution 7.** Proper cone addition defines the convolution and keeps its support in \(C_+\). Transferring each group of derivatives to the designated factor gives
\[
\begin{aligned}
\Box^{p+q+2}(E_p*E_q)
&=(\Box^{p+1}E_p)*(\Box^{q+1}E_q)\\
&=\delta*\delta=\delta.
\end{aligned}
\]
Theorem 1.1 proves \(E_p*E_q=E_{p+q+1}\).

For the direct line calculation write \(\xi=t-x\), \(\eta=t+x\), so \(dt\,dx=\tfrac12d\xi\,d\eta\), \(q=\xi\eta\), and the cone is \(\xi,\eta\ge0\). The integrand for \(E_0*E_0\) is \(1/4\) where both characteristic pairs are nonnegative. For output \(\xi,\eta\ge0\), the intermediate pair ranges over \([0,\xi]\times[0,\eta]\). Thus
\[
(E_0*E_0)(t,x)
=\tfrac14\cdot\tfrac12\,\xi\eta
=\frac{\boldsymbol1_{C_+}q}{8}=E_1
\]
inside the cone, and it is zero outside. The bounded rectangle makes the integral finite; its density agrees with the distributional convolution by U021's tensor integration formula. Boundary values have measure zero and do not alter this identity.

**Solution 8.** Differentiate (2.9) twice. The derivatives are justified on compact tests by the summable series bounds already proved; equivalently the differentiated scalar series is dominated by a constant times \(q^{-1/2}\) on every compact cone region. This gives
\[
G_{a,2}=\tfrac12\partial_a^2F_a
=\frac{\boldsymbol1_{\{t>|x|\}}q^{3/2}}{4\pi}\mathcal C''(aq).
\]
Corollary 2.2 proves the global equation \((\Box-a)^3G_{a,2}=\delta\) and uniqueness with cone support.

The coefficient of \(z^2\) in \(\mathcal C\) is \(1/4!\), so \(\mathcal C''(0)=2/4!=1/12\). Hence
\[
G_{0,2}=\frac{\boldsymbol1_{C_+}q^{3/2}}{48\pi}=R_3.
\]
Indeed \(\Gamma(3)=2\), \(\Gamma(5/2)=3\sqrt\pi/4\), and (1.2) gives the same coefficient. This is the inverse with point-source coefficient one.

## Free sources and exact proof dependencies

- Christian Bär, Nicolas Ginoux and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, freely accessible author version, [arXiv:0806.1036](https://arxiv.org/abs/0806.1036), §1.2, Lemma 1.2.2 and Proposition 1.2.4, printed pp.10–17. The actual continuation and vertex proofs were read. Their parameter \(\alpha\) is \(2\lambda\) here, and their dimension is spacetime dimension \(n+1\). U027 Lemma 4.0 supplies the complete programme proof, including the scalar identities for which the source refers elsewhere.
- [U027](causal-point-sources-and-characteristic-cones.md), Lemma 4.0 and formulas (4.0a)–(4.0h), proves the global family, all constants, origin delta and linear substitution. [U022](causal-integration-of-complex-order.md), §1, formulas (1.3)–(1.6), and Theorems 2.1–2.2, proves the scalar causal family and Beta input. [U021](convolution-as-addition-of-supports.md), Theorems 1.1, 3.1–3.2 and Corollary 3.4, proves the used convolution and continuity statements.
- The nonvertex cone coordinates, exact supports, uniform potential series, all parameter derivatives, resolvent and higher-power identities, exponential conjugation and all eight solutions are proved here. No external citation replaces these proofs.
