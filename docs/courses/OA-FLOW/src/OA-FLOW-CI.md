# Closed conjugate-linear involutions from their graph Hilbert space

*Fresh local proof by GPT-6 Astra (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights in this new exposition.*

All Hilbert spaces are arbitrary, and inner products are linear in the first variable. We use completeness and the locally proved projection, Hilbert representation and bounded adjoint facts in [SF-0/SB-0](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-0), and the bounded and unbounded spectral calculus, with its exact domains, proved in SB-1–SB-6 there. No closed-form representation theorem, unbounded polar-decomposition theorem, normal-weight characterization or modular theorem is an input. The earlier Hilbert facts are [SF-0](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-0) and [SB-0](OA-FLOW-SF.md#OA-FLOW.SF.SB0); the full spectral-domain proof is [SB-1–SB-6](OA-FLOW-SF.md#OA-FLOW.SF.SB1). Scalar spectral convergence uses [SC-04–05](OA-FLOW-SC.md#sc-04).

The graph-Hilbert-space approach has a freely accessible human antecedent in [Masuda, Theorem 3.7, printed pp.42–43](https://www.math.okayama-u.ac.jp/mjou/mjou60/_02_Masuda.pdf#page=6). The proof below constructs the needed unitary directly, keeps its source and target spaces distinct, and verifies every unbounded domain. It proves the result for every closed densely defined conjugate-linear involution, without an algebra hypothesis.

<a id="oa-flow.ci.1"></a>

## CI-1. Adjoint and graph facts

For a Hilbert space \(K\), let \(\overline K\) have elements \(c y\), scalar multiplication \(\alpha(cy)=c(\overline\alpha y)\), and inner product \(\langle cy,cz\rangle_{\overline K}=\langle z,y\rangle_K\). The map \(c:K\to\overline K\) is a surjective conjugate-linear isometry.

Let \(T:D(T)\subseteq H\to K\) be densely defined and conjugate-linear, with complex-linear domain. The map \(A=cT:H\to\overline K\) is linear. A vector \(y\in K\) belongs to \(D(T^*)\) precisely when there is \(z\in H\) such that
\[
\langle Tx,y\rangle=\langle z,x\rangle\quad(x\in D(T));
\qquad T^*y=z.
\tag{CI1}
\]
Density makes \(z\) unique. Hilbert representation shows that existence is equivalent to boundedness of the displayed scalar pairing in \(\|x\|\). It gives \(T^*=A^*c\) and \(D(T^*)=c^{-1}D(A^*)\).

For clarity, the linear graph argument establishing the adjoint facts is short. The adjoint identity gives
\[
\Gamma(A)^\perp=\{(-A^*w,w):w\in D(A^*)\}.
\tag{CI2}
\]
Indeed the inner product of \((x,Ax)\) with \((z,w)\) vanishes exactly when \(\langle Ax,w\rangle=-\langle x,z\rangle\). A vector \(v\) is orthogonal to \(D(A^*)\) exactly when \((0,v)\in\overline{\Gamma(A)}\). Thus \(A\) is closable exactly when \(D(A^*)\) is dense: the closure of the graph is the graph of an operator exactly when its vertical part is zero. The adjoint graph is closed by passing to the limit in each scalar pairing. Applying (CI2) twice and taking orthogonal complements gives \(A^{**}=\overline A\) when \(A\) is closable. Conjugating source and target gives the same conclusions for \(T\): \(T^*\) is closed, it is densely defined when \(T\) is closable, and \(T^{**}=\overline T\). The conjugation maps are isometries, so they preserve graph closures.

Suppose now that \(S_0:D_0\to D_0\) is a densely defined closable conjugate-linear involution. Its graph is invariant under swapping its two coordinates. The same holds for the graph of its closure \(S\). Consequently
\[
S(D(S))=D(S),\qquad S^2x=x\quad(x\in D(S)).
\tag{CI3}
\]
In particular \(S\) is injective and has dense range. A vector \(x\) lies in \(D(S)\) exactly when a sequence \(x_n\in D_0\) converges to \(x\) and \(S_0x_n\) is Cauchy; in that case \(Sx=\lim_nS_0x_n\). One implication is the definition of graph closure in a metric space. For the other, completeness gives a limit of the Cauchy images and closedness puts the limiting pair in the graph. Thus \(D_0\) is a core for the entire closed graph.

<a id="oa-flow.ci.2"></a>

## CI-2. A bounded positive contraction encodes the involution

Equip \(V=D(S)\) with
\[
\langle v,w\rangle_V=\langle v,w\rangle_H+\langle Sw,Sv\rangle_H.
\tag{CI4}
\]
This is a linear-first inner product. A Cauchy sequence gives convergent vectors and images in \(H\); closedness of \(S\) identifies the limit, so \(V\) is complete. On this new Hilbert space, \(K v=Sv\) is a surjective conjugate-linear isometry with \(K^2=I\). Let \(j:V\to H\) be inclusion and put \(R=j^*j\). Then \(0\leq R\leq I\), \(R\) is injective, and
\[
KRK=I-R.
\tag{CI5}
\]
To verify the last equality, use antiunitarity of \(K\):
\(\langle KRKv,w\rangle_V=\langle Kw,RKv\rangle_V
=\langle Sw,Sv\rangle_H
=\langle v,w\rangle_V-\langle v,w\rangle_H\).
Also \(I-R\) is injective, since its quadratic value at \(v\) is \(\|Sv\|^2\).

Define initially
\[
U(R^{1/2}v)=jv\qquad(v\in V).
\tag{CI6}
\]
This is well defined and isometric because
\(\|R^{1/2}v\|_V^2=\langle Rv,v\rangle_V=\|jv\|_H^2\).
Injectivity of \(R\) makes its square-root range dense in \(V\), and \(j(V)\) is dense in \(H\). The extension is therefore a unitary \(U:V\to H\). In particular
\[
j=UR^{1/2}.
\tag{CI7}
\]
This constructs the only bounded polar factor needed; it does not import polar decomposition.

<a id="oa-flow.ci.3"></a>

## CI-3. Full polar data and exact domains

The spectral measure of \(R\) has no mass at \(0\) or \(1\), by the two injectivity statements. Define on \(V\)
\[
L=\frac{1-R}{R},
\]
using the Borel function \((1-t)/t\) on \(0<t<1\), and put
\[
\Delta=ULU^*,\qquad J=UKU^*.
\tag{CI8}
\]
Here \(\Delta\) is positive injective self-adjoint, and \(J\) is an antiunitary involution. Since
\[
1+\frac{1-t}{t}=\frac1t,
\]
the exact spectral-domain criterion gives
\[
D(L^{1/2})=\operatorname{Ran}R^{1/2},\qquad
D(\Delta^{1/2})=U\operatorname{Ran}R^{1/2}=j(V)=D(S).
\tag{CI9}
\]
To check the range statement explicitly, \(w=R^{1/2}v\) gives integrability of \(t^{-1}\) against the spectral measure of \(w\). Conversely that integrability defines \(v=R^{-1/2}w\) and gives \(R^{1/2}v=w\). There is no inverse outside its actual domain.

The real functional-calculus consequence of (CI5) is
\(K(1-R)^{1/2}=R^{1/2}K\). For \(v\in V\), the bounded scalar product \(L^{1/2}R^{1/2}=(1-R)^{1/2}\) is valid on all \(V\). Therefore
\[
J\Delta^{1/2}jv
=UKL^{1/2}R^{1/2}v
=UK(1-R)^{1/2}v
=UR^{1/2}Kv
=jKv=Sv.
\tag{CI10}
\]
Together with (CI9), this proves \(S=J\Delta^{1/2}\) with equality of domains.

Antiunitary spectral transport in (CI5) replaces \(t\) by \(1-t\) and conjugates the scalar function. Applied to the real function \((1-t)/t\), it gives
\[
J\Delta J=\Delta^{-1}.
\tag{CI11}
\]
Both sides have the spectral domain specified by the reciprocal function; the equality is not cancellation of unbounded products. More generally, for every \(z\in\mathbb C\),
\[
J\Delta^zJ=\Delta^{-\overline z},
\tag{CI12}
\]
including equality of the domains after applying \(J\).

Write \(A=\Delta^{1/2}\). Formula (CI1) applied to \(S=JA\) shows
\[
F:=S^*=AJ=JA^{-1},\qquad D(F)=D(A^{-1}).
\tag{CI13}
\]
Indeed \(y\) is in the adjoint domain exactly when \(Jy\in D(A)\); then the scalar pairing is represented by \(AJy\). The spectral relation \(JAJ=A^{-1}\) identifies this domain with \(D(A^{-1})\). It follows with exact product domains that
\[
FS=A^2=\Delta,\qquad SF=A^{-2}=\Delta^{-1},\qquad F^2=I.
\tag{CI14}
\]
For example, \(v\in D(FS)\) means \(v\in D(A)\) and \(JAv\in D(A^{-1})\); the latter condition is equivalent to \(Av\in D(A)\), so the domain is precisely \(D(A^2)\). The proof for \(SF\) uses the reciprocal powers. For \(F^2\), a vector in \(D(A^{-1})\) is sent by \(JA^{-1}\) back into that same domain, and the spectral product gives the identity.

These polar data are unique. If \(S=J_1A_1\), where \(J_1\) is antiunitary and \(A_1\) positive self-adjoint with \(D(A_1)=D(S)\), the adjoint pairing gives \(S^*S=A_1^2\) with its full square domain. Hence \(A_1\) is the unique positive square root of \(\Delta=S^*S\), by spectral calculus. The two antiunitaries agree on the dense range of \(A\), so are equal.

Finally \(U_t=\Delta^{it}\) is a strongly continuous unitary group by scalar spectral DCT, since \(|a^{it}|=1\). The same modulus identity preserves every real-power domain. Formula (CI12) gives
\[
JU_t=U_tJ,\qquad SU_t=U_tS,\qquad FU_t=U_tF,
\tag{CI15}
\]
on the full respective domains. The first sign is especially sensitive to anti-linearity: \(-\overline{it}=it\).

<a id="oa-flow.ci.4"></a>

## CI-4. The faithful-state model and an arbitrary-index domain test

Let \(M=M''\subseteq B(H)\) be unital and let \(\xi\) be cyclic and separating. The closed span of \(M'\xi\) has a projection in \(M\), fixing \(\xi\); separatingness makes the projection \(I\). Thus \(M'\xi\) is dense. Define \(S_0(x\xi)=x^*\xi\) and \(F_0(y'\xi)=y'^*\xi\). They are well defined, densely defined conjugate-linear involutions. Commutation and the inner-product convention give
\[
\langle S_0(x\xi),y'\xi\rangle
=\langle F_0(y'\xi),x\xi\rangle.
\tag{CI16}
\]
If \(x_n\xi\to0\) and \(S_0x_n\xi\to v\), (CI16) makes \(v\) orthogonal to the dense commutant orbit, so \(v=0\). This proves closability; the symmetric argument proves closability of \(F_0\). The preceding theorem applies to \(S=\overline{S_0}\). It does not assert \(\overline{F_0}=S^*\), a modular commutant theorem, or modular normalization of \(M\); those require their additional proofs.

The full domain claims can be tested on any index set \(I\). Choose numbers \(a_i>0\) and let \(H=\ell^2(I)\oplus\ell^2(I)\). Put
\[
S(x,y)=((a_i\overline{y_i})_i,(a_i^{-1}\overline{x_i})_i),
\quad
D(S)=\left\{(x,y)\in H:
\sum_i(a_i^{-2}|x_i|^2+a_i^2|y_i|^2)<\infty\right\}.
\tag{CI17}
\]
Finite-coordinate truncations show density and form a graph core; coordinate limits show closedness. The formula verifies (CI3) directly. Its polar data are
\[
J(x,y)=(\overline y,\overline x),\qquad
\Delta(x,y)=((a_i^{-2}x_i)_i,(a_i^2y_i)_i),
\tag{CI18}
\]
with the squared spectral-integrability domain for \(\Delta\). For \(I=\mathbb N\) and \(a_i=i\), the vector \(x_i=1/i,y=0\) lies in \(D(S)\setminus D(F)\); the swapped vector lies in \(D(F)\setminus D(S)\). This checks that neither full domain may be replaced by their intersection. Arbitrary \(I\), including the empty set, is allowed.

This complete analytic provider replaces the closed-involution/adjoint/polar components actually used from TC-03, TC-05 and TC-07–10, and HA-04's graph/polar facts. It does not replace the Hilbert-algebra multiplication, affiliated-multiplier or dual-algebra density proofs.
