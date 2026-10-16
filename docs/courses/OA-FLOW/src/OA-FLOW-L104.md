# Compact translations and twisted torus actions

Translations on any compact Hausdorff abelian group have scalar character fibers. Scalar fixed points also force one-dimensional nonzero fibers for general compact abelian actions, but the products of those fibers may carry nontrivial phases. A concrete two-torus action shows why the circle classification does not extend to arbitrary compact abelian groups.

*Original expression: CC0-1.0 to the extent of rights held.*

<a id="oa-flow.compact.translation"></a>

## Character fibers on a compact abelian group

Let \(G\) be compact Hausdorff abelian, with normalized Haar measure and additive notation. For a continuous character \(\chi_p:G\to\mathbb T\), let
\[
 (\alpha_sf)(t)=f(t+s),\qquad f\in L^\infty(G).
 \tag{T1}
\]
All functions here are Haar equivalence classes. Haar conventions, density of continuous functions in \(L^1\), and continuity of \(L^1\) translations are supplied by [L24](OA-FLOW-L24.md#oa-flow.grp.haarconventions). The preadjoint of \(\alpha_s\) is \(g(t)\mapsto g(t-s)\); as in L102, \(L^1\) is exactly the normal functional space of the multiplication algebra on \(L^2(G)\). The factorization \(g=\xi\overline\eta\) and the multiplier commutant proof there apply verbatim to this finite measure space. Thus (T1) is a point-ultraweakly continuous normal action.

Its average is
\[
 E(f)=\int_G\alpha_s(f)\,ds
     =\left(\int_G f\right)1.
 \tag{T2}
\]
To prove the formula without choosing representatives for uncountably many translates, average on the predual. For continuous \(g\), Haar invariance gives the equality of continuous functions
\(\int_G g(t-s)\,ds=(\int_Gg)1\). The Bochner integral is legitimate by compactness and \(L^1\) translation continuity, as in L24. Approximate any \(g\in L^1\) by continuous functions. Both its averaged translate and \(g\mapsto(\int g)1\) are contractions on \(L^1\), so the formula extends to all \(g\). Taking the adjoint proves (T2).

If \(f\) is fixed by all translations, \(f=E(f)\), so \(f\) is constant. If
\(\alpha_s(f)=\chi_p(s)f\), multiply by \(\overline{\chi_p}\). The product is fixed, and hence constant. Conversely \(\chi_p\) itself has that covariance. Therefore
\[
 L^\infty(G)_p=\mathbb C\chi_p.
 \tag{T3}
\]
The normal projection onto this fiber has the precise formula
\[
 P_p f=\int_G\overline{\chi_p(s)}\,\alpha_s(f)\,ds
      =\left(\int_G f(t)\overline{\chi_p(t)}\,dt\right)\chi_p.
 \tag{T4}
\]
Indeed \(\chi_p E(f\overline{\chi_p})\) equals the first integral: multiplication by a fixed bounded function is normal, and the integrands agree as equivalence classes. Then use (T2). For \(G=\mathbb T^2\), this gives fibers
\(\mathbb C e^{2\pi i(ms+nt)}\), \((m,n)\in\mathbb Z^2\).

<a id="oa-flow.compact.cocycle"></a>

## The multiplication phases in scalar fixed-point actions

Now let a compact abelian group act normally and point-ultraweakly continuously on a nonzero von Neumann algebra \(M\), with fixed algebra \(\mathbb C1\). For any character \(p\), the proof of (E4) in [L103](OA-FLOW-L103.md#oa-flow.ergcircle.degrees) uses only multiplication of characters. Thus each nonzero fiber is spanned by a unitary \(w_p\), and the set \(J\) of appearing characters is a subgroup of the discrete dual. Choose \(w_0=1\). Products of the chosen unitaries determine phases
\[
 w_pw_q=c(p,q)w_{p+q},\qquad |c(p,q)|=1.
 \tag{T5}
\]
Associativity and normalization give
\[
 c(p,q)c(p+q,r)=c(q,r)c(p,q+r),\qquad
 c(p,0)=c(0,p)=1.
 \tag{T6}
\]
Replacing \(w_p\) by \(b_pw_p\), where \(|b_p|=1\) and \(b_0=1\), replaces \(c(p,q)\) by
\[
 c'(p,q)=b_pb_q\overline{b_{p+q}}c(p,q).
 \tag{T7}
\]
These formulas follow simply by computing the two products. When \(J=\mathbb Z\), choosing powers of one generator makes all phases one, as in L103. With two generators, the phase comparing their two orders of multiplication need not disappear: (T7) multiplies \(c(p,q)\) and \(c(q,p)\) by the same scalar, so their ratio is unchanged.

<a id="oa-flow.torus.regular"></a>

## A twisted regular algebra and its faithful trace

Fix \(\theta\in\mathbb R\) and write \(e(r)=e^{2\pi ir}\). On \(J=\mathbb Z^2\), set
\[
 c_\theta((m,n),(p,q))=e(\theta np).
 \tag{T8}
\]
For \(a=(m,n)\), \(b=(p,q)\), \(d=(r,k)\), the two exponents in (T6) are
\(\theta(np+(n+q)r)\) and \(\theta(qr+n(p+r))\), which agree. The normalization is immediate.

On \(H=\ell^2(J)\), define
\[
 \lambda(a)\delta_b=c_\theta(a,b)\delta_{a+b},
 \qquad
 M_\theta=\{\lambda(a):a\in J\}''.
 \tag{T9}
\]
Each \(\lambda(a)\) permutes the orthonormal basis with modulus-one coefficients, so is unitary. The cocycle identity gives
\[
 \lambda(a)\lambda(b)=c_\theta(a,b)\lambda(a+b).
 \tag{T10}
\]
In particular \(\lambda(a)^*=\overline{c_\theta(a,-a)}\lambda(-a)\); the same expression is both a left and a right inverse because \(c_\theta(a,-a)=c_\theta(-a,a)\).

For \(b\in J\), also define
\[
 \rho(b)\delta_a=c_\theta(a,b)\delta_{a+b}.
 \tag{T11}
\]
These are unitaries. Applying both \(\lambda(d)\rho(b)\) and \(\rho(b)\lambda(d)\) to \(\delta_a\), equality of their coefficients is precisely
\(c_\theta(a,b)c_\theta(d,a+b)=c_\theta(d,a)c_\theta(d+a,b)\).
Thus every \(\rho(b)\) commutes with \(M_\theta\). Since \(\rho(b)\delta_0=\delta_b\), the vector \(\delta_0\) is separating: if \(x\delta_0=0\) for \(x\in M_\theta\), then \(x\delta_b=\rho(b)x\delta_0=0\) for all \(b\), and hence \(x=0\).

It follows that
\[
 \tau(x)=\langle x\delta_0,\delta_0\rangle
 \tag{T12}
\]
is a faithful normal state. For positivity, \(\tau(x^*x)=\|x\delta_0\|^2\), which also proves faithfulness. Normality is that of a vector coefficient. It is a trace: on two generators, both \(\tau(\lambda(a)\lambda(b))\) and \(\tau(\lambda(b)\lambda(a))\) vanish unless \(a+b=0\); in that case their coefficients agree by the preceding inverse identity. Extend by bilinearity to finite sums. The finite sums form a unital *-algebra with bicommutant \(M_\theta\); [BD1–5](OA-FLOW-BD.md#oa-flow.bd.1) gives bounded ultraweak approximation of every element by such sums. For one fixed finite sum, separate ultraweak continuity of multiplication extends the trace identity in the other variable; then fix that arbitrary element and extend in the first variable. Separate continuity follows directly from the vector-series tests in [CP4](OA-FLOW-CP.md#oa-flow.cp.4), by moving the fixed bounded factor to a test vector. No joint continuity of multiplication is used.

The GNS map for this trace is concretely \(\Lambda_\tau(x)\mapsto x\delta_0\): it preserves inner products by (T12), and its range contains every \(\delta_a=\lambda(a)\delta_0\). It therefore extends to a unitary onto \(H\). The \(\lambda(a)\) form a complete orthonormal family in this trace Hilbert space.

<a id="oa-flow.torus.gauge"></a>

## A faithful ergodic two-torus action

For \(s=(s_1,s_2)\in\mathbb T^2\), define
\[
 D_s\delta_{(m,n)}=e(ms_1+ns_2)\delta_{(m,n)}.
 \tag{T13}
\]
This unitary group is strongly continuous: approximate a vector in \(\ell^2(J)\) by a finite-support vector; continuity on the finite support is elementary, and the remaining difference is at most twice the tail norm. Direct calculation gives
\[
 D_s\lambda(m,n)D_s^*=e(ms_1+ns_2)\lambda(m,n).
 \tag{T14}
\]
Consequently \(\alpha_s=\operatorname{Ad}D_s\) preserves \(M_\theta\). Conjugation is normal by the vector-series description of normal functionals. For each fixed \(x\), its individual vector coefficients under conjugation are continuous by strong continuity of \(D\). An absolutely summable vector series has uniformly small tails bounded by \(\|x\|\) times the sum of products of vector norms, so every normal coefficient is continuous. This proves point-ultraweak continuity. Also \(D_s\delta_0=\delta_0\), so \(\tau\circ\alpha_s=\tau\).

If \(x\) is an eigenvector of degree \(a=(m,n)\), then
\[
 D_sx\delta_0=e(ms_1+ns_2)x\delta_0.
 \tag{T15}
\]
In the coordinate expansion of \(x\delta_0\), every coefficient at \(b\ne a\) vanishes: vary a coordinate \(s_j\) for which \(b_j\ne a_j\) to separate the two characters. Thus \(x\delta_0\) is a scalar multiple of \(\delta_a\). Since \(\delta_0\) is separating, \(x\) is the same scalar multiple of \(\lambda(a)\). Conversely (T14) supplies every such eigenvector. Hence
\[
 (M_\theta)_a=\mathbb C\lambda(a)\quad(a\in\mathbb Z^2),
 \qquad M_\theta^\alpha=\mathbb C1.
 \tag{T16}
\]
Testing (T14) at \(a=(1,0)\) and \((0,1)\) shows that the kernel is zero. The action is faithful and ergodic.

Finally, put \(U=\lambda(1,0)\) and \(V=\lambda(0,1)\). Equation (T10) gives
\[
 U^mV^n=\lambda(m,n),\qquad
 VU=e(\theta)UV.
 \tag{T17}
\]
The power formulas hold also for negative integers, because the cocycle is one on either coordinate subgroup. If \(\theta\notin\mathbb Z\), (T17) shows \(M_\theta\) is noncommutative: \(UV\) is unitary, and \(e(\theta)-1\ne0\). This includes every irrational \(\theta\). Thus a faithful ergodic \(\mathbb T^2\)-action need not be conjugate to translation on the commutative algebra \(L^\infty(\mathbb T^2)\).

<a id="oa-flow.torus.untwisted"></a>

## The zero-phase model is ordinary translation

When \(\theta=0\), define a unitary
\[
 \mathcal F:\ell^2(\mathbb Z^2)\longrightarrow L^2(\mathbb T^2),
 \qquad \mathcal F\delta_{(m,n)}=z_1^mz_2^n.
 \tag{T18}
\]
Completeness follows from the circle basis in CC0 and its tensor-product statement, with the product integration convention in L24. On basis vectors,
\(\mathcal F\lambda(m,n)\mathcal F^*\) is multiplication by \(z_1^mz_2^n\).

These multipliers generate the entire multiplication algebra. For \(f\in L^\infty(\mathbb T^2)\), average translations against \(F_N(s_1)F_N(s_2)\). The result \(f_N\) is a finite trigonometric polynomial, satisfies \(\|f_N\|_\infty\leq\|f\|_\infty\), and tends to \(f\) in \(L^2\). For the last assertion, the operators are \(L^2\) contractions by the integral norm bound; they converge on each basis vector by the explicit Fejér coefficients, and hence on all \(L^2\) by density. Multiplication by \(f_N\) tends strongly to multiplication by \(f\): for bounded \(g\), use
\(\|(f_N-f)g\|_2\leq\|g\|_\infty\|f_N-f\|_2\); for general \(g\in L^2\), approximate by bounded truncations and use the common bound \(2\|f\|_\infty\). The multiplication algebra is its own commutant by the finite-measure proof in L102, so it is strongly closed. This proves
\[
 \mathcal F M_0\mathcal F^*=L^\infty(\mathbb T^2)
 \quad\hbox{in its multiplication representation}.
 \tag{T19}
\]
Under \(\mathcal F\), \(D_s\) is translation by \(s\), as follows first on the Fourier basis and then by continuity. Conjugating a multiplier therefore translates its function. Thus the construction contains ordinary torus translation at zero phase and noncommutative scalar-fiber actions at nonintegral phase, with the difference recorded exactly by (T17).

This develops the compact-group and two-torus question in Takesaki, *Theory of Operator Algebras II*, Exercise XI.1.4, p.330.
