# A necessary time strip for smooth mixed solvability

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Unique solvability for every smooth datum forces more than uniqueness of existing solutions. A boundary determinant cannot have zeros with arbitrarily negative imaginary time frequency. We derive a fixed smooth-space estimate, test it against normalized repeated-root modes, and make the final real-algebraic argument explicit without a Puiseux expansion or an attained supremum.

Read [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md), [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md), [Analytic root barriers and supported solvability](analytic-root-barriers-and-supported-solvability.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Fourier convention and Gaussian formula; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies scalar calculus and cutoffs. [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) supplies finite scalar and polynomial algebra. [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html), Sections 14.1–14.4, supplies the precise Fréchet topology and open-mapping theorem. 

The general hyperbolic-cone theorem is proved in [Real roots and their convex component](../AN02-L192.html#4-pass-to-multiple-roots-and-obtain-convexity), Theorem 4.1. The analytic zero-order theorem remains a planned prerequisite, with its precise statement in [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md). Only its uses remain conditional on that proof. Exercise 1 also uses the available Holmgren theorem in [Analytic coefficients and one-sided uniqueness](../AN02-L191.html#3-a-continuously-differentiable-surface-needs-no-analytic-flattening), Theorem 3.2, and the two planned analytic uniqueness prerequisites stated in [Uniqueness from the principal boundary symbol](uniqueness-from-the-principal-boundary-symbol.md).

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The linked lessons supply the prerequisite proofs used below.

## The exact solvability hypothesis

Use coordinates \(x=(a,z,t)\), with normal position \(a\), tangential position \(x'=(z,t)\), time covector \(N=e_t\) and boundary covector \(\theta=e_a\). Let \(P\) be a nonzero complex polynomial of total degree \(m\ge1\), hyperbolic in \(N\), with barrier \(\tau_0\). Let \(h=m_+\) be [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s upper normal count, and let there be exactly \(h\) polynomial boundary operators \(B_1,\ldots,B_h\). Their transported upper monic factor and residue determinant are denoted by \(R_+\) and \(L^\partial\).

Assume that for every forcing \(f\), right smooth on \(\{a\ge0,t\ge0\}\) and flat at \(t=0\), and every boundary datum \(g_j\), smooth on \(\{t\ge0\}\) and flat at \(t=0\), there is a unique right-smooth solution of
\[
\begin{gathered}
P(D)u=f\\
\quad(a>0,t>0),\\
\qquad
 D_t^ju|_{t=0}=0\\
\quad(0\le j<m),\\
\qquad
 B_j(D)u|_{a=0}=g_j .
\end{gathered}
\tag{1}
\]
All corner derivatives are continuous from the quarter-space. No growth bound in \(a,z\) is assumed. The stated hypothesis follows, in particular, from unique solvability of the complete mixed problem for arbitrary smooth data flat at the initial hypersurface, by setting its initial data to zero.

**Theorem.** There is a number \(\gamma_0\le0\), with \(\gamma_0<\tau_0\), such that
\(L^\partial(\xi'+i\gamma N')\ne0\) for every real tangential \(\xi'\) and every \(\gamma<\gamma_0\).
An empty upper factor has \(h=0\) and determinant one, so that case is immediate. In the remainder of the proof \(h\ge1\).

## Right-smooth Fréchet spaces and one fixed estimate

Let \(E\) be the space of jointly right-smooth functions on \(a\ge0\), with time variable ranging over all of \(\mathbb R\), supported in \(t\ge0\). Its seminorms are the suprema of all derivatives up to each finite order on the nested boxes
\(0\le a\le A,\ |z|\le A,\ |t|\le A\), for positive integers \(A\).
Use the corresponding boundary space \(G\), with no \(a\) variable.

These are Fréchet spaces with their stated seminorms. Here is the boundary completeness check. A seminorm-Cauchy sequence has uniformly convergent continuous derivatives of every fixed order on each box. The limits agree on overlapping boxes. The fundamental theorem of calculus along each coordinate segment, including normal segments with endpoint \(a=0\), passes through uniform convergence. It identifies the limit of a derivative with the appropriate coordinate derivative of the limit, with a right derivative at the normal boundary. Iterating this statement gives all orders and their continuous boundary limits. Uniform convergence on boxes gives convergence in every stated seminorm. The limit vanishes at negative time. Countable separating seminorms give the complete metric described in [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) Section14.1. Thus no extension across \(a=0\) has been assumed. The same argument proves completeness of \(G\), and its finite product with \(E\).

Every datum in \(E\) or \(G\) has zero time jets at zero. Conversely a quarter-space function flat at initial time extends by zero to a right-smooth causal function. For the solution in 1 this flatness follows from the equation, rather than from an additional infinitely long initial condition. Its exact time order is \(m\):
\[
\begin{gathered}
P(D)=P_m(N)D_t^m\\
+
       \sum_{j=0}^{m-1}Q_j(D_a,D_z)D_t^j,
       \\
\qquad P_m(N)\ne0 .
\end{gathered}
\tag{2}
\]
Right continuity extends this equation to \(t=0\) for \(a>0\). The given first \(m\) time-jet functions and their spatial derivatives vanish. Every time derivative of \(f\) vanishes there too. Differentiate 2 successively in time: the next highest jet is expressed using only already zero lower jets and a zero forcing jet. Induction gives all time jets zero. Their spatial derivatives vanish as well, and continuity extends the identities to \(a=0\). Taylor's integral remainder, uniformly on compact spatial boxes, proves smoothness of the zero past extension, including the corner. The equation has no time-boundary delta term and the boundary traces extend as the given causal data.

Consequently
\(T:E\longrightarrow E\times G^h,\quad T v=(Pv,(B_jv|_{a=0})_{j=1}^h)\)
is a continuous linear bijection. Continuity follows from the finite differential orders. Surjectivity and injectivity follow from 1 and the preceding extension argument. [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) Section14.4 therefore makes its inverse continuous.

Fix \(T_*=1\), \(c=T_*/2\), and the boundary point \(y=(0,0,T_*)\). The continuous output seminorm is the sum of the first \(h\) normal jets at \(y\). Continuity and scalar rescaling give constants \(C,A,k\), independent of \(v\), such that
\[
\begin{gathered}
\sum_{j=0}^{h-1}|D_a^jv(y)|
 \\
\le C\left\{\|Pv\|_{A,k}
       +\sum_{\nu=1}^h\|B_\nu v|_{a=0}\|_{A,k}\right\}
       \\
\quad(v\in E).
\end{gathered}
\tag{3}
\]
Here each norm means the maximum of derivatives of order at most \(k\) on the relevant box, restricted to nonnegative time; increasing \(A,k\) combines the finite collection of input seminorms. If their finite maximum is zero, arbitrary scalar rescaling gives zero output; otherwise rescale into the fixed continuity neighborhood. This proves 3 also on its zero seminorm set.

## A normalized mode at a determinant zero

Choose once and for all \(\gamma_*<\min(\tau_0-1,-1)\). For
\(\zeta'=\xi'+i\gamma N'\), with \(\xi'\) real and \(\gamma<\gamma_*\), the zero normal representative belongs to [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s tube. Its factors have their actual upper/lower meanings. [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s coefficient bounds are uniform here: translating the frequency by \(-i(\tau_0-1)N\) places it in the smaller negative cone of [equation 18 in Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md), while translating the polynomial by \(+i(\tau_0-1)N\) makes its barrier one. The two translations cancel in its values and leave at least one unit of original time-cone margin.

Suppose \(L^\partial(\zeta')=0\). The square boundary matrix is singular. Choose its nonzero null polynomial \(H(w)\), of degree below \(h\), and normalize the sum of the absolute values of its coefficients to one. Thus
\[
\begin{gathered}
\|H\|_{\mathrm{coef},1}=1,\\
\qquad
 \beta_{R_+}(B_\nu,H)=0\ (1\le\nu\le h),\\
\qquad
 U(a)=\frac1{2\pi i}\int_{\mathcal C_+}
       \frac{H(w)e^{iaw}}{R_+(w,\zeta')}\,dw .
\end{gathered}
\tag{4}
\]
The finite positive contour surrounds all upper roots, with multiplicities. The interior equation cancels \(R_+\) and leaves an entire integrand, so \(P(D_a,\zeta')U=0\). At the boundary, applying \(B_\nu\) gives precisely the zero residue pairing in 4. Differentiating in \(a\) gives the jets
\(J_j=D_a^jU(0)=[w^{-1}]w^jH(w)/R_+(w,\zeta')\).
All these statements hold at repeated roots.

The first \(h\) jets reconstruct \(H\) exactly:
\[
 H(w)=
 \left[R_+(w,\zeta')
       \sum_{j=0}^{h-1}\frac{J_j}{w^{j+1}}\right]_+ .
 \tag{5}
\]
Indeed the Laurent expansion of \(H/R_+\) begins with
\(\sum_{j=0}^{h-1}J_jw^{-j-1}\), and its remainder is \(O(w^{-h-1})\). Multiplication by the monic degree-\(h\) factor leaves a remainder \(O(w^{-1})\); taking the polynomial part proves 5. Each polynomial part \( [R_+/w^{j+1}]_+\) has coefficient norm at most that of \(R_+\). [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s polynomial coefficient bound therefore gives fixed \(C_0,M_0\) with
\[
\begin{gathered}
1\\
=\|H\|_{\mathrm{coef},1}
   \\
\le \|R_+(\cdot,\zeta')\|_{\mathrm{coef},1}
          \sum_{j=0}^{h-1}|J_j|
   \\
\le C_0(1+|\zeta'|)^{M_0}
          \sum_{j=0}^{h-1}|J_j| .
\end{gathered}
\tag{6}
\]
This detects a jet without assuming that the value \(U(0)\) itself is nonzero.

There are uniform polynomial bounds for every fixed number of normal derivatives of \(U\). If \(R_+(w)=w^h+\sum_{j<h}c_jw^j\), a root has modulus at most \(1+\sum_{j<h}|c_j|\): for a larger modulus, the leading term strictly dominates the sum of the lower terms. [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s coefficient bound therefore bounds all root moduli polynomially. Surround the upper roots by disks of a common radius between one and two, choosing a radius away from the finitely many tangencies. The outer union boundary has length at most \(4\pi h\), distance at least one from every root, and imaginary part at least minus two. On it \(|R_+|\ge1\), the normalized \(H\) has polynomial modulus, and \(|e^{iaw}|\le e^{2a}\) for \(a\ge0\). Hence, for each fixed \(r\),
\[
\begin{gathered}
|D_a^rU(a)|\le C_r e^{2a}(1+|\zeta'|)^{M_r}
       \\
\quad(a\ge0,\ \gamma<\gamma_*).
\end{gathered}
\tag{7}
\]
No root separation or globally continuous choice of \(H\) is required. Each frequency is tested separately, and its coefficient normalization makes all constants uniform.

## Cutting time and obtaining a logarithmic bound

Let \(\chi\in C^\infty(\mathbb R)\) be zero for \(t\le0\) and one for \(t\ge c\). Such a cutoff is supplied by the compact smooth-cutoff prerequisite, with a rescaled transition interval. Set
\(\mathcal U(a,z,t)=U(a)e^{i x'\cdot\zeta'}\) and \(v=\chi(t)\mathcal U\).
The mode solves \(P\mathcal U=0\), with all its homogeneous boundary traces zero. Thus \(v\in E\), while its forcing and boundary data vanish for \(t\ge c\). Their possibly nonzero terms are finite Leibniz commutators involving positive derivatives of \(\chi\), supported in \(0\le t\le c\).

On that interval the modulus of the tangent exponential is \(e^{-\gamma t}\le e^{-\gamma c}\). Its spatial and time derivatives multiply it by powers of \(\zeta'\). Apply 7 on \(0\le a\le A\), including every derivative needed by the finite orders of \(P,B_\nu\) and 3. The fixed cutoff derivatives then give constants independent of this frequency:
\[
\begin{gathered}
\|Pv\|_{A,k}
  +\sum_{\nu=1}^h\|B_\nu v|_{a=0}\|_{A,k}
       \\
\le C_1(1+|\zeta'|)^{M_1}e^{-\gamma c}.
\end{gathered}
\tag{8}
\]
At \(y\), \(\chi=1\), so the output in 3 is exactly
\(e^{-\gamma T_*}\sum_{j<h}|J_j|\). Consequently
\[
 \sum_{j=0}^{h-1}|J_j|
       \le C_2(1+|\zeta'|)^{M_1}
                    e^{\gamma(T_*-c)} .
 \tag{9}
\]
Combine this with 6, enlarge the constant to at least one and the exponent to a nonnegative integer, and put \(d_*=T_*-c>0\):
\[
\begin{gathered}
1\le C_3(1+|\zeta'|)^{M_2}e^{d_*\gamma},
 \\
\qquad
 -\gamma\le d_*^{-1}\log C_3
          \\
+(M_2/d_*)\log(1+|\zeta'|).
\end{gathered}
\tag{10}
\]
This estimate holds at every determinant zero with \(\gamma<\gamma_*\). By itself it permits negative imaginary frequencies with magnitude comparable to a logarithm. The real-algebraic step rules out that remaining possibility.

## The zero set and an unattained supremum

The bad set
\[
\begin{gathered}
S\\
=\left\{\begin{gathered}(\xi',\gamma)\in\mathbb R^{n-1}\times\mathbb R:\\
       \gamma<\gamma_*,\
       L^\partial(\xi'+i\gamma N')\\
=0\end{gathered}\right\}
\end{gathered}
\tag{11}
\]
is semialgebraic. We spell out its finite polynomial description, rather than calling the analytic determinant itself a polynomial.

The normal degree \(d\), upper count \(h\), lower count \(d-h\), and leading normal coefficient \(q(\zeta')\ne0\) are fixed by [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md) on these frequencies. Introduce \(d\) complex root variables, represented by their real and imaginary coordinates. Require their first \(h\) imaginary parts to be positive and all remaining ones to be negative. Require the coefficient identity
\(P(w,\zeta')=q(\zeta')\prod_{\ell=1}^d(w-\lambda_\ell)\).
This is finitely many real polynomial equalities in \(\xi',\gamma\) and the root coordinates. Repetitions are allowed. The first \(h\) variables define a monic polynomial \(R_+\); its coefficients are polynomials in those variables. [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md)'s finite Laurent recurrence says that every
\(\beta_{R_+}(B_\nu,w^j)\), for \(0\le j<h\), is a polynomial in the coefficients of \(R_+,B_\nu\). Requiring real and imaginary parts of the resulting determinant to be zero adds two real polynomial equalities.

For every frequency under consideration these root variables exist, and the prescribed strict halfplane signs identify exactly the actual upper factor, including multiplicities. Conversely every set of variables satisfying these constraints gives that same factor and its determinant. Projecting away the root variables gives precisely S. [Symbols at infinity](symbols-at-infinity.md) Lemma2.1 proves that such finite real polynomial projections are semialgebraic. No algebraic root label, simple-root assumption, or zero-free individual branch has entered this argument.

For \(R\ge1\) define
\[
\begin{gathered}
F(R)\\
=\sup\left(\begin{gathered}\{0\}\cup\\
       \left\{\begin{gathered}-\gamma:(\xi',\gamma)\in S,\
                    \\
|\xi'|^2+\gamma^2\le R^2\end{gathered}\right\}\end{gathered}\right),
 \\
\qquad 0\le F(R)\le R .
\end{gathered}
\tag{12}
\]
It is nondecreasing and finite. Its graph is semialgebraic even if its supremum is not attained: a number \(y\) is its value exactly when \(y\ge0\), every member of the displayed set is at most \(y\), and for every \(\epsilon>0\) the displayed set has a member greater than \(y-\epsilon\). Include the member zero in both quantifiers. These are finite real polynomial quantifiers using the description of S, so [Symbols at infinity](symbols-at-infinity.md) Lemma2.1 applies.

10 gives \(F(R)\le A_0+A_1\log(1+R)\) after increasing \(A_0\ge0\). We prove that a nondecreasing semialgebraic function with this bound must be bounded, exposing the polynomial mechanism from [equation 18 in Analytic root barriers and supported solvability](analytic-root-barriers-and-supported-solvability.md)–[equation 21 in Analytic root barriers and supported solvability](analytic-root-barriers-and-supported-solvability.md).

If \(F\) were unbounded, monotonicity would give \(F(R)\to\infty\). Choose a finite polynomial-sign formula for its graph and discard identically zero polynomials in that formula. The graph has empty two-dimensional interior. At every graph point at least one of its nonzero defining polynomials must vanish: otherwise their signs would stay constant on a small ball, and the formula would include that whole ball, impossible for a function graph. Their product is a nonzero polynomial \(A\) satisfying
\[
\begin{gathered}
A(R,F(R))=0,\\
\qquad
 A(R,y)=\sum_{j=0}^J R^j a_j(y),\\
\qquad a_J\ne0 .
\end{gathered}
\tag{13}
\]
If \(J=0\), the nonzero polynomial \(a_0\) has only finitely many real roots, contradicting \(F(R)\to\infty\). For \(J>0\), put \(l=\deg a_J\) and \(D=\max_j\deg a_j\). For large positive \(y\), the leading coefficient polynomial has modulus at least \(c_0y^l\), while all lower coefficient polynomials have modulus at most \(C_0'y^D\). Divide 13 by \(R^J\). For all sufficiently large \(R\),
\[
 c_0F(R)^l\le (C_0''/R)F(R)^D .
 \tag{14}
\]
If \(D=l\), this is impossible when \(R\) is large. If \(D>l\), it forces
\(F(R)\ge c_1R^{1/(D-l)}\), contradicting its logarithmic upper bound. A positive power dominates a logarithm; the explicit integral comparison in Exercise3 below verifies that limit. Thus F is bounded.

Every point of S occurs in the norm ball of some radius R. A common bound \(F(R)\le M_*\) therefore bounds \(-\gamma\) on all of S. Choose \(\gamma_0<\min(\gamma_*,-M_*-1)\). There are no bad frequencies below it:
\[
\begin{gathered}
L^\partial(\xi'+i\gamma N')\ne0
       \\
\quad(\xi'\in\mathbb R^{n-1},\
                       \gamma<\gamma_0<\min(0,\tau_0)).
\end{gathered}
\tag{15}
\]
This proves the theorem, including the case S is empty. It also excludes an identically zero determinant under the solvability hypothesis.

For independent original time and boundary covectors, use an invertible real linear coordinate map taking the two defining physical linear functions to positive multiples of \(t,a\). A smooth seminorm on a compact set transforms into a finite bound by smooth seminorms on the compact image, and the inverse map gives the reverse bound, by the finite derivative chain rule. Causal support, right boundary derivatives and flat initial jets are preserved. The dual map transports the time-frequency line and normal factorization; any positive time scaling multiplies its imaginary parameter by a fixed positive number. Thus the existence of a uniform lower strip transports back as well. No Euclidean orthogonality of the original covectors is needed.

## The term hyperbolic for a mixed system

For a balanced system, the three conditions are: the boundary count equals the upper normal count; its principal boundary symbol is nonzero at the time direction; and the determinant has the lower-time zero-free strip just proved necessary. Such a system is called a hyperbolic mixed problem. This definition records those exact conditions. It does not by itself prove existence under them. [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md) and [Degenerate boundary symbols and smooth nonuniqueness](degenerate-boundary-symbols-and-smooth-nonuniqueness.md) supply the other necessary obstructions at their stated scopes; The zero-free-region extension and the general mixed-existence construction are developed in the following lessons.

## Exercises with complete solutions

**Exercise 1 (entry: uniqueness and a bad time strip can coexist).** In coordinates \((a,z,t)\) take
\[
\begin{gathered}
P(\xi,y,s)=(s-i)^2-\xi^2,\\
\qquad
 B_1(\xi,y,s)=(s-i)^2+y^2,\\
\qquad
 L^\partial(y,s)=(s-i)^2+y^2 .
\end{gathered}
\tag{16}
\]
Find the upper count, principal boundary symbol and the determinant zeros with arbitrarily negative imaginary time. Explain why uniqueness of existing smooth solutions does not imply existence for all smooth data in this example.

**Solution.** The variable y is an unused real spatial frequency in the interior polynomial. Its two time roots for real normal \(\xi\) are \(s=i+\xi,i-\xi\), so it is hyperbolic in time. On \(\operatorname{Im}s<0\) the normal roots are \(i-s\) and \(s-i\), with positive and negative imaginary parts respectively. Thus \(h=1\), the upper factor is \(w+s-i\), and the tangent-only boundary symbol has the determinant displayed in 16. Its principal degree is two and its principal symbol is \(s^2+y^2\), which takes value one at \(N'=(0,1)\). [Uniqueness from the principal boundary symbol](uniqueness-from-the-principal-boundary-symbol.md) therefore gives uniqueness of existing smooth solutions relative to its explicitly planned bases.

For real \(r>1\), set \(y=r,s=i(1-r)\). The determinant is \((-ir)^2+r^2=0\), with imaginary time tending to minus infinity. The associated exact homogeneous mode is
\[
\begin{gathered}
\mathcal U_r(a,z,t)=e^{-ra}e^{irz+(r-1)t},\\
\qquad
 P(D)\mathcal U_r=0,\\
\qquad
 B_1(D)\mathcal U_r|_{a=0}=0 .
\end{gathered}
\tag{17}
\]
Indeed \(D_a\) acts by \(ir\), \(D_z\) by r and \(D_t\) by \(i(1-r)\), so both polynomial identities vanish. It is not causal and hence does not contradict uniqueness. Multiplying by the fixed cutoff used in 8 gives a causal test with value \(e^{(r-1)T_*}\) at the output, whereas every fixed finite input seminorm is at most a polynomial in r times \(e^{(r-1)c}\). Their ratio grows exponentially because \(T_*>c\). Therefore the continuous inverse estimate required by unique solvability for every datum fails. The theorem proves that at least one smooth flat datum has no solution; it does not claim that every datum is insoluble, nor identify a particular datum by this estimate.

**Exercise 2 (intermediate: detect a repeated upper root).** Let \(R_+(w)=(w-\lambda)^2\), with \(\operatorname{Im}\lambda>0\), and \(H(w)=A+Bw\). Compute the contour mode and its first two normal jets. Reconstruct H and bound its coefficient norm by those jets.

**Solution.** The double-pole residue differentiates \(H(w)e^{iaw}\) at \(w=\lambda\). Hence
\[
\begin{gathered}
U(a)=e^{ia\lambda}\{B+ia(A+\lambda B)\},\\
\qquad
 J_0=B,\\
\quad J_1=A+2\lambda B,\\
\qquad
 H(w)=J_0w+J_1-2\lambda J_0 .
\end{gathered}
\tag{18}
\]
The formula for \(J_1\) follows by applying \(D_a=-i\partial_a\) at zero. Multiplying
\((w-\lambda)^2(J_0/w+J_1/w^2)\) and taking its polynomial part gives the same expression, verifying 5 at the repeated root. In particular
\[
 |A|+|B|
    \le |J_1|+(1+2|\lambda|)|J_0| .
 \tag{19}
\]
If \(U(0)=J_0=0\), H can still be nonzero: take \(B=0,A=1\), when \(J_1=1\). Both jets zero force H zero. A value-only normalization would lose this valid mode; the finite jet sum in 3 and 6 detects it.

**Exercise 3 (advanced: a nonattained supremum and the power gap).** For \(R>1\), consider the open fiber \(0<q<\sqrt R\). Write polynomial quantifiers defining its supremum, exhibit its annihilating polynomial, and derive the sharp positive-power bound from the leading-R coefficient argument. Prove explicitly that no logarithmic upper bound can hold for that supremum.

**Solution.** The fiber condition is \(q>0,q^2<R\). Its supremum is characterized by y being an upper bound and, for every \(\epsilon>0\), a member q being greater than \(y-\epsilon\). This gives \(y=\sqrt R\), although y itself is excluded from the fiber:
\[
\begin{gathered}
F(R)=\sup\{q:q>0,\ q^2<R\}\\
=\sqrt R,\\
\qquad
 A(R,y)=R-y^2,\\
\qquad A(R,F(R))=0 .
\end{gathered}
\tag{20}
\]
The highest-R coefficient is \(a_1=1\), of degree \(l=0\), and the lower coefficient is \(a_0=-y^2\), so \(D=2\). Dividing the exact identity by R gives \(1=F(R)^2/R\), hence \(F(R)=R^{1/2}\). This is exactly the power \(1/(D-l)\) of 14. The nonattainment has no effect on the upper-bound and arbitrary-accuracy quantifiers.

For any \(\alpha>0\) and \(R\ge1\),
\[
\begin{gathered}
\log R=\int_1^R t^{-1}\,dt
       \\
\le \int_1^R t^{\alpha/2-1}\,dt
       \\
=\frac{2}{\alpha}(R^{\alpha/2}-1),\\
\qquad
 \frac{\log R}{R^\alpha}\longrightarrow0 .
\end{gathered}
\tag{21}
\]
The inequality follows because \(t^{\alpha/2}\ge1\). Dividing its right side by \(R^\alpha\) tends to zero, which proves the displayed limit. Also \(\log(1+R)\le\log2+\log R\) for \(R\ge1\). Thus a bound \(F(R)\le A+B\log(1+R)\) contradicts \(F(R)\ge cR^\alpha\) for every positive c and \(\alpha\). Taking \(\alpha=1/2\) proves the assertion for the open fiber, and the same calculation completes the general contradiction in 14.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
