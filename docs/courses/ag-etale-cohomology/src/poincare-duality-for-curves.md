# Poincaré duality for curves

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Links and citations revised by Claude Opus 5.5 (Anthropic). Connecting-map and trace-normalization arguments by GPT-6 Astra (OpenAI), Ultra, October 2026. Self-checked by the contributing AIs. Original text released under CC0.*

The degree of a divisor supplies an orientation for a smooth algebraic curve. Poincaré duality says that this orientation pairs compactly supported cohomology with ordinary cohomology, including coefficients that have ramification at finitely many points. The local calculation at those points is essential. We give that calculation and then the full argument of M. Artin for constructible coefficients.

## 1. Conventions and the earlier results used

Throughout, \(k\) is algebraically closed, \(n\geq2\) is invertible in \(k\), and \(\Lambda=\mathbf Z/n\). The case \(n=1\) has zero coefficients and is immediate. A curve means a separated smooth scheme of finite type over \(k\), purely of dimension one. It has finitely many connected components. A constructible \(\Lambda\)-sheaf has finite module values on a finite constructible stratification. We write \(D^b_c(X,\Lambda)\) for complexes with constructible cohomology and only finitely many nonzero cohomology sheaves. All sheaves and derived operations are on the small étale site.

Put

\[
\Lambda(1)=\mu_n,\qquad K_X=\mu_n[2],\qquad
D_XF=R\mathcal Hom_\Lambda(F,K_X).
\tag{1.1}
\]

The symbol \(\mathcal Hom\) denotes internal sheaf Hom. Without the calligraphic symbol, \(R\operatorname{Hom}_\Lambda\) will mean the derived Hom of complexes of modules. A shift satisfies \(H^r(A[s])=H^{r+s}(A)\). For a local system \(L\), write \(L^\vee=\mathcal Hom_\Lambda(L,\Lambda)\), and \(L^\vee(1)=L^\vee\otimes_\Lambda\mu_n\). The sheaf \(\mu_n\) is an invertible rank-one \(\Lambda\)-sheaf. Choosing a primitive root identifies it with \(\Lambda\), but the formulas will keep the twist.

Our trace sends \(c_1^{(n)}(\mathcal O_C(x))\) to \(+1\) for a point on a connected smooth projective curve \(C\). The pairing is ordered with the compactly supported class first:

\[
R\Gamma_c(X,F)\otimes^L_\Lambda R\Gamma(X,D_XF)
\longrightarrow R\Gamma_c(X,K_X)\longrightarrow\Lambda.
\tag{1.2}
\]

Switching two classes of degrees \(r,s\) contributes \((-1)^{rs}\), together with the coefficient symmetry. In particular switching two degree-one classes changes the sign. This convention also fixes the curve trace used for the Lefschetz trace formula.

Here are the exact cohomological imports. Lesson 7 proves exact finite pushforward, finite base change and geometric-stalk comparison. Lesson 8, Theorem 6.1, proves procyclic cohomology, including its inflation maps. Lesson 10, Theorem 6.2 and Proposition 8.1, proves the Kummer/degree computation and the degree of finite pullback. Lesson 11 proves the constructible Serre property and exact extension by zero. Lesson 12, Sections 8 and 10, proves ordinary curve finiteness and the prime-to-characteristic bounds: degree at most two for a proper curve and at most one for an affine curve. Lesson 14, Sections 10–12, proves the projection formula, localization, and compact-support finiteness and the degree-two bound. Strictly henselian local schemes are acyclic for abelian étale sheaves, as proved in Lesson 16, Section 2.

We also use the geometric curve foundations stated in Lesson 12, Section 2: smooth projective completion, finite normalization, the classification of finite local systems by finite étale covers on a normal curve, and the Picard/Jacobian facts explicitly stated in Lesson 10, Picard input 6.1. None of these imports is Poincaré duality. The codimension-one cohomological calculation needed below will be proved here, before the general purity lesson.

## 2. The trace and its normalization

Let \(C\) be connected and smooth projective. Kummer and Lesson 10 give

\[
H^2(C,\mu_n)=\operatorname{Pic}(C)/n\operatorname{Pic}(C)
\xrightarrow[\deg]{\sim}\Lambda.
\tag{2.1}
\]

Recall why degree gives precisely this quotient. The degree-zero subgroup is divisible by \(n\), and there is a degree-one line bundle. If \(\deg L=na\), choose \(M\) of degree \(a\); then \(L\otimes M^{-n}\) has degree zero and is an \(n\)-th power. Thus \(L\) is an \(n\)-th power. The converse follows by taking degrees. The trace in (2.1) is therefore canonical, without choosing a root of unity or a splitting of the degree sequence.

For a connected open \(j:X\hookrightarrow C\), let \(i:Z=C-X\hookrightarrow C\). The finite reduced boundary has no positive cohomology. From

\[
0\longrightarrow j_!\mu_n\longrightarrow\mu_n
\longrightarrow i_*\mu_n\longrightarrow0
\]

we obtain

\[
H^2_c(X,\mu_n)=H^2(C,j_!\mu_n)
\xrightarrow{\sim}H^2(C,\mu_n)
\xrightarrow[\operatorname{Tr}_X]{\sim}\Lambda.
\tag{2.2}
\]

The completion is unique up to the unique isomorphism extending the identity on the function field: a birational map between smooth projective curves extends at every valuation ring, and its inverse does too. Thus (2.2) is independent of the completion. If \(V\subset X\) is a nonempty connected open, the map \(H^2_c(V,\mu_n)\to H^2_c(X,\mu_n)\) preserves trace, since both maps to the same \(H^2(C,\mu_n)\). For a disconnected curve, trace is the sum of (2.2) over its connected components.

The compact degree bound gives \(R\Gamma_c(X,K_X)\in D^{\leq0}(\Lambda)\). Its canonical map to \(H^0=H^2_c(X,\mu_n)\), followed by this trace, is the derived trace in (1.2). Cup product and evaluation construct the first map in (1.2): use the projection formula for compact support and the sheaf evaluation \(F\otimes^L D_XF\to K_X\).

**Proposition 2.1 (finite trace).** If \(f:X\to Y\) is finite and generically étale between smooth curves, there is a trace

\[
\tau_f:f_*\mu_{n,X}\longrightarrow\mu_{n,Y},
\qquad
\operatorname{Tr}_Y\circ H^2_c(\tau_f)=\operatorname{Tr}_X.
\tag{2.3}
\]

On the étale locus the trace is summation over the sheets. At a closed geometric point \(y\), its formula is

\[
(a_x)_{x\mid y}\longmapsto\sum_{x\mid y}e_xa_x
\tag{2.4}
\]

in additive root-of-unity notation, where \(e_x\) is the ramification index. In particular \(\tau_f f^{-1}\) is multiplication by the degree on each connected target component.

**Proof.** The finite morphism is flat: over a target discrete valuation ring its finite algebra is torsion free, hence free. Let \(V\subset Y\) be the étale locus. Normality gives \(f_*\Lambda_X=j_*L\), where \(L\) is the permutation local system over \(V\). Indeed, on an étale target chart its finite inverse image is normal; each connected component is integral and meets the inverse image of \(V\). A locally constant function on such a component is determined by its value on that dense open. Generic summation therefore extends by \(j_*\) to a map \(f_*\Lambda\to\Lambda\). Tensoring by the locally constant \(\mu_n\) gives \(\tau_f\).

Over a strictly henselian target trait, the sheets specializing to a given \(x\) form one inertia orbit of size \(e_x\). The residue field is separably closed, so there is no residue-degree factor. An invariant locally constant value \(a_x\) is repeated \(e_x\) times in the generic sum, proving (2.4). The same formula follows from the norm on units: the determinant norm of a scalar root of unity on that branch is its \(e_x\)-th power. Norm is compatible with \(n\)-th powers, hence with Kummer.

For projective curves norm on line bundles sends a divisor \(\sum m_x[x]\) to \(\sum m_x[f(x)]\), since all residue fields are \(k\). To check it, trivialize a line bundle on the generic point and take determinant norms of its local rational transition functions; their valuations are the sums of the valuations on the branches. Consequently norm preserves the degree of divisors and induces (2.3) under Kummer and (2.1).

A finite map of open curves extends to their projective completions. The inverse image of \(Y\) in the source completion is exactly \(X\): any valuation point above \(Y\) must lie in \(X\), by the valuative criterion for the proper map \(X\to Y\). Thus the open-completion square is cartesian. Finite base change and exact extension by zero carry the projective norm compatibility to (2.3) for compact support. This proves every assertion. \(\square\)

For finite étale \(f\), all \(e_x=1\); trace is the usual sum and transfer. Pullback in degree two is multiplication by the degree, whereas the norm trace in (2.3) preserves the degree of a point divisor. These are different maps with different directions.

## 3. Finite coefficient duality

The coefficient ring need not be a field. The following elementary fact is the reason the argument still works.

**Lemma 3.1.** The module \(\Lambda\) is injective over itself. For a finite \(\Lambda\)-module \(M\), the functor

\[
M^\vee=\operatorname{Hom}_\Lambda(M,\Lambda)
\]

is exact, separates points, preserves cardinality, and the evaluation map \(M\to M^{\vee\vee}\) is an isomorphism.

**Proof.** Every ideal is \(d\Lambda\) for some divisor \(d\mid n\). A map from this ideal to \(\Lambda\) is determined by \(a=h(d)\), which satisfies \((n/d)a=0\). This says precisely that \(a=db\) for some \(b\in\Lambda\). Multiplication by \(b\) extends \(h\) to all of \(\Lambda\). Baer's criterion proves injectivity, and hence exactness of Hom into \(\Lambda\).

A finite module is a finite direct sum of cyclic groups of orders dividing \(n\). For the cyclic group of order \(d\), its dual is the subgroup \((n/d)\Lambda\), also of order \(d\). A generator pairs with \(n/d\), so the dual separates that generator and all its nonzero multiples. The same conclusion holds on each summand. Thus evaluation is injective, and equal cardinalities make it an isomorphism. \(\square\)

For a bounded complex of finite modules \(A\), derived duality is computed by ordinary Hom into \(\Lambda\), and

\[
H^r(R\operatorname{Hom}_\Lambda(A,\Lambda))
=H^{-r}(A)^\vee.
\tag{3.1}
\]

This follows by applying the exact dual functor to cycles, boundaries and their quotient, with the usual Hom-complex differential. Evaluation uses the graded symmetry and gives the canonical complex bidual map; (3.1) and Lemma 3.1 show it is an isomorphism.

These assertions do not say that \(A\) has a finite resolution by finitely generated projective modules. For example \(\mathbf Z/\ell\) over \(\mathbf Z/\ell^2\) has an infinite resolution with successive maps multiplication by \(\ell\). A skyscraper with that value is allowed in our theorem. A perfect pairing below means that the two finite groups are each other's \(\Lambda\)-dual, and that the specified derived duality map is an isomorphism.

## 4. Inertia and the valuation calculation

Let \(S\) be the strict henselization of a smooth curve at a closed geometric point, \(i:s\hookrightarrow S\) its closed point, and \(j:\eta\hookrightarrow S\) its generic point. The ring of \(S\) is a strictly henselian discrete valuation ring. Write \(I=\operatorname{Gal}(\bar\eta/\eta)\). A finite locally constant sheaf on \(\eta\) is a finite continuous \(I\)-module \(M\).

We use the ramification description

\[
1\longrightarrow P\longrightarrow I\longrightarrow
T=\widehat{\mathbf Z}^{(p')}(1)\longrightarrow1,
\tag{4.1}
\]

where \(p\) is the residue characteristic exponent, \(P\) is pro-\(p\), and \(P=1\) in characteristic zero. This is the geometric ramification fact for a strict smooth trait. Its tame description comes from adjoining all prime-to-\(p\) roots of a uniformizer. Units have such roots by Hensel's lemma and the separably closed residue field. For a finite Galois extension, inertia acts on a uniformizer modulo its square through a finite subgroup of the residue multiplicative group; that quotient is cyclic of order prime to \(p\). The kernel is the wild group: its successive ramification quotients embed in the residue additive group and are \(p\)-groups. Passing to the inverse limit gives (4.1). The roots of the uniformizer identify its quotient canonically with the indicated Tate-twisted group. This input is a statement about valuation extensions, not a cohomological purity or duality theorem.

**Lemma 4.1.** For a finite \(\Lambda[I]\)-module \(M\),

\[
H^0(I,M)=M^I,\qquad
H^1(I,M)=(M^P)_T(-1),\qquad H^q(I,M)=0\quad(q>1).
\tag{4.2}
\]

There is a canonical evaluation isomorphism

\[
H^1(I,M^\vee)\xrightarrow{\sim}(M^I)^\vee(-1).
\tag{4.3}
\]

**Proof.** Invariants for \(P\) are exact on these modules. A finite set of elements and their \(P\)-action factors through a finite \(p\)-group, whose order is a unit in \(\Lambda\); averaging lifts any invariant section of a quotient. The same averaging contraction of the finite-group cochain complex kills positive cohomology. Continuous cohomology is the filtered limit over finite quotients, so \(H^{>0}(P,M)=0\). Hochschild–Serre reduces to \(T\) acting on \(M^P\).

Choose a topological generator \(\gamma\) of \(T\) temporarily. The cyclic resolution and inflation computation of Lesson 8, Section 6, apply using only cyclic quotients of order prime to \(p\). If the action factors through order \(r\), replace \(r\) by \(ar\), with \(a\) divisible by the exponent of \(M\) and still prime to \(p\). The norm \(N_{ar}=aN_r\) then vanishes. Inflation is the identity on degree-one representatives and multiplication by \(a^{\lfloor q/2\rfloor}\) in degree \(q\geq2\), so every higher class dies after such a refinement. This proves degree one is the coinvariant group \(M^P/(\gamma-1)M^P\), and all higher degrees are zero. Replacing \(\gamma\) by a unit multiple changes the cocycle evaluation by that unit; recording the tame character makes the identification canonical with the factor \((-1)\). This proves (4.2).

Averaging also identifies \((M^\vee)^P\) with \((M^P)^\vee\). On \(N=M^P\), dualizing the two-term sequence defined by \(\gamma-1\), using exactness from Lemma 3.1, gives

\[
(N^\vee)_T\xrightarrow{\sim}(N^T)^\vee,
\qquad [\lambda]\longmapsto\lambda|_{N^T}.
\tag{4.4}
\]

Indeed the transpose of \(\gamma-1\) differs from \(\gamma^{-1}-1\) by an invertible factor, and its cokernel is the dual of the kernel. Combining this with (4.2) proves (4.3). \(\square\)

Notice the distinction: the dual of \(M^I\) is the **coinvariant** quotient of the dual module. Invariants of the dual cannot replace it. For a tame unipotent Jordan block of size two over \(\mathbf F_\ell\), the invariant line maps to zero in the coinvariant quotient. Such an example would invalidate a proof based on the map from invariants to coinvariants being an isomorphism.

**Lemma 4.2 (the point orientation).** There is a canonical identification

\[
Ri^!\Lambda=\Lambda(-1)[-2],\qquad
Ri^!\mu_n=\Lambda[-2].
\tag{4.5}
\]

These are the trace-normalized identifications: the boundary of the Kummer class of a uniformizer is \(-1\) in the second identification. Thus the positive point generator is the **negative** of that boundary.

**Proof.** Strict henselian acyclicity makes global sections on \(S\) its exact closed-stalk functor. The localization triangle is

\[
i_*Ri^!\Lambda\longrightarrow\Lambda
\longrightarrow Rj_*\Lambda\longrightarrow i_*Ri^!\Lambda[1].
\tag{4.6}
\]

It can be constructed by an injective resolution and the subcomplex of sections supported on \(s\); the quotient restricts to the generic open. Formula (4.2) for trivial coefficients says that the last direct image has stalk \(\Lambda\) in degree zero, \(\Lambda(-1)\) in degree one, and zero in higher degrees. The map on degree zero in (4.6) is the identity. Thus the first term has just \(\Lambda(-1)\) in degree two. A complex with one cohomology sheaf has its canonical identification with that sheaf in its degree, proving the first formula of (4.5).

Kummer identifies \(H^1(\eta,\mu_n)=K^\times/K^{\times n}\), where \(K\) is the fraction field. Every unit of the strict local ring is an \(n\)-th power by Hensel's lemma. Valuation therefore gives \(K^\times/K^{\times n}=\mathbf Z/n\), sending a uniformizer to \(+1\). Denote the localization boundary by \(\lambda\). Use **negative valuation** to identify its target with \(\Lambda\): the class \(\epsilon_s=-\lambda\kappa(t)\) corresponds to \(1\). Tensoring by the invertible local system \(\mu_n\) gives the two compatible identifications in (4.5). A different uniformizer differs by a unit, so gives the same \(\epsilon_s\). The following cochain calculation proves that this choice, rather than the opposite one, agrees with the degree trace. \(\square\)

**Lemma 4.3 (connecting maps and the global point class).** Connecting homomorphisms are formed by lifting a cocycle and differentiating its lift, with no additional sign. For a two-open cover \(C=U\cup V\), put \(W=U\cap V\) and use the Mayer–Vietoris quotient \(q(u,v)=v|_W-u|_W\). Let \(m\) be its connecting map. For a coefficient sequence \(0\to A\xrightarrow{i}B\to C'\to0\) with connecting map \(\delta\),

\[
\delta_C m_{C'}=-m_A\delta_W.
\tag{4.7}
\]

If \(V=C\setminus\{s\}\), let \(e:H^2_s(U,A)\to H^2(C,A)\) be excision followed by forgetting supports. Then \(e\lambda=-m_A\) on \(H^1(W,A)\). With the divisor and Picard conventions of Lesson 10, Section 5, these identities give

\[
e\lambda\kappa(t)=c_1^{(n)}\mathcal O_C(-s),\qquad
e\epsilon_s=c_1^{(n)}\mathcal O_C(s).
\tag{4.8}
\]

**Proof.** We spell out both signs. Compatible termwise split injective resolutions of the coefficient sequence give exact columns after taking sections. Injective sheaves are flasque, so their sections on \(C\), \(U\amalg V\), and \(W\) also form exact rows. Write \(r\) for restriction from \(C\) to \(U\amalg V\). For \(x\in Z^0(C'_W)\), lift \(x\) to \(b\in B_W^0\) and write \(db=i(a)\). Choose \(y\in C'^0_{U\amalg V}\) with \(qy=x\); then \(dy=rz\) for a cocycle \(z\in C'^1_C\). Lift \(y,z\) to \(\widetilde y,\widetilde z\) in the corresponding \(B\)-complexes. There are \(u\in A_W^0\), \(v\in A_{U\amalg V}^1\) with

\[
q\widetilde y-b=i(u),\qquad
d\widetilde y-r\widetilde z=i(v),\qquad qv=a+du.
\]

Choose \(w\in A_{U\amalg V}^0\) with \(qw=u\), and write \(d\widetilde z=i(\beta)\). Then \(v-dw\) lifts \(a\), but \(d(v-dw)=-r\beta\). Thus \(m_A\delta_W(x)=[-\beta]\), whereas \(\delta_Cm_{C'}(x)=[\beta]\), proving (4.7). Changes of lifts add coboundaries. This calculation applies to multiplicative abelian sheaves by writing their resolutions additively.

For localization, represent a class on \(W\) by a cocycle \(a\) in a flasque resolution, and lift it to \(\widetilde a\) on \(U\). Its differential is supported at \(s\), extends by zero to a global cocycle \(z\), and represents \(e\lambda(a)\). A lift of \(a\) under \(q\) is \((-\widetilde a,0)\), whose differential is \(-rz\). Hence \(m_A(a)=-[z]\), proving \(e\lambda=-m_A\).

Choose \(U\) so that the divisor of \(t\) on \(U\) is exactly \([s]\). The local rational lifts of \([s]\) in the valuation sequence are \(t\) on \(U\) and \(1\) on \(V\). For a coefficient boundary with local lifts \(b_U,b_V\), its class is \(m(b_U-b_V)\): subtracting a global resolution lift from the two local lifts and differentiating proves this identity directly. Consequently the divisor boundary is \(m_{\mathbf G_m}(t)\). Lesson 10, equation (5.4), identifies that boundary with \(\mathcal O_C(-s)\), not \(\mathcal O_C(s)\). The Kummer and Mayer–Vietoris square is therefore anticommutative:

\[
\begin{array}{ccc}
H^0(W,\mathbf G_m)&\xrightarrow{m_{\mathbf G_m}}&H^1(C,\mathbf G_m)\\
\kappa_W\downarrow&&\downarrow\kappa_C\\
H^1(W,\mu_n)&\xrightarrow{m_{\mu_n}}&H^2(C,\mu_n).
\end{array}
\]

Combining its sign with the localization sign gives

\[
e\lambda\kappa(t)=-m_{\mu_n}\kappa(t)
=\kappa_Cm_{\mathbf G_m}(t)
=c_1^{(n)}\mathcal O_C(-s).
\]

Negation gives the second equality of (4.8). On a projective curve its trace is \(+1\) by (2.1). For an open curve the same supported class maps through its projective completion, so (2.2) gives the identical compact trace. Each point is treated independently, proving compatibility for a finite set of points. \(\square\)

For example, with \(n=3\) on \(\mathbf P^1\), the raw class \(e\lambda\kappa(t)\) has trace \(2\), whereas \(e\epsilon_s\) has trace \(1\). Modulo two the two signs coincide; that case alone cannot distinguish the normalizations.

## 5. The local calculation for a ramified extension

For the moment write \(D_0=R\mathcal Hom_\Lambda(-,\Lambda)\) on a smooth curve. Let \(j:U\hookrightarrow X\) be dense and \(L\) finite locally constant on \(U\).

**Theorem 5.1.** There is a natural isomorphism

\[
D_0(j_*L)=j_*L^\vee.
\tag{5.1}
\]

In particular \(\mathcal Ext^q_\Lambda(j_*L,\Lambda)=0\) for \(q>0\).

**Proof.** On \(U\), a trivializing étale cover reduces to finite-module duality: Lemma 3.1 gives \(R\mathcal Hom(L,\Lambda)=L^\vee\). We check the remaining finitely many stalks on the strict local traits of Section 4. Fix one, with generic module \(M\), and put \(A=M^I\).

These stalk calculations use pointed étale neighbourhoods and their strict-local limit. Finite monodromy modules and the maps between them descend to such neighbourhoods; the geometric-stalk and cohomological-continuity formulas of Lesson 7 identify the open direct-image stalk with the generic-field cohomology on the strict trait. We can therefore compute the boundary triangle there. Adjunction for open extension by zero gives

\[
D_0(j_!L)=Rj_*L^\vee.
\tag{5.2}
\]

For a finite point module, (4.5) and Lemma 3.1 give

\[
D_0(i_*A)=i_*A^\vee(-1)[-2].
\tag{5.3}
\]

These internal formulas follow by testing Hom from an arbitrary sheaf or complex and using the open or closed adjunction; Section 6 spells out that argument. Apply \(D_0\) to

\[
0\longrightarrow j_!L\longrightarrow j_*L
\longrightarrow i_*A\longrightarrow0.
\tag{5.4}
\]

At the closed stalk, the resulting triangle has the exact segment

\[
0\longrightarrow H^1(D_0j_*L)_s
\longrightarrow H^1(I,M^\vee)
\xrightarrow{b}A^\vee(-1)
\longrightarrow H^2(D_0j_*L)_s\longrightarrow0.
\tag{5.5}
\]

There are no higher terms by (4.2) and (5.3). In degree zero the same triangle identifies \(\mathcal Hom(j_*L,\Lambda)\) with \(j_*L^\vee\), since (5.3) starts in degree two.

It remains to identify \(b\), not merely its source and target. Compare (5.4) with the constant-module sequence

\[
0\to j_!\underline A\to\underline A\to i_*A\to0
\]

using the inclusion \(A=M^I\to M\). Dualizing gives a map from (5.5) to the sequence for \(\underline A\). On the middle term it is restriction of functionals \(M^\vee\to A^\vee\); on the last term it is the identity. For \(A=\Lambda\), apply internal Hom into an injective resolution to this short exact sequence. Its termwise exact dual sequence is the supported-sections sequence
\(0\to i_*i^!I^\bullet\to I^\bullet\to j_*j^{-1}I^\bullet\to0\).
Indeed the three Hom terms are respectively sections with closed support, the resolution itself, and its open direct image. The two maps are support inclusion and restriction. Its boundary is therefore exactly the localization boundary, obtained by differentiating a lift, without an additional sign from identifying the triangle. By (4.5) this boundary is **negative** valuation. For a finite \(A\), evaluate a functional on each \(a\in A\); naturality reduces each evaluation to that constant \(\Lambda\) calculation. Exact finite coefficient duality then identifies the boundary with minus the canonical map \(H^1(I,A^\vee)=A^\vee(-1)\). Thus, for general \(M\), \(b\) is the **negative** of the restriction/evaluation map (4.4), with its \((-1)\) Tate twist. Negation is invertible, and Lemma 4.1 proves that this map is an isomorphism.

Both outside groups in (5.5) consequently vanish. The calculation on \(U\) and these closed stalks proves the asserted positive-Ext vanishing everywhere, and the degree-zero identification proves (5.1). \(\square\)

This calculation includes wild monodromy: one first averages the pro-\(p\) group and then takes tame coinvariants. It does not require the tame monodromy to be semisimple, or the stalk module to be free over \(\Lambda\).

## 6. Constructible duals and biduality

We first justify the adjunction operations just used. For a finite map \(f\), the exact functor \(f_*\) has a right adjoint \(f^!\). One explicit construction is the sheaf associated with

\[
V\longmapsto\operatorname{Hom}_{Y,\Lambda}(f_*\Lambda_V,A),
\tag{6.1}
\]

where \(V\) is an étale object of \(X\) and \(\Lambda_V\) is its free represented module sheaf. This presheaf is already a sheaf: a covering gives the exact coequalizer presentation of \(\Lambda_V\); exact \(f_*\) preserves it, and Hom turns it into the sheaf equalizer. Finite pushforward also preserves arbitrary sums, since its geometric stalks are finite sums of source stalks. Every module sheaf has a presentation by sums of these free represented sheaves. Applying that presentation proves \(\operatorname{Hom}(B,f^!A)=\operatorname{Hom}(f_*B,A)\). Since \(f_*\) is exact, \(f^!\) preserves injectives. Applying \(f^!\) to an injective resolution constructs \(Rf^!\) and its derived adjunction. For an open immersion, the right adjoint of exact \(j_!\) is the exact inverse image \(j^{-1}\). For a closed immersion, \(i^!\) is sections with closed support, agreeing with (4.6).

**Lemma 6.1 (internal adjunction).** For finite \(f\), and bounded constructible \(B\) and a bounded-below \(A\), there is a canonical isomorphism

\[
Rf_*R\mathcal Hom_X(B,Rf^!A)
\xrightarrow{\sim}R\mathcal Hom_Y(Rf_*B,A).
\tag{6.2}
\]

For an open immersion the corresponding formula is

\[
R\mathcal Hom_X(j_!B,A)
=Rj_*R\mathcal Hom_U(B,j^{-1}A).
\tag{6.3}
\]

**Proof.** Test (6.2) by Hom from a complex \(M\) on \(Y\). The sequence of adjunctions is

\[
\begin{aligned}
\operatorname{Hom}(M,Rf_*R\mathcal Hom(B,Rf^!A))
&=\operatorname{Hom}(f^{-1}M\otimes^LB,Rf^!A)\\
&=\operatorname{Hom}(Rf_*(f^{-1}M\otimes^LB),A)\\
&=\operatorname{Hom}(M\otimes^LRf_*B,A)\\
&=\operatorname{Hom}(M,R\mathcal Hom(Rf_*B,A)).
\end{aligned}
\tag{6.4}
\]

The third equality is the finite, hence proper, projection formula of Lesson 14. Its arbitrary-complex domain allows these tensors even if \(\Lambda\) has infinite global dimension. Naturality and Yoneda prove (6.2). All identifications are induced by evaluation and the adjunction counit, so the displayed isomorphism is the counit comparison. Replacing finite pushforward by \(j_!\), using \(j_!B\otimes^LM=j_!(B\otimes^Lj^{-1}M)\) and the open adjunction, gives (6.3). The closed-immersion version of (6.2) is (5.3). \(\square\)

Since tensoring by an invertible local system is exact and local, (5.1) and (4.5) give

\[
\begin{aligned}
D_XL&=L^\vee(1)[2]&&\text{if }L\text{ is locally constant on }X,\\
D_X(i_*A)&=i_*A^\vee&&\text{for a closed point},\\
D_X(j_!L)&=Rj_*L^\vee(1)[2],\\
D_X(j_*L)&=j_*L^\vee(1)[2].
\end{aligned}
\tag{6.5}
\]

**Theorem 6.2 (local biduality).** The functor \(D_X\) preserves \(D^b_c(X,\Lambda)\). The canonical evaluation morphism

\[
F\longrightarrow D_XD_XF
\tag{6.6}
\]

is an isomorphism there.

**Proof.** For a finite-support sheaf, (6.5) reduces both claims to Lemma 3.1. For \(j_*L\), applying the last formula twice cancels the twist and the shift, and gives \(j_*L^{\vee\vee}=j_*L\). The bidual map here is the canonical one: restriction to \(U\) is module evaluation, and the degree-zero internal-Hom comparison in Theorem 5.1 is natural. A morphism between these \(j_*\)-extensions is determined on \(U\), so that restriction identifies (6.6).

For any constructible sheaf \(F\), choose a dense open where it is locally constant and write

\[
A=\ker(F\to j_*j^{-1}F),\quad G=F/A,\quad
J=j_*j^{-1}F,\quad B=J/G.
\tag{6.7}
\]

The sheaves \(A,B\) have finite support and are constructible; \(G\) is a constructible subobject of \(J\). The latter is constructible because its closed stalks are the finite inertia invariants and its restriction to the open is locally constant. The sequences \(0\to G\to J\to B\to0\) and \(0\to A\to F\to G\to0\) show that \(D_XG,D_XF\) are bounded constructible, since that class is closed under triangles. They also give morphisms of biduality triangles. Two known isomorphisms in a triangle imply the third is an isomorphism, by the cohomology long exact sequences. Starting with \(J,B\), then with \(A,G\), proves (6.6) for \(F\).

A bounded constructible complex has a finite sequence of good-truncation triangles whose factors are shifts of its cohomology sheaves. Apply the same triangle argument successively. The shifts use the graded evaluation convention of Section 3; hence these maps are the canonical bidual maps, not merely some isomorphisms between the objects. This proves the theorem. \(\square\)

The dual of \(j_!L\) may have two local cohomology sheaves, from \(R^0j_*\) and \(R^1j_*\). Replacing \(Rj_*\) by \(j_*\) in that line of (6.5) would lose the boundary contribution.

## 7. Finite maps and the dualizing complex

**Theorem 7.1.** For a finite generically étale map \(f:X\to Y\) of smooth curves there is a canonical trace-normalized isomorphism

\[
K_X\xrightarrow{\sim}Rf^!K_Y.
\tag{7.1}
\]

Under it, the counit \(Rf_*Rf^!K_Y\to K_Y\) is \(\tau_f[2]\). For every \(F\in D^b_c(X,\Lambda)\),

\[
D_Y(f_*F)\xrightarrow{\sim}f_*D_XF.
\tag{7.2}
\]

**Proof.** First work without twist or shift. Transpose the weighted trace \(f_*\Lambda_X\to\Lambda_Y\) to a map \(\Lambda_X\to Rf^!\Lambda_Y\). Apply exact finite pushforward and (6.2). The resulting map is

\[
f_*\Lambda_X\longrightarrow
R\mathcal Hom_Y(f_*\Lambda_X,\Lambda_Y),
\qquad a\longmapsto\bigl(b\longmapsto\tau_f(ab)\bigr).
\tag{7.3}
\]

On the dense étale locus this is the perfect dot product on a permutation module. Both sides of (7.3) are its \(j_*\)-extension: the left side by the normality argument in Proposition 2.1, and the right side by Theorem 5.1. Therefore (7.3) is an isomorphism. Finite pushforward is conservative, since a stalk of a source sheaf occurs as a summand in a target geometric stalk; exactness extends conservativity to complexes. Thus the transposed map \(\Lambda_X\to Rf^!\Lambda_Y\) is an isomorphism.

The same argument after tensoring by the invertible \(\mu_{n,Y}\) and shifting by two proves (7.1). Alternatively \(f^{-1}\mu_{n,Y}=\mu_{n,X}\), and (6.4) shows the right adjoint commutes with this invertible twist. The map was defined by transposing \(\tau_f[2]\), so its counit is precisely that trace. Substituting \(A=K_Y\) into (6.2) proves (7.2). \(\square\)

At a ramified closed stalk the elementary form \(\sum e_xa_xb_x\) need not be nondegenerate: some \(e_x\) may be zero modulo \(n\). This does not contradict (7.3). A stalk of **internal** Hom includes compatibility on a neighbourhood and is not the Hom of the two individual stalk modules. The proof uses the generic pairing and its sheaf extension.

If both curves are proper, (7.2), exact finite pushforward and (2.3) identify the global evaluation-and-trace pairing for \(f_*F\) on \(Y\) with the pairing for \(F\) on \(X\). Indeed (6.4) defines (7.2) from the counit; composing that counit with \(\operatorname{Tr}_Y\) is \(\operatorname{Tr}_X\). Thus the duality maps commute with finite pushforward, including their signs.

## 8. Artin's comparison functors on the projective line

We prove the proper theorem first for **every constructible sheaf** on \(X=\mathbf P^1_k\). Define

\[
T^r(F)=\operatorname{Hom}_\Lambda(H^{-r}(X,D_XF),\Lambda).
\tag{8.1}
\]

Evaluation and trace give natural maps

\[
\eta_F^r:H^r(X,F)\longrightarrow T^r(F).
\tag{8.2}
\]

Both sides are cohomological functors of \(F\), and (8.2) respects their connecting maps. For \(T\), dualizing a short exact sequence reverses its triangle, and the exact module dual reverses the cohomology sequence again. Its connecting maps are those obtained by the same Hom-complex and triangle conventions as evaluation. Thus the comparison is a morphism of long exact sequences. All groups are finite by Theorem 6.2 and the ordinary constructible finiteness theorem of Lesson 12.

**Lemma 8.1.** For any constructible sheaf \(F\), \(T^r(F)=0\) if \(r<0\) or \(r>2\). For a finite-support sheaf \(A\), \(\eta_A^r\) is an isomorphism in every degree.

**Proof.** For \(J=j_*L\), (6.5) gives

\[
T^r(J)=H^{2-r}(X,j_*L^\vee(1))^\vee.
\tag{8.3}
\]

The proper curve bound makes this zero for \(r<0\). A finite-support \(A\) has \(D_XA=i_*A^\vee\), so both its ordinary cohomology and \(T\) are concentrated in degree zero. That degree's pairing is evaluation followed by the point trace \(+1\) from Section 4. Lemma 3.1 proves it is perfect.

Use (6.7). The sequence \(G\to J\to B\) and its \(T\) sequence show \(T^r(G)=0\) for \(r<0\); both neighbours \(T^{r-1}(B)\) and \(T^r(J)\) vanish. The sequence \(A\to F\to G\) then gives \(T^r(F)=0\) there as well. Finally \(D_0F\) has no negative sheaf cohomology because it is a derived Hom of sheaves. Hence \(D_XF=D_0F(1)[2]\) has no cohomology below degree \(-2\). Derived global sections preserve this lower bound, so (8.1) is zero for \(r>2\). \(\square\)

In particular the finite-support sequence in (6.7) induces exact rows

\[
\begin{aligned}
0&\to H^0(A)\to H^0(F)\to H^0(G)\to0,\\
0&\to T^0(A)\to T^0(F)\to T^0(G)\to0,
\end{aligned}
\tag{8.4}
\]

and compatible isomorphisms \(H^r(F)=H^r(G)\), \(T^r(F)=T^r(G)\) for \(r>0\). Thus positive degrees reduce to sheaves with no finite-support sections.

**Lemma 8.2.** If \(f:C\to X\) is finite generically étale from a disjoint union of connected smooth projective curves and \(I=f_*\Lambda_C\), then \(\eta_I^0\) and \(\eta_I^2\) are isomorphisms. Moreover \(H^1(X,I)\) and \(T^1(I)\) have equal order.

**Proof.** By Section 7 the comparison is the constant-coefficient comparison on \(C\). On each component, \(H^0(C,\Lambda)=\Lambda\) and \(H^2(C,\mu_n)=\Lambda\); their pairing is multiplication followed by the trace identity. The exchanged pairing contracts \(H^2(C,\Lambda)=\Lambda(-1)\) with \(H^0(C,\mu_n)=\Lambda(1)\). Thus the comparisons in degrees zero and two are isomorphisms. In degree one, Lesson 10 gives both \(H^1(C,\Lambda)\) and \(H^1(C,\mu_n)\) order \(n^{2g}\), where a root identifies the coefficient sheaves if needed. The latter group's dual has the same order by Lemma 3.1. Sum over the components. No degree-one perfect pairing has yet been used. \(\square\)

For constants on \(\mathbf P^1\), genus is zero, so \(H^1=0\) and Lemma 8.2 directly proves duality in every degree. The next two sections are necessary to extend that calculation from constants to all constructible sheaves.

## 9. Finite-constant embeddings and effacement

**Lemma 9.1.** Suppose \(G\) is constructible on a smooth projective curve \(X\) and has no nonzero finite-support subsheaf. There exists a finite generically étale map \(f:C\to X\), with \(C\) a disjoint union of smooth projective curves, and a monomorphism

\[
G\longrightarrow I=f_*\Lambda_C.
\tag{9.1}
\]

It can be chosen so that

\[
H^r(X,G)\longrightarrow H^r(X,I)=H^r(C,\Lambda)
\quad\text{is zero for every }r>0.
\tag{9.2}
\]

**Proof of the embedding.** Choose a dense open \(U\) where \(G\) is locally constant, with finite fibre module \(M\). The map \(G\to j_*G|_U\) is injective: its kernel has finite support. The finite monodromy of \(M\) factors through a finite group \(\Gamma\), realized by a finite étale cover of \(U\).

As a \(\Lambda\)-module, \(M\) embeds in \(\Lambda^a\). On a cyclic summand of order \(d\mid n\), use multiplication by \(n/d\) into \(\Lambda\), and sum these embeddings. Let \(h:M\hookrightarrow\Lambda^a\) be one such injection. The map

\[
m\longmapsto(\gamma\longmapsto h(\gamma m))
\tag{9.3}
\]

embeds \(M\) equivariantly into the permutation module \(\operatorname{Map}(\Gamma,\Lambda^a)\), with the action \((g\phi)(\gamma)=\phi(\gamma g)\). It is injective by evaluation at the identity, and the displayed formula verifies equivariance. On sheaves this gives \(G|_U\hookrightarrow r_*\Lambda\), allowing \(a\) disjoint copies of the trivializing cover \(r\).

Normalize \(X\) in the function fields of these cover components. Normalization is finite, its curves are smooth because \(k\) is perfect, and they are projective. The resulting \(f:C\to X\) is generically étale. Normality gives \(f_*\Lambda=j_*r_*\Lambda\), as in Section 2. Thus applying left exact \(j_*\) to (9.3), and composing with \(G\to j_*G|_U\), proves (9.1). \(\square\)

**Proof of effacement.** Start with this embedding. All \(H^1(C,\Lambda)\) are finite. Each of their elements is a \(\Lambda\)-torsor, hence becomes zero after pullback to that finite étale torsor. Take the fibre product of the finitely many torsors and choose, on each connected component of \(C\), one connected component of the product. It still surjects onto that component: a nonempty finite étale image is open and closed. This gives a finite étale cover killing every degree-one class. Its source remains smooth projective.

Next kill degree two. On each of the resulting connected curves choose a rational function \(a\) with valuation one at some point; a uniformizer in that point's local ring is such a rational function. The polynomial \(T^n-a\) is Eisenstein at that discrete valuation ring, so defines a function-field extension of degree \(n\). Its derivative is nonzero because \(n\) is invertible. Normalize the projective curve in this extension to obtain a finite generically étale cover of degree \(n\) by a smooth projective curve. Pullback on \(H^2(-,\mu_n)\) is multiplication by \(n\), by Lesson 10, Proposition 8.1, and is therefore zero. Choose a root of unity to infer the same statement for \(H^2(-,\Lambda)\); the zero map is independent of that choice.

The composite cover \(h:C'\to C\) kills all positive cohomology of \(\Lambda\): degree one stays zero after the second pullback, degree two has just been killed, and larger degrees already vanish. The sheaf unit \(\Lambda_C\to h_*\Lambda_{C'}\) is a monomorphism, since on each geometric stalk it is the diagonal into a nonempty set of sheets, including at ramified points. Composing (9.1) with its exact finite pushforward therefore remains a monomorphism \(G\to(fh)_*\Lambda\). On cohomology the new map factors through pullback to \(C'\), proving (9.2). \(\square\)

The lemma kills the relevant cohomology through one finite-constant embedding. It does not assert that \(G\) itself becomes constant on the whole projective curve.

## 10. The full Artin diagram chase

**Theorem 10.1.** On \(X=\mathbf P^1_k\), every \(\eta_F^r\) in (8.2) is an isomorphism for every constructible \(\Lambda\)-sheaf \(F\) and every integer \(r\).

**Proof.** Remove the finite-support part as in (6.7) and write an effacing embedding from Lemma 9.1 as

\[
0\longrightarrow G\longrightarrow I\longrightarrow Q\longrightarrow0.
\tag{10.1}
\]

Its two long exact sequences form a commutative diagram under \(\eta\). We will use exactness explicitly. Write \(a\) for an ordinary-cohomology element and \(b\) for a \(T\)-element, and let \(\delta\) denote the corresponding connecting maps.

**Degree-zero injectivity for all sheaves.** Both rows start with a monomorphism from the degree-zero group of \(G\) into that of \(I\), since negative groups vanish. If \(\eta_G^0(a)=0\), the image of \(a\) in \(H^0(I)\) has zero image under the isomorphism \(\eta_I^0\) of Lemma 8.2; hence that image is zero, and \(a=0\). The exact rows (8.4), together with finite-support duality, extend this injectivity to \(F\). This conclusion holds for every constructible sheaf, and in particular for \(Q\).

**Degree-zero surjectivity.** Given \(b\in T^0(G)\), send it into \(T^0(I)\) and lift there to \(a_I\in H^0(I)\) using \(\eta_I^0\). Its image \(a_Q\in H^0(Q)\) has zero \(\eta_Q^0\), because the image of \(b\) in \(T^0(Q)\) is zero. The injectivity just proved implies \(a_Q=0\). Thus \(a_I\) comes from \(a_G\in H^0(G)\); the injectivity \(T^0(G)\to T^0(I)\) now gives \(\eta_G^0(a_G)=b\). The rows (8.4) extend this isomorphism to every \(F\). We have proved every \(\eta^0\) is an isomorphism.

**Degree-one injectivity.** Suppose \(a_G\in H^1(G)\) has \(\eta_G^1(a_G)=0\). Effacement makes its image in \(H^1(I)\) zero, so \(a_G=\delta(a_Q)\) for some \(a_Q\in H^0(Q)\). The image \(\eta_Q^0(a_Q)\) has zero boundary in \(T^1(G)\), hence comes from \(b_I\in T^0(I)\). Lift \(b_I\) by \(\eta_I^0\) to \(a_I\in H^0(I)\). The difference between \(a_Q\) and the image of \(a_I\) has zero \(\eta_Q^0\), so is zero. Therefore \(\delta(a_Q)=0\) and \(a_G=0\). By (8.4) and its positive-degree isomorphisms this proves injectivity of \(\eta_F^1\) for every \(F\).

Apply this conclusion to \(I\) itself, viewed as a constructible sheaf on \(\mathbf P^1\). Lemma 8.2 gives equal finite orders on its two sides. Thus \(\eta_I^1\) is an isomorphism. This is how the degree-one constant pairing on its cover curves enters the proof; it has not been assumed.

**Degree-one surjectivity.** Let \(b_G\in T^1(G)\). Its image in \(T^1(I)\) lifts to \(a_I\in H^1(I)\). The image \(a_Q\in H^1(Q)\) has zero image under the already injective \(\eta_Q^1\); hence \(a_Q=0\). Lift \(a_I\) to \(a_G\in H^1(G)\). The difference \(b_G-\eta_G^1(a_G)\) is in the kernel of \(T^1(G)\to T^1(I)\), and therefore equals \(\delta(b_Q)\) for some \(b_Q\in T^0(Q)\). Surjectivity of \(\eta_Q^0\) lifts \(b_Q\) to an ordinary \(a_Q\), whose boundary supplies this remaining difference. Thus \(\eta_G^1\) is surjective. Reduction through the finite-support part proves every \(\eta_F^1\) is an isomorphism.

**Degree-two injectivity.** If \(a_G\in H^2(G)\) maps to zero under \(\eta_G^2\), effacement writes it as \(\delta(a_Q)\) with \(a_Q\in H^1(Q)\). Its \(\eta_Q^1\)-image comes from \(T^1(I)\), whose element lifts by the just proved isomorphism \(\eta_I^1\). Injectivity of \(\eta_Q^1\) says that \(a_Q\) differs from that lift's image by zero. Therefore its boundary is zero. This proves injectivity in degree two, first for \(G\), then for every \(F\).

**Degree-two surjectivity.** Given \(b_G\in T^2(G)\), its image in \(T^2(I)\) lifts to \(a_I\in H^2(I)\), since \(\eta_I^2\) is an isomorphism by Lemma 8.2. Its image in \(H^2(Q)\) has zero \(\eta_Q^2\), and the preceding injectivity makes that image zero. Lift \(a_I\) to \(a_G\in H^2(G)\). The remaining difference lies in the image of \(T^1(Q)\), and is the boundary of an ordinary element of \(H^1(Q)\) because \(\eta_Q^1\) is surjective. This completes degree two, and reduction gives the result for every \(F\).

Ordinary groups and \(T\)-groups vanish below zero and above two. All degrees have now been proved. \(\square\)

**Corollary 10.2 (all proper smooth curves).** The same theorem holds on every smooth projective curve.

**Proof.** On each connected curve \(C\), choose a nonconstant separating rational function \(t\). Such a function exists since \(k\) is perfect and the smooth function field has transcendence degree one: its differential space has dimension one, and some \(dt\neq0\); then the finite extension \(k(C)/k(t)\) is separable, by the exact differential sequence. At a valuation point, either \(t\) or \(t^{-1}\) is regular, so \(t\) extends to \(f:C\to\mathbf P^1\). This map is proper with finite fibres and hence finite, and is generically étale by separability.

The sheaf \(f_*F\) is constructible. Formula (7.2) and exact finite pushforward identify its ordinary and \(T\) groups with those for \(F\) on \(C\). Section 7 proves that these identifications commute with the comparison \(\eta\), including trace. Theorem 10.1 therefore proves the result on \(C\). For disjoint components take finite direct sums. \(\square\)

This reduction uses the full constructible theorem on \(\mathbf P^1\). Checking only its constant sheaf, whose degree-one cohomology is zero, would not justify the corollary.

## 11. Open curves and the derived theorem

**Theorem 11.1 (Poincaré duality).** For any smooth curve \(X\) and \(F\in D^b_c(X,\Lambda)\), the map adjoint to (1.2) is a canonical isomorphism

\[
R\Gamma(X,D_XF)\xrightarrow{\sim}
R\operatorname{Hom}_\Lambda(R\Gamma_c(X,F),\Lambda).
\tag{11.1}
\]

For a constructible sheaf \(F\), it identifies each factor of

\[
H^r_c(X,F)\times
\mathbb H^{2-r}\bigl(X,R\mathcal Hom_\Lambda(F,\mu_n)\bigr)
\xrightarrow{\ \operatorname{Tr}(a\cup b)\ }\Lambda
\tag{11.2}
\]

with the finite \(\Lambda\)-dual of the other. In particular, if \(L\) is locally constant, the second factor is \(H^{2-r}(X,L^\vee(1))\).

**Proof.** On a proper curve, Corollary 10.2 says that the map \(R\Gamma(F)\to R\operatorname{Hom}(R\Gamma(D_XF),\Lambda)\) induces an isomorphism on every cohomology group, by (3.1). It is therefore an isomorphism. Exact finite-group biduality identifies its transposed map with (11.1); both are the adjoints of the same ordered evaluation pairing. This proves (11.1) for sheaves on proper curves. Natural evaluation comparisons respect triangles. Induction on the finite number of nonzero cohomology sheaves, using good-truncation triangles, proves it for every \(D^b_c\) complex on a proper curve.

Now choose a smooth projective completion \(j:X\hookrightarrow\overline X\). Exact \(j_!\) preserves bounded constructibility, and (6.3) gives

\[
D_{\overline X}(j_!F)=Rj_*D_XF.
\tag{11.3}
\]

Apply the proper theorem to \(j_!F\). On its right side, \(R\Gamma(\overline X,j_!F)=R\Gamma_c(X,F)\). On its left side, (11.3) gives \(R\Gamma(\overline X,Rj_*D_XF)=R\Gamma(X,D_XF)\). The compact trace is defined through this completion, and (6.3) is defined by evaluation; hence this transported map is exactly (11.1), not an unrelated isomorphism of its objects.

For a sheaf, take degree \(-r\) in (11.1). Its left-hand group is the second factor of (11.2), and its right-hand group is \(H^r_c(X,F)^\vee\) by (3.1). Finiteness follows from Lessons 12 and 14 and Theorem 6.2. Dualizing again gives the converse identification, so the pairing is mutually perfect. The first line of (6.5) gives the local-system specialization. \(\square\)

For arbitrary constructible \(F\), the second factor in (11.2) is hypercohomology of **internal derived** Hom. It cannot generally be replaced by ordinary cohomology of the degree-zero dual sheaf. Its local boundary terms carry the ramification information computed in Sections 4–6.

## 12. Cup product and the Jacobian

Let \(C\) be connected smooth projective of genus \(g\). The theorem and Section 2 give the canonical perfect pairing

\[
H^1(C,\Lambda)\times H^1(C,\mu_n)\longrightarrow\Lambda,
\qquad (a,b)\longmapsto\operatorname{Tr}_C(a\cup b),
\tag{12.1}
\]

and \(H^2(C,\mu_n)=\Lambda\) by trace. Choosing a primitive root turns (12.1) into a perfect pairing on \(H^1(C,\Lambda)\). Without that choice, the pairing of two untwisted classes takes values in \(\Lambda(-1)\); no canonical root has been silently inserted.

Kummer identifies

\[
H^1(C,\mu_n)=\operatorname{Pic}^0(C)[n]=Jn,
\tag{12.2}
\]

where \(J\) is the Jacobian. Tensoring the trace by the invertible \(\mu_n\) gives the perfect pairing

\[
H^1(C,\mu_n)\times H^1(C,\mu_n)
\xrightarrow{\cup}H^2(C,\mu_n^{\otimes2})
\xrightarrow{\operatorname{Tr}}\mu_n(k).
\tag{12.3}
\]

**Jacobian comparison, stated.** Under (12.2) and the principal polarization of \(J\), (12.3) is the Weil pairing, up to the sign, or equivalently the inversion, attached to the chosen polarization/Abel-map convention. We state this comparison without proof; it is not used in the proof of Theorem 11.1. In particular, perfection of (12.3) has already been proved for every invertible \(n\), independently of that comparison.

Here is a precise way to read the historical sign, rather than identifying an unspecified Weil convention with a guessed sign. Fix \(o\in C(k)\), let \(a_o:C\to J\) send \(x\) to \(\mathcal O_C(x-o)\), and let \(u\in H^1(C,J[n])\) be the pullback along \(a_o\) of the \([n]\)-torsor on \(J\). For \(v:J[n]\to\Lambda\), write \(u_v=v_*u\). The comparison in Deligne's convention says

\[
\operatorname{Tr}(u_v\cup b)=v(b),\qquad
\operatorname{Tr}(b\cup u_v)=-v(b)
\quad(b\in H^1(C,\mu_n)=J[n]).
\tag{12.4}
\]

These are two orders of the same degree-one pairing. The second is the minus sign in Arcata, VI.2. The full argument in “Dualité,” §3, compares the \((1,1)\) Künneth component of the diagonal class with \(-u\). It obtains that minus sign when the Kummer connecting map is moved past a degree-one shift. Evaluation against the diagonal then gives the first equality of (12.4), and the graded exchange gives the second. This explains which convention the stated comparison uses; we do not turn that geometric comparison into an omitted step of the preceding duality proof.

The comparison also shows that the self-pairing in (12.3) is alternating. Graded commutativity alone would give only \(2(b\cup b)=0\); when \(n\) is even, that weaker identity does not establish alternation. The alternating conclusion here uses the stated Weil-pairing comparison. The perfectness conclusion uses the proved duality theorem.

## 13. Three examples

**Example 13.1: the projective line.** The nonzero groups are

\[
H^0(\mathbf P^1,\Lambda)=\Lambda,\qquad
H^2(\mathbf P^1,\mu_n)=\Lambda.
\]

The latter generator is \(c_1^{(n)}(\mathcal O(1))\). Their pairing sends \((a,b)\) to \(ab\), since its trace is one. Degree one is zero on both sides. The exchanged degree-zero/degree-two pairing is again evaluation with the appropriate twist. This verifies the constant-coefficient theorem directly.

**Example 13.2: an elliptic curve.** For \(E\) with origin, \(\operatorname{Pic}^0(E)\) is identified with \(E\) through the chosen standard polarization convention. Thus

\
H^1(E,\mu_n)=E[n,\qquad
|En|=n^2.
\]

The theorem proves its cup-and-trace pairing is perfect. The stated comparison identifies it with the Weil pairing, with the convention-dependent inversion described in Section 12. In a symplectic basis its values have the form \(e_n(P,Q)=\zeta\), \(e_n(P,P)=e_n(Q,Q)=1\). Reversing the ordered basis inverts \(\zeta\). The origin and polarization enter the geometric identification, whereas the trace of a point remains \(+1\).

**Example 13.3: the punctured line.** Write \(U=\mathbf G_m\subset\mathbf P^1\), with boundary ordered as \((0,\infty)\). Compact localization and Kummer give

\[
H^1_c(U,\Lambda)=\operatorname{coker}(\Lambda\xrightarrow{\mathrm{diag}}\Lambda^2),
\qquad H^1(U,\mu_n)=\Lambda\cdot\kappa(t).
\tag{13.1}
\]

Here \(\kappa(t)\) is the Kummer class of the coordinate. Its valuations are \(+1\) at zero and \(-1\) at infinity; its **trace-normalized supported residues** are their negatives, by (4.5). Both groups have order \(n\), and Theorem 11.1 identifies them as duals. With the usual connecting map of compact localization, put \(c=\delta(0,1)\). The explicit computation in Solution 2 gives

\[
\operatorname{Tr}(c\cup\kappa(t))=-1.
\tag{13.2}
\]

Thus the pairing in the bases \(c,\kappa(t)\) is \((a,b)\mapsto-ab\), still a perfect pairing over \(\Lambda\). Ordinary and compact degree one happen to have the same order here, but their generators come from different constructions.

## 14. Exercises

1. **Easy.** Verify all constant-coefficient duality pairings on \(\mathbf P^1\), retaining the Tate twist until a root is chosen.
2. **Medium.** Compute both sides of duality for \(U=\mathbf G_m\) and \(F=\Lambda\). Identify the boundary generator of \(H^1_c\), the Kummer generator of \(H^1\), and their pairing. Check the other degrees as well.
3. **Medium.** For a closed point \(i\) and a dense open \(j\) with finite local system \(L\), compute \(D_X(i_*\Lambda)\) and \(D_X(j_!L)\). Describe the two possible boundary cohomology sheaves in the second answer.
4. **Medium.** Prove that \(H^1(X,L)\) and \(H^1_c(X,L^\vee(1))\) have the same order on a smooth affine curve. Allow finite nonfree \(\Lambda\)-module fibres.
5. **Hard.** Prove local biduality for \(j_*L\) at a missing point using wild and tame inertia. Identify the boundary map in the Ext sequence, and explain why replacing coinvariants by invariants is invalid.

## 15. Complete solutions

**Solution 1.** Proper support equals ordinary support. Since genus is zero, Lesson 10 gives \(H^1(\mathbf P^1,\mu_n)=0\), and choosing any primitive root gives the same vanishing for \(\Lambda\). The groups \(H^0(\Lambda)=\Lambda\) and \(H^2(\mu_n)=\Lambda\) pair by multiplication because \(\operatorname{Tr}(c_1^{(n)}\mathcal O(1))=1\). In the other order, \(H^2(\Lambda)=\Lambda(-1)\) pairs with \(H^0(\mu_n)=\Lambda(1)\) by their canonical contraction to \(\Lambda\); the trace supplies the identity. The factors in degree one are both zero. All groups outside degrees zero through two vanish, so the remaining pairings are between zero groups. A root trivializes both twists in the exchanged pairing and again yields multiplication. This verifies each degree without invoking general duality. \(\square\)

**Solution 2.** Since \(\operatorname{Pic}(\mathbf G_m)=0\) and \(k[t,t^{-1}]^\times=k^\times t^{\mathbf Z}\), Kummer gives

\[
H^0(U,\mu_n)=\mu_n(k),\quad H^1(U,\mu_n)=\Lambda\kappa(t),
\quad H^q(U,\mu_n)=0\ (q\geq2).
\tag{15.1}
\]

The compact localization sequence for the ordered boundary \(D=(0,\infty)\) gives

\[
H^0_c(U,\Lambda)=0,\quad
H^1_c(U,\Lambda)=\Lambda^2/\mathrm{diag}(\Lambda),\quad
H^2_c(U,\Lambda)=\Lambda(-1),
\tag{15.2}
\]

and no higher groups. The generator \(c=\delta(0,1)\) identifies the quotient with \(\Lambda\) by \((a_0,a_\infty)\mapsto a_\infty-a_0\).

We detail its pairing sign. For an ordinary degree-one class \(b\) on \(U\), the supported localization boundary at \(D\) is its vector of residues \(\partial b\in H^0(D,\Lambda)\), using the point orientation (4.5). Evaluation pairs this with a boundary value \(a\in H^0(D,\Lambda)\). Compatibility of the open and closed evaluation triangles gives

\[
\operatorname{Tr}(\delta a\cup b)
=-\sum_{x\in D}a_x\operatorname{res}_x(b).
\tag{15.3}
\]

To see the minus explicitly, represent the two localization triangles by cones and use the differential rule \(d(v\cup w)=dv\cup w+(-1)^{\deg v}v\cup dw\). Moving the connecting operator from the first degree-one boundary class to the second degree-one ordinary class changes the sign once. The remaining degree-two supported class is the point evaluation, whose trace is \(+1\) by Section 4. Thus the adjoint residue is the negative of the compact connecting map, giving (15.3). This also shows the formula is independent of a chosen cochain representative: changing the lift adds a coboundary, and adding a diagonal value contributes zero because the sum of the residues of a global Kummer unit on this punctured projective line is zero.

For \(b=\kappa(t)\), negative valuation gives \(\operatorname{res}_0b=-1\) and \(\operatorname{res}_\infty b=1\). Hence (15.3) is \(a_0-a_\infty\). Taking \(a=(0,1)\) proves (13.2), and scaling the two classes gives \((a,b)\mapsto-ab\) on their two copies of \(\Lambda\). In degree two, \(H^2_c(U,\Lambda)=\Lambda(-1)\) pairs perfectly with \(H^0(U,\mu_n)=\Lambda(1)\) by contraction and trace. In degree zero both relevant groups are zero. This checks every degree. \(\square\)

**Solution 3.** Internal closed adjunction gives

\[
R\mathcal Hom_X(i_*\Lambda,K_X)
=i_*R\operatorname{Hom}_\Lambda(\Lambda,Ri^!K_X).
\]

By (4.5), \(Ri^!K_X=\Lambda\); hence \(D_X(i_*\Lambda)=i_*\Lambda\), in degree zero, with the point trace normalized to one. For the open, (6.3) and finite-module duality give

\[
D_X(j_!L)=Rj_*L^\vee(1)[2].
\]

At a missing point with module \(M\), (4.2) identifies the stalk of its cohomology in degree \(-2\) as \((M^\vee)^I(1)\), and in degree \(-1\) as \(H^1(I,M^\vee)(1)=(M^I)^\vee\). There is no higher local contribution. On the open only degree \(-2\) remains. The degree \(-1\) sheaf is supported on the finite boundary. Dropping \(R^1j_*\) would erase it. \(\square\)

**Solution 4.** Apply Theorem 11.1 to the local system \(F=L^\vee(1)\). Lemma 3.1 and the invertibility of the twist identify

\[
F^\vee(1)=(L^\vee(1))^\vee(1)=L.
\]

The degree-one pairing is therefore

\[
H^1_c(X,L^\vee(1))\times H^1(X,L)\longrightarrow\Lambda.
\]

It identifies the ordinary group with the dual of the compact group. Both are finite, and Lemma 3.1 says a finite module and its dual have equal cardinality. Their orders are consequently equal. Neither that lemma nor local-system duality assumes free fibres. Affineness ensures the usual ordinary degree-one bound; the equality itself also holds on any smooth curve. \(\square\)

**Solution 5.** On the strict trait of the missing point let \(M=L_{\bar\eta}\) and \(A=M^I\). Wild invariants are exact by averaging, since \(P\) is pro-\(p\) and \(n\) is prime to \(p\). Tame cohomology is computed by the cyclic resolution and inflation, giving

\[
H^1(I,M^\vee)=((M^\vee)^P)_T(-1)
=(M^I)^\vee(-1),\qquad H^{>1}(I,M^\vee)=0.
\]

The middle equality is restriction of functionals after taking coinvariants, justified by dualizing \(\gamma-1\). It is not the equality of \((M^I)^\vee\) with \((M^\vee)^I\).

Dualize \(0\to j_!M\to j_*M\to i_*A\to0\) with \(D_0\). The local point orientation gives \(D_0i_*A=i_*A^\vee(-1)[-2]\); open adjunction gives \(D_0j_!M=Rj_*M^\vee\). Thus positive Ext is the kernel or cokernel of

\[
H^1(I,M^\vee)\longrightarrow A^\vee(-1).
\]

Compare with the constant \(A\) sequence using \(A\hookrightarrow M\). The injective-resolution calculation in Theorem 5.1 identifies the arrow with restriction of functionals followed by the ordinary localization boundary. In the trace-normalized target (4.5), it is the **negative** of the displayed coinvariant isomorphism. Its kernel and cokernel are zero; higher Ext is already zero. Degree zero is \(j_*M^\vee\). Hence \(D_0j_*M=j_*M^\vee\), and applying the same calculation to \(M^\vee\) gives \(D_0D_0j_*M=j_*M^{\vee\vee}=j_*M\). Evaluation is this isomorphism by naturality, and adding \((1)[2]\) twice cancels the twists and shifts as in Theorem 6.2.

For the requested obstruction, take \(M=\mathbf F_\ell^2\) with tame generator \(\gamma(e_1)=e_1\), \(\gamma(e_2)=e_2+e_1\). Then \(M^T=\mathbf F_\ell e_1\), whereas \(M_T=M/\mathbf F_\ell e_1\); the natural invariant-to-coinvariant map is zero. The pairing of dual coinvariants with invariants, however, is perfect by (4.4). This verifies both the ramified biduality calculation and the necessity of its corrected map. \(\square\)

## 16. Sources and the boundary of the comparison

- **[Local and global curve proof]** P. Deligne, *[SGA 4½](https://publications.ias.edu/sites/default/files/Number32.pdf)*, “Dualité,” §§1–3, especially Théorèmes 1.3–1.4 and 2.2, Lemme 2.3, and the Artin argument in §2.5. Sections 3–10 above supply the coefficient algebra, inertia map, point orientation, finite trace, finite covers and every diagram chase. The argument there uses dual coinvariants; Lemma 4.1 writes out the evaluation map explicitly.
- **[Trace and historical signs]** Deligne, [“Cohomologie étale: les points de départ”](https://publications.ias.edu/sites/default/files/Number32.pdf) [Arcata], the curve-duality discussion in VI.1–VI.2, including the minus sign of VI.2. “Dualité,” §3, proves the diagonal/torsor comparison described in Section 12. The Jacobian/Weil identification is stated here without proof; the constructible duality proof is complete without it.
- **[Original adjunction formalism]** *[SGA 4](https://www.normalesup.org/~forgogozo/SGA4/)*, Exposé XVIII, §§2–3, especially 2.9, 3.1.8, 3.1.10 and 3.2.3–3.2.6. The trace counit and internal adjunction used here are proved directly in Sections 6–7. The general higher-dimensional smooth duality theorem in XVIII.3.2.5 is historical context, not an unproved premise for the curve argument.
- **[Modern exceptional inverse image]** The Stacks Project Authors, [locally quasi-finite duality, Tags 0F58–0F59](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-section-duality-locally-quasi-finite), [its derived form, Tags 0F5M–0F5N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-section-derived-duality-locally-quasi-finite), [general derived upper shriek, Tags 0G2B–0G2C](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-section-derived-upper-shriek), and [the presheaf description, Tag 0GLK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-lemma-describe-Rf-upper-shriek). The finite/open portion needed here is constructed in Section 6, and its internal formula is proved by the full Yoneda calculation.
- **[Weighted trace]** [Weightings and trace maps, Tags 0GKE, 0GKG and 0GKI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-section-weightings). Proposition 2.1 proves the relevant finite smooth-curve trace, including ramification weights and norm compatibility. Theorem 7.1 explains why a possibly degenerate raw closed-stalk weighted form still defines a perfect internal sheaf pairing.
- **[Curve cohomology comparison]** [Curves revisited, Tags 03VJ, 03VK and 03VM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/trace.html#trace-section-cohomology-curves-revisited), [smooth projective curve groups, Tag 03RQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-cohomology-smooth-projective-curve), and [finite pullback on degree two, Tag 0AMB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-pullback-on-h2-curve). The trace chapter's duality remark and its sketch of the \(K(\pi,1)\) assertion are not proofs of the theorem used here. The full constructible theorem and local biduality are proved above, beyond those modern remarks.

Lessons 10 and 14 supply the curve degree and compact-support foundations; the next lesson develops purity and Gysin maps beyond the point calculation already proved here. The fixed trace and the order in (1.2) supply the normalization needed for the Lefschetz trace formula. This lesson distinguishes complete curve duality from the Jacobian comparison, which it states without proof. The linked AI Integrated Stacks Project reader contains AI-proposed corrections and additions and is not reviewed by the maintainers of the [official Stacks Project](https://stacks.math.columbia.edu/).
