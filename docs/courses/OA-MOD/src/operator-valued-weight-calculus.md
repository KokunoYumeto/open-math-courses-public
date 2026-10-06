# Finite calculus and composition of operator-valued weights

## Conventions, extended positives and finite calculus

### 1. Conventions and finite ideals

Let \(N\subseteq M\) be von Neumann algebras with the same identity unless a corner is displayed. Positive functionals are elements of \(N_*^+\), arbitrary scalar sums are suprema of finite subsums, and inner products are linear in the first variable. We use \([0,\infty]\) with \(0\cdot\infty=0\).

For a weight \(\varphi\) on \(M\), set

\[
 \mathfrak N_\varphi=\{x\in M:\varphi(x^*x)<\infty\},\qquad
 \mathfrak M_\varphi=\operatorname{span}_{\mathbb C}\{y^*x:x,y\in\mathfrak N_\varphi\}.
\]

The first set is a left ideal. On \(\mathfrak M_\varphi\), the unique linear extension is fixed by

\[
 \varphi(y^*x)=\langle\Lambda_\varphi(x),\Lambda_\varphi(y)\rangle.
 \tag{1}
\]

The GNS map may have a nonzero null space for a nonfaithful weight. Semifiniteness means ultraweak density of \(\mathfrak M_\varphi\). Normality means preservation of arbitrary bounded increasing positive-net suprema; the equivalent lower-semicontinuity and dominated-functional descriptions are understood through the normal-weight characterization.

### 2. The extended positive cone

Define \(\widehat N_+\) to be the additive, nonnegative homogeneous, norm-lower-semicontinuous maps

\[
 h:N_*^+\to[0,\infty],\qquad h(0)=0,
\]

ordered pointwise. A bounded \(a\in N_+\) is embedded as
\(\widehat a(\omega)=\omega(a)\). For \(a\in N\), define
\(\omega_a(x)=\omega(a^*xa)\). Then

\[
 (a^*ha)(\omega)=h(\omega_a).
 \tag{2}
\]

Addition, nonnegative scaling, and increasing suprema are all evaluated pointwise.

The spectral-form provider gives every \(h\in\widehat N_+\) as an affiliated positive self-adjoint operator \(A\) on a projection corner \(eH\), together with an infinite part off \(eH\). Bounded cutoffs \(h_r\) increase pointwise to \(h\), and

\[
\begin{aligned}
 h(\omega)&=\sup_r\omega(h_r),\\
 \widehat\varphi(h)&=\sup_r\varphi(h_r).
\end{aligned}
 \tag{3}
\]

for any normal weight \(\varphi\) on \(N\). Equivalently,

\[
 \widehat\varphi(h)=
 \sup\{h(\omega):\omega\in N_*^+,\ \omega\leq\varphi\}.
 \tag{4}
\]

These formulas include infinity and do not require the finite form domain to be dense in the ambient representation. Thus an extended positive cannot be silently replaced by an everywhere-densely-defined operator.

### 3. Definition and finite calculus for operator valued weights

An operator valued weight (OVW) from \(M\) to \(N\) is a map

\[
 T:M_+\longrightarrow\widehat N_+
\]

which is additive and nonnegative homogeneous. For \(x\in M_+\) and
\(n\in N\), it satisfies

\[
 T(n^*xn)=n^*T(x)n.
 \tag{5}
\]

The covariance uses extended-positive conjugation. It does not assume \(T(1)\) is bounded or finite.

The normality condition is

\[
 T(x)=\sup_iT(x_i)\quad\text{if }0\leq x_i\uparrow x,
 \tag{6}
\]

in \(\widehat N_+\). Equivalently, every scalar composite

\[
 (\omega\circ T)(x)=T(x)(\omega),\qquad\omega\in N_*^+,
 \tag{7}
\]

is a normal weight on \(M\). One direction follows by evaluation of (6); the other follows because positive normal functionals separate extended positives. This is the correct topology-free meaning of normality.

Define the finite ideals

\[
\begin{aligned}
 \mathfrak N_T
 &=\{x\in M:T(x^*x)\in N_+\},\\
 \mathfrak M_T
 &=\operatorname{span}_{\mathbb C}
   \{y^*x:x,y\in\mathfrak N_T\}.
\end{aligned}
 \tag{8}
\]

First observe that \(\mathfrak N_T\) is a linear left ideal and a
right \(N\)-module. Linearity uses
\((x+y)^*(x+y)\leq2x^*x+2y^*y\).
For \(m\in M\), \(x\in\mathfrak N_T\), and \(n\in N\), left and right
multiplication give, respectively,

\[
 T((mx)^*(mx))\leq\|m\|^2T(x^*x),
 \tag{9}
\]

\[
 T((xn)^*xn)=n^*T(x^*x)n.
 \tag{10}
\]

An extended positive dominated by a bounded positive is itself bounded,
by the spectral description in CW-02. These estimates therefore give
the stated domain properties.

Here is a construction of the linear extension that does not assume it
in the positivity argument. Let
\(F_T=\{a\in M_+:T(a)\in N_+\}\).
It is a hereditary additive cone. If \(a,b,c,d\in F_T\) and
\(a-b=c-d\), then \(a+d=c+b\), and finite additivity gives
\(T(a)-T(b)=T(c)-T(d)\) in \(N_{\rm sa}\).
Thus \(T\) extends uniquely and real linearly to
\(F_T-F_T\), and complex linearly to its complex span.

This complex span is exactly \(\mathfrak M_T\). Indeed, if
\(a\in F_T\), then \(a^{1/2}\in\mathfrak N_T\) and
\(a=(a^{1/2})^*a^{1/2}\). Conversely, for
\(x,y\in\mathfrak N_T\), linearity of the left ideal and the
polarization identity, with \(z_k=x+i^ky\),

\[
y^*x=\frac14\sum_{k=0}^3i^kz_k^*z_k
\tag{10c}
\]

put \(y^*x\) in the complex span of \(F_T\). If
\(z=a-b\geq0\) with \(a,b\in F_T\), then
\(T(z)+T(b)=T(a)\) in the extended cone. Hence \(T(z)\) is bounded,
belongs to \(F_T\), and equals \(T(a)-T(b)\). This proves

\[
F_T=\mathfrak M_T\cap M_+
\]

and positivity of the extension without subtracting infinite values.
Every use of \(T(z)\) for \(z\in\mathfrak M_T\) means this unique
extension.

Polarizing the OVW covariance first in the algebra variable and then
in the multiplier gives, for \(a,b\in N\) and
\(z\in\mathfrak M_T\), the bounded bimodule identity

\[
 T(azb)=aT(z)b.
 \tag{11}
\]

To check the second polarization explicitly, for positive
\(z\in F_T\) compare \(T((u+tv)^*z(u+tv))\) with
\((u+tv)^*T(z)(u+tv)\) at \(t=1,-1,i,-i\).
This yields \(T(u^*zv)=u^*T(z)v\).
Complex linearity extends it to every \(z\in\mathfrak M_T\).

For \(x_1,\ldots,x_r\in\mathfrak N_T\) and \(c_1,\ldots,c_r\in N\),
put \(z=\sum_i x_ic_i\). The extension and (11) give

\[
\begin{aligned}
 \sum_{i,j}c_i^*T(x_i^*x_j)c_j
 &=T(z^*z)\\
 &\geq0.
\end{aligned}
 \tag{10a}
\]

The matrix-column criterion for positivity in \(M_r(N)\) now proves
\([T(x_i^*x_j)]\geq0\).
In particular the two-by-two matrix criterion gives

\[
\begin{aligned}
 \|T(y^*x)\|^2
 &\leq\|T(x^*x)\|\\
 &\quad\cdot\|T(y^*y)\|.
\end{aligned}
 \tag{10b}
\]

For completeness, add \(\varepsilon1\) to the first diagonal of the
positive two-by-two matrix and take its Schur complement. This gives
\(B^*(A+\varepsilon1)^{-1}B\leq C\) with
\(A=T(y^*y)\), \(B=T(y^*x)\), \(C=T(x^*x)\).
Since \((A+\varepsilon1)^{-1}\geq(\|A\|+\varepsilon)^{-1}1\),
taking norms and then \(\varepsilon\downarrow0\) proves (10b).
These arguments contain no subtraction of infinite values.

If \(T(1)=1\), then \(\mathfrak N_T=M\): for every \(x\in M\),

\[
T(x^*x)\leq\lVert x\rVert^2T(1)=\lVert x\rVert^2 1.
\]

Thus the linear extension is defined on all of \(M\). For \(a\in N_+\),
covariance applied to \(1\) and \(a^{1/2}\) gives \(T(a)=a\);
linearity gives \(T|_N=\operatorname{id}_N\). The extension is a positive
\(N\)-bimodule projection. A positive unital map has norm one when
\(N\ne0\), so this recovers the norm-one projection clause. In the
zero-algebra case the unique map has norm zero.

The OVW is semifinite when \(\mathfrak N_T\) is ultraweakly dense in
\(M\). This is equivalent to ultraweak density of \(\mathfrak M_T\).
To see the equivalence directly, direct \(F_T\) by positive order and put

\[
u_a=a(1+a)^{-1}\qquad(a\in F_T).
\]

The \(u_a\) increase strongly to a projection \(e\), the join of the
support projections of the elements of \(F_T\). The same cutoff argument
as in WS-02 gives

\[
\begin{aligned}
\overline{\mathfrak N_T}^{\,\mathrm{uw}}&=Me,\\
\overline{\mathfrak M_T}^{\,\mathrm{uw}}&=eMe.
\end{aligned}
\tag{11a}
\]

For clarity, \(x\in\mathfrak N_T\) satisfies \(x=xe\); conversely
\(xu_a\in\mathfrak N_T\) and \(xu_a\to xe\) strongly. Likewise
\(u_a z u_a\in\mathfrak M_T\) and tends strongly to \(eze\).
Thus either density condition is equivalent to \(e=1\).

The OVW is faithful when, for \(x\in M_+\),

\[
 T(x)=0\text{ in }\widehat N_+
 \quad\Longrightarrow\quad x=0.
 \tag{12}
\]

Equivalently, \(T(x^*x)\ne0\) for every nonzero \(x\in M\): apply one
condition to \(x^*x\), and the other to \(x=a^{1/2}\).
“N.s.f.” means all three properties. The zero OVW is semifinite on every algebra (its finite ideal is all of \(M\)), but faithful only on the zero algebra; a nonfaithful OVW can nevertheless be semifinite.

## Normal extension to the extended cone

For \(P\subseteq N\subseteq M\), let \(T:M_+\to\widehat N_+\) and
\(S:N_+\to\widehat P_+\) be normal OVWs. The scalar map
\(q_\alpha(y)=S(y)(\alpha)\), \(\alpha\in P_*^+\), is a normal weight on
\(N\), including when it takes infinity. It is not automatically a bounded
functional, so a putative preadjoint \(S_*\alpha\in N_*^+\) cannot define
the extension.

**Extension theorem.** There is a unique additive, nonnegatively homogeneous
 map preserving increasing suprema
\(\widehat S:\widehat N_+\to\widehat P_+\) that agrees with \(S\).
For \(h\in\widehat N_+\),

\[
\begin{aligned}
 \widehat S(h)(\alpha)&=\widehat{q_\alpha}(h),\\
 \widehat S(h)&=\sup_r S(h_r).
\end{aligned}
 \tag{22a}
\]

where the \(h_r\in N_+\) are the bounded spectral cutoffs of CW-02.
More generally the second identity holds for every increasing net of
bounded positive elements with extended-positive supremum \(h\); the
net need not have a common finite operator-norm bound.

**Proof.** CW-03 applies to the arbitrary normal scalar weight \(q_\alpha\).
It gives \(\widehat{q_\alpha}(h)=\sup_r q_\alpha(h_r)\).
Thus the function of \(\alpha\) on the right is the pointwise supremum
of the increasing extended positives \(S(h_r)\), and belongs to
\(\widehat P_+\): additivity and homogeneity commute with a directed
supremum, and a supremum of lower-semicontinuous functions is lower
semicontinuous. CW-03 proves independence of the approximants, agreement
with \(S\), additivity, scaling and preservation of increasing suprema
after evaluation at every \(\alpha\). Those evaluations separate the
cone. Uniqueness follows by applying preservation of suprema to \(h_r\).

For \(p\in P\), \(p^*h_rp\uparrow p^*hp\) pointwise, because for each
normal positive functional \(\omega\) its value is \(h_r(\omega_p)\).
Consequently covariance of \(S\) on bounded positives and preservation
of suprema imply

\[
 \widehat S(p^*hp)=p^*\widehat S(h)p.
 \tag{22b}
\]

This proof uses the exact scalar-extension theorem CW-03; it does not
assume directedness of all finite positive elements. \(\square\)

## The full range of the extended map

**Full range of the extended map.** If \(T:M_+\to\widehat N_+\) is
faithful, normal and semifinite, then \(D=T(\mathfrak M_T)\) is an
ultraweakly dense two-sided *-ideal of \(N\). Its canonical extension
\(\widehat T:\widehat M_+\to\widehat N_+\) from (22a), with the algebras
renamed, is onto. The assertion concerns the extended cone; it does not
say that every extended positive has a bounded preimage in \(M_+\).

**Proof.** The finite-domain bimodule identity (11) makes \(D\) a
two-sided *-ideal. Its ultraweak closure has the form \(zN\) for a central
projection \(z\in N\). For \(x\in\mathfrak N_T\), the element
\(T(x^*x)\) lies in \(D\subseteq zN\). Put \(y=x(1-z)\).
Covariance gives

\[
\begin{aligned}
 T(y^*y)
 &=(1-z)T(x^*x)(1-z)\\
 &=0.
\end{aligned}
 \tag{22c}
\]

Faithfulness implies \(x(1-z)=0\). Semifiniteness makes
\(\mathfrak M_T\), hence \(\mathfrak N_T\), ultraweakly dense in \(M\):
each positive finite-value element \(a\) belongs to \(\mathfrak N_T\)
because \(a^2\leq\|a\|a\), and \(\mathfrak M_T\) is their complex span.
Right multiplication by \(1-z\) is ultraweakly continuous, so (22c)
applied to the dense ideal forces \(1-z=0\).

Every \(b\in D_+\) has a **positive** finite-value lift. Choose a
self-adjoint \(h\in\mathfrak M_T\) with \(T(h)=b\), and write
\(h=a-c\) with \(a,c\in F_T\); this is possible by the construction
of the real extension in Section 3. Then \(b\leq T(a)\). The bounded
positive-operator factorization lemma gives a contraction \(s\in N\)
with \(b=sT(a)s^*\). By (5), \(s a s^*\in F_T\) and
\(T(s a s^*)=b\). This step needs no claim that \(|h|\) has finite
weight.

To make the maximal-family argument precise, let
\(\mathcal B=D_+\setminus\{0\}\). Order the multiplicity functions
\(m:\mathcal B\to\mathbb N_0\) pointwise, retaining only those for
which every finite sum \(\sum_{b\in F}m(b)b\) is at most \(1\).
For each \(b\ne0\), admissibility bounds \(m(b)\) by
\(\|b\|^{-1}\), so the pointwise supremum of a chain remains
integer-valued. Every finite sum for this supremum is controlled by
one member of the chain. Zorn's lemma therefore gives a maximal
admissible \(m\). Let \(r=1-\sum_{b\in\mathcal B}m(b)b\in N_+\),
where the sum is the bounded strong supremum. If \(r\ne0\),
ultraweak density of \(D\) gives
\(d\in D\) with \(r^{1/2}d\ne0\). Then

\[
\begin{aligned}
 c&:=\frac{r^{1/2}dd^*r^{1/2}}
          {\max(1,\|d\|^2)},\\
 0&<c\leq r,\qquad c\in D_+.
\end{aligned}
 \tag{22d}
\]

Increasing the multiplicity of \(c\) by one contradicts maximality.
Thus \(\sum_bm(b)b=1\). Relabel the nonzero copies, with their
multiplicities, as a family \((b_i)_{i\in I}\).

For any \(y\in N_+\), the family
\(y^{1/2}b_i y^{1/2}\in D_+\) sums strongly to \(y\). Choose positive
finite-value lifts \(a_i\in M_+\) of these elements. Their arbitrary
sum \(A=\sum_i\widehat a_i\) exists as the supremum of finite subsums
in \(\widehat M_+\). Preservation of increasing suprema in (22a)
gives \(\widehat T(A)=y\). Finally, for
\(H\in\widehat N_+\), take the increasing bounded spectral cutoffs
\(y_n\uparrow H\) of CW-02, set \(d_1=y_1\) and
\(d_n=y_n-y_{n-1}\in N_+\) for \(n>1\), and lift each \(d_n\) as just
proved to \(A_n\in\widehat M_+\). Then
\(\widehat T(\sum_n A_n)=\sum_n d_n=H\). No countability assumption
on \(N\), \(M\), or the first family \(I\) was used. \(\square\)

## Composition and its finite domains

Define

\[
 U=S\circ T:=\widehat S\circ T:M_+\longrightarrow\widehat P_+.
 \tag{23}
\]

The preceding identities prove additivity, homogeneity and \(P\)-covariance.
If \(x_i\uparrow x\) is a bounded increasing positive net in \(M\),
normality of \(T\), followed by the extension theorem, gives
\(U(x_i)\uparrow U(x)\). Thus \(U\) is a normal OVW.

Write
\(\mathfrak M_S^+=\{h\in N_+:S(h)\in P_+\}\).
For \(x\in\mathfrak N_T\), the exact bounded-intermediate-domain identity is

\[
 x\in\mathfrak N_U
 \quad\Longleftrightarrow\quad
 T(x^*x)\in\mathfrak M_S^+.
 \tag{24}
\]

Thus \(\mathfrak N_U\cap\mathfrak N_T\) is precisely the set of such
\(x\), and in particular it is contained in \(\mathfrak N_U\).
Indeed \(T(x^*x)\) is bounded when \(x\in\mathfrak N_T\), and the
extension then agrees with \(S\). The condition cannot be replaced by
\(T(x^*x)\in\mathfrak N_S\): for \(S\) equal to summation on
\(\ell^\infty(\mathbb N)_+\), \(h_n=1/n\) satisfies
\(S(h^2)<\infty\) while \(S(h)=\infty\).

**Finite contractions.** For any semifinite OVW \(R:A_+\to\widehat B_+\)
on a unital inclusion, there is an increasing net
\(0\leq e_\gamma\leq1\) in \(\mathfrak M_R^+\) converging strongly to
\(1\). In particular \(e_\gamma\in\mathfrak N_R\).

To prove this, let \(F\) run through finite subsets of
\(\mathfrak M_R^+\) and let \(k\) run through the positive integers.
Put \(h_F=\sum_{a\in F}a\) and

\[
 e_{F,k}=k h_F(1+k h_F)^{-1}.
 \tag{25a}
\]

The scalar function \(f(t)=t/(1+t)=1-(1+t)^{-1}\) is operator monotone
on positive bounded operators: the inverse reverses positive order.
Hence \((F,k)\mapsto e_{F,k}\) is increasing for inclusion of \(F\)
and increase of \(k\). Moreover
\(0\leq e_{F,k}\leq1\) and \(e_{F,k}\leq k h_F\). Monotonicity of \(R\)
implies that \(R(e_{F,k})\) is bounded. For fixed \(F\), spectral calculus
gives \(e_{F,k}\uparrow s(h_F)\).

The join of these support projections is \(1\). If their complement
were a nonzero projection \(q\), then \(q a=a q=0\) for every
\(a\in\mathfrak M_R^+\). This would hold on
\(\mathfrak M_R=\operatorname{span}\mathfrak M_R^+\), contradicting its
ultraweak density in \(A\). Thus the increasing contraction net has
supremum \(1\), and bounded monotone convergence gives strong (hence,
for these self-adjoint elements, strong*) convergence.
Since \(e_{F,k}^2\leq e_{F,k}\), each belongs to \(\mathfrak N_R\).

Here the equality
\(\mathfrak M_R=\operatorname{span}\mathfrak M_R^+\) follows from
polarization of \(y^*x\) into finite positive squares. Conversely, if
\(R(a)\) is bounded for \(a\geq0\), then \(a^{1/2}\in\mathfrak N_R\)
and \(a\in\mathfrak M_R\). No norm density is asserted.

**Composition theorem.** If \(S\) and \(T\) are semifinite, then \(U\) is
semifinite. If \(S\) and \(T\) are faithful, then \(U\) is faithful.
In particular composition preserves n.s.f. OVWs, for arbitrary
von Neumann algebras.

For the first assertion choose the preceding nets \(e_\delta\) for \(T\)
and \(u_\gamma\) for \(S\), and put \(z_{\delta,\gamma}=e_\delta u_\gamma\).
Covariance of \(T\) gives

\[
\begin{aligned}
 T(z_{\delta,\gamma}^*z_{\delta,\gamma})
 &=u_\gamma T(e_\delta^2)u_\gamma\\
 &\leq\|T(e_\delta^2)\|u_\gamma^2.
\end{aligned}
 \tag{25b}
\]

Both sides are bounded positives in \(N\). Since \(S(u_\gamma^2)\)
is bounded, applying \(S\) proves \(z_{\delta,\gamma}\in\mathfrak N_U\).
These are contractions, and the product net converges strong* to \(1\).
For example,

\[
 \|(e_\delta u_\gamma-1)\xi\|
 \leq\|(u_\gamma-1)\xi\|+\|(e_\delta-1)\xi\|,
\]

and the adjoints satisfy the reversed version of the same estimate.
For every \(m\in M\),
\(z_{\delta,\gamma}^*m z_{\delta,\gamma}\in\mathfrak M_U\), by the
left-ideal property of \(\mathfrak N_U\). Bounded strong* multiplication
therefore yields ultraweak convergence of these elements to \(m\).
This proves semifiniteness directly.

If \(S\) is faithful and \(\widehat S(h)=0\), then
\(0\leq S(h_r)\leq\widehat S(h)=0\) for the spectral cutoffs.
Faithfulness gives \(h_r=0\) for all \(r\), hence \(h=0\).
If also \(T\) is faithful, \(U(x)=0\) implies \(T(x)=0\) and then \(x=0\).
This argument includes the zero-algebra cases. \(\square\)

## The scalar semifiniteness detector

**A scalar test for semifiniteness.** Let \(T:M_+\to\widehat N_+\)
be normal and let \(\nu\) be a faithful normal weight on \(N\).
If \(\nu\circ T\) is semifinite, then \(T\) is semifinite. When
\(\nu\) is also semifinite, the converse follows from the composition
theorem above. Thus an n.s.f. scalar reference weight detects
semifiniteness of a normal OVW in either direction.

For the nontrivial direction, take
\(x\in\mathfrak M_{\nu\circ T}^+\). Its extended value
\(H=T(x)\) has finite \(\widehat\nu(H)\). In the spectral
description (3), faithfulness of \(\nu\) excludes any nonzero
infinite projection of \(H\); otherwise the increasing truncations
on that projection would make \(\widehat\nu(H)=\infty\).
Consequently the bounded spectral projections
\(e_r=1_{[0,r]}(H)\in N\) increase strongly to \(1\).
Covariance gives

\[
\begin{aligned}
 T(e_r x e_r)&=e_r H e_r\in N_+,\\
 e_r x e_r&\longrightarrow x
 \quad\text{strongly}.
\end{aligned}
 \tag{25c}
\]

Thus \(x\) is an ultraweak limit of positive elements of
\(\mathfrak M_T\). Since
\(\mathfrak M_{\nu\circ T}^+\) linearly spans the ultraweakly dense
finite linear domain of the semifinite scalar weight, \(\mathfrak M_T\) is
ultraweakly dense in \(M\). \(\square\)

**Source and open clauses.** The human antecedents are Takesaki, *Theory of Operator Algebras II*, IX.4.12–4.17(i–ii), printed pp.221–223/PDF pp.241–243, and IX.4.21(i), printed pp.227–228/PDF pp.247–248. OVW-01 proves the exact finite-ideal, module, linear-extension, norm-one projection, semifiniteness, faithfulness, and normality clauses of IX.4.12–4.14. OVW-02 and OVW-04 prove the normal extension and n.s.f. composition assertions of IX.4.15–4.16. IX.4.18 existence/covariance and IX.4.21(ii–iii) uniqueness/modular restriction require separate source and proof review; IX.4.22–4.25 retain their separately registered duality and index consequences.
