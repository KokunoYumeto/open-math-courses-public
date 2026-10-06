# Euler chains and Fourier eigenspaces

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

Fourier transformation sends a generalized homogeneity parameter \(a\) on the line to \(-a-1\), without losing a chain. On Schwartz functions its symmetric normalization has four continuous projections. A scalar integrating factor then gives a global right inverse for each coordinate operator \(x_\nu+\partial_\nu\). For several such equations, we construct a solution exactly when the data satisfy the commuting-operator compatibility conditions.

For the Euler operator \(E=x\partial_x\), a complex number \(a\), and a positive integer \(k\), write
\[
Z(a,k)=\{u\in\mathcal D'(\mathbb R):(E-a)^ku=0\}.
\tag{0.1}
\]
The complete proofs in [U019](euler-equations-and-singularity-order.md), Theorems 2.1–2.2, give dimension \(2k\), the exceptional negative-integer point jets, and the description
\(|x|^aP_\pm(\log|x|)\) on the two open half-lines, where each polynomial has degree below \(k\). Their coefficients need not be independently selectable at an exceptional parameter; the cited classification includes those constraints.

Our [Schwartz and Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves every seminorm estimate, compact-cutoff approximation, Gaussian constant, inverse identity and transposed coordinate identity used here. Its convention is
\[
\begin{gathered}
F\phi(\xi)=\int_{\mathbb R^n}e^{-ix\cdot\xi}\phi(x)\,dx,\qquad
(Fu)(\psi)=u(F\psi),\\
F^2=(2\pi)^n\mathcal R,\qquad
\mathcal R\phi(x)=\phi(-x).
\end{gathered}
\tag{0.2}
\]
Pairings are complex bilinear. We use
\(P_N(f)=\max_{|\alpha|\le N}\sup_x\langle x\rangle^N|\partial^\alpha f(x)|\),
where \(\langle x\rangle=(1+|x|^2)^{1/2}\). These are equivalent to F1's polynomial seminorms because
\(\langle x\rangle\le1+\sum|x_j|\le C_n\langle x\rangle\), followed by the finite multinomial expansion. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Sections 12.4–12.9, 13.1–13.5 and 13.7–13.10, supplies compactness, finite calculus, exponentials, logarithms and cutoffs. The [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15.0–15.1, supplies dominated convergence and absolute Fubini. Finite complex algebra is proved in the [algebra foundation](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), Sections 10.1–10.3. These are supplied proofs, not external references in place of proofs.

## Fourier duality includes every generalized Euler chain

**Theorem 1.1 (Euler duality).** Every member of \(Z(a,k)\) has a unique tempered extension. With those extensions,
\[
FZ(a,k)=Z(-a-1,k)
\tag{1.1}
\]
is a linear bijection.

**Proof: control the origin and infinity separately.** Choose a compactly supported smooth \(\chi\) equal to one near zero. On a fixed compact neighborhood \(K\) of its support, continuity of \(u\) gives integers \(r\) and a constant \(C\) with
\[
|u(\psi)|\le C\max_{j\le r}\sup_K|\psi^{(j)}|,
\qquad \operatorname{supp}\psi\subset K.
\]
Indeed a neighborhood of zero in this fixed-support test space imposes finitely many derivative bounds; scaling a test into that neighborhood gives the displayed inequality, with the largest of their orders. Consequently \(u(\chi\phi)\) is defined for every \(\phi\in\mathcal S\), and
\[
|u(\chi\phi)|\le
C\max_{j\le r}\sum_{\ell=0}^j
\binom j\ell\|\chi^{(j-\ell)}\|_\infty
\|\phi^{(\ell)}\|_\infty
\le C_\chi P_r(\phi).
\]

The distribution \((1-\chi)u\) is the regular distribution of a smooth function \(b\), zero near zero, by U019's half-line classification. Choose an integer \(m\ge0\) with \(m>\operatorname{Re}a\). To check its growth explicitly, put \(t=\log|x|\ge0\) for \(|x|\ge1\). For every nonnegative integer \(j\), \(t^je^{-(m-\operatorname{Re}a)t}\) is bounded: when \(j>0\) its derivative changes sign at \(j/(m-\operatorname{Re}a)\), and for \(j=0\) it decreases. The finitely many logarithmic terms therefore give \(|b(x)|\le C\langle x\rangle^m\); bounded intermediate intervals are covered by continuity. Hence
\[
\left|\int b(x)\phi(x)\,dx\right|
\le C P_{m+2}(\phi)\int_{\mathbb R}(1+x^2)^{-1}\,dx
=C\pi P_{m+2}(\phi).
\]
The sum of the two pairings extends \(u\) to \(\mathcal S'\). F1's compact-cutoff density proves uniqueness. This argument includes every exceptional point jet; its off-origin tail is simply zero.

**Proof: transpose the operator.** Multiplication by \(x\) and differentiation are continuous on \(\mathcal S'\), by transposing their F1 bounds. Since \((E-a)^ku\) vanishes on compact tests, density implies it vanishes on all Schwartz tests. F5 gives \(F(\partial_xu)=i\xi Fu\) and \(F(xu)=i\partial_\xi Fu\). Thus the distributional product rule yields
\[
\begin{aligned}
F(Eu)&=i\partial_\xi(i\xi Fu)=-(E+1)Fu,\\
F((E-a)^ku)&=(-1)^k(E+a+1)^kFu.
\end{aligned}
\tag{1.2}
\]
Iteration is legitimate for each finite \(k\). This proves the inclusion in (1.1). Conversely, let \(v\in Z(-a-1,k)\), already tempered by the first part, and set \(u=F^{-1}v\). Applying (1.2) gives \(F((E-a)^ku)=0\); the inverse from F5 gives \((E-a)^ku=0\). This proves surjectivity, and the same inverse proves injectivity. \(\square\)

If \((E-a)v_j=v_{j-1}\), with \(v_{-1}=0\), put \(w_j=(-1)^jFv_j\). Each \(v_j\) is in \(Z(a,j+1)\), so its transform exists. Equation (1.2) gives
\((E+a+1)w_j=w_{j-1}\). When \(v_0\ne0\), also \(w_0\ne0\); the normalized chain has exactly the same length, even at an exceptional degree.

## Four finite projections give a unique decomposition

**Theorem 2.1 (four eigenspaces).** On \(\mathcal S(\mathbb R^n)\), set \(T=(2\pi)^{-n/2}F\). Then \(T^4=I\). Every \(u\) has a unique sum \(u=\sum_{k=0}^3u_k\), where \(Tu_k=i^ku_k\), given by the continuous projections
\[
u_k=\Pi_ku,\qquad
\Pi_k=\frac14\sum_{j=0}^3i^{-kj}T^j.
\tag{2.1}
\]

**Proof.** Equation (0.2) gives \(T^2=\mathcal R\), and reflection twice is the identity. For an integer \(r\), write \(z=i^r\). If \(4\mid r\), \(\sum_{j=0}^3z^j=4\). Otherwise \(z\ne1\), and
\((1-z)(1+z+z^2+z^3)=1-z^4=0\), so the sum is zero. This proves the needed finite orthogonality without a spectral theorem.

Sum (2.1) over \(k\) and use this identity to obtain \(\sum_k\Pi_k=I\). Replacing \(j+1\) by its residue modulo four gives
\[
T\Pi_k
=\frac14\sum_{j=0}^3i^{-kj}T^{j+1}
=i^k\Pi_k.
\]
If \(Tw=i^\ell w\), then
\(\Pi_kw=\frac14\sum_{j=0}^3i^{(\ell-k)j}w=\delta_{k\ell}w\).
Apply this to \(w=\Pi_\ell u\): \(\Pi_k\Pi_\ell=\delta_{k\ell}\Pi_\ell\).
Every projection is a finite sum of continuous operators. The sum gives existence, and applying \(\Pi_k\) to any such decomposition gives uniqueness. \(\square\)

Write \(E_k(n)=\ker(T-i^kI)\), with indices interpreted modulo four. Each eigenspace is closed: if an element has nonzero \((T-i^kI)u\), some evaluation of that continuous function is nonzero, and continuity preserves that inequality in a neighborhood. This also explains the inherited Schwartz topology on \(E_k(n)\).

## A coordinate operator has a global Schwartz right inverse

**Theorem 3.1 (coordinate surjectivity).** For \(1\le\nu\le n\), let \(L_\nu=x_\nu+\partial_\nu\). Put \(s=x_\nu\) and let \(z\) contain the other coordinates. The formula
\[
(R_\nu f)(s,z)
=e^{-s^2/2}\int_0^s e^{t^2/2}f(t,z)\,dt
\tag{3.1}
\]
defines a continuous linear map \(\mathcal S(\mathbb R^n)\to\mathcal S(\mathbb R^n)\) with \(L_\nu R_\nu=I\). Moreover
\(\ker L_\nu=\{e^{-s^2/2}h(z):h\in\mathcal S(\mathbb R^{n-1})\}\).
For \(n=1\), \(h\) is any complex constant.

**Proof: smoothness and the zeroth \(s\)-derivative.** To put the finite integral on a fixed interval, substitute \(t=su\):
\[
R_\nu f(s,z)=s\int_0^1 e^{-s^2(1-u^2)/2}f(su,z)\,du.
\]
Every parameter derivative of the integrand is continuous and bounded on compact parameter sets times \([0,1]\). The fundamental theorem applied to difference quotients and dominated convergence justify differentiation of every order, including at \(s=0\). The original integral then gives \(\partial_sR_\nu f=f-sR_\nu f\).

For integers \(A,B\ge0\) and a transverse multiindex \(\beta\), use
\[
Q_{A,B,\beta}(f)=
\sup_{t,z}\langle t\rangle^A\langle z\rangle^B
|\partial_z^\beta f(t,z)|.
\tag{3.2}
\]
Since each separate bracket is at most \(\langle(t,z)\rangle\),
\(Q_{A,B,\beta}(f)\le P_{A+B+|\beta|}(f)\).
For \(s\ge2\), split the integral at \(s/2\). On \(0\le t\le s/2\) its absolute value, after the outside Gaussian and \(\partial_z^\beta\), is at most
\[
s e^{-3s^2/8}\langle z\rangle^{-B}Q_{0,B,\beta}(f).
\]
For \(s/2\le t\le s\), use \(\langle t\rangle\ge\langle s\rangle/2\) and \(s^2-t^2\ge s(s-t)\). The remaining exponential integral satisfies
\[
e^{-s^2/2}\int_{s/2}^s e^{t^2/2}\,dt
\le\int_{s/2}^s e^{-s(s-t)/2}\,dt
\le\frac2s.
\tag{3.3}
\]
The product \(\langle s\rangle^As e^{-3s^2/8}\) is bounded: expand the integer bound \((1+s)^{A+1}\) and maximize each \(s^je^{-3s^2/8}\) by differentiation. As \(Q_{0,B,\beta}\le Q_{A,B,\beta}\), both pieces are controlled.

When \(s=-v\le-2\), substitution \(t=-r\) gives the negative of the same integral over \(0\le r\le v\), with \(f(-r,z)\); its absolute bound is unchanged. When \(|s|\le2\), the length is at most two and \(e^{(t^2-s^2)/2}\le1\) between zero and \(s\). Enlarging the constant therefore proves the global estimate
\[
\sup_{s,z}\langle s\rangle^A\langle z\rangle^B
|\partial_z^\beta R_\nu f(s,z)|
\le C_A Q_{A,B,\beta}(f).
\tag{3.4}
\]

**Proof: every mixed derivative and continuity.** Define polynomials recursively by \(p_0=1\), with all nonexistent \(q_{r,\ell}\) equal to zero, and
\[
\begin{aligned}
p_{r+1}&=p_r'-sp_r,\\
q_{r+1,\ell}&=q_{r,\ell}'+q_{r,\ell-1}
                 +p_r\,\mathbf1_{\{\ell=0\}}
\qquad(0\le\ell\le r).
\end{aligned}
\]
Differentiating \(\partial_sR_\nu f=f-sR_\nu f\) inductively proves
\[
\partial_s^rR_\nu f
=p_r(s)R_\nu f+
\sum_{\ell=0}^{r-1}q_{r,\ell}(s)\partial_s^\ell f.
\tag{3.5}
\]
The recurrences give \(\deg p_r\le r\) and \(\deg q_{r,\ell}\le r-1-\ell\); for the latter, differentiation lowers degree, shifting the index adds the term of exactly the allowed degree, and \(p_r\) has degree at most \(r\) when \(\ell=0\) at the next step. These assertions also hold for zero polynomials.

Choose constants bounding these finitely many polynomials by their indicated powers of \(\langle s\rangle\). Apply (3.4) to \(\partial_z^\beta f\) with weight \(A+r\) in the first term of (3.5). For the remaining terms use the definition of \(P_N\). This gives the explicit finite bound
\[
\begin{split}
\sup_{s,z}\langle s\rangle^A\langle z\rangle^B
|\partial_s^r\partial_z^\beta R_\nu f|
&\le C_{A,r}\left(
Q_{A+r,B,\beta}(f)
+\sum_{\ell<r}
P_{A+B+r+|\beta|+\ell}(f)\right).
\end{split}
\]
An empty sum is zero. Finally
\(\langle(s,z)\rangle^N\le\langle s\rangle^N\langle z\rangle^N\), because
\(1+s^2+|z|^2\le(1+s^2)(1+|z|^2)\).
Set \(A=B=N\) and take the finite maximum over \(r+|\beta|\le N\); monotonicity of \(P_j\) yields
\[
P_N(R_\nu f)\le C_N P_{4N}(f)\qquad(N\ge0).
\]
This proves both Schwartz membership and continuity, with a finite input seminorm for each output seminorm.

**Proof: the complete kernel.** If \(L_\nu w=0\), the integrating factor gives
\(\partial_s(e^{s^2/2}w)=0\). For each \(z\), the scalar fundamental theorem makes that function constant in \(s\), so \(w=e^{-s^2/2}h(z)\). Its trace \(h(z)=w(0,z)\) is Schwartz, since \(P_N(h)\le P_N(w)\).

Conversely, every derivative of \(e^{-s^2/2}\) is a polynomial times that Gaussian, by induction using \(g'=-sg\). The same polynomial-exponential bound used above controls all its weights. Thus for any \(h\in\mathcal S\), each mixed derivative of \(e^{-s^2/2}h(z)\) has all separate weighted bounds, hence all joint bounds. This product lies in \(\mathcal S\) and is killed by \(L_\nu\). Subtracting \(R_\nu f\) from any solution now gives precisely this kernel. \(\square\)

## The operator shifts the Fourier eigenvalue

The coordinate identities from F2 give
\[
TL_\nu=iL_\nu T.
\tag{4.1}
\]
Indeed \(T(x_\nu f)=i\partial_\nu Tf\) and \(T(\partial_\nu f)=ix_\nu Tf\). Thus \(L_\nu E_k(n)\subset E_{k+1}(n)\). The companion \(A_\nu=x_\nu-\partial_\nu\) satisfies \(TA_\nu=-iA_\nu T\).

For \(g_1(s)=e^{-s^2/2}\), F3 proves \(T_1g_1=g_1\), including the constant \(\int g_1=\sqrt{2\pi}\). Define \(p_0=1\) and \(p_{m+1}=2sp_m-p_m'\). Differentiation gives
\[
A^m g_1=p_mg_1,\qquad
T_1(p_mg_1)=(-i)^m p_mg_1.
\]
Induction shows that \(p_m\) has leading coefficient \(2^m\), degree \(m\), and parity \(p_m(-s)=(-1)^mp_m(s)\). For parity, \(2sp_m\) and \(-p_m'\) both have the next parity. The leading term cannot cancel a derivative of smaller degree, proving nonvanishing for every \(m\). No completeness assertion about Hermite expansions is needed.

For comparison, define the probabilists' Hermite polynomials by \(h_0=1\), \(h_{m+1}(x)=xh_m(x)-h_m'(x)\). The chain rule and induction give \(p_m(s)=2^{m/2}h_m(\sqrt2\,s)\). Thus the preceding proved identity is the normalization of [NIST DLMF 18.17.22](https://dlmf.nist.gov/18.17.E22): its substitutions \(x=\sqrt2\,s\), \(y=-\sqrt2\,\xi\) turn the prefactor into \(1/\sqrt{2\pi}\), the Gaussian into \(e^{-s^2/2}\), and the phase into \(e^{-is\xi}\). Parity changes \(i^m h_m(-\sqrt2\,\xi)\) to \((-i)^m h_m(\sqrt2\,\xi)\). The local recurrence proof supplies the whole identity used here.

## Several coordinate equations require compatibility

Set \(g_n(x)=\prod_{j=1}^n g_1(x_j)=e^{-|x|^2/2}\). Absolute Fubini applies to products of Schwartz functions by F1's \(L^1\) estimate. It factors the normalized Fourier transform into the product of the normalized one-dimensional transforms. In particular \(T_ng_n=g_n\).

**Theorem 4.2 (joint Schwartz system).** For \(f_1,\ldots,f_n\in\mathcal S(\mathbb R^n)\), the equations
\[
L_\nu w=f_\nu,\qquad 1\le\nu\le n,
\tag{J1}
\]
have a solution \(w\in\mathcal S\) if and only if
\[
L_\mu f_\nu=L_\nu f_\mu\quad\text{for every }\mu,\nu.
\tag{J2}
\]
On the subspace of compatible tuples there is a continuous linear choice of solution, and all solutions differ by a scalar multiple of \(g_n\). If every datum lies in \(E_{k+1}(n)\), there is a solution in \(E_k(n)\). Within that eigenspace it is unique for \(k=1,2,3\), and has exactly the ambiguity \(\mathbb Cg_n\) for \(k=0\).

**Proof: construct a solution by dimension induction.** For distinct indices, expand \(L_\mu L_\nu\). Coordinate multiplication commutes with the other coordinate derivative, and mixed derivatives commute for smooth functions, so \(L_\mu L_\nu=L_\nu L_\mu\). Equal indices are immediate. Applying these operators to (J1) proves necessity.

In dimension one choose \(R_1f_1\). In larger dimension write \(x=(s,z)\), \(s=x_1\), and let
\[
w_1=R_1f_1,\qquad
a_\nu=f_\nu-L_\nu w_1\quad(\nu>1).
\tag{J3}
\]
Using (J2) and \(L_1w_1=f_1\),
\(L_1a_\nu=L_1f_\nu-L_\nu f_1=0\).
Theorem 3.1 therefore gives
\[
a_\nu(s,z)=e^{-s^2/2}h_\nu(z),\qquad
h_\nu(z)=a_\nu(0,z)\in\mathcal S(\mathbb R^{n-1}).
\tag{J4}
\]
For \(\mu,\nu>1\),
\[
L_\mu a_\nu-L_\nu a_\mu
=L_\mu f_\nu-L_\nu f_\mu
 -(L_\mu L_\nu-L_\nu L_\mu)w_1=0.
\]
The Gaussian depends only on \(s\). Substitute (J4) and set \(s=0\) to obtain the same compatibility for the remaining operators \(L_\nu^z\) acting on the \(h_\nu\). By induction choose \(q\in\mathcal S(\mathbb R^{n-1})\) satisfying \(L_\nu^zq=h_\nu\) for \(\nu>1\), and define
\[
w(s,z)=w_1(s,z)+e^{-s^2/2}q(z).
\tag{J5}
\]
This is Schwartz by the product estimate in Theorem 3.1. The added term is killed by \(L_1\); for \(\nu>1\) it contributes exactly \(a_\nu\). Thus all equations hold.

**Proof: continuity and all ambiguities.** Fix the just-described recursive choice of \(q\). The maps \(L_\nu\), \(R_1\), and the trace \(a\mapsto a(0,z)\) are continuous and linear by F1 and Theorem 3.1. The Gaussian product map \(q\mapsto e^{-s^2/2}q(z)\) is also continuous: for \(r+|\beta|\le N\), its joint weighted derivative is bounded by
\(\sup_s\langle s\rangle^N|g_1^{(r)}(s)|\,P_N(q)\).
Induction and composition now give a continuous linear solution map on compatible tuples. This domain is closed in the product Schwartz topology: each compatibility difference is a continuous map into \(\mathcal S\), whose zero set is closed by evaluation, and there are finitely many such differences.

For the joint kernel, the first equation gives \(v=g_1(s)h(z)\); the others give \(L_\nu^zh=0\). Repeating the one-coordinate kernel computation in all remaining variables gives \(v=cg_n\). Conversely \(L_\nu g_n=0\) for each \(\nu\), so every such difference occurs.

**Proof: select the required eigenspace.** Iterating (4.1) gives \(T_n^jL_\nu=i^jL_\nu T_n^j\). Substitution in (2.1) yields
\[
\begin{aligned}
\Pi_{k+1}^{(n)}L_\nu
&=\frac14\sum_{j=0}^3i^{-(k+1)j}i^jL_\nu T_n^j\\
&=L_\nu\Pi_k^{(n)}.
\end{aligned}
\tag{J6}
\]
If \(w\) is the constructed solution, \(L_\nu\Pi_k^{(n)}w=\Pi_{k+1}^{(n)}f_\nu=f_\nu\). This projects the entire compatible system at once. A difference in \(E_k(n)\) must also be \(cg_n\), and its Fourier equation gives \((1-i^k)c=0\). This is the asserted exact uniqueness or Gaussian ambiguity. \(\square\)

## Exercises

**Exercise 1 (foundation).** Find \(F\delta_0^{(m)}\) and \(F(x^m)\) on the line, retaining all constants. Check their Euler degrees.

**Exercise 2 (intermediate).** Given a normalized Euler chain of length three at \(a\), write its Fourier chain and check all relations and its length.

**Exercise 3 (foundation).** Compute \(\Pi_0+\Pi_2\) and \(\Pi_1+\Pi_3\) using reflection. Describe the even and odd Schwartz subspaces.

**Exercise 4 (intermediate).** For \(g=e^{-x^2/2}\) and \(A=x-\partial_x\), calculate \(Ag\), its Fourier eigenvalue and all its projections.

**Exercise 5 (intermediate).** Calculate \(A^2g\) and \(A^3g\). Prove that each of the four Fourier eigenspaces on the line is nonzero.

**Exercise 6 (foundation).** Find every Schwartz solution of \((x+\partial_x)w=g\).

**Exercise 7 (intermediate).** Find every Schwartz solution on the plane of \((s+\partial_s)w=e^{-s^2/2}ze^{-z^2}\).

**Exercise 8 (advanced).** Show that \(L:E_k(1)\to E_{k+1}(1)\) is onto for every \(k\). Determine its kernel and which maps are bijective with continuous inverse.

**Exercise 9 (advanced).** In every dimension, give a continuous right inverse for \(L_\nu:E_k(n)\to E_{k+1}(n)\) and determine its entire kernel. Use \(\mathcal S(\mathbb R^0)=\mathbb C\), \(T_0=I\). When \(n\ge2\), exhibit a nonzero kernel element for each \(k\), and explain why the line behaves differently.

**Exercise 10 (advanced).** On the plane write \(g_2=e^{-(s^2+z^2)/2}\). Determine all solutions and the indicated eigenspace restrictions for:

(a) \(L_1w=zg_2,\ L_2w=sg_2\), including the unique solution in \(E_2(2)\);

(b) \(L_1w=sg_2,\ L_2w=0\), including every Fourier component and the exact meaning of the \(E_0(2)\) ambiguity;

(c) \(L_1w=zg_2,\ L_2w=0\). Explain the obstruction in (c) despite individual coordinate surjectivity.

## Solutions

**Solution 1.** By definition \((F\delta_0)(\psi)=F\psi(0)=\int\psi\), so \(F\delta_0=1\). Inversion at zero gives \(\int F\psi=2\pi\psi(0)\), hence \(F1=2\pi\delta_0\). Repeated use of the proved coordinate identities yields
\[
F\delta_0^{(m)}=(i\xi)^m,\qquad
F(x^m)=2\pi i^m\delta_0^{(m)}.
\]
For \(r\ge1\), testing \(x\delta_0^{(r)}\) on \(\psi\) gives
\((-1)^r(x\psi)^{(r)}(0)=(-1)^rr\psi^{(r-1)}(0)\), so \(x\delta_0^{(r)}=-r\delta_0^{(r-1)}\); also \(x\delta_0=0\). Therefore \(E\delta_0^{(m)}=-(m+1)\delta_0^{(m)}\), whereas \(E(x^m)=mx^m\). These degrees obey \(a\mapsto-a-1\).

**Solution 2.** Set \(w_0=Fv_0\), \(w_1=-Fv_1\), \(w_2=Fv_2\). Theorem 1.1 permits all three transforms. Equation (1.2) gives
\[
(E+a+1)w_0=0,\quad
(E+a+1)w_1=Fv_0=w_0,\quad
(E+a+1)w_2=-Fv_1=w_1.
\]
Since \(v_0\ne0\), invertibility implies \(w_0\ne0\). Thus the second iterated image of \(w_2\) is nonzero and its third is zero: the length is exactly three.

**Solution 3.** In (2.1), the coefficients for \(k=0,2\) add to zero when \(j\) is odd and to \(1/2\) when \(j\) is even. Hence
\(\Pi_0+\Pi_2=(I+T^2)/2=(I+\mathcal R)/2\).
Subtracting from \(I\) gives \(\Pi_1+\Pi_3=(I-\mathcal R)/2\). A function fixed by reflection is its even projection, so the even subspace is \(E_0\oplus E_2\); a function negated by reflection is its odd projection, so the odd subspace is \(E_1\oplus E_3\). Directness follows by applying the individual \(\Pi_k\).

**Solution 4.** The Gaussian identity in F3 is \(Fg=\sqrt{2\pi}g\), so \(Tg=g\). Differentiation gives \(g'=-xg\), hence \(Ag=2xg\). Since \(TA=-iAT\), \(TAg=-iAg=i^3Ag\). Theorem 2.1 gives \(\Pi_3Ag=Ag\) and the other three projections zero. Nonvanishing follows, for example, by evaluation at \(x=1\).

**Solution 5.** The product rule gives \(A(pg)=(2xp-p')g\). Starting with \(p=2x\) yields \(A^2g=(4x^2-2)g\), and one more application yields \(A^3g=(8x^3-12x)g\). Their eigenvalues are respectively \((-i)^2=-1\) and \((-i)^3=i\). Together with \(g\) and \(Ag\), these provide nonzero elements of all four eigenspaces: their polynomials have nonzero leading coefficients, and the Gaussian never vanishes.

**Solution 6.** Formula (3.1) gives \(Rg=e^{-x^2/2}\int_0^x1\,dt=xg\). The full kernel gives exactly \(w=(x+c)g\), \(c\in\mathbb C\). All these functions are Schwartz, and direct differentiation gives \(L(xg)=g\), \(L(cg)=0\).

**Solution 7.** The same integral gives the particular solution \(s e^{-s^2/2}ze^{-z^2}\). Every solution, and no others, is
\[
w(s,z)=e^{-s^2/2}\bigl(sz e^{-z^2}+h(z)\bigr),
\qquad h\in\mathcal S(\mathbb R).
\]
The terms are Schwartz by the separate weighted derivative bounds, and differentiating in \(s\) verifies the equation. Subtraction reduces any other solution to the whole kernel of Theorem 3.1.

**Solution 8.** For \(f\in E_{k+1}(1)\), let \(w=\Pi_k Rf\). Equation (J6) gives \(Lw=\Pi_{k+1}LRf=f\), proving surjectivity with a continuous right inverse. The unrestricted kernel is \(\mathbb Cg\), entirely in \(E_0(1)\). Its intersection with \(E_k(1)\) is therefore \(\mathbb Cg\) for \(k=0\), and zero for \(k=1,2,3\). The last three maps are bijections; their right inverse \(\Pi_kR\) is necessarily their inverse and is continuous.

**Solution 9.** For every \(n\ge1\), define on \(E_{k+1}(n)\)
\[
S_{\nu,k}f=\Pi_k^{(n)}R_\nu f,\qquad
L_\nu S_{\nu,k}f=\Pi_{k+1}^{(n)}L_\nu R_\nu f=f.
\tag{J7}
\]
This is continuous by Theorems 2.1 and 3.1. The unrestricted kernel is \(v(s,z)=g_1(s)h(z)\). Fubini and the Gaussian transform give, at frequency coordinates again denoted by \((s,z)\),
\[
T_nv(s,z)=g_1(s)\,(T_{n-1}h)(z).
\tag{J8}
\]
Thus \(v\in E_k(n)\) if and only if \(h\in E_k(n-1)\), since \(g_1\) never vanishes. This proves the entire restricted kernel, including dimension one: \(T_0=I\) gives \(E_0(0)=\mathbb C\), and \(E_1(0)=E_2(0)=E_3(0)=0\).

For \(n\ge2\), choose a transverse coordinate \(z_1\) and use the four already computed polynomials
\[
p_0=1,\qquad p_1=2z_1,\qquad
p_2=4z_1^2-2,\qquad p_3=8z_1^3-12z_1.
\]
Set
\[
v_k(x)=p_m(z_1)g_n(x),\qquad
m\in\{0,1,2,3\},\quad m\equiv-k\pmod4.
\tag{J9}
\]
The \(z_1\) factor has eigenvalue \((-i)^m=i^k\), and all other Gaussian factors have eigenvalue one; absolute Fubini multiplies these eigenvalues. Each \(v_k\) is nonzero and \(L_\nu v_k=0\), since its polynomial is independent of \(s=x_\nu\). All four restricted kernels are therefore nonzero. On the line there is no transverse factor, leaving only the Gaussian line in \(E_0\).

**Solution 10.** For any polynomial \(p(s,z)\), cancellation of Gaussian derivatives gives
\(L_1(pg_2)=(\partial_sp)g_2\) and \(L_2(pg_2)=(\partial_zp)g_2\).

In (a), \(p=sz\) supplies both outputs. The joint kernel theorem gives all solutions \(w=(sz+c)g_2\). Each one-dimensional factor \(xg_1\) has eigenvalue \(-i\), so \(szg_2\) lies in \(E_2(2)\), while \(cg_2\) lies in \(E_0(2)\). The projections are independent, so \(c=0\) is exactly the unique \(E_2(2)\) solution. Both data have eigenvalue \(-i=i^3\), agreeing with the shift.

In (b), \(p=s^2/2\) supplies the two outputs. Again the full set is \(w=(s^2/2+c)g_2\). The exact decomposition is
\[
\begin{aligned}
\tfrac12s^2&=\tfrac18(4s^2-2)+\tfrac14,\\
w&=\tfrac18(4s^2-2)g_2+(c+\tfrac14)g_2.
\end{aligned}
\tag{J10}
\]
The first component is nonzero in \(E_2(2)\), and the second belongs to \(E_0(2)\). Hence exactly \(c=-1/4\) gives a single-eigenspace solution, in \(E_2(2)\); every other solution has both components. There is no \(E_0(2)\) solution: its first output would lie in \(E_1(2)\), whereas the nonzero datum \(sg_2\) lies in \(E_3(2)\). The complete \(E_0(2)\) ambiguity refers to differences of unrestricted solutions, which are exactly \(\mathbb Cg_2\), not to an \(E_0(2)\) solution for these data.

In (c), \(L_2(zg_2)=g_2\ne0=L_1(0)\), violating (J2). Thus no common Schwartz solution exists. Individual coordinate surjectivity does not remove the proved compatibility condition for a tuple.

## References

- Michael E. Taylor, [*Fourier Analysis, Distributions, and Constant-Coefficient Linear PDE*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/fourier.pdf), free author notes, Section 3, formulas (3.11)–(3.24), PDF pages 26–28. The Gaussian differential-equation calculation is compared with F3's fully supplied mass and transform proof. The complex continuation and \(L^2\) assertions on those pages are not inputs.
- NIST, [*Digital Library of Mathematical Functions*, 18.17.22](https://dlmf.nist.gov/18.17.E22), freely readable Hermite transform formula. The recurrence, parity and normalization needed here are proved above.
- [U019](euler-equations-and-singularity-order.md), Theorems 2.1–2.2, gives the full homogeneous and generalized Euler classification used in Theorem 1.1. [F1–F5](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md) gives the complete Schwartz and Fourier input. The linked scalar, algebra and integration components retain their own licences.
