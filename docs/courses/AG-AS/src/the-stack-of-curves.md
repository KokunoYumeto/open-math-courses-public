# The stack of curves

*Written by GPT-6.1 Sol (OpenAI), Codex, Ultra, October 2026. Self-checked by the writing AI. Original text: public domain (CC0). Appendix A and the smoothing argument follow Stacks Project proofs, cited in the text.*

A node has a deformation \(xy=t\). The parameter \(t\) smooths its two branches, while deformations of the rest of a curve must glue around it. For proper nodal curves both parts of that gluing problem are unobstructed. Stability supplies a different ingredient: it removes vector fields, including those carried by a rational tail or bridge. Together these facts make the moduli of stable curves a smooth Deligne–Mumford stack.

We use the algebraicity theorem for the full curve stack proved in Lesson 8, Appendix A §A.8, the arbitrary-base Deligne–Mumford criterion proved in [Lesson 6](quotient-and-dm-stacks.md), and the infinitesimal methods of Lesson 7. Ordinary curve cohomology, Riemann–Roch and degree of a line bundle are prerequisites. Section 9 specifies the other ordinary geometric and deformation inputs. None of the smoothness, stability or dimension results proved here is used as its own prerequisite.

All stacks are over \(\operatorname{Spec}\mathbb Z\). A geometric fibre means base change to an algebraic closure of the residue field. The base of a family may be an arbitrary scheme. We use \(g\geq2\) whenever writing \(\mathcal M_g\) or \(\overline{\mathcal M}_g\).

## 1. Families and their diagonal

### 1.1. The full curve stack

An object of \(\mathcal{Curves}(S)\) is a morphism of algebraic spaces
\[
f:X\longrightarrow S
\tag{1.1}
\]
which is proper, flat, of finite presentation, with fibres of dimension at most one. An arrow over \(S\) is an \(S\)-isomorphism. Pullback defines arrows over other bases. Initially a curve may be nonreduced, disconnected, zero-dimensional or empty. Smoothness, connectedness and stability will select open substacks; they are not part of (1.1).

Allowing algebraic spaces is essential to effective descent. Given an fppf cover and compatible families, descent of algebraic spaces produces \(X\), and properness, flatness, finite presentation and the dimension bound descend. Isomorphisms descend uniquely, so this is descent of the entire groupoid. The theorem proved in Lesson 8, Section 8 and Appendix A §A.8, [Stacks, Tag 0D5A], says that this stack is algebraic.

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
Its relative dualizing complex is \(\omega_{X/S}[1]\). Appendix A proves relative duality, including its coherent trace and arbitrary-base formation; see [Stacks, Tag 0E6N].

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

**Lemma 5.0.1 (a generation test on all subcurves).** Let \(C\) be a connected projective reduced nodal curve over an algebraically closed field. Let \(L\) be a line bundle such that
\[
 \deg(L|_D)\geq 2g(D)
\tag{G.1}
\]
for every nonempty connected reduced subcurve \(D\), where \(g(D)=\dim H^1(D,\mathcal O_D)\). Then \(L\) is globally generated.

**Proof.** For a closed point \(p\), let \(I_p\) be its ideal. Field duality gives
\[
 H^1(C,I_pL)^\vee
 =\operatorname{Hom}_C(I_pL,\omega_C).
\tag{G.2}
\]
We show that a map on the right cannot be nonzero. Choose one connected union \(D\) of components on which it is generically nonzero. Pull the map to the smooth normalization of those components. At a smooth point other than \(p\), it is a regular section of \(\omega_C L^{-1}\); at a smooth \(p\), it is allowed one extra pole, because \(I_p^{-1}=\mathcal O_C(p)\).

At a node distinct from \(p\), the two branch values of the section agree in the fibre of this line bundle. If the other component is outside \(D\), its section is zero, so the branch in \(D\) must vanish there. At \(p\) itself, when it is a node, use the completed local ring
\[
 B=k[[x]]\times_k k[[y]],\qquad I_p=(x,y).
\]
A homomorphism \(I_p\to B\) is multiplication by a pair \((a(x),b(y))\) of regular branch series, with no equality required between their constants. Indeed its values on \(x,y\) are \((xa(x),0)\) and \((0,yb(y))\); conversely the annihilator relations on \(x,y\) force exactly these forms. Thus the map has no additional pole on either branch, and only the matching-value condition is removed. The same statement for \(I_pL\to\omega_C\) follows by choosing local frames. Faithfully flat completion reflects these local statements for the coherent modules.

Let \(\delta(D)\) count the nodes joining \(D\) to its complement. The normalization degree formula gives
\[
 \deg(\omega_C|_D)=2g(D)-2+\delta(D).
\]
The boundary nodes force \(\delta(D)\) zeros, with at most one exception if \(p\) is a boundary node. A smooth \(p\in D\) instead allows one extra pole. In every case the resulting line bundle on the normalized components of \(D\), after imposing these zeros and poles, has total degree at most
\[
 2g(D)-2-\deg(L|_D)+1\leq-1.
\]
Its section is generically nonzero on every chosen component. On a smooth proper component such a regular section has an effective zero divisor, so its degree is nonnegative. Summing over the components contradicts the displayed bound. Therefore the Hom group in (G.2), and hence \(H^1(C,I_pL)\), is zero. The exact evaluation sequence makes \(H^0(C,L)\to L|_p\) surjective for every closed point. The evaluation cokernel is coherent; its nonempty support on a finite-type field scheme would contain a closed point. It is consequently zero. \(\square\)

**Lemma 5.0 (tail-free dualizing sheaves).** Let \(C\) be a geometric prestable curve of genus \(g\geq1\) with no rational tail. If \(g=1\), then \(\omega_C\simeq\mathcal O_C\). If \(g\geq2\), every \(\omega_C^{\otimes m}\), \(m\geq2\), is globally generated.

**Proof.** On each normalized component the dualizing degree is \(2g_v-2+n_v\). It is nonnegative: a rational component has at least two branches in the tail-free connected genus-positive curve; a positive-genus component has nonnegative degree as well. The total degree is \(2g-2\).

When \(g=1\), every component degree is zero. Duality and \(H^0(C,\mathcal O_C)=k\) give \(h^0(C,\omega_C)=1\). Choose a nonzero section. On any normalized component where it is not identically zero it has no zero, by degree zero. At an adjoining node its value is therefore nonzero on the other branch. Connectedness propagates this to all components. The section is nowhere zero, including at nodes, and trivializes \(\omega_C\).

Suppose \(g\geq2\) and fix \(m\geq2\). For a proper connected subcurve \(D\), put \(r=g(D)\). Its boundary is nonempty, and
\[
 \deg(\omega_C^{\otimes m}|_D)=m(2r-2+\delta(D)).
\tag{G.3}
\]
If \(r=0\), all its normalized components are rational and its internal graph is a tree. Their total valence in the whole curve is \(2(|V_D|-1)+\delta(D)\). Every such vertex has valence at least two, so \(\delta(D)\geq2\); (G.3) is at least zero, which is \(2r\). If \(r=1\), its nonempty boundary gives degree at least \(m\geq2=2r\). If \(r\geq2\), the degree is at least \(2(2r-1)\geq2r\). For \(D=C\), it is \(m(2g-2)\geq2g\). Thus (G.1) holds for every connected subcurve, and Lemma 5.0.1 proves global generation. \(\square\)

These geometric assertions descend through field extension: the canonical cohomology and evaluation maps pull back under a field extension, and faithful flatness detects their surjectivity and a nowhere-zero section. They provide precisely the individual-fibre conclusions used in the arbitrary-base semistable-openness proof.

Semistability is open in \(\mathcal P\). We include the family argument. Fix \(m\geq2\). Lemma 5.0 proves the individual-fibre dualizing-sheaf input, retaining the tail-free scope of [Stacks, Tag 0E3K].

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

We use the two local algebra results proved in Lemmas 6.8–6.9 below: a finite-dimensional lci \(k\)-algebra admits a finite flat deformation over \(k[[t]]\) with étale generic fibre [Stacks, Tag 0E7W]; and an essentially finite-type lci local ring of dimension one at a closed point admits a flat deformation \(B_i/k[[t]]\) with
\[
t^{N_i}\in\operatorname{Fitt}_1
(\Omega_{B_i/k[[t]]})
\tag{6.9}
\]
for some \(N_i\), with the specified special local ring [Stacks, Tag 0E7X]. The Fitting bound says that this local deformation is smooth after inverting \(t\). The lemmas retain the specified special algebras and local rings. We first use them to prove the global density statement.

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

#### 6.5.1. Smooth generic fibres from linear perturbations

The local smoothing inputs can be proved by varying the constant and linear terms of the defining equations. The argument works over every field, including imperfect fields and finite fields.

**Lemma 6.6 (a generic linear perturbation).** Let \(1\le c\le n\) and let \(f_1,\ldots,f_c\in k[x_1,\ldots,x_n]\). Introduce parameters \(a_{ij}\), for \(0\le i\le n\), \(1\le j\le c\), and put
\[
g_j=f_j+a_{0j}+\sum_{i=1}^n a_{ij}x_i.
\]
There is a nonempty open in the parameter space \(\mathbf A^{c(n+1)}_k\) over which the scheme defined by the \(g_j\) is smooth over that parameter space.

*Proof.* Full rank of the matrix
\[
\left(\frac{\partial f_j}{\partial x_i}+a_{ij}\right)_{i,j}
\]
gives a standard smooth presentation. Suppose a point of rank less than \(c\) lay above the generic parameter point. In its residue field choose a kernel vector and renumber its nonzero entry, then divide to write it as \((1,\lambda_2,\ldots,\lambda_c)\). Its equations express
\[
a_{i1}=-\frac{\partial f_1}{\partial x_i}
-\sum_{j=2}^c\lambda_j\left(\frac{\partial f_j}{\partial x_i}+a_{ij}\right),
\qquad
a_{0j}=-f_j-\sum_i a_{ij}x_i.
\]
Thus all parameters belong to the field generated by the \(n\) elements \(x_i\), the \(c-1\) elements \(\lambda_j\), and the \(n(c-1)\) slopes \(a_{ij}\) with \(j\ge2\). Its transcendence degree is at most
\[
n+(c-1)+n(c-1)=c(n+1)-1.
\]
At a point above the generic parameter point, however, the \(c(n+1)\) parameters are algebraically independent. This contradiction excludes every deficient-rank point there. The deficient-rank locus is closed and of finite type. Its image is constructible by finite-type Chevalley; a constructible subset of an irreducible Noetherian space whose closure is the whole space contains its generic point. Consequently its closure is proper. The complement is the required nonempty open, with the full-rank smooth presentations just described. \(\square\)

**Lemma 6.7 (smoothing a global complete intersection).** If
\[
P=k[x_1,\ldots,x_n]/(f_1,\ldots,f_c)
\]
is a nonzero global complete intersection of dimension \(d=n-c\), there is a flat finitely presented \(k[[t]]\)-algebra \(Q\) with \(Q/tQ=P\), smooth generic fibre, and
\[
t^N\in\operatorname{Fitt}_d(\Omega_{Q/k[[t]]})
\]
for some integer \(N\ge0\).

*Proof.* Write \(R=k[[t]]\). Choose every \(a_{ij}\) in \(tR\), with its generic parameter point in the open of Lemma 6.6, and set \(Q=R[x]/(g_1,\ldots,g_c)\). This choice is possible also when \(k\) is finite. The subset \(tR\) is infinite inside \(k((t))\). A nonzero polynomial over a field cannot vanish on every tuple from an infinite subset: induct on its number of variables, choosing the earlier variables so that a nonzero coefficient remains nonzero, then avoiding the finitely many roots of the remaining one-variable polynomial. Apply this to a nonzero polynomial defining a principal open contained in the good parameter open. Its chosen value is nonzero in \(R\), so the **generic** point lies in that open. The closed parameter point remains zero, as required to preserve the special fibre.

At a prime of \(R[x]\) containing \(t,g_1,\ldots,g_c\), the sequence \(t,g_1,\ldots,g_c\) is regular: \(t\) is injective, and its reduction is the given regular sequence on the polynomial ring. In this Noetherian local ring regular sequences can be permuted, by *Regular sequences, depth and Cohen–Macaulay modules*, Proposition 1.2. Moving \(t\) to the end makes it injective on \(Q\) there. At primes not containing \(t\), multiplication by \(t\) is a unit. Hence \(Q\) has no \(R\)-torsion and is flat over the DVR \(R\). Its special fibre and finite presentation are the displayed presentation; the choice of parameters and Lemma 6.6 give smoothness of \(Q[1/t]\).

For completeness, the same presentation has relative dimension \(d\) everywhere on its generic fibre. At a point with a full \(c\)-row Jacobian minor, its smooth coordinate chart has \(n-c=d\) free coordinates. The presentation of differentials is
\[
Q^c\xrightarrow{(\partial g_j/\partial x_i)}Q^n
\longrightarrow\Omega_{Q/R}\longrightarrow0.
\]
Its \(d\)-th Fitting ideal is generated by the \(c\)-minors. Those minors generate the unit ideal after inverting \(t\). Clearing a finite list of denominators in the identity expressing \(1\) gives \(t^N\) in the original Fitting ideal. This is the claimed bound. If \(c=0\), take \(Q=R[x]\), with Fitting ideal \(Q\) and \(N=0\). \(\square\)

#### 6.5.2. Finite lci algebras and specified local rings

**Lemma 6.8 (finite smoothing, Tag 0E7W).** A finite-dimensional lci \(k\)-algebra \(A\) has a finite flat deformation \(B/k[[t]]\), with \(B/tB=A\) and étale generic fibre.

*Proof.* A finite-dimensional algebra is Artinian and is a finite product of its local factors, by *Noetherian and Artinian rings*, Theorem 4.2. Treat each nonzero factor separately. A local finite-dimensional lci algebra has a global complete-intersection presentation. Here is the passage from its local presentation: choose polynomial equations giving its regular sequence near the presenting closed point. Localize once to make the sequence regular on that neighbourhood. Its codimension equals the number of polynomial variables, since the point has finite residue field and the quotient has local dimension zero. This localized complete intersection has dimension zero. It is therefore finite-dimensional over \(k\); remove all its other local factors by one further principal localization. The remaining ring is the desired \(A\). To present a principal localization as a global complete intersection, combine the inverted elements into \(h\), add a variable \(z\), and impose \(hz-1\) **first**. This equation is a nonzerodivisor: its unit constant coefficient lets one kill successively every coefficient of a polynomial in its kernel. Its quotient is the localized polynomial ring. Follow it by the chosen regular sequence there. The resulting sequence is regular in the enlarged polynomial ring and has the required quotient. This supplies the global presentation without asserting regularity of the original equations away from the chosen neighbourhood.

Apply Lemma 6.7, with relative dimension zero, to obtain a flat finite-type \(R=k[[t]]\)-algebra \(Q\) whose closed fibre is this local \(A\) and whose generic fibre is smooth of dimension zero. The closed fibre has a unique point, and that point is quasi-finite. The finite-part theorem over a henselian local base, *Étale neighbourhoods, henselization and quasi-finite morphisms* (AG-FSE-07), Lemma 4.1, splits
\[
Q=B\times C,
\]
where \(B\) is finite over \(R\), has this entire closed fibre, and \(C/tC=0\). This theorem uses the genuinely assigned algebraic Zariski Main and henselian-algebra prerequisites at their recorded states. The direct summand \(B\) of the flat \(R\)-module \(Q\) is flat. Its generic fibre is an open-and-closed part of the smooth zero-dimensional generic fibre of \(Q\), and is therefore étale. It recovers the prescribed \(A\). Finally take the product over the original finitely many local factors. For \(A=0\), the zero algebra gives the empty finite flat family. \(\square\)

**Lemma 6.9 (local smoothing with a Fitting bound, Tag 0E7X).** Let \(A\) be an essentially finite-type lci local \(k\)-algebra, with residue field \(\kappa\), and put \(d=\dim A+\operatorname{trdeg}_k\kappa\). There is a flat essentially finite-type \(k[[t]]\)-algebra \(B\) whose special fibre is \(A\), with
\[
t^N\in\operatorname{Fitt}_d(\Omega_{B/k[[t]]}).
\]

*Proof.* A local lci presentation can be spread to a global complete intersection \(P\) near its presenting prime \(\mathfrak p\): its finitely many equations and successive injection conditions persist after one localization. Adjoining an inverse variable expresses that localization as a global complete intersection. The finite-type field dimension formula gives \(\dim P=\dim A+\operatorname{trdeg}_k\kappa=d\), after choosing this neighbourhood with its fixed codimension. Apply Lemma 6.7 to \(P\), obtaining \(Q\). Let \(\mathfrak q\) be the inverse image of \(\mathfrak p\) in \(Q\), and set \(B=Q_{\mathfrak q}\). Localization preserves flatness and commutes with the special-fibre quotient and the differential presentation. Thus \(B/tB=P_{\mathfrak p}=A\), and the Fitting bound localizes to the asserted one. \(\square\)

At the closed singular points used in Proposition 6.5, the residue field is finite over \(k\) and \(\dim A=1\), so the last lemma has \(d=1\) and supplies exactly (6.9). The construction retains each specified special local ring, which is needed to compare its deformation with the global formal family.

The perturbation argument follows the Stacks Project authors’ *Deformation Problems*, labels `lemma-jouanolou-type-thing`, `lemma-smoothing-affine-lci`, `lemma-smoothing-artinian-lci` and `lemma-smoothing-at-lci-point`, in the AI Integrated Stacks Project at revision `565b10e987aba5969b21145a0833f42d69f96790`. This independently expressed treatment includes the polynomial-density proof, the generic-point qualification and the corrected derivative index. The writing is CC0; the Stacks source keeps its own attribution and its GNU FDL terms.

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
- Appendix A proves that proper flat Gorenstein curve duality gives \(\omega_{X/S}[1]\), with an invertible \(\omega_{X/S}\) and formation under arbitrary base change, at the full scope of [Stacks, Tag 0E6N]. Over a field it gives \(H^1(L)^\vee=\operatorname{Hom}(L,\omega_C)\). The normalization description (5.3)–(5.4) was proved here from the local node module.
- For a proper curve, ampleness of a line bundle is equivalent to positive degree on each one-dimensional irreducible component [Stacks, Tag 0B5Y]; ampleness descends through a finite surjection and can be tested after a field extension. For a proper finitely presented morphism of algebraic spaces, fibre ampleness extends to relative ampleness on a base neighbourhood and defines a universal open [Stacks, Tag 0D3D]. Lemmas 5.0.1 and 5.0 prove the individual-curve global-generation and triviality inputs for the semistable open, in the tail-free scope of [Stacks, Tag 0E3K].
- A flat local-complete-intersection morphism has perfect cotangent complex of amplitude \([-1,0]\). For a square-zero base extension with kernel \(I\), the obstruction to a marked flat deformation is in \(\operatorname{Ext}^2(L,\mathcal O\otimes I)\); classes of lifts and infinitesimal automorphisms are the degree-one and degree-zero Ext groups. This is the ordinary cotangent deformation theorem on the small étale topos [Stacks, Tags 08V5 and 0D17]. The actual programme provider is *The cotangent complex* (AG-HP-12), §10: its global ringed-space theorem is a stated foundation whose full sheaf-extension proof remains genuinely assigned there. Its affine obstruction theorem, Theorem 9.1, and the lci amplitude theorem, Theorem 7.2, are written. Since the Artinian curve families here are schemes, this exact ringed-space scope suffices; no arbitrary-site extension is claimed. The connecting map gives the obstruction, while its sufficiency and torsor require that precise global classification. Formal local structure of a split node over a Noetherian local base is \(A^\wedge[[x,y]]/(xy-a)\) [Stacks, Tag 0CBX].
- The Artinian formal smoothness criterion for a scheme locally of finite presentation over a Noetherian local base is used at a point of finite-type residue field. Passing to a smooth atlas gives the identical criterion for stacks; see the ordinary scheme criterion in [Stacks, Tag 0DZS]'s atlas proof and Lesson 7's proved versal-to-smooth step. Faithfully flat local base change detects smoothness. The Witt ring of a perfect field in characteristic \(p\) is a complete discrete valuation ring with residue that field.
- Schlessinger prorepresentability requires a singleton residual value, the full small-extension fibre-product conditions, finite tangent dimension and the injectivity of the coefficient derivation map [Stacks, Tag 06JM]. A complete Noetherian local formally smooth algebra with unchanged residue field is a power-series algebra, with number of variables its relative tangent dimension [Stacks, Tag 0DZK]. The hypotheses for both were verified in Theorem 6.4. The actual written Schlessinger provider is *Formal moduli and Schlessinger’s theorem* (AG-HP-06), Theorem 5.1; the complete-local power-series argument is proved there in Theorem 7.3.
- Grothendieck's algebraization theorem [Stacks, Tag 089A] applies to a cartesian system of schemes over \(A/I^n\), for a Noetherian \(I\)-adically complete ring \(A\), with proper special fibre and compatible invertible sheaves ample on that fibre. It produces a proper algebraization and the compatible ample sheaf. Section 6.4 uses it over a marked deformation ring and then pulls back to \(k[[t]]\); Section 6.5 uses it over \(k[[t]]\). Both check flatness and generic smoothness. Lemmas 6.6–6.9 prove the local lci smoothing inputs, [Stacks, Tags 0E7W and 0E7X], including finite zero-dimensional components.

The curve-stack algebraicity theorem is proved at full scope in Lesson 8, Appendix A §A.8, [Stacks, Tag 0D5A]. Its graph spaces, Hilbert diagonal and Picard stack were constructed there. The projective fixed-polynomial Hilbert scheme used for boundedness is the ordinary prerequisite from AG-HP-05. The unramified-diagonal Deligne–Mumford criterion was proved in Lesson 6, rather than assumed anew here.

The mathematical reading uses the [AI Integrated Stacks Project release](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790), read at its exact pinned revision. The assigned Moduli of Curves locators are Tags 0DMH, 0DMJ, 0DPY, 0DSP, 0E0E, 0DST, 0DSV, 0DSW, 0E0H, 0E6H, 0E0F, 0E1H, 0E1L, 0E0J, 0E0K, 0DZT, 0DZY, 0E84, 0E85, 0E87, 0DSX, 0E00, 0E6N, 0E6S, 0E6X, 0E73, 0E74, 0E75, 0E76, 0E79 and 0E7A. Their complete assigned scopes were read. The formal-moduli label in examples-defos.tex was confirmed in that same release before use; it has no numbered tag. Proposition 6.5 proves the full isolated-lci density statement of Tag 0E85, including its zero-dimensional part.

Two source wording corrections are reflected above: Tag 0DSP's opening diagonal paragraph names the polarized stack where the curve stack is intended; Tag 0DZY's global-functions item must select its smooth \(h^0=1\) open, rather than the whole smooth open. Also the final displayed connecting sequence in Tag 08V5's proof must end in \(\operatorname{Ext}^2(L,\mathcal G)\), as its statement and triangle require. The arguments here retain the correct objects and degrees.

Grothendieck's *FGA*, Exposé 182, Section 7, discusses formal moduli through a functor of marked infinitesimal deformations. Its Theorem 10 uses \(H^0(T)=H^2(T)=0\) for a smooth proper scheme to obtain a regular formal moduli ring, and it relates algebraization to projectivity and \(H^2(\mathcal O)=0\). For genus-at-least-two curves these vanishings are exactly the smooth-curve ingredients used above. The passage was checked in the [public maintained English edition](https://github.com/KokunoYumeto/fga-en/blob/b987b99fbdaff80efb9f23815a3583fa0a52d284/releases/2026-08-30-r1/fga-en-canon-errata-0001-0017.pdf), Exposé pages 31–32; the edition is unofficial.

Deligne and Mumford's [*The irreducibility of the space of curves of given genus*](https://www.numdam.org/item/PMIHES_1969__36__75_0.pdf), §1, Definition 1.1 defines stable curves over an arbitrary scheme using proper flat families and geometric fibres with nodes and sufficiently attached nonsingular rational components. The definition was checked in the original paper. Theorems 5.2, 6.2 and 6.3 above supply independently written proofs of the assigned modern criteria; the original paper is a historical source, not a substitute for those proofs.

## Appendix A. Relative duality for Gorenstein curves

Section and statement numbers within this appendix are local to the appendix; an explicit course or provider title qualifies every outside reference.

### A.1. The claim and the genuine prerequisites

Let \(f:X\to S\) be a proper, flat, finitely presented morphism from an algebraic space to a scheme. Suppose that every nonempty geometric fibre is Gorenstein and pure of dimension one. The empty family is allowed: the assertions about its invertible sheaf and trace have their unique empty interpretation. There is an invertible \(\mathcal O_X\)-module \(\omega_{X/S}\), with relative duality trace
\[
\tau_f:Rf_*(\omega_{X/S}[1])\longrightarrow\mathcal O_S,
\tag{D1}
\]
whose formation commutes **canonically with every base change** \(g:T\to S\). With \(f_T:X_T=X\times_ST\to T\) and projection \(g_X:X_T\to X\), the comparison is
\[
b_g:g_X^*\omega_{X/S}\xrightarrow{\ \sim\ }\omega_{X_T/T}.
\tag{D2}
\]
It identifies the pulled-back trace with \(\tau_{f_T}\), and the comparisons for successive base changes compose. The relative dualizing complex is \(\omega_{X/S}[1]\); the shift means that its only cohomology sheaf is in degree \(-1\).

For a fibre \(C=X_s\) over an arbitrary field \(k=\kappa(s)\), this pair gives
\[
H^1(C,L)^\vee\cong\operatorname{Hom}_C(L,\omega_C),
\qquad V^\vee=\operatorname{Hom}_k(V,k),
\tag{D3}
\]
for coherent \(L\), with the trace normalization inherited from (D1). Neither perfection of \(k\), reducedness, geometric irreducibility, nor a chosen rational point is required. Pure dimension one is essential for the uniform shift \([1]\). A disjoint zero-dimensional component has its dualizing module in degree zero; it is not covered by the pure-one-dimensional assertion.

The following are the actual provider contracts used here.

| Provider | Exact contribution and inspected state |
|---|---|
| Lesson 8, Appendix A §8 (`reader-section-8`), §§12.10–12.11 | **Written reader proofs:** recognition of separated locally Noetherian spaces at points with local-ring dimension ≤1; proper field schemes of dimension ≤1 are H-projective, including reducible and nonreduced schemes. Exact anchors are `native-spaces-over-fields-lemma-codim-1-point-in-schematic-locus` and `native-varieties-lemma-dim-1-proper-projective`.  The reader's lower foundations keep their explicit unbound state; this binding is not a transitive-closure certificate. |
| AG-QC-15, *Dualizing sheaves and Serre duality for projective schemes*, Lemma 2.1, Theorems 4.1–4.2 | **Written** field Ext calculation, representing sheaf and field Serre duality. The actual lesson begins with projective schemes over a field. These results supply (D3) once the relative pair has been compared to the fibre pair. They do not supply (D2). |
| AG-QC-16, *The right adjoint of derived pushforward*, §1, Proposition 1.1, Theorem 3.1 | The qcqs-scheme right adjoint is a **genuinely assigned stated foundation**, with compact generation and Brown representability still externally identified in its §8; its formal adjunction, trace/composition, and finite Noetherian coinduction computation are **written**. Section 4's relative projective-bundle formula (11) is a real stated assignment, not a written proof. Section 3 below supplies the needed relative projective-space proof. We do not assign arbitrary-base relative Gorenstein duality to this lesson. |
| AG-QC-08, *Base change and the Grothendieck complex*, Lemma 3.1 and Theorem 3.2 | **Written** finite projective replacement and universal tensor comparison for a proper scheme over a **Noetherian** ring and a coherent base-flat sheaf. Section 4 below explains the return to an arbitrary ring, rather than changing that written theorem's hypotheses. |
| AG-MO-03, *Limits of schemes and Noetherian approximation* | Actual scheme finite-presentation approximation assignment. Prescribed-open Theorem 5.2/07RN remains an honestly **planned internal repair**. It is not the Zariski Main lesson. The additional flat-model argument is now integrated and written in Lesson 3 §5.6.7 C.1, Lesson 3 §5.6.7 C.1. These inputs descend a projective flat family and its hyperplane bundle to a flat Noetherian model. |
| Current AG-CA lessons by actual title and file | **Written current-edition proofs:** *Noetherian and Artinian rings*, Theorem 5.1 (Artin–Rees); *Faithful flatness and the local criterion for flatness*, Theorem 3.1/Corollary 3.2 (module/projective descent), Theorem 4.2 (Noetherian local criterion); *Regular sequences, depth and Cohen–Macaulay modules*, Theorems 4.1–4.2 and 6.1; *Projective dimension and the Auslander–Buchsbaum formula*, Theorems 1.3, 2.2–2.3 and 3.1; *Regular local rings*, Theorem 2.2 and Proposition 3.3. Exact current files and hashes are recorded in §9. The current course has 23 units, so the frozen 20-lesson numbering must not be used for these bindings. The extra Gorenstein dualizing-complex and arbitrary-ring recognition arguments are supplied in §2. |
| AG-ET-03, *Cohomology on sites*, and AG-ET-04, *Hypercoverings* | Genuine **planned** cohomology/hypercover foundations already bound in the gerbe support. AG-ET-04 owns the free abelian sheaf resolution and hypercover cohomology comparison on sites with fibre products. The étale sites here have fibre products. These are used only for the ordinary affine hypercover/Amitsur computation in §7, not for a claimed pre-existing space-duality theorem. |
| AG-HP-12 §10 | The exact global ringed-space deformation classification is a genuinely assigned **stated foundation**. Artinian families in Lesson 9 are schemes, so its stated scope suffices. This draft does not duplicate that classification, the local lci smoothing proof, or the genus-one cohomology argument in Lesson 5. |

### A.2. Two algebra arguments that make the fibre test legitimate

#### A.2.1. A dualizing complex on a Gorenstein local ring is a shifted free line

For a Noetherian ring \(R\), a dualizing complex \(D\) has bounded finite cohomology, finite injective dimension and its canonical homothety is an isomorphism
\[
R\xrightarrow{\sim}R\operatorname{Hom}_R(D,D).
\]
For a Noetherian **local** ring, “Gorenstein” means that \(R[0]\) is a dualizing complex. This is the native source's definition; in finite dimension it is equivalent to finite injective dimension of \(R\).

First, \(\mathbb D_D=R\operatorname{Hom}_R(-,D)\) is an involutive anti-equivalence on \(D^b_{\mathrm{fin}}(R)\). Here is the argument needed for that fact. A bounded injective representative of \(D\) bounds the possible Ext degrees, and a bounded-above finite free resolution of a finite module makes every Ext module finite. The evaluation map
\[
K\longrightarrow\mathbb D_D\mathbb D_DK
\tag{D4}
\]
is an isomorphism for finite free modules and their bounded complexes, by the homothety identity. To pass to bounded finite-cohomology \(K\), truncate a finite free resolution far to the left. Its omitted tail is a finite module placed arbitrarily far to the left. If a bounded injective representative of \(D\) is in degrees \([l,u]\), applying \(\mathbb D_D\) to a module has cohomology in \([l,u]\), and applying it twice has cohomology in a uniformly bounded interval \([l-u,u-l]\). Consequently, after shifting the omitted tail far enough to the left, neither that tail nor its double dual affects any specified cohomology degree of (D4). Comparison with the finite free truncation proves (D4) in every degree. This also proves the required boundedness and finiteness, so the anti-equivalence is an actual functor on the stated category.

We need one elementary consequence. If \(F:D^b_{\mathrm{fin}}(R)\to D^b_{\mathrm{fin}}(R)\) is an \(R\)-linear equivalence and \(R\) is local, then \(F(R)\) is a shift of \(R\). Put \(k=R/\mathfrak m\). All cohomology of \(F(k)\) is annihilated by \(\mathfrak m\), since the scalar action on \(F(k)\) is the transported scalar action on \(k\). If its first and last nonzero degrees were \(a<b\), projection onto the last cohomology, a nonzero linear map to the first, and inclusion of the first would give a nonzero negative-degree self map. Full faithfulness prohibits this, because \(\operatorname{Ext}^{a-b}_R(k,k)=0\). Thus \(F(k)\) is a vector space in one degree \(a\); its endomorphism ring is \(k\), so this vector space has dimension one and \(F(k)\cong k[-a]\).

A quasi-inverse \(G\) sends \(k\) to \(k[a]\). Induction on length now gives \(G(E)=E'[a]\) for each finite-length module \(E\), where \(E'\) also has finite length. For \(T=F(R)\), full faithfulness therefore gives
\[
\operatorname{Hom}(T,E[-a+i])=\operatorname{Ext}^i_R(R,E')=0
\quad(i\ne0).
\tag{D5}
\]
Testing with \(E=k\), and using the top cohomology truncation and Nakayama, shows that \(H^j(T)=0\) for \(j>a\) and that \(H^a(T)\) is cyclic. There cannot be another nonzero \(H^j(T)\), either: represent \(T\) by a bounded-above complex \(P\) of finite free modules and map it to \(M[-j]\), with \(M=\operatorname{coker}(P^{j-1}\to P^j)\). This map injects \(H^j(T)\) into \(M\). Artin–Rees gives an \(n\) such that
\(H^j(T)\cap\mathfrak m^nM\subset\mathfrak mH^j(T)\).
The resulting map \(T\to(M/\mathfrak m^nM)[-j]\) is nonzero on cohomology by Nakayama, contradicting (D5) when \(j\ne a\). Thus \(T=M_0[-a]\) with \(M_0\) cyclic. The canonical scalar map
\(R\to\operatorname{End}_R(M_0)\)
is an isomorphism by full faithfulness. If \(M_0=R/I\), this canonical map has kernel \(I\), so \(I=0\). Hence \(T=R[-a]\).

Apply this consequence to \(F=\mathbb D_R\mathbb D_D\) when \(R\) is Gorenstein. It shows that \(R\operatorname{Hom}_R(D,R)\) is a shifted free line. Apply the involution \(\mathbb D_R\) once more: \(D\) is also a shifted free line. This proves the precise Gorenstein fact used below, including the object, not merely a numerical rank.

For clarity about its use over a field, let \(C\) be pure one-dimensional and projective over \(k\), and embed it in \(P=\mathbf P^N_k\), with \(N\ge1\). At a point \(x\), set \(B=\mathcal O_{P,x}\), \(R=\mathcal O_{C,x}=B/I\), and \(c=N-1\). Theorem 2.2 of *Regular local rings* gives global dimension \(\dim B\). Hence \(\operatorname{Ext}^{\dim B+1}_B(M,B)=0\) for every module \(M\); dimension shifting in an injective resolution gives finite injective dimension of \(B\). Coinduction makes \(D_R=R\operatorname{Hom}_B(R,B)[N]\) a dualizing complex for \(R\): it has finite cohomology and a bounded injective \(R\)-representative, and the homothety identity is the finite-free biduality of the perfect \(B\)-module \(R\). Explicitly,
\[
R\operatorname{Hom}_R(D_R,D_R)
 \cong R\operatorname{Hom}_B(D_R,B[N])\cong R.
\]
The first comparison is derived coinduction; the second is finite-free evaluation.

If \(R\) is Gorenstein, §2.1 says this complex has a single free rank-one cohomology module. Its degree is exactly \(-1\). To see the shift rather than guess it, every minimal prime of \(I\) has height \(c\), by the finite-type dimension formula and purity. Choose a \(B\)-regular sequence of length \(c\) in \(I\) by prime avoidance in successive CM quotients, as in AG-QC-15 Lemma 2.1. In the last quotient \(B_0\), the image \(I_0\) has height zero. A minimal prime containing \(I_0\) is an associated prime of the CM ring \(B_0\), so some nonzero element is annihilated by \(I_0\). Consequently \(\operatorname{Hom}_{B_0}(R,B_0)\ne0\). Repeated one-element coinduction gives
\(\operatorname{Ext}^c_B(R,B)\ne0\), while the lower Ext groups vanish. The single nonzero Ext degree must therefore be \(c\), and the shift \([N]\) places it in degree \(c-N=-1\). A minimal finite free resolution shows that its last dual cokernel is nonzero, so its length is \(c\); Theorem 3.1 of *Projective dimension and the Auslander–Buchsbaum formula* also yields \(\operatorname{depth}R=\dim R\). This proves both CM and the shifted-line assertion in the exact pure-curve field scope needed here, including generic and closed points.

#### A.2.2. The arbitrary-ring residue-field test

Let \(R\) be any ring and let \(K\) be pseudo-coherent and bounded below. If
\[
K\otimes_R^L\kappa(\mathfrak p)\cong\kappa(\mathfrak p)[1]
\tag{D6}
\]
for every prime \(\mathfrak p\), then \(K\cong L[1]\) for an invertible module \(L\).

Here is a local proof, retaining the bounded-below assumption. Represent \(K\) by a bounded-above complex of finite free modules. At a degree \(i\) where its residue-field cohomology vanishes, the two adjacent matrices have residue ranks adding to the dimension of the middle term. Invert nonzero minors of those ranks. Gaussian elimination, together with the identity that two consecutive differentials compose to zero, splits off the corresponding identity two-term complexes and leaves a zero term in degree \(i\). Thus, on a neighbourhood of \(\mathfrak p\), the complex splits into its truncations below and above \(i\), and its upper truncation is perfect. Choose \(i\) below both the lower cohomology bound of \(K\) and \(-1\). Its lower truncation is zero, so \(K\) is perfect near \(\mathfrak p\). A bounded finite free representative can now be reduced in the same way, degree by degree, to the ranks of its residue-field cohomology. Under (D6) it has one free term of rank one, in degree \(-1\). This proves the local claim. The sheaf \(L=H^{-1}(K)\) and its canonical truncation isomorphism \(L[1]\to K\) glue these local descriptions. There is no appeal to a Noetherian hypothesis or to an ordinary, underived fibre test on an arbitrary nonflat module.

### A.3. Relative projective space, with its trace

Let \(\pi:P=\mathbf P^N_A\to\operatorname{Spec}A\), for an arbitrary ring \(A\), and put \(D_P=\mathcal O_P(-N-1)[N]\). The ordered affine cover \(D_+(T_0),\ldots,D_+(T_N)\) computes the cohomology of every twist. Its Laurent monomial decomposition works over \(\mathbb Z\) and hence over every \(A\): nonnegative exponent monomials give \(H^0\), all-negative exponent monomials give \(H^N\), and the other monomial summands are contractible. For a monomial whose negative exponent indices form a nonempty proper subset J, its summands occur exactly on cover intersections containing J; insert/remove a fixed index outside J with the ordered Čech sign to contract that summand. When J is empty the usual augmented simplex leaves degree zero; when J contains all indices only top degree remains. This proves the calculation over A rather than inferring it from field dimensions. In particular
\[
R\Gamma(P,D_P)\cong A,
\]
with trace extracting the coefficient of \(T_0^{-1}\cdots T_N^{-1}\) in ordered top Čech cohomology. This is an \(A\)-linear trace, not a choice of a scalar in each fibre.

Use the right adjoint \(a_\pi\) genuinely assigned in AG-QC-16 §1. Transposing this trace produces \(c:D_P\to a_\pi(A)\). Testing against every shift of \(\mathcal O_P(t)\), for every integer \(t\), gives the coefficient pairings
\[
R\Gamma(P,\mathcal O(-N-1-t))[N]
 \longrightarrow R\operatorname{Hom}_A(R\Gamma(P,\mathcal O(t)),A).
\tag{D7}
\]
They are isomorphisms of complexes. For \(t\ge0\), a monomial \(T^\alpha\) of degree \(t\) pairs with \(T_0^{-\alpha_0-1}\cdots T_N^{-\alpha_N-1}\), giving the dual finite free bases. For \(-N\le t\le-1\), both complexes are zero. For \(t\le-N-1\), the same pairing with the roles reversed identifies the finite free modules, now in degree \(-N\). The \(N=0\) assertion is simply the identity adjunction of \(\operatorname{Spec}A\); the tautological twist is trivial and the trace is the identity.

Here and below all ample twists detect objects, not only coherent sheaves. Indeed, let \(L\) be ample on a qc separated scheme and suppose \(R\operatorname{Hom}(L^n,K)=0\) for all integers \(n\). Choose finitely many sections \(s_i\) of positive powers of \(L\) whose nonvanishing opens are affine and cover the scheme. On \(X_{s_i}\), localization is the filtered colimit of tensoring by the corresponding positive powers, with transition multiplication by \(s_i\). Thus
\[
R\Gamma(X_{s_i},K|_{X_{s_i}})
 \cong\operatorname*{colim}_{m}R\Gamma(X,K\otimes L^{m\deg(s_i)})=0.
\]
For this equality use a finite affine Čech computation; filtered colimits are exact and commute with its finitely many terms. On an affine open, a quasi-coherent-cohomology complex is zero precisely when its derived section complex is zero. The opens cover, so \(K=0\). This proves the detection statement for the full derived category. Applying it to the cone of \(c\), (D7) proves
\[
a_\pi(A)\cong\mathcal O_P(-N-1)[N]
\tag{D8}
\]
with the specified trace. This supplies the needed part of AG-QC-16's stated relative formula rather than using its external link as a proof.

### A.4. Perfect cohomology of ample twists over an arbitrary ring

Let \(p:Y\to\operatorname{Spec}A\) be a projective, flat, finitely presented scheme and \(L\) a relatively ample invertible sheaf. For every integer \(n\),
\[
P_n=R\Gamma(Y,L^n)
\tag{D9}
\]
is perfect over \(A\), and its canonical derived tensor comparison is an isomorphism for every \(A\)-algebra \(A'\).

Here is the precise approximation and return. After replacing \(L\) by a positive power for the embedding, descend the finite equations of \(Y\hookrightarrow\mathbf P^N_A\), the original line bundle, its finite trivializations and transition functions, and their equalities to a finitely generated \(\mathbb Z\)-algebra \(A_0\). The scheme finite-presentation limit assertion is the genuine AG-MO-03 assignment. The flat-model argument in the integrated Lesson 3 §5.6.7 C.1 allows a later Noetherian model on which \(Y_0\to\operatorname{Spec}A_0\) is flat: apply it to the finitely many affine coordinate algebras of the descended projective scheme, and take one common stage for their covers and gluing equalities. Projectivity holds at the model because the descended closed immersion is already into projective space. The descended \(L_0\) is a line bundle, hence base-flat on \(Y_0\).

AG-QC-08 Theorem 3.2 now supplies a bounded finite projective \(A_0\)-complex \(P_{0,n}\) with universal tensor comparison. Its pullback
\(P_{0,n}\otimes_{A_0}A\)
is a bounded finite projective \(A\)-complex and computes (D9). The same fixed comparison computes cohomology over every \(A'\); composition of the affine tensor identifications identifies this with the canonical derived base-change map. Thus this return supplies perfectness and its actual comparison, not just finiteness of individual fibre cohomology groups.

We also use the following elementary derived Čech identity. For any \(K\in D_{\mathrm{QCoh}}(Y)\), any \(A\)-complex \(M\), and any affine base change \(A\to A'\),
\[
R\Gamma(Y,K)\otimes_A^L M
 \cong R\Gamma(Y,K\otimes_A^L M),
\quad
R\Gamma(Y,K)\otimes_A^L A'
 \cong R\Gamma(Y_{A'},L g_Y^*K).
\tag{D10}
\]
Take a finite affine cover of the separated scheme \(Y\). Its intersections are affine and their rings are \(A\)-flat, because \(Y/A\) is flat. Derived sections on each intersection are the corresponding module complex, and affine pullback computes its derived tensor with \(A'\). Choose K-flat representatives to compute the tensors. The finite Čech total complex then commutes with derived tensor; no infinite product has been interchanged with it. This proves (D10), for unbounded complexes as well. The maps are the usual projection/base-change comparisons, since their affine restrictions are the corresponding tensor maps.

### A.5. Proper adjoints commute with every base change on projective charts

Keep the hypotheses of §4. Let \(D_Y=a_p(A)\), with counit \(\tau\). For \(A\to A'\), put \(Y'=Y\times_AA'\), \(p':Y'\to\operatorname{Spec}A'\), and \(g_Y:Y'\to Y\). Base change (D10) and the trace give
\[
R\Gamma(Y',Lg_Y^*D_Y)
 \cong R\Gamma(Y,D_Y)\otimes_A^L A'
 \xrightarrow{\tau\otimes1}A'.
\]
Its adjoint transpose is the specific comparison
\[
\eta_g:Lg_Y^*D_Y\longrightarrow a_{p'}(A').
\tag{D11}
\]
For \(L_n=L^n\), testing this map gives
\[
\begin{aligned}
R\operatorname{Hom}_{Y'}(g_Y^*L_n,Lg_Y^*D_Y)
&\cong R\operatorname{Hom}_Y(L_n,D_Y)\otimes_A^L A'\\
&\cong R\operatorname{Hom}_A(P_n,A)\otimes_A^L A'\\
&\cong R\operatorname{Hom}_{A'}(P_n\otimes_A^L A',A')\\
&\cong R\operatorname{Hom}_{Y'}(g_Y^*L_n,a_{p'}(A')).
\end{aligned}
\tag{D12}
\]
The first is (D10) applied to \(L_n^\vee\otimes D_Y\); the second and fourth are derived adjunction; the third is finite-projective duality for the perfect complex (D9). Every comparison uses evaluation and the same counit. Consequently their composite is the map induced by (D11), rather than an unrelated abstract isomorphism. Ample-twist detection from §3 proves that (D11) is an isomorphism. It preserves the trace by its definition. For two successive base changes, both comparison maps transpose the same twice-pulled-back trace; uniqueness under adjunction makes them equal. This proves coherence as well as existence.

The same argument proves the tensor comparison
\[
a_p(M)\cong Lp^*M\otimes_Y^L D_Y
\tag{D13}
\]
for every \(A\)-complex \(M\). Its comparison is the transpose of projection formula followed by \(\tau\otimes1_M\); testing on \(L_n\) replaces the third line of (D12) by
\(R\operatorname{Hom}_A(P_n,A)\otimes_A^L M
 \cong R\operatorname{Hom}_A(P_n,M)\).
This is again finite-projective duality, and the same detection proves (D13).

#### A.5.1. Why this adjoint complex is bounded and pseudo-coherent

These properties must be proved before applying the residue-field test of §2.2. Choose the flat Noetherian model \(Y_0/A_0\) used in §4 and an embedding \(i:Y_0\hookrightarrow P_0=\mathbf P^N_{A_0}\). Adjunction composition, (D8), and the **written** Noetherian finite-map computation of AG-QC-16 Theorem 3.1 give
\[
a_{p_0}(A_0)=Ri^b(\mathcal O_{P_0}(-N-1)[N]).
\tag{D14}
\]
The ambient Hom object carries the \(\mathcal O_{Y_0}\)-action specified by coinduction; omitting that action would not define the object on \(Y_0\).

Locally in a standard affine of \(P_0\), write its ring as \(B=A_0[t_1,\ldots,t_N]\) and \(Y_0\) as a finite quotient module \(C=B/I\). The \(A_0\)-flat module \(C\) has a locally finite free \(B\)-resolution of length at most \(N\). Indeed, construct a finite free resolution through its \(N\)-th syzygy. All syzygies are \(A_0\)-flat, by induction on the short exact sequences between the flat middle and quotient modules. Tensoring with a residue field of \(A_0\) therefore leaves a resolution. The fibre polynomial ring is regular of dimension at most \(N\), so its \(N\)-th syzygy is projective after localizing at the point under consideration, by *Regular local rings*, Theorem 2.2 (with Proposition 3.3 and localization for the polynomial fibre). A free resolution and the preceding flatness show that
\(\operatorname{Tor}^B_1(K_N,\kappa(x))
 =\operatorname{Tor}^{B_s}_1((K_N)_s,\kappa(x))=0\).
The Noetherian local flatness criterion, *Faithful flatness and the local criterion for flatness*, Theorem 4.2, applied to the local ring \(B_x\), makes the finite syzygy \(K_N\) free near that point. Thus the resolution can be truncated there.

Dualizing this resolution into the ambient line and shifting by \([N]\) represents the underlying \(A_0\)-complex in (D14) by a bounded complex of \(A_0\)-flat modules in degrees \([-N,0]\). It has bounded coherent cohomology as a \(C\)-complex, so is pseudo-coherent over \(C\). For \(Y=Y_0\times_{A_0}A\), (D11) identifies \(D_Y\) with derived pullback of (D14). Derived pullback preserves pseudo-coherence, by tensoring a bounded-above finite free representative. Since \(C\) is \(A_0\)-flat,
\(D_0\otimes_C^L(C\otimes_{A_0}A)=D_0\otimes_{A_0}^L A\),
and the displayed bounded \(A_0\)-flat representative proves the retained lower and upper bounds locally. These facts return **both** hypotheses of §2.2 to the original arbitrary base.

### A.6. The Gorenstein conclusion on those charts

Suppose now that every nonempty geometric fibre of \(Y/A\) is Gorenstein and pure of dimension one. Purity is invariant under field extension. To make the descent of the Gorenstein conclusion explicit, apply (D11) to a residue field \(k\) and then an algebraic closure \(\bar k\). The field duality complex becomes a line in degree \(-1\) on the geometric fibre by §2.1. For a point of the k-fibre, choose a point over it on that faithfully flat geometric fibre. The derived tensor of its point complex with the resulting residue-field extension is one-dimensional in degree \(-1\); faithfulness implies the same statement before that field extension. The bounded pseudo-coherent field complex therefore satisfies the test of §2.2 and is already a line in degree \(-1\). This proves exactly the residue-field shifted-line assertion needed below, rather than assuming an underived nonflat descent test.

By (D11), the restriction of \(D_Y\) to \(Y_s\) is its normalized field duality complex. Section 2.1 and the field embedding computation identify it with an invertible sheaf in degree \(-1\). Pulling further to any point \(y\in Y_s\) gives
\[
D_Y\otimes_{\mathcal O_Y}^L\kappa(y)\cong\kappa(y)[1].
\]
The boundedness and pseudo-coherence proved in §5.1 allow §2.2 to apply. Hence
\[
D_Y\cong\omega_{Y/A}[1],\qquad \omega_{Y/A}=H^{-1}(D_Y)
\tag{D15}
\]
with \(\omega_{Y/A}\) invertible. It is base-flat, because \(Y/A\) is flat and it is locally free over \(\mathcal O_Y\). Taking degree \(-1\) in (D11) gives the **ordinary** line-bundle base change in (D2): derived and ordinary pullback agree for this line bundle. Trace preservation and successive-base-change compatibility have already been proved at the complex level.

For later descent we also record the top-cohomology interpretation without importing a dimension theorem for families. Formula (D13), now with (D15), gives \(a_p(M)=p^*M\otimes\omega_{Y/A}[1]\) for every module \(M\). For an injective \(A\)-module \(J\) and a quasi-coherent sheaf \(F\),
\[
\operatorname{Hom}_A(H^i(Y,F),J)
 =\operatorname{Hom}_{D(A)}(R\Gamma(Y,F),J[-i])
 =\operatorname{Ext}^{1-i}_Y(F,p^*J\otimes\omega_{Y/A})=0
\quad(i>1).
\]
Injective modules detect a nonzero module, so \(H^i(Y,F)=0\) for \(i>1\). Thus \(R\Gamma(Y,F)[1]\) is in \(D^{\le0}(A)\), and its degree-zero cohomology is \(H^1(Y,F)\). The truncation triangle and t-structure orthogonality give
\[
\operatorname{Hom}_Y(F,\omega_{Y/A})
 =\operatorname{Hom}_{D(A)}(R\Gamma(Y,F)[1],A)
 =\operatorname{Hom}_A(H^1(Y,F),A).
\tag{D16}
\]
The map sends \(u:F\to\omega_{Y/A}\) to \(\tau\circ H^1(u)\). This specifies the representing trace for ordinary sheaves over the arbitrary base as well.

### A.7. Return from projective charts to the original algebraic space

#### A.7.1. The field recognition/projectivity binding and projective charts

The written coherent reader supplies the full field argument at the required scope. A separated locally Noetherian algebraic space has a scheme neighbourhood at a point \(x\) if the local-ring dimension at \(x\) is at most one (§12.10, actual statement and proof at lines 1709–1713). In a proper finite-type \(k\)-space of dimension at most one, every point satisfies that condition. Its scheme open neighbourhoods therefore cover the whole space, making it a scheme. The reader's proof constructs an invariant affine open around the finite orbit in a finite scheme cover and then descends the finite groupoid quotient; it does not assume that an étale affine chart by itself makes the original point schematic.

For that proper \(k\)-scheme, §12.11 constructs an ample bundle on each reduced one-dimensional component, glues those bundles across the finite intersections, and then lifts the bundle through the nilpotent thickening. Vanishing of \(H^2\) in topological dimension one supplies the Picard lift; ampleness is unchanged by the nilpotent thickening. A finite-type scheme with an ample bundle is quasi-projective; properness turns the resulting immersion into a closed immersion. Zero-dimensional proper schemes are finite and projective, and the empty scheme has its unique closed immersion. These endpoint cases are explicitly retained in the reader §8. Thus every proper field algebraic space of dimension at most one is an H-projective scheme, with no reducedness or perfect-field restriction. The word “codimension” in the copied recognition slogan must not replace its actual **local-ring dimension** hypothesis.

Lesson 9 Proposition 1.1 applies this field result and the genuinely assigned AG-HP-12 §10 deformation classification to produce an étale cover \(\{S_i\to S\}\) by affine schemes for which \(X_i=X\times_SS_i\) is a projective scheme over \(S_i\). Its use of that stated deformation foundation remains honest; we do not claim that the present draft proves it. In particular, these are projective **base** charts, not arbitrary affine source charts. Properness, flatness and finite presentation survive those base changes. Sections 3–6 consequently supply pairs \((\omega_i[1],\tau_i)\) on every chart.

#### A.7.2. Descent of the line bundle and of its trace

For every affine open \(T\) in a refinement of \(S_i\times_SS_j\), the pullbacks of \((\omega_i[1],\tau_i)\) and \((\omega_j[1],\tau_j)\) are the same right-adjoint representing pair for the projective scheme \(X_T/T\), by (D11). Yoneda gives a **unique trace-preserving** comparison between them. Uniqueness makes the comparisons agree on refinements and satisfy the cocycle condition on triple overlaps. Since each object is a sheaf shifted by \([1]\), these comparisons are ordinary line-bundle isomorphisms; their composition is ordinary composition of sheaf maps. Ordinary étale/fpqc descent of quasi-coherent modules gives a sheaf \(\omega\) on the original space \(X\). One can compute this descent on affine covers by the faithfully flat equalizer and its Amitsur sequence. Finite presentation and projectivity descend by *Faithful flatness and the local criterion for flatness*, Theorem 3.1 and Corollary 3.2, and rank one is checked in every fibre, so \(\omega\) is invertible. Its pullback to \(X_i\) is the specified \(\omega_i\), not an unidentified fibrewise substitute.

We spell out the cohomology comparison used for the trace. For a qcqs algebraic space over an affine base and a bounded-below quasi-coherent-cohomology complex, an affine étale hypercover computes derived cohomology. At each simplicial degree one may take a finite union of affines: begin with a finite affine étale atlas and cover the quasi-compact matching spaces by finite affine covers, successively. The quasi-separatedness keeps these matching spaces quasi-compact. The free-sheaf resolution/hypercover comparison is the exact AG-ET-04 planned input identified in §1, with the derived site cohomology input AG-ET-03. Tensoring with a flat algebra commutes with this computation: in each fixed total degree the bounded-below hypothesis leaves only finitely many hypercover degrees, and flat tensor preserves exactness. On each affine piece the comparison is ordinary module tensor. This proves the canonical flat base-change comparison in this bounded-below scope, with its composition compatibility.

We also need an all-complex comparison for **étale base changes**, which has a different elementary proof. Regard \(f\) as a morphism of the small étale ringed topoi. If \(T\to S\) is étale, the small étale topos of \(T\) is the slice by its represented sheaf, and the topos of \(X_T\) is the corresponding slice on \(X\). Restriction to such a slice is exact. Its left adjoint is extension by zero: locally on the étale site its module is the direct sum of the modules indexed by the sections of the represented étale object. Direct sums and sheafification are exact, so this left adjoint is exact. Consequently restriction preserves K-injective complexes, by adjunction applied to an acyclic complex. Underived direct image commutes with these slice restrictions, by evaluation on each étale object. Restricting a K-injective representative therefore proves
\[
 (Rf_*K)|_{T_{\mathrm{\acute et}}}
   \cong Rf_{T*}(K|_{X_T})
\tag{D16a}
\]
for every complex \(K\), without a boundedness assumption. On \(\mathcal O\)-modules this restriction is the ordinary flat pullback along the étale map, so it is also its derived pullback.

For \(K\) with quasi-coherent cohomology, the right side of (D16a) has quasi-coherent cohomology on each projective base chart: a finite affine Čech calculation on the separated projective scheme gives the usual scheme pushforward, including for unbounded complexes. Quasi-coherence is étale local, so \(Rf_*K\) has quasi-coherent cohomology on \(S\) itself. On an affine base, the affine derived-section equivalence for quasi-coherent complexes identifies (D16a) with the canonical tensor comparison
\[
 R\Gamma(X,K)\otimes_A^L B
   \cong R\Gamma(X_B,K_B)
\tag{D16b}
\]
for every étale \(A\)-algebra \(B\) and every \(K\in D_{\mathrm{QCoh}}(X)\). This all-complex assertion follows from slice localization and the projective base charts; it does not interchange flat tensor with an unbounded infinite hypercover totalization.

Locally let \(S=\operatorname{Spec}A\). Choose finitely many affine members of the above projective base cover and put \(B=\prod B_i\); then \(A\to B\) is faithfully flat étale and \(X_B\) is a projective scheme over \(B\). Applying (D16b) to a quasi-coherent sheaf \(F\) gives
\[
H^q(X,F)\otimes_AB\cong H^q(X_B,F_B).
\]
The right side vanishes for \(q>1\) by §6. Faithfulness proves the same vanishing on \(X\). This includes \(F=\omega\). Thus \(Rf_*\omega[1]\) has no positive cohomology, and a map from it to \(\mathcal O_S\) is determined by its degree-zero map
\(R^1f_*\omega\to\mathcal O_S\).
The chart traces give compatible maps of this sheaf by the same flat base-change comparison, so they descend to (D1). This construction supplies an actual trace on the original space.

#### A.7.3. The descended pair really represents duality

The assertion about a relative dualizing **complex** asks for more than an invertible sheaf with field pairings. For every affine base chart \(T=\operatorname{Spec}A\) and every \(K\in D_{\mathrm{QCoh}}(X_T)\), the descended trace induces
\[
R\operatorname{Hom}_{X_T}(K,\omega_{X_T/T}[1])
 \xrightarrow{\sim}
R\operatorname{Hom}_A(R\Gamma(X_T,K),A).
\tag{D17}
\]
Here is the descent proof, avoiding an unassigned algebraic-space compact-generator theorem.

Choose the faithfully flat étale \(A\to B\) of §7.2 with \(X_B\) projective. Write \(B_n=B^{\otimes_A(n+1)}\), \(X_n=X_T\times_AB_n\), and let \(r_n:X_n\to X_T\) be the affine flat projection. The exact Amitsur resolution of a module supplies the corresponding resolution of \(D=\omega[1]\) by \(R(r_n)_*D_n\). Here every \(r_n\) is affine; its higher direct images of the quasi-coherent line sheaf vanish, as one checks after an affine étale cover of the target using ordinary affine module cohomology. Thus these terms are \((r_n)_*\omega_n[1]\). On such a target cover the augmented complex is the ordinary module Amitsur complex. It is split after faithfully flat pullback, so exactness is reflected before pullback. This proves that it really resolves D, rather than merely matching its fibres. Applying derived Hom in the second variable computes
\[
R\operatorname{Hom}_{X_T}(K,D)
 \cong\operatorname{Tot}_nR\operatorname{Hom}_{X_n}(K_n,D_n).
\tag{D18}
\]
More explicitly, resolve the cosimplicial target by injective complexes and use product totalization; derived Hom, as the right adjoint to derived tensor, preserves that homotopy limit. This does not assert that ordinary Hom commutes with an arbitrary infinite tensor product. Derived pullback–pushforward adjunction identifies the individual terms in (D18).

Similarly the Amitsur resolution of \(A\) gives
\[
R\operatorname{Hom}_A(R\Gamma(X_T,K),A)
 \cong\operatorname{Tot}_n
 R\operatorname{Hom}_{B_n}(R\Gamma(X_T,K)\otimes_A^LB_n,B_n).
\tag{D19}
\]
The all-complex étale comparison (D16b) identifies the first argument in each term with \(R\Gamma(X_n,K_n)\). Each \(X_n/B_n\) is a projective base change of \(X_B/B\). Its pair is the pair of §§5–6, and therefore the projective derived adjunction identifies the terms of (D18) and (D19). The identifications are trace-induced and commute with every cosimplicial structure map, by the coherence of (D11). They induce (D17).

This proof applies to unbounded \(K\) as stated. The two target resolutions are resolutions of the bounded-below objects \(\omega[1]\) and \(A\); their exact augmented Amitsur complexes identify their homotopy totalizations with those targets. Applying derived Hom in its second variable preserves that homotopy limit for any fixed source. Comparison of the individual terms then uses the already proved all-complex étale base change (D16b) and projective adjunction. Thus there is no truncation-return or unbounded hypercohomology convergence assertion left implicit in (D17).

This is precisely the relative representing property. In particular it constructs the value at \(A\) of the space right adjoint needed here; it does not purport to prove Brown representability for every qcqs algebraic space. The line sheaf is base-flat and finitely presented, so its shift is relatively perfect as required by the relative definition.

#### A.7.4. Arbitrary base change and return maps

Now let \(g:T\to S\) be **any** morphism of schemes, including a nonflat or non-Noetherian one. The pulled-back cover \(S_i\times_ST\to T\) remains étale and surjective. Refine it by affine opens; the corresponding \(X_T\) charts are projective schemes. The canonical derived base-change map
\[
 Lg^*Rf_*K\longrightarrow Rf_{T*}Lg_X^*K
\tag{D19a}
\]
is an isomorphism for \(K\in D_{\mathrm{QCoh}}(X)\): restrict it to those étale refinements, use slice localization (D16a), and apply the projective comparison (D10). These restrictions detect an isomorphism. Both sides have quasi-coherent cohomology by the projective chart computation. In particular this supplies the actual return map for the pulled-back trace, as well as for \(Rf_*\mathcal O_X\). Formula (D11) on each refined chart gives
\(g_X^*\omega\cong\omega_{X_T/T}\),
with its pulled-back trace. On overlaps both comparisons are the unique trace-preserving representing comparison, so they descend to the global (D2). For \(T'\xrightarrow hT\xrightarrow gS\), uniqueness proves
\[
b_{g\circ h}=b_h\circ h_X^*b_g
\tag{D20}
\]
under the canonical pullback composition identifications. Thus reduction to projective charts returns the specified line bundle, the trace and their coherent comparisons to the original family. Exactly the same argument allows algebraic-space base changes by taking affine étale charts of the new base. No flatness of \(g\) has been introduced.

### A.8. The consequences actually used in Lesson 9

For a residue-field fibre \(C\), §7.1 makes \(C\) a projective scheme. Its complex is the field complex in AG-QC-16 Theorem 5.1 by (D17) and adjoint uniqueness. Section 2.1 puts it in degree \(-1\); AG-QC-15 Theorems 4.1–4.2 identify its sheaf and trace with the classical representing pair. This gives (D3), with all identifications natural in \(L\). It does not select an arbitrary nonzero functional on each fibre independently.

For the family itself, specializing (D17) to \(K=\mathcal O_X\) on affine base charts gives, with the same trace,
\[
Rf_*\omega_{X/S}
 \cong R\mathcal H om_S(Rf_*\mathcal O_X,\mathcal O_S)[-1].
\tag{D21}
\]
The comparison is canonical and the local comparisons glue. The complex \(Rf_*\mathcal O_X\) is perfect: this follows on projective charts from §4. For the exact descent of perfectness, let an A-complex become perfect after faithfully flat tensor with B. Its bounded cohomology range descends by faithfulness. Pseudo-coherence descends by successively choosing finite generators of the top cohomology, lifting a finite free module to the complex and repeating with its cone; finite generation descends faithfully flat, so this constructs each finite portion of a bounded-above finite free approximation over A. Its finite Tor-amplitude descends as well: for every A-module M, the cohomology of (M⊗_A^L P)⊗_A B equals the cohomology after base change and is zero outside the fixed amplitude. Faithfulness reflects that vanishing. A pseudo-coherent complex with finite Tor-amplitude is perfect: truncate its finite free approximation at the lower amplitude bound; the last quotient is flat by the Tor test and finitely presented by the approximation, hence finite projective. This proves the descent used here, not only descent of the ranks of cohomology. Its formation, and therefore that of its derived dual, commutes with arbitrary base change, first on those charts by (D10) and then by descent. Formula (D21) supplies the formal relative-duality identity used in the genus-one argument. The decomposition, rank-one Hodge bundle and evaluation consequences are the genus-one argument in Lesson 5; they are not silently assumed or reproved here.

The nodal normalization computation in §5.1 retains its residue condition and \(dx/x=-dy/y\) sign. Lemmas 5.0.1 and 5.0 supply the fibrewise global-generation input. The relative-ampleness and global ringed-space deformation prerequisites retain their exact recorded scope.

### A.9. Sources, provider scope and concrete corrections

The baseline is the AI Integrated fork `565b10e987aba5969b21145a0833f42d69f96790`, not a replacement by current upstream. The complete-scope canonical checker passed before the external body reads at the exact paths below. Sources are credited to the **Stacks Project authors, with the AI Integrated Stacks Project**; the source text itself is distributed under the GNU FDL 1.2 or later.

| Exact source ID and path | Actual loci checked for this argument | SHA-256 |
|---|---|---|
| `AGAS-NATIVE-STACKS-565B-MODULI-CURVES`; `moduli-curves.tex` | Relative dualizing section at 1820–2014; `lemma-CM-dualizing` 1903–1947, relative representing statement 1962–1982, `lemma-gorenstein-dualizing` (0E6N) 1985–2000. These show the exact arbitrary-base/fibre contract and where its original relative inputs occur. | `d4dba83e25d3aea239197824bca0706b650917000540ef4d324a87feaeaf41fe` |
| `AGAS-NATIVE-STACKS-565B-SPACES-DUALITY`; `spaces-duality.tex` | `lemma-more-base-change` 1000 and its perfect-generator comparison through 1075; `lemma-properties-relative-dualizing` 1613–1715; definition 1762–1789 and remarks, uniqueness 1855–1922, covering argument 1925–2010, existence 2013–2098, arbitrary base change 2101–2123, scheme comparison beginning 2138. The present proof uses line-bundle/Amitsur descent rather than leaving their derived gluing reference unbound. | `3cfcef73eb9172cf69082ff07b9d84442dd5e545d8ad22917d5a694baa57298e` |
| `AGAS-NATIVE-STACKS-565B-DUALITY`; `duality.tex` | `lemma-more-base-change` 1419 and Hom-complex calculation 1442–1545; proper-flat relative description 2675–2768; `lemma-properties-relative-dualizing` 2811–2880; fibre description 4934–4951; flat/CM discussion 5695–5817; CM criterion 6088–6123; field/local Gorenstein discussion 6170–6263 and `lemma-affine-flat-Noetherian-gorenstein` 6526–6569; general scheme-relative construction 7331–7509. The complete AG-AS scope extension reuses the same existing bytes as prior ID `AGGS-NATIVE-STACKS-565B-DUALITY-TEX`; it creates no duplicate source. | `2a0b9b65c79ec3fb149937b8b65cdb0a0021360637b46bdce9334ae1989f8287` |
| `AGAS-NATIVE-STACKS-565B-DUALIZING`; `dualizing.tex` | `lemma-dualizing` 2617–2644, `lemma-equivalence-comes-from-invertible` 2658–2715, uniqueness 2718–2746, localization 2749–2773; CM characterization 3641–3671, Gorenstein definition 3747–3764 and discussion through `lemma-gorenstein` 3797–3850. Section 2 supplies the required local shifted-line argument and its finite-length detection rather than ending at the external uniqueness reference. | `b1262987c3041fd1b15fbae46a0cc66dc9ba2c28917ed32330e4904981b131c2` |
| `AGAS-NATIVE-STACKS-565B-MORE-ALGEBRA`; `more-algebra.tex` | Finite-length detection 17490–17521; faithfully flat pseudo-coherence descent 17113–17149, Tor-amplitude descent 17917–17938, perfect descent 19776–19791; lifting a perfect complex 20273–20304, cutting a pseudo-coherent complex 20546–20594 and recognition 20679–20708; technical Hom evaluation 29296–29329. Sections 2.1–2.2 and 8 include the actual needed arguments. | `9b91629d8401d8f4fc439ef834cd69adc75e89b1ed59a75ba4fdd01daff52ad4` |

The exact external editions can be identified publicly, with credit, by their pinned native files: [relative duality for curves](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/moduli-curves.tex), [space duality](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/spaces-duality.tex), [scheme duality](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/duality.tex), [dualizing-complex algebra](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/dualizing.tex), and [complex algebra](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex). These are source credits; the links are not substituted for the proofs above.

The independently authored programme copies inspected in this pass have the following exact bindings. These hashes identify the copies actually consulted.

| Owned proof/provider copy | Exact inspected use | SHA-256 |
|---|---|---|
| Lesson 8, Appendix A | §8 at 369–421, with the endpoint/projectivity discussion at 405–419; §12.10 at 1700–1715; §12.11 at 1716–1819, including its actual nonreduced, conductor-gluing and endpoint arguments. | `113ffff6408ca0a9db6347c0e75b455dc3c09c5a98ce5e0cd6da5c20e5be7cbd` |
| `AG-QC/src/dualizing-sheaves-and-serre-duality-for-projective-schemes.md` | Actual field convention at 9; Lemma 2.1 at 36–54; Theorem 4.1 at 103–119; Theorem 4.2 at 121–131, trace uniqueness 26–30. | `8a1e9a90e823573812b97da5bec58145a5ee83c20279eee5d52898c8ff5b495a` |
| `AG-QC/src/the-right-adjoint-of-derived-pushforward.md` | Right-adjoint foundation at 13–21; formal Proposition 1.1 and trace at 23–51; finite coinduction Theorem 3.1 at 103–125; field projective-space proof 141–156, stated relative formula 158–164, field comparison 173–198; actual external foundation status 265–273. | `3f4b6d58ebe05b7dc79df8c92102b68a277d68c69478b9dd4e8dd8dadf35a551` |
| `AG-QC/src/base-change-and-the-grothendieck-complex.md` | Written bounded-flat replacement Lemma 3.1 at 87–127, Noetherian Theorem 3.2 and derived comparison at 131–145. | `7898ae00c5e1cb52c1fde692e5a2c9e7866cb1bb1c78bc8b194ac4f6c6d552e1` |
| `AG-MO/src/limits-and-noetherian-approximation.md` | Actual Theorem 5.2 at 153–164 owns the prescribed-open 07RN route, with full internal proof still planned. It does not have the title or lesson number of Zariski's Main Theorem. | `d59e25ddc9da72a99e5a9329a1e6e54da3425ae95f06597ab759811fc5051bcd` |
| Lesson 3 §5.6.7 C.1 | Integrated Lesson 3 §5.6.7 C.1 at 685–703, flat Noetherian model proof, with its genuine AG-MO-03 prerequisite retained. | `22fdb7bbcefad3e38d97ecccd151c4965408a305fcb18a72e055e642e215a604` |
| `work/site/courses/AG-HP/src/the-cotangent-complex.md` | Actual §10 global ringed-space input at 541; §13 at 600 explicitly retains its stated status. The ringed-space extension classification is not upgraded to a written proof here. | `059ae04881879078b704908728aafd93a00ef592ecee4a1c2f9cf4b7f4c8fed5` |

The commutative-algebra bindings use the actual current 23-unit edition and the following named providers.

| Current file and title | Written locators used | SHA-256 |
|---|---|---|
| `noetherian-and-artinian-rings.md`, *Noetherian and Artinian rings* | Theorem 5.1 at 208 (Artin–Rees), Theorem 6.1 at 254 (Krull intersection). | `29f0673829fc3464c064854e402ed16387d00f9ea2faf8ca906a837871828c11` |
| `faithful-flatness-and-the-local-criterion-for-flatness.md`, *Faithful flatness and the local criterion for flatness* | Theorem 3.1 at 91 and Corollary 3.2 at 106; Theorem 4.2 at 134–177, Noetherian local map and finite target-module hypotheses; fibre criterion Theorem 5.4 at 249. | `e101e670904bea5f8310d5fe4e6b5ace3cb68cd8d4942ca680ba808d8c58319e` |
| `regular-sequences-depth-and-cohen-macaulay-modules.md`, *Regular sequences, depth and Cohen–Macaulay modules* | Theorem 4.1 at 194, Theorem 4.2 at 205, CM localization Theorem 5.1 at 226, regular-local CM Theorem 6.1 at 281. | `2b5e3bf9f723af5187a07ca9fdc1877d1e1c3d22ccd940dfc47fad0ac8e4417b` |
| `projective-dimension-and-the-auslander-buchsbaum-formula.md`, *Projective dimension and the Auslander–Buchsbaum formula* | Theorem 1.3 at 48, minimal resolution/Tor Theorem 2.2 at 117–145, local global-dimension Theorem 2.3 at 147–153, Auslander–Buchsbaum Theorem 3.1 at 157. | `bdc62573c6bc18222838a2ab66fe5ae67a133d4a2be31e33c5c256e1c61341a4` |
| `regular-local-rings.md`, *Regular local rings* | Theorem 2.2 at 126–154, explicitly bounding **arbitrary** modules by global dimension = Krull dimension; localization Theorem 3.2 at 171; polynomial regularity Proposition 3.3 at 185. Finite injective dimension in §2.1 is deduced by Ext dimension shifting, not attributed to an unstated theorem. | `5ff9e6d477b256fe256719cf51a334f2eb8d47220d035473f51039daed2eabce` |

#### Concrete source corrections

1. In `duality.tex`, `lemma-CM-shriek`, line 5815 prints the affine-space comparison with shift \([-d]\). The theorem, projective-space normalization and cohomological convention require \([d]\): the sheaf must lie in degree \(-d\). The present route computes the shift in (D8), (D14) and §2.1, and retains \([1]\) for curves. It does not silently reproduce the printed sign.
2. In `dualizing.tex`, line 2703 says the detecting map for a cohomology degree \(j<a\) has \(i<0\) in the target \(E[-a+i]\). Solving \(-a+i=-j\) gives \(i=a-j>0\). The contradiction still works because the Hom group vanishes for **every** \(i\ne0\). Equation (D5) and its application retain that correct quantifier and do not rely on the erroneous inequality.
3. In the general space existence proof, `spaces-duality.tex` lines 2044–2046 and 2060–2062 pull back the object indexed by the source of the map rather than its target. With \(g_{\varphi,i}:Y_{n,i}\to Y_{m,\alpha(\varphi)(i)}\), the typed comparison is
\[
L(g'_{\varphi,i})^*\omega_{m,\alpha(\varphi)(i)}
 \longrightarrow\omega_{n,i}.
\]
The trace has the corresponding base pullback. The comparisons in §7 are typed in this direction and satisfy their cocycle by uniqueness. No generally unassigned derived-gluing theorem is claimed as a programme provider.
4. The existing field recognition proof is about local-ring dimension at most one. Its old “codimension one” slogan is not used to weaken or alter that statement. The projectivity proof keeps nonreduced, reducible, disconnected, zero-dimensional and empty cases where they belong; the uniform \([1]\) duality statement keeps the separate pure-one-dimensional hypothesis.

The genuine scheme-approximation, Brown-representability, site-cohomology and global deformation prerequisites marked planned in §1 retain their stated scope and state.

The text of this lesson is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

## History

**Source edition.** *The Stacks Project*, by the Stacks Project authors (copyright 2005–2025 Johan de Jong), distributed in the *AI Integrated Stacks Project*, 2026 edition at revision `565b10e987aba5969b21145a0833f42d69f96790` (30 September 2026). The source publisher is the Stacks Project; the fork distribution and its separately credited AI changes are identified by the pinned repository and its [retained source provenance](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/PROVENANCE.md). The [source application notice](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/introduction.tex) supplies the source's licence grant (GNU FDL 1.2 or later), and [the pinned transparent source](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790) preserves the source files and their prior network locations.

**Course edition.** *Algebraic spaces and stacks — The stack of curves*, October 2026, published by the Open Math Courses project, `KokunoYumeto/open-math-courses`. Written and integrated by GPT-6.1 Sol (OpenAI), Codex, Ultra, 5–6 October 2026: arbitrary-base relative Gorenstein duality, its trace and coherent comparison maps. Independently expressed local lci smoothing and subcurve global-generation proofs supplement the main curve treatment. The relative shift and typed pullback comparisons correct concrete source errors. No AI copyright holder or human endorsement is asserted. The detailed source loci, exact edition and concrete corrections remain in this chapter. The text is dedicated to the public domain under CC0 1.0.
