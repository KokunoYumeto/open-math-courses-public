# Homogeneous operators in the continuous core



The continuous core turns a nontracial weight into a homogeneous positive
operator in a semifinite algebra. The ordinary trace of that operator is usually
infinite, so the integral cannot be obtained by silently applying the tracial
\(L^p\) construction. This lesson builds the graded integral, proves the
weight--operator dictionary needed by the source exercises, and proves the
Banach, Hölder, cyclicity and onto duality conclusions in their exact ranges.

Read the general core and density construction, LP-01--04
first. It proves the fixed algebra, normalized scaling trace, supported density
correspondence, localizer pairing and coherent change of reference for arbitrary
von Neumann algebras. We identify its supported symbols and Lebesgue spectral
representations explicitly below. The orbit integral uses \(ds\), with the same
trace normalization as LP-01. The analytic, Banach, product and duality arguments
then use the named measurable-operator, trace, complex-analysis and Hahn--Banach
proofs. HL-12 proves the supplementary state-dependent interpolation
identification using the reflexivity already established in HL-10.

Throughout, \(M\) is a factor with separable predual. Write
\((\widetilde M,\theta,\tau)\) for its fixed continuous core. Thus

\[
 M=\widetilde M^\theta,
 \qquad
 \tau\mathbin\circ\theta_s=e^{-s}\tau .
\tag{HL.1}
\]

The measurable algebra for \(\tau\) is denoted by
\(\mathscr S_\tau(\widetilde M)\). Products of measurable operators mean the
closed measurable products constructed in
MT-09.

## Equivariant copies of the translation algebra are weights

**The core and its supported symbols.** Choose a faithful normal semifinite
reference \(\chi\). By LP-01,
the regular core has a faithful normal semifinite orbit weight \(E\),
fixed algebra \(M\), and trace \(\tau\) satisfying (HL.1).
LP-04 constructs the normal
trace-preserving equivariant change from a \(\psi\)-chart to a
\(\chi\)-chart. It fixes \(M\) and sends the translation unitary to
\([D\psi:D\chi]_t\lambda_t^\chi\). Its proof uses a multiplication
unitary in the regular representation and verifies the ordered cocycle law;
it proves equality of the actual traces, not just proportionality.

One may therefore regard the core as pairs \((\chi,A)\) modulo these chart
maps. The identity and composition laws in LP-04 make this an equivalence
relation. Move finitely many representatives to one chart to add, multiply
or take adjoints. Those operations, the norm and the ultraweak topology are
independent of chart because every transition is a normal isomorphism with
normal inverse. A single chart identifies the resulting algebra with its
complete von Neumann algebra. The fixed copy of \(M\), \(\theta\) and
\(\tau\) agree in all charts.

This construction is functorial for normal isomorphisms. If
\(\rho:M\to N\) is one, put \(\chi'=\chi\circ\rho^{-1}\).
The map \(\Lambda_\chi(x)\mapsto\Lambda_{\chi'}(\rho(x))\) is an
isometry on the GNS domain, onto a dense domain; it extends to a unitary.
It intertwines the closed Tomita operators since it intertwines their
defining involutions and their graph closures. Hence it intertwines the
modular groups. Applying it pointwise in the regular Hilbert space gives
the normal core isomorphism
\[
 \pi_\chi(x)\longmapsto\pi_{\chi'}(\rho(x)),\qquad
 \lambda_t^\chi\longmapsto\lambda_t^{\chi'}.
\]
It intertwines \(\theta\) and its positive integral \(E\), so it
transports the dual weight \(\chi\circ E\) to \(\chi'\circ E\).
It also transports the generator of \(\lambda\); the trace construction
in LP-01 therefore proves trace preservation. Naturality of the balanced
matrix cocycle, proved in SI-14,
makes these maps commute with every chart transition. Composition and
identities hold on the displayed generators and hence on the whole core.
Here functoriality concerns isomorphisms; no core map for an arbitrary
inclusion is being asserted.

For a normal semifinite weight \(\varphi\), including a nonfaithful one,
LP-02 constructs the unique
positive affiliated operator \(h_\varphi\) with
\[
 \varphi\circ E=\tau_{h_\varphi},\qquad
 \theta_s(h_\varphi)=e^{-s}h_\varphi,
 \qquad s(h_\varphi)=s(\varphi).
\]
The theorem proves the converse as well. Its proof descends the fixed
relative cocycle by CX-10, lifts it by OR-03, and handles nonfaithful
supports by the complementary-corner theorem; a citation is not being
used in place of that earlier written argument.

The identification with the weight symbol requires a support check.
Let \(e=s(\varphi)\). Complete \(\varphi|_{eMe}\) by a faithful
normal semifinite weight on \((1-e)M(1-e)\), using
CW-06, and call
the diagonal faithful weight \(\bar\varphi\). In its chart,
\(h_{\bar\varphi}^{it}=\lambda_t^{\bar\varphi}\).
Since \(e\) is in the centralizer of \(\bar\varphi\), it is a
constant reducing projection for both the regular coefficient action and
these translations. Bimodularity of \(E\) gives, on every positive \(A\),
\[
 \varphi(E(A))
 =\bar\varphi(E(eAe))
 =\tau_{h_{\bar\varphi}}(eAe)
 =\tau_{e h_{\bar\varphi}}(A).
\]
The last equality follows with bounded spectral regularizations, which
commute with \(e\), and then normal increasing evaluation. Density
uniqueness in PT-08 proves
\(h_\varphi=e h_{\bar\varphi}\), extended by zero on the complement.
Thus its supported imaginary powers are
\(\varphi^{it}:=e\lambda_t^{\bar\varphi}\); they have initial and
final projection \(e\), including \(\varphi^{i0}=e\).
Density uniqueness and LP-04 show that the symbol is independent of the
completion and chart. Regular covariance and modular restriction to the
centralizer corner give
\[
 h_\varphi^{it}x h_\varphi^{-it}=\sigma_t^\varphi(x)
 \quad(x\in eMe).
\]
The zero weight gives zero density and zero supported symbols.

Put

\[
 \begin{aligned}
 A&=L^\infty(\mathbb R),\\
 (\rho_t f)(r)&=f(r+t),
 \end{aligned}
\tag{HL.2}
\]

and define

\[
 \begin{aligned}
 V(t)(r)&=e^{-irt},\\
 H(r)&=e^{-r}.
 \end{aligned}
\tag{HL.3}
\]

The characters \(V(t)\) generate \(A\), \(V(t)=H^{it}\), and
\(\rho_s(V(t))=e^{-ist}V(t)\).

Let \(\varphi\) be a nonzero normal semifinite weight on \(M\), with support
\(e=s(\varphi)\). The density construction above gives a positive self-adjoint operator
\(h_\varphi\), affiliated with \(e\widetilde M e\), such that

\[
 \begin{aligned}
 \theta_s(h_\varphi)&=e^{-s}h_\varphi,\\
 h_\varphi^{it}&=\varphi^{it},\\
 s(h_\varphi)&=e.
 \end{aligned}
\tag{HL.4}
\]

Here \(\varphi^{it}\) is the canonical core unitary symbol; no bounded density
inside \(M\) is being asserted. Spectral calculus defines

\[
 \begin{aligned}
 \pi^\varphi(f)&=f(-\log h_\varphi),\\
 f&\in L^\infty(\mathbb R).
 \end{aligned}
\tag{HL.5}
\]

Here is a proof that (HL.5) is defined on Lebesgue classes and is faithful.
On the nonzero support put \(Q=-\log h_\varphi\), with spectral measure
\(P\). Grade one gives \(\theta_s(Q)=Q+s\), so
\(\theta_s(P(B))=P(B-s)\) for every Borel set \(B\).
For a positive normal functional \(\nu\) on the corner, scalar Tonelli gives
\[
 \int_{\mathbb R}\nu(P(B-s))\,ds=|B|\nu(e).
\]
Indeed the inner indicator is \(1_B(r+s)\), and its integral in \(s\)
is the Lebesgue measure \(|B|\), independently of \(r\). The finite
scalar spectral measure has total mass \(\nu(e)\). If \(|B|=0\),
the left integrand is a continuous nonnegative function of \(s\), since
the dual action is spatially strongly continuous. It vanishes at zero.
Every positive normal \(\nu\) therefore annihilates \(P(B)\), so
\(P(B)=0\). Conversely, if \(P(B)=0\), all its translates are zero.
Choosing \(\nu(e)>0\) in the same equality forces \(|B|=0\).
Thus the spectral null sets are exactly the Lebesgue null sets. Spectral
calculus consequently gives the faithful normal map (HL.5), onto its range.
The unitary-generator theorem PT-03
also shows that this spectral algebra is generated by its imaginary powers.
Equations (HL.3--4) give

\[
 \begin{aligned}
 \pi^\varphi(V(t))&=h_\varphi^{it}=\varphi^{it},\\
 \theta_s\pi^\varphi(f)&=\pi^\varphi(\rho_s f).
 \end{aligned}
\tag{HL.6}
\]

This proves existence. It also proves uniqueness: an equivariant normal
homomorphism with the prescribed values on every \(V(t)\) agrees with
\(\pi^\varphi\) on the von Neumann algebra generated by those characters.

Conversely, let

\[
 \pi:(A,\rho)\longrightarrow(e\widetilde M e,\theta)
\tag{HL.7}
\]

be an equivariant normal star isomorphism onto its range. Set \(h=\pi(H)\), using affiliated
spectral calculus. Then

\[
 \theta_s(h)=e^{-s}h,
 \qquad s(h)=e.
\tag{HL.8}
\]

The positive grade-one density theorem supplies a unique normal semifinite
weight \(\varphi_\pi\) with \(h=h_{\varphi_\pi}\). Since \(V(t)=H^{it}\),

\[
 \pi(V(t))=h^{it}=\varphi_\pi^{it}.
\tag{HL.9}
\]

The first uniqueness argument now gives \(\pi=\pi^{\varphi_\pi}\). Hence
nonzero normal semifinite weights, including their nonzero supports, classify
precisely the equivariant copies of the translation algebra in core corners.
The zero weight has zero support and cannot yield a faithful copy of the
nonzero algebra \(A\).

## Localizers recover the weight and scaling measures

For \(a\in\widetilde M_+\), let

\[
 I_\theta(a)=\int_{\mathbb R}\theta_t(a)\,dt
\tag{HL.10}
\]

be the positive extended orbit integral \(E\) of LP-01. A **normalized
localizer** satisfies \(E(a)=1\). Existence has an explicit bounded witness:
if \(d\) is the injective reference density in LP-01, put
\(a_0=d^{-1}1_{(1,\infty)}(d)\). For each scalar \(\ell>0\),
\(\int_{s<\log\ell}e^s\ell^{-1}\,ds=1\); spectral calculus and
positive normal evaluation give \(E(a_0)=1\).

If \(h=h_\varphi\) and \(x\in M_+\), write
\(b_x=x^{1/2}a x^{1/2}\) and \(c_x=x^{1/2}h x^{1/2}\).
Since \(E\) is bimodular, \(E(b_x)=x\). The equality
\(\varphi\circ E=\tau_h\) proved in LP-02 therefore gives the first
line below on the full positive cone:

\[
 \begin{aligned}
 \varphi(x)
 &=\tau\!\left(
     h^{1/2}b_xh^{1/2}
   \right)\\
 &=\tau\!\left(
     a^{1/2}c_xa^{1/2}
   \right).
 \end{aligned}
\tag{HL.11}
\]

Both lines mean the normal trace pairing of the corresponding extended
positive form and may be infinite; its finite domain need not be dense. The second line follows first for bounded spectral truncations by
tracial cyclicity and then for the full form by the extended-positive
monotone limit from
PT-08. Since the left side does
not mention \(a\), (HL.11) also proves independence of the normalized
localizer.

The source uses the following affiliated regularizer \(r_\varepsilon\).
It is unbounded: its scalar multiplier grows like
\(\varepsilon^{-1/2}\lambda^{1/4}\) as \(\lambda\to\infty\).
A bounded alternative is \(s_\varepsilon\). Put

\[
 \begin{aligned}
 r_\varepsilon&=h^{1/2}(1+\varepsilon h^{1/2})^{-1/2},\\
 s_\varepsilon&=h^{1/2}(1+\varepsilon h)^{-1/2},\\
 \|s_\varepsilon\|&\leq\varepsilon^{-1/2}.
 \end{aligned}
\tag{HL.12}
\]

For the bounded positive operator \(b_x\), the normal weight
\(\Phi_{b_x}(c)=\tau(b_x^{1/2}c b_x^{1/2})\) extends normally to the
extended positive cone. Spectral calculus gives
\(r_\varepsilon^2=h/(1+\varepsilon h^{1/2})\uparrow h\) and
\(s_\varepsilon^2=h/(1+\varepsilon h)\uparrow h\) as
\(\varepsilon\downarrow0\). On bounded spectral bands, tracial cyclicity
identifies \(\Phi_{b_x}(r_\varepsilon^2)\) with the closed-form trace
\(\tau(r_\varepsilon b_xr_\varepsilon)\). Normal extension gives the same
identity for the full affiliated operator, including infinite values.
Consequently normality and (HL.11) prove

\[
 \varphi(x)
 =\lim_{\varepsilon\downarrow0}
   \tau\!\left(
     r_\varepsilon b_xr_\varepsilon
   \right).
\tag{HL.13}
\]

The same limit holds with \(s_\varepsilon\) in place of
\(r_\varepsilon\). The trace values increase because the squared spectral
multipliers increase; the noncommuting sandwiches themselves are not asserted
to increase in operator order.

There is a normalization defect in the printed scaling-measure exercise. Let
\(\mu\) be a normal weight on \(A=L^\infty(\mathbb R)\) such that

\[
 \mu\mathbin\circ\rho_t=e^{-t}\mu
\tag{HL.14}
\]

and suppose \(0<\mu(f_0)<\infty\) for some \(f_0\in A_+\).
The all-normal trace correspondence CW-11,
applied to Lebesgue integration on \(A\), represents \(\mu\) by an
extended measurable density \(g\), including its possible infinite part:

\[
 \mu(f)=\int_{\mathbb R}g(r)f(r)\,dr.
\tag{HL.15}
\]

Changing variables in (HL.14) yields

\[
 \begin{aligned}
 g(r-t)&=e^{-t}g(r)\\
 &\text{for almost every }r.
 \end{aligned}
\tag{HL.16}
\]

Thus \(q(r)=e^{-r}g(r)\) is translation invariant modulo null sets. A
measurable function with this property is almost everywhere constant. One
direct proof convolves each finite truncation of \(q\) with a compactly
supported approximate identity: every convolution is continuous and invariant
under the dense subgroup of rational translations, hence constant. The
\(L^1\) translation estimate of BI-03
makes these convolutions converge weak-star to each bounded truncation.
Constants are weak-star closed, so each truncation is constant; their
increasing limit gives the assertion. The finite nonzero value of
\(f_0\) rules out both constants zero and infinity. Consequently

\[
 \boxed{
 \begin{aligned}
 \mu(f)&=c\int_{\mathbb R}e^r f(r)\,dr,\\
 c&>0 .
 \end{aligned}}
\tag{HL.17}
\]

This weight is faithful and semifinite. The source's coefficient \(1\) follows
only after an additional normalization fixing \(c=1\). Every \(c>0\) satisfies
the printed hypotheses, so omitting \(c\) changes the statement.

Without the finite nonzero test, the same invariant-density argument gives
an extended constant \(c\in[0,\infty]\). A nonzero scaling weight has
\(c>0\), and \(c=\infty\) means that every nonzero positive function
has infinite weight. This extended case is needed for infinite weights below.

## Finite weights are exactly measurable core densities

Let \(h=h_\varphi\) and
\(\mathcal A^\varphi=\pi^\varphi(A)=W^*(h^{it}:t\in\mathbb R)\). For
\(\lambda>0\), write

\[
 d_h(\lambda)=\tau(1_{(\lambda,\infty)}(h)).
\tag{HL.18}
\]

Grade one and trace scaling give the exact distribution law

\[
 d_h(e^s\lambda)=e^{-s}d_h(\lambda).
\tag{HL.19}
\]

Indeed
\(\theta_s(1_{(\lambda,\infty)}(h))\)
is \(1_{(e^s\lambda,\infty)}(h)\), and (HL.1) applies. More explicitly, the
restriction \(\mu_\varphi=\tau\mathbin\circ\pi^\varphi\) is a normal scaling
weight on \(A\), so (HL.17) gives
\(\mu_\varphi(f)=c_\varphi\int e^r f(r)\,dr\). Choose
\(g\in L^1(\mathbb R)_+\cap L^\infty(\mathbb R)\) with
\(\int g(r)\,dr=1\). Then \(a=\pi^\varphi(g)\) is a normalized localizer on
the support corner; adjoining a normalized complementary-corner localizer does
not change the following trace. The inverse-density formula (HL.11), at
\(x=1\), gives

\[
 c_\varphi
 =\mu_\varphi(Hg)
 =\tau(a^{1/2}ha^{1/2})
 =\varphi(1).
\]

Since \(1_{(\lambda,\infty)}(H)=1_{(-\infty,-\log\lambda)}\), the scaling
law therefore has the exact extended constant

\[
 d_h(\lambda)=\frac{\varphi(1)}{\lambda}
\tag{HL.20}
\]

including infinite values. For \(\varphi(1)=\infty\) the coefficient is
the extended value just described, rather than a finite instance of (HL.17).

If \(\varphi(1)<\infty\), (HL.20) makes every high spectral tail finite and
tending to zero. The spectral-tail criterion
MT-11 shows that \(h\) is
\(\tau\)-measurable. Conversely, if \(h\) is measurable, some nonzero high
spectral tail has finite trace unless \(h\) is bounded. In the bounded case,
grade one and preservation of the operator norm already force \(h=0\), which
corresponds to the zero finite weight. In the nonzero case, (HL.19) gives a
finite constant in (HL.20), so \(\varphi(1)<\infty\).

The intersection criterion is now exact. If \(\varphi\) is finite and nonzero,
then for \(0<a<b<\infty\), put \(p_{a,b}=1_{[a,b]}(h)\). We have

\[
 \begin{aligned}
 p_{a,b}&\in\mathcal A^\varphi\cap\mathfrak m_\tau,\\
 \tau(p_{a,b})&=\varphi(1)(a^{-1}-b^{-1}).
 \end{aligned}
\tag{HL.21}
\]

whenever the band is nonzero. Conversely, suppose
\(0\neq z\in\mathcal A^\varphi\cap\mathfrak m_\tau\). A nonzero spectral
projection of \(|z|\) has finite trace and still belongs to
\(\mathcal A^\varphi\). Thus the restriction of \(\tau\) to this copy of
\(L^\infty(\mathbb R)\) has a nonzero finite value. The scaling-measure lemma
(HL.17) applies, so its coefficient is finite; (HL.20) then gives
\(\varphi(1)<\infty\). We have proved

\[
 \boxed{
 \begin{gathered}
 \varphi(1)<\infty\\
 \Updownarrow\\
 \mathcal A^\varphi\cap\mathfrak m_\tau\neq\{0\}\\
 \Updownarrow\\
 h_\varphi\in\mathscr S_\tau(\widetilde M).
 \end{gathered}}
\tag{HL.22}
\]

For the zero weight, the first and third conditions hold while the displayed
nonzero-intersection condition does not. The source works with nonzero weights;
that hypothesis is necessary for the three-way formulation.

## Distribution scaling forbids negative real grade

For a closed densely defined operator \(T\) affiliated with \(\widetilde M\),
say that \(T\) has **grade** \(\alpha\in\mathbb C\) when

\[
 \theta_s(T)=e^{-\alpha s}T
 \qquad(s\in\mathbb R).
\tag{HL.23}
\]

Let

\[
 \begin{gathered}
 \mathscr H(\alpha)\\
 =\{T:\\
 \operatorname{grad}(T)=\alpha,\\
 T\in\mathscr S_\tau(\widetilde M)\}.
 \end{gathered}
\tag{HL.24}
\]

If \(T=u|T|\) and \(\alpha=p+iq\), uniqueness of polar decomposition gives

\[
 \begin{aligned}
 \theta_s(|T|)&=e^{-ps}|T|,\\
 \theta_s(u)&=e^{-iqs}u.
 \end{aligned}
\tag{HL.25}
\]

Writing \(d_T(\lambda)=\tau(1_{(\lambda,\infty)}(|T|))\), the same calculation
as in (HL.19) yields

\[
 d_T(e^{ps}\lambda)=e^{-s}d_T(\lambda).
\tag{HL.26}
\]

Suppose \(p<0\) and \(T\neq0\). If \(T\) is bounded, preservation of operator
norm under \(\theta_s\) contradicts
\(\|T\|=e^{-ps}\|T\|\). If \(T\) is unbounded, measurability supplies a
\(\lambda\) with \(0<d_T(\lambda)<\infty\). For \(s>0\), the threshold
\(e^{ps}\lambda\) is smaller than \(\lambda\), so monotonicity gives

\[
 d_T(e^{ps}\lambda)\ge d_T(\lambda),
\]

whereas (HL.26) gives the strictly smaller value
\(e^{-s}d_T(\lambda)\). This contradiction proves

\[
 \begin{aligned}
 \mathscr H(\alpha)&=\{0\}\\
 &\text{when }\Re\alpha<0.
 \end{aligned}
\tag{HL.27}
\]

Now let \(\alpha=0\). Every spectral projection of a grade-zero measurable
operator is fixed by \(\theta\). If such an operator were unbounded,
measurability would supply a nonzero finite-trace high spectral projection
\(e\). But

\[
 \tau(e)=\tau(\theta_s(e))=e^{-s}\tau(e)
\]

is impossible. Hence the operator is bounded, and the fixed-point identity in
(HL.1) places it in \(M\). Conversely, every \(x\in M\) is bounded,
\(\tau\)-measurable and fixed. Therefore

\[
 \boxed{\mathscr H(0)=M.}
\tag{HL.28}
\]

Purely imaginary nonzero grades are different: core unitaries can have such a
grade. Statement (HL.28) concerns the exact grade zero.

## Every positive real grade has a functional density

Let \(T\in\mathscr H(\alpha)\), with \(\alpha=p+iq\) and \(p>0\). Functional
calculus, (HL.25), and the measurable-power theorem give

\[
 \theta_s\bigl(|T|^{1/p}\bigr)
 =e^{-s}|T|^{1/p}.
\tag{HL.29}
\]

Thus \(|T|^{1/p}\) is a positive measurable grade-one operator. The
support-preserving bijection LP-02
and (HL.22) produce a unique normal positive functional
\(\omega_T\in M_*^+\) such that

\[
 |T|^{1/p}=h_{\omega_T}.
\tag{HL.30}
\]

In particular

\[
 |T|=h_{\omega_T}^{\,p}.
\tag{HL.31}
\]

For a real grade \(p\), (HL.25) puts the polar partial isometry \(u\) in \(M\),
so \(T=u h_{\omega_T}^{p}\). For a complex grade, choose once and for all a
faithful normal state \(\chi\) and put \(d=h_\chi\). The unitary \(d^{iq}\) has
grade \(iq\). Hence \(u d^{-iq}\) has grade zero and lies in \(M\), giving the
normal form

\[
 \begin{aligned}
 T&=v d^{iq}h_{\omega_T}^{p},\\
 v&=u d^{-iq}\in M.
 \end{aligned}
\tag{HL.32}
\]

The fixed choice of \(\chi\) is only a coordinate for the imaginary grade; the
operator \(T\), its modulus and the functional \(\omega_T\) do not depend on it.
Also, if a nonzero operator has two grades, then
\(e^{-\alpha s}T=e^{-\beta s}T\) for every \(s\), forcing
\(\alpha=\beta\). Distinct homogeneous spaces therefore have zero
intersection.

## The canonical integral and the grade-one predual

Let \(T\in\mathscr H(1)\), with polar decomposition

\[
 \begin{aligned}
 T&=u h_\omega,\\
 u&\in M,\\
 \omega&\in M_*^+.
 \end{aligned}
\tag{HL.33}
\]

We first establish linearity and the module action of the density map; neither
follows from polar decomposition alone. For positive normal functionals write
\(D(\omega)=h_\omega\). A sum of positive measurable grade-one operators
is again positive, measurable and of grade one. Evaluate its inverse density
by the second line of (HL.11). Linearity of the extended trace on positive
forms gives
\(D(\omega_1+\omega_2)=h_{\omega_1}+h_{\omega_2}\), and positive scalar
multiplication is preserved as well. The positive decomposition argument in
LP-03 now extends \(D\) to a
well-defined complex linear map on \(M_*\): it expresses every normal
functional as four positive ones using the summable vector coefficients of
CP04--06, and proves independence of that expression by positive additivity. Its
injectivity follows from injectivity on positive functionals: a self-adjoint
element of its kernel has equal positive and negative density parts, and the
real and imaginary parts handle the general kernel.

For \(x\in M\), put \(\omega_x(y)=\omega(x^*yx)\). We claim
\(D(\omega_x)=xh_\omega x^*\). To check this using the inverse formula,
fix \(y\in M_+\) and write \(y^{1/2}x=v|y^{1/2}x|\), with
\(p=v^*v\). If \(a\) is a normalized localizer, then
\(a'=v^*av+(1-p)a(1-p)\) is another: \(v,p\in M\) are fixed by
\(\theta\), so its orbit integral is \(p+(1-p)=1\). The complement term
vanishes between the two factors \(|y^{1/2}x|\). Tracial closed-form
pairings thus give

\[
 \begin{aligned}
 \tau\bigl(a^{1/2}y^{1/2}xh_\omega x^*y^{1/2}a^{1/2}\bigr)
 &=\tau\bigl(h_\omega^{1/2}|y^{1/2}x|a'|y^{1/2}x|h_\omega^{1/2}\bigr)\\
 &=\omega(x^*yx).
 \end{aligned}
\]

The first equality is understood through the normal positive trace pairings
of HL-02, so it does not assume boundedness of \(h_\omega\).
Density uniqueness in LP-02 proves the claim. Polarizing this
congruence identity gives
\(D[y\mapsto\omega(b^*yc)]=c h_\omega b^*\) for \(b,c\in M\).
In particular the normal functional \(y\mapsto\omega(yu)\) has density
\(u h_\omega\). Its polar support is \(u^*u=s(\omega)\), as in (HL.33).
Conversely HL-05 puts every grade-one operator in this form. Hence \(D\)
is onto \(\mathscr H(1)\).

Define \(\int T=D^{-1}(T)(1)\). This linear functional agrees with the
following localizer formula:

\[
 \int T
 =\tau(a^{1/2}Ta^{1/2}).
\tag{HL.34}
\]

Indeed, decompose \(D^{-1}(T)\) into a complex linear combination of
positive functionals. Each localized positive density in (HL.11), at
\(x=1\), has finite trace. Their linear combination is trace integrable,
and the linearity just proved identifies it with the localized measurable
product in (HL.34). Thus (HL.34) is finite and independent of \(a\), and

\[
 \int u h_\omega=\omega(u).
\tag{HL.35}
\]

The polarized congruence identity fixes the orientation: the functional
associated with \(T\) is

\[
 \begin{aligned}
 F_T(x)&=\int xT,\\
 x&\in M.
 \end{aligned}
\tag{HL.36}
\]

Every normal functional has a polar decomposition of the form
\(x\mapsto\omega(xu)\), and its density is \(u h_\omega\). Thus

\[
 T\longmapsto F_T
\tag{HL.37}
\]

is a linear bijection from \(\mathscr H(1)\) onto \(M_*\). Moreover

\[
 \begin{aligned}
 \|T\|_1&:=\int|T|\\
 &=\omega(1)=\|F_T\|.
 \end{aligned}
\tag{HL.38}
\]

Since the predual is complete, (HL.37--38) prove that
\(\mathscr H(1)\) is a Banach space. They also show why the ordinary core trace
cannot replace the integral: in the scalar model \(M=\mathbb C\), the density
\(ce^{-r}\) has infinite ordinary \(\tau\)-integral, while its canonical
integral is \(c\).


### Spectral size and an initial product bound

For a measurable operator \(T\) of grade \(a+ib\), \(a>0\), put
\(g(T)=(\int|T|^{1/a})^a\). The definition applies even when \(a>1\);
it is not yet asserted to be a norm. The distribution formula in HL-03 gives

\[
 d_T(\lambda)=g(T)^{1/a}\lambda^{-1/a},
 \qquad \mu_t(T)=g(T)t^{-a}.
\]

Here \(\mu_t(T)\) is the infimum of \(\|Te\|\) over projections with
\(\tau(1-e)\leq t\). The spectral-cut characterization follows from the
projection comparison of MT-02: a cut with norm below \(\lambda\) must
discard at least the dimension of \(1_{(\lambda,\infty)}(|T|)\).
At positive real grade, therefore, convergence in measure within one fixed
homogeneous space is exactly convergence of the gauge of the difference.
In particular, on grade one it is predual norm convergence.

We will use two estimates for arbitrary measurable operators:
\(\mu_{s+t}(A+B)\leq\mu_s(A)+\mu_t(B)\) and
\(\mu_{s+t}(AB)\leq\mu_s(A)\mu_t(B)\). For the first, intersect the two
bounded-domain cuts. For the second, take cuts \(e,f\) for \(A,B\).
The right support \(r\) of \((1-e)B\) has trace at most \(\tau(1-e)\),
because its polar range lies in \(1-e\). On \(q=f\wedge(1-r)\),
\(Bq=eBq\), and the ordinary product is defined and bounded by
\(\|Ae\|\|Bf\|\). Projection subadditivity bounds \(\tau(1-q)\) by
\(s+t\). Infima, with arbitrarily small slack in the norm bounds, prove the
estimate for the closed measurable product. The same argument gives
\(\mu_t(CAD)\leq\|C\|\mu_t(A)\|D\|\) for bounded core operators \(C,D\).

If \(A,B\) have grades \(a+ib\) and \(1-a-ib\), \(0<a<1\), their product
has grade one. Set \(s=a\), \(t=1-a\). Then

\[
 \|AB\|_1
 \leq a^{-a}(1-a)^{-(1-a)}g(A)g(B).
\]

This rough estimate uses actual bounded-domain projections and makes no
claim that the cut operators remain homogeneous. Its constant is at most
two and tends to one at both endpoints. At real grade zero, HL-04's
spectral-tail argument gives boundedness, and the bounded module estimate
supplies the corresponding endpoint bound.

## Complex powers interpolate positive densities

Let \(h,k\in\mathscr H(1)_+\) and \(0\leq\Re z\leq1\). Positive real
powers are measurable. At real exponent zero use the supported imaginary
powers, which are bounded partial unitaries. Closed measurable multiplication
and grade addition give

\[
 h^z k^{1-z}\in\mathscr H(1).
\tag{HL.39}
\]

We establish holomorphy of the actual product

\[
 F(z)=h^z k^{1-z}
\tag{HL.40}
\]

in the open strip. For any positive measurable \(c\), \(z\mapsto c^z\)
is differentiable in measure on \(\Re z>0\), with derivative the spectral
function \(c^z\log c\), defined as zero on the kernel. On \(0\leq\lambda\leq R\),
the difference quotients of \(\lambda^z\) converge uniformly near each
\(z_0\) with positive real part: powers times logarithms tend to zero at
\(\lambda=0\), and their second derivatives are uniformly bounded on a small
closed disk about \(z_0\). Functional calculus proves the bounded-cut assertion.
The omitted high spectral projection has arbitrarily small trace as
\(R\to\infty\); this proves differentiability in measure.

The product rule in MT-09 now gives

\[
 F'(z)=h^z\log h\,k^{1-z}-h^z k^{1-z}\log k
\]

as a limit in measure. This formula denotes the two measurable spectral
products, not an assertion that \(\log h\) or \(\log k\) alone is measurable.
The difference quotients have grade one, and continuity of the dual action
in measure keeps their limit in that grade. The last lemma of HL-06 turns
this convergence into predual norm convergence. Thus \(F\) is norm holomorphic.
The spectral cuts prove differentiability in the measure algebra; they are
never asserted to approximate \(F\) inside a homogeneous analytic space.

On the two boundary lines the direct module formulas are

\[
 F(it)=(h^{it}k^{-it})k,
\tag{HL.41}
\]

\[
 F(1+it)=h(h^{it}k^{-it}).
\tag{HL.42}
\]

The parenthesized operator has grade zero and is a contraction in \(M\).
Consequently

\[
 \begin{aligned}
 \|F(it)\|_1&\leq\|k\|_1,\\
 \|F(1+it)\|_1&\leq\|h\|_1.
 \end{aligned}
\tag{HL.43}
\]

For the sharp interior estimate, first take \(\|h\|_1=\|k\|_1=1\).
The initial product bound gives
\(\|F(u+it)\|_1\leq B(u)=u^{-u}(1-u)^{-(1-u)}\).
Fix \(0<\delta<1/2\). The function is norm holomorphic and bounded on the
closed inner strip \(\delta\leq\Re z\leq1-\delta\), and both boundary
bounds are \(B(\delta)\). Apply CI-02 there. For each fixed interior point
let \(\delta\downarrow0\); since \(B(\delta)\to1\), its norm is at most one.
This use of inner strips requires no unproved norm continuity across an
outer boundary. Rescaling \(h,k\) and using (HL.43) proves

\[
 \boxed{\begin{aligned}
 \|h^z k^{1-z}\|_1
 &\leq\|h\|_1^{\Re z}
        \|k\|_1^{1-\Re z}.
 \end{aligned}}
\tag{HL.44}
\]

Zero inputs give a zero product; endpoint geometric means use \(c^0=1\).
All operator powers remain supported. The mathematical source comparison is
Hiai, section 11, Lemmas 11.14 and 11.17--11.21; the derivative and inner-strip
arguments above include their actual topology and support conditions.

**Continuity on the closed strip.** The same family is continuous in the
predual norm even where a real exponent becomes zero. Here is a measure-topology
argument that also covers a nonfaithful density. Near \(z=it_0\), restrict to
\(0\leq\Re z\leq1/2\). Write \(e_R=1_{(0,R]}(h)\) and cut the second
factor into its spectral regions \([0,\eta)\), \([\eta,R]\) and \((R,\infty)\),
where \(0<\eta<1<R\). Omitting the high part of the first or second density
changes the product by operators with left or right trace support at most
\(\tau(1_{(R,\infty)}(h))\) or \(\tau(1_{(R,\infty)}(k))\). These tend to
zero as \(R\to\infty\). After the first cut, the low part of the second
factor has operator norm at most
\[
 \max(1,R^{1/2})\eta^{1/2}.
\]
On the remaining region, \(e_Rh^z\) is uniformly bounded and strongly
continuous up to \(z=it_0\), by spectral dominated convergence on the support
of \(h\). The operator \(1_{[\eta,R]}(k)k^{1-z}\) is norm continuous and
has a fixed finite-trace support \(q=1_{[\eta,R]}(k)\).

If bounded operators \(B_n=B_nq\) converge strongly to zero and are uniformly
bounded, normality of the finite functional \(a\mapsto\tau(qaq)\) gives
\(\tau(B_n^*B_n)\to0\). The spectral estimate
\(\tau(1_{(\delta,\infty)}(|B_n|))\leq\delta^{-2}\tau(B_n^*B_n)\)
then gives convergence in measure. Apply this to the middle-region differences,
first keeping \(R,\eta\) fixed, then letting \(\eta\downarrow0\) and
\(R\to\infty\). This proves measure continuity at the left boundary.
Apply the same argument to
\(F(z)^*=k^{1-\bar z}h^{\bar z}\) at the right boundary. The differences
of the original products have grade one; HL-06 therefore upgrades their
measure convergence to predual norm convergence. The auxiliary cuts do not
claim to preserve grades, and no interpolation-space convergence has been
inferred from these cuts.


## The corrected Banach range for a fixed grade

For \(\alpha=p+iq\), \(0<p\leq1\), define

\[
 \|T\|_\alpha=\left(\int|T|^{1/p}\right)^p.
\tag{HL.45}
\]

HL-05 makes this finite. We first prove the complementary product bound.
If \(0<p<1\), write \(S=u h^p\) and \(T=k^{1-p}v\), using the left polar
decomposition for \(S\) and right polar decomposition for \(T\).
Here \(h,k\) are positive grade-one densities, while \(u,v\) are bounded
core partial isometries whose imaginary grades cancel. Their spectral
supports give \(\|S\|_\alpha=(\int h)^p\) and
\(\|T\|_{1-\alpha}=(\int k)^{1-p}\). The bounded module estimate for \(\mu_1\)
and (HL.44) prove
\(\|ST\|_1\leq\|S\|_\alpha\|T\|_{1-\alpha}\).
This does not assume \(u,v\in M\). At the zero/one real-grade endpoints use
bounded multiplication and the same \(\mu_1\) estimate.

The pairing is norming without an onto duality assumption. For nonzero
\(S=u h^p\), set \(T_0=h^{1-p}u^*\). Then
\(ST_0=u h u^*\), and its nonzero spectral tails are equivalent to those
of \(h\). Thus \(\int ST_0=\int h\) and
\(\|T_0\|_{1-\alpha}=(\int h)^{1-p}\).
Normalize \(T_0\) to have gauge one. Together with the product bound this gives

\[
 \|S\|_\alpha
 =\sup_{\|T\|_{1-\alpha}\leq1}\left|\int ST\right|.
\]

Linearity of the grade-one integral proves the triangle inequality from this
supremum. Homogeneity and separation follow from the distribution law.
For \(p=1\), the imaginary-grade isometry below reduces to HL-06.

Completeness retains the actual measurable limit. The exact size formula
\(\mu_t(T)=\|T\|_\alpha t^{-p}\) turns every norm-Cauchy net into a
measure-Cauchy net. MT-05--09 give a measurable limit, and trace scaling makes
\(\theta_s\) continuous in measure, preserving the grade. For fixed \(n\)
(or a fixed index in the original directed net), apply
\(\mu_{s+t}(S+T)\leq\mu_s(S)+\mu_t(T)\) to the differences with the limit.
Let the moving index tend to its measure limit and then let \(t\downarrow0\).
It gives \(\|T_n-T\|_\alpha\leq\liminf_m\|T_n-T_m\|_\alpha\).
The Cauchy condition proves norm convergence. Hence the homogeneous space
is Banach.

**The state-dependent compatible couple.** To specify a meaningful compatible couple,
fix a faithful state \(\chi\), put \(d=h_\chi\), and embed
\(X_0=J_\chi(M)\) in \(X_1=M_*\), where \(J_\chi(x)(y)=\chi(yx)\) and
\(X_0\) has the transported operator norm. Faithfulness proves injectivity
by testing at \(y=x^*\). The supplementary identification target is

\[
 [X_0,X_1]_p.
\tag{HL.46}
\]

The map \(T\mapsto F_{T d^{1-p}}\) and its onto isometry are proved in
HL-12, after the independent duality proof of HL-10.
The Banach argument above does not use that later interpolation theorem.
The raw inclusions of grades zero and one into the measurable algebra would
give a zero intermediate space: the bounded endpoint projections induced by
\((e^{-s}\mathrm{Id}-\theta_s)/(e^{-s}-1)\), \(s\ne0\), annihilate every
interpolation element by CI-05.

For the imaginary part, the core unitary \(d^{-iq}\) gives a linear bijection

\[
 R_{d^{-iq}}:\mathscr H(p+iq)\longrightarrow\mathscr H(p).
\tag{HL.47}
\]

Indeed \(|Td^{-iq}|=d^{iq}|T|d^{-iq}\). Traciality preserves every spectral-tail
trace, so the distribution constant and gauge are unchanged:

\[
 \|Td^{-iq}\|_p=\|T\|_{p+iq}.
\tag{HL.48}
\]

At real grade zero the spectral-tail argument of HL-04 gives boundedness;
the same unitary coordinate identifies an imaginary grade with \(M\)
isometrically.

For the counterexample beyond the Banach range, take orthogonal positive
grade-one densities \(h_1,h_2\) of integral one, and let \(p>1\).
Set \(T_j=h_j^p\). Spectral calculus on the two supports gives

\[
 (T_1+T_2)^{1/p}=h_1+h_2,
\tag{HL.49}
\]
\[
 \|T_1\|_p=\|T_2\|_p=1,\qquad
 \|T_1+T_2\|_p=2^p>2.
\tag{HL.50}
\]

The displayed gauge is then a quasi-norm. The corrected positive Banach range is

\[
 0<\Re\alpha\leq1.
\tag{HL.51}
\]

A separable factor other than the scalar factor supplies the two orthogonal
nonzero supports used in the counterexample; the source's universal assertion
is refuted already by a matrix factor. In the scalar factor each homogeneous
space is one-dimensional, so its gauge is a norm even outside this universal
Banach range.

## Products, Hölder bounds and the cyclic integral

Let \(T_j\in\mathscr H(\alpha_j)\), \(1\leq j\leq n\), with

\[
 \alpha_1+\cdots+\alpha_n=1.
\tag{HL.52}
\]

For a nonzero product every factor is nonzero, so HL-04 forces
\(p_j=\Re\alpha_j\geq0\). These real grades sum to one and are at most one.
Grade-zero real parts give bounded operators. Zero-factor products are
trivial; on a zero space of negative real grade set the gauge of its sole
element to zero. The desired estimate is

\[
 \|T_1\cdots T_n\|_1\leq
 \prod_{j=1}^n\|T_j\|_{\alpha_j}.
\tag{HL.53}
\]

The product belongs to the measurable algebra by MT-09, and grade addition
already proves

\[
 T_1\cdots T_n\in\mathscr H(1).
\tag{HL.54}
\]

We prove the full finite-product bound without presuming a multilinear
homogeneous strip representation. For \(p_j>0\) put
\(r_j=1/p_j\), \(C_j=\|T_j\|_{\alpha_j}^{r_j}\) and
\(A_j=u_j\min(|T_j|,1)\). These bounded caps are auxiliary core operators,
not homogeneous operators. The exact spectral distribution gives, for
\(\varepsilon>0\),

\[
 \tau(|A_j|^{r_j(1+\varepsilon)})
 =C_j(1+\varepsilon^{-1}).
\]

For \(p_j=0\) put \(A_j=T_j\). Apply the tracial product theorem TI-10
iteratively, with output exponent \(1+\varepsilon\) and input exponents
\(r_j(1+\varepsilon)\). All intermediate exponents are at least one,
since the partial reciprocal sums are at most \(1/(1+\varepsilon)\).

Write \(X=T_1\cdots T_n\), \(A=u_X\min(|X|,1)\) and
\(Q=A_1\cdots A_n\). Each difference \(T_j-A_j\), for \(p_j>0\), has
finite left and right trace support. Measurable multiplication preserves
finite trace rank: the right support of \(BY\) lies under that of \(Y\),
and polar equivalence bounds its left trace rank by that of \(Y\);
the right-multiplication argument is analogous. Projection subadditivity
handles sums. Expanding \(X-Q\) and \(X-A\) therefore shows that \(Q-A\)
has finite trace rank. It is also bounded, so its tracial
\(L^{1+\varepsilon}\) norm is uniformly bounded as \(\varepsilon\downarrow0\).

The cap \(A\) has distribution constant \(\|X\|_1\), hence
\(\varepsilon^{1/(1+\varepsilon)}
 \|A\|_{L^{1+\varepsilon}(\tau)}\to\|X\|_1\).
Tracial Minkowski makes the same limit hold for \(Q\). After multiplication
by \(\varepsilon^{1/(1+\varepsilon)}\), the tracial Hölder bound tends to
\(\prod_j\|T_j\|_{\alpha_j}\), because \(\sum_jp_j=1\).
This proves (HL.53), including imaginary grades and bounded endpoints.

For cyclicity we prove the two-factor identity first. If \(S,T\) have the
same grade \(1/2+ib\), polar equivalence gives
\(\int S^*S=\int SS^*\). Polarize this identity using \(S+i^kT\),
\(k=0,1,2,3\). It gives \(\int ST^*=\int T^*S\).
This argument applies to the common complex half grade, not just the real one.

Next let \(A,B\) have complementary real grades \(p,1-p\), \(0<p<1\).
The real and imaginary parts decompose each into a complex linear combination
of positive elements of its same real grade. For positive elements write
\(A=h^p\), \(B=k^{1-p}\). By HL-07 the scalar functions
\(\int h^z k^{1-z}\) and \(\int k^{1-z}h^z\) are holomorphic in the
open strip. On \(z=1/2+it\), the common-half-grade identity applies to
\(S=h^z\) and \(T=k^z\): both have grade \(1/2+it\), and
\(T^*=(k^z)^*=k^{\bar z}=k^{1-z}\) on this line. Thus
\(\int ST^*=\int T^*S\) says precisely that the two functions agree there.
The identity theorem gives equality throughout the strip, in particular
at \(z=p\). Linearity gives \(\int AB=\int BA\) for the original elements.
The real zero/one endpoints are the module identity of HL-06.

For complementary complex grades \(p+ib,1-p-ib\), put \(w=d^{ib}\).
Then \(A=Sw^*\) and \(B=wT\) have complementary real grades,
\(ST=AB\), and \(TS=w^*BAw\). Conjugation by this core unitary preserves
the integral of a positive grade-one operator by equality of spectral tails;
linearity extends it to all of \(\mathscr H(1)\). Thus
\(\int ST=\int TS\), including the bounded endpoints.
Group the first \(n-1\) factors in (HL.52) and apply this two-factor result:

\[
 \int T_1T_2\cdots T_n
 =\int T_nT_1T_2\cdots T_{n-1}.
\tag{HL.55}
\]

No localizer has been commuted past a homogeneous factor.

## Complementary grades are exact dual partners

The norming, finite-coordinate density and closed-range separation steps below use NP1 and NP2 in their full normed-space and locally convex forms. They do not use Banach–Alaoglu or Krein–Smulian.

Let \(\alpha=p+iq\), \(0<p<1\). The pairing is

\[
 \langle S,T\rangle=\int ST,\qquad
 S\in\mathscr H(\alpha),\ T\in\mathscr H(1-\alpha).
\tag{HL.56}
\]

HL-08--09 give

\[
 |\langle S,T\rangle|
 \leq\|S\|_\alpha\|T\|_{1-\alpha}.
\tag{HL.57}
\]

For \(S=u h^p\), the exact polar equality test is

\[
 T_0=h^{1-p}u^*.
\tag{HL.58}
\]

Its spectral tails give

\[
 \begin{aligned}
 \int ST_0&=\int h,\\
 \|S\|_\alpha&=(\int h)^p,\\
 \|T_0\|_{1-\alpha}&=(\int h)^{1-p}.
 \end{aligned}
\tag{HL.59}
\]

It proves norming in each variable, using cyclicity for the reversed orientation.
We now prove onto representation rather than assume it in a strip contract.

**Uniform convexity for \(0<p\leq1/2\).** Put \(r=1/p\geq2\).
For the real-grade space the required Clarkson bound is

\[
 \|A+B\|_p^r+\|A-B\|_p^r
 \leq2^{r-1}(\|A\|_p^r+\|B\|_p^r).
\]

Here is a direct strip proof. Normalize the right-hand parenthesis to one
and write \(A=uH^p\), \(B=vK^p\), with
\(\int H+\int K=1\). To test the norm of the pair \((A+B,A-B)\),
take \(C=P^{1-p}w\), \(D=Q^{1-p}x\) with
\(\|C\|_{1-p}^{r'}+\|D\|_{1-p}^{r'}=1\), \(r'=1/(1-p)\).
Then \(\int P+\int Q=1\). The norming supremum for the two-component
space is its scalar \(\ell^r\) norm: apply (HL.59) to each component and
choose the scalar conjugate-exponent weights.

Use the holomorphic scalar function

\[
 G(z)=\int (uH^z+vK^z)P^{1-z}w
          +(uH^z-vK^z)Q^{1-z}x.
\]

Holomorphy follows term by term from HL-07 and bounded \(M\)-module
multiplication. On each line \(\Re z=\delta>0\), Hölder bounds its modulus
by

\[
 ((\int H)^\delta+(\int K)^\delta)
 ((\int P)^{1-\delta}+(\int Q)^{1-\delta})\leq2.
\]

On \(\Re z=1/2\), Cauchy--Schwarz in the common-half-grade Hilbert
space, applied to the two components, gives \(|G(z)|\leq\sqrt2\).
That Hilbert structure is obtained by polarizing
\(\int S^*S\); positivity, (HL.45), and the common-half-grade cyclic
identity of HL-09 identify its norm, while HL-08 supplies completeness.
The parallelogram identity makes the squared norm of
\((uH^z+vK^z,uH^z-vK^z)\) equal to two, and the dual test pair has norm one.
For \(p<1/2\), apply CI-02 on \(\delta\leq\Re z\leq1/2\) and let
\(\delta\downarrow0\). It gives \(|G(p)|\leq2^{1-p}\).
At \(p=1/2\) use the Hilbert estimate itself. Take the two-component
norming supremum and undo normalization to obtain Clarkson's bound.
Zero densities remain supported throughout the argument.

For unit vectors with \(\|A-B\|_p\geq\eta\), the bound implies
\(\|(A+B)/2\|_p^r\leq1-(\eta/2)^r\). This is uniform convexity.
The unitary isometry (HL.47--48) gives it for imaginary translates too.

**Why uniform convexity gives reflexivity here.** For any Banach space \(E\),
the canonical image of its unit ball is weak-star dense in the bidual unit
ball. Indeed, if its image under finitely many functionals failed to
approximate the corresponding bidual coordinates, finite-dimensional real
separation would produce \(f\in E^*\) and \(x^{**}\) of norm at most one
with \(\Re x^{**}(f)>\sup_{\|x\|\leq1}\Re f(x)=\|f\|\), a contradiction.
This is the finite-coordinate Hahn--Banach argument.

Let now \(E\) be uniformly convex and \(\|x^{**}\|=1\).
Take a net \(x_i\) in its unit ball converging weak-star to \(x^{**}\).
For any prescribed \(\eta>0\), choose the convexity deficit \(\delta>0\)
and a unit \(f\in E^*\) with \(\Re x^{**}(f)>1-\delta/2\).
Eventually \(\Re f(x_i)>1-\delta\). Every midpoint in that tail has norm
greater than \(1-\delta\), so uniform convexity gives
\(\|x_i-x_j\|<\eta\). The net is norm Cauchy and has a limit \(x\in E\);
its canonical image is \(x^{**}\). Scaling handles every bidual element.
Thus \(E\) is reflexive. Its dual is reflexive as well: any element of
\(E^{***}\) restricts on the surjective canonical copy of \(E\) to an
element of \(E^*\), which represents it on all of \(E^{**}\).

**Onto dual representation.** The map
\(\Phi:T\mapsto[S\mapsto\int ST]\) is a linear isometry by (HL.59).
Its range is norm closed because the complementary space is Banach, and a
closed linear subspace is weakly closed by Hahn--Banach.
It is weak-star dense: a proper weak-star closure would, by separation on
finitely many evaluations, give a nonzero \(S\) annihilating the range,
contradicting the polar norming test.

If \(p\leq1/2\), \(\mathscr H(\alpha)\) is reflexive by the preceding proof.
Weak and weak-star topologies on its dual coincide, so the closed and dense
range is the whole dual. If \(p>1/2\), apply that case to \(1-\alpha\).
It identifies \(\mathscr H(\alpha)\) with the dual of its reflexive
complementary space. Taking the bidual and using cyclicity identifies the
dual of \(\mathscr H(\alpha)\) with \(\mathscr H(1-\alpha)\) in the
orientation (HL.56). Hence

\[
 \boxed{\mathscr H(1-\alpha)\cong\mathscr H(\alpha)^*,\qquad
 T\longmapsto[S\mapsto\int ST]}
\tag{HL.60}
\]

is an onto isometry. At the endpoints, \(\mathscr H(1)\cong M_*\) and
\(M=\mathscr H(0)\cong M_*^*\). The full dual of \(M\) need not consist of
normal functionals. The convexity/reflexivity source comparison is Hiai,
section 11, Propositions 11.24--11.26 and Theorem 11.28; the proof here
supplies the convexity and finite-coordinate reflexivity steps.

## Core commutants recover centralizers

Fix a faithful normal semifinite weight \(\varphi\), and put

\[
 \begin{aligned}
 \mathcal A^\varphi&=\pi^\varphi(A),\\
 \mathcal D^\varphi&=Z(\widetilde M)\vee\mathcal A^\varphi.
 \end{aligned}
\tag{HL.61}
\]

The algebra \(\mathcal A^\varphi\) is generated by
\(h_\varphi^{it}=\varphi^{it}\). The supported-symbol calculation in
HL-01, here with full support, proves the modular implementation

\[
 \begin{aligned}
 \sigma_t^\varphi(x)&=h_\varphi^{it}x h_\varphi^{-it},\\
 x&\in M.
 \end{aligned}
\tag{HL.62}
\]

Hence

\[
 \begin{gathered}
 x\in(\mathcal A^\varphi)'\cap M\\
 \Updownarrow\\
 xh_\varphi^{it}=h_\varphi^{it}x\quad(t\in\mathbb R)\\
 \Updownarrow\\
 \sigma_t^\varphi(x)=x\quad(t\in\mathbb R)\\
 \Updownarrow\\
 x\in M_\varphi .
 \end{gathered}
\tag{HL.63}
\]

This proves

\[
 (\mathcal A^\varphi)'\cap M=M_\varphi.
\tag{HL.64}
\]

The two algebras joined in (HL.61) commute, so
\(\mathcal D^\varphi\) is abelian. If
\(x\in\mathcal D^\varphi\cap M\), then \(x\) commutes with
\(\mathcal A^\varphi\), and (HL.64) places \(x\) in \(M_\varphi\). Every
\(y\in M_\varphi\) commutes with \(\mathcal A^\varphi\) by (HL.64), and it
commutes with \(Z(\widetilde M)\) by definition. It therefore commutes with all
of \(\mathcal D^\varphi\), in particular with \(x\). Thus

\[
 \boxed{
 \mathcal D^\varphi\cap M\subseteq Z(M_\varphi).}
\tag{HL.65}
\]

The source states an inclusion in (HL.65), and the proof preserves that exact
strength. Equality needs additional information about the core center and is
not inferred here.

## The state-dependent interpolation isometry

Fix a faithful normal state \(\chi\) and let \(d=h_\chi\). We identify
\(\mathscr H(1)\) with \(M_*\) by HL-06. Thus
\[
 X_0=Md,\qquad \|xd\|_{X_0}=\|x\|_\infty,
 \qquad X_1=\mathscr H(1)=M_*.
\tag{HL.66}
\]
Indeed, \(F_{xd}(y)=\chi(yx)=J_\chi(x)(y)\). Since \(\int d=1\), the
inclusion \(X_0\subset X_1\) is contractive. Its injectivity also follows
from faithfulness, by testing at \(y=x^*\). The sum space of CI-01 is
exactly \(X_1\), with its predual norm.

**Theorem.** For \(0<p<1\), the map
\[
 I_p:\mathscr H(p)\longrightarrow[X_0,X_1]_p,
 \qquad I_p(T)=T d^{1-p}
\tag{HL.67}
\]
is an onto linear isometry. In predual notation the image is
\(F_{T d^{1-p}}\). The interpolation space uses the norm-continuous,
boundary-decaying class of CI-03, with no change of definition.

The proof uses the Banach and duality results of HL-08--10 already established
without this identification. In particular, every real-grade space
\(\mathscr H(p)\), \(0<p<1\), is reflexive. We give the boundary approximation
and the surjectivity argument explicitly.

The compatible sum, boundary-decaying strip space and complete evaluation quotient are supplied by CI01, CI03 and CI04. Norm extension, norming and convex separation use NP1 and NP2.

### The embedded space and its endpoint ball

Hölder's inequality makes \(I_p\) a contraction into \(X_1\). It is injective
even though \(d^{p-1}\) need not be measurable. If \(T d^{1-p}=0\), put
\(q_n=1_{[1/n,n]}(d)\). The bounded operator \(d^{p-1}q_n\) is measurable,
so associativity of closed measurable products gives \(Tq_n=0\).
This equality implies \(q_nH\subset\ker T\): approximate a vector in
\(q_nH\) using the domain of the unclosed composition, and use closedness
of \(T\). Since \(q_n\uparrow1\), the closed kernel is all of \(H\).
Hence \(T=0\).

Give \(Y=I_p(\mathscr H(p))\subset X_1\) its transported norm. Then
\(Y\) is a reflexive Banach space, continuously embedded in \(X_1\), and
\(xd=I_p(xd^p)\), so \(X_0\subset Y\).

We also need the unit ball of \(X_0\) to be closed in \(X_1\). Suppose
\(x_n d\to a\) in predual norm and \(\|x_n\|_\infty\leq1\).
The normal functionals
\[
 \eta_y(x)=\chi(yx),\qquad y\in M,
\]
have norm-dense linear span in \(M_*\). Otherwise Hahn--Banach and
\((M_*)^*=M\) would give a nonzero \(x\in M\) with \(\chi(yx)=0\)
for every \(y\); taking \(y=x^*\) contradicts faithfulness.
For each \(y\), \(\eta_y(x_n)=F_{x_nd}(y)\) converges. Uniform boundedness
and this norm density imply that \(\omega(x_n)\) converges for every
\(\omega\in M_*\). Its limit is a bounded linear functional on \(M_*\)
of norm at most one, hence is evaluation at an \(x\in M\) with
\(\|x\|_\infty\leq1\). Testing at every \(y\) shows \(a=xd\).
This proves the claimed closedness. Scaled balls are closed as well.

### Smoothing an admissible strip inside the smaller endpoint

Write \(k_n(t)=\sqrt{n/\pi}\,e^{-nt^2}\). For
\(f\in\mathcal F(X_0,X_1)\), define in \(X_1\)
\[
 g_n(z)=\int_{\mathbb R}k_n(t)f(z+it)\,dt.
\tag{HL.68}
\]
These integrals exist by approximation with step functions and an integrable
norm bound. On the two boundaries, convolution is also an integral in
\(X_j\), and

\[
 \sup_t\|g_n(j+it)\|_{X_j}\leq\sup_t\|f(j+it)\|_{X_j}.
\]

It preserves continuity and vanishing at infinity. Interior holomorphy follows
by integrating the Cauchy formula on a disk and interchanging integrals under
the Gaussian bound. Thus \(g_n\in\mathcal F\).

The two boundary functions of \(f\) are uniformly continuous, since they
belong to \(C_0(\mathbb R;X_j)\). Splitting the convolution into
\(|t|<\delta\) and its complement proves
\(\|g_n-f\|_{\mathcal F}\to0\).

More is true: \(g_n(z)=x_n(z)d\), where \(x_n\) is an entire
operator-norm-holomorphic \(M\)-valued function bounded on the closed strip.
To see this, contour shifting in \(X_1\) gives
\[
 g_n(z)=\sqrt{n/\pi}
  \int_{\mathbb R}e^{n(z-it)^2}f(it)\,dt.
\tag{HL.69}
\]
For completeness, apply the scalar Cauchy theorem to
\(e^{n(z-\zeta)^2}\ell(f(\zeta))\) between the vertical lines
\(0\) and \(\Re z\), first using an inner line and then continuity to
reach the boundary. On the horizontal edges the Gaussian tends uniformly to
zero, while \(f\) is bounded in \(X_1\). Let their heights tend to infinity.
All \(\ell\in X_1^*\) give the identity, hence so does Hahn--Banach.
The right side of (HL.69) is an \(X_0\)-valued integral. Its kernels and
their complex derivatives have integrable bounds on compact sets. It is
therefore entire in \(X_0\), and
\[
 \|x_n(z)\|_\infty
 \leq e^{n(\Re z)^2}\sup_t\|f(it)\|_{X_0}.
\]
This proves the assertion and supplies the specific analytic approximation
needed below.

### The lower norm estimate

Consider any \(g\in\mathcal F\) of the form \(g(z)=x(z)d\), with
\(x\) operator-norm holomorphic and bounded on the closed strip and
continuous there. To estimate \(\|x(p)d^p\|_p\), take a unit vector of
the complementary grade, written \(R=u h^{1-p}\), where
\(\int h=1\) and \(u\in M\) is its polar partial isometry. Define
\[
 H(z)=\int u h^z d^{1-z}x(1-\bar z)^*.
\tag{HL.70}
\]
HL-07, including its closed-strip continuity proof, and bounded module
multiplication make \(H\) bounded and continuous on the closed strip and
holomorphic inside it. The reflected adjoint of \(x\) is holomorphic.
At the left boundary \(b_t=u h^{it}d^{-it}\) is a contraction in \(M\), so
\[
 |H(it)|=\left|\int b_t d x(1+it)^*\right|
 \leq\|x(1+it)d\|_1.
\]
At the right boundary, (HL.44) gives
\[
 |H(1+it)|\leq\|x(it)\|_\infty.
\]
Three lines, evaluated at \(1-p\), therefore bounds
\(\left|\int R(x(p)d^p)^*\right|\) by \(\|g\|_{\mathcal F}\).
The norming pairing of HL-08--10, and invariance of the norm under adjoints,
give
\[
 \|g(p)\|_Y=\|x(p)d^p\|_p\leq\|g\|_{\mathcal F}.
\tag{HL.71}
\]

Apply this estimate to the smoothings \(g_n\) above and to
\(g_n-g_m\). Their values at \(p\) are Cauchy in \(Y\). Completeness of
\(Y\), its continuous injection into \(X_1\), and
\(g_n(p)\to f(p)\) in \(X_1\) identify the limit with \(f(p)\).
Consequently
\[
 [X_0,X_1]_p\subset Y,
 \qquad \|a\|_Y\leq\|a\|_{[X_0,X_1]_p}.
\tag{HL.72}
\]
The actual representatives \(x_n(p)d^p\) converge in their grade-\(p\)
norm. Hölder gives convergence of their products with \(d^{1-p}\) in
grade-one norm, consistent with closed measurable multiplication.

### Admissible representatives and the reverse inclusion

Let \(T=u h^p\ne0\), put \(m=\int h>0\), and set
\[
 A_T(z)=m^{p-z}u h^z d^{1-z}.
\tag{HL.73}
\]
Then \(A_T(p)=I_p(T)\). It is bounded and predual-norm continuous on the
closed strip and holomorphic inside it. Its lower boundary belongs to
\(X_0\), and its endpoint bounds are exactly
\[
 \sup_t\|A_T(it)\|_{X_0}\leq m^p,
 \qquad \sup_t\|A_T(1+it)\|_1\leq m^p=\|T\|_p.
\]
The lower boundary need not be operator-norm continuous. We therefore do
not assert \(A_T\in\mathcal F\).

Convolve \(A_T\) with \(k_n\) as in (HL.68), calling the result
\(B_n\), and put
\[
 a_n(z)=e^{(z^2-p^2-1)/n}B_n(z).
\]
The lower-boundary integral belongs to \(X_0\) with norm at most \(m^p\):
its approximating finite weighted averages lie in that ball, which we proved
closed in \(X_1\). The same observation for integrals against a complex
kernel gives the bound by \(m^p\) times its \(L^1\)-norm. In particular,
translation of the Gaussian kernel proves continuity of \(B_n(it)\) in
\(X_0\). The other boundary is norm continuous by the same argument in
\(X_1\). The exponential factor supplies boundary decay, has modulus at
most one on the strip, and gives \(a_n(p)=e^{-1/n}B_n(p)\).
Interior holomorphy and sum-norm continuity follow as for (HL.68).
Thus
\[
 a_n\in\mathcal F,\qquad
 \|a_n\|_{\mathcal F}\leq\|T\|_p,\qquad
 a_n(p)\longrightarrow I_p(T)\quad\hbox{in }X_1.
\]

To turn this into the required interpolation conclusion we use reflexivity,
not a claim that the interpolation ball is closed in the predual. Let
\(j:Y\hookrightarrow X_1\) be the inclusion. The subspace
\(j^*(X_1^*)\) is norm dense in \(Y^*\). Indeed, if its norm closure were
proper, Hahn--Banach would give a nonzero element of \(Y^{**}\) annihilating
it. Reflexivity writes that element as evaluation at \(y\in Y\);
then every \(\ell\in X_1^*\) annihilates \(j(y)\). This contradicts
injectivity of \(j\).

By (HL.72), the sequence \(a_n(p)\) is bounded in \(Y\) by \(\|T\|_p\).
Its convergence in \(X_1\) gives convergence against \(j^*(X_1^*)\).
The density just proved and the uniform \(Y\)-bound give weak convergence
in \(Y\) to \(I_p(T)\). Hahn--Banach separation of a closed convex set
now shows that finite convex combinations of any tail approximate
\(I_p(T)\) in \(Y\)-norm. Each such combination still has interpolation
norm at most \(\|T\|_p\). Scaling and the zero vector show that, for every
\(y\in Y\) and \(\varepsilon>0\), there is a \(c\in[X_0,X_1]_p\) with
\[
 \|c\|_{[X_0,X_1]_p}\leq\|y\|_Y,
 \qquad \|y-c\|_Y<\varepsilon.
\]

Fix \(0<q<1\). Apply this approximation successively to the remaining
error, making the error after step \(k\) at most \(q^k\|y\|_Y\).
The resulting series of interpolation elements has total interpolation norm
at most \(\|y\|_Y/(1-q)\). Completeness from CI-04 gives its sum, and the
continuous injection into \(Y\) identifies the sum with \(y\). Letting
\(q\downarrow0\) proves the reverse of (HL.72). This proves the onto
isometry (HL.67).

One may also obtain actual strip representatives from the series: choose
a representative of each term with a summable, arbitrarily small excess
over its interpolation norm and sum in the complete strip space of CI-03.
Their values have grade one, their inverse images have grade \(p\), and
Hölder controls the closed products throughout. This establishes admissible
representatives with boundary norm arbitrarily close to \(\|T\|_p\);
it does not assert that the infimum defining the norm is attained.

### Products with several varying grades

The analytic product requirement can be stated with its exact grades. Take
positive grade-one densities \(h_1,\ldots,h_N\) in \(\mathscr H(1)_+\), contractions
\(u_1,\ldots,u_N\in M\), nonnegative numbers \(a_j,b_j\) with
\(\sum_j a_j=\sum_j b_j=1\), and real \(q_j\) with \(\sum_jq_j=0\).
Put
\[
 \alpha_j(z)=a_j+(b_j-a_j)z+iq_j,
 \qquad P(z)=\prod_{j=1}^N u_jh_j^{\alpha_j(z)}.
\]
Supported imaginary powers are used at zero real part. For every point of
the closed strip the product has grade one, and HL-09 gives the exact bound
\[
 \|P(s+it)\|_1
 \leq\prod_{j=1}^N
       \left(\int h_j\right)^{(1-s)a_j+sb_j}.
\]
Zero inputs are treated separately; a zero density makes its supported
factor zero. In the open strip, each nonconstant exponent has positive real
part, so the measure derivative argument of HL-07 applies factor by factor.
An exponent with \(a_j=b_j=0\) is constant and its factor is bounded.
The product rule in measure and the constant total grade make \(P\)
predual-norm holomorphic.

For boundary continuity, cut off the high spectral tail of each density.
The differences have trace rank bounded by the sum of those tail traces,
also after multiplication by the other measurable factors. At each boundary
some exponent has positive real part. Keep one such factor in a finite
spectral band \([\eta,R]\); its omitted low part is small in operator norm,
uniformly near that boundary after all the high cuts. The remaining bounded
factors are strongly and strongly-adjoint continuous. The middle product
has the form \(C(z)qD(z)\) with \(\tau(q)<\infty\). For uniformly bounded
strongly-adjoint-continuous \(C,D\), its differences tend to zero in
tracial \(L^2\): apply normality of \(\tau(q\,\cdot\,q)\) to
\((C(z)-C(z_0))q\) and \(q(D(z)-D(z_0))\), and use the bounded multiplier
estimate. Hence they tend to zero in measure. Remove the auxiliary cuts
and use grade one to obtain predual-norm continuity. This proves the stated
multilinear analytic families and their endpoint bounds without changing
grades in the approximating strip construction above.

**Source comparison.** Kosaki, *Applications of the complex interpolation
method to a von Neumann algebra: non-commutative \(L^p\)-spaces* (1984),
Theorem 9.1 and Remark 9.2, printed pp. 57--59, give this identification as
the left-embedding case, with the source's \(L^r\) exponent \(r=1/p\).
The smoothing/reflexivity mechanism is compared with Theorem 1.5,
Lemma 1.6 and Theorem 1.8, printed pp. 33--36. The proof above supplies
the contour smoothing, lower estimate, closed endpoint ball and convergent
series argument here; these source references replace none of those steps.


HL-01--11 cover the eleven XII.6 callback groups. Equations (HL.17) and
(HL.51) retain the source corrections. The arguments include the
actual measure-to-predual holomorphy bridge, inner-strip bound, norming
triangle inequality, finite-product trace-cap limit, graded cyclicity,
Clarkson convexity and onto dual representation. The core and density inputs
are the written LP01--04 proofs, with the supported-symbol and spectral-class
arguments in HL-01 and the localizer evaluation in HL-02. HL-12 gives the state-dependent
interpolation isometry, its admissible strip construction and finite-product
analytic families, with exact source comparison to Kosaki's Theorem 9.1.
