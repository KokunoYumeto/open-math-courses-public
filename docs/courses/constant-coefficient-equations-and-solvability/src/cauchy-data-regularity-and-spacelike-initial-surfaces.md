# Cauchy data, regularity and spacelike initial surfaces

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A causal inverse solves the equation with vanishing past data. To prescribe nonzero initial traces, we first match enough finite normal jets that the remaining forcing extends by zero. The weighted regularity gain then gives a classical solution. We derive the exact boundary source and explain what data determine the solution when a past cone has lower dimension. The same kernel and a controlled graph extension give a local theorem for curved spacelike surfaces.

Read [Causal fundamental solutions and lower order expansions](causal-fundamental-solutions-and-lower-order-expansions.md), [Local regularity, sharp embeddings, and compactness](local-regularity-and-compactness.md), and [The wave Cauchy problem and Kirchhoff's formula](flat-wave-cauchy-and-kirchhoff.md). We use the first lesson's proper causal inverse and local weight gain, the second lesson's Theorem 3.1 on classical derivatives, and Lemma 3 of the third lesson on whole-plane finite normal jets. That lemma states that arbitrary \(g_k\in C^{M-k}(\mathbb R^{n-1})\), \(0\le k\le M\), are the jets \(\partial_t^kv(0,y)\) of a \(C^M\) function. Its proof uses the compact compatible-jet theorem stated there. We also use Plancherel, smooth coordinate changes and integration by parts.

Keep a nonzero polynomial \(P\), hyperbolic in direction \(N\), with principal part \(F=P_m\). Write \(\Gamma=\Gamma(F,N)\), \(C=\Gamma^*\), \(H_N=\{N\cdot x\ge0\}\), and \(D=-i\partial\). The preceding lesson constructs the regular kernel \(E\), supported in \(C\), with \(P(D)E=\delta\). Its support cone satisfies \(N\cdot c\ge b|c|\), \(c\in C\), for some \(b>0\).

## A classical regularity consequence

Set
\[
r=\lfloor n/2\rfloor+1.
\]
For any integer \(j\ge0\), a globally \(C^{j+r}\) forcing supported in \(H_N\) has a unique causal solution in \(C^j(\mathbb R^n)\). Indeed, for a compact smooth \(\psi\), every derivative of \(\psi f\) through order \(j+r\) is continuous and compactly supported, hence square integrable. Plancherel gives
\[
\psi f\in B_{2,(1+|\xi|)^{j+r}}.
\]
For an integer order, the Fourier weight is comparable to the finite collection of monomials through that order. Thus \(f\) belongs to this space locally. The weight \(S_P\) is bounded below by a positive constant: at least one highest nonzero polynomial derivative is a nonzero constant. The local weight gain in *Causal fundamental solutions and lower order expansions* therefore puts \(u\) in \(B_{2,(1+|\xi|)^{j+r}}^{\mathrm{loc}}\). Finally
\[
(1+|\xi|)^j/(1+|\xi|)^{j+r}=(1+|\xi|)^{-r}\in L^2,
\]
because \(r>n/2\). *Local regularity, sharp embeddings, and compactness* Theorem3.1 gives \(u\in C^j\). No claim of optimality for this convenient integer loss is made.

For smooth forcing the same solution is \(C^j\) for every \(j\), hence smooth. Uniqueness is already in \(\mathcal D'\), so the solutions at different regularity levels are one and the same distribution. A solution supported in \(H_N\) and globally \(C^j\) has every boundary derivative of order at most \(j\) equal to zero, by continuity from the open negative halfspace.

## Flat Cauchy data and dependence

Normalize \(|N|=1\), choose orthogonal coordinates \((t,y)\) with \(t=N\cdot x\), and write
\[
\begin{gathered}
P(D)=\sum_{\ell=0}^m A_\ell(D_y)D_t^\ell,\\
A_m=F(N)\ne0,\quad \deg A_\ell\le m-\ell.
\end{gathered}
\tag{1}
\]
For integer \(j\ge m\), assume
\[
\begin{gathered}
f\in C^{j+r}(\overline H_N),\\
\phi_k\in C^{m-k+j+r}(\partial H_N),\quad 0\le k<m.
\end{gathered}
\tag{2}
\]
There is one and only one \(u\in C^j(\overline H_N)\) satisfying
\[
\begin{gathered}
P(D)u=f\text{ in }H_N^\circ,\\
D_t^ku|_{t=0}=\phi_k,\quad 0\le k<m.
\end{gathered}
\tag{3}
\]
The notation \(C^q\) on the closed halfspace means that all derivatives through order \(q\) extend continuously to its boundary.

For existence, put \(M=m+j+r\). Starting with \(\phi_0,\ldots,\phi_{m-1}\), define successively, for \(0\le s\le j+r\),
\[
\begin{aligned}
\phi_{m+s}=A_m^{-1}\Bigl(
&(D_t^sf)|_{t=0}\\
&-\sum_{\ell<m}A_\ell(D_y)\phi_{\ell+s}\Bigr).
\end{aligned}
\tag{4}
\]
Every index \(\ell+s\) on the right is smaller than \(m+s\). Inductively \(\phi_k\in C^{M-k}\): the trace of \(D_t^sf\) has regularity \(j+r-s\), and applying \(A_\ell\) to \(\phi_{\ell+s}\) loses at most \(m-\ell\) derivatives, leaving
\[
M-(\ell+s)-(m-\ell)=j+r-s.
\]
Thus all derivatives used in (4), including the last continuous trace, are justified.

Apply the whole-plane finite normal-jet lemma to the ordinary normal jets \(i^k\phi_k\), \(0\le k\le M\). It gives \(v\in C^M(\mathbb R^n)\) with \(D_t^kv|_{t=0}=\phi_k\). Set \(h=f-P(D)v\) on \(t\ge0\). It is \(C^{j+r}\) and (4) makes \(D_t^s h|_{t=0}=0\) for \(0\le s\le j+r\). Tangential differentiation of these identities shows that every mixed boundary derivative through that total order vanishes. Extend \(h\) by zero to \(t<0\), obtaining \(h_+\in C^{j+r}(\mathbb R^n)\). To verify this regularity, join the derivatives on the two sides; their traces agree at every order in question. The fundamental theorem of calculus along coordinate lines identifies the joined functions as the successive classical derivatives.

By the classical regularity estimate, \(w=E*h_+\) is globally \(C^j\), supported in \(H_N\), and satisfies \(P(D)w=h_+\). All its boundary derivatives through order \(j\) vanish. Consequently \(u=v+w\), restricted to \(t\ge0\), has (3).

For uniqueness and dependence, derive the actual boundary distribution. If \(u\in C^j(\overline H_N)\), \(j\ge m\), and \(U=1_{\{t\ge0\}}u\), repeated integration by parts in \(t\) gives
\[
\begin{aligned}
D_t^\ell U
&=1_{\{t\ge0\}}D_t^\ell u\\
&\quad+\sum_{a=0}^{\ell-1}(-i)^{a+1}
\phi_{\ell-1-a}(y)\,\delta^{(a)}(t).
\end{aligned}
\]
There is one copy of each boundary term; the \(\delta^{(a)}\)'s denote ordinary derivatives. Therefore
\[
\begin{gathered}
P(D)U=f_++B_\phi,\\
\begin{aligned}
B_\phi&=\sum_{\ell=1}^m\sum_{a=0}^{\ell-1}
(-i)^{a+1}A_\ell(D_y)\\
&\qquad{}\cdot\phi_{\ell-1-a}(y)\,\delta^{(a)}(t).
\end{aligned}
\end{gathered}
\tag{5}
\]
where \(f_+\) is the zero extension as a distribution. The formula requires only the prescribed \(m\) traces; tangential integrations by parts are legitimate at the regularities in (2). The proper inverse identity in *Causal fundamental solutions and lower order expansions* now yields the causal representation
\[
U=E*(f_++B_\phi).
\tag{6}
\]
In particular, if \(f=0\) and all \(\phi_k=0\), then \(U=0\). This gives uniqueness without growth assumptions.

For \(x\in H_N\), let
\[
\begin{gathered}
K_x=(x-C)\cap H_N,\\
K_x^\partial=(x-C)\cap\partial H_N.
\end{gathered}
\tag{7}
\]
Both are compact by the cone bound in *Causal fundamental solutions and lower order expansions*. If two sets of data agree in neighborhoods of these sets, respectively in the closed halfspace and its boundary, their forcing and boundary-distribution differences vanish near the entire relevant pairing set in (6). Properness makes the resulting support sum closed, and it excludes \(x\); the solution differences therefore vanish on a neighborhood of \(x\). This proves dependence on the data germs at the past cone, with exactly the finite boundary derivatives in (5). It does not require values of the data anywhere outside that cone's germ.

When \(C\) has nonempty interior in \(\mathbb R^n\), the point value \(u(x)\) for \(N\cdot x>0\) is determined even by the pointwise restrictions of \(f,\phi_k\) to the closed sets in (7). Here is the extra argument. Choose \(v\in\operatorname{int}C\) and set \(x_\varepsilon=x-\varepsilon v\), with small \(\varepsilon>0\) so \(x_\varepsilon\in H_N^\circ\). The compact past set at \(x_\varepsilon\) lies inside the open set \(x-\operatorname{int}C\). If the data differences vanish pointwise on the original past sets, they vanish in neighborhoods of the smaller past set, relative to \(H_N\) and its boundary: the smaller past cone is a compact subset of that open set. The preceding germ argument gives equality at \(x_\varepsilon\). Continuity of the \(C^j\) solutions and \(\varepsilon\downarrow0\) gives equality at \(x\). At the initial plane, equality follows directly from \(\phi_0\).

For lower-dimensional \(C\), that last pointwise-value assertion needs qualification. A concrete counterexample is
\[
\begin{gathered}
P(D)=D_v^2\text{ on }\mathbb R^2_{v,a},\\
N=(1,1),\quad H_N=\{v+a\ge0\},\\
C=\{(s,0):s\ge0\}.
\end{gathered}
\tag{8}
\]
The operator is hyperbolic in direction \(N\). Compare the zero solution with
\[
u(v,a)=\frac{a-v}{2},\qquad f=0.
\]
On the initial line \(v=-a\), its value datum is \(\phi_0(a)=a\), and its normal \(D\)-datum is
\(\phi_1=-i(\partial_v+\partial_a)u=0\). At \(x=(1,0)\), the past cone meets the initial line only at \((0,0)\), where both data values agree with the zero data. The forcing is zero on the whole past cone. Yet \(u(1,0)=-1/2\). The tangential derivative of \(\phi_0\) at that footprint is required by the conversion between the prescribed normal and the active evolution direction. Thus pointwise data values on a degenerate footprint do not suffice. Equations (5)–(7) give the valid general germ/jet statement; the full-dimensional refinement is proved separately above.

For an unnormalized nonzero \(N\), apply this construction to \(N/|N|\) and replace the prescribed jets by \(\phi_k/|N|^k\), because \(D_N=|N|D_{N/|N|}\). The past cone is unchanged under that positive normalization. If \(m=0\), there are no Cauchy traces and \(u=f/P\); this case does not require the finite normal recursion.

For smooth \(f,\phi_k\), the finite theorem applies for every \(j\ge m\). Its solutions coincide by uniqueness and form one \(C^\infty(\overline H_N)\) solution. This is the full smooth Cauchy corollary, not merely smoothness away from the initial plane.

## Curved spacelike initial surfaces

The causal kernel also gives a local Cauchy theorem. Let \(\Sigma\) be a smooth hypersurface near \(x_0\), with its chosen future conormal in \(\Gamma\). For \(j\ge m\), prescribe \(f\in C^{j+r}\) on its closed future side locally and normal jets \(\phi_k\in C^{m-k+j+r}(\Sigma)\), \(0\le k<m\). Then in a sufficiently small future neighborhood there is a \(C^j\) solution of \(P(D)u=f\) with those jets, unique on smaller neighborhoods whose closed past cones stay in the data patch. Smooth data give a smooth solution. Data germs on that local past cone determine the solution; no value-only claim for a degenerate cone is inferred.

We prove this by a global graph extension with controlled geometry. Translate \(x_0\) to zero and rotate the future unit conormal there to \(e_t\). Locally \(\Sigma\) is \(t=S(y)\), with \(S(0)=0\), \(\nabla S(0)=0\). The transformed hyperbolicity cone contains \(e_t\). Choose \(b>0\) so that
\[
t(c)\ge b|c|\qquad(c\in C).
\]
On a small spatial ball of radius \(2\delta\), \(|\nabla S|\) is as small as desired. Multiply \(S\) by a fixed spatial cutoff, equal to one on the radius-\(\delta\) ball and zero outside the radius-\(2\delta\) ball. Because \(|S(y)|\le\varepsilon|y|\) on that ball, both the original derivative and the cutoff derivative keep the extended gradient bounded by \(C_0\varepsilon\). Choose the original ball so this bound is less than \(b/2\) and the graph conormals
\[
M(y)=e_t-\sum_\alpha S_{y_\alpha}(y)e_{y_\alpha}
\]
all lie in one compact subset of \(\Gamma\). Denote the resulting global, compactly supported smooth graph function again by \(S\), and put
\[
\Omega_+=\{(t,y):t\ge S(y)\}.
\]
There is \(\kappa>0\) with \(M(y)\cdot c\ge\kappa|c|\) for all \(y\), \(c\in C\). This follows either from the small-gradient bound or from a common interior ball for the compact set of conormals. Along \(z+\lambda c\), the derivative of \(t-S(y)\) is \(M(y+\lambda c_y)\cdot c\ge0\). Therefore
\[
C+\Omega_+\subset\Omega_+.
\tag{9}
\]
Also \(S\) is bounded. For \(a\in C\), \(z\in\Omega_+\) and \(a+z\) in a fixed compact, \(t(a)\le\max t(a+z)+\|S\|_\infty\); the cone bound controls \(|a|\), and hence \(|z|\). Addition is proper on \(C\times\Omega_+\). Thus the proper convolution identities in *Causal fundamental solutions and lower order expansions* apply here too, and \(P(D)\) is an automorphism on distributions supported in \(\Omega_+\), with inverse \(E*\). The image stays in \(\Omega_+\) by (9).

Flatten the graph by \(s=t-S(y)\). The expression of \(P(D)\) in these smooth coordinates has smooth coefficients, degree \(m\), and highest pure normal coefficient \(P_m(M(y))\ne0\). If normal data are prescribed using the future unit field \(\nu(y)=M(y)/|M(y)|\), extended independently of \(t\), the coefficient of \((-i\partial_s)^k\) in \(D_\nu^k\) is \(|M(y)|^k\ne0\). Other terms have fewer normal derivatives. The first \(m\) prescribed normal jets therefore determine the first \(m\) \(D_s\)-jets successively, using only smooth coefficients and tangential derivatives, with regularity \(C^{M-k}\), \(M=m+j+r\). A different fixed smooth transverse extension of the normal field changes only the lower normal terms and has the same triangular conversion.

Now prescribe that \(D_s^q(f-P(D)v)=0\) at \(s=0\), \(0\le q\le j+r\). The nonzero highest coefficient \(P_m(M(y))\) determines the remaining normal jets of \(v\), of indices \(m,\ldots,M\), successively. Terms of total differential order at most \(m+q\) involve previously determined jets, except for the single leading pure normal one. Smooth coefficient derivatives do not raise that total order. The regularity count in (4) therefore remains \(C^{M-k}\) for the \(k\)-th jet. The whole-plane finite normal-jet lemma, followed by the graph coordinate change, supplies \(v\in C^M\) with these jets.

The residual \(h=f-P(D)v\) on \(\Omega_+\) has every boundary mixed derivative through order \(j+r\) equal to zero. Its zero extension \(h_+\) across the graph is \(C^{j+r}\), by the joined-derivative argument in the smooth \(s,y\) coordinates. The local weight gain and classical regularity estimate, using the proper addition just proved, give
\[
w=E*h_+\in C^j(\mathbb R^n),\qquad \operatorname{supp}w\subset\Omega_+.
\]
All its graph boundary jets through order \(j\) vanish. Hence \(u=v+w\) solves the global graph problem with the prescribed data.

The local data can be extended to the global graph before this construction. Boundary data are extended by smooth cutoffs within their chart. For a \(C^q\) forcing on a closed halfspace chart, extend to the other side by
\[
\widetilde f(s,y)=\sum_{\ell=0}^q a_\ell f(-c_\ell s,y),\qquad s<0,
\]
where the \(q+1\) positive distinct \(c_\ell\)'s and Vandermonde coefficients satisfy \(\sum_\ell a_\ell(-c_\ell)^d=1\) for \(0\le d\le q\). The normal derivatives match through order \(q\), as do all mixed derivatives of that total order; a compact chart cutoff then gives the needed global future forcing. This supplies an actual finite extension rather than an assumed smooth extension of finite data.

Uniqueness on the global graph follows by zero extension. If two \(C^j\) solutions have zero forcing difference and zero normal jets through \(m-1\), their difference extended by zero across \(\Sigma\) has \(P(D)U=0\). To check this, in the smooth flattened coordinates all ordinary mixed traces through order \(m-1\) vanish by the triangular conversion and tangential differentiation; integration by parts produces no boundary distribution. Proper inversion \(U=E*(P(D)U)\) makes it zero.

Finally, the construction really is local. Since the global graph is Lipschitz with constant \(\varepsilon'<b/2\) and \(S(0)=0\), a pair \(x=z+c\), \(z\in\Omega_+\), \(c\in C\), obeys
\[
\begin{aligned}
(b-\varepsilon')|c|
&\le x_t+\varepsilon'|x_y|\\
&\le(1+\varepsilon')|x|.
\end{aligned}
\tag{10}
\]
This follows from \(z_t\ge-\varepsilon'|z_y|\) and \(c_t\ge b|c|\). Hence every relevant past point \(z=x-c\) lies in a ball of radius a fixed constant times \(|x|\). For \(x\) sufficiently near zero, its entire closed past set stays within the original data patch. If two extensions agree there, their forcing and boundary differences, and any cutoff commutator used to localize a local solution, have supports away from that compact past set. Proper inversion with \(E\) makes their solutions agree near \(x\), exactly as in (6)–(7). One can choose a compact cutoff equal to one near the past set and supported within the patch; its commutator is then outside the set. This proves local uniqueness and independence of the extensions on the stated smaller neighborhoods. For smooth data, uniqueness across all finite \(j\)'s again gives a smooth solution.

## Exercises with complete solutions

**Exercise 1 (intermediate: the classical integer loss).** Explain why \(r=\lfloor n/2\rfloor+1\) suffices in the classical regularity estimate. What fails in that particular argument at \(r=n/2\), when \(n\) is even?

**Solution.** Compact \(C^{j+r}\) data have all derivatives through that integer order in \(L^2\), so Plancherel puts them in \(B_{2,(1+|\xi|)^{j+r}}\). The causal inverse preserves at least that weight, since \(S_P\ge c>0\). To obtain \(j\) continuous derivatives from *Local regularity, sharp embeddings, and compactness*, one needs \((1+|\xi|)^{-r}\in L^2\). In polar coordinates, its squared tail behaves as \(\int^\infty s^{n-1-2r}\,ds\), finite exactly for \(r>n/2\). At equality it is logarithmically divergent. This failure is a failure of that general embedding argument; it does not prove that a particular equation has no stronger regularity estimate.

**Exercise 2 (advanced: a finite jet recursion and a boundary sign check).** Let
\[
P(D)=D_t^2-D_y^2+aD_t+b,\qquad a,b\in\mathbb C,
\]
in two total variables. For \(j=2\), determine the regularities of the jets used in the construction, their recursion, and the boundary source in the representation formula.

**Solution.** Here \(m=2\), \(r=\lfloor2/2\rfloor+1=2\), and \(M=6\). The forcing is \(C^4\), and the prescribed \(D_t\)-jets have regularities \(\phi_0\in C^6\), \(\phi_1\in C^5\). The remaining jets are \(\phi_k\in C^{6-k}\), \(2\le k\le6\), defined successively by
\[
\begin{gathered}
\phi_{2+s}=(D_t^sf)|_{t=0}
+D_y^2\phi_s-a\phi_{s+1}-b\phi_s,\\
0\le s\le4.
\end{gathered}
\]
At \(s=4\), all terms are continuous; none requires a derivative above its given count. Formula (5) gives
\[
B_\phi=-i(\phi_1+a\phi_0)\delta(t)-\phi_0\delta'(t).
\]
For comparison, \(D_t^2=-\partial_t^2\) has boundary terms \(-u_t(0,y)\delta-u(0,y)\delta'\); since \(\phi_1=-iu_t(0,y)\), this is exactly \(-i\phi_1\delta-\phi_0\delta'\). The additional \(aD_t\) term contributes \(-ia\phi_0\delta\), as stated.

**Exercise 3 (advanced: values and germs on a degenerate footprint).** For \(P(D)=D_v^2\), \(N=(1,1)\), find the solution in \(v+a\ge0\) in terms of the boundary value \(g(a)=u(-a,a)\) and normal \(D\)-datum \(\phi_1(a)\). Show explicitly which derivative cannot be recovered from data values at a single footprint point.

**Solution.** Every classical homogeneous solution has \(u(v,a)=A(a)+vB(a)\). On the initial line, \(g=A-aB\), hence \(A=g+aB\). The ordinary normal derivative is
\[
(\partial_v+\partial_a)u|_{v=-a}
=B+A'-aB'=g'+2B.
\]
Since this ordinary derivative is \(i\phi_1\), one gets
\[
\begin{gathered}
B=(i\phi_1-g')/2,\\
u(v,a)=g(a)+\frac{v+a}{2}
\bigl(i\phi_1(a)-g'(a)\bigr).
\end{gathered}
\]
The future kernel is \(-v1_{\{v\ge0\}}\delta(a)\), so its minimal cone is the ray \(C=\{(s,0):s\ge0\}\). At \((1,0)\) the initial footprint is only \((0,0)\); the formula uses \(g'(0)\), as well as \(g(0)\) and \(\phi_1(0)\). Taking \(g(a)=a\), \(\phi_1=0\), gives \(u=(a-v)/2\) and \(u(1,0)=-1/2\), while both datum values at the footprint vanish. Agreement of germs determines the required derivative. Agreement only of values at that point does not.

**Exercise 4 (advanced: a global graph with arbitrary growth).** For the Lorentz cone \(C=\{(t,y):t\ge|y|\}\), let \(S\) be a smooth function on all space with \(|\nabla S|\le\kappa<1\), without assuming \(S\) bounded. Prove proper addition on \(C\times\{t\ge S(y)\}\) and explain how the graph Cauchy construction extends to this situation.

**Solution.** Subtract a constant to take \(S(0)=0\). Lipschitz continuity gives \(S(y)\ge-\kappa|y|\). If \(x=z+c\), \(c\in C\), \(z_t\ge S(z_y)\), then
\[
\begin{aligned}
c_t&\le x_t+\kappa|z_y|\\
&\le x_t+\kappa|x_y|+\kappa|c_y|\\
&\le x_t+\kappa|x_y|+\kappa c_t.
\end{aligned}
\]
Therefore \((1-\kappa)c_t\le x_t+\kappa|x_y|\). On a fixed compact set of outputs, \(c_t\), \(|c_y|\le c_t\), and \(z=x-c\) are bounded. Closedness gives properness. Along a future cone vector, the graph defining function has derivative \(c_t-\nabla S\cdot c_y\ge(1-\kappa)c_t\ge0\), so the graph future is invariant under adding \(C\). Its conormals \((1,-\nabla S)\) lie in a compact subset of the open Lorentz cone. Thus every step of the curved-surface construction uses proper addition, that invariant future set and a nonzero leading normal coefficient, all of which hold here. The graph flattening and whole-plane jet extension are global; the regularity estimates are local and impose no uniform bounds on data at infinity. Finite and smooth graph Cauchy data therefore have the corresponding unique solutions with arbitrary growth. The proper-pair bound also supplies their local dependence neighborhoods.

## References

The exact causal inverse, proper support-pair construction and weight gain are proved in [Causal fundamental solutions and lower order expansions](causal-fundamental-solutions-and-lower-order-expansions.md). The Fourier criterion for \(j\) classical derivatives is Theorem 3.1 of [Local regularity, sharp embeddings, and compactness](local-regularity-and-compactness.md). The whole-plane finite normal-jet extension is Lemma 3 of [The wave Cauchy problem and Kirchhoff's formula](flat-wave-cauchy-and-kirchhoff.md), with its exact compact Whitney entry stated in the preceding section.
