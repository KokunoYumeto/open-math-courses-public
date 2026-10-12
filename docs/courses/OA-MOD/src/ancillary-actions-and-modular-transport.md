# Ancillary actions and modular transport

An action on a von Neumann algebra moves both the points of its centre and the factor lying over each point. Its ancillary groupoid records those two motions together. Keeping the full groupoid is essential: two group elements can have the same endpoints and still act differently on the factor. We first compare algebraic cocycle conjugacy with this field description, then split countable ancillary groupoids, correct noncommutative composition defects, and transport weights and their complete modular domains.

All von Neumann algebras below have separable predual. Measured spaces are standard and carry nonzero sigma-finite measures. A group action on an algebra is continuous in the usual automorphism topology. A group described as separable locally compact is not assumed second countable. A strict field action obeys its identities at every arrow of its specified invariant conull model. An identity between the original measurable representatives, by contrast, can hold almost everywhere separately for each group element.

We use the following earlier programme proofs, with these abbreviations.

| Name | Earlier proof and the part used |
| --- | --- |
| STRICT | Strict variable fields and ancillary conjugacy, Sections 1–6: simultaneous field localization, exact unitary cocycles, canonical conjugating fields and independence of choices |
| LOCAL | Localizing factor actions and uniform cocycles, Sections 1–6: Haar repair, exact representatives, effective quotients and automatic continuity |
| VAR | Variable factor fields and measurable conjugacy, Theorem 1.1 and Sections 2–3: decomposition and integration of an isomorphism |
| INNER | Ancillary actions and unitary corrections, Lemmas 1.1 and 2.1 and Theorem 2.2: the Borel inner subgroup, its unitary section and constant fields |
| SUSP | A suspension from separated crossings, the complete suspension theorem through (S32) |
| RETURN | Return arrows and factor-field flows, Theorems 3.1 and 4.1 and Corollary 4.2: return products, unitary correction and the transitive case |

The central standard-form input needed by the first three proofs is supplied in Section 1. All later uses of cohomology reduction refer to the proved 1. Lifting arrows with compatible finite choices through 4. Measurable flows and their return cocycles.

## 1. Central standard forms and the ancillary action

Let \(M\) be represented faithfully on a separable Hilbert space. The central decomposition constructed in Realizing an abelian algebra as the diagonal algebra through Centers and the factor decomposition gives

\[
 M=\int_X^\oplus M_x\,d\mu(x),\qquad
 Z(M)=L^\infty(X,\mu),
 \tag{ANC.1}
\]

with factor fibres almost everywhere. We need this decomposition in measurable standard forms, including the cones, rather than just as algebras of decomposable operators.

Choose a faithful normal state \(\varphi\). For example, sum the vector functionals of a countable dense sequence of unit vectors with strictly positive summable coefficients. Normality follows by monotone convergence; a positive operator on which the sum vanishes annihilates the dense sequence and is zero. By Central disintegration of a separable weighted algebra, disintegrate this state over the specified central diagonal. Its proof constructs actual measurable GNS spaces and gives

\[
 H_\varphi=\int_X^\oplus H_{\varphi_x}\,d\mu(x),\qquad
 J_\varphi=\int_X^\oplus J_x\,d\mu(x),\qquad
 \Delta_\varphi=\int_X^\oplus\Delta_x\,d\mu(x).
 \tag{ANC.2}
\]

The last equality includes the maximal square-integrability domain, by Constructing the integral weight and its full operators. Each \(\varphi_x\) is normal, semifinite and faithful. Since \(\int\varphi_x(1)\,d\mu=1\), it is finite almost everywhere. On nonzero fibres its value at one is strictly positive. Remove the exceptional null set. Recovering measurable GNS vectors by an injective equation makes \(\Omega_x=\Lambda_{\varphi_x}(1)\) a measurable section. Finiteness has been established before applying that inverse-GNS result.

Here is the missing cone argument. Let \(a_j(x)\) be the common countable strong* dense contraction family of A common countable strong* dense contraction family. The finite-weight case of Quarter powers produce a self-dual cone says

\[
 P_x=\overline{\{aJ_xaJ_x\Omega_x:a\in M_x\}}.
 \tag{ANC.3}
\]

Indeed its quadratic generators are \(\lambda(\xi)J_x\xi\); for the finite weight every \(\xi=\Lambda_{\varphi_x}(a)=a\Omega_x\) belongs to the finite star domain, and \(J_x\Omega_x=\Omega_x\). Thus these are exactly the vectors in (ANC.3). Bounded strong* approximation and continuity of multiplication on bounded sets show that the countable measurable sections

\[
 n^2a_j(x)J_xa_j(x)J_x\Omega_x,\qquad n,j\geq1,
 \tag{ANC.4}
\]

are dense in every \(P_x\). Integer scaling suffices: write any bounded \(a\) as \(n(a/n)\), with \(n\geq\|a\|\).

Let \(Q\) be the cone of square-integrable measurable sections lying in \(P_x\) almost everywhere. It is closed: from an \(L^2\)-convergent sequence take a pointwise convergent subsequence, and use closedness of each \(P_x\). It is self-dual. To see the nontrivial inclusion, test a vector in its dual against the sections (ANC.4), normalized to have norm at most one and restricted to sets of finite measure. Testing all such restrictions forces each fibre inner product to be real and nonnegative almost everywhere. A common null set works for this countable family; density and the self-duality of \(P_x\), proved in SF-04, then put the vector in \(Q\). The reverse inclusion follows by integration of nonnegative fibre inner products.

The global natural cone lies in \(Q\), since its quadratic generators decompose as in (ANC.3), using (ANC.2). Both cones are self-dual, so inclusion reverses on taking duals and gives equality. We have proved

\[
 (M,H_\varphi,J_\varphi,P_\varphi)
 =\int_X^\oplus(M_x,H_{\varphi_x},J_x,P_x)\,d\mu(x)
 \tag{ANC.5}
\]

in the precise sense of the algebra, Hilbert space, conjugation and cone. The fibre standard-form axioms are The standard-form axioms.

Canonical implementers are measurable in these fields. For completeness, use the measurable orthonormal frames of Compact orthonormal frames and measurable dimension to work on each fixed-dimension stratum. Given a measurable field of normal isomorphisms, impose on an ambient unitary the equations implementing the countable algebra generators and intertwining the conjugations, and the two cone inclusions tested on the countable dense families (ANC.4). These are Borel conditions: equality is tested on countable Hilbert frames, and distance to a cone is the infimum of distances to its dense family. The canonical implementation theorem Patching the unique comparisons gives exactly one such unitary in every fibre. Projection of this Borel graph to the parameter space is therefore a Borel bijection. The proved injective Borel image theorem, Theorem 4.3(5) in Polish spaces and standard Borel spaces, makes its inverse Borel. Conversely a measurable unitary field implements a measurable algebra field by conjugation. This establishes the measurability required in VAR and STRICT without assuming a classification of factors.

Now let \(\alpha:G\to\operatorname{Aut}(M)\). Choose a strict nonsingular point model \(T_g\) of its centre action. Existence follows from the compact-model construction in Measurable actions and compact models, Lemma 3.1 and Theorem 4.1, followed by STRICT Theorem 3.1. That theorem, applied to (ANC.5), supplies jointly measurable fibre isomorphisms

\[
 A(g,x):M_x\longrightarrow M_{T_gx},\qquad
 A(gh,x)=A(g,T_hx)A(h,x),
 \tag{ANC.6}
\]

at every arrow of an invariant conull model, representing

\[
 (\alpha_g a)(T_gx)=A(g,x)(a(x))
 \tag{ANC.7}
\]

almost everywhere for each fixed \(g\). Its proof uses the effective second countable quotient of the continuous algebra action, repairs dimension strata and standard-form data by Haar essential values, and then pulls back to the original group. It retains the original group labels, including the kernel. It does not assert that a separable locally compact group itself is second countable.

The **ancillary groupoid** is \(G\ltimes X=G\times X\), with source \(x\), range \(T_gx\), and multiplication

\[
 (g,T_hx)(h,x)=(gh,x).
 \tag{ANC.8}
\]

Its ancillary action is (ANC.6). Central ergodicity means that the fixed algebra in \(L^\infty(X)\) consists of scalars. It is the standing condition in the source definition, although the comparison in Section 2 does not require it. Nothing in (ANC.8) deletes stabilizer arrows.

## 2. Cocycle conjugacy with changing factor fields

Let \(\alpha\) act on \(M=\int_X M_x\,d\mu\) and \(\beta\) on \(N=\int_Y N_y\,d\nu\), with strict centre actions \(T,S\). Algebraic cocycle conjugacy consists of a normal isomorphism \(\Phi:M\to N\) and a continuous unitary \(\beta\)-cocycle \(u_g\in N\) satisfying

\[
 \Phi\alpha_g\Phi^{-1}=\operatorname{Ad}(u_g)\beta_g,\qquad
 u_{gh}=u_g\beta_g(u_h).
 \tag{ANC.9}
\]

The ancillary version consists of a measure-class Borel isomorphism \(F:X_0\to Y_0\) between invariant conull sets, a measurable field \(\theta_x:M_x\to N_{Fx}\), and measurable unitaries \(w(g,x)\in N_{F(T_gx)}\), such that, at every remaining arrow,

\[
 F(T_gx)=S_g(Fx),
 \tag{ANC.10}
\]


\[
 \theta_{T_gx}A(g,x)\theta_x^{-1}
 =\operatorname{Ad}(w(g,x))B(g,Fx),
 \tag{ANC.11}
\]


\[
 w(gh,x)=w(g,T_hx)\,
 B(g,F(T_hx))(w(h,x)).
 \tag{ANC.12}
\]

The group element is unchanged under the groupoid map \((g,x)\mapsto(g,Fx)\). An arbitrary orbit equivalence would be a different assertion.

**Comparison theorem.** Conditions (ANC.9) and (ANC.10)–(ANC.12) are equivalent, for the full variable factor fields and every separable locally compact \(G\).

To prove the forward direction, restrict \(\Phi\) to the centre. It gives a measure-class isomorphism \(F\) initially intertwining each fixed \(g\) almost everywhere. STRICT Lemma 1.1 repairs both \(F\) and its inverse to exact inverse equivariant maps on invariant conull sets. Its Haar repair is needed here: an uncountable intersection of conull sets would not suffice.

Put \(\rho=dF_*\mu/d\nu\). The coordinate unitary from the pulled-back standard field to the target Hilbert space has formula

\[
 (V_F\xi)(y)=\rho(y)^{1/2}\xi(F^{-1}y).
 \tag{ANC.13}
\]

Change of variables proves its norm identity and surjectivity; positive scalar multiplication preserves the cones and intertwines the conjugations. Remove this coordinate unitary from the canonical implementer of \(\Phi\). The remainder commutes with the central diagonal, so Uniqueness over the same diagonal structure decomposes it into fibre unitaries. Countable generator tests and the cone identity (ANC.5) make these the canonical implementers of \(\theta_x\). This is precisely VAR Theorem 1.1, whose standard-form hypothesis has now been constructed.

A first representative of \(u_g\), evaluated at \(F(T_gx)\), gives (ANC.11)–(ANC.12) only with exceptional sets depending on the parameters. Apply STRICT Theorem 4.1 to the actual unitary cocycle, then Theorem 5.1 to the canonical conjugating field. The former uses source-unitary path orbits and a closed-orbit Haar repair, retaining the original unitary class for every fixed \(g\). The latter repairs the canonical fibre implementers under the strict source and target actions and verifies algebra, conjugation and cone conditions on one invariant conull set. It yields (ANC.11)–(ANC.12) with the repaired \(\theta,w\). Scalar phases are retained: strictifying only \(\operatorname{Ad}(u_g)\) would not prove (ANC.12). These theorems have exactly the measurable standard-form input (ANC.5), with no constant-factor or freeness hypothesis.

Conversely, integrate \(\theta\) using its measurable canonical implementers and (ANC.13). This gives the normal isomorphism

\[
 (\Phi a)(Fx)=\theta_x(a(x)).
 \tag{ANC.14}
\]

Define the global unitary by its range coordinate,

\[
 u_g(y)=w(g,T_{g^{-1}}F^{-1}y).
 \tag{ANC.15}
\]

It is an essentially bounded measurable field of unitaries. Substituting \(x=T_{(gh)^{-1}}F^{-1}y\) in (ANC.12) gives \(u_{gh}=u_g\beta_g(u_h)\); substituting in (ANC.11) gives the first identity of (ANC.9). These substitutions explain why the range coordinate in (ANC.15) matters.

Finally \(g\mapsto u_g\) is Borel for the strong topology: its matrix coefficients against countable square-integrable fundamental sections are Borel by parameter integration. The boundedness by one and the same calculation for adjoints give the strong unitary Borel structure. The map \(g\mapsto(u_g,\beta_g)\) is a Borel homomorphism into the Polish semidirect product \(\mathcal U(N)\rtimes\operatorname{Aut}(N)\), so it is continuous by LOCAL Lemma 4.2. That lemma applies to every separable locally compact domain, not only second countable ones. Its proof takes a positive finite Haar-measure subset of a preimage of a small target neighborhood and uses continuity of \(L^1\) translation to show that its difference set contains an identity neighborhood. Thus (ANC.9) has the required continuity. This completes the reverse direction.

STRICT Proposition 6.1 and Corollary 6.2 compare any two strict choices through the identity global isomorphism. Transporting \(F,\theta,w\) by those comparisons shows that the result is independent of the chosen central decompositions and strict representatives. In particular it proves the ancillary criterion for centrally ergodic actions without narrowing their factor fields.

## 3. Splitting the full countable groupoid

Suppose now that \(G\) is countable discrete, and write

\[
 R=\{(T_gx,x):g\in G,\ x\in X\},\qquad
 H_x=\{g\in G:T_gx=x\}.
 \tag{ANC.16}
\]

Assume the measured principal relation \(R\) is hyperfinite. Work on its exact invariant conull exhaustion by finite relations. Apply the compatible lifting theorem 1. Lifting arrows with compatible finite choices to the endpoint map \(G\ltimes X\to R\). Equivalently, start with the first group label in a fixed enumeration that sends \(x\) to \(y\), and use the finite compatible construction there. It gives a Borel map \(c:R\to G\) with

\[
 T_{c(y,x)}x=y,\qquad
 c(z,y)c(y,x)=c(z,x),\qquad c(x,x)=e.
 \tag{ANC.17}
\]

Finite classes are included: compatibility, rather than an arbitrary choice of lifts around a cycle, enforces the last identity.

Conjugation by \(c(y,x)\) carries \(H_x\) onto \(H_y\). Define

\[
 \lambda_{y,x}(h)=c(y,x)h c(y,x)^{-1}.
 \tag{ANC.18}
\]

Equation (ANC.17) implies \(\lambda_{z,y}\lambda_{y,x}=\lambda_{z,x}\). On triples \((h,y,x)\), with \((y,x)\in R\) and \(h\in H_y\), put

\[
 (k,z,y)(h,y,x)=(k\lambda_{z,y}(h),z,x).
 \tag{ANC.19}
\]

Associativity follows by applying the preceding identity; the unit at \(x\) is \((e,x,x)\), and the inverse of \((h,y,x)\) is \((\lambda_{x,y}(h^{-1}),x,y)\). These are Borel operations since the group is countable and all displayed maps are Borel.

The required splitting is the explicit groupoid isomorphism

\[
 (g,x)\longmapsto
 (g c(T_gx,x)^{-1},T_gx,x).
 \tag{ANC.20}
\]

Its first entry fixes \(T_gx\), and the inverse is \((h,y,x)\mapsto(hc(y,x),x)\). For \(g=h c(y,x)\) and \(g'=k c(z,y)\), their product is

\[
 g'g=k\,[c(z,y)h c(z,y)^{-1}]c(z,x),
\]

which is exactly (ANC.19). Thus it preserves composition, units and inverses. It is bijective on each source and each range fibre, hence also preserves the counting-measure structures integrated over the unit measure. This proves the splitting of the full ancillary groupoid as the stabilizer field acted on by the principal relation.

The global kernel of the centre action is generally smaller than \(H_x\). For instance the permutation action of \(S_3\) on three equally weighted points has trivial global kernel but point stabilizers of order two. Replacing \(H_x\) by the global kernel would lose actual arrows.

Nor does (ANC.20) imply a splitting of a global group extension. Let \(\mathbb Z\) act transitively on \(\{0,1,2\}\) by addition modulo three. The group extension with kernel \(3\mathbb Z\) and quotient \(\mathbb Z/3\mathbb Z\) has no section homomorphism: an element of order three can only map to zero in the torsion-free group \(\mathbb Z\). Nevertheless \(c(j,i)=j-i\), for the representatives \(0,1,2\), satisfies (ANC.17), and the groupoid is the product of the three-point pair relation and the loop group \(3\mathbb Z\).

In particular the splitting applies to every countable amenable group action, because its principal measured orbit relation is hyperfinite by Invariant means on measured relations, Proposition 2.1, Lemma 5.1, Theorem 6.1 and Corollary 6.2. The complete mean-to-finite-relation proof is located there. This statement concerns the principal relation used as the base of the splitting; it does not identify isotropy with that relation.

## 4. Removing a noncommutative composition defect

Let \(P\) be Polish and \(H\) a Borel normal subgroup, which need not be closed. On a groupoid let \(A(\gamma)\in P\) be Borel, equal to one on units, and multiplicative modulo \(H\). Its uniquely determined defect is

\[
 u(\gamma_2,\gamma_1)
 =A(\gamma_2)A(\gamma_1)A(\gamma_2\gamma_1)^{-1}\in H.
 \tag{ANC.21}
\]

We call \(A\) a cross-homomorphism modulo \(H\). Associativity, applied to three composable arrows, proves the exact identity

\[
 u(\gamma_3,\gamma_2)u(\gamma_3\gamma_2,\gamma_1)
 =\operatorname{Ad}(A(\gamma_3))(u(\gamma_2,\gamma_1))
 \,u(\gamma_3,\gamma_2\gamma_1).
 \tag{ANC.22}
\]

For example both sides, after multiplication on the right by \(A(\gamma_3\gamma_2\gamma_1)\), equal \(A(\gamma_3)A(\gamma_2)A(\gamma_1)\).

For a normalized Borel cochain \(V(\gamma)\in H\), set \(B=VA\). Direct multiplication gives its defect:

\[
 u_B(\gamma_2,\gamma_1)
 =V(\gamma_2)\operatorname{Ad}(A(\gamma_2))(V(\gamma_1))
 \,u(\gamma_2,\gamma_1)V(\gamma_2\gamma_1)^{-1}.
 \tag{ANC.23}
\]

Consequently \(B\) is a homomorphism exactly when

\[
 u(\gamma_2,\gamma_1)
 =A(\gamma_2)V(\gamma_1)^{-1}A(\gamma_2)^{-1}
 \,V(\gamma_2)^{-1}V(\gamma_2\gamma_1).
 \tag{ANC.24}
\]

This is the precise use of the coboundary expression: it annihilates the existing defect while changing the implementing map from \(A\) to \(VA\). An arbitrary right side of (ANC.24) need not satisfy (ANC.22) for the unchanged \(A\). Section 8 gives a four-point counterexample. Thus one must keep the action and its noncommutative defect together.

**Defect-removal theorem.** A strict Borel cross-homomorphism on a hyperfinite countable principal measured relation can be changed by such a Borel \(H\)-valued cochain into a homomorphism on an invariant conull reduction. The same conclusion holds for a strict cross-homomorphism of a properly ergodic nonsingular real flow, on an all-time invariant conull model.

For the countable case form the standard Borel extension groupoid

\[
 \mathcal E=\{(y,b,x):(y,x)\in R,\ bA(y,x)^{-1}\in H\}.
 \tag{ANC.25}
\]

The condition is Borel even when \(H\) is not closed. Put \((z,c,y)(y,b,x)=(z,cb,x)\). Normality and (ANC.21) show closure: writing \(c=h_2A(z,y)\), \(b=h_1A(y,x)\), the product lies in \(HA(z,x)\). The inverse belongs to \(HA(x,y)\), by applying the same coset identity to the two inverse arrows. Units are \((x,1,x)\). Its endpoint groupoid is exactly \(R\). Apply CLR-01 to lift the identity of \(R\) to \(\mathcal E\). The middle coordinate of the lift is a Borel homomorphism \(B(y,x)\in HA(y,x)\). Then \(V=BA^{-1}\in H\), and (ANC.23) proves (ANC.24). This proof handles finite cycles and arbitrary Borel normal \(H\); it constructs no topological quotient \(P/H\).

For the flow case take the all-time suspension model proved in SUSP. Its base \((Z,S)\) is aperiodic and nonsingular, with a finite positive roof \(r\) bounded below. Write a point as \(x=(z,v)\), \(0\leq v<r(z)\), and put

\[
 \begin{gathered}
 R_0(z)=0,\qquad R_n(z)=\sum_{j=0}^{n-1}r(S^jz)\quad(n>0),\\
 R_{-n}(z)=-R_n(S^{-n}z)\quad(n>0).
 \end{gathered}
 \tag{ANC.26}
\]

For each \(t,x\) there is a unique integer \(n\) such that

\[
 T_t(z,v)=(S^nz,w),\qquad
 w=v+t-R_n(z),\quad 0\leq w<r(S^nz).
 \tag{ANC.27}
\]

The lower bound on the roof ensures the signed sums go to both infinities; the inequalities make the choice Borel.

Set \(d(z)=A(r(z),(z,0))\). Define \(b(S^nz,z)\) for positive \(n\) by the ordered product

\[
 b(S^nz,z)=d(S^{n-1}z)\cdots d(Sz)d(z),
 \tag{ANC.28}
\]

use one for \(n=0\), and use the inverse forward product for negative \(n\). Aperiodicity makes \(n\) unique. Cancellation of adjacent inverse factors proves the homomorphism identity on the base relation, including products with opposite signs. The strict coset law for \(A\), iterated along these return arrows, gives

\[
 b(S^nz,z)A(R_n(z),(z,0))^{-1}\in H.
 \tag{ANC.29}
\]

Now put \(a(z,v)=A(v,(z,0))\) and, with (ANC.27), define

\[
 B(t,(z,v))=a(S^nz,w)b(S^nz,z)a(z,v)^{-1}.
 \tag{ANC.30}
\]

In a composition the two vertical terms at the middle point cancel and the return products compose. Thus \(B\) is a strict homomorphism on the full flow groupoid. Decomposing a flow arrow into inverse vertical, return and final vertical arrows, and using (ANC.29), proves \(B(t,x)A(t,x)^{-1}\in H\). The Borel cochain \(V=BA^{-1}\) proves the claim. This is the return construction of RETURN Theorem 3.1, written with the multiplication order visible.

The strictness assumption in this argument is substantive. The section \(\{(z,0)\}\) has ambient measure zero. A fixed-time almost-everywhere quotient identity cannot simply be evaluated there, especially when \(H\) is not closed. In Section 5 we first strictify a genuine cocycle with a Polish target and obtain the required inner-valued correction after the return reduction. No strictification theorem for the possibly non-Polish quotient \(P/H\) is being used.

## 5. When only the centre action remains

Let \(N\) be a separable factor with

\[
 \overline{\operatorname{Int}(N)}=\operatorname{Aut}(N),\qquad
 M=L^\infty(X,\mu)\,\overline\otimes\,N.
 \tag{ANC.31}
\]

The topology on automorphisms is convergence on the predual, equivalently strong convergence of canonical standard implementers by Canonical implementation of automorphisms and The precise topology of a standard implementation. Let \(\alpha\) induce \(T\) on the centre, and let its simple lift be

\[
 (\beta_g a)(y)=a(T_{g^{-1}}y).
 \tag{ANC.32}
\]


**Centre-lifting theorem.** The action \(\alpha\) is cocycle conjugate to \(\beta\) in either of the following cases: the acting group is countable discrete, its centre action is free and its principal measured relation is hyperfinite; or the group is \(\mathbb R\) and its centre action is free and ergodic. In the discrete case ergodicity is not required. For two actions on this fixed constant-factor algebra satisfying the corresponding assumptions, cocycle conjugacy is equivalent to conjugacy of their centre actions.

We first recall why both correction stages have legitimate Borel targets. INNER Lemma 1.1 proves that \(\operatorname{Aut}(N)\) is Polish, \(\operatorname{Int}(N)\) is a Borel normal subgroup, and there is a Borel unitary implementer section \(s\) with \(s(\mathrm{id})=1\). Its explicit section fixes the scalar ambiguity by making the first nonzero matrix coefficient of a unitary positive real. On a factor any two implementers differ by a scalar, so this normalization is unique. The normalized set is Borel; the injective Borel image theorem applied to \(\operatorname{Ad}\) gives the Borel inner subgroup and the section. It need not be a closed subgroup.

In the discrete case, countability gives a common invariant conull strict factor action. Freeness gives exactly one group arrow for each endpoint pair, hence a Borel homomorphism \(b:R\to\operatorname{Aut}(N)\). Apply 3. The limiting cohomology theorem with \(P=\operatorname{Aut}(N)\), \(H=\operatorname{Int}(N)\), the identity cocycle and \(b\). Density in (ANC.31) gives a Borel \(f:X\to\operatorname{Aut}(N)\) and \(h:R\to\operatorname{Int}(N)\) such that

\[
 b(y,x)=h(y,x)f(y)f(x)^{-1}.
\]

Therefore the conjugated field action

\[
 c(y,x)=f(y)^{-1}b(y,x)f(x)
       =f(y)^{-1}h(y,x)f(y)
 \tag{ANC.33}
\]

is a homomorphism taking values in \(\operatorname{Int}(N)\). The map \(a(x)\mapsto f(x)^{-1}(a(x))\) is a normal algebra automorphism, by INNER Theorem 2.2 or by Section 1's measurable canonical integration.

Choose \(W(y,x)=s(c(y,x))\). The product \(W(z,y)W(y,x)W(z,x)^{-1}\) implements the identity, hence is scalar. Apply Section 4 with the Polish group \(\mathcal U(N)\), its normal scalar subgroup \(\mathbb T1\), and \(A=W\). The corrected map \(C:R\to\mathcal U(N)\) is a homomorphism and still implements \(c\). Thus

\[
 U_g(y)=C(y,T_{g^{-1}}y)
 \tag{ANC.34}
\]

is a \(\beta\)-cocycle, and the conjugated action is \(\operatorname{Ad}(U_g)\beta_g\). The first correction made automorphisms inner; the second removed the scalar obstruction to a unitary cocycle. Innerness alone would not have supplied (ANC.34).

For a properly ergodic real centre action, LOCAL Theorem 5.2 first supplies a strict jointly Borel \(\operatorname{Aut}(N)\)-valued action \(\Theta(t,x)\). Use SUSP and (ANC.26)–(ANC.27). This time the return products

\[
 b(S^nz,z)=\Theta(R_n(z),(z,0))
 \tag{ANC.35}
\]

already form a homomorphism. The aperiodic base relation is hyperfinite, as proved by the marker construction used in 4. Measurable flows and their return cocycles. Apply CLR-03 on that base to obtain \(f,h\) with \(b(y,z)=h(y,z)f(y)f(z)^{-1}\). Define

\[
 a(z,v)=\Theta(v,(z,0)),\qquad F(z,v)=a(z,v)f(z).
 \tag{ANC.36}
\]

The exact action law gives \(\Theta(t,x)=a(T_tx)b(y,z)a(x)^{-1}\), where \(x=(z,v)\) and \(T_tx=(y,w)\). Hence

\[
 \begin{aligned}
 F(T_tx)^{-1}\Theta(t,x)F(x)
 &=f(y)^{-1}b(y,z)f(z)\\
 &=f(y)^{-1}h(y,z)f(y)\in\operatorname{Int}(N).
 \end{aligned}
 \tag{ANC.37}
\]

for every arrow. This produces strict inner values by calculation, without taking limits inside a nonclosed subgroup. Apply the Borel implementer section and the flow case of Section 4 to its scalar defect. We obtain a strict unitary cocycle \(C(t,x)\) implementing (ANC.37). Then \(U_t(y)=C(t,T_{-t}y)\) is a global \(\beta\)-cocycle. Borel integration and LOCAL Lemma 4.2 give its strong continuity, as in Section 2. Integration of \(F^{-1}\) gives the required conjugating automorphism. This proves the properly ergodic case.

A free ergodic flow that is not properly ergodic has a conull transitive orbit. On that orbit choose \(x_0\). The orbit map \(t\mapsto T_tx_0\) is Borel and injective, hence has a Borel inverse \(t(x)\). Set \(F(x)=\Theta(t(x),x_0)\). The identity \(t(T_sx)=s+t(x)\) gives

\[
 F(T_sx)^{-1}\Theta(s,x)F(x)=\mathrm{id}.
 \tag{ANC.38}
\]

Here no inner-density assumption is needed and the correcting unitary is one. This is also the transitive argument in RETURN Theorem 4.1. Together the two cases cover the free ergodic real action.

Finally an inner perturbation acts trivially on the centre, so cocycle conjugacy necessarily gives a conjugacy of centre actions. Conversely a measure-class conjugacy of centres integrates to a conjugacy between their simple lifts on the same factor \(N\). Apply the theorem to both actions and compose. To verify the cocycles compose, if \(\gamma_g=\operatorname{Ad}(u_g)\beta_g\) and \(v\) is a \(\gamma\)-cocycle, then

\[
 v_{gh}u_{gh}
 =v_g\gamma_g(v_h)u_g\beta_g(u_h)
 =v_gu_g\beta_g(v_hu_h).
 \tag{ANC.39}
\]

For inversion, \(u_g^*\gamma_g(u_h^*)=\beta_g(u_h^*)u_g^*=u_{gh}^*\). Transport through the algebra conjugacies preserves these identities. This proves the classification assertion. The uncountable real transformation groupoid has not been called an orbitally discrete AF groupoid; its countable return relation is the object to which hyperfinite reduction was applied.

## 6. Transporting an arbitrary semifinite weight

Let \(\Phi:M\to N\) be any normal isomorphism and let \(\varphi\) be a normal semifinite faithful weight on \(M\). Define

\[
 \psi(b)=\varphi(\Phi^{-1}(b)),\qquad b\in N_+.
 \tag{ANC.40}
\]

This equality is on the entire positive cone and allows infinity. Normality, faithfulness and semifiniteness pass through \(\Phi\), as proved in The weight and every finite domain. In particular

\[
 \mathfrak n_\psi=\Phi(\mathfrak n_\varphi),\qquad
 \mathfrak n_\psi\cap\mathfrak n_\psi^*
 =\Phi(\mathfrak n_\varphi\cap\mathfrak n_\varphi^*).
 \tag{ANC.41}
\]

The exact GNS transport of GNS transport and the square-root scalar through Composition, with all arrows visible, here with scalar one, is

\[
 V\Lambda_\varphi(a)=\Lambda_\psi(\Phi(a)).
 \tag{ANC.42}
\]

Equality of the squared norms is (ANC.40) applied to \(\Phi(a^*a)\); (ANC.41) gives dense range, so \(V\) extends to a unitary.

Let \(S_{\varphi,0}\) denote the Tomita involution on the finite star domain. Since \(\Phi\) preserves adjoints, (ANC.42) gives \(VS_{\varphi,0}=S_{\psi,0}V\) on its entire domain, with onto correspondence of domains. A unitary homeomorphism of the two graph spaces commutes with taking closures. Therefore

\[
 VS_\varphi V^*=S_\psi,\qquad
 VJ_\varphi V^*=J_\psi,\qquad
 V\Delta_\varphi V^*=\Delta_\psi.
 \tag{ANC.43}
\]

The second and third equalities follow from uniqueness of polar decomposition of the closed involutions. For every complex \(z\), spectral calculus then gives

\[
 V\mathcal D(\Delta_\varphi^z)=\mathcal D(\Delta_\psi^z),\qquad
 V\Delta_\varphi^z\xi=\Delta_\psi^zV\xi.
 \tag{ANC.44}
\]

Precisely, the domain condition is \(\int_{(0,\infty)}\lambda^{2\operatorname{Re}z}\,d\|E_\varphi(\lambda)\xi\|^2<\infty\); (ANC.43) transports the spectral projections. Both modular operators are injective. Formula (ANC.44) includes unbounded positive and negative real powers, not just the bounded modular unitaries. In particular

\[
 \sigma_t^\psi\Phi=\Phi\sigma_t^\varphi.
 \tag{ANC.45}
\]

There is no assumption that \(\varphi(1)\) is finite, and no use of \(\Lambda_\varphi(1)\) in this argument.

Apply this to (ANC.9). Put \(\varphi_g=\varphi\circ\alpha_g^{-1}\), \(\psi=\varphi\circ\Phi^{-1}\), and \(\psi_g=\varphi_g\circ\Phi^{-1}\). Inverting the first identity of (ANC.9) gives the exact order

\[
 \psi_g=(\psi\circ\beta_g^{-1})\circ\operatorname{Ad}(u_g^*).
 \tag{ANC.46}
\]

Thus each transported weight has the full modular description (ANC.41)–(ANC.45). A group-action unitary cocycle \(u_g\) has not thereby been identified with a Connes cocycle for a pair of weights. Nor does (ANC.46) assert that any of these weights is invariant under the original action.

## 7. Measure factors and complete modular domains

Suppose \(\Phi\) has the field description (ANC.14), and disintegrate an arbitrary normal semifinite faithful weight as

\[
 \varphi(a)=\int_X\varphi_x(a(x))\,d\mu(x).
\]

The disintegration and its all-positive integral formula are Central disintegration of a separable weighted algebra. With \(\rho=dF_*\mu/d\nu\), define on the target factor

\[
 \psi_y(b)=\rho(y)\,
 \varphi_{F^{-1}y}\bigl(\theta_{F^{-1}y}^{-1}(b)\bigr).
 \tag{ANC.47}
\]

This is a measurable field of normal semifinite faithful weights: measurable positive operator fields pull back through the measurable isomorphisms, the original field has measurable weight values by A countable contractive family detects every positive value, and multiplication by the finite positive Borel function \(\rho\) preserves these properties. The density is finite and positive almost everywhere for equivalent sigma-finite measures.

Change of variables for nonnegative measurable functions proves, including infinite values,

\[
 \int_Y\psi_y(b(y))\,d\nu(y)
 =\int_X\varphi_x(\theta_x^{-1}(b(Fx)))\,d\mu(x)
 =\psi(b).
 \tag{ANC.48}
\]

In particular the global finite left ideal consists exactly of bounded fields for which the integral of \(\psi_y(b(y)^*b(y))\) is finite. Its elements need not have a uniform bound on the fibre weight values.

The normalized fibre GNS unitary is

\[
 V_x\Lambda_{\varphi_x}(a)
 =\rho(Fx)^{-1/2}\Lambda_{\psi_{Fx}}(\theta_x(a)).
 \tag{ANC.49}
\]

The norm identity follows from (ANC.47), and finite ideals correspond because the scalar is positive and finite. The canonical measurable implementation from Section 1, or the measurable GNS vector construction MW-03 on a countable fundamental family, makes \(V_x\) measurable. The integrated GNS unitary is

\[
 (\mathcal V\xi)(y)
 =\rho(y)^{1/2}V_{F^{-1}y}\xi(F^{-1}y).
 \tag{ANC.50}
\]

Its norm is preserved by change of variables. On a global GNS vector the two scalar factors in (ANC.49)–(ANC.50) cancel, giving (ANC.42). Thus it is the same unitary, not a different identification chosen after the fact.

Multiplying a weight by a positive scalar changes the GNS norm but not the transported closed Tomita operator: the normalized map in (ANC.49) carries the finite star graph onto the other finite star graph, and the scalar is real. Apply the graph argument of Section 6 fibrewise. For every complex \(z\),

\[
 V_x\Delta_{\varphi_x}^{z}V_x^*
 =\Delta_{\psi_{Fx}}^{z}
 \tag{ANC.51}
\]

with equality of domains. Combining the full direct-integral description in MW-04 with change of variables yields

\[
 \begin{split}
 &\int_Y
 \|\Delta_{\psi_y}^{z}(\mathcal V\xi)(y)\|^2\,d\nu(y)\\
 &\hspace{1em}=\int_X
 \|\Delta_{\varphi_x}^{z}\xi(x)\|^2\,d\mu(x).
 \end{split}
 \tag{ANC.52}
\]

Both sides are extended nonnegative integrals, with the condition that the vector belongs to the respective fibre domain almost everywhere. This proves the maximal-domain correspondence under base change, including unbounded powers. Fibre membership by itself is insufficient; Section 8 exhibits a vector whose fibre domains are all valid but whose global integral diverges.

For the simple lift (ANC.32) and product weight \(\psi=\mu\otimes\omega\), the earlier formula (ANC.46) becomes especially concrete. Write \(r_g=d(T_g)_*\mu/d\mu\). Then

\[
 \psi_g(a)=\int_X r_g(y)\,
 \omega\bigl(u_g(y)^*a(y)u_g(y)\bigr)\,d\mu(y),
 \qquad a\geq0.
 \tag{ANC.53}
\]

Indeed \((\beta_g^{-1}a)(x)=a(T_gx)\), so its integration pushes \(\mu\) forward by \(T_g\), with this direction of the derivative. Then apply the inner conjugation in (ANC.46). Formula (ANC.53) separates the base-measure change from the fibre weight change; neither can be omitted.

There is a corresponding distinction between the unitary cocycle and its standard implementer. In any standard form \((N,H,J,P)\), the canonical unitary for \(\operatorname{Ad}(u)\) is

\[
 I(u)=uJuJ.
 \tag{ANC.54}
\]

The two factors belong to the commuting algebras \(N\) and \(N'\). This unitary implements \(\operatorname{Ad}(u)\), commutes with \(J\), and preserves \(P\) in both directions by the standard-form cone axiom applied to \(u\) and \(u^*\). Uniqueness in SE-10 proves (ANC.54). If \(K_g\) canonically implements \(\beta_g\), then

\[
 I(u_g)K_g
 \tag{ANC.55}
\]

canonically implements \(\operatorname{Ad}(u_g)\beta_g\), and

\[
 [I(u_g)K_g][I(u_h)K_h]
 =I(u_g\beta_g(u_h))K_{gh}
 =I(u_{gh})K_{gh}.
 \tag{ANC.56}
\]

Here \(K_gJK_g^*=J\) and \(K_g aK_g^*=\beta_g(a)\) justify moving the two left and right factors. But \(I(\zeta u)=I(u)\) for every scalar \(\zeta\) of modulus one. Canonical standard implementers therefore lose the scalar phase of a unitary cocycle. This is why the unitary correction in Section 5 and the exact unitary strictification in Section 2 cannot be replaced by their automorphism-level versions.

## 8. Examples that test the hypotheses and domains

**The unchanged-action coboundary test.** Take the pair groupoid on \(\{0,1,2,3\}\), let \(P=H=S_3\), and put \(A=1\). Let \(a=(12)\), \(b=(23)\). Choose a normalized cochain with \(V(2,1)=a\), \(V(1,0)=b\), and all other values one. Denote the right side of (ANC.24) by

\[
 D(z,y,x)=V(y,x)^{-1}V(z,y)^{-1}V(z,x).
\]

Then

\[
 \begin{gathered}
 D(3,2,1)=a^{-1},\qquad D(3,1,0)=b^{-1},\\
 D(2,1,0)=b^{-1}a^{-1},\qquad D(3,2,0)=1.
 \end{gathered}
 \tag{ANC.57}
\]

For the unchanged action \(A=1\), (ANC.22) would require \(a^{-1}b^{-1}=b^{-1}a^{-1}\), which is false in \(S_3\): the two products are opposite three-cycles. Thus an arbitrary \(D\) is not the asserted two-cocycle for this fixed action. There is no contradiction with defect removal. That theorem starts with the actual defect \(u_A\), and produces a particular \(V\) for which \(u_A=D\), equivalently \(u_{VA}=1\). Formula (ANC.23) is valid for every cochain.

**An isotropy obstruction to unitary lifting.** Let

\[
 X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

On \(M_2(\mathbb C)\), the automorphisms \(\operatorname{Ad}(X)\) and \(\operatorname{Ad}(Z)\) commute and square to the identity, since \(XZ=-ZX\). They define an action of \((\mathbb Z/2\mathbb Z)^2\) on the one-point centre. Any implementer of \(\operatorname{Ad}(X)\) is a scalar multiple of \(X\): its quotient with \(X\) commutes with every matrix, and commutation with the matrix units forces that quotient to be scalar. The same holds for \(Z\). Such two implementers still anticommute and cannot be the commuting images of the two generators under a unitary representation. Every fibre automorphism here is inner, but there is no homomorphic unitary lift. The free-centre hypothesis in Section 5 excludes exactly this kind of isotropy obstruction to its argument.

**Finite fibres and an unbounded global modular operator.** On

\[
 M=L^\infty((0,1),dx)\,\overline\otimes\,M_2(\mathbb C),
 \qquad D_x=\operatorname{diag}(x,1),
\]

use the faithful normal finite weight

\[
 \varphi(a)=\int_0^1\operatorname{Tr}(D_xa(x))\,dx.
 \tag{ANC.58}
\]

Identify each GNS fibre with the Hilbert–Schmidt matrices by \(\Lambda_x(a)=aD_x^{1/2}\). Matrix multiplication gives

\[
 J_x\xi=\xi^*,\qquad
 \Delta_x\xi=D_x\xi D_x^{-1},\qquad
 S_x\xi=D_x^{-1/2}\xi^*D_x^{1/2}.
 \tag{ANC.59}
\]

The last identity is checked on \(aD_x^{1/2}\), where it becomes \(a^*D_x^{1/2}\). All domains in an individual fibre are the full four-dimensional space. Globally, however, the closure has the domain given by the square integral of this formula. One can verify fullness directly: first cut to \(x\geq1/n\), then bound all matrix coefficients; the resulting bounded fields lie in the finite star domain, and these cutoffs converge in the graph norm whenever its stated integral is finite.

For the constant vector field \(\xi(x)=E_{21}\), one has \(\|\xi\|^2=1\) but

\[
 \Delta_x^{1/2}E_{21}=x^{-1/2}E_{21},\qquad
 \int_0^1\|\Delta_x^{1/2}\xi(x)\|^2\,dx
 =\int_0^1\frac{dx}{x}=\infty.
 \tag{ANC.60}
\]

Thus \(\xi\notin\mathcal D(\Delta_\varphi^{1/2})\), despite belonging to every fibre domain. The cutoffs \(\xi_n=\mathbf1_{[1/n,1)}E_{21}\) have squared modular graph contribution \(\log n\), which diverges.

Now change the base measure to \(d\nu=dx/x\) while representing the same algebra and weight. Here \(F\) is the identity and \(\rho=d\mu/d\nu=x\). Formula (ANC.47) gives fibre density \(D'_x=xD_x=\operatorname{diag}(x^2,x)\). Its modular ratios are the same as those of \(D_x\). In the Hilbert–Schmidt identifications (ANC.49) is the identity, while (ANC.50) is multiplication by \(\sqrt{x}\). Its norm satisfies

\[
 \int_0^1\|\sqrt{x}\,\xi(x)\|^2\,\frac{dx}{x}
 =\int_0^1\|\xi(x)\|^2\,dx.
 \tag{ANC.61}
\]

The corresponding modular integral for \(\sqrt{x}E_{21}\) is still \(\int_0^1dx/x\). This checks both the direction of the Radon–Nikodym factor and the full-domain assertion (ANC.52).

**Reading the comparison correctly.** The splitting in Section 3 preserves loop groups; the reduction in Section 5 needs a free centre action; and (ANC.54) forgets scalar phases. These are three separate facts. The three-point \(\mathbb Z\)-action in Section 3, the Pauli example above and the four-point calculation (ANC.57) show why none can be substituted for another.

## References

M. Takesaki, *Theory of Operator Algebras III*, Chapter XIII, Section 3, Definition 3.30, Propositions 3.31–3.32, Remark 3.33, Proposition 3.34 and Corollary 3.35, printed pages 53–56, are the mathematical antecedents for Sections 1–5. The formulation of the noncommutative coboundary is qualified by the explicit defect-change identity (ANC.23) and counterexample (ANC.57). The source's real-flow assertion is implemented through a countable return relation and includes the separate transitive free case.

The programme proofs linked above supply the central decomposition, standard form, strictification, suspension and cohomology inputs. Sections 6–8 derive the weight and full modular-domain transport from those constructions and the earlier weight-transport lessons.
