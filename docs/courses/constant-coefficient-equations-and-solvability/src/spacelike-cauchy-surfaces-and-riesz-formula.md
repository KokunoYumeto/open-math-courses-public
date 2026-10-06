# Spacelike Cauchy surfaces and the Riesz formula

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A curved initial surface can determine a wave just as a time plane does. Local spacelikeness makes the normal Cauchy recursion possible. A separate condition at infinity makes every causal line meet the surface and keeps the convolution region compact. In three spatial dimensions, the resulting representation has a geometric form: curvature and a reflected null derivative replace the flat sphere terms.

Read [The wave Cauchy problem and Kirchhoff's formula](flat-wave-cauchy-and-kirchhoff.md) for the normalization \(W_c=c^{-2}\partial_t^2-\Delta_x\), the finite order of its causal kernel, and the finite-jet extension lemma. Riesz's primary paper [Riesz] develops wave representations using reflected null rays. We derive the surface density, curvature coefficient and full representation below.

## Which graphs are global Cauchy surfaces?

Let \(c>0\), \(x\in\mathbb R^n\), \(n\geq1\), and put
\[
\begin{aligned}
\Gamma&=\{(S(x),x):x\in\mathbb R^n\},\\
H_S&=\{t\geq S(x)\}.
\end{aligned}
\tag{1}
\]
A nonzero causal direction \((a,b)\) satisfies \(|a|\geq|b|/c\). A global Cauchy surface meets each affine line with such a direction once and transversely.

**Theorem 1.** For a \(C^1\) graph, this property is equivalent to
\[
\begin{gathered}
|\nabla S(x)|<1/c,\\
|x|-c|S(x)|\longrightarrow+\infty
\quad (|x|\to\infty).
\end{gathered}
\tag{2}
\]
Every smooth hypersurface with the line-intersection property is a graph of this kind.

**Proof.** Assume (2). Orient a causal line to the future, so \(a\geq|b|/c\), \(a>0\). Its intersection equation is the zero of
\[
g(\lambda)=t_0+a\lambda-S(x_0+\lambda b).
\tag{3}
\]
If \(b\ne0\), then
\(g'=a-\nabla S\cdot b>a-|b|/c\geq0\); if \(b=0\), \(g'=a>0\). For a strictly timelike direction, the global bound \(|S(x)|\leq|x|/c+C\) implies \(g(\lambda)\to\pm\infty\) at the respective ends. For a null direction put \(h(x)=|x|-c|S(x)|\). For positive and negative \(\lambda\), respectively,
\[
\begin{aligned}
g(\lambda)&\geq t_0-|x_0|/c+
h(x_0+\lambda b)/c,\\
g(\lambda)&\leq t_0+|x_0|/c-
h(x_0+\lambda b)/c.
\end{aligned}
\tag{4}
\]
Coercivity gives the same two limits. Thus there is exactly one zero, and the strictly positive derivative makes it transverse.

Conversely, vertical lines identify any hypersurface with the intersection property as a global graph; their transverse intersection and the implicit function theorem give its regularity. If \(|\nabla S|\geq1/c\) at a point, choose \(b\) in that gradient direction. Then \((\nabla S\cdot b,b)\) is a nonzero causal tangent vector, contrary to transversality. Hence the strict gradient inequality holds.

Choose \(T>|S(0)|\). A past null ray from \((T,0)\) has intersection equation
\[
S(\rho\omega)+\rho/c=T,\qquad \rho>0.
\tag{5}
\]
The left side is strictly increasing in \(\rho\). Each ray has one intersection, and the implicit function theorem makes its radius continuous in \(\omega\in S^{n-1}\). Compactness of the sphere bounds all these radii. For points inside that past cone, the inequality corresponding to (5) implies a smaller radial parameter. Thus both its graph section and its intersection with \(H_S\) are compact. Future null rays from \((-T,0)\) give the same conclusion for that graph section.

If \(h(x)\leq cT\) and \(S(x)\leq0\), then
\(|x|+cS(x)\leq cT\), so the graph point is in the past section from \((T,0)\). If \(S(x)\geq0\), then \(|x|-cS(x)\leq cT\), so it is in the future section from \((-T,0)\). The sublevel set \(\{h\leq cT\}\) is consequently closed and bounded. Taking all sufficiently large \(T\) proves \(h(x)\to+\infty\). \(\square\)

The strict gradient bound also implies the global Lipschitz estimate
\(|S(x+b)-S(x)|\leq|b|/c\), by integration along a segment. Consequently
\[
H_S+C_c^+\subset H_S.
\tag{6}
\]
Moreover, addition is proper on \(C_c^+\times H_S\). If
\((t,x)=(a,b)+(s,y)\) stays in a compact set, then \(a\geq|b|/c\), \(s\geq S(y)\), and
\[
|y|-c|S(y)|\leq ct+|x|.
\tag{7}
\]
Indeed \(|x-y|+cS(y)\leq ct\); use the triangle inequality and \(S(y)\geq-|S(y)|\). Coercivity bounds \(y\). Continuity bounds \(s\) below, while \(a=t-s\geq0\) bounds the two times above. The other coordinates are bounded; closedness proves properness.

The condition at infinity cannot be dropped. In one dimension \(S(x)=c^{-1}\sqrt{1+x^2}\) has \(|S'|<1/c\), but the null line \(t=x/c\) never meets its graph.

## Finitely differentiable data on the graph

**Theorem 2.** Let \(k\geq2\), let \(v\) be an integer with \(v\geq(n-3)/2\), and put \(M=k+v+2\). Suppose \(S\in C^M\) satisfies (2). If
\[
\begin{aligned}
f&\in C^{M-2}(H_S),\\
u_0&\in C^M(\mathbb R^n),\qquad
u_1\in C^{M-1}(\mathbb R^n),
\end{aligned}
\tag{8}
\]
there is \(u\in C^k(H_S)\) with
\[
\begin{aligned}
W_cu&=f,\\
u(S(x),x)&=u_0(x),\\
u_t(S(x),x)&=u_1(x).
\end{aligned}
\tag{9}
\]
It is unique among \(C^2\) solutions. The data \(u_1\) specify the ordinary temporal derivative. The notation \(C^r(H_S)\) uses the graph chart \((r,x)\mapsto(r+S(x),x)\), \(r\geq0\).

**Proof.** Flatten the graph by \(r=t-S(x)\) and set \(w(r,x)=u(r+S(x),x)\). An old spatial derivative becomes \(\partial_{x_i}-S_i\partial_r\). Expanding gives
\[
\begin{aligned}
W_cu&=A w_{rr}+2\nabla S\cdot\nabla_x w_r\\
&\quad+(\Delta S)w_r-\Delta_xw,\\
A&=c^{-2}-|\nabla S|^2>0.
\end{aligned}
\tag{10}
\]
For \(g_j=\partial_r^jw(0,\cdot)\), prescribe \(g_0=u_0\), \(g_1=u_1\), and use the recursion
\[
\begin{aligned}
A g_{j+2}&=\partial_r^j\widetilde f(0,x)+\Delta g_j\\
&\quad-2\nabla S\cdot\nabla g_{j+1}
-(\Delta S)g_{j+1},
\end{aligned}
\tag{11}
\]
for \(0\leq j\leq M-2\), where \(\widetilde f(r,x)=f(r+S(x),x)\). The numerator has class \(C^{M-j-2}\); \(A^{-1}\) has class \(C^{M-1}\). Induction therefore gives \(g_j\in C^{M-j}\).

Lemma 3 of the preceding lesson extends these jets to a \(C^M\) function in the flattened coordinates. Pull it back to a function \(v_*\in C^M\) on spacetime. Equation (11) makes all normal derivatives of \(f-W_cv_*\) through order \(M-2\) vanish at the graph. Tangential differentiation gives the mixed jets too. Extension by zero to the lower side is consequently a global \(F\in C^{M-2}\), supported in \(H_S\).

Set \(z=E_c*F\). Properness is (7). The kernel order and translated-pairing proof in the preceding lesson give \(z\in C^k\), including \(n=1,v=-1\), where one derivative is put on the measure-valued first derivative of \(E_c\). Equation (6) puts its support in \(H_S\), so its value and first derivatives have zero boundary trace. Then \(u=v_*+z\) has (9).

For uniqueness, a homogeneous difference has zero trace and zero temporal derivative. Tangential differentiation of the trace gives
\[
u_{x_i}+S_i u_t=0
\quad\hbox{on }\Gamma.
\tag{12}
\]
Every first derivative therefore vanishes there. Extension by zero is \(C^1\); integration by parts across the graph yields \(W_cU=0\) without a surface distribution. Proper causal convolution now gives
\(U=(W_cE_c)*U=E_c*(W_cU)=0\). \(\square\)

No uniform gap between \(|\nabla S|\) and \(1/c\), and no growth condition on the data, is required.

## The cone section and its intrinsic area

For the remainder take \(n=3\), a smooth graph satisfying (2), and a point \(q\) strictly above it. Translate \(q\) to the origin temporarily. Write
\[
\begin{aligned}
R(t,x)&=c^2t^2-|x|^2,\\
p(\alpha,\beta)&=c^{-2}\alpha_t\beta_t-\alpha_x\cdot\beta_x.
\end{aligned}
\tag{13}
\]
The associated Lorentz form on vectors is
\(G(v,z)=c^2v_tz_t-v_x\cdot z_x\).
The vector \(p^\sharp\alpha\) is defined by
\((p^\sharp\alpha)u=p(\alpha,du)\).
Thus \(W_c=p(\partial,\partial)\).

Each past null ray meets \(\Gamma\) once. The compact section
\(\Sigma=\Gamma\cap(-C_c^+)\) has a smooth parametrization
\[
\begin{gathered}
X(\omega)=(-r(\omega)/c,r(\omega)\omega),\\
r>0,\qquad \omega\in S^2.
\end{gathered}
\tag{14}
\]
Put \(w=\log r\). In \(-G(dX,dX)\), the \(dr^2\) terms cancel and \(\omega\cdot d\omega=0\). The resulting positive metric and area element are
\[
g_\Sigma=r^2g_{S^2},\qquad d\sigma=r^2d\omega.
\tag{15}
\]
This area is induced by the Lorentz form on the spacelike section.

We need an actual defining function \(s\) for the initial graph, positive above it, with
\[
p(dR,ds)=-1
\quad\hbox{near }\Sigma.
\tag{16}
\]
Use ray coordinates \(t=-\kappa\rho/c\), \(x=\rho\omega\), near \(\kappa=1\). The graph equation has a smooth positive solution \(\rho_b(\kappa,\omega)\), by transversality and compactness. Define
\[
s=-\frac12\log\frac{\rho}{\rho_b(\kappa,\omega)}.
\tag{17}
\]
Its zero set is the graph, and it is positive toward the origin. The Euler field \(\mathcal E=t\partial_t+x\cdot\partial_x\) fixes \(\kappa,\omega\), so \(2\mathcal Es=-1\). Since \(p^\sharp dR=2\mathcal E\), this proves (16). Locally \(s\) is a positive smooth multiple of \(t-S(x)\). Extend that multiplier by a partition so it is one outside a compact neighborhood of \(\Sigma\); (16) remains valid near the section.

**Lemma 3.** The distributional density
\[
c\,\delta(R)\delta(s)\,dt\,dx
\tag{18}
\]
on the past branch equals the intrinsic area density \(d\sigma\) on \(\Sigma\).

**Proof.** Integrate in \(t\) using \(\delta(c^2t^2-\rho^2)\) on the negative branch. It contributes \(1/(2c\rho)\). The spatial polar Jacobian is \(\rho^2d\rho\,d\omega\). On the cone, (17) reads
\(s=-\tfrac12(\log\rho-w(\omega))\), so
\(\delta(s)=2r\delta(\rho-r)\).
Multiplication by \(c\) leaves \(r^2d\omega\), exactly (15). \(\square\)

## A reflected null direction

Set \(h=p(ds,ds)\). Near \(\Sigma\), define
\[
\begin{aligned}
V&=A p^\sharp ds+B p^\sharp dR,\\
A&=-\frac1{1-4Rh},\\
B&=-\frac h{1-4Rh}.
\end{aligned}
\tag{19}
\]
The denominator is nonzero after shrinking the neighborhood. As \(p(dR,dR)=4R\), substitution gives
\[
Vs=0,\qquad VR=1.
\tag{20}
\]
On the section define the reflected vector
\[
L=p^\sharp(2ds+h\,dR).
\tag{21}
\]
It is the unique vector satisfying
\[
\begin{gathered}
G(L,L)=0,\qquad G(L,T\Sigma)=0,\\
dR(L)=-2.
\end{gathered}
\tag{22}
\]
Indeed, the square of its covector is \(4h-4h=0\). The two defining differentials vanish on \(T\Sigma\), and its \(dR\) pairing is \(-2\). The Lorentz normal plane of a spacelike two-plane has two null lines. The radial line has zero \(dR\) pairing; the other line contains exactly one vector with the prescribed pairing.

For a more explicit description, let \(g=\nabla_{S^2}w\). Then
\[
\begin{aligned}
L_t&=\frac{1+|g|^2}{2cr},\\
L_x&=\frac{(1-|g|^2)\omega-2g}{2r}.
\end{aligned}
\tag{23}
\]
The tangent vector associated with \(v\in T_\omega S^2\) is
\[
\left(-\frac r c\,g\cdot v,\
r(g\cdot v)\omega+rv\right).
\]
Direct substitution in \(G\) verifies nullity, orthogonality, and \(dR(L)=-2\), identifying (23) with (21). Its positive time component fixes the future orientation.

For integration by parts we also need
\[
\operatorname{div}V=-W_cs
\quad\hbox{on }\Sigma.
\tag{24}
\]
Equation (16) implies \(\mathcal Es=-1/2\), so \(ds\) has degree \(-1\), and \(h\) has degree \(-2\). Hence \(p(dh,dR)=2\mathcal Eh=-4h\). At \(R=0\), \(dA=-4h\,dR\), giving
\[
p(dA,ds)=4h,\qquad p(dB,dR)=4h.
\]
As \(W_cR=8\), the divergence is
\[
4h-W_cs+4h-8h=-W_cs.
\]
Using (21) and \(V=-p^\sharp ds-hp^\sharp dR\) on the section, we conclude
\[
p(ds,du)-\operatorname{div}(Vu)=Lu+uW_cs.
\tag{25}
\]

## Why the scalar coefficient is curvature

The convenient function
\[
s_0=-\frac12\bigl(\log(-ct)-w(x/|x|)\bigr)
\tag{26}
\]
has (16) and vanishes on \(\Sigma\). It can differ from the actual defining function away from the cone. We therefore verify that it gives the same scalar and reflected vector on the section.

The difference \(g_0=s_0-s\) has \(\mathcal Eg_0=0\). Its zero trace on \(\Sigma\) propagates along nearby null rays, so it vanishes on \(R=0\). Because \(R\) is a submersion there, \(g_0=f_0R\) locally. The equality \(p(dg_0,dR)=0\) gives
\[
p(df_0,dR)+4f_0=0.
\tag{27}
\]
On \(R=0\) we get
\[
W_cg_0=2p(df_0,dR)+f_0W_cR=0.
\tag{28}
\]
Thus \(W_cs_0=W_cs\). Also \(ds_0=ds+f_0dR\) and
\(p(ds_0,ds_0)=h-2f_0\) there. The covector in (21) remains unchanged. The area density remains unchanged because the two functions restrict identically to the cone.

Polar differentiation of (26) now gives
\[
W_cs=\frac{1-\Delta_{S^2}w}{2r^2}.
\tag{29}
\]
The temporal second derivative contributes \(1/(2c^2t^2)=1/(2r^2)\) on the cone. The spatial part \(w(\omega)/2\) contributes \(\Delta_{S^2}w/(2r^2)\).

**Lemma 4.** The Gaussian curvature of the metric (15) is
\[
K=r^{-2}(1-\Delta_{S^2}w).
\tag{30}
\]
Consequently \(W_cs=K/2\) on \(\Sigma\).

**Proof.** In stereographic coordinates \((a,b)\), the unit sphere metric is \(e^{2\phi}(da^2+db^2)\), with
\(\phi=\log2-\log(1+a^2+b^2)\).
For a conformal plane metric \(e^{2\psi}(da^2+db^2)\), the Christoffel entries are
\[
\begin{aligned}
\Gamma^1_{11}&=\psi_a,&\Gamma^2_{11}&=-\psi_b,\\
\Gamma^1_{12}&=\psi_b,&\Gamma^2_{12}&=\psi_a,\\
\Gamma^1_{22}&=-\psi_a,&\Gamma^2_{22}&=\psi_b.
\end{aligned}
\tag{31}
\]
In the first component of the curvature vector
\(\mathcal R(\partial_a,\partial_b)\partial_b\), the derivative terms give
\(-\psi_{aa}-\psi_{bb}\), and the two quadratic products cancel. Lowering that component multiplies it by \(e^{2\psi}\), and division by the metric determinant \(e^{4\psi}\) yields
\[
K=-e^{-2\psi}\Delta\psi.
\tag{32}
\]
For \(\psi=\phi+w\), direct differentiation gives
\(\Delta\phi=-e^{2\phi}\) and
\(\Delta_{S^2}w=e^{-2\phi}\Delta w\).
Substitution in (32) proves (30) in each stereographic chart, hence everywhere. The convention gives curvature one to the unit sphere. Equation (29) finishes the proof. \(\square\)

## The representation formula

Return to a general observation point \(q=(T,X)\) above the graph. Put
\[
\begin{aligned}
R_q(t,y)&=c^2(t-T)^2-|y-X|^2,\\
\Sigma_q&=\Gamma\cap(q-C_c^+).
\end{aligned}
\tag{33}
\]
Let \(d\sigma_q\) and \(K_q\) be the area and curvature of its positive induced metric, and let \(L_q\) be the unique reflected null vector with \(dR_q(L_q)=-2\).

To display the translated forcing without a long integration subscript, set
\[
\begin{aligned}
r_q(y)&=|y-X|,\\
f_q(y)&=f(T-r_q(y)/c,y),\\
\end{aligned}
\tag{33a}
\]
The spatial integration region is
\[
D_q=\{y:(T-r_q(y)/c,y)\in H_S\}.
\]

**Theorem 5 (Riesz representation).** Every \(C^2(H_S)\) solution of \(W_cu=f\) satisfies
\[
\begin{aligned}
u(T,X)&=\frac1{4\pi}
\int_{D_q}\frac{f_q(y)}{r_q(y)}\,dy\\
&\quad+\frac1{4\pi}\int_{\Sigma_q}K_q u\,d\sigma_q\\
&\quad+\frac1{2\pi}\int_{\Sigma_q}L_q u\,d\sigma_q.
\end{aligned}
\tag{34}
\]
The spatial displacement in the forcing term is measured from \(X\).

**Proof.** Translate \(q\) to zero. The past fundamental kernel is
\[
\begin{gathered}
E=\frac c{2\pi}\delta(R)\quad\hbox{on the past branch},\\
W_cE=\delta_0.
\end{gathered}
\tag{35}
\]
Choose a smooth \(\chi\) that is zero for arguments at most zero and one for arguments at least one. Write
\(\chi_\epsilon(s)=\chi(s/\epsilon)\).
The past cone meets the support of \(\chi_\epsilon(s)\) in a common compact set. Insert a compact cutoff equal to one on that set and near zero. Since \(\chi_\epsilon(s)=1\) near zero for small \(\epsilon\), integration by parts using (35) gives
\[
\begin{aligned}
u(0)&=\langle E,\chi_\epsilon W_cu\rangle\\
&\quad+\langle E\,p(ds,du),\chi_\epsilon'\rangle\\
&\quad-\langle u\,p(dE,ds),\chi_\epsilon'\rangle.
\end{aligned}
\tag{36}
\]
For clarity, expand \(W_c(\chi_\epsilon u)\). The product rule gives
\(\chi_\epsilon W_cu+2\chi_\epsilon'p(ds,du)+uW_c\chi_\epsilon\).
Integrating the last term once transfers a derivative to \(Eu\), producing
\(-\chi_\epsilon'p(dE,ds)u-\chi_\epsilon'Ep(ds,du)\). This proves (36).

Near the section, the branch is away from the vertex and (16) gives
\[
p(dE,ds)=-\frac c{2\pi}\delta'(R).
\tag{37}
\]
The vector \(V\) satisfies (20), so transverse integration by parts yields
\[
\begin{aligned}
&\langle\delta'(R)\chi_\epsilon'(s),u\rangle\\
&\quad=-\langle\delta(R)\chi_\epsilon'(s),
\operatorname{div}(Vu)\rangle.
\end{aligned}
\tag{38}
\]
No derivative of \(\chi_\epsilon'\) remains because \(Vs=0\).

The independent transverse coordinates \((R,s)\) imply
\(\delta(R)\chi_\epsilon'(s)\to\delta(R)\delta(s)\).
Apply Lemma 3, (25), and \(W_cs=K/2\) to the two boundary terms. They become
\[
\frac1{2\pi}\int_\Sigma
\left(Lu+\frac K2u\right)d\sigma.
\tag{39}
\]
For the first term in (36), \(\chi_\epsilon\) tends to \(1_{H_S}\) on the cone. The section has zero measure for the cone measure, and compactness permits dominated convergence. Integrating the time delta in (35) gives
\[
\frac1{4\pi}\int_{(-|y|/c,y)\in H_S}
\frac{f(-|y|/c,y)}{|y|}\,dy.
\tag{40}
\]
The singularity \(1/|y|\) is locally integrable in three dimensions. Equations (39)–(40) prove the formula for smooth \(u\).

To justify the same calculation for \(C^2\) solutions, extend \(u\) through the graph locally in its \(r=t-S(x)\) chart. For \(r<0\), use
\[
\begin{aligned}
\widetilde u(r,x)&=6u(-r,x)\\
&\quad-8u(-2r,x)+3u(-3r,x).
\end{aligned}
\tag{41}
\]
For normal derivative orders \(j=0,1,2\), the coefficient sum
\(6(-1)^j-8(-2)^j+3(-3)^j\) equals one. All derivatives through order two therefore join continuously. A partition followed by mollification gives smooth approximations in the \(C^2\) norm on the common compact pairing region. Their wave images converge uniformly to \(f\); their values and first derivatives on \(\Sigma\) also converge uniformly. The cone kernel is a finite measure on this region, and the surface has finite area. Pass to the limit in (39)–(40). Finally translate the coordinates back to \(q\), giving (34). \(\square\)

The boundary terms use only the Cauchy data. Differentiating \(u_0(x)=u(S(x),x)\) gives
\[
\nabla_xu=\nabla u_0-u_1\nabla S
\quad\hbox{on }\Gamma,
\]
and hence
\[
Lu=L_x\cdot\nabla u_0+
(L_t-L_x\cdot\nabla S)u_1.
\tag{42}
\]
Together with \(u=u_0\), this expresses both surface integrals through known data.

## Checking the plane and the total curvature

For \(\Gamma=\{t=T_0\}\), let \(\tau=T-T_0>0\). The section has radius \(r=c\tau\), and
\[
\begin{aligned}
K&=1/r^2,\\
L_t&=1/(2cr),\qquad L_x=\omega/(2r).
\end{aligned}
\tag{43}
\]
The curvature integral contributes the average of \(u_0(X+r\omega)\). The reflected derivative integral contributes the average of
\(\tau u_1(X+r\omega)+r\omega\cdot\nabla u_0(X+r\omega)\).
The forcing term is the backward-cone term of Kirchhoff's formula. Thus (34) recovers every coefficient and sign of the flat formula.

There is also a direct total-curvature identity:
\[
\int_\Sigma K\,d\sigma
=\int_{S^2}(1-\Delta_{S^2}w)\,d\omega
=4\pi.
\tag{44}
\]
Integration by parts on the closed sphere makes the Laplacian integral zero. This proves (44) from the metric calculation, without an additional global curvature theorem. Substituting the solution \(u=1,f=0\) in (34) gives the same check.

## Exercises with complete solutions

**Exercise 1 (basic: an affine Cauchy surface).** Let \(S(x)=b+a\cdot x\), with \(c|a|<1\). Verify both conditions in (2), future closure, and properness of causal addition.

**Solution.** The gradient is \(a\). Moreover,
\[
|x|-c|b+a\cdot x|
\geq(1-c|a|)|x|-c|b|\longrightarrow+\infty.
\]
Theorem 1 applies. For a future causal displacement \((s,y)\), \(s\geq|y|/c\geq a\cdot y\), so \(t\geq b+a\cdot x\) implies \(t+s\geq b+a\cdot(x+y)\). This is future closure. For bounded output, (7) and the displayed coercive estimate bound the input spatial coordinate; the time bounds in the properness proof then bound both inputs.

**Exercise 2 (intermediate: the curved recursion).** In one spatial dimension, compute the first unknown normal jet \(g_2\) for arbitrary \(S\), \(u_0\), \(u_1\), and source \(f\). Specialize to an affine graph.

**Solution.** Equation (11) at \(j=0\) gives
\[
\begin{aligned}
(c^{-2}-(S')^2)g_2&=f(S(x),x)+u_0''\\
&\quad-2S'u_1'-S''u_1.
\end{aligned}
\]
The term involving \(S''\) comes from differentiating the coefficient in the spatial square. For \(S=b+ax\),
\[
g_2=\frac{f(b+ax,x)+u_0''-2au_1'}{c^{-2}-a^2}.
\]
The denominator is positive when \(c|a|<1\). This is the second derivative at fixed flattened spatial coordinate, equal to the ordinary second temporal derivative on the graph.

**Exercise 3 (intermediate: reading a reflected derivative from data).** Prove (42). On a time plane, calculate the two surface terms in (34) from it.

**Solution.** The chain rule gives
\(\partial_i u_0=u_{x_i}+S_i u_t\). Substituting \(u_t=u_1\) in \(Lu=L_tu_t+L_x\cdot\nabla_xu\) yields (42). On the plane \(\nabla S=0\), (43) gives
\[
Lu=\frac{u_1}{2cr}+\frac{\omega\cdot\nabla u_0}{2r}.
\]
Multiplying by \(d\sigma=r^2d\omega\) and the factor \(1/(2\pi)\) gives the sphere average of
\((r/c)u_1+r\omega\cdot\nabla u_0\).
Since \(r/c=\tau\), this is the correct elapsed-time velocity term. The factor \(K=1/r^2\) in the other integral gives the average of \(u_0\).

**Exercise 4 (advanced: invariance of the surface coefficients).** Replace a normalized defining function \(s\) by another normalized function \(s_0\) with the same trace on the cone section. Prove that \(L\) and \(W_cs\) on the section do not change.

**Solution.** Both functions have Euler derivative \(-1/2\), so their difference is constant along radial dilations. Its zero trace on the section gives a zero trace on nearby null rays. Thus \(s_0-s=f_0R\). Pairing its differential with \(dR\) and using both normalizations gives (27). Since \(W_cR=8\), the product rule on \(R=0\) gives (28). For the vector, there
\[
ds_0=ds+f_0dR,\qquad
p(ds_0,ds_0)=h-2f_0.
\]
Consequently
\(2ds_0+p(ds_0,ds_0)dR=2ds+h\,dR\).
Applying \(p^\sharp\) proves invariance of \(L\).

**Exercise 5 (advanced: the tilted section's curvature).** In three dimensions take \(S=b+a\cdot x\), \(c|a|<1\), and \(q=(T,X)\) above it. Set \(\tau=T-b-a\cdot X\). Calculate \(r(\omega)\) and show that the induced curvature of its null section is constant:
\[
K=\frac{1-c^2|a|^2}{c^2\tau^2}.
\]

**Solution.** On the past ray, \(t=T-r/c\), \(x=X+r\omega\), so its boundary equation is
\(\tau=r(1/c+a\cdot\omega)\). Therefore
\[
r(\omega)=\frac{c\tau}{1+ca\cdot\omega}.
\]
Put \(z=ca\cdot\omega\) and \(A=c|a|<1\). The sphere identities
\(\Delta z=-2z\) and \(|\nabla z|^2=A^2-z^2\) follow by restricting a linear function to the unit sphere. As \(w=\log(c\tau)-\log(1+z)\),
\[
\begin{aligned}
\Delta w&=\frac{2z}{1+z}+\frac{A^2-z^2}{(1+z)^2},\\
1-\Delta w&=\frac{1-A^2}{(1+z)^2}.
\end{aligned}
\]
Insert \(r^{-2}=(1+z)^2/(c^2\tau^2)\) in (30). This gives the stated positive constant. Although its radial function varies, its Lorentz induced metric has constant curvature. As a check, the total curvature is
\[
2\pi(1-A^2)\int_{-1}^1\frac{d\mu}{(1+A\mu)^2}=4\pi
\]
for \(A>0\), and the same value is immediate for \(A=0\).

**Exercise 6 (advanced: a curvature density of changing sign).** For a positive radial null section let \(w(\omega)=\epsilon P_2(\omega_3)\), where \(P_2(z)=(3z^2-1)/2\) and \(\epsilon>0\). Compute \(K\,d\sigma\). Find a range of \(\epsilon\) for which its curvature is negative along the equator, and calculate its total curvature. This exercise concerns the induced geometry of the radial section.

**Solution.** For a function of \(z=\omega_3\),
\[
\Delta_{S^2}F(z)=(1-z^2)F''(z)-2zF'(z).
\]
For \(P_2\), this is \(3-9z^2=-6P_2(z)\). Hence
\[
K\,d\sigma=(1+6\epsilon P_2(\omega_3))\,d\omega.
\]
At the equator \(P_2=-1/2\), so the curvature is negative when \(\epsilon>1/3\); the positive factor \(r^{-2}\) does not alter its sign. The integral of \(P_2\) is
\(2\pi\int_{-1}^1(3z^2-1)/2\,dz=0\).
Thus the total curvature remains \(4\pi\). The fixed total does not require pointwise positive curvature.

## References

[Riesz] M. Riesz, *L'intégrale de Riemann-Liouville et le problème de Cauchy pour l'équation des ondes*, Bulletin de la Société Mathématique de France 67 (1939), 153–170, [primary paper](https://www.numdam.org/article/BSMF_1939__67__S153_0.pdf), especially pp. 160–162 for the reflected-null-ray representation.
