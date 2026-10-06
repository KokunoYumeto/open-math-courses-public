# Original proof of the modular fundamental theorem at arbitrary Hilbert-algebra scope

Reconstruction, 2026-10-04. This is a complete deduction from the precise earlier programme contracts listed below. No external citation is an input to the argument. Freely readable sources are audited separately in the free-source record in [core-source-lineage.json](../core-source-lineage.json); their existence does not replace any proof below.

The statement covers the full completion of every left Hilbert algebra on an arbitrary Hilbert space, both von Neumann algebras, every bounded multiplication vector, and faithful normal semifinite weights. It has no state, cyclic-vector, separability or sigma-finiteness hypothesis.

<a id="oa-flow.mf06.1"></a>

## Exact earlier programme inputs and remaining P514 closure

Use inner products linear in the first variable. The following inputs are earlier programme theorem contracts, rather than external books or article imports.

| Input | Exact proof locator | Use here |
| --- | --- | --- |
| Closed involution and anti-linear adjoint convention | [CI-1–3](OA-FLOW-CI.md#oa-flow.ci.1) | Closed involutions S and F=S*, polar data including exact domains |
| Bounded multiplication ideals and adjoints | [HA-R1–2](OA-FLOW-HA-R.md#oa-flow.ha-r.1) | Right bounded vectors, right operators, adjoints and ideal covariance |
| Closed affiliated multipliers | [HA-R3](OA-FLOW-HA-R.md#oa-flow.ha-r.3) | The closed left multiplier T_v and its adjoint pairing on the right algebra |
| Polar transport and bounded cutoffs | [HA-R4–5](OA-FLOW-HA-R.md#oa-flow.ha-r.4) | Bounded cutoff vectors for T_v and their involutions |
| Right algebra, full involution graph, commutant | [HA-R5–6](OA-FLOW-HA-R.md#oa-flow.ha-r.5) | Density, the right closed involution F, and generation of M' |
| Adjoint intersection | [HA-R7](OA-FLOW-HA-R.md#oa-flow.ha-r.7) | Full multiplication algebras and exact adjoint domains |
| Full completion and mixed products | [WH-04 Sections 2–4](OA-FLOW-WH04.md#oa-flow.wh04.2) | Full left A, full right D, mixed identity, and preservation of S and M on completion |
| Spectral operations | [SB-1–SB-6](OA-FLOW-SF.md#OA-FLOW.SF.SB1) | Borel functions, powers with integral domains, spectral cutoffs, spectral transport and dominated convergence |
| Scalar and vector integration bridge | [MF scalar bridge](OA-FLOW-MF-SB.md), SB-1–SB-4; actual earlier CF-1, SC-02–05/08–09, FF scalar interchange/Gaussian and SF-4 bodies bound in core-foundation-inputs.json | Vectorwise strong integrals, dominated convergence, the one-pole calculation (21), and continuous L1 Fourier uniqueness |
| Weight application only | [NF-5](OA-FLOW-NF.md#oa-flow.nf.5), [ST-2](OA-FLOW-ST12.md#oa-flow.st.2) and [WR-3](OA-FLOW-WR.md#wr-3)–[WR-5](OA-FLOW-WR.md#wr-5); used only by Section 7 | Faithful normal GNS image, full weight algebra, and identification of bounded vectors with the finite ideal |

The general Hilbert-algebra deduction in Sections 1–6 uses the earlier CI, BD, HA-R and WH-04 Sections 2–4 bodies, together with the earlier SF full spectral calculus and the exact narrow MF scalar bridge. Its cutoff input includes actual product-algebra membership and graph convergence, as proved in HA-R5. The faithful n.s.f. weight application in Section 7 uses the actual earlier GW/NF/ST and WR-3–5 proofs and is not a premise of Sections 1–6. The new scalar bridge uses only the actual earlier CF/SC/FF/SF proof bodies, including a direct rectangular excision argument. Exact current and historical bindings are in core-foundation-inputs.json.

<a id="oa-flow.mf06.2"></a>

## Data and theorem

Let C be a left Hilbert algebra, let H be its Hilbert completion, and replace C by its full left completion A. The full right algebra is D. Earlier completion results give

$$
 M=\lambda(A)'',\qquad M'=R(D)'',\qquad
 A=B_l\cap D(S),\qquad D=B_r\cap D(F),\qquad F=S^*.
\tag{1}
$$

They also give injective assignments of bounded multipliers and

$$
 \lambda_v w=R_wv\quad(v\in B_l,\ w\in B_r),\qquad
 \lambda_{Sv}=\lambda_v^*\ (v\in A),\qquad
 R_{Fw}=R_w^*\ (w\in D).
\tag{2}
$$

The products are vq=λ_vq in A and wz=R_z w in D. The closed-involution polar result gives

$$
 S=J\Delta^{1/2},\quad F=J\Delta^{-1/2},\quad
 \Delta=FS,\quad J^2=1,\quad J\Delta J=\Delta^{-1},
\tag{3}
$$

with Δ positive, injective and self-adjoint. In particular, D(S)=D(Δ^{1/2}) and D(F)=D(Δ^{-1/2}). Define U_t=Δ^{it}. Spectral transport, including anti-linearity of J, gives

$$
 JU_t=U_tJ,\quad SU_t=U_tS,\quad FU_t=U_tF,
\tag{4}
$$

on the respective domains. The opposite right algebra D^op has polar data J, Δ^{-1} and full partner A.

We will prove

$$
 JA=D,\quad JD=A,\quad JMJ=M',
\tag{5}
$$

$$
 U_tA=A,\quad U_tD=D,\quad
 \lambda_{U_tv}=U_t\lambda_vU_{-t},\quad
 R_{U_tw}=U_tR_wU_{-t},
\tag{6}
$$

and consequently U_tMU_{-t}=M and U_tM'U_{-t}=M'. The multiplication identities in (6) also hold for every v∈B_l and w∈B_r, without an involution-domain hypothesis.

<a id="oa-flow.mf06.3"></a>

## 1. A positive resolvent supplies bounded left multiplication

For v∈D(S), close the map w↦R_wv on D and call the resulting operator T_v. Its affiliation and adjoint test-domain contract are

$$
 T_v\text{ is affiliated with }M,\qquad
 D\subseteq D(T_v^*),\qquad T_v^*w=R_wSv.
\tag{7}
$$

No adjoint-core assertion is used. Write T_v=uh=ku, where h=(T_v* T_v)^{1/2}, k=(T_v T_v*)^{1/2}. The polar partial isometry and spectral projections belong to M. For real f∈C_c(0,∞), extended by zero at 0, the earlier cutoff theorem gives

$$
 f(k)v\in A,\quad \lambda_{f(k)v}=kf(k)u,\qquad
 f(h)Sv\in A,\quad \lambda_{f(h)Sv}=hf(h)u^*,
\tag{8}
$$

$$
 S(f(k)v)=f(h)Sv.
\tag{9}
$$

All operators on the right in (8) are bounded extensions.

Fix s>0 and w∈D, and put v=(Δ+s)^{-1}w. Then v∈D(Δ), so (7)-(9) apply. Set B=kf(k), a bounded self-adjoint operator. Applying (9) to the real function a↦a²f(a)² and using the anti-linear adjoint pairing yields

$$
 E:=\langle B\Delta v,Bv\rangle
 =\langle\Delta v,k^2f(k)^2v\rangle
 =\langle h^2f(h)^2Sv,Sv\rangle
 =\|hf(h)Sv\|^2\geq0.
\tag{10}
$$

Cauchy-Schwarz therefore gives

$$
 \|B\Delta v\|^2+s^2\|Bv\|^2\geq2sE.
$$

Expanding the norm of B(Δ+s)v, the cross term is 2sE, so

$$
 4s\|hf(h)Sv\|^2\leq\|B(\Delta+s)v\|^2=\|kf(k)w\|^2.
\tag{11}
$$

Polar transport and (8) identify kf(k)=uλ_{f(h)Sv}. Hence (2) implies

$$
 \|kf(k)w\|\leq\|R_w\|\,\|f(h)Sv\|.
\tag{12}
$$

Put c=||R_w||/(2√s). Equations (11)-(12) say that the spectral measure μ of h at Sv satisfies

$$
 \int_0^\infty (a^2-c^2)f(a)^2\,d\mu(a)\leq0.
\tag{13}
$$

Choose f supported in (c,∞), nonnegative and equal to one on any prescribed compact subinterval of (c,∞). Equation (13) makes the measure of that subinterval zero. Countably many compact intervals exhaust (c,∞). Thus $P=1_{[0,c]}(h)$ satisfies P Sv=Sv. Spectral mass at zero is included.

For z∈D, affiliation gives PR_z=R_zP. By (7),

$$
 R_zSv=P R_zSv=P T_v^*z=Phu^*z.
$$

The last operator is bounded with norm at most c. Thus Sv∈B_l. Since S is an involution, Sv∈D(S), so fullness gives Sv∈A and then v=S(Sv)∈A. Its multiplier has the same norm as the multiplier of Sv. We have proved

$$
 (\Delta+s)^{-1}D\subseteq A,\qquad
 \|\lambda_{(\Delta+s)^{-1}w}\|\leq\frac{\|R_w\|}{2\sqrt s}.
\tag{14}
$$

Applying this proved argument to D^op gives the symmetric estimate with Δ^{-1}, A, D and R interchanged. No step commuted Δ with h or k.

<a id="oa-flow.mf06.4"></a>

## 2. The two half powers have a proved common test core

Let V=D(Δ^{1/2})∩D(Δ^{-1/2}). Give it the sum of the three squared norms of z, Δ^{1/2}z and Δ^{-1/2}z. The spectral operator

$$
 Q=\Delta^{1/2}+\Delta^{-1/2}
$$

has exactly this domain. Its scalar function is at least 2. The operators Q^{-1}, Δ^{1/2}Q^{-1} and Δ^{-1/2}Q^{-1} are bounded; their scalar functions are respectively

$$
 \frac{\sqrt a}{a+1},\qquad\frac{a}{a+1},\qquad\frac1{a+1}.
\tag{15}
$$

Because F(D)=D and Δ^{-1/2}=JF, the set Δ^{-1/2}D=JD is dense in H. For z∈V choose w_n∈D with Δ^{-1/2}w_n→Qz, and set z_n=(Δ+1)^{-1}w_n. Equation (14) gives z_n∈A. Spectral multiplication on w_n∈D(Δ^{-1/2}) gives z_n∈D(Δ^{-1/2}) and

$$
 Qz_n=\Delta^{-1/2}w_n.
$$

Applying the three bounded maps in (15) proves convergence of z_n, Δ^{1/2}z_n and Δ^{-1/2}z_n. Therefore

$$
 A\cap D(F)\text{ is a core for the simultaneous two-half-power graph norm on }V.
\tag{16}
$$

The sequence is chosen for an individual vector in a metric Hilbert norm. This does not require H to be separable. The proof does not infer a common core from two separate core statements.

<a id="oa-flow.mf06.5"></a>

## 3. The resolvent yields an equation of bounded sesquilinear forms

Keep s>0, w∈D and v=(Δ+s)^{-1}w. Set

$$
 X=R_w,\qquad Y=J\lambda_v^*J.
$$

Both are bounded. We claim, for z_1,z_2∈V,

$$
 \langle Xz_1,z_2\rangle
 =\langle Y\Delta^{-1/2}z_1,\Delta^{1/2}z_2\rangle
 +s\langle Y\Delta^{1/2}z_1,\Delta^{-1/2}z_2\rangle.
\tag{17}
$$

First take z_1,z_2∈A∩D(F), and set a=(Sz_1)z_2∈A. Its involution is Sa=(Sz_2)z_1. Mixed multiplication and the adjoint of λ_{z_1} give

$$
 \langle Xz_1,z_2\rangle
 =\langle w,a\rangle
 =\langle\Delta v,a\rangle+s\langle v,a\rangle.
\tag{18}
$$

Antiunitarity and (3) identify the second form on the right of (17) as

$$
 \begin{aligned}
 \langle Y\Delta^{1/2}z_1,\Delta^{-1/2}z_2\rangle
 &=\langle Fz_2,\lambda_v^*Sz_1\rangle\\
 &=\langle S((Sv)(Sz_1)),z_2\rangle\\
 &=\langle z_1v,z_2\rangle=\langle v,a\rangle.
 \end{aligned}
\tag{19}
$$

The use of S is valid because (Sv)(Sz_1)∈A. For the other form,

$$
 \begin{aligned}
 \langle Y\Delta^{-1/2}z_1,\Delta^{1/2}z_2\rangle
 &=\langle Sz_2,\lambda_v^*Fz_1\rangle\\
 &=\langle v(Sz_2),Fz_1\rangle\\
 &=\langle z_1,S(v(Sz_2))\rangle\\
 &=\langle(Sz_2)z_1,Sv\rangle\\
 &=\langle Sa,Sv\rangle=\langle\Delta v,a\rangle.
 \end{aligned}
\tag{20}
$$

Here v(Sz_2)∈A, so every adjoint-domain pairing is legitimate. Equations (18)-(20) prove (17) on the test algebra. All three forms are continuous for the V norm in each variable. The common-core result (16) extends (17) to V.

<a id="oa-flow.mf06.6"></a>

## 4. Solve the bounded equation by finite spectral partitions

Put k_s(t)=s^{-1/2}s^{-it}/(2cosh(πt)). SB-2 of [MF scalar bridge](OA-FLOW-MF-SB.md), using the earlier SF-4 rectangle proof and its local direct rectangular excision, proves the scalar identity

$$
 \int_{\mathbb R}\frac{e^{ixt}}{2\cosh(\pi t)}\,dt
 =\frac1{2\cosh(x/2)}\qquad(x\in\mathbb R).
\tag{21}
$$

The bridge subtracts the single principal part at i/2 and verifies the remainder is continuous at that point, so the proved convex primitive theorem applies directly. It supplies the rectangle index, vertical-edge bounds and limit, rather than importing a general residue theorem. In particular,

$$
 \int k_s(t)e^{it\log(a/b)}\,dt=\frac{\sqrt{ab}}{a+sb}\quad(a,b>0),
\tag{22}
$$

and ∫|k_s(t)|dt=1/(2√s).

For a bounded positive invertible operator D and a bounded operator Z on its Hilbert space, define

$$
 \Psi_D(Z)=D^{1/2}ZD^{-1/2}+sD^{-1/2}ZD^{1/2},
\qquad
 \Phi_D(Z)=\int k_s(t)D^{it}ZD^{-it}\,dt.
$$

The latter is an operator-norm integral, since log D is bounded, constructed by SB-1 of the bridge. If D=Σ_j a_jp_j has finitely many spectral values, its (j,l) block satisfies

$$
 p_j\Psi_D(Z)p_l=\frac{a_j+sa_l}{\sqrt{a_ja_l}}p_jZp_l,
\qquad
 p_j\Phi_D(Z)p_l=\frac{\sqrt{a_ja_l}}{a_j+sa_l}p_jZp_l.
$$

Thus Φ_D Ψ_D(Z)=Z. Approximate an arbitrary bounded positive invertible D in operator norm by finite positive spectral step functions whose values remain between the same positive lower and upper bounds. Their half powers, inverse half powers and logarithms converge in norm. For each fixed t, their unitary powers converge in norm. The common integrable bound |k_s(t)| and dominated convergence give norm convergence of Φ_D(Z). Passing to the limit proves

$$
 \Phi_D\Psi_D(Z)=Z
\tag{23}
$$

for every such D.

Now let $E_n=1_{[1/n,n]}(\Delta)$, and let D_n be Δ restricted to E_nH. Compress (17) to E_nH. Every vector there belongs to V, and the compressed equation is

$$
 E_nXE_n=\Psi_{D_n}(E_nYE_n).
$$

Equation (23) gives

$$
 E_nYE_n=E_n\left[\int k_s(t)U_tXU_{-t}\,dt\right]E_n.
$$

SB-1 defines the bracket strongly on each Hilbert vector, with norm at most ||X||/(2√s). Since E_n→I strongly, we obtain the bounded-operator identity

$$
 J\lambda_{(\Delta+s)^{-1}w}^*J
 =\int_{\mathbb R}k_s(t)U_tR_wU_{-t}\,dt.
\tag{24}
$$

No unbounded product such as Δ^{1/2}YΔ^{-1/2} was asserted to exist on all H. The spectral compressions justified every such product where it was used.

For finite positive spectral step functions, (22) with b=1 gives the next identity block by block. Positive spectral cutoffs and step approximations extend it to Δ: on each fixed spectral interval the functions converge uniformly, SB-1 gives convergence of the vector integrals, and both sides have norm at most 1/(2√s), permitting removal of the cutoff. Thus

$$
 \Delta^{1/2}(\Delta+s)^{-1}
 =\int_{\mathbb R}k_s(t)U_t\,dt.
\tag{25}
$$

Boundedness and strong convergence follow from the same integrable majorant.

<a id="oa-flow.mf06.7"></a>

## 5. Recover the actual bounded vectors before taking generated algebras

Fix w,z∈D, set v_s=(Δ+s)^{-1}w, and apply (24) to Jz. Mixed multiplication and S=JΔ^{1/2} give

$$
 \begin{aligned}
 \left[\int k_s(t)U_tR_wU_{-t}\,dt\right]Jz
 &=J\lambda_{v_s}^*z\\
 &=JR_zSv_s\\
 &=(JR_zJ)\Delta^{1/2}(\Delta+s)^{-1}w\\
 &=\int k_s(t)(JR_zJ)U_tw\,dt.
 \end{aligned}
\tag{26}
$$

The operator JR_zJ is complex-linear. This arrangement is essential: the kernel is never passed through a lone anti-linear J.

Write s=e^r and cancel the nonzero factor e^{-r/2}. Equation (26), after pairing with any q∈H, states that the Fourier transform of

$$
 t\longmapsto\frac{\langle U_tR_wU_{-t}Jz-(JR_zJ)U_tw,q\rangle}{2\cosh(\pi t)}
$$

vanishes at every real r. The function is continuous and integrable. SB-3–SB-4 of the bridge make it zero at every t. Hilbert pairings separate vectors. Applying J to the resulting equality gives

$$
 R_zJU_tw=JU_tR_wU_{-t}Jz\qquad(z\in D).
\tag{27}
$$

Therefore JU_tw is left bounded, with

$$
 \lambda_{JU_tw}=JU_tR_wU_{-t}J.
\tag{28}
$$

It also belongs to D(S): w∈D(F), U_t preserves D(F), and J maps D(F) onto D(S). Hence fullness puts JU_tw∈A.

At t=0, (28) gives JD⊆A. Apply the proved assertion to D^op, whose modular operator is Δ^{-1}, to get JA⊆D. Since J²=I these inclusions are equalities. In particular,

$$
 \lambda_{Jw}=JR_wJ\quad(w\in D),\qquad
 R_{Jv}=J\lambda_vJ\quad(v\in A).
\tag{29}
$$

Using λ(A)''=M and R(D)''=M', equation (29) proves JMJ=M'. These conclusions use the earlier identification of the generated right algebra with M' in (1), together with vector boundedness and exact involution domains. The modular-conjugation identity JMJ=M' was not assumed.

<a id="oa-flow.mf06.8"></a>

## 6. Finish MF-06, including the entire bounded-vector spaces

For v∈A write v=Jw with w∈D. Equations (4) and (28) show

$$
 U_tv=JU_tw\in A,\qquad
 \lambda_{U_tv}=JU_tR_wU_{-t}J=U_t\lambda_vU_{-t}.
$$

Applying this also at -t proves U_tA=A. Applying the same argument to D^op gives U_tD=D and the right-multiplier covariance in (6). Taking generated algebras proves normalization of M and M'. Spectral calculus gives strong continuity of U_t; bounded multiplication on both sides then gives strong* continuity of U_txU_{-t} for every x∈B(H).

For v,q∈A, multiplier covariance gives

$$
 U_t(vq)=\lambda_{U_tv}U_tq=(U_tv)(U_tq).
$$

The domain commutations in (4) show preservation of sharp and flat, so the algebra actions are complex-linear involution-preserving automorphisms. Moreover (29) gives

$$
 J(vq)=R_{Jv}Jq=(Jq)(Jv),\qquad FJv=JSv.
\tag{30}
$$

Thus J is the conjugate-linear involution-preserving anti-isomorphism between A and D with the stated right-product order.

Now take v∈B_l with no domain condition. For z∈D, the already proved covariance on D gives

$$
 R_zU_tv=U_tR_{U_{-t}z}v=U_t\lambda_vU_{-t}z.
$$

This is the defining boundedness test for U_tv∈B_l and identifies its multiplier as U_tλ_vU_{-t}. Applying -t proves U_tB_l=B_l. For w∈B_r and a∈A, the left covariance similarly gives

$$
 \lambda_aU_tw=U_t\lambda_{U_{-t}a}w=U_tR_wU_{-t}a.
$$

This proves U_tw∈B_r with R_{U_tw}=U_tR_wU_{-t}, and the inverse parameter proves U_tB_r=B_r.

The original C need not be U_t-invariant. The theorem concerns its canonical full completion A, with the same S, Δ, J and generated M.

<a id="oa-flow.mf06.9"></a>

## 7. Faithful normal semifinite weights, without countability assumptions

Let φ be a faithful normal semifinite weight on an arbitrary von Neumann algebra N. The earlier [NF-5](OA-FLOW-NF.md#oa-flow.nf.5) and [WR-3](OA-FLOW-WR.md#wr-3)–[WR-5](OA-FLOW-WR.md#wr-5) supply the faithful normal GNS representation π_φ and identify the full left algebra and all bounded vectors, with

$$
 \lambda_{\Lambda_\varphi(x)}=\pi_\varphi(x)\quad(x\in\mathfrak n_\varphi).
$$

The represented image is a von Neumann algebra with normal inverse by the earlier [ST-2 image and topology theorem](OA-FLOW-ST12.md#oa-flow.st.2). Define

$$
 \sigma_t^\varphi(x)=\pi_\varphi^{-1}(U_t\pi_\varphi(x)U_{-t}).
\tag{31}
$$

Normalization makes this well defined. Unitary conjugation and the faithful normal inverse representation show that each map is a normal \*-automorphism, and the U_t group law gives its group law. Strong* continuity, together with the uniform norm bound ||σ_t(x)||=||x||, implies sigma-strong* continuity: for a square-summable family of test vectors, the tails are uniformly dominated by a constant times the sum of their squared norms. WH-02 transports these intrinsic topologies back to N.

The bounded-vector covariance and the exact earlier correspondence between B_l and n_φ give

$$
 \sigma_t^\varphi(\mathfrak n_\varphi)=\mathfrak n_\varphi,\qquad
 \Lambda_\varphi(\sigma_t^\varphi(x))=U_t\Lambda_\varphi(x).
\tag{32}
$$

For a∈N_+, apply (32) to a^{1/2} when φ(a)<∞. Preservation of square roots under \*-automorphisms and unitarity of U_t yield

$$
 \varphi(\sigma_t^\varphi(a))
 =\|\Lambda_\varphi(\sigma_t^\varphi(a^{1/2}))\|^2
 =\|\Lambda_\varphi(a^{1/2})\|^2=\varphi(a).
$$

The inverse parameter shows that finiteness is equivalent in both directions. Hence if φ(a)=∞, the transformed value is also infinite. Thus φ∘σ_t^φ=φ on the full positive cone. This proves exactly the weight consequence of MF-06; the KMS characterization and its uniqueness are additional theorems.

<a id="oa-flow.mf06.10"></a>

## Audit boundary

The general Hilbert-algebra argument now invokes actual earlier CI/BD/HA-R, WH-04 Sections 2–4 and SF spectral proofs. Its exact scalar bridge remains separately bound. The faithful n.s.f. weight application now uses the actual earlier GW/NF/ST/WR proofs; those application inputs are never premises of the general Hilbert-algebra deduction. The later [canonical opposite-weight formula](OA-FLOW-MW.md#mw-2) is a separate consequence; no nonfaithful extension is asserted.