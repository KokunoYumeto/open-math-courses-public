# Countable cores, multiplier domains and measurable choices

A countable algebra core can recover products, closed multiplier graphs and the generated von Neumann algebra. It does not determine membership in every original, possibly nonfull fibre algebra. This lesson supplies the mechanisms used in assembling the integral Hilbert algebra, then separates full-completion membership, selection of a proper defect, and measurable implementation of fibre isomorphisms.

Read the rational star-core and dense-product proofs first. Localize products before using them in the integral. Read the multiplier-core proof with the construction of the opposite field. The completed-measure selector, full-completion code and qualified fullness argument follow. The constant-graph example is a diagnostic at that boundary. The CH construction is a separate conditional investigation.

Use inner products linear in the first variable, separable fibres and a standard sigma-finite base with measure completion. The Hilbert-field coordinates, measurable graph and polar operators, single-fibre right algebra, full completion, bounded strong-star approximation, and compact weak operator balls are the inputs. Approximation is applied to a new rational core only after it is proved to be a left Hilbert algebra. The selection proof uses finite-Borel-measure tightness on Polish spaces; it proves analytic measurability and selection after completion.

## Generate a measurable rational star core

Begin with the exact graph-dense set in the field definition. Its rational star closure gives countably many measurable products and operators; it is not asserted equal to the original algebra.

Let \(a_j(\gamma)\) be the DI-00 fundamental family. Enumerate all finite words in the \(a_j\) and \(a_j^\sharp\), and all finite \(\mathbb Q(i)\)-linear combinations of those words, including zero. Denote this countable family by \(b_j(\gamma)\). It is closed under its rational algebra operations and involution. Let \(\mathcal B_\gamma\) be its complex linear span inside \(\mathcal A_\gamma\).

For each original \(a_j\), the vectors \(L_{a_j}a_k=a_ja_k\) are measurable. The \(a_k\) are Hilbert-fundamental, and \(L_{a_j}\) is bounded in each fibre. Its matrix coefficients, and hence its action on every measurable vector, are measurable by DF-03; there is no assertion of an essential bound on its norm. Its adjoint is \(L_{a_j^\sharp}\), so that operator field is measurable too. Induction on word length now makes every \(b_j\), \(b_j^\sharp\), \(L_{b_j}\) and product \(b_jb_k\) measurable.

Finite complex coefficients can be approximated by rational complex coefficients in both vector and involution norm. Thus the countable family itself, not just its complex span, is dense in the closed involution graph:

\[
 \overline{\{(b_j(\gamma),S_\gamma b_j(\gamma)):j\geq1\}}
   =G(S_\gamma)
 \quad\text{in the graph topology on }D(S_\gamma).
 \tag{SCF.1}
\]

Here the closure is taken after identifying the first coordinate with the domain vector; the antilinear graph can equivalently be linearized in \(\overline H_\gamma\oplus H_\gamma\). The equality follows because the original core is a core for its own graph closure. It does not identify the original algebra with that closed domain or with its full completion.

All countably many algebra identities, measurable representatives and null-set exceptions can be fixed on one common conull set. Operations on the zero fibre give zero. No uncountable family of membership statements is being placed on a common conull set.

## Prove product density before completing the core

The new core must have dense products before the Hilbert-algebra approximation theorem can be applied to it. The opposite algebra gives the required test vectors.

Fix one fibre and suppress its parameter. The first three left Hilbert algebra axioms pass from \(\mathcal A\) to \(\mathcal B\). We prove the fourth.

Suppose \(\eta\perp\mathcal B^2\). Since \(\mathcal B\) is Hilbert-dense, \(\langle L_b^*\eta,c\rangle=0\) for all \(b,c\in\mathcal B\) implies \(L_b^*\eta=0\). Star closure gives \(L_b\eta=0\) for every \(b\in\mathcal B\). For arbitrary \(a\in\mathcal A\), choose \(b_n\in\mathcal B\) with \(b_n\to a\) and \(b_n^\sharp\to a^\sharp\). For every \(r\in\mathcal A_r\), right boundedness and the adjoint identity give

\[
 0=\langle L_{b_n}\eta,r\rangle
   =\langle\eta,R_r b_n^\sharp\rangle
   \longrightarrow\langle\eta,R_r a^\sharp\rangle
   =\langle L_a\eta,r\rangle .
 \tag{SCF.2}
\]

The right algebra is Hilbert-dense by RD-04. Hence \(L_a\eta=0\) for every \(a\in\mathcal A\), and the dense-product axiom for \(\mathcal A\) forces \(\eta=0\). Thus \(\mathcal B^2\) is dense. In particular \(\mathcal B\) is a left Hilbert algebra, with the same closed involution \(S\) and the same \(F=S^*\).

We also identify the associated right algebra exactly. Restricting a right-bounded operator for \(\mathcal A\) to \(\mathcal B\) gives one inclusion. Conversely let \(\eta\in\mathcal B_r\), with bounded operator \(Q\) satisfying \(Qb=L_b\eta\) on \(\mathcal B\), and \(\eta\in D(F)\). For \(a,b_n,r\) as above,

\[
 \langle Qb_n,r\rangle
 =\langle\eta,R_r b_n^\sharp\rangle
 \longrightarrow\langle\eta,R_r a^\sharp\rangle
 =\langle L_a\eta,r\rangle .
 \tag{SCF.3}
\]

The first expression also tends to \(\langle Qa,r\rangle\). Density gives \(Qa=L_a\eta\) for every \(a\in\mathcal A\). Thus the right algebras, their right operators and their involution are identical.

RD-05 identifies the von Neumann algebra generated by these right operators with the commutant of each left algebra. Taking commutants, and then using WH-03–04 for two-step dualization, gives

\[
 L(\mathcal B)''=L(\mathcal A)'',\qquad
 \mathcal B_r=\mathcal A_r,\qquad
 \mathcal B_{rr}=\mathcal A_{rr}.
 \tag{SCF.4}
\]

These are equalities of the actual subspaces and represented operators on the same Hilbert space. They do not say that \(\mathcal B=\mathcal A\) or that either original algebra was full.

## Localize explicit products and operator generators

The dense products now have explicitly known factors. Bound both factors at once on finite-measure sets. These are the actual vectors used in graph assembly and algebra generation, not witnesses promised by a selection theorem.

Enumerate all pairs \((b_i,b_j)\). Their products are measurable by SCF-01, and their complex span is \(\mathcal B^2\), hence dense by SCF-02. These pairs are therefore an explicit measurable product-fundamental family. No selection of a point in an unspecified relation is necessary.

The measurable operator family \(L_{b_j}\) generates \(L(\mathcal A_\gamma)''\) by (SCF.4): passing from the rational family to its complex span changes no operator commutant. On a sigma-finite base, choose finite-measure sets \(E_m\uparrow\Gamma\). For each \(j\) define

\[
 E_{j,m}=
 E_m\cap\{\|b_j\|,\|b_j^\sharp\|,\|L_{b_j}\|\leq m\},
 \qquad d_{j,m}=1_{E_{j,m}}b_j .
 \tag{SCF.10}
\]

The norms are measurable, the sets increase to the base up to the fixed null set, and every \(d_{j,m}\) belongs to the original integral algebra. The operator norm need not have been bounded on the entire base.

For products, intersect the two factors' six level bounds and the same finite-measure exhaustion. Each localized factor belongs to the integral algebra and its product is the corresponding scalar localization of \(b_ib_j\). Orthogonality to all these products, followed by further bounded scalar localization, gives fibrewise orthogonality to their countable fundamental family. Thus the global product span is dense. The localized \(d_{j,m}\) supply the generator family used by DI-09. This proves both of those original constructions, at the full original fibre generality of DI-00.

## Keep a closed multiplier domain under approximation

A second graph enters: multiplication by a fixed right-domain vector. Its domain is not controlled by involution graph density alone. The following proof gives bounded strong-star approximants and controls their rationalization error.

Let \(\eta(\gamma)\in D(F_\gamma)\) be a measurable field, with measurable \(F_\gamma\eta(\gamma)\). In one fibre let

\[
 T_\eta=\overline{\,a\mapsto L_a\eta:\ a\in\mathcal A\,}.
 \tag{SCF.5}
\]

The single-fibre existence and affiliation assertions are HA-07 and RD-01. We claim that the graph is already the closure of the countable pairs

\[
 (b_j,L_{b_j}\eta),\qquad j\geq1.
 \tag{SCF.6}
\]

Indeed \(a\in\mathcal A\subseteq\mathcal A_{rr}=\mathcal B_{rr}\). HAP-06, now applied to the established Hilbert algebra \(\mathcal B\), supplies \(c_n\in\mathcal B\) with

\[
 c_n\to a,\qquad c_n^\sharp\to a^\sharp,\qquad
 \|L_{c_n}\|\leq\|L_a\|,\qquad L_{c_n}\to L_a
 \text{ strongly*}.
 \tag{SCF.7}
\]

Consequently \(L_{c_n}\eta\to L_a\eta\). Each \(c_n\) is a finite complex combination of the countable words. Approximate those finitely many coefficients by \(\mathbb Q(i)\) so closely that both vector errors, and the multiplier operator-norm error, are less than \(1/n\). This gives a member of the enumerated rational family with the same two graph limits in (SCF.6). Its multiplier norm is at most \(\|L_a\|+1/n\), which is sufficient here; we do not falsely retain the exact norm bound after rational approximation.

Every initial graph pair in (SCF.5) is therefore in the closure of (SCF.6); the reverse inclusion is immediate. Closing proves the claim. All vectors in (SCF.6) are measurable by SCF-01. Their closed linear span is the graph field of \(T_{\eta(\gamma)}\), by DF-04 or DI-01. Hence the closed right multiplier field is measurable, including its full domain.

For a countable graph-fundamental family \(\eta_k\) of \(F_\gamma\), the same \(b_j\) works for every \(k\). Polar fields and spectral cutoffs are then measurable by DI-01. Applying RD-03–04 to each \(T_{\eta_k}\) gives the countable right graph core and its measurable right operators used in DI-05. This establishes that consumer without a proper-original-algebra selector.

Graph density alone would not justify replacing (SCF.7) by an arbitrary graph approximation. In the trace algebra \(L^\infty(0,1)\subset L^2(0,1)\), take

\[
 a_n(t)=n\,1_{(0,n^{-3})}(t),\qquad \eta(t)=t^{-1/3}.
 \tag{SCF.8}
\]

The closed involution is conjugation, whereas the closed right multiplier is multiplication by \(\eta\). Exact integration gives

\[
 \|a_n\|_S^2=\frac2n\longrightarrow0,\qquad
 \|L_{a_n}\|=n,\qquad
 \|T_\eta a_n\|_2^2=3n .
 \tag{SCF.9}
\]

The image vectors diverge in norm. The bounded strong approximation in (SCF.7) is the required extra argument.

### Extend a right-core identity by weak pairings

One mechanism will also be used in the full-completion and unitary tests. Suppose a fixed vector \(x\) and bounded operator \(B\) satisfy \(R_rx=Br\) on a right graph core. For arbitrary right-algebra \(r\), choose core \(r_n\) with \(r_n\to r\) and \(Fr_n\to Fr\). For any original left-algebra test vector \(c\),

\[
 \begin{aligned}
 \langle R_{r_n}x,c\rangle
   &=\langle x,L_cFr_n\rangle,\\
 \langle x,L_cFr_n\rangle
   &\longrightarrow\langle x,L_cFr\rangle,\\
 \langle x,L_cFr\rangle
   &=\langle R_rx,c\rangle .
 \end{aligned}
 \tag{SCF.M1}
\]

On the core the first line is \(\langle Br_n,c\rangle\), which tends to \(\langle Br,c\rangle\). Density of the test vectors gives \(R_rx=Br\). Every \(R_r\) is already defined and bounded because \(r\) is in the right algebra. No uniform bound on the approximating \(R_{r_n}\) is needed: the limit is taken in the pairing involving the fixed bounded \(L_c\). This is the domain extension used by the later compact code and unitary tests.

### Diagnose the failed graph argument

**Problem 2.** Why does the decreasing first quantity in (SCF.9) not make (SCF.6) a graph core without the HAP approximation?

**Solution.** The sequence is a core approximation of the zero vector for the closed involution, but its image under the fixed closed multiplier has squared norm \(3n\). It does not converge to that multiplier's image of zero. The proof of SCF-03 instead approximates each fixed \(a\) with uniform multiplier bounds and strong convergence on the particular \(\eta\). Rational approximation then has an explicitly controlled operator-norm error. Hilbert graph density and a graph core for this second closed operator are distinct requirements.

## Choose a witness after completing the measure

The explicit core constructions above required no abstract choice. To select an isomorphism or a proper defect we must first code a relation, then select in the completed measure. Projection of a Borel relation need not be Borel.

We give the measure-theoretic selection argument explicitly. A standard Borel base may be realized as a Borel subset of a Polish space; extend its measure by zero outside that subset. Replace the sigma-finite measure by an equivalent finite one: on a disjoint Borel finite-measure exhaustion use positive densities \(2^{-m}/(1+\mu(E_m))\). The resulting measure has the same null sets and the same completed Borel sigma-field. Finite Borel measure tightness is the named scalar input.

First, every Borel subset \(B\) of a Polish space \(Z\) is the projection of a closed subset of \(Z\times\mathbb N^{\mathbb N}\). Here are the coding steps. A closed set has a constant witness. An open set is a countable union of closed distance level sets. Closed-projection codes are closed under countable union by using the first witness coordinate as the chosen index; a convergent sequence of witnesses eventually has the same first coordinate. They are closed under countable intersection by interleaving countably many witnesses and imposing all their closed conditions. The class of sets whose set and complement both have such codes is a sigma-field containing all open sets. It therefore contains every Borel set.

Every nonempty Polish space \(P\) is a continuous image of a closed subset of \(\mathbb N^{\mathbb N}\). To see this, cover it by countably many closed balls of successively smaller radii, intersect each child with its parent, and discard empty children. At depth \(n\) require diameter at most \(2^{-n}\). The valid infinite paths form a closed set of codes. Nested nonempty closed cells of shrinking diameter in a complete metric have exactly one common limit point. This limit depends continuously on the code and every point has a path. These two constructions reduce projections with any Polish witness space to projections with a Baire-space witness.

Now let \(C\subseteq X\times\mathbb N^{\mathbb N}\) be closed and \(A=p_X(C)\). We prove that \(A\) is measurable in the completion of any finite Borel measure. By tightness choose increasing compact sets \(X_m\) with complement measures tending to zero. It suffices to work on one compact \(X_m\).

Compactify each discrete coordinate by one point, and set \(K=(\mathbb N\cup\{\infty\})^{\mathbb N}\). In the compact metric space \(X_m\times K\), the closed code \(C_m=C\cap(X_m\times\mathbb N^{\mathbb N})\) is a \(G_\delta\) subset of its compact closure \(D\). Indeed the Baire-coordinate subspace is the intersection of the open conditions that each coordinate is different from \(\infty\), and relative closedness gives \(C_m=D\cap(X_m\times\mathbb N^{\mathbb N})\). Write \(C_m=\bigcap_n U_n\), with \(U_n\) relatively open in \(D\), and exhaust each \(U_n\) by increasing compact sets \(K_{n,k}\).

We need continuity from below for the outer measure of arbitrary increasing subsets. For \(A_k\uparrow A\), choose measurable hulls \(H_k\supseteq A_k\) of exact outer measure. The sets \(D_k=\bigcap_{\ell\geq k}H_\ell\) contain \(A_k\), increase with \(k\), and satisfy \(\mu(D_k)\leq\mu(H_k)=\mu^*(A_k)\). Therefore \(\mu^*(A)\leq\mu(\bigcup_kD_k)\leq\lim_k\mu^*(A_k)\); the reverse inequality is automatic. This justifies the outer-measure continuity used next.

Fix \(0<\alpha<\mu^*(p_X(C_m))\). Starting with \(C_m\), choose \(k_n\) inductively so that

\[
 \mu^*\!\left(p_X\!\left(C_m\cap
       \bigcap_{i=1}^n K_{i,k_i}\right)\right)>\alpha .
 \tag{SCF.11}
\]

The previous set lies in \(U_n=\bigcup_kK_{n,k}\), so the choice follows from the proved continuity from below. The compact sets \(Q_n=\bigcap_{i=1}^nK_{i,k_i}\) decrease. Their intersection \(Q\) lies in \(C_m\). Compactness gives \(p_X(Q)=\bigcap_np_X(Q_n)\): for a point in every projected set, its nested compact fibres have a common point. Continuity from above of finite measure now yields \(\mu(p_X(Q))\geq\alpha\).

Thus the outer measure of \(p_X(C_m)\) is its supremum over compact subsets. A countable sequence of such compact subsets, together with a measurable hull of exact outer measure, shows that \(p_X(C_m)\) differs from a Borel subset by a subset of a null set. It is completed-measurable. The compact exhaustion of \(X\) proves the same for \(A\). This proves the analytic measurability needed here, rather than treating a projection of a Borel set as automatically Borel.

Finally let \(R\subseteq X\times Y\) be Borel, where \(Y\) is Polish, and let \(D=p_X(R)\). Use the closed code \(C\subseteq X\times(Y\times\mathbb N^{\mathbb N})\) supplied above, and equip the witness space with a complete metric. Cover it by a fixed countable tree of nested closed cells with diameters at most \(2^{-n}\). For each cell \(K_s\), the hitting set

\[
 D_s=\{x:C_x\cap K_s\ne\varnothing\}
 \tag{SCF.12}
\]

is analytic and hence completed-measurable. For \(x\in D\), choose successively the least indexed child whose hitting set contains \(x\). The chosen finite prefix is a completed-measurable countable-valued function at every stage. Fixed representatives of its cells form a measurable Cauchy sequence. At depth \(n\), take a point of \(C_x\) in the chosen cell; its distance from the fixed representative is at most \(2^{-n}\). These witness points have the same limit, which lies in \(C_x\) by closedness. Its \(Y\)-coordinate is a completed-measurable map \(v\) with

\[
 (x,v(x))\in R\qquad(x\in D).
 \tag{SCF.13}
\]

For an analytic relation use one additional closed witness and project the chosen point; the same proof applies. Countable rational matrix tests can therefore be selected after coding. There is no general Borel-selector assertion. A completed-measurable map into a Polish space has a Borel representative off one measure-null set: replace the countably many simple-function approximants by Borel ones and pass to their pointwise limit on the common conull set.

## Code exactly the full completion

The canonical full completion does have a measurable membership code. Test an involution vector and a bounded multiplier in compact weak balls. The weak-pairing extension proved earlier in the multiplier section is the mechanism also displayed in (SCF.18); this code does not assume original algebra membership is measurable.

There is a useful membership relation that the core really does determine: membership in \((\mathcal A_\gamma)_{rr}\). Work on a fixed dimension stratum \(H_0\), with a countable right graph core \(r_j(\gamma)\) constructed in SCF-03.

For \(n\geq1\), use auxiliary variables \(z\) in the weak Hilbert ball of radius \(n\) and \(X\) in the weak operator ball of radius \(n\). Both are compact metric spaces. For the Hilbert ball this follows directly by embedding it through a countable orthonormal basis into a product of scalar disks and imposing the closed finite-sum bounds; the limiting coordinates are square summable. The operator assertion is DC-01. Require

\[
 \|\xi\|\leq n,\qquad
 \langle\xi,F_\gamma r_j\rangle=\langle r_j,z\rangle,
 \qquad Xr_j=R_{r_j}\xi \quad(j\geq1).
 \tag{SCF.20}
\]

Test the vector equalities against a countable Hilbert-fundamental family. The equations are jointly Borel in \((\gamma,\xi,z,X)\) and continuous in the compact variables \((z,X)\) at fixed \((\gamma,\xi)\).

Existence in this compact auxiliary space is Borel. To make that assertion explicit, list the scalar residual equations and, for each \(m\), sum the bounded absolute values of the first \(m\) residuals. The minimum over the compact space equals the infimum over a fixed countable dense set, hence is a Borel function of \((\gamma,\xi)\). Existence of a zero for every finite list is equivalent to existence of a simultaneous zero, by nested compactness. Thus the projection is the intersection of the Borel conditions that each of these minima is zero. DC-02 additionally selects a witness.

The first pairing conditions in (SCF.20) say exactly \(\xi\in D(S_\gamma)\) and \(S_\gamma\xi=z\), by extending from the right graph core to the entire graph of \(F_\gamma=S_\gamma^*\). The last equations extend from the right core to every vector \(r\) of the right algebra by the argument in (SCF.18), tested on \(\mathcal A_\gamma\). They say that \(\xi\) is left bounded, with \(\lambda_\xi=X\). Hence the union of these Borel projections over \(n\) is exactly

\[
 \mathscr F=\{(\gamma,\xi):\xi\in(\mathcal A_\gamma)_{rr}\}.
 \tag{SCF.21}
\]

The involution vector and bounded multiplier are unique, since the right core is Hilbert-dense. Their chosen versions are therefore the actual \(S_\gamma\xi\) and \(\lambda_\xi\), not arbitrary substitutes. Choose the least admissible integer \(n\) on the Borel union \(\mathscr F\), and apply DC-02 on each resulting Borel piece. Uniqueness makes these choices agree whenever their domains overlap. Their coordinates and norms are consequently Borel on \(\mathscr F\). This also proves that the full completion, rather than the original nonclosed subalgebra, has canonical measurable membership.

## Select a proper defect under its actual hypothesis

The distinction between a completion and an original algebra becomes decisive here. State a Borel original-membership or analytic-defect hypothesis before selecting outside the original algebra.

Assume explicitly that, on the fixed conull dimension strata, the original membership relation

\[
 \mathscr A=\{(\gamma,\xi):\xi\in\mathcal A_\gamma\}
 \tag{SCF.22}
\]

is Borel. More generally it is enough that the defect relation below be analytic. These are additional hypotheses, not consequences of DI-00.

Since \(\mathscr F\) is Borel, the defect relation \(\mathscr D=\mathscr F\setminus\mathscr A\) is Borel in the first case. Its projection \(N\), the set of nonfull fibres, is analytic and therefore completed-measurable by SCF-05. If \(\mu(N)>0\), that theorem selects \(c(\gamma)\) with \((\gamma,c(\gamma))\in\mathscr D\) on \(N\). The full-completion code supplies measurable \(S_\gamma c(\gamma)\), \(\lambda_{c(\gamma)}\), and all their norms.

Intersect \(N\) with a finite-measure exhaustion and the three integer level bounds. Their union is \(N\), so at least one resulting set \(E\) has positive finite measure. After replacing it by a Borel subset modulo a null set, it satisfies

\[
 0<\mu(E)<\infty,\qquad
 \|c(\gamma)\|,\ \|S_\gamma c(\gamma)\|,
 \ \|\lambda_{c(\gamma)}\|\leq m \quad(\gamma\in E).
 \tag{SCF.23}
\]

Extend \(c\) by zero outside \(E\). This section is in the direct integral of the full fibre completions and is outside the original fibre algebra at every retained point of \(E\). It is nonzero there, since zero belongs to every algebra.

DI-07, now using the proved graph and product constructions, identifies the two-step global dual with the integral of these full completions. If the original integral were full, the selected section would be in the original integral, contradicting its fibre membership on \(E\). Thus, **under the additional analytic-defect hypothesis**, the integral is full if and only if the original fibres are full almost everywhere. The forward implication uses this hypothesis; the reverse implication only uses almost-everywhere equality of the fibres and the two-step dual identity.

This is the correct proper-completion selection instance at its stated hypotheses. It does not prove the original unqualified SELECTION contract or the full printed generality of Corollary VI.3.9.

### Check a measurable proper defect

**Problem 1.** Take the constant original field \(c_{00}\subset\ell^2\) on \([0,1]\). Produce the locally bounded proper-completion witness and explain why this case satisfies the added hypothesis.

**Solution.** Membership in \(c_{00}\) is the countable union of the closed coordinate subspaces with support contained in \(\{1,\ldots,m\}\); it is Borel. The constant vector \(v\) of (SCF.25) is outside every original fibre and in its full completion. Its vector, involution and multiplier norms are respectively \(1/\sqrt3\), \(1/\sqrt3\) and \(1/2\), all bounded by one. The full base has finite measure one. It therefore gives the exact witness in (SCF.23), and the original integral is not full. This contrasts with SCF-10 because that example has no measurable original membership relation.

## Test the hypothesis with constant graph data

Can the countable graph family supply that missing hypothesis by itself? Two scalar-coordinate algebras with identical closed graphs show that it cannot.

Let \(H=\ell^2(\mathbb N)\), with coordinatewise multiplication and conjugation. For every \(x\in H\), its left multiplication has norm \(\|x\|_\infty\leq\|x\|_2\). The involution is an isometry on the whole space. Both \(c_{00}\), the complex finite-support algebra, and \(H\) are left Hilbert algebras with Hilbert completion \(H\), closed involution equal to conjugation, and left von Neumann algebra \(\ell^\infty(\mathbb N)\).

The right-bounded space for either original algebra is all of \(H\): multiplication by \(x\in H\) is bounded with norm \(\|x\|_\infty\). The closed right involution is conjugation on \(H\). Hence their associated right algebra and their full left completion are both \(H\). In particular \(H\) is full, and \(c_{00}\) is not.

Choose a Vitali set \(V\subseteq[0,1]\), one representative for each rational equivalence class meeting that interval. With Lebesgue measure, \(V\) is not measurable even in the completion and has no measurable subset of positive measure. For completeness, distinct rational translates of \(V\) are disjoint, and the translates with rational shifts in \([-1,1]\) cover \([0,1]\) while lying in a bounded interval. If \(V\) were measurable with positive measure, countable additivity for these disjoint translates would contradict the finite measure of that interval; if its measure were zero, their covering would contradict \(\mu([0,1])=1\). The same disjoint-translate argument excludes a positive-measure measurable subset of \(V\).

On the Lebesgue standard base set

\[
 \mathcal A_\gamma=
 \begin{cases}
 c_{00},&\gamma\in V,\\
 H,&\gamma\notin V .
 \end{cases}
 \tag{SCF.24}
\]

The constant family of all finite-support \(\mathbb Q(i)\)-vectors is Hilbert-fundamental and graph-dense for every fibre. Its involutions and products are constant measurable fields. It therefore satisfies all four conditions of DI-00 and even the source's stronger set-density reading of Definition VI.3.1. Nevertheless the set of nonfull fibres is exactly \(V\).

Take the fixed vector \(v=(2^{-n})_{n\geq1}\). It is in \(H\setminus c_{00}\), with

\[
 \|v\|_2^2=\frac13,\qquad
 Sv=v,\qquad \|L_v\|=\frac12 .
 \tag{SCF.25}
\]

The defect relation in the constant full completion has pullback

\[
 \{\gamma:(\gamma,v)\in\mathscr F\setminus\mathscr A\}=V.
 \tag{SCF.26}
\]

A Borel or analytic defect relation would have a completed-measurable pullback under this Borel constant-vector map, by SCF-05. Equation (SCF.26) contradicts that conclusion. Thus the original five-clause contract's general Borel-or-analytic coding of proper-completion defects is false under DI-00 alone. No general cross-section theorem repairs a relation that lacks its required measurable code.

This unconditional example demonstrates the missing coding hypothesis. It does not, by itself, disprove the literal fullness equivalence when an almost-everywhere assertion is interpreted without assuming that the fullness locus is measurable. The next example treats that stronger claim, with its extra set-theoretic assumption made explicit.

## Recognize and measurably implement algebra isomorphisms

Unitary implementation asks a separate choice question for full algebras. Countable closed tests must be proved sufficient for all products and the closed involution before a selected Hilbert-space unitary can be called an algebra isomorphism.

Consider the two full fields in DI-14. Partition the base by their dimensions using DF-02. The strata on which dimensions differ have no isomorphisms. On a common dimension stratum, trivialize both Hilbert fields by one separable Hilbert space \(H_0\). The zero-dimensional case has one unitary and one zero algebra.

For nonzero \(H_0\), its unitary group is Polish in the strong topology. On a fixed Hilbert-fundamental sequence \(e_\ell\), a compatible complete metric is

\[
 d(U,V)=\sum_{\ell\geq1}2^{-\ell}
 \left(\min(1,\|(U-V)e_\ell\|)
       +\min(1,\|(U^*-V^*)e_\ell\|)\right).
 \tag{SCF.14}
\]

A Cauchy sequence has strong limits for both the operators and their adjoints. Their uniform bounds let the inverse identities pass to the limits, so the first limit is unitary and the second is its adjoint. Separability follows from the countable vector coordinates. Inversion is strong-continuous on this group.

Take the rational left star cores \(a_j\) and the measurable rational right graph cores \(r_k\), and take the corresponding cores with the two fields exchanged. Require the tests

\[
 \langle Ua_j,F_2r_k\rangle=\langle r_k,Ua_j^\sharp\rangle,
 \qquad R_{r_k}Ua_j=UL_{a_j}U^*r_k ,
 \tag{SCF.15}
\]

their symmetric \(U^*\)-versions, and

\[
 U\Delta_1^{it}U^*e_\ell=\Delta_2^{it}e_\ell
 \quad(t\in\mathbb Q,\ \ell\geq1).
 \tag{SCF.16}
\]

Each equality is continuous in \(U\) at fixed parameter, and jointly Borel in the parameter and \(U\). For example, variable-vector action is a limit of action on finite rational coordinate approximants, using \(\|U\|=1\). The other operator fields are measurable from SCF-01–03 and DI-03. Norms or countable matrix coefficients test each vector equality. Thus their common relation \(\Sigma\) is Borel and each unitary fibre \(\Sigma_\gamma\) is closed.

We verify sufficiency, which is separate from Borel coding. The first identity in (SCF.15), extended from the right graph core by graph density, is the adjoint characterization of

\[
 Ua_j\in D(S_2),\qquad S_2Ua_j=Ua_j^\sharp .
 \tag{SCF.17}
\]

Put \(Q=UL_{a_j}U^*\). For arbitrary \(r\in(\mathcal A_2)_r\), approximate it by \(r_n\) in the right graph core. Although the norms of their right multipliers need not be bounded, for every \(c\in\mathcal A_2\),

\[
 \langle R_{r_n}Ua_j,c\rangle
 =\langle Ua_j,L_cF_2r_n\rangle
 \longrightarrow\langle Ua_j,L_cF_2r\rangle .
 \tag{SCF.18}
\]

The mixed identity makes the first expression \(\langle Qr_n,c\rangle\), which converges to \(\langle Qr,c\rangle\). Density identifies \(R_rUa_j=Qr\). Hence \(Ua_j\) is left bounded for the full second algebra, and (SCF.17) puts it in \(\mathcal A_2\); its multiplier is \(Q\).

For arbitrary \(\xi\in\mathcal A_1\), use HAP-06 on its rational core as in SCF-03. The approximants converge in the involution graph, with uniformly bounded multipliers converging strongly*. Closedness of \(S_2\) gives \(U\xi\in D(S_2)\) and \(S_2U\xi=US_1\xi\). For each fixed right-bounded \(r\), passing to the limit in the mixed identity gives

\[
 R_rU\xi=(U\lambda_\xi U^*)r,\qquad
 \lambda_{U\xi}=U\lambda_\xi U^* .
 \tag{SCF.19}
\]

Fullness of the second algebra now gives \(U\xi\in\mathcal A_2\). The symmetric tests prove the inverse inclusion. The multiplier identity proves preservation of all products, and the closed involution identity proves preservation of the involution. Thus \(U\) is exactly a full left-Hilbert-algebra isomorphism. Conversely every such isomorphism satisfies these tests; its intertwining of the closed involutions and their adjoints also gives the modular tests, which are compatible redundant tests.

By the assumed fibre isomorphisms, the projection of \(\Sigma\) covers the base modulo a null set. SCF-05 gives a completed-measurable choice \(V_\gamma\in\Sigma_\gamma\). Choose Borel representatives on the common conull set. The direct integral is unitary; the norm, involution and multiplier identities preserve precisely the three conditions defining each integral algebra. Fibrewise product preservation then gives a unitary isomorphism of the original integral algebras. No arbitrary global Hilbert-space isomorphism is being assumed decomposable.

### Check empty and zero-dimensional strata

**Problem 3.** What happens on zero-dimensional or unequal-dimensional unitary strata?

**Solution.** Two zero Hilbert spaces have the unique zero algebra and unique unitary between them; all graph and multiplier tests are empty or zero. Their isomorphism relation is a singleton. If dimensions differ, no unitary exists. SCF-06 partitions these cases before selecting, and does not infer a selector on an empty relation. No positive-measure proper-defect set can occur in the zero fibre.

## Investigate the stronger failure under CH

The following investigation alone assumes CH. It strengthens the preceding coding obstruction to a full global integral with no full original fibres. It supplies no premise to assembly, the qualified fullness theorem or central disintegration.

**Additional hypothesis for this item only:** the Continuum Hypothesis, so that the real continuum has cardinality \(\aleph_1\). This hypothesis is not adopted for the other constructions or for the course.

Continue with the Lebesgue base \(\Gamma=[0,1]\) and \(H=\ell^2(\mathbb N)\). Enumerate the base as \(\{\gamma_\beta:\beta<\omega_1\}\). Enumerate all Borel maps \(\Gamma\to H\) as \(\{f_\alpha:\alpha<\omega_1\}\). This enumeration exists: Borel sets have countable real codes; a map into a separable metric space is specified by inverse images of a countable open basis. There are at most continuum many such maps, and the constant maps give the reverse bound.

At \(\gamma_\beta\), let \(\mathcal A_{\gamma_\beta}\) be the complex star algebra generated by \(c_{00}\) and

\[
 \{f_\alpha(\gamma_\beta):\alpha\leq\beta\}.
 \tag{SCF.27}
\]

Every ordinal \(\beta<\omega_1\) is countable. Its generator list and finite word list are countable, so this algebra has countable complex Hamel dimension. It is proper in \(H\): an infinite-dimensional Hilbert space cannot be a countable union of finite-dimensional subspaces, which are closed and nowhere dense, by the Baire category theorem. Products stay in \(H\), since \(\|xy\|_2\leq\|x\|_\infty\|y\|_2\).

Each fibre is a left Hilbert algebra: bounded multiplication, the adjoint identity and the closable conjugation restrict from \(H\), while \(c_{00}^2=c_{00}\) makes its product span Hilbert-dense. Its closed involution is conjugation on \(H\). It has the same constant rational graph-fundamental family as in SCF-09 and satisfies all four conditions of Definition VI.3.1. All fibres have full completion \(H\), and none is full.

For a fixed \(\alpha\), its map \(f_\alpha\) belongs to \(\mathcal A_{\gamma_\beta}\) whenever \(\beta\geq\alpha\). The exceptional initial segment

\[
 \{\gamma_\beta:\beta<\alpha\}
 \tag{SCF.28}
\]

is countable and hence is a Borel null set. Every completed-measurable Hilbert-valued section has a Borel representative off one null set. Therefore every such section belongs to the original fibre algebra almost everywhere, with a null set that may depend on the section.

It follows directly from the integral definition, including its multiplier bound, that the original integral is exactly

\[
 \mathcal D=
 \left\{\xi\in L^2(\Gamma;\ell^2):
       \operatorname*{ess\,sup}_{(\gamma,n)}
                         |\xi(\gamma)_n|<\infty\right\}.
 \tag{SCF.29}
\]

Involution is pointwise conjugation. This algebra is full. One can check fullness without using the disputed corollary: its finite-support simple vectors are dense in \(L^2(\Gamma\times\mathbb N)\); its closed involution is conjugation on that Hilbert space. Right boundedness is exactly essential boundedness of the coefficient function. The necessity follows by testing on normalized finite-measure indicator functions in a fixed coordinate; if a proposed bound fails, some coordinate exceeds it on a positive finite-measure set. The sufficiency is the pointwise multiplication estimate. Thus its right algebra is \(\mathcal D\), and its second dual is again \(\mathcal D\).

No completed-measurable section can lie outside the original fibre algebra on a positive-measure set. After taking a Borel representative, it is some \(f_\alpha\) and is inside the fibres except on its countable initial segment and the representative's null set. This proves both the failure of the proper-completion selector and

\[
 \text{under CH:}\qquad
 \int^\oplus\mathcal A_\gamma\,d\mu=\mathcal D
 \text{ is full},\qquad
 \mathcal A_\gamma\ne(\mathcal A_\gamma)_{rr}
 \text{ for every }\gamma .
 \tag{SCF.30}
\]

Under this explicit hypothesis the literal unqualified converse in printed Corollary VI.3.9 fails for fields satisfying the printed Definition VI.3.1. This is a conditional counterexample, not a claim of an unconditional counterexample to that corollary. It prevents a ZFC proof of that general claim if ZFC together with CH is consistent. Borel original membership or analytic defect membership in SCF-08 excludes this pathology and gives a valid corrected converse.

## Synthesize graph, algebra and choice tests

**Problem.** For the scalar field at the start of the integral lesson, explain why the section \(x(t)=t^{-1/4}\) defines an involution-graph vector but no bounded global multiplier. Then truncate it to construct integral-algebra vectors converging in that graph norm.

**Solution.** Both vector and involution have squared integral two. Its multiplier norm is \(t^{-1/4}\), which has infinite essential supremum. Put \(x_m=1_{[1/m,1)}x\). Every \(x_m\) and its conjugate is square integrable and its multiplier norm is at most \(m^{1/4}\), so it belongs to the integral algebra. The omitted squared graph norm is \(2\int_0^{1/m}t^{-1/2}\,dt=4/\sqrt m\), tending to zero. The multiplier norms have no common bound. Graph-norm convergence alone therefore does not assert bounded multiplication by the limit.

**Problem.** Which hypotheses are used to assemble an algebra, to recover fullness of original fibres, and to implement fibre isomorphisms?

**Solution.** Assembly uses the graph-dense countable algebra set, measurable products, and the vector, involution and multiplier bounds. Its opposite field uses a genuine closed multiplier core obtained by bounded strong-star approximation. Full fibres imply a full integral with no defect-selection hypothesis. The reverse implication additionally needs the analytic defect relation; the constant-graph example shows why this cannot be omitted from the selection step. Implementation instead uses full fibres, a coded nonempty relation of genuine algebra isomorphisms, and selection after measure completion. Unequal dimensions leave that relation empty; the zero-dimensional case is treated directly. CH is assumed only in its separate counterexample.

### Mathematical sources

Masamichi Takesaki, *Theory of Operator Algebras II*, VI.1 and VI.3, gives the Hilbert-algebra approximation and direct-integral antecedents; Volume I, Appendix A, gives measurable-selection antecedents. The present arguments give explicit product families, multiplier graph cores, sufficient unitary tests and the qualified defect-selection theorem. They retain the distinction between full completion and the original algebra. The new explanatory connections, weak-pairing bridge and synthesis solutions are CC0-1.0 contributions by OpenAI Codex, Ultra, October 2026. Existing proof and component licences remain.

