# Weight domination and exact half-strip endpoints

**Self-checked by the writing AI.**

For a modular orbit, analytic continuation to imaginary time \(-i/2\) measures the norm of right multiplication on the GNS space. For a weight cocycle, the same endpoint measures domination of the numerator by the denominator. The conjugating operator at this endpoint has a fixed order; reversing its factors can change the weight even in two dimensions.

The source targets are Takesaki, *Theory of Operator Algebras II*, VIII.3, Theorem 3.17 and all three parts of Lemma 3.18. We prove the operator strip criterion rather than importing an unspecified domain assertion. The exact inputs are SK's spectral bands and powers; MA-08's scalar boundary uniqueness and bounded-strip maximum principle; WH-10's full finite-star graph core; MF-06's modular implementation and commutant theorem; CX-03/CZ-02's Gaussian entire elements and full analytic right multiplication; NW-12's closed GNS graph; WG's finite domains; CZ-05's centralizer multiplier/cyclicity criterion; and GC-03/04/08's balanced weight and normalized cocycle. The underlying scalar integration and complex-analysis contracts retain their stated status.

Throughout, inner products are linear in the first slot. A bounded function on a closed strip is required to be bounded on the entire strip, sigma-weakly continuous there, and holomorphic in its interior. We do not demand norm continuity of its real boundary orbit.

## A closed intertwining relation is a bounded operator strip

Let \(D>0\) be an injective positive self-adjoint operator on an arbitrary Hilbert space, and put

\[
 P_n=1_{[1/n,n]}(D),\qquad
 \mathcal E=\bigcup_{n\geq1}P_nH,\qquad
 \mathcal S_s=\{z:-s\leq\operatorname{Im}z\leq0\},\quad s>0.
 \tag{HS.1}
\]

Spectral bands are not finite-dimensional projections. They make all powers on \(\mathcal E\) defined, and form a core for every fixed spectral power.

**Strip criterion.** For \(a,b\in B(H)\), the full domain assertion

\[
 aD(D^s)\subseteq D(D^s),\qquad D^s a\xi=bD^s\xi
 \quad(\xi\in D(D^s))
 \tag{HS.2}
\]

is equivalent to a bounded sigma-weakly continuous, interior-holomorphic extension \(F\) of \(D^{it}aD^{-it}\) to \(\mathcal S_s\), whose other edge is

\[
 F(t-is)=D^{it}bD^{-it}.
 \tag{HS.3}
\]

The extension is unique. If \(A_0,B_0>0\) bound the norms of \(a,b\), respectively, then

\[
 \|F(t-iu)\|\leq A_0^{\,1-u/s}B_0^{\,u/s}
 \quad(0\leq u\leq s).
 \tag{HS.4}
\]

If a von Neumann subalgebra \(N\subseteq B(H)\) contains \(a\) and is invariant under \(\operatorname{Ad}(D^{it})\), the extension takes values in \(N\).

**From the domain to the strip.** For \(\xi,\eta\in\mathcal E\), form the entire scalar function

\[
 f_{\xi,\eta}(z)
 =\langle aD^{-iz}\xi,D^{-i\bar z}\eta\rangle.
 \tag{HS.5}
\]

Its values on the two edges are the matrix coefficients of the two operators in (HS.3) and the real orbit. At the lower edge, move the positive power using (HS.2):

\[
 f_{\xi,\eta}(t-is)
 =\langle D^s aD^{-it-s}\xi,D^{-it}\eta\rangle
 =\langle D^{it}bD^{-it}\xi,\eta\rangle.
 \tag{HS.6}
\]

All powers act on band vectors. On the whole strip, (HS.5) is bounded: each band bounds its positive and negative real powers uniformly for \(u\in[0,s]\), while real-time powers are unitary. MA-08 therefore bounds it by
\(\max(\|a\|,\|b\|)\|\xi\|\|\eta\|\).
For each \(z\), Hilbert-space Riesz representation gives a bounded operator \(F(z)\) with these coefficients. Uniform bounds and density of \(\mathcal E\) give weak operator continuity throughout the closed strip and holomorphy of every matrix coefficient inside.

On bounded subsets of \(B(H)\), finite sums of vector coefficients approximate every normal functional uniformly; the trace-class representation of the predual supplies this assertion. Thus \(F\) is sigma-weakly continuous and weak-star holomorphic. For precision, on a disc inside the strip, scalar Cauchy coefficients define bounded operators \(C_j\) by their vector coefficients. Their norms satisfy \(\|C_j\|\leq CR^{-j}\), where \(C\) bounds \(F\) on the circle of radius \(R\). The norm-convergent series \(\sum_j C_j(z-z_0)^j\) has the same scalar tests as \(F\). It equals \(F\), proving norm holomorphy in the interior.

To obtain (HS.4), scalarize (HS.5) and multiply by

\[
 \exp(-izc),\qquad c=s^{-1}\log(B_0/A_0).
 \tag{HS.7}
\]

Its modulus at \(z=t-iu\) is \(e^{-uc}\). The two edge bounds of the product are both \(A_0\|\xi\|\|\eta\|\). The product is still bounded on this finite-height strip, so MA-08 gives (HS.4). Density recovers the operator norm.

If \(N\) is as stated, any normal functional annihilating \(N\) vanishes on the real edge of \(F\). Boundary uniqueness makes it vanish throughout the strip. Since a von Neumann algebra is sigma-weakly closed, these tests imply \(F(z)\in N\), including \(b=F(-is)\).

**From the strip to the domain.** For band vectors, the matrix coefficient of the given \(F\) agrees with (HS.5) on the real edge. Boundary uniqueness identifies them on the strip. At \(z=-is\), replace \(\xi\) by \(D^s\xi\) to obtain

\[
 \langle a\xi,D^s\eta\rangle=\langle bD^s\xi,\eta\rangle,
 \qquad \xi,\eta\in\mathcal E.
 \tag{HS.8}
\]

Since \(\mathcal E\) is a core for the self-adjoint \(D^s\), its adjoint-domain criterion gives \(a\xi\in D(D^s)\) and \(D^s a\xi=bD^s\xi\) for \(\xi\in\mathcal E\). For arbitrary \(\xi\in D(D^s)\), apply this to \(P_n\xi\) and use closedness of \(D^s\). This proves the full domain assertion. The same scalar boundary uniqueness proves uniqueness of the strip. \(\square\)

## A conjugation inequality produces the endpoint

Fix a faithful normal semifinite weight \(\varphi\) on \(M\), represented on its faithful normal GNS space. Write

\[
 S=J\Delta^{1/2},\qquad \sigma_t=\sigma_t^\varphi,\qquad
 \mathfrak a_\varphi=\mathfrak n_\varphi\cap\mathfrak n_\varphi^*.
 \tag{HS.9}
\]

Suppose \(a\in M\) satisfies

\[
 \varphi(axa^*)\leq\varphi(x)\qquad(x\in M_+).
 \tag{HS.10}
\]

Then \(xa^*\in\mathfrak n_\varphi\) for every \(x\in\mathfrak n_\varphi\), and

\[
 R\Lambda_\varphi(x)=\Lambda_\varphi(xa^*),\qquad
 \|R\|\leq1,\qquad R\in M'.
 \tag{HS.11}
\]

Indeed apply (HS.10) to \(x^*x\). The resulting estimate makes this rule well defined and contractive on the dense GNS range. Left multiplication commutes with it on that range, hence \(R\) belongs to the represented commutant.

For \(x\in\mathfrak a_\varphi\), the element \(ax\) is in \(\mathfrak n_\varphi\) by the left ideal property; its adjoint \(x^*a^*\) is there by (HS.11). Thus \(ax\in\mathfrak a_\varphi\), and

\[
 S a\Lambda_\varphi(x)
 =\Lambda_\varphi(x^*a^*)=R S\Lambda_\varphi(x).
 \tag{HS.12}
\]

WH-10 makes \(\Lambda_\varphi(\mathfrak a_\varphi)\) a graph core for \(S\). Boundedness of \(a,R\) and closedness of \(S\) extend this identity to all \(D(S)=D(\Delta^{1/2})\). Multiply by \(J\) to get

\[
 \Delta^{1/2}a\xi=b\Delta^{1/2}\xi,\qquad
 b=JRJ\in M,\quad \|b\|\leq1.
 \tag{HS.13}
\]

Here \(b\in M\) uses the modular commutant theorem. HS-01 gives a bounded \(M\)-valued strip extension of \(\sigma_t(a)\), with

\[
 \sigma_{-i/2}(a)=b,\qquad
 \sigma_{t-i/2}(a)=\sigma_t(b).
 \tag{HS.14}
\]

The notation denotes the unique closed-strip extension. It does not assert that \(a\) is entire.

## A strip endpoint acts on the whole finite left ideal

Conversely, suppose \(\sigma_t(a)\) has a bounded \(M\)-valued extension \(F\) to the closed lower half-strip, with \(b=F(-i/2)\). Then

\[
 xa^*\in\mathfrak n_\varphi,\qquad
 \Lambda_\varphi(xa^*)=JbJ\Lambda_\varphi(x)
 \quad(x\in\mathfrak n_\varphi).
 \tag{HS.15}
\]

In particular

\[
 \varphi(aya^*)\leq\|b\|^2\varphi(y),\qquad y\in M_+.
 \tag{HS.16}
\]

At scalar zero the right side is interpreted as the zero weight; the zero endpoint forces \(a=0\) by (HS.2) and injectivity of \(\Delta^{1/2}\).

**Proof of the full domain, without assuming an entire \(a\).** Let

\[
 a_r=\sqrt{r/\pi}\int_{\mathbb R}e^{-rt^2}\sigma_t(a)\,dt,\qquad
 b_r=\sqrt{r/\pi}\int_{\mathbb R}e^{-rt^2}\sigma_t(b)\,dt.
 \tag{HS.17}
\]

CZ-02/CX-03 show that \(a_r\) is entire and that \(a_r\to a\), \(b_r\to b\) sigma-strongly*, with uniform norm bounds. The given strip necessarily satisfies
\(F(t-i/2)=\sigma_t(b)\): translate the strip and compare its real boundary by uniqueness.

The convolution \(\int g_r(t)F(t+z)\,dt\) is bounded and sigma-weakly continuous on the strip and holomorphic inside, by scalar integration and Cauchy bounds. On its real edge it is \(\sigma_z(a_r)\). Boundary uniqueness therefore identifies it with the entire continuation of \(a_r\) on that strip. Its endpoint is \(b_r\), so

\[
 \sigma_{-i/2}(a_r)=b_r,\qquad
 \Lambda_\varphi(xa_r^*)=Jb_rJ\Lambda_\varphi(x).
 \tag{HS.18}
\]

The second equality is CX-03's full entire right multiplier formula. For fixed \(x\in\mathfrak n_\varphi\), its left algebra entries converge sigma-strongly to \(xa^*\), and its right vectors converge in Hilbert norm to \(JbJ\Lambda_\varphi(x)\). NW-12's closed GNS graph proves both membership and (HS.15). This avoids identifying a dense GNS subspace with the full finite ideal.

If \(\varphi(y)<\infty\), apply (HS.15) to \(y^{1/2}\) and take squared norms. This proves (HS.16). If \(\varphi(y)=\infty\) and \(\|b\|>0\), the inequality is automatic; the zero case was already settled. \(\square\)

HS-02 and HS-03 prove precisely the equivalence in VIII.3.18(i), together with the full domain and identity in part (ii). More generally, for any \(C>0\),

\[
 \varphi(aya^*)\leq C\varphi(y)\ (y\geq0)
 \quad\Longleftrightarrow\quad
 F\text{ exists and }\|F(-i/2)\|\leq\sqrt C.
 \tag{HS.19}
\]

Apply the contraction result to \(a/\sqrt C\); no scaling of the reference weight or cocycle normalization is needed.

## Reflecting the strip proves the centralizer endpoint identity

Let \(F,a,b\) be as in HS-03. Reflect and take the adjoint:

\[
 G(z)=F(\bar z-i/2)^*,\qquad -1/2\leq\operatorname{Im}z\leq0.
 \tag{HS.20}
\]

This is again bounded, sigma-weakly continuous and interior holomorphic. It has real edge \(\sigma_t(b^*)\) and lower edge \(\sigma_t(a^*)\). Applying HS-03 to \(b^*\) gives

\[
 xb\in\mathfrak n_\varphi,\qquad
 \Lambda_\varphi(xb)=Ja^*J\Lambda_\varphi(x)
 \quad(x\in\mathfrak n_\varphi).
 \tag{HS.21}
\]

No contractive bound on this reflected endpoint is required.

Suppose in addition \(c=aa^*\in M_\varphi\). Then \(c\) is a two-sided multiplier of \(\mathfrak m_\varphi\) and is cyclic there, by CZ-05. For \(x\in\mathfrak n_\varphi\), (HS.21) and the fixed-element right multiplier formula yield

\[
 \begin{aligned}
 \varphi(b^*x^*xb)
 &=\|Ja^*J\Lambda_\varphi(x)\|^2\\
 &=\langle Jaa^*J\Lambda_\varphi(x),\Lambda_\varphi(x)\rangle\\
 &=\langle\Lambda_\varphi(xc),\Lambda_\varphi(x)\rangle
 =\varphi(x^*xc)=\varphi(cx^*x).
 \end{aligned}
 \tag{HS.22}
\]

Every value is on a finite linear domain. In particular \(xc\in\mathfrak n_\varphi\), and \(b^*x^*xb\) has finite weight by (HS.21). Polarization, or the finite positive spanning property of WG, proves

\[
 b^*yb\in\mathfrak m_\varphi,\qquad
 \varphi(cy)=\varphi(b^*yb)\quad(y\in\mathfrak m_\varphi).
 \tag{HS.23}
\]

This is the exact finite-domain statement of VIII.3.18(iii). We have not assigned a complex weight value to an arbitrary element of \(M\), nor silently replaced \(\mathfrak m_\varphi\) by another weight's finite algebra.

## Domination of weights is the norm of a cocycle endpoint

**Theorem.** Let \(\varphi,\psi\) be faithful normal semifinite weights on an arbitrary von Neumann algebra \(M\), and fix \(C>0\). The following are equivalent:

1. \(\psi(x)\leq C\varphi(x)\) for every \(x\in M_+\).
2. The normalized cocycle \(u_t=[D\psi:D\varphi]_t\) has a bounded sigma-weakly continuous \(M\)-valued extension to \(-1/2\leq\operatorname{Im}z\leq0\), holomorphic inside, with \(\|u_{-i/2}\|\leq\sqrt C\).

The extension is unique, satisfies

\[
 \|u_{t-iy}\|\leq C^y\quad(0\leq y\leq1/2),
 \tag{HS.24}
\]

and has the exact finite-domain identity

\[
 u_{-i/2}^*x u_{-i/2}\in\mathfrak m_\varphi,\qquad
 \psi(x)=\varphi(u_{-i/2}^*x u_{-i/2})
 \quad(x\in\mathfrak m_\psi).
 \tag{HS.25}
\]

The domination statement includes infinite positive values. The complex linear endpoint identity has the stated \(\psi\)-finite domain.

**Proof.** Apply GC-03/04/08 with the numerator first. On \(N=M_2(M)\) take

\[
 \Omega(X)=\psi(X_{11})+\varphi(X_{22}),\qquad
 A=C^{-1/2}E_{12},\qquad \alpha=\sigma^\Omega.
 \tag{HS.26}
\]

This is faithful normal semifinite; its diagonal modular restrictions and matrix-unit covariance give

\[
 \alpha_t(A)=C^{-1/2}u_tE_{12},\qquad
 AA^*=C^{-1}E_{11}\in N_\Omega.
 \tag{HS.27}
\]

For any positive matrix \(X\), direct multiplication gives

\[
 A X A^*=C^{-1}X_{22}E_{11},\qquad
 \Omega(AXA^*)=C^{-1}\psi(X_{22}).
 \tag{HS.28}
\]

If condition 1 holds, this is at most \(\varphi(X_{22})\leq\Omega(X)\). HS-02/03 produce a closed half-strip extension of \(\alpha_t(A)\), with endpoint norm at most one. Its \(12\) matrix entry is \(C^{-1/2}u_z\); other entries vanish by scalar boundary uniqueness. Thus condition 2 follows.

Conversely, the stipulated \(u_z\) extends \(\alpha_t(A)\), with endpoint norm at most one. HS-03 gives \(\Omega(AXA^*)\leq\Omega(X)\) on all \(N_+\). Put \(X=xE_{22}\). Formula (HS.28) yields condition 1 for every positive \(x\), including infinite values. The order of the matrix indices in (HS.28) is essential: \(E_{12}XE_{21}=X_{22}E_{11}\).

For the endpoint formula, if \(x\in\mathfrak m_\psi\), then \(X=xE_{11}\in\mathfrak m_\Omega\). Apply HS-04 with \(A\), whose endpoint is \(B=C^{-1/2}u_{-i/2}E_{12}\). It gives

\[
 C^{-1}\psi(x)
 =\Omega(AA^*X)=\Omega(B^*XB)
 =C^{-1}\varphi(u_{-i/2}^*xu_{-i/2}).
 \tag{HS.29}
\]

HS-04 supplies finiteness of the final linear value. Cancel the positive finite scalar \(C^{-1}\) to obtain (HS.25).

Finally apply the weighted strip estimate HS-01 to \(\alpha_z(A)\). The real-edge norm is \(C^{-1/2}\), and the lower-edge norm is at most one. Multiplying its norm bound by \(\sqrt C\) gives \(C^y\). Boundary uniqueness proves uniqueness of \(u_z\). \(\square\)

## Sharp scale and a noncommuting endpoint

**A sharp scalar scale.** If \(\psi=C\varphi\), the normalized cocycle is \(u_t=C^{it}1\), by PT-04/11. Its continuation is

\[
 u_{t-iy}=C^y C^{it}1,\qquad u_{-i/2}=\sqrt C\,1.
 \tag{HS.30}
\]

Thus (HS.24) is sharp, including \(0<C<1\). The real orbit consists of unitaries, even when its imaginary-time norm is less than one.

**Two noncommuting densities.** On \(M_2(\mathbb C)\), set

\[
 h=\begin{pmatrix}1&0\\0&4\end{pmatrix},\qquad
 k=\begin{pmatrix}5&-3\\-3&5\end{pmatrix},\qquad
 \varphi(x)=\operatorname{Tr}(hx),\quad
 \psi(x)=\operatorname{Tr}(kx).
 \tag{HS.31}
\]

These are faithful finite normal weights. GC-09, with numerator and denominator interchanged, gives

\[
 u_t=k^{it}h^{-it},\qquad
 v=u_{-i/2}=k^{1/2}h^{-1/2}
 =\frac{\sqrt2}{2}
     \begin{pmatrix}3&-1/2\\ -1&3/2\end{pmatrix}.
 \tag{HS.32}
\]

The least domination constant is

\[
 C_*=\|v\|^2
 =\left\|\begin{pmatrix}5&-3/2\\ -3/2&5/4\end{pmatrix}\right\|
 =\frac{25+3\sqrt{41}}8.
 \tag{HS.33}
\]

Indeed \(\psi\leq C\varphi\) on positives is equivalent to \(k\leq Ch\): rank-one positives test the operator order, and finite trace cyclicity proves the converse. Congruence by \(h^{-1/2}\) gives \(v^*v\leq C1\). Its two eigenvalues are \((25\pm3\sqrt{41})/8\), verifying the exact maximum in (HS.33).

The correct endpoint recovers the numerator:

\[
 \varphi(v^*xv)=\operatorname{Tr}(v h v^*x)
 =\operatorname{Tr}(kx)=\psi(x).
 \tag{HS.34}
\]

The reversed product \(w=h^{-1/2}k^{1/2}=v^*\) gives instead

\[
 w h w^*=
 \begin{pmatrix}13/2&-15/4\\ -15/4&37/8\end{pmatrix}.
 \tag{HS.35}
\]

At \(x=E_{11}\), the wrong endpoint gives \(13/2\) instead of \(5\). This checks the factor order in (HS.25) without relying on a commuting model.

## Problems with complete solutions

**Problem 1. A right multiplier can be contractive without the algebra element being a contraction.** For the weight with density \(h=\operatorname{diag}(1,4)\), choose \(a=2E_{12}\). Verify (HS.10), and compute its endpoint and right GNS operator.

**Solution.** The orbit is \(4^{-it}a\), and
\(\sigma_{-i/2}(a)=4^{-1/2}a=E_{12}\). Its norm is one, although \(\|a\|=2\). Directly \(a^*ha=4E_{22}\leq h\), so
\(\varphi(axa^*)=\operatorname{Tr}(a^*ha\,x)\leq\varphi(x)\).
On Hilbert–Schmidt matrices the GNS map is \(\Lambda(x)=xh^{1/2}\), \(J\xi=\xi^*\), and \(J E_{12}J\) is right multiplication by \(E_{21}\). Accordingly

\[
 \Lambda(xa^*)=xh^{1/2}E_{21}
 =J E_{12}J\Lambda(x),
 \tag{HS.36}
\]

as (HS.15) requires. The endpoint, not the real-time operator norm of \(a\), controls right multiplication.

**Problem 2. Retain a genuinely infinite algebra and unbounded densities.** On
\(M=\prod_{i\in I}M_2(\mathbb C)\), choose arbitrary positive numbers \(r_i\), with no common upper bound, and let

\[
 \varphi(x)=\sum_i r_i\operatorname{Tr}(h x_i),\qquad
 \psi(x)=\sum_i r_i\operatorname{Tr}(k x_i),
 \tag{HS.37}
\]

using (HS.31) and an arbitrary nonempty index set \(I\). Show that the exact domination constant and the endpoint remain \(C_*\) and the bounded family \(v_i=v\).

**Solution.** All sums are suprema of finite subsums. Both weights are faithful and normal. Finite-coordinate positive elements have finite weight; finite-coordinate projections increase strongly to one, proving semifiniteness. Summing the block inequalities gives \(\psi\leq C_*\varphi\) on every positive, including infinite sums. A rank-one test in one block forces \(C\geq C_*\). In each block the scalar \(r_i^{it}\) cancels between numerator and denominator, leaving the same unitary cocycle and \(v\). The continuation is a bounded constant block family. The full density operators can still be unbounded and not trace-measurable. No countability of \(I\) enters this argument. Formula (HS.25) retains its finite \(\psi\)-linear domain; positive block sums may also be evaluated directly without subtracting infinities.

**Problem 3. Reconstruct the endpoint norm from the closed GNS map.** Under (HS.10), why is the endpoint in HS-02 fixed uniquely, and why does a proof on the finite-star space need a graph-core argument?

**Solution.** The dense GNS rule (HS.11) has exactly one bounded extension \(R\). Therefore \(b=JRJ\) is fixed. HS-01 then gives a unique strip, and its endpoint is this \(b\). In (HS.12) the vector \(\Lambda(x)\) is initially in the finite-star core. Passing to arbitrary \(\xi\in D(S)\) requires simultaneous convergence of \(\Lambda(x_j)\) and \(S\Lambda(x_j)\); Hilbert-norm density alone does not supply the latter. WH-10's graph core and closedness of \(S\) do supply it. HS-03 independently passes from entire Gaussian factors to every \(x\in\mathfrak n_\varphi\) by the closed GNS graph, so no finite-star restriction survives in the final formula.

The unit proves the full half-strip contraction criterion, the whole finite-left-ideal right action, the centralizer endpoint identity on its exact finite linear domain, and the weight-domination theorem with its exact cocycle endpoint. The remaining supported cocycle and analytic-generator results in VIII.3 and the operator-valued weight analogues are not proved in this lesson.
