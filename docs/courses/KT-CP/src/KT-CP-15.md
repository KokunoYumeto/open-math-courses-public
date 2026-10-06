# Equivalence of groupoids and Morita equivalence of their C*-algebras

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A transversal changes the space of units while preserving the arrows that describe the underlying geometry. Its algebra usually changes as an algebra. An equivalence space records how the two unit spaces describe the same geometry, and its compact test functions become an imprimitivity module.

We prove the equivalence theorem for both full and reduced algebras. The proof constructs a linking Haar system, proves positivity of the required convolution forms, and identifies both corner norms. We then apply it to orbit spaces, homogeneous spaces and suspension flows.

Our groupoids and equivalence spaces are second countable, locally compact and locally Hausdorff; the unit spaces are Hausdorff, and all Haar systems have full support. Test functions on non-Hausdorff spaces mean the patch spans of Lesson 13. In particular, taking a pointwise modulus is not an operation on that space. We use the convolution convention of Lesson 14, with \(f^*(\gamma)=\overline{f(\gamma^{-1})}\). Properness of an action means that its action-relation map is proper, in the sense of being closed after every base change.

## The space between two groupoids

Write \(\mathcal G\rightrightarrows X\) and \(\mathcal H\rightrightarrows Y\). An equivalence consists of a space \(Z\), continuous open surjective anchors
\[
 X\ \xleftarrow{\ r_Z\ }\ Z\ \xrightarrow{\ s_Z\ }\ Y,
 \tag{15.1}
\]
and commuting left \(\mathcal G\)- and right \(\mathcal H\)-actions. Both actions are free and proper. The anchors induce homeomorphisms
\[
 Z/\mathcal H\cong X,\qquad \mathcal G\backslash Z\cong Y.
 \tag{15.2}
\]
The right action is defined when \(s_Z(z)=r(h)\); the left action when \(s(g)=r_Z(z)\). Each action preserves the other anchor.

There are unique division arrows
\[
 [z,w]_{\mathcal G}w=z\quad(s_Z(z)=s_Z(w)),\qquad
 z[z,w]_{\mathcal H}=w\quad(r_Z(z)=r_Z(w)).
 \tag{15.3}
\]
Existence follows from (15.2), and uniqueness from freeness. They are continuous. For example, the left action-relation map
\((g,w)\mapsto(gw,w)\) is a continuous proper bijection onto
\(Z\times_{s_Z}Z\), hence a homeomorphism. That fibre product is closed in \(Z\times Z\), since \(Y\) is Hausdorff. Its inverse followed by projection is the first division map. The right argument is identical.

The opposite space \(\bar Z\) has interchanged anchors and actions
\[
 h\bar z=\overline{zh^{-1}},\qquad
 \bar z g=\overline{g^{-1}z}.
 \tag{15.4}
\]
It is an \((\mathcal H,\mathcal G)\)-equivalence.

Form the topological disjoint union
\[
 \mathcal L=\mathcal G\sqcup Z\sqcup\bar Z\sqcup\mathcal H,
 \qquad \mathcal L^{(0)}=X\sqcup Y.
 \tag{15.5}
\]
The existing products and actions define its products except for the two cross products, which are
\[
 z\bar w=[z,w]_{\mathcal G},\qquad
 \bar z w=[z,w]_{\mathcal H}.
 \tag{15.6}
\]
Inversion interchanges \(z,\bar z\). These formulas give a locally Hausdorff groupoid. Continuity follows from the division maps. Associativity with two cross products is the identity
\([x,y]_{\mathcal G}z=x[y,z]_{\mathcal H}\): both sides follow by writing
\(z=y[y,z]_{\mathcal H}\) and commuting the two actions. The remaining cases use the action laws, or follow by inversion. Thus this assertion includes the mixed products, rather than only the two original subgroupoids.

## Measures on the cross arrows

Let \(\lambda^x,\beta^y\) be the Haar systems of \(\mathcal G,\mathcal H\). For \(r_Z(z)=x\) and \(s_Z(w)=y\), define
\[
 \begin{aligned}
 \sigma^x(\phi)&=\int_{\mathcal H^{s_Z(z)}}\phi(zh)\,d\beta^{s_Z(z)}(h),\\
 \tau^y(\phi)&=\int_{\mathcal G^{r_Z(w)}}\phi(g^{-1}w)\,d\lambda^{r_Z(w)}(g).
 \end{aligned}
 \tag{15.7}
\]
They are measures on \(Z^x=r_Z^{-1}(x)\) and \(Z_y=s_Z^{-1}(y)\). The division homeomorphisms identify these fibres with Haar fibres, so they are Radon and have full support. A different \(z\) in its right orbit gives the same first integral by left invariance of \(\beta\); left invariance of \(\lambda\) gives the same independence for the second integral.

We need continuity of these families, including for patch functions. Here is the compact argument. For a term \(\phi\in C_c(V)\), with \(V\subset Z\) Hausdorff open, choose
\(\operatorname{supp}_V\phi\subset O\subset C\subset V\), where \(O\) is open and \(C\) compact Hausdorff. For the right action, the pairs in \(C\times C\) having the same \(r_Z\) form a compact Hausdorff space. The action-relation homeomorphism identifies it with the compact set of \((z,h)\) for which \(z,zh\in C\).

Cover its compact arrow-coordinate image by finitely many Hausdorff patches of \(\mathcal H\), and partition the compact relation accordingly. The functions obtained from \(\phi(zh)\) and this partition extend by zero to continuous compact functions on the **composable** part of \(C\) times each arrow patch. This is a closed fibre product inside a Hausdorff product; we do not extend by zero across the anchor equation. To check continuity within it, points with \(zh\in O\) eventually remain in that open part of the compact relation. At a point with \(zh\notin O\), a persistent nonzero value would have a convergent subnet in the compact support of its partition term. Hausdorffness of the product forces that limit to be the alleged boundary point; continuity on the relation then contradicts \(\phi(zh)=0\). The compact integration observation (14.2), which uses extension from the closed fibre product and finite product approximation, proves continuity of the orbit integral on \(O\).

It is constant on right orbits. Since \(r_Z:O\to r_Z(O)\) is open, this descends to a continuous function on \(r_Z(O)\). It vanishes outside the compact set \(r_Z(\operatorname{supp}\phi)\), which is closed in \(X\) and lies in that open set. Therefore \(x\mapsto\sigma^x(\phi)\) belongs to \(C_c(X)\). Inverting the action proves the \(\tau\) assertion. Summing proves both for patch spans.

This proof also gives positive averaging onto the quotient. For example, if \(d\geq0\) belongs to \(C_c(s_Z(V))\), take a nonnegative \(\chi\in C_c(V)\) whose \(\tau\)-average is positive on \(\operatorname{supp}d\). Such a \(\chi\) is a finite sum of bumps, using full support and a compact cover. Then
\[
 \psi(z)=\frac{d(s_Z(z))\chi(z)}{\tau^{s_Z(z)}(\chi)}
 \quad\text{has}\quad \tau^y(\psi)=d(y).
 \tag{15.8}
\]
Use zero outside the support of \(d\); its compact support lies where the denominator is bounded below. The analogous assertion holds for \(\sigma\).

Give \(\mathcal L\) the range Haar measures
\[
 \kappa^x=\lambda^x+\sigma^x\quad(x\in X),\qquad
 \kappa^y=\overline{\tau^y}+\beta^y\quad(y\in Y),
 \tag{15.9}
\]
where the bar pushes a measure on \(Z\) to \(\bar Z\). Continuity and full support have just been proved. For left invariance, multiplication by \(g\in\mathcal G\) preserves \(\lambda\), and carries the first formula in (15.7) to the same formula based at \(gz\). Multiplication by \(z\in Z\) carries the \(\mathcal H\)-part to \(\sigma^{r_Z(z)}\). On the opposite part use \(w=z\) in (15.7): it carries \(\overline{g^{-1}z}\) to \(z\overline{g^{-1}z}=g\), hence carries that measure to \(\lambda^{r_Z(z)}\). Inversion and symmetry give the other two cases. Thus (15.9) is a Haar system, and Lesson 14 constructs both algebras of \(\mathcal L\).

For \(\phi,\psi\in C_c(Z)\), convolution in \(\mathcal L\) gives
\[
 \begin{aligned}
 (f\phi)(z)&=\int f(g)\phi(g^{-1}z)\,d\lambda^{r_Z(z)}(g),\\
 (\phi b)(z)&=\int\phi(zh)b(h^{-1})\,d\beta^{s_Z(z)}(h),\\
 \langle\phi,\psi\rangle_{\mathcal H}(h)
 &=\int\overline{\phi(g^{-1}z)}\psi(g^{-1}zh)\,d\lambda^{r_Z(z)}(g),\\
 {}_{\mathcal G}\langle\phi,\psi\rangle(g)
 &=\int\phi(gwh)\overline{\psi(wh)}\,d\beta^{s_Z(w)}(h).
 \end{aligned}
 \tag{15.10}
\]
Choose \(s_Z(z)=r(h)\) in the third line and \(r_Z(w)=s(g)\) in the fourth. Their independence is (15.7). The two forms are \(\phi^**\psi\) and \(\phi*\psi^*\) in the two diagonal corners. Associativity and the adjoint identity of Lesson 14 consequently prove all bimodule identities, including
\[
 {}_{\mathcal G}\langle\phi,\psi\rangle\chi
   =\phi\langle\psi,\chi\rangle_{\mathcal H}.
 \tag{15.11}
\]
Their positivity for the full norms still requires proof.

## An approximate identity made from cross arrows

We first establish the analytic ingredient that makes positivity possible.

**Lemma 15.1.** There are nets
\[
 e_\iota=\sum_j\phi_{\iota j}^**\phi_{\iota j}\in C_c(\mathcal H),
 \qquad
 a_\rho=\sum_j\psi_{\rho j}*\psi_{\rho j}^*\in C_c(\mathcal G),
 \tag{15.12}
\]
which are two-sided convolution approximate identities on their diagonal test algebras, and act as approximate identities on the appropriate cross-arrow spaces. Convergence is uniform with supports in a fixed compact set for each fixed test function.

**Proof.** We construct \(e_\iota\). Fix a compact \(K\subset Y\), an open neighborhood \(W\) of the units in \(\mathcal H\), and \(\varepsilon>0\). Continuity of the division map at \((z,z)\) gives each \(z\) a precompact Hausdorff neighborhood \(V\) such that
\([v,w]_{\mathcal H}\in W\) whenever \(v,w\in V\) have the same \(r_Z\). Since \(s_Z\) is open and onto, finitely many such \(V_j\) have source images covering \(K\). Choose \(d_j\geq0\) supported compactly inside those images, with \(\sum_jd_j=1\) on \(K\) and \(\sum_jd_j\leq1\) everywhere. By (15.8), choose \(\psi_j\geq0\) supported compactly in \(V_j\) with \(\tau(\psi_j)=d_j\).

For one of these functions put \(A(x)=\sigma^x(\psi)\) and, for \(t>0\), put
\[
 \phi_t(z)=\frac{\psi(z)}{\sqrt{A(r_Z(z))+t}}.
 \tag{15.13}
\]
Then
\[
 \sigma^x(\phi_t)=\frac{A(x)}{\sqrt{A(x)+t}},\qquad
 \phi_t(z)\sigma^{r_Z(z)}(\phi_t)
       =\psi(z)\frac{A(r_Z(z))}{A(r_Z(z))+t}.
 \tag{15.14}
\]
The last expression tends uniformly to \(\psi\). Indeed \(A(r_Z(z))=0\) forces \(\psi(z)=0\) by full support. On the compact Hausdorff support the continuous error
\(\psi(z)t/(A(r_Z(z))+t)\) decreases to zero. Compactness, or Dini's theorem, gives uniform convergence. Outside that support it is zero. This argument avoids dividing by a potentially vanishing orbit integral.

Choose a small \(t_j\) for each \(j\), and set \(e=\sum_j\phi_{t_j}^**\phi_{t_j}\). Its values are nonnegative, and it is self-adjoint; these are statements about its test kernel, before using C*-positivity. Fubini and (15.10) give
\[
 \int_{\mathcal H^y}e(h)\,d\beta^y(h)
 =\sum_j\tau^y\!\left(\phi_{t_j}\,
                      (\sigma(\phi_{t_j})\circ r_Z)\right).
 \tag{15.15}
\]
The right side differs uniformly from \(\sum_jd_j(y)\) by less than \(\varepsilon\): dominate the fixed supports by positive patch bumps, whose \(\tau\)-integrals have a common finite bound, and apply the uniform errors in (15.14). Thus the range masses are within \(\varepsilon\) of one on \(K\), and at most \(1+\varepsilon\) everywhere. Self-adjointness gives the same source bound, so \(\|e\|_I\leq1+\varepsilon\). Its carrying compact set lies in \(W\), by the choice of the \(V_j\) and the division formula.

Here are the support and uniformity details when \(W\) shrinks. First fix one neighborhood of the units that controls compact supports. Take a locally finite cover of \(Y\) by compact sets \(K_i\) whose interiors cover \(Y\). Choose a compact arrow neighborhood \(U_i'\) of \(K_i\), using finitely many compact Hausdorff charts, and put
\(U_i=U_i'\cap r^{-1}(K_i)\cap s^{-1}(K_i)\).
Their union \(U\) is a neighborhood of the units. For any compact \(D\subset Y\), its range or source slice in \(U\) is contained in a finite union of the \(U_i'\): only finitely many \(K_i\) meet \(D\). More precisely the slice is a finite union of compact closed slices of the \(U_i\), hence compact. Restrict all subsequent \(W\) to the interior of \(U\). Products with a fixed test support now lie in a fixed compact set; composability cuts out a closed subset of the compact product.

We can also arrange Hausdorffness on any required compact range slice. Cover a compact \(D\subset Y\) by interiors of finitely many closed unit neighborhoods \(D_j\), each contained in a Hausdorff arrow chart \(B_j\). Intersect the unit neighborhoods
\(r^{-1}(Y\setminus D_j)\cup B_j\).
If two arrows in the resulting range slice at \(D\) cannot be separated, continuity to the Hausdorff unit space gives the same range. That range lies in some \(D_j\), placing both arrows in \(B_j\), a contradiction. Inversion gives the source version.

For a fixed finite collection of test patches, take compact neighborhoods of their supports inside the original Hausdorff patches. Continuity of the actions at units and compactness let us shrink \(W\) so that small translations of these compact sets stay in those patches and change the test values uniformly little. One direct justification of the shrinking step is to take, over each fixed unit, a finite cover of the compact anchor fibre by product neighborhoods on which the action has the desired property. A closed-map compactness argument extends that finite cover to nearby units. Cover the compact anchor image by finitely many such unit neighborhoods, and add the complement of that image. Apply this to \(W\) and \(W^{-1}\), so that it also controls translations whose output, rather than input, meets the support. The preceding Hausdorff slices permit the uniform-continuity argument inside the chosen charts.

On those Hausdorff patches write, for a left action on a test function \(q\),
\[
 eq-q=\int e(h)\big(q(h^{-1}\,\cdot\,)-q\big)\,d\beta
             +\big(\beta(e)-1\big)q.
 \tag{15.16}
\]
The first term is uniformly small by the translation control and the bound \(1+\varepsilon\); the second is small by (15.15), taking \(K\) to contain the anchor image of the support of \(q\). The same argument applies to each term of a patch sum. Taking adjoints gives the right convolution assertion. Let compact \(K\) exhaust \(Y\), shrink \(W\) subject to these finite constraints, and let \(\varepsilon\downarrow0\). This yields the claimed net with the required fixed-support convergence. Repeating the construction for \(\bar Z\) gives \(a_\rho\). ∎

Applying the lemma to the identity equivalence of a groupoid with itself also gives an ordinary test-function approximate identity. Neither that application nor the construction above has presumed positivity in a full completion.

## Positivity and the two corner norms

Let \(p,q\) be the unit-space multipliers of \(\mathcal L\) corresponding to the characteristic functions of \(X,Y\). The bound and formulas (14.14)–(14.15), applied to bounded unit functions, put them in the multiplier algebras of both completions. They are complementary projections. On the core their four corners are
\[
 \begin{pmatrix}
 C_c(\mathcal G)&C_c(Z)\\
 C_c(\bar Z)&C_c(\mathcal H)
 \end{pmatrix}.
 \tag{15.17}
\]

**Lemma 15.2.** For \(v_1,\ldots,v_n\in C_c(\mathcal L)p\), the matrix
\([v_i^**v_j]_{i,j}\) is positive in \(M_n(C^*(\mathcal G))\).

**Proof.** Write the two components of \(v_i\) as \(f_i\in C_c(\mathcal G)\) and \(\eta_i\in C_c(\bar Z)\). The matrix is the sum of \([f_i^**f_j]\) and \([\eta_i^**\eta_j]\). The first is a usual C*-algebra Gram matrix. For the second use (15.12):
\[
 \eta_i^**e_\iota*\eta_j
   =\sum_k(\phi_{\iota k}*\eta_i)^**
                  (\phi_{\iota k}*\eta_j).
 \tag{15.18}
\]
Every factor \(\phi_{\iota k}*\eta_i\) belongs to \(C_c(\mathcal G)\), so the matrix on the right is positive. Lemma 15.1 and continuity of convolution make it converge to the desired matrix in \(I\)-norm, hence in the full norm. The positive cone is closed. ∎

**Theorem 15.3.** Zero extension identifies \(C^*(\mathcal G)\) and \(C^*(\mathcal H)\) with the complementary full corners of \(C^*(\mathcal L)\). The analogous assertion holds for reduced algebras.

**Proof for the full norms.** Restricting an \(I\)-contractive representation of \(\mathcal L\) to \(C_c(\mathcal G)\) gives an \(I\)-contractive representation of \(\mathcal G\), since its \(I\)-norm is unchanged. Thus the corner norm is at most the full \(\mathcal G\)-norm.

For the reverse bound, take a separable nondegenerate representation \(\pi\) of \(C^*(\mathcal G)\) on \(H_\pi\). On the algebraic tensor space \(C_c(\mathcal L)p\odot H_\pi\) put
\[
 \left\langle\sum_i v_i\otimes h_i,\sum_j w_j\otimes k_j\right\rangle
 =\sum_{i,j}\langle h_i,\pi(v_i^**w_j)k_j\rangle.
 \tag{15.19}
\]
Lemma 15.2 makes this positive. Divide by the null space and complete to \(H\). Left convolution by \(F\in C_c(\mathcal L)\) has formal adjoint left convolution by \(F^*\). It preserves the null space: a null vector pairs to zero with every vector by Cauchy–Schwarz, so its image pairs to zero using the formal adjoint, including with itself. Hence convolution gives a representation on the dense tensor domain.

Its matrix coefficients are continuous for uniform convergence on a fixed compact set, by convolution continuity and the bound of \(\pi\) by \(I\). The ordinary approximate identity supplied after Lemma 15.1 makes its essential range dense. The completion is separable: choose countable compact-patch approximating sets in \(C_c(\mathcal L)\) and a countable dense set in \(H_\pi\), and use (15.19) to approximate tensors. The exact disintegration prerequisite of Lesson 14 therefore makes this a bounded \(I\)-contractive representation of \(\mathcal L\).

Its \(p\)-subspace is the completion of \(C_c(\mathcal G)\odot H_\pi\), and
\[
 f\otimes h\longmapsto\pi(f)h
 \tag{15.20}
\]
is an isometry onto \(H_\pi\). Orthogonality to the other row follows from the block products in (15.17); surjectivity follows from nondegeneracy. Left convolution by a \(\mathcal G\)-kernel acts there as \(\pi\). Its \(\mathcal L\)-norm is consequently at least \(\|\pi(f)\|\). Supremum over separable cyclic representations gives the full norm of \(f\). This proves equality, and symmetry proves the \(\mathcal H\)-corner equality. Core compression and density identify the completed corners.

To prove fullness of \(p\), its generated ideal contains the \(\mathcal G\)-corner and the cross corners, by the diagonal approximate identity. It contains every \(\phi^**\psi\) in the \(\mathcal H\)-corner; (15.12) and its convolution approximation then put all of that corner in the ideal. Thus it contains all four corners. Symmetry proves fullness of \(q\).

**Proof for the reduced norms.** This part needs no disintegration. For \(f\in C_c(\mathcal G)\), the regular source fibre of \(\mathcal L\) at \(x\in X\) is
\(\mathcal G_x\sqcup\bar Z_x\); \(f\) acts as the \(\mathcal G\)-regular operator on the first summand and zero on the second. At \(y\in Y\) it is \(Z_y\sqcup\mathcal H_y\), with measure \(\tau^y+\beta_y\). Choose \(z_0\in Z_y\). The homeomorphism
\[
 \mathcal G_{r_Z(z_0)}\longrightarrow Z_y,\qquad
       \gamma\longmapsto\gamma z_0
 \tag{15.21}
\]
carries the source Haar measure to \(\tau^y\), by inversion in (15.7). It intertwines the action of \(f\) with the regular representation of \(\mathcal G\) at \(r_Z(z_0)\). The \(\mathcal H_y\)-summand is zero. Taking the supremum over both kinds of unit proves equality with \(\|f\|_{r,\mathcal G}\). Symmetry proves the other corner norm. The images of full multiplier projections in a quotient remain full, so \(p,q\) are full in the reduced completion too. ∎

By *Imprimitivity bimodules and Morita equivalence*, Theorem 5.1, complementary full corners have the off-diagonal corner as their imprimitivity module. We have therefore proved
\[
 \begin{aligned}
 C^*(\mathcal G)&\sim_M C^*(\mathcal H),
   &E&=\overline{C_c(Z)}^{\,C^*(\mathcal L)},\\
 C_r^*(\mathcal G)&\sim_M C_r^*(\mathcal H),
   &E_r&=\overline{C_c(Z)}^{\,C_r^*(\mathcal L)}.
 \end{aligned}
 \tag{15.22}
\]
The actions and forms are exactly (15.10), and
\(\|\phi\|_E^2=\|\langle\phi,\phi\rangle_{\mathcal H}\|\), with the corresponding reduced norm for \(E_r\). Positivity is supplied by the proved corner identifications, not by the sign of a scalar kernel.

There is a precise compatibility between the two equivalences. Let \(I_{\mathcal H}\) be the kernel of \(C^*(\mathcal H)\to C_r^*(\mathcal H)\). The full-to-reduced linking quotient induces a map \(E\to E_r\), whose kernel is
\[
 \{\xi:\langle\xi,\xi\rangle_{\mathcal H}\in I_{\mathcal H}\}
       =\overline{E I_{\mathcal H}}.
 \tag{15.23}
\]
The equality and quotient norm are *The Rieffel correspondence and induced representations*, Lemma 1.1 and Proposition 2.2. Its left ideal is exactly \(I_{\mathcal G}\), since the quotient's two corners have just been identified with the reduced algebras. Thus \(E_r=E/\overline{E I_{\mathcal H}}\), and the Rieffel correspondence matches the two regular kernels. This also proves that the same groupoid with two full Haar systems has Morita equivalent algebras: use its identity equivalence, with the two systems on its two sides.

## Changing the unit space

Let \(N\subset X\) be locally closed, meet every orbit, and satisfy the additional condition
\[
 r:s^{-1}(N)\longrightarrow X
       \quad\text{is open and onto}.
 \tag{15.24}
\]
Set \(Z=s^{-1}(N)\) and \(\mathcal H=\mathcal G|_N\). Multiplication gives a left \(\mathcal G\)-action and a right \(\mathcal H\)-action on \(Z\). The anchors are \(r:Z\to X\) and \(s:Z\to N\). The latter is open: it is the base change of the open source map of \(\mathcal G\). Similarly \(r:\mathcal H\to N\) is the base change of (15.24), and inversion makes its source map open.

Both actions are free. Their division arrows are
\[
 [z,w]_{\mathcal G}=zw^{-1},\qquad
 [z,w]_{\mathcal H}=z^{-1}w
 \tag{15.25}
\]
on the respective equal-source and equal-range pairs. These formulas show that the action-relation maps are homeomorphisms onto the closed anchor fibre products. They are therefore proper, including after base change. Fibres of \(r\) are precisely right \(\mathcal H\)-orbits, and fibres of \(s\) are left \(\mathcal G\)-orbits. Openness of the anchors identifies the quotient topologies. Thus \(Z\) is an equivalence.

If \(\mathcal H\) has a full Haar system, (15.22) gives
\[
 C^*(\mathcal G)\sim_M C^*(\mathcal G|_N),\qquad
 C_r^*(\mathcal G)\sim_M C_r^*(\mathcal G|_N).
 \tag{15.26}
\]
A Haar system on the reduction is a real requirement. Restricting ambient Haar measures to a transverse set often gives zero measures. For Hausdorff groupoids, existence transfers across equivalence by [Williams]. Here its hypotheses are satisfied: the two groupoids are second countable locally compact Hausdorff, their range maps are open, and the original groupoid has a Haar system. For a non-Hausdorff reduction we require a Haar system explicitly; smooth or étale transverse constructions supply it in the examples.

Merely meeting every orbit, even with a closed \(N\), does not imply (15.24). The horizontal-translation reduction in Lesson 13 has an isolated cross arrow at the origin and a range map that is not open. It cannot be substituted into this theorem.

## Inner exactness survives a change of groupoid

Assume in this section that the equivalent groupoids and their equivalence space are Hausdorff, with the second countability and full Haar hypotheses used above. Inner exactness means exactness of the reduced sequence for every open invariant subset of units, as defined in Lesson 14. It is weaker than exactness of the crossed-product functor on all coefficient algebras.

**Theorem 15I.1 (LaLonde).** Equivalent groupoids are inner exact simultaneously.

**Proof.** For an open invariant \(U\subseteq\mathcal G^{(0)}\), put
\[
V=s_Z(r_Z^{-1}(U))\subseteq\mathcal H^{(0)}.
\tag{15I.1}
\]
The anchors are open, so \(V\) is open; the commuting actions make it invariant. Moreover
\[
r_Z^{-1}(U)=s_Z^{-1}(V).
\tag{15I.2}
\]
To prove the nontrivial containment, suppose \(s_Z(z)\in V\). Choose \(z'\) with the same source and \(r_Z(z')\in U\). The left principal action gives \(z'=gz\) for an arrow \(g\) whose source is \(r_Z(z)\). Invariance of \(U\) gives \(r_Z(z)\in U\). Interchanging the anchors proves the analogous inverse construction from invariant \(V\), so (15I.1) is a bijection on invariant open sets.

In the linking groupoid \(L\), the set \(W=U\sqcup V\) is therefore invariant. Its open and closed reductions are again linking groupoids, for the restricted equivalence spaces. Write
\[
C=C_r^*(L),\quad
I=C_r^*(L|_W),\quad
K=\ker\bigl(C_r^*(L)\to C_r^*(L|_{L^{(0)}\setminus W})\bigr).
\tag{15I.3}
\]
Let \(p,q\) be the complementary unit-space corner projections in \(M(C)\). The fibre unitaries proving the reduced corner theorem above apply to these restrictions as well. Thus \(pCp=C_r^*(\mathcal G)\), \(pIp=C_r^*(\mathcal G|_U)\), and
\[
pKp=\ker\bigl(C_r^*(\mathcal G)
   \to C_r^*(\mathcal G|_{\mathcal G^{(0)}\setminus U})\bigr).
\tag{15I.4}
\]
The corresponding statements hold in the \(q\)-corner for \(\mathcal H,V\). The restriction homomorphism sends \(p\) to the closed-reduction \(\mathcal G\)-corner projection, which explains the kernel identity rather than just an abstract Morita equivalence.

These restriction maps are defined for the general Haar systems here, not only for counting systems. Invariance makes every source fibre over a closed-reduction unit stay in that reduction, with the same Haar measure. Its regular operator is consequently the corresponding original fibre operator, proving contractivity of restriction. Compactly supported functions on the closed reduction extend to the Hausdorff ambient groupoid by a compactly supported Tietze extension, so the range is dense and hence onto. For an open invariant reduction, extension by zero gives its original regular norm, with zero fibre operators elsewhere; convolution shows that its image is an ideal. This also proves \(I\subseteq K\) in (15I.3).

The projection \(p\) is full in \(C\). For any ideal \(J\triangleleft C\),
\[
J=\overline{C(pJp)C}.
\tag{15I.5}
\]
Indeed, finite sums in \(CpC\) approximate a C*-approximate identity because that ideal is dense in \(C\). Multiplying \(j\in J\) on both sides by such sums approximates it by sums whose middle terms are \(pbjcp\in pJp\). The reverse inclusion is immediate. Hence equality of two ideals' \(p\)-corners implies equality of the ideals.

If \(\mathcal G\) is inner exact, (15I.4) gives \(pKp=pIp\). Equation (15I.5) makes \(K=I\). Taking \(q\)-corners now gives exactness of the reduced restriction sequence for \(\mathcal H,V\). Every invariant \(V\) arises from (15I.1), so \(\mathcal H\) is inner exact. Applying the same argument to the opposite equivalence proves the converse. ∎

The argument tracks both the open ideal and the closed-reduction kernel through the same linking algebra. An abstract isomorphism of ideal lattices, without this compatibility with restriction, would not identify the kernel in (15I.4). The theorem permits transfer of the inner-exactness hypothesis in Lesson 14's ideal description to any equivalent Hausdorff model.

## Two familiar equivalences

Suppose a second countable locally compact group \(K\) acts freely and properly on a second countable locally compact Hausdorff space \(P\). The orbit space \(B=P/K\) is locally compact Hausdorff, and its quotient map is open, by Lesson 9. Regard \(B\) as a unit groupoid. Then \(Z=P\), with anchors \(\operatorname{id}_P,q\), is an \((P\rtimes K,B)\)-equivalence. The left action sends the source of an arrow to its target; the right unit action fixes the point. Freeness and properness of the left action are precisely those of the original group action. The right action-relation map is the closed diagonal of \(P\). The two quotient assertions are \(P/B=P\) and \((P\rtimes K)\backslash P=B\). Therefore
\[
 C_0(P)\rtimes K\sim_M C_0(B),\qquad
 C_0(P)\rtimes_r K\sim_M C_0(B).
 \tag{15.27}
\]
We used the full and reduced transformation identifications of Lesson 14. This recovers the free proper result of Lesson 9.

For the scalar version of Green's theorem, let \(H\) be a closed subgroup of \(K\). The space \(Z=K\) is an equivalence between \(K/H\rtimes K\) and the one-unit groupoid \(H\). Its anchors are \(k\mapsto kH\) and the constant map. The left action is multiplication by the transformation arrow, and the right action is multiplication by \(H\). The left action-relation map has inverse determined by \(k'k^{-1}\); the right one is a homeomorphism onto the closed equal-coset relation. The quotient assertions and openness follow from the quotient topology of \(K/H\). Hence
\[
 C_0(K/H)\rtimes K\sim_M C^*(H),\qquad
 C_0(K/H)\rtimes_r K\sim_M C_r^*(H).
 \tag{15.28}
\]

The modular factors are worth checking. Write \(\Delta_K,\Delta_H\) for the modular functions and put
\[
 \xi(k)=\Delta_K(k)^{1/2}F(k),\qquad
 \kappa(h)=\left(\frac{\Delta_K(h)}{\Delta_H(h)}\right)^{1/2}.
 \tag{15.29}
\]
Here \(\xi\) is the linking test function and \(F\) the rescaled Green function of (7.38). Passing from groupoid kernels to crossed-product kernels uses \(\Delta_K(a)^{-1/2}\), or \(\Delta_H(h)^{-1/2}\), by (14.16). Substitution in (15.10) gives
\[
 \begin{aligned}
 (cF)(k)&=\int_K c(a,kH)F(a^{-1}k)\,da,\\
 (Fb)(k)&=\int_H\kappa(h)F(kh)b(h^{-1})\,dh,\\
 R(F,Q)(h)&=\kappa(h)\int_K\overline{F(k)}Q(kh)\,dk,\\
 L(F,Q)(a,kH)&=\frac{\Delta_K(k)}{\Delta_K(a)}
       \int_H\Delta_K(h)F(kh)\overline{Q(a^{-1}kh)}\,dh .
 \end{aligned}
 \tag{15.30}
\]
For the third line, choose \(z=e\) in (15.10) and change \(g^{-1}=k\); then \(dg=\Delta_K(k)^{-1}dk\). The two factors from (15.29) and the \(\Delta_H(h)^{-1/2}\) conversion leave exactly \(\kappa(h)\). For the fourth line the product of the two factors in (15.29), followed by the \(\Delta_K(a)^{-1/2}\) conversion, is
\(\Delta_K(k)\Delta_K(h)/\Delta_K(a)\).
Thus these are the scalar formulas already proved in Lesson 7. General coefficient algebras require its coefficient-valued construction; the scalar groupoid theorem alone does not supply that extra structure.

## Suspensions and the Kronecker flow

Let \(\varphi:P\to P\) be a homeomorphism of a second countable locally compact Hausdorff space. Its suspension is
\[
 \Sigma_\varphi=(\mathbb R\times P)/\!\sim,\qquad
       (t+1,x)\sim(t,\varphi(x)).
 \tag{15.31}
\]
Equivalently, the deck action of \(n\in\mathbb Z\) is
\((t,x)\mapsto(t-n,\varphi^n(x))\).
It is free and proper: on compact sets the real coordinates bound the possible integers. Hence the suspension is locally compact Hausdorff and second countable. Small intervals of length less than one give quotient charts.

Translation defines a flow \(s[t,x]=[t+s,x]\). The embedded copy \(N=\{[0,x]:x\in P\}\) meets every orbit. Every arrow with source in \(N\) is uniquely described by \((t,x)\), so the equivalence space is
\[
 Z=\mathbb R\times P,\qquad
     r_Z(t,x)=[t,x],\quad s_Z(t,x)=x.
 \tag{15.32}
\]
The range anchor is the open quotient map; the source anchor is the open projection. An arrow starting and ending in \(N\) has integer time \(n\), and sends \(x\) to \(\varphi^n(x)\). Consequently the reduction is \(P\rtimes\mathbb Z\). Its topology is the product topology with discrete integer coordinate, as is seen in the quotient charts. If a reduction arrow has target \(x\) and time \(n\), its source is \(\varphi^{-n}(x)\), and its right action is
\[
 (t,x)\cdot(x,n)=(t+n,\varphi^{-n}(x)).
 \tag{15.33}
\]
This preserves \([t,x]\), as required. The left action is addition of flow time. The division formulas (15.25) prove principality; alternatively two points with the same suspension image differ by one unique deck transformation. Counting measure on the reduction and Lebesgue measure on the flow groupoid are full Haar systems.

With \(\alpha(a)=a\circ\varphi^{-1}\), the equivalence theorem and Lesson 14 give
\[
 C_0(\Sigma_\varphi)\rtimes\mathbb R
       \sim_M C_0(P)\rtimes_\alpha\mathbb Z,
 \qquad
 C_0(\Sigma_\varphi)\rtimes_r\mathbb R
       \sim_M C_0(P)\rtimes_{\alpha,r}\mathbb Z .
 \tag{15.34}
\]
Both groups are amenable, so in this example each full algebra equals its reduced algebra, by Lesson 4. Compactness of \(P\) is needed only when we write \(C(P)\) rather than \(C_0(P)\).

Take \(P=\mathbb R/\mathbb Z\) and \(\varphi(z)=z+\theta\). The map
\[
 [t,z]\longmapsto(t\bmod1,\ z+\theta t\bmod1)
 \tag{15.35}
\]
is a homeomorphism \(\Sigma_\varphi\to\mathbb T^2\). It respects (15.31); an inverse is obtained by lifting the first coordinate and subtracting \(\theta t\) from the second, with different lifts related by the deck action. The flow becomes
\((x,y)\mapsto(x+s,y+\theta s)\).
The transversal is \(\{0\}\times\mathbb T\), and the return times are the integers. Thus
\[
 C(\mathbb T^2)\rtimes_{\mathrm{Kronecker}}\mathbb R
       \sim_M A_\theta .
 \tag{15.36}
\]
Our generators agree with Lesson 3: for \(v(z)=e^{2\pi iz}\) and the unitary \(u\) implementing \(\alpha\),
\[
 uvu^*=e^{-2\pi i\theta}v,\qquad
       vu=e^{2\pi i\theta}uv .
 \tag{15.37}
\]
The equivalence holds for every real \(\theta\); irrationality is the additional hypothesis for minimality and simplicity. Morita invariance of K-theory and Lesson 11's calculation give \(K_0(A_\theta)\cong K_1(A_\theta)\cong\mathbb Z^2\). A Morita equivalence here is not an assertion that these two displayed algebras are isomorphic.

## The suspension sequence and PV

For compact \(P\), put \(A=C(P)\). Functions on its suspension identify with the mapping torus
\[
 M_\alpha=\{a\in C([0,1],A):a(1)=\alpha^{-1}(a(0))\}.
 \tag{15.38}
\]
Indeed \(a(t)(x)=F([t,x])\), and (15.31) gives
\(a(1)(x)=a(0)(\varphi(x))\).
Evaluation at zero yields \(0\to SA\to M_\alpha\to A\to0\), where \(SA=C_0((0,1),A)\). Under the positive suspension identification of Lesson 10, its connecting map is \(\alpha_*^{-1}-1\), as computed in Lesson 11. Multiplying its target by \(\alpha_*\) changes it to \(1-\alpha_*\).

Apply the Connes–Thom isomorphism to the suspension flow and the K-theory isomorphism of (15.34). Their parity shift rotates this six-term sequence into the PV sequence. Writing \(B=A\rtimes_\alpha\mathbb Z\), it has the cyclic form
\[
 \begin{gathered}
 K_0(A)\xrightarrow{\,1-\alpha_*\,}K_0(A)
    \xrightarrow{\,i_*\,}K_0(B)\xrightarrow{\,\partial_0\,}K_1(A),\\
 K_1(A)\xrightarrow{\,1-\alpha_*\,}K_1(A)
    \xrightarrow{\,i_*\,}K_1(B)\xrightarrow{\,\partial_1\,}K_0(A).
 \end{gathered}
 \tag{15.39}
\]
The first row's last group continues as the second row's first group, and conversely. Here \(i\) is the canonical coefficient inclusion. Exactness follows from the mapping-torus sequence and the two isomorphisms.

The exact written Fourier-window comparison in *The Pimsner–Voiculescu exact sequence*, Lemma 2.1 and equation (2.9), identifies the transported arrows with \(i_*\), in the positive both-degree Thom normalization specified in Lesson 11. Its dependencies include the Thom theorem, without the PV application, so this use introduces no circular proof. The geometric equivalence and this comparison prove the PV deduction with the canonical coefficient arrows. Rosenberg, §2.5, p. 108, gives the literature presentation. The same argument works for locally compact \(P\) with \(C_0(P)\).

## Exercises with solutions

**Exercise 1.** Let \(K\) act freely and properly on a second countable locally compact Hausdorff space \(P\). Check every equivalence condition for the space \(P\) between \(P\rtimes K\) and the unit groupoid \(P/K\). Explain why freeness cannot be omitted.

**Solution.** Use the anchors \(\operatorname{id}_P,q\). Both are open and onto. The left action of \((x,k)\) is defined at \(k^{-1}x\) and sends it to \(x\); the right action at \(q(z)\) fixes \(z\). They commute because the quotient is constant on the left orbits. The left action-relation map identifies with \((k,z)\mapsto(kz,z)\), so it is proper by hypothesis and injective by freeness. The right map is the closed diagonal, hence proper and free. Right orbits are singleton points, yielding \(P\); left orbits yield \(P/K\) with exactly the quotient topology. If \(k\ne e\) fixes \(z\), the non-unit arrow \((z,k)\) fixes \(z\), violating freeness of the left groupoid action. For a one-point space with a nontrivial finite group, the crossed product is \(C^*(K)\), whose distinct irreducible blocks prevent Morita equivalence to \(\mathbb C\). This also shows the algebraic consequence of the omitted hypothesis.

**Exercise 2.** For an equivalence of étale groupoids with counting Haar systems, write the four formulas (15.10) as sums and verify the imprimitivity identities.

**Solution.** First both anchors of \(Z\) are local homeomorphisms. For \(r_Z\), choose a neighborhood \(V\) of \(z\) whose equal-range division arrows all lie in the open unit space of \(\mathcal H\). Formula (15.3) then forces two equal-range points of \(V\) to coincide. The open anchor is thus a homeomorphism of \(V\) onto its open image. Use \(\mathcal G\) similarly for \(s_Z\). The cross-fibre measures (15.7) are consequently counting measures.

Replace each integral in (15.10) by a sum over the specified range fibre. For compact patch supports only finitely many terms occur at a fixed arrow, since the fibres are discrete and Hausdorff. In the linking algebra let \(\xi,\eta,\zeta\) denote the upper-right kernels. Directly,
\[
 \begin{aligned}
 \langle\xi,\eta b\rangle_{\mathcal H}
     &=\xi^**(\eta*b)=(\xi^**\eta)*b,\\
 \langle\xi b,\eta\rangle_{\mathcal H}
     &=(\xi*b)^**\eta=b^**(\xi^**\eta),\\
 {}_{\mathcal G}\langle f\xi,\eta\rangle
     &=(f*\xi)*\eta^*=f*(\xi*\eta^*),\\
 {}_{\mathcal G}\langle\xi,\eta\rangle\zeta
     &=(\xi*\eta^*)*\zeta=\xi*(\eta^**\zeta).
 \end{aligned}
 \tag{15.40}
\]
Associativity here is the finite-sum change of variables proved in Lesson 14; every product has matching corner types. Taking adjoints gives conjugate symmetry of both forms and the corresponding identities in the other variable. Linearity follows term by term. Lemma 15.2 and Theorem 15.3 supply positivity and fullness in the full completion and its reduced quotient, so all completed imprimitivity axioms hold. Pointwise nonnegativity of a sum has not been used as a substitute for C*-positivity.

**Exercise 3.** Construct the equivalence in (15.36), including its topology and generator relation.

**Solution.** For \(\varphi(z)=z+\theta\), use \(Z=\mathbb R\times\mathbb T\), anchors
\(r_Z(t,z)=(t\bmod1,z+\theta t\bmod1)\) and \(s_Z(t,z)=z\).
The left flow arrow of time \(s\) adds \(s\) to \(t\). A right arrow of time \(n\) and target \(z\) sends \((t,z)\) to \((t+n,z-n\theta)\); its range anchor is unchanged. Equal-range points differ by exactly one such integer, and equal-source points by exactly one real-time left arrow. Thus the division maps are continuous in the quotient charts and the action-relation maps identify with closed anchor fibre products. The two anchors are open, so the orbit identifications are homeomorphisms. Haar measures are \(dt\) and counting measure. Applying (15.22) and (14.16) proves (15.36). Pullback by the inverse rotation sends \(v(z)\) to \(e^{-2\pi i\theta}v(z)\); the covariance relation therefore gives exactly (15.37), with no extra \(2\pi\) in the integer return time.

**Exercise 4.** For compact \(P\) and a homeomorphism \(\varphi\), prove the suspension Morita equivalence and deduce the PV sequence. Determine its K-groups when \(\varphi=\operatorname{id}\).

**Solution.** The deck action in (15.31) is free and proper by the bounded-real-coordinate argument. The bibundle (15.32), with the two actions just computed, has open anchors and the principal division maps (15.25). The reduction has the product topology of \(P\rtimes\mathbb Z\), with counting Haar system. The full and reduced conclusions are (15.34).

The function identification in (15.38) gives the evaluation extension. Its connecting map is \(\alpha_*^{-1}-1\); applying the target automorphism \(\alpha_*\) gives \(1-\alpha_*\). Thom shifts parity, and the imprimitivity module gives the other K-theory isomorphism. Transporting the extension's exact cycle gives (15.39); the canonical suspension comparison specified above identifies its two middle maps with \(i_*\). This records the additional prerequisite needed for those named arrows.

If \(\alpha=1\), Lesson 5 gives \(B=A\otimes C(\mathbb T)\). Evaluation on the circle has the constant-function section and kernel \(SA\). Its split six-term sequence and the positive suspension isomorphism yield
\[
 K_i(B)\cong K_i(A)\oplus K_{i-1}(A),\qquad i\in\mathbb Z/2.
 \tag{15.41}
\]
In particular \(P=\mathbb T\) gives \(\mathbb Z^2\) in each parity. This calculation uses the split circle extension and remains valid when the K-groups have torsion.

**Exercise 5 (advanced).** Explain why every locally compact group, viewed as a one-unit groupoid, is inner exact, and why this does not imply exactness of its crossed-product functor.

**Solution.** The only open invariant unit sets are empty and the singleton. Their restriction sequences are respectively the identity quotient sequence and the identity inclusion sequence, hence are exact. For a discrete group, a trivial coefficient action has reduced crossed product \(B\otimes C_r^*(G)\), as proved in Lesson 2. Exactness of the crossed-product functor would therefore imply tensor exactness of \(C_r^*(G)\). The group constructed in Lesson 2 has a nonexact reduced group algebra, yet its one-unit groupoid is inner exact by the first argument. Theorem 15I.1 preserves the latter restriction property; it does not identify it with the stronger coefficient-functor property. ∎

## What this lesson does not prove

The dense-domain disintegration theorem, with its inductive-limit continuity, adjoint and dense essential-range hypotheses, is proved in Lesson 14, “The full norm and disintegration,” including all six construction subsections. [Muhly–Williams, *Renault's equivalence theorem for groupoid crossed products*, Theorem 7.8, pp. 45–46, and Proposition 7.6, p. 45] remains the precise historical statement and proof credit. We used it for the full corner's induced representations. The reduced corner calculation used the explicit fibre unitaries instead.

The Hausdorff inner-exactness theorem is proved here by tracking restricted linking corners and their quotient kernels.

We also use the verified Hilbert-module prerequisites: complementary full corners give an imprimitivity module *Imprimitivity bimodules and Morita equivalence*, Theorem 5.1; quotient modules have null submodule \(\overline{EI}\) and the quotient inner product *The Rieffel correspondence and induced representations*, Lemma 1.1 and Proposition 2.2. Those general operator-module proofs are supplied by the indicated lessons.

Haar-system existence for an abstract Hausdorff reduction uses Williams's Theorem 2.1. The theorem here assumes a supplied full Haar system on each side in the locally Hausdorff case. It proves Morita equivalence, without claiming a literal algebra isomorphism or reproving the stable-isomorphism theorem.

Morita invariance of K-theory is proved in the written programme lesson *Morita invariance of K-theory and maps induced by correspondences*, Corollary 2.2 and Theorem 5.1. The second countable locally compact suspension spaces give separable, hence sigma-unital, algebras, as required by that proof. The Connes–Thom and mapping-torus boundary results are proved in Lessons 10–11. The canonical PV coefficient maps use the written Fourier-window proof identified above. The classical circle K-groups used in the numerical example are the same Bott prerequisite as in Lesson 11.

## References

- Y. Li, [*Groupoid C*-algebras*](https://ncg-leiden.github.io/groupoid2022/groupoid_notes.pdf), version 7 February 2024, §3.2, §4 and §5, especially the linking construction on pp. 24–26.
- A. Sims and D. P. Williams, [*Renault's equivalence theorem for reduced groupoid C*-algebras*](https://www.aidansims.com/papers/SWi2010.pdf), arXiv:1002.3093v1, 2010. Linking Haar system: Lemmas 3–4, pp. 4–5; reduced corners: Theorem 13, pp. 9–10; full corners and regular-kernel compatibility: Proposition 15 and Theorem 17, pp. 10–12.
- P. S. Muhly and D. P. Williams, [*Renault's equivalence theorem for groupoid crossed products*](https://nyjm.albany.edu/m/2008/3p.pdf), New York Journal of Mathematics Monographs 3, 2008. Non-Hausdorff support tools: Lemmas 2.10–2.15, pp. 10–12; orbit averaging: Proposition 2.16 and Corollary 2.17, pp. 12–14; approximate identities: Proposition 6.8, pp. 38–42; disintegration: Theorem 7.8.
- D. P. Williams, [*Haar systems on equivalent groupoids*](https://arxiv.org/pdf/1501.04077), 2016, Theorem 2.1, p. 2.
- R. Meyer, *Actions of higher categories on C*-algebras*, in *Topics in Noncommutative Geometry*, Clay Mathematics Proceedings 16, 2012, §§3.1–3.3, pp. 85–89. This gives the correspondence viewpoint and Morita equivalences; the convolution proof above supplies the groupoid analytic details. [Electronic volume](https://www.claymath.org/wp-content/uploads/2022/03/cmip016c.pdf).
- A. Connes, [*Noncommutative Geometry*](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf), 1994, Chapter II, §7, Proposition 1, p. 117, for free proper actions; §§5 and 8, pp. 106–107 and 123–124, for smooth groupoids and transverse geometry.
- J. Rosenberg, *Examples and applications of noncommutative geometry and K-theory*, in *Topics in Noncommutative Geometry*, 2012, §§1.1–1.3 and §2.5, pp. 94–99 and 108. [Electronic volume](https://www.claymath.org/wp-content/uploads/2022/03/cmip016c.pdf).
- *Imprimitivity bimodules and Morita equivalence*, Theorem 5.1; *The Rieffel correspondence and induced representations*, Lemma 1.1 and Proposition 2.2.

- S. M. LaLonde, [*On some permanence properties of exact groupoids*](https://arxiv.org/abs/1703.05190v3), revised author manuscript 2018; published 2020.

