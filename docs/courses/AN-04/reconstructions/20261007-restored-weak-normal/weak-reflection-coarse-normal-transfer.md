# A coarse normalized normal bound away from glancing

This is an owner receiving use of the complete U057–U062 providers. It does
not invoke glancing normal smallness or establish a positive commutator.
All assumptions about uniform families include their full off-microsupport
rapid-decay and residual topology.

All norms and equation tests use the fixed compact-patch convention in U067, Section 1. This is only a domain convention; the analytic bound below uses the earlier providers stated here.

Keep the full weak wave form (GN1)–(GN3), with either \(V=H^1_0\) or \(H^1\)
and its actual antidual. Let \(B_r\) have uniform target b-order \(s+1\),
common proper compact kernel support in a fixed time-elliptic compact cone
\(K\), and individual order at most zero. All derivatives appearing below
are legal for each \(r>0\). Assume elliptic solution and forcing testers on
a larger neighborhood of \(K\), of orders \(s-1/2\) and \(s+1/2\), respectively:
\[
 X=\|u\|_V+\|Q_-u\|_V,\quad
 Y=\|f\|_{V^*}+\|Q_ff\|_{V^*},\quad Z^2=X^2+Y^2<\infty .
 \tag{CN1}
\]
A source tester of order \(s+1\) supplies the smaller source order by U058.
For an induction step with \(s\le1/2\), the nonpositive lower solution order
is supplied by the background energy norm.

Choose \(T\in\Psi_b^{-1}\) with time principal symbol \(\tau^{-1}\) near
\(K\), and \(D_tT=I+E\) there, where the actual order-minus-one discrepancy
is retained if an exact microlocal time inverse is not selected. Its full
microsupport stays in the fixed larger cone. Set \(A_r=TB_r\), of target
order \(s\). The already proved sharp form defect and source estimate
U059 (SF17), followed by the lower-term bound in U060 Section 3, give
\[
 \kappa\|D_{\mathrm{sp}}A_ru\|^2
       \le \|D_tA_ru\|^2+C Z^2 .
 \tag{CN2}
\]
This is U060 (GN13). Its proof uses the positivity of \(G\), the full form
identity, the balanced-pair estimate and the two norms in (CN1). It uses
neither the anchor relation (GN4), the small number (GN6), nor the freezing
estimate (GN14). It therefore applies on this time-elliptic compact cone
without a glancing hypothesis. All complex lower matrices remain in its
lower constant, and the weak Neumann antidual remains the original one.

The exact \(D_tT\) composition gives
\[
 D_tA_ru=B_ru+E B_ru,\qquad
 \|E B_ru\|+\|A_ru\|\le C X .
 \tag{CN3}
\]
Indeed \(EB_r\) has zero-derivative coefficient order at most \(s\), and
\(A_r\) has that same order. In U059's mixed notation each belongs to
\(\mathcal M_{s-1}\); the solution tester of order \(s-1/2\) supplies their
\(L^2\) values by (SF5) and downward transfer. If \(E\) is only microlocally
order minus one, separate its order-zero piece off \(K\); U058 makes its
composition with \(B_r\) uniformly residual. This piece has the same bound.

The full normal commutator of \(T\) is
\[
 [D_x,T]=U+W D_x,\qquad
 U\in\Psi_b^{-1},\quad W\in\Psi_b^{-2}.
 \tag{CN4}
\]
Consequently \([D_x,T]B_r\in\mathcal M_{s-1}\), including every composition
and normal-commutator remainder: expand
\(D_xB_r=B_rD_x+U_r+W_rD_x\), with coefficient orders \(s+1,s\).
The coefficients after left multiplication by \(W\) have orders \(s-1,s\),
and \(UB_r\) has zero-derivative order \(s\). Thus (SF5) gives
\[
 \|[D_x,T]B_ru\|\le C X .
 \tag{CN5}
\]
Use \(T D_xB_ru=D_xA_ru-[D_x,T]B_ru\), (CN2) and (CN3).
Cauchy–Schwarz and the elementary squared triangle bound give
\[
 \|T D_xB_ru\|^2+\|TB_ru\|_V^2
          \le C_N\|B_ru\|^2+C_{\mathrm{low}}Z^2 .
 \tag{CN6}
\]
One may choose \(C_N\) from \(\kappa\) and fixed time/cotangent cutoffs,
independently of subsequent geometric widths. At fixed widths, full family
seminorms and all actual lower remainders enter \(C_{\mathrm{low}}\);
that constant need not remain bounded as widths shrink.

This bound supplies the two normalized normal factors needed to estimate
small hyperbolic coefficient errors. Its leading coefficient has no
glancing smallness factor. A positive hyperbolic commutator still must make
its zero-, linear- and quadratic-normal *coefficient* norms sufficiently
small, keep its weak-equation multiplier and full matrix lower form, and
establish the sharp source trade separately.

Exact unchanged providers are:
[U059, Sections 3–5, SF5/SF17](../20261007-restored-sharp-form/sharp-boundary-form-defect.md),
U060, Section 3, GN13,
[U058 uniform microsupport](../20261007-restored-uniform-microsupport/uniform-microsupport-and-dual-sources.md),
and the actual normal-commutator calculus cited by
U062, WC6.
These complete proofs are used directly. Original eligible receiving
expression is CC0-1.0; approved source routes remain valid.
