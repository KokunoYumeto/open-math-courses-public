# SH02-FGC-UNIT. The graded line in a Fourier support comparison

Original programme text: CC0 1.0 Universal. The complete proof below is relative to its named operation imports. The source account at the end distinguishes the published Fourier statements from the ordered-map calculation proved here.

Two constructions of the same Fourier isomorphism can differ on their orientation line. This lesson computes that difference for every continuous linear bundle map, including maps whose rank varies. It then writes the complete support comparison with the initial line insertion and final line contraction separately visible. The resulting sign comes from the two bundle projections in one mixed correspondence, so no decomposition of the kernel of the map is needed.

The published antecedent used here is the vector-bundle Fourier calculus in M. Kashiwara and P. Schapira, *Microlocal Study of Sheaves*, Astérisque 128 (1985), §2.1. In particular, Proposition 2.1.5 relates proper direct image to inverse image, and exceptional inverse image to ordinary direct image, under Fourier transformation. That statement does not specify the mixed-correspondence antipode transports and the two ordered contractions compared below; those maps are defined and calculated in this lesson.

## SH02-FGC-DEPENDENCIES. Maps that the proof uses

Read [Fourier functoriality](fourier-functoriality.md), SH02-FF-CONVENTIONS, SH02-FF-LINEAR-KERNEL and SH02-FF-MATES, for the primitive kernel isomorphism and its chosen adjunction. Read [The linear Fourier comparison](linear-fourier-trace.md), SH02-LFT-MATE, SH02-LFT-SUPPORT and SH02-LFT-LINE-ORDER, for the direct comparison, its support square and the right-ordered trace input.

The proof uses SH02-FF-BOUNDS for the bounded-below tensor scope; SH02-LFT-IMP-BC-NU and SH02-LFT-IMP-PF-ADJUNCTION for full locally compact Hausdorff proper-support base change, composition, projection formula, exceptional adjunction and their mate-pasting identities; SH02-LFT-IMP-ORIENTATION for bundle orientation traces and their coordinate-change compatibility; and SH02-FS-COMPARE for the actual halfspace comparison. Every exceptional map has the finite abelian-sheaf dimension bound supplied by the bundle ranks. The line factors are bounded invertible objects, and cut factors are flat sheaves in degree zero. These retain their separate import obligations. No comparison with a differently normalized second Fourier adjunction is used.

## SH02-FGC-CONVENTIONS. The two line operations occupy different places

Let \(B\) be locally compact Hausdorff and let \(h:E_1\to E_2\) be any continuous morphism of real vector bundles of fixed finite ranks \(n_1,n_2\) over its identity. Its transpose is \(r:E_2^*\to E_1^*\). The coefficient ring \(k\) is commutative and unital, of finite global dimension. An object \(F\) is arbitrary in \(D^+_{\mathbb R_{>0}}(E_1;k)\), with a global lower bound and the parameter-space scalar transport specified in SH02-FF-DOMAINS. There is no upper bound, finite-stalk, constructibility, orientability, field, constant-kernel-rank, or manifold-base assumption. The bundle ranks give the finite abelian-sheaf proper-support dimension bounds for the exceptional maps. Locally constant ranks are allowed componentwise only when those bounds remain global. Put

\[
W_i=O_{E_i}[n_i],\quad L=\omega_r,\quad
D=R\mathcal Hom(L,k),\quad \epsilon=(-1)^{n_2-n_1}.
\tag{FGC1}
\]

Let \(G_h:r^!T_1\to T_2Rh_*\otimes L\) be the direct comparison LFT17. Let \(\ell_h\) denote the mate-defined FF L3 with its initial FF11 cancellation expanded by the right tensor equivalence FGC21–FGC22 below. The theorem proved here is

\[
\ell_h=\epsilon G_h.
\tag{FGC2}
\]

Define two distinct final endpoint cancellations:

\[
\begin{aligned}
\overline G_h&=(1\otimes\operatorname{coev}_L^{-1})
 (G_h\otimes1_D),\\
\bar\ell_h^{\,b}&=
 (1\otimes\operatorname{ev}_L\sigma_{L,D})
 (\ell_h\otimes1_D).
\end{aligned}
\tag{FGC3}
\]

Here \(\operatorname{ev}_L:D\otimes L\to k\), and \(\operatorname{coev}_L:k\to L\otimes D\). Their ordering
is part of the definition. Since \(L\) has parity \(n_2-n_1\),

\[
\operatorname{ev}_L\sigma_{L,D}
=\epsilon\operatorname{coev}_L^{-1}.
\tag{FGC4}
\]

Equations FGC2 and FGC4 imply \(\bar\ell_h^{\,b}=\overline G_h\). Together with the direct support theorem LFT21, this proves the complete support square written in SH02-FGC-SUPPORT. The input uses LFT-L2, the initial extraction defining L3 uses FGC22, and the final cancellation uses the second line of FGC3. These are three explicitly distinct maps. Using inverse coevaluation at the final original endpoint instead leaves the factor \(\epsilon\).

## SH02-FGC-RAW-MATE. One mixed kernel fixes the adjoint map

Put \(X_i=E_i\times_BE_i^*\), with projections \(p_i\) to \(E_i\) and \(q_i\) to \(E_i^*\). Put
\(Y=E_1\times_BE_2^*\), with projections \(s\) to \(E_1\) and \(q\) to \(E_2^*\). The maps are

\[
u(x,\eta)=(x,r\eta),\qquad v(x,\eta)=(hx,\eta),
\quad p_1u=s,
\quad q_1u=rq,
\quad p_2v=hs,
\quad q_2v=q.
\tag{FGC5}
\]

Let \(N_i\) and \(C_i\) be the nonpositive and nonnegative pairing cuts on \(X_i\).
Write \(N=u^{-1}N_1=v^{-1}N_2\) and \(C=u^{-1}C_1=v^{-1}C_2\). Let \(P_i=T_{E_i^*}\)
and let its **raw** right adjoint be

\[
\mathcal R_i(F)=Rq_{i*}R\Gamma_{N_i}(p_i^!F).
\tag{FGC6}
\]

The bundle formula for \(p_i\) uses the orientation of its fiber \(E_i^*\),
identified positively with \(W_i\). This presentation uses the raw
tensor-Hom/proper-support adjunction; it has no separately chosen second
Fourier adjunction.

Apply original FF primitive exchange to r. Its left-adjoint map is

\[
A_r:h^{-1}P_2\longrightarrow P_1Rr_!.
\tag{FGC7}
\]

The two sides identify, by the actual proper-support base-change and
projection-formula maps, with the same mixed kernel functor

\[
K\longmapsto Rs_!(q^{-1}K\otimes k_N).
\tag{FGC8}
\]

On the left use the cartesian \((v,s,p_2,h)\) square. On the right use the
cartesian \((u,q,q_1,r)\) square, the flat cut, and \(p_1u=s\). This is exactly
the FF6 construction applied to r, rather than a newly chosen isomorphism.

The right adjoint of FGC8 is \(Rq_*R\Gamma_Ns^!\). Consequently the actual right
mate of FGC7 is the following chain:

\[
\begin{aligned}
\Lambda_h(F):r^!\mathcal R_1F
&\longrightarrow Rq_*u^!R\Gamma_{N_1}p_1^!F\\
&\longrightarrow Rq_*R\Gamma_N(u^!p_1^!F)\\
&\longrightarrow Rq_*R\Gamma_Ns^!F\\
&\longrightarrow Rq_{2*}R\Gamma_{N_2}(Rv_*s^!F)\\
&\longrightarrow Rq_{2*}R\Gamma_{N_2}(p_2^!Rh_*F)
=\mathcal R_2Rh_*F.
\end{aligned}
\tag{FGC9}
\]

The first arrow is the exceptional/ordinary-image exchange, the second
the exceptional mate of the flat-cut projection formula, and the third
exceptional transitivity. The fourth is ordinary-image composition and
the ordinary tensor-Hom exchange for the pulled-back cut. The last uses
the inverse of

\[
p_2^!Rh_*\xrightarrow{\sim}Rv_*s^!,
\tag{FGC10}
\]

which is the right mate of proper-support base change
\(h^{-1}Rp_{2!}\to Rs_!v^{-1}\). In particular FGC10 is not an assertion that
arbitrary ordinary base change is invertible.

To verify the **map** in FGC9, the two Hom identifications for FGC7 pass
through
\(\operatorname{Hom}(K,Rq_*R\Gamma_Ns^!F)\), using the tensor-Hom adjunction for exactly the
coefficient in FGC8. Reversing the left proper-kernel identifications gives
the last two arrows of FGC9, and reversing the right ones gives its first
three arrows. Under these identifications precomposition by \(A_r\) is the
identity on that middle Hom group. Hence FGC9 is its right mate, by the
adjunction bijection. Equivalently, this is the mate of the two FF6 squares pasted together.

## SH02-FGC-ORDINARY. Changing the cut by ordinary inverse image

Write \(A_i\) for ordinary inverse image by the antipode of \(E_i^*\). Let \(z_i\) on \(X_i\)
negate only its covector coordinate, and let z on Y negate eta only. Then

\[
p_i z_i=p_i,\quad sz=s,\quad uz=z_1u,\quad vz=z_2v,
\quad q_i z_i=A_iq_i,
\quad qz=A_2q.
\tag{FGC11}
\]

In FGC11 an \(A_i\) on a space denotes its antipode map; in functor expressions
it denotes ordinary inverse image by that map. The maps \(z_i\) and z exchange
N and C and act ordinarily as identity on coefficients pulled from \(p_i\)
or s, including every explicitly base-pulled \(W_i\).

There is an ordinary change-of-coordinates isomorphism

\[
I_i(F):A_i\mathcal R_iF
 \longrightarrow Rq_{i*}R\Gamma_{C_i}(p_i^!F)
 =U_iF\otimes W_i.
\tag{FGC12}
\]

In this definition the coefficient transport \(z_i^{-1}p_i^!F\to p_i^!F\)
is obtained from \(p_i^!F=p_i^{-1}F\otimes W_i\) using **ordinary** identity
on the pulled-back coefficient and line. Call this transport \(\kappa_i\).
It is not the exceptional mate for \(p_i z_i=p_i\).

Let \(d_i:V_i\to\mathcal R_i\) be the fixed raw-adjoint comparison, with
\(V_i=A_iT_i\otimes W_i\). The literal FS6 chain, with its inequalities
interchanged, gives the map identity

\[
I_i\,A_i(d_i)=c_i\otimes1_{W_i}.
\tag{FGC13}
\]

Indeed applying the ordinary output antipode to that chain changes its
positive proper cut to the negative proper cut and its negative local
support to the positive local support. These are exactly the arrows and
inverses defining \(c_i\). The coefficient \(W_i\) stays on the right throughout;
there is no exceptional coordinate action on it in FGC12/FGC13. This checks
the specified \(d_i\), not a right mate chosen after \(c_i\).

## SH02-FGC-ORIENTATION. The transitivity square detects the sign

For the following computation let
\(J=p_1^!F\) and let \(\tau:u^!J\to s^!F\) be exceptional transitivity. Denote
the canonical exceptional exchanges by

\[
\begin{aligned}
\chi_u(J)&:z^{-1}u^!J\longrightarrow u^!z_1^{-1}J,\\
\chi_{p_1}(F)&:z_1^{-1}p_1^!F\longrightarrow p_1^!F,\\
\chi_s(F)&:z^{-1}s^!F\longrightarrow s^!F.
\end{aligned}
\tag{FGC14}
\]

Exceptional transitivity and its counit compatibility give the exactly
typed commutative square

\[
\tau\,u^!\chi_{p_1}(F)\,\chi_u(J)
=\chi_s(F)\,z^{-1}\tau:
z^{-1}u^!p_1^!F\longrightarrow s^!F.
\tag{FGC15}
\]

Both routes are the exceptional exchange for \(sz=s\) after expanding
\(s=p_1u\). To check its normalization, take the proper-support adjunct:
the two composite counits are the trace for s, and proper-support
coordinate-change pasting identifies the same negation of its fiber.
The composite-adjunction counit identity then proves FGC15.

Let \(\kappa_s:z^{-1}s^!F\to s^!F\) be ordinary coefficient transport in
\(s^!F=s^{-1}F\otimes W_2\). The maps \(p_1\) and s are bundle projections of
ranks \(n_1\) and \(n_2\). Their actual exceptional exchanges therefore satisfy

\[
\chi_{p_1}(F)=(-1)^{n_1}\kappa_1(F),\qquad
\chi_s(F)=(-1)^{n_2}\kappa_s(F).
\tag{FGC16}
\]

This follows on arbitrary F from the coefficient orientation trace:
negation of a rank-\(n_i\) integration fiber has degree \((-1)^{n_i}\), and the
coefficient pullback is unchanged. The same orientation local-system
maps appear in every trivialization, so the equality is global even
for nonorientable bundles. These are projection calculations only.

Substitute FGC16 into FGC15 and solve for the following composite:

\[
\kappa_s\,(z^{-1}\tau)\,
 \chi_u(J)^{-1}\,u^!\kappa_1^{-1}
=\epsilon\,\tau:
u^!p_1^!F\longrightarrow s^!F.
\tag{FGC17}
\]

The successive objects on its left are
\(u^!J\), \(u^!z_1^{-1}J\), \(z^{-1}u^!J\), \(z^{-1}s^!F\), and \(s^!F\). Thus every arrow
has the displayed direction; no cancellation of an exceptional exchange
against an ordinary identity is implicit. This is the complete local
coefficient comparison needed below.

Equivalently, the exceptional exchange \(\chi_u\) acts by \(\epsilon\) after
identifying its pulled-back coefficient through LFT19. This assertion is
only about coefficients pulled from \(E_1\). It does not replace
\(\chi_r(T_1F)\), or \(\chi_r\) at any arbitrary object, by a scalar.

## SH02-FGC-TRANSPORT. Retain the exceptional exchange until it reaches the coefficient

Let \(\chi_r:A_2r^!\to r^!A_1\) be the usual exceptional exchange. Write the full
antipode-canceled raw comparison as

\[
\begin{aligned}
K_h: r^!(U_1F\otimes W_1)
&\xrightarrow{r^!I_1^{-1}}r^!A_1\mathcal R_1F\\
&\xrightarrow{\chi_r(\mathcal R_1F)^{-1}}
 A_2r^!\mathcal R_1F
\xrightarrow{A_2\Lambda_h}A_2\mathcal R_2Rh_*F\\
&\xrightarrow{I_2}U_2Rh_*F\otimes W_2.
\end{aligned}
\tag{FGC18}
\]

In FGC18 it is the inverse of \(\chi_r\), as displayed, that is used.

Expand \(\Lambda_h\) by FGC9. Naturality and pasting of exceptional/ordinary
base change move the displayed \(\chi_r^{-1}\) through the first arrow of
FGC9 to \(\chi_u^{-1}\) on its coefficient. Naturality of the exceptional
cut-mate moves it through \(R\Gamma_N\), while ordinary changes \(z_i\),z exchange
that cut with C. At the transitivity arrow the resulting coefficient
route is exactly the left side of FGC17: its initial ordinary transport
is \(u^!\kappa_1^{-1}\), and its final one is \(\kappa_s\). Thus this portion of
the expanded chain is \(\epsilon\) times the direct C-chain transitivity.
This step retains \(\chi_r\) until its mate-pasting image \(\chi_u\) has been
reached; it never treats \(\chi_r\) as scalar on an arbitrary coefficient.

There is no additional scalar at the last FGC10 interchange. Its canonical
exceptional-coordinate square intertwines \(\chi_s\) and \(\chi_{p_2}\). Both bundle
projections have rank \(n_2\), so replacing those two exceptional coefficient
actions by \(\kappa_s\) and \(\kappa_2\) cancels the same factor \((-1)^{n_2}\) on the two
routes. Consequently FGC10 respects their ordinary transports. The
ordinary cut-Hom exchange and q-image composition also respect ordinary
coordinate change. They contain no new orientation permutation.

It follows that \(K_h\) is \(\epsilon\) times the chain obtained from FGC9 by
replacing N with C and using the direct transitivity map \(\tau\). This is an
identity of the full natural maps on arbitrary F, using only counit,
projection-formula, cut-mate, and Cartesian-pasting identities.

## SH02-FGC-EXTRACTION. Extract the right line by tensor equivalence

Write \(Z=T_2Rh_*F\) and \(X=r^!T_1F\). FF3a specifies

\[
d:L\otimes W_1\longrightarrow W_2.
\tag{FGC19}
\]

By LFT19, the direct C-chain of SH02-FGC-TRANSPORT, after extracting the input
\(W_1\) on the right, is exactly \((1_Z\otimes d)(G_h\otimes1_{W_1})\). Indeed
LFT19 defines its coefficient identification by \(u^!p_1^!F=s^!F\) and right
cancellation of \(W_1\); this is the same \(\tau\) and same FF3a d, not a separate
orientation identification. Both coefficient and line orders are retained.

Use FGC13 at the two endpoints of FGC18. The original antipode-canceled
FF11 map, denoted \(\widetilde\ell_h\), therefore satisfies

\[
\widetilde\ell_h
=\epsilon(1_Z\otimes d)(G_h\otimes1_{W_1}):
X\otimes W_1\longrightarrow Z\otimes W_2.
\tag{FGC20}
\]

For clarity the coherent extraction defining original L3 can be written
without an unspecified forward evaluation. Put \(D_1=R\mathcal Hom(W_1,k)\), let
\(u_1:k\to W_1\otimes D_1\) be coevaluation, and define

\[
j:L\longrightarrow W_2\otimes D_1,
\qquad j=(d\otimes1_{D_1})(1_L\otimes u_1).
\tag{FGC21}
\]

This is exactly the FF3a identification, characterized by tensoring
right by \(W_1\) and evaluating \(D_1\otimes W_1\). Then

\[
\ell_h=(1_Z\otimes j^{-1})
 (\widetilde\ell_h\otimes1_{D_1})(1_X\otimes u_1).
\tag{FGC22}
\]

Substitute FGC20. Naturality of tensoring moves \(G_h\) through the insertion,
and the remaining map on L is \(j^{-1}(d\otimes1_{D_1})(1_L\otimes u_1)=1_L\).
Thus FGC22 is \(\epsilon G_h\), proving FGC2 for this explicitly fixed coherent
initial FF11 completion. No symmetry is added in this step. The output
line in the final FTC13 cancellation has not yet been canceled.

Finally apply FGC4 to that final line. The two factors \(\epsilon\) multiply
to one, and FGC3 gives \(\bar\ell_h^{\,b}=\overline G_h\). The direct support square LFT21
therefore becomes the square with this precisely specified original L3
and final braided evaluation. Initial FF11 coevaluation and final FTC13
braided evaluation occupy different places and are not interchanged.

## SH02-FGC-SCOPE. Why the proof includes maps whose rank jumps

For an identity bundle map, \(\epsilon=1\) and d is the identity-unit
transitivity. The initial coherent FF11 extraction gives the identity;
the final relative line is the tensor unit. For a zero inclusion the formula gives the parity of its transpose projection; Problem 2 checks the complete input and final contraction on every coefficient object.
The proof above uses the mixed kernel directly and does not assume a separate projection calculation or a partial Fourier factorization.

This argument never assumes that a sheaf conic for joint scaling is
conic in one direct-sum factor. In particular it does not reduce a
general projection \(E_1\) direct-sum \(E_2\) -> \(E_2\) by a fiberwise conic contraction.
Rank jumps are handled by the mixed diagram and the two full vector
bundle projections, which exist without a kernel bundle.

## SH02-FGC-SUPPORT. The completed support square

**Theorem.** Keep the primitive map \(A_h:r^{-1}T_1\to T_2Rh_!\) of FF6, the right-ordered map \(\bar\theta_r\) of LFT-L2, the coherent initial extraction FGC22 defining \(\ell_h\), and the final braided contraction \(\bar\ell_h^{\,b}\) of FGC3. Then on every conic \(D^+\) coefficient object in SH02-FGC-CONVENTIONS,
\[
\bar\ell_h^{\,b}\circ\bar\theta_r
 =T_2(\nu_h)\circ A_h:
r^{-1}T_1\longrightarrow T_2Rh_*.
\tag{FGC23}
\]

**Proof.** FGC2 is an equality of the actual uncontracted natural maps, proved by FGC6–FGC22. The parity identity FGC4 gives
\[
\bar\ell_h^{\,b}
=\epsilon^2\overline G_h
=\overline G_h.
\tag{FGC24}
\]
LFT21 identifies \(\overline G_h\bar\theta_r\) with the right side of FGC23. All three input and endpoint conventions are preserved in that substitution. This proves the equality. \(\square\)

This proves the linear support equation FTC13 with its chosen maps. Braided evaluation and inverse coevaluation are different forward-ordered contractions. With the same initial extraction and input but inverse coevaluation at the final original endpoint, the left side is \(\epsilon\) times the right side. For a zero inclusion into an odd-rank bundle with integral coefficients it can differ from it.

## SH02-FGC-PROBLEMS. Three tests of the completed convention

**Problem 1.** For \(h=\operatorname{id}_E\), verify both the initial extraction and the final support endpoint when \(E\) has odd rank.

**Solution.** Here \(n_1=n_2\), so \(\epsilon=1\) and \(L=k\). The FF11 map is the identity on \(T_EF\otimes W_E\). The map \(j\) of FGC21 is coevaluation for \(W_E\), and FGC22 cancels that very insertion by \(j^{-1}\). Hence \(\ell_h=1\). The final line is the tensor unit, so braided evaluation and inverse coevaluation agree there. Thus FGC23 is the identity square. The odd rank of \(E\) alone introduces no sign: the relevant parity at the final endpoint is the relative rank.

**Problem 2.** For the zero inclusion \(i:B\to E^*\), with \(E\) of rank \(n\), check FGC23 on an arbitrary \(K\in D^+(B;k)\).

**Solution.** The transpose is the projection \(\pi:E\to B\). The primitive map identifies the Fourier transform of \(Ri_*K\) with \(\pi^{-1}K\); both cuts contain its zero-section support. Since \(i\) is proper, the right side of FGC23 is identity. The direct kernel comparison is the positive projection orientation identification on \(\pi^{-1}K\otimes W_E\). By FGC2, the uncontracted original map is \((-1)^n\) times this map. The input \(\bar\theta_\pi\) inserts \(\operatorname{coev}_{W_E}\) on the right: the coefficient symmetry in the definition of \(\theta_\pi\) cancels the coefficient symmetry in LFT-L2. The final braid contributes another \((-1)^n\). Their product is one. The calculation works on arbitrary complexes because those two coefficient symmetries are inverse as natural transformations; it uses no finite-stalk assumption.

**Problem 3.** Let \(B=\mathbb R\), \(E_1=B\times\mathbb R^2\), \(E_2=B\times\mathbb R\), and \(h_b(x,y)=bx\). Locate the sign in the proof at \(b=0\).

**Solution.** The kernel dimension jumps at zero, but \(p_1\) and \(s\) remain vector-bundle projections of ranks two and one. Their exceptional antipode exchanges have signs \(+1\) and \(-1\). The typed transitivity square FGC15 therefore gives \(\epsilon=-1\) throughout \(B\). The cut and mate construction remains defined at zero, so FGC2 holds without selecting a kernel bundle. The final braided contraction again cancels that uniform factor.

## SH02-FGC-STATUS. Keep the support and trace proofs distinct

The proved results are the full-map identity FGC2 and the support square FGC23 with the separately specified initial extraction, trace input and final braided contraction. Their proof includes arbitrary locally compact Hausdorff bases, arbitrary conic bounded-below coefficients over the stated ring, nonorientable bundles and rank jumps. The downstream microlocal endpoint is proved in [Following the microlocal comparison maps](microlocal-endpoint-propagation.md), SH02-MEP-SUPPORT and SH02-MEP-MATE-UNTWIST. The operation imports remain those explicitly declared in SH02-FF-DOMAINS; this calculation does not replace their foundational proofs.

The trace equation FTC14 and its exact reformulation LFT41 are proved separately in [The complete transpose endpoint](fourier-transpose-endpoint.md), SH02-FTE-TRACE. That proof uses the full L3 comparison here and then compares the additional units, counits and orientation-line maps. The parity identity alone would not prove it. The distinct prescribed second-adjunction normalization comparisons FDN18 and FDN19 are proved in [The geometric normalization of Fourier adjunctions](fourier-literal-normalization.md), SH02-NDF-SOURCE-MAPS, by the actual full-category defect calculation and the unique normalized opposite comparison. That theorem is separate from the support and trace proofs here.

**Published source and proof mechanism.** [Kashiwara–Schapira, *Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), printed pp. 39–41 (PDF pp. 42–44), gives the two halfspace presentations in Proposition 2.1.1 and Definition 2.1.2, inverse equivalences in Theorem 2.1.3(i), and the two linear functorialities in Proposition 2.1.5. Its §2.1 expressly recalls these results without proofs. The exceptional inverse image in Proposition 2.1.5(ii) is essential: it is not an ordinary inverse-image formula with the orientation line discarded. The source allows a locally compact base and bounded-below conic complexes, but its half-line formulation is compared with the parameter-conic category through the course's conic-descent proof, not by silently identifying two definitions.

The construction here supplies the map-level step not printed in that statement. FGC9 is obtained by taking the mate of the common mixed-cut proper-image map; FGC10 is the mate of proper-support base change, rather than an arbitrary ordinary-image base-change isomorphism. FGC15 then compares the two exceptional antipode transports by transitivity. Their projection-fibre degrees give the relative-rank sign in FGC17–FGC20 even when the linear map has rank jumps. Finally FGC21–FGC22 undo the specified initial insertion, and FGC4 identifies the distinct final contractions. This sequence proves FGC23 for the declared maps without deriving a sign from an isomorphism of endpoint objects.

For the operation primitives, [Pierre Schapira, *An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026 version](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), Theorem 4.5.3 and equation (4.5.4), p. 93, give proper-support base change and its compact-support fibre formula. Theorem 4.6.1 and Corollary 4.6.2, pp. 94–95, provide dimension-bounded exceptional adjunction and transitivity; Proposition 5.1.9, pp. 107–108, gives the submersion orientation formula by a local trace calculation. These supply the relevant mechanisms, not the ordered sign comparison above. The two-bounded-below projection formula still uses the explicit truncation argument SH02-FF-BOUNDS: the printed projection formula, Theorem 4.4.7, p. 91, has boundedness hypotheses that cannot simply be dropped. The source terminology and mathematics are credited here; the independently written course argument is under CC0, and the human works retain their own terms.
