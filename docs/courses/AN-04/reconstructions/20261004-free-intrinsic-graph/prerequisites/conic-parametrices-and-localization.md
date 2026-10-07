# Conic inverses and the full localization theorem

An elliptic test can be inverted near its noncharacteristic directions.
The inverse need not be an actual inverse on all distributions: a smooth
error is enough. We construct that inverse with every symbol remainder,
then prove that finitely many directional tests recover the full local
Besov estimate. This supplies the converse in the intrinsic localization
theorem, including finite-rank matrix tests.

This is a bounded modified selection of AN03-U010, Section 2, and
AN03-U012, Section 6, with the conic and intrinsic arguments completed
below. Original principal author and publisher: AN-03 course-writing
task / AN-03 local course project, 2026. Earlier modification: AN-03 course-writing task and OpenAI
Codex. This selection and its connecting proofs: GPT-6 Astra (OpenAI),
Ultra, 4 October 2026; publisher: AN-04 local course project.

Original text: CC0.

## K0. Exact inputs and conic conventions

We use ordinary symbols \(S^d=S^d_{1,0}\), real orders, left
quantization, \(D=-i\partial\), and the Fourier inverse factor
\((2\pi)^{-n}\). No homogeneous expansion is assumed.
The complete earlier proofs are:

- [P2 O0–O6](ordinary-operator-calculus.md): all differentiated product
  remainders, compact amplitudes, proper kernels and their smooth ideal;
- [P1 B1–B6](dyadic-endpoint.md): the exact supremum Besov endpoint,
  local order-zero mapping and smooth outputs;
- [T0–T3 and W1–W5](coordinate-and-wavefront-localization.md): coordinate
  and frame transport, essential support, its product inclusion, the
  Fourier wavefront criterion and proper compact conic cutoffs;
- the exact U001 smooth cutoffs, compactness, finite-dimensional inverse
  and differential proofs linked in those companions.

Write \(\operatorname{ess}(A)\) for the complementary closed conic set
of points where a full symbol is smoothing on a neighborhood. In
particular T2 proves
\[
 \operatorname{ess}(AB)
       \subset\operatorname{ess}(A)\cap\operatorname{ess}(B).
 \tag{R1}
\]
Every operator below is proper when it acts on an arbitrary distribution.
A kernel with compact support in both variables is proper. An error
that is smoothing on a cone means one fixed open cone on which all
negative-order estimates, with all derivatives, hold.

All constructions can be made in a compact part of one coordinate
chart. They extend by zero as proper operators on the manifold.
The statements about local spaces then apply in every chart and frame
by T3. Thus no finite global atlas or uniform geometry is assumed.

## K1. Summation with every derivative and with support retained

For global ordinary symbols with compact base support, put
\[
 p_{d,L}(a)=\max_{|\alpha|+|\beta|\le L}
  \sup_{x,\xi}\langle\xi\rangle^{-d+|\alpha|}
       \|\partial_\xi^\alpha\partial_x^\beta a(x,\xi)\|.
 \tag{R2}
\]
The same proof below works for uniformly bounded global base estimates.
Matrix norms may be used throughout.

Let \(a_j\in S^{d_j}\), \(d_j\to-\infty\). Monotonicity is not
required. Set \(D_k=\max_{j\ge k}d_j\); the maximum exists since
only finitely many terms can exceed the first term of that tail.
There is a smooth \(a\) such that
\[
 \begin{gathered}
 a\in S^{D_0},\qquad
 a-\sum_{j<k}a_j\in S^{D_k}\quad(k\ge0),\\
 \operatorname{supp}a\subset\bigcup_j\operatorname{supp}a_j.
 \end{gathered}
 \tag{R3}
\]
Its class modulo \(S^{-\infty}\) is unique and is unchanged by
rearranging the sequence, with the corresponding tail orders.

**Proof.** Choose a fixed smooth \(\chi\), equal to one for
\(|\xi|\le1\) and zero for \(|\xi|\ge2\). Choose strictly increasing
\(R_j\to\infty\) so large that
\[
 A_j=(1-\chi(\xi/R_j))a_j,\qquad
 p_{d_j+1,L}(A_j)\le2^{-j}\quad(0\le L\le j).
 \tag{R4}
\]
Here is the estimate ensuring that choice. When no derivative hits
the cutoff, its support has \(|\xi|\ge R_j\), and the one-order
loss contributes at most \(C/R_j\). When \(r\ge1\) frequency
derivatives hit it, their factor is at most \(C_rR_j^{-r}\),
supported where \(R_j\le|\xi|\le2R_j\). The remaining derivatives
of \(a_j\) have order \(d_j-|\alpha|+r\); the weight in (R2)
therefore gives at most \(C\langle\xi\rangle^{-1+r}R_j^{-r}\),
again at most \(C'/R_j\). Base derivatives do not differentiate
this cutoff. For each finite list \(L\le j\), take \(R_j\) larger
than all these finitely many constants times \(2^j\), and larger
than \(R_{j-1}+1\). This proves (R4).

Define \(a=\sum_j A_j\). On each bounded frequency set only
finitely many terms occur, so \(a\) is smooth and can be
differentiated term by term there. Fix \(k,L\). Choose
\(J\ge\max(k,L)\) with \(d_j+1\le D_k\) for every \(j\ge J\).
Since \(p_{D_k,L}\le p_{d_j+1,L}\), the tail is bounded by
\(\sum_{j\ge J}2^{-j}\) in this seminorm. This bound follows
pointwise from finite sums before taking the supremum; no
unproved interchange of an infinite differentiated series is used.
The remaining terms in \(a-\sum_{j<k}a_j\) are finitely many
symbols of order at most \(D_k\) and the finitely many terms
\(-\chi(\xi/R_j)a_j\), \(j<k\). Each of the latter has bounded
frequency support and hence is smoothing. This proves every
seminorm assertion in (R3), including \(k=0\).

At a point outside the displayed union of supports, a neighborhood
meets only finitely many possible \(A_j\); shrink it so that each
of their original \(a_j\) vanishes there. Then \(a\) vanishes
there. This proves support containment, even when the union is
not closed. Two sums differ by \(S^{D_k}\) for every \(k\),
so their difference is smoothing. For a finite initial segment
of a rearrangement, let \(D\) be the largest order omitted from
it. An original initial segment containing those chosen terms
and every term of order greater than \(D\) shows that the new
remainder is in \(S^D\). This proves the rearranged assertion.
\(\square\)

### K1a. The properly supported operator sum actually needed here

Suppose \(C_j\in\Psi^{d-j}\) have kernels supported in one
fixed compact chart product. There exists a compact-kernel
\(C\in\Psi^d\) with
\[
 C-\sum_{j<N}C_j\in\Psi^{d-N}\qquad(N\ge0).
 \tag{R5}
\]
Indeed P2 O4–O5 and Fourier inversion of the compact kernel in
the difference variable give a full symbol \(c_j\in S^{d-j}\)
with base support in one fixed compact set. Sum those symbols
by K1. Quantize the result using a fixed compact kernel cutoff
equal to one near that compact diagonal. The same cutoff
changes each original \(C_j\) only by a smooth compact kernel:
the changed part is separated from the diagonal. Quantizing
each remainder in (R3), and adding these finitely many smooth
differences, proves (R5). This is an asymptotic sum; there is
no claim that \(\sum_j C_j\) converges in operator norm.

## K2. Ordinary matrix inverses on an elliptic cone

Let \(a(x,\xi)\in S^d\) be a square matrix symbol. It is elliptic
on a compactly based conic neighborhood \(V\), above a radius \(R\),
if there is \(c>0\) such that
\[
 \|a(x,\xi)v\|\ge c\langle\xi\rangle^d\|v\|
 \quad ((x,\xi)\in V,\ |\xi|\ge R).
 \tag{R6}
\]
The matrix is injective, hence bijective by the proved finite-dimensional
dimension theorem applied to the underlying real space of dimension
\(2q\), for matrix size \(q\). Its unique real inverse is complex linear:
\(a(iv)=i\,a(v)\) and uniqueness give \(a^{-1}(iw)=i\,a^{-1}w\).
The bound is \(\|a^{-1}\|\le c^{-1}\langle\xi\rangle^{-d}\).
The real cofactor formula gives smoothness where it is invertible,
and hence smoothness of its complex matrix entries.
Differentiating \(a^{-1}a=I\) gives
\[
 \partial a^{-1}=-a^{-1}(\partial a)a^{-1}.
 \tag{R7}
\]
For a combined base/frequency multiindex \(\nu\ne0\), repeated
Leibniz differentiation gives more explicitly
\[
 (\partial^\nu a^{-1})a
 =-\sum_{0<\mu\le\nu}\binom\nu\mu
       (\partial^{\nu-\mu}a^{-1})(\partial^\mu a).
 \tag{R8}
\]
Multiply on the right by \(a^{-1}\) and use induction on
\(|\nu|\). If \(\alpha\) counts its frequency derivatives,
each term has order \(-d-|\alpha|\): the two inverse orders
and the order of \(a\) add in precisely that way. Thus
\(a^{-1}\in S^{-d}\) on each smaller elliptic cone, with all
base derivatives of order zero cost.

Multiplication by a smooth degree-zero angular/base cutoff supported
strictly within \(V\), and by a high-frequency cutoff zero below \(R\),
extends this inverse smoothly by zero to a compact-base global
\(S^{-d}\) symbol. All cutoff derivatives have the ordinary budgets;
near the support boundary the cutoff already vanishes on a neighborhood.

The condition is stable under \(S^{d-1}\) errors: their action on a
vector has norm at most \(C\langle\xi\rangle^{d-1}\|v\|\),
so (R6) retains \(c/2\) after increasing the radius. Chart and frame
changes preserve it by T1–T3 and compact bounds for the invertible
coordinate and frame matrices. This defines the intrinsic open
elliptic set of an ordinary operator, without classical symbols.

## K3. A two-sided conic parametrix with one fixed error cone

Let \(A\in\Psi^d\) be proper and elliptic at a nonzero covector
\(\rho\). There is a proper \(B\in\Psi^{-d}\) such that
\[
 I-BA\quad\hbox{and}\quad I-AB
 \quad\hbox{are smoothing near }\rho.
 \tag{R9}
\]
The operator \(B\) may have compact kernel in the chosen chart.

**Proof.** Work with a full local symbol \(a\) of \(A\), after
compact localization as in P2 O5. Choose nested conic neighborhoods
\(V_0\Subset V_1\Subset V_2\) of \(\rho\), where compact containment
means containment of their closed base/unit-direction sections.
Take \(V_2\) inside the elliptic region. K2 constructs a compact-base
\(b_0\in S^{-d}\), equal to \(a^{-1}\) on \(V_1\) at high
frequency. Proper compact quantization gives \(B_0\) with that
full symbol modulo smoothing. Hence
\[
 E_L=I-B_0A\in\Psi^{-1}\ \hbox{on }V_1,
 \qquad E_L\in\Psi^0\ \hbox{locally everywhere}.
 \tag{R10}
\]
The first claim is exactly the first remainder of P2's full product
formula, since \(b_0a=I\) there. There is no assertion that this
error has negative order outside \(V_1\).

Take a further scalar conic cutoff equal to one near the closure
of \(V_0\), supported in \(V_1\), with the same harmless low-frequency
truncation. Multiply a full local symbol of \(E_L\) by it and
extend by zero. The result is a global compact-base \(S^{-1}\)
symbol, because the error has order \(-1\) throughout its support.
Its proper compact quantization \(R_L\in\Psi^{-1}\) satisfies
\[
 R_L-E_L\ \hbox{is smoothing on }V_0.
 \tag{R11}
\]
All kernels \(R_L^jB_0\) are supported in one fixed compact chart
product: both factors were chosen inside that product, and its
intermediate integrations do not enlarge it. Their orders are
\(-d-j\). K1a therefore gives \(B_L\in\Psi^{-d}\) with
\[
 B_L-S_N\in\Psi^{-d-N},\qquad
 S_N=\sum_{j=0}^{N-1}R_L^jB_0.
 \tag{R12}
\]
For every finite \(N\ge1\), associativity gives the exact identity
\[
 S_NA=I-R_L^N+
       \sum_{j=0}^{N-1}R_L^j(R_L-E_L).
 \tag{R13}
\]
The last sum is smoothing on \(V_0\) by (R1) and (R11).
The other two errors in \(B_LA-I\) are \(R_L^N\in\Psi^{-N}\)
and \((B_L-S_N)A\in\Psi^{-N}\). Therefore \(B_LA-I\) has
every negative order on the same \(V_0\), with every differentiated
estimate. It is smoothing there.

For the right side put \(E_R=I-AB_0\), cut its order-\(-1\)
symbol down in the same way to obtain \(R_R\), and asymptotically
sum \(B_0R_R^j\). With \(T_N=\sum_{j<N}B_0R_R^j\), the finite
identity is
\[
 AT_N=I-R_R^N+
       \sum_{j=0}^{N-1}(R_R-E_R)R_R^j.
 \tag{R14}
\]
It proves \(AB_R-I\) smoothing on \(V_0\). Matrix factors have
not been commuted in either construction. Finally
\[
 B_L-B_R=B_L(I-AB_R)+(B_LA-I)B_R
 \tag{R15}
\]
is smoothing there by (R1). Thus \(AB_L-I\) is also smoothing
there, and \(B=B_L\) proves (R9). \(\square\)

This also proves microlocal uniqueness modulo smoothing. If a given
\(\widetilde B\in\Psi^{-d}\) has a left inverse property on a
cone, compare it with \(B\) using (R15); the difference is smoothing
on a smaller common cone, so it has the right inverse property as
well. The same argument starts from a right inverse.
Conversely, a left inverse property implies, in full symbols,
\(ba=I+r\) with \(r\in S^{-1}\). At high frequency
\(\|ba v\|\ge\|v\|/2\), while \(\|b\|\le C\langle\xi\rangle^{-d}\).
Thus (R6) holds. For a right inverse, write \(ab=I+r\).
The bound \(\|(I+r)v\|\ge\|v\|/2\) gives bijectivity and
\(\|(I+r)^{-1}\|\le2\) by finite-dimensionality. Hence
\(b(I+r)^{-1}\) is a right inverse for \(a\). A square matrix
with a right inverse is surjective, therefore bijective, so
\(a^{-1}=b(I+r)^{-1}\) has the required norm bound.

As one consequence, \(Au\) smooth microlocally at an elliptic point
implies \(u\) smooth there. Indeed \(u=BAu+(I-BA)u\): W4 makes
the first term regular in that direction, and makes the second
regular by its smoothing symbol. Together with pseudolocality this
gives equality of the two wavefront sets on the elliptic set.

## K4. A finite conic partition reconstructs a compact localization

Fix \(\varphi\in C_c^\infty\), with support \(K\) in one chart.
Suppose open cones \(V_\rho\) cover \(K\times S^{n-1}\).
There are finitely many proper compact-kernel \(Q_j\in\Psi^0\)
and a smooth proper kernel \(R\) such that
\[
 \varphi I=\sum_{j=1}^JQ_j+R,\qquad
 \operatorname{ess}(Q_j)\subset V_{\rho_j}.
 \tag{R16}
\]

**Proof.** The compactness of \(K\times S^{n-1}\), proved by the
earlier finite-dimensional compactness results, gives a finite
subcover after shrinking each chosen neighborhood. Use the U001
finite smooth cutoff construction in the ambient base/frequency
coordinates, restrict to the unit sphere, and obtain nonnegative
\(h_j(x,\omega)\) supported strictly inside those conic sections.
Their sum \(H\) is positive on \(K\times S^{n-1}\). Its minimum
there is positive; choose \(\epsilon>0\) with \(H\ge2\epsilon\)
on that compact set. Let \(F(t)\) be smooth, zero for
\(t\le\epsilon/2\), and equal to \(1/t\) for \(t\ge\epsilon\).
It is constructed by multiplying the reciprocal by a smooth cutoff
away from zero and extending by zero. Set
\[
 q_j(x,\omega)=\varphi(x)h_j(x,\omega)F(H(x,\omega)).
 \tag{R17}
\]
These are smooth and satisfy \(\sum_jq_j=\varphi\) everywhere:
on \(K\times S^{n-1}\) the reciprocal applies, and outside \(K\)
both sides vanish. Each support stays inside its assigned section.

Extend them by \(q_j(x,\xi/|\xi|)\theta(|\xi|)\), where
\(\theta=0\) near zero and \(\theta=1\) above a fixed radius.
Frequency derivatives of \(\xi/|\xi|\) have their degree-\(-1\)
budget; the iterated chain rule proves that these are compact-base
\(S^0\) symbols. Quantize with a common proper compact kernel
cutoff equal to one near the relevant diagonal. The full symbols
change only by smoothing, by P2 O4. Consequently their sum is
\(\varphi(x)\theta(|\xi|)I\) modulo smoothing. Its difference
from \(\varphi(x)I\) has compact frequency support, hence is
smoothing. T2's finite compact cosphere argument now gives a
smooth proper kernel \(R\), proving (R16). \(\square\)

## K5. Directional Besov tests give the actual local space

Let \(s\in\mathbb R\) and \(v\in\mathcal D'\). Suppose that at
each nonzero covector \(\rho\) there is a proper \(A_\rho\in\Psi^0\),
elliptic there, such that \(A_\rho v\in B^s_{2,\infty,\mathrm{loc}}\).
Then
\[
 v\in B^s_{2,\infty,\mathrm{loc}}.
 \tag{R18}
\]

**Proof.** K3 supplies a proper \(B_\rho\in\Psi^0\) and a
cone \(V_\rho\) on which \(E_\rho=I-B_\rho A_\rho\) is
smoothing. For any fixed compact output cutoff, use K4 to choose
finitely many \(Q_j\) whose essential supports lie in these cones.
Then exactly
\[
 Q_jv=Q_jB_{\rho_j}(A_{\rho_j}v)+Q_jE_{\rho_j}v.
 \tag{R19}
\]
The first term belongs to the local Besov space by P1 B6. The
second is smooth: (R1) makes its essential support empty, and
the compact output support and properness confine its kernel
to a compact product, so T2 gives a smooth kernel. Equation
(R16) reconstructs \(\varphi v\) from finitely many such pieces
and one more smooth output. These pieces have compact support.
For a compactly supported distribution, local Besov membership
is global membership in the chart: multiply by one larger compact
cutoff equal to one near its support. Smooth compact functions
belong to every such space by Fourier decay. The triangle inequality
for the dyadic supremum norm therefore proves (R18). No uniform
constant over an infinite family of tests is needed. \(\square\)

## K6. The full intrinsic localization theorem

Let \(\Lambda\subset T^*X\setminus0\) be a smooth closed conic
Lagrangian, and \(E\to X\) a smooth finite-rank complex bundle.
Put \(s=-m-n/4\). The intrinsic class consists of distributions
for which every finite word in proper order-one operators with
symbol of order zero on \(\Lambda\) has output in
\(B^s_{2,\infty,\mathrm{loc}}\); the empty word is included.
Then:

1. \(\operatorname{WF}(u)\subset\Lambda\) for \(u\in I^m\).
2. Every proper \(A\in\Psi^0(X;E,E)\) maps \(I^m\) to itself.
3. If for each nonzero \(\rho\) there is a proper order-zero
   \(A_\rho\), elliptic at \(\rho\), with \(A_\rho u\in I^m\),
   then \(u\in I^m\).

**Proof.** Assertion 1 is precisely the proved W5, transported by
T3. For assertion 2 let \(L\) be an admissible order-one matrix
operator. The full product formula gives principal commutator
symbol \(la-al\) modulo \(S^0\). On \(\Lambda\) both products
are of order zero, since \(l|_\Lambda\in S^0\). Thus
\([L,A]\) is again admissible; its order need only be one.
For every finite word the exact telescoping identity is
\[
 \begin{aligned}
 L_1\cdots L_N A
 &=A L_1\cdots L_N\\
 &\quad+\sum_{j=1}^N
   L_1\cdots L_{j-1}[L_j,A]L_{j+1}\cdots L_N.
 \end{aligned}
 \tag{R20}
\]
For \(N=1\) this is the definition of the commutator. Multiplying
the identity for the suffix by \(L_1\), and replacing
\(L_1A\) by \(AL_1+[L_1,A]\), proves it inductively, without
exchanging any matrix factors. The first output in (R20) is
in \(B^s_{\mathrm{loc}}\) by P1's order-zero bound. Each summand
is an admissible word applied to \(u\). The empty-word case uses
the same order-zero bound. This proves assertion 2.

For assertion 3 choose the conic parametrix \(B_\rho\) of K3.
By assertion 2, \(v_\rho=B_\rho A_\rho u\in I^m\).
The error \(u-v_\rho=E_\rho u\) has an operator \(E_\rho\)
whose symbol is smoothing on some cone \(V_\rho\). Fix an
arbitrary admissible word \(W\).
Choose a proper compact conic cutoff \(Q_\rho\), elliptic at
\(\rho\), with essential support inside \(V_\rho\), as in W4.
Then
\[
 Q_\rho Wu=Q_\rho Wv_\rho+Q_\rho WE_\rho u.
 \tag{R21}
\]
The first term lies in \(B^s_{\mathrm{loc}}\); the second is
smooth by (R1) and the compact-kernel argument of K5.
Thus every nonzero direction has an elliptic Besov test for \(Wu\).
K5 gives \(Wu\in B^s_{\mathrm{loc}}\). This holds for every
finite word, including \(W=I\), and proves assertion 3.
All constants may depend on that word. The chart and bundle
formulations agree by T3. \(\square\)

## K7. Independence of sufficiently small cutoff and Lagrangian extension

Suppose \(Au\in I^m(X,\Lambda_1)\), with \(A\in\Psi^0\)
proper and elliptic at \(\rho\). There is a fixed cone \(V\)
about \(\rho\) such that, for every proper compact-kernel
\(P\in\Psi^0\) with \(\operatorname{ess}(P)\subset V\),
\[
 Pu\in I^m(X,\Lambda_1).
 \tag{R22}
\]
Indeed use \(B\) from K3, shrink \(V\) inside the smoothing
region of \(E=I-BA\), and write \(Pu=PBAu+PEu\).
K6(2) treats the first term. The second is smooth by (R1).
A smooth section satisfies every word estimate, by P2 O5 and
the compact smooth Fourier bounds. This proves (R22).
In particular any sufficiently small elliptic test at \(\rho\)
can replace the original one. A larger cutoff containing other,
untested directions is not covered by this assertion.

Now let two closed conic Lagrangians \(\Lambda_1,\Lambda_2\)
agree on an open cone \(V\). For \(w\in I^m(X,\Lambda_1)\),
take a compact proper \(P\in\Psi^0\) whose essential support
is compactly contained in \(V\) in base/unit-direction variables.
Then
\[
 Pw\in I^m(X,\Lambda_2).
 \tag{R23}
\]
To prove this, choose a compact proper scalar \(C\in\Psi^0\)
with full symbol one modulo smoothing on a neighborhood of
\(\operatorname{ess}(P)\), and essential support inside \(V\).
To construct it, cover that compact base/unit-direction set by
finitely many smooth bumps supported in \(V\), as in K4, and
let \(H\) be their positive sum. Compose \(H\) with a smooth
function zero below a small positive threshold and one above
a larger threshold below its minimum on the compact set.
The resulting conic symbol is one near the compact set and
supported in \(V\). Truncate near zero frequency and quantize
with a compact kernel cutoff. P2 O4 gives the required full
symbol modulo smoothing.

For any admissible \(\Lambda_2\)-word \(L_1\cdots L_N\), put
\(M_j=CL_jC\). Its principal symbol is \(c^2l_j\) modulo
\(S^0\), so it has order zero on \(\Lambda_1\): on the support
of \(c\) the two Lagrangians agree, and outside it the symbol
is smoothing. Thus every \(M_j\) is admissible for \(\Lambda_1\).
Also \(L_j-M_j\) is smoothing on a fixed neighborhood of
\(\operatorname{ess}(P)\), by the full product expansion.
The finite difference identity
\[
 \begin{aligned}
 &(L_1\cdots L_N-M_1\cdots M_N)P\\
 &\quad=\sum_{j=1}^N L_1\cdots L_{j-1}
      (L_j-M_j)M_{j+1}\cdots M_NP
 \end{aligned}
 \tag{R24}
\]
has smoothing summands by (R1). Properness and compact output
localization make them smooth on distributions. Meanwhile K6(2)
gives \(Pw\in I^m(X,\Lambda_1)\), so \(M_1\cdots M_NPw\)
has the required Besov order. This proves (R23). Interchanging
the two extensions proves the reverse assertion. Together with
(R22), this proves that the microlocal intrinsic class depends
only on the germ of the Lagrangian and on sufficiently small
elliptic cutoffs, when a closed conic extension is used.

## Two exercises with complete solutions

**Exercise K1.** Let
\[
 A=\begin{pmatrix}2&1\\0&1\end{pmatrix},\qquad
 B_0=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
 \tag{R25}
\]
Check the finite inverse-correction algebra and explain why it
does not imply convergence of an infinite matrix series.

**Solution.** Direct multiplication gives
\(R=I-AB_0=\begin{pmatrix}-2&-1\\-1&0\end{pmatrix}\) and
\(L=I-B_0A=\begin{pmatrix}-1&-1\\-2&-1\end{pmatrix}\).
Here \(B_0R=LB_0=\begin{pmatrix}-2&-1\\-3&-1\end{pmatrix}\),
whereas \(RB_0=\begin{pmatrix}-3&-1\\-1&0\end{pmatrix}\).
For every finite \(N\), telescoping gives
\(A\sum_{j<N}B_0R^j=I-R^N\) and
\((\sum_{j<N}L^jB_0)A=I-L^N\).
For \(N=2\) the first side is
\(\begin{pmatrix}-4&-2\\-2&0\end{pmatrix}=I-R^2\).
But \(\lambda=-1-\sqrt2\) and \(v=(-\lambda,1)^T\)
satisfy \(Rv=\lambda v\), since \(\lambda^2+2\lambda-1=0\).
Thus \(B_0R^jv=\lambda^jB_0v\) does not tend to zero.
The infinite matrix series cannot converge. K3 uses decreasing
symbol orders and (R5), not convergence of this algebraic series.
\(\square\)

**Exercise K2.** On the line choose smooth \(\gamma_+\), zero
for \(\xi\le1\) and one for \(\xi\ge2\), and set
\(\gamma_-(\xi)=\gamma_+(-\xi)\). Let \(\varphi,\psi\) be
compact smooth cutoffs with \(\psi=1\) near
\(\operatorname{supp}\varphi\). Show explicitly how the two
directional pieces recover \(\varphi v\) modulo a smooth term.

**Solution.** Put \(Q_\pm=\varphi\gamma_\pm(D)\psi\).
The function \(r=1-\gamma_+-\gamma_-\) is smooth and supported
in \([-2,2]\). Since \(\varphi\psi=\varphi\),
\[
 \begin{gathered}
 \varphi v=Q_+v+Q_-v+Rv,\\
 K_R(x,y)=\frac{\varphi(x)\psi(y)}{2\pi}
       \int_{-2}^{2}e^{i(x-y)\xi}r(\xi)\,d\xi.
 \end{gathered}
 \tag{R26}
\]
Every derivative of this compact-frequency integral is absolutely
convergent, so \(R\) has a smooth compact kernel. If both
directional pieces belong to \(B^s_{\mathrm{loc}}\), their compact
support makes them global \(B^s\) functions in this chart; the
same is true of the smooth compact \(Rv\). The triangle inequality
then gives the exact endpoint bound for \(\varphi v\).
This is K4–K5 with the two points of the one-dimensional unit sphere.
\(\square\)

## Free human sources and the remaining course scope

[Gerd Grubb's author-hosted Chapter 7](https://web.math.ku.dk/~grubb/dist7n.pdf),
Lemma 7.3 and Theorem 7.18(1), with Corollary 7.19(1), supplies
the cutoff construction and finite inverse-correction method.
Its summation lemma is a sketch; K1 supplies every missing derivative
estimate and the support argument. K2–K3 give the full ordinary-symbol
conic construction rather than assuming a homogeneous expansion.

[Lars Hörmander, *Fourier integral operators. I*](https://projecteuclid.org/journals/acta-mathematica/volume-127/issue-none/Fourier-integral-operators-I/10.1007/BF02392052.pdf),
Propositions 1.1.9 and 2.5.1, records the asymptotic convention and
the parametrix mechanism. Its external proof references are not
programme dependencies. The complete proofs used here are the
ones written above and the exact earlier programme proofs in K0.

The intrinsic localization theorem is now supplied in full. The
representation using every prescribed nondegenerate or clean phase,
refined symbol orders, global Maslov data and the remaining AN-04
course are still separate proof obligations.
