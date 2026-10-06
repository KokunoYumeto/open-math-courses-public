# Locally compact groupoids and Haar systems

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A crossed product remembers arrows supplied by a group action. A groupoid keeps the arrows, their sources and their targets, without requiring one group to describe every orbit. Integration is then a family of measures on the arrow fibres. Continuity of that family is an additional condition, and it has consequences for the topology.

Our main convention is to integrate on range fibres with left-invariant measures. We first work with Hausdorff arrow spaces. We then explain the locally Hausdorff convention needed for holonomy groupoids, using an explicit group bundle with two inseparable arrows.

## Reversible arrows

A groupoid \(\mathcal G\rightrightarrows X\) has a unit space \(X=\mathcal G^{(0)}\), range and source maps \(r,s:\mathcal G\to X\), and a product on
\[
 \mathcal G^{(2)}=\{(\gamma,\eta):s(\gamma)=r(\eta)\}.
 \tag{13.1}
\]
An arrow \(\gamma\) goes from \(s(\gamma)\) to \(r(\gamma)\); \(\gamma\eta\) means first \(\eta\), then \(\gamma\). The product is associative when defined, has the units at each end, and every arrow has an inverse:
\[
 \begin{gathered}
 r(\gamma)\gamma=\gamma=\gamma s(\gamma),\\
 \gamma\gamma^{-1}=r(\gamma),\qquad
 \gamma^{-1}\gamma=s(\gamma),\\
 r(\gamma\eta)=r(\gamma),\qquad
 s(\gamma\eta)=s(\eta).
 \end{gathered}
 \tag{13.2}
\]
We identify a unit with its identity arrow. A topological groupoid has continuous unit inclusion, range, source, inverse and multiplication, the latter with the subspace topology on (13.1).

The fibres and isotropy groups are
\[
 \mathcal G^x=r^{-1}(x),\qquad
 \mathcal G_x=s^{-1}(x),\qquad
 \mathcal G_x^x=\mathcal G^x\cap\mathcal G_x.
 \tag{13.3}
\]
Two units lie in the same orbit if some arrow connects them. In particular
\[
 \mathcal G\cdot x=r(\mathcal G_x).
 \tag{13.4}
\]
Isotropy is a group at one unit. An arrow from \(x\) to \(y\) identifies the two isotropy groups by \(h\mapsto\gamma h\gamma^{-1}\); changing the arrow can change this identification by an inner automorphism.

Except in the explicitly non-Hausdorff section, both \(X\) and \(\mathcal G\) are locally compact Hausdorff. Second countability will be stated when a theorem requires it. A groupoid is **principal** if all its isotropy groups are trivial, equivalently if \((r,s)\) is injective: two arrows with the same endpoints differ by an isotropy arrow. It is **proper** if \((r,s):\mathcal G\to X\times X\) is proper. These are separate conditions.

Basic examples fix the meaning of these definitions.

- A group \(H\) is a groupoid with one unit. A space \(X\) is a groupoid with only identity arrows.
- The pair groupoid \(X\times X\) has \(r(x,y)=x\), \(s(x,y)=y\), inverse \((y,x)\), and \((x,y)(y,z)=(x,z)\). It has one orbit when \(X\) is nonempty and has trivial isotropy.
- An equivalence relation \(R\subseteq X\times X\) has those same operations. It is a topological groupoid in the subspace topology, but local compactness of \(R\) is an extra condition. The relation for the partition into singletons is the diagonal, not the empty set.
- For a continuous map \(p:X\to B\), the fibre-pair groupoid is \(X\times_B X=\{(x,y):p(x)=p(y)\}\). If \(X,B\) are locally compact Hausdorff, this is closed in \(X\times X\), hence locally compact; its orbits are the fibres of \(p\).
- A topological group bundle has \(r=s:\mathcal G\to X\), with each fibre a group and with jointly continuous multiplication, inverse and unit inclusion. Giving a quotient map and separate topological group structures on its fibres does not by itself impose this joint continuity.

## Transformation groupoids

Let a locally compact group \(H\) act continuously on a locally compact Hausdorff space \(X\) on the left. We use coordinates with the target written first:
\[
 \begin{gathered}
 X\rtimes H=X\times H,\qquad
 r(x,g)=x,\qquad s(x,g)=g^{-1}x,\\
 (x,g)(g^{-1}x,h)=(x,gh),\\
 (x,g)^{-1}=(g^{-1}x,g^{-1}).
 \end{gathered}
 \tag{13.5}
\]
The units are \((x,e)\).

**Proposition 13.1.** These formulas make \(X\rtimes H\) a locally compact Hausdorff groupoid. Its orbits are the \(H\)-orbits in \(X\), and its isotropy at \(x\) is the stabilizer \(H_x\).

**Proof.** The arrow space is a product of locally compact Hausdorff spaces. The composable-pair space is parametrized by \((x,g,h)\mapsto((x,g),(g^{-1}x,h))\), with continuous inverse given by the displayed coordinates. Product and inverse are therefore continuous. The action law verifies all identities (13.2), and associativity reduces to the group law.

An arrow with source \(y\) and label \(g\) has target \(gy\), so (13.4) is \(Hy\). An arrow \((x,g)\) has both endpoints \(x\) exactly when \(g^{-1}x=x\), that is, \(g\in H_x\); multiplication there is the stabilizer group law. ∎

For a homeomorphism \(T:X\to X\), take \(H=\mathbb Z\), \(n\cdot x=T^n x\). Then
\[
 s(x,n)=T^{-n}x,\qquad
 (x,n)(T^{-n}x,m)=(x,n+m).
 \tag{13.6}
\]
The isotropy is \(\{n:T^n x=x\}\): it vanishes at a nonperiodic point and is \(q\mathbb Z\) at a point of least positive period \(q\).

## Local homeomorphisms and counting measures

A topological groupoid is **étale** when \(r:\mathcal G\to X\) is a local homeomorphism. Inversion implies the same property for \(s\). Both maps are open, since an arbitrary open set is a union of open chart pieces and each chart maps them to open subsets of \(X\). Intersecting a range chart with a source chart gives an **open bisection**: an open set \(U\subseteq\mathcal G\) on which both \(r\) and \(s\) are homeomorphisms onto open subsets of \(X\).

The unit space is open in an étale groupoid. To verify this without assuming it, choose a source chart \(U\) about the identity at \(x\). The set
\(O=s(U)\cap e^{-1}(U)\) is open in \(X\), where \(e\) is the unit inclusion. For \(y\in O\), both \(e(y)\) and the chart inverse of \(y\) lie in \(U\) and have source \(y\), so they coincide. Thus
\[
 e(O)=(s|_U)^{-1}(O)
 \tag{13.7}
\]
is open in \(\mathcal G\), giving the claim. Each source or range fibre is discrete, because a bisection meets it in at most one point.

A **left Haar system** is a family of positive Radon measures \(\lambda^x\) on the fibres \(\mathcal G^x\) such that each has full support, the function
\[
 \lambda(f)(x)=\int_{\mathcal G^x} f(\eta)\,d\lambda^x(\eta)
 \tag{13.8}
\]
is continuous for every \(f\in C_c(\mathcal G)\), and left multiplication preserves the measures:
\[
 \int_{\mathcal G^{s(\gamma)}} f(\gamma\eta)\,d\lambda^{s(\gamma)}(\eta)
       =\int_{\mathcal G^{r(\gamma)}}f(\eta)\,d\lambda^{r(\gamma)}(\eta).
 \tag{13.9}
\]
The support of (13.8) lies in the compact set \(r(\operatorname{supp}f)\), so it is also compactly supported. Full support is part of the definition; permitting zero fibre measures would invalidate the openness result below.

**Proposition 13.2.** Every locally compact Hausdorff étale groupoid has the counting Haar system
\[
 \lambda^x(f)=\sum_{\eta\in\mathcal G^x}f(\eta).
 \tag{13.10}
\]

**Proof.** Each fibre is closed and discrete. Its counting measure is Radon: a compact subset of a discrete space is finite. It has full support. Left multiplication is a bijection between the two fibres in (13.9), proving invariance.

For continuity, cover the compact support of \(f\) by finitely many bisections and use a compact-support partition of unity to write \(f=\sum_j f_j\), with \(\operatorname{supp}f_j\) compact inside a bisection \(U_j\). For one such term, (13.10) is \(f_j((r|_{U_j})^{-1}(x))\) on \(r(U_j)\) and zero elsewhere. Its support is compact inside that open set, so extension by zero is continuous on \(X\). Summing proves (13.8). ∎

The same proof applies to the patch-based function space in the locally Hausdorff étale case described below: decompose each compact Hausdorff-patch term into bisection terms inside that patch.

## Haar systems for actions and pairs

**Proposition 13.3.** Fix a left Haar measure \(dg\) on \(H\). The transformation groupoid (13.5) has the Haar system
\[
 \lambda^x(f)=\int_H f(x,g)\,dg.
 \tag{13.11}
\]

**Proof.** The map \(g\mapsto(x,g)\) identifies the range fibre with \(H\), so this is a full-support Radon measure. Left multiplication by \((x,a)\) carries \((a^{-1}x,g)\) to \((x,ag)\), preserving it by left invariance of \(dg\).

If \(f\) has compact support, its group coordinates lie in a common compact set \(K\subseteq H\). Near any fixed \(x_0\), restrict \(x\) to a compact neighborhood. Continuity of \(f\) on the resulting compact product gives uniform continuity in \(x\), in the sense that \(\sup_{g\in K}|f(x,g)-f(x_0,g)|\to0\). One may prove this by finitely many product neighborhoods covering \(\{x_0\}\times K\). Multiplication by the finite Haar measure of \(K\) now bounds the difference between the two integrals. This proves continuity. ∎

For the pair groupoid, a positive full-support Radon measure \(\mu\) on \(X\) gives
\[
 \lambda^x(f)=\int_X f(x,y)\,d\mu(y).
 \tag{13.12}
\]
The same compact-product continuity argument applies, while left multiplication changes only the first coordinate. For \(X=\mathbb R\) with Lebesgue measure, the range fibre at \(x\) is \(\{x\}\times\mathbb R\) with ordinary Lebesgue integration in its second coordinate. Its groupoid algebra will be the compact-operator example in Lesson 14.

## A Haar system forces open range

**Theorem 13.4.** A locally compact Hausdorff groupoid with a Haar system has open range and source maps.

**Proof.** Let \(U\subseteq\mathcal G\) be open and \(\gamma\in U\). Choose \(f\in C_c(\mathcal G)\), \(f\geq0\), with \(f(\gamma)>0\) and support contained in \(U\). Full support of \(\lambda^{r(\gamma)}\) makes its integral positive: \(f\) is bounded below by a positive number on a nonempty relatively open piece of that fibre. By continuity,
\[
 V=\{x:\lambda(f)(x)>0\}
 \tag{13.13}
\]
is an open neighborhood of \(r(\gamma)\). A positive integral requires the fibre to meet \(U\), so \(V\subseteq r(U)\). This works for each arrow in \(U\), proving that \(r(U)\) is open. Inversion gives openness of \(s\). ∎

In a locally Hausdorff groupoid, choose the bump in a Hausdorff open patch contained in \(U\), and extend it by zero. If (13.8) is required for patch functions, this same proof still works. Global continuity of that zero extension is unnecessary.

## Continuous Haar measures on a group bundle

For a **group bundle**, range and source agree: every fibre \(\mathcal G_x=r^{-1}(x)\) is a locally compact group, with identity \(e_x\). Individual Haar measures always exist. The issue is their normalization across different fibres.

**Theorem (Haar systems on group bundles).** A second countable locally compact Hausdorff group bundle with open range map has a Haar system.

**Proof.** Fix \(x_0\). Choose \(b\in C_c(\mathcal G)\), \(b\geq0\), with \(b(e_{x_0})>0\). On the open neighborhood
\[
V=\{x:b(e_x)>0\}
\tag{13A.1}
\]
choose the left Haar measure \(\mu_x\) of \(\mathcal G_x\), normalized by \(\mu_x(b)=1\). This is possible and unique: the integral is finite by compact support and positive because \(b\) is positive on a neighborhood of the identity. We first prove continuity of this normalized family on \(V\).

We need a local bound. If \(K\subset\mathcal G\) is compact, then
\[
\sup_{x\in W}\mu_x(K\cap\mathcal G_x)<\infty
\tag{13A.2}
\]
for some neighborhood \(W\subset V\) of \(x_0\). If \(K\cap\mathcal G_{x_0}\) is empty, compactness of \(r(K)\) gives such a neighborhood with empty intersections. Otherwise choose finitely many open sets \(O_1,\ldots,O_m\), centered at points of that intersection, covering it, and small enough that
\[
b(g^{-1}h)\geq c>0
\quad\text{whenever }g,h\in O_j\text{ belong to the same fibre}.
\tag{13A.3}
\]
To obtain them, use continuity of \((g,h)\mapsto g^{-1}h\) at each pair \((g_j,g_j)\), where the value is \(e_{x_0}\), and take a common positive lower bound for the finite family. Openness of \(r\) makes every \(r(O_j)\) a neighborhood of \(x_0\). The compact set \(K\setminus\bigcup_jO_j\) has range avoiding \(x_0\). Shrinking \(W\), therefore, makes \(K\cap\mathcal G_x\subset\bigcup_jO_j\) and makes each \(O_j\cap\mathcal G_x\) nonempty for \(x\in W\).

Choose \(g_j^x\in O_j\cap\mathcal G_x\); continuity of these choices is unnecessary. On \(K\cap\mathcal G_x\), the sum \(\sum_j b((g_j^x)^{-1}h)\) is at least \(c\). Each summand has integral one by left invariance. Hence \(\mu_x(K\cap\mathcal G_x)\leq m/c\), proving (13A.2).

Now let \(x_n\to x_0\) in \(V\), and regard the measures as measures on \(\mathcal G\), supported on their closed fibres. Bound (13A.2) gives a uniform bound on each compact set, including the finitely many initial terms. Such a sequence has a vaguely convergent subsequence. Here is the measure-compactness step explicitly. Exhaust the second countable locally compact space by compact sets whose interiors cover it. On each interior choose a countable dense subset of its compactly supported continuous test functions in the supremum norm, using compact subsets of a slightly larger exhaustion set. Successive subsequences and a diagonal choice make the integrals converge on all these test functions. The uniform compact-set bounds extend convergence to every \(f\in C_c(\mathcal G)\). The resulting positive linear functional is bounded on each compact-support space; the Riesz representation theorem gives its Radon measure \(\mu\).

This limit is supported on \(\mathcal G_{x_0}\): a compact test support disjoint from that fibre has compact range avoiding \(x_0\), so its integrals eventually vanish. Moreover \(\mu(b)=1\). We show left invariance. Fix \(g\in\mathcal G_{x_0}\). Openness of \(r\), with a countable neighborhood basis at \(g\), gives choices \(g_n\in\mathcal G_{x_n}\) tending to \(g\). Indeed, eventually \(x_n\) belongs to the range of each basis neighborhood; choose in successively smaller neighborhoods.

For \(f\in C_c(\mathcal G)\), extend the function \(h\mapsto f(gh)\) on the closed fibre \(\mathcal G_{x_0}\) to some \(F\in C_c(\mathcal G)\). Such an extension follows by a compact-support bump and the Tietze extension theorem on the second countable locally compact Hausdorff space; the original fibre function has compact support. All supports involved in \(f(g_nh)\) and \(F(h)\) lie in one compact set \(Q\): use compactness of \(\{g,g_1,g_2,\ldots\}\), compactness of \(\operatorname{supp}f\), and continuity of inversion and multiplication on the closed composable-pair set. We have
\[
\sup_{h\in Q\cap\mathcal G_{x_n}}
       |f(g_nh)-F(h)|\longrightarrow0.
\tag{13A.4}
\]
Otherwise points witnessing a fixed positive error have a convergent subsequence in \(Q\). Its limit belongs to \(\mathcal G_{x_0}\), and multiplication continuity and the defining equality of \(F\) there contradict that error. Bound (13A.2) for \(Q\) permits integration of (13A.4). Passing to the vague limit in
\[
\int f(g_nh)\,d\mu_{x_n}(h)=\int f(h)\,d\mu_{x_n}(h)
\tag{13A.5}
\]
therefore gives \(\int f(gh)\,d\mu(h)=\int f(h)\,d\mu(h)\). Restrictions of the ambient compactly supported functions include all compactly supported fibre functions by the same extension argument. Thus \(\mu\) is a nonzero left invariant Radon measure of \(\mathcal G_{x_0}\). Haar uniqueness and \(\mu(b)=1\) identify it with \(\mu_{x_0}\).

Every subsequence has a further vaguely convergent subsequence, and the preceding argument identifies every such limit. It follows that \(\mu_{x_n}(f)\to\mu_{x_0}(f)\) for each test function. The same proof works at every point of \(V\), with this fixed \(b\). First countability of the unit space turns this sequential assertion into continuity. The use of sequences here is justified by the theorem's second countability hypothesis.

Finally cover the unit space by neighborhoods \(V_j\) obtained from such functions \(b_j\), and take a locally finite partition of unity \((\rho_j)\) subordinate to a shrinking of this cover, with \(\operatorname{supp}\rho_j\subset V_j\). This exists because a second countable locally compact Hausdorff space is paracompact. Put
\[
\lambda^x=\sum_j\rho_j(x)\mu_x^j.
\tag{13A.6}
\]
At a fixed \(x\) this is a finite positive combination of Haar measures of the same group. It is Radon, left invariant, nonzero, and has full support because the coefficients sum to one. For each \(f\in C_c(\mathcal G)\), local finiteness and the continuity proved above make \(x\mapsto\lambda^x(f)\) continuous; each summand extends by zero outside \(V_j\) because its coefficient has closed support inside \(V_j\). This is the required Haar system. ∎

The group-bundle existence theorem is recorded in Li, *Groupoid C*-algebras*, Theorem 9.8. Its proof here uses Haar uniqueness, uniform local mass bounds and compactness of measures; an open range map alone is not being asserted sufficient for an arbitrary groupoid.

## Lie groupoids and density conventions

A Lie groupoid has smooth arrow and unit manifolds, smooth operations, and range and source submersions. The unit manifold is Hausdorff; the arrow manifold can be locally Hausdorff, with Hausdorff arrow fibres, as in the holonomy case. In the Hausdorff case a smooth Haar system can be constructed as follows.

Choose a smooth strictly positive density on the vector bundle
\(E=\ker(dr)|_X\). Such a density exists on a second countable unit manifold: choose a bundle metric using a smooth partition of unity, and take its volume density. For an arrow \(\gamma\), the differential of
\[
 L_\gamma:\mathcal G^{s(\gamma)}\longrightarrow
                    \mathcal G^{r(\gamma)},\qquad \eta\mapsto\gamma\eta
 \tag{13.14}
\]
transports the density at the identity of \(s(\gamma)\) to a density at \(\gamma\). Smooth multiplication makes these fibre densities smooth in groupoid charts. Associativity makes them left invariant. Their strict positivity gives full support.

Their fibre integrals are continuous, and are smooth for smooth compactly supported test functions. Indeed a submersion chart has coordinates \((x,z)\) in which \(r(x,z)=x\); integration there has a smooth positive density factor \(a(x,z)\,dz\). A compact-support partition of unity reduces the assertion to finitely many such charts. Continuity follows from uniform continuity and a common compact \(z\)-support, and derivatives pass under that same compact integral. Thus these densities give a Haar system. The same chart argument uses compact patch sections in the locally Hausdorff smooth case.

The choice of density can be avoided in the convolution notation. Write
\[
 \Omega^{1/2}_\gamma
  =|\Lambda^{\mathrm{top}}\ker(dr)_\gamma^*|^{1/2}
       \otimes|\Lambda^{\mathrm{top}}\ker(ds)_\gamma^*|^{1/2}.
 \tag{13.15}
\]
For a composable pair, groupoid translations identify the two middle half-density factors. Their product is a full density in the integration variable, while the two outer factors remain half-densities at the endpoints. This makes
\[
 (a*b)(\gamma)=\int_{\eta\zeta=\gamma}a(\eta)b(\zeta)
 \tag{13.16}
\]
intrinsic. Inversion exchanges the endpoint factors; the involution also complex conjugates the section. A positive density trivialization recovers scalar-valued kernels and a Haar measure. These are the conventions of [Connes 1994]. The C*-completion and its regular representations are developed in Lesson 14.

## The non-Hausdorff test-function space

Suppose \(\mathcal G\) is locally Hausdorff and locally compact, with locally compact Hausdorff unit space and Hausdorff fibres. The notation \(C_c(\mathcal G)\) now means the linear span of the zero extensions of elements of \(C_c(U)\), where \(U\subseteq\mathcal G\) is Hausdorff and open. The compact support is taken inside \(U\). Its image in \(\mathcal G\) is compact but need not be closed. Zero extension need not be globally continuous.

This definition agrees with ordinary \(C_c\) for Hausdorff \(\mathcal G\), by a finite compact-support partition of unity. In the locally Hausdorff case the same argument partitions an individual patch term into smaller Hausdorff patches; hence using a Hausdorff patch basis gives the same span. Haar continuity is required for these test functions. On a smooth groupoid use smooth patch sections of (13.15) in the same way.

Here is a complete example. Start with two copies of \(\mathbb R\), identify their nonzero points, and leave the two origins distinct. Denote the origins by \(e_0,\sigma_0\), and the nonzero arrow at \(x\) by \(e_x\). Let the ordinary line be the unit space, with unit arrow \(e_x\), and set
\[
 \begin{gathered}
 r=s:\mathcal G\to\mathbb R,\qquad r(e_x)=x,\quad r(\sigma_0)=0,\\
 \mathcal G_x^x=\{e_x\}\quad(x\ne0),\qquad
 \mathcal G_0^0=\{e_0,\sigma_0\}\cong\mathbb Z/2.
 \end{gathered}
 \tag{13.17}
\]
All arrows are self-inverse, and \(\sigma_0^2=e_0\). The two open charts \(U_+\), \(U_-\) contain, respectively, \(e_0,\sigma_0\) and all the nonzero arrows. Each is homeomorphic to \(\mathbb R\) by \(r\). They make this a locally compact locally Hausdorff étale groupoid. To check multiplication continuity, use a chart at each member of a composable pair. Both members have the same base coordinate \(x\); the product lies in the plus chart when the two chart signs agree, and in the minus chart when they differ. In those coordinates multiplication is the identity map in \(x\). These charts cover the composable-pair space, proving continuity. The unit section is \(U_+\), which is open and not closed.

A patch function is a sum of a plus-chart extension \(\phi_+\) and a minus-chart extension \(\psi_-\), where \(\phi,\psi\in C_c(\mathbb R)\). All patch functions have this form: partition each original Hausdorff-patch term over its intersections with the two charts. If
\[
 F=\phi+\psi,\qquad a=\phi(0),\qquad b=\psi(0),
 \tag{13.18}
\]
the function has value \(F(x)\) at \(e_x\) for \(x\ne0\), value \(a\) at \(e_0\), and value \(b\) at \(\sigma_0\). Therefore the whole test-function space is exactly
\[
 C_c(\mathcal G)\cong
   \{(F,a,b):F\in C_c(\mathbb R),\ a,b\in\mathbb C,\ F(0)=a+b\}.
 \tag{13.19}
\]
For the converse, choose \(\phi\in C_c(\mathbb R)\) with value \(a\) at zero and put \(\psi=F-\phi\). The condition gives \(\psi(0)=b\), so this represents the prescribed triple.

Counting measures on the fibres integrate this function to \(F(x)\): at zero their integral is \(a+b=F(0)\). Thus they are a continuous Haar system for the patch space.

This example gives a precise meaning to the failure of naive continuous test functions. Global continuity forces both origin values and the limit of the nonzero values to be equal. If the function is also in (13.19), write that common value as \(c\); the compatibility says \(c=2c\), so \(c=0\). A plus-chart bump with \(\phi(0)=1\) is an allowed patch function with values \(1,0\) at the origins, and is discontinuous at the second one. Conversely a globally continuous compactly supported bump with both origin values \(1\) fails (13.19). Its counting integral has value \(2\) at zero and limit \(1\), so it cannot be used as a Haar-continuity test.

Consequently the naive space is not even a subspace of the intended patch space in this example. It misses necessary local functions and also admits functions with the wrong integration continuity. Moreover (13.19) is not closed under pointwise multiplication. Multiply equal plus and minus bumps of value one at zero: the product has nonzero-coordinate limit \(1\) and both origin values \(0\), violating (13.19). The operation needed for groupoid algebras is convolution, as in Lesson 14.

For foliations, a holonomy arrow is a leafwise path modulo agreement of endpoints and transverse holonomy germs. The holonomy groupoid has the manifold as its unit space, with range and source smooth submersions; its arrow space can be non-Hausdorff. The non-Hausdorff holonomy groupoid of the Reeb foliation of the three-sphere is a stated geometric example in [Connes 1982]. The exact written construction is *The C*-algebra of a foliation*, Lemma 1.1, Lemma 2.1 and Theorem 2.2: paths modulo transverse germs give the groupoid, its locally Hausdorff arrow charts, and the Hausdorff holonomy covering of each leaf. The Reeb leaf and germ facts, including the non-Hausdorff transverse model, are proved in Lesson 16. The patch-section convention above is what allows local holonomy charts to provide test kernels.

## Orbit spaces and reductions

Give \(X/\mathcal G\) the quotient topology for the orbit map \(q:X\to X/\mathcal G\). If range and source are open, this quotient map is open: the saturation of an open \(O\subseteq X\) is
\[
 q^{-1}(q(O))=r(s^{-1}(O)),
 \tag{13.20}
\]
which is open. Properness also makes the orbit space Hausdorff. Indeed the orbit relation is the image of the proper map \((r,s)\), hence closed; if two units are unrelated, product neighborhoods avoiding this closed relation have disjoint images under the open quotient map. Local compactness follows by projecting a compact neighborhood of a lift. This repeats the topological argument for proper actions in Lesson 9, with arrows replacing group elements.

### When orbit topology is manageable

Here we require the arrow space to be Hausdorff. No Haar system is needed for the following result: open range and source maps suffice.

**Theorem (Mackey–Glimm–Ramsay).** Let \(\mathcal G\rightrightarrows X\) be a second countable locally compact Hausdorff groupoid with open range and source. The following conditions are equivalent:

1. The orbit space \(Q=X/\mathcal G\) is \(T_0\).
2. Every nonempty closed subset of \(Q\) contains a nonempty relatively open Hausdorff subspace.
3. Every orbit is locally closed in \(X\).
4. Every orbit is a \(G_\delta\) subset of \(X\).
5. For every \(x\), the range map \(\mathcal G_x\to\mathcal G\cdot x\) is open, with the orbit given its subspace topology.

Condition 2 is called *almost Hausdorff*. The result distinguishes a manageable orbit quotient from a quotient where even individual orbits have the wrong relative topology. It does not say that the entire quotient is Hausdorff. The statement appears in [Li 2024, Theorem 3.14, p. 17]; Ramsay's work supplies the groupoid version of the earlier Mackey–Glimm theory. We give the proof, including the step where open groupoid maps replace translations by group elements.

**Proof.** Write \([B]=r(s^{-1}(B))\) for saturation. Saturation is open for open \(B\), and \(q:X\to Q\) is open by (13.20). The images of a countable base of \(X\) form a countable base of \(Q\).

Orbit closures are invariant. To see this, suppose \(s(\gamma)\in\overline O\) and choose a neighborhood \(W\) of \(r(\gamma)\). There is an arrow neighborhood \(N\) of \(\gamma\) with \(r(N)\subseteq W\). Since \(s(N)\) is a neighborhood of \(s(\gamma)\), it meets \(O\). Some arrow of \(N\) therefore has both endpoints in \(O\), and its range belongs to \(W\). Thus \(r(\gamma)\in\overline O\). It follows that
\[
 q^{-1}\big(\overline{\{q(x)\}}\big)=\overline{\mathcal G\cdot x}.
 \tag{13B.1}
\]
Indeed the right side is closed and invariant, so its image is closed in the quotient; conversely the preimage on the left is a closed set containing the orbit.

#### Distinguishing points makes each orbit a countable intersection

Assume condition 1. If \(B_n\) is a countable base of \(X\), put \(U_n=[B_n]\). Membership in the \(U_n\)'s distinguishes distinct orbits, because \(q(B_n)\) is a base of the \(T_0\) quotient. Therefore
\[
 \mathcal G\cdot x=
    \bigcap_{x\in U_n}U_n
       \ \cap\ \left(X\setminus\bigcup_{x\notin U_n}U_n\right).
 \tag{13B.2}
\]
A second countable locally compact Hausdorff space is metrizable. Every closed subset \(C\) of a metrizable space is a \(G_\delta\): for nonempty \(C\) take the open sets \(\{y:d(y,C)<1/n\}\), and handle the empty set directly. The second factor in (13B.2) is closed, while the first is a countable intersection of open sets. Thus condition 4 follows.

We will use that such an orbit is Baire. Here is the relevant completeness fact. A second countable locally compact Hausdorff space has a compatible complete metric: metrize its one-point compactification and identify the original space with the closed graph of \(y\mapsto 1/d(y,\infty)\) in the product with \(\mathbb R\); the compact case is already complete. If \(O=\bigcap V_n\) is a \(G_\delta\), the graph
\[
 y\longmapsto
   \left(y,\big(d(y,X\setminus V_n)^{-1}\big)_{n\geq1}\right)
 \tag{13B.3}
\]
is closed in \(X\times\mathbb R^{\mathbb N}\). Use the value 1 when the complement is empty. A convergent graph sequence cannot approach any complement because its corresponding coordinate would diverge. The graph topology agrees with the topology of \(O\), and the product has a complete metric. Hence \(O\) is completely metrizable and Baire.

#### A Baire orbit has an open orbit map

Fix \(x\), put \(O=\mathcal G\cdot x\), and let \(H=\mathcal G_x^x\). Right multiplication makes \(H\) act freely and properly on \(\mathcal G_x\). In fact
\[
 (\alpha,h)\longmapsto(\alpha,\alpha h)
 \tag{13B.4}
\]
is a homeomorphism onto the closed relation
\(\{(\alpha,\beta):r(\alpha)=r(\beta)\}\); its inverse uses \(\alpha^{-1}\beta\). The quotient \(Y=\mathcal G_x/H\) is consequently locally compact Hausdorff, by the proper-quotient argument above. Its quotient map \(\pi\) is open since it is a group-action quotient. Thus \(Y\) is second countable and \(\sigma\)-compact. Range descends to a continuous bijection
\[
 b:Y\longrightarrow O,
 \qquad b([\alpha])=r(\alpha).
 \tag{13B.5}
\]
Injectivity follows because two arrows with the same range differ by the right isotropy element \(\alpha^{-1}\beta\).

Suppose condition 4 holds. Exhaust \(Y\) by compact sets \(K_n\). Each \(b(K_n)\) is compact and closed in the Hausdorff orbit \(O\), and their union is \(O\). The Baire property gives a nonempty open \(J\subseteq O\) contained in some \(b(K_n)\). A continuous bijection from a compact space to a Hausdorff space is a homeomorphism, so \(b^{-1}\) is continuous on \(J\).

We must propagate this local information without assuming local bisections. The groupoid \(\mathcal G|_O\) acts continuously on \(Y\) by
\(\gamma[\alpha]=[\gamma\alpha]\). This descends from multiplication: the pullback of the open quotient map \(\pi\) is still open, as is checked on product neighborhoods, and hence is a quotient map. Also range and source on \(\mathcal G|_O\) are open relative to \(O\). For example
\(r(N\cap\mathcal G|_O)=r(N)\cap O\) for open \(N\subseteq\mathcal G\), since \(O\) is invariant.

Let \(A\subseteq Y\) be open and \(y\in b(A)\). Choose \(z\in J\) and an arrow \(\gamma:z\to y\). The unique point \(b^{-1}(z)\) is carried to \(b^{-1}(y)\in A\). Continuity of the action supplies neighborhoods \(N\) of \(\gamma\) and \(W\) of \(b^{-1}(z)\) such that every composable pair in \(N\times W\) acts into \(A\). Continuity of \(b^{-1}\) on \(J\) supplies an open neighborhood \(J'\subseteq J\) of \(z\) with \(b^{-1}(J')\subseteq W\). Now
\[
 r\big(N\cap s^{-1}(J')\big)
       \quad\hbox{is an open neighborhood of }y\hbox{ in }O,
       \quad\hbox{contained in }b(A).
 \tag{13B.6}
\]
Every arrow used here acts on the unique point over its source. Thus \(b\) is open everywhere. Since \(\pi\) is open, the original orbit map \(b\pi\) is open. This proves \(4\Rightarrow5\).

If condition 5 holds, \(b\) is a homeomorphism, so the orbit is locally compact in its subspace topology. A locally compact subspace \(O\) of a Hausdorff space is locally closed: at any point choose an ambient open \(W\) with \(O\cap W\) contained in a compact neighborhood \(C\subseteq O\). As \(C\) is closed in \(X\),
\(W\cap\overline O\subseteq C\subseteq O\). These neighborhoods show that \(O\) is open in \(\overline O\). This proves \(5\Rightarrow3\). Conversely a locally closed subset of a metrizable space is a \(G_\delta\), so \(3\Rightarrow4\).

Condition 3 also implies condition 1. If two distinct orbits had the same closure \(C\), each would be a nonempty open dense subset of \(C\). They would intersect, contradicting their distinctness. Formula (13B.1) says exactly that distinct point closures distinguish points in \(Q\). We have now proved the equivalence of conditions 1, 3, 4 and 5.

#### Finding a Hausdorff part of the quotient

Assume condition 5. We show that the quotient has a nonempty open Hausdorff part. Choose a relatively compact open arrow neighborhood \(V\) of some unit, put \(N=\overline V\), and choose a nonempty relatively compact open \(P_0\subseteq X\) with
\(e(P_0)\subseteq V\). Thus \(N\) is compact and its interior contains every unit over \(P_0\). We claim there is a nonempty open \(P\subseteq P_0\) such that
\[
 (r,s)(\mathcal G)\cap(P\times P)
                   =(r,s)(N)\cap(P\times P).
 \tag{13B.7}
\]
In words, all related pairs in this neighborhood can be joined by arrows in one compact set.

Suppose no such \(P\) exists. Use a compatible metric on \(X\). Inductively choose nonempty open sets \(P_n\) with compact closures, \(\overline{P_{n+1}}\subseteq P_n\), and diameters tending to zero. Here is the additional property we arrange. Since (13B.7) fails on \(P_n\), choose related \(x_n,y_n\in P_n\) with \((y_n,x_n)\notin(r,s)(N)\), and an arrow \(\sigma_n:x_n\to y_n\). The compact image \((r,s)(N)\) is closed in \(X\times X\). We can therefore choose a compact neighborhood \(M_n\subseteq P_n\) of \(x_n\) and an open neighborhood \(T_n\subseteq P_n\) of \(y_n\) such that
\[
 (T_n\times M_n)\cap(r,s)(N)=\varnothing.
 \tag{13B.8}
\]
Choose an open arrow neighborhood \(A_n\) of \(\sigma_n\) with
\(s(A_n)\subseteq\operatorname{int}M_n\) and \(r(A_n)\subseteq T_n\). Since source is open, \(s(A_n)\) is an open neighborhood of \(x_n\). Choose \(P_{n+1}\) with compact closure inside
\(P_n\cap\operatorname{int}M_n\cap s(A_n)\), and diameter less than \(1/(n+1)\). This completes the induction.

The nested compact closures have a unique common point \(x_\infty\); it belongs to every \(P_n\). Since \(x_\infty\in s(A_n)\), choose \(\tau_n\in A_n\) with source \(x_\infty\). Its range \(z_n\) lies in \(T_n\subseteq P_n\), hence \(z_n\to x_\infty\) in the same orbit. But (13B.8) and \(x_\infty\in M_n\) say that no arrow in \(N\) joins \(x_\infty\) to \(z_n\). This contradicts condition 5: the image of
\((\operatorname{int}N)\cap\mathcal G_{x_\infty}\) is a relative orbit neighborhood of \(x_\infty\), since that open set contains its unit. Eventually \(z_n\) must belong to that image. The claim follows.

The relation in (13B.7) is closed in \(P\times P\), and \(q|_P:P\to q(P)\) is an open quotient. Its quotient is Hausdorff: for an unrelated pair choose product neighborhoods avoiding the closed relation. Their images under the open quotient map are disjoint neighborhoods of the two classes. Thus \(q(P)\) is a nonempty open Hausdorff subspace of \(Q\).

To obtain condition 2 for every nonempty closed \(F\subseteq Q\), apply the same argument to the invariant closed unit set \(Y=q^{-1}(F)\). Its reduction is still second countable locally compact Hausdorff and has open range and source relative to \(Y\); its source fibres and orbit topologies are the original ones. The restricted quotient \(Y\to F\) is open: the image of \(Y\cap W\) is \(F\cap q(W)\) for open \(W\subseteq X\). The preceding construction gives the required relatively open Hausdorff part of \(F\). This proves \(5\Rightarrow2\).

Finally condition 2 implies condition 1. If two distinct points had the same closure \(C\), each would belong to every nonempty relatively open subset of \(C\). A nonempty relatively open Hausdorff part of \(C\) would contain both points and would have to separate them. Its separating neighborhoods are also relatively open in \(C\), which is impossible. All five conditions are equivalent. ∎

For an action of \(\mathcal G\) on a second countable locally compact Hausdorff space \(Z\), apply the theorem to the transformation groupoid \(\mathcal G\ltimes Z\). Its source map is the pullback of the open map \(s\), hence open; inversion gives openness of range. The arrow space is a closed fibre product in \(\mathcal G\times Z\), so is second countable locally compact Hausdorff. Its orbit map at \(z\) is precisely \(\gamma\mapsto\gamma z\). This proves the action version, with the second-countability hypothesis on \(Z\) explicit.

The nested-neighborhood argument is the groupoid counterpart of Effros's argument in the group case; compare [Williams 2007]. Open source provides arrows from the limiting unit, and open range propagates the first Baire neighborhood. Neither step assumes an étale groupoid or a continuous local choice of an arrow.

For any subset \(N\subseteq X\), its **reduction** is
\[
 \mathcal G|_N=r^{-1}(N)\cap s^{-1}(N)\rightrightarrows N.
 \tag{13.21}
\]

**Proposition 13.5.** The reduction is a topological groupoid in its induced topology. If \(N\) is open or closed, it retains local compactness in the Hausdorff setting, and local Hausdorff charts in the locally Hausdorff setting. Meeting every orbit makes it full.

**Proof.** The units at both endpoints of every retained arrow belong to \(N\), so inverses and composable products stay in the reduction. Its composable-pair topology is the subspace topology inherited from \(\mathcal G^{(2)}\). Restrictions of the original continuous structure maps therefore give a topological groupoid. For open \(N\) the arrow space is open; for closed \(N\) it is closed. Open and closed subspaces of a locally compact Hausdorff space are locally compact Hausdorff; apply the same assertion in a Hausdorff chart for the locally Hausdorff case. Fullness means exactly that each original orbit meets \(N\); then its intersections with \(N\) are precisely the reduction orbits. ∎

Neither fullness nor closedness by itself supplies a Haar system by restriction. In the pair groupoid of \(\mathbb R\), \(N=\{0\}\) meets the single orbit, but restricting the Lebesgue range measure to the sole arrow \((0,0)\) gives zero measure. The reduced one-point groupoid instead has a nonzero Dirac Haar measure.

A full closed reduction can even fail to have any Haar system. Let \(\mathbb R\) translate horizontally on \(\mathbb R^2\), and take
\[
 N=\{(0,y):y\geq0\}\ \cup\ \{(1,y):y\leq0\}.
 \tag{13.22}
\]
It is closed and meets every horizontal orbit. In the reduction, the arrow from \((0,0)\) to \((1,0)\) is isolated: restrict its target to the second half-line, its source to the first, and its translation coordinate to \((1/2,3/2)\). The common height must then be zero and the translation must be one. The range of this open singleton is \(\{(1,0)\}\), which is not open in \(N\). Theorem 13.4 forbids a Haar system. Transversal reductions used for foliations require their own local transversality and open-anchor arguments; Proposition 13.5 alone does not prove equivalence or a measure construction.

## Open range and second countability

Openness of range is necessary, and in general it is not sufficient without further hypotheses. To see this directly, let \(X\) be the one-point compactification of an uncountable discrete set \(D\). The pair groupoid \(X\times X\) has open range and source projections. Any Haar system on it would, by left invariance, use one common full-support Radon measure \(\mu\) on its second coordinate. This measure would be finite on compact \(X\), while \(\mu(\{d\})>0\) for every \(d\in D\). For each positive integer \(n\), only finitely many such masses can be at least \(1/n\). Their union is countable, contradicting uncountability of \(D\). Thus no Haar system exists.

## Selecting measures on open fibres

We first establish the measure-selection result needed for transfer. A **full continuous \(p\)-system** for a map \(p:Y\to B\) is a family of positive Radon measures \(\beta^b\) supported on exactly \(p^{-1}(b)\), such that \(b\mapsto\beta^b(f)\) is continuous for every \(f\in C_c(Y)\).

**Lemma (open-fibre selection).** An open continuous surjection between second countable locally compact Hausdorff spaces admits a full continuous \(p\)-system.

**Proof.** We give the selection argument, including the convergence of the measures. Choose a complete compatible metric \(d\leq1\) on \(Y\). Such a metric is available here: countably many compactly supported separating functions give a compatible metric \(d_0\); a compact exhaustion and compactly supported cutoffs give a proper continuous function \(h:Y\to[0,\infty)\). The metric \(d_0(y,z)+|h(y)-h(z)|\) is complete, since a Cauchy sequence stays in one compact sublevel set of \(h\). Truncating it at one preserves completeness and topology.

For finitely supported probability measures define
\[
 W(\mu,\nu)=\inf_{\gamma}\int d(y,z)\,d\gamma(y,z),
 \tag{13A.10}
\]
where \(\gamma\) ranges over couplings with the specified marginals. A coupling is just a finite nonnegative matrix with those row and column sums. Gluing two such matrices through their common marginal proves the triangle inequality. Mixing couplings with common weights proves convexity of the distance. We use the same formula for limits of these probabilities.

Write \(F_b\) for the probabilities supported on the closed fibre \(p^{-1}(b)\). If a finite probability \(\mu=\sum a_j\delta_{y_j}\) belongs to \(F_b\), openness of \(p\) gives, for each \(\varepsilon>0\), a neighborhood \(V\) of \(b\) such that
\[
 \operatorname{dist}_W(\mu,F_c)<\varepsilon\quad(c\in V).
 \tag{13A.11}
\]
Indeed choose one point of \(p^{-1}(c)\) in each \(\varepsilon\)-ball about \(y_j\), and transport the mass \(a_j\) there. Finite probabilities are dense among probabilities on a fibre: put all but a small mass in a compact set, partition that compact set into finitely many small-diameter Borel pieces, and choose a point in each nonempty piece. The omitted mass costs at most its mass because \(d\leq1\).

Choose numbers \(\varepsilon_n=4^{-n}\varepsilon_0\). Using (13A.11), a locally finite partition of unity on \(B\) produces a continuous, pointwise finitely supported probability \(\sigma_0(b)\) with distance less than \(\varepsilon_0\) from \(F_b\). Here the measures being mixed are fixed finite probabilities at the centres of the covering neighborhoods. Continuity is in \(W\); changes in finitely many weights cost at most the sum of their absolute changes.

Suppose \(\sigma_n\) has already been constructed. At each \(b\), choose a finite \(\mu_b\in F_b\) with \(W(\mu_b,\sigma_n(b))<\varepsilon_n\). Continuity of \(\sigma_n\) and (13A.11) give a neighborhood on which
\[
 W(\mu_b,\sigma_n(c))<2\varepsilon_n,
 \qquad \operatorname{dist}_W(\mu_b,F_c)<\varepsilon_{n+1}.
 \tag{13A.12}
\]
Mix these \(\mu_b\)'s with a locally finite partition of unity. Convexity gives a continuous finite probability \(\sigma_{n+1}\) satisfying
\[
 W(\sigma_{n+1}(c),\sigma_n(c))<2\varepsilon_n,
 \qquad \operatorname{dist}_W(\sigma_{n+1}(c),F_c)<\varepsilon_{n+1}.
 \tag{13A.13}
\]

The summable distances have an actual probability limit. At a fixed \(c\), choose optimal successive finite couplings; a minimum exists on the compact polytope of coupling matrices, and their expected distances are less than \(2\varepsilon_n\). Realize them as a chain of random variables using their finite conditional probabilities and independent uniform variables on \([0,1]\). The expected sum of successive distances is finite. Thus almost every chain is Cauchy and has a limit in the complete space \(Y\). Its distribution \(\mu^c\) is a Radon probability, and the coupling with each stage shows convergence in \(W\), with the uniform bound \(\sum_{k\geq n}2\varepsilon_k\). This bound also shows that \(c\mapsto\mu^c\) is continuous in \(W\).

The function \(d(y,p^{-1}(c))\) is bounded and 1-Lipschitz. Its integral against \(\sigma_n(c)\) is at most \(\varepsilon_n\), by the second inequality of (13A.13). Taking the limit proves that \(\mu^c\) is supported on the fibre. A continuous compactly supported function on \(Y\) is uniformly continuous for \(d\): a sequence contradicting uniform continuity would have one point tending into its compact support and the other at distance tending to zero. It can therefore be approximated uniformly by bounded Lipschitz functions, using infima of \(f(z)+L d(y,z)\) for its real and imaginary parts. The coupling estimate for Lipschitz functions proves continuity of \(c\mapsto\mu^c(f)\).

We still need full support; one selection alone need not have it. Take a countable base of precompact open subsets \(U_i\subset Y\). For \(y\in U_i\), choose \(r>0\) with the \(d\)-ball of radius \(r\) about \(y\) contained in \(U_i\). On a neighborhood \(V\) of \(p(y)\), (13A.11) permits us to start the same construction with \(\sigma_0(c)=\delta_y\) and \(\varepsilon_0<r/16\). Its limit stays within \(\sum_n2\varepsilon_n<r/2\) of \(\delta_y\), so \(\mu^c(U_i)>1/2\) for every \(c\in V\).

These neighborhoods cover \(p(U_i)\). Second countability and compactly supported base cutoffs give countably many functions \(0\leq\theta_j\leq1\), each with closed support inside one such \(V_j\), whose positivity sets cover each \(p(U_i)\). Include the corresponding local probability selections \(\mu_j^c\), and enumerate all these choices in one sequence. Set
\[
 \beta^c=\sum_{j\geq1}2^{-j}\theta_j(c)\mu_j^c,
 \tag{13A.14}
\]
interpreting a term as zero outside \(V_j\). Every term is continuous on test functions, including across the boundary of \(V_j\); the tail is bounded by \(\|f\|_\infty\sum_{j>N}2^{-j}\). Hence the test integrals are continuous. These are finite Radon measures supported on their fibres. Whenever the fibre meets \(U_i\), one positive term gives it positive mass in \(U_i\). The base then proves full support. ∎

This supplies the result credited to Blanchard in [Williams 2016]. Second countability enters both the partitions and the countable full-support mixture.

## Averaging and Haar transfer

A \((G,H)\)-**equivalence** is a locally compact Hausdorff space \(Z\) with commuting free proper left \(G\)- and right \(H\)-actions. Its open surjective anchors are \(p:Z\to G^{(0)}\) and \(q:Z\to H^{(0)}\), and the actions identify \(Z/H\) with \(G^{(0)}\) and \(G\backslash Z\) with \(H^{(0)}\). Equivalently, the action maps are homeomorphisms onto the corresponding equal-anchor relations. For example, for \(p(z)=p(w)\), there is a unique arrow \(h=[z,w]_H\) with \(zh=w\), and this division map is continuous. These are precisely the equivalence data used in Lesson 15.

**Theorem (Haar transfer).** Let \(G,H\) be second countable locally compact Hausdorff groupoids, and let \(Z\) be an equivalence between them. If \(G\) has a Haar system, then so does \(H\).

**Proof.** First \(Z\) is itself second countable; this does not have to be added as an assumption. Choose countably many precompact open subsets \(U_j\subset Z\) whose \(q\)-images cover \(H^{(0)}\), using openness of \(q\) and second countability of that unit space. Each point of \(Z\) lies in \(G\cdot\overline{U_j}\) for some \(j\). A compact exhaustion of \(G\), together with these compact sets and the closed composability relation, expresses \(Z\) as a countable union of compact continuous images. Thus \(Z\) is \(\sigma\)-compact.

The equal-\(q\) relation in \(Z\times Z\) is a \(G_\delta\), since the diagonal of the metrizable space \(H^{(0)}\) is a \(G_\delta\). Its continuous division map to \(G\), sending \((z,w)\) to the unique \(g\) with \(z=gw\), has the diagonal of \(Z\) as the inverse image of \(G^{(0)}\). The unit space is closed in the metrizable arrow space \(G\), hence is a \(G_\delta\). Consequently the diagonal of \(Z\) is a \(G_\delta\) in \(Z\times Z\).

Every compact Hausdorff space \(C\) with a \(G_\delta\) diagonal has a countable base. To check this directly, take decreasing open neighborhoods \(O_n\) of the diagonal with decreasing closed neighborhoods inside them and intersection equal to the diagonal. Compactness gives finite open covers \(\mathcal U_n\) with \(U\times U\subset O_n\) for every member. For \(x\in O\subset C\) open, some star of \(x\) in these covers is contained in \(O\). Otherwise points outside \(O\) paired with \(x\) in successively smaller \(O_n\)'s have a cluster point outside \(O\) on the diagonal, a contradiction. The countably many cover members therefore form a base. Apply this to compact subsets of \(Z\). Local compactness and \(\sigma\)-compactness give a countable cover of \(Z\) by open sets with compact closures, each having a countable base. Their bases together prove the assertion.

Now apply the preceding lemma to \(p\), obtaining a full system \(\beta^u\). We first construct a nonnegative continuous function \(b\) on \(Z\), positive somewhere on each \(G\)-orbit, with
\[
 \operatorname{supp}b\cap q^{-1}(K)\text{ compact whenever }K\subset H^{(0)}
 \text{ is compact}.
 \tag{13A.15}
\]
Choose a locally finite cover by precompact open sets \(V_j\subset H^{(0)}\) and a subordinate partition \(\rho_j\) with closed support inside \(V_j\). Openness and surjectivity of \(q\) permit finitely many compactly supported nonnegative bumps on \(Z\) whose positivity images cover \(\overline{V_j}\); let their sum be \(b_j\). Then \(b(z)=\sum_j\rho_j(q(z))b_j(z)\) is continuous and positive on every orbit. Over a compact \(K\), local finiteness restricts its support to finitely many compact \(\operatorname{supp}b_j\)'s. This proves (13A.15).

Average the selected measures using \(G\)'s Haar system:
\[
 \nu^u(f)=\int_{G^u}\int_{p^{-1}(s(g))}
                 f(gz)b(z)\,d\beta^{s(g)}(z)\,d\lambda^u(g).
 \tag{13A.16}
\]
We verify finiteness and continuity before claiming these are measures. Put \(K=\operatorname{supp}f\) and \(L=\operatorname{supp}b\cap q^{-1}(q(K))\). The latter is compact by (13A.15). The nonzero integrand has \(z\in L\) and \(gz\in K\). Properness of the action makes the set of such composable pairs compact. Thus \(F(g,z)=f(gz)b(z)\), initially on the closed composable-pair space, has compact support there. Extend it to a compactly supported continuous function on \(G\times Z\), by extending on a closed set and multiplying by a compact cutoff.

Integration of such a function against \(\beta^v\) is continuous in \((g,v)\): on a compact rectangle approximate uniformly by finite sums \(a(g)c(z)\); continuity of the selected system and a compact positive envelope bound the integral errors uniformly. Restricting to \(v=s(g)\) gives a function \(\Psi_f\in C_c(G)\). Its support is contained in the projection of the compact composable support above. Haar continuity now proves that (13A.16) is finite and continuous in \(u\). Positivity and local boundedness on compact test supports make it a Radon measure by the Riesz representation theorem.

Only points of \(p^{-1}(u)\) contribute. Conversely, if \(f\geq0\) and \(f(w)>0\), choose \(z\) in the same \(G\)-orbit with \(b(z)>0\), and \(g\) with \(gz=w\). Full support of \(\beta^{s(g)}\) gives \(\Psi_f(g)>0\). Its continuity and full support of \(\lambda^{p(w)}\) give \(\nu^{p(w)}(f)>0\). Thus \(\nu\) is a full \(p\)-system. Left invariance of \(\lambda\), with the substitution \(g\mapsto g_0g\), proves
\[
 (g_0)_*\nu^{s(g_0)}=\nu^{r(g_0)}.
 \tag{13A.17}
\]

For \(v\in H^{(0)}\), choose \(z\in q^{-1}(v)\) and define
\[
 \kappa^v(a)=\int_{p^{-1}(p(z))}a([z,w]_H)\,d\nu^{p(z)}(w),
 \qquad a\in C_c(H).
 \tag{13A.18}
\]
The map \(w\mapsto[z,w]_H\) is a homeomorphism onto \(H^v\), so this is a full-support Radon measure on that range fibre. If another choice is \(z'=gz\), its equal-anchor fibre is obtained by \(w'=gw\). Equation (13A.17) and commutation of the actions give \([gz,gw]_H=[z,w]_H\). Hence (13A.18) is independent of the choice.

Its test integral is continuous as a function of \(z\). Locally restrict \(z\) to a compact neighborhood \(K_Z\). A contributing \(w\) has the form \(zh\) with \(h\in\operatorname{supp}a\); these \(w\)'s lie in the compact image of the closed composable subset of \(K_Z\times\operatorname{supp}a\). A local compact cutoff, extension from the closed equal-anchor relation, and the same finite-sum integration argument prove continuity. This function is constant on the fibres of the open quotient \(q\), so descends to a continuous function of \(v\).

Finally, for \(h_0\in H\) and \(q(z)=r(h_0)\), use \(zh_0\) to compute the measure at \(s(h_0)\). The identity
\[
 [zh_0,w]_H=h_0^{-1}[z,w]_H
 \tag{13A.19}
\]
shows directly that \(\kappa^{s(h_0)}(a\circ L_{h_0})=\kappa^{r(h_0)}(a)\). This is left invariance. Thus \(\kappa\) is the required Haar system. ∎

The transfer theorem and averaging method are due to [Williams 2016]. The proof above includes the open-fibre selection and the passage from an equivariant system to the other groupoid's measures. It imposes neither étaleness nor a choice of transversal.

## A symbolic groupoid

Finally fix \(n\geq2\), let \(Y=\{1,\ldots,n\}^{\mathbb N}\) with its compact product topology, and let \(\sigma\) remove the first letter. The Cuntz groupoid is
\[
 \begin{gathered}
 \mathcal G_n=\{(x,k,y):k=p-q,\ p,q\geq0,\
                         \sigma^p x=\sigma^q y\},\\
 r(x,k,y)=x,\quad s(x,k,y)=y,\quad
 (x,k,y)(y,l,z)=(x,k+l,z).
 \end{gathered}
 \tag{13.23}
\]
Its inverse is \((y,-k,x)\). For finite words \(a,b\), including the empty word, the sets
\[
 Z(a,b)=\{(az,|a|-|b|,bz):z\in Y\}
 \tag{13.24}
\]
are compact open bisections and define its topology. They cover the arrow space by the defining shift equality. For intersections at the same lag, matching longer prefixes either gives a smaller set of this form or an empty intersection; they therefore form a basis. Range and source identify each with the two prefix cylinders. Their prefix product rules make inversion and multiplication continuous. Distinct arrows with distinct lag are separated by the lag; with equal lag they can be separated by a differing coordinate in their source or range cylinders. Thus the groupoid is Hausdorff, locally compact and étale, and Proposition 13.2 supplies its Haar system.

**Theorem (the Cuntz groupoid algebra).** With the counting Haar system,
\[
C^*(\mathcal G_n)\cong\mathcal O_n.
\tag{13A.7}
\]
Here \(\mathcal O_n\) is the universal unital C*-algebra generated by isometries \(s_1,\ldots,s_n\) with orthogonal ranges summing to the identity. We use the full completion constructed in Lesson 14.

**Proof.** Let \(S_i=1_{Z(i,\varnothing)}\). Counting convolution and inversion of bisections give
\[
S_i^*S_j=\delta_{ij}1_Y,\qquad
\sum_{i=1}^n S_iS_i^*=1_Y,
\qquad S_aS_b^*=1_{Z(a,b)}.
\tag{13A.8}
\]
The first identities follow by cancelling equal first letters; the range cylinders partition \(Y\). The empty word gives \(S_\varnothing=1_Y\), which is the convolution identity because \(Y\) is the compact unit space. Thus the universal property gives a homomorphism \(\pi:\mathcal O_n\to C^*(\mathcal G_n)\). The identity is nonzero: any regular representation from Lesson 14 acts by the identity on its nonzero fibre Hilbert space.

This homomorphism is onto. A compact-support partition of unity decomposes any test function into finitely many functions supported inside the bisections \(Z(a,b)\). On a bisection, prefix-cylinder step functions approximate continuous functions uniformly, because finite-prefix cylinders form a clopen basis of the compact word space. Each step function is a finite linear combination of characteristic functions \(1_{Z(ac,bc)}\). A function on one bisection has I-norm at most its supremum norm, since a bisection meets each range and source fibre at most once. Summing over the finite decomposition therefore gives approximation in I-norm, hence in the full C*-norm. Equation (13A.8) places every approximant in the image of \(\pi\), proving surjectivity.

To prove injectivity, use the circle actions. The universal action on \(\mathcal O_n\) is \(\gamma_z(s_i)=zs_i\). On the groupoid algebra multiply a kernel at \((x,k,y)\) by \(z^k\). Additivity of the integer lag makes this a star automorphism of the convolution algebra. It preserves the I-norm, and precomposition permutes the representations defining the full norm; thus it extends isometrically to the full completion. It is norm continuous in \(z\) on finite bisection sums, and then on the completion by density. The map \(\pi\) intertwines these two circle actions.

The fixed algebra of \(\gamma\) is the closure of the increasing finite matrix algebras
\[
F_k=\operatorname{span}\{s_as_b^*:|a|=|b|=k\}
       \cong M_{n^k}(\mathbb C).
\tag{13A.9}
\]
Indeed the defining relations reduce every star polynomial to a sum of \(s_as_b^*\). Circle averaging keeps exactly the terms of equal length. Also
\(s_as_b^*=\sum_i s_{ai}s_{bi}^*\), so these spans increase. Their matrix-unit relations follow from \(s_a^*s_b=\delta_{ab}1\) for words of the same length. No coefficient relation can vanish: multiplying a proposed relation on the left by \(s_c^*\) and on the right by \(s_d\) isolates its coefficient times the nonzero identity. The same argument for the \(S_a\)'s proves that \(\pi\) is injective, hence isometric, on every \(F_k\). It is therefore injective on their closed union.

Circle averaging \(E(a)=\int_{\mathbb T}\gamma_z(a)\,dz\) is faithful. If \(E(a^*a)=0\), then for every state \(\omega\), the continuous nonnegative function \(z\mapsto\omega(\gamma_z(a^*a))\) has zero Haar integral. Haar full support makes it identically zero, so at \(z=1\) every state vanishes on \(a^*a\); hence \(a=0\). If \(\pi(a)=0\), equivariance gives \(\pi(E(a^*a))=0\). The fixed-algebra injectivity gives \(E(a^*a)=0\), and faithfulness gives \(a=0\). This proves (13A.7). ∎

Sims, *Hausdorff étale groupoids and their C*-algebras*, Examples 2.4.7 and 3.2.7, describes this one-vertex graph model. The bisection generators, density argument and gauge injectivity required for the identification have been proved here.

## Exercises with solutions

**Exercise 1 (basic).** For a continuous action \(H\curvearrowright X\), verify the transformation-groupoid operations, determine the orbit and isotropy at \(x\), and specialize to a homeomorphism \(T\) acting by \(\mathbb Z\).

**Solution.** An arrow \((x,g)\) goes from \(g^{-1}x\) to \(x\). The endpoint condition for its product with \((y,h)\) is \(y=g^{-1}x\). The product \((x,gh)\) has source \(h^{-1}g^{-1}x\), the source of the second arrow. Inversion in (13.5) gives both products equal to the appropriate units. Three composable arrows multiply to \((x,ghk)\) in either order, proving associativity. The action and group operations give continuity of inverse, and the \((x,g,h)\) parametrization of composable pairs gives continuity of multiplication. Local compactness and the Hausdorff property follow from the product topology.

An arrow with source \(x\) has the form \((gx,g)\), so the orbit is \(Hx\). Isotropy consists of \((x,g)\) with \(gx=x\), and its group law is the law of \(H_x\). For \(T\), these become \(T^{\mathbb Z}x\) and \(\{m:T^m x=x\}\). If the least positive period is \(q\), division by \(q\) shows that every return time is a multiple of \(q\); hence the isotropy is \(q\mathbb Z\). With no positive return time it is zero.

**Exercise 2 (basic).** Prove that range and source are open in an étale groupoid. Show also that its unit space is open.

**Solution.** Cover an open set \(V\subseteq\mathcal G\) by range-chart pieces \(V\cap U\). The image of each is open in the chart's open range image, hence open in \(X\). Their union is \(r(V)\). Since \(s=r\circ\mathrm{inv}\), inversion, a homeomorphism, gives the same assertion for source.

For openness of units, choose a source chart \(U\) at \(e(x)\) and set \(O=s(U)\cap e^{-1}(U)\). It is an open neighborhood of \(x\). The unique arrow in \(U\) with source \(y\in O\) is \(e(y)\), because this unit also belongs to \(U\). Thus \(e(O)=(s|_U)^{-1}(O)\) is open in the arrow space. Such neighborhoods cover all the units. This proof permits the arrow space to be non-Hausdorff; only the local homeomorphism and continuous unit inclusion were used.

**Exercise 3 (intermediate).** Prove that a full-support continuous Haar system forces the range map to be open. Explain why allowing zero fibre measures destroys the conclusion.

**Solution.** Given \(\gamma\in U\) with \(U\) open, take a nonnegative compact bump supported inside \(U\) and positive at \(\gamma\). In the locally Hausdorff case take a Hausdorff-patch bump and its zero extension. Positivity persists on a relatively open neighborhood in \(\mathcal G^{r(\gamma)}\), and full support makes its measure positive. Hence \(\lambda(f)(r(\gamma))>0\). Haar continuity makes \(\{\lambda(f)>0\}\) an open neighborhood of \(r(\gamma)\). Every fibre with positive integral meets \(U\), so this neighborhood lies in \(r(U)\). Doing this at every \(\gamma\in U\) proves openness.

The family of zero measures is invariant and its integrals are continuous on every topological groupoid. In particular it can be placed on the reduction (13.22), whose range map is not open. The full-support condition is precisely what rules it out.

**Exercise 4 (advanced).** For the doubled-origin group bundle (13.17), determine the entire patch test-function space and its counting integrals. Compare it carefully with globally continuous compactly supported functions, and test pointwise multiplication.

**Solution.** The plus and minus charts cover the arrow space. For a compactly supported function on any Hausdorff open patch, a finite partition of unity inside that patch splits it into terms supported in the intersections with these two charts. Zero extending these terms shows that every test function is \(\phi_++\psi_-\) with \(\phi,\psi\in C_c(\mathbb R)\). It gives the triple \(F=\phi+\psi\), \(a=\phi(0)\), \(b=\psi(0)\), satisfying \(F(0)=a+b\). Conversely a compact bump with prescribed value \(a\) at zero supplies \(\phi\), and \(\psi=F-\phi\) supplies the rest. This proves (13.19), including surjectivity.

The counting integral is \(F(x)\) away from zero and \(a+b=F(0)\) at zero, so it is continuous. Global continuity of an arrow function, restricted to each of the two charts, forces \(a=b=F(0)\). Combining this with the patch constraint gives \(a=b=F(0)=0\). Thus the intersection of the two function spaces consists exactly of the compactly supported functions which vanish at both origins.

To see both failures outside their intersection, take a nonnegative compact bump \(\rho\) on the ordinary line with \(\rho(0)=1\). Its plus-chart extension has triple \((\rho,1,0)\), is a test function, and is not globally continuous. The globally continuous function with nonzero values \(\rho(x)\) and both origin values \(1\) has counting integral \(2\) at zero and limit \(1\); it is not a patch test function. Accordingly, saying only that the naive globally continuous space is “too small” would conceal that it also contains inadmissible functions.

Finally the pointwise product of the plus and minus extensions of \(\rho\) has triple \((\rho^2,0,0)\). It violates \(\rho^2(0)=0+0\). The patch span is a vector space of integration kernels, not an algebra under pointwise multiplication.

## Proofs and prerequisites

- The Mackey–Glimm–Ramsay equivalences are proved in the orbit-space section, including the open-orbit-map and almost-Hausdorff implications. The transformation-groupoid argument proves the action version for a second countable locally compact Hausdorff acted-on space. No Haar system or local bisections enter this proof.
- Group-bundle Haar existence and Haar transfer under equivalence are proved above, including full continuous measure selection and second countability of an equivalence space. The measure argument uses the ordinary Riesz representation and probability-measure extension theorems.
- The holonomy construction is the exact written programme prerequisite *The C*-algebra of a foliation*, Lemma 1.1, Lemma 2.1 and Theorem 2.2, for second countable foliated manifolds, including locally Hausdorff arrow spaces and Hausdorff holonomy covers. The Reeb transverse model and leaf geometry are proved in Lesson 16. Their original attribution to Connes is retained.
- The Cuntz-algebra identification is proved by the bisection generators and circle averaging above. Its full groupoid norm and regular representation use the owned construction in Lesson 14; Morita equivalence is the subject of Lesson 15.
- Haar measure on locally compact groups, compact-support partitions of unity on locally compact Hausdorff spaces, and smooth partitions of unity on second countable manifolds are the general prerequisites used in the explicit constructions.

## References

- Yuezhao Li, [*Groupoid C*-algebras*](https://ncg-leiden.github.io/groupoid2022/groupoid_notes.pdf), Leiden seminar notes, revised 7 February 2024, §§1–3 and §9.
- Alain Connes, [*A survey of foliations and operator algebras*](https://alainconnes.org/wp-content/uploads/foliationsfine.pdf), 1982, §6; locators here refer to the author's electronic edition.
- Alain Connes, [*Noncommutative Geometry*](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf), 1994, Chapter II, §§5 and 8.
- Dana P. Williams, [*Haar Systems on Equivalent Groupoids*](https://arxiv.org/pdf/1501.04077), *Proceedings of the American Mathematical Society, Series B* **3** (2016), 1–8, Theorem 2.1.
- Aidan Sims, [*Hausdorff étale groupoids and their C*-algebras*](https://aidansims.com/papers/Sims2017.pdf), 2017, Examples 2.4.7 and 3.2.7.

- *The C*-algebra of a foliation*, in *Foliations and their operator algebras*, Lemma 1.1, Lemma 2.1 and Theorem 2.2. This is a written programme proof; its source is available on GitHub.

- Arlan Ramsay, *The Mackey–Glimm dichotomy for foliations and other Polish groupoids*, *Journal of Functional Analysis* **94** (1990), 358–374, [original article](https://doi.org/10.1016/0022-1236(90)90018-G). Attribution for the groupoid dichotomy; the proof is supplied above.
- Dana P. Williams, *Crossed Products of C*-Algebras*, AMS, 2007, Theorem 6.2 and its proof, pp. 176–179, [book record](https://doi.org/10.1090/surv/134). The group case and Effros argument are credited; the groupoid proof uses open source and range maps as shown above.
