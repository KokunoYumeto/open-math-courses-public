# Compatible modular weights and the full positive cone

A modular flow can signal the existence of an operator-valued weight,
but equality on a finite GNS ideal does not determine what happens at
infinite scalar values. The construction here descends a trace-case map
through two compatible crossed products. A single positive spectral
density and an onto extended-positive average make the descent work on
every positive input. Inner products are linear in the first variable.

## The reconstruction statement and its exact inputs

Let \(N\subset M\) be a unital inclusion of von Neumann algebras,
with no countability assumption. Let \(\varphi\) on \(N\) and
\(\psi\) on \(M\) be faithful normal semifinite weights. Suppose

\[
\sigma_t^\psi(n)=\sigma_t^\varphi(n).
\tag{OE.1}
\]

Here \(n\in N\) and \(t\in\mathbb R\).
The target is a unique faithful normal semifinite operator-valued
weight \(E:M_+\to\widehat N_+\) with

\[
\psi(x)=\widehat\varphi(E(x))
\quad(x\in M_+).
\tag{OE.2}
\]

The equality is in \([0,\infty]\), so (OE.2) includes positive
operators of infinite \(\psi\)-weight. The converse says that an
existing faithful normal semifinite \(E\), composed with any faithful
normal semifinite \(\varphi\), produces a compatible pair.

Four exact external contracts remain visible. Scalar harmonic facts
supply vector-valued real-line Plancherel, compact approximate
identities, and the Weyl commutant. Forward modular restriction is
used only for an **already existing** faithful normal semifinite
operator-valued weight. The all-normal trace representation includes
weights with an infinite part. Positive Tonelli governs the normal
extensions of the dual orbit integrals. These four inputs are not proved
in these lessons. The normal extension
and full range
of a faithful normal semifinite operator-valued weight are treated in a
separate lesson.
None of these providers is the theorem (OE.2) or the false
all-positive reverse implication of IX.4.20.

## A concrete common crossed-product pair

Represent \(M\) faithfully and normally on the GNS space of
\(\psi\). Put \(U_t=\Delta_\psi^{it}\), so
\(U_t mU_t^*=\sigma_t^\psi(m)\). On
\(\mathcal H=L^2(\mathbb R,H_\psi)\), define

\[
\begin{aligned}
(\pi(m)\xi)(r)&=U_{-r}mU_r\xi(r),\\
(\lambda(t)\xi)(r)&=\xi(r-t),\\
(D_s\xi)(r)&=e^{-isr}\xi(r).
\end{aligned}
\tag{OE.3}
\]

Equation (OE.1) makes this the same regular action for \(N\).
Set

\[
\begin{gathered}
P=(\pi(M),\lambda(\mathbb R))'',\\
Q=(\pi(N),\lambda(\mathbb R))''\subset P.
\end{gathered}
\tag{OE.4}
\]

The unitary field \((V\xi)(r)=U_r\xi(r)\) conjugates \(\pi(m)\)
to the constant operator \(m\otimes1\); in particular both
representations in (OE.4) are faithful and normal. Conjugation by
\(D_s\) defines the shared dual action \(\theta_s\), with
\(\theta_s(\pi(m))=\pi(m)\) and
\(\theta_s(\lambda(t))=e^{-ist}\lambda(t)\).

Here is the fixed-point check that the descent needs. The operators
\((R_t\xi)(r)=\xi(r+t)\) and
\((V_t\xi)(r)=U_t\xi(r+t)\) are related by
\(VV_tV^*=1\otimes R_t\). Each \(V_t\) commutes with \(P\).
If \(X\in P\) is fixed by every \(\theta_s\), then \(VXV^*\)
commutes with all multiplication phases \(1\otimes D_s\) and all
translations \(1\otimes R_t\). Their Weyl commutant is scalar on the
second tensor factor, so \(VXV^*=a\otimes1\). It also commutes with
the conjugates of constant \(M'\)-operators. At the continuous fiber
\(r=0\) this gives \(a\in M''=M\). Thus \(P^\theta=\pi(M)\), and
the same argument gives \(Q^\theta=\pi(N)\). Applying it to the
spectral projections and infinite-part projection of an extended
positive element gives the corresponding fixed-point identities in
\(\widehat P_+\) and \(\widehat Q_+\).

## Dual averages and one normalized trace density

For \(X\in P_+\), integrate its positive dual orbit:

\[
T_P(X)=\int_{\mathbb R}\theta_s(X)\,ds.
\tag{OE.5}
\]

The integral lies in \(\widehat M_+\).
The integral is the increasing supremum of compact-interval
integrals, evaluated on positive normal functionals. The fixed-point
result of OE-02 places it in the displayed cone. Interchanging two
positive suprema proves normality; invariance of the orbit integral
proves \(M\)-bimodularity. A continuous nonnegative orbit with zero
integral vanishes at zero, so \(T_P\) is faithful. The same
construction gives \(T_Q:Q_+\to\widehat N_+\).

For \(f\in C_c(\mathbb R)\), vector-valued Plancherel with the
Lebesgue convention in (OE.5) gives

\[
T_P(\lambda(f)^*\lambda(f))
=2\pi\|f\|_2^2 1.
\tag{OE.6}
\]

The coefficient vectors \(\lambda(f)m\) span an ultraweakly dense
subspace of \(P\). Equation (OE.6), bimodularity, and finite
\(\psi\)-cutdowns show that \(T_P\) and
\(W_P=\widehat\psi\circ T_P\) are semifinite. The same holds for
\(T_Q\) and \(W_Q=\widehat\varphi\circ T_Q\). Their normality and
faithfulness follow directly from the orbit construction and the
scalar weights. This reasoning works with arbitrary Hilbert-space
multiplicity: a single compactly supported vector orbit has a
separable closed span, where scalar Plancherel applies coordinatewise.

The forward modular restriction contract, applied only to the
**existing** \(T_P\) and \(T_Q\), identifies the modular actions of
\(W_P,W_Q\) on \(M,N\). The dual action commutes with
\(\operatorname{Ad}\lambda(t)\): its scalar phase on \(\lambda(t)\)
cancels under conjugation. Moving this conjugation through the
positive orbit integral, and restricting it to the fixed algebra, gives

\[
 T_P(\lambda(t)X\lambda(t)^*)
   =\widehat{\sigma_t^\psi}(T_P(X)).
\]

Here the hat denotes the action on the extended positive cone of
\(M\). It is covariance, and need not be invariance. Modular
invariance of \(\psi\), also on its extended cone, now gives

\[
 W_P(\lambda(t)X\lambda(t)^*)
  =\widehat\psi\bigl(\widehat{\sigma_t^\psi}(T_P(X))\bigr)
  =W_P(X).
\]

The same two steps hold for \(Q\), with \(\varphi\) in place of
\(\psi\). Thus it is the scalar weights \(W_P,W_Q\) that are
invariant under each inner conjugation. Their unitary centralizer
criterion puts every \(\lambda(t)\) in both scalar centralizers.
Generation of \(P,Q\) therefore yields
\(\sigma_t^{W_P}=\operatorname{Ad}\lambda(t)\) and the analogous
formula for \(W_Q\). Inverse centralizer-density perturbation then
constructs uniquely normalized faithful normal semifinite traces
\(\tau_P,\tau_Q\) such that

\[
\begin{gathered}
\bigl[DW_P:D\tau_P\bigr]_t=\lambda(t),\\
\bigl[DW_Q:D\tau_Q\bigr]_t=\lambda(t).
\end{gathered}
\tag{OE.7}
\]

Both traces obey \(\tau\circ\theta_s=e^{-s}\tau\). To see the sign,
let \(h\) be the positive injective affiliated operator with
\(h^{it}=\lambda(t)\). The dual action has
\(\theta_s(h)=e^{-s}h\). Perturbing the dual-invariant \(W\) by
\(h^{-1}\) gives the trace and the displayed scaling. A direct
Fourier check for \(M=\mathbb C\) gives
\(h(p)=e^{-p}\) and \(\tau(F)=\int e^pF(p)\,dp\), whose translated
weight scales by \(e^{-s}\). The normalization in (OE.7) is stronger
than mere equality of modular automorphism groups.

## Tracial induction without a semifinite restriction

For arbitrary semifinite \(Q\subset P\) with faithful normal
semifinite traces \(\tau_Q,\tau_P\), define for \(X\in P_+\) a
normal weight on \(Q\) by

\[
\chi_X(y)=\tau_P(y^{1/2}Xy^{1/2}).
\tag{OE.8}
\]

Here \(y\in Q_+\).
This weight can be nonsemifinite even when both traces are
semifinite. For example, the usual trace of \(1\) on
\(B(\ell^2)\) is infinite when restricted to \(\mathbb C1\).
The **all-normal** trace representation therefore supplies a unique
\(S(X)\in\widehat Q_+\) with

\[
\begin{gathered}
\widehat\tau_Q(S(X)\mathbin{\cdot}y)\\
=\chi_X(y).
\end{gathered}
\tag{OE.9}
\]

This holds for every \(y\in Q_+\).
The dot denotes extended-positive trace pairing; it is not an
ordinary product with a possibly unbounded operator.

Uniqueness in (OE.9) transfers additivity and homogeneity in \(X\)
to \(S\). Normality follows by swapping the supremum of an
increasing positive net with the normal trace pairing. For
\(a\in Q\), cyclicity in the pairing shows
\(\chi_{a^*Xa}(y)=\chi_X(aya^*)\); hence
\(S(a^*Xa)=a^*S(X)a\). Setting \(y=1\) in (OE.9) gives

\[
\widehat\tau_Q(S(X))=\tau_P(X).
\tag{OE.10}
\]

This identity holds on all \(P_+\).
Thus \(S\) is faithful. To verify semifiniteness, start with
\(\tau_P(X)<\infty\). The infinite spectral projection of
\(S(X)\) vanishes. Its bounded spectral cuts \(q_k\in Q\)
increase strongly to \(1\), and
\(S(q_kXq_k)=q_kS(X)q_k\in Q_+\). These compressions converge
ultraweakly to \(X\). The finite \(\tau_P\)-cone is ultraweakly
dense, proving that the bounded-output domain of \(S\) is dense.
No increasing-compression assertion is needed.

The same pairing proves uniqueness among trace-preserving normal
operator-valued weights. Applied to the \(P,Q\) of OE-02 and their
scaling traces, it also gives equivariance:

\[
S\theta_s^P=\theta_s^Q S.
\tag{OE.11}
\]

Indeed \(\theta_{-s}^Q S\theta_s^P\) has the same scalar trace
identity (OE.10), because the two trace-scaling factors cancel.
Consequently \(S(\pi(M)_+)\subset\widehat N_+\): equivariance
fixes every spectral projection of the output. Define
\(E=S|_{M_+}\), identifying \(M,N\) with their images under
\(\pi\). It is normal and \(N\)-bimodular.

## The equality at infinity

The shared \(\lambda(t)\in Q\subset P\) has one spectral generator
\(h\), not two unrelated affiliated densities. In both algebras,
(OE.7) and the fixed-reference cocycle theorem identify the entire
scalar weights as \(W_P=(\tau_P)_h\) and
\(W_Q=(\tau_Q)_h\). Let \(h_k=h\wedge k\in Q_+\), and write
\(C_k(Z)=h_k^{1/2}Zh_k^{1/2}\) on either algebra's positive cone.
Normality of the density perturbations, \(Q\)-bimodularity of
\(S\), and (OE.10) give, for every \(X\in P_+\),

\[
\begin{gathered}
\widehat W_Q(S(X))\\
=\sup_k\widehat\tau_Q(C_k(S(X)))\\
=\sup_k\tau_P(C_k(X))\\
=W_P(X).
\end{gathered}
\tag{OE.12}
\]

Every equality is in \([0,\infty]\). The spectral cuts turn an
unbounded density into bounded bimodule sandwiches; they do not
require trace measurability or finite scalar values.

Write bars for the normal extensions to extended positive cones.
Positive Tonelli applied to (OE.5) and equivariance (OE.11) gives
the commutative descent square

\[
\begin{gathered}
\overline S\,\overline T_P
=\overline T_Q\,\overline S
\quad\text{on }\widehat P_+.
\end{gathered}
\tag{OE.13}
\]

For precision, this means equality after evaluation by every
positive normal functional on \(Q\): both sides integrate the same
nonnegative dual-orbit pairing. The canonical embeddings
\(\widehat M_+\hookrightarrow\widehat P_+\) and
\(\widehat N_+\hookrightarrow\widehat Q_+\) are the fixed-point
spectral-pair embeddings of OE-02.

The public full-range proof
for a faithful normal semifinite operator-valued weight says
\(\overline T_P(\widehat P_+)=\widehat M_+\). It starts
with the ultraweakly dense finite-output ideal, gives each positive
output in that ideal a positive bounded-input lift by bimodule
factorization, resolves \(1\) by a possibly uncountable family of
such outputs, and then lifts spectral increments of an arbitrary
extended positive target. That public proof remains under review;
it cannot be replaced by a countable analytic test on the finite cone.

Take **any** \(y\in M_+\), including \(\psi(y)=\infty\), and
choose \(X\in\widehat P_+\) with
\(\overline T_P(X)=y\). Normal extension of (OE.12) and the
square (OE.13) then give

\[
\begin{gathered}
\psi(y)=\widehat W_P(X)\\
=\widehat W_Q(\overline S X)\\
=\widehat\varphi(E(y)).
\end{gathered}
\tag{OE.14}
\]

This is (OE.2) on the **whole** positive cone. It uses an onto lift
at the infinite values; the finite-GNS reverse calculation in
IX.4.20 does not provide one.

## Faithfulness, semifiniteness, and direct uniqueness

Equation (OE.14) and faithfulness of \(\psi\) make \(E\) faithful.
For semifiniteness, take \(y\in M_+\) with
\(\psi(y)<\infty\). Then \(E(y)\) has no infinite spectral part.
If \(q_k=1_{[0,k]}(E(y))\), the bimodule rule gives
\(E(q_kyq_k)=q_kE(y)q_k\in N_+\), and \(q_kyq_k\to y\)
ultraweakly. The finite \(\psi\)-cone itself is ultraweakly dense:
finite-weight positive contractions \(e_i\uparrow1\) strongly give
\(e_iye_i\to y\) and
\(\psi(e_iye_i)\leq\|y\|\psi(e_i^2)<\infty\).
Hence the bounded-output domain of \(E\) is ultraweakly dense.
The compressions are not asserted to increase.

Suppose \(E_1,E_2\) both satisfy (OE.2) for the same
\(\varphi,\psi\). For \(c\in\mathfrak n_\varphi\), their bimodule
identities imply

\[
\begin{gathered}
\widehat\varphi(c^*E_1(y)c)
=\psi(c^*yc)\\
=\widehat\varphi(c^*E_2(y)c)
\quad(y\in M_+).
\end{gathered}
\tag{OE.15}
\]

These are the extended quadratic forms of \(E_1(y)\) and
\(E_2(y)\) on the dense left \(N\)-module
\(\Lambda_\varphi(\mathfrak n_\varphi)\). To see why this domain
suffices, take the finite-energy spectral projections of either
form. Their bounded cuts send this module into its finite form
domain, where form norm is bounded by a multiple of Hilbert norm.
The cuts approximate every finite-energy vector in form norm, so
the finite part of this module is a form core. Equality in
(OE.15), including infinite values, gives the same core and the
same closed form. Extended-positive spectral-pair uniqueness
therefore gives \(E_1(y)=E_2(y)\) for every \(y\).

For the converse direction, start with an existing faithful normal
semifinite \(E\), choose faithful normal semifinite \(\varphi\),
and put \(\psi=\widehat\varphi\circ E\). Scalar cutdowns show
\(\psi\) is normal faithful semifinite. The forward modular
restriction theorem for this **existing** \(E\) gives (OE.1).
It does not use compatible-pair reconstruction.

## Dependency and source boundary

The theorem proved by the chain OE-02–06 is relative to its named
providers. The concrete averages, trace case, common-density
argument, full-range lift, and form-core uniqueness are displayed
because each controls a different possible loss of an infinite
value. The all-normal trace representation is stronger than the
semifinite-density statement in PT-08. The public OVW-03 full-range property is stronger than density
of the bounded-output ideal. The positive
Tonelli identity is an identity of **extended** maps, not only of
ordinary bounded operators. Until the exact providers and their
transitive foundations receive public proof or admitted imports,
OE-01 is a complete author-side draft **relative to those contracts**,
not an internally closed or admitted B9 theorem.

The target statement is Takesaki, *Theory of Operator Algebras II*,
IX.4 Theorem 4.18, printed p. 223/PDF p. 243; its printed proof
continues on pp. 225–227/PDF pp. 245–247. This course route uses
the trace construction of Haagerup, *Operator Valued Weights in von
Neumann Algebras* I, Theorems 1.12, 2.7 and 4.7(1), and II,
Theorem 5.1/Lemma 5.2. IX.4.20 has a false all-positive reverse
implication, corrected in What the analytic strong sum actually proves through Analytic rank-one operators with the wrong infinite value.
Nothing in OE-05 invokes that reverse. The argument does not import
the converse modular theorem that would presuppose OE-01.

The original mechanism figure for the shared density and onto square is retained as a reproducible private figure pending a separate public figure review. The exact primary pages, source identities, and open dependency boundaries are recorded in the course source audit.