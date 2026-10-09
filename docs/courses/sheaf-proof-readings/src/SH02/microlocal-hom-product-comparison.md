# SH02-MHPC — Transporting both inputs before forming internal Hom

Course SH-02, unit SH02-MHPC. Original AI-authored programme expression is dedicated under CC0 1.0 Universal. The argument constructs the general ordinary-inverse-image comparison discussed in SH02-MH-HOM-PRODUCT-OPEN. Its explicitly named prerequisite proofs remain separate obligations in their stated scope; cited human-authored sources retain their own terms.

An exceptional inverse image need not agree with ordinary inverse image up to a fixed orientation twist. That fact does not prevent the desired microlocal Hom comparison. The construction here first transports each directional morphism to the common manifold. It then forms an internal Hom there. Exceptional restriction enters only for the diagonal of that common manifold, where composition of adjunctions gives exactly the needed ordinary coefficient objects.

## SH02-MHPC-CONVENTIONS — The maps and their bounds

Let $k$ be a commutative unital ring of finite global dimension. All input complexes belong to $D^b$ of arbitrary $k$-module sheaves. They need not be constructible, have finite stalks, or be perfect. Manifolds are finite-dimensional smooth real manifolds, Hausdorff and countable at infinity. Maps in this lesson are arbitrary smooth maps; no submersion or noncharacteristic hypothesis is imposed. No manifold is assumed oriented or compact.

Write

$$
M_U(A,B)=\mu hom_U(A,B),\qquad
a_U:T^*U\longrightarrow T^*U,\quad (u,\xi)\longmapsto(u,-\xi),
$$

and write $K^a=a_U^{-1}K$. An external product over a common base means the derived tensor product of ordinary inverse images to the fibre product. All tensor products below are derived. For any map $v:U\to V$, set

$$
E_v=U\times_VT^*V,
\quad
\varpi_v:E_v\to T^*V,
\quad
\rho_v:E_v\to T^*U,
\quad
\rho_v(u,\xi)=(u,dv_u^*\xi).
$$

The proof uses four individually specified constructions from [microlocal Hom](../../SH02-microlocal-hom.html): common invertible-line cancellation SH02-MH-TWISTS; the two inverse comparisons MH19 and MH20 in SH02-MH-PAIR-TRANSPORT; and the ordinary-product comparison MH23 in SH02-MH-HOM-PRODUCT. It does not assume that unit's general fibre-product ordinary-Hom target. The required microlocal external-product and inverse-image operations retain their prerequisites in [microlocalization](../../SH02-microlocalization.html). Proper-support base change, its projection formula, composition and internal exceptional adjunction are the contracts in [exceptional operations](../../SH02-exceptional-operations.html); orientation traces and boundedness are specified in [manifold duality](../../SH02-manifold-duality.html).

In the notation above, the two inverse comparisons used here are

$$
R\rho_{v!}\varpi_v^{-1}M_V(A_2,A_1)
\longrightarrow M_U(v^{-1}A_2,v^{-1}A_1)
\tag{MHPC1}
$$

and

$$
R\rho_{v!}\varpi_v^{-1}M_V(A_2,A_1)
\longrightarrow M_U(v^!A_2,v^!A_1).
\tag{MHPC2}
$$

They are morphisms for arbitrary $v$, rather than asserted isomorphisms. Their construction uses the actual trace-induced map $v^{-1}A\otimes\omega_{U/V}\to v^!A$ with its prescribed direction. Common tensoring of both arguments by an invertible shifted local system $L$ gives the canonical isomorphism

$$
M_U(A_2,A_1)\simeq M_U(A_2\otimes L,A_1\otimes L).
\tag{MHPC3}
$$

All spaces of covectors used below are vector bundles or products of vector bundles over manifolds. Their dimensions are finite. The proper-support image functors therefore have the uniform finite cohomological-dimension bounds required by the operation contracts, including when a transpose derivative has varying rank. Derived tensor preserves boundedness by finite global dimension of $k$. Internal Hom of bounded inputs is bounded by the manifold and coefficient dimension theorem SH02-MD-BOUNDED-HOM. Thus every displayed microlocal Hom and every intermediate proper-support image lies in the stated bounded derived category. This checks definedness without a finite-rank or proper-map restriction on the sheaves.

## SH02-MHPC-DIAGONAL — Internal Hom convolution on one manifold

Let $U$ be a manifold, and let $A_1,A_2,B_1,B_2\in D^b(k_U)$. On the fibre product of two cotangent bundles, write

$$
s:T^*U\times_UT^*U\longrightarrow T^*U,
\qquad s(u,\xi,\eta)=(u,\xi+\eta).
$$

There is a canonical morphism

$$
\begin{aligned}
&Rs_!\bigl(M_U(A_2,A_1)^a\boxtimes_U M_U(B_2,B_1)\bigr)\\
&\qquad\longrightarrow
M_U\bigl(R\mathcal Hom(A_1,B_2),R\mathcal Hom(A_2,B_1)\bigr).
\end{aligned}
\tag{MHPC4}
$$

Here is a construction that does not use the general fibre-product statement. Put $W=U\times U$, let $p_1,p_2$ be its projections, and let $\delta:U\hookrightarrow W$ be the diagonal. The already constructed ordinary-product comparison is

$$
\begin{aligned}
&M_U(A_2,A_1)^a\boxtimes M_U(B_2,B_1)\\
&\qquad\longrightarrow M_W(H_1,H_2),\\
H_1&=R\mathcal Hom(p_1^{-1}A_1,p_2^{-1}B_2),\\
H_2&=R\mathcal Hom(p_1^{-1}A_2,p_2^{-1}B_1).
\end{aligned}
\tag{MHPC5}
$$

The projection $p_2$ is a submersion. Its relative dualizing object

$$
L=\omega_{W/U}=p_1^{-1}\omega_U
$$

is an invertible shifted local system, and $p_2^!B=p_2^{-1}B\otimes L$. Tensoring an internal Hom by such a line commutes with moving the line into its second argument. This is checked locally where the line is a constant free rank-one module with a shift, and the resulting natural isomorphisms glue. Therefore

$$
\begin{aligned}
H_1\otimes L&\simeq R\mathcal Hom(p_1^{-1}A_1,p_2^!B_2),\\
H_2\otimes L&\simeq R\mathcal Hom(p_1^{-1}A_2,p_2^!B_1).
\end{aligned}
$$

Use MHPC3 to replace the target of MHPC5 by $M_W(H_1\otimes L,H_2\otimes L)$. Pull the map back to $E_\delta=U\times_WT^*W$, apply $R\rho_{\delta!}$, and follow it by MHPC2 for $\delta$. The resulting two arguments are $\delta^!(H_i\otimes L)$. Internal exceptional adjunction and composition give

$$
\begin{aligned}
\delta^!R\mathcal Hom(p_1^{-1}A,p_2^!B)
&\simeq R\mathcal Hom(\delta^{-1}p_1^{-1}A,\delta^!p_2^!B)\\
&\simeq R\mathcal Hom(A,B).
\end{aligned}
\tag{MHPC6}
$$

Both composites $p_1\delta$ and $p_2\delta$ are the identity. In particular $\delta^!p_2^!\simeq\mathrm{id}^!=\mathrm{id}$ is the composition isomorphism of the actual exceptional adjunctions. It leaves no orientation line and no shift. This identity is the reason to introduce $L$ before exceptional restriction. It does not replace $\delta^!$ by $\delta^{-1}$ on an arbitrary coefficient object.

Finally $E_\delta$ identifies with $T^*U\times_UT^*U$. The transpose derivative of the diagonal sends $(\xi,\eta)$ to $\xi+\eta$, so $\rho_\delta=s$. Pulling the source of MHPC5 back to this bundle gives exactly the source of MHPC4. This completes its construction. The product comparison, common-line isomorphism, exceptional inverse comparison, and internal adjunction are all natural in the four inputs, so MHPC4 is natural as well.

## SH02-MHPC-EXCHANGE — Two proper-support images and one addition map

The next identity keeps the geometric part of the proof separate from the Hom arguments. Suppose $E\to U$ and $E'\to U$ are vector bundles and $r:E\to T^*U$, $t:E'\to T^*U$ are smooth maps over $U$. For bounded $P$ on $E$ and $Q$ on $E'$, the standard proper-support comparisons give a canonical isomorphism

$$
R(r\times_Ut)_!(P\boxtimes_UQ)
\simeq Rr_!P\boxtimes_URt_!Q.
\tag{MHPC7}
$$

No properness of $r$ or $t$ is required. To see precisely which comparisons occur, factor $r\times_Ut$ as

$$
E\times_UE'
\xrightarrow{\,1_E\times_Ut\,}E\times_UT^*U
\xrightarrow{\,r\times_U1\,}T^*U\times_UT^*U.
$$

The first square with $t:E'\to T^*U$ and the second-coordinate projection is cartesian. Proper-support base change identifies the image of the second factor $Q$ with the inverse image of $Rt_!Q$; the projection formula retains the first factor $P$. The intermediate object is consequently

$$
\operatorname{pr}_E^{-1}P\otimes
\operatorname{pr}_{T^*U}^{-1}Rt_!Q.
$$

For the second map use its cartesian square with $r$ and the first-coordinate projection. The projection formula moves the already obtained second factor through the image, and base change identifies the first factor with the inverse image of $Rr_!P$. Proper-support composition proves MHPC7. These are the base-change and projection maps for $!$ throughout; replacing them by ordinary-image fibre formulas would not justify the identity.

Compose with addition $s$. If $h=s\circ(r\times_Ut)$, proper-support composition gives

$$
Rh_!(P\boxtimes_UQ)
\simeq Rs_!(Rr_!P\boxtimes_URt_!Q).
\tag{MHPC8}
$$

There is a second compatibility we will need. If $r$ is linear on the vector-bundle fibres, then it commutes with their antipodes. The cartesian square of the two antipodal homeomorphisms yields

$$
Rr_!(P^a)\simeq(Rr_!P)^a.
\tag{MHPC9}
$$

Since this is inverse image across a homeomorphism and proper-support base change, it introduces no orientation factor. Orientation signs enter only when an exceptional inverse image or a shifted tensor permutation actually occurs.

## SH02-MHPC-TRANSPORT — A comparison for two arbitrary maps

Let $f:U\to X$ and $g:U\to Y$ be arbitrary maps of manifolds. Define

$$
C=E_f\times_UE_g
=U\times_{X\times Y}(T^*X\times T^*Y),
$$

and let $b_X:C\to T^*X$, $b_Y:C\to T^*Y$ be the evident maps. Write

$$
h:C\to T^*U,
\qquad
h(u,\xi,\eta)=(u,df_u^*\xi+dg_u^*\eta).
$$

For $F_1,F_2\in D^b(k_X)$ and $G_1,G_2\in D^b(k_Y)$, there is a canonical morphism

$$
\begin{aligned}
&Rh_!\bigl(b_X^{-1}M_X(F_2,F_1)^a
\otimes b_Y^{-1}M_Y(G_2,G_1)\bigr)\\
&\qquad\longrightarrow
M_U\bigl(
R\mathcal Hom(f^{-1}F_1,g^{-1}G_2),
R\mathcal Hom(f^{-1}F_2,g^{-1}G_1)\bigr).
\end{aligned}
\tag{MHPC10}
$$

Put

$$
P=\varpi_f^{-1}M_X(F_2,F_1),\qquad
Q=\varpi_g^{-1}M_Y(G_2,G_1).
$$

The source of MHPC10 is $Rh_!(P^a\boxtimes_UQ)$. Apply MHPC8 and MHPC9 with $r=\rho_f$ and $t=\rho_g$ to identify it with

$$
Rs_!\bigl((R\rho_{f!}P)^a\boxtimes_UR\rho_{g!}Q\bigr).
$$

Apply the ordinary inverse comparison MHPC1 separately for $f$ and $g$. Their antipodal pullback and external tensor product give a map from this object to

$$
Rs_!\bigl(
M_U(f^{-1}F_2,f^{-1}F_1)^a
\boxtimes_U
M_U(g^{-1}G_2,g^{-1}G_1)\bigr).
$$

Now use MHPC4 with $A_i=f^{-1}F_i$ and $B_i=g^{-1}G_i$. Its target is exactly the target of MHPC10. This constructs the desired morphism for both arbitrary maps at once.

Every factor is either a specified natural comparison or a canonical isomorphism from proper-support composition. There is no choice of a splitting of a tangent map, orientation generator, transverse approximation, or cone representative. The sign in the source has its usual directional meaning: if the original $X$-morphism has covector $\xi$ and the $Y$-morphism has covector $\eta$, the antipodal first factor is placed at $-\xi$, and the output covector is $-df^*\xi+dg^*\eta$. The map $h$ itself remains the positive sum on its displayed coordinates.

## SH02-MHPC-FIBRE-PRODUCT — The full ordinary-inverse-image target

Let $X\to S$ and $Y\to S$ be maps of manifolds, and suppose the fibre product $Z=X\times_SY$ is an embedded submanifold of $X\times Y$. Let $j:Z\hookrightarrow X\times Y$ be that embedding, and let $q_X,q_Y$ be its projections. The covector correspondence is

$$
T^*Z\xleftarrow{\rho_j}
Z\times_{X\times Y}(T^*X\times T^*Y)
\xrightarrow{\varpi_j}T^*X\times T^*Y.
$$

Apply MHPC10 with $U=Z$, $f=q_X$ and $g=q_Y$. Since $dj=(dq_X,dq_Y)$, restriction of a covector pair to $TZ$ is

$$
\rho_j(z,\xi,\eta)
=(z,dq_X^*\xi+dq_Y^*\eta)=h(z,\xi,\eta).
$$

Moreover the pullback tensor product on $C$ is precisely the external product over $S$ used in SH02-MH-PRODUCT. Thus MHPC10 becomes

$$
\begin{aligned}
&R\rho_{j!}\bigl(M_X(F_2,F_1)^a
\boxtimes_S M_Y(G_2,G_1)\bigr)\\
&\qquad\longrightarrow
M_Z\bigl(
R\mathcal Hom(q_X^{-1}F_1,q_Y^{-1}G_2),
R\mathcal Hom(q_X^{-1}F_2,q_Y^{-1}G_1)\bigr).
\end{aligned}
\tag{MHPC11}
$$

This proves the general ordinary-inverse-image comparison with the full stated hypotheses. Neither projection is required to be a submersion, and the two maps to $S$ need not be transverse. In fact MHPC10 needs only the two maps from the common manifold, so the fibre-product result is a specialization of a stronger comparison.

The construction has the ordinary evaluation normalization. The ordinary-product map MHPC5 is induced by precomposition and postcomposition: arrows $A_2\to A_1$, $A_1\to B_2$ and $B_2\to B_1$ compose in that order to $A_2\to B_1$, with the derived tensor symmetry used when factors are grouped. MHPC4 transports this same evaluation through the diagonal adjunction; the counit for $p_2\delta=\mathrm{id}$ removes the inserted relative orientation. MHPC10 transports each outer arrow by the ordinary inverse comparison before performing that evaluation. The base-change and projection formulas in MHPC7 commute with evaluation by their adjunction definitions. Hence the resulting map keeps precomposition on the $F$ input and postcomposition on the $G$ input, including their signs.

Here is the map-level reduction in the ordinary-product case $S=\mathrm{pt}$. Put $U=X\times Y$, $W=U\times U$, and define

$$
\pi:W\longrightarrow U,\qquad
\pi((x,y),(x',y'))=(x,y').
$$

For $A_i=q_X^{-1}F_i$ and $B_i=q_Y^{-1}G_i$, the two product-Hom arguments in MHPC5 are $\pi^{-1}H_i^{\mathrm{orig}}$, where $H_i^{\mathrm{orig}}$ are the arguments of MH23 on $X\times Y$. This identification is canonical: smooth internal-Hom exchange for $\pi$ follows from internal exceptional adjunction and $\pi^!=\pi^{-1}\otimes\omega_\pi$ by cancelling the same invertible relative line.

In the evaluation construction for $W$, the additional $y$ and $x'$ coefficient kernels are those of the constant unit sheaves. Their evaluations are the identity maps of these units. Group the $X$ and $Y$ factors in the same order as in MH23, using the derived tensor symmetry. Evaluating the unit factors leaves exactly the $\pi$-pullback of the original precomposition/postcomposition evaluation on $X\times Y$. Thus the extra coefficient variables contribute no new operation or sign.

For the diagonal restriction, compare the line $L=\omega_{p_2}$ used in MHPC4 with $\omega_\pi$. Their quotient $D=L\otimes\omega_\pi^{-1}$ is invertible. Since $\pi\delta=\mathrm{id}_U$,

$$
\delta^!(\pi^{-1}H_i^{\mathrm{orig}}\otimes L)
\simeq\delta^!(\pi^!H_i^{\mathrm{orig}}\otimes D)
\simeq H_i^{\mathrm{orig}}\otimes\delta^{-1}D.
$$

Both arguments acquire the same line, and MHPC3 cancels it. The alternative identification through $p_2\delta=\mathrm{id}$ identifies that common line on both arguments at once; changing a common line identification acts by conjugation and cancels, rather than multiplying the Hom map by a scalar. The remaining section/projection comparison is the mate of the identity for $\pi\delta=\mathrm{id}$, hence is the identity by the adjunction triangular identity. These are equalities of the evaluated kernel maps before applying their specialization and Fourier functors, so those functors preserve the equality.

On covectors, the images of $q_X$ and $q_Y$ are the complementary subbundles with zero $Y$ and zero $X$ component respectively. Addition identifies their fibre product with $T^*(X\times Y)$. The submersion inverse comparisons identify the transported objects with these zero-component extensions. This identifies the source of the reduced kernel map with the source of MH23. Together with the preceding evaluation and adjunction calculation, it proves that MHPC11 specializes to MH23 with its given normalization.

## SH02-MHPC-EXAMPLE — A projection which is not a submersion

Take $S=Y=\mathbb R$ with $Y\to S$ the identity, and let $X=\{0\}\to S$ be inclusion. Then $Z=\{0\}$, $q_X$ is the identity of a point, and $q_Y=i:\{0\}\hookrightarrow\mathbb R$ is a codimension-one embedding. For $F_1=F_2=k$ the general comparison specializes to the canonical map

$$
R\Gamma_c\bigl(T_0^*\mathbb R;
M_{\mathbb R}(G_2,G_1)|_{T_0^*\mathbb R}\bigr)
\longrightarrow R\operatorname{Hom}_k((G_2)_0,(G_1)_0).
$$

In our construction this is the ordinary inverse microlocal Hom comparison for $i$, followed by composition with the identity on $k$. It is defined for all bounded $G_1,G_2$. It is not asserted to be an isomorphism.

The failed shortcut can be detected independently. On the constant sheaf, $i^!k_{\mathbb R}=k[-1]$ while $i^{-1}k_{\mathbb R}=k$. On the point sheaf, both $i^!k_{\{0\}}$ and $i^{-1}k_{\{0\}}$ are $k$. Thus a single invertible coefficient twist cannot identify $i^!$ with $i^{-1}$ on all inputs. MHPC11 never makes this replacement. It applies the ordinary inverse comparison to $i$ before taking internal Hom on the point.

## SH02-MHPC-PROBLEM — Locate the cancellation

Let $U$ be a nonorientable $n$-manifold. In the proof of MHPC4, identify the relative dualizing object of $p_2:U\times U\to U$ and explain why no orientation local system remains in the final two Hom arguments. Explain also why applying the same cancellation to an arbitrary embedding into a product is not justified.

**Solution.** The relative tangent bundle of $p_2$ is the first tangent factor, so $\omega_{p_2}=p_1^{-1}o_U[n]$. It is invertible even when $o_U$ is not trivial. Tensor both product-Hom arguments by this very object before applying $\delta^!$. Internal exceptional adjunction gives

$$
\delta^!R\mathcal Hom(p_1^{-1}A,p_2^!B)
\simeq R\mathcal Hom(A,(p_2\delta)^!B)
=R\mathcal Hom(A,B).
$$

This is composition of functors and their adjunctions. In local orientation coordinates the relative shifts $n$ and $-n$ and the mutually dual lines cancel, but the global composition identity already supplies that cancellation without choosing those coordinates. For an arbitrary embedding $j:V\hookrightarrow U\times U$, the same calculation yields $R\mathcal Hom((p_1j)^{-1}A,(p_2j)^!B)$. Unless further hypotheses apply to $p_2j$, its exceptional inverse image does not become ordinary inverse image. The proof of MHPC11 avoids this obstacle by using only the diagonal of the common manifold for the internal Hom step.

## SH02-MHPC-ANTECEDENT — What this resolves

Direct exceptional restriction gives an exceptional coefficient target on a general fibre product. It cannot alone produce the ordinary target by cancelling a fixed orientation line: the point-embedding example shows why that replacement fails. The separate-transport construction above obtains the ordinary target without adding a submersion or transversality hypothesis. Its key order is to transport each Hom input to the common manifold first, then use the diagonal there; the exceptional restriction is applied only at that diagonal.

The argument depends on the previously constructed ordinary product, the two single-map inverse comparisons, common-line cancellation, and the stated finite-dimensional operation contracts. It does not depend on the general ordinary target it proves. The ordinary-product specialization is checked by the explicit projection, section, evaluation and adjunction calculation in SH02-MHPC-FIBRE-PRODUCT, with the conormal directions in their displayed order. Every unresolved foundational or Fourier trace-comparison obligation in these inputs remains a separate proof obligation.

**Published sources and proof mechanisms.** The definition behind the two single-map transports is the graph microlocal Hom kernel of Kashiwara and Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Definition 5.5.1 and Proposition 5.5.2, pp. 91–92 (PDF pp. 94–95). Its §§2.3 and 5.5 provide microlocal inverse comparisons and graph identifications with separately stated isomorphism hypotheses; Proposition 2.3.5, p. 48 (PDF p. 51), is an antecedent for keeping the ordinary and exceptional inverse maps distinct. The present construction requires the actual MH19 and MH20 maps and their stated finite-dimensional providers, not an unconditional isomorphism for either inverse comparison.

The internal diagonal step has a precise sheaf-theoretic antecedent in Schapira's [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), Proposition 4.6.5, p. 95, and Proposition 4.6.8, pp. 96–97. The first proof applies tensor–Hom adjunction and the projection formula; the second applies it to the diagonal and cancels the two composite identity maps. MHPC4 uses that mechanism after twisting both Hom arguments by the same invertible relative line. The line cancels by the evaluation-defined MH1, while the diagonal transpose derivative adds the two covectors. No orientation generator or constructibility condition enters this step.

The proper-support product calculation in MHPC7–MHPC9 uses Cartesian base change, the projection formula and composition of proper direct images. Proposition 4.5.6 of the same notes, p. 94, proves the compact-support Künneth formula by that sequence of operations for bounded inputs on locally compact spaces of finite cohomological dimension. Applying the named operation contracts over the common base gives the relative product map used here; ordinary direct-image Künneth is not substituted for it. The antipode is a proper homeomorphism, so that change of cotangent coordinates contributes no exceptional shift. This accounts for the negative first covector and positive addition map simultaneously.

These passages justify comparison with the underlying graph, diagonal and proper-support mechanisms. They do not state the whole separately transported comparison MHPC10 in its displayed arbitrary-map scope, or identify its ordinary-product specialization with MH23. Those are the two additional arguments given here: the separate transports followed by MHPC4, and the projection/section normalization with the auxiliary-variable unit. The proof applies to all bounded coefficient complexes under the stated manifold and finite-global-dimension assumptions, with no perfectness, finite-rank, orientability or transversality restriction.
