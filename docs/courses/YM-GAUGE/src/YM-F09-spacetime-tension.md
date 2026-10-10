# Space-time tension at every spatial order

The [fixed-time estimates](../classical-fixed-time-estimates.html)
control the original heat extension at each physical time.
The wave equation needs additional estimates with the actual
space-time norm. This chapter constructs them from the electric
curvature, proves every coefficient bound, and then proceeds by
an explicit induction through all ordinary spatial derivatives.

The prerequisites are the [tension equation and null structure](../classical-tension-null-structure.html),
[curl-free and backward heat bounds](../classical-curlfree-backward-heat.html),
and [potential wave estimates](../classical-potential-wave.html).
The original fields, coordinates, bracket conventions and full
ordered derivative tuples are retained. The physical interval
\(I\) is compact and nondegenerate, the speed is \(c>0\), and
the heat interval is \([0,S]\). The current regular solution
has the actual Yang–Mills and Gauss data, so \(w_i(0)=W(0)=0\).

The human-source comparison is Sung-Jin Oh,
[*Gauge choice for the Yang–Mills equations using the Yang–Mills heat
flow and local well-posedness in \(H^1\)*, arXiv:1210.1558v2](https://arxiv.org/abs/1210.1558v2),
the parabolic tension estimates. Its original author TeX was read
in the exact ranges recorded in the provenance. The proof below
is independent exposition with full receiving formulas and
constants. It makes no novelty claim and does not assume the
later finite physical wave closure.

## 1. Retain both spatial sums and prove their cancellation

The full forcing already displayed in NX.7 is


\[
Q_i=2\sum_{k,j}[F_{kj},D_kF_{ij}]
   +2\sum_{k,j}[F_{kj},D_jF_{ik}]
   -2c^{-2}\sum_j[E_j,D_iE_j-2D_jE_i].
\tag{ST.1}
\]


The second spatial sum, with its two dummy labels exchanged,
is exactly
\(\sum_{k,j}[F_{jk},D_kF_{ij}]
=-\sum_{k,j}[F_{kj},D_kF_{ij}]\).
This is a bijection of all nine ordered pairs; the three diagonal
pairs are zero because \(F_{kk}=0\). Thus their complete sum is
zero. Neither individual sum has been discarded or presumed zero.
The exact receiving identity and its full tuple bound are


\[
Q_i=-2c^{-2}\sum_j[E_j,D_iE_j-2D_jE_i],
\qquad
|Q|\le12c^{-2}|E||D_xE|.
\tag{ST.2}
\]


For the first contraction, the bracket norm bound and
Cauchy–Schwarz give
\(\big|(\sum_j[E_j,D_iE_j])_i\big|
 \le2|E||D_xE|\).
The second contraction obeys the same bound after retaining all
output indices. Equation factor two and the additional coefficient
two yield \(2c^{-2}(2+4)=12c^{-2}\). In particular the original
electric metric factor remains present.

The source's expression
\(2[F_{0j},D^jF_{0i}+D_0F^j{}_i]\)
agrees through the physical coordinate map and
\(D_tF_{ij}=D_iE_j-D_jE_i\). The same cancellation mechanism was
already used for the temporal component in HT.60. NX.7's prior
termwise upper bound remains valid; ST.2 uses more of the exact
structure of its displayed expression.

## 2. Full temporal-connection bounds in spatial L4

Let \(\overline M_h\) be the actual time suprema from CF.15.
Evaluate the existing nonnegative polynomial \(b_q\) at


\[
\begin{aligned}
\mathscr J_q
 &=3^{q/2}b_q\bigl((S^{1/4}\overline M_h)_{0\le h<q};
                         (K_l)_{0\le l\le q}\bigr),\\
\mathscr R_q
 &=C_S^{3/4}\mathscr J_q^{1/4}\mathscr J_{q+1}^{3/4}.
\end{aligned}\tag{ST.3}
\]


Here \(K_l\) are exactly HT.23's constants for \(W\).
The exact reverse expansion HP.24, as in HT.39, gives for every
ordinary word of length \(q\) its polynomial bound. A term with
\(j\) potential leaves has residual factor \(s^{j/4}\), bounded
above by the original \(S^{j/4}\). There are \(3^q\) ordered
words and one temporal output. Therefore


\[
\|\partial_x^{(q)}W(t,s)\|_2
 \le cd^2\mathscr J_qs^{-q/2-1/4},\qquad
\|\partial_x^{(q)}W(t,s)\|_4
 \le cd^2\mathscr R_qs^{-q/2-5/8}.
\tag{ST.4}
\]


For the second inequality apply
\(\|u\|_4\le\|u\|_2^{1/4}(C_S\|\nabla u\|_2)^{3/4}\)
to the full ordered tuple. The exact exponent is
\((q/2+1/4)/4+3(q/2+3/4)/4=q/2+5/8\).
This proves ST.4 from existing coefficients, without inserting
a new unknown temporal norm.

Differentiate the actual identity \(a_t(s)=-\int_s^S W(r)dr\).
Every integral over a positive closed heat interval is legitimate
for the current regular field. Define, with no zero denominator
for any nonnegative integer \(q\),


\[
\begin{aligned}
\gamma_q&=q/2-3/8,\\
\mathfrak h_q(s,S)&=\int_s^S r^{-q/2-5/8}\,dr
   =\frac{s^{-\gamma_q}-S^{-\gamma_q}}{\gamma_q},\\
\|\partial_x^{(q)}a_t(s)\|_{L^\infty_tL^4_x}
 &\le cd^2\mathscr R_q\mathfrak h_q(s,S).
\end{aligned}\tag{ST.5}
\]


In particular
\(\mathfrak h_0=(8/3)(S^{3/8}-s^{3/8})\),
\(\mathfrak h_1=8(s^{-1/8}-S^{-1/8})\), and
\(\mathfrak h_2=(8/5)(s^{-5/8}-S^{-5/8})\).
Both original endpoints and all coefficients remain.

For \(\beta>\max(\gamma_q,0)\) define the exact scalar norms


\[
\mathfrak H_q^p(\beta)
=\|s^\beta\mathfrak h_q(s,S)\|_{L^p((0,S],ds/s)},
\qquad p=2,\infty.
\tag{ST.6}
\]


Expansion of the full square and integration of its three terms,
each integrable under the stated inequality, gives


\[
\begin{aligned}
(\mathfrak H_q^2(\beta))^2
 &=\frac{S^{2(\beta-\gamma_q)}}{\gamma_q^2}
 \left(\frac1{2\beta-2\gamma_q}
       -\frac2{2\beta-\gamma_q}+\frac1{2\beta}\right),\\
\mathfrak H_q^\infty(\beta)
 &=\frac{S^{\beta-\gamma_q}}{\beta}
    \left(\frac{\beta-\gamma_q}{\beta}\right)^{
                                  (\beta-\gamma_q)/\gamma_q}.
\end{aligned}\tag{ST.7}
\]


For the second line, differentiate the unchanged function
\(s^\beta(s^{-\gamma_q}-S^{-\gamma_q})/\gamma_q\).
Its single interior critical point is
\(s=S((\beta-\gamma_q)/\beta)^{1/\gamma_q}\).
It lies strictly between zero and \(S\) for either sign of
\(\gamma_q\). The derivative is positive before it and negative
after it, and both endpoint limits are zero. Substitution proves
the asserted maximum. No norm or physical domain has been replaced.

## 3. Both actual electric input norms

For \(k=3/2,5/2\), put \(\beta_k=(k-1)/2\). The full backward
identity used in PW.7, followed by CF.20, proves


\[
\begin{aligned}
\overline P_k^2
 &=\frac{S^{\beta_k}}{\sqrt{2\beta_k}}W_k(S)
                       +\frac1{\beta_k}\mathcal F_k^2,\\
\overline P_k^\infty
 &=S^{\beta_k}W_k(S)
                       +\frac1{\sqrt{2\beta_k}}\mathcal F_k^2,\\
\|s^{\beta_k}W_k(s)\|_{L^p(ds/s)}
 &\le\overline P_k^p,\qquad p=2,\infty .
\end{aligned}\tag{ST.8}
\]


The superscripts are integrability exponents. Both lines retain the
actual endpoint \(W_k(S)\) and differentiated wave forcing in
\(\mathcal F_k^2\). In particular this adds the supremum version to
PW.8, rather than replacing a forcing norm by an energy norm.
The annular approximation in PW Section 1 establishes the required
wave bounds on the actual derivative-regular potential.

Let \(d_c=\sqrt2(2\pi c)^{-1/4}\), \(H_0=C_MC_S\sqrt{K_1K_2}\),
and keep \(U_0\) and \(\mathcal A\) from CF.15 and CF.28.
The exact electric curvature and its spatial covariant derivative
are


\[
\begin{aligned}
E_i={}&\partial_ta_i-\partial_i a_t+[a_t,a_i],\\
D_jE_i={}&\partial_j\partial_ta_i-\partial_j\partial_i a_t
 +[\partial_j a_t,a_i]+[a_t,\partial_ja_i]
 +[a_j,\partial_ta_i]-[a_j,\partial_i a_t]
 +[a_j,[a_t,a_i]].
\end{aligned}\tag{ST.9}
\]


Thus every term of the original physical expression, including its
seven derivative terms, remains identifiable. Define actual norms


\[
\mathbb E_0^p=\|s^{1/4}\|E(s)\|_{L^4_{t,x}}\|_{L^p(ds/s)},
\qquad
\mathbb E_1^p=\|s^{3/4}\|D_xE(s)\|_{L^4_{t,x}}\|_{L^p(ds/s)}.
\tag{ST.10}
\]


Hölder, the full derivative wave bound HW.33 and ST.4–ST.8 give


\[
\begin{aligned}
\mathbb E_0^p\le e_0^p:={}&
 cd_c\overline P_{3/2}^p
 +|I|^{1/4}cd^2\mathscr R_1\mathfrak H_1^p(1/4)\\
&+2\mathcal A\,cd^2\mathscr R_0\mathfrak H_0^p(1/8),\\
\mathbb E_1^p\le e_1^p:={}&
 cd_c\overline P_{5/2}^p
 +|I|^{1/4}cd^2\mathscr R_2\mathfrak H_2^p(3/4)\\
&+4\mathcal A\,cd^2\mathscr R_1\mathfrak H_1^p(5/8)\\
&+\frac{4cd^2H_0d_c\sqrt S}{e}\overline P_{3/2}^p
 +2U_0cd_cS^{1/4}\overline P_{3/2}^p\\
&+4|I|^{1/4}U_0^2cd^2\mathscr R_0\mathfrak H_0^p(1/4).
\end{aligned}\tag{ST.11}
\]


Here is a term-by-term proof. The first terms in the two expressions
ST.9 are bounded by \(cd_cW_{3/2}\) and \(cd_cW_{5/2}\),
respectively. The factor \(c\) comes from the temporal component of
\(\partial_c=(c^{-1}\partial_t,\partial_x)\), not from a changed
time coordinate. The pure derivatives of \(a_t\) use ST.5 and
the physical factor \(|I|^{1/4}\).

For the bracket in \(E\), use
\(\|a(s)\|_{L^4_tL^\infty_x}\le\mathcal A s^{-1/8}\) and the
\(L^\infty_tL^4_x\) bound for \(a_t\). Its remaining heat weight is
\(s^{1/8}\). In \(D_xE\), the third and sixth terms each have bound
\(2\mathcal A\,cd^2\mathscr R_1s^{-1/8}\mathfrak h_1\);
both appear in the coefficient four, with remaining weight \(s^{5/8}\).
The fourth term uses
\(\|a_t\|_\infty\le cd^2H_0\log(S/s)\) and
\(\|\partial_xa\|_{L^4_{t,x}}\le d_cW_{3/2}\).
Its excess heat weight is \(\sqrt{s}\log(S/s)\), whose exact
supremum is \(2\sqrt S/e\) by HT.43. The fifth term uses
\(\|a\|_\infty\le U_0s^{-1/4}\), leaving \(s^{1/4}\) after the
weighted \(W_{3/2}\) input. The final double bracket costs four:
use two copies of this \(L^\infty\) bound and the \(L^4_{t,x}\)
bound for \(a_t\); the remaining weight is \(s^{1/4}\).
Every displayed \((q,\beta)\) satisfies ST.6's strict inequality.
Minkowski completes the proof for each \(p=2,\infty\), with the
same order of physical and heat norms throughout.

## 4. The complete electric forcing has three controlled heat norms

The pointwise bound ST.2 and space-time Hölder imply, on the
unchanged heat interval,


\[
\begin{aligned}
\int_0^S\|Q(s)\|_{L^2_{t,x}}\,ds
 &\le q_1:=12c^{-2}e_0^2e_1^2,\\
\|s\|Q(s)\|_{L^2_{t,x}}\|_{L^2(ds/s)}
 &\le q_2:=12c^{-2}\min(e_0^\infty e_1^2,e_0^2e_1^\infty),\\
\sup_s s\|Q(s)\|_{L^2_{t,x}}
 &\le q_\infty:=12c^{-2}e_0^\infty e_1^\infty.
\end{aligned}\tag{ST.12}
\]


For the first line retain \(ds=s\,ds/s\) and the exact product
\(s=s^{1/4}s^{3/4}\); Cauchy–Schwarz uses the two squared heat
norms. For the next two lines use the same factor identity and
the indicated supremum norms. No individual unweighted electric
integral has been asserted finite.

## 5. Covariant energy gives the first two space-time quantities

Keep the original equation
\(\partial_sw=\sum_jD_jD_jw+\mathcal R_Fw+Q\), where
\((\mathcal R_Fw)_i=2\sum_j[F_{ij},w_j]\).
The exact bracket and full spatial curvature norm give


\[
\|\mathcal R_F(s)\|_{L^\infty_{t,x}\to L^\infty_{t,x}}
 \le a_0(s):=4\sqrt2 H_Fd\,s^{-3/4},\qquad
\Phi(s):=\int_0^s a_0(r)dr=16\sqrt2 H_Fd\,s^{1/4}.
\tag{ST.13}
\]


This is an upper coefficient for the actual multiplication operator;
the field and its equation are unchanged. Spatial covariant
integration by parts, then integration in the original physical
measure \(dt\), gives


\[
\frac12\frac d{ds}\|w\|_{L^2_{t,x}}^2+\|D_xw\|_{L^2_{t,x}}^2
 =\operatorname{Re}\langle w,\mathcal R_Fw+Q\rangle_{t,x}.
\tag{ST.14}
\]


No time integration by parts is involved. Spatial cutoff errors
vanish by the regular \(L^2\) fields and their derivatives.

To integrate this identity exactly, set \(z(s)=e^{-\Phi(s)}w(s)\).
This is an explicitly invertible scalar comparison map, with
\(w=e^\Phi z\) and \(D_xw=e^\Phi D_xz\); the original field is
recovered in each bound below. Its equation has multiplication
operator \(\mathcal R_F-a_0I\). Hence


\[
\frac12(\|z\|_2^2)' +\|D_xz\|_2^2
 \le \|z\|_2\,e^{-\Phi}\|Q\|_2,\qquad z(0)=0.
\tag{ST.15}
\]


Regularizing the norm by \((\|z\|_2^2+\epsilon^2)^{1/2}\),
integrating its differential inequality, and letting \(\epsilon\)
decrease to zero proves
\(\|z(s)\|_2\le\int_0^s e^{-\Phi(r)}\|Q(r)\|_2dr\le q_1\).
Integrating ST.15 and keeping its nonnegative endpoint term then
gives \(\int_0^S\|D_xz\|_2^2ds\le q_1^2\).
Consequently, with explicit quantities


\[
\begin{aligned}
A_0&:=e^{\Phi(S)}q_1,\\
A_D&:=e^{\Phi(S)}q_1,\\
A_\partial&:=A_D+2\sqrt2\,U_0S^{1/4}A_0,
\end{aligned}
\qquad
\begin{aligned}
\sup_s\|w(s)\|_{L^2_{t,x}}&\le A_0,\\
\left(\int_0^S\|D_xw(s)\|_{L^2_{t,x}}^2ds\right)^{1/2}&\le A_D,\\
\left(\int_0^S\|\partial_xw(s)\|_{L^2_{t,x}}^2ds\right)^{1/2}&\le A_\partial .
\end{aligned}\tag{ST.16}
\]


The last inequality uses the exact
\(\partial_jw=D_jw-[a_j,w]\),
the full tuple bracket bound \(2|a||w|\), and
\(\int_0^S s^{-1/2}ds=2\sqrt S\). It does not exchange a time
supremum and a heat integral. These are actual \(L^2_{t,x}\) norms.

## 6. The full ordinary forcing and the second spatial level

Expanding every spatial covariant derivative yields


\[
\begin{aligned}
N_w:=(\partial_s-\Delta)w
={}&2\sum_j[a_j,\partial_jw]
 +[\sum_j\partial_ja_j,w]
 +\sum_j[a_j,[a_j,w]]
 +\mathcal R_Fw+Q.
\end{aligned}\tag{ST.17}
\]


Use \(\|\partial_xa\|_\infty\le U_1s^{-3/4}\) from CF.15.
Each displayed term now has its own finite weighted bound:


\[
\begin{aligned}
\|s\|N_w(s)\|_{L^2_{t,x}}\|_{L^2(ds/s)}
 \le N_2:={}&4U_0S^{1/4}A_\partial\\
 &+(2\sqrt6\,U_1S^{1/4}
       +4U_0^2\sqrt S+8H_FdS^{1/4})A_0+q_2.
\end{aligned}\tag{ST.18}
\]


For the first term write \(s^{3/4}\|\partial w\|
=s^{1/4}(s^{1/2}\|\partial w\|)\).
The derivative coefficient in the second costs \(\sqrt3\)
and a bracket factor two; the exact norm
\(\|s^{1/4}\|_{L^2(ds/s)}=\sqrt2 S^{1/4}\) yields \(2\sqrt6\).
The double bracket costs four and
\(\|s^{1/2}\|_{L^2(ds/s)}=\sqrt S\).
The curvature term costs \(4\sqrt2 H_Fd\), multiplied by
the preceding \(s^{1/4}\) norm, yielding eight.
The last term is ST.12. Thus no linear or nonlinear forcing
term was omitted.

Multiply the original equation
\(\partial_sw-\Delta w=N_w\) by \(-s\Delta w\) in the original
space-time \(L^2\) inner product. Spatial integration by parts gives


\[
\frac12\frac d{ds}\bigl(s\|\partial_xw\|_2^2\bigr)
   +s\|\Delta w\|_2^2
 =\frac12\|\partial_xw\|_2^2-s\operatorname{Re}\langle\Delta w,N_w\rangle .
\tag{ST.19}
\]


The original heat endpoint term at zero vanishes: the field is
regular through zero and \(w(0)=0\). One may first integrate
from a positive endpoint and then take its actual limit.
Young's inequality, with both coefficients \(1/2\), gives


\[
\begin{aligned}
\sup_{0<s\le S}\sqrt{s}\|\partial_xw(s)\|_{L^2_{t,x}}
 &\le A_1:=\sqrt{A_\partial^2+N_2^2},\\
\left(\int_0^S s\|\partial_x^{(2)}w(s)\|_{L^2_{t,x}}^2ds\right)^{1/2}
 &\le A_1 .
\end{aligned}\tag{ST.20}
\]


For the second line, Plancherel proves the exact full tuple identity
\(\sum_{i,j}\|\partial_i\partial_jw\|_2^2
=\|\Delta w\|_2^2\), because
\(\sum_{i,j}\xi_i^2\xi_j^2=(\sum_i\xi_i^2)^2\).
This is a proved map between the two original expressions,
not a dropped mixed derivative.

Finally the same five terms of ST.17, now using the first line
of ST.20, give


\[
\begin{aligned}
\sup_{0<s\le S}s\|N_w(s)\|_{L^2_{t,x}}
 \le N_\infty:={}&4U_0S^{1/4}A_1\\
 &+(2\sqrt3\,U_1S^{1/4}
       +4U_0^2\sqrt S+4\sqrt2 H_FdS^{1/4})A_0+q_\infty.
\end{aligned}\tag{ST.21}
\]


All powers are the same as in ST.18; the scalar heat norms are
replaced by their exact suprema \(S^{1/4}\) or \(\sqrt S\).
The physical factors \(c\), \(c^{-2}\), \(|I|^{1/4}\), the finite
heat endpoint, and every endpoint wave norm remain in ST.3–ST.21.

## 7. Every ordinary electric derivative

The same calculation has a finite all-order form. Preserve the
previous low-order bounds and define
\(U_j=3^{(j+1)/2}\overline M_j\), so
\(\|\partial_x^{(j)}a(s)\|_\infty\le U_js^{-j/2-1/4}\).
For every half-integer \(k\ge3/2\), extend ST.8 using its exact
\(\beta_k=(k-1)/2>0\); PW.7 and CF.20 prove those same formulas.
Write \(\eta_0^p=e_0^p\), and for each integer \(q\ge1\) set


\[
\begin{aligned}
\eta_q^p:={}&cd_c\overline P_{q+3/2}^p
 +|I|^{1/4}cd^2\mathscr R_{q+1}
                         \mathfrak H_{q+1}^p(q/2+1/4)\\
&+\frac{4cd^2H_0d_c\sqrt S}{e}\overline P_{q+1/2}^p\\
&+2|I|^{1/4}cd^2
  \sum_{l=1}^q{q\choose l}U_{q-l}\mathscr R_l
                                     \mathfrak H_l^p(l/2).
\end{aligned}\tag{ST.22}
\]


Then


\[
\|s^{q/2+1/4}
       \|\partial_x^{(q)}E(s)\|_{L^4_{t,x}}\|_{L^p(ds/s)}
 \le\eta_q^p,\qquad q\ge0,\quad p=2,\infty.
\tag{ST.23}
\]


To prove this, differentiate the first line of ST.9 by every
ordered \(q\)-word. The first two terms are bounded by
\(cd_cW_{q+3/2}\) and ST.5 with \(q+1\).
For the bracket retain every Leibniz subset \(J\) of the word:
\([\partial_Ja_t,\partial_{J^c}a_i]\).
The empty subset uses \(a_t\) in \(L^\infty_{t,x}\) and
\(\partial^{(q)}a\) in \(L^4_{t,x}\), bounded by
\(d_cW_{q+1/2}\). Its excess power is again
\(\sqrt{s}\log(S/s)\).
For a nonempty subset of size \(l\), use ST.5 for its
\(a_t\) factor and the full \(U_{q-l}\) bound for its
potential factor. The remaining power is exactly \(s^{l/2}\).
There are \({q\choose l}\) such subsets. For a fixed subset the
reordering of the two derivative tuples is bijective; the
full contraction is bounded by their full norms. This proves
the sum in ST.22 with bracket constant two and no uncounted
component factor. Its scalar norms are finite since
\(l/2>\gamma_l\) and \(l>0\).
The \(q=0\) case uses ST.11's actual \(L^4_tL^\infty_x\)
potential input, avoiding a divergent constant heat bound.

For the covariant derivative retain the exact rule

\[
\partial_I(D_jE_i)
 =\partial_I\partial_jE_i+
   \sum_{J\subset I}[\partial_Ja_j,\partial_{I\setminus J}E_i].
\]

Here a subset means positions in the ordered word, preserving
the order in each factor. Put \(\delta_0^p=e_1^p\) from ST.11,
and, for \(q\ge1\),


\[
\begin{aligned}
\delta_q^p
 &=\eta_{q+1}^p+
      2S^{1/4}\sum_{l=0}^q{q\choose l}U_l\eta_{q-l}^p,\\
\|s^{q/2+3/4}
       \|\partial_x^{(q)}D_xE(s)\|_{L^4_{t,x}}\|_{L^p(ds/s)}
 &\le\delta_q^p .
\end{aligned}\tag{ST.24}
\]


The first term has precisely the weight in ST.23 for \(q+1\).
In a bracket, the two original weights total
\(l/2+1/4+(q-l)/2+1/4=q/2+1/2\), leaving \(s^{1/4}\).
Thus ST.24 follows for both stated heat exponents. The same formula
also gives a second valid bound at \(q=0\); the sharper termwise
bound ST.11 is retained in the definition.

Differentiating the full electric expression ST.2 now proves


\[
\begin{aligned}
Q_q^1&:=12c^{-2}\sum_{l=0}^q{q\choose l}\eta_l^2\delta_{q-l}^2,\\
Q_q^2&:=12c^{-2}\sum_{l=0}^q{q\choose l}
    \min(\eta_l^\infty\delta_{q-l}^2,
                         \eta_l^2\delta_{q-l}^\infty),\\
Q_q^\infty&:=12c^{-2}\sum_{l=0}^q{q\choose l}
                         \eta_l^\infty\delta_{q-l}^\infty,\\
\left\|s^{q/2+1}\|\partial_x^{(q)}Q(s)\|_{L^2_{t,x}}
                           \right\|_{L^p(ds/s)}
 &\le Q_q^p,\qquad p=1,2,\infty .
\end{aligned}\tag{ST.25}
\]


Each subset has weight
\(l/2+1/4+(q-l)/2+3/4=q/2+1\).
Apply space-time Hölder and then heat Hölder with the exact
exponents indicated. The minimum is legitimate term by term,
since each of its alternatives bounds that same term.
At \(q=0\) these are exactly the three constants in ST.12.

## 8. A triangular recurrence for every tension derivative

Retain the full ordinary spatial curvature tuple. Define


\[
\begin{aligned}
H_l^F&=C_MC_S\sqrt{R_{l+1}R_{l+2}},\\
C_l^F&=\sqrt2\,3^{l/2}d\,
 b_l\bigl((S^{1/4}\overline M_h)_{0\le h<l};
                           (H_r^F)_{0\le r\le l}\bigr).
\end{aligned}\tag{ST.26}
\]


The covariant Morrey bound, exact reverse expansion and full
ordered spatial curvature metric give
\(\|(\partial_x^{(l)}F_{ij})_{i,j}\|_\infty
 \le C_l^F s^{-l/2-3/4}\).
The factor \(\sqrt2\) retains the six ordered spatial pairs
against the three unordered curvature pairs; the temporal
curvature components remain in the upper covariant norm.
In particular \(C_0^F=\sqrt2 H_Fd\).
All these constants have already defined finite inputs.

Set \(A_0\) as in ST.16 and \(B_1=A_\partial\). We will construct
constants for the original full ordinary derivative tuples by


\[
\sup_s s^{n/2}\|\partial_x^{(n)}w(s)\|_{L^2_{t,x}}\le A_n,\qquad
\left(\int_0^S s^{n-1}
       \|\partial_x^{(n)}w(s)\|_{L^2_{t,x}}^2ds\right)^{1/2}
 \le B_n\quad(n\ge1).
\tag{ST.27}
\]


Suppose \(A_0,\ldots,A_q\) and \(B_1,\ldots,B_{q+1}\) have
already been constructed. They exist initially for \(q=0\)
by ST.16. Define the finite number


\[
\begin{aligned}
N_q^2:={}&
4S^{1/4}\sum_{l=0}^q{q\choose l}U_lB_{q-l+1}\\
&+2\sqrt6 S^{1/4}
          \sum_{l=0}^q{q\choose l}U_{l+1}A_{q-l}\\
&+4\sqrt S
 \sum_{\substack{r,h,n\ge0\\r+h+n=q}}
        \frac{q!}{r!\,h!\,n!}U_rU_hA_n\\
&+4\sqrt2 S^{1/4}
          \sum_{l=0}^q{q\choose l}C_l^F A_{q-l}
 +Q_q^2 .
\end{aligned}\tag{ST.28}
\]


The five lines estimate the five original terms of ST.17 after
every ordinary derivative is distributed. For the first term,
the remaining weight after the potential bound is
\(s^{1/4}s^{(q-l+1)/2}\); use \(B_{q-l+1}\).
For the second and fourth terms it is
\(s^{1/4}s^{(q-l)/2}\); use \(A_{q-l}\) and the exact scalar
heat norm \(\sqrt2 S^{1/4}\).
The divergence contracts three entries and retains its factor
\(\sqrt3\). For the double bracket use the three disjoint
ordered subsets, with multiplicity \(q!/(r!h!n!)\).
Their combined potential exponent is \((r+h)/2+1/2\);
the remaining scalar norm is \(\|s^{1/2}\|_2=\sqrt S\).
The bracket factors remain respectively four, two, four and
four as in ST.17. Thus, with full word/output norms,


\[
\left\|s^{q/2+1}
     \|\partial_x^{(q)}N_w(s)\|_{L^2_{t,x}}\right\|_{L^2(ds/s)}
 \le N_q^2 .
\tag{ST.29}
\]


No \(A_{q+1}\) or \(B_{q+2}\) occurs in ST.28. This fact
makes the following construction an actual finite induction.

Apply the ordinary heat equation to every ordered \(q\)-word
of \(w\), multiply it by minus \(s^{q+1}\) times its Laplacian,
and sum all entries. Exactly as in ST.19, integration and
Young's inequality give


\[
\begin{aligned}
&s^{q+1}\|\partial_x^{(q+1)}w(s)\|_2^2
 +\int_0^s r^{q+1}\|\partial_x^{(q+2)}w(r)\|_2^2dr\\
&\quad\le(q+1)\int_0^s r^q\|\partial_x^{(q+1)}w(r)\|_2^2dr
 +\int_0^s r^{q+1}\|\partial_x^{(q)}N_w(r)\|_2^2dr.
\end{aligned}\tag{ST.30}
\]


The full Fourier tuple identity used in ST.20 applies to each
additional word and then to their sum. The original lower
endpoint term vanishes by regularity through zero; no initial
term with nonzero value is suppressed. Therefore define


\[
A_{q+1}=B_{q+2}
 =\sqrt{(q+1)B_{q+1}^2+(N_q^2)^2}.
\tag{ST.31}
\]


This proves the next two inequalities ST.27. The expression
\((N_q^2)^2\) is the square of the named heat-exponent-two
constant, as distinguished from its superscript label.
At \(q=0\), ST.28 and ST.31 reproduce ST.18 and ST.20 exactly.
Induction proves ST.27 at every finite order.

After this step, the supremum version of all five original
forcing terms is also available:


\[
\begin{aligned}
N_q^\infty:={}&
4S^{1/4}\sum_{l=0}^q{q\choose l}U_lA_{q-l+1}\\
&+2\sqrt3 S^{1/4}\sum_{l=0}^q{q\choose l}U_{l+1}A_{q-l}\\
&+4\sqrt S
 \sum_{\substack{r,h,n\ge0\\r+h+n=q}}
         \frac{q!}{r!\,h!\,n!}U_rU_hA_n\\
&+4S^{1/4}\sum_{l=0}^q{q\choose l}C_l^FA_{q-l}
 +Q_q^\infty,\\
\sup_s s^{q/2+1}\|\partial_x^{(q)}N_w(s)\|_{L^2_{t,x}}
 &\le N_q^\infty .
\end{aligned}\tag{ST.32}
\]


This is the same complete product calculation as ST.28,
using the exact scalar suprema and the newly constructed
\(A_{q+1}\). No loop in the induction is introduced.

For the exact comparison with the source's physical coordinate,
set \(x^0=ct\), with source interval \(cI\), only in the comparison
map from HW.28. Then \(\widetilde w_i(x^0,x,s)=w_i(x^0/c,x,s)\)
and \(dx^0=c\,dt\). The source's spatial and time norm definitions
at author lines 987–1019 consequently give, component by component,


\[
\begin{aligned}
\|\widetilde w_i\|_{\mathcal L_s^{1,p}
                    \mathcal L_{x^0}^2\dot{\mathcal H}_x^{m-1}}
 &=\sqrt c\,
 \left\|s^{(m-1)/2}\|\partial_x^{(m-1)}w_i\|_{L^2_{t,x}}
                                              \right\|_{L^p(ds/s)},\\
\|\widetilde N_{w,i}\|_{\mathcal L_s^{2,p}
                    \mathcal L_{x^0}^2\dot{\mathcal H}_x^q}
 &=\sqrt c\,
 \left\|s^{q/2+1}\|\partial_x^{(q)}N_{w,i}\|_{L^2_{t,x}}
                                              \right\|_{L^p(ds/s)}.
\end{aligned}\tag{ST.33}
\]


The unchanged heat exponents are
\(1-1/4-3/4+(m-1)/2=(m-1)/2\) and
\(2-1/4-3/4+q/2=1+q/2\).
For each spatial derivative order the full ordered L2 tuple equals
the Fourier homogeneous norm, since its squared symbol is
\((\xi_1^2+\xi_2^2+\xi_3^2)^q\).
The full three-output norm lies between the maximum component norm
and \(\sqrt3\) times that maximum for each of \(p=2,\infty\);
the upper inequality follows by bounding each component before
taking the outer norm, and the lower one by inclusion.
Thus the exact measure factor and component comparison are proved.
The original physical \(t\)-norms remain the objects estimated above.

The improved tension and forcing estimates are therefore now
proved at all ordinary spatial orders, with explicit finite
recurrences and all original field terms, heat factors,
physical measures and endpoint dependencies retained. They
depend on the actual full wave norms at the indicated orders.
The next calculation must establish which finite collection
closes the physical wave estimate and control the remaining
boundary terms; ST.1–ST.33 does not assume or assert that closure.

![Exact weighted temporal kernels with their attained maxima on the original heat interval.](../figures/f09-spacetime-tension.svg)

**Figure ST.** The three functions are exactly
\(s^\beta\mathfrak h_q(s,S)\) from ST.5–ST.7 at \(S=4\) square
metres, for the indicated original \(q,\beta\).
Their distinct physical units are retained on separate panels.
Each marked maximum is the exact critical point from ST.7.
The lower displayed heat time is a viewing limit; the original
domain remains \(0<s\le S\). These are scalar proof kernels,
not sampled Yang–Mills fields.

## 9. Exercises with complete solutions

### Exercise 1. Account for every canceled pair

Prove ST.2 directly from both spatial sums in ST.1, keeping
the ordered pairs and the derivative acting on its original field.

**Solution.** For each \(k,j\), set
\(A_{kj}=[F_{kj},D_kF_{ij}]\).
The term indexed by \((j,k)\) in the second sum is


\[
[F_{jk},D_kF_{ij}]=-A_{kj}.
\tag{ST.34}
\]


The exchange \((k,j)\mapsto(j,k)\) is a bijection of all nine
pairs. The three diagonal pairs vanish because \(F_{kk}=0\);
the six off-diagonal terms cancel their displayed partners.
No covariant derivatives were commuted. Applying any ordinary
derivative word to this exact zero identity retains the same
cancellation at every order.

### Exercise 2. An exact kernel norm and its maximum

Take \(q=1,\beta=1/4\). Evaluate both norms in ST.7 and
locate the maximum.

**Solution.** Here \(\gamma_1=1/8\) and
\(\mathfrak h_1=8(s^{-1/8}-S^{-1/8})\). Direct substitution gives


\[
\mathfrak H_1^2(1/4)=8\sqrt{2/3}\,S^{1/8},\qquad
\mathfrak H_1^\infty(1/4)=2S^{1/8},\qquad s_*=S/256.
\tag{ST.35}
\]


For the first value, the bracket of three integrals in ST.7
is \(4-16/3+2=2/3\), with exterior factor \(64S^{1/4}\)
before taking the square root. For the maximum,
\(((\beta-\gamma_1)/\beta)^{1/\gamma_1}=(1/2)^8\).
Substitution into the unchanged function confirms the value.

### Exercise 3. Write the first nontrivial induction step

Expand ST.28 at \(q=1\) and identify the new constants
constructed by ST.31.

**Solution.** Both choices of the single differentiated
potential in the double bracket occur. The full expression is


\[
\begin{aligned}
N_1^2={}&4S^{1/4}(U_0B_2+U_1B_1)
 +2\sqrt6 S^{1/4}(U_1A_1+U_2A_0)\\
&+4\sqrt S(2U_0U_1A_0+U_0^2A_1)
 +4\sqrt2 S^{1/4}(C_0^FA_1+C_1^FA_0)+Q_1^2,\\
A_2&=B_3=\sqrt{2B_2^2+(N_1^2)^2}.
\end{aligned}\tag{ST.36}
\]


The preceding step already constructed \(A_1,B_2\).
Neither \(A_2\) nor \(B_3\) occurs in the first two lines.
Thus this is a finite computation from prior constants, not
an inequality assuming the desired new bound.

### Exercise 4. Ordered electric derivatives

Expand \(\partial_r\partial_sE_i\) from ST.9.

**Solution.** Ordinary derivatives commute on the regular
field, but the bracket order is retained. The complete result is


\[
\begin{aligned}
\partial_r\partial_sE_i={}&
 \partial_t\partial_r\partial_sa_i-\partial_r\partial_s\partial_i a_t\\
&+[\partial_r\partial_sa_t,a_i]
 +[\partial_sa_t,\partial_ra_i]
 +[\partial_ra_t,\partial_sa_i]
 +[a_t,\partial_r\partial_sa_i].
\end{aligned}\tag{ST.37}
\]


The two middle bracket terms come from the two distinct
one-element subsets of the ordered word. Even when \(r=s\),
both occurrences remain and give multiplicity two.
This is precisely the binomial factor in ST.22.

### Exercise 5. Retain a nonzero heat datum in the comparison identity

For ST.15 with a general initial norm \(\|z(0)\|_2=a\ge0\)
and \(\int_0^S e^{-\Phi}\|Q\|_2ds\le q\), prove the
corresponding two bounds.

**Solution.** The regularized norm argument gives
\(\sup_s\|z(s)\|_2\le a+q\).
Integrating the original squared energy identity and retaining
its initial contribution gives


\[
\sup_s\|z(s)\|_2\le a+q,\qquad
\int_0^S\|D_xz(s)\|_2^2ds\le\tfrac12a^2+(a+q)q.
\tag{ST.38}
\]


The upper endpoint term is nonnegative and may be dropped
only for this inequality. Multiplication by the original
\(e^{\Phi(S)}\) gives the corresponding bounds on \(w\).
The actual Yang–Mills tension has \(a=0\); this calculation
shows exactly where that datum enters. It does not claim that
a nonzero tension datum satisfies the original field equations.

### Exercise 6. A noncommuting electric jet

Let
\(T_1=\begin{pmatrix}0&i\\i&0\end{pmatrix}\),
\(T_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\), and
\(T_3=\operatorname{diag}(i,-i)\).
At one point suppose the only nonzero electric entries are
\(E_1=eT_1\) and \(D_2E_1=fT_2\), with real \(e,f\).
Evaluate ST.2.

**Solution.** Matrix multiplication gives
\([T_1,T_2]=-2T_3\).
Only the output \(i=2\) and the first part of its \(j=1\)
term survive, so


\[
Q_2=4c^{-2}efT_3,\qquad Q_1=Q_3=0,\qquad
|Q|=4\sqrt2\,c^{-2}|ef|.
\tag{ST.39}
\]


The Hilbert–Schmidt norms are
\(|E|=\sqrt2|e|\), \(|D_xE|=\sqrt2|f|\).
The proved upper bound is therefore \(24c^{-2}|ef|\),
which indeed dominates the computed value.
This is a test of the pointwise tensor expression, not a
claim of a global solution with these prescribed jets.

### Exercise 7. Compare the two tension conventions exactly

Use \(x^0=ct\), \(\widetilde a_0=c^{-1}a_t\),
\(\widetilde a_i=a_i\), with evaluation at \(t=x^0/c\).
Compute the spatial tension in the source coordinate.

**Solution.** The chain rule and connection term give
\(\widetilde D_0=c^{-1}D_t\) on the composed fields.
The original electric curvature obeys
\(\widetilde F_{0i}=c^{-1}E_i\). Hence


\[
\widetilde w_i
=-\widetilde D_0\widetilde F_{i0}
 +\sum_j\widetilde D_j\widetilde F_{ij}
=c^{-2}D_tE_i-G_i=w_i.
\tag{ST.40}
\]


The time arguments are related by the stated composition.
The physical measure then contributes \(\sqrt c\) in L2,
as in ST.33. No component or speed was silently removed.

### Exercise 8. The strict heat-weight threshold

For \(\gamma_q>0\), show that the \(L^2(ds/s)\) norm in
ST.6 diverges at the excluded value \(\beta=\gamma_q\).

**Solution.** The weighted kernel is
\((1-(s/S)^{\gamma_q})/\gamma_q\). Its exact cutoff square is


\[
\begin{aligned}
\int_\varepsilon^S
 [s^{\gamma_q}\mathfrak h_q(s,S)]^2\frac{ds}{s}
=\frac1{\gamma_q^2}\biggl[
 \log(S/\varepsilon)
 -\frac2{\gamma_q}(1-(\varepsilon/S)^{\gamma_q})
 +\frac1{2\gamma_q}(1-(\varepsilon/S)^{2\gamma_q})
 \biggr].
\end{aligned}\tag{ST.41}
\]


The latter two terms have finite limits; the logarithm
diverges. If \(\gamma_q<0\) and \(\beta=0\), the kernel instead
tends to the nonzero constant \(S^{-\gamma_q}/(-\gamma_q)\),
so its squared heat integral again diverges.
These exact endpoint behaviors justify both strict inequalities
in \(\beta>\max(\gamma_q,0)\).


## Further reading: electric smoothing with fewer wave inputs

[Electric-curvature smoothing](../classical-electric-smoothing.html),
ES.25–ES.29, gives complete alternative inputs for ST.12 and ST.22–ST.32.
Every finite electric derivative is bounded from the lowest electric
input, retaining the potential bracket, the original factor
\(12c^{-2}\), and all heat exponents. The estimates above remain valid;
the linked proof gives the stronger dependence needed in the finite
wave argument.


## Further reading: every tension term in the wave equation

[The complete tension forcing](../classical-tension-forcing.html),
TW.1–TW.30, uses electric smoothing to evaluate all tension constants
from the lowest electric inputs. It also proves the exact spatial-label
operator estimates for the full wave forcing, including the covariant
derivative and nested commutator terms.
