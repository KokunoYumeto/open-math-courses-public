# Expanding subspaces and hyperbolic Lefschetz cutoffs

A local Lefschetz contribution can be computed by compact cohomology on an expanding subspace. “Expanding” here is a condition on positive real eigenvalues. It does not mean that every vector in the subspace grows in a chosen Euclidean metric. The proof first separates directions by modulus, constructs a metric suited to that separation, and then removes the extra directions by their action on positive rays.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 2 October 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

Learn first Homotopies and local cutoffs for Lefschetz contributions, Lefschetz traces of constructible correspondences, and Perfect operations and finite microlocal coefficients. We also use the written SH-02 proofs of normalized positive-scaling transport, ordinary and proper-support contraction to the zero section, and transport through sheaf operations, in Transport along a scaling action. The exact current proof scopes are recorded privately. These are programme prerequisites; their transitive foundations and independent review remain open.

Let \(V\) be a finite-dimensional real vector space, \(k\) a characteristic-zero field, and \(F\) a bounded positively conic, real constructible complex with perfect stalks. Conicity means local constancy along parametrized positive scaling orbits. On a vector space the nonzero orbits are embedded rays. Fix
\[
 u:V\longrightarrow V,\qquad
 \phi:u^{-1}F\longrightarrow F,\qquad
 1\notin\operatorname{Ev}(u).
 \qquad\text{(1)}
\]
The fixed set of \(u\) is \(\{0\}\). Its normalized local contribution is \(C_0(\phi)\). If the coefficient vanishes near zero this number is zero. Traces below are alternating traces on perfect complexes, written \(\operatorname{str}\).

## Spectral intervals define the two kinds of subspace

Write \(V^\mathbb C_\lambda\) for the generalized \(\lambda\)-eigenspace of the complexification of \(u\). An invariant real subspace \(S\) is a **shrinking space** when the restriction has no real eigenvalue greater than one and the quotient has no real eigenvalue in \([0,1)\). An invariant real subspace \(E\) is an **expanding space** when the restriction has no real eigenvalue in \([0,1)\) and the quotient has no real eigenvalue greater than one. Equivalently,
\[
 \begin{aligned}
 \bigoplus_{\lambda\in[0,1)}V^\mathbb C_\lambda
 &\subset S^\mathbb C
 \subset\bigoplus_{\lambda\notin(1,\infty)}V^\mathbb C_\lambda,\\
 \bigoplus_{\lambda\in(1,\infty)}V^\mathbb C_\lambda
 &\subset E^\mathbb C
 \subset\bigoplus_{\lambda\notin[0,1)}V^\mathbb C_\lambda.
 \end{aligned}
 \qquad\text{(2)}
\]
The intervals in this display are subsets of the real axis in \(\mathbb C\); their complements include nonreal eigenvalues. Invariance is still required.

**Proof of the equivalence.** The primary decomposition projections are polynomials in \(u\): the pairwise relatively prime powers of \(z-\lambda\) give the projections by the polynomial Bezout identity. They therefore preserve every invariant subspace. The restriction and quotient decompose into their intersections and images in the primary blocks. A nonzero invariant part of a \(\lambda\)-block has eigenvalue \(\lambda\); a nonzero quotient of that block does too. Thus excluding an eigenvalue from the restriction forces the intersection to vanish, whereas excluding it from the quotient forces the entire block into the subspace. These are exactly the two inclusions in each line of (2). Conjugate blocks occur together because the subspace is real. This proves both directions.

In particular,
\[
 u^{-1}S=S,\qquad u|_E:E\longrightarrow E
 \text{ is an isomorphism}.
 \qquad\text{(3)}
\]
Indeed, the quotient by \(S\) has no zero eigenvalue, while the restriction to \(E\) has none. The first equality does not assert \(uS=S\): zero eigenvalues may occur inside \(S\).

The smallest expanding space is
\[
 W=\left(\bigoplus_{\lambda>1}V^\mathbb C_\lambda\right)\cap V.
 \qquad\text{(4)}
\]
Every expanding space contains \(W\). A negative eigenvalue of large modulus is allowed in an expanding space but is not forced into it.

For such an \(E\), define \(C_E=R\Gamma_c(E;F|_E)\). Its operator \(U_E\) is compactly supported pullback by the linear isomorphism \(u_E=u|_E\), followed by \(\phi|_E\):
\[
 C_E\xrightarrow{u_E^*}
 R\Gamma_c(E;u_E^{-1}(F|_E))
 \xrightarrow{\phi|_E}C_E.
 \qquad\text{(5)}
\]
Properness of \(u_E\) justifies the first arrow. Conic proper-support contraction identifies \(C_E\) with the zero costalk of \(F|_E\), which is perfect by the perfect-operation theorem. This proves finiteness without assuming compact support of \(F\) on \(V\).

We will prove
\[
 \boxed{C_0(\phi)=\operatorname{str}(U_E)
 \quad\text{for every expanding space }E.}
 \qquad\text{(6)}
\]

## Conic projections and the actual contraction maps

We need constructibility for a projection \(q:A\oplus B\to B\), although this map is not proper. For a conic perfect constructible \(K\), both \(Rq_!K\) and \(Rq_*K\) are conic perfect constructible.

**Proof.** Compactify \(A\) by the sphere
\[
 Y=\{(t,v)\in\mathbb R\oplus A:t^2+|v|^2=1\},\qquad
 a\longmapsto\frac{(1,a)}{\sqrt{1+|a|^2}}.
 \qquad\text{(7)}
\]
The image is the open positive hemisphere. Let \(j:A\oplus B\hookrightarrow Y\times B\) be this embedding and put \(m(t,v,b)=(v,tb)\). On \(t>0\), \(m=t(a,b)\). Normalized conic transport therefore identifies \(j^{-1}m^{-1}K\) with \(K\). Consequently
\[
 j_!K\simeq k_{\{t>0\}}\otimes m^{-1}K,\qquad
 Rj_*K\simeq R\mathcal Hom(k_{\{t>0\}},m^{-1}K).
 \qquad\text{(8)}
\]
The second identity is open restriction and ordinary adjunction. The map \(m\) is analytic and the positive hemisphere is subanalytic. The constructible inverse-image, tensor and internal-Hom theorems show that both objects in (8) are bounded with perfect stalks. Projection \(\pi:Y\times B\to B\) is proper, so its direct image has the same properties. Since \(q=\pi j\), these images are \(Rq_!K\) and \(Rq_*K\).

Conicity follows from the actual equivariant direct-image comparisons for \(q\). For \(q_!\) they are proper-support base change, even though \(q\) itself is not proper. For \(q_*\), product base change with the scaling parameter is checked on rectangles using interval descent; conjugation by the action homeomorphism gives the action square. The normalized transport in both cases restricts to the identity at parameter one. No general theorem that arbitrary nonproper images preserve constructibility is being used.

For a conic \(H\) on \(B\), the following specified maps are isomorphisms:
\[
 R\Gamma(B;H)\xrightarrow{\mathrm{restriction}}H_0,
 \qquad
 R\Gamma_{\{0\}}(B;H)
 \xrightarrow{\mathrm{support\ inclusion}}R\Gamma_c(B;H).
 \qquad\text{(9)}
\]
These are the ordinary and proper-support contraction maps. Ordinary restriction also gives \(R\Gamma(\overline B_b;H)\simeq H_0\) for every closed ball of positive radius. To see the last assertion, restriction to each open ball is an isomorphism by the scaling restriction criterion: the parameter set carrying a vector into that ball is a nonempty interval. For a compact closed ball, neighbourhood continuity computes its sections from the slightly larger open balls. Their restrictions are all the same isomorphism to the germ at zero. Thus the induced closed-ball restriction is that isomorphism. No orientation shift occurs in these maps.

## An adapted metric produces the correct mixed box

First suppose that no eigenvalue has modulus one. The real primary decomposition gives
\[
 V=V_+\oplus V_-,\qquad
 V_+^\mathbb C=\bigoplus_{|\lambda|>1}V^\mathbb C_\lambda,\quad
 V_-^\mathbb C=\bigoplus_{|\lambda|<1}V^\mathbb C_\lambda.
 \qquad\text{(10)}
\]
There is an inner product for which, with \(0<c_1<1<c_2\),
\[
 |u_-b|\le c_1|b|,\qquad |u_+a|\ge c_2|a|.
 \qquad\text{(11)}
\]

**Proof.** If a linear map \(A\) has spectral radius less than \(q<1\), define
\[
 |v|_P^2=\sum_{j\ge0}q^{-2j}|A^jv|_0^2.
 \qquad\text{(12)}
\]
A Jordan block estimate bounds \(|A^j|\) by a polynomial in \(j\) times \(r^j\), with \(r<q\), so the series converges and is a positive definite quadratic form. Shifting its sum gives
\[
 |Av|_P^2=q^2(|v|_P^2-|v|_0^2)\le q^2|v|_P^2.
 \qquad\text{(13)}
\]
Apply this construction to \(u_-\) and to \(u_+^{-1}\), and take the orthogonal sum of the two forms. This proves (11), including singular \(u_-\).

For \(a,b>0\) set
\[
 Z_{a,b}=B_a^+\times\overline B_b^-.
 \qquad\text{(14)}
\]
The plus ball is open and the minus ball closed. Since \(u_+^{-1}B_a^+\subset B_a^+\) and \(\overline B_b^-\subset u_-^{-1}\overline B_b^-\),
\[
 u^{-1}Z_{a,b}\cap Z_{a,b}
 =u_+^{-1}B_a^+\times\overline B_b^-.
 \qquad\text{(15)}
\]
This is open in \(Z_{a,b}\) and closed in \(u^{-1}Z_{a,b}\). The latter assertion uses closedness of the minus ball inside its preimage; the former uses openness of the inverse plus ball inside the plus ball. The compact closure has only the fixed point zero. The ordinary cutoff theorem therefore gives
\[
 C_0(\phi)=\operatorname{str}(U_{a,b}),
 \quad U_{a,b}\text{ on }R\Gamma_c(Z_{a,b};F|_{Z_{a,b}}).
 \qquad\text{(16)}
\]
This operator is ordinary pullback on the ambient compact coefficient \(F_{Z_{a,b}}\), followed by closed restriction on the entrance and open extension on the exit. It is not pullback of arbitrary compactly supported sections by a possibly singular \(u\).

## A large cutoff stabilizes by extension by zero

Fix \(b>0\) and write \(Z_{\infty,b}=V_+\times\overline B_b^-\). For sufficiently large \(a\), the **forward open-extension map**
\[
 R\Gamma_c(Z_{a,b};F)
 \longrightarrow R\Gamma_c(Z_{\infty,b};F)
 \qquad\text{(17)}
\]
is an isomorphism.

**Proof.** Use (7) with \(A=V_+\), \(B=V_-\), and let
\[
 F'=j_!(F_{\{|x_-|\le b\}}),
 \qquad\text{(18)}
\]
where \(x_-\) denotes the minus coordinate. Equivalently, \(F'=k_{\{t>0\}}\otimes m^{-1}F\otimes k_{\{|x_-|\le b\}}\). It is constructible and its closed support lies in the compact set \(Y\times\overline B_b^-\). Its restriction to \(t=0\) is zero, because \(j_!\) is open extension by zero.

Push \(F'\) by \(g(t,v,b)=t\). Properness on its closed support implies that \(H=Rg_*F'\) is a perfect constructible complex on \(\mathbb R\). Proper base change gives \(H_0=0\). Choose \(\epsilon_0>0\) with no singularity of \(H\) on either of the intervals \((-\epsilon_0,0)\), \((0,\epsilon_0)\).

For \(0<\epsilon<\epsilon_0\),
\[
 R\Gamma([-\epsilon,\epsilon];H)\simeq H_0=0.
 \qquad\text{(19)}
\]
Here is the endpoint argument. On the compact interval, localize at zero. The complementary arms are \([-\epsilon,0)\) and \((0,\epsilon]\). Each carries a constant complex. Its open extension across zero has zero ordinary sections: the triangle from the constant complex on the corresponding closed half interval to its value at zero has restriction map the identity, hence zero fibre. The same statement for bounded complexes follows by truncation, or the derived interval-gluing calculation in Constructible gluing on an interval. The two arm terms vanish, leaving \(H_0\). This proves (19).

The finite plus ball corresponds to
\[
 t>\tau(a),\qquad \tau(a)=(1+a^2)^{-1/2}.
 \qquad\text{(20)}
\]
Localize \(F'\) into this open set and its closed complement. Since \(F'\) has no stalks for \(t\le0\), the complementary term for \(0<\tau(a)<\epsilon_0\) is \(R\Gamma([-\tau(a),\tau(a)];H)=0\). All closed supports here are compact. The first arrow of this localization triangle is exactly (17), so it is an isomorphism. This proves stabilization with its direction and its endpoint convention specified.

If \(V_+=0\), the plus ball and plus cylinder are both a point, and (17) is the identity. The proof needs no fictitious sphere in that case.

## The stabilized operator is compact pullback on the expanding fibre

Let \(q:V_+\oplus V_-\to V_-\), \(H=Rq_!F\). Proper-support base change and (9) give
\[
 \begin{aligned}
 R\Gamma_c(Z_{a,b};F)
 &\xrightarrow{\sim}R\Gamma_c(Z_{\infty,b};F)\\
 &\simeq R\Gamma(\overline B_b^-;H)
 \xrightarrow{\sim}H_0
 \simeq R\Gamma_c(V_+;F|_{V_+}).
 \end{aligned}
 \qquad\text{(21)}
\]
The middle identity integrates along the plus fibres. The minus base is compact, so ordinary and compact sections agree there.

We check the operators in (21). The square with \(q\), \(u\), and \(u_-\) is Cartesian: for a target plus coordinate \(a'\) and a source minus coordinate \(b\), the unique source plus coordinate is \(u_+^{-1}a'\). Hence proper-support base change gives the actual comparison
\[
 u_-^{-1}H\xrightarrow{\sim}Rq_!u^{-1}F
 \xrightarrow{Rq_!\phi}H.
 \qquad\text{(22)}
\]
At zero it is the compact pullback and coefficient map (5) for \(E=V_+\). Invertibility of \(u_+\) supplies the proper fibre map, while no invertibility of \(u_-\) is needed.

On the closed minus ball, (22) acts by ordinary \(u_-\)-pullback followed by restriction from \(u_-^{-1}\overline B_b^-\) to \(\overline B_b^-\). Restriction to its zero germ intertwines this operator with the operator on \(H_0\): both restrictions are the counit for the same point inclusion, and \(u_-(0)=0\).

For completeness, finite plus cutoffs intertwine the same operators. Write \(j_a:B_a^+\hookrightarrow V_+\). The plus part of the cutoff map is open extension from \(u_+^{-1}B_a^+\) into \(B_a^+\), after proper pullback by \(u_+\). Compose it with the open-extension counit \(j_{a!}j_a^{-1}F\to F\). Transitivity of open extension identifies that composite with extension from \(u_+^{-1}B_a^+\) directly into \(V_+\), followed by \(\phi\). The minus part is restriction to \(\overline B_b^-\) in both paths. Proper-support base change commutes with these counits. Thus, if \(\beta_a\) is the first map of (21), the resulting square has
\[
 \beta_a U_{a,b}=U_{\infty,b}\beta_a,
 \qquad
 H_0\text{ carrying }U_{V_+}.
 \qquad\text{(23)}
\]
This is an equality of natural morphisms before stabilization. Once \(a\) is large, \(\beta_a\) is an isomorphism. Equations (16), (21) and (23) prove (6) for \(E=V_+\) under the modulus assumption. They also prove finiteness of every complex used in (21).

## Positive scalar transport removes eigenvalues of unit modulus

Choose a small closed interval \(I\subset(0,\infty)\) about one such that \(tu\) never has eigenvalue one. Normalized conic transport gives one morphism on \(V\times I\),
\[
 (tu)^{-1}F\simeq u^{-1}F
 \xrightarrow{\phi}F,
 \qquad\text{(24)}
\]
where the notation on the right includes pullback from \(V\). At \(t=1\) the transport is the identity. The linear-family theorem proves that \(C_0(\phi_t)\) is constant.

Every fixed expanding space \(E\) for \(u\) remains expanding for \(tu\) if \(I\) is small enough: finitely many positive real eigenvalues stay on their original side of one, zero stays zero, and nonreal or negative eigenvalues remain outside the positive intervals. Moreover \(\operatorname{str}(U_{E,t})\) is constant. To justify the latter with the actual maps, use projection \(r:E\times I\to I\). Proper-support base change identifies \(Rr_!\mathrm{pr}_E^{-1}(F|_E)\) with the constant complex \(C_E\) on \(I\). The joint map \((e,t)\mapsto(tu_Ee,t)\) is a proper homeomorphism over \(I\): its inverse is continuous, with uniformly bounded inverse on compact parameter sets. Compact pullback and the family morphism (24) therefore produce an endomorphism of that constant complex. Interval descent says that all its slice maps are the same endomorphism under the specified identifications. This proves trace constancy; independent choices of coefficient maps at each \(t\) would not suffice.

The finitely many values \(t=|\lambda|^{-1}\) for nonzero eigenvalues are the only ones for which \(tu\) has an eigenvalue of modulus one. Choose a nearby value avoiding them. We may therefore apply the hyperbolic proof to \(tu\) and return to \(u\). What remains is to compare the expanding spaces.

## A quotient with no positive eigenvalue has zero ray trace

We first prove a useful trace identity. Let \(A:L\to L\) have no real eigenvalue in \([0,\infty)\), and let \(G\) be conic perfect constructible with \(\psi:A^{-1}G\to G\). Then \(A\) is invertible and
\[
 \operatorname{str}R\Gamma_c(L;\psi)
 =\operatorname{str}(\psi_0).
 \qquad\text{(25)}
\]
The left operator includes proper compact pullback by \(A\).

**Proof.** For \(L=0\), both sides are the same point trace. Suppose \(\dim L>0\). Let \(L^\times=L\setminus\{0\}\) and
\[
 \gamma:L^\times\to S(L)=L^\times/\mathbb R_{>0},
 \qquad \sigma([v])=[Av].
 \qquad\text{(26)}
\]
The sphere \(S(L)\) is compact, and \(\sigma\) is an analytic diffeomorphism. It has no fixed point: a fixed positive ray would give \(Av=cv\) for a real \(c>0\).

Choose a norm to identify \(L^\times\) with \(S(L)\times(0,\infty)\). Conic transport and interval descent identify \(G|_{L^\times}=\gamma^{-1}M\), where \(M=R\gamma_*(G|_{L^\times})\) is perfect constructible. This identification is the ordinary radial counit, without a radial shift. The map \(\psi\) descends to \(\sigma^{-1}M\to M\). Indeed, after the same radial coordinates, \(A\) sends \((s,r)\) to \((\sigma s,r|As|)\). Its positive change in the radial coordinate is identified by normalized conic transport, and ordinary interval descent gives exactly the descended map.

It follows that
\[
 R\Gamma(L^\times;G)\simeq R\Gamma(S(L);M)
 \qquad\text{(27)}
\]
intertwines the ordinary pullback operators. The compact-coefficient Lefschetz formula on \(S(L)\) gives trace zero, since \(\sigma\) has no fixed point. This use of the formula is on a compact sphere, with compact closed coefficient support.

The localization triangle at zero is invariant under \(A\), because \(A^{-1}(0)=0\). Its terms are perfect: the middle is \(G_0\) by (9), the last is finite by (27), and the first is perfect by the triangle. Trace additivity and the zero trace of its last term give
\[
 \operatorname{str}R\Gamma_{\{0\}}(L;G)
 =\operatorname{str}R\Gamma(L;G)
 =\operatorname{str}(\psi_0).
 \qquad\text{(28)}
\]
Finally the support-inclusion isomorphism in (9) commutes with \(A\)-pullback, since \(A\) is a proper isomorphism preserving zero. It identifies the first trace in (28) with the compact trace in (25). This proves the identity.

## Every expanding space gives the same trace

Let \(E\) be any expanding space and let \(W\) be (4). Set \(L=E/W\), and let \(A\) be the induced map. It has no real eigenvalue in \([0,\infty)\): positive eigenvalues greater than one have been removed with their full primary blocks, eigenvalues in \([0,1)\) were excluded from \(E\), and one is absent throughout. Put \(p:E\to L\), \(K=F|_E\), and \(G=Rp_!K\).

The projection lemma makes \(G\) conic perfect constructible. The square with \(p,u_E,A\) is Cartesian because \(u|_W\) is invertible. Its proper-support base change and the coefficient map give \(A^{-1}G\to G\). Composition of proper-support direct images and fibre base change give, with their actual operators,
\[
 R\Gamma_c(L;G)\simeq R\Gamma_c(E;K),
 \qquad
 G_0\simeq R\Gamma_c(W;F|_W).
 \qquad\text{(29)}
\]
The first is the compact operator \(U_E\). The second is \(U_W\), since the fibre over zero is \(W\) and its inverse under \(u_E\) is \(W\). Applying (25) proves
\[
 \operatorname{str}(U_E)=\operatorname{str}(U_W).
 \qquad\text{(30)}
\]

In the hyperbolic case \(V_+\) is itself an expanding space, so (30) compares it and \(E\) through \(W\). The proof of (6) for \(V_+\) consequently proves it for every \(E\). The scalar-family argument then proves (6) without the modulus assumption. This completes the expanding-space theorem.

The comparison is an equality of traces, not an isomorphism between all the complexes \(C_E\). Negative or nonreal directions can change their grading and dimension while contributing no discrepancy in trace. The shrinking-space theorem requires its own supported-cohomology argument and will be proved next.

## Exercises with complete solutions

### Positive intervals include zero

*Difficulty: Introductory.*

For \(u=\operatorname{diag}(3,\tfrac12,-2,0)\), find the smallest and largest expanding and shrinking spaces. Check (3), and decide whether \(uS=S\) for the smallest shrinking space.

**Solution.** Name the coordinate lines \(L_3,L_{1/2},L_{-2},L_0\). The smallest expanding space is \(L_3\), and the largest is \(L_3\oplus L_{-2}\). The smallest shrinking space is \(L_{1/2}\oplus L_0\), and the largest adds \(L_{-2}\). The positive interval \([0,1)\) includes the zero block. The quotient by either shrinking space is invertible, so its inverse image is that space. But \(u(L_{1/2}\oplus L_0)=L_{1/2}\), which is smaller. The restrictions to both expanding spaces are invertible.

### A Jordan block needs another metric

*Difficulty: Intermediate.*

Let \(A(x,y)=(x/2+y,y/2)\). Show that its spectral radius is \(1/2\), although it expands one Euclidean unit vector. Find a norm for which its operator norm is at most \(3/5\).

**Solution.** The matrix is one Jordan block with eigenvalue \(1/2\). It sends \((0,1)\) to \((1,1/2)\), of Euclidean norm \(\sqrt5/2>1\). Put \(|(x,y)|_P^2=x^2/100+y^2\). In coordinates \((x/10,y)\), the matrix is \(\tfrac12 I+N\), where \(N\) has its only nonzero entry \(1/10\) in the upper right. The triangle inequality for operator norms gives \(\|A\|_P\le1/2+1/10=3/5\). Thus the contracting metric is compatible with the spectrum, not with the original coordinate length.

### Orientation remains inside compact pullback

*Difficulty: Intermediate.*

For \(u(x,y)=(-2x,y/2)\) on \(\mathbb R^2\), take \(F=k_{\mathbb R^2}[r]\) and the canonical coefficient map. Compute \(C_0(\phi)\) using \(E=\mathbb R\times\{0\}\).

**Solution.** This \(E\) is expanding: its only eigenvalue is negative, so none lies in \([0,1)\), and the quotient eigenvalue \(1/2\) is not greater than one. Its compact complex is \(k[r-1]\). The reflection \(x\mapsto-2x\) acts by \(-1\) on the compact orientation generator of the line. Therefore the trace is \((-1)^{r-1}(-1)=(-1)^r\). Formula (6) gives this local contribution. Omitting the orientation action would give the wrong sign.

### The stabilization map has a direction

*Difficulty: Intermediate.*

For constant coefficients on \(V_+\oplus V_-\), with dimensions \(d_+,d_-\), calculate both sides of (17). Explain why an open half interval at infinity contributes zero in its proof.

**Solution.** The open plus ball has compact cohomology \(k[-d_+]\), while the compact closed minus ball has ordinary and compact cohomology \(k\). Both the finite box and infinite cylinder consequently have compact complex \(k[-d_+]\). The forward open-extension map preserves the consistently oriented plus generator and is the identity on the minus factor, hence is an isomorphism. In the compactification proof, an arm such as \((0,\epsilon]\) is open inside \([0,\epsilon]\). Its extension by zero fits into the triangle from the constant closed-interval complex to its value at zero. Their ordinary section map is the identity, so the arm term is zero. Compact cohomology of the open interval \((0,\epsilon)\), which is \(k[-1]\), is a different calculation.

### A negative eigenvalue removes the ray contribution

*Difficulty: Advanced.*

Apply (25) to \(A(x)=-2x\) on \(\mathbb R\) with \(G=k_{\mathbb R}\). Calculate the action on each term of localization at zero and on the positive-ray sphere.

**Solution.** The sphere is the two-point set \(S^0\); \(A\) swaps its points. Its ordinary section complex is \(k^2\) in degree zero and has trace zero. Ordinary sections on the line are \(k\), with action \(+1\). The zero costalk is \(k[-1]\), and reflection acts by \(-1\) on its orientation generator, giving alternating trace \(+1\). Its support-inclusion map identifies it with \(R\Gamma_c(\mathbb R;k)=k[-1]\), with the same action. Thus localization has traces \(1=1+0\), and the compact trace equals the stalk trace as asserted. The two complexes are not isomorphic.

### Rotation can be deformed across modulus one

*Difficulty: Advanced.*

Let \(u\) be rotation by \(\pi/2\) on \(\mathbb R^2\), \(F=k_{\mathbb R^2}\), and \(\phi\) canonical. Explain why (6) applies even though both eigenvalues have modulus one, and compute the contribution.

**Solution.** The eigenvalues are \(i,-i\), so one is absent and the zero subspace is expanding. Its compact complex is \(k\) with the identity operator; the contribution is one. For the intermediate proof, the family \(tu\), for positive \(t\) close to one, never has eigenvalue one. For \(t<1\) both directions are contracting, while for \(t>1\) both are expanding by modulus. In the latter case compact cohomology is \(k[-2]\), and the orientation-preserving rotation/dilation acts by \(+1\), still giving trace one. The normalized scalar family gives the same local class on both sides and at \(t=1\).

### Different expanding spaces can have different complexes

*Difficulty: Advanced.*

For \(u=-\mathrm{id}\) on \(\mathbb R^n\), \(n>0\), and constant \(F\), compare the expanding spaces \(0\) and \(\mathbb R^n\). Verify (30) without claiming their compact complexes are isomorphic.

**Solution.** Both spaces are expanding because the eigenvalue \(-1\) belongs to neither positive forbidden interval. The point space gives \(k\) in degree zero with trace one. The entire space gives \(k[-n]\). The proper pullback acts on its compact orientation generator by \(\operatorname{sgn}\det(-I)=(-1)^n\). Its alternating trace is \((-1)^n(-1)^n=1\). For \(n>0\), their nonzero cohomology occurs in different degrees, so they are not isomorphic. Equality of trace is exactly the conclusion of the quotient argument.

## Source context and the next localization theorem

The point result is the expanding case of the local contributions in Kashiwara's microlocal Lefschetz fixed-point formula for constructible sheaves. The stabilization proof above supplies the small-interval calculation directly after a proper compactification. The cutoff invokes the ordinary boundary order proved in the preceding course lesson.

For higher-dimensional fixed components, see Yuichi Ike, Yutaka Matsui and Kiyoshi Takeuchi, [Hyperbolic localization and Lefschetz fixed point formulas for higher-dimensional fixed point sets](https://arxiv.org/abs/1504.04185v2), §5. Their expanding-subbundle construction and trace functions give further context. This lesson proves the assigned point theorem with real constructible coefficients; the higher-component theorem has additional geometry and is not inferred here.

The next lesson will prove the full shrinking-space trace with its actual support maps, then deduce the complex stalk/costalk formulas and the transverse constant-sheaf sign.
