# Modular covariance through positive multipliers and operator averages

The modular theorem relates three kinds of data: the closed involution of a Hilbert algebra, its bounded multiplication operators, and the unitary powers of its positive modular operator. We prove the theorem for the full completion of any left Hilbert algebra on any Hilbert space. In particular, the conclusion concerns every bounded multiplication vector, including vectors outside the involution domains. A faithful normal semifinite weight enters only in Section 7.

The bounded-vector reduction in Section 1 is the polar-multiplier argument of [Combes, Lemmas 2.3–2.5, printed pp.51–52](https://www.numdam.org/item/CM_1971__23_1_49_0.pdf#page=4). The relation between opposite multiplication, resolvents and modular averages is classical; a free account is [Boey, Theorem 4.12 and Lemmas 4.13–4.14, Proposition 4.15 and Corollaries 4.16–4.18, printed pp.32–40](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/245c2a41-48ee-4c8d-ad38-95a8353dc3d1/content#page=38). Here the argument is organized around positive multipliers and an averaging certificate. We construct the operator average by solving a bounded semigroup equation, verify the certificate on the complete graph domains, and then use the positive-multiplier reduction to recover the whole bounded-vector spaces. These references identify antecedents; all mathematical premises are the proved programme inputs below.

<a id="oa-flow.mf06.1"></a>

## Earlier definitions and analytic inputs

Inner products are linear in the first variable. We use the following exact earlier interfaces.

| Proved input | Scope used here |
| --- | --- |
| [CI-1–3](OA-FLOW-CI.md#oa-flow.ci.1) | Conjugate-linear adjoints, closed involutions, their polar operators and complete spectral domains |
| [HA-R1–2 and HA-R7](OA-FLOW-HA-R.md#oa-flow.ha-r.1), also on the opposite algebra | Injective bounded multipliers, their ideals, adjoints and the full adjoint-intersection criterion |
| [HA-R3–5](OA-FLOW-HA-R.md#oa-flow.ha-r.3), also on the opposite algebra | Closed affiliated multipliers, their actual adjoint test domains, polar transport and cutoff membership |
| [HA-R5–6](OA-FLOW-HA-R.md#oa-flow.ha-r.5) | The complete dual involution, graph cores, density and generation of the commutant |
| [WH-04 Sections 2–4](OA-FLOW-WH04.md#oa-flow.wh04.2) | Full completion with unchanged closed involution, full left/right testing algebras and mixed products on all bounded vectors |
| [SF SB-1–SB-6](OA-FLOW-SF.md#oa-flow.sf.sb1) | Borel calculus, bounded polar operations, spectral powers with integral domains, cutoffs, spectral convergence and the concrete ultraweak vector-series convention |
| [MF-SB SB-1–SB-4](OA-FLOW-MF-SB.md#oa-flow.mf-sb.2) | Strong vectorwise integrals, the scalar hyperbolic-cosine transform and continuous integrable Fourier uniqueness |
| [CF Section 1](OA-FLOW-CF.md#oa-flow.cf.1), through the same integration bridge | Norm integrals on compact intervals, their estimates and the fundamental theorem used for the bounded semigroup equation |
| [NF-5](OA-FLOW-NF.md#oa-flow.nf.5), [ST-2](OA-FLOW-ST12.md#oa-flow.st.2), [WR-3–5](OA-FLOW-WR.md#wr-3), only in Section 7 | The faithful normal GNS image, its normal inverse, and the complete finite-ideal/full-algebra correspondence for every faithful n.s.f. weight |

The measure, Gaussian and rectangle arguments behind MF-SB are its earlier CF/SC/FF/SF inputs. The general Hilbert-algebra proof uses neither a weight-recovery theorem nor a later KMS or natural-cone theorem.

<a id="oa-flow.mf06.2"></a>

## Data and the full statement

Let \(C\) be a left Hilbert algebra, \(H\) its Hilbert completion, \(A\) its full left completion and \(D\) the full right algebra. Write \(B_l,B_r\) for the entire left- and right-bounded vector spaces. The earlier completion and duality theorems give

\[
M=\lambda(A)'',\qquad M'=R(D)'',\qquad
A=B_l\cap D(S),\qquad D=B_r\cap D(F),\qquad F=S^*.
\tag{MF0}
\]

The multiplier maps are injective, take values respectively in \(M,M'\), and satisfy

\[
\lambda_v w=R_wv\quad(v\in B_l,\ w\in B_r),\qquad
\lambda_{Sv}=\lambda_v^*\quad(v\in A),\qquad
R_{Fw}=R_w^*\quad(w\in D).
\tag{MF1}
\]

The products are \(vq=\lambda_vq\) in \(A\) and \(wz=R_z w\) in \(D\). In particular, the right representation reverses the product. CI supplies

\[
S=J\Delta^{1/2},\quad F=J\Delta^{-1/2},\quad
\Delta=FS,\quad J^2=I,\quad J\Delta J=\Delta^{-1},
\tag{MF2}
\]

where \(\Delta\) is positive, injective and self-adjoint. These are equalities with their full domains; in particular
\(D(S)=D(\Delta^{1/2})\) and \(D(F)=D(\Delta^{-1/2})\). For \(U_t=\Delta^{it}\), anti-linear spectral transport gives

\[
JU_t=U_tJ,\qquad SU_t=U_tS,\qquad FU_t=U_tF,
\tag{MF3}
\]

on the respective domains. The right algebra, regarded as the left algebra \(D^{\mathrm{op}}\), has polar data \(J,\Delta^{-1}\) and full partner \(A\).

**Theorem.** For every real \(t\),

\[
\begin{gathered}
JB_l=B_r,\qquad JB_r=B_l,\qquad JA=D,\qquad JD=A,\qquad JMJ=M',\\
U_tB_l=B_l,\qquad U_tB_r=B_r,\qquad U_tA=A,\qquad U_tD=D,\\
\lambda_{U_tv}=U_t\lambda_vU_{-t}\quad(v\in B_l),\qquad
R_{U_tw}=U_tR_wU_{-t}\quad(w\in B_r),\\
R_{Jv}=J\lambda_vJ\quad(v\in B_l),\qquad
\lambda_{Jw}=JR_wJ\quad(w\in B_r),\\
U_tMU_{-t}=M,\qquad U_tM'U_{-t}=M'.
\end{gathered}
\tag{MF-T}
\]

The restrictions of \(U_t\) are involution-preserving algebra automorphisms. The map \(J:A\to D\) is a conjugate-linear involution-preserving anti-isomorphism. Conjugation by \(U_t\) is pointwise strong* continuous on the represented algebras. The original algebra \(C\) need not itself be invariant; its full completion has the same \(S,J,\Delta\) and generated algebra as \(C\).

## 1. Positive multipliers reduce the whole-vector problem

<a id="oa-flow.mf06.polar-reduction"></a>

The difference between a full Hilbert algebra and its bounded-vector space is a domain condition. A positive multiplier restores that condition automatically.

If \(x\in M\) and \(v\in B_l\), then for \(z\in D\)
\(R_zxv=xR_zv=x\lambda_vz\). Hence

\[
xv\in B_l,\qquad\lambda_{xv}=x\lambda_v.
\tag{MF-P1}
\]

Similarly, for \(y\in M'\) and \(w\in B_r\), testing against \(a\in A\) gives
\(\lambda_ayw=y\lambda_aw=yR_wa\), so
\(yw\in B_r\) and \(R_{yw}=yR_w\).

Take the bounded polar decomposition \(\lambda_v=uh\) in \(M\), where \(h\geq0\) and \(u\) is its partial isometry. Put \(\eta=u^*v\). Then (MF-P1) gives \(\lambda_\eta=h\). The adjoint-intersection theorem says that a bounded multiplication vector whose multiplier and its adjoint are multipliers belongs to the full algebra. Thus

\[
\eta\in A,\qquad S\eta=\eta,\qquad v=u\eta.
\tag{MF-P2}
\]

For the last equality, \(\lambda_{u\eta}=uh=\lambda_v\), and injectivity of the multiplier map identifies the vectors. This proves the vector support identity rather than assuming it from the operator support. The same argument in \(M'\) gives, for every \(w\in B_r\), a factorization

\[
w=y\zeta,\qquad y\in M',\quad \zeta\in D,\quad F\zeta=\zeta.
\tag{MF-P3}
\]

Consequently algebra-level identities will suffice for the whole bounded-vector part of (MF-T). Suppose a unitary \(V\) satisfies \(VA=A\) and \(\lambda_{V\eta}=V\lambda_\eta V^*\) on \(A\). Taking generated algebras gives \(VMV^*=M\). For (MF-P2),

\[
Vv=(VuV^*)V\eta\in B_l,\qquad
\lambda_{Vv}=(VuV^*)\lambda_{V\eta}=V\lambda_vV^*.
\tag{MF-P4}
\]

Substituting \(V^*\eta\in A\) into the assumed covariance shows that \(V^*\) satisfies the same conditions. Applying (MF-P4) to \(V^*\) therefore gives equality of the entire spaces. The same assertion holds on the right. No assertion about the domain of \(v\) occurs here.

Likewise, if \(JA=D\), \(R_{J\eta}=J\lambda_\eta J\) on \(A\), and \(JMJ=M'\), then

\[
Jv=(JuJ)J\eta\in B_r,\qquad
R_{Jv}=(JuJ)R_{J\eta}=J\lambda_vJ.
\tag{MF-P5}
\]

The symmetric statement and \(J^2=I\) give both surjectivities. The remaining task is therefore to establish the algebra-level identities. We do this by identifying two averages of the same multiplication operation.

<a id="oa-flow.mf06.6"></a>

## 2. Operator averages from a bounded semigroup equation

The scalar bridge proves

\[
\int_{\mathbb R}\frac{e^{ixt}}{2\cosh(\pi t)}\,dt
=\frac1{2\cosh(x/2)}\quad(x\in\mathbb R).
\tag{MF-A1}
\]

For \(s>0\), put
\(k_s(t)=s^{-1/2}e^{-it\log s}/(2\cosh(\pi t))\). Its two consequences are

\[
\int k_s(t)e^{it\log(a/b)}\,dt=\frac{\sqrt{ab}}{a+sb}\quad(a,b>0),
\qquad \int |k_s(t)|\,dt=\frac1{2\sqrt s}.
\tag{MF-A2}
\]

Define, on bounded operators and Hilbert vectors respectively,

\[
\mathcal A_s(X)=\int k_s(t)U_tXU_{-t}\,dt,\qquad
K_s=\int k_s(t)U_t\,dt
=\Delta^{1/2}(\Delta+s)^{-1}.
\tag{MF-A3}
\]

These are strong vectorwise integrals, with bounds
\(\|\mathcal A_s(X)\|\leq\|X\|/(2\sqrt s)\) and
\(\|K_s\|\leq1/(2\sqrt s)\). Each individual vector integrand is norm continuous; MF-SB constructs its compact Riemann integrals and controls the tails. This construction makes no separability or operator-norm-continuity assertion.

To verify the formula for \(K_s\), first restrict to a spectral interval \([1/n,n]\) and approximate \(\Delta\) there by finite positive spectral step functions. For a spectral value \(a\), (MF-A2) with \(b=1\) is precisely the claimed formula. Uniform convergence on that interval gives the equality there. The positive spectral projections increase strongly to \(I\); the common bound \(1/(2\sqrt s)\) permits their removal from both sides. This proves the identity as a bounded operator on all \(H\).

We next characterize the operator average without an inverse theorem for holomorphic groups. Let \(D_0\) be bounded positive invertible, with \(mI\leq D_0\leq MI\), and let \(X\) be bounded. Consider the equation

\[
D_0Y+sYD_0=D_0^{1/2}XD_0^{1/2}.
\tag{MF-A4}
\]

It has a unique bounded solution,

\[
L_{s,D_0}(X)=\int_0^\infty
e^{-rD_0}D_0^{1/2}XD_0^{1/2}e^{-srD_0}\,dr.
\tag{MF-A5}
\]

Indeed, the integrand is norm continuous and is bounded by
\(M\|X\|e^{-(1+s)mr}\). Thus its norm integral exists, by compact integration and the scalar tail bound. Bounded spectral calculus gives norm differentiation of each exponential: the scalar difference quotients converge uniformly on \([m,M]\). Differentiating the integrand and applying the compact fundamental theorem gives (MF-A4) after the exponential tail is removed. If \(D_0Y+sYD_0=0\), then \(e^{-rD_0}Ye^{-srD_0}\) has zero norm derivative. It is constant, and its norm tends to zero, so \(Y=0\). This proves uniqueness directly.

Since \(\log D_0\) is bounded, \(t\mapsto D_0^{it}XD_0^{-it}\) is operator-norm continuous, so its kernel integral is an operator-norm integral. The solution is also this modular average:

\[
L_{s,D_0}(X)=\int_{\mathbb R}k_s(t)D_0^{it}XD_0^{-it}\,dt.
\tag{MF-A6}
\]

For \(D_0=\sum_j a_jp_j\), the \((j,l)\) block of (MF-A5) is
\(\sqrt{a_ja_l}(a_j+sa_l)^{-1}p_jXp_l\), by the elementary exponential integral. Equation (MF-A2) gives the identical block in (MF-A6). For general \(D_0\), choose finite spectral step functions within \([m,M]\) converging uniformly to the identity function. Their positive square roots and their exponential functions converge in norm at each fixed \(r\); the common exponential bound gives convergence of (MF-A5). Their imaginary powers converge in norm at each fixed \(t\), and \(|k_s|\) gives convergence of (MF-A6). Thus the equality passes to the limit.

Multiplying (MF-A4) on the left and right by \(D_0^{-1/2}\) now proves the following inversion rule: the unique bounded \(Y\) satisfying

\[
X=D_0^{1/2}YD_0^{-1/2}
  +sD_0^{-1/2}YD_0^{1/2}
\tag{MF-A7}
\]

is the modular average in (MF-A6). The semigroup construction takes place only for bounded positive invertible \(D_0\). For an unbounded modular operator we will use this rule on bounded spectral compressions; no unbounded semigroup equation or globally defined unbounded operator product is being assumed.

<a id="oa-flow.mf06.3"></a>

## 3. Graph regularization of an opposite multiplication vector

The averages in Section 2 are bounded operators. To connect them with multiplication, we need a regularization that actually lies in the full algebra. Fix \(s>0\) and \(w\in D\), and set \(v=(\Delta+s)^{-1}w\). Bounded spectral calculus puts \(v\) in \(D(\Delta)\).

For any \(v\in D(S)\), the opposite version of HA-R3 closes the map \(z\mapsto R_zv\), initially defined on \(D\), to an affiliated operator \(T_v\). In particular,

\[
T_v\text{ is affiliated with }M,\qquad
D\subseteq D(T_v^*),\qquad T_v^*z=R_zSv.
\tag{MF-G1}
\]

We use this adjoint identity on its stated testing algebra; we do not assert that \(D\) is an adjoint core. Let \(T_v=uh=ku\) be its two polar decompositions. The positive operators \(h=(T_v^*T_v)^{1/2}\), \(k=(T_vT_v^*)^{1/2}\) and \(u\) have the full polar domains and spectral transport proved in HA-R4. For real \(f\in C_c(0,\infty)\), extended by zero at zero, HA-R5 gives actual algebra membership and

\[
\begin{gathered}
f(k)v,\ f(h)Sv\in A,\qquad S(f(k)v)=f(h)Sv,\\
\lambda_{f(k)v}=kf(k)u,\qquad
\lambda_{f(h)Sv}=hf(h)u^*.
\end{gathered}
\tag{MF-G2}
\]

All displayed multipliers are bounded extensions. Apply the involution formula also to the real compactly supported function \(a\mapsto a^2f(a)^2\). Since \(\Delta v=FSv\), the anti-linear adjoint pairing gives the nonnegative cross term

\[
\begin{aligned}
\langle kf(k)\Delta v,kf(k)v\rangle
&=\langle\Delta v,k^2f(k)^2v\rangle\\
&=\langle h^2f(h)^2Sv,Sv\rangle
=\|hf(h)Sv\|^2.
\end{aligned}
\tag{MF-G3}
\]

Both adjoint-domain vectors are legitimate: \(Sv\in D(F)\) because \(v\in D(\Delta)\), and the cutoff vector lies in \(A\subset D(S)\). If \(B=kf(k)\), Cauchy–Schwarz yields
\(\|B\Delta v\|^2+s^2\|Bv\|^2\geq2s\|hf(h)Sv\|^2\).
The cross term in \(\|B(\Delta+s)v\|^2\) has the same nonnegative sign. Polar transport, (MF-G2) and mixed multiplication therefore give

\[
\begin{aligned}
4s\|hf(h)Sv\|^2
&\leq\|kf(k)w\|^2\\
&=\|u\lambda_{f(h)Sv}w\|^2
\leq\|R_w\|^2\|f(h)Sv\|^2.
\end{aligned}
\tag{MF-G4}
\]

For the spectral measure \(\mu\) of \(h\) at \(Sv\), put \(c=\|R_w\|/(2\sqrt s)\). The inequality says

\[
\int_0^\infty(a^2-c^2)f(a)^2\,d\mu(a)\leq0.
\tag{MF-G5}
\]

A nonnegative cutoff supported in \((c,\infty)\) and equal to one on a prescribed compact subinterval shows that subinterval has zero measure. Countably many such intervals exhaust \((c,\infty)\). Thus \(P=1_{[0,c]}(h)\) satisfies \(PSv=Sv\); the possible zero spectral mass is retained.

Since \(P\in M\), it commutes with every \(R_z\), \(z\in D\). Equation (MF-G1) gives
\(R_zSv=PR_zSv=PT_v^*z=Phu^*z\).
The last operator is bounded by \(c\). Hence \(Sv\) is left bounded, lies in \(D(S)\) by the closed-involution property, and belongs to \(A\) by fullness. Applying \(S\) once more gives \(v\in A\), with the same multiplier norm. We have proved

\[
(\Delta+s)^{-1}D\subseteq A,\qquad
\|\lambda_{(\Delta+s)^{-1}w}\|\leq\frac{\|R_w\|}{2\sqrt s}.
\tag{MF-G6}
\]

The same argument for \(D^{\mathrm{op}}\) proves the reciprocal estimate, exchanging \(\Delta,A,D,\lambda,R\) with \(\Delta^{-1},D,A,R,\lambda\). No step commutes \(\Delta\) with the unrelated polar operator \(h\) or \(k\).

<a id="oa-flow.mf06.4"></a>

This regularization also supplies the precise common testing domain required for bounded forms. Set
\(V=D(\Delta^{1/2})\cap D(\Delta^{-1/2})\), with squared norm
\(\|z\|^2+\|\Delta^{1/2}z\|^2+\|\Delta^{-1/2}z\|^2\).
The spectral operator \(Q=\Delta^{1/2}+\Delta^{-1/2}\) has exactly domain \(V\). Its inverse and the two half-power compositions have bounded scalar functions

\[
Q^{-1}:\frac{\sqrt a}{a+1},\qquad
\Delta^{1/2}Q^{-1}:\frac a{a+1},\qquad
\Delta^{-1/2}Q^{-1}:\frac1{a+1}.
\tag{MF-C1}
\]

Because \(F(D)=D\), the set \(\Delta^{-1/2}D=JD\) is dense in \(H\). For \(z\in V\), choose \(w_n\in D\) with \(\Delta^{-1/2}w_n\to Qz\), and set \(z_n=(\Delta+1)^{-1}w_n\). Equation (MF-G6) puts \(z_n\) in \(A\). The spectral functions on \(w_n\in D(\Delta^{-1/2})\) also put it in \(D(F)\) and give \(Qz_n=\Delta^{-1/2}w_n\). Applying each of the three bounded maps in (MF-C1) gives

\[
z_n\to z,\qquad\Delta^{1/2}z_n\to\Delta^{1/2}z,\qquad
\Delta^{-1/2}z_n\to\Delta^{-1/2}z.
\tag{MF-C2}
\]

Thus \(A\cap D(F)\) is a core for the simultaneous graph norm on \(V\). This is one common-core proof, rather than an inference from separate cores. The sequence approximates one vector in a metric norm, and places no countability assumption on \(H\).

<a id="oa-flow.mf06.5"></a>

## 4. Mixed products furnish the averaging certificate

Keep \(w\in D\), \(s>0\), \(v=(\Delta+s)^{-1}w\), and put
\(X=R_w\), \(Y=J\lambda_v^*J\). Both are bounded. We will prove

\[
\langle Xz_1,z_2\rangle
=\langle Y\Delta^{-1/2}z_1,\Delta^{1/2}z_2\rangle
 +s\langle Y\Delta^{1/2}z_1,\Delta^{-1/2}z_2\rangle
\quad(z_1,z_2\in V).
\tag{MF-F1}
\]

For the initial calculation take \(z_1,z_2\in A\cap D(F)\), and put
\(a=(Sz_1)z_2\in A\). Its involution is \(Sa=(Sz_2)z_1\). Mixed multiplication and the bounded adjoint of \(\lambda_{z_1}\) give

\[
\langle Xz_1,z_2\rangle
=\langle w,a\rangle
=\langle\Delta v,a\rangle+s\langle v,a\rangle.
\tag{MF-F2}
\]

The two half-power pairings recover these terms. Antiunitarity, (MF2), (MF1), and the anti-linear adjoint criterion give

\[
\begin{aligned}
\langle Y\Delta^{1/2}z_1,\Delta^{-1/2}z_2\rangle
&=\langle Fz_2,\lambda_v^*Sz_1\rangle\\
&=\langle S((Sv)(Sz_1)),z_2\rangle\\
&=\langle z_1v,z_2\rangle=\langle v,a\rangle.
\end{aligned}
\tag{MF-F3}
\]

Here \((Sv)(Sz_1)\in A\) before applying \(S\). For the other pairing,

\[
\begin{aligned}
\langle Y\Delta^{-1/2}z_1,\Delta^{1/2}z_2\rangle
&=\langle Sz_2,\lambda_v^*Fz_1\rangle\\
&=\langle v(Sz_2),Fz_1\rangle\\
&=\langle z_1,S(v(Sz_2))\rangle\\
&=\langle(Sz_2)z_1,Sv\rangle\\
&=\langle Sa,Sv\rangle=\langle\Delta v,a\rangle.
\end{aligned}
\tag{MF-F4}
\]

The product \(v(Sz_2)\) likewise lies in \(A\). All pairings therefore use the actual domains. The three forms in (MF-F1) are separately continuous in the simultaneous graph norm on \(V\). Equation (MF-C2) extends the identity from the testing algebra to every pair in \(V\).

Let \(E_n=1_{[1/n,n]}(\Delta)\) and \(D_n=\Delta|_{E_nH}\). Every vector in \(E_nH\) belongs to \(V\), so (MF-F1) compresses to
\[
E_nXE_n=D_n^{1/2}(E_nYE_n)D_n^{-1/2}
       +sD_n^{-1/2}(E_nYE_n)D_n^{1/2}.
\]
The uniqueness rule (MF-A7) identifies its solution with the compressed operator average. Since \(E_n\) commutes with every \(U_t\), bounded multiplication through the strong integral gives
\(E_nYE_n=E_n\mathcal A_s(X)E_n\).
Both \(Y\) and \(\mathcal A_s(X)\) are bounded; \(E_n\to I\) strongly. Therefore

\[
J\lambda_{(\Delta+s)^{-1}w}^*J=\mathcal A_s(R_w).
\tag{MF-F5}
\]

This is the averaging certificate. It was obtained through a bounded equation on each spectral compression, without interpreting \(\Delta^{1/2}Y\Delta^{-1/2}\) as an operator on all of \(H\).

<a id="oa-flow.mf06.7"></a>

## 5. Separate the averages and identify the algebra actions

Apply the certificate to \(Jz\), where \(z\in D\). With \(v_s=(\Delta+s)^{-1}w\), mixed multiplication gives

\[
\begin{aligned}
\mathcal A_s(R_w)Jz
&=J\lambda_{v_s}^*z
=JR_zSv_s\\
&=(JR_zJ)\Delta^{1/2}(\Delta+s)^{-1}w
=(JR_zJ)K_sw.
\end{aligned}
\tag{MF-R1}
\]

Thus the averages of the two continuous bounded vector functions
\(t\mapsto U_tR_wU_{-t}Jz\) and
\(t\mapsto(JR_zJ)U_tw\) agree for every \(s>0\). The operator \(JR_zJ\) is complex-linear, so it commutes with vector integration without conjugating \(k_s\).

For completeness, pair the difference with \(q\in H\) and put \(s=e^r\). Cancelling \(e^{-r/2}\) says that the Fourier transform of the continuous integrable function
\[
t\longmapsto
\frac{\langle U_tR_wU_{-t}Jz-(JR_zJ)U_tw,q\rangle}
     {2\cosh(\pi t)}
\]
vanishes at every real \(r\). MF-SB SB-3 makes this function zero at every \(t\); Hilbert pairings separate vectors. Applying \(J\) to the resulting pointwise equality yields

\[
R_zJU_tw=JU_tR_wU_{-t}Jz\quad(z\in D),\qquad
\lambda_{JU_tw}=JU_tR_wU_{-t}J.
\tag{MF-R2}
\]

The bounded right side proves left boundedness through the complete defining test. The vector also lies in \(D(S)\): \(w\in D(F)\), \(U_t\) preserves that domain, and \(J\) carries \(D(F)\) onto \(D(S)\). Fullness therefore gives \(JU_tw\in A\).

At \(t=0\) this proves \(JD\subseteq A\). Run Sections 2–5 for \(D^{\mathrm{op}}\), whose modular operator is \(\Delta^{-1}\), and obtain \(JA\subseteq D\). Both calculations have the same full testing domains and no weight premise. Since \(J^2=I\),

\[
JD=A,\qquad JA=D,\qquad
\lambda_{Jw}=JR_wJ\quad(w\in D),\qquad
R_{Jv}=J\lambda_vJ\quad(v\in A).
\tag{MF-R3}
\]

The first identity and \(JU_t=U_tJ\) now turn (MF-R2) into
\[
U_tA\subseteq A,\qquad
\lambda_{U_tv}=U_t\lambda_vU_{-t}\quad(v\in A).
\]
Apply the same inclusion at \(-t\) to obtain \(U_tA=A\). The opposite calculation gives \(U_tD=D\) and its multiplier covariance. Taking the generated algebras gives

\[
JMJ=M',\qquad U_tMU_{-t}=M,\qquad U_tM'U_{-t}=M'.
\tag{MF-R4}
\]

For the conjugation equality, conjugation by the antiunitary takes a commutant to the commutant of the conjugated set: the operator equation expressing commutation is transported in both directions by \(J^2=I\). Applying this twice to (MF-R3) and using (MF0) proves the asserted equality. This does not assume the modular commutant theorem in advance.

<a id="oa-flow.mf06.8"></a>

## 6. Assemble the full domains, products and continuity

Apply the positive-multiplier reduction of Section 1 to the unitary \(U_t\), using the algebra covariance just proved and its inverse at \(-t\). Apply it also to \(J\), using (MF-R3)–(MF-R4). We obtain, on the entire bounded-vector spaces,

\[
\begin{gathered}
U_tB_l=B_l,\qquad U_tB_r=B_r,\qquad JB_l=B_r,\qquad JB_r=B_l,\\
\lambda_{U_tv}=U_t\lambda_vU_{-t},\qquad
R_{U_tw}=U_tR_wU_{-t},\\
R_{Jv}=J\lambda_vJ,\qquad \lambda_{Jw}=JR_wJ.
\end{gathered}
\tag{MF-S1}
\]

The polar reduction used positive bounded multipliers and the adjoint-intersection criterion. It imposed neither \(v\in D(S)\) nor \(w\in D(F)\). Restricting these complete identities to the intersections in (MF0), and using the full-domain commutations (MF3), proves all of (MF-T).

For \(v,q\in A\), covariance gives
\(U_t(vq)=\lambda_{U_tv}U_tq=(U_tv)(U_tq)\).
On \(D\), the same calculation with its right-product convention gives
\(U_t(wz)=R_{U_tz}U_tw=(U_tw)(U_tz)\).
Equation (MF3) preserves the two involutions. Finally, for \(v,q\in A\),

\[
J(vq)=R_{Jv}Jq=(Jq)(Jv),\qquad FJv=JSv.
\tag{MF-S2}
\]

The product identity follows from (MF-S1); the involution identity follows from (MF2) with its transported domains. Thus \(J\) has exactly the stated conjugate-linearity, reversed product order and involution behavior.

Spectral dominated convergence makes \(U_t\) strongly continuous. For fixed \(x\in B(H)\), \(q\in H\), and \(t\to t_0\),
\[
\|(U_txU_{-t}-U_{t_0}xU_{-t_0})q\|
\leq\|x\|\|(U_{-t}-U_{-t_0})q\|
 +\|(U_t-U_{t_0})xU_{-t_0}q\|\longrightarrow0.
\]
The identical estimate for \(x^*\) proves pointwise strong* continuity. Its uniformly bounded orbit also has pointwise \(\sigma\)-strong* continuity on a concrete von Neumann algebra: every square-summable family of test vectors has a uniformly small tail, bounded by \(4\|x\|^2\) times the tail sum of squared norms; the finite initial sum tends to zero. These estimates apply to arbitrary parameter nets and arbitrary Hilbert spaces. Each automorphism \(x\mapsto U_txU_{-t}\) is normal: pulling back an ultraweak vector series through unitary conjugation replaces its vectors by their \(U_{-t}\)-images and preserves their summability.

<a id="oa-flow.mf06.9"></a>

## 7. The application to every faithful normal semifinite weight

Let \(\varphi\) be a faithful normal semifinite weight on an arbitrary von Neumann algebra \(N\), and put
\(\mathfrak n_\varphi=\{x\in N:\varphi(x^*x)<\infty\}\).
NF-5 and WR-3–5 give its faithful normal GNS representation \(\pi_\varphi\), the full algebra
\(\Lambda_\varphi(\mathfrak n_\varphi\cap\mathfrak n_\varphi^*)\), and the exact correspondence
\[
B_l=\Lambda_\varphi(\mathfrak n_\varphi),\qquad
\lambda_{\Lambda_\varphi(x)}=\pi_\varphi(x)
\quad(x\in\mathfrak n_\varphi).
\]
ST-2 proves that \(\pi_\varphi(N)\) is a von Neumann algebra and that the inverse representation is normal. Let \(J,\Delta,U_t\) be the polar data of this full algebra and define

\[
\sigma_t^\varphi(x)
=\pi_\varphi^{-1}(U_t\pi_\varphi(x)U_{-t}).
\tag{MF-W1}
\]

The algebra normalization in (MF-T) makes the definition valid. Unitary conjugation and the faithful normal representation with its normal inverse make each \(\sigma_t^\varphi\) a normal \(*\)-automorphism. The group law of \(U_t\) gives the group law. Section 6 proves pointwise \(\sigma\)-strong* continuity in the represented algebra, and ST-2 transports the complete intrinsic topology back to \(N\). There is no countability, state or cyclic-vector reduction.

The whole bounded-vector correspondence and (MF-S1) give

\[
\sigma_t^\varphi(\mathfrak n_\varphi)=\mathfrak n_\varphi,\qquad
\Lambda_\varphi(\sigma_t^\varphi(x))=U_t\Lambda_\varphi(x)
\quad(x\in\mathfrak n_\varphi).
\tag{MF-W2}
\]

To justify the vector equality explicitly, (MF-S1) identifies the multiplier of the right-hand vector with \(U_t\pi_\varphi(x)U_{-t}\). The complete correspondence gives a unique finite-ideal element with that multiplier; faithfulness identifies it with \(\sigma_t^\varphi(x)\). The inverse time gives both directions of the ideal equality.

For \(a\in N_+\) with \(\varphi(a)<\infty\), its square root lies in \(\mathfrak n_\varphi\). A \(*\)-automorphism preserves the positive square root, so (MF-W2) and unitarity give

\[
\varphi(\sigma_t^\varphi(a))
=\|\Lambda_\varphi(\sigma_t^\varphi(a^{1/2}))\|^2
=\|\Lambda_\varphi(a^{1/2})\|^2
=\varphi(a).
\tag{MF-W3}
\]

Applying the same calculation at \(-t\) shows that finiteness is equivalent in both directions. Therefore \(\varphi(a)=\infty\) implies \(\varphi(\sigma_t^\varphi(a))=\infty\) as well. The identity \(\varphi\circ\sigma_t^\varphi=\varphi\) holds on the whole positive cone. This last passage has the classical square-root and inverse-time antecedent in [Combes, Theorem 2.11, printed p.55](https://www.numdam.org/item/CM_1971__23_1_49_0.pdf#page=8).

<a id="oa-flow.mf06.10"></a>

## Scope

Sections 1–6 concern arbitrary full left Hilbert algebras and their entire bounded-vector spaces. Section 7 uses the separate, earlier given-weight GNS and full-algebra correspondence. The KMS characterization, its uniqueness, and the later opposite-weight construction are further theorems; none is a premise of this proof.
