# Composing sheaf operators through an intermediate space

Course: SH-02. Unit: SH02-KER. Language: English.

The prerequisite proofs below are supplied by [Finite resolutions and proper supports on locally compact spaces](../../../SH-02/finite-resolutions-and-proper-supports.html) and the compact-support and coefficient constructions it links. The kernel calculation retains the general locally compact spaces and full bounded-below test-object range stated here.

Original text is dedicated under CC0 1.0 Universal. Linked materials retain their own licenses.

The aim is to calculate a composite sheaf operator by eliminating its intermediate variable, then determine when that calculation supplies an inverse. A kernel here is a complex of sheaves on a product. Its support may have noncompact fibers, its stalks may be infinitely generated, and its coefficients may have torsion. Proper support is part of the operation used to eliminate the variable.

## SH02-KER-001. Ambient objects and conventions

Let \(A\) be a commutative ring with identity and finite global dimension. Fix an integer \(g\geq 0\) bounding its global dimension. No Noetherian, field, or finite-generation assumption is imposed. The zero ring is allowed in statements that do not expressly exclude it. The extra condition \(A\ne 0\) will be used only for detecting a nonzero cohomological shift.

For a topological space \(T\), write \(A_T\) for its constant coefficient sheaf and \(D(A_T)\) for the derived category of sheaves of \(A_T\)-modules. Write \(D^+(A_T)\) for objects whose cohomology vanishes below a single integer, and \(D^b(A_T)\) for objects whose cohomology vanishes outside a finite interval. These are global bounds on the object; stalkwise bounds that vary without a uniform bound do not suffice. We use cochain complexes:

\[
H^i(E[s])=H^{i+s}(E).
\]

All tensor products of complexes below are derived over the indicated constant coefficient sheaf, and \(R\mathcal Hom\) is the internal derived Hom. An expression \(\operatorname{Hom}_{D(A_T)}(E,F)\) denotes a morphism set, rather than an internal Hom sheaf.

The spaces \(X,Y,Z\) are locally compact Hausdorff spaces of finite c-soft dimension. This topological dimension condition is taken for sheaves of abelian groups, not merely for sheaves over a specially chosen coefficient ring. A c-soft sheaf is one whose sections over a compact subset extend to the whole space. Fix finite bounds \(d_T\) for the lengths of c-soft resolutions on each space \(T\) that occurs. The foundational dimension theorem recalled below allows us to use the same bounds for compact-support cohomology and for projections with fiber \(T\). Products occurring in the construction have finite c-soft dimension as well.

For a continuous map \(f:U\to V\), the sheaf \(f_!E\) consists locally of sections of \(E\) whose support is proper over the open subset of \(V\) under consideration. Proper means that inverse images of compact sets are compact. In particular, \(f_!\) is not being replaced by \(f_*\). We use \(Rf_!\) and its right adjoint \(f^!\), as well as the ordinary adjunction \(f^{-1}\dashv Rf_*\). For constant coefficients, \(f^{-1}\) is exact and preserves the tensor unit and derived tensor products.

This unit has no manifold, orientation, noncharacteristic, constructibility, or finite-rank hypotheses. It also makes no claim that an arbitrary sheaf kernel is determined by its induced functor.

## SH02-KER-002. The prerequisite contract

The following contracts specify the exact maps and bounds used by the calculation. [Finite resolutions and proper supports](../../../SH-02/finite-resolutions-and-proper-supports.html#LCH1) proves the general topological dimension criterion, coefficient transfer, fibre and product bounds, and exceptional adjunction. Its [derived algebra and projection proof](../../../SH-02/finite-resolutions-and-proper-supports.html#LCH4) supplies the bounded-kernel tensor–Hom adjunction and both actual mixed projection maps.

### SH02-KER-IMP-DER. Derived sheaf algebra

Sheaves admit the resolutions needed to construct derived tensor and internal Hom. The resulting tensor product is associative and symmetric, with symmetry on homogeneous terms given by the Koszul sign \((-1)^{ij}\). Inverse image preserves it. There are natural adjunction bijections

\[
\operatorname{Hom}(B\otimes_A^L C,D)
 \simeq \operatorname{Hom}(C,R\mathcal Hom_A(B,D)),
\qquad
\operatorname{Hom}(f^{-1}C,D)
 \simeq \operatorname{Hom}(C,Rf_*D).
\]

The constant-coefficient specializations of the Stacks Project's [flat resolutions and derived tensor product](https://stacks.math.columbia.edu/tag/06Y7), [derived pullback](https://stacks.math.columbia.edu/tag/06YI), and [internal derived Hom adjunction](https://stacks.math.columbia.edu/tag/08DJ) supply these algebraic constructions. They do not, by themselves, supply exceptional inverse image or proper-support base change. For the actual bounded kernel and bounded-below test objects used here, [the derived-algebra proof](../../../SH-02/finite-resolutions-and-proper-supports.html#LCH4) gives the finite flat model, injective internal-Hom model and chain-level currying, retaining every product over an unbounded-above source.

### SH02-KER-IMP-GEOM. Compact supports and dimension

We import the c-soft resolution theorem, its characterization of finite c-soft dimension by uniform compact-support cohomological bounds, and its consequences for coefficients. For a projection \(p:S\times T\to S\), proper base change gives, for every sheaf \(M\),

\[
(R^j p_!M)_s
 \simeq H_c^j\bigl(T;M|_{\{s\}\times T}\bigr).
\tag{KER-G1}
\]

Consequently \(p_!\) has cohomological dimension at most \(d_T\), including on sheaves of abelian groups. There are composition isomorphisms

\[
Rf_!Rh_!\simeq R(fh)_!,
\]

and the associated compact-support Leray and hypercohomology spectral sequences. A closed embedding \(i\) has \(Ri_!=i_*=i_!\), an exact functor.

Here is the useful dimension consequence, with its argument made explicit. For a sheaf \(M\) on \(S\times T\), the compact-support Leray sequence has terms

\[
H_c^p(S;R^q p_!M)
 \Longrightarrow H_c^{p+q}(S\times T;M).
\]

The terms vanish for \(q>d_T\) by (KER-G1), and for \(p>d_S\) by the c-soft dimension bound on \(S\). Thus \(H_c^j(S\times T;M)=0\) for \(j>d_S+d_T\), uniformly in \(M\). The imported dimension criterion gives

\[
d_{S\times T}\leq d_S+d_T.
\tag{KER-G2}
\]

Applying this to abelian sheaves first establishes the topological bound required for exceptional inverse image. Iteration treats threefold products. No coefficient global-dimension term is needed in (KER-G2); that term will enter only when taking derived tensor products.

### SH02-KER-IMP-BCPF. Two specified comparison isomorphisms

For a Cartesian square of the spaces under consideration,

\[
\begin{array}{ccc}
U'&\xrightarrow{u}&U\\
{f'}\downarrow&&\downarrow f\\
V'&\xrightarrow{v}&V,
\end{array}
\]

we use the proper-support base-change isomorphism

\[
\beta:v^{-1}Rf_!M\xrightarrow{\sim}Rf'_!u^{-1}M.
\tag{KER-BC}
\]

Its underlying comparison takes a local proper-supported section to its pullback; properness of its support persists under this Cartesian pullback. Derived base change is the corresponding canonical comparison on resolutions. The theorem asserts that it is an isomorphism; it does not require \(f\) itself to be proper.

We also use the proper-support projection formula

\[
\pi_f:N\otimes_A^L Rf_!M
 \xrightarrow{\sim}
 Rf_!(f^{-1}N\otimes_A^L M).
\tag{KER-PF}
\]

The comparison comes from tensoring a pulled-back local section of \(N\) with a section of \(M\) proper over the base; its support remains proper. The derived comparison is formed using flat and proper-support-acyclic resolutions. The required range here is \(M,N\in D^+\) with at least one of them bounded, with the above finite coefficient and map-dimension bounds. The passage from the bounded-input formula to this mixed range is proved in SH02-KER-PF-RANGE below. Both directions of (KER-PF), together with the stated tensor symmetry, will be used explicitly. Unlike the usual perfect-object projection formula for arbitrary \(Rf_*\), this import is for \(Rf_!\) on locally compact Hausdorff spaces and does not require a perfect kernel.

### SH02-KER-IMP-DUAL. The exceptional adjunction

For the relevant maps with finite cohomological dimension of \(f_!\) on abelian sheaves, we import the construction

\[
f^!:D^+(A_V)\longrightarrow D^+(A_U),
\qquad Rf_!\dashv f^!.
\]

Its unit is \(\eta^f:\mathrm{id}\to f^!Rf_!\), and its counit is \(\epsilon^f:Rf_!f^!\to\mathrm{id}\). Their triangle identities and naturality are part of this adjunction. The [exceptional-adjoint construction](../../../SH-02/finite-resolutions-and-proper-supports.html#LCH3) proves the construction of \(f^!\), including its passage from abelian-sheaf dimension to general \(A\)-coefficients, its differential signs and the trace-preserving comparison between resolution choices. We use neither a manifold formula for \(f^!\) nor a replacement of internal Hom by tensoring with a dual.

## SH02-KER-003. Bounds that make the operators well-defined

**Lemma.** Suppose \(B\in D^{[a,b]}(A_T)\), \(C\in D^{\geq m}(A_T)\), and \(Q\in D^{\geq t}(A_T)\). Then

\[
B\otimes_A^L C\in D^{\geq a+m-g}(A_T),
\qquad
R\mathcal Hom_A(B,Q)\in D^{\geq t-b}(A_T).
\tag{KER-A1}
\]

If also \(C\in D^{\leq n}\), then

\[
B\otimes_A^L C\in D^{[a+m-g,b+n]}(A_T).
\tag{KER-A2}
\]

If \(f_!\) has cohomological dimension at most \(d\), then

\[
Rf_!D^{[u,v]}\subset D^{[u,v+d]},
\qquad
f^!D^{\geq m}\subset D^{\geq m-d}.
\tag{KER-A3}
\]

**Proof.** The tensor bounds can be checked at stalks: a K-flat sheaf resolution remains K-flat on taking a stalk. At each stalk, the hyper-Tor spectral sequence has entries

\[
\bigoplus_{i+j=q}
\operatorname{Tor}^A_p(H^i(B)_x,H^j(C)_x)
\quad\text{in total degree }q-p.
\]

They vanish unless \(a\leq i\leq b\), \(j\geq m\), and \(0\leq p\leq g\). This puts every possible total degree at least \(a+m-g\). With \(j\leq n\), every total degree is at most \(b+n\). The finite \(i\)-range and finite Tor range ensure that every total degree receives only finitely many terms even when \(C\) is unbounded above; equivalently, one obtains the same bounds by finite truncation of \(B\), finite flat dimension, and truncating \(C\) above the degree being tested. Thus the bounded-below spectral sequence converges in the range used. Vanishing at all stalks proves the asserted sheaf bounds.

For internal Hom, choose a representative of \(B\) zero outside \([a,b]\) and a bounded-below injective representative of \(Q\) zero below \(t\). The total internal Hom complex in degree \(r\) has factors

\[
\mathcal Hom_A(B^i,I^{i+r}).
\]

If \(r<t-b\), each factor is zero. This complex computes the internal derived Hom by SH02-KER-IMP-DER. Hence the second bound in (KER-A1) holds. This argument supplies a lower bound only; it does not assert an upper bound on internal Hom for arbitrary sheaves.

The first assertion in (KER-A3) follows from the hypercohomology spectral sequence for \(Rf_!\): its sheaf cohomology indices lie in \([u,v]\), and its derived-functor indices lie in \([0,d]\). Right derived functors of left exact functors also preserve a lower bound for a bounded-below input.

For the assertion about \(f^!\), its existence as a functor on \(D^+\) is the import SH02-KER-IMP-DUAL. Let \(Q\in D^{\geq m}\) and put \(E=f^!Q\). If

\[
B_0=\tau_{\leq m-d-1}E,
\]

then \(B_0\) is bounded, since \(E\in D^+\). The first assertion of (KER-A3) gives \(Rf_!B_0\in D^{\leq m-1}\). The standard derived-category orthogonality and the exceptional adjunction yield

\[
\operatorname{Hom}(B_0,E)
 \simeq\operatorname{Hom}(Rf_!B_0,Q)=0.
\]

The truncation map \(B_0\to E\) is therefore zero. It induces isomorphisms on cohomology in every degree at most \(m-d-1\), so those cohomology sheaves vanish. This proves the last bound. \(\square\)

The finite Tor bound is the only part of this lemma that uses \(g\). Finite weak global dimension would suffice for that tensor estimate. We retain finite global dimension throughout the unit because it is the coefficient convention of the source-range results being covered; we do not use the weaker tensor hypothesis to make an unverified change to the other imports.

### SH02-KER-PF-RANGE — Extending the bounded projection formula

The bounded-input projection formula is enough for the mixed ranges used
in (KER-C4) and (KER-C5). Here is the reduction, including its canonical
map. Assume the comparison (KER-PF) has been constructed naturally on
bounded-below objects, and is known to be an isomorphism when both inputs
are bounded. These are the bounded formula and resolution constructions
in SH02-KER-IMP-BCPF.

First let the base factor \(N\) be bounded with lower bound \(a\), and
let \(M\) be bounded below. For an integer \(t\), use the truncation
triangle

\[
M_{\leq t}\longrightarrow M\longrightarrow T_t\longrightarrow M_{\leq t}[1],
\qquad T_t\in D^{\geq t+1}.
\]

The truncation \(M_{\leq t}\) is bounded. Apply the two exact functors
on the sides of (KER-PF) to this triangle. By (KER-A1), exactness of
inverse image and lower-bound preservation by \(Rf_!\), both resulting
tail objects satisfy

\[
N\otimes_A^L Rf_!T_t\in D^{\geq t+1+a-g},
\qquad
Rf_!(f^{-1}N\otimes_A^L T_t)\in D^{\geq t+1+a-g}.
\]

For a fixed degree \(q\), choose \(t\) so large that \(t+a-g>q\).
The tails have zero cohomology in degrees \(q-1\) and \(q\), so the
truncation maps induce isomorphisms in degree \(q\) on both sides.
Naturality gives a commutative square between the comparison for
\(M_{\leq t}\) and the comparison for \(M\). The former is an isomorphism
by the bounded formula. Hence the latter is an isomorphism on
\(H^q\). This works for every \(q\), proving (KER-PF) in this case.

Next let the source factor \(M\) be bounded with lower bound \(a\), and
let \(N\) be bounded below. Truncate \(N\), with tail
\(S_t\in D^{\geq t+1}\). Finite cohomological dimension makes
\(Rf_!M\) bounded, with the same lower bound \(a\). Thus

\[
S_t\otimes_A^L Rf_!M\in D^{\geq t+1+a-g},
\qquad
Rf_!(f^{-1}S_t\otimes_A^L M)\in D^{\geq t+1+a-g}.
\]

The same truncation square proves the comparison an isomorphism in
each degree. The natural comparison itself, rather than an unspecified
isomorphism between its endpoints, has therefore been proved invertible
in both required ranges. No direct image has been interchanged with an
infinite limit, and no perfectness or finite-generation hypothesis has
been added. The bounded projection formula, resolution existence and
finite map-dimension assumptions remain the declared inputs. \(\square\)

## SH02-KER-004. Kernels as operators and their right adjoints

Let

\[
p:X\times Y\to X,\qquad q:X\times Y\to Y,
\qquad K\in D^b(A_{X\times Y}).
\]

Define

\[
\Phi_K(G)=Rp_!(K\otimes_A^L q^{-1}G),
\qquad G\in D^+(A_Y),
\tag{KER-O1}
\]

and

\[
\Psi_K(F)=Rq_*R\mathcal Hom_A(K,p^!F),
\qquad F\in D^+(A_X).
\tag{KER-O2}
\]

The first coordinate is the output coordinate of \(\Phi\). Thus \(\Phi_K\) goes from \(Y\) to \(X\), while \(\Psi_K\) goes from \(X\) to \(Y\).

For \(K\in D^{[a,b]}\) and \(G\in D^{\geq m}\), the tensor in (KER-O1) has lower bound \(a+m-g\). Consequently \(\Phi_K(G)\in D^+(A_X)\). If \(G\in D^{[m,n]}\), the stronger bound is

\[
\Phi_K(G)\in D^{[a+m-g,b+n+d_Y]}(A_X).
\tag{KER-O3}
\]

For \(F\in D^{\geq m}\), (KER-A3) gives \(p^!F\in D^{\geq m-d_Y}\), (KER-A1) gives internal Hom lower bound \(m-d_Y-b\), and \(Rq_*\) preserves this lower bound. Therefore

\[
\Psi_K(F)\in D^{\geq m-d_Y-b}(A_Y).
\tag{KER-O4}
\]

This proves that both displayed operators have the stated \(D^+\) domains and codomains. Formula (KER-O3) also proves that \(\Phi_K\) preserves \(D^b\). We do not impose an upper cohomological bound on \(\Psi_K(F)\) for a general bounded input.

A kernel morphism \(u:K\to K'\) induces a natural transformation \(\Phi_u:\Phi_K\to\Phi_{K'}\) by tensoring with \(u\) and applying \(Rp_!\). Contravariance of internal Hom gives \(\Psi_u:\Psi_{K'}\to\Psi_K\). These are adjoint mates under the next proposition. All these functors are exact, and the shift rules are

\[
\Phi_{K[s]}=\Phi_K[s],\qquad
\Psi_{K[s]}=\Psi_K[-s],\qquad
\Psi_K(F[s])=\Psi_K(F)[s].
\tag{KER-O5}
\]

## SH02-KER-005. The adjunction, with its structural maps

**Proposition.** There is a natural adjunction \(\Phi_K\dashv\Psi_K\) on the categories in SH02-KER-004.

**Proof.** For \(G\in D^+(A_Y)\) and \(F\in D^+(A_X)\), first transpose a map across \(Rp_!\dashv p^!\), then across the tensor-Hom adjunction, then across \(q^{-1}\dashv Rq_*\). This gives

\[
\begin{aligned}
\operatorname{Hom}_{D(A_X)}(\Phi_KG,F)
&\simeq
\operatorname{Hom}_{D(A_{X\times Y})}
 (K\otimes_A^L q^{-1}G,p^!F)\\
&\simeq
\operatorname{Hom}_{D(A_{X\times Y})}
 (q^{-1}G,R\mathcal Hom_A(K,p^!F))\\
&\simeq
\operatorname{Hom}_{D(A_Y)}(G,\Psi_KF).
\end{aligned}
\tag{KER-ADJ}
\]

Every transposition is a bijection with inverse given by the corresponding counit or evaluation. Their composite is therefore a bijection, natural in both arguments. All intermediate objects lie in the needed bounded-below categories by SH02-KER-003 and SH02-KER-004. This is the required adjunction. \(\square\)

For clarity, its unit \(\eta^K_G:G\to\Psi_K\Phi_KG\) is the composite

\[
\begin{aligned}
G
&\longrightarrow Rq_*q^{-1}G\\
&\longrightarrow
Rq_*R\mathcal Hom_A(K,K\otimes_A^L q^{-1}G)\\
&\longrightarrow
Rq_*R\mathcal Hom_A
 (K,p^!Rp_!(K\otimes_A^L q^{-1}G)).
\end{aligned}
\tag{KER-UNIT}
\]

The arrows are, respectively, the ordinary inverse-image unit, the tensor-Hom unit, and the image under \(Rq_*R\mathcal Hom_A(K,-)\) of the exceptional unit for \(p\). Its counit \(\epsilon^K_F:\Phi_K\Psi_KF\to F\) is

\[
\begin{aligned}
Rp_!\bigl(K\otimes_A^L
 q^{-1}Rq_*R\mathcal Hom_A(K,p^!F)\bigr)
&\longrightarrow
Rp_!\bigl(K\otimes_A^L R\mathcal Hom_A(K,p^!F)\bigr)\\
&\longrightarrow Rp_!p^!F
\longrightarrow F.
\end{aligned}
\tag{KER-COUN}
\]

Here the first arrow uses the counit of \(q^{-1}\dashv Rq_*\), the second is tensor-Hom evaluation, and the third is \(\epsilon^p\). The evaluation uses the stated symmetry when the standard Hom convention places \(K\) on the other side. Thus it includes the usual Koszul signs.

These maps satisfy the triangle identities: (KER-UNIT) is the image of \(\mathrm{id}_{\Phi_KG}\) under (KER-ADJ), and (KER-COUN) is the inverse image of \(\mathrm{id}_{\Psi_KF}\). Naturality of (KER-ADJ), applied to these identities, gives

\[
\epsilon^K_{\Phi_KG}\circ\Phi_K(\eta^K_G)=\mathrm{id},
\qquad
\Psi_K(\epsilon^K_F)\circ\eta^K_{\Psi_KF}=\mathrm{id}.
\]

The same transposition, with a morphism \(u:K\to K'\) inserted in the tensor factor, puts that morphism in the first, contravariant input of internal Hom. This verifies the mate statement for \(\Phi_u\) and \(\Psi_u\), including its direction.

## SH02-KER-006. Eliminating the middle variable

Let \(K\in D^b(A_{X\times Y})\) and \(L\in D^b(A_{Y\times Z})\). On \(X\times Y\times Z\), write \(r_{12},r_{13},r_{23}\) for the two-coordinate projections. Define their convolution over \(Y\) by

\[
K\star_Y L
 =Rr_{13!}(r_{12}^{-1}K\otimes_A^L r_{23}^{-1}L).
\tag{KER-C1}
\]

The order in this notation agrees with operator composition: the right factor acts first. If \(K\in D^{[a,b]}\) and \(L\in D^{[c,e]}\), then

\[
K\star_Y L\in
D^{[a+c-g,b+e+d_Y]}(A_{X\times Z}).
\tag{KER-C2}
\]

Indeed, inverse image is exact, (KER-A2) bounds the tensor, and \(r_{13}\) has fiber \(Y\) and proper-support cohomological dimension at most \(d_Y\). Thus the convolution is again a bounded kernel; no properness assumption on \(\operatorname{supp}(K)\) or \(\operatorname{supp}(L)\) has entered.

**Proposition.** There are natural isomorphisms

\[
\theta:\Phi_K\Phi_L\xrightarrow{\sim}\Phi_{K\star_Y L},
\qquad
\sigma:\Psi_L\Psi_K\xrightarrow{\sim}\Psi_{K\star_Y L}.
\tag{KER-C3}
\]

**Proof of the first isomorphism.** Denote the projections by

\[
\begin{array}{lll}
a:X\times Y\to X,&b:X\times Y\to Y,\\
c:Y\times Z\to Y,&d:Y\times Z\to Z,\\
e:X\times Z\to X,&f:X\times Z\to Z.
\end{array}
\]

Let \(t_X,t_Z\) be the first and third projections from the threefold product. Given \(G\in D^+(A_Z)\), put \(B=L\otimes_A^L d^{-1}G\). Then \(B\in D^+\). The square with maps \(r_{12},r_{23},b,c\) is Cartesian, so (KER-BC) supplies the indicated second line in the following calculation:

\[
\begin{aligned}
\Phi_K\Phi_LG
&=Ra_!\bigl(K\otimes_A^L b^{-1}Rc_!B\bigr)\\
&\xrightarrow[\beta]{\sim}
Ra_!\bigl(K\otimes_A^L Rr_{12!}r_{23}^{-1}B\bigr)\\
&\xrightarrow[\pi_{r_{12}}]{\sim}
Ra_!Rr_{12!}
 \bigl(r_{12}^{-1}K\otimes_A^L r_{23}^{-1}B\bigr)\\
&\xrightarrow{\sim}
Rt_{X!}\bigl(r_{12}^{-1}K\otimes_A^L
 r_{23}^{-1}L\otimes_A^L t_Z^{-1}G\bigr).
\end{aligned}
\tag{KER-C4}
\]

The third line is exactly (KER-PF), with bounded base factor \(K\). The last line uses \(ar_{12}=t_X\), \(dr_{23}=t_Z\), composition of \(!\)-images, and monoidality of inverse image. Write \(M=r_{12}^{-1}K\otimes_A^L r_{23}^{-1}L\), a bounded complex. Since \(t_X=er_{13}\) and \(t_Z=fr_{13}\), the final expression in (KER-C4) continues as

\[
\begin{aligned}
Re_!Rr_{13!}
 \bigl(M\otimes_A^L r_{13}^{-1}f^{-1}G\bigr)
&\xrightarrow[\pi_{r_{13}}^{-1}]{\sim}
Re_!\bigl(Rr_{13!}M\otimes_A^L f^{-1}G\bigr)\\
&=\Phi_{K\star_Y L}G.
\end{aligned}
\tag{KER-C5}
\]

The first arrow is the inverse projection formula, expressed with the base factor on the right using the specified tensor symmetry. Its bounded factor is \(M\), while \(f^{-1}G\) is only required to be bounded below. All direct images have finite cohomological dimension by the projection and product bounds. Thus no unbounded totalization or unsupported extension of (KER-PF) is implicit. The composite (KER-C4)-(KER-C5) defines \(\theta\), naturally in \(K,L,G\).

**Proof and definition of the second isomorphism.** Put \(C=K\star_Y L\). For every \(G\in D^+(A_Z)\) and \(F\in D^+(A_X)\), the first part and SH02-KER-005 give

\[
\begin{aligned}
\operatorname{Hom}(G,\Psi_L\Psi_KF)
&\simeq\operatorname{Hom}(\Phi_K\Phi_LG,F)\\
&\xrightarrow{\,\theta_G^{-1}\,}
\operatorname{Hom}(\Phi_CG,F)\\
&\simeq\operatorname{Hom}(G,\Psi_CF).
\end{aligned}
\tag{KER-C6}
\]

The middle map is precomposition by \(\theta_G^{-1}\), so its direction is specified. These are natural bijections. Yoneda gives a unique natural isomorphism \(\sigma_F\) inducing them.

In terms of the already specified units and counits, \(\sigma_F\) is the following explicit mate. Start with \(\Psi_L\Psi_KF\), apply \(\eta^C\), replace \(\Phi_C\) by \(\Phi_K\Phi_L\) using \(\theta^{-1}\), then use the two counits:

\[
\begin{aligned}
\Psi_L\Psi_KF
&\longrightarrow\Psi_C\Phi_C\Psi_L\Psi_KF\\
&\longrightarrow\Psi_C\Phi_K\Phi_L\Psi_L\Psi_KF\\
&\xrightarrow{\Psi_C\Phi_K(\epsilon^L_{\Psi_KF})}
 \Psi_C\Phi_K\Psi_KF\\
&\xrightarrow{\Psi_C(\epsilon^K_F)}\Psi_CF.
\end{aligned}
\tag{KER-C7}
\]

The first two arrows are respectively \(\eta^C_{\Psi_L\Psi_KF}\) and \(\Psi_C(\theta^{-1}_{\Psi_L\Psi_KF})\). Equation (KER-C6) proves that (KER-C7) is invertible. This argument obtains the right-adjoint composition from the proved \(!\)-composition and adjunction. It does not presume that arbitrary inverse image commutes with internal Hom or that ordinary \(*\)-base change is always invertible. \(\square\)

## SH02-KER-007. The diagonal test

Let \(\delta_X:X\to X\times X\) be the diagonal, and set

\[
I_X=\delta_{X*}A_X=A_{\Delta_X}.
\]

The diagonal is closed because \(X\) is Hausdorff. Thus \(I_X\) is a bounded kernel in degree zero, with stalk \(A\) on the diagonal and zero elsewhere.

**Proposition.** There are natural isomorphisms

\[
\Phi_{I_X}\simeq\mathrm{id}_{D^+(A_X)},
\qquad
\Psi_{I_X}\simeq\mathrm{id}_{D^+(A_X)}.
\tag{KER-D1}
\]

**Proof.** Write \(p_1,p_2\) for the projections from \(X\times X\). The projection formula for the closed embedding \(\delta_X\), followed by exactness of its direct image, gives

\[
I_X\otimes_A^L p_2^{-1}G
 \simeq R\delta_{X!}
 \bigl(A_X\otimes_A^L\delta_X^{-1}p_2^{-1}G\bigr)
 \simeq\delta_{X!}G.
\]

Here \(p_2\delta_X=\mathrm{id}_X\). Applying \(Rp_{1!}\) and using \(p_1\delta_X=\mathrm{id}_X\) proves the first assertion with a specified natural comparison. The identity functor is right adjoint to itself. By SH02-KER-005, \(\Psi_{I_X}\) is right adjoint to \(\Phi_{I_X}\); the first assertion and uniqueness of a representing right adjoint prove the second. More explicitly, \(\operatorname{Hom}(G,\Psi_{I_X}F)\simeq\operatorname{Hom}(G,F)\) naturally for every \(G\), and Yoneda supplies the isomorphism. \(\square\)

In particular,

\[
\Phi_{I_X[s]}\simeq[s],\qquad
\Psi_{I_X[s]}\simeq[-s].
\tag{KER-D2}
\]

The absence of a dimension or orientation shift in (KER-D1) follows from the two identity composites of the diagonal with the projections. It does not follow from identifying an exceptional inverse image with an ordinary inverse image.

## SH02-KER-008. Two inverse kernels, including shifts

**Theorem.** Let \(K\in D^b(A_{X\times Y})\) and \(L\in D^b(A_{Y\times X})\). Suppose specified isomorphisms of kernels give

\[
L\star_X K\simeq I_Y[r],\qquad
K\star_Y L\simeq I_X[s]
\tag{KER-E1}
\]

for integers \(r,s\). Then each of \(\Phi_K,\Phi_L,\Psi_K,\Psi_L\) is an equivalence between its stated bounded-below derived categories. One has

\[
\begin{aligned}
\Phi_K^{-1}&\simeq\Psi_K
 \simeq\Phi_L[-r]\simeq\Phi_L[-s],\\
\Phi_L^{-1}&\simeq\Psi_L
 \simeq\Phi_K[-r]\simeq\Phi_K[-s].
\end{aligned}
\tag{KER-E2}
\]

They also restrict to equivalences between the bounded derived categories. If \(A\ne0\) and \(X\ne\varnothing\), then \(r=s\).

**Proof.** Put \(F=\Phi_K\) and \(G=\Phi_L\). Kernel morphism functoriality, SH02-KER-006, and the shifted diagonal formula imply

\[
GF\simeq[r]\text{ on }D^+(A_Y),\qquad
FG\simeq[s]\text{ on }D^+(A_X).
\tag{KER-E3}
\]

We first prove equivalence without presupposing equality of the shifts. Because exact functors commute with shifts, \(H=G[-r]\) is a left inverse of \(F\), and \(J=G[-s]\) is a right inverse. Write the isomorphisms as

\[
\alpha:HF\xrightarrow{\sim}\mathrm{id}_{D^+(A_Y)},
\qquad
\beta:FJ\xrightarrow{\sim}\mathrm{id}_{D^+(A_X)}.
\]

There is a natural isomorphism

\[
H\xrightarrow{H\beta^{-1}}HFJ
 \xrightarrow{\alpha J}J.
\tag{KER-E4}
\]

Consequently \(FH\simeq FJ\simeq\mathrm{id}\) as well as \(HF\simeq\mathrm{id}\), proving that \(F\) is an equivalence. Since \(G=H[r]\), \(G\) is also an equivalence. This elementary argument uses only the two supplied natural isomorphisms; it places no triangle-coherence requirement on the originally supplied kernel isomorphisms in (KER-E1).

Every quasi-inverse of an equivalence is both a left and a right adjoint: the Hom bijection is obtained by applying the equivalence and the inverse isomorphisms, or equivalently by transporting identity morphisms across the fully faithful functor. Thus uniqueness of right adjoints identifies \(\Psi_K\) with both \(H\) and \(J\). Interchanging \(F,G\) gives the second line of (KER-E2). This proves the equivalence of all four functors.

The bound (KER-O3) proves that \(F,G\) preserve bounded objects. Their shifted quasi-inverses do too. Hence their inverse isomorphisms restrict to \(D^b\), and (KER-E2) shows that the right adjoints preserve bounded objects under the present inverse-kernel hypotheses. No general upper bound for arbitrary \(\Psi\) was used.

Finally, associating \(FGF\) in the two ways in (KER-E3) yields a natural isomorphism \(F[r]\simeq F[s]\). Since \(F\) is essentially surjective and commutes with shifts, every \(Q\in D^+(A_X)\) satisfies \(Q[r]\simeq Q[s]\). Take \(Q=A_X\). At any point of the nonempty space \(X\), the stalk of \(A_X[r]\) has its only nonzero cohomology in degree \(-r\), and that of \(A_X[s]\) in degree \(-s\). Since \(A\ne0\), these degrees coincide. Thus \(r=s\). \(\square\)

The exceptional cases matter. If \(A=0\), all the sheaf categories and both diagonal kernels vanish; arbitrary \(r,s\) satisfy the same assertions, so equality of shifts cannot be deduced. If \(A\ne0\) and \(X\) is empty, (KER-E1) forces \(Y\) to be empty as well: otherwise its nonzero diagonal could not be isomorphic to the zero convolution. When both spaces are empty, all shifts act on the zero category and there is again no shift rigidity. If \(A\ne0\) and exactly one space is empty, (KER-E1) is impossible.

## SH02-KER-009. Worked example: infinite fibers distinguish the two adjoints

Take \(A=\mathbb Z\) and let \(X=Y=\mathbb Z\) with the discrete topology. These are locally compact Hausdorff spaces of c-soft dimension zero. A sheaf is a family of abelian groups; a complex of sheaves is a family of complexes with the global cohomological bound required by \(D^+\). Let \(K=A_{X\times Y}\), concentrated in degree zero.

For a point \(x\), compact subsets of its discrete fiber are finite. Proper-supported direct image is therefore direct sum over the fiber, so

\[
(\Phi_K G)_x=\bigoplus_{y\in\mathbb Z}G_y.
\tag{KER-M1}
\]

This holds for complexes as written: direct sums of modules are exact, and no higher fiber cohomology occurs. On the same discrete spaces, the right adjoint of summation along a fiber is the repetition of the object on each point of that fiber. Thus \((p^!F)_{(x,y)}=F_x\). Internal Hom from \(A\) is the identity, and ordinary direct image along \(q\) is product. Products of modules are exact, giving

\[
(\Psi_K F)_y=\prod_{x\in\mathbb Z}F_x.
\tag{KER-M2}
\]

The adjunction reduces to a transparent statement: maps from each summand \(G_y\) to each \(F_x\) can be indexed either first by \(x\) or first by \(y\). This is exactly the Hom bijection between (KER-M1) and (KER-M2).

The support of this kernel is the entire product, and its projections have infinite fibers. With \(G_y=\mathbb Z\), replacing \(!\) by \(*\) in (KER-M1) would replace the direct sum by the product. The family equal to \(1\) at every integer belongs to the product and not to the direct sum. Thus that substitution would change the operator even in degree zero. Infinite-rank stalks or torsion families can equally be used in this example.

## SH02-KER-010. Exercise: a translated diagonal and the sign of the inverse

Let \(X=Y=\mathbb Z\) be discrete and let \(A\) satisfy SH02-KER-001. Define the closed subsets

\[
\Gamma=\{(x,y):x=y+3\}\subset X\times Y,
\qquad
\Gamma'=\{(y,x):x=y+3\}\subset Y\times X.
\]

For integers \(u,v\), set \(K=A_\Gamma[u]\) and \(L=A_{\Gamma'}[v]\). Compute both convolutions, the two \(\Phi\)-operators, and \(\Psi_K\). Which shift of \(L\) gives an actual inverse kernel for \(K\)? Prove your answer for arbitrary modules, not only for finite-dimensional vector spaces.

**Solution.** On the discrete threefold product, the tensor defining \(K\star_Y L\) is supported at triples satisfying \(x=y+3=x'\). For each \(x=x'\), exactly one integer \(y=x-3\) occurs. Each surviving tensor stalk is \(A\otimes_A^L A[u+v]=A[u+v]\), since \(A\) is free of rank one over itself. Projection along the middle coordinate therefore has no higher direct image and gives

\[
K\star_Y L=I_X[u+v].
\]

The same calculation for \(L\star_X K\) uses \(x=y+3=y'+3\), so \(y=y'\), and gives \(I_Y[u+v]\). Directly from the single-point fibers,

\[
(\Phi_KG)_x=G_{x-3}[u],\qquad
(\Phi_LF)_y=F_{y+3}[v].
\]

To undo \(\Phi_K\), one must translate back and shift by \(-u\). The inverse-kernel normalization is

\[
L[-(u+v)]=A_{\Gamma'}[-u],
\qquad
(\Psi_KF)_y=F_{y+3}[-u].
\]

This also follows from (KER-E2). All computations used only the tensor unit, exact finite summation, and shifts; arbitrary stalk modules and every ring in the stated class are included. If \(A=0\), the displayed formulas still hold, although shifts are no longer distinguishable.

## SH02-KER-011. Exercise: torsion detects the lower tensor bound

Let both spaces be a point, \(A=\mathbb Z\), \(K=(\mathbb Z/6)[2]\), and \(G=\mathbb Z/10\) in degree zero. Compute the cohomology of \(\Phi_KG\). Then explain which part of the definition would be lost by using ordinary tensor product.

**Solution.** Use the free resolution \([\mathbb Z\xrightarrow{6}\mathbb Z]\) of \(\mathbb Z/6\), in degrees \(-1,0\). After tensoring with \(\mathbb Z/10\), the kernel and cokernel of multiplication by \(6\) are both \(\mathbb Z/2\). After the shift by \(2\), the only nonzero cohomology groups are

\[
H^{-3}(\Phi_KG)=\mathbb Z/2,
\qquad
H^{-2}(\Phi_KG)=\mathbb Z/2.
\]

Here \(K\in D^{[-2,-2]}\), \(G\in D^{[0,0]}\), \(g=1\), and the point has \(d=0\). The interval predicted by (KER-O3) is exactly \([-3,-2]\). Ordinary tensor product would retain the cokernel in degree \(-2\) and discard the Tor group in degree \(-3\). Hence passing silently to vector-space intuition would lose part of this operator.

## SH02-KER-012. Antecedents, reuse, and exact remaining work

The kernel formalism is presented in Pierre Schapira's freely available
[An Introduction to Sheaves on Grothendieck Topologies, version dated
1 August 2026, §4.9, pp. 100–101](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf).
Equation (4.9.2) defines proper-support composition of bounded kernels;
Proposition 4.9.1 gives its associative comparison, with the detailed
calculation on a product of four spaces assigned to Exercise 4.7. Equations
(4.9.4)–(4.9.7) describe a kernel operator, composition of operators and
its right adjoint. Proposition 4.9.2 realizes the ordinary and
proper-support sheaf operations by graph kernels.

The coordinate convention needs care. This reading makes the first
coordinate the output, using the source's operation “kernel composed
with input.” Its named operator instead places the input on the first
coordinate. Swapping the two factors identifies its convention with
ours; without that swap, a quoted adjoint or composition formula would
have the wrong domain and codomain.

| Construction in this reading | Exact source comparison and proof supplied here |
|---|---|
| Coefficients and topological dimension | The notes' general convention on p. 9 is a commutative unital ring of finite global dimension. Their “soft” condition in Definition 4.3.1, p. 86, is extension from compact subsets, which is the c-soft convention used here. Definition 4.3.13, p. 89, records the finite-dimension conditions. The product bound (KER-G2) is derived here from compact-support Leray and the explicitly imported dimension criterion. |
| Proper-support base change | Theorem 4.5.3, p. 93, treats bounded-below objects and includes the compact-support fibre formula (4.5.4). Its proof uses exact inverse image and sheaves acyclic on the fibres. This is the base-change comparison in (KER-C4); it imposes no properness on the whole kernel support. |
| Projection formula and its range | Theorem 4.4.7, p. 91, takes a bounded source factor and a bounded-above base factor; its proof uses almost-free and proper-image-acyclic resolutions. Its bounded-input case is the foundational input here. SH02-KER-PF-RANGE proves the two mixed bounded/bounded-below extensions needed by (KER-C4)–(KER-C5), using the lower bounds already proved in SH02-KER-003. |
| Right adjoint and actual comparison maps | Theorem 4.6.1, p. 94, supplies the exceptional adjoint under finite cohomological dimension and invokes representability for its existence. Formula (4.9.6), p. 101, gives the kernel adjoint after the coordinate swap. Here (KER-ADJ) composes three Hom transpositions on the full stated category, (KER-UNIT) and (KER-COUN) specify the structural maps, and (KER-C6)–(KER-C7) construct the right-adjoint composition as the mate of the proved left-adjoint comparison. |
| Diagonals, inverse kernels and examples | Proposition 4.9.2 explains the graph-kernel mechanism. Here the diagonal proof uses its two identity projections directly. The shifted inverse criterion then uses the explicit isomorphism between a left and a right inverse, followed by a nonzero-stalk test for equality of shifts. The zero-ring and empty-space cases, infinite discrete fibres, translated diagonal and torsion calculation are treated by the arguments and solutions in this reading. |

The bounded input range of the notes' §4.9 does not by itself settle the
bounded-below operator and test-object range here. The explicit estimates
(KER-A1)–(KER-A3), the projection-range proof, and (KER-O3)–(KER-O4)
justify that passage under the stated foundational contracts. In
particular, the right adjoint is only asserted to preserve bounded
objects when the inverse-kernel hypotheses have been imposed. Proper-support
\(!\)-composition is essential: ordinary direct image \(Rf_*\) is never substituted for proper-support direct image in
the convolution; the infinite discrete example shows the difference
already in degree zero.

The algebraic constructions in SH02-KER-IMP-DER are compared with the
official Stacks Project native source at revision
[a04446e5](https://github.com/stacks/stacks-project/tree/a04446e57ec1fbc252a871afcec7752fb2807b14).
In cohomology.tex, [Tag 06Y7](https://stacks.math.columbia.edu/tag/06Y7)
constructs derived tensor products using K-flat resolutions, proves that
K-flatness can be checked on stalks, and records the graded symmetry.
[Tag 06YI](https://stacks.math.columbia.edu/tag/06YI) constructs derived
pullback and its compatibility with tensor products. For the constant
coefficient sheaves used here, this specializes to exact inverse image.
[Tag 08DJ](https://stacks.math.columbia.edu/tag/08DJ) proves the internal
Hom adjunction through K-flat and K-injective representatives and its
sections over open sets. These are constructions of ringed-space
derived algebra; they do not supply topological proper supports or
exceptional inverse image.

This exposition develops the boundedness estimates before the operator
calculus, constructs the units and counits, calculates the middle-variable
elimination in its two projection-formula configurations, and only then
tests diagonal and inverse kernels. The discrete and torsion examples
exercise precisely the support and coefficient issues those steps use.
The classical constructions are credited above; the independently
written course text is CC0. The linked human works retain their own
terms, including the Stacks Project's
[GFDL terms](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/COPYING).

[Finite resolutions and proper supports](../../../SH-02/finite-resolutions-and-proper-supports.html) supplies these foundational constructions at the full scope used here. Its resolution criterion and coefficient transfer prove the geometric contract; the actual compact-support comparison maps prove base change and composition; the finite integral model constructs the exceptional adjoint; and finite flat and injective models construct the coefficient algebra. Its two mixed projection maps are precisely the maps to which SH02-KER-PF-RANGE applies. The proofs retain arbitrary stalk modules, general finite-c-soft-dimension locally compact Hausdorff spaces, and globally bounded-below test objects.

The spherical-kernel calculation, conic Fourier transformation, manifold
duality, specialization, microlocalization, microlocal Hom, microsupport
estimates and involutivity require their own hypotheses and proofs.
They are not consequences asserted by this unit.
