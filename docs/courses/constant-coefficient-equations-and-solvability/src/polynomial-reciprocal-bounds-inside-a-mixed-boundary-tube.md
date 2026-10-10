# Polynomial reciprocal bounds inside a mixed boundary tube

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Zero-freeness gives a reciprocal at each frequency. The boundary-kernel construction needs one polynomial bound valid as frequency and imaginary displacement both grow. We prove that bound on a closed tube lying one time unit inside the zero-free tube. The selected normal factor, the principal cone and a compact-fiber minimum all receive finite polynomial descriptions. A direct monic root bound then controls the reciprocal, without a Puiseux expansion.

Read [Extending a boundary time strip to its propagation cone](extending-a-boundary-time-strip-to-its-propagation-cone.md), [Symbols at infinity](symbols-at-infinity.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Fourier convention and Gaussian formula; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies scalar calculus and cutoffs. [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) supplies finite scalar and polynomial algebra. 

The general hyperbolic-cone theorem is proved in [Real roots and their convex component](../AN02-L192.html#4-pass-to-multiple-roots-and-obtain-convexity), Theorem 4.1. The analytic zero-order theorem remains a planned prerequisite, with its precise statement in [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md). Only its uses remain conditional on that proof.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The linked lessons supply the prerequisite proofs used below.

## The precise closed tube

Use [Extending a boundary time strip to its propagation cone](extending-a-boundary-time-strip-to-its-propagation-cone.md)'s notation and original strip parameter: \(\Sigma\) is the open convex principal nonzero cone containing \(N'\), and \(L=L^\partial\) is holomorphic and nonzero when \(\operatorname{Im}\zeta'\in\gamma_0N'-\Sigma\). Work in [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s barrier-one normalization, or with an original barrier \(\tau_0\) and a strip bound \(\gamma_0\le\min(0,\tau_0)\). All the following statements concern that chosen bound. Define
\[
\begin{gathered}
K=\{\zeta'\in\mathbb C^{n-1}:
       \\
\operatorname{Im}\zeta'\in(\gamma_0-1)N'-\overline\Sigma\}.
 \\
\qquad
 (1+|\zeta'|)^{-M}\le C|L(\zeta')|
                         \\
\quad(\zeta'\in K).
\end{gathered}
\tag{1}
\]
**Lemma.** There are \(C>0\) and an integer \(M\ge0\) for which the displayed bound holds.
The norm is any fixed Euclidean norm on real and imaginary quotient coordinates.

The buffer of one unit matters. Since \(N'\in\Sigma\), we have
\(N'+\overline\Sigma\subset\Sigma\). To verify this without a closure substitution, take \(v_j\in\Sigma\) tending to \(v\in\overline\Sigma\). For large \(j\), the point \(N'+v-v_j\) is inside the open cone, near \(N'\). Its sum with \(v_j\) is \(N'+v\), and an open convex cone is closed under addition. Thus every point of K lies in the open [Extending a boundary time strip to its propagation cone](extending-a-boundary-time-strip-to-its-propagation-cone.md) zero-free tube. The closure in 1 does not include any zero of L.

## Finite polynomial descriptions of the selected objects

We need the actual selected determinant, not merely a polynomial relation with all its algebraic branches. First the interior cone is semialgebraic. Divide the homogeneous principal polynomial by \(P_m(N)\) so its time-leading coefficient is one. The available homogeneous-cone theorem states that its coefficients are real and that a real vector \(v\) belongs to \(\Gamma(P_m,N)\) exactly when all the roots of its time-line polynomial are real and strictly negative. Consequently
\[
\begin{gathered}
v\in\Gamma
 \\
\quad\Longleftrightarrow\\
\quad
 \exists r_1,\ldots,r_m<0:\\
\quad
 P_m(v+sN)=P_m(N)\prod_{j=1}^m(s-r_j).
\end{gathered}
\tag{2}
\]
The coefficient identities are finitely many real polynomial equations. Repeated roots are permitted. [Symbols at infinity](symbols-at-infinity.md) projection makes \(\Gamma\) semialgebraic, and makes its real image \(\Omega=\pi\Gamma\) semialgebraic too. This uses the available cone theorem at its stated scope, with the full proof in [Real roots and their convex component](../AN02-L192.html#4-pass-to-multiple-roots-and-obtain-convexity), Theorem 4.1.

We next describe the graph of L on its original projected tube
\(\mathcal T_{\tau_0}=\{\zeta':\operatorname{Im}\zeta'\in\tau_0N'-\Omega\}\).
Choose coordinates \(\theta=e_a,N=e_t\). For \(\zeta'\) in this tube introduce a complex normal representative \(v\) with
\(\operatorname{Im}(v,\zeta')\in\tau_0N-\Gamma\).
Represent all complex variables by their real and imaginary parts. Introduce \(d=h+\ell\) complex roots \(\lambda_j\), the first \(h\) strictly upper and the rest strictly lower, and impose
\[
\begin{gathered}
P(v+w,\zeta')=q(\zeta')\prod_{j=1}^d(w-\lambda_j),
 \\
\qquad
 R_+(w,\zeta')=\prod_{j=1}^h(w-v-\lambda_j).
\end{gathered}
\tag{3}
\]
The first identity is the coefficient identity at the admissible full representative. Its leading coefficient \(q\) is nonzero by [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md). The second is [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s transport to zero normal representative: its roots there are \(v+\lambda_j\), which need not themselves be upper. All factors are selected by the signs at the admissible representative, not by a false upper sign at zero representative.

Each entry \(\beta_{R_+}(B_\nu,w^j)\) is a polynomial in the coefficients of the monic \(R_+\) and the polynomial \(B_\nu\), by [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md)'s finite Laurent recurrence. Its determinant is therefore a polynomial in the introduced variables. Equate that determinant to a new complex value \(l\), impose all the above real and imaginary coefficient equations and sign conditions, and project away the representative and roots. This gives a semialgebraic graph. It is exactly the graph of L: every actual frequency has an admissible lift and the selected roots, and [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s normal covariance makes every allowed lift give the same determinant. This also treats repeated roots, an empty lower factor and \(h=0\), whose determinant is one. Denote this actual graph by \(\mathcal G_L\).

The principal symbol on real \(\Omega\) has a semialgebraic graph as well. Its value at a real \(\eta'\in\Omega\) is the unique complex \(\lambda\) satisfying the limit
\[
 \epsilon^\kappa L(-i\eta'/\epsilon)
          \longrightarrow(-i)^\kappa\lambda,\qquad
                        \epsilon\downarrow0 .
 \tag{4}
\]
For small positive \(\epsilon\), the displayed frequency is in \(\mathcal T_{\tau_0}\): its membership means
\(\eta'/\epsilon+\tau_0N'\in\Omega\), which follows by openness at \(\eta'\) and positive scaling. [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md)'s analytic germ proves that the limit is precisely
\((-i)^\kappa\widehat\Lambda_0(\eta')\).

Here is a polynomial description of that limit. For every real \(\delta>0\), require an \(r>0\) such that, for every \(0<\epsilon<r\), there exist complex \(\zeta',l\) with
\(\epsilon\zeta'=-i\eta'\), \((\zeta',l)\in\mathcal G_L\), and
\(|\epsilon^\kappa l-(-i)^\kappa\lambda|^2<\delta^2\).
The graph of L is single-valued, so this is the actual limit condition, and the existence clause prevents a vacuous test outside its domain. For \(\kappa\ge0\) the last condition is already polynomial in real coordinates. For \(\kappa=-p<0\), rewrite it as
\(|l-(-i)^\kappa\epsilon^p\lambda|^2<\delta^2\epsilon^{2p}\).
Only multiplication by a positive power of the positive \(\epsilon\) was used. [Symbols at infinity](symbols-at-infinity.md) handles these finitely many real quantifiers. We have therefore described the graph of the actual principal value, not an arbitrary branch of an annihilating polynomial.

The component \(\Sigma\) now has a finite polynomial description too. [Extending a boundary time strip to its propagation cone](extending-a-boundary-time-strip-to-its-propagation-cone.md) proved it star-shaped with respect to \(N'\). Thus
\[
\begin{gathered}
\eta'\in\Sigma
 \\
\quad\Longleftrightarrow\\
\quad
 \eta'\in\Omega,\\
\quad
 \widehat\Lambda_0((1-u)N'+u\eta')\ne0
                        \\
\quad\hbox{for every }0\le u\le1 .
\end{gathered}
\tag{5}
\]
The forward implication is the star property. Conversely the segment lies in the original projected cone by convexity, and the displayed nonzero condition puts the whole segment in the principal nonzero set. It connects \(\eta'\) to \(N'\) and so puts it in the same connected component. The principal graph just constructed and the universal \(u\)-quantifier make 5 semialgebraic. This argument avoids using an unwritten theorem that all semialgebraic components are semialgebraic.

Finally \(\overline\Sigma\) is semialgebraic: membership means that for every positive \(\delta\) there is a point of \(\Sigma\) within \(\delta\). [Symbols at infinity](symbols-at-infinity.md) again eliminates the finitely many real quantifiers. The set
\[
 \operatorname{Im}\zeta'=(\gamma_0-1)N'-v,\qquad
                         v\in\overline\Sigma
 \tag{6}
\]
is closed and semialgebraic and is exactly K. All graph uses of L below are in its actual projected tube, as established before 2.

## A positive compact-fiber minimum

The origin is in \(\overline\Sigma\), by positive scaling toward zero. Thus \(K\) contains
\(\zeta'_0=i(\gamma_0-1)N'\). Choose \(R_0>1+|\zeta'_0|\). For \(R\ge R_0\), the closed bounded set \(K\cap\{|\zeta'|\le R\}\) is nonempty and compact. The actual continuous determinant has no zero there. Hence
\[
\begin{gathered}
f(R)=\min_{\substack{\zeta'\in K\\|\zeta'|\le R}}
                       |L(\zeta')|>0,\\
\qquad
 g(R)=1/f(R)>0 .
\end{gathered}
\tag{7}
\]
The minimum is attained. It is nonincreasing in R, so g is finite and nondecreasing.

The graph of f is semialgebraic. A positive \(q\) is its value if some \((\zeta',l)\in\mathcal G_L\) in the specified compact fiber satisfies \(|l|^2=q^2\), and every graph point in that fiber satisfies \(|l|^2\ge q^2\). These are real polynomial conditions using 6. Taking a reciprocal with \(qg=1\) makes the graph of g semialgebraic. Square roots or nonattainment have not been hidden in its graph description.

Choose a finite polynomial-sign formula defining that graph, discarding any identically zero defining polynomials. A function graph has empty two-dimensional interior. At each graph point at least one of those nonzero polynomials must vanish: otherwise all their signs would be constant in a small ball that the formula would include. Their nonzero product gives
\[
\begin{gathered}
A(R,g(R))=0,\\
\qquad
 A(R,y)=\sum_{j=0}^d b_j(R)y^j,\\
\qquad b_d\ne0 .
\end{gathered}
\tag{8}
\]
Here \(d\ge1\). If \(d=0\), a nonzero polynomial \(b_0(R)\) would vanish at every \(R\ge R_0\), impossible.

Let \(l=\deg b_d\) and \(D=\max_j\deg b_j\), so \(D\ge l\). For sufficiently large R the leading coefficient satisfies
\(|b_d(R)|\ge cR^l>0\), and the sum of all lower coefficient moduli is at most \(CR^D\). Divide 8 by \(b_d\). The elementary monic root bound gives
\[
\begin{gathered}
g(R)\\
\le1+\sum_{j<d}|b_j(R)/b_d(R)|
        \\
\le C'(1+R)^{D-l}.
\end{gathered}
\tag{9}
\]
For completeness, a root of \(y^d+\sum_{j<d}c_jy^j\) has modulus at most \(1+\sum_{j<d}|c_j|\): at a larger modulus, the leading term strictly dominates the sum of the lower terms. This proof works for every branch and does not require an asymptotic series for g.

The finitely bounded initial interval causes no difficulty: its values satisfy \(g(R)\le g(R_1)\) by monotonicity for a sufficiently large fixed \(R_1\). Enlarge the constant in 9 and put \(M=D-l\ge0\). Given any \(\zeta'\in K\), choose \(R=\max(R_0,|\zeta'|)\). Since \(f(R)\le|L(\zeta')|\), the reciprocal bound in 9 implies 1, after the fixed comparison
\(1+R\le(1+R_0)(1+|\zeta'|)\).
This proves the complete lemma with an integer exponent and constants independent of all points of K.

## Polynomially bounded boundary inverse matrices

The same buffered set also gives the numerator bounds needed next. For \(\zeta'\in K\), write its imaginary part as \((\gamma_0-1)N'-v\), \(v\in\overline\Sigma\). For every real \(b<1\), the frequency \(\zeta'+ibN'\) remains in the original projected [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md) tube, because
\((\tau_0-\gamma_0+1-b)N'+v\in\Omega\).
The coefficient of \(N'\) is positive. A positive multiple of \(N'\) plus a point of \(\overline\Sigma\) belongs to \(\Sigma\), by the buffered-cone argument already proved.

[Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s projected zero exclusion therefore gives \(q(\zeta'+ibN')\ne0\) for all \(b<1\). The polynomial \(z\mapsto q(\zeta'+zN')\) has fixed degree \(m_0\) and leading coefficient \(G(N)\ne0\). Absorb the real part of a putative root into the real frequency. Every root has imaginary part at least one, so factoring at \(z=0\) gives \(|q(\zeta')|\ge|G(N)|\). For \(m_0=0\) this is the equality for the nonzero constant q.

As in [equation 8 in Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)–[equation 10 in Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md), divide the normal polynomial by q, apply the monic root bound and Vieta's finite coefficient identities, then the finite Laurent recurrence. The selected transported factors, residue matrix and its cofactors are all polynomially bounded on K. 1 consequently gives
\[
\begin{gathered}
M^\partial(\zeta')^{-1}
       =\frac{\operatorname{adj}M^\partial(\zeta')}{L(\zeta')},
 \\
\qquad
 |(M^\partial)^{-1}_{jk}(\zeta')|
       \le C_1(1+|\zeta'|)^{M_1}
                         \\
\quad(\zeta'\in K).
\end{gathered}
\tag{10}
\]
They are holomorphic on the open zero-free tube. At \(h=0\), the inverse matrix is the empty identity and no boundary kernels are required. This proves a matrix coefficient estimate, not a Fourier–Laplace kernel construction. In particular it makes no false assertion that transported upper roots remain upper on every projected complex frequency.

## Exercises with complete solutions

**Exercise 1 (entry: an exact minimum at negative degree).** Let \(L(s)=1/(s-i)\), with \(\gamma_0=0\) and \(\Sigma=(0,\infty)\). Find f and g for \(K=\{\operatorname{Im}s\le-1\}\), using \(R\ge1\). Identify the polynomial for g and an optimal growth exponent.

**Solution.** Maximizing \(|s-i|\) over this compact disk fiber minimizes \(|L|\). The triangle inequality gives \(|s-i|\le R+1\), and equality occurs at \(s=-iR\), which lies in K. Hence
\[
\begin{gathered}
f(R)=\frac1{R+1},\\
\qquad g(R)=R+1,\\
\qquad
 A(R,y)=y-R-1 .
\end{gathered}
\tag{11}
\]
The highest-y coefficient has degree zero in R, and the lower coefficient has degree one. 9 gives \(M=1\), exactly the actual growth order. Any exponent \(M<1\) would fail as \(R\to\infty\). The principal determinant has degree \(-1\), but its reciprocal has the required polynomial growth.

**Exercise 2 (intermediate: a direct wave bound).** For [Extending a boundary time strip to its propagation cone](extending-a-boundary-time-strip-to-its-propagation-cone.md)'s wave determinant
\(L(y,s)=s/2-q(y,s)\), \(q^2=s^2-y^2\), let \(c=\sqrt3/2\) and
\(\Sigma=\{(v_y,v_s):v_s>0,\ |v_y|<cv_s\}\).
On its buffered tube
\(\operatorname{Im}y=-v_y,\operatorname{Im}s=-1-v_s\),
where \(v_s\ge0,|v_y|\le cv_s\), prove a polynomial lower bound directly.

**Solution.** The selected q branch is the actual analytic one in the lower interior projected cone; the buffered set lies there. Its sign is immaterial to the following identities:
\[
\begin{gathered}
L(s/2+q)\\
=y^2-\tfrac34s^2\\
=(y-cs)(y+cs),\\
\qquad
 |\operatorname{Im}(y\pm cs)|\ge c .
\end{gathered}
\tag{12}
\]
Indeed the two imaginary parts are \(-v_y\mp c(1+v_s)\); their absolute values are at least c by \(|v_y|\le cv_s\). Thus the product has modulus at least \(c^2=3/4\) and neither factor nor \(s/2+q\) can vanish. Also
\(|q|^2=|s^2-y^2|\le |s|^2+|y|^2=|(y,s)|^2\).
It follows that
\[
\begin{gathered}
|L(y,s)|\\
\ge\frac{3/4}{(3/2)|(y,s)|}
           \\
=\frac1{2|(y,s)|}
           \\
\ge\frac1{2(1+|(y,s)|)} .
\end{gathered}
\tag{13}
\]
The frequency norm is nonzero since \(|\operatorname{Im}s|\ge1\). This is a valid uniform estimate with exponent one; no claim that the exponent is optimal for this wave boundary is made. The margin of one time unit gives the fixed nonzero imaginary parts in 12.

**Exercise 3 (advanced: a leading coefficient can depend on R).** On \(R\ge2\), let \(g(R)=R^2/(R-1)\). Find its polynomial relation, compute the exponent \(D-l\) from 9, and control the initial interval without replacing the leading coefficient by a constant.

**Solution.** The relation and coefficient degrees are
\[
\begin{gathered}
(R-1)g(R)-R^2=0,\\
\qquad
 b_1(R)=R-1,\\
\quad b_0(R)=-R^2,\\
\quad l=1,\ D=2 .
\end{gathered}
\tag{14}
\]
For \(R\ge2\), \(R-1\ge R/2\). Thus \(g(R)\le2R\), with the exponent \(D-l=1\). Also \(g(R)\ge R\), so a smaller asymptotic growth exponent would fail. Differentiation gives
\[
\begin{gathered}
g'(R)=\frac{R(R-2)}{(R-1)^2}\ge0,\\
\qquad
 R\le g(R)\le2R,\\
\qquad
 \frac1{g(R)}\ge\frac1{2R}.
\end{gathered}
\tag{15}
\]
The leading coefficient's zero at \(R=1\) is outside the domain; it cannot be divided out before that fact is checked. On any finite initial interval \([2,R_1]\), monotonicity bounds g by its finite endpoint value, exactly the extension step after 9. The degree-one leading coefficient improves the bound from the lower coefficient's raw degree two to the correct growth degree one.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
