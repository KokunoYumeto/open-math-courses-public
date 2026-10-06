# Dual conormal distributions and intrinsic boundary jets

This component retains the supported-test and duality proofs in AN03-U034, *Global boundary operators, compressed wave fronts, and normal extension*, Sections 2.5–2.6 and 3.1–3.4, with the exact current prerequisite connections stated below. The original source was written and dedicated to the public domain by Codex, September 2026 (CC0). The source connections and clarifications are by the AN-04 course-writing task and OpenAI Codex, 5 October 2026, also CC0. The linked conormal amplitude component retains its separate GFDL 1.2 licence.

All pairings here are the complex-linear distribution pairing against dual densities. Thus the transpose of \(D=-i\partial\) is \(-D\); Hilbert antidual conventions are used only where explicitly stated elsewhere. The full [conormal amplitude, Besov and completeness proofs](conormal-amplitudes-and-test-spaces.md) supply (C2)–(C17). The [locally finite partition proof PS5](../20261004-free-intrinsic-graph/prerequisites/global-principal-symbol.md) supplies the global compactly supported chart cutoffs. All arguments apply entry by entry to finite-rank bundles with their actual density changes.

For clarity, an ambient distribution supported in a closed half-space annihilates a smooth function which is zero on that half-space. On a fixed compact set the distribution has some finite order \(L\), by the complete [test-function argument T0](../20261004-free-intrinsic-graph/prerequisites/coordinate-and-wavefront-localization.md). Such a function and all its derivatives vanish at the boundary. Multiply it by a cutoff supported within normal distance \(2\epsilon\) of the half-space and equal to one within distance \(\epsilon\); the pairing does not change by support. Taylor's formula to degree greater than \(2L+1\) bounds its first \(L\) derivatives, including all derivatives on that cutoff, by \(C\epsilon\). The distributional finite-order bound makes its pairing tend to zero. Compact localization proves the stated annihilation and the independence of smooth extensions used below.

The mathematical antecedent is the approved Hörmander III, 2007 eBook, Section 18.3. The complete test and trace proofs follow. The further compressed operator calculus and the noncharacteristic \(\mathcal N\) extension are separate subsequent obligations.

## 1. The supported conormal test class

For real \(m\), let \(\mathcal A^m(X)\) consist of distributions supported
in the closed manifold which, in every boundary chart and its extension,
are conormal of order \(m\) to \(x_n=0\). Explicitly put
\(\kappa=-m-n/4\) and require
\[
 Pu\in B^\kappa_{2,\infty,\mathrm{loc}}
 \quad\text{for every }P\in\operatorname{Diff}_b(X),
 \qquad \operatorname{supp}u\subset X.
 \tag{GA1}
\]
The topology uses all these local seminorms. Multiplication, coordinate
changes and finite frame transitions are continuous on those Besov
spaces by (C2)–(C3), and the following local calculation identifies the intrinsic tangent fields: a smooth normal coefficient vanishing at zero equals \(t\int_0^1\partial_t b(x',st)\,ds\), so it is a smooth multiple of \(t\partial_t\).
Moving a coefficient through a word in tangent fields leaves only
shorter words with smooth coefficients. Hence (GA1) is intrinsic and
agrees exactly with (C15), with the original shift \(-m-n/4\).

The coordinate seminorms can use \(D'\) and \(X_n=x_nD_n\). The precise
comparison with the original weighted derivatives is
\[
 x_n^kD_n^k=\prod_{j=0}^{k-1}(X_n+ij),\qquad
 X_n^k=\sum_{j=0}^k c_{kj}\,x_n^jD_n^j,
 \tag{GA2}
\]
where the first polynomial identity defines an invertible triangular
change of basis and the second is its inverse. The first follows by
\(D_n x_n=x_nD_n-i\) and induction: multiplying
\(x_n^kD_n^k\) by \(X_n+ik\) on the right gives
\(x_n^{k+1}D_n^{k+1}\). These identities retain every lower term and its
factor \(i\). Tangential derivatives commute with \(X_n\). On compact
sets all smooth-coefficient tangent words reduce to these generators.
In particular (GA1) makes \(u\) smooth in the interior by repeated
ordinary derivatives there and the local Sobolev estimate.

## 2. Approximation which preserves the original closed support

Let \(q\in C_c^\infty(\mathbb R^n)\) have integral one and support in
the open positive half-space. Set
\(q_\varepsilon(z)=\varepsilon^{-n}q(z/\varepsilon)\) and
\(Q_\varepsilon u=q_\varepsilon*u\). For a distribution supported in
\(x_n\ge0\), this convolution is smooth and supported in
\(x_n\ge c\varepsilon\), where
\(c=\min_{\operatorname{supp}q}z_n>0\). Its support remains in one
fixed compact enlargement when the input support is fixed and
\(0<\varepsilon\le\varepsilon_0\).

We prove convergence in the conormal topology, including its weighted
normal derivatives. Write \(X_n=x_nD_n\), \(D_n=-i\partial_n\).
Integration by parts in the distribution pairing gives the exact identity
\[
 [X_n,Q_\varepsilon]u
     =D_{z_n}(z_nq_\varepsilon)*u.
 \tag{GS1}
\]
Indeed \(Q_\varepsilon X_nu\) has coefficient
\(y_nD_{z_n}q_\varepsilon+iq_\varepsilon\), whereas
\(X_nQ_\varepsilon u\) has coefficient
\(x_nD_{z_n}q_\varepsilon\). Their difference is
\(z_nD_{z_n}q_\varepsilon-iq_\varepsilon
=D_{z_n}(z_nq_\varepsilon)\). Both terms and their sign are retained.

Define \(q_0=q\),
\(q_{j+1}=D_{z_n}(z_nq_j)\), and let \(Q_{j,\varepsilon}\) denote
convolution by \(\varepsilon^{-n}q_j(z/\varepsilon)\).
Every \(q_j\) is smooth, has the same compact positive normal support,
and \(\int q_j=0\) for \(j\ge1\). Repeating (GS1) proves
\[
 X_n^\ell Q_\varepsilon
       =\sum_{j=0}^{\ell}\binom\ell j
          Q_{j,\varepsilon}X_n^{\ell-j}.
 \tag{GS2}
\]
Tangential derivatives commute with all these convolutions. These are
equalities on distributions; no boundary derivative term is dropped.

The Fourier multipliers satisfy, for each fixed \(j\),
\[
 |\widehat q(\varepsilon\xi)-1|
       \le C\min(\varepsilon|\xi|,1),\qquad
 |\widehat q_j(\varepsilon\xi)|
       \le C_j\min(\varepsilon|\xi|,1)\quad(j\ge1).
 \tag{GS3}
\]
For small arguments use the mean, the first-moment integral and
\(|e^{-iv}-1|\le|v|\); for all arguments use their finite \(L^1\)
norms. These multipliers commute with the dyadic projections of (C2).
Let \(\kappa'>\kappa\), \(\delta=\kappa'-\kappa>0\), and
\(\tau=\min(1,\delta)\). The multiplier bound on the \(l\)-th block
is at most \(C\min(\varepsilon2^l,1)\). Since
\[
 \sup_{l\ge0}2^{-l\delta}\min(\varepsilon2^l,1)
       \le C_\delta\varepsilon^{\tau}\quad(0<\varepsilon\le1),
 \tag{GS4}
\]
each difference multiplier in (GS3) maps
\(B^{\kappa'}_{2,\infty}\) to \(B^\kappa_{2,\infty}\) with norm
at most \(C\varepsilon^\tau\). To verify (GS4), split at
\(2^l=\varepsilon^{-1}\). Below it the expression is
\(\varepsilon2^{l(1-\delta)}\), at most
\(\varepsilon^\delta\) if \(\delta\le1\), and at most
\(\varepsilon\) otherwise. Above it the expression is
\(2^{-l\delta}\le\varepsilon^\delta\).

For \(u\in\mathcal A^{m'}\), \(m'<m\), the actual indices are
\(\kappa'=-m'-n/4\), \(\kappa=-m-n/4\), so
\(\delta=m-m'>0\). Subtract \(X_n^\ell u\) from (GS2). Its
\(j=0\) term is \((Q_\varepsilon-I)X_n^\ell u\), and all its
\(j\ge1\) terms have the mean-zero bounds in (GS3). Every input
\(D'^{\alpha'}X_n^{\ell-j}u\) has the same Besov index
\(\kappa'\), by the full definition (GA1). Consequently
\[
 \|D'^{\alpha'}X_n^\ell(Q_\varepsilon u-u)\|_{B^\kappa_{2,\infty}}
 \le C_{\alpha',\ell}\varepsilon^{\min(1,m-m')}
       \sum_{j=0}^\ell
       \|D'^{\alpha'}X_n^{\ell-j}u\|_{B^{\kappa'}_{2,\infty}}.
 \tag{GS5}
\]
Equations (GA2) and the full product rule now give every original
weighted derivative seminorm and every smooth-coefficient tangent word.
Thus \(Q_\varepsilon u\to u\) in \(\mathcal A^m\), not merely as an
ordinary weak distribution, with finite-seminorm control.

Finally choose the locally finite chart partition \(\varphi_j\) and
input cutoffs \(\psi_j=1\) near their supports from the included PS5 partition construction. In each
boundary chart use the positive convolution just proved; in interior
charts use a compact mollifier whose small translations remain interior.
Use the actual half-density and bundle coordinate maps on both sides.
Define
\[
 \mathcal Q_\varepsilon u
    =\sum_j\varphi_j Q^{(j)}_\varepsilon(\psi_j u).
 \tag{GS6}
\]
Choose each chart's convolution radius no larger than its fixed distance
from the cutoff support to the chart edge; a constant multiple of
\(\varepsilon\) in that chart suffices. On a fixed input compact set only
finitely many \(\psi_j\) occur, giving a single compact output set
\(K'\), independent of sufficiently small \(\varepsilon\). Smooth
multiplications and chart maps are continuous in (GA1). Since
\(\sum_j\varphi_j\psi_j u=u\), (GS5) and the full Leibniz rule prove
\[
 \mathcal Q_\varepsilon:\mathcal E'(X)\to C^\infty(X),\qquad
 \mathcal Q_\varepsilon u\longrightarrow u\text{ in }\mathcal A^m(X)
 \quad(u\in\mathcal A^{m'},\ m'<m).
 \tag{GS7}
\]
For compact input its output is compact and supported in the interior,
including in boundary charts. The convergence is uniform on bounded
sets of each fixed compact \(\mathcal A^{m'}\) source, by the displayed
finite-seminorm estimates. This proves the required support-preserving
smoothing lemma with its original order indices.

## 3. Dual distributions and boundary traces

### 3.1. The lowest test order and the dual class

Put \(m_0=-(n+2)/4\). In a boundary chart, let \(\phi(x',t)\) be smooth
up to \(t=0\), compactly supported for \(t\ge0\), and let \(H\phi\)
be its zero extension. Integrating its normal Fourier transform by parts
\(N\) times gives, for \(|\tau|\ge1\),
\[
 \widehat{H\phi}(x',\tau)
 =\sum_{j=0}^{N-1}\frac{\partial_t^j\phi(x',0)}{(i\tau)^{j+1}}
  +\frac{1}{(i\tau)^N}
       \int_0^\infty e^{-it\tau}\partial_t^N\phi(x',t)\,dt .
 \tag{GD1}
\]
Each displayed boundary jet, including its sign, follows from the lower
endpoint in integration by parts. The remainder and all its tangential
derivatives are bounded by the corresponding compact smooth seminorms.
For any requested number of frequency derivatives, first multiply by
powers of \(t\) under the integral and repeat the same integration by
parts with enough extra terms; this gives the full order-\(-1\)
symbol estimates. Multiplying by a cutoff equal to one for
\(|\tau|\ge2\) and absorbing the compact-frequency part into a smooth
amplitude yields the exact reduced conormal form (C16).
For codimension one its amplitude order is
\(m+(n-2)/4\); order \(-1\) means exactly
\(m=m_0\). If \(\phi(x',0)\ne0\), the first term in (GD1) is nonzero,
so a uniform claim of a lower conormal order is false. Hence
\[
 C_c^\infty(X)\hookrightarrow\mathcal A^m_c(X)
 \quad\text{continuously for every }m\ge m_0,
 \tag{GD2}
\]
where a smooth boundary function is represented by its zero extension.
The continuous inclusion for \(m>m_0\) is immediate from the symbol
orders or the dyadic Besov weights. Interior-supported smooth functions
belong to every order.

Define \(\mathcal A'(X)\) as the ambient supported distributions \(u\)
whose action on every compactly supported smooth boundary function is
continuous with respect to the \(\mathcal A^m\) topology, for every
\(m\ge m_0\). Precisely, for each compact \(K\subset X\) and each such
\(m\), finitely many defining seminorms \(p_{m,K,l}\) and a constant
give
\[
 |u(\phi)|\le C_{m,K}\sum_{l=1}^{L}p_{m,K,l}(H\phi)
 \quad(\operatorname{supp}\phi\subset K).
 \tag{GD3}
\]
The action is independent of an ambient smooth extension of \(\phi\):
two extensions agreeing on the closed half-space differ by a smooth
function vanishing on its interior and to every order at its boundary;
the supported distribution annihilates that difference. This is checked
in each chart and patched by a partition. The topology on
\(\mathcal A'\) used here is the weak topology generated by all
\(u\mapsto|u(v)|\) for compactly supported \(v\in\mathcal A\), where
\(\mathcal A=\bigcup_m\mathcal A^m\).

We prove that the pairing in (GD3) extends uniquely to every compactly
supported \(v\in\mathcal A^m\), \(m\ge m_0\). Choose \(m_1>m\).
The support-preserving \(\mathcal Q_\varepsilon v\) is smooth with support
in a fixed compact \(K'\), and (GS7) gives convergence in
\(\mathcal A^{m_1}\). The bound (GD3) at order \(m_1\) makes
\(u(\mathcal Q_\varepsilon v)\) converge. If another smooth sequence
converges to \(v\) in the same order, its difference has pairing tending
to zero by that bound, so the extension is unique. To show continuity
on \(\mathcal A^m_K\), use (GD3) at \(m_1\) on the approximants and
take the limit. The inclusion
\(\mathcal A^m_K\hookrightarrow\mathcal A^{m_1}_{K'}\) is continuous,
which supplies the finite \(\mathcal A^m\) bound. No convergence in the
same endpoint order \(m\) has been assumed. This constructs the full
pairing and the stated weak topology.

### 3.2. Interior restriction, absence of boundary-supported elements, density

If \(u\in\mathcal A'\) vanishes on all tests in the interior, then for
each compactly supported \(v\in\mathcal A^m\) choose
\(m_1>\max(m,m_0)\). Each \(\mathcal Q_\varepsilon v\) is smooth and
supported in the interior, so
\(u(\mathcal Q_\varepsilon v)=0\). The convergence in
\(\mathcal A^{m_1}\) and the extended continuity prove \(u(v)=0\).
Smooth boundary tests are among these \(v\), hence \(u=0\) as an
ambient distribution. Therefore
\[
 \mathcal A'(X)\longrightarrow\mathcal D'(X^\circ),
 \qquad u\longmapsto u|_{X^\circ}
 \quad\text{is injective}.
 \tag{GD4}
\]
In particular no nonzero distribution supported only on
\(\partial X\) belongs to \(\mathcal A'\). This follows from the exact
density argument, not from a mistaken identification of the two
distribution spaces.

Smooth boundary functions are weakly dense in \(\mathcal A'\).
First every smooth boundary function defines an element of
\(\mathcal A'\): on a compact test support, multiply that function by
a smooth compact cutoff and pair it with the supported conormal
distribution. In the normal form (C16), the compact smooth factor has
rapidly decreasing normal Fourier transform. Integrating the full
symbol amplitude against that transform bounds the pairing by finitely
many \(S^{m+(n-2)/4}\) seminorms for every real \(m\); the normal-form
topology comparison in (C16) gives the corresponding
\(\mathcal A^m\) bound. Interior terms use the ordinary distribution
pairing. Thus the smooth approximants below really belong to
\(\mathcal A'\).
For a compactly supported \(v\in\mathcal A\), define
\(u_\varepsilon(v)=u(\mathcal Q_\varepsilon v)\). The adjoint of each
local term in (GS6) is convolution with a compact smooth reflected
kernel, followed by smooth cutoffs and coordinate/half-density maps.
For a distribution \(u\), this adjoint is a smooth function of the
remaining variable, including at its boundary; on every compact set
only finitely many chart terms occur. Thus \(u_\varepsilon\) is
represented by a smooth function on \(X\). For each fixed \(v\) of
order \(m\), choose \(m_1>\max(m,m_0)\). By (GS7),
\(\mathcal Q_\varepsilon v\to v\) in \(\mathcal A^{m_1}\), and the
extended continuity gives
\[
 u_\varepsilon(v)=u(\mathcal Q_\varepsilon v)
       \longrightarrow u(v).
 \tag{GD5}
\]
This is weak density with the actual test topology, for every compact
conormal test. Together with (GD4), it identifies \(\mathcal A'\) with
its image of interior distributions; it does not make all interior
distributions members of \(\mathcal A'\).

### 3.3. The invariant boundary delta and trace

Let \(\varphi\) be a compactly supported smooth test density on
\(\partial X\), with the dual bundle coefficient when appropriate.
In a boundary chart define the supported distribution density
\[
 T\varphi=\varphi(x')\otimes\delta(t),\qquad
 \delta(t)=(2\pi)^{-1}\int_{\mathbb R}e^{it\tau}\,d\tau.
 \tag{GD6}
\]
For a new defining function \(\bar t=\alpha(x',t)t\),
\(\alpha(x',0)>0\), the exact distribution density law is
\(\delta(\bar t)|d\bar t|=\delta(t)|dt|\): the delta coefficient
contributes \(\alpha(x',0)^{-1}\) and the normal density contributes
\(\alpha(x',0)\). The tangential density and bundle transitions are
the usual ones. Hence \(T\) is intrinsic, not a choice of boundary
coordinate or a half-density shortcut.

The original Fourier amplitude in (GD6) is constant in \(\tau\), with
the exact coefficient \((2\pi)^{-1}\varphi(x')\). Formula (C16) for
codimension one therefore gives
\(m+(n-2)/4=0\), that is,
\[
 T:C_c^\infty(\partial X;E^*\otimes\Omega_{\partial X})
       \longrightarrow
       \mathcal A^{(2-n)/4}_c(X;E^*\otimes\Omega_X)
 \quad\text{continuously}.
 \tag{GD7}
\]
The direct Besov estimate uses the same dyadic amplitude bound, so the
target topology is included. Define the boundary restriction by
\[
 \langle u|_{\partial X},\varphi\rangle=u(T\varphi),
 \qquad u\in\mathcal A'(X).
 \tag{GD8}
\]
The exact conormal order in (GD7) lies above \(m_0\), so the extended
pairing is available. Its continuity in \(\varphi\) follows from
(GD3) and (GD7), and its weak continuity in \(u\) is one of the
defining seminorms of \(\mathcal A'\). Thus (GD8) is a distribution on
the boundary.

For a smooth function \(u\) up to the boundary, use the positive normal
convolution on \(T\varphi\). It is a unit-mass smooth approximate delta
supported at positive normal distance \(O(\varepsilon)\). Consequently
\(u(\mathcal Q_\varepsilon T\varphi)\) tends to
\(\int_{\partial X}u(x',0)\varphi(x')\), with the full chart density
factor. The extension of the pairing in Section 3.1 gives the same limit
for \(u(T\varphi)\). Hence (GD8) agrees with ordinary smooth
restriction. Its uniqueness among weakly continuous trace maps follows
from (GD5).

### 3.4. Corrected differentiation with its exact sign

Let \(u\in\mathcal A'(\overline{\mathbb R}{}^n_+)\), represented as an
ambient distribution supported in the closed half-space. Write
\(u_\partial=u|_{x_n=0}\) from (GD8). Define
\[
 \nabla_j^\mathrm{int}u
   :=D_j u+i\delta_{jn}\,u_\partial\otimes\delta(x_n).
 \tag{GD9}
\]
This is the original ambient derivative plus its full boundary delta
correction, with no suppression of either term. The sign follows first
for a smooth \(u\) from
\[
 D_n(Hu) = H(D_nu)-i\,u(x',0)\otimes\delta(x_n),
 \qquad
 D_j(Hu)=H(D_ju)\quad(j<n).
 \tag{GD10}
\]
Both identities are direct distributional product rules, since
\(D_nH=-i\delta\). Adding the term in (GD9) makes
\(\nabla_j^\mathrm{int}u\) the supported representative of the
ordinary interior derivative for smooth \(u\).

We prove membership in \(\mathcal A'\) for general \(u\). Let \(\phi\)
be a compact smooth boundary test, and distinguish its ambient smooth
extension from its supported zero extension \(H\phi\). In the
\(\mathcal A'\) pairing, \(u(-D_j\phi)\) is the pairing with the zero
extension of \(-D_j\phi\). The full distribution identity is
\[
 -D_j(H\phi)
     =H(-D_j\phi)+i\delta_{jn}\,
                         \phi(x',0)\otimes\delta(x_n).
 \tag{GD11}
\]
Therefore the two terms in (GD9) combine exactly to
\[
 (\nabla_j^\mathrm{int}u)(\phi)
   =u\bigl(-D_j(H\phi)\bigr).
 \tag{GD12}
\]
The ordinary differential map
\(D_j:\mathcal A^m_K\to\mathcal A^{m+1}_{K}\) is continuous: the
normal derivative multiplies the full conormal amplitude by \(\tau\)
and differentiates its smooth base coefficient, while tangential
derivatives differentiate that coefficient; (C4)–(C5) control all
remainders. Equivalently it is the exact order-one conormal map (C17)
with compact support. If \(m\ge m_0\), then \(m+1\ge m_0\), so
(GD12) and the defining estimate at order \(m+1\) show that
\(\nabla_j^\mathrm{int}u\in\mathcal A'\). The map is weakly continuous:
for each compact conormal test \(v\), its defining functional is
\(u\mapsto u(-D_jv)\), another test in \(\mathcal A\).
In the interior the delta term vanishes, so
\((\nabla_j^\mathrm{int}u)|_{X^\circ}=D_j(u|_{X^\circ})\).

The uncorrected derivative can fail to lie in \(\mathcal A'\). For
example choose a smooth \(u\) with nonzero boundary value. By (GD10)
the ambient derivative contains the nonzero boundary-supported term
\(-i u_\partial\delta\), while \(H(D_nu)\) is in \(\mathcal A'\).
If \(D_n(Hu)\) were in \(\mathcal A'\), subtracting
\(H(D_nu)\) would put a nonzero boundary-supported distribution in
\(\mathcal A'\), contradicting (GD4). This proves the distinction,
rather than treating the two derivatives as identical presentations.

## 4. Multiplication, intrinsic jets and their distributional meaning

Multiplication by a smooth coefficient preserves every local supported conormal order: commute the coefficient through each tangent word and use the Besov multiplier bound. It consequently preserves the dual class, since the dual pairing with a conormal test \(v\) becomes the original pairing with the same coefficient times \(v\). This action is weakly continuous and agrees with ordinary interior multiplication. The boundary trace satisfies \((au)|_{\partial X}=a|_{\partial X}\,u|_{\partial X}\), since multiplication of \(a\) with \(T\varphi\) in (GD6) evaluates its boundary value.

The intrinsic derivatives commute, and obey the ordinary product rule with these coefficients. Both assertions hold after interior restriction by distributional differentiation; each side belongs to the dual class by (GD12) and the multiplier statement, so injectivity (GD4) proves the equalities of their actual supported representatives. The same argument proves that a smooth vector field acts intrinsically in any chart and transforms by the ordinary chain rule. Its iterates have the weakly continuous traces just constructed. None of these assertions identifies a raw ambient derivative with the corrected derivative (GD9).
