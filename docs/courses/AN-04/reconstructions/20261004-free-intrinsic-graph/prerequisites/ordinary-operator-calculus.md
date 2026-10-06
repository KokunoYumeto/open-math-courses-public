# Ordinary symbols, composition and proper localization

This bounded modified selection retains the arguments of AN03-U010,
*Symbols, operators and Sobolev scales*, Sections 3–5, and AN03-U012,
*Detecting regularity without choosing coordinates*, Sections 1–2 and 5.
It specializes them to the ordinary class \(S^m_{1,0}\) used in the
frequency-graph lesson. The metric verification and the identification of
the multiplier with the actual operator integral are supplied explicitly.
The general manifold and coordinate-transport theorems remain separate.

Original principal author and publisher: AN-03 course-writing task /
AN-03 local course project. Copyright © 2026 AN-03 course project
contributors. Earlier modification: AN-03 course-writing task and
OpenAI Codex. This selection and its connecting arguments: GPT-6 Astra
(OpenAI), Ultra, 4 October 2026; publisher: AN-04 local course project.

Permission is granted to copy, distribute and modify this component under
the GNU Free Documentation License, Version 1.2 only, with no Invariant
Sections, no Front-Cover Texts and no Back-Cover Texts. The
[licence](operator-notices/COPYING), [title information](operator-notices/TITLE_PAGE.md),
[history](operator-notices/HISTORY.md) and [rights notice](operator-notices/RIGHTS.md)
accompany it.

## O0. Exact prerequisites and conventions

The [quadratic multiplier companion](gauss-transform-estimates.md)
includes its complete localization and finite-dimensional prerequisites.
The [measure](measure-and-l2.md) and [Fourier](fourier-l2.md) companions
supply completed integration, inversion and distributional compatibility.
Use \(D=-i\partial\), Fourier exponential \(e^{-ix\cdot\xi}\), and
inverse factor \((2\pi)^{-n}\). Matrix symbols have fixed finite sizes
and are multiplied in the displayed order.

Write \(a\in S^m\) when every derivative satisfies
\[
 |\partial_x^\beta\partial_\xi^\alpha a(x,\xi)|
       \leq C_{\alpha,\beta}\langle\xi\rangle^{m-|\alpha|}.
 \tag{O1}
\]
These are global estimates in this paragraph. On an open base set the
same bounds are required on each compact subset. A compact base cutoff
then extends a local symbol by zero to a global symbol. Orders are real.
All statements include dimension zero, where the integrals have one
point, Fourier maps are the identity and symbols are finite matrices.

### O0.1. Product tests determine a distributional kernel

Let \(\varphi(x,y)\) be compact smooth in a product of two Euclidean
open sets. Choose compact smooth \(\alpha(x),\beta(y)\), each one
near the corresponding projection of its support. Extend \(\varphi\)
by zero to Euclidean space. Fourier inversion gives
\[
 \varphi(x,y)=(2\pi)^{-2n}\iint
       \widehat\varphi(\xi,\eta)
       \alpha(x)e^{ix\cdot\xi}\,
       \beta(y)e^{iy\cdot\eta}\,d\xi\,d\eta .
\]
The same integral converges uniformly after every fixed number of
base derivatives: its Fourier transform is Schwartz, so all resulting
polynomial factors are integrable. Truncate to larger frequency boxes
and approximate each compact integral by Riemann sums. Uniform
continuity on the compact base and frequency product makes these
sums converge with any fixed finite set of derivatives. At step \(k\)
make the error less than \(1/k\) for all derivatives through order
\(k\). The resulting finite sums of product test functions have one
fixed compact support and converge to \(\varphi\) in its complete
smooth test topology. Thus a distribution vanishing on all product
tests vanishes on \(\varphi\). This proves the kernel detection used
in O5–O6 without a general kernel representation theorem.

## O1. Schwartz action and the exact multiplier formula

For \(u\in\mathcal S\) define
\[
 \operatorname{Op}(a)u(x)=(2\pi)^{-n}
           \int e^{ix\cdot\xi}a(x,\xi)\widehat u(\xi)\,d\xi .
 \tag{O2}
\]
This integral and all its differentiated versions converge absolutely.
Output derivatives create finitely many powers of \(\xi\) and base
derivatives of \(a\). To estimate
\(x^\gamma\partial_x^\beta\operatorname{Op}(a)u\), move
\(|\gamma|\) frequency derivatives off the exponential by integration
by parts. Each resulting integrand is a symbol derivative, a polynomial
and a derivative of \(\widehat u\). Its integral is bounded by one
sufficiently large Schwartz seminorm of \(u\) times finitely many
symbol seminorms, with a remaining integrable weight of order less
than \(-n\). Boundary terms vanish by the same rapid decrease.
Thus (O2) maps \(\mathcal S\) continuously to itself, with uniform
operator seminorms on each bounded symbol set. Differentiating and
integrating once also gives
\[
 [\operatorname{Op}(a),D_j]=i\operatorname{Op}(\partial_{x_j}a),
 \qquad
 [\operatorname{Op}(a),x_j]=-i\operatorname{Op}(\partial_{\xi_j}a).
 \tag{O3}
\]

For \(c\in\mathcal S(\mathbb R^{2n})\), let \(Qc\) be the Fourier
multiplier \(e^{ip\cdot q}\) in the variables dual to \((y,\eta)\).
The partial Fourier transform in \(y\) is a Schwartz function of
\((p,\eta)\): multiplication by \(p\) is integration by parts in \(y\),
differentiation in \(p\) inserts powers of \(y\), and every seminorm is
bounded by integrating an arbitrarily decreasing \(y\) weight.
The same holds for its inverse. Their two-sided identities follow
from the supplied Fourier inversion theorem on each slice; the
seminorm estimates justify every parameter derivative.
The Fourier translation rule in \(\eta\) therefore gives
\[
 \begin{split}
 Qc(y,\eta)
  &=(2\pi)^{-n}\int e^{iy\cdot p}
                         \mathcal F_yc(p,\eta+p)\,dp\\
  &=(2\pi)^{-n}\iint e^{-iv\cdot w}
                              c(y+v,\eta+w)\,dv\,dw .
 \end{split} \tag{O4}
\]
For the second line expand the partial transform and substitute
\(p=w\), its original base variable \(y+v\). That double integral
is absolutely convergent for a Schwartz \(c\). This establishes
the multiplier normalization and sign without a kernel theorem.

## O2. The exact ordinary metric verification

In \((y,\eta)\) put
\[
 g_{(y,\eta)}(v,\nu)=|v|^2+\langle\eta\rangle^{-2}|\nu|^2,
 \qquad m(y,\eta)=\langle\eta\rangle^r .
 \tag{O5}
\]
The function \(\langle\eta\rangle\) is 1-Lipschitz: the reverse
triangle inequality applied to \((1,\eta)\) proves it. Thus, within
a metric ball of radius less than \(1/2\), the neighboring frequency
weights have ratio between \(1/2\) and \(3/2\). This proves slow
variation and local weight comparison, uniformly in the center.

For \(A(p,q)=p\cdot q\), the symmetric map is
\(\frac12\left(\begin{smallmatrix}0&I\\I&0\end{smallmatrix}\right)\).
The companion's dual-form calculation gives
\[
 g_Y^A(X-Y)=4\bigl(\langle\eta_Y\rangle^2|y_X-y_Y|^2
                                      +|\eta_X-\eta_Y|^2\bigr),
 \qquad h(X)=\frac1{2\langle\eta_X\rangle}\leq\frac12 .
 \tag{O6}
\]
In particular \(g_X\leq g_X^A\).
For \(u=\eta_X,v=\eta_Y\),
\(\langle u\rangle\leq\langle v\rangle+|u-v|
 \leq\langle v\rangle(1+|u-v|)\).
Interchange \(u,v\) for the reciprocal ratio. Squaring and using
\((1+t)^2\leq2(1+t^2)\) proves
\[
 g_Y(T)\leq2(1+|\eta_X-\eta_Y|^2)g_X(T),\qquad
 \frac{m(Y)}{m(X)}
 \leq2^{|r|/2}(1+|\eta_X-\eta_Y|^2)^{|r|/2}.
 \tag{O7}
\]
These are precisely the observation-point assumptions of the
quadratic-multiplier Theorems 7.1 and 8.1, with constants independent
of \(X,Y\). Consequently
\[
 Qc-\sum_{|\alpha|<N}
                  \frac{\partial_\eta^\alpha D_y^\alpha c}{\alpha!}
                  \in S^{r-N},\qquad c\in S^r.
 \tag{O8}
\]
The coefficient follows by expanding
\((iD_y\cdot D_\eta)^j/j!\); since \(iD_\eta=\partial_\eta\),
it has exactly the displayed sign. Every derivative has its own
finite input-seminorm bound. Convergence on bounded symbol sets in
the local smooth topology is preserved, as proved in the companion.

For parameters \((x,\xi)\), apply this to
\(c_{x,\xi}(y,\eta)=a(x,\eta)b(y,\xi)\).
Its weight is \(\langle\eta\rangle^{m_1}\langle\xi\rangle^{m_2}\).
A parameter derivative \(\partial_\xi^\alpha\partial_x^\beta\)
lowers the latter order by \(|\alpha|\); a transformed derivative
\(\partial_\eta^{\alpha'}\partial_y^{\beta'}\) lowers the former
by \(|\alpha'|\). Thus the full pre-diagonal remainder is bounded by
\[
 C\langle\eta\rangle^{m_1-N-|\alpha'|}
      \langle\xi\rangle^{m_2-|\alpha|}.
 \tag{O9}
\]
Parameter derivatives are genuine derivatives of the resulting
function: apply the compact symbol approximants from the metric
companion, use the estimates for every parameter derivative, and
pass to the limit in the fundamental theorem along compact parameter
segments. One additional derivative bounds the modulus of continuity;
a finite grid upgrades pointwise convergence to uniform convergence
on each compact set. Repeating this proves the assertion in every
order. All constants use finitely many original seminorms.

## O3. Adjoints, composition and tempered distributions

For Schwartz symbols, Fubini applied to (O2) twice gives the product
symbol
\[
 (a\circ b)(x,\xi)=(2\pi)^{-n}
  \iint e^{i(x-y)\cdot(\eta-\xi)}
                       a(x,\eta)b(y,\xi)\,dy\,d\eta
  =\left[Q_{y,\eta}c_{x,\xi}\right]_{y=x,\eta=\xi}.
 \tag{O10}
\]
For example \(a=a(\xi)\), \(b=e^{iv\cdot x}b_0(\xi)\) gives
\(a\circ b=e^{iv\cdot x}a(\xi+v)b_0(\xi)\), confirming the sign.
For an adjoint, interchanging the two base variables and conjugating
the scalar pairing gives, by the same integral (O4),
\[
 a^\dagger=Q(a^*).
 \tag{O11}
\]
Here \(^*\) is conjugate transpose and the pairing is
\((u,v)=\int u\overline v\), linear in \(u\).
Explicitly, the adjoint kernel has integrand
\(e^{i(x-y)\cdot\xi}a(y,\xi)^*\); its left symbol is obtained by
putting \(y=x+v,\xi=\eta+w\), giving \(e^{-iv\cdot w}\) in (O4).

Equations (O8)–(O9), followed by the diagonal chain rule, prove
\[
 \begin{aligned}
 a^\dagger&\in S^{m_1},\qquad a\circ b\in S^{m_1+m_2},\\
 a^\dagger-\sum_{|\alpha|<N}
       \frac{\partial_\xi^\alpha D_x^\alpha(a^*)}{\alpha!}
             &\in S^{m_1-N},\\
 a\circ b-\sum_{|\alpha|<N}
       \frac{(\partial_\xi^\alpha a)(D_x^\alpha b)}{\alpha!}
             &\in S^{m_1+m_2-N}.
 \end{aligned} \tag{O12}
\]
For a total frequency derivative of the diagonal product, each
derivative lands on either \(\xi\) or \(\eta\) in (O9); either choice
lowers the combined order by one. Base derivatives have order zero.

These formulas and the operator identities hold for all ordinary
symbols. To justify this passage, multiply symbols by cutoffs
\(\chi(\epsilon x)\chi(\epsilon\xi)\), with \(\chi=1\) near zero.
These are bounded approximants in the original symbol classes:
on the support of a differentiated frequency cutoff,
\(\epsilon\leq C\langle\xi\rangle^{-1}\), and all base cutoff
derivatives are bounded. They converge locally smoothly.
The multiplier theorem gives bounded, locally convergent adjoints
and products in their asserted orders. For a fixed Schwartz \(u\),
(O2) and dominated convergence give local smooth convergence of
the outputs. O1 bounds every stronger output Schwartz seminorm
uniformly; outside a large base ball one extra decay power makes
the tails small. Hence the outputs converge in every Schwartz
seminorm. The same uniform operator bounds permit passage through
the double composition. The adjoint pairing and
\[
 \operatorname{Op}(a)\operatorname{Op}(b)
                         =\operatorname{Op}(a\circ b)
 \tag{O13}
\]
therefore hold on \(\mathcal S\).

Define the extension to the usual bilinear distribution dual by
\(\langle Pu,\phi\rangle=\langle u,\overline{P^\dagger\overline\phi}\rangle\).
O1 and (O11) make the right test function Schwartz and give continuity.
On ordinary functions this is exactly the original integral pairing;
thus no Fourier or duality convention has changed. Transposing (O13)
proves it on \(\mathcal S'\). The same proof supplies finite-seminorm
continuity of the adjoint and bilinear product maps. No general
bijection between all tempered kernels and all continuous operators
is required for these ordinary symbols.

## O4. Compact amplitudes and smooth off-diagonal kernels

For a smooth \(c(x,y,\eta)\), compactly supported in \((x,y)\), with
ordinary order \(m\) in \(\eta\), the distribution
\[
 K_c(x,y)=(2\pi)^{-n}\int e^{i(x-y)\cdot\eta}c(x,y,\eta)\,d\eta
 \tag{O14}
\]
is well defined. Against a compact smooth test function, integrate
by parts in \(y\) with \((1-\Delta_y)^k\); division by
\(\langle\eta\rangle^{2k}\), \(2k>m+n\), makes the integral
absolutely convergent and controlled by finitely many test seminorms.
Derivatives of \(c\) in \(y\) have the same order. A frequency cutoff
can therefore be removed by dominated convergence.

Apply O2 in \((y,\eta)\), with \(x\) as parameter, and restrict:
\[
 p(x,\xi)=\left[Q_{y,\eta}c(x,y,\eta)\right]_{y=x,\eta=\xi},
 \qquad
 p-\sum_{|\alpha|<N}
       \frac{\partial_\eta^\alpha D_y^\alpha c(x,x,\xi)}{\alpha!}
                          \in S^{m-N}.
 \tag{O15}
\]
For compact frequency support, Fourier inversion in \(x-y\)
identifies the left symbol with (O4), so its operator kernel is
(O14). For general amplitudes use frequency cutoffs as in O3:
the amplitudes are bounded in their original estimates, (O15)
converges locally with all derivatives and stays bounded in \(S^m\),
and testing the kernels in the absolutely convergent regularization
above gives the same distributional limit. This proves both kernel
identity and every remainder estimate.

For a left symbol \(p\), its kernel is smooth off \(x=y\).
On a compact set with \(|x-y|\geq\delta>0\), repeatedly use
\[
 e^{i(x-y)\cdot\xi}
   =|x-y|^{-2k}(-\Delta_\xi)^k e^{i(x-y)\cdot\xi}.
 \tag{O16}
\]
Moving the derivatives onto the symbol lowers its order by \(2k\).
After any prescribed number of \(x,y\) derivatives, choose \(k\)
large enough to make the integral absolutely convergent. Coefficients
and their derivatives are uniformly bounded on the separated compact
set, so dominated convergence proves all derivatives there. A symbol
in every negative order has a smooth kernel on every compact set,
by the same argument without division by \(|x-y|\).

## O5. Proper operators and the actual local representation

Work in a Euclidean open set. An ordinary pseudodifferential kernel
is smooth off the diagonal and, near each diagonal base point, has
a local symbol representation (O14), of order \(m\), modulo a
smooth kernel. A compact restriction of the base variables is
understood before applying O14. This is the local class used here.
It includes each quantized symbol, by O4. Multiplication by smooth
base cutoffs and O15 preserve the class and its order.

A kernel is proper when the inverse image of a compact set under
either coordinate projection of its support is compact. For a
compact output set this confines all relevant input points to a
compact set; reversing the projections gives the analogous output
bound for a compact input set. Choose cutoffs equal to one on
neighborhoods of those compact sets.

For each fixed output cutoff \(\chi\), take such an input cutoff
\(\psi\), and a larger \(\psi_1=1\) near \(\operatorname{supp}\psi\).
The compact kernel \(\chi(x)K(x,y)\psi_1(y)\) has a finite cover
near its diagonal part by local representations. A finite smooth
partition in the base exists by the supplied U001 cutoff construction.
Multiply by a cutoff in the second variable equal to one near
each diagonal base piece. Each resulting local amplitude has compact
support and reduces by O15 to a compact-base symbol of order \(m\).
All omitted pieces are smooth by O16 and have compact support in
both variables. Summing the finite symbol pieces gives \(p\in S^m\)
and a compact smooth kernel \(R\) with
\[
 \chi Pu=\operatorname{Op}(p)(\psi u)+R(\psi u).
 \tag{O17}
\]
Indeed \(\psi_1\psi=\psi\), and proper support makes every discarded
input term vanish near \(\operatorname{supp}\chi\).
This is the representation assumed in the endpoint companion B6.

Here is the distributional meaning of that assertion. The transpose
of each local symbol operator sends compact smooth tests to smooth
functions, by O1–O3 after localization. The smooth remainder has the
same property by differentiation under its integral. Proper support
confines the support of the transposed output to one compact set,
for tests supported in a fixed compact set. Its derivative seminorms
are bounded by finitely many seminorms of the input test function.
Thus it is a continuous map of the compact smooth test spaces.
The usual inductive-limit test topology consequently makes the
transpose-test map continuous on \(\mathcal D\). Its transpose
defines \(P:\mathcal D'\to\mathcal D'\). This also gives strong-dual
continuity: for a bounded test set \(B\), the seminorm of \(Pu\) on
\(B\) is the seminorm of \(u\) on its transpose image; a continuous
linear map takes bounded sets to bounded sets, directly by pulling
back each zero neighborhood in the definition of boundedness.
If \(\psi=1\) near the corresponding input compact, pairing with
each output test shows \(Pu=P(\psi u)\) there. This proves the
cutoff independence and (O17) on distributions. The same argument
gives \(P:C^\infty\to C^\infty\); the reverse proper projection
keeps outputs compact for compactly supported inputs.
It also proves \(\mathcal E'\to\mathcal E'\), where
\(\mathcal E'\) denotes compactly supported distributions.

## O6. Proper products, remainders and the principal symbol

Properness makes composition meaningful on all distributions.
For compact output and input cutoffs \(\phi,\psi\), choose an
intermediate cutoff \(\chi\) equal to one near both supports.
Then
\[
 \phi AB\psi=(\phi A\chi)(\chi B\psi)
                       +\phi A(1-\chi^2)B\psi.
 \tag{O18}
\]
The first term uses the finite local representations of O5 and
the product formula O12. For the second, properness confines the
intermediate variable to a compact set. Where \(1-\chi^2\) is
nonzero, both relevant external variables are separated from it;
O16 makes both kernels smooth there. Their compact integral and
every derivative are therefore smooth. Smooth remainders in the
first term also remain smooth: one operator acts on a compact smooth
kernel in one variable, and its O1 bounds, with any finite parameter
derivatives, justify differentiation. Transposition treats the other
order. Smooth proper kernels consequently form a two-sided ideal.

For completeness, the support of \(AB\) is contained in the composed
support relation. To see absence of support at an external pair
outside that relation, properness confines all possible intermediate
points near that pair to a compact set. Each intermediate point
misses one of the two closed supports; finite subcovering and a
smooth partition split the pairing into terms in which one factor
vanishes. This proves the assertion first on tests and then by
transpose on distributions. The composed relation is closed:
for convergent external pairs, properness confines the intermediate
points to a compact set, so a subsequence converges into both closed
supports. Both its projections are proper by the same two successive
compactness bounds. Thus \(AB\) is proper.

The \(N=1\) formula in O12 gives principal symbol \(ab\) modulo
\(S^{m+m'-1}\), in the displayed matrix order. For scalars the
leading products commute; the \(N=2\) formula gives
\[
 \sigma_{m+m'-1}([A,B])=\frac1i
       \sum_j(\partial_{\xi_j}a\,\partial_{x_j}b
                    -\partial_{x_j}a\,\partial_{\xi_j}b)
       \pmod{S^{m+m'-2}} .
 \tag{O19}
\]
For matrices the order \(m+m'\) term is \(ab-ba\).
In particular, if an order-one matrix symbol vanishes on a specified
frequency graph modulo \(S^0\), its commutator with an order-zero
matrix symbol still has order at most one and vanishes there modulo
\(S^0\). The derivative and lower-order terms are of order zero.
No order-zero matrix-commutator assertion is made.

## Free human comparison

[Nicolas Lerner's author-hosted PSEUDO.2005.pdf](https://webusers.imj-prg.fr/~nicolas.lerner/PSEUDO.2005.pdf),
Section 1.2, especially (1.2.2) and (1.2.8), gives the quantization
and composition formulas with its \(2\pi\) Fourier convention.
Its confinement and symbolic-calculus Sections 3.2–4.1 are the
free comparison for the retained multiplier route. All used proofs
and the conversion of conventions are supplied above and in the
linked programme companions. No human-source expression is copied.
