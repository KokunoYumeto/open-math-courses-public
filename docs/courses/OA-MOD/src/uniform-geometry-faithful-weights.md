# Uniform geometry of faithful weights

The Connes cocycle can compare weights by more than its real-time values. A
contractive continuation through a lower strip defines an order, and allowing
all strip widths produces an extended metric on faithful normal semifinite
weights. We prove the order and metric arguments, identify the trace-density
model, correct a factor of two in the printed model, and prove completeness.

The source section fixes a separable properly infinite von Neumann algebra.
The arguments below use neither restriction: throughout, \(M\) is a von
Neumann algebra and \(\mathcal W_0(M)\) is its set of faithful normal semifinite
weights. The trace model separately assumes that \(M\) is semifinite. The
positive Fourier convention is fixed by its action on a single frequency.
The two spectral applications below use a real-line Fourier-algebra proof
and explicit contour and Poisson arguments. The half-strip domination theorem is
proved in HS05;
UW02 below checks the boundary continuity required by our definition.

## Contractive strips form an order

For \(\lambda>0\), put

\[
 \begin{aligned}
 S_\lambda
 &=\{z\in\mathbb C:\\
 &\qquad-\lambda\leq\Im z\leq0\}.
 \end{aligned}
 \tag{UW.1}
\]

For \(\varphi,\psi\in\mathcal W_0(M)\), write
\(\varphi\preceq_\lambda\psi\) when

\[
 u_t=[D\varphi:D\psi]_t
 \tag{UW.2}
\]

has a sigma-strongly continuous extension to \(S_\lambda\), holomorphic in
its interior, such that

\[
 \|u_z\|\leq1\qquad(z\in S_\lambda).
 \tag{UW.3}
\]

Local boundedness and scalar holomorphy make the interior extension
norm-holomorphic by the norming-predual argument in CX-03. Consequently,
products of two such extensions are holomorphic.

For each fixed \(\lambda\), the relation \(\preceq_\lambda\) is an order.
Reflexivity follows from \([D\varphi:D\varphi]_t=1\). If
\(\varphi_1\preceq_\lambda\varphi_2\) and
\(\varphi_2\preceq_\lambda\varphi_3\), the ordered chain rule gives

\[
 \begin{aligned}
 {}[D\varphi_1:D\varphi_3]_t
 &= [D\varphi_1:D\varphi_2]_t\\
 &\quad\cdot[D\varphi_2:D\varphi_3]_t.
 \end{aligned}
 \tag{UW.4}
\]

The product of the two strip extensions is contractive, proving
transitivity.

For antisymmetry, suppose both directions hold and denote the two lower-strip
extensions by \(u_z\) and \(v_z\). On the real axis,
\(v_t=u_t^*\). Let \(\omega\) be a normal state. The two scalar functions

\[
 \begin{gathered}
 \omega(v_z)\quad(\Im z\leq0),\\
 \overline{\omega(u_{\bar z})}\quad(\Im z\geq0).
 \end{gathered}
 \tag{UW.5}
\]

have equal boundary values and glue across the real axis. The elementary
Morera gluing argument from MA-08 makes the result holomorphic on
\(-\lambda<\operatorname{Im}z<\lambda\). Its modulus is at most one, while
its value at zero is one. The maximum-modulus principle therefore makes it
constant. Hence \(\omega(v_t)=1\) for every normal state and every real \(t\).
Normal states separate \(M\), so \(v_t=1\). Fixed-reference cocycle
injectivity in CX-10 gives \(\varphi_1=\varphi_2\).

Write

\[
 \begin{gathered}
 \varphi\preceq_\infty\psi\\
 \Longleftrightarrow\\
 \varphi\preceq_\lambda\psi\quad(\lambda>0).
 \end{gathered}
 \tag{UW.6}
\]

The extensions for different widths agree on overlaps by scalar analytic
uniqueness. Thus (UW.6) is equivalently a contractive holomorphic extension
of (UW.2) to the closed lower half-plane.

## The half-strip recovers pointwise order

The weight-domination theorem HS05
has the following exact form. If \(\alpha,\beta\in\mathcal W_0(M)\) and
\(C>0\), then

\[
 \alpha(x)\leq C\,\beta(x)
 \quad(x\in M_+)
 \tag{UW.7}
\]

is equivalent to continuation of \([D\alpha:D\beta]_t\) through the strip
\(-1/2\leq\operatorname{Im}z\leq0\), with lower-boundary norm at most
\(C^{1/2}\). HS05 proves both implications on the full positive cone,
including infinite values, and gives the bound \(C^y\) at height \(-y\).
Its construction uses the balanced matrix weight and the complete
fixed-operator strip proof in HS01–04.

We must also verify sigma-strong continuity on the boundary: the statement
of HS05 initially specifies sigma-weak continuity. Here is the needed
strengthening of HS01.
Use its notation \(D>0\), \(s>0\), and bounded \(a,b\), with
\[
 \begin{gathered}
 aD(D^s)\subseteq D(D^s),\\
 D^sa\xi=bD^s\xi
 \quad(\xi\in D(D^s)).
 \end{gathered}
\]
Thus \(a\) acts continuously on \(D(D^s)\) with its graph norm.
For a spectral-band vector \(\xi\), the HS01 extension satisfies
\[
 \begin{gathered}
 F(t-iu)\xi\\
 =D^{it+u}aD^{-it-u}\xi,\\
 0\leq u\leq s.
 \end{gathered}
\]
The vector \(D^{-it-u}\xi\) varies continuously in that graph norm,
because its spectral support lies in a compact subinterval of
\((0,\infty)\). The same holds after applying \(a\).
For each fixed \(v\in D(D^s)\), spectral dominated convergence
makes \((t,u)\mapsto D^{it+u}v\) norm continuous up to both edges:
the scalar multipliers obey \(r^u\leq1+r^s\) for \(r>0\).
This bound also controls a varying \(v\) in graph norm. Hence
\(F(t-iu)\xi\) is jointly norm continuous for every band vector.
The strip's uniform operator bound and density of the band vectors
extend this conclusion to every vector in the Hilbert space.
It gives sigma-strong continuity as well: truncate a square-summable
vector family to finitely many vectors, and bound its remaining tail
uniformly by the common operator norm.

Apply this to the balanced modular operator and matrix unit used in
HS05. The cocycle extension is its indicated matrix entry, so it is
sigma-strongly continuous on the entire closed half-strip. Conversely,
a bounded sigma-strongly continuous extension is sigma-weakly continuous,
and HS05 applies to it. Thus the theorem has exactly the boundary
topology required in UW01, without assuming norm-continuous real orbits.

Taking \(C=1\) gives the precise bridge

\[
 \boxed{
 \begin{gathered}
 \alpha\preceq_{1/2}\beta\\
 \Longleftrightarrow\\
 \alpha(x)\leq\beta(x)\quad(x\in M_+).
 \end{gathered}}
 \tag{UW.8}
\]

All values in (UW.7)--(UW.8) are extended nonnegative values. No subtraction
of infinite weights is involved.

## Infinite strips and the balanced spectral subspace

Let \(\Phi=\varphi_1\oplus\varphi_2\) be the balanced weight on
\(N=M\mathbin{\overline\otimes}M_2\). The balanced-matrix formula SI-14 gives

\[
 \begin{aligned}
 \sigma_t^\Phi(1\otimes e_{12})
 &=[D\varphi_1:D\varphi_2]_t\\
 &\quad\otimes e_{12}.
 \end{aligned}
 \tag{UW.9}
\]

We use the positive Fourier convention: if \(f=\mathcal F b\), then

\[
 \begin{aligned}
 f(p)&=\int_{\mathbb R}e^{ipt}b(t)\,dt,\\
 \gamma_f(x)&=\int_{\mathbb R}b(t)\gamma_t(x)\,dt.
 \end{aligned}
 \tag{UW.50}
\]

The operator integral is weak-star. **The real-line Fourier algebra and its filters.** We prove the precise filter facts used here. The scalar Fourier transform, its Schwartz inversion, smooth cutoffs, and continuity of translations in \(L^1\) are established in BI-02–03. The argument below concerns the Fourier-algebra hull spectrum, rather than assuming its equality with a smooth-test definition.

For \(a,b\in L^1(\mathbb R)\), scalar Fubini gives
\[
\|a*b\|_1\leq\|a\|_1\|b\|_1,
\qquad\mathcal F(a*b)=(\mathcal Fa)(\mathcal Fb).
\]
The transform is injective. Indeed, if \(\mathcal Fa=0\) and \(\rho\in C_c^\infty\), Schwartz inversion and Fubini give
\[
\begin{aligned}
(a*\rho)(t)
&=\frac1{2\pi}\int e^{-ipt}
  (\mathcal Fa)(p)(\mathcal F\rho)(p)\,dp\\
&=0.
\end{aligned}
\]
The absolute iterated integral is bounded by \(\|a\|_1\|\mathcal F\rho\|_1\). Choosing nonnegative unit-mass \(\rho\) with shrinking support gives \(a*\rho\to a\) in \(L^1\), by the translation estimate in BI-03. Thus \(a=0\).

Completeness of \(L^1\) follows directly from positive integration: from a Cauchy sequence choose a subsequence whose successive norm differences are at most \(2^{-j}\). The sum of their absolute differences is integrable by monotone convergence. The subsequence therefore converges pointwise almost everywhere, and its \(L^1\) tail is bounded by the corresponding geometric tail. The original Cauchy sequence has the same \(L^1\) limit.

Consequently
\[
A=\mathcal F(L^1(\mathbb R)),
\qquad\|\mathcal Fa\|_A=\|a\|_1
\]
is a commutative Banach algebra, with \(\|f\|_\infty\leq\|f\|_A\). Each \(f\) is continuous by scalar dominated convergence. It vanishes at infinity: approximate its inverse transform in \(L^1\) by smooth compact functions, integrate their transforms by parts, and use the uniform Fourier bound. Smooth compact functions of the frequency variable belong to \(A\), by BI-03 inversion.

We need norm density of the compactly supported members \(A_c=A\cap C_c(\mathbb R)\). Fix \(\chi\in C_c^\infty\) with \(\chi(0)=1\), and let \(k=\mathcal F^{-1}\chi\). For \(\chi_n(p)=\chi(p/n)\), its inverse transform is \(k_n(t)=n k(nt)\) and \(\int k=1\). If \(f=\mathcal Fa\), then \(f\chi_n\in A_c\) and
\[
\begin{aligned}
\|f\chi_n-f\|_A
&=\|a*k_n-a\|_1\\
&\leq\int |k(s)|
 \|a(\,\cdot-s/n)-a\|_1\,ds
\longrightarrow0.
\end{aligned}
\]
Translation continuity and the integrable bound \(2\|a\|_1|k(s)|\) justify this limit. Positivity of \(k\) is not required.

Let \(X=E^*\), and suppose \(\alpha_t\) is a uniformly bounded weak-star continuous group with norm-continuous predual orbits. Put \(C_\alpha=\sup_t\|\alpha_t\|\), and write \(\beta_t\eta=\eta\circ\alpha_t\) for its predual action. For compact continuous \(a\), the norm integration construction defines
\[
B_a\eta=\int a(t)\beta_t\eta\,dt,
\qquad\|B_a\|\leq C_\alpha\|a\|_1.
\]
Completion extends \(B_a\) to every \(a\in L^1\). Define \(\alpha_f=B_a^*\) for \(f=\mathcal Fa\). Injectivity of the transform makes this unambiguous. It gives exactly the weak-star integral in (UW.50), a weak-star continuous map with
\(\|\alpha_f\|\leq C_\alpha\|f\|_A\).
Compact-rectangle Fubini on the predual, followed by \(L^1\) approximation, proves
\[
\alpha_f\alpha_g=\alpha_{fg}.
\]
The group law and translation of the inverse kernel also show that these filters commute with every \(\alpha_t\).

For the preceding \(\chi_n\), predual norm continuity gives
\[
\begin{aligned}
\|B_{k_n}\eta-\eta\|
&\leq\int |k(s)|\,
 \|\beta_{s/n}\eta-\eta\|\,ds\\
&\longrightarrow0.
\end{aligned}
\]
Thus \(\alpha_{\chi_n}x\to x\) weak-star. In particular, if every Fourier filter kills \(x\), then \(x=0\). This argument does not assume norm continuity of the orbit of \(x\).

**Local inversion in the actual algebra norm.** Suppose \(h=\mathcal Fa\) and \(h(p_0)=h_0\ne0\). Choose a smooth compact \(u\) equal to one near zero, put \(k=\mathcal F^{-1}u\), and set
\[
u_\varepsilon(p)=u((p-p_0)/\varepsilon),
\qquad
k_\varepsilon(t)=\varepsilon e^{-ip_0t}k(\varepsilon t).
\]
Then \(\mathcal Fk_\varepsilon=u_\varepsilon\). Subtracting the inverse transforms of \(hu_\varepsilon\) and \(h_0u_\varepsilon\) gives
\[
\begin{aligned}
\|(h-h_0)u_\varepsilon\|_A
&\leq\int |a(s)|\,
 \|k(\,\cdot-\varepsilon s)-k\|_1\,ds\\
&\longrightarrow0.
\end{aligned}
\]
To see the phase, \(k_\varepsilon(t-s)=e^{ip_0s}\varepsilon e^{-ip_0t}k(\varepsilon t-\varepsilon s)\), while \(h_0=\int a(s)e^{ip_0s}\,ds\). The phases have modulus one. Translation continuity and the bound \(2\|k\|_1|a(s)|\) prove the limit.

Use the unitization \(A^+=\mathbb C1\oplus A\) with norm \(|c|+\|f\|_A\). Choose \(\varepsilon\) so that \(q=(h-h_0)u_\varepsilon\) has norm less than \(|h_0|\). The convergent geometric series
\[
d^{-1}=h_0^{-1}\sum_{j=0}^{\infty}(-q/h_0)^j,
\qquad d=h_0 1+q,
\]
is an inverse in \(A^+\): multiplication of its partial sums by \(d\) leaves a remainder tending to zero in norm. Since \(A\) is an ideal of \(A^+\), the element \(v=u_\varepsilon d^{-1}\) belongs to \(A\). On a neighborhood of \(p_0\), we have \(u_\varepsilon=1\), \(d=h\), and hence \(hv=1\). This proves local inversion without replacing the \(A\) norm by the uniform norm.

**Local ideals, empty spectrum, and support.** For a closed ideal \(J\subset A\), let
\[
h(J)=\{p:f(p)=0\text{ for every }f\in J\}.
\]
If \(f\in A_c\) has support disjoint from \(h(J)\), then \(f\in J\). For each point of its compact support, choose \(h_j\in J\) nonzero there. The local inverse construction gives \(v_j\in A\) with \(h_jv_j=1\) on a neighborhood of that point. Choose finitely many such neighborhoods covering the support and a smooth compact partition \(q_j\) subordinate to them, with \(\sum_jq_j=1\) near the support; the cutoff and finite-partition construction is in BI-03. Then
\[
f=\sum_jfq_j=\sum_j h_j(v_jfq_j)\in J.
\]
Only compact supports disjoint from the hull are treated. No assertion that every function vanishing on the hull belongs to \(J\) is used.

Set \(I_\alpha(x)=\{f\in A:\alpha_fx=0\}\). The norm bound and product identity make it a closed ideal. Define \(\operatorname{Sp}_\alpha(x)=h(I_\alpha(x))\). If that hull is empty, the preceding lemma gives \(A_c\subset I_\alpha(x)\). Density gives \(I_\alpha(x)=A\), and \(\alpha_{\chi_n}x\to x\) then gives \(x=0\). Conversely \(x=0\) has empty spectrum, since a smooth compact function can be nonzero at any specified point.

For every \(f\in A\), the product identity gives \(I_\alpha(x)\subset I_\alpha(\alpha_fx)\). If \(p\notin\operatorname{supp}f\), a smooth compact function \(g\) supported away from \(\operatorname{supp}f\), with \(g(p)=1\), has \(gf=0\); thus it annihilates \(\alpha_fx\). These two observations prove
\[
\operatorname{Sp}_\alpha(\alpha_fx)
\subseteq\operatorname{Sp}_\alpha(x)
\cap\operatorname{supp}f.
\]
The support of \(f\) need not be compact. In particular, disjoint support and spectrum make the filter zero, by the empty-spectrum result just proved. Multiplying the group by \(e^{-i\delta t}\) translates the spectrum by \(-\delta\): its \(f\)-filter is the original group's filter for \(p\mapsto f(p-\delta)\), an isometric automorphism of \(A\).

These hypotheses apply to the modular action used here and to its phase translates. On its faithful GNS representation, the action is conjugation by the strongly continuous group \(\Delta^{it}\). For vector functionals, predual norm continuity follows from
\(\|\omega_\xi-\omega_\eta\|\leq(\|\xi\|+\|\eta\|)\|\xi-\eta\|\).
The norm-convergent vector expansions of SC-02 give it for all normal functionals by a finite head and a uniformly bounded tail. The action also has sigma-strong-star continuous element orbits. Multiplication by the continuous scalar phase preserves the predual condition. Nothing here requires a separable representation.

For the orbit
\(\gamma_t(x)=e^{i\nu t}x\), with \(x\ne0\), (UW.50) gives
\(\gamma_f(x)=f(\nu)x\), so its spectrum is \(\{\nu\}\).
Smooth compactly supported Fourier functions separate any other point
from \(\nu\), proving both inclusions in this hull equality.
Since
\(|e^{i\nu(t-is)}|=e^{\nu s}\), boundedness below the real axis selects
\(\nu\leq0\) in the filter spectrum.

We now prove the half-plane criterion using this filter calculus.

**A bounded lower extension excludes positive frequencies.** Suppose
\(F(t)=\gamma_t(x)\) extends holomorphically below the real axis, with
\(\|F(z)\|\leq C\), and has its weak-star continuous boundary values.
For \(f\in C_c^\infty(\mathbb R)\) supported in \((c,\infty)\), \(c>0\), set

\[
 \begin{gathered}
 b_f(z)\\
 =\frac1{2\pi}\int e^{-ipz}f(p)\,dp.
 \end{gathered}
 \tag{UW.51}
\]

This is entire. Two integrations by parts in \(p\), together with the
undifferentiated estimate for \(|t|\leq1\), give

\[
 \begin{gathered}
 \int |b_f(t-is)|\,dt\\
 \leq C_f(1+s)^2e^{-cs},\\
 s\geq0.
 \end{gathered}
 \tag{UW.52}
\]

In particular \(b_f\in L^1(\mathbb R)\) and \(\mathcal F b_f=f\).
This is exactly the Schwartz inversion proved in BI-03; it uses scalar
Fubini and a Gaussian approximate identity. No distributional inversion
or closed-set spectral synthesis is assumed.

For a normal functional \(\omega\), shift the contour of
\(b_f(z)\omega(F(z))\) down by \(s\). Its vertical integrals vanish:
on any fixed horizontal strip the two integrations by parts give
\(O(|\operatorname{Re}z|^{-2})\), and \(F\) is bounded.
If the boundary is only weak-star continuous, first start at depth
\(\eta>0\), then pass to \(\eta\downarrow0\) by the same integrable bound.
Consequently

\[
 \begin{gathered}
 |\omega(\gamma_f x)|\\
 \leq C\|\omega\|C_f(1+s)^2e^{-cs}\\
 \longrightarrow0\quad(s\to\infty).
 \end{gathered}
 \tag{UW.53}
\]

Normal functionals separate the algebra, so every such filter kills \(x\).
At each \(p>0\) choose such an \(f\) with \(f(p)\ne0\).
It belongs to the annihilator ideal and excludes \(p\) from its hull.
Hence \(\operatorname{Sp}_\gamma(x)\subseteq(-\infty,0]\).

**Negative spectrum supplies the contractive extension.** Now let
\(\gamma\) be an automorphism flow with sigma-strong-star continuous
element orbits and norm-continuous predual orbits, and assume that spectrum
inclusion. The preceding argument verifies both continuity properties for
every modular flow, which is the case needed for arbitrary weights here. For \(s>0\), put

\[
 \begin{gathered}
 P_s(r)=\frac{s}{\pi(s^2+r^2)},\\
 \int P_s(r)\,dr=1,\\
 \mathcal F P_s(p)=e^{-s|p|}.
 \end{gathered}
 \tag{UW.54}
\]

The mass identity is the elementary arctangent integral. For \(p>0\),
integrate \(e^{ipz}s/(\pi(z^2+s^2))\) on the rectangle with vertices
\(-R,R,R+iR,-R+iR\), where \(R>s\). The two vertical integrals are
\(O(R^{-1})\); the upper integral is \(O(R^{-1}e^{-pR})\).
The only pole inside is \(is\), with coefficient
\(e^{-ps}/(2\pi i)\). Subtract that simple-pole term and apply the
rectangle Cauchy formula to obtain the real integral \(e^{-ps}\).
For \(p<0\) use the lower rectangle, with clockwise orientation and pole
\(-is\), giving \(e^{sp}\). This proves (UW.54) using the scalar rectangle
Cauchy input, without importing an arbitrary-cycle residue theorem.
Both \(\partial_sP_s\) and \(P_s'\) are in \(L^1\), locally continuously
in \(s>0\), as their explicit rational formulas show.

Define the weak-star Poisson integral

\[
 \begin{gathered}
 F(t-is)\\
 =\int P_s(r)\gamma_{t-r}(x)\,dr.
 \end{gathered}
 \tag{UW.55}
\]

Positivity and unit mass give \(\|F(t-is)\|\leq\|x\|\).
We verify holomorphy without assuming spectral synthesis at zero.
For \(\delta>0\), use the dual Banach action
\(\beta_t^\delta=e^{-i\delta t}\gamma_t\). It is isometric and has
continuous predual orbits; it need not be an automorphism action.
The frequency-translation identity proved above gives
\(\operatorname{Sp}_{\beta^\delta}(x)
=\operatorname{Sp}_\gamma(x)-\delta\subseteq(-\infty,-\delta]\).
This also follows directly from (UW.50) by translating the Fourier function.
Let \(F_\delta\) be (UW.55) with \(\gamma\) replaced by \(\beta^\delta\).
Writing its kernel as \(P_s(t-v)\) makes both derivatives norm derivatives:
the difference quotients converge in \(L^1\), and the action is bounded.
The kernel for \(\partial_sF_\delta+i\partial_tF_\delta\), written as
a filter of \(\beta^\delta_t(x)\), is

\[
 \begin{gathered}
 K_s(v)\\
 =\partial_sP_s(v)-iP_s'(v),\\
 \mathcal F K_s(p)\\
 =-(|p|+p)e^{-s|p|}.
 \end{gathered}
 \tag{UW.56}
\]

Its Fourier support is contained in \([0,\infty)\), disjoint from
\(\operatorname{Sp}_{\beta^\delta}(x)\).
The filter-support inclusion and empty-spectrum criterion proved above
therefore make this filter zero. Thus
\(\partial_sF_\delta+i\partial_tF_\delta=0\), the Cauchy--Riemann equation
for \(z=t-is\). Continuous norm derivatives prove norm holomorphy.
Put \(E_\delta=F_\delta(t-is)-F(t-is)\). The integral and (UW.54),
with Cauchy--Schwarz for the probability measure \(P_s(r)\,dr\), give

\[
 \begin{aligned}
 &\|E_\delta\|\\
 &\leq\|x\|\delta|t|\\
 &\quad+\|x\|\sqrt{2(1-e^{-\delta s})}.
 \end{aligned}
 \tag{UW.57}
\]

This tends to zero uniformly on every compact subset of the lower
half-plane. The norm limit is holomorphic and retains its norm bound.

In a faithful normal representation, the vector integral corresponding to
(UW.55) exists: each continuous vector orbit on \(\mathbb R\) is separable
and bounded. Put \(Y=F(t-is)-\gamma_{t_0}(x)\) and
\(D(r)=\gamma_{t-r}(x)-\gamma_{t_0}(x)\). Jensen's inequality gives

\[
 \begin{gathered}
 \|Y\xi\|^2\\
 \leq\int P_s(r)\|D(r)\xi\|^2\,dr.
 \end{gathered}
 \tag{UW.58}
\]

As \((t,s)\to(t_0,0)\), split the integral at a small fixed
\(|r|\). Strong continuity controls the part near zero; the remaining
Poisson mass tends to zero, with integrand at most
\(4\|x\|^2\|\xi\|^2\). The same argument for \(x^*\) gives
strong-star continuity. Uniform boundedness makes this sigma-strong-star
continuity as well: each summable family of vector seminorms is handled
by a finite head and its uniformly bounded tail.
Thus (UW.55) has the required boundary regularity, without a separability
assumption on the algebra or its representation.

Apply both directions to \(\gamma=\sigma^\Phi\) and
\(x=1\otimes e_{12}\). Every integrand in (UW.55) remains in the
12-corner by (UW.9), so the extension has the form \(u_z\otimes e_{12}\).
The corner embedding is isometric and preserves the boundary topology.
We obtain the corrected equivalence

\[
 \boxed{
 \begin{gathered}
 \varphi_1\preceq_\infty\varphi_2\\
 \Longleftrightarrow\\
 \operatorname{Sp}_{\sigma^\Phi}(1\otimes e_{12})\\
 \subseteq(-\infty,0].
 \end{gathered}}
 \tag{UW.10}
\]

Taking adjoints instead gives the positive half-line for \(e_{21}\).
Indeed the filter identity for \(x^*\) replaces \(f(p)\) by
\(\overline{f(-p)}\), so its annihilator hull is reflected.
Using the positive half-line for \(e_{12}\) would instead contradict
the eigenvector calculation in this convention.

**A complete scalar sign test.** Take \(M=\mathbb C\),
\(\psi(r)=r\) and \(\varphi(r)=r/2\) for \(r\geq0\).
These are faithful normal finite weights. The balanced density on
\(M_2(\mathbb C)\) is \(\operatorname{diag}(1/2,1)\) relative to its
usual trace. Hence

\[
 \begin{gathered}
 u_t=2^{-it},\\
 |u_{t-is}|=2^{-s}\leq1,\\
 \operatorname{Sp}_{\sigma^\Phi}(e_{12})
 =\{-\log2\}.
 \end{gathered}
 \tag{UW.59}
\]

Thus \(\varphi\preceq_\infty\psi\), while the positive
half-line condition fails. The adjoint \(e_{21}\) has frequency \(\log2\).
For equal weights the frequency is zero, retained by both closed
half-lines. The zero vector has empty spectrum by the filter argument above.

## The extended uniform distance

Scaling a weight changes the cocycle by

\[
 \begin{aligned}
 {}[D(c\varphi):D(d\psi)]_t
 &=(c/d)^{it}\\
 &\quad\cdot[D\varphi:D\psi]_t,\\
 &\hspace{5em}c,d>0.
 \end{aligned}
 \tag{UW.11}
\]

Define

\[
 \begin{aligned}
 d(\varphi,\psi)
 &=\inf\bigl\{a>0:\\
 &\quad e^{-a}\psi\preceq_\infty\varphi,\\
 &\quad \varphi\preceq_\infty e^a\psi
 \bigr\}.
 \end{aligned}
 \tag{UW.12}
\]

This is an extended metric. Multiplying both weights in a comparison by the
same positive scalar leaves its cocycle unchanged. Hence the two inequalities
in (UW.12), after reciprocal rescaling, also give

\[
 e^{-a}\varphi\preceq_\infty\psi
 \preceq_\infty e^a\varphi,
 \tag{UW.13}
\]

which proves symmetry. If \(a\) and \(b\) are admissible for
\((\varphi,\psi)\) and \((\psi,\chi)\), respectively, transitivity gives

\[
 \begin{gathered}
 e^{-(a+b)}\chi\preceq_\infty\varphi,\\
 \varphi\preceq_\infty e^{a+b}\chi.
 \end{gathered}
 \tag{UW.14}
\]

Taking infima proves the triangle inequality. If \(d(\varphi,\psi)=0\),
(UW.8) gives, for every \(a>0\),

\[
 e^{-a}\psi\leq\varphi\leq e^a\psi.
 \tag{UW.15}
\]

Letting \(a\downarrow0\) at each positive element, including an infinite
value, gives \(\varphi=\psi\).

If \(d(\varphi,\psi)<a\), the cocycle

\[
 U_t=[D\psi:D\varphi]_t
 \tag{UW.16}
\]

extends to an entire \(M\)-valued function satisfying

\[
 \|U_z\|\leq e^{a|\operatorname{Im}z|}.
 \tag{UW.17}
\]

Indeed, the two comparisons in (UW.12) give compatible extensions in the
lower and upper half-planes after applying (UW.11); they glue across the real
axis. The scalar factor in (UW.11) gives exactly the exponential in
(UW.17). The topology defined by \(d\) is the **uniform topology** on
\(\mathcal W_0(M)\).

## Trace densities and the factor-of-two correction

Let \(M\) be semifinite, let \(\tau\) be a faithful normal semifinite trace,
and let \(h,k\) be positive injective self-adjoint operators affiliated with
\(M\). Put

\[
 \varphi=\tau_h,
 \qquad
 \psi=\tau_k.
 \tag{UW.18}
\]

The density convention is the one in PT-08, so that

\[
 [D\varphi:D\psi]_t=h^{it}k^{-it}.
 \tag{UW.19}
\]

For \(\lambda>0\), rescale time by \(2\lambda\). The function

\[
 \begin{aligned}
 w_t
 &=[D\varphi:D\psi]_{2\lambda t}\\
 &=h^{2\lambda it}k^{-2\lambda it}\\
 &=[D\tau_{h^{2\lambda}}
   :D\tau_{k^{2\lambda}}]_t.
 \end{aligned}
 \tag{UW.20}
\]

has a contractive half-strip extension exactly when the cocycle in (UW.19)
has a contractive strip of width \(\lambda\). Equations (UW.8) and PT-08's
order-preserving density correspondence therefore prove

\[
 \boxed{
 \begin{gathered}
 \varphi\preceq_\lambda\psi\\
 \Longleftrightarrow\\
 h^{2\lambda}\leq k^{2\lambda}.
 \end{gathered}}
 \tag{UW.21}
\]

The printed XII.5.6 omits the factor \(2\) in (UW.21). Its formula cannot be
reconciled with the half-strip identity (UW.8). A concrete obstruction occurs
in \(M_2(\mathbb C)\). Let

\[
 \begin{aligned}
 h&=\begin{pmatrix}2&0\\0&1\end{pmatrix},\\
 k&=\begin{pmatrix}3&1\\1&2\end{pmatrix}.
 \end{aligned}
 \tag{UW.22}
\]

Then \(k-h\) is the positive rank-one matrix with every entry equal to one,
but

\[
 \begin{gathered}
 k^2-h^2=
 \begin{pmatrix}6&5\\5&4\end{pmatrix},\\
 \det(k^2-h^2)=-1.
 \end{gathered}
 \tag{UW.23}
\]

Thus \(h\leq k\) while \(h^2\nleq k^2\). At \(\lambda=1\), the printed
criterion would accept this pair, whereas the defining strip and (UW.8)
correctly reject it.

The infinite-width conclusion printed after that formula remains valid. If
\(p(s)=1_{[0,s]}(h)\) and \(q(s)=1_{[0,s]}(k)\), then

\[
 \begin{gathered}
 \varphi\preceq_\infty\psi\\
 \Longleftrightarrow h^r\leq k^r\;(r>0)\\
 \Longleftrightarrow h^n\leq k^n\;(n\geq1)\\
 \Longleftrightarrow p(s)\geq q(s)\;(s\geq0).
 \end{gathered}
 \tag{UW.24}
\]

Only the implication from integer powers to spectral projections needs care.
If \(\xi\in q(s)H\) and \(\mu>s\), the inequality with exponent \(2n\) gives

\[
 \begin{gathered}
 \|\mu^{-n}h^n\xi\|^2
 \leq\|\mu^{-n}k^n\xi\|^2\\
 \leq(s/\mu)^{2n}\|\xi\|^2.
 \end{gathered}
 \tag{UW.25}
\]

The spectral theorem then puts \(\xi\) in \(p(s)H\), so \(q(s)\leq p(s)\).
Conversely, this projection order gives
\(1-p(s)\leq1-q(s)\). The layer-cake formula for quadratic forms yields,
for every \(r>0\),

\[
 \begin{aligned}
 \langle h^r\xi,\xi\rangle
 &=\int_0^\infty r s^{r-1}\\
 &\quad\cdot
 \langle(1-p(s))\xi,\xi\rangle\\
 &\qquad ds\\
 &\leq\langle k^r\xi,\xi\rangle.
 \end{aligned}
 \tag{UW.26}
\]

The equality and inequality allow the value \(+\infty\). This proves all of
(UW.24), and (UW.21) converts the all-real-power condition back to
\(\preceq_\infty\).

## Differentiable cocycles are bounded logarithmic perturbations

Keep the trace setting and put

\[
 \begin{aligned}
 H&=\log h,\\
 K&=\log k,\\
 u_t&=[D\psi:D\varphi]_t\\
 &=e^{itK}e^{-itH}.
 \end{aligned}
 \tag{UW.27}
\]

The map \(t\mapsto u_t\) is sigma-strong-star differentiable if and only if

\[
 \begin{gathered}
 K=H+a,\\
 D(H)=D(K).
 \end{gathered}
 \tag{UW.28}
\]

for a bounded self-adjoint \(a\in M\).

Suppose first that the derivative at zero exists. Differentiating
\(u_t^*u_t=1\) shows that \(u'_0=ia\) for a bounded self-adjoint \(a\).
For \(\xi\in D(H)\), the identity

\[
 e^{itK}\xi=u_t e^{itH}\xi
 \tag{UW.29}
\]

has a strong derivative at zero. Stone's exact derivative-domain theorem
SG-04 gives \(\xi\in D(K)\) and \(K\xi=(H+a)\xi\). Applying the same argument
to \(e^{itH}=u_t^*e^{itK}\) gives the reverse domain inclusion. This proves
(UW.28).

Conversely, a bounded self-adjoint perturbation preserves self-adjointness
and the domain. The cocycle identity and the derivative at zero give the
strong-star differential equation

\[
 \begin{gathered}
 u'_t=i\,u_t\sigma_t^\varphi(a),\\
 u_0=1.
 \end{gathered}
 \tag{UW.30}
\]

and hence

\[
 u_t=1+i\int_0^t
 u_s\sigma_s^\varphi(a)\,ds.
 \tag{UW.31}
\]

The integral is sigma-strong-star. Iteration gives the time-ordered Dyson
series; its \(n\)-th term has norm at most
\(\|a\|^n|t|^n/n!\). It therefore converges in norm on compact time
intervals and verifies (UW.30), proving the converse without differentiating
an unbounded product formally.

## Uniform distance bounds the perturbation spectrum

Let \(\varphi,\psi\in\mathcal W_0(M)\) and suppose

\[
 \alpha=d(\varphi,\psi)<\infty.
 \tag{UW.32}
\]

Write \(u_t=[D\psi:D\varphi]_t\), as in (UW.16).
The entire extension in UW-04 is norm differentiable. Set
\(a=-iu'_0\in M\); differentiation of \(u_t^*u_t=1\) at zero gives
\(a=a^*\). Differentiating the cocycle identity
\(u_{t+s}=u_t\sigma_t^\varphi(u_s)\) in \(s\) at zero gives (UW.30).
In the trace-density setting of UW-06, its domain argument identifies
\(a=K-H\) on \(D(H)=D(K)\). For arbitrary weights, the bounded
cocycle derivative defines \(a\) without introducing trace densities.
For every \(\varepsilon>0\), put \(b=\alpha+\varepsilon\).
Equation (UW.17) gives

\[
 \|u_z\|
 \leq e^{(\alpha+\varepsilon)|\operatorname{Im}z|}.
 \tag{UW.33}
\]

The differential equation supplies the actual modular orbit

\[
 \sigma_t^\varphi(a)
 =-i\,u_t^*u'_t.
 \tag{UW.34}
\]

The functions \(u_t\) and \(u'_t\) are cocycle functions; they have
not been identified as orbits of fixed algebra elements. Therefore the
fixed-element spectral-product theorem does not justify a product-support
step here. We instead construct the entire continuation of (UW.34)
and prove its Fourier-filter support directly.

Put \(u^\sharp(z)=u(\bar z)^*\). This is entire: if
\(u(w)=\sum_n c_n(w-\bar z_0)^n\) near \(\bar z_0\), then
\(u^\sharp(z)=\sum_n c_n^*(z-z_0)^n\) near \(z_0\).
Its norm has the same bound as \(u\). The norm Cauchy estimate on the
circle of radius one about \(z\) gives

\[
 \|u'_z\|\leq e^b e^{b|\operatorname{Im}z|}.
 \tag{UW.60}
\]

Consequently

\[
 \begin{gathered}
 G(z)=-i\,u^\sharp(z)u'_z,\\
 G(t)=\sigma_t^\varphi(a),\\
 \|G(z)\|\leq e^b e^{2b|\operatorname{Im}z|}.
 \end{gathered}
 \tag{UW.61}
\]

Both factors are norm holomorphic and multiplication is a bounded bilinear
map, so \(G\) is entire. The reflection in \(u^\sharp\) is essential;
\(z\mapsto u(z)^*\) alone would not be holomorphic.

Take \(f\in C_c^\infty(\mathbb R)\) supported in \((c,\infty)\),
where \(c>2b\), and use its inverse Fourier function \(b_f\) from
(UW.51). The inversion and integrability proved in UW-03 make
\(\sigma_f^\varphi(a)\) exactly the filter in (UW.50).
For a normal functional \(\omega\), the rectangle contour shift gives

\[
 \begin{aligned}
 &\omega(\sigma_f^\varphi(a))\\
 &=\int b_f(t-is)\\
 &\quad\cdot\omega(G(t-is))\,dt.
 \end{aligned}
 \tag{UW.62}
\]

For fixed \(s\), the vertical sides vanish because \(b_f\) is
\(O(|t|^{-2})\) uniformly on that strip and \(G\) is bounded there
by (UW.61). All horizontal integrals are absolutely convergent.
Equations (UW.52) and (UW.61) give

\[
 \begin{aligned}
 &|\omega(\sigma_f^\varphi(a))|\\
 &\leq\|\omega\| e^b C_f(1+s)^2\\
 &\quad\cdot e^{-(c-2b)s}\longrightarrow0.
 \end{aligned}
 \tag{UW.63}
\]

Thus every such filter annihilates \(a\). For \(f\) supported in
\((-\infty,-c)\), shift upwards instead: \(b_f(t+is)\) has the
same exponential decay, and (UW.61) is symmetric in the two half-planes.
This proves annihilation for the negative tests too.

At any point outside \([-2b,2b]\), choose a smooth compactly supported
test function nonzero there and supported entirely on the corresponding
side, with some \(c>2b\). It lies in the annihilator ideal, so the point
is absent from the annihilator hull defined in UW-03. Hence
\(\operatorname{Sp}_{\sigma^\varphi}(a)\subseteq[-2b,2b]\).
Intersecting these closed intervals over all \(\varepsilon>0\) proves

\[
 \boxed{
 \operatorname{Sp}_{\sigma^\varphi}(a)
 \subseteq[-2\alpha,2\alpha].}
 \tag{UW.35}
\]

The argument proves the claimed support at the filter definition, without
a product of distributions or a spectral-synthesis assumption. Reflecting
the Fourier sign leaves this symmetric interval unchanged. The case
\(\alpha=0\) is included by the same intersection (and the metric gives
\(\varphi=\psi\), hence \(a=0\)). The factor two in (UW.35) is present
in the source and is distinct from the missing factor two corrected
in (UW.21).

## Entire functions of small exponential type vary little

Let \(E\) be a complex Banach space. Given \(\varepsilon,R>0\), there is
\(\delta>0\) such that every entire \(f:\mathbb C\to E\) satisfying

\[
 \begin{gathered}
 \|f(z)\|\leq e^{\delta|\Im z|},\\
 z\in\mathbb C.
 \end{gathered}
 \tag{UW.36}
\]

also satisfies

\[
 \begin{gathered}
 \|f(z)-f(0)\|\leq\varepsilon,\\
 |z|<R.
 \end{gathered}
 \tag{UW.37}
\]

First take scalar-valued entire functions. For \(c\geq0\), let
\(\mathcal H_c\) denote those satisfying

\[
 \begin{gathered}
 g\in\mathcal H_c\\
 \Longleftrightarrow\\
 |g(z)|\leq e^{c|\Im z|}\quad(z\in\mathbb C).
 \end{gathered}
 \tag{UW.38}
\]

For \(0<c\leq1\), these functions are uniformly bounded on each compact
set. Cauchy's estimate makes them equicontinuous on every smaller concentric
disc. Arzela--Ascoli on discs of integer radius, followed by a diagonal
subsequence, gives locally uniform convergence; the limit is entire by the
local Cauchy formula and retains the defining bound. The compact-open
topology is metrized by the weighted sum of the suprema on those discs.
Thus \(\mathcal H_c\) is compact. The sets decrease as \(c\downarrow0\), and
their intersection
consists exactly of the constants of modulus at most one. Indeed, if \(g\)
belongs to every \(\mathcal H_c\), the Cauchy estimate on the circle of
radius \(L\) about \(z_0\), used with \(c=L^{-2}\), gives

\[
 \begin{gathered}
 A_L=L^{-2}|\Im z_0|+L^{-1},\\
 |g'(z_0)|\leq L^{-1}e^{A_L}.
 \end{gathered}
 \tag{UW.38a}
\]

Letting \(L\to\infty\) gives \(g'(z_0)=0\). Thus \(g\) is constant, and its
real-axis bound is at most one.

Let

\[
 \begin{gathered}
 q(g)=\sup_{|z|\leq R}|g(z)-g(0)|,\\
 \mathcal U=\{g:q(g)<\varepsilon\}.
 \end{gathered}
 \tag{UW.39}
\]

This is an open neighborhood of \(\mathcal H_0\). If no
\(\mathcal H_\delta\) lay in \(\mathcal U\), choose
\(g_n\in\mathcal H_{1/n}\setminus\mathcal U\). A subsequence converges on
compact sets to an element of every \(\mathcal H_c\), hence to an element of
\(\mathcal H_0\subset\mathcal U\), contradicting openness. Thus some
\(\delta\) works for scalar functions.

For Banach-valued \(f\), compose with every \(\ell\in E^*\) of norm at most
one. The scalar result gives

\[
 \begin{gathered}
 |\ell(f(z)-f(0))|\leq\varepsilon,\\
 |z|<R.
 \end{gathered}
 \tag{UW.40}
\]

Hahn--Banach norms the vector difference, proving (UW.37). This proof also
shows that \(\delta\) depends only on \(\varepsilon\) and \(R\), not on \(E\).

## Completeness and continuity

The extended metric space \((\mathcal W_0(M),d)\) is complete. Let
\((\varphi_n)\) be \(d\)-Cauchy. Choose a tail index \(N\) and set
\(\rho=\varphi_N\). Every tail weight has finite distance from \(\rho\), and
these distances are uniformly bounded. Hence

\[
 U_n(z)=[D\varphi_n:D\rho]_z
 \tag{UW.41}
\]

is entire and uniformly bounded on each compact subset of \(\mathbb C\).

Fix \(R>0\). If \(d(\varphi_n,\varphi_m)<\delta\), write

\[
 W_{nm}(z)=[D\varphi_n:D\varphi_m]_z.
 \tag{UW.42}
\]

UW-08 makes \(W_{nm}(z)\) uniformly close to one for \(|z|\leq R\) once
\(\delta\) is small. Analytic continuation of the chain rule gives

\[
 U_n(z)=W_{nm}(z)U_m(z).
 \tag{UW.43}
\]

The common compact bound on \(U_m\) now shows that \((U_n)\) is uniformly
Cauchy on \(|z|\leq R\). Its locally uniform norm limit \(V\) is entire.
On the real axis it is a strongly continuous unitary
\(\sigma^\rho\)-cocycle: unitarity and the cocycle law pass through the norm
limit. The reconstruction theorem CX-10 gives a unique
\(\psi\in\mathcal W_0(M)\) with

\[
 V_t=[D\psi:D\rho]_t.
 \tag{UW.44}
\]

For \(\varepsilon>0\), choose \(n\) so late that
\(d(\varphi_m,\varphi_n)<\varepsilon\) for every later \(m\). The functions
\([D\varphi_m:D\varphi_n]_z\) have the common bound
\(e^{\varepsilon|\operatorname{Im}z|}\). Their locally uniform limit is the
analytic continuation of \([D\psi:D\varphi_n]_t\), by (UW.43)--(UW.44).
The same bound survives the limit, so

\[
 d(\psi,\varphi_n)\leq\varepsilon.
 \tag{UW.45}
\]

Thus \(\varphi_n\to\psi\) in the uniform topology. Choosing the fixed tail
reference \(\rho\) explicitly avoids assuming in advance that the whole
sequence lies in one finite-distance component.

For every \(x\in M_+\), the evaluation map

\[
 \varphi\longmapsto\varphi(x)
 \tag{UW.46}
\]

is continuous into \([0,\infty]\) with its order topology. Indeed,
\(d(\varphi,\psi)<a\) and (UW.8) give

\[
 \begin{gathered}
 e^{-a}\psi(x)\leq\varphi(x),\\
 \varphi(x)\leq e^a\psi(x).
 \end{gathered}
 \tag{UW.47}
\]

This squeeze also handles the value \(+\infty\).

Finally, for faithful normal states \(\varphi,\psi\),

\[
 \boxed{
 \|\varphi-\psi\|\leq4d(\varphi,\psi).}
 \tag{UW.48}
\]

If \(d(\varphi,\psi)<a\), (UW.47) in both directions gives, for
\(0\leq x\leq1\),

\[
 |\varphi(x)-\psi(x)|
 \leq e^a-1.
 \tag{UW.49}
\]

The self-adjoint functional \(\varphi-\psi\) vanishes at one, so its norm is
twice the supremum in (UW.49). If \(d<1/2\), let
\(a\downarrow d\) and use \(e^a-1\leq2a\) on this interval. If
\(d\geq1/2\), the trivial state bound \(\|\varphi-\psi\|\leq2\) gives the
same conclusion. This proves (UW.48) for every finite \(d\); it is automatic
when \(d=\infty\).

## Scope and ownership

UW-01--09 cover Takesaki II XII.5, Definition 5.1 through Lemma 5.8, with
the density exponent corrected in (UW.21). The half-strip domination theorem
is the explicit OA-MOD prerequisite OA-MOD-UW-DEP-DOMINATION. The general
Arveson/Paley--Wiener theorem is the explicit OA-FLOW-owned prerequisite
OA-MOD-UW-DEP-ARVESON-PW. Crossed products, dual actions, action cocycles,
flow classification, and the later action of inner automorphisms remain with
OA-FLOW.

## References

- M. Takesaki, *Theory of Operator Algebras II*, Springer, 2003, Chapter XII,
  Section 5, printed pages 421--425.
- M. Takesaki, *Theory of Operator Algebras II*, Chapter VIII, Section 3,
  Theorem 3.17.
