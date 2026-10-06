# The vector retained by a comparison map

**Self-checked by the writing AI.**

A bounded comparison map can lose part of the cyclic vector of a functional. Its polar factor still produces a useful vector, but the norm records a projection of the cyclic vector. This unit proves the general identity before imposing conditions that remove that loss.

## Arbitrary weights and bounded observations

Let \(M\) be a von Neumann algebra, let \(\varphi\) be any weight, and let \(\omega\) be a bounded positive functional satisfying \(\omega\le c\varphi\) for a finite \(c>0\). Neither normality nor semifiniteness is assumed here. Inner products are linear in the first variable. Use

\[
(H,\pi,\Lambda)=(H_\varphi,\pi_\varphi,\Lambda_\varphi),\qquad
(H_\omega,\pi_\omega,\Omega_\omega)
\]

for the weight and bounded-functional GNS representations. The first GNS map has domain exactly
\(\mathfrak n_\varphi=\{x:\varphi(x^*x)<\infty\}\).
The bounded-functional representation is cyclic, with
\(\|\Omega_\omega\|^2=\omega(1)\).

WG003–006 construct these representations. DW03–04 give the bounded comparison operator and its polar decomposition:

\[
C:H\longrightarrow H_\omega,\quad
C\Lambda(x)=\pi_\omega(x)\Omega_\omega,\qquad
h=C^*C\in\pi(M)'_+,\qquad C=Uh^{1/2}.
\tag{GV1}
\]

Let \(K=\overline{\operatorname{ran}C}\) and let \(P\) be the orthogonal projection onto \(K\). Then

\[
UU^*=P,\qquad U^*U=s(h),\qquad
U^*\pi_\omega(a)=\pi(a)U^*\quad(a\in M).
\tag{GV2}
\]

These are the exact range and polar intertwining conclusions of DW04, with bounded polar decomposition supplied by BK07. In particular \(K\) reduces \(\pi_\omega(M)\), so \(P\) commutes with that algebra. No equality \(P=I\) is presumed.

## A canonical vector without dense range

Define

\[
\eta_\omega=U^*\Omega_\omega.
\]

Then

\[
h^{1/2}\Lambda(x)=\pi(x)\eta_\omega
\quad(x\in\mathfrak n_\varphi),\qquad
\|\eta_\omega\|^2=\|P\Omega_\omega\|^2\le\omega(1).
\tag{GV3}
\]

Moreover \(\eta_\omega\in s(h)H\), and equality in the norm inequality holds precisely when \(\Omega_\omega\in K\). By cyclicity and invariance of \(K\), this is equivalent to \(K=H_\omega\).

**Proof.** Using (GV1) and (GV2), for a vector in the stated finite domain,

\[
\begin{aligned}
\pi(x)\eta_\omega
&=U^*\pi_\omega(x)\Omega_\omega
=U^*C\Lambda(x)\\
&=s(h)h^{1/2}\Lambda(x)
=h^{1/2}\Lambda(x).
\end{aligned}
\]

Also \(s(h)U^*=U^*\), proving the support inclusion. The adjoint pairing gives

\[
\|U^*\Omega_\omega\|^2
=\langle UU^*\Omega_\omega,\Omega_\omega\rangle
=\langle P\Omega_\omega,\Omega_\omega\rangle
=\|P\Omega_\omega\|^2.
\]

The orthogonal decomposition into \(K\) and \(K^\perp\) proves the inequality and its equality condition. If \(\Omega_\omega\in K\), invariance gives \(\pi_\omega(M)\Omega_\omega\subseteq K\); cyclicity forces \(K=H_\omega\). The converse is immediate. This includes the zero functional and zero Hilbert spaces. \(\square\)

The vector also defines a bounded positive functional

\[
\rho_\omega(a)=\langle\pi(a)\eta_\omega,\eta_\omega\rangle.
\]

It has the exact description

\[
\rho_\omega(a)=
\langle\pi_\omega(a)P\Omega_\omega,P\Omega_\omega\rangle,\qquad
0\le\rho_\omega\le\omega.
\tag{GV4}
\]

Its comparison operator is \(h\), and
\(\rho_\omega(y^*x)=\omega(y^*x)\) for
\(x,y\in\mathfrak n_\varphi\).

**Proof.** Move \(U^*\) across the pairing and use the intertwining to obtain

\[
\langle\pi(a)U^*\Omega_\omega,U^*\Omega_\omega\rangle
=\langle\pi_\omega(a)\Omega_\omega,P\Omega_\omega\rangle
=\langle\pi_\omega(a)P\Omega_\omega,P\Omega_\omega\rangle.
\]

The last step uses the reducing decomposition. It decomposes \(\omega\) into the two positive vector functionals of \(P\Omega_\omega\) and \((1-P)\Omega_\omega\). This proves domination. For the finite-domain pairing, (GV3) gives

\[
\rho_\omega(y^*x)
=\langle\pi(x)\eta_\omega,\pi(y)\eta_\omega\rangle
=\langle h\Lambda(x),\Lambda(y)\rangle
=\omega(y^*x).
\]

Uniqueness of the bounded form representative gives its comparison operator \(h\). \(\square\)

Even the canonical polar choice need not determine a unique solution to the module identity in (GV3). The next statement describes all solutions when both weights and functionals are normal.

## All solutions and the finite-domain projection

Assume now that \(\varphi\) and \(\omega\) are normal. Let \(e\in M\) be the finite-domain projection of WS02:

\[
\overline{\mathfrak n_\varphi}^{\,\sigma\text{-strong}}=Me,
\qquad \mathfrak n_\varphi\subseteq Me.
\]

There are increasing positive contractions \(u_\alpha\in\mathfrak m_\varphi^+\) with \(u_\alpha\uparrow e\) strongly. The GNS representation \(\pi\) is normal by WG007, using the positive-map criterion NP04. Set \(E=\pi(e)\), an orthogonal projection on \(H\).

The full solution set of

\[
\pi(x)\zeta=h^{1/2}\Lambda(x)\quad(x\in\mathfrak n_\varphi)
\]

is

\[
\eta_\omega+(1-E)H.
\tag{GV5}
\]

Consequently there is exactly one solution in \(EH\), namely

\[
\eta_\omega^e=E\eta_\omega,\qquad
\|\eta_\omega^e\|^2=\omega(e).
\tag{GV6}
\]

This vector implements the compressed functional

\[
a\longmapsto\omega(eae)
\]

on all of \(M\).

**Proof.** The difference of two solutions belongs to
\(W=\bigcap_{x\in\mathfrak n_\varphi}\ker\pi(x)\).
Since \(x=xe\), every vector in \((1-E)H\) belongs to \(W\). Conversely, if \(\xi\in W\), then \(\pi(u_\alpha)\xi=0\). Normality gives
\(\pi(u_\alpha)\uparrow E\) strongly, so \(E\xi=0\).
Thus \(W=(1-E)H\), proving (GV5) and uniqueness on \(EH\).

To determine the norm and the functional, first observe that

\[
\pi_\omega(e)\Omega_\omega\in K.
\tag{GV7}
\]

Indeed \(u_\alpha\in\mathfrak n_\varphi\), and

\[
C\Lambda(u_\alpha)=\pi_\omega(u_\alpha)\Omega_\omega
\longrightarrow\pi_\omega(e)\Omega_\omega
\]

in norm. The squared error is
\(\omega((e-u_\alpha)^2)\le\omega(e-u_\alpha)\to0\).
Here \(u_\alpha=eu_\alpha e\), and normality of the bounded functional is used.

Intertwining gives
\(E\eta_\omega=U^*\pi_\omega(e)\Omega_\omega\).
The operator \(U^*\) is an isometry on \(K\), so (GV7) yields

\[
\|E\eta_\omega\|^2
=\|\pi_\omega(e)\Omega_\omega\|^2
=\omega(e).
\]

Write \(v=\pi_\omega(e)\Omega_\omega\in K\). Because \(K\) reduces the representation,

\[
\begin{aligned}
\langle\pi(a)U^*v,U^*v\rangle
&=\langle\pi_\omega(a)v,Pv\rangle\\
&=\langle\pi_\omega(a)\pi_\omega(e)\Omega_\omega,
                  \pi_\omega(e)\Omega_\omega\rangle
=\omega(eae).
\end{aligned}
\]

This proves the last assertion. \(\square\)

Thus the general polar vector in GV02 and the supported vector in OW14 can differ. If \(\varphi\) is semifinite, then \(e=1\), so the distinction vanishes and the norm is \(\omega(1)\). If \(\omega(a)=\omega(eae)\) for all \(a\), (GV7) puts \(\Omega_\omega\) itself in \(K\); cyclicity gives dense range, and the canonical vector already lies in \(EH\).

## A noncentral two-dimensional calculation

In \(M=M_2(\mathbb C)\), let \(e=E_{11}\). Define the normal weight
\(\varphi(te)=t\) for \(t\ge0\), and give every other positive matrix value infinity. WS08 proves the weight and normality assertions. Its GNS space is \(H=\mathbb C^2\), with
\(\Lambda(x)=xe_1\) on \(Me\), and \(\pi\) the usual matrix action.

Fix \(0<t<1\), put

\[
C_t=\begin{pmatrix}1&t\\t&1\end{pmatrix},
\qquad \omega_t(a)=\operatorname{Tr}(C_ta).
\]

The matrix is strictly positive, with eigenvalues \(1+t,1-t\).
The functional is dominated by \(\varphi\), since its value on \(se\) is \(s\), while all other positive inputs have infinite weight.

Realize the functional GNS space as the Hilbert space of two-by-two matrices with the usual Hilbert–Schmidt inner product. Its cyclic vector is \(C_t^{1/2}\), and its representation is left multiplication. Let \(r=C_t^{1/2}e_1\); then \(\|r\|=1\). The comparison map is

\[
Cv=vr^*,\qquad C^*Z=Zr.
\]

Indeed, for \(x=ve_1^*\) one has
\(xC_t^{1/2}=vr^*\). The Hilbert–Schmidt norm of \(vr^*\) is \(\|v\|\), so \(C\) is an isometry. Thus \(h=I\) and \(U=C\), whereas its two-dimensional range is a proper subspace of the four-dimensional functional GNS space.

The canonical and supported vectors are therefore

\[
\eta_{\omega_t}=C^*C_t^{1/2}=C_te_1=e_1+te_2,\qquad
\eta_{\omega_t}^e=e_1.
\]

Their squared norms are \(1+t^2\) and \(1\); the original functional norm is \(2\). All three numbers are different. Every vector \(e_1+ze_2\), \(z\in\mathbb C\), satisfies the module identity, because \(x=xe\) ignores the second coordinate. This verifies both the lost norm and the precise uniqueness boundary.

## Problems and exact source extent

**Problem 1.** Show that \(\rho_\omega=\omega\) in (GV4) if and only if the comparison map has dense range.

**Solution.** Dense range means \(P=I\), so (GV4) gives equality. Conversely equality evaluated at \(1\) gives
\(\|P\Omega_\omega\|^2=\|\Omega_\omega\|^2\).
Thus \(\Omega_\omega\in K\), and cyclicity gives \(K=H_\omega\).
No normality is used.

**Problem 2.** In GV04 compute \(\rho_{\omega_t}\) and exhibit a positive density matrix for \(\omega_t-\rho_{\omega_t}\).

**Solution.** The vector \(\eta=e_1+te_2\) gives

\[
\rho_{\omega_t}(a)=\langle a\eta,\eta\rangle,\qquad
D_\eta=\begin{pmatrix}1&t\\t&t^2\end{pmatrix}.
\]

Subtracting this density from \(C_t\) gives
\(\operatorname{diag}(0,1-t^2)\ge0\).
It also shows directly that the two functionals agree on \(eMe\), while their values at the identity differ.

The exact mathematical antecedent is Takesaki II VII1 equations (29)–(33). Those comparison and vector identities are valid at their stated generality. GV02 supplies their complete arbitrary-weight bounded-functional argument from DW04. GV03–04 explain extra uniqueness and norm statements that require support or semifiniteness. The separately recorded defect concerns the unrestricted norm-value definition in Theorem1.17, not the preceding vector identity.

