# Curvature and holonomy groups

Curvature measures the failure of horizontal transport to commute. We derive its principal and associated forms, prove both Bianchi identities, and construct full and restricted holonomy as immersed Lie groups, including nonclosed holonomy. The chapter then develops intrinsic torsion, binary-form and tensor-product curvature spaces, and complete local connection equations. The final constructions produce actual analytic connections at regular and singular Poisson parameters.

Read first [Connections and parallel transport](connections-and-parallel-transport.md), [Principal bundles and associated bundles](principal-bundles-and-associated-bundles.md), [Local tools for bundles and transport](local-tools-for-bundles-and-transport.md), and the exact earlier exterior-calculus and example proofs in [DG-CHAR-17](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-17.md). Each part supplies its proofs and identifies its freely accessible human construction sources. The definitions and signs used in subsequent parts are fixed where they first appear.

## A. Exterior calculus and principal curvature

We use the right principal action and left Maurer form of **Connections and parallel transport**, A.1–A.4, abbreviated **Conn**. **PB** denotes **Principal bundles and associated bundles**. The exact earlier foundations are PB C.2–C.3 for tangent, exterior and Lie algebra constructions; Local tools 0.3, 2.1 and 2.3 for calculus, local smooth flows and group exponentials; and DG-CHAR-17 D.0–D.1 for ordinary exterior forms, their products, exterior differentiation and smooth pullback. All manifolds and Lie groups in this part are finite dimensional, Hausdorff, second countable and smooth.

**Lemma A.1 (forms with Lie algebra coefficients).** Let \(\mathfrak g\) be a finite dimensional real Lie algebra. A \(\mathfrak g\)-valued form is a smooth alternating multilinear map into \(\mathfrak g\); exterior differentiation acts on its coordinates in any fixed vector-space basis. There is a well-defined bracket
\[
[a\otimes X,b\otimes Y]=(a\wedge b)\otimes[X,Y]_{\mathfrak g}.
\tag{A.1}
\]
For forms \(\alpha,\beta,\gamma\) of degrees \(p,q,r\), respectively, it satisfies
\[
\begin{aligned}
{}[\alpha,\beta]&=-(-1)^{pq}[\beta,\alpha],\\
[\alpha,[\beta,\gamma]]
&=[[\alpha,\beta],\gamma]+(-1)^{pq}[\beta,[\alpha,\gamma]],\\
d[\alpha,\beta]&=[d\alpha,\beta]+(-1)^p[\alpha,d\beta].
\end{aligned}
\tag{A.2}
\]
It commutes with pullback. Its evaluation is the shuffle sum
\
[\alpha,\beta
=\sum_{\sigma\in\mathrm{Sh}(p,q)}\operatorname{sgn}(\sigma)
 [\alpha(v_{\sigma(1)},\ldots,v_{\sigma(p)}),
 \beta(v_{\sigma(p+1)},\ldots,v_{\sigma(p+q)})]_{\mathfrak g}.
\tag{A.3}
\]
Here a shuffle preserves the order inside each of the two displayed blocks.

**Proof.** Fix a basis \(e_a\) of \(\mathfrak g\). Every valued form is uniquely \(\sum_a\alpha^a e_a\). Define the bracket by
\(\sum_{a,b}\alpha^a\wedge\beta^b[e_a,e_b]\).
A change of basis has constant coefficients; bilinearity of the vector-space bracket cancels the basis-change matrices and their inverses in this expression. Thus it is independent of the basis. The same constant-coordinate argument proves independence of the definition of \(d\).

The wedge product of scalar forms is the shuffle sum by its alternating multilinear definition: choosing which \(p\) of the ordered vectors enter the first factor specifies exactly one shuffle, and the remaining \(q\) enter the second. Applying this to each basis coefficient gives (A.3). Equivalently it is the full permutation sum divided by \(p!q!\): reordering within the two blocks changes both the permutation sign and the alternating factor's sign, leaving the term unchanged, with exactly \(p!q!\) repetitions.

For the first identity of (A.2), scalar graded commutativity contributes \((-1)^{pq}\), and the Lie bracket contributes a minus sign. For the second, it suffices by trilinearity to take \(\alpha=aX,\beta=bY,\gamma=cZ\) with constant \(X,Y,Z\). Move the scalar factors in each term to the order \(a\wedge b\wedge c\). The factor \((-1)^{pq}\) in the last term cancels the sign from moving \(b\) past \(a\). The remaining identity is
\([X,[Y,Z]]=[[X,Y],Z]+[Y,[X,Z]]\), the Lie algebra Jacobi identity. The exterior product rule in DG-CHAR-17 D.1 gives the last identity of (A.2) coefficient by coefficient. Pullback preserves scalar wedges and their coefficients, so it preserves this bracket too.

In particular, for a one-form \(\omega\),
\
[\omega,\omega=2[\omega(v),\omega(w)]_{\mathfrak g}.
\tag{A.4}
\]
For later use the Jacobi identity gives
\[
[\omega,[\omega,\omega]]=0,\qquad
[\omega,[\omega,\alpha]]=\tfrac12[[\omega,\omega],\alpha].
\tag{A.5}
\]
Indeed (A.2) with its first two entries equal to \(\omega\) gives the second equality. With all three entries \(\omega\), it says that twice the first expression equals \([[\omega,\omega],\omega]\), which by graded antisymmetry is its negative. Three times the expression is therefore zero, proving the first equality over the real numbers. □

**Lemma A.2 (insertion, exterior evaluation and Cartan's formula).** For a vector field \(X\), insertion is
\[
(\iota_X\alpha)(X_1,\ldots,X_{k-1})
=\alpha(X,X_1,\ldots,X_{k-1}),
\]
and is zero on functions. It is a derivation of degree \(-1\):
\[
\iota_X(\alpha\wedge\beta)
 =\iota_X\alpha\wedge\beta+(-1)^p\alpha\wedge\iota_X\beta,
\qquad p=\deg\alpha.
\tag{A.6}
\]
For a scalar or fixed-vector-space-valued \(k\)-form,
\[
\begin{aligned}
(d\alpha)(X_0,\ldots,X_k)
={}&\sum_{i=0}^k(-1)^i
 X_i\bigl(\alpha(X_0,\ldots,\widehat X_i,\ldots,X_k)\bigr)\\
&+\sum_{i<j}(-1)^{i+j}
 \alpha([X_i,X_j],X_0,\ldots,\widehat X_i,\ldots,\widehat X_j,\ldots,X_k).
\end{aligned}
\tag{A.7}
\]
Let \(\varphi_t\) be the local flow of \(X\). The Lie derivative
\(\mathcal L_X\alpha=\left.\frac{d}{dt}\right|_0\varphi_t^*\alpha\)
exists and satisfies
\[
\mathcal L_X=d\iota_X+\iota_Xd,\qquad
\mathcal L_Xd=d\mathcal L_X,\qquad
[\mathcal L_X,\iota_Y]=\iota_{[X,Y]},\qquad
[\mathcal L_X,\mathcal L_Y]=\mathcal L_{[X,Y]}.
\tag{A.8}
\]
Its evaluation is
\[
(\mathcal L_X\alpha)(Y_1,\ldots,Y_k)
=X\bigl(\alpha(Y_1,\ldots,Y_k)\bigr)
 -\sum_j\alpha(Y_1,\ldots,[X,Y_j],\ldots,Y_k).
\tag{A.9}
\]
All these statements for fixed-vector-space coefficients mean the corresponding componentwise identities.

**Proof.** Local tools 2.1 gives a smooth local solution \(\varphi_t(x)\) of the autonomous equation. Uniqueness gives \(\varphi_{t+s}(x)=\varphi_t(\varphi_s(x))\) whenever both sides are defined; in particular \(\varphi_{-t}\) is a local inverse. Thus pullback by the flow is well defined and differentiable at zero on a neighbourhood of each point. No complete vector field is required.

For a wedge of one-forms \(\lambda_1\wedge\cdots\wedge\lambda_k\), expansion of its alternating evaluation in the first argument gives
\[
\iota_X(\lambda_1\wedge\cdots\wedge\lambda_k)
=\sum_{j=1}^k(-1)^{j-1}\lambda_j(X)
 \lambda_1\wedge\cdots\wedge\widehat\lambda_j\wedge\cdots\wedge\lambda_k.
\]
Every form is locally a sum of such wedges with smooth scalar coefficients. Dividing this sum into insertions in the first and second factors of a product proves (A.6). Inserting twice also gives
\(\iota_X\iota_Y+\iota_Y\iota_X=0\), since the two first arguments are exchanged.

To verify (A.7), let \(Q\) be its proposed right side. It is alternating: exchanging adjacent arguments reindexes its single-index terms, exchanges the corresponding pairs in its double sum, and reverses the bracket when that pair itself is exchanged. Each resulting term has the opposite sign. It is linear over smooth functions in every argument. By alternation it suffices to check the first argument. Replace \(X_0\) by \(fX_0\). In the term with \(i=j>0\) of the first sum, the extra contribution is
\((-1)^j(X_jf)\alpha(X_0,\ldots,\widehat X_j,\ldots,X_k)\).
In the bracket term indexed by \((0,j)\), use
\([fX_0,X_j]=f[X_0,X_j]-(X_jf)X_0\), which follows from the operator definition of the bracket in PB C.3. This gives exactly the negative of that extra contribution. Every other term simply acquires the factor \(f\). Thus \(Q\) is a differential form. On coordinate vector fields all brackets vanish, and the remaining sum is the alternating derivative of the coefficient functions, exactly the coordinate definition of \(d\) in DG-CHAR-17 D.1. Equality on the coordinate basis proves (A.7).

Pullback preserves wedges. Differentiating this identity for \(\varphi_t\) proves that \(\mathcal L_X\) is a derivation of degree zero. On a function \(f\) it is \(Xf\). Since
\(\varphi_t^*df=d(f\circ\varphi_t)\), smoothness and equality of mixed derivatives, proved in DG-CHAR-17 D.0, give
\(\mathcal L_Xdf=d(Xf)\).

The operator \(d\iota_X+\iota_Xd\) is also a derivation of degree zero. This follows directly by applying the two graded product rules: the two terms involving \(d\alpha\wedge\iota_X\beta\) cancel, as do the two involving \(\iota_X\alpha\wedge d\beta\); the remaining terms are its action on \(\alpha\), wedged with \(\beta\), and \(\alpha\) wedged with its action on \(\beta\). On \(f\) it is \(Xf\), and on \(df\) it is \(d(Xf)\), because \(d^2=0\). Functions and their coordinate differentials generate forms locally, so equality on them proves Cartan's formula. Multiplication of that formula by \(d\) on either side, using \(d^2=0\), proves commutation with \(d\).

The commutator of a degree-zero derivation and a degree-\(-1\) derivation is a degree-\(-1\) derivation: expanding each composition on a product cancels the two mixed terms. Thus \([\mathcal L_X,\iota_Y]\) and \(\iota_{[X,Y]}\) can again be compared on \(f\) and \(df\). Both give zero on \(f\); on \(df\) the first gives \(X(Yf)-Y(Xf)=[X,Y]f\), also the second's value. This proves the third identity. The same product expansion makes \([\mathcal L_X,\mathcal L_Y]\) a degree-zero derivation. It equals \(\mathcal L_{[X,Y]}\) on functions by the definition of the bracket, and on \(df\) by commutation with \(d\). Hence it equals it everywhere.

Finally the proposed right side of (A.9) is a degree-zero derivation on forms: expanding an evaluation of a wedge distributes both differentiation and the bracket replacements over its two factors. It agrees with \(\mathcal L_X\) on functions. On \(df\), evaluated at \(Y\), it is \(X(Yf)-[X,Y]f=Y(Xf)=d(Xf)(Y)\). The same local-generator argument proves (A.9). □

**Lemma A.3 (differentiating the adjoint action and representations).** For a Lie group \(G\) with the bracket of PB C.3,
\[
(d\operatorname{Ad})_e(X)Y=[X,Y].
\tag{A.10}
\]
If \(\rho:G\to\mathrm{GL}(W)\) is a smooth finite dimensional representation and \(r=d\rho_e\), then
\[
r([X,Y])=r(X)r(Y)-r(Y)r(X).
\tag{A.11}
\]
The fundamental vector fields of a right principal action satisfy
\[
[\zeta_X,\zeta_Y]=\zeta_{[X,Y]},
\tag{A.12}
\]
and the left Maurer form \(\theta_g=dL_{g^{-1}}\) satisfies
\[
d\theta+\tfrac12[\theta,\theta]=0.
\tag{A.13}
\]

**Proof.** We first prove the needed naturality for maps that need not be invertible. Suppose \(f:N\to N'\), and fields \(U,V\) on \(N\) are respectively \(f\)-related to \(U',V'\). For a smooth local function \(a\) on \(N'\), the chain rule gives
\[
U(a\circ f)=(U'a)\circ f,\qquad V(a\circ f)=(V'a)\circ f.
\]
Applying these identities twice and subtracting gives
\([U,V](a\circ f)=([U',V']a)\circ f\).
Local coordinate functions on \(N'\) determine tangent vectors, so the brackets are \(f\)-related. This is a local argument and needs no extension of the functions beyond their coordinate neighbourhood.

Write \(L_X(g)=dL_gX\) and \(R_Y(g)=dR_gY\). On \(G\times G\), the fields \((0,L_X)\) and \((R_Y,0)\) commute by the coordinate formula for the bracket: each component depends only on its own factor. Under multiplication \(\mu(a,b)=ab\), they are related to \(L_X\) and \(R_Y\), respectively, as differentiating \(ab\exp(tX)\) and \(\exp(tY)ab\) verifies. Since multiplication is onto, the preceding naturality proves \([L_X,R_Y]=0\).

Differentiation of \(g\exp(tX)=\exp(t\operatorname{Ad}(g)X)g\), the exponential conjugation identity of Local tools 2.3, gives
\[
L_X(g)=R_{\operatorname{Ad}(g)X}(g).
\]
For a fixed basis \(e_j\), write \(\operatorname{Ad}(g)X=\sum_j f_j(g)e_j\). Then \(L_X=\sum_j f_jR_{e_j}\), and the bracket product rule gives
\[
[L_Y,L_X]=\sum_j (L_Y f_j)R_{e_j},
\]
because the left and right fields commute. Evaluating at \(e\) yields
\([Y,X]=\sum_j df_j(e)(Y)e_j=(d\operatorname{Ad})_e(Y)X\).
Renaming \(X,Y\) proves (A.10).

More generally a smooth group homomorphism \(f:G\to H\) relates \(L_X\) to \(L_{df_eX}\), by differentiating \(f(gb)=f(g)f(b)\). Naturality of brackets and evaluation at the identity show that \(df_e\) preserves Lie brackets. On a general linear group, \(L_B(M)=MB\), and the coordinate vector-field formula gives
\(L_B,L_C=MBC-MCB\). Thus its bracket at the identity is \(BC-CB\), proving (A.11). For complex \(W\), the same matrix computation uses its underlying real manifold and complex-linear endomorphisms.

For a fixed \(p\), the orbit map \(a\mapsto pa\) relates \(L_X\) to \(\zeta_X\), since the curve \(a\exp(tX)\) maps to \(pa\exp(tX)\). The same naturality proves (A.12) at all points in that orbit. Every point occurs in some orbit, so the identity holds on \(P\).

Finally \(\theta(L_X)=X\) is constant. Formula (A.7) in degree one therefore gives \(d\theta(L_X,L_Y)=-\theta([L_X,L_Y])=-[X,Y]\). Formula (A.4) gives \(\frac12\theta,\theta=[X,Y]\). The left invariant fields obtained from a basis form a frame everywhere, so these evaluations prove (A.13). □

Let \(P\to M\) have principal connection \(\omega\). Write \(h=\mathrm{id}-\Phi\) for its horizontal projection, as constructed in Conn A.1–A.2.

**Theorem A.4 (the principal curvature form).** The two-form
\[
\Omega=d\omega+\tfrac12[\omega,\omega]
\tag{A.14}
\]
is horizontal and adjoint-equivariant:
\[
\iota_{\zeta_X}\Omega=0,\qquad R_a^*\Omega=\operatorname{Ad}(a^{-1})\Omega.
\tag{A.15}
\]
For horizontal vector fields \(U,V\),
\[
\Omega(U,V)=-\omega([U,V]).
\tag{A.16}
\]
Consequently \(\Omega=h^*d\omega\), where \(h^*\alpha\) means applying \(h\) to each argument. The horizontal distribution is closed under vector-field brackets if and only if \(\Omega=0\).

In a section chart \(p=s(x)g\), put \(A=s^*\omega\). Then
\[
F=s^*\Omega=dA+\tfrac12[A,A],\qquad
\Omega_{s(x)g}(dR_gds(v)+\zeta_X,\ dR_gds(w)+\zeta_Y)
=\operatorname{Ad}(g^{-1})F_x(v,w).
\tag{A.17}
\]
Every tangent vector at \(s(x)g\) has the displayed form, with a unique vertical correction.

**Proof.** The flow of \(\zeta_X\) is \(R_{\exp(tX)}\), because differentiating \(p\exp(tX)\) at time \(t\) gives its fundamental vector, and Local tools 2.3 gives this curve for all \(t\). The equivariance in Conn A.2 and (A.10) give
\[
\mathcal L_{\zeta_X}\omega
=\left.\frac{d}{dt}\right|_0\operatorname{Ad}(\exp(-tX))\omega
=-[X,\omega].
\tag{A.18}
\]
Here \(d\exp_0=\mathrm{id}\) from Local tools 2.3 justifies the chain rule; no exponential-series identity is being assumed. Also \(\iota_{\zeta_X}\omega=X\), a constant zero-form. Cartan's formula yields
\(\iota_{\zeta_X}d\omega=-[X,\omega]\).
From (A.4), \(\frac12\iota_{\zeta_X}[\omega,\omega]=[X,\omega]\). The sum is zero. The fundamental vectors span each vertical space by Conn A.2, proving horizontality.

For fixed \(a\), pullback commutes with \(d\) and the valued bracket. The constant linear map \(\operatorname{Ad}(a^{-1})\) commutes with coefficient differentiation and preserves the Lie algebra bracket by PB C.3. Applying these facts to \(R_a^*\omega=\operatorname{Ad}(a^{-1})\omega\) proves equivariance of \(\Omega\).

If \(U,V\) are horizontal, \(\omega(U)=\omega(V)=0\). Formula (A.7) gives \(d\omega(U,V)=-\omega([U,V])\), and the bracket term in (A.14) vanishes. This proves (A.16). Since \(\Omega\) is horizontal, all its values are recovered by horizontally projecting its two arguments; on those arguments it is \(d\omega\). This is \(\Omega=h^*d\omega\).

Every horizontal tangent vector extends locally to a horizontal field by expanding it in a smooth horizontal frame, whose existence is Conn A.1. Thus vanishing of \(\Omega\) is equivalent to \(\omega([U,V])=0\) for all local horizontal fields, which is precisely the asserted closure under brackets. No existence theorem for integral leaves is claimed in this equivalence.

Pulling (A.14) back by \(s\) proves the formula for \(F\). The projection of \(dR_gds(v)\) is \(v\). Subtracting it from an arbitrary tangent vector with base projection \(v\) leaves a vertical vector, uniquely \(\zeta_X\) by Conn A.2. Horizontality removes both vertical corrections in (A.17), and equivariance evaluates the remaining pair as \(\operatorname{Ad}(g^{-1})s^*\Omega(v,w)\). □

**Theorem A.5 (valued horizontal forms and the covariant exterior derivative).** Let \(\rho:G\to\mathrm{GL}(W)\) be a smooth representation, \(r=d\rho_e\), and \(E=P\times_GW\). Horizontal equivariant forms
\[
\alpha\in\Omega^k(P,W),\qquad R_a^*\alpha=\rho(a^{-1})\alpha,
\]
correspond bijectively to \(E\)-valued \(k\)-forms on \(M\). Their covariant exterior derivative is
\[
D\alpha=h^*d\alpha=d\alpha+B\wedge\alpha,\qquad B=r(\omega)\in\Omega^1(P,\operatorname{End}(W)).
\tag{A.19}
\]
For \(k=0\), this is exactly the covariant derivative of Conn D.1. In a section chart it is
\[
D\alpha_s=d\alpha_s+r(A)\wedge\alpha_s,\qquad \alpha_s=s^*\alpha.
\tag{A.20}
\]
The product \(B\wedge\alpha\) uses matrix action after the shuffle product. These constructions include real and complex representations.

**Proof.** For a horizontal equivariant \(\alpha\), define the base form at \(x\) by
\[
\beta_x(v_1,\ldots,v_k)=[p,\alpha_p(w_1,\ldots,w_k)],
\qquad p\in P_x,\quad d\pi(w_i)=v_i.
\tag{A.21}
\]
Surjectivity of \(d\pi\) provides lifts. Changing any lift by a vertical vector makes no change by horizontality. Replacing \(p\) by \(pa\), use \(dR_aw_i\) as lifts. Equivariance and the associated relation give
\([pa,\rho(a^{-1})\alpha_p(w_1,\ldots,w_k)]=[p,\alpha_p(w_1,\ldots,w_k)]\).
This proves well-definedness. In the section \(s\) its coordinates are \(s^*\alpha\), hence smooth.

Conversely a base form \(\beta\) determines a unique \(\alpha_p(w_1,\ldots,w_k)\) by (A.21), because \(u\mapsto[p,u]\) is a linear isomorphism onto \(E_x\) by PB B.1. In local charts this inverse is
\(\rho(g^{-1})\beta_s(d\pi(w_1),\ldots,d\pi(w_k))\);
it is smooth, horizontal and equivariant. Both constructions are pointwise inverse. For \(k=0\) they are the section/function correspondence in PB B.2.

For the derivative, the horizontal projection commutes with constant right translations, by Conn A.2. Therefore \(h^*d\alpha\) is horizontal and has the same equivariance as \(\alpha\). We show it equals the last expression in (A.19). Differentiating equivariance along \(R_{\exp(tX)}\), as in (A.18), gives
\(\mathcal L_{\zeta_X}\alpha=-r(X)\alpha\).
Since \(\iota_{\zeta_X}\alpha=0\), Cartan's formula gives
\(\iota_{\zeta_X}d\alpha=-r(X)\alpha\).
The insertion product rule, applied coefficientwise, gives
\[
\iota_{\zeta_X}(B\wedge\alpha)
=(\iota_{\zeta_X}B)\alpha-B\wedge\iota_{\zeta_X}\alpha
=r(X)\alpha.
\]
Thus \(d\alpha+B\wedge\alpha\) is horizontal. On entirely horizontal arguments the term \(B\wedge\alpha\) is zero, since each shuffle evaluates \(B\) on one of those arguments. Its value is consequently \(d\alpha\) there, the value of \(h^*d\alpha\). Horizontality now proves equality on all arguments. Pullback by \(s\) gives (A.20). For \(k=0\), \(h^*du\) evaluated on a tangent vector with base value \(v\) is \(du(L_pv)\), the defining formula in Conn D.1. □

**Theorem A.6 (Bianchi and the square of the derivative).** For adjoint-equivariant horizontal forms, the covariant derivative is \(D\alpha=d\alpha+[\omega,\alpha]\). It satisfies
\[
D\Omega=0,\qquad D^2\alpha=[\Omega,\alpha].
\tag{A.22}
\]
For any representation as in A.5,
\[
D^2\alpha=r(\Omega)\wedge\alpha.
\tag{A.23}
\]

**Proof.** For the adjoint representation, (A.10) says that its derivative is \(X\mapsto[X,\,\cdot\,]\). Thus A.5 gives the stated expression for \(D\).

Using (A.2) and the fact that \(d\omega\) has degree two,
\[
d\Omega
=\tfrac12\bigl([d\omega,\omega]-[\omega,d\omega]\bigr)
=-[\omega,d\omega].
\]
Adding \([\omega,\Omega]=[\omega,d\omega]+\frac12[\omega,[\omega,\omega]]\) yields zero by (A.5). The form \(\Omega\) is horizontal and equivariant by A.4, so this algebraic calculation is indeed its covariant derivative.

For any \(\mathfrak g\)-valued form \(\alpha\), direct expansion gives
\[
\begin{aligned}
(d+[\omega,\,\cdot\,])^2\alpha
&=[d\omega,\alpha]-[\omega,d\alpha]+[\omega,d\alpha]
  +[\omega,[\omega,\alpha]]\\
&=[d\omega+\tfrac12[\omega,\omega],\alpha]
=[\Omega,\alpha].
\end{aligned}
\]
For basic forms A.5 makes each successive application the covariant derivative and preserves basicness, proving (A.22).

For the general representation put \(B=r(\omega)\). The ordinary product rule for matrix-valued forms follows by summing scalar wedge products over matrix indices. It gives
\[
(d+B\wedge)^2\alpha=(dB+B\wedge B)\wedge\alpha.
\]
The two terms containing \(B\wedge d\alpha\) have opposite signs and cancel. At two tangent vectors \(v,w\), (A.11) gives
\[
(B\wedge B)(v,w)
=r(\omega(v))r(\omega(w))-r(\omega(w))r(\omega(v))
=r([\omega(v),\omega(w)]).
\]
As \(r\) is constant and linear, \(dB=r(d\omega)\); hence \(dB+B\wedge B=r(\Omega)\). This proves (A.23) without an additional representation identity. □

**Theorem A.7 (changes of section, pullbacks and associated curvature).** If \(s'=sa\), where \(a:U\to G\) is smooth, then
\[
F'=\operatorname{Ad}(a^{-1})F.
\tag{A.24}
\]
For a smooth map \(f:N\to M\), the pullback principal bundle has the pulled-back connection, and its curvature is the pullback of \(\Omega\). On the associated vector bundle, the curvature operator
\[
R^\nabla(X,Y)\sigma
=\nabla_X\nabla_Y\sigma-\nabla_Y\nabla_X\sigma-\nabla_{[X,Y]}\sigma
\tag{A.25}
\]
has local matrix \(r(F(X,Y))\). In particular its action is independent of the chosen frame.

**Proof.** Differentiating \(s'(x)=s(x)a(x)\) splits \(ds'(v)\) into \(dR_{a(x)}ds(v)\) and a vertical vector. Both vertical corrections vanish when inserted in \(\Omega\), and constant right equivariance at the point gives
\((s')^*\Omega(v,w)=\operatorname{Ad}(a(x)^{-1})s^*\Omega(v,w)\).
This is (A.24), valid even though \(a\) varies with \(x\).

PB A.3 constructs \(f^*P=\{(y,p):f(y)=\pi(p)\}\) with smooth local principal charts and projection \(q:f^*P\to P\). The form \(q^*\omega\) reproduces fundamental vectors, since \(dq\) sends their generators to those of \(P\), and it is equivariant since \(q\) commutes with the actions. Conn A.2 therefore makes it a connection. Pullback commutes with \(d\) and the coefficient bracket by DG-CHAR-17 D.1 and A.1. Applying (A.14) shows its curvature is \(q^*\Omega\). In a pulled-back section, its base curvature is \(f^*F\).

For the operator identity use a section chart, write the local coefficient of \(\sigma\) as \(u\), and set \(B=r(A)\). Conn D.1 gives \(\nabla_Xu=Xu+B(X)u\). Expanding the first two terms of (A.25) and subtracting the third cancels the second derivatives of \(u\), since \(XYu-YXu=[X,Y]u\), and cancels the terms in \(Xu,Yu\) paired with \(B\). What remains is
\[
\bigl(X(B(Y))-Y(B(X))-B([X,Y])
      +B(X)B(Y)-B(Y)B(X)\bigr)u.
\]
Formula (A.7) identifies the first three coefficients with \(dB(X,Y)\). As in A.6, the whole matrix is
\((dB+B\wedge B)(X,Y)=r(F(X,Y))\).
The operator on the left of (A.25) is defined by the intrinsic derivative of Conn D.1, so it is independent of the frame. This calculation also proves directly that it is linear over smooth functions in \(X,Y,\sigma\), since its final expression is evaluation of an endomorphism-valued two-form. □

The constructions in this part use Peter W. Michor's [freely accessible author draft of *Topics in Differential Geometry*](https://www.mat.univie.ac.at/~michor/dgbook.pdf), Sections 4.12–4.14, 4.24, 9.6–9.9, 19.2 and 19.5. The proofs above explicitly supply the differential and Lie algebra identities needed here. They do not use the later Frölicher–Nijenhuis assertions, general holonomy theorems or an external citation in place of a programme proof.

Original exposition: GPT-6 Astra (OpenAI), October 2026, CC0 1.0. No source prose, diagrams or PDF pages are reproduced.

## B. Curvature from iterated vertical derivatives

Let \(\pi:E\to M\) be a smooth fibre bundle. Its vertical bundle \(VE=\ker d\pi\) is a vector bundle over \(E\), and also a fibre bundle over \(M\), with fibre \(T(E_x)\) at \(x\). Here \(V(VE)\) always means the vertical bundle of \(VE\to M\). Its fibre over \(x\) is \(T(T(E_x))\). Distinguishing these two base spaces is essential when subtracting second derivatives.

**Lemma B.1 (the interchange map and its affine fibres).** On \(V(VE)\) there is a canonical smooth involution \(\kappa\). In local fibre coordinates its rule is
\[
\kappa(x;y,u;v,w)=(x;y,v;u,w).
\tag{B.1}
\]
Our order is the ordinary tangent order: \((x;y,u)\) is the point of \(VE\), and \((v,w)\) is its vertical tangent vector. Thus for a two-parameter map \(a(t,\epsilon)\) inside a fixed fibre, representing
\(\left.\partial_t\right|_0\left.\partial_\epsilon\right|_0a(t,\epsilon)\),
we have
\[
y=a(0,0),\quad u=\partial_\epsilon a(0,0),\quad
v=\partial_t a(0,0),\quad w=\partial_t\partial_\epsilon a(0,0).
\]
The double projection is
\[
\Pi(x;y,u;v,w)=((x;y,u),(x;y,v))\in VE\times_E VE.
\tag{B.2}
\]
Each fibre of \(\Pi\) is an affine space modelled on \(V_{(x,y)}E\). Its canonical difference is
\[
(x;y,u;v,w)-_\Pi(x;y,u;v,\widehat w)
=(x;y,w-\widehat w).
\tag{B.3}
\]
Every smooth bundle map \(F:E\to E'\) over \(M\) induces maps \(VF,VVF\); they commute with \(\kappa\), and \(VVF\) preserves these affine differences with linear part \(VF\).

**Proof.** PB C.2 supplies the tangent construction and its coordinate changes. In a bundle chart, a curve in \(T(E_x)\) has local data \(t\mapsto(y(t),u(t))\); its tangent at zero is the displayed quadruple. Every such quadruple is represented by a two-parameter map, using
\(a(t,\epsilon)=y+tv+\epsilon u+t\epsilon w\)
in a coordinate neighbourhood and restricting both parameters sufficiently near zero. Equality of the four coordinates is therefore precisely equality of the resulting tangent vectors in \(T(T(E_x))\).

For a change of fibre coordinates \(z=f(x,y)\), keep \(x\) fixed while taking the two fibre derivatives. The chain and product rules give
\[
\begin{aligned}
z&=f(x,y),&
u_z&=f_yu,&
v_z&=f_yv,\\
w_z&=f_yw+f_{yy}(v,u).
\end{aligned}
\tag{B.4}
\]
Here \(f_y\) and \(f_{yy}\) are evaluated at \((x,y)\). The Hessian is symmetric by Local tools 0.3 and PB C.3's mixed-partial proof. Consequently exchanging \(u,v\) commutes with (B.4), so (B.1) defines a chart-independent smooth involution. This also proves that it interchanges the two projections in (B.2).

At fixed \(x,y,u,v\), (B.4)'s last line is an affine bijection in \(w\), with linear part \(f_y\). Subtracting two such lines cancels the Hessian term and transforms their difference by \(f_y\), the coordinate transformation of a vertical vector. This proves (B.3) is intrinsic. Adding a vertical vector to \(w\) defines a free transitive action on each fibre, independent of coordinates by the same calculation, which proves the affine-space assertion.

For a smooth map \(F\) over \(M\), use its local expression \((x,y)\mapsto(x,f(x,y))\). The derivative formula is still (B.4), even when \(f_y\) is not invertible. Symmetry of \(f_{yy}\) again proves commutation with \(\kappa\), and cancellation of its common Hessian term proves preservation of affine differences. No rank hypothesis on \(F\) is needed. □

**Theorem B.2 (the induced connection on the vertical bundle).** Let \(\Phi:TE\to VE\) be a connection projection as in Conn A.1. For a local section \(s\) and a base vector field \(X\), write
\[
D_Xs=\Phi(ds(X))\in\Gamma(VE|_s).
\tag{B.5}
\]
There is a unique connection \(\Phi^V\) on \(VE\to M\) such that for every smooth one-parameter family \(s_\epsilon\) of local sections,
\[
D^V_X\left(\left.\partial_\epsilon\right|_0s_\epsilon\right)
=\kappa\left(\left.\partial_\epsilon\right|_0D_Xs_\epsilon\right).
\tag{B.6}
\]
In bundle coordinates \((x^i,y^a)\), set
\[
\Phi(\partial_{x^i})=\Gamma_i^a(x,y)\partial_{y^a},\qquad
\Phi(\partial_{y^a})=\partial_{y^a}.
\]
Repeated fibre indices are summed. On \(VE\), with coordinates \((x,y,u)\), the induced projection fixes \(\partial_{y^a},\partial_{u^a}\) and has
\[
\Phi^V(\partial_{x^i})
=\Gamma_i^a\partial_{y^a}
+(\partial_{y^b}\Gamma_i^a)u^b\partial_{u^a}.
\tag{B.7}
\]
For a section \((s,u)\) of \(VE\to M\), this says
\[
D^V_X(s,u)
=(x;s,u;\ Xs+\Gamma_X,\ Xu+(\partial_y\Gamma_X)u),
\qquad \Gamma_X=X^i\Gamma_i(x,s).
\tag{B.8}
\]
In \(\partial_y\Gamma_X\), \(X^i\) depends only on the base coordinate.

**Proof.** Conn A.1 gives exactly the displayed local form of \(\Phi\), and hence
\(D_Xs=(x;s,Xs+\Gamma_X(x,s))\).
For \(u=\partial_\epsilon s_\epsilon|_0\), differentiating this expression gives, in the ordinary tangent order of B.1,
\[
\left.\partial_\epsilon\right|_0D_Xs_\epsilon
=(x;s,\ Xs+\Gamma_X;\ u,\ Xu+(\partial_y\Gamma_X)u).
\]
Applying \(\kappa\) gives (B.8).

Conversely (B.7), extended linearly and smoothly, defines a projection onto the vertical tangent space of \(VE\to M\): it is the identity on that space, and all displayed values are vertical. Conn A.1 therefore makes it a connection in each coordinate neighbourhood. Every local section \((s,u)\) is locally the variation of some family \(s_\epsilon\), by taking \(s_\epsilon(x)=s(x)+\epsilon u(x)\) in fibre coordinates near the point in question and restricting the neighbourhood and parameter if necessary. Formula (B.6) thus determines its covariant derivative on every local section.

Both variation and the interchange map are intrinsic by B.1, so two coordinate constructions satisfying (B.6) give the same derivatives on all sections on their overlap. These derivatives determine the projection itself: in fibre coordinates, through any specified point use a section with constant fibre coordinates; its differential on each base coordinate vector is that coordinate vector. The derivative supplies the projection of those base vectors, and the projection on all vertical vectors is already the identity. The local projections therefore agree and glue to a smooth global connection. This also proves uniqueness. □

**Theorem B.3 (the nonlinear curvature and its commutator formula).** Put \(h=\mathrm{id}-\Phi\). The formula
\[
\mathcal R(U,V)=-\Phi[hU,hV]
\tag{B.9}
\]
defines a smooth horizontal \(VE\)-valued two-form on \(E\). Equivalently,
\[
\mathcal R(U,V)
=-\Phi[U,V]+\Phi[U,\Phi V]+\Phi[\Phi U,V]-[\Phi U,\Phi V].
\tag{B.10}
\]
Its fibre-coordinate coefficients are
\[
\mathcal R^a_{ij}
=\partial_i\Gamma_j^a-\partial_j\Gamma_i^a
+(\partial_b\Gamma_i^a)\Gamma_j^b
-(\partial_b\Gamma_j^a)\Gamma_i^b.
\tag{B.11}
\]
Here \(\partial_i\) differentiates the base variable at fixed \(y\), and \(\partial_b\) differentiates the fibre variable. For arbitrary base vector fields \(X,Y\) and any local section \(s\),
\[
\mathcal R(ds(X),ds(Y))
=\bigl(D^V_XD_Ys-_\Pi\kappa(D^V_YD_Xs)\bigr)-D_{[X,Y]}s.
\tag{B.12}
\]
The inner difference uses the affine fibres in B.1. The outer difference is ordinary subtraction in \(V_{s(x)}E\).

**Proof.** For a smooth scalar \(f\), \(h(fU)=fhU\), and
\([fhU,hV]=f[hU,hV]-(hVf)hU\).
The second term is killed by \(\Phi\). Thus (B.9) is linear over functions in its first argument, and by antisymmetry also in its second. It is horizontal because \(h\) kills vertical arguments, and takes vertical values by its definition. The coordinate bracket formula in PB C.3 proves smoothness.

Vertical fields are closed under brackets: in a bundle chart they have only \(\partial_y\) components, and their bracket still has only those components. In particular
\(\Phi[\Phi U,\Phi V]=[\Phi U,\Phi V]\).
Expanding \(h=\mathrm{id}-\Phi\) in (B.9) gives (B.10).

The horizontal lifts of coordinate fields are
\(H_i=\partial_i-\Gamma_i^a\partial_a\).
Their bracket has zero base components and fibre coefficient
\[
-\partial_i\Gamma_j^a+\partial_j\Gamma_i^a
+\Gamma_i^b\partial_b\Gamma_j^a-\Gamma_j^b\partial_b\Gamma_i^a.
\]
Applying \(-\Phi\) changes its sign, yielding (B.11). Since \(\mathcal R\) is horizontal, this also gives its value on the original coordinate vectors \(\partial_i,\partial_j\).

We prove (B.12) for general \(X,Y\), including their variable coefficients. In the fixed bundle chart write
\[
u_X=Xs+\Gamma_X(x,s),\qquad u_Y=Ys+\Gamma_Y(x,s).
\]
Formula (B.8) yields
\[
\begin{aligned}
D^V_XD_Ys&=(x;s,u_Y;\ u_X,\ Z_{XY}),&
Z_{XY}&=Xu_Y+(\partial_y\Gamma_X)u_Y,\\
D^V_YD_Xs&=(x;s,u_X;\ u_Y,\ Z_{YX}),&
Z_{YX}&=Yu_X+(\partial_y\Gamma_Y)u_X.
\end{aligned}
\]
After applying \(\kappa\) to the second expression, both have double projection \((u_Y,u_X)\); the affine difference is therefore \((x;s,Z_{XY}-Z_{YX})\). To expand its last component, distinguish \(X^i\partial_i\), acting on a function of \((x,y)\) while \(y\) is fixed, from the derivative of that function evaluated at \(y=s(x)\). The chain rule gives
\[
\begin{aligned}
Z_{XY}-Z_{YX}
={}&[X,Y]s+\Gamma_{[X,Y]}\\
&+X^iY^j\bigl(
\partial_i\Gamma_j-\partial_j\Gamma_i
+(\partial_y\Gamma_i)\Gamma_j-(\partial_y\Gamma_j)\Gamma_i\bigr)(x,s).
\end{aligned}
\tag{B.13}
\]
Here is the cancellation explicitly. In \(X(\Gamma_Y(x,s))\), differentiation of \(Y^j\) contributes \((XY^j)\Gamma_j\); subtracting the corresponding \(Y(\Gamma_X(x,s))\) contribution leaves \(\Gamma_{[X,Y]}\). Differentiating \(s\) in those two terms contributes
\((\partial_y\Gamma_Y)Xs-(\partial_y\Gamma_X)Ys\).
The last two terms in \(Z_{XY}-Z_{YX}\), after substituting \(u_Y,u_X\), contain precisely the negatives of these contributions, plus
\((\partial_y\Gamma_X)\Gamma_Y-(\partial_y\Gamma_Y)\Gamma_X\).
Finally \(X(Ys)-Y(Xs)=[X,Y]s\) by PB C.3. The remaining base derivatives are exactly the first two entries in the second line of (B.13). This proves the displayed expansion without assuming coordinate fields commute in the original formula.

Subtracting \(D_{[X,Y]}s=(x;s,[X,Y]s+\Gamma_{[X,Y]})\) leaves \(X^iY^j\mathcal R_{ij}\) by (B.11). Since \(d\pi\,ds=\mathrm{id}\) and \(\mathcal R\) is horizontal, this is \(\mathcal R(ds(X),ds(Y))\). All differences used above are the intrinsic ones of B.1, so the coordinate proof proves (B.12) globally on the section's domain. □

**Theorem B.4 (parallel maps and naturality).** A smooth bundle map \(F:E\to E'\) over \(M\) is parallel when
\[
dF\circ\Phi=\Phi'\circ dF.
\tag{B.14}
\]
This is equivalent to sending horizontal vectors into horizontal vectors. Its vertical derivative \(VF:VE\to VE'\) is then parallel for the connections of B.2, and
\[
dF\bigl(\mathcal R(U,V)\bigr)=\mathcal R'(dF(U),dF(V)).
\tag{B.15}
\]
Neither an invertibility hypothesis nor a constant-rank hypothesis on \(F\) is needed.

**Proof.** The identity \(\pi'F=\pi\) implies \(dF(VE)\subset VE'\). If (B.14) holds, horizontal vectors map to horizontal vectors. Conversely decompose each tangent vector into its horizontal and vertical components. The first maps horizontally by assumption, and the second vertically, where both projections act as the identity. This gives (B.14).

For a local section \(s\), (B.14) gives
\(D'_X(Fs)=VF(D_Xs)\).
Differentiate this identity for a family \(s_\epsilon\), apply \(\kappa\) and use B.1's naturality of the interchange map. B.2 then gives
\[
D'^{\,V}_X(VF(v))=VVF(D^V_Xv)
\]
for every local variation \(v\), hence for every local section of \(VE\). The section test used at the end of B.2 proves that \(VF\) is parallel.

For the curvature statement one can use (B.12) and preservation of its affine differences from B.1. Here is also a direct bracket proof. A local base field \(X\) has a unique horizontal lift \(H_X\) on either bundle, by Conn A.1. Parallelness and \(d\pi'H_X'=X\) show that \(H_X,H_X'\) are \(F\)-related. A.3's bracket naturality for arbitrary smooth maps makes their brackets \(F\)-related. Applying the commuting vertical projections and negating yields (B.15) on two horizontal lifts. At any point, such lifts attain every pair of horizontal tangent vectors. Horizontality of both curvatures and (B.14) extend the identity to arbitrary \(U,V\). □

**Lemma B.5 (the interchange map in a principal trivialization).** For a principal \(G\)-bundle, identify \(VP\) with \(P\times\mathfrak g\) by \(\zeta_X(p)\leftrightarrow(p,X)\), as proved in Conn A.2. For \(\xi\in V(VP)\), use coordinates
\[
\Psi(\xi)=(p,X;Y,Z),
\tag{B.16}
\]
where \(X\) is the left-trivialized outer velocity of the point \(p\), \(Y\) is the inner vertical vector at \(p\), and \(Z\) is the derivative of that inner vector's Lie algebra coordinate along the outer variation. This deliberately places the outer coordinate first. Then
\[
\Psi\kappa\Psi^{-1}(p,X;Y,Z)
=(p,Y;X,Z+[X,Y]).
\tag{B.17}
\]
An explicit representative for \(\Psi^{-1}\) is
\[
\left.\partial_t\right|_0\left.\partial_\epsilon\right|_0
 p\exp(tX)\exp\bigl(\epsilon(Y+tZ)\bigr).
\tag{B.18}
\]
The two-parameter surface inside (B.18) has the same value, two first derivatives and mixed derivative at zero as
\[
p\exp\bigl(tX+\epsilon Y+t\epsilon(Z+\tfrac12[X,Y])\bigr).
\tag{B.19}
\]
Thus the required mixed-order exponential identity is proved here without presupposing a Baker–Campbell–Hausdorff expansion.

**Proof.** The map \(VP\to P\times\mathfrak g\) is a smooth bundle isomorphism over \(M\) by Conn A.2. Its vertical derivative identifies \(V(VP)\) with \(V(P\times\mathfrak g)\). In ordinary tangent coordinates the latter has order \((p,Y;X,Z)\); permuting \(X,Y\) gives (B.16), so \(\Psi\) is a smooth diffeomorphism.

For (B.18), at \(\epsilon=0\) the point is \(p\exp(tX)\), whose outer velocity has coordinate \(X\). Its \(\epsilon\)-derivative has left Lie coordinate \(Y+tZ\) because it is right multiplication of that point by \(\exp(\epsilon(Y+tZ))\). Therefore the inner coordinate and its derivative are \(Y,Z\), proving the inverse formula.

To compute the swap, choose a fibre identification \(G\to P_x,\ a\mapsto pa\). A general two-parameter surface in that fibre has group coordinate \(a(t,\epsilon)\) with \(a(0,0)=e\). Put
\[
U=\theta(a_t),\qquad V=\theta(a_\epsilon).
\]
The pullback of the Maurer–Cartan identity (A.13) to the parameter rectangle gives
\[
\partial_tV-\partial_\epsilon U=-[U,V].
\tag{B.20}
\]
At the origin the original coordinates are \(X=U(0,0)\), \(Y=V(0,0)\), \(Z=\partial_tV(0,0)\). Swapping the parameters gives the last coordinate \(\partial_\epsilon U(0,0)=Z+[X,Y]\), proving (B.17). For equal \(p,X,Y\), the affine difference of two elements is the vertical vector with Lie coordinate \(Z-\widehat Z\): in any fibre chart, differentiating the left Maurer trivialization adds a term bilinear in the common first velocities, which cancels in the difference. The remaining linear factor is precisely \(\theta_p\). This also follows directly by applying the chain rule to (B.16).

For completeness we prove (B.19)'s exact mixed coefficient. Local tools 2.3 gives a smooth exponential chart near \(0\in\mathfrak g\). Pull \(\theta\) back to that chart and denote the resulting smoothly varying linear map by \(a_z:\mathfrak g\to\mathfrak g\); thus \(a_0=\mathrm{id}\). On a radial exponential curve, the one-parameter-group property gives \(a_{tW}W=W\). Consequently the bilinear map
\(B(U,V)=(da)_0(U)V\)
satisfies \(B(W,W)=0\). Expanding this equality at \(U+V\) proves \(B(U,V)=-B(V,U)\). Maurer–Cartan at zero gives
\[
B(U,V)-B(V,U)=-[U,V],
\]
so \(B(U,V)=-\tfrac12[U,V]\).

Let \(z(t,\epsilon)\) be the logarithm, in this chart, of
\(\exp(tX)\exp(\epsilon(Y+tZ))\).
Then \(z(t,0)=tX\), \(z_t(0,0)=X\), \(z_\epsilon(0,0)=Y\), and
\[
a_{z(t,0)}z_\epsilon(t,0)=Y+tZ.
\]
Differentiating in \(t\) at zero yields
\(B(X,Y)+z_{t\epsilon}(0,0)=Z\), hence
\(z_{t\epsilon}(0,0)=Z+\frac12[X,Y]\).
These are exactly the value, first derivatives and mixed derivative of the exponent in (B.19). Applying the smooth exponential map preserves equality of these four jets by the chain rule, as in (B.4). This proves the asserted equality in \(V(VP)\); it makes no claim about the unmixed second derivatives. □

**Theorem B.6 (the principal commutator recovers the structure equation).** For a principal connection, the vertical trivialization \(VP\to P\times\mathfrak g\) is parallel when the target carries the product of the original connection on \(P\) and the trivial connection on \(\mathfrak g\). For a section \(s\) put \(a_X=(s^*\omega)(X)\). In the coordinate order of B.5,
\[
\Psi(D^V_XD_Ys)=(s,a_X;\ a_Y,\ Xa_Y).
\tag{B.21}
\]
The nonlinear curvature is \(\mathcal R=\zeta_\Omega\), and (B.12) in these coordinates becomes
\[
\zeta^{-1}\mathcal R(ds(X),ds(Y))
=Xa_Y-Ya_X-a_{[X,Y]}+[a_X,a_Y]
=(s^*\Omega)(X,Y).
\tag{B.22}
\]

**Proof.** First \(\mathcal R(U,V)=-\Phi[hU,hV]\), whereas A.4 gives
\(\Omega(U,V)=-\omega([hU,hV])\).
Since \(\Phi=\zeta\omega\) by Conn A.2, this proves \(\mathcal R=\zeta_\Omega\), with the same minus sign in both definitions.

We prove the claimed parallelness explicitly. A local section of \(VP\), in vertical trivialization, is a pair \((s,v)\) with \(v:U\to\mathfrak g\). It is the variation at zero of
\(s_\epsilon=s\exp(\epsilon v)\).
Let \(a=s^*\omega\). Conn A.3 gives
\[
s_\epsilon^*\omega
=\operatorname{Ad}(\exp(-\epsilon v))a
+(\exp(\epsilon v))^*\theta.
\]
Differentiating this expression with respect to \(\epsilon\) at zero, and then evaluating on \(X\), gives
\[
\left.\partial_\epsilon\right|_0(s_\epsilon^*\omega)(X)
=-[v,a_X]+Xv.
\tag{B.23}
\]
The first term is (A.10). For the second, in B.5's exponential chart it is \(a_{\epsilon v}(\epsilon Xv)\); differentiating at zero gives \(Xv\), since \(a_0=\mathrm{id}\). This justifies the derivative even for variable \(v\).

Before applying \(\kappa\), the variation of \(D_Xs_\epsilon\) therefore has coordinates
\((s,v;\ a_X,\ -[v,a_X]+Xv)\).
By (B.17), after the swap its coordinates are
\((s,a_X;\ v,\ Xv)\).
B.2 identifies this with \(D^V_X(s,v)\). Under the ordinary target coordinates on \(V(P\times\mathfrak g)\), it is precisely the pair consisting of \(D_Xs\) and the ordinary derivative \(Xv\). That is the covariant derivative for the product connection: its projection sends a tangent \((w,z)\) to \((\Phi w,z)\), a vertical vector for \(P\times\mathfrak g\to M\). The section test in B.2 now proves parallelness on all tangent vectors.

Take \(v=a_Y\) to obtain (B.21). The second iterated derivative, after swapping, is
\[
\Psi\kappa(D^V_YD_Xs)
=(s,a_X;\ a_Y,\ Ya_X+[a_Y,a_X]).
\]
Both double projections agree. By B.5 their affine difference has Lie coordinate
\(Xa_Y-Ya_X-[a_Y,a_X]=Xa_Y-Ya_X+[a_X,a_Y]\).
Subtracting \(D_{[X,Y]}s\) subtracts \(a_{[X,Y]}\). Formula (A.7) and (A.4) identify the result with
\((da+\frac12[a,a])(X,Y)\), which is \(s^*\Omega(X,Y)\) by A.4. This proves (B.22) and reconstructs the structure equation through the nonlinear commutator with every subtraction specified. □

**Lemma B.7 (the linear case and its matrix curvature).** Let \(E\to M\) be a real vector bundle. A smooth connection projection on its total space is preserved by every fibre dilation \(v\mapsto\lambda v\) if and only if in every linear bundle chart
\[
\Gamma_i(x,v)=A_i(x)v.
\tag{B.24}
\]
In that case, under the canonical vertical identification \(VE=E\times_M E\), its reduced derivative is
\[
\nabla_Xs=Xs+A(X)s,
\]
and is linear over real constants in \(s\), linear over smooth functions in \(X\), and satisfies the Leibniz rule. Conversely real bilinearity of the reduced derivative in \(X,s\) forces (B.24). Its curvature is fibrewise linear, with
\[
\mathcal R(\partial_i,\partial_j)_{(x,v)}
=\bigl(\partial_iA_j-\partial_jA_i+[A_i,A_j]\bigr)v.
\tag{B.25}
\]

**Proof.** In a linear bundle chart a dilation sends
\(\partial_i-\Gamma_i(x,v)\partial_v\)
to
\(\partial_i-\lambda\Gamma_i(x,v)\partial_v\)
at \((x,\lambda v)\). By B.4 it is parallel exactly when
\(\Gamma_i(x,\lambda v)=\lambda\Gamma_i(x,v)\).
The value \(\lambda=0\) gives \(\Gamma_i(x,0)=0\). Differentiating the equality in \(\lambda\) at zero gives
\(\Gamma_i(x,v)=d_v\Gamma_i(x,0)v\).
Thus smooth homogeneity actually gives linearity, and the matrix \(A_i(x)=d_v\Gamma_i(x,0)\) is smooth. Conversely (B.24) visibly gives the required homogeneity.

For a vector bundle the canonical vertical identification sends the derivative of a fibre curve \(v(t)\) to \((v(0),v'(0))\), using its vector-space difference quotient. Linear transition maps preserve this rule, so it is global. Formula (B.5) in this identification gives the asserted reduced derivative. The ordinary product rule proves its three properties. Conversely, fix \(x\) and \(i\), and choose local sections with constant coefficient values \(v,w\) near \(x\). Additivity and homogeneity in these sections make \(v\mapsto\Gamma_i(x,v)\) linear. If bilinearity was originally stated only for global sections, a smooth cutoff equal to one near \(x\), provided by Local tools 3.1, extends these local sections by zero; the same values and derivatives at \(x\) give the conclusion. Smoothness again gives smooth \(A_i\).

Finally substitute (B.24) into (B.11). The fibre derivatives are \(A_i,A_j\), so the last two terms become \(A_iA_jv-A_jA_iv\); the base derivatives are \((\partial_iA_j-\partial_jA_i)v\). This proves (B.25), the usual matrix formula, directly from nonlinear curvature. The commutator interpretation also follows from B.12 or the explicit operator expansion in A.7. □

This part reconstructs the mathematical arguments of Gustavo Amilcar Saldaña Moncada and Gregor Weingart, [*On Connections and their Curvatures*, freely accessible arXiv version 2207.06542v1](https://arxiv.org/abs/2207.06542v1), Sections 2–4 and Appendix A. The connection axioms used earlier are already proved in Conn A.1–A.3. The new proofs above include coordinate independence, arbitrary-field cancellation, induced-connection existence and uniqueness, parallelness of the principal vertical trivialization, and the exact mixed exponential identity. The source's ordinary and reordered tangent coordinates are distinguished explicitly.

Original exposition: GPT-6 Astra (OpenAI), October 2026, CC0 1.0. This is newly written exposition and proof completion from the freely accessible paper; its prose, diagrams and page images are not reproduced. The human construction source is credited above.

## C. Smooth subgroup generation and holonomy

This part supplies the topology and parameter arguments required to treat **all finitely piecewise \(C^1\) paths**. Such a path is continuous on a compact interval and \(C^1\) on each member of a finite subdivision, with finite continuous one-sided derivatives at its endpoints. A homotopy of paths or loops means a continuous homotopy with the stated endpoints fixed. It is not assumed smooth.

**Theorem C.1 (a subgroup generated by smooth families).** Let \(G\) be a finite dimensional Lie group. Let \(\mathcal C\) be any family of smooth maps
\(c:D_c\to G\), where \(D_c\) is a connected open subset of a finite dimensional Euclidean space and \(e\in c(D_c)\). Let \(H\) be the subgroup generated by their values. Then \(H\) has a connected, Hausdorff, second-countable Lie-group structure for which \(H\hookrightarrow G\) is an injective immersion. Every generating map, and every finite product of generating maps and their inverses with independently varying parameters, is smooth into \(H\). Its topology need not be the subspace topology.

**Proof.** A **word map** is a finite product of the \(c\)'s and their inverses, on the product of their domains; include the constant empty word \(e\). Its domain is connected and its image contains \(e\). For completeness, a connected open subset of Euclidean space is polygonally path connected: the points reachable from a fixed point by finitely many line segments in the set form an open set, because a small ball about a reachable point can be appended; its complement is open by the same ball argument. Connectedness makes the complement empty. Coordinatewise concatenation then connects any two points of a finite product of these domains. The union of all word images is exactly \(H\).

Let \(r\) be the largest differential rank attained by any word map at any point. It exists because these ranks are integers between zero and \(\dim G\). Products, inverses, fixed values of words, and smooth substitutions into their parameters produce maps whose rank is at most \(r\): each is a word map composed with a smooth parameter map, and the chain rule bounds its rank. We call these substituted maps *word expressions*.

Choose a word attaining rank \(r\). Fix all but \(r\) suitable coordinate directions at that point, and multiply its values by the inverse of its value at the point. By the constant-rank and inverse theorems, Local tools 1.2–1.4, restriction to a sufficiently small ball gives a smooth embedding
\[
q:B\longrightarrow G,\qquad q(0)=e,\qquad \dim B=r,
\tag{C.1}
\]
which is a word expression. Here is the precise local use of those theorems: an invertible \(r\)-minor gives local coordinates in which the selected \(r\) variables are the first \(r\) target coordinates; the remaining target coordinates are smooth functions of those variables. Thus the map is a graph over an open ball and is an embedding. For \(r=0\), \(B\) is a point. A rank-zero word is locally constant, by the coordinate mean-value theorem in Local tools 0.3; it is constant on its connected domain and equals \(e\). Thus \(H=\{e\}\) in that case. The following argument includes the positive-dimensional case.

We first prove a local absorption fact. Suppose \(f:D\to G\) is a word expression, \(f(t_0)=g\), and \(Q:V\to G\) is any rank-\(r\) embedded word expression with \(Q(v_0)=g\). Consider
\[
P(v,t)=Q(v)g^{-1}f(t).
\tag{C.2}
\]
Its rank is at most \(r\), and its \(v\)-derivative at \((v_0,t_0)\) has rank \(r\). The same minor remains nonzero nearby, so its rank there is exactly \(r\). The constant-rank theorem gives an embedded \(r\)-dimensional local image \(N\), containing both nearby \(Q(v)\) and nearby \(f(t)\). The \(Q\)-slice has invertible differential into \(N\), hence covers an open neighbourhood of \(g\) in \(N\). Shrinking the two parameter neighbourhoods makes \(f(t)\) lie in that slice. Consequently
\[
t\longmapsto Q^{-1}(f(t))
\tag{C.3}
\]
is defined and smooth near \(t_0\). This assertion concerns the indicated local embedded image; it does not say that every ambiently nearby point of \(H\) lies in that image.

Use all right translates \(q(B)h\), \(h\in H\), as chart images on the set \(H\). They cover it because \(e\in q(B)\). If two charts meet at a point, apply (C.3) with one chart as \(Q\) and the other as \(f\). Their overlap is open near that point in each parameter ball, and the coordinate changes are smooth. Declaring sets open when their intersections with every chart pull back to open sets therefore makes each chart a homeomorphism onto an open set, with exactly these smooth changes of coordinates. Inclusion into \(G\) is continuous and smooth, since it is the smooth chart map in each chart. Two distinct points of \(H\) are separated by preimages of disjoint ambient open sets in \(G\); thus this topology is Hausdorff.

Every word expression is smooth into this atlas: at a value \(g\), use \(Q(v)=q(v)g\) in (C.3). In particular every word map is continuous into \(H\). Its image is connected and contains \(e\). The union of these images is connected: in a separation of their union, the member containing \(e\) must contain each entire connected image. This proves connectedness of \(H\).

In chart coordinates, multiplication has the form
\[
(u,v)\longmapsto q(u)h\,q(v)k,
\]
and inversion has the form \(u\mapsto(q(u)h)^{-1}\). Both are word expressions. Formula (C.3) shows that each is smooth in a chart about its value. The atlas thus gives smooth group operations. Its inclusion has injective differential in every chart because \(q\), and hence each translate, is an embedding.

It remains to prove second countability; it does not follow just from the ambient second countability. Choose a closed Euclidean ball \(\overline B_\rho\subset B\) about zero and put \(K=q(\overline B_\rho)\). It is compact in the constructed topology, as the continuous image of a compact Euclidean set, and contains an open identity neighbourhood. Choose a symmetric open identity neighbourhood \(V\subset K\), for example the intersection of a smaller open chart ball and its inverse. The union \(\bigcup_{n\ge1}V^n\) is a subgroup: symmetry gives inverses, and multiplication combines the numbers of factors. It is open because every translate of \(V\) is open; all its cosets are open, so its complement is open. Connectedness gives
\[
H=\bigcup_{n\ge1}V^n\subset\bigcup_{n\ge1}K^n\subset H.
\tag{C.4}
\]
Each \(K^n\) is compact: it is the continuous image under multiplication of \((\overline B_\rho)^n\), a closed bounded Euclidean set, using Local tools 0.1. Finitely many charts cover each \(K^n\). Their countable union is a countable atlas covering \(H\). Each Euclidean chart has a countable basis of rational-centred rational-radius balls contained in its domain. These form a basis because between any two distinct real numbers there is a rational number, as follows by choosing an integer denominator larger than the reciprocal of their separation and then an intervening integer numerator. A countable union of these chart bases is a countable basis for \(H\), by the countable-pair enumeration in Local tools 2.3. All claimed manifold and Lie-group properties are now proved. □

**Lemma C.2 (transport parameters with only \(C^1\) time regularity).** The global path-lifting, reversal, concatenation and equivariance results of Conn C.1–C.2 hold for finitely piecewise \(C^1\) paths. Their endpoint transport depends smoothly on a parameter \(z\) when, on a fixed finite subdivision and in local coordinates, \(\gamma_z(t)\) and \(\partial_t\gamma_z(t)\) have derivatives of every order in \(z\), all jointly continuous in \((z,t)\). No second time derivative is required.

**Proof.** In a section chart the horizontal equation is still
\[
g'=-dR_g\,A_{\gamma_z(t)}(\partial_t\gamma_z(t)).
\tag{C.5}
\]
For fixed \(z\), its Lie algebra coefficient is continuous on each closed time piece. Local tools 2.2 solves it over that piece, for every initial group value. The finite trivializing subdivision constructed in Conn C.1 works for continuous paths and therefore works here. Solving successively gives a unique whole lift, \(C^1\) on each piece. Equivariance, reversal and concatenation follow by applying the chain rule on each \(C^1\) piece and uniqueness, exactly to the curves \(p(t)a\), \(p(a+b-t)\), and the concatenated lifts, respectively. A piecewise \(C^1\) nondecreasing reparametrization with finitely many pieces likewise preserves the endpoint transport: \(p\circ\tau\) is horizontal wherever differentiated, and is constant on intervals on which \(\tau\) is constant. In particular a path followed by its reverse has identity transport.

We give the parameter step explicitly. In a local group chart write (C.5) as \(x'=F(t,x,z)\). The stated hypotheses and the smooth coefficients of the connection imply that every derivative \(D_{x,z}^jF\) is jointly continuous, including \(j=0\). Restrict \((t,x,z)\) to a compact product inside this chart. The coefficient \(F\), its first spatial derivative and each higher \(x,z\)-derivative have finite uniform bounds there by Local tools 0.1. On a sufficiently short interval \(I=[t_0,t_0+\epsilon]\), the integral operator
\[
T(u,a,z)(t)=a+\int_{t_0}^t F(s,u(s),z)\,ds
\tag{C.6}
\]
takes a closed supremum-norm ball of curves into its interior and contracts its curve variable with factor \(\epsilon L<1\), where \(L\) bounds \(D_xF\). Initial values \(a\) range over a smaller open ball, so the same bounds apply.

This operator is smooth in \(u,a,z\). Its derivatives are the integrals of the corresponding \(x,z\)-derivatives of \(F\) applied pointwise to increments; differentiation in \(a\) gives the constant curve. To justify every order, apply the segment formula of Local tools 0.3 in \((x,z)\). Uniform continuity of the next derivative on a slightly larger compact product bounds each difference remainder in supremum norm by
\[
\epsilon\,\omega(\|\Delta u\|_\infty+|\Delta z|)
                (\|\Delta u\|_\infty+|\Delta z|),
\qquad \omega(\delta)\longrightarrow0.
\tag{C.7}
\]
The same estimate applied to the preceding derivative proves its continuity in operator norm. Induction proves all the asserted operator derivatives. This argument never differentiates \(F\) in \(t\).

Local tools 2.A now makes the fixed point smooth in \((a,z)\) as a continuous-curve-valued function. Endpoint evaluation is bounded linear, hence preserves this smoothness. The integral equation also makes its time derivative \(F(t,x(t),z)\), and the same uniform estimates allow parameter differentiation of this formula, yielding the required jointly continuous mixed parameter derivatives.

For a whole compact time piece, the reference solution has compact graph. Cover it by finitely many local rectangles where this argument applies, subdivide the time interval into finitely many corresponding steps, and compose their smooth endpoint maps. At each step shrink the parameter neighbourhood to keep its endpoint in the next rectangle; there are only finitely many such restrictions. The trivializing subdivision itself persists in a common parameter neighbourhood by compactness of each closed segment, as proved in Conn C.2. Coordinate changes and the finite compositions preserve smoothness. This proves the stated parameter result without increasing the required time regularity. □

For a base point \(x\), a **small lasso** is a loop obtained by traversing a finitely piecewise \(C^1\) stem \(\alpha:x\to y\), a loop \(\ell\) based at \(y\) lying in one convex coordinate neighbourhood, and the reverse stem. The neighbourhood may also be required to trivialize the principal bundle. Convex refers to its coordinate image.

**Lemma C.3 (finite lasso factorization without a smooth homotopy assumption).** A finitely piecewise \(C^1\), continuously nullhomotopic based loop is, up to reparametrization and insertion or deletion of a path followed by its reverse, a finite product of small lassos and their inverses. Each lasso has a smooth one-parameter family of holonomy values in \(G\) that contains its value and starts at the identity; every loop in this family is continuously nullhomotopic and finitely piecewise \(C^1\).

**Proof.** Write the loop as \(c:[0,1]\to M\), based at \(x\). By the definition of based nullhomotopy there is a continuous
\[
F:[0,1]^2\to M,\quad
F(t,0)=c(t),\quad F(t,1)=F(0,s)=F(1,s)=x.
\tag{C.8}
\]
Cover its image by convex coordinate neighbourhoods contained in bundle trivializing neighbourhoods; these exist by taking a sufficiently small coordinate ball about each point.

We justify a finite fine grid whose closed cells map into single such neighbourhoods. Pull the cover back to the square. About each point choose a relative Euclidean ball of radius \(2\epsilon\) contained in one pulled-back set. Finitely many balls of radii \(\epsilon\) cover the square by Local tools 0.1. Choose \(\delta>0\) smaller than their finitely many radii. Every subset of the square of diameter less than \(\delta\) lies in one of the larger balls: choose a point in it and a smaller ball containing that point, then use the triangle inequality. Subdivide both coordinate intervals finely enough that every closed grid cell has diameter less than \(\delta\). Insert also the finite subdivision points at which \(c\) may have corners. Each closed cell now has a chosen convex trivializing neighbourhood containing its entire image.

At a vertex retain its value under \(F\). On the outer boundary retain the exact given path \(c\) and the three constant paths. For an interior grid edge, its continuous image lies in the intersection of the chosen neighbourhoods of the two adjacent cells. Replace that edge by a finitely piecewise smooth path in this open intersection with the same endpoints. To see that such a replacement exists, cover the original compact edge image by convex coordinate balls lying in the intersection, subdivide the edge by the same finite-cover argument, and on each subdivision join its endpoint values by a coordinate line segment in the chosen ball. Consecutive segments meet at the retained values. Use the same replacement, with reversed orientation, for the adjacent cell. Thus every cell boundary is a finitely piecewise \(C^1\) loop contained in its chosen convex neighbourhood, and the outside boundary is still exactly the original loop, with constant pieces.

Here is the required finite word identity. Add the grid cells row by row, starting at the bottom left, and within each row from left to right. Each new cell meets the previous union along one edge or two consecutive edges; its attachment is a connected boundary arc. There are no holes in these successive unions: after complete rows the union is a rectangle, and within a row it is that rectangle together with a left-hand row segment. Suppose an attachment replaces an old boundary arc \(u\) by a new arc \(v\), both from a vertex \(a\) to a vertex \(b\). Starting at the fixed bottom-left corner, write the old and new boundary words as
\[
B_{\rm old}=A\,u\,R,\qquad B_{\rm new}=A\,v\,R.
\]
Cancellation of reverse pairs gives the literal path-word identity
\[
B_{\rm new}=(A\,v\,u^{-1}A^{-1})\,B_{\rm old}.
\tag{C.9}
\]
The first factor is a lasso: its stem is the old boundary path \(A\), and \(v\,u^{-1}\) is a cell boundary or its inverse. For the initial cell its boundary is itself a small lasso with constant stem. Induction over all cells expresses the final outer boundary as finitely many such factors. Orient the initial outside traversal along the bottom edge from left to right; its other sides are constant, so it is \(c\) up to reparametrization and constant intervals. Equation (C.9) establishes the claimed cancellation relation, not just equality of homotopy classes. This distinction permits its use for connections with nonzero curvature.

For the parameter assertion take one lasso with stem \(\alpha\), inner base point \(y\), and coordinate loop \(u(t)\) in a convex open ball \(B\), with \(u(0)=u(1)=b\), the coordinate of \(y\). Set
\[
u_s(t)=b+s(u(t)-b).
\tag{C.10}
\]
For \(0\le s\le1\) this stays in \(B\). Its full image over this parameter interval is a compact subset of \(B\). It therefore stays in \(B\) for \(s\) in an open interval containing \([0,1]\): the image has positive distance from the closed complement, as follows by taking finitely many smaller balls inside \(B\), and \(|u_s-u_{s'}|\le |s-s'|\max_t|u(t)-b|\). If the maximum is zero the assertion is immediate. In each fixed \(C^1\) time piece, \(u_s\) and its time derivative satisfy all hypotheses of C.2. The fixed stem and reverse stem add no parameter dependence. Their holonomy is consequently a smooth \(G\)-valued function of \(s\). At \(s=0\) the inner loop is constant and the two stem transports cancel, giving \(e\). At \(s=1\) it is the prescribed lasso. Every inner loop is contractible by its coordinate straight-line contraction; conjugating that contraction by the stem gives a based nullhomotopy of the lasso. The inverse lasso has the inverse smooth holonomy family. □

**Lemma C.4 (countability of the fundamental group).** A connected, second-countable smooth manifold has countable fundamental group. Every continuous based loop is homotopic, with base point fixed, to a finitely piecewise smooth based loop.

**Proof.** First, the points reachable from a fixed point by finitely piecewise smooth paths form an open subset of the manifold: append short coordinate line segments in a ball. Its complement is open by the same argument. Connectedness makes this reachable set the whole manifold. The same argument applies to each connected component of any open subset; those components are open and are path connected.

There is a countable cover \(\{U_i\}\) by convex coordinate balls. Indeed start with all such balls and use the countable-subcover argument of Local tools 3.A: for each element of a countable basis contained in some covering ball, select one such ball; these selections cover every point. Every \(U_i\cap U_j\) has at most countably many connected components. Its components are disjoint open sets, and each contains a basis element; assign to a component the least index of a contained basis element. Distinct components have distinct assigned indices.

Choose a centre \(b_i\in U_i\). For each component \(W\) of each nonempty \(U_i\cap U_j\), choose a point \(q_{ijW}\in W\) and the two coordinate line-segment paths from \(b_i\) to \(q_{ijW}\) in \(U_i\) and from \(q_{ijW}\) to \(b_j\) in \(U_j\). For each \(i\) with \(x\in U_i\), choose also the coordinate path from the base point \(x\) to \(b_i\). There are countably many chosen paths and bridges, because pairs and countable unions are countable by Local tools 2.3.

Given a continuous based loop, the compact-interval subdivision argument of Conn C.1 puts each of finitely many consecutive segments inside some \(U_{i_k}\). In each such convex coordinate set a path is homotopic relative to its endpoints to the straight segment joining them: interpolate its coordinate values linearly with the coordinate values of that segment. The interpolation remains in the convex set and fixes both endpoints. These finitely many homotopies glue at the unchanged junctions. This already gives a finitely piecewise smooth representative.

Let \(y_k\in U_{i_k}\cap U_{i_{k+1}}\) be a junction, and let \(W_k\) be its intersection component. Join \(y_k\) to \(q_{i_k i_{k+1}W_k}\) by a finitely piecewise smooth path in \(W_k\), using the first paragraph. Insert this path followed by its reverse at the junction. Such insertion is a homotopy relative to the junction: for a path \(\beta:[0,1]\to M\) starting there, its outward-and-return traversal contracts through
\[
t\longmapsto
\begin{cases}
\beta(2t(1-s)),&0\le t\le\tfrac12,\\
\beta(2(1-t)(1-s)),&\tfrac12\le t\le1,
\end{cases}
\qquad 0\le s\le1.
\tag{C.11}
\]
The two branches agree at \(t=1/2\), so this is a continuous contraction fixing the endpoints.

After these insertions, the part between successive chosen junction points lies in one \(U_i\). Replace it, by the convex interpolation just proved, with the path from the first point to \(b_i\) and then to the second point. The initial and terminal parts are similarly replaced using \(x\) and the corresponding centres. The loop is therefore homotopic to a loop determined entirely by a finite string of chart indices and intersection-component indices, using the already chosen bridges and base-point paths. There are countably many finite strings over a countable alphabet: for each length repeatedly use the enumeration of pairs, then take the countable union over lengths. This gives a countable family of representatives of all homotopy classes.

The fundamental group here uses concatenation modulo these endpoint-fixed homotopies. Associativity and the constant-path identity follow by linearly interpolating the nondecreasing time subdivisions of a finite concatenation; reversal gives the inverse by (C.11). Thus the representatives counted above do give the elements of that group. No triangulation, CW-complex or Morse-theoretic assertion is used. □

**Theorem C.5 (full and restricted holonomy).** Fix a principal connection on \(P\to M\), a connected base \(M\), \(x\in M\) and \(p\in P_x\). For each finitely piecewise \(C^1\) based loop \(c\), define \(g_p(c)\in G\) by
\[
T_c(p)=p\,g_p(c).
\tag{C.12}
\]
The full holonomy group \(H\) consists of all such values. The restricted holonomy group \(H^0\) consists of those from continuously nullhomotopic based loops. Then \(H^0\) is a connected immersed Lie subgroup of \(G\), normal in \(H\). The full group has a second-countable immersed Lie-group structure with identity component \(H^0\), and \(H/H^0\) is countable. For \(a\in G\),
\[
H_{pa}=a^{-1}H_pa,\qquad H^0_{pa}=a^{-1}H^0_pa.
\tag{C.13}
\]
If \(q=T_\alpha(p)\) along a path from \(x\) to \(y\), then \(H_q=H_p\) and \(H_q^0=H_p^0\), as subgroups of \(G\).

**Proof.** Existence and uniqueness of (C.12) follow from the free transitive action on a principal fibre, PB A.2. If \(c*d\) means first traverse \(c\), then \(d\), equivariance in C.2 gives
\[
g_p(c*d)=g_p(d)\,g_p(c),\qquad
g_p(c^{-1})=g_p(c)^{-1}.
\tag{C.14}
\]
Indeed \(T_d(T_c(p))=T_d(p\,g_p(c))=p\,g_p(d)g_p(c)\). The constant loop gives the identity. This proves that \(H\) is a subgroup and fixes the order convention explicitly.

Nullhomotopic loops remain nullhomotopic after concatenation or reversal, by concatenating or reversing their based contractions. A conjugate loop \(c*\ell*c^{-1}\) is nullhomotopic when \(\ell\) is: first contract \(\ell\) inside that expression, then contract \(c*c^{-1}\) by (C.11). Its holonomy is \(g_p(c)^{-1}g_p(\ell)g_p(c)\). Consequently \(H^0\) is a normal subgroup of \(H\).

Apply C.1 to the family of **all** smooth maps from connected Euclidean open sets into \(G\) whose images lie in \(H^0\) and contain \(e\). Their generated subgroup is contained in \(H^0\). Conversely C.3 expresses the transport of every nullhomotopic finitely piecewise \(C^1\) loop as a finite product of values of smooth lasso-holonomy curves starting at \(e\). Each such curve belongs to this family, by C.2–C.3. Reversal of the order in (C.14) does not affect generated-subgroup membership. Thus the generated subgroup is exactly \(H^0\), and C.1 supplies its connected second-countable immersed Lie-group structure.

To count the quotient, first take any continuous based loop and choose a finitely piecewise smooth representative by C.4. Associate the coset
\[
[g_p(c)^{-1}]\in H/H^0.
\tag{C.15}
\]
This is independent of the representative. If \(c,d\) are based homotopic, \(c*d^{-1}\) is nullhomotopic: combine the homotopy from \(c\) to \(d\) with the fixed return path, then contract \(d*d^{-1}\). Equation (C.14) gives \(g_p(d)^{-1}g_p(c)\in H^0\). Normality therefore gives equality of the two cosets in (C.15). The inverse in (C.15) reverses the order in (C.14), so the assignment is a homomorphism from \(\pi_1(M,x)\). It is onto: every holonomy loop is continuous and has the same coset as any smooth representative of its homotopy class. Lemma C.4 makes its image countable.

For clarity we construct the full group's topology and smooth structure instead of inferring them from its being a subgroup. Make the countably many left cosets \(aH^0\) disjoint open copies of \(H^0\), with charts obtained by left translation. Different representatives of the same coset give compatible charts, because translation in \(H^0\) is smooth. The resulting space is Hausdorff, and is second countable by taking the union of the countably many countable bases.

Conjugation by each \(a\in H\) acts smoothly on \(H^0\). In fact it carries every member of the generating family used above to another member: it fixes \(e\), is smooth into \(G\), and stays in \(H^0\) by normality. The charts in C.1 are finite word expressions in these generators and fixed values. Conjugating such an expression gives another finite word expression in the conjugated generators, smooth into \(H^0\) by C.1. This proves smoothness in every chart; conjugation by \(a^{-1}\) is its smooth inverse.

On two cosets, multiplication has the formula
\[
(a u)(b v)=ab\,(b^{-1}u b)\,v,\qquad u,v\in H^0,
\tag{C.16}
\]
and inversion has the formula
\[
(a u)^{-1}=a^{-1}(a u^{-1}a^{-1}).
\tag{C.17}
\]
The just-proved conjugation property and the group operations of \(H^0\) make both formulas smooth into the corresponding coset. Inclusion into \(G\) is a translate of the immersed inclusion of \(H^0\) on every chart and is therefore a smooth injective immersion. The open subgroup \(H^0\) is also closed, because the other cosets are open. It is connected, while any connected set containing \(e\) must stay in this open-and-closed coset. Hence it is exactly the identity component.

Finally, equivariance gives
\(T_c(pa)=T_c(p)a=p\,g_p(c)a=pa(a^{-1}g_p(c)a)\),
which proves (C.13). If \(q=T_\alpha(p)\), a loop \(d\) based at \(y\) gives the loop \(\alpha*d*\alpha^{-1}\) based at \(x\). Equivariance and reverse transport give
\[
T_{\alpha^{-1}}T_dT_\alpha(p)
 =T_{\alpha^{-1}}(q\,g_q(d))
 =p\,g_q(d).
\]
Thus \(g_q(d)\in H_p\); reversing the role of the path proves the converse inclusion. Conjugation by a fixed path preserves nullhomotopy by the same insertion, contraction and cancellation argument used above, so the restricted groups agree too. □

In particular, a simply connected base has connected full holonomy: every continuous based loop is nullhomotopic, so \(H=H^0\) in C.5. This conclusion concerns the constructed Lie-group topology; it makes no closedness assertion about the image in \(G\).

The free construction reference is Peter W. Michor, [*Topics in Differential Geometry*, freely accessible author draft](https://www.mat.univie.ac.at/~michor/dgbook.pdf), Section 5.6 and Section 19.7, especially claims (1)–(4). The present proofs supply the subgroup atlas, second countability, the finite lasso identity for a continuous contraction, and the time-regularity argument internally. The source's later holonomy-algebra, reduction and flat-covering assertions are not assumed here.

Original exposition: GPT-6 Astra (OpenAI), October 2026, CC0 1.0. The human construction source is credited above; no source prose or page image is reproduced.

## D. Worked holonomy examples and solved exercises

The complete earlier proofs used here are Conn E.1–E.3 for the circle exponential and the Hopf potential and transport, Local tools 6.3–6.4 for circle charts and irrational density, and DG-CHAR-17 V.1, V.4–V.5 for Levi-Civita uniqueness, tautological curvature integration and the round-sphere metric and orientation. We retain the right-action sign convention (C.12)–(C.14).

**Lemma D.0 (angles and winding, including continuous homotopies).** Every continuous path in \(U(1)\) has a unique continuous real angle lift after its initial angle is fixed. The lift is finitely piecewise \(C^1\) when the path is. For a based loop, the final minus initial angle is \(2\pi n\), with \(n\in\mathbb Z\). This integer is invariant under continuous based homotopies, and it is zero exactly for nullhomotopic loops. Local angle differentials agree to give a global smooth one-form \(d\theta\) on the circle.

**Proof.** Conn E.1 proves that \(t\mapsto e^{it}\) covers \(U(1)\), has kernel \(2\pi\mathbb Z\), and satisfies \(\frac{d}{dt}e^{it}=ie^{it}\). Its derivative is nonzero. In the one-dimensional circle charts proved there, Local tools 1.2 supplies smooth inverse angle branches on sufficiently small arcs. Two such branches differ by a multiple of \(2\pi\); that difference is locally constant because it is continuous and integer-valued after division by \(2\pi\). Its derivative is therefore zero, proving the assertion about \(d\theta\).

Subdivide a path into finitely many closed segments whose images lie in such arcs, by the compact-interval argument of Conn C.1. Use an inverse branch on each segment and add an integer multiple of \(2\pi\) to agree with the preceding endpoint. At the first endpoint the prescribed initial angle chooses the unique multiple. This gives a continuous lift, with the same \(C^1\) regularity on each original piece, after inserting finitely many subdivision points. Two lifts differ continuously by a multiple of \(2\pi\); their equal initial values and connectedness of the interval make them equal. If the path closes, the kernel calculation gives its endpoint difference \(2\pi n\).

For homotopy invariance, let \(c_s(t)\) be a continuous based homotopy and fix a parameter \(s_0\). Choose the preceding finite subdivision and angle arcs for \(c_{s_0}\). Each closed segment remains inside its chosen arc for all \(s\) sufficiently near \(s_0\): continuity gives product neighbourhoods at each time, and compactness gives a finite subcover and a common parameter neighbourhood, exactly as in Conn C.2. The inverse-branch values vary continuously in \((s,t)\). At a junction the two branch values differ by \(2\pi\) times an integer, continuously in \(s\), so that integer is constant on a sufficiently small connected parameter interval. The same finite sequence of branch adjustments therefore gives lifts continuous in \((s,t)\), with their fixed common initial angle. Their endpoint difference is continuously \(2\pi n(s)\), so \(n(s)\) is locally constant. A locally constant integer on the connected interval of homotopy parameters is constant: the preimage of each value and its complement are open. A constant loop has integer zero, so nullhomotopic loops do too.

Conversely, if the angle lift \(u(t)\) has \(u(1)=u(0)\), then
\[
(s,t)\longmapsto
 \exp\!\bigl(i(u(0)+(1-s)(u(t)-u(0)))\bigr)
\tag{D.1}
\]
contracts the loop while fixing its base point. This proves the converse without a covering-space theorem. The loop \(t\mapsto e^{i(u(0)+2\pi nt)}\) realizes each integer \(n\). Concatenated lifts show that winding numbers add; reversing a lift negates its endpoint difference. □

**Example D.1 (Hopf curvature, its integral and full holonomy).** For the Hopf connection of Conn E.3, put \(w=x+iy\) and \(h=1+x^2+y^2\). Its unit-section potential and curvature are
\[
 A=\frac{i(x\,dy-y\,dx)}{h},
 \qquad
 F=\frac{2i}{h^2}\,dx\wedge dy.
\tag{D.2}
\]
Under the outward-oriented unit-sphere model of the projective line, \(F=(i/2)\,d\mathrm{area}\), and \(\int F=2\pi i\). Both holonomy groups are \(U(1)\).

**Proof.** Substituting \(w=x+iy\) into
\(A=(\bar w\,dw-w\,d\bar w)/(2h)\), proved in Conn E.3, gives the first formula. Since \(U(1)\) is abelian, A.4 makes \(F=dA\). Write \(\eta=x\,dy-y\,dx\). Then \(d\eta=2\,dx\wedge dy\) and
\[
dh\wedge\eta
=(2x\,dx+2y\,dy)\wedge(x\,dy-y\,dx)
=2(x^2+y^2)\,dx\wedge dy.
\]
The quotient rule gives
\(d(i\eta/h)=2i(h-(x^2+y^2))h^{-2}dx\wedge dy\), proving (D.2).

DG-CHAR-17 V.5 proves that
\[
q(x,y)=h^{-1}(2x,2y,1-x^2-y^2)
\]
parametrizes the unit sphere minus its south pole, with outward-oriented area form \(4h^{-2}dx\wedge dy\). This proves the area comparison. The radial integral and the omitted-point estimate in DG-CHAR-17 V.4 give, for the disk of radius \(R\),
\[
\int_{x^2+y^2\le R^2} F
=2\pi i\left(1-\frac1{1+R^2}\right).
\tag{D.3}
\]
Explicitly the radial identity there replaces \(dx\,dy\) by \(\pi\,d(r^2)\) on radial integrands, leaving
\(2\pi i\int_0^{R^2}(1+s)^{-2}ds\).
The primitive is \(-(1+s)^{-1}\). The missing neighbourhood is a disk of radius \(1/R\) in the other projective coordinate; smoothness bounds its integral by a constant times its area, tending to zero. Thus (D.3) tends to \(2\pi i\) on the entire projective line.

For holonomy based over \(w=0\), take the radial segment to \(r>0\), the loop \(w=r e^{i\phi}\), \(0\le\phi\le2\pi\), and the reversed radial segment. Conn E.3 proves that radial transport has constant section coordinate and that the lasso factor is
\[
\exp\!\left(-\frac{2\pi i r^2}{1+r^2}\right).
\tag{D.4}
\]
All these lassos contract in the coordinate plane. As \(r\ge0\) varies, \(r^2/(1+r^2)\) takes every value in \([0,1)\): for \(0\le a<1\), take \(r=\sqrt{a/(1-a)}\), using Local tools 0.0. Conn E.1 proves that the exponential of an interval of this one-period length gives the whole circle. Hence the restricted holonomy already contains every element of \(U(1)\). The full group is a subgroup of \(U(1)\), so both equal it. Formula (C.13) and the path comparison in C.5 give the same conclusion at every point of the connected base. □

**Example D.2 (the round sphere's tangent connection).** On the unit sphere in \(\mathbb R^3\), orthogonal projection of the ordinary derivative onto the tangent plane is its Levi-Civita connection. Its full and restricted holonomy groups, in an oriented orthonormal frame, are \(\mathrm{SO}(2)\).

**Proof.** At a unit vector \(n\), the projection is \(P_n=I-nn^T\). It is smooth and sends each tangent vector to itself, because differentiating \(|n|^2=1\) identifies the tangent plane with \(n^\perp\). For tangent vector fields \(Y\), put \(\nabla_XY=P_n\,dY(X)\). The ordinary product rule gives function-linearity in \(X\) and the Leibniz rule in \(Y\). If \(Y,Z\) are tangent, self-adjointness of \(P_n\) gives
\[
X(Y\cdot Z)=(\nabla_XY)\cdot Z+Y\cdot(\nabla_XZ).
\]
This is metric compatibility. The difference
\(dY(X)-dX(Y)\) equals the tangent vector \([X,Y]\): in any local parametrization \(n(u)\), expand \(Y=\sum_jY^j\partial_j n\), \(X=\sum_iX^i\partial_i n\); the terms \(X^iY^j\partial_i\partial_jn-Y^iX^j\partial_i\partial_jn\) cancel by the mixed-partial identity of PB C.3. The remaining coefficients are those of the bracket. Projection fixes that bracket, so the torsion is zero. DG-CHAR-17 V.1 proves uniqueness of a metric-compatible torsion-free connection, identifying this one as Levi-Civita.

Use the spherical coordinates and oriented orthonormal frame
\[
\begin{aligned}
n&=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta),\\
e_\theta&=(\cos\theta\cos\phi,\cos\theta\sin\phi,-\sin\theta),\\
e_\phi&=(-\sin\phi,\cos\phi,0),\qquad 0<\theta<\pi.
\end{aligned}
\tag{D.5}
\]
Here sine and cosine are the imaginary and real parts of the circle exponential of Conn E.1; its derivative and unit length give their derivative and norm identities. Direct dot products give \(e_\theta\cdot e_\phi=0\), unit norms and \(e_\theta\times e_\phi=n\). Differentiating gives
\[
\partial_\theta e_\theta=-n,\quad
\partial_\theta e_\phi=0,\quad
\partial_\phi e_\theta=\cos\theta\,e_\phi,\quad
P_n\partial_\phi e_\phi=-\cos\theta\,e_\theta.
\tag{D.6}
\]
For the last equality, \(\partial_\phi e_\phi=(-\cos\phi,-\sin\phi,0)\) has dot products \(-\cos\theta,0\) with \(e_\theta,e_\phi\). Consequently the matrix potential, whose columns are the derivatives of the frame vectors, is
\[
 A=\cos\theta\,J\,d\phi,\qquad
 J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\tag{D.7}
\]
These skew matrices describe the principal connection on oriented orthonormal frames: a frame change \(a\in\mathrm{SO}(2)\) changes the coefficient matrix to \(a^{-1}Aa+a^{-1}da\), by differentiating the changed frame and applying the Leibniz rule. Conn A.3 therefore assembles the local forms into a principal connection. Its associated derivative is the projection derivative by Conn D.1.

Since \(d\phi\wedge d\phi=0\), its curvature is
\[
F=-\sin\theta\,J\,d\theta\wedge d\phi.
\tag{D.8}
\]
Thus \(F_{12}=+\sin\theta\,d\theta\wedge d\phi\), agreeing with the positive Gaussian-curvature sign in DG-CHAR-17 V.5. Along a latitude, the parallel-frame equation has the constant coefficient \(-\cos\theta\,J\). Its solution after one circuit is
\[
\exp(-2\pi\cos\theta\,J).
\tag{D.9}
\]
Indeed
\(\exp(tJ)=\left(\begin{smallmatrix}\cos t&-\sin t\\ \sin t&\cos t\end{smallmatrix}\right)\):
this matrix starts at the identity and differentiates to \(J\) times itself, so uniqueness in Local tools 2.1 proves the exponential formula. Every element of \(\mathrm{SO}(2)\) has this form: its first column is a unit pair \((a,b)\), its second is the unique perpendicular unit pair \((-b,a)\) giving determinant \(+1\), and Conn E.1 supplies its angle.

To put all these loops at the same base frame, fix the equator point with \(\phi=0\), travel along its meridian to the chosen latitude, make one circuit, and return. Formula (D.7) vanishes on the meridian, so this frame comparison introduces no extra rotation. Each such lasso lies in the sphere minus its south pole, which is the coordinate plane of DG-CHAR-17 V.5, and is nullhomotopic by straight coordinate contraction followed by stem cancellation. As \(0<\theta<\pi\), \(\cos\theta\) takes all values in \((-1,1)\), by the circle parametrization in Conn E.1. The rotations in (D.9) therefore exhaust \(\mathrm{SO}(2)\). They belong to restricted holonomy, while all transport preserves oriented orthonormal frames. Hence both groups are exactly \(\mathrm{SO}(2)\). □

**Example D.3 (flat tori have trivial tangent holonomy).** Let \(\Lambda\subset\mathbb R^n\) be the integer span of a real basis, and equip \(\mathbb R^n/\Lambda\) with the metric induced by the Euclidean metric. The descended ordinary derivative is its Levi-Civita connection, is flat, and has trivial full and restricted holonomy.

**Proof.** A linear isomorphism taking the standard basis to the lattice basis identifies this quotient smoothly with \((\mathbb R/\mathbb Z)^n\). The circle charts and their smooth translation transitions are proved in Local tools 6.3; their finite products give this assertion in any \(n\). Local lifts of the quotient map to \(\mathbb R^n\) differ by locally constant lattice translations. Their derivatives are the identity. Thus all constant vector fields on \(\mathbb R^n\) descend, and an ordinary fixed orthonormal basis descends to a global orthonormal frame. In this frame define
\(\nabla_X(\sum_j f^j e_j)=\sum_jX(f^j)e_j\).
Translation transitions make this definition independent of every local lift. The product rule proves metric compatibility, and the coordinate bracket formula of PB C.3 proves zero torsion. DG-CHAR-17 V.1 identifies it as Levi-Civita. The potential in the global frame is zero, so A.7 gives zero curvature and the parallel equation keeps all frame coefficients constant. Every loop therefore has identity transport. When \(n=0\), the quotient is a point and the empty frame gives the same conclusion. □

**Example D.4 (a flat connection with dense, nonclosed holonomy).** On the trivial \(U(1)\)-bundle over the circle, take
\[
A=i\alpha\,d\theta,\qquad \alpha\in\mathbb R.
\tag{D.10}
\]
Its curvature is zero, its restricted holonomy is trivial, and its full holonomy is
\[
\{\exp(-2\pi i\alpha n):n\in\mathbb Z\}.
\tag{D.11}
\]
If \(\alpha\) is irrational this is a countable proper dense subgroup of \(U(1)\); its holonomy Lie-group topology is discrete.

**Proof.** The global one-form is defined in D.0. In every angle chart it is the differential of the coordinate, so \(d(d\theta)=0\). The Lie algebra is abelian, and A.4 gives zero curvature. On a lifted path with real angle \(u(t)\), the scalar horizontal equation is
\(g'=-i\alpha u'(t)g\).
Conn E.1, or differentiation and uniqueness in C.2, gives
\[
g(1)=g(0)\exp(-i\alpha(u(1)-u(0))).
\]
Lemma D.0 makes the endpoint difference \(2\pi n\) for loops and proves that all integers occur. This proves (D.11). It also makes that difference zero for every nullhomotopic loop, proving the restricted assertion without using an external flatness theorem.

For irrational \(\alpha\), the pigeonhole approximation in Local tools 6.4 proves that \(\{[\alpha n]:n\in\mathbb Z\}\) is dense in \(\mathbb R/\mathbb Z\). Scaling by \(2\pi\) and using the exponential circle charts identifies that quotient with \(U(1)\), so (D.11) is dense. It is countable and \(U(1)\) is uncountable by the explicit diagonal argument in Local tools 6.4; hence it is proper and nonclosed. The topology constructed in C.5 makes each coset of the trivial \(H^0\) an open point, so it is discrete. There is no contradiction with ambient density. For rational \(\alpha\), choose a positive integer \(q\) with \(q\alpha\in\mathbb Z\); the displayed powers repeat after \(q\), hence form a finite group. Its order is the least such positive \(q\), directly from the exponential period in Conn E.1. □

**Exercise D.5 (circle transport in the plane).** On the product \(U(1)\)-bundle over \(\mathbb R^2\), take \(A=i(x\,dy-y\,dx)\). Compute curvature and transport around the positively oriented circle of radius \(r\) centred at the origin.

**Solution.** Scalar coefficients commute, so \(F=dA=2i\,dx\wedge dy\), because \(d(x\,dy)=dx\wedge dy\) and \(d(y\,dx)=dy\wedge dx=-dx\wedge dy\). Along \(x=r\cos\phi,y=r\sin\phi\), the circle derivative identities of Conn E.1 give \(x\,dy-y\,dx=r^2d\phi\). The horizontal equation is \(g'=-ir^2g\), so its endpoint factor is \(\exp(-2\pi i r^2)\). For \(r=0\) the path is constant and the same formula gives one. Reversing orientation gives the inverse factor, by C.2. □

**Exercise D.6 (why the matrix Bianchi identity contains the connection).** Verify the local Bianchi equation and give a connection for which \(dF\ne0\).

**Solution.** Matrix products of forms use the exterior product of entries and matrix multiplication in their displayed order. From \(F=dA+A\wedge A\), the exterior product rule gives
\[
dF=dA\wedge A-A\wedge dA,
\qquad
[A,F]=A\wedge F-F\wedge A
=A\wedge dA-dA\wedge A.
\tag{D.12}
\]
The two cubic terms cancel by associativity. Thus \(dF+[A,F]=0\), in agreement with A.6.

For an explicit nonzero \(dF\), work on \(\mathbb R^3\) with the trivial real rank-two bundle and
\[
A=xC\,dy+D\,dz,\qquad
C=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
D=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
\]
These are valid \(\mathfrak{gl}_2(\mathbb R)\)-valued coefficients and so define a connection by Conn A.3 and D.1. Direct expansion gives
\[
F=C\,dx\wedge dy+x[C,D]\,dy\wedge dz,\qquad
dF=[C,D]\,dx\wedge dy\wedge dz.
\tag{D.13}
\]
Here \([C,D]=\operatorname{diag}(1,-1)\ne0\). In the bracket term only the product between \(D\,dz\) and \(C\,dx\wedge dy\) survives: all other terms repeat \(dy\) or \(dz\). It gives
\([D,C]\,dx\wedge dy\wedge dz=-dF\).
Hence \(dF\) need not vanish even though the full Bianchi equation always does. □

**Exercise D.7 (a flat line connection on the two-torus).** On the trivial \(U(1)\)-bundle over
\((\mathbb R/2\pi\mathbb Z)^2\), take
\(A=i\alpha\,d\theta+i\beta\,d\psi\).
Determine curvature and both holonomy groups.

**Solution.** The two angle differentials are globally defined by D.0 on the factors and pulled back to the product. Each is closed and the Lie algebra is abelian, so \(F=0\). Lift the two components of any path to angles \(u(t),v(t)\). The scalar horizontal equation gives endpoint factor
\[
\exp\!\left(-i\alpha(u(1)-u(0))-i\beta(v(1)-v(0))\right).
\]
For a loop, D.0 makes the differences \(2\pi m,2\pi n\). Every integer pair occurs, by traversing \(m\) turns in the first factor and \(n\) in the second. Thus
\[
H=\{\exp(-2\pi i(\alpha m+\beta n)):(m,n)\in\mathbb Z^2\}.
\tag{D.14}
\]
A nullhomotopic loop has both winding numbers zero because composing its contraction with either projection contracts that component. Conversely, if both are zero, the pair of contractions (D.1) is a based contraction in the torus. In particular \(H^0=\{1\}\). Formula (D.14) is finite if both parameters are rational, because a common denominator makes both generators roots of unity. If at least one is irrational, that generator alone is dense by D.4; the entire group is countable and hence still proper. Its Lie-group topology is discrete by C.5 in all cases. □

**Exercise D.8 (connected holonomy can fail to be closed).** Prove that full holonomy over a simply connected base is connected, and exhibit a connection over such a base whose holonomy is nonclosed.

**Solution.** Simply connected here means connected with every continuous based loop nullhomotopic. Thus the two defining sets in C.5 coincide: \(H=H^0\), which that theorem proves connected in its Lie-group topology.

For the nonclosed example let the base be \(\mathbb R^2\), let \(G=U(1)\times U(1)\), and choose an irrational real number \(\alpha\). On the trivial principal bundle use
\[
A=(i,i\alpha)\,x\,dy.
\tag{D.15}
\]
It is a smooth Lie algebra valued potential, so Conn A.3 gives a principal connection. Its curvature is
\((i,i\alpha)\,dx\wedge dy\).
For every finitely piecewise \(C^1\) loop \(c\), the two scalar horizontal equations yield
\[
g(c)=\left(e^{-i I(c)},e^{-i\alpha I(c)}\right),
\qquad I(c)=\int_c x\,dy.
\tag{D.16}
\]
The integral is the sum of ordinary integrals over its finitely many pieces, justified by Local tools 0.3. It requires no Stokes theorem. The rectangular loop
\((0,0)\to(1,0)\to(1,h)\to(0,h)\to(0,0)\)
has \(I(c)=h\), for every real \(h\), by the four side calculations of Conn F.2. Consequently the holonomy is exactly
\[
H=\{(e^{it},e^{i\alpha t}):t\in\mathbb R\}.
\tag{D.17}
\]
Every plane loop contracts through straight lines to its base point, so all these holonomies are restricted holonomies too. Local tools 6.4 proves, after the scaling \(t=2\pi s\), that (D.17) is a proper dense subgroup of the two-torus and that its parametrization has trivial kernel. With its parameter-line topology it is a connected immersed subgroup.

We also identify this topology with the holonomy structure of C.5. Take any smooth map from a Euclidean open set into \(G\) whose image lies in (D.17), and restrict near a parameter point to a small connected ball on which both circle coordinates have smooth angle branches \(u,v\). Membership in (D.17) implies
\[
v-\alpha u\in\{2\pi(n-\alpha m):m,n\in\mathbb Z\}.
\]
This is a countable set. A continuous real function on a connected ball with countable image must be constant: if it took two distinct values, its values along a line-segment path between the two points would include the whole intervening interval by Local tools 0.0; that interval is uncountable by the scaled diagonal argument of Local tools 6.4. Hence \(dv=\alpha\,du\), so every such map has rank at most one. The rectangles supply a smooth curve with nonzero derivative, making the maximal rank in C.1 exactly one. At the identity, choose the angle branches with \(u=v=0\); the same argument makes its local chart a segment with \(v=\alpha u\). The parametrization in (D.17) is thus a local diffeomorphism onto an identity neighbourhood for the C.5 structure. Its translates are local diffeomorphisms everywhere, and its injectivity and surjectivity make the local inverse maps a global smooth inverse. The two topologies agree. This is the required connected, nonclosed holonomy group. □

These computations use the exact earlier programme proofs cited at their points of use. Their free human construction sources and source terms remain in those lessons, including Peter W. Michor's [freely accessible author draft](https://www.mat.univie.ac.at/~michor/dgbook.pdf). No paid work supplies these calculations.

Original exposition: GPT-6 Astra (OpenAI), October 2026, CC0 1.0.

## E. Graded derivations and the curvature of a general projection

Let \(N\) be a smooth manifold. Put \(\Omega^j(N)=0\) for \(j<0\) and \(j>\dim N\). A real-linear map \(D:\Omega^*(N)\to\Omega^*(N)\) is a **graded derivation of degree \(r\)** if it increases degree by \(r\) and
\[
D(\alpha\wedge\beta)
=D\alpha\wedge\beta+(-1)^{rp}\alpha\wedge D\beta,
\qquad \alpha\in\Omega^p(N).
\tag{E.1}
\]
No continuity of \(D\) is assumed. Ordinary exterior differentiation and all scalar exterior-algebra rules are proved in DG-CHAR-17 D.0–D.1; insertion by a vector field and the ordinary Cartan identities are proved in A.2.

**Lemma E.1 (locality and insertion by a tangent-valued form).** Every graded derivation is local: its value at a point depends only on the germ of its input there. If \(K\in\Omega^k(N;TN)\), there is a unique graded derivation \(i_K\) of degree \(k-1\) which vanishes on functions and sends a one-form \(\alpha\) to \(\alpha\circ K\). In local coordinates,
\[
K=\sum_j K^j\otimes\partial_j
\quad\Longrightarrow\quad
i_K=\sum_j K^j\wedge i_{\partial_j}.
\tag{E.2}
\]
For a \(p\)-form \(\alpha\), \(p\ge1\), its evaluation is
\[
(i_K\alpha)(v_1,\ldots,v_{k+p-1})
=\sum_{\sigma\in\mathrm{Sh}(k,p-1)}
 \operatorname{sgn}(\sigma)\,
 \alpha\bigl(K(v_{\sigma(1)},\ldots,v_{\sigma(k)}),
             v_{\sigma(k+1)},\ldots,v_{\sigma(k+p-1)}\bigr).
\tag{E.3}
\]
For \(k=0\), the first block is empty and \(K\) is a vector field. For \(p=0\), insertion is zero.

**Proof.** First \(D1=D(1\cdot1)=2D1\), so \(D1=0\) and real-linearity makes \(D\) vanish on constant functions. Suppose a form \(\alpha\) vanishes on an open neighbourhood of \(x\). Choose a smooth cutoff \(\chi\) equal to one near \(x\) and supported in that neighbourhood, by Local tools 3.1. Then \(\chi\alpha=0\) everywhere and
\[
0=D(\chi\alpha)=D\chi\wedge\alpha+\chi D\alpha.
\]
At \(x\), the first term vanishes and the second is \(D\alpha(x)\). Thus \(D\alpha(x)=0\). Subtracting two inputs proves locality. It also defines \(D\) on local forms: extend a local form near a point by multiplying it by a supported cutoff and extending by zero, then apply \(D\). Different extensions agree near the point and so give the same value. In a smaller neighbourhood the same extension can be used, proving smoothness of the locally defined output. The local derivation rule follows from the global rule and locality.

In (E.2), \(i_{\partial_j}\) is a derivation of degree \(-1\), by A.2. Multiplication by the \(k\)-form \(K^j\) makes its degree \(k-1\). Its product-rule sign is correct: moving \(K^j\) past a \(p\)-form contributes \((-1)^{kp}\), which combines with the ordinary insertion sign \((-1)^p\) to give \((-1)^{(k-1)p}\). Thus (E.2) is a derivation, vanishes on functions, and sends \(\alpha\) to \(\sum_jK^j\alpha(\partial_j)=\alpha\circ K\).

A derivation vanishing on functions is \(C^\infty\)-linear. Its values on one-forms therefore determine its values on all forms: locally write every form as a finite sum of smooth coefficients times exterior products of coordinate differentials, and use the derivation rule. Two expressions (E.2) in different coordinates agree on functions and one-forms by the intrinsic formula \(\alpha\circ K\), hence agree on all forms. This proves existence, uniqueness and coordinate independence.

For (E.3), evaluate \(K^j\wedge i_{\partial_j}\alpha\) by the scalar shuffle formula in DG-CHAR-17 D.0, or A.1's scalar expansion. For each shuffle the sum over \(j\) inserts
\(\sum_jK^j(v_{\sigma(1)},\ldots,v_{\sigma(k)})\partial_j\)
into the first slot of \(\alpha\), exactly \(K\) on those arguments. This gives (E.3), including \(k=0\). Equivalently the full permutation sum is divided by \(k!(p-1)!\), since permutations within either block repeat the same term that many times. □

**Lemma E.2 (derivations that vanish on functions).** If \(D\) has degree \(r\) and vanishes on functions, then there is a unique \(L\in\Omega^{r+1}(N;TN)\) with \(D=i_L\). For \(r<-1\), this says \(D=0\).

**Proof.** Function-linearity gives, in local coordinates,
\[
D\left(\sum_j a_j\,dx^j\right)=\sum_j a_j\,D(dx^j).
\]
Put \(L=\sum_jD(dx^j)\otimes\partial_j\) in this chart. Its coefficients are smooth \((r+1)\)-forms. This formula gives \(D\alpha=\alpha\circ L\) for every one-form. A different chart gives the same \(L\), because covectors separate tangent vectors: taking coordinate differentials determines every component of its value on each tuple. Thus \(L\) is a global tangent-valued form. The uniqueness in E.1 gives \(D=i_L\) on all forms. If \(r+1<0\), \(D(dx^j)=0\) by the degree convention, so \(L=0\) and the same local expansion gives \(D=0\). □

**Lemma E.3 (the graded commutator).** For derivations \(D,E\) of degrees \(a,b\), respectively,
\[
[D,E]=DE-(-1)^{ab}ED
\tag{E.4}
\]
is a derivation of degree \(a+b\). It is graded antisymmetric and satisfies
\[
[D,[E,F]]=[[D,E],F]+(-1)^{ab}[E,[D,F]]
\tag{E.5}
\]
when \(F\) has degree \(c\).

**Proof.** Apply \(DE\) and \(ED\) to a product with first factor of degree \(p\). In \(DE(\alpha\beta)\), the two mixed terms have coefficients
\((-1)^{a(p+b)}\) on \(E\alpha\,D\beta\) and
\((-1)^{bp}\) on \(D\alpha\,E\beta\).
After multiplying \(ED(\alpha\beta)\) by \((-1)^{ab}\), its corresponding coefficients are
\((-1)^{ab+ap}\) and \((-1)^{ab+b(p+a)}\).
They agree with the first pair, respectively, and cancel in the difference. The terms with both operators on one factor remain:
\
[D,E
=[D,E]\alpha\,\beta+(-1)^{(a+b)p}\alpha\,[D,E]\beta.
\]
This proves the derivation assertion. Swapping \(D,E\) in (E.4) proves graded antisymmetry.

For Jacobi, the left side of (E.5) expands to
\[
DEF-(-1)^{bc}DFE-(-1)^{a(b+c)}EFD
  +(-1)^{a(b+c)+bc}FED.
\tag{E.6}
\]
Expanding the two terms on the right gives these same four terms and two cancelling pairs. The \(EDF\) pair has coefficients \(-(-1)^{ab}\) and \(+(-1)^{ab}\). The \(FDE\) pair has coefficients \(-(-1)^{(a+b)c}\) and \(+(-1)^{ab+b(a+c)+ac}\), equal in magnitude because the latter exponent differs by \(2ab\). The remaining coefficients of \(DFE,EFD,FED\) reduce to those in (E.6), modulo even integers. Associativity of operator composition therefore proves (E.5). □

Define the **Lie derivation** of \(K\in\Omega^k(N;TN)\) by
\[
\mathcal L_K=[i_K,d]
=i_Kd+(-1)^k d i_K.
\tag{E.7}
\]
It has degree \(k\). For a vector field this agrees with A.2's ordinary Lie derivative.

**Theorem E.4 (complete decomposition of every graded derivation).** For every derivation \(D\) of degree \(r\), there are unique
\[
K\in\Omega^r(N;TN),\qquad L\in\Omega^{r+1}(N;TN)
\]
such that
\[
D=\mathcal L_K+i_L.
\tag{E.8}
\]
Negative form degrees mean zero. Moreover
\[
[\mathcal L_K,d]=0,\qquad
[D,d]=\mathcal L_L,
\tag{E.9}
\]
so \(D\) commutes with \(d\) in the graded sense exactly when \(L=0\). It vanishes on functions exactly when \(K=0\).

**Proof.** We first determine the restriction of \(D\) to functions. For \(r<0\) that restriction is zero. Suppose \(r\ge0\). In a small convex coordinate ball about \(x\), the fundamental theorem in Local tools 0.3 gives
\[
f(y)-f(x)
=\sum_j(y^j-x^j)a_j(y),\qquad
a_j(y)=\int_0^1\partial_j f(x+t(y-x))\,dt.
\tag{E.10}
\]
Each \(a_j\) is smooth. To justify all derivatives, differentiate the smooth integrand in \(y\) on a smaller closed coordinate ball; each derivative is uniformly continuous and bounded on its product with \([0,1]\). The segment remainder and the integral estimate in Local tools 0.3 justify differentiation under the integral, successively for every order. Also \(a_j(x)=\partial_jf(x)\).

Use locality from E.1 to apply \(D\) to this identity, and then evaluate at \(x\). The terms with the factor \(y^j-x^j\) vanish, leaving
\[
(Df)_x=\sum_j(\partial_j f)(x)\,(Dx^j)_x.
\tag{E.11}
\]
Thus \(K=\sum_jDx^j\otimes\partial_j\) has \(Df=df\circ K\). The right side determines \(K\) independently of coordinates, since local coordinate differentials separate vectors; equivalently apply (E.11) to the new coordinate functions to obtain their tensor transformation rule. Its local coefficients are smooth forms, so it is a smooth global tangent-valued form. For \(r<0\), set \(K=0\).

By (E.7), \(\mathcal L_K f=i_Kdf=df\circ K\) on functions. Hence \(D-\mathcal L_K\) vanishes on functions and E.2 makes it uniquely \(i_L\). This proves existence. If \(\mathcal L_K+i_L=0\), apply it to functions to get \(df\circ K=0\) for every local \(f\), and therefore \(K=0\). E.1 then gives \(L=0\), proving uniqueness and also injectivity of \(K\mapsto\mathcal L_K\).

Expanding (E.7) and using \(d^2=0\), the coefficient of \(d i_Kd\) in
\(\mathcal L_Kd-(-1)^k d\mathcal L_K\)
is \((-1)^k-(-1)^k=0\); the other terms contain \(d^2\). Thus the first identity in (E.9) holds. Applying it to (E.8) gives
\([D,d]=[i_L,d]=\mathcal L_L\).
Injectivity gives its vanishing criterion, and (E.11) gives the function-vanishing criterion. In particular derivations of degree below \(-1\) vanish, while those of degree \(-1\) are ordinary insertions by vector fields. □

**Theorem E.5 (the two brackets and their different gradings).** For \(K\) of tangent-form degree \(k\) and \(L\) of degree \(\ell\), define the insertion bracket by
\[
[K,L]_{\mathrm{ins}}
=i_KL-(-1)^{(k-1)(\ell-1)}i_LK.
\tag{E.12}
\]
Insertion on a tangent-valued form acts on its form component, as in (E.2). This bracket has form degree \(k+\ell-1\) and is a graded Lie bracket when degree \(k\) is assigned shifted degree \(k-1\). The Frölicher–Nijenhuis bracket is uniquely defined by
\[
[\mathcal L_K,\mathcal L_L]
=\mathcal L_{[K,L]_{\mathrm{FN}}}.
\tag{E.13}
\]
It has form degree \(k+\ell\) and is a graded Lie bracket for the unshifted degrees. It agrees with the ordinary vector-field bracket in degree zero. If \(I=\operatorname{Id}_{TN}\), then
\[
i_I\alpha=p\alpha\quad(\alpha\in\Omega^p),\qquad
\mathcal L_I=d,\qquad [I,K]_{\mathrm{FN}}=0.
\tag{E.14}
\]
The mixed identity, with both degrees as stated above, is
\[
[i_K,\mathcal L_L]
=\mathcal L_{i_KL}+(-1)^\ell i_{[K,L]_{\mathrm{FN}}}.
\tag{E.15}
\]

**Proof.** The componentwise insertion on a tangent-valued form is intrinsic: a change of tangent frame multiplies its form coefficients by smooth functions, and \(i_K\) is \(C^\infty\)-linear, so the change matrices and inverse matrices cancel. By E.3, \([i_K,i_L]\) is a derivation, and it vanishes on functions. In coordinates its value on \(dx^j\) is
\(i_KL^j-(-1)^{(k-1)(\ell-1)}i_LK^j\).
E.2 therefore gives
\[
[i_K,i_L]=i_{[K,L]_{\mathrm{ins}}}.
\tag{E.16}
\]
Injectivity of insertion and the antisymmetry and Jacobi identities in E.3 transfer to (E.12), with the indicated shifted degrees.

Equations (E.9) and (E.5) show that
\([[\mathcal L_K,\mathcal L_L],d]=0\).
The unique decomposition E.4 makes this commutator a pure Lie derivation, which defines (E.13). Its degree is \(k+\ell\). Injectivity of \(\mathcal L\) transfers graded antisymmetry and Jacobi from E.3. For vector fields \(X,Y\), evaluation on functions gives
\[
\mathcal L_{[X,Y]_{\mathrm{FN}}}f
=X(Yf)-Y(Xf)=[X,Y]f,
\]
so covector separation identifies the two vector fields.

Insertion by \(I\) replaces each of the \(p\) one-form factors in a local decomposable \(p\)-form by itself. Since its degree is zero, every term has positive sign, giving \(i_I\alpha=p\alpha\). Thus
\(\mathcal L_I\alpha=i_Id\alpha-di_I\alpha=(p+1)d\alpha-pd\alpha=d\alpha\).
Equations (E.9) and (E.13), with injectivity, make \(I\) central for the FN bracket.

For the sign in (E.15), put \(Q=[i_K,\mathcal L_L]\). On functions,
\[
Qf=i_K(df\circ L)=df\circ(i_KL)
=\mathcal L_{i_KL}f.
\]
The middle equality follows by expanding \(L=\sum_jL^j\otimes\partial_j\) and using function-linearity of \(i_K\). Hence \(Q-\mathcal L_{i_KL}=i_S\) for a uniquely determined \(S\). Jacobi and (E.9) give
\[
[Q,d]
=-(-1)^{(k-1)\ell}[\mathcal L_L,\mathcal L_K]
=(-1)^\ell\mathcal L_{[K,L]_{\mathrm{FN}}}.
\]
The left side is \(\mathcal L_S\), so injectivity gives
\(S=(-1)^\ell[K,L]_{\mathrm{FN}}\), proving (E.15). This derivation fixes its sign by operator identities rather than by a degree mnemonic.

Two useful explicit consequences follow. For scalar forms \(\alpha,\beta\) of degrees \(k,\ell\), and vector fields \(X,Y\),
\[
\begin{aligned}
{}[\alpha\otimes X,\beta\otimes Y]_{\mathrm{FN}}
={}&\alpha\wedge\beta\otimes[X,Y]
+\alpha\wedge\mathcal L_X\beta\otimes Y
-\mathcal L_Y\alpha\wedge\beta\otimes X\\
&+(-1)^k\bigl(
 d\alpha\wedge i_X\beta\otimes Y
 +i_Y\alpha\wedge d\beta\otimes X\bigr).
\end{aligned}
\tag{E.17}
\]
Indeed (E.7) expands to
\(\mathcal L_{\alpha X}=\alpha\wedge\mathcal L_X+(-1)^k d\alpha\wedge i_X\).
Apply the commutator of this expression and its \(\beta,Y\) counterpart to a function \(f\). The two second derivatives combine as
\(\alpha\wedge\beta(XY-YX)f\).
The remaining \(Yf\) coefficient is
\(\alpha\wedge\mathcal L_X\beta+(-1)^kd\alpha\wedge i_X\beta\).
The \(Xf\) coefficient is
\(-\mathcal L_Y\alpha\wedge\beta+(-1)^ki_Y\alpha\wedge d\beta\):
moving \(d\beta\), of degree \(\ell+1\), past \(i_Y\alpha\), of degree \(k-1\), gives that last sign. These are precisely the coefficients of (E.17); injectivity by evaluation on functions proves the formula.

More generally, if \(D_j=\mathcal L_{K_j}+i_{L_j}\) has degree \(r_j\), so \(K_j\) has degree \(r_j\) and \(L_j\) degree \(r_j+1\), then
\[
\begin{aligned}
{}[D_1,D_2]
={}&\mathcal L_{[K_1,K_2]_{\mathrm{FN}}
                  +i_{L_1}K_2-(-1)^{r_1r_2}i_{L_2}K_1}\\
&+i_{[L_1,L_2]_{\mathrm{ins}}
                  +[K_1,L_2]_{\mathrm{FN}}
                  -(-1)^{r_1r_2}[K_2,L_1]_{\mathrm{FN}}}.
\end{aligned}
\tag{E.18}
\]
Expand its four operator commutators. The pure Lie and pure insertion terms are (E.13) and (E.16). For the other two use (E.15) and graded antisymmetry; the conversion
\((-1)^{r_2}[L_1,K_2]_{\mathrm{FN}}
=-(-1)^{r_1r_2}[K_2,L_1]_{\mathrm{FN}}\)
gives the displayed sign. This proves the full decomposition of the commutator. □

**Theorem E.6 (curvature and cocurvature of a tangent projection).** Let \(P:TN\to TN\) be a smooth projection, \(P^2=P\), and put \(h=I-P\). Define two tangent-valued two-forms
\[
C(X,Y)=P[hX,hY],\qquad
\overline C(X,Y)=h[PX,PY].
\tag{E.19}
\]
These auxiliary forms use a positive bracket convention. The connection curvature used in B.3 will be \(R=-C\) when \(P\) is a bundle's vertical projection. For every such tangent projection,
\[
\frac12[P,P]_{\mathrm{FN}}=C+\overline C,\qquad
[P,C+\overline C]_{\mathrm{FN}}=0,
\tag{E.20}
\]
and
\[
[C,P]_{\mathrm{FN}}=i_C\overline C+i_{\overline C}C.
\tag{E.21}
\]
The first form is the obstruction to closure of the horizontal sections under brackets; the second is the corresponding obstruction for vertical sections.

**Proof.** Function-linearity of \(C\) follows from
\([f hX,hY]=f[hX,hY]-(hYf)hX\), since \(Ph=0\). The other slot follows by antisymmetry. The same proof with \(hP=0\) makes \(\overline C\) tensorial. Both are smooth alternating two-forms. Their values are vertical and horizontal, respectively; \(C\) vanishes if an argument is vertical and \(\overline C\) if an argument is horizontal. Their vanishing is consequently exactly the asserted bracket-closure condition.

For tangent endomorphisms \(K,L\), (E.13) implies the explicit formula
\[
\begin{aligned}
{}[K,L]_{\mathrm{FN}}(X,Y)
={}&[KX,LY]+[LX,KY]\\
&-L([KX,Y]+[X,KY])
 -K([LX,Y]+[X,LY])\\
&+(LK+KL)[X,Y].
\end{aligned}
\tag{E.22}
\]
Here is a direct derivation. From (E.7) and the exterior-evaluation formula A.2, for a one-form \(\beta\) one obtains
\[
(\mathcal L_K\beta)(X,Y)
=KX(\beta(Y))-KY(\beta(X))
-\beta([KX,Y]+[X,KY]-K[X,Y]).
\]
The terms \(X(\beta(KY))\) and \(Y(\beta(KX))\) cancel on expanding \(i_Kd\beta-d(i_K\beta)\). Set \(\beta=df\circ L=\mathcal L_Lf\), repeat with \(K,L\) interchanged, and add: the commutator of two degree-one operators is their sum. The paired second derivatives give the first two vector-field brackets in (E.22), and the remaining terms give its last two lines. Evaluation on all \(f\) proves (E.22).

Set \(K=L=P\) and use \(P^2=P\). Half its right side is
\[
[PX,PY]-P[PX,Y]-P[X,PY]+P[X,Y]
=h[PX,PY]+P[hX,hY],
\]
by expanding the second expression with \(h=I-P\). This is \(C+\overline C\). For the next identity let \(T=[P,P]_{\mathrm{FN}}\). The graded Jacobi identity with all three entries \(P\), of degree one, gives
\(2[P,[P,P]]=[[P,P],P]=-[P,[P,P]]\);
hence \([P,T]=0\) over the real numbers. This proves the second assertion of (E.20).

We supply the remaining insertion identity, including its coefficient. In the following computation all brackets of forms are FN brackets. Since \([P,T]=0\), (E.15) gives
\[
[i_T,\mathcal L_P]=\mathcal L_{i_TP}.
\]
Apply the operator Jacobi identity to \(i_T,\mathcal L_P,\mathcal L_P\). The first two operators have degree one, while their commutator has degree two, so it gives
\[
[i_T,[\mathcal L_P,\mathcal L_P]]
=2[[i_T,\mathcal L_P],\mathcal L_P].
\]
The left side is \([i_T,\mathcal L_T]=\mathcal L_{i_TT}\) by (E.15), because \([T,T]=0\) for the even degree \(2\). The right side is
\(2\mathcal L_{[i_TP,P]}\).
Injectivity of \(\mathcal L\) yields
\[
i_TT=2[i_TP,P].
\tag{E.23}
\]
Now \(T=2(C+\overline C)\) and \(i_TP=P\circ T=2C\). Furthermore \(i_CC=0\) and \(i_{\overline C}\overline C=0\): each inserted value is in the kind of tangent direction annihilated by that form. Substitution into (E.23) gives
\(4(i_C\overline C+i_{\overline C}C)=4[C,P]\),
proving (E.21). No involutivity assumption was used. □

**Theorem E.7 (naturality for arbitrary smooth maps).** Let \(f:N\to N'\) be smooth. Say that \(K\in\Omega^k(N;TN)\) and \(K'\in\Omega^k(N';TN')\) are \(f\)-related if
\[
Tf\bigl(K(v_1,\ldots,v_k)\bigr)
=K'(Tf(v_1),\ldots,Tf(v_k)).
\tag{E.24}
\]
Then \(i_Kf^*=f^*i_{K'}\) and
\(\mathcal L_Kf^*=f^*\mathcal L_{K'}\).
For two related pairs, their insertions, insertion brackets and FN brackets are related. These assertions require no injectivity, surjectivity or constant rank of \(Tf\).

**Proof.** In the shuffle formula (E.3), pullback sends every scalar-form argument through \(Tf\). Equation (E.24) moves \(Tf\) past the one inserted value, giving exactly
\(i_Kf^*\alpha=f^*i_{K'}\alpha\).
The same multilinear shuffle argument with a tangent-valued \(L\) in place of \(\alpha\), and with \(Tf\) applied also to the output, proves relatedness of \(i_KL,i_{K'}L'\). The insertion-bracket assertion follows by subtraction with its prescribed sign.

Pullback commutes with exterior differentiation by DG-CHAR-17 D.1. It therefore intertwines the commutators in (E.7), proving the Lie-derivation assertion. For two pairs it also intertwines their operator commutators and hence their FN Lie derivations by (E.13). Apply this last equality to a smooth function \(u\) on \(N'\). Since \(\mathcal L_Q u=du\circ Q\), it says that \(du\) annihilates the difference between the two sides of (E.24) for the prospective bracket. Local coordinate differentials at \(f(x)\) separate tangent vectors. If global functions are required, multiply those coordinate functions by a cutoff equal to one near \(f(x)\), using Local tools 3.1; their differentials there are unchanged. Thus the difference is zero, proving relatedness.

This argument also proves the converse tests: intertwining insertion on exact one-forms already implies (E.24), as does intertwining Lie derivations on functions. When \(f\) is a local diffeomorphism, (E.24) defines a pullback of tangent-valued forms using \((Tf)^{-1}\); all three bracket/insertion identities then become ordinary pullback identities. For a vector field \(X\), differentiating this pullback along its local flow gives
\(\mathcal L_X(\alpha\otimes Y)=\mathcal L_X\alpha\otimes Y+\alpha\otimes[X,Y]\),
by the product rule, A.2 and the tangent pushforward derivative. Formula (E.17) with first degree zero gives this same expression as \([X,\alpha\otimes Y]_{\mathrm{FN}}\). To spell out that derivative on \(Y\), in coordinates
\(D\varphi_t^{-1}(\varphi_t(x))Y(\varphi_t(x))\)
has derivative at zero
\(-DX(x)Y(x)+DY(x)X(x)=X,Y\);
the local flow equation and the inverse derivative formula in Local tools 0.4 justify both terms. Thus the usual tensor Lie derivative agrees with the FN bracket in this case too. □

**Theorem E.8 (Bianchi on an arbitrary smooth fibre bundle).** Let \(\pi:E\to M\) be a smooth fibre bundle with connection projection \(P:TE\to VE\) and horizontal projection \(h=I-P\). Define
\[
R(X,Y)=-P[hX,hY].
\tag{E.25}
\]
Then
\[
[P,P]_{\mathrm{FN}}=[h,h]_{\mathrm{FN}}=-2R,\qquad
[P,R]_{\mathrm{FN}}=[h,R]_{\mathrm{FN}}=0.
\tag{E.26}
\]
Writing \(d_h=\mathcal L_h\), the corresponding scalar-form identities are
\[
d_h^2=-\mathcal L_R,\qquad [d_h,\mathcal L_R]=0.
\tag{E.27}
\]
Every smooth base map induces a pullback connection, and its curvature is related to \(R\) by the induced map of total spaces.

**Proof.** In a bundle chart \((x^i,y^a)\), vertical vector fields have only \(\partial_{y^a}\) components. Their bracket, computed by PB C.3, has only such components too. Thus the vertical space is closed under brackets and \(\overline C=0\) in E.6, while \(C=-R\). Equations (E.20) give \([P,P]=-2R\) and \([P,R]=0\). Since \(I\) is FN-central by E.5, expansion of \(h=I-P\) gives \([h,h]=[P,P]\) and \([h,R]=-[P,R]=0\). The operator \(d_h\) has odd degree one, so \([d_h,d_h]=2d_h^2\). Apply (E.13) to get (E.27). This uses no linear or principal structure on the fibre.

For a coordinate form of the identity, write
\[
H_i=\partial_{x^i}-\Gamma_i^a\partial_{y^a},\qquad
R=\tfrac12R_{ij}^a\,dx^i\wedge dx^j\otimes\partial_{y^a},
\]
where repeated indices are summed. Formula B.3, or direct expansion of \(-[H_i,H_j]\), gives
\[
R_{ij}^a
=\partial_i\Gamma_j^a-\partial_j\Gamma_i^a
+\Gamma_j^b\partial_b\Gamma_i^a
-\Gamma_i^b\partial_b\Gamma_j^a.
\tag{E.28}
\]
Here \(\partial_b=\partial/\partial y^b\). For a vertical field \(V=V^a\partial_{y^a}\), its bracket with \(H_i\) is
\[
[H_i,V]
=\bigl(\partial_iV^a-\Gamma_i^b\partial_bV^a
                  +V^b\partial_b\Gamma_i^a\bigr)\partial_{y^a}.
\]
The vector-field Jacobi identity applied to \(H_i,H_j,H_k\), with
\([H_j,H_k]=-R_{jk}^a\partial_{y^a}\), therefore gives the full coefficient equation
\[
\sum_{\mathrm{cyc}(i,j,k)}
\bigl(\partial_iR_{jk}^a-\Gamma_i^b\partial_bR_{jk}^a
                 +R_{jk}^b\partial_b\Gamma_i^a\bigr)=0.
\tag{E.29}
\]
It includes the two vertical derivative terms; retaining only the base derivatives is generally incorrect.

Finally let \(f:M'\to M\) be any smooth map. The pullback total space
\(E'=\{(x',e):f(x')=\pi(e)\}\)
is a smooth bundle: local bundle coordinates identify it with \(f^{-1}(U)\times S\), whose transitions are those of \(E\) evaluated at \(f(x')\). A tangent vector is a pair \((v',w)\) with \(Tf(v')=T\pi(w)\), as follows directly by differentiating these product coordinates. Set
\[
P'(v',w)=(0,Pw).
\tag{E.30}
\]
The result is a tangent vector because \(T\pi(Pw)=0\); it is vertical for \(E'\to M'\), and it fixes all such vertical vectors. It is therefore a smooth connection projection. Its horizontal part is \((v',hw)\). For the map \(F:E'\to E\), \(F(x',e)=e\), one has \(TF\circ P'=P\circ TF\), so the projections are \(F\)-related. Apply E.7 and (E.26) to obtain relatedness of the two curvatures. In bundle coordinates this construction reads
\[
(\Gamma')_a^b(x',y)
=\sum_i(\partial_a f^i)(x')\Gamma_i^b(f(x'),y),
\]
and the curvature relation is the tensor pullback in the two base arguments. Thus the construction also covers maps whose derivative has nonconstant rank. □

**Exercise E.9 (distinguish the two gradings).** For a tangent-valued \(k\)-form \(K\), compute both orders of its insertion bracket with \(I\), and compare the FN bracket.

**Solution.** Insertion by \(I\) multiplies the \(k\)-form component of \(K\) by \(k\), whereas \(i_KI=I\circ K=K\). Since \(I\) has shifted degree zero, (E.12) gives
\[
[I,K]_{\mathrm{ins}}=(k-1)K,\qquad
[K,I]_{\mathrm{ins}}=(1-k)K.
\]
This includes \(k=0\), when \(i_IK=0\) and \(i_KI=K\). By (E.14), both orders of the FN bracket are zero. The two answers use different gradings and different operator definitions, so they are compatible. □

**Exercise E.10 (a nonlinear Bianchi calculation).** On \(\mathbb R^3\times\mathbb R\to\mathbb R^3\), use
\(\Gamma_1=y^2,\ \Gamma_2=x^1y,\ \Gamma_3=x^2y^2\).
Compute curvature and verify (E.29).

**Solution.** Formula (E.28) gives
\[
R_{12}=y+x^1y^2,\qquad
R_{23}=(1-x^1x^2)y^2,\qquad
R_{31}=0.
\tag{E.31}
\]
For example the two nonlinear terms in \(R_{12}\) are
\(x^1y(2y)-y^2x^1=x^1y^2\); those in \(R_{23}\) are
\(x^2y^2x^1-x^1y(2x^2y)=-x^1x^2y^2\).
Both the base terms and the nonlinear terms in \(R_{31}\) vanish.

Put
\(\delta_iV=\partial_iV-\Gamma_i\partial_yV+V\partial_y\Gamma_i\).
Then
\[
\begin{aligned}
\delta_1R_{23}
&=-x^2y^2-y^2\,2(1-x^1x^2)y
           +(1-x^1x^2)y^2\,2y=-x^2y^2,\\
\delta_2R_{31}&=0,\\
\delta_3R_{12}
&=-x^2y^2(1+2x^1y)+(y+x^1y^2)\,2x^2y=x^2y^2.
\end{aligned}
\tag{E.32}
\]
Their sum is zero, exactly (E.29). In contrast
\(\partial_1R_{23}+\partial_2R_{31}+\partial_3R_{12}=-x^2y^2\),
which is not identically zero. Thus even a one-dimensional nonlinear fibre requires the full vertical corrections. □

**Exercise E.11 (a projection with nonzero cocurvature).** On \(\mathbb R^4\), use horizontal fields
\(H_1=\partial_x,\ H_2=\partial_y+x\partial_z\)
and vertical fields
\(V_1=\partial_z,\ V_2=\partial_w+z\partial_x\).
Let \(P\) project onto the latter pair along the former. Compute \(C,\overline C\) and the right side of (E.21), and show why \([P,C]_{\mathrm{FN}}\) need not vanish.

**Solution.** The four fields form a basis everywhere. Their dual one-forms are
\[
\theta^1=dx-z\,dw,\quad\theta^2=dy,\quad
\eta^1=dz-x\,dy,\quad\eta^2=dw.
\]
Evaluation on the four fields gives respectively the four coordinate rows of the identity matrix, proving both the basis assertion and the duality. Thus
\(P=\eta^1\otimes V_1+\eta^2\otimes V_2\).
The brackets are
\([H_1,H_2]=V_1\) and \([V_1,V_2]=H_1\), by direct differentiation. Tensoriality in E.6 therefore gives
\[
C=\theta^1\wedge\theta^2\otimes V_1,\qquad
\overline C=\eta^1\wedge\eta^2\otimes H_1.
\]
Insertion has degree one in both cases, so
\[
i_C\overline C+i_{\overline C}C
=\theta^1\wedge\theta^2\wedge\eta^2\otimes H_1
 +\eta^1\wedge\eta^2\wedge\theta^2\otimes V_1.
\tag{E.33}
\]
Indeed \(i_C\eta^1=\theta^1\wedge\theta^2,\ i_C\eta^2=0\), and
\(i_{\overline C}\theta^1=\eta^1\wedge\eta^2,\ i_{\overline C}\theta^2=0\); the insertion product rule gives exactly (E.33). Its value on \((H_1,H_2,V_2)\) is \(H_1\ne0\). By (E.21) it equals \([C,P]_{\mathrm{FN}}\); graded antisymmetry gives
\([P,C]_{\mathrm{FN}}=-[C,P]_{\mathrm{FN}}\ne0\).
The vertical space is not bracket-closed, since \([V_1,V_2]=H_1\). It therefore does not have the special vertical integrability of a fibre bundle, and the unrestricted Bianchi formula correctly retains cocurvature. □

The free construction source is Peter W. Michor, [*Topics in Differential Geometry*, freely accessible author draft](https://www.mat.univie.ac.at/~michor/dgbook.pdf), Sections 16.1–16.7, 16.11–16.16. Every consumed identity and prerequisite is proved above or in an exact earlier programme proof. The positive auxiliary projection curvature \(C\) is distinguished from the negative-bracket connection curvature \(R\), and the mixed-commutator sign is derived explicitly from the operator definitions.

Original exposition: GPT-6 Astra (OpenAI), October 2026, CC0 1.0. The human construction source is credited above; no source prose or page image is reproduced.

## F. Intrinsic torsion and compatible tangent connections

A reduction of a frame bundle carries more information than a connection with values in some matrix algebra. The reduction fixes the tensors that transport must preserve; its intrinsic torsion measures whether any preserving connection can have zero torsion. We prove the global obstruction, compute it for metrics of every signature and for nondegenerate two-forms, and derive the algebraic curvature and derivative constraints.

Our conventions use frames \(u:V\to T_xM\), with right action \(u\cdot h=u\circ h\). All manifolds are smooth, Hausdorff and second countable; all vector spaces in this part are finite dimensional over \(\mathbb R\). An \(H\)-structure means a smooth principal \(H\)-subbundle \(B\) of the frame bundle, for an embedded matrix Lie group \(H\subset\mathrm{GL}(V)\). Its Lie algebra is \(\mathfrak h\subset\operatorname{End}(V)\).

The free comparison source is Robert L. Bryant, *Recent advances in the theory of holonomy*, [arXiv:math/9910059v2](https://arxiv.org/abs/math/9910059v2), Sections 1.2–1.4. The proofs below include the linear inverses, the global gluing and the coordinate calculations needed here. No onward reference in that paper is a proof provider. The earlier programme dependencies are Local tools 0.0, 0.2, 0.3, 1.3, 2.1 and 3.1; Principal bundles A.2 and C.1–C.3; Connections A.3–A.4, B.1, C.2 and D.1; DG-CHAR-17 D.1; and Parts A and C above.

**Lemma F.1 (metric and alternating-form reductions).** A smooth nondegenerate symmetric form of locally constant signature \((p,q)\) gives a smooth \(\mathrm O(p,q)\)-reduction. A smooth nondegenerate alternating two-form gives a smooth symplectic reduction. Their Lie algebras consist, respectively, of the endomorphisms satisfying
\[
 g(Av,w)+g(v,Aw)=0,\qquad
 \sigma(Av,w)+\sigma(v,Aw)=0.
 \tag{F.1}
\]

**Proof.** First establish the linear normal forms. For a nonzero-dimensional nondegenerate symmetric form there is a vector \(v\) with \(g(v,v)\ne0\): otherwise polarization gives \(g(v,w)=0\) for all \(v,w\). Normalize this vector to squared length \(1\) or \(-1\). Its orthogonal complement is nondegenerate, since a vector orthogonal to the complement and to \(v\) is orthogonal to the whole space. Projection onto the complement is
\[
 z\longmapsto z-\frac{g(z,v)}{g(v,v)}v.
 \tag{F.2}
\]
Induction gives a basis with diagonal entries \(1\) and \(-1\). The number of positive entries is intrinsic: a positive definite subspace has dimension at most the number of positive entries, because projection to those coordinates is injective on that subspace. The positive coordinate subspace attains this bound. The negative count follows in the same way.

For an alternating form, choose \(v\ne0\) and \(w\) with \(\sigma(v,w)=1\), using nondegeneracy and rescaling. The complement orthogonal to their span is nondegenerate, and the projection onto it is
\[
 z\longmapsto z-\sigma(z,w)v+\sigma(z,v)w.
 \tag{F.3}
\]
Both pairings of this expression with \(v,w\) vanish. Induction gives a symplectic basis; in particular the dimension is even.

These constructions work smoothly near any point of a manifold. Extend the finitely many selected vectors to local smooth fields. Every denominator chosen nonzero at the point stays nonzero on a smaller neighbourhood. The square roots of positive smooth functions used for metric normalization are smooth: the positive square-root function is the local inverse of \(t\mapsto t^2\) on \(t>0\), by Local tools 1.3, and exists by Local tools 0.0. Thus the induction gives local smooth adapted frames. In particular metric signature is locally constant.

For completeness the model groups are embedded Lie groups without an appeal to a closed-subgroup theorem. If \(Q\) is the fixed symmetric matrix, the derivative at the identity of
\(A\mapsto A^TQA\), with target the space of symmetric matrices, is
\[
 B\longmapsto B^TQ+QB.
\]
It is onto: a prescribed symmetric \(S\) is the image of \(B=\frac12Q^{-1}S\). The implicit-function theorem, Local tools 1.3, makes the level \(A^TQA=Q\) a submanifold near the identity. Multiplication by an element of the level transports this conclusion to every point. Matrix multiplication and inverse restrict smoothly, so this is an embedded matrix Lie group.

For a fixed nonsingular skew matrix \(J\), the same argument has target the skew matrices. If \(S^T=-S\), then \(B=\frac12J^{-1}S\) satisfies \(B^TJ+JB=S\). Thus the symplectic group is also an embedded matrix Lie group. Differentiating their defining equations gives exactly (F.1). The equations are closed conditions within \(\mathrm{GL}(V)\). Finally an adapted local frame identifies all adapted frames over that neighbourhood with \(U\times H\); a change of adapted frame is a smooth \(H\)-valued matrix. These are the required principal-bundle charts. The zero-dimensional cases have the single trivial frame and require no induction. \(\square\)

**Proposition F.2 (solder form, torsion and change of connection).** On an \(H\)-structure define the \(V\)-valued solder form
\[
 \theta_u(\xi)=u^{-1}T_u\pi(\xi).
 \tag{F.4}
\]
For a principal connection \(\omega\), the form
\[
 \tau=d\theta+\omega\wedge\theta
 \tag{F.5}
\]
is horizontal and \(H\)-equivariant. Under the associated identification
\(B\times_HV\simeq TM\), it is the torsion tensor
\[
 T(X,Y)=\nabla_XY-\nabla_YX-[X,Y].
 \tag{F.6}
\]
All compatible tangent connections form an affine space with difference bundle
\(T^*M\otimes\mathfrak h_M\), where
\(\mathfrak h_M=B\times_H\mathfrak h\subset\operatorname{End}(TM)\).
If \(\nabla'=\nabla+A\), then
\[
 T'=T+\delta A,\qquad
 (\delta A)(X,Y)=A_XY-A_YX.
 \tag{F.7}
\]

**Proof.** The map \([u,v]\mapsto uv\) is well defined because
\((u h)v=u(hv)\), and in a local frame it is a smooth fibrewise linear isomorphism. The solder form is horizontal and obeys
\(R_h^*\theta=h^{-1}\theta\), directly from (F.4). It corresponds to the identity \(TM\)-valued one-form on \(M\).

Part A.5 identifies its covariant exterior derivative with (F.5), and proves that this derivative is again horizontal and equivariant. To identify the tensor completely, choose a local section \(s:U\to B\). Write
\(X=sx\), \(Y=sy\), and \(a=s^*\omega\). Connections D.1 gives
\[
 s^{-1}\nabla_XY=X(y)+a(X)y.
\]
The exterior derivative formula gives
\[
 (s^*d\theta)(X,Y)=X(y)-Y(x)-s^{-1}[X,Y].
\]
Adding \(a(X)y-a(Y)x\) proves (F.6). This also proves directly that \(T\) is linear over smooth functions in both slots.

Connections A.4 proves that principal connection differences are precisely horizontal equivariant \(\mathfrak h\)-valued one-forms. In the associated tangent bundle these act as \(A_X\in\mathfrak h_M\). Conversely every such tensor gives that principal difference form, using the inverse frame and the established associated-bundle correspondence. No choice of frame changes the resulting connection. Subtracting (F.6) for the two connections gives (F.7). \(\square\)

Define the linear map and its kernel
\[
 \begin{split}
 \delta:V^*\otimes\mathfrak h&\longrightarrow
                  \Lambda^2V^*\otimes V,\\
 (\delta a)(v,w)&=a(v)w-a(w)v,\qquad
 \mathfrak h^{(1)}=\ker\delta.
 \end{split}
 \tag{F.8}
\]
The action on the domain is
\((h\cdot a)(v)=h\,a(h^{-1}v)h^{-1}\); substitution shows
\(\delta(h\cdot a)(v,w)=h(\delta a)(h^{-1}v,h^{-1}w)\).
Thus the kernel, image and cokernel are \(H\)-modules.

**Theorem F.3 (global intrinsic-torsion obstruction).** The class of the torsion of any compatible connection in
\[
 B\times_H\operatorname{coker}\delta
 \tag{F.9}
\]
is independent of that connection. It vanishes if and only if there is a global compatible torsion-free connection. When it vanishes, all such connections form an affine space modelled on
\(\Gamma(B\times_H\mathfrak h^{(1)})\).
Moreover, a compatible torsion-free connection given near a closed subset extends, after possibly shrinking that neighbourhood, to a global one whenever the intrinsic torsion vanishes globally.

**Proof.** A compatible connection exists by Connections B.1, applied to the given principal bundle. The rank of the bundle map \(\delta\) is constant: in every adapted frame its matrix is the same fixed linear map (F.8). A basis of its kernel and a complement, supplied by Local tools 0.2, give local smooth frames for the kernel and image. The equivariance just proved makes their transition functions and the quotient transition functions well defined. These are precisely the associated bundles in the statement.

Independence follows from (F.7). Necessity of vanishing follows by choosing a torsion-free connection. For sufficiency take an initial compatible connection \(\nabla^0\) with torsion \(T^0\). Vanishing means \(T^0\) is a smooth section of the image bundle. Choose any linear right inverse of \(\delta\) on its image in a model fibre, by restricting \(\delta\) to a linear complement of its kernel and inverting that restriction. In each adapted trivialization this gives a smooth local tensor \(A_i\) with
\(\delta A_i=-T^0\). This chosen right inverse need not be \(H\)-equivariant; only its local use is required.

Choose a subordinate locally finite smooth partition \((\chi_i)\), using the complete proof in Local tools 3.1. This prerequisite retains the human attribution and component terms of its integrated Brenner partition-of-unity material. Extend \(\chi_i A_i\) by zero off its chart, and put
\[
 A=\sum_i\chi_i A_i.
 \tag{F.10}
\]
Each extension is smooth because the support is contained in the chart, and the sum is smooth by local finiteness. Since \(\delta\) is a fibrewise linear map and \(\sum_i\chi_i=1\), one has \(\delta A=-T^0\). Thus \(\nabla^0+A\) is the required global connection. Two such connections differ by a section of \(\ker\delta\), and adding any such section preserves zero torsion; this proves the affine-space assertion.

For the relative assertion, let \(\nabla^U\) be given on \(U\supset K\), with \(K\) closed. Choose a global compatible torsion-free \(\nabla\) by the preceding construction. The difference \(A^U=\nabla^U-\nabla\) is a section of the kernel bundle on \(U\). Local tools 3.1 supplies a cutoff \(\chi\) supported in \(U\) and equal to one near \(K\). Extend \(\chi A^U\) by zero. Its values remain in the kernel, so
\(\nabla+\chi A^U\) is globally compatible and torsion-free, and agrees with \(\nabla^U\) near \(K\). \(\square\)

**Theorem F.4 (all metric signatures).** For a nondegenerate symmetric form \(g\), the map (F.8) for
\(\mathfrak h=\mathfrak{so}(V,g)\) is an isomorphism. Consequently every smooth nondegenerate metric has exactly one torsion-free metric-compatible connection.

**Proof.** Given \(a:V\to\mathfrak{so}(V,g)\), set
\(b(X,Y,Z)=g(a(X)Y,Z)\). Condition (F.1) says \(b\) is skew in its last two slots. If \(t(X,Y,Z)=g((\delta a)(X,Y),Z)\), then
\(t(X,Y,Z)=b(X,Y,Z)-b(Y,X,Z)\). Conversely, for any tensor \(t\) skew in its first two slots, set
\[
 b(X,Y,Z)=\frac12\bigl(
 t(X,Y,Z)-t(Y,Z,X)+t(Z,X,Y)\bigr).
 \tag{F.11}
\]
Interchanging \(Y,Z\) and using the skew symmetry of \(t\) negates the expression. Subtracting the expression with \(X,Y\) interchanged gives exactly \(t(X,Y,Z)\). Nondegeneracy of \(g\) therefore produces an \(a(X)Y\), uniquely for this \(b\), and its endomorphisms satisfy (F.1).

Uniqueness of \(b\) also follows directly: if \(\delta a=0\), then \(b\) is symmetric in its first two slots and skew in its last two; hence
\[
 b(X,Y,Z)=b(Y,X,Z)=-b(Y,Z,X)
          =-b(Z,Y,X)=b(Z,X,Y)=b(X,Z,Y)=-b(X,Y,Z).
\]
Thus \(b=0\), so \(a=0\). This proves bijectivity, with inverse (F.11). The formula uses only \(g\) and permutations of arguments, so it commutes with changes of adapted frame.

Lemma F.1 supplies the metric reduction and Theorem F.3 now supplies existence and uniqueness globally. Preservation of the metric follows in an adapted frame from (F.1), and conversely that condition characterizes metric-compatible coefficients.

One can recover the connection without frames:
\[
 \begin{aligned}
 2g(\nabla_XY,Z)={}&Xg(Y,Z)+Yg(Z,X)-Zg(X,Y)\\
 &+g([X,Y],Z)-g([Y,Z],X)+g([Z,X],Y).
 \end{aligned}
 \tag{F.12}
\]
To derive this, write metric compatibility for the three derivatives on the right, expand them into pairings with covariant derivatives, and replace
\(\nabla_YX\) by \(\nabla_XY-[X,Y]\), and similarly for the other two reversed pairs. Every unwanted covariant-derivative term cancels, leaving the left side and the displayed bracket terms. No positivity was used anywhere. \(\square\)

**Theorem F.5 (symplectic intrinsic torsion and all compatible choices).** For a nondegenerate alternating form \(\sigma\), let
\(\mathfrak h=\mathfrak{sp}(V,\sigma)\). There are natural identifications
\[
 \ker\delta\simeq\operatorname{Sym}^3 V^*,
 \qquad
 \operatorname{coker}\delta\simeq\Lambda^3 V^*.
 \tag{F.13}
\]
Under the second identification, the intrinsic torsion of a smooth nondegenerate two-form is \(d\sigma\). Thus a torsion-free connection preserving \(\sigma\) exists exactly when \(d\sigma=0\); when one exists, all of them form an affine space modelled on
\(\Gamma(\operatorname{Sym}^3T^*M)\).

**Proof.** Lower the output of \(a(X)Y\) by setting
\(c(X,Y,Z)=\sigma(a(X)Y,Z)\). Condition (F.1) is equivalent to
\(c(X,Y,Z)=c(X,Z,Y)\). For a \(V\)-valued alternating two-tensor \(T\), write
\(t(X,Y,Z)=\sigma(T(X,Y),Z)\) and define
\[
 \mathcal A_\sigma(T)(X,Y,Z)
      =t(X,Y,Z)+t(Y,Z,X)+t(Z,X,Y).
 \tag{F.14}
\]
This is an alternating three-form: interchange \(X,Y\) and use the skew symmetry of the first two slots of \(t\); the other interchanges follow cyclically. It is onto, since for any three-form \(\eta\) the prescription
\(\sigma(T(X,Y),Z)=\frac13\eta(X,Y,Z)\) defines a unique \(T\) and gives \(\mathcal A_\sigma(T)=\eta\).

If \(T=\delta a\), its lowered tensor is
\(t(X,Y,Z)=c(X,Y,Z)-c(Y,X,Z)\). The cyclic sum vanishes, because the last-two-slot symmetry of \(c\) cancels its six terms in pairs. Conversely, suppose \(\mathcal A_\sigma(T)=0\). Define
\[
 c(X,Y,Z)=\frac13\bigl(t(X,Y,Z)+t(X,Z,Y)\bigr).
 \tag{F.15}
\]
It is symmetric in \(Y,Z\), so defines an \(\mathfrak{sp}(V,\sigma)\)-valued \(a\). Its first-slot difference is
\[
 c(X,Y,Z)-c(Y,X,Z)
 =\frac13\bigl(2t(X,Y,Z)+t(X,Z,Y)-t(Y,Z,X)\bigr)
 =t(X,Y,Z);
\]
the last equality uses the vanishing cyclic sum and
\(t(Z,X,Y)=-t(X,Z,Y)\). Hence \(\delta a=T\). We have proved exactness of
\[
 V^*\otimes\mathfrak{sp}(V,\sigma)
 \ \xrightarrow{\ \delta\ }\ \Lambda^2V^*\otimes V
 \ \xrightarrow{\ \mathcal A_\sigma\ }\ \Lambda^3V^*
 \ \longrightarrow\ 0.
 \tag{F.16}
\]
For the first kernel, \(\delta a=0\) means \(c\) is also symmetric in \(X,Y\); the two adjacent transpositions imply full symmetry. Conversely every fully symmetric \(c\) has these properties and uniquely defines \(a\), by nondegeneracy. All constructions are invariant under \(\sigma\)-preserving changes of basis. This proves both natural identifications.

Take any compatible connection on the reduction of Lemma F.1. The exterior derivative formula, proved in DG-CHAR-17 D.1, is
\[
 d\sigma(X,Y,Z)=
 \sum_{\mathrm{cyc}}\bigl(X(\sigma(Y,Z))-\sigma([X,Y],Z)\bigr).
\]
Compatibility replaces each differentiated pairing by
\(\sigma(\nabla_XY,Z)+\sigma(Y,\nabla_XZ)\).
In the cyclic sum the second terms, using skew symmetry of \(\sigma\), combine with the first into
\(\sum_{\mathrm{cyc}}\sigma(\nabla_XY-\nabla_YX,Z)\).
Thus
\[
 d\sigma(X,Y,Z)=\sum_{\mathrm{cyc}}\sigma(T(X,Y),Z)
                         =\mathcal A_\sigma(T)(X,Y,Z).
 \tag{F.17}
\]
Theorem F.3 and (F.13) now prove the global assertions. In particular this is an existence proof on every smooth second-countable manifold, with no compactness assumption and no invocation of Darboux's theorem. \(\square\)

For a compatible tangent connection we use the curvature convention
\[
 R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z.
 \tag{F.18}
\]
It agrees with the matrix curvature \(da+a\wedge a\) of Part A.7.

**Theorem F.6 (curvature spaces and the derivative obstruction).** Define
\[
 \begin{split}
 K(\mathfrak h)
 &=\{r\in\Lambda^2V^*\otimes\mathfrak h:
                 r(X,Y)Z+r(Y,Z)X+r(Z,X)Y=0\},\\
 K^1(\mathfrak h)
 &=\{s\in V^*\otimes K(\mathfrak h):
                 s(X)(Y,Z)+s(Y)(Z,X)+s(Z)(X,Y)=0\}.
 \end{split}
 \tag{F.19}
\]
For every compatible torsion-free tangent connection, its curvature lies in the associated \(K(\mathfrak h)\)-bundle and its covariant derivative lies in the associated \(K^1(\mathfrak h)\)-bundle. In particular
\(K^1(\mathfrak h)=0\) implies \(\nabla R=0\). No irreducibility or completeness is required.

**Proof.** The representation on \(V\) identifies \(\nabla\) with the principal connection and \(R\) with its associated curvature, by A.7. Thus \(R\) is \(\mathfrak h_M\)-valued. For the solder form, A.6 gives
\(D^2\theta=\Omega\wedge\theta\). Since \(D\theta=\tau=0\), we obtain
\(\Omega\wedge\theta=0\). Evaluating the wedge on three vectors and passing to their base tangent vectors gives
\[
 R(X,Y)Z+R(Y,Z)X+R(Z,X)Y=0.
 \tag{F.20}
\]
The wedge has precisely these three terms, since \(\Omega\) is alternating in its two inputs.

Connections on duals and tensors are defined by differentiating pairings and products. Explicitly the derivative of curvature is
\[
 \begin{aligned}
 ((\nabla_XR)(Y,Z))W={}&\nabla_X(R(Y,Z)W)
       -R(\nabla_XY,Z)W\\
       &-R(Y,\nabla_XZ)W-R(Y,Z)\nabla_XW.
 \end{aligned}
 \tag{F.21}
\]
The connection rules show cancellation of derivatives of any scalar multiplying \(X,Y,Z,W\); this is a tensor. Applying (F.21) to (F.20), with its cyclic permutations, differentiates the zero tensor, so
\((\nabla_XR)\) satisfies the same algebraic first Bianchi identity. Also the adjoint connection preserves \(\mathfrak h_M\): in an adapted frame its derivative is \(X(r)+[a(X),r]\), which is still \(\mathfrak h\)-valued. Consequently \(\nabla R\) belongs to \(T^*M\otimes K(\mathfrak h)_M\).

The full second Bianchi identity in A.6 gives \(DR=0\). Its exterior evaluation on vector fields is
\[
 0=\sum_{\mathrm{cyc}}
       \bigl(\nabla_X^{\operatorname{End}}(R(Y,Z))-R([X,Y],Z)\bigr).
\]
Insert the definition (F.21) before applying the resulting endomorphism to an arbitrary \(W\). The terms that differentiate \(Y,Z\) collect as
\[
 \sum_{\mathrm{cyc}}
       R(\nabla_XY-\nabla_YX-[X,Y],Z)
       =\sum_{\mathrm{cyc}}R(T(X,Y),Z).
\]
It follows that, for an arbitrary compatible tangent connection,
\[
 \sum_{\mathrm{cyc}}(\nabla_XR)(Y,Z)
       +\sum_{\mathrm{cyc}}R(T(X,Y),Z)=0.
 \tag{F.22}
\]
With \(T=0\), the first sum vanishes and gives exactly the second defining equation of (F.19). Both linear equations in (F.19) commute with the \(H\)-action, by direct substitution, so their kernels form the asserted associated bundles. If the fibre \(K^1(\mathfrak h)\) is zero, the tensor \(\nabla R\) is zero at every point. \(\square\)

**Lemma F.7 (the algebraic curvature ideal).** The linear span
\[
 \mathfrak h_K=\operatorname{span}
    \{r(v,w):r\in K(\mathfrak h),\ v,w\in V\}
 \tag{F.23}
\]
is an ideal of \(\mathfrak h\), and
\(K(\mathfrak h_K)=K(\mathfrak h)\) as subspaces of
\(\Lambda^2V^*\otimes\mathfrak h\).

**Proof.** For \(A\in\mathfrak h\), the induced tensor action is
\[
 (A\cdot r)(v,w)=[A,r(v,w)]-r(Av,w)-r(v,Aw).
 \tag{F.24}
\]
Its cyclic Bianchi sum is zero. Indeed applying \(A\) to
\(\sum_{\mathrm{cyc}}r(v,w)z=0\), and subtracting the same Bianchi identity with each of \(v,w,z\) in turn replaced by its image under \(A\), gives precisely that cyclic sum. Thus \(A\cdot r\in K(\mathfrak h)\). Rearranging (F.24) writes
\([A,r(v,w)]\) as a sum of three values of tensors in \(K(\mathfrak h)\), which proves the ideal property by linearity. Every \(r\in K(\mathfrak h)\) takes values in \(\mathfrak h_K\) by the definition of the span, so it belongs to \(K(\mathfrak h_K)\); the reverse inclusion is immediate from the same Bianchi equation. \(\square\)

The assertion that an actual torsion-free **holonomy** algebra must equal its curvature ideal also needs a curvature-generation theorem. Lemma F.7 by itself makes no such holonomy claim. The complete generation proof and resulting criterion are supplied in Part G.3 and G.5. Part H supplies the complete binary-form calculations. Parts I and L construct actual analytic connections, and Parts J and M prove their complete local structure equations.

**Exercise F.8 (a nonvanishing obstruction).** On \(\mathbb R^4\) consider
\[
 \sigma=e^{x^1}(dx^1\wedge dx^2+dx^3\wedge dx^4).
 \tag{F.25}
\]
Determine whether a torsion-free connection can preserve \(\sigma\).

**Solution.** Its contraction with a vector having components
\((v^1,v^2,v^3,v^4)\) is
\(e^{x^1}(v^1dx^2-v^2dx^1+v^3dx^4-v^4dx^3)\), which is zero only for the zero vector. Thus the form is nondegenerate. The exterior product rule gives
\[
 d\sigma=e^{x^1}\,dx^1\wedge dx^3\wedge dx^4\ne0.
 \tag{F.26}
\]
By the complete obstruction calculation (F.17), no torsion-free compatible connection exists. Compatible connections do exist by F.1 and Connections B.1; their torsion must have this same nonzero image under \(\mathcal A_\sigma\). \(\square\)

**Exercise F.9 (many compatible connections, smaller holonomy).** On
\(\mathbb R^2\) take \(\sigma=dx\wedge dy\), the flat coordinate connection \(\nabla^0\), and the symmetric tensor \(c=y\,dx^{\otimes3}\). Define \(A\) by
\(\sigma(A_XY,Z)=c(X,Y,Z)\), and set \(\nabla=\nabla^0+A\).
Compute \(\nabla\), its curvature and its full holonomy.

**Solution.** Put \(e_1=\partial_x\), \(e_2=\partial_y\), and let \(N\) be the endomorphism \(Ne_1=e_2\), \(Ne_2=0\). Since \(\sigma(e_2,e_1)=-1\), the only nonzero coordinate coefficient is
\[
 A_{e_1}e_1=-y e_2,\qquad
 a=-yN\,dx,\qquad N^2=0.
 \tag{F.27}
\]
The symmetry of \(c\) proves torsion-freeness and compatibility by F.5; one may also check (F.1) and \(A_XY=A_YX\) directly. The coordinate curvature is
\[
 da+a\wedge a=N\,dx\wedge dy,\qquad R(e_1,e_2)=N,
 \tag{F.28}
\]
because \(d(-y\,dx)=dx\wedge dy\) and \(dx\wedge dx=0\).

For a piecewise \(C^1\) path \(\gamma(t)=(x(t),y(t))\), the parallel-transport equation of Connections D.1 is
\(v'=y(t)x'(t)Nv\). Its exact solution matrix is
\[
 P_\gamma=I+N\int_\gamma y\,dx.
 \tag{F.29}
\]
To verify it, differentiate using Local tools 0.3; the term involving \(N^2\) vanishes, and the initial value is \(I\). Uniqueness is the already proved transport uniqueness. Products of such matrices add their scalar coefficients, and their inverses negate them.

All based-loop transports therefore lie in \(\{I+tN:t\in\mathbb R\}\).
Conversely, traverse the rectangle with vertices
\((0,0),(1,0),(1,b),(0,b),(0,0)\). Direct integration along its four edges gives \(\int y\,dx=-b\). Varying \(b\) yields every real coefficient. Loops based elsewhere give the same conclusion by conjugating with transport along a joining path, since the matrices \(I+tN\) commute. Hence
\[
 \operatorname{Hol}(\nabla)=\operatorname{Hol}^0(\nabla)
       =\{I+tN:t\in\mathbb R\}.
 \tag{F.30}
\]
Every loop in \(\mathbb R^2\) contracts to its base point by straight interpolation, so full and restricted holonomy coincide, also as asserted in C.5. This group is a smooth embedded copy of the additive real line: its parameter is the lower-left matrix entry, and multiplication adds that entry. Its intrinsic holonomy Lie-group structure agrees with this one: in C.1 every generating map into these matrices has rank at most one, whereas the rectangle family has rank one. It is a proper subgroup of the symplectic group, since for example the matrix \(\operatorname{diag}(2,\frac12)\) preserves \(dx\wedge dy\) and is not \(I+tN\). Thus preserving a structure does not assert that the connection has its full structure group as holonomy. \(\square\)

**Theorem F.10 (the derivative criterion for actual holonomy).** Let \(\nabla\) be a smooth torsion-free tangent connection on a connected manifold. Let
\(\mathfrak h_x\subset\operatorname{End}(T_xM)\) be its holonomy Lie algebra, with the immersed Lie-group structure proved in C.5. If
\[
 K^1(\mathfrak h_x)=0,
 \tag{F.31}
\]
then \(\nabla R=0\) on the whole manifold. This holds even when the holonomy group is nonclosed. In particular a connection with nonparallel curvature has
\(K^1(\mathfrak h_x)\ne0\).

**Proof.** We first prove that each curvature endomorphism belongs to the holonomy Lie algebra at its base point. A tangent connection is represented by a principal connection on the full frame bundle: take as the columns of its local matrix \(a(X)\) the covariant derivatives of the chosen frame vectors. Changing the frame by a matrix \(g\) and applying the product rule gives
\(a'=g^{-1}ag+g^{-1}dg\), the connection law of Connections A.3. These local principal forms therefore glue.

Fix a frame \(u\) over \(y\). In a coordinate neighbourhood let \(U,V\) be the horizontal lifts of two coordinate vector fields. Their local flows exist and depend smoothly on parameters by Local tools 2.1. For sufficiently small \(t,s\), the commutator of these flows is
\[
 q(t,s)=\Phi_V^{-s}\Phi_U^{-t}\Phi_V^s\Phi_U^t(u)
                  =u\,g(t,s).
 \tag{F.32}
\]
The projected path is a coordinate rectangle and closes, so the last equality defines a unique smooth matrix \(g(t,s)\), by the smooth principal division map in PB A.2. The rectangle contracts within its coordinate chart. Thus \(g(t,s)\) belongs to restricted holonomy, and
\(g(0,s)=g(t,0)=I\).

The smooth-family construction in C.5, using C.1, makes \(g\) a smooth map into the intrinsic restricted holonomy group as well. Consequently
\(\partial_tg(0,s)\in\mathfrak h_u\) for every small \(s\), where \(\mathfrak h_u\) is the holonomy algebra expressed in the frame \(u\). Differentiating the linear equations of this vector subspace gives
\(\partial_s\partial_tg(0,0)\in\mathfrak h_u\). This argument does not require holonomy to be closed in the general linear group.

We compute this mixed derivative explicitly. In any local coordinates on the total frame bundle, differentiating the four flow compositions in (F.32) by the chain and product rules gives
\[
 \partial_s\partial_tq(0,0)
          =D V(u)\,U(u)-D U(u)\,V(u)=[U,V]_u.
 \tag{F.33}
\]
Here the first flow contributes the initial variation \(U(u)\); differentiating its transport by the second flow contributes \(DV(u)U(u)\). Differentiating the reverse \(U\)-flow at the displaced point contributes \(-DU(u)V(u)\). The reverse \(V\)-flow has no remaining first \(t\)-variation on the \(s=0\) axis, since the two \(U\)-flows cancel there. These are all mixed terms. Both first derivatives of \(q\) at the origin are zero, so this mixed derivative is an intrinsic tangent vector, with no coordinate-change Hessian term.

The bracket is vertical because its projected coordinate fields commute. By A.4,
\(\omega_u([U,V])=-\Omega_u(U,V)\). On the other hand, differentiating \(q=u\,g\), whose two first derivatives vanish at the origin, and using reproduction of fundamental vectors gives
\[
 \partial_s\partial_tg(0,0)=-\Omega_u(U,V).
 \tag{F.34}
\]
Therefore \(\Omega_u(U,V)\in\mathfrak h_u\). Coordinate pairs span all alternating input pairs, and A.7 identifies this with
\(R_y(v,w)\in\mathfrak h_y\) for arbitrary \(v,w\in T_yM\).

We next construct the smooth holonomy-algebra bundle without assuming a principal reduction by a closed subgroup. For any path \(\gamma:x\to y\), let \(P_\gamma:T_xM\to T_yM\) be its transport and define
\[
 \mathcal H_y=P_\gamma\mathfrak h_xP_\gamma^{-1}.
 \tag{F.35}
\]
This is independent of the path. Indeed for two choices their transport quotient is a holonomy element at \(x\); conjugation by this element is a smooth inner automorphism of the intrinsic holonomy group in C.5, and its differential preserves \(\mathfrak h_x\). The change-of-base conclusion of C.5 also identifies \(\mathcal H_y\) with the actual holonomy algebra at \(y\).

Near a point \(y_0\), choose a fixed path to \(y_0\), followed by the straight coordinate segment from \(y_0\) to \(y\) in a convex coordinate ball. Connections C.2 makes its transport a smooth matrix \(P(y)\). If \(A_1,\ldots,A_d\) is a basis of \(\mathfrak h_x\), the matrices
\(P(y)A_iP(y)^{-1}\) are a smooth pointwise independent frame. Hence \(\mathcal H\subset\operatorname{End}(TM)\) is a smooth vector subbundle.

Transport along every path preserves \(\mathcal H\), by concatenation in (F.35). Its induced covariant derivative preserves this subbundle too. To check that implication rather than assume it, take a path \(c\) from \(y\) and a section \(A\) of \(\mathcal H\). If \(P_t\) is transport along \(c|_{[0,t]}\), then
\(P_t^{-1}A(c(t))P_t\in\mathcal H_y\). Differentiate at \(t=0\). The matrix transport equation \(P_t'=-a(c'(t))P_t\) shows that this derivative is
\[
 (\nabla^{\operatorname{End}}_{c'(0)}A)_y
          =c'(0)(A)+[a(c'(0)),A].
 \tag{F.36}
\]
A derivative of a curve in the fixed vector subspace \(\mathcal H_y\) stays in it. Every tangent vector is the initial velocity of a coordinate path, so the preservation assertion follows in every direction.

The first part of the proof put \(R_y\) in \(\Lambda^2T_y^*M\otimes\mathcal H_y\). The first Bianchi identity puts it in \(K(\mathcal H_y)\). The two differentiation arguments in F.6 now apply verbatim to this smooth preserved algebra bundle: (F.21) differentiates the first Bianchi identity, and the zero-torsion instance of (F.22) gives the second. Thus
\((\nabla R)_y\in K^1(\mathcal H_y)\). Conjugation and transport of tangent arguments in (F.35) identify this fibre with \(K^1(\mathfrak h_x)\), because the two equations (F.19) commute with a linear change of basis. Under (F.31) every fibre is zero; hence \(\nabla R=0\) everywhere. \(\square\)

Theorem F.10 proves containment of curvature in the holonomy algebra and the full derivative criterion. Part G.3 proves the additional statement that transported curvature spans that algebra, and G.5 derives the first holonomy criterion.

The construction in this part uses the exact free Bryant arXiv version cited above, together with the complete earlier programme proofs specified at each step. New exposition and proof completions: GPT-6 Astra (OpenAI), October 2026, CC0 1.0. Source prose, figures and files are not reproduced. The partitions of unity it uses are proved in Local tools for bundles and transport.

## G. Transported curvature generates holonomy

This part completes the curvature-generation argument and the first algebraic holonomy criterion. Its free construction source is Andrew Clarke and Bianca Santoro, *Holonomy Groups in Riemannian Geometry*, [exact arXiv version 1206.3170v1](https://arxiv.org/abs/1206.3170v1), Section 3.4. We supply the parameter, topology and reduction arguments below; an external foliation or subgroup theorem is not a proof dependency. Throughout, paths are finitely piecewise \(C^1\), as in Part C.

**Lemma G.1 (comparison of two immersed group structures).** Suppose a homomorphism \(j:K\to H\) between finite-dimensional, Hausdorff, second-countable Lie groups is bijective, smooth, and has injective differential. Then it is a diffeomorphism.

**Proof.** Put \(m=\dim K\) and \(n=\dim H\); injectivity gives \(m\le n\). Translation makes the differential rank equal to \(m\) everywhere. By the constant-rank theorem, Local tools 1.4, each point of \(K\) has a coordinate neighbourhood on which \(j\) is an embedding onto a coordinate \(m\)-dimensional slice in \(H\).

We can cover \(K\) by countably many compact sets \(C_l\), each contained in one such neighbourhood. Here are the needed countability and compactness details. A second-countable space has a countable subcover of every open cover: for each basis member contained in a member of the cover, choose one such covering member; these choices still cover every point. Apply this to the coordinate neighbourhoods just obtained. In each of the resulting countably many Euclidean coordinate domains, closed balls with rational centres and rational positive radii whose closures lie in the domain form a countable covering family. Every point lies in one, by taking a sufficiently small ball and approximating its centre and radius by rationals. Their inverse chart images are compact by Local tools 0.1.

Each \(j(C_l)\) is compact and hence closed in the Hausdorff space \(H\). If \(m<n\), it has empty interior: it lies in a coordinate slice with a transverse coordinate identically zero, whereas an open Euclidean ball contains points with that coordinate nonzero. Thus these closed sets are nowhere dense.

We give the elementary completeness argument that rules out their covering \(H\). Choose in an \(H\)-chart a closed ball \(B_0\) of positive radius contained in the chart domain. Since \(j(C_1)\) has empty interior and is closed, there is a smaller closed coordinate ball \(B_1\) of positive radius inside the interior of \(B_0\), disjoint from \(j(C_1)\). Inductively choose \(B_l\) inside the interior of \(B_{l-1}\), disjoint from \(j(C_l)\), with radius at most \(2^{-l}\). In the fixed chart their centres are Cauchy: all centres after the \(l\)-th lie in \(B_l\), of diameter at most \(2^{1-l}\). Euclidean completeness gives a limit in every \(B_l\), since these balls are closed. That point belongs to none of the \(j(C_l)\), contradicting surjectivity. This proves \(m=n\).

The inverse-function theorem, Local tools 1.2, now gives a smooth local inverse everywhere. Bijectivity makes these local inverses restrictions of the unique global inverse, so that inverse is smooth. The dimension-zero case has the same conclusion directly from point charts. \(\square\)

Fix a principal \(G\)-bundle with connection form \(\omega\), curvature \(\Omega\), and \(u\in P_x\). Let \(P(u)\) denote the set of points reachable from \(u\) by horizontal lifts of paths. At this stage it is only a subset; no submanifold assertion is assumed. Let \(H,H^0,\mathfrak h\) be the full holonomy group, its identity component and its Lie algebra from C.5.

**Lemma G.2 (variation of horizontal transport).** Let \(c(s,t)\), \(0\le t\le1\), be a family of paths with \(c(s,0)=x\). Assume the parameter regularity of C.2 on a fixed finite time subdivision. Write \(q(s,t)\) for the horizontal lift with \(q(s,0)=u\), and define
\[
 b(s,t)=\omega_{q(s,t)}(\partial_s q(s,t)).
\]
Then
\[
 b(s,1)=\int_0^1
       \Omega_{q(s,t)}(\partial_tq(s,t),\partial_sq(s,t))\,dt .
 \tag{G.1}
\]
If also \(c(s,1)=x\), write \(q(s,1)=u\,g(s)\). Its left logarithmic derivative satisfies
\[
 \vartheta^L_{g(s)}g'(s)
   =\int_0^1
       \Omega_{q(s,t)}(\partial_tq,\partial_sq)\,dt ,
 \tag{G.2}
\]
where \(\vartheta^L_g=T_gL_{g^{-1}}\). In a matrix group the left side is \(g^{-1}g'\).

**Proof.** On a time piece C.2 supplies the parameter derivatives and their continuous mixed time derivatives. Pull back \(\omega\) along \(q\). Its \(dt\)-coefficient is zero by horizontality, so the pullback is \(b\,ds\). The structure equation A.4 gives
\[
 (q^*\Omega)(\partial_t,\partial_s)=\partial_t b:
 \qquad d(b\,ds)=\partial_t b\,dt\wedge ds,\quad
 [b\,ds,b\,ds]=0.
 \tag{G.3}
\]
The same computation is valid with \(C^1\) time regularity: the differentiated integral equation in C.2 gives
\(\partial_t\partial_sq=\partial_s\partial_tq\) continuously on each time piece, and the chain and product rules prove (G.3) in coordinates. No second pure time derivative is used.

At an interior subdivision point the two expressions for \(q(s,t)\) agree as functions of \(s\), so their \(s\)-derivatives agree and \(b\) is continuous there. Integrate (G.3) on each piece and add; the intermediate endpoint terms cancel. At \(t=0\), the lift is the fixed point \(u\), so \(b(s,0)=0\). This proves (G.1) by Local tools 0.3. The orbit map \(a\mapsto ua\) pulls \(\omega\) back to \(\vartheta^L\): the tangent \(T_eL_a A\) is represented by \(ua\exp(tA)\), on which reproduction of fundamental vectors gives \(A\). Apply this at \(q(s,1)=ug(s)\) to obtain (G.2). \(\square\)

**Theorem G.3 (curvature generation, including nonclosed holonomy).** For a connected base and arbitrary finite-dimensional structure Lie group,
\[
 \mathfrak h
  =\operatorname{span}_{\mathbb R}
    \{\Omega_v(X,Y):
        v\in P(u),\ X,Y\in T_vP\}.
 \tag{G.4}
\]
Horizontal \(X,Y\) suffice. The span in (G.4) is an ordinary finite-dimensional linear span, with no topological closure.

**Proof.** Denote the span on the right by \(\mathfrak k\). First we prove \(\mathfrak k\subseteq\mathfrak h\) without assuming a holonomy reduction. At \(v\in P(u)\), horizontally lift two coordinate vector fields \(U_0,V_0\). Their projected flows commute. The flow commutator
\[
 q(t,s)=\Phi_V^{-s}\Phi_U^{-t}\Phi_V^s\Phi_U^t(v)
        =v\,g(t,s)
 \tag{G.5}
\]
is the lift of a small contractible coordinate rectangle. The principal division map makes \(g\) smooth into \(G\), and its values lie in \(H_v^0\), with \(g(0,s)=g(t,0)=e\). By C.5 this smooth identity-containing family is smooth into the intrinsic \(H_v^0\) too. Change of base along the horizontal path to \(v\) identifies that group with \(H^0\), with the same construction of its smooth structure.

In a coordinate chart at \(e\) whose differential identifies \(T_eG\) with \(\mathfrak g\), the vectors \(\partial_tg(0,s)\) belong to the fixed subspace \(\mathfrak h\). Therefore their \(s\)-derivative at zero lies in \(\mathfrak h\) as well. The calculation F.33 applies to any flows, not only frame-bundle flows, and gives the intrinsic mixed tangent vector
\(\partial_s\partial_tq(0,0)=[U,V]_v\); both first derivatives vanish. Differentiating \(q=vg\) then gives
\[
 \partial_s\partial_tg(0,0)
   =\omega_v([U,V])=-\Omega_v(U,V).
 \tag{G.6}
\]
The last equality is A.4. Coordinate horizontal lifts span the horizontal tangent space, and curvature vanishes when an input is vertical. Thus every value in (G.4) is in \(\mathfrak h\).

The subspace \(\mathfrak k\) is invariant under \(\operatorname{Ad}(H)\). Indeed, if \(a\in H\) and \(v=T_\gamma u\), first lift a based loop with endpoint \(ua\) and then \(\gamma\). Equivariance gives endpoint \(va\), so \(va\in P(u)\). Curvature equivariance A.4 yields
\[
 \Omega_{va}(T_vR_aX,T_vR_aY)
       =\operatorname{Ad}(a^{-1})\Omega_v(X,Y).
 \tag{G.7}
\]
Using \(a^{-1}\) too proves equality of the transformed span with \(\mathfrak k\). Differentiating along \(\exp(tA)\) for \(A\in\mathfrak h\), using A.3 and Local tools 2.3, also proves
\([\mathfrak h,\mathfrak k]\subseteq\mathfrak k\).

We now bound the tangent rank of all finite products of small-lasso holonomies. A small lasso consists of a fixed stem from \(x\) to a point \(z\), a loop \(c\) in a convex coordinate ball about \(z\), and the reverse stem. In these coordinates put
\[
 c_s(t)=z+s(c(t)-z).
 \tag{G.8}
\]
The compact image of \(c\) stays inside the open ball, so (G.8) is defined in the ball for \(s\) in an open interval containing \([0,1]\). Its path and velocity have exactly the regularity of C.2. Write \(v\) for transport of \(u\) along the stem, and horizontally lift \(c_s\) from \(v\). Every point of this lift is in \(P(u)\). Equation (G.2) says that the left logarithmic derivative of the loop holonomy \(g(s)\) belongs to \(\mathfrak k\), since the integrand belongs to this finite-dimensional linear subspace. To justify the integral assertion, choose a linear complement by Local tools 0.2; projection onto the complement vanishes on the integrand and hence on its integral. Reverse transport along the stem takes \(vg(s)\) to \(ug(s)\), so this is the same group element for the whole lasso.

The right logarithmic derivative belongs to \(\mathfrak k\) too, since
\[
 \vartheta^R g'=\operatorname{Ad}(g)\vartheta^L g',
 \quad
 \vartheta^R_{ab}\,d(ab)=\vartheta^R_a\,da+
                    \operatorname{Ad}(a)\vartheta^R_b\,db .
 \tag{G.9}
\]
Here \(\vartheta^R_g=T_gR_{g^{-1}}\). Both identities follow by differentiating multiplication and translation; in matrices they read
\(g'g^{-1}=g(g^{-1}g')g^{-1}\) and
\(d(ab)(ab)^{-1}=da\,a^{-1}+a(db\,b^{-1})a^{-1}\).
Differentiating \(aa^{-1}=e\) gives the corresponding inverse formula
\(-\operatorname{Ad}(a^{-1})\vartheta^R_a\,da\).
The same translation calculation proves these identities for any Lie group. Equation (G.7) now shows that every word in such lasso curves and their inverses, with independently varying parameters, has differential rank at most \(\dim\mathfrak k\).

Apply C.1 to these lasso curves, each of which contains the identity at \(s=0\). Its constructed connected immersed group \(K\) has dimension equal to the maximum rank of their word maps, hence at most \(\dim\mathfrak k\). Its underlying set is \(H^0\): this is exactly the finite lasso factorization C.3, which applies to every continuously nullhomotopic piecewise \(C^1\) loop.

The identity map \(K\to H^0\) is smooth. Every chart of \(K\) in C.1 is a translated finite word expression in lasso curves, and C.5 makes these curves and word expressions smooth into \(H^0\). Its differential is injective because composition with the immersed inclusion \(H^0\hookrightarrow G\) is the immersed inclusion \(K\hookrightarrow G\). Lemma G.1 therefore makes this identity map a diffeomorphism. In particular
\[
 \dim\mathfrak h=\dim K\le\dim\mathfrak k
                    \le\dim\mathfrak h.
 \tag{G.10}
\]
Together with \(\mathfrak k\subseteq\mathfrak h\), equality of dimensions proves (G.4). No closedness, simply connectedness or completeness hypothesis has entered. \(\square\)

**Theorem G.4 (the full immersed holonomy reduction).** The reachable set \(P(u)\) has a Hausdorff second-countable smooth principal \(H\)-bundle structure over \(M\). Inclusion \(P(u)\hookrightarrow P\) is an injective immersion. The original connection restricts to an \(\mathfrak h\)-valued principal connection on this bundle, with the same horizontal transport and holonomy. Embeddedness is not asserted.

**Proof.** Choose a countable cover by convex coordinate balls \(U_i\), with centres \(z_i\), and a fixed path from \(x\) to each \(z_i\). Such paths exist: the points reachable by piecewise coordinate segments form an open set with open complement in a connected manifold, by the ball argument of C.1. Transport \(u\) along the fixed stem to \(v_i\), then along the straight segment from \(z_i\) to \(y\in U_i\). The resulting section \(\sigma_i(y)\) is smooth into \(P\) by C.2, and lies in \(P(u)\).

Each fibre of \(P(u)\) is exactly \(\sigma_i(y)H\). The inclusion from right to left follows by first transporting around a loop representing \(h\in H\), then following the path defining \(\sigma_i\). For the reverse inclusion, compare the path reaching a given \(w\in P(u)_y\) with the path defining \(\sigma_i(y)\), using reversal, equivariance and the division map. The unique element \(h\) with \(w=\sigma_i(y)h\) is the holonomy of their based concatenation. Thus
\[
 (y,h)\longmapsto \sigma_i(y)h
 \tag{G.11}
\]
is a bijection \(U_i\times H\to P(u)|_{U_i}\).

On overlaps write \(\sigma_j(y)=\sigma_i(y)a_{ij}(y)\). The division map makes \(a_{ij}\) smooth into \(G\) and its values are in \(H\). It is smooth into the intrinsic \(H\) as follows. Near a fixed overlap point \(y_0\), join \(y_0\) to \(y\) within a smaller convex coordinate neighbourhood in the overlap. The two stem-and-radial paths defining \(a_{ij}(y)\) then give a continuous family of based loops homotopic to the one at \(y_0\). By C.5 their values have the same coset modulo \(H^0\). Consequently
\(a_{ij}(y_0)^{-1}a_{ij}(y)\) is a smooth identity-containing family in \(H^0\), so C.5 makes it smooth there. Left translation proves the assertion for \(a_{ij}\).

Use (G.11) as bundle charts. Their transitions are
\((y,h)\mapsto(y,a_{ij}(y)h)\) in the appropriate direction, hence smooth. They define a manifold and a smooth free principal \(H\)-action, with the displayed local trivializations. Inclusion into \(P\) is smooth in these charts. Its differential is injective: its base component is the identity on \(T_yM\), and on the vertical component it is the injective differential of \(H\hookrightarrow G\). Its continuity and injectivity separate distinct points by ambient Hausdorff neighbourhoods. Countably many bundle charts, each with a countable basis from \(U_i\times H\), make the total space second countable.

It remains to prove that the connection really restricts; the mere set description does not prove this. Put \(a_i=\sigma_i^*\omega\). Varying the endpoint of the radial segment in any coordinate direction and applying (G.1) gives
\[
 a_i(\partial_{y^j})
   =\int_0^1\Omega_{q(y,t)}
                (\partial_tq,\partial_{y^j}q)\,dt
      \ \in\mathfrak h .
 \tag{G.12}
\]
All points \(q(y,t)\) are reachable from \(u\), so membership follows from G.3. In (G.11) the pulled-back form is therefore
\[
 \operatorname{Ad}(h^{-1})a_i+\vartheta_H^L ,
 \tag{G.13}
\]
which is \(\mathfrak h\)-valued and smooth. It reproduces fundamental \(H\)-vectors and is \(H\)-equivariant by the already proved connection transformation law, Connections A.3. Thus it is a principal \(H\)-connection.

Horizontal lifting for this connection exists over every finite path by Connections C.1 and C.2, applied to the Lie group \(H\). Its image in \(P\) solves the original horizontal-lift equation with the same initial value, because (G.13) is the pulled-back original form. Uniqueness gives equality of the lifts. Curvature is the pullback of \(\Omega\), by the structure equation and preservation of brackets under the inclusion of Lie algebras. Every original holonomy element is obtained by the same loop lift in \(P(u)\); conversely each loop lift there is an original loop lift. The holonomy group is exactly \(H\). \(\square\)

**Theorem G.5 (the first algebraic holonomy criterion).** Let \(\nabla\) be a smooth torsion-free tangent connection on a connected manifold, and let \(\mathfrak h_x\subseteq\operatorname{End}(T_xM)\) be its actual holonomy algebra. With \(K(\mathfrak h_x)\) and \((\mathfrak h_x)_K\) defined in F.6–F.7,
\[
 (\mathfrak h_x)_K=\mathfrak h_x.
 \tag{G.14}
\]
Together with F.10, a connection with nonparallel curvature satisfies both
\((\mathfrak h_x)_K=\mathfrak h_x\) and \(K^1(\mathfrak h_x)\ne0\). These are necessary conditions; no sufficiency or classification assertion is made.

**Proof.** Apply G.3 to the frame-bundle connection constructed in F.10. Fix \(y\in M\) and a path \(\gamma:x\to y\), with tangent transport \(P_\gamma\). By A.7, curvature in the frame transported along \(\gamma\) has endomorphism values
\(P_\gamma^{-1}R_y(v,w)P_\gamma\). Hence G.3 says that all these values span \(\mathfrak h_x\).

Transport both tangent arguments too and set
\[
 r_\gamma(v,w)=
   P_\gamma^{-1}R_y(P_\gamma v,P_\gamma w)P_\gamma,
       \qquad v,w\in T_xM .
 \tag{G.15}
\]
Curvature containment and change of base in F.10 make this tensor \(\mathfrak h_x\)-valued. Transporting the three inputs of the first Bianchi identity F.20 gives its cyclic identity, so \(r_\gamma\in K(\mathfrak h_x)\). Since \(P_\gamma\) is an isomorphism, the values in (G.15) still span \(\mathfrak h_x\). They are among the defining generators of \((\mathfrak h_x)_K\), giving one inclusion; the reverse inclusion follows from the definition of \(K(\mathfrak h_x)\). This proves (G.14). The derivative condition is exactly F.10 by contraposition. \(\square\)

**Theorem G.6 (flatness and transport).** A principal connection is flat, meaning \(\Omega=0\), if and only if its restricted holonomy is trivial. For a flat connection, transports along endpoint-fixed homotopic paths agree. On a simply connected base there is a global horizontal section through any prescribed initial point, and its trivialization identifies the connection with the product connection. Every flat connection has such a horizontal trivialization locally.

**Proof.** Equation (G.4) shows that \(\Omega=0\) implies \(\mathfrak h=0\). A zero-dimensional Lie group is discrete, since its charts are points. The connected group \(H^0\) must therefore be the singleton identity. Conversely \(H^0=\{e\}\) gives \(\mathfrak h=0\), so G.4 makes curvature vanish at every point reachable from \(u\). Every base point has a reachable point above it, and every other point of that principal fibre is its right translate. Curvature equivariance then makes \(\Omega\) vanish everywhere.

If two paths \(c,d:x\to y\) are homotopic with endpoints fixed, \(c*d^{-1}\) is a nullhomotopic based loop, using the explicit cancellation of C.3. Its transport is \(T_d^{-1}T_c\). Trivial restricted holonomy gives \(T_c=T_d\). On a simply connected base all paths with fixed endpoints are homotopic, by applying this same concatenation and cancellation to a contraction of \(c*d^{-1}\). Thus \(\sigma(y)=T_cu\) is independent of the chosen path \(c:x\to y\).

Locally choose a fixed stem and radial coordinate paths, as in G.4. The resulting local expression for \(\sigma\) is smooth by C.2, so \(\sigma\) is globally smooth. For any coordinate curve \(y(t)\) starting at \(y_0\), path independence gives
\(\sigma(y(t))=T_{y|_{[0,t]}}\sigma(y_0)\). Differentiating at zero makes \(d\sigma(y'(0))\) horizontal; every tangent vector is such an initial velocity. Therefore \(\sigma^*\omega=0\). The smooth principal trivialization \((y,g)\mapsto\sigma(y)g\), with smooth inverse from PB A.2, pulls the connection back to \(\vartheta_G^L\), the product connection.

For the local assertion restrict to a convex coordinate ball. Straight contraction makes it simply connected, and the restricted curvature still vanishes; the preceding proof applies. Conversely a horizontal local section has pullback connection form zero, so A.7 gives zero curvature there and equivariance gives zero curvature on its whole trivialization. \(\square\)

**Exercise G.7 (why transported curvature is necessary).** On the trivial \(U(1)\)-bundle over \(\mathbb R^2\), let the local connection form be \(a=i x^2\,dy\). Determine its curvature at the origin and its holonomy there.

**Solution.** Since the Lie algebra is abelian, A.7 gives
\[
 \Omega=da=2ix\,dx\wedge dy,\qquad \Omega_{(0,0)}=0.
 \tag{G.16}
\]
The exact abelian transport formula of Connections E.1 is
\(g(c)=\exp(-\int_c a)\). Traverse the rectangle
\((0,0),(1,0),(1,b),(0,b),(0,0)\).
The horizontal sides contribute zero, the side at \(x=0\) contributes zero, and the side at \(x=1\) contributes \(ib\). Hence its holonomy is \(\exp(-ib)\). As \(b\) varies through \(\mathbb R\), these values exhaust \(U(1)\), by the circle parametrization proved in Connections E.1. The plane contracts linearly, so full and restricted holonomy both equal \(U(1)\). Curvature vanishing at one point therefore does not make its holonomy algebra zero; (G.4) requires the curvature values over all transported points. \(\square\)

The mathematical source for the generation and reduction statements is the exact free Clarke–Santoro version identified above. All prerequisites used in the proofs are proved here or in the indicated earlier programme lessons. New exposition and proof completions: GPT-6 Astra (OpenAI), October 2026, CC0 1.0. Source prose, figures and files are not reproduced.

## H. Binary forms: all degrees and the complete cubic symbols

The free construction sources for this part are Etingof and collaborators, [*Introduction to representation theory*, exact arXiv 0901.0827v5](https://arxiv.org/abs/0901.0827v5), Section 1.14, Problem 1.55(a)–(f), and Bryant's [exact free arXiv math/9910059v2](https://arxiv.org/abs/math/9910059v2), Sections 1.4 and 3.2. We give the real-field representation proof, every curvature equation, the argument for arbitrarily large degree, and the small-degree and prolongation calculations. The sources' exercise instructions and dimension statements are not substitutes for these proofs.

Write \(E,H,F\) for the standard generators of the split real algebra, with
\[
 [H,E]=2E,\qquad [H,F]=-2F,\qquad [E,F]=H.
 \tag{H.1}
\]
Thus a representation is a triple of endomorphisms satisfying (H.1). For \(m\ge0\), let \(V_m\) have basis \(e_0,\ldots,e_m\), identified with the homogeneous monomials \(x^{m-j}y^j\), and put
\[
 Ee_j=j e_{j-1},\qquad
 He_j=(m-2j)e_j,\qquad
 Fe_j=(m-j)e_{j+1}.
 \tag{H.2}
\]
A term with a zero coefficient at an endpoint is zero; no vector with an out-of-range index is introduced.

**Theorem H.1 (all irreducible real modules).** Every nonzero finite-dimensional irreducible real representation of (H.1) is exactly one \(V_m\), up to equivalence. Each \(V_m\) is irreducible over both \(\mathbb R\) and \(\mathbb C\), and is faithful when \(m\ge1\). The one-dimensional \(V_0\) is trivial.

**Proof.** We first supply a real highest-weight argument without assuming complex eigenvalues. Eigenvectors for distinct real eigenvalues of any endomorphism are linearly independent. Indeed, in a shortest nontrivial relation \(\sum_j a_jv_j=0\), apply \(T-\lambda_1 I\); one term disappears and all remaining nonzero coefficients stay nonzero, contradicting minimality. This also proves that an endomorphism of a \(d\)-dimensional space has at most \(d\) distinct eigenvalues with nonzero eigenvectors.

Let the representation space have dimension \(n\ge1\). On its \(n^2\)-dimensional endomorphism space, the commutator with \(H\) satisfies
\[
 [H,E^j]=2jE^j,\qquad [H,F^j]=-2jF^j,
 \tag{H.3}
\]
by induction from \([H,AB]=[H,A]B+A[H,B]\). If all \(I,E,\ldots,E^{n^2}\) were nonzero, they would be \(n^2+1\) eigenvectors with distinct eigenvalues of this commutator operator, which is impossible. Some positive power of \(E\) vanishes, and hence \(E^{n^2}=0\). The same reasoning gives \(F^{n^2}=0\). In particular \(W=\ker E\) is nonzero: for any nonzero vector take the last nonzero term in its \(E\)-power sequence. The relation \(EH=HE-2E\) makes \(W\) invariant under \(H\).

For \(w\in W\), the relations imply
\[
 \begin{split}
 HF^jw&=F^j(H-2j)w,\\
 EF^jw&=jF^{j-1}(H-j+1)w,\\
 E^jF^jw&=j!\,H(H-1)\cdots(H-j+1)w.
 \end{split}
 \tag{H.4}
\]
For the second formula, \(j=1\) is \(EFw=Hw\). If it holds for \(j\), use \(EF=FE+H\) and the first formula to obtain
\[
 EF^{j+1}w
 =jF^j(H-j+1)w+F^j(H-2j)w
 =(j+1)F^j(H-j)w.
\]
The first formula follows by the same induction from \([H,F]=-2F\). Repeated application of the second proves the third, since every polynomial in \(H\) preserves \(W\).

Set \(N=n^2\). Since \(F^N=0\), (H.4) shows that
\(P(H)|_W=0\), where \(P(t)=\prod_{j=0}^{N-1}(t-j)\). This fact supplies a real eigenvector. Define
\[
 p_j(t)=\prod_{\substack{0\le k<N\\k\ne j}}
                     \frac{t-k}{j-k}.
\]
Then \(\sum_jp_j(t)=1\), because the difference is a polynomial of degree at most \(N-1\) vanishing at \(N\) distinct points. The elementary polynomial fact used here follows by dividing a polynomial vanishing at \(a\) by \(t-a\), successively at each distinct root; a nonzero polynomial cannot have more roots than its degree. Also \((t-j)p_j(t)\) is a scalar multiple of \(P(t)\). For nonzero \(w\in W\), at least one vector \(v=p_m(H)w\) is nonzero, and it satisfies \(Ev=0\), \(Hv=mv\), for an integer \(0\le m<N\).

Let \(q\) be the last index for which \(F^qv\ne0\). Nilpotence of \(F\) makes it finite. Apply the second formula in (H.4) to \(F^{q+1}v=0\):
\[
 0=(q+1)(m-q)F^qv.
\]
Thus \(q=m\). The vectors \(v,Fv,\ldots,F^mv\) are nonzero eigenvectors of \(H\) with distinct eigenvalues \(m,m-2,\ldots,-m\), so they are independent. Their span is invariant under \(E,H,F\) by (H.4), and irreducibility makes it the whole space. Rescale them by
\[
 e_j=\frac{(m-j)!}{m!}\,F^jv .
\]
The resulting action is exactly (H.2). Dimension \(m+1\) makes \(m\) unique.

Conversely, direct application to \(e_j\) verifies (H.1) for (H.2); for example \(EF e_j-FE e_j=((m-j)(j+1)-j(m-j+1))e_j=(m-2j)e_j\). The two other commutators follow from the change of the diagonal weight by \(2\) or \(-2\). This is also the action \(x\partial_y,\ x\partial_x-y\partial_y,\ y\partial_x\) on the stated monomials.

Any nonzero invariant subspace over \(\mathbb R\) or \(\mathbb C\) contains one of the \(e_j\): apply the Lagrange polynomials in the diagonal operator \(H\) to a nonzero vector and isolate a nonzero coordinate. Applying \(E^j\), then successive powers of \(F\), gives every basis vector. Thus the representation is irreducible over both fields. Finally, if \(aE+bH+cF=0\) and \(m\ge1\), applying it to \(e_0\) gives \(b=c=0\); applying it to \(e_1\) then gives \(a=0\). This proves faithfulness. \(\square\)

**Exercise H.2 (every invariant bilinear form).** Determine all invariant bilinear forms on \(V_m\), \(m\ge1\), and the signature in the even-degree case.

**Solution.** Invariance means \(B(Av,w)+B(v,Aw)=0\) for \(A=E,H,F\). The \(H\)-identity gives
\(2(m-i-j)B(e_i,e_j)=0\). Thus only the antidiagonal entries
\(b_i=B(e_i,e_{m-i})\) can be nonzero. The \(E\)-identity on \((e_i,e_{m+1-i})\) gives
\[
 i b_{i-1}+(m+1-i)b_i=0,\qquad
 b_i=\frac{(-1)^i}{\binom mi}\,b_0 .
 \tag{H.5}
\]
Here \(\binom mi=m!/(i!(m-i)!)\); substituting this expression verifies the recurrence. The \(F\)-identity is
\((m-i)b_{i+1}+(i+1)b_i=0\), the same recurrence. All other \(E\)- and \(F\)-identities have both terms zero by the weight condition. This proves existence and exhausts all invariant forms.

When \(b_0\ne0\), every antidiagonal entry is nonzero, so a vector pairing to zero with every basis vector has every coordinate zero. The form is nondegenerate. Equation (H.5) gives \(b_{m-i}=(-1)^m b_i\), so the form is alternating for odd \(m\) and symmetric for even \(m\). For \(m=2l\), each pair \(e_i,e_{m-i}\), \(i<l\), has matrix \(\left(\begin{smallmatrix}0&b_i\\b_i&0\end{smallmatrix}\right)\). The vectors \(e_i+e_{m-i}\) and \(e_i-e_{m-i}\) are orthogonal and have opposite nonzero squared values. Normalizing by the positive square roots of their absolute values, justified in Local tools 0.0, gives one positive and one negative direction per pair. The remaining middle direction has value
\[
 b_l=\frac{(-1)^l b_0}{\binom{2l}l}.
 \tag{H.6}
\]
The signature is \((l+1,l)\) if this is positive, and \((l,l+1)\) if negative. In particular the cubic form is symplectic, and a quartic form with \(b_0>0\) has signature \((3,2)\). No \(m\ge1\) admits an invariant positive-definite form: invariance under \(H\) already forces \(B(e_0,e_0)=0\). \(\square\)

For the rest of this part \(m\ge1\), and \(\mathfrak h\) is the faithful three-dimensional algebra acting on \(V_m\). For an alternating \(\mathfrak h\)-valued tensor write
\[
 R_{ij}=R(e_i,e_j)=a_{ij}E+b_{ij}H+c_{ij}F,
 \quad R_{ji}=-R_{ij},\quad R_{ii}=0.
 \tag{H.7}
\]

**Theorem H.3 (the equations and all large degrees).** Membership in \(K(\mathfrak h)\) is equivalent to the following equations for every \(0\le i<j<k\le m\) and \(0\le l\le m\):
\[
 \begin{aligned}
 0={}&k a_{ij}\delta_{l,k-1}+(m-2k)b_{ij}\delta_{l,k}
                    +(m-k)c_{ij}\delta_{l,k+1}\\
    &+i a_{jk}\delta_{l,i-1}+(m-2i)b_{jk}\delta_{l,i}
                    +(m-i)c_{jk}\delta_{l,i+1}\\
    &-j a_{ik}\delta_{l,j-1}-(m-2j)b_{ik}\delta_{l,j}
                    -(m-j)c_{ik}\delta_{l,j+1}.
 \end{aligned}
 \tag{H.8}
\]
Here a Kronecker delta is one when its indices agree and zero otherwise. These equations force \(K(\mathfrak h)=0\) for every \(m\ge5\).

**Proof.** Insert (H.2) and (H.7) into
\(R_{ij}e_k+R_{jk}e_i-R_{ik}e_j=0\), the first Bianchi identity of F.6, and take the coefficient of \(e_l\). This gives (H.8). Conversely those coefficients exhaust the vector equation. The Bianchi expression is alternating in \(i,j,k\), by alternation of \(R\); repeated inputs give zero and arbitrary inputs follow by trilinearity. Thus testing the ordered triples is sufficient.

There is a useful way to force a coefficient to vanish. Define the set of active output indices of \(\mathfrak h e_j\) by
\[
 S_j=\{j-1:j>0\}\ \cup\ \{j:m-2j\ne0\}\
                        \cup\ \{j+1:j<m\}.
 \tag{H.9}
\]
For fixed \(i<j\), choose \(k\ne i,j\). If \(k>0\) and \(k-1\notin S_i\cup S_j\), the coefficient of \(e_{k-1}\) in the Bianchi equation is only \(k a_{ij}\), so \(a_{ij}=0\). If \(m-2k\ne0\) and \(k\notin S_i\cup S_j\), it similarly forces \(b_{ij}=0\). If \(k<m\) and \(k+1\notin S_i\cup S_j\), it forces \(c_{ij}=0\). A permutation of the triple merely changes the overall sign, so \(k\) need not be larger than \(j\).

For \(a_{ij}\) it suffices to take
\(k\in\{1,\ldots,m\}\) outside \(\{i,i+1,i+2,j,j+1,j+2\}\), a set of at most six indices. For \(c_{ij}\), take
\(k\in\{0,\ldots,m-1\}\) outside
\(\{i-2,i-1,i,j-2,j-1,j\}\).
For \(b_{ij}\), take \(k\in\{0,\ldots,m\}\) outside
\(\{i-1,i,i+1,j-1,j,j+1\}\) and outside \(\{m/2\}\) if \(m\) is even. The respective available sets have \(m,m,m+1\) elements and exclude at most \(6,6,7\). For every \(m\ge7\) a choice exists in each case, proving that all coefficients vanish in all these degrees.

For completeness the exact active sets (H.9), including the vanishing middle weight when \(m\) is even, leave the following possible coefficients in the two remaining degrees. Every coefficient not listed is forced to zero by the preceding test.
\[
 \begin{array}{c|l}
 m&\text{possible nonzero coefficients}\\ \hline
 5&a_{03},a_{13},a_{14},b_{14},c_{14},c_{24},c_{25}\\
 6&a_{14},b_{15},c_{25}
 \end{array}
 \tag{H.10}
\]
This finite list can be checked directly from (H.9): for each pair remove \(S_i\cup S_j\) from the output indices \(k-1,k,k+1\) with their stated nonzero scalar coefficients. In degree five those active sets are
\(\{0,1\},\{0,1,2\},\{1,2,3\},\{2,3,4\},\{3,4,5\},\{4,5\}\).
In degree six they are
\(\{0,1\},\{0,1,2\},\{1,2,3\},\{2,4\},\{3,4,5\},\{4,5,6\},\{5,6\}\).
These lists specify every entry of the test.

For \(m=5\), the triples \(035,135,025,024\) now give, respectively,
\(5a_{03}e_4=0,\ 5a_{13}e_4=0,\ 5c_{25}e_1=0,\ 5c_{24}e_1=0\).
The triple \(014\) gives \(5b_{14}e_0+5c_{14}e_1=0\), so both coefficients vanish; \(145\) then gives \(5a_{14}e_4=0\). For \(m=6\), triples \(146,015,025\) give
\(6a_{14}e_5=0,\ 6b_{15}e_0=0,\ 6c_{25}e_1=0\).
Thus the remaining coefficients vanish too. This proves the assertion for every degree, not merely a finite numerical range. \(\square\)

**Theorem H.4 (all small curvature spaces).** The spaces \(K(\mathfrak h)\) for \(m=1,2,3,4\) have dimensions \(3,6,3,1\), respectively. Their complete tensors are as follows; unspecified pairs have value zero.

For \(m=1\), \(R_{01}\) is any element of \(\mathfrak h\). For \(m=2\), with six independent real parameters \(p,q,r,s,t,u\),
\[
 \begin{array}{c|l}
 ij&R_{ij}\\ \hline
 01&-uE-\tfrac12 rH+pF\\
 02&2tE+qH+rF\\
 12&sE+tH+uF
 \end{array}
 \tag{H.11}
\]
For \(m=3\), write \(R(a,b,c)\) for the three-parameter tensor
\[
 \begin{array}{c|l}
 ij&R(a,b,c)_{ij}\\ \hline
 01&-6aE\\
 02&-3bE+3aH\\
 03&9cE+9bH-9aF\\
 12&-5cE-bH+5aF\\
 13&3cH+3bF\\
 23&6cF
 \end{array}
 \tag{H.12}
\]
For \(m=4\), every tensor is \(tR_0\), where
\[
 (R_{0,03},R_{0,04},R_{0,12},R_{0,13},R_{0,14},R_{0,23})
      =(2E,-4H,-E,\tfrac12H,-2F,F).
 \tag{H.13}
\]
In each of these four degrees, \(\mathfrak h_K=\mathfrak h\).

**Proof.** In dimension two there are no ordered triples, so \(R_{01}\) is unrestricted. In degree two the only triple \(012\) has three coefficient equations
\[
 2b_{12}-a_{02}=0,\qquad
 2a_{01}+2c_{12}=0,\qquad
 -2b_{01}-c_{02}=0.
\]
Their full solution is (H.11), with the six remaining coefficients named as there.

We show explicitly that the two longer tables exhaust their equations. In degree three the single-coefficient test (H.9) first gives
\(b_{01}=c_{01}=a_{23}=b_{23}=0\).
Name \(c_{12}=5a,\ c_{13}=3b,\ c_{23}=6c\). Denote by \((ijk;l)\) the \(e_l\)-coefficient in (H.8). Successive equations give the following values:
\[
 \begin{array}{c|c@{\qquad}c|c}
 (012;2)&c_{02}=0 &(013;1)&b_{03}=9b\\
 (023;1)&a_{03}=9c &(013;0)&b_{13}=3c\\
 (023;2)&a_{02}=-3b &(012;0)&b_{12}=-b\\
 (123;1)&a_{13}=0 &(123;2)&a_{12}=-5c .
 \end{array}
 \tag{H.14}
\]
After these substitutions, all remaining equations are zero or one of
\[
 3a_{01}-2c_{03}=0,\quad
 -3b_{02}-c_{03}=0,\quad
 15a+2a_{01}-b_{02}=0.
\]
They give \(b_{02}=3a,\ a_{01}=-6a,\ c_{03}=-9a\). These are precisely all entries of (H.12). Conversely substitution of that table into (H.8) for the four triples makes every coefficient zero, as is also seen by reversing the displayed eliminations and checking their zero residuals.

In degree four the test (H.9) allows only
\[
 a_{03},b_{03},c_{03},b_{04},a_{12},
 a_{13},b_{13},c_{13},a_{14},b_{14},c_{14},c_{23}.
\]
Its active output sets are
\(\{0,1\},\{0,1,2\},\{1,3\},\{2,3,4\},\{3,4\}\);
they show directly that every omitted coefficient is zero. Set \(c_{23}=t\). The remaining equations successively give
\[
 \begin{array}{c|c@{\qquad}c|c}
 (013;2)&c_{03}=0 &(014;0)&b_{14}=0\\
 (023;1)&a_{03}=2t &(013;0)&b_{13}=t/2\\
 (034;3)&b_{04}=-4t &(014;1)&c_{14}=-2t\\
 (034;4)&b_{03}=0 &(013;1)&c_{13}=0\\
 (123;1)&a_{13}=0 &(123;2)&a_{12}=-t\\
 (124;1)&a_{14}=0 &&
 \end{array}
 \tag{H.15}
\]
This is (H.13). To verify all ten triple equations for \(R_0\), the possibly nonzero cyclic sums are the following, already expressed as multiples of basis vectors:
\[
 \begin{array}{c|l}
 013&0+2e_0-2e_0\\
 014&0-8e_1+8e_1\\
 023&0+4e_1-4e_1\\
 034&8e_3+0-8e_3\\
 123&-3e_2+3e_2+0\\
 124&-4e_3+0+4e_3\\
 134&-2e_4+0+2e_4 .
 \end{array}
\]
The triples \(012,024,234\) have all three terms zero. Thus all equations vanish, and there are no restrictions on \(t\).

Each parametrization is injective: its parameters can be read from the designated free entries. This proves the dimensions. Finally, for \(m=1\) the arbitrary \(R_{01}\) spans all of \(\mathfrak h\); for \(m=2\) the arbitrary \(R_{12}\) does. For \(m=3\), the tensor \(R(1,0,0)\) already has nonzero scalar multiples of \(E,H,F\) among its values. For \(m=4\), the same is true of \(R_0\). Their values therefore span \(\mathfrak h\), proving \(\mathfrak h_K=\mathfrak h\). \(\square\)

**Theorem H.5 (the entire derivative table and the holonomy restrictions).** The complete dimensions are
\[
 \begin{array}{c|r|r|r}
 m&\dim K&\dim K^1&\dim\mathfrak h_K\\ \hline
 1&3&6&3\\
 2&6&15&3\\
 3&3&4&3\\
 4&1&0&3\\
 m\ge5&0&0&0
 \end{array}
 \tag{H.16}
\]
In the cubic case every element \(S\in K^1\) has the form
\(S(e_i)=R(a_i,b_i,c_i)\), where
\[
 \begin{pmatrix}
 a_0&b_0&c_0\\
 a_1&b_1&c_1\\
 a_2&b_2&c_2\\
 a_3&b_3&c_3
 \end{pmatrix}
 =D(u,v,w,z):=
 \begin{pmatrix}
 0&-3u&-3v\\
 u&-v&-2w\\
 2v&w&-z\\
 3w&3z&0
 \end{pmatrix}.
 \tag{H.17}
\]
Consequently an irreducible split-real \(\mathfrak{sl}_2\) holonomy representation of a torsion-free tangent connection can only have \(m=1,2,3,4\). For \(m=4\) its curvature is parallel. Nonparallel curvature requires \(m=1,2,3\). These conclusions are necessary restrictions and do not assert realization.

**Proof.** By F.6, the derivative condition is
\[
 S(e_i)_{jk}-S(e_j)_{ik}+S(e_k)_{ij}=0
                \quad(i<j<k).
 \tag{H.18}
\]
For \(m=1\) there are no triples, so \(K^1=V_1^*\otimes K\) has dimension \(2\cdot3=6\). For \(m=2\) there is one triple and its target is \(\mathfrak h\). The map in (H.18) is onto: set \(S(e_1)=S(e_2)=0\), and choose \(S(e_0)\) using (H.11) so that its \(12\)-value is any prescribed element of \(\mathfrak h\). Its domain has dimension \(3\cdot6=18\), so its kernel has dimension \(18-3=15\). Here the elementary dimension formula follows by extending a basis of the kernel to a basis of the domain; the images of the added vectors form a basis of the image.

For \(m=3\), substitution of (H.12) makes the four rows of (H.18), in the \(E,H,F\) basis, exactly
\[
 \begin{array}{c|ccc}
 012&-5c_0+3b_1-6a_2&-b_0-3a_1&5a_0\\
 013&-9c_1-6a_3&3c_0-9b_1&3b_0+9a_1\\
 023&-9c_2-3b_3&-9b_2+3a_3&6c_0+9a_2\\
 123&-5c_3&-3c_2-b_3&6c_1-3b_2+5a_3 .
 \end{array}
 \tag{H.19}
\]
Setting these entries to zero gives
\[
 \begin{gathered}
 a_0=c_3=0,\quad b_0=-3a_1,\quad
 c_0=-\tfrac32a_2,\quad b_1=-\tfrac12a_2,\\
 c_1=-\tfrac23a_3,\quad b_2=\tfrac13a_3,\quad
 c_2=-\tfrac13b_3 .
 \end{gathered}
\]
The remaining entries of (H.19) then vanish identically. Put
\(u=a_1,\ v=a_2/2,\ w=a_3/3,\ z=b_3/3\); this gives exactly (H.17), with four independent parameters.

For \(m=4\), write \(S(e_i)=\lambda_iR_0\). Using (H.13), the triples \(012,013,023\), in order, give
\(-\lambda_0E=0,\ -2\lambda_1E=0,\ -2\lambda_2E=0\).
The triple \(034\) then gives \(4\lambda_3H+2\lambda_4E=0\). Independence of \(E,H\) forces every \(\lambda_i=0\). For \(m\ge5\), \(K=0\) already forces \(K^1=0\). Together with H.3–H.4 these facts prove the full table.

Theorem H.1 exhausts all irreducible real representations. The first holonomy criterion G.5 eliminates all \(m\ge5\), since their curvature-value span is zero but their acting algebra is three-dimensional. Theorem F.10 applied to the quartic zero derivative space forces \(\nabla R=0\). Its contraposition gives the stated restriction for nonparallel curvature. \(\square\)

**Theorem H.6 (complete cubic higher symbols).** Regard \(K^1\) as the subspace of \(V_3^*\otimes K\) given by (H.17). Define
\[
 \begin{aligned}
 K^2&=(V_3^*\otimes K^1)\cap
             (\operatorname{Sym}^2V_3^*\otimes K),\\
 K^3&=(V_3^*\otimes K^2)\cap
             (\operatorname{Sym}^3V_3^*\otimes K).
 \end{aligned}
 \tag{H.20}
\]
The intersections use the displayed inclusions in tensor powers of \(V_3^*\). Then \(K^2\) is one-dimensional and \(K^3=0\). In the coordinates \((u,v,w,z)\) of (H.17), every \(Q\in K^2\) has rows \(Q(e_i)=(u_i,v_i,w_i,z_i)\) given by
\[
 \begin{pmatrix}
 u_0&v_0&w_0&z_0\\
 u_1&v_1&w_1&z_1\\
 u_2&v_2&w_2&z_2\\
 u_3&v_3&w_3&z_3
 \end{pmatrix}
 =t
 \begin{pmatrix}
 0&0&0&-3\\
 0&0&1&0\\
 0&-1&0&0\\
 3&0&0&0
 \end{pmatrix}.
 \tag{H.21}
\]

**Proof.** Symmetry means that row \(j\) of
\(D(u_i,v_i,w_i,z_i)\) equals row \(i\) of
\(D(u_j,v_j,w_j,z_j)\). For the six pairs these are precisely the vanishing rows
\[
 \begin{array}{c|ccc}
 01&u_0&3u_1-v_0&3v_1-2w_0\\
 02&2v_0&3u_2+w_0&3v_2-z_0\\
 03&3w_0&3u_3+3z_0&3v_3\\
 12&-u_2+2v_1&v_2+w_1&2w_2-z_1\\
 13&-u_3+3w_1&v_3+3z_1&2w_3\\
 23&-2v_3+3w_2&-w_3+3z_2&z_3 .
 \end{array}
 \tag{H.22}
\]
From rows \(01,02,03\), first obtain
\(u_0=v_0=w_0=v_3=0\), then \(u_1=v_1=u_2=0\).
Rows \(13,23\) give \(z_1=w_2=w_3=z_2=z_3=0\).
The remaining equalities are
\(w_1=-v_2,\ z_0=3v_2,\ u_3=-z_0=3w_1\).
Putting \(t=w_1\) gives (H.21), and substitution verifies every row of (H.22). Thus there is exactly one free parameter.

Let \(T_i\) be the four rows of the matrix in (H.21). A member of \(V_3^*\otimes K^2\) has coefficients \(\lambda_i\) multiplying that fixed matrix. Symmetry of its first two inputs requires
\(\lambda_iT_j=\lambda_jT_i\) for all \(i,j\).
All four \(T_i\) are nonzero and pairwise linearly independent, since their nonzero entries occur in different columns. For each \(i\), choose \(j\ne i\); the displayed equality forces \(\lambda_i=\lambda_j=0\). Thus every coefficient is zero, proving \(K^3=0\). The inner two-input symmetry is already built into \(K^2\), so these additional transpositions give exactly full three-input symmetry, as required by (H.20). \(\square\)

**Theorem H.7 (the cubic modules and a regular flag).** As \(\mathfrak{sl}_2\)-modules, the cubic \(K\) and \(K^1\) are isomorphic to \(V_2\) and \(V_3\). The tableau \(K^1\subset V_3^*\otimes K\) has a flag with successive kernel drops \(3,1,0,0\), while its first symmetric prolongation has dimension one. These symbol calculations alone do not construct a torsion-free connection.

**Proof.** Use the natural tensor action (F.24) on \(K\). Substituting (H.12) gives
\[
 \begin{array}{c|ccc}
 &a'&b'&c'\\ \hline
 E\cdot(a,b,c)&0&-2a&-b\\
 H\cdot(a,b,c)&-2a&0&2c\\
 F\cdot(a,b,c)&-b&-2c&0
 \end{array}
 \tag{H.23}
\]
For example, the \(02\)-value of \(E\cdot R\) is
\([E,-3bE+3aH]-2R_{01}=6aE\), giving \(b'=-2a\).
The \(01\) and \(23\) values give the other two coordinates; the remaining pairs satisfy (H.12) with these same coordinates by substitution. The \(H\)-row follows by subtracting the two input weights from the output weight; the \(F\)-row follows in the same way from its commutator and input action. If \(\varepsilon_a,\varepsilon_b,\varepsilon_c\) denote the coordinate basis in this parameter space, the basis
\(\varepsilon_c,-\varepsilon_b,\varepsilon_a\) has exactly the action (H.2) for \(m=2\).

On \(S\in K^1\) the action is \((A\cdot S)(v)=A\cdot S(v)-S(Av)\). Substitution of (H.17) and (H.23) gives
\[
 \begin{array}{c|cccc}
 &u'&v'&w'&z'\\ \hline
 E&0&-u&-2v&-3w\\
 H&-3u&-v&w&3z\\
 F&-3v&-2w&-z&0
 \end{array}
 \tag{H.24}
\]
For instance the \(a\)-coordinates of rows \(1,2,3\) under \(E\) are \(0,-2u,-6v\), and the \(b\)-coordinate of row \(3\) is \(-9w\); these read off \(u',v',w',z'\) and give the first row of (H.24). The analogous coordinate checks give the other rows. The basis
\(\varepsilon_z,-\varepsilon_w/3,\varepsilon_v/3,-\varepsilon_u\)
therefore has the action (H.2) for \(m=3\), proving both module identifications.

For the flag take the ordered basis
\[
 v_1=e_0+e_3,\quad v_2=e_1,\quad v_3=e_2,\quad v_4=e_3.
\]
It is a basis because its coordinate matrix is invertible by subtracting its last column from its first. Let \(A_j\) be the subspace of \(K^1\) vanishing on \(v_1,\ldots,v_j\), with \(A_0=K^1\). Equation (H.17) gives
\(S(v_1)=(3w,-3u+3z,-3v)\).
This evaluation has rank three and kernel \(v=w=0,\ z=u\), of dimension one. On this kernel \(S(v_2)=(u,0,0)\), so \(A_2=0\), and \(A_3=A_4=0\). The successive drops
\(\dim A_{j-1}-\dim A_j\) are therefore \(3,1,0,0\).

These ranks are maximal: the first evaluation has three-dimensional target, and after it the remaining domain has dimension one. The displayed nonzero minors persist under a sufficiently small change of the ordered basis, so the flag is regular in this rank sense.

Here is the elementary bound behind the weighted sum. For a tableau \(A\subset\operatorname{Hom}(V,W)\) and an ordered basis \(v_1,\ldots,v_n\), let \(A_i\) consist of its maps vanishing on the first \(i\) basis vectors. In its symmetric prolongation \(A^{(1)}\), let \(B_i\) consist of \(Q\) with \(Q(v_j)=0\) for \(j\le i\). Symmetry gives
\(Q(v_{i+1})(v_j)=Q(v_j)(v_{i+1})=0\) for those \(j\), so evaluation at \(v_{i+1}\) maps \(B_i\) into \(A_i\), with kernel \(B_{i+1}\). The elementary dimension formula used in H.5 gives
\[
 \begin{aligned}
 \dim A^{(1)}
   &=\sum_{i=0}^{n-1}(\dim B_i-\dim B_{i+1})\\
   &\le\sum_{i=0}^{n-1}\dim A_i\\
   &=\sum_{j=1}^n j(\dim A_{j-1}-\dim A_j).
 \end{aligned}
 \tag{H.25}
\]
Both terminal spaces vanish because the \(v_j\) form a basis. The last equality follows by collecting the coefficient of each \(\dim A_i\).

In our case the bound is \(4+1=3+2=5\), whereas H.6 proves \(\dim K^2=1\). Equality in (H.25) for a regular flag is the algebraic involutivity condition; this tableau fails it. No existence theorem is invoked from this terminology. Actual connection coefficients must satisfy their differential equations and compatibility conditions; Part I supplies the nonlinear realization arguments. \(\square\)

**Lemma H.8 (the cubic ordinary prolongation is zero).** For the action on \(V_3\), the map
\(\delta:V_3^*\otimes\mathfrak h\to\Lambda^2V_3^*\otimes V_3\)
from F.2 is injective. A cubic \(\mathfrak{sl}_2\)-structure consequently has at most one compatible torsion-free connection.

**Proof.** Write \(A_i=A(e_i)=\alpha_iE+\beta_iH+\gamma_iF\). The equation \(\delta A=0\) is \(A_i e_j=A_j e_i\). For the pair \(03\), (H.2) gives
\(3\alpha_0e_2-3\beta_0e_3=3\beta_3e_0+3\gamma_3e_1\);
hence \(\alpha_0=\beta_0=\beta_3=\gamma_3=0\).
For \(02\), it now gives
\(\gamma_0e_3=3\beta_2e_0+3\gamma_2e_1\), so these three coefficients vanish. For \(13\), it gives
\(3\alpha_1e_2-3\beta_1e_3=\alpha_3e_0\), forcing those three to vanish. Finally \(12\) gives
\(\gamma_1e_3=\alpha_2e_0\), eliminating the remaining two coefficients. Thus \(A=0\). Differences of compatible torsion-free connections lie in this kernel by F.2, so uniqueness follows. Existence is not asserted. \(\square\)

The exact free representation source is by Pavel Etingof, Oleg Golberg, Sebastian Hensel, Tiankai Liu, Alex Schwendner, Dmitry Vaintrob and Elena Yudovina. Its Section 1.14 supplies the representation problem; H.1 gives a complete real-field solution. Bryant's exact free preprint supplies the holonomy and cubic-symbol questions; H.3–H.8 give the full calculations. New exposition and proof completions: GPT-6 Astra (OpenAI), October 2026, CC0 1.0. Source prose, figures and files are not reproduced.

## I. Poisson realization, including singular data

The construction in this part uses the freely readable author preprint of Chi, Merkulov and Schwachhöfer, Section 3, and Crainic and Mărcuț's exact arXiv preprint, cited below. Their omitted local calculations and existence prerequisites are proved here. Teschl's free author draft supplies the analytic-ODE construction lead; the coefficient argument below proves the required convergence without assuming a complex-analysis theorem. Throughout this part, analytic means locally represented by an absolutely convergent real power series. Smooth statements also hold without the analytic hypothesis.

**Lemma I.1 (analytic calculus, implicit functions and flows).** An analytic map has analytic local inverses wherever its derivative is invertible. Analytic equations with invertible derivative in the unknown have analytic local solutions. The local flow of an analytic vector field is analytic jointly in time and initial value; an analytic ordinary differential equation also has analytic dependence on all its analytic parameters. Integration over a fixed compact real time interval preserves analyticity in parameters when the integrand is jointly analytic on a neighbourhood of that interval and the parameter in question.

**Proof.** We supply the convergence facts used in this assertion. For a vector of positive radii \(r=(r_1,\ldots,r_d)\), let \(\mathcal A_r\) consist of formal series
\[
 f(z)=\sum_{\nu\in\mathbb N^d}c_\nu z^\nu,\qquad
 \|f\|_r=\sum_\nu |c_\nu|r^\nu<\infty.
 \tag{I.1}
\]
Here \(z^\nu=\prod_jz_j^{\nu_j}\) and \(r^\nu=\prod_jr_j^{\nu_j}\). It is a complete normed algebra. Indeed, for a Cauchy sequence, every weighted coefficient has a limit. The sum of the absolute differences over any finite set is bounded by the Cauchy bound; taking the supremum over all finite sets proves both summability of the limit and convergence in norm. For multiplication, the coefficient at \(\nu\) is the finite sum over \(\mu+\kappa=\nu\). The triangle inequality, followed by the increasing finite partial sums of nonnegative numbers, gives \(\|fg\|_r\leq\|f\|_r\|g\|_r\). Finite vectors of series are complete with the sum of the component norms.

The series converge uniformly on the closed box of radii \(r\): a tail is bounded by its norm tail. On a smaller box, every differentiated series converges uniformly too. For example, at radii \(\rho_j<r_j\), each differentiation multiplies a term by at most a constant times \(|\nu|\), while its weight acquires a factor bounded by \(q^{|\nu|}\), where \(q=\max_j(\rho_j/r_j)<1\). The numbers \(n^kq^n\) are bounded for every fixed \(k\): choose \(q<q'<1\); eventually \((1+1/n)^kq<q'\), so the sequence decreases at a geometric rate after a finite initial segment. The fundamental theorem of calculus applied to finite polynomial sums, then uniform convergence of the sums and derivatives, justifies termwise differentiation. In particular these series define smooth functions with the indicated derivatives.

Absolute convergence also justifies substitution and composition. If \(F(w)=\sum_\nu a_\nu w^\nu\) converges absolutely at a positive radius vector \(R\), and series \(w_j\) satisfy \(\|w_j\|_r<R_j\), the substituted series converges in \(\mathcal A_r\), since
\[
 \sum_\nu |a_\nu|\prod_j\|w_j\|_r^{\nu_j}
 \leq\sum_\nu |a_\nu|R^\nu.
 \tag{I.2}
\]
Evaluating finite partial sums and passing to the norm limit identifies this series with the actual composition. Expanding about an interior constant instead of zero gives the same assertion. A reciprocal with nonzero constant is analytic after shrinking: factor out that constant and use the geometric series in an algebra element of norm less than one. Determinants and the adjugate formula therefore give analytic matrix inversion.

For completeness, the estimates also give an analytic implicit-function theorem directly. After translation and multiplication by an invertible matrix, write \(F(u,z)=0\) as \(u=T(u,z)\), where \(T(0,0)=0\) and \(D_uT(0,0)=0\). Work in \(\mathcal A_r\) for the parameter \(z\), with unknown vector \(u\) in a closed norm ball of radius \(b\). Absolute convergence of the derivative series and the absence of a constant term in \(D_uT\) let us choose \(b\), then the parameter radii, so that the substitution norm of \(D_uT\) on this ball is less than a fixed \(q<1\). The estimate follows term by term from
\[
 u^k-v^k=\sum_{j=0}^{k-1}u^j(u-v)v^{k-1-j},
\]
and its successive application to the factors of a multivariable monomial; hence it bounds the difference of two substitutions by \(q\|u-v\|_r\). Shrink the parameter radii further so that \(\|T(0,z)\|_r<(1-q)b\). The map preserves the ball and is a contraction. The complete contraction proof in Local tools 1.1 applies to this complete normed space, and yields a convergent power-series solution. Pointwise it is the unique nearby solution, by the same finite-dimensional contraction argument. Applying this to \(F(u,z)=f(u)-z\) proves the analytic inverse assertion. The submersion and constant-rank coordinate constructions of Local tools 1.3–1.4 now also work analytically.

For an ODE, translate the data and write its integral equation as
\[
 u(t,\eta,\lambda)
  =\eta+\int_0^t F(s,u(s,\eta,\lambda),\lambda)\,ds.
 \tag{I.3}
\]
In the algebra of series in \(t,\eta,\lambda\), integration in \(t\) has operator norm at most its radius \(r_t\): the term \(c\,t^j\) becomes \(c\,t^{j+1}/(j+1)\). Choose a small fixed norm ball of radius \(b\) for \(u\) on which the substituted \(F\) and its \(u\)-derivative have finite bounds \(M,L\). These bounds exist by (I.2), using smaller radii than the original convergence radii. Make the norm of \(\eta\) less than \(b/2\), choose \(r_tM<b/2\) and \(r_tL<1\), and apply the contraction proof again. Termwise differentiation on smaller boxes proves the ODE. Local tools 2.1 supplies uniqueness, so this analytic solution is the smooth solution already constructed there. Initial time is another analytic parameter in \(F(t_0+s,u,\lambda)\). A finite succession of local flow maps, whose compositions are analytic by (I.2), proves analyticity wherever a solution exists through a fixed compact time interval.

Finally cover the compact time interval by finitely many boxes of joint analyticity about \((t_i,z_0)\), and subdivide it so that each closed subinterval lies strictly inside one such box. Choose a common positive parameter radius smaller than all those boxes allow. In each box expand the integrand in \((t-t_i,z-z_0)\). Absolute coefficient sums bound the integral of the absolute series on its subinterval. Integrating term by term thus gives a parameter series with finite coefficient norm, by the triangle inequality and the interval length. Adding the finitely many series proves the integration assertion. This argument supplies convergence, rather than inferring analyticity from smooth parameter dependence. □

**Lemma I.2 (local integral coordinates).** Let \(D\) be a smooth rank-\(k\) vector subbundle of \(TN\). Suppose brackets of its local sections are sections of \(D\). Near every point there are coordinates in which \(D\) is spanned by the first \(k\) coordinate vector fields. The coordinates may be chosen analytic if the subbundle has analytic local frames. Its local leaves are the slices with the other coordinates constant.

**Proof.** A nonvanishing vector field \(X\) can be straightened. Choose a coordinate hyperplane transverse to \(X\) at the point and map \((t,z)\) to the time-\(t\) flow of \(X\) starting at \(z\) in that hyperplane. Its derivative at the point is invertible: its first column is \(X\), and the other columns span the chosen hyperplane. Local tools 1.2 and 2.1 give the smooth coordinate map. Lemma I.1 gives its analytic version. In these coordinates \(X=\partial_t\), by the flow equation.

Proceed by induction on \(k\); for \(k=0\) there is nothing to prove. Straighten one member of a local frame. Subtract from the other frame members their \(t\)-components times \(\partial_t\), obtaining independent \(Z_2,\ldots,Z_k\) tangent to the \(t\)-slices. Involutivity and their zero \(t\)-components give
\[
 [\partial_t,Z_a]=\sum_{b=2}^k C_{ab}(t,z)Z_b.
 \tag{I.4}
\]
The coefficients are smooth, or analytic, since an invertible minor of the frame solves for them. Solve the matrix equation \(M'=-MC\), \(M(0,z)=I\). It has the same regularity by Local tools 2.1 and I.1. It is invertible: the solution of \(N'=CN\), \(N(0,z)=I\), satisfies \((MN)'=0\), so \(MN=I\); a square matrix with a right inverse is invertible by finite-dimensional linear algebra. The fields \(Y_a=\sum_bM_{ab}Z_b\) satisfy \(\partial_tY_a=0\), and thus are the extensions of fields on the slice \(t=0\). Their brackets are tangent to that slice and lie in their span, by involutivity of \(D\). Apply the induction hypothesis on the slice, then keep those new coordinates independent of \(t\). This proves the coordinate assertion. On any connected small integral manifold, each remaining coordinate has zero differential, and is constant along coordinate segments. Thus the indicated slices give the local integral leaves and the local quotient by them. □

**Lemma I.3 (Poisson and symplectic conventions).** Let
\[
 \pi=\tfrac12\sum_{i,j}P^{ij}(x)\,\partial_{x^i}\wedge\partial_{x^j},
 \qquad P^{ij}=-P^{ji},
\]
and define \(\{f,g\}=\sum_{i,j}P^{ij}\partial_i f\,\partial_jg\). This bracket satisfies Jacobi precisely when
\[
 \sum_\ell\left(
 P^{i\ell}\partial_\ell P^{jk}
 +P^{j\ell}\partial_\ell P^{ki}
 +P^{k\ell}\partial_\ell P^{ij}\right)=0
 \quad\text{for all }i,j,k.
 \tag{I.5}
\]
Our anchor and Hamiltonian field convention is
\[
 \beta(\pi^\sharp\alpha)=\pi(\alpha,\beta),\qquad
 X_f=\pi^\sharp df,\qquad X_fg=\{f,g\}.
 \tag{I.6}
\]
On a symplectic manifold with two-form \(\sigma\), we define \(X_f\) by \(\iota_{X_f}\sigma=df\). Its bracket is Poisson. In a coordinate frame, if \(W\) is the matrix of \(\sigma\), its Poisson matrix is \(W^{-1}\), and the matrix of \(\pi^\sharp\) is \(-W^{-1}\).

**Proof.** The bracket is skew and obeys the product rule. Its Jacobiator is a derivation in each of its three entries: expanding the product rule produces two cross terms from each of two cyclic summands, with opposite signs, while the remaining terms give the product rule for the Jacobiator. Alternatively expanding the displayed coordinate bracket cancels the second-derivative terms in pairs using \(P^{ij}=-P^{ji}\). The coefficient of \(\partial_i f\,\partial_jg\,\partial_kh\) is exactly (I.5). Necessity follows by taking coordinate functions, and sufficiency follows from the same expansion.

Jacobi implies
\[
 [X_f,X_g]=X_{\{f,g\}},
 \tag{I.7}
\]
because application to \(h\) gives the Jacobi identity. In the symplectic case, smooth matrix inversion gives unique smooth fields \(X_f\). Cartan's formula A.2 gives \(\mathcal L_{X_f}\sigma=0\), and
\(\iota_{[X_f,X_g]}\sigma=\mathcal L_{X_f}dg=d(X_fg)\).
Thus (I.7) holds for the symplectic bracket as well. Applying this equality to \(h\) proves its Jacobi identity directly. Finally \(\sigma(X,\cdot)\) has coordinate column \(-WX\), so \(X_f=-W^{-1}df\), and evaluating \(dg(X_f)\) proves the matrix assertions. In particular, for \(\sigma=dx\wedge da\), our convention gives \(\{x,a\}=-1\). All signs below use (I.6). □

**Theorem I.4 (regular coordinates and the smaller realization).** Near a point where a Poisson tensor has constant rank \(2r\), there are local coordinates
\((p_1,q_1,\ldots,p_r,q_r,z_1,\ldots,z_s)\) in which
\[
 \pi=\sum_{i=1}^r\partial_{p_i}\wedge\partial_{q_i}.
 \tag{I.8}
\]
They may be chosen analytic for an analytic tensor. On the product of this coordinate neighbourhood with \(\mathbb R^s\), with extra coordinates \(w_\alpha\), the form
\[
 \sigma=\sum_{i=1}^r dq_i\wedge dp_i+
             \sum_{\alpha=1}^s dw_\alpha\wedge dz_\alpha
 \tag{I.9}
\]
is symplectic and projection is a Poisson submersion. Its dimension is \(2r+2s\).

**Proof.** If the rank is positive, some coordinate function \(p\) has \(X_p\ne0\). Straighten this field as in I.2 and choose its time coordinate \(q\), so that \(\{p,q\}=1\). Subtract constants to put \(p=q=0\) at the chosen point. Since \(dp(X_q)=-1\) and \(dq(X_p)=1\), the two differentials are independent. Their joint zero set is a local submanifold by Local tools 1.3. Equation (I.7) gives \([X_p,X_q]=0\). These fields have commuting local flows: the pushforward of \(X_q\) by the flow of \(X_p\) has derivative the transported bracket, hence is constant when the bracket vanishes. This derivative identity follows by differentiating the flow composition on a coordinate function, or equivalently from A.2's flow definition of the Lie derivative. Uniqueness of the flow ODE then gives commutation.

For a point \(z\) on the joint zero set, use
\[
 (s,t,z)\longmapsto
     \operatorname{Fl}_{X_p}^{\,t}\operatorname{Fl}_{X_q}^{-s}(z).
 \tag{I.10}
\]
It has invertible derivative, carries \(p\) to \(s\) and \(q\) to \(t\), and makes \(X_p=\partial_q\), \(X_q=-\partial_p\). The identities defining these Hamiltonian fields force every mixed coefficient between \(p,q\) and the remaining coordinates to vanish. Jacobi says that every Hamiltonian flow preserves the bracket: \(X_f\{g,h\}=\{X_fg,h\}+\{g,X_fh\}\). Taking the remaining coordinate functions shows that the remaining coefficients are independent of both \(p\) and \(q\). Consequently
\(\pi=\partial_p\wedge\partial_q+\pi_0(z)\), where \(\pi_0\) satisfies (I.5) and has constant rank \(2r-2\). Induction gives (I.8); at rank zero all coefficients vanish. A skew form has even rank by the elementary elimination into nondegenerate two-dimensional pairs used in F.1, so this accounts for the entire rank. The flow and inverse constructions are analytic by I.1 when the coefficients are analytic.

The constant matrix of (I.9) is invertible, its exterior derivative is zero, and I.3 gives its bracket as \(\sum_i\partial_{p_i}\wedge\partial_{q_i}+\sum_\alpha\partial_{z_\alpha}\wedge\partial_{w_\alpha}\). For functions pulled back from the original neighbourhood, the second sum vanishes. Projection is a submersion, proving the realization assertion and dimension. □

**Lemma I.5 (a two-form from a cotangent spray).** Let \(O\subset\mathbb R^n\) be open, with Poisson matrix \(P(x)\), and put \(B(x)=-P(x)\), the matrix of \(\pi^\sharp\). In cotangent coordinates \((x,a)\), consider a smooth vector field
\[
 \mathcal V(x,a)=\bigl(B(x)a,\gamma(x,a)\bigr),
 \quad \gamma(x,0)=0,\quad D_a\gamma(x,0)=0.
 \tag{I.11}
\]
There is an open neighbourhood \(S\) of the entire zero section in \(T^*O\) on which its flow \(\varphi_t\) exists for \(0\leq t\leq1\), and
\[
 \sigma=\int_0^1\varphi_t^*\sigma_{\rm can}\,dt,
 \qquad \sigma_{\rm can}=\sum_i dx^i\wedge da_i
 \tag{I.12}
\]
is closed and nondegenerate. Such a field exists with \(\gamma=0\). Every ordinary Poisson spray on this chart has the form (I.11). If the coefficients are analytic, so is \(\sigma\).

**Proof.** Every \((x,0)\) is stationary. Local tools 2.1, iterated along the compact stationary time interval, gives an open neighbourhood of this point on which the flow exists throughout that interval. Taking their union gives an open neighbourhood of the zero section. This does not require a common fibre radius over a noncompact \(O\). Differentiate the field at \((x,0)\). The identity \(\gamma(x,0)=0\) also gives \(D_x\gamma(x,0)=0\), so its derivative is the block matrix \(\left(\begin{smallmatrix}0&B(x)\\0&0\end{smallmatrix}\right)\). The variational equation therefore gives
\[
 (d\varphi_t)_{(x,0)}(u,v)=(u+tB(x)v,v).
 \tag{I.13}
\]
For two such tangent vectors,
\[
 \sigma_{(x,0)}\bigl((u,v),(w,z)\bigr)
   =z(u)-v(w)+\pi_x(v,z).
 \tag{I.14}
\]
Indeed substitution into \(\sigma_{\rm can}\) adds \(2t\pi(v,z)\), whose integral is \(\pi(v,z)\). Pairing first with all \((w,0)\) shows that a null vector has \(v=0\); pairing then with all \((0,z)\) gives \(u=0\). Thus the form is nondegenerate at every zero. The determinant remains nonzero on an open neighbourhood; intersect it with the flow domain to define \(S\). Differentiation under the fixed integral is justified by Local tools 0.3 on compact time intervals. Pullback commutes with \(d\), so \(d\sigma=0\).

A Poisson spray is a field with base projection \(B(x)a\) and dilation law \(m_t^*\mathcal V=t\mathcal V\), where \(m_t(x,a)=(x,ta)\), \(t>0\). The law says \(\gamma(x,ta)=t^2\gamma(x,a)\). Taylor expansion at zero shows \(\gamma(x,0)=D_a\gamma(x,0)=0\); indeed it also identifies \(\gamma\) with its quadratic Taylor term. Thus every such spray is covered. Our proof even allows any smooth vertical term vanishing to first order at the zero section. Lemma I.1 proves analytic dependence of the flow and analyticity of its fixed-time integral. □

**Lemma I.6 (the exact endpoint calculation).** Along an integral curve \((x(t),a(t))=\varphi_t(\xi)\), set
\[
 A^i{}_j(t)=\sum_k\partial_jB^i{}_k(x(t))a_k(t),\quad
 D u=u'-Au,\quad D^*\alpha=\alpha'+A^T\alpha.
 \tag{I.15}
\]
For a variation \(v_0\in T_\xi(T^*O)\), write
\(d\varphi_t(v_0)=(u(t),v(t))\). Then
\[
 Du=Bv,\qquad D(B\alpha)=B D^*\alpha.
 \tag{I.16}
\]
If \(\eta_v\) solves \(D^*\eta_v=v\), and \(\eta_w\) is the analogous solution for a second variation with components \((w,z)\), then
\[
 \sigma(v_0,w_0)
 =\left[\eta_w(u)-\eta_v(w)-\pi(\eta_v,\eta_w)\right]_{t=0}^{t=1}.
 \tag{I.17}
\]
The auxiliary equations admit arbitrary prescribed initial or final values.

**Proof.** Differentiating \(x'=B(x)a\) gives \(u'=Au+Bv\), independently of the vertical part of the spray. Jacobi (I.5) gives
\[
 B'=AB+BA^T.
 \tag{I.18}
\]
Here the \(ik\) entry on the left is
\(\sum_{\ell,j}\partial_\ell P^{ki}P^{j\ell}a_j\).
The corresponding entry on the right is
\(\sum_{\ell,j}(\partial_\ell P^{ji}P^{k\ell}
 +P^{\ell i}\partial_\ell P^{jk})a_j\).
Their equality is (I.5) for \(j,k,i\), with antisymmetry applied to its last two terms. This explicit calculation is the use of the Poisson condition. Differentiating \(B\alpha\) and using (I.18) gives the second identity of (I.16).

The two dual derivatives satisfy
\[
 (\alpha(u))'=(D^*\alpha)(u)+\alpha(Du),\qquad
 \bigl(\pi(\alpha,\beta)\bigr)'
   =\pi(D^*\alpha,\beta)+\pi(\alpha,D^*\beta).
 \tag{I.19}
\]
The first is the product rule with cancelling \(A\)-terms. For the second use \(\pi(\alpha,\beta)=\beta^TB\alpha\) and (I.18); the \(A\)-terms again cancel. Substitute \(D^*\eta_v=v\), \(D^*\eta_w=z\), \(Du=Bv\), \(Dw=Bz\) in the derivative of the bracket in (I.17). The terms \(\eta_w(Bv)=\pi(v,\eta_w)\) cancel one derivative of \(\pi\), and \(-\eta_v(Bz)=\pi(\eta_v,z)\) cancels the other. What remains is \(z(u)-v(w)=\sigma_{\rm can}((u,v),(w,z))\). Integration proves (I.17).

These auxiliary equations are finite-dimensional inhomogeneous linear ODEs on the compact interval. To see that their solutions cannot stop inside it, bound their coefficients by \(L\) and inhomogeneous term by \(C\). On intervals of length \(\delta\) with \(\delta L<1/2\), the integral equation bounds the supremum of a solution by \(2(|\eta(t_0)|+\delta C)\). Finitely many such intervals cover \([0,1]\); Local tools 2.1 continues each solution through them. Reversing time treats final data. □

**Theorem I.7 (symplectic realization at every Poisson point).** With \(S,\sigma\) from I.5, the cotangent projection \(p:S\to O\) is a Poisson submersion, regardless of changes in the rank of \(\pi\). Moreover, with \(p_1=p\circ\varphi_1\),
\[
 (\ker dp)^{\perp_\sigma}=\ker dp_1.
 \tag{I.20}
\]
This gives a local smooth symplectic realization near every point of every smooth Poisson manifold, and an analytic one for analytic input. The conclusion holds for every spray covered by I.11.

**Proof.** Both \(p\) and \(p_1\) are submersions: projection is one, and a flow map is locally a diffeomorphism, with inverse the reversed flow by uniqueness. Their kernels have dimension \(n\). Take \(v_0\in\ker dp\), \(w_0\in\ker dp_1\), so that \(u(0)=0\), \(w(1)=0\). Choose the auxiliary solutions in I.6 with \(\eta_v(0)=0\), \(\eta_w(1)=0\). Both endpoint values in (I.17) vanish. Thus \(\ker dp_1\subset(\ker dp)^\perp\). Nondegeneracy identifies the latter with the annihilator of an \(n\)-dimensional subspace in a \(2n\)-dimensional space, so it too has dimension \(n\). This proves (I.20).

Let \(\theta\in T^*_{p(\xi)}O\), and let \(v_0\) be defined by
\(\iota_{v_0}\sigma=p^*\theta\).
It belongs to \((\ker dp)^\perp=\ker dp_1\), so \(u(1)=0\). In (I.17), choose \(\eta_v(1)=0\) and let \(\eta_w(0)=\zeta\) be arbitrary. Evaluation on any \(w_0\), whose base component at zero is \(w(0)\), gives
\[
 \theta(w(0))
 =\eta_v(0)(w(0))+
       \zeta\bigl(B(x(0))\eta_v(0)-u(0)\bigr).
 \tag{I.21}
\]
For each fixed \(w_0\) we may choose every \(\zeta\), by I.6. Hence \(u(0)=B\eta_v(0)\). Choosing \(\zeta=0\), and using surjectivity of \(dp\), then gives \(\eta_v(0)=\theta\). Consequently
\[
 dp(v_0)=\pi^\sharp\theta.
 \tag{I.22}
\]
For \(\theta=df\), this says \(dp(X_{p^*f})=X_f\). Applying \(dg\) proves \(\{p^*f,p^*g\}_S=p^*\{f,g\}\). This is exactly the Poisson property, with the convention I.6. The local chart construction proves the manifold statement, and I.1 and I.5 give its analytic version. Neither an external foliation theorem nor a constant-rank hypothesis enters this argument. □

**Example I.8 (a realization through a rank change).** On \(\mathbb R^2\), let
\(\pi=x\,\partial_x\wedge\partial_y\).
It has rank two for \(x\ne0\) and rank zero on \(x=0\). A symplectic realization on all of \(\mathbb R^4\), with coordinates \((x,y,u,v)\), is projection together with
\[
 \begin{aligned}
 \sigma={}&h(v)\,dx\wedge du+dy\wedge dv\\
          &+uH(v)\,dx\wedge dv+xh(v)\,du\wedge dv,\\
 h(v)={}&\int_0^1e^{-tv}\,dt,\qquad
 H(v)=\int_0^1\int_0^t e^{-sv}\,ds\,dt .
 \end{aligned}
 \tag{I.23}
\]
Both functions are analytic, including at zero, with \(h(0)=1\), \(H(0)=1/2\).

**Verification.** In dimension two the alternating three-index expression (I.5) vanishes. The zero-vertical-part spray is
\(\mathcal V=-vx\,\partial_x+ux\,\partial_y\), with flow
\[
 \varphi_t(x,y,u,v)
 =\left(xe^{-tv},\,y+ux\int_0^t e^{-sv}\,ds,\,u,\,v\right).
 \tag{I.24}
\]
It is defined for all real time and data. Substituting in \(dx_t\wedge du+dy_t\wedge dv\), then integrating, gives (I.23). For the last coefficient use
\(\frac{d}{dt}\bigl(t\int_0^te^{-sv}ds\bigr)
=\int_0^te^{-sv}ds+te^{-tv}\).
For \(v\ne0\),
\[
 h(v)=\frac{1-e^{-v}}v,\qquad
 H(v)=\frac{v-1+e^{-v}}{v^2}.
 \tag{I.25}
\]
The integral definitions remove both apparent singularities. Expanding the exponential proves absolute convergence of the resulting series on every bounded interval: \(\sum |v|^k/k!\) converges by a ratio bound once \(k>2|v|\). Termwise integration yields the stated values and analyticity. The identity \(h'-H+h=0\) proves \(d\sigma=0\) directly. Its matrix determinant is \(h(v)^2>0\), since the defining integral for \(h\) is positive. Direct inversion gives the \(xy\) entry of the Poisson matrix equal to \(x\), in agreement with I.7. Thus the total symplectic form remains nondegenerate above the entire rank-zero line; no division by \(x\) has been used. □

**Theorem I.9 (admissible maps and every Jacobi identity).** Let \(\mathfrak g\subset\mathfrak{gl}(V)\) be a finite-dimensional real Lie algebra, and let \(\phi:\mathfrak g^*\to\Lambda^2V^*\) be smooth. For \(a\in\mathfrak g^*\), define
\[
 \begin{aligned}
 \delta_Aa(B)&=a([A,B]),&
 j(q,x)(A)&=q(Ax),\\
 \lambda(D_a(x,y))&=(d\phi_a(\lambda))(x,y).
 \end{aligned}
 \tag{I.26}
\]
Here \(A,B\in\mathfrak g\), \(q\in V^*\), \(x,y\in V\), \(\lambda\in\mathfrak g^*\), and \(D_a:\Lambda^2V\to\mathfrak g\) is defined by the natural finite-dimensional double-dual identification. Suppose
\[
 \begin{aligned}
 (d\phi_a(\delta_Aa))(x,y)
    &=\phi_a(Ax,y)+\phi_a(x,Ay),\\
 D_a(x,y)z+D_a(y,z)x+D_a(z,x)y&=0 .
 \end{aligned}
 \tag{I.27}
\]
On \(W^*=\mathfrak g^*\oplus V^*\), define the bracket on linear coordinate functions by
\[
 \{\ell_A,\ell_B\}=\ell_{[A,B]},\quad
 \{\ell_A,\ell_x\}=\ell_{Ax},\quad
 \{\ell_x,\ell_y\}=\phi_a(x,y),
 \tag{I.28}
\]
and extend by the coordinate bivector rule. This is Poisson. Conversely its Jacobi identities imply (I.27). The first condition holds, in particular, if
\(\phi(a\circ\operatorname{Ad}_g)(x,y)=\phi(a)(gx,gy)\)
for every element of a connected matrix group with Lie algebra \(\mathfrak g\).

**Proof.** By I.3 it is enough to check triples of linear coordinates. For three elements of \(\mathfrak g\), the identity is the Lie algebra Jacobi identity. For \(A,B,x\), it is
\(A(Bx)-B(Ax)-[A,B]x=0\), the defining matrix commutator identity. For \(A,x,y\), the cyclic sum is
\[
 (d\phi_a(\delta_Aa))(x,y)
     -\phi_a(x,Ay)-\phi_a(Ax,y),
 \tag{I.29}
\]
which is zero by (I.27). Finally the \(\mathfrak g^*\)-component of \(X_{\ell_x}\) is \(-j(q,x)\), so the cyclic sum for \(x,y,z\) is
\[
 -q\bigl(D_a(y,z)x+D_a(z,x)y+D_a(x,y)z\bigr).
 \tag{I.30}
\]
It vanishes by the second condition. Conversely, (I.29) and (I.30), for all \(q\), imply both conditions. Differentiating the stated group equivariance at \(g=\exp(tA)\) gives the first. Thus every coordinate Jacobi identity has been accounted for. □

**Theorem I.10 (a connection from any realized parameter).** For an admissible \(\phi\) as in I.9 and any point \((a_0,q_0)\in W^*\), there is a local torsion-free connection on a manifold of dimension \(\dim V\), with connection matrices in \(\mathfrak g\), and a frame at which
\[
 R(x,y)=-D_{a_0}(x,y),\qquad
 (\nabla_xR)(y,z)=
      \bigl(dD_{a_0}(j(q_0,x))\bigr)(y,z).
 \tag{I.31}
\]
The connection is analytic when \(\phi\) is analytic. The construction applies also at singular Poisson parameters.

**Proof.** By I.7, take a symplectic realization \(\mu:S\to U\subset W^*\) through the specified point, and choose a preimage \(s_0\). For \(w\in W=\mathfrak g\oplus V\), let \(\xi_w=X_{\mu^*\ell_w}\). These fields are pointwise independent as \(w\) varies in a basis of \(W\): \(d\mu\) is onto, so \((d\mu)^*\) is injective, and the symplectic form converts independent covectors to independent vectors. The Poisson property and I.7 give \(d\mu(\xi_w)=X_{\ell_w}\). Using (I.7) and (I.28), their brackets are
\[
 [\xi_A,\xi_B]=\xi_{[A,B]},\quad
 [\xi_A,\xi_x]=\xi_{Ax},\quad
 [\xi_x,\xi_y]=\xi_{D_a(x,y)}.
 \tag{I.32}
\]
The last expression means the field obtained by taking the variable coefficients of \(D_a(x,y)\), pulled back by \(\mu\), in the fixed \(\xi_A\)-frame. It follows by differentiating \(\phi_a(x,y)\); no bracket formula for constant coefficients is being applied to a variable coefficient without its differential.

The rank-\(\dim W\) distribution spanned by these fields is involutive: the bracket of two variable linear combinations expands into the displayed brackets and derivatives of their coefficients, all in the same span. Lemma I.2 supplies a local integral manifold \(F\) through \(s_0\). On \(F\) let \((\omega,\theta)\) be the dual \(\mathfrak g\oplus V\)-valued coframe, so that \((\omega,\theta)(\xi_{A+x})=(A,x)\). Evaluation of exterior derivatives on every pair of these frame fields gives
\[
 d\theta=-\omega\wedge\theta,\qquad
 d\omega+\tfrac12[\omega,\omega]
       =-\tfrac12D_a(\theta\wedge\theta).
 \tag{I.33}
\]
We normalize \(D_a(\theta\wedge\theta)(U,V)=2D_a(\theta(U),\theta(V))\), and \((\omega\wedge\theta)(U,V)=\omega(U)\theta(V)-\omega(V)\theta(U)\). For two vertical fields (I.33) is the first bracket of (I.32); for one vertical and one horizontal field it is the second; for two horizontal fields it is the third. This verifies all components and factors.

The vertical distribution spanned by the \(\xi_A\) is itself involutive. Use I.2 to choose a local quotient \(F\to M\) and a transverse local section \(s:M\to F\) through \(s_0\). Then \(e=s^*\theta\) is a \(V\)-valued coframe, since \(\ker\theta\) is precisely that vertical distribution; put \(A=s^*\omega\). Define a connection by
\[
 \nabla_XY=e^{-1}\bigl(X(e(Y))+A(X)e(Y)\bigr).
 \tag{I.34}
\]
The product rule verifies the connection axioms. Its torsion is \(e^{-1}(de+A\wedge e)\), which is zero by (I.33), and its curvature in this frame is \(dA+\tfrac12[A,A]\), hence \(-D_{a\circ s}\) by the same equation. This directly constructs the base and its connection; no global quotient of a local group action is assumed.

For its covariant derivative, first differentiate the infinitesimal identity in (I.27). If \(\mathfrak g\) acts on its curvature tensors by
\[
 (A\cdot D)(x,y)=[A,D(x,y)]-D(Ax,y)-D(x,Ay),
 \tag{I.35}
\]
the result is \(dD_a(\delta_Aa)=-A\cdot D_a\). Indeed differentiation of the left side of (I.27) in a direction \(\lambda\) has two terms,
\((d^2\phi_a(\lambda,\delta_Aa))(x,y)
+(d\phi_a(\delta_A\lambda))(x,y)\);
the second is \(\lambda([A,D_a(x,y)])\). Moving it to the other side and using every \(\lambda\) proves the assertion. On \(F\), the parameter satisfies, by (I.28),
\[
 da(\xi_A)=\delta_Aa,\qquad da(\xi_x)=-j(q,x).
 \tag{I.36}
\]
Consequently, on the section a tangent vector with \(e(X)=x\) obeys
\(da(X)=\delta_{A(X)}a-j(q,x)\).
The tensor connection formula F.6 says \(\nabla R=dR+A\cdot R\) in this coframe. Substitute \(R=-D_a\), (I.35) and (I.36): the vertical terms cancel, and the result is the second identity in (I.31).

All these fields, distributions, coframes and quotient sections are analytic when \(\phi\) is analytic, by I.1, I.2 and I.7; hence so is (I.34). If \(G\subset GL(V)\) is an injectively immersed Lie subgroup with Lie algebra \(\mathfrak g\), the trivial principal bundle \(M\times G\) has solder form \(g^{-1}e\) and connection form \(\operatorname{Ad}_{g^{-1}}A+g^{-1}dg\). PB and Conn prove its associated connection is (I.34). Its frame map \((m,g)\mapsto e_m^{-1}g\) is an injective immersion. In the embedded case it is the usual local \(G\)-reduction; the connection construction does not require closedness. □

**Theorem I.11 (full holonomy and a nonparallel test).** In I.10, suppose the values of \(D_{a_0}\) span \(\mathfrak g\). Then the resulting connection has holonomy algebra \(\mathfrak g\). It has nonparallel curvature if \(dD_{a_0}(j(q_0,x))\ne0\) for some \(x\). If \(D\) has a nonzero derivative at any point of the full-span set, some \(q_0,x\) give this nonparallel example.

**Proof.** A connected injectively immersed matrix group \(G\) with this algebra can be constructed if it has not already been specified. Generate a subgroup by the curves \(\exp(tA)\), \(A\in\mathfrak g\). Conjugation by these curves preserves \(\mathfrak g\): its derivative is the linear equation with operator \(\operatorname{ad}A\), which preserves this finite-dimensional subspace, so uniqueness gives the assertion. The logarithmic derivatives of every finite word in these curves therefore lie in \(\mathfrak g\). Their ranks are at most \(\dim\mathfrak g\), while a word in exponentials of a basis has exactly this rank at the origin. The complete subgroup construction C.1 supplies the required connected group with Lie algebra \(\mathfrak g\).

Parallel transport is given in the frame \(e\) by the \(\mathfrak g\)-valued connection matrix. Its group ODE, proved in Local tools 2.2 and Conn C.2, gives solutions in \(G\); uniqueness identifies them with the matrix transport. Apply C.5 to the principal bundle \(M\times G\) in I.10 to obtain its intrinsic holonomy group and algebra. Its image in the frame group has algebra contained in \(\mathfrak g\). F.10 puts each curvature value at the chosen frame in this algebra. Equation (I.31) and the spanning hypothesis imply the reverse inclusion. The same equation gives the nonparallel test directly.

The span of the elements \(j(q,x)\) is all of \(\mathfrak g^*\). Indeed, an element \(A\) annihilated by all of them satisfies \(q(Ax)=0\) for every \(q,x\), hence \(A=0\) as an endomorphism. By finite-dimensional duality the span has zero annihilator and is the whole dual space. Thus if \(dD_a\) is nonzero, it cannot vanish on every \(j(q,x)\). In particular this applies when \(\phi\) is not affine on some connected open component of the full-span set: if \(dD\) vanished throughout that component, \(D\) would be constant along each segment in a small ball by the fundamental theorem, and hence on the component. The sets accessible by finite polygonal paths in an open connected set are open equivalence classes, so there is only one; integration would make \(\phi\) affine there. This component qualification avoids inferring nonparallelness merely from different affine formulas on disconnected components. □

**Example I.12 (an actual analytic cubic connection).** Use the real binary-cubic representation H.1, with basis \(e_0,e_1,e_2,e_3\), and dual Lie algebra coordinates
\[
 \alpha=a(E),\qquad\beta=a(H),\qquad\gamma=a(F).
\]
For any real constant \(c\), define a skew form \(\phi_a\) by its six upper-triangular entries:
\[
 \begin{array}{c|l}
 ij&\phi_a(e_i,e_j)\\ \hline
 01&-3\alpha^2\\
 02&3\alpha\beta\\
 03&-9\alpha\gamma-\tfrac92\beta^2+c\\
 12&5\alpha\gamma+\tfrac12\beta^2-\tfrac c3\\
 13&-3\beta\gamma\\
 23&-3\gamma^2
 \end{array}
 \tag{I.37}
\]
This is admissible and gives a real analytic torsion-free connection on a four-dimensional base with full restricted holonomy equal to the image of \(SL(2,\mathbb R)\) on binary cubics and with nonparallel curvature.

**Verification.** Differentiating the six entries with respect to \(\alpha,\beta,\gamma\) gives exactly
\[
 D_a=R(\alpha,-\beta,-\gamma)
 \tag{I.38}
\]
in H.4's complete cubic curvature table. Thus the first Bianchi condition is already fully proved. To verify the other condition, the three vector fields \(\delta_Aa\) in these coordinates are
\[
 \delta_Ea=(0,-2\alpha,\beta),\quad
 \delta_Ha=(2\alpha,0,-2\gamma),\quad
 \delta_Fa=(-\beta,2\gamma,0).
 \tag{I.39}
\]
Substitution in (I.37) gives the following six entries of its directional derivative, in the order \(01,02,03,12,13,23\):
\[
 \begin{aligned}
 \delta_E\phi={}&
 (0,-6\alpha^2,9\alpha\beta,3\alpha\beta,
                  6\alpha\gamma-3\beta^2,-6\beta\gamma),\\
 \delta_H\phi={}&
 (-12\alpha^2,6\alpha\beta,0,0,
                   6\beta\gamma,12\gamma^2),\\
 \delta_F\phi={}&
 (6\alpha\beta,6\alpha\gamma-3\beta^2,-9\beta\gamma,
                  -3\beta\gamma,-6\gamma^2,0).
 \end{aligned}
 \tag{I.40}
\]
Using \(Ee_j=je_{j-1}\), \(He_j=(3-2j)e_j\), \(Fe_j=(3-j)e_{j+1}\) from H.1, the entries of \(\phi(Ae_i,e_j)+\phi(e_i,Ae_j)\) are these same lists. For example the \(13\) entry for \(E\) is \(\phi_{03}+3\phi_{12}=6\alpha\gamma-3\beta^2\); the constants cancel. The other potentially constant combinations are checked in the same lists. Thus every entry of the first condition of (I.27) is verified for a basis of \(\mathfrak{sl}_2\), hence for every \(A\).

Choose \(a_0=(1,0,0)\), \(q_0=e_1^*\), \(c=0\). Equation (I.38) gives \(D_{a_0}=R(1,0,0)\), whose values at \(01,02,03\) are \(-6E,3H,-9F\); they span the acting algebra. Moreover
\[
 j(q_0,e_0)=(0,0,3),\qquad
 dD_{a_0}(j(q_0,e_0))=R(0,0,-3)\ne0.
 \tag{I.41}
\]
Theorems I.10–I.11 therefore supply an actual analytic connection with full Lie algebra and nonparallel curvature, rather than only algebraically permissible tensors.

To identify its restricted group, first \(SL(2,\mathbb R)\) is an analytic Lie group: the gradient of \(ad-bc\) is \((d,-c,-b,a)\), which is nonzero when the determinant is one, so I.1 gives regular level-set coordinates. Multiplication and the determinant-one inverse are polynomial, and its tangent algebra at the identity is the trace-zero matrices. It is connected. For a matrix with first column \(v\ne0\), put \(r=|v|>0\), \(u=v/r\), and let \(Ju\) be its positive quarter-turn. The determinant-one condition uniquely writes the second column as \(t u+r^{-1}Ju\). Thus the matrix is the product of the rotation with columns \(u,Ju\) and \(\left(\begin{smallmatrix}r&t\\0&r^{-1}\end{smallmatrix}\right)\). The circle is path connected by Local tools 6.3; \(r\) can be joined to \(1\) inside the positive half-line, and \(t\) to zero. These give a path to the identity. The action on the third symmetric power is polynomial and differentiates to H.1's three displayed operators. It is faithful: if a matrix fixes every cubic, it fixes the cubes of both basis vectors; equality of cubes of real linear forms forces equality of the forms, so it fixes both vectors and is the identity. H.1 also proves injectivity of its derivative. The image has the injectively immersed connected Lie-group structure transported from \(SL(2,\mathbb R)\).

The restricted holonomy lies in this image and has its full Lie algebra. Its inclusion has invertible derivative at the identity, so the inverse function theorem gives an open identity neighbourhood in the image. The subgroup is therefore open; its cosets are open, and connectedness of the image forces it to be the whole image. This argument uses the intrinsic group topology and does not assume the image is closed.

At the chosen parameter, the seven-dimensional target Poisson matrix, in coordinates \((\alpha,\beta,\gamma,q_0,q_1,q_2,q_3)\), has rank six. Its last row and column are zero, and its first six rows and columns form
\[
 \begin{pmatrix}
 0&-2&0&0&0&2\\
 2&0&0&0&1&0\\
 0&0&0&3&0&0\\
 0&0&-3&0&-3&0\\
 0&-1&0&3&0&0\\
 -2&0&0&0&0&0
 \end{pmatrix}.
 \tag{I.42}
\]
Expanding along the last row and then its paired column, and next along the \(\gamma\)-row and its paired column, leaves the \((\beta,q_1)\) block. The determinant is \(2^2\,3^2\,1^2=36\). This proves rank six; the same minor remains nonzero nearby, while an odd-dimensional skew matrix has rank at most six. The regular realization I.4 consequently has dimension eight, while the cotangent realization I.7 has dimension fourteen. In both cases the independent Hamiltonian distribution has dimension seven and its vertical subdistribution dimension three, giving the same four-dimensional connection base. The larger realization changes neither of these latter dimensions. □

The cubic structure equations for every connection, determination of the full germ by curvature data, the complex representation tests, and the complete converse at singular structure-equation data remain to be proved in subsequent parts. The existence theorem and endpoint calculation above are not substitutes for those assertions.

Free construction sources for this part: Quo-Shin Chi, Sergey A. Merkulov and Lorenz J. Schwachhöfer, *On the Existence of Infinite Series of Exotic Holonomies*, [free author preprint dated 9 April 1996](https://wwwold.mathematik.tu-dortmund.de/~lschwach/papers/Berger/InfExoticHol.pdf), native pages 7–13, Section 3; Marius Crainic and Ioan Mărcuț, *On the existence of symplectic realizations*, [arXiv:1009.2085v1](https://arxiv.org/pdf/1009.2085v1), native pages 1–7; Gerald Teschl, *Ordinary Differential Equations and Dynamical Systems*, [free author preliminary version](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf), Section 4.1, native pages 122–124. The exact access records identify the retained editions. No paid onward reference supplies a proof here, and no source prose, image or PDF is redistributed. The preceding proofs, including the analytic convergence and local quotient arguments, supply every construction prerequisite used in this part.

## J. Complete cubic equations and local determination

We now complete the real cubic construction using the exact free Chi–Merkulov–Schwachhöfer author preprint cited in Part I, especially its Section 3 and the cubic case of its appendix. The latter leaves a linear calculation to the reader; J.1 supplies it. The local equivalence argument below also supplies the details needed at singular Poisson data. All algebraic prerequisites are proved in Parts F–I. No classification, external equivalence theorem or external analyticity theorem is assumed.

Write \(V=\operatorname{Sym}^3(\mathbb R^2)\), with the basis \(e_0,e_1,e_2,e_3\) and operators \(E,H,F\) of H.1. Let \(\mathfrak g\) and \(G\) be the cubic images of \(\mathfrak{sl}_2(\mathbb R)\) and \(\mathrm{SL}_2(\mathbb R)\). The connectedness and faithfulness of this group were proved in I.12. Throughout J.1–J.6, \(\alpha=a(E),\beta=a(H),\gamma=a(F)\) are the coordinates of \(a\in\mathfrak g^*\). Write \(Q(a)=\phi_0(a)\) for the quadratic part of I.12, and let \(\Omega\) be the invariant alternating form with \(\Omega(e_0,e_3)=1\), \(\Omega(e_1,e_2)=-1/3\). Thus
\[
\begin{array}{c|rrrrrr}
ij&01&02&03&12&13&23\\\hline
Q(a)_{ij}&-3\alpha^2&3\alpha\beta&-9\alpha\gamma-\tfrac92\beta^2&5\alpha\gamma+\tfrac12\beta^2&-3\beta\gamma&-3\gamma^2
\end{array}
\tag{J.1}
\]
Set \(\phi_c(a)=Q(a)+c\Omega\), and define \(D_a(x,y)\in\mathfrak g\) by
\[
\lambda(D_a(x,y))=dQ_a(\lambda)(x,y),\qquad
j(q,x)(A)=q(Ax),\qquad
(\delta_Aa)(B)=a([A,B]).
\tag{J.2}
\]
In particular \(D_a\) is linear in \(a\), and I.12 identifies it with the H.4 curvature tensor \(R(\alpha,-\beta,-\gamma)\). In this part \(\mathcal R\) denotes the actual curvature tensor of a connection, so as to distinguish it from that parametrization.

**Lemma J.1 (the entire cubic bilinear compatibility space).** Over either \(\mathbb R\) or \(\mathbb C\), a bilinear form \(T\) on the cubic module satisfies
\[
T(x,Ay)=T(y,Ax)\quad(x,y\in V,\ A\in\mathfrak g)
\tag{J.3}
\]
if and only if \(T=c\Omega\) for a scalar \(c\).

**Proof.** Put \(t_{ij}=T(e_i,e_j)\). The equations for \(E,H,F\), respectively, are
\[
j t_{i,j-1}=i t_{j,i-1},\qquad
(3-2j)t_{ij}=(3-2i)t_{ji},\qquad
(3-j)t_{i,j+1}=(3-i)t_{j,i+1},
\tag{J.4}
\]
where a zero coefficient makes an out-of-range term zero. In the first equation use \(i=0\), \(j=1,2,3\): this kills \(t_{00},t_{01},t_{02}\). In the third use \(i=3\), \(j=0,1,2\): it kills \(t_{31},t_{32},t_{33}\). The second equation at the pairs \(01,02,13,23\) then kills \(t_{10},t_{20},t_{13},t_{23}\). The first equation at \(12\) kills \(t_{11}\), and the third at \(12\) kills \(t_{22}\). The four remaining entries satisfy
\[
t_{30}=-t_{03},\qquad t_{21}=-t_{12},\qquad 3t_{12}=t_{30}.
\tag{J.5}
\]
They are exactly the entries of \(t_{03}\Omega\). Conversely, the invariance proved in H.2 says \(\Omega(Ax,y)+\Omega(x,Ay)=0\). Alternation changes its first term into \(-\Omega(y,Ax)\), giving (J.3). All divisions above are by nonzero real integers, so the same proof works over the complex field. \(\square\)

**Lemma J.2 (the two parameter identifications).** The maps
\[
a\longmapsto D_a:\mathfrak g^*\longrightarrow K(\mathfrak g),\qquad
q\longmapsto L_q:V^*\longrightarrow K^1(\mathfrak g),\qquad
L_q(x)=D_{j(q,x)}
\tag{J.6}
\]
are isomorphisms. They respect the tensor actions, with the following conventions: \(D\) has the ordinary curvature action, whereas \(a\) and \(q\) transform by composition with \(\operatorname{Ad}_g\) and \(g\) on a change of frame by \(g\).

**Proof.** The first assertion is precisely the H.4 table with the invertible change of coordinates \((a,b,c)=(\alpha,-\beta,-\gamma)\). For the second put \(q_i=q(e_i)\). In those H.4 coordinates the four rows of \(L_q(e_i)\) are
\[
\begin{pmatrix}
0&-3q_0&-3q_1\\
q_0&-q_1&-2q_2\\
2q_1&q_2&-q_3\\
3q_2&3q_3&0
\end{pmatrix}.
\tag{J.7}
\]
These are all the solutions in H.5, with its four free parameters equal to \(q_0,q_1,q_2,q_3\). This proves bijectivity, including membership in the whole derivative-curvature space.

For clarity the change-of-frame identities, proved by differentiating the group identity for \(Q\) in I.9–I.12, are
\[
D_{a\circ\operatorname{Ad}_g}(x,y)
=\operatorname{Ad}_{g^{-1}}D_a(gx,gy),\qquad
L_{q\circ g}(x)(y,z)
=\operatorname{Ad}_{g^{-1}}L_q(gx)(gy,gz).
\tag{J.8}
\]
Here the second follows from the first and
\(j(q\circ g,x)=j(q,gx)\circ\operatorname{Ad}_g\).
Alternatively, differentiating the first identity at \(g=\exp(tA)\) gives
\[
D_{\delta_Aa}=-A\mathbin{\cdot}D_a,
\tag{J.9}
\]
where \((A\mathbin{\cdot}D)(x,y)=[A,D(x,y)]-D(Ax,y)-D(x,Ay)\). The equality for \(E,H,F\) is also the H.7 table after the same coordinate change. The differential identity integrates along each group flow by uniqueness of a linear ODE, and connectedness of \(G\) gives the group identity. To justify this last step without a generation theorem, products of basis exponentials contain a neighbourhood of the identity by the inverse function theorem; the subgroup they generate is open, all its cosets are open, and connectedness makes it the whole group. \(\square\)

**Theorem J.3 (complete equations of every real cubic connection).** Let a smooth torsion-free connection be reduced to the cubic group on a four-dimensional manifold. On each connected local reduced frame bundle there are unique smooth functions \(a\) with values in \(\mathfrak g^*\), \(q\) with values in \(V^*\), and a constant \(c\in\mathbb R\), such that its solder form \(\theta\), connection form \(\omega\), curvature and parameters satisfy
\[
\begin{aligned}
d\theta&=-\omega\wedge\theta,\\
d\omega+\tfrac12[\omega,\omega]&=-\tfrac12D_a(\theta\wedge\theta),\\
da(U)&=\delta_{\omega(U)}a-j(q,\theta(U)),\\
dq(U)(y)&=q(\omega(U)y)+\phi_c(a)(\theta(U),y),\\
dc&=0,\qquad \mathcal R=-D_a,\qquad \nabla\mathcal R=L_q.
\end{aligned}
\tag{J.10}
\]
The normalization is \(D_a(\theta\wedge\theta)(U,W)=2D_a(\theta U,\theta W)\). The functions transform by \(a(ug)=a(u)\circ\operatorname{Ad}_g\), \(q(ug)=q(u)\circ g\); \(c\) is invariant.

**Proof.** The form \((\omega,\theta)\) is a coframe on the seven-dimensional reduced bundle: its kernel is horizontal with zero solder value and hence zero, and dimensions agree. Denote its dual fields by \(\xi_A,\xi_x\), for constant \(A\in\mathfrak g\), \(x\in V\). The torsion-free first Bianchi identity and the differentiated Bianchi identity were proved in F.6. Thus \(\mathcal R\in K(\mathfrak g)\) and \(\nabla\mathcal R\in K^1(\mathfrak g)\). J.2 defines unique \(a,q\) by \(\mathcal R=-D_a\) and \(\nabla\mathcal R=L_q\). These are smooth because the inverse maps are fixed linear maps. Tensorial change of frame and (J.8) prove the stated equivariance. In particular
\[
\xi_Aa=\delta_Aa,\qquad (\xi_Aq)(y)=q(Ay).
\tag{J.11}
\]
Horizontal differentiation of \(\mathcal R=-D_a\), followed by (J.6), gives
\(-D_{\xi_xa}=L_q(x)=D_{j(q,x)}\). Injectivity gives \(\xi_xa=-j(q,x)\).

The torsion and curvature form equations, evaluated on the dual frame, give the brackets
\[
[\xi_A,\xi_B]=\xi_{[A,B]},\qquad
[\xi_A,\xi_x]=\xi_{Ax},\qquad
[\xi_x,\xi_y]=\xi_{D_a(x,y)}.
\tag{J.12}
\]
In the last expression the coefficients of the vertical field depend on the point. Acting on a function still means the pointwise linear combination of the fundamental fields; no derivative of those coefficients occurs in that operation.

Set \(T(x,y)=(\xi_xq)(y)\). Apply the last bracket to \(a(B)\). Its left side is \(-T(x,By)+T(y,Bx)\), while its right side is \(a([D_a(x,y),B])\). Consequently
\[
T(x,By)-T(y,Bx)=a([B,D_a(x,y)]).
\tag{J.13}
\]
The equivariance equation of \(Q\), already verified in I.12, gives exactly the same right side:
\[
Q(a)(x,By)-Q(a)(y,Bx)
=dQ_a(\delta_Ba)(x,y)
=a([B,D_a(x,y)]).
\tag{J.14}
\]
J.1 therefore gives \(T=Q(a)+c\Omega\), where \(c=T(e_0,e_3)-Q(a)_{03}\) is a smooth scalar function.

We prove that it is constant, including the vertical directions. From \([\xi_A,\xi_x]=\xi_{Ax}\) and (J.11),
\[
\xi_A T(x,y)=T(Ax,y)+T(x,Ay).
\tag{J.15}
\]
The same equation holds for \(Q(a)\) by (J.14)'s equivariance identity. Invariance of \(\Omega\) gives \((\xi_Ac)\Omega=0\), so \(\xi_Ac=0\).

Apply \([\xi_x,\xi_y]\) to \(q(z)\). Using \(\xi_xa=-j(q,x)\), the left side is
\[
-q(D_a(y,z)x)+q(D_a(x,z)y)
 +(\xi_xc)\Omega(y,z)-(\xi_yc)\Omega(x,z).
\tag{J.16}
\]
The right side is \(q(D_a(x,y)z)\). The first Bianchi identity for \(D_a\) says that the first two terms in (J.16) already equal that right side. Thus, at each point, \(\ell(x)=\xi_xc\) obeys
\[
\ell(x)\Omega(y,z)=\ell(y)\Omega(x,z).
\tag{J.17}
\]
If \(\ell(x)\ne0\), choose a nonzero \(y\in\ker\ell\), possible since \(\dim V=4\). The equation forces \(\Omega(y,z)=0\) for every \(z\), contradicting nondegeneracy. Hence \(\ell=0\). Since all the \(\xi_A,\xi_x\) span the tangent space, \(dc=0\). In a coordinate ball the fundamental theorem of calculus along segments makes \(c\) constant; such balls show local constancy, and connectedness gives constancy on the connected component. Every equation in (J.10) has now been proved, and the constructions of \(a,q,c\) prove uniqueness. \(\square\)

**Lemma J.4 (local determination of a coframe by parameter equations).** Suppose a smooth \(n\)-manifold has a frame \(X_1,\ldots,X_n\) and a smooth parameter map \(z\) into an open set of \(\mathbb R^m\), with
\[
[X_i,X_j]=\sum_k C_{ij}^{k}(z)X_k,\qquad
X_i z=\rho_i(z).
\tag{J.18}
\]
Assume the displayed coefficient functions and parameter vector fields are analytic. Any two such framed manifolds with the same coefficient functions and the same parameter value at specified points are locally isomorphic as framed manifolds with parameters. The isomorphism carrying those specified points is unique as a germ. Each realization has local coordinates in which the frame, its dual coframe and its parameter map are analytic. No rank assumption on \(dz\) or on the family \(\rho_i\) is required.

**Proof.** Let \(\varphi_i^t\) be the smooth local flow of \(X_i\). Choose a small parameter box on which the successive flows exist, and set
\[
\Phi(t_1,\ldots,t_n)=
\varphi_n^{t_n}\circ\cdots\circ\varphi_1^{t_1}(p).
\tag{J.19}
\]
Its derivative at zero sends the standard basis to \(X_1(p),\ldots,X_n(p)\), so the smooth inverse function theorem makes it a local coordinate map. Along a flow of \(X_i\), the value of \(z\) solves \(z'=\rho_i(z)\). ODE uniqueness therefore determines \(z\circ\Phi\) solely from \(z(p)\) and the \(\rho_i\). It is analytic in \(t\) by I.1, even if the originally given functions on the manifold were merely smooth.

We also determine the entire pulled-back coframe. Transport a tangent vector by the differential of \(\varphi_i^s\), and write it as \(v(s)=\sum_k b^k(s)X_k(\varphi_i^s(r))\). In any smooth coordinate system the variational equation is \(v'=DX_i\,v\). Differentiating the displayed expansion and using \([X_i,X_k]=DX_k\,X_i-DX_i\,X_k\) gives
\[
\frac{db^\ell}{ds}
=-\sum_k b^k(s)C_{ik}^{\ell}(z(\varphi_i^s(r))).
\tag{J.20}
\]
For the \(j\)-th column of \(d\Phi\), start with \(X_j\) just after the \(j\)-th flow in (J.19), and push it successively through flows \(j+1,\ldots,n\). Its initial coefficient vector is the \(j\)-th standard basis vector. Thus each column is obtained by finitely many linear equations (J.20) whose coefficients and parameter paths have already been determined. They depend analytically on all \(t_i\) by I.1. Let \(B(t)\) be the resulting matrix. If \(\eta\) is the coframe dual to \(X_i\), then
\[
\Phi^*\eta=B(t)\,dt,\qquad B(0)=I.
\tag{J.21}
\]
The matrix is invertible on a smaller box, and its inverse is analytic by I.1. Hence both frame and coframe are analytic in these coordinates.

For two realizations the parameter ODEs and all initial data for (J.20) agree. Uniqueness gives identical \(z\circ\Phi\) and identical \(B\). The map \(\Phi'\circ\Phi^{-1}\) is consequently an isomorphism preserving every frame field and the parameter map. Any such isomorphism commutes with the local flows, by ODE uniqueness, so it has this prescribed value at every point (J.19). This proves uniqueness as a germ. The same argument supplies analytic coordinate changes wherever they are needed: in an already obtained analytic chart the vector fields are analytic, so its ordered-flow charts are analytic by I.1.

As a check on the transport sign, for \(X_1=\partial_x\), \(X_2=e^x\partial_y\), one has \([X_1,X_2]=X_2\). The ordered-flow coordinates based at the origin are \((x,y)=(t_1,e^{t_1}t_2)\). Their first column has frame coefficients \((1,t_2)\), as (J.20) gives when it transports \(X_1\) along \(X_2\). The minus sign is essential. This example is a direct check; the preceding variational calculation proves the general formula. \(\square\)

**Theorem J.5 (analytic germs and the cubic converse at every parameter).** Every smooth torsion-free real cubic connection is analytic in suitable local coordinates. At a specified reduced frame its germ is determined by \((a,q,c)\), or by \((\mathcal R,\nabla\mathcal R,\nabla^2\mathcal R)\) at that frame. Every triple \((a_0,q_0,c_0)\in\mathfrak g^*\oplus V^*\oplus\mathbb R\) occurs in such an analytic connection. Every local cubic connection is locally equivalent to the Poisson construction of I.10 for \(\phi_{c_0}\), including when the parameter lies in a rank-changing part of that Poisson space.

**Proof.** Apply J.4 on the reduced frame bundle to the seven fields \(\xi_E,\xi_H,\xi_F,\xi_{e_0},\ldots,\xi_{e_3}\). The parameter space is the whole eight-dimensional space with coordinates \(z=(a,q,c)\). Its vector fields in (J.18) are
\[
\begin{aligned}
\rho_A(a,q,c)&=(\delta_Aa,\ q\circ A,\ 0),\\
\rho_x(a,q,c)&=(-j(q,x),\ \phi_c(a)(x,\,\cdot\,),\ 0).
\end{aligned}
\tag{J.22}
\]
These are polynomial, as are the bracket coefficients (J.12). J.4 gives an analytic coframe and a unique frame-preserving local equivalence for identical initial triples.

The vertical distribution is spanned by the three \(\xi_A\). It is involutive by (J.12) and analytic in the coordinates just obtained. The analytic integral-coordinate construction of I.2 gives a local base quotient and an analytic transverse section. On that section let \(e=\theta|_s\), \(A=\omega|_s\). As in I.10, \(e\) is a coframe and the base connection is
\[
e(\nabla_XY)=X(e(Y))+A(X)e(Y).
\tag{J.23}
\]
It is analytic because these matrices and their inverses are analytic. The frame-preserving equivalence maps the vertical distribution to the corresponding vertical distribution and therefore descends to a base diffeomorphism. It preserves (J.23), and hence the connection and the specified reduced frame. One can choose the second transverse section to be the image of the first, so this assertion needs no global quotient construction. Conversely, any local connection-preserving base map carrying the specified frame lifts by its differential to a map preserving \(\theta,\omega\), and J.4 gives uniqueness of its germ. This proves local determination and analyticity.

To prove existence at every initial triple, fix \(c_0\). I.12 proves that \(\phi_{c_0}\) is admissible on all of \(\mathfrak g^*\), so I.7 gives a symplectic realization at \((a_0,q_0)\), with no rank restriction. Use its zero-section point over that value, and apply I.10. On the resulting integral frame manifold, the parameter functions are the restrictions of the realization's \(a,q\), and their derivatives on the dual frame are precisely (J.22): this follows directly from the three linear-coordinate brackets in I.9. Its curvature is \(-D_a\) and its first covariant derivative is \(L_q\), by I.10 and linearity of \(D\). J.2 and J.3 therefore recover those same \(a,q,c_0\) from the constructed connection. The construction is analytic by I.1, I.2 and I.7. J.4 now identifies any other local connection having those initial data with this Poisson construction. At no point was an equal-parameter fibre product or a constant-rank condition on the parameter map used.

Finally, covariant differentiation of \(\nabla\mathcal R=L_q\) gives
\[
(\nabla^2\mathcal R)(x,\,\cdot\,)=L_{T_x},\qquad
T_x(y)=\phi_c(a)(x,y).
\tag{J.24}
\]
This identity can be checked at the given frame by horizontal differentiation: \(L\) is a fixed linear equivariant map, and \(\xi_xq=T_x\). Equivalently it follows from the associated tensor derivative rule in Connections D.1. Thus \(\mathcal R\) determines \(a\), \(\nabla\mathcal R\) determines \(q\), and applying \(L^{-1}\) to the first slot of \(\nabla^2\mathcal R\) determines every \(T_x\). Since \(\Omega(e_0,e_3)=1\),
\[
c=T_{e_0}(e_3)+9\alpha\gamma+\tfrac92\beta^2.
\tag{J.25}
\]
This proves the assertion about curvature jets. A torsion-free connection whose local holonomy is contained in a conjugate of the cubic group is covered as well: the local holonomy reduction proved in G.4, extended to that group, gives the reduced connection just used. Locally this extension is simply the product of a section of the holonomy reduction with \(G\), with its \(\mathfrak g\)-valued connection form as in I.10. \(\square\)

**Proposition J.6 (constant parameter rank and the flat case).** For a cubic connection the map \(u\mapsto(a(u),q(u))\) has constant even rank locally. Rank zero is equivalent to flatness locally. A cubic connection with parallel curvature is flat.

**Proof.** Fix its constant \(c\). In the seven frame directions, the differential of \((a,q)\) has columns equal to the seven Hamiltonian vector fields of the linear coordinates on the Poisson space \(\mathfrak g^*\oplus V^*\) for \(\phi_c\), by (J.22). Its rank is therefore the rank of the Poisson matrix at that parameter. The matrix is skew, and the elementary alternating-form argument in F.1 proves that this rank is even.

Each local Hamiltonian flow preserves that matrix as a bivector. Here is the precise reason: the Jacobi identity gives
\(X_f\{g,h\}=\{X_fg,h\}+\{g,X_fh\}\).
In coordinates this is the vanishing of the Lie derivative of the bivector; differentiating its pullback by the flow therefore gives zero. This differentiation follows componentwise from the chain rule and the variational equation, the same pullback calculation used in A.2. The flow and its inverse have invertible derivatives, so the bivector rank is preserved. Ordered frame flows descend by (J.22) to these Hamiltonian flows. They reach every point in a neighbourhood by (J.19), proving the constant-rank assertion even if the ambient Poisson rank varies near the image.

Rank zero at a frame makes all the linear brackets zero. The brackets \([E,H]=-2E\), \([E,F]=H\), \([H,F]=-2F\) first give \(a=0\). The brackets with \(H\) then give \(q=0\), because \(H\) has the four nonzero weights \(3,1,-1,-3\) on \(V\). The remaining bracket is \(c\Omega\), giving \(c=0\). Every vector field (J.22) vanishes at this triple, so uniqueness of its ODE keeps the triple zero throughout a frame neighbourhood. Thus \(\mathcal R=-D_a=0\) there. Conversely, if the connection is flat, J.2 gives \(a=0\) throughout the reduced neighbourhood; \(da=-j(q,\theta)\) gives \(q=0\) by taking \(H\), and \(dq=\phi_c(0)(\theta,\,\cdot\,)\) gives \(c=0\). Its parameter rank is zero.

If \(\nabla\mathcal R=0\) on a neighbourhood, J.2 gives \(q=0\) there. Thus \(Q(a)+c\Omega=0\) by the horizontal equation for \(dq\). Its \(01\) and \(23\) entries in (J.1) give \(\alpha=\gamma=0\). Its \(12\) entry gives \(c=3\beta^2/2\); its \(03\) entry then gives \(-3\beta^2=0\). Hence \(\beta=c=0\), so the connection is flat. This last algebraic implication also holds over \(\mathbb C\), since a scalar with square zero is zero. \(\square\)

**Lemma J.7 (real irreducibility and complexification).** Let a real Lie algebra act irreducibly on a nonzero finite-dimensional real vector space \(V\). Its complexification \(V_{\mathbb C}\) is either irreducible or is the direct sum of two irreducible conjugate complex submodules \(W\oplus\overline W\). The reducible case occurs exactly when \(V\) has an invariant real operator \(J\) with \(J^2=-I\). For any real representation, the curvature space \(K\) and derivative-curvature space \(K^1\) commute with complexification.

**Proof.** A conjugation-stable complex subspace \(S\subset V_{\mathbb C}\) is the complexification of its real fixed subspace: for \(s\in S\), both \((s+\overline s)/2\) and \((s-\overline s)/(2i)\) are real fixed vectors in \(S\), and they sum to \(s\) after multiplying the second by \(i\). Therefore a nonzero invariant conjugation-stable \(S\) is all of \(V_{\mathbb C}\), by real irreducibility.

Choose a nonzero complex submodule \(W\) of smallest positive dimension; it is irreducible. So is \(\overline W\). Their intersection, a submodule of each, is either zero or both of them. If they agree, the preceding paragraph gives \(W=V_{\mathbb C}\). Otherwise their sum is nonzero and conjugation-stable, so \(V_{\mathbb C}=W\oplus\overline W\). Define \(J\) on this sum by multiplication by \(i\) on \(W\) and by \(-i\) on \(\overline W\). It commutes with conjugation, preserves the real fixed subspace and commutes with the algebra action; its real restriction has square \(-I\).

Conversely, an invariant real \(J\) with \(J^2=-I\) gives the complementary complex projections \((I-iJ)/2\), \((I+iJ)/2\). Their images are its \(+i\) and \(-i\) eigenspaces, conjugate to each other. Both are nonzero: if one vanished, conjugation would make the other vanish as well. The minimal-submodule argument just given also proves each is irreducible, since a nonzero proper submodule of one, together with its conjugate, would be a proper nonzero conjugation-stable submodule.

Finally, the definitions in F.6 express \(K\) as the kernel of the real linear Bianchi map, and \(K^1\) as the kernel of another real linear Bianchi map on \(V^*\otimes K\). Finite tensor spaces and exterior powers complexify coefficientwise in a real basis. For a real linear map \(B\), the equation \(B(u+iv)=0\) is equivalent to \(Bu=Bv=0\); hence \(\ker B_{\mathbb C}=(\ker B)_{\mathbb C}\). Apply this successively to the two maps. No complete-reducibility theorem or spectral theorem is involved. \(\square\)

**Proposition J.8 (the ordinary-prolongation realification test).** Suppose \(\mathfrak h\subset\mathfrak{gl}(V)\) acts real-irreducibly, has an invariant complex structure \(J\), and is spanned by the values of its algebraic curvature tensors. Write \(V_{\mathbb C}=W\oplus\overline W\) for the eigenspaces of \(J\), and let \(\mathfrak k\) be the image of \(\mathfrak h_{\mathbb C}\) on \(W\). If
\[
\mathfrak k^{(1)}=
\{S\in W^*\otimes\mathfrak k:S(x)y=S(y)x\}=0,
\tag{J.26}
\]
then \(J\mathfrak h=\mathfrak h\). In particular \(\mathfrak h\) is the underlying real algebra of its complex action on \(W\), and
\[
\begin{aligned}
K(\mathfrak h)_{\mathbb C}&=K(\mathfrak k)\oplus K(\overline{\mathfrak k}),\\
K^1(\mathfrak h)_{\mathbb C}&=K^1(\mathfrak k)\oplus K^1(\overline{\mathfrak k}).
\end{aligned}
\tag{J.27}
\]
The real fixed spaces in these decompositions identify with the respective complex spaces regarded as real vector spaces. Torsion-free holonomy algebras satisfy the curvature-span hypothesis by G.5.

**Proof.** Since all operators commute with \(J\), restriction embeds \(\mathfrak h_{\mathbb C}\) into \(\mathfrak k\oplus\overline{\mathfrak k}\), with surjective projections. Consider \(R\in K(\mathfrak h_{\mathbb C})\). For \(x,y\in W\), \(z\in\overline W\), the Bianchi identity has separate components
\[
R(x,y)z=0,\qquad R(y,z)x=R(x,z)y.
\tag{J.28}
\]
For fixed \(z\), the map \(x\mapsto R(x,z)|_W\) belongs to \(\mathfrak k^{(1)}\), so it vanishes. The conjugate argument, using \(\overline{\mathfrak k}^{(1)}=0\), kills \(R(x,z)|_{\overline W}\) as well. Faithfulness of the two-block embedding gives \(R(W,\overline W)=0\). Also (J.28) says \(R(W,W)\) acts only on \(W\); similarly \(R(\overline W,\overline W)\) acts only on \(\overline W\).

The real curvature-span hypothesis complexifies by J.7. Thus \(\mathfrak h_{\mathbb C}\) is spanned by curvature values supported in one block or the other. Its projections onto \(\mathfrak k\) and \(\overline{\mathfrak k}\) are surjective, so the span in the first block is all of \(\mathfrak k\oplus0\), and the span in the second is all of \(0\oplus\overline{\mathfrak k}\). Consequently
\[
\mathfrak h_{\mathbb C}=\mathfrak k\oplus\overline{\mathfrak k}.
\tag{J.29}
\]
Conjugation exchanges the blocks. The complex-linear operation taking \((A,B)\) to \((iA,-iB)\) commutes with conjugation and preserves (J.29); on the real fixed space it is exactly multiplication of the corresponding real operator by \(J\). Its square is minus the identity, proving \(J\mathfrak h=\mathfrak h\). Projection of the real fixed space onto \(\mathfrak k\) is a real-linear bijection, with inverse \(A\mapsto(A,\overline A)\); it respects brackets.

The first equality (J.27) now follows from the vanishing mixed components and (J.28). Conversely, any algebraic curvature tensor of \(\mathfrak k\) on \(W\) extends by zero on arguments involving \(\overline W\), taking values in the first block of (J.29); it satisfies every Bianchi triple. The same holds in the conjugate block, proving equality rather than only inclusion.

For the second, let \(S\in K^1(\mathfrak h_{\mathbb C})\). Each \(S_u\) has the two pure components just described. The derivative Bianchi equation for \(u\in\overline W\), \(x,y\in W\) reads
\[
S_u(x,y)+S_x(y,u)+S_y(u,x)=0.
\tag{J.30}
\]
The last two terms vanish by the first decomposition, so \(S_u(x,y)=0\). Interchanging the blocks proves the other mixed derivative vanishes. The remaining pure triples are precisely the derivative Bianchi equations for \(K^1(\mathfrak k)\) and its conjugate. Conversely their zero extensions satisfy all mixed and pure equations. This proves the second equality and, by conjugation, the stated real identifications. \(\square\)

**Exercise J.9 (signs, the actual example and the two prolongations).** Verify the symplectic sign for a rank-two realization; finish the dimension, nonparallelness and nonmetric checks for the I.12 example; and distinguish the ordinary and curvature prolongations of the complex cubic action.

**Solution.** First use the plus-insertion convention of I.3: \(\iota_{X_f}\sigma=df\), \(\{f,g\}=X_fg\). For
\(\sigma=dp\wedge dq+dt\wedge dz\), contraction gives
\[
X_p=-\partial_q,\quad X_q=\partial_p,\quad X_t=-\partial_z,
\qquad \{p,q\}=-1.
\tag{J.31}
\]
Projection to \((p,q,t)\) is therefore a realization of the bracket with \(\{p,q\}=-1\), \(\{p,t\}=\{q,t\}=0\). To realize the bracket with \(\{p,q\}=1\) under the same convention, use
\[
\widetilde\sigma=dq\wedge dp+dz\wedge dt.
\tag{J.32}
\]
Then \(X_p=\partial_q\), \(X_q=-\partial_p\), \(X_t=\partial_z\). All brackets of projected functions follow by the chain rule, so this checks the full Poisson-map assertion, not only three coordinate values.

For the I.12 example, the target has dimension seven, and its explicit \(6\)-by-\(6\) minor has determinant \(36\). Its skew \(7\)-by-\(7\) matrix therefore has rank six on a neighbourhood; rank cannot be seven by F.1. The regular realization I.4 has dimension \(2r+2s=8\), where \(2r=6\), \(s=1\). Its local symplectic leaves have dimension six by those same regular coordinates. The integral frame manifold I.10 has dimension \(\dim\mathfrak g+\dim V=7\), its vertical distribution has dimension three, and its base has dimension four. The all-point cotangent construction I.7 is another valid realization, of dimension fourteen; either construction yields those same frame and base dimensions.

At \(a=(1,0,0)\), \(q=e_1^*\), \(c=0\), one has \(j(q,e_0)=(0,0,3)\) in the \(E,H,F\) dual coordinates. Consequently
\[
(\nabla_{e_0}\mathcal R)(e_2,e_3)=D_{(0,0,3)}(e_2,e_3)=-18F\ne0.
\tag{J.33}
\]
The curvature values at that frame span \(\mathfrak g\) by I.12, so I.11 gives full restricted cubic holonomy. H.1 proves its irreducibility: any group-invariant real subspace is Lie-algebra invariant by differentiation, and the latter representation is irreducible. If a nondegenerate symmetric form were parallel, transport around loops would preserve its value at this frame, by the tensor derivative and transport rules in Connections D.1 and C.2. Differentiating the holonomy action would give a nonzero invariant symmetric bilinear form. H.2 proves there is none on the cubic module. The connection thus preserves no pseudo-Riemannian metric.

Finally let an element of the ordinary complex prolongation be specified by
\(A_i=\alpha_iE+\beta_iH+\gamma_iF\), with \(A_ie_j=A_je_i\). The equations at pairs \(03,02,13,12\), in that order, force the following coefficients to vanish:
\[
\begin{array}{c|l}
03&\alpha_0,\beta_0,\beta_3,\gamma_3\\
02&\gamma_0,\beta_2,\gamma_2\\
13&\alpha_1,\beta_1,\alpha_3\\
12&\gamma_1,\alpha_2.
\end{array}
\tag{J.34}
\]
For example the first equality is \(3\alpha_0e_2-3\beta_0e_3=3\beta_3e_0+3\gamma_3e_1\); the next three follow immediately from the same action formulas after the preceding zero coefficients are removed. The list contains all twelve coefficients. Thus \(\mathfrak g_{\mathbb C}^{(1)}=0\). In contrast, the derivative-curvature space is defined on \(V^*\otimes K\), not on \(V^*\otimes\mathfrak g\). Its complete table (J.7) has four independent arbitrary complex parameters, by the real kernel calculation H.5 and coefficientwise complexification J.7. Hence \(\dim_{\mathbb C}K^1(\mathfrak g_{\mathbb C})=4\). This verifies explicitly both spaces used in the realification test. \(\square\)

### Free construction sources and scope of this part

The mathematical construction lead is Quo-Shin Chi, Sergey A. Merkulov and Lorenz J. Schwachhöfer, *On the Existence of Infinite Series of Exotic Holonomies*, the freely readable [author preprint dated 9 April 1996](https://wwwold.mathematik.tu-dortmund.de/~lschwach/papers/Berger/InfExoticHol.pdf), native PDF pages 12–13, Theorem 3.10 and its proof, and the cubic calculation requested on native page 17. J.1 proves that calculation; J.3 supplies all differentiated equations with the conventions of Part I; J.4–J.5 prove the local equivalence and analytic assertions, including singular parameter values. The remaining linear tests and exercises are proved directly from the complete programme arguments in F–I. The exact free Bryant and Etingof source versions credited in H and the Crainic–Mărcuț and Teschl versions credited in I remain the construction sources of those earlier proofs.

These are new proofs and exposition; no source prose, images or source files are reproduced. This part completes the real cubic equations, local determination, the representation tests and the associated exercises. Part K treats the Spencer and tensor-product calculations; Parts L and M treat the infinite families and their full structure-equation hypotheses.

## K. Spencer algebra and tensor-product curvature

This part uses the exact free Merkulov–Schwachhöfer preprint cited below, Section 3.1 and the tensor-product examples in Section 5. Its cohomological classification results are not prerequisites here. We prove the needed complex and its contraction directly, then obtain the entire tensor-product curvature space by coordinate elimination. The real and complex calculations have the same coefficients. In the tensor-product theorems both factor dimensions are at least three; no assertion about the exceptional two-dimensional factor is implicit in them.

Write \(\mathbb F=\mathbb R\) or \(\mathbb C\). All vector spaces in K.1–K.6 are finite-dimensional over \(\mathbb F\). Exterior and symmetric tensors mean alternating and symmetric multilinear maps, with the elementary tensor operations proved in Principal bundles C.2 and DG-CHAR-17 D.0. Complex scalar versions follow by the identical basis constructions. For \(\mathfrak g\subset\operatorname{End}(V)\), put \(\mathfrak g^{(-1)}=V\), \(\mathfrak g^{(0)}=\mathfrak g\), and
\[
\mathfrak g^{(r)}=
(\mathfrak g^{(r-1)}\otimes V^*)\cap
(V\otimes\operatorname{Sym}^{r+1}V^*),\qquad r\geq1.
\tag{K.1}
\]
The intersection is taken in the tensor space with one output in \(V\) and \(r+1\) covariant arguments. Thus every partial evaluation in \(r\) of those arguments must be in \(\mathfrak g\). Define
\[
C^{p,q}=\mathfrak g^{(p-1)}\otimes\Lambda^qV^*,\qquad p,q\geq0,
\tag{K.2}
\]
and set spaces with a negative index to zero. The first \(p\) covariant slots are symmetric and the last \(q\) alternating. On \(p\geq1\) set
\[
\begin{aligned}
(\partial T)(u_1,\ldots,u_{p-1};x_0,\ldots,x_q)
={}&\sum_{i=0}^q(-1)^i
T(u_1,\ldots,u_{p-1},x_i;
x_0,\ldots,\widehat{x_i},\ldots,x_q).
\end{aligned}
\tag{K.3}
\]
For \(p=0\), set \(\partial=0\).

**Proposition K.1 (the Spencer complex and its curvature term).** The map (K.3) takes \(C^{p,q}\) to \(C^{p-1,q+1}\), satisfies \(\partial^2=0\), and is equivariant under every change of basis preserving \(\mathfrak g\). Let
\[
H^{p,q}(\mathfrak g)=
\frac{\ker(\partial:C^{p,q}\longrightarrow C^{p-1,q+1})}
{\operatorname{im}(\partial:C^{p+1,q-1}\longrightarrow C^{p,q})}.
\tag{K.4}
\]
Then \(H^{p,1}=0\) for \(p\geq1\), and
\[
H^{1,2}(\mathfrak g)=
K(\mathfrak g)/\partial(\mathfrak g^{(1)}\otimes V^*).
\tag{K.5}
\]
If \(\mathfrak g^{(1)}=0\), this last space is \(K(\mathfrak g)\). The space \(\mathfrak g^{(1)}\) is the kernel of the torsion-change map of F.2.

**Proof.** Each summand of (K.3), with all but one of the remaining symmetric slots fixed, has the partial-evaluation property in (K.1). It is therefore in the asserted smaller prolongation. The displayed sum is alternating in the \(x_i\): transposing adjacent variables either exchanges their two omission terms with opposite signs, or changes the sign of the alternating last slots in every other term. All constructions are contractions and permutations of tensor slots, so they commute with a simultaneous change of basis.

In \(\partial^2T\), a term is indexed by two distinct \(x_i,x_j\) moved to the symmetric slots. Moving \(x_i\) first and \(x_j\) second has the opposite omission sign to moving them in the other order. The symmetric slots give equal evaluations. These terms cancel in pairs, proving \(\partial^2=0\). The case \(p\leq1\) follows also from the stipulated zero targets.

An element of \(C^{p,1}\) has \(p\) symmetric slots and one distinguished last slot. Its differential vanishes precisely when the last slot can be interchanged with the last symmetric slot. The symmetric-slot permutations then interchange it with any slot. It is a fully symmetric \((p+1)\)-tensor with the partial-evaluation property of \(\mathfrak g^{(p)}\). Conversely every such tensor is a cycle. Its differential from \(C^{p+1,0}=\mathfrak g^{(p)}\) is exactly that tensor, viewed with one distinguished slot. This proves \(H^{p,1}=0\) for \(p\geq1\). The restriction matters: \(H^{0,1}\) is in general \(\operatorname{End}(V)/\mathfrak g\).

An element of \(C^{1,2}\) is a skew map \(R(x,y)\in\mathfrak g\), with the single symmetric slot used as its vector argument. Formula (K.3) is
\[
(\partial R)(x,y,z)=R(y,z)x-R(x,z)y+R(x,y)z.
\tag{K.6}
\]
Its kernel is exactly the curvature space of F.6, which proves (K.5). Finally \(\mathfrak g^{(1)}\) consists of maps \(S:V\to\mathfrak g\) with \(S(x)y=S(y)x\), the kernel of F.2's torsion-change map. With our placement of the distinguished slot, (K.3) on \(\mathfrak g\otimes V^*\) is the negative of that map; its kernel and image are unchanged. \(\square\)

**Lemma K.2 (polynomial contraction, including an embedded coefficient space).** For \(\mathfrak g=\operatorname{End}(V)\), one has \(H^{p,q}(\mathfrak g)=0\) whenever \(p+q>0\); \(H^{0,0}=V\). More generally let \(E\subset F\). On
\[
\operatorname{Sym}^pE\otimes\Lambda^q F
\tag{K.7}
\]
take the differential that differentiates a symmetric factor and wedges that factor, using \(E\subset F\), into the exterior part. Its cohomology vanishes at \(p>0\); at \(p=0\) it is canonically \(\Lambda^q(F/E)\). These assertions remain true after tensoring with an arbitrary finite-dimensional coefficient space.

**Proof.** For the full endomorphism algebra, (K.1) is \(V\otimes\operatorname{Sym}^{r+1}V^*\). Choose coordinates \(z_i\) on \(V\). Represent a symmetric \(p\)-tensor \(T\) by the polynomial \(T(z,\ldots,z)/p!\). Then (K.3) becomes the ordinary polynomial exterior derivative \(d=\sum_i dz_i\wedge\partial_{z_i}\). The factorial ensures that insertion into a symmetric slot agrees with differentiation with coefficient one in this correspondence.

Let \(\mathcal E=\sum_i z_i\partial_{z_i}\), and let \(h=\iota_{\mathcal E}\). On a polynomial differential form with homogeneous polynomial degree \(p\) and exterior degree \(q\),
\[
dh+hd=(p+q)I.
\tag{K.8}
\]
Here is an algebraic verification. The insertion and exterior derivative product rules make their anticommutator a degree-zero derivation, as checked in A.2. On a coordinate function it sends \(z_i\) to \(z_i\), and on \(dz_i\) it sends \(dz_i\) to \(dz_i\). Repeated use of that product rule on \(z_1^{a_1}\cdots z_d^{a_d}dz_{i_1}\wedge\cdots\wedge dz_{i_q}\) therefore multiplies it by \(\sum a_i+q=p+q\). These monomials span the space, proving (K.8). A cycle of positive total degree is consequently the differential of \(hT/(p+q)\). Degree zero consists just of constant vectors, proving the first statement, including zero-dimensional \(V\).

For (K.7), choose a complement \(F=E\oplus T\), whose existence is elementary basis extension in Local tools 0.2. Write exterior tensors uniquely as sums in
\[
\operatorname{Sym}^p E\otimes\Lambda^a E\otimes\Lambda^b T,
\qquad a+b=q.
\tag{K.9}
\]
Using basis symbols \(e_i\) for the symmetric factors, the differential is \(d=\sum_i(e_i\wedge\,\cdot\,)\partial_{e_i}\). Contraction is \(h=\sum_i e_i\,\iota_{e_i^*}\), where \(e_i^*\) is extended to vanish on \(T\). The same monomial calculation gives \(dh+hd=(p+a)I\) on (K.9); the \(T\) factors are unchanged. All summands with \(p+a>0\) are exact. The remaining summands have \(p=a=0\) and consist of \(\Lambda^qT\). Canonically they are the quotient of \(\Lambda^q F\) by the image of \(E\otimes\Lambda^{q-1}F\), namely \(\Lambda^q(F/E)\). A basis extending a basis of \(E\) proves this quotient description directly: exactly the exterior basis monomials containing an \(E\) basis vector are removed. It also proves independence from the complement. Extra coefficient factors do not affect the differential or this calculation. \(\square\)

Let \(\dim U=m\geq3\), \(\dim W=n\geq3\), and \(V=U\otimes W\). Define the represented algebra
\[
\mathfrak a=\{A\otimes I_W+I_U\otimes B:A\in\operatorname{End}(U),\ B\in\operatorname{End}(W)\}.
\tag{K.10}
\]
Its kernel as a map from the two endomorphism algebras is \(\{(tI_U,-tI_W):t\in\mathbb F\}\). Indeed, off-diagonal coefficients in a tensor-product basis first force both operators to be diagonal, and their diagonal coefficients obey \(A_i^i+B_a^a=0\) for every \(i,a\), so each is a scalar with opposite value. In particular \(\dim\mathfrak a=m^2+n^2-1\).

For \(Q\in V^*\otimes V^*\), define \(R_Q\) on decomposable arguments by
\[
\begin{aligned}
R_Q(u\otimes a,v\otimes b)(w\otimes c)
={}&u\otimes c\ Q(v\otimes b,w\otimes a)
-v\otimes c\ Q(u\otimes a,w\otimes b)\\
&+w\otimes a\ Q(v\otimes b,u\otimes c)
-w\otimes b\ Q(u\otimes a,v\otimes c).
\end{aligned}
\tag{K.11}
\]
This is separately multilinear in the six factor vectors, so it extends uniquely to a trilinear expression on \(V\), by the defining tensor-product relations.

**Theorem K.3 (every general-linear tensor-product curvature tensor).** Formula (K.11) defines an equivariant linear isomorphism
\[
V^*\otimes V^*\longrightarrow K(\mathfrak a),\qquad Q\longmapsto R_Q.
\tag{K.12}
\]
In particular it describes the entire curvature space, over either field, for every \(m,n\geq3\).

**Proof.** Formula (K.11) is skew in the first two \(V\) arguments. For fixed \(u,a,v,b\), its first two terms are an endomorphism of \(U\) tensored with \(I_W\), and its last two an endomorphism of \(W\) tensored with \(I_U\). Thus its values lie in \(\mathfrak a\). In the cyclic sum on three decomposable arguments, each of the twelve terms cancels one other term with the same output tensor and the same ordered inputs of \(Q\), but opposite sign. For example \(u\otimes c\,Q(v\otimes b,w\otimes a)\) cancels the last term of \(R_Q(v\otimes b,w\otimes c)(u\otimes a)\). The other cancellations are obtained by cyclically permuting this example and by doing the same for the second term. Multilinearity proves the first Bianchi identity on all arguments. Simultaneous basis changes commute with the displayed tensor contractions, proving equivariance.

We prove surjectivity explicitly. Choose bases \(u_i\), \(w_a\), and abbreviate \(u_i\otimes w_a\) to \(v_{ia}\). Write an arbitrary \(R\in K(\mathfrak a)\) as
\[
R(v_{ia},v_{jb})(v_{kc})
=\sum_l A_{ia,jb;k}^{l}v_{lc}
 +\sum_d B_{ia,jb;c}^{d}v_{kd}.
\tag{K.13}
\]
Choose a linear right inverse to the surjection in (K.10) by choosing bases and a complement to its kernel. This initially supplies skew coefficient families \(A,B\). The only freedom for each pair \(ia,jb\) is adding \(tI_U\) to \(A\) and subtracting \(tI_W\) from \(B\).

There is a unique choice for which the image of \(A_{ia,jb}\) lies in \(\operatorname{span}(u_i,u_j)\) and that of \(B_{ia,jb}\) lies in \(\operatorname{span}(w_a,w_b)\). To see existence, the coefficient of \(v_{ld}\) in the Bianchi equation is
\[
\begin{aligned}
0={}&A_{ia,jb;k}^{l}\delta_c^d+B_{ia,jb;c}^{d}\delta_k^l
 +A_{jb,kc;i}^{l}\delta_a^d+B_{jb,kc;a}^{d}\delta_i^l\\
&+A_{kc,ia;j}^{l}\delta_b^d+B_{kc,ia;b}^{d}\delta_j^l.
\end{aligned}
\tag{K.14}
\]
Choose \(c\notin\{a,b\}\), set \(d=c\), and take \(l\notin\{i,j\}\). Then
\(A_{ia,jb;k}^{l}=-B_{ia,jb;c}^{c}\delta_k^l\) for every \(k\). Thus all rows of \(A\) outside \(i,j\) are a common scalar \(\mu\) times the corresponding identity rows. Such an outside row exists since \(m\geq3\), and the equation also makes \(\mu\) independent of the choice of \(c\). Interchanging the two factors in this argument gives all rows of \(B\) outside \(a,b\) equal to \(-\mu\) times the identity rows. More explicitly, choose \(k\notin\{i,j\}\), \(l=k\), \(d\notin\{a,b\}\) in (K.14): it gives \(B_{ia,jb;c}^{d}=-A_{ia,jb;k}^{k}\delta_c^d=-\mu\delta_c^d\). Replace \(A\) by \(A-\mu I_U\) and \(B\) by \(B+\mu I_W\). This gives the asserted image restrictions, even when \(i=j\) or \(a=b\). Uniqueness follows because a nonzero scalar identity cannot have image in a subspace spanned by at most two of the basis vectors. The normalized families remain skew.

For any indices \(j,b,k,a\), choose \(i\notin\{j,k\}\) and \(c\notin\{a,b\}\). The coefficient \(v_{ic}\) in (K.14) reads
\[
A_{ia,jb;k}^{i}=-B_{jb,kc;a}^{c}.
\tag{K.15}
\]
The left side is independent of \(c\), and the right side independent of \(i\). Since at least one such \(i\) and \(c\) always exist, their common value is independent of both choices. Define it to be \(Q_{jb,ka}\).

We now recover every coefficient, including repeated indices. If \(i\ne j\), choose only \(c\notin\{a,b\}\), and take the coefficient \(v_{ic}\) in the Bianchi equation for \((ia,jb,kc)\). The possible additional term \(B_{ia,jb;c}^{c}\delta_k^i\) is zero by the normalization. Thus the result is still (K.15), for every \(k\), including \(k=i\). By the definition just made, its right side is \(Q_{jb,ka}\). Skewness in the first pair similarly gives \(A_{ia,jb;k}^{j}=-Q_{ia,kb}\). All other rows are zero. If \(i=j\), that same coefficient equation has two contributions from the other \(B\) operators, and gives
\[
A_{ia,ib;k}^{i}=-B_{ib,kc;a}^{c}-B_{kc,ia;b}^{c}
=Q_{ib,ka}-Q_{ia,kb}.
\tag{K.16}
\]
Consequently, in all cases,
\[
A_{ia,jb;k}^{l}=\delta_i^l Q_{jb,ka}-\delta_j^l Q_{ia,kb}.
\tag{K.17}
\]

Choose \(l\notin\{i,j\}\) and put \(k=l\) in (K.14). If \(a\ne b\), its coefficient with \(d=a\) gives \(B_{ia,jb;c}^{a}=-A_{jb,lc;i}^{l}=Q_{jb,ic}\); the term from \(A_{ia,jb;l}^{l}\) is zero by normalization. Skewness gives the row with \(d=b\). If \(a=b\), both remaining \(A\) terms occur, giving their difference just as in (K.16). Thus
\[
B_{ia,jb;c}^{d}=\delta_a^d Q_{jb,ic}-\delta_b^d Q_{ia,jc}.
\tag{K.18}
\]
Equations (K.17)–(K.18) are precisely (K.11), proving surjectivity without a cohomology or representation-classification theorem. The normalized coefficients of the zero curvature tensor are zero. Equation (K.15) therefore recovers \(Q=0\) from \(R_Q=0\), proving injectivity. \(\square\)

**Proposition K.4 (Ricci recovery and dimension).** Define the Ricci contraction by
\(\operatorname{Ric}_Q(y,z)=\operatorname{tr}(x\mapsto R_Q(x,y)z)\).
For a bilinear form \(T\) on \(U\otimes W\), let \(s_U\) interchange its two \(U\) indices and \(s_W\) its two \(W\) indices, leaving the other indices in place. Put \(s=m+n\), and
\[
\Pi_{\epsilon,\eta}=\tfrac14(I+\epsilon s_U)(I+\eta s_W),
\qquad \epsilon,\eta\in\{1,-1\}.
\tag{K.19}
\]
Then
\[
\operatorname{Ric}_Q=(sI-s_U-s_W)Q,\qquad
Q=\sum_{\epsilon,\eta=\pm1}
\frac{\Pi_{\epsilon,\eta}\operatorname{Ric}_Q}{s-\epsilon-\eta},
\qquad \dim K(\mathfrak a)=m^2n^2.
\tag{K.20}
\]

**Proof.** Trace (K.13) using (K.17)–(K.18): sum the coefficient with output \(v_{ia}\) over all \(i,a\), with inputs \(v_{ia},v_{jb},v_{kc}\). Its four terms give, respectively,
\[
mQ_{jb,kc},\quad -Q_{jc,kb},\quad nQ_{jb,kc},\quad -Q_{kb,jc}.
\tag{K.21}
\]
These are the asserted contraction formula. The index exchanges commute, square to the identity, and act on different tensor factors. Direct multiplication proves that the four operators (K.19) sum to \(I\), are idempotent, have pairwise zero products, and satisfy \(s_U\Pi_{\epsilon,\eta}=\epsilon\Pi_{\epsilon,\eta}\), \(s_W\Pi_{\epsilon,\eta}=\eta\Pi_{\epsilon,\eta}\). On each image the contraction therefore multiplies by \(s-\epsilon-\eta\). The possible denominators are \(s-2,s,s+2\), all nonzero since \(s\geq6\). This proves the inverse. Finally K.3 identifies the curvature space with the bilinear forms on an \(mn\)-dimensional space, of dimension \((mn)^2\). \(\square\)

Let \(h\) be a nondegenerate bilinear form on \(W\), with
\(h(b,a)=\epsilon h(a,b)\), where \(\epsilon=1\) in the symmetric case and \(\epsilon=-1\) in the alternating case. Write
\[
\mathfrak b=\operatorname{End}(U)\otimes I_W
 +I_U\otimes\mathfrak{aut}(h),\qquad
\mathfrak{aut}(h)=\{B:h(Ba,b)+h(a,Bb)=0\}.
\tag{K.22}
\]
In the symmetric case assume \(n\geq3\); in the alternating case \(n\geq4\) and even. The latter follows also from the alternating-form basis proof in F.1. Always \(m\geq3\).

**Theorem K.5 (the complete orthogonal and symplectic restrictions).** Every \(R\in K(\mathfrak b)\) is uniquely \(R_Q\) with
\[
Q(u\otimes a,v\otimes b)=P(u,v)h(a,b),\qquad
P(v,u)=\epsilon P(u,v).
\tag{K.23}
\]
Conversely every such \(P\) gives an element of \(K(\mathfrak b)\). Thus
\[
K(\mathfrak b)\cong
\begin{cases}
\operatorname{Sym}^2U^*,&\epsilon=1,\\
\Lambda^2U^*,&\epsilon=-1.
\end{cases}
\tag{K.24}
\]
The real symmetric statement includes every nondegenerate signature.

**Proof.** By K.3, write \(R=R_Q\). For decomposable first arguments \(u\otimes a,v\otimes b\), its \(W\)-factor operator from (K.11) is
\[
B_{ua,vb}(c)=a\,Q(v\otimes b,u\otimes c)
 -b\,Q(u\otimes a,v\otimes c).
\tag{K.25}
\]
Its image lies in \(\operatorname{span}(a,b)\). Because \(R\) takes values in \(\mathfrak b\), and decompositions in (K.10) differ only by opposite scalars, there is a scalar \(\lambda\) for which
\[
h(Bx,y)+h(x,By)=\lambda h(x,y).
\tag{K.26}
\]
In fact \(\lambda=2\operatorname{tr}(B)/n\): write (K.26) as \(B^{\mathsf T}H+HB=\lambda H\), multiply by \(H^{-1}\), and take the trace. The equality \(\operatorname{tr}(XY)=\operatorname{tr}(YX)\) follows by interchanging the two finite summed indices.

We first show \(\lambda=0\). If the plane \(L=\operatorname{span}(a,b)\) is nondegenerate for \(h\), then \(W=L\oplus L^\perp\) and the restriction to \(L^\perp\) is nondegenerate. Indeed solve for the \(L\) component using the invertible restriction on \(L\); a vector in the radical of the complement would then be orthogonal to all of \(W\). The complement has positive dimension under the stated bounds. For \(x,y\in L^\perp\), both terms on the left of (K.26) vanish because \(Bx,By\in L\). Nondegeneracy of the complement forces \(\lambda=0\).

Such pairs \((a,b)\) suffice to determine the polynomial \(\lambda\) for all pairs. There exists at least one nondegenerate plane: for an alternating form choose a pair with nonzero pairing; for a symmetric form polarization gives a vector with nonzero square, and its nondegenerate complement gives a second such vector. This argument works over \(\mathbb C\) without choosing square roots. Given any pair, interpolate linearly to that fixed nondegenerate pair. The determinant of the restricted two-by-two matrix is a polynomial in the interpolation parameter, nonzero at its final value; a nonzero one-variable polynomial has only finitely many roots, by repeated division by a linear factor. At all other parameters \(\lambda=0\). Since \(\lambda=2\operatorname{tr}(B)/n\) is also a polynomial, it vanishes identically along the interpolation, in particular at its initial pair. This argument works over either infinite field. Thus every operator (K.25) actually belongs to \(\mathfrak{aut}(h)\).

Fix \(u\in U\), and define \(T(a,c)=Q(u\otimes a,u\otimes c)\). Identify covectors with vectors by the invertible map \(a\mapsto h(a,\,\cdot\,)\), writing \(T(a,\,\cdot\,)=h(Ma,\,\cdot\,)\). The assertion that (K.25) for the two arguments with this same \(u\) preserves \(h\) becomes
\[
\begin{cases}
(Mb)\mathbin{\odot}a-(Ma)\mathbin{\odot}b=0,&\epsilon=1,\\
(Mb)\wedge a-(Ma)\wedge b=0,&\epsilon=-1.
\end{cases}
\tag{K.27}
\]
The symmetric product here can be taken without the factor \(1/2\); its normalization does not change the equation. To verify (K.27), write (K.26) with \(\lambda=0\), substitute (K.25), and replace each occurrence of \(h(c,a)\) by \(\epsilon h(a,c)\). Its four terms are exactly the two indicated symmetric or alternating products, after the invertible covector identification.

For independent \(a,b\), contract one tensor slot with any linear functional vanishing on both. Either equation gives \(f(Mb)a-f(Ma)b=0\). Independence implies both coefficients vanish; hence \(Ma,Mb\in\operatorname{span}(a,b)\). Varying \(b\), in a space of dimension at least three, gives \(Ma\in\operatorname{span}(a)\) for every \(a\). Such a linear map is scalar: its values on basis vectors are scalar multiples of those vectors, and its value on each sum of two distinct basis vectors makes those scalars equal. Thus \(M=tI\). In the symmetric case this satisfies (K.27); in the alternating case the second equation is \(-2t\,a\wedge b=0\), giving \(t=0\). We have proved
\[
Q(u\otimes a,u\otimes c)=
\begin{cases}
t(u)h(a,c),&\epsilon=1,\\
0,&\epsilon=-1.
\end{cases}
\tag{K.28}
\]

In the symmetric case take the same \(W\)-vector \(a\) in the first two arguments of (K.25). That operator is \(a\otimes\ell\), with
\(\ell(c)=Q(v\otimes a,u\otimes c)-Q(u\otimes a,v\otimes c)\).
Preservation of the symmetric form says \(h(a,\,\cdot\,)\odot\ell=0\). For \(a\ne0\), a nonzero covector \(\alpha=h(a,\,\cdot\,)\) cannot have zero symmetric product with a nonzero \(\ell\): evaluate on a vector where \(\alpha\ne0\) twice to obtain \(\ell=0\) there, and then on that vector and an arbitrary one to obtain \(\ell=0\) everywhere. Thus \(Q\) is symmetric in its \(U\) indices. Polarizing (K.28) in \(u\) now proves \(Q=P\otimes h\) with symmetric \(P\). Explicitly choose \(a_0,c_0\) with \(h(a_0,c_0)\ne0\), define \(P(u,v)=Q(u\otimes a_0,v\otimes c_0)/h(a_0,c_0)\), and use the expansion at \(u+v\) to prove equality for every \(a,c\).

In the alternating case, polarization of the zero in (K.28) says \(Q\) is alternating in the \(U\) indices. Fix \(u,v\), and write \(T(a,c)=Q(u\otimes a,v\otimes c)\). With the same \(a\) in (K.25), its operator is \(-2a\otimes T(a,\,\cdot\,)\). Preservation of \(h\) says \(h(a,\,\cdot\,)\wedge T(a,\,\cdot\,)=0\). Two covectors have zero exterior product precisely when they are dependent: choose a vector where the first is nonzero and evaluate their wedge on it and an arbitrary vector. Hence \(T(a,\,\cdot\,)\) is proportional to \(h(a,\,\cdot\,)\). The same basis-and-sums argument for the corresponding linear operator makes the proportionality scalar independent of \(a\). Thus \(Q=P\otimes h\), and its already established \(U\)-alternation makes \(P\) alternating.

Conversely substitution of (K.23) into (K.11) gives the factor operators
\[
\begin{aligned}
A_{ua,vb}&=h(a,b)\bigl(\epsilon u\otimes P(v,\,\cdot\,)-v\otimes P(u,\,\cdot\,)\bigr),\\
B_{ua,vb}&=P(u,v)\bigl(\epsilon a\otimes h(b,\,\cdot\,)-b\otimes h(a,\,\cdot\,)\bigr).
\end{aligned}
\tag{K.29}
\]
Expanding \(h(Bx,y)+h(x,By)\) gives four terms cancelling in pairs, using \(\epsilon^2=1\). Thus \(B\in\mathfrak{aut}(h)\), proving membership in \(K(\mathfrak b)\). Uniqueness follows from K.3 and nonzero \(h\). \(\square\)

**Theorem K.6 (the derivative-curvature space vanishes).** For either algebra in K.5, \(K^1(\mathfrak b)=0\). The same holds for every Lie subalgebra of \(\mathfrak b\). Every torsion-free connection reduced to a subgroup of either tensor-product group consequently has parallel curvature.

**Proof.** Let \(S\in V^*\otimes K(\mathfrak b)\) satisfy the derivative Bianchi identity. K.5 gives a unique linear family \(P_x\), symmetric or alternating as specified there, such that \(S_x=R_{P_x\otimes h}\). The two factor operators in (K.29) have trace zero: the trace of a rank-one map \(u\otimes\lambda\) is \(\lambda(u)\), and \(P(v,u)=\epsilon P(u,v)\), \(h(b,a)=\epsilon h(a,b)\) make both traces vanish. Consequently the derivative Bianchi identity splits into zero in each factor. Indeed a pair of factor operators acting as zero on the tensor product must be opposite scalars by (K.10); their trace zero makes those scalars zero over \(\mathbb R\) or \(\mathbb C\).

Choose independent \(u,v,w\in U\). The coefficient in the \(v\) direction of the \(U\)-factor in the derivative Bianchi identity for \(u\otimes a,v\otimes b,w\otimes c\), evaluated on an arbitrary last \(U\)-argument, is
\[
\epsilon h(b,c)P_{u\otimes a}(w,\,\cdot\,)
-h(a,b)P_{w\otimes c}(u,\,\cdot\,)=0.
\tag{K.30}
\]
For completeness the three \(U\)-operators before taking that coefficient are (K.29)'s first line for the pairs \((v,b;w,c)\) with \(P_{u\otimes a}\), \((w,c;u,a)\) with \(P_{v\otimes b}\), and \((u,a;v,b)\) with \(P_{w\otimes c}\). Their respective \(v\) coefficients are the first term, zero, and the second term of (K.30).

For nonzero \(a\), choose nonzero \(b\in\ker h(a,\,\cdot\,)\), possible since \(n\geq2\); nondegeneracy supplies \(c\) with \(h(b,c)\ne0\). Equation (K.30) gives \(P_{u\otimes a}(w,\,\cdot\,)=0\) for all \(w\) independent of \(u\). A third independent vector \(v\) exists since \(m\geq3\). This also kills the value at \(w=u\): take \(w_0\) independent of \(u\); both \(w_0\) and \(w_0+u\) are independent of \(u\), and subtract their zero values. The assertions with \(u=0\) or \(a=0\) follow by linearity. Therefore \(P_{u\otimes a}=0\) for all decomposable vectors, which span \(V\), so \(S=0\).

For a subalgebra \(\mathfrak c\subset\mathfrak b\), the inclusions of value spaces give \(K(\mathfrak c)\subset K(\mathfrak b)\) and \(K^1(\mathfrak c)\subset K^1(\mathfrak b)\), directly from their Bianchi definitions. Finally F.6 proves that the covariant derivative of the curvature of a torsion-free reduced connection takes values in this derivative-curvature space. It must therefore vanish. In the terminology that a locally symmetric affine connection has parallel curvature, these are locally symmetric cases; no classification of symmetric spaces is needed. \(\square\)

**Lemma K.7 (first jets of a line bundle).** Let \(L\) be a smooth real or complex line bundle on a smooth manifold, or a holomorphic line bundle on a complex manifold. Its first-jet bundle has a canonical exact sequence
\[
0\longrightarrow T^*X\otimes L\longrightarrow J^1L
\xrightarrow{\operatorname{ev}}L\longrightarrow0.
\tag{K.31}
\]
In the holomorphic case use the holomorphic cotangent bundle in this formula. The definition and sequence require no connection.

**Proof.** At a point, declare two local sections equivalent if their values and first derivatives in a local line frame agree. If \(e'=ge\) is another frame, the scalar coefficient changes by \(f'=g^{-1}f\), so
\[
(f,df)\longmapsto
(g^{-1}f,\ g^{-1}df-g^{-2}f\,dg).
\tag{K.32}
\]
Together with the ordinary coordinate-change rule for covectors, this is an invertible fibrewise linear change of the pair. Product and chain rules show that successive changes compose, so equivalence of jets is independent of frame and coordinates, and these charts define a vector bundle. Every prescribed pair at a point is represented by an affine-linear coefficient function in a coordinate neighbourhood. In the holomorphic case that coefficient function is holomorphic.

Here holomorphic charts and coefficients can be expressed by convergent complex power series. Termwise differentiation, multiplication, the reciprocal of a nonzero coefficient and composition have the same absolute-convergence proofs as I.1, with complex coefficients; completeness follows by separating their real and imaginary parts. Thus (K.32) and its inverse are holomorphic in that case. No integrability theorem for an almost-complex structure is being used: the complex manifold and bundle are given.

Evaluation sends the jet to its value; it is surjective by constant local coefficient functions. When the value is zero, (K.32)'s derivative term is just \(g^{-1}df\). Those pairs therefore identify canonically with \(T^*X\otimes L\). This identifies the kernel and proves exactness in every fibre and local bundle chart. The inclusion of that kernel and the evaluation map are intrinsic, even though a splitting obtained from a frame is not. \(\square\)

**Proposition K.8 (the product first-jet sequence and its dual).** On \(X=X_1\times X_2\), let \(L=\pi_1^*L_1\otimes\pi_2^*L_2\), and abbreviate
\[
A=\pi_1^*(J^1L_1)\otimes\pi_2^*L_2,\qquad
B=\pi_1^*L_1\otimes\pi_2^*(J^1L_2).
\tag{K.33}
\]
There are canonical exact sequences
\[
\begin{aligned}
0&\longrightarrow J^1L\longrightarrow A\oplus B
\xrightarrow{\operatorname{ev}_1-\operatorname{ev}_2}L\longrightarrow0,\\
0&\longrightarrow L^*\longrightarrow A^*\oplus B^*
\longrightarrow(J^1L)^*\longrightarrow0.
\end{aligned}
\tag{K.34}
\]
They hold for smooth bundles and for holomorphic bundles, and are obtained without choosing connections.

**Proof.** In product coordinates and local factor frames, a first jet of \(L\) is a triple \((s,\eta_1,\eta_2)\), with derivative components in the two cotangent factors. Define its image to be
\[
(s,\eta_1,\eta_2)\longmapsto
\bigl((s,\eta_1),(s,\eta_2)\bigr).
\tag{K.35}
\]
A change of factor frames multiplies their product frame by \(g_1(x_1)g_2(x_2)\). In (K.32), differentiating this product in the first direction differentiates only \(g_1\), and differentiating in the second direction only \(g_2\). Hence the two components in (K.35) transform exactly as the two bundles (K.33). Coordinate changes in the factors also preserve their separate cotangent parts. Thus the map is globally defined and is smooth or holomorphic, as appropriate.

The value-difference map on \(A\oplus B\) is surjective locally, by the pair \(((s,0),(0,0))\). Its kernel consists exactly of pairs with a common value and arbitrary two derivatives, precisely the image of the injective map (K.35). These local descriptions prove the first sequence. Fibrewise duality gives the second: its first map is
\(\lambda\mapsto(\lambda\circ\operatorname{ev}_1,-\lambda\circ\operatorname{ev}_2)\), and its second map restricts functionals to (K.35)'s image. Restriction is surjective, because a linear functional on a subspace extends after choosing a complement; a basis in these local charts makes those extensions smooth or holomorphic. A functional vanishes on the kernel of the value-difference map exactly when it factors through that map, proving the middle exactness and the first map's injectivity. These facts also show that the dual sequence is canonical, independently of any local complement. \(\square\)

**Exercise K.9 (curvature, prolongation and dimensions).** Explain why zero ordinary prolongation need not imply zero curvature or zero derivative-curvature space; recover the tensor-product curvature parameter from its Ricci tensor; compute the dimensions for the two form-preserving factors; and identify the two terms in the dual product-jet sequence.

**Solution.** For the real or complex cubic algebra, H.8 and J.9 prove \(\mathfrak g^{(1)}=0\), while H.4–H.5 and J.7 give \(\dim K=3\), \(\dim K^1=4\) over the chosen field. These are explicit complete calculations, not dimension assumptions. K.1 explains the distinction: zero ordinary prolongation makes \(H^{1,2}=K\); it does not force that cohomology to vanish.

The general-linear parameter is recovered by the four projections and nonzero denominators in (K.20); its curvature space has dimension \(m^2n^2\). In the symmetric restriction a basis for the parameter space consists of the \(m\) diagonal symmetric forms and the \(m(m-1)/2\) off-diagonal symmetric pairs, so
\[
\dim K(\operatorname{GL}(U)\cdot\operatorname{O}(h))=\frac{m(m+1)}2.
\tag{K.36}
\]
Here the notation means the Lie algebra curvature space of the represented group, so disconnectedness of the orthogonal group is irrelevant. In the alternating restriction the \(m(m-1)/2\) strictly upper-triangular alternating pairs form a basis, giving
\[
\dim K(\operatorname{GL}(U)\cdot\operatorname{Sp}(h))=\frac{m(m-1)}2.
\tag{K.37}
\]
In both restricted cases \(s_UQ=s_WQ=\epsilon Q\), so the simpler Ricci formula is \(\operatorname{Ric}_Q=(m+n-2\epsilon)Q\). Dividing by that scalar recovers \(Q=P\otimes h\); any fixed pair with nonzero \(h\)-value then recovers \(P\). Both derivative-curvature spaces are zero by K.6, for every allowed real signature as well as over \(\mathbb C\).

Finally the two summands in the dual sequence (K.34) are explicitly
\[
A^*=\pi_1^*((J^1L_1)^*)\otimes\pi_2^*(L_2^*),\qquad
B^*=\pi_1^*(L_1^*)\otimes\pi_2^*((J^1L_2)^*).
\tag{K.38}
\]
They are different factor terms. The coordinate proof (K.35), followed by the difference-of-values dual map, determines both and their signs; no repeated copy of the first term belongs in place of the second. The canonical identifications used here send a tensor of two linear functionals to their product functional on decomposable tensors; choosing bases proves this is an isomorphism and the transition laws prove it is a bundle identification. \(\square\)

### Exact free source and proof boundaries

The construction source is Sergei Merkulov and Lorenz Schwachhöfer, *Classification of irreducible holonomies of torsion-free affine connections*, [arXiv:math/9907206v1, 1 July 1999](https://arxiv.org/pdf/math/9907206v1). The native title page identifies that exact edition. Section 3.1, native PDF pages 18–19, gives the prolongation and Spencer setup; native page 22 supplies the embedded symmetric/exterior-sequence motivation; Section 5, native pages 33–34, gives the product-jet sequence; native pages 37–38 give the general-linear, orthogonal and symplectic curvature formulas and consequences. The repeated first summand in the printed dual sequence on native page 34 is resolved here by deriving both factor terms directly.

K.2 supplies the polynomial contraction; K.3 supplies the entire coordinate surjectivity argument; K.5–K.6 supply all of the form-restriction and derivative-Bianchi calculations. Thus none of the source's external Borel–Weil, sheaf-cohomology, vanishing, spectral-sequence or holonomy-classification assertions is a proof provider. No paid onward reference is used. This is new exposition and proof completion; no human-source prose, figures or source files are reproduced. Parts L and M supply the infinite families and their complete structure equations.

## L. The infinite tensor families and actual connections

The tensor factor of dimension two is essential in this part. K.3–K.6 assumed both factor dimensions at least three and do not cover it. We use the exact free Chi–Merkulov–Schwachhöfer preprint cited below, supplying the algebraic and existence arguments explicitly. Part M supplies the complete curvature-space and differentiated structure-equation classification; the injective family constructed in this part does not alone compute the entire curvature space.

Let \(\mathbb F=\mathbb R\) or \(\mathbb C\), let \(U=\mathbb F^2\) have basis \(e,f\) and area form \(\varepsilon(e,f)=1\), and let \(W=\mathbb F^n\), \(n\geq3\), have a nondegenerate symmetric bilinear form \(h\). Put
\[
V=U\otimes W,\qquad
\mathfrak g=\mathfrak{sl}(U)\oplus\mathfrak{so}(W,h),\qquad
(A,M)(u\otimes x)=Au\otimes x+u\otimes Mx.
\tag{L.1}
\]
The direct sum acts faithfully. The scalar-kernel argument in K.3 works in any positive factor dimensions: a pair acting as zero consists of opposite scalar identities. Its first trace is zero and the field has characteristic zero, so both scalars are zero. Write \(A+M\) for this represented pair. The orthogonal algebra means \(h(Mx,y)+h(x,My)=0\). The trace-zero algebra on \(U\) is also its area-preserving algebra: direct evaluation on \(e,f\) gives
\(\varepsilon(Au,v)+\varepsilon(u,Av)=\operatorname{tr}(A)\varepsilon(u,v)\).

Define the operators
\[
S(u,v)w=\varepsilon(u,w)v+\varepsilon(v,w)u,\qquad
T(x,y)z=h(x,z)y-h(y,z)x.
\tag{L.2}
\]
They belong to \(\mathfrak{sl}(U)\) and \(\mathfrak{so}(W,h)\), respectively, by direct substitution in the preceding preservation equations. Let \(H e=e,H f=-f\), \(E f=e,E e=0\), and \(F e=f,F f=0\). Then
\[
S(e,e)=2E,\qquad S(e,f)=-H,\qquad S(f,f)=-2F.
\tag{L.3}
\]

**Lemma L.1 (normalizations and invariant pairings).** The alternating form
\[
\sigma(u\otimes x,v\otimes y)=\varepsilon(u,v)h(x,y)
\tag{L.4}
\]
is nondegenerate and invariant under \(\mathfrak g\). A nondegenerate invariant symmetric pairing on \(\mathfrak g\) is
\[
B(A+M,A'+M')=-\tfrac12\operatorname{tr}_U(AA')
                         -\tfrac12\operatorname{tr}_W(MM').
\tag{L.5}
\]
In these precise conventions,
\[
B(A,S(u,v))=\varepsilon(Au,v),\qquad
B(M,T(x,y))=h(Mx,y).
\tag{L.6}
\]
We use \(B\) as a chosen trace pairing, without identifying its normalization with the Killing form.

**Proof.** The matrix of (L.4), in the decomposition \(e\otimes W\oplus f\otimes W\), is \(\left(\begin{smallmatrix}0&h\\-h&0\end{smallmatrix}\right)\), which is invertible. Its invariance is the sum of the area- and \(h\)-preservation equations. The identity \(\operatorname{tr}(XY)=\operatorname{tr}(YX)\) follows by exchanging the two finite indices. It makes (L.5) symmetric and invariant under conjugation, and gives its infinitesimal invariance by differentiating, or by expanding the commutators.

The trace of a rank-one operator \(z\otimes\lambda\) is \(\lambda(z)\), as a basis calculation shows. Consequently
\[
\begin{aligned}
\operatorname{tr}(AS(u,v))
 &=\varepsilon(u,Av)+\varepsilon(v,Au)=-2\varepsilon(Au,v),\\
\operatorname{tr}(MT(x,y))
 &=h(x,My)-h(y,Mx)=-2h(Mx,y).
\end{aligned}
\tag{L.7}
\]
This proves (L.6).

On the basis \(H,E,F\), the nonzero entries of \(B\) are \(B(H,H)=-1\) and \(B(E,F)=B(F,E)=-1/2\), so that block is nondegenerate. Choose an \(h\)-orthogonal basis \(w_i\), with \(h(w_i,w_i)=d_i\ne0\). Such a basis is obtained by induction: polarization supplies a vector of nonzero square; subtract its component to form its nondegenerate perpendicular complement and repeat. This works over both fields without choosing complex square roots. The preservation equation in this basis is \(d_iM^i_j+d_jM^j_i=0\); it shows that the \(T_{ij}=T(w_i,w_j)\), \(i<j\), form a basis of the orthogonal algebra. Equation (L.6) makes them pairwise \(B\)-orthogonal, with \(B(T_{ij},T_{ij})=d_id_j\ne0\). Thus the second block, and hence \(B\), is nondegenerate. \(\square\)

**Proposition L.2 (irreducibility and all invariant bilinear forms).** The representation (L.1) is irreducible over \(\mathbb F\), and every invariant bilinear form on \(V\) is a scalar multiple of \(\sigma\). In particular it has no nonzero invariant symmetric bilinear form.

**Proof.** The associative algebra generated by \(E,F,H\) on \(U\) is all of \(\operatorname{End}(U)\): \(EF\) and \(FE\) are its two diagonal matrix units, and \(E,F\) the other two. On the orthogonal basis from L.1,
\[
T_{ij}^{2}=-d_id_j(P_i+P_j),
\tag{L.8}
\]
where \(P_i\) is the coordinate projection onto \(\mathbb Fw_i\). For distinct \(i,j,k\),
\(2P_i=(P_i+P_j)+(P_i+P_k)-(P_j+P_k)\).
Thus all \(P_i\) lie in the associative algebra generated by the \(T_{ij}\). The operator \(P_iT_{ij}P_j\) sends \(w_j\) to \(-d_jw_i\) and kills the other basis vectors. Its nonzero scalar multiple is the \(ij\) matrix unit. Hence that associative algebra is all of \(\operatorname{End}(W)\). This argument includes \(n=3\) and \(n=4\).

The two commuting factor actions on \(V\) therefore generate all tensor products of matrix units, which are every matrix unit of \(\operatorname{End}(V)\). A nonzero invariant subspace is stable under these products. Applying matrix units to a vector with a nonzero coordinate gives every basis vector, so the subspace is \(V\). Likewise an endomorphism commuting with \(\mathfrak g\) commutes with every matrix unit. Commutation with the diagonal units first makes it diagonal, and with the off-diagonal units makes all diagonal entries equal. Its commutant is precisely the scalars.

Given a bilinear form \(b\), nondegeneracy of \(\sigma\) writes it uniquely as \(b(x,y)=\sigma(Cx,y)\). If \(b\) is invariant, its preservation equation, minus that for \(\sigma\), is \(\sigma((CA-AC)x,y)=0\) for each represented \(A\in\mathfrak g\). Thus \(C\) commutes with \(\mathfrak g\), so is scalar. This proves the asserted description and excludes symmetric forms in characteristic zero. \(\square\)

For \(Z=A+M\in\mathfrak g\), define
\[
\begin{aligned}
\rho_Z(u\otimes x,v\otimes y)
={}&\varepsilon(u,v)\bigl(h(x,y)(A+M)
                  +T(x,My)+T(y,Mx)\bigr)\\
 &+h(x,My)S(u,v)-\varepsilon(Au,v)T(x,y).
\end{aligned}
\tag{L.9}
\]
All summands have the specified factor-algebra values, and the formula descends to a bilinear map of the two tensor-product arguments.

**Theorem L.3 (a faithful equivariant curvature family).** Formula (L.9) is skew in its arguments and satisfies the first Bianchi identity. The map
\[
\rho:\mathfrak g\longrightarrow K(\mathfrak g)
\tag{L.10}
\]
is linear, injective and equivariant under the area- and \(h\)-preserving factor groups, over either field and for every \(n\geq3\).

**Proof.** In (L.9), \(\varepsilon\) and \(h(x,My)\) are skew, \(h\) and \(S\) are symmetric, and \(\varepsilon(Au,v)\) is symmetric while \(T\) is skew. This proves skewness. Linearity is visible. Each formula is a contraction using the preserved forms, so changing the factors' bases sends \(\rho_Z\) to \(\rho_{gZg^{-1}}\), proving equivariance.

We supply the full Bianchi cancellation. In dimension two one has
\[
\varepsilon(u,v)w+\varepsilon(v,w)u+\varepsilon(w,u)v=0.
\tag{L.11}
\]
It follows by expansion on \(e,f\), or by noting that its left side is an alternating trilinear function in a two-dimensional space. The \(A\)-dependent part of \(\rho_Z(u x,v y)(w z)\), where juxtaposition denotes tensor product, is
\[
\varepsilon(u,v)h(x,y)Aw\otimes z
 -\varepsilon(Au,v)w\otimes\bigl(h(x,z)y-h(y,z)x\bigr).
\tag{L.12}
\]
In its cyclic sum, the coefficient of the displayed \(W\)-vector \(x\) is \(h(y,z)\) times
\[
\varepsilon(v,w)Au+\varepsilon(Au,v)w-\varepsilon(Aw,u)v=0.
\tag{L.13}
\]
Indeed (L.11) with \(Au,v,w\), and the symmetry \(\varepsilon(Au,w)=\varepsilon(Aw,u)\), give exactly this equation. The coefficients of \(y,z\) vanish by cyclic permutation. Collecting these terms proves a tensor identity whether or not \(x,y,z\) are independent.

For the \(M\) part put \(t(x,y)=h(Mx,y)\), a skew form. Its complete expansion is
\[
\begin{aligned}
\rho_M(u x,v y)(w z)
={}&\varepsilon(u,v)w\otimes
  \bigl(h(x,y)Mz+h(x,z)My+h(y,z)Mx\bigr)\\
 &-\varepsilon(u,v)w\otimes
  \bigl(t(y,z)x+t(x,z)y\bigr)\\
 &-t(x,y)\bigl(\varepsilon(u,w)v+\varepsilon(v,w)u\bigr)\otimes z.
\end{aligned}
\tag{L.14}
\]
In the cyclic sum the coefficient multiplying \(Mx\) is \(h(y,z)\) times (L.11), hence zero; the \(My,Mz\) terms vanish in the same way. The remaining coefficient multiplying \(t(x,y)z\) is
\[
\varepsilon(v,w)u-\varepsilon(w,u)v
-\varepsilon(u,w)v-\varepsilon(v,w)u=0.
\tag{L.15}
\]
The two other coefficients are its cyclic permutations. This accounts for every term of (L.14). Thus both parts satisfy Bianchi on decomposable vectors, and multilinearity proves it on all of \(V\).

For injectivity, take the same nonzero \(u\) in both arguments. The two algebra components of \(\rho_Z(u x,u y)=0\) are
\[
h(x,My)S(u,u)=0,\qquad
\varepsilon(Au,u)T(x,y)=0.
\tag{L.16}
\]
The directness of the represented sum was proved in (L.1). The operator \(S(u,u)\) is nonzero: choose \(v\) with \(\varepsilon(u,v)\ne0\), and evaluate it on \(v\). The first equality for all \(x,y\) gives \(M=0\). Some \(T(x,y)\) is nonzero by the basis in L.1, so the second equality for all \(u\) gives \(\varepsilon(Au,u)=0\). Polarizing this equality gives \(\varepsilon(Au,v)=0\) for all \(u,v\), since that form is symmetric. Nondegeneracy of \(\varepsilon\) gives \(A=0\). \(\square\)

**Proposition L.4 (a curvature tensor spanning the entire algebra).** In the real case take any signature \((p,q)\), \(p+q=n\geq3\), with an orthogonal basis having \(d_i=\pm1\). In the complex case take the standard form \(d_i=1\). For
\[
Z_0=2H+T_{12},
\tag{L.17}
\]
the values of \(\rho_{Z_0}\) span all of \(\mathfrak g\). The set of parameters \(Z\) with this spanning property is open and dense.

**Proof.** Write \(M=T_{12}\). In (L.16), choosing \(u=e\) or \(u=f\) kills the second component because these are eigenvectors of \(2H\). Since \(h(w_1,Mw_2)=-d_1d_2\ne0\), those values give nonzero pure multiples of \(E\) and \(F\) in the linear span.

Put \(u=e+f\). For a decomposable \(N=T(x,y)\), equations (L.3), (L.6) and (L.9) give
\[
\rho_{Z_0}(u x,u y)
=-2B(M,N)E+2B(M,N)H+2B(M,N)F-4N.
\tag{L.18}
\]
Subtract the already available \(E,F\) components and divide by \(-4\). Because such \(N\)'s span the orthogonal algebra, the span contains
\[
C_N=N-\tfrac12B(M,N)H
\quad\hbox{for every }N\in\mathfrak{so}(W,h).
\tag{L.19}
\]
Choose \(k\geq3\); then \(Mw_k=0\), and (L.9) yields
\(\rho_{Z_0}(e w_k,f w_k)=d_k(2H+M)\).
Subtracting \(C_M\) from \(2H+M\) leaves
\[
\bigl(2+\tfrac12B(M,M)\bigr)H
=\bigl(2+\tfrac12d_1d_2\bigr)H\ne0.
\tag{L.20}
\]
Thus \(H\) is also in the span, and (L.19) gives every \(N\) separately. This proves the claim for every real signature, including the definite ones, and for the complex standard form.

In bases, the map \(\Lambda^2V\to\mathfrak g\) defined by \(\rho_Z\) is a matrix with entries linear in \(Z\). Full rank is the nonvanishing of at least one maximal minor, so the full-span set is open. At (L.17) one such minor is nonzero, hence its determinant polynomial is not the zero polynomial. A polynomial over \(\mathbb R\) or \(\mathbb C\) vanishing on a nonempty open set is identically zero: restrict successively to coordinate lines in a product of small intervals or discs and use that a nonzero one-variable polynomial has at most its degree many roots. Thus that minor's zero set has empty interior. Its nonzero set is dense, proving density of the full-span set. \(\square\)

For \(Z=A+M\), \(Z'=A'+M'\), define
\[
\begin{aligned}
\Phi(Z,Z';u x,v y)
={}&\varepsilon(u,v)h(x,y)B(Z,Z')\\
 &-\varepsilon(Au,v)h(M'x,y)
  -\varepsilon(A'u,v)h(Mx,y)\\
 &+\varepsilon(u,v)\bigl(h(Mx,M'y)+h(My,M'x)\bigr).
\end{aligned}
\tag{L.21}
\]
Here and below \(u x\) abbreviates \(u\otimes x\).

**Proposition L.5 (an admissible quadratic map with its exact normalization).** For \(a=B(Z,\,\cdot\,)\in\mathfrak g^*\) and \(c\in\mathbb F\), put
\[
\phi_c(a)(x,y)=\tfrac12\Phi(Z,Z;x,y)+c\sigma(x,y).
\tag{L.22}
\]
The tensor \(\Phi\) is symmetric in its two algebra arguments, alternating in its two \(V\) arguments, and invariant. Its defining derivative in I.26 is exactly \(D_a=\rho_Z\). In particular \(\phi_c\) satisfies both admissibility equations I.27, over the chosen field, and its quadratic term is nonzero.

**Proof.** Symmetry in \(Z,Z'\) follows from symmetry of \(B,h\): interchange them in the last line of (L.21) and exchange the two \(h\) arguments. The first and last lines are alternating in \(u x,v y\) because their \(W\)-factors are symmetric and \(\varepsilon\) is skew. Each middle term is also alternating: \(\varepsilon(Au,v)\) is symmetric in \(u,v\), whereas \(h(M'x,y)\) is skew in \(x,y\). Invariance follows from the preserved forms and the conjugation-invariant trace pairing.

More precisely, (L.6) gives the identity
\[
\Phi(Z,Z';x,y)=B\bigl(Z',\rho_Z(x,y)\bigr).
\tag{L.23}
\]
To check every term on decomposable arguments, pair (L.9) with \(A'+M'\). Its first term gives \(\varepsilon(u,v)h(x,y)B(Z,Z')\). The two \(T\) terms give
\(\varepsilon(u,v)(h(M'x,My)+h(M'y,Mx))\), the last line of (L.21) by symmetry of \(h\). The \(S\) term gives \(h(x,My)\varepsilon(A'u,v)=-h(Mx,y)\varepsilon(A'u,v)\). The remaining \(T\) term is \(-\varepsilon(Au,v)h(M'x,y)\). These are exactly its two middle terms.

For a direction \(\lambda=B(Z',\,\cdot\,)\), differentiation of (L.22) and symmetry of \(\Phi\) give
\((d\phi_c)_a(\lambda)(x,y)=\Phi(Z,Z';x,y)=\lambda(\rho_Z(x,y))\).
Thus \(D_a=\rho_Z\); the factor \(1/2\) in (L.22) is required by this convention. The second admissibility equation is L.3's proved Bianchi identity. For the first, let \(g\) be an element of the represented factor group. Invariance of \(B\) identifies \(a\circ\operatorname{Ad}_g\) with \(g^{-1}Zg\). The tensor invariance just proved gives
\(\phi_c(a\circ\operatorname{Ad}_g)(x,y)=\phi_c(a)(gx,gy)\).
Differentiation at the identity is precisely the first equation I.27, as proved in I.9. Finally, if the quadratic term vanished identically, polarization would give \(\Phi=0\). Equation (L.23), nondegeneracy of \(B\) and injectivity of \(\rho\) would then force every element of the nonzero algebra \(\mathfrak g\) to be zero, a contradiction. \(\square\)

**Lemma L.6 (zero ordinary first prolongation).** For the algebra (L.1), \(\mathfrak g^{(1)}=0\). For the complex algebra acting on its underlying real vector space, its ordinary real first prolongation is also zero.

**Proof.** Let \(P:V\to\mathfrak g\) be linear and satisfy \(P_x y=P_y x\). Write its values on the two summands as
\[
\begin{aligned}
P_{e a}&=\ell(a)H+\beta(a)E+\gamma(a)F+M_a,\\
P_{f b}&=-k(b)H+\eta(b)E+\tau(b)F+N_b,
\end{aligned}
\tag{L.24}
\]
with linear scalar functionals and linear orthogonal-algebra-valued maps on \(W\). Comparing the \(f\)-component for the pair \(e a,e b\) gives \(\gamma(a)b=\gamma(b)a\). With distinct basis vectors it forces every coefficient of \(\gamma\) to vanish. The pair \(f a,f b\) similarly gives \(\eta=0\). The remaining same-summand equations are
\[
M_ab-M_ba=\ell(b)a-\ell(a)b,\qquad
N_ab-N_ba=k(b)a-k(a)b.
\tag{L.25}
\]
Write \(\ell^\sharp,k^\sharp\) for the vectors representing these covectors under \(h\). The unique orthogonal solutions of (L.25) are
\[
M_ab=\ell(b)a-h(a,b)\ell^\sharp,\qquad
N_ab=k(b)a-h(a,b)k^\sharp.
\tag{L.26}
\]
Substitution verifies their skew preservation of \(h\) and their differences. For uniqueness, a difference \(Q_ab\) is symmetric in \(a,b\), while \(t(a,b,c)=h(Q_ab,c)\) is skew in \(b,c\). Successively using these two symmetries gives
\(t(a,b,c)=t(b,a,c)=-t(b,c,a)=-t(c,b,a)=t(c,a,b)=t(a,c,b)=-t(a,b,c)\).
Thus \(t=0\) and \(Q=0\).

The mixed pair \(e a,f b\) now gives
\[
\begin{aligned}
\beta(a)b&=-k(b)a+k(a)b-h(a,b)k^\sharp,\\
\tau(b)a&=-\ell(a)b+\ell(b)a-h(a,b)\ell^\sharp.
\end{aligned}
\tag{L.27}
\]
Set \(a=w_i,b=w_j\) with \(i\ne j\) in an orthogonal basis. In the first equality the \(w_i\) coefficient forces \(k(w_j)=0\); in the second the \(w_j\) coefficient forces \(\ell(w_i)=0\). Every index has a different partner since \(n\geq3\), so \(k=\ell=0\). Equations (L.26) give \(M=N=0\), and (L.27) gives \(\beta=\tau=0\). Hence \(P=0\).

For a real-linear prolongation map in the complex representation, each value \(P_x\) is a complex-linear endomorphism. Symmetry gives
\(P_{ix}y=P_y(ix)=iP_yx=iP_xy\).
Therefore \(P_{ix}=iP_x\) as endomorphisms, so the map is actually complex-linear. The complex calculation just proved makes it zero. \(\square\)

**Theorem L.7 (actual analytic connections in every stated dimension and signature).** For every real \((p,q)\) with \(p+q=n\geq3\), there are real analytic torsion-free connections on a base of dimension \(2n\), with full holonomy algebra \(\mathfrak{sl}(2,\mathbb R)\oplus\mathfrak{so}(p,q)\) in its tensor representation, and with nonparallel curvature. Over \(\mathbb C\) there are holomorphic examples on a base of complex dimension \(2n\); their underlying real connections have dimension \(4n\) and the full underlying real algebra of \(\mathfrak{sl}(2,\mathbb C)\oplus\mathfrak{so}(n,\mathbb C)\). For (L.22), realization is possible at every parameter, including singular Poisson parameters.

**Proof.** First take \(\mathbb F=\mathbb R\). Proposition L.5 supplies every hypothesis of I.9. Theorems I.7 and I.10 therefore construct an actual analytic connection at any chosen \((a,q)\in\mathfrak g^*\oplus V^*\), for any real \(c\). At \(a_0=B(Z_0,\,\cdot\,)\), L.4 makes the curvature values span \(\mathfrak g\); I.11 proves the full holonomy-algebra assertion.

The derivative map is \(dD_a(\lambda)=\rho_{B^{-1}\lambda}\). Choose \(x=e\otimes w_1\) and the coordinate covector \(q_0\) with \(q_0(e\otimes w_1)=1\) and zero on the other basis vectors. Then
\[
j(q_0,x)(H)=q_0(Hx)=1.
\tag{L.28}
\]
Consequently \(B^{-1}j(q_0,x)\ne0\), and injectivity in L.3 gives \(dD_{a_0}(j(q_0,x))\ne0\). Equation I.31 proves nonparallel curvature at the selected frame. This conclusion is independent of \(c\). It is obtained at a specified parameter, without a generic-rank assumption.

Here are the analytic details allowing the same construction over \(\mathbb C\), so a complex existence assertion is not hidden in terminology. The coefficient Banach algebras and contraction proof in I.1 work with complex coefficients: their estimates use absolute values and the same convergent majorants; a Cauchy sequence is complete by taking real and imaginary parts. The implicit-function proof uses the invertible complex derivative and its Neumann series, so its resulting convergent series has complex coefficients and is holomorphic. The flow construction in that proof likewise permits a complex time variable and gives holomorphic flows for holomorphic vector fields. The identities needed in I.2's straightening and induction follow by their convergent derivatives and uniqueness. Thus that full Frobenius proof gives holomorphic integral manifolds and local quotient sections for holomorphic involutive constant-rank distributions.

In I.5–I.7 choose complex cotangent coordinates and the same spray with zero vertical term. On a small complex neighbourhood, its flow exists for real times \(0\leq t\leq1\) by the coefficient estimates of I.1, and depends holomorphically on the initial complex point. The coefficientwise integral of its pulled-back complex two-form is holomorphic by the uniform majorant argument in I.1. Its zero-section matrix is invertible over \(\mathbb C\), hence remains so locally. The complete endpoint identities I.16–I.24 are algebraic differentiations and integrations and hold unchanged over \(\mathbb C\). They prove the complex Poisson-submersion statement at every point. Finally, I.10's independent Hamiltonian fields, two involutive distributions, their just-established holomorphic quotients and formula I.34 are all holomorphic. This supplies the claimed holomorphic torsion-free connection, with complex curvature \(-\rho_{Z_0}\) and the same nonzero derivative test (L.28).

Regarding a holomorphic coframe as a real coframe with values in \(V_{\mathbb R}\) gives its underlying real connection by that identical formula. Parallel transport stays in the represented complex group, by the real-time group ODE. The curvature is complex bilinear. Its values span the complex algebra by L.4, and its real span is also that whole underlying real algebra: multiplying the first curvature argument by \(i\) multiplies the value by \(i\). The real holonomy argument of I.11 therefore applies and proves the stated equality. Nonparallelness is unchanged. The complex basis has \(2n\) elements, and adjoining their \(i\)-multiples gives a real basis with \(4n\) elements. This verifies the real dimension directly. \(\square\)

**Proposition L.8 (the represented groups, kernels and realification).** The full restricted holonomy groups of L.7 are the images of
\[
SL(2,\mathbb R)\times SO_0(p,q),\qquad
SL(2,\mathbb C)\times SO_0(n,\mathbb C)
\tag{L.29}
\]
under tensor product; the subscript denotes the identity component. The real kernel is trivial unless both \(p,q\) are even, in which case it consists of \((I,I)\) and \((-I,-I)\). The complex kernel has two elements exactly when \(n\) is even. The underlying real complex representation is irreducible. Its invariant real bilinear forms are exactly
\[
\operatorname{Re}(z\sigma),\qquad z\in\mathbb C,
\tag{L.30}
\]
and are all alternating. Consequently none of these full holonomy connections preserves a nondegenerate symmetric real bilinear form.

**Proof.** The groups in (L.29) have the displayed Lie algebras. For the orthogonal factor this follows from the local matrix constraint and tangent calculation in F.1; imposing determinant one does not change the identity component or its tangent algebra. For \(SL(2,\mathbb F)\), the derivative of determinant at the identity is trace, and an invertible entry solves the determinant equation locally for the opposite entry, giving its manifold chart and tangent algebra.

The group \(SL(2,\mathbb F)\) is connected over either field. Indeed elimination expresses every determinant-one matrix with upper-left entry \(a\ne0\) as a lower elementary matrix, \(\operatorname{diag}(a,a^{-1})\), and an upper elementary matrix. If that entry is zero, a left upper elementary operation makes it nonzero because the lower-left entry cannot also be zero. Write \(U(t)=\left(\begin{smallmatrix}1&t\\0&1\end{smallmatrix}\right)\), \(L(t)=\left(\begin{smallmatrix}1&0\\t&1\end{smallmatrix}\right)\). Direct multiplication gives
\[
U(t)L(-t^{-1})U(t)=
\begin{pmatrix}0&t\\-t^{-1}&0\end{pmatrix}=w(t),
\qquad w(t)w(-1)=\operatorname{diag}(t,t^{-1}).
\tag{L.31}
\]
Every elementary matrix is joined to the identity by replacing its parameter by \(s\) times that parameter, \(0\leq s\leq1\). Products give the required paths, also for complex parameters. The other factors in (L.29) are connected by definition. Their images are connected Lie subgroups with the faithful infinitesimal representation (L.1). The image may be given its quotient Lie-group structure by the finite kernel computed below; local charts follow because the differential is injective and the kernel is discrete. The complete subgroup result C.1 gives the same intrinsic image structure.

After restricting the constructed base to a coordinate ball, every based loop is contractible, by linear contraction in the coordinates. The holonomy group is therefore its restricted group. Its algebra is the full algebra by L.7. The inclusion into the connected represented group has invertible differential between equal-dimensional manifolds, so the inverse theorem gives an open identity neighbourhood in its image. A subgroup containing such a neighbourhood is open; its cosets are open and connectedness makes it the whole group. This proves (L.29).

If \(g\otimes k=I\), then \(g=tI\), \(k=t^{-1}I\). One direct proof applies \(g\otimes k\) to basis tensors: since \(k\) is invertible, applying a covector nonzero on \(kw_j\) shows that \(g\) preserves each basis line, and comparison for all \(i,j\) makes its diagonal entries equal and \(k\) the inverse scalar. The determinant-one condition on \(g\) gives \(t^2=1\), so only the two indicated pairs are possible.

For real signature \((p,q)\), the projections of a positive orthogonal frame onto the positive coordinate subspace form an invertible \(p\)-by-\(p\) matrix: a nonzero positive vector cannot be sent entirely into the negative subspace. The same reasoning applies to the negative block. Their determinants are continuous and nonzero along an orthogonal path from the identity. At \(-I\) their signs are \((-1)^p\) and \((-1)^q\), so both must be positive. Conversely, if \(p,q\) are even, rotate each positive coordinate two-plane and each negative coordinate two-plane through angle \(\pi\); these rotations preserve the form and give a path from \(I\) to \(-I\). The zero-dimensional block has determinant one and requires no rotations. Thus \(-I\in SO_0(p,q)\) exactly in the stated cases. In the complex group, odd \(n\) excludes \(-I\) by its determinant. For even \(n\) the same real two-plane rotations for the standard complex bilinear form give a path. This proves both kernels.

For the last assertions, the real associative algebra generated by the complex represented Lie algebra contains multiplication by \(i\): multiply the represented \(H\otimes I\) by \(iH\otimes I\), using \(H^2=I\). A real invariant subspace is therefore complex, and L.2 makes it all of \(V\) or zero. A commuting real endomorphism also commutes with multiplication by \(i\); it is complex-linear, so L.2's matrix-unit proof makes it a complex scalar. The real alternating form \(\Omega=\operatorname{Re}\sigma\) is nondegenerate: if \(\Omega(x,y)=0\) for all \(y\), applying this also to \(iy\) gives both real and imaginary parts of \(\sigma(x,y)\) zero, hence \(x=0\). Write any invariant real bilinear form as \(\Omega(Cx,y)\). The same preservation computation as in L.2 forces \(C\) into that complex-scalar commutant, giving exactly (L.30). These forms are alternating. In the real family the corresponding assertion is L.2. A parallel symmetric form would at a point be preserved by every parallel transport loop, hence by the full group; the computed invariant spaces exclude a nonzero such form. \(\square\)

**Exercise L.9 (dimensions, nonparallelness and the central quotient).** Specify the dimensions in the realization, exhibit a nonparallel parameter in every real signature, distinguish the complex representation from its realification, and determine whether the represented product is a direct product.

**Solution.** The basis in L.1 gives
\[
d=\dim_{\mathbb F}\mathfrak g=3+\frac{n(n-1)}2,\qquad
N=\dim_{\mathbb F}(\mathfrak g\oplus V)
  =\frac{n^2+3n+6}{2}.
\tag{L.32}
\]
For real input the arbitrary-point realization I.7 has dimension \(2N\); the coframe integral manifold in I.10 has dimension \(N\); its vertical leaves have dimension \(d\); and its base has dimension \(N-d=2n\). These are dimensions of different manifolds. A regular-point realization may be smaller by I.4, but is not needed for the arbitrary-point assertion. For holomorphic input the same numbers are complex dimensions; the underlying real dimensions are respectively \(4N,2N,2d,4n\).

For every real signature use \(Z_0=2H+T_{12}\), \(a_0=B(Z_0,\,\cdot\,)\), and the covector \(q_0\) from (L.28), with any \(c\). Formula (L.20) is either \((5/2)H\) or \((3/2)H\), never zero. Thus the curvature spans the full algebra. The nonzero value \(j(q_0,e\otimes w_1)(H)=1\), followed by the injective map (L.10), makes the covariant derivative of curvature nonzero. These are actual parameters of the constructed connections, not merely an algebraic tensor example.

Over \(\mathbb C\), L.2 gives one complex dimension of invariant complex bilinear forms; L.8 gives two real dimensions of invariant real bilinear forms, with basis \(\operatorname{Re}\sigma,\operatorname{Im}\sigma\). They are independent: a real combination corresponds to \(\operatorname{Re}(z\sigma)=0\), and evaluating also at \(ix\) gives \(z\sigma=0\), hence \(z=0\). No symmetric invariant appears on realification. The complex vector space has dimension \(2n\), so its realification has dimension \(4n\), not \(8n\).

Finally the group is the product in (L.29) modulo exactly the central kernel proved there. It is a direct product as a represented image when that kernel is trivial; otherwise the two factors share the simultaneous sign and the representation identifies \((I,I)\) with \((-I,-I)\). For real signatures the latter occurs precisely when both signature entries are even, and for the complex standard form precisely when \(n\) is even. None of these finite kernels changes the faithful Lie algebra, the curvature dimension lower bound \(d\), or the actual full-holonomy conclusion. Ordinary prolongation is zero by L.6, while the nonzero curvature family and its realized nonparallel derivatives show again that ordinary prolongation and derivative curvature are different spaces. \(\square\)

### Exact free source and continuation

The human construction source is Quo-Shin Chi, Sergey A. Merkulov and Lorenz J. Schwachhöfer, [*On the Existence of Infinite Series of Exotic Holonomies*, free author preprint dated 9 April 1996](https://wwwold.mathematik.tu-dortmund.de/~lschwach/papers/Berger/InfExoticHol.pdf). The relevant native pages are 5–6 for the factor conventions and curvature formula, 9–12 for the Poisson construction and invariant quadratic tensor, and 2 for the two families. The real dimension printed for the complex family on native page 2 is corrected by the explicit basis count above. The trace pairing is defined with its actual normalization, and the factor in the quadratic map is derived from I.26 rather than inferred from a name for the pairing.

The twistor/cohomology assertions preceding the curvature formula, the external references and the omitted computations are not proof providers. L.1–L.9 supply their stated claims directly; I.1–I.11 supply the complete analytic and Poisson construction. No source prose, image or PDF is reproduced. Part M proves the complete curvature and derivative-curvature spaces, the full quadratic-compatibility space, all infinite-family structure equations and their converse. The ordinary-prolongation calculation L.6 is used there to justify the realification of the entire curvature spaces.

## M. The entire tensor curvature spaces and complete structure equations

This part completes the algebra that an existence construction alone cannot supply. We keep exactly the conventions of L.1–L.5: \(V=\mathbb F^2\otimes W\), \(\mathfrak g=\mathfrak{sl}_2(\mathbb F)\oplus\mathfrak{so}(W,h)\), \(\mathbb F=\mathbb R\) or \(\mathbb C\), and \(n=\dim W\geq3\), except where a smaller dimension is explicitly allowed. The curvature map is (L.9), its pairing is (L.5), and its quadratic map is (L.22). All statements below concern the entire spaces defined by the Bianchi identities in F.6. No dimension formula from an external classification is assumed.

**Theorem M.1 (every first-Bianchi tensor).** The map \(Z\mapsto\rho_Z\) of L.3 is an isomorphism onto \(K(\mathfrak g)\). Consequently
\[
\dim_{\mathbb F}K(\mathfrak g)=d:=3+\frac{n(n-1)}2.
\tag{M.1}
\]
This includes every real signature, and includes \(n=3,4\) without exceptions.

**Proof.** Write \(ea=e\otimes a\), \(fa=f\otimes a\). A represented algebra element has the unique block form
\[
\begin{pmatrix}\alpha I+M&\beta I\\\gamma I&-\alpha I+M\end{pmatrix},
\qquad M\in\mathfrak{so}(W,h).
\tag{M.2}
\]
For an arbitrary \(R\in K(\mathfrak g)\), denote its four components on \((ea,eb)\) by \(\alpha_+(a,b),p(a,b),\gamma_+(a,b),M_+(a,b)\); on \((fa,fb)\) by \(\alpha_-(a,b),\beta_-(a,b),r(a,b),M_-(a,b)\); and on \((ea,fb)\) by \(\alpha(a,b),\beta(a,b),\gamma(a,b),C(a,b)\). Same-row arguments give alternating bilinear functions; the mixed functions are initially arbitrary bilinear functions.

The lower component of Bianchi on \((ea,eb,ec)\) is \(\gamma_+(a,b)c+\gamma_+(b,c)a+\gamma_+(c,a)b=0\). Apply this to any three distinct basis vectors and compare their coefficients. Every entry of \(\gamma_+\) is zero, since there is a third index when \(n\geq3\). The upper component on three \(f\)-vectors gives \(\beta_-=0\) in exactly the same way, with \(e,f\) exchanged.

The lower component on \((ea,eb,fc)\) and the upper component on \((fa,fb,ec)\) give, respectively,
\[
\begin{aligned}
M_+(a,b)c&=\alpha_+(a,b)c-\gamma(b,c)a+\gamma(a,c)b,\\
M_-(a,b)c&=-\alpha_-(a,b)c+\beta(c,b)a-\beta(c,a)b.
\end{aligned}
\tag{M.3}
\]
Choose the orthogonal basis \(w_i\) of L.1, with \(h(w_i,w_j)=d_i\delta_{ij}\), \(d_i\ne0\). In either equation put \(a=w_i,b=w_j,c=w_k\) with distinct indices and pair with \(w_k\). Skew-adjointness of \(M_\pm\) gives \(\alpha_\pm(w_i,w_j)=0\). Alternation then makes both functions identically zero. In the first equation, putting \(c=w_i\) and pairing with \(w_i\) gives \(\gamma(w_j,w_i)=0\) for \(i\ne j\). Skew-adjointness on \(w_i,w_j\) gives
\(d_j\gamma(w_i,w_i)=d_i\gamma(w_j,w_j)\).
Hence \(\gamma=s h\) for one scalar \(s\), and \(M_+(a,b)=sT(a,b)\). In the second equation the same two pairings give \(\beta(w_i,w_j)=0\) for \(i\ne j\) and
\(d_i\beta(w_j,w_j)=d_j\beta(w_i,w_i)\).
Thus \(\beta=t h\) and \(M_-(a,b)=-tT(a,b)\).

The two other components of these mixed Bianchi equations are
\[
\begin{aligned}
0={}&p(a,b)c+\alpha(b,c)a+C(b,c)a-\alpha(a,c)b-C(a,c)b,\\
0={}&r(a,b)c+\alpha(c,b)a-C(c,b)a-\alpha(c,a)b+C(c,a)b.
\end{aligned}
\tag{M.4}
\]
We solve them, without an assumption on the symmetry of \(\alpha\). Set
\(\mathcal C(a,b;c,z)=h(C(a,b)c,z)\), which is skew in its last two arguments. For distinct indices \(i,j\), pair the first equation in (M.4), with \(a=w_i,b=w_j\), with \(w_i\); then do this to the second equation. Skewness gives
\[
\begin{aligned}
\mathcal C(w_i,c;w_i,w_j)
 &=-p_{ij}h(c,w_i)-d_i\alpha(w_j,c),\\
\mathcal C(c,w_i;w_i,w_j)
 &=r_{ij}h(c,w_i)+d_i\alpha(c,w_j).
\end{aligned}
\tag{M.5}
\]
Here \(p_{ij}=p(w_i,w_j)\), and similarly for other two-index entries. Put \(c=w_i\) and compare the two equations. They give \(\alpha_{ij}+\alpha_{ji}=-p_{ij}-r_{ij}\). Interchanging \(i,j\) preserves the left side and negates the right side. Therefore
\(\alpha_{ij}=-\alpha_{ji}\) and \(r_{ij}=-p_{ij}\).
Putting \(c=w_j\) in (M.5), and also interchanging \(i,j\), gives \(d_i\alpha_{jj}=d_j\alpha_{ii}\). There is a scalar \(a_0\) for which the diagonal entries of \(\alpha\) equal those of \(a_0h\).

To determine the remaining skew part, take distinct \(i,j,k\), insert \((a,b,c)=(w_j,w_k,w_i)\) in the first equation of (M.4), and pair with \(w_i\). The result is
\[
\mathcal C(w_k,w_i;w_j,w_i)-\mathcal C(w_j,w_i;w_k,w_i)=-d_i p_{jk}.
\tag{M.6}
\]
The second equation of (M.5) evaluates its left side as
\(-d_i\alpha_{kj}+d_i\alpha_{jk}=2d_i\alpha_{jk}\).
Thus \(p_{jk}=-2\alpha_{jk}\) for distinct \(j,k\), and \(r_{jk}=2\alpha_{jk}\). Let \(M\in\mathfrak{so}(W,h)\) be the unique operator satisfying
\[
h(Ma,b)=\alpha(a,b)-a_0h(a,b).
\tag{M.7}
\]
It exists by nondegeneracy of \(h\), and the right side is alternating by the equations just proved.

For \(Z=a_0H+tE+sF+M\), direct substitution of \(e,f\) in (L.9) gives exactly the scalar components just determined and exactly \(M_+,M_-\). In particular its mixed diagonal scalar is \(a_0h(a,b)+h(Ma,b)\), its upper same-row scalar is \(-2h(Ma,b)\), and its lower same-row scalar is \(2h(Ma,b)\). Subtract this \(\rho_Z\) from \(R\). Only a mixed orthogonal component, still denoted \(C\), can remain. The first equation of (M.4) now says
\(C(a,c)b=C(b,c)a\).
For fixed \(c\), the trilinear tensor \(t(a,b,z)=h(C(a,c)b,z)\) is symmetric in its first two variables and skew in its last two. These symmetries force it to vanish:
\[
t(a,b,z)=t(b,a,z)=-t(b,z,a)=-t(z,b,a)
 =t(z,a,b)=t(a,z,b)=-t(a,b,z).
\tag{M.8}
\]
Characteristic zero and nondegeneracy of \(h\) give \(C=0\). We have proved surjectivity. L.3 already proved injectivity, membership and equivariance, and L.1 counted the basis of the algebra. This proves the theorem. \(\square\)

Identify \(\mathfrak g\) with \(\mathfrak g^*\) by \(Z\mapsto B(Z,\cdot)\), and write
\[
D_a=\rho_{B^{-1}a},\qquad
j(q,x)(A)=q(Ax),\qquad
L_q(x)=D_{j(q,x)}.
\tag{M.9}
\]
This is the positive \(j\) convention of I.9 and J.2; the minus sign occurs in the horizontal equation for \(a\), not in this definition.

**Theorem M.2 (every second-Bianchi derivative).** The map \(q\mapsto L_q\) is an equivariant isomorphism \(V^*\to K^1(\mathfrak g)\). In particular \(\dim_{\mathbb F}K^1(\mathfrak g)=2n\).

**Proof.** By M.1, any member of \(V^*\otimes K(\mathfrak g)\) is uniquely \(x\mapsto\rho_{Z_x}\), where \(Z:V\to\mathfrak g\) is linear. Write
\[
\begin{aligned}
Z_{ea}&=\ell(a)H+\beta(a)E+\gamma(a)F+M_a,\\
Z_{fa}&=k(a)H+\eta(a)E+\tau(a)F+N_a.
\end{aligned}
\tag{M.10}
\]
The defining condition is the algebra-valued identity
\(\rho_{Z_x}(y,z)+\rho_{Z_y}(z,x)+\rho_{Z_z}(x,y)=0\).
On three \(e\)-vectors its orthogonal component is
\(\gamma(a)T(b,c)+\gamma(b)T(c,a)+\gamma(c)T(a,b)=0\).
For three distinct orthogonal basis vectors the three \(T\)'s are independent, so \(\gamma=0\). Three \(f\)-vectors similarly give \(\eta=0\).

On \((ea,eb,fc)\), the \(E\) coefficient is
\[
h(b,c)\beta(a)-h(a,c)\beta(b)+2h(a,N_cb)=0.
\tag{M.11}
\]
On \((fa,fb,ec)\), the \(F\) coefficient is
\[
-h(b,c)\tau(a)+h(a,c)\tau(b)-2h(a,M_cb)=0.
\tag{M.12}
\]
Write \(\beta^\#,\tau^\#\) for the \(h\)-dual vectors. Nondegeneracy of \(h\) turns these equations into
\[
N_c=\tfrac12T(\beta^\#,c),\qquad M_c=\tfrac12T(\tau^\#,c).
\tag{M.13}
\]
The \(H\) coefficients of the same two triples are
\[
\begin{aligned}
0={}&h(b,c)\ell(a)-h(a,c)\ell(b)-h(b,M_ac)+h(a,M_bc),\\
0={}&-h(b,c)k(a)+h(a,c)k(b)+h(c,N_ab)-h(c,N_ba).
\end{aligned}
\tag{M.14}
\]
Substitution of (M.13) reduces the first line to
\(h(b,c)(\ell-\tau/2)(a)-h(a,c)(\ell-\tau/2)(b)=0\),
and the second to the negative of the same expression with covector \(k+\beta/2\). Put the two vector arguments equal to distinct orthogonal basis vectors and \(c\) equal to the second of them. Every entry of these covectors vanishes. Thus every possible derivative has the form
\[
\begin{aligned}
Z_{ea}&=\tfrac12\tau(a)H+\beta(a)E+\tfrac12T(\tau^\#,a),\\
Z_{fa}&=-\tfrac12\beta(a)H+\tau(a)F+\tfrac12T(\beta^\#,a).
\end{aligned}
\tag{M.15}
\]
For a covector \(q\) with \(q(ea)=r(a)\), \(q(fa)=s(a)\), the pairings in L.1 give directly
\[
\begin{aligned}
B^{-1}j(q,ea)&=-r(a)H-2s(a)E-T(r^\#,a),\\
B^{-1}j(q,fa)&=s(a)H-2r(a)F-T(s^\#,a).
\end{aligned}
\tag{M.16}
\]
For example the orthogonal term in the first line pairs with \(M\) as \(-h(Mr^\#,a)=r(Ma)\); the \(H,E,F\) pairings use \(B(H,H)=-1\), \(B(E,F)=-1/2\). Hence (M.15) is (M.16) with \(r=-\tau/2,s=-\beta/2\).

It remains to prove that every such parameter actually satisfies all derivative equations, including the orthogonal equations not needed for the elimination. Let \(\Phi\) be the symmetric four-tensor in L.5. Its contraction identity gives, for any \(T\in\mathfrak g\),
\[
\begin{aligned}
B(T,L_q(x)(y,z))
 &=\Phi(B^{-1}j(q,x),T;y,z)\\
 &=j(q,x)(\rho_T(y,z))=q(\rho_T(y,z)x).
\end{aligned}
\tag{M.17}
\]
The cyclic sum is zero by the complete first Bianchi proof L.3. Nondegeneracy of \(B\) proves membership in \(K^1\). If \(L_q=0\), injectivity of \(D\) gives \(q(Ax)=0\) for all \(A,x\); taking the invertible represented operator \(H\) gives \(q=0\). All contractions are equivariant, so the isomorphism is equivariant. \(\square\)

**Proposition M.3 (the whole spaces after realification).** For the full complex algebra acting on the underlying real space of \(\mathbb C^2\otimes\mathbb C^n\), every real curvature tensor is complex bilinear, and every real derivative tensor is complex linear in all three vector arguments. Its curvature and derivative spaces are therefore the underlying real spaces of the complex ones. Their real dimensions are \(2d\) and \(4n\).

**Proof.** The ordinary first prolongation of this real action is zero by L.6. For any real curvature tensor \(R\) and fixed vector \(x\), set \(P_y=R(ix,y)-iR(x,y)\), an element of the real algebra since the full complex algebra is closed under multiplication by \(i\). Subtract \(i\) times Bianchi on \((x,y,z)\) from Bianchi on \((ix,y,z)\). Algebra elements act complex linearly, so the terms containing \(R(y,z)\) cancel, leaving \(P_yz=P_zy\). The vanishing ordinary prolongation gives \(P=0\). Thus \(R\) is complex linear in its first argument and, by alternation, in its second.

Now let \(S\) be any real member of \(K^1\). Each \(S_x\) is complex bilinear by what was just proved. Subtract \(i\) times the derivative Bianchi identity on \((x,y,z)\) from the identity on \((ix,y,z)\). The terms \(S_y(z,ix)\), \(S_z(ix,y)\) cancel their \(i\)-multiples. The result is \(S_{ix}(y,z)=iS_x(y,z)\). Conversely the complex tensors in M.1 and M.2 satisfy the real equations on restriction. This proves both identifications and the dimension count. \(\square\)

**Lemma M.4 (all bilinear compatibility forms, including small dimensions).** Let \(n\geq1\) for this lemma. A bilinear form \(T\) on \(\mathbb F^2\otimes W\), with no symmetry assumed, satisfies
\[
T(x,Ay)=T(y,Ax)\quad(x,y\in V,\ A\in\mathfrak g)
\tag{M.18}
\]
if and only if \(T=c\sigma\). For the full complex action viewed over the reals, the real solutions are exactly \(T=\operatorname{Re}(c\sigma)\), \(c\in\mathbb C\). These spaces have dimension one over \(\mathbb F\) and dimension two over \(\mathbb R\), respectively.

**Proof.** Denote the four blocks of \(T\), on \((ea,eb),(ea,fb),(fa,eb),(fa,fb)\), by \(P,Q,R,S\). Equation (M.18) for \(H\) makes \(P,S\) symmetric and gives \(R(a,b)=-Q(b,a)\). Its mixed and same-row equations for \(E\) give \(P=0\) and symmetry of \(R\); the corresponding equations for \(F\) give \(S=0\) and symmetry of \(Q\). Thus
\[
T(ea,fb)=Q(a,b),\quad T(fa,eb)=-Q(a,b),\quad
T(ea,eb)=T(fa,fb)=0,
\tag{M.19}
\]
where \(Q\) is symmetric. The orthogonal algebra's equation is
\(Q(Ma,b)+Q(a,Mb)=0\).
For \(n=1\) every symmetric \(Q\) is already a multiple of \(h\). For \(n\geq2\), insert \(M=T_{ij}\), \(a=b=w_i\), in this equation to obtain \(2d_iQ(w_j,w_i)=0\). Then insert \(a=w_i,b=w_j\) to get \(d_iQ(w_j,w_j)=d_jQ(w_i,w_i)\). All off-diagonal entries vanish and all diagonal ratios coincide. Thus \(Q=ch\), proving the assertion over either field. This argument does not require irreducibility of the orthogonal factor in dimension two.

For the realification, the same block calculation gives a symmetric real bilinear \(Q\) on \(W\) viewed as real. The equation for \(iH\), evaluated on \(ea,fb\), adds
\(Q(ia,b)=Q(a,ib)\).
Define
\[
Q_{\mathbb C}(a,b)=Q(a,b)-iQ(ia,b).
\tag{M.20}
\]
Balance shows that it is symmetric and complex bilinear: replacing either argument by \(i\) times that argument multiplies (M.20) by \(i\). Orthogonal invariance follows by applying the real invariance equation both to \((a,b)\) and \((ia,b)\); complex orthogonal operators commute with \(i\). The complex result already proved gives \(Q_{\mathbb C}=ch\), whence \(Q=\operatorname{Re}(ch)\). Formula (M.19) now gives \(T=\operatorname{Re}(c\sigma)\). Conversely these forms satisfy (M.18), since they are alternating and invariant. Nondegeneracy of \(\sigma\) makes the map \(c\mapsto\operatorname{Re}(c\sigma)\) injective: evaluate also with one argument multiplied by \(i\) to recover the imaginary part. \(\square\)

**Proposition M.5 (the entire quadratic curvature space).** Let \(\mathcal P\) be the space of symmetric bilinear maps \(\Psi:\mathfrak g^*\times\mathfrak g^*\to\Lambda^2V^*\) such that, for each \(a\), the algebra-valued alternating tensor defined by
\(\lambda(R_a(x,y))=\Psi(a,\lambda;x,y)\)
belongs to \(K(\mathfrak g)\). Then \(\mathcal P\) is the one-dimensional space generated by
\[
\Psi_0(a,\lambda;x,y)=\Phi(B^{-1}a,B^{-1}\lambda;x,y).
\tag{M.21}
\]
In particular every such tensor is invariant. For the full complex action viewed over the reals, the corresponding space is two-dimensional over \(\mathbb R\), consisting of the real parts of complex scalar multiples of (M.21), under the real identification \(Z\mapsto\operatorname{Re}B(Z,\cdot)\).

**Proof.** By M.1, a candidate \(\Psi\) uniquely determines a linear map \(C:\mathfrak g^*\to\mathfrak g^*\) with
\(\Psi(a,\lambda;x,y)=\lambda(D_{Ca}(x,y))\).
For fixed \(q\in V^*\), symmetry gives
\[
\lambda(D_{Cj(q,x)}(y,z))=q(D_{C\lambda}(y,z)x).
\tag{M.22}
\]
The cyclic sum of the right side vanishes. M.2 therefore gives a unique covector \(Fq\) with
\(Cj(q,x)=j(Fq,x)\) for every \(x\). Uniqueness also makes \(F\) linear. Evaluate this equation at \(A\in\mathfrak g\): for every \(q,x\),
\(q((C^*A)x)=q(F^*Ax)\).
Thus, as represented operators, \(C^*A=F^*A\). Set \(T=F^*\); it follows that \(T\mathfrak g\subset\mathfrak g\).

Because \(H^2=I\), write the fact \(TH\in\mathfrak g\) in blocks (M.2). It says
\[
T=\begin{pmatrix}aI+M&-bI\\cI&aI-M\end{pmatrix}.
\tag{M.23}
\]
The upper-right block of \(TE\in\mathfrak g\) is \(aI+M\), which must be scalar, so \(M\) is scalar. A scalar skew-adjoint operator for nondegenerate symmetric \(h\) is zero. The two diagonal blocks of \(TE\) are then \(0,cI\); for them to be opposite scalar blocks plus the same skew-adjoint block forces \(c=0\). Similarly the diagonal blocks of \(TF\), namely \(-bI,0\), force \(b=0\). Hence \(T=aI\) and \(C=aI\). L.5 proves that \(\Psi_0\) is symmetric, invariant and in the required space; it is nonzero because \(D\) is injective. This proves the assertion.

For realification, use M.3 and the nondegenerate real pairing \(\operatorname{Re}B\); nondegeneracy follows by testing \(Y\) and \(iY\). The same argument yields a real operator \(T\) with \(T\mathfrak g_{\mathbb R}\subset\mathfrak g_{\mathbb R}\). Now \(TH\) is complex linear and \(H^{-1}=H\) is complex linear, so \(T\) is complex linear. The block argument just given makes \(T=zI\), \(z\in\mathbb C\). Transposition under \(\operatorname{Re}B\) identifies its induced tensor with \(\operatorname{Re}(z\Phi)\). Every such tensor works by the complex contraction identity; the two real parameters are independent since the complex tensor is nonzero. \(\square\)

We next state the structure result in its full algebraic generality. This also explains exactly which facts must be checked before applying it to a representation. Let \(G\) be a connected real matrix group with faithful algebra \(\mathfrak g\subset\operatorname{End}(V)\). For \(a\in\mathfrak g^*\), put \((\delta_Aa)(B)=a([A,B])\). Assume the following four properties have been proved:

1. An equivariant linear map \(a\mapsto D_a\) is an isomorphism from \(\mathfrak g^*\) onto the entire \(K(\mathfrak g)\).
2. An equivariant homogeneous quadratic map \(Q:\mathfrak g^*\to\Lambda^2V^*\) satisfies \(dQ_a(\lambda)(x,y)=\lambda(D_a(x,y))\).
3. With \(j(q,x)(A)=q(Ax)\), the map \(q\mapsto L_q\), \(L_q(x)=D_{j(q,x)}\), is an isomorphism onto the entire \(K^1(\mathfrak g)\).
4. All bilinear solutions of \(T(x,Ay)=T(y,Ax)\) are exactly \(\mathcal I=(\Lambda^2V^*)^G\).

These are the same hypotheses whether the algebra and its dual are identified by any nondegenerate invariant pairing or left distinct. Euler differentiation gives \(Q(a)(x,y)=a(D_a(x,y))/2\). In particular the normalization of \(Q\) is fixed by the chosen \(D\).

**Theorem M.6 (complete structure equations under the four hypotheses).** Every smooth torsion-free connection reduced to such a \(G\) has, on each connected local reduced frame bundle, unique smooth functions \(a\in\mathfrak g^*\), \(q\in V^*\) and a constant \(\tau\in\mathcal I\) satisfying
\[
\begin{aligned}
d\theta&=-\omega\wedge\theta,\\
d\omega+\tfrac12[\omega,\omega]&=-\tfrac12D_a(\theta\wedge\theta),\\
da(U)&=\delta_{\omega(U)}a-j(q,\theta(U)),\\
dq(U)(y)&=q(\omega(U)y)+(Q(a)+\tau)(\theta(U),y),\\
d\tau&=0,\qquad \mathcal R=-D_a,\qquad \nabla\mathcal R=L_q.
\end{aligned}
\tag{M.24}
\]
The wedge normalization is that in J.3. Frame change is \(a(ug)=a(u)\circ\operatorname{Ad}_g\), \(q(ug)=q(u)\circ g\); \(\tau\) is invariant. Curvature is parallel on an open set if and only if \(q\) vanishes on that open set; at a single point \(\nabla\mathcal R=0\) if and only if \(q=0\) there.

**Proof.** The linear-algebra and differential identities used here do not depend on a special representation. We give them explicitly. On the local reduced bundle, \((\omega,\theta)\) is a coframe: the kernel of \(\omega\) is horizontal, the solder form identifies horizontal vectors with \(V\), and the vertical vectors are identified with \(\mathfrak g\) by \(\omega\). Write \(\xi_A,\xi_x\) for its dual fields. F.6 gives both Bianchi memberships. Hypotheses 1 and 3 therefore define unique smooth \(a,q\) by \(\mathcal R=-D_a\), \(\nabla\mathcal R=L_q\). Their fixed linear inverse maps and equivariance give
\[
\xi_Aa=\delta_Aa,\quad (\xi_Aq)(y)=q(Ay),\quad
\xi_xa=-j(q,x).
\tag{M.25}
\]
The last equation follows by differentiating \(\mathcal R=-D_a\) horizontally and using injectivity of \(D\). Torsion and curvature give exactly
\[
[\xi_A,\xi_B]=\xi_{[A,B]},\qquad
[\xi_A,\xi_x]=\xi_{Ax},\qquad
[\xi_x,\xi_y]=\xi_{D_a(x,y)}.
\tag{M.26}
\]

Put \(T(x,y)=(\xi_xq)(y)\). Apply the last bracket to \(a(B)\) and use (M.25). This gives
\(T(x,By)-T(y,Bx)=a([B,D_a(x,y)])\).
Equivariance of \(Q\), followed by hypothesis 2, gives
\[
Q(a)(x,By)-Q(a)(y,Bx)
=dQ_a(\delta_Ba)(x,y)=a([B,D_a(x,y)]).
\tag{M.27}
\]
Hypothesis 4 now says \(T-Q(a)=\tau\), with \(\tau\) taking values in the fixed finite-dimensional vector space \(\mathcal I\). Smoothness follows by choosing any basis of this space and a linear coordinate projection. Acting with a vertical field and using \([\xi_A,\xi_x]=\xi_{Ax}\) gives
\(\xi_AT(x,y)=T(Ax,y)+T(x,Ay)\).
The same equation holds for \(Q(a)\). The right side for their difference is zero by invariance of \(\tau\), so \(\xi_A\tau=0\).

Finally apply \([\xi_x,\xi_y]\) to \(q(z)\). The derivative of the quadratic terms is
\(-q(D_a(y,z)x)+q(D_a(x,z)y)\), which equals \(q(D_a(x,y)z)\) by first Bianchi. That is already the right side of the bracket equation. The remaining terms therefore satisfy
\[
(\xi_x\tau)(y,z)=(\xi_y\tau)(x,z).
\tag{M.28}
\]
At any fixed point, the left side is a trilinear tensor symmetric in \(x,y\) and skew in \(y,z\). The six interchanges in (M.8) make it zero. Thus all horizontal derivatives of \(\tau\) vanish as well. The coframe spans every tangent direction, so \(d\tau=0\); integration along coordinate segments and connectedness give constancy. No nondegeneracy or one-dimensionality of \(\mathcal I\) was needed. All of (M.24) and uniqueness now follow. The two parallel-curvature assertions follow from injectivity of \(q\mapsto L_q\). \(\square\)

**Theorem M.7 (analytic germs and the converse at every parameter).** Under the same four hypotheses, every such smooth connection is locally real analytic in suitable coordinates. Its germ at a specified reduced frame is determined by \((a,q,\tau)\) at that frame, and hence by \(\mathcal R,\nabla\mathcal R,\nabla^2\mathcal R\) there. Every triple \((a_0,q_0,\tau_0)\in\mathfrak g^*\times V^*\times\mathcal I\) occurs in a real-analytic local connection. The converse includes points where the associated Poisson rank changes.

**Proof.** Fix bases of the three parameter spaces and of \(\mathfrak g\oplus V\). The brackets (M.26) have coefficients polynomial in \(a\). Equations (M.25) and (M.24) give polynomial parameter derivatives along the dual coframe:
\[
\begin{aligned}
\rho_A(a,q,\tau)&=(\delta_Aa,\ q\circ A,\ 0),\\
\rho_x(a,q,\tau)&=(-j(q,x),\ (Q(a)+\tau)(x,\cdot),\ 0).
\end{aligned}
\tag{M.29}
\]
The complete coframe theorem J.4 applies: ordered flows determine parameter values by their analytic ordinary differential equations, and determine the coframe coefficients by the linear transport equations with these parameter values. Its proof supplies convergent analytic charts even when the original data are merely smooth. It also supplies a unique local coframe equivalence for equal initial parameters. No rank hypothesis occurs in that argument.

The vertical subbundle \(\theta=0\) is analytic and involutive by (M.26). The analytic Frobenius theorem proved in I.2 gives local analytic quotient coordinates and an analytic transversal. Pulling back \(\theta,\omega\) to this transversal gives an analytic invertible coframe and its analytic connection matrices. Solving for the coordinate Christoffel coefficients uses only matrix inversion, so they are analytic. A coframe equivalence preserves the vertical subbundle and the connection and solder forms, and therefore descends to a connection equivalence sending the specified frame to the other one. This proves the germ and analyticity assertions.

For existence fix \(\tau_0\). The map \(\phi=Q+\tau_0\) is equivariant and its derivative transpose is \(D_a\in K(\mathfrak g)\). It is admissible in I.9, whose full Jacobi proof makes its coordinate bracket Poisson. The all-point symplectic realization I.7 and the quotient construction I.10 apply at \((a_0,q_0)\), giving an analytic torsion-free local connection with curvature \(-D_{a_0}\) and derivative \(L_{q_0}\). These theorems were proved without constant rank. On its integral frame manifold, the Hamiltonian brackets give horizontal derivative \(\xi_xq=\phi(a)(x,\cdot)\); comparison with M.6 recovers exactly \(\tau_0\). Thus the construction realizes the prescribed triple, rather than just its first two components. A connection already given with that triple is equivalent to the constructed one by the coframe determination just proved.

For the curvature-jet assertion, first recover \(a\) from \(-\mathcal R\) with \(D^{-1}\), then \(q\) from \(\nabla\mathcal R\) with \(L^{-1}\). Equivariance of the fixed linear map \(L\) makes it parallel on associated bundles. Consequently
\[
\nabla_x(\nabla\mathcal R)=L_{\nabla_xq},\qquad
T(x,y)=(\nabla_xq)(y),\qquad \tau=T-Q(a).
\tag{M.30}
\]
Here \(\nabla^2\mathcal R\) is the unsymmetrized second covariant derivative, and all tensor slots are retained. Apply \(L^{-1}\) in (M.30) to recover \(T\) and then \(\tau\). This proves the final assertion. \(\square\)

**Theorem M.8 (complete equations for both infinite families).** The four hypotheses hold for every real tensor family of L.1 with \(n\geq3\), and for the full complex tensor family viewed over the reals. For the real family,
\[
\mathcal I=\mathbb R\sigma,\quad \tau=c\sigma,\quad
Q(a)=\tfrac12\Phi(B^{-1}a,B^{-1}a).
\tag{M.31}
\]
For the complex family viewed over the reals, \(\mathcal I=\{\operatorname{Re}(c\sigma):c\in\mathbb C\}\), the algebra-dual identification is by \(B_{\mathbb R}=\operatorname{Re}B\), and the quadratic map is the real part of the complex map in (M.31). Every smooth connection reduced to these groups has exactly (M.24), is locally real analytic, is determined at a specified frame by its first three curvature tensors as in M.30, and is obtained locally by the all-point Poisson construction for its parameter triple.

**Proof.** In the real family, M.1, L.5, M.2 and M.4 prove hypotheses 1–4 respectively. Invariance under the connected group follows either directly from the tensor formulas or, for a bilinear form, by differentiating its pullback along a group path: its derivative is zero, so its value equals that at the identity. Such paths are finite concatenations of exponential-chart paths, since the subgroup they generate is open and its cosets partition a connected group. The form description in M.4 is therefore exactly \(\mathcal I\).

For realification, \(B_{\mathbb R}\) is nondegenerate as in M.5. Every real covector on a complex vector space is the real part of a unique complex-linear covector: for a real covector \(r\) that covector is \(x\mapsto r(x)-ir(ix)\), as direct substitution verifies. M.3 identifies the whole curvature and derivative spaces. Under these identifications the real versions of \(D,j,L\) are exactly the restrictions of their complex versions followed by the real dual pairing. The derivative identity for \(\operatorname{Re}Q\) follows by taking the real part of the complex identity. M.4 proves the last hypothesis and the full two-dimensional invariant space. Thus M.6 and M.7 apply to both families in their entirety. L.7 additionally supplies holomorphic representatives for complex parameters, with complex base dimension \(2n\), hence real dimension \(4n\). The local classification here needs no assumption that a chosen parameter yields full holonomy; L.4 and L.7 separately give explicit parameters that do. \(\square\)

**Exercise M.9 (surjectivity, scalar recovery and pointwise parallelness).** Explain why an injective curvature family with one full-span tensor does not establish M.8. Give a basis-free recovery of its constant parameter from curvature jets. Construct a realized connection for which \(\nabla\mathcal R=0\) at one point but curvature is not parallel on any neighbourhood of that point.

**Solution.** Injection and a full-span value give an algebraic family and, with I.10–I.11, actual full-holonomy examples. They do not state that an arbitrary element of \(K\) lies in the family, nor determine the whole \(K^1\). Those onto assertions require M.1 and M.2; after realification they also require M.3. Without them, one cannot define \(a,q\) for every reduced connection as in M.6.

Recover \(a,q,T,\tau\) by M.30. In the real case, for any bilinear form \(b\) write \(b^\flat x=b(x,\cdot)\). With \(m=\dim_{\mathbb R}V=2n\),
\[
c=\frac1m\operatorname{tr}\bigl((\sigma^\flat)^{-1}\tau^\flat\bigr).
\tag{M.32}
\]
Indeed the operator inside the trace is \(cI\). A reduced-frame change conjugates this operator, and cyclic invariance of trace proves that the answer is independent of that frame. In the realified complex case put \(\Omega=\operatorname{Re}\sigma\), let \(Jx=ix\), and set \(C=(\Omega^\flat)^{-1}\tau^\flat\). If \(c=a+ib\), then \(C=aI+bJ\). In a real basis \(v_1,iv_1,\ldots,v_{2n},iv_{2n}\), \(J\) has trace zero and \(J^2=-I\). Hence, with \(m=4n\),
\[
c=\frac{\operatorname{tr}C}{m}
       -i\frac{\operatorname{tr}(JC)}{m}.
\tag{M.33}
\]
Reduced-frame changes also preserve \(J\), proving invariance of both traces.

Finally take \(a_0=0,q_0=0,\tau_0=\sigma\) in a real family, or \(\tau_0=\operatorname{Re}\sigma\) in a realified complex family. M.7 realizes these exact parameters. At the specified point \(\mathcal R=0\) and \(\nabla\mathcal R=0\). But (M.24) and homogeneity give \((\nabla_xq)(y)=\tau_0(x,y)\) there, so
\[
\nabla_x(\nabla\mathcal R)=L_{\tau_0(x,\cdot)}\ne0
\quad\hbox{for every nonzero }x.
\tag{M.34}
\]
The inequality follows from nondegeneracy of \(\tau_0\) and injectivity in M.2 or M.3. An identically zero \(\nabla\mathcal R\) on a neighbourhood would have zero derivative there, a contradiction. Thus a pointwise vanishing first derivative is strictly weaker than parallel curvature on a neighbourhood. \(\square\)

The free construction source for this part is Quo-Shin Chi, Sergey A. Merkulov and Lorenz J. Schwachhöfer, *On the Existence of Infinite Series of Exotic Holonomies*, author preprint dated 9 April 1996, [exact freely accessible author PDF](https://wwwold.mathematik.tu-dortmund.de/~lschwach/papers/Berger/InfExoticHol.pdf), especially the tensor formulas and admissible-map/structure equations on PDF pages 5–6 and 9–13. M.1–M.5 supply complete coefficient and symmetry proofs here; source references to outside cohomology, classification or unproved linear algebra are not proof providers. M.6–M.9 use the complete local realization and coframe proofs already given in I.1–I.10 and J.4. No source prose, source PDF or third-party proof is reproduced. The normalization of every displayed equation is the explicitly verified pairing and curvature map of Part L.
