# Polar cutoffs from finite spectral partitions

*Original local proof by GPT-6 Astra (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights held.*

This proof uses the single-operator spectral calculus in [SF, SB4–SB6 and SF1](OA-FLOW-SF.md#oa-flow.sf.sb4), scalar dominated convergence in [SC5](OA-FLOW-SC.md#sc-05), and the scalar interchange proof at the start of [FF](OA-FLOW-FF.md#oa-flow.ff.1). The standard form, its cone representatives and the finite matrix standard form are the actual constructions [NC4](OA-FLOW-NC.md#oa-flow.nc.4), [CR6–CR8](OA-FLOW-CR.md#oa-flow.cr.6), and [MC2–MC4](OA-FLOW-MC.md#oa-flow.mc.2). A joint spectral theorem for two operators is not an input.

Exact individual earlier proof locators: [OA-FLOW.CF.8](OA-FLOW-CF.md#oa-flow.cf.8), [OA-FLOW.CR.8](OA-FLOW-CR.md#oa-flow.cr.8), [OA-FLOW.FF.1](OA-FLOW-FF.md#oa-flow.ff.1), [OA-FLOW.MC.2](OA-FLOW-MC.md#oa-flow.mc.2), [OA-FLOW.MC.3](OA-FLOW-MC.md#oa-flow.mc.3), [OA-FLOW.MC.4](OA-FLOW-MC.md#oa-flow.mc.4), [OA-FLOW.NC.4](OA-FLOW-NC.md#oa-flow.nc.4), [OA-FLOW.PC.1](OA-FLOW-PC.md#oa-flow.projection.pc1), [OA-FLOW.SC.3](OA-FLOW-SC.md#sc-03), [OA-FLOW.SC.4](OA-FLOW-SC.md#sc-04), [OA-FLOW.SC.5](OA-FLOW-SC.md#sc-05), [OA-FLOW.SC.6](OA-FLOW-SC.md#sc-06), [OA-FLOW.SF.SB4](OA-FLOW-SF.md#oa-flow.sf.sb4), [OA-FLOW.SF.SB5](OA-FLOW-SF.md#oa-flow.sf.sb5), [OA-FLOW.SF.SB6](OA-FLOW-SF.md#oa-flow.sf.sb6), [OA-FLOW.SF.SF1](OA-FLOW-SF.md#oa-flow.sf.sf1).

<a id="oa-flow.fp.1"></a>

## FP1. Conventions and the exact scalar inequality

Let \(M\) be any von Neumann algebra in its standard form \((M,H,J,P)\), with no separability assumption. Fix \(\phi\in M_*^+\), let \(\xi\in P\) be its representing vector, and set

<a id="equation-fp1"></a>

\[
R_x=Jx^*J,\qquad
c_\phi(x)=\|(x-R_x)\xi\|,\qquad
I_\phi(x)=\tfrac12c_\phi(x)^2,\qquad
q_\phi(x)^2=\phi(x^*x+xx^*).
\tag{FP1}
\]
Thus \(R\) is a linear anti-representation, \(R_x^*=R_{x^*}\), and \(R(M)\) commutes with \(M\). Since \(J\xi=\xi\),

<a id="equation-fp2"></a>

\[
\|x\xi\|^2=\phi(x^*x),\quad
\|R_x\xi\|^2=\phi(xx^*),\quad
J(x-R_x)\xi=-(x^*-R_{x^*})\xi.
\tag{FP2}
\]
In particular \(c_\phi(x)=c_\phi(x^*)\). Every operator applied here is bounded.

For \(a>0\), define the real Borel function
\[
g_a(t)=\operatorname{sign}(t)\,1_{[a,\infty)}(t^2),\qquad \operatorname{sign}(0)=0.
\]
For real \(s,t\), direct integration of this step function gives

<a id="equation-fp3"></a>

\[
K(s,t):=\int_0^\infty|g_a(s)-g_a(t)|^2\,da
=\begin{cases}|s^2-t^2|,&st\ge0,\\
A^2+3B^2,&st<0,\end{cases}
\quad A=\max(|s|,|t|),\quad B=\min(|s|,|t|).
\tag{FP3}
\]
For opposite signs the integrand is \(4\) on \(0<a\le B^2\), \(1\) on \(B^2<a\le A^2\), and zero after \(A^2\). For equal signs it is \(1\) between the two squared absolute values and zero elsewhere. Values at the finitely many endpoints do not affect the integral. In both cases,

<a id="equation-fp4"></a>

\[
K(s,t)\le |s-t|(|s|+|t|).
\tag{FP4}
\]
In the opposite-sign case the difference between the right side and the left side is \(2B(A-B)\ge0\); in the equal-sign case there is equality.

<a id="oa-flow.fp.2"></a>

## FP2. The finite partition argument

First let \(h=h^*\) have finite spectrum and write
\[
h=\sum_{i=1}^m t_i e_i,\qquad
e_i e_j=0\ (i\ne j),\qquad \sum_i e_i=1.
\]
Zero spectral projections may be omitted. The bounded projections
\[
Q_{ij}=L_{e_i}R_{e_j}
\]
commute within each product. The \(Q_{ij}\) are mutually orthogonal, sum to the identity, and require no measure construction. Put
\[
\mu_{ij}=\|Q_{ij}\xi\|^2\ge0.
\]
Orthogonality, first summing over \(j\) and then over \(i\), gives

<a id="equation-fp5"></a>

\[
\sum_j\mu_{ij}=\|e_i\xi\|^2=\phi(e_i),\qquad
\sum_i\mu_{ij}=\|R_{e_j}\xi\|^2=\phi(e_j).
\tag{FP5}
\]
For every real function \(g\) on this finite spectrum,

<a id="equation-fp6"></a>

\[
2I_\phi(g(h))=\sum_{i,j}|g(t_i)-g(t_j)|^2\mu_{ij}.
\tag{FP6}
\]
Indeed \(L_{g(h)}-R_{g(h)}\) acts on \(Q_{ij}H\) by the scalar \(g(t_i)-g(t_j)\). Integrating this finite sum and using FP4 and the finite Cauchy–Schwarz inequality yields

<a id="equation-fp7"></a>

\[
\begin{aligned}
\int_0^\infty I_\phi(g_a(h))\,da
&\le \tfrac12\sum_{i,j}|t_i-t_j|(|t_i|+|t_j|)\mu_{ij}\\
&\le\tfrac12
\left(\sum_{i,j}|t_i-t_j|^2\mu_{ij}\right)^{1/2}
\left(\sum_{i,j}(|t_i|+|t_j|)^2\mu_{ij}\right)^{1/2}\\
&\le\tfrac12(2I_\phi(h))^{1/2}(4\phi(h^2))^{1/2}
=I_\phi(h)^{1/2}q_\phi(h).
\end{aligned}
\tag{FP7}
\]
The last inequality uses \((|s|+|t|)^2\le2(s^2+t^2)\) and the two marginals FP5. All sums are finite.

<a id="oa-flow.fp.3"></a>

## FP3. Passage to a general bounded selfadjoint element

Let \(h=h^*\in M\), \(B=\|h\|\). Choose finite real Borel step functions \(f_n\) on \([-B,B]\) with
\[
\sup_{|t|\le B}|f_n(t)-t|\le 1/n,\qquad |f_n(t)|\le B+1.
\]
For example use the lower endpoints of the finitely many intervals obtained by intersecting \([-B,B]\) with intervals of length \(1/n\), and define any final endpoint separately. Put \(h_n=f_n(h)\). The single-operator spectral calculus gives \(h_n\in M_{\rm sa}\), finite spectrum, and \(\|h_n-h\|\le1/n\). The right operators converge in norm too. Hence

<a id="equation-fp8"></a>

\[
I_\phi(h_n)\longrightarrow I_\phi(h),\qquad
q_\phi(h_n)\longrightarrow q_\phi(h).
\tag{FP8}
\]

Here are the necessary details for the discontinuous cutoffs. Let
\[
\nu(C)=\langle 1_C(h)\xi,\xi\rangle .
\]
This is a finite positive Borel measure. The scalar measure for the right spectral projections \(R_{1_C(h)}=J1_C(h)J\), at the same vector, is also \(\nu\), by FP2. A finite measure has at most countably many atoms: for each positive integer \(k\), only finitely many points have mass at least \(1/k\), and every positive atom belongs to one such set. Consequently
\[
\mathcal E=\{t^2:t\ne0,\ \nu(\{t\})>0\}
\]
is countable. If \(a>0\) is outside \(\mathcal E\), the only possible discontinuities of \(g_a\), namely \(\pm\sqrt a\), have zero \(\nu\)-mass. At every other \(t\), \(g_a(f_n(t))\to g_a(t)\). Since \(|g_a|\le1\), scalar dominated convergence in the single spectral measure proves

<a id="equation-fp9"></a>

\[
g_a(h_n)\xi\longrightarrow g_a(h)\xi,\qquad
R_{g_a(h_n)}\xi\longrightarrow R_{g_a(h)}\xi.
\tag{FP9}
\]
The second assertion can also be obtained by applying \(J\) to the first, because these functions are real and \(J\xi=\xi\). Thus \(I_\phi(g_a(h_n))\to I_\phi(g_a(h))\) for Lebesgue-almost every \(a>0\).

The functions of \(a\) in this assertion are measurable. To see this without assuming a vector-valued spectral theorem, approximate \(a>0\) from below by \(a_k=2^{-k}\lfloor2^k a\rfloor\). For sufficiently large \(k\), \(a_k>0\), and \(a_k\uparrow a\). The positive and negative spectral tails defining \(g_{a_k}(h)\xi\) converge in norm to those for \(g_a(h)\xi\), by continuity from above of \(\nu\). Each approximating vector function is countably stepwise constant. The same holds on the right, so the squared commutator norm is a pointwise limit of measurable scalar functions.

For all \(n\) and \(a>0\),

<a id="equation-fp10"></a>

\[
0\le I_\phi(g_a(h_n))
\le2\|\xi\|^2\,1_{(0,(B+1)^2]}(a).
\tag{FP10}
\]
This follows from the two norm bounds \(\|g_a(h_n)\xi\|,\|R_{g_a(h_n)}\xi\|\le\|\xi\|\), and the spectral bound on \(h_n\). The right side is Lebesgue integrable. A second application of scalar dominated convergence, now in \(a\), together with FP7–FP8 proves

<a id="equation-fp11"></a>

\[
\int_0^\infty I_\phi(g_a(h))\,da
\le I_\phi(h)^{1/2}q_\phi(h).
\tag{FP11}
\]
This proves the required continuous-spectrum step using only finite atomic arrays and single-operator spectral measures. No joint measure, extension of rectangle coefficients, or two-variable spectral synthesis has been used.

<a id="oa-flow.fp.4"></a>

## FP4. Polar cutoffs of an arbitrary element

Let \(x=v|x|\in M\) be the polar decomposition supplied by SF/PC1. For \(a>0\) set
\[
v_a=v\,1_{[\sqrt a,\infty)}(|x|).
\]
Then

<a id="equation-fp12"></a>

\[
v_a^*v_a=1_{[a,\infty)}(x^*x),\qquad
v_av_a^*=1_{[a,\infty)}(xx^*).
\tag{FP12}
\]
The second equality follows by transporting the spectral calculus through the polar isometry from the support of \(|x|\) to the support of \(|x^*|\); the threshold is positive, so neither kernel contributes. Integrating \(1_{[a,\infty)}(\lambda)\) in \(a>0\) gives \(\lambda\). Scalar interchange in the finite vector spectral measures therefore gives

<a id="equation-fp13"></a>

\[
\int_0^\infty q_\phi(v_a)^2\,da=q_\phi(x)^2.
\tag{FP13}
\]

Use the actual matrix standard form MC2–MC4 for \(M_2(M)\), with Hilbert space \(H^{2\times2}\), componentwise left matrix multiplication, and \(J_2(\zeta)_{ij}=J\zeta_{ji}\). The positive functional \(\Theta([a_{ij}])=\phi(a_{11})+\phi(a_{22})\) has cone vector \(\operatorname{diag}(\xi,\xi)\), also when \(\phi\) is zero or nonfaithful. For
\[
H_x=\begin{pmatrix}0&x^*\\x&0\end{pmatrix}
\]
one has

<a id="equation-fp14"></a>

\[
I_\Theta(H_x)=2I_\phi(x),\quad
q_\Theta(H_x)^2=2q_\phi(x)^2,\quad
g_a(H_x)=\begin{pmatrix}0&v_a^*\\v_a&0\end{pmatrix}.
\tag{FP14}
\]
The first identity is the sum of the squared norms of the two commutator entries, which agree by FP2. For the last identity, \(H_x^2=\operatorname{diag}(x^*x,xx^*)\); multiply its spectral cutoff by the sign of \(H_x\), whose off-diagonal entries are \(v^*,v\). This is bounded single-operator Borel calculus, including the zero kernel. Apply FP11 to \(H_x\), use FP14 both before and after cutoff, and divide by \(2\). The result is

<a id="equation-fp15"></a>

\[
\boxed{\displaystyle
\int_0^\infty I_\phi(v_a)\,da\le I_\phi(x)^{1/2}q_\phi(x).}
\tag{FP15}
\]
The integrand is measurable by the selfadjoint matrix argument FP3, and has bounded support. The statement holds for every bounded \(x\) and every normal positive finite functional, with no faithfulness assumption.

<a id="oa-flow.fp.5"></a>

## FP5. The strict cutoff selection and its necessary premise

Suppose \(\eta>0\), \(q_\phi(x)>0\), and \(I_\phi(x)\le\eta q_\phi(x)^2\). There is \(a>0\) with

<a id="equation-fp16"></a>

\[
q_\phi(v_a)>0,\qquad
I_\phi(v_a)<2\sqrt\eta\,q_\phi(v_a)^2.
\tag{FP16}
\]
Otherwise \(I_\phi(v_a)\ge2\sqrt\eta\,q_\phi(v_a)^2\) whenever the latter mass is positive. It also holds at every zero-mass point, since the left side is nonnegative. Integrating and using FP13 and FP15 would imply
\[
2\sqrt\eta\,q_\phi(x)^2\le
\int I_\phi(v_a)\,da\le
\sqrt\eta\,q_\phi(x)^2,
\]
which contradicts the two strict premises. In the normalization \(s_\phi(x)=q_\phi(x)/\sqrt2\), FP16 implies

<a id="equation-fp17"></a>

\[
c_\phi(v_a)<\sqrt8\,\eta^{1/4}s_\phi(v_a).
\tag{FP17}
\]
Positive mass cannot be replaced by \(x\ne0\) for a nonfaithful functional. In \(M_2\), take \(\phi(z)=z_{11}\) and \(x=E_{22}\). The input inequality holds with both sides zero, while no nonzero cutoff has positive mass. This example is included in the theorem's scope rather than discarded by a faithfulness assumption.
