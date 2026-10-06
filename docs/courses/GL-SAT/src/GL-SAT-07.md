# Convolution and rigidity

*Written by GPT-6.1 Sol (OpenAI), October 2026. Public domain (CC0).*

Convolution composes two modifications of a bundle. The intermediate bundle is part of the correspondence; forgetting it is a proper map. We construct that correspondence on finite schemes, prove the dimension estimate for every source stratum, and use it to prove that convolution preserves the perverse heart. We then construct duals by reversing framed modifications and prove both duality identities. None of these arguments assumes general IC parity or semisimplicity.

Work with a connected reductive group \(G/\mathbb C\) and a characteristic-zero coefficient field \(\Lambda\). Put \(O=\mathbb C[[t]]\), \(F=\mathbb C((t))\), \(K=L^+G\), and \(K_n=\ker(K\to J_nG)\). All sheaves have finite Schubert support. Write \(O_\lambda=\operatorname{Gr}^{\lambda}\), \(Z_\lambda=\overline{O_\lambda}_{\mathrm{red}}\), and \(d_\lambda=\langle2\rho,\lambda\rangle\).

The scheme inputs are Loop groups and the affine Grassmannian, Theorem 7.1 and §§2,4; Beauville–Laszlo gluing and the moduli interpretation, §§1–3,7–8; and Orbits and Schubert varieties, §§2–5. We use the dimension and contraction proofs in Semi-infinite orbits and weight functors, §§7–10. The category, finite jets, duality and exact faithful cohomology are proved in The Satake category, §§1–4,6. The classical base-change, projection, trace and duality maps are constructed in Constructible complexes on algebraic varieties, Appendices F–K. Torsor descent in the heart is Equivariant perverse sheaves and perverse sheaves on stacks, Lemma B.2; product acyclicity is its Lemma B.5.

## 1. Two endpoints give a bounded scheme

Choose the faithful closed representation \(G\hookrightarrow\operatorname{GL}(V)\) of the loop-group lesson. Let \(X_1,X_2\) be finite closed unions of Schubert varieties, with bounds
\[
t^{N_i}V_O\subset L_i\subset t^{-N_i}V_O.
\]
These inclusions hold over every parameter algebra. A chain of modifications is described locally by
\[
[g,y],\qquad gK\in X_1,\quad y\in X_2,
\qquad (g,y)\sim(gh^{-1},hy)\ (h\in K).
\]
Its first and last endpoints are
\[
p([g,y])=gK,\qquad m([g,y])=gy.                         \tag{1.1}
\]
The relative second lattice satisfies
\[
t^{N_2}L_1\subset gL_2\subset t^{-N_2}L_1.
\]
Consequently its last endpoint has bound \(M=N_1+N_2\), including over nonreduced parameter rings.

Here is a scheme construction of the contraction. Over an étale frame chart \(U\to X_1\), choose the formal frame \(g_U\) of the universal first disc torsor. Such charts and their formal lifts are proved in the loop-group lesson, Lemma 4.1: first trivialize the smooth torsor modulo \(t\), then lift through its square-zero thickenings. In the finite product \(U\times X_M\), impose the closed condition
\[
g_U^{-1}z\in X_2.                                      \tag{1.2}
\]
The inverse frame sends the target bound into bound \(M+N_1\), so (1.2) is the inverse image of an actual closed immersion in a finite stage. Replacing the frame multiplies the relative endpoint by an integral element. Since \(X_2\) is \(K\)-stable, the closed ideals agree on overlaps. Faithfully flat ideal descent from the gluing lesson constructs
\[
Y=X_1\widetilde\times X_2\hookrightarrow X_1\times X_M.  \tag{1.3}
\]
This is a closed immersion on the full parameter functors, not merely an injection on complex points. Thus \(Y\) is projective and \(m\) is proper.

The endpoint description explains uniqueness. For any two endpoints, choose a formal frame of the first torsor and apply its inverse to the second endpoint. Another frame changes the relative endpoint by precisely the contraction relation above. This gives inverse maps between the full twisted product and the two-endpoint functor. Condition (1.2) cuts out its relative-support subfunctor.

For finite descent, take \(n\ge\max(1,2N_2)\). The all-ring calculation of Lesson 6, §1, makes \(K_n\) act trivially on \(X_2\). Let \(E_n\to X_1\) be the torsor of frames of the universal disc torsor modulo \(t^n\). Its étale charts are \(U\times J_nG\), so it is a finite-type smooth torsor. Its dimension over \(X_1\) is
\[
e_n=\dim J_nG=n\dim G.
\]
Truncated frames lift formally on affine charts, and two lifts differ by \(K_n\). Therefore
\[
Y=E_n\times^{J_nG}X_2,
\qquad q:E_n\times X_2\longrightarrow Y                 \tag{1.4}
\]
is a smooth torsor of relative dimension \(e_n\). Increasing the frame level gives the same associated scheme: this is the identity in every formal frame chart, hence descends.

## 2. The twisted external product and its shifts

Over a field, \(P\boxtimes Q\) is perverse when \(P,Q\) are perverse. We recall the proof needed here. Tensor product is exact on stalk vector spaces, and
\[
\mathcal H^k(P\boxtimes Q)
 =\bigoplus_{a+b=k}\mathcal H^a(P)\boxtimes\mathcal H^b(Q).
\]
The support dimension of each term is at most \(-a-b=-k\). This proves the upper perverse bound. Proper-support base change and projection formula give compact-support Künneth on product neighbourhoods: first integrate along one projection, then along the other. The finite-dimensional local pairing with the dualizing complexes consequently gives
\(D(P\boxtimes Q)=DP\boxtimes DQ\).
The same upper bound for \(DP,DQ\) proves the lower bound. These are the explicit maps of the constructible-complexes lesson, H.1–H.6 and J.

Let \(P,Q\) be Satake-heart objects on \(X_1,X_2\), and let
\(\pi:E_n\times X_2\to X_1\times X_2\).
The complex
\[
\pi^*(P\boxtimes Q)[e_n]
\]
is perverse. Equivariance of \(Q\) supplies its descent for the contraction action. Torsor descent, Lemma B.2, gives a unique perverse object \(P\widetilde\boxtimes Q\) with
\[
q^*(P\widetilde\boxtimes Q)[e_n]
 \simeq\pi^*(P\boxtimes Q)[e_n].                         \tag{2.1}
\]
The two shifts cancel. In a formal frame chart the descended complex is \(P|_U\boxtimes Q\), with no extra shift. A higher frame level pulls back both sides of (2.1); connected-fibre full faithfulness and the normalized descent identify them canonically. Closed enlargement of either support extends the corresponding twisted sheaf by zero.

Smooth duality applied to the equally normalized pullbacks in (2.1) gives
\[
D(P\widetilde\boxtimes Q)
 \simeq DP\widetilde\boxtimes DQ.                       \tag{2.2}
\]
Define the derived convolution by
\[
P*Q=Rm_*(P\widetilde\boxtimes Q).                       \tag{2.3}
\]
We next prove that this is in the heart.

## 3. The image of each source-stratum closure

The source strata are
\[
T_{\alpha,\beta}=O_\alpha\widetilde\times O_\beta.
\]
They are smooth and irreducible, of dimension \(d_\alpha+d_\beta\). Indeed on the finite frame torsor they are products of the two smooth irreducible orbits. Their reduced closures are
\[
Y_{\alpha,\beta}=Z_\alpha\widetilde\times Z_\beta.
\]
The latter is reduced and irreducible after the same smooth faithfully flat pullback, and its indicated open stratum is dense. The closure contains exactly the strata with \(\gamma\le\alpha\) and \(\eta\le\beta\). These finitely many closure relations give a closed filtration by any order placing smaller pairs first.

We prove
\[
m(Y_{\alpha,\beta})=Z_{\alpha+\beta}.                   \tag{3.1}
\]
Use the actual representations constructed in the orbit lesson's upper-bound proof, equation (3.8). Their largest weights are \(\chi_i=c_i\omega_i\), with \(c_i>0\). If \(gK\in Z_\alpha\), that proof gives
\[
\rho_i(g^{-1})V_{i,O}
 \subset t^{-\langle\chi_i,\alpha\rangle}V_{i,O}.
\]
Compose this bound with the one for \(hK\in Z_\beta\). Since \((gh)^{-1}=h^{-1}g^{-1}\), an endpoint of dominant type \(\delta\) satisfies
\[
\langle\chi_i,\delta\rangle
 \le\langle\chi_i,\alpha+\beta\rangle\quad\text{for every }i.
\]
The orbit lesson, §5, constructs the loop-group homomorphism \(\kappa\), proves \(\kappa(K)=0\), and proves additivity by multiplying its torus-kernel lifts. Hence \(\alpha+\beta-\delta\in\mathbb Z\Phi^\vee\). Write it as \(\sum_i a_i\alpha_i^\vee\). The displayed inequalities say \(c_i a_i\ge0\), so all integral \(a_i\ge0\). Thus \(\delta\le\alpha+\beta\).

This proves the upper containment on complex points. Reducedness makes the morphism factor through the reduced closed target: a pulled-back defining function vanishes at every closed point and is zero on a reduced finite-type complex scheme. Conversely \([t^\alpha,t^\beta]\) maps to \(t^{\alpha+\beta}\). The image of the projective source is closed and \(K\)-stable; it contains that orbit and its closure. This proves (3.1). In particular its image dimension is \(d_\alpha+d_\beta\).

## 4. The fibre estimate on every stratum

Fix an endpoint in \(O_{\nu^+}\). Equivariance lets us represent it by \(t^\nu\), with \(\nu\) antidominant. Then \(d_{\nu^+}=-\langle2\rho,\nu\rangle\). The closed fibre in \(Y_{\alpha,\beta}\) is
\[
F_\nu=m^{-1}(t^\nu)\cap Y_{\alpha,\beta}.
\]
The endpoint immersion (1.3) identifies its reduced space with a closed \(T\)-stable subset of \(Z_\alpha\).

Partition it by the finitely many semi-infinite strata \(S_\phi\) meeting \(Z_\alpha\). The explicit dominant-cocharacter contraction of the weight-functor lesson, equation (7.1), implies
\[
F_\nu\cap S_\phi\ne\varnothing\quad\Longrightarrow\quad t^\phi\in F_\nu.
\]
Closedness and torus stability keep the contraction inside the fibre. At this fixed point the second relative modification is \(t^{\nu-\phi}\in Z_\beta\). Its semi-infinite dimension is nonnegative, so
\[
\langle\rho,\beta+\nu-\phi\rangle\ge0.
\]
The proved dimension theorem also gives
\[
\dim(F_\nu\cap S_\phi)
 \le\langle\rho,\alpha+\phi\rangle
 \le\langle\rho,\alpha+\beta+\nu\rangle.
\]
Take the maximum over the finite partition. We obtain
\[
2\dim F_\nu
 \le d_\alpha+d_\beta-d_{\nu^+}.                         \tag{4.1}
\]
Every dimension here is the dimension of the reduced fibre. The same inequality bounds its intersection with the open source stratum. It holds for every pair \((\alpha,\beta)\), including boundary strata; no dual-group interpretation of the indices is used.

Over each target orbit, the smooth finite-jet orbit map admits étale local sections. Such a section \(\sigma\) identifies the inverse image with the product of the orbit chart and its fibre, by \((x,z)\mapsto\sigma(x)z\); its inverse uses \(\sigma(x)^{-1}\). It preserves all source strata. Thus (4.1), together with the proper source-stratum closures and (3.1), is stratified semismallness. If Whitney strata are required, they are the orbit strata themselves: generic Whitney regularity is proved in the constructible-complexes lesson, K.5; its bad set for an incident pair is invariant under the transitive finite-jet action on the lower orbit, so one good point makes every point good. On source frame charts the stratification is a product of these orbit stratifications. Product and analytic étale coordinates preserve the tangent and secant conditions.

## 5. Convolution is perverse and exact

Put \(A=P\widetilde\boxtimes Q\). On \(T_{\alpha,\beta}\), local frame charts and the orbit bounds for \(P,Q\) give locally constant cohomology only in degrees
\[
b\le-d_\alpha-d_\beta.
\]
At \(x\in O_\delta\), intersect the fibre with each source stratum. Each piece has compact-support cohomological dimension at most twice its dimension, by the proved bound of the constructible-complexes lesson, F.1–F.2. Ordinary truncation triangles therefore put its total compact cohomology in degrees at most
\[
2\dim(F_x\cap T_{\alpha,\beta})-d_\alpha-d_\beta
 \le-d_\delta.                                          \tag{5.1}
\]
Use compact cohomology on these pieces, which need not be proper. Intersect the finite closed source filtration with the whole fibre and apply compact-support localization successively. It preserves (5.1). The whole fibre is proper, so only at this last step does compact cohomology equal ordinary cohomology. Proper base change proves the upper perverse bound for \(Rm_*A\).

Apply exactly the same argument to \(DP,DQ\). Equations (2.2) and proper duality give
\[
D(P*Q)=DP*DQ.                                           \tag{5.2}
\]
Their upper bound is the lower perverse bound for \(P*Q\). Thus convolution is perverse.

It is spherical. The left integral action on the first frame commutes with the right contraction action. This construction is finite: a level \(\ell\ge n+2N_1\) acts trivially on the truncated first frame, since conjugating a matrix congruence by its frame loses at most \(2N_1\) powers of \(t\). Enlarge \(\ell\) to fix the endpoint bound too. The action therefore descends at finite jet level through (2.1), and proper base change gives its normalized action on the pushforward.

External tensor product over the field, descent, and proper derived image preserve triangles. Since the convolution of every pair of heart objects is in the heart, a short exact sequence in either argument gives a short exact convolution sequence by its heart long exact sequence. Convolution is exact in each variable. Enlarging supports or jet levels gives the canonical same object, as in §2.

## 6. Unit, associativity, and the highest constituent

The unit is \(\mathbf1=IC_0=\delta_K\), in degree zero. With either relative modification fixed at the base point, the relevant correspondence is the identity correspondence on the other support. Its descended sheaf is that other object, with no added shift. Hence \(\mathbf1*P=P=P*\mathbf1\), with the natural identifications.

For associativity take chains of three modifications. The successive lattice bounds are \(N_1,N_1+N_2,N_1+N_2+N_3\). Impose the relative-position closed conditions by the same frame-chart ideal descent as in (1.2). This is a projective correspondence. Descend the threefold external product on a common finite frame cover. Proper base change and projection formula identify both parenthesizations with its proper image under the last-endpoint map: on a frame chart this is just integration first in one factor and then in the other, and the composition isomorphism identifies it with integration in both. The descent maps agree on overlaps by their normalized uniqueness. The four-modification correspondence proves the pentagon, since both composites pull back to the same external-product associativity map. The identity correspondences likewise prove the unit triangles. We have constructed an exact monoidal heart.

There is one unconditional multiplicity assertion even while general semisimplicity remains unproved. The simple \(IC_{\alpha+\beta}\) occurs exactly once as a composition factor of \(IC_\alpha*IC_\beta\). Indeed (4.1) makes its fibre over the largest orbit zero dimensional. It is a finite closed torus-stable set, so every point is fixed and has first endpoint \(t^\phi\). Its two nonnegative height quantities sum to zero:
\[
\rho(\alpha+\phi)+\rho(\beta+\nu-\phi)=0,
\qquad\nu=w_0(\alpha+\beta).
\]
Each is therefore zero. If the dominant representative of \(\phi\) is \(\gamma\le\alpha\), then
\(\rho(\alpha+\phi)\ge\rho(\alpha-\gamma)\ge0\).
Equality forces \(\gamma=\alpha\) and \(\phi=w_0\alpha\). For the second assertion, reflect a Weyl-orbit point with positive simple-root pairing: reflection decreases its \(\rho\)-value by that positive pairing. The unique minimum is the antidominant point. The second relative endpoint is similarly \(t^{w_0\beta}\). The two-endpoint immersion makes this a unique fibre point, and it lies in the open source stratum. Thus the convolution restricts to the constant rank-one system shifted by \(d_{\alpha+\beta}\). Open restriction is exact on the perverse heart; all lower-support simples restrict to zero. Its rank-one restriction consequently gives exactly one largest simple constituent. This argument alone does not assert a direct-summand splitting.

## 7. Inversion on finite frames

Inversion of a right coset is a left coset. We construct the required operation using frames, where inversion is an actual morphism.

Let \(X_N\) be an inversion-stable bounded lattice stage, and take \(n>2N+1\). The inverse of a matrix whose lattice has bound \(N\) has the same bound: apply its inverse to the two lattice inclusions. Let
\[
E_n=(LG|_{X_N})/K_n,\qquad p:E_n\to X_N.
\]
There is a second map
\[
f:E_n\to X_N,\qquad[g]\mapsto g^{-1}K.                  \tag{7.1}
\]
If \(g\) is replaced by \(ga\), \(a\in K_n\), its inverse endpoint is multiplied on the left by \(a^{-1}\). This congruence group fixes the whole bounded stage, so (7.1) is well-defined over every parameter algebra. Frame-chart descent makes it a scheme morphism.

We prove that both \(p,f\) are smooth with connected fibres of dimension \(e_n=n\dim G\). This is already known for \(p\). On an étale target frame chart choose \(h\), set \(\ell=n+2N\), and write
\[
f^{-1}(U)=K/(h^{-1}K_nh)=J_\ell G/H,
\qquad H=(h^{-1}K_nh)/K_\ell.                            \tag{7.2}
\]
Indeed an inverse endpoint \(hK\) has a frame \(a h^{-1}\), \(a\in K\), and changing the original right frame is the displayed conjugate subgroup. Matrix bounds give
\[
K_\ell\subset h^{-1}K_nh\subset K_1.
\]
All formulas here are relative to \(U\).

Here is an all-base polynomial exponential calculation. For \(1\le a<r\), Lemma 1.1 of Lesson 6 makes \(U_{a,r}=K_a/K_r\) smooth and connected, of dimension \((r-a)\dim G\), with Lie algebra \(t^a\mathfrak g[t]/t^r\mathfrak g[t]\). Finite matrix exponential and logarithm are inverse polynomial maps on the nilpotent matrix ideal modulo \(t^r\). For \(u\in U_{a,r}(\mathbb C)\), the curve \(z\mapsto\exp(z\log u)\) belongs to \(U_{a,r}\): every defining equation vanishes at every nonnegative integer \(z=m\), where the value is \(u^m\), so vanishes identically. Differentiating at zero gives \(\log u\in\operatorname{Lie}U_{a,r}\). Since \(U_{a,r}\) is reduced, this inclusion holds schematically. Its logarithmic image is closed and reduced and has the full dimension of the irreducible Lie-algebra affine space, so equals that space. This proves a scheme isomorphism and hence inverse coordinates over every complex algebra, including nonreduced and nonnoetherian algebras. Compatible truncations give the formal coordinates. The transported group law is truncated BCH, generally not addition; conjugation commutes with these coordinates.

In these coordinates \(H\) is the subbundle
\[
t^n\operatorname{Ad}(h^{-1})\mathfrak g[[t]]
 /t^\ell\mathfrak g[[t]].                              \tag{7.3}
\]
Write \(M=t^n\operatorname{Ad}(h^{-1})\mathfrak g_{R[[t]]}\). The matrix bounds give \(t^\ell\mathfrak g_{R[[t]]}\subset M\subset t^{n-2N}\mathfrak g_{R[[t]]}\subset t\mathfrak g_{R[[t]]}\). Integrality can be checked in the faithful matrix representation: the inclusion of \(\mathfrak g\) into its matrix Lie algebra has a complex-linear complement, which remains a complement over \(R\). The finite-projective lattice-quotient proof of Lesson 2, Lemma 2.1, after changing the ambient lattice basis, makes both \(M/t^\ell\mathfrak g_{R[[t]]}\) and \(t\mathfrak g_{R[[t]]}/M\) finite projective over \(R\). Thus (7.3) is a vector subbundle; its split finite sequences commute with arbitrary base change. Moreover \(\det\operatorname{Ad}=1\): torus roots occur in opposite pairs, and the determinant character on a root group is a unit of \(\mathbb C[x]\), hence constant and equal to one at the identity. The dense big cell proves the scheme identity on \(G\). Smith reduction on geometric fibres now gives the rank \((\ell-n)\dim G\). Formal conjugation and exponential identify (7.3) with \(H\) on all test algebras. In particular \(H\) is a smooth closed subgroup with connected fibres, whose underlying scheme is that vector bundle; its group law need not be commutative.

No quotient-existence assertion is needed. Map \(q:J_\ell G\times U\to f^{-1}(U)\) by \(j\mapsto[kh^{-1}]\), using any formal lift \(k\) of \(j\). The affine smooth-lifting proof of Lesson 3, §7.5, supplies lifts. The inclusion \(K_\ell\subset h^{-1}K_nh\) proves independence. Every frame in the target is locally of this form, and multiplication gives
\[
(J_\ell G\times U)\times_{f^{-1}(U)}(J_\ell G\times U)
 =(J_\ell G\times U)\times_U H.
\]
Consequently \(q\) is an \(H\)-torsor. It is smooth and surjective: on its fppf trivializing cover this is the assertion for \(H\); flatness and finite presentation descend, and the smooth-fibre criterion in Smooth morphisms, Theorem 3.1, gives smoothness.

For completeness, the same criterion proves smoothness of \(f^{-1}(U)\to U\). Flatness and local finite presentation descend through the faithfully flat locally finitely presented source cover \(q\), by Flat quotient bootstrap over an arbitrary base, Lemma 5.2. On a geometric fibre, \(q\) is smooth of dimension \((\ell-n)\dim G\), and its source is smooth. At a closed point above a closed target point, the tangent sequence is surjective and has kernel of that dimension; the smooth chart dimension formula gives the identical difference for local dimensions. Hence target tangent dimension equals target local dimension, and the field Jacobian criterion proves that fibre smooth. Theorem 3.1 now applies over \(U\). Its relative dimension is \(\ell\dim G-(\ell-n)\dim G=e_n\). Its geometric fibres are connected, being surjective images of connected jet groups. This proves the claim, including after arbitrary base change. The full stage with the symmetric lattice bound is inverse-stable; for a chosen Schubert union the inverse target is its union of types \(-w_0\lambda\).

For \(Q\) in the Satake heart, \(f^*Q[e_n]\) is perverse. Its equivariance gives descent for the right frame action. Torsor descent along \(p\) defines \(I(Q)\) by
\[
p^*I(Q)[e_n]=f^*Q[e_n].                                \tag{7.4}
\]
Left multiplication of frames leaves \(f\) invariant, so the object has the required spherical action. The action factors through a sufficiently large finite jet group by the same congruence-loss bound used in §5. Its support types are \(\lambda^*=-w_0\lambda\), preserving dimension and closure order. Higher frame levels give canonical comparisons in (7.4).

For involutivity choose \(n\ge m+2N\). The map
\[
j_{n,m}:E_n\to E_m,\quad[g]\mapsto[g^{-1}]
\]
is well-defined because its conjugated frame error lies in \(K_{n-2N}\subset K_m\). It satisfies \(p_mj_{n,m}=f_n\), \(f_mj_{n,m}=p_n\). Pulling (7.4) through these identities gives \(p_n^*I^2Q=p_n^*Q\). Connected-fibre full faithfulness descends the canonical isomorphism \(I^2Q=Q\). Equal-dimensional smooth duality in (7.4) likewise gives \(I(DQ)=D(IQ)\).

Finally inversion reverses convolution. Pull the two convolution correspondences back to a sufficiently deep frame \(e=[g_0]\) of the whole endpoint. On the correspondence with endpoint \(g_0^{-1}K\), reverse the chain and translate every endpoint by \(g_0\). Its new endpoint is \(g_0K\). The intermediate endpoint \(x\) becomes \(g_0x\). A deeper frame error fixes every bounded stage, making the construction independent of its representative. Reverse again to get its inverse. On relative frame charts (7.4) identifies the two twisted sheaves with their factors interchanged. Proper base change and normalized descent give
\[
I(P*Q)=IQ*IP.                                          \tag{7.5}
\]
Reversing a longer chain commutes with either bracketing, so these identifications satisfy associativity coherence. Reversing twice gives the identity. Define
\[
Q^\vee=I(DQ).
\]
Equations (5.2), (7.4) and (7.5) give \((P*Q)^\vee=Q^\vee*P^\vee\), \((Q^\vee)^\vee=Q\), and \(\mathbf1^\vee=\mathbf1\).

## 8. Evaluation, coevaluation and both triangles

The fibre of \(m\) over the unit is its first endpoints whose inverse relative modification lies in the second support. On that fibre (7.4) identifies the twisted sheaf with \(P\otimes IQ\). Extend by zero to a common finite proper stage. Proper base change, structural duality and tensor–Hom adjunction give natural bijections
\[
\begin{aligned}
\operatorname{Hom}(P*Q,\mathbf1)
&=\operatorname{Hom}(R\Gamma_c(P\otimes IQ),\Lambda)\\
&=\operatorname{Hom}(P,D(IQ))
 =\operatorname{Hom}(P,Q^\vee).
\end{aligned}\tag{8.1}
\]
The first equality is adjunction to the closed unit point and its proper fibre. The second is the defining structural trace pairing, followed by tensor–Hom adjunction, on that actual finite stage. Thus it uses the classical operations already proved, with no equivariant-cohomology assertion.

Let \(\mathrm{ev}_Q:Q^\vee*Q\to\mathbf1\) correspond to \(1_{Q^\vee}\). Equation (8.1), associativity and (7.5) yield
\[
\begin{aligned}
\operatorname{Hom}(A*Q,C)
&=\operatorname{Hom}((A*Q)*C^\vee,\mathbf1)\\
&=\operatorname{Hom}(A*(Q*C^\vee),\mathbf1)\\
&=\operatorname{Hom}(A,C*Q^\vee).
\end{aligned}\tag{8.2}
\]
So right convolution by \(Q^\vee\) is right adjoint to right convolution by \(Q\). Let \(\mathrm{coev}_Q:\mathbf1\to Q*Q^\vee\) be its unit at \(\mathbf1\).

We check the tensor compatibility of this adjunction, which is needed for actual duality. Adjoining an unchanged first modification to the fibre correspondence of (8.1) tensors its pairing by the first factor. On a common finite frame cover, this follows from projection formula and the composition-counit identity: integration of \(B\otimes r^*F\) gives \(B\otimes Rr_!F\), and its trace is \(1_B\) tensored with the original trace. The tensor–Hom evaluation acts on those same two relative factors; the extra factor is unchanged. These identities are the adjunction and trace maps constructed in the constructible-complexes lesson, H.1–H.6. Proper base change identifies their frame pullbacks, and faithful descent makes them equal on the correspondence. Thus the bijection (8.2) commutes with left convolution by any \(B\).

Apply that compatibility to the identity maps defining the unit and counit. It proves
\[
\eta_A=1_A*\mathrm{coev}_Q,\qquad
\epsilon_C=1_C*\mathrm{ev}_Q.
\]
The adjunction triangles are consequently exactly
\[
(1_Q*\mathrm{ev}_Q)(\mathrm{coev}_Q*1_Q)=1_Q,
\qquad
(\mathrm{ev}_Q*1_{Q^\vee})(1_{Q^\vee}*\mathrm{coev}_Q)=1_{Q^\vee}.
                                                               \tag{8.3}
\]
This proves a right dual. The same argument with left convolution supplies a left dual with the same underlying object. Every Satake-heart object is therefore dualizable. In particular
\[
IC_\lambda^\vee=IC_{-w_0\lambda}.
\]
No semisimple decomposition was used.

## 9. A natural monoidal structure on ordinary cohomology

A local twisted-product spectral sequence alone gives a filtration. To obtain the natural tensor isomorphism, use a bounded moving-point family.

Let \(B=\mathbb A^2\) with ordered points \(a,b\) of the curve \(\mathbb A^1_t\). Start with \(X_1\times B\). The first universal modification, with parameter \(t-a\), gives a bundle on the curve by the moving gluing theorem of Lesson 3, §8. The parameter is monic and hence a nonzerodivisor over every base ring, as required by that proof. Restrict the bundle to the finite disc \((t-b)^n=0\), and let \(E_n^B\) be its frame torsor. Smooth lifting through the truncated disc gives its étale frame charts. Form
\[
\mathcal Y=E_n^B\times^{J_nG}X_2,\qquad\tau:\mathcal Y\to B.
\]
It is proper: the bounded Grassmannian and Plücker constructions give a \(J_nG\)-equivariant closed immersion of \(X_2\) into a finite projective representation. Descend that representation through \(E_n^B\); the associated support is closed in the resulting projective bundle over the proper \(X_1\times B\).

Descend \(P\boxtimes\Lambda_B\boxtimes Q\) to \(\mathcal A\). On the two frame maps of equal relative dimension \(e_n\), its formula is
\[
q^*\mathcal A[e_n]
 =\pi^*(P\boxtimes\Lambda_B\boxtimes Q)[e_n].             \tag{9.1}
\]
Thus \(\mathcal A[2]\) is perverse on the total family, and its fibre has the original convolution normalization. Off the diagonal, the first modification is canonically trivial at the disc around \(b\), so
\[
(\mathcal Y,\mathcal A)|_{a\ne b}
 =(X_1\times X_2,P\boxtimes Q)\times\{a\ne b\}.          \tag{9.2}
\]
On the diagonal it is the local twisted product with its twisted sheaf.

The total source strata are pairs of relative orbit indices. Étale frame charts make their stratification a product of the fixed first orbit stratification, the smooth base, and the second orbit stratification. It is Whitney by the product argument of §4, and each stratum is smooth over \(B\). The actual proper stratified-submersion proof in the constructible-complexes lesson, I.6, gives a local stratum-preserving product over every base ball, including balls meeting the diagonal. The contractible-parameter descent of Lesson 6, equation (2.4), descends the complex as well as its cohomology systems: its proof descends all attaching maps by full faithfulness. Therefore every \(R^k\tau_*\mathcal A\) is a local system on all of \(\mathbb A^2\).

This base is simply connected, by straight-line contraction. Parallel transport between its fibres is canonical. Using (9.2), ordinary field Künneth, and the diagonal fibre gives
\[
H^k(P*Q)=\bigoplus_{r+s=k}H^r(P)\otimes H^s(Q).          \tag{9.3}
\]
Proper composition identifies the diagonal-source cohomology with the convolution cohomology. All the maps are natural in both sheaves. Increasing stages or frame levels restricts the same maps and hence gives the same identification. The analogous three-point proper family over \(\mathbb A^3\) proves associativity compatibility: both binary comparisons are transport of the same threefold Künneth map from the distinct-point locus. Path independence on this contractible base identifies them. The unit family gives unit compatibility. Thus total ordinary cohomology is an exact faithful strong monoidal functor.

Equation (9.3) retains its ordinary grading. Permuting tensor factors in cohomology carries the usual Koszul signs. An ordinary symmetric-vector-space constraint requires the fusion construction and its parity adjustment; neither is inferred from associativity alone.

## 10. Minuscule rank-two convolutions

Take \(G=\operatorname{GL}_2\), \(P=IC_{(1,0)}=\Lambda_{\mathbb P^1}[1]\). Its double correspondence parametrizes
\[
O^2=L_0\supset L_1\supset L_2,\qquad
\operatorname{length}(L_0/L_1)=\operatorname{length}(L_1/L_2)=1,
\quad tL_i\subset L_{i+1}.
\]
The first lattice is determined by a line \(\ell\subset\mathbb C^2\). Over its projective line let \(S=\mathcal O(-1)\) and \(W=\mathbb C^2/S=\mathcal O(1)\). Constant and first-order coefficients give the direct decomposition
\[
L_1/tL_1=S\oplus tW.
\]
Thus the chain surface is \(\mathbb P(S\oplus W)=\mathbb F_2\). The central endpoint \(L_2=tO^2\) gives the section \(W\), whose normal bundle is \(\operatorname{Hom}(W,S)=\mathcal O(-2)\). Every other endpoint has type \((2,0)\), and its first lattice is uniquely \(L_1=L_2+tO^2\).

This is the cone resolution of Lesson 6, §8.1. To see the incidence map in coordinates, choose \(\ell=\langle(u,v)\rangle\) and a complementary vector \(q\) of determinant one. The lattice is generated modulo \(t^2O^2\) by \(t\ell\) and \(b\ell+w tq\). Expanding their Plücker wedge gives the cone coordinates \([bu^2:buv:bv^2:w]\). Hence the first line is the resolution's conic direction, the central section is its exceptional curve, and the morphism is exactly the displayed incidence resolution.

The twisted sheaf on this smooth surface is \(\Lambda[2]\). Its endpoint fibres and semismall inequalities are:

| Endpoint type | Orbit dimension | Fibre | Twice the fibre dimension |
| --- | ---: | --- | ---: |
| \((2,0)\) | 2 | point | 0 |
| \((1,1)\) | 0 | \(\mathbb P^1\) | 2 |

Let \(Q\) be its pushforward. The explicit relative disc-bundle pairing of Lesson 6, equation (8.2), gives maps \(u:\delta\to Q\) and \(v:Q\to\delta\) with \(vu=-2\). Characteristic zero makes \(-2\) invertible, so \((-1/2)v\) retracts \(u\). Split off this point summand in the perverse heart. The complement has vertex stalk only in degree \(-2\), vertex costalk only in degree \(2\), and open restriction \(\Lambda[2]\). Its strict point bounds identify it as the IC. Therefore
\[
IC_{(1,0)}*IC_{(1,0)}=IC_{(2,0)}\oplus IC_{(1,1)}.        \tag{10.1}
\]
This decomposition has been constructed directly.

A central point sheaf acts by translating every lattice, as follows from the identity correspondence with a scalar frame. Translate the second factor by \((-1,-1)\). Associativity and (10.1) give
\[
IC_{(1,0)}*IC_{(0,-1)}=IC_{(1,-1)}\oplus IC_0.           \tag{10.2}
\]
Its fibre over \(O^2\) is exactly the projective line of first lattices.

For \(\operatorname{PGL}_2\), let \(\omega^\vee\) be the primitive positive coweight. Determinant normalization identifies the two minuscule chains with the same \(\mathbb F_2\) correspondence on complex points. The forward projected-frame morphism is continuous, and the source and target proper chain spaces have those same endpoints and unique normalized lattice representatives. The compact-to-Hausdorff argument of Lesson 6, §7.3, therefore identifies their analytic spaces and strata. The same resolution and pairing prove
\[
IC_{\omega^\vee}*IC_{\omega^\vee}=IC_{2\omega^\vee}\oplus IC_0.
                                                               \tag{10.3}
\]
The two factors belong to the odd component and their convolution to the even component. Its cohomology has dimensions \(1,2,1\) in degrees \(-2,0,2\), from the two generators of the minuscule cohomology in degrees \(-1,1\). With characteristic-two coefficients the pairing scalar vanishes and these splitting arguments do not apply; the nonsplit object is calculated explicitly in Lesson 6.

## 11. Exercises with solutions

**Exercise 11.1 (easy).** Compute the fibre over the unit in (10.2).

*Solution.* The last lattice is \(O^2\). Choosing the first lattice amounts to choosing its one-dimensional quotient direction, equivalently a line \(\ell\subset O^2/tO^2\). The second relative modification is forced by the two endpoints. Thus the fibre functor is the ordinary line Grassmannian \(\mathbb P^1\), with its reduced structure; the endpoint embedding rules out any extra choice. Its dimension one makes (4.1) an equality, since both source orbit dimensions are one and the target orbit is a point. \(\square\)

**Exercise 11.2 (easy).** Check the unit and its normalization directly on a frame chart.

*Solution.* If the first support is the base point, its frame torsor is \(J_nG\), and its associated product with the second support is that support. Formula (2.1) has the same shift \([e_n]\) on both sides, so the descended sheaf is \(Q\). If the second support is the base point, each second relative endpoint is the first endpoint, the correspondence is \(X_1\), and the descended sheaf is \(P\). Proper image under each identity map gives the unit isomorphism. Their compositions on a three-modification chart are the identity, proving the unit triangle. \(\square\)

**Exercise 11.3 (medium).** Prove the fibre estimate for the two minuscule \(\operatorname{GL}_2\) factors without the general theorem.

*Solution.* A length-two quotient \(O^2/L_2\) has Smith type \((2,0)\) or \((1,1)\). In the first case it is cyclic of length two and has a unique length-one submodule, so the intermediate lattice is unique. In the second case \(L_2=tO^2\), and every line of \(O^2/tO^2\) is an intermediate lattice. The fibres have dimensions zero and one. The source has dimension two, while the respective target orbits have dimensions two and zero. Hence twice each fibre dimension equals source dimension minus target-orbit dimension. Translation gives the same calculation for the inverse minuscule second factor. \(\square\)

**Exercise 11.4 (medium).** Derive the \(\operatorname{PGL}_2\) decomposition from its actual fibres and their local pairing.

*Solution.* The normalized minuscule chain surface is \(\mathbb F_2\), with a point fibre over the open type-two orbit and \(\mathbb P^1\) over the unit. Its constant shifted pushforward is perverse by those stalk and relative cochain bounds. The maps from and to the unit have one-dimensional Hom spaces. Their composite is the exceptional normal Euler number \(-2\), calculated from \(\mathcal O(-2)\). Scale the second map to obtain a retraction. The remaining summand has open constant rank one and strict point stalk/costalk bounds, hence is \(IC_{2\omega^\vee}\). The split point summand is \(IC_0\), proving (10.3). No dimension-only decomposition argument is needed. \(\square\)

**Exercise 11.5 (hard).** Construct the dual of an arbitrary classical Satake-heart object and verify both triangle identities, keeping inversion off the right-coset space.

*Solution.* Use the finite frame scheme and its two maps \(p([g])=gK\), \(f([g])=g^{-1}K\). Section 7 proves their smooth connected relative dimension \(e_n\). Descend \(f^*DQ[e_n]\) along \(p\) to obtain \(Q^\vee=I(DQ)\). Endpoint-framed chain reversal gives the contravariant monoidal involution. The proper unit fibre identifies \(\operatorname{Hom}(P*Q,\mathbf1)\) with \(\operatorname{Hom}(P,Q^\vee)\), by the explicit structural trace and tensor–Hom adjunction. Its identity defines evaluation; the derived bijection (8.2) defines right-convolution adjunction and coevaluation at the unit. Projection formula with an unchanged first modification gives \(\eta_A=1_A*\mathrm{coev}\) and \(\epsilon_C=1_C*\mathrm{ev}\), as proved in §8. Substituting these into the two adjunction triangles gives exactly (8.3). Left convolution gives the left dual as well. Every construction lies in a finite scheme or finite frame torsor. \(\square\)

## References

- I. Mirković and K. Vilonen, [*Geometric Langlands duality and representations of algebraic groups over commutative rings*](https://arxiv.org/abs/math/0401222v5), free corrected preprint, §§4–6.
- X. Zhu, [*An introduction to affine Grassmannians and the geometric Satake equivalence*](https://arxiv.org/abs/1603.05593v2), free lecture notes, §5.1.
- L. Fargues and P. Scholze, [*Geometrization of the local Langlands correspondence*](https://arxiv.org/abs/2102.13459), free preprint, Proposition VI.8.2, for comparison with the dualizability statement in its different geometric setting. The classical construction and both triangles are proved above.
