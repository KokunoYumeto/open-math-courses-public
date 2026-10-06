# Cone symmetries without a global faithful state

*Written and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, 5 October 2026. Original exposition is CC0.*

A standard cone can have no vector with full support. We therefore build its positive symmetries on invariant supported corners and prove that their algebra implementers agree. Uniform bounds make the resulting operator belong to the original von Neumann algebra. This supplies the missing generality in the positive-factorization theorem and then in the generator and orientation theorems.

The source target is Takesaki, *Theory of Operator Algebras II*, Exercise IX.1(11), printed page 166 in the approved edition: extend the results of IX.1(6), (8), (9) and (10) beyond sigma-finiteness. We retain the corrections already proved in the earlier readings: the quadratic identity in (6) is asserted for cone vectors, and the dense-face lemma in (8) requires injectivity. Removing a cardinality assumption does not restore either false statement.

The exact inputs are Every projection has a faithful cone corner and The corner seen by a positive vector/07/08/09, faithful corner representations and supported faces, The standard-form axioms and Real decomposition and orthogonal supports, the standard-form axioms and support geometry, The bounded prerequisite boundary and Finite-vector approximation and the bicommutant/07, positive calculus, strong limits and support projections, and Unbounded measurable functions and Transport, reduction, and membership in an algebra, spectral projections in the algebra. For the previously written proofs we use Recover the unique positive algebra element, sigma-finite positive factorization, Faces determine a symmetrized projection action and Extend the projections and prove Jordan multiplication/03 and Transport a faithful vector and its order intervals and Identify the order-map formula exactly, Jordan reconstruction and its local quarter-power formula, Split the whole map along a central projection and Assemble the cone unitary and prove canonicity, central splitting and implementation, Norm limits keep both directions of the cone action and A continuous Jordan flow fixes the center first/04/05, bounded cone flows, All von Neumann derivations are inner, unrestricted innerness, and A commutator commuting with its first entry is quasinilpotent through Two checks on the quotient and on orientation ambiguity, orientations and reconstruction.

Fix an arbitrary standard form \((M,H,J,P)\). For a projection \(e\in M\), write \(Q_e=eJeJ\), \(K_e=Q_eH\), and \(P_e=P\cap K_e\). SE-03 makes the restriction of \(eMe\) to \(K_e\) a faithful standard form, with conjugation \(J_e=J|_{K_e}\). A projection is called sigma-finite when its corner has a faithful normal state; include zero. These projections need not be central.

## Countably many supports still fit in one faithful corner

Every \(\xi\in P\) has a sigma-finite support \(s_\xi\): by SE-06, its vector functional is faithful on the supported corner, and normalization gives a state when \(\xi\ne0\). Conversely SE-09 constructs a cone vector with support any prescribed sigma-finite projection.

Here is the countable-join fact we will need. If \(\xi_n\in P\), choose strictly positive scalars \(c_n\) with \(\sum_n c_n\|\xi_n\|<\infty\), and put \(\xi=\sum_n c_n\xi_n\). Then

\[
 s_\xi=\bigvee_n s_{\xi_n}.
 \tag{NX.1}
\]

Indeed the projection on the right fixes the sum, giving one inequality. For the other, fix \(n\) and write \(\xi=c_n\xi_n+\eta_n\) with \(\eta_n\in P\), by norm convergence and closedness. Its smallest closed face is \(P_{s_\xi}\), by SE-07. The face property puts \(\xi_n\) in that face, hence \(s_{\xi_n}\le s_\xi\). This proves (NX.1). Choosing one full-support vector for each of countably many sigma-finite projections proves that their join is sigma-finite. No commutation or orthogonality of those projections is used.

The sigma-finite projections have supremum one. If their supremum is \(r\), it fixes every cone vector and hence the complex linear span of the cone, which is dense in \(H\). Therefore \(r=1\). Their finite joins are sigma-finite by (NX.1), so they form an upward-directed family. Increasing projection nets converge strongly to their supremum: the union of their ranges is dense in the range of that supremum, and the contractions converge on this dense union. This also follows from BK-02. Thus their net converges strongly to one, without replacing that net by a sequence.

## Enlarge a corner until the symmetry preserves it

Let \(T\in B(H)\) be positive and invertible, with \(TP=P\). Its restriction to the cone and its inverse preserve order. Since \(T\) is a homeomorphism of \(H\), it carries closed cone faces to closed cone faces. SE-08 consequently gives an order bijection \(f\) of the projection lattice, characterized by

\[
 TP_e=P_{f(e)}.
 \tag{NX.2}
\]

An order bijection preserves arbitrary suprema: apply its inverse to each candidate upper bound. It also preserves sigma-finite projections. If \(e=s_\xi\), it carries the smallest closed face of \(\xi\) onto that of \(T\xi\), so \(f(e)=s_{T\xi}\). The same argument applies to \(T^{-1}\).

For a sigma-finite \(e\), define

\[
 \widetilde e=\bigvee_{n\in\mathbb Z}f^n(e).
 \tag{NX.3}
\]

This is a countable join of sigma-finite projections, hence sigma-finite by NX-01; preservation of suprema gives \(f(\widetilde e)=\widetilde e\). Let \(\mathcal E_T\) be all sigma-finite projections fixed by \(f\). It is directed, since a finite join of fixed projections is fixed and sigma-finite. Formula (NX.3) shows that every sigma-finite projection is below an element of \(\mathcal E_T\), so its supremum is one.

For \(e\in\mathcal E_T\), the equality \(TP_e=P_e\) and the dense complex span of \(P_e\) in \(K_e\) give \(TK_e=K_e\). Because \(T=T^*\), this invariant closed subspace reduces \(T\): if \(v\perp K_e\), then \(\langle Tv,w\rangle=\langle v,Tw\rangle=0\) for \(w\in K_e\). Its inverse also restricts to \(K_e\). Hence

\[
 \begin{gathered}
 T_e=T|_{K_e}>0,\\
 T_eP_e=P_e,\\
 \|T_e\|\le\|T\|,\\
 \|T_e^{-1}\|\le\|T^{-1}\|.
 \end{gathered}
 \tag{NX.4}
\]

Finally \(Q_e\to I\) strongly along \(\mathcal E_T\). Both \(e\) and \(JeJ\) converge strongly to one; subtracting their product from the identity and using contraction bounds proves the assertion. Thus these invariant cone corners exhaust the entire standard Hilbert space.

## The Hilbert-space factorization controls the algebra norm

For any positive element \(a\) in a standard-form algebra, the operator \(aJaJ\) is positive, and

\[
 \|aJaJ\|=\|a\|^2.
 \tag{NX.5}
\]

The upper bound follows by multiplication of norms. For the lower bound, if \(0<r<\|a\|\), its spectral projection \(p=1_{(r,\infty)}(a)\) is nonzero, by SK-05/08. The faithful corner property SE-03 gives \(K_p\ne0\). Both \(a\) and \(JaJ\) reduce this space and are at least \(rI\) there. They commute. Their product is therefore at least \(r^2I\): expand it as \((a-rI)JaJ+r(JaJ-rI)+r^2I\), a sum of commuting positive products on this space. This gives norm at least \(r^2\); let \(r\) increase to \(\|a\|\). The zero case is immediate. The same proof works in every faithful standard corner. Its representation preserves the norm of a positive element: faithfulness keeps every nonzero spectral projection nonzero, so the preceding spectral lower-bound test and the operator upper bound give the same norm.

For \(e\in\mathcal E_T\), apply PA-06 to the sigma-finite standard form of \(eMe\). There is a unique positive element \(h_e\), invertible in \(eMe\), such that

\[
 T_e=h_eJ_eh_eJ_e.
 \tag{NX.6}
\]

Define the fixed positive constants \(m=\|T^{-1}\|^{-1/2}\) and \(C=\|T\|^{1/2}\), for the nonzero algebra. By (NX.4)–(NX.6), applied also to the inverse factorization,

\[
 me\le h_e\le Ce.
 \tag{NX.7}
\]

Indeed \(\|h_e\|^2=\|T_e\|\) and \(\|h_e^{-1}\|^2=\|T_e^{-1}\|\); positive spectral calculus converts the latter bound into the lower inequality. These bounds do not depend on the corner. For the zero corner set \(h_0=0\), so (NX.7) still makes sense.

## Compatibility and the global positive implementer

We first show that for \(e,f\in\mathcal E_T\) with \(e\le f\),

\[
 h_fe=eh_f=h_e.
 \tag{NX.8}
\]

Work temporarily in the faithful standard representation of \(N=fMf\) on \(K_f\). Choose \(\xi\in P_e\) with support \(e\), by SE-09. The operator \(b=J_fh_fJ_f\) is invertible in the commutant of \(N\). The cyclic commutant subspace generated by \(b\xi\) is the same as that generated by \(\xi\), since \(N'b=N'\). Since \(h_f\in N\),

\[
 \begin{gathered}
 \overline{N'h_fb\xi}\\
 =h_f\overline{N'\xi}\\
 =h_f(eK_f).
 \end{gathered}
\]

The image on the right is closed because \(h_f\) is boundedly invertible. By (NX.6) the vector on the left is \(T\xi\), which belongs to \(P_e\). Its support is therefore at most \(e\). The cyclic-subspace characterization of supports gives \(h_f(eK_f)\subset eK_f\). Thus \((f-e)h_fe=0\) in this faithful representation, hence in the algebra. Self-adjointness of \(h_f\) gives the reverse off-diagonal equality, so \(h_f\) commutes with \(e\).

It follows that \(h_f\) and its conjugate reduce \(K_e\). Their restrictions factor \(T_e\) using the positive element \(eh_fe\), which is invertible in \(eMe\) by (NX.7). The uniqueness in PA-06 identifies it with \(h_e\), proving (NX.8). This is the step that makes the local choices compatible; compactness of a bounded family alone would not supply it.

Regard each \(h_e\) as an element of \(M\) by zero extension outside \(e\). On the dense linear subspace \(\bigcup_{e\in\mathcal E_T}eH\), prescribe \(h\zeta=h_e\zeta\) when \(\zeta\in eH\). Directedness and (NX.8) make this well defined and linear, with norm at most \(C\). It extends to a bounded operator on \(H\). The net \(h_e\) converges strongly to it: it is eventually constant on each such \(eH\), and the uniform bound gives convergence on its closure. Since \(M\) is strongly closed, \(h\in M\). Taking strong limits in the positive inequalities (NX.7) gives

\[
 mI\le h\le CI.
 \tag{NX.9}
\]

Thus \(h\) is positive and invertible. Taking the strong limit of (NX.8), with one corner fixed, gives \(he=eh=h_e\). It follows that \(hJhJ\) agrees with \(T\) on every \(K_e\). Since \(Q_e\to I\) strongly, these spaces have dense union, and

\[
 T=hJhJ.
 \tag{NX.10}
\]

The uniqueness proof uses no cardinality assumption. If positive invertible \(h,k\in M\) give the same product, put \(a=k^{-1}h\). Commutation of left and right factors gives \(aJaJ=I\), so \(a^{-1}=JaJ\in M\cap M'\). Hence \(a\) is central, \(h=ka\), and \(h\) commutes with \(k\). Therefore \(a=k^{-1/2}hk^{-1/2}\) is positive. The central standard-form identity now gives \(JaJ=a\), whence \(a^2=I\), and positive calculus gives \(a=I\). Conversely any positive invertible \(h\in M\) gives a positive invertible product \(hJhJ\); the cone axiom applied to \(h\) and to \(h^{-1}\) proves that it maps \(P\) onto itself. This proves the full characterization for arbitrary \(M\). The zero standard form is immediate and needs no constants \(m,C\).

## Jordan reconstruction is global; quarter powers are local

Let \(U:H_1\to H_2\) be a complex-linear unitary between arbitrary standard forms, with \(UP_1=P_2\). The complete proof JR-01–03 already assumes no faithful state. It uses all closed faces, finite spectral steps, cone-vector functionals and arbitrary increasing nets. It gives a unique normal Jordan star isomorphism \(\theta:M_1\to M_2\), with

\[
 \begin{gathered}
 Uj_1(x)U^*={} \\
 j_2(\theta(x)),\\
 j_i(x)={} \\
 (x+J_ix^*J_i)/2,
 \end{gathered}
 \tag{NX.11}
\]

and \(\omega_{U\xi}\circ\theta=\omega_\xi\) for every \(\xi\in P_1\). The latter identity also holds for \(J_1\)-fixed vectors, as JR-03 proves. Its asserted extension to all complex Hilbert vectors is false, with the same matrix counterexample regardless of any cardinality assumption.

The faithful-vector method remains available on each supported corner. Choose a sigma-finite projection \(e\in M_1\) and \(\xi\in P_{1,e}\) with support \(e\). Put \(f=\theta(e)\). The face correspondence gives \(UP_{1,e}=P_{2,f}\), and therefore a unitary from \(K_{1,e}\) onto \(K_{2,f}\). Its image \(U\xi\) has support \(f\), so both corner functionals are faithful and finite. The restriction \(\theta_e:eM_1e\to fM_2f\) is well defined and onto. Indeed a Jordan map preserves \(exe\): with \(a\circ b=(ab+ba)/2\), expand the identity \(exe=2e\circ(e\circ x)-e\circ x\), and apply square polarization.

Apply the full faithful-corner proof JR-04/05/06 to these two forms. If \(\Theta_1,\Theta_2\) denote their quarter-power maps for \(\xi,U\xi\), respectively, then \(\theta_e=\Theta_2^{-1}U\Theta_1\), with the inverse taken on the precise principal-face span proved in QO. The order intervals and closed-domain calculation are thus retained wherever a full-support finite vector exists. These corner maps agree with the global \(\theta\), so they agree on overlaps. Their corner algebras determine the global map: the net \(exe\) converges strongly to \(x\) and is bounded, and hence converges ultraweakly; normality then determines \(\theta(x)\). There is no invented faithful normal functional on a non-sigma-finite algebra.

The auxiliary statements in PA are consistent with the same distinction. An injective map with dense algebraic face range, as in PA-05, forces \(\Theta(1)\) to have full support by its proved principal-face argument; thus its hypotheses already force sigma-finiteness. Statements involving a faithful normal positive functional apply on its supported corner. All five valid steps of the sigma-finite positive-factorization proof remain the local inputs in (NX.6); NX-01–04 prove the global conclusion without assuming those global faithful vectors exist.

## Every bounded cone generator has an algebra representative

For arbitrary \(M\), a bounded complex-linear \(D\in B(H)\) generates cone automorphisms at every real time exactly when

\[
 \begin{gathered}
 D=x+JxJ, \\
 \text{for some }x\in M.
 \end{gathered}
 \tag{NX.12}
\]

Here is how the full generator proof extends. GN-01 uses only self-duality, closedness and the bounded exponential series. Its norm Lie–Trotter proof splits \(D\) into \(S=(D+D^*)/2\) and \(K=(D-D^*)/2\), each generating cone automorphisms. It also proves \(JDJ=D\).

For \(S=S^*\), apply NX-04 to \(e^S\). Write \(e^S=hJhJ\), with \(h\) positive invertible, and set \(a=\log h\in M_{\rm sa}\). The commuting factors give \(hJhJ=e^{a+JaJ}\). Bounded positive logarithms therefore give \(S=a+JaJ\). The unique positive implementer at time \(t\) is \(e^{ta}\), so the continuous and differentiable lift asserted in GN-02 follows at this full scope as well.

For \(K^*=-K\), use NX-05 on \(U_t=e^{tK}\) to obtain the normal Jordan flow \(\theta_t\). The center-fixing argument GN-03 is cardinality independent: JI-04's central splitting shows that the center is preserved, (NX.11) gives \(\theta_t(z)=U_tzU_t^*\) there, and for small \(t\) its effect on each central projection has norm distance less than one. Distinct commuting projections have distance one, so they are fixed. Subdivision of any real time into small times, followed by norm spectral approximation, fixes the entire center at every time. Each Jordan half-time map then acts on its own invariant multiplicative and antimultiplicative central pieces; squaring it preserves products on both. Thus \(\theta_t\) is a star automorphism.

SE-10/11 and JI-06 give standard implementation and its uniqueness for arbitrary standard forms. Hence \(\theta_t(x)=U_txU_t^*\). Its norm derivative is the bounded star derivation \(d(x)=[K,x]\in M\), with norm at most \(2\|K\|\), exactly as proved in GN-04. AU-03, or its bounded consequence BI-08, supplies \(b=b^*\in M\) with \(d=i[b,\cdot]\). Write the skew commutant remainder as \(K=ib+ic\), \(c=c^*\in M'\). From \(JKJ=K\), the element \(z=b+JcJ\) is both central self-adjoint and satisfies \(JzJ=-z\). The standard-form central identity also gives \(JzJ=z\); thus \(z=0\) and \(K=ib+J(ib)J\). These are precisely GN-05's identities, requiring no finite functional.

Combining the two parts gives (NX.12) with \(x=a+ib\). Conversely the commuting exponential identity \(e^{t(x+JxJ)}=e^{tx}Je^{tx}J\), together with the cone axiom at \(t\) and \(-t\), proves equality of the cone images. Finally \(x+JxJ=0\) holds exactly when \(x\in iZ(M)_{\rm sa}\): the equation makes \(x\) central, and the central identity makes it skew-adjoint; the converse follows by substitution. This retains the full real-linear kernel statement and every valid generator clause.

## Orientations recover arbitrary standard-form algebras

Let \(\mathfrak g\) be the bounded cone-generator algebra, \(Z=Z(M)\), and \(\Phi(x)=x+JxJ\). By NX-06 it is exactly the real Lie image of \(M\). The proof ON-01 of vanishing central commutators uses a factorial norm estimate and applies on any Hilbert space. Consequently ON-02 identifies the center \(\mathfrak c\) of \(\mathfrak g\) as \(Z_{\rm sa}\), and \(j:x+Z\mapsto\widehat{\Phi(x)}\) identifies the real Lie algebras \(M/Z\) and \(\mathfrak g/\mathfrak c\). Their centers are zero. AU-03 identifies \(M/Z\) with all everywhere-defined complex derivations of \(M\), including automatic boundedness.

Transport multiplication by \(i\) through \(j\) to obtain \(I_M\). An orientation is any real-linear map \(I\) on the quotient satisfying \(I^2=-1\), \(I(u^*)=-(Iu)^*\), and \([Iu,v]=[u,Iv]=I[u,v]\). ON-03 proves these identities for \(I_M\). The proof requires only the quotient just established, so applies here without change of hypotheses.

For two orientations, ON-04 proves that their centroid maps commute and that \(I_2I_1^{-1}\) is an adjoint-compatible involution. Its two eigenspaces lift to commuting von Neumann subalgebras \(A,B\subset M\) with \(M=A+B\) and \(A\cap B=Z\). The mutual-commutant proof does not assume the orientations are continuous. ON-05 proves in full that the ultraweak ideal generated by \([A,A]\) has the form \(eM\) for a central projection \(e\). Its projection joins are arbitrary nets; no countable selection is used. It gives \(A=eM+Z\) and \(B=(1-e)M+Z\). Therefore the orientations agree on the quotient from \(eM\) and are negatives on the quotient from \((1-e)M\). The sign projection is not uniquely determined on abelian central summands, where the quotient is zero.

For any central projection \(e\), the algebra \(N=eM+(1-e)M'\) has standard form \((N,H,J,P)\). The verification in ON-06 uses only the two central Hilbert summands and the standard-form axioms. On its first quotient summand its orientation is \(I_M\), and on the second it is \(-I_M\). Apply NX-06 to these arbitrary standard forms as well. This realizes every orientation classified in the preceding paragraph; the sigma-finiteness check in ON-06 is no longer needed.

The concrete reconstruction also retains its full scope. Given \(I=I_M\), let \(\mathcal C_I\) be the pairs \((D,E)\in\mathfrak g^2\) with \(\widehat E=I\widehat D\), and set \(r_\pm(D,E)=D\pm iE\). Then

\[
 \begin{gathered}
 M=r_-(\mathcal C_I),\\
 M'=r_+(\mathcal C_I).
 \end{gathered}
 \tag{NX.13}
\]

Indeed NX-06 gives \(D=\Phi(x)\), and the quotient condition gives \(E=\Phi(ix)+z\) for \(z\in Z_{\rm sa}\). Direct conjugate-linearity yields \(D-iE=2x-iz\in M\) and \(D+iE=2JxJ+iz\in M'\). Every element is obtained by choosing \(D=\Phi(x/2)\), \(E=\Phi(ix/2)\), as in ON-07. The zero quotient and abelian cases in ON-08 are unchanged. Thus all seven orientation clauses hold for arbitrary algebras and arbitrary Hilbert cardinality, without a continuity assumption on the orientation.

## Why the limiting family cannot be replaced by one state

Let \(I\) be uncountable, \(M=\ell^\infty(I)\) acting diagonally on \(H=\ell^2(I)\), let \(J\) be coordinate conjugation, and let \(P\) be the nonnegative vectors. The standard-form axioms follow coordinate by coordinate; the commutant is the same diagonal algebra, since commuting with all single-coordinate projections forces diagonal action.

Every vector of \(\ell^2(I)\) has countable support. For each positive integer \(n\), only finitely many coordinates can have magnitude at least \(1/n\); take their countable union. Hence no cone vector has full support. Equivalently, a faithful normal state would assign strictly positive masses to all the single-coordinate projections, while their finite sums have total mass at most one. Such a summable positive family has only countably many nonzero entries, by the same finite-threshold argument. Thus this algebra is not sigma-finite.

Choose numbers \(m\le h_i\le C\), with \(m>0\), and define \((T\xi)_i=h_i^2\xi_i\). This positive invertible operator maps \(P\) onto itself. Every countable-coordinate corner is invariant and has positive implementer \(h_e=(h_i)_{i\in e}\). Their uniform bounds are exactly those in NX-03, and compatibility gives the diagonal global element \(h=(h_i)_{i\in I}\), with \(T=hJhJ\). Finite or countable coordinate subsets, ordered by inclusion, exhaust \(I\) as a net. No sequence of countable subsets does so: its union is countable. This example explains both the invariant-corner construction and the use of arbitrary nets.

The proof also does not replace arbitrary corners by central ones. For example, \(B(\ell^2(I))\) has only the central projections zero and one. To check this, an operator commuting with every rank-one projection preserves every one-dimensional subspace; applying it to the sum of two independent vectors shows that its eigenvalue is the same on both, so it is scalar. The family of mutually orthogonal rank-one projections prevents a faithful normal state by the same summability argument. Nevertheless every finite-dimensional corner has the faithful normal normalized matrix trace, and their directed supremum is one. Central decomposition alone would miss this case; NX-01–04 explicitly allow noncentral projections.
