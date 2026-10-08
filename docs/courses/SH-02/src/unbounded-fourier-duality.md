# SH02-UFD — Duality when the dual leaves the original transform category

The Fourier–Sato duality of Kashiwara and Schapira (see [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §2.1 and §5.1) is extended here to unbounded complexes. The argument below specifies an unbounded kernel expression before comparing it with a dual. This is necessary even when the original input is bounded below. Public domain (CC0).

## SH02-UFD-DOMAINS — The ambient category for the comparison

Let $k$ be a commutative unital ring of finite global dimension. Let $B$ be locally compact Hausdorff, and let $\tau:E\to B$ be a real vector bundle of fixed finite rank $n$. Its dual projection is $\pi:E^*\to B$. Set

\[
X=E\times_B E^*,\qquad p:X\to E,\qquad q:X\to E^*,
\qquad \rho=\tau p=\pi q,\qquad
N=\{(x,\xi):\langle x,\xi\rangle\leq0\}.
\tag{UFD1}
\]

All categories $D(k_Y)$ in this lesson are classical unbounded derived categories of module sheaves. Internal Hom is a derived sheaf Hom. In particular it is not replaced by tensoring with a coefficient dual. No constructibility, finite generation, field, Noetherian, compact-base or finite-dimensional-base assumption is imposed.

The maps $p,q,\tau,\pi,\rho$ have uniform finite integral proper-support cohomological dimension. The proper-fibre formula reduces their bounds on abelian sheaves to compactly supported cohomology of finite-dimensional real vector spaces: the respective bounds are $n,n,n,n,2n$. This uses the integral dimension and proper-support prerequisites of [SH02-EX-FINITE-RESOLUTION](../../sheaf-proof-readings/SH02-exceptional-operations.html#SH02-EX-FINITE-RESOLUTION); it does not use a finite cohomological dimension for $B$ or for nonproper ordinary direct image. The [unbounded proper-support construction](../../sheaf-proof-readings/SH02-unbounded-range-bridge.html#SH02-UR-PROPER-IMAGE) and its [right adjoint](../../sheaf-proof-readings/SH02-unbounded-range-bridge.html#SH02-UR-EXCEPTIONAL-ADJOINT) therefore apply to these maps.

Define, on all objects of $D(k_E)$,

\[
T_EF=Rq_!(k_N\otimes_k^L p^{-1}F),\qquad
J_EK=Rq_*R\mathcal Hom(k_N,p^!K).
\tag{UFD2}
\]

These expressions are defined without any condition on the bounds of $F$ or $K$. Ordinary direct image on the right is computed by a K-injective replacement; a finite amplitude for that ordinary direct image is not being asserted. On bounded-below conic objects, $T_E$ is the original Fourier transform and $J_E$ is the inverse-transform expression $I_E$ of [SH02-FDN-SETUP](../../sheaf-proof-readings/SH02-fourier-duality-normalization.html#SH02-FDN-SETUP). Thus $J_E$ extends that exact kernel expression to the ambient unbounded category. The notation here does not assert an equivalence on every unbounded nonconic object.

The closed-subset coefficient sheaf $k_N$ is flat, by its stalks. Exact inverse image and the bound for $q_!$ give

\[
T_E D^{[a,b]}(k_E)\subset D^{[a,b+n]}(k_{E^*}),
\tag{UFD3}
\]

where either endpoint may be infinite. In particular $T_E$ retains the bounded-below input range of the original transform. The dual of such an input need not retain that range.

## SH02-UFD-ADJOINTS — Two identities on entire complexes

For a map $f:Y\to Z$ between locally compact Hausdorff spaces with a uniform finite integral proper-support dimension bound, and arbitrary complexes $A,Q\in D(k_Z)$ and $L\in D(k_Y)$, there are natural isomorphisms

\[
f^!R\mathcal Hom(A,Q)
\simeq R\mathcal Hom(f^{-1}A,f^!Q),
\tag{UFD4}
\]

\[
Rf_*R\mathcal Hom(L,f^!Q)
\simeq R\mathcal Hom(Rf_!L,Q).
\tag{UFD5}
\]

The first is the full comparison [SH02-UR-HOM-PULLBACK](../../sheaf-proof-readings/SH02-unbounded-range-bridge.html#SH02-UR-HOM-PULLBACK). To recall its map, transpose evaluation after the trace $Rf_!f^!R\mathcal Hom(A,Q)\to R\mathcal Hom(A,Q)$, using the unbounded projection formula. Testing against any $C\in D(k_Y)$ gives, in order,

\[
\begin{aligned}
\operatorname{Hom}(C,f^!R\mathcal Hom(A,Q))
&\simeq\operatorname{Hom}(Rf_!C\otimes_k^L A,Q)\\
&\simeq\operatorname{Hom}(Rf_!(C\otimes_k^L f^{-1}A),Q)\\
&\simeq\operatorname{Hom}(C,R\mathcal Hom(f^{-1}A,f^!Q)).
\end{aligned}
\tag{UFD6}
\]

Every adjunction is used in the full classical derived category, so an upper bound for $A$ is unnecessary.

For completeness, the second identity follows by testing against $C\in D(k_Z)$:

\[
\begin{aligned}
\operatorname{Hom}(C,Rf_*R\mathcal Hom(L,f^!Q))
&\simeq\operatorname{Hom}(f^{-1}C\otimes_k^L L,f^!Q)\\
&\simeq\operatorname{Hom}(Rf_!(f^{-1}C\otimes_k^L L),Q)\\
&\simeq\operatorname{Hom}(C\otimes_k^L Rf_!L,Q)\\
&\simeq\operatorname{Hom}(C,R\mathcal Hom(Rf_!L,Q)).
\end{aligned}
\tag{UFD7}
\]

Yoneda proves the isomorphism. Its actual map is obtained from the ordinary counit, evaluation and the proper-support trace. More explicitly, with $V=Rf_*R\mathcal Hom(L,f^!Q)$, transpose

\[
V\otimes_k^L Rf_!L
\simeq Rf_!(f^{-1}V\otimes_k^L L)
\longrightarrow Rf_!f^!Q\longrightarrow Q.
\tag{UFD8}
\]

These are the same comparisons as their bounded versions. All tensor permutations are the graded symmetry of complexes, and all internal-Hom totalizations retain their products. Neither proof interchanges Hom with a filtered colimit, or replaces a product with a direct sum.

Composition is specified by the existing bounded comparison [SH02-EX-IMP-COMPOSE](../../sheaf-proof-readings/SH02-exceptional-operations.html#SH02-EX-IMP-COMPOSE) and its extension to whole complexes. Suppose $f$ and $g$ have uniform integral proper-support dimension bounds $r$ and $s$. Bounded composition and these amplitude bounds give a bound $r+s$ for $(fg)_!$ on abelian sheaves. If $I$ is an injective coefficient sheaf on the domain of $g$, bounded composition gives $Rf_!(g_!I)\simeq R(fg)_!I$: the injective sheaf computes $Rg_!I=g_!I$, and the right side is concentrated in degree zero. Therefore $g_!I$ is $f_!$-acyclic.

For an arbitrary complex choose a K-injective representative $I^\bullet$ with injective terms. Tag 07K7 computes $Rg_!$ and $R(fg)_!$ by applying their underived functors to $I^\bullet$, because their dimensions are finite. It also computes $Rf_!$ on the complex $g_!I^\bullet$, whose terms were just proved $f_!$-acyclic. Underived canonical composition $f_!g_!=(fg)_!$ thus supplies the unbounded comparison $Rf_!Rg_!\simeq R(fg)_!$. This is the bounded comparison on bounded-below inputs, and associativity is the underived composition associativity through these same acyclic models. The right-adjoint comparison $g^!f^!\simeq(fg)^!$ is defined by transposing the composite proper-support trace. Uniqueness with that trace fixes its coherence; no unspecified softness assertion or arbitrary isomorphism between endpoints is used.

## SH02-UFD-RELATIVE — A dual with an arbitrary base test object

For $H\in D(k_B)$ put

\[
\mathbb D_{E,H}F=R\mathcal Hom(F,\tau^!H),\qquad
\mathbb D_{E^*,H}G=R\mathcal Hom(G,\pi^!H).
\tag{UFD9}
\]

**Theorem.** For every $F\in D(k_E)$ and $H\in D(k_B)$ there is a natural isomorphism

\[
J_E\mathbb D_{E,H}F
\xrightarrow{\sim}\mathbb D_{E^*,H}(T_EF).
\tag{UFD10}
\]

It is contravariant in $F$, covariant in $H$, and compatible with open restriction on $B$. No conicity is needed for this identity of kernel expressions.

**Proof.** The specified exceptional composition comparisons give

\[
p^!\tau^!H\simeq\rho^!H\simeq q^!\pi^!H.
\tag{UFD11}
\]

Apply UFD4 to $p$, then UFD11, then currying for internal Hom, and finally UFD5 for $q$:

\[
\begin{aligned}
J_E\mathbb D_{E,H}F
&=Rq_*R\mathcal Hom(k_N,p^!R\mathcal Hom(F,\tau^!H))\\
&\simeq Rq_*R\mathcal Hom(k_N,R\mathcal Hom(p^{-1}F,p^!\tau^!H))\\
&\simeq Rq_*R\mathcal Hom(k_N,R\mathcal Hom(p^{-1}F,q^!\pi^!H))\\
&\simeq Rq_*R\mathcal Hom(k_N\otimes_k^L p^{-1}F,q^!\pi^!H)\\
&\simeq R\mathcal Hom(Rq_!(k_N\otimes_k^L p^{-1}F),\pi^!H).
\end{aligned}
\tag{UFD12}
\]

This composite is the displayed map. UFD8 specifies its last arrow, and UFD6 specifies its first comparison; the intermediate currying retains the order $k_N,p^{-1}F$. Naturality gives both variance assertions. Open restriction is exact and commutes with the proper-support functors, ordinary direct images in an open base-change square, internal Hom and their adjunction comparisons. The composite therefore restricts to the same composite for the restricted bundle. All intermediate objects exist on the full derived categories by UFD1–UFD8. $\square$

## SH02-UFD-COEFFICIENT — The coefficient dual on the full source input range

Let $O$ be the orientation sign local system of $E$ on $B$, and use the positive dual-basis identification with the orientation system of $E^*$. Its self-pairing is $O\otimes_k O\simeq k_B$. Put $W^{-1}=O[-n]$.

Only the bounded-input vector-bundle dualizing formula is needed at this step. Applied to the bounded complex $W^{-1}$, it gives

\[
\tau^!W^{-1}\simeq k_E,\qquad \pi^!W^{-1}\simeq k_{E^*}.
\tag{UFD13}
\]

These are exactly the orientation evaluation maps in [SH02-FDN-DUALITIES](../../sheaf-proof-readings/SH02-fourier-duality-normalization.html#SH02-FDN-DUALITIES). We do not extend a vector-bundle dualizing formula to an arbitrary unbounded argument by an unproved continuity assertion.

Define $D'_EF=R\mathcal Hom(F,k_E)$, on all of $D(k_E)$, and similarly on $E^*$. Taking $H=W^{-1}$ in UFD10 gives

\[
J_E(D'_EF)\xrightarrow{\sim}D'_{E^*}(T_EF)
\qquad(F\in D(k_E)).
\tag{UFD14}
\]

In particular this proves the coefficient-dual formula for every bounded-below conic input, with the inverse-transform expression on the left evaluated in its explicitly defined unbounded extension. The arbitrary locally compact Hausdorff base is retained. This is the needed interpretation when the dual leaves the original bounded-below transform domain; it is not a claim that this dual is bounded below.

## SH02-UFD-ABSOLUTE — The absolute dual and its ambient hypothesis

For absolute duality additionally assume that the compact-support functor on $B$ has uniformly finite integral cohomological dimension, equivalently the finite c-soft-dimension hypothesis used by the dualizing formalism. Put $a_B:B\to\{*\}$ and $\omega_B=a_B^!k$. The corresponding bound for $E$ and $E^*$ is at most the base bound plus $n$, by proper-support composition and the fibre bounds. Thus $a_E^!$ and $a_{E^*}^!$ exist by the same unbounded construction. Composition gives

\[
\omega_E=a_E^!k\simeq\tau^!\omega_B,
\qquad \omega_{E^*}\simeq\pi^!\omega_B.
\tag{UFD15}
\]

Conversely, a uniform compact-support bound on $E$ gives the base bound: exact direct image along the closed zero section $i$ satisfies $R\Gamma_c(B;A)=R\Gamma_c(E;i_*A)$ for every abelian sheaf $A$. Thus stating the absolute-duality hypothesis on $B$ preserves the source's finite-dimensional-duality domain on the total space.

For $D_EF=R\mathcal Hom(F,\omega_E)$, UFD10 with $H=\omega_B$ and UFD15 gives

\[
J_E(D_EF)\xrightarrow{\sim}D_{E^*}(T_EF)
\qquad(F\in D(k_E)).
\tag{UFD16}
\]

This includes every bounded-below conic input of the absolute-duality statement with its ambient dualizing hypothesis. No biduality isomorphism or perfectness of $F$ enters.

## SH02-UFD-RANGE-CHECK — Why extending the kernel expression matters

**Problem.** Take $B=E=E^*=\{*\}$, $k$ a field, and $F=\bigoplus_{m\geq0}k[-m]$. Compute UFD14, and determine whether its left input lies in the original bounded-below transform domain.

**Solution.** In rank zero all projections are identities, $N$ is the point, and both $T_E$ and $J_E$ are the identity functor. The complex $F$ has $k$ in every nonnegative degree. Hence

\[
D'F=R\operatorname{Hom}_k(F,k)=\prod_{m\geq0}k[m]
\tag{UFD17}
\]

has a nonzero group in every nonpositive degree. Its terms and differential follow by applying the Hom-complex formula to the displayed direct-sum complex; all vector spaces are projective. Thus $D'F$ is not bounded below. UFD14 is the identity on this perfectly well-defined unbounded complex. The calculation shows a domain problem with reading the original bounded-below inverse-transform notation literally, not a failure of the duality identity after the stated extension.

**Problem.** Identify the precise additional conclusions which cannot be extracted merely from UFD12.

**Solution.** UFD12 compares the displayed kernel expressions. It does not show that all unbounded objects are conic, that either expression defines an inverse equivalence on a larger conic category, or that a chosen opposite-halfspace adjunction agrees with the original one. The prescribed paired inverse identities FDN18–FDN19 are proved separately in [SH02-NDF-SOURCE-MAPS](../../sheaf-proof-readings/SH02-fourier-literal-normalization.html#SH02-NDF-SOURCE-MAPS), and the Fourier trace identity FTC14 in [SH02-FTE-TRACE](../../sheaf-proof-readings/SH02-fourier-transpose-endpoint.html#SH02-FTE-TRACE). Neither result is used in UFD14 or UFD16.

The stronger unbounded identities and this explicit interpretation of the printed input range supply the mathematical range witness.
