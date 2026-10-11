# Detecting and determining operator-valued weights

A faithful scalar weight can reveal whether an operator-valued weight is semifinite and can determine every one of its extended-positive outputs. Its modular group also remembers the scalar modular action on the target algebra. The three claims have different proofs: the last requires a mixed analytic graph theorem. Throughout, \(N\subseteq M\) is a unital inclusion of arbitrary von Neumann algebras, and no countability hypothesis is imposed.

## The three assertions and the scalar detector

Write \(\mathcal W(N)\) for normal semifinite weights on \(N\), and \(\mathcal W_0(N)\) for their faithful members. For operator-valued weights, the source uses \(\mathcal W(M,N)\) for all normal operator-valued weights and \(\mathcal W_0(M,N)\) for the faithful normal semifinite ones. In particular, \(S\in\mathcal W(M,N)\) need not be semifinite. Let \(T:M_+\to\widehat N_+\) initially be only normal. Takesaki II IX.4 Lemma 4.21 says:

1. If \(\psi\in\mathcal W_0(N)\) and \(\widehat\psi\circ T\) is semifinite, then \(T\) is semifinite.
2. If \(S\in\mathcal W(M,N)\) and \(\widehat\psi\circ T=\widehat\psi\circ S\) for one \(\psi\in\mathcal W_0(N)\), then \(T=S\), even when \(S\) is neither faithful nor semifinite.
3. If \(T\in\mathcal W_0(M,N)\), then \(\sigma_t^{\widehat\psi\circ T}(n)=\sigma_t^\psi(n)\) for every \(n\in N\), \(t\in\mathbb R\), and \(\psi\in\mathcal W_0(N)\).

Here scalar composition evaluates a normal weight on the **extended** positive \(T(x)\), including its infinite values. For (1), put \(\Phi=\widehat\psi\circ T\). If \(x\in\mathfrak M_\Phi^+\), faithfulness of \(\psi\) forces the infinite projection of \(T(x)\) to vanish. With \(e_r=1_{[0,r]}(T(x))\in N\), covariance gives

\[
\begin{aligned}
T(e_rxe_r)&=e_rT(x)e_r\in N_+,\\
e_rxe_r&\longrightarrow x\quad\text{strongly}.
\end{aligned}
\tag{OR.1}
\]

The finite cone of the semifinite scalar weight \(\Phi\) linearly spans the ultraweakly dense hereditary *-subalgebra \(\mathfrak M_\Phi\) of \(M\). Equation (OR.1) places each of its positive generators in the ultraweak closure of the bounded-output linear domain \(\mathfrak M_T\); hence that domain is ultraweakly dense and \(T\) is semifinite. Neither finite linear domain is asserted to be a two-sided ideal of \(M\). This is the scalar detector with the source quantifiers displayed. The cutdowns need not increase. Conversely, the composition theorem makes \(\widehat\psi\circ T\) semifinite when both \(T\) and \(\psi\) are semifinite. \(\square\)

## Uniqueness from one scalar composite, including infinity

Assume the hypotheses of assertion (2). Set \(\Phi=\widehat\psi\circ T=\widehat\psi\circ S\). This common scalar weight need not be semifinite. The argument uses faithfulness and semifiniteness of \(\psi\), the covariance identities for \(S,T\), and their extended-positive outputs; it requires no semifiniteness or faithfulness assumption on either operator-valued weight.

For every \(x\in M_+\) and \(a\in N\), covariance and the equality of scalar composites give the identity in \([0,\infty]\)

\[
\begin{aligned}
\widehat\psi\bigl(a^*T(x)a\bigr)
&=\Phi(a^*xa)\\
&=\widehat\psi\bigl(a^*S(x)a\bigr).
\end{aligned}
\tag{OR.2}
\]

First suppose \(S(x)=K\in N_+\) and let \(C=\|K\|\). For every \(a\in\mathfrak N_\psi\), (OR.2) yields

\[
\begin{aligned}
\widehat\psi\bigl(a^*T(x)a\bigr)
&\le C\psi(a^*a)\\
&<\infty.
\end{aligned}
\tag{OR.3}
\]

This forces \(H=T(x)\le C1\) as an extended positive. Indeed, if its spectral projection \(q=1_{(C+\varepsilon,\infty]}(H)\) were nonzero, faithfulness and semifiniteness of \(\psi\) would give a nonzero \(a\in\mathfrak N_\psi\) with \(qa=a\). Then the left side of (OR.3) would be at least \((C+\varepsilon)\psi(a^*a)\), a contradiction. The same test excludes a nonzero infinite projection. Now both \(H\) and \(K\) are bounded. Their quadratic forms agree on the dense set \(\Lambda_\psi(\mathfrak N_\psi)\) by (OR.2), so polarization and faithfulness of the GNS representation give \(H=K\). The same reasoning applies whenever \(T(x)\) is bounded.

For arbitrary \(x\in M_+\), write \(K=S(x)\) and \(H=T(x)\) as extended spectral positives in a faithful normal representation of \(N\). Let \(e_r=1_{[0,r]}(K)\) and \(f_r=1_{[0,r]}(H)\), excluding any infinite part. Covariance and the bounded-output case just proved yield

\[
\begin{aligned}
e_rHe_r&=e_rKe_r,\\
f_rHf_r&=f_rKf_r\quad(r>0).
\end{aligned}
\tag{OR.4}
\]

We must use both families: equality on a merely dense set of test vectors need not identify closed unbounded forms. If \(\xi\) has finite \(K\)-energy, spectral calculus gives \(e_r\xi\to\xi\) in the \(K\)-form norm. By (OR.4), each \(e_r\xi\) has finite \(H\)-energy and, for \(s\ge r\), the \(H\)-energy of \((e_s-e_r)\xi\) equals its \(K\)-energy. Closedness of the \(H\)-form therefore puts \(\xi\) in its finite form domain with the same energy. The \(f_r\) argument gives the reverse inclusion and equality. The finite domains, their quadratic forms, and hence their infinite projections coincide. Uniqueness of the closed spectral form gives \(T(x)=S(x)\). Since \(x\) was arbitrary, \(T=S\) on the full positive cone. \(\square\)

## The forward modular graph transfer

Let \(T\in\mathcal W_0(M,N)\) and \(\varphi,\psi\in\mathcal W_0(N)\).
Put \(\Phi=\widehat\varphi\circ T\) and
\(\Psi=\widehat\psi\circ T\). Both are faithful normal semifinite
by OVW04.
The mixed actions are

\[
\begin{aligned}
u_t^N(n)&=[D\psi:D\varphi]_t\,\sigma_t^\varphi(n),\\
u_t^M(x)&=[D\Psi:D\Phi]_t\,\sigma_t^\Phi(x).
\end{aligned}
\tag{OR.5}
\]

These are groups of normal complex-linear isometries, with pointwise
sigma-weakly continuous real orbits, by the cocycle law and the
balanced-weight construction.
They need not preserve products. We prove that their real actions agree
on \(N\), without first assuming that \(u^M\) preserves \(N\).

**The scalar graph and its two bounds.** Take
\((a,b)\in\mathcal G(u_{-i}^N)\). The exact criterion
AG07 gives
\(a\mathfrak N_\varphi^*\subseteq\mathfrak N_\psi^*\),
\(\mathfrak N_\psi b\subseteq\mathfrak N_\varphi\), and
\(\psi(av)=\varphi(vb)\) for
\(v\in\operatorname{span}\mathfrak N_\varphi^*\mathfrak N_\psi\).
The last equality uses finite complex-linear weight values.

Here is also the full positive domination needed below. On \(M_2(N)\)
use \(\Omega(X)=\psi(X_{11})+\varphi(X_{22})\). The matrices
\(A=aE_{12}\), \(B=bE_{12}\) are the endpoints of a bounded modular
strip \(F\) of height one, by AG07. Put \(C=F(-i/2)=cE_{12}\).
HS03, applied
first to \(F\) on its upper half and then to
\(z\mapsto F(\bar z-i)^*\) on its upper half, gives
\(\Omega(AXA^*)\leq\|c\|^2\Omega(X)\) and
\(\Omega(B^*XB)\leq\|c\|^2\Omega(X)\) for every positive matrix \(X\).
Testing respectively \(X=QE_{22}\) and \(X=QE_{11}\) proves

\[
\begin{aligned}
\widehat\psi(aQa^*)&\leq K^2\widehat\varphi(Q),\\
\widehat\varphi(b^*Qb)&\leq L^2\widehat\psi(Q)
\qquad(Q\in\widehat N_+),
\end{aligned}
\tag{OR.6}
\]

with \(K=L=\|c\|\). For extended \(Q\), take its increasing bounded
spectral truncations. Conjugation preserves their extended-positive
supremum, and normal scalar evaluation preserves it by
CW03. This includes infinite
values and an infinite spectral part; the convention is \(0\cdot\infty=0\).
Applying (OR.6) to \(T(q)\) and using bimodularity gives

\[
\begin{aligned}
\Psi(aqa^*)&\leq K^2\Phi(q),\\
\Phi(b^*qb)&\leq L^2\Psi(q)
\qquad(q\in M_+).
\end{aligned}
\tag{OR.7}
\]

In particular right multiplication by \(a^*\) sends
\(\mathfrak N_\Phi\) into \(\mathfrak N_\Psi\), with GNS norm bound
\(K\); right multiplication by \(b\) sends \(\mathfrak N_\Psi\)
into \(\mathfrak N_\Phi\), with bound \(L\).

**The finite matrix and its oriented mixed ideal.** Write
\(\dot T:\mathfrak M_T\to N\) for the finite linear extension in
OVW01.
For \(y,z\in\mathfrak N_T\), the bounded matrix

\[
R=\begin{pmatrix}
T(y^*y)&\dot T(y^*z)\\
\dot T(z^*y)&T(z^*z)
\end{pmatrix}
\]

is positive. Indeed, its quadratic form on a column \((d_1,d_2)\)
over \(N\) is \(T((yd_1+zd_2)^*(yd_1+zd_2))\geq0\), using the
right \(N\)-module and bimodule laws. To recall why these columns
detect positivity, a negative spectral projection
\(p=1_{(-\infty,-\varepsilon)}(R)\ne0\) would satisfy
\(pRp\leq-\varepsilon p\). Some \(p_{jj}\) is nonzero; its column
\(d_i=p_{ij}\) would give
\(\sum_{i,k}d_i^*R_{ik}d_k=(pRp)_{jj}\leq-\varepsilon p_{jj}\),
contradicting positivity. Thus no amplified unbounded OVW is needed.

Now assume also \(y\in\mathfrak N_\Phi\) and
\(z\in\mathfrak N_\Psi\). For the balanced weight
\(\theta(H)=\varphi(H_{11})+\psi(H_{22})\) on \(M_2(N)_+\),

\[
\theta(R)=\Phi(y^*y)+\Psi(z^*z)<\infty.
\]

Let \(W=R^{1/2}\in M_2(N)\). Since
\(\theta(W^*W)<\infty\), its first-column entries \(w_{j1}\) are
in \(\mathfrak N_\varphi\), and its second-column entries
\(w_{j2}\) are in \(\mathfrak N_\psi\). Therefore

\[
\dot T(y^*z)=R_{12}
=\sum_{j=1}^2w_{j1}^*w_{j2}
\in\operatorname{span}\mathfrak N_\varphi^*\mathfrak N_\psi.
\]

The order of the two scalar ideals has been obtained from the columns,
not inferred from an unordered intersection of domains.

**The finite scalar overlap.** If \(\omega\) is a normal weight on
\(N\), the equality
\((\widehat\omega\circ T)(h)=\omega(\dot T(h))\) is finite on
every positive \(h\in\mathfrak M_T\cap\mathfrak M_{\widehat\omega\circ T}\).
By linear extension it holds on the span of these positive elements.
For \(v,w\in\mathfrak N_T\cap\mathfrak N_{\widehat\omega\circ T}\),
polarization of the four squares \((v+i^kw)^*(v+i^kw)\) puts
\(v^*w\) in this span. Thus the equality applies to this product,
and \(\dot T(v^*w)\) is in \(\mathfrak M_\omega\).
It has not been asserted on arbitrary elements of \(\mathfrak M_T\).

For the finite-output \(y,z\) just considered, (OR.7) and the right
module law put \(ya^*\) in \(\mathfrak N_T\cap\mathfrak N_\Psi\)
and \(zb\) in \(\mathfrak N_T\cap\mathfrak N_\Phi\).
Consequently the overlap applies to
\(ay^*z=(ya^*)^*z\) for \(\omega=\psi\), and to
\(y^*zb=y^*(zb)\) for \(\omega=\varphi\).
The scalar graph identity, applied to the verified mixed element
\(\dot T(y^*z)\), gives

\[
\begin{aligned}
\Psi(ay^*z)
&=\psi\bigl(a\dot T(y^*z)\bigr)\\
&=\varphi\bigl(\dot T(y^*z)b\bigr)
=\Phi(y^*zb).
\end{aligned}
\tag{OR.8}
\]

**Right spectral cuts and the full graph.** For arbitrary
\(y\in\mathfrak N_\Phi\), put \(H=T(y^*y)\).
Its scalar value \(\widehat\varphi(H)\) is finite. Faithfulness of
\(\varphi\) excludes a nonzero infinite spectral projection of \(H\),
as in OVW05.
Hence \(e_r=1_{[0,r]}(H)\) increases strongly to \(1\). For
\(y_r=ye_r\), covariance gives
\(T(y_r^*y_r)=e_rHe_r\leq r1\), and

\[
\begin{aligned}
\|\Lambda_\Phi(y-y_r)\|^2
&=\widehat\varphi\bigl((1-e_r)H(1-e_r)\bigr)\\
&\longrightarrow0.
\end{aligned}
\]

For this convergence, the two spectral pieces add to \(H\), whose
scalar value is finite, and normality gives
\(\widehat\varphi(e_rHe_r)\uparrow\widehat\varphi(H)\).
There is no subtraction of infinite values. Thus
\(y_r\in\mathfrak N_T\cap\mathfrak N_\Phi\).
Independently cut \(T(z^*z)\) for \(z\in\mathfrak N_\Psi\), obtaining
\(z_s=zf_s\in\mathfrak N_T\cap\mathfrak N_\Psi\) and convergence
in its \(\Psi\)-GNS norm. These are right cuts; the operators
\(y_r,z_s\) are not claimed to increase.

The bounds (OR.7) give convergence also of
\(\Lambda_\Psi(y_ra^*)\) to \(\Lambda_\Psi(ya^*)\) and
\(\Lambda_\Phi(z_sb)\) to \(\Lambda_\Phi(zb)\).
Apply (OR.8) to \(y_r,z_s\) and pass to the two Hilbert-space pairings

\[
\begin{aligned}
\Psi(ay_r^*z_s)
&=\langle\Lambda_\Psi(z_s),\Lambda_\Psi(y_ra^*)\rangle,\\
\Phi(y_r^*z_sb)
&=\langle\Lambda_\Phi(z_sb),\Lambda_\Phi(y_r)\rangle.
\end{aligned}
\]

Their limits prove (OR.8) for every
\(y\in\mathfrak N_\Phi\), \(z\in\mathfrak N_\Psi\), and linearity
covers their mixed product span. Together with the two ideal inclusions
from (OR.7), AG07 now gives

\[
\mathcal G(u_{-i}^N)\subseteq\mathcal G(u_{-i}^M).
\tag{OR.9}
\]

The comparison theorem proved in OR04 applies to these explicitly
normal isometric groups and yields \(u_t^M(n)=u_t^N(n)\) for every
\(n\in N\). Setting \(\psi=\varphi\) proves the modular restriction

\[
\sigma_t^{\widehat\varphi\circ T}(n)=\sigma_t^\varphi(n)
\qquad(n\in N,\ t\in\mathbb R).
\tag{OR.10}
\]

For general \(\psi\), evaluating at \(n=1\) also proves
\([D\Psi:D\Phi]_t=[D\psi:D\varphi]_t\in N\).
The operator-valued weight was given throughout; no compatibility-to-existence
theorem or countable-sum converse has entered the proof. \(\square\)

## Comparing generators across an inclusion

**Theorem.** Let \(N\subseteq M\) be a unital inclusion of von Neumann
algebras. Let \(v_t^N\) and \(v_t^M\) be groups of normal
complex-linear isometries on their respective algebras, with pointwise
sigma-weakly continuous real orbits. If their closed-strip generators satisfy
\(\mathcal G(v_{-i}^N)\subseteq\mathcal G(v_{-i}^M)\) in
\(M\oplus M\), then \(v_t^M(n)=v_t^N(n)\) for every \(n\in N\)
and real \(t\). Invariance of \(N\) under \(v^M\) is a conclusion.

**Proof.** We use the explicit kernel construction of
AG02, the
scalar uniqueness lemma AG03,
and the strip translation and gluing arguments in
AG01.
Those arguments require normality of the real maps, which is a hypothesis
here. The classification of general surjective isometries is not needed.

In particular AG02 supplies, for every \(n\in N\), a bounded net
\(n_r\to n\) sigma-weakly in \(N\), each having an entire orbit
\(F^N\) with

\[
\|F^N(t+iy)\|\leq C e^{c|y|}
\qquad(t,y\in\mathbb R)
\]

for suitable \(C>0,c\geq0\) depending on the approximant. The construction
integrates \((\sin rz/(rz))^2\) against the real orbit and divides by
its positive real integral; its horizontal bound and approximate-identity
property are proved in AG02, without a Fourier-distribution theorem.

Fix one such approximant \(x\), and put \(x_k=F^N(-ik)\) for
\(k\in\mathbb Z\). Translation preserves this entire core. Therefore
\((x_k,x_{k+1})\) belongs to both negative-imaginary graphs.
Reversing each pair supplies the positive-imaginary graph as well:
translation of a strip with endpoints \((a,b)\) gives the inverse strip
with endpoints \((b,a)\), as proved in AG01. The strips for \(v^M\)
can thus be glued upward and downward through every integer height.
Their common edges agree by real translation. Testing with a normal
functional and subdividing triangles along the finitely many common edges
gives Morera's criterion on each larger strip. Local boundedness and the
predual Cauchy argument of AG01 give an entire \(M\)-valued orbit
\(F^M\) for \(x\), with \(F^M(-ik)=x_k\).

On the strip between integer heights \(j,j+1\), its two edge norms
are bounded by \(Ce^{c|j|}\) and \(Ce^{c|j+1|}\), since the real maps
of \(v^M\) are isometries. Each glued strip is bounded before applying
the scalar maximum principle. Consequently

\[
\|F^M(t+iy)\|\leq Ce^c e^{c|y|}
\qquad(t,y\in\mathbb R).
\]

For \(\rho\in M_*\), the entire scalar function
\(f(z)=\rho(F^M(z)-F^N(z))\) has this horizontal exponential bound
and vanishes at every imaginary integer, in particular at all positive
ones. AG03 proves \(f=0\) by its finite Blaschke-product argument.
The predual separates \(M\), so the two real orbits of \(x\) agree.

Finally \(n_r\to n\) also sigma-weakly in \(M\), because the
inclusion of a von Neumann subalgebra is normal and every normal
functional on \(M\) restricts normally to \(N\). Normality of the
fixed maps \(v_t^M,v_t^N\) lets the equality pass to \(n\).
This proves the theorem for arbitrary cardinality, without assuming that
the ambient real action already preserves the smaller algebra. \(\square\)

The human antecedent for the three assertions of this lesson is
M. Takesaki, *Theory of Operator Algebras II*, IX.4 Lemma 4.21,
printed pages 227–230. Its scalar analytic inputs are VIII.3 Lemma 3.18,
Proposition 3.24 and Theorem 3.25, proved here through HS03, AG01–03
and AG07, with the inclusion comparison and finite-output transfer
spelled out above. The mixed ideals and all positive inequalities retain
their full semifinite scope, including infinite positive values.
