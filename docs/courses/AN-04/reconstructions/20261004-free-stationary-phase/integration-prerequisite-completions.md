# Mixed derivatives and the compact-interval integral

Private prerequisite companion. This is an attributed adaptation and extension
of Jiří Lebl, *Basic Analysis*, version 6.3,
[freely accessible author edition](https://www.jirka.org/ra/), under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
The source sections actually read for these arguments are §§5.1–5.3, 7.5,
8.6 and 9.1. Complete earlier programme proofs are retained and bound in
`integration-proof-chain.json`; this companion supplies their used omissions
and the integral Taylor formula needed by the Morse reduction.

The earlier topology and differential chains, including the ordered complete
real-field axioms, finite-dimensional norms, derivative rules, mean-value
theorem and smooth inverse theorem, remain in force. This chapter concerns
bounded-interval Riemann integration. It does not claim the general improper
or Lebesgue integration, multidimensional substitution or exponential
contracts needed elsewhere in the full stationary-phase lesson.

## P11. Higher derivatives and Hessian symmetry

### P11.1. Equivalence of the two definitions of \(C^r\)

The earlier companion defines \(C^r\) recursively by requiring the total
derivative to be \(C^{r-1}\). Lebl §8.6 instead requires every ordered
partial derivative through order \(r\) to exist and be continuous.
These definitions agree for maps between finite-dimensional real spaces.

First, a map \(f=(f_1,\ldots,f_m)\) is differentiable exactly when all
its components are differentiable. If \(Df(p)=A\), applying a coordinate
projection to its remainder gives the component derivative, since a
coordinate's absolute value is at most the vector norm. Conversely assemble
the component derivatives into a matrix \(A\). If \(r_j(h)\) is the
\(j\)th component remainder, then
\[
 \frac{|f(p+h)-f(p)-Ah|}{|h|}
 \leq\sqrt m\max_j\frac{|r_j(h)|}{|h|}\longrightarrow0.
 \tag{P11.1}
\]
The finite maximum tends to zero by taking the minimum of the component
thresholds. Empty coordinate blocks give the unique zero map. The same
coordinate inequalities characterize continuity. By induction on \(r\),
they characterize recursive \(C^r\) regularity as well, because the
derivative matrices consist of finitely many component derivatives.

For \(r=1\), the equivalence with continuous partials is the complete
Proposition 8.4.6, including P10.3's omitted base case. Suppose the equivalence
holds at order \(r-1\). If \(f\) is recursively \(C^r\), every entry
of \(Df\) is \(C^{r-1}\). Those entries are the first partials by
Proposition 8.3.9, so the induction hypothesis supplies all their ordered
partials through order \(r-1\), continuously. This gives all ordered
partials of \(f\) through order \(r\).

Conversely, if those ordered partials exist continuously, Proposition 8.4.6
makes \(f\) a \(C^1\) map. Each first partial has continuous ordered
partials through order \(r-1\), so is recursively \(C^{r-1}\) by
induction. Assembling the entries shows \(Df\in C^{r-1}\), hence
\(f\in C^r\). This proves the equivalence for every finite order; being
smooth means satisfying it for every order. No commutation of derivatives
was assumed in this argument. \(\square\)

### P11.2. The exact scope of the mixed-partial proof

The programme contains the full double-mean-value proof of Proposition
8.6.2 at `sec_mvhighordders.html#sec_mvhighordders-10`. It compares the same
rectangle difference quotient in both orders. For distinct indices, choose
\(B(p,r)\subset U\) and \(0<s,t<r/3\); all points of the closed
rectangle, including its edges, lie in this ball, since their distance
from \(p\) is at most \(s+t<2r/3\).

The source supplies points \(p_0,p_1\) in that rectangle with
\[
 G(s,t)=\partial_\ell\partial_m f(p_0)
       =\partial_m\partial_\ell f(p_1).
\]
Each point tends to \(p\) because its distance is bounded by \(s+t\).
Given \(\varepsilon>0\), continuity therefore makes both respective
errors from their values at \(p\) less than \(\varepsilon\), once
\(s,t\) are sufficiently small. Subtracting the two equal expressions
for \(G\) gives
\[
 |\partial_\ell\partial_m f(p)-\partial_m\partial_\ell f(p)|
 <2\varepsilon.
\]
If the left side were positive, taking \(\varepsilon\) smaller than
half of it would contradict this bound. Thus it is zero. Equal indices
already give the same expression. This records the boundary and limit
steps in the existing proof without replacing its mean-value argument.
P11.1 verifies that its \(C^2\) hypothesis agrees with the one used here.

For a \(C^k\) function, any two orders of a fixed list of at most
\(k\) differentiations give the same result. To swap two adjacent
operators, first apply the inner operators to obtain a function with at
least two continuous derivatives. Apply the just-proved second-order
identity on its open domain. Any remaining outer derivatives preserve
this equality, because equal functions have equal difference quotients.
Any permutation is a finite sequence of adjacent swaps: successively move
the desired first, second and later entries into position. This proves
the assertion for every order, including repeated indices. In particular
the smooth Hessians in P4 and M1 are symmetric. \(\square\)

## P12. The omitted integral inputs

### P12.1. Suprema and infima used by Darboux sums

All sets in this paragraph are nonempty and bounded when both extrema are
used. If every \(a\in A\) is at most every \(b\in B\), each \(b\)
is an upper bound for \(A\), so \(\sup A\leq b\). Thus \(\sup A\)
is a lower bound for \(B\), and \(\sup A\leq\inf B\).

For two sets, write \(A+B=\{a+b:a\in A,b\in B\}\). The number
\(\sup A+\sup B\) is an upper bound for \(A+B\). By P6.2, for
each \(\varepsilon>0\) choose
\(a>\sup A-\varepsilon/2\) and \(b>\sup B-\varepsilon/2\).
Their sum exceeds \(\sup A+\sup B-\varepsilon\). No smaller upper
bound is therefore possible, proving
\(\sup(A+B)=\sup A+\sup B\). Negating the sets proves
\(\inf(A+B)=\inf A+\inf B\), since
\(\inf(-A)=-\sup A\) and \(\sup(-A)=-\inf A\), directly by
the order definitions.

For \(c>0\), \(c\sup A\) bounds \(cA\) above. Choosing
\(a>\sup A-\varepsilon/c\) proves it is the least such bound.
Thus \(\sup(cA)=c\sup A\); negation proves the corresponding
infimum formula. For \(c=0\), the image set is \(\{0\}\); for
\(c<0\), factor out the minus sign and use the preceding negation
identities. These statements justify the extrema operations used in
Lebl's integral-linearity proof.

If \(A\subset B\) and every \(b\in B\) is at most some \(a\in A\),
then \(\sup A=\sup B\): inclusion gives one inequality, and the second
condition makes every upper bound for \(A\) an upper bound for \(B\).
Reversing order proves the analogous infimum assertion. This supplies the
cofinal-partition step left to an exercise in Lemma 5.2.1.

Finally, for bounded functions \(f\leq g\) on the same nonempty set,
\(\inf f\leq\inf g\) because \(\inf f\) is a lower bound for
all values of \(g\); likewise \(\sup f\leq\sup g\). For functions
on the same set, every value of \(f+g\) lies between
\(\inf f+\inf g\) and \(\sup f+\sup g\). These give inequalities,
without asserting equality when the two extrema require different points.
\(\square\)

### P12.2. Upper refinement and the necessary integrability criterion

Use Lebl's definitions of a partition \(P\), its lower and upper sums
\(L(P,f),U(P,f)\), and the lower and upper Darboux integrals. The complete
lower-refinement proof is Proposition 5.1.7. For its omitted upper half,
each refined interval is contained in its original interval, so its
supremum \(\widetilde M_q\) is at most the original \(M_i\).
Multiplying by positive refined lengths and summing over that original
interval gives
\[
 \sum_{q=k_{i-1}+1}^{k_i}\widetilde M_q\Delta\widetilde x_q
 \leq M_i\sum_{q=k_{i-1}+1}^{k_i}\Delta\widetilde x_q
 =M_i\Delta x_i.
\]
Summing over \(i\) proves \(U(\widetilde P,f)\leq U(P,f)\).
The index \(q\) in the source definition of \(\Delta\widetilde x_q\)
must start at 1, not 0; no undefined \(\widetilde x_{-1}\) is used.

Proposition 5.1.13 proves that arbitrarily small gaps \(U(P,f)-L(P,f)\)
imply Riemann integrability. Conversely suppose the common integral is
\(I\). By the defining supremum and infimum choose partitions \(P_1,P_2\)
with \(L(P_1,f)>I-\varepsilon/2\) and
\(U(P_2,f)<I+\varepsilon/2\). Their union is a finite partition and
refines both, so
\[
 U(P_1\cup P_2,f)-L(P_1\cup P_2,f)<\varepsilon.
\]
This proves the necessary half that will be used below. For any finite
list of integrable functions, take the union of the chosen partitions to
obtain all their small-gap bounds on one common partition. \(\square\)

### P12.3. Negative scalars, addition, restrictions and orientation

The positive-scalar part of Proposition 5.2.4 already has a written proof.
For its negative-scalar exercise, P12.1 gives
\[
 L(P,-f)=-U(P,f),\qquad U(P,-f)=-L(P,f).
\]
Taking the defining extrema gives
\(\underline\int(-f)=-\overline\int f\) and
\(\overline\int(-f)=-\underline\int f\). Thus \(-f\) is integrable
when \(f\) is, with integral \(-\int f\). Combining this with the
proved nonnegative-scalar case gives every real scalar.

For the addition exercise, choose a common partition with the sum of the
two Darboux gaps smaller than \(\varepsilon\), using P12.2. The
pointwise extrema inequalities of P12.1 imply
\[
 L(P,f)+L(P,g)\leq L(P,f+g)\leq U(P,f+g)
 \leq U(P,f)+U(P,g).
\]
Consequently the Darboux gap of \(f+g\) is less than \(\varepsilon\),
so Proposition 5.1.13 proves its integrability. Both \(\int(f+g)\)
and \(\int f+\int g\) lie in the displayed outside interval, whose
length is less than \(\varepsilon\). Their difference is therefore
zero, proving full linearity. Repeated application proves linearity for
any finite sum. The unused general Darboux subadditivity assertion is
not needed in this proof.

For Corollary 5.2.3, let \([c,d]\subset[a,b]\) with \(c<d\).
If \(c>a\), split at \(c\) by Proposition 5.2.2 to obtain integrability
on \([c,b]\); if \(c=a\), it is already known. If \(d<b\), split
that interval at \(d\); if \(d=b\), no second split is needed. This
proves the restriction exercise in all endpoint cases. Define the integral
on a singleton to be 0 and define \(\int_y^x f=-\int_x^y f\) for
\(x<y\). These are orientation conventions, not limits of undefined
partitions.

Within a fixed interval \([a,b]\), put \(J(x)=\int_a^x f\).
Additivity gives \(\int_x^y f=J(y)-J(x)\) when \(x<y\); the
definitions give it when \(x=y\) and \(x>y\). Subtracting these
identities proves
\(\int_x^z f=\int_x^y f+\int_y^z f\) in every order of the three
points. In particular, changing the base point of an antiderivative
integral changes it by a constant, completing Remark 5.3.4. \(\square\)

### P12.4. The norm bound and passing a uniform error through an integral

For \(f:[a,b]\to\mathbb R^m\) with Riemann-integrable components,
define its integral componentwise. Its norm is also integrable. To see
this, on any partition interval the reverse triangle inequality and the
coordinate bound give
\[
 \bigl||f(x)|-|f(y)|\bigr|\leq |f(x)-f(y)|
 \leq\sum_{j=1}^m |f_j(x)-f_j(y)|
 \leq\sum_j(M_{ij}-m_{ij}).
\]
Taking a supremum in \(x\) and an infimum in \(y\), by P12.1, bounds
the oscillation of \(|f|\) by that sum. Therefore its Darboux gap is
at most the sum of the component gaps. A common partition from P12.2
makes this arbitrarily small, proving integrability of \(|f|\).

Write \(I=\int_a^b f\). If \(I\ne0\), let \(v=I/|I|\). Finite
linearity, the Euclidean Cauchy–Schwarz bound and integral monotonicity
(Proposition 5.2.6) give
\[
 |I|=v\cdot I=\int_a^b v\cdot f(t)\,dt
 \leq\int_a^b |f(t)|\,dt.\tag{P12.1}
\]
For \(I=0\) the same inequality follows from nonnegativity of the last
integral. In particular \(|\int_a^b f|\leq(b-a)\sup|f|\).
Complex-valued integrals are the case \(m=2\), using their real and
imaginary components.

If \(f_\lambda\) and \(f\) are integrable and
\(\sup_{[a,b]}|f_\lambda-f|\to0\), the same bound and linearity give
\[
 \left|\int_a^b f_\lambda-\int_a^b f\right|
 \leq(b-a)\sup_{[a,b]}|f_\lambda-f|\longrightarrow0.\tag{P12.2}
\]
This is the precise uniform-error result used in Theorem 9.1.1. It does
not assume that an arbitrary pointwise limit can pass through an integral.
\(\square\)

### P12.5. Endpoint and domain details in the fundamental theorem

The programme supplies the full proofs of both forms of the fundamental
theorem, Theorems 5.3.1 and 5.3.3. In the latter, a derivative at an
endpoint of \([a,b]\) means the appropriate one-sided derivative. At
interior points it is the ordinary two-sided derivative. P12.3 justifies
its signed integral differences when the increment is negative. Its final
non-strict error estimate proves the strict limit definition by starting
with half the requested error. A different integration base point changes
the primitive by a constant, by P12.3, and hence has the same derivative.

In the substitution proof of Theorem 5.3.5, the primitive of a continuous
\(f:[c,d]\to\mathbb R\) may be evaluated at an endpoint of that
interval. To apply the earlier open-domain chain rule without a boundary
assumption, extend \(f\) to the real line by the constant value \(f(c)\)
to the left and \(f(d)\) to the right. This extension is continuous:
away from the junctions the assertion is inherited or constant, and at a
junction the original one-sided continuity and the identical constant
value give the same bound on both sides. If \(c=d\), use the constant
function \(f(c)\) everywhere.

The primitive \(\widetilde F(y)=\int_{g(a)}^y\widetilde f(u)\,du\)
is consequently \(C^1\) on an open interval containing the whole range
of \(g\), by the proved fundamental theorem on each bounded subinterval.
Its derivative is \(\widetilde f\). The open-domain chain rule now
applies to \(\widetilde F\circ g\) at every interior point of
\([a,b]\), including points where \(g\) reaches \(c\) or \(d\).
The source's first-fundamental-theorem argument gives exactly its stated
oriented substitution formula. No monotonicity or injectivity of \(g\)
is required. This is only the one-variable formula; multidimensional
change of variables remains a separate proof obligation. \(\square\)

### P12.6. Integration by parts and the required Taylor formula

For \(u,v\in C^1([a,b])\), the product derivative is continuous.
The product rule and the first fundamental theorem therefore give
\[
 \int_a^b u(t)v'(t)\,dt
 =u(b)v(b)-u(a)v(a)-\int_a^b u'(t)v(t)\,dt.\tag{P12.3}
\]
This follows by integrating \((uv)'=u'v+uv'\) and using linearity;
all integrands are continuous and hence integrable by Lemma 5.2.7.
Vector-valued \(v\) is handled componentwise.

Let \(g\in C^N([0,1];\mathbb R^m)\), \(N\geq1\). Define
\[
 R_N=\frac1{(N-1)!}\int_0^1(1-t)^{N-1}g^{(N)}(t)\,dt.
\]
The first fundamental theorem gives \(R_1=g(1)-g(0)\). For \(N\geq2\),
apply (P12.3) with \(u(t)=(1-t)^{N-1}\) and \(v=g^{(N-1)}\).
The endpoint term at 1 vanishes, and the one at 0 is
\(-g^{(N-1)}(0)\). Since
\(u'=-(N-1)(1-t)^{N-2}\), this gives
\[
 R_N=R_{N-1}-\frac{g^{(N-1)}(0)}{(N-1)!}.
\]
Induction now proves the full integral-remainder identity
\[
 g(1)=\sum_{j=0}^{N-1}\frac{g^{(j)}(0)}{j!}
 +\frac1{(N-1)!}\int_0^1(1-t)^{N-1}g^{(N)}(t)\,dt.\tag{P12.4}
\]
The polynomial derivative used here follows by the product rule applied
to its \(N-1\) equal factors. Applying the fundamental theorem to
\(-(1-t)^N/N\) also gives \(\int_0^1(1-t)^{N-1}\,dt=1/N\).
Thus (P12.1) bounds \(|R_N|\) by \(\sup|g^{(N)}|/N!\).

For M1, take \(g(t)=f(q+tv,u',s)\) and \(N=2\). Repeated chain
rules give \(g'(0)=v\partial_1f(q,u',s)=0\) and
\(g''(t)=v^2\partial_1^2f(q+tv,u',s)\). Formula (P12.4) is precisely
the identity (M1.3), including its factor 2 in the definition of \(A\).
It holds for positive, zero and negative \(v\) on any segment contained
in the chart. No exchange of two integrals is used. \(\square\)

### P12.7. Smooth dependence on all parameters of a compact integral

Let \(U\subset\mathbb R^p\) be open, and suppose that \(f(t,z)\)
and all its ordered \(z\)-partial derivatives through order \(r\)
are continuous on \([a,b]\times U\). Then
\[
 H(z)=\int_a^b f(t,z)\,dt
\]
is \(C^r\) and every such parameter derivative is the integral of the
corresponding derivative of \(f\). The assertion holds for all finite
\(r\), for \(r=\infty\), and for finite-dimensional vector values.

Fix \(z_0\), and choose a closed ball \(K\) centred at \(z_0\) with
positive radius, contained in \(U\). The product \([a,b]\times K\)
is closed and bounded in a Euclidean space, hence compact. To verify
closedness directly, a point outside either factor has a positive-distance
neighbourhood still outside that factor; coordinate projections do not
increase distance. Boundedness follows from the sum of the squared
coordinate bounds. F0-COMP therefore makes each continuous integrand on
this product uniformly continuous.

For \(z\to z_0\), this gives
\(\sup_t|f(t,z)-f(t,z_0)|\to0\). P12.4 proves continuity of \(H\).
For a coordinate increment \(he_j\) sufficiently small to stay in the
interior of \(K\), the one-variable mean-value argument of the existing
Theorem 9.1.1 gives, for each scalar component, a point \(\theta\)
between 0 and \(h\) with
\[
 \frac{f(t,z+he_j)-f(t,z)}h=\partial_j f(t,z+\theta e_j).
\]
Uniform continuity of \(\partial_j f\) makes the difference between
this quotient and \(\partial_j f(t,z)\) tend uniformly in \(t\) to
zero. The intermediate point may depend on \(t\); the uniform bound
does not. By linearity and (P12.2),
\[
 \partial_j H(z)=\int_a^b\partial_j f(t,z)\,dt.
\]
The earlier continuity argument applied to \(\partial_j f\) shows
that this partial derivative is continuous jointly in \(z\). Repeat
with each ordered derivative of \(f\). Finite induction gives every
ordered partial through order \(r\), continuously; P11.1 identifies
this with \(C^r\) regularity. Applying the argument at every finite
order proves the smooth case. Vector values follow componentwise.
When \(p=0\) there are no parameter derivatives; when \(a=b\) every
integral is the zero map. These cases satisfy the same conclusion directly.
\(\square\)

## Use in the Morse reduction

P11 supplies the mixed-partial input in the Schur-complement calculation P4. P12 supplies the precise Taylor and compact-parameter integration inputs in M1. The full earlier inverse/implicit and signature proofs remain unchanged. The global Fourier integrals, exponential identities and multidimensional Jacobian substitutions needed by the analytic module are still separate obligations.
