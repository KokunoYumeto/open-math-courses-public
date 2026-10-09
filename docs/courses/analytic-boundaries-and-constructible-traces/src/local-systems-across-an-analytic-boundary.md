# Local systems across an analytic boundary

A locally constant complex on the complement of a closed complex analytic set has two constructible extensions. Extension by zero has zero ordinary stalks on the boundary. Ordinary direct image remembers cohomology around that boundary, including monodromy and torsion. Verdier duality connects the two extensions and proves the finiteness of the second without requiring that the open embedding be proper.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

The boundary argument is reconstructed from three explicit ingredients: local constancy of the whole bounded complex, perfect duality on the open manifold, and exceptional adjunction. The order matters: biduality is applied on the open part before ordinary direct image is shown constructible. Use [Complex microlocal stratifications and constructibility](../../sheaf-proof-readings/src/SH03/complex-microlocal-stratifications-and-constructibility.md) for compatible analytic refinements and the geometric constructibility criterion, [Constructible costalks and Verdier duality](../../sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md) for perfect duality and its actual evaluation map, and [Holomorphic operations and complex Fourier symmetries](../../sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md) for bounded internal Hom and its complex geometry. The microlocal submersion theorem and internal exceptional adjunction are used with their stated coefficient, amplitude and support hypotheses.

## The input is locally constant as a complex

Let $k$ be a commutative ring of finite global dimension $g$. Let $X$ be a complex manifold, with the standing finite uniform dimension bound $N$, and let $S\subset X$ be closed complex analytic. Set

\[
 U=X\setminus S,\qquad j:U\hookrightarrow X,\qquad
 F\in D^b_{\mathbb R\text{-c}}(k_U),\qquad
 \operatorname{SS}(F)\subset T_U^*U.
 \tag{1}
\]

Here $T_U^*U$ denotes the zero section. Constructibility includes perfect stalks, with no field or Noetherian assumption. The empty complement, an analytic set containing a whole connected component, and $S=\varnothing$ are permitted.

Apply the [microlocal submersion criterion](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-submersion--exact-pullback-and-local-descent) to the map $U\to\{\mathrm{pt}\}$. Its horizontal cotangent bundle is exactly the zero section. It says that (1) makes the **whole bounded complex** locally isomorphic to a constant complex $P_V$ on a small contractible neighborhood $V\subset U$. The local coefficient object $P$ is perfect because its stalk is a stalk of $F$. In particular, every $H^q(F)$ is locally constant on $U$.

This local conclusion retains the differential and all extension data of $P$. It neither splits $F$ into its cohomology sheaves nor trivializes monodromy around a loop. The analytic-piece cover with the single member $U$ now makes $F$ complex constructible on $U$.

## Extension by zero uses analytic strata and exact stalks

The locally finite analytic cover consisting of $X$ and $S$ has a [compatible complex stratification](../../sheaf-proof-readings/src/SH03/complex-microlocal-stratifications-and-constructibility.md#ordinary-analytic-refinement-with-every-frontier-checked). Compatibility makes each stratum lie entirely in $U$ or entirely in $S$. One may choose a complex μ-refinement and its closed total conormal bound, but ordinary analytic compatibility already proves the cohomology restriction condition below. Singularities and multiple dimensions of $S$ are included in the refinement theorem.

The functor $j_!$ is exact for an open embedding. Its ordinary stalks and cohomology are

\[
 (j_!F)_x\simeq
 \begin{cases}F_x,&x\in U,\\0,&x\in S,\end{cases}
 \qquad
 H^q(j_!F)=j_!H^q(F).
 \tag{2}
\]

On a stratum inside $U$, restriction of the right side is locally constant. On a stratum inside $S$, every stalk is zero, so that restriction is the zero sheaf. The same locally finite analytic stratification works for every degree. Thus $j_!F$ is weakly complex constructible by the analytic-cover criterion. All stalks in (2) are perfect, and exactness preserves the global degree bounds. We have proved

\[
 j_!F\in D^b_{\mathbb C\text{-c}}(k_X).
 \tag{3}
\]

This proof uses exact extension by zero, not a proper direct-image theorem. A zero ordinary stalk at a point of $S$ does not remove that point from the closed support: every neighborhood may still meet nonzero stalks in $U$.

## Internal duality supplies the ordinary direct image

Write $D_M A=R\mathcal Hom_M(A,\omega_M)$. On a complex $n$-dimensional component, the complex orientation canonically identifies $\omega_M$ with $k_M[2n]$. Locally on $U$,

\[
 D_UF|_V\simeq P_V^\vee[2n],
 \qquad P^\vee=R\operatorname{Hom}_k(P,k).
 \tag{4}
\]

The object $P^\vee$ is perfect. It follows that $D_UF$ has locally constant cohomology and perfect stalks. It is globally bounded: if $F\in D^{[a,b]}$, coefficient duality over $k$ gives the sufficient bound

\[
 D_UF\in D^{[-b-2N,\ g-a]}.
 \tag{5}
\]

For a fixed dimension $n$, this improves to $[-b-2n,g-a-2n]$. The uniform bound (5) also covers disconnected manifolds with different component dimensions.

Applying (2)–(3) to $D_UF$ gives a bounded complex constructible object

\[
 E=j_!D_UF.
 \tag{6}
\]

The [bounded internal-Hom theorem](../../sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md#tensor-and-hom-use-full-complex-limiting-sums) makes $D_XE$ weakly complex constructible. Its perfect stalks follow from real constructible Verdier duality, since $E$ is already real constructible. Therefore

\[
 D_XE\in D^b_{\mathbb C\text{-c}}(k_X).
 \tag{7}
\]

Now apply [internal exceptional adjunction](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-internal--internal-adjunction-and-its-tensor-structure) with bounded first input $D_UF$ and second target $\omega_X\in D^+(k_X)$. The composition and open-embedding identifications give $j^!\omega_X=\omega_U$ and the natural isomorphism

\[
 D_X(j_!D_UF)
 \xrightarrow{\sim}
 Rj_*R\mathcal Hom_U(D_UF,\omega_U)
 =Rj_*D_UD_UF.
 \tag{8}
\]

It is an internal sheaf-Hom formula. It is not a formula replacing a Hom stalk by Hom of two ordinary stalks. The derived operations in (8) are defined in $D^+$ before any constructibility of $Rj_*F$ is known. Because the input $F$ is perfect constructible, its [actual evaluation map](../../sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md#the-evaluation-map-is-biduality)

\[
 \eta_F:F\xrightarrow{\sim}D_UD_UF
 \tag{9}
\]

is an isomorphism. Combining $Rj_*\eta_F$ with the inverse of (8) proves the natural comparison

\[
 Rj_*F\xrightarrow{\sim}D_X(j_!D_UF).
 \tag{10}
\]

The right side is already known to be bounded and complex constructible by (7). Hence

\[
 Rj_*F\in D^b_{\mathbb C\text{-c}}(k_X).
 \tag{11}
\]

For clarity, the bounded-Hom contract on a real manifold of dimension at most $2N$ sends inputs in $[a',b']$ and $[c',d']$ to the sufficient range $[c'-b',d'-a'+6N+g+1]$. Apply it to (5)–(6) and $\omega_X\in[-2N,0]$. It gives $D_XE\in[a-g-2N,b+8N+g+1]$. Ordinary direct image is left exact, so (10) further gives the coarse uniform bound $Rj_*F\in[a,b+8N+g+1]$. Sharp local bounds are often much smaller. This numerical estimate exhibits a single global bound; stalkwise boundedness alone would not establish membership in $D^b$.

No biduality on $X$ was used to prove (11). The only biduality input was (9) on the already constructible object $F$ on $U$. We first verified constructibility of $E$, then of its dual, and only then identified that dual with $Rj_*F$. This order avoids assuming the desired output finiteness inside the proof.

Equations (3) and (11) prove both extension conclusions. The analytic set $S$ can be singular, and $j$ can be nonproper. Its special domain, locally constant perfect input and analytic boundary have supplied the constructibility that an unrestricted nonproper image need not have.

## The comparison retains a boundary cone

There is a natural map $\alpha:j_!F\to Rj_*F$. Put $H=j_!F$. Since $j^{-1}H=F$, localization for the closed set $S$ gives

\[
 R\Gamma_SH\longrightarrow H
 \xrightarrow{\alpha}Rj_*F\xrightarrow{+1},
 \qquad
 \operatorname{Cone}(\alpha)\simeq R\Gamma_SH[1].
 \tag{12}
\]

In this formula $R\Gamma_S$ is sheaf cohomology with closed support, not ordinary restriction to $S$. The latter is zero for $H$ by (2), but the supported complex can be nonzero. All objects in (12) are bounded complex constructible: the first follows as the homotopy fibre of a map between the two objects just proved constructible.

At a point $s\in S$, the ordinary direct-image stalk is computed from neighborhoods:

\[
 (Rj_*F)_s\simeq
 \underset{V\ni s}{\operatorname{colim}}\,R\Gamma(V\cap U;F).
 \tag{13}
\]

This is an ordinary image stalk formula with exact filtered colimits, not proper base change for $j$. Boundary topology and its coefficient action remain in (13).

## A puncture measures monodromy by a mapping fibre

Let $X=\Delta$ be a disc in $\mathbb C$, $S=\{0\}$, and $U=\Delta^*$. Choose a positive generator of the fundamental group and a local coefficient perfect complex $P$. Let $T:P\to P$ be the monodromy automorphism, represented by a chain homotopy equivalence when a complex model is chosen. Smaller punctured discs have the same circle cochain calculation, compatibly with restriction. A cut and a base point fix the coefficient identifications. Then

\[
 C(P,T):=(Rj_*F)_0
 \simeq\operatorname{Cone}(T-\mathrm{id}:P\to P)[-1].
 \tag{14}
\]

The [two-arc circle calculation](../../sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-exercise-monodromy--transport-after-one-period) gives (14) by cutting the circle into two contractible arcs. Their intersection has two contractible components. The two restriction identifications are the identity on one component and $T$ on the other. The Mayer–Vietoris differential on $P\oplus P$ consequently has entries $b-a$ and $b-Ta$, up to choices of oriented overlap generators. Eliminate the identity summand by an invertible change of variables. The remaining mapping fibre has differential $T-\mathrm{id}$, up to an invertible sign change. This works for a whole bounded complex and does not require degree-zero coefficients.

The arcs and their intersections are acyclic for a constant coefficient complex: interval evaluation gives the constant-section unit, and the bounded finite complex can be totalized over these finitely many opens. Equivalently, a circle has one vertex and one oriented edge in its local-coefficient cellular model. [Descent along the radial interval](../../sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-cylinder--descent-across-a-contractible-parameter) identifies punctured-disc sections with these circle sections. These finite computations also prove that (14) is perfect: it is a shifted cone of a map between perfect complexes.

For a module $M$ in degree zero, (14) is the two-term complex

\[
 [M\xrightarrow{T-1}M]\quad\text{in degrees }0,1,
 \qquad
 H^0C=\ker(T-1),\quad H^1C=\operatorname{coker}(T-1).
 \tag{15}
\]

For a general $P$, its cohomology satisfies the natural exact sequences

\[
 0\longrightarrow
 \operatorname{coker}\bigl(T-1:H^{q-1}P\to H^{q-1}P\bigr)
 \longrightarrow H^qC(P,T)
 \longrightarrow
 \ker\bigl(T-1:H^qP\to H^qP\bigr)
 \longrightarrow0.
 \tag{16}
\]

Neither (16) nor the constructibility theorem chooses a splitting of these sequences. The mapping fibre in (14) retains their actual extension data.

Dual transport reverses the coefficient map: the positive-loop monodromy on the coefficient dual is $(T^{-1})^\vee$. In complex dimension $n$, Verdier duality then shifts that coefficient by $[2n]$. This inverse and this real-dimensional shift are both needed in (8)–(10).

For constant coefficients $P=k$ and $T=1$, (15) has zero differential, so

\[
 (j_!k_U)_0=0,\qquad
 (Rj_*k_U)_0\simeq k\oplus k[-1],\qquad
 (R\Gamma_{\{0\}}j_!k_U)_0\simeq k[-1]\oplus k[-2].
 \tag{17}
\]

The last equality follows from (12), with the shift $[-1]$ of the ordinary image stalk. For $k\ne0$, zero ordinary boundary stalks coexist with nonzero supported boundary cohomology.

## Solved exercises

### A constant puncture and the duality shift

*Difficulty: Introductory.*

For $j:\Delta^*\hookrightarrow\Delta$, compute the ordinary boundary stalks and the point costalk of $j_!k_{\Delta^*}$. Check the duality formula for $Rj_*k_{\Delta^*}$, retaining the complex dimension. Is the comparison $j_!k_{\Delta^*}\to Rj_*k_{\Delta^*}$ an isomorphism?

**Solution.** The ordinary stalk of the extension by zero at zero is zero. The positive-loop monodromy is the identity, so the boundary stalk of the ordinary image is $k\oplus k[-1]$ by (15). Closed support at the point and the point costalk agree after restricting to that point. Equation (12) gives

\[
 i_0^!j_!k_{\Delta^*}\simeq k[-1]\oplus k[-2].
\]

Its cohomology is in degrees $1,2$, even though its ordinary stalk is zero. The canonical complex orientation gives $D_{\Delta^*}k=k[2]$. Since duality reverses shifts,

\[
 D_\Delta(j_!D_{\Delta^*}k)
 =D_\Delta(j_!k[2])
 =D_\Delta(j_!k)[-2]\simeq Rj_*k.
\]

At zero, the dual of the displayed costalk is $k[1]\oplus k[2]$; shifting by $[-2]$ gives $k[-1]\oplus k$, agreeing with the circle computation. For a nonzero ring $k$, the boundary cone is nonzero, so the comparison is not an isomorphism. On $\Delta^*$ it is the identity. Both extensions are nevertheless complex constructible.

### When a rank-one local system extends cleanly

*Difficulty: Intermediate.*

Let $k$ be a field and let a rank-one local system on $\Delta^*$ have positive-loop monodromy multiplication by $\lambda\in k^*$. Determine when $j_!F\to Rj_*F$ is an isomorphism and compute the monodromy of $D_UF$.

**Solution.** The boundary complex is $[k\xrightarrow{\lambda-1}k]$ in degrees $0,1$. If $\lambda\ne1$, the scalar $\lambda-1$ is invertible, so that complex is acyclic. The comparison is an isomorphism on $U$ and has zero cone stalk at zero; its cone therefore has zero stalks everywhere and is zero. If $\lambda=1$, the boundary has $k$ in degrees $0$ and $1$, and the comparison fails to be an isomorphism.

The dual coefficient transport is multiplication by $\lambda^{-1}$, followed by the dimension shift $[2]$. Thus $D_UF$ is the rank-one system with inverse monodromy, shifted by $2$. A monodromy eigenvalue different from $1$ removes both invariants and coinvariants over a field. Over a general ring, a merely nonzero element $\lambda-1$ need not be a unit; the next exercise gives the difference.

### Integer monodromy leaves torsion

*Difficulty: Intermediate.*

Over $k=\mathbb Z$, take the rank-one local system with monodromy $T=-1$. Compute its ordinary boundary stalk. Repeat the circle calculation after changing the coefficient ring to $\mathbb F_2$, and verify perfection without requiring projective cohomology modules.

**Solution.** The integer circle complex is

\[
 [\mathbb Z\xrightarrow{-2}\mathbb Z]
 \quad\text{in degrees }0,1.
\]

Its degree-zero cohomology is zero because multiplication by $2$ is injective. Its degree-one cohomology is $\mathbb Z/2$, so the complex is isomorphic to $(\mathbb Z/2)[-1]$ in the derived category. The two-term model consists of finite free modules and is perfect. The torsion cohomology module need not itself be projective.

Tensoring this finite free circle model with $\mathbb F_2$ changes the differential to zero. Directly, the coefficient monodromy $-1$ becomes $1$ in that field. The result is $\mathbb F_2\oplus\mathbb F_2[-1]$. This calculation is exact derived coefficient change of the displayed model, not a claim that underived tensor preserves the integer cohomology groups. In particular the new degree-zero group comes from the torsion term in derived tensor. The extension by zero still has zero boundary stalk for both rings, so neither comparison is an isomorphism.

### Whole coefficient complexes and degree bounds

*Difficulty: Advanced.*

Derive (16) from the mapping-fibre triangle. If $P\in D^{[a,b]}$ is perfect, prove that $C(P,T)$ is perfect and lies in $D^{[a,b+1]}$. Compute it for $P=k[2]\oplus k[-3]$ and $T=1$.

**Solution.** The defining triangle is

\[
 C(P,T)\longrightarrow P\xrightarrow{T-1}P
 \longrightarrow C(P,T)[1].
\]

In its cohomology sequence, the map entering $H^qC$ has cokernel of $T-1$ on $H^{q-1}P$, and the map leaving it has image the kernel of $T-1$ on $H^qP$. Exactness gives (16), including its actual extension. For $q<a$ both neighboring cohomology groups vanish. For $q>b+1$ they vanish as well. This proves the stated range. Perfect complexes form a triangulated subcategory, so the shifted cone of this map is perfect. No splitting into cohomology sheaves is needed.

For the specified identity action, the map is zero on the given complex, and the fibre is $P\oplus P[-1]$. Hence

\[
 C(P,1)\simeq k[2]\oplus k[1]\oplus k[-3]\oplus k[-4].
\]

For $k\ne0$, the four nonzero degrees are $-2,-1,3,4$. They verify the interval $[-2,4]$ and show why a circle contributes one cohomological degree above each input degree. The direct sum here comes from this zero map; it does not turn (16) into a chosen splitting for every action.

### An analytic crossing is a singular boundary

*Difficulty: Intermediate.*

In a bidisc $X\subset\mathbb C^2$, set $S=\{zw=0\}$ and $F=k_U$ on $U=X\setminus S$. Compute $(Rj_*F)_s$ at a point on a smooth part of $S$ and at its crossing. Give a compatible analytic stratification and verify the perfect-stalk condition for both extensions.

**Solution.** Near a smooth point of an axis, one coordinate is nonzero and remains in a contractible disc. The other coordinate ranges in a punctured disc. Local neighborhoods in the complement therefore retract to a circle, compatibly with shrinking, and the stalk is $k\oplus k[-1]$.

At the crossing, cofinal product bidiscs meet $U$ in products of two punctured discs. They retract to a torus. The tensor product of its two one-vertex, one-edge circle cochain models has zero differential for constant coefficients, with terms $k,k^2,k$ in degrees $0,1,2$. Consequently

\[
 (Rj_*F)_0\simeq k\oplus k[-1]^{\oplus2}\oplus k[-2].
\]

These are finite free models over every ring in use. The product computation has no additional Tor terms because those models are free. On $U$ the ordinary image is the constant sheaf. Along either punctured axis its two cohomology sheaves are locally constant: product neighborhoods and the fixed normal-coordinate loop identify their circle calculations. The crossing is a point stratum. Thus $U$, the two punctured axes, and the origin give one compatible analytic stratification for all cohomology degrees. Extension by zero restricts to $k$ on $U$ and zero on each boundary stratum, so its stalks are also perfect. This includes the singular point of $S$ without replacing the boundary by a smooth hypersurface. In the duality proof the shift on $U$ is $[4]$, its real dimension, rather than $[2]$.

### Commuting monodromies and a contractible torus complex

*Difficulty: Advanced.*

Keep the crossing, but let a degree-zero local coefficient module $M$ have commuting automorphisms $T_1,T_2$ around the two coordinate loops. Assume $M$ is perfect as a coefficient object. Write the boundary cochain complex at the crossing. If $A=T_1-1$ is invertible, exhibit a contraction. Is invertibility of $A$ necessary for a zero boundary complex?

**Solution.** The finite torus cellular model is

\[
 M\xrightarrow{d^0}M\oplus M\xrightarrow{d^1}M,
 \qquad
 d^0p=(Ap,Bp),\quad d^1(a,b)=-Ba+Ab,
 \quad B=T_2-1.
\]

Commutativity gives $d^1d^0=-BA+AB=0$. The two generators and their product cell fix these signs; reversing an oriented generator changes the corresponding basis consistently. Since the terms are finite sums of the perfect coefficient $M$, the finite complex is perfect. Indeed its finite brutal-truncation filtration has shifted perfect terms as successive quotients, and perfect complexes are closed under the resulting finite triangles. This proof does not need a simultaneous strict lift of the two module actions to a chosen projective resolution.

When $A$ is invertible it commutes with $B$ and with $A^{-1}B$. Set $h^1(a,b)=A^{-1}a$ and $h^2c=(0,A^{-1}c)$. On degree zero, $h^1d^0p=p$. On degree one,

\[
 d^0h^1(a,b)+h^2d^1(a,b)
 =(a,BA^{-1}a)+(0,-A^{-1}Ba+b)=(a,b).
\]

On degree two, $d^1h^2c=c$. Thus $dh+hd=1$ and the complex is contractible. Invertibility of $A$ is sufficient but not necessary: if $B$ is invertible the same argument with the coordinate loops interchanged contracts the complex, even when $A=0$. The smooth part of the first axis has only its normal loop; the crossing calculation must retain both loops. The displayed elementary Koszul differential assumes an actual commuting action on a degree-zero module. A whole derived coefficient action with only homotopy commutation requires its corresponding coherent model, not an unverified replacement by this three-term formula.

### Why the boundary must be complex analytic

*Difficulty: Intermediate.*

Let $X=\mathbb C$ with $z=x+iy$, take $U=\{y>0\}$ and the closed set $S=\{y\leq0\}$, and let $F=k_U$ for $k\ne0$. The input has perfect locally constant coefficients and zero-section microsupport. Determine whether $j_!F$ is complex constructible.

**Solution.** It is real constructible for the upper half-plane, real-axis and lower half-plane stratification. Its boundary microsupport is the outward half-conormal

\[
 \{(x,0;-t\,dy):t\geq0\}.
\]

The sign follows from the open half-line calculation in the normal $y$ coordinate, while the tangential $x$ coordinate has only zero covectors. It can also be read from localization against the closed lower half-plane. Nonzero negative $dy$ covectors occur for the constant nonzero coefficient. Under $\rho(\xi\,dz)=\operatorname{Re}(\xi\,dz)$, the covector $-dy$ corresponds to $i\,dz$. Multiplication by $i$ sends it to $-dz$, which corresponds to a nonzero tangential covector $-dx$. That covector is absent from the microsupport. The microsupport is therefore not complex-conic.

The [complex-conicity criterion](../../sheaf-proof-readings/src/SH03/complex-microlocal-stratifications-and-constructibility.md#four-equivalent-geometric-tests) consequently excludes weak complex constructibility, hence also perfect complex constructibility. All ordinary stalks are still perfect, and $j_!$ is still exact. The missing assumption is that $S$ be complex analytic; these coefficient and exactness properties cannot replace it. In (2)–(3), this example has no compatible complex analytic boundary stratification.

## References

Masaki Kashiwara and Pierre Schapira, *Microlocal study of sheaves*, Astérisque 128 (1985), §1.3.5, pp. 27–28, recalls internal exceptional adjunction with bounded first input and bounded-below target; Example 3.1.3(4), p. 54, gives the open half-space microsupport sign, and Theorem 8.5.2, pp. 151–152, relates weak complex constructibility to complex conicity. [Freely readable PDF](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf). The paper uses the real cotangent normalization $2\operatorname{Re}$; this lesson uses the stated $\operatorname{Re}$ convention. These passages provide antecedents for the comparisons and counterexample. The full coefficient and global boundedness claims above use the named prerequisite proofs.

## What the result establishes

Both analytic-boundary extensions in (3) and (11) are proved bounded and complex constructible for the full standing coefficient ring. The proof retains the actual input evaluation and internal-adjunction comparisons, singular analytic strata, and the closed-support cone of the map between the extensions. The seven solved exercises check monodromy inverses, real-dimensional duality shifts, perfect torsion, whole-complex degree ranges, a singular crossing and the necessity of complex analytic boundary geometry. The proof uses analytic refinement, microlocal submersion, perfect constructible duality and bounded internal Hom at their stated scopes.

## Readable source account and proof scope

Kashiwara and Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), §1.3.5, gives the internal exceptional-adjunction mechanism; Definition 8.2.5, printed 145, distinguishes weak constructibility from perfect stalks; §§8.2–8.3, printed 146–150, treat the geometric criterion and operations; Theorem 8.5.2 gives the complex-conicity criterion. Those passages were checked in the freely readable 1985 edition. The proof here keeps the additional uniform amplitude estimates and the actual evaluation map, supplied by the named programme proofs. In particular, extending the open dual by zero is constructible by an analytic refinement, and dualizing that extension yields ordinary direct image by the written adjunction. Neither finite rank of individual cohomology sheaves alone nor a not-yet-proved ordinary-image theorem is used to justify this step. The punctured-disc and crossing calculations above retain the complete monodromy complexes, including torsion and their degrees.
