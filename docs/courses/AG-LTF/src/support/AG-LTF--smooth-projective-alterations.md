# Smooth projective alterations

*Expository proof written by GPT-6.1 Sol (OpenAI) in Codex at Ultra, October 2026. Original exposition is CC0. Linked human and AI Integrated Stacks proof components retain their own notices and terms.*

We construct the smooth projective alteration needed to pass from projective purity to smooth-proper purity over a finite field. The construction retains a boundary divisor during dimension induction, extends an actual labelled curve family, resolves its monomial nodes by global blowups, and descends finite algebraic data. Every alteration used for the rational cohomological splitting is generically separable.

## 1. The alteration and boundary assertions

**Theorem 1.1.** Let \(X_0\) be a smooth proper geometrically integral \(d\)-fold over a finite field \(k\). There exist a finite extension \(k'/k\), a smooth projective geometrically integral \(Y_0/k'\), and a proper dominant generically finite, generically separable morphism
\[
g:Y_0\longrightarrow X_0\times_k k'.
\tag{1.1}
\]

Generic separability permits a dense open over which \(g\) is finite étale. No restriction that its degree be prime to \(\ell\) is needed for the rational \(\ell\)-adic application: every positive integer degree is invertible in \(\mathbf Q_\ell\).

The route below strengthens (1.1) during induction. Over an algebraically closed field, for every projective integral \(W\) and proper closed subset \(B\), we prove the existence of a smooth projective alteration \(W'\to W\), generically separable, such that the reduced inverse image of \(B\) is a strict normal-crossing divisor. That boundary condition is needed at dimension \(d-1\) to resolve the nodal family at dimension \(d\). We preserve this assertion for pairs throughout the induction.

## 2. A projective modification of a proper integral variety

Let \(X\) be proper and integral over a field. Choose finitely many nonempty affine opens \(U_i\) covering \(X\), and closed embeddings \(U_i\hookrightarrow\mathbf A^{N_i}\hookrightarrow\mathbf P^{N_i}\). Their coordinate functions are rational functions on \(X\), giving rational maps \(\phi_i:X\dashrightarrow\mathbf P^{N_i}\). On the nonempty common open \(U=\bigcap_iU_i\), take their combined graph. Let \(G\) be its reduced closure in
\[
X\times P,\qquad P=\prod_i\mathbf P^{N_i}.
\tag{2.1}
\]
Then \(G\) is integral and \(G\to X\) is proper and birational.

The projection \(G\to P\) is quasi-finite. For a geometric point \(z=(z_i)\) of \(P\), a point of its fibre whose image \(x\) belongs to \(U_i\) must satisfy \(\phi_i(x)=z_i\). The graph equality holds on all of \(G|_{U_i}\), since \(\phi_i\) is defined there and its graph is closed. Its restriction to \(U_i\) is an embedding, so at most one \(x\in U_i\) is possible. Each pair \((x,z)\) gives at most one underlying point of the closed graph. The finite cover by the \(U_i\) therefore bounds the number of geometric points in every fibre. A finite-type zero-dimensional fibre is a finite scheme. Thus the projection is quasi-finite.

It is also proper, since \(G\) is closed in the proper \(X\times P\) over \(P\). Proper quasi-finite morphisms are finite. A finite scheme over a projective scheme is projective: the pullback of an ample bundle is ample, and the scheme is proper. Consequently \(G\) is projective over the field. This proves the particular Chow modification needed here, using only graph closure, proper quasi-finite finiteness and the ample finite-pullback criterion. It does not assert that \(G\) is regular.

Normalize \(G\); normalization is finite for varieties over a field, so the result is still projective and the map to \(X\) remains birational. One algebraic justification for the finiteness, in the perfect-field case after an algebraic closure, is to choose a separating finite Noether normalization. The integral closure of the polynomial ring in the finite separable function field is contained in the trace-dual finite module of an integral field basis. Since that polynomial ring is Noetherian and normal, the integral closure is finite. This also makes the normalization of the intermediate finite algebra finite.

If a boundary \(B\) is prescribed, blow up its ideal before normalizing. The inverse-image ideal is then invertible. On an integral dominant source its nonzero local generator is a nonzero divisor, so its support is an effective Cartier divisor. These operations are projective and birational, hence generically separable. They reduce the pair problem to a normal projective variety with a boundary supported on a Cartier divisor.

## 3. Two algebraic constructions used in the induction

**Projective graph flattening.** Let \(Q\to S\) be projective, with \(S\) integral, and let \(Q_U\) be flat over a dense open \(U\subset S\), with one Hilbert polynomial \(P\). Its identity closed family in \(Q_U\) defines a map
\[
U\longrightarrow\operatorname{Hilb}^{P}_{Q/S}.
\tag{3.1}
\]
The Hilbert theorem makes that parameter scheme projective over \(S\). Let \(S'\) be the reduced closure of the image of \(U\). It is integral, projective over \(S\), and isomorphic to \(U\) over that open: the section's graph is closed there. Thus \(S'\to S\) is a modification. The universal Hilbert family over \(S'\) is the strict transform of the generic family and is flat.

For clarity, this last equality is scheme-theoretic. The universal family agrees with the given family over \(U\). Flatness over an integral base makes multiplication by every nonzero base element injective in its structure sheaf. It has no extra subsheaf supported over the complement of \(U\), so it equals the schematic closure of that generic family. This is precisely the saturation defining strict transform. Several projective families can be flattened simultaneously by the closure of their common section in a product of the fixed-polynomial Hilbert schemes.

Normalization of \(S'\) preserves flatness by base change. For the integral strict transform it is harmless to replace it by the generic-component closure: in the applications below the geometric generic fibre is integral and the smooth locus meets every fibre component. Dimensions remain one, because the strict transform is contained in a base change all of whose fibres have dimension one, and dimension theory for varieties gives the opposite lower bound. Its nonsmooth locus is contained in the pullback of the original finite relative nonsmooth locus; hence the smooth locus remains dense in each fibre component.

**Constants and connected fibres for a normal curve fibration.** Suppose \(Q\) is normal and projective, \(Q\to S\) is proper, every fibre is a curve, and the smooth locus meets every component of every fibre. Suppose the generic fibre is smooth. Let \(L\) be the algebraic closure of \(k(S)\) inside \(k(Q)\), and let \(S_1\) be the normalization of \(S\) in \(L\). This is finite, with separable generic field extension, and \(Q\to S\) factors through \(S_1\). Indeed its integral functions in \(L\) belong to the normal local rings of \(Q\). Proper coherent finiteness identifies \(S_1\) with \(\operatorname{Spec}_S(f_*\mathcal O_Q)\): both algebras are the integral closure of the base in the generic constant field.

When \(S\) is smooth, \(S_1\to S\) is étale in this situation. At each point of \(S_1\), choose a smooth point of a fibre component above it. A smooth morphism has a section through that point after an étale neighbourhood of the base. Composing with \(S_1\) gives a section of its finite normal base change. A section chooses a component birational to that normal étale neighbourhood; a finite birational map to a normal scheme is an isomorphism. Normal components are disjoint, so this component is an open local branch. The finite map is therefore étale at the selected point. Such points cover \(S_1\).

The induced proper map \(Q\to S_1\) has geometrically connected fibres. Here is the needed connectedness argument without applying the flat Stein theorem. After completion of a strict local base, flat coherent base change still gives global function algebra equal to that local base. If its geometric special fibre were disconnected, the complete-local proper finite étale lifting theorem would lift the open-and-closed decomposition to the whole proper scheme. It would give a nontrivial idempotent in its local global function ring, a contradiction. Purely inseparable residue-field enlargement does not change the underlying point space. This proves geometric connectedness. The same completion argument proves connected fibres over a normal point for any proper birational map whose source is integral: its finite constant factor is the normalization of that normal point and hence is the point itself.

These are the exact versions used below. Flatness and geometric reducedness have not been retroactively asserted for the original fibration.

## 4. Producing the curve fibration and enough marked points

Work over an algebraically closed field \(K\), and let \(W\) be normal projective of dimension \(d\ge2\), with Cartier boundary \(B\). Choose a sufficiently ample embedding. General linear projection gives a finite morphism
\[
\pi:W\longrightarrow\mathbf P^d
\tag{4.1}
\]
which is étale on a dense open and whose restriction to each boundary component is generically birational onto its image. The projection conditions can be checked by the usual incidence argument: avoidance of \(W\) at infinity gives finiteness; the differentials of the embedding coordinates span the generic cotangent space, so a general \(d\)-tuple has full rank; for a \((d-1)\)-dimensional boundary component the pair-incidence condition in a projection to dimension \(d\) confines double points to a smaller-dimensional locus. These are nonempty open conditions, and there are finitely many boundary components.

Choose a general point \(p\in\mathbf P^d\) outside the branch locus and \(\pi(B)\), also avoiding the generic tangent-incidence conditions for the finitely many boundary images. The induced projection of each boundary image to \(\mathbf P^{d-1}\) then has full generic differential rank. Blow up the finite smooth set \(\pi^{-1}(p)\). Projection along the lines through \(p\) gives
\[
f:W_1\longrightarrow\mathbf P^{d-1}.
\tag{4.2}
\]
Every fibre is nonempty and equidimensional of dimension one. It is finite over the corresponding line away from the exceptional charts, so has dimension at most one; the \(d-1\) defining equations give dimension at least one. Every component maps onto the line and meets \(\pi^{-1}(p)\). Near those points \(\pi\) is étale, and the blown-up projection is the standard smooth line fibration near its exceptional section. Thus the smooth locus of \(f\) is dense in every fibre component.

The generic fibre can be made smooth. A normal variety has singular locus of codimension at least two. General curve sections avoid that locus by the point-incidence dimension count, and are smooth on its smooth complement by the tangent-incidence count. The latter only needs a sufficiently ample embedding separating first jets, the same concrete Bertini mechanism used in Lesson 9. Choose the projection centre and a line fibre from that open incidence set. Properness then gives smoothness over a dense open of the base. Replace the base by its finite constant factor in §3. It is still smooth and projective, and the fibre is now geometrically connected. The Cartier boundary maps finitely to the base and is generically étale, by its adapted projection.

We need markings meeting every fibre component at at least three distinct smooth points. Let \(\mathcal L\) be very ample on \(W_1\), and use \(\mathcal L^N\). Any integral fibre component has at least \(N+1\) linearly independent restrictions of sections: a basepoint-free pencil for \(\mathcal L\) restricts to a nonconstant rational parameter, whose first \(N+1\) powers are independent. Thus hyperplanes containing that component have codimension at least \(N+1\) in the parameter space. The incidence of a hyperplane containing any fibre component is closed, by proper fibre-dimension upper semicontinuity. Its dimension is at most parameter dimension plus base dimension minus \(N+1\). Taking \(N\) larger than the base dimension produces a hyperplane avoiding every component, so its intersection divisor is finite over the base.

At any selected closed base point we can also avoid the finite nonsmooth set and intersect the smooth curve loci transversely. These are open conditions. The resulting divisor is finite étale near that base point and meets each component in at least \(N\ge3\) distinct smooth points. Repeat at points outside the opens already covered. Quasi-compactness gives finitely many such divisors; choose them with distinct generic components. Their union is a finite generically étale divisor satisfying the three-point condition everywhere. Enlarge \(B\) by it.

Take the normal base cover for a finite separable Galois field extension splitting all the finite boundary-component fields. Its reduced inverse boundary is a union of sections: every component is finite and birational to the normal new base, hence is that base. The sections may meet at exceptional parameters, but on a dense open they are mutually disjoint. The three distinct smooth points on every geometric fibre are retained by this base change. Use the strict generic-component transform of \(W_1\); the finite relative nonsmooth locus and dimension-one argument in §3 preserve the required fibre properties.

## 5. Extending the stable pointed family

The required curve extension is proved in Stable pointed-family extension, using a tricanonical stable-curve atlas, its properness, an invertible level structure and a projective separable cover. We record its precise form.

**Theorem 5.1 (stable pointed-family extension).** Let \(K\) be algebraically closed and \(S\) integral and projective over \(K\). A smooth proper geometrically connected genus-\(g\) family over a dense open \(U\subset S\), with \(n\ge3\) ordered disjoint sections, extends after a projective generically finite generically separable alteration \(S'\to S\) to a projective stable ordered \(n\)-pointed family over a normal integral projective \(S'\). After restricting the original dense open, the extension carries the actual identifying isomorphism to the pulled-back original family, including its labels.

The proof includes \(g=0\) and \(g=1\): attach fixed pointed elliptic tails to raise the unpointed genus to \(G=g+n\ge3\), extend that stable family, and recover the ordered core by partial normalization at the persistent attaching nodes and the finite étale component algebra. On the compact-type locus the normalized prime-level cover is finite étale. Normalize the base in a chosen separable lift field before taking the graph of its actual morphism to the level space; this retains the identifying arrow. A separable weak Chow construction produces the projective scheme cover. The resulting theorem requires neither a projective coarse moduli space with a postulated universal curve nor an everywhere finite projective fine cover of pointed moduli.

Apply Theorem 5.1 to the smooth marked generic family of §4, shrinking its comparison open so the labels are disjoint. We obtain an actual projective stable family \(C\to S'\) with the prescribed labelled generic isomorphism to the strict transform of \(Q\). Use that normal projective altered base as \(S\) in §6. All new extensions of the base function field are finite separable; the identifying isomorphism is part of the construction.

## 6. Extending the curve map: three markings prevent contraction

Suppose \(Q\to S\) is the marked model of §4 and \(C\to S\) is the stable curve furnished by Theorem 5.1, generically isomorphic to it with the labels matching. Let \(\Gamma\) be the reduced closure of the generic graph in \(C\times_SQ\). Using §3, modify and normalize \(S\) so that both \(Q\) and \(\Gamma\) are flat over \(S\). Continue with their strict transforms. They have pure one-dimensional underlying fibres; the smooth locus still meets every component of \(Q_s\).

The stable total space \(C\) is normal over this normal base. Flatness and the Cohen–Macaulay nodal fibres give Serre \(S_2\) by the flat local depth formula. In codimension one it is smooth over the regular codimension-one base: relative singular points lie over the degeneration locus and have codimension at least two in the total space; the generic fibre is smooth. Thus \(R_1\) holds, and Serre's criterion gives normality.

For each component \(A\) of a fibre of \(Q\), there is exactly one component of \(\Gamma_s\) dominating it. Choose a general smooth point on \(A\). The proper birational projection \(\Gamma\to Q\) is quasi-finite there: otherwise positive-dimensional inverse images over a dense subset of \(A\) would give a component of \(\Gamma_s\) of dimension at least two. The non-quasi-finite locus has closed image by properness, so the map is finite on a neighbourhood of the chosen point. That neighbourhood of \(Q\) is normal because it is smooth over the normal base. Finite birationality makes the map an isomorphism. This proves uniqueness. The same argument applies to every component of \(C_s\), since its general points are smooth over \(S\).

No component \(D\) of \(\Gamma_s\) can be contracted to a point \(c\in C_s\) while dominating a component \(A\subset Q_s\). Choose three distinct smooth marked points on \(A\). The inverse image of each marked point under \(\Gamma\to Q\) is connected, by the proper birational normal-point argument of §3, and meets \(D\). It also contains the labelled point on the generic graph's closure. Its image in \(C_s\) therefore connects \(c\) to that label. If \(c\) is different from all three labels, the three connecting curves have different components through \(c\): otherwise uniqueness of the component of \(\Gamma_s\) dominating that component of \(C_s\) would make the inverse images of two distinct marked points meet. A nodal curve has at most two branches at a point, contradiction. If \(c\) equals one of the labels, the other two connecting curves give two branches at that labelled point. Stable labels lie in the smooth locus, again a contradiction.

Every positive-dimensional fibre of \(\Gamma\to C\) would contain such a contracted fibre component. Therefore the map is proper and quasi-finite, hence finite. It is birational and \(C\) is normal, so it is an isomorphism. The generic isomorphism has extended to an actual projective birational map
\[
C\longrightarrow Q.
\tag{6.1}
\]
In particular it is not merely a rational map to the original variety. This is the role of the three-point condition.

The inverse image of the Cartier boundary of \(Q\) is a divisor in \(C\). Its horizontal components are among the stable sections. Every remaining component maps into a proper closed subset of the base. Enlarge that base subset to include the degeneration locus and the images of all vertical boundary components. The boundary is now contained in the sections plus the inverse image of that base subset.

## 7. Completing the dimension induction

Apply the strengthened induction hypothesis to that projective base, whose dimension is \(d-1\), with its prescribed proper closed subset. Obtain a smooth projective altered base \(S_1\) and a strict normal-crossing divisor \(D\) containing the inverse image of the subset. The base alteration is generically separable. Pull back \(C\); it is still a stable, hence semistable, projective curve, smooth over \(S_1-D\), with disjoint sections in its relative smooth locus.

### 7.1. Inputs, boundary and local models

Let \(K\) be algebraically closed, \(S\) smooth projective over \(K\), and \(D\) a strict normal-crossing divisor on \(S\). Let \(f:C\to S\) be an integral projective semistable curve, with smooth generic fibre and smooth over \(S-D\). Include finitely many mutually disjoint stable marked sections in its relative smooth locus. Put

\[
E=\bigl(f^{-1}D\cup\text{marked sections}\bigr)_{\mathrm{red}}.
\tag{7.1}
\]

We construct a finite sequence of projective birational blowups whose source is smooth and whose reduced total inverse image of \(E\) is strict normal crossing. Any original effective Cartier boundary supported in \(E\) then pulls back to a union of components of that strict normal-crossing divisor.

At a closed node the completed local model is

\[
R=A[[u,v]]/(uv-\varepsilon\prod_{i=1}^{q}t_i^{a_i}),
\qquad a_i\ge0,
\tag{7.2}
\]

where \(A\) is a complete regular local base ring, the \(t_i\) are the distinct boundary parameters through the base point, and \(\varepsilon\) is a unit. Absorb \(\varepsilon\) into \(u\). The generic smoothness assumption makes the product nonzero. Parameters with exponent zero are retained as independent boundary coordinates. At a relative smooth point, the total space is regular and the boundary is locally the product of the base boundary parameters and, if a marked section is present, one additional fibre parameter.

The node has nonsingular polar form \(uv\) in every characteristic. Lifting its two coordinates and using flatness lifts its single equation; the formal implicit-function and hyperbolic splitting argument removes higher terms and gives \(uv-h\). The degeneration is contained in \(D\), so factoriality of the regular completed base ring gives the displayed monomial. We retain the regularity criterion by faithfully flat completion for varieties over a perfect field, blowup compatibility with flat base change, the completed normal-crossing criterion and étale descent of invariant coherent ideals. These are the local algebraic foundations retained in §9. Every blowup below is of a global coherent ideal; formal coordinates are certificates for its charts, not data to be glued into a new formal global scheme.

### 7.2. Removing the codimension-two singular components

For \(a_i\ge2\), the local codimension-two singular component has reduced ideal

\[
P_i=(u,v,t_i),\qquad R/P_i=A/(t_i).
\tag{7.3}
\]

Initially these are smooth global components: they lie in the finite relative nodal locus and, over the indicated smooth \(D_i\), their completed maps are the displayed base quotients. In particular a global component cannot combine the local ideals associated with two different global components of the strict divisor \(D\). Node sheets over a point are locally disjoint. Thus each reduced global codimension-two component has the completion \(7.3\), is regular at every closed point, and is smooth over \(K\). There are finitely many of them.

Choose one whole reduced global component \(T\) and blow its ideal. At a point of \(T\), its local ideal is \(7.3\). On the \(u\)-chart set \(v=uV, t_i=us\). The actual blowup chart is obtained by saturation, not by retaining an embedded exceptional factor:

\[
V=u^{a_i-2}s^{a_i}\prod_{j\ne i}t_j^{a_j}.
\tag{7.4}
\]

Eliminating \(V\) gives a regular chart with coordinates \(u,s\) and the other base parameters. Its reduced vertical boundary is the coordinate product

\[
u\,s\prod_{j\ne i}t_j=0.
\tag{7.5}
\]

The \(v\)-chart is symmetric. On the \(t_i\)-chart set \(u=t_iU, v=t_iV\); then

\[
UV=t_i^{a_i-2}\prod_{j\ne i}t_j^{a_j}.
\tag{7.6}
\]

Its boundary retains every \(t_j\), including \(t_i\) when its new exponent is zero. These presentations are the genuine charts: after substitution the old equation has a factor \(u^2\) or \(t_i^2\); division is justified by the saturation defining the Rees chart, and the displayed quotient is a domain, so there is no further torsion component.

The charts prove the following global induction statement. Other codimension-two singular components survive as their reduced strict transforms with unchanged exponent. They meet these charts only in the \(t_i\)-chart: on such a component the restriction of the centre ideal is the principal boundary ideal \((t_i)\), so its strict transform is unchanged locally. The chosen component has at most one replacement codimension-two singular component, with exponent \(a_i-2\); when that exponent is less than two there is no replacement. The regular \(u\)- and \(v\)-charts create none. The replacement, when present, again has a regular base-quotient completed local ring and is smooth. Consequently the same assertion applies at the next step without choosing a node branch.

At the generic point of a global codimension-two component \(T\), the order \(a(T)\) of the smoothing parameter along its base divisor is well defined. Changing a boundary equation by a unit or exchanging \(u,v\) does not change it. The local monomial model shows the same order at all points of that sheet. The nonnegative integer

\[
\Phi=\sum_{T\subset\operatorname{Sing}(C),\ \operatorname{codim}T=2}
\left\lfloor\frac{a(T)}2\right\rfloor
\tag{7.7}
\]

decreases by exactly one at every chosen blowup: either the replacement order drops by two or a component of order two or three disappears. Other summands are unchanged and no new summand occurs in the regular charts. Hence this phase terminates. On its possibly singular charts all positive exponents are now one; already regular charts have normal-crossing boundary and need no further singular-locus blowup.

This first phase also preserves the semistable curve structure over \(S\). On the \(u\)-chart its structural equation over the base is \(us=t_i\), with the other base coordinates unchanged; on the \(t_i\)-chart it is (7.6). Both are the usual flat nodal equations: the algebra \(A[p,q]/(pq-h)\) is free as an \(A\)-module with basis \(1,p,p^2,\ldots,q,q^2,\ldots\), and its fibres are a smooth hyperbola or two reduced transverse lines. The analogous completed-local flatness criterion gives the same conclusion for the completed charts. Thus, at the start of the next phase only, the finite relative nodal locus and its base-intersection quotients remain available. No such relative-curve assertion is propagated through the next phase.

### 7.3. The squarefree phase: intrinsic centres and exact chart transition

The remaining singular charts have the form

\[
UV=x_1\cdots x_r,\qquad r\ge2,
\tag{7.8}
\]

with additional independent regular parameters \(z_1,\ldots,z_b\). The reduced vertical boundary has equation

\[
\prod_{i=1}^{r}x_i\prod_{\nu=1}^{b_0}z_\nu=0;
\tag{7.9}
\]

the remaining \(z\)'s are not boundary parameters. The reduced singular locus is the union of the smooth local components

\[
F_{ij}=(U,V,x_i,x_j),\qquad 1\le i<j\le r.
\tag{7.10}
\]

Indeed outside \(U=V=0\) the equation can be eliminated, and at \(U=V=0\) it is singular exactly when at least two distinct \(x_i\)'s vanish. This criterion is valid in every characteristic. At the beginning of this phase, the components \(7.10\) are smooth global components by their base-intersection quotients in the semistable charts. Thereafter their smoothness and local identity will be proved by strict transforms, not by finiteness over the original base.

Inductively maintain this statement: every remaining reduced global singular component is smooth and has at each of its points exactly one local ideal \(7.10\); each chart's distinct pairs identify distinct global components through that point. The charts are either regular with normal-crossing boundary or of the form \(7.8\)-\(7.9\). Choose one whole reduced global singular component \(F\). Near a point of \(F\), renumber so that its ideal is \(F_{12}\), and blow it.

On the \(U\)-chart put

\[
V=U V_0,\quad x_1=U s_1,\quad x_2=U s_2.
\]

After saturation,

\[
V_0=s_1s_2x_3\cdots x_r.
\tag{7.11}
\]

This chart is regular by eliminating \(V_0\). Its reduced boundary is exactly

\[
U s_1s_2x_3\cdots x_r\prod z_\nu=0.
\tag{7.12}
\]

The \(V\)-chart is symmetric. On the \(x_1\)-chart put

\[
U=x_1U_1,\quad V=x_1V_1,\quad x_2=x_1s_2;
\qquad U_1V_1=s_2x_3\cdots x_r.
\tag{7.13}
\]

This has \(r-1\) active factors \(s_2,x_3,\ldots,x_r\). Its reduced boundary contains those factors, every old inactive boundary coordinate, and the additional inactive coordinate \(x_1\). The \(x_2\)-chart is symmetric, with active factors \(s_1,x_3,\ldots,x_r\) and additional inactive coordinate \(x_2\). Saturation is justified as in the first phase.

The pair-to-component identifications are explicit. In the \(x_1\)-chart,

\[
\begin{array}{c|c}
\text{new singular pair}&\text{old component whose strict transform it is}\\\hline
(s_2,x_j),\ j\ge3&F_{2j}\\
(x_i,x_j),\ 3\le i<j&F_{ij}.
\end{array}
\tag{7.14}
\]

In the \(x_2\)-chart, \((s_1,x_j)\) instead identifies \(F_{1j}\), and the pairs with both indices at least three still identify \(F_{ij}\). These identifications follow on the dense complement of the centre, where the blowup is an isomorphism, and hence identify the reduced strict transforms. There are no singularities in the \(U,V\)-charts. Thus the selected \(F_{12}\) disappears; every other old component persists somewhere as its strict transform; no new singular component is introduced. The assignments within each chart are injective, so no old component acquires two local branches at one point.

For completeness, smoothness can also be checked directly on the strict transforms. Restrict the centre ideal to another old component. On \(F_{1j}\) it is \((x_2)\); on \(F_{2j}\) it is \((x_1)\); on \(F_{ij}\) with \(i,j\ge3\) it is \((x_1,x_2)\). These are respectively an effective coordinate divisor or a smooth coordinate intersection in the regular component. Off the centre the restricted ideal is the unit ideal. The strict transform of an integral component not contained in the centre is its blowup along this restricted ideal: the Rees-algebra quotient embeds that blowup in the ambient blowup, and its dense unchanged complement has precisely the strict-transform closure. Blowing a regular scheme along one or two coordinate parameters stays regular, as its affine charts show. Consequently every remaining global component is again smooth. Its intersections with future centres have the same coordinate description in the new charts. This proves the induction statement for successive steps.

There are finitely many global singular components. Every step deletes the chosen component and replaces each other component by one irreducible strict transform: irreducibility follows by closing its integral unchanged dense complement. No component is wholly contained in a distinct chosen component because both have codimension three. By \(7.14\) there are no additional singular components. Therefore their number decreases by exactly one and this phase terminates.

At termination the remaining monomial charts have either no active factor or one. With no active factor \(UV=1\), both variables are units and the boundary is the inactive coordinate divisor. With one active factor \(UV=x\), eliminate \(x\); the reduced boundary is \(UV\prod z_\nu=0\), a coordinate divisor in the regular coordinates \(U,V,z_\nu\). Together with \(7.12\) and the regular charts from the first phase, this proves regularity and ordinary normal crossings everywhere.

### 7.4. The four-factor example and why the base quotient is not preserved

Take \(uv=t_1t_2t_3t_4\) over \(\mathbf A^4_{t_1,t_2,t_3,t_4}\), and blow \(F_{12}\). The \(t_1\)-chart is

\[
u'v'=s_2t_3t_4,\qquad t_2=t_1s_2.
\tag{7.15}
\]

The strict transform of \(F_{34}\) has ideal \((u',v',t_3,t_4)\); its coordinates are \((t_1,s_2)\). Its map to the original \(D_3\cap D_4\) is \((t_1,s_2)\mapsto(t_1,t_1s_2)\). The symmetric \(t_2\)-chart glues to it as \(\operatorname{Bl}_0\mathbf A^2_{t_1,t_2}\), with fibre \(\mathbf P^1\) at the origin. It is smooth but is not finite or unramified over that original intersection. It is nevertheless a valid next centre: its current completed ideal is one pair ideal \(7.10\) in the model \(7.15\), and its intersections with other remaining centres are the coordinate intersections established above. The proof never requires the modified total space to retain one-dimensional fibres over the original \(S\).

### 7.5. Global gluing and exchange of the two node branches

All centres are reduced closed global components of the intrinsic singular locus, or reduced strict transforms of those components; they are not assembled by choosing a \(u\)-branch. Initially the relative nodal ideal is \((u,v)\), intrinsically the appropriate Fitting ideal of the relative differentials. The ideals \((u,v,t_i)\) and \((u,v,t_i,t_j)\) are unchanged when the two node branches are exchanged, when their equations are multiplied by units, or when boundary labels are permuted. At later steps the centre is intrinsic as a global strict transform and the charts identify its completed ideal uniquely. A node-branch exchange interchanges the \(U,V\)-charts; the \(x_1,x_2\)-charts and pair identifications are compatible with that exchange.

An étale splitting cover may split one global centre into several disjoint local sheets; the pullback of its global ideal is the ideal of their union, so the global blowup pulls back to the same local blowup. Every chart comparison is a flat base change of this already defined algebraic blowup. The completion of each reduced centre is the displayed regular coordinate quotient; no completed branch is arbitrarily selected. Smoothness, chart identities and the stated intersections can thus be tested at all closed points after faithfully flat completion. Excellence and the smooth local descriptions ensure the reduced structures have exactly these completed ideals. Because every closed point is covered, regularity and the reduced boundary criteria hold globally. No assertion of finite nodal sheets is made after the squarefree singular-component blowups begin.

All singular-locus centres are smooth over \(K\) and contained in the singular locus. Their boundary compatibility is the explicit monomial coordinate compatibility above; a regular immersion into the singular total space is not needed for its Rees blowup. The ordinary smooth-centre normal-crossing condition applies to the boundary-refinement phase below, once the ambient total space is regular.

### 7.6. From normal crossings to strict normal crossings

Here is the elementary coordinate fact needed for the global centres. Write \(Z_J=(t_j:j\in J)\) for a coordinate intersection. Blow a larger coordinate intersection \(Z_L\), and on its \(k\)-chart write \(t_l=t_k s_l\) for \(l\in L-\{k\}\). If \(k\in J\), the strict transform of \(Z_J\) is empty in this chart: its unchanged dense complement outside the centre has zero \(k\)-th homogeneous blowup coordinate. If \(k\notin J\), its strict-transform ideal is \((s_j:j\in J\cap L)+(t_j:j\in J-L)\), a coordinate ideal of the same codimension. Thus surviving original intersections remain coordinate intersections under every earlier larger-intersection blowup. Two distinct \(r\)-fold intersections meet in their union-index intersection of size greater than \(r\). Blowing that intersection separates them: their normal directions over it use respectively the disjoint index sets \(J'-J\) and \(J-J'\), so their projectivized normal directions cannot meet. Earlier larger faces satisfy the same coordinate rule, and subsequent blowups cannot make disjoint strict transforms meet again. This proves the separation and smoothness claim used below, without assuming global branch labels.

Let \(X\) be the regular output and \(E_X\) its ordinary normal-crossing reduced boundary. In an étale splitting chart its local branches have equations \(t_1,\ldots,t_m\). For each \(r\ge2\), let \(Z_r\) be the reduced locus where at least \(r\) original local branches meet. Locally its ideal is the intersection of the coordinate ideals \((t_j:j\in J)\) for all \(r\)-element subsets \(J\). This construction is invariant under permutation and unit changes of the local branch equations and therefore descends to a global reduced closed ideal. It does not require globally distinct labels for the original branches.

Starting with the largest possible number of branches, blow the reduced strict transform of \(Z_r\), in descending order \(r=m_{\max},\ldots,2\). At the stage for \(r\), its local pieces are the strict transforms of the original \(r\)-fold coordinate intersections. Two distinct such pieces can only have met in an intersection of more than \(r\) original branches, already blown. The coordinate blowup calculation separates them there. Thus they are now disjoint and smooth; their union is a smooth global centre, with normal crossings with the current coordinate boundary. An empty centre is skipped.

The complete local coordinate verification of this claim is the successive subdivision of the positive orthant along all coordinate faces in descending dimension. The final charts are indexed by permutations \(\sigma\) of the \(m\) original branches and satisfy

\[
t_{\sigma(j)}=y_jy_{j+1}\cdots y_m,
\qquad 1\le j\le m.
\tag{7.16}
\]

It follows by the ordinary blowup chart rule: blowing an intersection divides all but the chosen exceptional coordinate by that coordinate; descending through the faces produces a nested chain of subsets. Reversing those divisions gives \(7.16\). It also verifies at each stage that the remaining equal-size face centres are separated and regular. Other parameters are unchanged, and the transformed reduced boundary is \(y_1\cdots y_m=0\).

The ray \(y_j=0\) corresponds to the nested subset \({\sigma(1),\ldots,\sigma(j)}\), whose cardinality is \(j\). A final chart contains at most one branch of each cardinality. Cardinality is preserved under all changes of branch-splitting chart. Exceptional components introduced at distinct stages have distinct cardinalities; cardinality one refers to original strict transforms. Consequently two local branches of the same global component cannot meet. Every global component is smooth, and intersections of distinct global components are smooth with the coordinate expected codimension. This is strict normal crossing. Marked sections and vertical components are treated as branches of the same divisor: the sections were disjoint, smooth and transverse to the vertical coordinate boundary before this refinement, since the singular-locus blowups were disjoint from their neighbourhoods.

### 7.7. Projectivity, birationality and the exact induction output

Each centre is a proper closed coherent subscheme, and each operation is its algebraic Rees blowup. Every operation is projective and is an isomorphism on the dense generic smooth comparison open. Hence the composite is projective and birational. The source remains integral, since the Rees algebra is a subalgebra of the polynomial ring over an integral scheme. It is regular after the singular phases and stays regular under the smooth coordinate boundary blowups; over the perfect field \(K\) it is smooth. Projectivity over the projective \(S\) makes it projective over \(K\). Birationality changes no function field, so this resolution introduces no inseparable extension.

An original nonzero effective Cartier boundary remains Cartier on the integral dominant source. Its support has pure codimension one and is contained in the transformed boundary, so it is a union of components of the strict normal-crossing divisor just proved. This gives exactly the boundary assertion required by the dimension induction. Generic separability contributed by earlier base alterations is preserved: the generic curve was geometrically integral, and a finite separable extension of the base function field remains separable after compositum with its total function field; the resolution itself is birational. 

Combined with the preceding generically separable base covers and the curve map (6.1), these modifications give a smooth projective generically separable alteration of \(W\). The original boundary is a union of components of the final strict normal-crossing divisor, so the induction retains its stronger pair assertion.

The bases of induction require no stable-curve theorem. In dimension zero the variety is a point over the algebraic closure. In dimension one, normalization is regular, hence smooth over the perfect field; the projective modification of §2 is finite after normalization because a nontrivial fibre component would be the whole irreducible curve. Finite birationality onto the normal curve makes it an isomorphism. Thus the normal proper curve is projective, and its reduced point boundary is strict normal crossing.

## 8. Descent to a finite field and the purity consequence

Starting with \(X_0\) over a finite field \(k\), carry out the finite algebraic construction over \(\overline{k}\). The resulting finitely presented schemes and morphisms, their projective embeddings, the finitely many global coherent blowup ideals, and a chosen dense finite étale comparison open descend together to a single finite extension \(k'/k\), since these algebraic data use only finitely many coefficients. The formal coordinates and units used to check completed local charts are proof certificates and need not descend. Smoothness and geometric integrality of the descended source follow because its base change to \(\overline{k}\) has those properties. The descended projective embedding gives projectivity; properness and the finite étale comparison morphism descend by faithfully flat base change. Thus the descended morphism has positive finite generic degree and is generically separable, as required in \(1.1\).

The cohomological reduction is proved in The Riemann hypothesis over finite fields, Proposition 6.2 using Smooth traces, duality and Gysin maps. Over the algebraic closure, define \(g_*\) as the adjoint of \(g^*\) for the normalized perfect Poincaré pairings. On an open where \(g\) is finite étale of degree \(e\), its sheet trace composed with pullback is \(e\). The complements have dimension at most \(d-1\), so compact localization identifies their top compact groups with the proper top groups. Trace composition then gives \(g_*g^*=e\) in every degree, by testing cup products against complementary-degree classes. Thus \(H^i(X)\) is a Frobenius-power-stable direct summand of \(H^i(Y)\). Projective purity gives its eigenvalues' moduli, and finite-field descent removes the power. Components of different dimensions are handled separately after a finite field extension; degree-zero components have permutation cohomology.

The construction above supplies the smooth projective source required for this trace splitting. Its degree need not be prime to \(\ell\), because the splitting uses \(\mathbf Q_\ell\).

## 9. Proof scope and sources

The projective modification, strict-transform Hilbert flattening, marked curve fibration, graph extension, monomial resolution, strict-boundary refinement, pair induction and finite-field descent are proved above. Stable pointed-family extension gives the exact geometric curve extension used in §5, including genera zero and one. Its numerical and surface-model proofs retain their exact openly licensed source bodies and corrections in the accompanying supporting readings and editable sources.

The algebraic foundations used here are coherent proper finiteness and base change, finite normalization, finite-pullback ampleness, regular-local factoriality, flat depth and dimension formulae, formal functions, and the ordinary completion and Rees blowup criteria. [Hilbert and Quot schemes](course:AG-HP/hilbert-and-quot-schemes), Theorem 4.1 and Corollary 4.2, supplies the proved fixed-polynomial parameter scheme. [Proper fundamental groups](course:AG-DFG/proper-fundamental-groups), Theorem 2.1, supplies complete-local finite étale lifting. Lefschetz pencils and vanishing cycles, Theorem 1.0, contains the characteristic-sensitive generic section argument. These uses do not assume the alteration theorem being proved.

[A. J. de Jong, *Smoothness, semi-stability and alterations*](https://www.numdam.org/item/PMIHES_1996__83__51_0/), Theorem 4.1 and Remark 4.2, is the primary theorem comparison. Its §§2.19,2.24,3.2–3.5 and4.11–4.28 describe the flattening, stable-family, monomial and induction mechanisms. The exposition above supplies the actual arguments with the precise family-extension and global-centre corrections. No redistribution or relicensing of the human primary PDF is implied.
