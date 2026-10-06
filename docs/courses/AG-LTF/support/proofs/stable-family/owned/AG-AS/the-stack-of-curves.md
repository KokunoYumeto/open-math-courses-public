# The stack of curves

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A node has a deformation \(xy=t\). The parameter \(t\) smooths its two branches, while deformations of the rest of a curve must glue around it. For proper nodal curves both parts of that gluing problem are unobstructed. Stability supplies a different ingredient: it removes vector fields, including those carried by a rational tail or bridge. Together these facts make the moduli of stable curves a smooth Deligne–Mumford stack.

We use the algebraicity theorem for the full curve stack stated in Lesson 8, the arbitrary-base Deligne–Mumford criterion proved in Lesson 6, and the infinitesimal methods of Lesson 7. Ordinary curve cohomology, Riemann–Roch and degree of a line bundle are prerequisites. Section 9 specifies the other ordinary geometric and deformation inputs. None of the smoothness, stability or dimension results proved here is used as its own prerequisite.

All stacks are over \(\operatorname{Spec}\mathbb Z\). A geometric fibre means base change to an algebraic closure of the residue field. The base of a family may be an arbitrary scheme. We use \(g\geq2\) whenever writing \(\mathcal M_g\) or \(\overline{\mathcal M}_g\).

## 1. Families and their diagonal

### 1.1. The full curve stack

An object of \(\mathcal{Curves}(S)\) is a morphism of algebraic spaces
\[
f:X\longrightarrow S
\tag{1.1}
\]
which is proper, flat, of finite presentation, with fibres of dimension at most one. An arrow over \(S\) is an \(S\)-isomorphism. Pullback defines arrows over other bases. Initially a curve may be nonreduced, disconnected, zero-dimensional or empty. Smoothness, connectedness and stability will select open substacks; they are not part of (1.1).

Allowing algebraic spaces is essential to effective descent. Given an fppf cover and compatible families, descent of algebraic spaces produces \(X\), and properness, flatness, finite presentation and the dimension bound descend. Isomorphisms descend uniquely, so this is descent of the entire groupoid. The theorem stated in Lesson 8, Section 8, [Stacks, Tag 0D5A], says that this stack is algebraic.

The same description works over an algebraic space \(S\). Choose an étale scheme cover \(U\to S\). A morphism \(S\to\mathcal{Curves}\) is a family over \(U\), together with its identifying isomorphism over \(U\times_S U\) and the cocycle equality on the triple product. Effective descent gives (1.1) over \(S\). Conversely its pullbacks give exactly this datum. A map between two such data descends to one and only one isomorphism between the resulting spaces; composition also descends. Thus the two constructions are quasi-inverse on objects and every arrow. This proves the extension of the moduli interpretation in [Stacks, Tag 0DMJ].

The stack is locally of finite presentation over \(\mathbb Z\). Indeed, over a filtered limit of affine bases, finite-presentation spaces descend using finitely many étale charts and their finitely presented overlaps. The morphism and its flatness and properness descend to a sufficiently late stage by the ordinary finite-presentation limit theorems. The fibre dimension bound does too. Isomorphisms and equality of isomorphisms descend at a late stage because both their maps and their inverse identities are finite-presentation data. Thus the full groupoid commutes with these limits. The limit characterization of local finite presentation for an algebraic stack applies.

### 1.2. Why a family is projective étale locally on its base

**Proposition 1.1.** Every family (1.1) becomes a projective scheme after an étale cover of its base. The stack of such families with a chosen relatively ample line bundle maps smoothly and surjectively to \(\mathcal{Curves}\).

**Proof.** A proper algebraic space of dimension at most one over a field is a scheme, and a proper scheme of that dimension is projective. These are the precise ordinary curve inputs recorded in Section 9. Every field-valued object therefore has an ample line bundle.

For a fixed family \(X/S\), the fibre of the forgetful map is the substack of the relative Picard stack whose line bundles are relatively ample. It is open: if a line bundle is ample on one fibre of a proper finitely presented morphism, it is relatively ample on the inverse image of a neighbourhood of that base point; this open commutes with arbitrary base change.

The relative Picard stack is algebraic by Lesson 8. It is smooth over \(S\). To check the latter assertion, take an Artinian square-zero extension \(A'\to A\) with kernel \(I\) and a line bundle on \(X_A\). The obstruction to lifting it is in
\[
H^2(X_A,\mathcal O_{X_A}\otimes_A I)=0.
\tag{1.2}
\]
The scheme \(X_A\) has topological dimension at most one; the vanishing is ordinary coherent cohomological dimension. Equivalently one may compute in étale charts. The Čech multiplication cocycle for the transition units has its obstruction in (1.2), and a vanishing obstruction changes those units to a genuine lifted cocycle. This gives marked lifts over every such extension. The Picard stack is locally of finite presentation, so the infinitesimal smoothness criterion, explained in Section 4.3, proves smoothness. The ample open is consequently smooth as well. Its field-valued nonemptiness proves surjectivity.

Take a smooth scheme atlas of this fibre over \(S\). The resulting smooth surjection to \(S\) admits sections after an étale cover of \(S\). Those sections supply relatively ample bundles. An algebraic space with a relatively ample line bundle is a scheme, and a proper morphism with such a bundle is projective locally on the base: a sufficiently high power gives a closed immersion into a projective space after shrinking. Refining the étale cover by those opens proves the assertion. \(\square\)

This proves [Stacks, Tag 0DPY]. It does not assert that every family is globally a scheme or has a global polarization.

### 1.3. Isomorphisms are bounded

**Proposition 1.2.** The diagonal of \(\mathcal{Curves}\) is separated and of finite presentation.

**Proof.** For two families \(X/S,Y/S\), the diagonal fibre is
\[
\operatorname{Isom}_S(X,Y)\subset\operatorname{Mor}_S(X,Y).
\tag{1.3}
\]
Lesson 8, Corollary 6.4, constructs the morphism space as an open in the Hilbert space of graphs and proves it locally of finite presentation. The locus of isomorphisms is open: apply the same proper, finite-projection isomorphism test to the universal map \(X\to Y\). The graph Hilbert space is separated, as proved by the two-kernel diagonal test in Lesson 8. Both spaces in (1.3) are therefore separated.

It remains to prove quasi-compactness, for which finite presentation of each individual curve is insufficient by itself. Use Proposition 1.1 and a smooth atlas of pairs of polarized curves. Since this atlas is locally of finite presentation over \(\mathbb Z\), its affine pieces are Noetherian. It suffices to work over a connected Noetherian affine \(S\) with projective families and relatively ample bundles \(L\) on \(X\), \(N\) on \(Y\).

Their fibre Hilbert polynomials
\[
P(n)=\chi(X_s,L_s^n),\qquad Q(n)=\chi(Y_s,N_s^n)
\]
are independent of \(s\): proper flat perfect cohomology makes every Euler characteristic locally constant, and \(S\) is connected. On \(X\times_S Y\) put \(H=\operatorname{pr}_X^*L\otimes\operatorname{pr}_Y^*N\). For any fibre isomorphism \(a:X_s\to Y_s\), its graph has polynomial
\[
\chi(X_s,L_s^n\otimes a^*N_s^n)
=P(n)+Q(n)-P(0).
\tag{1.4}
\]
Here curve Riemann–Roch gives additivity of degree and \(\chi(L^n)=n\deg L+\chi(\mathcal O)\), valid also for a proper scheme of dimension at most one; if an isomorphism exists, \(P(0)=Q(0)\). Zero-dimensional components contribute their constant Euler characteristic and do not invalidate (1.4).

All isomorphism graphs lie in this one fixed-polynomial projective Hilbert scheme. It is a Noetherian scheme of finite type over \(S\), by the precise projective Hilbert prerequisite from AG-HP-05. The open graph-isomorphism locus inside it is quasi-compact. Thus (1.3) is quasi-compact. Descent through the chosen smooth covers now proves that the diagonal is quasi-compact, separated and locally of finite presentation, hence of finite presentation. \(\square\)

This is [Stacks, Tag 0DSP], with the curve stack retained throughout. No preservation of the chosen polarizations is imposed on the isomorphisms in (1.3).

## 2. Open conditions and genus

### 2.1. A universal open-locus construction

Suppose a property of fibres determines, in every family, an open subset \(S_P\subset S\), invariant under isomorphism and satisfying
\[
(S_P)\times_S T=T_P
\tag{2.1}
\]
for every \(T\to S\). Restricting the objects to these opens gives a full open substack. To verify representability of the inclusion, its pullback by the object \(X/S\) is exactly the scheme \(S_P\); all arrows are still the original isomorphisms.

A common construction starts with the open \(W\subset X\) where a fibre-local property holds. If formation of \(W\) commutes with arbitrary base change, put
\[
S_P=S\setminus f(X\setminus W).
\tag{2.2}
\]
Properness makes the omitted image closed. A fibre is entirely in \(W\) precisely when its base point is in \(S_P\); this characterization and geometric invariance prove (2.1), including base changes that are not flat.

The ordinary fibre-locus theorems for flat finitely presented morphisms give such a \(W\) for Cohen–Macaulay, Gorenstein, local complete intersection, smooth and nodal fibres. For the nodal locus, “nodal” includes relative dimension one, and smooth points of a one-dimensional fibre count as nodal. They also give an open base locus of geometrically reduced fibres for a proper flat finitely presented morphism. Section 9 states these inputs separately from the resulting moduli assertions. Thus (2.2) proves the corresponding open substacks in [Stacks, Tags 0E0E, 0E0F, 0E1L, 0E0J, 0DZT and 0DSX].

Within Cohen–Macaulay curves, the relative-dimension-zero and relative-dimension-one parts of \(X\) are open and closed: fibre dimension is locally constant at a Cohen–Macaulay point of a flat family. Removing the proper image of the zero-dimensional part gives the open of equidimensional one-dimensional Cohen–Macaulay fibres. The same construction applies inside the Gorenstein locus. A local complete intersection family is already flat by definition of our stack, so it is syntomic. Within the smooth locus, the zero-dimensional part is likewise open and closed; deleting its proper image gives smooth curves of pure dimension one.

There is also an open of fibres with only finitely many nonsmooth points, [Stacks, Tag 0E0K]. The nonsmooth locus \(Z\) is closed in \(X\), hence proper over \(S\). Where its fibre is finite, properness and openness of the quasi-finite locus provide a neighbourhood on which \(Z\) is finite: remove the proper image of its non-quasi-finite part. This constructs the universal open in question.

### 2.2. Global functions and the genus pieces

For a proper one-dimensional scheme \(C/k\), we define its genus only when \(H^0(C,\mathcal O_C)=k\), and then set \(g=\dim_kH^1(C,\mathcal O_C)\). In a family the appropriate global-functions condition is universal:
\[
\mathcal O_T\xrightarrow{\ \sim\ }f_{T,*}\mathcal O_{X_T}
\quad\text{for every }T\to S.
\tag{2.3}
\]

**Lemma 2.1.** The fibres of dimension one with \(H^0(X_s,\mathcal O_{X_s})=\kappa(s)\) form a universal open locus. On it (2.3) holds, \(R^1f_*\mathcal O_X\) is finite locally free and its formation commutes with arbitrary base change. Its rank gives open and closed genus pieces.

**Proof.** Proper flat perfect cohomology represents \(Rf_*\mathcal O_X\) locally by a finite complex of finite free modules, compatible with every derived base change. Coherent cohomological dimension on the fibres and cancellation of contractible free summands let us choose it in degrees \(0,1\). The locus of fibres of dimension one is open for a proper flat finitely presented family; it excludes the empty fibre.

At a point in that locus the unit section \(1\) is a nonzero element of \(H^0\). The locus where \(h^0=1\) is open by upper semicontinuity, since all nearby nonempty fibres have \(h^0\geq1\). For a two-term free complex \(P^0\to P^1\), choose a minor of size \(\operatorname{rank}P^0-1\) invertible at the point. It splits off an isomorphism, leaving one column in degree zero. The unit is a cycle and its coefficient in this remaining column is a unit after shrinking. The cycle equality therefore forces that whole column to be zero, including any nilpotent entries; it also trivializes the kernel. Locally the complex is consequently
\[
\mathcal O_S[0]\oplus E[-1]
\tag{2.4}
\]
with \(E\) finite locally free. Its degree-zero unit is the stated summand. Tensoring (2.4) with any base algebra proves (2.3) and identifies \(R^1f_*\mathcal O_X\) with \(E\), with all base changes. Ranks of a finite locally free module are locally constant, proving the last assertion. \(\square\)

This proves the genus construction of [Stacks, Tag 0E6H]. We write \(\mathcal{Curves}_g\) for these pieces; geometric reducedness is not built into that notation.

For a reduced connected proper curve over an algebraically closed field, every global function is constant. One proof restricts the function to each integral proper component, where a regular function is constant, and observes that meeting components have equal constants. Connectedness makes every constant equal. Geometric reducedness and connectedness therefore imply the fibre condition in Lemma 2.1. Conversely, on geometrically reduced proper fibres, their global-functions algebra after algebraic closure is one copy of the field per connected component. Hence, inside the geometrically reduced pure-one-dimensional open, the condition \(h^0=1\) selects exactly the geometrically connected fibres. This proves the open \(\mathcal{Curves}^{\mathrm{grc},1}\) and its open and closed pieces \(\mathcal{Curves}^{\mathrm{grc},1}_g\), [Stacks, Tag 0E1H].

Reduced one-dimensional fibres are Cohen–Macaulay. At a closed point, a reduced Noetherian ring of dimension one has no embedded associated prime, so an element avoiding its finitely many minimal primes is a non-zero-divisor; its depth is one. A connected reduced fibre of dimension one has no separate zero-dimensional component. These observations justify the pure-dimension condition just used.

Define
\[
\mathcal M_g
=\mathcal{Curves}^{\mathrm{smooth},1}
\cap\mathcal{Curves}^{\mathrm{grc},1}_g.
\tag{2.5}
\]
It is an open algebraic stack locally of finite presentation over \(\mathbb Z\). This is the connected genus-\(g\) smooth locus; the full smooth locus also contains disconnected and zero-dimensional objects.

## 3. The maximal Deligne–Mumford open

### 3.1. An invariant differential module

For a family \(X/S\) set \(G=\operatorname{Aut}_S(X)\). Proposition 1.2 makes it a separated, finitely presented group algebraic space over \(S\). Let \(e:S\to G\) be its identity and put
\[
V=e^*\Omega_{G/S}.
\tag{3.1}
\]
This is a finitely presented \(\mathcal O_S\)-module. Formation of \(V\) commutes with arbitrary base change, because relative Kähler differentials do.

**Lemma 3.1.** \(G\to S\) is unramified if and only if \(V=0\). The largest open on which this holds is the zero locus of the module \(V\), and this open commutes with every base change.

**Proof.** Translation gives
\[
\Omega_{G/S}\simeq\pi^*V,\qquad \pi:G\to S.
\tag{3.2}
\]
For completeness, use the isomorphism over the first factor \(G\) of \(G\times_S G\) sending \((g,h)\) to \((g,g^{-1}h)\). It sends the diagonal section to the identity section. Pulling back the relative differentials of the second projection along these two sections identifies the left side of (3.2) with its right side. This argument works on étale charts and needs no flatness of \(G\).

A locally finitely presented morphism is unramified precisely when its relative differentials vanish. Thus (3.2) proves the equivalence. The nonzero-support locus of a finite module is closed, so its complement \(S_V\) is open. A point belongs to it if and only if \(V\otimes\kappa(s)=0\), by Nakayama. After any field extension that test is unchanged. Consequently the pullback module has precisely the pulled-back zero locus, proving the base-change assertion. \(\square\)

### 3.2. The universal criterion

**Theorem 3.2.** There is a maximal Deligne–Mumford open substack \(\mathcal D\subset\mathcal{Curves}\). For every family \(X/S\),
\[
S\to\mathcal{Curves}\text{ factors through }\mathcal D
\quad\Longleftrightarrow\quad
\operatorname{Aut}_S(X)\to S\text{ is unramified}.
\tag{3.3}
\]
This is [Stacks, Tag 0DSW].

**Proof.** On a smooth atlas of \(\mathcal{Curves}\), apply Lemma 3.1 to the universal family. Its zero locus is invariant under every isomorphism of families and satisfies arbitrary base change. Thus it descends, by Section 2.1, to an open \(\mathcal D\). Its pullback by \(X/S\) is precisely \(S_V\). The map factors through this open exactly when \(V=0\) everywhere, proving both directions of (3.3).

The diagonal of \(\mathcal D\) is unramified. Indeed, over a geometric pair of its points, the isomorphism space is either empty or becomes a torsor under the automorphism group after choosing an isomorphism. The latter group is unramified. Thus every geometric fibre of the locally finitely presented diagonal has zero differentials. Relative differentials on the diagonal are finite modules; fibrewise vanishing and Nakayama make them zero. Lesson 6's proved unramified-diagonal criterion supplies an étale atlas, so \(\mathcal D\) is Deligne–Mumford.

Finally any Deligne–Mumford open has unramified diagonal, hence unramified inertia after its diagonal base change. Its families have \(V=0\), so it is contained in \(\mathcal D\). This proves maximality. \(\square\)

For a proper curve \(C/k\), the tangent space at the identity of its automorphism group is
\[
\operatorname{Der}_k(\mathcal O_C,\mathcal O_C)=H^0(C,T_C),
\qquad
T_C=\mathcal H om(\Omega_{C/k},\mathcal O_C).
\tag{3.4}
\]
Indeed an automorphism of the trivial first-order deformation reducing to the identity has the form \(a\mapsto a+\epsilon D(a)\); multiplicativity says exactly that \(D\) is a derivation, and its inverse is \(1-\epsilon D\). These formulas glue and prove (3.4). Since the differential module in (3.1) is finite, zero tangent space over a field is equivalent to its vanishing, and thus to unramifiedness. No restriction on the characteristic is used.

## 4. Nodal curves and smoothness over the integers

### 4.1. The local node calculation

A curve is nodal if its geometric fibres are pure one-dimensional and their singularities are ordinary double points. At a node over an algebraically closed field \(k\) the completed ring is
\[
R=k[[x,y]]/(xy).
\tag{4.1}
\]
Smooth points are allowed. The nodal locus \(\mathcal N=\mathcal{Curves}^{\mathrm{nodal}}\) is the open constructed in Section 2.1. A node is a hypersurface local complete intersection, hence Gorenstein.

Complete the cotangent complex of the algebraic node at its singular point. Its completed, or continuous, cotangent complex is the two-term complex
\[
\widehat L=[R\xrightarrow{(y,x)}R\,dx\oplus R\,dy]
\quad\text{in degrees }-1,0.
\tag{4.2}
\]
Dualizing against \(R\) gives \(R^2\to R\), \((a,b)\mapsto ya+xb\). Thus the local deformation module is
\[
T^1_R=\operatorname{coker}(R^2\to R)=R/(x,y)=k,
\qquad T^q_R=0\quad(q\geq2).
\tag{4.3}
\]
Changing a relation \(xy\) to \(xy-\epsilon c\) represents \(c\) in this quotient. Coordinate changes \(x\mapsto x+\epsilon a,\ y\mapsto y+\epsilon b\) change its coefficient by \(ya+xb\), explaining the quotient directly.

The one local smoothing parameter therefore appears in
\[
xy=t.
\tag{4.4}
\]
The algebra \(A[x,y]/(xy-a)\) is free as an \(A\)-module, with basis \(1,x,x^2,\ldots,y,y^2,\ldots\): division by the monic leading monomial \(xy\) gives existence and uniqueness of this normal form. In particular it is flat for every \(a\in A\). Over an Artinian local \(A\), a split node in a flat family has completed ring \(A[[x,y]]/(xy-a)\), \(a\in\mathfrak m_A\), by the ordinary formal local-structure theorem [Stacks, Tag 0CBX]. Its proof successively absorbs all nonconstant errors into \(x,y\); only the constant error remains as \(a\). Lifting \(a\) across \(A'\to A\) gives the local lift. Smooth charts also lift. This proves local unobstructedness, but does not yet prove that the local pieces glue.

### 4.2. The global obstruction includes the local deformation sheaf

**Proposition 4.1.** Let \(A'\to A\) be a square-zero surjection of Artinian local rings, with kernel \(I\). Every proper flat nodal curve \(C/A\) lifts to a proper flat finitely presented nodal curve over \(A'\), with the given identification on reduction.

**Proof.** The closed fibre is a proper algebraic space of dimension one over a field, hence a scheme. A nilpotent thickening of a scheme by an algebraic space is again a scheme, so \(C\) itself is a scheme. These ordinary facts let us use scheme cohomology over any Artinian residue field. Node calculations may be checked after a faithfully flat field extension that splits their two branches.

Since \(C/A\) is flat and its fibres are local complete intersections, it is a local complete intersection morphism. Its cotangent complex \(L_{C/A}\) is perfect in degrees \([-1,0]\). Put \(M=\mathcal O_C\otimes_A I\), and define
\[
\mathcal T^q(M)=\mathcal E xt^q_{\mathcal O_C}(L_{C/A},M).
\tag{4.5}
\]
The ordinary cotangent deformation theorem gives an obstruction in \(\operatorname{Ext}^2(L_{C/A},M)\); it vanishes if and only if a marked flat lift exists. When lifts exist, their classes are a torsor under \(\operatorname{Ext}^1(L_{C/A},M)\), and their automorphisms reducing to the identity are \(\operatorname{Ext}^0(L_{C/A},M)\). This is the precise general theorem used here, not a nodal smoothness assertion.

The two-term complex gives \(\mathcal T^q(M)=0\) for \(q\geq2\). On the smooth locus its degree-one cohomology is zero. Consequently \(\mathcal T^1(M)\) is a coherent sheaf supported on the finitely many closed-fibre nodes. A proper closed subspace with that support is finite over the Artinian base: it is proper and quasi-finite, hence finite. It is affine, so
\[
H^1(C,\mathcal T^1(M))=0.
\tag{4.6}
\]
Also the underlying Noetherian space of \(C\) has dimension one, so
\[
H^2(C,\mathcal T^0(M))=0.
\tag{4.7}
\]
The local-to-global Ext spectral sequence
\[
H^p(C,\mathcal T^q(M))
\Longrightarrow\operatorname{Ext}^{p+q}(L_{C/A},M)
\tag{4.8}
\]
now has all its terms of total degree two equal to zero: they are (4.7), (4.6), and \(H^0(\mathcal T^2(M))\). Therefore \(\operatorname{Ext}^2(L_{C/A},M)=0\). The obstruction vanishes and a marked flat lift exists.

The deformation theorem retains finite presentation. Its underlying closed fibre is the original proper curve. Properness is invariant under nilpotent thickenings for a finitely presented separated morphism; separatedness likewise lifts across the nilpotent base extension. The geometric fibres of the lifted family are the original geometric fibres, because an Artinian nilpotent extension does not change the residue fields. They are still nodal and one-dimensional. Thus the lift is an object of \(\mathcal N(A')\), as required. \(\square\)

At a field-valued nodal curve \(C/k\) with \(\delta\) nodes, (4.8) also gives the exact sequence
\[
0\longrightarrow H^1(C,T_C)
\longrightarrow \operatorname{Ext}^1(L_{C/k},\mathcal O_C)
\longrightarrow k^\delta
\longrightarrow H^2(C,T_C)=0.
\tag{4.9}
\]
Each coordinate of \(k^\delta\) is a smoothing direction (4.4). The surjectivity says that prescribed first-order smoothing directions at all nodes can be realized globally. Merely observing \(H^2(T_C)=0\) would not establish Proposition 4.1: the term \(H^1(\mathcal T^1(M))\) also had to vanish.

### 4.3. From infinitesimal lifts to smoothness

**Theorem 4.2.** The nodal stack \(\mathcal N\) is smooth over \(\mathbb Z\).

**Proof.** The stack is algebraic and locally of finite presentation by Sections 1–2. We spell out the infinitesimal-to-geometric step so that the assertion includes every characteristic.

Let \(C/k\) be a geometric point, with \(k\) algebraically closed. In characteristic zero take the complete local coefficient ring \(\Lambda=k\). In characteristic \(p>0\), take \(\Lambda=W(k)\), the Witt discrete valuation ring, with residue field \(k\). The maps \(\mathbb Q\to k\) and \(\mathbb Z_{(p)}\to W(k)\), respectively, are faithfully flat. We work over \(\Lambda\), where the point has residue field \(k\), a finite-type field over this local base.

Choose a smooth scheme atlas \(U\to\mathcal N_\Lambda\) and a \(k\)-point \(u\) above \(C\); one exists after taking an affine open in the nonempty smooth atlas fibre. Given a marked infinitesimal deformation of \(u\) over an Artinian \(\Lambda\)-algebra \(A\), Proposition 4.1 lifts its underlying curve across any square-zero \(A'\to A\). Smoothness of \(U\to\mathcal N_\Lambda\) then lifts the map to the atlas, together with its given reduction and identifying arrow. Thus the formal deformation functor of \(u\) is unobstructed.

For a scheme locally of finite presentation over the Noetherian local ring \(\Lambda\), with a point of residue field \(k\), this Artinian lifting test says that its completed local ring at that point is formally smooth over \(\Lambda\); the ordinary local criterion then says the scheme is smooth at that point. Equivalently apply the versal-ring criterion whose atlas proof was given in Lesson 7. The finite-type residue-field hypothesis is satisfied here. Hence \(U\) is smooth over \(\Lambda\) at \(u\), and \(\mathcal N_\Lambda\) is smooth at \(C\).

Smoothness at a point descends along the indicated faithfully flat local base change. In characteristic zero the local ring of the base at the image point is \(\mathbb Q\), so smoothness over \(\mathbb Q\) is exactly the local test for smoothness over \(\mathbb Z\) there. We have proved it at every geometric point of \(\mathcal N\). Its smooth locus is consequently the whole stack. \(\square\)

This proves [Stacks, Tag 0E00], using both the local node and the global gluing calculation. Since smooth curves are nodal, their open substacks are smooth too. In particular \(\mathcal M_g\) is smooth over \(\mathbb Z\), [Stacks, Tag 0E84].

## 5. Dualizing sheaves and stability

### 5.1. Prestable and semistable families

A **prestable** family is a nodal family satisfying (2.3). Equivalently its geometric fibres are reduced, connected nodal curves of dimension one. The equivalence follows from Lemma 2.1 and the global-functions calculation for reduced curves. Thus
\[
\mathcal P=\mathcal N\cap\mathcal{Curves}^{\mathrm{grc},1},
\qquad
\mathcal P_g=\mathcal P\cap\mathcal{Curves}_g
\tag{5.1}
\]
are open algebraic stacks and are smooth over \(\mathbb Z\) by Theorem 4.2. This proves [Stacks, Tags 0E6S and 0E6H] for prestable curves and their genus pieces.

For a prestable family \(f:X\to S\), ordinary relative duality for proper flat Gorenstein curves supplies an invertible dualizing sheaf \(\omega_{X/S}\). It commutes with arbitrary base change:
\[
\omega_{X_T/T}\simeq \omega_{X/S}|_{X_T}.
\tag{5.2}
\]
Its relative dualizing complex is \(\omega_{X/S}[1]\). The exact duality input, including arbitrary-base formation, is recorded in Section 9; see [Stacks, Tag 0E6N].

Over an algebraically closed field, let \(\nu:\coprod_v C_v\to C\) be the normalization of a prestable curve. Each \(C_v\) is smooth and proper. Let \(D_v\) be the reduced divisor of preimages of nodes on \(C_v\), and write \(n_v=\deg D_v\). Locally at a node a dualizing form is
\[
\frac{dx}{x}=-\frac{dy}{y}.
\tag{5.3}
\]
Thus a section of \(\omega_C\) is a meromorphic differential on the normalization with at most simple poles at node branches, whose two residues at each node sum to zero. Away from the nodes it is an ordinary regular differential. The local module in (5.3) is free of rank one, and its restriction to either branch is the logarithmic canonical module. Gluing these local descriptions proves
\[
\nu^*\omega_C|_{C_v}\simeq\omega_{C_v}(D_v),
\qquad
\deg(\nu^*\omega_C|_{C_v})=2g_v-2+n_v.
\tag{5.4}
\]
The sign in (5.3) means opposite residues also in characteristic two, where opposite and equal coincide. A self-node has two preimages on the same \(C_v\), and contributes **two** to \(n_v\).

A **rational tail** is a smooth rational component meeting the rest of the curve in one point. A **rational bridge** is one meeting the rest in two points. For \(g\geq1\), a prestable curve is **semistable** here if it has no rational tail; bridges are permitted. These conventions are those of [Stacks, Tags 0E6X and 0E73].

Semistability is open in \(\mathcal P\). We include the family argument. Fix \(m\geq2\). For a nodal curve with no rational tails, the ordinary curve global-generation theorem says that \(\omega^m\) is globally generated if \(g\geq2\), and \(\omega\simeq\mathcal O\) if \(g=1\), [Stacks, Tag 0E3K]. This is a line-bundle theorem on an individual curve, not an openness theorem about moduli.

For \(g\geq2\), (5.4) makes \(\omega\) have nonnegative degree on every normalized component, with positive total degree \(2g-2\). Consequently \(H^0(C,\omega^{1-m})=0\). To see this, on a negative-degree component the section is zero; on a degree-zero component a nonzero section would have no zeros. At a node adjoining a zero section it must vanish, and connectedness propagates that vanishing to every degree-zero component. Duality gives \(H^1(C,\omega^m)=0\). Proper flat perfect cohomology therefore makes \(f_*\omega^m\) finite locally free with base change near this fibre, and evaluation
\[
f^*f_*\omega^m\longrightarrow\omega^m
\tag{5.5}
\]
is surjective on the fibre. Its finite cokernel vanishes on an open containing that fibre. Removing its proper bad-locus image makes (5.5) surjective on a neighbourhood of the base point. Such fibres cannot have a tail: restriction of \(\omega^m\) to a tail has degree \(-m\), contradicting global generation.

For \(g=1\), Lemma 2.1 and relative duality give
\[
Rf_*\omega_{X/S}\simeq
(Rf_*\mathcal O_X)^\vee[-1]
\simeq E^\vee[0]\oplus\mathcal O_S[-1],
\qquad \operatorname{rank}E=1.
\]
Thus \(f_*\omega\) is locally free of rank one with every base change, even on a nonreduced base. A local generator evaluates to a nowhere-zero section on the tail-free fibre, since \(\omega\) there is trivial. Remove the proper image of its zero locus to make \(\omega\) trivial on the whole neighbouring family. These fibres also have no tails by (5.4). Conversely any tail prevents (5.5), or triviality of \(\omega\), respectively. These characterizations are geometric and commute with base change, so the constructed semistable locus is a universal open.

### 5.2. The numerical criterion

The dual graph has a vertex \(v\) of weight \(g_v\) for each normalized component and an edge for each node, with loops for self-nodes. If it has \(V\) vertices and \(E\) edges, connectedness and the normalization sequence give
\[
0\to\mathcal O_C\to\nu_*\mathcal O_{\widetilde C}
\to\bigoplus_{\text{nodes}}k\to0,
\qquad
g=\sum_v g_v+E-V+1.
\tag{5.6}
\]
The last map subtracts the two branch values. Taking Euler characteristics proves the formula. The valence \(n_v\) counts loops twice, exactly as in (5.4).

**Lemma 5.1.** For a prestable curve \(C\) of genus \(g\geq2\) over a field, the following are equivalent:

1. Its geometric fibre has no rational tail or rational bridge.
2. \(2g_v-2+n_v>0\) for every vertex of its geometric dual graph.
3. \(\omega_C\) is ample.

**Proof.** Work over an algebraic closure; ampleness can be checked after a field extension. For \(g_v\geq2\) the number in (2) is positive. If \(g_v=1\), it is positive unless \(n_v=0\); that exception makes the component the whole connected curve and gives \(g=1\), excluded here. For \(g_v=0\), positivity means \(n_v\geq3\).

Consider a rational-normalization vertex with \(n_v\leq2\). If there is no self-node, its image is a smooth rational component. Valence zero would make it the whole genus-zero curve; valence one gives a tail and valence two a bridge. If it has a self-node, that loop already consumes both branches. There are no external edges, so it is the entire connected curve, of genus one by (5.6). This too is excluded. Therefore, at genus at least two, failure of positivity is exactly a rational tail or bridge. This proves (1) equivalent to (2), including irreducible self-nodal curves.

An invertible sheaf on a proper reduced curve is ample if and only if its degree on each irreducible component is positive. Equivalently test its pullback to the finite surjective normalization, where the assertion is the usual smooth-curve degree criterion; ampleness both ascends and descends through a finite surjection. Applying this to (5.4) proves (2) equivalent to (3). \(\square\)

A prestable genus-\(g\) curve with these properties is **stable**. This recovers Deligne–Mumford's original Definition 1.1 for \(g\geq2\): every nonsingular rational component must meet the other components in more than two points. The normalization argument explains why the original condition also handles singular rational components.

### 5.3. Stability in an arbitrary family

**Theorem 5.2 (neighbourhood criterion).** Let \(f:X\to S\) be a prestable family of genus \(g\geq2\), and let \(s\in S\). Then
\[
X_s\text{ has no geometric rational tails or bridges}
\quad\Longleftrightarrow\quad
\omega_{X/S}|_{f^{-1}(U)}\text{ is ample over }U
\tag{5.7}
\]
for some open neighbourhood \(U\) of \(s\). No Noetherian hypothesis on \(S\) is required.

**Proof.** By (5.2) the restriction of the relative dualizing sheaf to \(X_s\) is its dualizing sheaf. If the left side holds, Lemma 5.1 makes this restriction ample. The ordinary relative-ampleness theorem for a proper finitely presented algebraic-space morphism then gives an open \(U\) on which \(\omega_{X/S}\) is relatively ample, [Stacks, Tag 0D3D]. Conversely relative ampleness restricts to ampleness on \(X_s\), and Lemma 5.1 excludes its tails and bridges. This proves both directions of [Stacks, Tag 0E74]. \(\square\)

**Corollary 5.3.** The stable genus-\(g\) stack \(\overline{\mathcal M}_g\) is open in \(\mathcal{Curves}\), and it is smooth over \(\mathbb Z\).

**Proof.** Within \(\mathcal P_g\), take the union of the neighbourhoods supplied by Theorem 5.2. Its points are exactly the stable fibres. By (5.2) and the geometric criterion of Lemma 5.1, this open commutes with every base change. Section 2.1 makes it an open substack. Since \(\mathcal P_g\) is itself open in \(\mathcal N\), it is also open in \(\mathcal{Curves}\). Theorem 4.2 gives smoothness. This proves [Stacks, Tags 0E76 and 0E79]. \(\square\)

The definitions and argument also identify stable families as prestable families of genus at least two with relatively ample dualizing sheaf, [Stacks, Tags 0E73 and 0E75]. This is a statement over every base, not only over fields.

## 6. Automorphisms, dimension and formal coordinates

### 6.1. Vector fields on the normalization

**Lemma 6.1.** For a nodal curve over an algebraically closed field,
\[
T_C\simeq\nu_*\!\left(\bigoplus_v T_{C_v}(-D_v)\right).
\tag{6.1}
\]
In particular a stable curve of genus at least two has \(H^0(C,T_C)=0\).

**Proof.** Away from nodes, normalization is an isomorphism and there is nothing to check. At a completed node write its ring as
\[
k[[x]]\times_k k[[y]]
=\{(a(x),b(y)):a(0)=b(0)\}.
\tag{6.2}
\]
A derivation is determined by \(D(x)\) and \(D(y)\). The equation \(D(xy)=yD(x)+xD(y)=0\) forces the \(y\)-branch value of \(D(x)\) and the \(x\)-branch value of \(D(y)\) to be zero. The matching-constant condition then forces their other values to be divisible by \(x\) and \(y\), respectively. Conversely any \(x a(x)\partial_x\) and \(y b(y)\partial_y\) define a derivation of (6.2). Thus branch vector fields must vanish at their respective preimages of the node. This describes exactly the right side of (6.1). The local identifications agree off the nodes, and equality of these coherent modules can be tested after the faithfully flat completions of their local rings. They therefore glue to (6.1).

The degree of the line bundle in its \(v\)-summand is
\[
\deg T_{C_v}(-D_v)=2-2g_v-n_v.
\tag{6.3}
\]
On a stable curve every such degree is negative by Lemma 5.1. A negative-degree line bundle on a smooth proper curve has no nonzero section: the zero divisor of a nonzero section would have nonnegative degree equal to the degree of the bundle. Taking sections of (6.1) proves the claim. \(\square\)

**Theorem 6.2.** The stack \(\overline{\mathcal M}_g\), \(g\geq2\), is Deligne–Mumford. For a geometric prestable curve of genus at least two, stability is equivalent to its automorphism group being unramified, and equivalent to its automorphism group being finite.

**Proof.** For a stable geometric curve, (3.4) and Lemma 6.1 give zero tangent space at the identity. Lemma 3.1 makes its automorphism group unramified. In a stable family, the fibre of \(V\) in (3.1) is zero at every geometric point; Nakayama gives \(V=0\). By Theorem 3.2 the entire stable open factors through \(\mathcal D\), hence is Deligne–Mumford. This proves [Stacks, Tag 0E7A].

Over a field, an unramified finite-type group algebraic space is finite étale. Indeed its geometric fibres have dimension zero and are reduced. A zero-dimensional finite-type algebraic space over a field is a scheme, and a zero-dimensional finite-type scheme has finitely many points and is finite over that field. Unramifiedness then says its residue extensions are separable. These are ordinary zero-dimensional space facts from Lesson 2.

Conversely, if a genus-at-least-two prestable curve is unstable, Lemma 5.1 gives a smooth rational tail or bridge. On a tail the subgroup of \(\operatorname{PGL}_2\) fixing its one attachment point has dimension two. On a bridge, the subgroup fixing its two attachment points is \(\mathbb G_m\), of dimension one. Every member extends by the identity on all other components. To verify the extension for a whole group scheme, use the branch fibre-product algebra (6.2): a pointed automorphism preserves the evaluation at each attaching point, so it induces an automorphism of the glued ring after every base change. It therefore acts on the glued curve, and the action is faithful because it is faithful on that component. These subgroups make the automorphism group positive-dimensional, hence neither finite nor unramified. This proves all the stated equivalences. \(\square\)

The theorem allows a finite étale automorphism group whose order is divisible by the residue characteristic. It uses no averaging argument. In a family, we have proved that the automorphism space is separated, finitely presented and unramified; its finiteness over the whole base will follow from the proper diagonal in Lesson 10, rather than from finiteness of its individual fibres alone.

### 6.2. Smooth curves and their dimension

**Theorem 6.3.** For \(g\geq2\), \(\mathcal M_g\) is a Deligne–Mumford stack, smooth over \(\mathbb Z\), of relative dimension \(3g-3\).

**Proof.** A smooth proper geometrically connected genus-\(g\) curve has ample dualizing sheaf, of degree \(2g-2>0\). Hence it is stable. Definition (2.5) makes \(\mathcal M_g\) an open substack of \(\overline{\mathcal M}_g\), so Theorem 6.2 gives the Deligne–Mumford property. Theorem 4.2 gives smoothness.

For a geometric fibre \(C/k\), its tangent sheaf is a line bundle of degree \(2-2g<0\). Thus \(H^0(C,T_C)=0\). Riemann–Roch says
\[
\chi(T_C)=\deg T_C+1-g=3-3g,
\qquad h^1(C,T_C)=3g-3.
\tag{6.4}
\]
The cotangent deformation theorem identifies \(H^1(C,T_C)\) with its first-order marked deformations. In an étale scheme atlas of the Deligne–Mumford stack, lifting the point across the dual numbers is unique once the curve deformation and reduction of the atlas point are specified. Thus its relative tangent space is precisely this vector space. A smooth morphism has relative dimension equal to its geometric relative tangent dimension. This proves the dimension at every point and completes the theorem. \(\square\)

The smoothness and open inclusion correspond to [Stacks, Tags 0E84 and 0E87]. Smoothness here includes lifting curves from characteristic \(p\) across mixed-characteristic Artinian coefficient extensions.

### 6.3. A universal ring for marked deformations

Let \(k\) be algebraically closed and \(\Lambda\) a complete Noetherian local ring with residue field \(k\). For a fixed curve \(C/k\), let \(\operatorname{Def}_C(A)\) denote classes of flat proper finitely presented \(A\)-curves equipped with an identification of their closed fibre with \(C\), for Artinian local \(\Lambda\)-algebras \(A\) with residue field \(k\). Isomorphisms must respect that identification.

**Theorem 6.4.** If \(C\) is smooth, proper and connected of genus \(g\geq2\), the marked functor is prorepresented by
\[
R_C\simeq\Lambda[[u_1,\ldots,u_{3g-3}]].
\tag{6.5}
\]
The isomorphism depends on choices of parameters.

**Proof.** We verify the hypotheses of the ordinary Schlessinger prorepresentability theorem, rather than import the formal moduli conclusion.

First there are no automorphisms of a marked deformation that reduce to the identity. Filter the maximal ideal of an Artinian coefficient algebra by powers, and refine to small extensions with kernel killed by the maximal ideal. If the automorphism is already the identity on the quotient, its possible difference at the next step is
\[
H^0(C,T_C)\otimes_k I=0
\tag{6.6}
\]
by the infinitesimal automorphism formula. Induction through the finite filtration proves it is the identity. Hence any isomorphism between two marked deformations, if it exists, is unique.

Next verify infinitesimal patching, including identifying arrows. For a ring fibre product \(B=A_1\times_{A_0}A_2\), take \(A_2\to A_0\) to be a small extension; this is the case needed in Schlessinger's tests. Deformations over the \(A_i\) are nilpotent thickenings of the same \(C\). The inverse image of each affine open in \(C\) is affine. Their coordinate algebras are flat over their Artinian bases. The flat-module fibre-product patching proved in Lesson 8, Lemma 3.1, makes their fibre-product algebra flat over \(B\), with exactly the specified base-change isomorphisms. Units, multiplication, localization on principal overlaps and all homomorphisms patch with it.

Finite presentation also holds. Lift finitely many algebra generators from the quotient by the square-zero kernel \(J=\ker(B\to A_1)\). Nilpotent Nakayama shows they generate the patched algebra. Map a polynomial algebra on those generators onto it. Its kernel is \(B\)-flat, since source and quotient are \(B\)-flat, and its reduction modulo \(J\) is the finitely generated relation ideal of the \(A_1\)-algebra. Lifting those relations and using \(J^2=0\) shows the kernel finitely generated. The local algebras therefore glue to a finitely presented flat scheme. Its closed fibre is \(C\), and separatedness and properness persist across the nilpotent base extension. This gives an equivalence of the full deformation groupoids over the fibre product.

Taking isomorphism classes now gives a bijection
\[
\operatorname{Def}_C(B)\xrightarrow{\ \sim\ }
\operatorname{Def}_C(A_1)\times_{\operatorname{Def}_C(A_0)}
\operatorname{Def}_C(A_2).
\tag{6.7}
\]
The point needing care is injectivity: equality on \(A_0\) supplies a unique marked isomorphism by (6.6), so there is no choice of a different gluing arrow. Full faithfulness of patching then gives the unique comparison over \(B\). In particular (6.7) proves Schlessinger's fibre-product axioms, including its prorepresentability axiom for a small extension on both sides.

The tangent space is \(H^1(C,T_C)\), finite-dimensional by properness. Also \(\operatorname{Def}_C(k)\) is a singleton. The ordinary Schlessinger prorepresentability theorem [Stacks, Tag 06JM] now provides a complete Noetherian local prorepresenting \(\Lambda\)-algebra \(R_C\) with residue field \(k\). In its stated version one also asks that the map \(\operatorname{Der}_\Lambda(k,k)\to T\operatorname{Def}_C\) be injective; its source is zero because \(\Lambda\to k\) is surjective. Its relative tangent dimension is \(3g-3\) by (6.4).

Finally Proposition 4.1 shows the functor unobstructed; on a smooth closed fibre any lifted family is smooth, since that condition is a universal open containing the only base point. Thus the prorepresenting ring is formally smooth over \(\Lambda\). A complete Noetherian local formally smooth algebra with the same residue field as \(\Lambda\) is a power-series algebra over \(\Lambda\); the number of variables is its relative tangent dimension. Applying that ordinary complete-local-ring theorem gives (6.5). \(\square\)

This proves the confirmed untagged result [AI Integrated Stacks Project, examples-defos.tex, lemma-smooth-proper-curve-formal-moduli-dimension] in genus at least two. “Marked” matters: a finite automorphism of \(C\) that acts nontrivially on the marking remains an automorphism in the moduli stack, even though it is absent from this formal functor.

### 6.4. Boundary tangent spaces and smoothing all nodes

For a stable nodal \(C/k\), apply Riemann–Roch to (6.1). With \(\delta=E\) nodes, (5.6) gives
\[
\chi(T_C)=\sum_v(3-3g_v-n_v)=3-3g+\delta.
\]
Since \(H^0(T_C)=0\), (4.9) implies
\[
h^1(T_C)=3g-3-\delta,\qquad
\dim_k\operatorname{Ext}^1(L_{C/k},\mathcal O_C)=3g-3.
\tag{6.8}
\]
The first space moves the components with their attaching branches; the extra \(\delta\) directions smooth the nodes. Thus every stable boundary point has the same total tangent dimension as the smooth locus.

The marked-ring proof of Theorem 6.4 applies to stable nodal curves as well: Lemma 6.1 eliminates automorphisms, (6.7) still holds, and Proposition 4.1 eliminates obstructions. Its ring \(R\) over \(k\) is a power-series ring in \(3g-3\) variables. The universal marked deformations over \(R/\mathfrak m_R^n\) have compatible dualizing bundles, ample on the special fibre.

Algebraize this system over \(R\) using the precise ordinary formal projective existence theorem [Stacks, Tag 089A]: a cartesian proper formal family with a compatible line bundle ample on its special fibre, over a complete Noetherian local ring, is the completion of a proper projective family. Flatness of the algebraization follows from the infinitesimal flatness criterion and its proper closed nonflat-locus image, as in Lesson 8, Proposition 4.2. Its closed fibre is \(C\). The universal stable open contains the closed point of the local base, so the whole algebraized family is stable.

Now the ordinary completed local-structure theorem applies to this actual Noetherian family. At the \(i\)-th original node its completed ring has relation \(x_i y_i-a_i\), with \(a_i\in R\). Equation (4.9) says that the linear parts of the \(a_i\) are independent in \(\mathfrak m_R/\mathfrak m_R^2\). Complete them to a basis; the formal inverse function theorem lets us use the \(a_i\) themselves among the parameters of \(R\). The continuous ring map \(R\to k[[t]]\) sending every \(a_i\) to \(t\) and the other parameters to zero pulls back the algebraized family to a proper flat stable curve over \(k[[t]]\).

Its generic fibre is smooth. To check this last statement beyond formal neighbourhoods, the relative nonsmooth locus is closed and proper. A nonsmooth generic point would specialize to one of the original nodes. At that node the completed family has \(xy=t\), whose nonsmooth locus is contained in \(t=0\): the relative Jacobian equations \(x=y=0\) also impose \(t=0\). Faithfully flat completion therefore leaves no generic nonsmooth point specializing there. This is a contradiction. The family remains prestable of genus \(g\) and stable by the universal open criteria, since their opens contain the closed point of the local base.

Every stable geometric point is consequently a specialization of a smooth point. In particular \(\mathcal M_g\) is dense in \(\overline{\mathcal M}_g\), as in [Stacks, Tag 0E87]. This argument supplies a deformation of the curve; it does not assert that different curves have the same smoothing or that the stack has a global universal deformation scheme.

### 6.5. The larger isolated-lci locus

Let \(\mathcal L^+\) be the intersection of the local-complete-intersection open and the finite-nonsmooth-locus open of Section 2.1. It still permits disconnected, nonreduced and zero-dimensional components.

**Proposition 6.5.** The full smooth locus is open and dense in \(\mathcal L^+\), [Stacks, Tag 0E85].

**Proof.** It is already open. To prove density, take a field-valued object \(C/k\) of \(\mathcal L^+\). It is a projective scheme by the ordinary dimension-at-most-one theorem. Since it is Cohen–Macaulay, its zero-dimensional and pure-one-dimensional parts are open and closed.

We use two exact local algebra inputs: a finite-dimensional lci \(k\)-algebra admits a finite flat deformation over \(k[[t]]\) with étale generic fibre [Stacks, Tag 0E7W]; and an essentially finite-type lci local ring of dimension one at a closed point admits a flat deformation \(B_i/k[[t]]\) with
\[
t^{N_i}\in\operatorname{Fitt}_1
(\Omega_{B_i/k[[t]]})
\tag{6.9}
\]
for some \(N_i\), with the specified special local ring [Stacks, Tag 0E7X]. The Fitting bound says that this local deformation is smooth after inverting \(t\). These are ordinary local complete-intersection smoothing results; we now prove how they give the claimed global density.

The first input treats the zero-dimensional part. On the pure-one-dimensional part there are only finitely many nonsmooth closed points \(p_i\). The computation of Section 4.2 applies with “lci with isolated nonsmooth points” in place of “nodal”: its cotangent complex still has amplitude \([-1,0]\), its degree-one sheaf is still supported at these finite points, and its degree-zero sheaf still has zero \(H^2\). Thus every Artinian infinitesimal lift exists.

Moreover arbitrary specified local lifts at the \(p_i\) can be realized by a global lift. The local-to-global exact sequence makes
\[
\operatorname{Ext}^1(L_{C/A},M)
\longrightarrow H^0(\mathcal T^1(M))
\tag{6.10}
\]
surjective. The right side is the product of the local degree-one deformation modules at those points, since its support is finite over the Artinian base. Choose any global lift. Its restrictions differ from the prescribed local lifts by classes in that product. Lift those differences through (6.10) and change the global lift by the resulting torsor element. Its restrictions are now isomorphic to the prescribed lifts, respecting their given reductions. This proves smoothness of the global-to-local deformation map, with the identifying arrows retained.

Apply this successively to the local systems \(B_i/t^nB_i\). We obtain a compatible global formal curve \(C_n\) over \(k[[t]]/(t^n)\), with compatible local identifying isomorphisms. An ample line bundle on the special fibre lifts successively because \(H^2(\mathcal O_C\otimes I)=0\). The compatible line bundles and curves algebraize by Tag 089A to a projective family \(Y/k[[t]]\); its infinitesimal reductions are flat, so the flatness argument of Section 6.4 proves \(Y\) flat.

Its generic fibre is smooth. The relative lci and pure-one-dimensional loci contain the special fibre; removing their proper bad-locus images, which miss the closed point of the local base, shows that this part of \(Y\) is a flat lci family of relative dimension one. Near \(p_i\), compatibility of the reductions identifies the completed relative differential modules with the inverse system from \(B_i\). Fitting ideals commute with reduction. Thus (6.9) holds in the \(t\)-adic completion of the local ring of \(Y\), and descends to that local ring by faithful flatness of Noetherian completion. The nonsmooth locus near \(p_i\) is cut out by this first Fitting ideal, so it has no point with \(t\) invertible there. At an originally smooth point, openness of smoothness gives the same conclusion. Properness forces every nonsmooth generic point to specialize to a special-fibre point, so none exists. Combining with the finite flat deformation of the zero-dimensional part gives a projective flat smoothing of all of \(C\).

The classifying trait lies in \(\mathcal L^+\): this universal open contains its closed point, hence the whole local trait. Its generic point lies in the full smooth locus, and its closed point is the original object. Every point of \(\mathcal L^+\) is therefore in the closure of that smooth locus, proving density. \(\square\)

## 7. Examples

### 7.1. Two genus-two stable curves

Let \(E_1,E_2\) be smooth elliptic curves over an algebraically closed field, with chosen points \(p_1,p_2\). Identify those points transversely. The resulting proper nodal curve has two weight-one vertices and one edge. Formula (5.6) gives \(g=1+1+1-2+1=2\), and (5.4) gives degree one on each component. It is stable. Its automorphisms cannot translate either elliptic component freely, since they must preserve the attaching point; component exchanges may occur if the pointed elliptic components are isomorphic.

Alternatively choose four distinct points \(a,b,c,d\) on \(\mathbb P^1\), identify \(a\) with \(b\) and \(c\) with \(d\), and form the nodal gluing. The resulting curve is irreducible with two nodes. Its graph has one weight-zero vertex and two loops, so \(g=0+2-1+1=2\). Its normalized dualizing bundle is
\[
\omega_{\mathbb P^1}(a+b+c+d)\simeq\mathcal O_{\mathbb P^1}(2).
\tag{7.1}
\]
It is stable. Automorphisms lift to \(\mathbb P^1\) and preserve the unordered two pairs of attaching points. They form a finite group because a projective transformation is determined by its action on three distinct points. This finite group may be nontrivial.

The constructions are algebraic gluings: at each identified pair, the local functions are pairs of branch functions with equal value, as in (6.2). These rings make ordinary nodes, not cusps. The following data distinguish the two examples:

| Curve | Normalization | Graph edges | Branch counts | Dualizing degrees |
|---|---|---:|---|---|
| Two elliptic components joined once | \(E_1\amalg E_2\) | \(1\) | \((1,1)\) | \((1,1)\) |
| One rational component with two self-nodes | \(\mathbb P^1\) | \(2\) loops | \(4\) | \(2\) |

Their tangent spaces both have dimension three. In the first example (6.8) gives two directions preserving the node and one smoothing it; in the second it gives one direction preserving the two nodes and two smoothing them.

### 7.2. Adding a tail or inserting a bridge

Attach a new \(\mathbb P^1\) to a stable curve at one smooth point. This adds one vertex and one edge and leaves the genus unchanged. The new component has dualizing degree \(-1\), so the curve is prestable and unstable; its automorphism group contains the two-dimensional subgroup fixing the one attachment.

Starting instead at a node of a stable curve, separate its two branches and insert a \(\mathbb P^1\) between them. Removing one edge and adding two edges and a vertex again preserves the genus. The inserted component has dualizing degree zero and carries the \(\mathbb G_m\) subgroup fixing both attachments. This curve is semistable and unstable. If one simply attaches a bridge between two previously distinct smooth points without removing an old edge, the graph gains a cycle and the genus increases by one; these are different constructions.

### 7.3. The low-genus automorphisms

For \(\mathbb P^1\), the full automorphism scheme is \(\operatorname{PGL}_2\), smooth of dimension three, and \(T_{\mathbb P^1}\simeq\mathcal O(2)\) has three global sections. For a smooth connected genus-one curve over an algebraically closed field, choose one point to identify it with an elliptic curve. Translation embeds the elliptic curve into its unpointed automorphism group, of dimension one. Its tangent bundle is trivial, so \(h^0(T)=1\), agreeing with (3.4).

More explicitly, any automorphism of the genus-one curve is a translation followed by an automorphism fixing the chosen point. The pointed subgroup has zero tangent space, because \(H^0(T(-p))=0\), and is finite by the same degree-zero-space argument as in Theorem 6.2. Thus the full group has exactly dimension one. These examples prove the positive-dimensional assertions of [Stacks, Tag 0DSV]. They explain the genus restriction in Theorem 6.3 without assuming a section for a general genus-one family.

## 8. Exercises and solutions

**Exercise 8.1 (easy: Riemann–Roch).** Let \(C/k\) be a smooth projective geometrically connected curve of genus \(g\geq2\). Prove \(H^0(C,T_C)=0\) and \(\dim_kH^1(C,T_C)=3g-3\).

**Solution.** Its canonical line bundle has degree \(2g-2\), so \(T_C=\omega_C^{-1}\) has degree \(2-2g<0\). A nonzero section of a line bundle on a smooth proper integral curve determines an effective zero divisor of degree equal to the degree of that bundle. A negative degree is impossible; hence \(h^0(T_C)=0\). Riemann–Roch gives \(h^0(T_C)-h^1(T_C)=2-2g+1-g=3-3g\), and therefore \(h^1(T_C)=3g-3\). A field extension does not change these cohomology dimensions, so one may first pass to an algebraic closure without changing the answer.

**Exercise 8.2 (medium: unstable automorphisms).** Let \(C\) be a prestable genus-at-least-two curve over an algebraically closed field with a rational tail or bridge. Prove that \(\operatorname{Aut}(C)\) has positive dimension.

**Solution.** For a tail, choose a coordinate making its one attachment \(\infty\). The affine transformations \(z\mapsto az+b\), \(a\in\mathbb G_m,\ b\in\mathbb A^1\), form a smooth group of dimension two fixing that point. For a bridge, make its attachments \(0,\infty\); the transformations \(z\mapsto az\) form \(\mathbb G_m\), of dimension one.

Extend every transformation by the identity on the other normalized components. At each node, regular functions are pairs of branch functions with equal value at the attaching points. The transformation preserves those values, so it preserves this subalgebra and defines an automorphism of the whole curve. This verification is valid after an arbitrary base change; it gives a group-scheme morphism into \(\operatorname{Aut}(C)\). Its kernel is trivial because restriction to the chosen component is faithful. A homomorphism of finite-type algebraic groups with zero-dimensional kernel has image of the same dimension as its source, by the fibre-dimension theorem applied after field extension. Thus the automorphism group has dimension at least two or one, respectively. In particular it cannot be unramified or finite.

**Exercise 8.3 (medium: openness of stability).** Deduce openness of stability in a prestable genus-\(g\) family, \(g\geq2\), from Theorem 5.2.

**Solution.** Let \(S^{\mathrm{st}}\) be the set of points whose geometric fibres have no rational tail or bridge. At each \(s\in S^{\mathrm{st}}\), Theorem 5.2 gives an open \(U_s\) containing \(s\) on which \(\omega_{X/S}\) is relatively ample. Its restriction to every fibre over \(U_s\) is ample. The converse implication of that theorem, or Lemma 5.1, shows \(U_s\subset S^{\mathrm{st}}\). Thus \(S^{\mathrm{st}}=\bigcup_s U_s\) is open.

After any \(T\to S\), formula (5.2) pulls back the dualizing sheaf. Stability of a fibre is unchanged by extending its residue field, so \(T^{\mathrm{st}}=T\times_S S^{\mathrm{st}}\). The construction is invariant under every family isomorphism. Consequently the inclusion of stable families is represented by this open on every test scheme, proving an open immersion of stacks, including arbitrary non-Noetherian bases.

**Exercise 8.4 (hard: the node and global smoothness).** Prove that the stack of nodal curves is smooth over \(\mathbb Z\), starting from \(xy=t\).

**Solution.** The node \(R=k[[x,y]]/(xy)\) has completed cotangent complex \([R\to R^2]\), with map \(1\mapsto(y,x)\). Its dual has cokernel \(k\), kernel the branch derivations vanishing at the node, and no cohomology in degree two. The relation \(xy-\epsilon c\) realizes its degree-one class \(c\). A lift of its smoothing coefficient in \(A[[x,y]]/(xy-a)\) across \(A'\to A\) gives a flat local deformation, because the polynomial node model has the free normal-form basis from Section 4.1 and its completed version is adically flat over the Artinian base.

Local lifts must be glued. For a proper nodal family \(C/A\) over an Artinian base and a square-zero kernel \(I\), set \(M=\mathcal O_C\otimes_A I\). Since \(L_{C/A}\) is locally free in degrees \(-1,0\), its sheaf Ext groups vanish in degree at least two. Its degree-one sheaf vanishes on the smooth locus, and is supported at the finitely many special-fibre nodes. The supporting closed subspace is proper and quasi-finite over \(A\), hence finite and affine; therefore \(H^1(\mathcal T^1(M))=0\). Meanwhile \(H^2(\mathcal T^0(M))=0\) by one-dimensional coherent cohomology.

These are all the total-degree-two terms in the local-to-global spectral sequence, so \(\operatorname{Ext}^2(L_{C/A},M)=0\). The cotangent deformation theorem now glues a marked flat lift. It is finitely presented and proper, and its geometric fibres remain nodal since the base extension is nilpotent. Thus the nodal stack is unobstructed for every Artinian square-zero extension, including extensions of mixed characteristic.

Finally the stack is algebraic and locally of finite presentation. At a geometric point use \(\Lambda=k\) in characteristic zero and \(\Lambda=W(k)\) in characteristic \(p\). A smooth scheme atlas over \(\Lambda\) lifts both the curve and the atlas point across every Artinian extension, so its completed local ring is formally smooth over \(\Lambda\). The ordinary local infinitesimal criterion gives a smooth atlas neighbourhood over \(\Lambda\). Faithfully flat local descent to \(\mathbb Q\) or \(\mathbb Z_{(p)}\), respectively, gives smoothness over \(\mathbb Z\) at the original point. Since every point is covered, the whole nodal stack is smooth. This solution accounts for both (4.6) and (4.7); the node parameter alone would not have supplied the global gluing argument.

## 9. Precise prerequisites and source notes

The following ordinary results are used with their indicated hypotheses. They do not contain the moduli conclusions proved in this lesson.

- A proper algebraic space of dimension at most one over a field is a scheme; a proper scheme of that dimension is projective. A nilpotent thickening of a scheme by an algebraic space is a scheme. Proposition 1.1 also uses the existence of étale local sections of a smooth surjection and the relative ample-bundle projectivity criterion.
- For a flat finitely presented morphism, the relative Cohen–Macaulay, Gorenstein, local-complete-intersection, smooth and nodal loci are open and have arbitrary base-change compatibility. Nodal includes pure relative dimension one [Stacks, Tag 0DSH]. For a proper flat finitely presented morphism, geometric reducedness is open, and the dimension-one fibre locus is open. The separation of relative dimensions in the Cohen–Macaulay and smooth cases is the ordinary relative-dimension locus theorem.
- Proper flat perfect direct image of a relatively perfect complex commutes with every derived base change; in particular it applies to a line bundle and to \(\mathcal O_X\). Finite perfect complexes detect cohomology dimensions and rank locally. Coherent sheaves on a Noetherian scheme of dimension one have no cohomology in degrees at least two. These are the same cohomology inputs used in Lessons 7–8.
- Proper flat Gorenstein curve duality gives \(\omega_{X/S}[1]\), with an invertible \(\omega_{X/S}\) and formation under arbitrary base change, as set out in [Stacks, Tag 0E6N]. Over a field it gives \(H^1(L)^\vee=\operatorname{Hom}(L,\omega_C)\). The normalization description (5.3)–(5.4) was proved here from the local node module.
- For a proper curve, ampleness of a line bundle is equivalent to positive degree on each one-dimensional irreducible component [Stacks, Tag 0B5Y]; ampleness descends through a finite surjection and can be tested after a field extension. For a proper finitely presented morphism of algebraic spaces, fibre ampleness extends to relative ampleness on a base neighbourhood and defines a universal open [Stacks, Tag 0D3D]. The individual-curve theorem [Stacks, Tag 0E3K] gives \(\omega\simeq\mathcal O\) in tail-free genus one and global generation of \(\omega^m\), \(m\geq2\), in tail-free genus at least two. It is used only for the semistable open, not for the proved stable ampleness equivalence.
- A flat local-complete-intersection morphism has perfect cotangent complex of amplitude \([-1,0]\). For a square-zero base extension with kernel \(I\), the obstruction to a marked flat deformation is in \(\operatorname{Ext}^2(L,\mathcal O\otimes I)\); classes of lifts and infinitesimal automorphisms are the degree-one and degree-zero Ext groups. This is the ordinary cotangent deformation theorem on the small étale topos [Stacks, Tags 08V5 and 0D17]. Its obstruction assertion follows from the connecting map into \(\operatorname{Ext}^2(L,\mathcal O\otimes I)\) in the cotangent transitivity triangle. Formal local structure of a split node over a Noetherian local base is \(A^\wedge[[x,y]]/(xy-a)\) [Stacks, Tag 0CBX].
- The Artinian formal smoothness criterion for a scheme locally of finite presentation over a Noetherian local base is used at a point of finite-type residue field. Passing to a smooth atlas gives the identical criterion for stacks; see the ordinary scheme criterion in [Stacks, Tag 0DZS]'s atlas proof and Lesson 7's proved versal-to-smooth step. Faithfully flat local base change detects smoothness. The Witt ring of a perfect field in characteristic \(p\) is a complete discrete valuation ring with residue that field.
- Schlessinger prorepresentability requires a singleton residual value, the full small-extension fibre-product conditions, finite tangent dimension and the injectivity of the coefficient derivation map [Stacks, Tag 06JM]. A complete Noetherian local formally smooth algebra with unchanged residue field is a power-series algebra, with number of variables its relative tangent dimension [Stacks, Tag 0DZK]. The hypotheses for both were verified in Theorem 6.4.
- Grothendieck's algebraization theorem [Stacks, Tag 089A] applies to a cartesian system of schemes over \(A/I^n\), for a Noetherian \(I\)-adically complete ring \(A\), with proper special fibre and compatible invertible sheaves ample on that fibre. It produces a proper algebraization and the compatible ample sheaf. Section 6.4 uses it over a marked deformation ring and then pulls back to \(k[[t]]\); Section 6.5 uses it over \(k[[t]]\). Both check flatness and generic smoothness. The ordinary local lci smoothing inputs in Proposition 6.5 are stated exactly there, [Stacks, Tags 0E7W and 0E7X].

The curve-stack algebraicity theorem is the stated input from Lesson 8, [Stacks, Tag 0D5A]. Its graph spaces, Hilbert diagonal and Picard stack were constructed there. The projective fixed-polynomial Hilbert scheme used for boundedness is the ordinary prerequisite from AG-HP-05. The unramified-diagonal Deligne–Mumford criterion was proved in Lesson 6, rather than assumed anew here.

The mathematical reading uses the [AI Integrated Stacks Project release](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790). The Moduli of Curves locators are Tags 0DMH, 0DMJ, 0DPY, 0DSP, 0E0E, 0DST, 0DSV, 0DSW, 0E0H, 0E6H, 0E0F, 0E1H, 0E1L, 0E0J, 0E0K, 0DZT, 0DZY, 0E84, 0E85, 0E87, 0DSX, 0E00, 0E6N, 0E6S, 0E6X, 0E73, 0E74, 0E75, 0E76, 0E79 and 0E7A. The formal-moduli discussion in examples-defos.tex has no numbered tag. Proposition 6.5 proves the full isolated-lci density statement of Tag 0E85, including its zero-dimensional part.

For the curve-stack results, two source distinctions matter: Tag 0DSP's opening diagonal paragraph names the polarized stack where the curve stack is intended; Tag 0DZY's global-functions item must select its smooth \(h^0=1\) open, rather than the whole smooth open. Also the final displayed connecting sequence in Tag 08V5's proof must end in \(\operatorname{Ext}^2(L,\mathcal G)\), as its statement and triangle require.

Grothendieck's *FGA*, Exposé 182, Section 7, discusses formal moduli through a functor of marked infinitesimal deformations. Its Theorem 10 uses \(H^0(T)=H^2(T)=0\) for a smooth proper scheme to obtain a regular formal moduli ring, and it relates algebraization to projectivity and \(H^2(\mathcal O)=0\). For genus-at-least-two curves these vanishings are exactly the smooth-curve ingredients used above. The passage appears in the [public maintained English edition](https://github.com/KokunoYumeto/fga-en/blob/b987b99fbdaff80efb9f23815a3583fa0a52d284/releases/2026-08-30-r1/fga-en-canon-errata-0001-0017.pdf), Exposé pages 31–32; the edition is unofficial.

Deligne and Mumford's [*The irreducibility of the space of curves of given genus*](https://www.numdam.org/item/PMIHES_1969__36__75_0.pdf), §1, Definition 1.1 defines stable curves over an arbitrary scheme using proper flat families and geometric fibres with nodes and sufficiently attached nonsingular rational components. Theorems 5.2, 6.2 and 6.3 above prove the modern criteria; the original paper is a historical source, not a substitute for those proofs.
