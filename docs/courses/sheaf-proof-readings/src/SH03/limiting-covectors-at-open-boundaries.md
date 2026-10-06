# Limiting covectors at open boundaries

Extending a sheaf across an open boundary can create singular directions. The new direction need not be the sum of two convergent covectors: their bases may approach one another while their lengths tend to infinity. We first isolate the error estimate that makes such cancellation meaningful. We then move the boundary into the region where the sheaf is already defined, pass to the actual extension functors, and finally treat the trace across a missing submanifold.

Let \(k\) be a commutative ring and let the manifolds be finite dimensional, Hausdorff and countable at infinity. All complexes in the extension and trace statements belong to \(D^+(k_X)\) or the indicated open subspace; they are bounded below, and their stalk modules need not be finite or perfect. Smooth charts suffice, and the coordinate estimates below are invariant under \(C^2\) changes. We use the noncharacteristic extension bounds and uniform directional localization, the two extension-continuity calculations, and the proper-image and closed-embedding support tests. Each has its proof in the linked reading.

## Cancellation with a controlled base error {#limiting-sum-sequences}

For two conic sets \(A,B\subset T^*X\), define their limiting sum in a coordinate chart by

\[
(x;\xi)\in A\widehat+ B
\iff
\begin{cases}
(x_n;\alpha_n)\in A,\quad(y_n;\beta_n)\in B,\\
x_n,y_n\longrightarrow x,\quad\alpha_n+\beta_n\longrightarrow\xi,\\
|x_n-y_n|\,|\alpha_n|\longrightarrow0.
\end{cases}
\tag{L1}
\]

The sets need not be closed in the whole cotangent bundle. In particular \(A\) may be a microsupport defined only over an open subset. Since the sums in (L1) are bounded, the inequality \(|\beta_n|\leq|\alpha_n|+|\alpha_n+\beta_n|\) shows that the last condition is equivalent to the one with \(\beta_n\). Interchanging the inputs proves symmetry. Constant witnesses give the ordinary same-base sum as a subset. Multiplying both input covectors by a positive constant proves conicity.

The resulting set is closed. Indeed, given points of the limiting sum converging to \((x;\xi)\), select from a witness for the \(m\)-th point one pair with each base error, sum error and weighted product less than \(1/m\). Those selected pairs witness membership at the limit. This argument also handles zero output covectors. Local equivalence of norms makes the definition independent of the particular norms used.

Here is the coordinate check, including the large terms. If \(h\) changes base coordinates, put \(Q(x)=Dh_x^{-T}\). On a smaller relatively compact chart, \(h,Q\) are Lipschitz and the matrices are bounded. The transformed sum equals

\[
Q(x_n)\alpha_n+Q(y_n)\beta_n
=Q(y_n)(\alpha_n+\beta_n)
 +(Q(x_n)-Q(y_n))\alpha_n.
\tag{L2}
\]

The last summand has norm at most \(C|x_n-y_n||\alpha_n|\), hence tends to zero. The transformed weighted product is bounded by a constant times the original one. Thus (L1) transforms by the cotangent map at \(x\); applying the same argument to \(h^{-1}\) proves the converse. A locally Lipschitz derivative is the precise regularity used here; \(C^2\) charts provide it. Mere convergence of the two bases would not control the error in (L2).

## Inward directions and the two signs {#inward-directions}

For an open set \(\Omega\), an inward direction at \(x\) is a vector having an open cone of nearby directions whose sufficiently short translations take nearby points of \(\Omega\) into \(\Omega\). Denote the open convex cone of these directions by \(D_x(\Omega)\). This is the local translation definition proved in the boundary-cone calculation. Its positive polar is

\[
N_x^*(\Omega)=\{\eta:\langle w,\eta\rangle\geq0
\text{ for every }w\in D_x(\Omega)\}.
\tag{L3}
\]

The normal cone has closed graph; at an interior point it is \(\{0\}\). When there are no inward directions, the polar is the full cotangent fibre. We retain the zero covectors in this notation. Superscript \(a\) will mean fibrewise negation.

Suppose \(\epsilon\in\{1,-1\}\) and \(\xi_0\notin\epsilon N_{x_0}^*(\Omega)\). By the defining polar inequality there is an inward vector \(v\) with \(\epsilon\langle v,\xi_0\rangle<0\). Choose a thin closed pointed cone \(C\), with nonempty interior and \(v\in\operatorname{Int}C\), whose nonzero directions lie in \(D_{x_0}(\Omega)\). Compactness of its unit section gives a common neighborhood and a common translation length. After shrinking, \(\Omega\) is locally invariant under \(C\), all nearby normals belong to \(C^\circ\), and

\[
\langle v,\eta\rangle\geq c_0|\eta|,
\qquad \eta\in N_y^*(\Omega),\qquad c_0>0.
\tag{L4}
\]

To see the strict bound, place a ball of radius \(c_0\) about \(v\) inside \(C\) and pair \(v-c_0\eta^\sharp/|\eta|\) with \(\eta\). A positive translation along \(v\) takes nearby closure points of \(\Omega\) into \(\Omega\) as well: approximate a closure point by interior points; their errors can be absorbed into a small ball of directions about \(v\). All translations in this assertion stay in the selected chart.

## Move the boundary, keeping both signs {#moving-boundary-separation}

Let \(A\subset T^*X|_\Omega\) be conic and assume

\[
(x_0;\xi_0)\notin A\widehat+\epsilon N^*(\Omega),
\qquad \xi_0\ne0,
\qquad \epsilon\langle v,\xi_0\rangle<0.
\tag{L5}
\]

Use nested balls \(B_0\Subset B_1\) about \(x_0\) inside the translation chart. For small positive \(s,t\), define

\[
\begin{aligned}
\ell(x)&=\langle x-x_0,\xi_0\rangle,&h_s(x)&=s+\epsilon\ell(x),\\
\phi_{t,s}(x)&=x-t h_s(x)v,& Z_s&=B_0\cap\{h_s>0\},\\
\Omega_{t,s}&=Z_s\cap\phi_{t,s}^{-1}(\Omega).
\end{aligned}
\tag{L6}
\]

Choose the parameter range so that \(\phi_{t,s}(B_0)\subset B_1\). Put \(d=1-\epsilon t\langle v,\xi_0\rangle>0\). Direct substitution gives

\[
D\phi_{t,s}=I-\epsilon t(v\otimes\xi_0),\quad
\det D\phi_{t,s}=d,\quad
h_s\circ\phi_{t,s}=d h_s,\quad
\phi_{t,s}^{-1}(y)=y+\frac{t}{d}h_s(y)v.
\tag{L7}
\]

Thus this is an affine diffeomorphism, and every point of the closure of \(\Omega_{t,s}\) relative to \(Z_s\) lies in \(\Omega\): its image under \(\phi_{t,s}\) is in \(\overline\Omega\), and the inverse adds a positive strict inward translation. If \(0<t'<t\), the images of a fixed \(x\in Z_s\) differ by the inward vector \((t-t')h_s(x)v\). Consequently

\[
\Omega_{t,s}\subset\Omega_{t',s}\subset\Omega\cap Z_s,
\qquad \bigcup_{t>0\text{ small}}\Omega_{t,s}=\Omega\cap Z_s.
\tag{L8}
\]

For the union, openness of \(\Omega\) puts each fixed point in all sufficiently small members. Only relative closures and normals inside \(Z_s\) will be used. In particular artificial boundaries of \(B_0\) or \(\{h_s>0\}\) do not enter the argument.

At \(x\in Z_s\), write \(y=\phi_{t,s}(x)\). The polar of the inward cone transforms by the transpose derivative. Hence

\[
\theta\in N_x^*(\Omega_{t,s})
\iff
\theta=\eta-\epsilon t\langle v,\eta\rangle\xi_0,
\quad \eta\in N_y^*(\Omega).
\tag{L9}
\]

There are neighborhoods \(V\subset B_0\) of \(x_0\), \(W\) of \(\xi_0\), and \(\delta>0\), independent of \(s,t\), such that for \(0<s,t<\delta\), over \(V\cap Z_s\),

\[
\begin{aligned}
A\cap(\epsilon N^*(\Omega_{t,s}))^a&\subset T_X^*X,\\
(A+\epsilon N^*(\Omega_{t,s}))\cap((V\cap Z_s)\times W)&=\varnothing.
\end{aligned}
\tag{L10}
\]

Here is a proof of both assertions that does not bound the input covectors. If no common choices worked, a sequence of smaller neighborhoods and parameters would give \(x_n\to x_0\), \(s_n,t_n\to0\), and \(\alpha_n\in A_{x_n}\), \(\theta_n\in N_{x_n}^*(\Omega_{t_n,s_n})\) with either
\(\alpha_n+\epsilon\theta_n=0\) nontrivially, or \(\alpha_n+\epsilon\theta_n=\beta_n\to\xi_0\). Pass to one of the two alternatives and denote it by \(c=0\) or \(c=1\). If \(\theta_n=0\) in the second alternative along a subsequence, pairing \(\alpha_n=\beta_n\) with the zero normal at \(x_n\) already contradicts (L5). We may therefore assume \(\theta_n\ne0\) in both alternatives.

Apply (L9), obtaining \(y_n\) and \(\eta_n\ne0\), and set

\[
\rho_n=\alpha_n+\epsilon\eta_n
=c\beta_n+a_n\xi_0,
\qquad a_n=t_n\langle v,\eta_n\rangle>0.
\tag{L11}
\]

For \(c=0\), this has exactly the positive direction \(\xi_0\). For \(c=1\), rewrite it as \((1+a_n)\xi_0+(\beta_n-\xi_0)\). It follows in both cases that, for large \(n\),

\[
\frac{\rho_n}{|\rho_n|}\longrightarrow\frac{\xi_0}{|\xi_0|},
\qquad |\rho_n|\geq c_1 t_n|\eta_n|,
\qquad c_1>0.
\tag{L12}
\]

For example, in the second case \(|\beta_n-\xi_0|\leq|\xi_0|/2\) implies \(|\rho_n|\geq(1/2+a_n)|\xi_0|\); combine this with (L4). Since \(|x_n-y_n|=t_n h_{s_n}(x_n)|v|\),

\[
\frac{|x_n-y_n||\eta_n|}{|\rho_n|}
\leq \frac{|v|}{c_1}h_{s_n}(x_n)\longrightarrow0,
\qquad
\frac{|x_n-y_n||\alpha_n|}{|\rho_n|}\longrightarrow0.
\tag{L13}
\]

The second limit follows from \(\alpha_n=\rho_n-\epsilon\eta_n\) and \(|x_n-y_n|\to0\). Conicity now lets us divide both covectors by \(|\rho_n|\). Equations (L12)–(L13) are witnesses for \((x_0;\xi_0/|\xi_0|)\) in the forbidden limiting sum. Conicity contradicts (L5). This proves (L10). The reflected height \(s+\epsilon\ell\) is what makes the coefficient \(a_n\) positive for both extension signs.

## The full open-extension estimates {#arbitrary-open-extensions}

For an arbitrary open inclusion \(j:\Omega\hookrightarrow X\) and \(F\in D^+(k_\Omega)\), put \(A=\operatorname{SS}(F)\), viewed only over \(\Omega\). Then

\[
\operatorname{SS}(Rj_*F)\subset A\widehat+N^*(\Omega),
\qquad
\operatorname{SS}(j_!F)\subset A\widehat+N^*(\Omega)^a.
\tag{L14}
\]

Extension by zero is exact, so \(j_!\) needs no derived replacement. No properness of \(j\), constructibility or finiteness of stalks is assumed.

Both extensions vanish off \(\overline\Omega\) and agree with \(F\) inside \(\Omega\). At a boundary point outside their closed support they vanish locally. At a remaining boundary point \(x_0\), points in the support of \(F\) approach \(x_0\). Their zero covectors belong to \(A\). Pairing those zero covectors with any fixed \(\epsilon N_{x_0}^*(\Omega)\) shows that this entire signed cone belongs to the right side of (L14). In particular zero output covectors are accounted for. It is enough to exclude a nonzero \(\xi_0\) outside that right side.

Take \(\epsilon=1\) for \(Rj_*\), \(\epsilon=-1\) for \(j_!\). Since \(\xi_0\notin\epsilon N_{x_0}^*(\Omega)\), the preceding inward-cone construction and (L10) apply. Fix a sufficiently small \(s>0\), so \(Z_s\) is an actual neighborhood of \(x_0\), and let \(j_{t,s}:\Omega_{t,s}\hookrightarrow Z_s\). Define

\[
K_t=\begin{cases}
Rj_{t,s*}(F|_{\Omega_{t,s}}),&\epsilon=1,\\
j_{t,s!}(F|_{\Omega_{t,s}}),&\epsilon=-1.
\end{cases}
\tag{L15}
\]

At every relevant relative boundary point, \(F\) is defined on a neighborhood, because \(\overline{\Omega_{t,s}}^{\,Z_s}\subset\Omega\). The pointwise noncharacteristic estimates therefore apply to this actual local ambient complex. The first line of (L10) supplies their hypothesis; the second excludes the chosen covector window. At interior points the same exclusion follows by adding the zero normal. Outside the relative closure the extension vanishes. Thus

\[
\operatorname{SS}(K_t)\cap((V\cap Z_s)\times W)=\varnothing
\quad\text{for every sufficiently small }t>0.
\tag{L16}
\]

For ordinary extension, first choose a closed pointed cone \(C'\) such that \(\xi_0\in\operatorname{Int}(C')^-\) and \((C')^-\setminus\{0\}\subset\mathbb R_{>0}W\), where the negative polar means \(\langle c,\eta\rangle\leq0\). Such a cone is the negative polar of a sufficiently narrow closed covector cone about \(\xi_0\); the bipolar theorem and a strict angular margin give the stated properties. Conicity converts (L16) into avoidance on the entire interior negative polar. Let \(\iota:Z_s\hookrightarrow E\) be inclusion in the full coordinate vector space and set \(\widetilde K_t=R\iota_*K_t\). These are one coherent full-chart tower, agreeing with \(K_t\) on \(Z_s\). Use uniform directional localization to choose one relatively compact lens \(S\), with \(x_0\in\operatorname{Int}S\) and \(\overline S\subset V\cap Z_s\), such that

\[
Rq_{C'*}\mathcal L_S\widetilde K_t=0
\quad\text{for all small }t.
\tag{L17}
\]

Here \(q_{C'}\) passes to the directional topology and \(\mathcal L_S=R\mathcal Hom(k_S,-)\) is the supported localization used in that proof. The compact lens has a neighborhood inside \(Z_s\), where \(\widetilde K_t\) agrees with the actual extension (L15).

Choose \(t_n\downarrow0\). Equation (L8) gives an increasing exhaustion of \(\Omega\cap Z_s\). The actual injective-resolution comparison J1 in the linked continuity proof identifies

\[
Rj_*F|_{Z_s}\simeq\operatorname{holim}_n K_{t_n}.
\tag{L18}
\]

All these objects have the common lower bound of \(F\). The right adjoint \(\iota_*\) preserves injectives and products, because its left adjoint is exact. The same bounded-below injective product-and-fibre calculation as P17 consequently gives \(\operatorname{holim}_n\widetilde K_{t_n}\simeq R\iota_*(Rj_*F|_{Z_s})\). Applying P17 to the fixed functor \(Rq_{C'*}\mathcal L_S\) and this coherent tower carries (L17) through the limit. Its value is zero. The localized limit agrees with \(Rj_*F\) near \(x_0\), and \(\xi_0\in\operatorname{Int}(C')^-\); the cone-to-support-test implication therefore excludes \((x_0;\xi_0)\). This uses one vanishing localized object before taking products, not an interchange of a stalk with arbitrary products.

For extension by zero, use the uniform compact-cap theorem on (L16). It supplies a single cap geometry, with compact cap \(K_x\) and closed base \(L_x\) inside \(V\cap Z_s\), for every vertex \(x\) near \(x_0\), such that

\[
H^q(K_x;K_t)\xrightarrow{\sim}H^q(L_x;K_t)
\quad\text{for every }q\text{ and every small }t.
\tag{L19}
\]

By J2, the direct limits of the two sides along \(t_n\downarrow0\) are the corresponding groups of \(j_!F\). These identifications commute with the actual cap-to-base restriction map, since both are made using compact supports and extension by zero. Exactness of filtered colimits preserves the isomorphism. The converse cap test now excludes \((x_0;\xi_0)\) from \(\operatorname{SS}(j_!F)\). This proves the second estimate directly, without using biduality to impose a finiteness condition.

## Adding a full conormal {#full-conormal-sequence}

Let \(M\) be a closed smooth submanifold, with adapted coordinates \((u,z)\) and \(M=\{u=0\}\). Write cotangent coordinates as \((u,z;a,b)\), where \(b\) is tangential to \(M\). For conic \(A\), define \(Z_M(A)\subset T^*M\) by

\[
(z_0;b_0)\in Z_M(A)
\iff
\begin{cases}
(u_n,z_n;a_n,b_n)\in A,\\
u_n\to0,\quad z_n\to z_0,\quad b_n\to b_0,\\
|u_n||a_n|\to0.
\end{cases}
\tag{L20}
\]

If \(\rho:T^*X|_M\to T^*M\) is restriction of covectors, then

\[
A\widehat+T_M^*X=\rho^{-1}Z_M(A).
\tag{L21}
\]

For necessity, a conormal input has base \((0,w_n)\) and covector \((c_n,0)\). The limiting sum forces \(b_n\to b_0\), while the base separation is at least \(|u_n|\). Thus its weighted condition implies (L20). Conversely, for any prescribed final normal component \(a_0\), pair the witness in (L20) with \((0,z_n;a_0-a_n,0)\). The sum is \((a_0,b_n)\), and the required product is bounded by \(|u_n||a_n|+|u_n||b_n|\to0\). This proves equality for every \(a_0\); one must not demand that the normal input sequence be bounded.

The tangential condition is intrinsic. For completeness, write an inverse adapted coordinate change as \((u,z)=(P(u',z'),Q(u',z'))\), with \(P(0,z')=0\). Covectors transform by

\[
\begin{aligned}
a'&=D_{u'}P^t a+D_{u'}Q^t b,\\
b'&=D_{z'}P^t a+D_{z'}Q^t b.
\end{aligned}
\tag{L22}
\]

The normal coordinates have comparable size near \(M\). Moreover \(D_{z'}P(0,z')=0\), so \(|D_{z'}P(u',z')|\leq C|u'|\). Bounded derivatives and the same estimate for \(Q\) give

\[
|u'||a'|\leq C|u|(|a|+|b|),
\qquad
b'-D_{z'}Q(0,z')^t b=O\bigl(|u'|(|a|+|b|)\bigr).
\tag{L23}
\]

Both errors tend to zero for a sequence in (L20). The limiting tangential covector therefore transforms by exactly the cotangent change on \(M\). Applying the inverse change proves equivalence.

## The same condition as a normal-cone slice {#normal-cone-slice}

Set \(\Lambda=T_M^*X\). In \(T^*X\), this is the submanifold \(u=b=0\). Its normal bundle has coordinates \((v,z;\alpha,\zeta)\), where \((0,z;\alpha,0)\) is the base in \(\Lambda\) and \((v,\zeta)\) are the normal components. By definition, the normal cone \(C_\Lambda(A)\) consists of the limits

\[
\begin{gathered}
(u_n,z_n;c_n,d_n)\in A,\quad r_n\longrightarrow+\infty,\\
(z_n,c_n)\longrightarrow(z,\alpha),\qquad
(r_nu_n,r_nd_n)\longrightarrow(v,\zeta).
\end{gathered}
\tag{L24}
\]

This coordinate definition of the normal bundle and cone is invariant under a \(C^1\) ambient diffeomorphism: subtract its value on the nearby submanifold, use the first-order expansion in the normal variable, and multiply by \(r_n\); the remainder is \(o(|(u_n,d_n)|)\), whose scaled value tends to zero because \(r_n(u_n,d_n)\) converges. Cotangent changes induced by \(C^2\) base changes have this regularity.

Identify \(T^*M\) with the locus \(v=\alpha=0\) in this normal bundle. This identification has the usual cotangent sign. With symplectic convention \(\omega=d(\sum\xi_jdx_j)\), inverse contraction sends \(\lambda\,dx+\mu\,d\xi\) to \(\lambda\,\partial_\xi-\mu\,\partial_x\). The covector \(-v\,da+\zeta\,dz\) on \(\Lambda\) consequently gives normal vector \(v\,\partial_u+\zeta\,\partial_b\). In particular the tangential component is \(\zeta\), with no antipodal change.

We claim

\[
Z_M(A)=T^*M\cap C_{T_M^*X}(A).
\tag{L25}
\]

Starting with (L20), put

\[
s_n=|u_n|(1+|a_n|),\qquad
r_n=\frac{1+|a_n|}{\sqrt{s_n+1/n}}.
\tag{L26}
\]

Then \(s_n\to0\), \(r_n\to\infty\), \(|a_n|/r_n\leq\sqrt{s_n+1/n}\to0\), and \(r_n|u_n|\leq\sqrt{s_n}\to0\). Conicity puts \((u_n,z_n;a_n/r_n,b_n/r_n)\) in \(A\). Equation (L24) now gives exactly \((v,z;\alpha,\zeta)=(0,z_0;0,b_0)\). Conversely, given (L24) with \(v=\alpha=0\), multiply its covectors by \(r_n\). The resulting \(a_n=r_nc_n\), \(b_n=r_nd_n\) satisfy (L20), since \(|u_n||a_n|=|r_nu_n||c_n|\to0\). This proves (L25), including unbounded normal covectors and zero limits.

## The trace across a missing submanifold {#missing-submanifold-trace}

Let \(U=X\setminus M\), with inclusions \(j:U\hookrightarrow X\) and \(i:M\hookrightarrow X\). For \(F\in D^+(k_U)\) and \(A=\operatorname{SS}(F)\),

\[
\begin{aligned}
\operatorname{SS}(Rj_*F)\cap T^*X|_M&\subset A\widehat+T_M^*X,\\
\operatorname{SS}(j_!F)\cap T^*X|_M&\subset A\widehat+T_M^*X,\\
\operatorname{SS}(i^{-1}Rj_*F)&\subset T^*M\cap C_{T_M^*X}(A).
\end{aligned}
\tag{L27}
\]

The first two are estimates in the ambient cotangent bundle. The last concerns the actual trace complex on \(M\). For a selected side of a hypersurface, (L14) retains finer sign information.

Work on an adapted coordinate domain \(W\subset\mathbb R^r_u\times\mathbb R^m_z\). If \(r=0\), the complement is locally empty and all three assertions vanish. For \(r>0\), take the doubled real blowup

\[
\begin{aligned}
B_W&=\{(\theta,t,z)\in S^{r-1}\times\mathbb R\times\mathbb R^m:
(t\theta,z)\in W\},\\
\beta(\theta,t,z)&=(t\theta,z),\quad
B_+=B_W\cap\{t>0\},\quad D=B_W\cap\{t=0\}.
\end{aligned}
\tag{L28}
\]

Allowing both signs of \(t\) makes \(B_W\) a manifold without boundary. The map \(h=\beta|_{B_+}\) is a diffeomorphism onto \(W\setminus M\), with inverse \((u,z)\mapsto(u/|u|,|u|,z)\). Also \(\beta\) is proper: the inverse image of a compact \(K\subset W\) is closed in the compact set \(S^{r-1}\times[-R,R]\times\operatorname{pr}_zK\), where \(R=\max_K|u|\), and lies entirely in \(B_W\). Source and target are restricted together; no improper truncation of the source is being made. In rank one the sphere is \(S^0\), so the construction still sees both sides.

Let \(G=h^{-1}(F|_{W\setminus M})\), and let \(k:B_+\hookrightarrow B_W\). Ordinary composition, and proper-support composition for the second comparison, give the canonical identifications

\[
R\beta_*Rk_*G\simeq Rj_*F|_W,
\qquad R\beta_*k_!G\simeq j_!F|_W.
\tag{L29}
\]

In the second comparison \(R\beta_*=R\beta_!\) by properness; \(\beta k=jh\), and the diffeomorphism \(h\) cancels its inverse image. These are the actual composition maps supplied in the proper-support proof, not a fibre substitution for the nonproper map \(j\).

Apply (L14) on \(B_W\). At the hypersurface \(D\), either signed half-normal is contained in \(T_D^*B_W\), so the microsupport of each extension in (L29) is bounded there by \(\operatorname{SS}(G)\widehat+T_D^*B_W\). The proper-image microsupport theorem implies that an ambient covector \((0,z_0;a_0,b_0)\) in either left side of (L27) has a lift, for some \(\theta_0\), satisfying

\[
(\theta_0,0,z_0;0,\langle\theta_0,a_0\rangle,b_0)
\in\operatorname{SS}(G)\widehat+T_D^*B_W.
\tag{L30}
\]

The sphere component is zero because \(d\beta\) on a sphere-tangent vector is multiplied by \(t=0\). Zero pulled-back covectors remain allowed; the proper-image theorem includes them.

Use (L20)–(L21), with normal coordinate \(t\), to express (L30). There are \((\theta_n,t_n,z_n;\lambda_n,\tau_n,b_n)\in\operatorname{SS}(G)\), with \(t_n>0\), \((\theta_n,t_n,z_n)\to(\theta_0,0,z_0)\), \(\lambda_n\to0\), \(b_n\to b_0\), and \(t_n|\tau_n|\to0\). Diffeomorphism covariance, obtained directly by composing the local support-test functions with \(h\) and \(h^{-1}\), gives \((t_n\theta_n,z_n;a_n,b_n)\in A\) with

\[
\lambda_n=t_n a_n|_{T_{\theta_n}S^{r-1}},\qquad
\tau_n=\langle\theta_n,a_n\rangle,\qquad
t_n^2|a_n|^2=|\lambda_n|^2+t_n^2|\tau_n|^2\longrightarrow0.
\tag{L31}
\]

The last identity uses the Euclidean orthogonal decomposition into sphere-tangent and radial covectors. Sphere-coordinate norms are uniformly equivalent to this metric near \(\theta_0\). In rank one the first component is absent and the identity still holds. Thus \(u_n=t_n\theta_n\) satisfies \(|u_n||a_n|\to0\), proving the ambient assertions of (L27) by (L21). Both the radial and sphere estimates are necessary to control arbitrary growth of \(a_n\).

For every sheaf \(Q\) the sequence \(0\to j_!j^{-1}Q\to Q\to i_*i^{-1}Q\to0\) is exact on stalks: over \(U\) the first map is the identity, and over \(M\) the second is the identity. All four functors in its outer terms are exact. Applying this degreewise therefore gives the canonical open–closed localization triangle for complexes. Apply it to \(Rj_*F\), whose restriction to \(U\) is \(F\), to obtain

\[
j_!F\longrightarrow Rj_*F\longrightarrow
i_*i^{-1}Rj_*F\xrightarrow{+1}.
\tag{L32}
\]

The first map is the adjunction map corresponding to the identity of \(F\); the second is restriction to the closed submanifold. The triangle inequality for microsupport bounds the third term by the union of the first two. Since it is supported on \(M\), the ambient estimates apply everywhere it can have microsupport. The exact closed-embedding formula identifies its microsupport with \(\rho^{-1}\operatorname{SS}(i^{-1}Rj_*F)\). The surjective map \(\rho\), (L21), and (L25) give the final trace bound. If \(M\) is empty there is no boundary to estimate, and the trace complex is zero.

## Products, restriction, and the limiting sum {#limiting-tensor-estimate}

We now turn the boundary trace into an estimate for tensor products. The key is to realize ordinary restriction as a trace from a punctured cylinder. First we prove the external-product estimate, keeping the actual compact restriction maps. Then the cylinder argument and a diagonal coordinate calculation supply the limiting sum.

In this section, assume that the commutative ring \(k\) has finite global dimension \(d\), and take bounded complexes with arbitrary stalk modules. No constructibility, finite generation, perfection, or noncharacteristic condition is imposed. These hypotheses ensure that every derived tensor used here is bounded. The preceding extension and trace arguments retain their stated bounded-below scope over an arbitrary commutative ring.

### Coefficients on a compact cap {#compact-cap-tensor-comparison}

For manifolds \(X,Y\), with projections \(q_X,q_Y\), set

\[
F\boxtimes^L G=q_X^{-1}F\otimes_k^L q_Y^{-1}G,
\qquad
F\in D^{[a,b]}(k_X),\quad G\in D^{[c,e]}(k_Y).
\tag{Q1}
\]

The finite flat replacement gives a flat model for \(F\) in degrees \([a-d,b]\). Inverse image preserves flatness: its stalks are the corresponding original flat stalks. Tensoring with a bounded representative for the second factor therefore gives

\[
F\boxtimes^L G\in D^{[a+c-d,b+e]}(k_{X\times Y}),
\qquad
s_y^{-1}(F\boxtimes^L G)
\simeq F\otimes_k^L(G_y)_X,
\tag{Q2}
\]

where \(s_y(x)=(x,y)\). The second identification is the exact, monoidal inverse-image comparison on these flat models. It does not use a microsupport estimate for inverse images.

Let \(Q\) be compact in a coordinate vector space \(E\), take \(F\in D^b(k_E)\), and let \(M\in D^b(k)\). The canonical coefficient multiplication map is an isomorphism:

\[
R\Gamma(Q;F|_Q)\otimes_k^L M
\xrightarrow{\sim}
R\Gamma(Q;(F\otimes_k^L M_E)|_Q).
\tag{Q3}
\]

Here is a resolution proof that also fixes its naturality. Write \(i_Q:Q\hookrightarrow E\) and \(B_Q=i_{Q*}i_Q^{-1}F\). Exact closed extension identifies \(R\Gamma(Q;F|_Q)\) with \(R\Gamma_c(E;B_Q)\). The closed-subspace tensor map \(B_Q\otimes^L M_E\to i_{Q*}(F|_Q\otimes^L M_Q)\) is an isomorphism on stalks, checked with a flat model for \(M\). The compact-support projection proof now applies on the manifold \(E\), not on the possibly singular or lower-dimensional compact set \(Q\).

More explicitly, choose a bounded c-soft resolution \(A\) of \(B_Q\), using the finite manifold cohomological-dimension argument proved there. Choose a bounded projective module complex \(P\) representing \(M\); finite global dimension permits this even for infinitely generated modules. Each projective term is a summand of a free module. Thus \(A^i\otimes P^j_E\) is a summand of a coproduct of c-soft sheaves and remains c-soft. Compactly supported sections commute with that coproduct: a compact support meets only finitely many nonzero local coefficient indices after a finite subcover. They also preserve the splitting. Consequently the actual map

\[
\Gamma_c(E;A)\otimes_k P
\longrightarrow\Gamma_c(E;A\otimes_k P_E)
\tag{Q4}
\]

is a termwise isomorphism. Both complexes are bounded, and their terms on the right are compact-section acyclic. The finite acyclic-resolution calculation proves (Q3). If \(R\subset Q\) is another compact set, the sheaf map \(B_Q\to B_R\) is actual restriction. Coefficient multiplication commutes with that map, so (Q3) identifies the restriction on the tensor with the original restriction tensored by \(M\). No finite-rank Künneth assertion or choice of a resolution varying continuously with \(y\) is needed.

### A fixed cut can test several directions {#external-product-microsupport}

We claim

\[
\operatorname{SS}(F\boxtimes^L G)
\subset \operatorname{SS}(F)\times\operatorname{SS}(G).
\tag{Q5}
\]

Consider \((x_0,y_0;\xi_0,\eta_0)\) outside the right side, and suppose first that \((x_0;\xi_0)\notin\operatorname{SS}(F)\). If \(\xi_0=0\), the constant-function support tests vanish on a whole base neighborhood. Those tests are the stalks of \(F\), so \(F\) is zero on that neighborhood. The external product is then locally zero for every second covector. Exclusion of a zero covector supplies this neighborhood; a single zero stalk would not suffice.

Suppose \(\xi_0\ne0\). The uniform compact-cap implication supplies a nonzero closed pointed cone \(C\), a number \(h>0\), and the fixed halfspace and base

\[
H_X=\{x:\langle x-x_0,\xi_0\rangle\geq-h\},\quad
L_X=\partial H_X,\quad
Q_z=(z+C)\cap H_X,\quad R_z=(z+C)\cap L_X.
\tag{Q6}
\]

For all vertices \(z\) in one neighborhood of \(x_0\), these sets are compact, lie in the coordinate domain, and the actual restriction from \(Q_z\) to \(R_z\) is an isomorphism on derived sections of \(F\). Also \(\langle c,\xi_0\rangle<0\) for every nonzero \(c\in C\).

In the product chart choose the cone \(\Gamma=C\times\{0\}\) and the cutting functional \(\lambda=(\xi_0,0)\). The tested covector remains \(\nu=(\xi_0,\eta_0)\). With this choice,

\[
\begin{aligned}
((z,w)+\Gamma)\cap(H_X\times E_Y)&=Q_z\times\{w\},\\
((z,w)+\Gamma)\cap(L_X\times E_Y)&=R_z\times\{w\},\\
\langle(c,0),\lambda\rangle
&=\langle(c,0),\nu\rangle=\langle c,\xi_0\rangle<0.
\end{aligned}
\tag{Q7}
\]

Equations (Q2)–(Q3), including their naturality, identify the product cap comparison with

\[
\bigl[R\Gamma(Q_z;F)\longrightarrow R\Gamma(R_z;F)\bigr]
\otimes_k^L G_w.
\tag{Q8}
\]

It is an isomorphism for every nearby \((z,w)\), with geometry independent of the module complex \(G_w\).

We spell out why this comparison excludes \(\nu\), even though the cut uses \(\lambda\). The cap-to-cone proof (D17)–(D19) starts with \(J=F\boxtimes^L G\), extended from its chart, and \(B=J_{H_\lambda\setminus L_\lambda}\). Its cone projector has stalk the fibre of the cap-to-base map, hence vanishes on a vertex neighborhood \(V\). Properness used here follows from strict negativity: \(\lambda(c)\leq-a|c|\) on \(\Gamma\), for some \(a>0\); if \(p\) ranges in a compact set and \(p+c\in H_\lambda\), then \(|c|\) is bounded. The closed correspondence over that compact set is therefore compact, including when \(\Gamma\) has empty interior.

Choose a directional lens \(S=O_1\setminus O_0\), where \(O_1=B_r(p_0)+\Gamma\), \(O_0=O_1\cap\{\lambda(p-p_0)<-b\}\), and \(r,b>0\) are small. If \(p=p_0+v+c\in S\), then \(|v|<r\) and \(a|c|\leq b+|\lambda|r\). Thus the closure of the lens lies in \(V\cap\operatorname{Int}H_\lambda\), while \(p_0\) is in its interior. Directional support compatibility and the actual projector unit give a complex

\[
A=\mathcal L_S B,\qquad
A\simeq J\text{ near }p_0,\qquad Rq_{\Gamma*}A=0.
\tag{Q9}
\]

The last step (D20) of that proof applies to every covector strictly negative on \(\Gamma\), independently of the cutting functional. For clarity, a \(C^1\) test with such a differential decreases at a fixed positive rate on each unit cone ray in a sufficiently small ball. Adding \(\Gamma\) to its negative sublevel patch gives a directional open with the same germ. The sets \((B_\epsilon(p)+\Gamma)\) minus that open lie in \(B_{K\epsilon}(p)\); the strict ray decrease bounds the time needed to enter the sublevel. They form an ordinary relative neighborhood basis of the complementary germ. Directional support compatibility and (Q9) annihilate their supported sections, so the local support-test stalk vanishes. The negative margin persists in a covector neighborhood, as required in the definition of microsupport. By (Q7) it applies to \(\nu\) for every \(\eta_0\). If instead the second factor's covector is excluded, interchange the factors. This proves (Q5).

### Ordinary restriction from a punctured cylinder {#characteristic-restriction-proof}

Let \(i:M\hookrightarrow X\) be a closed smooth submanifold and \(F\in D^b(k_X)\). With the intrinsic limit set of (L20)–(L25), we prove

\[
\operatorname{SS}(i^{-1}F)
\subset Z_M(\operatorname{SS}(F))
=T^*M\cap C_{T_M^*X}(\operatorname{SS}(F)).
\tag{Q10}
\]

Put \(Y=X\times\mathbb R_t\), \(N=M\times\{0\}\), and let \(j:Y\setminus N\hookrightarrow Y\) and \(q:Y\to X\). Use the closed half-line coefficient:

\[
K=q^{-1}F\otimes_k k_{\{t\geq0\}},\qquad
H=j^{-1}K,\qquad
K\longrightarrow Rj_*H.
\tag{Q11}
\]

The last arrow is the actual adjunction unit. The half-line sheaf has stalks \(k\) or zero, so it is flat and the displayed ordinary tensor equals the derived tensor. Equivalently, \(K\) is restriction of \(q^{-1}F\) to the closed half-cylinder, followed by exact closed extension; this identification is checked on stalks.

The unit in (Q11) is an isomorphism. Away from \(N\) this follows from open restriction. Near a point of \(N\), take a product box \(U\times(-\epsilon,\epsilon)\). Its source and target section complexes are respectively the derived sections of the pulled-back \(F|_U\) on

\[
W=U\times[0,\epsilon),\qquad
Z=W\setminus(M\times\{0\}),
\tag{Q12}
\]

and the unit is their restriction map. These are locally compact Hausdorff spaces. Both projections to \(U\) have the same section \(s(x)=(x,\epsilon/2)\), and the fibre-preserving homotopy is

\[
(x,t,r)\longmapsto (x,(1-r)t+r\epsilon/2),\qquad 0\leq r\leq1.
\tag{Q13}
\]

It stays in \(W\), and stays in \(Z\) when started there: if \(x\in M\), the initial \(t\) is already positive. The relative contraction (D11)–(D12) identifies the actual pullbacks \(R\Gamma(U;F)\to R\Gamma(W;q^{-1}F)\) and \(R\Gamma(U;F)\to R\Gamma(Z;q^{-1}F)\) as isomorphisms. Their triangle with restriction commutes. Thus the restriction is an isomorphism as an actual map. The product boxes form a neighborhood basis, proving the assertion on stalks. Properness is used in D11 for the compact homotopy interval, not for either projection in (Q12).

Writing \(i_N:N\hookrightarrow Y\), we consequently have the canonical identification

\[
i_N^{-1}Rj_*H\simeq i_N^{-1}K\simeq i^{-1}F.
\tag{Q14}
\]

By (Q5), with the flat half-line factor, \(\operatorname{SS}(H)\) is contained in \((\operatorname{SS}(F)\times T^*\mathbb R)|_{Y\setminus N}\). The precise sign of its last covector is unnecessary here. In adapted coordinates \((u,z)\) on \(X\), \(M=\{u=0\}\), apply the missing-submanifold trace estimate (L27) to \(H\) and use (Q14). For any \((z_0;b_0)\) in the microsupport of that trace, (L20) supplies witnesses satisfying

\[
\begin{gathered}
(u_n,z_n,t_n;a_n,b_n,\tau_n)\in\operatorname{SS}(H),\qquad
(u_n,z_n,t_n)\longrightarrow(0,z_0,0),\\
b_n\longrightarrow b_0,\qquad
|(u_n,t_n)|\,|(a_n,\tau_n)|\longrightarrow0,\\
(u_n,z_n;a_n,b_n)\in\operatorname{SS}(F),\qquad
|u_n|\,|a_n|\longrightarrow0.
\end{gathered}
\tag{Q15}
\]

The last limit follows by bounding its two factors by the corresponding factors above it. No bound on \(a_n\) or \(\tau_n\) separately is imposed. This is exactly the criterion for (Q10). Empty submanifolds give zero restriction; in codimension zero the same argument reduces to the ordinary restricted microsupport. The proof supplies ordinary restriction and makes no assertion about exceptional restriction or a duality comparison.

### Restrict the external product to the diagonal {#diagonal-limiting-sum}

For \(F,G\in D^b(k_X)\), exact monoidal inverse image along \(\Delta:X\hookrightarrow X\times X\) gives

\[
\Delta^{-1}(F\boxtimes^L G)\simeq F\otimes_k^L G,
\qquad
\operatorname{SS}(F\otimes_k^L G)
\subset Z_\Delta\bigl(\operatorname{SS}(F)\times\operatorname{SS}(G)\bigr).
\tag{Q16}
\]

The second inclusion follows from (Q10), (Q5), and monotonicity of the sequence definition of \(Z_\Delta\). We compute the right side, including its large normal covectors. In product coordinates use \(u=x-y\), \(z=y\). Then

\[
\alpha\,dx+\beta\,dy
=\alpha\,du+(\alpha+\beta)\,dz,
\qquad a=\alpha,\quad b=\alpha+\beta.
\tag{Q17}
\]

The criterion (L20) says precisely that \((x_n;\alpha_n)\) and \((y_n;\beta_n)\) tend in base to the same point, their sum tends to the desired tangent covector, and \(|x_n-y_n||\alpha_n|\to0\). Conversely every witness in (L1) gives such a diagonal witness. Hence, for any conic sets \(A,B\),

\[
Z_\Delta(A\times B)=A\widehat+ B,
\qquad
\boxed{\operatorname{SS}(F\otimes_k^L G)
\subset\operatorname{SS}(F)\widehat+\operatorname{SS}(G).}
\tag{Q18}
\]

This establishes the full limiting tensor estimate used by the constructibility criterion. The covectors in its witnesses may be unbounded, and their bases need not coincide before taking the limit. The boundedness of the tensor is supplied by (Q2); over a ring without a suitable Tor bound, bounded inputs alone would not justify applying these bounded-below support tests.

## Four tensor and restriction checks with solutions {#tensor-restriction-exercises}

### A tilted cut changes the cap height

Take first and second coordinates \(x,y\in\mathbb R\), the cone \(C=(-\infty,0]\), and a target covector \((1,2)\) at the origin. Compare the cap cut at \(-h\) by this covector with the cap cut by \((1,0)\), at vertex \((z,w)\).

**Solution.** The cone slice has \(y=w\) and \(x\leq z\). The target-covector cut gives \(-h-2w\leq x\leq z\), whereas the first-factor cut gives \(-h\leq x\leq z\). The first cap varies in height with \(w\); one cannot substitute the fixed first-factor cap without an additional argument. The first-factor cut gives exactly that fixed cap. Both covectors are strictly negative on \(C\times\{0\}\), so (Q9) and the cone-to-test proof still exclude the target direction.

### Why the half-line is closed

In the cylinder construction, take \(X=M=\{*\}\) and \(F=k\ne0\). Compare the units for the closed and open positive half-line sheaves at zero.

**Solution.** In both cases the restriction to \(\mathbb R\setminus\{0\}\) is constant on the positive component and zero on the negative one. Its ordinary derived extension has stalk \(k\) at zero: sections on a small positive interval are \(k\), with no higher cohomology. The closed half-line sheaf also has stalk \(k\), and its unit is the identity under constant sections. The open extension-by-zero sheaf has zero stalk, so its unit at zero is \(0\to k\), not an isomorphism. Replacing the closed half-line in (Q11) by the open one would break (Q14).

### Tangent boundaries create every covector

Over a field, in \(\mathbb R^2_{x,y}\), take \(F=k_{\{x\geq y^2\}}\) and \(G=k_{\{x\leq0\}}\). Compute their tensor and explain why the ordinary same-base sum at the origin cannot replace the limiting sum.

**Solution.** Both sheaves are stalkwise flat and their supports intersect only at the origin, so the actual tensor is \(k_{\{(0,0)\}}\). The closed-embedding formula gives its full cotangent fibre at that point. A smooth coordinate change and the closed-half-line support test give boundary normals \(c(1,-2y)\), \(c\geq0\), for \(F\), and \((-b,0)\), \(b\geq0\), for \(G\). Thus their same-base sum at the origin contains only horizontal covectors. To obtain a target \((\xi,\eta)\) with \(\eta\ne0\), choose \(t_n\to0\) with sign opposite to \(\eta\), and put

\[
\begin{aligned}
p_n&=(t_n^2,t_n),& q_n&=(0,t_n),& c_n&=-\eta/(2t_n)>0,\\
\alpha_n&=c_n(1,-2t_n),&\beta_n&=(\xi-c_n,0),&
\alpha_n+\beta_n&=(\xi,\eta).
\end{aligned}
\tag{Q19}
\]

Eventually \(\xi-c_n\leq0\), so these are the required two normals. Their weighted base error is \(t_n^2c_n\sqrt{1+4t_n^2}\to0\), although both horizontal covectors diverge. Horizontal targets already belong to the same-base sum. The limiting sum therefore contains the full fibre, as the tensor demands.

### Infinite modules and a nontrivial Tor degree

Let \(k=\mathbb Z\), \(V=\bigoplus_{n\geq0}\mathbb Z/2\), and take constant sheaves \(F=V_X\), \(G=(\mathbb Z/2)_X\). Calculate the tensor degrees and its microsupport bound.

**Solution.** Tensor the free two-term resolution \(\mathbb Z\xrightarrow{2}\mathbb Z\), in degrees \(-1,0\), of \(\mathbb Z/2\) with \(V\). Its differential becomes zero. Hence

\[
H^{-1}(F\otimes^L G)=V_X,
\qquad H^0(F\otimes^L G)=V_X,
\qquad H^j(F\otimes^L G)=0\quad(j\ne-1,0).
\tag{Q20}
\]

The exhibited complex is constant, so the zero-section criterion bounds its microsupport by the zero section; the limiting sum of the two input zero sections is the same zero section. The nonzero degree \(-1\) shows why the derived tensor cannot be replaced by the ordinary tensor. The infinite module is not subject to any finite-generation or perfect-stalk requirement in this proof.

## Four checks with solutions

### An unbounded sequence contributes a finite tangent direction

In \(X=\mathbb R_u\times\mathbb R_z\), let \(M=\{u=0\}\). Let \(A\) consist of all positive multiples of \((a,b)=(n,1)\) over \((u,z)=(n^{-2},0)\), for integers \(n\geq1\). Show that every \((0,0;a_0,1)\) belongs to \(A\widehat+T_M^*X\), although the ordinary same-base sum is empty.

**Solution.** The displayed sequence has \(b_n=1\) and \(|u_n||a_n|=1/n\to0\). Pair it with \((0,0;a_0-n,0)\). The sums converge to the specified covector and the weighted base error tends to zero. There are no bases shared by \(A\) and \(T_M^*X\), so the ordinary sum is empty. Any sequence in this example whose tangential coefficient tends to one and whose base tends to \(M\) has scaling factor tending to one and \(n\to\infty\); its normal coefficient must therefore diverge. Bounded inputs would miss this direction.

### Why base convergence alone is insufficient

Replace the bases in the preceding example by \((n^{-1},0)\). Can a limiting sum have final tangential coefficient one? Check the effect of the adapted change \(u'=e^z u\), \(z'=z\).

**Solution.** Write the positive scale as \(c_n\). Tangential convergence to one forces \(c_n\to1\), whereas \(|u_n||a_n|=c_n\to1\). Condition (L20) fails, so no final normal component can repair the defect. In the new coordinates, \(a'=e^{-z'}a\) and \(b'=b-ua\). The unscaled sequence has \(b'=0\) although \(b=1\). This is the uncontrolled error in (L2) and (L23). In the first example the corresponding error is \(ua=1/n\to0\), so the tangent limit is unchanged.

### The two sides in normal rank one

Let \(X=\mathbb R\), \(M=\{0\}\), and let \(F\) be the constant sheaf with a nonzero, possibly infinitely generated, module \(V\) on \(U=\mathbb R\setminus\{0\}\). Compute its trace \(i^{-1}Rj_*F\) and compare the ambient boundary directions of the two extensions.

**Solution.** Each sufficiently small punctured interval is the disjoint union of two contractible intervals, so its derived sections are \(V\oplus V\) in degree zero. The restriction maps identify the two summands by their sides, giving \(i^{-1}Rj_*F=V\oplus V\). The rank-one blowup has two points in its sphere fibre, exactly encoding those two components. Ordinary extension is locally the sum of the constant sheaves on the two closed half-lines; extension by zero is the corresponding sum on the open half-lines. The endpoint support tests in the directional reading give opposite half-rays for the two sides, whose union is the full cotangent fibre at zero in either case. The trace is a complex on a point and has only the zero covector there. No finite-generation assumption entered any calculation.

### Radial control does not replace sphere control

In normal rank two, take \(\theta_n=(1,0)\), \(t_n\to0^+\), and \(a_n=t_n^{-1}(0,1)\). Does \(t_n|\tau_n|\to0\) alone imply \(t_n|a_n|\to0\)?

**Solution.** Here \(\tau_n=\langle\theta_n,a_n\rangle=0\), but the sphere covector is \(\lambda_n=(0,1)|_{T_{(1,0)}S^1}\), of norm one. Thus \(t_n|a_n|=1\). The missing condition is precisely \(\lambda_n\to0\), which comes from the zero sphere component of the proper-image lift (L30). Equation (L31) combines both controls and makes clear why neither may be omitted.

## Sources and scope {#sources-and-scope}

The human reference is Masaki Kashiwara and Pierre Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/), also available from [Schapira’s author page](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf). Its normal-cone geometry and open-extension estimates guide the results treated here. The proof above develops the sequence errors, both boundary signs, actual extension limits, and the doubled-blowup reduction explicitly, using the linked programme proofs. The external-product, ordinary-restriction and limiting tensor statements are also treated in that work. The argument here uses explicit compact coefficient maps, a closed-half-line cylinder and the diagonal, for bounded inputs over a ring of finite global dimension. Involutivity, compatible microlocal stratifications and the further constructible-duality foundations have separate proofs and hypotheses.
