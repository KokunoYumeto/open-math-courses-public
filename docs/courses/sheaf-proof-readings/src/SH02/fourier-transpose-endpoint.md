# SH02-FTE-UNIT. Transposing the complete Fourier trace comparison

Original programme text: CC0 1.0 Universal. 

Fourier functoriality identifies the objects at the corners of a trace square. To prove that square commutes, its two routes must use the same adjunction and the same ordered orientation maps. This lesson compares the entire transposed endpoint. Two line crossings and the defect between the paired Fourier adjunctions cancel in prescribed places, giving the linear trace equation for every bundle map in the full bounded-below category.

The kernel-adjunction framework is compared with Schapira's [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026, §4.9, formulas (4.9.4)–(4.9.7), pp. 100–101](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=100). That passage gives a proper kernel transform and its raw right adjoint. This reading uses a mixed-kernel mate calculation followed by explicit tensor-duality identities to compare the complete course endpoints. Neither the signs nor the correspondence of the named maps follows from the kernel functor formulas alone. The final source account records that distinction.

## SH02-FTE-DEPENDENCIES. The operations and comparisons in use

Use [Fourier functoriality](fourier-functoriality.md), SH02-FF-CONVENTIONS, SH02-FF-BOUNDS, SH02-FF-LINEAR-KERNEL and SH02-FF-MATES, for the primitive exchange, its raw kernel adjunction, the relative line FF3a and the R2/R3/R4 rewrites. [The linear Fourier comparison](linear-fourier-trace.md), SH02-LFT-SUPPORT, SH02-LFT-PAIRED, SH02-LFT-ANTIPODE-CHECK, SH02-LFT-LINE-ORDER and SH02-LFT-TRANSPOSE-AUDIT, supplies the direct support square, the two explicitly related adjunctions, their full-category scalar, the right-ordered coefficient trace and the exact endpoint reduction. [The graded line in a Fourier support comparison](fourier-graded-comparison.md), SH02-FGC-EXTRACTION and SH02-FGC-SUPPORT, fixes the initial coherent FF11 extraction and the separately braided final contraction.

The operation imports are SH02-LFT-IMP-BC-NU, SH02-LFT-IMP-PF-ADJUNCTION and SH02-LFT-IMP-ORIENTATION: proper-support base change and composition on locally compact Hausdorff spaces, projection formula, ordinary/exceptional adjunctions, their module/mate/pasting identities, and orientation traces with coordinate-change compatibility. The actual reversed halfspace comparison is SH02-FS-COMPARE. The proof uses the paired scalar already proved on all conic objects, including its enhanced-center and conic-descent inputs. Each of those prerequisites retains its own proof-closure and source-account obligations. The present argument does not use Verdier biduality or a negatively normalized replacement adjunction.

## SH02-FTE-CONVENTIONS. State the endpoint before transposing it

Let \(S\) be an arbitrary locally compact Hausdorff space. Let \(h:E_1\to E_2\) be a continuous fiberwise linear map of real vector bundles over its identity, with fixed finite ranks \(n_1,n_2\). Its transpose is \(r:E_2^*\to E_1^*\). The coefficient ring \(k\) is commutative and unital, of finite global dimension. Complexes belong to the full conic \(D^+\) categories with a global lower bound and the parameter-space scalar transport of SH02-FF-DOMAINS. There is no upper bound, finite-stalk, field, constructibility, orientability, constant-kernel-rank, manifold-base, or properness hypothesis. The bundle ranks supply the finite abelian-sheaf proper-support dimension bounds needed for \(h^!\) and \(r^!\). Locally constant bundle ranks may be used componentwise only when the required bounds remain global.

All tensors below are derived and all line factors are pulled from the base \(S\).
Write \(a_i\) for ordinary inverse image by negation on \(E_i\) and \(A_i\) for the same functor on \(E_i^*\). Put

\[
\begin{gathered}
T_i=T_{E_i},\quad P_i=T_{E_i^*},\quad
M_i=A_i(-)\otimes W_i,\quad
V_i=M_iT_i,\quad Q_i=a_iP_i(-)\otimes W_i,\\
A=W_1,\quad B=W_2,\quad L=\omega_h,\quad
D=R\mathcal Hom(L,k),\quad \epsilon=(-1)^{n_1-n_2}.
\tag{FTE1}
\end{gathered}
\]

The letters \(A\) and \(B\) are orientation lines, while \(S\) denotes the base and \(A_i\) denotes an antipode functor. The prescribed relative-line
isomorphism and its rigid mate are

\[
\begin{aligned}
d:L\otimes B&\longrightarrow A,\\
c:D\otimes A&\xrightarrow{1_D\otimes d^{-1}}
D\otimes L\otimes B
\xrightarrow{\operatorname{ev}_L\otimes1_B}B.
\tag{FTE2}
\end{aligned}
\]

Here d is exactly FF3a. Put \(u_C:k\to C\otimes C^\vee\) for coevaluation;
\(\operatorname{ev}_C:C^\vee\otimes C\to k\) is evaluation. They satisfy

\[
(1_L\otimes c)(u_L\otimes1_A)=d^{-1}.
\tag{FTE3}
\]

This is the tensor-duality triangle, without a symmetry. In particular
the coherent relative inverse identification is the rigid mate of d,
not an independently chosen scalar on a trivialized orientation line.

Let \(\ell_r:h^!P_2\to P_1Rr_*\otimes L\) be original FF L3 for r, with its
initial FF11 cancellation specified by FGC21–FGC22. Define

\[
\begin{aligned}
\bar\ell_r^{\,c}
 &=(1\otimes u_L^{-1})(\ell_r\otimes1_D),\\
\bar\ell_r^{\,b}
 &=(1\otimes\operatorname{ev}_L\sigma_{L,D})
   (\ell_r\otimes1_D)
 =\epsilon\bar\ell_r^{\,c}.
\tag{FTE4}
\end{aligned}
\]

Their common domain is \(h^!P_2(-)\otimes D\) and target is \(P_1Rr_*(-)\).
The superscripts c and b name the coherent and braided final
cancellations. In particular neither alters the initial extraction of
L3 from FF11. Let \(J^c\) and \(J^b\) be LFT34 with these respective middle
maps. Let \(F_h\) denote original FF R3 precomposed with \(V_1\sigma_{J,D}\),
where \(J=h^!H\). Thus

\[
F_h:V_1(J\otimes D)\longrightarrow Rr_*V_2H.
\tag{FTE5}
\]

**Theorem.** The complete endpoint equality is

\[
J_h^c=\epsilon F_h,\qquad
J_h^b=F_h.
\tag{FTE6}
\]

The support comparison FGC2–FGC4 in [The graded line in a Fourier support comparison](fourier-graded-comparison.md), applied to \(r\), gives \(\bar\ell_r^{\,b}=\overline G_r\). Thus FTE6 identifies the direct endpoint with \(F_h\). The source-line calculation FTE3 then proves LFT41 and the trace equation FTC14. We prove the endpoint equality first, keeping the original units, counits and orientation maps.

## SH02-FTE-MODULES. Transport the right line through the actual adjunction

Use \(\mathcal H=h^!\) and \(\mathcal R=Rr_*\) to keep functors separate from objects.
Let \(b_h:\mathcal HQ_2\to Q_1\mathcal R\) be \(B_h\) inverse in LFT36. Let

\[
b_i:P_iM_i\longrightarrow Q_i
\tag{FTE7}
\]

be the actual kernel input-antipode exchange and right-line projection
formula of LFT-P1. These maps must be retained: \(b_i\) is not a claim that
input and output antipodes act identically on an integration class.
Let \(\eta_i\), \(\varepsilon_i\) be the unit/counit of \(T_i\) left adjoint to \(Q_i\).
Transporting this adjunction gives \(V_i\) left adjoint to \(P_i\) with

\[
\alpha_i=b_{i,T_i}^{-1}\eta_i,
\qquad \beta_i:V_iP_i\longrightarrow1.
\tag{FTE8}
\]

For any base-pulled invertible graded line C write

\[
\begin{aligned}
e(X,C)&:\mathcal H(X\otimes C)\longrightarrow\mathcal H X\otimes C,\\
q_i(X,C)&:Q_i(X\otimes C)\longrightarrow Q_iX\otimes C,\\
\widehat q_1(X,C)&:
Q_1\mathcal R(X\otimes C)\longrightarrow Q_1\mathcal RX\otimes C.
\tag{FTE9}
\end{aligned}
\]

The last map first applies \(Q_1\) to the ordinary-image right-line
projection formula and then \(q_1\). The first is the exceptional right-line
extraction defined by adjunction. Expanding \(Q_i=a_iP_i(-)\otimes W_i\),
the map \(q_i\) is \(P_i\)'s right projection formula followed by the symmetry
that moves C past \(W_i\). This last symmetry is part of \(q_i\). In particular
\(q_i\) at \(C=W_i\) includes the self-braid of \(W_i\).

The mixed mate is compatible with these module maps:

\[
\widehat q_1(X,C)b_h(X\otimes C)
 =(b_h(X)\otimes1_C)e(Q_2X,C)\mathcal Hq_2(X,C).
\tag{FTE10}
\]

Here is a map verification. The primitive \(A_h\) is built from pullback,
proper-support composition/base change, and tensoring with the flat
degree-zero pairing cut. Tensoring its coefficient by a base line and
using each right projection formula gives the same kernel arrow, with
the line on the right. Adjunction transports this commutative module
square to FTE10. In the raw right kernel the right line moves past its
rightmost orientation factor; this is precisely the symmetry in \(q_i\)
above. The fixed comparison \(Q_i\) to its raw right kernel is itself right
linear for this \(q_i\), since every arrow of the reversed FS6 chain is
localization, support inclusion, or an image projection formula with
that same orientation factor. Thus no unsigned replacement of \(q_i\) is
being made when taking mates. The same argument, with identity primitive
arrow, proves that \(\eta_i\) is a module morphism for the right structures
of \(T_i\) and \(Q_i\). These statements require only bounded invertible C.

The exceptional antipode exchange \(\chi\) is written in the direction

\[
\chi(X):a_1\mathcal HX\longrightarrow\mathcal Ha_2X.
\tag{FTE11}
\]

Its involution identity and its compatibility with e follow by taking
the proper-support adjunct: the coordinate-change square is an
involution and the coefficient line is pulled from its fixed base.
Concretely
\(\chi(a_2X)^{-1}=a_1\chi(X)\), after suppressing \(a_i^2=1\), and the
module square uses identity ordinary transport on C. This does not
declare \(\chi(X)\) to be a scalar on arbitrary X.

Write

\[
c_r:\mathcal RA_2\longrightarrow A_1\mathcal R,
\qquad g_i:Q_iA_i\longrightarrow a_iQ_i
\tag{FTE12}
\]

for the geometric ordinary-image and kernel antipode exchanges. The antipode-mate lemma proved in SH02-FTE-ANTIPODE gives the following fully typed consequence:

\[
\begin{aligned}
&a_1b_h(A_2Z)\,a_1\mathcal H(g_2(Z)^{-1})
 \,a_1\chi(Q_2Z)\\
&\hspace{20pt}=\epsilon\,\Omega_Zb_h(Z),\\
\Omega_Z
&=(a_1Q_1c_r(Z))^{-1}(a_1g_1(\mathcal RZ))^{-1}:
Q_1\mathcal RZ\longrightarrow a_1Q_1\mathcal RA_2Z.
\tag{FTE13}
\end{aligned}
\]

The first line starts at \(\mathcal HQ_2Z\) and ends at
\(a_1Q_1\mathcal RA_2Z\). The lemma says the right mate of the simultaneous antipode
is \((-1)^{n_i}g_i\). Taking mates of the primitive mixed-kernel equivariance
and moving its invertible output arrows gives FTE13. Its scalar is the
ratio of these two actual mate signs, while \(\chi\) remains explicitly
inside the first route. This is not a scalarization of \(\chi\).

## SH02-FTE-ANTIPODE. The mate of a simultaneous antipode has its own sign

We prove the coordinate-change assertion used in FTE13. This also fixes its normalization without a calculation restricted to a single coefficient object.

For one bundle \(E\) of rank \(n\), use \(p:E\times_SE^*\to E\), \(q:E\times_SE^*\to E^*\), and the negative pairing cut \(N\). The simultaneous antipode \(z(x,\xi)=(-x,-\xi)\) preserves \(N\). Let \(a,A\) be ordinary antipode inverse images on the two bundles. The proper kernel gives \(t:Ta\to AT\). Its raw right adjoint is
\[
S_0K=Rp_*R\mathcal Hom(k_N,q^!K).
\tag{FTE-A1}
\]
Let \(\chi_q:z^{-1}q^!\to q^!A\) be the exceptional coordinate exchange. The raw right mate of \(t\) is
\[
\begin{aligned}
S_0AK
&\xrightarrow{Rp_*R\mathcal Hom(k_N,\chi_q^{-1})}
Rp_*R\mathcal Hom(k_N,z^{-1}q^!K)\\
&\simeq Rp_*z^{-1}R\mathcal Hom(k_N,q^!K)
\simeq aS_0K.
\end{aligned}
\tag{FTE-A2}
\]
Indeed the raw kernel adjunction first takes the proper-support adjunct for \(q\), then the cut tensor–Hom adjunct, then the ordinary \(p\) adjunct. Precomposition by \(t\) introduces \(\chi_q^{-1}\) in the first step; preservation of the cut gives the second arrow; \(pz=ap\) gives the third. This proves the displayed mate by its Hom bijection.

Under \(q^!K=q^{-1}K\otimes W_E\), let \(\kappa:q^!AK\to z^{-1}q^!K\) use ordinary identity on the base-pulled orientation line. The actual exceptional exchange instead satisfies
\[
\chi_q^{-1}=(-1)^n\kappa.
\tag{FTE-A3}
\]
Its proper-support adjunct must commute with the orientation trace along the \(E\) fiber. The fiber coordinate change is negation, with orientation degree \((-1)^n\). This determines the coefficient map before applying local Hom or image. The line remains on the right and the cut has degree zero. Local orientation changes conjugate both routes by the same transition map, so the equality glues on nonorientable bundles over an arbitrary locally compact base.

The specified comparison \(d_0:Q\to S_0\) is the reversed FS6 chain. In the positive-cut presentation put \(C=\{\langle x,\xi\rangle\geq0\}\) and \(K'=q^{-1}K\otimes W_E\). The chain is
\[
\begin{aligned}
Rp_!(K'_C)&\longleftarrow Rp_!R\Gamma_N(K'_C)\\
&\simeq Rp_!((R\Gamma_NK')_C)\\
&\longrightarrow Rp_*((R\Gamma_NK')_C)
\longleftarrow Rp_*R\Gamma_NK'.
\end{aligned}
\tag{FTE-A4}
\]
All invertible backward arrows use their specified inverses. Each map is local-support forgetting, a comparison of localization triangles, support inclusion, or cut restriction. These commute with the ordinary simultaneous coordinate change using identity on \(W_E\). Their inverses commute as well. Thus transporting the ordinary version of FTE-A2 through \(d_0\) gives exactly the geometric map \(g:QA\to aQ\) of FTE12. Restoring FTE-A3 proves
\[
m=(-1)^n g,
\tag{FTE-A5}
\]
where \(m\) is the actual right mate of \(t\) under \(T\dashv Q\).

For the bundle map \(h\), let \(d_h:Rh_!a_1\to a_2Rh_!\) and \(e_r:r^{-1}A_1\to A_2r^{-1}\) be geometric exchanges. The primitive mixed kernel obeys
\[
(A_2A_h)(e_rT_1)(r^{-1}t_1)
=(t_2Rh_!)(T_2d_h)(A_ha_1).
\tag{FTE-A6}
\]
Both routes integrate the same negative cut on \(E_1\times_SE_2^*\), with its simultaneous negation. The two mixed maps preserve that coordinate-change square. Pasting proper-support base change and projection formula therefore gives the same kernel arrow along both routes. This includes rank jumps and does not choose a kernel bundle.

The right mates of \(d_h\) and \(e_r\) are \(\chi^{-1}\) and \(c_r\). Taking right mates of FTE-A6 reverses their order and gives
\[
m_1(\mathcal R)Q_1(c_r)(b_hA_2)
=(a_1b_h)\chi^{-1}(Q_2)\mathcal H(m_2).
\tag{FTE-A7}
\]
Its common source is \(\mathcal HQ_2A_2\), and its common target is \(a_1Q_1\mathcal R\). Compose at the input with \(\mathcal H(m_2^{-1})\chi(Q_2)\) and cancel the adjacent inverses. Apply \(a_1\), substitute FTE-A5 at both ranks, and move the two invertible output exchanges to the opposite side. The result is precisely FTE13. The exceptional map \(\chi\) remains present on its arbitrary coefficient. Only the two independently calculated kernel-mate signs have been replaced by scalars.

## SH02-FTE-OUTPUT. A common target for two adjuncts

Fix H and put

\[
\begin{gathered}
J=\mathcal HH,\quad Z=T_2H,\quad X=\mathcal RZ,\quad
Y=\mathcal RM_2Z=\mathcal RV_2H,\\
t_H=b_h(Z)\mathcal H\eta_{2,H}:J\longrightarrow Q_1X.
\end{gathered}
\tag{FTE14}
\]

Define an output map, including the ordinary-image module comparison,
by

\[
\begin{aligned}
\Psi_Z:Q_1X\otimes B
&\xrightarrow{\Omega_Z\otimes1_B}
a_1Q_1\mathcal RA_2Z\otimes B\\
&\xrightarrow{(a_1\widehat q_1(A_2Z,B))^{-1}}
a_1Q_1\mathcal R(A_2Z\otimes B)
=P_1Y\otimes A.
\tag{FTE15}
\end{aligned}
\]

This equality uses \(a_1Q_1=P_1(-)\otimes A\) with ordinary identity
on the base-pulled A. Introduce the common composite

\[
K_H=\Psi_Z(t_H\otimes1_B)(1_J\otimes c):
J\otimes D\otimes A\longrightarrow P_1Y\otimes A.
\tag{FTE16}
\]

All subsequent endpoint comparisons will be made after right tensoring
by A, an equivalence. Thus a verified equality there proves the
original equality on every derived object.

## SH02-FTE-INPUT. The two copies of the source orientation line

Let \(\widetilde b\) be the antipode-canceled FF11 map for r, before its initial
line extraction. Explicitly, on a coefficient K,

\[
\begin{aligned}
\widetilde b(K):\mathcal HP_2K\otimes B
&\xrightarrow{e(P_2K,B)^{-1}}
\mathcal H(P_2K\otimes B)=\mathcal Ha_2Q_2K\\
&\xrightarrow{\chi(Q_2K)^{-1}}a_1\mathcal HQ_2K
\xrightarrow{a_1b_h(K)}a_1Q_1\mathcal RK
=P_1\mathcal RK\otimes A.
\tag{FTE17}
\end{aligned}
\]

Let \(s_H\) be the map whose conjugation by \(\alpha_2,\beta_1\) gives the
alternative transposed endpoint:

\[
s_H=\bar\ell_r^{\,c}(V_2H)
(\mathcal H\alpha_{2,H}\otimes1_D):
J\otimes D\longrightarrow P_1Y.
\tag{FTE18}
\]

Expanding the coherent initial extraction and final inverse coevaluation gives

\[
s_H\otimes1_A
=\widetilde b(M_2Z)
(\mathcal H\alpha_{2,H}\otimes1_B)(1_J\otimes c).
\tag{FTE19}
\]

Here is a proof of this line cancellation. Define
\[
\begin{aligned}
j&=(d\otimes1_{B^\vee})(1_L\otimes u_B):L\longrightarrow A\otimes B^\vee,\\
\phi&=(c\otimes1_{A^\vee})(1_D\otimes u_A):D\longrightarrow B\otimes A^\vee.
\end{aligned}
\tag{FTE19a}
\]
The initial extraction defining \(\ell_r\) inserts \(u_B\), applies \(\widetilde b\otimes1_{B^\vee}\), and then \(j^{-1}\). The coherent final contraction first evaluates \(B^\vee\otimes B\) and then uses \(u_A^{-1}\) on \(A\otimes A^\vee\). The \(B\) duality triangle therefore gives
\[
\bar\ell_r^{\,c}
=(1\otimes u_A^{-1})(\widetilde b\otimes1_{A^\vee})(1\otimes\phi).
\tag{FTE19b}
\]
Tensor on the right by \(A\). By the defining identity
\((1_B\otimes\operatorname{ev}_A)(\phi\otimes1_A)=c\), the \(A\) duality triangle gives
\(\bar\ell_r^{\,c}\otimes1_A=\widetilde b(1\otimes c)\).
Composing with the input unit proves FTE19, with no symmetry inserted into an ordered inverse pair.

To compare
the first two maps, insert \(\alpha_2=b_2^{-1}\eta_2\). The elementary
kernel-module square is

\[
a_2q_2(A_2Z,B)(b_2(Z)^{-1}\otimes1_B)
=(-1)^{n_2}(a_2g_2(Z)^{-1}\otimes1_B).
\tag{FTE20}
\]

Its domain is \(Q_2Z\otimes B\) and its target is \(a_2Q_2A_2Z\otimes B\).
On the left the intermediate object \(P_2M_2Z\otimes B\) is
\(a_2Q_2M_2Z\). Expanding \(b_2\) first undoes its \(P_2\) projection formula
and its input-antipode exchange. Expanding \(q_2\) restores that projection
formula and crosses the B already inside \(M_2Z\) with the rightmost
orientation B of \(Q_2\). The two \(P_2\) projection formulas cancel, the
remaining geometric map is \(a_2g_2^{-1}\), and the single self-braid
is \((-1)^{n_2}\). This is the complete word \(B\otimes B\); neither copy is
silently treated as the other.

Apply FTE10 to \(b_h\) at \(A_2Z\otimes B\) in FTE17. Move the resulting \(q_2\)
through \(\chi\) inverse using its naturality and through e inverse using
its module coherence. Equation FTE20 then supplies \((-1)^{n_2}\). The
remaining coefficient route is

\[
a_1b_h(A_2Z)\chi(Q_2A_2Z)^{-1}
\mathcal H(a_2g_2(Z)^{-1}).
\tag{FTE21}
\]

Naturality of \(\chi\) and its involution identity turn this into the
first route in FTE13:
\(\chi(Q_2A_2Z)^{-1}\mathcal H(a_2g_2^{-1})=a_1\mathcal H(g_2^{-1})a_1\chi(Q_2Z)\).
Thus FTE13 contributes \(\epsilon\) and its remaining output module map
is exactly \(\Psi_Z\). We have proved the map identity

\[
\widetilde b(M_2Z)(\mathcal Hb_2(Z)^{-1}\otimes1_B)
=(-1)^{n_1}\Psi_Z(b_h(Z)\otimes1_B).
\tag{FTE22}
\]

The scalar is \((-1)^{n_2}\epsilon=(-1)^{n_1}\). Compose with
\(\mathcal H\eta_2\otimes1_B\) and the displayed c in FTE19. This gives

\[
s_H\otimes1_A=(-1)^{n_1}K_H.
\tag{FTE23}
\]

This comparison kept \(\chi\) on arbitrary coefficient \(Q_2Z\) until the actual
mate equation FTE13 was applied; it never replaced it by its value on k.

## SH02-FTE-ADJOINT. Compare the complete R3 adjunct

Let \(\gamma_1:P_1A_1\to a_1P_1\) be the input-antipode kernel exchange
underlying \(b_1\). Define

\[
\begin{aligned}
q_X:M_1(X\otimes D)=A_1X\otimes D\otimes A
&\xrightarrow{1\otimes c}A_1X\otimes B\\
&\xrightarrow{c_r(Z)^{-1}\otimes1_B}
\mathcal RA_2Z\otimes B
\xrightarrow{\mathrm{PF}^{-1}}Y.
\tag{FTE24}
\end{aligned}
\]

The right-ordered R3 formula is then exactly

\[
F_h=q_X M_1(E_h(H)\otimes1_D)
 M_1(\mathrm{PF}_{T_1,J,D}),
\tag{FTE25}
\]

where \(\mathrm{PF}_{T_1}:T_1(J\otimes D)\to T_1J\otimes D\). This is FF R3 after
the two opposite coefficient/inverse-line symmetries have canceled.
In particular FTE25 has no guessed sign extracted from LFT-L3.

The adjunct of \(F_h\) under \(V_1\) left adjoint to \(P_1\) is
\(f_H=P_1(F_h)\alpha_{1,J\otimes D}\). Naturality of \(b_1\), the unit module
square verified in SH02-FTE-MODULES, and the \(T_1/Q_1\) adjunct equation
\(Q_1E_h\eta_{1,J}=t_H\) (LFT36) give

\[
f_H=P_1(q_X)b_1(X\otimes D)^{-1}
q_1(X,D)^{-1}(t_H\otimes1_D).
\tag{FTE26}
\]

Every object is fixed here: after \(t_H\otimes1_D\) it is \(Q_1X\otimes D\);
\(q_1\) inverse makes \(Q_1(X\otimes D)\); \(b_1\) inverse makes \(P_1M_1(X\otimes D)\);
\(P_1q_X\) reaches \(P_1Y\). Thus no independent inverse-equivalence
identification has been inserted into the R2 endpoint.

It remains to compare FTE26 tensor A with FTE16. Expand \(q_1\) inverse,
\(b_1\) inverse and \(q_X\). All \(P_1\) right projection formulas and \(\gamma_1\)
maps occur in the same order as in \(\Psi_Z\); \(c_r\) occurs in the same inverse
direction. Their naturality moves them away from the pure line word.
Before the remaining contraction that word is

\[
A\otimes D\otimes A.
\tag{FTE27}
\]

The A at the left comes from \(Q_1X\); the A at the right is the external
tensor used to compare the endpoints. On the FTE26 route, \(q_1\) inverse
first crosses the left A with D, and \(q_X\) contracts D with that A.
It therefore uses

\[
(c\otimes1_A)(\sigma_{A,D}\otimes1_A):
A\otimes D\otimes A\longrightarrow B\otimes A.
\tag{FTE28}
\]

On the common \(K_H\) route, c first contracts D with the external A,
then inverse \(q_1\) in \(\Psi_Z\) crosses the remaining A with B. It uses

\[
\sigma_{A,B}(1_A\otimes c):
A\otimes D\otimes A\longrightarrow B\otimes A.
\tag{FTE29}
\]

Since \(|A|=n_1\), \(|B|=n_2\), \(|D|=n_2-n_1\) modulo 2, FTE28 is \((-1)^{n_1}\)
times FTE29. Explicitly the respective symmetry coefficients are
\((-1)^{n_1(n_2-n_1)}\) and \((-1)^{n_1n_2}\); their ratio is \((-1)^{n_1}\).
The coefficient of the same map c occurs once in each route. This
line equality is independent of its local generator and glues by
evaluation, so it proves an identity of tensor morphisms before
any sheaf image is applied. We obtain

\[
f_H\otimes1_A=(-1)^{n_1}K_H=s_H\otimes1_A.
\tag{FTE30}
\]

Tensoring by A is faithful. Therefore \(f_H\)=\(s_H\) as maps
\(J\otimes D\to P_1Y\), for every H in the full stated category.

## SH02-FTE-TRACE. Restore the original units and conclude the trace equation

Let \(u_i:1\to V_iP_i\) and \(v_i:P_iV_i\to1\) be the original \(P_i\)/\(V_i\)
adjunction. The paired-defect theorem SH02-LFT-ANTIPODE-CHECK gives

\[
v_i\alpha_i=(-1)^{n_i},\quad
v_i^{-1}=\alpha_i(-1)^{n_i},\quad
u_i^{-1}=\beta_i V_i((-1)^{n_i})P_i.
\tag{FTE31}
\]

Substitute these exact maps into \(J^c\), whose definition was LFT34.
The adjunct under \(V_1\) left adjoint to \(P_1\) is \(\epsilon\) \(s_H\): naturality
moves the output scalar through the middle map, while the input
scalar supplies its inverse, equal to itself. The remaining adjunct
of \(\beta_1V_1(s_H)\) is \(s_H\) by the duality triangle. By FTE30 it is
\(\epsilon\) \(f_H\). The adjunction bijection proves \(J^c=\epsilon F_h\).
Finally FTE4 gives \(J^b=\epsilon J^c=F_h\). This proves FTE6.

FGC24 applied to \(r\) gives \(J^b=J^{\mathrm{dir}}\). Its proof uses the final braid in
FTE4, whereas the initial FF11 cancellation remains coherent. Hence

\[
J_h^{\mathrm{dir}}=J_h^b=F_h.
\tag{FTE32}
\]

To complete the input-line comparison, \(\bar\theta_h\) is the LFT-L2 map
\(K\to J\otimes D\), with \(K=h^{-1}H\). Expanding \(F_h\) by FTE25 and then
\(\bar\theta_h\) inserts \(L\otimes D\) next to A. FTE3 contracts \(D\otimes A\)
and leaves \(d^{-1}:A\to L\otimes B\). The remaining coefficient
symmetry is the one in the prescribed R4 source rewrite \(\lambda_h\).
Consequently

\[
F_h V_1\bar\theta_h
=\mathcal R_{12}(E_hT_1\theta_h)\lambda_h
=\Theta_h^{\mathrm{FF}}.
\tag{FTE33}
\]

The equality follows from the displayed duality triangle, with its endpoint now identified by FTE32. No extra parity is added after this contraction.
Equations FTE32–FTE33 prove LFT41. To recover FTC14, apply the inverse of the output antipode/right-line equivalence \(\mathcal R_{12}\). The original R4 map \(D_h\) becomes \(C_h\), while support inclusion commutes with this equivalence by ordinary antipode exchange and the bounded-line projection formula. The direct support transpose LFT35 is \(\nu_rV_2C_h=J_h^{\mathrm{dir}}V_1\bar\theta_h\). Equations FTE32–FTE33 therefore give
\[
\nu_rT_2\circ D_h=E_h\circ T_1\theta_h.
\tag{FTE34}
\]
This is FTC14 with the original R2 and R4 endpoint constructions, the explicitly ordered FF orientation maps, and the unchanged raw Fourier adjunctions. Faithfulness of the equivalence proves equality of maps on every object in the stated category. \(\square\)

## SH02-FTE-PROBLEMS. Follow each sign to its map

**Problem 1.** Let \(h=\operatorname{id}_E\), with \(E\) of odd rank. Explain why FTE6 gives identity at both complete endpoints even though each paired Fourier defect is \(-1\).

**Solution.** The relative line \(L\) is the tensor unit and \(n_1=n_2\), so \(\epsilon=1\). The two paired defects enter as their ratio in the conjugation defining \(J^c\); that ratio is one. The primitive exchange and its mate are identity maps. The coherent extraction inserts the same \(W_E\) coevaluation that its relative-line identification removes. The final contraction has degree zero. Consequently \(J^c=J^b=F_h=1\), under the identity-map orientation identifications. Odd absolute rank contributes two equal factors, not an odd relative-rank sign.

**Problem 2.** Let \(h:\mathbb R\to0\), \(k=\mathbb Z\), with positive dual orientations and coefficient \(H=k\). Compare the coherent, braided and direct transposed endpoints after the coefficient trace input.

**Solution.** The relative line is \(W=O_{\mathbb R}[1]\), its parity is odd, and \(\epsilon=-1\). The R2 map is the positive compact-support trace, so \(F_hV_1\bar\theta_h=\Theta_h^{\mathrm{FF}}\) is positive under its specified orientation identifications. FTE6 gives \(J^cV_1\bar\theta_h=-\Theta_h^{\mathrm{FF}}\). The final braided contraction contributes one further minus sign, so \(J^bV_1\bar\theta_h=\Theta_h^{\mathrm{FF}}\). FGC24 identifies \(J^b\) with \(J^{\mathrm{dir}}\). The transpose is a proper zero inclusion; hence its support-forgetting map is identity. Thus the original two FTC14 routes agree positively, although the intermediate coherent endpoint has the opposite sign. This checks the complete equality without changing either Fourier unit or counit.

**Problem 3.** Why can the proof tensor the two adjuncts by \(A\), yet cannot conclude the same equality merely by checking their values on a constant sheaf?

**Solution.** Tensoring by the invertible graded line \(A\) is an equivalence of the full derived category. It is faithful on every Hom set, so FTE30 proves equality of the original two morphisms for each arbitrary coefficient object. A constant-sheaf test gives one component of a natural transformation and supplies no comparable faithfulness statement. In this proof the parity identity is an equality of line morphisms before arbitrary sheaf operations, while the paired defect used in FTE31 has already been proved on all conic objects. Neither is justified by a single object test.

## SH02-FTE-SOURCES. What the kernel source supplies and what the endpoint proof adds

The corresponding passage is Schapira's [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026, §4.9, pp. 100–101](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=100). It defines the proper kernel transform, writes its tensor–Hom right adjoint, and obtains two graph-kernel descriptions by adjunction. It works with bounded kernels on locally compact spaces of finite soft dimension. FTE-A1–FTE-A2 use that right-adjoint mechanism, with the adjunction read as a Hom bijection so that the actual coordinate-change mate is retained. The stated globally bounded-below scope and arbitrary locally compact base use the separately named programme contracts; they are not inferred merely from the source's functor notation.

The orientation comparison is with [Definition 5.1.4, Proposition 5.1.5 and Proposition 5.1.9, pp. 107–108](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=107). Those passages give the orientation sheaf and the exceptional pullback formula for a topological submersion, whose proof tests on local product neighborhoods by compact-support integration. Here FTE-A3 calculates the degree of negation on the integration fiber and glues it by orientation transition maps. FTE-A4 then carries the ordinary simultaneous coordinate change through the specified reversed halfspace chain. The resulting mate sign is an equality of maps before taking images, not a value assigned to exceptional pullback on arbitrary coefficients from its value on the tensor unit.

Astérisque 128 (1985), [§2.1, Propositions 2.1.5–2.1.6, p. 41](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=44), supplies classical Fourier functoriality statements; the section explicitly omits their proofs. Neither it nor the kernel-adjoint passage specifies the course's coherent initial extraction, braided final contraction, pair of positive adjunctions or the named complete endpoint. FTE6 is therefore proved here from the fixed course data, not imported as the assertion that two isomorphic functors have the same transformation.

The proof carries one mixed kernel through its actual module maps and exceptional antipode exchange, tensors both adjuncts by the same invertible source line, and compares the two ordered three-line words in FTE27–FTE29. Their common target makes the two parity contributions comparable. Faithfulness of tensoring with that line gives the full-object equality in FTE30. Only then does FTE31 insert the already proved paired defect, and FTE3 contracts the input line to recover the trace equation with the original R2/R4 maps. All three solved problems test complete endpoints rather than selected intermediate signs.

The paired-defect theorem and enhanced-center argument remain supplied by SH02-LFT-ANTIPODE-CHECK and SH02-LFT-CENTER, with their own foundations. The direct/graded support identification is supplied by SH02-FGC-SUPPORT. The programme's further conic, orientation, enhancement, mate-coherence and six-operation obligations remain open where stated; this repair does not clear them transitively.

The exposition is organized around a common target, two explicit line crossings and the final adjunction transpose. The cited sources provide classical operation and orientation ingredients, not this sequence of named endpoint calculations. No source diagram or exercise sequence is incorporated. Independently expressed programme text is CC0, while actual human components retain their existing terms.

## SH02-FTE-STATUS. What the complete calculation proves

The endpoint comparison FTE6 and trace equation FTE34 are proved for all continuous fiberwise linear maps between finite-rank bundles over the stated locally compact Hausdorff base, including rank jumps and nonorientable bundles. Coefficients retain the full conic globally bounded-below domain over a commutative unital ring of finite global dimension. The coherent initial FF11 extraction, the braided final support endpoint, the unchanged raw Fourier adjunctions and the prescribed R3/R4 line maps are separately specified.

The dependent microlocal trace comparison is proved in [Following the microlocal comparison maps](microlocal-endpoint-propagation.md), SH02-MEP-TRACE, using the original R2/R4 maps and the counit-normalized normal orientations. SH02-MEP-MATE-UNTWIST separately supplies the contracted ordinary adjoint endpoint. The source account compares the actual foundation passages without identifying an unspecified external convention with these named course maps. The prescribed second-adjunction normalization comparisons FDN18 and FDN19 are different statements, proved in [The geometric normalization of Fourier adjunctions](fourier-literal-normalization.md), SH02-NDF-SOURCE-MAPS. Its full-category defect calculation and unique normalized comparison supply those inverse equations; the present trace proof preserves its own raw adjunctions and does not use that normalization theorem. This working reader does not certify full transitive proof closure, a source-book erratum, formalization or translation.
