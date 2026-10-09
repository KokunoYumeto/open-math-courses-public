# Analytic boundaries and constructible traces

Two lessons explain extensions of local systems across singular analytic boundaries and construct the supported trace class of a constructible complex. Thirteen exercises have complete solutions.

- [Local systems across an analytic boundary](local-systems-across-an-analytic-boundary.html) · [editable source](src/local-systems-across-an-analytic-boundary.md)
- [Constructible traces and local Euler indices](constructible-traces-and-local-euler-indices.html) · [editable source](src/constructible-traces-and-local-euler-indices.md)

The analytic-boundary theorem allows every commutative coefficient ring of finite global dimension, with nonzero coefficients specified in nonvanishing examples. The Euler-index and trace lesson uses a characteristic-zero field and retains its orientation, shift, boundedness and closed-support hypotheses. The geometric, perfect-duality and sheaf-operation prerequisites remain at their stated scopes.

The exact normalized maps are in these earlier lessons:

- [Product evaluation with a cohomologically constructible factor](providers/SH02-CB.html#SH02-CB-EXTERNAL-HOM)
- [Exceptional inverse image of internal Hom](providers/SH02-EX.html#SH02-EX-HOM) and [exceptional composition](providers/SH02-EX.html#SH02-EX-COMPOSITION)

Download the readings, sources and build code · [Reuse terms](LICENSE.txt) · Provenance

[Further sheaf proof readings](../sheaf-proof-readings/index.html) include the linked constructibility and microlocal prerequisites with editable sources.

---

# Local systems across an analytic boundary

A locally constant complex on the complement of a closed complex analytic set has two constructible extensions. Extension by zero has zero ordinary stalks on the boundary. Ordinary direct image remembers cohomology around that boundary, including monodromy and torsion. Verdier duality connects the two extensions and proves the finiteness of the second without requiring that the open embedding be proper.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

The boundary argument is reconstructed from three explicit ingredients: local constancy of the whole bounded complex, perfect duality on the open manifold, and exceptional adjunction. The order matters: biduality is applied on the open part before ordinary direct image is shown constructible. Use [Complex microlocal stratifications and constructibility](../sheaf-proof-readings/src/SH03/complex-microlocal-stratifications-and-constructibility.md) for compatible analytic refinements and the geometric constructibility criterion, [Constructible costalks and Verdier duality](../sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md) for perfect duality and its actual evaluation map, and [Holomorphic operations and complex Fourier symmetries](../sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md) for bounded internal Hom and its complex geometry. The microlocal submersion theorem and internal exceptional adjunction are used with their stated coefficient, amplitude and support hypotheses.

## The input is locally constant as a complex

Let $k$ be a commutative ring of finite global dimension $g$. Let $X$ be a complex manifold, with the standing finite uniform dimension bound $N$, and let $S\subset X$ be closed complex analytic. Set

\[
 U=X\setminus S,\qquad j:U\hookrightarrow X,\qquad
 F\in D^b_{\mathbb R\text{-c}}(k_U),\qquad
 \operatorname{SS}(F)\subset T_U^*U.
 \tag{1}
\]

Here $T_U^*U$ denotes the zero section. Constructibility includes perfect stalks, with no field or Noetherian assumption. The empty complement, an analytic set containing a whole connected component, and $S=\varnothing$ are permitted.

Apply the [microlocal submersion criterion](../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-submersion--exact-pullback-and-local-descent) to the map $U\to\{\mathrm{pt}\}$. Its horizontal cotangent bundle is exactly the zero section. It says that (1) makes the **whole bounded complex** locally isomorphic to a constant complex $P_V$ on a small contractible neighborhood $V\subset U$. The local coefficient object $P$ is perfect because its stalk is a stalk of $F$. In particular, every $H^q(F)$ is locally constant on $U$.

This local conclusion retains the differential and all extension data of $P$. It neither splits $F$ into its cohomology sheaves nor trivializes monodromy around a loop. The analytic-piece cover with the single member $U$ now makes $F$ complex constructible on $U$.

## Extension by zero uses analytic strata and exact stalks

The locally finite analytic cover consisting of $X$ and $S$ has a [compatible complex stratification](../sheaf-proof-readings/src/SH03/complex-microlocal-stratifications-and-constructibility.md#ordinary-analytic-refinement-with-every-frontier-checked). Compatibility makes each stratum lie entirely in $U$ or entirely in $S$. One may choose a complex μ-refinement and its closed total conormal bound, but ordinary analytic compatibility already proves the cohomology restriction condition below. Singularities and multiple dimensions of $S$ are included in the refinement theorem.

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

The [bounded internal-Hom theorem](../sheaf-proof-readings/src/SH03/holomorphic-operations-and-complex-fourier-symmetries.md#tensor-and-hom-use-full-complex-limiting-sums) makes $D_XE$ weakly complex constructible. Its perfect stalks follow from real constructible Verdier duality, since $E$ is already real constructible. Therefore

\[
 D_XE\in D^b_{\mathbb C\text{-c}}(k_X).
 \tag{7}
\]

Now apply [internal exceptional adjunction](../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-internal--internal-adjunction-and-its-tensor-structure) with bounded first input $D_UF$ and second target $\omega_X\in D^+(k_X)$. The composition and open-embedding identifications give $j^!\omega_X=\omega_U$ and the natural isomorphism

\[
 D_X(j_!D_UF)
 \xrightarrow{\sim}
 Rj_*R\mathcal Hom_U(D_UF,\omega_U)
 =Rj_*D_UD_UF.
 \tag{8}
\]

It is an internal sheaf-Hom formula. It is not a formula replacing a Hom stalk by Hom of two ordinary stalks. The derived operations in (8) are defined in $D^+$ before any constructibility of $Rj_*F$ is known. Because the input $F$ is perfect constructible, its [actual evaluation map](../sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md#the-evaluation-map-is-biduality)

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

For clarity, the [bounded-Hom contract](../sheaf-proof-readings/src/SH02/manifold-duality.md#sh02-md-bounded-hom--boundedness-for-arbitrary-bounded-inputs) on a real manifold of dimension at most $2N$ sends inputs in $[a',b']$ and $[c',d']$ to the sufficient range $[c'-b',d'-a'+6N+g+1]$. Apply it to (5)–(6) and $\omega_X\in[-2N,0]$. It gives $D_XE\in[a-g-2N,b+8N+g+1]$. Ordinary direct image is left exact, so (10) further gives the coarse uniform bound $Rj_*F\in[a,b+8N+g+1]$. Sharp local bounds are often much smaller. This numerical estimate exhibits a single global bound; stalkwise boundedness alone would not establish membership in $D^b$.

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

The [two-arc circle calculation](../sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-exercise-monodromy--transport-after-one-period) gives (14) by cutting the circle into two contractible arcs. Their intersection has two contractible components. The two restriction identifications are the identity on one component and $T$ on the other. The Mayer–Vietoris differential on $P\oplus P$ consequently has entries $b-a$ and $b-Ta$, up to choices of oriented overlap generators. Eliminate the identity summand by an invertible change of variables. The remaining mapping fibre has differential $T-\mathrm{id}$, up to an invertible sign change. This works for a whole bounded complex and does not require degree-zero coefficients.

The arcs and their intersections are acyclic for a constant coefficient complex: [interval evaluation](../sheaf-proof-readings/src/SH02/convex-acyclicity.md#sh02-ca-local-system--locally-constant-coefficients-and-evaluation) gives the constant-section unit, and the bounded finite complex can be totalized over these finitely many opens. Equivalently, a circle has one vertex and one oriented edge in its local-coefficient cellular model. [Descent along the radial interval](../sheaf-proof-readings/src/SH02/conic-descent.md#sh02-con-cylinder--descent-across-a-contractible-parameter) identifies punctured-disc sections with these circle sections. These finite computations also prove that (14) is perfect: it is a shifted cone of a map between perfect complexes.

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

The [complex-conicity criterion](../sheaf-proof-readings/src/SH03/complex-microlocal-stratifications-and-constructibility.md#four-equivalent-geometric-tests) consequently excludes weak complex constructibility, hence also perfect complex constructibility. All ordinary stalks are still perfect, and $j_!$ is still exact. The missing assumption is that $S$ be complex analytic; these coefficient and exactness properties cannot replace it. In (2)–(3), this example has no compatible complex analytic boundary stratification.

## References

Masaki Kashiwara and Pierre Schapira, *Microlocal study of sheaves*, Astérisque 128 (1985), §1.3.5, pp. 27–28, recalls internal exceptional adjunction with bounded first input and bounded-below target; Example 3.1.3(4), p. 54, gives the open half-space microsupport sign, and Theorem 8.5.2, pp. 151–152, relates weak complex constructibility to complex conicity. [Freely readable PDF](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf). The paper uses the real cotangent normalization $2\operatorname{Re}$; this lesson uses the stated $\operatorname{Re}$ convention. These passages provide antecedents for the comparisons and counterexample. The full coefficient and global boundedness claims above use the named prerequisite proofs.

## What the result establishes

Both analytic-boundary extensions in (3) and (11) are proved bounded and complex constructible for the full standing coefficient ring. The proof retains the actual input evaluation and internal-adjunction comparisons, singular analytic strata, and the closed-support cone of the map between the extensions. The seven solved exercises check monodromy inverses, real-dimensional duality shifts, perfect torsion, whole-complex degree ranges, a singular crossing and the necessity of complex analytic boundary geometry. The proof uses analytic refinement, microlocal submersion, perfect constructible duality and bounded internal Hom at their stated scopes.

## Readable source account and proof scope

Kashiwara and Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), §1.3.5, gives the internal exceptional-adjunction mechanism; Definition 8.2.5, printed 145, distinguishes weak constructibility from perfect stalks; §§8.2–8.3, printed 146–150, treat the geometric criterion and operations; Theorem 8.5.2 gives the complex-conicity criterion. Those passages were checked in the freely readable 1985 edition. The proof here keeps the additional uniform amplitude estimates and the actual evaluation map, supplied by the named programme proofs. In particular, extending the open dual by zero is constructible by an analytic refinement, and dualizing that extension yields ordinary direct image by the written adjunction. Neither finite rank of individual cohomology sheaves alone nor a not-yet-proved ordinary-image theorem is used to justify this step. The punctured-disc and crossing calculations above retain the complete monodromy complexes, including torsion and their degrees.

---

# Constructible traces and local Euler indices

An Euler index is a signed count of finite cohomology groups. To connect that count to geometry, we turn the identity of a constructible complex into a class with values in the dualizing complex. The diagonal supplies the comparison between an endomorphism and an evaluated tensor. Its exceptional restriction, ordinary restriction and comparison map must all remain visible: they measure different kinds of information.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

The supported trace below is defined by its actual maps: product evaluation, exceptional restriction to the diagonal, the closed-embedding counit, graded interchange and evaluation. Its normalization is checked directly at a point by the chain-level supertrace. Use [Constructible costalks and Verdier duality](../sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md#perfect-stalks-give-perfect-costalks) for the actual local dual pairings and perfection, [Perfect coefficients on compact fibres](../sheaf-proof-readings/src/SH03/perfect-coefficients-on-compact-fibres.md#finite-descent-on-a-compact-triangulation) for finiteness on compact subanalytic sets, and [Perfect operations and finite microlocal coefficients](../sheaf-proof-readings/src/SH03/perfect-operations-and-finite-microlocal-coefficients.md#perfect-inverse-images-tensors-and-internal-hom) for bounded tensor and internal Hom. The normalized maps come from [the product evaluation theorem, SH02-CB-EXTERNAL-HOM](../sheaf-proof-readings/src/SH02/cohomological-biduality.md#sh02-cb-external-hom--a-constructible-factor-in-a-product), [exceptional inverse image of internal Hom, SH02-EX-HOM](../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-hom--exceptional-inverse-image-of-internal-hom), and [exceptional composition, SH02-EX-COMPOSITION](../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-composition--composition-restriction-and-change-of-base), with their stated hypotheses. The present construction uses their formal neighborhood systems, proper-support soft, fibre and composition results, and derived resolution and duality prerequisites. Proper trace transport, the global index theorem and characteristic cycles require the further arguments described below.

## Two finite local measurements

Throughout this lesson, $k$ is a commutative field of characteristic zero. Let $X$ be a real analytic manifold with the standing finite uniform dimension bound, and let

\[
 F\in D^b_{\mathbb R\text{-c}}(k_X).
 \tag{1}
\]

Constructibility in (1) includes perfect stalks. The characteristic-zero field hypothesis makes the point supertrace determine an integer Euler index. No statement here extends the global trace or cycle construction to an arbitrary coefficient ring.

For a bounded complex $P$ with finite-dimensional cohomology, define

\[
 \chi(P)=\sum_q(-1)^q\dim_k H^q(P)\in\mathbb Z.
 \tag{2}
\]

The sum is finite. Over a field, such a complex is perfect. A bounded finite-dimensional representative is therefore available for calculations, although replacing a complex by a representative does not change its morphisms in the derived category.

For the point inclusion $i_x:\{x\}\hookrightarrow X$, write

\[
 A_x(F)=i_x^{-1}F=F_x,\qquad
 C_x(F)=i_x^!F\simeq R\Gamma_{\{x\}}(X;F).
 \tag{3}
\]

The second expression is **cohomology supported at the point**, equivalently the point costalk. The compact-support symbol in the notation below does not replace it with the global complex $R\Gamma_c(X;F)$.

Both complexes in (3) are perfect by the constructible-costalk theorem. We can consequently form the integer-valued functions

\[
 \chi(F)(x)=\chi(A_x(F)),\qquad
 \chi_c(F)(x)=\chi(C_x(F)).
 \tag{4}
\]

The [local dual pairing](../sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md#duality-exchanges-the-measurements-before-biduality) identifies

\[
 (D_XF)_x\simeq R\operatorname{Hom}_k(C_x(F),k),\qquad
 D_XF=R\mathcal Hom(F,\omega_X).
 \tag{5}
\]

For a finite coefficient complex $P$, duality sends $H^q(P)$ to its vector-space dual in degree $-q$. Thus $\chi(P^\vee)=\chi(P)$: the signs $(-1)^{-q}$ and $(-1)^q$ agree. Equation (5) proves the dual-sections identity

\[
 \chi_c(F)=\chi(D_XF).
 \tag{6}
\]

This proof uses the actual costalk–dual-stalk comparison. It does not identify a costalk with a stalk. Since $F$ and $D_XF$ are constructible, choose a common locally finite subanalytic stratification for their cohomology sheaves. On each stratum all their cohomology ranks are locally constant. Boundedness makes (4) finite sums of those ranks, so both functions are constructible.

On an $n$-dimensional component, the manifold normalization is

\[
 \omega_X=\operatorname{or}_X[n].
 \tag{7}
\]

For the constant sheaf $k_X$, the [coordinate-ball support calculation](../sheaf-proof-readings/src/SH02/manifold-duality.md#sh02-md-euclidean--the-compact-support-generator) gives $A_x(k_X)=k$ and $C_x(k_X)=\operatorname{or}_{X,x}[-n]$. Hence its ordinary local index is $1$, while its costalk index is $(-1)^n$. No global orientation is needed to count the dimension of the orientation line.

## Global indices require a separate finiteness check

Define

\[
 \chi(X;F)=\chi(R\Gamma(X;F)),\qquad
 \chi_c(X;F)=\chi(R\Gamma_c(X;F))
 \tag{8}
\]

only when the corresponding complex has bounded finite-dimensional cohomology. Local constructibility alone does not supply this global condition on a noncompact space.

For example, take $X$ to be a countable discrete manifold and $F=k_X$. Every stalk and costalk is the finite complex $k$, and both local functions in (4) are $1$. Nevertheless,

\[
 \Gamma(X;F)=\prod_{m\geq1}k,\qquad
 \Gamma_c(X;F)=\bigoplus_{m\geq1}k
\]

are infinite-dimensional. Neither global index in (8) is defined by (2).

If $F$ has compact **closed support**, both global complexes are perfect by compact constructible finiteness. Here closed support means the complement of the largest open set on which $F$ vanishes; it is the closure of the set of points with a nonzero cohomology stalk. In particular, extension by zero from an open interval has the closed interval as its closed support, even though its endpoint stalks vanish.

The support is a compact subanalytic set. Restricting to it and using the closed-embedding equivalence reduces ordinary sections to the compact-set finiteness theorem. The same theorem applies to compact sections, and the canonical map

\[
 R\Gamma_c(X;F)\longrightarrow R\Gamma(X;F)
 \tag{9}
\]

is an isomorphism because the complex is supported on that compact set. Indeed, for its closed inclusion $i:Z\hookrightarrow X$, the ordinary localization equivalence gives $F\simeq i_*i^{-1}F$. The embedding is proper, so composition identifies the two sides of (9) with $R\Gamma_c(Z;i^{-1}F)$ and $R\Gamma(Z;i^{-1}F)$. These section functors agree on the compact space $Z$, and their comparison is the identity. Consequently $\chi_c(X;F)=\chi(X;F)$ in this case. Relating this integer to the geometric characteristic class requires the proper trace compatibility proved in the next stage.

## The identity and the evaluated tensor

The internal Hom adjunction gives

\[
 \operatorname{Hom}(F,F)
 \simeq\operatorname{Hom}(k_X,R\mathcal Hom(F,F)).
\]

Let $e_F:k_X\to R\mathcal Hom(F,F)$ be the morphism corresponding to $\mathrm{id}_F$. Let $\mathrm{ev}_F:D_XF\otimes^L F\to\omega_X$ be evaluation. We define the contraction with the following explicit graded order as

\[
 t_F:F\otimes^LD_XF
 \xrightarrow{\,\tau\,}D_XF\otimes^LF
 \xrightarrow{\,\mathrm{ev}_F\,}\omega_X.
 \tag{10}
\]

The symmetry $\tau$ is the graded symmetry: homogeneous elements of degrees $a,b$ acquire $(-1)^{ab}$ when interchanged. This sign is part of (10).

Let $q_1,q_2:X\times X\to X$ be the projections, and let $\delta:X\to X\times X$ be the closed diagonal. Put

\[
 K_F=F\boxtimes^LD_XF.
\]

[The product evaluation theorem, SH02-CB-EXTERNAL-HOM](../sheaf-proof-readings/src/SH02/cohomological-biduality.md#sh02-cb-external-hom--a-constructible-factor-in-a-product), applied with the cohomologically constructible factor on the second copy of $X$, gives the canonical isomorphism

\[
 K_F\xrightarrow{\sim}
 R\mathcal Hom(q_2^{-1}F,q_1^!F).
 \tag{11}
\]

It includes the graded permutation placing the first factor $F$ before the second factor $D_XF$. This is the evaluation map of that theorem with its actual normalization. Constructibility and the perfect local section representatives establish its invertibility; an abstract isomorphism of its source and target would not suffice for the trace construction.

Apply exceptional restriction along $\delta$. [The exceptional-Hom comparison, SH02-EX-HOM](../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-hom--exceptional-inverse-image-of-internal-hom), is an isomorphism for a bounded first Hom input and a bounded-below second input. Here $q_2^{-1}F$ is bounded and $q_1^!F$ is bounded below; the finite manifold dimension makes the exceptional functors available. It gives

\[
 \begin{aligned}
 \delta^!K_F
 &\simeq\delta^!R\mathcal Hom(q_2^{-1}F,q_1^!F)\\
 &\simeq R\mathcal Hom(\delta^{-1}q_2^{-1}F,\delta^!q_1^!F)\\
 &\simeq R\mathcal Hom(F,F).
 \end{aligned}
 \tag{12}
\]

The last step uses $q_2\delta=\mathrm{id}_X$ and [the normalized exceptional composition, SH02-EX-COMPOSITION](../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-composition--composition-restriction-and-change-of-base), for $q_1\delta=\mathrm{id}_X$. Denote the inverse of (12) by

\[
 \theta_F:R\mathcal Hom(F,F)\xrightarrow{\sim}\delta^!K_F.
 \tag{13}
\]

There is no unexplained dimension shift in (12): the exceptional composition has already accounted for the relative dualizing factor in $q_1^!$. We keep $\delta^!$ until the next map.

## From exceptional to ordinary restriction along a closed embedding

For any closed embedding $i:Z\hookrightarrow W$, proper and ordinary direct image agree, and ordinary restriction satisfies $i^{-1}i_*\simeq\mathrm{id}$. Apply $i^{-1}$ to the exceptional counit:

\[
 i_*i^!A\xrightarrow{\epsilon_A}A.
\]

This defines a natural comparison

\[
 \beta_{i,A}:i^!A
 \simeq i^{-1}i_*i^!A
 \xrightarrow{\,i^{-1}\epsilon_A\,}i^{-1}A.
 \tag{14}
\]

Its adjunction characterization also gives uniqueness. Compose a candidate $b:i^!A\to i^{-1}A$ with the ordinary unit $A\to i_*i^{-1}A$ and the exceptional counit. Requiring

\[
 i_*b: i_*i^!A\longrightarrow i_*i^{-1}A
 \quad=\quad
 \bigl(i_*i^!A\xrightarrow{\epsilon_A}A
          \longrightarrow i_*i^{-1}A\bigr)
 \tag{15}
\]

forces $b$ to be (14), because $i_*$ is fully faithful. Applying $i^{-1}$ to the right side of (15) recovers exactly (14): the ordinary unit restricts to the identity. This is the unit–counit characterization of the closed-diagonal comparison used here.

For $i=\delta$, ordinary restriction gives $\delta^{-1}K_F\simeq F\otimes^LD_XF$. The complete evaluated endomorphism map is therefore

\[
 R\mathcal Hom(F,F)
 \xrightarrow{\theta_F}\delta^!K_F
 \xrightarrow{\beta_{\delta,K_F}}\delta^{-1}K_F
 \simeq F\otimes^LD_XF
 \xrightarrow{t_F}\omega_X.
 \tag{16}
\]

The comparison (14) is generally not an isomorphism. For example, if $i$ includes a point in a positive-dimensional manifold and $A=k_W$, its two restrictions are $\operatorname{or}_{W,x}[-n]$ and $k$. Their degrees differ. Replacing $i^!$ by $i^{-1}$ would erase precisely the local support information retained in (16).

## The characteristic class has closed support

Set $Z=\operatorname{supp}(F)$, with the closed-support convention above, and abbreviate $E_F=R\mathcal Hom(F,F)$. Outside $Z$ the restriction of $F$ is zero, so $E_F$ is zero there as well. Thus $E_F$ is supported on $Z$.

If $i:Z\hookrightarrow X$ is the closed embedding, [closed-support localization](../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-embedding--open-closed-and-locally-closed-inclusions) gives $R\Gamma_ZA=i_*i^!A$ and an isomorphism

\[
 R\Gamma_ZE_F\xrightarrow{\sim}E_F.
 \tag{17}
\]

Indeed the complementary open restriction of $E_F$ vanishes, so its localization triangle has zero open term. For any map $v:E_F\to\omega_X$, apply $R\Gamma_Z$ to $v$ and use the inverse of (17). This gives its unique supported lift

\[
 E_F\longrightarrow R\Gamma_Z\omega_X.
 \tag{18}
\]

Uniqueness follows from the adjunction between the inclusion of complexes supported on $Z$ and $R\Gamma_Z$. It is the **supported source $E_F$** that gives this uniqueness. A map from $k_X$ whose open restriction happens to vanish would not by itself justify a unique lift.

Use (16) for $v$ in (18), then precompose with $e_F$. The image of the global unit is

\[
 C(F)\in H_Z^0(X;\omega_X),\qquad
 k_X\xrightarrow{e_F}E_F
 \longrightarrow R\Gamma_Z\omega_X.
 \tag{19}
\]

Here $H_Z^0(X;\omega_X)=H^0R\Gamma(X;R\Gamma_Z\omega_X)$. Formula (19) defines the supported trace class used in this lesson. If $Z\subset S$ with $S$ closed, the inclusion of support conditions gives a natural map $R\Gamma_Z\omega_X\to R\Gamma_S\omega_X$. The image of (19) is the class with support condition $S$.

All maps are natural under an isomorphism of $F$ in the derived category: its identity conjugates to the new identity, evaluation pairs the conjugate morphisms, and the diagonal comparisons are natural. This proves that (19) depends on the derived object, not on a chosen representative. They are also compatible with open restriction, since the exceptional comparisons, closed-diagonal counit and supported localization all restrict to their counterparts on an open subset.

On a positive-dimensional manifold, $C(F)$ has values in a dualizing complex. It is not obtained by placing the stalk numbers $\chi(F)(x)$ in degree-zero constant coefficients. Relating constructible functions to these geometric classes is a later theorem.

## A point fixes the trace sign

Take $X=\{\mathrm{pt}\}$. Its dualizing complex is $k$, both diagonal restrictions are the identity, and $\beta$ is the identity. Let $P$ be a bounded complex of finite-dimensional vector spaces. In these conventions the tensor–Hom map is

\[
 \Phi:P\otimes P^\vee\longrightarrow\operatorname{Hom}^\bullet(P,P),
 \qquad \Phi(p\otimes\varphi)(q)=p\,\varphi(q).
 \tag{20}
\]

For homogeneous $\varphi$ of degree $b$, the dual differential is $d\varphi=(-1)^{b+1}\varphi d$. Consequently (20) is a chain map: its tensor differential evaluates as $dp\,\varphi(q)+(-1)^{a+b+1}p\,\varphi(dq)$, which is the Hom differential for an element of degree $a+b$. This checks the normalization used in (11)–(13).

Choose homogeneous bases $e_{q,j}$ of $P^q$, with dual basis $e_{q,j}^*$ of degree $-q$. Under (20), the element representing the identity is

\[
 \sum_{q,j}e_{q,j}\otimes e_{q,j}^*.
\]

It is closed because $\mathrm{id}_P$ is a chain map. Applying (10), the swap contributes $(-1)^{q(-q)}=(-1)^q$, and evaluation contributes $1$. Thus the trace of the identity is $\sum_q(-1)^q\dim P^q$ as an element of $k$.

We must still show that this alternating count of terms equals the alternating count of cohomology. Write $B^q=\operatorname{im}d^{q-1}$ and $Z^q=\ker d^q$. The two finite-dimensional exact sequences

\[
 0\longrightarrow Z^q\longrightarrow P^q\longrightarrow B^{q+1}\longrightarrow0,
 \qquad
 0\longrightarrow B^q\longrightarrow Z^q\longrightarrow H^q(P)\longrightarrow0
\]

give $\dim P^q=\dim B^q+\dim H^q(P)+\dim B^{q+1}$. The boundary contributions cancel in the finite alternating sum. Therefore

\[
 C(P)=\chi(P)\,1_k.
 \tag{21}
\]

This cancellation is a computation on a representative; it does not assert a canonical splitting of a general sheaf complex into its cohomology.

More generally a degree-zero chain endomorphism $u$ preserves $B^q$ and $Z^q$. Trace is additive on a finite invariant subspace and its quotient: a basis adapted to the subspace makes its matrix block triangular. The isomorphism $P^q/Z^q\simeq B^{q+1}$ conjugates the induced endomorphisms. The same cancellation proves

\[
 \operatorname{str}(u):=\sum_q(-1)^q\operatorname{tr}(u^q)
 =\sum_q(-1)^q\operatorname{tr}(H^q(u)).
 \tag{22}
\]

A chain homotopy changes neither side. One can also see the invariance directly: for a degree $-1$ map $h$, the terms in $\operatorname{str}(dh+hd)$ cancel after reindexing, using $\operatorname{tr}(AB)=\operatorname{tr}(BA)$ for maps between two finite-dimensional vector spaces. This last identity follows by writing both traces as the same sum of matrix products.

The integer in (21) embeds into $k$ because the characteristic is zero. The same graded construction over a positive-characteristic field would return the image of that integer in the field; it could lose its value. For instance, the identity of $k^2$ has Euler index $2$ but trace $0$ in characteristic two.

## Shifts and triangles give local accounting rules

With the cohomological convention $H^q(P[r])=H^{q+r}(P)$, reindexing (2) gives

\[
 \chi(P[r])=(-1)^r\chi(P).
 \tag{23}
\]

If $P\to Q\to R\xrightarrow{+1}$ is a distinguished triangle of bounded finite coefficient complexes, its long exact cohomology sequence is a finite exact sequence after appending zero terms. Alternating dimensions in any finite exact sequence sum to zero: writing each term as its incoming image plus outgoing image cancels consecutive contributions. Applied in the order $H^q(P),H^q(Q),H^q(R),H^{q+1}(P)$, this yields

\[
 \chi(Q)=\chi(P)+\chi(R).
 \tag{24}
\]

Stalk and costalk functors preserve distinguished triangles. Equations (23)–(24) consequently apply pointwise to both functions in (4). They also apply to global indices whenever all three section complexes satisfy the finiteness condition in (8).

These rules concern Euler indices. We have not yet proved the corresponding general additivity theorem for sheaf characteristic classes. At a point it follows from (21) and (24), but the geometric statement requires its own trace argument.

## Exercises with complete solutions

### Cancel the boundaries in a nontrivial chain trace

*Difficulty: Intermediate.*

Let $P^0=k^2$, $P^1=k^3$, with differential $d(x,y)=(x,0,0)$ and all other terms zero. Let $u^0=\operatorname{diag}(a,b)$ and $u^1=\operatorname{diag}(a,c,e)$. Verify that $u$ is a chain map, compute its trace through cohomology and through terms, and calculate $C(P)$ for $u=\mathrm{id}$. Explain why adding a chain homotopy does not change the answer.

**Solution.** The equality $du^0=u^1d$ is $(ax,0,0)=(ax,0,0)$. Its zeroth cohomology is $\ker d=k(0,1)$, where $u$ acts by $b$. Its first cohomology is $k^3/k(1,0,0)$, with induced diagonal entries $c,e$. Thus the alternating cohomology trace is $b-c-e$.

The alternating term trace is $(a+b)-(a+c+e)=b-c-e$. The same entry $a$ occurs on the boundary and its preceding quotient, so it cancels. For the identity, $C(P)=(2-3)1_k=-1_k$, also equal to $(1-2)1_k$ from cohomology.

If $u$ changes by $dh+hd$, its cohomology action is unchanged. Explicitly, write $h:P^1\to P^0$ as a $2\times3$ matrix. The only potentially nonzero traces are $\operatorname{tr}(hd)$ on $P^0$ and $\operatorname{tr}(dh)$ on $P^1$, both the top-left entry of $h$. They have opposite signs. Their difference is zero, so the evaluated trace is homotopy invariant.

### A cone accounts for a shift without choosing a splitting

*Difficulty: Introductory.*

Let $v:k^2\to k^3$ have rank $r$, and let $R=\operatorname{Cone}(v)$, with the input spaces placed in degree zero. Find $\chi(R)$ from its cohomology and from its distinguished triangle. What are $C(k[1])$ and $C(k\oplus k[1])$ on a point? Does vanishing of this last class imply that its complex is zero?

**Solution.** The cone has $H^{-1}(R)=\ker v$ of dimension $2-r$ and $H^0(R)=\operatorname{coker}v$ of dimension $3-r$. Consequently $\chi(R)=-(2-r)+(3-r)=1$. The triangle $k^2\to k^3\to R\xrightarrow{+1}$ gives the same result $3-2=1$ through (24).

The shift $k[1]$ has its nonzero cohomology in degree $-1$, so (21) gives $C(k[1])=-1_k$. Direct-sum evaluation makes the identity block diagonal, hence $C(k\oplus k[1])=1_k-1_k=0$. The complex still has two nonzero cohomology groups. Its characteristic class is a signed trace and need not detect the object. No sheaf-level splitting or general geometric additivity theorem was used.

### Calculate the closed-embedding comparison rather than replacing it

*Difficulty: Advanced.*

Let $i:\{0\}\hookrightarrow\mathbb R$ and $A=k_{\mathbb R}$. Compute $i^!A$, $i^{-1}A$ and $\beta_{i,A}$. Then take $A=i_*P$ for a bounded finite coefficient complex $P$, and compute the same map. Prove uniqueness of the support lift (18), and indicate the hypothesis that makes the proof work.

**Solution.** Point-supported cohomology of a constant sheaf on a line is the fibre of $k\to k\oplus k$, with map $a\mapsto(a,a)$, obtained by deleting the point from a small interval. This fibre is $k[-1]$. Ordinary restriction is $k$. Since $\operatorname{Hom}_{D(k)}(k[-1],k)=\operatorname{Ext}^1_k(k,k)=0$, the comparison $\beta_{i,A}$ is the zero morphism. Its source is nevertheless nonzero.

For $A=i_*P$, closed-support localization is an isomorphism $i_*i^!A\to A$. The equivalences $i^!i_*P\simeq P$ and $i^{-1}i_*P\simeq P$ turn the defining counit in (14) into the identity. Thus $\beta_{i,i_*P}=\mathrm{id}_P$. The contrast records dependence on the object; it does not give an isomorphism between the two functors in general.

For the support lift, let $E$ be supported on a closed set $Z$ and let $j:X\setminus Z\hookrightarrow X$. The triangle $R\Gamma_ZE\to E\to Rj_*j^{-1}E\xrightarrow{+1}$ has zero open term. Hence $R\Gamma_ZE\to E$ is an isomorphism. The right adjunction for $R\Gamma_Z$ gives

\[
 \operatorname{Hom}(E,R\Gamma_ZA)\xrightarrow{\sim}\operatorname{Hom}(E,A)
\]

for every $A$. This proves existence and uniqueness of the lift of $E\to A$, and applying the functor to that map produces it explicitly. The needed hypothesis is that the source $E$ is supported on $Z$. In (19) we apply it to $E=E_F$, then precompose with the unit; we do not assume $k_X$ is supported on $Z$.

### Check finiteness before reading a trace as an integer

*Difficulty: Intermediate.*

Compare $F=k_{\mathbb R^n}$, a constant sheaf on a countable discrete manifold, and a bounded constructible complex with compact closed support. Determine which global Euler indices are defined in these examples. Why does a field-valued trace cease to recover the integer index in characteristic $p>0$?

**Solution.** Contractibility gives $R\Gamma(\mathbb R^n;k)=k$, while the compactly supported cohomology of an oriented real $n$-ball, or its one-point compactification, gives $R\Gamma_c(\mathbb R^n;k)=k[-n]$. The same holds for $\mathbb R^n$ by the usual exhaustion and compact-support extension maps. Thus both indices are defined, with values $1$ and $(-1)^n$. Noncompactness by itself does not prevent finiteness, and it does not force ordinary and compact indices to agree.

On the countable discrete manifold, the section groups are the infinite product and direct sum displayed above. Each contains arbitrarily large finite linearly independent sets, so its dimension is infinite. The local Euler functions remain $1$, but (8) supplies no global integer.

A bounded constructible complex with compact closed support has perfect ordinary and compact section complexes by compact finiteness. The map (9) identifies them, so both indices exist and agree. These are consequences of the support and coefficient hypotheses, not of counting local ranks alone.

Over characteristic $p$, the supertrace of the identity still computes the image of the alternating integer in $k$. The nonzero integer $p$ maps to zero, for example for a $p$-dimensional vector space in degree zero. Equality of field-valued traces therefore determines the integer only modulo $p$. Characteristic zero makes the map $\mathbb Z\to k$ injective and avoids this loss.

### Keep the real orientation line and the cohomological shift

*Difficulty: Intermediate.*

Let $L$ be a finite-rank local system on a real $n$-manifold, and let $F=L[r]$. Compute $A_x(F)$, $C_x(F)$, $(D_XF)_x$ and both functions in (4). Which computations require an orientation of the entire manifold? Which shift would be incorrect if one treated the manifold as complex without that hypothesis?

**Solution.** On a small coordinate ball, $L$ is constant with fibre $L_x$. Ordinary restriction gives $A_x(F)=L_x[r]$. The local orientation calculation gives

\[
 C_x(F)=L_x\otimes\operatorname{or}_{X,x}[r-n].
\]

Duality reverses the coefficient shift and contributes the manifold dualizing complex, so

\[
 (D_XF)_x=L_x^\vee\otimes\operatorname{or}_{X,x}[n-r].
\]

These expressions also match (5), using the canonical self-duality of the orientation line: its transition functions are signs, whose inverse equals itself. Consequently

\[
 \chi(F)(x)=(-1)^r\operatorname{rank}L_x,\qquad
 \chi_c(F)(x)=(-1)^{r-n}\operatorname{rank}L_x
             =(-1)^{n-r}\operatorname{rank}L_x.
\]

The final equality is equality of parities. All calculations are local and retain the orientation line, so none requires a global orientation. One may trivialize that line only after choosing an orientation. The shift is the real dimension $n$. Replacing it with $2n$ is justified only when $n$ instead denotes a complex dimension of a complex manifold, which is a different hypothesis and convention.

### Compare an open interval and a closed interval at every point

*Difficulty: Advanced.*

On $X=\mathbb R$, put $F_{c}=k_{[0,1]}$ and $F_{o}=k_{(0,1)}$, the latter extended by zero. Compute both local Euler functions at interior points, endpoints and exterior points, then both global indices. Verify (6) using the dual sheaves and explain why the zero endpoint stalks of $F_{o}$ do not remove the endpoints from its closed support.

**Solution.** At an interior point both sheaves are locally constant $k$, so their ordinary stalk is $k$ and their costalk is $k[-1]$. At an endpoint, use the localization fibre

\[
 C_x(F)\longrightarrow F_x
 \longrightarrow R\Gamma(B\setminus\{x\};F)\xrightarrow{+1}
\]

in a sufficiently small interval $B$. For $F_{c}$, the middle term is $k$ and the punctured term is $k$ on the side inside $[0,1]$; restriction is the identity. The costalk is zero. For $F_{o}$ the middle term is zero and the punctured term is $k$ on the interior side. The fibre is $k[-1]$. At an exterior point both measurements vanish. The complete table is

| Sheaf and function | $x\in(0,1)$ | $x\in\{0,1\}$ | $x\notin[0,1]$ |
|---|---:|---:|---:|
| $\chi(F_{c})(x)$ | $1$ | $1$ | $0$ |
| $\chi_c(F_{c})(x)$ | $-1$ | $0$ | $0$ |
| $\chi(F_{o})(x)$ | $1$ | $0$ | $0$ |
| $\chi_c(F_{o})(x)$ | $-1$ | $-1$ | $0$ |

For $j:(0,1)\hookrightarrow\mathbb R$, open internal-Hom adjunction gives $D_{\mathbb R}F_{o}\simeq Rj_*\omega_{(0,1)}=Rj_*k_{(0,1)}[1]$. On a small interval about either endpoint, the nonempty intersection with $(0,1)$ is a contractible interval. Its [derived constant sections](../sheaf-proof-readings/src/SH02/convex-acyclicity.md#sh02-ca-constant--constant-coefficients) are $k$ and the restriction maps preserve that constant value. Thus the actual constant-section comparison gives $Rj_*k_{(0,1)}\simeq F_{c}$. This proves $D_{\mathbb R}F_{o}\simeq F_{c}[1]$ as a sheaf complex, with its maps. Constructible biduality and reversal of shifts now give $D_{\mathbb R}F_{c}\simeq F_{o}[1]$. Taking their stalk Euler indices reproduces the two costalk rows, including endpoints, and verifies (6).

For global sections, the closed interval is contractible and compact, giving $R\Gamma(\mathbb R;F_{c})=R\Gamma_c(\mathbb R;F_{c})=k$. Extension by zero identifies compact sections of $F_{o}$ with compact sections on the open interval, giving $R\Gamma_c(\mathbb R;F_{o})=k[-1]$. Its closed support is $[0,1]$, so (9) also gives $R\Gamma(\mathbb R;F_{o})=k[-1]$. Therefore both global indices of $F_{c}$ are $1$ and both global indices of $F_{o}$ are $-1$.

Every neighborhood of either endpoint contains interior points where $F_{o}$ has nonzero stalk. There is no open vanishing neighborhood of an endpoint. Hence the endpoints belong to the closed support used for properness and supported characteristic classes. This remains true despite their zero ordinary stalks.

## References

Masaki Kashiwara, *Index theorem for constructible sheaves*, Astérisque 130 (1985), §8.3–8.4, pp. 205–206, expresses local stalk and costalk Euler indices through characteristic-cycle intersections and relates constructible functions to cycles; [freely readable article](https://www.numdam.org/item/AST_1985__130__193_0/). Those intersection statements belong to the subsequent geometric arguments. The normalized supported map and point trace in this lesson are constructed above using the linked product evaluation, exceptional-Hom and composition proofs.

## What the construction prepares

The identity, the normalized diagonal evaluation, the closed-embedding comparison and contraction now define the supported class (19). Its point value is the Euler index with the graded sign proved in (21). Local stalk and costalk indices and their elementary accounting rules are established, with separate global finiteness conditions. The next lesson must compare this full chain with proper direct image on the closed support, retaining the unit, exceptional and ordinary exchanges and the evaluated tensor map. Only that compatibility will identify the integral of $C(F)$ with the global Euler index for compact support; cotangent characteristic cycles require further geometric constructions beyond this lesson.

## Source account for the supported normalization

Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), §§4.6–4.8, pp. 94–99, provides the exceptional-Hom, dual-sections and external-Hom framework. Corollary 4.6.2 fixes exceptional composition; Propositions 4.6.5, 4.6.7 and 4.6.8 give exceptional Hom, closed support and the diagonal comparison. Proposition 4.8.3 states the local dual pairings, and Proposition 4.8.4 proves the external-Hom comparison from represented neighborhood systems. Its §4.8 states a Noetherian coefficient convention and explains the perfect-complex replacement; its external-Hom proposition has a bounded second input. Both restrictions hold in this field-coefficient, bounded construction. The more general neighbourhood-system proof required by the linked provider remains that provider’s explicit argument. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), §8.3–8.4, concerns local Euler indices and characteristic cycles, not a substitute proof of the supported diagonal map. Here that map is derived from the cited operation contracts in (9)–(19), and its point sign is proved in (20)–(21). Additivity of Euler numbers is proved; additivity of the supported class, its proper transport, and the global index theorem are not asserted without their further proofs.
